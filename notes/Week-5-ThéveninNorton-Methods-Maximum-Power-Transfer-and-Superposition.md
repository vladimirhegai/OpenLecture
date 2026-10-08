# Week 5: Thévenin/Norton Methods, Maximum Power Transfer and Superposition

## Overview

> **Info:** This week covers Thévenin and Norton equivalents for linear resistive networks, including dependent sources. Test-source analysis also handles zero open-circuit voltage. For a finite positive $R_{Th}$ and an adjustable resistive load, maximum power occurs at $R_L=R_{Th}$. Superposition then separates the contributions of independent sources.

- Find Thévenin and Norton equivalents with the four lecture methods, and choose a method based on the kinds of sources in the network.
- Convert between the Thévenin and Norton forms using $V_{Th}=v_{oc}$, $I_N=i_{sc}$ and $R_{Th}=R_N=\dfrac{v_{oc}}{i_{sc}}$.
- Use a test source to find $R_{Th}$ when the network has dependent sources, including the case $V_{Th}=0$.
- Derive the maximum power transfer condition $R_L=R_{Th}$ and compute $p_{\max}=\dfrac{V_{Th}^2}{4R_{Th}}$ and the resulting efficiency.
- Apply superposition by turning off independent sources one at a time while keeping dependent sources active, and explain why power does not superpose.

## Topic 1: Thévenin and Norton equivalents — four methods

A load connected to terminals $a$–$b$ cannot tell what is inside the network it is plugged into; it only sees the relationship between the terminal voltage and the terminal current. For a linear network that relationship is a straight line, and a straight line needs only two numbers. The Thévenin form stores them as a voltage source in series with a resistor, and the Norton form stores them as a current source in parallel with a resistor.

### The two equivalent circuits

| Quantity | Meaning |
|---|---|
| $v_{oc}$ | Open-circuit voltage $v_{ab}$ with nothing connected to the terminals |
| $i_{sc}$ | Short-circuit current from $a$ to $b$ through a wire placed across the terminals |
| $V_{Th}$ | Thévenin source voltage, equal to $v_{oc}$ |
| $I_N$ | Norton source current, equal to $i_{sc}$ |
| $R_{Th}=R_N$ | Equivalent resistance seen from the terminals, equal to $\dfrac{v_{oc}}{i_{sc}}$ when $i_{sc}\ne0$; otherwise use a test source |

```schematic
V1 0,3 -> 0,0 "$V_{Th}$"
R1 0,3 -> 3,3 "$R_{Th}$"
wire 0,0 -> 3,0
terminal 3,3 "a" right
terminal 3,0 "b" right
I1 6,0 -> 6,3 "$I_N$"
wire 6,3 -> 8,3
R2 8,3 -> 8,0 "$R_N$"
wire 6,0 -> 8,0
wire 8,3 -> 10,3
wire 8,0 -> 10,0
terminal 10,3 "a" right
terminal 10,0 "b" right
```

$$V_{Th}=v_{oc},\qquad I_N=i_{sc},\qquad R_{Th}=R_N=\frac{v_{oc}}{i_{sc}},\qquad v_o=V_{Th}-R_{Th}\,i_o$$

Here $v_o=v_{ab}$ and $i_o$ leaves $a$ into a load, giving $v_o=V_{Th}-R_{Th}i_o$. The relation $v_{oc}=R_{Th}i_{sc}$ holds when these quantities are finite. The ratio determines $R_{Th}$ only when $i_{sc}\ne0$: if both source responses are zero, measure the slope with a test source. Likewise, $R_{Th}=0$ needs special treatment for Norton conversion.

### Choosing a method

The lecture gives four ways to get two of the three quantities. Which ones are allowed depends on whether the network contains independent sources, dependent sources, or both.

| Method | What you compute | Independent sources only | Independent + dependent | Dependent sources only |
|---|---|---|---|---|
| 1. Two analyses | $v_{oc}$ and $i_{sc}$, then $R_{Th}=\dfrac{v_{oc}}{i_{sc}}$ | Yes if $i_{sc}\ne0$ | Yes if $i_{sc}\ne0$ | No ($v_{oc}=i_{sc}=0$) |
| 2. Deactivate sources | $R_{eq}$ by series/parallel reduction, plus $v_{oc}$ or $i_{sc}$ | Yes | No | No |
| 3. Test source | $R_{Th}=\dfrac{v_T}{i_T}$ with independent sources off | Yes | Yes | Yes (the only option) |
| 4. Test source as a variable | One analysis giving $v_T=R_{Th}\,i_T+V_{Th}$ | Yes | Yes | Yes, when a finite unique port relation exists |

> **Tip:** Resistors and independent sources only: deactivate the sources and reduce (Method 2), then find whichever of $v_{oc}$ or $i_{sc}$ is easier. Dependent sources present: use $\dfrac{v_{oc}}{i_{sc}}$ (Method 1) or a test source (Methods 3 and 4). Dependent sources only: $V_{Th}=0$, so only the test-source methods give $R_{Th}$.

> **Warning:** Deactivate independent voltage sources with shorts and independent current sources with opens. Keep dependent sources and their control relations. Plain series/parallel resistor reduction generally does not determine the resistance of a network with dependent sources; use circuit analysis with a test source.

**Example: Lecture example · Thévenin and Norton by two analyses**

Find the Thévenin and Norton equivalents at terminals $a$–$b$ of the network below.

```schematic
V1 0,3 -> 0,0 "$25\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\Omega$"
R2 3,3 -> 3,0 "$20\,\Omega$"
wire 3,3 -> 5,3
I1 5,0 -> 5,3 "$3\,\mathrm{A}$"
R3 5,3 -> 8,3 "$4\,\Omega$"
wire 0,0 -> 8,0
terminal 8,3 "a" right
terminal 8,0 "b" right
label 3,3 "$v_1$" above
ground 3,0
```

