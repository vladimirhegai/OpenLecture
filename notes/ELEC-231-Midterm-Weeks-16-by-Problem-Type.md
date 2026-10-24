# ELEC 231 Midterm: Weeks 1–6 by Problem Type

## Start here: what the midterm asks

**Midterm:** Friday Oct 30 · 2 hours · 30 marks · Weeks 1–6 · Casio 991 only.

Every solution in this note is written in the same three moves. Use them on the exam too:

1. **Type:** name the kind of problem, and the clue in the question that told you.
2. **Method:** follow the numbered steps from that subtopic.
3. **Conditions:** use the given values (or the circuit before the switch) to fix the constants.

Find your question in the left column, then jump to its section. Clicking a link scrolls there; the browser’s Back button returns.

| The question gives you… | Go to | Weeks |
|---|---|---|
| a complex number to convert, multiply, divide, raise to a power or take roots of | [Topic A](#topic-a) | 1 |
| an ODE to classify, or a function to check | [Topic B](#topic-b) | 2 |
| a first-order ODE where the $y$’s and $t$’s can be split apart | [B1 · Separable](#b1) | 3 |
| $y^{\prime}+a(t)\,y=f(t)$ | [B2 · Integrating factor](#b2) | 3 |
| $M\,dt+N\,dy=0$ | [B3 · Exact](#b3), [B4 · Make it exact](#b4) | 4 |
| $ay^{\prime\prime}+by^{\prime}+cy=0$ (numbers $a,b,c$) | [B5 · Characteristic equation](#b5) | 4–5 |
| $ay^{\prime\prime}+by^{\prime}+cy=g(t)$ | [B6 · Undetermined coefficients](#b6) | 6 |
| a second-order ODE with $t$ in the coefficients, and one solution given | [B7 · Reduction of order](#b7) | 6 |
| “does a unique solution exist?”, an interval, or two solutions to compare | [Topic C](#topic-c) | 3, 5, 6 |
| a circuit with a switch: find $v(t)$ or $i(t)$ | [Topic D](#topic-d) | 1–3, 5 |

## Topic A: Complex numbers

[Week 1 · Topic 1](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/1cbac07a-cd02-48c2-8c30-c9829c4e06b2#079a564f-840a-46b1-9f12-5d8d123edad9) [Week 1 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/1cbac07a-cd02-48c2-8c30-c9829c4e06b2#fef2e73f-cd85-498c-9b6a-1ff1e058d7d3)

Complex numbers show up twice on the midterm:

- as their own question (convert, divide, raise to a power, take roots);
- inside [B5](#b5), when a characteristic equation has no real roots and you need $\sqrt{-36}=j6$.

**One number, two ways to write it.** A complex number is a point (an arrow) in the plane. You can give its coordinates, or its length and angle:

$$z=a+jb=c\,e^{j\theta}=c\angle\theta$$

- $a=\mathrm{Re}\{z\}$: the **real part**, how far right
- $b=\mathrm{Im}\{z\}$: the **imaginary part**, how far up
- $c=|z|$: the **magnitude**, the length of the arrow
- $\theta=\angle z$: the **angle**, measured from the positive real axis
- $j=\sqrt{-1}$, so $j^2=-1$ (this course writes $j$, not $i$)

Example: $3+j4$ has $a=3$, $b=4$, $c=\sqrt{9+16}=5$ and $\theta=\tan^{-1}(4/3)=53.13^\circ$, so $3+j4=5\angle53.13^\circ$.

**Converting between the two forms:**

| Direction | Formula |
|---|---|
| polar → rectangular | $a=c\cos\theta,\quad b=c\sin\theta$ |
| rectangular → polar | $c=\sqrt{a^2+b^2},\quad \theta=\tan^{-1}\!\left(\dfrac{b}{a}\right)$, then fix the quadrant |

> **Warning:** **The quadrant trap.** The calculator’s $\tan^{-1}$ only returns angles between $-90^\circ$ and $90^\circ$. Look at the signs of $a$ and $b$ first. If $a<0$ (left half of the plane), **add $180^\circ$** to what the calculator gives.

**Arithmetic: pick the form that makes the operation easy.**

| Operation | Use | Rule |
|---|---|---|
| $z_1\pm z_2$ | rectangular | add (subtract) real parts and imaginary parts separately |
| $z_1z_2$ | polar | multiply magnitudes, **add** angles: $c_1c_2\angle(\theta_1+\theta_2)$ |
| $z_1/z_2$ | polar | divide magnitudes, **subtract** angles: $\frac{c_1}{c_2}\angle(\theta_1-\theta_2)$ |
| $z_1/z_2$ | rectangular | multiply top and bottom by the **conjugate** of the bottom: $(a+jb)^*=a-jb$ |
| $z^k$ | polar | $c^k\angle k\theta$ (de Moivre) |

The conjugate works because $(a+jb)(a-jb)=a^2+b^2$, a real number. Powers of $j$ repeat every four: $j^2=-1$, $j^3=-j$, $j^4=1$, and $\dfrac1j=-j$.

**Roots: a $k$-th root question always has $k$ answers.** Write $z$ in polar form, then:

$$\begin{gathered}z^{1/k}=c^{1/k}\angle\dfrac{\theta+360^\circ\ell}{k}, \\ \ell=0,1,\dots,k-1\end{gathered}$$

- all $k$ roots have the **same magnitude** $c^{1/k}$;
- the first is at angle $\theta/k$;
- the rest follow, each $360^\circ/k$ further round the circle.

```graph
title "Drag $z$, change $k$: the $k$ roots sit evenly on one circle"
x -3 3 label="Re"
y -3 3 label="Im"
equal
drag Z 0 2.5 label="$z$" color=1
slider k 2 6 3 step=1 label="$k$"
let c "hypot(Z_x,Z_y)"
let th "atan2(Z_y,Z_x)"
let r "c^(1/k)"
arrow "Z_x" "Z_y" color=1
circle "0" "0" "r" color=0 dash
point "r*cos(th/k)" "r*sin(th/k)" label="the $k$ roots of $z$" color=2
point "r*cos((th+2*pi)/k)" "r*sin((th+2*pi)/k)" color=2
point "if(k>2, r*cos((th+4*pi)/k), 99)" "if(k>2, r*sin((th+4*pi)/k), 99)" color=2
point "if(k>3, r*cos((th+6*pi)/k), 99)" "if(k>3, r*sin((th+6*pi)/k), 99)" color=2
point "if(k>4, r*cos((th+8*pi)/k), 99)" "if(k>4, r*sin((th+8*pi)/k), 99)" color=2
point "if(k>5, r*cos((th+10*pi)/k), 99)" "if(k>5, r*sin((th+10*pi)/k), 99)" color=2
readout "$|z|$" "c"
readout "$\angle z$" "deg(th)" unit="°"
readout "root magnitude" "r"
caption "Start: $z=2.5\angle90^\circ$, $k=3$. The roots have magnitude $2.5^{1/3}$; the first is at $90^\circ/3=30^\circ$, the others $120^\circ$ apart."
```

> **Info:** **Bonus (skip-safe): why multiplying adds angles.** In polar form $z_1z_2=c_1e^{j\theta_1}\,c_2e^{j\theta_2}=c_1c_2\,e^{j(\theta_1+\theta_2)}$: the exponent rule $e^Ae^B=e^{A+B}$ adds the angles. Euler’s identity $e^{j\theta}=\cos\theta+j\sin\theta$ connects the two forms. The lecture uses it to get trig identities for free: expand $e^{jA}e^{jB}=e^{j(A+B)}$ and compare real parts to get $\cos(A+B)=\cos A\cos B-\sin A\sin B$.

> **Tip:** **Casio 991 check:** complex mode does $+,-,\times,\div$ and can show the answer as $r\angle\theta$. Use it to check, but write the steps: the marks are for the working.

**Example: Example 1 · W1 · All four fourth roots · lecture Example 1.2**

Find the fourth roots of $z=81e^{j60^\circ}$.

1. **Type:** roots ($k=4$). The number is already polar: $c=81$, $\theta=60^\circ$.
2. **Method:** magnitude $81^{1/4}=3$; first angle $60^\circ/4=15^\circ$; spacing $360^\circ/4=90^\circ$.

   $$\begin{gathered}z^{1/4}=3\angle(15^\circ+90^\circ\ell), \\ \ell=0,1,2,3\end{gathered}$$

**Answer:** $3\angle15^\circ,\ 3\angle105^\circ,\ 3\angle195^\circ,\ 3\angle285^\circ$.

**Problem: Problem 1 · W1 · Convert, watching the quadrant** (introductory)

Write (a) $-3+j4$ and (b) $-3-j4$ in polar form.

<details><summary>Solution</summary>

1. **Type:** rectangular → polar. Both have $a<0$: left half, so the $180^\circ$ fix applies.
2. Magnitude (same for both).

   $$c=\sqrt{(-3)^2+4^2}=5$$
3. (a) The calculator gives $\tan^{-1}(4/-3)=-53.13^\circ$. The point is in quadrant II, so add $180^\circ$.

   $$\theta=126.87^\circ$$
4. (b) The calculator gives $\tan^{-1}(-4/-3)=53.13^\circ$. The point is in quadrant III, so add $180^\circ$.

   $$\theta=233.13^\circ\ \ (=-126.87^\circ)$$

**Answer:** (a) $5\angle126.87^\circ$. (b) $5\angle233.13^\circ$, the same as $5\angle-126.87^\circ$.

</details>

**Problem: Problem 2 · W1 · Divide in rectangular form · lecture Example 1.1** (introductory)

Compute $\dfrac{80+j18}{8+j10}$. Give the answer in rectangular and polar form.

<details><summary>Solution</summary>

1. **Type:** division of two rectangular numbers: multiply top and bottom by the conjugate $8-j10$.

   $$\dfrac{(80+j18)(8-j10)}{(8+j10)(8-j10)}$$
2. Bottom: $8^2+10^2=164$. Top: expand, using $j^2=-1$.

   $$(640+180)+j(144-800)=820-j656$$
3. Divide both parts by 164.

   $$5-j4$$
4. Polar: $a>0$, $b<0$, quadrant IV, so the calculator angle is already right.

   $$\sqrt{41}\angle-38.66^\circ$$

**Answer:** $5-j4=\sqrt{41}\angle-38.66^\circ\approx6.40\angle-38.66^\circ$.

</details>

**Problem: Problem 3 · W1 · A high power** (intermediate)

Compute $(1+j)^8$.

<details><summary>Solution</summary>

1. **Type:** power. Go polar first: $c=\sqrt2$, $\theta=45^\circ$.

   $$1+j=\sqrt2\angle45^\circ$$
2. de Moivre: raise the magnitude to the 8th, multiply the angle by 8.

   $$(\sqrt2)^8\angle360^\circ=16\angle0^\circ$$

**Answer:** $(1+j)^8=16$.

</details>

**Problem: Problem 4 · W1 · Cube roots of a negative number** (intermediate)

Find all three cube roots of $-8$, in polar and rectangular form.

<details><summary>Solution</summary>

1. **Type:** roots ($k=3$). Polar first: $-8$ sits on the negative real axis.

   $$-8=8\angle180^\circ$$
2. Magnitude $8^{1/3}=2$; first angle $180^\circ/3=60^\circ$; spacing $120^\circ$.

   $$2\angle60^\circ,\quad 2\angle180^\circ,\quad 2\angle300^\circ$$
3. Rectangular: $a=2\cos\theta$, $b=2\sin\theta$.

   $$1+j\sqrt3,\quad -2,\quad 1-j\sqrt3$$

**Answer:** $2\angle60^\circ=1+j\sqrt3$, $2\angle180^\circ=-2$, $2\angle300^\circ=1-j\sqrt3$. The real root $-2$ is only one of three.

</details>

**Problem: Problem 5 · W1 + W5 · The complex roots of a quadratic** (intermediate)

Solve $s^2+4s+13=0$. (This is exactly the step you meet in [B5](#b5).)

<details><summary>Solution</summary>

1. **Type:** quadratic with $b^2-4ac<0$: the roots are complex.

   $$s=\dfrac{-4\pm\sqrt{16-52}}{2}=\dfrac{-4\pm\sqrt{-36}}{2}$$
2. $\sqrt{-36}=\sqrt{36}\,\sqrt{-1}=j6$.

   $$s=\dfrac{-4\pm j6}{2}$$

**Answer:** $s=-2\pm j3$: a conjugate pair (same real part, opposite imaginary parts).

</details>

## Topic B: Find the general solution

[Week 2 · Topic 1](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/08d203f6-a2b5-41b9-adfd-a14e22fb03d8#68929800-f011-4be7-a85a-29543465ed52) [Week 2 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/08d203f6-a2b5-41b9-adfd-a14e22fb03d8#49e5b3a7-1038-4f16-a4cc-2170fbbd61dc)

This is the core of the midterm: you are given an ODE (ordinary differential equation) and must find $y(t)$. There are seven methods, B1–B7. Which one works depends only on what the equation looks like, so the first move is always to **name the equation**.

**Step 1: name it.** Ask these five questions:

| Label | Ask | Yes | No |
|---|---|---|---|
| **Order** | What is the highest derivative? | $y^{\prime\prime}+y=0$: 2nd order | — |
| **Linear** | Do $y,y^{\prime},y^{\prime\prime}$ appear only to the first power, never multiplied together or inside a function? ($t$ may appear anywhere.) | $t^3y^{\prime\prime}+e^ty^{\prime}+y=0$ | $yy^{\prime}=t$, $\ y^{\prime}=\sin y$, $\ y^{\prime}=y^2$ |
| **Homogeneous** (linear only) | With every $y$-term on the left, is the right side $0$? | $y^{\prime\prime}+4y=0$ | $y^{\prime\prime}+4y=8$ |
| **Constant coefficients** | Are the numbers in front of $y,y^{\prime},y^{\prime\prime}$ constants? | $y^{\prime\prime}+3y^{\prime}+2y=0$ | $ty^{\prime\prime}+y=0$ |
| **Autonomous** | Is $t$ missing from the equation completely? | $y^{\prime}=y(1-y)$ | $y^{\prime}=t-y$ |

**Step 2: pick the method.**

| If the equation is… | Method | Go to |
|---|---|---|
| 1st order, $\dfrac{dy}{dt}=g(t)\,h(y)$ | separate the variables | [B1](#b1) |
| 1st order, linear: $y^{\prime}+a(t)\,y=f(t)$ | integrating factor | [B2](#b2) |
| $M\,dt+N\,dy=0$ with $\dfrac{\partial M}{\partial y}=\dfrac{\partial N}{\partial t}$ | exact equation | [B3](#b3) |
| $M\,dt+N\,dy=0$, but the test fails | integrating factor that makes it exact | [B4](#b4) |
| $ay^{\prime\prime}+by^{\prime}+cy=0$, constants $a,b,c$ | characteristic equation | [B5](#b5) |
| $ay^{\prime\prime}+by^{\prime}+cy=g(t)$ | undetermined coefficients | [B6](#b6) |
| 2nd order, $t$ in the coefficients, one solution $y_1$ given | reduction of order | [B7](#b7) |

**Step 3: fix the constants.** Every method ends with a **general solution**: a formula with arbitrary constants.

- 1st order: one constant, $C$. One condition, like $y(1)=2$, fixes it.
- 2nd order: two constants, $c_1,c_2$. Two conditions fix them: usually $y(0)$ and $y^{\prime}(0)$.
- A problem with a condition is an **initial value problem** (IVP). Substitute the condition into the general solution and solve for the constant.

**Checking a solution** (a Week 2 question type): substitute $y$ and its derivatives into the ODE. It is a solution if the two sides match for **every** $t$. For an IVP, also check the starting value.

Example: $y=e^{-2t}$ and $y^{\prime}+2y=0$: $\;-2e^{-2t}+2e^{-2t}=0$ ✓.

**Problem: Problem 6 · W2 · Name it, then route it · lecture Example 2.1 and others** (introductory)

For each equation, give its order, and say whether it is linear, homogeneous, constant-coefficient and autonomous. Then name the subtopic (B1–B7) that solves it.

(a) $t^3y^{\prime\prime}+e^ty^{\prime}+y=0$

(b) $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$

(c) $y^{\prime\prime}+2y^{\prime}+5y=10$

(d) $\dfrac{di}{dt}+5i=50$

(e) $(t-y)\,dt-(t+y)\,dy=0$

<details><summary>Solution</summary>

1. (a) Highest derivative $y^{\prime\prime}$; $y$ terms are first power with $t$-only coefficients; right side 0; coefficients $t^3,e^t$ vary; $t$ appears. 2nd order, linear, homogeneous, **not** constant-coefficient, not autonomous → [B7](#b7) (once one solution is given).
2. (b) $y^2$ is not first power, so nonlinear; $t$ appears. It splits as $\frac{1}{t^3}\cdot y^2$ → [B1](#b1).
3. (c) 2nd order, linear, right side $10\neq0$ so **non**homogeneous, constant coefficients, autonomous → [B6](#b6).
4. (d) 1st order, linear, nonhomogeneous, constant coefficients, autonomous → [B2](#b2) (it also separates: $\frac{di}{50-5i}=dt$).
5. (e) As $y^{\prime}=\frac{t-y}{t+y}$: $y$ sits in a denominator, so nonlinear. In $M\,dt+N\,dy$ form, test exactness → [B3](#b3).

**Answer:** (a) 2nd, linear, homogeneous, variable coefficients → B7. (b) 1st, nonlinear → B1. (c) 2nd, linear, nonhomogeneous, constant → B6. (d) 1st, linear, constant → B2. (e) 1st, nonlinear → B3.

</details>

**Problem: Problem 7 · W2 · Check, then pick the member that fits** (introductory)

Which of $y=t^2$, $\;y=t^2+1$, $\;y=5t^2$ solve $ty^{\prime}-2y=0$? Which one also satisfies $y(1)=5$?

<details><summary>Solution</summary>

1. **Type:** checking solutions: substitute each one.
2. $y=t^2$: $y^{\prime}=2t$.

   $$t(2t)-2t^2=0\ \checkmark$$
3. $y=t^2+1$: $y^{\prime}=2t$.

   $$t(2t)-2(t^2+1)=-2\neq0\ \times$$
4. $y=5t^2$: $y^{\prime}=10t$.

   $$t(10t)-2(5t^2)=0\ \checkmark$$
5. **Condition:** at $t=1$, $t^2=1$ and $5t^2=5$.

**Answer:** $t^2$ and $5t^2$ are solutions (both are $Ct^2$); $t^2+1$ is not. Only $y=5t^2$ satisfies $y(1)=5$.

</details>

### B1 · Separable equations

[Week 3 · Topic 1](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/3d1ae4a9-687d-4654-873d-be3439faea2f#c40cdedd-01db-45b4-9498-4c4929ba8f49)

**The simplest case.** If you can move every $y$ to one side and every $t$ to the other, you can integrate each side on its own.

A first-order ODE is **separable** when it can be written as:

$$\dfrac{dy}{dt}=g(t)\,h(y)$$

- $g(t)$ = a part with only $t$ in it
- $h(y)$ = a part with only $y$ in it

Example: $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$ has $g=\dfrac{1}{t^3}$ and $h=y^2$. Not separable: $\dfrac{dy}{dt}=t+y$, because a **sum** can’t be split into a product (that one goes to [B2](#b2)).

An equation already written as $M(t)\,dt+N(y)\,dy=0$, with only $t$ in $M$ and only $y$ in $N$, is separated already.

**Method:**

1. **Separate:** divide by $h(y)$ and multiply by $dt$:  $\dfrac{dy}{h(y)}=g(t)\,dt$.
2. **Integrate** both sides. Write one constant $C$, on the $t$ side.
3. **Condition:** substitute the given point to find $C$.
4. **Solve for $y$** if you can. If you can’t, the implicit answer (like $y^2+3=6(t^2+1)$) is a full answer.

**Calculus you need here:**

| Integral | Result | Note |
|---|---|---|
| $\int t^n\,dt$ | $\dfrac{t^{n+1}}{n+1}$ | any $n\neq-1$, e.g. $\int t^{-3}dt=-\dfrac{1}{2t^2}$ |
| $\int \dfrac1y\,dy$ | $\ln|y|$ | the $n=-1$ case |
| $\int \dfrac{f^{\prime}(t)}{f(t)}\,dt$ | $\ln|f(t)|$ | spot “top = derivative of bottom”: $\int\dfrac{t}{t^2+1}dt=\dfrac12\ln(t^2+1)$ |
| $\int e^{at}\,dt$ | $\dfrac{1}{a}e^{at}$ |  |
| undo $\ln$ | $e^{\ln A}=A$ | $e^{C}$ is just another constant; $\ln A+\ln B=\ln(AB)$ |

> **Warning:** **Dividing by $h(y)$ hides constant solutions.** If $h(y_0)=0$ for a number $y_0$, then $y=y_0$ is a solution too. For $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$, $y=0$ is a solution that the separated formula misses.

> **Info:** **Bonus (skip-safe): why separating is allowed.** Divide by $h$: $\dfrac{1}{h(y)}\dfrac{dy}{dt}=g(t)$. Integrate both sides with respect to $t$. By the chain rule, $\int\dfrac{1}{h(y)}\dfrac{dy}{dt}\,dt=\int\dfrac{1}{h(y)}\,dy$. Writing “$dy$” and “$dt$” as separate pieces is shorthand for exactly this.

**Example: Example 2 · W3 · Separate after factoring · lecture Example 3.3**

Solve $\dfrac{dy}{dt}=\dfrac{3t+ty^2}{y+t^2y}$, $\;y(1)=3$.

1. **Type:** factor top and bottom; it becomes $g(t)\,h(y)$, so separable.

   $$\dfrac{dy}{dt}=\dfrac{t(3+y^2)}{y(1+t^2)}$$
2. **Separate:** $y$’s left, $t$’s right.

   $$\dfrac{y}{3+y^2}\,dy=\dfrac{t}{1+t^2}\,dt$$
3. **Integrate:** both are “top = half the derivative of bottom”.

   $$\tfrac12\ln(3+y^2)=\tfrac12\ln(1+t^2)+c$$
4. Multiply by 2 and exponentiate; $e^{2c}$ becomes a new constant $C_1$.

   $$3+y^2=C_1(1+t^2)$$
5. **Condition** $y(1)=3$: $\;3+9=C_1(2)$.

   $$C_1=6$$
6. Solve for $y$; take the $+$ root because $y(1)=3>0$.

   $$y^2=6t^2+3$$

**Answer:** $y^2+3=6(t^2+1)$, i.e. $y=\sqrt{6t^2+3}$.

**Problem: Problem 8 · W3 · Separate and use a starting value · Pre-tutorial 3(a)** (introductory)

Solve $\dfrac{dy}{dt}=-\dfrac{t}{y}$, $\;y=2$ when $t=1$.

<details><summary>Solution</summary>

1. **Type:** $-\dfrac{t}{y}=(-t)\cdot\dfrac1y$: separable.
2. **Separate:** multiply by $y\,dt$.

   $$y\,dy=-t\,dt$$
3. **Integrate.**

   $$\dfrac{y^2}{2}=-\dfrac{t^2}{2}+C$$
4. **Condition:** $\frac{4}{2}=-\frac12+C$, so $C=\frac52$. Multiply by 2.

   $$t^2+y^2=5$$
5. Solve for $y$, keeping the $+$ root since $y(1)=2>0$.

   $$y=\sqrt{5-t^2}$$

**Answer:** $y=\sqrt{5-t^2}$ (a circle of radius $\sqrt5$, upper half), valid for $-\sqrt5<t<\sqrt5$.

</details>

**Problem: Problem 9 · W3 · A general solution with a power · lecture Example 3.2** (introductory)

Find the general solution of $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$.

<details><summary>Solution</summary>

1. **Type:** separable, $g=t^{-3}$, $h=y^2$.

   $$y^{-2}\,dy=t^{-3}\,dt$$
2. **Integrate** with the power rule ($n=-2$ and $n=-3$).

   $$-y^{-1}=-\tfrac12t^{-2}+C$$
3. Multiply by $-1$ and flip (rename $-C$ as $C$).

   $$\dfrac1y=\dfrac{1}{2t^2}+C\quad\Rightarrow\quad y=\dfrac{2t^2}{1+2Ct^2}$$

**Answer:** $\dfrac1y=\dfrac{1}{2t^2}+C$, i.e. $y=\dfrac{2t^2}{1+2Ct^2}$. Also $y=0$ (the constant solution lost by dividing by $y^2$).

</details>

**Problem: Problem 10 · W3 · An exponential of y** (intermediate)

Solve $\dfrac{dy}{dt}=2t\,e^{-y}$, $\;y(0)=0$.

<details><summary>Solution</summary>

1. **Type:** $2t\cdot e^{-y}$: separable. Dividing by $e^{-y}$ is multiplying by $e^{y}$.

   $$e^{y}\,dy=2t\,dt$$
2. **Integrate.**

   $$e^{y}=t^2+C$$
3. **Condition:** $e^0=0+C$, so $C=1$.

   $$e^{y}=t^2+1$$
4. Take $\ln$ of both sides.

   $$y=\ln(t^2+1)$$

**Answer:** $y=\ln(t^2+1)$.

</details>

**Problem: Problem 11 · W3 · Differential form · Pre-tutorial 3(b)** (intermediate)

Solve $3t(y^2+1)\,dt+y(t^2+2)\,dy=0$.

<details><summary>Solution</summary>

1. **Type:** each term is (t-part)(y-part), so dividing by $(y^2+1)(t^2+2)$ separates it.

   $$\dfrac{3t}{t^2+2}\,dt+\dfrac{y}{y^2+1}\,dy=0$$
2. **Integrate:** both are “top = derivative of bottom” (times $\frac32$ and $\frac12$).

   $$\tfrac32\ln(t^2+2)+\tfrac12\ln(y^2+1)=c$$
3. Multiply by 2, then combine the logs: $3\ln A+\ln B=\ln(A^3B)$.

   $$\ln\!\big[(t^2+2)^3(y^2+1)\big]=2c$$
4. Exponentiate.

   $$(t^2+2)^3(y^2+1)=C$$

**Answer:** $(t^2+2)^3(y^2+1)=C$ (implicit; $C>0$).

</details>

**Problem: Problem 12 · W3 · Collect before separating · lecture Example 3.4** (advanced)

Solve $y\,dt+(t^3y^2+t^3)\,dy=0$.

<details><summary>Solution</summary>

1. **Type:** factor $t^3$ out of the $dy$ term: $y\,dt+t^3(y^2+1)\,dy=0$. Dividing by $t^3y$ separates it.

   $$t^{-3}\,dt+\dfrac{y^2+1}{y}\,dy=0$$
2. Split the fraction: $\dfrac{y^2+1}{y}=y+\dfrac1y$.

   $$\int t^{-3}\,dt+\int\left(y+\dfrac1y\right)dy=C$$
3. **Integrate.**

   $$-\dfrac{1}{2t^2}+\dfrac{y^2}{2}+\ln|y|=C$$
4. Multiply by 2 (rename $2C$ as $C_1$).

   $$y^2+2\ln|y|-t^{-2}=C_1$$

**Answer:** $y^2+2\ln|y|-t^{-2}=C_1$ (implicit), plus the constant solution $y=0$.

</details>

### B2 · Linear equations: the integrating factor

[Week 3 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/3d1ae4a9-687d-4654-873d-be3439faea2f#a43fc96e-8dc5-4a1e-bfdf-bf1acf01f98b)

**What if you can’t separate the variables?** $\dfrac{dy}{dt}=t-y$ won’t split into ($t$-part)×($y$-part), so [B1](#b1) fails. But if the equation is **linear**, an integrating factor solves it every time.

First-order linear equations can be written as:

$$\dfrac{dy}{dt}+a(t)\,y=f(t)$$

- $a(t)$ = the coefficient of $y$: everything multiplying $y$, **sign included**
- $f(t)$ = the forcing: everything left over, with no $y$ in it

Examples:

- $y^{\prime}=t-y$ → move $y$ left: $y^{\prime}+y=t$. So $a(t)=1$, $f(t)=t$.
- $ty^{\prime}+2y=t^2$ → divide by $t$: $y^{\prime}+\frac2t\,y=t$. So $a(t)=\frac2t$, $f(t)=t$.
- $y^{\prime}=(8t+3)y$ → $y^{\prime}-(8t+3)y=0$. So $a(t)=-(8t+3)$, $f(t)=0$.

> **Warning:** Get $y^{\prime}$ **alone** first (coefficient 1). Read $a(t)$ only after dividing: in $ty^{\prime}+2y=t^2$, $a(t)$ is $\frac2t$, not $2$.

**The integrating factor.** An integrating factor is a special function $\mu(t)$ that we multiply the entire equation by, to turn its left side into **one derivative**. The formula is:

$$\mu(t)=e^{\int a(t)\,dt}$$

After multiplying by $\mu$, the left side is exactly $(\mu y)^{\prime}$, so the equation becomes:

$$\dfrac{d}{dt}\big(\mu\,y\big)=\mu\,f$$

Integrate both sides:

$$\mu\,y=\int\mu\,f\,dt+C$$

**Method:**

1. **Standard form:** get $y^{\prime}$ alone; read $a(t)$ and $f(t)$.
2. **Integrating factor:** $\mu=e^{\int a\,dt}$. Leave out the $+C$ in this integral.
3. **Rewrite:** $(\mu y)^{\prime}=\mu f$.
4. **Integrate:** $\mu y=\int\mu f\,dt+C$. This is where the constant goes; don’t forget it.
5. **Divide by $\mu$**, then use the condition to find $C$.

```steps
title "The method on y′ + 2y = 4"
$$ y'+2y=4 $$
Standard form already: $a=2$, $f=4$.
$$ \mu=e^{\int2\,dt}=\hl{e^{2t}} $$
Integrating factor.
$$ \hl{e^{2t}}y'+\hl{2e^{2t}}y=\hl{4e^{2t}} $$
Multiply every term by $\mu$.
$$ \hl{\big(e^{2t}y\big)^{\prime}}=4e^{2t} $$
The left side is one derivative (product rule backwards).
$$ e^{2t}y=2e^{2t}+\hl{C} $$
Integrate both sides: $\int4e^{2t}dt=2e^{2t}$.
$$ y=2+Ce^{-2t} $$
Divide by $e^{2t}$.
```

**Calculus you need here:**

| Expression | Result | Note |
|---|---|---|
| $e^{\int k\,dt}$ | $e^{kt}$ | constant $a(t)=k$ |
| $e^{\int\frac{k}{t}dt}$ | $e^{k\ln t}=t^k$ | e.g. $a=\frac2t$ gives $\mu=t^2$; $a=-\frac1t$ gives $\mu=\frac1t$ |
| $\int(2t+5)^5\,dt$ | $\dfrac{(2t+5)^6}{12}$ | substitution $u=2t+5$, $du=2\,dt$ |
| $\int t\,e^{t}\,dt$ | $(t-1)\,e^{t}$ | integration by parts; check by differentiating |
| $\int t\,e^{t^2}dt$ | $\tfrac12e^{t^2}$ | substitution $u=t^2$ |

> **Tip:** **Shortcut for constant $a=k$ and constant $f=F$:** $\;y=\dfrac{F}{k}+Ce^{-kt}$. Every RC and RL circuit equation has this shape (see [D1](#d1)).

> **Info:** **Bonus (skip-safe): why does the integrating factor work?** Recall the **product rule** from calculus: $(\mu y)^{\prime}=\mu y^{\prime}+\mu^{\prime} y$. With $\mu=e^{\int a\,dt}$, the chain rule gives $\mu^{\prime}=a\,\mu$. So
> 
> $$
> (\mu y)^{\prime}=\mu y^{\prime}+a\mu y=\mu\,(y^{\prime}+ay)
> $$
> 
> which is exactly $\mu$ times the left side of the equation. Multiplying by $\mu$ turns “$y^{\prime}+ay$” into a single derivative you can integrate.

> **Info:** **Both separable and linear?** For example $y^{\prime}=(8t+3)y$, or any equation with constant $a$ and $f$. Then either method works: separating is usually faster.

**Example: Example 3 · W3 · A coefficient that varies with t · lecture Example 3.1**

Solve $\dfrac{dy}{dt}+\dfrac{10\,y}{2t+5}=10$, $\;y(0)=0$.

1. **Type:** linear, $y^{\prime}$ already alone. $a(t)=\dfrac{10}{2t+5}$, $f(t)=10$.
2. **Integrating factor:** $\int\frac{10}{2t+5}dt=5\ln(2t+5)$, and $e^{5\ln(2t+5)}=(2t+5)^5$.

   $$\mu=(2t+5)^5$$
3. **Rewrite:** $(\mu y)^{\prime}=\mu f$.

   $$\dfrac{d}{dt}\big[(2t+5)^5y\big]=10(2t+5)^5$$
4. **Integrate** with $u=2t+5$, $du=2\,dt$: $\;10\int u^5\frac{du}{2}=\frac56u^6$.

   $$(2t+5)^5y=\tfrac56(2t+5)^6+C$$
5. **Condition** $y(0)=0$: $\;0=\frac56\cdot5^6+C$.

   $$C=-\dfrac{5^7}{6}$$
6. **Divide** by $(2t+5)^5$.

   $$y=\tfrac56(2t+5)-\dfrac{5^7}{6(2t+5)^5}$$

**Answer:** $y=\dfrac56(2t+5)-\dfrac{5^7}{6(2t+5)^5}$.

**Problem: Problem 13 · W3 · The lecture’s RL equation · lecture §1.1** (introductory)

Solve $\dfrac{di}{dt}+5i=50$, $\;i(0)=0$ (the series RL circuit of the Week 3 lecture, $i$ in amperes).

<details><summary>Solution</summary>

1. **Type:** linear with constant $a=5$, $f=50$.
2. **Integrating factor** and rewrite.

   $$\mu=e^{5t},\qquad \big(e^{5t}i\big)^{\prime}=50e^{5t}$$
3. **Integrate:** $\int50e^{5t}dt=10e^{5t}$.

   $$e^{5t}i=10e^{5t}+C$$
4. **Condition:** $0=10+C$, so $C=-10$. Divide by $e^{5t}$.

   $$i=10-10e^{-5t}$$

**Answer:** $i(t)=10(1-e^{-5t})\,\mathrm{A}$. It rises from 0 towards 10 A (the shortcut: $F/k=50/5=10$).

</details>

**Problem: Problem 14 · W3 · Linear and separable: solve it both ways · Pre-tutorial 3(c)** (introductory)

Find the general solution of $\dfrac{dy}{dt}=8ty+3y$ with an integrating factor, then check it by separating.

<details><summary>Solution</summary>

1. **Type:** linear. Standard form: $y^{\prime}-(8t+3)y=0$, so $a=-(8t+3)$, $f=0$.
2. **Integrating factor:** $\int-(8t+3)\,dt=-4t^2-3t$.

   $$\mu=e^{-4t^2-3t}$$
3. **Rewrite and integrate:** $f=0$, so the right side integrates to just $C$.

   $$\big(\mu y\big)^{\prime}=0\quad\Rightarrow\quad e^{-4t^2-3t}y=C$$
4. **Divide** by $\mu$.

   $$y=Ce^{4t^2+3t}$$
5. **Check by separating:** $\dfrac{dy}{y}=(8t+3)\,dt$ gives $\ln|y|=4t^2+3t+c$, the same family.

**Answer:** $y=Ce^{4t^2+3t}$.

</details>

**Problem: Problem 15 · W3 · An integral that needs parts** (intermediate)

Solve $y^{\prime}+y=t$, $\;y(0)=0$.

<details><summary>Solution</summary>

1. **Type:** linear, $a=1$, $f=t$. Not separable ($t-y$ is a sum).
2. **Integrating factor** and rewrite.

   $$\mu=e^{t},\qquad\big(e^{t}y\big)^{\prime}=te^{t}$$
3. **Integrate** with the calculus table: $\int te^tdt=(t-1)e^t$.

   $$e^{t}y=(t-1)e^{t}+C$$
4. Divide by $e^t$.

   $$y=t-1+Ce^{-t}$$
5. **Condition:** $0=-1+C$, so $C=1$.

   $$y=t-1+e^{-t}$$

**Answer:** $y=t-1+e^{-t}$.

</details>

**Problem: Problem 16 · W3 · Divide first, then a power of t** (intermediate)

Solve $t\,y^{\prime}+2y=t^2$, $\;y(1)=0$, for $t>0$.

<details><summary>Solution</summary>

1. **Type:** linear. Divide by $t$ to get $y^{\prime}$ alone.

   $$y'+\dfrac{2}{t}\,y=t$$
2. **Integrating factor:** $e^{\int\frac2t dt}=e^{2\ln t}=t^2$.

   $$\big(t^2y\big)^{\prime}=t^3$$
3. **Integrate.**

   $$t^2y=\dfrac{t^4}{4}+C$$
4. **Condition:** $0=\frac14+C$, so $C=-\frac14$. Divide by $t^2$.

   $$y=\dfrac{t^2}{4}-\dfrac{1}{4t^2}$$

**Answer:** $y=\dfrac{t^2}{4}-\dfrac{1}{4t^2}$.

</details>

**Problem: Problem 17 · W3 · An integrating factor with t²** (advanced)

Solve $y^{\prime}+2t\,y=t$, $\;y(0)=1$.

<details><summary>Solution</summary>

1. **Type:** linear, $a=2t$, $f=t$.
2. **Integrating factor:** $\int2t\,dt=t^2$.

   $$\mu=e^{t^2},\qquad\big(e^{t^2}y\big)^{\prime}=te^{t^2}$$
3. **Integrate** with $u=t^2$: $\int te^{t^2}dt=\frac12e^{t^2}$.

   $$e^{t^2}y=\tfrac12e^{t^2}+C$$
4. Divide by $e^{t^2}$.

   $$y=\tfrac12+Ce^{-t^2}$$
5. **Condition:** $1=\frac12+C$, so $C=\frac12$.

   $$y=\tfrac12+\tfrac12e^{-t^2}$$

**Answer:** $y=\dfrac12\big(1+e^{-t^2}\big)$. (It is also separable: $y^{\prime}=t(1-2y)$.)

</details>

### B3 · Exact equations

[Week 4 · Topic 1](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/ce2fa611-8b68-46a9-b6ca-653ae9c59aee#c9f71086-78d7-4bc3-a405-e0c6375fb6ca) [Week 4 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/ce2fa611-8b68-46a9-b6ca-653ae9c59aee#954310f2-d355-42ff-bd75-4e6b1d00f02d)

**When the equation comes in “$dt$ and $dy$” form.** Some first-order equations are neither separable nor linear, but their left side is the change of one hidden function $U(t,y)$. Then the solution is simply $U(t,y)=C$.

Write the equation with everything on the left:

$$M(t,y)\,dt+N(t,y)\,dy=0$$

- $M$ = everything multiplying $dt$, **sign included**
- $N$ = everything multiplying $dy$, **sign included**

Examples:

- $3t\,dt+4y\,dy=0$: $\;M=3t$, $N=4y$.
- $y^{\prime}=\dfrac{t-y}{t+y}$ → cross-multiply: $(t+y)\,dy=(t-y)\,dt$ → move all left: $(t-y)\,dt-(t+y)\,dy=0$. So $M=t-y$, $N=-(t+y)$.
- $2ty\,y^{\prime}=t^2-y^2$ → $(t^2-y^2)\,dt-2ty\,dy=0$. So $M=t^2-y^2$, $N=-2ty$.

> **Warning:** Moving the $dy$ term across the $=$ sign flips its sign. In $y^{\prime}=\frac{t-y}{t+y}$, $N$ is $-(t+y)$, not $t+y$. One wrong sign makes the test fail.

**The exactness test.** The equation is **exact** when the cross derivatives match:

$$\dfrac{\partial M}{\partial y}=\dfrac{\partial N}{\partial t}$$

Then there is a function $U(t,y)$ with

$$\dfrac{\partial U}{\partial t}=M,\quad \dfrac{\partial U}{\partial y}=N$$

and the general solution is

$$U(t,y)=C$$

**Method:**

1. **Rewrite** as $M\,dt+N\,dy=0$ (everything on the left).
2. **Test:** is $M_y=N_t$? ($M_y$ means $\partial M/\partial y$.) If not, go to [B4](#b4).
3. **Integrate $M$ in $t$:** $U=\int M\,dt+f(y)$. The “constant” is a whole function $f(y)$.
4. **Match $N$:** differentiate that $U$ in $y$, set it equal to $N$, solve for $f^{\prime}(y)$, integrate.
5. **Answer:** $U(t,y)=C$. Use the condition to find $C$.

**Calculus you need here** (partial derivatives: hold the other letter fixed, like a number):

| Expression | Result | Note |
|---|---|---|
| $\dfrac{\partial}{\partial t}(t^2y)$ | $2ty$ | $y$ is a constant multiplier |
| $\dfrac{\partial}{\partial y}(t^2y)$ | $t^2$ | $t^2$ is a constant multiplier |
| $\dfrac{\partial}{\partial y}(t-y)$ | $-1$ | $t$ is a constant: its derivative is 0 |
| $\int(2ty+3t^2)\,dt$ | $t^2y+t^3+f(y)$ | integrate in $t$ with $y$ fixed; anything with only $y$ vanishes under $\partial/\partial t$, so the constant is $f(y)$ |

> **Info:** **Bonus (skip-safe): why the test works, and what the answer means.** If $U$ exists, then $M_y=U_{ty}$ and $N_t=U_{yt}$. Mixed partial derivatives are equal, so $M_y=N_t$ must hold. Along a solution, $dU=U_t\,dt+U_y\,dy=M\,dt+N\,dy=0$: $U$ never changes. So each solution is a **level curve** $U(t,y)=C$ of the surface $z=U(t,y)$.

Slide $C$: the plane cuts the surface along one solution curve (an ellipse), drawn again on the floor.

```graph3d
title "Solutions of $3t\,dt+4y\,dy=0$ are level curves of $3t^2+4y^2$"
x -3 3 label="$t$"
y -3 3 label="$y$"
z 0 30 label="$U$"
view az=-55 el=28
slider C 1 24 12 step=1 label="$C$"
surface "3*x^2+4*y^2" label="$U=3t^2+4y^2$"
plane "C" label="height $C$"
```

**Example: Example 4 · W4 · Test, integrate, match · lecture Example 4.1**

Solve $(2ty+3t^2)\,dt+t^2\,dy=0$.

1. **Type:** $M\,dt+N\,dy=0$ form, with $M=2ty+3t^2$ and $N=t^2$.
2. **Test:** hold $t$ fixed for $M_y$, hold $y$ fixed for $N_t$.

   $$M_y=2t=N_t\quad\checkmark$$
3. **Integrate $M$ in $t$** ($y$ fixed).

   $$U=t^2y+t^3+f(y)$$
4. **Match $N$:** $U_y$ must equal $t^2$.

   $$t^2+f^{\prime}(y)=t^2\quad\Rightarrow\quad f^{\prime}(y)=0$$
5. So $f$ is a plain constant, which joins $C$.

   $$t^2y+t^3=C$$

**Answer:** $t^2y+t^3=C$ (explicitly, $y=\dfrac{C-t^3}{t^2}$).

**Problem: Problem 18 · W4 · Test, then solve · lecture exercise (a)** (introductory)

Test $3t\,dt+4y\,dy=0$ for exactness, and if so, solve.

<details><summary>Solution</summary>

1. **Type:** $M\,dt+N\,dy=0$ with $M=3t$, $N=4y$.
2. **Test:** $M$ has no $y$, $N$ has no $t$.

   $$M_y=0=N_t\quad\checkmark$$
3. **Integrate $M$ in $t$.**

   $$U=\tfrac32t^2+f(y)$$
4. **Match $N$:** $f^{\prime}(y)=4y$, so $f=2y^2$.

   $$U=\tfrac32t^2+2y^2$$
5. **Answer:** $U=C$; multiply by 2 and rename the constant.

   $$3t^2+4y^2=C$$

**Answer:** Exact. $3t^2+4y^2=C$ (ellipses: the graph above). It is also separable.

</details>

**Problem: Problem 19 · W4 · Test before you integrate · lecture exercise (d)** (introductory)

Is $y^{\prime}=\dfrac{t}{t+y}$ exact?

<details><summary>Solution</summary>

1. **Type:** a slope formula: rewrite it in $M\,dt+N\,dy=0$ form first.

   $$t\,dt-(t+y)\,dy=0$$
2. **Read** $M=t$ and $N=-(t+y)$.
3. **Test.**

   $$M_y=0,\qquad N_t=-1$$
4. $0\neq-1$: **not exact**. The next move would be [B4](#b4), but neither of its ratios works here: $\frac{M_y-N_t}{N}=-\frac{1}{t+y}$ has both letters, and $\frac{N_t-M_y}{M}=-\frac1t$ has no $y$. The lecture stops at “not exact”.

**Answer:** Not exact: $M_y=0\neq-1=N_t$.

</details>

**Problem: Problem 20 · W4 · Cross-multiply, then use a condition · lecture exercise (b)** (intermediate)

Solve $y^{\prime}=\dfrac{t-y}{t+y}$, $\;y(0)=1$.

<details><summary>Solution</summary>

1. **Type:** slope formula → cross-multiply and move everything left.

   $$(t-y)\,dt-(t+y)\,dy=0$$
2. **Test:** $M=t-y$, $N=-t-y$.

   $$M_y=-1=N_t\quad\checkmark$$
3. **Integrate $M$ in $t$.**

   $$U=\tfrac12t^2-ty+f(y)$$
4. **Match $N$:** $-t+f^{\prime}(y)=-t-y$, so $f^{\prime}=-y$ and $f=-\frac12y^2$.

   $$\tfrac12t^2-ty-\tfrac12y^2=C$$
5. Multiply by 2 (rename the constant).

   $$t^2-2ty-y^2=C$$
6. **Condition** $y(0)=1$: $\;0-0-1=C$.

   $$C=-1$$

**Answer:** $t^2-2ty-y^2=-1$.

</details>

**Problem: Problem 21 · W4 · The sign trap · lecture exercise (c)** (intermediate)

Solve $2ty\,y^{\prime}=t^2-y^2$.

<details><summary>Solution</summary>

1. **Type:** write $y^{\prime}=\frac{dy}{dt}$, multiply by $dt$ and move the $dy$ term left: it becomes **negative**.

   $$(t^2-y^2)\,dt-2ty\,dy=0$$
2. **Test:** $M=t^2-y^2$, $N=-2ty$.

   $$M_y=-2y=N_t\quad\checkmark$$
3. **Integrate $M$ in $t$.**

   $$U=\tfrac13t^3-ty^2+f(y)$$
4. **Match $N$:** $-2ty+f^{\prime}(y)=-2ty$, so $f^{\prime}=0$.

   $$\tfrac13t^3-ty^2=C$$
5. Multiply by 3 (rename the constant).

   $$t^3-3ty^2=C$$

**Answer:** $t^3-3ty^2=C$. With $+2ty\,dy$ (wrong sign) the test gives $-2y\neq2y$ and fails.

</details>

### B4 · Not exact: make it exact with an integrating factor

[Week 4 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/ce2fa611-8b68-46a9-b6ca-653ae9c59aee#ebb7e8ad-4fda-4034-97dc-a9c048d71335)

**What if the exactness test fails?** Multiply the whole equation by a function $\mu$ (an **integrating factor**) chosen so that the new equation passes the test. Then finish with [B3](#b3).

Start from $M\,dt+N\,dy=0$ with $M_y\neq N_t$, and compute the **mismatch**:

$$M_y-N_t$$

**Theorem 1.** If this ratio depends on $t$ only, call it $f(t)$:

$$\dfrac{M_y-N_t}{N}=f(t)\quad\Rightarrow\quad \mu=e^{\int f(t)\,dt}$$

**Theorem 2.** If this ratio depends on $y$ only, call it $g(y)$:

$$\dfrac{N_t-M_y}{M}=g(y)\quad\Rightarrow\quad \mu=e^{\int g(y)\,dy}$$

**Memory aid:**

- Theorem 1 divides the mismatch by $N$ and must leave only $t$.
- Theorem 2 divides by $M$, with the subtraction **flipped** ($N_t-M_y$), and must leave only $y$.

**Method:**

1. **Test:** $M_y\neq N_t$ (otherwise it is already exact: [B3](#b3)).
2. **Ratios:** compute both. Keep the one that depends on a single letter.
3. **Integrating factor:** $\mu=e^{\int f\,dt}$ or $\mu=e^{\int g\,dy}$ (no $+C$ needed).
4. **Multiply the whole equation** by $\mu$: both $M$ and $N$.
5. **Re-test** (it must pass now), then solve with the [B3](#b3) steps.

**Calculus you need here:**

| Expression | Result | Note |
|---|---|---|
| $e^{\int\frac{k}{y}dy}$ | $e^{k\ln|y|}=|y|^k$ | e.g. $g=\frac2y$ gives $\mu=y^2$; $g=-\frac1y$ gives $\mu=\frac1y$ |
| $e^{\int\frac{k}{t}dt}$ | $t^k$ | e.g. $f=-\frac2t$ gives $\mu=t^{-2}=\frac{1}{t^2}$ |
| $e^{\int k\,dt}$ | $e^{kt}$ | constant ratio |

> **Info:** **Bonus (skip-safe): where Theorem 1 comes from.** Multiply by $\mu(t)$ and ask for the new equation to pass the test: $(\mu M)_y=(\mu N)_t$, i.e. $\mu M_y=\mu^{\prime} N+\mu N_t$. Rearranged:
> 
> $$
> \dfrac{\mu^{\prime}}{\mu}=\dfrac{M_y-N_t}{N}
> $$
> 
> A $\mu$ depending on $t$ alone can only exist if the right side depends on $t$ alone. Then $\ln\mu=\int f\,dt$. Theorem 2 is the same argument with $\mu(y)$.

**Example: Example 5 · W4 · Repair, then finish · lecture exercise (e) and Pre-tutorial 4**

Solve $y\,dt+(3+3t-y)\,dy=0$.

1. **Type:** $M\,dt+N\,dy=0$ with $M=y$, $N=3+3t-y$. **Test:** $M_y=1$, $N_t=3$: not exact.
2. **Ratios:** Theorem 1 gives $\frac{1-3}{3+3t-y}$, which has both letters. Theorem 2 gives $y$ only.

   $$\dfrac{N_t-M_y}{M}=\dfrac{3-1}{y}=\dfrac2y$$
3. **Integrating factor:** $e^{\int\frac2y dy}=e^{2\ln|y|}$.

   $$\mu=y^2$$
4. **Multiply the whole equation** by $y^2$.

   $$y^3\,dt+(3y^2+3ty^2-y^3)\,dy=0$$
5. **Re-test.**

   $$M_y=3y^2=N_t\quad\checkmark$$
6. **Integrate $M$ in $t$** ($y$ fixed).

   $$U=ty^3+f(y)$$
7. **Match $N$:** $3ty^2+f^{\prime}(y)=3y^2+3ty^2-y^3$, so $f^{\prime}=3y^2-y^3$.

   $$f(y)=y^3-\tfrac14y^4$$

**Answer:** $ty^3+y^3-\dfrac{y^4}{4}=C$.

**Problem: Problem 22 · W4 · A factor in t only** (introductory)

Solve $(t^2+y)\,dt-t\,dy=0$ for $t>0$.

<details><summary>Solution</summary>

1. **Type:** $M=t^2+y$, $N=-t$. **Test:** $M_y=1$, $N_t=-1$: not exact.
2. **Ratios:** Theorem 1 leaves only $t$.

   $$\dfrac{M_y-N_t}{N}=\dfrac{1-(-1)}{-t}=-\dfrac2t$$
3. **Integrating factor:** $e^{\int-\frac2t dt}=e^{-2\ln t}$.

   $$\mu=\dfrac{1}{t^2}$$
4. **Multiply the whole equation** by $\frac{1}{t^2}$.

   $$\Big(1+\dfrac{y}{t^2}\Big)dt-\dfrac1t\,dy=0$$
5. **Re-test.**

   $$M_y=\dfrac{1}{t^2}=N_t\quad\checkmark$$
6. **Integrate $M$ in $t$:** $\int\frac{y}{t^2}dt=-\frac yt$.

   $$U=t-\dfrac{y}{t}+f(y)$$
7. **Match $N$:** $-\frac1t+f^{\prime}=-\frac1t$, so $f^{\prime}=0$.

   $$t-\dfrac yt=C$$

**Answer:** $t-\dfrac{y}{t}=C$, i.e. $y=t^2-Ct$. Check with [B2](#b2): the equation is also linear, $y^{\prime}-\frac{y}{t}=t$, and gives the same family.

</details>

**Problem: Problem 23 · W4 · A factor in y only** (intermediate)

Solve $y\,dt+(2t+y^3)\,dy=0$.

<details><summary>Solution</summary>

1. **Type:** $M=y$, $N=2t+y^3$. **Test:** $M_y=1$, $N_t=2$: not exact.
2. **Ratios:** Theorem 1 gives $\frac{-1}{2t+y^3}$ (both letters). Theorem 2:

   $$\dfrac{N_t-M_y}{M}=\dfrac{2-1}{y}=\dfrac1y$$
3. **Integrating factor:** $e^{\int\frac1y dy}=e^{\ln|y|}$.

   $$\mu=y$$
4. **Multiply the whole equation** by $y$.

   $$y^2\,dt+(2ty+y^4)\,dy=0$$
5. **Re-test.**

   $$M_y=2y=N_t\quad\checkmark$$
6. **Integrate $M$ in $t$.**

   $$U=ty^2+f(y)$$
7. **Match $N$:** $2ty+f^{\prime}=2ty+y^4$, so $f=\frac{y^5}{5}$.

   $$ty^2+\dfrac{y^5}{5}=C$$

**Answer:** $ty^2+\dfrac{y^5}{5}=C$.

</details>

**Problem: Problem 24 · W4 · Which theorem applies?** (advanced)

Find an integrating factor for each equation, then solve it.

(a) $(2y+3t)\,dt+t\,dy=0$

(b) $y^2\,dt+(ty+1)\,dy=0$

<details><summary>Solution</summary>

1. (a) **Test:** $M_y=2$, $N_t=1$. Theorem 1: $\frac{2-1}{t}=\frac1t$, only $t$.

   $$\mu=e^{\int\frac1t dt}=t$$
2. (a) Multiply by $t$: this is exactly the B3 worked example.

   $$(2ty+3t^2)\,dt+t^2\,dy=0$$
3. (a) Its solution (from B3).

   $$t^2y+t^3=C$$
4. (b) **Test:** $M_y=2y$, $N_t=y$. Theorem 1 gives $\frac{y}{ty+1}$ (both letters). Theorem 2:

   $$\dfrac{N_t-M_y}{M}=\dfrac{y-2y}{y^2}=-\dfrac1y$$
5. (b) **Integrating factor:** $e^{-\ln|y|}$.

   $$\mu=\dfrac1y$$
6. (b) Multiply by $\frac1y$ and re-test: $M_y=1=N_t$.

   $$y\,dt+\Big(t+\dfrac1y\Big)dy=0$$
7. (b) $U=ty+f(y)$; matching $N$ gives $f^{\prime}=\frac1y$, so $f=\ln|y|$.

   $$ty+\ln|y|=C$$

**Answer:** (a) $\mu=t$, $\;t^2y+t^3=C$. (b) $\mu=\dfrac1y$, $\;ty+\ln|y|=C$.

</details>

### B5 · Second order, constant coefficients: the characteristic equation

[Week 5 · Topic 1](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/0c7a77fe-aeed-47a8-b1c3-4967d73eea21#92fa557c-ab2a-49cb-a238-b9f4e76fa0b8)

**Now the equation has $y^{\prime\prime}$.** When every coefficient is a plain number, one guess solves it: $y=e^{st}$. Each derivative just brings out another $s$, so the whole ODE turns into a quadratic in $s$.

Second-order linear homogeneous equations with constant coefficients look like:

$$a\,y^{\prime\prime}+b\,y^{\prime}+c\,y=0$$

- $a,b,c$ = numbers (constants), with $a\neq0$
- right side $=0$ (homogeneous). If it isn’t $0$, you also need [B6](#b6).

Reading off the characteristic equation (replace $y^{\prime\prime}\to s^2$, $y^{\prime}\to s$, $y\to1$):

- $y^{\prime\prime}+3y^{\prime}+2y=0$ → $s^2+3s+2=0$
- $4y^{\prime\prime}+4y^{\prime}+y=0$ → $4s^2+4s+1=0$
- $y^{\prime\prime}+9y=0$ → $s^2+9=0$ (no $y^{\prime}$ term, so no $s$ term)

**The characteristic equation.** Its roots decide the form of the solution:

$$a\,s^2+b\,s+c=0$$

Solve it by factoring, or with the quadratic formula:

$$s=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$$

If $b^2-4ac<0$, the square root is of a negative number: $\sqrt{-16}=j4$. See [Topic A](#topic-a) for complex roots.

| Roots | General solution $y(t)$ | $y(0)$ | $y^{\prime}(0)$ |
|---|---|---|---|
| two different real: $s_1\neq s_2$ | $Ae^{s_1t}+Be^{s_2t}$ | $A+B$ | $s_1A+s_2B$ |
| one repeated real: $s$ | $(A+Bt)\,e^{st}$ | $A$ | $sA+B$ |
| complex pair: $\sigma\pm j\omega$ | $e^{\sigma t}(A\cos\omega t+B\sin\omega t)$ | $A$ | $\sigma A+\omega B$ |

The last two columns are the time saver: with conditions at $t=0$ you get the two equations for $A$ and $B$ without differentiating. For conditions at any other time, differentiate $y(t)$ yourself.

**Method:**

1. **Characteristic equation:** replace $y^{\prime\prime}\to s^2$, $y^{\prime}\to s$, $y\to1$.
2. **Roots:** factor, or use the quadratic formula.
3. **Form:** pick the row of the table that matches the roots.
4. **Conditions:** $y(0)$ and $y^{\prime}(0)$ give two equations; solve for $A$ and $B$.

**Calculus you need here** (to differentiate the forms yourself):

| Function | Derivative | Rule |
|---|---|---|
| $e^{st}$ | $s\,e^{st}$ | chain rule |
| $t\,e^{st}$ | $(1+st)\,e^{st}$ | product rule |
| $e^{\sigma t}\cos\omega t$ | $e^{\sigma t}(\sigma\cos\omega t-\omega\sin\omega t)$ | product rule |
| $e^{\sigma t}\sin\omega t$ | $e^{\sigma t}(\sigma\sin\omega t+\omega\cos\omega t)$ | product rule |

```graph
title "Slide $k$ through 1: the same start, three kinds of response"
x 0 8 label="$t$"
y -0.6 1.2 label="$y$"
slider k 0 5 0.5 step=0.05 label="$k$" animate
let d "sqrt(abs(1-k))"
let s1 "-1+d"
let s2 "-1-d"
curve "if(k<0.999, (s2*exp(s1*x)-s1*exp(s2*x))/(s2-s1), if(k>1.001, exp(-x)*(cos(d*x)+sin(d*x)/d), (1+x)*exp(-x)))" label="$y(t)$" color=1
hline "0"
readout "$b^2-4ac=4-4k$" "4-4*k"
caption "$y^{\prime\prime}+2y^{\prime}+ky=0$ with $y(0)=1$, $y^{\prime}(0)=0$. For $k<1$: two real roots, a smooth decay. At $k=1$: a repeated root. For $k>1$: complex roots, and the solution oscillates inside a decaying envelope $e^{-t}$."
```

> **Info:** **Bonus (skip-safe): why $e^{st}$ turns the ODE into a quadratic.** Put $y=e^{st}$, $y^{\prime}=se^{st}$, $y^{\prime\prime}=s^2e^{st}$ into the ODE:
> 
> $$
> as^2e^{st}+bse^{st}+ce^{st}=(as^2+bs+c)\,e^{st}=0
> $$
> 
> Since $e^{st}$ is never zero, the bracket must be: that is the characteristic equation. Complex roots give real answers through Euler, $e^{(\sigma\pm j\omega)t}=e^{\sigma t}(\cos\omega t\pm j\sin\omega t)$. The extra $t$ for a repeated root comes from reduction of order ([B7](#b7)).

**Example: Example 6 · W5 · Complex roots, real answer**

Solve $y''+2y'+5y=0$, $\;y(0)=1$, $y'(0)=1$.

1. **Type:** second order, constant coefficients, right side 0.
2. **Characteristic equation** and roots; $\sqrt{4-20}=\sqrt{-16}=j4$.

   $$s^2+2s+5=0\quad\Rightarrow\quad s=\dfrac{-2\pm j4}{2}=-1\pm j2$$
3. **Form:** complex row, with $\sigma=-1$ and $\omega=2$.

   $$y=e^{-t}(A\cos2t+B\sin2t)$$
4. **Conditions** from the table: $y(0)=A$ and $y^{\prime}(0)=\sigma A+\omega B$.

   $$A=1,\qquad -A+2B=1\ \Rightarrow\ B=1$$

**Answer:** $y=e^{-t}(\cos2t+\sin2t)$: an oscillation (frequency 2 rad/s) inside a decaying envelope $e^{-t}$.

**Problem: Problem 25 · W5 · Two different real roots** (introductory)

Solve $y''+5y'+6y=0$, $\;y(0)=2$, $y'(0)=-5$.

<details><summary>Solution</summary>

1. **Type:** constant coefficients, homogeneous.
2. **Characteristic equation:** factor it.

   $$s^2+5s+6=(s+2)(s+3)=0\quad\Rightarrow\quad s=-2,\,-3$$
3. **Form:** two different real roots.

   $$y=Ae^{-2t}+Be^{-3t}$$
4. **Conditions:** $y(0)=A+B$, $y^{\prime}(0)=-2A-3B$.

   $$A+B=2,\qquad -2A-3B=-5$$
5. Multiply the first by 2 and add: $-B=-1$.

   $$B=1,\qquad A=1$$

**Answer:** $y=e^{-2t}+e^{-3t}$.

</details>

**Problem: Problem 26 · W5 · A repeated root** (introductory)

Solve $4y''+4y'+y=0$, $\;y(0)=4$, $y'(0)=0$.

<details><summary>Solution</summary>

1. **Type:** constant coefficients, homogeneous.
2. **Characteristic equation:** a perfect square.

   $$4s^2+4s+1=(2s+1)^2=0\quad\Rightarrow\quad s=-\tfrac12\ \text{(twice)}$$
3. **Form:** repeated root, so the extra $t$.

   $$y=(A+Bt)\,e^{-t/2}$$
4. **Conditions:** $y(0)=A$, $y^{\prime}(0)=sA+B$ with $s=-\frac12$.

   $$A=4,\qquad -2+B=0\ \Rightarrow\ B=2$$

**Answer:** $y=(4+2t)\,e^{-t/2}$.

</details>

**Problem: Problem 27 · W5 · No damping term** (intermediate)

Solve $y''+9y=0$, $\;y(0)=2$, $y'(0)=3$.

<details><summary>Solution</summary>

1. **Type:** constant coefficients, homogeneous; there is no $y^{\prime}$ term ($b=0$).
2. **Characteristic equation:** $s^2=-9$.

   $$s=\pm j3\qquad(\sigma=0,\ \omega=3)$$
3. **Form:** complex row with $e^{0t}=1$.

   $$y=A\cos3t+B\sin3t$$
4. **Conditions:** $y(0)=A$, $y^{\prime}(0)=\omega B=3B$.

   $$A=2,\qquad B=1$$

**Answer:** $y=2\cos3t+\sin3t$. With $\sigma=0$ it never decays: this is the ideal LC circuit in [Topic D](#topic-d).

</details>

**Problem: Problem 28 · W5 · Work backwards from the roots** (advanced)

A constant-coefficient equation $y^{\prime\prime}+by^{\prime}+cy=0$ has characteristic roots $-3\pm j4$. 

(a) Find $b$ and $c$. (b) Write the general solution. (c) Find the solution with $y(0)=0$, $y^{\prime}(0)=8$.

<details><summary>Solution</summary>

1. **Type:** reverse question: build the quadratic from its roots, $(s-s_1)(s-s_2)=0$.
2. (a) Multiply out the conjugate pair: $(s+3)^2-(j4)^2=(s+3)^2+16$.

   $$s^2+6s+25=0\quad\Rightarrow\quad b=6,\ c=25$$
3. (b) **Form:** complex row with $\sigma=-3$, $\omega=4$.

   $$y=e^{-3t}(A\cos4t+B\sin4t)$$
4. (c) **Conditions:** $y(0)=A=0$; $y^{\prime}(0)=\sigma A+\omega B=4B=8$.

   $$A=0,\qquad B=2$$

**Answer:** (a) $y^{\prime\prime}+6y^{\prime}+25y=0$. (b) $y=e^{-3t}(A\cos4t+B\sin4t)$. (c) $y=2e^{-3t}\sin4t$.

</details>

### B6 · Undetermined coefficients

[Week 6 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/357f26bd-d16c-4769-af0a-d1b2f535d62e#77a5aea3-a3f4-4738-a817-01c3f18cfdae)

**What if the right side isn’t zero?** The forcing $g(t)$ (a source, in a circuit) pushes the solution. The [B5](#b5) solutions only ever produce $0$ on the right, so they need a partner that produces $g(t)$.

Second-order linear equations with constant coefficients and a forcing term look like:

$$a\,y^{\prime\prime}+b\,y^{\prime}+c\,y=g(t)$$

- left side = the same as in B5 (numbers $a,b,c$)
- $g(t)$ = the **forcing**: everything with no $y$ in it, moved to the right

The solution is always built from two pieces:

$$y=y_c+y_p$$

- $y_c$ = the **complementary solution**: the general solution with $g$ replaced by $0$ (that is [B5](#b5)). It holds the two constants $c_1,c_2$.
- $y_p$ = a **particular solution**: any one function that produces $g(t)$. No constants.

Mini example: $y^{\prime\prime}+y=3$. Then $y_c=c_1\sin t+c_2\cos t$, and $y_p=3$ works ($0+3=3$). So $y=3+c_1\sin t+c_2\cos t$.

**Finding $y_p$: guess its form from $g(t)$.** Write a guess with unknown coefficients ($A,B,\dots$), substitute it, and match coefficients. The guess copies the shape of $g$:

| Term in $g(t)$ | Guess for $y_p$ |
|---|---|
| constant, or polynomial of degree $n$ | $A_nt^n+\dots+A_1t+A_0$ (**all** lower powers) |
| $e^{at}$ | $Ae^{at}$ |
| $\sin rt$ or $\cos rt$ | $A\cos rt+B\sin rt$ (**always both**) |
| $e^{at}\cos rt$ or $e^{at}\sin rt$ | $e^{at}(A\cos rt+B\sin rt)$ |
| a sum of these | the sum of their guesses |

> **Warning:** **The $\times t$ rule.** If any term of your guess already appears in $y_c$, substituting it gives $0$, so it can never produce $g$. **Multiply that guess by $t$.** If it is still in $y_c$ (a repeated root), multiply by $t^2$.

**Method:**

1. **Complementary:** solve the equation with $g=0$ ([B5](#b5)) to get $y_c$.
2. **Guess:** take $y_p$’s form from the table. Compare it with $y_c$; apply the $\times t$ rule if needed.
3. **Substitute** $y_p$ into the ODE and **match coefficients** (constants, each $\cos$, each $\sin$, each power of $t$). Solve for $A,B,\dots$
4. **Add:** $y=y_c+y_p$.
5. **Conditions** on the **whole** $y$, never on $y_c$ or $y_p$ alone.

**Calculus you need here:**

| Expression | Result | Note |
|---|---|---|
| $\cos^2t$ | $\tfrac12+\tfrac12\cos2t$ | remove squares before guessing |
| $\sin^2t$ | $\tfrac12-\tfrac12\cos2t$ |  |
| $(A\cos rt+B\sin rt)^{\prime\prime}$ | $-r^2(A\cos rt+B\sin rt)$ | each derivative brings out an $r$ |
| $(te^{at})^{\prime}$ | $(1+at)\,e^{at}$ | product rule |
| $(t\,f)^{\prime\prime}$ | $t\,f^{\prime\prime}+2f^{\prime}$ | product rule twice, for a $\times t$ guess |

> **Info:** **Bonus (skip-safe): why $y=y_c+y_p$ works.** The left side is linear: put in $y_c+y_p$ and you get (what $y_c$ gives) + (what $y_p$ gives) $=0+g=g$. And $y_c$ still carries two free constants, enough to meet any two conditions. The $\times t$ rule has the same root: a term of $y_c$ gives $0$ on the left, so it is useless as a guess.

**Example: Example 7 · W6 · The tutorial problem, with two boundary values · Week 6 tutorial, lecture notes p. 3–4**

Solve $\ddot y+y=6\cos^2t$ with $y(0)=0$ and $y(\pi/2)=0$. The tutorial gives the forms $y_c=c_1\sin t+c_2\cos t$ and $y_p=A+B\cos2t+D\sin2t$. ($\ddot y$ is the professor’s notation for $y^{\prime\prime}$.)

1. **Type:** constant coefficients with forcing $6\cos^2t$. **Complementary:** $s^2+1=0$ gives $s=\pm j$.

   $$y_c=c_1\sin t+c_2\cos t$$
2. Remove the square with the identity, so the guess table applies.

   $$6\cos^2t=3+3\cos2t$$
3. **Guess:** constant → $A$; $\cos2t$ → both $\cos2t$ and $\sin2t$. None of them is in $y_c$.

   $$y_p=A+B\cos2t+D\sin2t$$
4. Differentiate twice: each derivative brings out a 2.

   $$y_p''=-4B\cos2t-4D\sin2t$$
5. **Substitute** $y_p^{\prime\prime}+y_p$ and collect.

   $$A-3B\cos2t-3D\sin2t=3+3\cos2t$$
6. **Match** constants, cosines and sines.

   $$A=3,\qquad B=-1,\qquad D=0$$
7. **Add** $y_c$ **before** using the conditions: they apply to the whole $y$.

   $$y=3-\cos2t+c_1\sin t+c_2\cos t$$
8. **Condition** $y(0)=0$: $\sin0=0$, $\cos0=1$.

   $$3-1+c_2=0\quad\Rightarrow\quad c_2=-2$$
9. **Condition** $y(\pi/2)=0$: $\cos\pi=-1$, $\sin\frac\pi2=1$, $\cos\frac\pi2=0$.

   $$3+1+c_1=0\quad\Rightarrow\quad c_1=-4$$

**Answer:** $y=3-\cos2t-4\sin t-2\cos t$.

```graph
title "Tutorial problem: pick the constants"
x 0 6.3 label="$t$"
y -8 8 label="$y$"
slider c1 -6 6 0 step=0.5 label="$c_1$"
slider c2 -6 6 0 step=0.5 label="$c_2$"
curve "3-cos(2*x)" label="$y_p=3-\cos2t$" color=0 dash
curve "3-cos(2*x)+c1*sin(x)+c2*cos(x)" label="$y=y_p+c_1\sin t+c_2\cos t$" color=1
point "0" "0" label="must pass $(0,0)$" color=3
point "pi/2" "0" label="must pass $(\pi/2,0)$" color=3
readout "$y(0)$" "2+c2"
readout "$y(\pi/2)$" "4+c1"
caption "Every $c_1,c_2$ gives a solution of the ODE. Only $c_1=-4$, $c_2=-2$ passes through both points."
```

**Why the $\times t$ rule matters.** When the forcing matches a term of $y_c$, the response does not settle to the shape of $g$: it keeps growing, like $t\cos2t$. Slide $\omega$ to 2:

```graph
title "Forcing at the natural frequency"
x 0 12 label="$t$"
y -25 25 label="$y$"
slider w 1 3 1.5 step=0.05 label="$\omega$" animate
curve "if(abs(w-2)<0.001, sin(2*x)-2*x*cos(2*x), 8/(4-w^2)*(sin(w*x)-w/2*sin(2*x)))" label="$y(t)$, starting at rest" color=1
curve "2*x" label="$\pm2t$" color=0 dash
curve "-2*x" color=0 dash
caption "Solutions of $y''+4y=8\sin\omega t$ with $y(0)=y'(0)=0$. Here $y_c$ contains $\sin2t$ and $\cos2t$. For $\omega$ far from 2 the swing stays small. At $\omega=2$ the forcing is in $y_c$, the particular solution needs the extra $t$, and the swing grows along $\pm2t$."
```

**Problem: Problem 29 · W6 · A constant forcing, from rest** (introductory)

Solve $y''+4y=8$, $\;y(0)=0$, $y'(0)=0$.

<details><summary>Solution</summary>

1. **Type:** constant coefficients, constant forcing. **Complementary:** $s^2+4=0$, $s=\pm j2$.

   $$y_c=c_1\cos2t+c_2\sin2t$$
2. **Guess:** a constant, $y_p=A$ (not in $y_c$). **Substitute:** $0+4A=8$.

   $$y_p=2$$
3. **Add.**

   $$y=2+c_1\cos2t+c_2\sin2t$$
4. **Conditions:** $y(0)=2+c_1=0$; $y^{\prime}(0)=2c_2=0$.

   $$c_1=-2,\qquad c_2=0$$

**Answer:** $y=2-2\cos2t$. A constant source gives a constant $y_p$: the same idea as an RLC circuit switched onto a DC source ([Topic D](#topic-d)).

</details>

**Problem: Problem 30 · W6 · A polynomial guess needs every lower power** (introductory)

Find the general solution of $y''+y'-2y=2t$.

<details><summary>Solution</summary>

1. **Type:** forcing $2t$. **Complementary:** $s^2+s-2=(s+2)(s-1)$.

   $$y_c=c_1e^{t}+c_2e^{-2t}$$
2. **Guess:** degree 1, so $At+B$. The $B$ is needed even though $g$ has no constant.

   $$y_p=At+B,\quad y_p'=A,\quad y_p''=0$$
3. **Substitute.**

   $$A-2(At+B)=2t$$
4. **Match** the $t$ terms, then the constants.

   $$-2A=2,\qquad A-2B=0$$
5. Solve.

   $$A=-1,\qquad B=-\tfrac12$$

**Answer:** $y=c_1e^{t}+c_2e^{-2t}-t-\tfrac12$. Guessing only $At$ fails: the leftover constant $A$ has nothing to match.

</details>

**Problem: Problem 31 · W6 · The guess is already in the complementary solution** (intermediate)

Find the general solution of $y''-y'-2y=3e^{2t}$.

<details><summary>Solution</summary>

1. **Type:** exponential forcing. **Complementary:** $s^2-s-2=(s-2)(s+1)$.

   $$y_c=c_1e^{2t}+c_2e^{-t}$$
2. **Guess:** the table says $Ae^{2t}$, but that is in $y_c$ (it would give $0=3e^{2t}$). Multiply by $t$.

   $$y_p=Ate^{2t}$$
3. Product rule, twice.

   $$y_p'=A(1+2t)e^{2t},\qquad y_p''=A(4+4t)e^{2t}$$
4. **Substitute** and divide by $e^{2t}$. The $t$ terms cancel.

   $$A\big[(4+4t)-(1+2t)-2t\big]=3A=3$$
5. Solve.

   $$A=1$$

**Answer:** $y_p=te^{2t}$, so $y=c_1e^{2t}+c_2e^{-t}+te^{2t}$.

</details>

**Problem: Problem 32 · W6 · Choose the form; do not solve** (intermediate)

For $y''-2y'+y=g(t)$, write the guess for $y_p$ when $g$ is (a) $t^2$, (b) $e^{-t}$, (c) $e^t$, (d) $\cos t$.

<details><summary>Solution</summary>

1. **Type:** guessing only. **Complementary** first: $s^2-2s+1=(s-1)^2$, a repeated root.

   $$y_c=(c_1+c_2t)e^t$$
2. (a) Degree 2: all lower powers.

   $$At^2+Bt+C$$
3. (b) $e^{-t}$ is not in $y_c$.

   $$Ae^{-t}$$
4. (c) $Ae^t$ and $Ate^t$ are **both** in $y_c$, so multiply by $t^2$.

   $$At^2e^t$$
5. (d) Cosine needs both cosine and sine.

   $$A\cos t+B\sin t$$

**Answer:** (a) $At^2+Bt+C$. (b) $Ae^{-t}$. (c) $At^2e^t$. (d) $A\cos t+B\sin t$.

</details>

**Problem: Problem 33 · W6 · A trig guess that is already in the complementary solution** (advanced)

Find a particular solution of $y''+9y=12\cos3t$. Use $(tf)^{\prime\prime}=tf^{\prime\prime}+2f^{\prime}$ from the calculus table.

<details><summary>Solution</summary>

1. **Type:** trig forcing. **Complementary:** $y_c=c_1\cos3t+c_2\sin3t$ already contains $\cos3t$, so multiply the guess by $t$.

   $$y_p=t\,f,\qquad f=A\cos3t+B\sin3t$$
2. **Substitute:** since $f^{\prime\prime}=-9f$, the $t$ terms cancel in $y_p^{\prime\prime}+9y_p$.

   $$y_p''+9y_p=t(f''+9f)+2f'=2f'$$
3. Differentiate $f$.

   $$2f'=-6A\sin3t+6B\cos3t$$
4. **Match** with $12\cos3t$.

   $$6B=12,\qquad -6A=0$$

**Answer:** $A=0$, $B=2$: $y_p=2t\sin3t$. The swing grows like $2t$, as in the graph above.

</details>

### B7 · Reduction of order

[Week 6 · Topic 1](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/357f26bd-d16c-4769-af0a-d1b2f535d62e#400c9eda-6dcb-4cf4-9c21-265384342cb1)

**What if the coefficients have $t$ in them?** Like $y^{\prime\prime}-ty^{\prime}+y=0$. The characteristic equation ([B5](#b5)) only works when the coefficients are numbers. But if the question **gives you one solution** $y_1$, reduction of order finds the second one.

Write the equation with $y^{\prime\prime}$ alone (divide by its coefficient):

$$y^{\prime\prime}+p(t)\,y^{\prime}+q(t)\,y=0$$

- $p(t)$ = the coefficient of $y^{\prime}$ (sign included)
- $q(t)$ = the coefficient of $y$
- $y_1(t)$ = the solution you are given. Check it first: it must give $0$.

Mini examples:

- $y^{\prime\prime}-ty^{\prime}+y=0$ with $y_1=t$: here $p=-t$, $q=1$. Check: $0-t\cdot1+t=0$ ✓.
- $t^2y^{\prime\prime}-3ty^{\prime}+4y=0$ with $y_1=t^2$: divide by $t^2$, so $p=-\frac3t$, $q=\frac4{t^2}$.

**The idea.** Look for the second solution as the known one times an unknown function $v(t)$:

$$y=y_1\,v$$

Substituting makes every plain-$v$ term cancel, so only $v^{\prime}$ and $v^{\prime\prime}$ are left. Setting $z=v^{\prime}$ turns that into a **first-order** equation: the order went down by one.

**Method:**

1. **Substitute** $y=y_1v$, with $y^{\prime}=y_1^{\prime} v+y_1v^{\prime}$ and $y^{\prime\prime}=y_1^{\prime\prime} v+2y_1^{\prime} v^{\prime}+y_1v^{\prime\prime}$.
2. **Collect** terms: the plain-$v$ terms cancel, because $y_1$ is a solution.
3. **Set $z=v^{\prime}$** and solve the first-order equation for $z$ (usually separable, [B1](#b1); or linear, [B2](#b2)).
4. **Integrate:** $v=\int z\,dt$, plus a constant.
5. **Multiply back:** $y=y_1v$. The constant from step 4 gives back $C\,y_1$, the solution you started with.

**Check with the formula.** Reduction of order always ends at

$$y_2=y_1\int\dfrac{e^{-\int p\,dt}}{y_1^{\,2}}\,dt$$

Use it to check your answer, or as a shortcut if the question allows it.

**Calculus you need here:**

| Expression | Result | Note |
|---|---|---|
| $(y_1v)^{\prime}$ | $y_1^{\prime} v+y_1v^{\prime}$ | product rule |
| $(y_1v)^{\prime\prime}$ | $y_1^{\prime\prime} v+2y_1^{\prime} v^{\prime}+y_1v^{\prime\prime}$ | product rule twice; the middle terms combine |
| $\int\frac1z\,dz$ | $\ln|z|$ | for the separable $z$ equation |
| $e^{-2\ln t}$ | $\dfrac{1}{t^2}$ | $e^{k\ln t}=t^k$ |
| $\int\dfrac{e^{t^2/2}}{t^2}\,dt$ | no formula | leave it as an integral: that is a full answer |

> **Info:** **Bonus (skip-safe): why the plain-$v$ terms cancel.** After substituting, collect everything that multiplies $v$ itself: it is $v\,(y_1^{\prime\prime}+p\,y_1^{\prime}+q\,y_1)$. The bracket is the ODE applied to $y_1$, which is $0$ because $y_1$ is a solution.

The professor’s example, step by step:

```steps
title "Lecture: reduce y″ − t y′ + y = 0, given y₁ = t"
$$ y''-ty'+y=0,\qquad y_1=t $$
Check: $y_1=t$ gives $0-t+t=0$.
$$ y=\hl{tv} $$
Multiply the known solution by an unknown $v$.
$$ y'=\hl{v+tv'},\qquad y''=\hl{2v'+tv''} $$
Product rule (calculus table).
$$ (2v'+tv'')-t(v+tv')+tv=0 $$
Substitute all three into the ODE.
$$ \hl{tv''+(2-t^2)v'}=0 $$
Collect terms. The $-tv$ and $+tv$ cancel.
$$ t\hl{z'}+(2-t^2)\hl{z}=0 $$
Set $z=v^{\prime}$: first order in $z$.
```

**Example: Example 8 · W6 · Finish the lecture example · handwritten notes p. 1–2**

Solve $tz'+(2-t^2)z=0$ (from the stepper above), then find the general solution of $y''-ty'+y=0$ for $t\neq0$.

1. **Type:** the $z$ equation is separable. Divide by $tz$ and move the $t$ terms right.

   $$\dfrac{dz}{z}=\dfrac{t^2-2}{t}\,dt=\left(t-\dfrac2t\right)dt$$
2. **Integrate** both sides: $\int\frac1z\,dz=\ln|z|$.

   $$\ln|z|=\dfrac{t^2}2-2\ln|t|+C$$
3. Exponentiate; $e^{-2\ln|t|}=1/t^2$.

   $$z=C_1\,\dfrac{e^{t^2/2}}{t^2}$$
4. **Integrate** again, $v=\int z\,dt$. This integral has no formula, so it stays.

   $$v=C_1\int\dfrac{e^{t^2/2}}{t^2}\,dt+C_2$$
5. **Multiply back** by $y_1=t$.

   $$y=tv$$

**Answer:** $y=C_2\,t+C_1\,t\displaystyle\int\frac{e^{t^2/2}}{t^2}\,dt$. Formula check: $p=-t$, so $e^{-\int p\,dt}=e^{t^2/2}$ and $y_1^2=t^2$. ✓

**Problem: Problem 34 · W5 + W6 · Where the repeated-root t comes from** (introductory)

$y''+4y'+4y=0$ has the repeated characteristic root $s=-2$, so $y_1=e^{-2t}$. Use reduction of order to find the general solution.

<details><summary>Solution</summary>

1. **Type:** one solution given: reduction of order. **Substitute** $y=e^{-2t}v$.

   $$y'=e^{-2t}(v'-2v)$$
2. Differentiate again.

   $$y''=e^{-2t}(v''-4v'+4v)$$
3. **Collect:** substitute and divide by $e^{-2t}$. The $v^{\prime}$ terms cancel too.

   $$(v''-4v'+4v)+4(v'-2v)+4v=v''=0$$
4. **Integrate** twice.

   $$v=C_1+C_2t$$
5. **Multiply back.**

   $$y=(C_1+C_2t)\,e^{-2t}$$

**Answer:** $y=(C_1+C_2t)e^{-2t}$: exactly the repeated-root row of [B5](#b5). The extra $t$ is $v$.

</details>

**Problem: Problem 35 · W6 · A second solution with a logarithm** (intermediate)

For $t>0$, $y_1=t^2$ solves $t^2y''-3ty'+4y=0$. Find the general solution.

<details><summary>Solution</summary>

1. **Type:** variable coefficients, one solution given. **Substitute** $y=t^2v$.

   $$y'=2tv+t^2v',\qquad y''=2v+4tv'+t^2v''$$
2. **Collect:** the plain $v$ terms cancel ($2-6+4=0$).

   $$t^4v''+t^3v'=0$$
3. Divide by $t^4$ and **set $z=v^{\prime}$**.

   $$z'+\dfrac zt=0$$
4. Separate: $\int\frac{dz}{z}=-\int\frac{dt}{t}$, so $\ln|z|=-\ln t+C$.

   $$z=\dfrac{C_2}t$$
5. **Integrate:** $\int\frac1t\,dt=\ln t$ for $t>0$.

   $$v=C_1+C_2\ln t$$
6. **Multiply back** by $t^2$.

   $$y=C_1t^2+C_2t^2\ln t$$

**Answer:** $y=C_1t^2+C_2t^2\ln t$. Formula check: $p=-\frac3t$, $e^{-\int p}=t^3$, $\int\frac{t^3}{t^4}dt=\ln t$. ✓

</details>

## Topic C: Does exactly one solution exist?

[Week 3 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/3d1ae4a9-687d-4654-873d-be3439faea2f#8c746b9b-2fbf-48f4-8a2d-704a643bdcf7) [Week 5 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/0c7a77fe-aeed-47a8-b1c3-4967d73eea21#b4f41ebe-f4f6-4d5d-816d-ceaa37811b8f)

Some midterm questions ask **whether** a problem has exactly one solution, or **where** it is guaranteed, without solving anything. Two theorems answer that: one for first-order equations, one for second-order linear ones.

The answer is always found the same way: write the equation in a standard form, then look for the places where something breaks (division by zero, a log of a negative, a square root of a negative).

### C1 · First order: is there exactly one solution through this point?

[Week 3 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/3d1ae4a9-687d-4654-873d-be3439faea2f#8c746b9b-2fbf-48f4-8a2d-704a643bdcf7)

**When:** the question gives $\dfrac{dy}{dt}=F(t,y)$ and a starting point $(t_0,y_0)$, and asks if a unique solution passes through it.

Write the equation with the derivative alone:

$$\dfrac{dy}{dt}=F(t,y)$$

- $F(t,y)$ = everything on the right side once $\dfrac{dy}{dt}$ is alone
- $\dfrac{\partial F}{\partial y}$ = its **partial derivative** in $y$: differentiate in $y$ while treating $t$ as a constant

**The theorem** (Spiegel, used in the Week 3 lecture):

> **Info:** If $F$ and $\dfrac{\partial F}{\partial y}$ are both continuous (finite, defined) in a region around $(t_0,y_0)$, then **exactly one** solution passes through $(t_0,y_0)$.

- **Conditions hold** → existence and uniqueness are guaranteed (near $t_0$).
- **Conditions fail** → the theorem says **nothing**. There may be no solution, one, or many. The conditions are sufficient, not necessary.

Mini examples:

- $y^{\prime}=t^2+3ty$: $F_y=3t$. Both are fine everywhere → unique through **every** point.
- $y^{\prime}=\dfrac{t}{y}$: $F_y=-\dfrac{t}{y^2}$. Both break on the line $y=0$ → guaranteed only at points with $y_0\neq0$.

**Method:**

1. **Write $F$:** get $\dfrac{dy}{dt}$ alone.
2. **Differentiate:** find $\dfrac{\partial F}{\partial y}$, holding $t$ fixed.
3. **Find the bad set:** where is $F$ or $\dfrac{\partial F}{\partial y}$ undefined (divide by 0, $\ln$ of $\le0$, $\sqrt{\ }$ of $<0$, $y^{-1/2}$ at $y=0$)?
4. **Check the point:** is $(t_0,y_0)$ away from the bad set? Yes → unique solution. No → no conclusion.

**Calculus you need here:**

| $F$ | $\dfrac{\partial F}{\partial y}$ | Note |
|---|---|---|
| $t^2+3ty$ | $3t$ | $t$ is a constant: $t^2$ disappears |
| $\dfrac{t}{y}=t\,y^{-1}$ | $-t\,y^{-2}$ | power rule in $y$ |
| $\sqrt{y}=y^{1/2}$ | $\dfrac{1}{2\sqrt y}$ | undefined at $y=0$ |
| $\dfrac{2t-(\ln t)\,y}{t-3}$ | $-\dfrac{\ln t}{t-3}$ | only the $y$ term survives |

```graph
title "$y^{\prime}=\sqrt{y}$: one solution through $(1,4)$, many through $(1,0)$"
x -1 5 label="$t$"
y -0.5 6 label="$y$"
field "sqrt(max(y,0))" density=18
hline "0" label="$y=0$ is a solution" color=1
family c 1 3 0.5 "if(x>c,(x-c)^2/4,0)" color=2 label="also solutions through $(1,0)$"
curve "((x+3)/2)^2" from=-3 label="the only solution through $(1,4)$" color=3
point "1" "0" color=1
point "1" "4" color=3
caption "At $y=0$, $\partial F/\partial y=1/(2\sqrt y)$ is undefined, so the theorem gives no guarantee, and indeed many curves leave $(1,0)$: each stays at 0, then rises as $(t-c)^2/4$. Above the axis everything is smooth and the solution is unique."
```

> **Info:** **Bonus (skip-safe): why a blown-up $\partial F/\partial y$ allows several solutions.** $\partial F/\partial y$ measures how strongly nearby curves are pushed apart. If it stays finite, two solutions that start together can never separate. At $y=0$ for $\sqrt y$ it is infinite, so a curve can “peel off” the axis at any moment.

**Problem: Problem 36 · W3 · Same equation, two starting points** (introductory)

For $\dfrac{dy}{dt}=\sqrt{y}$: (a) does the theorem guarantee a unique solution through $(1,4)$? (b) through $(1,0)$? For (b), check that $y=0$ and $y=\dfrac{(t-1)^2}{4}$ (for $t\ge1$) both pass through $(1,0)$ and solve the ODE.

<details><summary>Solution</summary>

1. **Type:** existence and uniqueness, first order. $F=\sqrt y$.
2. **Differentiate** in $y$.

   $$\dfrac{\partial F}{\partial y}=\dfrac{1}{2\sqrt y}$$
3. **Bad set:** $F$ needs $y\ge0$; $F_y$ is undefined at $y=0$. So the bad set is $y\le0$.
4. (a) $(1,4)$ has $y_0=4>0$: both are continuous around it → unique.
5. (b) $(1,0)$ lies on $y=0$ → no conclusion from the theorem.
6. Check $y=\frac{(t-1)^2}{4}$: $y^{\prime}=\frac{t-1}{2}$ and $\sqrt y=\frac{t-1}{2}$ for $t\ge1$ ✓. And $y=0$: $0=\sqrt0$ ✓. Both equal 0 at $t=1$.

**Answer:** (a) Yes, exactly one solution through $(1,4)$. (b) The theorem gives no guarantee, and in fact at least two solutions pass through $(1,0)$.

</details>

**Problem: Problem 37 · W3 · Which points are guaranteed?** (introductory)

For $\dfrac{dy}{dt}=\dfrac{t}{y}$, decide whether the theorem guarantees a unique solution through (a) $(2,1)$, (b) $(0,3)$, (c) $(2,0)$.

<details><summary>Solution</summary>

1. **Type:** existence and uniqueness, first order. $F=\dfrac ty$.
2. **Differentiate** in $y$ (power rule).

   $$\dfrac{\partial F}{\partial y}=-\dfrac{t}{y^2}$$
3. **Bad set:** both divide by $y$, so the line $y=0$.
4. **Check the points:** (a) $y_0=1$ and (b) $y_0=3$ are off the line; (c) $y_0=0$ is on it.

**Answer:** (a) Yes. (b) Yes. (c) No guarantee: $F$ itself is undefined at $(2,0)$.

</details>

**Problem: Problem 38 · W3 · A strip, not a point** (intermediate)

For $(t-3)\,y^{\prime}+(\ln t)\,y=2t$, $\;y(1)=2$, find the region containing the starting point where the theorem applies. Do not solve.

<details><summary>Solution</summary>

1. **Type:** existence and uniqueness. **Write $F$:** isolate $y^{\prime}$.

   $$F=\dfrac{2t-(\ln t)\,y}{t-3}$$
2. **Differentiate** in $y$; only the $y$ term survives.

   $$\dfrac{\partial F}{\partial y}=-\dfrac{\ln t}{t-3}$$
3. **Bad set:** $\ln t$ needs $t>0$; division needs $t\neq3$. Nothing restricts $y$.
4. **Check the point:** $t_0=1$ lies between $0$ and $3$.

   $$0<t<3,\quad\text{any }y$$

**Answer:** The strip $0<t<3$ (all $y$). The start $(1,2)$ is inside it, so exactly one solution passes through it.

</details>

### C2 · Second order linear: interval, zero start, independent solutions

[Week 5 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/0c7a77fe-aeed-47a8-b1c3-4967d73eea21#b4f41ebe-f4f6-4d5d-816d-ceaa37811b8f)

**When:** a second-order **linear** equation with two conditions $y(t_0)$, $y^{\prime}(t_0)$, and the question asks on what interval exactly one solution exists, or whether two given solutions can build the general solution.

First divide by the coefficient of $y^{\prime\prime}$ so it stands alone:

$$y^{\prime\prime}+p(t)\,y^{\prime}+q(t)\,y=g(t)$$

- $p(t)$ = the coefficient of $y^{\prime}$ (after dividing)
- $q(t)$ = the coefficient of $y$ (after dividing)
- $g(t)$ = the forcing (after dividing)

> **Info:** **The theorem.** If $p$, $q$ and $g$ are continuous on an open interval $I$ containing $t_0$, then for **any** values of $y(t_0)$ and $y^{\prime}(t_0)$ there is **exactly one** solution, and it exists on the **whole** interval $I$.

- The largest such $I$ runs from the nearest “trouble point” on the left of $t_0$ to the nearest on the right.
- Constant coefficients ($ay^{\prime\prime}+by^{\prime}+cy=g$ with continuous $g$): no trouble points, $I$ is the whole real line.

Mini example: $t\,y^{\prime\prime}+y=0$ → divide by $t$: $q=\dfrac1t$, trouble at $t=0$. For $t_0=5$: $I=(0,\infty)$. For $t_0=-2$: $I=(-\infty,0)$.

**Method (interval):**

1. **Divide** by the coefficient of $y^{\prime\prime}$; read $p,q,g$.
2. **Trouble points:** where $p$, $q$ or $g$ is undefined (zero denominators, $\ln$ of $\le0$, …).
3. **Pick the piece** of the $t$-axis between trouble points that contains $t_0$. Use open ends.

**Zero start.** If the equation is linear and **homogeneous** ($g=0$) and both conditions are zero, $y(t_0)=0$ and $y^{\prime}(t_0)=0$, then:

$$y(t)\equiv0$$

Reason in one line: $y=0$ obviously solves it and fits both conditions, and the theorem says there is only one solution. No solving needed.

**Two solutions → the general solution?** If $y_1$ and $y_2$ solve the same homogeneous linear equation, compute their **Wronskian**:

$$W=y_1\,y_2^{\prime}-y_1^{\prime}\,y_2$$

- $W\neq0$ → $y_1,y_2$ are **independent**, and $y=c_1y_1+c_2y_2$ is the general solution.
- $W=0$ → one is a multiple of the other; they give only one real constant, so they are **not** enough.

This is why the repeated-root case in [B5](#b5) uses $(c_1+c_2t)e^{st}$ and not $c_1e^{st}+c_2e^{st}$.

> **Info:** **Bonus (skip-safe): why the Wronskian decides it.** Fitting $c_1y_1+c_2y_2$ to $y(t_0)$ and $y^{\prime}(t_0)$ gives two equations:
> 
> $$
> c_1y_1+c_2y_2=y(t_0),\quad c_1y_1^{\prime}+c_2y_2^{\prime}=y^{\prime}(t_0)
> $$
> 
> That $2\times2$ system has a unique answer exactly when its determinant $y_1y_2^{\prime}-y_1^{\prime} y_2=W$ is not zero. $W\neq0$ means every pair of starting values can be matched.

**Problem: Problem 39 · W5 · Find the interval; do not solve** (intermediate)

For $(t-1)\,y^{\prime\prime}+y^{\prime}+y=\ln t$, find the largest interval on which the theorem guarantees exactly one solution for (a) $t_0=2$, (b) $t_0=\tfrac12$.

<details><summary>Solution</summary>

1. **Type:** existence and uniqueness, second-order linear. **Divide** by $t-1$.

   $$\begin{gathered}p=\dfrac1{t-1}, \\ q=\dfrac1{t-1}, \\ g=\dfrac{\ln t}{t-1}\end{gathered}$$
2. **Trouble points:** $\ln t$ needs $t>0$; the denominator needs $t\neq1$. So the pieces are $(0,1)$ and $(1,\infty)$.
3. **Pick the piece:** $t_0=2$ is in $(1,\infty)$; $t_0=\tfrac12$ is in $(0,1)$.

**Answer:** (a) $(1,\infty)$. (b) $(0,1)$.

</details>

**Problem: Problem 40 · W5 · Which pair gives the general solution?** (intermediate)

Both pairs solve $y^{\prime\prime}+4y^{\prime}+4y=0$: (a) $e^{-2t}$ and $3e^{-2t}$; (b) $e^{-2t}$ and $te^{-2t}$. Compute each Wronskian and decide which pair gives the general solution.

<details><summary>Solution</summary>

1. **Type:** independence: compute $W=y_1y_2^{\prime}-y_1^{\prime} y_2$.
2. (a) $y_2^{\prime}=-6e^{-2t}$, $y_1^{\prime}=-2e^{-2t}$.

   $$W=e^{-2t}(-6e^{-2t})-(-2e^{-2t})(3e^{-2t})=0$$
3. (b) Product rule: $(te^{-2t})^{\prime}=(1-2t)e^{-2t}$.

   $$W=e^{-2t}(1-2t)e^{-2t}-(-2e^{-2t})\,te^{-2t}=e^{-4t}$$
4. $e^{-4t}$ is never zero, so pair (b) is independent.

**Answer:** (a) $W=0$: not enough (they are multiples). (b) $W=e^{-4t}\neq0$: general solution $y=(c_1+c_2t)e^{-2t}$.

</details>

**Problem: Problem 41 · W5 + W6 · The answer without solving** (advanced)

Solve $y^{\prime\prime}+t\,y^{\prime}+e^{t}\,y=0$, $\;y(0)=0$, $\;y^{\prime}(0)=0$.

<details><summary>Solution</summary>

1. **Type:** looks unsolvable with our methods ($t$ and $e^t$ coefficients), but it is linear, homogeneous, with a **zero start**.
2. **Interval:** $p=t$, $q=e^t$, $g=0$ are continuous everywhere, so exactly one solution exists on the whole real line.
3. **Guess the obvious one:** $y=0$ gives $0+0+0=0$ ✓, and $y(0)=0$, $y^{\prime}(0)=0$ ✓.
4. By uniqueness, that is **the** solution.

**Answer:** $y(t)\equiv0$ for all $t$.

</details>

## Topic D: Circuits → ODE → solution

[Week 2 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/08d203f6-a2b5-41b9-adfd-a14e22fb03d8#77c9c878-68d6-44e3-8f1e-2f68ba18701b) [Week 5 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/0c7a77fe-aeed-47a8-b1c3-4967d73eea21#d5ad9ba9-0ec5-4b62-acf5-b1c7e17d6463)

Every circuit question in this course is the same job: a switch moves (or a source changes) at $t=0$, and you need $v(t)$ or $i(t)$ afterwards.

The circuit hands you two things:

- **the ODE**, from KVL or KCL after the switch;
- **the starting values**, from the circuit before the switch.

Then Topic B solves the ODE, exactly as before.

**The element facts.** Everything in this topic comes from these three rows:

| Element | Law | In DC steady state | At the switching instant |
|---|---|---|---|
| Capacitor $C$ | $i=C\dfrac{dv}{dt}$ | **open circuit** ($i=0$) | $v_C$ **cannot jump**: $v_C(0^+)=v_C(0^-)$ |
| Inductor $L$ | $v=L\dfrac{di}{dt}$ | **short circuit** ($v=0$) | $i_L$ **cannot jump**: $i_L(0^+)=i_L(0^-)$ |
| Resistor $R$ | $v=iR$ | — | its current and voltage **can** jump |

- **DC steady state** = “the switch has been there **for a long time**”: nothing changes any more, so every $\frac{d}{dt}$ is 0.
- $0^-$ = just before the switch moves; $0^+$ = just after.

So always solve for the quantity that **can’t jump**: $v_C$ in a capacitor circuit, $i_L$ in an inductor circuit. Get everything else (resistor currents, $i_C$, $v_L$) from it afterwards.

**What each element looks like at the three moments you need:**

|  | $t=0^-$ (old DC state) | $t=0^+$ (just after) | $t\to\infty$ (new DC state) |
|---|---|---|---|
| Capacitor | open circuit, holding $V_0$ | a **voltage source** $V_0$ | open circuit again |
| Inductor | short circuit, carrying $I_0$ | a **current source** $I_0$ | short circuit again |
| Resistor | Ohm’s law | Ohm’s law (may jump) | Ohm’s law |

```graph
title "A capacitor charging from $0\,\mathrm{V}$: its voltage is continuous, its current jumps"
x -1 5 label="$t/\tau$"
y -0.2 1.2 label="fraction of final value"
curve "if(x<0, 0, 1-exp(-x))" label="$v_C$: starts at 0, no jump" color=1
curve "if(x<0, 0, exp(-x))" label="$i_C$: 0 before, jumps at $t=0$" color=2
vline "0" label="switch closes" color=0
caption "Pre-tutorial 2 in picture form. Before the switch closes no current flows. Just after, $v_C$ is still 0, so all of the source current goes into the capacitor: $i_C$ jumps, $v_C$ doesn’t."
```

**The switching recipe** (every circuit problem):

1. **Before ($t<0$):** the switch has been in its old position for a long time, so the circuit is in DC steady state. Replace $C$ by an open circuit and $L$ by a short. Find $v_C(0^-)$ or $i_L(0^-)$.
2. **Just after ($t=0^+$):** carry them over: $v_C(0^+)=v_C(0^-)$, $i_L(0^+)=i_L(0^-)$. To find anything else at $0^+$, redraw the **new** circuit with $C$ as a voltage source $v_C(0^+)$ and $L$ as a current source $i_L(0^+)$, then use KVL/KCL.
3. **After ($t>0$):** in the new circuit, write KCL at a node or KVL around the loop. Replace $i_C$ by $C\frac{dv}{dt}$ and $v_L$ by $L\frac{di}{dt}$. That is the ODE.
4. **Solve:** one $L$ or $C$ → first order → [B2](#b2) (or the [D1](#d1) formula). An $L$ and a $C$ → second order → [B5](#b5) (no source) or [B6](#b6) (constant source), see [D2](#d2). The values from step 2 are the conditions.
5. **Check ($t\to\infty$):** DC steady state again ($C$ open, $L$ short). Your answer must approach this final value.

> **Warning:** **Before and after are two different circuits.** Draw both. Use the old one only for step 1; write the ODE (step 3) from the new one, with only the parts still connected.

> **Warning:** **Signs come from the drawn arrow.** If the reference arrow for $i_L$ points against the real current, the starting value is **negative**. Find the real direction first, then compare it with the arrow.

> **Info:** **Bonus (skip-safe): why $v_C$ and $i_L$ can’t jump.** If $v_C$ jumped, $\frac{dv}{dt}$ would be infinite, so $i=C\frac{dv}{dt}$ would be infinite: no real circuit supplies that. The same with $v=L\frac{di}{dt}$ for an inductor current. The stored energy $\frac12Cv^2$ or $\frac12Li^2$ cannot change instantly.

### D1 · First-order RC and RL circuits

[Week 1 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/1cbac07a-cd02-48c2-8c30-c9829c4e06b2#ab5bf400-4411-4869-8d74-7790f8ee6f2c) [Week 2 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/08d203f6-a2b5-41b9-adfd-a14e22fb03d8#77c9c878-68d6-44e3-8f1e-2f68ba18701b) [Week 3 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/3d1ae4a9-687d-4654-873d-be3439faea2f#a43fc96e-8dc5-4a1e-bfdf-bf1acf01f98b)

**When:** after the switch, the circuit has **one** capacitor or **one** inductor (after combining), plus resistors and DC sources. Then the ODE is first order, and it always has the same shape.

Call $x$ the quantity that can’t jump ($v_C$ or $i_L$). For $t>0$, KCL or KVL always gives:

$$\dfrac{dx}{dt}+\dfrac{x}{\tau}=\dfrac{x_f}{\tau}$$

- $x$ = $v_C$ in an RC circuit, $i_L$ in an RL circuit
- $\tau$ = the **time constant** (seconds): $\;\tau=R_{th}C\;$ or $\;\tau=\dfrac{L}{R_{th}}$
- $x_f$ = the **final value** $x(\infty)$, from the DC steady state after the switch ($x_f=0$ if no source is left)
- $R_{th}$ = the resistance the $C$ or $L$ “sees”: turn the sources off (voltage source → short, current source → open) and combine the resistors between its two terminals, in the $t>0$ circuit

This is a [B2](#b2) equation with constant $a=\frac1\tau$ and constant $f=\frac{x_f}{\tau}$. Its shortcut solution, with the starting value $x(0)=x_0$, is the one formula you need:

$$x(t)=x_f+\big(x_0-x_f\big)\,e^{-t/\tau},\qquad t\ge0$$

**Method** (the D0 recipe, specialised):

1. **$x_0$:** from the $t<0$ DC circuit ($C$ open, $L$ short), carried over to $0^+$.
2. **$x_f$:** from the $t\to\infty$ DC circuit, with the switch in its **new** position.
3. **$\tau$:** find $R_{th}$ seen by the $C$ or $L$ in the $t>0$ circuit; $\tau=R_{th}C$ or $L/R_{th}$.
4. **Plug in:** $x(t)=x_f+(x_0-x_f)e^{-t/\tau}$.
5. **Anything else** from $x(t)$: Ohm’s law, KCL, $i_C=C\frac{dv_C}{dt}$, $v_L=L\frac{di_L}{dt}$.

|  | Natural response | Step response |
|---|---|---|
| When | no source is left after $t=0$: stored energy dies out | a DC source drives the circuit after $t=0$ |
| Final value | $x_f=0$ | $x_f$ from the new DC steady state |
| Answer | $x_0\,e^{-t/\tau}$ | $x_f+(x_0-x_f)\,e^{-t/\tau}$ |

**Reading the curve:** after $1\tau$, $e^{-1}=37\%$ of the starting gap $x_0-x_f$ is left (63% done); after $2\tau$, 13.5%; after $5\tau$, under 1% (“done”).

```graph
title "Drag the sliders: the curve always heads for $x_f$, and the tangent at $t=0$ reaches $x_f$ at $t=\tau$"
x 0 8 label="$t$"
y -12 12 label="$x$"
slider x0 -10 10 10 step=1 label="$x_0$"
slider xf -10 10 2 step=1 label="$x_f$"
slider tau 0.2 3 1 step=0.1 label="$\tau$"
curve "xf+(x0-xf)*exp(-x/tau)" label="$x(t)=x_f+(x_0-x_f)e^{-t/\tau}$" color=1
curve "x0+(xf-x0)*x/tau" from=0 to="tau" label="tangent at $t=0$" color=0 dash
hline "xf" label="$x_f$" color=3
point "tau" "xf+(x0-xf)*exp(-1)" label="at $t=\tau$: 37% of the gap left" color=2
readout "$x(5\tau)$" "xf+(x0-xf)*exp(-5)"
caption "Set $x_f=0$ for a natural response. A bigger $\tau$ (bigger $RC$ or $L/R$) means a slower circuit."
```

**Formulas you’ll also need:**

| Quantity | Formula | Note |
|---|---|---|
| derivative of the exponential | $\dfrac{d}{dt}e^{-t/\tau}=-\dfrac1\tau e^{-t/\tau}$ | for $i_C=C\frac{dv}{dt}$ and $v_L=L\frac{di}{dt}$ |
| energy stored | $w_C=\tfrac12Cv^2,\quad w_L=\tfrac12Li^2$ | in joules |
| parallel resistors | $R_1\parallel R_2=\dfrac{R_1R_2}{R_1+R_2}$ | for $R_{th}$ |

> **Info:** **Bonus (skip-safe): where the formula comes from (the lecture’s RC step response).** A current source $I_s$, a resistor $R$ and a capacitor $C$ in parallel. KCL at the top node: capacitor current plus resistor current equals the source current:
> 
> $$
> C\dfrac{dv}{dt}+\dfrac{v}{R}=I_s\quad\Rightarrow\quad\dfrac{dv}{dt}+\dfrac{v}{RC}=\dfrac{I_s}{C}
> $$
> 
> That is the standard form with $\tau=RC$ and $x_f=RI_s$, so $v=RI_s+(V_0-RI_s)e^{-t/RC}$. It is [B2](#b2) with constant coefficients, and it also separates ([B1](#b1)), as the lecture showed for the RL circuit.

**Example: Example 9 · W3 · Circuit → ODE → answer · lecture §1.1**

The switch closes at $t=0$; the inductor carries no current before. Find $i(t)$ for $t\ge0$.

```schematic
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$10\,\Omega$" i="$i$"
L1 6,3 -> 6,0 "$2\,\mathrm{H}$" v="$v$"
wire 6,0 -> 0,0
ground 0,0
```

1. **Type:** one inductor, one DC source → first-order RL step response. Solve for $i$ (the inductor current).
2. **Before:** the switch is open, so no current: $i(0^-)=0$, and $i(0^+)=0$ (it can’t jump).
3. **After:** KVL around the loop: the source equals the resistor voltage plus the inductor voltage.

   $$2\dfrac{di}{dt}+10i=100$$
4. Divide by $L=2$ to get the standard form: $\frac1\tau=5$, so $\tau=0.2\,\mathrm{s}$ (check: $L/R=2/10$).

   $$\dfrac{di}{dt}+5i=50$$
5. **Final value:** at $t\to\infty$ the inductor is a short, so $i_f=100/10=10\,\mathrm{A}$.
6. **Plug in** $x_0=0$, $x_f=10$, $\tau=0.2$.

   $$i(t)=10+(0-10)e^{-5t}$$

**Answer:** $i(t)=10\big(1-e^{-5t}\big)\,\mathrm{A}$, the same answer the integrating factor gave (Problem in [B2](#b2)).

**Problem: Problem 42 · W1 · RL natural response · Pre-tutorial 1** (introductory)

The switch has been closed for a long time and opens at $t=0$. With $L=8\,\mathrm{mH}$, $R=4\,\Omega$ and $I_s=4\,\mathrm{A}$, find the numerical expression for $i(t)$, $t\ge0$, and sketch it.

```schematic
I1 0,0 -> 0,3 "$I_s=4\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$R_0$"
S1 3,3 -> 6,3 "$t=0$" action=open
L1 6,3 -> 6,0 "$8\,\mathrm{mH}$" i="$i$"
wire 6,3 -> 9,3
R2 9,3 -> 9,0 "$4\,\Omega$" v="$v$"
wire 9,0 -> 0,0
ground 0,0
```

<details><summary>Solution</summary>

1. **Type:** after the switch opens, only the $L$–$R$ loop is left, with no source: RL **natural** response. Solve for $i$.
2. **Before:** DC steady state, so $L$ is a short. It shorts $R_0$ and $R$, so all of $I_s$ flows down through $L$.

   $$i(0^-)=4\,\mathrm{A}=i(0^+)$$
3. **After:** $L$ discharges through $R$. No source, so $x_f=0$.

   $$\tau=\dfrac{L}{R}=\dfrac{8\times10^{-3}}{4}=2\,\mathrm{ms}$$
4. **Plug in:** $\frac1\tau=500\,\mathrm{s^{-1}}$.

   $$i(t)=4e^{-500t}\,\mathrm{A}$$
5. **Sketch:** starts at 4 A, is $4e^{-1}\approx1.47\,\mathrm{A}$ at $t=2\,\mathrm{ms}$, and is essentially 0 after $5\tau=10\,\mathrm{ms}$.

**Answer:** $i(t)=4e^{-500t}\,\mathrm{A}$, $t\ge0$ ($\tau=2\,\mathrm{ms}$): an exponential decay from 4 A.

</details>

**Problem: Problem 43 · W2 · Can the capacitor current jump? · Pre-tutorial 2** (introductory)

The capacitor is uncharged ($V_0=0$). The switch closes at $t=0$, with $I_s=2\,\mathrm{A}$ and $R=1\,\mathrm{k\Omega}$. Find the capacitor current at $t=0^-$ (switch open) and at $t=0^+$ (switch closed). Is there a discontinuity in the capacitor current, unlike the capacitor voltage?

```schematic
I1 0,0 -> 0,3 "$I_s=2\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$1\,\mathrm{k\Omega}$" i="$v/R$"
S1 3,3 -> 6,3 "$t=0$" action=close
C1 6,3 -> 6,0 "$C$" v="$v$" i="$i_C$"
wire 6,0 -> 0,0
ground 0,0
```

<details><summary>Solution</summary>

1. **Type:** a $0^-$/$0^+$ question: use “$v_C$ can’t jump”, then KCL at $0^+$.
2. **Before:** the switch is open, so the capacitor is disconnected.

   $$i_C(0^-)=0$$
3. **Just after:** $v(0^+)=v(0^-)=0$ (can’t jump). So the resistor current is $v/R=0$.
4. KCL at the top node: all of the source current must go into the capacitor.

   $$i_C(0^+)=I_s-\dfrac{v(0^+)}{R}=2-0=2\,\mathrm{A}$$
5. **Afterwards:** $v$ rises towards $RI_s=2000\,\mathrm{V}$ and $i_C$ decays to 0.

**Answer:** $i_C(0^-)=0$, $i_C(0^+)=2\,\mathrm{A}$: yes, the capacitor **current** jumps; the capacitor **voltage** stays continuous at 0.

</details>

**Problem: Problem 44 · W2–W3 · Read the circuit from its response · textbook P7.42** (intermediate)

In this circuit the switch closes at $t=0$, and for $t\ge0$:

$i(t)=\big(10-10e^{-500t}\big)\,\mathrm{A},\qquad v(t)=200e^{-500t}\,\mathrm{V}\ (t\ge0^+)$

Find $V_s$, $R$, the initial current $I_0$ and $L$.

```schematic
V1 0,3 -> 0,0 "$V_s$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$R$" i="$i$"
L1 6,3 -> 6,0 "$L$" v="$v$"
wire 6,0 -> 0,0
ground 0,0
```

<details><summary>Solution</summary>

1. **Type:** RL step response read backwards: match $x_f+(x_0-x_f)e^{-t/\tau}$ term by term.
2. **Starting value:** $I_0=i(0)=10-10=0$.
3. **Just after:** $i=0$, so the resistor has no voltage and the whole source appears across $L$.

   $$V_s=v(0^+)=200\,\mathrm{V}$$
4. **Final value:** $L$ is a short, so $i_f=V_s/R$.

   $$10=\dfrac{200}{R}\quad\Rightarrow\quad R=20\,\Omega$$
5. **Time constant:** $\frac1\tau=500$, so $\tau=2\,\mathrm{ms}=L/R$.

   $$L=20\times0.002=40\,\mathrm{mH}$$
6. **Check:** $L\frac{di}{dt}=0.04\times5000e^{-500t}=200e^{-500t}$ ✓.

**Answer:** $V_s=200\,\mathrm{V}$, $R=20\,\Omega$, $I_0=0$, $L=40\,\mathrm{mH}$.

</details>

**Problem: Problem 45 · W2 · RC natural response with a divider first · textbook P7.22** (intermediate)

The switch has been closed for a long time and opens at $t=0$. Find (a) $v(0)$, (b) $\tau$ for $t>0$, (c) $v(t)$, (d) the initial energy stored in the capacitor.

```schematic
I1 0,0 -> 0,3 "$7.5\,\mathrm{mA}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$80\,\mathrm{k\Omega}$"
R2 3,3 -> 6,3 "$20\,\mathrm{k\Omega}$"
S1 6,3 -> 9,3 "$t=0$" action=open
C1 9,3 -> 9,0 "$0.4\,\mu\mathrm{F}$" v="$v(t)$"
wire 9,3 -> 12,3
R3 12,3 -> 12,0 "$50\,\mathrm{k\Omega}$"
wire 12,0 -> 0,0
ground 0,0
```

<details><summary>Solution</summary>

1. **Type:** after the switch opens, only $C$ and $50\,\mathrm{k\Omega}$ are left, no source: RC **natural** response. Solve for $v$.
2. **Before:** $C$ is open, so the source current splits between $80\,\mathrm{k\Omega}$ and the $20+50=70\,\mathrm{k\Omega}$ path (current divider).

   $$i_{70}=7.5\,\mathrm{mA}\cdot\dfrac{80}{80+70}=4\,\mathrm{mA}$$
3. (a) $v$ is the voltage across $50\,\mathrm{k\Omega}$.

   $$v(0^-)=4\,\mathrm{mA}\times50\,\mathrm{k\Omega}=200\,\mathrm{V}=v(0^+)$$
4. (b) **After:** $C$ sees only $50\,\mathrm{k\Omega}$.

   $$\tau=RC=50\times10^3\times0.4\times10^{-6}=20\,\mathrm{ms}$$
5. (c) **Plug in** $x_f=0$, $\frac1\tau=50\,\mathrm{s^{-1}}$.

   $$v(t)=200e^{-50t}\,\mathrm{V}$$
6. (d) **Energy.**

   $$w=\tfrac12Cv^2=\tfrac12(0.4\times10^{-6})(200)^2=8\,\mathrm{mJ}$$

**Answer:** (a) $200\,\mathrm{V}$. (b) $20\,\mathrm{ms}$. (c) $v(t)=200e^{-50t}\,\mathrm{V}$, $t\ge0$. (d) $8\,\mathrm{mJ}$.

</details>

**Problem: Problem 46 · W1–W2 · The sign of the reference arrow · textbook P7.1** (intermediate)

The switch has been closed for a long time and opens at $t=0$. Note the direction of $i$ (**up** through the inductor). Find (a) the initial value of $i$, (b) the initial energy stored in the inductor, (c) the time constant for $t>0$, (d) the numerical expression for $i(t)$, $t\ge0$.

```schematic
V1 0,3 -> 0,0 "$120\,\mathrm{V}$"
R1 0,3 -> 3,3 "$3\,\Omega$"
R2 3,3 -> 3,0 "$30\,\Omega$"
R3 3,3 -> 6,3 "$6\,\Omega$"
S1 6,3 -> 9,3 "$t=0$" action=open
L1 9,0 -> 9,3 "$8\,\mathrm{mH}$" i="$i$"
wire 9,3 -> 12,3
R4 12,3 -> 12,0 "$2\,\Omega$"
wire 12,0 -> 0,0
ground 0,0
```

<details><summary>Solution</summary>

1. **Type:** after the switch opens, only $L$ and $2\,\Omega$ are left, no source: RL **natural** response. Solve for $i$.
2. **Before:** $L$ is a short, which also shorts the $2\,\Omega$. The source sees $3\,\Omega$ in series with $30\parallel6=5\,\Omega$.

   $$I=\dfrac{120}{3+5}=15\,\mathrm{A}$$
3. The middle node is at $120-15\times3=75\,\mathrm{V}$, so $75/6=12.5\,\mathrm{A}$ flows right through $6\,\Omega$ and then **down** through $L$.
4. (a) The arrow points **up**, against the real current, so the value is negative.

   $$i(0^-)=i(0^+)=-12.5\,\mathrm{A}$$
5. (b) **Energy** (the sign doesn’t matter: $i$ is squared).

   $$w=\tfrac12(8\times10^{-3})(12.5)^2=0.625\,\mathrm{J}$$
6. (c) **After:** $L$ sees only $2\,\Omega$.

   $$\tau=\dfrac{L}{R}=\dfrac{8\times10^{-3}}{2}=4\,\mathrm{ms}$$
7. (d) **Plug in** $x_0=-12.5$, $x_f=0$, $\frac1\tau=250$.

   $$i(t)=-12.5e^{-250t}\,\mathrm{A}$$

**Answer:** (a) $-12.5\,\mathrm{A}$. (b) $0.625\,\mathrm{J}$. (c) $4\,\mathrm{ms}$. (d) $i(t)=-12.5e^{-250t}\,\mathrm{A}$, $t\ge0$.

</details>

**Problem: Problem 47 · W2 · Step response that needs a Thévenin equivalent · textbook P7.52(a)** (advanced)

The switch has been in position $a$ for a long time. At $t=0$ it moves to position $b$ and stays there. Find the initial and final values of the capacitor voltage, the time constant for $t\ge0$, and $v_C(t)$ for $t\ge0$. (The $200\,\mathrm{V}$ source has its $-$ on top. The two $t=0$ switches are one two-position switch: at $t=0$ the contact at $a$ opens and the contact at $b$ closes.)

```schematic
V1 0,3 -> 0,0 "$120\,\mathrm{V}$"
R1 0,3 -> 2,3 "$10\,\mathrm{k\Omega}$"
S1 2,3 -> 4,3 "$t=0$" action=open
C1 4,3 -> 4,0 "$40\,\mathrm{nF}$" v="$v_C$" i="$i$"
S2 4,3 -> 6,3 "$t=0$" action=close
R2 6,3 -> 8,3 "$12.5\,\mathrm{k\Omega}$"
R3 8,3 -> 8,0 "$150\,\mathrm{k\Omega}$"
R4 8,3 -> 10,3 "$50\,\mathrm{k\Omega}$"
V2 10,0 -> 10,3 "$200\,\mathrm{V}$"
wire 10,0 -> 0,0
label 2,3 "$a$" above
label 6,3 "$b$" above
ground 0,0
```

<details><summary>Solution</summary>

1. **Type:** one capacitor, a DC source after the switch: RC **step** response. Solve for $v_C$.
2. **Before (position $a$):** $C$ is open, so no current flows through $10\,\mathrm{k\Omega}$: the capacitor holds the full source.

   $$v_C(0^-)=120\,\mathrm{V}=v_C(0^+)$$
3. **After (position $b$):** replace everything right of $b$ by its Thévenin equivalent. With $C$ removed, no current flows in $12.5\,\mathrm{k\Omega}$; the divider gives the node voltage (the source’s top is at $-200\,\mathrm{V}$).

   $$V_{th}=-200\cdot\dfrac{150}{150+50}=-150\,\mathrm{V}$$
4. Sources off (the $200\,\mathrm{V}$ source becomes a short): $12.5\,\mathrm{k\Omega}$ plus $150\parallel50$.

   $$R_{th}=12.5+37.5=50\,\mathrm{k\Omega}$$
5. **Final value and time constant:** $C$ ends at $V_{th}$.

   $$\begin{gathered}v_f=-150\,\mathrm{V}, \\ \tau=(50\times10^{3})(40\times10^{-9})=2\,\mathrm{ms}\end{gathered}$$
6. **Plug in:** $x_0-x_f=120-(-150)=270$, $\frac1\tau=500$.

   $$v_C(t)=-150+270e^{-500t}\,\mathrm{V}$$

**Answer:** $v_C(0)=120\,\mathrm{V}$, $v_C(\infty)=-150\,\mathrm{V}$, $\tau=2\,\mathrm{ms}$, $v_C(t)=-150+270e^{-500t}\,\mathrm{V}$, $t\ge0$.

</details>

### D2 · RLC circuits (second order)

[Week 5 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/0c7a77fe-aeed-47a8-b1c3-4967d73eea21#d5ad9ba9-0ec5-4b62-acf5-b1c7e17d6463)

**When the circuit has one inductor and one capacitor** (after combining), its equation is **second order**. The math is [B5](#b5) (and [B6](#b6) when a source stays on). The new part is getting the equation and the two starting values from the circuit.

Before anything, find the starting values with the switching recipe in [Topic D](#topic-d): $v_C(0^+)$ and $i_L(0^+)$ carry over from just before the switch.

**The two circuits you will meet:**

```schematic
V1 0,3 -> 0,0 "$V_s$"
R1 0,3 -> 3,3 "$R$" i="$i$"
L1 3,3 -> 6,3 "$L$"
C1 6,3 -> 6,0 "$C$" v="$v_C$"
wire 6,0 -> 0,0
ground 0,0
```

```schematic
C1 0,3 -> 0,0 "$C$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$L$" i="$i_L$"
wire 3,3 -> 6,3
R1 6,3 -> 6,0 "$R$" i="$i_R$"
wire 6,0 -> 0,0
ground 0,0
```

|  | Series | Parallel |
|---|---|---|
| Unknown | $v_C$ (or the loop current $i$) | the common voltage $v$ |
| Equation | $v_C^{\prime\prime}+\dfrac{R}{L}v_C^{\prime}+\dfrac{1}{LC}v_C=\dfrac{V_s}{LC}$ | $v^{\prime\prime}+\dfrac{1}{RC}v^{\prime}+\dfrac{1}{LC}v=0$ |
| Damping $\alpha$ | $\dfrac{R}{2L}$ | $\dfrac{1}{2RC}$ |
| Natural frequency $\omega_0$ | $\dfrac{1}{\sqrt{LC}}$ | $\dfrac{1}{\sqrt{LC}}$ (the same) |
| Starting value | $v_C(0^+)=v_C(0^-)$ | $v(0^+)=v_C(0^-)$ |
| Starting slope | $v_C^{\prime}(0^+)=\dfrac{i(0^+)}{C}$, with $i=i_L$ entering the $+$ of $C$ | $v^{\prime}(0^+)=\dfrac{i_C(0^+)}{C}$, with $i_C(0^+)$ from KCL |

Both equations have the shape below, so the characteristic equation and its roots are:

$$s^2+2\alpha s+\omega_0^2=0$$

$$s=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}$$

**Compare $\alpha$ with $\omega_0$ to know the shape before solving.** These are the three root cases of [B5](#b5) with circuit names:

| Compare | Roots | Name | Form of the response |
|---|---|---|---|
| $\alpha>\omega_0$ | two real | **overdamped** | $A_1e^{s_1t}+A_2e^{s_2t}$ |
| $\alpha=\omega_0$ | one repeated | **critically damped** | $(A_1+A_2t)e^{-\alpha t}$ |
| $\alpha<\omega_0$ | $-\alpha\pm j\omega_d$ | **underdamped** | $e^{-\alpha t}(B_1\cos\omega_dt+B_2\sin\omega_dt)$ |
| $\alpha=0$ (no $R$) | $\pm j\omega_0$ | **undamped** (LC) | $B_1\cos\omega_0t+B_2\sin\omega_0t$ |

Here $\omega_d=\sqrt{\omega_0^2-\alpha^2}$ is the **damped frequency**: how fast an underdamped response oscillates.

```graph
title "Slide R through the three cases (series RLC, $L=1\,\mathrm{H}$, $C=0.25\,\mathrm{F}$)"
x 0 6 label="$t$ (s)"
y -8 11 label="$v_C$ (V)"
slider R 0 10 1 step=0.1 label="$R$ ($\Omega$)" animate
let a "R/2"
let wd "sqrt(abs(4-a^2))"
let s1 "-a+wd"
let s2 "-a-wd"
curve "if(abs(a-2)<0.001, 10*(1+2*t)*exp(-2*t), if(a<2, 10*exp(-a*t)*(cos(wd*t)+a/wd*sin(wd*t)), 10*(s2*exp(s1*t)-s1*exp(s2*t))/(s2-s1)))" label="$v_C(t)$, from $10\,\mathrm{V}$ with $i=0$" color=1
hline "0"
readout "$\alpha=R/2L$" "a"
readout "$\omega_0=1/\sqrt{LC}$" "2"
caption "$\omega_0=2$ is fixed. $R<4$: $\alpha<\omega_0$, underdamped (it swings below zero). $R=4$: critically damped, the fastest return without overshoot. $R>4$: overdamped, a slow creep back. $R=0$: undamped, it never dies out."
```

**With a source that stays on** (a step response), the answer is a **final value** plus a part that dies out. The final value comes from the DC steady state ($C$ open, $L$ short): it is the constant $y_p$ of [B6](#b6). Fit the constants to $v_C=V_f+(\text{transient})$, not to the transient alone.

**Method:**

1. **Before:** DC steady state for $t<0$ gives $v_C(0^-)$ and $i_L(0^-)$.
2. **Starting values:** $v_C(0^+)=v_C(0^-)$, $i_L(0^+)=i_L(0^-)$, then the starting slope (table above).
3. **Equation:** series or parallel? Compute $\alpha$ and $\omega_0$; compare them to pick the form.
4. **Final value:** $0$ with no source; otherwise the DC steady state after the switch.
5. **Constants:** use the starting value and slope on the full expression (product rule for the slope).

> **Warning:** **Units.** Convert $\mathrm{mH}$, $\mathrm{mF}$, $\mu\mathrm{F}$, $\mathrm{nF}$ to H and F before computing $\alpha$ and $\omega_0$. $1\,\mathrm{nF}=10^{-9}\,\mathrm{F}$, $1\,\mu\mathrm{F}=10^{-6}\,\mathrm{F}$, $1\,\mathrm{mH}=10^{-3}\,\mathrm{H}$.

> **Info:** **Bonus (skip-safe): where the series equation comes from.** KVL around the loop, then replace the current by $Cv_C^{\prime}$:
> 
> ```steps
> $$ V_s=Ri+Li^{\prime}+v_C $$
> KVL: the three element voltages add up to the source.
> $$ i=\hl{Cv_C^{\prime}} $$
> The loop current is the capacitor current.
> $$ V_s=RC\,v_C^{\prime}+LC\,v_C^{\prime\prime}+v_C $$
> Substitute the current and its derivative.
> $$ v_C^{\prime\prime}+\hl{\dfrac RL}v_C^{\prime}+\hl{\dfrac1{LC}}v_C=\hl{\dfrac{V_s}{LC}} $$
> Divide by $LC$.
> ```
> 
> For the parallel circuit, KCL at the top node is $Cv^{\prime}+i_L+\dfrac vR=0$. Differentiate once and use $i_L^{\prime}=\dfrac vL$.

**Example: Example 10 · W5 · A series step response · textbook P8.53**

The circuit has been in operation for a long time with $V_s=200\,\mathrm{V}$. At $t=0$ the source drops to $100\,\mathrm{V}$. Find $v_C(t)$ for $t\ge0$.

```schematic
V1 0,3 -> 0,0 "$200\to100\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$" i="$i$"
L1 3,3 -> 6,3 "$40\,\mathrm{mH}$"
C1 6,3 -> 6,0 "$10\,\mathrm{mF}$" v="$v_C$"
wire 6,0 -> 0,0
ground 0,0
```

1. **Type:** one $L$, one $C$ in one loop with a source that stays on: series RLC step response.
2. **Before:** DC steady state, $C$ open so $i=0$. No drop on $R$ or $L$, so $C$ holds the old source voltage.

   $$v_C(0^-)=200\,\mathrm{V},\quad i(0^-)=0$$
3. **Starting values:** both carry over. The slope is $i/C$.

   $$v_C(0^+)=200,\quad v_C'(0^+)=\dfrac{0}{0.01}=0$$
4. **Equation:** $\alpha=\frac{4}{2(0.04)}=50$, $\omega_0=\frac{1}{\sqrt{0.04\times0.01}}=50$. Equal: critically damped.

   $$v_C''+100v_C'+2500v_C=250000$$
5. **Final value:** new DC steady state, $C$ open again, so $v_C\to100\,\mathrm{V}$. Write final value + repeated-root transient.

   $$v_C=100+(A_1+A_2t)e^{-50t}$$
6. **Constants:** the value gives $A_1$.

   $$100+A_1=200\ \Rightarrow\ A_1=100$$
7. The slope (product rule) gives $A_2$.

   $$A_2-50A_1=0\ \Rightarrow\ A_2=5000$$

**Answer:** $v_C=100+(100+5000t)e^{-50t}\,\mathrm{V}$, $t\ge0$ ($t$ in seconds). It starts at 200 V, flat, and settles at 100 V without overshoot.

**Problem: Problem 48 · W5 · No resistor: an ideal LC circuit · textbook P8.14** (introductory)

$C=250\,\mathrm{mF}$ and $L=0.4\,\mathrm{H}$ are in parallel. Initially $v(0)=0$ and $i_L(0)=-3\,\mathrm{A}$ (reference downward). Find (a) $v(t)$, (b) its frequency in rad/s, (c) its maximum amplitude.

```schematic
C1 0,3 -> 0,0 "$250\,\mathrm{mF}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$0.4\,\mathrm{H}$" i="$i_L$"
wire 3,0 -> 0,0
ground 0,0
```

<details><summary>Solution</summary>

1. **Type:** parallel, no $R$: $\alpha=0$, undamped.

   $$v''+\dfrac{1}{LC}v=v''+10v=0$$
2. **Form:** $\omega_0=\sqrt{10}$; the cosine term is zero because $v(0)=0$.

   $$v=B\sin(\sqrt{10}\,t)$$
3. **Starting slope:** KCL $i_C+i_L=0$, so $i_C(0^+)=3\,\mathrm{A}$ downward.

   $$v'(0^+)=\dfrac{3}{0.25}=12\,\mathrm{V/s}$$
4. **Constant:** $v^{\prime}(0)=\sqrt{10}\,B=12$.

   $$B=\dfrac{12}{\sqrt{10}}\approx3.795$$

**Answer:** (a) $v=\dfrac{12}{\sqrt{10}}\sin(\sqrt{10}\,t)\,\mathrm{V}$. (b) $\omega_0=\sqrt{10}\approx3.162\,\mathrm{rad/s}$. (c) $3.795\,\mathrm{V}$; with no $R$ it never decays.

</details>

**Problem: Problem 49 · W5 · Read the circuit back from its response · textbook P8.3** (introductory)

In a parallel RLC circuit, $C=50\,\mathrm{nF}$ and the voltage is $v=-5e^{-5000t}+20e^{-20000t}\,\mathrm{V}$ for $t\ge0$. Find $\alpha$, $\omega_0$, $L$ and $R$.

```schematic
C1 0,3 -> 0,0 "$50\,\mathrm{nF}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$L$" i="$i_L$"
wire 3,3 -> 6,3
R1 6,3 -> 6,0 "$R$" i="$i_R$"
wire 6,0 -> 0,0
ground 0,0
```

<details><summary>Solution</summary>

1. **Type:** two decaying exponentials = overdamped. The exponents are the roots $s_1=-5000$, $s_2=-20000$.
2. **Roots → equation:** $s^2+2\alpha s+\omega_0^2=(s+5000)(s+20000)$. Compare: $2\alpha$ is the sum, $\omega_0^2$ the product.

   $$s^2+25000s+10^8=0$$
3. So $\alpha=12500\,\mathrm{s^{-1}}$ and $\omega_0=10^4\,\mathrm{rad/s}$.
4. $\omega_0^2=\dfrac{1}{LC}$ gives $L$.

   $$L=\dfrac{1}{10^8\times50\times10^{-9}}=0.2\,\mathrm{H}$$
5. Parallel: $\alpha=\dfrac{1}{2RC}$ gives $R$.

   $$R=\dfrac{1}{2(12500)(50\times10^{-9})}=800\,\Omega$$

**Answer:** $\alpha=12500\,\mathrm{s^{-1}}$, $\omega_0=10^4\,\mathrm{rad/s}$, $L=0.2\,\mathrm{H}$, $R=800\,\Omega$.

</details>

**Problem: Problem 50 · W5 · Switch to a series loop · textbook P8.44** (intermediate)

The switch has been in position $a$ for a long time. At $t=0$ it moves to $b$. Find $i(t)$ for $t\ge0$.

```schematic
V1 0,3 -> 0,0 "$70\,\mathrm{V}$"
R1 0,3 -> 3,3 "$50\,\Omega$"
S1 3,3 -> 6,3 "$t=0$" action=open
C1 6,3 -> 6,0 "$200\,\mathrm{nF}$" v="$v_C$"
S2 6,3 -> 9,3 "$t=0$" action=close
R2 9,3 -> 12,3 "$200\,\Omega$" i="$i$"
L1 12,3 -> 12,0 "$100\,\mathrm{mH}$"
wire 12,0 -> 0,0
ground 0,0
label 3,3 "$a$" above
label 9,3 "$b$" above
```

<details><summary>Solution</summary>

1. **Type:** after the switch, $C$, $200\,\Omega$ and $L$ form one loop with no source: series RLC natural response.
2. **Before:** in position $a$, $C$ is open in steady state, so no current in $50\,\Omega$ and $C$ charges to the source. $L$ is disconnected.

   $$v_C(0^-)=70\,\mathrm{V},\quad i(0^-)=0$$
3. **Starting slope:** KVL round the new loop, $v_C=Ri+L\,i^{\prime}$, at $0^+$.

   $$i'(0^+)=\dfrac{70-200(0)}{0.1}=700\,\mathrm{A/s}$$
4. **Equation:** $\alpha=\dfrac{200}{2(0.1)}=1000$, $\omega_0^2=\dfrac{1}{0.1\times200\times10^{-9}}=5\times10^7$. $\alpha<\omega_0$: underdamped.

   $$\omega_d=\sqrt{5\times10^7-10^6}=7000\,\mathrm{rad/s}$$
5. **Form:** $i(0)=0$ removes the cosine.

   $$i=B\,e^{-1000t}\sin7000t$$
6. **Constant:** at $t=0$ the slope is $7000B=700$.

   $$B=0.1$$

**Answer:** $i=0.1\,e^{-1000t}\sin7000t\ \mathrm{A}$ $=100\,e^{-1000t}\sin7000t\ \mathrm{mA}$, $t\ge0$.

</details>

**Problem: Problem 51 · W5 · The slope comes from KCL · textbook P8.7** (intermediate)

$R=\tfrac{12500}{3}\,\Omega$, $L=250\,\mathrm{mH}$, $C=10\,\mathrm{nF}$ in parallel. Initially $v(0)=90\,\mathrm{V}$ and $i_L(0)=-30\,\mathrm{mA}$ (references as drawn). Find $v(t)$ for $t\ge0$.

```schematic
C1 0,3 -> 0,0 "$10\,\mathrm{nF}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$250\,\mathrm{mH}$" i="$i_L$"
wire 3,3 -> 6,3
R1 6,3 -> 6,0 "$\tfrac{12500}{3}\,\Omega$" i="$i_R$"
wire 6,0 -> 0,0
ground 0,0
```

<details><summary>Solution</summary>

1. **Type:** parallel RLC, no source: natural response.
2. **Starting slope:** $i_R=\dfrac{90}{12500/3}=21.6\,\mathrm{mA}$. KCL $i_C+i_L+i_R=0$.

   $$i_C(0^+)=30-21.6=8.4\,\mathrm{mA}$$
3. Divide by $C$.

   $$v'(0^+)=\dfrac{8.4\times10^{-3}}{10^{-8}}=8.4\times10^5\,\mathrm{V/s}$$
4. **Equation:** $\alpha=\dfrac{1}{2RC}=12000$, $\omega_0=\dfrac{1}{\sqrt{LC}}=20000$. $\alpha<\omega_0$: underdamped.

   $$\omega_d=\sqrt{20000^2-12000^2}=16000$$
5. **Form** with $v(0)=90$ as the cosine coefficient.

   $$v=e^{-12000t}(90\cos16000t+B_2\sin16000t)$$
6. **Constant:** slope at 0 is $-\alpha(90)+\omega_dB_2$.

   $$-12000(90)+16000B_2=840000\ \Rightarrow\ B_2=120$$

**Answer:** $v=e^{-12000t}(90\cos16000t+120\sin16000t)\,\mathrm{V}$, $t\ge0$.

</details>

**Problem: Problem 52 · W5 · Choose R for critical damping · textbook P8.42** (advanced)

$R$ is adjusted for critical damping. At the moment the switch closes, $v_C=90\,\mathrm{V}$ and the inductor current is $i=24\,\mathrm{mA}$. Find (a) $R$, (b) $i$ and $\dfrac{di}{dt}$ just after closing, (c) $i(t)$ and $v_C(t)$ for $t\ge0$.

```schematic
C1 0,3 -> 0,0 "$160\,\mathrm{nF}$" v="$v_C$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$R$" i="$i$"
L1 6,3 -> 6,0 "$250\,\mathrm{mH}$"
wire 6,0 -> 0,0
ground 0,0
```

<details><summary>Solution</summary>

1. **Type:** one loop, no source: series RLC natural response. Critical means $\alpha=\omega_0$.
2. **(a)** $\omega_0=\dfrac{1}{\sqrt{0.25\times160\times10^{-9}}}=5000$. Set $\dfrac{R}{2L}=5000$.

   $$R=2(0.25)(5000)=2500\,\Omega$$
3. **(b)** $i$ is an inductor current, so it carries over. KVL round the loop: $v_C=Ri+L\,i^{\prime}$.

   $$i'(0^+)=\dfrac{90-2500(0.024)}{0.25}=120\,\mathrm{A/s}$$
4. **(c) Form:** repeated root $-5000$.

   $$i=(A_1+A_2t)e^{-5000t}$$
5. **Constants:** $A_1=i(0)=0.024$; slope $A_2-5000A_1=120$.

   $$A_2=240$$
6. Then $v_C=Ri+L\,i^{\prime}$ (or check: $i=-C\,v_C^{\prime}$, since $i$ leaves the $+$ of $C$).

   $$v_C=(90+3\times10^5\,t)e^{-5000t}$$

**Answer:** (a) $R=2500\,\Omega$. (b) $i(0^+)=24\,\mathrm{mA}$, $i^{\prime}(0^+)=120\,\mathrm{A/s}$. (c) $i=(0.024+240t)e^{-5000t}\,\mathrm{A}$, $v_C=(90+3\times10^5t)e^{-5000t}\,\mathrm{V}$.

</details>

**Problem: Problem 53 · W5 + W6 · The answer is zero · textbook P8.24** (advanced)

The switch has been open a long time; the capacitor is uncharged. At $t=0$ it closes. Find $v_o(t)$ for $t\ge0$.

```schematic
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 3,3 "$400\,\Omega$"
L1 3,3 -> 3,0 "$1.25\,\mathrm{H}$" i="$i_L$"
S1 3,3 -> 6,3 "$t=0$" action=close
C1 6,3 -> 6,0 "$1.25\,\mu\mathrm{F}$" v="$v_o$"
wire 6,0 -> 0,0
ground 0,0
```

<details><summary>Solution</summary>

1. **Type:** after closing, $L$ and $C$ share the top node, fed through $400\,\Omega$: a parallel RLC with a DC source.
2. **Before:** $L$ is a short in steady state, so it carries all the source current; $C$ is disconnected and uncharged.

   $$i_L(0^-)=\dfrac{12}{400}=30\,\mathrm{mA},\quad v_o(0^-)=0$$
3. **Starting slope:** at $0^+$, $v_o=0$ so the $400\,\Omega$ still carries $30\,\mathrm{mA}$, and all of it goes into $L$. KCL leaves nothing for $C$.

   $$i_C(0^+)=30-30=0\ \Rightarrow\ v_o^{\prime}(0^+)=0$$
4. **Equation:** KCL $\dfrac{v_o-12}{400}+i_L+Cv_o^{\prime}=0$. Differentiating removes the constant 12, so the equation is homogeneous.

   $$Cv_o''+\dfrac{v_o'}{400}+\dfrac{v_o}{L}=0$$
5. **Condition:** a homogeneous linear equation with $v_o(0)=0$ and $v_o^{\prime}(0)=0$ has only the zero solution (the zero-start rule in [Topic C](#topic-c)).

**Answer:** $v_o(t)=0$ for all $t\ge0$. The inductor already carries the whole source current, so nothing ever flows into the capacitor.

</details>
