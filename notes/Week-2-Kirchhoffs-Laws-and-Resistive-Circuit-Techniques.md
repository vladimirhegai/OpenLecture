# Week 2: Kirchhoff’s Laws and Resistive Circuit Techniques

## Overview

> **Info:** Week 2 turns Week 1’s voltage, current, power, and Ohm’s law into tools for solving complete resistive circuits. Start with conservation laws, then use series/parallel reduction and dividers when the topology allows them; finish with measurement effects and delta–wye transformations for bridge networks.

### Learning outcomes

- Apply Kirchhoff’s current and voltage laws with consistent reference directions.
- Analyze circuits containing dependent sources and their controlling variables.
- Identify series and parallel connections and reduce resistive networks.
- Use voltage and current dividers, including loading and resistor tolerance.
- Explain voltage, current, and resistance measurements and balance a Wheatstone bridge.
- Use delta-to-wye (pi-to-tee) transformations to simplify three-terminal networks.

## Topic 1: Kirchhoff’s current and voltage laws

Ohm’s law relates a resistor’s voltage and current, but it does not tell you how currents split or how different element voltages fit together. Kirchhoff’s current law (KCL) enforces charge conservation at a node; Kirchhoff’s voltage law (KVL) enforces a consistent voltage change around a closed loop. Assume the lumped circuit model used in this course.

| Term | Meaning |
|---|---|
| Node | All points joined by ideal wire; they share one electric potential. |
| Branch | A path carrying an element current between circuit nodes. |
| Loop | A closed path used to sum voltage changes. |
| Reference direction / polarity | An assigned current arrow or voltage $+/-$ labeling. A negative answer reverses the assigned sense. |
| Reference node | The node assigned zero potential. Here it is called ground, $0$; it need not be Earth ground. |

$$\sum_{\text{entering}}i_k=\sum_{\text{leaving}}i_k,\qquad \sum_{\text{closed loop}}\Delta v_k=0$$

The index $k$ labels an element or branch, $i_k$ is its signed current, and $\Delta v_k$ is the voltage change during your chosen traversal. For KCL, use one convention throughout. For KVL, crossing from $-$ to $+$ gives a rise and from $+$ to $-$ gives a drop. With resistor current entering its labeled positive terminal, $v_k=R_k i_k$, where $R_k$ is resistance; with the opposite reference pairing, $v_k=-R_k i_k$.

**Example: Split currents and check power (Tutorial P2.19)**

Find $i_1$, $i_2$ and $v_o$, and check that the power balances.

```schematic
I1 0,0 -> 0,3 "$1.5\,\mathrm{A}$" v_rev="$v_o$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$100\,\Omega$" i="$i_1$"
R2 3,3 -> 6,3 "$150\,\Omega$" i="$i_2$"
R3 6,3 -> 6,0 "$250\,\Omega$"
wire 6,0 -> 0,0
```

1. The source injects current at $a$; its two exit paths are the $100\,\Omega$ branch and the series branch.

   $$i_1+i_2=1.5\,\mathrm A$$
2. Both paths connect the same endpoints, so their voltage drops are equal.

   $$100i_1=(150+250)i_2\quad\Longrightarrow\quad i_1=4i_2$$
3. Substitute into KCL, then recover the source voltage using Ohm’s law.

   $$5i_2=1.5\quad\Longrightarrow\quad i_2=0.3\,\mathrm A,\quad i_1=1.2\,\mathrm A,\quad v_o=100(1.2)=120\,\mathrm V$$
4. Resistors absorb power; source current enters its negative voltage terminal, so its absorbed power is negative.

   $$p_R=100(1.2)^2+150(0.3)^2+250(0.3)^2=180\,\mathrm W,\qquad p_s=-(120)(1.5)=-180\,\mathrm W$$
5. Verification: the official tutorial solution agrees. circuit_validate and circuit_simulate confirm the currents, voltage, KCL, and power balance.

   $$\boxed{i_1=1.2\,\mathrm A,\quad i_2=0.3\,\mathrm A,\quad v_o=120\,\mathrm V;\quad P_{\mathrm{delivered}}=180\,\mathrm W}$$

**Answer:** $i_1=1.2\,\mathrm{A}$, $i_2=0.3\,\mathrm{A}$, $v_o=120\,\mathrm{V}$; $180\,\mathrm{W}$ delivered $=180\,\mathrm{W}$ absorbed.

> **Warning:** A current arrow is a reference, not a prediction. Keep it fixed if the answer is negative. An ideal current source fixes current but leaves its voltage to the circuit; an ideal voltage source fixes voltage but leaves its current to the circuit.

> **Tip:** Label nodes, arrows, and polarities first. Write KCL at a current split and KVL through a useful loop; substitute Ohm’s law only after the signs are clear. Finally check $\sum p_k=0$, where $p_k$ is absorbed power under the passive sign convention.

## Topic 2: Analyzing circuits with dependent sources

A dependent source models a circuit whose output responds to another voltage or current. It is still an ideal source, so KCL and KVL apply unchanged; the extra requirement is its control equation. Solve the controller and the source together instead of guessing a source value.

- Identify the controlling current or voltage and keep its exact reference arrow or polarity.
- Write the source law; for example, $i_d=\beta i_\Delta$, where $i_d$ is source current, $i_\Delta$ is the controlling current, and $\beta$ is a dimensionless current gain.
- Write conservation and resistor equations, then substitute the control law to close the algebra.
- Check both conservation and the control law in the final result. A dependent source can absorb or deliver power.

**Example: A current-controlled current source (Lecture 2)**

Find $i_\Delta$, $i_o$ and $v_o$.

```schematic
V1 0,3 -> 0,0 "$500\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\Omega$" i="$i_\Delta$"
R2 3,3 -> 3,0 "$20\,\Omega$" i="$i_o$" v="$v_o$"
wire 3,3 -> 6,3
G1 6,0 -> 6,3 "$5i_\Delta$"
wire 6,0 -> 0,0
label 3,3 "$b$" above
```

1. The dependent source and the controlling branch both inject current into $b$.

   $$i_o=i_\Delta+5i_\Delta=6i_\Delta$$
2. Use the resistor law to express the output voltage in the same unknown.

   $$v_o=(20\,\Omega)i_o=(120\,\Omega)i_\Delta$$
3. KVL through the independent source and both resistors now contains one unknown.

   $$500-5i_\Delta-v_o=0\quad\Longrightarrow\quad 500=125i_\Delta$$
4. Recover all three requested quantities and check the control law.

   $$\boxed{i_\Delta=4\,\mathrm A,\quad i_o=24\,\mathrm A,\quad v_o=480\,\mathrm V};\qquad i_d=20\,\mathrm A=5(4\,\mathrm A)$$
