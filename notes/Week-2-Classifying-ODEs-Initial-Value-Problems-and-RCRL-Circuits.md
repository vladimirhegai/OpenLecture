# Week 2: Classifying ODEs, Initial Value Problems and RC/RL Circuits

## Calculus refresher: the derivatives used this week

This week you mostly differentiate and substitute. You will be given the solution families you need; learning a general method for finding them comes in Week 3.

| Reminder | What to remember |
|---|---|
| $y'=\dfrac{dy}{dt}$; $y''=\dfrac{d^2y}{dt^2}$ | First derivative = rate of change; second derivative = rate of change of that rate. |
| $\dfrac{d}{dt}(K)=0$ | $K$ is a constant, even when you do not know its value. |
| $\dfrac{d}{dt}(Ae^{kt})=Ak e^{kt}$ | Chain rule: multiply by the derivative of the exponent. $A$ and $k$ are constants. |
| $e^0=1$; $e^{-kt}\to0$ for $k>0$ | Use the first at $t=0$, and the second when finding the long-term value. |

For instance, if $y=3-2e^{-4t}$, the constant $3$ differentiates to zero. The exponential contributes a factor of $-4$, so the two negative signs cancel:

$$\dfrac{dy}{dt}=(-2)(-4)e^{-4t}=8e^{-4t}$$

**Problem: Try it 1 · Quick calculus check · original** (introductory)

1. Differentiate $y=5+3e^{-2t}$.
2. For $v(t)=8-6e^{-100t}$, find $v(0)$ and the value approached as $t\to\infty$.

<details><summary>Solution</summary>

1. Multiply by the derivative of the exponent.

   $$y'=-6e^{-2t}$$
2. At zero, use $e^0=1$. At large positive time, the exponential tends to zero.

   $$v(0)=8-6=2,\qquad v(t)\to8$$

**Answer:** 1. $y'=-6e^{-2t}$. 2. $v(0)=2$ and $v\to8$.

</details>

## Week 2 overview

There are three separate jobs this week: describe the kind of differential equation you have, understand what its solution means, and connect a simple circuit to that equation. Learn them in that order; the circuit section will reuse the same ideas about functions and starting values.

## Topic 1: Classifying a differential equation

A differential equation relates an unknown function to its derivatives. In $\dfrac{dy}{dt}+2y=6$, we want a function $y(t)$ whose rate of change plus twice its value always equals $6$.

An **ordinary differential equation (ODE)** uses derivatives with respect to one independent variable. Here $t$ is the independent variable, and $y$ is the dependent variable: its value depends on $t$.

### Five labels, five different questions

Read $y'$ as $\dfrac{dy}{dt}$ below. For the linear-equation labels, first move all terms containing $y$ or its derivatives to the left.

