# Week 2: Classifying ODEs, Initial Value Problems and RC/RL Circuits

## Topic 1: Classifying a differential equation

A **differential equation** is an equation for an unknown *function* that involves its derivatives.

It is **ordinary** (an ODE) when the derivatives are taken with respect to one variable only.
- $t$: the **independent variable** (here, time)
- $i(t)$: the **dependent variable** (the unknown, such as a current)

Week 1's $\dfrac{di}{dt}+\dfrac{R}{L}i=0$ is an ODE.

An ODE is **linear** if it can be written as

$$a_n(t)\dfrac{d^ny}{dt^n}+\dots+a_1(t)\dfrac{dy}{dt}+a_0(t)\,y=f(t)$$

In this form:
- $a_k(t)$: the **coefficients** (may depend on $t$, never on $y$)
- $f(t)$: the **forcing** (the input, a source)

Linear means scaling works: if $y$ solves it with forcing $f$, then $A\,y$ solves it with forcing $A\,f$. Double the source, double the response.

| Label | Test |
|---|---|
| **Order** | The highest derivative of the unknown. $\dfrac{di}{dt}+\dfrac{R}{L}i=0$ is 1st order; the RLC equation $\dfrac{d^2i}{dt^2}+\dfrac{R}{L}\dfrac{di}{dt}+\dfrac{i}{LC}=0$ is 2nd order. |
| **Linear** | Fits the form above: $y$ and its derivatives appear alone, to the first power. Any $y^2$, $y\dfrac{dy}{dt}$, $\sin y$, $e^{y}$, $\dfrac1y$ makes it **nonlinear**. |
| **Homogeneous** | Linear, and $f(t)\equiv0$ ("zero for every $t$") once every $y$-term is on the left. |
| **Constant-coefficient** | Linear, and every $a_k$ is a constant (like $R$, $L$, $C$). |
| **Autonomous** | No $t$ anywhere except inside $y(t)$: the equation does not change with time. |

**Example: Example 1 · Functions of t are allowed (lecture Example 2.1)**

Is $t^3\dfrac{d^2y}{dt^2}+e^{t}\dfrac{dy}{dt}+y=0$ linear? Classify it fully.

1. The highest derivative is $\dfrac{d^2y}{dt^2}$.

   $$\text{order }2$$
2. $y$ and its derivatives each appear alone, to the first power. $t^3$ and $e^{t}$ are functions of $t$ only: the linear form allows that.

   $$a_2(t)=t^3,\quad a_1(t)=e^{t},\quad a_0=1$$
3. Nothing is left on the right.

   $$f(t)=0\ \Rightarrow\ \text{homogeneous}$$
4. But $t^3$ and $e^{t}$ change with time, so it is neither constant-coefficient nor autonomous.

   $$\text{variable coefficients, not autonomous}$$

**Answer:** Yes, linear: second-order, linear, homogeneous, variable-coefficient, not autonomous.

Linearity only cares how $y$ appears, not how $t$ appears.

**Example: Example 2 · Move the y-terms left before judging**

Classify $\dfrac{dy}{dt}=3y$ and $\dfrac{dy}{dt}=3y+2$.

1. Put every $y$-term on the left. The first has nothing left over on the right.

   $$\dfrac{dy}{dt}-3y=0\ \Rightarrow\ \text{homogeneous}$$
2. The second keeps a $2$: that is forcing, so it is not homogeneous.

   $$\dfrac{dy}{dt}-3y=2\ \Rightarrow\ f(t)=2$$
3. A constant forcing does not change with time, so the second one is still autonomous. Both are first-order, linear, constant-coefficient.

   $$\text{no }t\text{ anywhere}\ \Rightarrow\ \text{autonomous}$$

**Answer:** Both: first-order, linear, constant-coefficient, autonomous.
- $\dfrac{dy}{dt}=3y$: homogeneous
- $\dfrac{dy}{dt}=3y+2$: not homogeneous

