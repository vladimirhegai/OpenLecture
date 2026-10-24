# Week 4: Method Choice, Source Transformations and Thévenin–Norton Equivalents

## Overview

> **Info:** Use the nodal and mesh methods from Week 3 to choose an efficient setup, transform sources, and find a two-terminal equivalent. Thévenin and Norton begin here. Week 5 continues their dependent-source cases and adds maximum power transfer and superposition.

- Choose between nodal and mesh analysis based on the actual unknowns and the requested quantity.
- Transform a voltage source in series with a resistor into a current source in parallel with that resistor, and reverse the transformation.
- Find open-circuit voltage, short-circuit current and equivalent resistance.
- Reconnect a load and account for meter loading.
- Use the original circuit to calculate the power of its internal elements and sources.

## Topic 1: Method choice — nodal or mesh?

Method choice means looking at the circuit before doing algebra. For nodal analysis, count the node voltages that remain unknown after using grounded voltage sources and other source constraints. For mesh analysis, identify the meshes, then use current-source constraints to see how many mesh currents remain independent. Compare the equations you will actually need, rather than counting sources alone.

| What you notice | Usually a useful approach | Reason |
|---|---|---|
| Only one or two unknown node voltages | Nodal analysis | KCL directly gives a small set of equations. |
| A voltage source connected to ground | Nodal analysis | Its other node voltage is known from the source polarity. |
| A few meshes and several voltage sources | Mesh analysis | KVL uses the known source voltages directly. |
| A current source belonging to one mesh only | Mesh analysis | That mesh current is known, with a sign set by the source arrow. |
| A floating voltage source | Nodal analysis with a supernode, or mesh analysis | Compare the supernode KCL plus voltage constraint against the alternative mesh setup. |
| A current source shared by two meshes | Mesh analysis with a supermesh, or nodal analysis | Compare the supermesh KVL plus current constraint against the alternative nodal setup. |
| A requested resistor voltage or current | Use the method that gives it with fewer conversions | A resistor voltage is a node difference; a branch current may be one mesh current or a difference. |

1. Mark the quantity the problem asks for.
2. List the unknown node voltages and the mesh currents; write obvious source constraints first.
3. Count the remaining independent equations and decide which method gives a simpler path.
4. Write the equations and solve by substitution; recover the requested quantity in its stated reference direction.

> **Warning:** Dependent sources do not automatically remove an unknown. Express their control variables first and see whether a useful substitution really follows. An ideal source can also fix a branch voltage or current while its power remains unknown.

**Example: Lecture 4 · Two nodal equations versus five mesh equations**

Decide which method needs fewer equations, then find the power in the $300\,\Omega$ resistor.

```schematic
V1 0,4 -> 0,0 "$256\,\mathrm{V}$"
R1 0,4 -> 3,4 "$150\,\Omega$"
R2 3,4 -> 3,0 "$200\,\Omega$"
R3 3,4 -> 6,4 "$100\,\Omega$"
E1 6,4 -> 6,0 "$50i_\Delta$"
R4 6,4 -> 9,4 "$250\,\Omega$"
R5 9,4 -> 9,0 "$400\,\Omega$"
R6 9,4 -> 12,4 "$500\,\Omega$"
V2 12,0 -> 12,4 "$128\,\mathrm{V}$"
wire 3,4 -> 3,6
wire 9,4 -> 9,6
R7 9,6 -> 3,6 "$300\,\Omega$" i="$i_\Delta$"
wire 0,0 -> 12,0
label 3,4 "$a$" below
label 6,4 "$b$" above
label 9,4 "$c$" below
label 12,4 "$d$" right
ground 0,0
```

1. Ground the bottom wire. Read both independent voltage-source polarities and express the dependent source control.

   $$v_s=256,\quad v_d=-128,\quad i_\Delta=\dfrac{v_c-v_a}{300},\quad v_b=50i_\Delta=\dfrac{v_c-v_a}{6}$$
2. Five meshes would require five KVL equations. The source constraints leave only $v_a$ and $v_c$ as independent nodal unknowns, so choose nodal analysis.
3. Write KCL at $a$ and $c$ using resistor voltage differences.

   $$\begin{aligned}\dfrac{v_a-256}{150}+\dfrac{v_a}{200}+\dfrac{v_a-v_b}{100}+\dfrac{v_a-v_c}{300}&=0\\\dfrac{v_c-v_b}{250}+\dfrac{v_c}{400}+\dfrac{v_c+128}{500}+\dfrac{v_c-v_a}{300}&=0\end{aligned}$$
4. Substitute the control equation and clear the denominators.

   $$16v_a-3v_c=1024,\qquad-16v_a+67v_c=-1536$$
5. Add to eliminate $v_a$, then back-substitute.

   $$64v_c=-512\Rightarrow v_c=-8\,\mathrm{V},\quad v_a=62.5\,\mathrm{V}$$
6. Use the original leftward current reference through 300 Ω.

   $$i_\Delta=\dfrac{-8-62.5}{300}=-0.235\,\mathrm{A},\quad P_{300}=300(0.235)^2=16.5675\,\mathrm{W}$$

**Answer:** Node-voltage (2 equations vs 5). $p_{300\,\Omega}\approx16.57\,\mathrm{W}$.

## Topic 2: Source transformations

A voltage source $V_s$ in series with a resistor $R$ has the same terminal voltage–current relation as a current source $I_s=V_s/R$ in parallel with the same $R$. Keep the same external terminals when redrawing. The Norton arrow points toward the terminal that was the voltage source positive side.

$$I_s=\frac{V_s}{R},\qquad V_s=I_sR$$

```schematic
V1 0,3 -> 0,0 "$v_s$"
R1 0,3 -> 3,3 "$R$"
wire 0,0 -> 3,0
terminal 3,3 "$a$" right
terminal 3,0 "$b$" right
I1 6,0 -> 6,3 "$i_s=\tfrac{v_s}{R}$"
wire 6,3 -> 8,3
R2 8,3 -> 8,0 "$R$"
wire 6,0 -> 8,0
wire 8,3 -> 10,3
wire 8,0 -> 10,0
terminal 10,3 "$a$" right
terminal 10,0 "$b$" right
```

1. Identify the two external terminals and the source–resistor pair that is truly in series or parallel.
2. Transform the pair, preserving source polarity or arrow direction.
3. Combine any series or parallel resistors and sources that the transformation exposes.
4. Solve the simpler circuit. Return to the original diagram for internal currents and source powers.

> **Tip:** A resistor in parallel with an ideal voltage source does not change that pair's external voltage. A resistor in series with an ideal current source does not change that branch current. You may omit such resistors from an external-equivalent calculation, but include them when finding original source power.

**Example: Lecture 4 · Transform, solve, then recover original source powers**

Use source transformations to find $v_o$. Then find the power developed by the $250\,\mathrm{V}$ source and by the $8\,\mathrm{A}$ source.

```schematic
V1 0,4 -> 0,0 "$250\,\mathrm{V}$"
R2 3,4 -> 3,0 "$125\,\Omega$"
R1 3,4 -> 7,4 "$25\,\Omega$"
R4 7,4 -> 7,0 "$100\,\Omega$" v="$v_o$"
wire 0,4 -> 3,4
wire 7,4 -> 10,4
I1 10,4 -> 10,2 "$8\,\mathrm{A}$"
R3 10,2 -> 10,0 "$10\,\Omega$"
R5 10,4 -> 13,4 "$5\,\Omega$"
R6 13,4 -> 13,0 "$15\,\Omega$"
wire 0,0 -> 13,0
label 7,4 "$b$" above
label 10,2 "$d$" right
label 13,4 "$e$" above
ground 0,0
```

