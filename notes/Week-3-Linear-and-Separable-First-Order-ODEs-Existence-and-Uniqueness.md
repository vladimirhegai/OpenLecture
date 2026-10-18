# Week 3: Linear and Separable First-Order ODEs; Existence and Uniqueness

## Topic 1: Linear ODEs and the integrating factor

A first-order ODE is **linear** if it can be written in standard form.

**Standard form** $\dfrac{dy}{dt}+a(t)\,y=f(t)$:
- $a(t)$: the **coefficient** of $y$
- $f(t)$: the **forcing** (the input, e.g. a source)

**The trick:** multiply both sides by the **integrating factor** $\mu(t)=e^{\int a(t)\,dt}$ (mu).
- The left side becomes the derivative of one product, $\mu y$.
- A single derivative can be undone by integrating.

```steps
title "Why the integrating factor works (lecture)"
$$ \dfrac{dy}{dt}+a(t)\,y=f(t) $$
Start from standard form.
$$ \hl{\mu}\dfrac{dy}{dt}+\hl{\mu}\,a\,y=\hl{\mu}\,f $$
Multiply every term by $\mu=e^{\int a\,dt}$.
$$ \mu\dfrac{dy}{dt}+\hl{\dfrac{d\mu}{dt}}\,y=\mu f $$
Chain rule: $\frac{d}{dt}e^{\int a\,dt}=a\,e^{\int a\,dt}$, so $\mu a$ is just $\frac{d\mu}{dt}$.
$$ \hl{\dfrac{d}{dt}\big[\mu\,y\big]}=\mu f $$
Product rule backwards: $\frac{d}{dt}[\mu y]=\mu\frac{dy}{dt}+\frac{d\mu}{dt}y$ is exactly the left side.
$$ \mu\,y=\hl{\int\mu f\,dt+C} $$
Integrate both sides. The $+C$ appears here.
$$ y=\hl{\dfrac{1}{\mu}}\Big[\int\mu f\,dt+C\Big] $$
Divide by $\mu$. Then the initial condition $y(t_0)=y_0$ fixes $C$.
```

$$\begin{gathered}\mu(t)=e^{\int a(t)\,dt}, \\ y(t)=\dfrac{1}{\mu}\Big[\int\mu\,f\,dt+C\Big]\end{gathered}$$

**Example: Example 1 · An RL circuit (lecture)**

The switch closes at $t=0$ and the inductor carries no current before that, so $i(0)=0$. Find $i(t)$.

```schematic
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$10\,\Omega$"
L1 6,3 -> 6,0 "$2\,\mathrm{H}$" i="$i$"
wire 6,0 -> 0,0
ground 0,0
```

1. KVL: the resistor drop $Ri$ plus the inductor drop $L\,di/dt$ equals the source.

   $$2\dfrac{di}{dt}+10\,i=100$$
2. Divide by $L=2$ first. The trap: here $a=5$, not $10$.

   $$\dfrac{di}{dt}+5\,i=50$$
3. $a$ is a constant, so $\int5\,dt=5t$. (No $+C$ is needed inside $\mu$.)

   $$\mu=e^{5t}$$
4. Multiply by $\mu$; the left side collapses into one derivative.

   $$\dfrac{d}{dt}\big[i\,e^{5t}\big]=50\,e^{5t}$$
5. Integrate, using $\int e^{kt}dt=\frac1k e^{kt}$.

   $$i\,e^{5t}=10\,e^{5t}+C$$
6. Put in $i(0)=0$ ($e^0=1$).

   $$0=10+C\ \Rightarrow\ C=-10$$
7. Divide by $e^{5t}$.

   $$i(t)=10-10\,e^{-5t}=10\big(1-e^{-5t}\big)\ \mathrm{A}$$

**Answer:** $i(t)=10\big(1-e^{-5t}\big)\ \mathrm{A}$

