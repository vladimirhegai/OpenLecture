# 03 · Implementation Technology — Midterm (Week 5)

**Midterm: Weeks 1–5.** This is one of the three main study sections for the 40-minute October 29 midterm.

**PS2 preparation:** Q1 and Q3–Q5 are in this study set. **Skip Q2 and Q6–Q8 for this midterm.**

## 1. Transistor switches and resistor-load NMOS gates

In **positive logic**, low voltage represents 0 and high voltage represents 1. A range between the valid low and high input levels is undefined; it is not a third valid binary value.

Use the ideal switch model for the course transistor networks.

- **NMOS:** conducts when its gate input is high; typically used to pull the output down to ground.
- **PMOS:** conducts when its gate input is low; typically used to pull the output up to $V_{DD}$.

These rules describe the rail-driven logic switches here; they are not a general analog MOSFET model.

In resistor-load NMOS logic, an open pull-down network lets the resistor pull the output high. When the NMOS network conducts, the output goes low and the resistor can carry steady current.

| NMOS pull-down arrangement | Conducts when | Output with a pull-up |
|---|---|---|
| One switch A | A=1 | $F=\overline A$ (NOT) |
| A and B in series | A=B=1 | $F=\overline{AB}$ (NAND) |
| A and B in parallel | Either input is 1 | $F=\overline{A+B}$ (NOR) |

```schematic
terminal 0,6 "VDD" above
R1 0,6 -> 0,4 "pull-up"
S1 0,4 -> 0,2 "A"
S2 0,2 -> 0,0 "B"
wire 0,4 -> 2,4
terminal 2,4 "F" right
ground 0,0
```

**Problem: Try it: identify a pull-down function** (intermediate)

Two NMOS switches controlled by A and B are in parallel below a resistor pull-up. Is the output AND, OR, NAND, or NOR?

<details><summary>Solution</summary>

1. Either high input completes a path to ground.

   $$\text{PDN conducts}=A+B$$
2. The output is low when that path conducts.

   $$F=\overline{A+B}$$

**Answer:** NOR.

</details>

## 2. Complementary CMOS: NOT, NAND, NOR, AND, OR

Static complementary CMOS replaces the resistor with a **PMOS pull-up network (PUN)**. It pairs that with an **NMOS pull-down network (PDN)**.

- Derive when the output must be 0: that is the PDN conduction condition $\overline F$.
- AND in a conduction condition means switches in series. OR means parallel branches.
- Build the PUN by swapping series and parallel and replacing NMOS with PMOS, keeping the same gate signals.

```digital
{"kind":"cmos","title":"CMOS inverter","pdn":{"gate":"A"}}
```

*A=0 turns the PMOS on and NMOS off; A=1 does the reverse.*

For a valid steady binary input, the ideal complementary network provides one path to a supply rail while the other network is off. Real CMOS still has leakage and dissipates energy during switching; “zero static power” is an ideal approximation.

**Example: NAND: trace both networks**

Design static CMOS for $F=\overline{AB}$.

1. The PDN must conduct only when both inputs are high.

   $$\overline F=AB$$
2. Put NMOS A and B in series. The dual PUN has PMOS A and B in parallel.
3. At A=B=1 the PDN is on. Otherwise at least one PMOS provides a pull-up path.

**Answer:** Two NMOS + two PMOS = four transistors.

```digital
{"kind":"cmos","title":"CMOS NAND","pdn":{"series":[{"gate":"A"},{"gate":"B"}]}}
```

*PMOS gate bubbles indicate conduction for a low gate input.*

**Example: NOR and transistor counting**

How does a 2-input NOR differ from a 2-input NAND? How many transistors implement a 2-input AND in basic static CMOS?

1. NOR needs parallel NMOS and series PMOS.

   $$F=\overline{A+B}$$
2. AND is a NAND followed by an inverter.

   $$N_{\mathrm{AND}}=4+2=6$$

**Answer:** NOR uses four transistors with the opposite series/parallel arrangement. Basic AND uses six.

```digital
{"kind":"cmos","title":"CMOS NOR","pdn":{"parallel":[{"gate":"A"},{"gate":"B"}]}}
```

*Parallel NMOS pull down when either input is 1. Series PMOS pull up only for A=B=0.*

For basic complementary static CMOS, an n-input NAND/NOR uses n NMOS + n PMOS. An AND/OR adds a two-transistor inverter after the corresponding NAND/NOR. Count the gates actually drawn before considering a cheaper equivalent implementation.

**Example: PS2 Q1: count the circuit that was given**

The supplied gate drawing has three NOTs, four 3-input ANDs, and one 4-input OR. How many transistors implement those gates in basic static CMOS?

1. The NOTs each use 2 transistors.

   $$3(2)=6$$
2. Each 3-input AND is a 3-input NAND followed by an inverter.

   $$4(2\cdot3+2)=32$$
3. The 4-input OR is a 4-input NOR followed by an inverter.

   $$2\cdot4+2=10$$