1. Drop the $125\,\Omega$ and the $10\,\Omega$; swap the $250\,\mathrm{V}$ + $25\,\Omega$.

   $$i_s=\dfrac{250}{25}=10\,\mathrm{A}$$
2. One node: net $2\,\mathrm{A}$ into $25\parallel100\parallel20=10\,\Omega$.

   $$v_o=(10-8)(10)=20\,\mathrm{V}$$
3. Back to the original for the $250\,\mathrm{V}$ source.

   $$p=250\Big(\dfrac{250-20}{25}+\dfrac{250}{125}\Big)=250(11.2)=2800\,\mathrm{W}$$
4. The $8\,\mathrm{A}$ source: $d=(8)(10)=80\,\mathrm{V}$.

   $$p=(80-20)(8)=480\,\mathrm{W}\text{ developed}$$

**Answer:** $v_o=20\,\mathrm{V}$; the $250\,\mathrm{V}$ source develops $2800\,\mathrm{W}$, the $8\,\mathrm{A}$ source $480\,\mathrm{W}$.

## Topic 3: Thévenin and Norton equivalents

| Equivalent | Circuit | Quantities |
|---|---|---|
| Thévenin | A voltage source in series with a resistance. | $V_{\mathrm{Th}}$ is the open-circuit terminal voltage; $R_{\mathrm{Th}}$ is the resistance seen at those terminals. |
| Norton | A current source in parallel with a resistance. | $I_N$ equals the external short-circuit current from a to b; the equivalent source arrow is from b toward a. |
| Conversion | The two forms describe the same terminal relation. | $R_N=R_{\mathrm{Th}}$ and $I_N=V_{\mathrm{Th}}/R_{\mathrm{Th}}$ when the ratio is defined. |

1. Identify terminals a and b and remove only the external load. Keep the original internal resistors and sources.
2. With the port open, solve the original circuit for $V_{\mathrm{Th}}=v_a-v_b$. An open port means no external load current; internal currents can still flow.
3. Find $R_{\mathrm{Th}}$. With only independent sources, deactivate ideal voltage sources to shorts and ideal current sources to opens, then find the resistance seen from a–b.
4. Alternatively, solve for the external short-circuit current $i_{sc}$ and use $R_{\mathrm{Th}}=V_{\mathrm{Th}}/i_{sc}$ when valid. Convert to Norton form if requested.
5. Draw the equivalent with the original terminal labels and reconnect the specified load.

$$v_{ab}=V_{\mathrm{Th}}-R_{\mathrm{Th}}i_L,\qquad i_L=\frac{V_{\mathrm{Th}}}{R_{\mathrm{Th}}+R_L},\qquad v_L=i_LR_L$$

Here $i_L$ leaves terminal a through the load toward b. For a positive Norton current, the equivalent source injects current into a from b, while the external short-circuit current returns from a to b. A negative $V_{\mathrm{Th}}$ or $I_N$ is valid: keep its sign relative to these references.

**Example: Lecture 4 · Open circuit, short circuit and sources deactivated**

Find the Thévenin and Norton equivalents at $a$–$b$.

```schematic
V1 0,4 -> 0,0 "$25\,\mathrm{V}$"
R1 0,4 -> 4,4 "$5\,\Omega$"
R2 4,4 -> 4,0 "$20\,\Omega$"
wire 4,4 -> 7,4
I1 7,0 -> 7,4 "$3\,\mathrm{A}$"
R3 7,4 -> 11,4 "$4\,\Omega$"
terminal 11,4 "$a$" right
terminal 11,0 "$b$" right
gap 11,4 -> 11,0 v="$v_{ab}$"
label 4,4 "$v_1$" above
wire 0,0 -> 11,0
ground 0,0
```

1. Open: no current in the $4\,\Omega$; KCL at $v_1$.

   $$\dfrac{v_1-25}{5}+\dfrac{v_1}{20}=3\;\Rightarrow\;V_{\mathrm{Th}}=v_1=32\,\mathrm{V}$$
2. Short: the $4\,\Omega$ joins $v_1$ to $b$.

   $$\dfrac{v_1-25}{5}+\dfrac{v_1}{20}+\dfrac{v_1}{4}=3\;\Rightarrow\;v_1=16,\;\;I_N=\dfrac{16}{4}=4\,\mathrm{A}$$
3. Two ways to get the resistance.

   $$R_{\mathrm{Th}}=\dfrac{32}{4}=8\,\Omega=(5\parallel20)+4$$

**Answer:** Thévenin: $32\,\mathrm{V}$ in series with $8\,\Omega$. Norton: $4\,\mathrm{A}$ (toward $a$) ∥ $8\,\Omega$.

### Dependent sources and test sources

Keep every dependent source and its controlling relation active. To find the port resistance, deactivate only independent sources, apply a test source at a–b, and calculate $R_{\mathrm{Th}}=v_T/i_T$ with $i_T$ entering the circuit at a. Week 5 gives more practice with this procedure.

> **Warning:** The open/short ratio needs a valid finite equivalent and a nonzero short-circuit current. If both open-circuit voltage and short-circuit current are zero, their ratio is 0/0; use a test source. Equivalent resistance can be negative in an active circuit containing dependent sources.

## Practice problems

There are 20 source problems here. Before solving, state the method you choose and why. In each Thévenin/Norton problem, mark the port and distinguish open circuit, short circuit, and sources deactivated; these are three different calculations. The tutorial, battery and meter questions add different loading and design situations.

| Practice group | What makes the problems different |
|---|---|
| Method choice | Bridge resistor power, a specified zero current, source power, and a current source adjusted to meet a power condition. |
| Transformations | Opposing sources, source polarity, a source in parallel with a resistor, and recovering internal source power. |
| Terminal equivalents | A negative Norton current, two measured load points, an unbalanced bridge, voltmeter loading and ammeter error. |

**Problem: Textbook P4.54 · Choose mesh analysis for a bridge** (intermediate)

**(a)** Which method would you use to find the power in the $10\,\Omega$ resistor, and why? **(b)** Find that power. **(c)** Find the power delivered by the $4\,\mathrm{A}$ source.

```schematic
I1 0,0 -> 0,6 "$4\,\mathrm{A}$"
wire 0,6 -> 9,6
R1 3,6 -> 3,3 "$8\,\Omega$"
R3 3,3 -> 3,0 "$1\,\Omega$"
R2 9,6 -> 9,3 "$2\,\Omega$"
R4 9,3 -> 9,0 "$4\,\Omega$"
R5 3,3 -> 9,3 "$10\,\Omega$" i="$i_{10}$"
wire 0,0 -> 9,0
label 3,3 "$l$" left
label 9,3 "$r$" right
label 6,6 "$t$" above
ground 0,0
```

<details><summary>Solution</summary>

1. Node: $3$ unknown node voltages. Mesh: $3$ meshes, but the current source fixes one.

   $$N_{\text{node}}=3,\qquad N_{\text{mesh}}=2$$
2. Set the left perimeter mesh current to 4 A. Let $i_2$ be the upper triangular mesh and $i_3$ the lower triangular mesh, both clockwise; express each shared resistor current as a difference.
3. Upper and lower triangles, clockwise.

   $$\begin{aligned}20i_2-10i_3&=32\\-10i_2+15i_3&=4\end{aligned}\;\Rightarrow\;i_2=2.6\,\mathrm{A},\;i_3=2\,\mathrm{A}$$
