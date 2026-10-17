# Week 5: Second-Order Linear ODEs and RLC Circuits

> **Info:** **Week 5 in one sentence:** an equation with $y''$, $y'$ and $y$ multiplied by constants is solved by guessing $y=e^{st}$, which turns calculus into a quadratic equation, and the RLC circuit is exactly this equation.
> 
> **By the end you can:**
> - solve $ay''+by'+cy=0$ in all three cases (two real roots, one repeated root, complex roots) and fit two initial conditions;
> - explain why two initial conditions give exactly one solution, test two solutions with the Wronskian, and find the interval where a solution is guaranteed;
> - write the ODE of a parallel or series RLC circuit and say whether it is overdamped, critically damped or underdamped;
> - find the natural response and the DC step response of an RLC circuit from $v_C(0)$ and $i_L(0)$.

> **Tip:** **What you need from earlier weeks**
> 
> - $j$ is the imaginary unit, $j^2=-1$, and **Euler's identity** $e^{j\theta}=\cos\theta+j\sin\theta$ (Week 1). It turns complex roots into cosines and sines.
> - Converting $a+jb$ to polar form $c\,e^{j\theta}$ with $c=\sqrt{a^2+b^2}$, $\tan\theta=b/a$ (Week 1).
> - Solving an IVP: find the general solution first, then use the initial condition to find the constant (Weeks 2–3). Now there are **two** constants and **two** conditions.
> - Capacitor and inductor laws: $i_C=C\,\dfrac{dv_C}{dt}$ and $v_L=L\,\dfrac{di_L}{dt}$ (Week 1 RL circuit).

## Topic 1: Second-order equations and the characteristic equation

A **second-order** ODE contains the second derivative $y''=\dfrac{d^2y}{dt^2}$. This week $a$, $b$, $c$ are plain numbers (*constant coefficients*) and the right side is $0$ (*homogeneous*: no source). We need a function whose derivatives look like the function itself, so that $ay''$, $by'$ and $cy$ can cancel to zero. The exponential $e^{st}$ does exactly that: each derivative is the same exponential times the number $s$. Substituting $y=e^{st}$ turns the ODE into an ordinary quadratic equation for $s$, called the **characteristic equation**. Its two roots decide the shape: a sum of two exponentials, an exponential times $(C_1+C_2t)$, or a decaying (or growing) cosine and sine. Use this whenever the equation has constant coefficients.

> **Info:** **Calculus reminder (derivative of an exponential):** if $s$ is a constant, $\dfrac{d}{dt}e^{st}=s\,e^{st}$ (chain rule: the derivative of the exponent $st$ is $s$). Differentiate again: $\dfrac{d^2}{dt^2}e^{st}=s^2e^{st}$. At $t=0$, $e^{0}=1$. And $e^{st}$ is never zero, so we may divide by it.
> 
> So for $y=e^{st}$: $ay''+by'+cy=as^2e^{st}+bse^{st}+ce^{st}=(as^2+bs+c)\,e^{st}$, which is zero exactly when $as^2+bs+c=0$.

