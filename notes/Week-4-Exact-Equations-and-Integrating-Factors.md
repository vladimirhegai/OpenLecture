# Week 4: Exact Equations and Integrating Factors

## Topic 1: Exact equations

Every first-order ODE can be written as $M\,dt+N\,dy=0$.
- $M$, $N$: expressions in $t$ and $y$
- $U(t,y)$: one function whose two slopes are $M$ and $N$ (if it exists)
- $\dfrac{\partial U}{\partial t}$: a **partial derivative** (differentiate in $t$ while treating $y$ as a fixed number)

The equation is **exact** when $M=\dfrac{\partial U}{\partial t}$ and $N=\dfrac{\partial U}{\partial y}$.

Then the left side is the change of $U$ for a small step ($dU$). So the equation says $U$ doesn't change:

$$M\,dt+N\,dy=\dfrac{\partial U}{\partial t}dt+\dfrac{\partial U}{\partial y}dy=dU=0$$

So $U$ never changes along a solution: **every solution is a curve $U(t,y)=C$**.

You can check an equation is exact without knowing $U$ (Theorem 4.1).

It works because both sides equal “differentiate $U$ once in $t$ and once in $y$”, and the order doesn't matter:

$$M\,dt+N\,dy=0\ \text{is exact}\iff\dfrac{\partial M}{\partial y}=\dfrac{\partial N}{\partial t}$$

```steps
title "Finding $U$ (lecture Example 4.1)"
$$ (2ty+3t^2)\,dt+t^2\,dy=0 $$
Here $M=2ty+3t^2$ and $N=t^2$.
$$ \dfrac{\partial M}{\partial y}=\hl{2t},\qquad \dfrac{\partial N}{\partial t}=\hl{2t} $$
Test: hold $t$ fixed to get $\partial(2ty)/\partial y=2t$; hold $y$ fixed to get $\partial(t^2)/\partial t=2t$. Equal, so exact.
$$ \dfrac{\partial U}{\partial t}=2ty+3t^2 $$
So some $U$ has $M$ as its $t$-slope. Undo that slope by integrating in $t$.
$$ U=\hl{t^2y+t^3+f(y)} $$
With $y$ fixed, $\int 2ty\,dt=t^2y$ and $\int 3t^2dt=t^3$. The "constant" can be any $f(y)$, since $\partial f(y)/\partial t=0$.
$$ \dfrac{\partial U}{\partial y}=\hl{t^2+f^{\prime}(y)}=t^2 $$
Differentiate in $y$ and set it equal to $N=t^2$.
$$ f^{\prime}(y)=\hl{0}\ \Rightarrow\ f(y)=\text{const} $$
The $t^2$ cancels. What is left must contain only $y$ (if a $t$ survives, you made a mistake).
$$ \hl{t^2y+t^3=C} $$
The solution is $U=C$ (the constant from $f$ is absorbed into $C$).
```

The lecture also does it in the other order:
- **Integrate $N$ in $y$:** $U=\int t^2\,dy=t^2y+g(t)$
- **Match $M$:** $g^{\prime}(t)=3t^2$, so $g=t^3$

Same $U$. Start with whichever integral is easier.

**Example: Example 1 · Lecture (a): the answer is a family of curves**

Solve $3t\,dt+4y\,dy=0$.

1. $M=3t$ has no $y$ and $N=4y$ has no $t$, so both test derivatives are $0$: exact.

   $$\dfrac{\partial M}{\partial y}=0=\dfrac{\partial N}{\partial t}$$
2. Integrate $M$ in $t$ ($\int t\,dt=\tfrac{t^2}{2}$) and add $f(y)$.

   $$U=\tfrac32t^2+f(y)$$
3. Match $N$. This time $f$ is not constant: $\int 4y\,dy=2y^2$.

   $$f^{\prime}(y)=4y\ \Rightarrow\ f(y)=2y^2$$
4. Set $U=C$ and double it to clear the fraction ($2C$ is just another constant, so call it $C$ again).

   $$3t^2+4y^2=C$$

**Answer:** $3t^2+4y^2=C$: one ellipse for each $C>0$

```graph3d
title "Solutions are level curves of $U$ (lecture (a))"
x -2 2 label="$t$"
y -2 2 label="$y$"
z 0 28 label="$U$"
view az=-55 el=30
slider C 1 24 8 step=1 label="$C$"
surface "3*x^2+4*y^2" label="$U=3t^2+4y^2$" mesh=30
plane "C" label="where $U=C$: one solution curve"
caption "Slide the plane: each height $C$ cuts the bowl in one ellipse, and its shadow on the floor is the solution $3t^2+4y^2=C$. An initial condition picks the height."
```

**Example: Example 2 · Lecture (b): start from $dy/dt$, then use a starting point**