5. Power is an independent sign check; the two sources together supply the resistor losses.

   $$p_{500}=-2000\,\mathrm W,\quad p_d=-9600\,\mathrm W,\quad p_{5}=80\,\mathrm W,\quad p_{20}=11520\,\mathrm W;\qquad \sum p=0$$
6. math_evaluate verifies the controlling-current equation. circuit_validate and circuit_simulate with the computed fixed $20\,\mathrm A$ source confirm this operating point; the simulator does not implement the dependency itself.

   $$i_o-i_\Delta-i_d=24-4-20=0\,\mathrm A$$

**Answer:** $i_\Delta=4\,\mathrm{A}$, $i_o=24\,\mathrm{A}$, $v_o=480\,\mathrm{V}$

> **Warning:** Do not treat a dependent source as an independent source while solving: its value changes with its controller. If a gain multiplies a voltage to give a current, the gain has units $\mathrm{A/V}$; multiplying a current to give a voltage requires $\mathrm{V/A}$.

> **Tip:** When the controller is a branch current, express the other currents and resistor voltages in terms of that one current. This often turns the problem into one KVL equation, as in the example.

## Topic 3: Series and parallel resistance

Reduction replaces a resistor network by one resistor with the same terminal voltage–current relationship. Series means a shared connection with no alternate current path; parallel means exactly the same two endpoint nodes. Decide from connectivity, even when a drawing makes the elements look different.

$$R_{\mathrm{series}}=\sum_{k=1}^{n}R_k,\qquad \frac{1}{R_{\mathrm{parallel}}}=\sum_{k=1}^{n}\frac{1}{R_k},\qquad R_1\parallel R_2=\frac{R_1R_2}{R_1+R_2}$$

Here $n$ is the number of resistors, $R_k$ is each resistance, and $R_{\mathrm{series}}$ or $R_{\mathrm{parallel}}$ is the equivalent resistance for that connection. The symbol $\parallel$ denotes a parallel combination. These formulas apply to resistor networks; they do not make unlike source connections interchangeable.

**Why the reduction formulas work**

1. Series resistors have the same physical current $i$; KVL adds their drops.

   $$v=\sum_{k=1}^{n}iR_k=i\sum_{k=1}^{n}R_k\quad\Longrightarrow\quad R_{\mathrm{series}}=v/i=\sum R_k$$
2. Parallel resistors have the same voltage $v$; KCL adds their currents.

   $$i=\sum_{k=1}^{n}\frac{v}{R_k}=v\sum_{k=1}^{n}\frac{1}{R_k}\quad\Longrightarrow\quad \frac{1}{R_{\mathrm{parallel}}}=\frac{i}{v}=\sum\frac{1}{R_k}$$

**Example: Reduce, then work back to each branch (Lecture 2)**

Find the equivalent resistance seen by the source, then $i_s$, $i_1$ and $i_2$.

```schematic
V1 0,3 -> 0,0 "$120\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$" i="$i_s$"
R2 3,3 -> 3,0 "$18\,\Omega$" i="$i_1$"
R3 3,3 -> 6,3 "$3\,\Omega$"
R4 6,3 -> 6,0 "$6\,\Omega$" i="$i_2$"
wire 6,0 -> 0,0
label 3,3 "$x$" above
label 6,3 "$a$" above
```

1. Node $a$ joins only two resistor elements, so combine that series path first.

   $$R_{36}=3+6=9\,\Omega$$
2. The entire series path shares $x$ and $0$ with the $18\,\Omega$ branch.

   $$R_{x0}=18\parallel9=\frac{18(9)}{18+9}=6\,\Omega;\qquad R_{\mathrm{in}}=4+6=10\,\Omega$$
3. The reduced network gives source current; restore the voltage at the split.

   $$i_s=\frac{120}{10}=12\,\mathrm A,\qquad V_x=i_sR_{x0}=72\,\mathrm V$$
4. Use each complete branch resistance to find its current.

   $$\boxed{i_1=72/18=4\,\mathrm A,\quad i_2=72/9=8\,\mathrm A,\quad R_{\mathrm{in}}=10\,\Omega};\quad i_1+i_2=i_s$$
5. circuit_validate and circuit_simulate confirm these results. The source power equals the sum of all resistor powers.

   $$P_s=120(12)=1440\,\mathrm W=4(12)^2+18(4)^2+3(8)^2+6(8)^2$$

**Answer:** $R_{eq}=10\,\Omega$, $i_s=12\,\mathrm{A}$, $i_1=4\,\mathrm{A}$, $i_2=8\,\mathrm{A}$

> **Warning:** Sharing one node does not prove series connection if another branch also touches that node. Sharing one endpoint does not prove parallel connection. Also, series currents can have opposite algebraic signs when their reference arrows point in opposite senses.

> **Tip:** For at least two finite positive resistors, a series equivalent exceeds the largest resistance, and a parallel equivalent is below the smallest. Reduce from an obvious inner pair, redraw after each step, and preserve enough labels to recover the requested original currents.

## Topic 4: Voltage and current dividers

Dividers are shortcuts for distributing a known total voltage along a series path or a known total current among parallel branches. The topology is the reason the formulas work: series elements share current, while parallel elements share voltage. Use the voltage or current actually applied to the selected subnetwork.

$$v_j=v\frac{R_j}{R_{\mathrm{eq}}},\qquad R_{\mathrm{eq}}=\sum_{k=1}^{n}R_k$$

For voltage division, $v$ is the voltage across the entire series chain, $v_j$ is the drop across resistor $R_j$, $j$ selects that resistor, and $R_{\mathrm{eq}}$ is the total series resistance. Drops are referenced in the common current direction. In a two-resistor divider with source voltage $v_s$ and output across $R_2$, $v_o=\dfrac{v_sR_2}{R_1+R_2}$ when no load draws current from the junction.

$$i_j=i\frac{R_{\mathrm{eq}}}{R_j}=i\frac{G_j}{\sum_{k=1}^{n}G_k},\qquad G_j=\frac{1}{R_j};\qquad i_1=i\frac{R_2}{R_1+R_2},\quad i_2=i\frac{R_1}{R_1+R_2}$$

For current division, $i$ is the total current entering the parallel network, $i_j$ flows through branch resistance $R_j$, $G_j$ is its conductance, and $R_{\mathrm{eq}}$ is the parallel equivalent. All branch currents use the same endpoint direction. The last two formulas apply only to two branches. Lower resistance takes more current: the two-branch numerator contains the other branch’s resistance.

**Derive both divider rules from Ohm’s law**

