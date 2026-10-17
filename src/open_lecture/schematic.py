"""Schematic language: coordinate circuit drawings that agents write and the app renders as SVG.

One statement per line, on a grid with y pointing up:

    V1 0,3 -> 0,0 "50 V"            two-terminal element from its first to its second point
    R1 0,3 -> 3,3 "$5\\,\\Omega$" i="$i_a$"
    wire 3,3 -> 6,3 -> 6,0          polyline of plain wire
    ground 0,0

The first point of an element is its + terminal and current is measured from the first point
to the second, matching the netlist convention in CIRCUIT_LANGUAGE.md. See skills/schematic.md.
"""

import re
import shlex
import threading
from functools import lru_cache
from math import hypot

from .errors import DomainError

# schemdraw keeps the drawing being built in global state, and the API renders on a thread pool:
# without this, drawings requested together (a note page loads all of them at once) mix elements.
_render_lock = threading.Lock()

PREFIXES = [  # longest first
    ("AM", "ammeter"),
    ("VM", "voltmeter"),
    ("R", "resistor"),
    ("C", "capacitor"),
    ("L", "inductor"),
    ("V", "voltage_source"),
    ("I", "current_source"),
    ("E", "dependent_voltage_source"),
    ("H", "dependent_voltage_source"),
    ("G", "dependent_current_source"),
    ("F", "dependent_current_source"),
    ("B", "battery"),
    ("D", "diode"),
    ("S", "switch"),
    ("X", "element"),
]
POSITIONS = {"above", "below", "left", "right"}
GROUND_DIRECTIONS = {"down", "up", "left", "right"}
ELEMENT_OPTIONS = {"i", "i_rev", "v", "v_rev", "state", "action", "flip"}
MAX_LINES, MAX_COORD, MIN_LENGTH = 120, 40.0, 1.0
EPS = 1e-6
FENCE = re.compile(r"```schematic[^\n]*\n(.*?)```", re.S)
POINT = re.compile(r"^\(?(-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\)?$")
NAME = re.compile(r"^[A-Za-z][A-Za-z0-9_]{0,15}$")


def fail(line_no: int, message: str):
    raise DomainError("invalid_schematic", f"Schematic line {line_no}: {message}")


def kind_of(name: str) -> str | None:
    upper = name.upper()
    for prefix, kind in PREFIXES:
        if upper.startswith(prefix):
            return kind
    return None


def point(token: str, line_no: int) -> tuple[float, float]:
    match = POINT.match(token)
    if not match:
        fail(line_no, f"expected a point like 3,0 but found {token!r}")
    x, y = float(match[1]), float(match[2])
    if abs(x) > MAX_COORD or abs(y) > MAX_COORD:
        fail(line_no, f"point {token} is outside the ±{MAX_COORD:g} grid")
    return x, y


def path(tokens: list[str], line_no: int) -> tuple[list[tuple[float, float]], list[str]]:
    """Parse `p -> p [-> p ...]` and return the points and the remaining tokens."""
    points = [point(tokens[0], line_no)] if tokens else []
    rest = tokens[1:]
    while len(rest) >= 2 and rest[0] == "->":
        points.append(point(rest[1], line_no))
        rest = rest[2:]
    if len(points) < 2:
        fail(line_no, "expected two points joined by ->, e.g. 0,0 -> 0,3")
    return points, rest


def options(tokens: list[str], line_no: int, allowed: set[str]) -> tuple[str, dict[str, str]]:
    label, found = "", {}
    for token in tokens:
        key, eq, value = token.partition("=")
        if eq and re.fullmatch(r"[a-z_]+", key):
            if key not in allowed:
                fail(line_no, f"unknown option {key!r}; allowed: {', '.join(sorted(allowed)) or 'none'}")
            found[key] = value
        elif token in allowed:  # `flip`; a bare i or v draws an unlabelled arrow or +/- marks
            found[token] = "" if token in {"i", "i_rev", "v", "v_rev"} else "true"
        elif not label:
            label = token
        else:
            fail(line_no, f"unexpected {token!r}; quote labels that contain spaces")
    return label, found