1. Find $V_{Th}$ from the open-circuit voltage.
2. Find $i_{sc}$ and $R_{Th}$.
3. Check $R_{Th}$ by deactivating the sources, and state the Norton equivalent.

1. With $a$–$b$ open, no current flows in the $4\,\Omega$ resistor, so $v_{oc}=v_1$. Write KCL at $v_1$ (currents leaving), with the $3\,\mathrm{A}$ source pushing current into the node.

   $$\begin{aligned}\frac{v_1-25}{5}+\frac{v_1}{20}-3&=0\\ v_1&=32\,\mathrm{V}=V_{Th}\end{aligned}$$
2. Short $a$ to $b$. The $4\,\Omega$ resistor now runs from the node (call its voltage $v_2$) to the reference, and its current is $i_{sc}$.

   $$\begin{aligned}\frac{v_2-25}{5}+\frac{v_2}{20}+\frac{v_2}{4}-3&=0\\ v_2&=16\,\mathrm{V},\qquad i_{sc}=\frac{v_2}{4}=4\,\mathrm{A}\end{aligned}$$
3. The two analyses give the resistance directly.

   $$R_{Th}=\frac{v_{oc}}{i_{sc}}=\frac{32}{4}=8\,\Omega$$
4. Check with Method 2: short the $25\,\mathrm{V}$ source and open the $3\,\mathrm{A}$ source, then look into $a$–$b$.

   $$R_{eq}=(5\parallel 20)+4=4+4=8\,\Omega$$
5. The Norton source is the short-circuit current, with the same resistance in parallel.

   $$I_N=i_{sc}=4\,\mathrm{A},\qquad R_N=R_{Th}=8\,\Omega$$

**Answer:** **(a)** $V_{Th}=32\,\mathrm{V}$. **(b)** $i_{sc}=4\,\mathrm{A}$, $R_{Th}=8\,\Omega$. **(c)** $(5\parallel20)+4=8\,\Omega$ confirms $R_{Th}$; the Norton equivalent is a $4\,\mathrm{A}$ source (arrow toward $a$) in parallel with $8\,\Omega$.

### Networks with dependent sources

A dependent source cannot be switched off, so the resistance has to be measured the way an instrument would measure it. Connect a test source to $a$–$b$, let the network respond, and take the ratio of terminal voltage to terminal current. If the network has no independent sources, nothing drives it when the terminals are open, so $V_{Th}=0$; the dependent source can still make $R_{Th}$ negative.

$$R_{Th}=\frac{v_T}{i_T}\quad(\text{independent sources off}),\qquad v_T=R_{Th}\,i_T+V_{Th}\quad(\text{all sources on})$$

Here $v_T$ is the test-source voltage across $a$–$b$ (+ at $a$) and $i_T$ is the test current entering the network at $a$. Method 3 turns the independent sources off and uses the left formula. Method 4 keeps every source on and solves for $v_T$ as a function of $i_T$: the slope of that line is $R_{Th}$ and its intercept at $i_T=0$ is $V_{Th}$, so one analysis gives the whole equivalent.

**Example: Lecture example · Test source on a dependent-only network**

The network below contains only a dependent source, so a test source $v_T$ is connected at $a$ and drives a current $i_T$ into the network.

```schematic
E1 0,3 -> 0,0 "$12i_\Delta$"
R1 0,3 -> 3,3 "$2\,\Omega$"
R2 3,3 -> 3,0 "$4\,\Omega$" i="$i_\Delta$"
wire 3,3 -> 6,3
V1 6,3 -> 6,0 "$v_T$" i_rev="$i_T$"
wire 0,0 -> 6,0
label 3,3 "a" above
ground 0,0
```

1. Find $V_{Th}$.
2. Find $R_{Th}=\dfrac{v_T}{i_T}$.

1. With the test source removed, the network has no independent source, so every voltage and current is zero and $V_{Th}=0$. For the same reason $i_{sc}=0$, so $\dfrac{v_{oc}}{i_{sc}}$ is undefined and a test source is the only way to get $R_{Th}$.

   $$V_{Th}=0$$
2. The controlling current flows down through the $4\,\Omega$ resistor, which has $v_T$ across it.

   $$i_\Delta=\frac{v_T}{4}$$
3. KCL at $a$: the test current plus the current arriving through the $2\,\Omega$ resistor equals the current leaving through the $4\,\Omega$ resistor.

   $$i_T+\frac{12i_\Delta-v_T}{2}=i_\Delta$$
4. Substitute $i_\Delta=\dfrac{v_T}{4}$ and collect terms.

   $$\begin{aligned}i_T+\frac{3v_T-v_T}{2}&=\frac{v_T}{4}\\ i_T&=-\frac{3}{4}v_T\end{aligned}$$
5. Take the ratio.

   $$R_{Th}=\frac{v_T}{i_T}=-\frac{4}{3}\,\Omega$$

**Answer:** **(a)** $V_{Th}=0$. **(b)** $R_{Th}=-\tfrac{4}{3}\,\Omega\approx-1.33\,\Omega$. The resistance is negative because the dependent source supplies power.

**Example: Lecture example · One analysis with a test source (Method 4)**

The loop on the left sets the controlling current $i$; the right part contains the dependent current source $20i$ and the controlling voltage $v$. The two parts share only the bottom wire. A test source $v_T$ is applied at $a$, driving $i_T$ into the network.