> **Tip:** **The method**
> 
> 1. Write the ODE as $ay''+by'+cy=0$ and read off the numbers $a$, $b$, $c$.
> 2. Write the characteristic equation $as^2+bs+c=0$ (replace $y''\to s^2$, $y'\to s$, $y\to1$).
> 3. Solve it: factor, or use $s=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$.
> 4. Pick the general solution from the table below (the sign of $b^2-4ac$ decides the case).
> 5. For an IVP: differentiate the general solution, put $t=0$ into $y$ and $y'$, and solve the two equations for $C_1$ and $C_2$.

$$\begin{gathered}
y=e^{st}\ \Rightarrow\ (as^2+bs+c)\,e^{st}=0\\
as^2+bs+c=0\\
s_{1,2}=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
\end{gathered}$$

| Roots of $as^2+bs+c=0$ | General solution | Equations for $C_1,C_2$ | Shape |
|---|---|---|---|
| Two different real roots $s_1\neq s_2$ ($b^2-4ac>0$) | $y=C_1e^{s_1t}+C_2e^{s_2t}$ | $C_1+C_2=y(0)$, $s_1C_1+s_2C_2=y^{\prime}(0)$ | Sum of two exponentials; no wiggles |
| One repeated real root $s$ ($b^2-4ac=0$) | $y=(C_1+C_2t)\,e^{st}$ | $C_1=y(0)$, $sC_1+C_2=y^{\prime}(0)$ | Like the first row; the extra $t$ gives at most one hump |
| Complex pair $s=\sigma\pm j\omega$ ($b^2-4ac<0$) | $y=e^{\sigma t}(C_1\cos\omega t+C_2\sin\omega t)$ | $C_1=y(0)$, $\sigma C_1+\omega C_2=y^{\prime}(0)$ | Oscillates at $\omega$ rad/s inside the envelope $e^{\sigma t}$ |

**Example: Example 1 · Two real roots: the general solution**

Find the general solution of $y''-5y'+6y=0$.

1. Read off the coefficients: $a=1$, $b=-5$, $c=6$, and write the characteristic equation by replacing $y^{\prime\prime}$ with $s^2$, $y^{\prime}$ with $s$ and $y$ with $1$.

   $$s^2-5s+6=0$$
2. Factor it: we need two numbers that multiply to $6$ and add to $-5$, which are $-2$ and $-3$.

   $$(s-2)(s-3)=0\ \Rightarrow\ s_1=2,\ s_2=3$$
3. The roots are real and different, so the first row of the table applies: each root gives one exponential, and we add them with two free constants.

   $$y=C_1e^{2t}+C_2e^{3t}$$
4. Check one piece: for $y=e^{2t}$ we have $y^{\prime}=2e^{2t}$ and $y^{\prime\prime}=4e^{2t}$, so the left side is $(4-10+6)e^{2t}=0$. The same works for $e^{3t}$: $9-15+6=0$.

   $$(4-10+6)\,e^{2t}=0\ \checkmark$$

**Answer:** $y=C_1e^{2t}+C_2e^{3t}$

**Example: Example 2 · Two real roots: an initial value problem**

Solve $y''+3y'+2y=0$ with $y(0)=1$ and $y'(0)=0$.

1. Write the characteristic equation and factor it ($1\cdot2=2$ and $1+2=3$).

   $$s^2+3s+2=(s+1)(s+2)=0\ \Rightarrow\ s_1=-1,\ s_2=-2$$
2. Two different real roots give the general solution with two constants.

   $$y=C_1e^{-t}+C_2e^{-2t}$$
3. We also need $y^{\prime}$ because the second condition is about the slope; use $\frac{d}{dt}e^{st}=se^{st}$ on each term.

   $$y'=-C_1e^{-t}-2C_2e^{-2t}$$
4. Put $t=0$ in both (every $e^{0}=1$) and set them equal to the given values: this gives two equations for two unknowns.

   $$\begin{aligned}y(0)&=C_1+C_2=1\\ y'(0)&=-C_1-2C_2=0\end{aligned}$$
5. Add the two equations: $C_1$ cancels and leaves $-C_2=1$, so $C_2=-1$; then the first equation gives $C_1=1-C_2=2$.

   $$C_2=-1,\qquad C_1=2$$
6. Substitute the constants and check: $y(0)=2-1=1$ and $y^{\prime}(0)=-2+2=0$.

   $$y=2e^{-t}-e^{-2t}$$

**Answer:** $y=2e^{-t}-e^{-2t}$

> **Info:** **Calculus reminder (product rule):** $\dfrac{d}{dt}\big[f\,g\big]=f^{\prime}g+f\,g^{\prime}$. For $t\,e^{st}$ take $f=t$ ($f^{\prime}=1$) and $g=e^{st}$ ($g^{\prime}=se^{st}$):
> 
> $\dfrac{d}{dt}\big(t\,e^{st}\big)=1\cdot e^{st}+t\cdot s\,e^{st}=(1+st)\,e^{st}$.

**Example: Example 3 · Repeated root: why the extra t**

Solve $y''+4y'+4y=0$ with $y(0)=2$ and $y'(0)=-1$.

1. Write the characteristic equation; it is a perfect square, so there is only one root.

   $$s^2+4s+4=(s+2)^2=0\ \Rightarrow\ s=-2\ \text{(twice)}$$
2. One root gives only one exponential, $e^{-2t}$. The combination $C_1e^{-2t}+C_2e^{-2t}=(C_1+C_2)e^{-2t}$ is really one constant, and one constant cannot match two conditions (a value **and** a slope). We need a second, different solution: try $te^{-2t}$. By the product rule:

   $$y=te^{-2t},\quad y'=(1-2t)e^{-2t}$$
3. Differentiate once more (product rule again: derivative of $1-2t$ is $-2$) and substitute into the left side: everything cancels, so $te^{-2t}$ really is a solution.

   $$\begin{gathered}y''=(-4+4t)e^{-2t}\\ (-4+4t)+4(1-2t)+4t=0\ \checkmark\end{gathered}$$
4. So the general solution for a repeated root is $(C_1+C_2t)e^{st}$. Differentiate it with the product rule to get the slope.

   $$\begin{gathered}y=(C_1+C_2t)e^{-2t}\\ y'=C_2e^{-2t}-2(C_1+C_2t)e^{-2t}\end{gathered}$$
5. Put $t=0$: the first condition gives $C_1$ directly, then the second gives $C_2$.

   $$\begin{aligned}y(0)&=C_1=2\\ y'(0)&=C_2-2C_1=-1\ \Rightarrow\ C_2=3\end{aligned}$$
6. Put $C_1=2$ and $C_2=3$ back into $(C_1+C_2t)e^{-2t}$, then check both conditions: $y(0)=2$, and $y^{\prime}(0)=C_2-2C_1=3-4=-1$.

   $$y=(2+3t)\,e^{-2t}$$

**Answer:** $y=(2+3t)\,e^{-2t}$

> **Info:** **Algebra reminder (square root of a negative number):** $\sqrt{-16}=\sqrt{16}\,\sqrt{-1}=4j$, because $j=\sqrt{-1}$. So when $b^2-4ac<0$ the quadratic formula gives a complex pair
> 
> $s=\sigma\pm j\omega$ with $\sigma=-\dfrac{b}{2a}$ (sigma, the real part) and $\omega=\dfrac{\sqrt{4ac-b^2}}{2a}$ (omega, the imaginary part, always taken positive).
> 
> **Calculus reminder (sine and cosine):** $\dfrac{d}{dt}\cos\omega t=-\omega\sin\omega t$ and $\dfrac{d}{dt}\sin\omega t=\omega\cos\omega t$.

> **Info:** **Where the cosine and sine come from (complex roots)**
> 
> 1. Both roots work, so $e^{(\sigma+j\omega)t}$ and $e^{(\sigma-j\omega)t}$ are solutions (complex-valued ones).
> 2. Split each with $e^{x+y}=e^xe^y$: $e^{(\sigma\pm j\omega)t}=e^{\sigma t}\,e^{\pm j\omega t}$.
> 3. Euler's identity $e^{j\theta}=\cos\theta+j\sin\theta$ with $\theta=\pm\omega t$ gives $e^{\sigma t}(\cos\omega t\pm j\sin\omega t)$ (because $\cos(-x)=\cos x$ and $\sin(-x)=-\sin x$).
> 4. Sums and multiples of solutions are solutions (Topic 2). Half the sum is $e^{\sigma t}\cos\omega t$; the difference divided by $2j$ is $e^{\sigma t}\sin\omega t$. These two are **real** solutions.
> 5. So $y=e^{\sigma t}(C_1\cos\omega t+C_2\sin\omega t)$ with real constants: no $j$ is left in the answer.

**Example: Example 4 · Complex roots: a decaying oscillation**

Solve $y''+2y'+5y=0$ with $y(0)=1$ and $y'(0)=1$.

1. Write the characteristic equation; it does not factor nicely, so use the quadratic formula with $a=1$, $b=2$, $c=5$.

   $$s=\frac{-2\pm\sqrt{4-20}}{2}=\frac{-2\pm\sqrt{-16}}{2}$$
2. Use $\sqrt{-16}=4j$ and divide by $2$: the real part is $\sigma=-1$ and the imaginary part is $\omega=2$.

   $$s=\frac{-2\pm4j}{2}=-1\pm2j$$
3. Complex roots $\sigma\pm j\omega$ give the third row of the table with $\sigma=-1$, $\omega=2$.

   $$y=e^{-t}\left(C_1\cos2t+C_2\sin2t\right)$$
4. Differentiate with the product rule ($f=e^{-t}$, $g=C_1\cos2t+C_2\sin2t$, $g^{\prime}=-2C_1\sin2t+2C_2\cos2t$) and collect the cosine and sine terms.

   $$\begin{aligned}y'=e^{-t}\big[&(2C_2-C_1)\cos2t\\ &-(C_2+2C_1)\sin2t\big]\end{aligned}$$
5. Put $t=0$ into $y$ and $y^{\prime}$ (use $\cos0=1$, $\sin0=0$, $e^0=1$), so every sine term vanishes. The first equation gives $C_1=1$ directly; put it into the second: $-1+2C_2=1$, so $2C_2=2$.

   $$\begin{aligned}y(0)&=C_1=1\\ y'(0)&=-C_1+2C_2=1\ \Rightarrow\ C_2=1\end{aligned}$$
6. Put $C_1=C_2=1$ back into the general solution and check: $y(0)=1$ and $y^{\prime}(0)=2\cdot1-1=1$.

   $$y=e^{-t}\left(\cos2t+\sin2t\right)$$

**Answer:** $y=e^{-t}(\cos2t+\sin2t)$

> **Warning:** **Common mistakes**
> 
> - Writing $C_1e^{st}+C_2e^{st}$ for a repeated root. That is only one constant, $(C_1+C_2)e^{st}$; the second solution must be $t\,e^{st}$.
> - Leaving $j$ in the answer, e.g. $e^{(-1+2j)t}$, or using $\omega=2j$. The real answer uses only the numbers $\sigma=-1$ and $\omega=2$: $e^{-t}(C_1\cos2t+C_2\sin2t)$.
> - Setting $y^{\prime}(0)=C_2$. Differentiate first (product rule!), then put $t=0$: you get $sC_1+C_2$ (repeated root) or $\sigma C_1+\omega C_2$ (complex roots).
> - Dropping $a$: for $4y^{\prime\prime}+4y^{\prime}+y=0$ the characteristic equation is $4s^2+4s+1=0$, not $s^2+4s+1=0$.

**Problem: Try it 1 · General solution, two real roots** (introductory)

Find the general solution of $y''+y'-6y=0$.

<details><summary>Solution</summary>

1. Replace $y^{\prime\prime}\to s^2$, $y^{\prime}\to s$, $y\to1$ to get the characteristic equation.

   $$s^2+s-6=0$$
2. Factor: two numbers multiplying to $-6$ and adding to $1$ are $3$ and $-2$.

   $$(s+3)(s-2)=0\ \Rightarrow\ s_1=2,\ s_2=-3$$
3. Two different real roots: one exponential for each, with two constants.

   $$y=C_1e^{2t}+C_2e^{-3t}$$

**Answer:** $y=C_1e^{2t}+C_2e^{-3t}$

</details>

**Problem: Try it 2 · Pure oscillation** (introductory)

Solve $y''+9y=0$ with $y(0)=0$ and $y'(0)=6$. Does the solution ever die out?

<details><summary>Solution</summary>

1. Here $a=1$, $b=0$ (there is no $y^{\prime}$ term) and $c=9$, so the characteristic equation has no $s$ term.

   $$s^2+9=0\ \Rightarrow\ s^2=-9$$
2. Take the square root: $\sqrt{-9}=3j$, so the roots are purely imaginary: $\sigma=0$, $\omega=3$.

   $$s=\pm3j$$
3. With $\sigma=0$ the envelope is $e^{0t}=1$, so the general solution is a plain cosine and sine.

   $$y=C_1\cos3t+C_2\sin3t$$
4. Differentiate: $y^{\prime}=-3C_1\sin3t+3C_2\cos3t$. At $t=0$: $y(0)=C_1=0$ and $y^{\prime}(0)=3C_2=6$, so $C_2=2$.

   $$C_1=0,\quad C_2=2$$
5. The solution oscillates forever with amplitude $2$; there is no decay because there is no $y^{\prime}$ term (in a circuit: no resistor).

   $$y=2\sin3t$$

**Answer:** $y=2\sin3t$; it never dies out (amplitude stays $2$).

</details>

**Problem: Try it 3 · Repeated root IVP** (intermediate)

Solve $y''-6y'+9y=0$ with $y(0)=1$ and $y'(0)=5$.

<details><summary>Solution</summary>

1. The characteristic equation is a perfect square, so $s=3$ is a repeated root.

   $$s^2-6s+9=(s-3)^2=0$$
2. A repeated root needs the extra $t$: the general solution is $(C_1+C_2t)e^{3t}$.

   $$y=(C_1+C_2t)\,e^{3t}$$
3. Differentiate with the product rule: $f=C_1+C_2t$ has $f^{\prime}=C_2$, and $g=e^{3t}$ has $g^{\prime}=3e^{3t}$.

   $$y'=C_2e^{3t}+3(C_1+C_2t)e^{3t}$$
4. Put $t=0$ (so $e^0=1$ and the $C_2t$ term is $0$): $y(0)=C_1=1$, and $y^{\prime}(0)=C_2+3C_1=5$, so $C_2=5-3(1)=2$.

   $$C_1=1,\quad C_2=2$$
5. Put the constants back in and check: $y(0)=1$, $y^{\prime}(0)=2+3=5$.

   $$y=(1+2t)\,e^{3t}$$

**Answer:** $y=(1+2t)\,e^{3t}$

</details>

**Problem: Try it 4 · Leading coefficient not 1** (intermediate)

Solve $4y''+4y'+y=0$ with $y(0)=4$ and $y'(0)=0$.

<details><summary>Solution</summary>

1. Keep $a=4$ in the characteristic equation (do not drop it); the left side is a perfect square, since $(2s+1)^2=4s^2+4s+1$.

   $$4s^2+4s+1=(2s+1)^2=0$$
2. So $2s+1=0$ gives $s=-\tfrac12$ as a repeated root, and the solution needs the extra $t$.

   $$y=(C_1+C_2t)\,e^{-t/2}$$
3. Differentiate with the product rule: $f=C_1+C_2t$ has $f^{\prime}=C_2$, and $g=e^{-t/2}$ has $g^{\prime}=-\tfrac12e^{-t/2}$.

   $$y'=C_2e^{-t/2}-\tfrac12(C_1+C_2t)e^{-t/2}$$
4. At $t=0$: $y(0)=C_1=4$ and $y^{\prime}(0)=C_2-\tfrac12C_1=0$, so $C_2=\tfrac12(4)=2$.

   $$C_1=4,\quad C_2=2$$
5. Put the constants back in and check: $y(0)=4$, $y^{\prime}(0)=2-\tfrac12(4)=0$.

   $$y=(4+2t)\,e^{-t/2}$$

**Answer:** $y=(4+2t)\,e^{-t/2}$

</details>

**Problem: Try it 5 · Work backwards from a solution** (advanced)

One solution of $y''+by'+cy=0$ is $y=e^{-3t}\cos4t$.

1. Find $b$ and $c$.
2. Solve the same equation with $y(0)=0$ and $y'(0)=8$.

<details><summary>Solution</summary>

1. A solution $e^{\sigma t}\cos\omega t$ comes from the complex roots $\sigma\pm j\omega$, so here $\sigma=-3$, $\omega=4$.

   $$s=-3\pm4j$$
2. Rebuild the quadratic from its roots: $(s-s_1)(s-s_2)=(s+3-4j)(s+3+4j)=(s+3)^2-(4j)^2=(s+3)^2+16$.

   $$s^2+6s+25=0\ \Rightarrow\ b=6,\ c=25$$
3. The general solution is the complex-root row with $\sigma=-3$, $\omega=4$.

   $$y=e^{-3t}(C_1\cos4t+C_2\sin4t)$$
4. From the table, $y(0)=C_1$ and $y^{\prime}(0)=\sigma C_1+\omega C_2=-3C_1+4C_2$. The first condition gives $C_1=0$; put that into the second.

   $$C_1=0,\quad -3(0)+4C_2=8\ \Rightarrow\ C_2=2$$
5. Put $C_1=0$ and $C_2=2$ into the general solution; the cosine term drops out. Check: $y(0)=0$ and $y^{\prime}(0)=4\cdot2=8$.

   $$y=2e^{-3t}\sin4t$$

**Answer:** $b=6$, $c=25$; $y=2e^{-3t}\sin4t$

</details>

## Topic 2: Why two initial conditions give exactly one answer

Topic 1 gave a recipe; this topic explains why it is complete and when it can be trusted. **Superposition:** for a *linear homogeneous* equation ($y$, $y^{\prime}$, $y^{\prime\prime}$ appear only to the first power, multiplied by functions of $t$, and the right side is $0$), any sum of constant multiples of solutions is again a solution. **Wronskian:** two solutions $y_1$, $y_2$ give *every* solution as $C_1y_1+C_2y_2$ as long as they are *linearly independent*, meaning neither is just a constant multiple of the other; the Wronskian $W$ is a one-line test for this. **Existence and uniqueness:** a second-order equation needs two starting facts, the value $y(t_0)$ and the slope $y^{\prime}(t_0)$, just as an RLC circuit needs the capacitor voltage and the inductor current. With both given (and continuous coefficients) there is exactly one solution, so once our formula fits both conditions it **is** the answer.

> **Tip:** **The method**
> 
> *Is $C_1y_1+C_2y_2$ the general solution?*
> 1. Check that $y_1$ and $y_2$ each solve the equation (substitute).
> 2. Compute the Wronskian $W=y_1y_2^{\prime}-y_1^{\prime}y_2$. If $W\neq0$, then $C_1y_1+C_2y_2$ is the general solution. (For two solutions of the same equation, $W$ is either zero at every $t$ or at no $t$, so checking one convenient time such as $t=0$ is enough.)
> 
> *Where is the solution of an IVP guaranteed to exist (and be unique)?*
> 3. Divide by the coefficient of $y^{\prime\prime}$ to get the standard form $y^{\prime\prime}+p(t)\,y^{\prime}+q(t)\,y=g(t)$.
> 4. Mark every $t$ where $p$, $q$ or $g$ is not continuous (division by zero, $\ln$ of a number $\le0$, $\tan$ at $\pm\frac{\pi}{2},\pm\frac{3\pi}{2},\dots$).
> 5. The answer is the largest open interval that contains the starting time $t_0$ and none of the marked points.

$$W(y_1,y_2)=\begin{vmatrix}y_1&y_2\\ y_1'&y_2'\end{vmatrix}=y_1y_2'-y_1'y_2$$

> **Info:** **Existence and uniqueness theorem.** Consider $y^{\prime\prime}+p(t)\,y^{\prime}+q(t)\,y=g(t)$ with $y(t_0)=Y_0$ and $y^{\prime}(t_0)=Y_1$. If $p$, $q$ and $g$ are continuous on an open interval $I$ that contains $t_0$, then there is **exactly one** solution, and it exists on the **whole** interval $I$.
> 
> For Topic 1's equations $p=b/a$ and $q=c/a$ are constants and $g=0$: continuous everywhere. So the solutions we found are valid for all $t$ and are the only ones.

**Example: Example 5 · Superposition in action**

1. Show that $y_1=e^{2t}$ and $y_2=e^{3t}$ both solve $y''-5y'+6y=0$.
2. Without any new calculation, explain why $y=4e^{2t}-7e^{3t}$ is also a solution.
3. Why does this trick fail for $y''-5y'+6y=12$?

1. Substitute $y_1=e^{2t}$: $y_1^{\prime}=2e^{2t}$, $y_1^{\prime\prime}=4e^{2t}$.

   $$(4-10+6)\,e^{2t}=0\ \checkmark$$
2. Substitute $y_2=e^{3t}$: $y_2^{\prime}=3e^{3t}$, $y_2^{\prime\prime}=9e^{3t}$.

   $$(9-15+6)\,e^{3t}=0\ \checkmark$$
3. For $y=4y_1-7y_2$, the derivative of a sum is the sum of the derivatives and constants come out in front, so the left side splits into the two pieces we already know are zero.

   $$\begin{gathered}y''-5y'+6y\\=4\,(y_1''-5y_1'+6y_1)-7\,(y_2''-5y_2'+6y_2)\\=4\cdot0-7\cdot0=0\end{gathered}$$
4. With a right side of $12$, each solution makes the left side equal $12$, so $4y_1-7y_2$ would make it $4\cdot12-7\cdot12=-36\neq12$. Superposition needs the right side to be $0$ (homogeneous).

   $$4(12)-7(12)=-36\neq12$$

**Answer:** Both are solutions; $4e^{2t}-7e^{3t}$ is too (superposition). With right side $12$ it fails, because the equation is not homogeneous.

**Example: Example 6 · The Wronskian test: a good pair and a bad pair**

Compute the Wronskian and decide whether $C_1y_1+C_2y_2$ can be the general solution:

1. $y_1=e^{-t}$, $y_2=e^{-2t}$ (both solve $y''+3y'+2y=0$);
2. $y_1=e^{2t}$, $y_2=5e^{2t}$ (both solve $y''-4y'+4y=0$).

1. Pair 1: differentiate each function first: $y_1^{\prime}=-e^{-t}$ and $y_2^{\prime}=-2e^{-2t}$.

   $$y_1'=-e^{-t},\quad y_2'=-2e^{-2t}$$
2. Put them into $W=y_1y_2^{\prime}-y_1^{\prime}y_2$ and combine the exponentials with $e^{-t}e^{-2t}=e^{-3t}$.

   $$W=e^{-t}(-2e^{-2t})-(-e^{-t})e^{-2t}=-e^{-3t}$$
3. $-e^{-3t}$ is never zero, so the pair is independent and $C_1e^{-t}+C_2e^{-2t}$ is the general solution.

   $$W\neq0$$
4. Pair 2: $y_1^{\prime}=2e^{2t}$ and $y_2^{\prime}=10e^{2t}$, so the two products are equal and cancel.

   $$W=e^{2t}(10e^{2t})-(2e^{2t})(5e^{2t})=0$$
5. $W=0$ because $y_2$ is just $5y_1$: $C_1e^{2t}+5C_2e^{2t}=(C_1+5C_2)e^{2t}$ has only one real constant. It cannot fit, for example, $y(0)=1$ and $y^{\prime}(0)=0$ (that would need $K=1$ and $2K=0$).

   $$W=0\ \Rightarrow\ \text{not a general solution}$$

**Answer:** (1) $W=-e^{-3t}\neq0$: general solution. (2) $W=0$: $5e^{2t}$ is a multiple of $e^{2t}$, so this is not a general solution (the missing partner is $te^{2t}$).

**Example: Example 7 · Why the repeated-root recipe is complete**

For $y''+4y'+4y=0$ (Example 3), show that $y_1=e^{-2t}$ and $y_2=te^{-2t}$ have a nonzero Wronskian.

1. Differentiate: $y_1^{\prime}=-2e^{-2t}$, and by the product rule $y_2^{\prime}=(1-2t)e^{-2t}$.

   $$y_1'=-2e^{-2t},\quad y_2'=(1-2t)e^{-2t}$$
2. Substitute into $W=y_1y_2^{\prime}-y_1^{\prime}y_2$; every product contains $e^{-2t}e^{-2t}=e^{-4t}$.

   $$W=(1-2t)e^{-4t}+2t\,e^{-4t}$$
3. Expand the bracket: $(1-2t)+2t=1$, so the $-2t$ and $+2t$ cancel and only $e^{-4t}$ is left.

   $$W=e^{-4t}$$
4. $e^{-4t}$ is never zero, so $e^{-2t}$ and $te^{-2t}$ are independent and $(C_1+C_2t)e^{-2t}$ can fit any $y(0)$ and $y^{\prime}(0)$. By uniqueness, it gives the only solution.

   $$W=e^{-4t}\neq0$$

**Answer:** $W=e^{-4t}\neq0$, so $(C_1+C_2t)e^{-2t}$ is the general solution.

**Example: Example 8 · Largest interval: division by zero**

Find the largest interval on which the IVP is certain to have exactly one solution:

$(t^2-9)\,y''+t\,y'+4y=e^t$

1. with $y(1)=0$, $y'(1)=2$;
2. with $y(5)=1$, $y'(5)=0$.

1. Divide every term by the coefficient of $y^{\prime\prime}$, which is $t^2-9$, to reach standard form.

   $$y''+\frac{t}{t^2-9}\,y'+\frac{4}{t^2-9}\,y=\frac{e^t}{t^2-9}$$
2. Read off $p$, $q$, $g$. All three have $t^2-9$ downstairs, and $e^t$ is fine everywhere, so the only bad points are where $t^2-9=0$.

   $$t^2-9=0\ \Rightarrow\ t=-3,\ t=3$$
3. The marked points split the line into $(-\infty,-3)$, $(-3,3)$ and $(3,\infty)$. Part 1 starts at $t_0=1$, which lies in the middle piece.

   $$t_0=1\in(-3,\,3)$$
4. Part 2 starts at $t_0=5$, which lies in the right piece. The interval may not cross $t=3$, but nothing stops it on the right, so it runs to $\infty$.

   $$t_0=5\in(3,\,\infty)$$

**Answer:** (1) $-3<t<3$; (2) $t>3$.

**Example: Example 9 · Largest interval: several kinds of trouble**

Find the largest interval on which $(t-2)\,y''+y'+(t-2)(\tan t)\,y=0$, $y(3)=1$, $y'(3)=0$ is certain to have a unique solution.

1. Divide by $t-2$ (the coefficient of $y^{\prime\prime}$); in the last term the $(t-2)$ cancels.

   $$y''+\frac{1}{t-2}\,y'+(\tan t)\,y=0$$
2. $p=\dfrac{1}{t-2}$ breaks at $t=2$. $q=\tan t=\dfrac{\sin t}{\cos t}$ breaks where $\cos t=0$: $t=\pm\frac{\pi}{2}\approx\pm1.571$, $\pm\frac{3\pi}{2}\approx\pm4.712$, … $g=0$ is fine.

   $$t=2,\quad t=\tfrac{\pi}{2}+k\pi$$
3. Look left and right of $t_0=3$: the nearest bad point on the left is $2$ (because $\frac{\pi}{2}\approx1.57$ is further away), and on the right it is $\frac{3\pi}{2}\approx4.71$.

   $$2<3<\tfrac{3\pi}{2}$$
4. The guaranteed interval is the open stretch between these two nearest bad points; it contains $t_0=3$ and no bad point.

   $$2<t<\tfrac{3\pi}{2}$$

**Answer:** $2<t<\dfrac{3\pi}{2}\approx4.71$

> **Warning:** **Common mistakes**
> 
> - Reading the bad points before dividing by the coefficient of $y^{\prime\prime}$. The coefficient of $y^{\prime\prime}$ being zero is usually *the* bad point.
> - Giving an interval that does not contain $t_0$, or a closed interval like $[-3,3]$. The answer is open and must contain $t_0$.
> - Counting $e^{2t}$ and $5e^{2t}$ as two solutions. They are the same solution scaled ($W=0$) and cannot fit two conditions.
> - Using superposition on an equation with a nonzero right side (a source term). It only works for homogeneous equations.

**Problem: Try it 6 · A Wronskian with exponentials** (introductory)

Show that $e^{3t}$ and $e^{-3t}$ solve $y''-9y=0$, compute their Wronskian, and write the general solution.

<details><summary>Solution</summary>

1. Check each one by substituting: $(e^{3t})^{\prime\prime}=3^2e^{3t}=9e^{3t}$, so $y^{\prime\prime}-9y=9e^{3t}-9e^{3t}=0$; likewise $(e^{-3t})^{\prime\prime}=(-3)^2e^{-3t}=9e^{-3t}$ gives $0$.

   $$9-9=0\ \checkmark$$
2. Differentiate: $y_1^{\prime}=3e^{3t}$ and $y_2^{\prime}=-3e^{-3t}$. Put them into $W=y_1y_2^{\prime}-y_1^{\prime}y_2$ and use $e^{3t}e^{-3t}=e^0=1$, so each product is just a number.

   $$W=e^{3t}(-3e^{-3t})-3e^{3t}e^{-3t}=-3-3=-6$$
3. $W=-6$ is never zero, so the pair is independent and every solution is a combination of the two.

   $$y=C_1e^{3t}+C_2e^{-3t}$$

**Answer:** $W=-6$; $y=C_1e^{3t}+C_2e^{-3t}$

</details>

**Problem: Try it 7 · A Wronskian with cosine and sine** (introductory)

Compute the Wronskian of $y_1=\cos2t$ and $y_2=\sin2t$ (solutions of $y''+4y=0$). Is $C_1\cos2t+C_2\sin2t$ the general solution?

<details><summary>Solution</summary>

1. Differentiate each function (chain rule: the inside $2t$ brings out a factor $2$).

   $$y_1'=-2\sin2t,\quad y_2'=2\cos2t$$
2. Substitute into $W=y_1y_2^{\prime}-y_1^{\prime}y_2$: the first product is $\cos2t\cdot2\cos2t$ and the second is $(-2\sin2t)\sin2t$, which is subtracted, so its minus sign becomes plus.

   $$W=2\cos^2 2t+2\sin^2 2t$$
3. Factor out $2$ and use the identity $\cos^2x+\sin^2x=1$ with $x=2t$. $W=2$ is never zero, so the pair is independent.

   $$W=2(\cos^2 2t+\sin^2 2t)=2\neq0$$

**Answer:** $W=2\neq0$, so yes: $y=C_1\cos2t+C_2\sin2t$ is the general solution.

</details>

**Problem: Try it 8 · Largest interval with a source term** (intermediate)

Find the largest interval on which $(t+1)\,y''-t\,y'+y=\dfrac{1}{t-4}$, $y(0)=1$, $y'(0)=0$ has a unique solution.

<details><summary>Solution</summary>

1. Divide by $t+1$ to reach standard form; the right side picks up a second factor downstairs.

   $$y''-\frac{t}{t+1}\,y'+\frac{1}{t+1}\,y=\frac{1}{(t+1)(t-4)}$$
2. Mark the bad points (division by zero): $p$ and $q$ break at $t=-1$; $g$ breaks at $t=-1$ and at $t=4$.

   $$t=-1,\quad t=4$$
3. The start $t_0=0$ lies between $-1$ and $4$, so the largest open interval around it that avoids both bad points is:

   $$-1<t<4$$

**Answer:** $-1<t<4$

</details>

**Problem: Try it 9 · Logarithms and two starting points** (intermediate)

For $(t-1)\,y''+y'+y=\ln t$, find the largest interval on which a unique solution is guaranteed when the initial conditions are given at

1. $t_0=2$;
2. $t_0=\tfrac12$.

<details><summary>Solution</summary>

1. Divide every term by $t-1$, the coefficient of $y^{\prime\prime}$, to reach standard form.

   $$y''+\frac{1}{t-1}\,y'+\frac{1}{t-1}\,y=\frac{\ln t}{t-1}$$
2. Bad points: $t=1$ (division by zero) and every $t\le0$ ($\ln t$ is only defined for $t>0$).

   $$t\le0,\quad t=1$$
3. Starting at $t_0=2$: to the right there is no bad point, so the interval runs to $\infty$; to the left it must stop at $t=1$.

   $$1<t<\infty$$
4. Starting at $t_0=\tfrac12$: on the left it must stop at $0$ (where $\ln t$ stops existing) and on the right at $1$.

   $$0<t<1$$

**Answer:** (1) $t>1$; (2) $0<t<1$.

</details>

**Problem: Try it 10 · Uniqueness as a tool** (advanced)

1. Solve $y''+t\,y'+e^t\,y=0$ with $y(2)=0$ and $y'(2)=0$ (no formula needed).
2. Explain why $y=t^2$ cannot be a solution of any equation $y''+p(t)\,y'+q(t)\,y=0$ with $p$, $q$ continuous near $t=0$.

<details><summary>Solution</summary>

1. Part 1: the zero function $y=0$ satisfies the equation ($0+0+0=0$) and both conditions.

   $$y=0$$
2. $p=t$ and $q=e^t$ are continuous everywhere, so the theorem says there is only **one** solution. Since $y=0$ works, it is the solution.

   $$y(t)=0\ \text{for all } t$$
3. Part 2: $y=t^2$ has $y(0)=0$ and $y^{\prime}(0)=2\cdot0=0$, the same starting data as the zero function.

   $$y(0)=0,\quad y'(0)=0$$
4. If $t^2$ solved such an equation, uniqueness would force $t^2=0$ for all $t$ near $0$, which is false. So no such equation exists.

   $$t^2\not\equiv0$$

**Answer:** (1) $y=0$. (2) $t^2$ and $0$ share $y(0)=y^{\prime}(0)=0$, so uniqueness would force $t^2\equiv0$: impossible.

</details>

## Topic 3: RLC circuits

An RLC circuit stores energy in **two** places: the capacitor (through its voltage $v_C$) and the inductor (through its current $i_L$). Energy sloshes back and forth between them while the resistor turns some of it into heat, which is why the circuit gives a second-order ODE and why it can *ring*. KCL (parallel circuit) or KVL (series circuit), differentiated once, gives exactly Topic 1's equation, and the three root cases get circuit names: **overdamped** (two real roots), **critically damped** (repeated root) and **underdamped** (complex roots: a decaying oscillation). The two initial conditions come from the two storage elements, $V_0=v_C(0)$ and $I_0=i_L(0)$, which cannot jump at a switch. The *natural response* is what the circuit does with no source after $t=0$; the *step response* is the response to a constant (DC) source switched in at $t=0$.

> **Tip:** **The method** (Nilsson & Riedel, Chapter 8)
> 
> 1. Find $V_0=v_C(0^+)$ and $I_0=i_L(0^+)$ from the circuit before the switch (in DC steady state $C$ acts as an open circuit and $L$ as a wire); they do not jump. For a step response also find the final value $V_f$.
> 2. Compute $\alpha$ and $\omega_0$: parallel $\alpha=\dfrac{1}{2RC}$, series $\alpha=\dfrac{R}{2L}$; both $\omega_0=\dfrac{1}{\sqrt{LC}}$.
> 3. Compare: $\alpha>\omega_0$ overdamped (find $s_1,s_2$); $\alpha=\omega_0$ critically damped; $\alpha<\omega_0$ underdamped (find $\omega_d$).
> 4. Write the response form from the table (add $V_f$ for a step response).
> 5. Second condition: $\dfrac{dv_C}{dt}(0^+)=\dfrac{i_C(0^+)}{C}$ or $\dfrac{di_L}{dt}(0^+)=\dfrac{v_L(0^+)}{L}$, with $i_C(0^+)$ from KCL or $v_L(0^+)$ from KVL.
> 6. Solve the two equations for the two constants and check $t=0$.

$$\begin{gathered}
\text{parallel (KCL):}\\ \frac{d^2v}{dt^2}+\frac{1}{RC}\frac{dv}{dt}+\frac{v}{LC}=0\\[6pt]
\text{series (KVL):}\\ \frac{d^2i}{dt^2}+\frac{R}{L}\frac{di}{dt}+\frac{i}{LC}=0
\end{gathered}$$

$$\begin{gathered}
s^2+2\alpha s+\omega_0^2=0\\
s_{1,2}=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}\\
\omega_d=\sqrt{\omega_0^2-\alpha^2}
\end{gathered}$$

| Case | Test | Roots | Natural response | What it looks like |
|---|---|---|---|---|
| Overdamped | $\alpha>\omega_0$ | real: $s_1,s_2$ | $A_1e^{s_1t}+A_2e^{s_2t}$ | Slow return to zero, no ringing |
| Critically damped | $\alpha=\omega_0$ | repeated: $s=-\alpha$ | $D_1te^{-\alpha t}+D_2e^{-\alpha t}$ | No ringing; settles fastest of the non-ringing cases (in the long run) |
| Underdamped | $\alpha<\omega_0$ | $-\alpha\pm j\omega_d$ | $e^{-\alpha t}(B_1\cos\omega_dt+B_2\sin\omega_dt)$ | Rings at $\omega_d$ inside the envelope $e^{-\alpha t}$ |

> **Info:** **Symbols.** $\alpha$ (alpha) is the *neper frequency* in s$^{-1}$: how fast the envelope dies. $\omega_0$ (omega-zero) is the *resonant radian frequency* in rad/s: how fast the circuit would oscillate with no loss. $\omega_d$ (omega-d) is the *damped radian frequency*, the actual oscillation rate when underdamped. $A_1,A_2$, $B_1,B_2$, $D_1,D_2$ are the textbook's names for $C_1,C_2$ in each case. $V_0$ and $I_0$ are the starting capacitor voltage and inductor current. For a step response add the final value $V_f$ (the capacitor voltage long after the switch): $v_C=V_f+(\text{natural form})$. The textbook marks step-response constants with a prime, $A_1^{\prime}$, $B_1^{\prime}$, $D_1^{\prime}$: that prime is only a label, **not** a derivative.
> 
> **Circuit reminder (starting slopes):** from $i_C=C\,\dfrac{dv_C}{dt}$ we get $\dfrac{dv_C}{dt}(0^+)=\dfrac{i_C(0^+)}{C}$, and from $v_L=L\,\dfrac{di_L}{dt}$ we get $\dfrac{di_L}{dt}(0^+)=\dfrac{v_L(0^+)}{L}$. In the parallel circuit (all branch currents drawn downward) KCL gives $i_C(0^+)=-\dfrac{V_0}{R}-I_0$; in the series loop KVL gives $v_L(0^+)=-RI_0-V_0$.

**Example: Example 10 · Writing the parallel RLC equation**

The source-free parallel circuit below has $R=200\,\Omega$, $L=50\,\mathrm{mH}$ and $C=0.2\,\mu\mathrm{F}$. The voltage $v$ is $+$ at the top, and the branch currents $i_C$, $i_L$, $i_R$ are all drawn downward.

```schematic
C1 0,3 -> 0,0 "$0.2\,\mu\mathrm{F}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$50\,\mathrm{mH}$" i="$i_L$"
wire 3,3 -> 6,3
R1 6,3 -> 6,0 "$200\,\Omega$" i="$i_R$"
wire 6,0 -> 0,0
ground 0,0
```

1. Use KCL to write the second-order ODE for the voltage $v$.
2. Find $\alpha$, $\omega_0$ and the characteristic roots, and name the type of damping.

1. All three elements share the voltage $v$. KCL at the top node: the three currents leaving it (all drawn downward) add to zero. Write $i_C=C\dfrac{dv}{dt}$ and $i_R=\dfrac{v}{R}$; the inductor current $i_L$ cannot yet be written in terms of $v$.

   $$C\frac{dv}{dt}+i_L+\frac{v}{R}=0$$
2. Differentiate the whole equation once and replace $\dfrac{di_L}{dt}$ by $\dfrac{v}{L}$ (from the inductor law $v=L\,\dfrac{di_L}{dt}$). Now only $v$ appears.

   $$C\frac{d^2v}{dt^2}+\frac{v}{L}+\frac{1}{R}\frac{dv}{dt}=0$$
3. Divide by $C$ and order the derivatives: this is the parallel RLC equation, a Topic 1 equation with $a=1$, $b=\frac{1}{RC}$, $c=\frac{1}{LC}$.

   $$\frac{d^2v}{dt^2}+\frac{1}{RC}\frac{dv}{dt}+\frac{v}{LC}=0$$
4. Substitute $v=e^{st}$: the characteristic equation is $s^2+\frac{1}{RC}s+\frac{1}{LC}=0$. The textbook writes it as $s^2+2\alpha s+\omega_0^2=0$, so matching the $s$ terms gives $2\alpha=\frac{1}{RC}$ and matching the constants gives $\omega_0^2=\frac{1}{LC}$. This is where the formulas come from.

   $$\alpha=\frac{1}{2RC},\qquad \omega_0^2=\frac{1}{LC}$$
5. Put in the numbers: $\alpha=\dfrac{1}{2(200)(0.2\times10^{-6})}$ and $\omega_0^2=\dfrac{1}{(0.05)(0.2\times10^{-6})}$.

   $$\begin{gathered}\alpha=12\,500\ \mathrm{s^{-1}}\\ \omega_0=10\,000\ \mathrm{rad/s}\end{gathered}$$
6. Since $\alpha>\omega_0$, the number under the root in $s_{1,2}=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}$ is positive, so the roots are real and different: overdamped. Here $\sqrt{\alpha^2-\omega_0^2}=\sqrt{1.5625\times10^8-10^8}=7500$.

   $$s_{1,2}=-12\,500\pm7500$$
7. Take the $+$ sign for $s_1$ and the $-$ sign for $s_2$. Both are negative, so both exponentials decay.

   $$s_1=-5000,\quad s_2=-20\,000\ \mathrm{s^{-1}}$$

**Answer:** $v''+\dfrac{1}{RC}v'+\dfrac{1}{LC}v=0$; $\alpha=12\,500\ \mathrm{s^{-1}}$, $\omega_0=10^4$ rad/s, $s_1=-5000$, $s_2=-20\,000$: overdamped.

**Example: Example 11 · Overdamped parallel RLC (textbook 8.5)**

In the source-free parallel circuit below, $R=2\,\mathrm{k\Omega}$, $L=250\,\mathrm{mH}$ and $C=10\,\mathrm{nF}$. The initial inductor current is $I_0=i_L(0)=-30\,\mathrm{mA}$ (drawn downward, so it actually flows up) and the initial capacitor voltage is $V_0=v(0)=90\,\mathrm{V}$.

```schematic
C1 0,3 -> 0,0 "$10\,\mathrm{nF}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$250\,\mathrm{mH}$" i="$i_L$"
wire 3,3 -> 6,3
R1 6,3 -> 6,0 "$R$" i="$i_R$"
wire 6,0 -> 0,0
ground 0,0
```

1. Calculate the initial current in each branch.
2. Find $v(t)$ for $t\ge0$.
3. Find $i_L(t)$ for $t\ge0$.

1. All three branches have the voltage $v(0)=90$ V across them. Resistor: Ohm's law, $i_R=v/R$. Inductor: given. Capacitor: KCL at the top node, $i_C+i_L+i_R=0$, so $i_C=-i_R-i_L$.

   $$\begin{aligned}i_R(0)&=\tfrac{90}{2000}=45\ \mathrm{mA}\\ i_L(0)&=-30\ \mathrm{mA}\\ i_C(0)&=-45-(-30)=-15\ \mathrm{mA}\end{aligned}$$
2. Compute $\alpha=\dfrac{1}{2RC}$ (parallel circuit) and $\omega_0^2=\dfrac{1}{LC}$, with $C=10\,\mathrm{nF}=10^{-8}$ F and $L=250\,\mathrm{mH}=0.25$ H.

   $$\begin{gathered}\alpha=\frac{1}{2(2000)(10^{-8})}=25\,000\ \mathrm{s^{-1}}\\ \omega_0^2=\frac{1}{(0.25)(10^{-8})}=4\times10^{8}\end{gathered}$$
3. Compare: $\alpha^2=6.25\times10^8$ is bigger than $\omega_0^2=4\times10^8$, so the response is overdamped. Then $\sqrt{\alpha^2-\omega_0^2}=\sqrt{2.25\times10^8}=15\,000$ and $s_{1,2}=-25\,000\pm15\,000$.

   $$s_1=-10\,000,\quad s_2=-40\,000$$
4. Two real roots, so the response is a sum of two decaying exponentials (overdamped form) with unknown constants $A_1$, $A_2$.

   $$v=A_1e^{-10\,000t}+A_2e^{-40\,000t}$$
5. First equation: put $t=0$ (both exponentials become $1$); $v(0)$ must equal the capacitor voltage $V_0=90$ V.

   $$A_1+A_2=90$$
6. Second equation: differentiating gives $\dfrac{dv}{dt}=s_1A_1e^{s_1t}+s_2A_2e^{s_2t}$, which is $s_1A_1+s_2A_2$ at $t=0$. It must equal the starting slope $\dfrac{i_C(0)}{C}=\dfrac{-0.015}{10^{-8}}=-1.5\times10^6$ V/s.

   $$-10\,000A_1-40\,000A_2=-1.5\times10^6$$
7. Divide the second equation by $-10\,000$ to get $A_1+4A_2=150$. Subtract the first equation ($A_1+A_2=90$): $A_1$ cancels and $3A_2=60$, so $A_2=20$. Then $A_1=90-20=70$.

   $$A_2=20,\qquad A_1=70$$
8. Put the constants into the form. Check: $v(0)=70+20=90$ V.

   $$v(t)=70e^{-10\,000t}+20e^{-40\,000t}\ \mathrm{V}$$
9. For $i_L$ use KCL again, $i_L=-i_R-i_C=-\dfrac{v}{R}-C\dfrac{dv}{dt}$. Dividing $v$ by $2000$ gives $\dfrac{v}{R}=35e^{-10\,000t}+10e^{-40\,000t}$ mA. Differentiating $v$ and multiplying by $C=10^{-8}$ gives $C\dfrac{dv}{dt}=-7e^{-10\,000t}-8e^{-40\,000t}$ mA (for example $10^{-8}\cdot70\cdot(-10\,000)=-0.007$ A).

   $$i_L=-(35-7)e^{-10\,000t}-(10-8)e^{-40\,000t}$$
10. Collect the numbers. Check: $i_L(0)=-28-2=-30$ mA, the given starting current.

   $$i_L(t)=-28e^{-10\,000t}-2e^{-40\,000t}\ \mathrm{mA}$$

**Answer:** (1) $i_R=45$ mA, $i_L=-30$ mA, $i_C=-15$ mA. (2) $v=70e^{-10\,000t}+20e^{-40\,000t}$ V. (3) $i_L=-28e^{-10\,000t}-2e^{-40\,000t}$ mA.

**Example: Example 12 · Critically damped parallel RLC (textbook 8.6)**

The circuit of Example 11 has its resistance increased to $R=2.5\,\mathrm{k\Omega}$. Everything else is the same: $L=250\,\mathrm{mH}$, $C=10\,\mathrm{nF}$, $V_0=90\,\mathrm{V}$, $I_0=-30\,\mathrm{mA}$ (downward reference). Find $v(t)$ for $t\ge0$.

```schematic
C1 0,3 -> 0,0 "$10\,\mathrm{nF}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$250\,\mathrm{mH}$" i="$i_L$"
wire 3,3 -> 6,3
R1 6,3 -> 6,0 "$R$" i="$i_R$"
wire 6,0 -> 0,0
ground 0,0
```

1. Only $\alpha=\dfrac{1}{2RC}$ changes; $\omega_0=\dfrac{1}{\sqrt{LC}}=20\,000$ rad/s has no $R$ in it (from Example 11, $\omega_0^2=4\times10^8$).

   $$\alpha=\frac{1}{2(2500)(10^{-8})}=20\,000=\omega_0$$
2. $\alpha=\omega_0$: critically damped, with the repeated root $s=-\alpha=-20\,000$. A repeated root needs the extra $t$ (Topic 1).

   $$v=D_1te^{-20\,000t}+D_2e^{-20\,000t}$$
3. Starting slope: KCL gives $i_C(0)=-\dfrac{V_0}{R}-I_0=-\dfrac{90}{2500}-(-0.03)=-0.036+0.03=-0.006$ A, and $\dfrac{dv}{dt}(0^+)=\dfrac{i_C(0^+)}{C}$.

   $$\frac{dv}{dt}(0^+)=\frac{-0.006}{10^{-8}}=-6\times10^5\ \mathrm{V/s}$$
4. Put $t=0$ in the form: the $D_1t$ term vanishes, so $v(0)=D_2$. Differentiate with the product rule, $\dfrac{dv}{dt}=D_1e^{-\alpha t}-\alpha(D_1t+D_2)e^{-\alpha t}$, which is $D_1-\alpha D_2$ at $t=0$. Set both equal to the known values.

   $$\begin{aligned}v(0)&=D_2=90\\ D_1-\alpha D_2&=-6\times10^5\end{aligned}$$
5. The first equation gives $D_2=90$ directly. Move $-\alpha D_2$ to the right side of the second: $D_1=-6\times10^5+20\,000(90)=-6\times10^5+1.8\times10^6$.

   $$D_1=1.2\times10^6\ \mathrm{V/s}$$
6. Put $D_1$ and $D_2$ into the form and factor out $e^{-20\,000t}$. Check: $v(0)=90$ V.

   $$v(t)=(1.2\times10^6\,t+90)\,e^{-20\,000t}\ \mathrm{V}$$

**Answer:** $v(t)=(1.2\times10^{6}\,t+90)\,e^{-20\,000t}$ V, $t\ge0$

**Example: Example 13 · Underdamped parallel RLC (textbook 8.7)**

The circuit of Example 11 has its resistance increased to $R=\dfrac{12\,500}{3}\,\Omega\approx4.17\,\mathrm{k\Omega}$. Still $L=250\,\mathrm{mH}$, $C=10\,\mathrm{nF}$, $V_0=90\,\mathrm{V}$, $I_0=-30\,\mathrm{mA}$ (downward reference). Find $v(t)$ for $t\ge0$.

```schematic
C1 0,3 -> 0,0 "$10\,\mathrm{nF}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$250\,\mathrm{mH}$" i="$i_L$"
wire 3,3 -> 6,3
R1 6,3 -> 6,0 "$R$" i="$i_R$"
wire 6,0 -> 0,0
ground 0,0
```

1. Compute the new $\alpha=\dfrac{1}{2RC}$. Dividing by $R=\frac{12\,500}{3}$ is the same as multiplying by $\frac{3}{12\,500}$, so a $3$ moves to the top.

   $$\alpha=\frac{3}{2(12\,500)(10^{-8})}=12\,000\ \mathrm{s^{-1}}$$
2. $\alpha=12\,000$ is less than $\omega_0=20\,000$ (unchanged from Example 11): underdamped. The ringing frequency is $\omega_d=\sqrt{\omega_0^2-\alpha^2}$.

   $$\omega_d=\sqrt{4\times10^8-1.44\times10^8}=16\,000\ \mathrm{rad/s}$$
3. Complex roots $-\alpha\pm j\omega_d=-12\,000\pm j16\,000$ give the underdamped form (Topic 1 complex row with $\sigma=-\alpha$, $\omega=\omega_d$).

   $$v=e^{-12\,000t}(B_1\cos16\,000t+B_2\sin16\,000t)$$
4. Starting slope from KCL: $i_C(0)=-\dfrac{V_0}{R}-I_0=-\dfrac{90\cdot3}{12\,500}+0.03=-0.0216+0.03=0.0084$ A, and $\dfrac{dv}{dt}(0^+)=\dfrac{i_C(0^+)}{C}$.

   $$\frac{dv}{dt}(0^+)=\frac{0.0084}{10^{-8}}=8.4\times10^5\ \mathrm{V/s}$$
5. At $t=0$ the form gives $v(0)=B_1$ and (product rule, as in Example 4) $\dfrac{dv}{dt}(0)=-\alpha B_1+\omega_dB_2$. Set both equal to the known values.

   $$\begin{aligned}B_1&=90\\ -12\,000(90)+16\,000B_2&=8.4\times10^5\end{aligned}$$
6. Put $B_1=90$ into the second equation and move $-1.08\times10^6$ to the right: $16\,000B_2=8.4\times10^5+1.08\times10^6=1.92\times10^6$, then divide by $16\,000$.

   $$B_2=120$$
7. Put $B_1=90$ and $B_2=120$ into the form. Check: $v(0)=90$ V.

   $$v=e^{-12\,000t}(90\cos16\,000t+120\sin16\,000t)$$

**Answer:** $v(t)=e^{-12\,000t}\,(90\cos16\,000t+120\sin16\,000t)$ V, $t\ge0$

![Examples 11–13 on one plot (same $L$, $C$ and starting values; only $R$ changes). Overdamped (blue) creeps back to 0; critically damped (green) never crosses 0 and, in the long run, settles fastest of the non-ringing cases; underdamped (orange) overshoots and rings, with the swings shrinking inside $e^{-\alpha t}$. Time in milliseconds.](/figures/elec231/w5_damping.svg)

*Examples 11–13 on one plot (same $L$, $C$ and starting values; only $R$ changes). Overdamped (blue) creeps back to 0; critically damped (green) never crosses 0 and, in the long run, settles fastest of the non-ringing cases; underdamped (orange) overshoots and rings, with the swings shrinking inside $e^{-\alpha t}$. Time in milliseconds.*

**Example: Example 14 · Series RLC step response with a DC source (textbook 8.53)**

The series circuit below has been running for a long time with $v_s=200\,\mathrm{V}$. At $t=0$ the source voltage suddenly drops to $v_s=100\,\mathrm{V}$ and stays there. The elements are $4\,\Omega$, $40\,\mathrm{mH}$ and $10\,\mathrm{mF}$. The capacitor voltage $v_o$ is $+$ at the top, and the loop current $i$ flows from the source through $R$ and $L$ into the $+$ terminal of $C$. Find $v_o(t)$ for $t\ge0$.

```schematic
V1 0,3 -> 0,0 "$v_s$"
R1 0,3 -> 3,3 "$4\,\Omega$" i="$i$"
L1 3,3 -> 6,3 "$40\,\mathrm{mH}$"
C1 6,3 -> 6,0 "$10\,\mathrm{mF}$" v="$v_o$"
wire 6,0 -> 0,0
ground 0,0
```

1. Before $t=0$ (DC steady state) the capacitor is an open circuit, so $i=0$, the resistor and the inductor have no voltage, and the capacitor holds the whole $200\,\mathrm{V}$. These carry over to $t=0^+$.

   $$V_0=v_o(0^+)=200\ \mathrm{V},\quad I_0=i(0^+)=0$$
2. For $t>0$, KVL around the loop: the source voltage $100$ V equals the sum of the three element voltages, $Ri+L\dfrac{di}{dt}+v_o$. The loop current is the capacitor current, $i=C\dfrac{dv_o}{dt}$, so $Ri=RC\dfrac{dv_o}{dt}$ and $L\dfrac{di}{dt}=LC\dfrac{d^2v_o}{dt^2}$.

   $$100=RC\,v_o^{\prime}+LC\,v_o^{\prime\prime}+v_o$$
3. Divide by $LC=(0.04)(0.01)=4\times10^{-4}$: the same left side as before, but now with a constant on the right (the *constant impressed voltage*).

   $$v_o''+100\,v_o'+2500\,v_o=250\,000$$
4. Final value: a constant $v_o=V_f$ has zero derivatives, so $2500V_f=250\,000$, i.e. $V_f=100\,\mathrm{V}$ (the capacitor ends at the source voltage). The rest is the natural part.

   $$V_f=100\ \mathrm{V}$$
5. Series circuit: $\alpha=\dfrac{R}{2L}=\dfrac{4}{0.08}=50\ \mathrm{s^{-1}}$ and $\omega_0=\dfrac{1}{\sqrt{LC}}=\dfrac{1}{\sqrt{4\times10^{-4}}}=\dfrac{1}{0.02}=50$ rad/s. Equal, so critically damped (repeated root $s=-50$). Add the critically damped natural form to $V_f$; the primes on $D_1^{\prime}$, $D_2^{\prime}$ are only labels (step-response constants), not derivatives.

   $$v_o=100+D_1^{\prime}te^{-50t}+D_2^{\prime}e^{-50t}$$
6. First equation: at $t=0$ the $t$-term vanishes, so $v_o(0)=V_f+D_2^{\prime}$, which must equal $V_0=200$. Second: the starting slope is $\dfrac{dv_o}{dt}(0^+)=\dfrac{i(0^+)}{C}=\dfrac{I_0}{C}=0$, and the slope of the form at $0$ is $D_1^{\prime}-\alpha D_2^{\prime}$ (product rule, as in Example 12; the constant $100$ has zero slope).

   $$\begin{aligned}100+D_2'&=200\\ D_1'-50D_2'&=0\end{aligned}$$
7. The first equation gives $D_2^{\prime}=200-100=100$. Put it into the second: $D_1^{\prime}=50\cdot100=5000$.

   $$D_2'=100,\quad D_1'=5000$$
8. Substitute and check: $v_o(0)=100+100=200$ V and $v_o\to100$ V as $t\to\infty$.

   $$v_o(t)=100+(5000t+100)\,e^{-50t}\ \mathrm{V}$$

**Answer:** $v_o(t)=100+(5000t+100)\,e^{-50t}$ V, $t\ge0$

> **Warning:** **Common mistakes**
> 
> - Using the parallel $\alpha=\frac{1}{2RC}$ for a series circuit. Series: $\alpha=\frac{R}{2L}$. ($\omega_0=\frac{1}{\sqrt{LC}}$ is the same for both.)
> - Setting $\frac{dv}{dt}(0^+)=0$ because $v_C$ was constant before the switch. The slope at $0^+$ is $i_C(0^+)/C$, and $i_C$ *can* jump.
> - Losing the sign of $I_0$: with $i_L$ drawn downward, $I_0=-30$ mA means $-\frac{V_0}{R}-I_0=-\frac{V_0}{R}+0.03$.
> - Step response: forgetting $V_f$ in the first equation. It is $V_f+A_1^{\prime}+A_2^{\prime}=V_0$, not $A_1^{\prime}+A_2^{\prime}=V_0$.
> - Comparing $\alpha$ with $\omega_0^2$. Compare $\alpha$ with $\omega_0$ (or $\alpha^2$ with $\omega_0^2$).

**Problem: Try it 11 · Three resistors, three damping types** (introductory)

A series RLC circuit has $L=1\,\mathrm{H}$ and $C=2.5\,\mathrm{mF}$. For $R=50\,\Omega$, $R=40\,\Omega$ and $R=24\,\Omega$, find $\alpha$, the characteristic roots and the type of damping.

<details><summary>Solution</summary>

1. $\omega_0=\dfrac{1}{\sqrt{LC}}$ does not depend on $R$, so compute it once ($C=2.5\,\mathrm{mF}=0.0025$ F).

   $$\omega_0=\frac{1}{\sqrt{(1)(0.0025)}}=\frac{1}{0.05}=20\ \mathrm{rad/s}$$
2. Series circuit: $\alpha=\dfrac{R}{2L}=\dfrac{R}{2}$ because $L=1$, so the three resistors give:

   $$\alpha=25,\ 20,\ 12\ \mathrm{s^{-1}}$$
3. $R=50$: $\alpha=25>\omega_0=20$, overdamped. Use $s_{1,2}=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}$ with $\sqrt{625-400}=15$.

   $$s=-25\pm15=-10,\ -40$$