**Example: Example 3 · A power is not an order**

Classify $\left(\dfrac{dy}{dt}\right)^3+\sin y=0$.

1. The cube is a power, not a derivative: the highest derivative is still the first.

   $$\text{order }1$$
2. $\left(\frac{dy}{dt}\right)^3$ (a derivative cubed) and $\sin y$ (the unknown inside a function) are both nonlinear.

   $$\text{nonlinear}$$
3. "Homogeneous" and "constant-coefficient" only apply to linear equations. No $t$ appears, so it is autonomous.

   $$\text{autonomous}$$

**Answer:** First-order, nonlinear, autonomous.

**Problem: Try it 1 · Scaling a solution** (introductory)

1. $y=t$ solves $\dfrac{dy}{dt}+y=1+t$. Without solving, find a solution of $\dfrac{dy}{dt}+y=5+5t$.

2. $y=\dfrac{1}{1-t}$ solves $\dfrac{dy}{dt}=y^2$. Is $2y=\dfrac{2}{1-t}$ also a solution?

<details><summary>Solution</summary>

1. The new forcing is $5\times$ the old one, and the equation is linear, so $5\times$ the old solution works.

   $$y=5t$$
2. Check: $\dfrac{d}{dt}(5t)=5$.

   $$5+5t=5+5t\ \checkmark$$
3. Part 2: $\dfrac{d}{dt}(1-t)^{-1}=(1-t)^{-2}$ (chain rule), so doubling $y$ doubles the left side but quadruples $y^2$.

   $$\dfrac{2}{(1-t)^2}\neq\dfrac{4}{(1-t)^2}$$

**Answer:** 1. $y=5t$.
2. No: scaling only works for linear equations, and $y^2$ makes this one nonlinear.

</details>

**Problem: Try it 2 · Circuit equations** (introductory)

Classify each ($C$, $R$, $I_0$, $\omega$, $V_T$ are constants):

1. $C\dfrac{dv}{dt}+\dfrac{v}{R}=I_0\cos(\omega t)$ (an RC circuit driven by an AC source)

2. $C\dfrac{dv}{dt}+I_0\big(e^{v/V_T}-1\big)=0$ (a capacitor discharging through a diode)

<details><summary>Solution</summary>

1. 1: $v$ and $\dfrac{dv}{dt}$ appear linearly, times the constants $C$ and $\dfrac1R$. The forcing $I_0\cos(\omega t)$ is not zero and depends on $t$.

   $$\text{constant coefficients, but }t\text{ in the forcing}$$
2. 2: the unknown $v$ sits inside an exponential, so it is nonlinear. No $t$ appears.

   $$e^{v/V_T}\ \Rightarrow\ \text{nonlinear}$$

**Answer:** 1. First-order, linear, nonhomogeneous, constant-coefficient, not autonomous.
2. First-order, nonlinear, autonomous.

</details>

## Topic 2: Solutions and initial value problems

A **solution** is a function that makes the equation true for **every** $t$.

To check one:
1. differentiate it
2. substitute into the equation
3. simplify both sides

Two more terms:
- **General solution**: the whole **family** of solutions of a first-order ODE, with one free constant $K$.
- **Initial value problem** (IVP): the ODE plus an **initial condition** $y(t_0)=y_0$ (the value at a starting time). That picks out one curve of the family.

A second-order ODE needs two conditions: $y(t_0)$ and $\dfrac{dy}{dt}(t_0)$.

```graph
title "$\dfrac{dy}{dt}=-2y+6$: drag the initial point"
x 0 3 label="$t$"
y -1 7 label="$y$"
field "-2*y+6"
family K -4 4 1 "3+K*exp(-2*t)" color=0
hline "3" label="$y=3$"
drag P 0 1 label="$(t_0,y_0)$" snap=0.25
solution "-2*y+6" x0="P_x" y0="P_y" label="the IVP solution"
readout "$K=(y_0-3)e^{2t_0}=$" "(P_y-3)*exp(2*P_x)"
caption "Faint curves: the family $y=3+Ke^{-2t}$. Each starting point picks one. Slide the point along its own curve: $K$ stays the same."
```

