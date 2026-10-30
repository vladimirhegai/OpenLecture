# ELEC 231 Midterm: Weeks 1–6 by Problem Type

## Start here: what the midterm asks

**Midterm:** 2 hours · 30 marks · Casio 991 only. Everything up to Monday Oct 26’s lecture and this week’s tutorial. **No Laplace transforms.**

> **Tip:** **The prof reuses his own problems.** If you can do every lecture example and tutorial problem, you’re fine: the midterm is that hard or easier. In this note they are marked **★**. Do the ★ ones first. The rest are short, easier warm-ups.

**Today’s plan (10:00–18:00).** Each block: read the steps, then do that section’s ★ problems with the answer closed.

| Time | Do | The ★ problems |
|---|---|---|
| 10:00–10:30 | [Topic A](#topic-a) complex numbers | Ex 1.1 divide, Ex 1.2 roots |
| 10:30–11:45 | [B0](#topic-b), [B1](#b1), [B2](#b2) name it, separable, linear | Ex 2.1, Ex 3.1–3.4, RL circuit, Pre-tut 3 |
| 11:45–12:00 | break |  |
| 12:00–13:00 | [B3](#b3), [B4](#b4) exact, make it exact | Ex 4.1–4.6, Pre-tut 4 |
| 13:00–13:45 | lunch |  |
| 13:45–14:30 | [D1](#d1) RC / RL circuits | Pre-tut 1, Pre-tut 2, RC natural/step |
| 14:30–15:30 | [B5](#b5), [D2](#d2) characteristic equation, RLC | Ex 5.2 (24 mA) |
| 15:30–15:45 | break |  |
| 15:45–16:45 | [B6](#b6), [B7](#b7) undetermined coefficients, reduction of order | Pre-tut 5 ($6\cos^2t$), $y^{\prime\prime}-ty^{\prime}+y=0$ |
| 16:45–17:05 | [Topic C](#topic-c) does a unique solution exist? | the two theorems |
| 17:05–18:00 | [Topic E](#topic-e) final run | redo every ★ from memory |

**Behind? Cut from the bottom of each block, never the ★ problems.** If you’re really short on time, skip [Topic C](#topic-c) and the non-★ warm-ups.

**Not taught, so not in this note:** Wronskians, the “multiply the guess by $t$” fix, guesses for $e^{at}$ or polynomial right sides, textbook circuit problems, Thévenin inside a circuit, Laplace.

Every solution in this note has the same shape. Use it on the exam too:

1. **Type:** say what kind of problem it is, and the clue. Example: “$y^{\prime}=t^2y$ is separable: a $t$-part times a $y$-part.”
2. **Steps:** run that section’s numbered steps, using its words. Every method starts with **Write**.
3. **Plug in:** use the given values to find the constants. Example: $y=Ce^{2t}$ with $y(0)=5$ gives $C=5$.

**Where do I go?** Find what the question gives you, then click the link. The browser’s Back button brings you back.

| The question gives you… | Go to |
|---|---|
| a complex number to convert, multiply, divide, power, roots | [Topic A](#topic-a) |
| an ODE to classify (order, linear, …) | [Topic B](#topic-b) |
| a first-order ODE where you can split the $y$’s from the $t$’s | [B1 · Separable](#b1) |
| $y^{\prime}+p(t)\,y=f(t)$ | [B2 · Integrating factor](#b2) |
| $M\,dt+N\,dy=0$ | [B3 · Exact](#b3), [B4 · Make it exact](#b4) |
| $ay^{\prime\prime}+by^{\prime}+cy=0$ (numbers $a,b,c$) | [B5 · Characteristic equation](#b5) |
| $ay^{\prime\prime}+by^{\prime}+cy=f(t)$ | [B6 · Undetermined coefficients](#b6) |
| $t$ in the coefficients, and one solution given | [B7 · Reduction of order](#b7) |
| “does a unique solution exist?”, or an interval | [Topic C](#topic-c) |
| a circuit with a switch: find $v(t)$ or $i(t)$ | [Topic D](#topic-d) |

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

<details><summary>★ Lecture §2: $\cos(A+B)$ and $\sin(A+B)$ from Euler, $\;e^{j\theta}=\cos\theta+j\sin\theta$</summary>

Step 1 · **Write** $e^{jA}e^{jB}=e^{j(A+B)}$ and expand each side with Euler.

$$
(\cos A+j\sin A)(\cos B+j\sin B)=\cos(A+B)+j\sin(A+B)
$$

Step 2 · **Multiply out** the left side ($j^2=-1$).

$$
\cos A\cos B-\sin A\sin B+j(\sin A\cos B+\cos A\sin B)
$$

Step 3 · **Match** the real parts, then the $j$ parts.

$$
\cos(A+B)=\cos A\cos B-\sin A\sin B
$$

$$
\sin(A+B)=\sin A\cos B+\cos A\sin B
$$

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

**Conjugate facts** (lecture 4.3): $z^*=a-jb$ (polar: flip the angle). Then $zz^*=a^2+b^2=c^2$, $\;z+z^*=2a$, $\;z-z^*=j2b$. And $|e^{j\theta}|=1$ always.

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

**Problem: ★ Problem 2 · W1 · Divide in rectangular form · lecture Example 1.1** (introductory)

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

**Problem: ★ Problem 4 · W1 · The four fourth roots · lecture Example 1.2** (introductory)

Find the four fourth roots of $z=81e^{j60^\circ}$.

<details><summary>Solution</summary>

1. **Type:** roots ($k=4$). Already polar: $c=81$, $\theta=60^\circ$.

   $$z=81\angle60^\circ$$
2. **Length:** the same for all four.

   $$81^{1/4}=3$$
3. **First angle.**

   $$\dfrac{60^\circ}{4}=15^\circ$$
4. **Spacing:** keep adding $360^\circ/4$.

   $$\dfrac{360^\circ}{4}=90^\circ$$
5. List all four.

   $$3\angle15^\circ,\quad 3\angle105^\circ,\quad 3\angle195^\circ,\quad 3\angle285^\circ$$

**Answer:** $3e^{j15^\circ}$, $3e^{j105^\circ}$, $3e^{j195^\circ}$, $3e^{j285^\circ}$.

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

**Linear means you can scale** (lecture §3.1): if $y(t)$ solves the equation with right side $f(t)$, then $A\,y(t)$ solves it with right side $A\,f(t)$. Example: $y=2-2e^{-2t}$ solves $y^{\prime}+2y=4$, so $3y=6-6e^{-2t}$ solves $y^{\prime}+2y=12$.

**Step 3: fix the constants.** Every method gives a **general solution**: a formula with unknown constants in it.

- 1st order → one constant, $C$. One condition, like $y(1)=2$, pins it down.
- 2nd order → two constants, $c_1$ and $c_2$. You need two conditions, usually $y(0)$ and $y^{\prime}(0)$.
- A problem that gives you conditions is called an **initial value problem** (IVP). Plug the conditions into the general solution and solve for the constants.

**Checking a solution** (Week 2 asks this). Plug $y$ and its derivatives into the ODE. If both sides match for **every** $t$, it’s a solution.

Example: is $y=e^{-2t}$ a solution of $y^{\prime}+2y=0$? $\;-2e^{-2t}+2e^{-2t}=0$ ✓. Yes.

**Problem: ★ Problem 6 · W2 · Name it, then route it · lecture Example 2.1 and others** (introductory)

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

<details><summary>★ Lecture Example 3.3 (try it, then open): $\;\dfrac{dy}{dt}=\dfrac{3t+ty^2}{y+t^2y}$, $\;y(1)=3$</summary>

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

**Problem: ★ Problem 8 · W3 · Separate and use a starting value · Pre-tutorial 3(a)** (introductory)

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

**Problem: ★ Problem 9 · W3 · A general solution with a power · lecture Example 3.2** (introductory)

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

**Problem: ★ Problem 10 · W3 · Differential form · Pre-tutorial 3(b)** (intermediate)

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

**Problem: ★ Problem 11 · W3 · Collect before separating · lecture Example 3.4** (intermediate)

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

<details><summary>★ Lecture Example 3.1 (try it, then open): $\;y^{\prime}+\dfrac{10\,y}{2t+5}=10$, $\;y(0)=0$</summary>

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

> **Tip:** **Shortcut when $p=k$ and $f=F$ are both plain numbers:** $\;y=\dfrac{F}{k}+Ce^{-kt}$. Example: $y^{\prime}+2y=4$ gives $y=2+Ce^{-2t}$. Every RC and RL circuit has this shape ([D1](#d1)).

> **Warning:** **Get $y^{\prime}$ alone first.** In $ty^{\prime}+2y=t^2$, divide by $t$ first. Then $p=\frac2t$, not $2$.

> **Warning:** **Multiply the right side by $\mu$ too.** It’s $\int\mu f\,dt$, not $\int f\,dt$.

> **Tip:** **Both separable and linear?** Either method works (the prof solves the RL circuit $i^{\prime}+5i=50$ both ways). Happens when $f=0$, or when $p$ and $f$ are plain numbers: $\;\dfrac{di}{50-5i}=dt$.

#### Practice: B2

**Problem: ★ Problem 12 · W3 · The lecture’s RL equation · lecture §1.1** (introductory)

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

**Problem: ★ Problem 13 · W3 · Linear and separable: solve it both ways · Pre-tutorial 3(c)** (introductory)

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

**Problem: Problem 14 · W3 · Divide first, then a power of t** (intermediate)

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

<details><summary>★ Lecture Example 4.1 (try it, then open): $\;(2ty+3t^2)\,dt+t^2\,dy=0$</summary>

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

<details><summary>★ Lecture exercise (b) (try it, then open): $\;y^{\prime}=\dfrac{t-y}{t+y}$, $\;y(0)=1$</summary>

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

**Problem: ★ Problem 15 · W4 · Test, then solve · lecture exercise (a)** (introductory)

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

**Problem: ★ Problem 16 · W4 · Test before you integrate · lecture exercise (d)** (introductory)

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

**Problem: ★ Problem 17 · W4 · The sign trap · lecture exercise (c)** (intermediate)

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

#### Steps and examples

1. **Write** it as $M\,dt+N\,dy=0$. Read $M$ and $N$ with their signs.
2. **Test:** $M_y\neq N_t$. (Equal? It’s already exact: [B3](#b3).)
3. **Find $\mu$:** try Case 1, then Case 2. Keep the ratio with only one letter. No $+C$ in this integral.
4. **Multiply** the whole equation by $\mu$: both $M$ and $N$.
5. **Re-test:** it must pass now. If not, recheck your algebra.
6. **Finish like B3:** integrate $M$ in $t$, match $N$, answer $U=C$, plug in.

<details><summary>★ Lecture Example 4.6 + Pre-tutorial 4 (try it, then open): $\;y\,dt+(3+3t-y)\,dy=0$</summary>

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

**Problem: Problem 18 · W4 · A factor in y only** (introductory)

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

#### Practice: B5

**Problem: Problem 19 · W5 · Two different real roots** (introductory)

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

**Problem: Problem 20 · W5 · A repeated root** (introductory)

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

**Problem: Problem 21 · W5 · No damping term** (intermediate)

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

**Steps**

1. **Write** it with every $y$ term on the left and $f(t)$ on the right.
2. **Solve $y_c$:** set the right side to $0$ and do [B5](#b5) (quadratic → case → form with $c_1,c_2$).
3. **Guess $y_p$** from the two cases below.
4. **Plug $y_p$ into the ODE and match:** constants with constants, each $\cos$, each $\sin$. Solve for $A,B,D$.
5. **Add:** $y=y_c+y_p$.
6. **Plug in** the conditions on the **whole** $y$, never on $y_c$ alone.

#### Case 1: f is a constant

Guess a constant $A$. Two derivatives of a constant are $0$, so only the $y$ term is left:

$$
y^{\prime\prime}+4y=8\quad\Longrightarrow\quad y_p=A,\quad 4A=8,\quad A=2
$$

#### Case 2: f is a sin or a cos

Guess **both** $\cos$ and $\sin$, even if $f$ has only one:

$$
5\sin2t\ \to\ A\cos2t+B\sin2t
$$

Why both: each derivative swaps $\cos$ and $\sin$, so both show up anyway. Handy fact: two derivatives multiply by $-r^2$:

$$
(A\cos rt+B\sin rt)^{\prime\prime}=-r^2(A\cos rt+B\sin rt)
$$

<details><summary>Full example: $\;y^{\prime\prime}+3y^{\prime}+2y=10\sin t$ (general solution)</summary>

Step 1 · **Solve $y_c$:** $s^2+3s+2=(s+1)(s+2)=0$.

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

**A constant plus a cos?** Guess the sum of the two guesses: $A+B\cos2t+D\sin2t$.

**A $\cos^2t$ or $\sin^2t$?** Turn it into a constant plus $\cos2t$ first:

$$
\begin{gathered}\cos^2t=\tfrac12+\tfrac12\cos2t, \\ \sin^2t=\tfrac12-\tfrac12\cos2t\end{gathered}
$$

#### ★ The tutorial problem (know this cold)

Pre-tutorial 5 = the Week 6 tutorial = the lecture’s own example. The single most likely midterm question. Be able to do every step, the two conditions included. ($\ddot y$ is the prof’s way of writing $y^{\prime\prime}$.)

$$
\ddot y+y=6\cos^2t,\qquad y(0)=0,\quad y(\pi/2)=0
$$

<details><summary>★ Full solution (try it, then open): $\;\ddot y+y=6\cos^2t$, $\;y(0)=0$, $\;y(\pi/2)=0$</summary>

Step 1 · **Solve $y_c$:** $s^2+1=0$ gives $s=\pm j$ (B5 Case 3, $\sigma=0$, $\omega=1$).

$$
y_c=c_1\sin t+c_2\cos t
$$

Step 2 · Use the identity: a constant plus $\cos2t$.

$$
6\cos^2t=3+3\cos2t
$$

Step 3 · **Guess $y_p$:** the constant → $A$ (Case 1). The $\cos2t$ → both $\cos2t$ and $\sin2t$ (Case 2).

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

The tutorial hands you $y_c$ and the $y_p$ guess. The exam might not: get $y_c$ from [B5](#b5) and $y_p$ from the two cases above.

#### Practice: B6

**Problem: Problem 22 · W6 · A constant right side, from rest** (introductory)

Solve $y^{\prime\prime}+4y=8$, $\;y(0)=0$, $y^{\prime}(0)=0$.

<details><summary>Solution</summary>

1. **Type:** numbers in front, right side $8$ → B6.
2. **Solve $y_c$:** $s^2+4=0$, $s=\pm j2$ (B5 Case 3).

   $$y_c=c_1\cos2t+c_2\sin2t$$
3. **Guess $y_p$:** a constant (Case 1).

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

**Problem: Problem 23 · W6 · The tutorial problem with sin², no hints · like Pre-tutorial 5** (intermediate)

Solve $y^{\prime\prime}+y=4\sin^2t$, $\;y(0)=0$, $y^{\prime}(0)=0$.

<details><summary>Solution</summary>

1. **Type:** numbers in front, right side not $0$ → B6. Same left side as the tutorial.
2. **Solve $y_c$:** $s^2+1=0$, $s=\pm j$ (B5 Case 3).

   $$y_c=c_1\sin t+c_2\cos t$$
3. **Write** the right side with the identity.

   $$4\sin^2t=2-2\cos2t$$
4. **Guess $y_p$:** constant + both $\cos2t$ and $\sin2t$.

   $$\begin{gathered}y_p=A+B\cos2t+D\sin2t \\ y_p^{\prime\prime}=-4B\cos2t-4D\sin2t\end{gathered}$$
5. **Plug in and match.**

   $$\begin{gathered}A-3B\cos2t-3D\sin2t=2-2\cos2t \\ A=2,\qquad B=\tfrac23,\qquad D=0\end{gathered}$$
6. **Add.**

   $$y=2+\tfrac23\cos2t+c_1\sin t+c_2\cos t$$
7. **Differentiate** for $y^{\prime}(0)$.

   $$y^{\prime}=-\tfrac43\sin2t+c_1\cos t-c_2\sin t$$
8. **Plug in** $t=0$.

   $$\begin{gathered}y(0)=2+\tfrac23+c_2=0\quad\Rightarrow\quad c_2=-\tfrac83 \\ y^{\prime}(0)=c_1=0\end{gathered}$$

**Answer:** $y=2+\tfrac23\cos2t-\tfrac83\cos t$.

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

**★ The prof’s example**, step by step (press the arrows). Then finish it yourself:

```steps
title "★ Lecture (Week 6): reduce y″ − t y′ + y = 0, given y₁ = t"
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

<details><summary>★ Finish the lecture example (try it, then open): solve $\;tz^{\prime}+(2-t^2)z=0$, then find $y$</summary>

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

**Problem: Problem 24 · W5 + W6 · Where the repeated-root t comes from** (introductory)

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

**Problem: Problem 25 · W6 · A second solution with a logarithm** (intermediate)

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

**The lecture’s words** (Theorem 3.2, Spiegel): if $F$ and $\dfrac{\partial F}{\partial y}$ are real, finite, one-valued and continuous in a region $R$, then exactly one solution passes through any point of $R$. The prof stresses: these conditions are **sufficient, not necessary**.

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

#### Practice: C1

**Problem: Problem 26 · W3 · Same equation, two starting points** (introductory)

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

**Problem: Problem 27 · W3 · Which points are guaranteed? · the Pre-tutorial 3(a) equation** (introductory)

For $\dfrac{dy}{dt}=-\dfrac{t}{y}$, decide whether the theorem guarantees a unique solution through (a) $(1,2)$, (b) $(0,3)$, (c) $(2,0)$.

<details><summary>Solution</summary>

1. **Type:** C1.
2. **Write.**

   $$F=-\dfrac ty$$
3. **Differentiate** in $y$ (power rule).

   $$F_y=\dfrac{t}{y^2}$$
4. **Find where it breaks:** both divide by $y$.

   $$y=0$$
5. **Check the points:** (a) $y_0=2$ and (b) $y_0=3$ are off the line. (c) $y_0=0$ is on it.

**Answer:** (a) Yes. (b) Yes. (c) No guarantee: $F$ itself is undefined at $(2,0)$.

</details>

### C2 · Second order linear: what interval?

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

**The lecture’s words** (Theorem 5.1, Spiegel): if all the coefficients $a_0(t),\dots,a_n(t)$ and the right side are continuous on $a\le t\le b$, and $a_0(t)$ (what multiplies the top derivative) is **never 0** there, then exactly one solution fits $y(c),y^{\prime}(c),\dots$ — same thing as “$p,q,f$ don’t break”.

The question is one of two cases:

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

#### Practice: C2

**Problem: Problem 28 · W5 · Find the interval; do not solve** (intermediate)

For $(t-1)\,y^{\prime\prime}+y^{\prime}+y=\ln t$, find the largest interval on which the theorem guarantees exactly one solution for (a) $t_0=2$, (b) $t_0=\tfrac12$.

<details><summary>Solution</summary>

1. **Type:** C2, Case 1.
2. **Write:** divide by $t-1$.

   $$p=\dfrac1{t-1},\quad q=\dfrac1{t-1},\quad f=\dfrac{\ln t}{t-1}$$
3. **Find where they break:** $\ln t$ needs $t>0$, the denominator needs $t\neq1$. Pieces: $(0,1)$ and $(1,\infty)$.
4. **Pick the piece:** $t_0=2$ is in $(1,\infty)$. $t_0=\tfrac12$ is in $(0,1)$.

**Answer:** (a) $(1,\infty)$. (b) $(0,1)$.

</details>

**Problem: Problem 29 · W5 + W6 · The answer without solving** (intermediate)

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

**★ Lecture example (Week 3 §1.1).** The switch closes at $t=0$. The inductor carries no current before that. Find $i(t)$ for $t\ge0$.

```schematic
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$10\,\Omega$" i="$i$"
L1 6,3 -> 6,0 "$2\,\mathrm{H}$" v="$v$"
wire 6,0 -> 0,0
ground 0,0
```

<details><summary>★ Lecture §1.1, the 100 V RL circuit (try it, then open)</summary>

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

#### Practice: D1

**Problem: ★ Problem 30 · W1 · RL natural response · Pre-tutorial 1** (introductory)

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

**Problem: ★ Problem 31 · W2 · Can the capacitor current jump? · Pre-tutorial 2** (introductory)

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

**Problem: ★ Problem 32 · W2 · RC natural and step response · lecture §4 and §5** (introductory)

(a) **Natural response** (lecture §4). The switch has been at $a$ for a long time, so $C$ is charged by $V_s$ through $R_1$. At $t=0$ it moves to $b$, leaving $C$ alone with $R$. Find $v(t)$, $t\ge0$.

```schematic
V1 0,3 -> 0,0 "$V_s$"
R1 0,3 -> 3,3 "$R_1$"
S1 3,3 -> 6,3 "$t=0$" action=open
C1 6,3 -> 6,0 "$C$" v="$v$"
S2 6,3 -> 9,3 "$t=0$" action=close
R2 9,3 -> 9,0 "$R$"
wire 9,0 -> 0,0
label 3,3 "$a$" above
label 9,3 "$b$" above
ground 0,0
```

(b) **Step response** (lecture §5, the Pre-tutorial 2 circuit above). $I_s$, $R$ and $C$ end up in parallel, $v(0)=V_0$. Find $v(t)$, $t\ge0$.

(c) In (a), take $V_s=10\,\mathrm{V}$, $R=1\,\mathrm{k\Omega}$, $C=1\,\mu\mathrm{F}$. Find $\tau$ and $v(\tau)$.

<details><summary>Solution</summary>

1. **Type:** one $C$ → first order → D1. (a) has no source after the switch: natural. (b) keeps $I_s$: step.
2. (a) **Before:** long time, $C$ is a gap, so no current flows through $R_1$ and $C$ sits at the source voltage.

   $$v(0^-)=V_s=v(0^+)$$
3. (a) **After:** only $C$ and $R$ in a loop, no source, so $x_f=0$. $C$ sees just $R$.

   $$\tau=RC$$
4. (a) **Plug in.**

   $$v(t)=V_s\,e^{-t/RC}$$
5. (b) **After:** long time, $C$ is a gap, so all of $I_s$ goes through $R$.

   $$\begin{gathered}V_f=RI_s \\ \tau=RC\end{gathered}$$
6. (b) **Plug in** with $x_0=V_0$.

   $$v(t)=RI_s+(V_0-RI_s)\,e^{-t/RC}$$
7. (b) **Check** with KCL at the top node: $C\frac{dv}{dt}+\frac vR=I_s$ is the [B2](#b2) shape, and $t\to\infty$ gives $RI_s$ ✓.
8. (c) **Numbers:** $\tau=RC=10^3\times10^{-6}$. After one $\tau$, $e^{-1}\approx0.368$ of the start is left.

   $$\begin{gathered}\tau=1\,\mathrm{ms} \\ v(\tau)=10e^{-1}\approx3.68\,\mathrm{V}\end{gathered}$$

**Answer:** (a) $v=V_se^{-t/RC}$. (b) $v=RI_s+(V_0-RI_s)e^{-t/RC}$. (c) $\tau=1\,\mathrm{ms}$, $v(\tau)\approx3.68\,\mathrm{V}$ (37% of $V_s$).

</details>

### D2 · An L and a C: RLC circuits (second order)

[Week 5 · Topic 3](/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/0c7a77fe-aeed-47a8-b1c3-4967d73eea21#d5ad9ba9-0ec5-4b62-acf5-b1c7e17d6463)

**Use this when**, after the switch, there’s an inductor **and** a capacitor.

**The move: it’s [B5](#b5) with circuit names.** The lecture’s parallel RLC gives this quadratic:

$$
s^2+\dfrac{1}{RC}\,s+\dfrac{1}{LC}=0
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

Name the two numbers in it:

$$
\begin{gathered}\alpha=\dfrac{1}{2RC}, \\ \omega_0=\dfrac{1}{\sqrt{LC}}\end{gathered}
$$

Then the roots are (lecture eq. 5.7):

$$
s_{1,2}=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}
$$

**Short example** (lecture Example 5.2): $R=400\,\Omega$, $C=25\,\mathrm{nF}$, $L=25\,\mathrm{mH}$:

$$
\begin{gathered}\alpha=\dfrac{1}{2(400)(25\times10^{-9})}=50\,000, \\ \omega_0=\dfrac{1}{\sqrt{(25\times10^{-3})(25\times10^{-9})}}=40\,000\end{gathered}
$$

(Series RLC, seen once in Week 2: $\;i^{\prime\prime}+\frac RL\,i^{\prime}+\frac1{LC}\,i=0$, so $\alpha=\frac{R}{2L}$ instead. Same $\omega_0$.)

#### The three cases (same as B5)

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
\alpha=50\,000,\ \omega_0=40\,000\quad\Longrightarrow\quad s=-50\,000\pm30\,000\quad\text{(overdamped)}
$$

$$
\alpha=\omega_0=40\,000\quad\Longrightarrow\quad (c_1+c_2t)e^{-40\,000t}\quad\text{(critical)}
$$

$$
\alpha=32\,000,\ \omega_0=40\,000\quad\Longrightarrow\quad \omega_d=24\,000\quad\text{(underdamped)}
$$

#### Step response: final value + natural response

A DC source switched on (lecture §3): the answer is the **final value** plus the natural response, like $y_p+y_c$ in [B6](#b6):

$$
i_L(t)=I+(\text{the B5 form})
$$

Why $I$: long after, $L$ is a wire, so it carries **all** of the source current. (That’s the lecture’s $I_P=I$.)

**Steps**

1. **Before:** old circuit. “No initial energy” means $v(0)=0$ and $i_L(0)=0$ (since $\tfrac12Cv^2=\tfrac12Li^2=0$).
2. **Carry across:** $v(0^+)=v(0^-)$, $i_L(0^+)=i_L(0^-)$. Then the slope (cards below).
3. **After:** compute $\alpha$, $\omega_0$. Final value: $I$ for $i_L$ with a source on, $0$ with none.
4. **Pick** the case (compare $\alpha$, $\omega_0$) and write $x=x_f+$ the form.
5. **Plug in** $t=0$: the value gives one equation, the slope gives the other. Use the **whole** answer, $x_f$ included.
6. **Check:** $t\to\infty$ gives $x_f$.

<details><summary>Slope of $i_L$: $\;\dfrac{di_L}{dt}(0^+)=\dfrac{v(0^+)}{L}$</summary>

Step 1 · From $v=L\frac{di_L}{dt}$. The lecture uses this in Example 5.2: $v(0)=0$, so the slope is $0$.

$$
\dfrac{di_L}{dt}(0^+)=\dfrac{0}{L}=0
$$

</details>

<details><summary>Slope of $v$: KCL, $\;i_C=-(i_L+i_R)$, then $\;v^{\prime}(0^+)=\dfrac{i_C(0^+)}{C}$</summary>

Step 1 · All three arrows point down, so the currents add to $0$ (plus any source current coming in). $i_R=\frac{v(0^+)}{R}$.

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

> **Warning:** **Fit the constants to the whole answer, the final value included.** $i_L=24+A_1e^{s_1t}+A_2e^{s_2t}$ with $i_L(0)=0$: $\;24+A_1+A_2=0$, not $A_1+A_2=0$.

> **Warning:** **Units first.** $1\,\mathrm{mH}=10^{-3}\,\mathrm{H}$, $1\,\mu\mathrm{F}=10^{-6}\,\mathrm{F}$, $1\,\mathrm{nF}=10^{-9}\,\mathrm{F}$. Keep currents in mA and the constants come out in mA.

#### Practice: D2

**Problem: ★ Problem 33 · W5 · Parallel RLC step response · lecture Example 5.2** (introductory)

The initial energy stored in the circuit is zero. At $t=0$ a DC current source of $24\,\mathrm{mA}$ is switched on. $R=400\,\Omega$, $C=25\,\mathrm{nF}$, $L=25\,\mathrm{mH}$. Find $i_L(t)$, $t\ge0$.

```schematic
I1 0,0 -> 0,3 "$24\,\mathrm{mA}$"
S1 0,3 -> 3,3 "$t=0$" action=close
C1 3,3 -> 3,0 "$25\,\mathrm{nF}$" v="$v$" i="$i_C$"
wire 3,3 -> 6,3
L1 6,3 -> 6,0 "$25\,\mathrm{mH}$" i="$i_L$"
wire 6,3 -> 9,3
R1 9,3 -> 9,0 "$R$" i="$i_R$"
wire 9,0 -> 0,0
ground 0,0
```

<details><summary>Solution</summary>

1. **Type:** an $L$ and a $C$ → second order → D2. A source stays on → step response: $i_L=24+$ natural.
2. **Before:** zero energy, so nothing is stored.

   $$v(0)=0,\qquad i_L(0)=0$$
3. **Carry across** (slope): $L\frac{di_L}{dt}=v$, and $v(0)=0$.

   $$\dfrac{di_L}{dt}(0)=0$$
4. **After:** $\alpha$ and $\omega_0$.

   $$\begin{gathered}\alpha=\dfrac{1}{2RC}=\dfrac{1}{2(400)(25\times10^{-9})}=50\,000 \\ \omega_0=\dfrac{1}{\sqrt{LC}}=40\,000\end{gathered}$$
5. **Pick:** $\alpha>\omega_0$, overdamped (B5 Case 1). Roots:

   $$\begin{gathered}s=-50\,000\pm\sqrt{50\,000^2-40\,000^2}=-50\,000\pm30\,000 \\ s_1=-20\,000,\qquad s_2=-80\,000\end{gathered}$$
6. Write the whole answer (mA).

   $$i_L=24+A_1e^{-20\,000t}+A_2e^{-80\,000t}$$
7. **Plug in** $i_L(0)=0$.

   $$24+A_1+A_2=0$$
8. **Plug in** the slope: differentiate, then $t=0$.

   $$-20\,000A_1-80\,000A_2=0\quad\Rightarrow\quad A_1=-4A_2$$
9. Solve: $-4A_2+A_2=-24$.

   $$A_2=8,\qquad A_1=-32$$
10. **Check:** $t\to\infty$ gives $24\,\mathrm{mA}$ ✓ (all the source current through the wire-like $L$).

**Answer:** $i_L(t)=24-32e^{-20\,000t}+8e^{-80\,000t}\ \mathrm{mA}$, $t\ge0$.

</details>

**Problem: Problem 34 · W5 · Same circuit, R = 500 Ω: critically damped · like lecture Example 5.2** (intermediate)

Repeat lecture Example 5.2 with $R=500\,\Omega$ (zero initial energy, $24\,\mathrm{mA}$, $25\,\mathrm{nF}$, $25\,\mathrm{mH}$). Find $i_L(t)$.

<details><summary>Solution</summary>

1. **Type:** same as Example 5.2: $i_L=24+$ natural, with $i_L(0)=0$ and $i_L^{\prime}(0)=0$.
2. **After:** only $\alpha$ changes.

   $$\begin{gathered}\alpha=\dfrac{1}{2(500)(25\times10^{-9})}=40\,000 \\ \omega_0=40\,000\end{gathered}$$
3. **Pick:** $\alpha=\omega_0$, critically damped (B5 Case 2), root $-40\,000$ twice.

   $$i_L=24+(D_1t+D_2)\,e^{-40\,000t}$$
4. **Plug in** $i_L(0)=0$.

   $$24+D_2=0\quad\Rightarrow\quad D_2=-24$$
5. **Plug in** the slope. Product rule: $i_L^{\prime}(0)=D_1-40\,000D_2$.

   $$D_1-40\,000(-24)=0\quad\Rightarrow\quad D_1=-960\,000$$

**Answer:** $i_L(t)=24-960\,000\,t\,e^{-40\,000t}-24e^{-40\,000t}\ \mathrm{mA}$.

</details>

**Problem: Problem 35 · W5 · Same circuit, R = 625 Ω: underdamped · like lecture Example 5.2** (intermediate)

Repeat lecture Example 5.2 with $R=625\,\Omega$. Find $i_L(t)$.

<details><summary>Solution</summary>

1. **Type:** same as Example 5.2: $i_L=24+$ natural, with $i_L(0)=0$ and $i_L^{\prime}(0)=0$.
2. **After:**

   $$\begin{gathered}\alpha=\dfrac{1}{2(625)(25\times10^{-9})}=32\,000 \\ \omega_0=40\,000\end{gathered}$$
3. **Pick:** $\alpha<\omega_0$, underdamped (B5 Case 3).

   $$\begin{gathered}\omega_d=\sqrt{40\,000^2-32\,000^2}=24\,000 \\ i_L=24+e^{-32\,000t}(B_1\cos24\,000t+B_2\sin24\,000t)\end{gathered}$$
4. **Plug in** $i_L(0)=0$.

   $$24+B_1=0\quad\Rightarrow\quad B_1=-24$$
5. **Plug in** the slope ($\sigma c_1+\omega c_2$ from B5).

   $$-32\,000B_1+24\,000B_2=0\quad\Rightarrow\quad B_2=-32$$

**Answer:** $i_L(t)=24-e^{-32\,000t}\big(24\cos24\,000t+32\sin24\,000t\big)\ \mathrm{mA}$.

</details>

**Problem: Problem 36 · W5 · Natural response: the slope comes from KCL · textbook P8.7** (intermediate)

$R=\tfrac{12500}{3}\,\Omega$, $L=250\,\mathrm{mH}$ and $C=10\,\mathrm{nF}$ are in parallel, with no source. At the start, $v(0)=90\,\mathrm{V}$ and $i_L(0)=-30\,\mathrm{mA}$ (arrows as drawn). Find $v(t)$ for $t\ge0$.

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

1. **Type:** parallel RLC, no source: a natural response, final value $0$.
2. **Carry across** (slope): first the resistor current, $i_R=\dfrac{90}{12500/3}=21.6\,\mathrm{mA}$. KCL (all arrows down): $i_C=-(i_L+i_R)$.

   $$i_C(0^+)=-(-30+21.6)=8.4\,\mathrm{mA}$$
3. Divide by $C$ to get the slope.

   $$v'(0^+)=\dfrac{8.4\times10^{-3}}{10^{-8}}=8.4\times10^5\,\mathrm{V/s}$$
4. **After:** $\alpha=\dfrac{1}{2RC}=12\,000$ and $\omega_0=\dfrac{1}{\sqrt{LC}}=20\,000$. $\alpha<\omega_0$, so underdamped.

   $$\omega_d=\sqrt{20\,000^2-12\,000^2}=16\,000$$
5. **Pick:** the cosine coefficient is $v(0)=90$.

   $$v=e^{-12\,000t}(90\cos16\,000t+c_2\sin16\,000t)$$
6. **Plug in** the slope: $-\alpha(90)+\omega_dc_2=8.4\times10^5$.

   $$-12\,000(90)+16\,000c_2=840\,000\ \Rightarrow\ c_2=120$$

**Answer:** $v=e^{-12\,000t}(90\cos16\,000t+120\sin16\,000t)\,\mathrm{V}$, $t\ge0$.

</details>

## Topic E: Final run — every ★ problem

**The last hour.** These are all the prof’s own problems. For each one: cover the answer, do it on paper, then open the box and check. Wrong or slow? Click the section link and redo it there (the full solutions are there, same steps).

**Week 1** · [Topic A](#topic-a) · [D1](#d1)

1. **Ex 1.1** Compute $\dfrac{80+j18}{8+j10}$.
2. **Ex 1.2** The four fourth roots of $81e^{j60^\circ}$.
3. **§2** Get $\cos(A+B)$ and $\sin(A+B)$ from $e^{jA}e^{jB}=e^{j(A+B)}$.
4. **Pre-tut 1** RL natural response: $L=8\,\mathrm{mH}$, $R=4\,\Omega$, $I_s=4\,\mathrm{A}$. Find $i(t)$ and sketch.

<details><summary>Answers: Week 1</summary>

1. $5-j4$
2. $3e^{j15^\circ},\ 3e^{j105^\circ},\ 3e^{j195^\circ},\ 3e^{j285^\circ}$
3. Expand both sides with Euler, match real parts and $j$ parts.
4. $\tau=2\,\mathrm{ms}$, $i=4e^{-500t}\,\mathrm{A}$

</details>

**Week 2** · [Topic B](#topic-b) · [D1](#d1)

1. **Ex 2.1** Is $t^3y^{\prime\prime}+e^ty^{\prime}+y=0$ linear? Order? Homogeneous? Constant coefficients?
2. **§4** RC natural response: $v(0)=V_s$, then $C$ alone with $R$. Find $v(t)$.
3. **§5** RC step response: $I_s$, $R$, $C$ in parallel, $v(0)=V_0$. Find $v(t)$.
4. **Pre-tut 2** Same circuit, $V_0=0$, $I_s=2\,\mathrm{A}$, $R=1\,\mathrm{k\Omega}$: $i_C(0^-)$ and $i_C(0^+)$?

<details><summary>Answers: Week 2</summary>

1. Linear, 2nd order, homogeneous, **not** constant-coefficient.
2. $v=V_se^{-t/RC}$
3. $v=RI_s+(V_0-RI_s)e^{-t/RC}$
4. $0$ and $2\,\mathrm{A}$: the current jumps, the voltage doesn’t.

</details>

**Week 3** · [B1](#b1) · [B2](#b2) · [Topic C](#topic-c)

1. **Ex 3.1** $y^{\prime}+\dfrac{10y}{2t+5}=10$, $y(0)=0$.
2. **§1.1** RL circuit: $2\frac{di}{dt}+10i=100$, $i(0)=0$. Integrating factor, then again by separating.
3. **Ex 3.2** $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$.
4. **Ex 3.3** $\dfrac{dy}{dt}=\dfrac{3t+ty^2}{y+t^2y}$, $y(1)=3$.
5. **Ex 3.4** $y\,dt+(t^3y^2+t^3)\,dy=0$.
6. **Pre-tut 3(a)** $\dfrac{dy}{dt}=-\dfrac ty$, $y(1)=2$.
7. **Pre-tut 3(b)** $3t(y^2+1)\,dt+y(t^2+2)\,dy=0$.
8. **Pre-tut 3(c)** $\dfrac{dy}{dt}=8ty+3y$.
9. **Theorem 3.2** When is there exactly one solution of $y^{\prime}=F(t,y)$ through a point?

<details><summary>Answers: Week 3</summary>

1. $\mu=(2t+5)^5$, $\;y=\tfrac56(2t+5)-\dfrac{5^7}{6(2t+5)^5}$
2. $i=10(1-e^{-5t})\,\mathrm{A}$
3. $\dfrac1y=\dfrac{1}{2t^2}-C$ (and $y=0$)
4. $y^2+3=6(t^2+1)$
5. $y^2+2\ln|y|-t^{-2}=C$
6. $t^2+y^2=5$, $\;y=\sqrt{5-t^2}$
7. $(t^2+2)^3(y^2+1)=C$
8. $y=Ce^{4t^2+3t}$
9. $F$ and $\partial F/\partial y$ continuous (finite) near the point. Sufficient, not necessary.

</details>

**Week 4** · [B3](#b3) · [B4](#b4)

1. **Ex 4.1** $(2ty+3t^2)\,dt+t^2\,dy=0$.
2. **(a)** $3t\,dt+4y\,dy=0$.
3. **(b)** $y^{\prime}=\dfrac{t-y}{t+y}$.
4. **(c)** $2ty\,y^{\prime}=t^2-y^2$.
5. **(d)** $y^{\prime}=\dfrac{t}{t+y}$: exact?
6. **(e) + Pre-tut 4** $y\,dt+(3+3t-y)\,dy=0$: find $\mu$, then solve.

<details><summary>Answers: Week 4</summary>

1. $t^2y+t^3=C$
2. $3t^2+4y^2=C$
3. $t^2-2ty-y^2=C$
4. $t^3-3ty^2=C$
5. No: $M_y=0\neq-1=N_t$.
6. $\mu=y^2$, $\;ty^3+y^3-\tfrac14y^4=C$

</details>

**Week 5** · [B5](#b5) · [D2](#d2) · [Topic C](#topic-c)

1. **§1** Parallel RLC: the characteristic equation and its three cases.
2. **Ex 5.2** Zero initial energy, $24\,\mathrm{mA}$ switched on, $400\,\Omega$, $25\,\mathrm{nF}$, $25\,\mathrm{mH}$. Find $i_L(t)$.
3. **Theorem 5.1** When does a linear $n$-th order ODE have exactly one solution?

<details><summary>Answers: Week 5</summary>

1. $s^2+\frac{1}{RC}s+\frac{1}{LC}=0$; $\alpha=\frac1{2RC}$ vs $\omega_0=\frac1{\sqrt{LC}}$: over / critical / under.
2. $i_L=24-32e^{-20\,000t}+8e^{-80\,000t}\ \mathrm{mA}$
3. Coefficients and right side continuous on the interval, and the top coefficient $a_0(t)\neq0$ there.

</details>

**Week 6** · [B6](#b6) · [B7](#b7)

1. **Lecture** $y^{\prime\prime}-ty^{\prime}+y=0$, $y_1=t$. Find the general solution.
2. **Pre-tut 5 = tutorial** $\ddot y+y=6\cos^2t$, $y(0)=0$, $y(\pi/2)=0$.

<details><summary>Answers: Week 6</summary>

1. $y=c_2t+c_1t\displaystyle\int\frac{e^{t^2/2}}{t^2}\,dt$
2. $y=3-\cos2t-4\sin t-2\cos t$

</details>