1. In a series chain, KVL gives the common current; each voltage is that current times its own resistance.

   $$v=iR_{\mathrm{eq}}\quad\Longrightarrow\quad i=\frac{v}{R_{\mathrm{eq}}}\quad\Longrightarrow\quad v_j=iR_j=v\frac{R_j}{R_{\mathrm{eq}}}$$
2. In a parallel network, the common voltage is total current times the equivalent resistance; each branch current is that voltage divided by its resistance.

   $$v=iR_{\mathrm{eq}}\quad\Longrightarrow\quad i_j=\frac{v}{R_j}=i\frac{R_{\mathrm{eq}}}{R_j}$$

$$R_{\mathrm{low}}=R_2\parallel R_L,\qquad v_o=v_s\frac{R_{\mathrm{low}}}{R_1+R_{\mathrm{low}}},\qquad P_{\mathrm{unloaded}}=\frac{v_s^2}{R_1+R_2}$$

Here $R_L$ is the load resistance connected across $R_2$, and $R_{\mathrm{low}}$ is the lower branch equivalent. $P_{\mathrm{unloaded}}$ is the positive power supplied by the source and dissipated by the unloaded divider; the source’s absorbed power is its negative. A finite positive load lowers $R_{\mathrm{low}}$ and therefore lowers $v_o$. Increasing both divider resistances at a fixed ratio reduces unloaded power, but also makes a fixed load more significant. The lecture’s sufficient loading guideline is $R_L\gg R_2$.

**Example: Worst-case divider tolerance (Lecture 2)**

Both resistors have a $\pm10\%$ tolerance. Find the nominal, maximum and minimum no-load output $v_o$.

```schematic
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
R1 0,3 -> 3,3 "$25\,\mathrm{k\Omega}$"
R2 3,3 -> 3,0 "$100\,\mathrm{k\Omega}$"
wire 3,3 -> 5,3
wire 3,0 -> 5,0
wire 3,0 -> 0,0
terminal 5,3
terminal 5,0
gap 5,3 -> 5,0 v="$v_o$"
```

1. Nominal voltage division gives the baseline. The ratio grows as the lower resistor grows or the upper resistor shrinks.

   $$v_{o,\mathrm{nom}}=100\frac{100}{25+100}=80\,\mathrm V$$
2. Maximum output uses the smallest upper resistor and largest lower resistor; resistance numbers below are in kilohms.

   $$R_{1,\min}=22.5\,\mathrm{k}\Omega,\quad R_{2,\max}=110\,\mathrm{k}\Omega;\quad v_{o,\max}=100\frac{110}{22.5+110}\approx83.02\,\mathrm V$$
3. Minimum output uses the largest upper resistor and smallest lower resistor.

   $$R_{1,\max}=27.5\,\mathrm{k}\Omega,\quad R_{2,\min}=90\,\mathrm{k}\Omega;\quad v_{o,\min}=100\frac{90}{27.5+90}\approx76.60\,\mathrm V$$
4. math_evaluate checks the arithmetic, and validated DC simulations confirm the nominal and both extreme circuits.

   $$\boxed{76.60\,\mathrm V\lesssim v_o\lesssim83.02\,\mathrm V,\qquad v_{o,\mathrm{nom}}=80\,\mathrm V}$$

**Answer:** $v_o=80\,\mathrm{V}$ nominal; $76.60\,\mathrm{V}\le v_o\le83.02\,\mathrm{V}$

**Example: Two current divisions in a row (Lecture 2)**

Find the power dissipated in the $6\,\Omega$ resistor.

```schematic
I1 0,0 -> 0,3 "$10\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$16\,\Omega$"
R2 3,3 -> 6,3 "$1.6\,\Omega$" i="$i_B$"
R3 6,3 -> 6,0 "$4\,\Omega$"
wire 6,3 -> 9,3
R4 9,3 -> 9,0 "$6\,\Omega$" i="$i_6$"
wire 9,0 -> 0,0
```

1. The $4\,\Omega$ and $6\,\Omega$ pair is parallel. Its equivalent is in series with $1.6\,\Omega$.

   $$R_{c0}=4\parallel6=2.4\,\Omega,\qquad R_B=1.6+2.4=4\,\Omega$$
2. The full $4\,\Omega$ branch divides the source current with the $16\,\Omega$ branch.

   $$i_B=10\frac{16}{16+4}=8\,\mathrm A$$
3. Divide that branch current, not the original source current, between the $4\,\Omega$ and $6\,\Omega$ resistors.

   $$i_6=8\frac{4}{4+6}=3.2\,\mathrm A$$
4. Use resistor power and compare with the validated operating-point simulation.

   $$\boxed{p_6=R_6i_6^2=6(3.2)^2=61.44\,\mathrm W}$$

**Answer:** $i_6=3.2\,\mathrm{A}$, $p_{6\Omega}=61.44\,\mathrm{W}$

> **Warning:** Do not apply the unloaded divider formula after attaching a load: $R_1$ and $R_2$ then carry different currents. Do not feed the original source current into a divider nested inside another branch. A resistor’s tolerance does not translate directly to the same percentage tolerance in output voltage.

> **Tip:** Voltage division favors larger resistance in series; current division favors smaller resistance in parallel. Reduce each complete branch first, then apply the shortcut. For worst-case output across the lower resistor, pair its maximum with the upper resistor’s minimum, and reverse those extremes for the minimum.

## Topic 5: Measurement and the Wheatstone bridge

A meter must connect to the variable it measures: an ammeter goes in series to carry the branch current, and a voltmeter goes in parallel to compare the two endpoint potentials. An ideal ammeter has zero resistance and behaves as a short; an ideal voltmeter has infinite resistance and behaves as an open. Real meters alter the circuit because their resistances are finite. An analog d’Arsonval movement responds to its coil current; shunt and series resistors extend its measurement range.

```schematic
V1 0,3 -> 0,0 "$v_s$"
R1 0,3 -> 3,3 "$R_1$"
AM1 3,3 -> 6,3
R2 6,3 -> 6,0 "$R_2$"
wire 6,3 -> 9,3
VM1 9,3 -> 9,0
wire 9,0 -> 0,0
```

| Meter | How it works | Effect on the circuit |
|---|---|---|
| Ideal ammeter | Measures the current through it; placed in series. | A short circuit ($0\,\Omega$): no effect. |
| Ideal voltmeter | Measures the voltage across it; placed in parallel. | An open circuit ($\infty\,\Omega$): no effect. |
| Digital meter | Samples the voltage or current at discrete times (sampling times). The usual meter in the lab. | Very high input resistance as a voltmeter, so loading is usually small. |
| Analog meter | A d'Arsonval movement: current in a movable coil in a permanent magnet's field turns a pointer against a restoring spring. | Finite resistance: a shunt $R_A$ (ammeter) or series $R_v$ (voltmeter) sets the range and loads the circuit. |

