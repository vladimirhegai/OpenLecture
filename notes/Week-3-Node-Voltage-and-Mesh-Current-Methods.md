# Week 3: Node-Voltage and Mesh-Current Methods

## Overview

> **Info:** Week 3 turns Kirchhoff’s current law (KCL), Kirchhoff’s voltage law (KVL), and Ohm’s law into two systematic ways to solve circuits that are difficult to reduce by series and parallel combinations. First identify the circuit’s structure, then solve for node voltages or mesh currents, including the constraints imposed by dependent sources.

### Learning outcomes

- Identify planar circuits, nodes, essential nodes, branches, essential branches, loops, and meshes (Nilsson 4.1).
- Apply the node-voltage method with independent and dependent sources, including known node voltages and supernodes (Nilsson 4.2–4.4).
- Apply the mesh-current method to planar circuits with independent and dependent sources, including known mesh currents and supermeshes (Nilsson 4.5–4.7).

## Topic 1: Circuit analysis terminology

Topology tells you which points share a voltage and which elements share a current. Treat an uninterrupted ideal wire as one node, regardless of how many bends or labeled points it contains. A planar circuit can be redrawn on a flat plane without branch crossings; a crossing in one drawing does not by itself make the circuit nonplanar.

| Term | Meaning |
|---|---|
| Node | A connection of two or more elements; all points on the same ideal wire have one potential. |
| Essential node | A node where three or more elements meet. |
| Path | A trace through connected elements without repeating an element. |
| Branch | An element path between nodes; use individual elements when counting branches here. |
| Essential branch | A path between essential nodes that passes through no other essential node; it may contain several series elements. |
| Loop | A closed path whose final node is its starting node. |
| Mesh | A loop containing no other loop in a planar drawing. |
| Planar circuit | A circuit that admits a drawing with no crossing branches. |

$$N_{\mathrm{KCL}}=n-1,\qquad M=b-n+1=b_e-n_e+1$$

Here $n$ counts all nodes, $b$ counts all element branches, $n_e$ counts essential nodes, $b_e$ counts essential branches, and $M$ counts independent loops (meshes for a connected planar drawing). These are structural counts. Known current sources add current constraints, so do not count their currents as new unknowns or blindly use the structural mesh count as the number of ordinary KVL equations. Only $n-1$ KCL equations are independent because adding the equations for all nodes gives zero.

**Example: Reading a circuit's structure (Lecture 3)**

Find the nodes, essential nodes, branches, essential branches and meshes.

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

1. The distinct nodes are a, b, c, d, e, f, g. Each of the ten listed elements forms one branch.

   $$n=7,\qquad b=10$$
2. These four nodes each connect at least three elements. Nodes a, d, f each connect only two.

   $$n_e=4,\qquad \{b,c,e,g\}$$
3. The essential branches are c–a–b; c–f–g; c–d–e; b–e; e–g; and the two distinct b–g branches through R7 and I.

   $$b_e=7$$
4. The meshes use (v1,R1,R5,R3,R2), (v2,R4,R6,R3,R2), (R5,R6,R7), and (R7,I). The loop through R5,R6,I encloses a smaller loop and is not a mesh.

   $$M=10-7+1=7-4+1=4$$

**Answer:** 7 nodes ($a$–$g$); 4 essential nodes ($b,c,e,g$); 10 branches; 7 essential branches; 4 meshes.

> **Warning:** A line crossing without a junction is not a connection. Keep parallel branches separate when counting; two elements with the same endpoints still form two branches. A mesh depends on a planar drawing, whereas a node depends on electrical connectivity.

> **Tip:** Collapse only the nonessential nodes when counting essential branches. Verify your mesh count with both $b-n+1$ and $b_e-n_e+1$.

## Topic 2: Node-voltage method

Use node voltages when you want a compact description of the circuit’s electrical potentials. Choose a reference node, assign its voltage zero, and write KCL at the remaining unknown nodes. Ohm’s law expresses every resistor current using the voltages at its ends. This often avoids solving separately for every branch current.

| Term | Meaning |
|---|---|
| Reference node (ground) | The chosen zero of potential; it need not represent a physical earth connection. |
| Node voltage $v_k$ | The potential at node $k$ relative to the reference node, positive at node $k$. |
| Conductance $G$ | $G=\dfrac{1}{R}$, where $R$ is resistance; conductance is measured in siemens. |
| Supernode | A group of non-reference nodes linked by ideal voltage sources, handled with boundary KCL and voltage constraints. |

$$i_{k\to j}=\frac{v_k-v_j}{R_{kj}},\qquad \sum_j\frac{v_k-v_j}{R_{kj}}=I_{k,\mathrm{in}}$$