4. Add the counts for this drawn realization.

   $$N=6+32+10=48$$

**Answer:** 48 transistors. Replacing the drawing with a different equivalent circuit answers a different question.

## 3. Function → pull-down → dual pull-up

**Example: Lecture complex gate: derive the conducting paths**

Implement $F=\overline A+\overline B\,\overline C$.

1. Complement the function to obtain the PDN condition.

   $$\overline F=A(B+C)$$
2. Use NMOS A in series with parallel NMOS B and C.
3. The dual PUN is PMOS A in parallel with series PMOS B and C.

**Answer:** Three NMOS + three PMOS = six transistors. The output is high when A=0, or when B=C=0.

```digital
{"kind":"cmos","title":"Complex complementary CMOS gate","pdn":{"series":[{"gate":"A"},{"parallel":[{"gate":"B"},{"gate":"C"}]}]}}
```

*Always distinguish the function at f from the condition that makes the PDN conduct.*

**Problem: Try it: preserve the outer inversion** (intermediate)

Build the PDN and count transistors for $F=\overline{AB+C}$.

<details><summary>Solution</summary>

1. The PDN condition is AB+C: a series A–B branch in parallel with C.
2. The PUN is parallel PMOS A/B in series with PMOS C. Each network has three transistors.

**Answer:** Six transistors total. This one complex gate gives the inverted function; an extra inverter would produce AB+C.

</details>

**Example: PS2 Q3: complete the missing PMOS half**

The given PDN has NMOS B in parallel with the series path A–C, where A=x1, B=x2, C=x3. Derive the PUN and F.

1. Write the condition for a complete ground path.

   $$G=B+AC$$
2. The output is the complement of the ground-path condition.

   $$F=\overline{B+AC}$$
3. Dualize: PMOS B is in series with parallel PMOS A and C.

   $$F=\overline B(\overline A+\overline C)$$

**Answer:** Three NMOS and three PMOS. The dual network keeps the same gate labels; PMOS already conducts on 0.

```digital
{"kind":"cmos","title":"PS2 Q3: complete complementary gate","pdn":{"parallel":[{"gate":"B"},{"series":[{"gate":"A"},{"gate":"C"}]}]}}
```

*A=x1, B=x2, C=x3. Compare the dual PMOS network with the supplied partial drawing.*

**Problem: PS2 Q5: simplify first, then draw CMOS** (intermediate)

$F(A,B,C,D)=\sum m(0,1,2,4,6,8,10,12,14)$. Find the minimum SOP and the corresponding static CMOS network.

<details><summary>Solution</summary>

1. All eight even rows have D=0 and contribute NOT D.
2. The only remaining 1 is row 1; combine it with row 0 by Boolean algebra.

   $$F=\overline D+\overline A\overline B\overline C$$
3. Complement before drawing the PDN.

   $$\overline F=D(A+B+C)$$
4. Use NMOS D in series with parallel A,B,C; dualize for the PUN.

**Answer:** Four NMOS and four PMOS. PUN: PMOS D in parallel with series PMOS A,B,C. The eight-transistor complex gate directly implements F.

</details>

## 4. CMOS drawing → function → truth table

Read the **NMOS half** first: start at F and find every complete path to ground. Multiply gate conditions along a series path and OR parallel paths, then complement once to obtain F.

Check with the PMOS half: a pull-up path must exist exactly when F=1. A complemented gate label is a signal name, not an instruction to complement the final output twice.

```digital
{"kind":"cmos","title":"PS2 Q4: interpret this CMOS circuit","pdn":{"series":[{"gate":"A"},{"parallel":[{"gate":"D"},{"series":[{"gate":"B"},{"gate":"C"}]}]}]}}
```

*Redrawn from PS2 Q4: A=x1, B=x2, C=x3, D=x4.*

**Example: PS2 Q4: derive the output and canonical SOP**

Read the four-input CMOS circuit above. Give its output function, truth table, and canonical 1-row indices.

1. A is in series with the parallel choice D or BC.

   $$G=A(D+BC)$$
2. A conducting PDN makes the output zero.

   $$F=\overline{A(D+BC)}$$
3. Complement using De Morgan to check the PUN.

   $$F=\overline A+\overline D(\overline B+\overline C)$$
4. All A=0 rows are 1; for A=1, only BCD=000,010,100 remain high.

   $$F=\sum m(0,1,2,3,4,5,6,7,8,10,12)$$

**Answer:** The table below gives every row. Expand the listed minterms if a full canonical SOP is requested; each minterm must include A,B,C,D.

| A | B | C | D | F |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 |
| 0 | 0 | 0 | 1 | 1 |
| 0 | 0 | 1 | 0 | 1 |
| 0 | 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 |

$$m_{10}=A\overline B C\overline D$$

For example, row 10 is 1010, so its full minterm is the expression above. For the whole function, OR the minterms at all eleven listed 1 rows.