def parse(source: str) -> dict:
    """Validate a schematic and return its statements. Raises DomainError with the line number."""
    lines = source.strip().splitlines()
    if not lines or not source.strip():
        raise DomainError("invalid_schematic", "Schematic is empty")
    if len(lines) > MAX_LINES:
        raise DomainError("invalid_schematic", f"Schematic is limited to {MAX_LINES} lines")
    items, names = [], set()
    for line_no, raw in enumerate(lines, 1):
        try:
            tokens = shlex.split(raw, comments=True, posix=True)
        except ValueError:
            fail(line_no, "unbalanced quotes")
        if not tokens:
            continue
        head, rest = tokens[0], tokens[1:]
        word = head.lower()
        if word == "wire":
            points, extra = path(rest, line_no)
            if extra:
                fail(line_no, f"wire takes only points, found {extra[0]!r}")
            items.append({"type": "wire", "points": points, "line": line_no})
        elif word == "gap":
            points, extra = path(rest, line_no)
            label, opts = options(extra, line_no, {"v", "v_rev", "flip"})
            if len(points) != 2:
                fail(line_no, "gap takes exactly two points")
            items.append({"type": "gap", "points": points, "label": label, "options": opts, "line": line_no})
        elif word in {"ground", "dot", "terminal", "label"}:
            if not rest:
                fail(line_no, f"{word} needs a point")
            at = point(rest[0], line_no)
            label, opts = "", {}
            position = None
            for token in rest[1:]:
                if token in (GROUND_DIRECTIONS if word == "ground" else POSITIONS):
                    position = token
                elif not label and word != "ground":
                    label = token
                else:
                    fail(line_no, f"unexpected {token!r}")
            if word == "label" and not label:
                fail(line_no, 'label needs text, e.g. label 3,3 "a" above')
            items.append({"type": word, "at": at, "label": label, "position": position, "line": line_no})
        else:
            kind = kind_of(head)
            if not kind or not NAME.match(head):
                fail(
                    line_no,
                    f"unknown statement {head!r}. Use wire, gap, ground, dot, terminal, label, or an element name "
                    "starting with R, C, L, V, I, E/H (dependent voltage), G/F (dependent current), B, D, S, "
                    "X (generic box), AM (ammeter) or VM (voltmeter)",
                )
            if head.upper() in names:
                fail(line_no, f"element {head} is defined twice")
            names.add(head.upper())
            points, extra = path(rest, line_no)
            if len(points) != 2:
                fail(line_no, f"{head} takes exactly two points; draw wires separately")
            label, opts = options(extra, line_no, ELEMENT_OPTIONS)
            for mark in ("i", "v"):  # `i="$i_s$" i_rev` means one reversed, labelled arrow
                if opts.get(f"{mark}_rev") == "" and mark in opts:
                    opts[f"{mark}_rev"] = opts.pop(mark)
            if opts.get("state", "open") not in {"open", "closed"}:
                fail(line_no, "state must be open or closed")
            if opts.get("action", "open") not in {"open", "close"}:
                fail(line_no, "action must be open or close (a switch that moves at t = 0)")
            (x1, y1), (x2, y2) = points
            if hypot(x2 - x1, y2 - y1) < MIN_LENGTH:
                fail(
                    line_no, f"{head} is shorter than {MIN_LENGTH:g} grid units; give it room (3 is typical)"
                )
            items.append(
                {
                    "type": "element",
                    "name": head,
                    "kind": kind,
                    "points": points,
                    "label": label,
                    "options": opts,
                    "line": line_no,
                }
            )
    if not any(item["type"] in {"element", "wire"} for item in items):
        raise DomainError("invalid_schematic", "Schematic has no elements or wires")
    return {"items": items}


def segments(items: list[dict]):
    for item in items:
        if item["type"] in {"wire", "element", "gap"}:
            pts = item["points"]
            for a, b in zip(pts, pts[1:]):
                yield item, a, b


def on_segment(p, a, b) -> bool:
    """True when p lies strictly inside segment a-b."""
    (px, py), (ax, ay), (bx, by) = p, a, b
    cross = (bx - ax) * (py - ay) - (by - ay) * (px - ax)
    if abs(cross) > EPS * max(1.0, hypot(bx - ax, by - ay)):
        return False
    dot = (px - ax) * (bx - ax) + (py - ay) * (by - ay)
    length = (bx - ax) ** 2 + (by - ay) ** 2
    return EPS < dot < length - EPS


def key(p) -> tuple[float, float]:
    return round(p[0], 4), round(p[1], 4)


