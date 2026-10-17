# Week 0: Calculus Refresher for ELEC 221

## Overview

> **Info:** Read this before Week 1 if your calculus is rusty. **You do not need to know any circuits to do it.** It covers only the calculus that ELEC 221 uses in Weeks 1–5. The examples use circuit quantities such as charge, current and power, but only as numbers with units: the table below is all the circuit knowledge you need. Whenever a circuit formula appears, it is given to you; the later weeks explain where it comes from.

### The only circuit words you need

| Word | Symbol and unit | What it means here |
|---|---|---|
| charge | $q$, coulombs ($\mathrm{C}$) | an amount of electricity, like litres of water |
| current | $i$, amperes ($\mathrm{A}=\mathrm{C/s}$) | how fast charge flows past a point, like litres per second. A negative current is charge flowing the other way. |
| energy | $w$, joules ($\mathrm{J}$) | energy, as in physics |
| power | $p$, watts ($\mathrm{W}=\mathrm{J/s}$) | how fast energy is used, joules per second |
| voltage | $v$, volts ($\mathrm{V}=\mathrm{J/C}$) | energy carried per coulomb; for this note just a number in volts |
| resistance | $R$, ohms ($\Omega$) | a property of a component; here it only appears inside formulas you are given |
| element, terminal |  | an element is any component (a battery, a lamp); its terminals are the two ends where it connects |
| load | often $R_L$ | the component that receives the power (a lamp, a speaker) |

