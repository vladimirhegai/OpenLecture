# ELEC 221 Practice Problems (doc 9b25cc14-ad3c-4306-886a-81065aafc951)

`build_practice.py` builds the note from one module per problem (list `MODULES`, sections `SECTIONS`).
`--publish` replaces the course document. A module that fails its checks is left out and reported.
Check the result with `node stepshots.cjs <docId> <outDir> [--dark] [--only=<title text>]`.

## Module interface

```python
SECTION = 'B'                       # A Kirchhoff (meters, bridges, Δ–Y) · B nodal/mesh/source transf. · C Thévenin/Norton · D max power/superposition
TITLE = 'Two sources, one bridge'   # after "Problem N · ". Section B: never name the method (the reader picks it). Section C: say "Thévenin" or "Norton".
SOURCE = 'Tutorial 4, Problem 4'    # shown in italics above the statement
CITES = [...]                       # citation dicts, copied from the week-note block when reused
PROMPT = '...'                      # the statement (Markdown), without the drawing
GIVEN = '...'                       # the drawing as given (schematic language, no #@ / #~ lines)
STEPS = [(step_title, drawing, notes), ...]   # the ```circuitsteps solution
def checks(check): ...              # assert topology (check(drawing) -> ({el: (from, to)}, raw)) and ALL arithmetic
```

Template: `p1_thevenin_mesh.py`. Fence grammar: `src/open_lecture/skills/math-tools.md` (```circuitsteps).

## How the user solves (follow exactly)

- **Mesh + Ohm's law is the default.** Mesh arrow per window (`#= mesh`, cw or ccw). Put `#= sign` + where the
  mesh current **enters** each resistor. KVL = sum of the sign you **enter** each element by = 0.
  Voltage between two points: walk from + to − with the same rule (`#= path` on the wires).
- **Nodal (when it is clearly the better method):** nodes a, b, c… → V_a, V_b, V_c; ground is 0 V and unnamed.
  Draw currents toward ground (high → low) with `i=` arrows. Current = (start − end)/R. KCL: leaving −, entering +.
  Supernode: `#= region` box.
- **Source transformation:** each transformation is its own step, so the reader watches the circuit change.
- **Thévenin (template p1_thevenin_mesh.py):** pull out the load (if any) → V_Th = V_oc by mesh + Ohm, read off
  with a KVL walk (`#= path`) from + terminal to − terminal → R_Th with sources off (V → wire, I → open; the
  removed sources fade red) or, with dependent sources, a test source (1 V or 1 A) → the Thévenin circuit as its
  own drawing (V_Th in series with R_Th, terminals in the same place) → load back on, mesh + Ohm for the answer.
- **Norton (template c2_p4_64.py):** short the terminals (draw the short as a wire, `#= text` "short") →
  I_N = i_sc by mesh + Ohm (the mesh current through the short; say which way it flows, a negative I_N flips the
  arrow) → R_N with sources off or a test source → the Norton circuit as its own drawing (current source ∥ R_N,
  arrow toward a, terminals in the same place). Title starts with "Norton".
- **The course's assessment sheet uses another edition's numbering.** "Textbook AP 4.16" (p. 148) is not the
  sheet's AP 4.16. Say which in SOURCE ('Textbook Assessment Problem 4.16' vs 'Assessment Problem 4.16').
- Keep k, m, µ in the equations (2kI, (1m)(2k) = 2 V): m·k = 1.
- **Section B:** the first step's notes say which method and why, in one line.
- Every value a later step reuses goes in the "Found so far" panel: `#+ $V_{Th}=8\,\mathrm{V}$`, declared once,
  in the step that finds it (the panel carries it forward; repeats are dropped).

## Layout is automatic

`frontend/src/components/mathtools/svgLayout.ts` moves overlapping labels apart and shrinks mesh arrows that
cross labels, in every circuit (problem drawings too). Place things sensibly and let it settle the rest;
`stepshots.cjs` reports any label overlap that remains, per step.

## Style

- Every step changes the picture (something added, removed or highlighted). 6–10 steps.
- Notes: one idea per line, no paragraphs, no intro furniture, no recap. Display math on its own lines
  (`$$` / equation / `$$`); the builder rejects one-line `$$…$$`.
- Keep unchanged parts at the same grid points across steps (the diff animation depends on it), and keep the
  whole frame ≤ about 10 × 4 grid units so it fits beside the values panel.
- Final answer boxed (`\boxed{}`); the "Found so far" panel holds it too.