4. The $10\,\Omega$ carries the difference.

   $$i_{10}=i_3-i_2=-0.6\,\mathrm{A},\qquad p=(0.6)^2(10)=3.6\,\mathrm{W}$$
5. Find the current source voltage by summing the resistor voltage drops along the left-hand path.

   $$v=8(1.4)+1(2)=13.2\,\mathrm{V},\qquad p=(4)(13.2)=52.8\,\mathrm{W}$$

**Answer:** **(a)** Mesh (2 equations vs 3). **(b)** $3.6\,\mathrm{W}$. **(c)** $52.8\,\mathrm{W}$ delivered.

</details>

**Problem: Textbook P4.58 · Choose a source value to make a branch current zero** (intermediate)

The variable voltage source $v_{dc}$ is adjusted so that $i_o=0$. **(a)** Node or mesh? **(b)** Find $v_{dc}$. **(c)** Check the power balance.

```schematic
V1 0,3 -> 0,0 "$230\,\mathrm{V}$"
R1 0,3 -> 4,3 "$5\,\Omega$"
R2 4,3 -> 8,3 "$15\,\Omega$"
wire 0,3 -> 0,5
R3 0,5 -> 8,5 "$30\,\Omega$" i="$i_o$"
wire 8,5 -> 8,3
R4 4,3 -> 4,1.8 "$10\,\Omega$"
V2 4,1.8 -> 4,0 "$115\,\mathrm{V}$"
V3 8,3 -> 8,0 "$v_{dc}$"
R5 0,0 -> 4,0 "$20\,\Omega$"
R6 4,0 -> 8,0 "$25\,\Omega$"
label 0,3 "$a$" left
label 4,3 "$m$" above
label 8,3 "$b$" right
ground 4,0
```

<details><summary>Solution</summary>

1. (a) Node voltages: the condition $i_o=0$ is a statement about node voltages, $v_a=v_b$. Ground the bottom-middle wire.

   $$v_a=v_b,\qquad v_l=v_a-230$$
2. Apply KCL at $m$, and the left voltage source loop (no current in the $30\,\Omega$).

   $$\begin{aligned}(v_a-v_m)\big(\tfrac15+\tfrac1{15}\big)&=\tfrac{v_m-115}{10}\\\tfrac{v_a-v_m}{5}&=\tfrac{230-v_a}{20}\end{aligned}\;\Rightarrow\;v_a=170,\;v_m=155\,\mathrm{V}$$
3. (b) The $1\,\mathrm{A}$ in the $15\,\Omega$ flows through the $25\,\Omega$ and $v_{dc}$.

   $$v_r=-25\,\mathrm{V},\qquad v_{dc}=v_b-v_r=195\,\mathrm{V}$$
4. (c) Power balance.

   $$230(3)+195(1)=885\,\mathrm{W}=45+15+160+180+25+460$$

**Answer:** **(a)** Node voltages. **(b)** $v_{dc}=195\,\mathrm{V}$. **(c)** $885\,\mathrm{W}$ developed $=885\,\mathrm{W}$ absorbed.

</details>

**Problem: Textbook P4.59 · Opposing current sources transformed to a loop** (intermediate)

**(a)** Use source transformations to find $i_o$. **(b)** Check with the node-voltage method.

```schematic
I1 0,4 -> 0,0 "$6\,\mathrm{mA}$"
wire 0,4 -> 3,4
R1 3,4 -> 3,0 "$2.3\,\mathrm{k\Omega}$"
R2 7,4 -> 3,4 "$2.7\,\mathrm{k\Omega}$" i="$i_o$"
R3 7,4 -> 7,0 "$1\,\mathrm{k\Omega}$"
wire 7,4 -> 10,4
I2 10,0 -> 10,4 "$4.2\,\mathrm{mA}$"
wire 0,0 -> 10,0
label 3,4 "$a$" above
label 7,4 "$b$" above
ground 0,0
```

<details><summary>Solution</summary>

1. Swap both current sources (mA, kΩ, V).

   $$6\times2.3=13.8\,\mathrm{V},\qquad 4.2\times1=4.2\,\mathrm{V}$$
2. One series loop.

   $$i_o=\dfrac{13.8+4.2}{2.3+2.7+1}=3\,\mathrm{mA}$$
3. Node check (currents out).

   $$\begin{aligned}\tfrac{v_a}{2.3}+\tfrac{v_a-v_b}{2.7}+6&=0\\\tfrac{v_b}{1}+\tfrac{v_b-v_a}{2.7}&=4.2\end{aligned}\;\Rightarrow\;v_a=-6.9,\;v_b=1.2$$
4. Same current.

   $$i_o=\dfrac{1.2-(-6.9)}{2.7}=3\,\mathrm{mA}$$
5. For the nodal check, use kΩ and mA and the node labels shown.

   $$\begin{gathered}\dfrac{v_a}{2.3}+\dfrac{v_a-v_b}{2.7}=-6\\\dfrac{v_b}{1}+\dfrac{v_b-v_a}{2.7}=4.2\Rightarrow v_a=-6.9,\ v_b=1.2\,\mathrm{V}\\i_o=\dfrac{v_b-v_a}{2.7}=3\,\mathrm{mA}\end{gathered}$$

**Answer:** $i_o=3\,\mathrm{mA}$ (both ways).

</details>

**Problem: Lecture 4 p.9 · Source power after transformation** (intermediate)

Find the power of the $6\,\mathrm{V}$ source. Is it absorbed or delivered?

```schematic
V1 0,4 -> 0,0 "$6\,\mathrm{V}$"
R1 0,4 -> 4,4 "$4\,\Omega$"
R2 4,4 -> 4,0 "$30\,\Omega$"
R3 4,4 -> 8,4 "$6\,\Omega$"
R4 8,4 -> 8,0 "$20\,\Omega$"
R5 8,4 -> 12,4 "$5\,\Omega$"
V2 12,4 -> 12,0 "$40\,\mathrm{V}$"
wire 0,0 -> 4,0
R6 4,0 -> 8,0 "$10\,\Omega$"
wire 8,0 -> 12,0
label 4,4 "$c$" above
label 8,4 "$d$" above
label 8,0 "$f$" below
ground 0,0
```

<details><summary>Solution</summary>

1. Right side: three swaps.

   $$\tfrac{40}{5}=8\,\mathrm{A};\;\;5\parallel20=4\,\Omega;\;\;8\times4=32\,\mathrm{V};\;\;\tfrac{32}{6+4+10}=1.6\,\mathrm{A}$$
2. Left side.

   $$\tfrac{6}{4}=1.5\,\mathrm{A}$$
3. One node: both current sources into $4\parallel20\parallel30=3\,\Omega$.

   $$v_c=(1.5+1.6)(3)=9.3\,\mathrm{V}$$
4. Back to the original.

   $$i=\dfrac{6-9.3}{4}=-0.825\,\mathrm{A}\;\Rightarrow\;p=(6)(0.825)=4.95\,\mathrm{W}\text{ absorbed}$$

**Answer:** The $6\,\mathrm{V}$ source **absorbs** $4.95\,\mathrm{W}$.

</details>

**Problem: Textbook P4.60 · A current source parallel to a resistor** (intermediate)

**(a)** Use source transformations to find $i_o$. **(b)** Check with the mesh-current method.