```schematic
V1 0,3 -> 0,0 "$5\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\mathrm{k}\Omega$" i="$i$"
E1 3,3 -> 3,0 "$3v$"
G1 6,3 -> 6,0 "$20i$"
wire 6,3 -> 8,3
R2 8,3 -> 8,0 "$25\,\Omega$" v="$v$"
wire 8,3 -> 10,3
V2 10,3 -> 10,0 "$v_T$" i_rev="$i_T$"
wire 0,0 -> 10,0
label 8,3 "a" above
ground 0,0
```

1. Express $v_T$ in terms of $i_T$ with all sources on.
2. Read off $V_{Th}$ and $R_{Th}$, and find $i_{sc}$.

1. KCL at $a$: $i_T$ enters, $20i$ leaves through the dependent source, and the rest flows down the $25\,\Omega$ resistor, whose voltage is $v=v_T$.

   $$v_T=v=25\,(i_T-20i)$$
2. KVL around the left loop gives the controlling current.

   $$5=2000\,i+3v\quad\Rightarrow\quad i=\frac{5-3v_T}{2000}$$
3. Substitute and solve for $v_T$.

   $$\begin{aligned}v_T&=25\,i_T-\frac{500\,(5-3v_T)}{2000}=25\,i_T-1.25+0.75\,v_T\\ v_T&=100\,i_T-5\end{aligned}$$
4. Compare with $v_T=R_{Th}\,i_T+V_{Th}$; the short-circuit current follows from $i_{sc}=\dfrac{V_{Th}}{R_{Th}}$.

   $$R_{Th}=100\,\Omega,\qquad V_{Th}=-5\,\mathrm{V},\qquad i_{sc}=\frac{-5}{100}=-50\,\mathrm{mA}$$

**Answer:** **(a)** $v_T=100\,i_T-5$ (volts, with $i_T$ in amperes). **(b)** $V_{Th}=-5\,\mathrm{V}$, $R_{Th}=100\,\Omega$, $i_{sc}=-50\,\mathrm{mA}$. The equivalent is a $5\,\mathrm{V}$ source with its + terminal toward $b$, in series with $100\,\Omega$.

> **Warning:** When you split a circuit into a network and its load, or replace part of a circuit by its Thévenin equivalent, every dependent source must stay in the same part as the voltage or current that controls it. If the controlling variable lies in the part you replace, the equivalent no longer knows what value to give the dependent source, and the answer is wrong.

## Topic 2: Maximum power transfer

Assume a finite Thévenin equivalent with $R_{Th}>0$ and an adjustable passive load $R_L\ge0$. A small load has little voltage, while a large load has little current, so load power approaches zero at both limits and has an interior maximum. The matching result below does not give a finite passive-load maximum for negative $R_{Th}$.

### Deriving the condition

```schematic
V1 0,3 -> 0,0 "$V_{Th}$"
R1 0,3 -> 3,3 "$R_{Th}$"
R2 3,3 -> 3,0 "$R_L$" i="$i$" v="$v_L$"
wire 0,0 -> 3,0
label 3,3 "a" above
ground 0,0
```

**Load resistance for maximum power**

1. The load is in series with $R_{Th}$, so the loop current is

   $$i=\frac{V_{Th}}{R_{Th}+R_L}$$
2. The power absorbed by the load is $i^2R_L$.

   $$p_L=i^2R_L=\frac{V_{Th}^2\,R_L}{(R_{Th}+R_L)^2}$$
3. Differentiate with respect to $R_L$ (quotient rule); $V_{Th}$ and $R_{Th}$ are fixed by the network.

   $$\frac{dp_L}{dR_L}=V_{Th}^2\,\frac{(R_{Th}+R_L)^2-2R_L(R_{Th}+R_L)}{(R_{Th}+R_L)^4}=V_{Th}^2\,\frac{R_{Th}-R_L}{(R_{Th}+R_L)^3}$$
4. The derivative is zero only when the numerator vanishes. It is positive below this value and negative above it, so this is a maximum. This assumes $R_{Th}>0$ and $V_{Th}\ne0$; when $V_{Th}=0$ the power is zero for every nonsingular passive load.

   $$R_L=R_{Th}$$
5. Substitute $R_L=R_{Th}$ back into $p_L$.

   $$p_{\max}=\frac{V_{Th}^2\,R_{Th}}{(2R_{Th})^2}=\frac{V_{Th}^2}{4R_{Th}}$$

$$R_L=R_{Th},\qquad p_{\max}=\frac{V_{Th}^2}{4R_{Th}}=\frac{R_{Th}\,I_N^2}{4}$$

For $R_{Th}>0$, the matched adjustable load is $R_L=R_{Th}$ and receives $p_{\max}=\dfrac{V_{Th}^2}{4R_{Th}}$. The Norton expression uses $V_{Th}=R_{Th}I_N$. Half the Thévenin voltage appears across the matched load. These statements require a finite equivalent and a positive resistance.

### Using the result

> **Warning:** Maximum power transfer is not maximum efficiency. At $R_L=R_{Th}$ the Thévenin resistance dissipates as much as the load, and the real sources inside the network may waste even more. Also, the condition assumes the load is the adjustable element: if instead a resistor in series with a fixed load is adjustable, as in Textbook P4.84, the load power is largest when that series resistance is zero.

**Example: Lecture example · Maximum power from a two-source network**

The load $R_L$ is adjustable.

```schematic
V1 0,0 -> 0,3 "$v_{S2}=3\,\mathrm{V}$"
I1 0,3 -> 0,6 "$i_{S1}=2\,\mathrm{mA}$"
wire 0,6 -> 8,6
R2 0,3 -> 3,3 "$R_2=3\,\mathrm{k}\Omega$"
wire 3,3 -> 4,3
R1 4,6 -> 4,3 "$R_1=4\,\mathrm{k}\Omega$"
R3 4,3 -> 4,0 "$R_3=6\,\mathrm{k}\Omega$"
R4 8,6 -> 8,3 "$R_L$"
wire 8,3 -> 8,0
wire 0,0 -> 8,0
label 8,6 "a" above
label 4,3 "m" right
label 0,3 "c" left
ground 4,0
```

