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
- `flip`: moves the label to the other side of the element.
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
