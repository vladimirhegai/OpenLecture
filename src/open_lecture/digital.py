"""Bounded, deterministic SVG figures for digital-systems notes and chat.

The JSON `digital` fence supports circuit, kmap, timing, fsm, cmos, and venn.
No arbitrary SVG, JavaScript, expressions, or external resources are accepted.
"""

import math
import re
from functools import lru_cache
from html import escape
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, TypeAdapter, ValidationError, model_validator

from .errors import DomainError

FENCE = re.compile(r"```digital[^\n]*\n(.*?)```", re.S)
Name = Annotated[str, Field(pattern=r"^[A-Za-z][A-Za-z0-9_]{0,15}$")]
Label = Annotated[str, Field(min_length=1, max_length=40)]
Coord = Annotated[float, Field(ge=50, le=1150)]


class Model(BaseModel):
    model_config = ConfigDict(extra="forbid", allow_inf_nan=False)


class Node(Model):
    id: Name
    gate: Literal[
        "INPUT",
        "OUTPUT",
        "AND",
        "OR",
        "NOT",
        "BUF",
        "NAND",
        "NOR",
        "XOR",
        "XNOR",
        "MUX",
        "DFF",
        "TFF",
        "JKFF",
        "LATCH",
        "BLOCK",
    ]
    x: Coord
    y: Coord
    label: str = Field(default="", max_length=40)
    inputs: int = Field(default=2, ge=0, le=8)

    @model_validator(mode="after")
    def pins(self):
        if self.gate in {"NOT", "BUF", "OUTPUT"}:
            self.inputs = 1
        elif self.gate in {"MUX", "DFF", "TFF", "LATCH"}:
            self.inputs = 2 if self.gate != "MUX" else 3
        elif self.gate == "JKFF":
            self.inputs = 3
        elif self.gate == "INPUT":
            self.inputs = 0
        if self.gate != "INPUT" and self.inputs == 0:
            raise ValueError("A gate needs at least one input")
        return self


class Wire(Model):
    start: str = Field(max_length=25)
    end: str = Field(max_length=25)
    via: list[tuple[Coord, Coord]] = Field(default_factory=list, max_length=8)


class Circuit(Model):
    kind: Literal["circuit"]
    title: Label = "Logic circuit"
    nodes: list[Node] = Field(min_length=1, max_length=32)
    wires: list[Wire] = Field(default_factory=list, max_length=80)

    @model_validator(mode="after")
    def connections(self):
        nodes = {n.id: n for n in self.nodes}
        if len(nodes) != len(self.nodes):
            raise ValueError("Node IDs must be unique")
        if any(n.gate not in {"INPUT", "OUTPUT"} and n.y < max(25, n.inputs * 11) + 30 for n in self.nodes):
            raise ValueError("Move gates down to leave room for their inputs and labels")
        driven = set()
        for w in self.wires:
            for ref, output in ((w.start, True), (w.end, False)):
                name, _, pin = ref.partition(".")
                if name not in nodes:
                    raise ValueError(f"Unknown node {name}")
                node = nodes[name]
                valid = (
                    pin == "out" and node.gate != "OUTPUT"
                    if output
                    else (pin.isdigit() and int(pin) < node.inputs)
                )
                if not valid:
                    raise ValueError(f"Invalid {'output' if output else 'input'} pin: {ref}")
            if w.end in driven:
                raise ValueError(f"Multiple drivers on {w.end}")
            driven.add(w.end)
        for n in self.nodes:
            for i in range(n.inputs):
                if f"{n.id}.{i}" not in driven:
                    raise ValueError(f"Unconnected input {n.id}.{i}")
        return self


class Group(Model):
    cells: list[int] = Field(min_length=1, max_length=16)
    label: Label


