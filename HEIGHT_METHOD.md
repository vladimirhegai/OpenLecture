# The Height Method (also called the river method)

This is the owner's main way of solving circuits, and every ELEC 221 week note is built around it. Read this before you explain a circuit, write a note, or add a height view. It covers three things: what the method is (so you can teach it), how a height view is written and rendered in this app, and the house rules the owner has asked for.

Other places to look:

- `notes/The-Height-Method-Complete-Guide.md` is the student-facing guide, with worked height views for Weeks 1–6. In the app it is the note "The Height Method: Complete Guide".
- `src/open_lecture/skills/schematic.md`, section "Height views", has the full `#@` grammar and the correctness rules.
- `frontend/src/components/Elevation.tsx` is the renderer. Its header comment repeats the grammar.
- `scripts/height_notes/` is the toolkit that generates views from a solver (see [Pipeline](#pipeline)).

## 1. The idea

Pick one node as **ground** and call it 0 V. Every other node's voltage is its **height** above ground, so a circuit becomes a landscape:

- **Sources lift** charge up.
- **Resistors let it slide down**, like a river running downhill. That picture is where the name "river method" comes from, and the app's optional "Straight line" view draws it literally: one supply rail on top and the current falling through the loads.
- A voltage is just a **height difference**, and power is **current × height change**.

KVL and KCL become things you can see:

- **KVL:** every node has exactly one height, so any walk around a loop ends at the height it started from. In other words, total climbs = total falls.
- **KCL:** the current arriving at a level equals the current leaving it.
- **Power:** current climbing through an element means the element delivers energy (green ▲). Current falling through it means the element absorbs energy (orange ▼). Total climbs × current = total falls × current.
- **Downhill is a resistor-only rule.** Sources, capacitors and inductors can carry current uphill, and that is exactly when they deliver energy.

## 2. Elements as pictures

| Element | Picture | Fixes | Leaves free |
|---|---|---|---|
| Wire, closed switch, ideal ammeter | Flat (one level) | No step | Any current |
| Resistor | A slope ("slide") | Current always runs downhill; fall = iR | — |
| Voltage source / battery | A **rigid step**: + end higher by V | The step | Any current, either way |
| Current source | A **stretchy step** ("lift/pump") | The current | Its step: whatever the circuit needs, even negative |
| Dependent V / I source | Rigid / stretchy step sized by its controller | Read the controller off the picture first | Same as above |
| Open switch, ideal voltmeter | A **gap** | No current | Spans whatever step is left over |
| Capacitor (W6) | A **held step** v_C (can't jump) | — | DC steady state: a gap |
| Inductor (W6) | A **held current** i_L (can't jump) | — | DC steady state: flat |
| Ground | The 0 level | Any node can be ground; moving it shifts every height equally and changes no answer | — |

## 3. The recipe (every walkthrough uses this order)

1. **Keep the given ground.** The first step of every walkthrough names ground. Preserve the original circuit's 0 V reference and draw negative voltages below it; the owner explicitly prefers this to shifting ground to the lowest node.
2. **Place the fixed heights.** Step across each voltage source from a known height.
3. **Find currents.** A current source fixes its current, never its step. A resistor carries fall ÷ R, downhill. Use KCL where branches meet.
4. **Place the rest.** Walk down each resistor by iR in the current's direction.
5. **Use the picture to simplify the unknowns.** Follow fixed source currents, combine parallel slides, and express branch flows with one unknown current when possible. Turn the flows into falls with iR, then walk two paths to the same node and equate their total falls. This is the preferred Week 1–2 teaching style. If that does not simplify a coupled circuit, name the unknown heights and write in = out at each.
6. **Answer and check.** Each node must have one height (KVL), the currents must balance at every node (KCL), and the climbs must equal the falls (power).

**Starting the drawing:** distinguish a trial sketch from the solved height view. Place voltage-source separations first; leave other heights unknown. Choose provisional resistor-current arrows and use signed iR steps. A negative current reverses the guessed flow and corrects the level order. When teaching how to draw the view, show an explicitly illustrative trial tab before the solved tab rather than requiring the final order in advance.

### Worked example

A 12 V source feeds 2 Ω, then node m, then 6 Ω and 3 Ω in parallel down to ground.

1. Ground the source's − end. The + end is at 12 V.
2. Below m the two resistors sit side by side: 6 ∥ 3 = 2 Ω. The total is 4 Ω, so the source lifts 12/4 = **3 A**.
3. The 2 Ω falls (3)(2) = 6 V, so **m = 6 V**.
4. Both lower resistors fall the same 6 V, so the river splits: 6/6 = **1 A** and 6/3 = **2 A** (1 + 2 = 3 ✓ KCL).
5. Power: the source climbs 3 A × 12 V = 36 W. The falls are 3 × 6 + 1 × 6 + 2 × 6 = 18 + 6 + 12 = 36 W ✓.

## 4. Week-by-week extensions (ELEC 221)

- **W1:** an element absorbs when current falls through it and delivers when current climbs. A voltage v with + at a and − at b equals height(a) − height(b), which is negative when the + end is lower. A connection is invalid if some node would need two heights. A node joined only through current sources floats (no unique answer).
- **W2:** **series** elements stack in one column and share one current. **Parallel** elements span the same two levels side by side and share one fall. A **divider** midpoint sits R₂/(R₁+R₂) of the way up the slope. A **load** is a second way down, so the midpoint **sags**. A **bridge** is balanced when its two midpoints are level, so the detector lies flat. **Δ–Y** keeps the three terminal heights.
- **W3:** node voltages *are* heights. **Averaging rule:** a node joined only by resistors sits at the conductance-weighted average of its neighbours, plus a lift for any injected current: v = (ΣGⱼvⱼ + I_in)/ΣGⱼ. **Supernode:** a voltage source between two unknown nodes is a **rigid rod**, and KCL around the rod pins it. **Mesh currents have no height.** Show only the real branch currents.
- **W4:** **Thévenin** is one step V_Th, then one slope R_Th down to terminal a. Ground b. With a open, a sits at V_Th. Drawing a current i makes a sag by R_Th·i. A short pulls a down to b, and the current that flows is I_N. To find R_Th, turn sources off: a voltage source becomes flat, a current source becomes a gap, and dependent sources stay on. Then push 1 A in, and a's height is R_Th. Equivalents keep **terminal** heights only, so never read an inside power off an equivalent.
- **W5:** **max power** puts the load at **half the open-circuit height** (V_Th/2): h and V_Th − h have a fixed sum, so their product is largest when they are equal. **Superposition** draws one picture per source and **adds heights node by node, never powers**.
- **W6** (not on the midterm, don't touch unless asked): use three snapshots, 0⁻ / 0⁺ / ∞. At 0⁺, C holds its step and L holds its current, and nothing else carries over. Between snapshots every height slides exponentially with one τ, where τ = distance to travel ÷ starting speed (it agrees with RC and L/R).

**When not to force heights:** single-element waveform questions (use i/v/p graphs), counting nodes and meshes, plain R_eq arithmetic, mesh currents, and coupled unknowns (do the algebra, and use the picture to check it).

## 5. Writing a height view in this app

Height views are `#@` comment lines at the end of a ```` ```schematic ```` block. The drawing parser ignores them, and `Elevation.tsx` renders them behind a **Height view** button. **Nothing is computed for you.** Every height and current you write must come from a verified solution.

```
#@ view "As drawn"                                  start a view; several views become tabs
#@ node m 6 "$m$: $6\,\mathrm{V}$"                  name, height (V), label; flags: ground | unknown | terminal
#@ node g 0 "ground: $0\,\mathrm{V}$" ground        repeat ground under new names (g2, g3…) per branch
#@ el V t g "$12\,\mathrm{V}$" col=0 i="$3\,\mathrm{A}$" to=t id=es
#@ el R t m "$2\,\Omega$: falls $6\,\mathrm{V}$" col=1 i="$3\,\mathrm{A}$" to=m id=e1
#@ step "Ground the bottom wire. ..." show=m,e1      walkthrough step; reveals listed nodes/element ids
#@ note "..."   #@ spoiler   #@ inline   #@ straight off   #@ mismatch a b "..."   #@ scale illustrative
```

- Element kinds: `R V I E G B C L X S W`. For V/E/B the **first node is +**. For I/G the arrow points **from the first node to the second**. `i` is the actual current's magnitude and `to` is the node it flows toward. Elements in one `col` stack in series. An element whose ends are at the same height lies flat between `col` and `col+1`.
- `plus=NODE v="$v_x$"` copies the drawing's voltage reference (blue + / −). Add it to **every** element whose drawing has `v=`, `v_rev=` or a gap voltage, even when its + end is the lower one (that is what makes v_x negative). Other elements get automatic black actual-polarity marks.
- `#@ spoiler` goes on every problem and Try it. `#@ inline` is for teaching visuals only, never for unsolved problems.
- The label text after `: ` stays hidden until a step `show`s that element, so write `"$4\,\Omega$: falls $8\,\mathrm{V}$"`.

## 6. House rules (owner's preferences)

- **Full loop** view is the default, and the owner prefers it ("full circle loop, not line"). Weeks 4–5 use `#@ straight off` on every view. Straight line (river/rail) is optional.
- **Keep the original ground.** Draw negative levels below 0 V. Do not shift the reference merely to make all heights positive.
- **Every circuit gets a height view**, and every problem or example with a circuit gets a step walkthrough in the recipe order. The first step names ground ("Ground the bottom wire." / "Same ground (…)." on later tabs).
- **Words:** a resistor **falls** ("falls 8 V", "no fall"). A source **steps**. An open switch **takes all of** the step. A wire or ammeter has **no step**. Current **climbs** (delivers) or **falls** (absorbs). Don't say "drop".
- **Tabs for cases:** before/after, switch positions, loads. For Thévenin use Open / Short / "Sources off, push 1 A". For superposition use "X alone" + "add". Keep node names the same across tabs.
- The owner is a visual, example-driven learner. Use the height picture to find the solution: known flows → branch splits → iR falls → matching endpoints → read the heights. Follow the worked examples in Weeks 1–2. Weave heights into each topic rather than making a separate "height workout" topic. Prefer many circuits, examples and practice over prose. See the memory notes on study-note style.

## 7. Pipeline

Views are **generated from a solver**, so heights, falls and currents can't be mistyped:

- `scripts/height_notes/mna.py` is a modified-nodal-analysis `solve(elems)` that supports dependent sources (the app's own simulator has none). Element tuples: `('R', name, a, b, ohms)`, `('V', name, p, n, volts)`, `('I', name, a, b, amps)`, `('E', name, p, n, {node: k}, const)`, `('G', name, a, b, {node: k})`. Node `'0'` is ground.
- `circuits*.py` holds each circuit as `add(key, schematic_source, netlist)`. `check_solve.py` / `check45.py` verify that the drawing's topology matches the netlist.
- `gen.py` (W3) and `w45lib.py` (W4–5) turn a netlist plus column layout into `#@` lines. In `w45lib.view(...)`, `gnd='low'` grounds the lowest node, `disp=` redraws off sources (0 V → flat `W`, 0 A → `S` gap), and `thevenin()` / `off()` are helpers.
- `build_w*v3.py` builds a week's blocks, and `apply45.py <docId> <blocks.json>` replaces them in place through the API. The API allows at most 100 operations per PATCH, with `expected_revision`.
- Checks: `audit_views.py` (downhill, falls, R = fall/i, KCL, power), `verify45.py`, `textcheck45.py` (odd `$`, first step names ground), `clipcheck.cjs <docId> 1300` (math overflow), `shots.cjs` / `pageshot.cjs` (screenshots of every tab and mode). The owner wants real screenshots checked before handover.

**Layout lessons:** put a monotonically falling series chain in one column. Order columns so no level line crosses a resistor. More than about 7 columns overflows the dialog. Nodes sharing a height must share a label. Keep labels to about 20 characters (axis labels over about 22 get clipped). Tab titles don't render LaTeX.

**Pitfall:** never write Python or LaTeX through a Bash heredoc. It collapses `\\` row breaks and turns `\t` into a tab. Use a file written with the Write tool instead.