4. $R=40$: $\alpha=\omega_0=20$, so the square root is $0$ and $s=-\alpha$ twice: critically damped.

   $$s=-20\ \text{(twice)}$$
5. $R=24$: $\alpha=12<\omega_0$, underdamped. The roots are $-\alpha\pm j\omega_d$ with $\omega_d=\sqrt{\omega_0^2-\alpha^2}=\sqrt{400-144}=16$.

   $$s=-12\pm j16$$

**Answer:** $R=50$: $-10,-40$ (overdamped). $R=40$: $-20$ twice (critical). $R=24$: $-12\pm j16$ (underdamped).

</details>

**Problem: Try it 12 · Series RLC natural response** (intermediate)

In the source-free series circuit below, $R=60\,\Omega$, $L=0.1\,\mathrm{H}$, $C=40\,\mu\mathrm{F}$. At $t=0$ the capacitor voltage is $V_0=v_C(0)=50\,\mathrm{V}$ and the current is $I_0=i(0)=0$. The current $i$ flows through $R$ and $L$ into the $+$ terminal of $C$. Find $i(t)$ for $t\ge0$.

```schematic
wire 0,0 -> 0,3
R1 0,3 -> 3,3 "$60\,\Omega$" i="$i$"
L1 3,3 -> 6,3 "$0.1\,\mathrm{H}$"
C1 6,3 -> 6,0 "$40\,\mu\mathrm{F}$" v="$v_C$"
wire 6,0 -> 0,0
ground 0,0
```

