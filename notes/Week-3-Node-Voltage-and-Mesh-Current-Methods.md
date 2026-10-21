# Week 3: Nodal and Mesh Analysis — Equations, Shared Currents and Practice

## Overview

> **Info:** This week gives you two systematic ways to solve circuits: nodal analysis finds node voltages using KCL; mesh analysis finds mesh currents using KVL. Both use Ohm's law. The worked examples show the setup, equations, substitution and interpretation of signs; the practice set focuses on different circuit structures.

- Identify nodes, branches and meshes, and choose a useful ground node.
- Write each resistor current as a voltage difference divided by its resistance.
- Handle voltage sources with source constraints and supernodes.
- Translate mesh currents into shared-branch currents.
- Handle current sources with known mesh currents or supermeshes.
- Include the controlling equations of dependent sources, then check currents and power.

## Topic 1: Nodes, branches and meshes

*Source: ELEC 221 Week 3.pdf, PDF p. 6; ELEC 221 Week 3.pdf, PDF p. 7*

| Term | What to identify on the diagram |
|---|---|
| Node | All points connected by ideal wire belong to the same node, even if the wire bends. A resistor or source separates nodes. |
| Ground / reference node | The node you assign 0 V. It is a voltage reference, not a place where current disappears. |
| Branch | A circuit element and the connection between its two end nodes. |
| Essential node | A node where three or more element terminals meet. |
| Loop | A closed path through the circuit. |
| Mesh | A loop containing no other loops inside it in a planar drawing. Mesh analysis uses these smallest loops. |

> **Tip:** Nodal analysis works for planar and nonplanar circuits. Mesh analysis requires a planar circuit. Count connected wires, rather than counting black dots or bends.

**Example: Lecture 3 · Count nodes and meshes**

Count the nodes, essential nodes, branches, essential branches and meshes.

```schematic
V1 0,6 -> 0,3 "$v_1$"
V2 0,3 -> 0,0 "$v_2$"
R1 0,6 -> 4,6 "$R_1$"
R5 4,6 -> 4,3 "$R_5$"
R2 0,3 -> 2,3 "$R_2$"
R3 2,3 -> 4,3 "$R_3$"
R6 4,3 -> 4,0 "$R_6$"
R4 0,0 -> 4,0 "$R_4$"
wire 4,6 -> 9,6
wire 4,0 -> 9,0
R7 6.5,6 -> 6.5,0 "$R_7$"
I1 9,0 -> 9,6 "$I$"
label 0,6 "$a$" left
label 4,6 "$b$" above
label 0,3 "$c$" left
label 2,3 "$d$" above
label 4,3 "$e$" right
label 0,0 "$f$" left
label 4,0 "$g$" below
```

1. Nodes $a$–$g$; ten elements, so ten branches.

   $$n=7,\qquad b=10$$

2. Essential nodes meet three or more elements: $b$, $c$, $e$, $g$. ($a$, $d$, $f$ only join two.)

   $$n_e=4$$

3. Essential branches: $c$–$a$–$b$, $c$–$f$–$g$, $c$–$d$–$e$, $b$–$e$, $e$–$g$, and the two $b$–$g$ paths ($R_7$ and $I$).

   $$b_e=7$$

4. Meshes, checked both ways.

   $$M=10-7+1=7-4+1=4$$

**Answer:** $7$ nodes, $4$ essential nodes, $10$ branches, $7$ essential branches and $4$ meshes. For a connected planar circuit, $M=b-n+1=10-7+1=4$. The four essential nodes give three essential node voltages relative to a reference, before using source constraints.

*Source: ELEC 221 Week 3.pdf, PDF p. 7*

## Topic 2: Nodal analysis (node-voltage analysis)

*Source: ELEC 221 Week 3.pdf, PDF p. 11; ELEC 221 Week 3.pdf, PDF p. 12; ELEC 221 Week 3.pdf, PDF p. 14; ELEC 221 Week 3.pdf, PDF p. 17*

Choose the nodes and a ground node first. A long common wire is often a convenient ground; putting ground at one terminal of a voltage source can also save work. Name the other node voltages, such as $v_a$ and $v_b$, relative to that ground.

1. Pick and label the nodes and ground. Use voltage-source polarities to identify any node voltages already known.
2. Choose current reference directions. Down toward ground is convenient for a resistor connected to ground; between two other nodes, choose either direction and keep it consistent.
3. Write KCL at each unknown node. Replace each resistor current with its starting-node voltage minus its ending-node voltage, divided by its resistance.
4. Use substitution to solve the simultaneous equations. Find any remaining branch currents and powers, then interpret negative signs.

$$i_{a\to b}=\frac{v_a-v_b}{R},\qquad i_{a\to0}=\frac{v_a}{R},\qquad \sum i_{\mathrm{leaving}}=0$$

Here $i_{a\to b}$ is your chosen current reference from $a$ to $b$, and $R$ is the resistance between them. You do not need to know the higher voltage first. If $v_a-v_b$ is negative, the actual resistor current flows from $b$ to $a$. An ideal current source contributes its specified current to KCL; its current is not calculated with $V/R$.

> **Tip:** Use a signed sum of currents leaving = 0, or currents in = currents out. Either convention works. For a resistor from $a$ to $b$, the contribution is $(v_a-v_b)/R$ in node $a$'s outgoing equation and $(v_b-v_a)/R$ in node $b$'s outgoing equation.

**Example: Lecture 3 · One unknown node, a voltage source and a current source**

Use the node-voltage method to find $i_a$, $i_b$ and $i_c$.

```schematic
V1 0,3 -> 0,0 "$50\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\Omega$" i="$i_a$"
R2 3,3 -> 3,0 "$10\,\Omega$" i="$i_b$"
wire 3,3 -> 6,3
R3 6,3 -> 6,0 "$40\,\Omega$" i="$i_c$"
wire 6,3 -> 9,3
I1 9,0 -> 9,3 "$3\,\mathrm{A}$"
wire 9,0 -> 0,0
label 3,3 "$a$" above
ground 0,0
```

1. Ground the bottom wire; only $a$ is unknown. KCL at $a$, currents out; the $3\,\mathrm{A}$ comes in.

   $$\dfrac{v_a-50}{5}+\dfrac{v_a}{10}+\dfrac{v_a}{40}=3$$

2. Multiply by 40 and solve.

   $$8v_a-400+4v_a+v_a=120\;\Rightarrow\;v_a=40\,\mathrm{V}$$

3. Use each resistor's voltage difference divided by its resistance, in the arrow directions.

   $$i_a=\dfrac{50-40}{5}=2\,\mathrm{A},\quad i_b=4\,\mathrm{A},\quad i_c=1\,\mathrm{A}$$

4. Check KCL at $a$.

   $$2+3=4+1$$

**Answer:** $v_a=40\,\mathrm{V}$; $i_a=2\,\mathrm{A}$, $i_b=4\,\mathrm{A}$, $i_c=1\,\mathrm{A}$

*Source: ELEC 221 Week 3.pdf, PDF p. 13*

**Example: Lecture 3 · Two unknown nodes: solve by substitution**

Use the node-voltage method to find $v_1$ and $v_2$.

```schematic
V1 0,3 -> 0,0 "$10\,\mathrm{V}$"
R1 0,3 -> 3,3 "$1\,\Omega$"
R2 3,3 -> 3,0 "$5\,\Omega$" v="$v_1$"
R3 3,3 -> 6,3 "$2\,\Omega$"
R4 6,3 -> 6,0 "$10\,\Omega$" v="$v_2$"
wire 6,3 -> 9,3
I1 9,0 -> 9,3 "$2\,\mathrm{A}$"
wire 9,0 -> 0,0
label 3,3 "1" above
label 6,3 "2" above
ground 0,0
```

1. Ground the bottom wire. The voltage-source top node is 10 V; call the unknowns $v_1$ and $v_2$. Define each resistor current leaving the node where you write KCL.

2. Apply KCL at node 1. Every term is a voltage difference divided by resistance.

   $$\dfrac{v_1-10}{1}+\dfrac{v_1}{5}+\dfrac{v_1-v_2}{2}=0$$

3. Apply KCL at node 2; the current source supplies 2 A into this node.

   $$\dfrac{v_2-v_1}{2}+\dfrac{v_2}{10}=2$$

4. Clear the denominators and isolate $v_2$ in the second equation.

   $$17v_1-5v_2=100,\quad-5v_1+6v_2=20,\quad v_2=\dfrac{20+5v_1}{6}$$

5. Substitute into the first equation, then back-substitute.

   $$17v_1-\dfrac{5(20+5v_1)}6=100\Rightarrow77v_1=700\Rightarrow v_1=\dfrac{100}{11},\quad v_2=\dfrac{120}{11}\,\mathrm{V}$$

6. Calculate the shared resistor current in the chosen direction. The result points from node 2 to node 1.

   $$i_{1\to2}=\dfrac{v_1-v_2}{2}=-\dfrac{10}{11}\,\mathrm{A}$$

**Answer:** $v_1=\dfrac{100}{11}\approx9.09\,\mathrm{V}$, $v_2=\dfrac{120}{11}\approx10.91\,\mathrm{V}$

*Source: ELEC 221 Week 3.pdf, PDF p. 12*

### Voltage-source cases and supernodes

| Source position | What to write |
|---|---|
| Between ground and a node | Read the node voltage from the polarity. For + at the node and − at ground, $v_a=V_s$; reverse polarity gives $v_a=-V_s$. |
| Between two unknown nodes | Treat the pair as a supernode for KCL. Also write the source constraint, such as $v_a-v_b=V_s$ when + is at a. |
| Dependent voltage source | Keep the source constraint and express its control in your unknowns, e.g. $v_c=8i_\phi$ with $i_\phi=(v_a-v_b)/5$. |

For a supernode, add the currents crossing its outer boundary. The voltage source inside has an unknown current that cancels when the two node equations are combined. The nodes remain distinct: their voltages differ by the source voltage.

**Example: Lecture 3 · A grounded voltage source fixes a node**

Solve for $v_1$ and $v_2$.

```schematic
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$25\,\Omega$" v="$v_1$"
R2 3,3 -> 6,3 "$10\,\Omega$"
R3 6,3 -> 6,0 "$50\,\Omega$" v="$v_2$"
wire 6,3 -> 9,3
I1 9,0 -> 9,3 "$5\,\mathrm{A}$"
wire 9,0 -> 0,0
label 3,3 "1" above
label 6,3 "2" above
ground 0,0
```