```graph
title "The lecture's sketch: change $R$ and watch $i(t)$"
x 0 1.2 label="$t$ (s)"
y 0 21 label="$i$ (A)"
slider R 5 20 10 step=1 label="$R$ ($\Omega$)"
curve "(100/R)*(1-exp(-R*t/2))" label="$i(t)$" color=1
hline "100/R" color=3 label="final value $100/R$"
vline "2/R" label="$t=\tau=L/R$"
readout "final current $=$" "100/R" unit=" A"
readout "$\tau=$" "2/R" unit=" s"
caption "Starts at 0 (an inductor's current can't jump), settles at $100/R$, and is $63\%$ of the way there at $t=\tau$. At $R=10\,\Omega$: 10 A, $\tau=0.2$ s."
```

**Example: Example 2 · A coefficient that changes with time (lecture Example 3.1)**

Solve $\dfrac{dy}{dt}+\dfrac{10\,y}{2t+5}=10$ with $y(0)=0$.

1. It is already in standard form.

   $$a(t)=\dfrac{10}{2t+5},\qquad f(t)=10$$
2. Integrate $a$ with the substitution $u=2t+5$, $du=2\,dt$, and $\int\frac{du}{u}=\ln u$.

   $$\int\dfrac{10}{2t+5}\,dt=5\ln(2t+5)$$
3. Move the 5 into the log ($k\ln u=\ln u^k$), then use $e^{\ln A}=A$.

   $$\mu=e^{\ln(2t+5)^5}=(2t+5)^5$$
4. Multiply by $\mu$ and collapse the left side.

   $$\dfrac{d}{dt}\Big[y\,(2t+5)^5\Big]=10\,(2t+5)^5$$
5. Integrate with the same $u$ ($dt=\frac{du}{2}$) and the power rule $\int u^5du=\frac{u^6}{6}$.

   $$y\,(2t+5)^5=\dfrac56(2t+5)^6+C$$
6. Put in $y(0)=0$; at $t=0$, $2t+5=5$.

   $$0=\dfrac56\,5^6+C\ \Rightarrow\ C=-\dfrac{5^7}{6}\approx-13\,020.83$$
7. Divide by $(2t+5)^5$.

   $$y(t)=\dfrac56(2t+5)-\dfrac{5^7}{6\,(2t+5)^5}$$

**Answer:** $y(t)=\dfrac56(2t+5)-\dfrac{5^7}{6\,(2t+5)^5}$

**Example: Example 3 · A ramp input: the integral needs parts**

Solve $\dfrac{dy}{dt}+2y=4t$ with $y(0)=1$.

1. $a=2$, so $\mu=e^{2t}$. Multiply and collapse.

   $$\dfrac{d}{dt}\big[y\,e^{2t}\big]=4t\,e^{2t}$$
2. The right side is a product, so integrate by parts with $u=4t$, $dv=e^{2t}dt$ (so $v=\frac12e^{2t}$): $\int u\,dv=uv-\int v\,du$.

   $$\int4t\,e^{2t}dt=2t\,e^{2t}-\int2e^{2t}dt$$
3. The leftover integral is $\int2e^{2t}dt=e^{2t}$.

   $$y\,e^{2t}=2t\,e^{2t}-e^{2t}+C$$
4. Divide by $e^{2t}$.

   $$y=2t-1+C\,e^{-2t}$$
5. Put in $y(0)=1$: $1=-1+C$, so $C=2$.

   $$y(t)=2t-1+2e^{-2t}$$

**Answer:** $y(t)=2t-1+2e^{-2t}$

The $e^{-2t}$ part dies out, leaving the line $2t-1$ that tracks the ramp.

**Problem: Try it 1 · Not in standard form yet** (introductory)

Solve $\dfrac{dy}{dt}=3y+6$ with $y(0)=0$.

<details><summary>Solution</summary>

1. Move $3y$ to the left. The coefficient of $y$ is $a=-3$: keep the sign.

   $$\dfrac{dy}{dt}-3y=6$$