1. Find the Thévenin equivalent at $a$–$b$ ($b$ is the bottom rail).
2. Choose $R_L$ for maximum power and find $(p_{R_L})_{\max}$.

1. Remove $R_L$ and use mesh currents (both clockwise). The current source is alone on the outer branch, so the left mesh current is known: $i_1=i_{S1}=2\,\mathrm{mA}$.

   $$i_1=i_{S1}=2\,\mathrm{mA}$$
2. KVL around the lower mesh through $v_{S2}$, $R_2$ and $R_3$ (resistances in $\mathrm{k}\Omega$ give currents in $\mathrm{mA}$).

   $$\begin{aligned}v_{S2}+R_2(i_2-i_1)+R_3i_2&=0\\ i_2=\frac{R_2i_{S1}-v_{S2}}{R_2+R_3}=\frac{6-3}{9}&=\tfrac{1}{3}\,\mathrm{mA}\end{aligned}$$
3. The open-circuit voltage is the drop from $a$ through $R_1$ and $R_3$ to $b$.

   $$v_{oc}=R_1i_1+R_3i_2=4(2)+6\left(\tfrac{1}{3}\right)=10\,\mathrm{V}$$
4. Deactivate: the current source opens and the voltage source becomes a short, so $R_2$ and $R_3$ both run from $m$ to $b$.

   $$R_{Th}=R_1+(R_2\parallel R_3)=4+2=6\,\mathrm{k}\Omega$$
5. Match the load and evaluate the maximum power.

   $$R_L=6\,\mathrm{k}\Omega,\qquad (p_{R_L})_{\max}=\frac{10^2}{4(6000)}=\frac{25}{6}\,\mathrm{mW}\approx4.17\,\mathrm{mW}$$

**Answer:** **(a)** $V_{Th}=10\,\mathrm{V}$, $R_{Th}=6\,\mathrm{k}\Omega$. **(b)** $R_L=6\,\mathrm{k}\Omega$ and $(p_{R_L})_{\max}=\dfrac{25}{6}\,\mathrm{mW}\approx4.17\,\mathrm{mW}$.

**Example: Lecture example · Maximum power is not maximum efficiency**

A $360\,\mathrm{V}$ source feeds an adjustable load $R_L$ through the resistor network below.

```schematic
V1 0,3 -> 0,0 "$360\,\mathrm{V}$"
R1 0,3 -> 3,3 "$30\,\Omega$"
R2 3,3 -> 3,0 "$150\,\Omega$"
wire 3,3 -> 6,3
R3 6,3 -> 6,0 "$R_L$"
wire 0,0 -> 6,0
label 3,3 "a" above
ground 0,0
```

1. Find $R_L$ for maximum power transfer.
2. Find the maximum power delivered to $R_L$.
3. Find the percentage of the source power that reaches $R_L$ at this setting.

1. Thévenin equivalent at $a$–$b$: a voltage divider for $V_{Th}$, and $30\,\Omega\parallel150\,\Omega$ with the source shorted.

   $$V_{Th}=360\cdot\frac{150}{180}=300\,\mathrm{V},\qquad R_{Th}=30\parallel150=25\,\Omega$$
2. Match the load and apply $p_{\max}=\dfrac{V_{Th}^2}{4R_{Th}}$.

   $$R_L=25\,\Omega,\qquad p_{\max}=\frac{300^2}{4(25)}=900\,\mathrm{W}$$
3. Go back to the original circuit with $R_L=25\,\Omega$: half of $V_{Th}$ is across the load, and the source current follows from the $30\,\Omega$ drop.

   $$v_{ab}=\frac{V_{Th}}{2}=150\,\mathrm{V},\qquad i_s=\frac{360-150}{30}=7\,\mathrm{A},\qquad p_s=360(7)=2520\,\mathrm{W}$$
4. Power balance check, then the efficiency.

   $$\begin{aligned}p_{30}+p_{150}+p_L&=7^2(30)+\frac{150^2}{150}+900=1470+150+900=2520\,\mathrm{W}\\ \eta&=\frac{900}{2520}=35.7\%\end{aligned}$$

**Answer:** **(a)** $R_L=25\,\Omega$. **(b)** $p_{\max}=900\,\mathrm{W}$. **(c)** The source delivers $2520\,\mathrm{W}$, so only $35.7\%$ reaches the load.

> **Tip:** For maximum power problems, always find the Thévenin equivalent first, using whichever Topic 1 method fits the sources. Then go back to the original circuit for anything about the internal sources (power supplied, efficiency), because the equivalent only describes behaviour at the terminals.

## Topic 3: Superposition

In these linear resistive circuits, each output voltage or current is a weighted sum of independent source values, with weights set by the resistances and dependent-source gains. Turn off the other independent sources and sum the signed contributions. Superposition also applies to linear dynamic circuits, but nonzero initial stored energy contributes a natural response that must be included once, not duplicated in every source contribution.

### The principle

$$y=\sum_{k=1}^{n}y_k=y_1+y_2+\cdots+y_n$$

Here $y$ is any branch voltage or current in the full circuit, $n$ is the number of independent sources, and $y_k$ is the value of that same variable when only independent source $k$ is on. Keep the reference direction of $y$ the same in every sub-circuit, so that the signs add correctly.

