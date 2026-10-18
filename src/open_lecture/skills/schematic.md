# Schematic
Draw circuits in notes with the schematic language. The app renders each drawing as a clean circuit diagram, so every worked example and practice problem with a circuit should show it instead of describing it in words.

## Where drawings go

- Inside any Markdown text (a problem `prompt`, an example `prompt`, a paragraph) as a fenced block:
  ````
  ```schematic
  V1 0,3 -> 0,0 "$50\,\mathrm{V}$"
  ...
  ```
  ````
- As a standalone `schematic` block `{"type": "schematic", "source": "...", "caption": "..."}` for a figure in the explanation.

Before saving, call `schematic_check` with the drawing. It returns the nodes and which nodes every element connects, so you can confirm that the drawing is the circuit you mean. Documents reject drawings that do not parse.

## Language

One statement per line on a grid where x grows right and y grows up. Points are `x,y` (e.g. `3,0`), and `#` starts a comment.

| Statement | Meaning |
|---|---|
| `NAME p1 -> p2 "label" options` | A two-terminal element from `p1` to `p2`. |
| `wire p1 -> p2 -> p3 ...` | Plain wire through the points. |
| `ground p` (`down` default, or `up`, `left`, `right`) | Ground symbol at `p`; that node becomes the reference node `0`. |
| `label p "a" above` | Node label (`above`, `below`, `left`, `right`). It names the node in `schematic_check`. |
| `terminal p "a" left` | Open-circle terminal, for a pair of terminals such as $a$–$b$. |
| `dot p` | Junction dot. Dots are added automatically where three or more wires meet. |
| `gap p1 -> p2 v="$v_o$"` | Nothing drawn: only a voltage label across an open pair of points. |

The element type comes from the name's first letters, as in SPICE:

| Prefix | Element | Prefix | Element |
|---|---|---|---|
| `R` | resistor | `E`, `H` | dependent voltage source (diamond) |
| `C` | capacitor | `G`, `F` | dependent current source (diamond) |
| `L` | inductor | `B` | battery |
| `V` | independent voltage source | `D` | diode |
| `I` | independent current source | `S` | switch |
| `X` | generic element box (e.g. "element X") | `AM`, `VM` | ammeter, voltmeter |

### Direction rule

The first point is the element's **+ terminal** and its **reference current flows from the first point to the second**, the same convention as the netlist language (`V1 n+ n-`):

- `V1 0,3 -> 0,0 "10 V"` puts + at the top. `I1 0,0 -> 0,3 "2 A"` points the source arrow up.
- `R1 3,3 -> 3,0 v="$v_o$" i="$i_o$"` marks + at the top and draws $i_o$ downward, which is the passive sign convention.
- `i_rev="$i_s$"` and `v_rev="$v_s$"` reverse just that annotation (`i="$i_s$" i_rev` means the same).
- A bare `i` or `v` (no value) draws an unlabelled arrow or unlabelled +/− marks.

### Labels and options

- The quoted text after the points is the element's label: its value or name. Write math in LaTeX between `$...$`, e.g. `"$5\,\Omega$"`, `"$2i_\Delta$"`, `"$R_1$"`. Plain text such as `"50 V"` also works.
- `i="$i_a$"`: a current arrow on the element. `v="$v_x$"`: + label − across it.
- `flip`: moves the label to the other side of the element. It also moves the `v` marks onto the side where the `i` arrow's label sits, so never combine `flip` with both `i=` and `v=`. Leave `flip` off on such an element: the value and the `i` label then sit on one side and the `v` marks on the other.
- Switches: `state=closed` (default open), `action=open` or `action=close` for a switch that moves at $t=0$.

### Layout

- Give each element 2 to 3 grid units of length. Keep the diagram compact: usually 3 to 4 units tall and up to about 12 units wide.
- Use only horizontal and vertical lines. Put the main source on the left, drawn from bottom to top, and the reference node along the bottom with one `ground`.
- Elements must meet at their end points. A point touching the middle of an element is an error, but a point on a wire joins that wire.
- Label the nodes the text refers to (`label 3,3 "$a$" above`), plus every current and voltage the problem asks about.