2. $\int(-3)\,dt=-3t$.

   $$\mu=e^{-3t}$$
3. Multiply, collapse, integrate ($\int6e^{-3t}dt=-2e^{-3t}$).

   $$y\,e^{-3t}=-2e^{-3t}+C$$
4. Divide by $e^{-3t}$ and put in $y(0)=0$: $0=-2+C$.

   $$y(t)=2e^{3t}-2$$

**Answer:** $y(t)=2e^{3t}-2$

With $a<0$ the solution grows instead of settling.

</details>

**Problem: Try it 2 · A $t$ in front of the derivative** (intermediate)

Solve $t\dfrac{dy}{dt}+2y=4t^2$ with $y(1)=2$, for $t>0$.

<details><summary>Solution</summary>

1. Divide every term by $t$, the right side too.

   $$\dfrac{dy}{dt}+\dfrac2t\,y=4t$$
2. $\int\frac2t\,dt=2\ln t$, and $e^{2\ln t}=e^{\ln t^2}=t^2$.

   $$\mu=t^2$$
3. Multiply by $t^2$, collapse, and integrate ($\int4t^3dt=t^4$).

   $$\dfrac{d}{dt}\big[t^2y\big]=4t^3\ \Rightarrow\ t^2y=t^4+C$$
4. Divide by $t^2$; $y(1)=2$ gives $2=1+C$, so $C=1$.

   $$y(t)=t^2+\dfrac{1}{t^2}$$

**Answer:** $y(t)=t^2+\dfrac{1}{t^2}$

</details>

## Topic 2: Separable ODEs

An ODE is **separable** if it can be written $N(y)\,\dfrac{dy}{dt}=M(t)$ (lecture Definition 3.1):
- $N(y)$: a function of $y$ only
- $M(t)$: a function of $t$ only

Equivalently, $\dfrac{dy}{dt}$ factors into a $t$-part times a $y$-part.

**How to solve:**
- **Separate:** every $y$ with $dy$ on one side, every $t$ with $dt$ on the other.
- **Integrate:** each side in its own variable. One $+C$ is enough.

Unlike the integrating factor, this also works for nonlinear equations.

$$N(y)\,\dfrac{dy}{dt}=M(t)\quad\Rightarrow\quad\int N(y)\,dy=\int M(t)\,dt+C$$

**Example: Example 4 · The same RL circuit, by separation (lecture)**

Solve $\dfrac{di}{dt}+5i=50$, $i(0)=0$ (Example 1) by separating the variables.

1. ```steps
$$ \dfrac{di}{dt}=50-5i $$
Move $5i$ to the right. There is no $t$ at all, so it factors trivially.
$$ \dfrac{\hl{di}}{\hl{50-5i}}=\hl{dt} $$
Separate: every $i$ on the left, every $t$ on the right.
$$ \hl{-\tfrac15\ln|50-5i|}=\hl{t}+C_1 $$
Integrate. Left: $u=50-5i$, $du=-5\,di$, and $\int\frac{du}{u}=\ln|u|$.
$$ \ln|50-5i|=\hl{-5t+C_2} $$
Multiply by $-5$. A constant times $-5$ is just a new constant, $C_2$.
$$ |50-5i|=\hl{e^{C_2}}\,e^{-5t} $$
Exponentiate both sides ($e^{a+b}=e^ae^b$).
$$ 50-5i=\hl{A}\,e^{-5t} $$
Drop the bars: the constant $A=\pm e^{C_2}$ carries the sign.
$$ 50-0=A\ \Rightarrow\ \hl{A=50} $$
Put in $i(0)=0$ ($e^0=1$).
$$ i(t)=\hl{10\big(1-e^{-5t}\big)}\ \mathrm{A} $$
Solve for $i$: $5i=50-50e^{-5t}$, then divide by 5.
```

**Answer:** $i(t)=10\big(1-e^{-5t}\big)\ \mathrm{A}$, the same as Example 1.