| Element | In each one-source sub-circuit | Reason |
|---|---|---|
| Independent voltage source (off) | Short circuit | Turning it off sets $v=0$ |
| Independent current source (off) | Open circuit | Turning it off sets $i=0$ |
| Dependent source | Stays in the circuit | Its value is set by a variable in the sub-circuit |
| Resistors | Unchanged | They set the weights $\dfrac{y_k}{\text{source}}$ |

**Example: Lecture example · Superposition with two independent sources**

Use superposition to find $v_o$ and $i_o$.

```schematic
V1 0,3 -> 0,0 "$v_{S1}=120\,\mathrm{V}$"
R1 0,3 -> 3,3 "$6\,\Omega$"
R3 3,3 -> 3,0 "$3\,\Omega$" i="$i_o$"
R2 3,3 -> 6,3 "$2\,\Omega$"
R4 6,3 -> 6,0 "$4\,\Omega$" v="$v_o$"
wire 6,3 -> 9,3
I1 9,3 -> 9,0 "$i_{S2}=12\,\mathrm{A}$"
wire 0,0 -> 9,0
label 3,3 "$v_1$" above
label 6,3 "$v_2$" above
ground 0,0
```

1. Find the contributions of $v_{S1}$ alone.
2. Find the contributions of $i_{S2}$ alone.
3. Add them to get $v_o$ and $i_o$.

1. $v_{S1}$ alone: open the current source. The $2\,\Omega$ and $4\,\Omega$ resistors are in series ($6\,\Omega$) and in parallel with $3\,\Omega$, giving $2\,\Omega$; the source sees $6+2=8\,\Omega$.

   $$i'_{S1}=\frac{120}{8}=15\,\mathrm{A},\qquad v'_1=15(2)=30\,\mathrm{V}$$
2. Split $v'_1$ to get the two outputs.

   $$i'_o=\frac{30}{3}=10\,\mathrm{A},\qquad v'_o=30\cdot\frac{4}{2+4}=20\,\mathrm{V}$$
3. $i_{S2}$ alone: short the voltage source. The source draws $12\,\mathrm{A}$ out of $v_2$. From $v_2$ the circuit looks like $4\,\Omega$ in parallel with $2+(6\parallel3)=4\,\Omega$, i.e. $2\,\Omega$.

   $$v''_o=-12(2)=-24\,\mathrm{V}$$
4. The $2\,\Omega$ branch carries half of the $12\,\mathrm{A}$, and $v''_1$ follows from a divider on the $4\,\Omega$ branch.

   $$v''_1=v''_o\cdot\frac{2}{2+2}=-12\,\mathrm{V},\qquad i''_o=\frac{-12}{3}=-4\,\mathrm{A}$$
5. Add the contributions. A DC simulation of the full circuit gives the same values ($v_1=18\,\mathrm{V}$). Note: the summary on lecture slide 33 swaps the two final expressions; the correct ones are $v_o=\dfrac{v_{S1}}{6}-2i_{S2}$ and $i_o=\dfrac{v_{S1}}{12}-\dfrac{i_{S2}}{3}$.

   $$\begin{aligned}v_o&=v'_o+v''_o=20-24=-4\,\mathrm{V}\\ i_o&=i'_o+i''_o=10-4=6\,\mathrm{A}\end{aligned}$$

**Answer:** **(a)** $v'_o=20\,\mathrm{V}$, $i'_o=10\,\mathrm{A}$. **(b)** $v''_o=-24\,\mathrm{V}$, $i''_o=-4\,\mathrm{A}$. **(c)** $v_o=-4\,\mathrm{V}$, $i_o=6\,\mathrm{A}$.

### Dependent sources and power

Dependent sources are part of the circuit's linear "machinery", not inputs, so they stay on in every sub-circuit and simply react to whatever the remaining independent source produces. Power, however, is a product of a voltage and a current, so it is not linear in the sources.

**Example: Lecture example · Superposition with dependent sources**

Use superposition on the two independent sources to find $v_o$. Both dependent sources stay active in each step.

```schematic
V1 0,3 -> 0,0 "$V_{S1}=10\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\Omega$" i="$i_\Delta$"
R2 3,3 -> 3,0 "$20\,\Omega$" v="$v_o$"
G1 6,3 -> 3,3 "$\alpha v_\Delta$"
R3 6,3 -> 6,0 "$10\,\Omega$" v="$v_\Delta$"
E1 6,0 -> 3,0 "$\beta i_\Delta$"
I1 9,0 -> 9,3 "$5\,\mathrm{A}$"
wire 6,3 -> 9,3
wire 6,0 -> 9,0
wire 0,0 -> 3,0
label 3,3 "a" above
label 6,3 "d" above
label 6,0 "c" below
ground 3,0
```

- $V_{S1}=10\,\mathrm{V}$, $I_{S3}=5\,\mathrm{A}$
- $I_{S2}=\alpha v_\Delta$ with $\alpha=0.4\,\mathrm{A/V}$
- $V_{S4}=\beta i_\Delta$ with $\beta=2\,\Omega$

1. Find $v'_o$ with only $V_{S1}$ on.
2. Find $v''_o$ with only $I_{S3}$ on.
3. Find $v_o$.

1. $V_{S1}$ alone: open $I_{S3}$. KCL at $d$: the only currents leaving $d$ are $\alpha v_\Delta$ (to $a$) and $\dfrac{v_\Delta}{10}$ (down $R_3$), and nothing enters.

   $$0.4\,v'_\Delta+\frac{v'_\Delta}{10}=0\quad\Rightarrow\quad v'_\Delta=0,\quad \alpha v'_\Delta=0$$
2. The right-hand resistor and dependent current source carry zero current because $v_\Delta=0$. The left $5\,\Omega$ and $20\,\Omega$ resistors form a divider. The controlling current is still $i_\Delta=\dfrac{10-8}{5}=0.4\,\mathrm{A}$, so the dependent voltage source remains at $0.8\,\mathrm{V}$; it does not change this divider.

   $$v'_o=10\cdot\frac{20}{5+20}=8\,\mathrm{V}$$