The current $i_{k\to j}$ is defined from node $k$ toward node $j$ through resistance $R_{kj}$. Voltages $v_k$ and $v_j$ use the same reference. The sum includes the resistor branches incident on node $k$; $I_{k,\mathrm{in}}$ is the net current injected into that node by current sources. A negative current means the actual direction opposes the chosen arrow.

**From KCL to the node-voltage equation**

1. Choose resistor currents leaving the node as positive. An injected source current enters and therefore has the opposite sign.

   $$\sum_j i_{k\to j}-I_{k,\mathrm{in}}=0$$
2. Replace each resistor current with its voltage difference divided by resistance.

   $$\sum_j\frac{v_k-v_j}{R_{kj}}=I_{k,\mathrm{in}}$$
3. Collect the unknown voltages. For ordinary positive resistors, the diagonal coefficient sums incident conductances and each off-diagonal coefficient is the negative connecting conductance.

   $$v_k\sum_jG_{kj}-\sum_jG_{kj}v_j=I_{k,\mathrm{in}},\qquad G_{kj}=\frac{1}{R_{kj}}$$

1. Choose a convenient reference, usually a node with many branches.
2. Label every non-reference voltage and mark voltages already fixed by sources.
3. Write KCL at unknown ordinary nodes and at supernode boundaries.
4. Write every voltage-source relation and dependent-source control relation.
5. Solve the simultaneous equations, then recover branch currents and powers.
6. Check KCL, source constraints, and total absorbed versus delivered power.

> **Warning:** Node-voltage analysis also works for nonplanar circuits. The planarity check appearing in the lecture’s nodal procedure is unnecessary for this method; planarity is required for the mesh-current method. Never apply Ohm’s law to an ideal voltage source to guess its current.

**Example: Two unknown node voltages (Lecture 3)**

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
ground 3,0
```

1. The source fixes vs=10 V; three resistor currents leave node 1.

   $$\frac{v_1-10}{1}+\frac{v_1}{5}+\frac{v_1-v_2}{2}=0$$
2. The 2 A source injects current into node 2.

   $$\frac{v_2-v_1}{2}+\frac{v_2}{10}=2$$
3. Multiply the KCL equations by 10 to remove fractions.

   $$17v_1-5v_2=100,\qquad -5v_1+6v_2=20$$
4. Substitute the second equation into the first.

   $$v_2=\frac{20+5v_1}{6},\qquad 77v_1=700$$
5. These are voltages relative to ground.

   $$v_1=\frac{100}{11}\,\mathrm{V}\approx9.091\,\mathrm{V},\qquad v_2=\frac{120}{11}\,\mathrm{V}\approx10.909\,\mathrm{V}$$
6. The negative sign means current actually flows from node 2 toward node 1.

   $$i_{1\to2}=\frac{v_1-v_2}{2}=-\frac{10}{11}\,\mathrm{A}$$

**Answer:** $v_1=\dfrac{100}{11}\approx9.09\,\mathrm{V}$, $v_2=\dfrac{120}{11}\approx10.91\,\mathrm{V}$

**Example: One node equation (Lecture 3)**

Use the node-voltage method to find the branch currents $i_a$, $i_b$ and $i_c$.

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
ground 3,0
```

1. Take the bottom wire as the reference. Only node $a$ is unknown; the $50\,\mathrm{V}$ source fixes the left end of the $5\,\Omega$ resistor. Sum the currents leaving $a$; the $3\,\mathrm{A}$ source enters it.

   $$\frac{v_a-50}{5}+\frac{v_a}{10}+\frac{v_a}{40}-3=0$$
2. Multiply by 40 and solve.

   $$8v_a-400+4v_a+v_a-120=0\ \Rightarrow\ 13v_a=520\ \Rightarrow\ v_a=40\,\mathrm{V}$$
3. Recover each branch current with Ohm's law, using its arrow.

   $$i_a=\frac{50-40}{5}=2\,\mathrm{A},\quad i_b=\frac{40}{10}=4\,\mathrm{A},\quad i_c=\frac{40}{40}=1\,\mathrm{A}$$
4. Check KCL at $a$: $i_a$ plus the source current must leave through $i_b$ and $i_c$.

   $$2+3=4+1$$

**Answer:** $v_a=40\,\mathrm{V}$; $i_a=2\,\mathrm{A}$, $i_b=4\,\mathrm{A}$, $i_c=1\,\mathrm{A}$

### Dependent sources: retain the control equation

A dependent source’s value must be solved with the rest of the circuit. Express its controlling current or voltage in the same node-voltage unknowns before substituting. For a current-controlled voltage source, the proportionality coefficient has units of ohms; for a voltage-controlled current source it has units of siemens.