class KMap(Model):
    kind: Literal["kmap"]
    title: Label = "Karnaugh map"
    variables: list[Name] = Field(min_length=2, max_length=4)
    ones: list[int] = Field(default_factory=list, max_length=16)
    dont_cares: list[int] = Field(default_factory=list, max_length=16)
    target: Literal[0, 1] = 1
    groups: list[Group] = Field(default_factory=list, max_length=12)

    @model_validator(mode="after")
    def cells(self):
        if len(set(self.variables)) != len(self.variables):
            raise ValueError("Variables must be distinct")
        size = 2 ** len(self.variables)
        if set(self.ones) & set(self.dont_cares):
            raise ValueError("Ones and don't-cares overlap")
        if any(v < 0 or v >= size for v in self.ones + self.dont_cares):
            raise ValueError("Minterm outside the map")
        order = gray_order(len(self.variables))
        rows, cols = len(order), len(order[0])
        for g in self.groups:
            cells = set(g.cells)
            if len(cells) != len(g.cells) or len(cells) not in {1, 2, 4, 8, 16}:
                raise ValueError("A group needs a power of two distinct cells")
            eligible = (set(self.ones) if self.target else set(range(size)) - set(self.ones)) | set(
                self.dont_cares
            )
            if not cells <= eligible or not cells - set(self.dont_cares):
                raise ValueError("Group contains an opposite value or only don't-cares")
            rectangles = []
            for h in (1, 2, 4):
                for w in (1, 2, 4):
                    if h > rows or w > cols or h * w != len(cells):
                        continue
                    for r in range(rows):
                        for c in range(cols):
                            rectangles.append(
                                {order[(r + i) % rows][(c + j) % cols] for i in range(h) for j in range(w)}
                            )
            if cells not in rectangles:
                raise ValueError("Group must be a Gray-adjacent rectangle, allowing wraparound")
        return self


class Signal(Model):
    name: Label
    wave: str = Field(min_length=1, max_length=48, pattern=r"^[01xz.]+$")


class Timing(Model):
    kind: Literal["timing"]
    title: Label = "Timing diagram"
    signals: list[Signal] = Field(min_length=1, max_length=12)
    unit: str = Field(default="interval", min_length=1, max_length=90)
    edges: list[int] = Field(default_factory=list, max_length=48)

    @model_validator(mode="after")
    def aligned(self):
        n = len(self.signals[0].wave)
        if any(len(s.wave) != n or s.wave.startswith(".") for s in self.signals):
            raise ValueError("Waves must have equal lengths and start with 0, 1, x or z")
        if any(e < 0 or e >= n for e in self.edges):
            raise ValueError("Edge marker is outside the diagram")
        return self


class State(Model):
    id: Name
    x: Coord
    y: Coord
    output: str = Field(default="", max_length=20)


class Transition(Model):
    start: Name
    end: Name
    label: Label
    bend: float = Field(default=0, ge=-160, le=160)


class FSM(Model):
    kind: Literal["fsm"]
    title: Label = "State diagram"
    states: list[State] = Field(min_length=1, max_length=16)
    transitions: list[Transition] = Field(default_factory=list, max_length=48)
    initial: Name

    @model_validator(mode="after")
    def references(self):
        ids = {s.id for s in self.states}
        if len(ids) != len(self.states) or self.initial not in ids:
            raise ValueError("States need unique IDs and an existing initial state")
        if any(t.start not in ids or t.end not in ids for t in self.transitions):
            raise ValueError("Transition refers to an unknown state")
        for a in self.states:
            if a.y < 105 or a.x < 80:
                raise ValueError("States need x >= 80 and y >= 105 for labels and reset arrows")
            if any(a.id != b.id and math.hypot(a.x - b.x, a.y - b.y) < 85 for b in self.states):
                raise ValueError("State centres must be at least 85 units apart")
        return self


class Network(Model):
    """A labelled transistor leaf or a series/parallel combination."""

    gate: Name | None = None
    series: list["Network"] | None = Field(default=None, min_length=2, max_length=8)
    parallel: list["Network"] | None = Field(default=None, min_length=2, max_length=8)

    @model_validator(mode="after")
    def one_kind(self):
        if sum(v is not None for v in (self.gate, self.series, self.parallel)) != 1:
            raise ValueError("Use exactly one of gate, series, parallel")
        return self


class CMOS(Model):
    kind: Literal["cmos"]
    title: Label = "CMOS network"
    pdn: Network

    @model_validator(mode="after")
    def bounded(self):
        def count(n, depth=0):
            if depth > 5:
                raise ValueError("CMOS network is too deep")
            return 1 if n.gate else sum(count(c, depth + 1) for c in n.series or n.parallel)

        if count(self.pdn) > 16:
            raise ValueError("CMOS network is limited to 16 NMOS transistors")
        return self


class Venn(Model):
    kind: Literal["venn"]
    title: Label = "Venn diagram"
    variables: list[Name] = Field(min_length=2, max_length=3)
    shaded: list[int] = Field(default_factory=list, max_length=8)

    @model_validator(mode="after")
    def regions(self):
        if len(set(self.variables)) != len(self.variables):
            raise ValueError("Variables must be distinct")
        if any(i < 0 or i >= 2 ** len(self.variables) for i in self.shaded):
            raise ValueError("Shaded region is outside the diagram")
        return self


