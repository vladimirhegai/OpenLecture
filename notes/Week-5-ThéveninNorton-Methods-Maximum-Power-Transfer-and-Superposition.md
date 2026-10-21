# Week 5: Dependent-Source Equivalents, Maximum Power Transfer and Superposition

## Overview

> **Info:** Continue Week 4's Thévenin/Norton equivalents with dependent sources and test sources, then use equivalents to maximize load power. Superposition follows: solve the response to one independent source at a time and add the signed voltages or currents. The practice set has 20 problems covering different controls, load conditions and source combinations.

- Find the port resistance while preserving dependent-source controls.
- Distinguish the independent-sources-off test from an all-sources-on terminal relation.
- Choose an adjustable load for maximum power when the equivalent resistance is positive.
- Check which component is actually being optimized, and distinguish maximum power from efficiency.
- Use superposition while retaining dependent sources and consistent reference directions.

## Topic 1: Thévenin/Norton with dependent sources

*Source: ELEC221-F2026-Week5-Sec001.pdf, PDF p. 13; ELEC221-F2026-Week5-Sec001.pdf, PDF p. 15; ELEC221-F2026-Week5-Sec001.pdf, PDF p. 17; ELEC221-F2026-Week5-Sec001.pdf, PDF p. 19*

Use the same nodal or mesh equations as before. The extra job is to preserve the control relation: if a source depends on $i_x$, first express $i_x$ using the current arrow shown. Do this again whenever the circuit changes for an open circuit, short circuit or test-source calculation.

| Calculation | Independent sources | Dependent sources | Result |
|---|---|---|---|
| Open-circuit voltage | All active | All active, controls expressed in the open circuit | $V_{\mathrm{Th}}=v_{ab,\mathrm{open}}$ |
| Short-circuit current | All active | All active, controls recalculated for the short | $I_N=i_{sc}$ from a to b |
| Test-source resistance | Voltage sources shorted; current sources opened | Kept active with their control relations | $R_{\mathrm{Th}}=v_T/i_T$, with $i_T$ entering a |
| All-sources-on terminal relation | All active | All active | $v_T=V_{\mathrm{Th}}+R_{\mathrm{Th}}i_T$ for current entering a |

1. Mark port a–b, ground b, and remove the external load if doing so leaves the control variables defined.
2. Write all controlling currents and voltages in terms of your node voltages or mesh currents.
3. For a resistance test, deactivate only independent sources and apply a test voltage or current at the port.
4. Write KCL/KVL plus control constraints and solve by substitution.
5. Use test current entering the network at the positive test-voltage terminal when forming $R=v/i$.

> **Warning:** If the removed load contains a controlling current or voltage, do not erase that control or silently set it to zero in every calculation. Preserve the controlling branch in the model, move the port boundary, or derive a terminal relation with that load variable explicitly present. P4.90 practices this situation.

**Example: Lecture 5 · A valid negative equivalent resistance**

The network has only a dependent source. Find $V_{\mathrm{Th}}$ and $R_{\mathrm{Th}}$.

```schematic
E1 0,3 -> 0,0 "$12i_\Delta$"
R1 0,3 -> 3,3 "$2\,\Omega$"
R2 3,3 -> 3,0 "$4\,\Omega$" i="$i_\Delta$"
wire 3,3 -> 6,3
wire 3,0 -> 6,0
terminal 6,3 "$a$" right
terminal 6,0 "$b$" right
wire 0,0 -> 3,0
label 0,3 "$s$" left
ground 0,0
```

1. Ground b. With no independent excitation and a unique solution, the open-circuit voltage and external short-circuit current are zero. Their ratio is 0/0, so use a test source.

   $$V_{\mathrm{Th}}=0,\quad I_N=0$$

2. Apply a test voltage $v_T$ at a–b, with $i_T$ entering a. Write the control current and dependent-source voltage.

   $$i_\Delta=\dfrac{v_T}{4},\quad v_s=12i_\Delta=3v_T$$

3. Write KCL at a, including current through the 2 Ω resistor.

   $$i_T=\dfrac{v_T-v_s}{2}+\dfrac{v_T}{4}=\dfrac{v_T-3v_T}{2}+\dfrac{v_T}{4}=-\frac34v_T$$

4. Use the signed input ratio. For a +1 V test, current entering the network is negative.

   $$R_{\mathrm{Th}}=\dfrac{v_T}{i_T}=-\frac43\,\Omega$$

**Answer:** $V_{\mathrm{Th}}=0$, $R_{\mathrm{Th}}=-\tfrac43\,\Omega$.

*Source: ELEC221-F2026-Week5-Sec001.pdf, PDF p. 13*

**Example: Lecture 5 · Find both equivalent parameters in one terminal equation**

Keep every source on and push a test current $i_T$ into $a$. Find $v_T$ as a function of $i_T$, then read off $V_{\mathrm{Th}}$, $R_{\mathrm{Th}}$ and $I_N$.

```schematic
V1 0,3 -> 0,0 "$5\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\mathrm{k\Omega}$" i="$i$"
E1 3,3 -> 3,0 "$3v$"
G1 6,3 -> 6,0 "$20i$"
wire 6,3 -> 8,3
R2 8,3 -> 8,0 "$25\,\Omega$" v="$v$"
wire 8,3 -> 10,3
terminal 10,3 "$a$" right
terminal 10,0 "$b$" right
wire 0,0 -> 10,0
label 3,3 "$m$" above
ground 0,0
```

1. KCL at $a$ ($v=v_T$).

   $$v_T=25\,(i_T-20i)$$

2. Left loop.

   $$5=2000\,i+3v_T\;\Rightarrow\;i=\dfrac{5-3v_T}{2000}$$

3. Substitute.

   $$v_T=25\,i_T-1.25+0.75\,v_T\;\Rightarrow\;v_T=100\,i_T-5$$

4. Read off.

   $$V_{\mathrm{Th}}=-5\,\mathrm{V},\quad R_{\mathrm{Th}}=100\,\Omega,\quad I_N=\dfrac{-5}{100}=-50\,\mathrm{mA}$$

**Answer:** $v_T=100\,i_T-5$: $V_{\mathrm{Th}}=-5\,\mathrm{V}$, $R_{\mathrm{Th}}=100\,\Omega$, $I_N=-50\,\mathrm{mA}$.

*Source: ELEC221-F2026-Week5-Sec001.pdf, PDF p. 14; ELEC221-F2026-Week5-Sec001.pdf, PDF p. 17*

> **Warning:** Zero independent excitation implies zero port voltage only when the circuit has a unique finite zero-input solution. A dependent-source network may have a nonzero resistance, including a negative resistance. The usual passive-load maximum-power matching rule below requires $R_{\mathrm{Th}}>0$.

## Topic 2: Maximum power transfer

*Source: ELEC221-F2026-Week5-Sec001.pdf, PDF p. 20; ELEC221-F2026-Week5-Sec001.pdf, PDF p. 21; ELEC221-F2026-Week5-Sec001.pdf, PDF p. 22; ELEC221-F2026-Week5-Sec001.pdf, PDF p. 25*

First identify the resistor whose power is being maximized and what is adjustable. For an adjustable passive load $R_L$ connected to a fixed resistive network, find the equivalent seen by that load. When the equivalent resistance is finite and positive, the load receives its maximum power at $R_L=R_{\mathrm{Th}}$.

$$i_L=\frac{V_{\mathrm{Th}}}{R_{\mathrm{Th}}+R_L},\qquad P_L=i_L^2R_L=\frac{V_{\mathrm{Th}}^2R_L}{(R_{\mathrm{Th}}+R_L)^2}$$

**Why matching maximizes load power**

1. Differentiate load power with respect to the adjustable load resistance. The source equivalent stays fixed.

   $$\dfrac{dP_L}{dR_L}=\dfrac{V_{\mathrm{Th}}^2(R_{\mathrm{Th}}-R_L)}{(R_{\mathrm{Th}}+R_L)^3}$$

2. For positive $R_{\mathrm{Th}}$, power increases below the matching resistance and decreases above it.

   $$R_L=R_{\mathrm{Th}}$$

3. Substitute the matching resistance into the current, voltage and power expressions.

   $$i_L=\dfrac{V_{\mathrm{Th}}}{2R_{\mathrm{Th}}},\quad v_L=\dfrac{V_{\mathrm{Th}}}{2},\quad P_{\max}=\dfrac{V_{\mathrm{Th}}^2}{4R_{\mathrm{Th}}}$$

1. Remove the adjustable load and find the network equivalent at its two terminals.
2. Check that the equivalent resistance is positive and the network is fixed as the load changes.
3. Set $R_L=R_{\mathrm{Th}}$ and calculate $P_{\max}$. If only discrete resistor values are available, evaluate the allowed choices around the optimum.
4. For source power or efficiency, reconnect the load in the original circuit and calculate the original source currents and voltages.