def topology(source: str) -> dict:
    """Nodes and element connections implied by the drawing, for checking it against a circuit."""
    items = parse(source)["items"]
    parent: dict = {}

    def find(p):
        parent.setdefault(p, p)
        while parent[p] != p:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    def union(a, b):
        parent[find(a)] = find(b)

    endpoints = set()
    for item, a, b in segments(items):
        endpoints.update({key(a), key(b)})
        if item["type"] == "wire":
            union(key(a), key(b))
    for item in items:
        if item["type"] in {"ground", "dot", "terminal", "label"}:
            endpoints.add(key(item["at"]))
    errors, warnings = [], []
    for item, a, b in segments(items):
        for p in endpoints:
            if on_segment(p, a, b):
                if item["type"] == "wire":
                    union(p, key(a))
                elif item["type"] == "element":
                    errors.append(
                        f"line {item['line']}: point {p[0]:g},{p[1]:g} touches the middle of {item['name']}; "
                        "end the element there or move the other connection"
                    )
    for p in endpoints:
        find(p)
    names: dict = {}
    for item in items:
        root = find(key(item["at"])) if "at" in item else None
        if item["type"] == "ground":
            names[root] = "0"
        elif item["type"] in {"label", "dot", "terminal"} and item["label"] and root not in names:
            names[root] = item["label"].strip("$")
    counter = 0
    for root in sorted({find(p) for p in endpoints}):
        if root not in names:
            counter += 1
            names[root] = f"n{counter}"
    degree: dict = {}
    for item, a, b in segments(items):
        for p in (a, b):
            degree[key(p)] = degree.get(key(p), 0) + 1
        for p in endpoints:
            if item["type"] == "wire" and on_segment(p, a, b):
                degree[p] = degree.get(p, 0) + 2
    marked = {key(item["at"]) for item in items if item["type"] in {"ground", "terminal", "dot", "label"}}
    elements = []
    for item in items:
        if item["type"] != "element":
            continue
        a, b = (key(p) for p in item["points"])
        first, second = names[find(a)], names[find(b)]
        for p in (a, b):
            if degree.get(p, 0) < 2 and p not in marked:
                warnings.append(f"{item['name']} terminal at {p[0]:g},{p[1]:g} is not connected to anything")
        if first == second:
            warnings.append(f"{item['name']} has both terminals on node {first} (shorted)")
        elements.append(
            {"name": item["name"], "kind": item["kind"], "label": item["label"], "from": first, "to": second}
        )
    nodes: dict[str, list] = {}
    for p in sorted(endpoints):
        nodes.setdefault(names[find(p)], []).append(f"{p[0]:g},{p[1]:g}")
    return {"nodes": nodes, "elements": elements, "errors": errors, "warnings": warnings}


def check(source: str) -> dict:
    """Parse plus topology; raises on structural errors so documents never store a broken drawing."""
    result = topology(source)
    if result["errors"]:
        raise DomainError("invalid_schematic", "Schematic: " + "; ".join(result["errors"]))
    return result


def check_fences(text: str):
    for match in FENCE.finditer(text):
        check(match[1])


# ---------- Rendering ----------


def upright(text: str) -> str:
    """Plain text as upright math, so it uses the same (complete) font as the math."""
    escaped = re.sub(r"([#%&_{}])", r"\\\1", text).replace(" ", r"\ ")
    return f"\\mathrm{{{escaped}}}"


def math_label(text: str) -> str:
    """Labels are LaTeX when they contain $; other labels render upright in the same math font.

    Mixed labels such as `car A, $12\\,\\mathrm{V}$` become one math expression: plain text set in
    the renderer's text font loses glyphs (a lowercase c drew as a stray stroke).
    """
    if not text:
        return text
    if "$" in text:
        parts = text.split("$")
        if len(parts) % 2 == 0:  # unbalanced $: leave it for the renderer to report
            return text
        if all(not part.strip() for part in parts[::2]):
            return text
        return (
            "$"
            + "".join(upright(part) if i % 2 == 0 and part else part for i, part in enumerate(parts))
            + "$"
        )
    if re.fullmatch(r"[A-Za-z]", text):  # node names such as a, b are italic like math
        return f"${text}$"
    return f"${upright(text)}$"


@lru_cache(maxsize=256)
def render_svg(source: str) -> str:
    """Render a validated schematic to a standalone SVG (black on transparent)."""
    items = check(source) and parse(source)["items"]
    with _render_lock:
        return _draw(items)