Figure = Annotated[Circuit | KMap | Timing | FSM | CMOS | Venn, Field(discriminator="kind")]
ADAPTER = TypeAdapter(Figure)


def parse(source: str):
    if len(source) > 30000:
        raise DomainError("invalid_digital", "Digital figure is limited to 30000 characters")
    try:
        return ADAPTER.validate_json(source)
    except (ValidationError, ValueError, RecursionError) as error:
        message = str(error)[:1200]
        raise DomainError("invalid_digital", f"Invalid digital figure: {message}") from None


def check(source: str) -> dict:
    figure = parse(source)
    return {"kind": figure.kind, "figure": figure.model_dump(exclude_none=True)}


def check_fences(text: str):
    for match in FENCE.finditer(text):
        parse(match[1])


def gray_order(n):
    rb = n // 2
    cb = n - rb
    return [[((r ^ (r >> 1)) << cb) | (c ^ (c >> 1)) for c in range(2**cb)] for r in range(2**rb)]


class SVG:
    def __init__(self, width, height, title):
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:g} {height:g}" '
            f'role="img" aria-labelledby="title"><title id="title">{escape(title)}</title>',
            '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" '
            'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            '<path d="M0 0 L10 5 L0 10 Z" fill="#334155"/></marker></defs>',
            '<rect width="100%" height="100%" fill="#fff"/>',
            '<g stroke="#334155" stroke-width="2" stroke-linejoin="round" fill="none">',
        ]

    def add(self, s):
        self.parts.append(s)

    def line(self, x, y, xx, yy, **attrs):
        self.add(f'<path d="M{x:g},{y:g} L{xx:g},{yy:g}" {attributes(attrs)}/>')

    def text(self, x, y, text, size=16, anchor="middle", color="#0f172a"):
        self.add(
            f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}" font-family="Arial,sans-serif" '
            f'font-size="{size}" stroke="none" fill="{color}">{escape(str(text))}</text>'
        )

    def circle(self, x, y, radius, **attrs):
        self.add(f'<circle cx="{x:g}" cy="{y:g}" r="{radius:g}" {attributes(attrs)}/>')

    def finish(self):
        return "".join(self.parts) + "</g></svg>"


def attributes(attrs):
    return " ".join(f'{k.replace("_", "-")}="{escape(str(v), quote=True)}"' for k, v in attrs.items())


def pin(node, number=None):
    if number is None:
        return node.x + 48, node.y
    return node.x - 48, node.y + (number - (node.inputs - 1) / 2) * 20