| Label | Question to ask | Useful distinction |
|---|---|---|
| Order | What is the highest derivative present? | $y''$ means second order; $(y')^3$ is still first order. |
| Linear | Are $y$ and its derivatives only to the first power, without multiplying each other or appearing inside functions? | $t^2y'+y$ is linear. $yy'$, $y^2$, and $\sin y$ are nonlinear. |
| Homogeneous (linear) | After collecting the unknown-function terms on the left, is the right side identically zero? | $y'-3y=0$ is homogeneous; $y'-3y=2$ is nonhomogeneous. |
| Constant coefficients (linear) | Are the multipliers of $y$ and its derivatives constants? | $y'+2y=\sin t$ has constant coefficients: the forcing on the right does not count as a coefficient. |
| Autonomous | Does the equation avoid explicit dependence on $t$? | $y'=3y+2$ is autonomous; $y'=ty$ is not. Writing $y(t)$ does not itself count as explicit $t$. |

For a linear equation, a **coefficient** multiplies $y$ or one of its derivatives. The leftover right side is called the **forcing**, often written $f(t)$; it can be zero, constant, or time-varying.

Use “homogeneous” here in the linear-ODE sense. For a nonlinear equation, mark homogeneous and constant coefficients as “not applicable” in these exercises.

**Example: Example 1 · Classify one equation · lecture Example 2.1**

Classify $t^3y''+e^ty'+y=0$ using all five labels.

1. The highest derivative is $y''$: second order.
2. Each occurrence of $y$, $y'$, and $y''$ is linear. The multipliers $t^3$ and $e^t$ depend only on $t$, which is allowed.
3. The right side is zero, so it is homogeneous.
4. The coefficients change with $t$, so they are variable coefficients.
5. The explicit $t^3$ and $e^t$ make it non-autonomous.

**Answer:** Second order; linear; homogeneous; variable coefficients; not autonomous.

**Problem: Try it 2 · Order and linearity · original** (introductory)

For now, identify **only order and linearity**. Do not solve.

1. $y''+4y=0$
2. $(y')^3+y=0$
3. $y'+y^2=t$

<details><summary>Solution</summary>

1. 1. The second derivative is highest, and the unknown appears linearly: second order, linear.
2. 2. Cubing $y'$ does not turn it into a third derivative: first order, nonlinear.
3. 3. Only a first derivative appears, but $y^2$ breaks linearity: first order, nonlinear.

**Answer:** 1. Second order, linear. 2. First order, nonlinear. 3. First order, nonlinear.

</details>

**Problem: Try it 3 · Separate the three remaining labels · original** (introductory)

All three equations below are first order and linear. Identify **homogeneous/nonhomogeneous**, **constant/variable coefficients**, and **autonomous/not autonomous**.

1. $y'=3y$
2. $y'=3y+2$
3. $y'+2y=\sin t$

<details><summary>Solution</summary>

1. Move the unknown-function terms left in 1 and 2.

   $$y'-3y=0,\qquad y'-3y=2$$
2. 1. Zero forcing; coefficients $1,-3$; no explicit time: homogeneous, constant coefficients, autonomous.
3. 2. Forcing $2$ is nonzero but does not depend on time: nonhomogeneous, constant coefficients, autonomous.
4. 3. The forcing $\sin t$ changes with time, but coefficients $1,2$ are constant: nonhomogeneous, constant coefficients, not autonomous.

**Answer:** 1. Homogeneous, constant, autonomous. 2. Nonhomogeneous, constant, autonomous. 3. Nonhomogeneous, constant, not autonomous.

</details>

**Problem: Try it 4 · Put the labels together · original** (introductory)

Classify fully; use “not applicable” where needed.

1. $y''+ty'+y=0$
2. $y'=\sin y$

<details><summary>Solution</summary>

1. 1. Highest derivative $y''$; unknown appears linearly; zero forcing; coefficient $t$ varies and introduces explicit time.
2. 2. The unknown is inside sine, so it is nonlinear. There is no explicit time.

**Answer:** 1. Second order, linear, homogeneous, variable coefficients, not autonomous. 2. First order, nonlinear, autonomous; the other two labels do not apply.

</details>

One consequence of linearity: if $y$ solves a linear equation with forcing $f(t)$, then $Ay$ solves the equation with forcing $Af(t)$, for constant $A$. For a homogeneous equation the forcing stays zero, so scaling a solution gives another solution of the same equation.

## Topic 2: What a solution is, and what an initial condition does

### First: check a function you are given

In algebra, solving $x+2=5$ gives a number. Solving $y'+2y=6$ gives a function: a rule assigning a value to $y$ at each time.

A proposed function is a solution when it makes the differential equation true throughout the interval being considered. Matching at just one time is not enough.

**Example: Example 2 · Check a proposed solution · original**

Does $y=3-2e^{-2t}$ solve $y'+2y=6$?

1. Differentiate the proposed function using the chain rule.

   $$y'=4e^{-2t}$$
2. Replace both $y'$ and $y$ on the left with their expressions.

   $$y'+2y=4e^{-2t}+2(3-2e^{-2t})$$
3. Expand and cancel. The result equals the required right side for every time.

   $$4e^{-2t}+6-4e^{-2t}=6$$

**Answer:** Yes. Its rate of change and its value combine to give $6$ for every $t$.

**Problem: Try it 5 · Your turn: check, without solving · original** (introductory)

Which of these solve $y'+2y=6$?

1. $y=3+e^{-2t}$
2. $y=3+t$

Differentiate each, substitute, and simplify. Candidate 2 matches the equation at one time; explain why that is insufficient.

<details><summary>Solution</summary>

1. For 1, the derivative is $-2e^{-2t}$.

   $$-2e^{-2t}+2(3+e^{-2t})=6$$
2. For 2, the derivative is $1$.

   $$1+2(3+t)=7+2t$$
3. This equals $6$ only at $t=-1/2$. A solution must satisfy the equation on an interval.

**Answer:** 1 is a solution; 2 is not.

</details>

### Then: a family of solutions

The same equation can have many solutions. For $y'+2y=6$, they can be written together as:

$$y=3+Ke^{-2t}$$

The free constant $K$ labels the different functions. Choosing $K=-2$ gives the worked example; choosing $K=1$ gives the first practice candidate; choosing $K=0$ gives the constant solution $y=3$.

This is the **general solution** on the real time line. You can check the whole family at once: $y'=-2Ke^{-2t}$, which cancels the exponential term in $2y$, leaving $6$.

### Finally: choose the member that starts in the right place

An **initial condition** specifies one starting value. The statement $y(0)=1$ means “when $t=0$, the function must equal $1$”; it says nothing about the derivative being $1$.

An **initial value problem (IVP)** gives the differential equation and the initial condition together. The differential equation describes the allowed behaviour, and the starting value selects the appropriate solution here.

**Example: Example 3 · Use a starting value · original**

Solve the IVP $y'+2y=6$, $y(0)=1$, using the given family $y=3+Ke^{-2t}$.

1. Put $t=0$ into the family; the exponential becomes $1$.

   $$y(0)=3+K$$
2. Set this equal to the required starting value and solve for the constant.

   $$3+K=1\quad\Rightarrow\quad K=-2$$
3. Put that constant back into the family.

   $$y(t)=3-2e^{-2t}$$

**Answer:** $y(t)=3-2e^{-2t}$. At $t=0$, this gives $1$, as required.

```graph
title "A starting point chooses one member of the family"
x 0 3 label="$t$"
y -1 7 label="$y$"
family K -4 4 1 "3+K*exp(-2*t)" color=0
hline "3" label="$y=3$"
drag P 0 1 label="starting point" snap=0.25
solution "-2*y+6" x0="P_x" y0="P_y" label="selected solution"
readout "$K=$" "(P_y-3)*exp(2*P_x)"
caption "Start at (0,1): K=-2. Move the point vertically to select a different curve; move it along that curve and K stays the same."
```

**Problem: Try it 6 · The starting time is not always zero · original** (introductory)

Use $y=3+Ke^{-2t}$ with $y(1)=5$. Find $K$ and write the selected solution. Start by substituting $t=1$ and $y=5$.

<details><summary>Solution</summary>

1. At $t=1$, the exponential is $e^{-2}$, not $1$.

   $$5=3+Ke^{-2}$$
2. Subtract $3$, then divide by $e^{-2}$.

   $$K=2e^2$$
3. Substitute and combine exponentials if desired.

   $$y=3+2e^2e^{-2t}=3+2e^{-2(t-1)}$$

**Answer:** $K=2e^2$, $y=3+2e^{-2(t-1)}$. At $t=1$ this gives $5$.

</details>

**Problem: Try it 7 · A solution of the equation can fail the IVP · original** (introductory)

For $y'+2y=6$ with $y(0)=1$, a student proposes $y=3+e^{-2t}$.

It already passed the differential-equation check. Does it solve this IVP? What must you check separately?

<details><summary>Solution</summary>

1. Check the initial condition separately.

   $$y(0)=3+1=4\ne1$$

**Answer:** No. It solves the differential equation but has the wrong starting value.

</details>

A second-order IVP typically specifies both a value $y(t_0)$ and a slope $y'(t_0)$. We will work with those in Week 5; this week, keep the distinction between the equation and the starting value clear.

## Topic 3: First-order RC and RL circuits

A capacitor stores energy through its voltage; an inductor stores energy through its current. Their component laws contain a first derivative, which is where the differential equation enters.

| Component | Law with current entering the + terminal | At DC steady state |
|---|---|---|
| Capacitor | $i_C=C\dfrac{dv_C}{dt}$ | Constant voltage means $i_C=0$: an open circuit. |
| Inductor | $v_L=L\dfrac{di_L}{dt}$ | Constant current means $v_L=0$: a short circuit. |

$C$ is capacitance in farads (F), and $L$ is inductance in henries (H). **Steady state** means the values have stopped changing; a zero derivative means constant, not necessarily zero.

### Start with a capacitor discharging through one resistor

The diagram shows the circuit **after** switching, with a capacitor already holding $8\,\mathrm{V}$. There is no source attached; the stored energy is released through the resistor. This is a **natural response**.

```schematic
C1 0,3 -> 0,0 "$5\,\mu\mathrm{F}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$2\,\mathrm{k\Omega}$" i="$i_R$"
wire 3,0 -> 0,0
ground 0,0
#~ flow
#~ init C1 8
#@ view "Just after switching"
#@ node a 8 "top: $8\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el C a g "$5\,\mu\mathrm{F}$" col=0 plus=a v="$v$" i="$4\,\mathrm{mA}$" to=a
#@ el R a g "$2\,\mathrm{k\Omega}$" col=1 i="$4\,\mathrm{mA}$" to=g
#@ note "Ground the bottom wire. The capacitor holds 8 V; resistor current is 8/2000 = 4 mA downward. Capacitor current is upward."
#@ view "One time constant"
#@ node a 2.9430355 "top: $2.94\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el C a g "$5\,\mu\mathrm{F}$" col=0 plus=a v="$v$" i="$1.47\,\mathrm{mA}$" to=a
#@ el R a g "$2\,\mathrm{k\Omega}$" col=1 i="$1.47\,\mathrm{mA}$" to=g
#@ note "Ground the bottom wire. At 10 ms the voltage is 8/e V, and both current magnitudes are v/R."
#@ view "Long after switching"
#@ node a 0 "top: $0\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el C a g "$5\,\mu\mathrm{F}$" col=0 plus=a v="$v$"
#@ el R a g "$2\,\mathrm{k\Omega}$" col=1
#@ note "Ground the bottom wire. With no source, the voltage and both currents tend to zero."
```

Both current arrows point down, so Kirchhoff’s current law (KCL) at the top node gives $i_C+i_R=0$. A negative value for one reference current simply means its actual direction is upward.

```steps
title "From the circuit to its equation"
$$ i_C+i_R=0 $$
No source injects current into the top node.
$$ C\dfrac{dv}{dt}+\dfrac{v}{R}=0 $$
Replace capacitor current with its law and resistor current with Ohm’s law.
$$ \dfrac{dv}{dt}+\dfrac{v}{RC}=0 $$
Divide both terms by C.
$$ v(t)=Ke^{-t/(RC)} $$
This solution family has the required exponential decay; check it by differentiating and substituting.
$$ v(0)=K=V_0 $$
The initial voltage V₀ fixes K, exactly as in Topic 2.
$$ v(t)=V_0e^{-t/\tau},\quad\tau=RC $$
The time constant τ is the decay time scale, measured in seconds.
```

**Example: Example 4 · Use the equation for the circuit above · original values**

Find $v(t)$ for the $2\,\mathrm{k\Omega}$, $5\,\mu\mathrm{F}$ circuit with $v(0)=8\,\mathrm{V}$.

1. Convert to ohms and farads before multiplying.

   $$\tau=2000(5\times10^{-6})=0.010\,\mathrm{s}$$
2. Use $V_0=8$ and $1/\tau=100$.

   $$v(t)=8e^{-100t}\,\mathrm{V},\qquad t\ge0$$
3. Check the starting and final values.

   $$v(0)=8\,\mathrm{V},\qquad v(t)\to0$$

**Answer:** $v(t)=8e^{-100t}\,\mathrm{V}$, with $t$ in seconds. At $t=\tau=10\,\mathrm{ms}$, $v=8/e\approx2.94\,\mathrm{V}$: about 37% remains.

**Problem: Try it 8 · Read the circuit equation · original** (introductory)

For that same discharge, answer without solving again:

1. Classify $v'+100v=0$ using all five labels.
2. Is $i_C=Cv'$ positive or negative during discharge? Explain using the downward reference arrow.

<details><summary>Solution</summary>

1. 1. It is first order, linear, homogeneous, constant-coefficient, and autonomous.
2. 2. Voltage decreases, so its derivative is negative.

   $$i_C=(5\times10^{-6})(-800e^{-100t})=-4e^{-100t}\,\mathrm{mA}$$

**Answer:** 1. First order, linear, homogeneous, constant coefficients, autonomous. 2. Negative: actual capacitor current flows upward.

</details>

### Add a source: the final voltage can be nonzero

Now a constant source remains connected after switching. The capacitor moves from its initial voltage $V_0$ toward a final voltage $V_f$, rather than necessarily toward zero.

```schematic
I1 0,0 -> 0,3 "$3\,\mathrm{mA}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$2\,\mathrm{k\Omega}$" i="$i_R$"
S1 3,3 -> 6,3 "$t=0$" action=close
C1 6,3 -> 6,0 "$1\,\mu\mathrm{F}$" v="$v$" i="$i_C$"
wire 6,0 -> 0,0
ground 0,0
#~ flow
#~ init C1 2
#@ view "Before switching"
#@ node a 6 "source top: $6\,\mathrm{V}$"
#@ node b 2 "capacitor: $2\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el I g a "$3\,\mathrm{mA}$" col=0 i="$3\,\mathrm{mA}$" to=a rail
#@ el R a g "$2\,\mathrm{k\Omega}$" col=1 i="$3\,\mathrm{mA}$" to=g
#@ el S a b "open" col=2
#@ el C b g "$1\,\mu\mathrm{F}$" col=3 plus=b v="$v$"
#@ note "Ground the bottom wire. The source drives only the resistor: 3 mA times 2 kΩ = 6 V. The isolated capacitor holds the given 2 V."
#@ view "Just after switching"
#@ node a 2 "top: $2\,\mathrm{V}$"
#@ node b 2 "capacitor: $2\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el I g a "$3\,\mathrm{mA}$" col=0 i="$3\,\mathrm{mA}$" to=a rail
#@ el R a g "$2\,\mathrm{k\Omega}$" col=1 i="$1\,\mathrm{mA}$" to=g
#@ el W a b "closed" col=2
#@ el C b g "$1\,\mu\mathrm{F}$" col=3 plus=b v="$v$" i="$2\,\mathrm{mA}$" to=g
#@ note "Ground the bottom wire. Capacitor voltage stays 2 V. The resistor takes 1 mA, leaving 2 mA into C."
#@ view "One time constant"
#@ node a 4.528482 "top: $4.53\,\mathrm{V}$"
#@ node b 4.528482 "capacitor: $4.53\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el I g a "$3\,\mathrm{mA}$" col=0 i="$3\,\mathrm{mA}$" to=a rail
#@ el R a g "$2\,\mathrm{k\Omega}$" col=1 i="$2.26\,\mathrm{mA}$" to=g
#@ el W a b "closed" col=2
#@ el C b g "$1\,\mu\mathrm{F}$" col=3 plus=b v="$v$" i="$0.736\,\mathrm{mA}$" to=g
#@ note "Ground the bottom wire. At 2 ms, v = 6 - 4/e V. KCL: resistor and capacitor currents add to 3 mA."
#@ view "Long after switching"
#@ node a 6 "top: $6\,\mathrm{V}$"
#@ node b 6 "capacitor: $6\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el I g a "$3\,\mathrm{mA}$" col=0 i="$3\,\mathrm{mA}$" to=a rail
#@ el R a g "$2\,\mathrm{k\Omega}$" col=1 i="$3\,\mathrm{mA}$" to=g
#@ el W a b "closed" col=2
#@ el C b g "$1\,\mu\mathrm{F}$" col=3 plus=b v="$v$"
#@ note "Ground the bottom wire. Capacitor current tends to zero, so all 3 mA flows in R and sets v = 6 V."
```

The capacitor initially holds $2\,\mathrm{V}$. In these ordinary switching circuits, capacitor voltage cannot jump, so it still holds $2\,\mathrm{V}$ just after the switch closes.

Write $0^-$ for just before switching and $0^+$ for just after. Thus $v_C(0^+)=v_C(0^-)=V_0$; for an inductor the corresponding continuous quantity is its current, $i_L(0^+)=i_L(0^-)$.

- **Initial value:** use the stored voltage before switching, or find it from the pre-switch steady-state circuit.
- **Final value:** analyse the post-switch DC steady state: capacitor open, so all source current $I_s$ flows through $R$ and $V_f=RI_s$.
- **Time constant:** for this one-resistor RC circuit, $\tau=RC$.

KCL now says “source current = capacitor current + resistor current”:

$$C\dfrac{dv}{dt}+\dfrac{v}{R}=I_s$$

The solution has the same decaying exponential as before, with the final voltage added:

$$v(t)=V_f+(V_0-V_f)e^{-t/\tau}$$

The quantity $v-V_f$ is the remaining difference from the final voltage. Call it $u=v-V_f$; because $V_f$ is constant, $u'=v'$. Substituting $v=V_f+u$ into KCL cancels $V_f/R=I_s$, leaving $Cu'+u/R=0$: the natural-response equation again.

At $t=0$, the formula gives $V_f+(V_0-V_f)=V_0$. As time passes, the exponential dies away and leaves $V_f$; at one time constant, 37% of the initial difference remains, so 63% of the change is complete.

**Example: Example 5 · Build the response from three quantities · original values**

For the source-driven circuit above, $I_s=3\,\mathrm{mA}$, $R=2\,\mathrm{k\Omega}$, $C=1\,\mu\mathrm{F}$ and $V_0=2\,\mathrm{V}$. Find $v(t)$.

1. The initial capacitor voltage is given.

   $$V_0=2\,\mathrm{V}$$
2. At steady state, the source current flows entirely through the resistor.

   $$V_f=(2000)(0.003)=6\,\mathrm{V}$$
3. Convert to SI units and multiply.

   $$\tau=(2000)(10^{-6})=0.002\,\mathrm{s}$$
4. Substitute all three quantities into the response.

   $$v(t)=6+(2-6)e^{-t/0.002}=6-4e^{-500t}\,\mathrm{V}$$

**Answer:** $v(t)=6-4e^{-500t}\,\mathrm{V}$, $t\ge0$, with $t$ in seconds. It starts at $2\,\mathrm{V}$ and approaches $6\,\mathrm{V}$.

```graph
title "Initial value, final value, and speed are separate choices"
x 0 12 label="$t$ (ms)"
y -1 13 label="$v$ (V)"
slider V0 0 12 2 step=1 label="$V_0$ (V)"
slider Vf 0 12 6 step=1 label="$V_f$ (V)"
slider tau 0.5 3 2 step=0.5 label="$\tau$ (ms)"
curve "Vf+(V0-Vf)*exp(-t/tau)" label="$v(t)$"
hline "Vf" label="final voltage"
vline "tau" label="one time constant"
caption "Move one slider at a time. V₀ sets the starting height, V_f sets the destination, and τ sets the speed. Set V_f=0 to recover discharge."
```

**Problem: Try it 9 · Can current jump? · Pre-tutorial 2** (introductory)

The capacitor is initially uncharged: $V_0=0$. The capacitance is unspecified and is not needed.

```schematic
I1 0,0 -> 0,3 "$2\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$1\,\mathrm{k\Omega}$" i="$i_R$"
S1 3,3 -> 6,3 "$t=0$" action=close
C1 6,3 -> 6,0 "$C$" v="$v$" i="$i_C$"
wire 6,0 -> 0,0
ground 0,0
#@ spoiler
#@ view "Before switching"
#@ node a 2000 "source top: $2000\,\mathrm{V}$"
#@ node b 0 "capacitor: $0\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el I g a "$2\,\mathrm{A}$" col=0 i="$2\,\mathrm{A}$" to=a rail
#@ el R a g "$1\,\mathrm{k\Omega}$" col=1 i="$2\,\mathrm{A}$" to=g
#@ el S a b "open" col=2
#@ el C b g "$C$" col=3 plus=b v="$v$"
#@ note "Ground the bottom wire. All 2 A flows in R, so its top is 2000 V; the disconnected capacitor holds the given 0 V."
#@ view "Just after switching"
#@ node a 0 "top: $0\,\mathrm{V}$"
#@ node b 0 "capacitor: $0\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el I g a "$2\,\mathrm{A}$" col=0 i="$2\,\mathrm{A}$" to=a rail
#@ el R a g "$1\,\mathrm{k\Omega}$" col=1
#@ el W a b "closed" col=2 i="$2\,\mathrm{A}$" to=b
#@ el C b g "$C$" col=3 plus=b v="$v$" i="$2\,\mathrm{A}$" to=g
#@ note "Ground the bottom wire. Capacitor voltage stays zero. R carries zero current, so all 2 A enters C."
```

Find capacitor current $i_C(0^-)$ and $i_C(0^+)$, using the downward reference into the capacitor. Is current discontinuous even though voltage is continuous?

<details><summary>Solution</summary>

1. Before switching the capacitor branch is disconnected, so its current is zero.

   $$i_C(0^-)=0$$
2. Immediately after switching, its voltage is still zero.

   $$v(0^+)=0$$
3. The resistor therefore carries no current at that instant.

   $$i_R(0^+)=\dfrac{0}{1000}=0$$
4. KCL sends all the source current into the capacitor.

   $$i_C(0^+)=I_s-i_R(0^+)=2\,\mathrm{A}$$

**Answer:** $i_C(0^-)=0$, $i_C(0^+)=2\,\mathrm{A}$. Yes, capacitor current jumps; capacitor voltage stays at $0\,\mathrm{V}$ through the switch.

</details>

### The RL version: track current instead of voltage

For a series resistor–inductor circuit, Kirchhoff’s voltage law (KVL) gives $V_s=Ri+L\dfrac{di}{dt}$, where $V_s$ is a constant source voltage. The starting current carries over through switching; at DC steady state the inductor is a short, so $I_f=V_s/R$.

$$i(t)=I_f+(I_0-I_f)e^{-t/\tau},\qquad\tau=\dfrac{L}{R}$$

$I_0$ is the initial inductor current and $I_f$ is its final current. The response has the same shape as the RC result; the changing quantity and time constant differ.

**Problem: Try it 10 · Build an RL response with less help · original** (introductory)

The inductor initially carries no current. The switch closes at $t=0$.

```schematic
V1 0,3 -> 0,0 "$24\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$6\,\Omega$" i="$i$"
L1 6,3 -> 6,0 "$0.3\,\mathrm{H}$" v="$v_L$"
wire 6,0 -> 0,0
ground 0,0
#~ flow
#~ init L1 0
#@ spoiler
#@ view "Before switching"
#@ node a 24 "source: $24\,\mathrm{V}$"
#@ node b 0 "after switch: $0\,\mathrm{V}$"
#@ node c 0 "inductor: $0\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$24\,\mathrm{V}$" col=0
#@ el S a b "open" col=1
#@ el R b c "$6\,\Omega$" col=2
#@ el L c g "$0.3\,\mathrm{H}$" col=3 plus=c v="$v_L$"
#@ note "Ground the bottom wire. The source steps 24 V, all taken by the open switch. No current flows."
#@ view "Just after switching"
#@ node a 24 "source: $24\,\mathrm{V}$"
#@ node b 24 "after switch: $24\,\mathrm{V}$"
#@ node c 24 "inductor: $24\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$24\,\mathrm{V}$" col=0
#@ el W a b "closed" col=1
#@ el R b c "$6\,\Omega$" col=2
#@ el L c g "$0.3\,\mathrm{H}$" col=3 plus=c v="$v_L$"
#@ note "Ground the bottom wire. Current is still zero, so the resistor has no fall; the inductor takes all 24 V."
#@ view "One time constant"
#@ node a 24 "source: $24\,\mathrm{V}$"
#@ node b 24 "after switch: $24\,\mathrm{V}$"
#@ node c 8.829107 "inductor: $8.83\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$24\,\mathrm{V}$" col=0 i="$2.53\,\mathrm{A}$" to=a
#@ el W a b "closed" col=1 i="$2.53\,\mathrm{A}$" to=b
#@ el R b c "$6\,\Omega$" col=2 i="$2.53\,\mathrm{A}$" to=c
#@ el L c g "$0.3\,\mathrm{H}$" col=3 plus=c v="$v_L$" i="$2.53\,\mathrm{A}$" to=g
#@ note "Ground the bottom wire. At 50 ms, i = 4(1 - 1/e) A; the resistor falls 15.17 V and the inductor takes 8.83 V."
#@ view "Long after switching"
#@ node a 24 "source: $24\,\mathrm{V}$"
#@ node b 24 "after switch: $24\,\mathrm{V}$"
#@ node c 0 "inductor: $0\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$24\,\mathrm{V}$" col=0 i="$4\,\mathrm{A}$" to=a
#@ el W a b "closed" col=1 i="$4\,\mathrm{A}$" to=b
#@ el R b c "$6\,\Omega$" col=2 i="$4\,\mathrm{A}$" to=c
#@ el L c g "$0.3\,\mathrm{H}$" col=3 plus=c v="$v_L$" i="$4\,\mathrm{A}$" to=g
#@ note "Ground the bottom wire. At steady state the inductor has no step, so i = 24/6 = 4 A."
```

1. Find $I_0$, $I_f$, and $\tau$.
2. Write $i(t)$.
3. Use $v_L=L\dfrac{di}{dt}$ to find $v_L(0^+)$. Does inductor voltage have to stay continuous?

<details><summary>Solution</summary>

1. The current cannot jump, so its starting value remains zero.

   $$I_0=0$$
2. At DC steady state the inductor is a short.

   $$I_f=\dfrac{24}{6}=4\,\mathrm{A}$$
3. Use the RL time constant.

   $$\tau=\dfrac{0.3}{6}=0.050\,\mathrm{s}$$
4. Put the three quantities into the current response.

   $$i(t)=4-4e^{-20t}\,\mathrm{A}$$
5. Differentiate and multiply by inductance.

   $$v_L(t)=0.3(80e^{-20t})=24e^{-20t}\,\mathrm{V}$$

**Answer:** $I_0=0$, $I_f=4\,\mathrm{A}$, $\tau=50\,\mathrm{ms}$. $i(t)=4-4e^{-20t}\,\mathrm{A}$ and $v_L(0^+)=24\,\mathrm{V}$. Inductor voltage can jump; its current is continuous.

</details>

These exponential response formulas apply to the simple first-order circuits here, with constant sources after the switch. In a more complicated RC/RL circuit, use the resistance seen by the storage element after switching for $R$; do not automatically choose one labelled resistor.