> **Tip:** **Ammeter rule of thumb (Lecture 2):** an ammeter's effective resistance should be no more than $\dfrac{1}{10}$ of the smallest resistance in the circuit. For example, the $5\,\Omega$ ammeter designed below suits circuits whose resistors are all $50\,\Omega$ or more. In Assessment AP 3.5 it is inserted in series with $100\,\Omega$ and reads $9.52\,\mathrm{mA}$ instead of $10\,\mathrm{mA}$, about a 5% error.

$$R_m=\frac{V_m}{I_m},\qquad R_A=\frac{V_m}{I_{\mathrm{FS}}-I_m},\qquad R_v=\frac{V_{\mathrm{FS}}}{I_m}-R_m$$

$R_m$ is the movement resistance, and $V_m$ and $I_m$ are its full-scale voltage and current. $R_A$ is the parallel shunt for an ammeter with desired total full-scale current $I_{\mathrm{FS}}>I_m$; its total input resistance is $R_m\parallel R_A$. $R_v$ is the series resistor for a voltmeter with desired full-scale terminal voltage $V_{\mathrm{FS}}\ge V_m$; its input resistance is $R_m+R_v$. These formulas protect the movement at full scale. Low ammeter resistance and high voltmeter resistance reduce measurement disturbance.

**Example: Designing an ammeter and a voltmeter (Lecture 2)**

A d'Arsonval movement ($R_m$) reads full scale at $50\,\mathrm{mV}$ and $1\,\mathrm{mA}$.

1. Find the shunt $R_A$ for a $10\,\mathrm{mA}$ full-scale ammeter (left).
2. Find the series resistor $R_v$ for a $150\,\mathrm{V}$ full-scale voltmeter (right).

```schematic
terminal 0,3 "$u$" left
terminal 0,0 left
wire 0,3 -> 4,3
wire 0,0 -> 4,0
R1 2,3 -> 2,0 "$R_m$"
R2 4,3 -> 4,0 "$R_A$"
terminal 7,3 "$u$" left
terminal 7,0 left
R3 7,3 -> 10,3 "$R_v$"
R4 10,3 -> 10,0 "$R_m$"
wire 10,0 -> 7,0
```

1. Convert milliunits before calculating the movement resistance.

   $$R_m=\frac{0.050}{0.001}=50\,\Omega$$
2. At ammeter full scale the movement carries its rated current, so KCL puts the remaining current through the shunt; both have the same voltage.

   $$i_A=0.010-0.001=0.009\,\mathrm A,\qquad R_A=\frac{0.050}{0.009}=\frac{50}{9}\,\Omega\approx5.556\,\Omega$$
3. The parallel equivalent is the resistance that this ammeter inserts into the measured branch.

   $$R_{\mathrm{ammeter}}=50\parallel(50/9)=5\,\Omega$$
4. For the voltmeter, full-scale terminal voltage drives the rated movement current through both series resistances.

   $$150=0.001(R_v+50)\quad\Longrightarrow\quad R_v=149950\,\Omega=149.95\,\mathrm{k}\Omega$$
5. Validated DC simulations give the rated movement voltage and current in both configurations. The voltmeter terminal resistance includes the movement.

   $$\boxed{R_A\approx5.556\,\Omega,\quad R_v=149.95\,\mathrm{k}\Omega,\quad R_{\mathrm{voltmeter}}=150\,\mathrm{k}\Omega}$$

**Answer:** $R_A=\dfrac{50}{9}\approx5.556\,\Omega$ (ammeter resistance $5\,\Omega$); $R_v=149.95\,\mathrm{k}\Omega$ (voltmeter resistance $150\,\mathrm{k}\Omega$)

**Example: A voltmeter loads a divider (Assessment AP 3.6)**

Find $v$ before the meter is connected. Then find the reading of the $150\,\mathrm{V}$ voltmeter designed above (internal resistance $150\,\mathrm{k}\Omega$).

```schematic
V1 0,3 -> 0,0 "$60\,\mathrm{V}$"
R1 0,3 -> 3,3 "$15\,\mathrm{k\Omega}$"
R2 3,3 -> 3,0 "$75\,\mathrm{k\Omega}$" v="$v$"
wire 3,3 -> 6,3
VM1 6,3 -> 6,0
wire 6,0 -> 0,0
```

1. Before connection, the two resistors form an unloaded series divider.

   $$v=60\frac{75}{15+75}=50\,\mathrm V$$
2. After connection, combine the lower resistor with the total voltmeter input resistance, not just the movement resistance.

   $$R_{\mathrm{low}}=75\,\mathrm{k}\Omega\parallel150\,\mathrm{k}\Omega=50\,\mathrm{k}\Omega$$
3. Apply voltage division to the modified circuit. This matches the official solution and both validated DC simulations.

   $$\boxed{v_{\mathrm{read}}=60\frac{50}{15+50}=\frac{600}{13}\,\mathrm V\approx46.15\,\mathrm V};\qquad v_{\mathrm{unmeasured}}=50\,\mathrm V$$

**Answer:** $v=50\,\mathrm{V}$; the voltmeter reads $46.15\,\mathrm{V}$.

$$i_g=0\ \Longrightarrow\ V_b=V_c,\qquad R_1R_x=R_2R_3,\qquad R_x=\frac{R_2}{R_1}R_3$$

A Wheatstone bridge measures an unknown resistance by finding a null. Use source top node $a$, ground $0$, left midpoint $b$, and right midpoint $c$: $R_1$ connects $a$–$b$, $R_3$ connects $b$–$0$, $R_2$ connects $a$–$c$, and the unknown $R_x$ connects $c$–$0$. The galvanometer between $b$ and $c$ carries current $i_g$. For an energized bridge with positive resistances and a working detector, zero detector current means equal midpoint potentials. Adjust the known variable $R_3$ until that happens.

**Derive the balance condition with two dividers**

1. At balance no current leaves either midpoint through the detector, so each side is a series divider driven by the same supply $v_s$.

   $$V_b=v_s\frac{R_3}{R_1+R_3},\qquad V_c=v_s\frac{R_x}{R_2+R_x}$$
2. Set the midpoint voltages equal and cancel the nonzero supply.

   $$\frac{R_3}{R_1+R_3}=\frac{R_x}{R_2+R_x}\quad\Longrightarrow\quad R_3(R_2+R_x)=R_x(R_1+R_3)$$
3. Cancel the common product and solve for the unknown resistance.

   $$R_2R_3=R_1R_x\quad\Longrightarrow\quad R_x=\frac{R_2R_3}{R_1}$$