> **Warning:** An adjustable series resistor feeding a different fixed resistor is a different optimization problem: write the target resistor power explicitly. Maximum load power also does not imply 50% efficiency for the entire original network. Dependent sources and internal branches must be included in the source-power calculation.

**Example: Lecture 5 · Match the load, then calculate original-circuit efficiency**

$R_L$ is adjustable. **(a)** Which $R_L$ gets the most power? **(b)** How much? **(c)** What fraction of the source's power reaches $R_L$?

```schematic
V1 0,3 -> 0,0 "$360\,\mathrm{V}$"
R1 0,3 -> 3,3 "$30\,\Omega$"
R2 3,3 -> 3,0 "$150\,\Omega$"
wire 3,3 -> 6,3
R3 6,3 -> 6,0 "$R_L$"
wire 0,0 -> 6,0
label 3,3 "$a$" above
ground 0,0
```

1. Remove $R_L$. The open output is the voltage across the fixed 150 Ω resistor.

   $$V_{\mathrm{Th}}=360\dfrac{150}{30+150}=300\,\mathrm{V}$$

2. Deactivate the voltage source for resistance, then reconnect and match the load.

   $$R_{\mathrm{Th}}=30\parallel150=25\,\Omega,\quad R_L=25\,\Omega$$

3. Compute the maximum power and the loaded output voltage.

   $$P_{\max}=\dfrac{300^2}{4(25)}=900\,\mathrm{W},\quad v_a=150\,\mathrm{V}$$

4. Use the original 360 V source and 30 Ω resistor for the source current.

   $$i_s=\dfrac{360-150}{30}=7\,\mathrm{A},\quad P_s=360(7)=2520\,\mathrm{W}$$

5. Divide actual load power by actual source power; the fixed 150 Ω branch also consumes power.

   $$\eta=\dfrac{900}{2520}\,100=35.7\%$$

**Answer:** **(a)** $25\,\Omega$ **(b)** $900\,\mathrm{W}$ **(c)** $35.7\%$

*Source: ELEC221-F2026-Week5-Sec001.pdf, PDF p. 24; ELEC221-F2026-Week5-Sec001.pdf, PDF p. 25*

**Example: Lecture 5 · Two independent sources before load matching**

$R_L$ is adjustable. Find the Thévenin equivalent at $a$–$b$ ($b$ is the bottom wire), then the best $R_L$ and $p_{\max}$.

```schematic
V1 0,0 -> 0,3 "$3\,\mathrm{V}$"
I1 0,3 -> 0,6 "$2\,\mathrm{mA}$"
wire 0,6 -> 8,6
R2 0,3 -> 3,3 "$3\,\mathrm{k\Omega}$"
wire 3,3 -> 4,3
R1 4,6 -> 4,3 "$4\,\mathrm{k\Omega}$"
R3 4,3 -> 4,0 "$6\,\mathrm{k\Omega}$"
R4 8,6 -> 8,3 "$R_L$"
wire 8,3 -> 8,0
wire 0,0 -> 8,0
label 8,6 "$a$" right
label 4,3 "$m$" right
label 0,3 "$c$" left
ground 4,0
```

1. Current source fixes mesh 1; KVL on the lower mesh (kΩ, mA).

   $$3+3(i_2-2)+6i_2=0\;\Rightarrow\;i_2=\tfrac13\,\mathrm{mA}$$

2. Open node voltage of $a$.

   $$V_{\mathrm{Th}}=4(2)+6(\tfrac13)=10\,\mathrm{V}$$

3. Sources off.

   $$R_{\mathrm{Th}}=4+(3\parallel6)=6\,\mathrm{k\Omega}$$

4. Match.

   $$R_L=6\,\mathrm{k\Omega},\qquad p_{\max}=\dfrac{10^2}{4(6000)}=4.17\,\mathrm{mW}$$

**Answer:** $V_{\mathrm{Th}}=10\,\mathrm{V}$, $R_{\mathrm{Th}}=6\,\mathrm{k\Omega}$; $R_L=6\,\mathrm{k\Omega}$ gets $4.17\,\mathrm{mW}$.

*Source: ELEC221-F2026-Week5-Sec001.pdf, PDF p. 24; ELEC221-F2026-Week5-Sec001.pdf, PDF p. 25*

## Topic 3: Superposition

*Source: ELEC221-F2026-Week5-Sec001.pdf, PDF p. 26; ELEC221-F2026-Week5-Sec001.pdf, PDF p. 30; ELEC221-F2026-Week5-Sec001.pdf, PDF p. 31; ELEC221-F2026-Week5-Sec001.pdf, PDF p. 37*

In a linear circuit, the total voltage or current is the algebraic sum of the contributions from the independent sources acting separately. Choose the output polarity or current arrow once and keep it unchanged in every subproblem. Negative contributions subtract from positive ones.

| Source being deactivated | Replacement |
|---|---|
| Ideal independent voltage source | Set its voltage to zero: replace it with a short circuit. |
| Ideal independent current source | Set its current to zero: replace it with an open circuit. |
| Dependent source | Keep it and recalculate its control from that subproblem. |
| Resistor | Keep it. Turning off a source does not remove its associated resistors. |

1. Name the requested output and its reference direction or polarity.
2. Keep one independent source active and deactivate the other independent sources. Keep all dependent sources.
3. Solve that reduced circuit using a divider, nodal analysis or mesh analysis.
4. Repeat for each independent source, using the same output reference.
5. Add the signed voltage or current contributions. Calculate power only from the final total voltage or current.

$$v=v^{(1)}+v^{(2)}+\cdots,\qquad i=i^{(1)}+i^{(2)}+\cdots$$

> **Warning:** Power does not superpose. For a resistor with current contributions $i^{(1)}$ and $i^{(2)}$, use $P_R=R(i^{(1)}+i^{(2)})^2$. Adding $R(i^{(1)})^2+R(i^{(2)})^2$ misses the cross term.

**Example: Lecture 5 · A voltage-source contribution and a current-source contribution**

Use superposition to find $v_o$ and $i_o$.

```schematic
V1 0,3 -> 0,0 "$120\,\mathrm{V}$"
R1 0,3 -> 3,3 "$6\,\Omega$"
R3 3,3 -> 3,0 "$3\,\Omega$" i="$i_o$"
R2 3,3 -> 6,3 "$2\,\Omega$"
R4 6,3 -> 6,0 "$4\,\Omega$" v="$v_o$"
wire 6,3 -> 9,3
I1 9,3 -> 9,0 "$12\,\mathrm{A}$"
wire 0,0 -> 9,0
label 0,3 "$s$" above
label 3,3 "$1$" above
label 6,3 "$2$" above
ground 0,0
```

1. $120\,\mathrm{V}$ alone (current source open).

   $$i_s=\dfrac{120}{6+(3\parallel6)}=15\,\mathrm{A},\quad v_1'=30,\quad i_o'=10\,\mathrm{A},\quad v_o'=20\,\mathrm{V}$$

2. $12\,\mathrm{A}$ alone (source shorted).

   $$v_o''=-12\,(4\parallel4)=-24\,\mathrm{V},\quad v_1''=-12,\quad i_o''=-4\,\mathrm{A}$$

3. Add.

   $$v_o=20-24=-4\,\mathrm{V},\qquad i_o=10-4=6\,\mathrm{A}$$

**Answer:** $v_o=-4\,\mathrm{V}$, $i_o=6\,\mathrm{A}$.

*Source: ELEC221-F2026-Week5-Sec001.pdf, PDF p. 34; ELEC221-F2026-Week5-Sec001.pdf, PDF p. 35; ELEC221-F2026-Week5-Sec001.pdf, PDF p. 36*

**Example: Lecture 5 · Recompute both dependent-source controls in each subproblem**

Use superposition on the two independent sources to find $v_o$. The current source is $0.4v_\Delta$ (A/V) and the voltage-source constraint is $2i_\Delta$ (Ω).

```schematic
V1 0,3 -> 0,0 "$10\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\Omega$" i="$i_\Delta$"
R2 3,3 -> 3,0 "$20\,\Omega$" v="$v_o$"
G1 6,3 -> 3,3 "$0.4v_\Delta$"
R3 6,3 -> 6,0 "$10\,\Omega$" v="$v_\Delta$"
E1 6,0 -> 3,0 "$2i_\Delta$"
I1 9,0 -> 9,3 "$5\,\mathrm{A}$"
wire 6,3 -> 9,3
wire 6,0 -> 9,0
wire 0,0 -> 3,0
label 0,3 "$s$" above
label 3,3 "$a$" above
label 6,3 "$d$" above
label 6,0 "$c$" below
ground 3,0
```

1. Use the original ground at the bottom of the 20 Ω resistor. Keep the dependent current and voltage sources in both subproblems. The output is the voltage at a relative to ground.