def _draw(items: list[dict]) -> str:
    import schemdraw
    import schemdraw.elements as elm
    from schemdraw.segments import Segment

    schemdraw.use("svg")
    schemdraw.svgconfig.text = "path"  # glyphs as paths: no fonts or text injection in the SVG
    classes = {
        "resistor": elm.Resistor,
        "capacitor": elm.Capacitor,
        "inductor": elm.Inductor2,
        "voltage_source": elm.SourceV,
        "current_source": elm.SourceI,
        "dependent_voltage_source": elm.SourceControlledV,
        "dependent_current_source": elm.SourceControlledI,
        "battery": elm.BatteryCell,
        "diode": elm.Diode,
        "element": elm.RBox,
        "ammeter": elm.MeterA,
        "voltmeter": elm.MeterV,
    }
    # Sources draw + at their end point; the language puts + at the first point.
    reversed_kinds = {"voltage_source", "dependent_voltage_source", "battery"}
    degree: dict = {}
    for item, a, b in segments(items):
        if item["type"] == "gap":
            continue
        for p in (a, b):
            degree[key(p)] = degree.get(key(p), 0) + 1
    points = list(degree)
    for item, a, b in segments(items):
        if item["type"] == "wire":
            for p in points:
                if on_segment(p, a, b):
                    degree[p] += 2
    with schemdraw.Drawing(show=False) as d:
        d.config(unit=3, fontsize=14, lw=1.4)
        for item in items:
            kind = item["type"]
            if kind == "wire":
                for a, b in zip(item["points"], item["points"][1:]):
                    elm.Line().endpoints(a, b)
                continue
            if kind == "gap":
                a, b = item["points"]
                gap = elm.Gap().endpoints(a, b)
                voltage(gap, item["options"])
                continue
            if kind in {"ground", "dot", "terminal", "label"}:
                at = item["at"]
                pos = {"above": "top", "below": "bottom", "left": "left", "right": "right"}.get(
                    item["position"] or "", "top"
                )
                if kind == "ground":
                    # Ground points down at theta 0; the others rotate the symbol about its terminal.
                    turn = {"up": 180, "left": -90, "right": 90}.get(item["position"] or "down", 0)
                    elm.Ground().at(at).theta(turn)
                elif kind == "dot":
                    dot = elm.Dot().at(at)
                    if item["label"]:
                        dot.label(math_label(item["label"]), loc=pos)
                elif kind == "terminal":
                    term = elm.Dot(open=True).at(at)
                    if item["label"]:
                        term.label(math_label(item["label"]), loc=pos)
                else:
                    offset = {"top": (0, 0.45), "bottom": (0, -0.45), "left": (-0.45, 0), "right": (0.45, 0)}[
                        pos
                    ]
                    elm.Label().at((at[0] + offset[0], at[1] + offset[1])).label(math_label(item["label"]))
                continue
            a, b = item["points"]
            opts = item["options"]
            if item["kind"] == "switch":
                element = elm.Switch(action=opts.get("action"), nc=opts.get("state") == "closed").endpoints(
                    a, b
                )
            elif item["kind"] in reversed_kinds:
                element = classes[item["kind"]]().endpoints(b, a)
                if item["kind"] != "battery" and abs(b[0] - a[0]) > abs(b[1] - a[1]):
                    # schemdraw draws "-" across the axis, which reads as "|" on a horizontal source.
                    element.segments[-3] = Segment([(0.15, 0), (0.35, 0)])
            else:
                element = classes[item["kind"]]().endpoints(a, b)
            flip = opts.get("flip") == "true"
            reverse = item["kind"] in reversed_kinds
            if item["label"]:
                element.label(math_label(item["label"]), loc="bottom" if flip else "top")
            voltage(element, opts, reverse=reverse, side="top" if flip else "bottom")
            for name, back in (("i", False), ("i_rev", True)):
                if name in opts:
                    toward_end = (not back) != reverse
                    elm.CurrentLabelInline(direction="in" if toward_end else "out").at(element).label(
                        math_label(opts[name])
                    )
        for p, count in degree.items():
            if count >= 3:
                elm.Dot(radius=0.1).at(p)
    return d.get_imagedata("svg").decode()


def voltage(element, opts: dict, reverse: bool = False, side: str = "bottom"):
    for name, back in (("v", False), ("v_rev", True)):
        if name in opts:
            plus_first = (not back) != reverse
            marks = ("+", math_label(opts[name]), "−") if plus_first else ("−", math_label(opts[name]), "+")
            element.label(marks, loc=side)