**Example: Example 4 · True for every t, not just one**

Which of $y=\cos 2t$ and $y=\sin t$ solve $\dfrac{d^2y}{dt^2}+4y=0$?

1. ```steps
$$ y=\cos 2t $$
The candidate.
$$ \dfrac{dy}{dt}=\hl{-2\sin 2t} $$
Chain rule: $\frac{d}{dt}\cos(at)=-a\sin(at)$.
$$ \dfrac{d^2y}{dt^2}=\hl{-4\cos 2t} $$
Again: $\frac{d}{dt}\sin(at)=a\cos(at)$.
$$ \dfrac{d^2y}{dt^2}+4y=\hl{-4\cos 2t+4\cos 2t} $$
Substitute into the left side.
$$ \dfrac{d^2y}{dt^2}+4y=\hl{0}\ \checkmark $$
Zero for every $t$: a solution.
```
2. For $y=\sin t$: $\dfrac{d^2y}{dt^2}=-\sin t$. Substituting leaves $3\sin t$.

   $$-\sin t+4\sin t=3\sin t$$
3. That is $0$ at $t=0$, but not at $t=\frac{\pi}{2}$, so it is **not** a solution.

   $$3\sin t\neq0$$

**Answer:** $\cos 2t$ is a solution; $\sin t$ is not.

**Example: Example 5 · One family, one condition**

Show that $y=3+Ke^{-2t}$ solves $\dfrac{dy}{dt}=-2y+6$ for every constant $K$. Then solve the IVP with $y(0)=1$.

1. Left side: the $3$ gives $0$, and $\frac{d}{dt}e^{-2t}=-2e^{-2t}$ (chain rule).

   $$\dfrac{dy}{dt}=-2Ke^{-2t}$$
2. Right side with the same $y$: the $6$s cancel. Both sides match for any $K$.

   $$-2(3+Ke^{-2t})+6=-2Ke^{-2t}\ \checkmark$$
3. Now put in the condition: at $t=0$, $e^{0}=1$.

   $$y(0)=3+K=1\ \Rightarrow\ K=-2$$

**Answer:** $y(t)=3-2e^{-2t}$.

In the graph above, put the point at $(0,1)$: the readout shows $K=-2$.

**Problem: Try it 3 · Starting the clock later** (introductory)

Same family $y=3+Ke^{-2t}$. Solve the IVP with $y(1)=5$.

<details><summary>Solution</summary>

1. Put $t=1$, not $t=0$: now $e^{-2}$ does not become $1$.

   $$3+Ke^{-2}=5\ \Rightarrow\ K=2e^{2}\approx14.78$$
2. Substitute and combine the exponentials ($e^{2}e^{-2t}=e^{-2(t-1)}$).

   $$y(t)=3+2e^{-2(t-1)}$$

**Answer:** $y(t)=3+2e^{-2(t-1)}$ ($K=2e^2\approx14.78$; drag the point to $(1,5)$ to see it).

</details>

**Problem: Try it 4 · The solution that never moves** (introductory)

For $\dfrac{dy}{dt}+ay=b$ with constants $a>0$ and $b$:
1. Which constant function $y=c$ is a solution?
2. Use the family $y=\dfrac{b}{a}+Ke^{-at}$ to show every solution ends up there.

<details><summary>Solution</summary>

1. A constant has derivative $0$.

   $$0+ac=b\ \Rightarrow\ c=\dfrac{b}{a}$$
2. It is the $K=0$ member of the family. For the others, $e^{-at}\to0$ as $t\to\infty$.

   $$y(t)=\dfrac{b}{a}+Ke^{-at}\ \to\ \dfrac{b}{a}$$