This ODE is both linear and separable.

**Example: Example 5 · Dividing can lose a solution (lecture, Spiegel i)**

Find the general solution of $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$.

1. Divide by $y^2$ (only allowed if $y\neq0$) and multiply by $dt$.

   $$\dfrac{dy}{y^2}=\dfrac{dt}{t^3}$$
2. Power rule on both sides: $\int y^{-2}dy=-y^{-1}$ and $\int t^{-3}dt=-\frac12t^{-2}$.

   $$-\dfrac1y=-\dfrac{1}{2t^2}+C$$
3. Multiply by $-1$, write the right side over $2t^2$, and flip both sides.

   $$\dfrac1y=\dfrac{1-2Ct^2}{2t^2}\ \Rightarrow\ y=\dfrac{2t^2}{1-2Ct^2}$$
4. Now check the case the division threw away. $y=0$ gives $0=\frac{0}{t^3}$ ✓, and no value of $C$ produces it.

   $$y\equiv0\ \text{is a solution too}$$

**Answer:** $y=\dfrac{2t^2}{1-2Ct^2}$ for any constant $C$, plus $y=0$

**Example: Example 6 · Factor first (lecture, Spiegel ii)**

Solve $\dfrac{dy}{dt}=\dfrac{3t+t\,y^2}{y+t^2y}$ with $y(1)=3$.

1. It doesn't look separable until you factor $t$ out of the top and $y$ out of the bottom.

   $$\dfrac{dy}{dt}=\dfrac{t\,(3+y^2)}{y\,(1+t^2)}$$
2. Now separate.

   $$\dfrac{y}{3+y^2}\,dy=\dfrac{t}{t^2+1}\,dt$$
3. Each top is half the derivative of its bottom, so each side is $\frac12\ln(\text{bottom})$ (substitute $u=$ bottom).

   $$\tfrac12\ln(3+y^2)=\tfrac12\ln(t^2+1)+c$$
4. Multiply by 2 and exponentiate; $C_1=e^{2c}$.

   $$3+y^2=C_1\,(t^2+1)$$
5. Put in $y(1)=3$: $12=2C_1$.

   $$C_1=6\ \Rightarrow\ y^2=6t^2+3$$
6. Take the $+$ square root, because $y(1)=+3$.

   $$y(t)=\sqrt{6t^2+3}$$

**Answer:** $y^2+3=6(t^2+1)$, i.e. $y(t)=\sqrt{6t^2+3}$

**Example: Example 7 · Differential form, implicit answer (lecture, Spiegel iii)**

Solve $y\,dt+(t^3y^2+t^3)\,dy=0$.

1. Factor $t^3$ out of the $dy$ term and move the $dt$ term across.

   $$t^3\,(y^2+1)\,dy=-y\,dt$$
2. Divide by $t^3y$ to separate, and split the fraction: $\frac{y^2+1}{y}=y+\frac1y$.

   $$\Big(y+\dfrac1y\Big)dy=-t^{-3}\,dt$$
3. Integrate: $\int y\,dy=\frac{y^2}{2}$, $\int\frac{dy}{y}=\ln|y|$, $-\int t^{-3}dt=\frac{t^{-2}}{2}$.

   $$\dfrac{y^2}{2}+\ln|y|=\dfrac{t^{-2}}{2}+C$$
4. Multiply by 2. $y$ can't be isolated (it is squared and inside a log), so leave the answer **implicit**: it is still a complete solution.

   $$y^2+2\ln|y|-t^{-2}=C_1$$

**Answer:** $y^2+2\ln|y|-t^{-2}=C_1$

**Problem: Try it 3 · Pre-tutorial 3** (intermediate)

Solve:
1. $\dfrac{dy}{dt}=-\dfrac{t}{y}$, $y(1)=2$. On what interval does the solution exist?
2. $3t\,(y^2+1)\,dt+y\,(t^2+2)\,dy=0$.
3. $\dfrac{dy}{dt}=8ty+3y$, by separation **and** by the integrating factor. Which route can lose a solution?