2. For the 10 V source alone, open the 5 A source. KCL at d forces the 10 Ω control voltage to zero. Its dependent current source is therefore zero for this subproblem.

   $$v_\Delta^{\prime}=0,\quad v_o^{\prime}=10\dfrac{20}{5+20}=8\,\mathrm{V}$$

3. The dependent voltage source still has a nonzero control current; it must not be replaced with a wire.

   $$i_\Delta^{\prime}=\dfrac{10-8}{5}=0.4\,\mathrm{A},\quad v_c^{\prime}=2i_\Delta^{\prime}=0.8\,\mathrm{V}$$

4. For the 5 A source alone, short the independent 10 V source. Write KCL at d to find the control voltage.

   $$5=0.4v_\Delta^{\prime\prime}+\dfrac{v_\Delta^{\prime\prime}}{10}\Rightarrow v_\Delta^{\prime\prime}=10\,\mathrm{V}$$

5. The dependent current source injects 4 A into a. The shorted independent voltage source leaves 5 Ω and 20 Ω connected to ground.

   $$v_o^{\prime\prime}=4(5\parallel20)=16\,\mathrm{V},\quad i_\Delta^{\prime\prime}=\dfrac{0-16}{5}=-3.2\,\mathrm{A}$$

6. Add the output contributions, preserving their common polarity.

   $$v_o=8+16=24\,\mathrm{V}$$

**Answer:** $v_o=24\,\mathrm{V}$

*Source: ELEC221-F2026-Week5-Sec001.pdf, PDF p. 34; ELEC221-F2026-Week5-Sec001.pdf, PDF p. 35; ELEC221-F2026-Week5-Sec001.pdf, PDF p. 36*

## Practice problems

These 20 source problems cover equivalent-circuit tests, matching, a fixed-load trap, two loads with the same power, finite available resistor values, controls that depend on load current, and several superposition structures. Where a source circuit supports multiple tasks, those tasks share one diagram instead of repeating the circuit as separate exercises.

| Group | Distinct challenges |
|---|---|
| Dependent-source equivalents | Current control, voltage control, zero independent excitation, zero Norton current with nonzero resistance. |
| Maximum power | Original-circuit efficiency, negative open voltage, fixed target resistor, two positive load solutions, discrete choices, load-current control. |
| Superposition | Adding a new source, a balanced bridge, multiple current sources, source current as an output, and controls that reverse sign between subproblems. |

**Problem: Assessment AP4.19 / Textbook P4.75 and P4.83 · Equivalent, matching and efficiency on one circuit** (intermediate)

Find **(a)** $V_{\mathrm{Th}}$; **(b)** $R_{\mathrm{Th}}$ using a test source; **(c)** the Norton equivalent; **(d)** the adjustable load and maximum power; **(e)** the percentage of total developed power delivered to that load.

```schematic
V1 0,3 -> 0,0 "$24\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
wire 0,3 -> 0,6
G1 3,6 -> 0,6 "$3i_x$"
wire 3,6 -> 3,3
wire 3,3 -> 5,3
I1 5,3 -> 5,0 "$4\,\mathrm{A}$"
wire 5,3 -> 7,3
R2 7,3 -> 7,0 "$8\,\Omega$" i="$i_x$"
wire 7,3 -> 9,3
terminal 9,3 "$a$" right
terminal 9,0 "$b$" right
wire 0,0 -> 9,0
ground 0,0
```

<details><summary>Solution</summary>

1. Open, KCL at $a$ with $i_x=\dfrac{v_a}{8}$.

   $$\dfrac{v_a-24}{2}+\dfrac{3v_a}{8}+4+\dfrac{v_a}{8}=0\;\Rightarrow\;V_{\mathrm{Th}}=8\,\mathrm{V}$$

2. Test source, independent sources off.

   $$i_T=\dfrac{v_T}{2}+\dfrac{3v_T}{8}+\dfrac{v_T}{8}=v_T\;\Rightarrow\;R_{\mathrm{Th}}=1\,\Omega$$

3. Check.

   $$i_{sc}=\tfrac{24}{2}-4=8\,\mathrm{A},\qquad \tfrac{8}{8}=1\,\Omega$$

4. Reconnect a load and match it to the positive equivalent resistance.

   $$R_o=1\,\Omega,\quad P_{\max}=\dfrac{8^2}{4(1)}=16\,\mathrm{W},\quad v_a=4\,\mathrm{V}$$

5. Return to the original circuit. The 24 V source delivers 204 W; the dependent current source delivers 30 W. The 4 A source absorbs 16 W.

   $$\begin{gathered}i_x=\frac48=0.5\,\mathrm{A}\\i_{24}=\dfrac{24-4}{2}-3(0.5)=8.5\,\mathrm{A}\\\eta=\dfrac{16}{24(8.5)+(24-4)(1.5)}\,100=6.84\%\end{gathered}$$

**Answer:** **(a)** $8\,\mathrm{V}$. **(b)** $1\,\Omega$. **(c)** $I_N=8\,\mathrm{A}$ from b toward a in parallel with $1\,\Omega$. **(d)** $R_o=1\,\Omega$, $P_{\max}=16\,\mathrm{W}$. **(e)** $6.84\%$.

</details>

*Source: Chapter 4 Problems.pdf, PDF p. 14; Chapter 4 Problems.pdf, PDF p. 15; TextBook-221.pdf, PDF p. 170; TextBook-221.pdf, PDF p. 171*

**Problem: Textbook P4.80 · A test source with a shared controlling current** (intermediate)

Find the Thévenin equivalent at $a$–$b$. The dependent source is controlled by $i_\Delta$ in the $12\,\Omega$.

```schematic
E1 0,4 -> 0,0 "$10i_\Delta$"
wire 0,4 -> 0,7
R1 0,7 -> 8,7 "$6\,\Omega$"
wire 8,7 -> 8,4
R2 0,4 -> 4,4 "$10\,\Omega$"
R3 8,4 -> 4,4 "$12\,\Omega$" i="$i_\Delta$"
R4 4,4 -> 4,0 "$2.5\,\Omega$"
wire 8,4 -> 11,4
terminal 11,4 "$a$" right
terminal 11,0 "$b$" right
wire 0,0 -> 11,0
label 0,4 "$x$" left
label 4,4 "$m$" above
ground 0,0
```

<details><summary>Solution</summary>

1. No independent source.

   $$V_{\mathrm{Th}}=0$$

2. Test voltage $v_T$ at $a$; $x=10i_\Delta$, $v_m=v_T-12i_\Delta$. KCL at $m$.

   $$i_\Delta+\dfrac{10i_\Delta-v_m}{10}=\dfrac{v_m}{2.5}\;\Rightarrow\;i_\Delta=\dfrac{v_T}{16}$$

3. For a concrete 1 V test, the constraint gives the following node voltages and test current.

   $$v_T=1\,\mathrm{V},\quad i_\Delta=\frac1{16}\,\mathrm{A},\quad v_x=0.625,\quad v_m=0.25\,\mathrm{V},\quad i_T=0.125\,\mathrm{A}$$

4. Test current: through the $6\,\Omega$ and the $12\,\Omega$.

   $$i_T=\dfrac{v_T-10i_\Delta}{6}+i_\Delta=\dfrac{v_T}{8}\;\Rightarrow\;R_{\mathrm{Th}}=8\,\Omega$$

**Answer:** $V_{\mathrm{Th}}=0$, $R_{\mathrm{Th}}=8\,\Omega$: the terminals act like an $8\,\Omega$ resistor.

</details>

*Source: TextBook-221.pdf, PDF p. 171*

**Problem: Textbook P4.74 · Test resistance with both independent and dependent sources** (intermediate)

Find the Thévenin equivalent at $a$–$b$.

```schematic
R1 0,3 -> 0,0 "$60\,\Omega$"
I1 3,0 -> 3,3 "$4\,\mathrm{A}$"
wire 0,3 -> 3,3
R2 3,3 -> 6,3 "$20\,\Omega$"
E1 6,3 -> 9,3 "$160i_\Delta$"
R3 9,3 -> 9,0 "$80\,\Omega$"
wire 9,3 -> 11,3
R4 11,3 -> 11,0 "$40\,\Omega$" i="$i_\Delta$"
wire 11,3 -> 13,3
terminal 13,3 "$a$" right
terminal 13,0 "$b$" right
wire 0,0 -> 13,0
label 3,3 "$n$" above
label 6,3 "$m$" above
ground 0,0
```

<details><summary>Solution</summary>

1. Control: $i_\Delta=\dfrac{v_a}{40}$, so the dependent source gives $v_m=v_a+160i_\Delta=5v_a$.

   $$4=\dfrac{v_n}{60}+\dfrac{v_n-5v_a}{20},\qquad \dfrac{v_n-5v_a}{20}=\dfrac{v_a}{80}+\dfrac{v_a}{40}$$