<details><summary>Solution</summary>

1. KVL around the loop (no source, so the three element voltages add to zero): $Ri+L\dfrac{di}{dt}+v_C=0$. Differentiate once and use $\dfrac{dv_C}{dt}=\dfrac{i}{C}$ (capacitor law, since $i$ enters the $+$ terminal), then divide by $L$.

   $$i''+\frac{R}{L}\,i'+\frac{1}{LC}\,i=0$$
2. $\alpha=\dfrac{R}{2L}=\dfrac{60}{0.2}=300$ and $\omega_0^2=\dfrac{1}{(0.1)(40\times10^{-6})}=250\,000$, so $\omega_0=500$. Since $\alpha<\omega_0$ the circuit is underdamped.

   $$\omega_d=\sqrt{500^2-300^2}=400\ \mathrm{rad/s}$$
3. Complex roots $-300\pm j400$ give the underdamped form for the current.

   $$i=e^{-300t}(B_1\cos400t+B_2\sin400t)$$
4. First condition: $i(0)=B_1$ must equal $I_0=0$. Second: $\dfrac{di}{dt}(0^+)=\dfrac{v_L(0^+)}{L}$, where KVL at $t=0^+$ gives $v_L(0^+)=-RI_0-V_0=-60(0)-50=-50$ V.

   $$\frac{di}{dt}(0^+)=\frac{-50}{0.1}=-500\ \mathrm{A/s}$$