**Answer:** $y=\dfrac{b}{a}$. Every solution approaches it (in the graph: $y=3$).

Topic 3 finds a circuit's final value this way, by setting the derivative to $0$.

</details>

## Topic 3: First-order RC and RL circuits

A circuit with one capacitor or one inductor gives a first-order linear ODE, because each element's law has one derivative.

Both laws use the **passive sign convention** (the current arrow enters the $+$ end).

Two moments matter at a switch:
- $0^-$: just before the switch moves
- $0^+$: just after

|  | Capacitor $C$ (farads) | Inductor $L$ (henries) |
|---|---|---|
| Law | $i=C\dfrac{dv}{dt}$ | $v=L\dfrac{di}{dt}$ |
| DC steady state (nothing changes) | open circuit: $i=0$ | short: $v=0$ |
| Can't jump at a switch | its voltage $v_C$ | its current $i_L$ |
| Time constant | $\tau=RC$ | $\tau=L/R$ |

**Example: Example 6 · RC natural response (lecture Figures 2.3–2.4)**

The switch has been at $a$ for a long time and moves to $b$ at $t=0$ (drawn as two switches acting together).

Find $v(t)$ for $t\ge0$.

```schematic
V1 0,3 -> 0,0 "$V_s$"
R1 0,3 -> 3,3 "$R_1$"
S1 3,3 -> 5,3 "$t=0$" action=open
C1 5,3 -> 5,0 "$C$" v="$v$"
S2 5,3 -> 8,3 "$t=0$" action=close
R2 8,3 -> 8,0 "$R$" i="$i$"
wire 8,0 -> 0,0
label 3,3 "$a$" above
label 8,3 "$b$" above
ground 0,0
```

1. Before $t=0$ the capacitor is open (DC), so no current flows in $R_1$, $R_1$ has no voltage, and $C$ sees all of $V_s$.

   $$v(0^-)=V_s$$
2. $v_C$ can't jump.

   $$v(0^+)=V_s$$
3. For $t\ge0$ only $C$ and $R$ are left. KCL at the top node (current down $C$ + current down $R$ = 0), with $v(0)=V_s$, is an IVP.

   $$C\dfrac{dv}{dt}+\dfrac{v}{R}=0$$
4. Divide by $C$. Same shape as Week 1's $\frac{di}{dt}+\frac{R}{L}i=0$, so the same solution, with $\tau=RC$.

   $$\dfrac{dv}{dt}+\dfrac{v}{RC}=0\ \Rightarrow\ v=V_se^{-t/\tau}$$
5. After one time constant, $e^{-1}\approx0.37$ is left.

   $$v(\tau)\approx0.37\,V_s$$

**Answer:** $v(t)=V_se^{-t/\tau}$, $\tau=RC$, $t\ge0$.

$R_1$ does not appear: after the switch it is cut off.

```schematic
I1 0,0 -> 0,3 "$I_s$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$R$" i="$v/R$"
S1 3,3 -> 6,3 "$t=0$" action=close
C1 6,3 -> 6,0 "$C$" v="$v$" i="$i$"
wire 6,0 -> 0,0
ground 0,0
```