2. The right-node KCL gives $v_n=5.75v_a$. Substitute into the left-node equation.

   $$4=\dfrac{5.75v_a}{60}+\dfrac{0.75v_a}{20}=\dfrac{2v_a}{15}\Rightarrow v_a=30\,\mathrm{V}$$

3. Solve.

   $$v_a=V_{\mathrm{Th}}=30\,\mathrm{V},\qquad v_n=172.5\,\mathrm{V}$$

4. Test current, current source off.

   $$1=\dfrac{v_a}{80}+\dfrac{v_a}{40}+\dfrac{5v_a}{80}=\dfrac{v_a}{10}\;\Rightarrow\;R_{\mathrm{Th}}=10\,\Omega$$

**Answer:** $V_{\mathrm{Th}}=30\,\mathrm{V}$, $R_{\mathrm{Th}}=10\,\Omega$

</details>

*Source: TextBook-221.pdf, PDF p. 170*

**Problem: Textbook P4.81 · Only dependent excitation and a series output resistor** (intermediate)

Find the Thévenin equivalent at $a$–$b$.

```schematic
R1 0,3 -> 0,0 "$50\,\Omega$"
wire 0,3 -> 3,3
R2 3,3 -> 3,1.6 "$5\,\Omega$"
E1 3,0 -> 3,1.6 "$6.5i_x$"
R3 3,3 -> 6,3 "$10\,\Omega$"
R4 6,3 -> 6,0 "$25\,\Omega$" i="$i_x$"
R5 6,3 -> 9,3 "$12\,\Omega$"
terminal 9,3 "$a$" right
terminal 9,0 "$b$" right
wire 0,0 -> 9,0
label 3,3 "$t$" above
label 3,1.6 "$k$" right
label 6,3 "$m$" above
ground 0,0
```

<details><summary>Solution</summary>

1. No independent source.

   $$V_{\mathrm{Th}}=0$$

2. Test current $1\,\mathrm{A}$ into $a$; $i_x=\dfrac{v_m}{25}$, dependent source: $v_k=-6.5i_x$. Apply KCL at $m$ and $t$.

   $$\begin{aligned}1&=\tfrac{v_m}{25}+\tfrac{v_m-v_t}{10}\\\tfrac{v_m-v_t}{10}&=\tfrac{v_t}{50}+\tfrac{v_t+6.5v_m/25}{5}\end{aligned}$$

3. Rearrange the second equation to express $v_t$ in terms of $v_m$; substitute into the first.

   $$\begin{gathered}\dfrac{v_m-v_t}{10}=0.22v_t+0.052v_m\Rightarrow v_t=0.15v_m\\1=\dfrac{v_m}{25}+\dfrac{0.85v_m}{10}=0.125v_m\end{gathered}$$

4. Solve.

   $$v_m=8\,\mathrm{V},\quad v_t=1.2\,\mathrm{V},\quad v_a=8+12=20\,\mathrm{V}\;\Rightarrow\;R_{\mathrm{Th}}=20\,\Omega$$

**Answer:** $V_{\mathrm{Th}}=0$, $R_{\mathrm{Th}}=20\,\Omega$

</details>

*Source: TextBook-221.pdf, PDF p. 171*

**Problem: Textbook P4.84 · Maximize power in a fixed resistor** (introductory)

**(a)** Which $R_o$ gives the most power in the $6\,\Omega$? (Hint: hasty conclusions could be hazardous to your career.) **(b)** What is that power?

```schematic
V1 0,3 -> 0,0 "$30\,\mathrm{V}$"
R1 0,3 -> 3,3 "$R_o$"
R2 3,3 -> 3,0 "$6\,\Omega$"
wire 0,0 -> 3,0
label 3,3 "$a$" above
ground 0,0
```

<details><summary>Solution</summary>

1. The target is the fixed 6 Ω resistor. $R_o$ is an adjustable resistor in series with it, so derive the target power instead of matching $R_o$ to 6 Ω.

2. Write the load power directly.

   $$p_6=\Big(\dfrac{30}{R_o+6}\Big)^2(6)$$

3. Power decreases as $R_o$ grows, so choose the smallest allowed resistance.

   $$R_o=0,\qquad p_{\max}=\dfrac{30^2}{6}=150\,\mathrm{W}$$

4. For a passive adjustable series resistor, the smallest allowed value maximizes the fixed resistor current.

   $$\dfrac{dP_6}{dR_o}=-\dfrac{10800}{(R_o+6)^3}<0\quad(R_o\ge0)$$

**Answer:** **(a)** $R_o=0$ (not $6\,\Omega$) **(b)** $150\,\mathrm{W}$

</details>

*Source: TextBook-221.pdf, PDF p. 171; TextBook-221.pdf, PDF p. 172*

**Problem: Textbook P4.88 · Find two loads that absorb the same specified power** (advanced)

$R_o$ is adjusted until it dissipates $1.5\,\mathrm{W}$. Find **both** values of $R_o$.

```schematic
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
R1 0,3 -> 3,3 "$50\,\Omega$"
R2 3,3 -> 3,0 "$200\,\Omega$"
R3 3,3 -> 6,3 "$60\,\Omega$" i="$i_x$"
R4 6,3 -> 6,1.5 "$40\,\Omega$"
E1 6,0 -> 6,1.5 "$60i_x$"
wire 6,3 -> 9,3
R5 9,3 -> 9,0 "$R_o$"
wire 0,0 -> 9,0
label 3,3 "$n$" above
label 6,3 "$a$" above
label 6,1.5 "$k$" right
ground 0,0
```

<details><summary>Solution</summary>

1. Open circuit ($i_x$ through $60+40\,\Omega$ and the dependent source).

   $$\begin{aligned}&v_a=-20i_x,\quad v_n=40i_x,\quad \dfrac{100-v_n}{50}=\dfrac{v_n}{200}+i_x\\&\Rightarrow\;i_x=1\,\mathrm{A},\quad V_{\mathrm{Th}}=-20\,\mathrm{V}\end{aligned}$$

2. For the short circuit set $v_a=0$. KCL at the left node gives $v_n=48$ V, so $i_x=0.8$ A; the dependent source gives $v_k=-48$ V.

   $$i_{sc}=\dfrac{48}{60}-\dfrac{0-(-48)}{40}=-0.4\,\mathrm{A},\quad R_{\mathrm{Th}}=\dfrac{-20}{-0.4}=50\,\Omega$$

3. Power equation.

   $$\Big(\dfrac{20}{50+R_o}\Big)^2R_o=1.5\;\Rightarrow\;3R_o^2-500R_o+7500=0$$

4. Two roots.

   $$R_o=\dfrac{500\pm400}{6}=150\,\Omega\;\text{ or }\;16.7\,\Omega$$

5. Both roots are positive and lie on opposite sides of the matching resistance. Check each against the requested power.

   $$\dfrac{400(150)}{(50+150)^2}=1.5\,\mathrm{W},\quad\dfrac{400(50/3)}{(50+50/3)^2}=1.5\,\mathrm{W}$$

**Answer:** $R_o=16.7\,\Omega$ or $R_o=150\,\Omega$.

</details>

*Source: TextBook-221.pdf, PDF p. 172*

**Problem: Textbook P4.87 · Matching with two different dependent sources** (advanced)

$R_o$ is adjusted for maximum power. **(a)** Find $R_o$. **(b)** Find $p_{\max}$. **(c)** What percentage of the power developed reaches $R_o$?

```schematic
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$" i="$i_\Delta$"
R2 3,3 -> 3,1.6 "$5\,\Omega$"
E1 3,1.6 -> 3,0 "$13i_\Delta$"
R3 3,3 -> 6,3 "$4\,\Omega$" v="$v_\Delta$"
G1 6,0 -> 6,3 "$v_\Delta$"
wire 6,3 -> 9,3
RO 9,3 -> 9,0 "$R_o$"
wire 0,0 -> 9,0
label 3,3 "$p$" above
label 3,1.6 "$k$" right
label 6,3 "$q$" above
ground 0,0
```

<details><summary>Solution</summary>

1. Open: the current source forces $v_\Delta=0$; left loop.

   $$\begin{aligned}&100=(2+5+13)\,i_\Delta\;\Rightarrow\;i_\Delta=5\,\mathrm{A}\\&V_{\mathrm{Th}}=100-2(5)=90\,\mathrm{V}\end{aligned}$$

2. For the short circuit set q to 0. Let p be the left end of the 4 Ω resistor; the dependent voltage-source top is $13(100-v_p)/2$. Write KCL at p.

   $$\dfrac{v_p-100}{2}+\dfrac{v_p-13(100-v_p)/2}{5}+\dfrac{v_p}{4}=0\Rightarrow v_p=80\,\mathrm{V}$$