```schematic
I1 0,0 -> 0,4 "$4\,\mathrm{A}$"
wire 0,4 -> 3,4
R1 3,4 -> 3,0 "$5\,\Omega$"
R2 3,4 -> 6,4 "$4\,\Omega$"
R3 6,4 -> 9,4 "$1\,\Omega$"
wire 6,4 -> 6,6
I2 9,6 -> 6,6 "$10\,\mathrm{A}$"
wire 9,6 -> 9,4
R4 9,4 -> 9,2 "$40\,\Omega$"
V1 9,2 -> 9,0 "$10\,\mathrm{V}$"
wire 9,4 -> 12,4
R5 12,4 -> 12,0 "$2\,\Omega$" i="$i_o$"
wire 0,0 -> 12,0
label 3,4 "$p$" above
label 6,4 "$q$" below
label 9,4 "$r$" below
ground 0,0
```

<details><summary>Solution</summary>

1. Swap both current sources.

   $$4\times5=20\,\mathrm{V},\qquad 10\times1=10\,\mathrm{V}$$
2. Node $r$ with three branches: $10\,\mathrm{V}$ behind $10\,\Omega$, $10\,\mathrm{V}$ behind $40\,\Omega$, $2\,\Omega$ to ground.

   $$\dfrac{v_r-10}{10}+\dfrac{v_r-10}{40}+\dfrac{v_r}{2}=0\;\Rightarrow\;v_r=2\,\mathrm{V}$$
3. Answer.

   $$i_o=\dfrac{2}{2}=1\,\mathrm{A}$$
4. For the mesh check, number meshes from the 4 A perimeter source, the large left interior, the 10 A top source, and the rightmost loop. Choose all clockwise.

   $$I_A=4\,\mathrm{A},\qquad I_C=-10\,\mathrm{A}$$
5. KVL in the two unknown meshes gives the following equations after those current constraints.

   $$50I_B-40I_D=0,\qquad-40I_B+42I_D=10$$
6. Substitute $I_B=0.8I_D$; the rightmost mesh current is the requested current.

   $$10I_D=10\Rightarrow I_D=i_o=1\,\mathrm{A}$$

**Answer:** $i_o=1\,\mathrm{A}$.

</details>

**Problem: Textbook P4.61 · Reversed polarity and original source power** (intermediate)

**(a)** Use source transformations to find $i_o$. **(b)** Work back to find the power developed by the $100\,\mathrm{V}$ source.

```schematic
V1 0,0 -> 0,3 "$100\,\mathrm{V}$"
R1 0,3 -> 3,3 "$20\,\mathrm{k\Omega}$"
R2 3,3 -> 3,0 "$80\,\mathrm{k\Omega}$"
R3 3,3 -> 6,3 "$3\,\mathrm{k\Omega}$"
I1 6,0 -> 6,3 "$12\,\mathrm{mA}$"
wire 6,3 -> 9,3
R4 9,3 -> 9,0 "$60\,\mathrm{k\Omega}$"
R5 9,3 -> 12,3 "$5\,\mathrm{k\Omega}$"
R6 12,3 -> 12,0 "$10\,\mathrm{k\Omega}$" i="$i_o$"
wire 0,0 -> 3,0
R7 3,0 -> 6,0 "$1\,\mathrm{k\Omega}$"
wire 6,0 -> 12,0
label 3,3 "$p$" above
label 6,3 "$q$" above
label 12,3 "$r$" above
label 3,0 "$l$" below
ground 6,0
```

<details><summary>Solution</summary>

1. Left side, swapped down to one source (kΩ, mA, V measured from the bottom-right wire).

   $$\tfrac{100}{20}=5\,\mathrm{mA};\;\;20\parallel80=16;\;\;5(16)=80\,\mathrm{V};\;\;16+3+1=20\,\mathrm{k\Omega}$$
2. Apply KCL at $q$.

   $$\dfrac{q+80}{20}+\dfrac{q}{60}+\dfrac{q}{15}=12\;\Rightarrow\;q=60\,\mathrm{V},\qquad i_o=\dfrac{60}{5+10}=4\,\mathrm{mA}$$
3. Recover original node voltages, using the lower-right node as ground. KCL at the 60 V node gives the middle-left voltage $p=39$ V. Let the left source lower node be $l$, so its upper node is $l-100$.

   $$\begin{gathered}\dfrac{60-p}{3}+\dfrac{60}{60}+\dfrac{60}{15}=12\Rightarrow p=39\\\dfrac{l-39}{80}+\dfrac{l-100-39}{20}+l=0\Rightarrow l=7\,\mathrm{V}\end{gathered}$$
4. The 20 kΩ current enters the voltage source negative terminal, so the source delivers power.

   $$i=\dfrac{39-(-93)}{20}=6.6\,\mathrm{mA},\quad P_{100,\mathrm{del}}=100(6.6)=660\,\mathrm{mW}$$

**Answer:** **(a)** $i_o=4\,\mathrm{mA}$. **(b)** The $100\,\mathrm{V}$ source develops $660\,\mathrm{mW}$.

</details>

**Problem: Textbook P4.62 · Transform both ends and check with mesh analysis** (intermediate)

**(a)** Make a series of source transformations to find $v_o$. **(b)** Check with the mesh-current method.

```schematic
I1 0,3 -> 0,0 "$2.5\,\mathrm{mA}$"
wire 0,3 -> 2,3
R1 2,3 -> 2,0 "$8\,\mathrm{k\Omega}$"
R2 2,3 -> 5,3 "$24\,\mathrm{k\Omega}$" v="$v_o$"
R3 5,3 -> 5,0 "$80\,\mathrm{k\Omega}$"
R4 5,3 -> 8,3 "$15\,\mathrm{k\Omega}$"
V1 8,3 -> 11,3 "$40\,\mathrm{V}$"
R5 11,3 -> 11,0 "$5\,\mathrm{k\Omega}$"
wire 11,3 -> 13,3
I2 13,0 -> 13,3 "$12\,\mathrm{mA}$"
wire 0,0 -> 13,0
label 2,3 "$a$" above
label 5,3 "$b$" above
label 8,3 "$c$" below
label 11,3 "$d$" below
ground 0,0
```

<details><summary>Solution</summary>

1. Swap both current sources (kΩ, mA, V).

   $$\begin{aligned}&2.5(8)=20\,\mathrm{V},\qquad 12(5)=60\,\mathrm{V}\\&\text{right side: }60+40=100\,\mathrm{V}\text{ behind }20\,\mathrm{k\Omega}\end{aligned}$$
2. Apply KCL at $b$ (the left side is $-20\,\mathrm{V}$ behind $8+24=32\,\mathrm{k\Omega}$).

   $$\dfrac{v_b-100}{20}+\dfrac{v_b+20}{32}+\dfrac{v_b}{80}=0\;\Rightarrow\;v_b=46.67\,\mathrm{V}$$
3. The $24\,\mathrm{k\Omega}$.

   $$i=\dfrac{46.67+20}{32}=2.083\,\mathrm{mA},\qquad v_o=-24(2.083)=-50\,\mathrm{V}$$
4. For the mesh check, choose clockwise meshes from left to right. The left and right perimeter current sources fix the outside meshes.

   $$I_A=-2.5\,\mathrm{mA},\quad I_D=-12\,\mathrm{mA}$$
5. The two interior meshes have KVL equations in kΩ and mA.

   $$112I_B-80I_C=-20,\qquad-80I_B+100I_C=-100$$
6. Solve the simultaneous equations and use the 24 kΩ branch reference.

   $$I_B=-\dfrac{25}{12}\,\mathrm{mA},\quad I_C=-\frac83\,\mathrm{mA},\quad v_o=24I_B=-50\,\mathrm{V}$$