$$i_\Phi=\frac{v_a-v_b}{R_{ab}},\qquad v_c=r_m i_\Phi$$

Here $i_\Phi$ is the controlling current from $a$ to $b$, $R_{ab}$ is that resistor’s resistance, $v_c$ is the voltage of a dependent source whose negative terminal is grounded, and $r_m$ is its current-to-voltage coefficient in ohms. The signs must follow the control arrow and source polarity.

**Example: Node voltages with a dependent source (Lecture 3)**

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
ground 3,0
```

1. KCL at node a.

   $$\frac{v_a-20}{2}+\frac{v_a}{20}+\frac{v_a-v_b}{5}=0$$
2. KCL at b and the controlling-current relation.

   $$\frac{v_b-v_a}{5}+\frac{v_b}{10}+\frac{v_b-v_c}{2}=0,\qquad v_c=8\frac{v_a-v_b}{5}$$
3. Substitute the dependent-source value, then collect terms.

   $$0.75v_a-0.2v_b=10,\qquad -v_a+1.6v_b=0$$
4. Elimination reduces the first equation to vb=10 V.

   $$v_a=1.6v_b,\qquad v_b=10\,\mathrm{V},\qquad v_a=16\,\mathrm{V}$$
5. Recover the source control and check its prescribed value.

   $$i_\Phi=\frac{16-10}{5}=1.2\,\mathrm{A},\qquad v_c=9.6\,\mathrm{V}$$
6. Resistor power is nonnegative under the passive sign convention.

   $$P_{5\Omega}=i_\Phi^2(5\,\Omega)=7.2\,\mathrm{W}$$

**Answer:** $v_a=16\,\mathrm{V}$, $v_b=10\,\mathrm{V}$, $i_\Phi=1.2\,\mathrm{A}$, $p_{5\Omega}=7.2\,\mathrm{W}$

### Known voltages and supernodes

A voltage source connected to the reference node directly fixes the other node’s voltage, with the sign determined by its polarity. A source between two unknown non-reference nodes fixes only their voltage difference. Enclose those nodes and the source in a supernode, write KCL for currents crossing the boundary, and add the voltage constraint. Internal source current cancels from boundary KCL.

**Example: A voltage source to ground fixes a node (Lecture 3)**

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
ground 3,0
```

1. The $100\,\mathrm{V}$ source sits between node 1 and the reference, so node 1 is known and needs no equation (special case 1).

   $$v_1=100\,\mathrm{V}$$
2. Write KCL at node 2 only, with currents leaving; the $5\,\mathrm{A}$ source enters node 2.

   $$\frac{v_2-100}{10}+\frac{v_2}{50}-5=0$$
3. Multiply by 50 and solve.

   $$5v_2-500+v_2-250=0\ \Rightarrow\ v_2=125\,\mathrm{V}$$

**Answer:** $v_1=100\,\mathrm{V}$, $v_2=125\,\mathrm{V}$

$$v_p-v_q=V_s,\qquad \sum_{\text{boundary}}i_{\mathrm{out}}=0$$

The source is positive at node $p$ and negative at node $q$, and $V_s$ is its voltage, independent or controlled. The boundary-current sum counts currents leaving the supernode, with entering currents negative. The two nodes remain distinct voltages; they are grouped only for KCL.