3. Both the 4 Ω resistor and dependent current source feed the external short.

   $$i_{sc}=\dfrac{80}{4}+80=100\,\mathrm{A},\quad R_{\mathrm{Th}}=\dfrac{90}{100}=0.9\,\Omega$$

4. At the matched load, q = 45 V, p = 85 V and $i_\Delta=7.5$ A. All three sources deliver power; calculate efficiency in the original circuit.

   $$R_o=0.9\,\Omega,\quad P_{\max}=2250\,\mathrm{W},\quad \eta=\dfrac{2250}{750+243.75+1800}\,100=80.54\%$$

**Answer:** **(a)** $0.9\,\Omega$ **(b)** $2250\,\mathrm{W}$ **(c)** $80.5\%$

</details>

*Source: TextBook-221.pdf, PDF p. 172*

**Problem: Textbook P4.94 · Three independent source contributions** (intermediate)

Use superposition to find $i_o$.

```schematic
I1 0,0 -> 0,4 "$6\,\mathrm{A}$"
wire 0,4 -> 2,4
R1 2,4 -> 2,0 "$20\,\Omega$"
R2 2,4 -> 5,4 "$1\,\Omega$" i="$i_o$"
I2 5,4 -> 5,0 "$10\,\mathrm{A}$"
wire 5,4 -> 11,4
R3 7,4 -> 7,0 "$60\,\Omega$"
R4 9,4 -> 9,2 "$5\,\Omega$"
V1 9,2 -> 9,0 "$75\,\mathrm{V}$"
R5 11,4 -> 11,0 "$30\,\Omega$"
wire 0,0 -> 11,0
label 2,4 "$p$" above
label 5,4 "$q$" above
label 9,2 "$k$" right
ground 0,0
```

<details><summary>Solution</summary>

1. $6\,\mathrm{A}$ alone.

   $$i_o'=6\cdot\dfrac{20}{20+(1+4)}=4.8\,\mathrm{A}$$

2. $10\,\mathrm{A}$ alone.

   $$i_o''=10\cdot\dfrac{4}{4+21}=1.6\,\mathrm{A}$$

3. $75\,\mathrm{V}$ alone.

   $$\dfrac{v-75}{5}+\dfrac{v}{60}+\dfrac{v}{30}+\dfrac{v}{21}=0\Rightarrow v=50.4,\;\;i_o'''=-\dfrac{50.4}{21}=-2.4\,\mathrm{A}$$

4. Add.

   $$i_o=4.8+1.6-2.4=4\,\mathrm{A}$$

**Answer:** $i_o=4\,\mathrm{A}$ ($4.8$, $1.6$, $-2.4$).

</details>

*Source: TextBook-221.pdf, PDF p. 173*

**Problem: Textbook P4.96 · Add a source to a circuit already solved** (intermediate)

Before the $5\,\mathrm{mA}$ source is attached between $a$ and $b$, $i_o=3.5\,\mathrm{mA}$. **(a)** Use superposition to find $i_o$ after it is attached. **(b)** Check with all three sources on.

```schematic
V1 0,3 -> 0,0 "$8\,\mathrm{V}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$5\,\mathrm{k\Omega}$"
R2 3,3 -> 6,3 "$2\,\mathrm{k\Omega}$"
R3 6,3 -> 6,0 "$6\,\mathrm{k\Omega}$" i="$i_o$"
wire 6,3 -> 9,3
I1 9,0 -> 9,3 "$10\,\mathrm{mA}$"
wire 3,3 -> 3,5
I2 6,5 -> 3,5 "$5\,\mathrm{mA}$"
wire 6,5 -> 6,3
wire 0,0 -> 9,0
label 3,3 "$a$" below
label 6,3 "$b$" below
ground 0,0
```

<details><summary>Solution</summary>

1. The new source alone ($8\,\mathrm{V}$ shorted, $10\,\mathrm{mA}$ open).

   $$i_o''=-5\cdot\dfrac{2}{2+6}=-1.25\,\mathrm{mA}$$

2. Add to the old answer.

   $$i_o=3.5-1.25=2.25\,\mathrm{mA}$$

3. Check: KCL at $b$ with all three.

   $$\dfrac{v_b-8}{2}+\dfrac{v_b}{6}+5=10\;\Rightarrow\;v_b=13.5\,\mathrm{V},\;\;i_o=2.25\,\mathrm{mA}$$

**Answer:** $i_o=2.25\,\mathrm{mA}$

</details>

*Source: TextBook-221.pdf, PDF p. 173*

**Problem: Textbook P4.95 · Superpose both an output voltage and source current** (intermediate)

Use superposition to find $i_o$ and $v_o$.

```schematic
V1 0,3 -> 0,0 "$180\,\mathrm{V}$" i_rev="$i_o$"
R1 0,3 -> 3,3 "$30\,\Omega$"
R2 3,3 -> 3,0 "$60\,\Omega$"
I1 6,3 -> 3,3 "$7.5\,\mathrm{A}$"
R3 6,3 -> 6,0 "$80\,\Omega$" v="$v_o$"
R4 6,3 -> 9,3 "$20\,\Omega$"
R5 9,3 -> 9,0 "$25\,\Omega$"
wire 0,3 -> 0,5
R6 0,5 -> 9,5 "$40\,\Omega$"
wire 9,5 -> 9,3
wire 0,0 -> 9,0
label 3,3 "$p$" below
label 6,3 "$q$" below
label 9,3 "$r$" right
ground 0,0
```

<details><summary>Solution</summary>

1. Ground the bottom node. Let S be the left voltage-source value and J the current from q to p. KCL at p, q and r gives:

   $$3v_p-2S=60J,\quad5v_q-4v_r=-80J,\quad23v_r-10v_q=5S$$

2. Use the second equation to express $v_r$ and substitute into the third.

   $$v_r=\dfrac{5v_q+80J}{4}\Rightarrow75v_q=20S-1840J$$

3. With 180 V alone, open the current source. Use the source current reference pointing upward.

   $$\begin{gathered}S=180,\ J=0:\\v_p=120,\ v_q=48,\ v_r=60\,\mathrm{V}\\i_o^{\prime}=\dfrac{180-120}{30}+\dfrac{180-60}{40}=5\,\mathrm{A}\end{gathered}$$

4. With 7.5 A alone, short the independent voltage source. Keep the same references.

   $$\begin{gathered}S=0,\ J=7.5:\\v_p=150,\ v_q=-184,\ v_r=-80\,\mathrm{V}\\i_o^{\prime\prime}=\dfrac{-150}{30}+\dfrac{80}{40}=-3\,\mathrm{A}\end{gathered}$$

5. Add the two output voltages and the two source-current contributions.

   $$v_o=48-184=-136\,\mathrm{V},\quad i_o=5-3=2\,\mathrm{A}$$

**Answer:** $i_o=2\,\mathrm{A}$, $v_o=-136\,\mathrm{V}$

</details>

*Source: TextBook-221.pdf, PDF p. 173*

**Problem: Textbook P4.93 · A balanced bridge appears in one subproblem** (advanced)

Use superposition to find $i_o$, the current in the $45\,\mathrm{V}$ source.

```schematic
V1 0,5 -> 0,2 "$45\,\mathrm{V}$" i_rev="$i_o$"
wire 0,5 -> 1,5
R1 1,5 -> 4,5 "$5\,\Omega$"
R2 4,5 -> 7,5 "$10\,\Omega$"
wire 7,5 -> 8,5
V2 8,5 -> 8,2 "$10\,\mathrm{V}$"
R3 4,5 -> 4,2 "$40\,\Omega$"
wire 0,2 -> 1,2
R4 1,2 -> 4,2 "$15\,\Omega$"
R5 4,2 -> 7,2 "$30\,\Omega$"
wire 7,2 -> 8,2
wire 0,2 -> 0,0 -> 3,0
I1 5,0 -> 3,0 "$8\,\mathrm{A}$"
wire 5,0 -> 8,0 -> 8,2
label 1,5 "$p$" above
label 4,5 "$m$" above
label 7,5 "$n$" above
label 4,2 "$k$" below
label 8,2 "$r$" right
ground 0,0
```

<details><summary>Solution</summary>

1. $45\,\mathrm{V}$ alone.

   $$i_o'=\dfrac{45}{5+(40\parallel40)+15}=1.125\,\mathrm{A}$$

2. $10\,\mathrm{V}$ alone.

   $$i_{10}=\dfrac{10}{53.33}=0.1875\,\mathrm{A},\quad i_o''=-0.1875\cdot\dfrac{40}{60}=-0.125\,\mathrm{A}$$

3. $8\,\mathrm{A}$ alone: balanced bridge ($\tfrac{10}{5}=\tfrac{30}{15}$), no current in the $40\,\Omega$.

   $$i_o'''=8\cdot\dfrac{45}{15+45}=6\,\mathrm{A}$$

