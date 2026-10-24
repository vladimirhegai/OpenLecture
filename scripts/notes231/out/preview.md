# [preview] Midterm sections head, a, b0, b1, b2

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

- → $g(t)$: a part with only $t$ in it
- → $h(y)$: a part with only $y$ in it

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

- → $a(t)$: the coefficient of $y$: everything multiplying $y$, **sign included**
- → $f(t)$: the forcing: everything left over, with no $y$ in it

Examples:

- $y^{\prime}=t-y$ → move $y$ left: $y^{\prime}+y=t$. So $a(t)=1$, $f(t)=t$.
- $ty^{\prime}+2y=t^2$ → divide by $t$: $y^{\prime}+\frac2t\,y=t$. So $a(t)=\frac2t$, $f(t)=t$.
- $y^{\prime}=(8t+3)y$ → $y^{\prime}-(8t+3)y=0$. So $a(t)=-(8t+3)$, $f(t)=0$.

> **Warning:** Get $y^{\prime}$ **alone** first (coefficient 1). Read $a(t)$ only after dividing: in $ty^{\prime}+2y=t^2$, $a(t)$ is $\frac2t$, not $2$.

**The integrating factor.** An integrating factor is a special function $\mu(t)$ that we multiply the entire equation by, to turn its left side into **one derivative**. The formula is:

$$\mu(t)=e^{\int a(t)\,dt}$$

After multiplying by $\mu$, the left side is exactly $(\mu y)^{\prime}$, so the equation becomes:

$$\begin{gathered}\dfrac{d}{dt}\big(\mu\,y\big)=\mu\,f \\ \Longrightarrow \\ \mu\,y=\int\mu\,f\,dt+C\end{gathered}$$

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