**Example: A supernode with a dependent source (Lecture 3)**

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
ground 3,0
```

1. The grounded source fixes va. Keep the leftward controlling-current arrow.

   $$v_a=50\,\mathrm{V},\qquad i_\Phi=\frac{v_b-50}{5}$$
2. Only branches crossing the b–c supernode boundary enter its KCL equation.

   $$\frac{v_b-50}{5}+\frac{v_b}{50}+\frac{v_c}{100}-4=0$$
3. The dependent source supplies the missing voltage relation.

   $$v_c-v_b=10i_\Phi=2(v_b-50),\qquad v_c=3v_b-100$$
4. Substitute before solving.

   $$\frac{v_b-50}{5}+\frac{v_b}{50}+\frac{3v_b-100}{100}-4=0\ \Rightarrow\ 0.25v_b=15$$
5. The source voltage is 20 V, equal to 10 ohms times 2 A.

   $$v_b=60\,\mathrm{V},\qquad v_c=80\,\mathrm{V},\qquad i_\Phi=2\,\mathrm{A}$$

**Answer:** $v_b=60\,\mathrm{V}$, $v_c=80\,\mathrm{V}$, $i_\Phi=2\,\mathrm{A}$

> **Warning:** Do not set the two supernode voltages equal. Do not include the internal voltage-source current in boundary KCL. A controlling current such as $\dfrac{v_b-v_a}{R}$ changes sign if you reverse its arrow.

> **Tip:** Choose a reference that makes a voltage source directly set a node voltage when practical. Keep a small equation checklist: one KCL relation per unknown ordinary node or supernode, plus every source and control constraint.

## Topic 3: Mesh-current method

For a planar circuit, assign one hypothetical circulating current to each mesh and write KVL around those meshes. A branch belonging to one mesh carries that mesh current. A branch shared by two meshes carries their algebraic combination. Assigning every mesh clockwise makes a shared resistor’s current a difference, which is easy to keep consistent.

| Term | Meaning |
|---|---|
| Mesh current $I_k$ | A chosen circulating current around mesh $k$; it is an analysis variable rather than necessarily a physical branch current. |
| Shared branch current | The signed sum of the mesh currents crossing a branch; for two clockwise adjacent meshes it is their difference. |
| Supermesh | A combined KVL contour that bypasses a current-source branch shared by two meshes. |
| Perimeter current source | A source belonging to only one mesh; it fixes that mesh current directly. |

$$i_{k\to\ell}=I_k-I_\ell,\qquad v_R=R(I_k-I_\ell)$$

Here $I_k$ and $I_\ell$ are clockwise currents in neighboring meshes. The shared branch current $i_{k\to\ell}$ and resistor voltage drop $v_R$ are referenced in mesh $k$’s traversal direction, and $R$ is the shared resistance. In mesh $\ell$’s KVL equation, the same drop is $R(I_\ell-I_k)$.

**Build the lecture’s two-mesh equations**

1. Take clockwise currents IL and IR in the left and right windows. V1 is the left source voltage, V2 the right source voltage, R1 the left-top resistance, R2 the right-top resistance, and R3 the shared center-to-bottom resistance. Both sources are positive at their upper terminals. The left source is a rise.

   $$-V_1+R_1I_L+R_3(I_L-I_R)=0$$
2. Clockwise traversal through the right source goes from its positive terminal to its negative terminal, so it is a drop.

   $$V_2+R_2I_R+R_3(I_R-I_L)=0$$
3. Collect terms. V1 fixes the left top node and V2 fixes the right top node relative to the common bottom node. R1 connects left to center, R2 center to right, and R3 center to bottom.

   $$(R_1+R_3)I_L-R_3I_R=V_1,\qquad -R_3I_L+(R_2+R_3)I_R=-V_2$$
4. The lecture’s rightward top currents are i1 and i2; its downward center current is i3. Recover physical branch currents after solving.

   $$i_1=I_L,\qquad i_2=I_R,\qquad i_3=I_L-I_R$$

> **Warning:** KVL requires a consistent traversal direction and source polarity: traversing $-\to+$ is a rise, and $+\to-$ is a drop. Mesh currents can be negative; keep the original arrows and interpret the sign after solving. Check planarity before using meshes.

**Example: Three meshes (Lecture 3)**

Use mesh currents to find the power of each voltage source and the voltage $v_o$.

```schematic
V1 0,3 -> 0,0 "$40\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
R2 3,3 -> 3,0 "$8\,\Omega$" v="$v_o$"
R3 3,3 -> 6,3 "$6\,\Omega$"
R4 6,3 -> 6,0 "$6\,\Omega$"
R5 6,3 -> 9,3 "$4\,\Omega$"
V2 9,3 -> 9,0 "$20\,\mathrm{V}$"
wire 9,0 -> 0,0
```

1. KVL in the left mesh.

   $$-40+2I_1+8(I_1-I_2)=0$$
2. The center mesh shares the vertical resistors with its neighbors.

   $$8(I_2-I_1)+6I_2+6(I_2-I_3)=0$$
3. The right source is a drop in clockwise traversal.

   $$6(I_3-I_2)+4I_3+20=0$$
4. Collect terms with currents in amperes.

   $$10I_1-8I_2=40,\quad -8I_1+20I_2-6I_3=0,\quad -6I_2+10I_3=-20$$
5. Eliminate I1 and I3 from the center equation.

   $$I_1=4+0.8I_2,\quad I_3=0.6I_2-2,\quad 10I_2=20$$
6. The right mesh’s actual circulation is counterclockwise.

   $$I_1=5.6\,\mathrm{A},\quad I_2=2\,\mathrm{A},\quad I_3=-0.8\,\mathrm{A}$$
7. The 8 ohm branch current is 3.6 A downward, not I1 alone.

   $$v_o=8(I_1-I_2)=28.8\,\mathrm{V}$$
8. For absorbed power, use current entering the positive source terminal. Both negative results mean delivery: 224 W and 16 W, respectively.

   $$p_{40\mathrm{V}}=-40I_1=-224\,\mathrm{W},\qquad p_{20\mathrm{V}}=20I_3=-16\,\mathrm{W}$$

**Answer:** $p_{40\mathrm{V}}=-224\,\mathrm{W}$ and $p_{20\mathrm{V}}=-16\,\mathrm{W}$ (both deliver); $v_o=28.8\,\mathrm{V}$

### Mesh analysis with dependent sources

Express the controlling quantity using mesh currents before solving. A current through a shared resistor is a difference of mesh currents, so a source controlled by that current usually depends on two mesh unknowns. The control equation remains part of the system even if the dependent-source symbol lies in only one mesh.

**Example: Mesh currents with a dependent source (Lecture 3)**

Use mesh currents to find the power dissipated in the $4\,\Omega$ resistor.

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
```

