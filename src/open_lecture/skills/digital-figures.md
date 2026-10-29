# Digital figures

Draw logic networks, Karnaugh maps, CMOS networks, timing diagrams, finite-state machines, and Venn diagrams as SVG in notes and chat.

Write a JSON object inside a `digital` Markdown fence, or a `code` block with `language: "digital"`.
Validate it with MCP `digital_check(source)` or `POST /api/v1/digital/check` (`{"source":"JSON..."}`).
`POST /api/v1/digital/render` returns SVG. Notes validate fences in every text field before saving.
No HTML, external URLs, executable expressions, or arbitrary SVG are accepted. Labels are plain text, not LaTeX.
Put equations and explanatory captions in the surrounding Markdown.

These are drawings, not circuit or HDL simulations. Check Boolean behavior separately with `logic_truth_table`.
Timing waves are explicitly authored samples; an edge marker does not sample a flip-flop automatically.
K-map groups are checked for the selected value, power-of-two size and Gray adjacency (including wraparound).
The checker does not prove that groups cover the entire function or that a solution has minimum cost.

## Logic circuits

```digital
{"kind":"circuit","title":"AND gate","nodes":[{"id":"A","gate":"INPUT","x":70,"y":90},{"id":"B","gate":"INPUT","x":70,"y":160},{"id":"G","gate":"AND","x":250,"y":125},{"id":"F","gate":"OUTPUT","x":430,"y":125}],"wires":[{"start":"A.out","end":"G.0"},{"start":"B.out","end":"G.1"},{"start":"G.out","end":"F.0"}]}
```

- Up to 32 nodes and 80 wires. Coordinates are 50–1150; y increases downward. Use 150–200 units between columns and 80–100 between rows.
- Node fields: `id` (unique identifier), `gate`, `x`, `y`, optional `label` (40 characters), `inputs` (1–8, default 2).
- Gates: INPUT, OUTPUT, AND, OR, NAND, NOR, XOR, XNOR, NOT, BUF, MUX, DFF, TFF, JKFF, LATCH, BLOCK.
- INPUT has no input pins. OUTPUT, NOT, BUF have one. MUX pins are 0=data0, 1=data1, 2=select. DFF/TFF/LATCH pins are data/T and clock/enable. JKFF pins are J, K, clock. The storage symbols show a positive-edge clock (`>`); label active-low and reset assumptions outside the diagram. No implicit reset pins.
- Pin names: `id.out` and `id.0`, `id.1`, ... top to bottom. Every input needs exactly one driver. Fan-out is allowed.
- Optional wire `via:[[x,y],...]` explicitly routes a polyline. Otherwise wires route orthogonally. Crossings do not define connectivity: the named endpoints do.
- BLOCK is a labeled rectangle for a functional unit; use it for a LUT, adder, decoder, or register and explain its port order nearby.

## Karnaugh maps

```digital
{"kind":"kmap","title":"Wraparound group","variables":["A","B","C","D"],"ones":[0,2,8,10],"groups":[{"cells":[0,2,8,10],"label":"B=0 and D=0"}]}
```

Variables are ordered MSB first; row variables are the first floor(n/2), columns are the rest.
2–4 variables, Gray axes 00,01,11,10. `ones` contains minterm numbers; unspecified cells are zero.
Optional `dont_cares:[...]` shows X. `target:0` groups zero cells for POS (default is 1 for SOP).
Each group needs `cells` and a plain-text `label`. Up to 12 groups. Matching coloured outlines and legends identify groups.
A group can use X but must include at least one required cell; it cannot include an opposite value.

## Timing diagrams

```digital
{"kind":"timing","title":"Rising-edge sampling","unit":"equal time intervals; ideal delay","signals":[{"name":"CLK","wave":"01010101"},{"name":"D","wave":"00110011"},{"name":"Q","wave":"00011001"}],"edges":[1,3,5,7]}
```

1–12 signals, each with a name and equal-length wave string (1–48 samples).
`0`, `1`: logic levels; `x`: unknown; `z`: high impedance; `.` repeats the preceding sample (cannot be first).
Optional `edges` highlights sample boundaries. `unit` labels the axis; state whether delays are ideal or what one interval means.
Show setup/hold violations as unknown when the actual outcome is not determined. Never draw a deterministic answer to metastability.

## State diagrams

```digital
{"kind":"fsm","title":"Moore machine","initial":"A","states":[{"id":"A","x":100,"y":150,"output":"z=0"},{"id":"B","x":330,"y":150,"output":"z=1"}],"transitions":[{"start":"A","end":"A","label":"w=0"},{"start":"A","end":"B","label":"w=1","bend":-65},{"start":"B","end":"A","label":"w=0","bend":-65},{"start":"B","end":"B","label":"w=1"}]}
```

Up to 16 states and 48 transitions. Coordinates: x>=80, y>=105, centres >=85 apart.
`initial` draws a reset arrow. Optional state `output` labels Moore outputs; use transition labels `input / output` for Mealy.
Optional `bend` (-160–160) bends an edge perpendicular to its direction. Self-loops draw above the state.
Explicitly state sampling edge, reset and overlap semantics in the note. This is a diagram checker, not an FSM completeness/minimization tool.

## CMOS

```digital
{"kind":"cmos","title":"CMOS NAND","pdn":{"series":[{"gate":"A"},{"gate":"B"}]}}
```

Supply the NMOS pull-down conduction network as a tree: `{"gate":"A"}`, `{"series":[...]}` or `{"parallel":[...]}`.
Combinations take 2–8 children; max depth 5 and max 16 NMOS leaves. The renderer constructs the dual PMOS pull-up automatically.
An NMOS leaf conducts for input 1; a PMOS leaf (bubble) conducts for input 0. The output is the complement of PDN conduction.
Only complementary static CMOS with series/parallel networks is supported. No transistor sizing, analog simulation or arbitrary pass-transistor topology.

Optional fields:

| Field | Does |
|---|---|
| `"pullup":"resistor"` | Draw a resistor-load NMOS gate (resistor instead of the PMOS network). |
| `"show":"pdn"` (or `"pun"`, `"none"`) | Draw the other half as a dashed "?" box, e.g. "derive the missing PMOS half". |
| `"inputs":{"A":1,"B":0}` | Show one row: each transistor on (green) or off (grey), the conducting path in green, and an arrow saying whether f is pulled up to 1 or down to 0 (with a resistor: whether current flows). Widens the drawing by 230 for the explanation. |
| `"output":"F"` | Output label (default `f`). |
| `"highlight":["pdn"]` | Accent colour on a half (logicsteps sets this). |

To build a CMOS gate step by step (complement → PDN → dual PUN → check a row) or let the reader try inputs, use a ```logicsteps card with cmos drawings: see math-tools.md.

## Venn diagrams

```digital
{"kind":"venn","title":"NOT(A AND B)","variables":["A","B"],"shaded":[0,1,2]}
```

Use 2 or 3 distinct variables, MSB first. `shaded` lists input-assignment indices, exactly like minterm numbers.
The rectangle is the whole universe; region 0 is outside every circle. This example shades everything except AB=11.

To walk through a circuit one gate at a time (label outputs left to right, or AND–OR → NAND–NAND), use a ```logicsteps card instead of several static figures: see math-tools.md. Circuit nodes and wires also accept `highlight: true` (accent colour) and `value: 0|1` (a bit chip on the output; wires at 1 draw green); logicsteps sets these for you.
