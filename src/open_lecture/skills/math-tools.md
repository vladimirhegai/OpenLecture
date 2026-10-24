# Math tools

Interactive math in notes: equation steppers, 2-D graphs with sliders and draggable points, and rotatable 3-D surfaces, written as fenced blocks in any Markdown text.

Each tool is a fenced code block inside Markdown text (a paragraph, a callout, a solution, a step explanation): ` ```steps `, ` ```graph `, ` ```graph3d `. The app renders them in `frontend/src/components/mathtools/`. Formulas use a small safe expression language, so nothing in a note is ever run as code. A broken fence shows a red error card naming the line. Check every tool in the browser (`scripts/notes231/toolshots.cjs <docId> <outDir>` screenshots every card and reports errors).

Use a tool when moving or stepping teaches something a static picture can't: watching an equation transform, dragging an initial condition, sliding a parameter through a threshold, turning a surface. Don't decorate. One well-chosen tool per idea beats three.

## Expressions

`+ - * /`, `^` (right-associative; `-x^2` is `-(x^2)`), parentheses, comparisons `< <= > >=` (give 1 or 0).
Constants `pi`, `e`. Functions: `sin cos tan asin acos atan atan2(y,x) sinh cosh tanh exp ln log10 sqrt cbrt abs sign floor ceil round min max hypot(a,b) mod(a,b) step(x) deg(rad) rad(deg) if(cond,a,b)`.
Multiplication is always explicit: `2*x`, not `2x`. Variables are the names below. An unknown name is an error.

## ```steps — an equation that transforms step by step

```
```steps
title "Separate, then integrate"
$$ \dfrac{dy}{dt}=t\,y $$
Start from the equation.
$$ \hl{\dfrac{1}{y}}\,dy=\hl{t}\,dt $$
Divide by $y$, multiply by $dt$.
```
```

- Each `$$ … $$` starts a step (one line, or several lines up to the closing `$$`). The lines after it, up to the next `$$`, are that step's note (Markdown, inline `$math$`).
- `\hl{…}` highlights what changed in this step. Use it on every step after the first, on the changed part only.
- The reader sees the previous line faded above the new one, clicks Next/Back (or ←/→), and can show all steps at once.
- Keep each note to one short sentence: what was done, and why if it isn't obvious. Each equation must fit the ~560 px note column; split long ones into two steps instead of using `aligned`.
- Use a stepper for derivations and the algebra of worked examples. Plain `worked_example` steps are fine for short arithmetic.

## ```graph — interactive 2-D plot

One statement per line: `kind positional… key=value… flag…`. Put tokens with spaces in double quotes. `#` starts a comment line.

| Statement | Meaning |
|---|---|
| `title "…"`, `caption "…"` | Text above / below (Markdown). |
| `x MIN MAX label="$t$" height=300` | Horizontal range (default −5..5) and label; optional plot height in px. |
| `y MIN MAX label="$y$"` | Vertical range. |
| `equal` | Same scale on both axes (complex plane, circles); the height follows from the ranges. |
| `slider NAME MIN MAX START step=S label="$k$" [animate]` | A slider; `NAME` can be used in every expression. `animate` adds a play button that sweeps it. |
| `let NAME "EXPR"` | A named value built from sliders, points and earlier lets (e.g. `let a "R/(2*L)"`), so long formulas stay readable. |
| `drag NAME X Y label="$z$" color=N snap=S` | A draggable point; expressions can use `NAME_x`, `NAME_y`. |
| `curve "EXPR" from=A to=B` | y = EXPR of `x` (or `t`, the same horizontal coordinate). `from`/`to` may use sliders. |
| `family NAME MIN MAX STEP "EXPR" from= to=` | The same curve for NAME = MIN, MIN+STEP, …, MAX (faint): a solution family. At most 60. `from`/`to` may use NAME (e.g. `from="c"` for piecewise solutions). Give it a `color=` when it sits on a grey `field`. |
| `param "X(s)" "Y(s)" S0 S1` | Parametric curve in `s`. |
| `field "F(x,y)" density=22` | Slope field of y′ = F. Grey unless `color=` is given. |
| `solution "F(x,y)" x0="P_x" y0="P_y"` | The solution of y′ = F through (x0, y0), integrated both ways (RK4) until it leaves the window. Pair with a `drag` point. |
| `level "G(x,y)" value="C"` / `values="1,2,3"` | Level curves G = value(s). |
| `region "COND(x,y)"` | Shades where COND > 0, e.g. `"y>0"`, `"(t>-1)*(t<3)"`. |
| `point "X" "Y"`, `arrow "X" "Y" x0="…" y0="…"` | A dot, or an arrow from (x0, y0) (default the origin). |
| `segment "X0" "Y0" "X1" "Y1"`, `circle "CX" "CY" "R"` | Lines and circles. |
| `hline "Y"`, `vline "X"` | Dashed reference lines (asymptotes, t = τ). |
| `text "X" "Y" "label"` | A label at a point (Markdown/LaTeX). |
| `readout "label" "EXPR" unit="°"` | A live value under the plot. |

