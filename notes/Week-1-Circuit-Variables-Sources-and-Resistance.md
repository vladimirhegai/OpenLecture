# Week 1: Circuit Variables, Sources, and Resistance

## Overview

> **Info:** Week 1 establishes the language of circuit analysis: charge flow, voltage, energy transfer, ideal sources, and resistance. As the first week, it provides the foundation for later circuit-solving methods; the lecture’s final Kirchhoff’s-law slides introduce the connection to Week 2.

### Learning outcomes

- Relate charge, current, voltage, power, and energy, with correct SI units (Nilsson 1.4–1.6).
- Apply the passive sign convention and distinguish absorbed from delivered power (Nilsson 1.5–1.6).
- Identify ideal independent and dependent voltage and current sources and their constraints (Nilsson 2.1).
- Use resistance, conductance, and Ohm’s law; distinguish active and passive elements and ideal opens and shorts (Nilsson 2.2).

## Topic 1: Circuit variables: charge, current, voltage, power, and energy

A circuit describes how charge moves and how energy is transferred between components. Charge is the quantity being transported; current tells you how quickly it passes a chosen cross-section. Conventional current follows positive-charge motion, so electron motion in a metal is opposite to the conventional current direction.

| Term | Meaning |
|---|---|
| Charge $q$ | Signed electric charge, measured in coulombs ($\mathrm{C}$). Positive and negative charges attract; like charges repel. |
| Current $i$ | Signed rate of charge flow along a reference arrow; measured in amperes ($\mathrm{A}=\mathrm{C/s}$). |
| Voltage $v$ | Energy transferred per unit charge between two terminals with a marked polarity; measured in volts ($\mathrm{V}=\mathrm{J/C}$). |
| Energy $w$ | Amount of energy transferred, measured in joules ($\mathrm{J}$). |
| Power $p$ | Rate of energy transfer, measured in watts ($\mathrm{W}=\mathrm{J/s}$). |

$$i(t)=\frac{dq(t)}{dt},\qquad q(t_2)-q(t_1)=\int_{t_1}^{t_2}i(\tau)\,d\tau$$

Here $t$ is time in seconds, $q(t)$ is cumulative signed charge crossing the reference section, and $i(t)$ is current along the chosen arrow. The integration variable $\tau$ is time; $t_1$ and $t_2$ are the beginning and end of the interval. Differentiate charge to find current; integrate current to find transferred charge, retaining any given initial charge.

$$v=\frac{dw}{dq},\qquad v_{ab}=V_a-V_b$$

In the energy-per-charge definition, $w$ is transferred energy and $q$ is charge. In the terminal reference, $V_a$ and $V_b$ are node potentials relative to the same reference, and $v_{ab}$ means plus at terminal $a$, minus at terminal $b$. A voltage always compares two points; a negative value means the actual polarity opposes the markings.

$$p(t)=\frac{dw(t)}{dt},\qquad w(t_2)-w(t_1)=\int_{t_1}^{t_2}p(\tau)\,d\tau$$

Here $p(t)$ is signed absorbed power and $w(t_2)-w(t_1)$ is net absorbed energy over the interval. Use the integral for changing power; for constant power $P$, the change is $P(t_2-t_1)$. The sign of absorbed power will be fixed by the current arrow and voltage polarity in the next section.

**Derivation: voltage and current determine power**

1. Apply the chain rule to energy transferred by moving charge, using compatible energy and charge references.

   $$p=\frac{dw}{dt}=\frac{dw}{dq}\frac{dq}{dt}$$
2. Substitute the definitions of voltage and current. This form gives absorbed power when current enters the terminal marked positive.

   $$p=vi$$

**Example: Total charge in a decaying current pulse (Assessment AP 1.3)**

For $t\ge0$ the current $i(t)=20e^{-5000t}\,\mathrm{A}$ enters terminal $a$ of element $X$; before $t=0$ it is zero. Find the total charge that enters terminal $a$.

```schematic
terminal 0,0 "a" left
X1 0,0 -> 4,0 "$X$" i="$i(t)$"
terminal 4,0 "b" right
```

1. The total signed transferred charge $Q$ is the area under the current waveform.

   $$Q=\int_0^\infty20e^{-5000t}\,dt$$
2. Use an antiderivative; its derivative was checked with math_evaluate.

   $$F(t)=-\frac{20}{5000}e^{-5000t},\qquad F'(t)=20e^{-5000t}$$
3. The exponential tends to zero. Final answer: 4000 microcoulombs enter terminal a; the arithmetic was independently verified.

   $$Q=F(\infty)-F(0)=\frac{20}{5000}=0.004\,\mathrm{C}=4\,\mathrm{mC}=4000\,\mu\mathrm{C}$$

