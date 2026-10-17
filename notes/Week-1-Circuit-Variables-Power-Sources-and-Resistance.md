# Week 1: Circuit Variables, Power, Sources and Resistance

## Overview

> **Info:** Week 1 sets up the language of circuits: what a circuit model is, five quantities (charge, current, voltage, energy, power), one sign rule, the first ideal elements (sources and resistors) and Kirchhoff's two laws. Sources: Dr. Eren's and Dr. Bakhshai's slides, Nilsson & Riedel Chapter 1 and Sections 2.1–2.2.

### Learning outcomes

- Decide when a circuit model (circuit theory) applies, and use SI units and prefixes.
- Move between charge, current, voltage, energy and power.
- Decide whether an element absorbs or delivers power, with heights and with the passive sign convention.
- Describe ideal and dependent sources, and decide whether a connection of sources is valid.
- Use Ohm's law and resistor power, and handle open and short circuits.
- Write KCL and KVL, and solve a simple circuit with the height method.

### Topic map

| # | Topic | Key result | In heights |
|---|---|---|---|
| 1 | Circuit models and units | size $<\dfrac{\lambda}{10}$ | — |
| 2 | Charge, current, voltage, energy, power | $i=dq/dt$, $p=vi$ | voltage = height difference |
| 3 | Passive sign convention | $p=\pm vi$, $\sum p=0$ | falling absorbs, climbing delivers |
| 4 | Ideal sources | $v=v_s$ or $i=i_s$ | a rigid step, or a fixed current |
| 5 | Resistors, open and short circuits | $v=iR$, $p=i^2R$ | current falls $iR$, always downhill |
| 6 | Kirchhoff's laws | $\sum i=0$, $\sum v=0$ | one height per node; currents balance |

> **Tip:** **How to use this note.** Each topic goes idea → formula → worked example → **Try it**. Answer each Try it on paper before opening its solution. The **Practice problems** at the end mix all the topics, exam style.

> **Info:** **Height views.** Think of voltage as height: pick one node as ground (0 V) and draw every other node at its voltage. Every circuit has a **Height view** button, and the problems have a **Walk me through it** that solves them one step at a time. Each topic adds one rule; Topic 6 puts them together into a six-step recipe.

## Topic 1: Circuit models, circuit theory and units

A real flashlight contains batteries, a spring, a metal case, a switch and a bulb. To analyze it we replace each part with an **ideal basic circuit element**: a mathematical model that (1) has exactly two terminals, (2) is described only by the voltage across it and the current through it, and (3) cannot be split into simpler elements. A connection of such elements is a **circuit model**, and **circuit analysis** means finding the voltage across and the current through every element of it.

```schematic
V1 0,3 -> 0,0 "$v_s$"
wire 0,3 -> 9,3
R3 9,3 -> 9,0 "$R_l$"
S1 9,0 -> 6,0 "switch"
R2 6,0 -> 3,0 "$R_c$"
R1 3,0 -> 0,0 "$R_1$"
ground 0,0
#@ view "Switch open (as drawn)"
#@ scale illustrative
#@ node t 10 "$v_s$"
#@ node n3 10 "$v_s$"
#@ node n2 0 "$0\,\mathrm{V}$"
#@ node n1 0 "$0\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ node g2 0 "$0\,\mathrm{V}$" ground
#@ el V t g "cells $v_s$" col=0
#@ el R t n3 "$R_l$: no fall" col=0
#@ el S n3 n2 "open switch: takes all of $v_s$" col=1
#@ el R n2 n1 "$R_c$" col=1
#@ el R n1 g2 "$R_1$" col=2
#@ note "With the switch open no current flows, so $R_l$, $R_c$ and $R_1$ have no voltage across them. Everything left of the gap sits at $v_s$, everything right of it at 0: the whole source voltage appears across the open switch (compare the headlamps, Textbook P2.13)."
#@ view "Switch closed (lamp on)"
#@ scale illustrative
#@ node t 10 "$v_s$"
#@ node c 3 "$i(R_c+R_1)$"
#@ node n2 3 "$i(R_c+R_1)$"
#@ node b 1 "$iR_1$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ node g2 0 "$0\,\mathrm{V}$" ground
#@ el V t g "cells $v_s$" col=0 i="$i$" to=t
#@ el R t c "$R_l$ (lamp)" col=1 i="$i$" to=c
#@ el W c n2 "closed switch: no step" col=1 i="$i$" to=n2
#@ el R n2 b "$R_c$" col=2 i="$i$" to=b
#@ el R b g2 "$R_1$" col=2 i="$i$" to=g2
#@ note "Closed, the switch is just a wire. The cells lift each coulomb to $v_s$ and it falls back to 0 through the lamp, the case and the spring. In a working flashlight the lamp has by far the largest resistance, so most of the fall (and most of the energy) happens in the lamp."
```

Circuit theory is a simplified version of electromagnetic field theory. The simplification is valid when three assumptions hold:

1. **Lumped parameters:** electrical effects happen instantaneously throughout the circuit, which requires the circuit to be small enough (rule below).
2. **No net charge** on any component: whatever charge enters one terminal leaves the other.
3. **No magnetic coupling** between components (coupled inductors are the exception treated later).

$$\lambda=\frac{c}{f},\qquad \text{lumped model valid if circuit size}<\frac{\lambda}{10}$$

Here $c\approx3\times10^{8}\,\mathrm{m/s}$ is the speed at which electrical signals travel, $f$ is the signal frequency in hertz and $\lambda$ is its wavelength in metres. The **rule of 1/10**: if the whole circuit is smaller than a tenth of the wavelength, a change at one end is felt at the other end essentially at once.

**Example: How small is "small enough"? (Section 001 lecture)**

Find the largest circuit that can be treated as lumped (a) on the $60\,\mathrm{Hz}$ power grid and (b) at a radio frequency of $1\,\mathrm{GHz}$.

1. Compute the wavelength at 60 Hz, then take one tenth.

   $$\lambda=\frac{3\times10^{8}}{60}=5\times10^{6}\,\mathrm{m}=5000\,\mathrm{km}\;\Rightarrow\;\text{size}<500\,\mathrm{km}$$
2. Repeat at 1 GHz.

   $$\lambda=\frac{3\times10^{8}}{10^{9}}=0.3\,\mathrm{m}\;\Rightarrow\;\text{size}<3\,\mathrm{cm}$$
3. Interpretation: an iron or a toaster on the 60 Hz grid is easily lumped; a 10 cm radio-frequency circuit board is not, and needs field theory.

**Answer:** **(a)** under $500\,\mathrm{km}$; **(b)** under $3\,\mathrm{cm}$.

**Problem: Try it 1 · Is a Wi-Fi board lumped?** (introductory)

A Wi-Fi router works at $2.4\,\mathrm{GHz}$. What is the largest circuit size for which a lumped model is valid? Can a $10\,\mathrm{cm}$ circuit board be analyzed with circuit theory at this frequency?

<details><summary>Solution</summary>

1. Wavelength first.

   $$\lambda=\frac{3\times10^{8}}{2.4\times10^{9}}=0.125\,\mathrm{m}$$
2. Apply the rule of 1/10.

   $$\text{size}<\frac{0.125}{10}=0.0125\,\mathrm{m}=1.25\,\mathrm{cm}$$
3. A 10 cm board is 8 times larger than the limit, so the lumped assumption fails.

**Answer:** Limit $1.25\,\mathrm{cm}$; a $10\,\mathrm{cm}$ board is **not** lumped at $2.4\,\mathrm{GHz}$.

</details>

### SI units and prefixes

Every answer needs a unit, and the derived units double as error checks: if your formula for power produces $\mathrm{V/A}$, the formula is wrong. Learn these as ratios.

| Quantity | Symbol | Unit | In other units |
|---|---|---|---|
| Charge | $q$ | coulomb ($\mathrm{C}$) | $\mathrm{A\cdot s}$ |
| Current | $i$ | ampere ($\mathrm{A}$) | $\mathrm{C/s}$ |
| Voltage | $v$ | volt ($\mathrm{V}$) | $\mathrm{J/C}$ |
| Energy | $w$ | joule ($\mathrm{J}$) | $\mathrm{W\cdot s}$ |
| Power | $p$ | watt ($\mathrm{W}$) | $\mathrm{J/s}=\mathrm{V\cdot A}$ |
| Resistance | $R$ | ohm ($\Omega$) | $\mathrm{V/A}$ |
| Conductance | $G$ | siemens ($\mathrm{S}$) | $\mathrm{A/V}$ |

| Prefix | atto | femto | pico | nano | micro | milli | kilo | mega | giga |
|---|---|---|---|---|---|---|---|---|---|
| Symbol | a | f | p | n | $\mu$ | m | k | M | G |
| Factor | $10^{-18}$ | $10^{-15}$ | $10^{-12}$ | $10^{-9}$ | $10^{-6}$ | $10^{-3}$ | $10^{3}$ | $10^{6}$ | $10^{9}$ |

> **Warning:** Capitalization matters: $\mathrm{m}$ (milli, $10^{-3}$) versus $\mathrm{M}$ (mega, $10^{6}$) is a factor of a billion. Convert to base units before substituting into a formula, and convert hours to seconds before computing joules.

**Problem: Try it 2 · Prefix warm-up** (introductory)

Convert each quantity. You will meet most of them again later this week.

1. $250\,\mu\mathrm{C}$ in coulombs
2. $3\,\mathrm{h}$ in seconds
3. $150\,\mathrm{mA}$ in amperes
4. $1.44\times10^{-18}\,\mathrm{J}$ with a prefix

<details><summary>Solution</summary>

1. Micro is $10^{-6}$.

   $$250\,\mu\mathrm{C}=250\times10^{-6}\,\mathrm{C}=2.5\times10^{-4}\,\mathrm{C}$$
2. One hour is 3600 s.

   $$3\,\mathrm{h}=3\times3600\,\mathrm{s}=10\,800\,\mathrm{s}$$
3. Milli is $10^{-3}$.

   $$150\,\mathrm{mA}=0.150\,\mathrm{A}$$
4. Atto is $10^{-18}$.

   $$1.44\times10^{-18}\,\mathrm{J}=1.44\,\mathrm{aJ}$$

**Answer:** **(1)** $2.5\times10^{-4}\,\mathrm{C}$; **(2)** $10\,800\,\mathrm{s}$; **(3)** $0.150\,\mathrm{A}$; **(4)** $1.44\,\mathrm{aJ}$.

</details>

## Topic 2: Charge, current, voltage, energy and power

Five quantities, each one a rate of another. Learn this chain and every Week 1 formula follows from it.

| Quantity | What it is | Formula | Unit |
|---|---|---|---|
| Charge $q$ | what flows; one electron carries $-e$ | $e=1.6022\times10^{-19}\,\mathrm{C}$ | coulomb, $\mathrm{C}$ |
| Current $i$ | charge per second through a wire | $i=dq/dt$, $q=\int i\,dt$ | ampere, $\mathrm{A}=\mathrm{C/s}$ |
| Voltage $v$ | energy per charge between two points (a height difference) | $v=dw/dq$, $w=qv$ | volt, $\mathrm{V}=\mathrm{J/C}$ |
| Power $p$ | energy per second | $p=dw/dt=vi$ | watt, $\mathrm{W}=\mathrm{J/s}=\mathrm{V\cdot A}$ |
| Energy $w$ | power added up over time | $w=\int p\,dt$, $w=P\,\Delta t$ | joule, $\mathrm{J}=\mathrm{W\cdot s}$ |

### Charge and current

- Charge is **quantized**: every charge is a whole number of electron charges, $e=1.6022\times10^{-19}\,\mathrm{C}$.
- **Current** is the flow of **positive** charge. In a wire the electrons move the other way; that only changes the sign.
- Every current comes with a **reference arrow**. $i=-3\,\mathrm{A}$ on an arrow pointing right means $3\,\mathrm{A}$ really flows left.
- **Differentiate** charge to get current. **Integrate** current to get charge: the area under the $i$–$t$ graph, plus any charge already there.
- Exponents have no units: in $e^{-5000t}$ the $5000$ is in $\mathrm{s^{-1}}$, so $t$ must be in seconds.

$$i=\frac{dq}{dt}\qquad\Longleftrightarrow\qquad q(t)=q(t_0)+\int_{t_0}^{t}i(\tau)\,d\tau$$

**Example: Differentiate charge to find current (Section 001 lecture; Textbook P1.11)**

The charge entering the upper terminal of an element is

$$q=\frac{1}{\alpha^2}-\left(\frac{t}{\alpha}+\frac{1}{\alpha^2}\right)e^{-\alpha t}\ \mathrm{C},\qquad \alpha=0.03679\ \mathrm{s^{-1}}.$$

Find the maximum current entering the terminal.

1. Current is the derivative of charge. The constant $\dfrac{1}{\alpha^2}$ differentiates to zero; use the product rule on the rest.

   $$i=-\left[\frac{1}{\alpha}e^{-\alpha t}-\alpha\left(\frac{t}{\alpha}+\frac{1}{\alpha^2}\right)e^{-\alpha t}\right]=-\frac{1}{\alpha}e^{-\alpha t}+te^{-\alpha t}+\frac{1}{\alpha}e^{-\alpha t}$$
2. The $\dfrac{1}{\alpha}$ terms cancel.

   $$i(t)=te^{-\alpha t}\ \mathrm{A}$$
3. A maximum needs $\dfrac{di}{dt}=0$. Since $e^{-\alpha t}$ is never zero, the bracket must vanish.

   $$\frac{di}{dt}=e^{-\alpha t}(1-\alpha t)=0\;\Rightarrow\;t=\frac{1}{\alpha}=27.2\,\mathrm{s}$$
4. Substitute back.

   $$i_{\max}=\frac{1}{\alpha}e^{-1}=\frac{1}{(0.03679)(2.718)}=10.0\,\mathrm{A}$$

**Answer:** $i(t)=te^{-\alpha t}\,\mathrm{A}$, with maximum $i_{\max}=10\,\mathrm{A}$ at $t=\dfrac{1}{\alpha}\approx27.2\,\mathrm{s}$.

**Problem: Try it 3 · Integrate current to find charge (Assessment AP 1.3; Textbook P1.7)** (introductory)

No current flows before $t=0$. For $t\ge0$ the current $i=20e^{-5000t}\,\mathrm{A}$ enters the left terminal of the element. Find the total charge that enters.

```schematic
terminal 0,0 "left" left
X1 0,0 -> 4,0 "element" i="$i$"
terminal 4,0 "right" right
```

<details><summary>Solution</summary>

1. Total charge is the whole area under the current curve.

   $$Q=\int_0^{\infty}20e^{-5000t}\,dt$$
2. Integrate the exponential.

   $$Q=\left[-\frac{20}{5000}e^{-5000t}\right]_0^{\infty}=0-\left(-\frac{20}{5000}\right)$$
3. Simplify and convert to microcoulombs.

   $$Q=0.004\,\mathrm{C}=4000\,\mu\mathrm{C}$$

**Answer:** $Q=4000\,\mu\mathrm{C}=4\,\mathrm{mC}$.

</details>

**Problem: Try it 4 · Charge from a sinusoidal current (Textbook P1.9)** (intermediate)

The current entering the left terminal of an element is $i=100\cos(2500t)\,\mathrm{mA}$. The charge at that terminal is zero at the instant the current is at its maximum. Find $q(t)$.

<details><summary>Solution</summary>

1. The cosine is maximum at $t=0$, so the initial condition is $q(0)=0$. Work in amperes.

   $$i=0.1\cos(2500t)\,\mathrm{A}$$
2. Integrate from 0 to $t$.

   $$q(t)=\int_0^{t}0.1\cos(2500\tau)\,d\tau=\frac{0.1}{2500}\sin(2500t)$$
3. Simplify, and check: differentiating gives back $0.1\cos(2500t)$.

   $$q(t)=4\times10^{-5}\sin(2500t)\,\mathrm{C}=40\sin(2500t)\,\mu\mathrm{C}$$

**Answer:** $q(t)=40\sin(2500t)\,\mu\mathrm{C}$.

</details>

### Voltage and energy: voltage is height

- **Voltage** is the energy each coulomb gains or loses between two points: $v=dw/dq$, so $w=qv$ when $v$ is constant.
- Think of it as **height**. Choose one node as **ground** ($0\,\mathrm{V}$); every other node sits at a height, its node voltage. A voltage is a height difference: $v_{ab}=V_a-V_b$.
- The $+$ and $-$ marks are only a reference. $v=+5\,\mathrm{V}$: the $+$ end is $5\,\mathrm{V}$ **higher**. $v=-5\,\mathrm{V}$: the $+$ end is $5\,\mathrm{V}$ **lower**.
- Positive charge going **down** gives up energy, like a falling ball; going **up** takes energy. An electron ($-e$) is the reverse: it **gains** energy going down.

```schematic
terminal 0,3 "$T_1$" left
X1 0,3 -> 0,0 "element" v="$v$" i="$i$"
terminal 0,0 "$T_2$" left
#@ view "With $v=+2\,\mathrm{V}$"
#@ node t1 2 "$T_1$: $2\,\mathrm{V}$"
#@ node t2 0 "$T_2$: $0\,\mathrm{V}$" ground
#@ el X t1 t2 "element" col=0 plus=t1 v="$v$"
#@ note "$v=+2\,\mathrm{V}$ means $T_1$ sits $2\,\mathrm{V}$ above $T_2$. Lifting $1\,\mathrm{C}$ of positive charge from $T_2$ up to $T_1$ costs $2\,\mathrm{J}$ ($w=qv$), so $120\,\mathrm{C}$ costs $240\,\mathrm{J}$."
#@ note "If $i>0$, positive charge enters at the top and slides down to $T_2$. It loses height, so the element absorbs energy."
```

**Problem: Try it 5 · Energy given to one electron (Textbook P1.10)** (introductory)

How much energy is imparted to an electron as it flows through a $9\,\mathrm{V}$ battery from the positive to the negative terminal? Give the answer in attojoules.

<details><summary>Solution</summary>

1. In heights: the battery's $+$ terminal is $9\,\mathrm{V}$ above its $-$ terminal, so the electron goes **down** $9\,\mathrm{V}$. A negative charge going down gains energy.

   $$\Delta U=q\,\Delta V=(-e)(-9\,\mathrm{V})=+9e>0$$
2. Size of the energy: $w=qv$ with the electron's charge.

   $$w=(1.6022\times10^{-19}\,\mathrm{C})(9\,\mathrm{V})=1.442\times10^{-18}\,\mathrm{J}$$
3. Atto is $10^{-18}$ (Topic 1).

   $$w=1.44\,\mathrm{aJ}$$

**Answer:** $1.44\,\mathrm{aJ}$.

</details>

### Power and energy

$$p=\frac{dw}{dt}=\frac{dw}{dq}\cdot\frac{dq}{dt}=vi\qquad\qquad w=\int_{t_1}^{t_2}p\,dt\quad(\text{constant }P:\ w=P\,\Delta t)$$

- Power is how fast energy moves: volts × amperes = watts.
- In heights, **power = current × the height it falls (or climbs)**. Topic 3 turns this into the sign rule.
- Energy is the area under $p(t)$. Use seconds to get joules. Bills use kilowatt-hours: $1\,\mathrm{kWh}=(1000\,\mathrm{W})(3600\,\mathrm{s})=3.6\,\mathrm{MJ}$.

**Problem: Try it 6 · Battery energy (Textbook P1.16)** (introductory)

A $9\,\mathrm{V}$ battery supplies $150\,\mathrm{mA}$ to a boom box for $3\,\mathrm{h}$. How much energy does the battery supply?

<details><summary>Solution</summary>