Every drawing statement takes `label="…"` (shown in the legend), `color=1..6` (0 = grey; default: next colour) and `dash`.

```
```graph
title "Drag the starting point"
x -3 3 label="$t$"
y -3 3 label="$y$"
field "y-t"
drag P 0 0.5 label="$(t_0,y_0)$"
solution "y-t" x0="P_x" y0="P_y" label="solution through your point"
```
```

## ```graph3d — rotatable surface

| Statement | Meaning |
|---|---|
| `x MIN MAX label=`, `y MIN MAX label=`, `z MIN MAX label=` | Ranges; `z` is fitted to the surface if left out. |
| `view az=-55 el=28` | Starting angles in degrees. The reader drags to turn it. |
| `slider …` | As in `graph`. |
| `surface "F(x,y)" label="…" mesh=30` | The surface z = F, coloured by height. |
| `plane "C" label="…"` | Horizontal plane z = C. Where it cuts the surface, the level curve F = C is drawn, and its shadow on the floor. |
| `levels values="1,3,5"` | Level curves of the surface on the floor. |
| `curve3 "X(s)" "Y(s)" "Z(s)" S0 S1`, `point3 "X" "Y" "Z"` | Space curves and points (`label=`, `color=`). |

```
```graph3d
title "Solutions of an exact equation are level curves of $F$"
z -1 8 label="$F$"
slider C 0 7 3 label="$C$"
surface "x^2+x*y+y^2" label="$F=x^2+xy+y^2$"
plane "C" label="the curve $F=C$"
```
```

## Writing them from Python

The ELEC 231 builder (`scripts/notes231/lib231.py`) has `D.STEPS(title, [(latex, note), …])`, `D.GRAPH(lines)` and `D.GRAPH3D(lines)`. Write builder files with the Write tool, never through a shell heredoc, because heredocs collapse `\\` in LaTeX.

## ```circuitsteps — a circuit that transforms step by step

For circuit solutions (mesh, nodal, supernode/supermesh, Thévenin/Norton, superposition, max power): each step is a whole drawing plus notes. The reader clicks Next; parts that appear fade in and stay blue for that step, parts that disappear flash red and fade out, and new overlays draw themselves in. All steps share one frame, so keep unchanged parts at the same grid points.

```
```circuitsteps
title "Find $V_o$: Thévenin with mesh + Ohm's law"
== Pull out the load
R1 0,3 -> 0,0 "$2\,\mathrm{k\Omega}$"
...schematic statements (no #@ / #~ needed)...
#= mesh 1.5,1.5 "$I_1$" ccw r=0.75
--
Notes for this step: Markdown, lists, $math$, and display math as
$$
6kI_1=6
$$
== next step ...
```
```

Overlays (`#=` lines, grid points; each takes `color=purple|pink|blue|green|orange|accent`):

| Statement | Draws |
|---|---|
| `#= mesh CX,CY "$I_1$" cw\|ccw r=0.9` | Mesh-current loop arrow (purple), name in the middle. |
| `#= path X,Y -> X,Y -> ... "label" [thin]` | Arrow along wires (pink, translucent): a KVL walk or where a current flows. Draw it ON the wires. |
| `#= sign X,Y +\|-` | Polarity box (+ blue, − pink), e.g. where a mesh current enters a resistor. |
| `#= text X,Y "$2\,\mathrm{V}$"` | Callout centred on the point (Ohm's-law results, node voltages). |
| `#= region X0,Y0 X1,Y1 "supernode"` | Dashed box: supernode, supermesh, the part being replaced. |

**Values found:** a `#+ $I_1=1\,\mathrm{mA}$` line in a step's drawing adds that value to the "Found so far" panel beside the circuit, from that step on (highlighted in the step that finds it). Add one for every value a later step reuses.

The card is as tall as its longest step (every title and note shares one grid cell), so Next never moves the page.

Write display math in notes on its own lines (`$$` / equation / `$$`): a one-line `$$…$$` renders inline-sized. Builder and checks: `scripts/practice221/` (`build_practice.py`, one module per problem, `stepshots.cjs <docId> <out> [--dark] [--mid]`).