1. Ground the bottom wire. The $100\,\mathrm{V}$ source sits between node 1 and ground.

   $$v_1=100\,\mathrm{V}$$

2. KCL at node 2 only (the $5\,\mathrm{A}$ comes in).

   $$\dfrac{v_2-100}{10}+\dfrac{v_2}{50}=5$$

3. Multiply by 50.

   $$5v_2-500+v_2=250\;\Rightarrow\;v_2=125\,\mathrm{V}$$

**Answer:** $v_1=100\,\mathrm{V}$, $v_2=125\,\mathrm{V}$

*Source: ELEC 221 Week 3.pdf, PDF p. 15*

**Example: Lecture 3 · A dependent voltage source controlled by resistor current**

Use the node-voltage method to find the power dissipated in the $5\,\Omega$ resistor.

```schematic
V1 0,3 -> 0,0 "$20\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
R2 3,3 -> 3,0 "$20\,\Omega$"
R3 3,3 -> 6,3 "$5\,\Omega$" i="$i_\Phi$"
R4 6,3 -> 6,0 "$10\,\Omega$"
R5 6,3 -> 9,3 "$2\,\Omega$"
E1 9,3 -> 9,0 "$8i_\Phi$"
wire 9,0 -> 0,0
label 3,3 "$a$" above
label 6,3 "$b$" above
label 9,3 "$c$" above
ground 0,0
```

1. Ground the bottom wire. Control first: the dependent source fixes $v_c$ in terms of $a$ and $b$.

   $$i_\Phi=\dfrac{v_a-v_b}{5},\qquad v_c=8i_\Phi=1.6(v_a-v_b)$$

2. KCL at $a$ and $b$.

   $$\begin{aligned}&\dfrac{v_a-20}{2}+\dfrac{v_a}{20}+\dfrac{v_a-v_b}{5}=0\\&\dfrac{v_b-v_a}{5}+\dfrac{v_b}{10}+\dfrac{v_b-v_c}{2}=0\end{aligned}$$

3. Substitute $v_c$ and collect.

   $$0.75v_a-0.2v_b=10,\qquad -v_a+1.6v_b=0$$

4. Solve.

   $$v_a=16\,\mathrm{V},\quad v_b=10\,\mathrm{V},\quad i_\Phi=1.2\,\mathrm{A}$$

5. Power in the $5\,\Omega$.

   $$p_{5\Omega}=(1.2)^2(5)=7.2\,\mathrm{W}$$

**Answer:** $v_a=16\,\mathrm{V}$, $v_b=10\,\mathrm{V}$, $i_\Phi=1.2\,\mathrm{A}$; $p_{5\Omega}=7.2\,\mathrm{W}$

*Source: ELEC 221 Week 3.pdf, PDF p. 14*

**Example: Lecture 3 · A dependent voltage source between two unknown nodes**

Use a supernode around $b$ and $c$ to find the node voltages.

```schematic
V1 0,3 -> 0,0 "$50\,\mathrm{V}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$40\,\Omega$"
R2 6,3 -> 3,3 "$5\,\Omega$" i="$i_\Phi$"
R3 6,3 -> 6,0 "$50\,\Omega$"
E1 9,3 -> 6,3 "$10i_\Phi$"
R4 9,3 -> 9,0 "$100\,\Omega$"
wire 9,3 -> 12,3
I1 12,0 -> 12,3 "$4\,\mathrm{A}$"
wire 12,0 -> 0,0
label 3,3 "$a$" above
label 6,3 "$b$" below
label 9,3 "$c$" below
ground 0,0
```

1. Ground the bottom wire. Read the grounded voltage source, and express the controlling current using its leftward reference.

   $$v_a=50\,\mathrm{V},\qquad i_\phi=\dfrac{v_b-50}{5}$$

2. Write the dependent voltage-source constraint. This expresses $v_c$ in terms of $v_b$.

   $$v_c-v_b=10i_\phi=2(v_b-50)\quad\Rightarrow\quad v_c=3v_b-100$$

3. Form a supernode containing $b$, $c$ and the voltage source between them. Write KCL using only the external branches.

   $$\dfrac{v_b-50}{5}+\dfrac{v_b}{50}+\dfrac{v_c}{100}=4$$

4. Substitute the constraint, clear the denominator and solve.

   $$20(v_b-50)+2v_b+(3v_b-100)=400\quad\Rightarrow\quad25v_b=1500$$

5. Back-substitute and check the source voltage.

   $$v_b=60\,\mathrm{V},\quad v_c=80\,\mathrm{V},\quad i_\phi=2\,\mathrm{A},\quad v_c-v_b=20=10i_\phi$$

**Answer:** $v_a=50\,\mathrm{V}$, $v_b=60\,\mathrm{V}$, $v_c=80\,\mathrm{V}$, $i_\Phi=2\,\mathrm{A}$

*Source: ELEC 221 Week 3.pdf, PDF p. 16; ELEC 221 Week 3.pdf, PDF p. 17*

> **Warning:** Do not use $I=V/R$ for an ideal voltage source. Its current must come from KCL or mesh currents. For a dependent source, write the control current or voltage with the original reference direction before substituting.

## Topic 3: Mesh analysis (mesh-current analysis)

*Source: ELEC 221 Week 3.pdf, PDF p. 18; ELEC 221 Week 3.pdf, PDF p. 19; ELEC 221 Week 3.pdf, PDF p. 21; ELEC 221 Week 3.pdf, PDF p. 22*

1. Identify the meshes and assign a current to each. Clockwise for all meshes usually makes shared-branch signs easier.
2. Mark which resistors belong to one mesh and which are shared. Translate the requested branch-current arrows into your mesh currents.
3. Write KVL around each independent mesh using $V=IR$ for resistors. Include any source constraints, then solve by substitution and convert back to branch currents.

| Branch | Expression to use |
|---|---|
| Resistor in mesh 1 only | $v_R=RI_1$ when traversed in the direction of $I_1$. |
| Resistor shared by clockwise meshes 1 and 2 | In the direction of mesh 1: $i_R=I_1-I_2$, so its KVL drop is $R(I_1-I_2)$. In mesh 2's direction use $R(I_2-I_1)$. |
| Voltage source in a KVL traversal | Using sum of drops = 0: traversing + to − contributes $+V_s$; − to + contributes $-V_s$. |
| Current source on one mesh's outer edge | That mesh current is known: $I_k=+I_s$ if the directions match and $I_k=-I_s$ if they oppose. |
| Current source shared by two meshes | Write KVL around the supermesh perimeter and a separate current-source constraint. |
| Dependent source | Express its controlling variable in mesh currents and keep its defining equation. |

Mesh currents are algebra variables assigned to loops. A branch current equals a mesh current only when that branch belongs to that mesh alone. If your two chosen mesh directions run the same way through a shared branch, add their contributions; determine this from the arrows instead of memorizing a difference.

**Example: Lecture 3 · Three meshes and shared resistors**

Use the mesh-current method to find **(a)** the power of each voltage source and **(b)** $v_o$.

```schematic
V1 0,3 -> 0,0 "$40\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
R2 3,3 -> 3,0 "$8\,\Omega$" v="$v_o$"
R3 3,3 -> 6,3 "$6\,\Omega$"
R4 6,3 -> 6,0 "$6\,\Omega$"
R5 6,3 -> 9,3 "$4\,\Omega$"
V2 9,3 -> 9,0 "$20\,\mathrm{V}$"
wire 9,0 -> 0,0
label 3,3 "$a$" above
label 6,3 "$b$" above
ground 0,0
```

1. Choose clockwise mesh currents $I_1$, $I_2$ and $I_3$ from left to right. The downward currents in the shared 8 Ω and 6 Ω resistors are $I_1-I_2$ and $I_2-I_3$.

2. Write KVL, counting resistor drops and source signs in each traversal.

   $$\begin{aligned}-40+2I_1+8(I_1-I_2)&=0\\8(I_2-I_1)+6I_2+6(I_2-I_3)&=0\\6(I_3-I_2)+4I_3+20&=0\end{aligned}$$

3. Use the first and third equations to express the outside mesh currents in terms of $I_2$.

   $$I_1=4+0.8I_2,\qquad I_3=-2+0.6I_2$$

4. Substitute both into the middle equation.

   $$-8(4+0.8I_2)+20I_2-6(-2+0.6I_2)=0\Rightarrow10I_2=20$$

5. Back-substitute. A negative mesh current means the actual mesh contribution opposes its chosen direction.

   $$I_1=5.6\,\mathrm{A},\ I_2=2\,\mathrm{A},\ I_3=-0.8\,\mathrm{A},\quad v_o=8(I_1-I_2)=28.8\,\mathrm{V}$$

6. For source power, use current entering the + terminal. Both results are negative absorbed power.

   $$p_{40\mathrm{V}}=-40I_1=-224\,\mathrm{W},\quad p_{20\mathrm{V}}=20I_3=-16\,\mathrm{W}$$

**Answer:** **(a)** The $40\,\mathrm{V}$ source delivers $224\,\mathrm{W}$; the $20\,\mathrm{V}$ source delivers $16\,\mathrm{W}$. **(b)** $v_o=28.8\,\mathrm{V}$

*Source: ELEC 221 Week 3.pdf, PDF p. 20*

### A current source between meshes: the supermesh

Combine the adjacent meshes for one KVL path around their outer perimeter, skipping the internal current-source branch. Keep the original mesh currents; the supermesh does not get an extra unknown current. Add a constraint whose signs come from the source arrow. For example, if the arrow follows $I_2$ and opposes $I_1$ through their shared branch, write $I_2-I_1=I_s$.

**Example: Assessment AP4.12 · Supermesh plus a current constraint**

Use the mesh-current method to find the power dissipated in the $1\,\Omega$ resistor. Mesh $a$ is lower-left, $b$ the top, $c$ lower-right (all clockwise).

```schematic
V1 0,3 -> 0,0 "$10\,\mathrm{V}$"
I1 0,3 -> 3,3 "$2\,\mathrm{A}$"
wire 0,3 -> 0,6
R1 0,6 -> 6,6 "$2\,\Omega$"
wire 6,6 -> 6,3
R2 3,3 -> 6,3 "$2\,\Omega$"
R3 3,3 -> 3,0 "$2\,\Omega$"
V2 6,0 -> 6,3 "$6\,\mathrm{V}$"
R4 6,0 -> 3,0 "$1\,\Omega$"
wire 3,0 -> 0,0
label 3,3 "$m$" above
label 6,3 "$r$" right
label 6,0 "$q$" right
ground 0,0
```