**Example: Balanced bridge and resistor ratings (Assessment AP 3.7)**

The bridge is balanced (no galvanometer current). Find $R_x$, and check whether any resistor exceeds a $250\,\mathrm{mW}$ rating.

```schematic
V1 0,6 -> 0,0 "$5\,\mathrm{V}$"
wire 0,6 -> 6,6
R1 3,6 -> 3,3 "$100\,\Omega$"
R3 3,3 -> 3,0 "$150\,\Omega$"
R2 6,6 -> 6,3 "$1\,\mathrm{k\Omega}$"
R4 6,3 -> 6,0 "$R_x$"
AM1 3,3 -> 6,3 "galvanometer"
wire 6,0 -> 0,0
```

1. The balance ratio determines the unknown without needing a detector resistance.

   $$R_x=\frac{1000(150)}{100}=1500\,\Omega$$
2. No detector current flows, so calculate one current for each series side.

   $$i_{\mathrm{left}}=\frac{5}{100+150}=20\,\mathrm{mA},\qquad i_{\mathrm{right}}=\frac{5}{1000+1500}=2\,\mathrm{mA}$$
3. Each resistor’s power uses its own resistance and branch current.

   $$p_{R_1}=100(0.020)^2=40\,\mathrm{mW},\quad p_{R_3}=150(0.020)^2=60\,\mathrm{mW},\quad p_{R_2}=1000(0.002)^2=4\,\mathrm{mW},\quad p_{R_x}=1500(0.002)^2=6\,\mathrm{mW}$$
4. The largest loss is below the rating. A validated simulation using an arbitrary finite $1\,\mathrm{k}\Omega$ detector confirms equal midpoints and zero detector current; this is a verification model, not a specified detector value.

   $$\boxed{R_x=1.5\,\mathrm{k}\Omega;\quad \max p_R=60\,\mathrm{mW}<250\,\mathrm{mW}\ \text{(ratings satisfied)}};\qquad V_b=V_c=3\,\mathrm V$$

**Answer:** $R_x=1.5\,\mathrm{k}\Omega$; the largest dissipation is $60\,\mathrm{mW}$, so every resistor is within its rating.

> **Warning:** Connecting an ammeter across an element adds a low-resistance bypass. A voltmeter in series adds a large resistance and changes the current. For a bridge, use the ratio corresponding to your actual node labels; the balance formula applies only at the null, not to an arbitrary unbalanced network.

> **Tip:** Include the meter’s terminal resistance in the circuit before calculating its reading. For accuracy, calculate the actual disturbance. For a bridge at balance, set detector current to zero and analyze the two sides as independent series paths.

## Topic 6: Delta-to-wye (pi-to-tee) transformations

A bridge can prevent direct series/parallel reduction because each tempting junction has an extra branch. A delta–wye transformation replaces a three-terminal resistor network by another with the same external terminal behavior. A delta ($\Delta$, also drawn as a pi) has one resistor between each pair of terminals; a wye (Y, also drawn as a tee) has one arm from each terminal to a new internal center. Preserve the three terminal identities when you redraw.

$$S=R_a+R_b+R_c,\qquad R_1=\frac{R_bR_c}{S},\qquad R_2=\frac{R_cR_a}{S},\qquad R_3=\frac{R_aR_b}{S}$$

Use the lecture’s labeling: delta resistance $R_a$ connects $b$–$c$, $R_b$ connects $c$–$a$, and $R_c$ connects $a$–$b$. Thus each delta subscript identifies the opposite terminal. $S$ is the sum of the three delta resistances. In the equivalent wye, $R_1$ joins terminal $a$ to center $n$, $R_2$ joins $b$ to $n$, and $R_3$ joins $c$ to $n$. Each wye arm is the product of the two delta resistances touching its terminal divided by $S$.

**Match the resistance between every terminal pair**

1. Disconnect the external connection at terminal $c$. The delta has a direct $a$–$b$ branch in parallel with a two-resistor path; the wye has two arms in series.

   $$R_{ab}=R_c\parallel(R_a+R_b)=\frac{R_c(R_a+R_b)}{S}=R_1+R_2$$
2. Repeat with the other external terminals open. Here $R_{ab}$, $R_{bc}$, and $R_{ca}$ mean measured pair resistances, not individual delta resistors.

   $$R_{bc}=\frac{R_a(R_b+R_c)}{S}=R_2+R_3,\qquad R_{ca}=\frac{R_b(R_c+R_a)}{S}=R_1+R_3$$
3. Add the first and third pair equations and subtract the second to isolate the arm at $a$.

   $$2R_1=R_{ab}+R_{ca}-R_{bc}=\frac{2R_bR_c}{S}\quad\Longrightarrow\quad R_1=\frac{R_bR_c}{S}$$
4. Cyclic relabeling gives the other two arms.

   $$R_2=\frac{R_cR_a}{S},\qquad R_3=\frac{R_aR_b}{S}$$
5. For the inverse, form the sum $Q$ of all wye pair products and use the forward equations. Dividing $Q$ by the opposite wye arm recovers a delta resistance.

   $$Q=R_1R_2+R_2R_3+R_3R_1=\frac{R_aR_bR_c}{S},\qquad \frac{Q}{R_1}=R_a$$

$$Q=R_1R_2+R_2R_3+R_3R_1,\qquad R_a=\frac{Q}{R_1},\qquad R_b=\frac{Q}{R_2},\qquad R_c=\frac{Q}{R_3}$$

$Q$ is the sum of the three pairwise products of wye resistances, with units $\Omega^2$. The inverse formulas give each delta resistance in ohms. Divide by the wye arm connected to the terminal opposite the desired delta resistor. These forms assume finite positive resistances. The center $n$ belongs only to the transformed network; do not attach an external circuit element to it.

**Example: Simplify a bridge with a delta-to-wye transformation (Lecture 2)**

Find the current and the power supplied by the $40\,\mathrm{V}$ source.

```schematic
V1 0,6 -> 0,0 "$40\,\mathrm{V}$" i_rev="$i_s$" flip
R1 0,6 -> 5,6 "$5\,\Omega$"
R2 5,6 -> 3,3 "$100\,\Omega$"
R3 5,6 -> 7,3 "$125\,\Omega$"
R4 3,3 -> 7,3 "$25\,\Omega$"
R5 3,3 -> 5,0 "$40\,\Omega$" flip
R6 7,3 -> 5,0 "$37.5\,\Omega$"
wire 5,0 -> 0,0
label 5,6 "$a$" above
label 3,3 "$b$" left
label 7,3 "$c$" right
```