```steps
title "Solving the step response (lecture)"
$$ C\dfrac{dv}{dt}+\dfrac{v}{R}=I_s $$
KCL at the top node for $t\ge0$: $I_s$ in = current down $C$ + current down $R$.
$$ \dfrac{dv}{dt}+\dfrac{v}{\hl{RC}}=\hl{\dfrac{I_s}{C}} $$
Divide by $C$. Same left side as the natural response, so $\tau=RC$.
$$ 0+\dfrac{V_f}{RC}=\dfrac{I_s}{C}\ \Rightarrow\ \hl{V_f=RI_s} $$
Final value $V_f$: in the end nothing changes, so $\frac{dv}{dt}=0$.
$$ \dfrac{du}{dt}+\dfrac{u+\hl{RI_s}}{RC}=\dfrac{I_s}{C} $$
Let $u=v-V_f$, the distance still to go. $V_f$ is constant, so $\frac{du}{dt}=\frac{dv}{dt}$.
$$ \dfrac{du}{dt}+\dfrac{u}{RC}=\hl{0} $$
$\frac{RI_s}{RC}=\frac{I_s}{C}$ cancels the right side.
$$ u(t)=\hl{(V_0-V_f)}\,e^{-t/\tau} $$
The natural response again, starting from $u(0)=V_0-V_f$.
$$ v(t)=\hl{V_f+}(V_0-V_f)\,e^{-t/\tau} $$
Add $V_f$ back: $v=u+V_f$.
$$ v(t)=\hl{RI_s}+(V_0-\hl{RI_s})\,e^{-t/RC} $$
For this circuit (lecture Eq. 2.5).
```