5. The slope of the form at $0$ is $-\alpha B_1+\omega_dB_2=-300(0)+400B_2$. Set it equal to $-500$ and divide by $400$.

   $$400B_2=-500\ \Rightarrow\ B_2=-1.25$$
6. Substitute. The minus sign means the current first flows against the drawn arrow: the capacitor discharges out of its $+$ terminal.

   $$i(t)=-1.25\,e^{-300t}\sin400t\ \mathrm{A}$$

**Answer:** $i(t)=-1.25\,e^{-300t}\sin400t$ A, $t\ge0$

</details>

**Problem: Try it 13 · Finding the peaks of a ringing voltage (textbook 8.13)** (intermediate)

In the source-free parallel circuit below, $R=2\,\Omega$, $C=250\,\mathrm{mF}$, $L=0.4\,\mathrm{H}$, $V_0=v(0)=0\,\mathrm{V}$ and $I_0=i_L(0)=-3\,\mathrm{A}$ (downward reference).

```schematic
C1 0,3 -> 0,0 "$250\,\mathrm{mF}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$0.4\,\mathrm{H}$" i="$i_L$"
wire 3,3 -> 6,3
R1 6,3 -> 6,0 "$2\,\Omega$" i="$i_R$"
wire 6,0 -> 0,0
ground 0,0
```