**Answer:** $v_o=-50\,\mathrm{V}$

</details>

**Problem: Textbook P4.64 · Norton equivalent with a shorted internal branch** (intermediate)

Find the Norton equivalent at $a$–$b$.

```schematic
I1 0,0 -> 0,4 "$15\,\mathrm{A}$"
wire 0,4 -> 3,4
R1 3,4 -> 3,0 "$8\,\Omega$"
R2 3,4 -> 6,4 "$2\,\Omega$"
R3 6,4 -> 6,0 "$12\,\Omega$"
wire 6,4 -> 9,4
terminal 9,4 "$a$" right
wire 0,0 -> 3,0
R4 3,0 -> 6,0 "$10\,\Omega$"
wire 6,0 -> 9,0
terminal 9,0 "$b$" right
label 3,4 "$p$" above
label 3,0 "$q$" below
ground 6,0
```

<details><summary>Solution</summary>

1. Short: current divider between $8\,\Omega$ and $2+10\,\Omega$.

   $$I_N=15\cdot\dfrac{8}{8+12}=6\,\mathrm{A}$$
2. Current source off (a gap).

   $$R_N=12\parallel(2+8+10)=7.5\,\Omega$$
3. Check.

   $$v_{oc}=I_NR_N=45\,\mathrm{V}=(3.75)(12)$$

**Answer:** $I_N=6\,\mathrm{A}$ (toward $a$) ∥ $R_N=7.5\,\Omega$.

</details>

**Problem: Textbook P4.67 · Negative Norton current** (intermediate)

Find the Norton equivalent at $a$–$b$.

```schematic
I1 0,0 -> 0,3 "$10\,\mathrm{mA}$"
R1 2,3 -> 2,0 "$10\,\mathrm{k\Omega}$"
V1 4,3 -> 4,0 "$30\,\mathrm{V}$"
wire 0,3 -> 4,3
R2 4,3 -> 7,3 "$15\,\mathrm{k\Omega}$"
I2 7,3 -> 7,0 "$3\,\mathrm{mA}$"
R3 9,3 -> 9,0 "$5\,\mathrm{k\Omega}$"
wire 7,3 -> 11,3
terminal 11,3 "$a$" right
terminal 11,0 "$b$" right
wire 0,0 -> 11,0
ground 0,0
```

<details><summary>Solution</summary>

1. Ground b and short a to b. The ideal 30 V source fixes the left node at 30 V. Define the external short-circuit current from a to b.

   $$i_{15\mathrm{k}}=\dfrac{30}{15}=2\,\mathrm{mA},\quad i_{sc}=2-3=-1\,\mathrm{mA}$$
2. Deactivate independent sources: short the 30 V source and open both current sources. The 10 kΩ resistor is bypassed by the shorted voltage source.

   $$R_N=15\parallel5=3.75\,\mathrm{k\Omega}$$
3. Use the negative Norton current to state the actual source direction and confirm the open-circuit voltage.

   $$V_{\mathrm{Th}}=I_NR_N=(-1)(3.75)=-3.75\,\mathrm{V}$$

**Answer:** $I_N=-1\,\mathrm{mA}$ (so $1\,\mathrm{mA}$ points from $a$ to $b$ inside the source) in parallel with $R_N=3.75\,\mathrm{k\Omega}$.

</details>

**Problem: Textbook P4.69 · Recover an equivalent from two measurements** (intermediate)

A box holds an unknown linear circuit. A $15\,\mathrm{k\Omega}$ load on $a$–$b$ reads $v_{ab}=45\,\mathrm{V}$; a $5\,\mathrm{k\Omega}$ load reads $25\,\mathrm{V}$. Find the Thévenin equivalent.

```schematic
X1 0,3 -> 0,0 "network"
wire 0,3 -> 3,3
wire 0,0 -> 3,0
RL 3,3 -> 3,0 "$R_L$" flip
terminal 3,3 "$a$" above
terminal 3,0 "$b$" below
ground 0,0
```

<details><summary>Solution</summary>

1. Load currents.

   $$i_1=\dfrac{45}{15}=3\,\mathrm{mA},\qquad i_2=\dfrac{25}{5}=5\,\mathrm{mA}$$
2. Two points on $v=V_{\mathrm{Th}}-R_{\mathrm{Th}}i$ (kΩ, mA).

   $$\begin{aligned}45&=V_{\mathrm{Th}}-3R_{\mathrm{Th}}\\25&=V_{\mathrm{Th}}-5R_{\mathrm{Th}}\end{aligned}$$
3. Subtract.

   $$R_{\mathrm{Th}}=10\,\mathrm{k\Omega},\qquad V_{\mathrm{Th}}=75\,\mathrm{V}$$

**Answer:** $V_{\mathrm{Th}}=75\,\mathrm{V}$, $R_{\mathrm{Th}}=10\,\mathrm{k\Omega}$.

</details>

**Problem: Textbook P4.68 · Two-source network and an open port** (intermediate)

Find the Thévenin equivalent at $a$–$b$.

```schematic
V1 0,3 -> 0,0 "$300\,\mathrm{V}$"
R1 0,3 -> 4,3 "$40\,\Omega$"
R2 4,3 -> 4,0 "$8\,\Omega$"
R3 4,3 -> 8,3 "$10\,\Omega$"
wire 0,3 -> 0,5
R4 0,5 -> 8,5 "$150\,\Omega$"
wire 8,5 -> 8,3
wire 0,5 -> 0,7
I1 8,7 -> 0,7 "$3\,\mathrm{A}$"
wire 8,7 -> 8,5
wire 8,3 -> 10,3
terminal 10,3 "$a$" right
terminal 10,0 "$b$" right
wire 0,0 -> 10,0
label 4,3 "$m$" above
ground 0,0
```

<details><summary>Solution</summary>

1. Ground b. The 300 V source fixes the left node. Write KCL at the middle node m and open output a; the 3 A source flows from a toward the 300 V node.

   $$\begin{aligned}\dfrac{v_m-300}{40}+\dfrac{v_m}{8}+\dfrac{v_m-v_a}{10}&=0\\\dfrac{v_a-300}{150}+\dfrac{v_a-v_m}{10}+3&=0\end{aligned}$$
2. Clear fractions, express $v_m$ from the first equation and substitute into the second.

   $$10v_m-4v_a=300\Rightarrow v_m=30+0.4v_a;\quad16v_a-15v_m=-150$$
3. Solve for the open-circuit voltage.

   $$16v_a-15(30+0.4v_a)=-150\Rightarrow v_a=V_{\mathrm{Th}}=30\,\mathrm{V}$$
4. Short the voltage source and open the current source for the resistance calculation.

   $$R_{\mathrm{Th}}=150\parallel\left[10+(40\parallel8)\right]=15\,\Omega$$

**Answer:** $V_{\mathrm{Th}}=30\,\mathrm{V}$, $R_{\mathrm{Th}}=15\,\Omega$.

</details>

**Problem: Textbook P4.77 · Compare open/short and deactivation methods** (intermediate)

**(a)** Find the Thévenin equivalent at $a$–$b$ from the open-circuit voltage and the short-circuit current. **(b)** Find $R_{\mathrm{Th}}$ by removing the sources and compare.