1. Both lower meshes cross the 20 ohm resistor in opposite directions.

   $$i_\phi=I_a-I_c$$
2. KVL in the lower-left mesh.

   $$-50+5(I_a-I_b)+20(I_a-I_c)=0$$
3. KVL in the upper triangular mesh.

   $$1I_b+4(I_b-I_c)+5(I_b-I_a)=0$$
4. KVL in the lower-right mesh includes the controlled-source drop.

   $$15i_\phi+20(I_c-I_a)+4(I_c-I_b)=0$$
5. Substitute the control relation into the third equation.

   $$25I_a-5I_b-20I_c=50,\quad -5I_a+10I_b-4I_c=0,\quad -5I_a-4I_b+9I_c=0$$
6. Solve the second equation for Ib, substitute into the third, and then recover Ib in terms of Ia.

   $$I_b=\frac{5I_a+4I_c}{10},\qquad I_c=\frac{35}{37}I_a,\qquad I_b=\frac{65}{74}I_a$$
7. Substitution into the first equation gives (125/74)Ia=50. Recover the other mesh currents and the control current.

   $$I_a=29.6\,\mathrm{A},\quad I_b=26\,\mathrm{A},\quad I_c=28\,\mathrm{A},\quad i_\phi=1.6\,\mathrm{A}$$
8. The 4 ohm resistor’s physical current is the difference of the adjacent mesh currents.

   $$i_{b\to c}=I_c-I_b=2\,\mathrm{A},\qquad P_{4\Omega}=4(I_c-I_b)^2=16\,\mathrm{W}$$

**Answer:** $i_\phi=1.6\,\mathrm{A}$; $p_{4\Omega}=16\,\mathrm{W}$

The controlling current gives a source voltage of $(15\,\Omega)(1.6\,\mathrm{A})=24\,\mathrm{V}$. Algebra verifies the original dependent circuit; circuit_validate and circuit_simulate with a fixed $24\,\mathrm{V}$ replacement reproduce the currents and $16\,\mathrm{W}$ result. This checks the operating point’s consistency rather than simulating the dependency directly.

### Current sources and supermeshes

An ideal current source fixes current but leaves its voltage unknown. If it lies on the perimeter of one mesh, set that mesh current equal to the signed source current. If two meshes share it, combine their outer paths into a supermesh that bypasses the source branch. Write KVL around that combined path and add the source-current constraint.

$$I_a-I_b=I_s$$

The source current $I_s$ is positive in the shared-branch direction followed by mesh $a$, and opposed by mesh $b$. Reverse the sign if the arrow is reversed. A supermesh does not introduce a new independent current: $I_a$ and $I_b$ remain the unknowns.

**Example: A supermesh (Assessment AP 4.12)**

Use mesh currents, with a supermesh around the $2\,\mathrm{A}$ source, to find the power dissipated in the $1\,\Omega$ resistor.

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
```

1. The current source lies between the lower-left and upper meshes.

   $$I_a-I_b=2$$
2. KVL around their combined boundary avoids the current-source branch.

   $$-10+2I_b+2(I_b-I_c)+2(I_a-I_c)=0$$
3. KVL around the remaining right mesh.

   $$-6+I_c+2(I_c-I_a)+2(I_c-I_b)=0$$
4. The supermesh KVL, right-mesh KVL, and source constraint form a complete system.

   $$2I_a+4I_b-4I_c=10,\quad -2I_a-2I_b+5I_c=6,\quad I_a-I_b=2$$
5. Substitute the current constraint into both KVL equations and eliminate Ic.

   $$I_a=I_b+2,\qquad I_c=\frac{4I_b+10}{5},\qquad I_b=5\,\mathrm{A}$$
6. The 1 ohm resistor belongs only to the right mesh. The result agrees with the source’s official solution.

   $$I_a=7\,\mathrm{A},\quad I_b=5\,\mathrm{A},\quad I_c=6\,\mathrm{A},\quad P_{1\Omega}=I_c^2(1\,\Omega)=36\,\mathrm{W}$$

**Answer:** $i_a=7\,\mathrm{A}$, $i_b=5\,\mathrm{A}$, $i_c=6\,\mathrm{A}$; $p_{1\Omega}=36\,\mathrm{W}$

> **Warning:** A current source’s voltage is generally not zero. Do not write $RI$ for that voltage or drop its branch while forgetting the current constraint. If the source is dependent, add its control relation as well.

> **Tip:** On a current-source perimeter, read the mesh current directly from the arrow. On a shared current-source branch, write the current-difference constraint first, then trace the supermesh boundary.

## Practice problems

Try each problem before opening its solution. All node voltages use the stated ground, and all source powers use the passive sign convention (positive means absorbed). The textbook page images were inspected to transcribe the circuits; worked solutions below were derived independently. DC checks use circuit_validate and circuit_simulate. For the dependent source in P4.27, the simulation uses its solved voltage as a fixed source and the original control equation is checked separately.

**Problem: Textbook P4.1** (introductory)

For this circuit, find the number of:

1. branches;
2. branches whose current is unknown;
3. essential branches;
4. essential branches whose current is unknown;
5. nodes;
6. essential nodes;
7. meshes.

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
```