3. $I_{S3}$ alone: short $V_{S1}$. KCL at $d$: $5\,\mathrm{A}$ enters from $I_{S3}$ and leaves through the dependent source and $R_3$.

   $$5=0.4\,v''_\Delta+\frac{v''_\Delta}{10}\quad\Rightarrow\quad v''_\Delta=10\,\mathrm{V},\quad \alpha v''_\Delta=4\,\mathrm{A}$$
4. The $4\,\mathrm{A}$ enters node $a$, which now sees $5\,\Omega$ (to the shorted source) in parallel with $20\,\Omega$. The voltage source $\beta i_\Delta$ only sets $v_c$ and does not change this KCL.

   $$\frac{v''_o}{5}+\frac{v''_o}{20}=4\quad\Rightarrow\quad v''_o=16\,\mathrm{V}$$
5. Add the contributions.

   $$v_o=v'_o+v''_o=8+16=24\,\mathrm{V}$$

**Answer:** **(a)** $v'_o=8\,\mathrm{V}$. **(b)** $v''_o=16\,\mathrm{V}$. **(c)** $v_o=24\,\mathrm{V}$.

$$p=(v'+v'')(i'+i'')=v'i'+v''i''+\underbrace{v'i''+v''i'}_{\text{cross terms}}\neq p'+p''$$

Here $v'$, $i'$ are an element's voltage and current from the first source alone, $v''$, $i''$ are from the second source alone, and $p'=v'i'$, $p''=v''i''$ are the powers in each sub-circuit. The cross terms are generally non-zero, so the true power is not the sum of the sub-circuit powers. Find the total $v$ and $i$ by superposition first, then compute $p=vi$.

> **Warning:** Two common superposition mistakes: (1) turning off a dependent source — only independent sources are switched off; (2) adding powers from the sub-circuits. For example, in the two-source lecture example the $4\,\Omega$ resistor absorbs $\dfrac{20^2}{4}=100\,\mathrm{W}$ and $\dfrac{(-24)^2}{4}=144\,\mathrm{W}$ in the two sub-circuits, but only $\dfrac{(-4)^2}{4}=4\,\mathrm{W}$ in the real circuit.

> **Tip:** Superposition pays off when each one-source sub-circuit collapses to dividers and series/parallel reductions, or when you need to know how much each source contributes. If the circuit has many sources or tangled dependent sources, a single nodal or mesh analysis is usually faster.

## Practice problems

Try each problem before opening the solution. The first two need only Thévenin basics, the middle ones practise superposition and dependent sources, and the last combines a dependent source with maximum power transfer. For each Thévenin problem, decide which of the four methods you will use before writing any equations.

**Problem: Assessment AP 4.16 · Thévenin equivalent of a bridge-like network** (introductory)

Find the Thévenin equivalent of the circuit with respect to terminals $a$, $b$.

```schematic
V1 0,3 -> 0,0 "$72\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\Omega$"
R2 3,3 -> 3,0 "$20\,\Omega$"
R3 3,3 -> 6,3 "$8\,\Omega$"
wire 0,3 -> 0,6 -> 2,6
R4 2,6 -> 5,6 "$12\,\Omega$"
wire 5,6 -> 6,6 -> 6,3
wire 6,3 -> 8,3
wire 0,0 -> 8,0
terminal 8,3 "a" right
terminal 8,0 "b" right
label 3,3 "$v_1$" below
ground 0,0
```

1. Find $R_{Th}$.
2. Find $v_{Th}$.

<details><summary>Solution</summary>

1. Only independent sources, so deactivate: short the $72\,\mathrm{V}$ source. Then $5\,\Omega\parallel20\,\Omega$ is in series with $8\,\Omega$, and that combination is in parallel with $12\,\Omega$.

   $$R_{Th}=12\parallel\big((5\parallel20)+8\big)=12\parallel12=6\,\Omega$$
2. Open circuit: write KCL at $v_1$ and at $a$ (currents leaving).

   $$\begin{aligned}\frac{v_1-72}{5}+\frac{v_1}{20}+\frac{v_1-v_a}{8}&=0\\ \frac{v_a-v_1}{8}+\frac{v_a-72}{12}&=0\end{aligned}$$
3. Solve the pair (a DC simulation gives the same node voltages).

   $$v_1=60\,\mathrm{V},\qquad v_{Th}=v_a=64.8\,\mathrm{V}$$

**Answer:** **(a)** $R_{Th}=6\,\Omega$. **(b)** $v_{Th}=64.8\,\mathrm{V}$.

</details>

**Problem: Textbook P4.84 · A maximum power trap** (introductory)

A $30\,\mathrm{V}$ source feeds a fixed $6\,\Omega$ resistor through a variable resistor $R_o$.

```schematic
V1 0,3 -> 0,0 "$30\,\mathrm{V}$"
R1 0,3 -> 3,3 "$R_o$"
R2 3,3 -> 3,0 "$6\,\Omega$"
wire 0,0 -> 3,0
ground 0,0
```

1. Find the value of $R_o$ that results in maximum power dissipation in the $6\,\Omega$ resistor. (Hint: hasty conclusions could be hazardous to your career.)
2. What is the maximum power that can be delivered to the $6\,\Omega$ resistor?

<details><summary>Solution</summary>

1. Here the load is fixed and the series resistance varies, so $R_L=R_{Th}$ does not apply. Write the load power directly.

   $$p_6=\left(\frac{30}{R_o+6}\right)^2(6)$$