4. Add.

   $$i_o=1.125-0.125+6=7\,\mathrm{A}$$

**Answer:** $i_o=7\,\mathrm{A}$ ($1.125$, $-0.125$, $6$).

</details>

*Source: TextBook-221.pdf, PDF p. 173*

**Problem: Assessment AP4.21 / Textbook P4.85(a–b), P4.86 · Efficiency with a voltage-controlled source** (advanced)

$R_o$ is set for maximum power; $v_\phi$ is the voltage across the $4\,\Omega$ in series with the $20\,\mathrm{V}$ source. **(a)** Find $R_o$. **(b)** Find $p_{\max}$. **(c)** (P4.86) What percentage of the power developed reaches $R_o$?

```schematic
V1 0,4 -> 0,0 "$100\,\mathrm{V}$"
R1 0,4 -> 3,4 "$4\,\Omega$"
R2 3,4 -> 6,4 "$4\,\Omega$"
R3 3,4 -> 3,2 "$4\,\Omega$" v="$v_\phi$"
V2 3,2 -> 3,0 "$20\,\mathrm{V}$"
wire 0,4 -> 0,7
E1 3,7 -> 0,7 "$v_\phi$"
R4 3,7 -> 6,7 "$4\,\Omega$"
wire 6,7 -> 6,4
wire 6,4 -> 8,4
R5 8,4 -> 8,0 "$R_o$"
wire 0,0 -> 8,0
label 3,4 "$c$" above
label 3,7 "$t$" above
label 3,2 "$d$" right
label 8,4 "$a$" above
ground 0,0
```

<details><summary>Solution</summary>

1. Open: $v_\phi=v_c-20$, dependent source top $=80+v_c$; KCL at $a$, then $c$.

   $$v_a=40+v_c,\qquad v_c=80\;\Rightarrow\;V_{\mathrm{Th}}=120\,\mathrm{V}$$

2. For the open port, KCL at c and a gives two equations. Substitute the source constraint and then $v_a=v_c+40$.

   $$\begin{gathered}\dfrac{v_c-100}{4}+\dfrac{v_c-20}{4}+\dfrac{v_c-v_a}{4}=0\\\dfrac{v_a-v_c}{4}+\dfrac{v_a-(v_c+80)}{4}=0\Rightarrow v_c=80\,\mathrm{V}\end{gathered}$$

3. Short: KCL at $c$.

   $$v_c=40\,\mathrm{V},\qquad I_N=\dfrac{120}{4}+\dfrac{40}{4}=40\,\mathrm{A}$$

4. Match.

   $$R_o=R_{\mathrm{Th}}=\dfrac{120}{40}=3\,\Omega,\qquad p_{\max}=\dfrac{120^2}{4(3)}=1200\,\mathrm{W}$$

5. Back to the original with $R_o=3\,\Omega$.

   $$\eta=\dfrac{1200}{100(30)+40(20)}=\dfrac{1200}{3800}=31.6\%$$

**Answer:** **(a)** $3\,\Omega$ **(b)** $1200\,\mathrm{W}$ **(c)** $31.6\%$

</details>

*Source: Chapter 4 Problems.pdf, PDF p. 16; Chapter 4 Problems.pdf, PDF p. 17; TextBook-221.pdf, PDF p. 172*

**Problem: Textbook P4.98 · A dependent current source stays active** (intermediate)

Use superposition to find $v_o$.

```schematic
V1 0,3 -> 0,0 "$25\,\mathrm{V}$"
R1 4,3 -> 0,3 "$4\,\mathrm{k\Omega}$" i="$i_\phi$"
I1 4,3 -> 4,0 "$5\,\mathrm{mA}$"
wire 4,3 -> 8,3
R2 8,3 -> 8,0 "$20\,\mathrm{k\Omega}$" v="$v_o$"
wire 0,3 -> 0,5
G1 0,5 -> 8,5 "$2.2i_\phi$"
wire 8,5 -> 8,3
wire 0,0 -> 8,0
label 4,3 "$n$" above
ground 0,0
```

<details><summary>Solution</summary>

1. $25\,\mathrm{V}$ alone, $i_\phi=\dfrac{v_o-25}{4}$ (mA, kΩ).

   $$2.2\,\dfrac{v_o-25}{4}=\dfrac{v_o-25}{4}+\dfrac{v_o}{20}\;\Rightarrow\;v_o'=30\,\mathrm{V}$$

2. $5\,\mathrm{mA}$ alone, $i_\phi=\dfrac{v_o}{4}$.

   $$2.2\,\dfrac{v_o}{4}=\dfrac{v_o}{4}+5+\dfrac{v_o}{20}\;\Rightarrow\;v_o''=20\,\mathrm{V}$$

3. Add.

   $$v_o=30+20=50\,\mathrm{V}$$

**Answer:** $v_o=50\,\mathrm{V}$

</details>

*Source: TextBook-221.pdf, PDF p. 173*

**Problem: Textbook P4.79 · Zero Norton current with nonzero port resistance** (advanced)

Find the Norton equivalent at $a$–$b$. There are only dependent sources: $i_\Delta$ is downward through $700\,\Omega$; the current source is $21i_\Delta$ and the voltage source is $(300\,\Omega)i_\Delta$.

```schematic
G1 0,0 -> 0,3 "$21i_\Delta$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$700\,\Omega$" i="$i_\Delta$"
E1 6,3 -> 3,3 "$300i_\Delta$"
R2 6,3 -> 6,0 "$10\,\Omega$"
wire 6,3 -> 9,3
wire 0,0 -> 9,0
terminal 9,3 "$a$" right
terminal 9,0 "$b$" right
label 3,3 "$x$" above
ground 0,0
```

<details><summary>Solution</summary>

1. Ground b and name the other internal node x. With no independent input and a unique solution, the open-circuit voltages and short-circuit current are zero.

   $$V_{\mathrm{Th}}=0,\quad I_N=0$$

2. Apply a 1 V test source at a–b. The controlling current and voltage-source constraint give $v_x$.

   $$i_\Delta=\dfrac{v_x}{700},\quad 1-v_x=300\dfrac{v_x}{700}\Rightarrow v_x=0.7\,\mathrm{V},\quad i_\Delta=1\,\mathrm{mA}$$

3. Use KCL around the supernode containing x and a. Define test current entering a.

   $$i_T=\dfrac{1}{10}+\dfrac{0.7}{700}-21\dfrac{0.7}{700}=0.08\,\mathrm{A}$$

4. Compute the resistance. A zero Norton source does not make the port a short circuit.

   $$R_N=\frac1{0.08}=12.5\,\Omega$$

**Answer:** $I_N=0\,\mathrm{A}$ and $R_N=12.5\,\Omega$; the port behaves as a $12.5\,\Omega$ resistor.

</details>

*Source: TextBook-221.pdf, PDF p. 171*

**Problem: Textbook P4.89 (a–c) · Maximum power with a negative open-circuit voltage** (advanced)

$R_o$ is adjusted for maximum power transfer. Find **(a)** $R_o$; **(b)** its maximum power; **(c)** the percentage of the total power developed that reaches $R_o$. The two independent voltage sources have their positive terminals at the bottom.

```schematic
V1 0,0 -> 0,4 "$200\,\mathrm{V}$"
R1 0,4 -> 4,4 "$1\,\Omega$"
wire 4,4 -> 6,4
R2 6,4 -> 8,4 "$2\,\Omega$"
V2 8,0 -> 8,4 "$100\,\mathrm{V}$"
R3 4,4 -> 4,0 "$20\,\Omega$" i="$i_\Delta$"
R4 0,0 -> 4,0 "$4\,\Omega$"
wire 4,0 -> 6,0
R5 6,0 -> 8,0 "$3\,\Omega$"
wire 0,4 -> 0,7
E1 0,7 -> 8,7 "$14i_\Delta$"
wire 8,7 -> 8,4
RL 5,4 -> 5,0 "$R_o$"
label 0,4 "$a$" left
label 4,4 "$p$" above
label 8,4 "$c$" right
ground 4,0
```

<details><summary>Solution</summary>

1. Ground the bottom central node. Call the load voltage v and top side nodes a and c. Preserve the inverted source polarities and the dependent-source constraint.

   $$i_\Delta=\frac v{20},\quad v_l=v_a+200,\quad v_r=v_c+100,\quad v_a-v_c=0.7v$$

2. Use KCL around the connected source supernode and at the load node. With load current $i_L$ referenced downward, the two reduced equations are:

   $$15v_a+10v_c-18v=-1000,\quad\dfrac{v-v_a}{1}+\dfrac{v-v_c}{2}+\frac v{20}+i_L=0$$