<details><summary>Solution</summary>

1. Count the elements: seven resistors and four sources give $b=11$ branches.
2. Only the independent $5\,\mathrm{mA}$ source has a prescribed current. The dependent current-source value is not known until its control voltage is known, so there are $10$ unknown branch currents.
3. The nodes are $0,a,b,c,d$. Each meets at least three elements, so $n=n_e=5$; no series-only node can be suppressed.
4. Every branch is essential: $b_e=11$, with $10$ unknown essential-branch currents.
5. For this connected planar circuit, $M=b-n+1=11-5+1=7$.

**Answer:** **Answers: (a) $11$; (b) $10$; (c) $11$; (d) $10$; (e) $5$; (f) $5$; (g) $7$.** These are dimensionless topology counts; no operating-point simulation is needed.

</details>

**Problem: Textbook P4.13** (introductory)

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
```

<details><summary>Solution</summary>

1. Choose nodal analysis because the two independent current sources enter KCL directly.
2. At $a$, $\dfrac{v_1}{125}+\dfrac{v_1-v_2}{25}=-2.4$. At $b$, $\dfrac{v_2}{250}+\dfrac{v_2}{375}+\dfrac{v_2-v_1}{25}=3.2$.
3. Multiply the first equation by $125$ and the second by $750$: $6v_1-5v_2=-300$ and $-30v_1+35v_2=2400$.
4. Multiply the first equation by $5$ and add: $10v_2=900$, so $v_2=90\,\mathrm{V}$. Back-substitution gives $6v_1=150$.
5. Check the connecting current: $\dfrac{25-90}{25}=-2.6\,\mathrm{A}$, so it flows toward $a$. The $3.2\,\mathrm{A}$ source delivers $288\,\mathrm{W}$; the $2.4\,\mathrm{A}$ source absorbs $60\,\mathrm{W}$; resistors absorb $228\,\mathrm{W}$. circuit_validate and circuit_simulate confirm the answers, KCL, and power balance.

**Answer:** **$v_1=25\,\mathrm{V}$ and $v_2=90\,\mathrm{V}$.**

</details>

**Problem: Assessment AP 4.10** (intermediate)

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
```

<details><summary>Solution</summary>

1. The perimeter source runs upward while clockwise $I_3$ runs downward on that branch. Thus $I_3=-16\,\mathrm{A}$; no supermesh is needed.
2. Left KVL: $-30+3I_1+2(I_1-I_2)+6I_1=0$, giving $11I_1-2I_2=30$.
3. Middle KVL: $8I_2+5(I_2-I_3)+4I_2+2(I_2-I_1)=0$, giving $-2I_1+19I_2=-80$.
4. Substitute $I_1=\dfrac{30+2I_2}{11}$ into the second equation: $205I_2=-820$. Hence $I_2=-4\,\mathrm{A}$ and $I_1=2\,\mathrm{A}$.
5. The downward $2\,\Omega$ current is $I_1-I_2=6\,\mathrm{A}$, so $P=(6\,\mathrm{A})^2(2\,\Omega)$.

**Answer:** **$P_{2\Omega}=72\,\mathrm{W}$.** The currents and power agree with the official solution. circuit_validate and circuit_simulate confirm this result and the KCL and power balances.

</details>

**Problem: Textbook P4.37** (intermediate)

1. Use the mesh-current method to find $i_a$, $i_b$ and $i_c$.
2. Repeat with the polarity of the $64\,\mathrm{V}$ source reversed.