2. This decreases steadily as $R_o$ increases, so the smallest allowed value, $R_o=0$, gives the maximum.

   $$R_o=0$$
3. Evaluate the power.

   $$p_{\max}=\frac{30^2}{6}=150\,\mathrm{W}$$

**Answer:** **(a)** $R_o=0\,\Omega$ (not $6\,\Omega$). **(b)** $p_{\max}=150\,\mathrm{W}$.

</details>

**Problem: Textbook P4.94 · Superposition with three sources** (intermediate)

Use the principle of superposition to find the current $i_o$.

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
ground 0,0
```

1. Find the contribution of each source to $i_o$.
2. Find $i_o$.

<details><summary>Solution</summary>

1. With the $75\,\mathrm{V}$ source shorted, the right-hand node sees $60\parallel5\parallel30$.

   $$R_{right}=\left(\tfrac{1}{60}+\tfrac{1}{5}+\tfrac{1}{30}\right)^{-1}=4\,\Omega$$
2. $6\,\mathrm{A}$ alone ($10\,\mathrm{A}$ open, $75\,\mathrm{V}$ shorted): current divider between $20\,\Omega$ and $1+4=5\,\Omega$.

   $$i'_o=6\cdot\frac{20}{20+5}=4.8\,\mathrm{A}$$
3. $10\,\mathrm{A}$ alone: the source draws $10\,\mathrm{A}$ from the right node; the share through the $1+20=21\,\Omega$ path flows in the direction of $i_o$.

   $$i''_o=10\cdot\frac{4}{4+21}=1.6\,\mathrm{A}$$
4. $75\,\mathrm{V}$ alone (both current sources open): nodal equation at the right node $v$, where the left side is $1+20=21\,\Omega$ to ground.

   $$\frac{v-75}{5}+\frac{v}{60}+\frac{v}{30}+\frac{v}{21}=0\;\Rightarrow\; v=50.4\,\mathrm{V},\quad i'''_o=-\frac{50.4}{21}=-2.4\,\mathrm{A}$$
5. Add the contributions (a DC simulation of the full circuit confirms $4\,\mathrm{A}$).

   $$i_o=4.8+1.6-2.4=4\,\mathrm{A}$$

**Answer:** **(a)** $6\,\mathrm{A}$ source: $4.8\,\mathrm{A}$; $10\,\mathrm{A}$ source: $1.6\,\mathrm{A}$; $75\,\mathrm{V}$ source: $-2.4\,\mathrm{A}$. **(b)** $i_o=4\,\mathrm{A}$.

</details>

**Problem: Assessment AP 4.19 · Thévenin equivalent with a dependent current source** (intermediate)

Find the Thévenin equivalent of the circuit with respect to terminals $a$, $b$.

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
wire 0,0 -> 9,0
terminal 9,3 "a" right
terminal 9,0 "b" right
ground 0,0
```

1. Find $v_{Th}$.
2. Find $R_{Th}$ with a test source.
3. Check your answer with $i_{sc}$.

<details><summary>Solution</summary>

1. Open circuit, KCL at $a$ (currents leaving): through $2\,\Omega$, through the dependent source toward the left node, through the $4\,\mathrm{A}$ source, and through $8\,\Omega$, with $i_x=\dfrac{v_a}{8}$.

   $$\frac{v_a-24}{2}+3\frac{v_a}{8}+4+\frac{v_a}{8}=0\;\Rightarrow\;v_{Th}=v_a=8\,\mathrm{V}$$
2. Test source: short the $24\,\mathrm{V}$ source, open the $4\,\mathrm{A}$ source, keep $3i_x$, and apply $v_T$ at $a$.

   $$i_T=\frac{v_T}{2}+\frac{3v_T}{8}+\frac{v_T}{8}=v_T\;\Rightarrow\;R_{Th}=\frac{v_T}{i_T}=1\,\Omega$$
3. Check: with $a$ shorted to $b$, $v_a=0$ so $i_x=0$ and the dependent source is off.

   $$i_{sc}=\frac{24}{2}-4=8\,\mathrm{A},\qquad \frac{v_{oc}}{i_{sc}}=\frac{8}{8}=1\,\Omega$$

**Answer:** **(a)** $v_{Th}=8\,\mathrm{V}$. **(b)** $R_{Th}=1\,\Omega$. **(c)** $i_{sc}=8\,\mathrm{A}$, so $\dfrac{v_{oc}}{i_{sc}}=1\,\Omega$ agrees.

</details>

**Problem: Textbook P4.93 · Superposition with a hidden balanced bridge** (intermediate)