Solve $\dfrac{dy}{dt}=\dfrac{t-y}{t+y}$ with $y(1)=0$.

1. Multiply both sides by $(t+y)\,dt$, then move everything to the left. The minus sign belongs to $N$.

   $$(t-y)\,dt-(t+y)\,dy=0$$
2. Test with $M=t-y$ and $N=-t-y$.

   $$\dfrac{\partial M}{\partial y}=-1=\dfrac{\partial N}{\partial t}$$
3. Integrate $M$ in $t$; with $y$ fixed, $\int y\,dt=ty$.

   $$U=\dfrac{t^2}{2}-ty+f(y)$$
4. Match $N$: $-t+f^{\prime}(y)=-t-y$, so $f^{\prime}(y)=-y$.

   $$f(y)=-\tfrac{y^2}{2}$$
5. Set $U=C$ and double.

   $$t^2-2ty-y^2=C$$
6. The starting point picks the curve: put $t=1$, $y=0$ into the left side.

   $$C=1-0-0=1$$
7. Check by differentiating in $t$, with $y=y(t)$.

**Product rule:** $\frac{d}{dt}(2ty)=2y+2ty^{\prime}$.

**Chain rule:** $\frac{d}{dt}y^2=2yy^{\prime}$.

   $$2t-2y-2ty^{\prime}-2yy^{\prime}=0\ \Rightarrow\ y^{\prime}=\dfrac{t-y}{t+y}\ \checkmark$$

**Answer:** $t^2-2ty-y^2=1$

**Example: Example 3 · Lecture (d): when the test fails**

Is $\dfrac{dy}{dt}=\dfrac{t}{t+y}$ exact?

1. Cross-multiply and move everything to the left.

   $$t\,dt-(t+y)\,dy=0$$
2. Test with $M=t$ and $N=-(t+y)$.

   $$\dfrac{\partial M}{\partial y}=0\ \neq\ -1=\dfrac{\partial N}{\partial t}$$
3. No $U$ exists, so the recipe can’t start.

Topic 2 repairs some equations like this one, but not this one: both of its tests fail here.

**Answer:** Not exact

**Problem: Try it 1 · Lecture (c): find the mistake** (introductory)

A classmate rewrites $2ty\,\dfrac{dy}{dt}=t^2-y^2$ as $(t^2-y^2)\,dt+2ty\,dy=0$.

They find $\dfrac{\partial M}{\partial y}=-2y\neq2y=\dfrac{\partial N}{\partial t}$ and give up.

What went wrong? Solve it.

<details><summary>Solution</summary>

1. Moving $2ty\,dy$ to the left flips its sign, so $N=-2ty$, not $+2ty$.

   $$(t^2-y^2)\,dt-2ty\,dy=0$$
2. Now the test passes.

   $$\dfrac{\partial M}{\partial y}=-2y=\dfrac{\partial N}{\partial t}$$
3. Integrate $M$ in $t$ ($y^2$ is a constant here, so $\int y^2dt=ty^2$).

   $$U=\dfrac{t^3}{3}-ty^2+f(y)$$
4. Match $N$: $-2ty+f^{\prime}(y)=-2ty$, so $f$ is constant. Set $U=C$ and multiply by 3.

   $$t^3-3ty^2=C$$

**Answer:** A lost minus sign. The solution is $t^3-3ty^2=C$.

</details>

**Problem: Try it 2 · Choose the constant** (intermediate)

Find the number $k$ that makes $(2t\sin y+y)\,dt+(t^2\cos y+kt)\,dy=0$ exact.

Then solve it with $y(1)=\dfrac{\pi}{2}$.

<details><summary>Solution</summary>

1. Both test derivatives, using $\frac{d}{dy}\sin y=\cos y$.

   $$\begin{gathered}\dfrac{\partial M}{\partial y}=2t\cos y+1, \\ \dfrac{\partial N}{\partial t}=2t\cos y+k\end{gathered}$$
2. They agree for every $t$ and $y$ only if $k=1$.

   $$k=1$$
3. Integrate $M$ in $t$ ($\sin y$ is a constant factor).

   $$U=t^2\sin y+ty+f(y)$$
4. Match $N=t^2\cos y+t$: $\partial U/\partial y=t^2\cos y+t+f^{\prime}(y)$, so $f^{\prime}=0$.

   $$U=t^2\sin y+ty$$
5. Put in $t=1$, $y=\frac{\pi}{2}$, with $\sin\frac{\pi}{2}=1$.

   $$C=1+\dfrac{\pi}{2}$$

**Answer:** $k=1$; $\ t^2\sin y+ty=1+\dfrac{\pi}{2}$

</details>

## Topic 2: Integrating factors