## Example

A 50 V source feeds a 5 Ω resistor into node $a$, which connects to 10 Ω and a dependent source $2i_a$ to ground:

```schematic
V1 0,3 -> 0,0 "$50\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\Omega$" i="$i_a$"
R2 3,3 -> 3,0 "$10\,\Omega$" v="$v_o$"
wire 3,3 -> 6,3
G1 6,3 -> 6,0 "$2i_a$"
wire 6,0 -> 0,0
label 3,3 "$a$" above
ground 0,0
```

`schematic_check` reports for this drawing that `V1` runs from `n1` to `0`, `R1` from `n1` to `a`, and `R2` and `G1` from `a` to `0`.

## Current flow (`#~` lines)

`#~` comment lines turn a drawing into a live circuit. Dots stream along every wire and element: faster dots mean more current, and the dots fade as a current dies. The reader can flip each switch, either with a button or by clicking the switch in the drawing (the app redraws it open or closed), and the transient plays in slow motion with live readouts and a plot. The app simulates the circuit itself in `frontend/src/components/flow/`: modified nodal analysis, with inductors and capacitors stepped by backward Euler. It supports R, L, C, V, I, S, AM (a wire) and VM (open) elements.

**Plug-in use: add the single line `#~ flow` to any drawing** (in the 231 builders: `flow(src)` from `lib231`, or `sch(src)` in build_w2v2.py, which does it for you). Everything else is automatic:

- **Values** are read from the labels: `"$4\,\mathrm{k\Omega}$"`, `"$2\,\mu\mathrm{F}$"`, `"$0.3\,\mathrm{H}$"`, `"$12\,\mathrm{V}$"`, `"$2\,\mathrm{A}$"`. A symbolic label (`$R$`, `$V_s$`) gets a stand-in (R 1 kΩ, C 1 µF, L 1 H, V 10 V, I 10 mA, so every RC/RL pair has τ = 1 ms), listed in the note under the plot.
- **Switches** start in the position before $t=0$: `action=open` means closed before, `action=close` means open before (`state=` overrides). Switches with the same label (two `"$t=0$"` switches drawn for one SPDT move) flip together with one button. A `"$t=0$"` label shows $t<0$, then $t=0$, then $t>0$.
- **Slow motion** is picked so the slowest time constant plays over about 2 s.
- **Readouts:** up to three currents (L, then C, then R) plus each capacitor's voltage (named by its `v=` label). Units and decimals are fixed from a preview run so the boxes never change width.
- Opening a switch that leaves an inductor carrying current with no path shows a "spark" warning (the simulation lets the current fall to 0).

Optional `#~` lines, only when the defaults are not what you want:

```
#~ value R1 4                force a value (SI with prefix: 8m, 10u, 2.5k); overrides the label
#~ init C1 2                 start a capacitor at 2 V (or an inductor at 2 A) instead of DC steady state
#~ slow 1000                 force the slow-motion factor
#~ probe L1 "inductor $L$:"  choose readouts yourself (current; first ones are plotted)
#~ probe C1 v "$v$:"         a voltage readout
#~ gang S1 S2                make switches flip together (otherwise: same label)
#~ note "…"                  replace the automatic note
```

The circuit starts in DC steady state for the starting switch positions (plus any `init`). Probe readouts and the plot show magnitudes; the dots show direction. Check every flow circuit with `node scripts/notes231/flowshots.cjs <docId> <outDir>`, which prints the readouts before and after each switch flip: compare them with the hand solution.

## Height views (voltage as height)

Every circuit in a study note should also carry a **height view**. The reader opens it with the "Height view" button on the drawing. It redraws the solved circuit with every node at its potential: ground (0 V) is the reference and the vertical axis is volts. Series elements stack in one column. Current arrows are orange when the current runs downhill (the element absorbs) and green when it runs uphill (the element delivers). The dialog's default **Full loop** mode draws every source, and so does the in-page `#@ inline` picture. The optional **Straight line** mode leaves out the grounded source that feeds the highest level and shows it as a labelled supply rail (a "9 V" bar at the top, one line falling through the loads). **Keep ground at the bottom of the picture:** if a circuit's nodes sit below the drawing's ground, measure heights from the lowest node instead, and say so in the first step (moving ground changes no answer).

