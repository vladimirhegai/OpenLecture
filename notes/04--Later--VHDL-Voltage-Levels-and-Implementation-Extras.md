# 04 · Later · VHDL, Voltage Levels, and Implementation Extras

**Later study — outside this midterm study set.** Keep this material for subsequent assessments; prioritize notes 01–03 now.

## VHDL and digital design flow

An **entity** declares the interface; an **architecture** describes the hardware implementing it. Concurrent assignments describe connections that exist together, rather than a list of software operations executed once from top to bottom.

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity logic_example is
  port (a, b, c : in std_logic;
        f       : out std_logic);
end entity;

architecture rtl of logic_example is
begin
  f <= b or (a and not c);
end architecture;
```

`std_logic` includes 0 and 1 plus simulation states such as `U` (uninitialized), `X` (unknown), and `Z` (high impedance). A Boolean truth-table proof checks the binary cases; it does not establish behavior for every simulation state.

The design flow is specification → schematic/HDL → synthesis and functional verification → physical implementation and timing verification. A correct truth table does not guarantee that a physical implementation meets timing.

**Problem: Try it: two outputs are concurrent** (intermediate)

Does exchanging the order of `f <= a and b;` and `g <= not a;` change these two outputs?

<details><summary>Solution</summary>

1. Each concurrent assignment defines its own logic; neither reads the other output.

**Answer:** No. Both connections exist concurrently. Ordering inside a process is a separate question.

</details>

The HDL examples in these notes are teaching descriptions. Their binary behavior is checked with the corresponding equations; no HDL simulator or synthesis run is claimed.

## XOR and parity extensions

| A | B | AB | A+B | $\overline{AB}$ | $\overline{A+B}$ | $A\oplus B$ |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

**NAND** is an AND followed by NOT; **NOR** is an OR followed by NOT. The small output bubble means inversion.

**XOR**, $A\oplus B$, is 1 when the inputs differ. XNOR is 1 when they match. XOR is not ordinary OR: $1\oplus1=0$.

**Problem: Try it: distinguish OR from XOR** (intermediate)

For $F=A+B$ and $G=A\oplus B$, find every input row where $F\ne G$.

<details><summary>Solution</summary>

1. Both give 0 at 00 and 1 at 01 and 10.
2. At 11, OR remains 1 while XOR is 0.

**Answer:** Only A=B=1.

</details>

**Example: Three-way light control**

The light is on when an odd number of three switches is closed. Derive a compact expression.

1. The 1 rows are 001,010,100,111.

   $$F=\sum m(1,2,4,7)$$
2. XOR tracks odd parity.

   $$F=A\oplus B\oplus C$$

**Answer:** `f <= a xor b xor c;` implements the binary truth table.

## Voltage thresholds and noise margin

In **positive logic**, low voltage represents 0 and high voltage represents 1. A range between the valid low and high input levels is undefined; it is not a third valid binary value.

| Quantity | Meaning |
|---|---|
| $V_{OL(\max)}$ | Largest guaranteed low output voltage |
| $V_{OH(\min)}$ | Smallest guaranteed high output voltage |
| $V_{IL(\max)}$ | Largest voltage guaranteed to be accepted as a low input |
| $V_{IH(\min)}$ | Smallest voltage guaranteed to be accepted as a high input |

$$NM_L=V_{IL(\max)}-V_{OL(\max)}$$

$$NM_H=V_{OH(\min)}-V_{IH(\min)}$$

**Example: Noise margin**

A driver guarantees $V_{OL}\le0.4$ V and $V_{OH}\ge2.4$ V. The receiver accepts low through 0.8 V and high from 2.0 V. Find both margins.

1. Low-level noise may raise the low output toward the receiver threshold.

   $$NM_L=0.8-0.4=0.4\ \mathrm V$$
2. High-level noise may lower the high output toward its threshold.

   $$NM_H=2.4-2.0=0.4\ \mathrm V$$

**Answer:** Both margins are 0.4 V. A voltage in the undefined input band has no guaranteed binary interpretation.

## Programmable logic, LUTs, and physical limits

The supplied implementation lecture develops transistor networks; its outline also names the chip families and delay topics below. PS2 supplies the PLA/LUT design tasks. The following descriptions connect those topics, without assuming an additional supplied lecture.

| Implementation | How the function is chosen |
|---|---|
| Standard fixed-function IC | Select an existing function and connect chips |
| PLA | Program product terms in an AND plane and select them in an OR plane |
| PAL / CPLD | PAL: programmable AND terms with a fixed OR structure; CPLD: interconnected programmable blocks |
| FPGA | Configure logic blocks (often LUTs), routing, and storage |
| ASIC / standard cells / gate array | Implement a custom circuit with the chosen fabrication/design approach |

**Example: A LUT stores a truth table**

What four stored bits implement XOR in a 2-input LUT addressed by AB=00,01,10,11?

1. Evaluate XOR at each address.

   $$0,1,1,0$$

**Answer:** Store 0,1,1,0 in address order. A k-input LUT needs $2^k$ truth-table entries.

**Example: PLA product terms can be shared**

For $F=AB+C$ and $G=AB+D$, give the product terms and output connections.

1. Create product lines P1=AB, P2=C, P3=D.
2. Select product lines for each OR output.

   $$F=P_1+P_2,\quad G=P_1+P_3$$

**Answer:** The AB term is generated once and used twice. This illustrates the programmable AND–OR structure.

**Propagation delay** is the time between an input transition and the resulting output transition. **Fan-in** counts a gate’s inputs; **fan-out** describes the load it drives. More loading can increase delay, so fewer gates need not mean the fastest circuit.

A buffer reproduces its input and can provide drive. A **tri-state buffer** drives 0 or 1 when enabled and disconnects its output when disabled; that disconnected state is **Z**, not logic 0. A shared bus needs controls that prevent conflicting drivers.

**Problem: Try it: tri-state bus control** (intermediate)

Driver A drives 1 and driver B drives 0 onto the same bus. Is the bus value an OR of their outputs?

<details><summary>Solution</summary>

1. Both outputs actively try to impose different voltages. Boolean OR does not model this connection.
2. Disable one driver to Z before allowing the other to drive.

**Answer:** No; the bus has contention. With both drivers disabled, the bus is undriven unless another circuit establishes its level.

</details>

## Other number bases: octal and base 4

Group bits because these bases are powers of two.

- Base 4: 2 bits per digit.
- Base 8: 3 bits per digit.
- Base 16: 4 bits per digit; A–F mean decimal 10–15.

Start each grouping at the radix point and work outward. Pad the far left of an integer or far right of a fraction with zeroes.

**Example: One pattern, two compact forms**

Convert $(10110110)_2$ to hex and octal.

1. Group by four for hex.

   $$1011\;0110\Rightarrow(\mathrm{B6})_{16}$$
2. Group by three for octal, padding only at the far left.

   $$010\;110\;110\Rightarrow(266)_8$$
3. Check the value independently.

   $$2(8^2)+6(8)+6=182$$

**Answer:** $(\mathrm{B6})_{16}=(266)_8=182$. Slide 43 prints 226 in its octal result; the grouping gives 266.

**Example: Octal to hex through binary**

Convert $(527)_8$ to hexadecimal.

1. Replace every octal digit with exactly three bits.

   $$(527)_8=(101\;010\;111)_2$$
2. Regroup from the right in fours.

   $$0001\;0101\;0111\Rightarrow(157)_{16}$$

**Answer:** $(157)_{16}$; both forms equal 343.

**Problem: Try it: group a fraction** (intermediate)

Convert $(11010.101)_2$ to hexadecimal and octal.

<details><summary>Solution</summary>

1. Use groups of four on each side of the radix point.

   $$0001\;1010.1010\Rightarrow(1\mathrm{A.A})_{16}$$
2. Use groups of three on each side.

   $$011\;010.101\Rightarrow(32.5)_8$$

**Answer:** $(1\mathrm{A.A})_{16}=(32.5)_8=26.625$.

</details>