If an equation isn't exact, multiply it by a function $\mu(t,y)$ (“mu”, an **integrating factor**).

The new equation $\mu M\,dt+\mu N\,dy=0$ has:
- **the same solution curves** (wherever $\mu\neq0$)
- **new coefficients**, which may pass the test

The lecture's two tests (Spiegel's Theorems 1 and 2) find a $\mu$ that depends on one variable only:

|  | Compute | Works if only this is left | Integrating factor |
|---|---|---|---|
| Test 1 | $\dfrac{1}{N}\Big(\dfrac{\partial M}{\partial y}-\dfrac{\partial N}{\partial t}\Big)$ | $t$: call it $f(t)$ | $\mu=e^{\int f(t)\,dt}$ |
| Test 2 | $\dfrac{1}{M}\Big(\dfrac{\partial N}{\partial t}-\dfrac{\partial M}{\partial y}\Big)$ | $y$: call it $g(y)$ | $\mu=e^{\int g(y)\,dy}$ |

Note:
- The two tests divide by different things and subtract in opposite orders.
- A constant counts as “only $t$” and “only $y$”.

Then multiply **both** $M$ and $N$ by $\mu$, re-test, and solve as in Topic 1.

**Example: Example 4 · Lecture (e): Test 1 fails, Test 2 works**

Make $y\,dt+(3+3t-y)\,dy=0$ exact.

1. $M=y$, $N=3+3t-y$. Not exact.

   $$\dfrac{\partial M}{\partial y}=1\ \neq\ 3=\dfrac{\partial N}{\partial t}$$
2. Test 1: the result still contains $y$, so it fails.

   $$\dfrac{1}{N}(1-3)=\dfrac{-2}{3+3t-y}$$
3. Test 2: only $y$ is left.

   $$\dfrac{1}{M}(3-1)=\dfrac{2}{y}=g(y)$$
4. $\int\frac{1}{y}dy=\ln|y|$, and $2\ln|y|=\ln y^2$, so $e^{2\ln|y|}=y^2$ (not $2y$).

   $$\mu=e^{\int\frac{2}{y}dy}=e^{2\ln|y|}=y^2$$
5. Multiply **both** parts by $y^2$ (Eq. (4.13)) and re-test: both derivatives are now $3y^2$.

   $$y^3\,dt+(3y^2+3ty^2-y^3)\,dy=0$$

**Answer:** $\mu=y^2$; the new equation is exact

**Example: Example 5 · Pre-tutorial 4: finish lecture (e)**

Solve $y^3\,dt+y^2(3+3t-y)\,dy=0$, Eq. (4.13).

1. Integrate $M=y^3$ in $t$: with $y$ fixed it is a constant.

   $$U=ty^3+f(y)$$
2. Match $N=3y^2+3ty^2-y^3$: the $3ty^2$ cancels.

   $$3ty^2+f^{\prime}(y)=3y^2+3ty^2-y^3\ \Rightarrow\ f^{\prime}(y)=3y^2-y^3$$
3. Power rule: $\int y^n dy=\frac{y^{n+1}}{n+1}$.

   $$f(y)=y^3-\dfrac{y^4}{4}$$
4. Set $U=C$ and multiply by 4.

   $$4(t+1)y^3-y^4=C$$
5. Lost solutions? Multiplying by $\mu=y^2$ can hide the line where $\mu=0$.

$y=0$ does solve the original ($M=0$ and $dy=0$). It is the $C=0$ curve, so nothing is lost.

**Answer:** $4(t+1)y^3-y^4=C$

The grey slopes below come from the original $y\,dt+(3+3t-y)\,dy=0$, before multiplying.
- **Drag the point:** the curve $4(t+1)y^3-y^4=C$ through it always follows them.
- **Drag it onto $y=0$:** $C=0$ and the curve is the line $y=0$ (plus the line $y=4t+4$, which also solves the equation).

```graph
title "Multiplying by $\mu=y^2$ didn't change the solutions"
x -1 3 label="$t$"
y -1 4 label="$y$"
field "-y/(3+3*x-y)"
drag P 0.5 1 label="$(t_0,y_0)$" snap=0.25
level "4*(x+1)*y^3-y^4" value="4*(P_x+1)*P_y^3-P_y^4" label="$4(t+1)y^3-y^4=C$ through your point" color=2
readout "$C=$" "4*(P_x+1)*P_y^3-P_y^4"
```

**Example: Example 6 · Test 1 gives μ = t**

Solve $(t^2+y^2+t)\,dt+ty\,dy=0$ with $y(1)=1$ (take $t>0$).

1. Test first: not exact.

   $$\dfrac{\partial M}{\partial y}=2y\ \neq\ y=\dfrac{\partial N}{\partial t}$$