1. For the upper delta, use the opposite-terminal labeling and sum its resistances.

   $$R_a=25\,\Omega,\quad R_b=125\,\Omega,\quad R_c=100\,\Omega,\quad S=250\,\Omega$$
2. Replace that triangle by three arms to a new center $n$.

   $$R_1=\frac{125(100)}{250}=50\,\Omega,\quad R_2=\frac{100(25)}{250}=10\,\Omega,\quad R_3=\frac{25(125)}{250}=12.5\,\Omega$$
3. The two paths from $n$ to ground now have no intervening branches at $b$ or $c$, so each is a series pair.

   $$R_{n0}=(10+40)\parallel(12.5+37.5)=50\parallel50=25\,\Omega$$
4. Include the source-side resistor and the arm at terminal $a$.

   $$R_{\mathrm{in}}=5+50+25=80\,\Omega$$
5. Use Ohm’s law and the source delivery convention. math_evaluate and a validated simulation of the original bridge confirm the answer.

   $$\boxed{i_s=\frac{40}{80}=0.5\,\mathrm A,\qquad P_{\mathrm{supplied}}=40(0.5)=20\,\mathrm W};\qquad p_{\mathrm{source,absorbed}}=-20\,\mathrm W$$

**Answer:** $i_s=0.5\,\mathrm{A}$; the source supplies $20\,\mathrm{W}$.

> **Warning:** The most common error is dividing by the wrong wye arm or multiplying delta resistors that do not touch the desired terminal. A transformation preserves behavior at its three external terminals, not the individual internal branch currents or resistor powers. Restore the original circuit to calculate an original resistor’s current or power.

> **Tip:** Choose a triangle or three-arm junction whose replacement creates clear series/parallel pairs. Label all three external terminals before transforming. Checking the resistance between each pair with the third terminal externally open is a useful equivalence check.

## Practice problems

**Problem: Textbook P2.17** (introductory)

Find $i_a$, $i_b$ and $v_b$, the power dissipated in each resistor, and the power delivered by the $80\,\mathrm{V}$ source.

```schematic
V1 0,3 -> 0,0 "$80\,\mathrm{V}$"
R1 0,3 -> 3,3 "$10\,\Omega$"
R2 3,3 -> 3,0 "$10\,\Omega$" i="$i_a$"
wire 3,3 -> 6,3
R3 6,3 -> 6,0 "$15\,\Omega$" i="$i_b$" v="$v_b$" flip
wire 6,0 -> 0,0
label 3,3 "$x$" above
```

<details><summary>Solution</summary>

1. Call the top-middle node $x$ and its voltage $v_x$ (bottom node is the reference). KCL at $x$: the current through the series $10\,\Omega$ resistor splits into $i_a$ and $i_b$.

   $$\frac{80-v_x}{10}=\frac{v_x}{10}+\frac{v_x}{15}$$
2. Multiply by 30 and solve.

   $$240-3v_x=3v_x+2v_x\ \Rightarrow\ v_x=30\,\mathrm{V}$$
3. Both right-hand resistors have $v_x$ across them.

   $$i_a=\frac{30}{10}=3\,\mathrm{A},\qquad i_b=\frac{30}{15}=2\,\mathrm{A},\qquad v_b=30\,\mathrm{V}$$
4. The source current is $i_a+i_b=5\,\mathrm{A}$. Resistor powers use $p=i^2R$.

   $$p_{10,\text{series}}=5^2(10)=250\,\mathrm{W},\quad p_{10,\text{shunt}}=3^2(10)=90\,\mathrm{W},\quad p_{15}=2^2(15)=60\,\mathrm{W}$$
5. Check: the source delivers $80\times5$, which equals the total dissipation.

   $$P_{80\,\mathrm{V}}=80(5)=400\,\mathrm{W}=250+90+60$$

**Answer:** **(a)** $i_a=3\,\mathrm{A}$ **(b)** $i_b=2\,\mathrm{A}$ **(c)** $v_b=30\,\mathrm{V}$ **(d)** $250\,\mathrm{W}$, $90\,\mathrm{W}$, $60\,\mathrm{W}$ **(e)** $400\,\mathrm{W}$

</details>

**Problem: Textbook P3.19** (introductory)

Find the power dissipated in the $1.2\,\mathrm{k}\Omega$ resistor.

```schematic
I1 0,0 -> 0,3 "$320\,\mathrm{mA}$"
wire 0,3 -> 9,3
R1 3,3 -> 3,0 "$800\,\Omega$"
R2 6,3 -> 6,0 "$2.4\,\mathrm{k\Omega}$"
R3 9,3 -> 9,0 "$1.2\,\mathrm{k\Omega}$"
wire 9,0 -> 0,0
```

<details><summary>Solution</summary>

1. All three resistors share the same endpoint pair, so use general current division. Convert the source current to $i_s=0.320\,\mathrm A$ and resistances to ohms. The parallel equivalent is $R_{\mathrm{eq}}=(\dfrac{1}{800}+\dfrac{1}{2400}+\dfrac{1}{1200})^{-1}=400\,\Omega$.
2. The selected branch takes $i_{1200}=\dfrac{i_sR_{\mathrm{eq}}}{1200}=\dfrac{0.320(400)}{1200}=0.106666\ldots\,\mathrm A$. The common voltage is $v=i_sR_{\mathrm{eq}}=128\,\mathrm V$.
3. Compute power using the unrounded current or common voltage: $p_{1200}=\dfrac{v^2}{1200}=\dfrac{128^2}{1200}=\dfrac{1024}{75}\,\mathrm W$. Therefore **$p_{1.2\,\mathrm{k}\Omega}\approx13.65\,\mathrm W$**. Verification: math_evaluate checks the arithmetic; circuit_validate and circuit_simulate confirm the voltage, selected branch current, KCL, and power balance.

**Answer:** 

</details>

**Problem: Assessment 3.1** (intermediate)

Find:

1. the voltage $v$;
2. the power delivered by the current source;
3. the power dissipated in the $10\,\Omega$ resistor.

```schematic
I1 0,0 -> 0,3 "$5\,\mathrm{A}$" v_rev="$v$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$30\,\Omega$"
R2 3,3 -> 6,3 "$7.2\,\Omega$"
R3 6,3 -> 6,0 "$64\,\Omega$"
R4 6,3 -> 9,3 "$6\,\Omega$"
R5 9,3 -> 9,0 "$10\,\Omega$"
wire 9,0 -> 0,0
```

<details><summary>Solution</summary>