def circuit_svg(f):
    width = max(n.x for n in f.nodes) + 120
    height = max(n.y + max(50, n.inputs * 11) for n in f.nodes) + 45
    svg = SVG(width, height, f.title)
    nodes = {n.id: n for n in f.nodes}
    # Draw wires first. Explicit endpoints define connectivity; crossings are not junctions.
    for w in f.wires:
        a, _, _ = w.start.partition(".")
        b, _, p = w.end.partition(".")
        x, y = pin(nodes[a])
        xx, yy = pin(nodes[b], int(p))
        via = w.via or [((x + xx) / 2, y), ((x + xx) / 2, yy)]
        points = [(x, y), *via, (xx, yy)]
        svg.add('<polyline points="' + " ".join(f"{px:g},{py:g}" for px, py in points) + '"/>')
    for n in f.nodes:
        x, y, gate = n.x, n.y, n.gate
        h = max(25, n.inputs * 11)
        if gate == "INPUT":
            svg.line(x - 32, y, x + 48, y)
            svg.text(x, y - 12, n.label or n.id)
            continue
        if gate == "OUTPUT":
            svg.line(x - 48, y, x + 15, y)
            svg.text(x, y - 12, n.label or n.id)
            continue
        for i in range(n.inputs):
            px, py = pin(n, i)
            svg.line(px, py, x - 10, py)
        svg.line(x + 29, y, x + 48, y)
        if gate in {"AND", "NAND"}:
            d = f"M{x - 28},{y - h} L{x},{y - h} C{x + 43},{y - h} {x + 43},{y + h} {x},{y + h} L{x - 28},{y + h} Z"
            svg.add(f'<path d="{d}" fill="#f8fafc"/>')
        elif gate in {"OR", "NOR", "XOR", "XNOR"}:
            d = (
                f"M{x - 30},{y - h} Q{x + 8},{y - h} {x + 35},{y} Q{x + 8},{y + h} {x - 30},{y + h} "
                f"Q{x - 10},{y} {x - 30},{y - h} Z"
            )
            svg.add(f'<path d="{d}" fill="#f8fafc"/>')
            if gate in {"XOR", "XNOR"}:
                svg.add(f'<path d="M{x - 37},{y - h} Q{x - 17},{y} {x - 37},{y + h}"/>')
        elif gate in {"NOT", "BUF"}:
            svg.add(f'<path d="M{x - 28},{y - 24} L{x + 29},{y} L{x - 28},{y + 24} Z" fill="#f8fafc"/>')
        else:
            svg.add(
                f'<rect x="{x - 28}" y="{y - h - 5}" width="63" height="{2 * h + 10}" rx="4" fill="#eff6ff"/>'
            )
            svg.text(x + 4, y - h - 15, n.label or n.id, 14)
            labels = {
                "MUX": ["0", "1", "S"],
                "DFF": ["D", ">"],
                "TFF": ["T", ">"],
                "JKFF": ["J", "K", ">"],
                "LATCH": ["D", "EN"],
            }.get(gate)
            if labels:
                for i, label in enumerate(labels):
                    _, py = pin(n, i)
                    svg.text(x - 21, py + 5, label, 12, "start")
                svg.text(x + 26, y + 5, "Y" if gate == "MUX" else "Q", 12, "end")
            else:
                svg.text(x + 4, y + 5, n.label or n.id, 12)
        if gate in {"NOT", "NAND", "NOR", "XNOR"}:
            svg.circle(x + 35, y, 5, fill="white")
        if gate not in {"MUX", "DFF", "TFF", "JKFF", "LATCH", "BLOCK"}:
            svg.text(x, y - h - 12, n.label or n.id, 14)
    return svg.finish()


COLORS = ["#2563eb", "#dc2626", "#059669", "#9333ea", "#d97706", "#0891b2"]


def kmap_svg(f):
    order = gray_order(len(f.variables))
    rows, cols = len(order), len(order[0])
    svg = SVG(130 + cols * 85, 150 + rows * 68 + len(f.groups) * 23, f.title)
    rb = len(f.variables) // 2
    svg.text(92, 30, "".join(f.variables[rb:]), anchor="start")
    svg.text(65, 59, "".join(f.variables[:rb]), size=14)
    for c in range(cols):
        svg.text(130 + c * 85, 59, format(c ^ (c >> 1), f"0{len(f.variables) - rb}b"))
    for r, row in enumerate(order):
        svg.text(65, 100 + r * 68, format(r ^ (r >> 1), f"0{rb}b"))
        for c, m in enumerate(row):
            x, y = 90 + c * 85, 70 + r * 68
            svg.add(f'<rect x="{x}" y="{y}" width="85" height="68" fill="#f8fafc" stroke="#cbd5e1"/>')
            svg.text(x + 9, y + 16, m, 11, "start", "#64748b")
            svg.text(x + 43, y + 43, "X" if m in f.dont_cares else int(m in f.ones), 22)
            for i, g in enumerate(f.groups):
                if m not in g.cells:
                    continue
                # Same-colour open edges join adjacent cells; edge fragments show wraparound.
                inset = 5 + (i % 3) * 4
                color = COLORS[i % len(COLORS)]
                for dr, dc, side in ((-1, 0, "t"), (1, 0, "b"), (0, -1, "l"), (0, 1, "r")):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and order[nr][nc] in g.cells:
                        continue
                    if side == "t":
                        svg.line(
                            x + inset, y + inset, x + 85 - inset, y + inset, stroke=color, stroke_width=3
                        )
                    elif side == "b":
                        svg.line(
                            x + inset,
                            y + 68 - inset,
                            x + 85 - inset,
                            y + 68 - inset,
                            stroke=color,
                            stroke_width=3,
                        )
                    elif side == "l":
                        svg.line(
                            x + inset, y + inset, x + inset, y + 68 - inset, stroke=color, stroke_width=3
                        )
                    else:
                        svg.line(
                            x + 85 - inset,
                            y + inset,
                            x + 85 - inset,
                            y + 68 - inset,
                            stroke=color,
                            stroke_width=3,
                        )
    for i, g in enumerate(f.groups):
        svg.text(90, 105 + rows * 68 + i * 23, g.label, 15, "start", COLORS[i % len(COLORS)])
    return svg.finish()