1. The $2\,\mathrm{A}$ source is shared by meshes $a$ and $b$.

   $$I_a-I_b=2$$

2. KVL around the supermesh (skip the source branch).

   $$-10+2I_b+2(I_b-I_c)+2(I_a-I_c)=0$$

3. KVL around mesh $c$.

   $$-6+I_c+2(I_c-I_a)+2(I_c-I_b)=0$$

4. Solve the three equations.

   $$I_a=7\,\mathrm{A},\quad I_b=5\,\mathrm{A},\quad I_c=6\,\mathrm{A}$$

5. The $1\,\Omega$ is only in mesh $c$.

   $$p_{1\Omega}=I_c^2(1)=36\,\mathrm{W}$$

**Answer:** $I_a=7\,\mathrm{A}$, $I_b=5\,\mathrm{A}$, $I_c=6\,\mathrm{A}$; $p_{1\Omega}=36\,\mathrm{W}$

*Source: Chapter 4 Problems.pdf, PDF p. 9*

**Example: Lecture 3 · A dependent source controlled by a shared-branch current**

Use the mesh-current method to find the power dissipated in the $4\,\Omega$ resistor. Mesh $a$ is lower-left, $b$ the top triangle, $c$ lower-right (all clockwise).

```schematic
V1 0,3 -> 0,0 "$50\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\Omega$"
R2 3,3 -> 6,3 "$4\,\Omega$"
R3 3,3 -> 3,0 "$20\,\Omega$" i="$i_\phi$"
E1 6,3 -> 6,0 "$15i_\phi$"
wire 0,3 -> 0,5
R4 0,5 -> 6,5 "$1\,\Omega$"
wire 6,5 -> 6,3
wire 6,0 -> 0,0
label 3,3 "$a$" above
label 6,3 "$b$" right
ground 0,0
```

1. Control first: both lower meshes cross the $20\,\Omega$.

   $$i_\phi=I_a-I_c$$

2. KVL equations.

   $$\begin{aligned}&-50+5(I_a-I_b)+20(I_a-I_c)=0\\&I_b+4(I_b-I_c)+5(I_b-I_a)=0\\&15i_\phi+20(I_c-I_a)+4(I_c-I_b)=0\end{aligned}$$

3. Substitute the control and collect.

   $$\begin{aligned}25I_a-5I_b-20I_c&=50\\-5I_a+10I_b-4I_c&=0\\-5I_a-4I_b+9I_c&=0\end{aligned}$$

4. Solve.

   $$I_a=29.6\,\mathrm{A},\quad I_b=26\,\mathrm{A},\quad I_c=28\,\mathrm{A},\quad i_\phi=1.6\,\mathrm{A}$$

5. The $4\,\Omega$ carries $I_c-I_b$.

   $$p_{4\Omega}=4(28-26)^2=16\,\mathrm{W}$$

**Answer:** $i_\phi=1.6\,\mathrm{A}$; $p_{4\Omega}=16\,\mathrm{W}$

*Source: ELEC 221 Week 3.pdf, PDF p. 21*

> **Warning:** Common setup checks: every independent unknown needs an equation; every dependent source needs its control relation; a supernode needs a voltage constraint; a supermesh needs a current constraint. For units, V/kΩ gives mA and V/Ω gives A.

## Practice problems

These 25 problems use the textbook, uploaded tutorial, assessment problems and lecture figures. Try the setup before opening a solution: label nodes or mesh currents, write shared-branch references, and write the equations. Work the algebra by substitution. Each title names the scenario so you can choose a different challenge rather than repeat a similar circuit.

| Practice route | Different situations to cover |
|---|---|
| Nodal | Power and source-current signs; symbolic source averaging; three unknown nodes; non-ground voltage references; dependent sources and floating sources. |
| Mesh | Topology counts; perimeter current source; reversed voltage polarity; three meshes; dependent source controls; supermesh constraints. |
| Mixed and tutorial | Change the ground node; bridge network; resistor design; nonzero return-node voltage; source power checks. |

**Problem: Textbook P4.8–4.9 · Nodal voltage and complete power balance** (introductory)

**(a)** Use the node-voltage method to find $v_o$. **(b)** Find the power developed by the $5\,\mathrm{A}$ source and by the $180\,\mathrm{V}$ source, and check the balance.

```schematic
V1 0,2 -> 0,0 "$180\,\mathrm{V}$"
R1 0,4 -> 0,2 "$12\,\Omega$"
R2 0,4 -> 3,4 "$5\,\Omega$"
R3 3,4 -> 3,0 "$2\,\Omega$" v="$v_o$"
wire 3,4 -> 6,4
I1 6,4 -> 6,0 "$5\,\mathrm{A}$"
wire 0,0 -> 6,0
label 0,4 "$t$" left
ground 0,0
```

<details><summary>Solution</summary>

1. Ground the bottom wire. The two series resistors in the source branch have no branch between them, so they carry the same current.

   $$R_s=12+5=17\,\Omega$$

2. Write KCL at the output node using current from the source branch into the node.

   $$\dfrac{180-v_o}{17}=\dfrac{v_o}{2}+5$$

3. Clear the denominator and solve.

   $$360-2v_o=17v_o+170\Rightarrow v_o=10\,\mathrm{V},\quad i_s=\dfrac{180-10}{17}=10\,\mathrm{A}$$

4. The voltage source delivers; the 5 A source absorbs because its current enters the positive-voltage terminal.

   $$P_{180,\mathrm{del}}=180(10)=1800\,\mathrm{W},\quad P_{5\mathrm{A},\mathrm{del}}=-10(5)=-50\,\mathrm{W}$$

5. Check the resistor powers against net power delivered.

   $$10^2(12+5)+\dfrac{10^2}{2}=1750\,\mathrm{W}=1800-50$$

**Answer:** **(a)** $v_o=10\,\mathrm{V}$. **(b)** $180\,\mathrm{V}$: $1800\,\mathrm{W}$; $5\,\mathrm{A}$: $-50\,\mathrm{W}$ (it absorbs $50\,\mathrm{W}$). Total $1750\,\mathrm{W}$ developed = dissipated.

</details>

*Source: TextBook-221.pdf, PDF p. 162; TextBook-221.pdf, PDF p. 163*

**Problem: Textbook P4.13 · Oppositely directed current sources** (introductory)

Use the node-voltage method to find $v_1$ and $v_2$.

```schematic
I1 0,3 -> 0,0 "$2.4\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$125\,\Omega$" v="$v_1$"
R2 3,3 -> 6,3 "$25\,\Omega$"
R3 6,3 -> 6,0 "$250\,\Omega$"
wire 6,3 -> 9,3
R4 9,3 -> 9,0 "$375\,\Omega$" v="$v_2$"
wire 9,3 -> 12,3
I2 12,0 -> 12,3 "$3.2\,\mathrm{A}$"
wire 12,0 -> 0,0
label 3,3 "1" above
label 6,3 "2" above
ground 0,0
```

<details><summary>Solution</summary>

1. Ground the bottom wire. KCL at node 1 (out = in; the $2.4\,\mathrm{A}$ leaves).

   $$\dfrac{v_1}{125}+\dfrac{v_1-v_2}{25}=-2.4$$

2. KCL at node 2 (the $3.2\,\mathrm{A}$ comes in).

   $$\dfrac{v_2}{250}+\dfrac{v_2}{375}+\dfrac{v_2-v_1}{25}=3.2$$

3. Clear fractions (×125 and ×750).

   $$6v_1-5v_2=-300,\qquad -30v_1+35v_2=2400$$

4. Add 5× the first to the second.

   $$10v_2=900\;\Rightarrow\;v_2=90\,\mathrm{V},\quad v_1=25\,\mathrm{V}$$

**Answer:** $v_1=25\,\mathrm{V}$, $v_2=90\,\mathrm{V}$

</details>

*Source: TextBook-221.pdf, PDF p. 163*

**Problem: Textbook P4.16 · Derive a symbolic voltage average** (introductory)

**(a)** Show that $v_o$ is the average of the source voltages. **(b)** Find $v_o$ if $v_1=150\,\mathrm{V}$, $v_2=200\,\mathrm{V}$ and $v_3=-50\,\mathrm{V}$.

```schematic
V1 0,2 -> 0,0 "$v_1$"
R1 0,4 -> 0,2 "$R$"
V2 3,2 -> 3,0 "$v_2$"
R2 3,4 -> 3,2 "$R$"
V3 6,2 -> 6,0 "$v_3$"
R3 6,4 -> 6,2 "$R$"
wire 0,4 -> 8,4
wire 0,0 -> 8,0
terminal 8,4 "$+$" right
terminal 8,0 "$-$" right
label 8,2 "$v_o$" right
ground 0,0
```

<details><summary>Solution</summary>

1. Ground the bottom common node. Each source fixes the node at the bottom of its equal resistor R; the shared output node has no external load.

2. Sum currents leaving the output node. There is one term for each source branch.

   $$\dfrac{v_o-v_1}{R}+\dfrac{v_o-v_2}{R}+\cdots+\dfrac{v_o-v_n}{R}=0$$

3. Multiply by R and isolate the output. Equal resistances give equal weights.

   $$nv_o-(v_1+v_2+\cdots+v_n)=0\Rightarrow v_o=\dfrac{v_1+v_2+\cdots+v_n}{n}$$

4. Substitute the three given source voltages, keeping the negative source value.

   $$v_o=\dfrac{150+200-50}{3}=100\,\mathrm{V}$$

**Answer:** $v_o$ is the average; with these values $v_o=100\,\mathrm{V}$.

</details>

*Source: TextBook-221.pdf, PDF p. 163*

**Problem: Textbook P4.11 · Three unknown nodes and six branch currents** (intermediate)

**(a)** Use the node-voltage method to find the branch currents $i_a$ to $i_f$. **(b)** Find the total power developed.

```schematic
V1 0,3 -> 0,0 "$80\,\mathrm{V}$"
R1 0,3 -> 3,3 "$800\,\Omega$" i="$i_b$"
R2 3,3 -> 6,3 "$500\,\Omega$" i="$i_c$"
R3 6,3 -> 9,3 "$2\,\mathrm{k\Omega}$" i="$i_d$"
wire 3,3 -> 3,5
R4 3,5 -> 9,5 "$1\,\mathrm{k\Omega}$" i="$i_a$"
wire 9,5 -> 9,3
R5 6,3 -> 6,0 "$3\,\mathrm{k\Omega}$" i="$i_e$"
R6 9,3 -> 9,0 "$250\,\Omega$" i="$i_f$"
wire 0,0 -> 9,0
label 3,3 "$p$" below
label 6,3 "$q$" above
label 9,3 "$r$" right
ground 0,0
```