**Answer:** $Q=0.004\,\mathrm{C}=4000\,\mu\mathrm{C}$

> **Warning:** A negative current is a valid answer: charge moves opposite to the reference arrow. Convert milliseconds to seconds and milliamperes to amperes before integration; the exponent of an exponential must be dimensionless.

> **Tip:** Read a waveform as a rate: its slope gives the derivative and its signed area gives the integral. Charge from current and energy from power use the same integration pattern.

## Topic 2: Passive sign convention: absorbed and delivered power

Power accounting answers “which element receives energy, and which supplies it?” Draw a voltage polarity and a current reference arrow before multiplying values. The passive sign convention (PSC) chooses the current arrow into the terminal marked positive; the arrow is a reference, not a claim about the actual current.

| Reference arrangement | Absorbed-power rule |
|---|---|
| Current reference enters the $+$ terminal | $p_{\mathrm{abs}}=vi$ |
| Current reference enters the $-$ terminal | $p_{\mathrm{abs}}=-vi$ |
| $p_{\mathrm{abs}}>0$ | The element absorbs energy at that rate. |
| $p_{\mathrm{abs}}<0$ | The element delivers energy at rate $-p_{\mathrm{abs}}$. |

$$p_{\mathrm{abs}}=\begin{cases}vi,&i\text{ enters }+,\\-vi,&i\text{ enters }-.\end{cases}$$

The quantities $v$ and $i$ are the signed voltage and current for the markings already chosen; $p_{\mathrm{abs}}$ is signed absorbed power. Inspect where the reference arrow enters, choose the formula, then substitute signed values. Delivered power as a positive magnitude is $-p_{\mathrm{abs}}$ only when the element is delivering.

$$\sum_k p_{\mathrm{abs},k}=0,\qquad P_{\mathrm{delivered,total}}=P_{\mathrm{absorbed,total}}$$

The index $k$ runs over every element in a complete circuit. The uppercase quantities $P_{\mathrm{delivered,total}}$ and $P_{\mathrm{absorbed,total}}$ are positive totals of delivered and absorbed power, respectively. A power-balance check catches many sign errors, although balance alone does not prove all circuit equations are satisfied.

**Example: Power balance in a three-element loop (Lecture 1)**

Write the power of each element with the passive sign convention and state the conservation-of-energy equation for this loop.

```schematic
X1 0,3 -> 0,0 "$a$" v="$v_a$" i_rev="$i_a$"
X2 0,3 -> 4,3 "$b$" v="$v_b$" i_rev="$i_b$"
X3 4,3 -> 4,0 "$c$" v_rev="$v_c$" i="$i_c$"
wire 4,0 -> 0,0
```

1. Element $a$: $i_a$ points up, so it enters the bottom terminal, which is marked $-$. Current entering $-$ means a minus sign.

   $$p_a=-v_ai_a$$
2. Element $b$: $v_b$ is $+$ on the left and $i_b$ flows right to left, so it enters the $-$ terminal.

   $$p_b=-v_bi_b$$
3. Element $c$: $v_c$ is $+$ at the bottom and $i_c$ flows down, entering the top ($-$) terminal.

   $$p_c=-v_ci_c$$
4. Energy is conserved, so the absorbed powers of all elements sum to zero.

   $$p_a+p_b+p_c=-(v_ai_a+v_bi_b+v_ci_c)=0$$

**Answer:** $p_a=-v_ai_a$, $p_b=-v_bi_b$, $p_c=-v_ci_c$, and $p_a+p_b+p_c=0$.

**Example: Same power, different references (Assessment AP 1.5)**

Terminal 2 of element $X$ is $20\,\mathrm{V}$ above terminal 1, and $4\,\mathrm{A}$ enters terminal 2. Find the power absorbed by $X$, and give $v$ and $i$ for each of the four reference choices (+ at terminal 1 or 2; arrow into terminal 1 or 2).

```schematic
terminal 0,3 "1" left
X1 0,3 -> 0,0 "$X$" v_rev="$20\,\mathrm{V}$" i_rev="$4\,\mathrm{A}$"
terminal 0,0 "2" left
```

1. With plus at terminal 1 and an arrow into terminal 1, both signed values are negative.

   $$v_{12}=V_1-V_2=-20\,\mathrm{V},\qquad i_{1\to2}=-4\,\mathrm{A}$$
2. These references obey PSC. Final answer: the element absorbs 80 watts.

   $$p_{\mathrm{abs}}=v_{12}i_{1\to2}=(-20)(-4)=80\,\mathrm{W}$$