1. The battery lifts $150\,\mathrm{mA}$ up its $9\,\mathrm{V}$ step. Use base units (Topic 1's prefix warm-up).

   $$P=(9)(0.150)=1.35\,\mathrm{W}$$
2. Constant power: multiply by the time in seconds.

   $$w=P\,\Delta t=(1.35)(10\,800)=14\,580\,\mathrm{J}$$

**Answer:** $14.58\,\mathrm{kJ}$.

</details>

## Topic 3: Passive sign convention

Every element either **absorbs** energy (a resistor heating up, a battery being charged) or **delivers** it. Read it straight off the heights:

- Current **falls** through the element (in at the high end): it **absorbs** $p=i\times\text{fall}$.
- Current **climbs** through it (in at the low end): it **delivers** $p=i\times\text{climb}$.
- The symbol doesn't decide this. A battery being charged absorbs, because current falls through it.

### The formula version

> **Info:** **Passive sign convention (PSC).** Arrow into $+$: $p=+vi$. Arrow into $-$: $p=-vi$. Then $p>0$ means **absorbs** and $p<0$ means **delivers**.

- It is the same rule as the heights: with the arrow into $+$ and $v,i>0$, the current enters the high end and falls, so $p>0$.
- Changing a reference flips the sign of $v$ or $i$ **and** the formula, so the power never changes.
- Resistors use the same convention for Ohm's law: $v=+iR$ (arrow into $+$) or $v=-iR$ (Topic 5).

```schematic
X1 0,3 -> 0,0 "$p=+vi$" v="$v$" i="$i$"
X2 4,3 -> 4,0 "$p=-vi$" v="$v$" i_rev="$i$"
X3 8,3 -> 8,0 "$p=-vi$" v_rev="$v$" i="$i$"
X4 12,3 -> 12,0 "$p=+vi$" v_rev="$v$" i_rev="$i$"
```

| On the drawing | On the height picture |
|---|---|
| $v$ with $+$ at $a$, $-$ at $b$ | $a$ is $v$ above $b$ (below it if $v<0$) |
| $i$ on an arrow | $i>0$: flows along the arrow. $i<0$: flows against it. |
| Electrons | move against the current; $-e$ **gains** energy going down, **loses** it going up |

### Power balance

- Energy is conserved, so in every circuit the signed powers sum to zero: $\sum p=0$.
- In heights: everything the climbs deliver, the falls absorb.
- Use it to check every answer.

**Example: Same element, four reference choices (Assessment AP 1.5)**

Terminal 2 of element $X$ is $20\,\mathrm{V}$ above terminal 1, and $4\,\mathrm{A}$ enters terminal 2. Find the power absorbed by $X$, and give $v$ and $i$ for each of the four reference choices ($+$ at terminal 1 or 2; arrow into terminal 1 or out of it).

```schematic
terminal 0,3 "1" left
X1 0,3 -> 0,0 "$X$" v_rev="$20\,\mathrm{V}$" i_rev="$4\,\mathrm{A}$"
terminal 0,0 "2" left
#@ node t2 20 "terminal 2: $20\,\mathrm{V}$"
#@ node t1 0 "terminal 1: $0\,\mathrm{V}$" ground
#@ el X t2 t1 "$X$" col=0 i="$4\,\mathrm{A}$" to=t1 plus=t2 v="$20\,\mathrm{V}$" id=eX
#@ step "Ground terminal 1. Terminal 2 is $20\,\mathrm{V}$ above it (given), so terminal 2 goes on top, even though the drawing puts it at the bottom." show=t2
#@ step "$4\,\mathrm{A}$ enters terminal 2 and leaves terminal 1: it flows down through $X$." show=eX
#@ step "Downhill, so $X$ absorbs $(20)(4)=80\,\mathrm{W}$. Each row of the table is this same picture; only the signs of $v$ and $i$ change with the references, never the power."
#@ note "The drawing puts terminal 1 on top, but terminal 2 is the higher one, so here it goes on top."
#@ note "$4\,\mathrm{A}$ enters terminal 2 and leaves terminal 1: it flows downhill through $X$, so $X$ absorbs $(20)(4)=80\,\mathrm{W}$. All four rows of the table describe this one picture."
```

1. Heights first. Ground terminal 1; terminal 2 is $20\,\mathrm{V}$ up. The $4\,\mathrm{A}$ enters terminal 2, the high end, and falls through $X$, so $X$ absorbs.

   $$p=(4\,\mathrm{A})(20\,\mathrm{V})=80\,\mathrm{W}\ \text{absorbed}$$
2. Now the labels. Choose $+$ at terminal 1 and the arrow into terminal 1. Both point against the facts, so both values are negative. The arrow enters $+$, so PSC gives $+vi$.

   $$v=-20\,\mathrm{V},\qquad i=-4\,\mathrm{A},\qquad p=vi=(-20)(-4)=+80\,\mathrm{W}$$
3. The other three choices change the signs, never the power.

   $$\begin{array}{c|c|c|c}+\text{ at}&\text{arrow}&(v,\ i)&p\\\hline 1&\text{into }1&(-20,\,-4)&+vi=80\,\mathrm{W}\\1&\text{out of }1&(-20,\,+4)&-vi=80\,\mathrm{W}\\2&\text{into }1&(+20,\,-4)&-vi=80\,\mathrm{W}\\2&\text{out of }1&(+20,\,+4)&+vi=80\,\mathrm{W}\end{array}$$

**Answer:** $X$ absorbs $80\,\mathrm{W}$, whatever references you choose.

**Problem: Try it 7 · Power, electrons and energy (Textbook P1.12 and P1.13)** (intermediate)

For the element below, $v=80\,\mathrm{V}$ and $i=-4\,\mathrm{A}$ (Textbook P1.12).

```schematic
terminal 0,3 "1" left
X1 0,3 -> 0,0 "$X$" v_rev="$v$" i="$i$"
terminal 0,0 "2" left
#@ spoiler
#@ view "P1.12: $i=-4\,\mathrm{A}$"
#@ node t2 80 "terminal 2: $80\,\mathrm{V}$"
#@ node t1 0 "terminal 1: $0\,\mathrm{V}$" ground
#@ el X t2 t1 "$X$" col=0 i="$4\,\mathrm{A}$" to=t1 id=eX plus=t2 v="$v$"
#@ step "Ground terminal 1. $v=80\,\mathrm{V}$ is marked + at terminal 2, so terminal 2 sits $80\,\mathrm{V}$ up." show=t2
#@ step "$i=-4\,\mathrm{A}$ is drawn into terminal 1, so the real current is $4\,\mathrm{A}$ the other way: in at terminal 2 and down to terminal 1." show=eX
#@ step "The current falls, so the element absorbs $(80\,\mathrm{V})(4\,\mathrm{A})=320\,\mathrm{W}$."
#@ step "Electrons move against the current: in at terminal 1 and up to terminal 2, so they are **leaving at terminal 2**. A negative charge that climbs **loses** energy, exactly the $320\,\mathrm{W}$ the element absorbs."
#@ view "P1.13: $i=+4\,\mathrm{A}$"
#@ node t2 80 "terminal 2: $80\,\mathrm{V}$"
#@ node t1 0 "terminal 1: $0\,\mathrm{V}$" ground
#@ el X t2 t1 "$X$" col=0 i="$4\,\mathrm{A}$" to=t2 id=eX plus=t2 v="$v$"
#@ step "Same ground (terminal 1), and terminal 2 is still $80\,\mathrm{V}$ up." show=t2
#@ step "$i=+4\,\mathrm{A}$ into terminal 1 is positive, so the current really enters at terminal 1 (the bottom) and climbs to terminal 2." show=eX
#@ step "The current climbs, so the element delivers $(80)(4)=320\,\mathrm{W}$."
#@ step "Electrons go against the current: in at terminal 2, out at terminal 1. So they are **entering terminal 2**, and they fall from $80\,\mathrm{V}$ to 0. A negative charge going **down** **gains** energy: the element acts as a source."
#@ note "Flipping the sign of $i$ flipped every answer, while the heights stayed the same."
```

1. Find the power. Is it absorbed or delivered?
2. The current is carried by electrons. Are electrons entering or leaving terminal 2?
3. Do the electrons gain or lose energy as they pass through the element?
4. (Textbook P1.13) Repeat 1–3 with $i=+4\,\mathrm{A}$.

<details><summary>Solution</summary>

1. Heights: ground terminal 1. $v=80\,\mathrm{V}$ with $+$ at terminal 2, so terminal 2 is $80\,\mathrm{V}$ up.
2. **(1)** $i=-4\,\mathrm{A}$ into terminal 1 means $4\,\mathrm{A}$ really enters terminal 2 (the high end) and falls. PSC check: the arrow enters terminal 1, the $-$ of $v$, so $p=-vi$.

   $$p=-vi=-(80)(-4)=+320\,\mathrm{W}\;(\text{absorbed})$$
3. **(2–3)** Electrons move against the current: in at terminal 1, out at terminal 2, climbing $80\,\mathrm{V}$. A negative charge that climbs loses energy, the energy the element absorbs.

   $$\Delta U=(-e)(+80\,\mathrm{V})<0$$
4. **(4)** With $i=+4\,\mathrm{A}$ the current enters terminal 1 (low) and climbs, so the element delivers. Electrons now enter terminal 2 and fall $80\,\mathrm{V}$, so they gain energy.

   $$\begin{aligned}p&=-vi=-(80)(4)=-320\,\mathrm{W}\\ \Delta U&=(-e)(-80\,\mathrm{V})>0\end{aligned}$$

**Answer:** **P1.12:** $320\,\mathrm{W}$ absorbed; electrons leave terminal 2; they lose energy. **P1.13:** $320\,\mathrm{W}$ delivered; electrons enter terminal 2; they gain energy.

</details>

**Problem: Try it 8 · Which car has the dead battery? (Section 001 lecture; Textbook P1.14)** (introductory)

To jump-start a car, its battery is connected to another car's battery: $+$ to $+$ and $-$ to $-$. The measured current is $i=30\,\mathrm{A}$, flowing through the cable from car B's positive terminal into car A's positive terminal. Both are $12\,\mathrm{V}$ batteries.

```schematic
B1 0,3 -> 0,0 "car A, $12\,\mathrm{V}$" v i="$i$"
wire 0,3 -> 5,3
B2 5,3 -> 5,0 "car B, $12\,\mathrm{V}$" v flip
wire 5,0 -> 0,0
#@ node top 12 "positive terminals: $12\,\mathrm{V}$"
#@ node g 0 "negative terminals: $0\,\mathrm{V}$" ground
#@ el B top g "car A" col=0 i="$30\,\mathrm{A}$" to=g id=eA
#@ el B top g "car B" col=1 i="$30\,\mathrm{A}$" to=top id=eB
#@ step "Both + terminals are wired together, and so are both − terminals. So there are only two heights: ground (0) and $12\,\mathrm{V}$." show=top
#@ step "The $30\,\mathrm{A}$ goes from car B's + terminal into car A's + terminal. So it climbs through car B (0 up to $12\,\mathrm{V}$) and falls through car A ($12\,\mathrm{V}$ down to 0)." show=eA,eB
#@ step "Climbing means delivering, falling means absorbing. Car B delivers $(12)(30)=360\,\mathrm{W}$ and car A absorbs it: **car A is being charged, so it has the dead battery**. Over $60\,\mathrm{s}$ that is $(360)(60)=21.6\,\mathrm{kJ}$."
#@ note "Both + terminals sit at $12\,\mathrm{V}$. In car B the current climbs from 0 to $12\,\mathrm{V}$: B lifts the charge, so it delivers energy."
#@ note "In car A the same current falls from $12\,\mathrm{V}$ to 0: A absorbs energy, i.e. it is being charged. A is the dead battery, taking in $(12)(30)=360\,\mathrm{W}$."
```

1. Which car has the dead battery?
2. If the connection is kept for $1\,\mathrm{min}$, how much energy reaches the dead battery?

<details><summary>Solution</summary>

1. Heights: the $-$ terminals are joined (ground) and the $+$ terminals are joined at $12\,\mathrm{V}$. The current climbs through car B and falls through car A.
2. Falling absorbs: car A is being charged, so A has the dead battery. PSC agrees: the arrow enters A's $+$, and the same current enters B's $-$.

   $$p_A=+vi=(12)(30)=+360\,\mathrm{W},\qquad p_B=-vi=-360\,\mathrm{W}$$
3. Constant power: energy is power times time in seconds.

   $$w=p\,\Delta t=(360)(60)=21\,600\,\mathrm{J}=21.6\,\mathrm{kJ}$$

**Answer:** **(1)** Car A. **(2)** $21.6\,\mathrm{kJ}$. (The textbook version, P1.14, uses $25\,\mathrm{A}$ and gives $18\,\mathrm{kJ}$.)

</details>

**Problem: Try it 9 · Find unknown voltages from the power balance (Section 001 lecture)** (intermediate)

In the loop below, $v_a=10\,\mathrm{V}$, $p_b=9\,\mathrm{W}$, $i_a=1\,\mathrm{A}$, $i_b=-1\,\mathrm{A}$ and $i_c=1\,\mathrm{A}$. Find $v_b$ and $v_c$.

```schematic
X1 0,3 -> 0,0 "$a$" v="$v_a$" i_rev="$i_a$"
X2 0,3 -> 4,3 "$b$" v="$v_b$" i_rev="$i_b$"
X3 4,3 -> 4,0 "$c$" v_rev="$v_c$" i="$i_c$"
wire 4,0 -> 0,0
#@ node top 10 "top wire: $10\,\mathrm{V}$"
#@ node m 1 "between $b$ and $c$: $1\,\mathrm{V}$"
#@ node g 0 "bottom wire: $0\,\mathrm{V}$" ground
#@ el X top g "$a$" col=0 i="$1\,\mathrm{A}$" to=top id=ea plus=top v="$v_a$"
#@ el X top m "$b$: falls $9\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=m id=eb plus=top v="$v_b$"
#@ el X m g "$c$: falls $1\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=g id=ec plus=g v="$v_c$"
#@ step "Ground the bottom wire. $v_a=10\,\mathrm{V}$ with + at the top, so the top wire is at $10\,\mathrm{V}$." show=top
#@ step "One loop, so one current: $1\,\mathrm{A}$ up through $a$, across $b$ from left to right ($i_b=-1\,\mathrm{A}$ on a right-to-left arrow), then down through $c$." show=ea
#@ step "$b$ absorbs $9\,\mathrm{W}$ while carrying $1\,\mathrm{A}$, so the charge falls $\dfrac{9\,\mathrm{W}}{1\,\mathrm{A}}=9\,\mathrm{V}$ through it. The node between $b$ and $c$ is at $10-9=1\,\mathrm{V}$." show=eb,m
#@ step "$c$ takes the charge the last $1\,\mathrm{V}$ down to ground, absorbing $1\,\mathrm{W}$." show=ec
#@ step "Read the voltages off the picture. $v_b$ has + on the left (the top wire), so $v_b=10-1=9\,\mathrm{V}$. The top of $c$ is $1\,\mathrm{V}$ above its bottom, but $v_c$ is marked + at the bottom, so $v_c=-1\,\mathrm{V}$."
#@ step "Check: $a$ lifts $1\,\mathrm{A}$ through $10\,\mathrm{V}$ ($10\,\mathrm{W}$ delivered), and $b$ and $c$ drop it $9+1\,\mathrm{V}$ ($9+1\,\mathrm{W}$ absorbed)."
#@ note "Element $a$ lifts each coulomb from 0 to $10\,\mathrm{V}$ (it delivers $10\,\mathrm{W}$). Element $b$ lets it fall $9\,\mathrm{V}$ and $c$ the last $1\,\mathrm{V}$. The falls add up to the rise: that is KVL."
#@ note "$v_c=-1\,\mathrm{V}$ only because its + mark is at the bottom. The top of $c$ is really $1\,\mathrm{V}$ higher."
```

<details><summary>Solution</summary>

1. Element $a$: $i_a$ points up into the bottom terminal, which is $-$, so PSC gives $-vi$. In heights: $1\,\mathrm{A}$ climbs $10\,\mathrm{V}$ through $a$.

   $$p_a=-v_ai_a=-(10)(1)=-10\,\mathrm{W}$$
2. Power balance gives $p_c$.

   $$p_a+p_b+p_c=0\;\Rightarrow\;p_c=10-9=1\,\mathrm{W}$$
3. Element $b$: $i_b$ is drawn right to left and enters the right terminal, which is $-$.

   $$p_b=-v_bi_b\;\Rightarrow\;v_b=-\frac{p_b}{i_b}=-\frac{9}{-1}=9\,\mathrm{V}$$
4. Element $c$: $i_c$ flows down, entering the top terminal, which is $-$.

   $$p_c=-v_ci_c\;\Rightarrow\;v_c=-\frac{p_c}{i_c}=-\frac{1}{1}=-1\,\mathrm{V}$$
5. Check with heights: up $10$ through $a$, down $9$ through $b$, down the last $1$ through $c$ back to ground. $v_c$ is negative only because its $+$ is on the low end.

   $$10-9-1=0$$

**Answer:** $v_b=9\,\mathrm{V}$ and $v_c=-1\,\mathrm{V}$. Element $a$ delivers $10\,\mathrm{W}$; $b$ and $c$ absorb $9\,\mathrm{W}$ and $1\,\mathrm{W}$.

</details>

## Topic 4: Ideal sources

- An ideal source **fixes one** quantity and lets the rest of the circuit choose the other.
- Sources are **active**: they can deliver net energy. They can also absorb it (a battery being charged). Resistors, capacitors and inductors are **passive**.

| Source | It fixes | The circuit decides | In heights |
|---|---|---|---|
| Voltage source (circle with $+$/$-$) | its voltage $v_s$ | its current (any size, either way) | a **rigid step**: the $+$ end is exactly $v_s$ higher |
| Current source (circle with arrow) | its current $i_s$ | its voltage | a **fixed current**; its step stretches to whatever is needed |
| Dependent source (diamond) | $v$ or $i$ = gain × a control elsewhere | the other one | same as above, once the control is known |

```schematic
V1 0,3 -> 0,0 "$v_s$"
I1 3,0 -> 3,3 "$i_s$"
E1 6,3 -> 6,0 "$\mu v_x$"
G1 9,0 -> 9,3 "$\beta i_x$"
```

| Dependent source | Relation | Units of the gain |
|---|---|---|
| Voltage-controlled voltage source | $v_s=\mu v_x$ | none (V/V) |
| Current-controlled voltage source | $v_s=\rho i_x$ | $\Omega$ (V/A) |
| Voltage-controlled current source | $i_s=\alpha v_x$ | $\mathrm{S}$ (A/V) |
| Current-controlled current source | $i_s=\beta i_x$ | none (A/A) |

- For a dependent source, **find the control first** ($v_x$ or $i_x$, with its sign from its own reference), then treat it like an ordinary source.
- The slides write $\mu$ for every gain; the textbook uses the four symbols above.

### Valid connections

Ideal sources are rigid, so some connections are impossible. Check with the heights before calculating:

- **Every node has one height (KVL).** Voltage sources in parallel must agree. A voltage source can't be shorted: its step would be forced to 0.
- **Current balances at every node (KCL).** Current sources in series must agree. A current source can't be left open.
- Voltage sources in series and current sources in parallel are always fine: steps add, currents add.
- **Valid but undetermined:** a node reached only through current sources has no fixed height. It **floats** (dashed in the height view), so the voltages and powers that depend on it can't be found.

> **Warning:** Never give a voltage source zero current, or a current source zero voltage, by default: the rest of the circuit sets them. Whether a source delivers depends only on which way the current crosses its step.

**Example: A source may absorb power (Tutorial P2.1; Textbook P2.1)**

Is this connection of ideal sources valid? Which sources develop power and which absorb it? Then reverse the polarity of the $10\,\mathrm{V}$ source and repeat. (The tutorial figure labels the current source \"8 V\"; the solution and the textbook treat it as $8\,\mathrm{A}$.)

```schematic
V1 0,3 -> 0,0 "$30\,\mathrm{V}$"
V2 0,3 -> 4,3 "$10\,\mathrm{V}$"
I1 4,0 -> 4,3 "$8\,\mathrm{A}$" flip
wire 4,0 -> 0,0
label 0,3 "$a$" above
label 4,3 "$b$" above
ground 0,0
#@ view "As drawn"
#@ node a 30 "$a$: $30\,\mathrm{V}$"
#@ node b 20 "$b$: $20\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$30\,\mathrm{V}$: absorbs" col=0 i="$8\,\mathrm{A}$" to=g id=e30
#@ el V a b "$10\,\mathrm{V}$: delivers" col=1 i="$8\,\mathrm{A}$" to=a id=e10
#@ el I g b "$8\,\mathrm{A}$: delivers" col=1 i="$8\,\mathrm{A}$" to=b id=e8
#@ step "Ground the bottom wire. The $30\,\mathrm{V}$ source has its + at $a$, so $a$ is at $30\,\mathrm{V}$." show=a
#@ step "The $10\,\mathrm{V}$ source has + at $a$ and − at $b$, so $b$ sits $10\,\mathrm{V}$ below $a$: $20\,\mathrm{V}$." show=b
#@ step "One loop, and the $8\,\mathrm{A}$ source fixes its current: $8\,\mathrm{A}$ up through the current source, from $b$ to $a$ through the $10\,\mathrm{V}$ source, and down through the $30\,\mathrm{V}$ source." show=e30,e10,e8
#@ step "Read off uphill and downhill. Current source: 0 up to $20\,\mathrm{V}$, delivers $(20)(8)=160\,\mathrm{W}$. $10\,\mathrm{V}$ source: $20$ up to $30\,\mathrm{V}$, delivers $(10)(8)=80\,\mathrm{W}$. $30\,\mathrm{V}$ source: $30$ down to 0, **absorbs** $(30)(8)=240\,\mathrm{W}$."
#@ step "Check: $160+80=240$. Every node has one height and the loop current is consistent, so the connection is valid."
#@ note "The current source lifts the charge from 0 to $20\,\mathrm{V}$ and the $10\,\mathrm{V}$ source lifts it on to $30\,\mathrm{V}$. It then falls back to 0 through the $30\,\mathrm{V}$ source, so that source absorbs $240\,\mathrm{W}$: it is being charged."
#@ view "10 V source reversed"
#@ node a 30 "$a$: $30\,\mathrm{V}$"
#@ node b 40 "$b$: $40\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$30\,\mathrm{V}$: absorbs" col=0 i="$8\,\mathrm{A}$" to=g id=e30
#@ el V b a "$10\,\mathrm{V}$: absorbs" col=1 i="$8\,\mathrm{A}$" to=a id=e10
#@ el I g b "$8\,\mathrm{A}$: delivers" col=2 i="$8\,\mathrm{A}$" to=b id=e8
#@ step "Same ground (the bottom wire). $a$ is still at $30\,\mathrm{V}$: the $30\,\mathrm{V}$ source didn't change." show=a
#@ step "Reversed, the $10\,\mathrm{V}$ source has its + at $b$, so $b$ is now $10\,\mathrm{V}$ **above** $a$: $40\,\mathrm{V}$." show=b
#@ step "The same $8\,\mathrm{A}$ loop. The current source now has to lift the charge from 0 all the way up to $40\,\mathrm{V}$: it delivers $(40)(8)=320\,\mathrm{W}$." show=e8
#@ step "The charge then falls $40\to30\,\mathrm{V}$ through the $10\,\mathrm{V}$ source (absorbs $80\,\mathrm{W}$) and $30\to0$ through the $30\,\mathrm{V}$ source (absorbs $240\,\mathrm{W}$). Check: $80+240=320$." show=e10,e30
#@ note "Now $b$ is above $a$. The current source has to lift the charge all the way to $40\,\mathrm{V}$ ($320\,\mathrm{W}$), and both voltage sources absorb on the way down."
```

1. Ground the bottom wire. Fixed heights: the $30\,\mathrm{V}$ source puts $a$ at $30\,\mathrm{V}$, and the $10\,\mathrm{V}$ source ($+$ at $a$) puts $b$ $10\,\mathrm{V}$ lower. Every node has one height.

   $$V_a=30\,\mathrm{V},\qquad V_b=30-10=20\,\mathrm{V}$$
2. Currents: one loop, and the $8\,\mathrm{A}$ source fixes it: up through the current source, from $b$ to $a$ through the $10\,\mathrm{V}$ source, down through the $30\,\mathrm{V}$ source. No conflict anywhere, so the connection is **valid**.
3. Climbs deliver, falls absorb.

   $$\begin{aligned}8\,\mathrm{A}&:\ 0\to20\,\mathrm{V},\ \text{delivers }(20)(8)=160\,\mathrm{W}\\10\,\mathrm{V}&:\ 20\to30\,\mathrm{V},\ \text{delivers }(10)(8)=80\,\mathrm{W}\\30\,\mathrm{V}&:\ 30\to0\,\mathrm{V},\ \text{absorbs }(30)(8)=240\,\mathrm{W}\end{aligned}$$
4. Reversed $10\,\mathrm{V}$ source: its $+$ is now at $b$, so $b$ is $10\,\mathrm{V}$ **above** $a$, at $40\,\mathrm{V}$. The current source must lift the charge all the way up, and both voltage sources let it fall.

   $$\begin{aligned}8\,\mathrm{A}&:\ 0\to40\,\mathrm{V},\ \text{delivers }320\,\mathrm{W}\\10\,\mathrm{V}&:\ 40\to30\,\mathrm{V},\ \text{absorbs }80\,\mathrm{W}\\30\,\mathrm{V}&:\ 30\to0\,\mathrm{V},\ \text{absorbs }240\,\mathrm{W}\end{aligned}$$

**Answer:** Valid both times. **As drawn:** the $30\,\mathrm{V}$ source absorbs $240\,\mathrm{W}$; the $10\,\mathrm{V}$ and $8\,\mathrm{A}$ sources deliver $80\,\mathrm{W}$ and $160\,\mathrm{W}$. **Reversed:** both voltage sources absorb ($240+80\,\mathrm{W}$) and the current source delivers $320\,\mathrm{W}$.

**Problem: Try it 10 · A dependent voltage source (Textbook P2.7)** (intermediate)

**(a)** What value of $v_g$ makes the connection valid? **(b)** For that value, find the power of the $8\,\mathrm{A}$ source.

```schematic
E1 0,3 -> 0,0 "$i_b/4$"
wire 0,3 -> 6,3
V1 3,3 -> 3,0 "$v_g$"
I1 6,3 -> 6,0 "$8\,\mathrm{A}$" flip
wire 6,0 -> 0,0
label 4.5,3 "$\leftarrow i_b$" above
#@ spoiler
#@ node t -2 "top: $-2\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ el E t g "$i_b/4$" col=0
#@ el V t g "$v_g$" col=1
#@ el I t g "$8\,\mathrm{A}$" col=2 i="$8\,\mathrm{A}$" to=g id=e8
#@ step "Ground the bottom wire. Find the control first: the $8\,\mathrm{A}$ source pulls $8\,\mathrm{A}$ down at the top-right corner, so $8\,\mathrm{A}$ flows rightward along the top wire. $i_b$ is drawn leftward, so $i_b=-8\,\mathrm{A}$."
#@ step "The dependent source (+ on top) sets the top wire's height: $\dfrac{i_b}{4}=-2\,\mathrm{V}$, so the top wire is $2\,\mathrm{V}$ **below** ground. $v_g$ sits across the same two wires, so $v_g=-2\,\mathrm{V}$ too." show=t
#@ step "The $8\,\mathrm{A}$ source moves charge from the top wire ($-2\,\mathrm{V}$) to the bottom wire (0): uphill, so it **delivers** $(2)(8)=16\,\mathrm{W}$. Its absorbed power is $-16\,\mathrm{W}$." show=e8
#@ note "$v_g=-2\,\mathrm{V}$ puts the top rail $2\,\mathrm{V}$ below ground. The $8\,\mathrm{A}$ source pushes charge from the top rail ($-2\,\mathrm{V}$) to ground: uphill, so it delivers $16\,\mathrm{W}$."
#@ note "The two voltage sources share one pair of levels (they are in parallel), so they must agree. How the current splits between them is not determined, so they get no arrows."
```

<details><summary>Solution</summary>

1. The dependent source and $v_g$ span the same two wires, so they share the same two heights: they must be equal.

   $$v_g=\frac{i_b}{4}$$
2. Find the control $i_b$, the current in the top wire flowing left. The 8 A source pulls 8 A down out of the top-right corner, so the wire carries 8 A to the right.

   $$i_b=-8\,\mathrm{A}$$
3. Substitute. The gain $\frac14$ turns amperes into volts, so it is $0.25\,\Omega$.

   $$v_g=\frac{-8}{4}=-2\,\mathrm{V}$$
4. Heights: ground the bottom wire; the top wire is at $-2\,\mathrm{V}$. The 8 A source moves charge from the top wire ($-2$) to the bottom wire (0): it climbs, so the source delivers. PSC agrees: its 8 A enters its top, the $+$ end of $v_g$.

   $$p_{8\mathrm{A}}=+vi=(-2)(8)=-16\,\mathrm{W}$$

**Answer:** **(a)** $v_g=-2\,\mathrm{V}$. **(b)** $p=-16\,\mathrm{W}$: the $8\,\mathrm{A}$ source delivers $16\,\mathrm{W}$.

</details>

**Problem: Try it 11 · A node with no height (Textbook P2.5)** (advanced)

The interconnection of ideal sources can lead to an indeterminate solution. Explain why $v_1$ and $v_2$ in this circuit are not unique. (Added) What *can* you say about $v_1$, $v_2$ and the powers?

```schematic
I1 0,0 -> 0,3 "$10\,\mathrm{A}$"
wire 0,3 -> 3,3
I2 2,3 -> 2,0 "$20\,\mathrm{A}$" v="$v_1$" flip
V1 3,3 -> 5,3 "$100\,\mathrm{V}$"
wire 5,3 -> 6,3
V2 6,0 -> 6,3 "$50\,\mathrm{V}$" flip
I3 3,0 -> 5,0 "$10\,\mathrm{A}$" v="$v_2$"
wire 0,0 -> 3,0
wire 5,0 -> 6,0
#@ spoiler
#@ node tl 100 "top left: $100\,\mathrm{V}$"
#@ node br 50 "bottom right: $50\,\mathrm{V}$"
#@ node bl 20 "bottom left: free" unknown
#@ node g 0 "top right: $0\,\mathrm{V}$" ground
#@ el I bl tl "$10\,\mathrm{A}$" col=0 i="$10\,\mathrm{A}$" to=tl id=ea
#@ el I tl bl "$20\,\mathrm{A}$" col=1 i="$20\,\mathrm{A}$" to=bl id=eb plus=tl v="$v_1$"
#@ el I bl br "$10\,\mathrm{A}$" col=2 i="$10\,\mathrm{A}$" to=br id=ec plus=bl v="$v_2$"
#@ el V br g "$50\,\mathrm{V}$" col=3 i="$10\,\mathrm{A}$" to=g id=e50
#@ el V tl g "$100\,\mathrm{V}$" col=4 i="$10\,\mathrm{A}$" to=tl id=e100
#@ step "Ground a node the voltage sources touch: the top-right one. The $100\,\mathrm{V}$ source (+ on the left) puts the top-left node at $100\,\mathrm{V}$, and the $50\,\mathrm{V}$ source (+ at the bottom) puts the bottom-right node at $50\,\mathrm{V}$." show=tl,br
#@ step "The bottom-left node touches only current sources. A current source fixes a current, never a height, so nothing pins this node: it floats (dashed)." show=bl
#@ step "$v_1$ is top left minus bottom left, and $v_2$ is bottom left minus bottom right. Slide the bottom-left node up or down: $v_1$ and $v_2$ change, but their sum stays $100-50=50\,\mathrm{V}$. Infinitely many answers fit, so they are **not unique**."
#@ step "The currents are all fixed and consistent: the bottom $10\,\mathrm{A}$ goes up the $50\,\mathrm{V}$ source and through the $100\,\mathrm{V}$ source to the top-left node, where $10+10=20\,\mathrm{A}$ leave down the $20\,\mathrm{A}$ source. KCL holds, so the connection is **valid**, just underdetermined." show=ea,eb,ec,e50,e100
#@ step "What is fixed: the $100\,\mathrm{V}$ source lifts $10\,\mathrm{A}$ from 0 to $100\,\mathrm{V}$ ($1000\,\mathrm{W}$ delivered), and the current falls $50\to0$ through the $50\,\mathrm{V}$ source ($500\,\mathrm{W}$ absorbed). The current sources together absorb the other $500\,\mathrm{W}$, but how they share it depends on the floating height."
#@ note "The dashed level is drawn at an arbitrary height: any height works."
```

<details><summary>Solution</summary>

1. Ground the top-right node, which both voltage sources touch, and step across them.

   $$V_{TL}=0+100=100\,\mathrm{V},\qquad V_{BR}=0+50=50\,\mathrm{V}$$
2. The bottom-left node connects only to current sources. They fix currents but never heights, so nothing pins $V_{BL}$: it floats.
3. Both unknown voltages involve that free height, but their sum does not.

   $$\begin{aligned}v_1&=V_{TL}-V_{BL}\\ v_2&=V_{BL}-V_{BR}\\ v_1+v_2&=V_{TL}-V_{BR}=50\,\mathrm{V}\end{aligned}$$
4. KCL still holds at every node (at the top left: $10$ in from the left source, $10$ in from the $100\,\mathrm{V}$ branch, $20$ out), so the connection is valid; it just has infinitely many solutions.
5. The voltage sources' powers are fixed: $10\,\mathrm{A}$ climbs $100\,\mathrm{V}$ through one and falls $50\,\mathrm{V}$ through the other. The current sources absorb the difference as a group.

   $$\begin{aligned}&p_{100}=-1000\,\mathrm{W},\qquad p_{50}=+500\,\mathrm{W}\\&\textstyle\sum p_{\text{current sources}}=+500\,\mathrm{W}\end{aligned}$$

**Answer:** The bottom-left node is joined only through current sources, so its height (and hence $v_1$ and $v_2$ separately) is undetermined. Only $v_1+v_2=50\,\mathrm{V}$ is fixed. The connection is still valid (KCL holds).

</details>

## Topic 5: Resistors, Ohm's law, open and short circuits

- A resistor turns electrical energy into heat (a toaster, a bulb filament). Resistance $R$ is in ohms, $\Omega=\mathrm{V/A}$.
- **Ohm's law:** $v=iR$ when the arrow enters $+$ (PSC), $v=-iR$ when it enters $-$.
- **In heights:** current always flows **downhill** through a resistor, and it falls $iR$. So $i=\text{fall}/R$.
- **Conductance** $G=1/R$ in siemens ($\mathrm{S}=\mathrm{A/V}$): $i=Gv$.
- **Power:** $p=i^2R=v^2/R\ge0$. Always downhill, so a resistor **always absorbs**. A negative resistor power means a sign error.

$$v=iR\ \ (\text{arrow into }+),\qquad G=\frac{1}{R},\qquad p=i^2R=\frac{v^2}{R}$$

```schematic
R1 0,0 -> 4,0 "$R$" v="$v$" i="$i$"
```

### Open and short circuits

|  | Short circuit (closed switch, wire) | Open circuit (open switch, gap) |
|---|---|---|
| Resistance | $R=0$ | $R\to\infty$ |
| Fixed | $v=0$ | $i=0$ |
| Set by the circuit | $i$ | $v$ |
| In heights | no step: both ends at the same height | no current; it takes whatever step is left over |

> **Warning:** Never compute $\dfrac{v}{R}$ for a short ($\dfrac00$) or $iR$ for an open ($0\cdot\infty$). Use $v=0$ and $i=0$ directly.

**Example: Reversing a voltage source (Tutorial P2.11; Textbook P2.11)**

Find $i$ and the power supplied by the source. Then reverse the source polarity and repeat.

```schematic
V1 0,3 -> 0,0 "$120\,\mathrm{V}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$10\,\mathrm{k\Omega}$" i="$i$" flip
wire 3,0 -> 0,0
#@ view "As drawn"
#@ node t 120 "top: $120\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$120\,\mathrm{V}$" col=0 i="$12\,\mathrm{mA}$" to=t id=es
#@ el R t g "$10\,\mathrm{k\Omega}$" col=1 i="$12\,\mathrm{mA}$" to=g id=er
#@ step "Ground the bottom wire. The source's + is on top, so the top wire is at $120\,\mathrm{V}$." show=t
#@ step "The resistor hangs straight between the two wires, so it falls the full $120\,\mathrm{V}$. Current = fall ÷ resistance: $\dfrac{120}{10\,000}=12\,\mathrm{mA}$, flowing downhill (down through it), so $i=12\,\mathrm{mA}$." show=er,es
#@ step "The source lifts $12\,\mathrm{mA}$ through $120\,\mathrm{V}$: it supplies $(120)(0.012)=1.44\,\mathrm{W}$, all of it absorbed by the resistor."
#@ note "The source lifts each coulomb $120\,\mathrm{V}$ and it falls the same $120\,\mathrm{V}$ through the resistor: $1.44\,\mathrm{W}$ in, $1.44\,\mathrm{W}$ out."
#@ view "Source reversed"
#@ node t -120 "top: $-120\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V g t "$120\,\mathrm{V}$ (reversed)" col=0 i="$12\,\mathrm{mA}$" to=g id=es
#@ el R t g "$10\,\mathrm{k\Omega}$" col=1 i="$12\,\mathrm{mA}$" to=t id=er
#@ step "Reversed, the source's + is on the bottom wire, so the top wire is $120\,\mathrm{V}$ **below** ground." show=t
#@ step "The resistor still falls $120\,\mathrm{V}$, but downhill is now from the bottom wire to the top wire: $12\,\mathrm{mA}$ flows **up** through it. For the drawn (downward) arrow that is $i=-12\,\mathrm{mA}$." show=er,es
#@ step "Same $1.44\,\mathrm{W}$ supplied and absorbed. A resistor always sits on a downhill stretch, whichever way the source points."
#@ note "Now the top wire is the low side and the current reverses ($i=-12\,\mathrm{mA}$). It still flows downhill through the resistor, which is why a resistor always absorbs."
```

1. Ground the bottom wire; the source puts the top wire at $120\,\mathrm{V}$. The resistor hangs between the two wires, so it falls $120\,\mathrm{V}$ and its current flows downhill, the way $i$ points.

   $$i=\frac{120}{10\,000}=0.012\,\mathrm{A}=12\,\mathrm{mA}$$
2. The source lifts what the resistor lets fall.

   $$p=(120)(0.012)=i^2R=1.44\,\mathrm{W}$$
3. Reversed: the top wire is now $120\,\mathrm{V}$ **below** ground, so downhill is upward through the resistor, against the arrow.

   $$i=-12\,\mathrm{mA},\qquad p=(-0.012)^2(10\,000)=1.44\,\mathrm{W}$$

**Answer:** $i=12\,\mathrm{mA}$ and the source supplies $1.44\,\mathrm{W}$. Reversed: $i=-12\,\mathrm{mA}$, and the source still supplies $1.44\,\mathrm{W}$.

**Problem: Try it 12 · Current source into a resistor (Textbook P2.12)** (introductory)

**(a)** Find $v$. **(b)** Find the power absorbed by the resistor. **(c)** Reverse the current source and repeat.

```schematic
I1 0,3 -> 0,0 "$75\,\mathrm{mA}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$8\,\mathrm{k\Omega}$" v="$v$" flip
wire 3,0 -> 0,0
#@ spoiler
#@ view "As drawn"
#@ node t -600 "top: $-600\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ el I t g "$75\,\mathrm{mA}$" col=0 i="$75\,\mathrm{mA}$" to=g id=es
#@ el R t g "$8\,\mathrm{k\Omega}$" col=1 i="$75\,\mathrm{mA}$" to=t id=er plus=t v="$v$"
#@ step "Ground the bottom wire. The current source fixes the current: $75\,\mathrm{mA}$ down through the source, along the bottom wire, and **up** through the resistor." show=es,er
#@ step "Current through a resistor always runs downhill, so the resistor's bottom must be its high end. The fall is $iR=(0.075)(8000)=600\,\mathrm{V}$: the top wire is $600\,\mathrm{V}$ below ground." show=t
#@ step "$v$ is marked + at the top, which is the low end: $v=-600\,\mathrm{V}$. The source lifts the charge back up $600\,\mathrm{V}$, delivering $(600)(0.075)=45\,\mathrm{W}$, which the resistor absorbs."
#@ note "The source drives the current up through the resistor, so the resistor's top must be lower than its bottom: $v=-600\,\mathrm{V}$. The source then lifts the charge $600\,\mathrm{V}$ back up ($45\,\mathrm{W}$)."
#@ view "Source reversed"
#@ node t 600 "top: $600\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ el I g t "$75\,\mathrm{mA}$ (reversed)" col=0 i="$75\,\mathrm{mA}$" to=t id=es
#@ el R t g "$8\,\mathrm{k\Omega}$" col=1 i="$75\,\mathrm{mA}$" to=g id=er plus=t v="$v$"
#@ step "Same ground (the bottom wire). Reversed, the source drives $75\,\mathrm{mA}$ the other way: **down** through the resistor." show=es,er
#@ step "Downhill through the resistor means its top is now the high end, $600\,\mathrm{V}$ above ground: $v=+600\,\mathrm{V}$. The power is unchanged, $45\,\mathrm{W}$." show=t
#@ note "Reversed, the current goes down through the resistor, so its top is now $600\,\mathrm{V}$ above the bottom. Same $45\,\mathrm{W}$, flipped picture."
```

<details><summary>Solution</summary>

1. The source fixes the loop current (Topic 4). Its arrow points down, so current flows down through the source, around the bottom, and **up** through the resistor.
2. Current flows downhill through a resistor, so the resistor's bottom is its high end, $iR$ above its top. $v$ is marked $+$ at the top, the low end, so it is negative.

   $$iR=(0.075)(8000)=600\,\mathrm{V}\;\Rightarrow\;v=-600\,\mathrm{V}$$
3. Resistor power does not depend on direction.

   $$p_R=i^2R=(0.075)^2(8000)=45\,\mathrm{W}$$
4. Reversing the source reverses the current, so the top becomes the high end; the power is unchanged.

   $$v=+600\,\mathrm{V},\qquad p_R=45\,\mathrm{W}$$

**Answer:** **(a)** $v=-600\,\mathrm{V}$; **(b)** $45\,\mathrm{W}$. **(c)** $v=+600\,\mathrm{V}$, still $45\,\mathrm{W}$.

</details>

**Problem: Try it 13 · Identify a resistor from measurements (Textbook P2.15)** (introductory)

The terminal voltage and current of a device were measured with the references shown. Model the device as a single resistor.

```schematic
X1 0,3 -> 0,0 "device" i="$i$"
wire 0,3 -> 3,3
wire 0,0 -> 3,0
gap 3,3 -> 3,0 v="$v$"
#@ view "Row $i=40\,\mathrm{mA}$"
#@ node t 22.4 "top: $22.4\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ el X t g "device" col=0 i="$40\,\mathrm{mA}$" to=g plus=t v="$v$" id=eD
#@ step "Ground the bottom terminal. $v=22.4\,\mathrm{V}$ with $+$ on top: the top sits $22.4\,\mathrm{V}$ up." show=t
#@ step "$i=40\,\mathrm{mA}$ is drawn into the top terminal and is positive, so it flows down through the device: downhill, as a resistor's current must." show=eD
#@ step "Resistance = fall ÷ current: $\dfrac{22.4}{0.040}=560\,\Omega$."
#@ note "Current flows downhill through the device, as it must through a resistor. Every row of the table has the same ratio of height to current."
#@ view "Row $i=-40\,\mathrm{mA}$"
#@ node t -22.4 "top: $-22.4\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ el X t g "device" col=0 i="$40\,\mathrm{mA}$" to=t plus=t v="$v$" id=eD
#@ step "Ground the bottom terminal. $v=-22.4\,\mathrm{V}$ with $+$ on top: the top sits $22.4\,\mathrm{V}$ **below** the bottom." show=t
#@ step "$i=-40\,\mathrm{mA}$ into the top means $40\,\mathrm{mA}$ really flows **up** through the device, from the bottom (0) to the top ($-22.4\,\mathrm{V}$): still downhill." show=eD
#@ step "Same ratio, $\dfrac{22.4}{0.040}=560\,\Omega$. Every row gives $560\,\Omega$, so the device is a single $560\,\Omega$ resistor."
#@ note "Negative values flip the picture: the top terminal is now the low one, and the current still runs downhill."
```

| $i$ (mA) | $-40$ | $-20$ | $20$ | $40$ | $60$ |
|---|---|---|---|---|---|
| $v$ (V) | $-22.4$ | $-11.2$ | $11.2$ | $22.4$ | $33.6$ |

<details><summary>Solution</summary>

1. The arrow enters the device's top terminal, which is the $+$ of $v$: PSC holds, so $v=iR$ with a plus sign. In heights: in every row the current flows downhill, as a resistor's must.
2. Compute $\dfrac{v}{i}$ for every row. The ratio is the same each time, so the device is a linear resistor.

   $$\frac{22.4\,\mathrm{V}}{0.040\,\mathrm{A}}=\frac{-11.2}{-0.020}=\frac{33.6}{0.060}=560\,\Omega$$

**Answer:** $R=560\,\Omega$ (a standard value).

</details>

**Problem: Try it 14 · Headlamps and a switch (Textbook P2.13)** (introductory)

Textbook Fig. P2.13 is a wiring sketch, not a schematic. A $12\,\mathrm{V}$ battery's $+$ terminal runs through a switch to one terminal of each of two headlamps, A and B. The other terminal of each lamp, and the battery's $-$ terminal, are bolted to the car's metal frame.

1. Draw a circuit model using an ideal voltage source, a switch and resistors.
2. Convert it into heights with the switch closed. What voltage does each lamp get?
3. (Added) Model each lamp as $2.4\,\Omega$. Find each lamp's current and power, and the battery's current and power.
4. (Added) What does the picture look like with the switch open?

<details><summary>Solution</summary>

1. The frame joins the battery's $-$ terminal and both lamps, so it is **one node**, and the natural ground: in a car, *ground* literally is the chassis. Both lamps connect between the same two nodes, so they are in **parallel**. Open the height view and walk through it.

```schematic
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
S1 0,3 -> 3,3 "switch" state=closed
wire 3,3 -> 6,3
R1 3,3 -> 3,0 "lamp A" flip
R2 6,3 -> 6,0 "lamp B" flip
wire 6,0 -> 0,0
ground 0,0
#@ node t 12 "battery +: $12\,\mathrm{V}$"
#@ node s 12 "lamp tops: $12\,\mathrm{V}$"
#@ node g 0 "frame: $0\,\mathrm{V}$" ground
#@ node g2 0 "frame: $0\,\mathrm{V}$" ground
#@ node g3 0 "frame: $0\,\mathrm{V}$" ground
#@ el V t g "$12\,\mathrm{V}$" col=0 i="$10\,\mathrm{A}$" to=t id=eb
#@ el W t s "closed switch: no step" col=0 i="$10\,\mathrm{A}$" to=s id=ew
#@ el R s g2 "lamp A: falls $12\,\mathrm{V}$" col=1 i="$5\,\mathrm{A}$" to=g2 id=eA
#@ el R s g3 "lamp B: falls $12\,\mathrm{V}$" col=2 i="$5\,\mathrm{A}$" to=g3 id=eB
#@ step "Ground the frame. The battery (+ on top) holds its + terminal at $12\,\mathrm{V}$."
#@ step "The closed switch is a wire, so there is no step across it: both lamp tops are at $12\,\mathrm{V}$ too." show=s
#@ step "Each lamp falls the full $12\,\mathrm{V}$ to the frame, carrying $\dfrac{12}{2.4}=5\,\mathrm{A}$ and absorbing $(12)(5)=60\,\mathrm{W}$." show=eA,eB
#@ step "The two $5\,\mathrm{A}$ streams join in the frame and return through the battery, which lifts $10\,\mathrm{A}$ through $12\,\mathrm{V}$: $120\,\mathrm{W}$ delivered." show=eb,ew
#@ note "Parallel elements always share the same two heights. Here both lamps hang from the $12\,\mathrm{V}$ rail to the frame."
```
2. **(2)** A closed switch is no step, so both lamp tops sit at $12\,\mathrm{V}$ and both bottoms at the frame's $0$: each lamp falls the full $12\,\mathrm{V}$.

   $$v_A=v_B=12\,\mathrm{V}$$
3. **(3)** Current = fall ÷ resistance, and power = current × fall. The battery lifts both lamp currents.

   $$\begin{aligned}&i_A=i_B=\frac{12}{2.4}=5\,\mathrm{A},\qquad p_A=p_B=(12)(5)=60\,\mathrm{W}\\&i_{\text{bat}}=5+5=10\,\mathrm{A},\qquad p_{\text{bat}}=(12)(10)=120\,\mathrm{W}\end{aligned}$$
4. **(4)** Open: no current flows, so neither lamp falls anything. The lamp tops drop to the frame's $0$, and the open switch takes all of the $12\,\mathrm{V}$ step.

**Answer:** **(1)** The battery and switch in series feed lamps A and B in parallel; the frame is the common bottom node. **(2)** $12\,\mathrm{V}$ each. **(3)** $5\,\mathrm{A}$ and $60\,\mathrm{W}$ per lamp; the battery supplies $10\,\mathrm{A}$ and $120\,\mathrm{W}$. **(4)** The lamps sit at $0\,\mathrm{V}$ and the open switch takes the full $12\,\mathrm{V}$.

</details>

## Topic 6: Kirchhoff's laws and the height method

- **Node:** a point where two or more elements meet. A whole connected wire is one node.
- **Loop:** a closed path that doesn't pass through any node twice.
- **Series:** exactly two elements meet at a node, so they carry the **same current**.
- **Parallel:** elements connected across the same two nodes, so they have the **same voltage**.

$$\text{KCL: }\sum_{\text{node}}i_k=0\qquad\qquad \text{KVL: }\sum_{\text{loop}}v_k=0$$

| Law | In words | In heights |
|---|---|---|
| KCL | current into a node = current out (charge doesn't pile up) | the river: streams split and join, nothing is lost |
| KVL | the voltages around any loop add to zero | every node has one height, so around a loop the climbs equal the falls |

- Pick one sign rule per equation, e.g. leaving $=+$, entering $=-$. The opposite rule only multiplies the equation by $-1$.
- A circuit with $n$ nodes gives only $n-1$ independent KCL equations; the last one is redundant.
- Week 2 develops both laws fully; Week 1 uses them on single loops and simple branches.

### The height method recipe

Every **Walk me through it** follows the same six steps (the full rules are in *The Height Method: Complete Guide*):

1. **Pick ground**: usually the $-$ end of the main source, or the node most elements touch. It is the 0 V level.
2. **Place the fixed heights**: step across every voltage source from a known height (its $+$ end is higher by its value).
3. **Find currents**: a current source fixes its own current (never its step); a resistor carries fall ÷ $R$, always downhill; use KCL where branches meet.
4. **Place the rest**: walk down each resistor by $iR$ in the current's direction.
5. **If heights depend on each other** (two or more unknown nodes, Week 2 onward): name the unknown heights, write KCL at each, solve, then place them. The picture checks the algebra; it does not replace it.
6. **Answer and check**: voltages are height differences. Every node must have one height (KVL; if it can't, the connection is invalid), the currents must balance at every node (KCL), and the climbs must equal the falls (power: climbing delivers, falling absorbs).

**Drawing it on paper:** a vertical axis in volts with ground at 0, one level per node. Series elements stack in one column; parallel elements span the same two levels side by side. A node joined to the rest only through current sources has no fixed level: draw it dashed (it floats).

**Example: The lecture's loop, solved with heights (Eren slides 37–47)**

The lecture's flashlight loop with numbers: $v_s=24\,\mathrm{V}$, $R_1=2\,\Omega$, $R_c=1\,\Omega$ and $R_l=9\,\Omega$. Using the lecture's references, find all seven unknowns $i_s, i_1, i_c, i_l, v_1, v_c, v_l$, and check the power balance.

```schematic
V1 0,3 -> 0,0 "$24\,\mathrm{V}$" i_rev="$i_s$"
wire 0,3 -> 6,3
R3 6,3 -> 6,0 "$9\,\Omega$" v="$v_l$" i="$i_l$"
R2 3,0 -> 6,0 "$1\,\Omega$" v="$v_c$" i="$i_c$"
R1 3,0 -> 0,0 "$2\,\Omega$" v="$v_1$" i="$i_1$"
label 0,3 "$d$" above
label 6,0 "$c$" right
label 3,0 "$b$" below
label 0,0 "$a$" left
#@ spoiler
#@ node d 24 "$d$: $24\,\mathrm{V}$"
#@ node c 6 "$c$: $6\,\mathrm{V}$"
#@ node b 4 "$b$: $4\,\mathrm{V}$"
#@ node a 0 "$a$: $0\,\mathrm{V}$" ground
#@ el V d a "$24\,\mathrm{V}$" col=0 i="$2\,\mathrm{A}$" to=d id=es
#@ el R d c "$9\,\Omega$: falls $18\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=c id=e9 plus=d v="$v_l$"
#@ el R c b "$1\,\Omega$: falls $2\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=b id=e1 plus=b v="$v_c$"
#@ el R b a "$2\,\Omega$: falls $4\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=a id=e2 plus=b v="$v_1$"
#@ step "Ground the bottom-left corner: $a=0$. The source's + is at $d$, so $d$ is at $24\,\mathrm{V}$." show=d
#@ step "Every node joins just two elements, so this is one path with one current $I$. The charge has to fall all $24\,\mathrm{V}$ through the three resistors, and each fall is $IR$: $9I+1I+2I=24$, so $I=2\,\mathrm{A}$." show=es
#@ step "Walk down from $d$. The $9\,\Omega$ resistor falls $(2)(9)=18\,\mathrm{V}$, so $c$ is at $24-18=6\,\mathrm{V}$." show=e9,c
#@ step "The $1\,\Omega$ falls $(2)(1)=2\,\mathrm{V}$, so $b$ is at $4\,\mathrm{V}$. The $2\,\Omega$ falls the last $(2)(2)=4\,\mathrm{V}$ and lands exactly on ground, which checks the work." show=e1,b,e2
#@ step "Read the voltages off the picture: $v_1$ ($b$ above $a$) $=4\,\mathrm{V}$ and $v_l$ ($d$ above $c$) $=18\,\mathrm{V}$. $v_c$ is marked + at $b$, which is $2\,\mathrm{V}$ **below** $c$, so $v_c=-2\,\mathrm{V}$."
#@ step "Power = current × height change. The source lifts $2\,\mathrm{A}$ through $24\,\mathrm{V}$: $48\,\mathrm{W}$ delivered. The resistors absorb $(2)(18)=36$, $(2)(2)=4$ and $(2)(4)=8\,\mathrm{W}$: $48\,\mathrm{W}$ in total."
#@ note "Up $24\,\mathrm{V}$ through the source, then down $18+2+4=24\,\mathrm{V}$ through the resistors: KVL as a picture."
#@ note "$v_c=-2\,\mathrm{V}$ because its + mark is on $b$, the lower end of the $1\,\Omega$ resistor."
```

1. **Pick ground** at $a$. **Fixed heights:** the source's $+$ is at $d$, so $d$ is at $24\,\mathrm{V}$.

   $$V_d=24\,\mathrm{V}$$
2. **Currents:** every node joins just two elements, so all four are in series and carry one current $I$ (KCL). It must fall the whole $24\,\mathrm{V}$ through the three resistors (KVL: climbs = falls).

   $$9I+1I+2I=24\;\Rightarrow\;I=2\,\mathrm{A}$$
3. **Place the rest:** walk down from $d$, falling $IR$ through each resistor. Landing exactly on 0 checks the work.

   $$V_c=24-18=6\,\mathrm{V},\qquad V_b=6-2=4\,\mathrm{V},\qquad V_a=4-4=0\ \checkmark$$
4. **Answer:** read each label against the picture. $i_s$, $i_1$ and $i_l$ point the way the current flows; $i_c$ points against it. $v_c$ has its $+$ at $b$, the low end of $R_c$.

   $$\begin{aligned}&i_s=i_1=i_l=2\,\mathrm{A},\quad i_c=-2\,\mathrm{A}\\&v_l=18\,\mathrm{V},\quad v_c=-2\,\mathrm{V},\quad v_1=4\,\mathrm{V}\end{aligned}$$
5. **Check** the power: the source lifts $2\,\mathrm{A}$ through $24\,\mathrm{V}$, and the resistors absorb current × fall.

   $$(24)(2)=48\,\mathrm{W}=(18)(2)+(2)(2)+(4)(2)$$
6. The lecture does the same thing with symbols: one current that falls $v_s$ through the series resistors.

   $$I=\frac{v_s}{R_1+R_c+R_l},\qquad v_1=IR_1,\quad v_c=-IR_c,\quad v_l=IR_l$$

**Answer:** $i_s=i_1=i_l=2\,\mathrm{A}$, $i_c=-2\,\mathrm{A}$; $v_1=4\,\mathrm{V}$, $v_c=-2\,\mathrm{V}$, $v_l=18\,\mathrm{V}$. The source delivers $48\,\mathrm{W}$ and the resistors absorb $8+4+36=48\,\mathrm{W}$.

**Problem: Try it 15 · KCL at one node (based on Eren slide 40)** (introductory)

Currents $i_A$ and $i_B$ are referenced into the node; $i_C$ and $i_D$ are referenced out of it. Given $i_A=3\,\mathrm{A}$, $i_B=-1\,\mathrm{A}$ and $i_C=4\,\mathrm{A}$, find $i_D$ and say which way that current really flows.

```schematic
X1 -1,3 -> 1,3 "A" i="$i_A$"
wire 1,3 -> 3,3
X2 3,6 -> 3,4 "B" i="$i_B$"
wire 3,4 -> 3,3
wire 3,3 -> 5,3
X3 5,3 -> 7,3 "C" i="$i_C$"
wire 3,3 -> 3,2
X4 3,2 -> 3,0 "D" i="$i_D$"
dot 3,3
```

<details><summary>Solution</summary>

1. Write KCL with entering = +, leaving = −.

   $$i_A+i_B-i_C-i_D=0$$
2. Solve and substitute.

   $$i_D=i_A+i_B-i_C=3+(-1)-4=-2\,\mathrm{A}$$
3. Negative means opposite to the arrow: 2 A actually flows into the node through branch D.

**Answer:** $i_D=-2\,\mathrm{A}$: $2\,\mathrm{A}$ flows **into** the node through D.

</details>

**Problem: Try it 16 · Walk back from one known current (Textbook P2.20)** (intermediate)

The current $i_a$ is $2\,\mathrm{mA}$. Find **(a)** $i_o$, **(b)** $i_g$ and **(c)** the power delivered by the current source.

```schematic
I1 0,0 -> 0,3 "$i_g$"
wire 0,3 -> 2,3
R1 2,3 -> 2,0 "$2\,\mathrm{k\Omega}$" i="$i_o$"
R2 2,3 -> 5,3 "$1\,\mathrm{k\Omega}$" i="$i_a$"
R3 5,3 -> 5,0 "$4\,\mathrm{k\Omega}$" flip
R4 5,0 -> 2,0 "$3\,\mathrm{k\Omega}$"
wire 2,0 -> 0,0
label 2,3 "$a$" above
label 5,3 "$b$" above
label 5,0 "$c$" right
label 0,0 "$d$" left
#@ spoiler
#@ node a 16 "$a$: $16\,\mathrm{V}$"
#@ node b 14 "$b$: $14\,\mathrm{V}$"
#@ node c 6 "$c$: $6\,\mathrm{V}$"
#@ node d 0 "$d$: $0\,\mathrm{V}$" ground
#@ node d2 0 "$d$: $0\,\mathrm{V}$" ground
#@ node d3 0 "$d$: $0\,\mathrm{V}$" ground
#@ el I d a "$i_g$: $10\,\mathrm{mA}$" col=0 i="$10\,\mathrm{mA}$" to=a id=eg
#@ el R a d2 "$2\,\mathrm{k\Omega}$: falls $16\,\mathrm{V}$" col=1 i="$8\,\mathrm{mA}$" to=d2 id=eo
#@ el R a b "$1\,\mathrm{k\Omega}$: falls $2\,\mathrm{V}$" col=2 i="$2\,\mathrm{mA}$" to=b id=e1
#@ el R b c "$4\,\mathrm{k\Omega}$: falls $8\,\mathrm{V}$" col=2 i="$2\,\mathrm{mA}$" to=c id=e4
#@ el R c d3 "$3\,\mathrm{k\Omega}$: falls $6\,\mathrm{V}$" col=2 i="$2\,\mathrm{mA}$" to=d3 id=e3
#@ step "Ground the bottom wire $d$. The only number given is $i_a=2\,\mathrm{mA}$, so follow it: from $a$ it runs through the $1$, $4$ and $3\,\mathrm{k\Omega}$ resistors back to $d$. Every node on that path joins just two elements, so all three carry $2\,\mathrm{mA}$, downhill." show=e1,e4,e3
#@ step "Climb back up from ground, adding each fall $iR$. The $3\,\mathrm{k\Omega}$ falls $6\,\mathrm{V}$, so $c$ is at $6\,\mathrm{V}$. The $4\,\mathrm{k\Omega}$ falls $8\,\mathrm{V}$, so $b$ is at $14\,\mathrm{V}$. The $1\,\mathrm{k\Omega}$ falls $2\,\mathrm{V}$, so $a$ is at $16\,\mathrm{V}$." show=c,b,a
#@ step "The $2\,\mathrm{k\Omega}$ hangs straight from $a$ to ground, so it falls the full $16\,\mathrm{V}$: $i_o=\dfrac{16}{2000}=8\,\mathrm{mA}$, downhill, the way its arrow points." show=eo
#@ step "KCL at $a$: the river splits into $8\,\mathrm{mA}$ down the $2\,\mathrm{k\Omega}$ and $2\,\mathrm{mA}$ to the right, so the source must lift $i_g=10\,\mathrm{mA}$." show=eg
#@ step "Power = current × height change. The source lifts $10\,\mathrm{mA}$ from 0 to $16\,\mathrm{V}$: it delivers $160\,\mathrm{mW}$. The resistors absorb $128+4+16+12=160\,\mathrm{mW}$."
#@ note "Volts × milliamperes = milliwatts, and milliamperes × kilohms = volts: the units stay friendly."
```

<details><summary>Solution</summary>

1. Ground the bottom wire $d$. The given $i_a=2\,\mathrm{mA}$ flows through the $1$, $4$ and $3\,\mathrm{k\Omega}$ resistors in series and falls $iR$ in each ($\mathrm{mA}\times\mathrm{k\Omega}=\mathrm{V}$).

   $$(2)(1)=2\,\mathrm{V},\qquad(2)(4)=8\,\mathrm{V},\qquad(2)(3)=6\,\mathrm{V}$$
2. Stack the falls up from ground to place every node.

   $$c=6\,\mathrm{V},\qquad b=6+8=14\,\mathrm{V},\qquad a=14+2=16\,\mathrm{V}$$
3. **(a)** The $2\,\mathrm{k\Omega}$ spans $a$ to ground, so it falls $16\,\mathrm{V}$.

   $$i_o=\frac{16\,\mathrm{V}}{2\,\mathrm{k\Omega}}=8\,\mathrm{mA}$$
4. **(b)** KCL at $a$: everything the source lifts leaves through the two branches.

   $$i_g=i_o+i_a=8+2=10\,\mathrm{mA}$$
5. **(c)** The source lifts $10\,\mathrm{mA}$ through $16\,\mathrm{V}$. Check it against the resistors' falls.

   $$\begin{aligned}p_g&=(16)(10)=160\,\mathrm{mW}\\ \textstyle\sum p_R&=(16)(8)+(2)(2)+(8)(2)+(6)(2)=160\,\mathrm{mW}\end{aligned}$$

**Answer:** **(a)** $i_o=8\,\mathrm{mA}$. **(b)** $i_g=10\,\mathrm{mA}$. **(c)** $160\,\mathrm{mW}$ delivered.

</details>

## Practice problems

Exam-style problems, mostly from the textbook, each mixing at least two topics. Give each a real attempt (10–15 minutes) before opening the solution. For circuits, sketch the height picture first.

**Problem: Textbook P1.15 · Which way does power flow?** (intermediate)

Two circuits A and B are connected by two wires. The reference arrow for $i$ points from B to A along the top wire, and $v$ is $+$ on the top wire.

```schematic
X1 0,3 -> 0,0 "A"
wire 0,3 -> 5,3
wire 0,0 -> 5,0
X2 5,3 -> 5,0 "B" flip
gap 2.5,3 -> 2.5,0 v="$v$"
label 2.5,3 "$\leftarrow i$" above
#@ spoiler
#@ view "Case 1"
#@ node t -20 "top wire: $-20\,\mathrm{V}$"
#@ node g 0 "bottom wire: $0\,\mathrm{V}$" ground
#@ el X g t "A" col=0 i="$150\,\mathrm{mA}$" to=g id=eA plus=t v="$v$"
#@ el X g t "B" col=1 i="$150\,\mathrm{mA}$" to=t id=eB plus=t v="$v$"
#@ step "Ground the bottom wire. $v=-20\,\mathrm{V}$ with + on the top wire, so the top wire is $20\,\mathrm{V}$ **below** the bottom wire." show=t
#@ step "$i=+150\,\mathrm{mA}$ is positive, so the current really flows the way its arrow points: from B to A along the top wire, down through A, and back along the bottom wire." show=eA,eB
#@ step "Down through A means from the top wire ($-20\,\mathrm{V}$) to the bottom wire (0): **uphill**. A delivers $(20)(0.15)=3\,\mathrm{W}$ and B absorbs it, so power flows **from A to B**."
#@ note "The top wire is $20\,\mathrm{V}$ below the bottom wire. The current runs down through A, but from $-20\,\mathrm{V}$ to 0 that is uphill: A delivers and B absorbs. $3\,\mathrm{W}$ flows from A to B."
#@ view "Case 2"
#@ node t 40 "top wire: $40\,\mathrm{V}$"
#@ node g 0 "bottom wire: $0\,\mathrm{V}$" ground
#@ el X t g "A" col=0 i="$15\,\mathrm{A}$" to=g id=eA plus=t v="$v$"
#@ el X t g "B" col=1 i="$15\,\mathrm{A}$" to=t id=eB plus=t v="$v$"
#@ step "Ground the bottom wire. The top wire is at $v=+40\,\mathrm{V}$." show=t
#@ step "$i=+15\,\mathrm{A}$ follows its arrow: from B to A along the top wire, then down through A." show=eA,eB
#@ step "Through A: $40\,\mathrm{V}$ down to 0, downhill, so A absorbs $(40)(15)=600\,\mathrm{W}$. B lifts the charge and delivers it: power flows **from B to A**."
#@ note "Current falls through A (absorbs) and climbs through B (delivers): $600\,\mathrm{W}$ from B to A."
#@ view "Case 3"
#@ node t -2000 "top wire: $-2\,\mathrm{kV}$"
#@ node g 0 "bottom wire: $0\,\mathrm{V}$" ground
#@ el X g t "A" col=0 i="$50\,\mathrm{mA}$" to=t id=eA plus=t v="$v$"
#@ el X g t "B" col=1 i="$50\,\mathrm{mA}$" to=g id=eB plus=t v="$v$"
#@ step "Ground the bottom wire. $v=-2\,\mathrm{kV}$: the top wire is $2000\,\mathrm{V}$ below the bottom wire." show=t
#@ step "$i=-50\,\mathrm{mA}$ is negative, so the current runs against its arrow: from A to B along the top wire, which means **up** through A from the bottom wire." show=eA,eB
#@ step "Through A: from 0 to $-2000\,\mathrm{V}$, downhill, so A absorbs $(2000)(0.05)=100\,\mathrm{W}$. Power flows **from B to A**."
#@ note "Both signs are negative: the top wire is low and the real current runs from A to B along it. Through A it goes from 0 down to $-2\,\mathrm{kV}$ (downhill, A absorbs): $100\,\mathrm{W}$ from B to A."
#@ view "Case 4"
#@ node t 80 "top wire: $80\,\mathrm{V}$"
#@ node g 0 "bottom wire: $0\,\mathrm{V}$" ground
#@ el X t g "A" col=0 i="$3\,\mathrm{A}$" to=t id=eA plus=t v="$v$"
#@ el X t g "B" col=1 i="$3\,\mathrm{A}$" to=g id=eB plus=t v="$v$"
#@ step "Ground the bottom wire. The top wire is at $v=+80\,\mathrm{V}$." show=t
#@ step "$i=-3\,\mathrm{A}$ runs against its arrow: from A to B along the top wire, so up through A." show=eA,eB
#@ step "Through A: 0 up to $80\,\mathrm{V}$, uphill, so A delivers $(80)(3)=240\,\mathrm{W}$. Power flows **from A to B**."
#@ note "The real current runs from A to B along the top wire, so it climbs through A (A delivers) and falls through B: $240\,\mathrm{W}$ from A to B."
```

For each case, find the power and say whether it flows from A to B or from B to A.

1. $i=150\,\mathrm{mA}$, $v=-20\,\mathrm{V}$
2. $i=15\,\mathrm{A}$, $v=40\,\mathrm{V}$
3. $i=-50\,\mathrm{mA}$, $v=-2\,\mathrm{kV}$
4. $i=-3\,\mathrm{A}$, $v=80\,\mathrm{V}$

<details><summary>Solution</summary>

1. Heights: ground the bottom wire, so the top wire sits at $v$. Power flows from the box where the current climbs to the box where it falls.
2. PSC on box A: the arrow carries current into A's top terminal, which is $+$, so A absorbs $p_A=+vi$. Positive means power flows B → A; negative means A → B.

   $$p_A=vi$$
3. Substitute each case, converting prefixes first.

   $$\begin{aligned}&(1)\ (-20)(0.15)=-3\,\mathrm{W}\\&(2)\ (40)(15)=600\,\mathrm{W}\\&(3)\ (-2000)(-0.05)=100\,\mathrm{W}\\&(4)\ (80)(-3)=-240\,\mathrm{W}\end{aligned}$$

**Answer:** **(1)** $3\,\mathrm{W}$ from A to B. **(2)** $600\,\mathrm{W}$ from B to A. **(3)** $100\,\mathrm{W}$ from B to A. **(4)** $240\,\mathrm{W}$ from A to B.

</details>

**Problem: Textbook P2.18 · The river splits** (intermediate)

The current $i_x$ is $25\,\mathrm{mA}$ and the voltage $v_x$ is $25\,\mathrm{V}$. Before computing anything, ask: which node's height are you given?

```schematic
V1 0,3 -> 0,0 "$v_g$"
R1 0,3 -> 3,3 "$2\,\mathrm{k\Omega}$" i="$i_x$"
R2 3,3 -> 3,0 "$5\,\mathrm{k\Omega}$" v="$v_x$" flip
R3 3,3 -> 6,3 "$1\,\mathrm{k\Omega}$" i="$i_1$"
R4 6,3 -> 6,0 "$250\,\Omega$" v="$v_1$" flip
wire 6,0 -> 0,0
label 3,3 "$a$" above
label 6,3 "$b$" above
#@ spoiler
#@ node top 75 "top: $75\,\mathrm{V}$"
#@ node a 25 "$a$: $25\,\mathrm{V}$"
#@ node b 5 "$b$: $5\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V top g "$v_g$: $75\,\mathrm{V}$" col=0 i="$25\,\mathrm{mA}$" to=top id=eg
#@ el R top a "$2\,\mathrm{k\Omega}$: falls $50\,\mathrm{V}$" col=1 i="$25\,\mathrm{mA}$" to=a id=e2
#@ el R a g2 "$5\,\mathrm{k\Omega}$: falls $25\,\mathrm{V}$" col=1 i="$5\,\mathrm{mA}$" to=g2 id=e5 plus=a v="$v_x$"
#@ el R a b "$1\,\mathrm{k\Omega}$: falls $20\,\mathrm{V}$" col=2 i="$20\,\mathrm{mA}$" to=b id=e1
#@ el R b g3 "$250\,\Omega$: falls $5\,\mathrm{V}$" col=2 i="$20\,\mathrm{mA}$" to=g3 id=e250 plus=b v="$v_1$"
#@ step "Ground the bottom wire. $v_x=25\,\mathrm{V}$ (+ at the top) is a height you are given: node $a$ is at $25\,\mathrm{V}$." show=a
#@ step "The $5\,\mathrm{k\Omega}$ falls those $25\,\mathrm{V}$ to ground, so it carries $\dfrac{25}{5000}=5\,\mathrm{mA}$ down." show=e5
#@ step "KCL at $a$: $i_x=25\,\mathrm{mA}$ arrives and $5\,\mathrm{mA}$ drops down the $5\,\mathrm{k\Omega}$, so the river carries on with $i_1=20\,\mathrm{mA}$." show=e1
#@ step "The $1\,\mathrm{k\Omega}$ falls $(20\,\mathrm{mA})(1\,\mathrm{k\Omega})=20\,\mathrm{V}$, so $b$ is at $5\,\mathrm{V}$: $v_1=5\,\mathrm{V}$. Check: the $250\,\Omega$ falls $5\,\mathrm{V}$ and carries $\dfrac{5}{250}=20\,\mathrm{mA}$." show=b,e250
#@ step "Above $a$: the $2\,\mathrm{k\Omega}$ falls $(25\,\mathrm{mA})(2\,\mathrm{k\Omega})=50\,\mathrm{V}$, so the top is at $75\,\mathrm{V}$: $v_g=75\,\mathrm{V}$." show=top,e2,eg
#@ step "The source lifts $25\,\mathrm{mA}$ through $75\,\mathrm{V}$: $1.875\,\mathrm{W}$. The falls absorb $1.25+0.125+0.4+0.1=1.875\,\mathrm{W}$."
#@ note "Straight line view: the $75\,\mathrm{V}$ rail feeds one stream that splits at $a$, $5\,\mathrm{mA}$ straight down and $20\,\mathrm{mA}$ on to $b$."
```

Find **(a)** $i_1$, **(b)** $v_1$, **(c)** $v_g$ and **(d)** the power supplied by the voltage source.

<details><summary>Solution</summary>

1. Ground the bottom wire. $v_x=25\,\mathrm{V}$ with $+$ on top places node $a$ at $25\,\mathrm{V}$. The $5\,\mathrm{k\Omega}$ falls those $25\,\mathrm{V}$.

   $$i_{5\mathrm{k}}=\frac{25\,\mathrm{V}}{5\,\mathrm{k\Omega}}=5\,\mathrm{mA}$$
2. **(a)** KCL at $a$: what arrives through the $2\,\mathrm{k\Omega}$ leaves through the other two.

   $$i_1=25-5=20\,\mathrm{mA}$$
3. **(b)** Walk down from $a$ through the $1\,\mathrm{k\Omega}$.

   $$V_b=25-(20)(1)=5\,\mathrm{V}=v_1\qquad\left(\text{check: }\frac{5}{250}=20\,\mathrm{mA}\right)$$
4. **(c)** Walk up from $a$ through the $2\,\mathrm{k\Omega}$ (the current falls through it, so the top is higher).

   $$v_g=25+(25)(2)=75\,\mathrm{V}$$
5. **(d)** The source lifts $25\,\mathrm{mA}$ through $75\,\mathrm{V}$. Check against the four falls.

   $$p=(75)(0.025)=1.875\,\mathrm{W}=1.25+0.125+0.4+0.1$$

**Answer:** **(a)** $i_1=20\,\mathrm{mA}$. **(b)** $v_1=5\,\mathrm{V}$. **(c)** $v_g=75\,\mathrm{V}$. **(d)** $1.875\,\mathrm{W}$.

</details>

**Problem: Assessment AP 1.6 (Textbook P1.18) · Peak power and total energy** (intermediate)

The voltage and current of an element are zero for $t<0$. For $t\ge0$,

$$v=80\,000\,te^{-500t}\ \mathrm{V},\qquad i=15\,te^{-500t}\ \mathrm{A},$$

with the arrow entering the $+$ terminal. Find **(a)** the time of maximum power, **(b)** the maximum power and **(c)** the total energy delivered to the element.

<details><summary>Solution</summary>

1. PSC holds, so multiply.

   $$p=vi=1.2\times10^{6}\,t^2e^{-1000t}\ \mathrm{W}$$
2. Set the derivative to zero (product rule). $t=0$ is a minimum, so the maximum is where the bracket vanishes.

   $$\frac{dp}{dt}=1.2\times10^{6}\,e^{-1000t}\,(2t-1000t^2)=0\;\Rightarrow\;t=\frac{2}{1000}=2\,\mathrm{ms}$$
3. Evaluate.

   $$p(0.002)=1.2\times10^{6}(0.002)^2e^{-2}=0.6496\,\mathrm{W}$$
4. Total energy is the area under $p$. A standard integral, or integration by parts twice, gives $\int_0^\infty t^2e^{-at}\,dt=\dfrac{2}{a^3}$.

   $$w=1.2\times10^{6}\cdot\frac{2}{1000^3}=2.4\times10^{-3}\,\mathrm{J}$$

**Answer:** **(a)** $2\,\mathrm{ms}$. **(b)** $649.6\,\mathrm{mW}$. **(c)** $2.4\,\mathrm{mJ}$.

</details>

**Problem: Textbook P2.6 · Choose the gain** (intermediate)

**(a)** What value of $\alpha$ makes the connection valid? **(b)** For that value, find the power of the $25\,\mathrm{V}$ source.

```schematic
I1 0,3 -> 0,0 "$15\,\mathrm{A}$"
G1 0,3 -> 4,3 "$\alpha v_x$"
V1 4,0 -> 4,3 "$25\,\mathrm{V}$" v_rev="$v_x$" flip
wire 4,0 -> 0,0
#@ spoiler
#@ node tl 10 "top left: undetermined" unknown
#@ node tr -25 "top right: $-25\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ el I tl g "$15\,\mathrm{A}$" col=0 i="$15\,\mathrm{A}$" to=g id=e15
#@ el V g tr "$25\,\mathrm{V}$" col=1 i="$15\,\mathrm{A}$" to=tr id=e25 plus=tr v="$v_x$"
#@ el G tl tr "$\alpha v_x$" col=2 i="$15\,\mathrm{A}$" to=tl id=eg
#@ step "Ground the bottom wire. The $25\,\mathrm{V}$ source has its + at the bottom, so the top-right node is $25\,\mathrm{V}$ **below** ground. $v_x$ is marked + at that node, so $v_x=-25\,\mathrm{V}$." show=tr
#@ step "One loop, so one current. The $15\,\mathrm{A}$ source pushes $15\,\mathrm{A}$ down the left side; it comes back up through the $25\,\mathrm{V}$ source and leftward through the diamond." show=e15,e25,eg
#@ step "The diamond's arrow points right, but $15\,\mathrm{A}$ flows left through it: $\alpha v_x=-15\,\mathrm{A}$, so $\alpha=\dfrac{-15}{-25}=0.6\,\mathrm{A/V}$."
#@ step "Through the $25\,\mathrm{V}$ source the current goes from 0 down to $-25\,\mathrm{V}$. That is downhill, so the source **absorbs** $(25)(15)=375\,\mathrm{W}$."
#@ step "The top-left node stays dashed: with two current sources in a row, nothing fixes its height. Only their combined lift, $25\,\mathrm{V}$ back up to ground, is known, so together they deliver the $375\,\mathrm{W}$."
#@ note "$v_x=-25\,\mathrm{V}$: the top right node is $25\,\mathrm{V}$ below ground. The $15\,\mathrm{A}$ loop current comes up through the $25\,\mathrm{V}$ source, which is downhill (0 to $-25\,\mathrm{V}$), so that source absorbs $375\,\mathrm{W}$."
#@ note "The top left node is dashed: two current sources in series leave its height undetermined. Only their combined lift, from $-25\,\mathrm{V}$ back to 0, is fixed, so together they deliver the $375\,\mathrm{W}$."
```

<details><summary>Solution</summary>

1. Read the control first. The 25 V source has $+$ at the bottom, but $v_x$ is marked $+$ at the top.

   $$v_x=-25\,\mathrm{V}$$
2. The two current sources share one path (series), so their currents must match. Around the loop, the 15 A source's arrow (down) and the dependent source's arrow (right) point in opposite senses, so

   $$\alpha v_x=-15\,\mathrm{A}\;\Rightarrow\;\alpha=\frac{-15\,\mathrm{A}}{-25\,\mathrm{V}}=0.6\,\mathrm{A/V}$$
3. Heights: ground the bottom wire; the top-right node is $25\,\mathrm{V}$ below it. The $15\,\mathrm{A}$ comes up through the $25\,\mathrm{V}$ source, from 0 down to $-25\,\mathrm{V}$: it falls, so the source absorbs.

   $$p_{25}=(25)(15)=375\,\mathrm{W}\ \text{absorbed}$$
4. PSC check: take the current downward through the source, $i_x=\alpha v_x=-15\,\mathrm{A}$. That arrow enters the source's top, its $-$ terminal, so $p=-vi$.

   $$p_{25}=-(25)(-15)=+375\,\mathrm{W}$$

**Answer:** **(a)** $\alpha=0.6\,\mathrm{A/V}=0.6\,\mathrm{S}$. **(b)** The $25\,\mathrm{V}$ source **absorbs** $375\,\mathrm{W}$.

</details>

**Problem: Textbook P1.28 · Charging a battery** (intermediate)

An industrial battery is charged at a constant $240\,\mathrm{V}$. The charging current starts at $5\,\mathrm{mA}$ and rises linearly to $10\,\mathrm{mA}$ at $5\,\mathrm{ks}$, stays at $10\,\mathrm{mA}$ until $10\,\mathrm{ks}$, then falls linearly to $5\,\mathrm{mA}$ at $15\,\mathrm{ks}$, when the charger is disconnected.

1. Sketch the current from $0$ to $15\,\mathrm{ks}$.
2. Sketch the power delivered to the battery.
3. Use the power sketch to find the total energy delivered.

<details><summary>Solution</summary>

1. Current: a trapezoid through the points below ($1\,\mathrm{ks}=1000\,\mathrm{s}$).

   $$\begin{array}{c|cccc}t\ (\mathrm{ks})&0&5&10&15\\\hline i\ (\mathrm{mA})&5&10&10&5\end{array}$$
2. The charger pushes current into the battery's $+$ terminal, so it falls through the battery: the battery absorbs $p=vi=240\,i$. Power has the same shape, scaled.

   $$\begin{array}{c|cccc}t\ (\mathrm{ks})&0&5&10&15\\\hline p\ (\mathrm{W})&1.2&2.4&2.4&1.2\end{array}$$
3. Energy is the area under $p$: two trapezoids with average 1.8 W and one rectangle at 2.4 W, each 5000 s wide.

   $$\begin{aligned}w&=(1.8+2.4+1.8)(5000)\\&=9+12+9=30\,\mathrm{kJ}\end{aligned}$$
4. Check another way: total charge is the area under $i$, and with constant $v$, $w=qv$ (Topic 2).

   $$Q=37.5+50+37.5=125\,\mathrm{C},\qquad w=(240)(125)=30\,\mathrm{kJ}$$

**Answer:** **(1–2)** Trapezoids: $i$ goes $5\to10\to10\to5\,\mathrm{mA}$ and $p$ goes $1.2\to2.4\to2.4\to1.2\,\mathrm{W}$, at breakpoints $0,5,10,15\,\mathrm{ks}$. **(3)** $30\,\mathrm{kJ}$.

</details>

**Problem: Textbook P2.8 · Is it valid?** (intermediate)

If the connection is valid, find the total power developed. If it is not valid, explain why.

```schematic
V1 0,4 -> 0,2 "$50\,\mathrm{V}$"
E1 0,0 -> 0,2 "$6i_\Delta$"
I1 3,2.5 -> 3,4 "$25\,\mathrm{A}$"
wire 3,2.5 -> 3,2
V2 3,2 -> 3,0 "$80\,\mathrm{V}$"
label 3,2.25 "$\downarrow i_\Delta$" right
V3 6,4 -> 6,0 "$250\,\mathrm{V}$" flip
wire 0,4 -> 6,4
wire 0,0 -> 6,0
#@ spoiler
#@ node t2 250 "top, via the 250 V source: $250\,\mathrm{V}$"
#@ node t1 200 "top, via the left branch: $200\,\mathrm{V}$"
#@ node m1 150 "left branch, middle: $150\,\mathrm{V}$"
#@ node m2 80 "middle branch, middle: $80\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t2 g "$250\,\mathrm{V}$" col=0
#@ el V m2 g "$80\,\mathrm{V}$" col=1
#@ el I m2 t2 "$25\,\mathrm{A}$" col=1
#@ el E g m1 "$6i_\Delta$" col=2
#@ el V t1 m1 "$50\,\mathrm{V}$" col=2
#@ mismatch t1 t2 "one node can't be at two heights"
#@ step "Ground the bottom wire. The $250\,\mathrm{V}$ source puts the top wire at $250\,\mathrm{V}$." show=t2
#@ step "Find the control: the middle branch carries the $25\,\mathrm{A}$ source's current upward, and $i_\Delta$ is drawn downward, so $i_\Delta=-25\,\mathrm{A}$. The dependent source's value is $6i_\Delta=-150\,\mathrm{V}$."
#@ step "Climb the left branch from ground. The dependent source is + at its bottom with value $-150\,\mathrm{V}$, so its top is $150\,\mathrm{V}$ **higher** than its bottom: $150\,\mathrm{V}$." show=m1
#@ step "The $50\,\mathrm{V}$ source (+ on top) adds $50\,\mathrm{V}$, so the left branch reaches the top wire at $200\,\mathrm{V}$." show=t1
#@ step "The top wire is one node, and the $250\,\mathrm{V}$ source already holds it at $250\,\mathrm{V}$. One node can't be at two heights: **the connection is invalid**. (The middle branch causes no trouble: its $80\,\mathrm{V}$ source puts its middle at $80\,\mathrm{V}$, and the current source takes whatever difference is left.)" show=m2
#@ note "Climb the left branch from ground. The dependent source is + at the bottom with value $6i_\Delta=-150\,\mathrm{V}$, so going up through it rises $150\,\mathrm{V}$, and the $50\,\mathrm{V}$ source adds $50\,\mathrm{V}$: the top would be at $200\,\mathrm{V}$."
#@ note "The $250\,\mathrm{V}$ source puts that same top node at $250\,\mathrm{V}$. A node has one height, so the connection is invalid. (The middle branch is fine: its current source can take any voltage.)"
```

<details><summary>Solution</summary>

1. Ground the bottom wire. The $250\,\mathrm{V}$ source fixes the top wire at $250\,\mathrm{V}$.
2. Find the control. The middle branch carries the 25 A source's current, which flows up; $i_\Delta$ points down.

   $$i_\Delta=-25\,\mathrm{A}\;\Rightarrow\;6i_\Delta=-150\,\mathrm{V}$$
3. Climb the left branch from ground. The dependent source is $+$ at its bottom with value $-150\,\mathrm{V}$, so going up through it rises $150\,\mathrm{V}$; the 50 V source adds 50 V.

   $$V_{\text{top}}=150+50=200\,\mathrm{V}$$
4. The top wire is one node, but it would need two heights. KVL is violated.

   $$200\,\mathrm{V}\neq250\,\mathrm{V}$$

**Answer:** **Not valid:** the left branch forces $200\,\mathrm{V}$ between the top and bottom nodes, but the $250\,\mathrm{V}$ source forces $250\,\mathrm{V}$.

</details>

**Problem: A step that depends on the current** (intermediate)

The diamond is a current-controlled voltage source whose step is $2i$ volts ($i$ in amperes), $+$ at its top. Ground the bottom wire.

```schematic
V1 0,3 -> 0,0 "$24\,\mathrm{V}$"
R1 0,3 -> 4,3 "$4\,\Omega$" i="$i$"
E1 4,3 -> 4,0 "$2i$" flip
wire 4,0 -> 0,0
label 4,3 "$x$" above
#@ spoiler
#@ view "As drawn"
#@ node tl 24 "top left: $24\,\mathrm{V}$"
#@ node x 8 "$x$: $8\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V tl g "$24\,\mathrm{V}$" col=0 i="$4\,\mathrm{A}$" to=tl id=eV
#@ el R tl x "$4\,\Omega$: falls $16\,\mathrm{V}$" col=1 i="$4\,\mathrm{A}$" to=x id=eR
#@ el E x g "$2i$: steps $8\,\mathrm{V}$" col=1 i="$4\,\mathrm{A}$" to=g id=eE
#@ step "Ground the bottom wire. The $24\,\mathrm{V}$ source (+ on top) puts the top-left corner at $24\,\mathrm{V}$." show=tl
#@ step "One loop, so one current $i$. Walk it clockwise from ground: up $24$ through the source, down $4i$ through the resistor, then down $2i$ through the diamond (its + is on top). You must land back on 0: $24-4i-2i=0$, so $i=4\,\mathrm{A}$." show=eV
#@ step "The resistor falls $(4)(4)=16\,\mathrm{V}$, so $x$ is at $8\,\mathrm{V}$. The diamond then steps exactly $2i=8\,\mathrm{V}$ down to ground, which checks the work." show=eR,x,eE
#@ step "Power: the source lifts $4\,\mathrm{A}$ through $24\,\mathrm{V}$ and delivers $96\,\mathrm{W}$. The current falls through the resistor ($(16)(4)=64\,\mathrm{W}$) and through the diamond ($(8)(4)=32\,\mathrm{W}$): both absorb, $64+32=96$."
#@ view "Diamond flipped"
#@ node tl 24 "top left: $24\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node x -24 "$x$: $-24\,\mathrm{V}$"
#@ el V tl g "$24\,\mathrm{V}$" col=0 i="$12\,\mathrm{A}$" to=tl id=eV
#@ el R tl x "$4\,\Omega$: falls $48\,\mathrm{V}$" col=1 i="$12\,\mathrm{A}$" to=x id=eR
#@ el E g2 x "$2i$ (flipped): steps $24\,\mathrm{V}$" col=2 i="$12\,\mathrm{A}$" to=g2 id=eE
#@ step "Same ground (the bottom wire) and the same source, so the top-left corner is still at $24\,\mathrm{V}$." show=tl
#@ step "Flipped, the diamond's + is at the bottom, so walking down through it now **climbs** $2i$. Around the loop: $24-4i+2i=0$, so $i=12\,\mathrm{A}$." show=eV
#@ step "The diamond's top, $x$, is $2i=24\,\mathrm{V}$ **below** ground: $-24\,\mathrm{V}$. So the resistor falls all the way from $+24$ to $-24$: $48\,\mathrm{V}=(12)(4)$, which checks." show=x,eR,eE
#@ step "Now both sources lift the charge: the $24\,\mathrm{V}$ source delivers $(24)(12)=288\,\mathrm{W}$ and the diamond, climbing from $-24$ to 0, delivers $288\,\mathrm{W}$. The resistor absorbs $(48)(12)=576\,\mathrm{W}$."
#@ note "A dependent source is still just a step. Its size waits on the current, so write the loop equation first, then place the levels."
```

1. Find $i$ and the voltage of node $x$.
2. Which elements absorb power? Check the balance.
3. Repeat with the diamond flipped ($+$ at its bottom).

<details><summary>Solution</summary>

1. Ground the bottom wire; the top-left corner is at $24\,\mathrm{V}$. One loop means one current $i$; the resistor falls $4i$ in the direction of $i$.
2. Walk the loop clockwise from ground, adding climbs and subtracting falls. The diamond's $+$ is on top, so going down through it falls $2i$.

   $$24-4i-2i=0\;\Rightarrow\;i=4\,\mathrm{A}$$
3. Place $x$: start at $24\,\mathrm{V}$ and fall $4i$. It matches the diamond's step.

   $$V_x=24-(4)(4)=8\,\mathrm{V}=2i\ \checkmark$$
4. Power = current × height change: the current falls through the resistor and the diamond, and climbs through the source.

   $$\begin{aligned}p_R&=(16)(4)=64\,\mathrm{W}\\ p_{\diamond}&=(8)(4)=32\,\mathrm{W}\\ p_{24}&=-(24)(4)=-96\,\mathrm{W}\end{aligned}$$
5. Flipped: going down through the diamond now climbs $2i$.

   $$24-4i+2i=0\;\Rightarrow\;i=12\,\mathrm{A},\qquad V_x=-2i=-24\,\mathrm{V}$$
6. Both sources now lift the charge, and the resistor falls $48\,\mathrm{V}$.

   $$p_R=(48)(12)=576\,\mathrm{W},\quad p_{\diamond}=-288\,\mathrm{W},\quad p_{24}=-288\,\mathrm{W}$$

**Answer:** **(1)** $i=4\,\mathrm{A}$, $V_x=8\,\mathrm{V}$. **(2)** The resistor ($64\,\mathrm{W}$) and the diamond ($32\,\mathrm{W}$) absorb; the source delivers $96\,\mathrm{W}$. **(3)** $i=12\,\mathrm{A}$ and $V_x=-24\,\mathrm{V}$; each source delivers $288\,\mathrm{W}$ and the resistor absorbs $576\,\mathrm{W}$.

</details>

**Problem: Textbook P2.9 · Total power developed** (advanced)

Find the total power developed in the circuit.

```schematic
V1 0,4 -> 0,2 "$50\,\mathrm{V}$"
I1 0,2 -> 0,0 "$75\,\mathrm{A}$"
G1 3,2 -> 3,4 "$5v_\Delta$"
V2 3,0 -> 3,2 "$20\,\mathrm{V}$"
I2 6,0 -> 6,4 "$25\,\mathrm{A}$" v_rev="$v_\Delta$" flip
wire 0,4 -> 6,4
wire 0,0 -> 6,0
#@ spoiler
#@ node t 10 "top: $10\,\mathrm{V}$"
#@ node m1 -40 "left middle: $-40\,\mathrm{V}$"
#@ node m2 -20 "middle: $-20\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t m1 "$50\,\mathrm{V}$" col=0 i="$75\,\mathrm{A}$" to=m1 id=e50
#@ el I m1 g "$75\,\mathrm{A}$" col=1 i="$75\,\mathrm{A}$" to=g id=e75
#@ el I g t "$25\,\mathrm{A}$" col=2 i="$25\,\mathrm{A}$" to=t id=e25 plus=t v="$v_\Delta$"
#@ el V g m2 "$20\,\mathrm{V}$" col=3 i="$50\,\mathrm{A}$" to=m2 id=e20
#@ el G m2 t "$5v_\Delta$" col=4 i="$50\,\mathrm{A}$" to=t id=eg
#@ step "All three branches run between the same two wires. Ground the bottom wire; the top wire's height is $v_\Delta$, still unknown."
#@ step "Every branch has a current source, so find the currents first. Charge can't pile up on the top wire: $25\,\mathrm{A}$ and $5v_\Delta$ come up, $75\,\mathrm{A}$ goes down. So $5v_\Delta+25=75$, giving $v_\Delta=10\,\mathrm{V}$ and $5v_\Delta=50\,\mathrm{A}$." show=t,e50,e75,e25,e20,eg
#@ step "Left branch, going down from the top ($10\,\mathrm{V}$): the $50\,\mathrm{V}$ source has + on top, so it drops the charge $50\,\mathrm{V}$ to $-40\,\mathrm{V}$. The $75\,\mathrm{A}$ source then lifts it $40\,\mathrm{V}$ back to ground." show=m1
#@ step "Middle branch, going up from ground: the $20\,\mathrm{V}$ source has + at ground, so the charge first drops $20\,\mathrm{V}$ to $-20\,\mathrm{V}$. The dependent source then lifts it $30\,\mathrm{V}$ to the top." show=m2
#@ step "Green (uphill) arrows deliver: $75\,\mathrm{A}\times40\,\mathrm{V}=3000\,\mathrm{W}$, $50\times30=1500\,\mathrm{W}$, $25\times10=250\,\mathrm{W}$. **Total developed: $4750\,\mathrm{W}$**, absorbed by the $50\,\mathrm{V}$ ($3750\,\mathrm{W}$) and $20\,\mathrm{V}$ ($1000\,\mathrm{W}$) sources."
#@ note "Every branch joins the same two levels, 0 and $10\,\mathrm{V}$, by a different path. Left: from the top the charge falls $50\,\mathrm{V}$ through the $50\,\mathrm{V}$ source to $-40\,\mathrm{V}$, then the $75\,\mathrm{A}$ source lifts it $40\,\mathrm{V}$ back to 0."
#@ note "Middle: it falls $20\,\mathrm{V}$ through the $20\,\mathrm{V}$ source, then the dependent source lifts it $30\,\mathrm{V}$ to the top. The green (uphill) arrows are the power developed: $3000+1500+250=4750\,\mathrm{W}$."
```

<details><summary>Solution</summary>

1. Ground the bottom wire; the top wire's height is $v_\Delta$, still unknown. Every branch has a current source, so find the currents first. KCL at the top wire, in = out:

   $$5v_\Delta+25=75\;\Rightarrow\;v_\Delta=10\,\mathrm{V}$$
2. Right branch: the 25 A source lifts its current from 0 to $10\,\mathrm{V}$, so it delivers.

   $$p_{25\mathrm{A}}=-(10)(25)=-250\,\mathrm{W}$$
3. Left branch, down from the top ($10\,\mathrm{V}$): the 50 V source ($+$ on top) drops the 75 A to $-40\,\mathrm{V}$, then the 75 A source lifts it $40\,\mathrm{V}$ back to ground.

   $$p_{50\mathrm{V}}=+(50)(75)=3750\,\mathrm{W},\qquad p_{75\mathrm{A}}=-(40)(75)=-3000\,\mathrm{W}$$
4. Middle branch, up from ground: $5v_\Delta=50\,\mathrm{A}$ first falls $20\,\mathrm{V}$ through the 20 V source ($+$ at the bottom) to $-20\,\mathrm{V}$, then the diamond lifts it $30\,\mathrm{V}$ to the top.

   $$p_{20\mathrm{V}}=+(20)(50)=1000\,\mathrm{W},\qquad p_{\mathrm{dep}}=-(30)(50)=-1500\,\mathrm{W}$$
5. Check the balance, then add the delivered powers.

   $$\begin{aligned}&-250+3750-3000+1000-1500=0\\&P_{\text{developed}}=250+3000+1500=4750\,\mathrm{W}\end{aligned}$$

**Answer:** $4750\,\mathrm{W}$ developed (25 A source $250\,\mathrm{W}$, 75 A source $3000\,\mathrm{W}$, dependent source $1500\,\mathrm{W}$), absorbed by the $50\,\mathrm{V}$ ($3750\,\mathrm{W}$) and $20\,\mathrm{V}$ ($1000\,\mathrm{W}$) sources.

</details>

## Summary: Week 1 in one read

> **Tip:** **One picture runs all of Week 1: voltage is height.** Charge is water, a source is a pump that lifts it, a resistor is a slide it falls down, and wires are flat. Each part below is one idea + one picture + an example. Each example has its height picture drawn right under the circuit. The table at the end says which part each practice problem needs.

### A · The five quantities

| Quantity | Picture it as | Formula | Unit |
|---|---|---|---|
| Charge $q$ | the water | one electron $=-1.6\times10^{-19}\,\mathrm{C}$ | $\mathrm{C}$ |
| Current $i$ | how much water passes per second | $i=dq/dt$ | $\mathrm{A}$ |
| Voltage $v$ | the **height difference** between two points | $v=dw/dq$ | $\mathrm{V}$ |
| Power $p$ | height × flow: energy per second | $p=vi$ | $\mathrm{W}$ |
| Energy $w$ | power piled up over time | $w=pt$ (constant $p$) | $\mathrm{J}$ |

```schematic
V1 0,3 -> 0,0 "$9\,\mathrm{V}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "lamp" i="$0.5\,\mathrm{A}$" flip
wire 3,0 -> 0,0
ground 0,0
#@ inline
#@ straight off
#@ node t 9 "top wire: $9\,\mathrm{V}$"
#@ node g 0 "bottom wire: $0\,\mathrm{V}$" ground
#@ el V t g "battery: lifts $9\,\mathrm{V}$" col=0 i="$0.5\,\mathrm{A}$" to=t id=eb
#@ el R t g "lamp: falls $9\,\mathrm{V}$" col=1 i="$0.5\,\mathrm{A}$" to=g id=el
#@ step "Ground the bottom wire. The battery's + end is $9\,\mathrm{V}$ up, so the top wire is at $9\,\mathrm{V}$." show=t
#@ step "The battery lifts $0.5\,\mathrm{A}$ up $9\,\mathrm{V}$ (it delivers $4.5\,\mathrm{W}$), and the same $0.5\,\mathrm{A}$ falls $9\,\mathrm{V}$ through the lamp (it absorbs $4.5\,\mathrm{W}$)." show=eb,el
```

**Example: A1 · One battery, every quantity**

The $9\,\mathrm{V}$ battery above pushes $0.5\,\mathrm{A}$ through the lamp for $1\,\mathrm{h}$. Find the charge that flows, the power, and the energy (two ways).

1. Charge = current × time. Time in **seconds**.

   $$q=it=(0.5)(3600)=1800\,\mathrm{C}$$
2. Power = height × flow.

   $$p=vi=(9)(0.5)=4.5\,\mathrm{W}$$
3. Energy, way 1: power × time.

   $$w=pt=(4.5)(3600)=16\,200\,\mathrm{J}$$
4. Energy, way 2: every coulomb falls $9\,\mathrm{V}$, giving up $9\,\mathrm{J}$. Same answer, because it is the same chain.

   $$w=qv=(1800)(9)=16\,200\,\mathrm{J}$$

**Answer:** $1800\,\mathrm{C}$, $4.5\,\mathrm{W}$, $16.2\,\mathrm{kJ}$.

**When things change with time**, the same chain needs calculus. There are only four moves:

| You have | You want | Do this |
|---|---|---|
| $q(t)$ | $i(t)$ | differentiate |
| $i(t)$ | charge that flowed | integrate = **area** under the $i$ graph |
| $v(t)$ and $i(t)$ | biggest power | $p=vi$, then set $dp/dt=0$ |
| $p(t)$ | energy | integrate = **area** under the $p$ graph |

- Graph made of straight lines? Don't integrate, add up **triangles, rectangles and trapezoids**.
- Voltage constant? Then $w=v\times(\text{area under }i)$, because $w=vq$.
- Peak of $te^{-at}$ is at $t=1/a$; peak of $t^2e^{-at}$ is at $t=2/a$ (Week 0 shows why). The integrals that come up:

$$\int_0^\infty e^{-at}dt=\frac1a,\qquad \int_0^\infty te^{-at}dt=\frac{1}{a^2},\qquad \int_0^\infty t^2e^{-at}dt=\frac{2}{a^3}$$

**Example: A2 · Charge, peak power and energy from a decaying current**

A current $i=6e^{-3t}\,\mathrm{A}$ ($t\ge0$) enters the $+$ end of an element whose voltage stays at $5\,\mathrm{V}$. Find the total charge, the peak power and the total energy.

1. Charge = area under $i$.

   $$q=\int_0^\infty 6e^{-3t}\,dt=\frac{6}{3}=2\,\mathrm{C}$$
2. Power = $vi$. It is biggest at the start, because $e^{-3t}$ only shrinks.

   $$p=5\cdot6e^{-3t}=30e^{-3t}\,\mathrm{W},\qquad p_{\max}=p(0)=30\,\mathrm{W}$$
3. Energy = area under $p$. Check with $w=vq$ (constant $v$).

   $$w=\int_0^\infty 30e^{-3t}\,dt=\frac{30}{3}=10\,\mathrm{J}=(5)(2)\ \checkmark$$

**Answer:** $2\,\mathrm{C}$, $30\,\mathrm{W}$ at $t=0$, $10\,\mathrm{J}$.

### B · Who absorbs and who delivers (the sign convention)

> **Info:** **Follow the real current through the element.** Goes **down** (in at the high end) → **absorbs**. Goes **up** (in at the low end) → **delivers**. How much: current × height.

- Reading the drawing: $+$ at $a$ and $v>0$ → $a$ is the **high** end. $v<0$ → $a$ is the **low** end.
- Current arrow with $i>0$ → flows **along** the arrow. $i<0$ → flows **against** it.
- Exam formula (same rule): arrow into $+$ → $p=vi$; arrow into $-$ → $p=-vi$. Positive = absorbs.
- Every circuit balances: total delivered = total absorbed.

```schematic
B1 0,3 -> 0,0 "car A (dead)" v i="$30\,\mathrm{A}$"
wire 0,3 -> 5,3
B2 5,3 -> 5,0 "car B (good)" v flip
wire 5,0 -> 0,0
#@ inline
#@ straight off
#@ node top 12 "both + terminals: $12\,\mathrm{V}$"
#@ node g 0 "both − terminals: $0\,\mathrm{V}$" ground
#@ el B top g "car A: absorbs" col=0 i="$30\,\mathrm{A}$" to=g id=eA
#@ el B top g "car B: delivers" col=1 i="$30\,\mathrm{A}$" to=top id=eB
#@ step "Ground the − terminals. Both + terminals are joined, so they share one height: $12\,\mathrm{V}$." show=top
#@ step "The $30\,\mathrm{A}$ climbs through car B (B delivers $360\,\mathrm{W}$) and falls through car A (A absorbs $360\,\mathrm{W}$): car A is being charged." show=eA,eB
```

**Example: B1 · The sign drill (four cases, one element)**

An element has $v$ marked $+$ on top and the current arrow pointing **into the top**. For each case, say who is higher, which way the current really goes, and whether the element absorbs or delivers.

```schematic
terminal 0,3 "top" left
X1 0,3 -> 0,0 "element" v="$v$" i="$i$"
terminal 0,0 "bottom" left
#@ inline
#@ straight off
#@ view "Case 1: $v=+10$, $i=+2$"
#@ node top 10 "top: $10\,\mathrm{V}$"
#@ node bot 0 "bottom: $0\,\mathrm{V}$" ground
#@ el X top bot "falls: absorbs $20\,\mathrm{W}$" col=0 i="$2\,\mathrm{A}$" to=bot id=eX plus=top v="$v$"
#@ step "Ground the bottom. $v=+10\,\mathrm{V}$ with + on top puts the top at $10\,\mathrm{V}$." show=top
#@ step "$i=+2\,\mathrm{A}$ on a downward arrow: the current really flows down, so it falls." show=eX
#@ view "Case 2: $v=+10$, $i=-2$"
#@ node top 10 "top: $10\,\mathrm{V}$"
#@ node bot 0 "bottom: $0\,\mathrm{V}$" ground
#@ el X top bot "climbs: delivers $20\,\mathrm{W}$" col=0 i="$2\,\mathrm{A}$" to=top id=eX plus=top v="$v$"
#@ step "Ground the bottom. $v=+10\,\mathrm{V}$ with + on top puts the top at $10\,\mathrm{V}$." show=top
#@ step "$i=-2\,\mathrm{A}$ on a downward arrow: the current really flows up, so it climbs." show=eX
#@ view "Case 3: $v=-10$, $i=+2$"
#@ node top -10 "top: $-10\,\mathrm{V}$"
#@ node bot 0 "bottom: $0\,\mathrm{V}$" ground
#@ el X top bot "climbs: delivers $20\,\mathrm{W}$" col=0 i="$2\,\mathrm{A}$" to=bot id=eX plus=top v="$v$"
#@ step "Ground the bottom. $v=-10\,\mathrm{V}$ with + on top puts the top at $-10\,\mathrm{V}$." show=top
#@ step "$i=+2\,\mathrm{A}$ on a downward arrow: the current really flows down, so it climbs." show=eX
#@ view "Case 4: $v=-10$, $i=-2$"
#@ node top -10 "top: $-10\,\mathrm{V}$"
#@ node bot 0 "bottom: $0\,\mathrm{V}$" ground
#@ el X top bot "falls: absorbs $20\,\mathrm{W}$" col=0 i="$2\,\mathrm{A}$" to=top id=eX plus=top v="$v$"
#@ step "Ground the bottom. $v=-10\,\mathrm{V}$ with + on top puts the top at $-10\,\mathrm{V}$." show=top
#@ step "$i=-2\,\mathrm{A}$ on a downward arrow: the current really flows up, so it falls." show=eX
```

| case | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| $v$ | $+10\,\mathrm{V}$ | $+10\,\mathrm{V}$ | $-10\,\mathrm{V}$ | $-10\,\mathrm{V}$ |
| $i$ | $+2\,\mathrm{A}$ | $-2\,\mathrm{A}$ | $+2\,\mathrm{A}$ | $-2\,\mathrm{A}$ |

1. Sign of $v$ → which end is high. Sign of $i$ → which way the current really goes (the arrow points down into the top).

   $$\begin{array}{c|c|c|c}\text{case}&\text{high end}&\text{current really goes}&\text{so}\\\hline 1&\text{top}&\text{down: top}\to\text{bottom}&\text{falls: absorbs}\\2&\text{top}&\text{up: bottom}\to\text{top}&\text{climbs: delivers}\\3&\text{bottom}&\text{down: top}\to\text{bottom}&\text{climbs: delivers}\\4&\text{bottom}&\text{up: bottom}\to\text{top}&\text{falls: absorbs}\end{array}$$
2. Size is always current × height $=(2)(10)=20\,\mathrm{W}$. Formula check: the arrow enters $+$, so $p=vi$.

   $$\begin{aligned}p_1&=(10)(2)=20\,\mathrm{W}\\ p_2&=(10)(-2)=-20\,\mathrm{W}\\ p_3&=(-10)(2)=-20\,\mathrm{W}\\ p_4&=(-10)(-2)=20\,\mathrm{W}\end{aligned}$$

**Answer:** Cases 1 and 4 **absorb** $20\,\mathrm{W}$; cases 2 and 3 **deliver** $20\,\mathrm{W}$. Two minus signs cancel: case 4 looks scary but is the same as case 1.

### C · Ideal sources

|  | Voltage source (circle, $+/-$) | Current source (circle, arrow) |
|---|---|---|
| Picture | a **rigid step**: an escalator of fixed height | a **pump** forcing a fixed flow |
| Fixes | the height difference: $+$ end is $v_s$ higher | the current: $i_s$ in the arrow's direction |
| Leaves free | its current (any size, either way) | its height difference (stretches to fit) |
| Delivers when | current climbs through it | current climbs through it |

- **Dependent source (diamond):** the same two kinds, but its number = gain × something measured elsewhere. **Find that something first** (with its sign), then treat it as a normal source.
- **Valid check 1, heights:** every node gets **one** height. Climb each path to a node; all paths must agree. (Two voltage sources side by side must be equal.)
- **Valid check 2, currents:** at every node, current in = current out. (Two current sources in one single path must push the same current.)
- **Floating node:** touched only by current sources → nothing fixes its height. Still valid, but voltages and powers that use that height can't be found.

**Example: C1 · Valid or not? A dependent step (like P2.8)**

$i_x$ is the current of the middle branch. Is the connection valid? Then repeat with the middle source changed to $3\,\mathrm{A}$.

```schematic
V1 0,4 -> 0,0 "$10\,\mathrm{V}$"
I1 3,0 -> 3,4 "$i_x=2\,\mathrm{A}$"
E1 6,4 -> 6,2 "$3i_x$"
V2 6,2 -> 6,0 "$4\,\mathrm{V}$"
wire 0,4 -> 6,4
wire 0,0 -> 6,0
#@ inline
#@ view "With $2\,\mathrm{A}$: valid"
#@ straight off
#@ node t 10 "top wire: $10\,\mathrm{V}$"
#@ node m 4 "right middle: $4\,\mathrm{V}$"
#@ node g 0 "bottom wire: $0\,\mathrm{V}$" ground
#@ el V t g "$10\,\mathrm{V}$" col=0
#@ el I g t "$2\,\mathrm{A}$" col=1 i="$2\,\mathrm{A}$" to=t id=ei
#@ el V m g "$4\,\mathrm{V}$" col=2
#@ el E t m "$3i_x$: steps $6\,\mathrm{V}$" col=2 id=ee
#@ step "Ground the bottom wire. The $10\,\mathrm{V}$ source puts the top wire at $10\,\mathrm{V}$." show=t
#@ step "Control first: $i_x=2\,\mathrm{A}$, so the diamond is a $3(2)=6\,\mathrm{V}$ step." show=ee
#@ step "Climb the right branch: $4\,\mathrm{V}$ then $6\,\mathrm{V}$ reaches $10\,\mathrm{V}$, the same height as the left branch. One height per node: **valid**." show=m,ei
#@ view "With $3\,\mathrm{A}$: invalid"
#@ straight off
#@ node t1 10 "top via the left: $10\,\mathrm{V}$"
#@ node t2 13 "top via the right: $13\,\mathrm{V}$"
#@ node m 4 "right middle: $4\,\mathrm{V}$"
#@ node g 0 "bottom wire: $0\,\mathrm{V}$" ground
#@ el V t1 g "$10\,\mathrm{V}$" col=0
#@ el I g t1 "$3\,\mathrm{A}$" col=1 i="$3\,\mathrm{A}$" to=t1
#@ el V m g "$4\,\mathrm{V}$" col=2
#@ el E t2 m "$3i_x=9\,\mathrm{V}$" col=2
#@ mismatch t1 t2 "one node can't be at two heights"
#@ step "Same ground; the left branch still holds the top wire at $10\,\mathrm{V}$." show=t1
#@ step "Now $3i_x=9\,\mathrm{V}$, so the right branch climbs $4+9=13\,\mathrm{V}$. The top wire would need two heights: **invalid**." show=t2
```

1. Ground the bottom wire. The left source fixes the top wire: $10\,\mathrm{V}$.
2. Find the control, then the diamond's step.

   $$i_x=2\,\mathrm{A}\;\Rightarrow\;3i_x=6\,\mathrm{V}$$
3. Climb the right branch and compare with $10\,\mathrm{V}$.

   $$4+6=10\,\mathrm{V}\ \checkmark\ \text{valid}$$
4. With $3\,\mathrm{A}$ the diamond becomes $9\,\mathrm{V}$, and the right branch reaches a different height.

   $$4+9=13\,\mathrm{V}\neq10\,\mathrm{V}\ \Rightarrow\ \text{invalid}$$

**Answer:** Valid with $2\,\mathrm{A}$; **invalid** with $3\,\mathrm{A}$ (the top wire would be at $10\,\mathrm{V}$ and $13\,\mathrm{V}$ at once).

**Example: C2 · Two current sources in one loop (like P2.6)**

Find $\alpha$ so the connection is valid, then the power of the $6\,\mathrm{V}$ source.

```schematic
I1 0,0 -> 0,3 "$3\,\mathrm{A}$"
G1 0,3 -> 4,3 "$\alpha v_x$"
V1 4,3 -> 4,0 "$6\,\mathrm{V}$" v="$v_x$" flip
wire 4,0 -> 0,0
#@ inline
#@ straight off
#@ node tl 9 "top left: floats" unknown
#@ node tr 6 "top right: $6\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ el I g tl "$3\,\mathrm{A}$" col=0 i="$3\,\mathrm{A}$" to=tl id=e3
#@ el G tl tr "$\alpha v_x$" col=1 i="$3\,\mathrm{A}$" to=tr id=eg
#@ el V tr g "$6\,\mathrm{V}$: absorbs $18\,\mathrm{W}$" col=2 i="$3\,\mathrm{A}$" to=g id=e6 plus=tr v="$v_x$"
#@ step "Ground the bottom wire. The $6\,\mathrm{V}$ source puts the top-right corner at $6\,\mathrm{V}$, so $v_x=+6\,\mathrm{V}$ (its + is on top)." show=tr
#@ step "One loop: the $3\,\mathrm{A}$ source pushes $3\,\mathrm{A}$ clockwise, so the diamond must push the same: $\alpha(6)=3$, $\alpha=0.5\,\mathrm{A/V}$." show=e3,eg
#@ step "The $3\,\mathrm{A}$ falls $6\to0$ through the $6\,\mathrm{V}$ source: it absorbs $18\,\mathrm{W}$." show=e6
#@ step "The top-left corner touches only current sources, so it floats (dashed). Together the two current sources deliver the $18\,\mathrm{W}$; how they split it can't be found." show=tl
```

1. Ground the bottom wire. Read the control: the $6\,\mathrm{V}$ source and $v_x$ both have $+$ on top.

   $$v_x=+6\,\mathrm{V}$$
2. Both current sources are in the one loop, so they must push the same current the same way (both clockwise here).

   $$\alpha v_x=3\;\Rightarrow\;\alpha=\frac{3}{6}=0.5\,\mathrm{A/V}$$
3. The $3\,\mathrm{A}$ goes down through the $6\,\mathrm{V}$ source, from $6$ to $0$: it falls, so the source absorbs.

   $$p=(3)(6)=18\,\mathrm{W}\ \text{absorbed}$$

**Answer:** $\alpha=0.5\,\mathrm{A/V}$; the $6\,\mathrm{V}$ source **absorbs** $18\,\mathrm{W}$. (The top-left node floats, so the current sources' individual powers are unknown.)

**Example: C3 · Currents first, then heights (like P2.9)**

$v$ is the top wire's height ($+$ on top). Find $v$ and every source's power.

```schematic
I1 0,0 -> 0,3 "$6\,\mathrm{A}$"
G1 3,3 -> 3,0 "$0.5v$"
I2 6,3 -> 6,0 "$2\,\mathrm{A}$"
wire 0,3 -> 8,3
wire 0,0 -> 8,0
gap 8,3 -> 8,0 v="$v$"
#@ inline
#@ straight off
#@ node t 8 "top wire: $8\,\mathrm{V}$"
#@ node g 0 "bottom wire: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom wire: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom wire: $0\,\mathrm{V}$" ground
#@ el I g t "$6\,\mathrm{A}$" col=0 i="$6\,\mathrm{A}$" to=t id=e6
#@ el G t g2 "$0.5v=4\,\mathrm{A}$" col=1 i="$4\,\mathrm{A}$" to=g2 id=eg
#@ el I t g3 "$2\,\mathrm{A}$" col=2 i="$2\,\mathrm{A}$" to=g3 id=e2
#@ step "Ground the bottom wire. The top wire's height is $v$, still unknown: no voltage source fixes it."
#@ step "Every branch is a current source, so use KCL at the top wire: $6\,\mathrm{A}$ comes up, $0.5v+2$ goes down. $6=0.5v+2$, so $v=8\,\mathrm{V}$ and the diamond carries $4\,\mathrm{A}$." show=t,e6,eg,e2
#@ step "Current × height: the $6\,\mathrm{A}$ climbs $8\,\mathrm{V}$ ($48\,\mathrm{W}$ delivered); $4\,\mathrm{A}$ and $2\,\mathrm{A}$ fall $8\,\mathrm{V}$ ($32+16=48\,\mathrm{W}$ absorbed)."
```

1. Ground the bottom wire. No voltage source, so the top height $v$ is unknown. Use **KCL first**: in = out at the top wire.

   $$6=0.5v+2\;\Rightarrow\;v=8\,\mathrm{V},\qquad 0.5v=4\,\mathrm{A}$$
2. Now current × height. Up = delivers, down = absorbs.

   $$\begin{aligned}6\,\mathrm{A}&:\ \text{climbs }8\,\mathrm{V},\ \text{delivers }48\,\mathrm{W}\\0.5v&:\ \text{falls }8\,\mathrm{V},\ \text{absorbs }32\,\mathrm{W}\\2\,\mathrm{A}&:\ \text{falls }8\,\mathrm{V},\ \text{absorbs }16\,\mathrm{W}\end{aligned}$$

**Answer:** $v=8\,\mathrm{V}$. The $6\,\mathrm{A}$ source delivers $48\,\mathrm{W}$; the diamond absorbs $32\,\mathrm{W}$ and the $2\,\mathrm{A}$ source $16\,\mathrm{W}$.

### D · Resistors, open and short circuits

| Element | Picture | Rule |
|---|---|---|
| Resistor | a **slide**: current always goes downhill | drop $=iR$, so $i=\text{drop}/R$; always absorbs, $p=i^2R=v^2/R$ |
| Short (closed switch, wire) | **flat** ground: no height change | $v=0$, any current |
| Open (open switch, gap) | a **cliff with no water**: nothing flows | $i=0$, any height difference |

- Ohm's law sign: $v=iR$ when the arrow enters $+$, $v=-iR$ when it enters $-$. Easier: find the high end; the current flows from it.
- Open switch in a loop: no current, so resistors drop nothing, and the switch takes **the whole** source step.

**Example: D1 · A staircase, then open the switch**

Find the current, each resistor's drop and power, with the switch closed. Then open it.

```schematic
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
S1 0,3 -> 3,3 "switch" state=closed
R1 3,3 -> 6,3 "$2\,\Omega$"
R2 6,3 -> 6,0 "$4\,\Omega$" flip
wire 6,0 -> 0,0
ground 0,0
#@ inline
#@ straight off
#@ view "Switch closed"
#@ node t 12 "top: $12\,\mathrm{V}$"
#@ node s 12 "top: $12\,\mathrm{V}$"
#@ node a 8 "middle: $8\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$12\,\mathrm{V}$" col=0 i="$2\,\mathrm{A}$" to=t id=es
#@ el W t s "closed switch: no step" col=0 i="$2\,\mathrm{A}$" to=s id=ew
#@ el R s a "$2\,\Omega$: falls $4\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=a id=e2
#@ el R a g2 "$4\,\Omega$: falls $8\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=g2 id=e4
#@ step "Ground the bottom wire. The source puts its + end at $12\,\mathrm{V}$, and the closed switch has no step." show=s
#@ step "One loop, one current. The two slides together must drop all $12\,\mathrm{V}$: $2i+4i=12$, so $i=2\,\mathrm{A}$." show=es,ew
#@ step "Drops: $(2)(2)=4\,\mathrm{V}$, then $(2)(4)=8\,\mathrm{V}$, landing on 0." show=a,e2,e4
#@ step "Power = drop × current: the resistors absorb $(4)(2)=8\,\mathrm{W}$ and $(8)(2)=16\,\mathrm{W}$; the source lifts $2\,\mathrm{A}$ up $12\,\mathrm{V}$, delivering $24\,\mathrm{W}$."
#@ view "Switch open"
#@ node t 12 "top: $12\,\mathrm{V}$"
#@ node s 0 "after switch: $0\,\mathrm{V}$"
#@ node a 0 "middle: $0\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$12\,\mathrm{V}$" col=0
#@ el S t s "open switch: takes all $12\,\mathrm{V}$" col=1
#@ el R s a "$2\,\Omega$: no fall" col=1
#@ el R a g2 "$4\,\Omega$: no fall" col=2
#@ step "Same ground. Open switch: no current anywhere, so neither resistor drops anything: everything after the switch sits at 0." show=s,a
#@ step "So the whole $12\,\mathrm{V}$ step is across the open switch."
```

1. Ground the bottom. Closed switch = flat. One loop, so one current; the slides must drop the full $12\,\mathrm{V}$.

   $$2i+4i=12\;\Rightarrow\;i=2\,\mathrm{A}$$
2. Each drop is $iR$; each power is drop × current.

   $$\begin{aligned}2\,\Omega&:\ 4\,\mathrm{V},\ 8\,\mathrm{W}\\4\,\Omega&:\ 8\,\mathrm{V},\ 16\,\mathrm{W}\\\text{source}&:\ (12)(2)=24\,\mathrm{W}\text{ delivered}\end{aligned}$$
3. Open the switch: $i=0$, so both drops are 0 and the switch takes all $12\,\mathrm{V}$.

   $$i=0,\qquad v_{\text{switch}}=12\,\mathrm{V}$$

**Answer:** Closed: $i=2\,\mathrm{A}$; drops $4\,\mathrm{V}$ and $8\,\mathrm{V}$; powers $8\,\mathrm{W}$ and $16\,\mathrm{W}$ ($24\,\mathrm{W}$ from the source). Open: $i=0$ and the switch has $12\,\mathrm{V}$ across it.

**Example: D2 · The minus-sign trap**

Find $v$ (marked $+$ on top of the resistor).

```schematic
I1 0,3 -> 0,0 "$3\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$5\,\Omega$" v="$v$" flip
wire 3,0 -> 0,0
#@ inline
#@ straight off
#@ node t -15 "top wire: $-15\,\mathrm{V}$"
#@ node g 0 "bottom wire: $0\,\mathrm{V}$" ground
#@ el I t g "$3\,\mathrm{A}$" col=0 i="$3\,\mathrm{A}$" to=g id=es
#@ el R t g "$5\,\Omega$: falls $15\,\mathrm{V}$" col=1 i="$3\,\mathrm{A}$" to=t id=er plus=t v="$v$"
#@ step "Ground the bottom wire. The source pushes $3\,\mathrm{A}$ down its own side, so the current comes back **up** through the resistor." show=es,er
#@ step "Current runs downhill through a resistor, so the bottom is the high end and the top is $(3)(5)=15\,\mathrm{V}$ lower: $-15\,\mathrm{V}$. The + of $v$ is on that low end, so $v=-15\,\mathrm{V}$." show=t
```

1. The current source pushes $3\,\mathrm{A}$ down the left side, so it comes **up** through the resistor.
2. Current goes downhill through a resistor, so the resistor's **bottom is the high end**, $iR$ above the top.

   $$iR=(3)(5)=15\,\mathrm{V}$$
3. $v$ has its $+$ on the low end, so it is negative.

   $$v=-15\,\mathrm{V}$$

**Answer:** $v=-15\,\mathrm{V}$. The minus only means the $+$ mark was put on the low end.

### E · Kirchhoff's laws + the height method

- **KCL (junctions):** water in = water out at every node. Streams split and join; nothing piles up.
- **KVL (loops):** walk around any loop and you land back at the same height, so **climbs = falls**. Same thing as \"every node has one height\".
- **Series** (one path, no junction): same current. **Parallel** (same two nodes): same height difference.

**The recipe for every circuit:**

1. **Ground** a node (usually the $-$ of the main source).
2. **Steps:** place every height a voltage source fixes.
3. **Currents:** current sources give theirs; a resistor carries drop ÷ $R$; KCL where streams meet.
4. **Walk:** go down each resistor by $iR$ to place the rest. (Stuck with unknowns? Write one equation: KVL around the loop, or KCL at the node.)
5. **Answer and check:** voltages = height differences; climbs = falls.

**Example: E1 · Start from the one height you know (like P2.18 and P2.20)**

$v_b=4\,\mathrm{V}$. Find every current, $v_g$ and the source's power.

```schematic
V1 0,3 -> 0,0 "$v_g$"
R1 0,3 -> 3,3 "$1\,\mathrm{k\Omega}$"
R2 3,3 -> 3,0 "$3\,\mathrm{k\Omega}$" flip
R3 3,3 -> 6,3 "$1\,\mathrm{k\Omega}$"
R4 6,3 -> 6,0 "$2\,\mathrm{k\Omega}$" v="$v_b$" flip
wire 6,0 -> 0,0
label 3,3 "$a$" above
label 6,3 "$b$" above
#@ inline
#@ node top 10 "top: $10\,\mathrm{V}$"
#@ node a 6 "$a$: $6\,\mathrm{V}$"
#@ node b 4 "$b$: $4\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V top g "$v_g$: $10\,\mathrm{V}$" col=0 i="$4\,\mathrm{mA}$" to=top id=eg
#@ el R top a "$1\,\mathrm{k\Omega}$: falls $4\,\mathrm{V}$" col=1 i="$4\,\mathrm{mA}$" to=a id=e1
#@ el R a g2 "$3\,\mathrm{k\Omega}$: falls $6\,\mathrm{V}$" col=1 i="$2\,\mathrm{mA}$" to=g2 id=e3
#@ el R a b "$1\,\mathrm{k\Omega}$: falls $2\,\mathrm{V}$" col=2 i="$2\,\mathrm{mA}$" to=b id=e1b
#@ el R b g3 "$2\,\mathrm{k\Omega}$: falls $4\,\mathrm{V}$" col=2 i="$2\,\mathrm{mA}$" to=g3 id=e2 plus=b v="$v_b$"
#@ step "Ground the bottom wire. $v_b=4\,\mathrm{V}$ is a height you are given: $b$ is at $4\,\mathrm{V}$." show=b
#@ step "The $2\,\mathrm{k\Omega}$ drops those $4\,\mathrm{V}$: $\dfrac{4}{2}=2\,\mathrm{mA}$. The $1\,\mathrm{k\Omega}$ above it carries the same $2\,\mathrm{mA}$ (series) and drops $2\,\mathrm{V}$, so $a$ is at $6\,\mathrm{V}$." show=e2,e1b,a
#@ step "The $3\,\mathrm{k\Omega}$ drops $6\,\mathrm{V}$: $2\,\mathrm{mA}$. KCL at $a$: $2+2=4\,\mathrm{mA}$ must arrive through the first $1\,\mathrm{k\Omega}$." show=e3,e1
#@ step "That $1\,\mathrm{k\Omega}$ drops $(4)(1)=4\,\mathrm{V}$, so the top is at $10\,\mathrm{V}$: $v_g=10\,\mathrm{V}$." show=top,eg
#@ step "Check: the source lifts $4\,\mathrm{mA}$ up $10\,\mathrm{V}$ ($40\,\mathrm{mW}$); the drops absorb $16+12+4+8=40\,\mathrm{mW}$."
```

1. Ground the bottom. Start at the known height and walk with drop = $iR$ (milliamps × kilohms = volts).

   $$i_{2\mathrm{k}}=\frac{4}{2}=2\,\mathrm{mA},\qquad V_a=4+(2)(1)=6\,\mathrm{V}$$
2. Down the $3\,\mathrm{k\Omega}$ from $a$, then KCL at $a$.

   $$i_{3\mathrm{k}}=\frac{6}{3}=2\,\mathrm{mA},\qquad i_{\text{in}}=2+2=4\,\mathrm{mA}$$
3. Walk up the first resistor to the top.

   $$v_g=6+(4)(1)=10\,\mathrm{V}$$
4. Power, and the check.

   $$p=(10)(4)=40\,\mathrm{mW}=16+12+4+8\ \checkmark$$

**Answer:** Currents: $4\,\mathrm{mA}$ in, splitting $2\,\mathrm{mA}$ / $2\,\mathrm{mA}$. $V_a=6\,\mathrm{V}$, $v_g=10\,\mathrm{V}$, the source delivers $40\,\mathrm{mW}$.

**Example: E2 · One loop with a dependent step (like "A step that depends on the current")**

The diamond's step is $2i$ volts, with $+$ at its **bottom**. Find $i$ and the height of $x$.

```schematic
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 4,3 "$6\,\Omega$" i="$i$"
E1 4,0 -> 4,3 "$2i$" flip
wire 4,0 -> 0,0
label 4,3 "$x$" above
#@ inline
#@ straight off
#@ node tl 12 "top left: $12\,\mathrm{V}$"
#@ node x -6 "$x$: $-6\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V tl g "$12\,\mathrm{V}$" col=0 i="$3\,\mathrm{A}$" to=tl id=eV
#@ el R tl x "$6\,\Omega$: falls $18\,\mathrm{V}$" col=1 i="$3\,\mathrm{A}$" to=x id=eR
#@ el E g2 x "$2i$: climbs $6\,\mathrm{V}$" col=2 i="$3\,\mathrm{A}$" to=g2 id=eE
#@ step "Ground the bottom wire. The $12\,\mathrm{V}$ source puts the top-left corner at $12\,\mathrm{V}$." show=tl
#@ step "Walk the loop clockwise: up $12$, down $6i$ through the resistor, then **up** $2i$ through the diamond (its + is at the bottom, so going down through it climbs). Back to 0: $12-6i+2i=0$, so $i=3\,\mathrm{A}$." show=eV
#@ step "The resistor drops $18\,\mathrm{V}$, so $x=12-18=-6\,\mathrm{V}$; the diamond climbs $2i=6\,\mathrm{V}$ back to 0, which checks." show=x,eR,eE
#@ step "Both sources lift the charge: $36+18=54\,\mathrm{W}$ delivered, and the resistor absorbs $(18)(3)=54\,\mathrm{W}$."
```

1. Ground the bottom. One loop → one current $i$. Walk clockwise and add up: climbs $+$, falls $-$. Going down through the diamond climbs $2i$ (its $+$ is at the bottom).

   $$12-6i+2i=0\;\Rightarrow\;i=3\,\mathrm{A}$$
2. Place $x$ by walking down the resistor.

   $$x=12-(3)(6)=-6\,\mathrm{V}$$
3. Check: the diamond climbs from $-6$ back to $0$, which is $2i=6\,\mathrm{V}$.

   $$\text{delivered: }(12)(3)+(6)(3)=54\,\mathrm{W}=\text{absorbed: }(18)(3)$$

**Answer:** $i=3\,\mathrm{A}$, $x=-6\,\mathrm{V}$. Both sources deliver ($36\,\mathrm{W}$ and $18\,\mathrm{W}$); the resistor absorbs $54\,\mathrm{W}$.

### Which part do I need? (practice problem map)

| Practice problem | Use | First move |
|---|---|---|
| P1.15 · Which way does power flow? | B | Ground the bottom wire, so the top wire sits at $v$. Find the box the current climbs through: power flows from it. |
| P2.18 · The river splits | E1 | $v_x$ is a height you're given. Walk with drop $=iR$ and KCL. |
| AP 1.6 · Peak power and total energy | A2 | $p=vi$, then $dp/dt=0$; energy with $\int t^2e^{-at}dt=2/a^3$. |
| P2.6 · Choose the gain | C2 | Current sources in one loop must agree. Read $v_x$ with its sign first. |
| P1.28 · Charging a battery | A | Energy = area under the $p$ graph (trapezoids), or $v\times$ area under $i$. |
| P2.8 · Is it valid? | C1 | Find the control, climb the left branch, compare with the 250 V source. |
| A step that depends on the current | E2 | One loop: climbs − falls $=0$, including the diamond's step. |
| P2.9 · Total power developed | C3 | KCL at the top wire first (find $v_\Delta$), then heights branch by branch. |

> **Warning:** **Five traps.** (1) Convert prefixes and hours to seconds before multiplying. (2) A minus sign on $v$ or $i$ usually just means the label points the other way; it is not an error. (3) A source can absorb: check which way the current crosses it. (4) Never give a voltage source zero current or a current source zero voltage by default. (5) Dependent source: find its control first, with its sign.

### Formula sheet

| Result | Formula | In heights |
|---|---|---|
| Lumped condition | size $<\dfrac{\lambda}{10}$, $\lambda=\dfrac{c}{f}$ | — |
| Current and charge | $i=\dfrac{dq}{dt}$, $q(t)=q(t_0)+\int_{t_0}^{t}i\,d\tau$ | — |
| Voltage and energy | $v=\dfrac{dw}{dq}$, $w=qv$ (constant $v$) | height difference between two points |
| Power | $p=\dfrac{dw}{dt}=vi$ | current × height fallen or climbed |
| Passive sign convention | $p=+vi$ (arrow into $+$), $p=-vi$ (arrow into $-$) | falling absorbs ($p>0$), climbing delivers ($p<0$) |
| Energy from power | $w=\int_{t_1}^{t_2}p\,dt$, $w=P\Delta t$ (constant $P$) | — |
| Power balance | $\sum_k p_k=0$ | total climbs = total falls |
| Ideal sources | $v=v_s$ or $i=i_s$; dependent: $\mu v_x$, $\rho i_x$, $\alpha v_x$, $\beta i_x$ | rigid step, or fixed current |
| Ohm's law and conductance | $v=\pm iR$, $G=\dfrac1R$, $i=Gv$ | current falls $iR$, downhill |
| Resistor power | $p=i^2R=\dfrac{v^2}{R}\ge0$ | always downhill, so always absorbs |
| Open and short | open: $i=0$; short: $v=0$ | open takes the leftover step; short has no step |
| Kirchhoff's laws | $\sum_{\text{node}}i=0$, $\sum_{\text{loop}}v=0$ | currents balance; one height per node |