<details><summary>Solution</summary>

1. Ground the bottom wire. Name the unknowns $p$, $q$ and $r$ as shown; use kΩ and mA. Write KCL at all three.

   $$\begin{aligned}\dfrac{80-p}{0.8}&=\dfrac{p-q}{0.5}+(p-r)\\\dfrac{p-q}{0.5}&=\frac q3+\dfrac{q-r}{2}\\(p-r)+\dfrac{q-r}{2}&=\frac r{0.25}\end{aligned}$$

2. Collect terms and use the third equation to express $r$.

   $$4.25p-2q-r=100,\quad12p-17q+3r=0,\quad r=\dfrac{2p+q}{11}$$

3. Substitute for $r$ in the second equation, then express $q$ and $r$ in terms of $p$.

   $$132p-187q+6p+3q=0\Rightarrow q=\frac34p,\quad r=\frac14p$$

4. Substitute into the first equation.

   $$4.25p-2(0.75p)-0.25p=100\Rightarrow p=40,\ q=30,\ r=10\,\mathrm{V}$$

5. Use each indicated branch arrow to calculate its current.

   $$i_a=30,\quad i_b=50,\quad i_c=20,\quad i_d=10,\quad i_e=10,\quad i_f=40\,\mathrm{mA}$$

6. The source supplies $i_b$; check total resistor power.

   $$P_{\mathrm{del}}=80(0.05)=4\,\mathrm{W}=2+0.2+0.2+0.9+0.3+0.4$$

**Answer:** $i_a=30$, $i_b=50$, $i_c=20$, $i_d=10$, $i_e=10$, $i_f=40\,\mathrm{mA}$; $4\,\mathrm{W}$ developed.

</details>

*Source: TextBook-221.pdf, PDF p. 163*

**Problem: Textbook P4.25 · Output voltage between two non-ground nodes** (intermediate)

Use the node-voltage method to find $v_o$.

```schematic
V1 0,3 -> 0,0 "$50\,\mathrm{V}$"
R1 0,3 -> 3,3 "$80\,\Omega$"
R2 3,3 -> 3,0 "$50\,\Omega$"
R3 3,3 -> 6,3 "$40\,\Omega$"
I1 6,0 -> 6,3 "$750\,\mathrm{mA}$"
wire 6,3 -> 9,3
R4 9,3 -> 9,0 "$200\,\Omega$"
wire 0,3 -> 0,5
R5 6,5 -> 0,5 "$800\,\Omega$" v="$v_o$"
wire 6,5 -> 6,3
wire 0,0 -> 9,0
label 3,3 "$m$" below
label 6,3 "$r$" below
ground 0,0
```

<details><summary>Solution</summary>

1. Ground the bottom wire. The voltage-source top is 50 V. Call the other unknowns $m$ and $r$; the requested voltage is positive on the right end of 800 Ω.

   $$v_o=r-50$$

2. Write KCL at both unknown nodes.

   $$\begin{aligned}\dfrac{m-50}{80}+\frac m{50}+\dfrac{m-r}{40}&=0\\\dfrac{r-m}{40}+\frac r{200}+\dfrac{r-50}{800}&=0.75\end{aligned}$$

3. Clear fractions and express $r$ from the second equation.

   $$23m-10r=250,\quad-20m+25r=650\Rightarrow r=26+0.8m$$

4. Substitute into the first equation, then find the output difference.

   $$23m-10(26+0.8m)=250\Rightarrow m=34,\ r=53.2\,\mathrm{V},\quad v_o=3.2\,\mathrm{V}$$

**Answer:** $v_o=3.2\,\mathrm{V}$

</details>

*Source: TextBook-221.pdf, PDF p. 165*

**Problem: Textbook P4.27 · A floating dependent voltage source** (advanced)

Use the node-voltage method to find $v$.

```schematic
I1 0,0 -> 0,3 "$4.8\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$7.5\,\Omega$" i="$i_x$"
R2 3,3 -> 6,3 "$2.5\,\Omega$"
R3 6,3 -> 6,0 "$10\,\Omega$" v="$v$"
E1 9,3 -> 6,3 "$i_x$"
R4 9,3 -> 9,0 "$2.5\,\Omega$"
R5 9,3 -> 12,3 "$1\,\Omega$"
V1 12,3 -> 12,0 "$12\,\mathrm{V}$"
wire 12,0 -> 0,0
label 3,3 "$a$" above
label 6,3 "$b$" above
label 9,3 "$c$" above
ground 0,0
```

<details><summary>Solution</summary>

1. Ground the bottom wire. $b$ and $c$ form a supernode (the dependent source joins them). Control: $i_x$ runs down the $7.5\,\Omega$.

   $$i_x=\dfrac{v_a}{7.5},\qquad v_c-v=(1\,\Omega)\,i_x$$

2. KCL at $a$ (the $4.8\,\mathrm{A}$ comes in).

   $$\dfrac{v_a}{7.5}+\dfrac{v_a-v}{2.5}=4.8\;\Rightarrow\;v_a=9+0.75v$$

3. So the voltage-source constraint is

   $$v_c=v+\dfrac{v_a}{7.5}=1.1v+1.2$$

4. KCL around the voltage-source constraint.

   $$\dfrac{v-v_a}{2.5}+\dfrac{v}{10}+\dfrac{v_c}{2.5}+\dfrac{v_c-12}{1}=0$$

5. Substitute and solve.

   $$1.74v-13.92=0\;\Rightarrow\;v=8\,\mathrm{V},\quad v_a=15\,\mathrm{V},\quad v_c=10\,\mathrm{V}$$

**Answer:** $v=8\,\mathrm{V}$ (with $v_a=15\,\mathrm{V}$, $v_c=10\,\mathrm{V}$, $i_x=2\,\mathrm{A}$)

</details>

*Source: TextBook-221.pdf, PDF p. 165*

**Problem: Assessment AP4.6 · A source controlled by a reversed current** (advanced)

Use the node-voltage method to find $v_1$ and $i_\phi$.

```schematic
V1 0,3 -> 0,0 "$60\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
R2 3,3 -> 3,0 "$24\,\Omega$"
R3 6,3 -> 3,3 "$3\,\Omega$" i="$i_\phi$"
R4 6,3 -> 6,0 "$3\,\Omega$"
wire 0,3 -> 0,5
E1 6,5 -> 0,5 "$6i_\phi$"
wire 6,5 -> 6,3
wire 6,0 -> 0,0
label 3,3 "$v_1$" above
ground 0,0
```

<details><summary>Solution</summary>

1. Ground the bottom wire. The right node is the $60\,\mathrm{V}$ node plus the dependent source's voltage.

   $$v_r=60+6i_\phi$$

2. KCL at $v_1$.

   $$\dfrac{v_1-60}{2}+\dfrac{v_1}{24}+\dfrac{v_1-(60+6i_\phi)}{3}=0$$

3. Control: $i_\phi$ flows from the right node to $v_1$.

   $$i_\phi=\dfrac{60+6i_\phi-v_1}{3}\;\Rightarrow\;v_1=60+3i_\phi$$

4. Substitute and solve.

   $$i_\phi=-4\,\mathrm{A},\qquad v_1=48\,\mathrm{V}$$

**Answer:** $v_1=48\,\mathrm{V}$, $i_\phi=-4\,\mathrm{A}$

</details>

*Source: Chapter 4 Problems.pdf, PDF p. 5*

**Problem: Textbook P4.1 · Count nodes, branches and meshes** (introductory)

Find the number of **(a)** branches, **(b)** branches with unknown current, **(c)** essential branches, **(d)** essential branches with unknown current, **(e)** nodes, **(f)** essential nodes, **(g)** meshes.

```schematic
V1 0,4 -> 0,0 "$18\,\mathrm{V}$"
wire 0,4 -> 0,7
R1 0,7 -> 10,7 "$R_1$"
wire 10,7 -> 10,4
R2 0,6 -> 3,6 "$R_2$" i_rev="$i_\Delta$"
R3 0,4 -> 3,4 "$R_3$"
wire 3,6 -> 3,4
G1 3,6 -> 10,6 "$2v_\Delta$"
R6 3,4 -> 3,0 "$R_6$" v="$v_\Delta$"
R4 3,4 -> 6,4 "$R_4$"
R5 6,4 -> 10,4 "$R_5$"
E1 6,4 -> 6,0 "$25i_\Delta$"
R7 10,4 -> 10,0 "$R_7$"
wire 10,4 -> 13,4
I1 13,0 -> 13,4 "$5\,\mathrm{mA}$"
wire 13,0 -> 0,0
label 0,4 "$a$" left
label 3,6 "$b$" above
label 6,4 "$c$" above
label 10,7 "$d$" right
label 13,0 "$e$" right
```

<details><summary>Solution</summary>

1. Branches: seven resistors and four sources.

   $$b=11$$

2. Only the $5\,\mathrm{mA}$ source has a known current; the dependent source $2v_\Delta$ depends on an unknown, so it does not count as known.

   $$b_{\text{unknown}}=10$$

3. Nodes: $a$ (top-left wire), $b$, $c$, $d$ and the bottom wire $e$. Each joins at least three elements.

   $$n=n_e=5$$

4. Every branch runs between essential nodes, so every branch is essential.

   $$b_e=11,\quad b_{e,\text{unknown}}=10$$

5. Meshes.

   $$M=b-n+1=11-5+1=7$$

**Answer:** **(a)** $11$ **(b)** $10$ **(c)** $11$ **(d)** $10$ **(e)** $5$ **(f)** $5$ **(g)** $7$

</details>

*Source: TextBook-221.pdf, PDF p. 162*

**Problem: Assessment AP4.10 · Perimeter source fixes a negative mesh current** (intermediate)

Use the mesh-current method to find the power dissipated in the $2\,\Omega$ resistor.

```schematic
V1 0,3 -> 0,0 "$30\,\mathrm{V}$"
R1 0,3 -> 3,3 "$3\,\Omega$"
R2 0,0 -> 3,0 "$6\,\Omega$"
R3 3,3 -> 3,0 "$2\,\Omega$"
R4 3,3 -> 6,3 "$8\,\Omega$"
R5 3,0 -> 6,0 "$4\,\Omega$"
R6 6,3 -> 6,0 "$5\,\Omega$"
wire 6,3 -> 9,3
I1 9,0 -> 9,3 "$16\,\mathrm{A}$"
wire 9,0 -> 6,0
ground 0,0
```