1. Find $v(t)$ for $t\ge0$.
2. Find the first three times $t_1<t_2<t_3$ at which $\dfrac{dv}{dt}=0$.
3. Show that $t_3-t_1=T_d$, the period of the oscillation, $T_d=\dfrac{2\pi}{\omega_d}$.
4. Show that $t_2-t_1=\dfrac{T_d}{2}$.
5. Calculate $v(t_1)$, $v(t_2)$ and $v(t_3)$.

<details><summary>Solution</summary>

1. Parallel circuit: $\alpha=\dfrac{1}{2RC}=\dfrac{1}{2(2)(0.25)}=1$ and $\omega_0^2=\dfrac{1}{LC}=\dfrac{1}{(0.4)(0.25)}=10$. Since $\alpha^2=1<\omega_0^2=10$, it is underdamped.

   $$\omega_d=\sqrt{\omega_0^2-\alpha^2}=\sqrt{10-1}=3\ \mathrm{rad/s}$$
2. Underdamped form: $v=e^{-t}(B_1\cos3t+B_2\sin3t)$. At $t=0$ it gives $v(0)=B_1$, which must equal $V_0=0$, so the cosine term drops out.

   $$v=B_2\,e^{-t}\sin3t$$
3. KCL (currents drawn downward): $i_C(0)=-\dfrac{V_0}{R}-I_0=0-(-3)=3$ A, so $\dfrac{dv}{dt}(0^+)=\dfrac{i_C(0^+)}{C}=\dfrac{3}{0.25}=12$ V/s. The form gives the slope $-\alpha B_1+\omega_dB_2=3B_2$ at $t=0$.

   $$3B_2=12\ \Rightarrow\ B_2=4$$
4. Put $B_2=4$ into the form:

   $$v(t)=4e^{-t}\sin3t\ \mathrm{V}$$
5. Product rule with $f=4e^{-t}$ ($f^{\prime}=-4e^{-t}$) and $g=\sin3t$ ($g^{\prime}=3\cos3t$): $\dfrac{dv}{dt}=4e^{-t}(3\cos3t-\sin3t)$. Since $e^{-t}$ is never zero, the slope is zero exactly when $\sin3t=3\cos3t$; divide by $\cos3t$ to get $\tan3t=3$.

   $$3t=\arctan3+k\pi=1.249+k\pi$$
6. The $+k\pi$ is there because $\tan$ repeats every $\pi$. Divide by $3$ and take $k=0,1,2$ for the first three positive times.

   $$t_1=0.416,\ t_2=1.464,\ t_3=2.511\ \mathrm{s}$$
7. Each step up in $k$ adds $\pi$ to $3t$, so it adds $\dfrac{\pi}{3}$ to $t$. Compare with the period $T_d=\dfrac{2\pi}{\omega_d}=\dfrac{2\pi}{3}$.

   $$\begin{gathered}t_3-t_1=\tfrac{2\pi}{3}=\tfrac{2\pi}{\omega_d}=T_d\\ t_2-t_1=\tfrac{\pi}{3}=\tfrac{T_d}{2}\end{gathered}$$
8. Put each time into $v=4e^{-t}\sin3t$. At every $t_k$, $\sin3t_k=\pm\dfrac{3}{\sqrt{10}}\approx\pm0.949$ (from $\tan3t=3$), with a minus sign at $t_2$, which is half a period later.

   $$\begin{aligned}v(t_1)&=4e^{-0.416}(0.949)\approx2.50\ \mathrm{V}\\ v(t_2)&=-4e^{-1.464}(0.949)\approx-0.878\ \mathrm{V}\\ v(t_3)&=4e^{-2.511}(0.949)\approx0.308\ \mathrm{V}\end{aligned}$$

**Answer:** (1) $v=4e^{-t}\sin3t$ V. (2) $t_1\approx0.416$ s, $t_2\approx1.464$ s, $t_3\approx2.511$ s. (3) $t_3-t_1=2\pi/3=T_d$. (4) $t_2-t_1=\pi/3=T_d/2$. (5) $v(t_1)\approx2.50$ V, $v(t_2)\approx-0.878$ V, $v(t_3)\approx0.308$ V.

</details>

**Problem: Try it 14 · No resistor: an LC circuit (textbook 8.14)** (intermediate)

The circuit of Try it 13 has its $2\,\Omega$ resistor removed, leaving $C=250\,\mathrm{mF}$ in parallel with $L=0.4\,\mathrm{H}$, with $v(0)=0$ and $i_L(0)=-3\,\mathrm{A}$ (downward reference).

```schematic
C1 0,3 -> 0,0 "$250\,\mathrm{mF}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$0.4\,\mathrm{H}$" i="$i_L$"
wire 3,0 -> 0,0
ground 0,0
```

1. Find $v(t)$ for $t\ge0$.
2. Calculate the frequency of $v(t)$ in rad/s.
3. Calculate the maximum amplitude of $v(t)$ in volts.

<details><summary>Solution</summary>

1. With no resistor the $\frac{1}{RC}$ term disappears ($R\to\infty$), so $\alpha=0$ and the equation is $v^{\prime\prime}+\frac{1}{LC}v=0$ with $\frac{1}{LC}=10$.

   $$v''+10v=0\ \Rightarrow\ s=\pm j\sqrt{10}$$
2. Purely imaginary roots: $v=B_1\cos\sqrt{10}t+B_2\sin\sqrt{10}t$, and $B_1=v(0)=0$.

   $$v=B_2\sin\sqrt{10}\,t$$
3. KCL with only two branches: $i_C(0)=-i_L(0)=3$ A, so $\dfrac{dv}{dt}(0)=\dfrac{3}{0.25}=12$ V/s $=\sqrt{10}\,B_2$.

   $$B_2=\frac{12}{\sqrt{10}}\approx3.795\ \mathrm{V}$$
4. The frequency is $\omega_0=\sqrt{10}$ and the amplitude is $B_2$; with no loss it never decays.

   $$v(t)=3.795\sin(3.162\,t)\ \mathrm{V}$$

**Answer:** (1) $v=\dfrac{12}{\sqrt{10}}\sin\sqrt{10}\,t\approx3.795\sin3.162t$ V. (2) $\sqrt{10}\approx3.162$ rad/s. (3) $3.795$ V.

</details>