1. Reduce from the far end, because the $6\,\Omega$ and $10\,\Omega$ resistors form a series path: $R_{6,10}=16\,\Omega$. This path is parallel with $64\,\Omega$, giving $R_{b0}=16\parallel64=12.8\,\Omega$. Add the $7.2\,\Omega$ resistor to obtain $20\,\Omega$, then combine with the $30\,\Omega$ branch: $R_{\mathrm{in}}=20\parallel30=12\,\Omega$.
2. The source drives this equivalent resistance, so **$v=5(12)=60\,\mathrm V$**. Its current enters the negative voltage terminal, giving absorbed power $p_s=-60(5)=-300\,\mathrm W$; it therefore **delivers $300\,\mathrm W$**.
3. Restore the original circuit. The $30\,\Omega$ current is $\dfrac{60}{30}=2\,\mathrm A$, leaving $5-2=3\,\mathrm A$ through $7.2\,\Omega$. The remaining branch voltage is $V_b=60-7.2(3)=38.4\,\mathrm V$. The $6+10\,\Omega$ path current is $i_{10}=\dfrac{38.4}{16}=2.4\,\mathrm A$.
4. The requested resistor power is **$p_{10}=10(2.4)^2=57.6\,\mathrm W$**. The remaining $64\,\Omega$ current is $\dfrac{38.4}{64}=0.6\,\mathrm A$, checking $3=2.4+0.6\,\mathrm A$ at $b$. Verification: the official assessment solution follows the same reduction and restoration. math_evaluate, circuit_validate, and circuit_simulate confirm $v$, source power, and resistor power; the sum of resistor powers equals source delivery.

**Answer:** 

</details>

**Problem: Textbook P3.12** (intermediate)

With no load, $v_o=25\,\mathrm{V}$. When the load $R_L$ is connected across $a$–$b$, $v_o$ drops to $15\,\mathrm{V}$. Find $R_L$.

```schematic
V1 0,3 -> 0,0 "$75\,\mathrm{V}$"
R1 0,3 -> 3,3 "$100\,\Omega$"
R2 3,3 -> 3,0 "$R_2$" v="$v_o$" flip
wire 3,3 -> 5,3
wire 3,0 -> 5,0
wire 3,0 -> 0,0
terminal 5,3 "a" right
terminal 5,0 "b" right
terminal 8,3
R3 8,3 -> 8,0 "$R_L$"
terminal 8,0
```

<details><summary>Solution</summary>

1. First determine the divider’s lower resistor from the unloaded condition. Voltage division gives $25=\dfrac{75R_2}{100+R_2}$. Cross-multiply: $25(100+R_2)=75R_2$, so $2500=50R_2$ and $R_2=50\,\Omega$.
2. Let $R_p=R_2\parallel R_L$ be the lower equivalent after loading. The loaded condition gives $15=\dfrac{75R_p}{100+R_p}$. Therefore $1500+15R_p=75R_p$, so $R_p=25\,\Omega$.
3. Recover the load from the parallel relationship: $\dfrac{1}{R_L}=\dfrac{1}{R_p}-\dfrac{1}{R_2}=\dfrac{1}{25}-\dfrac{1}{50}=\dfrac{1}{50}$. Thus **$R_L=50\,\Omega$**. It is positive and finite, consistent with output decreasing when a load is added. Verification: math_evaluate verifies the cross-multiplied linear equations and reciprocal calculation. circuit_validate and circuit_simulate confirm $25\,\mathrm V$ without the load and $15\,\mathrm V$ with the derived load, with KCL and power balance satisfied.

**Answer:** 

</details>

**Problem: Assessment 3.5** (intermediate)

1. Find the current $i$ in the circuit without a meter.
2. The analog ammeter designed in Lecture 2 ($5\,\Omega$ terminal resistance) is inserted as shown. What does it read?

```schematic
V1 0,3 -> 0,0 "$1\,\mathrm{V}$"
AM1 0,3 -> 3,3
R1 3,3 -> 3,0 "$100\,\Omega$" i="$i$"
wire 3,0 -> 0,0
```

<details><summary>Solution</summary>

1. Before connecting the instrument, Ohm’s law gives **$i=\dfrac{1}{100}=0.010\,\mathrm A=10\,\mathrm{mA}$**.
2. The inserted ammeter has equivalent resistance $50\parallel(\dfrac{50}{9})=5\,\Omega$. Its external series connection adds this resistance to the circuit, so $R_{\mathrm{total}}=100+5=105\,\Omega$.
3. The total current that the ammeter reports is **$i_{\mathrm{read}}=\dfrac{1}{105}\,\mathrm A\approx9.524\,\mathrm{mA}$**. This is slightly below the unmeasured current. The movement itself takes only one tenth of the total; its scale is calibrated to report total terminal current. Verification: this matches the official assessment’s rounded result. math_evaluate checks the division; circuit_validate and circuit_simulate verify both the original circuit and the full movement-plus-shunt measurement circuit, including current and power balance.

**Answer:** 

</details>

**Problem: Tutorial P2.35 (Tutorial 1_solutions.pdf)** (advanced)

Find $i_o$ (the current in the wire joining the two networks), $i_1$ and $i_2$.

```schematic
V1 0,3 -> 0,0 "$18\,\mathrm{V}$"
R1 0,3 -> 3,3 "$12\,\Omega$"
R2 3,3 -> 3,0 "$6\,\Omega$" v="$v_\Delta$"
wire 3,0 -> 0,0
wire 3,0 -> 6,0
label 4.5,0 "$\leftarrow i_o$" below
G1 6,3 -> 6,0 "$\dfrac{v_\Delta}{2}$"
wire 6,3 -> 12,3
wire 6,0 -> 12,0
R3 9,3 -> 9,0 "$10\,\Omega$" i="$i_1$"
R4 12,3 -> 12,0 "$5\,\Omega$" i="$i_2$"
```

<details><summary>Solution</summary>

1. Enclose the entire input network and apply KCL to its boundary. The connecting wire is its only electrical connection to the output network; no steady net current can enter through a single connection without leaving elsewhere. Therefore **$i_o=0\,\mathrm A$**. The control signal specifies a source law; it is not an additional conductive branch.
2. The input loop is independent of output current. Its clockwise current is $i=\dfrac{18}{12+6}=1\,\mathrm A$, so $v_\Delta=6i=6\,\mathrm V$.
3. Use the controller to determine the dependent source: $i_d=(0.5\,\mathrm{A/V})(6\,\mathrm V)=3\,\mathrm A$ downward. KCL at $c$ gives $i_1+i_2+3=0$.
4. The output resistors are parallel, so KVL gives $10i_1=5i_2$, or $i_2=2i_1$. Substitute into KCL: $3i_1=-3\,\mathrm A$. Therefore **$i_1=-1\,\mathrm A$ and $i_2=-2\,\mathrm A$**. Both resistor currents actually flow upward, opposite their reference arrows. The shared output voltage is $V_c-V_{0_R}=10i_1=-10\,\mathrm V$. Verification: the official tutorial solution agrees. math_evaluate verifies the output-voltage equation. circuit_validate and circuit_simulate confirm this operating point with the computed fixed $3\,\mathrm A$ source; this checks the resistive network and conservation, while the dependent-source law was checked separately. The simulator does not model the controller or explicitly measure the single connecting wire.