<details><summary>Solution</summary>

1. The perimeter source fixes mesh 3: clockwise $I_3$ opposes its upward arrow.

   $$I_3=-16\,\mathrm{A}$$

2. KVL in mesh 1.

   $$-30+3I_1+2(I_1-I_2)+6I_1=0\;\Rightarrow\;11I_1-2I_2=30$$

3. KVL in mesh 2.

   $$8I_2+5(I_2-I_3)+4I_2+2(I_2-I_1)=0\;\Rightarrow\;-2I_1+19I_2=-80$$

4. Solve.

   $$I_1=2\,\mathrm{A},\qquad I_2=-4\,\mathrm{A}$$

5. The $2\,\Omega$ carries $I_1-I_2$ downward.

   $$p_{2\Omega}=(6)^2(2)=72\,\mathrm{W}$$

**Answer:** $p_{2\Omega}=72\,\mathrm{W}$

</details>

*Source: Chapter 4 Problems.pdf, PDF p. 7; Chapter 4 Problems.pdf, PDF p. 8*

**Problem: Textbook P4.37 · Repeat the analysis after reversing a source** (intermediate)

**(a)** Use the mesh-current method to find $i_a$, $i_b$ and $i_c$. **(b)** Repeat with the polarity of the $64\,\mathrm{V}$ source reversed.

```schematic
V1 0,3 -> 0,0 "$40\,\mathrm{V}$"
R1 0,3 -> 3,3 "$3\,\Omega$" i="$i_a$"
R2 0,0 -> 3,0 "$2\,\Omega$"
R3 3,3 -> 3,0 "$45\,\Omega$" i="$i_b$"
R4 6,3 -> 3,3 "$4\,\Omega$" i="$i_c$"
R5 3,0 -> 6,0 "$1.5\,\Omega$"
V2 6,0 -> 6,3 "$64\,\mathrm{V}$"
ground 0,0
```

<details><summary>Solution</summary>

1. Clockwise mesh currents $I_L$, $I_R$. From the arrows: $i_a=I_L$, $i_b=I_L-I_R$, $i_c=-I_R$ (it points left).

2. Left mesh.

   $$-40+(3+2)I_L+45(I_L-I_R)=0\;\Rightarrow\;50I_L-45I_R=40$$

3. **(a)** Right mesh: clockwise through the $64\,\mathrm{V}$ source is a voltage rise.

   $$45(I_R-I_L)+5.5I_R-64=0\;\Rightarrow\;-45I_L+50.5I_R=64$$

4. Solve.

   $$I_R=10\,\mathrm{A},\quad I_L=9.8\,\mathrm{A}$$

5. **(b)** Only the source sign flips.

   $$-45I_L+50.5I_R=-64\;\Rightarrow\;I_R=-2.8\,\mathrm{A},\quad I_L=-1.72\,\mathrm{A}$$

**Answer:** **(a)** $i_a=9.8\,\mathrm{A}$, $i_b=-0.2\,\mathrm{A}$, $i_c=-10\,\mathrm{A}$. **(b)** $i_a=-1.72\,\mathrm{A}$, $i_b=1.08\,\mathrm{A}$, $i_c=2.8\,\mathrm{A}$.

</details>

*Source: TextBook-221.pdf, PDF p. 166*

**Problem: Textbook P4.36 · Three meshes and a power check** (intermediate)

**(a)** Use the mesh-current method to find the total power developed. **(b)** Check that it equals the total power dissipated.

```schematic
V1 0,3 -> 0,0 "$110\,\mathrm{V}$"
R1 0,3 -> 4,3 "$10\,\Omega$"
R2 4,3 -> 8,3 "$12\,\Omega$"
V2 8,3 -> 8,0 "$70\,\mathrm{V}$"
wire 0,3 -> 0,5
R3 0,5 -> 8,5 "$6\,\Omega$"
wire 8,5 -> 8,3
R4 4,3 -> 4,1.8 "$3\,\Omega$"
V3 4,0 -> 4,1.8 "$12\,\mathrm{V}$"
R5 0,0 -> 4,0 "$4\,\Omega$"
R6 4,0 -> 8,0 "$2\,\Omega$"
label 0,3 "$a$" left
label 4,3 "$m$" above
label 8,3 "$b$" right
label 0,0 "$l$" left
label 8,0 "$r$" right
ground 4,0
```

<details><summary>Solution</summary>

1. KVL equations (clockwise; $-\to+$ through a voltage source is a voltage rise).

   $$\begin{aligned}17i_1-3i_2-10i_3&=122\\-3i_1+17i_2-12i_3&=-82\\-10i_1-12i_2+28i_3&=0\end{aligned}$$

2. Solve.

   $$i_1=8\,\mathrm{A},\quad i_2=-2\,\mathrm{A},\quad i_3=2\,\mathrm{A}$$

3. Developed power.

   $$110(8)+70(2)+12(10)=880+140+120=1140\,\mathrm{W}$$

4. Dissipated.

   $$360+192+24+300+256+8=1140\,\mathrm{W}$$

**Answer:** $1140\,\mathrm{W}$ developed $=1140\,\mathrm{W}$ dissipated.

</details>

*Source: TextBook-221.pdf, PDF p. 166*

**Problem: Textbook P4.42 · A shared voltage controls a source** (intermediate)

Use the mesh-current method to find the power dissipated in the $10\,\Omega$ resistor.

```schematic
V1 0,3 -> 0,0 "$60\,\mathrm{V}$"
R1 0,3 -> 4,3 "$4\,\Omega$"
R2 4,3 -> 4,0 "$10\,\Omega$" v="$v_\Delta$"
R3 4,3 -> 8,3 "$2.5\,\Omega$"
E1 8,0 -> 8,3 "$\tfrac{v_\Delta}{2}$"
R4 0,0 -> 4,0 "$2\,\Omega$"
R5 4,0 -> 8,0 "$20\,\Omega$"
label 4,3 "$m$" above
label 0,0 "$l$" left
label 8,0 "$r$" right
ground 4,0
```

<details><summary>Solution</summary>

1. Choose clockwise mesh currents $i_1$ on the left and $i_2$ on the right. The downward current through the shared 10 Ω resistor is $i_1-i_2$.

2. Control.

   $$v_\Delta=10(i_1-i_2)$$

3. KVL equations.

   $$\begin{aligned}60&=4i_1+10(i_1-i_2)+2i_1\\0&=2.5i_2-\tfrac{v_\Delta}{2}+20i_2+10(i_2-i_1)\end{aligned}$$

4. Substitute the control voltage into the mesh equations; isolate $i_1$ and substitute.

   $$16i_1-10i_2=60,\quad-15i_1+37.5i_2=0\Rightarrow i_1=2.5i_2\Rightarrow i_2=2\,\mathrm{A}$$

5. Solve.

   $$i_1=5\,\mathrm{A},\quad i_2=2\,\mathrm{A},\quad v_\Delta=30\,\mathrm{V},\qquad p_{10\Omega}=\dfrac{30^2}{10}=90\,\mathrm{W}$$

**Answer:** $p_{10\,\Omega}=90\,\mathrm{W}$

</details>

*Source: TextBook-221.pdf, PDF p. 166*

**Problem: Textbook P4.30 · Change the reference node** (intermediate)

**(a)** Use the node-voltage method with node $a$ as the reference to find $v_o$ and the power delivered by the $0.5\,\mathrm{A}$ source. **(b)** Repeat with node $b$ as the reference. **(c)** Which reference is better, and why?

```schematic
I1 0,0 -> 0,3 "$0.5\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$40\,\Omega$"
V1 6,3 -> 3,3 "$12\,\mathrm{V}$"
R2 6,3 -> 6,0 "$100\,\Omega$" v="$v_o$"
R3 6,3 -> 9,3 "$150\,\Omega$"
R4 9,3 -> 9,0 "$50\,\Omega$"
wire 9,0 -> 0,0
label 3,3 "b" above
label 3,0 "a" below
```

<details><summary>Solution</summary>

1. **(a)** Reference $a$: $b$ and $c$ form a supernode with $v_c=v_b+12$. KCL around it (the $0.5\,\mathrm{A}$ comes in).

   $$\dfrac{v_b}{40}+\dfrac{v_b+12}{100}+\dfrac{v_b+12}{200}=0.5$$

2. Multiply by 200 and solve.

   $$8v_b+36=100\;\Rightarrow\;v_b=8\,\mathrm{V},\quad v_o=v_c=20\,\mathrm{V}$$

3. The source carries $0.5\,\mathrm{A}$ from a to b. Use the voltage difference between those nodes to calculate delivered power.

   $$p=(8)(0.5)=4\,\mathrm{W}\text{ delivered}$$

4. **(b)** Reference $b$: the source fixes $v_c=12\,\mathrm{V}$. One KCL, at $a$ (the $0.5\,\mathrm{A}$ leaves $a$).

   $$\dfrac{v_a}{40}+\dfrac{v_a-12}{100}+\dfrac{v_a-12}{200}+0.5=0\;\Rightarrow\;v_a=-8\,\mathrm{V}$$

5. Same answers.

   $$v_o=v_c-v_a=20\,\mathrm{V},\qquad p=(0-(-8))(0.5)=4\,\mathrm{W}$$

6. **(c)** Reference $b$ is better: the voltage source then fixes a node directly, so one plain KCL replaces the supernode.

**Answer:** **(a)** $v_o=20\,\mathrm{V}$; the source delivers $4\,\mathrm{W}$. **(b)** Same: $v_o=20\,\mathrm{V}$, $4\,\mathrm{W}$ (with $v_a=-8\,\mathrm{V}$). **(c)** $b$: the $12\,\mathrm{V}$ source then fixes $v_c$, leaving one equation.

</details>

*Source: TextBook-221.pdf, PDF p. 165*

**Problem: Textbook P4.24 · Negative node voltages and source current** (intermediate)

**(a)** Use the node-voltage method to find $i_1$, $i_2$ and $i_3$. **(b)** Check by showing the power dissipated equals the power developed.

