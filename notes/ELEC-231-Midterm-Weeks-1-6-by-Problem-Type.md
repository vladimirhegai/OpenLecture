# ELEC 231 Midterm: Weeks 1–6 by Problem Type

## Start here: what the midterm asks

**Midterm:** Friday Oct 30 · 2 hours · 30 marks · Casio 991 only.

**What’s on it** (announced in class): everything up to and including Monday Oct 26’s lecture (the comments on undetermined coefficients), plus this week’s tutorials (Mon Oct 26 and Wed Oct 28). That is every section of this note.

- **Not on it: Laplace transforms.** Skip them for now.
- **This week’s tutorial problem** is Pre-tutorial 5: $y^{\prime\prime}+y=6\cos^2t$ with $y(0)=0$, $y(\pi/2)=0$. It’s the “know this cold” card in [B6](#b6). Practise it until you can do it without looking.

Every solution in this note has the same shape. Use it on the exam too. Naming the type first is what tells you which steps to run.

1. **Type:** say what kind of problem it is, and the clue that told you. Example: “$y^{\prime}=t^2y$ is separable: the right side is a $t$-part times a $y$-part.”
2. **Steps:** run that section’s numbered steps, using its words. Every method starts with **Write** (put it in its form).
3. **Plug in:** use the given values to find the constants. Example: $y=Ce^{2t}$ with $y(0)=5$ gives $C=5$. (In a circuit, the values come from the circuit just before the switch moves.)

**Where do I go?** Find what your question gives you in the left column, then click the link. The browser’s Back button brings you back here.

| The question gives you… | Go to | Weeks |
|---|---|---|
| a complex number to convert, multiply, divide, raise to a power or take roots of | [Topic A](#topic-a) | 1 |
| an ODE to classify, or a function to check as a solution | [Topic B](#topic-b) | 2 |
| a first-order ODE where you can split the $y$’s from the $t$’s | [B1 · Separable](#b1) | 3 |
| $y^{\prime}+p(t)\,y=f(t)$ | [B2 · Integrating factor](#b2) | 3 |
| $M\,dt+N\,dy=0$ | [B3 · Exact](#b3), [B4 · Make it exact](#b4) | 4 |
| $ay^{\prime\prime}+by^{\prime}+cy=0$ (numbers $a,b,c$) | [B5 · Characteristic equation](#b5) | 4–5 |
| $ay^{\prime\prime}+by^{\prime}+cy=f(t)$ | [B6 · Undetermined coefficients](#b6) | 6 |
| a second-order ODE with $t$ in the coefficients, and one solution given | [B7 · Reduction of order](#b7) | 6 |
| “does a unique solution exist?”, an interval, or two solutions to compare | [Topic C](#topic-c) | 3, 5, 6 |
| a circuit with a switch: find $v(t)$ or $i(t)$ | [Topic D](#topic-d) | 1–3, 5 |
| a mixed set of exam-style problems, to practise like the real thing | [Topic E](#topic-e) | 1–6 |

## Topic A: Complex numbers

[Week 1 · Topic 1](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/1cbac07a-cd02-48c2-8c30-c9829c4e06b2#079a564f-840a-46b1-9f12-5d8d123edad9) [Week 1 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/1cbac07a-cd02-48c2-8c30-c9829c4e06b2#fef2e73f-cd85-498c-9b6a-1ff1e058d7d3)

**Use this when** you have to convert, multiply, divide, raise to a power, or take roots of a complex number. (They also show up inside [B5](#b5) Case 3: $\sqrt{-36}=j6$.)

**The move: every complex number has two forms.** Pick the one that makes the job easy.

$$
z=a+jb\quad=\quad c\angle\theta\quad(=c\,e^{j\theta})
$$

- $a+jb$ (**rectangular**): $a$ = how far right, $b$ = how far up. Easy for **adding**.
- $c\angle\theta$ (**polar**): $c$ = the length, $\theta$ = the angle from the positive real axis. Easy for **multiplying, dividing, powers, roots**.
- $j=\sqrt{-1}$, so $j^2=-1$. (This course writes $j$, not $i$.)

**Short example:**

$$
3+j4=5\angle53.13^\circ
$$

<details><summary>Why does multiplying add the angles? (optional)</summary>

Write both as exponentials and use $e^Ae^B=e^{A+B}$:

$$
c_1e^{j\theta_1}\cdot c_2e^{j\theta_2}=c_1c_2\,e^{j(\theta_1+\theta_2)}
$$

The two forms are linked by Euler’s identity, $e^{j\theta}=\cos\theta+j\sin\theta$. The lecture uses it for trig identities: expand $e^{jA}e^{jB}=e^{j(A+B)}$, and the real parts give $\cos(A+B)=\cos A\cos B-\sin A\sin B$.

</details>

#### Case 1: convert between the forms

**Polar → rectangular** (the arrow is the long side of a right triangle):

$$
a=c\cos\theta,\qquad b=c\sin\theta
$$

$$
2\angle30^\circ=2\cos30^\circ+j\,2\sin30^\circ=\sqrt3+j
$$

**Rectangular → polar** (Pythagoras, then $\tan^{-1}$):

$$
\begin{gathered}c=\sqrt{a^2+b^2}, \\ \theta=\tan^{-1}\!\left(\dfrac{b}{a}\right)\end{gathered}
$$

$$
3+j4:\quad c=\sqrt{9+16}=5,\quad \theta=\tan^{-1}\tfrac43=53.13^\circ
$$

> **Warning:** **The quadrant trap.** The calculator’s $\tan^{-1}$ only gives arrows pointing right. If $a<0$ (pointing left), **add $180^\circ$**. Example: $-1+j$. The calculator says $-45^\circ$, but the real angle is $-45^\circ+180^\circ=135^\circ$.

#### Case 2: multiply, divide, powers

Go **polar**. Lengths multiply/divide, angles add/subtract:

$$
2\angle30^\circ\times3\angle40^\circ=6\angle70^\circ
$$

$$
\dfrac{6\angle70^\circ}{3\angle40^\circ}=2\angle30^\circ
$$

**Power** (de Moivre): length to the power, angle times the power:

$$
(2\angle30^\circ)^3=8\angle90^\circ
$$

**Dividing in rectangular?** Multiply top and bottom by the **conjugate** of the bottom ($a+jb\to a-jb$). The bottom becomes $a^2+b^2$, a plain number:

$$
\dfrac{1}{1+j}=\dfrac{1-j}{(1+j)(1-j)}=\dfrac{1-j}{2}
$$

Adding or subtracting? Stay rectangular: $(1+j2)+(3-j5)=4-j3$.

<details><summary>Powers of $j$: $\;j^2=-1,\ \ j^3=-j,\ \ j^4=1,\ \ \dfrac1j=-j$</summary>

Step 1 · They repeat every four.

$$
j^3=j^2\cdot j=-j,\qquad j^4=(j^2)^2=1
$$

Step 2 · Dividing by $j$: multiply top and bottom by $j$.

$$
\dfrac1j=\dfrac{j}{j\cdot j}=\dfrac{j}{-1}=-j
$$

</details>

#### Case 3: roots (k answers)

A $k$-th root has **$k$ answers**, all the same length, evenly spaced round a circle. Go polar, then:

$$
\begin{gathered}z^{1/k}=c^{1/k}\angle\dfrac{\theta+360^\circ\ell}{k}, \\ \ell=0,1,\dots,k-1\end{gathered}
$$

- **Length:** $c^{1/k}$ for all of them.
- **First angle:** $\theta/k$.
- **Spacing:** add $360^\circ/k$ each time.

**Short example:** the square roots of $4\angle60^\circ$:

$$
\sqrt4=2,\quad \dfrac{60^\circ}{2}=30^\circ,\quad +\dfrac{360^\circ}{2}=180^\circ\quad\Longrightarrow\quad 2\angle30^\circ,\ \ 2\angle210^\circ
$$

<details><summary>Full example (lecture 1.2): the fourth roots of $\;z=81e^{j60^\circ}$</summary>

Step 1 · Already polar: $c=81$, $\theta=60^\circ$, $k=4$.

$$
z=81\angle60^\circ
$$

Step 2 · **Length:** $81^{1/4}$.

$$
81^{1/4}=3
$$

Step 3 · **First angle.**

$$
\dfrac{60^\circ}{4}=15^\circ
$$

Step 4 · **Spacing:** keep adding $360^\circ/4$.

$$
\dfrac{360^\circ}{4}=90^\circ
$$

Step 5 · List all four.

$$
3\angle15^\circ,\quad 3\angle105^\circ,\quad 3\angle195^\circ,\quad 3\angle285^\circ
$$

</details>

<details><summary>Why $k$ answers? (optional)</summary>

$\theta$ and $\theta+360^\circ$ are the same arrow. But after you divide by $k$, they point different ways. Each extra $360^\circ$ gives a new root, until you come back round after $k$ of them.

</details>

**What do the roots look like?**

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

> **Tip:** **Casio 991 check:** complex mode does $+,-,\times,\div$ and can show $r\angle\theta$. Use it to check, but write the steps: the marks are for the working.

#### Practice: A

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

**Step 2: pick the method.** Look at the **order** first. 1st-order and 2nd-order equations use different methods.

**1st order** (the top derivative is $y^{\prime}$). Check in this order and stop at the first one that fits:

| Check | Looks like | Go to |
|---|---|---|
| 1. A $t$-part **times** a $y$-part? | $y^{\prime}=g(t)\,h(y)$ | [B1](#b1) |
| 2. Linear: $y$, $y^{\prime}$ only to the power 1? | $y^{\prime}+p(t)\,y=f(t)$ | [B2](#b2) |
| 3. Neither: write it with $dt$, $dy$. Test passes? | $M\,dt+N\,dy=0$ | [B3](#b3) |
| 4. Test fails? | $M_y\neq N_t$ | [B4](#b4) |

**One example each:**

$$
y^{\prime}=t^2y\quad\Longrightarrow\quad\text{B1}\quad(g=t^2,\ h=y)
$$

$$
y^{\prime}+y=t\quad\Longrightarrow\quad\text{B2}\quad(\text{a sum: it won’t split})
$$

$$
(t-y)\,dt-(t+y)\,dy=0\quad\Longrightarrow\quad\text{B3}\quad(M_y=-1=N_t)
$$

$$
y\,dt+(3+3t-y)\,dy=0\quad\Longrightarrow\quad\text{B4}\quad(M_y=1\neq3=N_t)
$$

> **Tip:** **No $t$ at all** (autonomous, like $y^{\prime}=3y$)? Then it always separates: B1. For 2nd order, ignore this.

**2nd order** (the top derivative is $y^{\prime\prime}$). In Weeks 1–6 these are all linear, so ask two questions: numbers in front? right side $0$?

| In front of $y$ | Right side $0$ | Right side $f(t)$ |
|---|---|---|
| **Numbers** | [B5](#b5) quadratic | [B6](#b6) $y_c+y_p$ |
| **$t$ in front** | [B7](#b7) $y=y_1v$ | not on the midterm |

**One example each:**

$$
y^{\prime\prime}+3y^{\prime}+2y=0\quad\Longrightarrow\quad\text{B5}
$$

$$
y^{\prime\prime}+3y^{\prime}+2y=4\quad\Longrightarrow\quad\text{B6}
$$

$$
y^{\prime\prime}-t\,y^{\prime}+y=0,\ \ y_1=t\quad\Longrightarrow\quad\text{B7}
$$

**The same letters everywhere.** Every B method uses these names, so there’s less to remember:

| Letter | Means | In |
|---|---|---|
| $f(t)$ | the right side: no $y$ in it | B2, B6, B7, C2 |
| $p(t)$ | multiplies the term just under the top derivative | B2, B7, C2 |
| $q(t)$ | multiplies $y$ (2nd order) | B7, C2 |
| $g(t)$, $h(y)$ | a piece with only $t$ / only $y$ | B1, B3, B4 |
| $\mu$ | the multiply-everything factor | B2, B4 |
| $C$ | the one constant (1st order) | B1–B4 |
| $c_1,\ c_2$ | the two constants (2nd order) | B5–B7, D2 |
| $A,\ B,\ D$ | unknown numbers in a guess | B6 |

And every method starts with **Write** (put it in its form) and ends with **Plug in** (use the conditions).

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
4. (d) 1st order, linear ($p=5$, $f=50$) → [B2](#b2). It has no $t$, so it’s also autonomous, and B1 works too: $\frac{di}{50-5i}=dt$.
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

### B1 · Separable: a t-part times a y-part

[Week 3 · Topic 1](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/3d1ae4a9-687d-4654-873d-be3439faea2f#c40cdedd-01db-45b4-9498-4c4929ba8f49)

**Use this when** the right side splits into a $t$-part **times** a $y$-part, and you want $y(t)$:

$$
\dfrac{dy}{dt}=2t\,y
$$

Every separable equation has this shape:

$$
\dfrac{dy}{dt}=g(t)\cdot h(y)
$$

- $g(t)$ = a piece with **only $t$** in it
- $h(y)$ = a piece with **only $y$** in it

**Short examples:**

$$
\dfrac{dy}{dt}=\dfrac{y^2}{t^3}\quad\Longrightarrow\quad g=\dfrac{1}{t^3},\quad h=y^2
$$

$$
\dfrac{dy}{dt}=3y\quad\Longrightarrow\quad g=3,\quad h=y
$$

No $t$ at all (like $3y$) is fine: $g$ is just a number.

**Not separable:** $\dfrac{dy}{dt}=t+y$. That’s a **sum**, and a sum won’t split into a product. Go to [B2](#b2).

**The move: put every $y$ with $dy$ and every $t$ with $dt$, then integrate both sides.**

$$
\dfrac{dy}{dt}=2t\,y\quad\longrightarrow\quad \dfrac{dy}{y}=2t\,dt
$$

In general:

$$
\int\dfrac{dy}{h(y)}=\int g(t)\,dt+C
$$

<details><summary>Why can you move $dy$ and $dt$ around like a fraction? (optional)</summary>

Divide by $h$:

$$
\dfrac{1}{h(y)}\,\dfrac{dy}{dt}=g(t)
$$

Now integrate both sides with respect to $t$. The chain rule says

$$
\int\dfrac{1}{h(y)}\dfrac{dy}{dt}\,dt=\int\dfrac{1}{h(y)}\,dy
$$

Moving “$dt$” across is a shortcut for exactly this.

</details>

**Steps**

1. **Write** it as $\dfrac{dy}{dt}=g(t)\,h(y)$. Factor first if you have to.
2. **Separate:** divide by $h(y)$, multiply by $dt$. You get $\dfrac{dy}{h(y)}=g(t)\,dt$.
3. **Integrate** both sides. Write **one** constant $C$, on the $t$ side.
4. **Solve for $y$** if you can. If you can’t, the answer with $y$ mixed in (like $t^2+y^2=5$) is a full answer.
5. **Plug in** the condition, like $y(0)=3$, to find $C$.

**Short example:**

$$
\dfrac{dy}{y}=2t\,dt\quad\Longrightarrow\quad \ln|y|=t^2+C\quad\Longrightarrow\quad y=Ce^{t^2}
$$

<details><summary>Full example: $\;\dfrac{dy}{dt}=2t\,y$, $\;y(0)=3$</summary>

Step 1 · **Write:** it’s $g(t)=2t$ times $h(y)=y$.

$$
\dfrac{dy}{dt}=2t\cdot y
$$

Step 2 · **Separate:** divide by $y$, multiply by $dt$.

$$
\dfrac{dy}{y}=2t\,dt
$$

Step 3 · **Integrate** each side. One constant, on the $t$ side.

$$
\ln|y|=t^2+C
$$

Step 4 · **Solve for $y$:** raise $e$ to both sides. $e^{t^2+C}=e^{C}e^{t^2}$, and $e^{C}$ is just a new constant: call it $C$ again.

$$
y=C\,e^{t^2}
$$

Step 5 · **Plug in** $y(0)=3$: $e^{0}=1$.

$$
3=C
$$

**Answer:**

$$
y=3e^{t^2}
$$

</details>

<details><summary>Full example (lecture 3.3): $\;\dfrac{dy}{dt}=\dfrac{3t+ty^2}{y+t^2y}$, $\;y(1)=3$</summary>

Step 1 · **Write:** pull $t$ out of the top and $y$ out of the bottom. Now it’s a $t$-part times a $y$-part.

$$
\dfrac{dy}{dt}=\dfrac{t}{1+t^2}\cdot\dfrac{3+y^2}{y}
$$

Step 2 · **Separate:** everything with $y$ goes with $dy$, everything with $t$ goes with $dt$.

$$
\dfrac{y}{3+y^2}\,dy=\dfrac{t}{1+t^2}\,dt
$$

Step 3 · **Integrate:** on each side the top is half the derivative of the bottom (integral card “top = derivative of bottom”).

$$
\tfrac12\ln(3+y^2)=\tfrac12\ln(1+t^2)+C
$$

Step 4 · **Solve for $y$:** multiply by $2$, raise $e$ to both sides. $e^{2C}$ is a new constant: call it $C$.

$$
3+y^2=C\,(1+t^2)
$$

Step 5 · **Plug in** $y(1)=3$.

$$
3+9=C\cdot2
$$

$$
C=6
$$

Step 6 · Put $C=6$ back and take the $+$ root, because $y(1)=3$ is positive.

$$
y^2=6t^2+3
$$

**Answer:**

$$
y=\sqrt{6t^2+3}
$$

</details>

**Integrals that show up.** Open a card for an example:

<details><summary>Power rule: $\;\displaystyle\int t^n\,dt=\dfrac{t^{n+1}}{n+1}$ (any $n\neq-1$)</summary>

Step 1 · Add one to the power, divide by the new power. Works for negative powers too.

$$
\int t^{-3}\,dt=\dfrac{t^{-2}}{-2}=-\dfrac{1}{2t^2}
$$

</details>

<details><summary>One over: $\;\displaystyle\int\dfrac{1}{y}\,dy=\ln|y|$</summary>

Step 1 · This is the $n=-1$ case the power rule skips.

$$
\int\dfrac{dy}{y}=\ln|y|
$$

Step 2 · Undo the $\ln$ with $e$: $e^{\ln A}=A$. A constant $e^{C}$ is just a new constant.

$$
\ln|y|=t^2+C\quad\Longrightarrow\quad y=Ce^{t^2}
$$

</details>

<details><summary>Top = derivative of bottom: $\;\displaystyle\int\dfrac{f^{\prime}(t)}{f(t)}\,dt=\ln|f(t)|$</summary>

Step 1 · The derivative of $t^2+1$ is $2t$. The top is only $t$, so you get half.

$$
\int\dfrac{t}{t^2+1}\,dt=\tfrac12\ln(t^2+1)
$$

</details>

<details><summary>Exponential: $\;\displaystyle\int e^{at}\,dt=\dfrac1a\,e^{at}$</summary>

Step 1 · Divide by the number in front of $t$.

$$
\int e^{2t}\,dt=\tfrac12e^{2t}
$$

</details>

<details><summary>Combine logs: $\;k\ln A+\ln B=\ln(A^kB)$</summary>

Step 1 · Pull the number up as a power, then multiply inside one $\ln$.

$$
3\ln A+\ln B=\ln(A^3B)
$$

</details>

> **Warning:** **Dividing by $h(y)$ can lose a solution.** If $h$ is $0$ at some number, that flat line is a solution too. Example: in $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$, $h=y^2$ is $0$ at $y=0$, and $y=0$ works ($0=0$). List it next to your answer.

> **Warning:** **Only one $C$.** Put it on the $t$ side right when you integrate. Two constants ($C_1$ left, $C_2$ right) are really one.

#### Practice: B1

**Problem: Problem 8 · W3 · Separate and use a starting value · Pre-tutorial 3(a)** (introductory)

Solve $\dfrac{dy}{dt}=-\dfrac{t}{y}$, $\;y=2$ when $t=1$.

<details><summary>Solution</summary>

1. **Type:** $-\dfrac{t}{y}=(-t)\cdot\dfrac1y$, a $t$-part times a $y$-part → B1.
2. **Separate:** multiply both sides by $y\,dt$.

   $$y\,dy=-t\,dt$$
3. **Integrate** each side.

   $$\dfrac{y^2}{2}=-\dfrac{t^2}{2}+C$$
4. **Plug in** $t=1$, $y=2$.

   $$2=-\tfrac12+C\quad\Rightarrow\quad C=\tfrac52$$
5. Put $C$ back and multiply by $2$.

   $$t^2+y^2=5$$
6. **Solve for $y$.** Keep the $+$ root, since $y(1)=2$ is positive.

   $$y=\sqrt{5-t^2}$$

**Answer:** $y=\sqrt{5-t^2}$. It’s the top half of the circle $t^2+y^2=5$, so it only exists for $-\sqrt5<t<\sqrt5$.

</details>

**Problem: Problem 9 · W3 · A general solution with a power · lecture Example 3.2** (introductory)

Find the general solution of $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$.

<details><summary>Solution</summary>

1. **Type:** $\dfrac{y^2}{t^3}=\dfrac{1}{t^3}\cdot y^2$ → B1, with $g=t^{-3}$, $h=y^2$.
2. **Separate:** divide by $y^2$, multiply by $dt$.

   $$y^{-2}\,dy=t^{-3}\,dt$$
3. **Integrate** with the power rule ($n=-2$ on the left, $n=-3$ on the right).

   $$-y^{-1}=-\tfrac12t^{-2}+C$$
4. **Solve for $y$:** multiply by $-1$ (call $-C$ just $C$ again).

   $$\dfrac1y=\dfrac{1}{2t^2}+C=\dfrac{1+2Ct^2}{2t^2}$$
5. Flip both sides.

   $$y=\dfrac{2t^2}{1+2Ct^2}$$

**Answer:** $y=\dfrac{2t^2}{1+2Ct^2}$, plus $y=0$. We divided by $y^2$, which skips $y=0$ (see the warning).

</details>

**Problem: Problem 10 · W3 · An exponential of y** (intermediate)

Solve $\dfrac{dy}{dt}=2t\,e^{-y}$, $\;y(0)=0$.

<details><summary>Solution</summary>

1. **Type:** $2t\cdot e^{-y}$ is a $t$-part times a $y$-part → B1.
2. **Separate:** dividing by $e^{-y}$ is the same as multiplying by $e^{y}$.

   $$e^{y}\,dy=2t\,dt$$
3. **Integrate** each side.

   $$e^{y}=t^2+C$$
4. **Solve for $y$:** take $\ln$ of both sides.

   $$y=\ln(t^2+C)$$
5. **Plug in** $y(0)=0$: $\ln C=0$.

   $$C=1$$

**Answer:** $y=\ln(t^2+1)$.

</details>

**Problem: Problem 11 · W3 · Differential form · Pre-tutorial 3(b)** (intermediate)

Solve $3t(y^2+1)\,dt+y(t^2+2)\,dy=0$.

<details><summary>Solution</summary>

1. **Type:** each term is a $t$-part times a $y$-part → B1.
2. **Separate:** divide every term by $(y^2+1)(t^2+2)$. Now only $t$ sits with $dt$, only $y$ with $dy$.

   $$\dfrac{3t}{t^2+2}\,dt+\dfrac{y}{y^2+1}\,dy=0$$
3. **Integrate:** both are “top = derivative of bottom”, times $\frac32$ and $\frac12$.

   $$\tfrac32\ln(t^2+2)+\tfrac12\ln(y^2+1)=C$$
4. Multiply by $2$, then combine the logs (card above).

   $$\ln\!\big[(t^2+2)^3(y^2+1)\big]=2C$$
5. Raise $e$ to both sides. $e^{2C}$ is a new constant: call it $C$.

   $$(t^2+2)^3(y^2+1)=C$$

**Answer:** $(t^2+2)^3(y^2+1)=C$, with $C>0$. You can’t easily get $y$ alone, so this is a full answer.

</details>

**Problem: Problem 12 · W3 · Collect before separating · lecture Example 3.4** (advanced)

Solve $y\,dt+(t^3y^2+t^3)\,dy=0$.

<details><summary>Solution</summary>

1. **Type:** the $dy$ term has a common factor, $t^3y^2+t^3=t^3(y^2+1)$. Now each term is a $t$-part times a $y$-part → B1.
2. **Separate:** divide every term by $t^3y$.

   $$t^{-3}\,dt+\dfrac{y^2+1}{y}\,dy=0$$
3. Split the fraction so each part is easy: $\dfrac{y^2+1}{y}=y+\dfrac1y$.

   $$\int t^{-3}\,dt+\int\left(y+\dfrac1y\right)dy=C$$
4. **Integrate** each part.

   $$-\dfrac{1}{2t^2}+\dfrac{y^2}{2}+\ln|y|=C$$
5. Multiply by $2$ to clear the fractions ($2C$ is a new $C$).

   $$y^2+2\ln|y|-t^{-2}=C$$

**Answer:** $y^2+2\ln|y|-t^{-2}=C$, plus $y=0$, which we skipped by dividing by $y$.

</details>

### B2 · Linear first order: the integrating factor

[Week 3 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/3d1ae4a9-687d-4654-873d-be3439faea2f#a43fc96e-8dc5-4a1e-bfdf-bf1acf01f98b)

**Use this when** it won’t separate, but $y$ and $y^{\prime}$ only appear to the power 1:

$$
y^{\prime}+2y=4
$$

Every linear first-order equation can be written like this:

$$
y^{\prime}+p(t)\,y=f(t)
$$

- $p(t)$ = what multiplies $y$, **sign included**, once $y^{\prime}$ stands alone
- $f(t)$ = the right side: everything with no $y$ in it

**Short examples:**

$$
y^{\prime}=t-y\quad\Longrightarrow\quad y^{\prime}+y=t\quad\Longrightarrow\quad p=1,\quad f=t
$$

$$
ty^{\prime}+2y=t^2\quad\Longrightarrow\quad y^{\prime}+\tfrac2t\,y=t\quad\Longrightarrow\quad p=\tfrac2t,\quad f=t
$$

In the second one you **divide by $t$ first**, so $y^{\prime}$ stands alone.

**The move: multiply everything by $\mu$.** Then the left side becomes one derivative, and you just integrate.

$$
\mu=e^{\int p\,dt}
$$

After multiplying, the equation always turns into:

$$
(\mu\,y)^{\prime}=\mu\,f
$$

<details><summary>Why does multiplying by $\mu$ work? (optional)</summary>

The product rule says

$$
(\mu y)^{\prime}=\mu\,y^{\prime}+\mu^{\prime}\,y
$$

With $\mu=e^{\int p\,dt}$, the chain rule gives $\mu^{\prime}=p\,\mu$. So

$$
(\mu y)^{\prime}=\mu\,y^{\prime}+p\,\mu\,y=\mu\,(y^{\prime}+p\,y)
$$

That’s $\mu$ times the left side of your equation. So multiplying by $\mu$ turns $y^{\prime}+py$ into one derivative.

</details>

**Steps**

1. **Write** it as $y^{\prime}+p(t)\,y=f(t)$. Divide first if something multiplies $y^{\prime}$. Read $p$ and $f$.
2. **Find $\mu$** $=e^{\int p\,dt}$. No $+C$ here: any one $\mu$ works.
3. **Multiply** everything by $\mu$. The left side becomes $(\mu y)^{\prime}$, so you get $(\mu y)^{\prime}=\mu f$.
4. **Integrate** both sides: $\mu y=\int\mu f\,dt+C$. **This** is where the $+C$ goes.
5. **Divide** by $\mu$ to get $y$.
6. **Plug in** the condition to find $C$.

**Short example:**

$$
y^{\prime}+2y=4\quad\Longrightarrow\quad \mu=e^{2t}\quad\Longrightarrow\quad (e^{2t}y)^{\prime}=4e^{2t}
$$

<details><summary>Full example: $\;y^{\prime}+2y=4$, $\;y(0)=0$</summary>

Step 1 · **Write:** $y^{\prime}$ is already alone.

$$
p=2,\qquad f=4
$$

Step 2 · **Find $\mu$.**

$$
\mu=e^{\int2\,dt}=e^{2t}
$$

Step 3 · **Multiply** every term by $e^{2t}$. The left side is now one derivative (the product rule backwards).

$$
e^{2t}y^{\prime}+2e^{2t}y=4e^{2t}
$$

$$
(e^{2t}y)^{\prime}=4e^{2t}
$$

Step 4 · **Integrate** both sides: $\int4e^{2t}\,dt=2e^{2t}$.

$$
e^{2t}y=2e^{2t}+C
$$

Step 5 · **Divide** by $e^{2t}$.

$$
y=2+Ce^{-2t}
$$

Step 6 · **Plug in** $y(0)=0$.

$$
0=2+C\quad\Rightarrow\quad C=-2
$$

**Answer:**

$$
y=2-2e^{-2t}
$$

</details>

<details><summary>Full example (lecture 3.1): $\;y^{\prime}+\dfrac{10\,y}{2t+5}=10$, $\;y(0)=0$</summary>

Step 1 · **Write:** $y^{\prime}$ is already alone.

$$
p=\dfrac{10}{2t+5},\qquad f=10
$$

Step 2 · **Find $\mu$:** $\int\frac{10}{2t+5}dt=5\ln(2t+5)$, and $e^{5\ln(2t+5)}=(2t+5)^5$ (card “$e$ and $\ln$ cancel”).

$$
\mu=(2t+5)^5
$$

Step 3 · **Multiply:** the left side becomes $(\mu y)^{\prime}$.

$$
\big[(2t+5)^5y\big]^{\prime}=10(2t+5)^5
$$

Step 4 · **Integrate** with $u=2t+5$, $du=2\,dt$: $\;10\int u^5\,\frac{du}{2}=\frac56u^6$.

$$
(2t+5)^5y=\tfrac56(2t+5)^6+C
$$

Step 5 · **Divide** by $(2t+5)^5$.

$$
y=\tfrac56(2t+5)+\dfrac{C}{(2t+5)^5}
$$

Step 6 · **Plug in** $y(0)=0$.

$$
0=\tfrac56\cdot5+\dfrac{C}{5^5}
$$

$$
C=-\dfrac{5^7}{6}
$$

**Answer:**

$$
y=\tfrac56(2t+5)-\dfrac{5^7}{6(2t+5)^5}
$$

</details>

**Calculus that shows up.** Open a card for an example:

<details><summary>$e$ and $\ln$ cancel: $\;e^{\int\frac{k}{t}dt}=e^{k\ln t}=t^k$</summary>

Step 1 · $p=\frac2t$:

$$
\mu=e^{2\ln t}=t^2
$$

Step 2 · $p=-\frac1t$:

$$
\mu=e^{-\ln t}=\dfrac1t
$$

</details>

<details><summary>Constant $p$: $\;e^{\int k\,dt}=e^{kt}$</summary>

Step 1 · $p=5$:

$$
\mu=e^{5t}
$$

</details>

<details><summary>By parts: $\;\displaystyle\int t\,e^{t}\,dt=(t-1)\,e^{t}$</summary>

Step 1 · Check it by differentiating with the product rule:

$$
\big[(t-1)e^{t}\big]^{\prime}=e^{t}+(t-1)e^{t}=t\,e^{t}
$$

</details>

<details><summary>Substitution: $\;\displaystyle\int t\,e^{t^2}dt=\tfrac12e^{t^2}$</summary>

Step 1 · Let $u=t^2$, so $du=2t\,dt$ and $t\,dt=\frac12du$.

$$
\int t\,e^{t^2}dt=\tfrac12\int e^{u}\,du=\tfrac12e^{t^2}
$$

</details>

> **Tip:** **Shortcut when $p=k$ and $f=F$ are both plain numbers:** $\;y=\dfrac{F}{k}+Ce^{-kt}$. Example: $y^{\prime}+2y=4$ gives $y=2+Ce^{-2t}$. Every RC and RL circuit has this shape ([D1](#d1)).

> **Warning:** **Get $y^{\prime}$ alone first.** In $ty^{\prime}+2y=t^2$, divide by $t$ first. Then $p=\frac2t$, not $2$.

> **Warning:** **Multiply the right side by $\mu$ too.** It’s $\int\mu f\,dt$, not $\int f\,dt$.

<details><summary>Both separable and linear? (optional)</summary>

Some equations are both. Then either method works, and separating is usually faster.

- $f=0$: $\;y^{\prime}=(8t+3)y$ separates as $\dfrac{dy}{y}=(8t+3)\,dt$.
- $p$ and $f$ both numbers: $\;y^{\prime}+2y=4$ separates as $\dfrac{dy}{4-2y}=dt$.

</details>

#### Practice: B2

**Problem: Problem 13 · W3 · The lecture’s RL equation · lecture §1.1** (introductory)

Solve $\dfrac{di}{dt}+5i=50$, $\;i(0)=0$ (the series RL circuit of the Week 3 lecture, $i$ in amperes).

<details><summary>Solution</summary>

1. **Type:** linear → B2. Here the unknown is $i$ instead of $y$.
2. **Write:** $i^{\prime}$ is already alone.

   $$p=5,\qquad f=50$$
3. **Find $\mu$.**

   $$\mu=e^{5t}$$
4. **Multiply:** the left side becomes one derivative.

   $$(e^{5t}i)^{\prime}=50e^{5t}$$
5. **Integrate:** $\int50e^{5t}\,dt=10e^{5t}$.

   $$e^{5t}i=10e^{5t}+C$$
6. **Divide** by $e^{5t}$.

   $$i=10+Ce^{-5t}$$
7. **Plug in** $i(0)=0$.

   $$0=10+C\quad\Rightarrow\quad C=-10$$

**Answer:** $i(t)=10(1-e^{-5t})\,\mathrm{A}$. It climbs from 0 to 10 A. The shortcut gives the 10 straight away: $F/k=50/5$.

</details>

**Problem: Problem 14 · W3 · Linear and separable: solve it both ways · Pre-tutorial 3(c)** (introductory)

Find the general solution of $\dfrac{dy}{dt}=8ty+3y$ with an integrating factor, then check it by separating.

<details><summary>Solution</summary>

1. **Type:** linear → B2.
2. **Write:** move the $y$ terms left.

   $$\begin{gathered}y^{\prime}-(8t+3)\,y=0 \\ p=-(8t+3),\qquad f=0\end{gathered}$$
3. **Find $\mu$:** $\int-(8t+3)\,dt=-4t^2-3t$.

   $$\mu=e^{-4t^2-3t}$$
4. **Multiply:** $f=0$, so the right side is $0$.

   $$(\mu y)^{\prime}=0$$
5. **Integrate:** the integral of $0$ is just $C$.

   $$e^{-4t^2-3t}\,y=C$$
6. **Divide** by $\mu$.

   $$y=Ce^{4t^2+3t}$$
7. **Check by separating** (B1): $\dfrac{dy}{y}=(8t+3)\,dt$ gives $\ln|y|=4t^2+3t+C$, so $y=Ce^{4t^2+3t}$. Same answer.

**Answer:** $y=Ce^{4t^2+3t}$.

</details>

**Problem: Problem 15 · W3 · An integral that needs parts** (intermediate)

Solve $y^{\prime}+y=t$, $\;y(0)=0$.

<details><summary>Solution</summary>

1. **Type:** linear → B2. It won’t separate: $y^{\prime}=t-y$ is a sum.
2. **Write:** $y^{\prime}$ is already alone.

   $$p=1,\qquad f=t$$
3. **Find $\mu$.**

   $$\mu=e^{t}$$
4. **Multiply.**

   $$(e^{t}y)^{\prime}=t\,e^{t}$$
5. **Integrate** with the by-parts card: $\int te^t\,dt=(t-1)e^t$.

   $$e^{t}y=(t-1)e^{t}+C$$
6. **Divide** by $e^t$.

   $$y=t-1+Ce^{-t}$$
7. **Plug in** $y(0)=0$.

   $$0=-1+C\quad\Rightarrow\quad C=1$$

**Answer:** $y=t-1+e^{-t}$.

</details>

**Problem: Problem 16 · W3 · Divide first, then a power of t** (intermediate)

Solve $t\,y^{\prime}+2y=t^2$, $\;y(1)=0$, for $t>0$.

<details><summary>Solution</summary>

1. **Type:** linear → B2.
2. **Write:** divide by $t$ so $y^{\prime}$ stands alone.

   $$\begin{gathered}y^{\prime}+\dfrac{2}{t}\,y=t \\ p=\dfrac2t,\qquad f=t\end{gathered}$$
3. **Find $\mu$:** $e$ and $\ln$ cancel.

   $$\mu=e^{\int\frac2t dt}=e^{2\ln t}=t^2$$
4. **Multiply:** $\mu f=t^2\cdot t$.

   $$(t^2y)^{\prime}=t^3$$
5. **Integrate.**

   $$t^2y=\dfrac{t^4}{4}+C$$
6. **Divide** by $t^2$.

   $$y=\dfrac{t^2}{4}+\dfrac{C}{t^2}$$
7. **Plug in** $y(1)=0$.

   $$0=\tfrac14+C\quad\Rightarrow\quad C=-\tfrac14$$

**Answer:** $y=\dfrac{t^2}{4}-\dfrac{1}{4t^2}$.

</details>

**Problem: Problem 17 · W3 · An integrating factor with t²** (advanced)

Solve $y^{\prime}+2t\,y=t$, $\;y(0)=1$.

<details><summary>Solution</summary>

1. **Type:** linear → B2.
2. **Write:** $y^{\prime}$ is already alone.

   $$p=2t,\qquad f=t$$
3. **Find $\mu$:** $\int2t\,dt=t^2$.

   $$\mu=e^{t^2}$$
4. **Multiply.**

   $$(e^{t^2}y)^{\prime}=t\,e^{t^2}$$
5. **Integrate** with the substitution card: $\int te^{t^2}dt=\frac12e^{t^2}$.

   $$e^{t^2}y=\tfrac12e^{t^2}+C$$
6. **Divide** by $e^{t^2}$.

   $$y=\tfrac12+Ce^{-t^2}$$
7. **Plug in** $y(0)=1$.

   $$1=\tfrac12+C\quad\Rightarrow\quad C=\tfrac12$$

**Answer:** $y=\dfrac12\big(1+e^{-t^2}\big)$. It also separates, $y^{\prime}=t(1-2y)$, so you could check it with [B1](#b1).

</details>

### B3 · Exact equations

[Week 4 · Topic 1](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/ce2fa611-8b68-46a9-b6ca-653ae9c59aee#c9f71086-78d7-4bc3-a405-e0c6375fb6ca) [Week 4 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/ce2fa611-8b68-46a9-b6ca-653ae9c59aee#954310f2-d355-42ff-bd75-4e6b1d00f02d)

**Use this when** it’s neither separable nor linear, and it’s written with $dt$ and $dy$:

$$
(2ty+3t^2)\,dt+t^2\,dy=0
$$

Every exact equation is written like this, with everything on the left:

$$
M\,dt+N\,dy=0
$$

- $M$ = everything multiplying $dt$, **sign included**
- $N$ = everything multiplying $dy$, **sign included**

**Short examples:**

$$
(2ty+3t^2)\,dt+t^2\,dy=0\quad\Longrightarrow\quad M=2ty+3t^2,\quad N=t^2
$$

Given $y^{\prime}$ as a fraction? Cross-multiply, then move everything left:

$$
y^{\prime}=\dfrac{t-y}{t+y}\quad\Longrightarrow\quad (t-y)\,dt-(t+y)\,dy=0
$$

$$
M=t-y,\qquad N=-(t+y)
$$

**The move: find one function $U(t,y)$** whose $t$-derivative is $M$ and whose $y$-derivative is $N$. The answer is:

$$
U(t,y)=C
$$

But first check it’s exact, with the **cross test**:

$$
M_y=N_t
$$

- $M_y$ = differentiate $M$ in $y$, treating $t$ like a number
- $N_t$ = differentiate $N$ in $t$, treating $y$ like a number
- Not equal? Not exact: go to [B4](#b4).

<details><summary>Why the cross test, and why $U=C$? (optional)</summary>

If $U$ exists, then $M=U_t$ and $N=U_y$. So $M_y$ is $U$ differentiated in $t$, then $y$. And $N_t$ is $U$ differentiated in $y$, then $t$. The order doesn’t change the result, so the two must match.

$M\,dt+N\,dy$ is the small change in $U$. The equation sets that change to $0$, so $U$ stays at one constant value: $U=C$. Each solution is a contour line of the surface $z=U(t,y)$, like on a map.

</details>

**Steps**

1. **Write** it as $M\,dt+N\,dy=0$, everything on the left. Read $M$ and $N$ with their signs.
2. **Test:** is $M_y=N_t$? If not, go to [B4](#b4).
3. **Integrate $M$ in $t$**, treating $y$ like a number. Instead of $+C$, add $h(y)$: a piece with only $y$.
4. **Match $N$:** differentiate $U$ in $y$ and set it equal to $N$. Everything cancels except $h^{\prime}(y)$. Integrate it.
5. **Answer:** $U(t,y)=C$.
6. **Plug in** the condition to find $C$.

$$U=\int M\,dt+h(y)$$

Why $h(y)$ and not $C$: anything with only $y$ in it disappears when you differentiate in $t$. So it could be hiding there.

**Short example:**

$$
M=2ty+3t^2\quad\Longrightarrow\quad U=t^2y+t^3+h(y)
$$

<details><summary>Full example (lecture 4.1): $\;(2ty+3t^2)\,dt+t^2\,dy=0$</summary>

Step 1 · **Write:** already in form.

$$
M=2ty+3t^2,\qquad N=t^2
$$

Step 2 · **Test:** for $M_y$ treat $t$ as a number. For $N_t$ treat $y$ as a number.

$$
M_y=2t,\qquad N_t=2t\quad\checkmark
$$

Step 3 · **Integrate $M$ in $t$** ($y$ is a number). Add $h(y)$.

$$
U=t^2y+t^3+h(y)
$$

Step 4 · **Match $N$:** differentiate $U$ in $y$, set it equal to $N=t^2$.

$$
U_y=t^2+h^{\prime}(y)=t^2
$$

$$
h^{\prime}(y)=0\quad\Rightarrow\quad h=\text{a number}
$$

Step 5 · **Answer:** the number in $h$ merges into $C$.

$$
t^2y+t^3=C
$$

**Answer:**

$$
t^2y+t^3=C\qquad\Big(y=\dfrac{C-t^3}{t^2}\Big)
$$

</details>

<details><summary>Full example (lecture (b)): $\;y^{\prime}=\dfrac{t-y}{t+y}$, $\;y(0)=1$</summary>

Step 1 · **Write:** cross-multiply, $(t+y)\,dy=(t-y)\,dt$, then move everything left. Moving $dy$ across flips its sign.

$$
(t-y)\,dt-(t+y)\,dy=0
$$

$$
M=t-y,\qquad N=-t-y
$$

Step 2 · **Test.**

$$
M_y=-1,\qquad N_t=-1\quad\checkmark
$$

Step 3 · **Integrate $M$ in $t$.**

$$
U=\tfrac12t^2-ty+h(y)
$$

Step 4 · **Match $N$.**

$$
U_y=-t+h^{\prime}(y)=-t-y
$$

$$
h^{\prime}=-y\quad\Rightarrow\quad h=-\tfrac12y^2
$$

Step 5 · **Answer:** set $U=C$, then multiply by $2$ ($2C$ is a new $C$).

$$
t^2-2ty-y^2=C
$$

Step 6 · **Plug in** $t=0$, $y=1$.

$$
0-0-1=C\quad\Rightarrow\quad C=-1
$$

**Answer:**

$$
t^2-2ty-y^2=-1
$$

</details>

**Partial derivatives.** Differentiate in one letter, treat the other like a plain number. Open a card:

<details><summary>In $t$: $\;\dfrac{\partial}{\partial t}(t^2y)=2ty$</summary>

Step 1 · $y$ acts like a number, like $5$: the derivative of $5t^2$ is $10t$.

$$
\dfrac{\partial}{\partial t}(t^2y)=2t\cdot y
$$

</details>

<details><summary>In $y$: $\;\dfrac{\partial}{\partial y}(t^2y)=t^2$</summary>

Step 1 · $t^2$ acts like a number: the derivative of $5y$ is $5$.

$$
\dfrac{\partial}{\partial y}(t^2y)=t^2
$$

Step 2 · A term with no $y$ at all gives $0$.

$$
\dfrac{\partial}{\partial y}(t-y)=0-1=-1
$$

</details>

<details><summary>Integrate in $t$: $\;\displaystyle\int(2ty+3t^2)\,dt=t^2y+t^3+h(y)$</summary>

Step 1 · $y$ acts like a number. The “constant” is $h(y)$.

$$
\int 2ty\,dt=y\,t^2,\qquad \int3t^2\,dt=t^3
$$

</details>

> **Warning:** **Moving the $dy$ term across the $=$ flips its sign.** In $y^{\prime}=\frac{t-y}{t+y}$, $N$ is $-(t+y)$, not $t+y$. One wrong sign and the test fails.

#### Practice: B3

**Problem: Problem 18 · W4 · Test, then solve · lecture exercise (a)** (introductory)

Test $3t\,dt+4y\,dy=0$ for exactness, and if so, solve.

<details><summary>Solution</summary>

1. **Type:** $M\,dt+N\,dy=0$ → test for B3.
2. **Write:** already in form.

   $$M=3t,\qquad N=4y$$
3. **Test:** $M$ has no $y$ and $N$ has no $t$, so both are $0$.

   $$M_y=0,\qquad N_t=0\quad\checkmark$$
4. **Integrate $M$ in $t$.**

   $$U=\tfrac32t^2+h(y)$$
5. **Match $N$:** $U_y=h^{\prime}(y)$ must equal $4y$.

   $$h^{\prime}=4y\quad\Rightarrow\quad h=2y^2$$
6. **Answer:** $U=C$. Multiply by $2$ ($2C$ is a new $C$).

   $$3t^2+4y^2=C$$

**Answer:** Exact. $3t^2+4y^2=C$: ellipses. (It’s also separable: $4y\,dy=-3t\,dt$.)

</details>

**Problem: Problem 19 · W4 · Test before you integrate · lecture exercise (d)** (introductory)

Is $y^{\prime}=\dfrac{t}{t+y}$ exact?

<details><summary>Solution</summary>

1. **Type:** a slope fraction → write it with $dt$, $dy$ and test.
2. **Write:** cross-multiply, $(t+y)\,dy=t\,dt$, then move everything left.

   $$\begin{gathered}t\,dt-(t+y)\,dy=0 \\ M=t,\qquad N=-(t+y)\end{gathered}$$
3. **Test:** $M$ has no $y$.

   $$M_y=0,\qquad N_t=-1$$
4. $0\neq-1$, so it’s **not exact**. You’d try [B4](#b4) next, but neither ratio has just one letter. The lecture stops at “not exact”.

   $$\begin{gathered}\dfrac{M_y-N_t}{N}=-\dfrac{1}{t+y}, \\ \dfrac{N_t-M_y}{M}=-\dfrac1t\end{gathered}$$

**Answer:** Not exact: $M_y=0\neq-1=N_t$.

</details>

**Problem: Problem 20 · W4 · The sign trap · lecture exercise (c)** (intermediate)

Solve $2ty\,y^{\prime}=t^2-y^2$.

<details><summary>Solution</summary>

1. **Type:** not separable, not linear ($y^2$) → write with $dt$, $dy$ and test for B3.
2. **Write:** $2ty\,dy=(t^2-y^2)\,dt$. Moving $2ty\,dy$ left makes it **negative**.

   $$\begin{gathered}(t^2-y^2)\,dt-2ty\,dy=0 \\ M=t^2-y^2,\qquad N=-2ty\end{gathered}$$
3. **Test.**

   $$M_y=-2y,\qquad N_t=-2y\quad\checkmark$$
4. **Integrate $M$ in $t$.**

   $$U=\tfrac13t^3-ty^2+h(y)$$
5. **Match $N$:** $U_y=-2ty+h^{\prime}$ must equal $-2ty$.

   $$h^{\prime}=0$$
6. **Answer:** $U=C$. Multiply by $3$ ($3C$ is a new $C$).

   $$t^3-3ty^2=C$$

**Answer:** $t^3-3ty^2=C$. Keep $+2ty\,dy$ (wrong sign) and the test gives $-2y\neq2y$.

</details>

### B4 · Not exact: make it exact with μ

[Week 4 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/ce2fa611-8b68-46a9-b6ca-653ae9c59aee#ebb7e8ad-4fda-4034-97dc-a9c048d71335)

**Use this when** it’s written with $dt$ and $dy$, but the [B3](#b3) test **fails**:

$$
y\,dt+(3+3t-y)\,dy=0\qquad M_y=1\neq3=N_t
$$

**The move: multiply everything by a factor $\mu$** that makes it pass the test. Then finish it like [B3](#b3).

Same idea as $\mu$ in [B2](#b2): multiply by the right thing and the equation becomes easy.

To find $\mu$, start from the mismatch $M_y-N_t$ and try two ratios. One of them should have **only one letter** left.

#### Case 1: only t left

Divide the mismatch by $N$. If only $t$ is left, call it $g(t)$:

$$
\dfrac{M_y-N_t}{N}=g(t)\quad\Longrightarrow\quad \mu=e^{\int g\,dt}
$$

**Short example:** $(t^2+y)\,dt-t\,dy=0$:

$$
\dfrac{1-(-1)}{-t}=-\dfrac2t\quad\Longrightarrow\quad \mu=e^{-2\ln t}=\dfrac{1}{t^2}
$$

#### Case 2: only y left

Flip the subtraction and divide by $M$. If only $y$ is left, call it $h(y)$:

$$
\dfrac{N_t-M_y}{M}=h(y)\quad\Longrightarrow\quad \mu=e^{\int h\,dy}
$$

**Short example:** $y\,dt+(3+3t-y)\,dy=0$:

$$
\dfrac{3-1}{y}=\dfrac2y\quad\Longrightarrow\quad \mu=e^{2\ln y}=y^2
$$

(The lecture calls these Theorem 1 and Theorem 2.)

<details><summary>Where does Case 1 come from? (optional)</summary>

Multiply by $\mu(t)$ and ask the new equation to pass the test, $(\mu M)_y=(\mu N)_t$. On the left, $\mu$ has no $y$, so it just comes out. On the right, use the product rule:

$$
\mu\,M_y=\mu^{\prime} N+\mu\,N_t\quad\Longrightarrow\quad \dfrac{\mu^{\prime}}{\mu}=\dfrac{M_y-N_t}{N}
$$

The left side only has $t$, so the right side must too. Then $\ln\mu=\int g\,dt$. Case 2 is the same with $\mu(y)$.

</details>

#### Steps and examples

1. **Write** it as $M\,dt+N\,dy=0$. Read $M$ and $N$ with their signs.
2. **Test:** $M_y\neq N_t$. (Equal? It’s already exact: [B3](#b3).)
3. **Find $\mu$:** try Case 1, then Case 2. Keep the ratio with only one letter. No $+C$ in this integral.
4. **Multiply** the whole equation by $\mu$: both $M$ and $N$.
5. **Re-test:** it must pass now. If not, recheck your algebra.
6. **Finish like B3:** integrate $M$ in $t$, match $N$, answer $U=C$, plug in.

<details><summary>Full example (Pre-tutorial 4): $\;y\,dt+(3+3t-y)\,dy=0$</summary>

Step 1 · **Write.**

$$
M=y,\qquad N=3+3t-y
$$

Step 2 · **Test:** they don’t match.

$$
M_y=1,\qquad N_t=3
$$

Step 3 · **Find $\mu$:** Case 1 gives $\frac{1-3}{3+3t-y}$, both letters. Case 2 leaves only $y$.

$$
\dfrac{N_t-M_y}{M}=\dfrac{3-1}{y}=\dfrac2y
$$

Step 4 · $e$ and $\ln$ cancel: $e^{2\ln y}=y^2$.

$$
\mu=e^{\int\frac2y\,dy}=y^2
$$

Step 5 · **Multiply** the whole equation by $y^2$.

$$
y^3\,dt+(3y^2+3ty^2-y^3)\,dy=0
$$

Step 6 · **Re-test:** now $M=y^3$ and $N=3y^2+3ty^2-y^3$.

$$
M_y=3y^2,\qquad N_t=3y^2\quad\checkmark
$$

Step 7 · **Integrate $M$ in $t$** ($y$ is a number).

$$
U=ty^3+h(y)
$$

Step 8 · **Match $N$.**

$$
U_y=3ty^2+h^{\prime}(y)=3y^2+3ty^2-y^3
$$

$$
h^{\prime}=3y^2-y^3\quad\Rightarrow\quad h=y^3-\tfrac14y^4
$$

Step 9 · **Answer:** $U=C$.

$$
ty^3+y^3-\tfrac14y^4=C
$$

**Answer:**

$$
ty^3+y^3-\dfrac{y^4}{4}=C
$$

</details>

<details><summary>Full example (Case 1): $\;(t^2+y)\,dt-t\,dy=0$, $\;t>0$</summary>

Step 1 · **Write.**

$$
M=t^2+y,\qquad N=-t
$$

Step 2 · **Test.**

$$
M_y=1,\qquad N_t=-1
$$

Step 3 · **Find $\mu$:** Case 1 leaves only $t$.

$$
\dfrac{M_y-N_t}{N}=\dfrac{1-(-1)}{-t}=-\dfrac2t
$$

$$
\mu=e^{-2\ln t}=\dfrac{1}{t^2}
$$

Step 4 · **Multiply** by $\frac{1}{t^2}$.

$$
\Big(1+\dfrac{y}{t^2}\Big)dt-\dfrac1t\,dy=0
$$

Step 5 · **Re-test.**

$$
M_y=\dfrac{1}{t^2},\qquad N_t=\dfrac{1}{t^2}\quad\checkmark
$$

Step 6 · **Integrate $M$ in $t$:** $\int1\,dt=t$ and $\int\frac{y}{t^2}dt=-\frac yt$.

$$
U=t-\dfrac{y}{t}+h(y)
$$

Step 7 · **Match $N$:** $U_y=-\frac1t+h^{\prime}$ must equal $-\frac1t$.

$$
h^{\prime}=0
$$

Step 8 · **Answer.**

$$
t-\dfrac yt=C
$$

**Answer:**

$$
t-\dfrac yt=C\qquad(y=t^2-Ct)
$$

</details>

<details><summary>$e$ and $\ln$ cancel: $\;e^{\int\frac{k}{y}dy}=y^k$, $\;e^{\int\frac{k}{t}dt}=t^k$</summary>

Step 1 · $h=\frac2y$:

$$
\mu=e^{2\ln y}=y^2
$$

Step 2 · $h=-\frac1y$:

$$
\mu=e^{-\ln y}=\dfrac1y
$$

Step 3 · $g=-\frac2t$:

$$
\mu=e^{-2\ln t}=\dfrac{1}{t^2}
$$

</details>

> **Warning:** **The two ratios are different.** Case 1: $M_y-N_t$ over $N$. Case 2: $N_t-M_y$ (flipped) over $M$. Mix them up and the sign of $\mu$’s power flips.

#### Practice: B4

**Problem: Problem 21 · W4 · A factor in y only** (introductory)

Solve $y\,dt+(2t+y^3)\,dy=0$.

<details><summary>Solution</summary>

1. **Type:** $dt$, $dy$ form → test for B3.
2. **Write.**

   $$M=y,\qquad N=2t+y^3$$
3. **Test:** not exact → B4.

   $$M_y=1,\qquad N_t=2$$
4. **Find $\mu$:** Case 1 gives $\frac{-1}{2t+y^3}$, both letters. Case 2 leaves only $y$.

   $$\begin{gathered}\dfrac{N_t-M_y}{M}=\dfrac{2-1}{y}=\dfrac1y \\ \mu=e^{\ln y}=y\end{gathered}$$
5. **Multiply** by $y$.

   $$y^2\,dt+(2ty+y^4)\,dy=0$$
6. **Re-test.**

   $$M_y=2y,\qquad N_t=2y\quad\checkmark$$
7. **Integrate $M$ in $t$.**

   $$U=ty^2+h(y)$$
8. **Match $N$:** $U_y=2ty+h^{\prime}$ must equal $2ty+y^4$.

   $$h^{\prime}=y^4\quad\Rightarrow\quad h=\dfrac{y^5}{5}$$
9. **Answer.**

   $$ty^2+\dfrac{y^5}{5}=C$$

**Answer:** $ty^2+\dfrac{y^5}{5}=C$.

</details>

**Problem: Problem 22 · W4 · Which case applies?** (advanced)

Find an integrating factor for each equation, then solve it.

(a) $(2y+3t)\,dt+t\,dy=0$

(b) $y^2\,dt+(ty+1)\,dy=0$

<details><summary>Solution</summary>

1. (a) **Write** and **test:** $M=2y+3t$, $N=t$.

   $$M_y=2,\qquad N_t=1$$
2. (a) **Find $\mu$:** Case 1 leaves only $t$.

   $$\begin{gathered}\dfrac{M_y-N_t}{N}=\dfrac{2-1}{t}=\dfrac1t \\ \mu=e^{\ln t}=t\end{gathered}$$
3. (a) **Multiply** by $t$: it’s exactly the B3 lecture example.

   $$(2ty+3t^2)\,dt+t^2\,dy=0$$
4. (a) **Answer:** from B3.

   $$t^2y+t^3=C$$
5. (b) **Write** and **test:** $M=y^2$, $N=ty+1$.

   $$M_y=2y,\qquad N_t=y$$
6. (b) **Find $\mu$:** Case 1 gives $\frac{y}{ty+1}$, both letters. Case 2:

   $$\begin{gathered}\dfrac{N_t-M_y}{M}=\dfrac{y-2y}{y^2}=-\dfrac1y \\ \mu=e^{-\ln y}=\dfrac1y\end{gathered}$$
7. (b) **Multiply** by $\frac1y$ and **re-test.**

   $$\begin{gathered}y\,dt+\Big(t+\dfrac1y\Big)dy=0 \\ M_y=1,\qquad N_t=1\quad\checkmark\end{gathered}$$
8. (b) **Integrate $M$** and **match $N$:** $U=ty+h(y)$, and $U_y=t+h^{\prime}$ must equal $t+\frac1y$.

   $$h^{\prime}=\dfrac1y\quad\Rightarrow\quad h=\ln|y|$$
9. (b) **Answer.**

   $$ty+\ln|y|=C$$

**Answer:** (a) $\mu=t$, $\;t^2y+t^3=C$. (b) $\mu=\dfrac1y$, $\;ty+\ln|y|=C$.

</details>

### B5 · Second order, numbers in front, right side 0

[Week 5 · Topic 1](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/0c7a77fe-aeed-47a8-b1c3-4967d73eea21#92fa557c-ab2a-49cb-a238-b9f4e76fa0b8)

**Use this when** the equation looks like this, and you want $y(t)$:

$$
y^{\prime\prime}+3y^{\prime}+2y=0
$$

That is: a $y^{\prime\prime}$, plain numbers in front of $y^{\prime\prime}$, $y^{\prime}$ and $y$, and $0$ on the right.

- Right side not $0$, like $y^{\prime\prime}+y=3$? → [B6](#b6).
- $t$ in front, like $ty^{\prime\prime}+y=0$? → [B7](#b7).

**The move: turn the ODE into a quadratic.**

Swap $y^{\prime\prime}\to s^2$, $y^{\prime}\to s$, $y\to1$. Keep the numbers in front.

$$
y^{\prime\prime}+3y^{\prime}+2y=0\quad\longrightarrow\quad s^2+3s+2=0
$$

Two more:

$$
4y^{\prime\prime}+4y^{\prime}+y=0\quad\longrightarrow\quad 4s^2+4s+1=0
$$

$$
y^{\prime\prime}+9y=0\quad\longrightarrow\quad s^2+9=0
$$

No $y^{\prime}$ means no $s$ term. This quadratic is called the **characteristic equation**.

<details><summary>Why are we allowed to do this? (optional)</summary>

Guess $y=e^{st}$. Each derivative pulls out one more $s$:

$$
y^{\prime}=s\,e^{st},\qquad y^{\prime\prime}=s^2e^{st}
$$

Plug them into $y^{\prime\prime}+3y^{\prime}+2y=0$:

$$
s^2e^{st}+3s\,e^{st}+2e^{st}=0
$$

Pull out the $e^{st}$:

$$
(s^2+3s+2)\,e^{st}=0
$$

$e^{st}$ is never $0$, so the bracket must be $0$. That bracket is the quadratic.

So every root $s$ gives a solution $e^{st}$. Two roots give two solutions, and the general solution is $c_1$ times one plus $c_2$ times the other.

</details>

**Steps**

1. **Write** the quadratic: $as^2+bs+c=0$.
2. **Solve** it. Factor if you can. If not, use the quadratic formula (below).
3. **Pick** the case from what the roots look like. It tells you the form of $y$.
4. **Differentiate** $y$ to get $y^{\prime}$ (only if they give you $y^{\prime}(0)$).
5. **Plug in** $t=0$: $y(0)$ and $y^{\prime}(0)$ give two equations. Solve them for $c_1$ and $c_2$.

The quadratic formula:

$$
s=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}
$$

The number under the root, $b^2-4ac$, tells you the case:

| $b^2-4ac$ | Roots | Go to |
|---|---|---|
| $>0$ | two different real numbers | Case 1 |
| $=0$ | one number, twice | Case 2 |
| $<0$ | a complex pair ($\pm j$) | Case 3 |

#### Case 1: two different real roots

The quadratic gives two different numbers, $s_1$ and $s_2$.

Each one gives an exponential:

$$
y=c_1e^{s_1t}+c_2e^{s_2t}
$$

**Short example:**

$$
s=-1,\ -2\quad\Longrightarrow\quad y=c_1e^{-t}+c_2e^{-2t}
$$

<details><summary>Full example: $\;y^{\prime\prime}+3y^{\prime}+2y=0$, $\;y(0)=1$, $\;y^{\prime}(0)=0$</summary>

Step 1 · **Write** the quadratic.

$$
s^2+3s+2=0
$$

Step 2 · **Solve:** it factors. Two numbers that multiply to $2$ and add to $3$: $1$ and $2$.

$$
(s+1)(s+2)=0
$$

$$
s_1=-1,\qquad s_2=-2
$$

Step 3 · **Pick:** two different real roots, so Case 1.

$$
y=c_1e^{-t}+c_2e^{-2t}
$$

Step 4 · **Differentiate:** the derivative of $e^{kt}$ is $k\,e^{kt}$.

$$
y^{\prime}=-c_1e^{-t}-2c_2e^{-2t}
$$

Step 5 · **Plug in** $t=0$. Every $e^{0}=1$.

$$
y(0)=c_1+c_2=1
$$

$$
y^{\prime}(0)=-c_1-2c_2=0
$$

Step 6 · **Solve for $c_1$ and $c_2$:** add the two equations. The $c_1$’s cancel.

$$
-c_2=1\quad\Rightarrow\quad c_2=-1
$$

$$
c_1=1-c_2=2
$$

**Answer:**

$$
y=2e^{-t}-e^{-2t}
$$

</details>

#### Case 2: one repeated root

The quadratic gives the same number $s$ twice.

$c_1e^{st}+c_2e^{st}$ would really be just one term. So the second piece gets an extra $t$:

$$
y=(c_1+c_2t)\,e^{st}
$$

**Short example:**

$$
s=-2\ \text{(twice)}\quad\Longrightarrow\quad y=(c_1+c_2t)\,e^{-2t}
$$

<details><summary>Full example: $\;y^{\prime\prime}+4y^{\prime}+4y=0$, $\;y(0)=1$, $\;y^{\prime}(0)=1$</summary>

Step 1 · **Write** the quadratic.

$$
s^2+4s+4=0
$$

Step 2 · **Solve:** it’s a perfect square. (Check: $b^2-4ac=16-16=0$, so Case 2.)

$$
(s+2)^2=0
$$

$$
s=-2\ \text{(twice)}
$$

Step 3 · **Pick:** repeated root, so Case 2.

$$
y=(c_1+c_2t)\,e^{-2t}
$$

Step 4 · **Differentiate** with the product rule: (front)$^{\prime}$ times $e^{-2t}$, plus front times $(e^{-2t})^{\prime}$.

$$
y^{\prime}=c_2\,e^{-2t}-2(c_1+c_2t)\,e^{-2t}
$$

Step 5 · **Plug in** $t=0$. The $c_2t$ becomes $0$, and $e^{0}=1$.

$$
y(0)=c_1=1
$$

$$
y^{\prime}(0)=c_2-2c_1=1
$$

Step 6 · **Solve for $c_1$ and $c_2$:** put $c_1=1$ into the second equation.

$$
c_2-2=1\quad\Rightarrow\quad c_2=3
$$

**Answer:**

$$
y=(1+3t)\,e^{-2t}
$$

</details>

<details><summary>Why the extra $t$? (optional)</summary>

$c_1e^{st}$ and $c_2e^{st}$ are the same function, so together they only give one constant. You need a second, different solution.

When the root is repeated, $te^{st}$ also solves the ODE. Check with $y=te^{-2t}$ in $y^{\prime\prime}+4y^{\prime}+4y$: you get $0$.

It comes from reduction of order: see the first practice problem in [B7](#b7).

</details>

#### Case 3: complex roots

The number under the square root is negative. That’s fine.

Pull out a $j$, where $j=\sqrt{-1}$:

$$
\sqrt{-16}=\sqrt{16}\cdot\sqrt{-1}=4j
$$

So the two roots come out as a pair: the same real part, and $\pm$ a $j$ part.

$$
s=\sigma\pm j\omega
$$

- $\sigma$ (“sigma”) = the **real part**: the number without $j$.
- $\omega$ (“omega”) = the **$j$ part**: the number next to $j$, without the $\pm$.

For example:

$$
s=-1\pm j2\quad\Longrightarrow\quad \sigma=-1,\quad \omega=2
$$

The answer has **no $j$ in it**. The real part goes in the exponential. The $j$ part goes inside $\cos$ and $\sin$:

$$
y=e^{\sigma t}\,(c_1\cos\omega t+c_2\sin\omega t)
$$

**Short example:**

$$
s=-1\pm j2\quad\Longrightarrow\quad y=e^{-t}(c_1\cos2t+c_2\sin2t)
$$

<details><summary>Full example: $\;y^{\prime\prime}+2y^{\prime}+5y=0$, $\;y(0)=1$, $\;y^{\prime}(0)=1$</summary>

Step 1 · **Write** the quadratic.

$$
s^2+2s+5=0
$$

Step 2 · **Solve:** it doesn’t factor, so use the formula with $a=1$, $b=2$, $c=5$. Start with the part under the root. It’s negative, so Case 3.

$$
b^2-4ac=4-20=-16
$$

$$
\sqrt{-16}=j4
$$

$$
s=\dfrac{-2\pm j4}{2}=-1\pm j2
$$

Step 3 · **Pick:** Case 3 with real part $\sigma=-1$ and $j$ part $\omega=2$.

$$
y=e^{-t}(c_1\cos2t+c_2\sin2t)
$$

Step 4 · **Differentiate** with the product rule: $(e^{-t})^{\prime}$ times the bracket, plus $e^{-t}$ times (the bracket)$^{\prime}$.

$$
\begin{aligned}y^{\prime}&=-e^{-t}(c_1\cos2t+c_2\sin2t)\\&\quad+e^{-t}(-2c_1\sin2t+2c_2\cos2t)\end{aligned}
$$

Step 5 · **Plug in** $t=0$: $e^{0}=1$, $\cos0=1$, $\sin0=0$.

$$
y(0)=c_1=1
$$

$$
y^{\prime}(0)=-c_1+2c_2=1
$$

Step 6 · **Solve for $c_1$ and $c_2$:** put $c_1=1$ into the second equation.

$$
2c_2=2\quad\Rightarrow\quad c_2=1
$$

**Answer:**

$$
y=e^{-t}(\cos2t+\sin2t)
$$

</details>

**No $y^{\prime}$ term?** Like $y^{\prime\prime}+9y=0$:

$$
s^2+9=0\quad\Longrightarrow\quad s^2=-9\quad\Longrightarrow\quad s=\pm j3
$$

So $\sigma=0$ and $\omega=3$. Since $e^{0t}=1$, the exponential disappears:

$$
y=c_1\cos3t+c_2\sin3t
$$

<details><summary>Why $\cos$ and $\sin$, and where did the $j$ go? (optional)</summary>

The two roots give $e^{(\sigma+j\omega)t}$ and $e^{(\sigma-j\omega)t}$. Euler’s formula splits each one:

$$
e^{(\sigma\pm j\omega)t}=e^{\sigma t}\,(\cos\omega t\pm j\sin\omega t)
$$

Adding and subtracting the two solutions cancels the $j$’s. What’s left is $e^{\sigma t}\cos\omega t$ and $e^{\sigma t}\sin\omega t$.

Both are real solutions, so the general solution is $c_1$ times one plus $c_2$ times the other.

</details>

#### Traps and a quick check

> **Warning:** **Differentiate first, then plug in $t=0$.** In Cases 2 and 3 the product rule gives an extra term. Skip it and you get the wrong $c_2$. Example: in Case 2 above, $y^{\prime}(0)=c_2-2c_1$, not just $c_2$.

> **Warning:** **$\sigma$ keeps its sign.** $s=-1\pm j2$ gives $e^{-t}$, not $e^{t}$. Only $\omega$ drops the sign.

**Shortcut to check $c_1$ and $c_2$.** At $t=0$, each case always gives the same two equations. Open a card for a short example.

(Only for conditions at $t=0$. At another time, like $y(1)$, differentiate yourself.)

<details><summary>Case 1: $\;y(0)=c_1+c_2,\quad y^{\prime}(0)=s_1c_1+s_2c_2$</summary>

Step 1 · Roots $-2$ and $-3$, with $y(0)=2$ and $y^{\prime}(0)=-5$. Case 1:

$$
y=c_1e^{-2t}+c_2e^{-3t}
$$

Step 2 · $y(0)$: just add the constants.

$$
c_1+c_2=2
$$

Step 3 · $y^{\prime}(0)$: each root times its constant.

$$
-2c_1-3c_2=-5
$$

Step 4 · Multiply the first by $2$ and add: $-c_2=-1$.

$$
c_2=1
$$

$$
c_1=1
$$

Step 5 · Where it comes from: differentiate, then every $e^{0}=1$.

$$
y^{\prime}=s_1c_1e^{s_1t}+s_2c_2e^{s_2t}\quad\Rightarrow\quad y^{\prime}(0)=s_1c_1+s_2c_2
$$

</details>

<details><summary>Case 2: $\;y(0)=c_1,\quad y^{\prime}(0)=sc_1+c_2$</summary>

Step 1 · Root $-\tfrac12$ twice, with $y(0)=4$ and $y^{\prime}(0)=0$. Case 2:

$$
y=(c_1+c_2t)\,e^{-t/2}
$$

Step 2 · $y(0)$: the $c_2t$ is $0$ at $t=0$.

$$
c_1=4
$$

Step 3 · $y^{\prime}(0)$: the root times $c_1$, plus $c_2$.

$$
-\tfrac12c_1+c_2=0
$$

Step 4 · Put in $c_1=4$: $-2+c_2=0$.

$$
c_2=2
$$

Step 5 · Where it comes from: the product rule, then $t=0$.

$$
y^{\prime}=c_2e^{st}+s(c_1+c_2t)e^{st}\quad\Rightarrow\quad y^{\prime}(0)=c_2+sc_1
$$

</details>

<details><summary>Case 3: $\;y(0)=c_1,\quad y^{\prime}(0)=\sigma c_1+\omega c_2$</summary>

Step 1 · Roots $-3\pm j4$, so $\sigma=-3$ and $\omega=4$, with $y(0)=0$ and $y^{\prime}(0)=8$. Case 3:

$$
y=e^{-3t}(c_1\cos4t+c_2\sin4t)
$$

Step 2 · $y(0)$: $\cos0=1$ and $\sin0=0$.

$$
c_1=0
$$

Step 3 · $y^{\prime}(0)$: $\sigma$ times $c_1$, plus $\omega$ times $c_2$.

$$
-3c_1+4c_2=8
$$

Step 4 · Put in $c_1=0$: $4c_2=8$.

$$
c_2=2
$$

Step 5 · Where it comes from: the product rule, then $t=0$. The $\sin0=0$ wipes out two of the terms.

$$
y^{\prime}(0)=\sigma c_1+\omega c_2
$$

</details>

**What do the three cases look like?**

```graph
title "Slide $k$ through 1: the same start, all three cases"
x 0 8 label="$t$"
y -0.6 1.2 label="$y$"
slider k 0 5 0.5 step=0.05 label="$k$" animate
let d "sqrt(abs(1-k))"
let s1 "-1+d"
let s2 "-1-d"
curve "if(k<0.999, (s2*exp(s1*x)-s1*exp(s2*x))/(s2-s1), if(k>1.001, exp(-x)*(cos(d*x)+sin(d*x)/d), (1+x)*exp(-x)))" label="$y(t)$" color=1
hline "0"
readout "$b^2-4ac=4-4k$" "4-4*k"
caption "$y^{\prime\prime}+2y^{\prime}+ky=0$, starting at $y(0)=1$, $y^{\prime}(0)=0$. $k<1$: Case 1, it settles with no wiggle. $k=1$: Case 2, the border. $k>1$: Case 3, it wiggles while $e^{-t}$ shrinks it. Same three cases as an RLC circuit in D2."
```

#### Practice: B5

**Problem: Problem 23 · W5 · Two different real roots** (introductory)

Solve $y^{\prime\prime}+5y^{\prime}+6y=0$, $\;y(0)=2$, $y^{\prime}(0)=-5$.

<details><summary>Solution</summary>

1. **Type:** second order, numbers in front, right side $0$ → B5.
2. **Write** the quadratic.

   $$s^2+5s+6=0$$
3. **Solve:** two numbers that multiply to $6$ and add to $5$: $2$ and $3$.

   $$(s+2)(s+3)=0\quad\Rightarrow\quad s=-2,\,-3$$
4. **Pick:** two different real roots → Case 1.

   $$y=c_1e^{-2t}+c_2e^{-3t}$$
5. **Differentiate.**

   $$y^{\prime}=-2c_1e^{-2t}-3c_2e^{-3t}$$
6. **Plug in** $t=0$.

   $$c_1+c_2=2,\qquad -2c_1-3c_2=-5$$
7. Multiply the first equation by $2$ and add the second: $-c_2=-1$.

   $$c_2=1,\qquad c_1=1$$

**Answer:** $y=e^{-2t}+e^{-3t}$.

</details>

**Problem: Problem 24 · W5 · A repeated root** (introductory)

Solve $4y^{\prime\prime}+4y^{\prime}+y=0$, $\;y(0)=4$, $y^{\prime}(0)=0$.

<details><summary>Solution</summary>

1. **Type:** second order, numbers in front, right side $0$ → B5.
2. **Write** the quadratic.

   $$4s^2+4s+1=0$$
3. **Solve:** $b^2-4ac=16-16=0$, so one root. The formula gives $s=\frac{-4}{8}$.

   $$s=-\tfrac12\ \text{(twice)}$$
4. **Pick:** repeated root → Case 2.

   $$y=(c_1+c_2t)\,e^{-t/2}$$
5. **Differentiate** with the product rule.

   $$y^{\prime}=c_2e^{-t/2}-\tfrac12(c_1+c_2t)\,e^{-t/2}$$
6. **Plug in** $t=0$.

   $$c_1=4,\qquad c_2-\tfrac12c_1=0$$
7. Put $c_1=4$ into the second equation.

   $$c_2=2$$

**Answer:** $y=(4+2t)\,e^{-t/2}$.

</details>

**Problem: Problem 25 · W5 · No damping term** (intermediate)

Solve $y^{\prime\prime}+9y=0$, $\;y(0)=2$, $y^{\prime}(0)=3$.

<details><summary>Solution</summary>

1. **Type:** second order, numbers in front, right side $0$ → B5.
2. **Write** the quadratic. No $y^{\prime}$, so no $s$ term.

   $$s^2+9=0$$
3. **Solve:** $s^2=-9$, and $\sqrt{-9}=j3$.

   $$s=\pm j3$$
4. **Pick:** Case 3 with $\sigma=0$, $\omega=3$. $e^{0t}=1$, so no exponential.

   $$y=c_1\cos3t+c_2\sin3t$$
5. **Differentiate.**

   $$y^{\prime}=-3c_1\sin3t+3c_2\cos3t$$
6. **Plug in** $t=0$: $\cos0=1$, $\sin0=0$.

   $$c_1=2,\qquad 3c_2=3\ \Rightarrow\ c_2=1$$

**Answer:** $y=2\cos3t+\sin3t$. Nothing shrinks it, so it swings forever: that’s the ideal LC circuit in [D2](#d2).

</details>

**Problem: Problem 26 · W5 · Work backwards from the roots** (advanced)

A constant-coefficient equation $y^{\prime\prime}+by^{\prime}+cy=0$ has roots $-3\pm j4$. 

(a) Find $b$ and $c$. (b) Write the general solution. (c) Find the solution with $y(0)=0$, $y^{\prime}(0)=8$.

<details><summary>Solution</summary>

1. **Type:** backwards. Roots $s_1$, $s_2$ come from the quadratic $(s-s_1)(s-s_2)=0$.
2. (a) Multiply out. The brackets are $(s+3)-j4$ and $(s+3)+j4$: a difference of squares. And $(j4)^2=16j^2=-16$.

   $$(s+3)^2-(j4)^2=s^2+6s+9+16=s^2+6s+25$$
3. So $b=6$ and $c=25$.

   $$y^{\prime\prime}+6y^{\prime}+25y=0$$
4. (b) **Pick:** Case 3 with $\sigma=-3$, $\omega=4$.

   $$y=e^{-3t}(c_1\cos4t+c_2\sin4t)$$
5. (c) **Differentiate** with the product rule.

   $$y^{\prime}=-3e^{-3t}(c_1\cos4t+c_2\sin4t)+e^{-3t}(-4c_1\sin4t+4c_2\cos4t)$$
6. **Plug in** $t=0$.

   $$c_1=0,\qquad -3c_1+4c_2=8\ \Rightarrow\ c_2=2$$

**Answer:** (a) $b=6$, $c=25$. (b) $y=e^{-3t}(c_1\cos4t+c_2\sin4t)$. (c) $y=2e^{-3t}\sin4t$.

</details>

### B6 · Second order, numbers in front, right side f(t)

[Week 6 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/357f26bd-d16c-4769-af0a-d1b2f535d62e#77a5aea3-a3f4-4738-a817-01c3f18cfdae)

**Use this when** it looks like [B5](#b5), but the right side is **not** $0$:

$$
y^{\prime\prime}+y=3
$$

Every one of these looks like:

$$
a\,y^{\prime\prime}+b\,y^{\prime}+c\,y=f(t)
$$

- $a,b,c$ = plain numbers, same as [B5](#b5)
- $f(t)$ = the right side, everything with no $y$ in it (in a circuit: the source)

**The move: the answer comes in two pieces.**

$$
y=y_c+y_p
$$

- $y_c$ = the [B5](#b5) answer, with the right side set to $0$. It carries $c_1$ and $c_2$.
- $y_p$ = one guess that gives exactly $f(t)$. Copy the **shape** of $f(t)$, with unknown numbers $A,B,D$ in front.

**Short example:** $y^{\prime\prime}+y=3$:

$$
y_c=c_1\sin t+c_2\cos t,\qquad y_p=3
$$

$$
y=3+c_1\sin t+c_2\cos t
$$

<details><summary>Why add two pieces? (optional)</summary>

Plug $y_c+y_p$ into the left side. The $y_c$ part gives $0$ (that’s how B5 built it). The $y_p$ part gives $f$. Total: $0+f=f$.

And $y_p$ has no free constants, so on its own it can’t meet two conditions like $y(0)$ and $y^{\prime}(0)$. $y_c$ brings the $c_1,c_2$ that the conditions pin down.

</details>

**Steps**

1. **Write** it with every $y$ term on the left and $f(t)$ on the right.
2. **Solve $y_c$:** set the right side to $0$ and do [B5](#b5) (quadratic → case → form with $c_1,c_2$).
3. **Guess $y_p$** from the cases below. If any term of it is already in $y_c$, multiply it by $t$.
4. **Plug $y_p$ into the ODE and match:** constants with constants, each $\cos$, each $\sin$, each power of $t$. Solve for $A,B,\dots$
5. **Add:** $y=y_c+y_p$.
6. **Plug in** the conditions on the **whole** $y$, never on $y_c$ alone.

> **Tip:** **What the lecture worked (Mon Oct 26):** Cases 1 and 3 below (a constant, and $\sin$/$\cos$). That’s exactly what the tutorial problem needs. Nail those first.

#### Case 1: f is a constant or a polynomial

Guess a polynomial of the **same degree**, with **every lower power** too:

$$
\begin{gathered}8\ \to\ A, \\ 2t\ \to\ At+B, \\ t^2\ \to\ At^2+Bt+D\end{gathered}
$$

<details><summary>Full example: $\;y^{\prime\prime}+y^{\prime}-2y=2t$ (general solution)</summary>

Step 1 · **Solve $y_c$:** set the right side to $0$. The quadratic factors.

$$
s^2+s-2=(s+2)(s-1)=0
$$

$$
y_c=c_1e^{t}+c_2e^{-2t}
$$

Step 2 · **Guess $y_p$:** degree 1, so $At+B$. You need the $B$ even though $f$ has no constant.

$$
y_p=At+B
$$

$$
y_p^{\prime}=A,\qquad y_p^{\prime\prime}=0
$$

Step 3 · **Plug in** to $y^{\prime\prime}+y^{\prime}-2y$.

$$
0+A-2(At+B)=2t
$$

Step 4 · **Match** the $t$ terms, then the constants.

$$
-2A=2
$$

$$
A-2B=0
$$

Step 5 · Solve.

$$
A=-1,\qquad B=-\tfrac12
$$

Step 6 · **Add.**

$$
y=c_1e^{t}+c_2e^{-2t}-t-\tfrac12
$$

**Answer:**

$$
y=c_1e^{t}+c_2e^{-2t}-t-\tfrac12
$$

</details>

#### Case 2: f is an exponential

Guess the same exponential:

$$
3e^{2t}\ \to\ Ae^{2t}
$$

<details><summary>Full example: $\;y^{\prime\prime}+3y^{\prime}+2y=6e^{t}$ (general solution)</summary>

Step 1 · **Solve $y_c$:** $s^2+3s+2=(s+1)(s+2)$.

$$
y_c=c_1e^{-t}+c_2e^{-2t}
$$

Step 2 · **Guess $y_p$:** $e^{t}$ is not in $y_c$. Every derivative of $Ae^{t}$ is $Ae^{t}$.

$$
y_p=Ae^{t},\qquad y_p^{\prime}=y_p^{\prime\prime}=Ae^{t}
$$

Step 3 · **Plug in and match:** divide by $e^{t}$.

$$
A+3A+2A=6\quad\Rightarrow\quad A=1
$$

Step 4 · **Add.**

$$
y=c_1e^{-t}+c_2e^{-2t}+e^{t}
$$

**Answer:**

$$
y=c_1e^{-t}+c_2e^{-2t}+e^{t}
$$

</details>

#### Case 3: f is a sin or a cos

Guess **both** $\cos$ and $\sin$, even if $f$ has only one:

$$
5\sin2t\ \to\ A\cos2t+B\sin2t
$$

Why both: each derivative swaps $\cos$ and $\sin$, so both show up anyway. Handy fact: two derivatives multiply by $-r^2$:

$$
(A\cos rt+B\sin rt)^{\prime\prime}=-r^2(A\cos rt+B\sin rt)
$$

<details><summary>Full example: $\;y^{\prime\prime}+3y^{\prime}+2y=10\sin t$ (general solution)</summary>

Step 1 · **Solve $y_c$:** same quadratic as Case 2.

$$
y_c=c_1e^{-t}+c_2e^{-2t}
$$

Step 2 · **Guess $y_p$:** both $\cos t$ and $\sin t$.

$$
y_p=A\cos t+B\sin t
$$

$$
y_p^{\prime}=-A\sin t+B\cos t
$$

$$
y_p^{\prime\prime}=-A\cos t-B\sin t
$$

Step 3 · **Plug in** to $y^{\prime\prime}+3y^{\prime}+2y$ and collect the $\cos t$ and $\sin t$ terms.

$$
(A+3B)\cos t+(B-3A)\sin t=10\sin t
$$

Step 4 · **Match:** the right side has no $\cos t$, so its coefficient is $0$.

$$
A+3B=0
$$

$$
B-3A=10
$$

Step 5 · Solve: $A=-3B$, so $B+9B=10$.

$$
B=1,\qquad A=-3
$$

Step 6 · **Add.**

$$
y=c_1e^{-t}+c_2e^{-2t}-3\cos t+\sin t
$$

**Answer:**

$$
y=c_1e^{-t}+c_2e^{-2t}-3\cos t+\sin t
$$

</details>

**A sum of these?** Guess the sum of their guesses:

$$
t+e^{t}\ \to\ At+B+De^{t}
$$

**A $\cos^2t$ or $\sin^2t$?** Turn it into a constant plus $\cos2t$ first:

$$
\begin{gathered}\cos^2t=\tfrac12+\tfrac12\cos2t, \\ \sin^2t=\tfrac12-\tfrac12\cos2t\end{gathered}
$$

#### Case 4: the guess is already in y_c

Then plugging it in gives $0$, never $f$. **Multiply the guess by $t$.** Still in $y_c$ (a repeated root)? Multiply by $t^2$.

$$
y_c=c_1e^{2t}+c_2e^{-t},\quad f=3e^{2t}\quad\Longrightarrow\quad y_p=Ate^{2t}
$$

<details><summary>Full example: $\;y^{\prime\prime}-y^{\prime}-2y=3e^{2t}$ (general solution)</summary>

Step 1 · **Solve $y_c$:** $s^2-s-2=(s-2)(s+1)$.

$$
y_c=c_1e^{2t}+c_2e^{-t}
$$

Step 2 · **Guess $y_p$:** Case 2 says $Ae^{2t}$, but that’s in $y_c$. Multiply by $t$.

$$
y_p=Ate^{2t}
$$

Step 3 · Differentiate with the product rule, twice.

$$
y_p^{\prime}=A(1+2t)e^{2t}
$$

$$
y_p^{\prime\prime}=A(4+4t)e^{2t}
$$

Step 4 · **Plug in** and divide by $e^{2t}$. The $t$ terms cancel.

$$
A\big[(4+4t)-(1+2t)-2t\big]=3A=3
$$

Step 5 · **Match.**

$$
A=1
$$

Step 6 · **Add.**

$$
y=c_1e^{2t}+c_2e^{-t}+te^{2t}
$$

**Answer:**

$$
y=c_1e^{2t}+c_2e^{-t}+te^{2t}
$$

</details>

> **Warning:** **Always find $y_c$ before you guess.** That’s the only way to spot Case 4.

#### The tutorial problem (know this cold)

Pre-tutorial 5, the Week 7 tutorial (Oct 26, 28), and the lecture’s own example. Be able to do every step, the two conditions included. ($\ddot y$ is the professor’s way of writing $y^{\prime\prime}$.)

$$
\ddot y+y=6\cos^2t,\qquad y(0)=0,\quad y(\pi/2)=0
$$

<details><summary>Full solution: $\;\ddot y+y=6\cos^2t$, $\;y(0)=0$, $\;y(\pi/2)=0$</summary>

Step 1 · **Solve $y_c$:** $s^2+1=0$ gives $s=\pm j$ (B5 Case 3, $\sigma=0$, $\omega=1$).

$$
y_c=c_1\sin t+c_2\cos t
$$

Step 2 · No case for $\cos^2t$, so use the identity: a constant plus $\cos2t$.

$$
6\cos^2t=3+3\cos2t
$$

Step 3 · **Guess $y_p$:** the constant → $A$ (Case 1). The $\cos2t$ → both $\cos2t$ and $\sin2t$ (Case 3). None is in $y_c$.

$$
y_p=A+B\cos2t+D\sin2t
$$

Step 4 · Differentiate twice: each $\cos2t$, $\sin2t$ gets multiplied by $-4$.

$$
y_p^{\prime\prime}=-4B\cos2t-4D\sin2t
$$

Step 5 · **Plug in** to $y_p^{\prime\prime}+y_p$ and collect.

$$
A-3B\cos2t-3D\sin2t=3+3\cos2t
$$

Step 6 · **Match** the constants, the $\cos2t$’s and the $\sin2t$’s.

$$
A=3,\qquad B=-1,\qquad D=0
$$

Step 7 · **Add** $y_c$ **before** the conditions: they belong to the whole $y$.

$$
y=3-\cos2t+c_1\sin t+c_2\cos t
$$

Step 8 · **Plug in** $y(0)=0$: $\sin0=0$, $\cos0=1$.

$$
3-1+c_2=0\quad\Rightarrow\quad c_2=-2
$$

Step 9 · **Plug in** $y(\pi/2)=0$: $\cos\pi=-1$, $\sin\frac\pi2=1$, $\cos\frac\pi2=0$.

$$
3+1+c_1=0\quad\Rightarrow\quad c_1=-4
$$

**Answer:**

$$
y=3-\cos2t-4\sin t-2\cos t
$$

</details>

The tutorial hands you the forms of $y_c$ and $y_p$. On the exam they might not: the [Topic E](#topic-e) version has no hints.

#### Practice: B6

**Problem: Problem 27 · W6 · A constant right side, from rest** (introductory)

Solve $y^{\prime\prime}+4y=8$, $\;y(0)=0$, $y^{\prime}(0)=0$.

<details><summary>Solution</summary>

1. **Type:** numbers in front, right side $8$ → B6.
2. **Solve $y_c$:** $s^2+4=0$, $s=\pm j2$ (B5 Case 3).

   $$y_c=c_1\cos2t+c_2\sin2t$$
3. **Guess $y_p$:** a constant (Case 1). Not in $y_c$.

   $$y_p=A$$
4. **Plug in and match:** $y_p^{\prime\prime}=0$.

   $$0+4A=8\quad\Rightarrow\quad A=2$$
5. **Add.**

   $$y=2+c_1\cos2t+c_2\sin2t$$
6. **Differentiate** for $y^{\prime}(0)$.

   $$y^{\prime}=-2c_1\sin2t+2c_2\cos2t$$
7. **Plug in** $t=0$.

   $$\begin{gathered}y(0)=2+c_1=0\quad\Rightarrow\quad c_1=-2 \\ y^{\prime}(0)=2c_2=0\quad\Rightarrow\quad c_2=0\end{gathered}$$

**Answer:** $y=2-2\cos2t$. A constant source gives a constant $y_p$, like an RLC circuit switched onto DC ([D2](#d2)).

</details>

**Problem: Problem 28 · W6 · Choose the form; do not solve** (intermediate)

For $y^{\prime\prime}-2y^{\prime}+y=f(t)$, write the guess for $y_p$ when $f$ is (a) $t^2$, (b) $e^{-t}$, (c) $e^t$, (d) $\cos t$.

<details><summary>Solution</summary>

1. **Solve $y_c$ first** (you need it for Case 4): $s^2-2s+1=(s-1)^2$, a repeated root.

   $$y_c=(c_1+c_2t)\,e^{t}$$
2. (a) Case 1, degree 2: every lower power too.

   $$At^2+Bt+D$$
3. (b) Case 2. $e^{-t}$ is not in $y_c$.

   $$Ae^{-t}$$
4. (c) Case 4. $Ae^t$ is in $y_c$, and so is $Ate^t$. Multiply by $t^2$.

   $$At^2e^{t}$$
5. (d) Case 3: both $\cos$ and $\sin$.

   $$A\cos t+B\sin t$$

**Answer:** (a) $At^2+Bt+D$. (b) $Ae^{-t}$. (c) $At^2e^{t}$. (d) $A\cos t+B\sin t$.

</details>

**Problem: Problem 29 · W6 · A trig guess that is already in y_c** (advanced)

Find a particular solution of $y^{\prime\prime}+9y=12\cos3t$. Use $(t\,u)^{\prime\prime}=t\,u^{\prime\prime}+2u^{\prime}$ (product rule twice).

<details><summary>Solution</summary>

1. **Solve $y_c$:** $s=\pm j3$.

   $$y_c=c_1\cos3t+c_2\sin3t$$
2. **Guess $y_p$:** Case 3 says $A\cos3t+B\sin3t$, but that’s in $y_c$. Case 4: multiply by $t$.

   $$\begin{gathered}y_p=t\,u \\ u=A\cos3t+B\sin3t\end{gathered}$$
3. **Plug in:** $u^{\prime\prime}=-9u$, so the $t$ terms cancel.

   $$y_p^{\prime\prime}+9y_p=t(u^{\prime\prime}+9u)+2u^{\prime}=2u^{\prime}$$
4. Differentiate $u$.

   $$2u^{\prime}=-6A\sin3t+6B\cos3t$$
5. **Match** with $12\cos3t$.

   $$6B=12,\qquad -6A=0$$

**Answer:** $A=0$, $B=2$: $\;y_p=2t\sin3t$. It keeps growing like $2t$: that’s **resonance**.

</details>

### B7 · Reduction of order: t in front, one solution given

[Week 6 · Topic 1](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/357f26bd-d16c-4769-af0a-d1b2f535d62e#400c9eda-6dcb-4cf4-9c21-265384342cb1)

**Use this when** it’s second order with $t$ in front (so [B5](#b5) fails), and they **give you one solution** $y_1$:

$$
y^{\prime\prime}-t\,y^{\prime}+y=0,\qquad y_1=t
$$

Write it with $y^{\prime\prime}$ alone (divide by whatever multiplies it):

$$
y^{\prime\prime}+p(t)\,y^{\prime}+q(t)\,y=0
$$

- $p(t)$ = what multiplies $y^{\prime}$, sign included
- $q(t)$ = what multiplies $y$
- $y_1$ = the solution you’re given. Check it: plug it in, you should get $0$.

**Short example:**

$$
t^2y^{\prime\prime}-3ty^{\prime}+4y=0\quad\Longrightarrow\quad y^{\prime\prime}-\dfrac3t\,y^{\prime}+\dfrac4{t^2}\,y=0
$$

$$
p=-\dfrac3t,\qquad q=\dfrac{4}{t^2}
$$

**The move: guess $y=y_1\,v$.** The known solution times an unknown function $v(t)$.

$$
y=y_1\,v
$$

When you plug it in, every term with a plain $v$ **cancels**. Only $v^{\prime}$ and $v^{\prime\prime}$ are left. Call $z=v^{\prime}$ and it’s a **first-order** equation ([B1](#b1) or [B2](#b2)).

<details><summary>Why do the plain-$v$ terms cancel? (optional)</summary>

After you substitute, gather everything that multiplies $v$ itself. You get

$$
v\,(y_1^{\prime\prime}+p\,y_1^{\prime}+q\,y_1)
$$

The bracket is just $y_1$ plugged into the ODE, which is $0$ because $y_1$ is a solution.

</details>

**Steps**

1. **Write** it with $y^{\prime\prime}$ alone. Read $p$, $q$. Check $y_1$.
2. **Substitute** $y=y_1v$. Use the product rule for $y^{\prime}$ and $y^{\prime\prime}$ (below).
3. **Plug in and collect.** The plain-$v$ terms cancel.
4. **Solve for $z$:** set $z=v^{\prime}$. It’s first order: separate it ([B1](#b1)).
5. **Integrate:** $v=\int z\,dt+c_2$.
6. **Multiply back:** $y=y_1v$. The $c_2$ gives back $c_2\,y_1$, the solution you started with.
7. **Plug in** the conditions, if they give any.

The product rule for $y=y_1v$:

$$
y^{\prime}=y_1^{\prime}\,v+y_1\,v^{\prime}
$$

$$
y^{\prime\prime}=y_1^{\prime\prime}\,v+2y_1^{\prime}\,v^{\prime}+y_1\,v^{\prime\prime}
$$

**Short example:** with $y_1=t$:

$$
y=tv\quad\Longrightarrow\quad y^{\prime}=v+tv^{\prime},\quad y^{\prime\prime}=2v^{\prime}+tv^{\prime\prime}
$$

**The professor’s example**, step by step (press the arrows):

```steps
title "Lecture: reduce y″ − t y′ + y = 0, given y₁ = t"
$$ y^{\prime\prime}-ty^{\prime}+y=0,\qquad y_1=t $$
**Write.** Check: $y_1=t$ gives $0-t+t=0$.
$$ y=\hl{tv} $$
**Substitute:** the known solution times an unknown $v$.
$$ y^{\prime}=\hl{v+tv^{\prime}},\qquad y^{\prime\prime}=\hl{2v^{\prime}+tv^{\prime\prime}} $$
Product rule.
$$ (2v^{\prime}+tv^{\prime\prime})-t(v+tv^{\prime})+tv=0 $$
**Plug in** all three.
$$ \hl{tv^{\prime\prime}+(2-t^2)v^{\prime}}=0 $$
**Collect.** The $-tv$ and $+tv$ cancel.
$$ t\hl{z^{\prime}}+(2-t^2)\hl{z}=0 $$
Set $z=v^{\prime}$: now it’s first order in $z$.
```

<details><summary>Finish the lecture example: solve $\;tz^{\prime}+(2-t^2)z=0$, then find $y$</summary>

Step 1 · **Solve for $z$:** it separates. Divide by $tz$ and move the $t$ terms right.

$$
\dfrac{dz}{z}=\dfrac{t^2-2}{t}\,dt=\left(t-\dfrac2t\right)dt
$$

Step 2 · Integrate both sides.

$$
\ln|z|=\dfrac{t^2}2-2\ln|t|+C
$$

Step 3 · Raise $e$ to both sides. $e^{-2\ln|t|}=\frac1{t^2}$, and $e^{C}$ is a new constant $c_1$.

$$
z=c_1\,\dfrac{e^{t^2/2}}{t^2}
$$

Step 4 · **Integrate** $v=\int z\,dt$. This integral has no formula, so leave it as is.

$$
v=c_1\int\dfrac{e^{t^2/2}}{t^2}\,dt+c_2
$$

Step 5 · **Multiply back** by $y_1=t$.

$$
y=tv
$$

**Answer:**

$$
y=c_2\,t+c_1\,t\displaystyle\int\frac{e^{t^2/2}}{t^2}\,dt
$$

</details>

<details><summary>Full example: $\;t^2y^{\prime\prime}-3ty^{\prime}+4y=0$, $\;y_1=t^2$, $\;t>0$</summary>

Step 1 · **Write:** divide by $t^2$. Check $y_1$: $2t^2-6t^2+4t^2=0$ ✓.

$$
y^{\prime\prime}-\dfrac3t\,y^{\prime}+\dfrac4{t^2}\,y=0
$$

Step 2 · **Substitute** $y=t^2v$ (product rule).

$$
y^{\prime}=2tv+t^2v^{\prime}
$$

$$
y^{\prime\prime}=2v+4tv^{\prime}+t^2v^{\prime\prime}
$$

Step 3 · **Plug in and collect** (into the original, times $t^2$). The plain-$v$ terms cancel: $2-6+4=0$.

$$
t^4v^{\prime\prime}+t^3v^{\prime}=0
$$

Step 4 · **Solve for $z$:** divide by $t^4$, set $z=v^{\prime}$, separate.

$$
z^{\prime}+\dfrac zt=0
$$

$$
\dfrac{dz}{z}=-\dfrac{dt}{t}\quad\Rightarrow\quad z=\dfrac{c_1}{t}
$$

Step 5 · **Integrate:** $\int\frac1t\,dt=\ln t$ for $t>0$.

$$
v=c_1\ln t+c_2
$$

Step 6 · **Multiply back** by $t^2$.

$$
y=c_1t^2\ln t+c_2t^2
$$

**Answer:**

$$
y=c_1t^2\ln t+c_2t^2
$$

</details>

<details><summary>Check your answer: $\;y_2=y_1\displaystyle\int\dfrac{e^{-\int p\,dt}}{y_1^{\,2}}\,dt$</summary>

Step 1 · All the steps above always end at this formula. Use it to check, or as a shortcut if the question lets you. Same $p$ as in [B2](#b2).

$$
y_2=y_1\int\dfrac{e^{-\int p\,dt}}{y_1^{\,2}}\,dt
$$

Step 2 · Example: $t^2y^{\prime\prime}-3ty^{\prime}+4y=0$, $y_1=t^2$. Here $p=-\frac3t$.

$$
e^{-\int p\,dt}=e^{3\ln t}=t^3
$$

Step 3 · Plug in.

$$
y_2=t^2\int\dfrac{t^3}{t^4}\,dt=t^2\ln t\quad\checkmark
$$

</details>

> **Warning:** **Divide first.** $p$ is what multiplies $y^{\prime}$ **after** $y^{\prime\prime}$ stands alone. In $t^2y^{\prime\prime}-3ty^{\prime}+4y=0$, $p=-\frac3t$, not $-3t$.

> **Tip:** **An integral with no formula**, like $\int\frac{e^{t^2/2}}{t^2}dt$, can stay as an integral. That counts as a full answer.

#### Practice: B7

**Problem: Problem 30 · W5 + W6 · Where the repeated-root t comes from** (introductory)

$y^{\prime\prime}+4y^{\prime}+4y=0$ has the repeated root $s=-2$, so $y_1=e^{-2t}$. Use reduction of order to find the general solution.

<details><summary>Solution</summary>

1. **Type:** one solution given → B7.
2. **Substitute** $y=e^{-2t}v$ (product rule).

   $$\begin{gathered}y^{\prime}=e^{-2t}(v^{\prime}-2v) \\ y^{\prime\prime}=e^{-2t}(v^{\prime\prime}-4v^{\prime}+4v)\end{gathered}$$
3. **Plug in and collect**, then divide by $e^{-2t}$. This time the $v^{\prime}$ terms cancel too.

   $$(v^{\prime\prime}-4v^{\prime}+4v)+4(v^{\prime}-2v)+4v=v^{\prime\prime}=0$$
4. **Solve for $z$:** $z=v^{\prime}$, and $z^{\prime}=0$.

   $$z=c_2$$
5. **Integrate.**

   $$v=c_1+c_2t$$
6. **Multiply back.**

   $$y=(c_1+c_2t)\,e^{-2t}$$

**Answer:** $y=(c_1+c_2t)e^{-2t}$. That’s [B5](#b5) Case 2: the extra $t$ came from $v$.

</details>

**Problem: Problem 31 · W6 · A second solution with a logarithm** (intermediate)

For $t>0$, $y_1=t$ solves $t^2y^{\prime\prime}-ty^{\prime}+y=0$. Find the general solution.

<details><summary>Solution</summary>

1. **Type:** $t$ in front, one solution given → B7.
2. **Substitute** $y=tv$ (product rule).

   $$\begin{gathered}y^{\prime}=v+tv^{\prime} \\ y^{\prime\prime}=2v^{\prime}+tv^{\prime\prime}\end{gathered}$$
3. **Plug in and collect.** The plain-$v$ terms cancel: $-tv+tv=0$.

   $$\begin{gathered}t^2(2v^{\prime}+tv^{\prime\prime})-t(v+tv^{\prime})+tv=0 \\ t^3v^{\prime\prime}+t^2v^{\prime}=0\end{gathered}$$
4. **Solve for $z$:** divide by $t^3$, set $z=v^{\prime}$, separate.

   $$\begin{gathered}z^{\prime}+\dfrac zt=0 \\ z=\dfrac{c_1}{t}\end{gathered}$$
5. **Integrate.**

   $$v=c_1\ln t+c_2$$
6. **Multiply back** by $t$.

   $$y=c_1t\ln t+c_2t$$

**Answer:** $y=c_1t\ln t+c_2t$. Formula check: $p=-\frac1t$, $e^{-\int p\,dt}=t$, $y_2=t\int\frac{t}{t^2}dt=t\ln t$ ✓.

</details>

## Topic C: Does exactly one solution exist?

[Week 3 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/3d1ae4a9-687d-4654-873d-be3439faea2f#8c746b9b-2fbf-48f4-8a2d-704a643bdcf7) [Week 5 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/0c7a77fe-aeed-47a8-b1c3-4967d73eea21#b4f41ebe-f4f6-4d5d-816d-ceaa37811b8f)

**Use this when** the question asks “is there exactly one solution?” or “on what interval is one guaranteed?”.

**The move: don’t solve anything.** Write the equation in its form, then look for where something **breaks**:

$$
\begin{gathered}\dfrac{t}{y}\ \text{breaks at}\ y=0, \\ \ln t\ \text{breaks at}\ t\le0, \\ \sqrt{y}\ \text{breaks at}\ y<0\end{gathered}
$$

- First order, like $y^{\prime}=\dfrac ty$ → [C1](#c1).
- Second-order linear, like $t\,y^{\prime\prime}+y=0$ → [C2](#c2).

### C1 · First order: exactly one solution through this point?

[Week 3 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/3d1ae4a9-687d-4654-873d-be3439faea2f#8c746b9b-2fbf-48f4-8a2d-704a643bdcf7)

**Use this when** you get $y^{\prime}=F(t,y)$ and a starting point $(t_0,y_0)$:

$$
\dfrac{dy}{dt}=\dfrac{t}{y},\qquad y(2)=1
$$

**The rule:** check $F$ and its $y$-derivative $F_y$ near the point.

- **Both fine** (no blow-ups) → yes, **exactly one** solution through the point.
- **One breaks** → the theorem says **nothing**. That means “don’t know”, not “no”.

<details><summary>The theorem, and why $F_y$ matters (optional)</summary>

**Theorem** (Spiegel, Week 3 lecture): if $F$ and $\dfrac{\partial F}{\partial y}$ are both continuous near $(t_0,y_0)$, then exactly one solution passes through $(t_0,y_0)$.

$F_y$ says how fast the slope changes as you move up or down. If it stays finite, two solutions that start at the same point can never drift apart. For $\sqrt y$ it is infinite at $y=0$, so a curve can sit on the axis and then “peel off” at any moment (graph below).

</details>

**Steps**

1. **Write** it as $y^{\prime}=F(t,y)$: get $y^{\prime}$ alone.
2. **Differentiate** $F$ in $y$, treating $t$ like a number. That’s $F_y$.
3. **Find where it breaks:** where $F$ or $F_y$ has a $0$ in a denominator, $\ln$ of $\le0$, or $\sqrt{\ }$ of $<0$.
4. **Check the point:** away from those spots → exactly one solution. On them → no conclusion.

**Short examples:**

$$
F=t^2+3ty\quad\Longrightarrow\quad F_y=3t\quad\text{(never breaks: every point is fine)}
$$

$$
F=\dfrac ty\quad\Longrightarrow\quad F_y=-\dfrac{t}{y^2}\quad\text{(breaks at }y=0)
$$

<details><summary>Differentiate in $y$: $\;\dfrac{\partial}{\partial y}\Big(\dfrac{2t-(\ln t)\,y}{t-3}\Big)=-\dfrac{\ln t}{t-3}$</summary>

Step 1 · Treat $t$ like a number. Split the fraction: the $2t$ part has no $y$, so it gives $0$.

$$
\dfrac{2t}{t-3}-\dfrac{\ln t}{t-3}\,y\quad\Longrightarrow\quad F_y=-\dfrac{\ln t}{t-3}
$$

Step 2 · Power rule in $y$:

$$
\dfrac{\partial}{\partial y}\big(t\,y^{-1}\big)=-t\,y^{-2},\qquad \dfrac{\partial}{\partial y}\sqrt y=\dfrac{1}{2\sqrt y}
$$

</details>

**What does “no guarantee” look like?**

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
caption "At $y=0$, $F_y=1/(2\sqrt y)$ blows up, so no guarantee. And in fact many curves leave $(1,0)$. Above the axis nothing breaks, and only one curve goes through each point."
```

#### Practice: C1

**Problem: Problem 32 · W3 · Same equation, two starting points** (introductory)

For $\dfrac{dy}{dt}=\sqrt{y}$: (a) does the theorem guarantee a unique solution through $(1,4)$? (b) through $(1,0)$? For (b), check that $y=0$ and $y=\dfrac{(t-1)^2}{4}$ (for $t\ge1$) both pass through $(1,0)$ and solve the ODE.

<details><summary>Solution</summary>

1. **Type:** exactly one solution? First order → C1.
2. **Write.**

   $$F=\sqrt y$$
3. **Differentiate** in $y$.

   $$F_y=\dfrac{1}{2\sqrt y}$$
4. **Find where it breaks:** $F$ needs $y\ge0$, and $F_y$ blows up at $y=0$.

   $$y\le0$$
5. **Check the points:** (a) $(1,4)$ has $y_0=4>0$ → unique. (b) $(1,0)$ is on $y=0$ → no guarantee.
6. **Two solutions through $(1,0)$:** for $y=\frac{(t-1)^2}{4}$, $y^{\prime}=\frac{t-1}{2}=\sqrt y$ when $t\ge1$ ✓. For $y=0$: $0=\sqrt0$ ✓.

**Answer:** (a) Yes, exactly one solution through $(1,4)$. (b) No guarantee, and in fact at least two solutions pass through $(1,0)$.

</details>

**Problem: Problem 33 · W3 · Which points are guaranteed?** (introductory)

For $\dfrac{dy}{dt}=\dfrac{t}{y}$, decide whether the theorem guarantees a unique solution through (a) $(2,1)$, (b) $(0,3)$, (c) $(2,0)$.

<details><summary>Solution</summary>

1. **Type:** C1.
2. **Write.**

   $$F=\dfrac ty$$
3. **Differentiate** in $y$ (power rule).

   $$F_y=-\dfrac{t}{y^2}$$
4. **Find where it breaks:** both divide by $y$.

   $$y=0$$
5. **Check the points:** (a) $y_0=1$ and (b) $y_0=3$ are off the line. (c) $y_0=0$ is on it.

**Answer:** (a) Yes. (b) Yes. (c) No guarantee: $F$ itself is undefined at $(2,0)$.

</details>

**Problem: Problem 34 · W3 · A strip, not a point** (intermediate)

For $(t-3)\,y^{\prime}+(\ln t)\,y=2t$, $\;y(1)=2$, find the region containing the starting point where the theorem applies. Do not solve.

<details><summary>Solution</summary>

1. **Type:** C1.
2. **Write:** get $y^{\prime}$ alone.

   $$F=\dfrac{2t-(\ln t)\,y}{t-3}$$
3. **Differentiate** in $y$. Only the $y$ term survives.

   $$F_y=-\dfrac{\ln t}{t-3}$$
4. **Find where it breaks:** $\ln t$ needs $t>0$, and the denominator needs $t\neq3$. Nothing limits $y$.
5. **Check the point:** $t_0=1$ lies between $0$ and $3$.

   $$0<t<3,\quad\text{any }y$$

**Answer:** The strip $0<t<3$ (all $y$). The start $(1,2)$ is inside it, so exactly one solution passes through it.

</details>

### C2 · Second order linear: interval, zero start, two solutions

[Week 5 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/0c7a77fe-aeed-47a8-b1c3-4967d73eea21#b4f41ebe-f4f6-4d5d-816d-ceaa37811b8f)

**Use this when** it’s a second-order **linear** equation. First **write** it with $y^{\prime\prime}$ alone (same letters as [B7](#b7)):

$$
y^{\prime\prime}+p(t)\,y^{\prime}+q(t)\,y=f(t)
$$

**Short example:**

$$
t\,y^{\prime\prime}+y=0\quad\Longrightarrow\quad y^{\prime\prime}+\dfrac1t\,y=0\quad\Longrightarrow\quad p=0,\ q=\dfrac1t,\ f=0
$$

**The rule:** if $p$, $q$, $f$ don’t break on an interval around $t_0$, there’s **exactly one** solution there, for any starting values.

<details><summary>The theorem, word for word (optional)</summary>

If $p$, $q$ and $f$ are continuous on an open interval $I$ that contains $t_0$, then for **any** starting values $y(t_0)$ and $y^{\prime}(t_0)$ there is **exactly one** solution, and it works on the **whole** interval $I$.

</details>

The question is always one of three cases:

#### Case 1: what interval?

1. **Write** it with $y^{\prime\prime}$ alone. Read $p$, $q$, $f$.
2. **Find where they break** (trouble points): a $0$ in a denominator, $\ln$ of $\le0$, …
3. **Pick the piece** of the $t$-axis between trouble points that contains $t_0$. Round brackets.

**Short examples:**

$$
t\,y^{\prime\prime}+y=0:\quad q=\dfrac1t\ \text{breaks at}\ 0\quad\Longrightarrow\quad t_0=5:\ (0,\infty)
$$

$$
y^{\prime\prime}+3y^{\prime}+2y=\cos t:\quad\text{nothing breaks}\quad\Longrightarrow\quad(-\infty,\infty)
$$

#### Case 2: right side 0 and both starting values 0

Then the answer is zero, no solving:

$$
f=0,\quad y(t_0)=0,\quad y^{\prime}(t_0)=0\quad\Longrightarrow\quad y(t)\equiv0
$$

Why: $y=0$ solves it and fits both starting values, and there’s only one solution. It needs $f=0$: in $y^{\prime\prime}+y=1$, $y=0$ gives $0=1$.

#### Case 3: do y₁ and y₂ give the general solution?

Compute the **Wronskian**:

$$
W=y_1\,y_2^{\prime}-y_1^{\prime}\,y_2
$$

- $W\neq0$ → independent: $y=c_1y_1+c_2y_2$ **is** the general solution.
- $W=0$ → one is a multiple of the other: **not** enough.

**Short example:**

$$
e^{t},\ e^{2t}:\quad W=e^{t}\cdot2e^{2t}-e^{t}\cdot e^{2t}=e^{3t}\neq0
$$

That’s why the repeated root in [B5](#b5) uses $(c_1+c_2t)e^{st}$: $c_1e^{st}+c_2e^{st}$ is really one constant.

<details><summary>Why the Wronskian decides it (optional)</summary>

Fitting $c_1y_1+c_2y_2$ to $y(t_0)$ and $y^{\prime}(t_0)$ gives two equations:

$$
c_1y_1+c_2y_2=y(t_0),\qquad c_1y_1^{\prime}+c_2y_2^{\prime}=y^{\prime}(t_0)
$$

A $2\times2$ system has exactly one answer when its determinant, $y_1y_2^{\prime}-y_1^{\prime} y_2=W$, is not zero.

</details>

#### Practice: C2

**Problem: Problem 35 · W5 · Find the interval; do not solve** (intermediate)

For $(t-1)\,y^{\prime\prime}+y^{\prime}+y=\ln t$, find the largest interval on which the theorem guarantees exactly one solution for (a) $t_0=2$, (b) $t_0=\tfrac12$.

<details><summary>Solution</summary>

1. **Type:** C2, Case 1.
2. **Write:** divide by $t-1$.

   $$p=\dfrac1{t-1},\quad q=\dfrac1{t-1},\quad f=\dfrac{\ln t}{t-1}$$
3. **Find where they break:** $\ln t$ needs $t>0$, the denominator needs $t\neq1$. Pieces: $(0,1)$ and $(1,\infty)$.
4. **Pick the piece:** $t_0=2$ is in $(1,\infty)$. $t_0=\tfrac12$ is in $(0,1)$.

**Answer:** (a) $(1,\infty)$. (b) $(0,1)$.

</details>

**Problem: Problem 36 · W5 · Which pair gives the general solution?** (intermediate)

Both pairs solve $y^{\prime\prime}+4y^{\prime}+4y=0$: (a) $e^{-2t}$ and $3e^{-2t}$; (b) $e^{-2t}$ and $te^{-2t}$. Compute each Wronskian and decide which pair gives the general solution.

<details><summary>Solution</summary>

1. **Type:** C2, Case 3: compute $W=y_1y_2^{\prime}-y_1^{\prime} y_2$.
2. **Pair (a):** $y_1^{\prime}=-2e^{-2t}$, $y_2^{\prime}=-6e^{-2t}$.

   $$W=e^{-2t}(-6e^{-2t})-(-2e^{-2t})(3e^{-2t})=0$$
3. **Pair (b):** product rule, $(te^{-2t})^{\prime}=(1-2t)e^{-2t}$.

   $$W=e^{-2t}(1-2t)e^{-2t}-(-2e^{-2t})\,te^{-2t}=e^{-4t}$$
4. **Decide:** $e^{-4t}$ is never zero, so pair (b) is independent.

**Answer:** (a) $W=0$: not enough (they are multiples). (b) $W=e^{-4t}\neq0$: general solution $y=(c_1+c_2t)e^{-2t}$.

</details>

**Problem: Problem 37 · W5 + W6 · The answer without solving** (advanced)

Solve $y^{\prime\prime}+t\,y^{\prime}+e^{t}\,y=0$, $\;y(0)=0$, $\;y^{\prime}(0)=0$.

<details><summary>Solution</summary>

1. **Type:** $t$ and $e^t$ in front look impossible. But it’s linear, $f=0$, and both starting values are $0$: C2, Case 2.
2. **Write:** $p=t$, $q=e^t$, $f=0$. None of them ever breaks, so exactly one solution exists everywhere.
3. **Try $y=0$:** $0+0+0=0$ ✓, and $y(0)=0$, $y^{\prime}(0)=0$ ✓.
4. There’s only one solution, and $y=0$ works, so it is **the** solution.

**Answer:** $y(t)\equiv0$ for all $t$.

</details>

## Topic D: Circuits → ODE → solution

[Week 2 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/08d203f6-a2b5-41b9-adfd-a14e22fb03d8#77c9c878-68d6-44e3-8f1e-2f68ba18701b) [Week 5 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/0c7a77fe-aeed-47a8-b1c3-4967d73eea21#d5ad9ba9-0ec5-4b62-acf5-b1c7e17d6463)

**Use this when** a switch flips at $t=0$ and you need $v(t)$ or $i(t)$ after it.

**The move: solve for the thing that can’t jump**, $v_C$ (capacitor voltage) or $i_L$ (inductor current).

- Its **starting value** comes from the circuit **before** the switch.
- Its **ODE** comes from the circuit **after** the switch (KVL or KCL).
- Then solve the ODE with [Topic B](#topic-b). Get anything else ($i_C$, $v_R$, …) from it at the end.

**The three rules, one per element:**

| Element | Law | After a long time | At the switch |
|---|---|---|---|
| Capacitor $C$ | $i=C\dfrac{dv}{dt}$ | a **gap** | $v_C$ **can’t jump** |
| Inductor $L$ | $v=L\dfrac{di}{dt}$ | a **wire** | $i_L$ **can’t jump** |
| Resistor $R$ | $v=iR$ | — | can jump |

<details><summary>After a long time: $\;C$ = gap, $\;L$ = wire</summary>

Step 1 · Nothing changes any more, so every $\frac{d}{dt}$ is $0$.

$$
i_C=C\cdot0=0\quad\text{(gap)}
$$

$$
v_L=L\cdot0=0\quad\text{(wire)}
$$

Step 2 · Example: $12\,\mathrm{V}$ source, a resistor and a capacitor in one loop, left alone. No current flows, so the resistor has $0\,\mathrm{V}$:

$$
v_C=12\,\mathrm{V}
$$

</details>

<details><summary>At the switch: $\;v_C(0^+)=v_C(0^-)$, $\;i_L(0^+)=i_L(0^-)$</summary>

Step 1 · $0^-$ = just before, $0^+$ = just after. The value carries straight across.

$$
v_C(0^-)=12\,\mathrm{V}\quad\Longrightarrow\quad v_C(0^+)=12\,\mathrm{V}
$$

Step 2 · So for that instant a capacitor acts like a **battery** of its old voltage, and an inductor like a **current source** of its old current.

$$
C\ \to\ \text{voltage source }V_0,\qquad L\ \to\ \text{current source }I_0
$$

</details>

<details><summary>Why can’t $v_C$ and $i_L$ jump? (optional)</summary>

If $v_C$ jumped, its slope $\frac{dv}{dt}$ would be infinite at that instant. Then $i=C\frac{dv}{dt}$ would be an infinite current, and no real circuit can supply that.

Same for an inductor: a jump in $i_L$ would need an infinite voltage $v=L\frac{di}{dt}$. Another way: the stored energy, $\frac12Cv^2$ or $\frac12Li^2$, can’t change in zero time.

</details>

**Steps** (every circuit problem, D1 and D2):

1. **Before** ($t<0$): the old circuit, sitting for a long time. $C$ = gap, $L$ = wire. Find $v_C(0^-)$ or $i_L(0^-)$.
2. **Carry across** to $t=0^+$: $v_C(0^+)=v_C(0^-)$, $i_L(0^+)=i_L(0^-)$. Need another value at $0^+$? Redraw the **new** circuit with $C$ as a battery (or $L$ as a current source) and use KVL/KCL.
3. **After** ($t>0$): in the new circuit, find what you need: the final value and $\tau$ ([D1](#d1)), or $\alpha$ and $\omega_0$ ([D2](#d2)).
4. **Plug in** to the formula ([D1](#d1)), or **pick** the case and **plug in** the starting values ([D2](#d2)).
5. **Check** $t\to\infty$: $C$ = gap, $L$ = wire again. Your answer must head there.

**Short example:** a $V_s$, $R$, $C$ loop. KVL after the switch, with $i=C\frac{dv_C}{dt}$:

$$
V_s=Ri+v_C\quad\Longrightarrow\quad RC\,\dfrac{dv_C}{dt}+v_C=V_s
$$

One $C$ or one $L$ → first order → [D1](#d1). An $L$ **and** a $C$ → second order → [D2](#d2).

**What does “can’t jump” look like?**

```graph
title "A capacitor charging from $0\,\mathrm{V}$: its voltage doesn’t jump, its current does"
x -1 5 label="$t/\tau$"
y -0.2 1.2 label="scaled so the biggest value is 1"
curve "if(x<0, 0, 1-exp(-x))" label="$v_C$: starts at 0, no jump" color=1
curve "if(x<0, 0, exp(-x))" label="$i_C$: 0 before, jumps at $t=0$" color=2
vline "0" label="switch closes" color=0
caption "Pre-tutorial 2 (a problem in D1). Just after the switch, $v_C$ is still 0, so all of the source current goes into the capacitor. $i_C$ jumps; $v_C$ doesn’t."
```

> **Warning:** **Before and after are two different circuits.** Draw both. The old one is only for the starting value. Write the ODE from the new one, with only the parts still connected.

> **Warning:** **The sign comes from the drawn arrow.** Find which way the current really flows, then compare with the arrow. Opposite? The value is **negative**. Example: $3\,\mathrm{A}$ really flows down, the $i_L$ arrow points up → $i_L(0)=-3\,\mathrm{A}$.

### D1 · One C or one L: first order

[Week 1 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/1cbac07a-cd02-48c2-8c30-c9829c4e06b2#ab5bf400-4411-4869-8d74-7790f8ee6f2c) [Week 2 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/08d203f6-a2b5-41b9-adfd-a14e22fb03d8#77c9c878-68d6-44e3-8f1e-2f68ba18701b) [Week 3 · Topic 2](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/3d1ae4a9-687d-4654-873d-be3439faea2f#a43fc96e-8dc5-4a1e-bfdf-bf1acf01f98b)

**Use this when**, after the switch, only **one** capacitor or **one** inductor is left (after combining), plus resistors and DC sources.

Call $x$ the thing that can’t jump: $v_C$ in an RC circuit, $i_L$ in an RL circuit.

**The move: you don’t need to solve the ODE.** Find three numbers and plug them in:

$$
x(t)=x_f+\big(x_0-x_f\big)\,e^{-t/\tau}
$$

- $x_0$ = the **starting value** (from the old circuit)
- $x_f$ = the **final value**, long after the switch (from the new circuit). $0$ if no source is left.
- $\tau$ = the **time constant** in seconds: $\;\tau=R_{th}C\;$ or $\;\tau=\dfrac{L}{R_{th}}$

$R_{th}$ = the resistance the $C$ or $L$ “sees” in the new circuit: turn the sources off (a voltage source → a wire, a current source → a gap), then combine the resistors.

**Short example:**

$$
x_0=0,\quad x_f=10,\quad \tau=0.2\quad\Longrightarrow\quad x(t)=10-10e^{-5t}
$$

<details><summary>Where does the formula come from? (optional)</summary>

KVL or KCL after the switch always gives this [B2](#b2) equation, with $p=\frac1\tau$ and $f=\frac{x_f}{\tau}$:

$$
\dfrac{dx}{dt}+\dfrac{x}{\tau}=\dfrac{x_f}{\tau}
$$

Solve it once with $x(0)=x_0$ and you get the formula. Check: at $t=0$, $e^0=1$, so $x=x_0$ ✓. As $t\to\infty$, $e^{-t/\tau}\to0$, so $x\to x_f$ ✓.

Example (the lecture’s RC step response): $I_s$, $R$, $C$ in parallel. KCL: $C\frac{dv}{dt}+\frac vR=I_s$, so $\tau=RC$ and $x_f=RI_s$.

Why the sources go off for $R_{th}$: they only set $x_f$ (the right side). The speed $\tau$ comes from the left side: just the resistors and the $C$ or $L$.

</details>

**Steps**

1. **Before:** old circuit, long time ($C$ = gap, $L$ = wire). Find $x(0^-)$.
2. **Carry across:** $x_0=x(0^+)=x(0^-)$.
3. **After:** new circuit. Final value $x_f$ (long time again). Time constant: $R_{th}$, then $\tau=R_{th}C$ or $L/R_{th}$.
4. **Plug in:** $x(t)=x_f+(x_0-x_f)e^{-t/\tau}$.
5. **Check:** $x(0)=x_0$ and $x(\infty)=x_f$. Anything else comes from $x(t)$: $i_C=C\frac{dv_C}{dt}$, $v_L=L\frac{di_L}{dt}$, Ohm’s law.

#### Case 1: natural response (no source left)

The stored energy drains away through the resistors, so $x_f=0$:

$$
x(t)=x_0\,e^{-t/\tau}
$$

**Short example:** $i_L$ starts at $4\,\mathrm{A}$, $L=8\,\mathrm{mH}$, $R=4\,\Omega$:

$$
\tau=\dfrac{8\times10^{-3}}{4}=2\,\mathrm{ms}\quad\Longrightarrow\quad i(t)=4e^{-500t}\,\mathrm{A}
$$

#### Case 2: step response (a source stays on)

The source pushes $x$ to a new value $x_f$:

$$
x(t)=x_f+\big(x_0-x_f\big)\,e^{-t/\tau}
$$

**Short example:** $i$ starts at $0$, ends at $10\,\mathrm{A}$, $\tau=0.2\,\mathrm{s}$:

$$
i(t)=10+(0-10)e^{-5t}=10\big(1-e^{-5t}\big)\,\mathrm{A}
$$

#### Examples and handy facts

**Lecture example (§1.1).** The switch closes at $t=0$. The inductor carries no current before that. Find $i(t)$ for $t\ge0$.

```schematic
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$10\,\Omega$" i="$i$"
L1 6,3 -> 6,0 "$2\,\mathrm{H}$" v="$v$"
wire 6,0 -> 0,0
ground 0,0
```

<details><summary>Full solution: the lecture’s RL step response</summary>

Step 1 · **Before:** the switch is open, so no current flows.

$$
i(0^-)=0
$$

Step 2 · **Carry across:** an inductor current can’t jump.

$$
x_0=i(0^+)=0
$$

Step 3 · **After** (final value): long after, $L$ is a wire, so only the $10\,\Omega$ limits the current.

$$
x_f=\dfrac{100}{10}=10\,\mathrm{A}
$$

Step 4 · **After** (time constant): the source is off, so $L$ sees just the $10\,\Omega$.

$$
\tau=\dfrac{L}{R}=\dfrac{2}{10}=0.2\,\mathrm{s}
$$

Step 5 · **Plug in.**

$$
i(t)=10+(0-10)e^{-t/0.2}=10-10e^{-5t}
$$

Step 6 · **Check** with the ODE (KVL: $100=10i+2\frac{di}{dt}$). Divide by $2$: it’s $i^{\prime}+5i=50$, the [B2](#b2) practice problem. Same answer.

$$
\dfrac{di}{dt}+5i=50
$$

**Answer:**

$$
i(t)=10\big(1-e^{-5t}\big)\,\mathrm{A}
$$

</details>

**Handy facts.** Open a card for an example:

<details><summary>How fast it settles: after $1\tau$ 37% of the gap is left, after $5\tau$ it’s done</summary>

Step 1 · $e^{-1}\approx0.37$, $e^{-2}\approx0.135$, $e^{-5}<0.01$.

$$
x(\tau)=x_f+0.37\,(x_0-x_f)
$$

Step 2 · Example: $\tau=2\,\mathrm{ms}$.

$$
5\tau=10\,\mathrm{ms}\quad\text{(settled)}
$$

</details>

<details><summary>Derivative: $\;\dfrac{d}{dt}e^{-t/\tau}=-\dfrac1\tau\,e^{-t/\tau}$</summary>

Step 1 · For $i_C=C\frac{dv}{dt}$ or $v_L=L\frac{di}{dt}$. Example: $i=10-10e^{-5t}$, $L=2\,\mathrm{H}$:

$$
v_L=2\cdot50e^{-5t}=100e^{-5t}\,\mathrm{V}
$$

</details>

<details><summary>Energy stored: $\;w_C=\tfrac12Cv^2$, $\;w_L=\tfrac12Li^2$</summary>

Step 1 · In joules. The sign of $i$ doesn’t matter (it’s squared). Example: $L=8\,\mathrm{mH}$, $i=12.5\,\mathrm{A}$:

$$
w=\tfrac12(8\times10^{-3})(12.5)^2=0.625\,\mathrm{J}
$$

</details>

<details><summary>Parallel resistors: $\;R_1\parallel R_2=\dfrac{R_1R_2}{R_1+R_2}$</summary>

Step 1 · For $R_{th}$. Example:

$$
6\parallel3=\dfrac{18}{9}=2\,\Omega
$$

</details>

**What does the formula look like?**

```graph
title "Drag the sliders: the curve always heads for $x_f$"
x 0 8 label="$t$"
y -12 12 label="$x$"
slider x0 -10 10 10 step=1 label="$x_0$"
slider xf -10 10 2 step=1 label="$x_f$"
slider tau 0.2 3 1 step=0.1 label="$\tau$"
curve "xf+(x0-xf)*exp(-x/tau)" label="$x(t)=x_f+(x_0-x_f)e^{-t/\tau}$" color=1
hline "xf" label="$x_f$" color=3
point "tau" "xf+(x0-xf)*exp(-1)" label="at $t=\tau$: 37% of the gap left" color=2
caption "Set $x_f=0$ for a natural response. A bigger $\tau$ (bigger $RC$ or $L/R$) means a slower circuit."
```

#### Practice: D1

**Problem: Problem 38 · W1 · RL natural response · Pre-tutorial 1** (introductory)

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

**Problem: Problem 39 · W2 · Can the capacitor current jump? · Pre-tutorial 2** (introductory)

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
3. **Carry across:** $v(0^+)=v(0^-)=0$, since it can’t jump. The resistor sits across the capacitor, so its current is $v/R=0$.
4. **KCL** at the top node: the resistor takes nothing, so all of the source current goes into the capacitor.

   $$i_C(0^+)=I_s-\dfrac{v(0^+)}{R}=2-0=2\,\mathrm{A}$$
5. **Check:** $v$ rises toward $RI_s=2000\,\mathrm{V}$ and $i_C$ dies down to 0.

**Answer:** $i_C(0^-)=0$, $i_C(0^+)=2\,\mathrm{A}$. So yes, the capacitor **current** jumps. The capacitor **voltage** doesn’t: it stays at 0.

</details>

**Problem: Problem 40 · W2–W3 · Read the circuit from its response · textbook P7.42** (intermediate)

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
2. **Carry across:** put $t=0$ into $i(t)$: $I_0=10-10=0$.
3. **Carry across:** $i=0$, so the resistor has 0 V across it. The whole source voltage sits on $L$.

   $$V_s=v(0^+)=200\,\mathrm{V}$$
4. **After** (final value): long after, $L$ is a wire, so $i_f=V_s/R$. From $i(t)$, $i_f=10$.

   $$10=\dfrac{200}{R}\quad\Rightarrow\quad R=20\,\Omega$$
5. **After** (time constant): the exponent is $-500t$, so $\frac1\tau=500$ and $\tau=2\,\mathrm{ms}$. Use $\tau=L/R$.

   $$L=20\times0.002=40\,\mathrm{mH}$$
6. **Check:** $L\frac{di}{dt}=0.04\times5000e^{-500t}=200e^{-500t}$, which matches $v(t)$ ✓.

**Answer:** $V_s=200\,\mathrm{V}$, $R=20\,\Omega$, $I_0=0$, $L=40\,\mathrm{mH}$.

</details>

**Problem: Problem 41 · W2 · RC natural response with a divider first · textbook P7.22** (intermediate)

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

**Problem: Problem 42 · W1–W2 · The sign of the reference arrow · textbook P7.1** (intermediate)

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

**Problem: Problem 43 · W2 · Step response that needs a Thévenin equivalent · textbook P7.52(a)** (advanced)

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

### D2 · An L and a C: RLC circuits (second order)

[Week 5 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/0c7a77fe-aeed-47a8-b1c3-4967d73eea21#d5ad9ba9-0ec5-4b62-acf5-b1c7e17d6463)

**Use this when**, after the switch, there’s an inductor **and** a capacitor (combine series/parallel ones first, so you have one of each).

**The move: it’s [B5](#b5) with circuit names.** Same quadratic, same three cases. Write the quadratic as:

$$
s^2+2\alpha s+\omega_0^2=0
$$

- $\alpha$ (“alpha”) = the **damping**: how fast it dies out
- $\omega_0$ (“omega-zero”) = the **natural frequency**: how fast it would swing with no $R$
- Both come straight from $R$, $L$, $C$ (below), so you never have to derive the ODE on the exam.

A source still on after the switch? Then add the final value $V_f$ on top, like $y_p$ in [B6](#b6):

$$
v(t)=V_f+(\text{the B5 form})
$$

#### Series or parallel: α and ω₀

```schematic
V1 0,3 -> 0,0 "$V_s$"
R1 0,3 -> 3,3 "$R$" i="$i$"
L1 3,3 -> 6,3 "$L$"
C1 6,3 -> 6,0 "$C$" v="$v_C$"
wire 6,0 -> 0,0
ground 0,0
```

**Series** (solve for $v_C$):

$$
\begin{gathered}\alpha=\dfrac{R}{2L}, \\ \omega_0=\dfrac{1}{\sqrt{LC}}\end{gathered}
$$

**Short example:** $R=4\,\Omega$, $L=1\,\mathrm{H}$, $C=0.25\,\mathrm{F}$:

$$
\begin{gathered}\alpha=\dfrac{4}{2}=2, \\ \omega_0=\dfrac{1}{\sqrt{0.25}}=2\end{gathered}
$$

```schematic
C1 0,3 -> 0,0 "$C$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$L$" i="$i_L$"
wire 3,3 -> 6,3
R1 6,3 -> 6,0 "$R$" i="$i_R$"
wire 6,0 -> 0,0
ground 0,0
```

**Parallel** (solve for the shared $v$). Only $\alpha$ changes:

$$
\begin{gathered}\alpha=\dfrac{1}{2RC}, \\ \omega_0=\dfrac{1}{\sqrt{LC}}\end{gathered}
$$

**Short example:** $R=800\,\Omega$, $C=50\,\mathrm{nF}$:

$$
\alpha=\dfrac{1}{2(800)(50\times10^{-9})}=12500\,\mathrm{s^{-1}}
$$

<details><summary>Where do the equations come from? (optional)</summary>

**Series:** KVL around the loop, $V_s=Ri+Li^{\prime}+v_C$, with $i=Cv_C^{\prime}$. Divide by $LC$:

$$
v_C^{\prime\prime}+\dfrac RL\,v_C^{\prime}+\dfrac1{LC}\,v_C=\dfrac{V_s}{LC}
$$

Match with $s^2+2\alpha s+\omega_0^2$: $2\alpha=\frac RL$ and $\omega_0^2=\frac1{LC}$.

**Parallel:** KCL at the top node, $Cv^{\prime}+i_L+\frac vR=0$. Differentiate once, use $i_L^{\prime}=\frac vL$, divide by $C$:

$$
v^{\prime\prime}+\dfrac{1}{RC}\,v^{\prime}+\dfrac{1}{LC}\,v=0
$$

So $2\alpha=\frac{1}{RC}$. A big parallel $R$ takes almost no current, so it barely drains energy: less damping.

</details>

#### The three cases (same as B5)

Compare $\alpha$ with $\omega_0$. The roots are:

$$
s=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}
$$

| Compare | Name | B5 case | Form |
|---|---|---|---|
| $\alpha>\omega_0$ | **overdamped** | Case 1 | $c_1e^{s_1t}+c_2e^{s_2t}$ |
| $\alpha=\omega_0$ | **critically damped** | Case 2 | $(c_1+c_2t)e^{-\alpha t}$ |
| $\alpha<\omega_0$ | **underdamped** | Case 3 | $e^{-\alpha t}(c_1\cos\omega_dt+c_2\sin\omega_dt)$ |

Underdamped swings at $\omega_d$ (the B5 $\omega$; and $\sigma=-\alpha$):

$$
\omega_d=\sqrt{\omega_0^2-\alpha^2}
$$

**Short examples:**

$$
\alpha=5,\ \omega_0=3\quad\Longrightarrow\quad s=-5\pm4=-1,\,-9\quad\text{(overdamped)}
$$

$$
\alpha=50,\ \omega_0=50\quad\Longrightarrow\quad (c_1+c_2t)e^{-50t}\quad\text{(critical)}
$$

$$
\alpha=3,\ \omega_0=5\quad\Longrightarrow\quad \omega_d=4,\ \ e^{-3t}(c_1\cos4t+c_2\sin4t)
$$

No $R$ at all ($\alpha=0$, an ideal LC): $\;c_1\cos\omega_0t+c_2\sin\omega_0t$, swinging forever.

**What do the three cases look like?**

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
caption "$\omega_0=2$ never changes; only $\alpha=R/2$ moves. $R<4$: underdamped, it swings below zero before settling. $R=4$: critically damped, fastest with no overshoot. $R>4$: overdamped, a slow creep back."
```

#### Steps: the two starting values

Second order needs **two** starting values: $v(0)$ and the slope $v^{\prime}(0)$. The value carries across. The slope comes from the capacitor current:

$$
v_C^{\prime}(0^+)=\dfrac{i_C(0^+)}{C}
$$

1. **Before:** old circuit, long time ($C$ = gap, $L$ = wire). Find $v_C(0^-)$ and $i_L(0^-)$.
2. **Carry across:** $v_C(0^+)=v_C(0^-)$, $i_L(0^+)=i_L(0^-)$. Then find $i_C(0^+)$ and the slope (cards below).
3. **After:** series or parallel? Compute $\alpha$, $\omega_0$. Final value $V_f$: $0$ if no source is left, else the new DC state.
4. **Pick** the case (compare $\alpha$, $\omega_0$) and write $v=V_f+$ the form.
5. **Plug in** $t=0$: the value gives $c_1$, the slope (product rule) gives $c_2$. Use the **whole** answer, $V_f$ included.
6. **Check:** $t\to\infty$ gives $V_f$.

<details><summary>Slope in a series circuit: $\;i_C=$ the loop current $=i_L$</summary>

Step 1 · The loop current is the inductor current, so it carries across. Sign: $+$ if the arrow enters the $+$ end of $C$.

$$
v_C^{\prime}(0^+)=\dfrac{i_L(0^+)}{C}
$$

Step 2 · Example: $i(0^-)=0$.

$$
v_C^{\prime}(0^+)=0
$$

</details>

<details><summary>Slope in a parallel circuit: KCL, $\;i_C=-(i_L+i_R)$</summary>

Step 1 · All three arrows point down, so the currents add to $0$. $i_R=\frac{v(0^+)}{R}$.

$$
i_C(0^+)=-\big(i_L(0^+)+i_R(0^+)\big)
$$

Step 2 · Example: $v=10\,\mathrm{V}$, $R=5\,\Omega$, $i_L=1\,\mathrm{A}$, $C=0.5\,\mathrm{F}$.

$$
i_C=-(1+2)=-3\,\mathrm{A}
$$

$$
v^{\prime}(0^+)=\dfrac{-3}{0.5}=-6\,\mathrm{V/s}
$$

</details>

<details><summary>Solving for $i$ in a series circuit: $\;i^{\prime}(0^+)=\dfrac{v_L(0^+)}{L}$</summary>

Step 1 · $i(0^+)=i_L(0^-)$. For the slope, KVL around the new loop gives $v_L$.

$$
v_L(0^+)=v_C(0^+)-R\,i(0^+)
$$

Step 2 · Example: $v_C=70\,\mathrm{V}$, $i=0$, $L=0.1\,\mathrm{H}$.

$$
i^{\prime}(0^+)=\dfrac{70}{0.1}=700\,\mathrm{A/s}
$$

</details>

> **Warning:** **Fit the constants to the whole answer, $V_f$ included.** $v_C=100+(c_1+c_2t)e^{-50t}$ with $v_C(0)=200$: $\;100+c_1=200$, so $c_1=100$, not $200$.

> **Warning:** **Units first.** $1\,\mathrm{mH}=10^{-3}\,\mathrm{H}$, $1\,\mu\mathrm{F}=10^{-6}\,\mathrm{F}$, $1\,\mathrm{nF}=10^{-9}\,\mathrm{F}$. Example: $L=250\,\mathrm{mH}$, $C=10\,\mathrm{nF}$ → $\omega_0=\dfrac{1}{\sqrt{0.25\times10^{-8}}}=20000$.

**Textbook example (P8.53).** The circuit has been running for a long time with $V_s=200\,\mathrm{V}$. At $t=0$ the source drops to $100\,\mathrm{V}$. Find $v_C(t)$ for $t\ge0$.

```schematic
V1 0,3 -> 0,0 "$200\to100\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$" i="$i$"
L1 3,3 -> 6,3 "$40\,\mathrm{mH}$"
C1 6,3 -> 6,0 "$10\,\mathrm{mF}$" v="$v_C$"
wire 6,0 -> 0,0
ground 0,0
```

<details><summary>Full solution: a series step response</summary>

Step 1 · **Before:** long time, so $C$ is a gap and $i=0$. With no current, $R$ and $L$ drop nothing, so $C$ holds the whole $200\,\mathrm{V}$.

$$
v_C(0^-)=200\,\mathrm{V},\qquad i(0^-)=0
$$

Step 2 · **Carry across:** neither can jump. The slope is $i/C$, and $i=0$.

$$
v_C(0^+)=200
$$

$$
v_C^{\prime}(0^+)=\dfrac{0}{0.01}=0
$$

Step 3 · **After:** series, so $\alpha=\frac{R}{2L}$. Long after, $C$ is a gap again and holds the new source.

$$
\alpha=\dfrac{4}{2(0.04)}=50,\qquad \omega_0=\dfrac{1}{\sqrt{0.04\times0.01}}=50
$$

$$
V_f=100\,\mathrm{V}
$$

Step 4 · **Pick:** $\alpha=\omega_0$, critically damped (B5 Case 2). Add $V_f$.

$$
v_C=100+(c_1+c_2t)\,e^{-50t}
$$

Step 5 · Differentiate (product rule).

$$
v_C^{\prime}=c_2e^{-50t}-50(c_1+c_2t)e^{-50t}
$$

Step 6 · **Plug in** $t=0$.

$$
100+c_1=200\quad\Rightarrow\quad c_1=100
$$

$$
c_2-50c_1=0\quad\Rightarrow\quad c_2=5000
$$

Step 7 · **Check:** $t\to\infty$ gives $100\,\mathrm{V}$ ✓.

**Answer:**

$$
v_C=100+(100+5000t)\,e^{-50t}\,\mathrm{V}
$$

</details>

#### Practice: D2

**Problem: Problem 44 · W5 · No resistor: an ideal LC circuit · textbook P8.14** (introductory)

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
2. **Pick:** $\omega_0=\sqrt{10}$. The cosine coefficient is $v(0)=0$, so only the sine is left.

   $$v=c_2\sin(\sqrt{10}\,t)$$
3. **Carry across** (slope): KCL at the top node: $i_C+i_L=0$, so $i_C(0^+)=+3\,\mathrm{A}$ (down). Divide by $C$.

   $$v'(0^+)=\dfrac{3}{0.25}=12\,\mathrm{V/s}$$
4. **Plug in:** the slope of $c_2\sin(\sqrt{10}\,t)$ at $0$ is $\sqrt{10}\,c_2$. Set it equal to 12.

   $$c_2=\dfrac{12}{\sqrt{10}}\approx3.795$$

**Answer:** (a) $v=\dfrac{12}{\sqrt{10}}\sin(\sqrt{10}\,t)\,\mathrm{V}$. (b) $\omega_0=\sqrt{10}\approx3.162\,\mathrm{rad/s}$. (c) $3.795\,\mathrm{V}$. With no $R$, nothing uses up the energy, so it never dies out.

</details>

**Problem: Problem 45 · W5 · Read the circuit back from its response · textbook P8.3** (introductory)

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

**Problem: Problem 46 · W5 · Switch to a series loop · textbook P8.44** (intermediate)

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
3. **Carry across** (slope): KVL around the new loop is $v_C=Ri+L\,i^{\prime}$. At $0^+$, $v_C=70$ and $i=0$.

   $$i'(0^+)=\dfrac{70-200(0)}{0.1}=700\,\mathrm{A/s}$$
4. **After:** $\alpha=\dfrac{R}{2L}=\dfrac{200}{2(0.1)}=1000$ and $\omega_0^2=\dfrac{1}{LC}=\dfrac{1}{0.1\times200\times10^{-9}}=5\times10^7$. $\alpha^2=10^6$ is smaller, so underdamped.

   $$\omega_d=\sqrt{5\times10^7-10^6}=7000\,\mathrm{rad/s}$$
5. **Pick:** the cosine coefficient is $i(0)=0$, so only the sine is left.

   $$i=c_2\,e^{-1000t}\sin7000t$$
6. **Plug in:** the slope of this at $t=0$ is $7000c_2$. Set it equal to 700.

   $$c_2=0.1$$

**Answer:** $i=0.1\,e^{-1000t}\sin7000t\ \mathrm{A}$ $=100\,e^{-1000t}\sin7000t\ \mathrm{mA}$, $t\ge0$.

</details>

**Problem: Problem 47 · W5 · The slope comes from KCL · textbook P8.7** (intermediate)

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
2. **Carry across** (slope): first the resistor current, $i_R=\dfrac{90}{12500/3}=21.6\,\mathrm{mA}$. KCL at the top node (all arrows down): $i_C+i_L+i_R=0$, so $i_C=-(-30)-21.6$.

   $$i_C(0^+)=30-21.6=8.4\,\mathrm{mA}$$
3. Divide by $C$ to get the slope.

   $$v'(0^+)=\dfrac{8.4\times10^{-3}}{10^{-8}}=8.4\times10^5\,\mathrm{V/s}$$
4. **After:** $\alpha=\dfrac{1}{2RC}=12000$ and $\omega_0=\dfrac{1}{\sqrt{LC}}=20000$. $\alpha<\omega_0$, so underdamped.

   $$\omega_d=\sqrt{20000^2-12000^2}=16000$$
5. **Pick:** the cosine coefficient is $v(0)=90$.

   $$v=e^{-12000t}(90\cos16000t+c_2\sin16000t)$$
6. **Plug in:** the slope at $0$ is $-\alpha(90)+\omega_dc_2$ (the $y^{\prime}(0)$ column of the B5 table). Set it equal to $8.4\times10^5$.

   $$-12000(90)+16000c_2=840000\ \Rightarrow\ c_2=120$$

**Answer:** $v=e^{-12000t}(90\cos16000t+120\sin16000t)\,\mathrm{V}$, $t\ge0$.

</details>

**Problem: Problem 48 · W5 · Choose R for critical damping · textbook P8.42** (advanced)

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
4. **(c) Pick:** critically damped, so one repeated root $s=-\alpha=-5000$.

   $$i=(c_1+c_2t)e^{-5000t}$$
5. **Plug in:** $c_1=i(0)=0.024$. The slope at $0$ is $c_2-5000c_1$; set it equal to 120.

   $$c_2=240$$
6. For $v_C$, use the same KVL: $v_C=Ri+L\,i^{\prime}$. (Check: $i=-C\,v_C^{\prime}$, with a minus because $i$ leaves the $+$ of $C$.)

   $$v_C=(90+3\times10^5\,t)e^{-5000t}$$

**Answer:** (a) $R=2500\,\Omega$. (b) $i(0^+)=24\,\mathrm{mA}$, $i^{\prime}(0^+)=120\,\mathrm{A/s}$. (c) $i=(0.024+240t)e^{-5000t}\,\mathrm{A}$, $v_C=(90+3\times10^5t)e^{-5000t}\,\mathrm{V}$.

</details>

**Problem: Problem 49 · W5 + W6 · The answer is zero · textbook P8.24** (advanced)

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
3. **Carry across** (slope): at $0^+$, $v_o=0$, so the $400\,\Omega$ still carries $30\,\mathrm{mA}$. $L$ still takes all 30 mA (it can’t jump). KCL at the top node leaves nothing for $C$.

   $$i_C(0^+)=30-30=0\ \Rightarrow\ v_o^{\prime}(0^+)=0$$
4. **After:** KCL at the top node is $\dfrac{v_o-12}{400}+i_L+Cv_o^{\prime}=0$. Differentiate once: the constant 12 disappears, so the right side is $0$.

   $$Cv_o''+\dfrac{v_o'}{400}+\dfrac{v_o}{L}=0$$
5. **Plug in:** right side $0$, $v_o(0)=0$ and $v_o^{\prime}(0)=0$. The only solution that fits is $v_o=0$ (the zero-start rule in [Topic C](#topic-c)).

**Answer:** $v_o(t)=0$ for all $t\ge0$. The inductor already carries the whole source current, so nothing ever flows into the capacitor.

</details>

## Topic E: Practice midterm

**The professor’s advice:** “Study all the examples in the lectures and posted materials, and those in the tutorials, and you will be fine. The examples will be a good guide to the problems on the Midterm.”

So this set is built from those examples, some copied, some with new numbers or a twist. **Every solution uses exactly the steps of its section**, word for word, so you practise the way you learned it.

**How to use it:**

1. Close the rest of the note. Do a whole problem on paper before you open its solution.
2. Start every answer with the **type** (which section) and the clue that told you.
3. Stuck or wrong? Each answer ends with the section to review.

**The midterm question is always one of these.** Spot the clue, run the steps:

| You see… | Go to | First move |
|---|---|---|
| a complex number to divide, convert, power, root | [A](#topic-a) | go polar |
| $y^{\prime}=$ ($t$-part)($y$-part) | [B1](#b1) | separate |
| $y^{\prime}+p(t)\,y=f(t)$ | [B2](#b2) | $\mu=e^{\int p\,dt}$ |
| $M\,dt+N\,dy=0$ | [B3](#b3) / [B4](#b4) | test $M_y=N_t$ |
| $ay^{\prime\prime}+by^{\prime}+cy=0$ | [B5](#b5) | the quadratic |
| $ay^{\prime\prime}+by^{\prime}+cy=f(t)$ | [B6](#b6) | $y_c$, then guess $y_p$ |
| $t$ in front, $y_1$ given | [B7](#b7) | $y=y_1v$ |
| “exactly one solution?”, “interval?” | [C](#topic-c) | find where it breaks |
| a circuit with a switch | [D](#topic-d) | Before → Carry across → After |

**Redo the full-example cards too, solutions closed:** B1 (lecture 3.3), B2 (lecture 3.1), B3 (lecture 4.1), B4 (Pre-tutorial 4), B6 (the tutorial problem), B7 (the lecture example), D1 (the lecture RL circuit), D2 (P8.53).

**Problem: E1 · W1 · Divide, convert, take roots · like lecture Examples 1.1 and 1.2** (introductory)

(a) Write $z=\dfrac{10+j5}{2-j}$ in rectangular form. (b) Write $z$ in polar form. (c) Find all three cube roots of $8j$, in polar and in rectangular form.

<details><summary>Solution</summary>

1. (a) **Type:** dividing in rectangular → Topic A, Case 2. Multiply top and bottom by the conjugate of the bottom, $2+j$.

   $$z=\dfrac{(10+j5)(2+j)}{(2-j)(2+j)}$$
2. Multiply out. $j^2=-1$, so $5j^2=-5$. The bottom is $2^2+1^2$.

   $$\begin{gathered}(10+j5)(2+j)=20+j10+j10+5j^2=15+j20 \\ (2-j)(2+j)=5\end{gathered}$$
3. Divide each part by $5$.

   $$z=3+j4$$
4. (b) **Type:** Case 1, rectangular → polar. $a=3>0$, so no $180^\circ$ fix.

   $$\begin{gathered}c=\sqrt{3^2+4^2}=5 \\ \theta=\tan^{-1}\tfrac43=53.13^\circ\end{gathered}$$
5. (c) **Type:** Case 3, roots with $k=3$. Go polar first: $8j$ points straight up.

   $$8j=8\angle90^\circ$$
6. **Length:** the cube root of $8$.

   $$8^{1/3}=2$$
7. **First angle**, then **spacing** $360^\circ/3$.

   $$\begin{gathered}\dfrac{90^\circ}{3}=30^\circ \\ 30^\circ,\quad 150^\circ,\quad 270^\circ\end{gathered}$$
8. Convert each to rectangular (Case 1): $a=2\cos\theta$, $b=2\sin\theta$.

   $$\begin{gathered}2\angle30^\circ=\sqrt3+j \\ 2\angle150^\circ=-\sqrt3+j \\ 2\angle270^\circ=-j2\end{gathered}$$

**Answer:** (a) $3+j4$. (b) $5\angle53.13^\circ$. (c) $2\angle30^\circ=\sqrt3+j$, $\;2\angle150^\circ=-\sqrt3+j$, $\;2\angle270^\circ=-j2$. Review: [Topic A](#topic-a).

</details>

**Problem: E2 · W2 · Classify, then use linearity** (introductory)

For each equation, give the order and say whether it is linear, homogeneous, constant-coefficient and autonomous.

(a) $\dfrac{d^2i}{dt^2}+\dfrac{R}{L}\dfrac{di}{dt}+\dfrac{1}{LC}\,i=0$ (the series RLC circuit of the Week 2 notes)

(b) $y^{\prime}=y^2+t$

(c) $y^{\prime\prime}+y=6\cos^2t$

(d) $y=e^{-t}$ solves $y^{\prime}+2y=e^{-t}$. Without solving, give a solution of $y^{\prime}+2y=5e^{-t}$.

<details><summary>Solution</summary>

1. **Type:** classification → the five questions at the start of Topic B.
2. (a) **Order:** $i^{\prime\prime}$, so 2nd. **Linear:** $i$ only to the power 1. **Homogeneous:** right side $0$. **Constant coefficients:** $\frac RL$, $\frac1{LC}$ are numbers. **Autonomous:** no $t$ anywhere.
3. (b) **Order** 1. $y^2$ is not power 1, so **nonlinear**. The $t$ means **not** autonomous.
4. (c) **Order** 2, linear, numbers in front. Right side $\neq0$: **not** homogeneous. $\cos^2t$ has $t$: not autonomous.
5. (d) **Linearity:** multiply $y$ by $5$ and the whole left side is multiplied by $5$. Check:

   $$(5e^{-t})^{\prime}+2(5e^{-t})=-5e^{-t}+10e^{-t}=5e^{-t}\ \checkmark$$

**Answer:** (a) 2nd order, linear, homogeneous, constant-coefficient, autonomous. (b) 1st order, nonlinear, not autonomous. (c) 2nd order, linear, not homogeneous, constant-coefficient, not autonomous. (d) $y=5e^{-t}$. Review: [Topic B](#topic-b).

</details>

**Problem: E3 · W3–W4 · Name the type, then solve · like lecture Examples 3.3, 3.1 and 4.1** (intermediate)

Name the type of each equation, then solve it.

(a) $\dfrac{dy}{dt}=\dfrac{2t+2ty^2}{y+t^2y}$, $\;y(0)=1$

(b) $\dfrac{dy}{dt}+\dfrac{6y}{3t+2}=4$, $\;y(0)=0$

(c) $(2t+y\cos t)\,dt+(\sin t+2y)\,dy=0$, $\;y(0)=1$

<details><summary>Solution</summary>

1. (a) **Type:** factor top and bottom → a $t$-part times a $y$-part → B1. **Write:**

   $$\dfrac{dy}{dt}=\dfrac{2t}{1+t^2}\cdot\dfrac{1+y^2}{y}$$
2. **Separate.**

   $$\dfrac{y}{1+y^2}\,dy=\dfrac{2t}{1+t^2}\,dt$$
3. **Integrate:** both are “top = derivative of bottom” (the left one is half).

   $$\tfrac12\ln(1+y^2)=\ln(1+t^2)+C$$
4. **Solve for $y$:** multiply by $2$, raise $e$ to both sides ($e^{2C}$ is a new $C$).

   $$1+y^2=C\,(1+t^2)^2$$
5. **Plug in** $y(0)=1$, then take the $+$ root ($y(0)>0$).

   $$\begin{gathered}1+1=C\cdot1\quad\Rightarrow\quad C=2 \\ y=\sqrt{2(1+t^2)^2-1}\end{gathered}$$
6. (b) **Type:** linear → B2. **Write:** $y^{\prime}$ is alone.

   $$p=\dfrac{6}{3t+2},\qquad f=4$$
7. **Find $\mu$:** $\int\frac{6}{3t+2}dt=2\ln(3t+2)$, and $e$, $\ln$ cancel.

   $$\mu=(3t+2)^2$$
8. **Multiply.**

   $$\big[(3t+2)^2y\big]^{\prime}=4(3t+2)^2$$
9. **Integrate** with $u=3t+2$, $du=3\,dt$.

   $$(3t+2)^2y=\tfrac49(3t+2)^3+C$$
10. **Divide** by $(3t+2)^2$.

   $$y=\tfrac49(3t+2)+\dfrac{C}{(3t+2)^2}$$
11. **Plug in** $y(0)=0$.

   $$0=\tfrac89+\dfrac C4\quad\Rightarrow\quad C=-\tfrac{32}{9}$$
12. (c) **Type:** $dt$, $dy$ form → B3. **Write.**

   $$M=2t+y\cos t,\qquad N=\sin t+2y$$
13. **Test.**

   $$M_y=\cos t,\qquad N_t=\cos t\quad\checkmark$$
14. **Integrate $M$ in $t$** ($y$ is a number).

   $$U=t^2+y\sin t+h(y)$$
15. **Match $N$.**

   $$U_y=\sin t+h^{\prime}=\sin t+2y\quad\Rightarrow\quad h=y^2$$
16. **Answer**, then **plug in** $t=0$, $y=1$: $0+0+1=C$.

   $$t^2+y\sin t+y^2=1$$

**Answer:** (a) B1: $y=\sqrt{2(1+t^2)^2-1}$. (b) B2: $y=\frac49(3t+2)-\dfrac{32}{9(3t+2)^2}$. (c) B3: $t^2+y\sin t+y^2=1$. Review: [B1](#b1), [B2](#b2), [B3](#b3).

</details>

**Problem: E4 · W4 · Not exact: find the factor, then solve · like Pre-tutorial 4** (intermediate)

Consider $(3ty+y^2)\,dt+(t^2+ty)\,dy=0$ with $y(1)=1$. (a) Show it is not exact. (b) Find an integrating factor. (c) Solve.

<details><summary>Solution</summary>

1. **Type:** $dt$, $dy$ form → test (B3). **Write.**

   $$M=3ty+y^2,\qquad N=t^2+ty$$
2. (a) **Test:** they don’t match → B4.

   $$M_y=3t+2y,\qquad N_t=2t+y$$
3. (b) **Find $\mu$:** try Case 1. Factor the bottom, $N=t(t+y)$: the $(t+y)$ cancels, only $t$ is left.

   $$\begin{gathered}\dfrac{M_y-N_t}{N}=\dfrac{t+y}{t(t+y)}=\dfrac1t \\ \mu=e^{\int\frac1t\,dt}=t\end{gathered}$$
4. **Multiply** by $t$.

   $$(3t^2y+ty^2)\,dt+(t^3+t^2y)\,dy=0$$
5. **Re-test.**

   $$M_y=3t^2+2ty,\qquad N_t=3t^2+2ty\quad\checkmark$$
6. (c) **Integrate $M$ in $t$.**

   $$U=t^3y+\tfrac12t^2y^2+h(y)$$
7. **Match $N$:** $U_y=t^3+t^2y+h^{\prime}$ must equal $t^3+t^2y$.

   $$h^{\prime}=0$$
8. **Answer**, then **plug in** $t=1$, $y=1$: $1+\tfrac12=C$. Multiply by $2$.

   $$2t^3y+t^2y^2=3$$

**Answer:** (a) $M_y=3t+2y\neq2t+y=N_t$. (b) $\mu=t$. (c) $2t^3y+t^2y^2=3$. If a ratio seems to have both letters, factor before giving up. Review: [B4](#b4).

</details>

**Problem: E5 · W3 + W5 · Is the solution guaranteed?** (intermediate)

(a) For $\dfrac{dy}{dt}=3y^{2/3}$, does the theorem guarantee exactly one solution through (i) $(1,8)$, (ii) $(0,0)$? Then check that $y=0$ and $y=t^3$ both solve it. What does that say about $(0,0)$?

(b) Without solving, find the largest interval on which $(t^2-9)\,y^{\prime\prime}+t\,y^{\prime}+y=\dfrac1t$, $\;y(1)=0$, $y^{\prime}(1)=2$, has exactly one solution.

<details><summary>Solution</summary>

1. (a) **Type:** exactly one solution, first order → C1. **Write.**

   $$F=3y^{2/3}$$
2. **Differentiate** in $y$.

   $$F_y=2y^{-1/3}=\dfrac{2}{y^{1/3}}$$
3. **Find where it breaks:** $F$ is fine everywhere. $F_y$ divides by $y^{1/3}$.

   $$y=0$$
4. **Check the points:** (i) $y_0=8$ is off the line → exactly one. (ii) $y_0=0$ is on it → no guarantee.
5. Both pass through $(0,0)$ and solve it, so there really are two solutions there.

   $$\begin{gathered}y=0:\ 0=0\ \checkmark \\ y=t^3:\ 3t^2=3(t^3)^{2/3}\ \checkmark\end{gathered}$$
6. (b) **Type:** interval, second-order linear → C2, Case 1. **Write:** divide by $t^2-9$.

   $$p=\dfrac{t}{t^2-9},\quad q=\dfrac{1}{t^2-9},\quad f=\dfrac{1}{t(t^2-9)}$$
7. **Find where they break:** the bottoms are $0$ at $t=-3,\,0,\,3$.
8. **Pick the piece** containing $t_0=1$.

   $$(0,\,3)$$

**Answer:** (a) (i) Yes. (ii) No guarantee, and in fact two solutions ($y=0$, $y=t^3$) pass through $(0,0)$. (b) $(0,3)$. Review: [C1](#c1), [C2](#c2).

</details>

**Problem: E6 · W2 · RC step response, and a current that jumps · like Pre-tutorial 2** (introductory)

Before $t=0$ the switch is open and the capacitor holds $v=2\,\mathrm{V}$. The switch closes at $t=0$. (a) Write the ODE for $v$ for $t\ge0$. (b) Find $v(t)$. (c) Find $i_C$ just before and just after the switch closes.

```schematic
I1 0,0 -> 0,3 "$3\,\mathrm{mA}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$2\,\mathrm{k\Omega}$"
S1 3,3 -> 6,3 "$t=0$" action=close
C1 6,3 -> 6,0 "$5\,\mu\mathrm{F}$" v="$v$" i="$i_C$"
wire 6,0 -> 0,0
ground 0,0
```

<details><summary>Solution</summary>

1. **Type:** one capacitor and a DC source after the switch → D1, step response. Solve for $v$ (it can’t jump).
2. (a) **After:** KCL at the top node: the source current splits into $R$ and $C$. Divide by $C=5\times10^{-6}$.

   $$\begin{gathered}C\dfrac{dv}{dt}+\dfrac{v}{R}=I_s \\ \dfrac{dv}{dt}+100\,v=600\end{gathered}$$
3. (b) **Before:** given.

   $$v(0^-)=2\,\mathrm{V}$$
4. **Carry across:** a capacitor voltage can’t jump.

   $$x_0=v(0^+)=2\,\mathrm{V}$$
5. **After** (final value): long after, $C$ is a gap, so all of $I_s$ goes through $R$.

   $$x_f=RI_s=2000\times0.003=6\,\mathrm{V}$$
6. **After** (time constant): the current source is off (a gap), so $C$ sees just $R$.

   $$\tau=RC=2000\times5\times10^{-6}=0.01\,\mathrm{s}$$
7. **Plug in.**

   $$v=6+(2-6)e^{-t/0.01}=6-4e^{-100t}\ \mathrm{V}$$
8. (c) **Before:** the switch is open, so no current reaches $C$.

   $$i_C(0^-)=0$$
9. **Carry across:** $v=2\,\mathrm{V}$ still, so $R$ takes $\frac{2}{2000}=1\,\mathrm{mA}$. KCL: $C$ gets the rest.

   $$i_C(0^+)=3-1=2\,\mathrm{mA}$$
10. **Check** with $i_C=C\,v^{\prime}$ from (b): $v^{\prime}(0)=400$.

   $$i_C(0^+)=5\times10^{-6}\times400=2\,\mathrm{mA}\ \checkmark$$

**Answer:** (a) $v^{\prime}+100v=600$. (b) $v=6-4e^{-100t}\,\mathrm{V}$. (c) $0$ before, $2\,\mathrm{mA}$ after: the capacitor **current** jumps, its voltage doesn’t. Review: [D1](#d1).

</details>

**Problem: E7 · W5 · Complex roots, then a repeated root** (introductory)

Solve (a) $y^{\prime\prime}+4y^{\prime}+13y=0$, and (b) $y^{\prime\prime}+4y^{\prime}+4y=0$, each with $y(0)=1$, $y^{\prime}(0)=0$.

<details><summary>Solution</summary>

1. (a) **Type:** numbers in front, right side $0$ → B5. **Write** the quadratic.

   $$s^2+4s+13=0$$
2. **Solve** with the formula. Under the root: $16-52=-36<0$, so Case 3.

   $$s=\dfrac{-4\pm\sqrt{-36}}{2}=\dfrac{-4\pm j6}{2}=-2\pm j3$$
3. **Pick:** Case 3, $\sigma=-2$, $\omega=3$.

   $$y=e^{-2t}(c_1\cos3t+c_2\sin3t)$$
4. **Differentiate** (product rule).

   $$y^{\prime}=-2e^{-2t}(c_1\cos3t+c_2\sin3t)+e^{-2t}(-3c_1\sin3t+3c_2\cos3t)$$
5. **Plug in** $t=0$.

   $$\begin{gathered}y(0)=c_1=1 \\ y^{\prime}(0)=-2c_1+3c_2=0\quad\Rightarrow\quad c_2=\tfrac23\end{gathered}$$
6. (b) **Type:** B5. **Write** and **solve:** a perfect square.

   $$s^2+4s+4=(s+2)^2=0\quad\Rightarrow\quad s=-2\ \text{(twice)}$$
7. **Pick:** Case 2.

   $$y=(c_1+c_2t)\,e^{-2t}$$
8. **Differentiate** (product rule).

   $$y^{\prime}=c_2e^{-2t}-2(c_1+c_2t)\,e^{-2t}$$
9. **Plug in** $t=0$.

   $$\begin{gathered}y(0)=c_1=1 \\ y^{\prime}(0)=c_2-2c_1=0\quad\Rightarrow\quad c_2=2\end{gathered}$$

**Answer:** (a) $y=e^{-2t}\big(\cos3t+\tfrac23\sin3t\big)$. (b) $y=(1+2t)e^{-2t}$. Review: [B5](#b5).

</details>

**Problem: E8 · W5 · Parallel RLC step response · lecture Example 5.2, plus a twist** (intermediate)

The initial energy stored in the circuit is zero. At $t=0$ a DC current source of $24\,\mathrm{mA}$ is applied. (a) Find $i_L(t)$ for $t\ge0$. (b) Twist: which $R$ would make the circuit critically damped? Find $i_L(t)$ for that $R$.

```schematic
I1 0,0 -> 0,3 "$24\,\mathrm{mA}$"
S1 0,3 -> 3,3 "$t=0$" action=close
C1 3,3 -> 3,0 "$25\,\mathrm{nF}$" i="$i_C$"
wire 3,3 -> 6,3
L1 6,3 -> 6,0 "$25\,\mathrm{mH}$" i="$i_L$"
wire 6,3 -> 9,3
R1 9,3 -> 9,0 "$400\,\Omega$" i="$i_R$" v="$v$"
wire 9,0 -> 0,0
ground 0,0
```

<details><summary>Solution</summary>

1. **Type:** an $L$ and a $C$, all in parallel, with a DC source → D2, parallel step response. Solve for $i_L$ (it can’t jump).
2. (a) **Before:** zero energy, so nothing is charged and no current flows.

   $$i_L(0^-)=0,\qquad v_C(0^-)=0$$
3. **Carry across:** both carry over. Slope: $L$ sits across $C$, so $v_L=v_C(0^+)=0$, and $i_L^{\prime}=\frac{v_L}{L}$.

   $$i_L(0^+)=0,\qquad i_L^{\prime}(0^+)=\dfrac{0}{L}=0$$
4. **After:** parallel, so $\alpha=\frac{1}{2RC}$. Use H and F.

   $$\begin{gathered}\alpha=\dfrac{1}{2(400)(25\times10^{-9})}=50000, \\ \omega_0=\dfrac{1}{\sqrt{(0.025)(25\times10^{-9})}}=40000\end{gathered}$$
5. **After** (final value): long after, $L$ is a wire and takes all of the source.

   $$I_f=24\,\mathrm{mA}$$
6. **Pick:** $\alpha>\omega_0$, overdamped (B5 Case 1). Roots:

   $$\begin{gathered}s=-50000\pm\sqrt{50000^2-40000^2}=-50000\pm30000 \\ i_L=24+c_1e^{-20000t}+c_2e^{-80000t}\ \mathrm{mA}\end{gathered}$$
7. **Plug in** $t=0$: the value, then the slope (each root times its constant).

   $$\begin{gathered}24+c_1+c_2=0 \\ -20000c_1-80000c_2=0\end{gathered}$$
8. The second gives $c_1=-4c_2$. Put it in the first: $-3c_2=-24$.

   $$c_2=8,\qquad c_1=-32$$
9. (b) **Critical damping** means $\alpha=\omega_0=40000$. Solve $\frac{1}{2RC}=40000$.

   $$R=\dfrac{1}{2(40000)(25\times10^{-9})}=500\,\Omega$$
10. **Pick:** Case 2, root $-40000$ twice. Same final value.

   $$i_L=24+(c_1+c_2t)\,e^{-40000t}\ \mathrm{mA}$$
11. **Plug in** $t=0$: value, then slope ($c_2-40000c_1$ from the product rule).

   $$\begin{gathered}24+c_1=0\quad\Rightarrow\quad c_1=-24 \\ c_2-40000c_1=0\quad\Rightarrow\quad c_2=-960000\end{gathered}$$
12. **Check:** $t\to\infty$ gives $24\,\mathrm{mA}$ in both ✓.

**Answer:** (a) $i_L=24-32e^{-20000t}+8e^{-80000t}\ \mathrm{mA}$ (the lecture’s answer). (b) $R=500\,\Omega$: $i_L=24-24(1+40000t)e^{-40000t}\ \mathrm{mA}$. Review: [D2](#d2).

</details>

**Problem: E9 · W6 · The tutorial problem without the hints · Pre-tutorial 5** (intermediate)

(a) Solve $y^{\prime\prime}+y=6\cos^2t$, $\;y(0)=0$, $\;y(\pi/2)=0$. This time the forms of $y_c$ and $y_p$ are **not** given.

(b) For $y^{\prime\prime}-4y=e^{2t}+t$, write the form of $y_p$ and find it.

<details><summary>Solution</summary>

1. (a) **Type:** numbers in front, right side not $0$ → B6. **Solve $y_c$:** $s^2+1=0$, $s=\pm j$ (B5 Case 3, $\sigma=0$, $\omega=1$).

   $$y_c=c_1\sin t+c_2\cos t$$
2. No case fits $\cos^2t$, so use the identity first.

   $$6\cos^2t=3+3\cos2t$$
3. **Guess $y_p$:** constant → $A$ (Case 1); $\cos2t$ → both (Case 3). None is in $y_c$.

   $$y_p=A+B\cos2t+D\sin2t$$
4. Differentiate twice: each $\cos2t$, $\sin2t$ is multiplied by $-4$.

   $$y_p^{\prime\prime}=-4B\cos2t-4D\sin2t$$
5. **Plug in** to $y_p^{\prime\prime}+y_p$ and collect.

   $$A-3B\cos2t-3D\sin2t=3+3\cos2t$$
6. **Match** constants, $\cos2t$, $\sin2t$.

   $$A=3,\qquad B=-1,\qquad D=0$$
7. **Add.**

   $$y=3-\cos2t+c_1\sin t+c_2\cos t$$
8. **Plug in** $y(0)=0$: $\sin0=0$, $\cos0=1$.

   $$3-1+c_2=0\quad\Rightarrow\quad c_2=-2$$
9. **Plug in** $y(\pi/2)=0$: $\cos\pi=-1$, $\sin\frac\pi2=1$, $\cos\frac\pi2=0$.

   $$3+1+c_1=0\quad\Rightarrow\quad c_1=-4$$
10. (b) **Solve $y_c$:** $s^2-4=0$, $s=\pm2$ (B5 Case 1).

   $$y_c=c_1e^{2t}+c_2e^{-2t}$$
11. **Guess $y_p$:** $e^{2t}$ is in $y_c$ → Case 4, times $t$. The $t$ → Case 1, $Bt+D$.

   $$y_p=Ate^{2t}+Bt+D$$
12. Differentiate twice (product rule on $te^{2t}$).

   $$y_p^{\prime\prime}=A(4+4t)e^{2t}$$
13. **Plug in** to $y_p^{\prime\prime}-4y_p$. The $te^{2t}$ terms cancel.

   $$4Ae^{2t}-4Bt-4D=e^{2t}+t$$
14. **Match** $e^{2t}$, $t$, constants.

   $$A=\tfrac14,\qquad B=-\tfrac14,\qquad D=0$$

**Answer:** (a) $y=3-\cos2t-4\sin t-2\cos t$. (b) $y_p=\frac14te^{2t}-\frac14t$. Review: [B6](#b6).

</details>

**Problem: E10 · W6 · Reduction of order · like lecture Example 6.1** (intermediate)

Given that $y_1=t$ solves $t^2y^{\prime\prime}+t\,y^{\prime}-y=0$ for $t>0$, find the general solution.

<details><summary>Solution</summary>

1. **Type:** $t$ in front, one solution given → B7. **Write** (check $y_1$): $0+t-t=0$ ✓.
2. **Substitute** $y=tv$ (product rule).

   $$\begin{gathered}y^{\prime}=v+tv^{\prime} \\ y^{\prime\prime}=2v^{\prime}+tv^{\prime\prime}\end{gathered}$$
3. **Plug in and collect.** The plain-$v$ terms cancel ($tv-tv$).

   $$\begin{gathered}t^2(2v^{\prime}+tv^{\prime\prime})+t(v+tv^{\prime})-tv=0 \\ t^3v^{\prime\prime}+3t^2v^{\prime}=0\end{gathered}$$
4. **Solve for $z$:** set $z=v^{\prime}$, divide by $t^3$, separate (B1).

   $$\begin{gathered}\dfrac{dz}{z}=-\dfrac3t\,dt \\ z=\dfrac{c_1}{t^3}\end{gathered}$$
5. **Integrate** (power rule).

   $$v=-\dfrac{c_1}{2t^2}+c_2$$
6. **Multiply back** by $t$. $-\frac{c_1}{2}$ is just another constant: call it $c_1$.

   $$y=c_2\,t+\dfrac{c_1}{t}$$

**Answer:** $y=c_1\dfrac1t+c_2t$. Check $y=\frac1t$: $t^2\cdot\frac{2}{t^3}+t\cdot\left(-\frac{1}{t^2}\right)-\frac1t=0$ ✓. Review: [B7](#b7).

</details>