Two facts are taken as given (Week 1 explains them): the power going into an element is $p=vi$, its voltage times its current. When $p$ is **positive** the element **absorbs** energy (takes it in); when $p$ is **negative** it **delivers** energy (gives it back, \"energy is extracted\").

| Where | What you do | Calculus needed |
|---|---|---|
| Week 1: current | $i=\dfrac{dq}{dt}$, $q=\int i\,dt$ | derivative and integral of polynomials, exponentials, sines |
| Week 1: power and energy | $p=\dfrac{dw}{dt}$, $w=\int p\,dt$ | same, plus the product rule (since $p=vi$) |
| Week 1: peak current or power | when is it largest? | set the derivative to zero |
| Week 1: graphs | charge or energy from a sketch | area under a graph |
| Weeks 2–4 | solve circuits | none: algebra only |
| Week 5: maximum power transfer | best load $R_L$ | quotient rule, set the derivative to zero |

### Learning outcomes

- Read a derivative as a rate (slope) and an integral as an accumulation (area), with the right units.
- Differentiate and integrate $t^n$, $e^{-at}$, $\sin\omega t$ and $\cos\omega t$, using the product and quotient rules where needed.
- Find the maximum of a current, a power or a load power, including when it sits at an endpoint.
- Integrate currents into charge and powers into energy, including to $t=\infty$ and over graphs made of straight lines.

> **Tip:** Same rhythm as the weekly notes: **idea → rule → worked example → Try it**. Answer each Try it on paper before opening it. The practice problems at the end are textbook problems from Chapter 1 that the Week 1 note does not already use, plus one Week 5 maximum-power problem.

## Topic 1: The derivative is a rate

The derivative $\dfrac{df}{dt}$ answers one question: **how fast is $f$ changing right now?** Graphically it is the slope of the $f$–$t$ graph at that instant. Rising steeply means a large positive derivative, flat means zero, falling means negative.

Circuits are full of rates, which is why derivatives appear on the very first slides of Week 1:

$$i=\frac{dq}{dt}\quad[\mathrm{C/s}=\mathrm{A}],\qquad p=\frac{dw}{dt}\quad[\mathrm{J/s}=\mathrm{W}],\qquad v=\frac{dw}{dq}\quad[\mathrm{J/C}=\mathrm{V}]$$

Here $q$ is charge, $w$ is energy and $t$ is time in seconds. The units follow the fraction: dividing by $dt$ divides the unit by seconds. That is a free check on every answer.

For a straight-line graph the slope is the same everywhere, so the derivative is just rise over run. Many textbook problems give charge or energy as straight-line pieces, and then the current or power is constant on each piece.

**Problem: Try it 1 · Current from a charge graph** (introductory)

The charge that has entered an element changes in straight lines between these points:

| $t$ (s) | 0 | 2 | 4 | 5 |
|---|---|---|---|---|
| $q$ (mC) | 0 | 6 | 6 | 0 |

Find the current $i=\dfrac{dq}{dt}$ in each interval.

<details><summary>Solution</summary>

1. Each piece is a straight line, so the derivative is its slope, rise over run.

   $$0\text{–}2\ \mathrm{s}:\ \frac{6-0}{2}=3\,\mathrm{mA}$$
2. Flat graph: no change, so no current.

   $$2\text{–}4\ \mathrm{s}:\ \frac{6-6}{2}=0$$
3. Falling graph: negative slope. The charge flows back out again, so the current is negative.

   $$4\text{–}5\ \mathrm{s}:\ \frac{0-6}{1}=-6\,\mathrm{mA}$$

**Answer:** $3\,\mathrm{mA}$, then $0$, then $-6\,\mathrm{mA}$ (mC per second is mA).

</details>

## Topic 2: Derivative rules for circuit functions

Weeks 1–5 only ever use four kinds of function of time: powers of $t$, decaying exponentials, sines and cosines. These rules are all you need:

| Function $f(t)$ | Derivative $\dfrac{df}{dt}$ | Where you meet it |
|---|---|---|
| constant $K$ | $0$ | a fixed charge or voltage |
| $t^n$ | $nt^{n-1}$ | polynomial power or energy |
| $e^{-at}$ | $-ae^{-at}$ | decaying currents and charges |
| $\sin\omega t$ | $\omega\cos\omega t$ | AC voltages and currents |
| $\cos\omega t$ | $-\omega\sin\omega t$ | AC voltages and currents |
| $Kf(t)$, $f+g$ | $Kf'(t)$, $f'+g'$ | constants come out; sums split |

The pattern behind the exponential and sine rows is the **chain rule** in its simplest form: when the inside is a constant times $t$ (like $-500t$ or $377t$), differentiate the outside and **multiply by that constant**. That covers every case in Weeks 1–5.

### Exponential facts you will need

| Fact | Why it matters |
|---|---|
| $e^{0}=1$ | the value at $t=0$ |
| $e^{-at}\to0$ as $t\to\infty$ (for $a>0$) | a decaying current eventually dies out |
| $e^{-1}\approx0.368$, $e^{-2}\approx0.135$ | values at one and two time constants |
| $e^{-x}e^{-y}=e^{-(x+y)}$, so $\left(e^{-at}\right)^2=e^{-2at}$ | multiplying $v$ and $i$ to get $p$ |
| $e^{-at}$ is never zero | you may divide it out of an equation |
| $e^{-x}=k\ \Rightarrow\ x=\ln\dfrac1k$ | solving for a time |

**Example: Current from a charge that levels off**

The charge entering a terminal is $q(t)=4\left(1-e^{-500t}\right)\,\mathrm{mC}$ for $t\ge0$. Find $i(t)$ and its initial value.

1. Differentiate term by term. The constant 4 has derivative 0.

   $$i=\frac{d}{dt}\left(4-4e^{-500t}\right)=0-4\cdot\left(-500e^{-500t}\right)$$
2. Simplify. Units: mC per second is mA.

   $$i(t)=2000e^{-500t}\,\mathrm{mA}=2e^{-500t}\,\mathrm{A}$$
3. At $t=0$ the exponential is 1.

   $$i(0)=2\,\mathrm{A}$$
4. Sanity check: the charge rises fast at first and then levels off at $4\,\mathrm{mC}$, so the current starts large and decays to zero.

**Answer:** $i(t)=2e^{-500t}\,\mathrm{A}$, starting at $2\,\mathrm{A}$. (Topic 6 integrates this current back into the charge.)

**Problem: Try it 2 · Power from energy** (introductory)

The energy absorbed by an element is $w(t)=2t^3-3t^2\,\mathrm{mJ}$. Find $p(t)$, and the times when the power is zero.

<details><summary>Solution</summary>

1. Power is the rate of energy. Use the power rule on each term.

   $$p=\frac{dw}{dt}=6t^2-6t\ \mathrm{mW}$$
2. Factor and set it to zero.

   $$6t(t-1)=0\ \Rightarrow\ t=0\ \text{or}\ t=1\,\mathrm{s}$$
3. Between 0 and 1 s the power is negative: the element gives energy back.

   $$p(0.5)=6(0.25)-3=-1.5\,\mathrm{mW}$$

**Answer:** $p(t)=6t^2-6t\,\mathrm{mW}$; zero at $t=0$ and $t=1\,\mathrm{s}$.

</details>

**Problem: Try it 3 · How fast does the wall voltage change?** (introductory)

The voltage at a North American outlet is $v=170\sin(377t)\,\mathrm{V}$. Find $\dfrac{dv}{dt}$ and its largest value.

<details><summary>Solution</summary>

1. Sine rule with the chain-rule constant 377.

   $$\frac{dv}{dt}=170\cdot377\cos(377t)=64\,090\cos(377t)\ \mathrm{V/s}$$
2. Cosine is largest (1) when $t=0$, which is when the sine crosses zero: the voltage changes fastest as it passes through zero.

   $$\left.\frac{dv}{dt}\right|_{\max}=64\,090\,\mathrm{V/s}$$

**Answer:** $\dfrac{dv}{dt}=64\,090\cos(377t)\,\mathrm{V/s}$; maximum $\approx64\,\mathrm{kV/s}$.

</details>

**Problem: Try it 4 · When has the current decayed?** (introductory)

The current from the worked example is $i=2e^{-500t}\,\mathrm{A}$. When has it fallen to $0.5\,\mathrm{A}$?

<details><summary>Solution</summary>

1. Set up the equation and isolate the exponential.

   $$2e^{-500t}=0.5\ \Rightarrow\ e^{-500t}=0.25$$
2. Undo the exponential with the natural log.

   $$500t=\ln\frac{1}{0.25}=\ln4=1.386$$
3. Solve for $t$.

   $$t=\frac{1.386}{500}=2.77\,\mathrm{ms}$$

**Answer:** $t\approx2.77\,\mathrm{ms}$.

</details>

> **Warning:** The number in front of $t$ in an exponent carries units of $1/\mathrm{s}$, so $t$ must be in **seconds**: $e^{-500t}$ at $t=2\,\mathrm{ms}$ is $e^{-1}$, not $e^{-1000}$. Convert ms to s before substituting.

## Topic 3: Product and quotient rules

Power is $p=vi$. When both $v$ and $i$ change with time, or a current is something like $te^{-at}$, you are differentiating a **product**. In Week 5 the load power is a **fraction** with $R_L$ on the top and bottom. These two rules handle both:

$$\frac{d}{dt}(fg)=f'g+fg',\qquad\frac{d}{dx}\left(\frac{f}{g}\right)=\frac{f'g-fg'}{g^2}$$

In words: for a product, differentiate one factor at a time and add. For a quotient, \"bottom times derivative of top, minus top times derivative of bottom, over bottom squared\". The order of the minus matters; the order of the plus does not.

**Example: Product rule on a pulse current**

Find $\dfrac{di}{dt}$ for $i(t)=10te^{-200t}\,\mathrm{A}$.

1. Choose the factors.

   $$f=10t,\quad f'=10;\qquad g=e^{-200t},\quad g'=-200e^{-200t}$$
2. Apply $f'g+fg'$.

   $$\frac{di}{dt}=10e^{-200t}+10t\left(-200e^{-200t}\right)$$
3. Factor out the exponential. Factoring makes the next step (setting it to zero) easy.

   $$\frac{di}{dt}=10e^{-200t}\left(1-200t\right)\ \mathrm{A/s}$$

**Answer:** $\dfrac{di}{dt}=10e^{-200t}(1-200t)\,\mathrm{A/s}$. Topic 4 uses this to find the peak current.

**Example: Quotient rule on a load power**

In Week 5 you will look for the largest value of functions shaped like this one, where $R$ is a resistance in ohms. You don't need to know where it comes from; treat it as any function of $R$:

$$f(R)=\dfrac{R}{(R+4)^2}.$$

Find $\dfrac{df}{dR}$.

1. Top and bottom. The bottom needs the chain rule: the derivative of $(R+4)^2$ is $2(R+4)$, times the inside's derivative, 1.

   $$\text{top}=R,\ \ \text{top}'=1;\qquad\text{bottom}=(R+4)^2,\ \ \text{bottom}'=2(R+4)$$
2. Apply the rule.

   $$\frac{df}{dR}=\frac{1\cdot(R+4)^2-R\cdot2(R+4)}{(R+4)^4}$$
3. Cancel one $(R+4)$ from top and bottom, then simplify the bracket.

   $$\frac{df}{dR}=\frac{(R+4)-2R}{(R+4)^3}=\frac{4-R}{(R+4)^3}$$

**Answer:** $\dfrac{df}{dR}=\dfrac{4-R}{(R+4)^3}$: positive below $4\,\Omega$, zero at $4\,\Omega$, negative above.

**Problem: Try it 5 · Product rule** (introductory)

Differentiate $f(t)=t^2e^{-1000t}$. (This shape appears in Week 1 when $v$ and $i$ both grow like $te^{-500t}$.)

<details><summary>Solution</summary>

1. $f=t^2$, $g=e^{-1000t}$.

   $$\frac{d}{dt}\left(t^2e^{-1000t}\right)=2te^{-1000t}+t^2\left(-1000e^{-1000t}\right)$$
2. Factor.

   $$=te^{-1000t}\left(2-1000t\right)$$

**Answer:** $te^{-1000t}(2-1000t)$, which is zero at $t=0$ and $t=2\,\mathrm{ms}$.

</details>

**Problem: Try it 6 · How sensitive is a divider?** (introductory)

In Week 2 a circuit called a voltage divider has output voltage $v_o=v_s\dfrac{R}{R+10}$, where $v_s$ is a fixed voltage and $R$ is an adjustable resistance in ohms. Take the formula as given. Find $\dfrac{d}{dR}\left(\dfrac{R}{R+10}\right)$. Does turning $R$ change the output more when $R$ is small or when it is large?

<details><summary>Solution</summary>

1. Quotient rule: top $R$, bottom $R+10$, both derivatives 1.

   $$\frac{d}{dR}\frac{R}{R+10}=\frac{1\cdot(R+10)-R\cdot1}{(R+10)^2}=\frac{10}{(R+10)^2}$$
2. The derivative is largest at $R=0$ and shrinks as $R$ grows: the output saturates near $v_s$.

   $$R=0:\ 0.1\,\Omega^{-1};\qquad R=90\,\Omega:\ 0.001\,\Omega^{-1}$$

**Answer:** $\dfrac{10}{(R+10)^2}$: most sensitive when $R$ is small.

</details>

## Topic 4: Finding a maximum

"When is the current largest?" or "What load gives the most power?" At the top of a smooth hill the graph is momentarily flat, so its derivative is zero there. That gives a four-step method:

> **Info:** **Finding a maximum.** (1) Write the quantity as a function of **one** variable. (2) Differentiate and set the derivative to zero; solve. (3) Make sure it is a maximum: the derivative should change from + to −, **and** compare with the values at the ends of the allowed range (the largest value can sit at an end, where the derivative need not be zero). (4) Substitute back to get the maximum value.

**Example: Peak of a pulse current**

Find when $i(t)=10te^{-200t}\,\mathrm{A}$ ($t\ge0$) is largest, and its peak value.

1. From Topic 3, the derivative is already factored. The exponential is never zero, so only the bracket can vanish.

   $$10e^{-200t}(1-200t)=0\ \Rightarrow\ t=\frac{1}{200}=5\,\mathrm{ms}$$
2. Check: before 5 ms the bracket is positive (rising), after it is negative (falling). Also $i(0)=0$ and $i\to0$ as $t\to\infty$, so the ends are smaller. It is the maximum.
3. Substitute back.

   $$i_{\max}=10(0.005)e^{-1}=0.05(0.368)=18.4\,\mathrm{mA}$$

**Answer:** Peak $18.4\,\mathrm{mA}$ at $t=5\,\mathrm{ms}$.

**Example: Week 5 preview: maximum power transfer**

In Week 5 you will show that when a source with fixed values $V_{Th}$ (volts) and $R_{Th}$ (ohms) feeds an adjustable resistance $R_L$, the power $R_L$ receives is

$$p_L=V_{Th}^2\,\dfrac{R_L}{(R_{Th}+R_L)^2}.$$

Take the formula as given. $V_{Th}$ and $R_{Th}$ are constants; $R_L\ge0$ is the variable. Which $R_L$ makes $p_L$ largest, and how large?

1. $V_{Th}^2$ is a constant multiplier, so it just rides along. The rest is the Topic 3 function with 4 replaced by $R_{Th}$.

   $$\frac{dp_L}{dR_L}=V_{Th}^2\,\frac{R_{Th}-R_L}{(R_{Th}+R_L)^3}$$
2. Set it to zero: only the top can vanish.

   $$R_{Th}-R_L=0$$
3. It is positive below $R_{Th}$ and negative above, so this is a maximum. The ends give zero power: $p_L(0)=0$, and as $R_L\to\infty$ the bottom grows faster than the top.

   $$R_L=R_{Th}$$
4. Substitute back.

   $$p_{\max}=V_{Th}^2\,\frac{R_{Th}}{(2R_{Th})^2}=\frac{V_{Th}^2}{4R_{Th}}$$

**Answer:** $R_L=R_{Th}$, giving $p_{\max}=\dfrac{V_{Th}^2}{4R_{Th}}$. This is the \"maximum power transfer\" result you will meet in Week 5.

**Problem: Try it 7 · When the best answer is at the end** (intermediate)

A dimmer knob sets a resistance $R_s$ anywhere from $0$ to $10\,\Omega$. The power reaching a lamp is (take this as given)

$$p_L=\dfrac{3456}{(R_s+6)^2}\ \mathrm{W}.$$

Which setting gives the lamp the most power, and how much?

<details><summary>Solution</summary>

1. Rewrite with a negative power so the chain rule applies directly.

   $$p_L=3456\,(R_s+6)^{-2}$$
2. Differentiate: bring the power down, lower it by one, multiply by the inside's derivative (1).

   $$\frac{dp_L}{dR_s}=3456\cdot(-2)(R_s+6)^{-3}=-\frac{6912}{(R_s+6)^3}$$
3. This is negative for every allowed $R_s$, so it is never zero: the power only falls as $R_s$ grows. The maximum is at the left end of the range.

   $$R_s=0$$
4. Evaluate.

   $$p_L=\frac{3456}{36}=96\,\mathrm{W}$$

**Answer:** $R_s=0$, giving $96\,\mathrm{W}$. Setting the derivative to zero finds nothing here; checking the endpoints does.

</details>

## Topic 5: The integral is an accumulation (area)

Integration runs the derivative backwards. If current is the rate of charge, then adding up current over time gives charge; adding up power gives energy. Graphically, $\int_{t_1}^{t_2}f\,dt$ is the **signed area** between the graph and the $t$ axis: area above the axis counts positive, area below counts negative.

$$q(t_2)-q(t_1)=\int_{t_1}^{t_2}i\,dt\quad[\mathrm{A\cdot s}=\mathrm{C}],\qquad w(t_2)-w(t_1)=\int_{t_1}^{t_2}p\,dt\quad[\mathrm{W\cdot s}=\mathrm{J}]$$

Integrating with $dt$ **multiplies** the unit by seconds: the mirror image of Topic 1. When a graph is made of straight lines you do not need any calculus at all: split it into rectangles, triangles and trapezoids.

| Shape under the graph | Area |
|---|---|
| rectangle (constant value $K$ for time $T$) | $KT$ |
| triangle (from 0 up to height $K$, width $T$) | $\tfrac12KT$ |
| trapezoid (from $K_1$ to $K_2$, width $T$) | $\dfrac{K_1+K_2}{2}\,T$ (average height × width) |

**Problem: Try it 8 · Signed area** (introductory)

A current rises in a straight line from $0$ to $4\,\mathrm{A}$ between $t=0$ and $t=2\,\mathrm{ms}$, then falls in a straight line to $-2\,\mathrm{A}$ at $t=5\,\mathrm{ms}$, where it stops.

1. When does the current cross zero?
2. What net charge has passed?

<details><summary>Solution</summary>

1. The falling line drops $6\,\mathrm{A}$ in $3\,\mathrm{ms}$, i.e. $2\,\mathrm{A}$ per ms. From $4\,\mathrm{A}$ it reaches zero after $2\,\mathrm{ms}$ more.

   $$t=4\,\mathrm{ms}$$
2. Positive part: a triangle from 0 to 4 ms with height 4 A.

   $$\tfrac12(4\,\mathrm{A})(4\,\mathrm{ms})=8\,\mathrm{mC}$$
3. Negative part: a triangle from 4 to 5 ms reaching $-2\,\mathrm{A}$.

   $$\tfrac12(-2\,\mathrm{A})(1\,\mathrm{ms})=-1\,\mathrm{mC}$$
4. Add the signed areas: charge that flowed back cancels part of what flowed forward.

   $$Q=8-1=7\,\mathrm{mC}$$

**Answer:** **(1)** $t=4\,\mathrm{ms}$. **(2)** $7\,\mathrm{mC}$ net (A × ms gives mC).

</details>

## Topic 6: Antiderivatives, constants and integrals to infinity

An **antiderivative** $F$ of $f$ is a function whose derivative is $f$. The fundamental theorem of calculus says that the area is the change in $F$:

$$\int_{t_1}^{t_2}f(t)\,dt=F(t_2)-F(t_1),\qquad F'=f$$

| $f(t)$ | Antiderivative $F(t)$ |
|---|---|
| $K$ | $Kt$ |
| $t^n$ | $\dfrac{t^{n+1}}{n+1}$ |
| $e^{-at}$ | $-\dfrac{1}{a}e^{-at}$ |
| $\cos\omega t$ | $\dfrac{1}{\omega}\sin\omega t$ |
| $\sin\omega t$ | $-\dfrac{1}{\omega}\cos\omega t$ |

Every row is the matching derivative row of Topic 2 read backwards: **divide** by the constant in front of $t$ instead of multiplying. Checking an antiderivative is always possible: differentiate it and you should get back $f$.

### The constant is the initial condition

An indefinite integral carries a $+C$ because adding a constant does not change the derivative. In circuits that constant is physical: it is whatever charge (or energy) was already there at the start. Writing the integral from $0$ to $t$ builds the starting value in:

$$q(t)=q(0)+\int_0^t i(\tau)\,d\tau$$

The integration variable is renamed $\tau$ only so it does not clash with the upper limit $t$.

**Example: Charge from a decaying current**

A current $i=2e^{-500t}\,\mathrm{A}$ starts at $t=0$ with no charge stored. Find $q(t)$ and the total charge.

1. Integrate from 0 to $t$ using the exponential row.

   $$q(t)=\int_0^t2e^{-500\tau}\,d\tau=\left[-\frac{2}{500}e^{-500\tau}\right]_0^t$$
2. Upper limit minus lower limit; $e^0=1$.

   $$q(t)=-\frac{2}{500}e^{-500t}+\frac{2}{500}=0.004\left(1-e^{-500t}\right)\,\mathrm{C}$$
3. As $t\to\infty$ the exponential vanishes.

   $$q(\infty)=0.004\,\mathrm{C}=4\,\mathrm{mC}$$
4. This is exactly the charge we differentiated in Topic 2: integration undid the derivative.

**Answer:** $q(t)=4\left(1-e^{-500t}\right)\,\mathrm{mC}$; total $4\,\mathrm{mC}$.

### Integrals to infinity

\"Total charge\" or \"total energy\" from a decaying waveform means integrating to $t=\infty$. The exponential wins over any power of $t$, so the upper limit contributes zero. Three results cover every Week 1 problem:

$$\int_0^\infty e^{-at}\,dt=\frac1a,\qquad\int_0^\infty te^{-at}\,dt=\frac{1}{a^2},\qquad\int_0^\infty t^2e^{-at}\,dt=\frac{2}{a^3}\qquad(a>0)$$

**Where the middle one comes from (integration by parts)**

1. Integration by parts is the product rule integrated. Pick $u=t$ (it gets simpler when differentiated) and $dv=e^{-at}dt$.

   $$\int u\,dv=uv-\int v\,du,\qquad u=t,\ du=dt,\ \ v=-\frac1ae^{-at}$$
2. Substitute.

   $$\int_0^\infty te^{-at}\,dt=\left[-\frac{t}{a}e^{-at}\right]_0^\infty+\frac1a\int_0^\infty e^{-at}\,dt$$
3. The bracket is 0 at both ends: $t=0$ makes it zero, and at infinity the exponential wins. The last integral is $\dfrac1a$.

   $$=0+\frac1a\cdot\frac1a=\frac{1}{a^2}$$

Doing parts twice gives the $t^2$ result. On an exam, quoting $\int_0^\infty t^ne^{-at}\,dt=\dfrac{n!}{a^{n+1}}$ is usually fine; check with your instructor.

### Average value

The average of a quantity over an interval is its area divided by the width, $\langle p\rangle=\dfrac{1}{T}\int_0^Tp\,dt$. It is the constant power that would deliver the same energy in the same time.

**Problem: Try it 9 · Energy and average power** (introductory)

An element absorbs $p(t)=4t-t^2\,\mathrm{W}$ for $0\le t\le4\,\mathrm{s}$. Find **(a)** the energy absorbed and **(b)** the average power.

<details><summary>Solution</summary>

1. Power rule backwards on each term.

   $$w=\int_0^4\left(4t-t^2\right)dt=\left[2t^2-\frac{t^3}{3}\right]_0^4$$
2. Evaluate.

   $$w=32-\frac{64}{3}=\frac{32}{3}=10.67\,\mathrm{J}$$
3. Average = energy ÷ time.

   $$\langle p\rangle=\frac{10.67}{4}=2.67\,\mathrm{W}$$

**Answer:** **(a)** $10.67\,\mathrm{J}$. **(b)** $2.67\,\mathrm{W}$.

</details>

**Problem: Try it 10 · Totals to infinity** (introductory)

Find the total energy for **(a)** $p=2e^{-1000t}\,\mathrm{W}$ and **(b)** $p=3te^{-100t}\,\mathrm{W}$, both for $t\ge0$.

<details><summary>Solution</summary>

1. First formula with $a=1000$.

   $$w=2\cdot\frac{1}{1000}=0.002\,\mathrm{J}=2\,\mathrm{mJ}$$
2. Second formula with $a=100$.

   $$w=3\cdot\frac{1}{100^2}=3\times10^{-4}\,\mathrm{J}=0.3\,\mathrm{mJ}$$

**Answer:** **(a)** $2\,\mathrm{mJ}$. **(b)** $0.3\,\mathrm{mJ}$.

</details>

**Problem: Try it 11 · Don't forget the constant** (introductory)

A current $i=5\sin(100t)\,\mathrm{A}$ flows into an element that holds no charge at $t=0$. Find $q(t)$ and its largest value.

<details><summary>Solution</summary>

1. Integrate from 0 to $t$ with the sine row.

   $$q(t)=\int_0^t5\sin(100\tau)\,d\tau=\left[-\frac{5}{100}\cos(100\tau)\right]_0^t$$
2. The lower limit gives $+0.05$ because $\cos0=1$. That constant is what makes $q(0)=0$.

   $$q(t)=0.05\left(1-\cos100t\right)\,\mathrm{C}$$
3. Largest when $\cos100t=-1$.

   $$q_{\max}=0.05(2)=0.1\,\mathrm{C}$$

**Answer:** $q(t)=0.05(1-\cos100t)\,\mathrm{C}$, never negative, maximum $0.1\,\mathrm{C}$. Writing just $-0.05\cos100t$ would wrongly start at $-0.05\,\mathrm{C}$.

</details>

## Practice problems

Textbook Chapter 1 problems that the Week 1 note does not use, ordered from easier to harder, plus one Week 5 problem. Each mixes several topics above. Give each a real attempt before opening the solution.

**Problem: Textbook P1.8 · Charge from a decaying current** (intermediate)

There is no charge at the left terminal of an element for $t<0$. At $t=0$ a current $i=25e^{-1000t}\,\mathrm{mA}$ starts entering that terminal.

1. Find the charge $q(t)$ that accumulates for $t>0$.
2. Find the total charge that accumulates.
3. If the current is stopped at $t=1\,\mathrm{ms}$, how much charge has accumulated?

<details><summary>Solution</summary>

1. Integrate from 0 (where $q=0$). mA times seconds gives mC.

   $$q(t)=\int_0^t25e^{-1000\tau}\,d\tau=\frac{25}{1000}\left(1-e^{-1000t}\right)\,\mathrm{mC}=25\left(1-e^{-1000t}\right)\,\mu\mathrm{C}$$
2. Let $t\to\infty$.

   $$q(\infty)=25\,\mu\mathrm{C}$$
3. At $1\,\mathrm{ms}$ the exponent is $-1$.

   $$q(0.001)=25\left(1-e^{-1}\right)=25(0.632)=15.8\,\mu\mathrm{C}$$

**Answer:** **(1)** $q(t)=25\left(1-e^{-1000t}\right)\,\mu\mathrm{C}$. **(2)** $25\,\mu\mathrm{C}$. **(3)** $15.8\,\mu\mathrm{C}$ (63% of the total after one time constant).

</details>

**Problem: Week 5 bridge · Matching a load** (intermediate)

A circuit delivers power to an adjustable resistance $R_L\ge0$ (in ohms). Take as given that the power it receives is

$$p_L=\dfrac{900R_L}{(5+R_L)^2}\ \mathrm{W}.$$

1. Use a derivative to find the $R_L$ that makes $p_L$ largest.
2. Find $p_{\max}$.
3. Find $p_L$ for $R_L=2.5\,\Omega$ and $R_L=10\,\Omega$.

<details><summary>Solution</summary>

1. Quotient rule (Topic 3 with 4 → 5, times the constant 900), set to zero.

   $$\frac{dp_L}{dR_L}=900\,\frac{5-R_L}{(5+R_L)^3}=0\ \Rightarrow\ R_L=5\,\Omega$$
2. Positive below 5 Ω and negative above, and zero power at both ends of the range: a maximum.

   $$p_{\max}=\frac{900(5)}{10^2}=45\,\mathrm{W}$$
3. Evaluate the two other loads.

   $$p_L(2.5)=\frac{900(2.5)}{7.5^2}=40\,\mathrm{W},\qquad p_L(10)=\frac{900(10)}{15^2}=40\,\mathrm{W}$$

**Answer:** **(1)** $p_L=\dfrac{900R_L}{(5+R_L)^2}$, maximized at $R_L=5\,\Omega$. **(2)** $45\,\mathrm{W}$. **(3)** $40\,\mathrm{W}$ each: halving or doubling $R_L$ from its best value costs only about 11%.

</details>

**Problem: Textbook P1.19 · Peak power with a logarithm** (intermediate)

The voltage and current of an element are zero for $t<0$. For $t\ge0$ the power delivered to the element is $p=vi$, with

$$v=100e^{-500t}\ \mathrm{V},\qquad i=20-20e^{-500t}\ \mathrm{mA}.$$

1. Find the maximum power delivered to the element.
2. Find the total energy delivered to the element.

<details><summary>Solution</summary>

1. Multiply, converting mA to A, and combine exponentials: $e^{-500t}e^{-500t}=e^{-1000t}$.

   $$p=vi=100e^{-500t}\left(0.02-0.02e^{-500t}\right)=2e^{-500t}-2e^{-1000t}\ \mathrm{W}$$
2. Differentiate and set to zero.

   $$\frac{dp}{dt}=-1000e^{-500t}+2000e^{-1000t}=0$$
3. Divide by $1000e^{-500t}$ (never zero), then take logs.

   $$-1+2e^{-500t}=0\ \Rightarrow\ e^{-500t}=\tfrac12\ \Rightarrow\ t=\frac{\ln2}{500}=1.386\,\mathrm{ms}$$
4. Substitute: $e^{-500t}=\tfrac12$ and $e^{-1000t}=\tfrac14$. Since $p(0)=0$ and $p\to0$ at infinity, this is the maximum.

   $$p_{\max}=2\left(\tfrac12\right)-2\left(\tfrac14\right)=0.5\,\mathrm{W}$$
5. Total energy: integrate each exponential to infinity.

   $$w=\frac{2}{500}-\frac{2}{1000}=0.004-0.002=2\,\mathrm{mJ}$$

**Answer:** **(1)** $0.5\,\mathrm{W}$, at $t=1.39\,\mathrm{ms}$. **(2)** $2\,\mathrm{mJ}$.

</details>

**Problem: Textbook P1.26 · Charging a car battery from graphs** (advanced)

During a charge cycle an automobile battery has these voltage and current, each made of straight lines ($t$ in kiloseconds). The power delivered to the battery is $p=vi$.

| $t$ (ks) | 0 | 15 | 20 |
|---|---|---|---|
| $v$ (V) | 10 | 13.75 | 15 |
| $i$ (A) | 30 | 20 | 0 |

The voltage rises linearly from $10\,\mathrm{V}$ to $15\,\mathrm{V}$ over the full 20 ks. The current falls linearly from $30$ to $20\,\mathrm{A}$ over 0–15 ks, then to $0$ at 20 ks.

1. Find the total charge transferred to the battery.
2. Find the total energy transferred to the battery.

<details><summary>Solution</summary>

1. Charge = area under $i$: a trapezoid then a triangle. Keep $t$ in ks for now; A × ks gives kC.

   $$Q=\frac{30+20}{2}(15)+\frac12(20)(5)=375+50=425\,\mathrm{kC}$$
2. Energy needs $\int vi\,dt$. Both are lines, so their product is a quadratic and areas no longer work; write the lines as formulas ($T$ in ks).

   $$v=10+\frac{T}{4};\qquad i=30-\frac{2T}{3}\ (0\le T\le15),\quad i=80-4T\ (15\le T\le20)$$
3. First piece: multiply out, then integrate term by term.

   $$\int_0^{15}\left(300+\frac56T-\frac{T^2}{6}\right)dT=4500+93.75-187.5=4406.25$$
4. Second piece, the same way.

   $$\int_{15}^{20}\left(800-20T-T^2\right)dT=4000-1750-1541.67=708.33$$
5. Add, and convert: the unit is V·A·ks = kJ.

   $$W=4406.25+708.33=5114.6\,\mathrm{kJ}\approx5.11\,\mathrm{MJ}$$

**Answer:** **(1)** $425\,\mathrm{kC}$. **(2)** $\approx5.11\,\mathrm{MJ}$.

</details>

**Problem: Textbook P1.25 · Sinusoidal power and its average** (advanced)

An element has $v=36\sin(200\pi t)\,\mathrm{V}$ and $i=25\cos(200\pi t)\,\mathrm{A}$, and the power delivered to it is $p=vi$.

1. Find the maximum power delivered to the element and the maximum power extracted from it.
2. Find the average power over $0\le t\le5\,\mathrm{ms}$.
3. Find the average power over $0\le t\le6.25\,\mathrm{ms}$.

<details><summary>Solution</summary>

1. Multiply, then use the one identity this note needs: $\sin x\cos x=\tfrac12\sin2x$.

   $$p=900\sin(200\pi t)\cos(200\pi t)=450\sin(400\pi t)\ \mathrm{W}$$
2. A sine swings between $+1$ and $-1$.

   $$p_{\max}=+450\,\mathrm{W}\ \text{(delivered)},\qquad p_{\min}=-450\,\mathrm{W}\ \text{(450 W extracted)}$$
3. Integrate with the sine row, then divide by the width. Over 5 ms the angle $400\pi t$ completes one full cycle ($2\pi$), so the cosines cancel.

   $$\begin{aligned}\int_0^{T}450\sin(400\pi t)\,dt&=\frac{450}{400\pi}\left[1-\cos(400\pi T)\right]\\T=5\,\mathrm{ms}:\quad 1-\cos2\pi&=0\end{aligned}$$
4. Over 6.25 ms the angle reaches $2.5\pi$, where the cosine is 0.

   $$w=\frac{450}{400\pi}(1-0)=0.358\,\mathrm{J},\qquad\langle p\rangle=\frac{0.358}{0.00625}=57.3\,\mathrm{W}$$

**Answer:** **(1)** $450\,\mathrm{W}$ delivered and $450\,\mathrm{W}$ extracted. **(2)** $0$: as much energy goes back as comes in. **(3)** $57.3\,\mathrm{W}$.

</details>

**Problem: Textbook P1.21 · A maximum where the derivative isn't zero** (advanced)

The voltage and current of an element are zero for $t<0$. For $t\ge0$ the power delivered to the element is $p=vi$, with

$$v=\left(16\,000t+20\right)e^{-800t}\ \mathrm{V},\qquad i=\left(128t+0.16\right)e^{-800t}\ \mathrm{A}.$$

1. At what instant is the power maximum?
2. Find the maximum power.
3. Find the total energy delivered, in microjoules.

<details><summary>Solution</summary>

1. Spot that $v$ is $125$ times $i$'s bracket ($125\cdot128=16\,000$ and $125\cdot0.16=20$). That makes the power neat.

   $$p=vi=125\left(128t+0.16\right)^2e^{-1600t}\ \mathrm{W}$$
2. Product rule, with the chain rule on the square, then factor.

   $$\begin{aligned}\frac{dp}{dt}&=125\left(128t+0.16\right)e^{-1600t}\left[256-1600\left(128t+0.16\right)\right]\\&=-4.096\times10^{6}\,t\left(800t+1\right)e^{-1600t}\end{aligned}$$
3. For every $t>0$ this is negative: the power only falls. The derivative is zero only at $t=0$, the left end, so the maximum sits there (Topic 4: check the endpoints).

   $$t=0$$
4. Evaluate at $t=0$.

   $$p(0)=(20)(0.16)=3.2\,\mathrm{W}$$
5. Energy: expand the power and use the three infinity integrals with $a=1600$.

   $$\begin{aligned}w&=\int_0^\infty\left(2.048\times10^{6}t^2+5120t+3.2\right)e^{-1600t}\,dt\\&=\frac{2(2.048\times10^{6})}{1600^3}+\frac{5120}{1600^2}+\frac{3.2}{1600}\end{aligned}$$
6. Each term works out to a round number.

   $$w=0.001+0.002+0.002=0.005\,\mathrm{J}=5000\,\mu\mathrm{J}$$

**Answer:** **(1)** $t=0$. **(2)** $3.2\,\mathrm{W}$. **(3)** $5000\,\mu\mathrm{J}$.

</details>

## Summary

- A derivative is a rate (slope); an integral is an accumulation (signed area). $i=\dfrac{dq}{dt}$ and $q=\int i\,dt$ are the same idea run both ways, and so are $p$ and $w$.
- Units check every answer: $\dfrac{d}{dt}$ divides by seconds, $\int dt$ multiplies by seconds. Put $t$ in seconds inside an exponent.
- Only four function types appear: $t^n$, $e^{-at}$, $\sin\omega t$, $\cos\omega t$. Differentiating multiplies by the constant in front of $t$; integrating divides by it.
- Use the product rule for $p=vi$ and pulses like $te^{-at}$, and the quotient rule for Week 5 load power.
- For a maximum: derivative = 0, then confirm, and always compare the endpoints.
- An integral from $0$ to $t$ needs the starting value: $q(t)=q(0)+\int_0^ti\,d\tau$.
- Totals to infinity: $\int_0^\infty t^ne^{-at}\,dt=\dfrac{n!}{a^{n+1}}$. Straight-line graphs need only areas, unless you multiply two of them.

### Formula sheet

| Result | Formula | Use when |
|---|---|---|
| Rates in circuits | $i=\dfrac{dq}{dt}$, $p=\dfrac{dw}{dt}$ | a quantity's rate of change |
| Accumulations | $q=q(0)+\int_0^ti\,d\tau$, $w=\int p\,dt$ | total charge or energy |
| Power rule | $\dfrac{d}{dt}t^n=nt^{n-1}$; $\int t^n\,dt=\dfrac{t^{n+1}}{n+1}$ | polynomials |
| Exponential | $\dfrac{d}{dt}e^{-at}=-ae^{-at}$; $\int e^{-at}\,dt=-\dfrac1ae^{-at}$ | decaying waveforms |
| Sinusoids | $\dfrac{d}{dt}\sin\omega t=\omega\cos\omega t$, $\dfrac{d}{dt}\cos\omega t=-\omega\sin\omega t$ | AC waveforms; integrate by dividing by $\omega$ |
| Product rule | $(fg)'=f'g+fg'$ | $p=vi$, $te^{-at}$ |
| Quotient rule | $\left(\dfrac fg\right)'=\dfrac{f'g-fg'}{g^2}$ | load power vs $R_L$ |
| Maximum | $f'=0$, then check the sign change and the endpoints | peak current, power, best load |
| Integrals to infinity | $\int_0^\infty t^ne^{-at}\,dt=\dfrac{n!}{a^{n+1}}$ | total energy or charge |
| Average | $\langle p\rangle=\dfrac1T\int_0^Tp\,dt$ | average power |
| Logs | $e^{-x}=k\Rightarrow x=\ln\dfrac1k$ | solving for a time |