```schematic
V1 0,3 -> 0,0 "$20\,\mathrm{V}$"
R1 0,3 -> 3,3 "$25\,\mathrm{k\Omega}$" i="$i_1$"
R2 3,3 -> 3,0 "$250\,\Omega$" i="$i_2$"
I1 3,3 -> 6,3 "$11\,\mathrm{mA}$"
R3 6,3 -> 6,0 "$1\,\mathrm{k\Omega}$"
wire 6,3 -> 9,3
V2 9,0 -> 9,3 "$10\,\mathrm{V}$" i_rev="$i_3$"
wire 3,3 -> 3,5
R4 3,5 -> 9,5 "$500\,\Omega$"
wire 9,5 -> 9,3
wire 9,0 -> 0,0
label 3,5 "$a$" left
label 6,3 "$b$" above
ground 0,0
```

<details><summary>Solution</summary>

1. Ground the bottom wire. The $10\,\mathrm{V}$ source has its $+$ at ground, so $v_b=-10\,\mathrm{V}$. KCL at $a$ (currents out, in mA and kΩ).

   $$\dfrac{v_a-20}{25}+\dfrac{v_a}{0.25}+11+\dfrac{v_a+10}{0.5}=0$$

2. Multiply by 25.

   $$v_a-20+100v_a+275+50v_a+500=0\;\Rightarrow\;v_a=-5\,\mathrm{V}$$

3. Branch currents in their arrow directions.

   $$i_1=\dfrac{20-(-5)}{25}=1\,\mathrm{mA},\qquad i_2=\dfrac{-5}{0.25}=-20\,\mathrm{mA}$$

4. KCL at $b$: in from the source ($11$), the $500\,\Omega$ ($10$) and the $1\,\mathrm{k\Omega}$ ($10$); out down through the $10\,\mathrm{V}$ source.

   $$i_3=11+\dfrac{-5+10}{0.5}+\dfrac{0+10}{1}=31\,\mathrm{mA}$$

5. **(b)** Developed: both voltage sources. Dissipated: the resistors plus the $11\,\mathrm{mA}$ source (which absorbs).

   $$20(1)+10(31)=330\,\mathrm{mW}=25+100+50+100+55$$

**Answer:** **(a)** $i_1=1\,\mathrm{mA}$, $i_2=-20\,\mathrm{mA}$, $i_3=31\,\mathrm{mA}$. **(b)** $330\,\mathrm{mW}$ developed $=330\,\mathrm{mW}$ absorbed.

</details>

*Source: TextBook-221.pdf, PDF p. 164*

**Problem: Textbook P4.18 · A dependent source supplies power** (intermediate)

Use the node-voltage method to find the power delivered by the dependent voltage source.

```schematic
V1 0,3 -> 0,0 "$80\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\Omega$"
R2 3,3 -> 3,0 "$50\,\Omega$" i="$i_\sigma$"
R3 3,3 -> 6,3 "$10\,\Omega$"
E1 6,0 -> 6,3 "$75i_\sigma$"
R4 3,0 -> 6,0 "$15\,\Omega$"
wire 3,0 -> 0,0
label 3,3 "$a$" above
label 6,3 "$c$" right
label 6,0 "$d$" right
ground 0,0
```

<details><summary>Solution</summary>

1. Ground the bottom-left wire. Name $a$, the dependent source's $-$ end $c$ and $+$ end $d$. Write the control and voltage-source constraint.

   $$i_\sigma=\dfrac{v_a}{50},\qquad v_d-v_c=75i_\sigma=1.5v_a$$

2. KCL at $a$, times 50.

   $$10(v_a-80)+v_a+5(v_a-v_c)=0\;\Rightarrow\;16v_a-5v_c=800$$

3. KCL around the supernode: in through the $10\,\Omega$, out through the $15\,\Omega$.

   $$\dfrac{v_a-v_c}{10}=\dfrac{v_d}{15}=\dfrac{v_c+1.5v_a}{15}\;\Rightarrow\;v_c=0$$

4. So

   $$v_a=50\,\mathrm{V},\quad i_\sigma=1\,\mathrm{A},\quad v_d=75\,\mathrm{V},\quad i=\dfrac{50-0}{10}=5\,\mathrm{A}$$

5. The $5\,\mathrm{A}$ enters the dependent source's $-$ end and leaves its $+$ end: it delivers power.

   $$p=(75)(5)=375\,\mathrm{W}\text{ delivered}$$

**Answer:** The dependent source delivers $375\,\mathrm{W}$ ($i_\sigma=1\,\mathrm{A}$, $75\,\mathrm{V}$ source voltage, $5\,\mathrm{A}$).

</details>

*Source: TextBook-221.pdf, PDF p. 164*

**Problem: Textbook P4.49 · Supermesh with a voltage source absorbing power** (intermediate)

Use the mesh-current method to find the total power dissipated in the circuit.

```schematic
V1 0,3 -> 0,0 "$18\,\mathrm{V}$"
R1 0,3 -> 3,3 "$3\,\Omega$"
R2 3,3 -> 6,3 "$9\,\Omega$"
I1 3,0 -> 3,3 "$3\,\mathrm{A}$"
V2 6,0 -> 6,3 "$15\,\mathrm{V}$"
R3 0,0 -> 3,0 "$2\,\Omega$"
R4 3,0 -> 6,0 "$6\,\Omega$"
label 3,3 "$m$" above
label 3,0 "$q$" below
ground 0,0
```

<details><summary>Solution</summary>

1. Clockwise $I_a$ (left) and $I_b$ (right). The shared $3\,\mathrm{A}$ source points up; $I_b$ goes up through it and $I_a$ down.

   $$I_b-I_a=3$$

2. Supermesh KVL around the outside (the $15\,\mathrm{V}$ source is walked $-\to+$: a voltage rise).

   $$-18+3I_a+9I_b-15+6I_b+2I_a=0\;\Rightarrow\;5I_a+15I_b=33$$

3. Solve.

   $$I_a=-0.6\,\mathrm{A},\qquad I_b=2.4\,\mathrm{A}$$

4. Resistor powers.

   $$(0.6)^2(3+2)+(2.4)^2(9+6)=1.8+86.4=88.2\,\mathrm{W}$$

5. Check: developed $63+36=99\,\mathrm{W}$; absorbed $88.2\,\mathrm{W}$ plus $10.8\,\mathrm{W}$ in the $18\,\mathrm{V}$ source.

**Answer:** $88.2\,\mathrm{W}$ dissipated in the resistors (and the $18\,\mathrm{V}$ source absorbs another $10.8\,\mathrm{W}$).

</details>

*Source: TextBook-221.pdf, PDF p. 167*

**Problem: Tutorial Problem 4 · Bridge circuit by nodal analysis** (advanced)

Find $i_o$, $i_1$, $i_2$ and the power delivered by the current source. The tutorial solves this source circuit with a Y–Δ transformation; this exercise uses the same givens and requested quantities, with nodal analysis as an additional solution method.

```schematic
I1 0,0 -> 0,3 "$1\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$240\,\Omega$"
R2 3,3 -> 6,3 "$20\,\Omega$"
R3 6,3 -> 6,0 "$100\,\Omega$" i="$i_2$"
R4 6,3 -> 9,3 "$50\,\Omega$"
R5 9,3 -> 9,0 "$600\,\Omega$" i="$i_o$"
wire 3,3 -> 3,5
R6 3,5 -> 9,5 "$320\,\Omega$" i="$i_1$"
wire 9,5 -> 9,3
wire 9,0 -> 0,0
label 3,5 "$a$" left
label 6,3 "$b$" above
label 9,3 "$c$" right
ground 0,0
```

<details><summary>Solution</summary>

1. Ground the bottom wire; KCL at $a$, $b$, $c$.

   $$\begin{aligned}&\dfrac{v_a}{240}+\dfrac{v_a-v_b}{20}+\dfrac{v_a-v_c}{320}=1\\&\dfrac{v_b}{100}+\dfrac{v_b-v_a}{20}+\dfrac{v_b-v_c}{50}=0\\&\dfrac{v_c}{600}+\dfrac{v_c-v_b}{50}+\dfrac{v_c-v_a}{320}=0\end{aligned}$$

2. The second gives $v_b$ as a weighted average; substitute into the third.

   $$v_b=\tfrac58v_a+\tfrac14v_c,\qquad v_c=\tfrac{15}{19}v_a,\qquad v_b=\tfrac{125}{152}v_a$$

3. Substitute into the first.

   $$v_a=72.96\,\mathrm{V},\quad v_b=60\,\mathrm{V},\quad v_c=57.6\,\mathrm{V}$$

4. Currents and source power.

   $$i_o=\dfrac{57.6}{600}=0.096\,\mathrm{A},\quad i_1=0.048\,\mathrm{A},\quad i_2=0.6\,\mathrm{A},\quad p=72.96\,\mathrm{W}$$

**Answer:** $i_o=0.096\,\mathrm{A}$, $i_1=0.048\,\mathrm{A}$, $i_2=0.6\,\mathrm{A}$; the source delivers $72.96\,\mathrm{W}$.

</details>

*Source: ELEC221 Week 4 Tutorial.pdf, PDF p. 8; ELEC221 Week 4 Tutorial.pdf, PDF p. 10; ELEC221 Week 4 Tutorial.pdf, PDF p. 11*

**Problem: Lecture 3 p.22 · Three meshes with a shared current source** (advanced)

Use the mesh-current method to find the clockwise mesh currents $i_a$ (lower left), $i_b$ (top), $i_c$ (lower right) and the voltage $v$ across the current source.

```schematic
wire 0,3 -> 0,6
R1 0,6 -> 8,6 "$10\,\Omega$"
wire 8,6 -> 8,3
R2 0,3 -> 4,3 "$3\,\Omega$"
R3 4,3 -> 8,3 "$2\,\Omega$"
I1 4,0 -> 4,3 "$5\,\mathrm{A}$" v_rev="$v$"
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
V2 8,3 -> 8,0 "$50\,\mathrm{V}$"
R4 0,0 -> 4,0 "$6\,\Omega$"
R5 4,0 -> 8,0 "$4\,\Omega$"
label 4,3 "$m$" above
label 4,0 "$q$" below
label 8,3 "$r$" right
label 8,0 "$p$" right
ground 0,0
```

<details><summary>Solution</summary>

1. The shared source points up; $i_c$ goes up through it, $i_a$ down.

   $$i_c-i_a=5$$

2. Top mesh.

   $$10i_b+2(i_b-i_c)+3(i_b-i_a)=0\;\Rightarrow\;15i_b-3i_a-2i_c=0$$

3. Supermesh around the bottom two meshes, skipping the source.

   $$\begin{aligned}&-100+3(i_a-i_b)+2(i_c-i_b)+50+4i_c+6i_a=0\\&\Rightarrow\;9i_a-5i_b+6i_c=50\end{aligned}$$