def timing_svg(f):
    n = len(f.signals[0].wave)
    step = max(12, min(65, 640 / n))
    gutter = max(110, max(len(s.name) for s in f.signals) * 8 + 20)
    width, height = gutter + 35 + n * step, 90 + len(f.signals) * 60
    svg = SVG(width, height, f.title)
    for i in range(n + 1):
        x = gutter + i * step
        svg.line(x, 30, x, height - 45, stroke="#e2e8f0", stroke_width=1)
        if n <= 20 or i % 2 == 0:
            svg.text(x, height - 23, i, 12, color="#64748b")
    for e in f.edges:
        x = gutter + e * step
        svg.line(x, 25, x, height - 45, stroke="#d97706", stroke_dasharray="4 4")
    for row, signal in enumerate(f.signals):
        y = 50 + row * 60
        svg.text(gutter - 15, y + 6, signal.name, 15, "end")
        last = None
        for i, value in enumerate(signal.wave):
            value = last if value == "." else value
            x = gutter + i * step
            level = y - 13 if value == "1" else y + 13 if value == "0" else y
            if i and value != last:
                old_y = y - 13 if last == "1" else y + 13 if last == "0" else y
                svg.line(x, old_y, x, level, stroke="#2563eb")
            svg.line(
                x,
                level,
                x + step,
                level,
                stroke="#2563eb",
                stroke_dasharray="4 3" if value in "xz" else "none",
            )
            if value == "x":
                svg.text(x + step / 2, y - 5, "X", 11)
            elif value == "z":
                svg.text(x + step / 2, y - 5, "Z", 11)
            last = value
    svg.text(width / 2, height - 3, f.unit, 13)
    return svg.finish()


def fsm_svg(f):
    svg = SVG(max(s.x for s in f.states) + 100, max(s.y for s in f.states) + 100, f.title)
    nodes = {s.id: s for s in f.states}
    for t in f.transitions:
        a, b = nodes[t.start], nodes[t.end]
        if a.id == b.id:
            d = f"M{a.x - 22},{a.y - 23} C{a.x - 80},{a.y - 100} {a.x + 80},{a.y - 100} {a.x + 22},{a.y - 23}"
            tx, ty = a.x, a.y - 83
        else:
            dx, dy = b.x - a.x, b.y - a.y
            length = math.hypot(dx, dy)
            if length < 85:
                raise DomainError("invalid_digital", "State centres must be at least 85 units apart")
            ux, uy = dx / length, dy / length
            mx, my = (a.x + b.x) / 2 - uy * t.bend, (a.y + b.y) / 2 + ux * t.bend
            # Endpoints follow the control point so curved arrows meet the circle boundary.
            al, bl = math.hypot(mx - a.x, my - a.y), math.hypot(mx - b.x, my - b.y)
            ax, ay = a.x + 34 * (mx - a.x) / al, a.y + 34 * (my - a.y) / al
            bx, by = b.x + 36 * (mx - b.x) / bl, b.y + 36 * (my - b.y) / bl
            d = f"M{ax},{ay} Q{mx},{my} {bx},{by}"
            tx, ty = (ax + 2 * mx + bx) / 4, (ay + 2 * my + by) / 4 - 8
        svg.add(f'<path d="{d}" marker-end="url(#arrow)"/>')
        svg.text(tx, ty, t.label, 14)
    for s in f.states:
        svg.circle(s.x, s.y, 33, fill="#eff6ff")
        svg.text(s.x, s.y - 3 if s.output else s.y + 5, s.id)
        if s.output:
            svg.text(s.x, s.y + 17, s.output, 13)
        if s.id == f.initial:
            svg.line(s.x - 72, s.y, s.x - 35, s.y, marker_end="url(#arrow)")
            svg.text(s.x - 70, s.y - 9, "reset", 11)
    return svg.finish()


def dual(n):
    if n.gate:
        return n
    return Network(**{"parallel" if n.series else "series": [dual(c) for c in n.series or n.parallel]})


def dimensions(n):
    if n.gate:
        return max(110, len(n.gate) * 16 + 60), 70
    sizes = [dimensions(c) for c in n.series or n.parallel]
    return (
        (max(w for w, h in sizes), sum(h for w, h in sizes))
        if n.series
        else (sum(w for w, h in sizes), max(h for w, h in sizes) + 30)
    )