The height view is written as `#@` comment lines at the end of the same schematic source. The drawing parser ignores comments, so the drawing itself is unchanged. The app renders it in `frontend/src/components/Elevation.tsx`. Nothing is computed automatically: **you** solve the circuit and write the potentials and currents.

| Statement | Meaning |
|---|---|
| `#@ view "Title"` | Starts a view. Several views become tabs (e.g. "As drawn" / "Source reversed", "Switch open" / "Switch closed", one per case). |
| `#@ node NAME HEIGHT "label" [ground] [unknown]` | A node at HEIGHT volts. Write the label as `"top: $30\,\mathrm{V}$"`; the straight view shows the text after `: ` on the rail. Repeat a ground node under new names (all marked `ground`) when several branches end at ground. `unknown` draws an undetermined potential dashed, at an arbitrary height, and greys its arrows. |
| `#@ el KIND A B "label" col=N i="$2\,\mathrm{A}$" to=NODE` | One element between nodes A and B. Kinds: `C` capacitor, `L` inductor, `R` resistor, `V` voltage source, `I` current source, `E` dependent voltage source, `G` dependent current source, `B` battery, `X` generic element, `S` open switch, `W` closed switch (a plain wire). For V, E and B the **first node is +**. For I and G the **arrow points from the first node to the second**, as in the drawing. `i` is the actual current's magnitude and `to` the node it flows toward; leave out `i` when the current is undetermined. A vertical element sits in column `col`. An element whose two nodes have the same height lies flat between `col` and `col+1`. |
| `... plus=NODE v="$v_x$"` (on an `el`) | Copies a voltage reference from the drawing: a blue $+$ at NODE and $-$ at the other end, named $v_x$ (the name is optional). Add it to **every** element whose drawing carries `v=`/`v_rev=` (or a `gap` voltage across it), with NODE at the drawing's $+$ end even when that end is the lower one: that is what makes $v_x$ negative. Elements without it get black $+/-$ marks at their actual polarity ($+$ on the higher end) automatically; V and E show the signs inside their symbols. |
| `... rail` / `... norail` (on an `el`) | Force or forbid the straight view's supply rail for that grounded source. Use `rail` on a grounded **current** source that feeds the highest node (otherwise only voltage sources and batteries become rails). |
| `#@ node ... terminal` | An open terminal (e.g. $a$ of a Thévenin pair): a short lead ending in an open circle. |
| Kinds `C`, `L` | Capacitor (two plates) and inductor (coil). A snapshot draws $C$ as a held step and $L$ as a held current (see the guide's Week 6 rules); in DC steady state draw $C$ with no current and $L$ flat. |
| `#@ mismatch A B "text"` | Two levels that should be one node: draws a red bracket, for invalid connections. |
| `#@ note "text"` | One or two sentences under the drawing: what to notice. |
| `#@ scale illustrative` | Symbolic circuits: heights only show order, not amounts. |
| `#@ straight off` | Disables the straight-line mode for a view. Put it **after** that view's `#@ view` line; before the first `#@ view` it does nothing. |
| `#@ inline` | Also draws the finished first view in the page, under the circuit (the button still opens tabs and steps). Use it for teaching visuals and worked examples, never on problems the reader should solve first. Keep level and element labels short (about 20 characters), because the inline picture is scaled to the note's column. |
| `#@ spoiler` | Blurs the view until the reader clicks, for problems whose answer it reveals (every practice problem and Try it). |
| `#@ step "text" show=a,eR` | One step of a **height-view solution** ("Solve with heights" panel, Next/Back buttons). `show` lists the node names and element ids (`el ... id=eR`) that the step works out. Until then their levels and rail values read "?", their currents are hidden, and an element label `"$9\,\Omega$: falls $18\,\mathrm{V}$"` shows only the part before `: `. Anything never named in a `show` is given from the start. Write steps for every problem or example with a circuit, in this order: ground → voltage-source steps → currents → resistor falls ($iR$) → read off the asked-for voltages → power as current × height change, with uphill delivering and downhill absorbing. |

Rules that keep it correct. Check each one before saving, then open the dialog in a browser and look at every view in **both** modes:

- Wire the view exactly like the drawing: same elements, same connections, same + ends and arrow directions. A label that is negative in the drawing (e.g. $v_x=-25\,\mathrm{V}$) becomes a node placed *below* its partner.
- Use the solved values: each voltage source spans exactly its value, from its + node; resistors satisfy $v=iR$ and carry current downhill; KCL holds at every node; the absorbed powers (downhill) equal the delivered powers (uphill).
- Put the main source between ground and the **highest** node, so the straight view has a top rail. A source partway down stays drawn.
- Keep element labels short (`"$10\,\mathrm{k\Omega}$"`, `"$R_c$: falls $2\,\mathrm{V}$"`). Columns widen to fit labels, but long labels make wide dialogs.
- Write no height view for a symbol legend, a lone resistor symbol, or a figure with only currents (a KCL node): there are no potentials to show.

The full set of height-method rules for Weeks 1–6 lives in the course note **"The Height Method: Complete Guide"**; follow it when adding views to a week.

House style, so every walkthrough reads the same way:

- **Every problem or example with a circuit gets steps**, in the guide's six-step order: pick ground → fixed heights (voltage sources) → currents → the rest of the heights ($iR$) → coupled unknowns if any → answer and check (KVL, KCL, climbs = falls). The **first step always names ground** ("Ground the bottom wire." / "Same ground (…)." on a later tab).
- **Words:** a resistor **falls** ("$4\,\Omega$: falls $8\,\mathrm{V}$", "no fall"); a source **steps**; an open switch **takes all of** the step; a closed switch or ideal ammeter has **no step**; current **climbs** (delivers) or **falls** (absorbs). Avoid "drop" in height views. Patterns beyond a single solved picture:

- **Before/after and cases** (loads, meters, tolerances, switch positions, Δ–Y original vs transformed): one `view` per case. Keep node names the same across tabs so the reader compares like with like.
- **Coupled unknown heights** (node-voltage, supernode): steps go "name the unknown heights → KCL at each (or around the supernode) → solve → place them → currents → power". A voltage source between two unknowns is a rigid rod. Do not draw mesh currents; show only branch currents.
- **Thévenin/Norton:** ground $b$, mark $a$ with `terminal`, and use tabs *Open*, *Loaded* and *Short*. A source turned off is drawn as a flat `W` (voltage source) or an `S` gap (current source), labelled "off". Never read inside powers from an equivalent.
- **Superposition:** one tab per source acting alone, then a tab that adds the heights; say in a note that powers do not add.
- **Switching (Week 6):** tabs for $t=0^-$, $t=0^+$, a mid-transient instant and $t\to\infty$. At $0^+$ only capacitor steps and inductor currents carry over. "Downhill" is a resistor rule: $C$ and $L$ may carry current uphill (they deliver stored energy).

Example: the capstone loop, a 24 V source and 9, 1 and 2 Ω in series with a 2 A loop current:

```
#@ spoiler
#@ node d 24 "$d$: $24\,\mathrm{V}$"
#@ node c 6 "$c$: $6\,\mathrm{V}$"
#@ node b 4 "$b$: $4\,\mathrm{V}$"
#@ node a 0 "$a$: $0\,\mathrm{V}$" ground
#@ el V d a "$24\,\mathrm{V}$" col=0 i="$2\,\mathrm{A}$" to=d
#@ el R d c "$9\,\Omega$: falls $18\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=c
#@ el R c b "$1\,\Omega$: falls $2\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=b
#@ el R b a "$2\,\Omega$: falls $4\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=a
#@ note "Up $24\,\mathrm{V}$ through the source, then down $18+2+4=24\,\mathrm{V}$ through the resistors: KVL as a picture."
```