**Problem: Try it 15 · Series step response with a switch (textbook 8.49 and 8.50)** (advanced)

The switch has been in position $a$ for a long time. At $t=0$ it moves to position $b$ (drawn as two switches: the one to $a$ opens and the one to $b$ closes at $t=0$).

```schematic
V1 0,3 -> 0,0 "$80\,\mathrm{V}$"
R1 0,3 -> 2,3 "$9\,\mathrm{k\Omega}$"
R2 2,3 -> 2,0 "$15\,\mathrm{k\Omega}$"
S1 2,3 -> 4,3 "$a$" action=open
C1 4,3 -> 4,0 "$2\,\mu\mathrm{F}$" v="$v_C$"
S2 6,3 -> 4,3 "$b$" action=close
R3 8,3 -> 6,3 "$80\,\Omega$" i="$i$"
L1 10,3 -> 8,3 "$5\,\mathrm{mH}$"
V2 10,3 -> 10,0 "$100\,\mathrm{V}$"
wire 10,0 -> 0,0
ground 0,0
```

1. Find $v_C(t)$ for $t\ge0$.
2. Find $i(t)$ for $t\ge0$ ($i$ flows from the $100\,\mathrm{V}$ source towards the capacitor).

<details><summary>Solution</summary>

1. Before $t=0$ the capacitor (an open circuit in DC) sits across the $15\,\mathrm{k\Omega}$ resistor of a voltage divider; the inductor branch is cut off by the open switch $b$.

   $$V_0=80\cdot\frac{15}{9+15}=50\ \mathrm{V},\quad I_0=0$$
2. After $t=0$ the loop is $100$ V, $5$ mH, $80\,\Omega$, $2\,\mu$F in series. KVL gives $100=Ri+L\dfrac{di}{dt}+v_C$ with $i=C\dfrac{dv_C}{dt}$, the same type of equation as Example 14. In the final DC state $C$ is open, so $i=0$, $R$ and $L$ have no voltage, and the capacitor holds the whole source voltage.

   $$V_f=100\ \mathrm{V}$$
3. Series: $\alpha=\dfrac{R}{2L}=\dfrac{80}{0.01}=8000$ and $\omega_0^2=\dfrac{1}{(0.005)(2\times10^{-6})}=10^8$, so $\omega_0=10\,000$: underdamped.

   $$\omega_d=\sqrt{10^8-6.4\times10^7}=6000$$
4. Step form: the final value plus the underdamped natural part (the primes on $B_1^{\prime}$, $B_2^{\prime}$ are labels, not derivatives).

   $$v_C=100+e^{-8000t}(B_1'\cos6000t+B_2'\sin6000t)$$
5. Two equations at $t=0$: the value is $V_f+B_1^{\prime}=V_0$, and the slope of the form, $-\alpha B_1^{\prime}+\omega_dB_2^{\prime}$, equals $\dfrac{dv_C}{dt}(0^+)=\dfrac{i(0^+)}{C}=\dfrac{I_0}{C}=0$. The first gives $B_1^{\prime}$; move $-\alpha B_1^{\prime}$ to the right in the second.

   $$\begin{aligned}B_1'&=50-100=-50\\ 6000B_2'&=8000(-50)\end{aligned}$$
6. Divide by $6000$: $B_2^{\prime}=-\frac{400\,000}{6000}=-\frac{200}{3}\approx-66.67$ V. Put $B_1^{\prime}$ and $B_2^{\prime}$ into the form and take the minus sign outside the bracket.

   $$v_C=100-e^{-8000t}(50\cos6000t+66.67\sin6000t)$$
7. The current $i$ flows into the $+$ terminal of $C$, so $i=C\dfrac{dv_C}{dt}$. Product rule on $-e^{-8000t}(\dots)$: the cosine parts are $8000(50)-6000(66.67)=0$ and the sine parts are $8000(66.67)+6000(50)=833\,333$, so $\dfrac{dv_C}{dt}=833\,333\,e^{-8000t}\sin6000t$ V/s.

   $$i=(2\times10^{-6})(833\,333)\,e^{-8000t}\sin6000t$$
8. Multiply $2\times10^{-6}\cdot833\,333\approx1.667$. Check: $i(0)=0=I_0$, as it must be for an inductor current.

   $$i(t)=1.667\,e^{-8000t}\sin6000t\ \mathrm{A}$$

**Answer:** (1) $v_C=100-e^{-8000t}(50\cos6000t+66.67\sin6000t)$ V. (2) $i=1.667\,e^{-8000t}\sin6000t$ A, $t\ge0$.

</details>

## Mixed practice (exam style)

Mixed topics, like the midterm. Try each one before opening the solution.

**Problem: Practice 1 · Repeated root, peak and interval** (introductory)

Consider $y''+6y'+9y=0$ with $y(0)=0$ and $y'(0)=2$.

1. Solve the IVP.
2. On what interval is the solution valid, and why is it the only one?
3. Find the largest value of $y$ for $t\ge0$.

<details><summary>Solution</summary>

1. The characteristic equation is $s^2+6s+9=(s+3)^2=0$, so $s=-3$ is a repeated root and the solution needs the extra $t$.

   $$y=(C_1+C_2t)\,e^{-3t}$$
2. From the table: $C_1=y(0)=0$, and $sC_1+C_2=y^{\prime}(0)$ becomes $-3(0)+C_2=2$, so $C_2=2$.

   $$y=2t\,e^{-3t}$$
3. Constant coefficients ($p=6$, $q=9$, $g=0$) are continuous everywhere, so the theorem gives exactly one solution on all of $(-\infty,\infty)$.

   $$-\infty<t<\infty$$
4. Peak: by the product rule $y^{\prime}=2e^{-3t}-6te^{-3t}=2e^{-3t}(1-3t)$, which is zero only at $t=\tfrac13$. Before that $y^{\prime}>0$ (rising), after it $y^{\prime}<0$ (falling), so $t=\tfrac13$ is the maximum.

   $$t=\tfrac13$$
5. Put $t=\tfrac13$ into $y=2te^{-3t}$; the exponent becomes $-3\cdot\tfrac13=-1$.

   $$y_{\max}=2\cdot\tfrac13\,e^{-1}=\frac{2}{3e}\approx0.245$$

**Answer:** (1) $y=2te^{-3t}$. (2) All $t$; constant coefficients are continuous. (3) $y_{\max}=\frac{2}{3e}\approx0.245$ at $t=\frac13$.

</details>

**Problem: Practice 2 · One equation, every case** (intermediate)

Consider $y''+2y'+ky=0$, where $k$ is a constant.

1. For which values of $k$ are the roots real and different, repeated, or complex?
2. Solve the equation for $k=10$ with $y(0)=0$ and $y'(0)=6$.

<details><summary>Solution</summary>

1. The characteristic equation is $s^2+2s+k=0$ ($a=1$, $b=2$, $c=k$). The case is decided by the discriminant, the number under the square root in the quadratic formula.

   $$b^2-4ac=4-4k$$
2. $4-4k$ is positive when $k<1$, zero when $k=1$, negative when $k>1$.

   $$\begin{gathered}k<1:\ \text{real, different}\\ k=1:\ \text{repeated}\\ k>1:\ \text{complex}\end{gathered}$$
3. For $k=10$: $s=\dfrac{-2\pm\sqrt{4-40}}{2}=\dfrac{-2\pm\sqrt{-36}}{2}$, and $\sqrt{-36}=6j$.

   $$s=\frac{-2\pm6j}{2}=-1\pm3j$$
4. Complex form with $\sigma=-1$, $\omega=3$: $y=e^{-t}(C_1\cos3t+C_2\sin3t)$. From the table, $C_1=y(0)=0$ and $\sigma C_1+\omega C_2=-1(0)+3C_2=6$.

   $$C_1=0,\quad C_2=2$$
5. Put the constants into the form; the cosine term drops out. Check: $y(0)=0$ and $y^{\prime}(0)=3\cdot2=6$.

   $$y=2e^{-t}\sin3t$$

**Answer:** (1) $k<1$ real and different, $k=1$ repeated, $k>1$ complex. (2) $y=2e^{-t}\sin3t$.

</details>

**Problem: Practice 3 · Amplitude and phase with complex numbers** (intermediate)

1. Solve $y''+2y'+5y=0$ with $y(0)=3$ and $y'(0)=5$.
2. Write your answer in the form $A\,e^{-t}\cos(2t-\varphi)$ using the polar form of $3+j4$ (Week 1).

<details><summary>Solution</summary>

1. The characteristic equation $s^2+2s+5=0$ has roots $s=\dfrac{-2\pm\sqrt{4-20}}{2}=\dfrac{-2\pm4j}{2}=-1\pm2j$, so $\sigma=-1$, $\omega=2$ (same as Example 4).

   $$y=e^{-t}(C_1\cos2t+C_2\sin2t)$$
2. From the table, $C_1=y(0)=3$. Then $\sigma C_1+\omega C_2=-3+2C_2$ must equal $y^{\prime}(0)=5$, so $2C_2=8$ and $C_2=4$.

   $$y=e^{-t}(3\cos2t+4\sin2t)$$
3. Expand the target: $A\cos(2t-\varphi)=A\cos\varphi\cos2t+A\sin\varphi\sin2t$. Matching needs $A\cos\varphi=3$ and $A\sin\varphi=4$, which is exactly the polar form of $3+j4$.

   $$3+j4=A\,e^{j\varphi}$$
4. Find the magnitude $A=\sqrt{a^2+b^2}$ and the angle $\varphi=\arctan\frac{b}{a}$ (Week 1). The angle is in the first quadrant because both parts, $3$ and $4$, are positive.

   $$A=\sqrt{3^2+4^2}=5,\quad \varphi=\arctan\tfrac43\approx0.927$$
5. So the solution is one cosine of amplitude $5$ inside the envelope $e^{-t}$.

   $$y=5e^{-t}\cos(2t-0.927)$$

**Answer:** (1) $y=e^{-t}(3\cos2t+4\sin2t)$. (2) $y=5e^{-t}\cos(2t-0.927)$, with $\varphi\approx0.927$ rad $=53.1^\circ$.

</details>

**Problem: Practice 4 · Working backwards from v(t) (textbook 8.2)** (intermediate)

The natural response of the source-free parallel circuit below is known to be $v(t)=-12\left(e^{-200t}+e^{-1800t}\right)\,\mathrm{V}$ for $t\ge0$. If $C=18\,\mu\mathrm{F}$, find $i_L(0^+)$ in milliamperes ($i_L$ drawn downward).

```schematic
C1 0,3 -> 0,0 "$18\,\mu\mathrm{F}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$L$" i="$i_L$"
wire 3,3 -> 6,3
R1 6,3 -> 6,0 "$R$" i="$i_R$"
wire 6,0 -> 0,0
ground 0,0
```

<details><summary>Solution</summary>

1. Each exponent in $v(t)$ is a root of the characteristic equation: $s_1=-200$, $s_2=-1800$. Rebuild the equation from its roots, $(s-s_1)(s-s_2)$, and compare with the parallel form $s^2+\frac{1}{RC}s+\frac{1}{LC}$.

   $$(s+200)(s+1800)=s^2+2000s+360\,000$$
2. Matching the $s$ terms gives $\frac{1}{RC}=2000$; solve for $R$ with $C=18\times10^{-6}$ F.

   $$R=\frac{1}{2000\,(18\times10^{-6})}\approx27.78\ \Omega$$
3. Starting values from the given formula: $v(0)=-12(1+1)=-24$ V, and differentiating, $\frac{dv}{dt}=-12(-200e^{-200t}-1800e^{-1800t})$, so $\frac{dv}{dt}(0)=-12(-2000)=24\,000$ V/s.

   $$v(0)=-24\ \mathrm{V},\quad \frac{dv}{dt}(0)=24\,000\ \mathrm{V/s}$$
4. Capacitor current from $i_C=C\dfrac{dv}{dt}=(18\times10^{-6})(24\,000)$; resistor current from Ohm's law, $i_R=\dfrac{v}{R}=\dfrac{-24}{27.78}$ (exactly $-24\cdot2000\cdot18\times10^{-6}$, since $\frac{1}{R}=2000C$).

   $$\begin{aligned}i_C&=0.432\ \mathrm{A}\\ i_R&=-0.864\ \mathrm{A}\end{aligned}$$