<details><summary>Solution</summary>

1. (1) Multiply by $y\,dt$, integrate (power rule) and double; $y(1)=2$ makes the constant $4+1=5$.

   $$y\,dy=-t\,dt\ \Rightarrow\ y^2+t^2=5$$
2. A circle. Take the $+$ root since $y(1)>0$. It ends where $y=0$ (at $t=\pm\sqrt5$): there the slope $-\frac ty$ is infinite.

   $$y=\sqrt{5-t^2},\quad -\sqrt5<t<\sqrt5$$
3. (2) Move the $dt$ term across and divide by $(y^2+1)(t^2+2)$, which is never 0.

   $$\dfrac{y}{y^2+1}\,dy=-\dfrac{3t}{t^2+2}\,dt$$
4. As in Example 6, each top is half the derivative of its bottom, so each side is a log.

   $$\tfrac12\ln(y^2+1)=-\tfrac32\ln(t^2+2)+c$$
5. Multiply by 2, combine the logs ($\ln a+3\ln b=\ln ab^3$) and exponentiate; $K=e^{2c}$.

   $$(y^2+1)(t^2+2)^3=K$$
6. (3) Separation: factor out $y$, divide by it, integrate, exponentiate ($A=\pm e^C$). Dividing by $y$ lost $y=0$: put it back by allowing $A=0$.

   $$\dfrac{dy}{y}=(8t+3)\,dt\ \Rightarrow\ y=A\,e^{4t^2+3t}$$
7. Integrating factor: standard form has $a=-(8t+3)$ and $f=0$.

   $$\dfrac{d}{dt}\Big[e^{-(4t^2+3t)}\,y\Big]=0$$
8. So the bracket is a constant $A$. Nothing was divided by $y$, so $A=0$ is included automatically.

   $$y=A\,e^{4t^2+3t}$$

**Answer:** - **(1)** $y=\sqrt{5-t^2}$ on $-\sqrt5<t<\sqrt5$
- **(2)** $(y^2+1)(t^2+2)^3=K$
- **(3)** $y=Ae^{4t^2+3t}$

Separation loses $y=0$, the integrating factor does not.

</details>

**Problem: Try it 4 · Which method fits?** (introductory)