2. Test 1: the $y$ cancels, leaving only $t$.

   $$\dfrac{1}{N}(2y-y)=\dfrac{y}{ty}=\dfrac1t=f(t)$$
3. $\int\frac1t dt=\ln t$ and $e^{\ln t}=t$.

   $$\mu=e^{\ln t}=t$$
4. Multiply both parts by $t$; both test derivatives are now $2ty$.

   $$(t^3+ty^2+t^2)\,dt+t^2y\,dy=0$$
5. Integrate the new $M$ in $t$. Matching $N=t^2y$ gives $f^{\prime}(y)=0$.

   $$U=\dfrac{t^4}{4}+\dfrac{t^2y^2}{2}+\dfrac{t^3}{3}$$
6. Multiply $U=C$ by 12, then put in $t=1$, $y=1$.

   $$3t^4+6t^2y^2+4t^3=C,\qquad C=13$$
7. Here you can solve for $y$: isolate $y^2$, and take the $+$ root because $y(1)=1>0$.

   $$y=\sqrt{\dfrac{13-3t^4-4t^3}{6t^2}}$$

**Answer:** $y=\sqrt{\dfrac{13-3t^4-4t^3}{6t^2}}$

**Problem: Try it 3 · Both tests work, and one loses a solution** (intermediate)

For $y\,dt-t\,dy=0$, show that both tests give an integrating factor.

Solve it with the Test 2 factor. Which solution did that factor lose?

<details><summary>Solution</summary>

1. $M=y$, $N=-t$, so $\frac{\partial M}{\partial y}=1$, $\frac{\partial N}{\partial t}=-1$. Test 1 leaves only $t$.

   $$\dfrac{1-(-1)}{-t}=-\dfrac{2}{t}\ \Rightarrow\ \mu=e^{-2\ln t}=\dfrac{1}{t^2}$$
2. Test 2 leaves only $y$.

   $$\dfrac{-1-1}{y}=-\dfrac{2}{y}\ \Rightarrow\ \mu=e^{-2\ln y}=\dfrac{1}{y^2}$$
3. Multiply by $\frac{1}{y^2}$, integrate $M=\frac1y$ in $t$, and match $N=-\frac{t}{y^2}$ (it already matches, $f$ is constant).

   $$\dfrac{1}{y}\,dt-\dfrac{t}{y^2}\,dy=0\ \Rightarrow\ \dfrac{t}{y}=C$$
4. $\frac{t}{y}=C$ gives the lines $y=\frac{t}{C}$, but never $y=0$.

Yet $y=0$ solves $y\,dt-t\,dy=0$ ($M=0$ and $dy=0$). It sits where $\mu=\frac{1}{y^2}$ is undefined, so add it back.

   $$y=kt\quad\text{for any }k\text{, including }k=0$$

**Answer:** - **Test 1:** $\mu=\dfrac{1}{t^2}$
- **Test 2:** $\mu=\dfrac{1}{y^2}$
- **Solutions:** $y=kt$; $\mu=\dfrac{1}{y^2}$ loses $y=0$.

</details>

**Problem: Try it 4 · Linear equations are a special case** (intermediate)

Show that Test 1 always works for a linear equation $\dfrac{dy}{dt}+a(t)\,y=b(t)$, and that it gives the Week 3 integrating factor.

Then use it to solve $\dfrac{dy}{dt}+2y=4$ with $y(0)=0$.

<details><summary>Solution</summary>

1. Multiply by $dt$ and move everything left.

   $$\big(a(t)\,y-b(t)\big)\,dt+1\,dy=0$$
2. $\frac{\partial M}{\partial y}=a(t)$, $\frac{\partial N}{\partial t}=0$, $N=1$: Test 1 leaves only $t$.

   $$\dfrac{1}{1}\big(a(t)-0\big)=a(t)\ \Rightarrow\ \mu=e^{\int a(t)\,dt}$$
3. For $\frac{dy}{dt}+2y=4$: $a=2$, so $\mu=e^{2t}$.

   $$(2y-4)e^{2t}\,dt+e^{2t}\,dy=0$$
4. Integrating $N$ in $y$ is easier here ($e^{2t}$ is a constant factor). Add $g(t)$.

   $$U=ye^{2t}+g(t)$$
5. Match $M$: $g^{\prime}(t)=-4e^{2t}$. Using $\int e^{2t}dt=\frac12e^{2t}$:

   $$g(t)=-2e^{2t}\ \Rightarrow\ U=(y-2)e^{2t}$$
6. Put in $t=0$, $y=0$, then solve for $y$.

   $$(y-2)e^{2t}=-2\ \Rightarrow\ y=2-2e^{-2t}$$

**Answer:** $\mu=e^{\int a(t)\,dt}$ (the Week 3 factor); $\ y=2-2e^{-2t}$

</details>