```schematic
V1 0,3 -> 0,0 "$17.4\,\mathrm{V}$"
R1 0,3 -> 4,3 "$40\,\Omega$"
R2 4,3 -> 4,0 "$15\,\Omega$"
I1 4,3 -> 8,3 "$100\,\mathrm{mA}$"
wire 0,3 -> 0,5
R3 0,5 -> 8,5 "$26\,\Omega$"
wire 8,5 -> 8,3
R4 8,3 -> 8,0 "$10\,\Omega$"
wire 0,0 -> 4,0
R5 4,0 -> 8,0 "$4\,\Omega$"
wire 8,3 -> 10,3
wire 8,0 -> 10,0
terminal 10,3 "$a$" right
terminal 10,0 "$b$" right
label 4,3 "$p$" above
ground 0,0
```

<details><summary>Solution</summary>

1. Use the bottom-left node as ground. The source top is 17.4 V. Write KCL at p, a and b; retain the internal 10 Ω resistor even when the external port is open.

   $$\begin{aligned}\dfrac{v_p-17.4}{40}+\dfrac{v_p}{15}+0.1&=0\\\dfrac{v_a-17.4}{26}+\dfrac{v_a-v_b}{10}&=0.1\\\dfrac{v_b-v_a}{10}+\dfrac{v_b}{4}&=0\end{aligned}$$
2. The last equation gives $v_a=3.5v_b$. Substitute into the middle equation.

   $$\dfrac{3.5v_b-17.4}{26}+\dfrac{2.5v_b}{10}=0.1\Rightarrow v_b=2,\ v_a=7\,\mathrm{V},\quad V_{\mathrm{Th}}=5\,\mathrm{V}$$
3. For the short-circuit calculation set $v_a=v_b=t$. Write KCL for the joined node, then find external short current.

   $$\dfrac{t-17.4}{26}+\frac t4=0.1\Rightarrow t=\frac83\,\mathrm{V},\quad i_{sc}=\dfrac{17.4-t}{26}+0.1=\frac23\,\mathrm{A}$$
4. Use the ratio, then independently deactivate sources to verify the resistance.

   $$R_{\mathrm{Th}}=\frac5{2/3}=7.5\,\Omega=10\parallel(26+4)$$

**Answer:** $V_{\mathrm{Th}}=5\,\mathrm{V}$, $R_{\mathrm{Th}}=7.5\,\Omega$ (both ways).

</details>

**Problem: Textbook P4.63 · Recover every original source power** (advanced)

**(a)** Use source transformations to find $v_o$. **(b)** Find the power developed by the $340\,\mathrm{V}$ source and **(c)** by the $5\,\mathrm{A}$ source. **(d)** Check the power balance.

```schematic
I1 0,0 -> 0,4 "$5\,\mathrm{A}$"
R1 0,4 -> 3,4 "$8\,\Omega$"
R2 3,4 -> 3,0 "$20\,\Omega$"
wire 3,4 -> 3,7
V1 3,7 -> 6,7 "$340\,\mathrm{V}$"
wire 6,7 -> 6,4
R3 3,4 -> 6,4 "$80\,\Omega$"
R4 6,4 -> 9,4 "$5\,\Omega$"
wire 9,4 -> 12,4
R5 12,4 -> 12,0 "$45\,\Omega$"
wire 0,0 -> 3,0
R6 3,0 -> 9,0 "$10\,\Omega$"
wire 9,0 -> 12,0
gap 9,4 -> 9,0 v="$v_o$"
label 3,4 "$q$" above
label 6,4 "$r$" above
label 9,0 "$m$" below
ground 0,0
```

<details><summary>Solution</summary>

1. Drop the $8\,\Omega$ and $80\,\Omega$; swap the current source.

   $$5\times20=100\,\mathrm{V}$$
2. One loop, clockwise.

   $$\begin{aligned}100-340&=(20+5+45+10)\,i\;\Rightarrow\;i=-3\,\mathrm{A}\\v_o&=45i=-135\,\mathrm{V}\end{aligned}$$
3. $340\,\mathrm{V}$ source.

   $$i=3+\tfrac{340}{80}=7.25\,\mathrm{A},\qquad p=2465\,\mathrm{W}$$
4. $5\,\mathrm{A}$ source.

   $$v=20(8)+8(5)=200\,\mathrm{V},\qquad p=1000\,\mathrm{W}$$
5. Balance.

   $$2465+1000=3465=200+1280+1445+45+405+90$$

**Answer:** **(a)** $v_o=-135\,\mathrm{V}$ **(b)** $2465\,\mathrm{W}$ **(c)** $1000\,\mathrm{W}$ **(d)** $3465\,\mathrm{W}$ both ways.

</details>

**Problem: Textbook P4.56 · Adjust a current source to meet a power condition** (intermediate)

The variable current source $i_{dc}$ is adjusted so that the $15\,\mathrm{A}$ source develops $3750\,\mathrm{W}$. **(a)** Node or mesh? **(b)** Find $i_{dc}$.

```schematic
V1 0,3 -> 0,0 "$420\,\mathrm{V}$"
R1 0,3 -> 3,3 "$7.2\,\Omega$"
R2 3,3 -> 3,0 "$20\,\Omega$"
R3 3,3 -> 6,3 "$15\,\Omega$"
wire 3,3 -> 3,5
I1 6,5 -> 3,5 "$15\,\mathrm{A}$"
wire 6,5 -> 6,3
R4 6,3 -> 6,0 "$50\,\Omega$"
wire 6,3 -> 9,3
I2 9,3 -> 9,0 "$i_{dc}$"
wire 0,0 -> 3,0
R5 3,0 -> 6,0 "$40\,\Omega$"
wire 6,0 -> 9,0
label 3,3 "$p$" above
label 6,3 "$q$" below
label 6,0 "$m$" below
ground 0,0
```

<details><summary>Solution</summary>

1. (a) Node voltages: the given power is a statement about the node voltage difference across the current source.

   $$15\,(v_p-v_q)=3750\;\Rightarrow\;v_p-v_q=250\,\mathrm{V}$$
2. Apply KCL at $p$.

   $$\dfrac{420-v_p}{7.2}+15=\dfrac{v_p}{20}+\dfrac{250}{15}\;\Rightarrow\;v_p=300,\;v_q=50\,\mathrm{V}$$
3. Apply KCL at $q$ and $m$.

   $$\begin{aligned}\tfrac{250}{15}&=15+\tfrac{50-v_m}{50}+i_{dc}\\\tfrac{50-v_m}{50}+i_{dc}&=\tfrac{v_m}{40}\end{aligned}\;\Rightarrow\;v_m=66.67\,\mathrm{V},\;i_{dc}=2\,\mathrm{A}$$

**Answer:** **(a)** Node voltages. **(b)** $i_{dc}=2\,\mathrm{A}$.

</details>

**Problem: Textbook P4.73 · Voltmeter loading and signed error** (intermediate)

A $100\,\mathrm{k\Omega}$ voltmeter measures $v_{ab}$. **(a)** What does it read? **(b)** What is the percentage error, $\dfrac{\text{measured}-\text{actual}}{\text{actual}}\times100$?

```schematic
R1 0,6 -> 0,3 "$10\,\mathrm{k\Omega}$"
V1 0,3 -> 0,0 "$30\,\mathrm{V}$"
wire 0,6 -> 3,6
R2 3,6 -> 3,0 "$40\,\mathrm{k\Omega}$"
R3 3,6 -> 6,6 "$4\,\mathrm{k\Omega}$"
I1 6,0 -> 6,6 "$8\,\mathrm{mA}$"
R4 6,6 -> 9,6 "$3\,\mathrm{k\Omega}$"
R5 9,6 -> 9,0 "$10\,\mathrm{k\Omega}$"
wire 9,6 -> 11,6
terminal 11,6 "$a$" right
terminal 11,0 "$b$" right
wire 0,0 -> 11,0
label 3,6 "$p$" above
label 6,6 "$q$" above
ground 0,0
```