3. Use $v_a=v_c+0.7v$ to express the side nodes, then substitute into load-node KCL.

   $$v_c=0.3v-40,\quad v_a=v-40\Rightarrow 60+0.4v+i_L=0\Rightarrow v=-150-2.5i_L$$

4. Read the port equivalent and match the load. A negative voltage gives a negative referenced current but positive resistor power.

   $$V_{\mathrm{Th}}=-150\,\mathrm{V},\quad R_{\mathrm{Th}}=2.5\,\Omega,\quad R_o=2.5\,\Omega,\quad P_{\max}=\dfrac{150^2}{4(2.5)}=2250\,\mathrm{W}$$

5. At the matched load, v = −75 V and $i_L=-30$ A. Return to the original source currents; the sources deliver 4250 W, 1250 W and 984.375 W.

   $$\begin{gathered}v_a=-115\\v_c=-62.5\\i_\Delta=-3.75\,\mathrm{A}\\\eta=\dfrac{2250}{4250+1250+984.375}\,100=34.70\%\end{gathered}$$

**Answer:** **(a)** $R_o=2.5\,\Omega$. **(b)** $2250\,\mathrm{W}$. **(c)** $34.70\%$.

</details>

*Source: TextBook-221.pdf, PDF p. 172*

**Problem: Textbook P4.90 · Preserve a control current that flows through the load** (advanced)

Find **(a)** the $R_o$ for maximum power transfer; **(b)** the maximum power delivered to it; **(c)** the power delivered by the $280\,\mathrm{V}$ source at that setting. Here $i_\phi$ is the load current itself; keep it symbolic rather than deleting the controlling branch.

```schematic
R1 0,4 -> 3,4 "$10\,\Omega$"
R2 3,4 -> 6,4 "$5\,\Omega$" v="$v_\Delta$"
R3 6,4 -> 9,4 "$20\,\Omega$"
R4 0,4 -> 0,0 "$100\,\Omega$"
V1 3,4 -> 3,0 "$280\,\mathrm{V}$"
RL 6,4 -> 6,0 "$R_o$" i="$i_\phi$"
R5 9,4 -> 9,0 "$400\,\Omega$"
wire 9,4 -> 12,4
G1 12,4 -> 12,0 "$0.5125v_\Delta$"
wire 0,4 -> 0,7
E1 0,7 -> 12,7 "$50i_\phi$"
wire 12,7 -> 12,4
wire 0,0 -> 12,0
label 0,4 "$x$" left
label 3,4 "$s$" above
label 6,4 "$a$" above
label 9,4 "$z$" above
ground 0,0
```

<details><summary>Solution</summary>

1. Ground the bottom node, call the load voltage v, and retain $i_\phi$ downward through the load. Write the two control relations.

   $$v_s=280,\quad v_\Delta=280-v,\quad v_x-v_z=50i_\phi$$

2. KCL at the load node and around the x–z supernode includes the downward dependent current source.

   $$\begin{aligned}\dfrac{v-280}{5}+\dfrac{v-v_z}{20}+i_\phi&=0\\\dfrac{v_x}{100}+\dfrac{v_x-280}{10}+\dfrac{v_z-v}{20}+\dfrac{v_z}{400}+0.5125(280-v)&=0\end{aligned}$$

3. Isolate $v_z$ from the first equation. Substitute it and $v_x=v_z+50i_\phi$ into the second.

   $$v_z=5v-1120+20i_\phi,\quad44v_x+21v_z-225v+46200=0$$

4. Simplify to the actual load voltage–current relation, retaining the load-current control.

   $$100v+3500i_\phi-26600=0\Rightarrow v=266-35i_\phi$$

5. Maximize the load power in terms of its current, then recover its resistance.

   $$P_L=vi_\phi=266i_\phi-35i_\phi^2,\quad\dfrac{dP_L}{di_\phi}=266-70i_\phi=0\Rightarrow i_\phi=3.8\,\mathrm{A}$$

6. At this current, calculate load voltage, resistance and power.

   $$v=133\,\mathrm{V},\quad R_o=\dfrac{133}{3.8}=35\,\Omega,\quad P_{\max}=133(3.8)=505.4\,\mathrm{W}$$

7. Return to the original circuit for source power. $v_x=-189$ V, so the 280 V source supplies both the 10 Ω and 5 Ω currents.

   $$\begin{gathered}i_s=\dfrac{280-(-189)}{10}+\dfrac{280-133}{5}=76.3\,\mathrm{A}\\P_{280,\mathrm{del}}=280(76.3)=21364\,\mathrm{W}\end{gathered}$$

**Answer:** **(a)** $35\,\Omega$. **(b)** $505.4\,\mathrm{W}$. **(c)** $21.364\,\mathrm{kW}$ delivered.

</details>

*Source: TextBook-221.pdf, PDF p. 172*

**Problem: Textbook P4.91 · Maximum power with a current-controlled voltage source** (advanced)

Find **(a)** $R_L$ for maximum power transfer and **(b)** the maximum power. The source on the left has $+$ at its bottom; $i_\beta$ points right through $6\,\Omega$.

```schematic
V1 0,0 -> 0,4 "$480\,\mathrm{V}$"
R1 0,4 -> 4,4 "$6\,\Omega$" i="$i_\beta$"
R2 4,4 -> 4,0 "$40\,\Omega$"
wire 4,4 -> 6,4
R3 6,4 -> 8,4 "$8\,\Omega$"
E1 8,0 -> 8,4 "$20i_\beta$"
R4 0,0 -> 4,0 "$4\,\Omega$"
wire 4,0 -> 6,0
R5 6,0 -> 8,0 "$2\,\Omega$"
wire 0,4 -> 0,7
R6 0,7 -> 8,7 "$4\,\Omega$"
wire 8,7 -> 8,4
RL 5,4 -> 5,0 "$R_L$"
label 0,4 "$a$" left
label 4,4 "$p$" above
label 8,4 "$c$" right
label 8,0 "$r$" right
ground 4,0
```

<details><summary>Solution</summary>

1. Ground the bottom middle node and call the load voltage v. Name the side top nodes a and c, and the lower-right node r. Introduce downward load current $i_L$.

   $$i_\beta=\dfrac{v_a-v}{6},\quad v_l=v_a+480,\quad v_r=v_c+20i_\beta$$

2. Write KCL around the two source supernodes and at the load node, then clear denominators.

   $$\begin{aligned}8v_a-3v_c-2v&=-1440\\34v_a+21v_c-43v&=0\\-20v_a-15v_c+38v+120i_L&=0\end{aligned}$$

3. Use the first two equations to express the side voltages in terms of the load voltage.

   $$v_a=\dfrac{19v-3360}{30},\qquad v_c=\dfrac{46v+8160}{45}$$

4. Substitute these into the third equation to get the port relation.

   $$10v-480+120i_L=0\Rightarrow v=48-12i_L$$

5. Use the positive equivalent resistance for matching, then calculate power.

   $$V_{\mathrm{Th}}=48\,\mathrm{V},\quad R_{\mathrm{Th}}=12\,\Omega,\quad R_L=12\,\Omega,\quad P_{\max}=\dfrac{48^2}{4(12)}=48\,\mathrm{W}$$

6. Check the matched load voltage and current.

   $$i_L=\dfrac{48}{12+12}=2\,\mathrm{A},\quad v_L=24\,\mathrm{V},\quad v_Li_L=48\,\mathrm{W}$$

**Answer:** **(a)** $R_L=12\,\Omega$. **(b)** $48\,\mathrm{W}$.

</details>

*Source: TextBook-221.pdf, PDF p. 173*

**Problem: Textbook P4.82, using Fig. P4.72 · Available resistor values versus the continuous optimum** (advanced)

**(a)** Calculate the power delivered to $R_o$ for every listed Appendix H resistor with $10\,\Omega\le R_o<100\,\Omega$: $10,15,22,33,47,68\,\Omega$. **(b)** Plot power versus $R_o$. **(c)** Identify the best listed value and compare it with the continuous optimum.

```schematic
R1 0,4 -> 0,0 "$40\,\Omega$"
wire 0,4 -> 6,4
I1 3,4 -> 3,0 "$3\,\mathrm{A}$"
R2 6,4 -> 6,2 "$60\,\Omega$"
V1 6,2 -> 6,0 "$300\,\mathrm{V}$"
R3 6,4 -> 9,4 "$6\,\Omega$"
RL 9,4 -> 9,0 "$R_o$"
wire 0,0 -> 9,0
label 6,4 "$n$" above
label 9,4 "$a$" right
ground 0,0
```

<details><summary>Solution</summary>

1. Remove only the load and solve the open circuit at n. There is no current through the 6 Ω resistor, so its voltage drop is zero.

   $$\dfrac{v_n}{40}+\dfrac{v_n-300}{60}+3=0\Rightarrow V_{\mathrm{Th}}=v_n=48\,\mathrm{V}$$