3. Changing reference markings changes signed values and sometimes the formula, but never the physical absorbed power. This agrees with the official assessment solution.

   $$\begin{array}{c|c|c|c}+\text{ terminal}&\text{current arrow}&(v,i)&p_{\mathrm{abs}}\\1&1\to2&(-20\,\mathrm{V},-4\,\mathrm{A})&vi=80\,\mathrm{W}\\1&2\to1&(-20\,\mathrm{V},4\,\mathrm{A})&-vi=80\,\mathrm{W}\\2&1\to2&(20\,\mathrm{V},-4\,\mathrm{A})&-vi=80\,\mathrm{W}\\2&2\to1&(20\,\mathrm{V},4\,\mathrm{A})&vi=80\,\mathrm{W}\end{array}$$

**Answer:** $p=80\,\mathrm{W}$ absorbed, for every choice of references.

> **Warning:** A minus sign on $v$ or $i$ is not itself a statement that an element delivers power. Also, source symbols do not guarantee negative absorbed power: a voltage or current source can absorb energy. Always compute the signed power.

> **Tip:** For each element write “enters plus” or “enters minus” beside the current arrow. Then use $+vi$ or $-vi$ and check the sum of signed powers.

## Topic 3: Ideal independent and dependent sources

A source model specifies one terminal variable and lets the surrounding circuit determine the other. “Ideal” means the model enforces its specified relation exactly; it does not add the limits or internal resistance of a real battery or supply. The lecture treats DC values, while a prescribed independent-source value can more generally be a given function of time.

| Term | Meaning |
|---|---|
| Ideal basic element | A two-terminal mathematical model described by voltage and/or current and not subdivided into simpler basic elements. |
| Independent source | Its specified voltage or current does not depend on another circuit variable; its symbol is a circle. |
| Dependent source | Its output depends on a labeled voltage or current elsewhere in the circuit; its symbol is a diamond. |
| Voltage source | Fixes terminal voltage; terminal current must be found from the connection. |
| Current source | Fixes branch current; terminal voltage must be found from the connection. |

$$v_{ab}=v_s\quad\text{(voltage source)},\qquad i_{a\to b}=i_s\quad\text{(current source)}$$

Here $v_s$ is the specified source voltage, with plus at $a$ and minus at $b$, and $i_s$ is the specified source current, with arrow from $a$ to $b$. Neither equation gives the other terminal variable or the source power without further circuit information.

| Dependent-source type | Output relation and gain units |
|---|---|
| Voltage-controlled voltage source (VCVS) | $v_s=\mu v_x$; voltage gain $\mu$ is dimensionless. |
| Current-controlled voltage source (CCVS) | $v_s=r_m i_x$; transresistance $r_m$ has units $\Omega$. |
| Current-controlled current source (CCCS) | $i_s=\beta i_x$; current gain $\beta$ is dimensionless. |
| Voltage-controlled current source (VCCS) | $i_s=g_m v_x$; transconductance $g_m$ has units $\mathrm{S}=\mathrm{A/V}$. |

The control voltage $v_x$ and control current $i_x$ must each have their own polarity or arrow. The symbols $\mu$, $r_m$, $\beta$, and $g_m$ distinguish the four gain types; the slides use $\mu$ for several gains. The control variable retains its sign when substituted, and gain units must turn the control quantity into the output quantity.

**Example: A source may absorb power (Tutorial P2.1)**

Is this connection of ideal sources valid? Find the power of each source, then reverse the $10\,\mathrm{V}$ source and repeat.

```schematic
V1 0,3 -> 0,0 "$30\,\mathrm{V}$"
V2 0,3 -> 4,3 "$10\,\mathrm{V}$"
I1 4,0 -> 4,3 "$8\,\mathrm{A}$"
wire 4,0 -> 0,0
label 0,3 "$a$" above
label 4,3 "$b$" above
ground 0,0
```

1. The voltage sources set node differences. The current source can support the resulting voltage, so the source constraints are compatible.

   $$V_a=30\,\mathrm{V},\qquad V_a-V_b=10\,\mathrm{V}\Rightarrow V_b=20\,\mathrm{V}$$
2. The single path carries the imposed current from node b through the 10 V source toward a and down through the 30 V source.

   $$i_{30}=8\,\mathrm{A}\ (a\to0),\qquad i_{10}=-8\,\mathrm{A}\ (a\to b)$$