```schematic
V1 0,3 -> 0,0 "$40\,\mathrm{V}$"
R1 0,3 -> 3,3 "$3\,\Omega$" i="$i_a$"
R2 0,0 -> 3,0 "$2\,\Omega$"
R3 3,3 -> 3,0 "$45\,\Omega$" i="$i_b$"
R4 6,3 -> 3,3 "$4\,\Omega$" i="$i_c$"
R5 3,0 -> 6,0 "$1.5\,\Omega$"
V2 6,0 -> 6,3 "$64\,\mathrm{V}$"
```

<details><summary>Solution</summary>

1. Choose clockwise mesh currents $I_L$ and $I_R$ in the left and right windows. Then $i_a=I_L$, $i_b=I_L-I_R$, and $i_c=-I_R$, since its arrow points leftward.
2. Left KVL gives $-40+(3+2)I_L+45(I_L-I_R)=0$, or $50I_L-45I_R=40$.
3. In part (a), clockwise traversal goes through the right source from negative to positive, so right KVL is $45(I_R-I_L)+(4+1.5)I_R-64=0$, or $-45I_L+50.5I_R=64$.
4. Substitute $I_L=\dfrac{40+45I_R}{50}$: $10I_R=100$. Thus $I_R=10\,\mathrm{A}$ and $I_L=9.8\,\mathrm{A}$.
5. In part (b), only the right equation’s source sign changes: $-45I_L+50.5I_R=-64$. Elimination gives $10I_R=-28$, so $I_R=-2.8\,\mathrm{A}$ and $I_L=-1.72\,\mathrm{A}$.

**Answer:** **(a) $i_a=9.8\,\mathrm{A}$, $i_b=-0.2\,\mathrm{A}$, $i_c=-10\,\mathrm{A}$.**

**(b) $i_a=-1.72\,\mathrm{A}$, $i_b=1.08\,\mathrm{A}$, $i_c=2.8\,\mathrm{A}$.** Negative answers indicate directions opposite the original labels. circuit_validate and circuit_simulate confirm both source-polarity cases and their KCL and power balances.

</details>

**Problem: Textbook P4.27** (intermediate)

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
ground 6,0
```

<details><summary>Solution</summary>

1. Treat $b$ and $c$ as a supernode, since an ideal voltage source connects them. Let their voltages be $v$ and $v_c$, and let $v_a$ denote node $a$’s voltage.
2. KCL at $a$: $\dfrac{v_a}{7.5}+\dfrac{v_a-v}{2.5}=4.8$, giving $v_a=9+0.75v$ when voltages are in volts.
3. Supernode KCL: $\dfrac{v-v_a}{2.5}+\dfrac{v}{10}+\dfrac{v_c}{2.5}+\dfrac{v_c-12}{1}=0$.
4. The controls are $i_x=\dfrac{v_a}{7.5}$ and $v_c-v=(1\,\Omega)i_x$. Hence, in SI numerical form, $v_c=v+\dfrac{v_a}{7.5}=1.1v+1.2$.
5. Substitution into boundary KCL gives $1.74v-13.92=0$.
6. Check the dependency: $v_c-v=2\,\mathrm{V}=(1\,\Omega)(2\,\mathrm{A})$. circuit_validate and circuit_simulate with a fixed $2\,\mathrm{V}$ replacement confirm the operating point and power balance. The dependent relation is verified algebraically because the simulator does not directly support controlled sources.

**Answer:** **$v=8\,\mathrm{V}$, with $v_a=15\,\mathrm{V}$, $v_c=10\,\mathrm{V}$, and $i_x=2\,\mathrm{A}$.**

</details>

**Problem: Week 4 tutorial, Problem 4 (review using node voltages)** (advanced)

Find $i_o$, $i_1$, $i_2$ and the power delivered by the current source. The tutorial uses a wye-to-delta transformation; solve it with node voltages and compare.

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
```

<details><summary>Solution</summary>

1. A bridge network is a good nodal exercise because it cannot be reduced immediately by series/parallel combinations. Define $v_a,v_b,v_c$ relative to ground.
2. KCL: $\dfrac{v_a}{240}+\dfrac{v_a-v_b}{20}+\dfrac{v_a-v_c}{320}=1$; $\dfrac{v_b}{100}+\dfrac{v_b-v_a}{20}+\dfrac{v_b-v_c}{50}=0$; $\dfrac{v_c}{600}+\dfrac{v_c-v_b}{50}+\dfrac{v_c-v_a}{320}=0$.
3. The second equation gives $v_b=(\dfrac{5}{8})v_a+(\dfrac{1}{4})v_c$. Substitute into the third to obtain $v_c=(\dfrac{15}{19})v_a$, hence $v_b=(\dfrac{125}{152})v_a$.
4. Substitution into the first equation gives $v_a=72.96\,\mathrm{V}$, $v_b=60\,\mathrm{V}$, and $v_c=57.6\,\mathrm{V}$.
5. Recover $i_o=\dfrac{v_c}{600}$, $i_1=\dfrac{v_a-v_c}{320}$, and $i_2=\dfrac{v_b}{100}$.
6. The source current enters its negative-voltage terminal, so absorbed power is $p_s=-v_a(1\,\mathrm{A})=-72.96\,\mathrm{W}$.

