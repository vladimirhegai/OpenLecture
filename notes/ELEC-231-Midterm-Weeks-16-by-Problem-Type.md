# ELEC 231 Midterm: Weeks 1–6 by Problem Type

## Start here: what the midterm asks

**Midterm:** Friday Oct 30 · 2 hours · 30 marks · Weeks 1–6 · Casio 991 only.

Every solution in this note uses the same three moves. Use them on the exam too. Naming the type first is what tells you which method to use.

1. **Type:** say what kind of problem it is, and the clue that told you. Example: “$y^{\prime}=t^2y$ is separable: the right side is a $t$-part times a $y$-part.”
2. **Method:** do the numbered steps from that section.
3. **Conditions:** plug in the given values to find the constants. Example: $y=Ce^{2t}$ with $y(0)=5$ gives $C=5$. (In a circuit, the values come from the circuit just before the switch moves.)

**Where do I go?** Find what your question gives you in the left column, then click the link. The browser’s Back button brings you back here.

| The question gives you… | Go to | Weeks |
|---|---|---|
| a complex number to convert, multiply, divide, raise to a power or take roots of | [Topic A](#topic-a) | 1 |
| an ODE to classify, or a function to check as a solution | [Topic B](#topic-b) | 2 |
| a first-order ODE where you can split the $y$’s from the $t$’s | [B1 · Separable](#b1) | 3 |
| $y^{\prime}+a(t)\,y=f(t)$ | [B2 · Integrating factor](#b2) | 3 |
| $M\,dt+N\,dy=0$ | [B3 · Exact](#b3), [B4 · Make it exact](#b4) | 4 |
| $ay^{\prime\prime}+by^{\prime}+cy=0$ (numbers $a,b,c$) | [B5 · Characteristic equation](#b5) | 4–5 |
| $ay^{\prime\prime}+by^{\prime}+cy=g(t)$ | [B6 · Undetermined coefficients](#b6) | 6 |
| a second-order ODE with $t$ in the coefficients, and one solution given | [B7 · Reduction of order](#b7) | 6 |
| “does a unique solution exist?”, an interval, or two solutions to compare | [Topic C](#topic-c) | 3, 5, 6 |
| a circuit with a switch: find $v(t)$ or $i(t)$ | [Topic D](#topic-d) | 1–3, 5 |

## Topic A: Complex numbers

[Week 1 · Topic 1](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/1cbac07a-cd02-48c2-8c30-c9829c4e06b2#079a564f-840a-46b1-9f12-5d8d123edad9) [Week 1 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/1cbac07a-cd02-48c2-8c30-c9829c4e06b2#fef2e73f-cd85-498c-9b6a-1ff1e058d7d3)

Complex numbers show up in two places on the midterm:

- **On their own:** convert, divide, raise to a power, take roots.
- **Inside [B5](#b5):** when a characteristic equation has no real roots, you need things like $\sqrt{-36}=j6$.

**One number, two ways to write it.** Think of a complex number as an arrow from the origin. You can say where its tip is (how far right, how far up), or how long it is and which way it points:

$$z=a+jb=c\,e^{j\theta}=c\angle\theta$$

- $a=\mathrm{Re}\{z\}$ = the **real part**: how far right
- $b=\mathrm{Im}\{z\}$ = the **imaginary part**: how far up
- $c=|z|$ = the **magnitude**: how long the arrow is
- $\theta=\angle z$ = the **angle**: measured from the positive real axis, counter-clockwise
- $j=\sqrt{-1}$, so $j^2=-1$ (this course writes $j$, not $i$)

Example: $3+j4$ is 3 right and 4 up. Its length is $c=\sqrt{9+16}=5$ and its angle is $\theta=\tan^{-1}(4/3)=53.13^\circ$, so $3+j4=5\angle53.13^\circ$.

Why two forms? Adding is easy in $a+jb$. Multiplying, dividing and powers are easy in $c\angle\theta$.

**Polar → rectangular.** The arrow is the long side of a right triangle, so use cos and sin:

$$a=c\cos\theta,\quad b=c\sin\theta$$

Example: $2\angle30^\circ=2\cos30^\circ+j\,2\sin30^\circ=\sqrt3+j$.

**Rectangular → polar.** Pythagoras gives the length, $\tan^{-1}$ gives the angle:

$$c=\sqrt{a^2+b^2},\quad \theta=\tan^{-1}\!\left(\dfrac{b}{a}\right)$$

Example: the $3+j4=5\angle53.13^\circ$ above. But watch the quadrant:

> **Warning:** **The quadrant trap.** The calculator’s $\tan^{-1}$ only gives angles between $-90^\circ$ and $90^\circ$, i.e. arrows pointing right. If $a<0$, your arrow points left, so **add $180^\circ$** to what the calculator says. Example: $-1+j$ points up-left. The calculator gives $\tan^{-1}(1/{-1})=-45^\circ$, but the real angle is $-45^\circ+180^\circ=135^\circ$.

**Arithmetic: pick the form that makes the job easy.**

- **Add or subtract → rectangular.** Add the real parts, add the imaginary parts: $(1+j2)+(3-j5)=4-j3$.
- **Multiply → polar.** Multiply the lengths, add the angles: $2\angle30^\circ\times3\angle40^\circ=6\angle70^\circ$.
- **Divide → polar.** Divide the lengths, subtract the angles: $\dfrac{6\angle70^\circ}{3\angle40^\circ}=2\angle30^\circ$.
- **Power → polar** (de Moivre). Length to the power, angle times the power: $(2\angle30^\circ)^3=8\angle90^\circ$.
- **Divide → rectangular** (if both are given that way). Multiply top and bottom by the **conjugate** of the bottom, $(a+jb)^*=a-jb$: $\dfrac{1}{1+j}=\dfrac{1-j}{(1+j)(1-j)}=\dfrac{1-j}{2}$.

Why the conjugate works: $(a+jb)(a-jb)=a^2+b^2$ is a plain real number, so the bottom stops being complex.

Powers of $j$ repeat every four: $j^2=-1$, $j^3=j^2\cdot j=-j$, $j^4=(j^2)^2=1$. And $\dfrac1j=\dfrac{j}{j\cdot j}=-j$.

**Roots: a $k$-th root question always has $k$ answers.** Write $z$ in polar form, then use:

$$z^{1/k}=c^{1/k}\angle\dfrac{\theta+360^\circ\ell}{k},\quad \ell=0,1,\dots,k-1$$

- All $k$ roots have the **same length**, $c^{1/k}$.
- The first one is at angle $\theta/k$.
- Each next one is $360^\circ/k$ further round the circle.

Example: the square roots of $4\angle60^\circ$ have length $\sqrt4=2$ and angles $30^\circ$ and $30^\circ+180^\circ=210^\circ$. So they are $2\angle30^\circ$ and $2\angle210^\circ$.

Why $k$ answers: $\theta$ and $\theta+360^\circ$ are the same arrow, but after you divide by $k$ they point different ways.

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
caption "Start: $z=2.5\angle90^\circ$, $k=3$. The roots have length $2.5^{1/3}$. The first is at $90^\circ/3=30^\circ$, the others $120^\circ$ apart."
```

> **Info:** **Bonus (skip-safe): why multiplying adds angles.** Write both numbers as exponentials and use $e^Ae^B=e^{A+B}$: $z_1z_2=c_1e^{j\theta_1}\,c_2e^{j\theta_2}=c_1c_2\,e^{j(\theta_1+\theta_2)}$. The two forms are linked by Euler’s identity, $e^{j\theta}=\cos\theta+j\sin\theta$. The lecture uses it to get trig identities for free: expand $e^{jA}e^{jB}=e^{j(A+B)}$, and the real parts give $\cos(A+B)=\cos A\cos B-\sin A\sin B$.

> **Tip:** **Casio 991 check:** complex mode does $+,-,\times,\div$ and can show the answer as $r\angle\theta$. Use it to check your answer, but write the steps: the marks are for the working.

**Example: Example 1 · W1 · All four fourth roots · lecture Example 1.2**

Find the fourth roots of $z=81e^{j60^\circ}$.

1. **Type:** roots ($k=4$). The number is already polar: $c=81$, $\theta=60^\circ$.
2. **Length and first angle:** $81^{1/4}=3$, and $60^\circ/4=15^\circ$.
3. **Spacing:** $360^\circ/4=90^\circ$, so keep adding $90^\circ$.

   $$z^{1/4}=3\angle(15^\circ+90^\circ\ell),\quad \ell=0,1,2,3$$

**Answer:** $3\angle15^\circ,\ 3\angle105^\circ,\ 3\angle195^\circ,\ 3\angle285^\circ$.

**Problem: Problem 1 · W1 · Convert, watching the quadrant** (introductory)

Write (a) $-3+j4$ and (b) $-3-j4$ in polar form.

<details><summary>Solution</summary>

1. **Type:** rectangular → polar. Both have $a<0$ (they point left), so the $180^\circ$ fix applies.
2. **Length:** the same for both.

   $$c=\sqrt{(-3)^2+4^2}=5$$
3. **Angle (a):** the calculator gives $\tan^{-1}(4/{-3})=-53.13^\circ$. The arrow points up-left (quadrant II), so add $180^\circ$.

   $$\theta=126.87^\circ$$
4. **Angle (b):** the calculator gives $\tan^{-1}(-4/{-3})=53.13^\circ$. The arrow points down-left (quadrant III), so add $180^\circ$.

   $$\theta=233.13^\circ\ \ (=-126.87^\circ)$$

**Answer:** (a) $5\angle126.87^\circ$. (b) $5\angle233.13^\circ$, the same as $5\angle-126.87^\circ$.

</details>

**Problem: Problem 2 · W1 · Divide in rectangular form · lecture Example 1.1** (introductory)

Compute $\dfrac{80+j18}{8+j10}$. Give the answer in rectangular and polar form.

<details><summary>Solution</summary>

1. **Type:** dividing two rectangular numbers. Multiply top and bottom by the conjugate of the bottom, $8-j10$.

   $$\dfrac{(80+j18)(8-j10)}{(8+j10)(8-j10)}$$
2. **Multiply out:** the bottom is $8^2+10^2=164$. On top, expand and use $j^2=-1$.

   $$(640+180)+j(144-800)=820-j656$$
3. **Divide** both parts by 164.

   $$5-j4$$
4. **Polar:** $a>0$, $b<0$ points down-right (quadrant IV), so the calculator angle is already right.

   $$\sqrt{41}\angle-38.66^\circ$$

**Answer:** $5-j4=\sqrt{41}\angle-38.66^\circ\approx6.40\angle-38.66^\circ$.

</details>

**Problem: Problem 3 · W1 · A high power** (intermediate)

Compute $(1+j)^8$.

<details><summary>Solution</summary>

1. **Type:** a power, so go polar first: $c=\sqrt2$, $\theta=45^\circ$.

   $$1+j=\sqrt2\angle45^\circ$$
2. **de Moivre:** length to the 8th, angle times 8.

   $$(\sqrt2)^8\angle360^\circ=16\angle0^\circ$$

**Answer:** $(1+j)^8=16$.

</details>

**Problem: Problem 4 · W1 · Cube roots of a negative number** (intermediate)

Find all three cube roots of $-8$, in polar and rectangular form.

<details><summary>Solution</summary>

1. **Type:** roots ($k=3$). Go polar first: $-8$ points straight left.

   $$-8=8\angle180^\circ$$
2. **Roots:** length $8^{1/3}=2$, first angle $180^\circ/3=60^\circ$, spacing $360^\circ/3=120^\circ$.

   $$2\angle60^\circ,\quad 2\angle180^\circ,\quad 2\angle300^\circ$$
3. **Rectangular:** $a=2\cos\theta$, $b=2\sin\theta$.

   $$1+j\sqrt3,\quad -2,\quad 1-j\sqrt3$$

**Answer:** $2\angle60^\circ=1+j\sqrt3$, $2\angle180^\circ=-2$, $2\angle300^\circ=1-j\sqrt3$. The real root $-2$ is only one of three.

</details>

**Problem: Problem 5 · W1 + W5 · The complex roots of a quadratic** (intermediate)

Solve $s^2+4s+13=0$. (This is exactly the step you meet in [B5](#b5).)

<details><summary>Solution</summary>

1. **Type:** a quadratic with $b^2-4ac<0$, so the roots are complex.

   $$s=\dfrac{-4\pm\sqrt{16-52}}{2}=\dfrac{-4\pm\sqrt{-36}}{2}$$
2. **Root of a negative:** $\sqrt{-36}=\sqrt{36}\,\sqrt{-1}=j6$.

   $$s=\dfrac{-4\pm j6}{2}$$

**Answer:** $s=-2\pm j3$: a conjugate pair (same real part, opposite imaginary parts).

</details>

## Topic B: Find the general solution

[Week 2 · Topic 1](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/08d203f6-a2b5-41b9-adfd-a14e22fb03d8#68929800-f011-4be7-a85a-29543465ed52) [Week 2 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/08d203f6-a2b5-41b9-adfd-a14e22fb03d8#49e5b3a7-1038-4f16-a4cc-2170fbbd61dc)

This is the core of the midterm. You get an ODE (ordinary differential equation) and you have to find $y(t)$.

There are seven methods, B1–B7. Which one you use depends only on **what the equation looks like**. So the first move is always to name the equation.

**Step 1: name it.** Ask these five questions:

| Label | Question | Yes, like… | No, like… |
|---|---|---|---|
| **Order** | What is the highest derivative? | $y^{\prime\prime}+y=0$: 2nd | — |
| **Linear** | Is every $y$, $y^{\prime}$, $y^{\prime\prime}$ to the power 1, on its own? (No $y^2$, $yy^{\prime}$, $\sin y$. $t$ can be anywhere.) | $ty^{\prime\prime}+y=0$ | $y^{\prime}=y^2$ |
| **Homogeneous** | Move every $y$ term to the left. Is the right side $0$? | $y^{\prime\prime}+4y=0$ | $y^{\prime\prime}+4y=8$ |
| **Constant coefficients** | Are the things in front of $y$, $y^{\prime}$, $y^{\prime\prime}$ just numbers? | $y^{\prime\prime}+3y^{\prime}+2y=0$ | $ty^{\prime\prime}+y=0$ |
| **Autonomous** | Is there no $t$ anywhere? | $y^{\prime}=3y$ | $y^{\prime}=t-y$ |

**Step 2: pick the method.** Look at the **order** first. 1st-order and 2nd-order equations use completely different methods.

**1st order** (the highest derivative is $y^{\prime}$). Check these in order and stop at the first one that fits:

| Check | Method | Go to |
|---|---|---|
| 1. Can you split it into a $t$-part times a $y$-part? | separate the variables | [B1](#b1) |
| 2. Is it linear? | integrating factor | [B2](#b2) |
| 3. Neither? Write it as $M\,dt+N\,dy=0$. Is it exact? | exact equation | [B3](#b3) |
| 4. Not exact? | make it exact first | [B4](#b4) |

**1. Separable** → [B1](#b1). The right side is a $t$-part **times** a $y$-part:

$$\dfrac{dy}{dt}=g(t)\,h(y)$$

- **Example:** $y^{\prime}=t^2y$. Here $g=t^2$ and $h=y$.
- **Method:** get all the $y$’s on one side and all the $t$’s on the other, then integrate both sides: $\dfrac{dy}{y}=t^2\,dt$.
- **Autonomous equations are always separable.** $y^{\prime}=3y$ has no $t$ at all, so you can always write $\dfrac{dy}{3y}=dt$.

**2. Linear** → [B2](#b2). You can’t split it, but $y$ and $y^{\prime}$ only appear to the power 1:

$$y^{\prime}+a(t)\,y=f(t)$$

- **Example:** $y^{\prime}+y=t$. Here $a=1$ and $f=t$.
- **Why not B1?** $y^{\prime}=t-y$ is a $t$ **plus** a $y$, and a sum can’t be split into a product.
- **Method:** multiply everything by $\mu=e^{\int a\,dt}$ (here $e^t$). The left side becomes one derivative, $(e^ty)^{\prime}$, so you can integrate.

**3. Exact** → [B3](#b3). Not separable, not linear. Write it with $dt$ and $dy$:

$$M\,dt+N\,dy=0$$

- **Example:** $(t-y)\,dt-(t+y)\,dy=0$. Here $M=t-y$ and $N=-(t+y)$.
- **Test:** take $\dfrac{\partial M}{\partial y}=-1$ and $\dfrac{\partial N}{\partial t}=-1$. They match, so it’s exact.
- **Method:** find one function $U(t,y)$ whose $t$-derivative is $M$ and whose $y$-derivative is $N$. The answer is $U=C$.

**4. Not exact** → [B4](#b4). Same form, but the test fails:

- **Example:** $y\,dt+(3+3t-y)\,dy=0$. Here $\dfrac{\partial M}{\partial y}=1$ but $\dfrac{\partial N}{\partial t}=3$. No match.
- **Method:** multiply the whole equation by a factor that fixes the mismatch (here $y^2$). Now it passes the test, so finish it like B3.

**2nd order** (the highest derivative is $y^{\prime\prime}$). In Weeks 1–6 these are all **linear**, so you only ask two questions:

1. Are the things in front of $y^{\prime\prime}$, $y^{\prime}$, $y$ just **numbers**?
2. Is the **right side $0$**?

| In front of $y$ | Right side $0$ | Right side $g(t)$ |
|---|---|---|
| **Numbers in front** | [B5](#b5) characteristic equation | [B6](#b6) undetermined coefficients |
| **$t$ in front** | [B7](#b7) reduction of order | not in Weeks 1–6 |

**Numbers in front, right side 0** → [B5](#b5).

$$a\,y^{\prime\prime}+b\,y^{\prime}+c\,y=0$$

- **Example:** $y^{\prime\prime}+3y^{\prime}+2y=0$.
- **Method:** guess $y=e^{st}$. That turns the ODE into $s^2+3s+2=0$, so $s=-1$ or $s=-2$, and $y=Ae^{-t}+Be^{-2t}$.
- **Why it works:** every derivative of $e^{st}$ is still $e^{st}$ times a number. So $e^{st}$ cancels and you’re left with a plain quadratic in $s$.

**Numbers in front, right side not 0** → [B6](#b6).

$$a\,y^{\prime\prime}+b\,y^{\prime}+c\,y=g(t)$$

- **Example:** $y^{\prime\prime}+3y^{\prime}+2y=4$.
- **Method:** first solve the version with $0$ on the right (B5): $y_c=c_1e^{-t}+c_2e^{-2t}$. Then guess a $y_p$ that looks like $g(t)$. Here $g=4$ is a constant, so guess $y_p=A$: $2A=4$, $A=2$.
- **Answer:** add them. $y=c_1e^{-t}+c_2e^{-2t}+2$.
- **Why two pieces?** $y_c$ always gives $0$ on the left side. You need one extra piece, $y_p$, that gives the $4$.

**$t$ in front, right side 0** → [B7](#b7).

$$y^{\prime\prime}+p(t)\,y^{\prime}+q(t)\,y=0$$

- **Example:** $y^{\prime\prime}-t\,y^{\prime}+y=0$, and the question gives you one solution, $y_1=t$.
- **Why not B5?** With $t$ in front, the $e^{st}$ guess no longer cancels. So you need that given $y_1$.
- **Method:** guess $y=y_1\,v=t\,v$. After substituting, you get $t\,v^{\prime\prime}+(2-t^2)\,v^{\prime}=0$. Set $z=v^{\prime}$ and it’s a 1st-order equation (separable, B1).

> **Tip:** **Where does “autonomous” matter?** Only for 1st order: no $t$ means separable. For 2nd order, ignore it.

**Step 3: fix the constants.** Every method gives a **general solution**: a formula with unknown constants in it.

- 1st order → one constant, $C$. One condition, like $y(1)=2$, pins it down.
- 2nd order → two constants, $c_1$ and $c_2$. You need two conditions, usually $y(0)$ and $y^{\prime}(0)$.
- A problem that gives you conditions is called an **initial value problem** (IVP). Plug the conditions into the general solution and solve for the constants.

**Checking a solution** (Week 2 asks this). Plug $y$ and its derivatives into the ODE. If both sides match for **every** $t$, it’s a solution.

Example: is $y=e^{-2t}$ a solution of $y^{\prime}+2y=0$? $\;-2e^{-2t}+2e^{-2t}=0$ ✓. Yes.

**Problem: Problem 6 · W2 · Name it, then route it · lecture Example 2.1 and others** (introductory)

For each equation, give its order, and say whether it is linear, homogeneous, constant-coefficient and autonomous. Then say which method (B1–B7) solves it.

(a) $t^3y^{\prime\prime}+e^ty^{\prime}+y=0$

(b) $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$

(c) $y^{\prime\prime}+2y^{\prime}+5y=10$

(d) $\dfrac{di}{dt}+5i=50$

(e) $(t-y)\,dt-(t+y)\,dy=0$

<details><summary>Solution</summary>

1. (a) Highest derivative is $y^{\prime\prime}$, so 2nd order. Every $y$ is to the power 1, so linear. Right side is $0$, so homogeneous. But $t^3$ and $e^t$ are in front, not numbers. That’s the “$t$ in front” case → [B7](#b7) (once they give you one solution).
2. (b) $y^2$ is not power 1, so nonlinear. But it splits: $\frac{1}{t^3}\cdot y^2$ is a $t$-part times a $y$-part → [B1](#b1).
3. (c) 2nd order, linear, numbers in front. Right side is $10$, not $0$ → [B6](#b6).
4. (d) 1st order, linear ($a=5$, $f=50$) → [B2](#b2). It has no $t$, so it’s also autonomous, and B1 works too: $\frac{di}{50-5i}=dt$.
5. (e) Solve for $y^{\prime}$: $y^{\prime}=\frac{t-y}{t+y}$. $y$ is in a denominator, so nonlinear, and it won’t split. Test $M=t-y$, $N=-(t+y)$: both partials are $-1$ → exact, [B3](#b3).

**Answer:** (a) B7. (b) B1. (c) B6. (d) B2 (or B1). (e) B3.

</details>

**Problem: Problem 7 · W2 · Check, then pick the member that fits** (introductory)

Which of $y=t^2$, $\;y=t^2+1$, $\;y=5t^2$ solve $ty^{\prime}-2y=0$? Which one also satisfies $y(1)=5$?

<details><summary>Solution</summary>

1. **Type:** checking solutions. Plug each one in and see if you get $0$.
2. $y=t^2$: $y^{\prime}=2t$.

   $$t(2t)-2t^2=0\ \checkmark$$
3. $y=t^2+1$: $y^{\prime}=2t$.

   $$t(2t)-2(t^2+1)=-2\neq0\ \times$$
4. $y=5t^2$: $y^{\prime}=10t$.

   $$t(10t)-2(5t^2)=0\ \checkmark$$
5. **Condition:** at $t=1$, $t^2=1$ and $5t^2=5$. Only $5t^2$ gives $5$.

**Answer:** $t^2$ and $5t^2$ are solutions (both are $Ct^2$); $t^2+1$ is not. Only $y=5t^2$ satisfies $y(1)=5$.

</details>

### B1 · Separable equations

[Week 3 · Topic 1](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/3d1ae4a9-687d-4654-873d-be3439faea2f#c40cdedd-01db-45b4-9498-4c4929ba8f49)

**Start here: can you pull the $y$’s and the $t$’s apart?** If every $y$ can go on one side and every $t$ on the other, you just integrate each side. That kind of equation is called **separable**.

It looks like this:

$$\dfrac{dy}{dt}=g(t)\,h(y)$$

- $g(t)$ = a piece with only $t$ in it
- $h(y)$ = a piece with only $y$ in it

Reading the form:

- $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$ → separable: $g=\dfrac{1}{t^3}$, $h=y^2$.
- $\dfrac{dy}{dt}=3y$ → separable: $g=3$, $h=y$. No $t$ at all is fine.
- $\dfrac{dy}{dt}=t+y$ → **not** separable. A sum won’t split into a product, so go to [B2](#b2).
- $t^{-3}\,dt+y\,dy=0$ → already separated: only $t$ sits with $dt$, only $y$ sits with $dy$.

Why it works: once it reads $\dfrac{dy}{h(y)}=g(t)\,dt$, each side has only one letter, so you can integrate each side on its own.

**The method:**

$$\int\dfrac{dy}{h(y)}=\int g(t)\,dt+C$$

1. **Separate:** divide by $h(y)$ and multiply by $dt$, so you get $\dfrac{dy}{h(y)}=g(t)\,dt$.
2. **Integrate** both sides. Write just one constant $C$, on the $t$ side.
3. **Condition:** plug in the given point to find $C$.
4. **Solve for $y$** if you can. If you can’t, an implicit answer like $y^2+3=6(t^2+1)$ is a full answer.

```steps
title "The method on dy/dt = 2ty, y(0) = 3"
$$ \dfrac{dy}{dt}=2t\,y $$
Separable: $g=2t$, $h=y$.
$$ \hl{\dfrac{dy}{y}}=\hl{2t\,dt} $$
**Separate:** divide by $y$, multiply by $dt$.
$$ \ln|y|=t^2+\hl{C} $$
**Integrate** each side. One constant, on the $t$ side.
$$ \ln3=0+C\;\Rightarrow\;\hl{C=\ln3} $$
**Condition** $y(0)=3$.
$$ |y|=e^{t^2+\ln3}=\hl{3e^{t^2}} $$
**Solve for $y$:** raise $e$ to both sides, and use $e^{a+b}=e^a\,e^b$.
$$ \hl{y}=3e^{t^2} $$
$y(0)=3$ is positive, so take the $+$ sign.
```

**Calculus you need here:**

| Integral | Result | Note |
|---|---|---|
| $\int t^n\,dt$ | $\dfrac{t^{n+1}}{n+1}$ | any $n\neq-1$, e.g. $\int t^{-3}dt=-\dfrac{1}{2t^2}$ |
| $\int \dfrac1y\,dy$ | $\ln|y|$ | the $n=-1$ case |
| $\int \dfrac{f^{\prime}(t)}{f(t)}\,dt$ | $\ln|f(t)|$ | top = derivative of bottom, e.g. $\int\dfrac{t}{t^2+1}dt=\dfrac12\ln(t^2+1)$ |
| $\int e^{at}\,dt$ | $\dfrac{1}{a}e^{at}$ | e.g. $\int e^{2t}dt=\dfrac12e^{2t}$ |
| undo $\ln$ | $e^{\ln A}=A$ | $e^{C}$ is just a new constant |
| combine logs | $k\ln A+\ln B=\ln(A^kB)$ | e.g. $3\ln A+\ln B=\ln(A^3B)$ |

> **Warning:** **Dividing by $h(y)$ can lose a solution.** If $h(y_0)=0$ for some number $y_0$, the flat line $y=y_0$ is a solution too. You can’t divide by zero, so the separated answer skips it.
> 
> Example: in $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$, $h=y^2$ is zero at $y=0$. And $y=0$ works ($0=0$), so list it next to your answer.

> **Info:** **Bonus (skip-safe): why can you move $dy$ and $dt$ around like fractions?** Divide by $h$: $\dfrac{1}{h(y)}\dfrac{dy}{dt}=g(t)$. Now integrate both sides with respect to $t$. The chain rule says $\int\dfrac{1}{h(y)}\dfrac{dy}{dt}\,dt=\int\dfrac{1}{h(y)}\,dy$. Moving “$dt$” across is a shortcut for exactly this.

**Example: Example 2 · W3 · Separate after factoring · lecture Example 3.3**

Solve $\dfrac{dy}{dt}=\dfrac{3t+ty^2}{y+t^2y}$, $\;y(1)=3$.

1. **Type:** pull $t$ out of the top and $y$ out of the bottom. Now it’s a $t$-piece times a $y$-piece, so it’s separable.

   $$\dfrac{dy}{dt}=\dfrac{t(3+y^2)}{y(1+t^2)}$$
2. **Separate:** everything with $y$ goes with $dy$, everything with $t$ goes with $dt$.

   $$\dfrac{y}{3+y^2}\,dy=\dfrac{t}{1+t^2}\,dt$$
3. **Integrate:** on each side the top is half the derivative of the bottom, so each side gives $\tfrac12\ln(\text{bottom})$.

   $$\tfrac12\ln(3+y^2)=\tfrac12\ln(1+t^2)+c$$
4. **Undo the $\ln$:** multiply by 2, then raise $e$ to both sides. $e^{2c}$ is just a new constant, $C_1$.

   $$3+y^2=C_1(1+t^2)$$
5. **Condition** $y(1)=3$: $\;3+9=C_1(2)$.

   $$C_1=6$$
6. **Solve for $y$.** Take the $+$ root, because $y(1)=3$ is positive.

   $$y^2=6t^2+3$$

**Answer:** $y^2+3=6(t^2+1)$, so $y=\sqrt{6t^2+3}$.

**Problem: Problem 8 · W3 · Separate and use a starting value · Pre-tutorial 3(a)** (introductory)

Solve $\dfrac{dy}{dt}=-\dfrac{t}{y}$, $\;y=2$ when $t=1$.

<details><summary>Solution</summary>

1. **Type:** $-\dfrac{t}{y}=(-t)\cdot\dfrac1y$, a $t$-piece times a $y$-piece. Separable.
2. **Separate:** multiply both sides by $y\,dt$.

   $$y\,dy=-t\,dt$$
3. **Integrate** each side.

   $$\dfrac{y^2}{2}=-\dfrac{t^2}{2}+C$$
4. **Condition:** $\frac{4}{2}=-\frac12+C$, so $C=\frac52$. Then multiply by 2.

   $$t^2+y^2=5$$
5. **Solve for $y$.** Keep the $+$ root, since $y(1)=2$ is positive.

   $$y=\sqrt{5-t^2}$$

**Answer:** $y=\sqrt{5-t^2}$. It’s the top half of the circle $t^2+y^2=5$, so it only exists for $-\sqrt5<t<\sqrt5$.

</details>

**Problem: Problem 9 · W3 · A general solution with a power · lecture Example 3.2** (introductory)

Find the general solution of $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$.

<details><summary>Solution</summary>

1. **Type:** $\dfrac{y^2}{t^3}=\dfrac{1}{t^3}\cdot y^2$, so separable with $g=t^{-3}$, $h=y^2$.
2. **Separate:** divide by $y^2$, multiply by $dt$.

   $$y^{-2}\,dy=t^{-3}\,dt$$
3. **Integrate** with the power rule ($n=-2$ on the left, $n=-3$ on the right).

   $$-y^{-1}=-\tfrac12t^{-2}+C$$
4. **Solve for $y$:** multiply by $-1$ (and call $-C$ just $C$ again), then flip both sides.

   $$\dfrac1y=\dfrac{1}{2t^2}+C\quad\Rightarrow\quad y=\dfrac{2t^2}{1+2Ct^2}$$

**Answer:** $y=\dfrac{2t^2}{1+2Ct^2}$, plus $y=0$. We divided by $y^2$, which skips $y=0$ (see the warning above).

</details>

**Problem: Problem 10 · W3 · An exponential of y** (intermediate)

Solve $\dfrac{dy}{dt}=2t\,e^{-y}$, $\;y(0)=0$.

<details><summary>Solution</summary>

1. **Type:** $2t\cdot e^{-y}$ is a $t$-piece times a $y$-piece. Separable.
2. **Separate:** dividing by $e^{-y}$ is the same as multiplying by $e^{y}$.

   $$e^{y}\,dy=2t\,dt$$
3. **Integrate** each side.

   $$e^{y}=t^2+C$$
4. **Condition:** $e^0=0+C$, so $C=1$.

   $$e^{y}=t^2+1$$
5. **Solve for $y$:** take $\ln$ of both sides.

   $$y=\ln(t^2+1)$$

**Answer:** $y=\ln(t^2+1)$.

</details>

**Problem: Problem 11 · W3 · Differential form · Pre-tutorial 3(b)** (intermediate)

Solve $3t(y^2+1)\,dt+y(t^2+2)\,dy=0$.

<details><summary>Solution</summary>

1. **Type:** each term is a $t$-piece times a $y$-piece. Separable.
2. **Separate:** divide every term by $(y^2+1)(t^2+2)$. Now only $t$ sits with $dt$ and only $y$ with $dy$.

   $$\dfrac{3t}{t^2+2}\,dt+\dfrac{y}{y^2+1}\,dy=0$$
3. **Integrate:** both are “top = derivative of bottom”, times $\frac32$ and $\frac12$.

   $$\tfrac32\ln(t^2+2)+\tfrac12\ln(y^2+1)=c$$
4. Multiply by 2, then combine the logs: $3\ln A+\ln B=\ln(A^3B)$.

   $$\ln\!\big[(t^2+2)^3(y^2+1)\big]=2c$$
5. **Undo the $\ln$:** raise $e$ to both sides. $e^{2c}$ is a new constant $C$.

   $$(t^2+2)^3(y^2+1)=C$$

**Answer:** $(t^2+2)^3(y^2+1)=C$, with $C>0$. This implicit form is a full answer.

</details>

**Problem: Problem 12 · W3 · Collect before separating · lecture Example 3.4** (advanced)

Solve $y\,dt+(t^3y^2+t^3)\,dy=0$.

<details><summary>Solution</summary>

1. **Type:** the $dy$ term has a common factor: $t^3y^2+t^3=t^3(y^2+1)$. So each term is a $t$-piece times a $y$-piece. Separable.
2. **Separate:** divide every term by $t^3y$.

   $$t^{-3}\,dt+\dfrac{y^2+1}{y}\,dy=0$$
3. Split the fraction so each part is easy to integrate: $\dfrac{y^2+1}{y}=y+\dfrac1y$.

   $$\int t^{-3}\,dt+\int\left(y+\dfrac1y\right)dy=C$$
4. **Integrate** each part.

   $$-\dfrac{1}{2t^2}+\dfrac{y^2}{2}+\ln|y|=C$$
5. Multiply by 2 to clear the fractions (call $2C$ the new constant $C_1$).

   $$y^2+2\ln|y|-t^{-2}=C_1$$

**Answer:** $y^2+2\ln|y|-t^{-2}=C_1$ (implicit), plus $y=0$, which we skipped by dividing by $y$.

</details>

### B2 · Linear equations: the integrating factor

[Week 3 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/3d1ae4a9-687d-4654-873d-be3439faea2f#a43fc96e-8dc5-4a1e-bfdf-bf1acf01f98b)

**What if you can’t separate the variables?** Take $y^{\prime}=t-y$. The right side is a sum, so it won’t split into a $t$-piece times a $y$-piece, and [B1](#b1) fails.

But it is **linear**: $y$ and $y^{\prime}$ show up only to the first power (no $y^2$, no $\sin y$). Every linear equation can be solved with an **integrating factor**.

First get it into this shape:

$$\dfrac{dy}{dt}+a(t)\,y=f(t)$$

- $a(t)$ = whatever multiplies $y$, **sign included**
- $f(t)$ = everything else, the part with no $y$ in it (called the forcing)

Reading the form:

- $y^{\prime}=t-y$ → move $y$ left: $y^{\prime}+y=t$. So $a=1$, $f=t$.
- $ty^{\prime}+2y=t^2$ → divide by $t$: $y^{\prime}+\frac2t\,y=t$. So $a=\frac2t$, $f=t$.
- $y^{\prime}=(8t+3)y$ → move it left: $y^{\prime}-(8t+3)y=0$. So $a=-(8t+3)$, $f=0$.

> **Warning:** **Get $y^{\prime}$ alone first.** The number in front of $y^{\prime}$ must be 1 before you read $a(t)$. Example: in $ty^{\prime}+2y=t^2$, divide by $t$ first. Then $a(t)=\frac2t$, not $2$.

**The trick.** Multiply the whole equation by a function $\mu(t)$, called the **integrating factor**:

$$\mu(t)=e^{\int a(t)\,dt}$$

Example: $y^{\prime}+2y=4$ has $a=2$, so $\mu=e^{\int2\,dt}=e^{2t}$.

Why: after you multiply by this $\mu$, the left side is exactly one derivative, $(\mu y)^{\prime}$ (the product rule backwards). So the equation becomes:

$$\dfrac{d}{dt}\big(\mu\,y\big)=\mu\,f$$

A single derivative is easy to undo. Integrate both sides:

$$\mu\,y=\int\mu\,f\,dt+C$$

**The method:**

1. **Standard form:** get $y^{\prime}$ alone, then read $a(t)$ and $f(t)$.
2. **Integrating factor:** $\mu=e^{\int a\,dt}$. No $+C$ in this integral: any one $\mu$ works.
3. **Rewrite:** the equation becomes $(\mu y)^{\prime}=\mu f$.
4. **Integrate:** $\mu y=\int\mu f\,dt+C$. This is where the $+C$ goes. Don’t forget it.
5. **Divide by $\mu$** to get $y$, then use the condition to find $C$.

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
| $e^{\int\frac{k}{t}dt}$ | $e^{k\ln t}=t^k$ | for $t>0$, e.g. $a=\frac2t$ gives $\mu=t^2$; $a=-\frac1t$ gives $\mu=\frac1t$ |
| $\int(2t+5)^5\,dt$ | $\dfrac{(2t+5)^6}{12}$ | substitution $u=2t+5$, $du=2\,dt$ |
| $\int t\,e^{t}\,dt$ | $(t-1)\,e^{t}$ | integration by parts; check by differentiating |
| $\int t\,e^{t^2}dt$ | $\tfrac12e^{t^2}$ | substitution $u=t^2$ |

> **Tip:** **Shortcut when $a=k$ and $f=F$ are both constants:** $\;y=\dfrac{F}{k}+Ce^{-kt}$. Example: $y^{\prime}+2y=4$ gives $y=2+Ce^{-2t}$, same as the stepper. Every RC and RL circuit equation has this shape (see [D1](#d1)).

> **Info:** **Bonus (skip-safe): why does the integrating factor work?** The product rule says $(\mu y)^{\prime}=\mu y^{\prime}+\mu^{\prime} y$. With $\mu=e^{\int a\,dt}$, the chain rule gives $\mu^{\prime}=a\,\mu$. So
> 
> $$
> (\mu y)^{\prime}=\mu y^{\prime}+a\mu y=\mu\,(y^{\prime}+ay)
> $$
> 
> That’s $\mu$ times the left side of your equation. So multiplying by $\mu$ is exactly what turns $y^{\prime}+ay$ into one derivative.

> **Info:** **Both separable and linear?** Some equations are both. Then either method works, and separating is usually faster.
> 
> **When $f=0$:** $y^{\prime}=(8t+3)y$ separates as $\dfrac{dy}{y}=(8t+3)\,dt$.
> 
> **When $a$ and $f$ are both constants:** $y^{\prime}+2y=4$ separates as $\dfrac{dy}{4-2y}=dt$.

**Example: Example 3 · W3 · A coefficient that varies with t · lecture Example 3.1**

Solve $\dfrac{dy}{dt}+\dfrac{10\,y}{2t+5}=10$, $\;y(0)=0$.

1. **Type:** linear, and $y^{\prime}$ is already alone. So $a(t)=\dfrac{10}{2t+5}$ and $f(t)=10$.
2. **Integrating factor:** $\int\frac{10}{2t+5}dt=5\ln(2t+5)$. Then $e^{5\ln(2t+5)}=(2t+5)^5$, same rule as $e^{k\ln t}=t^k$.

   $$\mu=(2t+5)^5$$
3. **Rewrite:** the left side is now one derivative, $(\mu y)^{\prime}=\mu f$.

   $$\dfrac{d}{dt}\big[(2t+5)^5y\big]=10(2t+5)^5$$
4. **Integrate** the right side with $u=2t+5$, $du=2\,dt$: $\;10\int u^5\frac{du}{2}=\frac56u^6$.

   $$(2t+5)^5y=\tfrac56(2t+5)^6+C$$
5. **Condition** $y(0)=0$: $\;0=\frac56\cdot5^6+C$.

   $$C=-\dfrac{5^7}{6}$$
6. **Divide** by $(2t+5)^5$.

   $$y=\tfrac56(2t+5)-\dfrac{5^7}{6(2t+5)^5}$$

**Answer:** $y=\dfrac56(2t+5)-\dfrac{5^7}{6(2t+5)^5}$.

**Problem: Problem 13 · W3 · The lecture’s RL equation · lecture §1.1** (introductory)

Solve $\dfrac{di}{dt}+5i=50$, $\;i(0)=0$ (the series RL circuit of the Week 3 lecture, $i$ in amperes).

<details><summary>Solution</summary>

1. **Type:** linear, with constant $a=5$ and $f=50$.
2. **Integrating factor:** $\mu=e^{5t}$. **Rewrite** the left side as one derivative.

   $$\mu=e^{5t},\qquad \big(e^{5t}i\big)^{\prime}=50e^{5t}$$
3. **Integrate:** $\int50e^{5t}dt=10e^{5t}$.

   $$e^{5t}i=10e^{5t}+C$$
4. **Condition:** $0=10+C$, so $C=-10$. Then divide by $e^{5t}$.

   $$i=10-10e^{-5t}$$

**Answer:** $i(t)=10(1-e^{-5t})\,\mathrm{A}$. It starts at 0 and climbs toward 10 A. The shortcut gives the 10 straight away: $F/k=50/5$.

</details>

**Problem: Problem 14 · W3 · Linear and separable: solve it both ways · Pre-tutorial 3(c)** (introductory)

Find the general solution of $\dfrac{dy}{dt}=8ty+3y$ with an integrating factor, then check it by separating.

<details><summary>Solution</summary>

1. **Type:** linear. Move the $y$ terms left: $y^{\prime}-(8t+3)y=0$. So $a=-(8t+3)$ and $f=0$.
2. **Integrating factor:** $\int-(8t+3)\,dt=-4t^2-3t$.

   $$\mu=e^{-4t^2-3t}$$
3. **Rewrite and integrate:** $f=0$, so the right side is 0 and integrates to just $C$.

   $$\big(\mu y\big)^{\prime}=0\quad\Rightarrow\quad e^{-4t^2-3t}y=C$$
4. **Divide** by $\mu$.

   $$y=Ce^{4t^2+3t}$$
5. **Check by separating:** $\dfrac{dy}{y}=(8t+3)\,dt$ gives $\ln|y|=4t^2+3t+c$. Raise $e$ to both sides: $y=Ce^{4t^2+3t}$, the same answer.

**Answer:** $y=Ce^{4t^2+3t}$.

</details>

**Problem: Problem 15 · W3 · An integral that needs parts** (intermediate)

Solve $y^{\prime}+y=t$, $\;y(0)=0$.

<details><summary>Solution</summary>

1. **Type:** linear, $a=1$, $f=t$. It doesn’t separate: $y^{\prime}=t-y$ is a sum.
2. **Integrating factor:** $\mu=e^{t}$. **Rewrite** the left side as one derivative.

   $$\mu=e^{t},\qquad\big(e^{t}y\big)^{\prime}=te^{t}$$
3. **Integrate** with the calculus table: $\int te^tdt=(t-1)e^t$.

   $$e^{t}y=(t-1)e^{t}+C$$
4. **Divide** by $e^t$.

   $$y=t-1+Ce^{-t}$$
5. **Condition:** $0=-1+C$, so $C=1$.

   $$y=t-1+e^{-t}$$

**Answer:** $y=t-1+e^{-t}$.

</details>

**Problem: Problem 16 · W3 · Divide first, then a power of t** (intermediate)

Solve $t\,y^{\prime}+2y=t^2$, $\;y(1)=0$, for $t>0$.

<details><summary>Solution</summary>

1. **Type:** linear. Divide by $t$ so $y^{\prime}$ is alone.

   $$y'+\dfrac{2}{t}\,y=t$$
2. **Integrating factor:** $e^{\int\frac2t dt}=e^{2\ln t}=t^2$. **Rewrite:** $(t^2y)^{\prime}=t^2\cdot t$.

   $$\big(t^2y\big)^{\prime}=t^3$$
3. **Integrate** each side.

   $$t^2y=\dfrac{t^4}{4}+C$$
4. **Condition:** $0=\frac14+C$, so $C=-\frac14$. Then divide by $t^2$.

   $$y=\dfrac{t^2}{4}-\dfrac{1}{4t^2}$$

**Answer:** $y=\dfrac{t^2}{4}-\dfrac{1}{4t^2}$.

</details>

**Problem: Problem 17 · W3 · An integrating factor with t²** (advanced)

Solve $y^{\prime}+2t\,y=t$, $\;y(0)=1$.

<details><summary>Solution</summary>

1. **Type:** linear, $a=2t$, $f=t$.
2. **Integrating factor:** $\int2t\,dt=t^2$, so $\mu=e^{t^2}$. **Rewrite** the left side as one derivative.

   $$\mu=e^{t^2},\qquad\big(e^{t^2}y\big)^{\prime}=te^{t^2}$$
3. **Integrate** with $u=t^2$: $\int te^{t^2}dt=\frac12e^{t^2}$.

   $$e^{t^2}y=\tfrac12e^{t^2}+C$$
4. **Divide** by $e^{t^2}$.

   $$y=\tfrac12+Ce^{-t^2}$$
5. **Condition:** $1=\frac12+C$, so $C=\frac12$.

   $$y=\tfrac12+\tfrac12e^{-t^2}$$

**Answer:** $y=\dfrac12\big(1+e^{-t^2}\big)$. It also separates, $y^{\prime}=t(1-2y)$, so you could check it with [B1](#b1).

</details>

### B3 · Exact equations

[Week 4 · Topic 1](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/ce2fa611-8b68-46a9-b6ca-653ae9c59aee#c9f71086-78d7-4bc3-a405-e0c6375fb6ca) [Week 4 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/ce2fa611-8b68-46a9-b6ca-653ae9c59aee#954310f2-d355-42ff-bd75-4e6b1d00f02d)

**What if it’s neither separable nor linear?** Take $y^{\prime}=\dfrac{t-y}{t+y}$. It won’t split into ($t$-part)×($y$-part), and $y$ sits in the bottom, so [B1](#b1) and [B2](#b2) both fail.

Some of these equations are **exact**. Then the answer is one formula in $t$ and $y$ set equal to a constant, $U(t,y)=C$, and you find $U$ by integrating.

**First, write it in $dt$, $dy$ form,** with everything on the left:

$$M(t,y)\,dt+N(t,y)\,dy=0$$

- $M$ = everything multiplying $dt$, **sign included**
- $N$ = everything multiplying $dy$, **sign included**

Examples:

- $3t\,dt+4y\,dy=0$ → already in form. $M=3t$, $N=4y$.
- $y^{\prime}=\dfrac{t-y}{t+y}$ → cross-multiply: $(t+y)\,dy=(t-y)\,dt$. Move it all left: $(t-y)\,dt-(t+y)\,dy=0$. So $M=t-y$, $N=-(t+y)$.
- $2ty\,y^{\prime}=t^2-y^2$ → $2ty\,dy=(t^2-y^2)\,dt$ → $(t^2-y^2)\,dt-2ty\,dy=0$. So $M=t^2-y^2$, $N=-2ty$.

> **Warning:** Moving the $dy$ term to the other side of the $=$ flips its sign. In $y^{\prime}=\frac{t-y}{t+y}$, $N$ is $-(t+y)$, not $t+y$. One wrong sign and the test below fails.

**Is it exact? Do the cross test.** Differentiate $M$ in $y$, and $N$ in $t$. If you get the same thing, it’s **exact**:

$$\dfrac{\partial M}{\partial y}=\dfrac{\partial N}{\partial t}$$

- $M_y$ = derivative of $M$ in $y$, treating $t$ like a number
- $N_t$ = derivative of $N$ in $t$, treating $y$ like a number

Example: $(2ty+3t^2)\,dt+t^2\,dy=0$ has $M_y=2t$ and $N_t=2t$. Same, so it’s exact.

**If it’s exact, find $U$.** $U$ is the function whose two partial derivatives are $M$ and $N$:

$$\dfrac{\partial U}{\partial t}=M,\quad \dfrac{\partial U}{\partial y}=N$$

and the general solution is

$$U(t,y)=C$$

Example: for the equation above, $U=t^2y+t^3$. Check: $U_t=2ty+3t^2=M$ and $U_y=t^2=N$. So the answer is $t^2y+t^3=C$.

Why $U=C$: $M\,dt+N\,dy$ is the small change in $U$. The equation sets that change to 0, so $U$ stays at one constant value.

**Method:**

1. **Rewrite:** everything on the left, $M\,dt+N\,dy=0$. Read $M$ and $N$ with their signs.
2. **Test:** is $M_y=N_t$? If not, it isn’t exact: go to [B4](#b4).
3. **Integrate $M$ in $t$**, treating $y$ like a number: $U=\int M\,dt+f(y)$. The “$+C$” becomes $f(y)$, because anything with only $y$ in it vanishes when you differentiate in $t$.
4. **Match $N$:** differentiate this $U$ in $y$ and set it equal to $N$. The $t$ terms cancel, leaving $f^{\prime}(y)$. Integrate it.
5. **Answer:** write $U(t,y)=C$. If you’re given a starting value, plug it in to find $C$.

**Calculus you need here: partial derivatives.** Differentiate in one letter and treat the other like a plain number:

| Expression | Result | Why |
|---|---|---|
| $\dfrac{\partial}{\partial t}(t^2y)$ | $2ty$ | $y$ acts like a number |
| $\dfrac{\partial}{\partial y}(t^2y)$ | $t^2$ | $t^2$ acts like a number |
| $\dfrac{\partial}{\partial y}(t-y)$ | $-1$ | $t$ is a constant, so it gives 0 |
| $\int(2ty+3t^2)\,dt$ | $t^2y+t^3+f(y)$ | $y$ acts like a number; the constant is $f(y)$ |

> **Info:** **Bonus (skip-safe): why the cross test works.** If $U$ exists, then $M=U_t$ and $N=U_y$. So $M_y$ is $U$ differentiated in $t$ then $y$, and $N_t$ is $U$ differentiated in $y$ then $t$. The order doesn’t change the result, so the two must match. The picture: each solution is a **level curve** $U(t,y)=C$ of the surface $z=U(t,y)$, like a contour line on a map.

Slide $C$: the plane at height $C$ cuts the surface along one solution curve (an ellipse). The same curve is drawn on the floor.

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

1. **Type:** already in $M\,dt+N\,dy=0$ form. $M=2ty+3t^2$, $N=t^2$.
2. **Test:** for $M_y$ treat $t$ as a number; for $N_t$ treat $y$ as a number. They match.

   $$M_y=2t=N_t\quad\checkmark$$
3. **Integrate $M$ in $t$** ($y$ is a number). The constant is $f(y)$.

   $$U=t^2y+t^3+f(y)$$
4. **Match $N$:** $U_y$ must equal $N=t^2$.

   $$t^2+f^{\prime}(y)=t^2\quad\Rightarrow\quad f^{\prime}(y)=0$$
5. **Answer:** $f$ is just a number, so it merges into $C$.

   $$t^2y+t^3=C$$

**Answer:** $t^2y+t^3=C$ (solved for $y$: $y=\dfrac{C-t^3}{t^2}$).

**Problem: Problem 18 · W4 · Test, then solve · lecture exercise (a)** (introductory)

Test $3t\,dt+4y\,dy=0$ for exactness, and if so, solve.

<details><summary>Solution</summary>

1. **Type:** already in form. $M=3t$, $N=4y$.
2. **Test:** $M$ has no $y$ and $N$ has no $t$, so both derivatives are 0.

   $$M_y=0=N_t\quad\checkmark$$
3. **Integrate $M$ in $t$.**

   $$U=\tfrac32t^2+f(y)$$
4. **Match $N$:** $U_y=f^{\prime}(y)$ must equal $4y$, so $f=2y^2$.

   $$U=\tfrac32t^2+2y^2$$
5. **Answer:** set $U=C$. Multiply by 2 to clear the fraction ($2C$ is still just a constant: call it $C$).

   $$3t^2+4y^2=C$$

**Answer:** Exact. $3t^2+4y^2=C$: ellipses, the curves in the graph above. (It’s also separable: $4y\,dy=-3t\,dt$.)

</details>

**Problem: Problem 19 · W4 · Test before you integrate · lecture exercise (d)** (introductory)

Is $y^{\prime}=\dfrac{t}{t+y}$ exact?

<details><summary>Solution</summary>

1. **Type:** a slope formula. Cross-multiply, $(t+y)\,dy=t\,dt$, then move everything left.

   $$t\,dt-(t+y)\,dy=0$$
2. **Read** $M=t$ and $N=-(t+y)$. The minus came from moving the $dy$ term left.
3. **Test:** $M$ has no $y$, so $M_y=0$. But $N_t=-1$.

   $$M_y=0,\qquad N_t=-1$$
4. **Answer:** $0\neq-1$, so it’s **not exact**. Next you’d try [B4](#b4), but neither ratio there works: the first still has both letters, the second has no $y$. The lecture stops at “not exact”.

   $$\frac{M_y-N_t}{N}=-\frac{1}{t+y},\quad \frac{N_t-M_y}{M}=-\frac1t$$

**Answer:** Not exact: $M_y=0\neq-1=N_t$.

</details>

**Problem: Problem 20 · W4 · Cross-multiply, then use a condition · lecture exercise (b)** (intermediate)

Solve $y^{\prime}=\dfrac{t-y}{t+y}$, $\;y(0)=1$.

<details><summary>Solution</summary>

1. **Type:** a slope formula. Cross-multiply, $(t+y)\,dy=(t-y)\,dt$, and move everything left.

   $$(t-y)\,dt-(t+y)\,dy=0$$
2. **Test:** $M=t-y$, $N=-t-y$.

   $$M_y=-1=N_t\quad\checkmark$$
3. **Integrate $M$ in $t$.**

   $$U=\tfrac12t^2-ty+f(y)$$
4. **Match $N$:** $U_y=-t+f^{\prime}(y)$ must equal $-t-y$. So $f^{\prime}=-y$ and $f=-\frac12y^2$.

   $$\tfrac12t^2-ty-\tfrac12y^2=C$$
5. Multiply by 2 to clear the fractions (call $2C$ just $C$ again).

   $$t^2-2ty-y^2=C$$
6. **Condition** $y(0)=1$: plug in $t=0$, $y=1$: $\;0-0-1=C$.

   $$C=-1$$

**Answer:** $t^2-2ty-y^2=-1$.

</details>

**Problem: Problem 21 · W4 · The sign trap · lecture exercise (c)** (intermediate)

Solve $2ty\,y^{\prime}=t^2-y^2$.

<details><summary>Solution</summary>

1. **Type:** write $y^{\prime}=\frac{dy}{dt}$ and multiply by $dt$: $2ty\,dy=(t^2-y^2)\,dt$. Moving $2ty\,dy$ left makes it **negative**.

   $$(t^2-y^2)\,dt-2ty\,dy=0$$
2. **Test:** $M=t^2-y^2$, $N=-2ty$.

   $$M_y=-2y=N_t\quad\checkmark$$
3. **Integrate $M$ in $t$.**

   $$U=\tfrac13t^3-ty^2+f(y)$$
4. **Match $N$:** $U_y=-2ty+f^{\prime}(y)$ must equal $-2ty$, so $f^{\prime}=0$.

   $$\tfrac13t^3-ty^2=C$$
5. Multiply by 3 to clear the fraction (call $3C$ just $C$ again).

   $$t^3-3ty^2=C$$

**Answer:** $t^3-3ty^2=C$. If you keep $+2ty\,dy$ (wrong sign), the test gives $-2y\neq2y$ and fails.

</details>

### B4 · Not exact: make it exact with an integrating factor

[Week 4 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/ce2fa611-8b68-46a9-b6ca-653ae9c59aee#ebb7e8ad-4fda-4034-97dc-a9c048d71335)

**What if the exactness test fails?** Take $y\,dt+(3+3t-y)\,dy=0$: $M_y=1$ but $N_t=3$, so [B3](#b3) can’t start.

The fix: multiply the whole equation by a function $\mu$, called an **integrating factor**, picked so the new equation passes the test. Then solve it with the [B3](#b3) steps. Same idea as in [B2](#b2): multiply by the right thing and the equation becomes easy.

**How to find $\mu$.** Start with the mismatch between the two cross derivatives:

$$M_y-N_t$$

In the example: $M_y-N_t=1-3=-2$. Now divide it, and see which case you’re in.

**Case 1: divide by $N$, and only $t$ is left.** (The lecture calls this Theorem 1.)

$$\dfrac{M_y-N_t}{N}=f(t)\quad\Rightarrow\quad \mu=e^{\int f(t)\,dt}$$

Example: $(t^2+y)\,dt-t\,dy=0$ gives $\frac{1-(-1)}{-t}=-\frac2t$. Only $t$, so $\mu=e^{\int-\frac2t\,dt}=\frac{1}{t^2}$.

**Case 2: flip the subtraction, divide by $M$, and only $y$ is left.** (Theorem 2.)

$$\dfrac{N_t-M_y}{M}=g(y)\quad\Rightarrow\quad \mu=e^{\int g(y)\,dy}$$

Example: $y\,dt+(3+3t-y)\,dy=0$ gives $\frac{3-1}{y}=\frac2y$. Only $y$, so $\mu=e^{\int\frac2y\,dy}=y^2$.

Why only one letter: $\mu$ will be a function of one letter, so the ratio you integrate to get it can only contain that letter. If neither ratio has just one letter, these two cases don’t help.

**Method:**

1. **Test:** check that $M_y\neq N_t$. (If they’re equal, it’s already exact: go to [B3](#b3).)
2. **Ratios:** compute both. Keep the one that has only one letter in it.
3. **Integrating factor:** $\mu=e^{\int f\,dt}$ or $\mu=e^{\int g\,dy}$. No $+C$ needed: any one $\mu$ works.
4. **Multiply the whole equation** by $\mu$: both $M$ and $N$.
5. **Re-test:** it must pass now (if not, recheck your algebra). Then solve with the [B3](#b3) steps.

**Calculus you need here** ($e$ and $\ln$ cancel: $e^{k\ln y}=y^k$):

| Expression | Result | Example |
|---|---|---|
| $e^{\int\frac{k}{y}dy}$ | $e^{k\ln|y|}=|y|^k$ | $g=\frac2y$ gives $\mu=y^2$; $g=-\frac1y$ gives $\mu=\frac1y$ |
| $e^{\int\frac{k}{t}dt}$ | $t^k$ | $f=-\frac2t$ gives $\mu=t^{-2}=\frac{1}{t^2}$ |
| $e^{\int k\,dt}$ | $e^{kt}$ | the ratio is a constant $k$ |

> **Info:** **Bonus (skip-safe): where Case 1 comes from.** Multiply by $\mu(t)$ and ask the new equation to pass the test, $(\mu M)_y=(\mu N)_t$. On the left, $\mu$ has no $y$, so it just comes out: $\mu M_y$. On the right, the product rule gives $\mu^{\prime} N+\mu N_t$. Rearrange:
> 
> $$
> \dfrac{\mu^{\prime}}{\mu}=\dfrac{M_y-N_t}{N}
> $$
> 
> The left side only has $t$ in it, so the right side must too. Then $\ln\mu=\int f\,dt$. Case 2 is the same argument with $\mu(y)$.

**Example: Example 5 · W4 · Repair, then finish · lecture exercise (e) and Pre-tutorial 4**

Solve $y\,dt+(3+3t-y)\,dy=0$.

1. **Type:** $M\,dt+N\,dy=0$ form, with $M=y$, $N=3+3t-y$.
2. **Test:** the two cross derivatives don’t match, so it’s not exact.

   $$M_y=1\neq3=N_t$$
3. **Ratios:** Case 1 gives $\frac{1-3}{3+3t-y}$, which has both letters. Case 2 leaves only $y$.

   $$\dfrac{N_t-M_y}{M}=\dfrac{3-1}{y}=\dfrac2y$$
4. **Integrating factor:** $e^{\int\frac2y dy}=e^{2\ln|y|}$.

   $$\mu=y^2$$
5. **Multiply the whole equation** by $y^2$.

   $$y^3\,dt+(3y^2+3ty^2-y^3)\,dy=0$$
6. **Re-test:** it passes now.

   $$M_y=3y^2=N_t\quad\checkmark$$
7. **Integrate $M$ in $t$** ($y$ is a number).

   $$U=ty^3+f(y)$$
8. **Match $N$:** $U_y=3ty^2+f^{\prime}(y)$ must equal $3y^2+3ty^2-y^3$. So $f^{\prime}=3y^2-y^3$.

   $$f(y)=y^3-\tfrac14y^4$$
9. **Answer:** set $U=C$.

   $$ty^3+y^3-\tfrac14y^4=C$$

**Answer:** $ty^3+y^3-\dfrac{y^4}{4}=C$.

**Problem: Problem 22 · W4 · A factor in t only** (introductory)

Solve $(t^2+y)\,dt-t\,dy=0$ for $t>0$.

<details><summary>Solution</summary>

1. **Type:** $M=t^2+y$, $N=-t$. **Test:** $M_y=1$, $N_t=-1$: not exact.
2. **Ratios:** Case 1 leaves only $t$.

   $$\dfrac{M_y-N_t}{N}=\dfrac{1-(-1)}{-t}=-\dfrac2t$$
3. **Integrating factor:** $e^{\int-\frac2t dt}=e^{-2\ln t}=t^{-2}$.

   $$\mu=\dfrac{1}{t^2}$$
4. **Multiply the whole equation** by $\frac{1}{t^2}$.

   $$\Big(1+\dfrac{y}{t^2}\Big)dt-\dfrac1t\,dy=0$$
5. **Re-test:** it passes now.

   $$M_y=\dfrac{1}{t^2}=N_t\quad\checkmark$$
6. **Integrate $M$ in $t$:** $\int1\,dt=t$, and $\int\frac{y}{t^2}dt=-\frac yt$ ($y$ is a number).

   $$U=t-\dfrac{y}{t}+f(y)$$
7. **Match $N$:** $U_y=-\frac1t+f^{\prime}$ must equal $-\frac1t$, so $f^{\prime}=0$.

   $$t-\dfrac yt=C$$

**Answer:** $t-\dfrac{y}{t}=C$, so $y=t^2-Ct$. Check with [B2](#b2): the equation is also linear, $y^{\prime}-\frac{y}{t}=t$, and gives the same family.

</details>

**Problem: Problem 23 · W4 · A factor in y only** (intermediate)

Solve $y\,dt+(2t+y^3)\,dy=0$.

<details><summary>Solution</summary>

1. **Type:** $M=y$, $N=2t+y^3$. **Test:** $M_y=1$, $N_t=2$: not exact.
2. **Ratios:** Case 1 gives $\frac{-1}{2t+y^3}$ (both letters). Case 2 leaves only $y$:

   $$\dfrac{N_t-M_y}{M}=\dfrac{2-1}{y}=\dfrac1y$$
3. **Integrating factor:** $e^{\int\frac1y dy}=e^{\ln|y|}$.

   $$\mu=y$$
4. **Multiply the whole equation** by $y$.

   $$y^2\,dt+(2ty+y^4)\,dy=0$$
5. **Re-test:** it passes now.

   $$M_y=2y=N_t\quad\checkmark$$
6. **Integrate $M$ in $t$.**

   $$U=ty^2+f(y)$$
7. **Match $N$:** $U_y=2ty+f^{\prime}$ must equal $2ty+y^4$. So $f^{\prime}=y^4$ and $f=\frac{y^5}{5}$.

   $$ty^2+\dfrac{y^5}{5}=C$$

**Answer:** $ty^2+\dfrac{y^5}{5}=C$.

</details>

**Problem: Problem 24 · W4 · Which case applies?** (advanced)

Find an integrating factor for each equation, then solve it.

(a) $(2y+3t)\,dt+t\,dy=0$

(b) $y^2\,dt+(ty+1)\,dy=0$

<details><summary>Solution</summary>

1. (a) **Test:** $M_y=2$, $N_t=1$, not exact. **Ratios:** Case 1 gives $\frac{2-1}{t}=\frac1t$, only $t$.

   $$\mu=e^{\int\frac1t dt}=t$$
2. (a) **Multiply** by $t$: you get exactly the B3 worked example.

   $$(2ty+3t^2)\,dt+t^2\,dy=0$$
3. (a) **Answer:** the solution from B3.

   $$t^2y+t^3=C$$
4. (b) **Test:** $M_y=2y$, $N_t=y$, not exact. **Ratios:** Case 1 gives $\frac{y}{ty+1}$ (both letters). Case 2:

   $$\dfrac{N_t-M_y}{M}=\dfrac{y-2y}{y^2}=-\dfrac1y$$
5. (b) **Integrating factor:** $e^{\int-\frac1y dy}=e^{-\ln|y|}$.

   $$\mu=\dfrac1y$$
6. (b) **Multiply** by $\frac1y$ and re-test: $M_y=1=N_t$, it passes.

   $$y\,dt+\Big(t+\dfrac1y\Big)dy=0$$
7. (b) **Integrate and match:** $U=ty+f(y)$. $U_y=t+f^{\prime}$ must equal $t+\frac1y$, so $f^{\prime}=\frac1y$ and $f=\ln|y|$.

   $$ty+\ln|y|=C$$

**Answer:** (a) $\mu=t$, $\;t^2y+t^3=C$. (b) $\mu=\dfrac1y$, $\;ty+\ln|y|=C$.

</details>

### B5 · Second order, constant coefficients: the characteristic equation

[Week 5 · Topic 1](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/0c7a77fe-aeed-47a8-b1c3-4967d73eea21#92fa557c-ab2a-49cb-a238-b9f4e76fa0b8)

**What if the equation has a $y^{\prime\prime}$ in it?** Like $y^{\prime\prime}+3y^{\prime}+2y=0$. If every coefficient is a plain number, there’s a shortcut: guess $y=e^{st}$.

Why that guess works: each derivative of $e^{st}$ is $e^{st}$ again, times one more $s$. So the whole ODE turns into a quadratic in $s$, and you already know how to solve those.

The equations this works on look like:

$$a\,y^{\prime\prime}+b\,y^{\prime}+c\,y=0$$

- $a,b,c$ = plain numbers, no $t$ in them ($a\neq0$). Example: $y^{\prime\prime}+3y^{\prime}+2y=0$ has $a=1$, $b=3$, $c=2$.
- right side $=0$ (called **homogeneous**). If it isn’t $0$, like $y^{\prime\prime}+y=3$, you also need [B6](#b6).
- If a coefficient has $t$ in it, like $y^{\prime\prime}-ty^{\prime}+y=0$, this shortcut fails: see [B7](#b7).

**Step 1: the characteristic equation.** Swap each derivative for a power of $s$: $y^{\prime\prime}\to s^2$, $y^{\prime}\to s$, $y\to1$.

$$a\,s^2+b\,s+c=0$$

- $y^{\prime\prime}+3y^{\prime}+2y=0$ → $s^2+3s+2=0$
- $4y^{\prime\prime}+4y^{\prime}+y=0$ → $4s^2+4s+1=0$
- $y^{\prime\prime}+9y=0$ → $s^2+9=0$ (no $y^{\prime}$ term, so no $s$ term)

**Step 2: the roots.** Factor if you can. If not, use the quadratic formula:

$$s=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$$

A negative number under the root gives complex roots. Example: $s^2+2s+5=0$ has $\sqrt{4-20}=\sqrt{-16}=j4$, so $s=-1\pm j2$. Complex numbers are in [Topic A](#topic-a).

**Step 3: the roots pick the form.** Find your row:

| Roots | General solution $y(t)$ | $y(0)$ | $y^{\prime}(0)$ |
|---|---|---|---|
| two different real: $s_1\neq s_2$ | $Ae^{s_1t}+Be^{s_2t}$ | $A+B$ | $s_1A+s_2B$ |
| one repeated real: $s$ | $(A+Bt)\,e^{st}$ | $A$ | $sA+B$ |
| complex pair: $\sigma\pm j\omega$ | $e^{\sigma t}(A\cos\omega t+B\sin\omega t)$ | $A$ | $\sigma A+\omega B$ |

- **Two different roots:** $s=-1,\,-2$ → $y=Ae^{-t}+Be^{-2t}$. One exponential per root.
- **Repeated root:** $s=-\frac12$ twice → $y=(A+Bt)\,e^{-t/2}$. $Ae^{st}+Be^{st}$ is really one term, so you need a different second solution: $te^{st}$.
- **Complex pair:** $s=-1\pm j2$ → $y=e^{-t}(A\cos2t+B\sin2t)$. $\sigma$ = the real part (how fast it shrinks), $\omega$ = the $j$ part (how fast it wiggles).

**Time saver:** the last two columns already give $y(0)$ and $y^{\prime}(0)$. With conditions at $t=0$, write the two equations for $A$ and $B$ straight from the table.

Example: roots $-2$ and $-3$ → $y(0)=A+B$ and $y^{\prime}(0)=-2A-3B$. For conditions at another time, like $y(1)$, differentiate $y(t)$ yourself (table below).

**Method:**

1. **Characteristic equation:** swap $y^{\prime\prime}\to s^2$, $y^{\prime}\to s$, $y\to1$.
2. **Roots:** factor, or use the quadratic formula.
3. **Form:** pick the row of the table that matches your roots.
4. **Conditions:** $y(0)$ and $y^{\prime}(0)$ give two equations. Solve them for $A$ and $B$.

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
caption "$y^{\prime\prime}+2y^{\prime}+ky=0$, starting at $y(0)=1$, $y^{\prime}(0)=0$. $k<1$: two real roots, the curve settles with no wiggle. $k=1$: one repeated root, the border case. $k>1$: complex roots, it wiggles inside the shrinking envelope $e^{-t}$."
```

> **Info:** **Bonus (skip-safe): why $e^{st}$ turns the ODE into a quadratic.** Plug in $y=e^{st}$, $y^{\prime}=se^{st}$, $y^{\prime\prime}=s^2e^{st}$. Every term has $e^{st}$, so pull it out:
> 
> $$
> (as^2+bs+c)\,e^{st}=0
> $$
> 
> $e^{st}$ is never zero, so the bracket must be zero. That bracket is the characteristic equation.
> 
> For complex roots, Euler’s formula $e^{(\sigma\pm j\omega)t}=e^{\sigma t}(\cos\omega t\pm j\sin\omega t)$ turns the two exponentials into $\cos$ and $\sin$. That’s why the third row has no $j$ in it. The extra $t$ for a repeated root comes from reduction of order ([B7](#b7)).

**Example: Example 6 · W5 · Complex roots, real answer**

Solve $y''+2y'+5y=0$, $\;y(0)=1$, $y'(0)=1$.

1. **Type:** second order, plain-number coefficients, right side 0.
2. **Characteristic equation** and roots. $\sqrt{4-20}=\sqrt{-16}=j4$.

   $$s^2+2s+5=0\quad\Rightarrow\quad s=\dfrac{-2\pm j4}{2}=-1\pm j2$$
3. **Form:** complex row, with $\sigma=-1$ and $\omega=2$.

   $$y=e^{-t}(A\cos2t+B\sin2t)$$
4. **Conditions** straight from the table: $y(0)=A$ and $y^{\prime}(0)=\sigma A+\omega B$.

   $$A=1,\qquad -A+2B=1\ \Rightarrow\ B=1$$

**Answer:** $y=e^{-t}(\cos2t+\sin2t)$. It wiggles at 2 rad/s, and the $e^{-t}$ shrinks the wiggle towards 0.

**Problem: Problem 25 · W5 · Two different real roots** (introductory)

Solve $y''+5y'+6y=0$, $\;y(0)=2$, $y'(0)=-5$.

<details><summary>Solution</summary>

1. **Type:** plain-number coefficients, right side 0.
2. **Characteristic equation:** it factors.

   $$s^2+5s+6=(s+2)(s+3)=0\quad\Rightarrow\quad s=-2,\,-3$$
3. **Form:** two different real roots.

   $$y=Ae^{-2t}+Be^{-3t}$$
4. **Conditions** from the table: $y(0)=A+B$, $y^{\prime}(0)=-2A-3B$.

   $$A+B=2,\qquad -2A-3B=-5$$
5. Multiply the first equation by 2 and add the second: $-B=-1$.

   $$B=1,\qquad A=1$$

**Answer:** $y=e^{-2t}+e^{-3t}$.

</details>

**Problem: Problem 26 · W5 · A repeated root** (introductory)

Solve $4y''+4y'+y=0$, $\;y(0)=4$, $y'(0)=0$.

<details><summary>Solution</summary>

1. **Type:** plain-number coefficients, right side 0.
2. **Characteristic equation:** it’s a perfect square.

   $$4s^2+4s+1=(2s+1)^2=0\quad\Rightarrow\quad s=-\tfrac12\ \text{(twice)}$$
3. **Form:** repeated root, so add the extra $t$.

   $$y=(A+Bt)\,e^{-t/2}$$
4. **Conditions:** $y(0)=A$, $y^{\prime}(0)=sA+B$ with $s=-\frac12$.

   $$A=4,\qquad -2+B=0\ \Rightarrow\ B=2$$

**Answer:** $y=(4+2t)\,e^{-t/2}$.

</details>

**Problem: Problem 27 · W5 · No damping term** (intermediate)

Solve $y''+9y=0$, $\;y(0)=2$, $y'(0)=3$.

<details><summary>Solution</summary>

1. **Type:** plain-number coefficients, right side 0. There’s no $y^{\prime}$ term, so $b=0$.
2. **Characteristic equation:** $s^2+9=0$, so $s^2=-9$.

   $$s=\pm j3\qquad(\sigma=0,\ \omega=3)$$
3. **Form:** complex row. $e^{0t}=1$, so the exponential drops out.

   $$y=A\cos3t+B\sin3t$$
4. **Conditions:** $y(0)=A$, $y^{\prime}(0)=\omega B=3B$.

   $$A=2,\qquad B=1$$

**Answer:** $y=2\cos3t+\sin3t$. With $\sigma=0$ nothing shrinks it, so it swings forever. That’s the ideal LC circuit in [Topic D](#topic-d).

</details>

**Problem: Problem 28 · W5 · Work backwards from the roots** (advanced)

A constant-coefficient equation $y^{\prime\prime}+by^{\prime}+cy=0$ has characteristic roots $-3\pm j4$. 

(a) Find $b$ and $c$. (b) Write the general solution. (c) Find the solution with $y(0)=0$, $y^{\prime}(0)=8$.

<details><summary>Solution</summary>

1. **Type:** backwards. You have the roots, so build the quadratic as $(s-s_1)(s-s_2)=0$.
2. (a) Multiply out $(s+3-j4)(s+3+j4)=(s+3)^2-(j4)^2=(s+3)^2+16$.

   $$s^2+6s+25=0\quad\Rightarrow\quad b=6,\ c=25$$
3. (b) **Form:** complex row with $\sigma=-3$, $\omega=4$.

   $$y=e^{-3t}(A\cos4t+B\sin4t)$$
4. (c) **Conditions:** $y(0)=A=0$, and $y^{\prime}(0)=\sigma A+\omega B=4B=8$.

   $$A=0,\qquad B=2$$

**Answer:** (a) $y^{\prime\prime}+6y^{\prime}+25y=0$. (b) $y=e^{-3t}(A\cos4t+B\sin4t)$. (c) $y=2e^{-3t}\sin4t$.

</details>

### B6 · Undetermined coefficients

[Week 6 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/357f26bd-d16c-4769-af0a-d1b2f535d62e#77a5aea3-a3f4-4738-a817-01c3f18cfdae)

**What if the right side isn’t zero?** Like $y^{\prime\prime}+y=3$. The right side, $g(t)$, is called the **forcing** (in a circuit, it’s the source).

The [B5](#b5) solutions all give $0$ when you plug them in, never $g(t)$. So you need one extra piece that gives $g(t)$.

The equations look like:

$$a\,y^{\prime\prime}+b\,y^{\prime}+c\,y=g(t)$$

- left side = the same as in [B5](#b5): plain numbers $a,b,c$
- $g(t)$ = everything with no $y$ in it, moved to the right. Example: $y^{\prime\prime}+4y-8=0$ → $g=8$.

The answer always has two pieces:

$$y=y_c+y_p$$

- $y_c$ = the **complementary solution**: set the right side to $0$ and solve with [B5](#b5). It carries the two constants $c_1,c_2$.
- $y_p$ = a **particular solution**: any one function that gives exactly $g(t)$ when you plug it in. No constants.

Why adding works: plug in $y_c+y_p$. The $y_c$ part gives $0$ and the $y_p$ part gives $g$, so the total is $0+g=g$.

Example: $y^{\prime\prime}+y=3$.

- $y_c$: $s^2+1=0$, $s=\pm j$, so $y_c=c_1\sin t+c_2\cos t$.
- $y_p$: try a constant. $y_p=3$ gives $0+3=3$ ✓.
- Add: $y=3+c_1\sin t+c_2\cos t$.

**How do you find $y_p$? Copy the shape of $g(t)$.** Derivatives of $t^2$, $e^{2t}$ or $\cos3t$ stay the same kind of function.

So guess a $y_p$ that looks like $g$, with unknown numbers $A,B,\dots$ in front. Plug it in to find the numbers.

| Term in $g(t)$ | Guess for $y_p$ | Example |
|---|---|---|
| constant, or polynomial of degree $n$ | $A_nt^n+\dots+A_1t+A_0$ (**all** lower powers) | $2t$ → $At+B$ |
| $e^{at}$ | $Ae^{at}$ | $3e^{2t}$ → $Ae^{2t}$ |
| $\sin rt$ or $\cos rt$ | $A\cos rt+B\sin rt$ (**always both**) | $5\sin2t$ → $A\cos2t+B\sin2t$ |
| $e^{at}\cos rt$ or $e^{at}\sin rt$ | $e^{at}(A\cos rt+B\sin rt)$ | $e^{-t}\cos t$ → $e^{-t}(A\cos t+B\sin t)$ |
| a sum of these | the sum of their guesses | $t+e^{t}$ → $At+B+Ce^{t}$ |

- **Why all lower powers:** derivatives of $At$ make a constant. The $B$ in $At+B$ is there to balance it.
- **Why always both:** each derivative swaps $\cos$ and $\sin$, so both show up even if $g$ has only one.

> **Warning:** **Trap: your guess is already in $y_c$.** Then plugging it in gives $0$, so it can never give $g$. **Fix: multiply the guess by $t$.** If that is still in $y_c$ (a repeated root), multiply by $t^2$ instead.
> 
> Example: $y^{\prime\prime}-y^{\prime}-2y=3e^{2t}$ has $y_c=c_1e^{2t}+c_2e^{-t}$. The table says $Ae^{2t}$, but that’s in $y_c$. So guess $Ate^{2t}$.

**Method:**

1. **Complementary:** set the right side to $0$ and solve ([B5](#b5)). That gives $y_c$.
2. **Guess:** pick $y_p$’s shape from the table. If any term of it is already in $y_c$, multiply by $t$.
3. **Substitute:** plug $y_p$ into the left side.
4. **Match:** the constants must match, then each $\cos$, each $\sin$, each power of $t$. Solve for $A,B,\dots$
5. **Add:** $y=y_c+y_p$.
6. **Conditions:** use them on the **whole** $y$, never on $y_c$ or $y_p$ alone.

**Calculus you need here:**

| Expression | Result | Note |
|---|---|---|
| $\cos^2t$ | $\tfrac12+\tfrac12\cos2t$ | get rid of squares before guessing |
| $\sin^2t$ | $\tfrac12-\tfrac12\cos2t$ |  |
| $(A\cos rt+B\sin rt)^{\prime\prime}$ | $-r^2(A\cos rt+B\sin rt)$ | two derivatives = times $-r^2$ |
| $(te^{at})^{\prime}$ | $(1+at)\,e^{at}$ | product rule |
| $(t\,f)^{\prime\prime}$ | $t\,f^{\prime\prime}+2f^{\prime}$ | product rule twice, for a $\times t$ guess |

> **Info:** **Bonus (skip-safe): why you can’t skip $y_c$.** $y_p$ has no constants, so on its own it can’t meet two conditions like $y(0)=0$ and $y^{\prime}(0)=0$. $y_c$ brings the two free constants that the conditions pin down. And the trap above has the same cause: anything already in $y_c$ gives $0$ on the left, so it’s useless as a guess.

**Example: Example 7 · W6 · The tutorial problem, with two boundary values · Week 6 tutorial, lecture notes p. 3–4**

Solve $\ddot y+y=6\cos^2t$ with $y(0)=0$ and $y(\pi/2)=0$. The tutorial gives the forms $y_c=c_1\sin t+c_2\cos t$ and $y_p=A+B\cos2t+D\sin2t$. ($\ddot y$ is the professor’s notation for $y^{\prime\prime}$.)

1. **Type:** plain-number coefficients, forcing $6\cos^2t$. **Complementary:** $s^2+1=0$ gives $s=\pm j$.

   $$y_c=c_1\sin t+c_2\cos t$$
2. The table has no row for $\cos^2t$. Use the identity to turn it into a constant plus $\cos2t$.

   $$6\cos^2t=3+3\cos2t$$
3. **Guess:** the constant → $A$; the $\cos2t$ → both $\cos2t$ and $\sin2t$. None of them is in $y_c$.

   $$y_p=A+B\cos2t+D\sin2t$$
4. Differentiate twice: each $\cos2t$ and $\sin2t$ gets multiplied by $-4$.

   $$y_p''=-4B\cos2t-4D\sin2t$$
5. **Substitute** into $y_p^{\prime\prime}+y_p$ and collect.

   $$A-3B\cos2t-3D\sin2t=3+3\cos2t$$
6. **Match** the constants, the cosines and the sines.

   $$A=3,\qquad B=-1,\qquad D=0$$
7. **Add** $y_c$ **before** using the conditions: they belong to the whole $y$.

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
caption "Every $c_1,c_2$ gives a solution of the ODE. Only $c_1=-4$, $c_2=-2$ goes through both points."
```

**What does the extra $t$ look like?** When $g$ matches a term of $y_c$, the answer doesn’t just copy the shape of $g$. It keeps growing, like $t\cos2t$ (this is **resonance**). Slide $\omega$ to 2 and watch:

```graph
title "Forcing at the natural frequency"
x 0 12 label="$t$"
y -25 25 label="$y$"
slider w 1 3 1.5 step=0.05 label="$\omega$" animate
curve "if(abs(w-2)<0.001, sin(2*x)-2*x*cos(2*x), 8/(4-w^2)*(sin(w*x)-w/2*sin(2*x)))" label="$y(t)$, starting at rest" color=1
curve "2*x" label="$\pm2t$" color=0 dash
curve "-2*x" color=0 dash
caption "$y''+4y=8\sin\omega t$, starting at rest. Here $y_c$ has $\sin2t$ and $\cos2t$. With $\omega$ far from 2, the swing stays small. At $\omega=2$ the forcing is in $y_c$, $y_p$ needs the extra $t$, and the swing grows along $\pm2t$."
```

**Problem: Problem 29 · W6 · A constant forcing, from rest** (introductory)

Solve $y''+4y=8$, $\;y(0)=0$, $y'(0)=0$.

<details><summary>Solution</summary>

1. **Type:** plain-number coefficients, constant forcing. **Complementary:** $s^2+4=0$, $s=\pm j2$.

   $$y_c=c_1\cos2t+c_2\sin2t$$
2. **Guess:** a constant, $y_p=A$ (not in $y_c$). **Substitute:** $0+4A=8$.

   $$y_p=2$$
3. **Add.**

   $$y=2+c_1\cos2t+c_2\sin2t$$
4. **Conditions:** $y(0)=2+c_1=0$, and $y^{\prime}(0)=2c_2=0$.

   $$c_1=-2,\qquad c_2=0$$

**Answer:** $y=2-2\cos2t$. A constant source gives a constant $y_p$, just like an RLC circuit switched onto a DC source ([Topic D](#topic-d)).

</details>

**Problem: Problem 30 · W6 · A polynomial guess needs every lower power** (introductory)

Find the general solution of $y''+y'-2y=2t$.

<details><summary>Solution</summary>

1. **Type:** forcing $2t$. **Complementary:** $s^2+s-2=(s+2)(s-1)$.

   $$y_c=c_1e^{t}+c_2e^{-2t}$$
2. **Guess:** degree 1, so $At+B$. You need the $B$ even though $g$ has no constant.

   $$y_p=At+B,\quad y_p'=A,\quad y_p''=0$$
3. **Substitute.**

   $$A-2(At+B)=2t$$
4. **Match** the $t$ terms, then the constants.

   $$-2A=2,\qquad A-2B=0$$
5. Solve.

   $$A=-1,\qquad B=-\tfrac12$$

**Answer:** $y=c_1e^{t}+c_2e^{-2t}-t-\tfrac12$. With only $At$, you’d need $A=-1$ (from the $t$ terms) and $A=0$ (from the constants) at once, which is impossible.

</details>

**Problem: Problem 31 · W6 · The guess is already in the complementary solution** (intermediate)

Find the general solution of $y''-y'-2y=3e^{2t}$.

<details><summary>Solution</summary>

1. **Type:** exponential forcing. **Complementary:** $s^2-s-2=(s-2)(s+1)$.

   $$y_c=c_1e^{2t}+c_2e^{-t}$$
2. **Guess:** the table says $Ae^{2t}$, but that’s in $y_c$ (it would give $0=3e^{2t}$). Multiply by $t$.

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

1. **Type:** guessing only. Find the **complementary** first: $s^2-2s+1=(s-1)^2$, a repeated root.

   $$y_c=(c_1+c_2t)e^t$$
2. (a) Degree 2, so all lower powers too.

   $$At^2+Bt+C$$
3. (b) $e^{-t}$ is not in $y_c$.

   $$Ae^{-t}$$
4. (c) $Ae^t$ is in $y_c$, and so is $Ate^t$. Multiply by $t^2$.

   $$At^2e^t$$
5. (d) Cosine needs both cosine and sine.

   $$A\cos t+B\sin t$$

**Answer:** (a) $At^2+Bt+C$. (b) $Ae^{-t}$. (c) $At^2e^t$. (d) $A\cos t+B\sin t$.

</details>

**Problem: Problem 33 · W6 · A trig guess that is already in the complementary solution** (advanced)

Find a particular solution of $y''+9y=12\cos3t$. Use $(tf)^{\prime\prime}=tf^{\prime\prime}+2f^{\prime}$ from the calculus table.

<details><summary>Solution</summary>

1. **Type:** trig forcing. **Complementary:** $y_c=c_1\cos3t+c_2\sin3t$ already has $\cos3t$, so multiply the guess by $t$.

   $$y_p=t\,f,\qquad f=A\cos3t+B\sin3t$$
2. **Substitute:** $f^{\prime\prime}=-9f$, so the $t$ terms cancel in $y_p^{\prime\prime}+9y_p$.

   $$y_p''+9y_p=t(f''+9f)+2f'=2f'$$
3. Differentiate $f$.

   $$2f'=-6A\sin3t+6B\cos3t$$
4. **Match** with $12\cos3t$.

   $$6B=12,\qquad -6A=0$$

**Answer:** $A=0$, $B=2$: $y_p=2t\sin3t$. The swing grows like $2t$, as in the graph above.

</details>

### B7 · Reduction of order

[Week 6 · Topic 1](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/357f26bd-d16c-4769-af0a-d1b2f535d62e#400c9eda-6dcb-4cf4-9c21-265384342cb1)

**What if the coefficients have $t$ in them?** Like $y^{\prime\prime}-ty^{\prime}+y=0$. The $e^{st}$ guess from [B5](#b5) only works when the coefficients are plain numbers, so it fails here.

But if the question **gives you one solution**, $y_1$, then reduction of order finds the second one.

First get $y^{\prime\prime}$ alone (divide by whatever multiplies it):

$$y^{\prime\prime}+p(t)\,y^{\prime}+q(t)\,y=0$$

- $p(t)$ = what multiplies $y^{\prime}$, sign included
- $q(t)$ = what multiplies $y$
- $y_1(t)$ = the solution you’re given. Check it first: plug it in, you should get $0$.

Examples:

- $y^{\prime\prime}-ty^{\prime}+y=0$ with $y_1=t$: $p=-t$, $q=1$. Check: $0-t\cdot1+t=0$ ✓.
- $t^2y^{\prime\prime}-3ty^{\prime}+4y=0$ with $y_1=t^2$: divide by $t^2$, so $p=-\frac3t$, $q=\frac4{t^2}$. Check: $2t^2-6t^2+4t^2=0$ ✓.

**The idea.** Guess the second solution as the one you know, times an unknown function $v(t)$:

$$y=y_1\,v$$

Example: with $y_1=t$, try $y=tv$. When you plug it in, every term with a plain $v$ cancels, because $y_1$ already solves the ODE.

Only $v^{\prime}$ and $v^{\prime\prime}$ are left. Call $z=v^{\prime}$, and you have a **first-order** equation in $z$. The order went down by one: that’s the name.

**Method:**

1. **Substitute** $y=y_1v$, with $y^{\prime}=y_1^{\prime} v+y_1v^{\prime}$ and $y^{\prime\prime}=y_1^{\prime\prime} v+2y_1^{\prime} v^{\prime}+y_1v^{\prime\prime}$.
2. **Collect** terms. The plain-$v$ terms cancel.
3. **Set $z=v^{\prime}$** and solve the first-order equation for $z$. It’s usually separable ([B1](#b1)) or linear ([B2](#b2)).
4. **Integrate:** $v=\int z\,dt$, plus a constant.
5. **Multiply back:** $y=y_1v$. The constant from step 4 gives back $C\,y_1$, the solution you started with.

**Check with the formula.** All of those steps always end at:

$$y_2=y_1\int\dfrac{e^{-\int p\,dt}}{y_1^{\,2}}\,dt$$

Example: $t^2y^{\prime\prime}-ty^{\prime}+y=0$ with $y_1=t$ ($t>0$). Divide by $t^2$: $p=-\frac1t$, so $e^{-\int p\,dt}=e^{\ln t}=t$, and $y_2=t\int\frac{t}{t^2}\,dt=t\ln t$.

Use it to check your answer, or as a shortcut if the question lets you.

**Calculus you need here:**

| Expression | Result | Note |
|---|---|---|
| $(y_1v)^{\prime}$ | $y_1^{\prime} v+y_1v^{\prime}$ | product rule |
| $(y_1v)^{\prime\prime}$ | $y_1^{\prime\prime} v+2y_1^{\prime} v^{\prime}+y_1v^{\prime\prime}$ | product rule twice; the two $y_1^{\prime} v^{\prime}$ terms add up |
| $\int\frac1z\,dz$ | $\ln|z|$ | for the separable $z$ equation |
| $e^{-2\ln t}$ | $\dfrac{1}{t^2}$ | $e^{k\ln t}=t^k$ |
| $\int\dfrac{e^{t^2/2}}{t^2}\,dt$ | no formula | leave it as an integral; that counts as a full answer |

> **Info:** **Bonus (skip-safe): why the plain-$v$ terms cancel.** After you substitute, gather everything that multiplies $v$ itself. You get $v\,(y_1^{\prime\prime}+p\,y_1^{\prime}+q\,y_1)$. The bracket is just $y_1$ plugged into the ODE, which is $0$ because $y_1$ is a solution.

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
Plug all three into the ODE.
$$ \hl{tv''+(2-t^2)v'}=0 $$
Collect terms. The $-tv$ and $+tv$ cancel.
$$ t\hl{z'}+(2-t^2)\hl{z}=0 $$
Set $z=v^{\prime}$: now it’s first order in $z$.
```

**Example: Example 8 · W6 · Finish the lecture example · handwritten notes p. 1–2**

Solve $tz'+(2-t^2)z=0$ (from the stepper above), then find the general solution of $y''-ty'+y=0$ for $t\neq0$.

1. **Type:** the $z$ equation is separable. Divide by $tz$ and move the $t$ terms to the right.

   $$\dfrac{dz}{z}=\dfrac{t^2-2}{t}\,dt=\left(t-\dfrac2t\right)dt$$
2. **Integrate** both sides: $\int\frac1z\,dz=\ln|z|$.

   $$\ln|z|=\dfrac{t^2}2-2\ln|t|+C$$
3. Exponentiate. $e^{-2\ln|t|}=1/t^2$.

   $$z=C_1\,\dfrac{e^{t^2/2}}{t^2}$$
4. **Integrate** again, $v=\int z\,dt$. This integral has no formula, so leave it as is.

   $$v=C_1\int\dfrac{e^{t^2/2}}{t^2}\,dt+C_2$$
5. **Multiply back** by $y_1=t$.

   $$y=tv$$

**Answer:** $y=C_2\,t+C_1\,t\displaystyle\int\frac{e^{t^2/2}}{t^2}\,dt$. Formula check: $p=-t$, so $e^{-\int p\,dt}=e^{t^2/2}$ and $y_1^2=t^2$. ✓

**Problem: Problem 34 · W5 + W6 · Where the repeated-root t comes from** (introductory)

$y''+4y'+4y=0$ has the repeated characteristic root $s=-2$, so $y_1=e^{-2t}$. Use reduction of order to find the general solution.

<details><summary>Solution</summary>

1. **Type:** one solution given, so reduction of order. **Substitute** $y=e^{-2t}v$.

   $$y'=e^{-2t}(v'-2v)$$
2. Differentiate again.

   $$y''=e^{-2t}(v''-4v'+4v)$$
3. **Collect:** plug in and divide by $e^{-2t}$. This time the $v^{\prime}$ terms cancel too.

   $$(v''-4v'+4v)+4(v'-2v)+4v=v''=0$$
4. **Integrate** twice.

   $$v=C_1+C_2t$$
5. **Multiply back.**

   $$y=(C_1+C_2t)\,e^{-2t}$$

**Answer:** $y=(C_1+C_2t)e^{-2t}$. That’s the repeated-root row of [B5](#b5): the extra $t$ came from $v$.

</details>

**Problem: Problem 35 · W6 · A second solution with a logarithm** (intermediate)

For $t>0$, $y_1=t^2$ solves $t^2y''-3ty'+4y=0$. Find the general solution.

<details><summary>Solution</summary>

1. **Type:** $t$ in the coefficients, one solution given. **Substitute** $y=t^2v$.

   $$y'=2tv+t^2v',\qquad y''=2v+4tv'+t^2v''$$
2. **Collect:** the plain-$v$ terms cancel ($2-6+4=0$).

   $$t^4v''+t^3v'=0$$
3. Divide by $t^4$ and **set $z=v^{\prime}$**.

   $$z'+\dfrac zt=0$$
4. Separate: $\int\frac{dz}{z}=-\int\frac{dt}{t}$, so $\ln|z|=-\ln t+C$.

   $$z=\dfrac{C_2}t$$
5. **Integrate:** $\int\frac1t\,dt=\ln t$ for $t>0$.

   $$v=C_1+C_2\ln t$$
6. **Multiply back** by $t^2$.

   $$y=C_1t^2+C_2t^2\ln t$$

**Answer:** $y=C_1t^2+C_2t^2\ln t$. Formula check: $p=-\frac3t$, $e^{-\int p\,dt}=t^3$, $\int\frac{t^3}{t^4}dt=\ln t$. ✓

</details>

## Topic C: Does exactly one solution exist?

[Week 3 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/3d1ae4a9-687d-4654-873d-be3439faea2f#8c746b9b-2fbf-48f4-8a2d-704a643bdcf7) [Week 5 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/0c7a77fe-aeed-47a8-b1c3-4967d73eea21#b4f41ebe-f4f6-4d5d-816d-ceaa37811b8f)

**Can you answer without solving?** Some questions ask “is there exactly one solution?” or “on what interval is one guaranteed?”. You don’t solve the ODE. You check a theorem instead:

- **First order,** like $y^{\prime}=\dfrac ty$ → [C1](#c1).
- **Second-order linear,** like $t\,y^{\prime\prime}+y=0$ → [C2](#c2).

Both checks work the same way. Write the equation in a standard form, then look for the spots where something breaks:

- **Division by zero:** $\dfrac ty$ breaks at $y=0$.
- **$\ln$ of zero or a negative:** $\ln t$ breaks at $t\le0$.
- **Square root of a negative:** $\sqrt y$ breaks at $y<0$.

### C1 · First order: is there exactly one solution through this point?

[Week 3 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/3d1ae4a9-687d-4654-873d-be3439faea2f#8c746b9b-2fbf-48f4-8a2d-704a643bdcf7)

**When:** you get $\dfrac{dy}{dt}=F(t,y)$ and a starting point $(t_0,y_0)$. The question asks if exactly one solution goes through that point.

First get the derivative alone on the left:

$$\dfrac{dy}{dt}=F(t,y)$$

- $F(t,y)$ = everything on the right side
- $\dfrac{\partial F}{\partial y}$ (or $F_y$) = the **partial derivative** in $y$: differentiate in $y$ and treat $t$ like a number. Example: $F=y^2+t$ gives $F_y=2y$ (the $t$ is a constant, so it disappears).

**The theorem** (Spiegel, used in the Week 3 lecture):

> **Info:** If $F$ and $\dfrac{\partial F}{\partial y}$ are both continuous (no blow-ups, no gaps) near $(t_0,y_0)$, then **exactly one** solution passes through $(t_0,y_0)$.

So there are two outcomes:

- **Both are fine** → yes, exactly one solution (at least for $t$ near $t_0$).
- **One breaks** → the theorem says **nothing**. There could be no solution, one, or many. A fail means “don’t know”, not “no”.

Why $F_y$ matters: it says how fast the slope changes as you move up or down. If it blows up, solutions can split apart (see the graph below).

Mini examples:

- $y^{\prime}=t^2+3ty$: $F_y=3t$. Both are fine everywhere → exactly one solution through **every** point.
- $y^{\prime}=\dfrac{t}{y}$: $F_y=-\dfrac{t}{y^2}$. Both break on the line $y=0$ → guaranteed only at points with $y_0\neq0$.

**Method:**

1. **Write $F$:** get $\dfrac{dy}{dt}$ alone.
2. **Differentiate:** find $\dfrac{\partial F}{\partial y}$, treating $t$ as a number.
3. **Find the bad set:** where does $F$ or $\dfrac{\partial F}{\partial y}$ break? Look for a 0 in a denominator, $\ln$ of $\le0$, $\sqrt{\ }$ of $<0$. Example: $y^{-1/2}=\dfrac{1}{\sqrt y}$ breaks at $y=0$.
4. **Check the point:** is $(t_0,y_0)$ away from the bad set? Yes → exactly one solution. No → no conclusion.

**Calculus you need here:**

| $F$ | $\dfrac{\partial F}{\partial y}$ | Note |
|---|---|---|
| $t^2+3ty$ | $3t$ | $t$ is a number here, so $t^2$ disappears |
| $\dfrac{t}{y}=t\,y^{-1}$ | $-t\,y^{-2}$ | power rule in $y$ |
| $\sqrt{y}=y^{1/2}$ | $\dfrac{1}{2\sqrt y}$ | breaks at $y=0$ |
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
caption "At $y=0$, $\partial F/\partial y=1/(2\sqrt y)$ blows up, so the theorem gives no guarantee. And in fact many curves leave $(1,0)$: each sits at 0 for a while, then rises as $(t-c)^2/4$. Above the axis nothing breaks, and only one curve goes through each point."
```

> **Info:** **Bonus (skip-safe): why a blown-up $\partial F/\partial y$ allows several solutions.** $\partial F/\partial y$ says how much the slope changes when you move a little up or down. If it stays finite, two solutions that start at the same point can never drift apart. For $\sqrt y$ it is infinite at $y=0$, so a curve can sit on the axis and then “peel off” at any moment.

**Problem: Problem 36 · W3 · Same equation, two starting points** (introductory)

For $\dfrac{dy}{dt}=\sqrt{y}$: (a) does the theorem guarantee a unique solution through $(1,4)$? (b) through $(1,0)$? For (b), check that $y=0$ and $y=\dfrac{(t-1)^2}{4}$ (for $t\ge1$) both pass through $(1,0)$ and solve the ODE.

<details><summary>Solution</summary>

1. **Type:** existence and uniqueness, first order. $F=\sqrt y$.
2. **Differentiate** in $y$.

   $$\dfrac{\partial F}{\partial y}=\dfrac{1}{2\sqrt y}$$
3. **Bad set:** $F$ needs $y\ge0$, and $F_y$ breaks at $y=0$. So the bad set is $y\le0$.
4. **Check (a):** $(1,4)$ has $y_0=4>0$, so both are fine around it → unique.
5. **Check (b):** $(1,0)$ sits on $y=0$, in the bad set → the theorem tells you nothing.
6. **Two solutions:** for $y=\frac{(t-1)^2}{4}$, $y^{\prime}=\frac{t-1}{2}$ and $\sqrt y=\frac{t-1}{2}$ when $t\ge1$ ✓. For $y=0$, $0=\sqrt0$ ✓. Both equal 0 at $t=1$.

**Answer:** (a) Yes, exactly one solution through $(1,4)$. (b) The theorem gives no guarantee, and in fact at least two solutions pass through $(1,0)$.

</details>

**Problem: Problem 37 · W3 · Which points are guaranteed?** (introductory)

For $\dfrac{dy}{dt}=\dfrac{t}{y}$, decide whether the theorem guarantees a unique solution through (a) $(2,1)$, (b) $(0,3)$, (c) $(2,0)$.

<details><summary>Solution</summary>

1. **Type:** existence and uniqueness, first order. $F=\dfrac ty$.
2. **Differentiate** in $y$ (power rule).

   $$\dfrac{\partial F}{\partial y}=-\dfrac{t}{y^2}$$
3. **Bad set:** both divide by $y$, so the line $y=0$.
4. **Check the points:** (a) $y_0=1$ and (b) $y_0=3$ are off the line. (c) $y_0=0$ is on it.

**Answer:** (a) Yes. (b) Yes. (c) No guarantee: $F$ itself is undefined at $(2,0)$.

</details>

**Problem: Problem 38 · W3 · A strip, not a point** (intermediate)

For $(t-3)\,y^{\prime}+(\ln t)\,y=2t$, $\;y(1)=2$, find the region containing the starting point where the theorem applies. Do not solve.

<details><summary>Solution</summary>

1. **Type:** existence and uniqueness. **Write $F$:** get $y^{\prime}$ alone.

   $$F=\dfrac{2t-(\ln t)\,y}{t-3}$$
2. **Differentiate** in $y$. Only the $y$ term survives.

   $$\dfrac{\partial F}{\partial y}=-\dfrac{\ln t}{t-3}$$
3. **Bad set:** $\ln t$ needs $t>0$, and the denominator needs $t\neq3$. Nothing limits $y$.
4. **Check the point:** $t_0=1$ lies between $0$ and $3$.

   $$0<t<3,\quad\text{any }y$$

**Answer:** The strip $0<t<3$ (all $y$). The start $(1,2)$ is inside it, so exactly one solution passes through it.

</details>

### C2 · Second order linear: interval, zero start, independent solutions

[Week 5 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/0c7a77fe-aeed-47a8-b1c3-4967d73eea21#b4f41ebe-f4f6-4d5d-816d-ceaa37811b8f)

**When:** a second-order **linear** equation, usually with two starting values $y(t_0)$ and $y^{\prime}(t_0)$. The question asks one of three things:

- **Interval:** on what interval is exactly one solution guaranteed?
- **Zero start:** what is the solution if both starting values are 0?
- **Two solutions:** do two given solutions give the general solution?

For all three, first divide by whatever multiplies $y^{\prime\prime}$, so $y^{\prime\prime}$ stands alone:

$$y^{\prime\prime}+p(t)\,y^{\prime}+q(t)\,y=g(t)$$

- $p(t)$ = what multiplies $y^{\prime}$ (after dividing)
- $q(t)$ = what multiplies $y$ (after dividing)
- $g(t)$ = the right side, called the forcing (after dividing)

Example: $t\,y^{\prime\prime}+y=0$ → divide by $t$ → $y^{\prime\prime}+\dfrac1t\,y=0$. So $p=0$, $q=\dfrac1t$, $g=0$.

> **Info:** **The theorem.** If $p$, $q$ and $g$ are continuous on an open interval $I$ that contains $t_0$, then for **any** starting values $y(t_0)$ and $y^{\prime}(t_0)$ there is **exactly one** solution, and it works on the **whole** interval $I$.

**Interval.** A **trouble point** is a $t$ where $p$, $q$ or $g$ breaks. The biggest $I$ runs from the nearest trouble point left of $t_0$ to the nearest one on the right.

- $t\,y^{\prime\prime}+y=0$: $q=\dfrac1t$ breaks at $t=0$. For $t_0=5$, $I=(0,\infty)$. For $t_0=-2$, $I=(-\infty,0)$.
- $y^{\prime\prime}+3y^{\prime}+2y=\cos t$: nothing breaks, so $I$ is the whole real line. Same for any constant-coefficient equation whose $g$ never breaks.

**Method (interval):**

1. **Divide** by what multiplies $y^{\prime\prime}$. Read off $p,q,g$.
2. **Trouble points:** where $p$, $q$ or $g$ breaks (0 in a denominator, $\ln$ of $\le0$, …).
3. **Pick the piece** of the $t$-axis between trouble points that contains $t_0$. Use open ends (round brackets).

**Zero start.** Take a linear equation with right side $g=0$ and both starting values zero, $y(t_0)=0$ and $y^{\prime}(t_0)=0$. The answer is:

$$y(t)\equiv0$$

Why: $y=0$ solves any such equation and fits both starting values. The theorem says there is only one solution, so $y=0$ is it.

Example: $y^{\prime\prime}+3y^{\prime}+2y=0$, $y(1)=0$, $y^{\prime}(1)=0$ → $y\equiv0$, no solving needed. But it needs $g=0$: in $y^{\prime\prime}+y=1$, $y=0$ gives $0=1$, so it is not a solution.

**Two solutions → the general solution?** Say $y_1$ and $y_2$ both solve the same linear equation with $g=0$. Compute their **Wronskian**:

$$W=y_1\,y_2^{\prime}-y_1^{\prime}\,y_2$$

- $W\neq0$ → $y_1,y_2$ are **independent** (neither is a multiple of the other), and $y=c_1y_1+c_2y_2$ is the general solution.
- $W=0$ → one is a multiple of the other. Then $c_1y_1+c_2y_2$ really has only one constant, so it is **not** enough.

Example: $e^{t}$ and $e^{2t}$ give $W=e^t\cdot2e^{2t}-e^t\cdot e^{2t}=e^{3t}$. That is never zero → independent.

This is why the repeated-root case in [B5](#b5) uses $(c_1+c_2t)e^{st}$: $c_1e^{st}+c_2e^{st}$ is just $(c_1+c_2)e^{st}$, one constant.

> **Info:** **Bonus (skip-safe): why the Wronskian decides it.** Fitting $c_1y_1+c_2y_2$ to $y(t_0)$ and $y^{\prime}(t_0)$ gives two equations:
> 
> $$
> c_1y_1+c_2y_2=y(t_0),\quad c_1y_1^{\prime}+c_2y_2^{\prime}=y^{\prime}(t_0)
> $$
> 
> A $2\times2$ system like this has exactly one answer when its determinant, $y_1y_2^{\prime}-y_1^{\prime} y_2=W$, is not zero. So $W\neq0$ means you can match any pair of starting values.

**Problem: Problem 39 · W5 · Find the interval; do not solve** (intermediate)

For $(t-1)\,y^{\prime\prime}+y^{\prime}+y=\ln t$, find the largest interval on which the theorem guarantees exactly one solution for (a) $t_0=2$, (b) $t_0=\tfrac12$.

<details><summary>Solution</summary>

1. **Type:** existence and uniqueness, second-order linear. **Divide** by $t-1$.

   $$p=\dfrac1{t-1},\quad q=\dfrac1{t-1},\quad g=\dfrac{\ln t}{t-1}$$
2. **Trouble points:** $\ln t$ needs $t>0$, and the denominator needs $t\neq1$. So the pieces are $(0,1)$ and $(1,\infty)$.
3. **Pick the piece:** $t_0=2$ is in $(1,\infty)$. $t_0=\tfrac12$ is in $(0,1)$.

**Answer:** (a) $(1,\infty)$. (b) $(0,1)$.

</details>

**Problem: Problem 40 · W5 · Which pair gives the general solution?** (intermediate)

Both pairs solve $y^{\prime\prime}+4y^{\prime}+4y=0$: (a) $e^{-2t}$ and $3e^{-2t}$; (b) $e^{-2t}$ and $te^{-2t}$. Compute each Wronskian and decide which pair gives the general solution.

<details><summary>Solution</summary>

1. **Type:** independence, so compute $W=y_1y_2^{\prime}-y_1^{\prime} y_2$.
2. **Pair (a):** $y_2^{\prime}=-6e^{-2t}$, $y_1^{\prime}=-2e^{-2t}$.

   $$W=e^{-2t}(-6e^{-2t})-(-2e^{-2t})(3e^{-2t})=0$$
3. **Pair (b):** product rule, $(te^{-2t})^{\prime}=(1-2t)e^{-2t}$.

   $$W=e^{-2t}(1-2t)e^{-2t}-(-2e^{-2t})\,te^{-2t}=e^{-4t}$$
4. **Decide:** $e^{-4t}$ is never zero, so pair (b) is independent.

**Answer:** (a) $W=0$: not enough (they are multiples). (b) $W=e^{-4t}\neq0$: general solution $y=(c_1+c_2t)e^{-2t}$.

</details>

**Problem: Problem 41 · W5 + W6 · The answer without solving** (advanced)

Solve $y^{\prime\prime}+t\,y^{\prime}+e^{t}\,y=0$, $\;y(0)=0$, $\;y^{\prime}(0)=0$.

<details><summary>Solution</summary>

1. **Type:** the $t$ and $e^t$ coefficients look impossible with our methods. But it is linear, $g=0$, and both starting values are 0: a **zero start**.
2. **Interval:** $p=t$, $q=e^t$, $g=0$ never break, so exactly one solution exists on the whole real line.
3. **Try $y=0$:** $0+0+0=0$ ✓, and $y(0)=0$, $y^{\prime}(0)=0$ ✓.
4. **Conclude:** there is only one solution, and $y=0$ works, so it is **the** solution.

**Answer:** $y(t)\equiv0$ for all $t$.

</details>

## Topic D: Circuits → ODE → solution

[Week 2 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/08d203f6-a2b5-41b9-adfd-a14e22fb03d8#77c9c878-68d6-44e3-8f1e-2f68ba18701b) [Week 5 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/0c7a77fe-aeed-47a8-b1c3-4967d73eea21#d5ad9ba9-0ec5-4b62-acf5-b1c7e17d6463)

**What does a circuit question want?** Always the same thing: a switch flips at $t=0$, and you need $v(t)$ or $i(t)$ after it.

The circuit gives you two things:

- **the ODE**: write KVL or KCL for the circuit **after** the switch;
- **the starting value**: read it off the circuit **before** the switch.

Then you solve that ODE with [Topic B](#topic-b), like any other ODE.

**The three rules you need, one per element:**

| Element | Law | After a long time (DC) | When the switch flips |
|---|---|---|---|
| Capacitor $C$ | $i=C\dfrac{dv}{dt}$ | a **gap** (open circuit) | $v_C$ **can’t jump** |
| Inductor $L$ | $v=L\dfrac{di}{dt}$ | a **wire** (short circuit) | $i_L$ **can’t jump** |
| Resistor $R$ | $v=iR$ | — | its $v$ and $i$ **can** jump |

**After a long time** (called **DC steady state**): nothing changes any more, so every $\frac{d}{dt}$ is 0.

- **Capacitor:** $i=C\cdot0=0$. No current gets through, so it acts like a gap.
- **Inductor:** $v=L\cdot0=0$. No voltage across it, so it acts like a plain wire.

Example: a $12\,\mathrm{V}$ source, a resistor and a capacitor in one loop, left alone for a long time. No current flows, so the resistor has 0 V and the capacitor holds all $12\,\mathrm{V}$.

**When the switch flips:** $0^-$ = just before, $0^+$ = just after. “Can’t jump” means:

$$v_C(0^+)=v_C(0^-),\qquad i_L(0^+)=i_L(0^-)$$

Example: if the capacitor holds $12\,\mathrm{V}$ just before the switch flips, it still holds $12\,\mathrm{V}$ just after. Why: a jump would need an infinite current (see the Bonus at the end of this section).

**So which quantity do you solve for?** The one that can’t jump ($v_C$ or $i_L$), because its starting value carries straight across the switch. Get the rest from it afterwards, e.g. $i_C=C\frac{dv_C}{dt}$.

**What each element looks like at the three moments you need:**

|  | $t=0^-$ (old DC state) | $t=0^+$ (just after) | $t\to\infty$ (new DC state) |
|---|---|---|---|
| Capacitor | gap, holding $V_0$ | a **voltage source** $V_0$ | gap again |
| Inductor | wire, carrying $I_0$ | a **current source** $I_0$ | wire again |
| Resistor | Ohm’s law | Ohm’s law (may jump) | Ohm’s law |

- **Capacitor at $0^+$:** it still holds its old voltage $V_0$, so for that instant it acts like a battery. Example: charged to $12\,\mathrm{V}$ → a $12\,\mathrm{V}$ source.
- **Inductor at $0^+$:** it keeps pushing its old current $I_0$, so it acts like a current source. Example: carrying $4\,\mathrm{A}$ → a $4\,\mathrm{A}$ source.

```graph
title "A capacitor charging from $0\,\mathrm{V}$: its voltage doesn’t jump, its current does"
x -1 5 label="$t/\tau$"
y -0.2 1.2 label="scaled so the biggest value is 1"
curve "if(x<0, 0, 1-exp(-x))" label="$v_C$: starts at 0, no jump" color=1
curve "if(x<0, 0, exp(-x))" label="$i_C$: 0 before, jumps at $t=0$" color=2
vline "0" label="switch closes" color=0
caption "This is Pre-tutorial 2 (a problem in D1). Before the switch closes, no current goes into the capacitor. Just after, $v_C$ is still 0, so the resistor beside it gets no current and all of the source current goes into the capacitor. $i_C$ jumps; $v_C$ doesn’t."
```

**The switching recipe.** Every circuit problem, in five steps:

1. **Before ($t<0$):** the switch sat in its old spot for a long time, so use the DC rules: $C$ = gap, $L$ = wire. Find $v_C(0^-)$ or $i_L(0^-)$. Example: a capacitor that sat across a $12\,\mathrm{V}$ source → $v_C(0^-)=12\,\mathrm{V}$.
2. **Just after ($t=0^+$):** carry the value across: $v_C(0^+)=v_C(0^-)$, $i_L(0^+)=i_L(0^-)$. Need something else at $0^+$, like a resistor current? Draw the **new** circuit with $C$ as a voltage source $v_C(0^+)$ (or $L$ as a current source $i_L(0^+)$), then use KVL/KCL.
3. **After ($t>0$):** in the new circuit, write KVL around a loop or KCL at a node. Swap $i_C$ for $C\frac{dv}{dt}$ and $v_L$ for $L\frac{di}{dt}$. That’s the ODE. Example: a loop of $V_s$, $R$, $C$: $\;V_s=Ri+v_C$ with $i=C\frac{dv_C}{dt}$, so $RC\frac{dv_C}{dt}+v_C=V_s$.
4. **Solve:** one $L$ or one $C$ → first order → the [D1](#d1) formula (it’s a [B2](#b2) equation). An $L$ and a $C$ → second order → [D2](#d2) (solved with [B5](#b5) or [B6](#b6)). Your values from step 2 are the starting conditions.
5. **Check ($t\to\infty$):** use the DC rules again ($C$ = gap, $L$ = wire). Your answer must head to this final value. Example: in the $V_s$, $R$, $C$ loop, no current flows in the end, so $v_C\to V_s$.

> **Warning:** **Before and after are two different circuits.** Draw both. Use the old one only for the starting value (step 1). Write the ODE (step 3) from the new one, with only the parts still connected.

> **Warning:** **The sign comes from the drawn arrow.** First find which way the current really flows, then compare with the arrow. If they point opposite ways, the value is **negative**. Example: $3\,\mathrm{A}$ really flows down, the $i_L$ arrow points up → $i_L(0)=-3\,\mathrm{A}$.

> **Info:** **Bonus (skip-safe): why $v_C$ and $i_L$ can’t jump.** If $v_C$ jumped, its slope $\frac{dv}{dt}$ would be infinite at that instant. Then $i=C\frac{dv}{dt}$ would be an infinite current, and no real circuit can supply that. Same for an inductor: a jump in $i_L$ would need an infinite voltage $v=L\frac{di}{dt}$. Another way to see it: the stored energy, $\frac12Cv^2$ or $\frac12Li^2$, can’t change in zero time.

### D1 · First-order RC and RL circuits

[Week 1 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/1cbac07a-cd02-48c2-8c30-c9829c4e06b2#ab5bf400-4411-4869-8d74-7790f8ee6f2c) [Week 2 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/08d203f6-a2b5-41b9-adfd-a14e22fb03d8#77c9c878-68d6-44e3-8f1e-2f68ba18701b) [Week 3 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/3d1ae4a9-687d-4654-873d-be3439faea2f#a43fc96e-8dc5-4a1e-bfdf-bf1acf01f98b)

**When is a circuit first order?** When, after the switch, only **one** capacitor or **one** inductor is left (after combining), plus resistors and DC sources.

Then the ODE always has the same shape, and one formula solves it.

Call $x$ the quantity that can’t jump: $v_C$ in an RC circuit, $i_L$ in an RL circuit. For $t>0$, KVL or KCL always gives:

$$\dfrac{dx}{dt}+\dfrac{x}{\tau}=\dfrac{x_f}{\tau}$$

- $x$ = $v_C$ (RC circuit) or $i_L$ (RL circuit)
- $\tau$ = the **time constant**, in seconds: $\;\tau=R_{th}C\;$ or $\;\tau=\dfrac{L}{R_{th}}$
- $x_f$ = the **final value** $x(\infty)$: where $x$ ends up long after the switch ($x_f=0$ if no source is left)
- $R_{th}$ = the resistance the $C$ or $L$ “sees” (how to find it is just below)

Examples of reading the form:

- $\dfrac{di}{dt}+5i=50$ → $\frac1\tau=5$, so $\tau=0.2\,\mathrm{s}$. And $\frac{x_f}{\tau}=50$, so $x_f=50\times0.2=10\,\mathrm{A}$.
- $\dfrac{dv}{dt}+50v=0$ → $\tau=\frac1{50}\,\mathrm{s}=20\,\mathrm{ms}$, and $x_f=0$ (no source).

**Finding $R_{th}$**, in the $t>0$ circuit:

1. **Turn the sources off:** a voltage source becomes a wire, a current source becomes a gap.
2. **Combine** the resistors between the two ends of the $C$ or $L$.

Example: a voltage source in series with $6\,\Omega$ feeds a capacitor, and a $3\,\Omega$ sits across the capacitor. The source becomes a wire, so the capacitor sees $6\parallel3=2\,\Omega$.

Why the sources go off: they only set the right side of the ODE ($x_f$). The speed, $\tau$, comes from the left side, which only has the resistors and the $C$ or $L$.

**The formula.** The ODE above is a [B2](#b2) equation with constants $a=\frac1\tau$ and $f=\frac{x_f}{\tau}$. Solve it once, with starting value $x(0)=x_0$, and you get the one formula you need:

$$x(t)=x_f+\big(x_0-x_f\big)\,e^{-t/\tau},\qquad t\ge0$$

Why it makes sense:

- at $t=0$: $e^0=1$, so $x=x_f+x_0-x_f=x_0$, the starting value ✓
- as $t\to\infty$: $e^{-t/\tau}\to0$, so $x\to x_f$, the final value ✓

**Method.** You don’t even have to write the ODE: find three numbers and plug in.

1. **$x_0$:** from the $t<0$ circuit ($C$ = gap, $L$ = wire). It carries over to $0^+$.
2. **$x_f$:** from the $t\to\infty$ circuit, with the switch in its **new** spot ($C$ = gap, $L$ = wire again).
3. **$\tau$:** find $R_{th}$ in the $t>0$ circuit. Then $\tau=R_{th}C$ or $\tau=L/R_{th}$.
4. **Plug in:** $x(t)=x_f+(x_0-x_f)e^{-t/\tau}$.
5. **Anything else** comes from $x(t)$: Ohm’s law, KCL, $i_C=C\frac{dv_C}{dt}$, $v_L=L\frac{di_L}{dt}$.

Two names you’ll see:

- **Natural response:** no source after $t=0$. The stored energy drains away through the resistors, so $x_f=0$.
- **Step response:** a DC source is still connected after $t=0$. It pushes $x$ to a new value $x_f$.

|  | Natural response | Step response |
|---|---|---|
| Final value | $x_f=0$ | $x_f$ from the new DC circuit |
| Answer | $x_0\,e^{-t/\tau}$ | $x_f+(x_0-x_f)\,e^{-t/\tau}$ |
| Example | $i=4e^{-500t}$ | $i=10\big(1-e^{-5t}\big)$ |

**How fast does it settle?** Count in time constants. After:

- $1\tau$: 37% of the gap $x_0-x_f$ is left (63% done), since $e^{-1}\approx0.37$
- $2\tau$: 13.5% left
- $5\tau$: under 1% left; call it done

Example: $\tau=2\,\mathrm{ms}$ → the circuit has settled after about $5\tau=10\,\mathrm{ms}$.

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

> **Info:** **Bonus (skip-safe): where the formula comes from (the lecture’s RC step response).** Take a current source $I_s$, a resistor $R$ and a capacitor $C$, all in parallel. KCL at the top node: capacitor current + resistor current = source current.
> 
> $$
> C\dfrac{dv}{dt}+\dfrac{v}{R}=I_s\quad\Rightarrow\quad\dfrac{dv}{dt}+\dfrac{v}{RC}=\dfrac{I_s}{C}
> $$
> 
> That’s the standard form with $\tau=RC$ and $x_f=RI_s$. Plug in: $v=RI_s+(V_0-RI_s)e^{-t/RC}$. You can solve it with [B2](#b2), or separate it ([B1](#b1)), as the lecture did for the RL circuit.

**Example: Example 9 · W3 · Circuit → ODE → answer · lecture §1.1**

The switch closes at $t=0$. The inductor carries no current before that. Find $i(t)$ for $t\ge0$.

```schematic
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$10\,\Omega$" i="$i$"
L1 6,3 -> 6,0 "$2\,\mathrm{H}$" v="$v$"
wire 6,0 -> 0,0
ground 0,0
```

1. **Type:** one inductor and one DC source → first-order RL **step** response. Solve for $i$, the inductor current.
2. **Before:** the switch is open, so no current flows: $i(0^-)=0$. It can’t jump, so $i(0^+)=0$ too.
3. **After:** KVL around the loop: source voltage = resistor voltage + inductor voltage.

   $$2\dfrac{di}{dt}+10i=100$$
4. **Standard form:** divide by $L=2$. Then $\frac1\tau=5$, so $\tau=0.2\,\mathrm{s}$ (check: $L/R=2/10$ ✓).

   $$\dfrac{di}{dt}+5i=50$$
5. **Final value:** long after, the inductor is a wire, so $i_f=100/10=10\,\mathrm{A}$.
6. **Plug in** $x_0=0$, $x_f=10$, $\tau=0.2$.

   $$i(t)=10+(0-10)e^{-5t}$$

**Answer:** $i(t)=10\big(1-e^{-5t}\big)\,\mathrm{A}$. Same answer as the integrating-factor problem in [B2](#b2).

**Problem: Problem 42 · W1 · RL natural response · Pre-tutorial 1** (introductory)

The switch has been closed for a long time and opens at $t=0$. Use $L=8\,\mathrm{mH}$, $R=4\,\Omega$ and $I_s=4\,\mathrm{A}$. Find $i(t)$ for $t\ge0$ (with numbers) and sketch it.

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

1. **Type:** once the switch opens, only $L$ and the $4\,\Omega$ are left in a loop, with no source. That’s an RL **natural** response. Solve for $i$.
2. **Before:** a long time, so $L$ is a wire. That wire shorts out $R_0$ and the $4\,\Omega$, so all of $I_s$ goes down through $L$.

   $$i(0^-)=4\,\mathrm{A}=i(0^+)$$
3. **After:** $L$ dumps its energy into the $4\,\Omega$. No source, so $x_f=0$.

   $$\tau=\dfrac{L}{R}=\dfrac{8\times10^{-3}}{4}=2\,\mathrm{ms}$$
4. **Plug in:** $\frac1\tau=500\,\mathrm{s^{-1}}$.

   $$i(t)=4e^{-500t}\,\mathrm{A}$$
5. **Sketch:** it starts at 4 A, drops to $4e^{-1}\approx1.47\,\mathrm{A}$ at $t=\tau=2\,\mathrm{ms}$, and is basically 0 after $5\tau=10\,\mathrm{ms}$.

**Answer:** $i(t)=4e^{-500t}\,\mathrm{A}$, $t\ge0$ ($\tau=2\,\mathrm{ms}$): an exponential decay from 4 A.

</details>

**Problem: Problem 43 · W2 · Can the capacitor current jump? · Pre-tutorial 2** (introductory)

The capacitor starts uncharged ($V_0=0$). The switch closes at $t=0$. Use $I_s=2\,\mathrm{A}$ and $R=1\,\mathrm{k\Omega}$. Find the capacitor current just before ($t=0^-$, switch open) and just after ($t=0^+$, switch closed). Does the capacitor current jump, even though the capacitor voltage can’t?

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

1. **Type:** a just-before / just-after question. Use “$v_C$ can’t jump”, then KCL at $0^+$.
2. **Before:** the switch is open, so the capacitor isn’t connected to anything.

   $$i_C(0^-)=0$$
3. **Just after:** $v(0^+)=v(0^-)=0$, since it can’t jump. The resistor sits across the capacitor, so its current is $v/R=0$.
4. **KCL** at the top node: the resistor takes nothing, so all of the source current goes into the capacitor.

   $$i_C(0^+)=I_s-\dfrac{v(0^+)}{R}=2-0=2\,\mathrm{A}$$
5. **Afterwards:** $v$ rises toward $RI_s=2000\,\mathrm{V}$ and $i_C$ dies down to 0.

**Answer:** $i_C(0^-)=0$, $i_C(0^+)=2\,\mathrm{A}$. So yes, the capacitor **current** jumps. The capacitor **voltage** doesn’t: it stays at 0.

</details>

**Problem: Problem 44 · W2–W3 · Read the circuit from its response · textbook P7.42** (intermediate)

The switch closes at $t=0$. For $t\ge0$ you measure:

$i(t)=\big(10-10e^{-500t}\big)\,\mathrm{A},\qquad v(t)=200e^{-500t}\,\mathrm{V}\ (t\ge0^+)$

Find $V_s$, $R$, the starting current $I_0$ and $L$.

```schematic
V1 0,3 -> 0,0 "$V_s$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$R$" i="$i$"
L1 6,3 -> 6,0 "$L$" v="$v$"
wire 6,0 -> 0,0
ground 0,0
```

<details><summary>Solution</summary>

1. **Type:** RL step response, read backwards. Match each piece to $x_f+(x_0-x_f)e^{-t/\tau}$.
2. **Starting value:** put $t=0$ into $i(t)$: $I_0=10-10=0$.
3. **Just after:** $i=0$, so the resistor has 0 V across it. The whole source voltage sits on $L$.

   $$V_s=v(0^+)=200\,\mathrm{V}$$
4. **Final value:** long after, $L$ is a wire, so $i_f=V_s/R$. From $i(t)$, $i_f=10$.

   $$10=\dfrac{200}{R}\quad\Rightarrow\quad R=20\,\Omega$$
5. **Time constant:** the exponent is $-500t$, so $\frac1\tau=500$ and $\tau=2\,\mathrm{ms}$. Use $\tau=L/R$.

   $$L=20\times0.002=40\,\mathrm{mH}$$
6. **Check:** $L\frac{di}{dt}=0.04\times5000e^{-500t}=200e^{-500t}$, which matches $v(t)$ ✓.

**Answer:** $V_s=200\,\mathrm{V}$, $R=20\,\Omega$, $I_0=0$, $L=40\,\mathrm{mH}$.

</details>

**Problem: Problem 45 · W2 · RC natural response with a divider first · textbook P7.22** (intermediate)

The switch has been closed for a long time and opens at $t=0$. Find (a) $v(0)$, (b) $\tau$ for $t>0$, (c) $v(t)$, (d) the energy stored in the capacitor at $t=0$.

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

1. **Type:** once the switch opens, only $C$ and the $50\,\mathrm{k\Omega}$ are left, with no source. RC **natural** response. Solve for $v$.
2. **Before:** $C$ is a gap, so the source current has two paths: the $80\,\mathrm{k\Omega}$, or $20+50=70\,\mathrm{k\Omega}$. Current divider:

   $$i_{70}=7.5\,\mathrm{mA}\cdot\dfrac{80}{80+70}=4\,\mathrm{mA}$$
3. (a) $v$ is the voltage across the $50\,\mathrm{k\Omega}$ (it sits on the same two nodes as $C$).

   $$v(0^-)=4\,\mathrm{mA}\times50\,\mathrm{k\Omega}=200\,\mathrm{V}=v(0^+)$$
4. (b) **After:** $C$ only sees the $50\,\mathrm{k\Omega}$.

   $$\tau=RC=50\times10^3\times0.4\times10^{-6}=20\,\mathrm{ms}$$
5. (c) **Plug in** $x_f=0$, $\frac1\tau=50\,\mathrm{s^{-1}}$.

   $$v(t)=200e^{-50t}\,\mathrm{V}$$
6. (d) **Energy:** use $w=\frac12Cv^2$ with $v(0)=200\,\mathrm{V}$.

   $$w=\tfrac12Cv^2=\tfrac12(0.4\times10^{-6})(200)^2=8\,\mathrm{mJ}$$

**Answer:** (a) $200\,\mathrm{V}$. (b) $20\,\mathrm{ms}$. (c) $v(t)=200e^{-50t}\,\mathrm{V}$, $t\ge0$. (d) $8\,\mathrm{mJ}$.

</details>

**Problem: Problem 46 · W1–W2 · The sign of the reference arrow · textbook P7.1** (intermediate)

The switch has been closed for a long time and opens at $t=0$. Watch the direction of $i$: it points **up** through the inductor. Find (a) the starting value of $i$, (b) the energy stored in the inductor at $t=0$, (c) the time constant for $t>0$, (d) $i(t)$ for $t\ge0$, with numbers.

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

1. **Type:** once the switch opens, only $L$ and the $2\,\Omega$ are left, with no source. RL **natural** response. Solve for $i$.
2. **Before:** $L$ is a wire, and it shorts out the $2\,\Omega$. So the source sees $3\,\Omega$ in series with $30\parallel6=5\,\Omega$.

   $$I=\dfrac{120}{3+5}=15\,\mathrm{A}$$
3. The middle node sits at $120-15\times3=75\,\mathrm{V}$. So $75/6=12.5\,\mathrm{A}$ goes right through the $6\,\Omega$, then **down** through $L$.
4. (a) The arrow points **up**, but the real current goes down, so the value is negative.

   $$i(0^-)=i(0^+)=-12.5\,\mathrm{A}$$
5. (b) **Energy:** the sign doesn’t matter, because $i$ gets squared.

   $$w=\tfrac12(8\times10^{-3})(12.5)^2=0.625\,\mathrm{J}$$
6. (c) **After:** $L$ only sees the $2\,\Omega$.

   $$\tau=\dfrac{L}{R}=\dfrac{8\times10^{-3}}{2}=4\,\mathrm{ms}$$
7. (d) **Plug in** $x_0=-12.5$, $x_f=0$, $\frac1\tau=250$.

   $$i(t)=-12.5e^{-250t}\,\mathrm{A}$$

**Answer:** (a) $-12.5\,\mathrm{A}$. (b) $0.625\,\mathrm{J}$. (c) $4\,\mathrm{ms}$. (d) $i(t)=-12.5e^{-250t}\,\mathrm{A}$, $t\ge0$.

</details>

**Problem: Problem 47 · W2 · Step response that needs a Thévenin equivalent · textbook P7.52(a)** (advanced)

The switch has been at $a$ for a long time. At $t=0$ it moves to $b$ and stays there. Find the starting and final capacitor voltage, the time constant for $t\ge0$, and $v_C(t)$ for $t\ge0$. (The $200\,\mathrm{V}$ source has its $-$ on top. The two $t=0$ switches are one two-position switch: at $t=0$ the contact at $a$ opens and the contact at $b$ closes.)

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

1. **Type:** one capacitor, and a DC source still connected after the switch. RC **step** response. Solve for $v_C$.
2. **Before (at $a$):** $C$ is a gap, so no current flows through the $10\,\mathrm{k\Omega}$ and it drops 0 V. The capacitor gets the full source.

   $$v_C(0^-)=120\,\mathrm{V}=v_C(0^+)$$
3. **After (at $b$):** shrink everything right of $b$ into one source $V_{th}$ plus one resistor $R_{th}$ (Thévenin). Then it’s a plain RC loop.
4. **$V_{th}$:** take $C$ out. No current flows in the $12.5\,\mathrm{k\Omega}$, so $V_{th}$ is the voltage on the $150\,\mathrm{k\Omega}$: a divider with the $50\,\mathrm{k\Omega}$. The source’s top is at $-200\,\mathrm{V}$.

   $$V_{th}=-200\cdot\dfrac{150}{150+50}=-150\,\mathrm{V}$$
5. **$R_{th}$:** turn the source off (it becomes a wire). That leaves $12.5\,\mathrm{k\Omega}$ in series with $150\parallel50=37.5\,\mathrm{k\Omega}$.

   $$R_{th}=12.5+37.5=50\,\mathrm{k\Omega}$$
6. **Final value and time constant:** in the end $C$ is a gap again, so no current flows and $C$ sits at $V_{th}$.

   $$\begin{gathered}v_f=-150\,\mathrm{V}, \\ \tau=(50\times10^{3})(40\times10^{-9})=2\,\mathrm{ms}\end{gathered}$$
7. **Plug in:** $x_0-x_f=120-(-150)=270$, $\frac1\tau=500$.

   $$v_C(t)=-150+270e^{-500t}\,\mathrm{V}$$

**Answer:** $v_C(0)=120\,\mathrm{V}$, $v_C(\infty)=-150\,\mathrm{V}$, $\tau=2\,\mathrm{ms}$, $v_C(t)=-150+270e^{-500t}\,\mathrm{V}$, $t\ge0$.

</details>

### D2 · RLC circuits (second order)

[Week 5 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/0c7a77fe-aeed-47a8-b1c3-4967d73eea21#d5ad9ba9-0ec5-4b62-acf5-b1c7e17d6463)

**What if the circuit has an inductor *and* a capacitor?** Each one brings a derivative, so together they give a **second-order** ODE (one with $y^{\prime\prime}$ in it). Combine series/parallel $L$’s and $C$’s first, so you have one of each.

You already know how to solve it: [B5](#b5) when no source is left, [B6](#b6) when a source stays on. The new part is reading the equation and the two starting values off the circuit.

**The two circuits you will meet.** Learn both equations. Where they come from is in the Bonus box further down.

```schematic
V1 0,3 -> 0,0 "$V_s$"
R1 0,3 -> 3,3 "$R$" i="$i$"
L1 3,3 -> 6,3 "$L$"
C1 6,3 -> 6,0 "$C$" v="$v_C$"
wire 6,0 -> 0,0
ground 0,0
```

**Series:** solve for the capacitor voltage $v_C$.

$$v_C^{\prime\prime}+\dfrac{R}{L}v_C^{\prime}+\dfrac{1}{LC}v_C=\dfrac{V_s}{LC}$$

- $\alpha=\dfrac{R}{2L}$ = the **damping**: how fast the response dies out (half the $v_C^{\prime}$ number)
- $\omega_0=\dfrac{1}{\sqrt{LC}}$ = the **natural frequency**: how fast it would swing with no $R$ (square root of the $v_C$ number)
- right side $\dfrac{V_s}{LC}$ = the source. It is $0$ when no source is left.

Example: $R=4\,\Omega$, $L=1\,\mathrm{H}$, $C=0.25\,\mathrm{F}$ → $\alpha=\dfrac{4}{2}=2$ and $\omega_0=\dfrac{1}{\sqrt{0.25}}=2$.

```schematic
C1 0,3 -> 0,0 "$C$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$L$" i="$i_L$"
wire 3,3 -> 6,3
R1 6,3 -> 6,0 "$R$" i="$i_R$"
wire 6,0 -> 0,0
ground 0,0
```

**Parallel:** solve for the shared voltage $v$.

$$v^{\prime\prime}+\dfrac{1}{RC}v^{\prime}+\dfrac{1}{LC}v=0$$

- $\alpha=\dfrac{1}{2RC}$, **not** $\dfrac{R}{2L}$. Here a bigger $R$ means *less* damping: a big resistor in parallel takes almost no current, so it barely drains energy.
- $\omega_0=\dfrac{1}{\sqrt{LC}}$, the same as in series.

Example: $R=800\,\Omega$, $C=50\,\mathrm{nF}$ → $\alpha=\dfrac{1}{2(800)(50\times10^{-9})}=12500\,\mathrm{s^{-1}}$.

Both equations have the same characteristic equation. That is why $\alpha$ has the $2$ and $\omega_0$ the square: the roots come out clean.

$$s^2+2\alpha s+\omega_0^2=0$$

$$s=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}$$

**Which form? Compare $\alpha$ with $\omega_0$.** It is the root table of [B5](#b5), with circuit names:

| Compare | Roots | Name | Form of the response |
|---|---|---|---|
| $\alpha>\omega_0$ | two real | **overdamped** | $A_1e^{s_1t}+A_2e^{s_2t}$ |
| $\alpha=\omega_0$ | one repeated | **critically damped** | $(A_1+A_2t)e^{-\alpha t}$ |
| $\alpha<\omega_0$ | $-\alpha\pm j\omega_d$ | **underdamped** | $e^{-\alpha t}(B_1\cos\omega_dt+B_2\sin\omega_dt)$ |
| $\alpha=0$ (no $R$) | $\pm j\omega_0$ | **undamped** (LC) | $B_1\cos\omega_0t+B_2\sin\omega_0t$ |

In the underdamped row, the square root in the roots is of a negative number, so the roots are $-\alpha\pm j\omega_d$. $\omega_d$ is how fast the response swings:

$$\omega_d=\sqrt{\omega_0^2-\alpha^2}$$

Example: $\alpha=3$, $\omega_0=5$ → $\omega_d=\sqrt{25-9}=4$, so $v=e^{-3t}(B_1\cos4t+B_2\sin4t)$. (In the B5 table, $\sigma=-\alpha$ and $\omega=\omega_d$.)

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
caption "$\omega_0=2$ never changes; only $\alpha=R/2$ moves. $R<4$: underdamped, it swings below zero before settling. $R=4$: critically damped, the fastest way back with no overshoot. $R>4$: overdamped, a slow creep back. $R=0$: undamped, it swings forever."
```

**A second-order ODE needs two starting values: $y(0)$ and $y^{\prime}(0)$.** The value is easy: $v_C$ can’t jump, so $v_C(0^+)=v_C(0^-)$. The slope comes from the capacitor current:

$$v_C^{\prime}(0^+)=\dfrac{i_C(0^+)}{C}$$

Why: it is $i_C=C\,\dfrac{dv_C}{dt}$, divided by $C$. So the job is to find $i_C$ at $0^+$:

- **Series:** $i_C$ is the loop current $i$, which is also $i_L$, so it carries over from $0^-$. Sign: $+$ if the $i$ arrow enters the $+$ end of $C$, $-$ if it leaves it. Example: $i(0^-)=0$ → $v_C^{\prime}(0^+)=0$.
- **Parallel:** KCL at the top node at $0^+$ (all arrows down): $i_C=-(i_L+i_R)$, with $i_R=\dfrac{v(0^+)}{R}$. Example: $v=10\,\mathrm{V}$, $R=5\,\Omega$, $i_L=1\,\mathrm{A}$, $C=0.5\,\mathrm{F}$ → $i_C=-(1+2)=-3\,\mathrm{A}$, so $v^{\prime}(0^+)=-6\,\mathrm{V/s}$.
- **Series, solving for $i$ instead:** $i(0^+)=i_L(0^-)$, and the slope is $i^{\prime}(0^+)=\dfrac{v_L(0^+)}{L}$, with $v_L$ from KVL around the loop. Example: $v_C=70\,\mathrm{V}$, $i=0$, $L=0.1\,\mathrm{H}$ → $v_L=70$, $i^{\prime}(0^+)=700\,\mathrm{A/s}$.

**What if a source stays on after the switch?** (a **step response**) Then the answer does not die out to $0$. It settles to a **final value** $V_f$:

$$v_C(t)=V_f+(\text{part that dies out})$$

- $V_f$ = the new DC steady state ($C$ open, $L$ short). It is the constant $y_p$ of [B6](#b6).
- the part that dies out = the form from the table above.

Example: $v_C=100+(A_1+A_2t)e^{-50t}$ has $V_f=100\,\mathrm{V}$.

> **Warning:** **Fit the constants to the whole answer, final value included.** With $v_C(0)=200$: $\;100+A_1=200$, so $A_1=100$, not $200$.

**Method:**

1. **Before:** the old circuit in DC steady state ($C$ open, $L$ short). Find $v_C(0^-)$ and $i_L(0^-)$.
2. **Starting values:** both carry over to $0^+$. Then find the slope from $i_C$ (see above).
3. **Equation:** series or parallel? Compute $\alpha$ and $\omega_0$, compare them, and pick the form from the table.
4. **Final value:** $0$ if no source is left. Otherwise, the new DC steady state.
5. **Constants:** use the starting value and slope on the whole answer. Use the product rule for the slope.

> **Warning:** **Units.** Turn $\mathrm{mH}$, $\mathrm{mF}$, $\mu\mathrm{F}$, $\mathrm{nF}$ into H and F before computing $\alpha$ and $\omega_0$: $1\,\mathrm{mH}=10^{-3}\,\mathrm{H}$, $1\,\mu\mathrm{F}=10^{-6}\,\mathrm{F}$, $1\,\mathrm{nF}=10^{-9}\,\mathrm{F}$. Example: $L=250\,\mathrm{mH}$, $C=10\,\mathrm{nF}$ → $\omega_0=\dfrac{1}{\sqrt{0.25\times10^{-8}}}=20000$.

> **Info:** **Bonus (skip-safe): where the series equation comes from.** KVL around the loop, then swap the current for $Cv_C^{\prime}$:
> 
> ```steps
> $$ V_s=Ri+Li^{\prime}+v_C $$
> KVL: the voltages on R, L and C add up to the source.
> $$ i=\hl{Cv_C^{\prime}} $$
> The loop current is the capacitor current.
> $$ V_s=RC\,v_C^{\prime}+LC\,v_C^{\prime\prime}+v_C $$
> Put that current (and its derivative) into the KVL line.
> $$ v_C^{\prime\prime}+\hl{\dfrac RL}v_C^{\prime}+\hl{\dfrac1{LC}}v_C=\hl{\dfrac{V_s}{LC}} $$
> Divide by $LC$ so $v_C^{\prime\prime}$ stands alone.
> ```
> 
> Parallel: KCL at the top node gives $Cv^{\prime}+i_L+\dfrac vR=0$. Differentiate once, use $i_L^{\prime}=\dfrac vL$, and divide by $C$.

**Example: Example 10 · W5 · A series step response · textbook P8.53**

The circuit has been running for a long time with $V_s=200\,\mathrm{V}$. At $t=0$ the source drops to $100\,\mathrm{V}$. Find $v_C(t)$ for $t\ge0$.

```schematic
V1 0,3 -> 0,0 "$200\to100\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$" i="$i$"
L1 3,3 -> 6,3 "$40\,\mathrm{mH}$"
C1 6,3 -> 6,0 "$10\,\mathrm{mF}$" v="$v_C$"
wire 6,0 -> 0,0
ground 0,0
```

1. **Type:** one $L$ and one $C$ in one loop, and a source that stays on: a series RLC step response.
2. **Before:** long time, so DC steady state. $C$ is open, so $i=0$. With no current, $R$ and $L$ drop nothing, so $C$ holds the whole 200 V.

   $$v_C(0^-)=200\,\mathrm{V},\quad i(0^-)=0$$
3. **Starting values:** $v_C$ and $i$ can’t jump. The slope is $i/C$, and $i=0$.

   $$v_C(0^+)=200,\quad v_C'(0^+)=\dfrac{0}{0.01}=0$$
4. **Equation:** $\alpha=\frac{R}{2L}=\frac{4}{2(0.04)}=50$ and $\omega_0=\frac{1}{\sqrt{LC}}=\frac{1}{\sqrt{0.04\times0.01}}=50$. They are equal, so it is critically damped.

   $$v_C''+100v_C'+2500v_C=250000$$
5. **Final value:** long after the switch, $C$ is open again and holds the new source, so $v_C\to100\,\mathrm{V}$. Answer = final value + the repeated-root form.

   $$v_C=100+(A_1+A_2t)e^{-50t}$$
6. **Constants:** put in $t=0$. The value $v_C(0)=200$ gives $A_1$.

   $$100+A_1=200\ \Rightarrow\ A_1=100$$
7. The slope at $0$ (product rule) is $A_2-50A_1$, and it must be $0$.

   $$A_2-50A_1=0\ \Rightarrow\ A_2=5000$$

**Answer:** $v_C=100+(100+5000t)e^{-50t}\,\mathrm{V}$, $t\ge0$ ($t$ in seconds). It starts at 200 V with zero slope and settles at 100 V without overshooting.

**Problem: Problem 48 · W5 · No resistor: an ideal LC circuit · textbook P8.14** (introductory)

A $250\,\mathrm{mF}$ capacitor and a $0.4\,\mathrm{H}$ inductor are in parallel. At the start, $v(0)=0$ and $i_L(0)=-3\,\mathrm{A}$ (arrow pointing down). Find (a) $v(t)$, (b) its frequency in rad/s, (c) its maximum amplitude.

```schematic
C1 0,3 -> 0,0 "$250\,\mathrm{mF}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$0.4\,\mathrm{H}$" i="$i_L$"
wire 3,0 -> 0,0
ground 0,0
```

<details><summary>Solution</summary>

1. **Type:** parallel with no $R$, so $\alpha=0$: undamped. $\frac{1}{LC}=\frac{1}{0.25\times0.4}=10$.

   $$v''+\dfrac{1}{LC}v=v''+10v=0$$
2. **Form:** $\omega_0=\sqrt{10}$. The cosine coefficient is $v(0)=0$, so only the sine is left.

   $$v=B\sin(\sqrt{10}\,t)$$
3. **Starting slope:** KCL at the top node: $i_C+i_L=0$, so $i_C(0^+)=+3\,\mathrm{A}$ (down). Divide by $C$.

   $$v'(0^+)=\dfrac{3}{0.25}=12\,\mathrm{V/s}$$
4. **Constant:** the slope of $B\sin(\sqrt{10}\,t)$ at $0$ is $\sqrt{10}\,B$. Set it equal to 12.

   $$B=\dfrac{12}{\sqrt{10}}\approx3.795$$

**Answer:** (a) $v=\dfrac{12}{\sqrt{10}}\sin(\sqrt{10}\,t)\,\mathrm{V}$. (b) $\omega_0=\sqrt{10}\approx3.162\,\mathrm{rad/s}$. (c) $3.795\,\mathrm{V}$. With no $R$, nothing uses up the energy, so it never dies out.

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

1. **Type:** two decaying exponentials means two real roots: overdamped. The exponents are the roots, $s_1=-5000$ and $s_2=-20000$.
2. **Roots → equation:** multiply out $(s+5000)(s+20000)$ and line it up with $s^2+2\alpha s+\omega_0^2$.

   $$s^2+25000s+10^8=0$$
3. Read off: $2\alpha=25000$ and $\omega_0^2=10^8$.

   $$\alpha=12500\,\mathrm{s^{-1}},\quad\omega_0=10^4\,\mathrm{rad/s}$$
4. **$L$:** use $\omega_0^2=\dfrac{1}{LC}$.

   $$L=\dfrac{1}{10^8\times50\times10^{-9}}=0.2\,\mathrm{H}$$
5. **$R$:** it is parallel, so use $\alpha=\dfrac{1}{2RC}$.

   $$R=\dfrac{1}{2(12500)(50\times10^{-9})}=800\,\Omega$$

**Answer:** $\alpha=12500\,\mathrm{s^{-1}}$, $\omega_0=10^4\,\mathrm{rad/s}$, $L=0.2\,\mathrm{H}$, $R=800\,\Omega$.

</details>

**Problem: Problem 50 · W5 · Switch to a series loop · textbook P8.44** (intermediate)

The switch has been at $a$ for a long time. At $t=0$ it moves to $b$. Find $i(t)$ for $t\ge0$.

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

1. **Type:** after the switch, $C$, the $200\,\Omega$ and $L$ form one loop with no source: a series RLC natural response. We solve for $i$, the inductor current.
2. **Before:** at $a$, $C$ is open (steady state), so no current flows in the $50\,\Omega$ and $C$ charges to the full 70 V. $L$ isn’t connected, so its current is 0.

   $$v_C(0^-)=70\,\mathrm{V},\quad i(0^-)=0$$
3. **Starting slope:** KVL around the new loop is $v_C=Ri+L\,i^{\prime}$. At $0^+$, $v_C=70$ and $i=0$.

   $$i'(0^+)=\dfrac{70-200(0)}{0.1}=700\,\mathrm{A/s}$$
4. **Equation:** $\alpha=\dfrac{R}{2L}=\dfrac{200}{2(0.1)}=1000$ and $\omega_0^2=\dfrac{1}{LC}=\dfrac{1}{0.1\times200\times10^{-9}}=5\times10^7$. $\alpha^2=10^6$ is smaller, so underdamped.

   $$\omega_d=\sqrt{5\times10^7-10^6}=7000\,\mathrm{rad/s}$$
5. **Form:** the cosine coefficient is $i(0)=0$, so only the sine is left.

   $$i=B\,e^{-1000t}\sin7000t$$
6. **Constant:** the slope of this at $t=0$ is $7000B$. Set it equal to 700.

   $$B=0.1$$

**Answer:** $i=0.1\,e^{-1000t}\sin7000t\ \mathrm{A}$ $=100\,e^{-1000t}\sin7000t\ \mathrm{mA}$, $t\ge0$.

</details>

**Problem: Problem 51 · W5 · The slope comes from KCL · textbook P8.7** (intermediate)

$R=\tfrac{12500}{3}\,\Omega$, $L=250\,\mathrm{mH}$ and $C=10\,\mathrm{nF}$ are in parallel. At the start, $v(0)=90\,\mathrm{V}$ and $i_L(0)=-30\,\mathrm{mA}$ (arrows as drawn). Find $v(t)$ for $t\ge0$.

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

1. **Type:** parallel RLC, no source: a natural response.
2. **Starting slope:** first the resistor current, $i_R=\dfrac{90}{12500/3}=21.6\,\mathrm{mA}$. KCL at the top node (all arrows down): $i_C+i_L+i_R=0$, so $i_C=-(-30)-21.6$.

   $$i_C(0^+)=30-21.6=8.4\,\mathrm{mA}$$
3. Divide by $C$ to get the slope.

   $$v'(0^+)=\dfrac{8.4\times10^{-3}}{10^{-8}}=8.4\times10^5\,\mathrm{V/s}$$
4. **Equation:** $\alpha=\dfrac{1}{2RC}=12000$ and $\omega_0=\dfrac{1}{\sqrt{LC}}=20000$. $\alpha<\omega_0$, so underdamped.

   $$\omega_d=\sqrt{20000^2-12000^2}=16000$$
5. **Form:** the cosine coefficient is $v(0)=90$.

   $$v=e^{-12000t}(90\cos16000t+B_2\sin16000t)$$
6. **Constant:** the slope at $0$ is $-\alpha(90)+\omega_dB_2$ (the $y^{\prime}(0)$ column of the B5 table). Set it equal to $8.4\times10^5$.

   $$-12000(90)+16000B_2=840000\ \Rightarrow\ B_2=120$$

**Answer:** $v=e^{-12000t}(90\cos16000t+120\sin16000t)\,\mathrm{V}$, $t\ge0$.

</details>

**Problem: Problem 52 · W5 · Choose R for critical damping · textbook P8.42** (advanced)

$R$ is set so the circuit is critically damped. When the switch closes, $v_C=90\,\mathrm{V}$ and the inductor current is $i=24\,\mathrm{mA}$. Find (a) $R$, (b) $i$ and $\dfrac{di}{dt}$ just after closing, (c) $i(t)$ and $v_C(t)$ for $t\ge0$.

```schematic
C1 0,3 -> 0,0 "$160\,\mathrm{nF}$" v="$v_C$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$R$" i="$i$"
L1 6,3 -> 6,0 "$250\,\mathrm{mH}$"
wire 6,0 -> 0,0
ground 0,0
```

<details><summary>Solution</summary>

1. **Type:** one loop, no source: a series RLC natural response. Critically damped means $\alpha=\omega_0$.
2. **(a)** $\omega_0=\dfrac{1}{\sqrt{0.25\times160\times10^{-9}}}=5000$. Set $\alpha=\dfrac{R}{2L}=5000$ and solve for $R$.

   $$R=2(0.25)(5000)=2500\,\Omega$$
3. **(b)** $i$ is the inductor current, so it can’t jump: $i(0^+)=24\,\mathrm{mA}$. For the slope, use KVL around the loop, $v_C=Ri+L\,i^{\prime}$, at $0^+$.

   $$i'(0^+)=\dfrac{90-2500(0.024)}{0.25}=120\,\mathrm{A/s}$$
4. **(c) Form:** critically damped, so one repeated root $s=-\alpha=-5000$.

   $$i=(A_1+A_2t)e^{-5000t}$$
5. **Constants:** $A_1=i(0)=0.024$. The slope at $0$ is $A_2-5000A_1$; set it equal to 120.

   $$A_2=240$$
6. For $v_C$, use the same KVL: $v_C=Ri+L\,i^{\prime}$. (Check: $i=-C\,v_C^{\prime}$, with a minus because $i$ leaves the $+$ of $C$.)

   $$v_C=(90+3\times10^5\,t)e^{-5000t}$$

**Answer:** (a) $R=2500\,\Omega$. (b) $i(0^+)=24\,\mathrm{mA}$, $i^{\prime}(0^+)=120\,\mathrm{A/s}$. (c) $i=(0.024+240t)e^{-5000t}\,\mathrm{A}$, $v_C=(90+3\times10^5t)e^{-5000t}\,\mathrm{V}$.

</details>

**Problem: Problem 53 · W5 + W6 · The answer is zero · textbook P8.24** (advanced)

The switch has been open for a long time and the capacitor is uncharged. At $t=0$ the switch closes. Find $v_o(t)$ for $t\ge0$.

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

1. **Type:** after closing, $L$ and $C$ sit across the same two nodes, fed by the source through $400\,\Omega$: a parallel RLC with a DC source.
2. **Before:** steady state, so $L$ is a short and takes the whole source current. $C$ isn’t connected and has no charge.

   $$i_L(0^-)=\dfrac{12}{400}=30\,\mathrm{mA},\quad v_o(0^-)=0$$
3. **Starting slope:** at $0^+$, $v_o=0$, so the $400\,\Omega$ still carries $30\,\mathrm{mA}$. $L$ still takes all 30 mA (it can’t jump). KCL at the top node leaves nothing for $C$.

   $$i_C(0^+)=30-30=0\ \Rightarrow\ v_o^{\prime}(0^+)=0$$
4. **Equation:** KCL at the top node is $\dfrac{v_o-12}{400}+i_L+Cv_o^{\prime}=0$. Differentiate once: the constant 12 disappears, so the right side is $0$.

   $$Cv_o''+\dfrac{v_o'}{400}+\dfrac{v_o}{L}=0$$
5. **Condition:** right side $0$, $v_o(0)=0$ and $v_o^{\prime}(0)=0$. The only solution that fits is $v_o=0$ (the zero-start rule in [Topic C](#topic-c)).

**Answer:** $v_o(t)=0$ for all $t\ge0$. The inductor already carries the whole source current, so nothing ever flows into the capacitor.

</details>