4. Substitute $i_c=i_a+5$: $i_a=3i_b-2$ from the top mesh, then $15i_a-5i_b=20$.

   $$i_b=1.25\,\mathrm{A},\quad i_a=1.75\,\mathrm{A},\quad i_c=6.75\,\mathrm{A}$$

5. Node voltages at the source's ends.

   $$v=\big(100-3(0.5)\big)-6(1.75)=98.5-10.5=88\,\mathrm{V}$$

**Answer:** $i_a=1.75\,\mathrm{A}$, $i_b=1.25\,\mathrm{A}$, $i_c=6.75\,\mathrm{A}$; $v=88\,\mathrm{V}$

</details>

*Source: ELEC 221 Week 3.pdf, PDF p. 22*

**Problem: Textbook P4.41 · A signed dependent-source voltage** (advanced)

Use the mesh-current method to find the power developed in the dependent voltage source. Mesh 1 is lower left, mesh 2 the top, mesh 3 lower right (all clockwise).

```schematic
V1 0,4 -> 0,0 "$25\,\mathrm{V}$"
R1 0,4 -> 3,4 "$2\,\Omega$"
R2 3,4 -> 6,4 "$3\,\Omega$" v="$v_\phi$"
R3 3,4 -> 3,2 "$5\,\Omega$"
V2 3,2 -> 3,0 "$10\,\mathrm{V}$"
R4 6,4 -> 6,0 "$1\,\Omega$"
wire 6,0 -> 0,0
wire 0,4 -> 0,6
E1 3,6 -> 0,6 "$-3v_\phi$"
R5 3,6 -> 6,6 "$14\,\Omega$"
wire 6,6 -> 6,4
label 3,4 "$m$" above
ground 0,0
```

<details><summary>Solution</summary>

1. Control first: $v_\phi$ is across the $3\,\Omega$ shared by meshes 2 and 3.

   $$v_\phi=3(i_3-i_2)$$

2. KVL equations.

   $$\begin{aligned}&-25+2(i_1-i_2)+5(i_1-i_3)+10=0\\&3v_\phi+14i_2+3(i_2-i_3)+2(i_2-i_1)=0\\&i_3-10+5(i_3-i_1)+3(i_3-i_2)=0\end{aligned}$$

3. Solve with the control.

   $$i_1=4\,\mathrm{A},\quad i_2=-1\,\mathrm{A},\quad i_3=3\,\mathrm{A},\quad v_\phi=12\,\mathrm{V}$$

4. The voltage from the dependent source marked + to its marked − is $-3v_\phi=-36$ V. Current entering that + terminal is $-i_2=1$ A.

   $$p_{\mathrm{abs}}=(-3v_\phi)(-i_2)=-36\,\mathrm{W},\quad P_{\mathrm{del}}=36\,\mathrm{W}$$

**Answer:** The dependent source delivers $36\,\mathrm{W}$ (absorbs $-36\,\mathrm{W}$).

</details>

*Source: TextBook-221.pdf, PDF p. 166*

**Problem: Textbook P4.19 · Voltage-controlled current source** (advanced)

Use nodal analysis to find **(a)** $v_o$ across the $1250\,\Omega$ resistor and **(b)** the total power supplied. The dependent current source is $v_\Delta/(3000\,\Omega)$; its arrow points down.

```schematic
V1 0,3 -> 0,0 "$120\,\mathrm{V}$"
R1 0,3 -> 3,3 "$800\,\Omega$"
G1 3,3 -> 3,0 "$v_\Delta/3000$"
R2 3,3 -> 6,3 "$1250\,\Omega$" v="$v_o$"
R3 6,3 -> 6,0 "$500\,\Omega$" v="$v_\Delta$"
wire 6,3 -> 9,3
I1 9,0 -> 9,3 "$20\,\mathrm{mA}$"
wire 0,0 -> 9,0
label 3,3 "$a$" above
label 6,3 "$b$" above
ground 0,0
```

<details><summary>Solution</summary>

1. Ground the bottom node. Name the two unknown voltages $v_a$ and $v_b$. The control voltage is across the $500\,\Omega$ resistor.

   $$v_\Delta=v_b,\qquad v_o=v_a-v_b$$

2. Take resistor currents leaving each node as positive. Use kΩ and mA throughout these two equations.

   $$\begin{aligned}\dfrac{v_a-120}{0.8}+\dfrac{v_a-v_b}{1.25}+\dfrac{v_b}{3}&=0\\\dfrac{v_b-v_a}{1.25}+\dfrac{v_b}{0.5}&=20\end{aligned}$$

3. Clear the fractions. Express $v_b$ from the second equation and substitute it into the first.

   $$\begin{aligned}123v_a-28v_b&=9000,&-2v_a+7v_b&=50\\v_b&=\dfrac{50+2v_a}{7},&123v_a-4(50+2v_a)&=9000\end{aligned}$$

4. Solve, then take the requested voltage difference.

   $$v_a=80\,\mathrm{V},\quad v_b=30\,\mathrm{V},\quad v_o=80-30=50\,\mathrm{V}$$

5. The 120 V source supplies 50 mA; the independent current source supplies 20 mA at 30 V. The dependent current source absorbs power.

   $$\begin{gathered}P_{\mathrm{supplied}}=120(0.05)+30(0.02)=6.6\,\mathrm{W}\\P_{\mathrm{absorbed}}=2+2+1.8+0.8=6.6\,\mathrm{W}\end{gathered}$$

**Answer:** **(a)** $v_o=50\,\mathrm{V}$. **(b)** $6.6\,\mathrm{W}$ supplied.

</details>

*Source: TextBook-221.pdf, PDF p. 164*

**Problem: Textbook P4.23 · A source controlled by voltage-source current** (advanced)

Use nodal analysis to find $v_o$. The control current $i_\Delta$ points upward through the $10\,\mathrm{V}$ source. The dependent source has $+$ at ground and voltage $(20\,\Omega)i_\Delta$.

```schematic
V1 0,3 -> 0,0 "$10\,\mathrm{V}$" i_rev="$i_\Delta$"
R1 0,3 -> 3,3 "$10\,\Omega$"
R2 3,3 -> 6,3 "$20\,\Omega$"
R3 3,3 -> 3,0 "$40\,\Omega$" v="$v_o$"
E1 6,0 -> 6,3 "$20i_\Delta$"
wire 0,3 -> 0,5
R4 0,5 -> 6,5 "$30\,\Omega$"
wire 6,5 -> 6,3
wire 0,0 -> 6,0
label 0,3 "$a$" left
label 3,3 "$b$" above
label 6,3 "$c$" right
ground 0,0
```

<details><summary>Solution</summary>

1. Ground the bottom node. The left node is 10 V; the unknowns are $v_b=v_o$ and $v_c$. Find the control current with KCL at the 10 V node.

   $$i_\Delta=\dfrac{10-v_b}{10}+\dfrac{10-v_c}{30}$$

2. Use the dependent source polarity exactly as drawn.

   $$0-v_c=20i_\Delta\quad\Rightarrow\quad v_c=6v_b-80$$

3. Write KCL at node $b$, using voltage differences for each resistor current.

   $$\dfrac{v_b-10}{10}+\dfrac{v_b-v_c}{20}+\dfrac{v_b}{40}=0\quad\Rightarrow\quad7v_b-2v_c=40$$

4. Substitute the source constraint into KCL and solve.

   $$7v_b-2(6v_b-80)=40\quad\Rightarrow\quad v_b=24\,\mathrm{V},\quad v_c=64\,\mathrm{V}$$

5. Check the control current and source constraint. The negative current is opposite its upward reference.

   $$i_\Delta=\dfrac{10-24}{10}+\dfrac{10-64}{30}=-3.2\,\mathrm{A},\quad -v_c=20(-3.2)=-64\,\mathrm{V}$$

**Answer:** $v_o=24\,\mathrm{V}$.

</details>

*Source: TextBook-221.pdf, PDF p. 164*

**Problem: Tutorial P3.3 · Find an unknown resistor from a required current** (intermediate)

From the uploaded Week 4 tutorial: **(a)** choose $R$ so the current down the $80\,\Omega$ resistor is $4\,\mathrm{A}$; **(b)** find the power dissipated in $R$; **(c)** find the power generated by the current source. Use nodal voltages and KCL.

```schematic
I1 0,0 -> 0,5 "$20\,\mathrm{A}$"
R1 0,5 -> 4,5 "$60\,\Omega$"
R2 4,5 -> 4,2.5 "$40\,\Omega$"
R3 4,2.5 -> 4,0 "$80\,\Omega$" i="$4\,\mathrm{A}$"
wire 4,5 -> 7,5
R4 7,5 -> 7,0 "$R$"
wire 0,0 -> 7,0
label 0,5 "$s$" above
label 4,5 "$a$" above
label 4,2.5 "$b$" left
ground 0,0
```

<details><summary>Solution</summary>

1. Ground the bottom node. The specified resistor current fixes $v_b$. There is no branch at $b$ except the 40 Ω and 80 Ω resistors.

   $$v_b=80(4)=320\,\mathrm{V},\quad \dfrac{v_a-v_b}{40}=4\quad\Rightarrow\quad v_a=480\,\mathrm{V}$$

2. All 20 A from the source passes through the 60 Ω resistor. Apply KCL at $a$ to find the remaining branch current.

   $$20=\dfrac{480-320}{40}+\dfrac{480}{R}\quad\Rightarrow\quad i_R=16\,\mathrm{A}$$

3. Use the voltage across $R$ and its current to find the unknown resistance and its power.

   $$R=\dfrac{480}{16}=30\,\Omega,\qquad P_R=480(16)=7680\,\mathrm{W}$$

4. Find the current-source voltage by adding the drop across 60 Ω to $v_a$. The source current enters its negative-voltage terminal.

   $$v_s=480+60(20)=1680\,\mathrm{V},\quad P_{\mathrm{generated}}=1680(20)=33600\,\mathrm{W}$$

5. Check power in all four resistors.

   $$20^2(60)+4^2(40)+4^2(80)+16^2(30)=33600\,\mathrm{W}$$

**Answer:** **(a)** $R=30\,\Omega$. **(b)** $7680\,\mathrm{W}$. **(c)** $33.6\,\mathrm{kW}$ generated.

</details>

*Source: ELEC221 Week 4 Tutorial.pdf, PDF p. 4*

**Problem: Tutorial P3.4 · A return-path resistor changes the node voltages** (advanced)