2. Deactivate the independent sources for resistance: open the 3 A source and short the 300 V source.

   $$R_{\mathrm{Th}}=6+(40\parallel60)=30\,\Omega$$

3. Calculate the load power as a function of resistance, then evaluate it at the listed values.

   $$P_L(R_o)=\dfrac{48^2R_o}{(30+R_o)^2}$$

4. The continuous optimum is 30 Ω, but that value is not in the specified list. Evaluate both neighboring available values instead of automatically rounding to one.

   $$P_L(22)\approx18.746\,\mathrm{W},\quad P_L(33)\approx19.156\,\mathrm{W},\quad P_L(30)=19.2\,\mathrm{W}$$

The curve is continuous; the points are the available resistor choices in this problem.

```graph
title "P4.82: load power versus resistance"
x 0 100 label="$R_o$ ($\Omega$)"
y 0 21 label="$P_L$ (W)"
curve "2304*x/(30+x)^2" label="load power"
point "10" "2304*10/40^2"
point "15" "2304*15/45^2"
point "22" "2304*22/52^2"
point "33" "2304*33/63^2" label="best listed: 33 ohms" color=2
point "47" "2304*47/77^2"
point "68" "2304*68/98^2"
vline "30" label="continuous optimum" color=3
caption "Compare both available values around the optimum. The 33 ohm choice delivers slightly more power than 22 ohms."
```

**Answer:** Listed powers, in the stated order: $14.400,17.067,18.746,19.156,18.264,16.313\,\mathrm{W}$. Best listed choice: $33\,\Omega$. Continuous optimum: $30\,\Omega$ at $19.2\,\mathrm{W}$.

</details>

*Source: TextBook-221.pdf, PDF p. 171; TextBook-221.pdf, PDF p. 788*

**Problem: Textbook P4.92(a), using Fig. P4.7 · Superposition for a voltage inside a series branch** (intermediate)

Use superposition to find the voltage $v=v_x$ relative to ground at the junction of $6\,\Omega$ and $2\,\Omega$. This is the voltage marked in the original Fig. P4.7, rather than the voltage across either resistor.

```schematic
I1 0,0 -> 0,3 "$4.5\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$1\,\Omega$"
R2 3,3 -> 6,3 "$6\,\Omega$"
R3 6,3 -> 9,3 "$2\,\Omega$"
R4 9,3 -> 9,0 "$12\,\Omega$"
R5 9,3 -> 12,3 "$4\,\Omega$"
V1 12,3 -> 12,0 "$30\,\mathrm{V}$"
wire 0,0 -> 12,0
label 3,3 "$a$" above
label 6,3 "$x$" above
label 9,3 "$b$" above
ground 0,0
```

<details><summary>Solution</summary>

1. Activate only the 30 V source; open the 4.5 A source. From node b the resistance to ground is $12\parallel(2+6+1)$.

   $$R_b=12\parallel9=\dfrac{36}{7}\,\Omega,\quad v_b^{(30)}=30\dfrac{36/7}{4+36/7}=16.875\,\mathrm{V}$$

2. Current in the 2 Ω, 6 Ω, 1 Ω series branch flows from b toward ground. Calculate the voltage at x, which is above the 6 Ω + 1 Ω part.

   $$i^{(30)}=\dfrac{16.875}{9}=1.875\,\mathrm{A},\quad v_x^{(30)}=1.875(6+1)=13.125\,\mathrm{V}$$

3. Activate only the current source; short the 30 V source. Then $12\parallel4=3$ Ω, making the other path from a to ground $6+2+3=11$ Ω.

   $$v_a^{(4.5)}=4.5(1\parallel11)=4.125\,\mathrm{V},\quad i^{(4.5)}=\dfrac{4.125}{11}=0.375\,\mathrm{A}$$

4. Use the same x-to-ground reference. Subtract the 6 Ω drop from the a-node voltage, then add the two contributions.

   $$v_x^{(4.5)}=4.125-6(0.375)=1.875\,\mathrm{V},\quad v=13.125+1.875=15\,\mathrm{V}$$

**Answer:** $v=15\,\mathrm{V}$, made from $13.125\,\mathrm{V}+1.875\,\mathrm{V}$.

</details>

*Source: TextBook-221.pdf, PDF p. 173; TextBook-221.pdf, PDF p. 162*

**Problem: Textbook P4.97(a), using Fig. P4.21 · The dependent-source control changes in each subproblem** (advanced)

Use superposition to find $v_o$. The dependent current source is $3i_1$ directed from b to a, where $i_1$ is rightward through $6\,\Omega$. Only the independent sources are turned off.

```schematic
V1 0,3 -> 0,0 "$50\,\mathrm{V}$"
R1 0,3 -> 3,3 "$6\,\Omega$" i="$i_1$"
R2 3,3 -> 3,0 "$8\,\Omega$"
R3 3,3 -> 6,3 "$2\,\Omega$"
R4 6,3 -> 6,0 "$4\,\Omega$" v="$v_o$"
wire 6,3 -> 9,3
I1 9,0 -> 9,3 "$5\,\mathrm{A}$"
wire 3,3 -> 3,5
G1 6,5 -> 3,5 "$3i_1$"
wire 6,5 -> 6,3
wire 0,0 -> 9,0
label 0,3 "$s$" above
label 3,3 "$a$" below
label 6,3 "$b$" below
ground 0,0
```

<details><summary>Solution</summary>

1. Ground the bottom node. Let S be the active independent voltage and J the active independent current. Express the dependent control separately in each subproblem.

   $$i_1=\dfrac{S-v_a}{6},\qquad i_{\mathrm{dep}}=\dfrac{S-v_a}{2}$$

2. Write KCL at a and b with the dependent current source present; clear denominators.

   $$31v_a-12v_b=16S,\qquad-4v_a+3v_b=4J-2S$$

3. For 50 V acting alone, open the 5 A source. Substitute S=50 and J=0 and solve.

   $$31v_a^{\prime}-12v_b^{\prime}=800,\quad-4v_a^{\prime}+3v_b^{\prime}=-100\Rightarrow v_a^{\prime}=\dfrac{80}{3},\quad v_b^{\prime}=\dfrac{20}{9}\,\mathrm{V}$$

4. For 5 A acting alone, short the independent voltage source. The control becomes $i_1=-v_a/6$, and the dependent source remains active.

   $$31v_a^{\prime\prime}-12v_b^{\prime\prime}=0,\quad-4v_a^{\prime\prime}+3v_b^{\prime\prime}=20\Rightarrow v_a^{\prime\prime}=\dfrac{16}{3},\quad v_b^{\prime\prime}=\dfrac{124}{9}\,\mathrm{V}$$

5. Add voltages using the same output polarity; do not add powers.

   $$v_o=\dfrac{20}{9}+\dfrac{124}{9}=16\,\mathrm{V}$$

**Answer:** $v_o=16\,\mathrm{V}$.

</details>

*Source: TextBook-221.pdf, PDF p. 173; TextBook-221.pdf, PDF p. 164*

## Summary

- Independent voltage sources become shorts and independent current sources become opens only in the appropriate deactivation calculation.
- Dependent sources remain active, and each control is recomputed for the circuit being solved.
- Use a test source when the open/short ratio is 0/0.
- For a fixed network with positive equivalent resistance and an adjustable passive load, maximum load power occurs at $R_L=R_{\mathrm{Th}}$.
- Identify the actual target resistor and the actual adjustable element before applying a matching formula.
- Calculate original source powers and efficiency in the original loaded circuit.
- Superposition adds signed voltages or currents; compute power from the final total.

### Formula sheet

| Result | Formula | Use when |
|---|---|---|
| Test-source resistance | $R_{\mathrm{Th}}=\dfrac{v_T}{i_T}$ | Independent sources deactivated, dependent sources retained; iT enters the + port. |
| Terminal relation | $v=V_{\mathrm{Th}}-R_{\mathrm{Th}}i_L$ | iL leaves the network into the load. |
| Load power | $P_L=\dfrac{V_{\mathrm{Th}}^2R_L}{(R_{\mathrm{Th}}+R_L)^2}$ | Fixed linear resistive network feeding load RL. |
| Maximum power | $R_L=R_{\mathrm{Th}}$, $P_{\max}=\dfrac{V_{\mathrm{Th}}^2}{4R_{\mathrm{Th}}}$ | Equivalent resistance is finite and positive; the load is adjustable. |
| Efficiency | $\eta=\dfrac{P_L}{\sum P_{\mathrm{sources,delivering}}}\,100\%$ | Use actual source powers in the original circuit. |
| Superposition | $v=\sum v^{(k)}$, $i=\sum i^{(k)}$ | Circuit is linear; use the same reference for each contribution. |
| Resistor power after superposition | $P_R=R(\sum i^{(k)})^2$ | Add currents first, then calculate power. |