<details><summary>Solution</summary>

1. Ground b. For an ideal open-port measurement, name the left upper node x, middle upper node y and output node a. Use kΩ and mA.

   $$15v_x-10v_y=120,\quad7v_y-3v_x-4v_a=96,\quad13v_a-10v_y=0$$
2. Substitute $v_y=1.3v_a$ and $v_x=8+(13/15)v_a$ into the middle equation.

   $$2.5v_a=120\Rightarrow V_{\mathrm{Th}}=48\,\mathrm{V}$$
3. Deactivate the independent sources and calculate the resistance seen from a–b.

   $$R_{\mathrm{Th}}=[(10\parallel40)+4+3]\parallel10=6\,\mathrm{k\Omega}$$
4. The real 100 kΩ voltmeter is a load. Use the loaded equivalent.

   $$v_m=48\dfrac{100}{6+100}=45.283\,\mathrm{V}$$
5. Calculate signed error against the ideal open-port voltage.

   $$\dfrac{45.283-48}{48}\,100=-5.66\%$$

**Answer:** **(a)** $45.28\,\mathrm{V}$ **(b)** $-5.66\%$

</details>

**Problem: Textbook P4.70 · Small current in an unbalanced bridge** (advanced)

The bridge is balanced when $R_3=1200\,\Omega$. With $R_3=1204\,\Omega$, how much current does the $30\,\Omega$ galvanometer detect? (Hint: find the Thévenin equivalent across the galvanometer.)

```schematic
V1 0,4 -> 0,0 "$120\,\mathrm{V}$"
wire 0,4 -> 9,4
R1 3,4 -> 3,2 "$900\,\Omega$"
R2 3,2 -> 3,0 "$600\,\Omega$"
R3 9,4 -> 9,2 "$1204\,\Omega$"
R4 9,2 -> 9,0 "$R_x=800\,\Omega$"
RG 3,2 -> 9,2 "galvanometer $30\,\Omega$"
wire 0,0 -> 9,0
label 3,2 "$l$" left
label 9,2 "$r$" right
ground 0,0
```

<details><summary>Solution</summary>

1. Thévenin across the galvanometer: two dividers.

   $$V_{\mathrm{Th}}=120\Big(\dfrac{600}{1500}-\dfrac{800}{2004}\Big)=95.8\,\mathrm{mV}$$
2. Deactivate the 120 V source to a short, then find the resistance seen by the removed galvanometer.

   $$R_{\mathrm{Th}}=900\parallel600+1204\parallel800=840.6\,\Omega$$
3. The galvanometer is the load.

   $$i=\dfrac{0.0958}{840.6+30}=110\,\mu\mathrm{A}$$

**Answer:** About $110\,\mu\mathrm{A}$, from $l$ to $r$.

</details>

**Problem: Textbook P4.57 · Choose a method for source power with two supernodes** (advanced)

**(a)** Choose nodal or mesh analysis to find the power absorbed by the $10\,\mathrm{V}$ source and explain the choice. **(b)** Find the power. The current source is $v_x/(2\,\Omega)$; the dependent voltage source is $(2\,\Omega)i_x$.

```schematic
R1 0,3 -> 0,0 "$25\,\Omega$"
V1 0,3 -> 3,3 "$10\,\mathrm{V}$"
R2 3,3 -> 3,0 "$5\,\Omega$" v="$v_x$"
I1 3,3 -> 6,3 "$10\,\mathrm{A}$"
R3 6,0 -> 6,3 "$4\,\Omega$" i="$i_x$"
E1 9,3 -> 6,3 "$2i_x$"
R4 9,3 -> 9,0 "$2\,\Omega$"
wire 0,3 -> 0,5
G1 9,5 -> 0,5 "$v_x/2$"
wire 9,5 -> 9,3
wire 0,0 -> 9,0
label 0,3 "$a$" left
label 3,3 "$b$" above
label 6,3 "$c$" above
label 9,3 "$d$" right
ground 0,0
```

<details><summary>Solution</summary>

1. Use nodal analysis. Ground the bottom node. The left supernode KCL and its 10 V constraint determine $v_a$ and $v_b$ without solving the right-hand circuit.
2. The source gives $v_a=v_b+10$. Write KCL around the left supernode: the top dependent current source enters it.

   $$\dfrac{v_a}{25}+\dfrac{v_b}{5}+10-\dfrac{v_b}{2}=0$$
3. Substitute and clear the denominator.

   $$\dfrac{v_b+10}{25}+\dfrac{v_b}{5}+10-\dfrac{v_b}{2}=0\Rightarrow -13v_b+520=0\Rightarrow v_b=40,\ v_a=50\,\mathrm{V}$$
4. Find the current through the 10 V source with KCL at $a$. Define $i_{10}$ from its + terminal at $a$ to its − terminal at $b$.

   $$\dfrac{50}{25}+i_{10}-\dfrac{40}{2}=0\Rightarrow i_{10}=18\,\mathrm{A}$$
5. Use absorbed power because the requested current reference enters +.

   $$p_{10\mathrm{V},\mathrm{abs}}=10(18)=180\,\mathrm{W}$$

**Answer:** **(a)** Nodal analysis: the left supernode directly gives the required source current. **(b)** $180\,\mathrm{W}$ absorbed.

</details>

**Problem: Textbook P4.71 · Infer a battery equivalent from two real loads** (intermediate)

A battery supplies $12.5\,\mathrm{V}$ to a radio modeled as $6.25\,\Omega$, and $11.7\,\mathrm{V}$ to headlights modeled as $0.65\,\Omega$. Find the battery's Thévenin and Norton equivalents. The diagram shows the equivalent model to determine; use one load at a time.

```schematic
V1 0,3 -> 0,0 "$V_{\mathrm{Th}}$"
R1 0,3 -> 4,3 "$R_{\mathrm{Th}}$"
wire 4,3 -> 6,3
RL 6,3 -> 6,0 "$R_L$" v="$v_L$"
wire 0,0 -> 6,0
terminal 4,3 "$a$" above
terminal 4,0 "$b$" below
ground 0,0
```

<details><summary>Solution</summary>

1. Calculate each load current with Ohm's law.

   $$i_1=\dfrac{12.5}{6.25}=2\,\mathrm{A},\qquad i_2=\dfrac{11.7}{0.65}=18\,\mathrm{A}$$
2. Write the terminal relation for each measurement.

   $$12.5=V_{\mathrm{Th}}-2R_{\mathrm{Th}},\qquad11.7=V_{\mathrm{Th}}-18R_{\mathrm{Th}}$$
3. Subtract to eliminate the source voltage, then back-substitute.

   $$0.8=16R_{\mathrm{Th}}\Rightarrow R_{\mathrm{Th}}=0.05\,\Omega,\quad V_{\mathrm{Th}}=12.5+2(0.05)=12.6\,\mathrm{V}$$
4. Convert to Norton form. Its source arrow points from b toward a.

   $$I_N=\dfrac{12.6}{0.05}=252\,\mathrm{A},\quad R_N=0.05\,\Omega$$

**Answer:** Thévenin: $12.6\,\mathrm{V}$ in series with $0.05\,\Omega$. Norton: $252\,\mathrm{A}$ from $b$ to $a$ in parallel with $0.05\,\Omega$.

</details>