> **Tip:** **Any RC or RL circuit after a switch:** $x(t)=x_f+(x_0-x_f)\,e^{-t/\tau}$, where $x$ is $v_C$ or $i_L$.
> 
> - $x_0$: its value just before the switch (it can't jump).
> - $x_f$: its value long after (DC: $C$ open, $L$ short). No source left means $x_f=0$: the natural response.
> - $\tau=RC$ or $L/R$, with $R$ the resistance the element sees after the switch.

```graph
title "$v(t)=V_f+(V_0-V_f)e^{-t/RC}$"
x 0 60 label="$t$ (ms)"
y -1 14 label="$v$ (V)"
slider V0 0 12 2 step=0.5 label="$V_0$ (V)"
slider Vf 0 12 12 step=0.5 label="$V_f$ (V)"
slider R 0.5 5 4 step=0.1 label="$R$ (k$\Omega$)"
slider C 0.2 4 2 step=0.1 label="$C$ ($\mu$F)"
curve "Vf+(V0-Vf)*exp(-t/(R*C))" label="$v(t)$"
hline "Vf" color=0 label="$V_f$"
vline "R*C" color=2 label="$t=\tau$"
point "R*C" "Vf+(V0-Vf)*exp(-1)" color=2
vline "5*R*C" color=0 label="$t=5\tau$"
readout "$\tau=RC=$" "R*C" unit=" ms"
readout "$v(\tau)=$" "Vf+(V0-Vf)*exp(-1)" unit=" V"
caption "By $t=\tau$ it has covered $63\%$ of the way from $V_0$ to $V_f$; by $5\tau$, over $99\%$. Set $V_f=0$ for the natural response. Defaults: Example 8."
```

**Example: Example 7 · What can jump? (Pre-tutorial 2)**

In Fig. 2.6, $V_0=0$, $I_s=2\,\mathrm{A}$ and $R=1\,\mathrm{k\Omega}$.

Find the capacitor current $i$:
- at $t=0^-$ (switch open)
- at $t=0^+$ (switch closed)

Is it discontinuous at $t=0$, unlike $v$?

```schematic
I1 0,0 -> 0,3 "$2\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$1\,\mathrm{k\Omega}$" i="$v/R$"
S1 3,3 -> 6,3 "$t=0$" action=close
C1 6,3 -> 6,0 "$C$" v="$v$" i="$i$"
wire 6,0 -> 0,0
ground 0,0
```

1. At $0^-$ the switch is open: the capacitor branch is broken.

   $$i(0^-)=0$$
2. $v_C$ can't jump, and it started at $V_0=0$.

   $$v(0^+)=v(0^-)=0$$
3. So $R$ carries $\frac{v}{R}=0$, and KCL sends all of $I_s$ into the capacitor.

   $$i(0^+)=I_s-\dfrac{v(0^+)}{R}=2\,\mathrm{A}$$
4. Check with the formula $v=RI_s\big(1-e^{-t/RC}\big)$: then $i=C\frac{dv}{dt}=I_se^{-t/RC}$, which is $2\,\mathrm{A}$ at $0^+$ whatever $C$ is.

   $$i(t)=2e^{-t/RC}\,\mathrm{A}$$

**Answer:** $i(0^-)=0$, $i(0^+)=2\,\mathrm{A}$: yes, the capacitor current jumps, while $v$ stays at $0$.

Only $v_C$ and $i_L$ must be continuous.

**Example: Example 8 · Charging from a voltage source**

The $2\,\mu\mathrm{F}$ capacitor holds $2\,\mathrm{V}$ when the switch closes at $t=0$. Find $v(t)$ and the time when $v=10\,\mathrm{V}$.

```schematic
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$4\,\mathrm{k\Omega}$" i="$i$"
C1 6,3 -> 6,0 "$2\,\mu\mathrm{F}$" v="$v$"
wire 6,0 -> 0,0
ground 0,0
```

1. The stored voltage carries over: it starts at $2\,\mathrm{V}$, not $0$.

   $$v(0^+)=2\,\mathrm{V}$$
2. KVL round the loop for $t\ge0$. In series one current flows, and it is the capacitor current.

   $$12=4000\,i+v,\qquad i=2\times10^{-6}\dfrac{dv}{dt}$$
3. Substitute ($4000\times2\times10^{-6}=0.008$), then divide by $0.008$.

   $$\dfrac{dv}{dt}+125v=1500$$
4. $\tau=RC=8\,\mathrm{ms}$ ($\frac1\tau=125$). Long after, $C$ is open, $R$ carries nothing, so $v_f=12\,\mathrm{V}$.

   $$v(t)=12+(2-12)e^{-125t}=12-10e^{-125t}$$
5. Set $v=10$, isolate the exponential, take $\ln$ ($\ln e^{x}=x$, $\ln0.2=-\ln5$).

   $$e^{-125t}=0.2\ \Rightarrow\ t=\dfrac{\ln5}{125}=12.9\,\mathrm{ms}$$

**Answer:** $v(t)=12-10e^{-125t}\,\mathrm{V}$; $v=10\,\mathrm{V}$ at $t\approx12.9\,\mathrm{ms}$ (about $1.6\tau$).

**Example: Example 9 · The inductor version: RL step response**

The inductor has no current before the switch closes at $t=0$. Find $i(t)$ and the inductor voltage $v_L(t)$.

```schematic
V1 0,3 -> 0,0 "$24\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$6\,\Omega$"
L1 6,3 -> 6,0 "$0.3\,\mathrm{H}$" i="$i$" v="$v_L$"
wire 6,0 -> 0,0
ground 0,0
```

1. $i_L$ can't jump.

   $$i(0^+)=0$$
2. KVL for $t\ge0$: source = resistor + inductor. Divide by $0.3$.

   $$24=6i+0.3\dfrac{di}{dt}\ \Rightarrow\ \dfrac{di}{dt}+20i=80$$
3. $\tau=\frac{L}{R}$: here a bigger $R$ makes it faster (for RC, slower). Long after, $L$ is a short.

   $$\begin{gathered}\tau=\dfrac{0.3}{6}=50\,\mathrm{ms}, \\ i_f=\dfrac{24}{6}=4\,\mathrm{A}\end{gathered}$$
4. The step-response formula.

   $$i(t)=4+(0-4)e^{-20t}=4-4e^{-20t}$$
5. $v_L=L\frac{di}{dt}$ (chain rule). It jumps from $0$ to $24\,\mathrm{V}$ at $0^+$: an inductor's voltage may jump, its current may not.

   $$v_L=0.3\cdot80e^{-20t}=24e^{-20t}$$

**Answer:** $i(t)=4-4e^{-20t}\,\mathrm{A}$, $v_L(t)=24e^{-20t}\,\mathrm{V}$, $\tau=50\,\mathrm{ms}$.

**Problem: Try it 5 · Two resistors: which R is in τ?** (intermediate)

The capacitor is uncharged and the switch closes at $t=0$. Find $\tau$, $v(t)$ and $i(0^+)$.

```schematic
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
S1 0,3 -> 2,3 "$t=0$" action=close
R1 2,3 -> 5,3 "$6\,\mathrm{k\Omega}$"
R2 5,3 -> 5,0 "$3\,\mathrm{k\Omega}$"
wire 5,3 -> 8,3
C1 8,3 -> 8,0 "$5\,\mu\mathrm{F}$" v="$v$" i="$i$"
wire 8,0 -> 0,0
label 5,3 "$a$" above
ground 0,0
```

<details><summary>Solution</summary>

1. KCL at node $a$ (voltage $v$): current out through $6\,\mathrm{k\Omega}$, through $3\,\mathrm{k\Omega}$, and into $C$ adds to $0$.

   $$\dfrac{v-12}{6000}+\dfrac{v}{3000}+5\times10^{-6}\dfrac{dv}{dt}=0$$
2. Multiply by $6000$, then divide by $0.03$.

   $$\dfrac{dv}{dt}+100v=400$$
3. So $\tau=10\,\mathrm{ms}$. That is $(6\,\mathrm{k}\parallel3\,\mathrm{k})\,C=2\,\mathrm{k\Omega}\times5\,\mu\mathrm{F}$: with the source off, $C$ sees both resistors in parallel.

   $$\tau=(R_1\parallel R_2)\,C=10\,\mathrm{ms}$$
4. Final value: $C$ open, so a voltage divider; $V_0=0$.

   $$v_f=12\cdot\tfrac{3}{9}=4\ \Rightarrow\ v(t)=4-4e^{-100t}$$
5. At $0^+$, $v=0$, so $3\,\mathrm{k\Omega}$ carries nothing and all of $\frac{12}{6000}$ goes into $C$.

   $$i(0^+)=2\,\mathrm{mA}$$

**Answer:** - $\tau=10\,\mathrm{ms}$ (not $6\,\mathrm{k\Omega}\times C$)
- $v(t)=4-4e^{-100t}\,\mathrm{V}$
- $i(0^+)=2\,\mathrm{mA}$

</details>

**Problem: Try it 6 · Read a response backwards** (intermediate)

A capacitor voltage is $v(t)=8-6e^{-250t}\,\mathrm{V}$ for $t\ge0$. Find:
- $V_0$, $V_f$ and $\tau$
- the ODE it satisfies
- the current if $C=4\,\mu\mathrm{F}$

<details><summary>Solution</summary>

1. Match with $V_f+(V_0-V_f)e^{-t/\tau}$: the constant is $V_f$, $t=0$ gives $V_0$, the exponent gives $\frac1\tau$.

   $$V_f=8,\quad V_0=8-6=2,\quad \tau=\tfrac{1}{250}\,\mathrm{s}=4\,\mathrm{ms}$$
2. Every such response solves $\frac{dv}{dt}+\frac{v}{\tau}=\frac{V_f}{\tau}$ (its constant solution is $V_f$, as in Try it 4). Here $\frac1\tau=250$.

   $$\dfrac{dv}{dt}+250v=2000$$
3. $\frac{d}{dt}e^{-250t}=-250e^{-250t}$ (chain rule), so $\frac{dv}{dt}=(-6)(-250)e^{-250t}=1500e^{-250t}$. Multiply by $C$.

   $$i=4\times10^{-6}\cdot1500e^{-250t}=6e^{-250t}\,\mathrm{mA}$$

**Answer:** - $V_0=2\,\mathrm{V}$, $V_f=8\,\mathrm{V}$, $\tau=4\,\mathrm{ms}$
- ODE: $\dfrac{dv}{dt}+250v=2000$
- $i(t)=6e^{-250t}\,\mathrm{mA}$

</details>