3. The 30 V source absorbs 240 W; the 10 V and 8 A sources deliver 80 W and 160 W. Their signed sum is zero.

   $$p_{30}=30(8)=240\,\mathrm{W},\quad p_{10}=10(-8)=-80\,\mathrm{W},\quad p_8=-20(8)=-160\,\mathrm{W}$$
4. Reverse only the 10 V source polarity; retain the current references.

   $$V_a-V_b=-10\,\mathrm{V}\Rightarrow V_b=40\,\mathrm{V}$$
5. Final reversed-case result: both voltage sources absorb, and the current source delivers 320 W. The connection remains valid and power balances. Both cases agree with the official tutorial solution and circuit_simulate.

   $$p_{30}=240\,\mathrm{W},\quad p_{10}=80\,\mathrm{W},\quad p_8=-320\,\mathrm{W}$$

**Answer:** Valid both times. **As drawn:** $p_{30}=240\,\mathrm{W}$ (absorbs), $p_{10}=-80\,\mathrm{W}$, $p_{8\mathrm{A}}=-160\,\mathrm{W}$. **Reversed:** $p_{30}=240\,\mathrm{W}$, $p_{10}=80\,\mathrm{W}$, $p_{8\mathrm{A}}=-320\,\mathrm{W}$.

> **Warning:** Do not assign zero current to a voltage source or zero voltage to a current source. A dependent source is not an independent numerical value until its controlling variable is known. A negative output reverses the actual direction or polarity relative to its symbol.

> **Tip:** First write what each source fixes. Reject conflicting ideal constraints: unequal voltage sources directly across the same nodes, or unequal current sources in a single unbranched path, cannot both enforce their values. Compatible constraints can still leave some source currents or voltages undetermined. This is a model-consistency check.

## Topic 4: Resistance, conductance, Ohm’s law, and circuit limits

A resistor links voltage and current: a larger resistance requires a larger voltage to sustain the same current. An ideal linear resistor has a fixed resistance, so Ohm’s law applies directly once the references are chosen. Resistance is an element property; voltage and current depend on its connection.

| Term | Meaning |
|---|---|
| Resistance $R$ | Opposition to current flow, measured in ohms ($\Omega=\mathrm{V/A}$). |
| Conductance $G$ | Reciprocal of resistance, measured in siemens ($\mathrm{S}=\mathrm{A/V}$). |
| Active element | Can supply electrical energy; voltage and current sources are examples. |
| Passive element | Does not create energy; resistors dissipate it. Inductors and capacitors, studied later, can store and return previously supplied energy. |
| Ideal short | Connected terminals have zero voltage difference; current is determined by the rest of the circuit. |
| Ideal open | Separated terminals carry no current; voltage is determined by the rest of the circuit. |

$$G=\frac1R,\qquad v=Ri,\qquad i=Gv$$

Here $R$ is resistance, $G$ is conductance, $v$ is voltage from the marked plus terminal to the minus terminal, and $i$ enters the plus terminal. The reciprocal relation assumes a finite nonzero resistance. These voltage-current equations use PSC; when the current arrow enters the minus terminal, use $v=-Ri$.

$$p_R=vi=Ri^2=\frac{v^2}{R}=Gv^2\geq0\qquad(R>0)$$

The symbol $p_R$ is absorbed resistor power. For a positive resistor the squared forms are nonnegative regardless of actual current direction or voltage polarity. Use $Ri^2$ when current is known and $\dfrac{v^2}{R}$ when voltage is known; the product $vi$ needs matching PSC references.

**Derivation: resistor power and reversed references**

1. Substitute Ohm’s law into PSC power.

   $$p_R=vi=(Ri)i=Ri^2$$
2. Alternatively eliminate current; using G = 1/R also gives G times voltage squared.

   $$p_R=vi=v\left(\frac vR\right)=\frac{v^2}{R}$$
3. If the current reference enters the minus terminal, change both Ohm’s-law and power signs. Physical dissipation remains nonnegative.

   $$v=-Ri,\quad p_R=-vi=-(-Ri)i=Ri^2$$

**Example: Reversing a voltage source (Tutorial P2.11)**

Find $i$ and the power supplied by the source. Then reverse the source polarity and repeat.

```schematic
V1 0,3 -> 0,0 "$120\,\mathrm{V}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$10\,\mathrm{k\Omega}$" i="$i$"
wire 3,0 -> 0,0
```

1. The resistor shares both source terminals, so its voltage is fixed. Apply Ohm’s law with PSC.

   $$R=10\,000\,\Omega,\qquad v_R=120\,\mathrm{V},\qquad i=\frac{120}{10\,000}=0.012\,\mathrm{A}=12\,\mathrm{mA}$$
