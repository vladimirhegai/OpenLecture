import re
import shlex

import numpy as np

from .errors import DomainError

PREFIXES = {"": 1, "p": 1e-12, "n": 1e-9, "u": 1e-6, "m": 1e-3, "k": 1e3, "M": 1e6, "G": 1e9}


def parse(definition: str):
    title, components, probes = None, [], []
    analysis = None
    names = set()
    for number, raw in enumerate(definition.splitlines(), 1):
        try:
            parts = shlex.split(raw, comments=True)
            if not parts:
                continue
            if parts[0] == "circuit" and len(parts) == 2 and title is None:
                title = parts[1]
                continue
            if parts[0] == "analyze":
                if parts != ["analyze", "dc"] or analysis:
                    raise ValueError("Only one 'analyze dc' directive is supported in language v1")
                analysis = "dc"
                continue
            if parts[0] == "probe" and len(parts) == 2:
                match = re.fullmatch(r"([VI])\(([A-Za-z0-9_]+)\)", parts[1])
                if not match:
                    raise ValueError("Use probe V(node) or probe I(component)")
                probes.append({"quantity": match[1], "target": match[2]})
                continue
            name = parts[0].upper()
            if not re.fullmatch(r"[RVI][A-Z0-9_]{1,30}", name):
                raise ValueError("Supported components are R (resistor), V (DC voltage), and I (DC current)")
            kind = name[0]
            if len(parts) != (4 if kind == "R" else 5) or (kind != "R" and parts[3] != "DC"):
                raise ValueError("Use Rname node+ node- valueOhm, or V/I name syntax with DC valueV/A")
            if name in names:
                raise ValueError("Component names must be unique (case-insensitive)")
            names.add(name)
            nodes = [part.lower() for part in parts[1:3]]
            if any(not re.fullmatch(r"[a-zA-Z0-9_]{1,32}", node) for node in nodes) or nodes[0] == nodes[1]:
                raise ValueError("Terminals must be distinct alphanumeric node names; ground is 0")
            unit = {"R": "Ohm", "V": "V", "I": "A"}[kind]
            match = re.fullmatch(
                r"([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)([pnumkMG]?)" + unit, parts[-1]
            )
            if not match:
                raise ValueError(f"Expected numeric value with unit {unit} (e.g. 2k{unit})")
            value = float(match[1]) * PREFIXES[match[2]]
            if not np.isfinite(value) or abs(value) > 1e12 or (kind == "R" and value < 1e-9):
                raise ValueError("Value outside supported range (resistors: 1e-9 to 1e12 Ohm)")
            components.append(
                {
                    "name": name,
                    "kind": kind,
                    "positive": nodes[0],
                    "negative": nodes[1],
                    "value": value,
                    "unit": unit,
                }
            )
        except ValueError as error:
            raise DomainError("circuit_syntax", f"Line {number}: {error}", 422, {"line": number}) from error
    nodes = sorted(
        {node for component in components for node in (component["positive"], component["negative"])}
    )
    if title is None or analysis is None or not components or "0" not in nodes:
        raise DomainError(
            "circuit_incomplete", "A circuit needs a title, components, ground 0, and analyze dc", 422
        )
    if len(components) > 100 or len(nodes) > 80:
        raise DomainError("circuit_size", "Limit: 100 components and 80 nodes", 422)
    for probe in probes:
        probe["target"] = probe["target"].lower() if probe["quantity"] == "V" else probe["target"].upper()
        if probe["target"] not in (nodes if probe["quantity"] == "V" else names):
            raise DomainError("invalid_probe", f"Unknown probe target: {probe['target']}", 422)
    return {
        "language_version": 1,
        "title": title,
        "analysis": analysis,
        "nodes": nodes,
        "components": components,
        "probes": probes,
    }


def compile_spice(circuit):
    lines = ["Open Lecture validated DC circuit"]
    for component in circuit["components"]:
        dc = "DC " if component["kind"] in {"V", "I"} else ""
        lines.append(
            f"{component['name']} {component['positive']} {component['negative']} {dc}{component['value']:.12g}"
        )
    return "\n".join([*lines, ".op", ".end", ""])


def simulate_dc(circuit):
    nodes = {name: index for index, name in enumerate(node for node in circuit["nodes"] if node != "0")}
    sources = [component for component in circuit["components"] if component["kind"] == "V"]
    size = len(nodes) + len(sources)
    matrix, rhs = np.zeros((size, size)), np.zeros(size)
    voltage_indices = {component["name"]: len(nodes) + i for i, component in enumerate(sources)}
    for component in circuit["components"]:
        a, b = nodes.get(component["positive"]), nodes.get(component["negative"])
        value, kind = component["value"], component["kind"]
        if kind == "R":
            for row, sign_r in ((a, 1), (b, -1)):
                for col, sign_c in ((a, 1), (b, -1)):
                    if row is not None and col is not None:
                        matrix[row, col] += sign_r * sign_c / value
        elif kind == "I":
            if a is not None:
                rhs[a] -= value
            if b is not None:
                rhs[b] += value
        else:
            index = voltage_indices[component["name"]]
            for node, sign in ((a, 1), (b, -1)):
                if node is not None:
                    matrix[node, index] += sign
                    matrix[index, node] += sign
            rhs[index] = value
    try:
        solution = np.linalg.solve(matrix, rhs)
    except np.linalg.LinAlgError as error:
        raise DomainError(
            "singular_circuit", "Circuit is floating or has inconsistent/redundant ideal sources", 422
        ) from error
    if not np.all(np.isfinite(solution)) or not np.allclose(matrix @ solution, rhs, rtol=1e-8, atol=1e-9):
        raise DomainError("unstable_circuit", "Circuit solution failed numerical residual checks", 422)
    voltages = {"0": 0.0, **{name: float(solution[index]) for name, index in nodes.items()}}
    currents, powers = {}, {}
    for component in circuit["components"]:
        voltage = voltages[component["positive"]] - voltages[component["negative"]]
        current = (
            voltage / component["value"]
            if component["kind"] == "R"
            else component["value"]
            if component["kind"] == "I"
            else float(solution[voltage_indices[component["name"]]])
        )
        currents[component["name"]] = current
        powers[component["name"]] = voltage * current
    return {
        "engine": "numpy_modified_nodal_analysis",
        "verified": True,
        "analysis": "dc",
        "node_voltages": voltages,
        "branch_currents": currents,
        "component_power": powers,
        "units": {"node_voltages": "V", "branch_currents": "A", "component_power": "W"},
        "current_reference": "positive terminal to negative terminal; passive sign convention",
        "power_balance_watts": sum(powers.values()),
        "max_residual": float(np.max(np.abs(matrix @ solution - rhs))),
    }