def cmos_svg(f):
    pun = dual(f.pdn)
    pw, ph = dimensions(pun)
    nw, nh = dimensions(f.pdn)
    width = max(pw, nw) + 140
    height = ph + nh + 160
    svg = SVG(width, height, f.title)
    cx = width / 2

    def draw(n, x, y, w, h, pmos):
        mid = x + w / 2
        if n.gate:
            sy = y + h / 2
            svg.line(mid, y, mid, sy - 14)
            svg.line(mid, sy - 14, mid - 10, sy - 14)
            svg.line(mid - 10, sy - 14, mid - 10, sy + 14)
            svg.line(mid - 10, sy + 14, mid, sy + 14)
            svg.line(mid, sy + 14, mid, y + h)
            svg.line(mid - 19, sy - 17, mid - 19, sy + 17)
            svg.line(mid - 38, sy, mid - 25 if pmos else mid - 19, sy)
            if pmos:
                svg.circle(mid - 23, sy, 4, fill="white")
            svg.text(mid - 41, sy + 5, n.gate, 14, "end")
        elif n.series:
            total = sum(dimensions(c)[1] for c in n.series)
            yy = y
            for c in n.series:
                ch = h * dimensions(c)[1] / total
                draw(c, x, yy, w, ch, pmos)
                yy += ch
        else:
            xx = x
            total = sum(dimensions(c)[0] for c in n.parallel)
            svg.line(mid, y, mid, y + 15)
            svg.line(mid, y + h - 15, mid, y + h)
            for c in n.parallel:
                cw = w * dimensions(c)[0] / total
                cc = xx + cw / 2
                svg.line(mid, y + 15, cc, y + 15)
                svg.line(mid, y + h - 15, cc, y + h - 15)
                draw(c, xx, y + 15, cw, h - 30, pmos)
                xx += cw

    svg.text(cx, 24, "VDD")
    svg.line(cx, 30, cx, 45)
    draw(pun, (width - pw) / 2, 45, pw, ph, True)
    out_y = 70 + ph
    svg.line(cx, 45 + ph, cx, 95 + ph)
    svg.line(cx, out_y, width - 28, out_y)
    svg.circle(cx, out_y, 3, fill="#334155")
    svg.text(width - 25, out_y - 8, "f")
    draw(f.pdn, (width - nw) / 2, 95 + ph, nw, nh, False)
    bottom = 95 + ph + nh
    svg.line(cx, bottom, cx, bottom + 15)
    for i in range(3):
        svg.line(cx - 16 + i * 5, bottom + 15 + i * 6, cx + 16 - i * 5, bottom + 15 + i * 6)
    svg.text(12, 50, "PUN", 13, "start", "#2563eb")
    svg.text(12, 100 + ph, "PDN", 13, "start", "#dc2626")
    return svg.finish()


def venn_svg(f):
    svg = SVG(420, 340, f.title)
    centres = [(160, 150), (260, 150)] if len(f.variables) == 2 else [(165, 125), (255, 125), (210, 205)]
    r = 80
    for i, (x, y) in enumerate(centres):
        svg.add(
            f'<defs><clipPath id="inside{i}"><circle cx="{x}" cy="{y}" r="{r}"/></clipPath>'
            f'<mask id="outside{i}"><rect width="420" height="340" fill="white"/>'
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="black"/></mask></defs>'
        )
    for m in sorted(set(f.shaded)):
        for i in range(len(centres)):
            inside = bool(m & (1 << (len(centres) - 1 - i)))
            svg.add(f'<g {"clip-path" if inside else "mask"}="url(#{"inside" if inside else "outside"}{i})">')
        svg.add('<rect x="40" y="25" width="340" height="280" fill="#bfdbfe" stroke="none"/>')
        svg.add("</g>" * len(centres))
    svg.add('<rect x="40" y="25" width="340" height="280" stroke="#64748b"/>')
    for i, (x, y) in enumerate(centres):
        svg.circle(x, y, r)
        svg.text(x + (-35 if i == 0 else 35 if i == 1 else 0), y + (-45 if i < 2 else 50), f.variables[i], 18)
    svg.text(
        210,
        329,
        "Shaded assignments: " + ", ".join(format(m, f"0{len(centres)}b") for m in sorted(set(f.shaded))),
        13,
    )
    return svg.finish()


@lru_cache(maxsize=128)
def render_svg(source: str) -> str:
    f = parse(source)
    return {
        "circuit": circuit_svg,
        "kmap": kmap_svg,
        "timing": timing_svg,
        "fsm": fsm_svg,
        "cmos": cmos_svg,
        "venn": venn_svg,
    }[f.kind](f)