2. The resistor absorbs 1.44 W and the source delivers 1.44 W; p_s denotes signed absorbed source power.

   $$p_R=\frac{120^2}{10\,000}=1.44\,\mathrm{W},\qquad p_s=-1.44\,\mathrm{W}$$
3. Final reversed-case result: current reverses, resistor absorption remains 1.44 W, and source power supplied remains 1.44 W. Both cases were validated and checked with circuit_simulate against the official tutorial solution.

   $$v_R=-120\,\mathrm{V},\qquad i=-12\,\mathrm{mA},\qquad p_R=R(-0.012)^2=1.44\,\mathrm{W}$$
4. The conductance is the same in either case; this reciprocal was checked with math_evaluate.

   $$G=\frac1{10\,000}=0.0001\,\mathrm{S}=0.1\,\mathrm{mS}$$

**Answer:** $i=12\,\mathrm{mA}$ and the source supplies $1.44\,\mathrm{W}$. Reversed: $i=-12\,\mathrm{mA}$, and it still supplies $1.44\,\mathrm{W}$.

$$\text{Short: }R=0,\ v=0;\qquad \text{Open: }R\to\infty,\ i=0$$

For a short, $v$ is terminal voltage and $i$ may be nonzero; for an open, $i$ is branch current and $v$ may be nonzero. The resistance limits describe ideal closed and open switches. They do not imply that every terminal variable is zero.

> **Warning:** Never evaluate $\dfrac{v}{R}$ at an ideal short or multiply an open’s “infinite resistance” by zero. Use the constraints $v=0$ and $i=0$ directly. Shorting a nonzero ideal voltage source imposes conflicting voltages; opening the only path of a nonzero ideal current source imposes conflicting currents.

> **Tip:** Choose the power formula that uses what is already known. A negative power result for an ordinary positive resistor usually signals a reference-sign error.

### Bridge to Week 2: the lecture’s final circuit equations

Ohm’s law describes individual resistors; Kirchhoff’s laws connect those descriptions across a circuit. A node is a common electrical connection, and a loop is a closed path without revisiting an intermediate node. Kirchhoff’s current law (KCL) balances signed currents at each node; Kirchhoff’s voltage law (KVL) balances signed voltage changes around a loop. The syllabus develops these methods in Week 2.

$$\sum_{\text{node}}i_k=0,\qquad \sum_{\text{loop}}v_k=0$$

Here $i_k$ is each branch current with a consistent entering/leaving sign at the chosen node, and $v_k$ is each voltage contribution with a consistent traversal sign around the chosen loop. The index $k$ labels the contributions. Either global sign choice works; for a connected circuit with $n$ nodes, only $n-1$ KCL equations are independent.

**Example: Solving the lecture's single loop**

With $v_s$, $R_1$, $R_c$ and $R_l$ known, find all seven unknowns: $i_s, i_1, i_c, i_l, v_1, v_c, v_l$.

```schematic
V1 0,3 -> 0,0 "$v_s$" i_rev="$i_s$"
wire 0,3 -> 6,3
R3 6,3 -> 6,0 "$R_l$" v="$v_l$" i="$i_l$"
R2 3,0 -> 6,0 "$R_c$" v="$v_c$" i="$i_c$"
R1 3,0 -> 0,0 "$R_1$" v="$v_1$" i="$i_1$"
label 0,3 "$d$" above
label 6,0 "$c$" right
label 3,0 "$b$" below
label 0,0 "$a$" left
```

1. Use three independent node equations. The fourth, at d, is redundant.

   $$i_s-i_1=0,\quad i_1+i_c=0,\quad -i_c-i_l=0$$
2. Define I as the loop current in the source’s upward reference direction. The middle resistor arrow opposes that direction.

   $$i_s=i_1=i_l=I,\qquad i_c=-I$$
3. All three labeled resistor pairs obey PSC. Substitute the signed currents into each resistor equation.

   $$v_1=IR_1,\quad v_c=-IR_c,\quad v_l=IR_l$$
4. Use the lecture’s loop traversal and substitute the element relations.

   $$v_l-v_c+v_1-v_s=0\Rightarrow I(R_l+R_c+R_1)=v_s$$
5. Final symbolic solution: I and the branch currents are in amperes when v_s is in volts and the resistances are in ohms; all labeled voltages are in volts. The minus sign on v_c comes from its reference polarity.

   $$I=\frac{v_s}{R_1+R_c+R_l},\quad v_1=\frac{v_sR_1}{R_1+R_c+R_l},\quad v_c=-\frac{v_sR_c}{R_1+R_c+R_l},\quad v_l=\frac{v_sR_l}{R_1+R_c+R_l}$$