**Problem: Textbook P4.76 · An ammeter changes the current it measures** (advanced)

An ammeter measuring the downward current $i_\phi$ reads $6\,\mathrm{A}$. **(a)** Find its resistance. **(b)** Find the percentage error in the current measurement. In the redrawn circuit, $R_m$ models the ammeter's internal resistance in series with the $4.8\,\Omega$ resistor. The dependent source remains controlled by the current in that branch.

```schematic
V1 0,5 -> 0,0 "$24\,\mathrm{V}$"
R1 0,5 -> 3,5 "$2\,\Omega$"
R2 3,5 -> 3,2.5 "$4.8\,\Omega$" i="$i_\phi$"
RM 3,2.5 -> 3,0 "$R_m$"
wire 3,5 -> 9,5
R3 6,5 -> 6,0 "$100\,\Omega$"
R4 9,5 -> 9,0 "$25\,\Omega$"
wire 3,5 -> 3,7
R5 3,7 -> 12,7 "$4\,\Omega$"
wire 12,7 -> 12,5
R6 12,5 -> 12,0 "$16\,\Omega$"
wire 0,5 -> 0,9
G1 0,9 -> 12,9 "$2.5i_\phi$"
wire 12,9 -> 12,5
wire 0,0 -> 12,0
label 3,5 "$m$" left
label 12,5 "$r$" right
ground 0,0
```

<details><summary>Solution</summary>

1. Ground the bottom node. The measured control current makes the dependent source 15 A; combine 100 Ω and 25 Ω to 20 Ω.

   $$i_\phi=6\,\mathrm{A},\quad 2.5i_\phi=15\,\mathrm{A},\quad100\parallel25=20\,\Omega$$
2. Write KCL at the central node $m$ and right node $r$. Use the measured 6 A for the ammeter branch.

   $$\begin{aligned}\dfrac{v_m-24}{2}+\dfrac{v_m-v_r}{4}+\dfrac{v_m}{20}+6&=0\\\dfrac{v_r-v_m}{4}+\dfrac{v_r}{16}&=15\end{aligned}$$
3. Clear fractions, express $v_r$, and substitute.

   $$\begin{gathered}16v_m-5v_r=120\\5v_r-4v_m=240\Rightarrow12v_m=360\Rightarrow v_m=30,\ v_r=72\,\mathrm{V}\end{gathered}$$
4. The measured branch contains the original resistor and the meter in series.

   $$30=6(4.8+R_m)\Rightarrow R_m=0.2\,\Omega$$
5. For the true unmeasured current, remove $R_m$. Recalculate the dependent source with $i_\phi=v_m/4.8$; it is no longer fixed at 15 A.

   $$\begin{aligned}\dfrac{v_m-24}{2}+\dfrac{v_m-v_r}{4}+\dfrac{v_m}{20}+\dfrac{v_m}{4.8}&=0\\\dfrac{v_r-v_m}{4}+\dfrac{v_r}{16}&=2.5\dfrac{v_m}{4.8}\end{aligned}$$
6. The second equation gives $v_r=37v_m/15$. Substitute into the first.

   $$\dfrac{47}{120}v_m=12\Rightarrow i_{\mathrm{true}}=\dfrac{v_m}{4.8}=\dfrac{300}{47}\approx6.383\,\mathrm{A}$$
7. Use signed error relative to the true current.

   $$\%\mathrm{error}=\dfrac{6-300/47}{300/47}\,100=-6\%$$

**Answer:** **(a)** $R_m=0.2\,\Omega$. **(b)** The meter reads $6\%$ low; the true current is about $6.383\,\mathrm{A}$.

</details>

**Problem: Tutorial P3.2 · Open load, connected load and accidental short** (intermediate)

From the uploaded Week 4 tutorial: **(a)** find the no-load $v_o$; **(b)** find $v_o$ for $R_L=150\,\mathrm{k\Omega}$; **(c)** find the power in $25\,\mathrm{k\Omega}$ if the load terminals are shorted; **(d)** find the maximum power dissipated in the fixed $75\,\mathrm{k\Omega}$ resistor as the passive load changes.

```schematic
V1 0,4 -> 0,0 "$200\,\mathrm{V}$"
R1 0,4 -> 3,4 "$25\,\mathrm{k\Omega}$"
R2 3,4 -> 3,0 "$75\,\mathrm{k\Omega}$" v="$v_o$"
wire 3,4 -> 6,4
RL 6,4 -> 6,0 "$R_L$"
wire 0,0 -> 6,0
label 3,4 "$a$" above
ground 0,0
```

<details><summary>Solution</summary>

1. For no load, open $R_L$; the fixed 75 kΩ resistor remains. Use kΩ and mA.

   $$v_{o,\mathrm{open}}=200\dfrac{75}{25+75}=150\,\mathrm{V}$$
2. Find the equivalent seen by $R_L$. The source is shorted only for the resistance calculation.

   $$V_{\mathrm{Th}}=150\,\mathrm{V},\quad R_{\mathrm{Th}}=25\parallel75=18.75\,\mathrm{k\Omega}$$
3. Reconnect the specified load. Check with KCL in the original circuit.

   $$v_o=150\dfrac{150}{18.75+150}=133.33\,\mathrm{V};\quad\dfrac{200-v_o}{25}=\dfrac{v_o}{75}+\dfrac{v_o}{150}$$
4. For a shorted load, $v_o=0$. The 25 kΩ resistor has the full 200 V across it.

   $$P_{25}=\dfrac{200^2}{25000}=1.6\,\mathrm{W}$$
5. Part (d) concerns the fixed 75 kΩ resistor, not the adjustable load. Its voltage is greatest with the load open.

   $$P_{75,\max}=\dfrac{150^2}{75000}=0.3\,\mathrm{W}$$

**Answer:** **(a)** $150\,\mathrm{V}$. **(b)** $133.33\,\mathrm{V}$. **(c)** $1.6\,\mathrm{W}$. **(d)** $0.3\,\mathrm{W}$, with $R_L$ open.

</details>

## Summary

- Method choice compares the equations left after using valid source constraints.
- A source transformation preserves the behavior at the chosen terminals.
- Thévenin uses a voltage source in series with resistance; Norton uses a current source in parallel with resistance.
- Calculate the open circuit, short circuit and sources-deactivated circuit separately.
- Keep dependent sources active; use a test source when required.
- Real voltmeters and ammeters alter the circuit; use their finite resistance.
- Use the original circuit for original source powers.

### Formula sheet

| Result | Formula | Use when |
|---|---|---|
| Source transformation | $I_s=\dfrac{V_s}{R}$, $V_s=I_sR$ | V source + series R ↔ I source ∥ R. |
| Thévenin voltage | $V_{\mathrm{Th}}=v_{ab,\mathrm{open}}$ | The external load is disconnected. |
| Norton current | $I_N=i_{sc}$ | External short current reference is a to b. |
| Equivalent resistance | $R_N=R_{\mathrm{Th}}=\dfrac{V_{\mathrm{Th}}}{I_N}$ | The ratio is defined and the equivalent is valid. |
| Test source | $R_{\mathrm{Th}}=\dfrac{v_T}{i_T}$ | Independent sources off; dependent sources on; test current enters a. |
| Load current | $i_L=\dfrac{V_{\mathrm{Th}}}{R_{\mathrm{Th}}+R_L}$ | Load connected from a to b. |
| Measurement error | $\dfrac{\mathrm{measured}-\mathrm{true}}{\mathrm{true}}\,100\%$ | Compare a real meter with the circuit without that meter. |