Use the principle of superposition to find the current $i_o$ in the $45\,\mathrm{V}$ source.

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
ground 0,0
```

1. Find the contribution of each source to $i_o$.
2. Find $i_o$.

<details><summary>Solution</summary>

1. $45\,\mathrm{V}$ alone (short $10\,\mathrm{V}$, open $8\,\mathrm{A}$): $10+30=40\,\Omega$ is in parallel with $40\,\Omega$, in series with $5\,\Omega$ and $15\,\Omega$.

   $$i'_o=\frac{45}{5+(40\parallel40)+15}=\frac{45}{40}=1.125\,\mathrm{A}$$
2. $10\,\mathrm{V}$ alone (short $45\,\mathrm{V}$, open $8\,\mathrm{A}$): the source sees $10+\big(40\parallel(5+15)\big)+30=53.33\,\Omega$. The part of its current that goes through $5\,\Omega$ flows down through the shorted $45\,\mathrm{V}$ position, against $i_o$.

   $$i_{10}=\frac{10}{53.33}=0.1875\,\mathrm{A},\qquad i''_o=-0.1875\cdot\frac{40}{40+20}=-0.125\,\mathrm{A}$$
3. $8\,\mathrm{A}$ alone (both voltage sources shorted): the bridge is balanced because $\dfrac{10}{5}=\dfrac{30}{15}$, so the $40\,\Omega$ carries no current. The $8\,\mathrm{A}$ splits between the $10+5=15\,\Omega$ and $30+15=45\,\Omega$ paths.

   $$i'''_o=8\cdot\frac{45}{15+45}=6\,\mathrm{A}$$
4. Add the contributions (a DC simulation of the full circuit confirms $7\,\mathrm{A}$).

   $$i_o=1.125-0.125+6=7\,\mathrm{A}$$

**Answer:** **(a)** $45\,\mathrm{V}$: $1.125\,\mathrm{A}$; $10\,\mathrm{V}$: $-0.125\,\mathrm{A}$; $8\,\mathrm{A}$: $6\,\mathrm{A}$. **(b)** $i_o=7\,\mathrm{A}$.

</details>

**Problem: Assessment AP 4.21 · Maximum power with a dependent source** (advanced)

The variable resistor $R_o$ is adjusted for maximum power transfer. The dependent source $v_\phi$ equals the voltage across the $4\,\Omega$ resistor in series with the $20\,\mathrm{V}$ source.

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
label 8,4 "a" above
ground 0,0
```

1. Find the value of $R_o$ for maximum power transfer.
2. Find the maximum power delivered to $R_o$.

<details><summary>Solution</summary>

1. The dependent source rules out deactivation, so use $v_{oc}$ and $i_{sc}$. Call the centre node $v_1$; then $v_\phi=v_1-20$ and the top node is at $100+v_\phi=80+v_1$. Open circuit, KCL at $a$: the two $4\,\Omega$ currents into $a$ cancel.

   $$\frac{v_a-(80+v_1)}{4}+\frac{v_a-v_1}{4}=0\;\Rightarrow\;v_a=40+v_1$$
2. KCL at the centre node, then substitute $v_a$.

   $$\frac{v_1-100}{4}+\frac{v_1-v_a}{4}+\frac{v_1-20}{4}=0\;\Rightarrow\;2v_1-160=0,\;v_1=80\,\mathrm{V},\;v_{Th}=120\,\mathrm{V}$$
3. Short circuit ($v_a=0$): KCL at the centre node gives $v_1$, then add the two currents into the short.

   $$\begin{aligned}(v_1-100)+v_1+(v_1-20)&=0\;\Rightarrow\;v_1=40\,\mathrm{V}\\ i_{sc}=\frac{80+40}{4}+\frac{40}{4}&=40\,\mathrm{A}\end{aligned}$$
4. Thévenin resistance and the matched load.

   $$R_{Th}=\frac{120}{40}=3\,\Omega\;\Rightarrow\;R_o=3\,\Omega$$
5. Maximum power.

   $$p_{\max}=\frac{120^2}{4(3)}=1200\,\mathrm{W}$$

**Answer:** **(a)** $R_o=R_{Th}=3\,\Omega$ ($v_{Th}=120\,\mathrm{V}$, $i_{sc}=40\,\mathrm{A}$). **(b)** $p_{\max}=1200\,\mathrm{W}$.

</details>

## Summary

- A linear resistive port with finite equivalents has $V_{Th}=v_{oc}$ and $I_N=i_{sc}$. Use $R_{Th}=\dfrac{v_{oc}}{i_{sc}}$ when $i_{sc}\ne0$; use a test source if both are zero.
- Deactivating sources (voltage source → short, current source → open) gives $R_{Th}$ only when the network has no dependent sources.
- With dependent sources, use $\dfrac{v_{oc}}{i_{sc}}$ or a test source. A network with only dependent sources has $V_{Th}=0$, and its $R_{Th}=\dfrac{v_T}{i_T}$ can be negative.
- Method 4 needs one analysis: with all sources on, $v_T=R_{Th}\,i_T+V_{Th}$.
- A dependent source must stay in the same part of the circuit as its controlling variable when you split or replace parts of a circuit.
- A load receives maximum power when $R_L=R_{Th}$, and then $p_{\max}=\dfrac{V_{Th}^2}{4R_{Th}}$. That is not maximum efficiency (only $35.7\%$ in the lecture example). The matching result assumes finite $R_{Th}>0$ and an adjustable passive load.
- Superposition: switch off one independent source at a time, never a dependent source, and add voltages and currents — never powers.

### Formula sheet

| Result | Formula | Use when |
|---|---|---|
| Thévenin voltage | $V_{Th}=v_{oc}$ | Terminals $a$–$b$ open |
| Norton current | $I_N=i_{sc}$ | Terminals $a$–$b$ shorted |
| Equivalent resistance | $R_{Th}=R_N=\dfrac{v_{oc}}{i_{sc}}$ | $i_{sc}\ne0$; use a test source for $\dfrac{0}{0}$ |
| Terminal equation | $v_o=V_{Th}-R_{Th}\,i_o$ | Load current $i_o$ leaves terminal $a$ |
| Test source (Method 3) | $R_{Th}=\dfrac{v_T}{i_T}$ | Independent sources off; dependent sources present or only dependent sources |
| Test source as variable (Method 4) | $v_T=R_{Th}\,i_T+V_{Th}$ | A finite, unique linear resistive port relation |
| Load power | $p_L=\dfrac{V_{Th}^2R_L}{(R_{Th}+R_L)^2}$ | Power to any load on a Thévenin equivalent |
| Maximum power transfer | $R_L=R_{Th},\;p_{\max}=\dfrac{V_{Th}^2}{4R_{Th}}$ | Adjustable passive load and finite $R_{Th}>0$ |
| Superposition | $y=\sum_k y_k$ | Linear circuit with several independent sources (not for power) |