**Answer:** $i_s=i_1=i_l=-i_c=\dfrac{v_s}{R_1+R_c+R_l}$; $v_1=\dfrac{R_1v_s}{R_1+R_c+R_l}$, $v_c=-\dfrac{R_cv_s}{R_1+R_c+R_l}$, $v_l=\dfrac{R_lv_s}{R_1+R_c+R_l}$

## Practice problems

Try each problem before opening its solution. The problems progress from direct power and ideal-element interpretation to integration, source reversal, dependent-source constraints, and a time-varying power maximum.

**Problem: Textbook P1.16** (introductory)

A $9\,\mathrm{V}$ battery supplies $150\,\mathrm{mA}$ to a boom box for $3\,\mathrm{h}$. How much energy does the battery supply?

```schematic
B1 0,3 -> 0,0 "$9\,\mathrm{V}$"
wire 0,3 -> 3,3
X1 3,3 -> 3,0 "boom box" i="$150\,\mathrm{mA}$"
wire 3,0 -> 0,0
```

<details><summary>Solution</summary>

1. Use power times elapsed time because both terminal quantities are constant. Convert $I=0.150\,\mathrm{A}$ and $T=3(3600)=10800\,\mathrm{s}$, where $I$ is the supplied current and $T$ is duration.
2. Battery absorbed power is $p_b=-VI=-(9)(0.150)=-1.35\,\mathrm{W}$ because the current leaves its positive terminal; $V$ is its terminal voltage.
3. Energy supplied is $E_{\mathrm{sup}}=-p_bT=(1.35)(10800)=14580\,\mathrm{J}$.

**Answer:** **Answer: $E_{\mathrm{sup}}=14.58\,\mathrm{kJ}$ delivered by the battery.** Power, unit conversion, and energy arithmetic were checked with math_evaluate. The boom box has no specified resistive model, so no resistor simulation is assumed.

</details>

**Problem: Assessment AP 1.7** (introductory)

A DC transmission line runs at $800\,\mathrm{kV}$ and carries $1.8\,\mathrm{kA}$. At the Oregon end, current leaves the upper terminal, which is the $+$ terminal. Find the power at the Oregon end and say which way energy flows.

```schematic
terminal 0,3 "+" left
terminal 0,0 "−" left
wire 0,3 -> 5,3
wire 0,0 -> 5,0
X1 5,3 -> 5,0 "line" i="$1.8\,\mathrm{kA}$" flip
gap 1.5,3 -> 1.5,0 v="$800\,\mathrm{kV}$"
```

<details><summary>Solution</summary>

1. Use the current direction before multiplying. Current leaves the positive terminal, so Oregon-end absorbed power is $p_O=-VI$, where $V=800000\,\mathrm{V}$ and $I=1800\,\mathrm{A}$.
2. Substitute $p_O=-(800000)(1800)=-1.44\times10^9\,\mathrm{W}=-1440\,\mathrm{MW}$.
3. Negative absorbed power means delivery from this port.

**Answer:** **Answer: $p_O=-1440\,\mathrm{MW}$; $1440\,\mathrm{MW}$ is supplied at Oregon and transmitted toward California.** This matches the official assessment solution and was checked with math_evaluate. No resistive line model is provided.

</details>

**Problem: Textbook P1.8** (intermediate)

No charge has entered the left terminal of element $X$ before $t=0$. From $t=0$ the current $i(t)=25e^{-1000t}\,\mathrm{mA}$ enters that terminal ($t$ in seconds).

1. Find the transferred charge $q(t)$ for $t>0$.
2. Find the total charge if the current flows indefinitely.
3. Find the charge if the current is stopped at $t=1\,\mathrm{ms}$.

```schematic
terminal 0,0 left
X1 0,0 -> 4,0 "$X$" i="$i(t)$"
terminal 4,0 right
```

<details><summary>Solution</summary>

1. Choose integration because current is the rate of transferred charge. In amperes, $i(t)=0.025e^{-1000t}\,\mathrm{A}$.
2. Integrate with the initial value: $q(t)=q(0)+\int_0^t0.025e^{-1000\tau}\,d\tau=(\dfrac{0.025}{1000})(1-e^{-1000t})\,\mathrm{C}$.
3. Let the exponential tend to zero as $t\to\infty$.
4. Convert the stopping time to $0.001\,\mathrm{s}$: $q(0.001)=25(1-e^{-1})\,\mu\mathrm{C}$.

**Answer:** **(a) $q(t)=25(1-e^{-1000t})\,\mu\mathrm{C}$ for $t>0$.**