Linear, separable, both, or neither? (Don't solve.)
1. $\dfrac{dy}{dt}=t^2+y$
2. $\dfrac{dy}{dt}=e^{t+y}$
3. $\dfrac{dy}{dt}=2y-6$
4. $\dfrac{dy}{dt}=t+y^2$

<details><summary>Solution</summary>

1. **Linear** test: $y$ appears only to the first power.
2. **Separable** test: the right side factors into (function of $t$)$\times$(function of $y$).
3. (1) $y$ to the first power: linear. A sum that does not factor: not separable.

   $$\text{linear only}$$
4. (2) $e^{t+y}=e^t\,e^y$ factors: separable. $e^y$ is not first power: not linear.

   $$\text{separable only}$$
5. (3) $2y-6=2(y-3)$ has no $t$, so it factors; and $y$ is first power.

   $$\text{both}$$
6. (4) $y^2$ is not first power, and $t+y^2$ does not factor.

   $$\text{neither}$$

**Answer:** - **(1)** linear only
- **(2)** separable only
- **(3)** both
- **(4)** neither

</details>

## Topic 3: Existence and uniqueness

An **initial value problem** (IVP) is an ODE plus a starting point:
- $\dfrac{dy}{dt}=F(t,y)$: the **ODE**
- $y(t_0)=y_0$: the **starting point**

Before solving, ask: is there a solution through that point, and only one? The theorem answers with two checks on $F$.

$\dfrac{\partial F}{\partial y}$ (the **partial derivative**): differentiate $F$ with respect to $y$, treating $t$ as a constant.

> **Info:** **Existence and uniqueness theorem.** Suppose that in a region $R$ of the $ty$-plane, both $F(t,y)$ and $\dfrac{\partial F}{\partial y}$ are:
> - real, finite and single-valued
> - continuous
> 
> Then exactly one solution passes through each point of $R$.
> 
> The conditions are **sufficient, not necessary**: where they fail, the theorem says nothing. Typical failures:
> - dividing by zero
> - $\ln$ of a number $\le0$
> - negative powers of $y$ at $y=0$

**Example: Example 8 · Find where the theorem applies**

For $\dfrac{dy}{dt}=\dfrac{t+y}{t-y}$, is exactly one solution guaranteed through $(0,1)$? Through $(2,2)$?

1. $F$ breaks only where its bottom is zero: on the line $y=t$.

   $$F=\dfrac{t+y}{t-y},\qquad t\neq y$$
2. Quotient rule in $y$, with $t$ held fixed: the top $t+y$ has $y$-derivative $1$, the bottom $t-y$ has $-1$.

   $$\dfrac{\partial F}{\partial y}=\dfrac{(t-y)+(t+y)}{(t-y)^2}=\dfrac{2t}{(t-y)^2}$$
3. It breaks on the same line, so $R$ is the whole plane minus the line $y=t$. $(0,1)$ is off it; $(2,2)$ is on it.

   $$\begin{gathered}(0,1):\ \text{one solution} \\ (2,2):\ \text{no promise}\end{gathered}$$

**Answer:** - **Through $(0,1)$:** yes, exactly one solution.
- **Through $(2,2)$:** no guarantee. It sits on the line $y=t$, where $F$ is undefined.

**Example: Example 9 · Two solutions from one point**

For $\dfrac{dy}{dt}=y^{1/3}$ with $y(0)=0$:
1. Show that it has two different solutions.
2. Explain why the theorem allows it.

1. $F=y^{1/3}$ is continuous, but its $y$-derivative (power rule) has $y$ in the bottom.

   $$\dfrac{\partial F}{\partial y}=\dfrac{1}{3\,y^{2/3}}\ \to\ \infty\ \text{at}\ y=0$$
2. The start $(0,0)$ is on the bad line $y=0$, so the theorem promises nothing there. Solution 1 is the constant $y=0$: slope 0, and $0^{1/3}=0$.

   $$y_1(t)=0$$
3. Solution 2: separate, $y^{-1/3}dy=dt$. Power rule: $\int y^{-1/3}dy=\frac32y^{2/3}$. $y(0)=0$ makes $C=0$.

   $$\tfrac32\,y^{2/3}=t$$
4. Raise both sides to the power $\frac32$.

   $$y_2(t)=\Big(\dfrac{2t}{3}\Big)^{3/2},\quad t\ge0$$

**Answer:** $y=0$ and $y=(2t/3)^{3/2}$ both pass through $(0,0)$.

No contradiction: $\partial F/\partial y$ is infinite on $y=0$.

```graph
title "$dy/dt=y^{1/3}$: one curve per point, except on $y=0$"
x -3 4 label="$t$"
y -1.5 3 label="$y$"
region "abs(y)>0.1" color=3 label="conditions hold ($y\neq0$)"
field "cbrt(y)"
family c 0 3 0.5 "if(t>c,(2*(t-c)/3)^1.5,0)" color=4 label="solutions through $(0,0)$"
hline "0" color=2 label="$\partial F/\partial y=\infty$"
drag P -1 1 label="start" color=1
solution "cbrt(y)" x0="P_x" y0="P_y" color=1 label="solution through your start"
caption "Drag the start anywhere off the axis: exactly one curve. The purple curves sit on $y=0$ and then lift off, so through any point on the axis pass many solutions."
```

**Example: Example 10 · A smooth $F$, yet the solution blows up**

Solve $\dfrac{dy}{dt}=y^2$ with $y(0)=1$. For which $t$ does the solution exist?

1. Check the theorem first: $F$ and its $y$-derivative are continuous everywhere, so there is exactly one solution.

   $$F=y^2,\qquad\dfrac{\partial F}{\partial y}=2y$$
2. Separate and integrate with the power rule, $\int y^{-2}dy=-\frac1y$.

   $$\dfrac{dy}{y^2}=dt\ \Rightarrow\ -\dfrac1y=t+C$$
3. Put in $y(0)=1$: $C=-1$. Solve for $y$.

   $$-\dfrac1y=t-1\ \Rightarrow\ y=\dfrac{1}{1-t}$$
4. As $t\to1$ the bottom goes to 0 and $y\to\infty$. The theorem only promises a solution **near** $t_0$; this one ends at $t=1$.

   $$\text{exists only for } t<1$$

**Answer:** $y(t)=\dfrac{1}{1-t}$, which exists only for $t<1$ (it blows up at $t=1$)

```graph
title "$dy/dt=y^2$: drag the start, find the blow-up"
x -2 3 label="$t$"
y -2 6 label="$y$"
field "y^2"
drag P 0 1 label="$(t_0,y_0)$" color=1 snap=0.25
solution "y^2" x0="P_x" y0="P_y" color=1 label="the one solution"
vline "P_x+1/P_y" color=2 label="blow-up $t=t_0+1/y_0$"
readout "blows up at $t=$" "P_x+1/P_y"
caption "Start higher and it blows up sooner; start at $y_0=0$ and it stays $0$ forever. Below the axis it blows up to $-\infty$ in the past."
```

**Problem: Try it 5 · A linear equation: the region is a strip** (intermediate)

For $(t-3)\dfrac{dy}{dt}+(\ln t)\,y=2t$ with $y(1)=2$:
1. Where do the theorem's conditions hold?
2. Is exactly one solution through the start guaranteed?

<details><summary>Solution</summary>

1. Solve for $dy/dt$ to get $F$.

   $$F=\dfrac{2t-(\ln t)\,y}{t-3}$$
2. Differentiate in $y$ ($t$ held fixed): only the $y$ term survives.

   $$\dfrac{\partial F}{\partial y}=-\dfrac{\ln t}{t-3}$$
3. $\ln t$ needs $t>0$; dividing needs $t\neq3$. Neither depends on $y$, so the good regions are vertical strips.

   $$0<t<3\quad\text{or}\quad t>3\qquad(\text{any }y)$$
4. The start $(1,2)$ has $t=1$, inside $0<t<3$.

   $$\text{exactly one solution}$$

**Answer:** - **Conditions hold:** for $0<t<3$ and for $t>3$, at every $y$.
- **Guaranteed?** Yes: the start is in $0<t<3$.

</details>

**Problem: Try it 6 · Silent, not negative** (intermediate)

For $t\dfrac{dy}{dt}=y$: how many solutions pass through $(0,0)$? Through $(0,1)$?

<details><summary>Solution</summary>

1. Both break at $t=0$, so the theorem says nothing about either start.

   $$F=\dfrac yt,\quad\dfrac{\partial F}{\partial y}=\dfrac1t$$
2. Separate and integrate ($\ln|y|=\ln|t|+C$): every solution is a line through the origin.

   $$\dfrac{dy}{y}=\dfrac{dt}{t}\ \Rightarrow\ y=c\,t\quad(\text{any } c)$$
3. Every line $y=ct$ passes through $(0,0)$: infinitely many solutions.

   $$(0,0):\ \infty\ \text{solutions}$$
4. Put $t=0$ into the ODE itself: every solution has $y(0)=0$, so none reaches $(0,1)$.

   $$0\cdot\dfrac{dy}{dt}=y(0)\ \Rightarrow\ y(0)=0$$

**Answer:** - **Through $(0,0)$:** infinitely many (all $y=ct$).
- **Through $(0,1)$:** none.

Where the conditions fail, anything can happen.

</details>