5. KCL at the top node (all currents drawn downward): $i_C+i_L+i_R=0$, so $i_L=-i_C-i_R=-0.432+0.864$.

   $$i_L(0^+)=0.864-0.432=0.432\ \mathrm{A}$$

**Answer:** $i_L(0^+)=432$ mA

</details>

**Problem: Practice 5 · Critical damping and stored energy (textbook 8.4)** (advanced)

In the source-free parallel circuit below, a $5\,\mathrm{H}$ inductor is shunted by an $8\,\mathrm{nF}$ capacitor, the resistor $R$ is adjusted for critical damping, $V_0=v(0)=-25\,\mathrm{V}$ and $I_0=i_L(0)=-1\,\mathrm{mA}$ (downward reference).

```schematic
C1 0,3 -> 0,0 "$8\,\mathrm{nF}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$5\,\mathrm{H}$" i="$i_L$"
wire 3,3 -> 6,3
R1 6,3 -> 6,0 "$R$" i="$i_R$"
wire 6,0 -> 0,0
ground 0,0
```

1. Calculate $R$.
2. Calculate $v(t)$ for $t\ge0$.
3. Find $v(t)$ when $i_C(t)=0$.
4. What percentage of the initially stored energy remains stored in the circuit at the instant $i_C(t)$ is $0$?

<details><summary>Solution</summary>

1. Critical damping means $\alpha=\omega_0$. First $\omega_0=\dfrac{1}{\sqrt{5\cdot8\times10^{-9}}}=\dfrac{1}{2\times10^{-4}}=5000$; then solve $\dfrac{1}{2RC}=5000$ for $R$.

   $$R=\frac{1}{2(8\times10^{-9})(5000)}=12.5\ \mathrm{k\Omega}$$
2. Critically damped form: $v=D_1te^{-5000t}+D_2e^{-5000t}$, so $v(0)=D_2$ and (product rule) $\dfrac{dv}{dt}(0)=D_1-\alpha D_2$. Starting slope from KCL: $i_C(0)=-\dfrac{V_0}{R}-I_0=\dfrac{25}{12\,500}+0.001=0.003$ A, so $\dfrac{dv}{dt}(0^+)=\dfrac{0.003}{8\times10^{-9}}=375\,000$ V/s.

   $$\begin{aligned}D_2&=V_0=-25\\ D_1-\alpha D_2&=375\,000\end{aligned}$$
3. Move $-\alpha D_2$ to the right: $D_1=375\,000+\alpha D_2=375\,000+5000(-25)=250\,000$. Put $D_1$, $D_2$ into the form.

   $$v(t)=(250\,000\,t-25)\,e^{-5000t}\ \mathrm{V}$$
4. $i_C=C\frac{dv}{dt}$ is zero exactly when $\frac{dv}{dt}=0$. Product rule: $\frac{dv}{dt}=e^{-5000t}\left[250\,000-5000(250\,000t-25)\right]=e^{-5000t}(375\,000-1.25\times10^9t)$. Since $e^{-5000t}\neq0$, set the bracket to zero.

   $$t=\frac{375\,000}{1.25\times10^9}=3\times10^{-4}\ \mathrm{s}=300\ \mu\mathrm{s}$$
5. Put $t=3\times10^{-4}$ into $v(t)$: $250\,000\,t=75$ and $5000t=1.5$.

   $$v=(75-25)e^{-1.5}=50e^{-1.5}\approx11.16\ \mathrm{V}$$
6. Initial stored energy (capacitor $\frac12Cv^2$ plus inductor $\frac12Li_L^2$): $\frac12(8\times10^{-9})(-25)^2+\frac12(5)(-10^{-3})^2=2.5+2.5\ \mu\mathrm{J}$.

   $$w(0)=5\ \mu\mathrm{J}$$
7. At $300\,\mu$s, $i_C=0$, so KCL ($i_C+i_L+i_R=0$) gives $i_L=-i_R=-\frac{v}{R}=-\frac{11.16}{12\,500}=-0.893$ mA. Add the two stored energies.

   $$\begin{gathered}w=\tfrac12C v^2+\tfrac12L i_L^2\\ \approx0.498+1.991=2.489\ \mu\mathrm{J}\end{gathered}$$
8. Divide the energy still stored by the initial energy and convert to a percentage (the rest has been turned into heat in $R$).

   $$\frac{2.489}{5}\approx0.498=49.8\%$$

**Answer:** (1) $R=12.5$ k$\Omega$. (2) $v=(250\,000t-25)e^{-5000t}$ V. (3) at $t=300\,\mu$s, $v\approx11.16$ V. (4) about $49.8\%$.

</details>

**Problem: Practice 6 · Finding R and L from the current (textbook 8.39)** (intermediate)

In the source-free series circuit below, the current is known to be $i=B_1e^{-800t}\cos600t+B_2e^{-800t}\sin600t$ for $t\ge0$. The capacitor is $500\,\mu\mathrm{F}$, the initial current is zero and the initial capacitor voltage is $v_C(0)=12\,\mathrm{V}$. The current $i$ flows through $R$ and $L$ into the $+$ terminal of $C$. Find $R$, $L$, $B_1$ and $B_2$.

```schematic
wire 0,0 -> 0,3
R1 0,3 -> 3,3 "$R$" i="$i$"
L1 3,3 -> 6,3 "$L$"
C1 6,3 -> 6,0 "$500\,\mu\mathrm{F}$" v="$v_C$"
wire 6,0 -> 0,0
ground 0,0
```

<details><summary>Solution</summary>

1. Read the roots off the given form: the envelope gives $\alpha=800$ and the oscillation gives $\omega_d=600$. Since $\omega_d^2=\omega_0^2-\alpha^2$:

   $$\omega_0^2=800^2+600^2=10^6$$
2. $\omega_0^2=\dfrac{1}{LC}$ gives $L$; then the series $\alpha=\dfrac{R}{2L}$ gives $R$.

   $$\begin{gathered}L=\frac{1}{10^6(5\times10^{-4})}=2\ \mathrm{mH}\\ R=2(800)(0.002)=3.2\ \Omega\end{gathered}$$
3. First condition: at $t=0$ the form gives $i(0)=B_1$, and the initial current is zero.

   $$B_1=0$$
4. Second: KVL at $t=0^+$ gives $v_L(0^+)=-RI_0-V_0=-0-12=-12$ V, so $\dfrac{di}{dt}(0^+)=\dfrac{v_L(0^+)}{L}=\dfrac{-12}{0.002}=-6000$ A/s. The form gives the slope $-\alpha B_1+\omega_dB_2=600B_2$ at $t=0$.

   $$600B_2=-6000\ \Rightarrow\ B_2=-10\ \mathrm{A}$$

**Answer:** $R=3.2\,\Omega$, $L=2$ mH, $B_1=0$, $B_2=-10$ A, so $i=-10e^{-800t}\sin600t$ A.

</details>

**Problem: Practice 7 · From two exponentials to a circuit** (advanced)

The functions $y_1=e^{-t}$ and $y_2=e^{-4t}$ both solve an equation $y''+by'+cy=0$.

1. Find $b$ and $c$.
2. Compute the Wronskian of $y_1$, $y_2$. What does it tell you?
3. Solve the IVP with $y(0)=0$, $y'(0)=3$.
4. The answer to part 3 is the current $i(t)$ (in A) of a source-free series RLC circuit with $L=1\,\mathrm{H}$, $i(0)=0$, and $i$ flowing into the $+$ terminal of the capacitor. Find $R$, $C$ and the initial capacitor voltage $V_0$.

<details><summary>Solution</summary>

1. A solution $e^{st}$ means $s$ is a root, so the roots are $-1$ and $-4$. Rebuild the characteristic equation from them, $(s-s_1)(s-s_2)$, and read off $b$ and $c$.

   $$(s+1)(s+4)=s^2+5s+4\Rightarrow b=5,\ c=4$$
2. Differentiate: $y_1^{\prime}=-e^{-t}$, $y_2^{\prime}=-4e^{-4t}$. Put them into $W=y_1y_2^{\prime}-y_1^{\prime}y_2$ and use $e^{-t}e^{-4t}=e^{-5t}$.

   $$W=-4e^{-5t}+e^{-5t}=-3e^{-5t}\neq0$$
3. $W$ is never zero, so the pair is independent and $y=C_1e^{-t}+C_2e^{-4t}$ is the general solution. Its slope is $y^{\prime}=-C_1e^{-t}-4C_2e^{-4t}$. At $t=0$: $C_1+C_2=0$ and $-C_1-4C_2=3$. The first gives $C_2=-C_1$; put it into the second: $-C_1+4C_1=3$, so $3C_1=3$.

   $$C_1=1,\ C_2=-1\ \Rightarrow\ y=e^{-t}-e^{-4t}$$
4. Match the series equation $i^{\prime\prime}+\frac{R}{L}i^{\prime}+\frac{1}{LC}i=0$ with $b=5$, $c=4$ and $L=1$: $\frac{R}{1}=5$ and $\frac{1}{1\cdot C}=4$.

   $$R=5\ \Omega,\quad C=\tfrac14\ \mathrm{F}$$
5. Initial slope from KVL at $t=0^+$: $\frac{di}{dt}(0^+)=\frac{v_L(0^+)}{L}=\frac{-RI_0-V_0}{L}=\frac{-5(0)-V_0}{1}=-V_0$. Part 3 says the slope is $y^{\prime}(0)=3$, so $-V_0=3$.

   $$V_0=-3\ \mathrm{V}$$

**Answer:** (1) $b=5$, $c=4$. (2) $W=-3e^{-5t}\neq0$: independent. (3) $y=e^{-t}-e^{-4t}$. (4) $R=5\,\Omega$, $C=0.25$ F, $V_0=-3$ V.

</details>

## Summary

| Problem type | How to recognise it | What to do |
|---|---|---|
| Solve $ay^{\prime\prime}+by^{\prime}+cy=0$ | Constant numbers in front of $y^{\prime\prime}$, $y^{\prime}$, $y$; right side $0$ | Characteristic equation $as^2+bs+c=0$; pick the form from the roots (real / repeated / complex) |
| Second-order IVP | Two conditions: $y(0)$ and $y^{\prime}(0)$ | Differentiate the general solution, set $t=0$ in $y$ and $y^{\prime}$, solve the 2×2 system |
| Is $C_1y_1+C_2y_2$ general? | Two solutions given | $W=y_1y_2^{\prime}-y_1^{\prime}y_2\neq0$ means yes |
| Largest interval of existence | Coefficients depend on $t$; a start time $t_0$ is given | Divide by the $y^{\prime\prime}$ coefficient; mark bad points of $p,q,g$; open interval around $t_0$ |
| Parallel RLC natural response | R, L, C side by side, no source after $t=0$ | $\alpha=\frac{1}{2RC}$, $\omega_0=\frac{1}{\sqrt{LC}}$; $v(0)=V_0$, $\frac{dv}{dt}(0^+)=\frac{1}{C}\left(-\frac{V_0}{R}-I_0\right)$ |
| Series RLC natural response | R, L, C in one loop, no source | $\alpha=\frac{R}{2L}$; $i(0)=I_0$, $\frac{di}{dt}(0^+)=\frac{1}{L}(-RI_0-V_0)$ |
| Series RLC step response | A constant (DC) source in the loop from $t=0$ | $v_C=V_f+$ natural form, $V_f=$ source voltage; $V_f+(\cdot)=V_0$, $\frac{dv_C}{dt}(0^+)=\frac{I_0}{C}$ |

| Quantity | Formula |
|---|---|
| Characteristic roots | $s=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$, or $s=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}$ |
| Distinct / repeated / complex | $C_1e^{s_1t}+C_2e^{s_2t}$ / $(C_1+C_2t)e^{st}$ / $e^{\sigma t}(C_1\cos\omega t+C_2\sin\omega t)$ |
| Wronskian | $W=y_1y_2^{\prime}-y_1^{\prime}y_2$ |
| $\alpha$ (neper frequency) | parallel $\frac{1}{2RC}$, series $\frac{R}{2L}$ |
| $\omega_0$, $\omega_d$ | $\omega_0=\frac{1}{\sqrt{LC}}$, $\omega_d=\sqrt{\omega_0^2-\alpha^2}$ |
| Damping | $\alpha>\omega_0$ over, $\alpha=\omega_0$ critical, $\alpha<\omega_0$ under |