**(b) $q(\infty)=25\,\mu\mathrm{C}$.**

**(c) $q(1\,\mathrm{ms})\approx15.803\,\mu\mathrm{C}$.** After stopping, transferred charge stays at that value. Differentiating the proposed antiderivative with math_evaluate recovered the given current; the limiting and stopping-time arithmetic were also checked.

</details>

**Problem: Textbook P2.12** (intermediate)

1. Find $v$.
2. Find the power absorbed by the resistor.
3. Reverse the current source and repeat.

```schematic
I1 0,3 -> 0,0 "$75\,\mathrm{mA}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$8\,\mathrm{k\Omega}$" v="$v$"
wire 3,0 -> 0,0
```

<details><summary>Solution</summary>

1. The source sets branch current, so first determine the resistor current. The two-branch circuit must return the source current through the resistor: $i_R+0.075=0$, giving $i_R=-0.075\,\mathrm{A}$.
2. The resistor references obey PSC. With $R=8000\,\Omega$, $v=Ri_R=(8000)(-0.075)=-600\,\mathrm{V}$.
3. Compute resistor absorption: $p_R=Ri_R^2=(8000)(0.075)^2=45\,\mathrm{W}$. The source absorbed power is $p_s=v(0.075)=-45\,\mathrm{W}$, so power balances.
4. Reversing the arrow gives source current $-0.075\,\mathrm{A}$ in the retained downward reference, hence $i_R=+0.075\,\mathrm{A}$ and $v=+600\,\mathrm{V}$.
5. The squared current is unchanged: $p_R=45\,\mathrm{W}$ and $p_s=-45\,\mathrm{W}$.

**Answer:** **Original-arrow answers: $v=-600\,\mathrm{V}$ and $p_R=45\,\mathrm{W}$ absorbed.**

**Reversed-arrow answers: $v=+600\,\mathrm{V}$ and $p_R=45\,\mathrm{W}$ absorbed.** Both cases passed circuit_validate and circuit_simulate; simulated resistor currents, voltages, and powers agree, with zero current-equation residual and zero signed power imbalance.

</details>

**Problem: Textbook P2.6** (intermediate)

1. What value of $\alpha$ makes this connection valid? Give its units.
2. For that $\alpha$, find the power of the $25\,\mathrm{V}$ source.

```schematic
I1 0,3 -> 0,0 "$15\,\mathrm{A}$"
G1 0,3 -> 4,3 "$\alpha v_x$"
V1 4,0 -> 4,3 "$25\,\mathrm{V}$" v_rev="$v_x$"
wire 4,0 -> 0,0
```

<details><summary>Solution</summary>

1. Use source constraints and continuity of current in the single path. The voltage source gives $v_x=V_b-V_0=-25\,\mathrm{V}$.
2. At $a$, both source arrows leave the node, so compatibility requires $15+\alpha v_x=0$. Thus $\alpha=\dfrac{-15\,\mathrm{A}}{-25\,\mathrm{V}}=0.6\,\mathrm{A/V}$. A negative dependent-source current means actual flow opposes its arrow.
3. At $b$, the retained voltage-source current is $i_x=\alpha v_x=-15\,\mathrm{A}$.
4. The current reference enters the negative voltage-source terminal. Its signed absorbed power is $p_{25}=-(25\,\mathrm{V})i_x=-25(-15)=375\,\mathrm{W}$.

**Answer:** **(a) $\alpha=0.6\,\mathrm{S}$, a transconductance.**

**(b) The $25\,\mathrm{V}$ source absorbs $375\,\mathrm{W}$** (equivalently, its delivered power is $-375\,\mathrm{W}$). The algebra was checked with math_evaluate and agrees with the official Tutorial P2.6 solution. The simulator’s supported language excludes dependent sources, so this is an algebraic verification; no dependent-source simulation is claimed.

</details>

**Problem: Assessment AP 1.6** (advanced)

An element has $v(t)=80\,000\,te^{-500t}\,\mathrm{V}$ and $i(t)=15\,te^{-500t}\,\mathrm{A}$ for $t\ge0$ ($t$ in seconds), with the references below; both are zero for $t<0$. Find:

1. the time of maximum absorbed power;
2. that maximum power;
3. the total energy absorbed.

```schematic
terminal 0,3 left
X1 0,3 -> 0,0 "$X$" v="$v(t)$" i="$i(t)$"
terminal 0,0 left
```

<details><summary>Solution</summary>