**Answer:** 

</details>

**Problem: Textbook P3.58** (advanced)

Use a delta-to-wye transformation to find $v$.

```schematic
I1 0,0 -> 0,3 "$2\,\mathrm{A}$" v_rev="$v$"
wire 0,3 -> 0,5
R1 0,5 -> 8,5 "$28\,\Omega$"
wire 8,5 -> 8,3
R2 0,3 -> 4,3 "$20\,\Omega$"
R3 4,3 -> 8,3 "$10\,\Omega$"
R4 4,3 -> 4,0 "$5\,\Omega$"
R5 8,3 -> 8,0 "$105\,\Omega$"
wire 8,0 -> 0,0
```

<details><summary>Solution</summary>

1. The triangle prevents direct series/parallel reduction. Its resistance sum is $S=20+10+28=58\,\Omega$. Introduce center $n$ and apply the adjacent-product rule: the arm $a$–$n$ is $R_{an}=\dfrac{20(28)}{58}=(\dfrac{280}{29})\,\Omega$; arm $b$–$n$ is $R_{bn}=\dfrac{20(10)}{58}=(\dfrac{100}{29})\,\Omega$; arm $c$–$n$ is $R_{cn}=\dfrac{28(10)}{58}=(\dfrac{140}{29})\,\Omega$.
2. After transformation, the path from $n$ through $b$ to ground has resistance $R_B=(\dfrac{100}{29})+5=(\dfrac{245}{29})\,\Omega$. The path through $c$ has $R_C=(\dfrac{140}{29})+105=(\dfrac{3185}{29})\,\Omega$. These complete paths are parallel.
3. Add the input arm to their parallel equivalent: $R_{\mathrm{in}}=\dfrac{280}{29}+(\dfrac{245}{29})\parallel(\dfrac{3185}{29})=17.5\,\Omega$.
4. The original source’s terminal voltage is preserved by the transformation. Ohm’s law therefore gives **$v=(2\,\mathrm A)(17.5\,\Omega)=35\,\mathrm V$**, positive at the source’s upper terminal. Verification: math_evaluate checks the exact fractional reduction. circuit_validate and circuit_simulate of the original five-resistor circuit confirm $V_a=35\,\mathrm V$, KCL, and power balance. The original network remains the basis for any later individual-resistor current or power calculation.

**Answer:** 

</details>

## Summary

- KCL conserves current at nodes; KVL sums signed voltage changes around a closed loop. Reference directions stay fixed even when answers are negative.
- Dependent sources require a control equation in addition to KCL, KVL, and resistor laws.
- Series means one physical current path; parallel means the same node pair. Reduce by topology and then restore the original branches.
- Voltage division distributes series voltage in proportion to resistance; current division distributes parallel current in proportion to conductance.
- Loading changes divider output. Opposite resistor tolerance extremes determine the largest and smallest output ratios.
- Ammeters go in series and should have low input resistance; voltmeters go in parallel and should have high input resistance. Include real meter resistance before predicting a reading.
- At a Wheatstone bridge null, equal midpoint voltages give $R_1R_x=R_2R_3$ for the labels used here.
- Delta–wye transformations preserve external terminal behavior. Keep terminal labels, then reduce the transformed circuit and check power balance.

### Formula sheet

| Result | Formula | Use when |
|---|---|---|
| KCL | $\sum i_{\mathrm{entering}}=\sum i_{\mathrm{leaving}}$ | Relating currents at a node, with fixed arrows. |
| KVL | $\sum \Delta v_k=0$ | Relating signed voltage changes around a closed loop. |
| Resistor law and power | $v=Ri,\quad p=vi=Ri^2=\dfrac{v^2}{R}$ | Resistor current enters the positive voltage terminal. |
| Power check | $\sum p_k=0$ | All element powers use the passive sign convention; negative means delivery. |
| Series resistance | $R_{\mathrm{eq}}=\sum R_k$ | All selected resistors carry the same physical current. |
| Parallel resistance | $R_{\mathrm{eq}}=(\sum \dfrac{1}{R_k})^{-1};\quad R_1\parallel R_2=\dfrac{R_1R_2}{R_1+R_2}$ | All selected resistors share both nodes. |
| Voltage division | $v_j=\dfrac{vR_j}{R_{\mathrm{eq}}}$ | $R_{\mathrm{eq}}$ is the complete series resistance across voltage $v$. |
| Current division | $i_j=\dfrac{iR_{\mathrm{eq}}}{R_j}=\dfrac{iG_j}{\sum G_k}$ | $R_{\mathrm{eq}}$ is the parallel resistance receiving total current $i$. |
| Loaded divider | $v_o=\dfrac{v_s(R_2\parallel R_L)}{R_1+(R_2\parallel R_L)}$ | $R_L$ connects from the divider midpoint to the return node. |
| Unloaded divider loss | $P=\dfrac{v_s^2}{R_1+R_2}$ | Positive source delivery equals total resistor dissipation at no load. |
| Analog ammeter shunt | $R_m=\dfrac{V_m}{I_m};\quad R_A=\dfrac{V_m}{I_{\mathrm{FS}}-I_m}$ | Movement and shunt share the full-scale movement voltage. |
| Analog voltmeter series resistor | $R_v=\dfrac{V_{\mathrm{FS}}}{I_m}-R_m$ | Full-scale terminal voltage drives the rated movement current. |
| Balanced bridge | $R_x=\dfrac{R_2R_3}{R_1}$ | Detector current is zero; $R_1,R_3$ form the left side and $R_2,R_x$ the right. |
| Delta to wye | $R_1=\dfrac{R_bR_c}{S},\ R_2=\dfrac{R_cR_a}{S},\ R_3=\dfrac{R_aR_b}{S};\ S=R_a+R_b+R_c$ | Delta $R_a,R_b,R_c$ lie opposite terminals $a,b,c$; wye arms $R_1,R_2,R_3$ meet those terminals. |
| Wye to delta | $R_a=\dfrac{Q}{R_1},\ R_b=\dfrac{Q}{R_2},\ R_c=\dfrac{Q}{R_3};\ Q=R_1R_2+R_2R_3+R_3R_1$ | Use the same terminal labeling; divide by the arm opposite the desired delta edge. |