From the uploaded Week 4 tutorial: **(a)** use voltage division to find $v_o$ across the $40\,\Omega$; **(b)** find its current, then the current in $30\,\Omega$; **(c)** find the power absorbed by $50\,\Omega$. As an additional nodal exercise, reproduce the answer using the labeled nodes. The $70\,\Omega$ is in the return path, so node $b$ is not ground.

```schematic
V1 0,4 -> 0,0 "$60\,\mathrm{V}$"
R1 0,4 -> 3,4 "$40\,\Omega$" v="$v_o$"
R2 0,0 -> 3,0 "$70\,\Omega$"
R3 3,4 -> 3,0 "$20\,\Omega$"
wire 3,4 -> 6,4
R4 6,4 -> 6,0 "$30\,\Omega$" i="$i_{30}$"
R5 6,4 -> 9,4 "$50\,\Omega$"
R6 9,4 -> 9,0 "$10\,\Omega$"
wire 3,0 -> 9,0
label 3,4 "$a$" above
label 6,0 "$b$" below
label 9,4 "$c$" above
ground 0,0
```

<details><summary>Solution</summary>

1. Combine the right branch, then the three branches between $a$ and $b$.

   $$R_{ab}=20\parallel30\parallel(50+10)=10\,\Omega,\quad R_{\mathrm{total}}=40+10+70=120\,\Omega$$

2. Use the source current and voltage division.

   $$i_{40}=\dfrac{60}{120}=0.5\,\mathrm{A},\quad v_o=40(0.5)=20\,\mathrm{V}$$

3. The parallel network has 5 V across it; compute the requested branch current and power.

   $$\begin{gathered}v_a-v_b=0.5(10)=5\,\mathrm{V}\\i_{30}=\frac5{30}=166.67\,\mathrm{mA}\\P_{50}=\left(\frac5{60}\right)^2 50=347.22\,\mathrm{mW}\end{gathered}$$

4. For the nodal check, ground the source negative terminal. Write KCL at $a$, $b$ and $c$.

   $$\begin{aligned}\dfrac{v_a-60}{40}+\dfrac{v_a-v_b}{20}+\dfrac{v_a-v_b}{30}+\dfrac{v_a-v_c}{50}&=0\\\dfrac{v_b}{70}+\dfrac{v_b-v_a}{20}+\dfrac{v_b-v_a}{30}+\dfrac{v_b-v_c}{10}&=0\\\dfrac{v_c-v_a}{50}+\dfrac{v_c-v_b}{10}&=0\end{aligned}$$

5. The third equation gives $v_c=(v_a+5v_b)/6$. Substitute into the first two; simplify and solve.

   $$5v_a-4v_b=60,\quad8v_b-7v_a=0\quad\Rightarrow\quad v_a=40,\ v_b=35,\ v_c=\dfrac{215}{6}\,\mathrm{V}$$

6. Use differences between nodes, including the source node, to confirm the result.

   $$v_o=60-40=20\,\mathrm{V},\quad i_{30}=\dfrac{40-35}{30}=\frac16\,\mathrm{A}$$

**Answer:** **(a)** $v_o=20\,\mathrm{V}$. **(b)** $i_{40}=0.5\,\mathrm{A}$ and $i_{30}=166.67\,\mathrm{mA}$. **(c)** $P_{50}=347.22\,\mathrm{mW}$.

</details>

*Source: ELEC221 Week 4 Tutorial.pdf, PDF p. 6*

**Problem: Textbook P4.44 · A perimeter current source fixes one of three meshes** (advanced)

Use mesh analysis to find **(a)** the power delivered by the $12\,\mathrm{A}$ source, **(b)** the total power delivered, and **(c)** the total power dissipated. Choose clockwise currents $I_1$ in the upper-left mesh, $I_2$ in the upper-right mesh, and $I_3$ in the bottom mesh.

```schematic
V1 0,4 -> 0,1 "$600\,\mathrm{V}$"
R1 0,4 -> 4,4 "$10\,\Omega$"
R2 4,4 -> 8,4 "$8\,\Omega$"
V2 8,4 -> 8,1 "$400\,\mathrm{V}$"
R3 0,1 -> 4,1 "$14\,\Omega$"
R4 4,1 -> 8,1 "$2\,\Omega$"
R5 4,4 -> 4,1 "$40\,\Omega$"
wire 0,1 -> 0,-2 -> 2,-2
I1 2,-2 -> 6,-2 "$12\,\mathrm{A}$"
wire 6,-2 -> 8,-2 -> 8,1
label 4,4 "$b$" above
label 4,1 "$m$" below
label 8,1 "$r$" right
ground 0,1
```

<details><summary>Solution</summary>

1. The bottom mesh traverses the current-source branch from right to left. Its clockwise current therefore opposes the source arrow.

   $$I_3=-12\,\mathrm{A}$$

2. Write KVL in the other two meshes. The 40 Ω branch carries a difference of mesh currents.

   $$\begin{aligned}-600+10I_1+40(I_1-I_2)+14(I_1-I_3)&=0\\400+8I_2+40(I_2-I_1)+2(I_2-I_3)&=0\end{aligned}$$

3. Substitute the known current, then express $I_1$ from the first equation.

   $$64I_1-40I_2=432,\quad-40I_1+50I_2=-424,\quad I_1=6.75+0.625I_2$$

4. Substitute into the second equation.

   $$-40(6.75+0.625I_2)+50I_2=-424\quad\Rightarrow\quad I_2=-6.16\,\mathrm{A},\ I_1=2.9\,\mathrm{A}$$

5. Ground the left terminal of the 12 A source to calculate its voltage. Follow the two bottom resistors from left to right.

   $$\begin{gathered}v_r=14(I_1-I_3)+2(I_2-I_3)=220.28\,\mathrm{V}\\P_{12\mathrm{A},\mathrm{del}}=12(220.28)=2643.36\,\mathrm{W}\end{gathered}$$

6. Both voltage sources also deliver power. Add the resistor powers using their actual branch currents.

   $$\begin{aligned}P_{\mathrm{del}}&=2643.36+600(2.9)+400(6.16)=6847.36\,\mathrm{W}\\P_R&=10(2.9)^2+8(6.16)^2+40(9.06)^2\\&\quad+14(14.9)^2+2(5.84)^2=6847.36\,\mathrm{W}\end{aligned}$$

**Answer:** **(a)** $2643.36\,\mathrm{W}$. **(b)** $6847.36\,\mathrm{W}$. **(c)** $6847.36\,\mathrm{W}$.

</details>

*Source: TextBook-221.pdf, PDF p. 166*

**Problem: Textbook P4.47 · A dependent source uses a shared current with a reversed arrow** (advanced)

Use mesh analysis to find **(a)** $i_\Delta$; **(b)** the power delivered by the independent current source; **(c)** the power delivered by the dependent voltage source. Use clockwise $I_1$ for the left mesh and $I_2$ for the right mesh. The control arrow $i_\Delta$ points upward.

```schematic
I1 0,0 -> 0,3 "$8\,\mathrm{mA}$"
R1 0,3 -> 3,3 "$980\,\Omega$"
R2 3,3 -> 3,0 "$3.3\,\mathrm{k\Omega}$" i_rev="$i_\Delta$"
R3 3,3 -> 6,3 "$1.8\,\mathrm{k\Omega}$"
E1 6,3 -> 6,0 "$200i_\Delta$"
R4 6,0 -> 3,0 "$4.7\,\mathrm{k\Omega}$"
wire 3,0 -> 0,0
label 0,3 "$s$" above
label 3,3 "$a$" above
ground 0,0
```

<details><summary>Solution</summary>

1. The perimeter source fixes $I_1$. The upward shared-branch arrow is opposite the left mesh current in that branch.

   $$I_1=8\,\mathrm{mA},\qquad i_\Delta=I_2-I_1$$

2. Write KVL in the right mesh. Use kΩ and mA; the dependent voltage is $(0.2\,\mathrm{k\Omega})i_\Delta$.

   $$1.8I_2+0.2(I_2-I_1)+4.7I_2+3.3(I_2-I_1)=0$$

3. Substitute $I_1$ and solve.

   $$10I_2-3.5(8)=0\quad\Rightarrow\quad I_2=2.8\,\mathrm{mA},\quad i_\Delta=-5.2\,\mathrm{mA}$$

4. Find the voltage at the top of the independent source using the resistor voltages.

   $$v_a=3.3(8-2.8)=17.16\,\mathrm{V},\quad v_s=17.16+0.98(8)=25\,\mathrm{V}$$

5. Calculate delivered power with the indicated source polarities. Current $I_2$ enters the dependent source positive terminal, but its voltage is negative.

   $$P_{8\mathrm{mA},\mathrm{del}}=25(8)=200\,\mathrm{mW},\quad P_{E,\mathrm{del}}=-[0.2(-5.2)](2.8)=2.912\,\mathrm{mW}$$

**Answer:** **(a)** $i_\Delta=-5.2\,\mathrm{mA}$. **(b)** $200\,\mathrm{mW}$. **(c)** $2.912\,\mathrm{mW}$.

</details>

*Source: TextBook-221.pdf, PDF p. 167*

## Summary

- Nodal analysis and node-voltage analysis are the same method; mesh analysis and mesh-current analysis are the same method.
- Pick ground and name the remaining node voltages before writing KCL.
- Choose reference current arrows first; a negative result gives the opposite physical direction.
- A resistor current uses the difference between its two node voltages, not automatically a node voltage relative to ground.
- Mesh currents must be converted to branch currents before using Ohm's law or power formulas.
- Supernodes need voltage constraints; supermeshes need current constraints.
- Substitute dependent-source controls into the equations and check KCL, KVL and power afterward.

### Formula sheet

| Result | Formula | Use when |
|---|---|---|
| Resistor current | $i_{a\to b}=\dfrac{v_a-v_b}{R}$ | Writing nodal equations or recovering a branch current. |
| KCL | $\sum i_{\mathrm{leaving}}=0$ | At a node or around a supernode. |
| KVL | $\sum v_{\mathrm{drops}}=0$ | Around a mesh or supermesh; include signed source voltages. |
| Shared mesh resistor | $v_R=R(I_1-I_2)$ | Traversal follows mesh 1 and the two mesh contributions oppose. |
| Voltage-source constraint | $v_a-v_b=V_s$ | Source + is at a and − at b. |
| Source power | $p_{\mathrm{abs}}=vi$ | Current i enters the terminal marked +; a negative result is delivered power. |
| Resistor power | $p_R=i^2R=\dfrac{v_R^2}{R}$ | Use the actual branch current or resistor voltage. |