1. The references obey PSC, so multiply the waveforms: $p(t)=v(t)i(t)=1200000t^2e^{-1000t}\,\mathrm{W}$ when $t$ is in seconds. Use differentiation for the peak and integration for energy.
2. Differentiate: $p'(t)=2400000t e^{-1000t}(1-500t)$. For $t>0$, the exponential and $t$ are positive, so the derivative changes from positive to negative at $1-500t=0$. Also $p(0)=0$ and $p(t)\to0$ as $t\to\infty$, confirming a global maximum.
3. Evaluate $p(0.002)=1200000(0.002)^2e^{-2}=0.649609\ldots\,\mathrm{W}$.
4. Total energy is $W_{\mathrm{tot}}=\int_0^\infty1200000t^2e^{-1000t}\,dt$. An antiderivative is $F(t)=-1200000e^{-1000t}(\dfrac{t^2}{1000}+\dfrac{2t}{1000000}+\dfrac{2}{1000000000})$. It follows from integration by parts twice; differentiating it recovers $p(t)$.
5. The exponential makes $F(\infty)=0$, while $F(0)=-0.0024\,\mathrm{J}$. Hence $W_{\mathrm{tot}}=F(\infty)-F(0)=0.0024\,\mathrm{J}$.

**Answer:** **(a) $t_{\max}=\dfrac{1}{500}\,\mathrm{s}=2\,\mathrm{ms}$.**

**(b) $p_{\max}\approx649.6\,\mathrm{mW}$ absorbed.**

**(c) $W_{\mathrm{tot}}=2.4\,\mathrm{mJ}$ absorbed.** The derivative, peak equation, peak value, antiderivative, and energy arithmetic were checked with math_evaluate and match the official assessment solution. This is a time-varying unspecified element, not a resistive DC operating-point problem.

</details>

## Summary

- Current is signed charge-flow rate; integrating current gives transferred charge, including the initial value.
- Voltage measures energy per charge between two terminals; power is energy-transfer rate.
- Current reference entering plus gives $p_{\mathrm{abs}}=vi$; entering minus gives $p_{\mathrm{abs}}=-vi$. Negative absorbed power means delivery.
- Physical power is independent of reference choices, and a complete circuit must balance total delivered and absorbed power.
- An ideal voltage source fixes voltage; an ideal current source fixes current. A dependent source additionally needs a signed control variable and gain with correct units.
- For a positive linear resistor, $v=Ri$ under PSC and $p_R=Ri^2=\dfrac{v^2}{R}\geq0$. Its conductance is $G=\dfrac{1}{R}$.
- An ideal short fixes zero voltage; an ideal open fixes zero current. The other variable need not vanish.
- Kirchhoff’s laws link element equations: signed currents balance at a node and signed voltage changes balance around a loop.

### Formula sheet

| Result | Formula | Use when |
|---|---|---|
| Charge and current | $i=\dfrac{dq}{dt}$; $\Delta q=\int_{t_1}^{t_2}i(\tau)\,d\tau$ | Converting a signed charge waveform into current or accumulating transferred charge. |
| Voltage | $v=\dfrac{dw}{dq}$; $v_{ab}=V_a-V_b$ | Relating energy per charge or defining a terminal polarity. |
| Energy and power | $p=\dfrac{dw}{dt}$; $\Delta w=\int_{t_1}^{t_2}p(\tau)\,d\tau$ | Finding a rate or net absorbed energy; constant power gives power times duration. |
| Absorbed power | $p_{\mathrm{abs}}=vi$ (enters plus); $p_{\mathrm{abs}}=-vi$ (enters minus) | Computing signed element power from chosen terminal references. |
| Power balance | $\sum_kp_{\mathrm{abs},k}=0$ | Checking a complete circuit’s energy accounting. |
| Ideal source constraints | $v_{ab}=v_s$; $i_{a\to b}=i_s$ | A voltage source or current source fixes the corresponding terminal variable. |
| Dependent sources | $v_s=\mu v_x$; $v_s=r_mi_x$; $i_s=\beta i_x$; $i_s=g_mv_x$ | The output depends on a signed control; gain units follow the output/control ratio. |
| Conductance and Ohm’s law | $G=\dfrac{1}{R}$; $v=Ri$; $i=Gv$ | Finite positive resistor with current entering the plus terminal; reverse the sign for the opposite arrow. |
| Resistor power | $p_R=Ri^2=\dfrac{v^2}{R}=Gv^2$ | Positive resistor; choose the known voltage or current. |
| Open and short | Open: $i=0$; short: $v=0$ | Applying ideal switch constraints directly. |
| Kirchhoff bridge | $\sum_{\mathrm{node}}i_k=0$; $\sum_{\mathrm{loop}}v_k=0$ | Connecting element relations with consistent node and loop signs. |