**Answer:** **$i_o=0.096\,\mathrm{A}$, $i_1=0.048\,\mathrm{A}$, and $i_2=0.6\,\mathrm{A}$.**

**The source delivers $72.96\,\mathrm{W}$.** These values agree with the tutorial’s official Y–Δ solution. circuit_validate and circuit_simulate confirm all currents, KCL, and total power balance.

</details>

**Problem: Lecture page 22: Shared current source** (advanced)

Use the mesh-current method to find the mesh currents $i_a$, $i_b$, $i_c$ (all clockwise) and the voltage $v$ across the current source.

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
```

<details><summary>Solution</summary>

1. The current source is shared by the left and right lower meshes. Its upward arrow gives $I_c-I_a=5$.
2. Upper-mesh KVL: $10I_b+2(I_b-I_c)+3(I_b-I_a)=0$, or $15I_b-3I_a-2I_c=0$.
3. Bypass the source using the lower supermesh contour: $-100+3(I_a-I_b)+2(I_c-I_b)+50+4I_c+6I_a=0$, or $9I_a+6I_c-5I_b=50$.
4. Substitute $I_c=I_a+5$ into the upper equation to get $I_a=3I_b-2$. The supermesh becomes $15I_a-5I_b=20$, so $40I_b=50$.
5. From the left side, $v_b=100-3(I_a-I_b)=98.5\,\mathrm{V}$. The $6\,\Omega$ resistor carries $I_a$ from $e$ to $f$, so $v_e=6I_a=10.5\,\mathrm{V}$. Therefore $v=v_b-v_e$.

**Answer:** **$I_a=1.75\,\mathrm{A}$, $I_b=1.25\,\mathrm{A}$, $I_c=6.75\,\mathrm{A}$.**

**$v=88\,\mathrm{V}$.** circuit_validate and circuit_simulate confirm these branch currents and voltages, with KCL and total power balance satisfied.

</details>

## Summary

- Identify electrical nodes before writing equations; ideal wires share one potential.
- Distinguish branches, essential branches, loops, and meshes. Mesh analysis requires a planar circuit.
- Node-voltage analysis uses KCL and resistor currents $\dfrac{v_k-v_j}{R}$; it works for planar and nonplanar circuits.
- A grounded voltage source sets a known node voltage. A floating voltage source requires a supernode and a voltage-difference constraint.
- Dependent sources need explicit control equations using the correct branch directions and units.
- Mesh analysis uses KVL. A shared resistor carries a difference of adjacent clockwise mesh currents.
- A perimeter current source fixes one mesh current; a shared source requires a supermesh and a current-difference constraint.
- Recover requested branch quantities and check source constraints, KCL, and power balance. Negative current reverses the arrow; negative absorbed power means delivery.

### Formula sheet

| Result | Formula | Use when |
|---|---|---|
| Resistor branch current | $i_{k\to j}=\dfrac{v_k-v_j}{R_{kj}}$ | Writing node-voltage equations or recovering currents. |
| Nodal KCL | $\sum_j\dfrac{v_k-v_j}{R_{kj}}=I_{k,\mathrm{in}}$ | Current injected by sources balances outgoing resistor currents. |
| Grounded voltage source | $v_p=V_s$ (positive at $p$) | The source’s negative terminal is the reference. |
| Supernode constraint | $v_p-v_q=V_s$ | The source is positive at $p$, negative at $q$; pair with boundary KCL. |
| Shared mesh resistor | $v_R=R(I_k-I_\ell)$ | Both adjacent mesh currents are clockwise; the drop follows mesh $k$. |
| Supermesh constraint | $I_a-I_b=I_s$ | The shared source arrow follows mesh $a$ on that branch. |
| Structural equation counts | $N_{\mathrm{KCL}}=n-1$, $M=b-n+1=b_e-n_e+1$ | A connected circuit; $M$ is the mesh count when planar. Source constraints reduce ordinary unknown-current equations. |
| Dependent-source controls | $v_s=r_m i_x$, $i_s=g_m v_x$ | $r_m$ has units $\Omega$; $g_m$ has units $\mathrm{S}$. Retain control polarity and direction. |
| Power and checks | $p=vi$, $P_R=i^2R=\dfrac{v_R^2}{R}$, $\sum p=0$ | Use current entering the positive-voltage terminal for absorbed power. |
