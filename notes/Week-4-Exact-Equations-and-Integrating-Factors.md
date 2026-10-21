# Week 4: Exact Equations and Integrating Factors

## Calculus refresher: partial and implicit differentiation

The same letter $y$ plays two different roles this week. When taking a **partial derivative**, hold the other variable fixed; when differentiating an equation along a solution $y(t)$, use the chain rule.

| Task | Example | Reason |
|---|---|---|
| Differentiate $ty^2$ partially in $t$ | $\dfrac{\partial}{\partial t}(ty^2)=y^2$ | Hold $y$ fixed: it behaves like a constant multiplier. |
| Differentiate $ty^2$ partially in $y$ | $\dfrac{\partial}{\partial y}(ty^2)=2ty$ | Hold $t$ fixed. |
| Differentiate $ty(t)^2$ along a curve | $\dfrac{d}{dt}(ty^2)=y^2+2tyy^{\prime}$ | Both $t$ and $y(t)$ change: product rule, then chain rule. |

Integration with respect to one variable follows the same “hold the other fixed” idea: $\int2ty\,dt=t^2y+g(y)$. Any function $g(y)$ disappears when partially differentiated in $t$, so it is more general than adding just a number.

**Problem: Try it 1 · Check which variable is fixed · original** (introductory)

For $U(t,y)=t^2y+y^3$, find (a) $U_t=\partial U/\partial t$ and (b) $U_y=\partial U/\partial y$. Then find (c) $\int3y^2\,dt$.

<details><summary>Solution</summary>

1. Hold y fixed for (a).

   $$U_t=2ty$$
2. Hold t fixed for (b).

   $$U_y=t^2+3y^2$$
3. In (c), y² is constant with respect to t.

   $$\int3y^2\,dt=3ty^2+g(y)$$

**Answer:** (a) $2ty$. (b) $t^2+3y^2$. (c) $3ty^2+g(y)$.

</details>

## Week 4 overview

An exact equation describes a function that stays constant along its solutions. First see what that means, then learn to recover the function. Only after that will we introduce integrating factors for equations that are not already exact.

## Topic 1: What “exact” means

### Begin with a curve you already understand

The relation $t^2+y^2=9$ describes a circle. On a differentiable branch $y(t)$, differentiate both sides to get $2t+2yy^{\prime}=0$; in differential form this is $2t\,dt+2y\,dy=0$.

That equation says the quantity $U(t,y)=t^2+y^2$ does not change as you move along the solution. Solving the differential equation reverses this process: recover $U$, then write $U(t,y)=K$, with $K$ a constant.

```graph
title "Each constant selects a different curve"
x -4 4 label="$t$"
y -4 4 label="$y$"
equal
slider K 1 12 9 step=1 label="$K$"
level "x^2+y^2" value="K" label="$t^2+y^2=K$" color=1
point "0" "sqrt(K)" label="positive branch at t=0"
caption "The whole circle is a level curve. A solution y(t) uses a branch; the top and bottom branches cannot be joined through a vertical tangent as one differentiable y(t)."
```

### Read M and N from the differential form

$$M(t,y)\,dt+N(t,y)\,dy=0$$

$M$ is the expression multiplying $dt$, and $N$ multiplies $dy$. Exactness means there is one underlying function $U$ with $U_t=M$ and $U_y=N$, so the left side is its total differential $dU$.

$$dU=U_t\,dt+U_y\,dy$$

To test exactness, compare $M_y=\partial M/\partial y$ with $N_t=\partial N/\partial t$. If they are equal, the equation is exact locally, assuming continuous partial derivatives on a neighbourhood; all the potentials constructed below are checked directly.

$$\dfrac{\partial M}{\partial y}=\dfrac{\partial N}{\partial t}$$

The cross derivatives agree because they would both differentiate the same U once in each variable. Do this test before trying to reconstruct U.

**Problem: Try it 2 · Identify and test; do not solve yet · lecture equations** (introductory)

Write $M,N$ and test exactness for:

1. $y'=\dfrac{t-y}{t+y}$.
2. $y'=\dfrac{t}{t+y}$.

Cross-multiply, then move all terms to the left. Keep track of the minus sign.

<details><summary>Solution</summary>

1. 1. Move the dy term to the left.

   $$(t-y)\,dt-(t+y)\,dy=0$$
2. So M = t − y and N = −t − y; the test passes.

   $$M_y=-1=N_t$$
3. 2. Here M = t and N = −t − y; the derivatives differ.

   $$M_y=0\ne-1=N_t$$

**Answer:** 1. Exact. 2. Not exact. The original slope formulas require t + y ≠ 0.

</details>

## Topic 2: Recover the function U

### Integrate one part, then use the other to finish

Integrating $M$ with respect to $t$ gives part of $U$ and an unknown function $g(y)$. Differentiate that result in $y$ and match it to $N$ to discover what $g(y)$ must be.

**Example: Example 1 · A nonconstant “constant of integration” · original**

Solve $2ty\,dt+(t^2+2y)\,dy=0$.

1. Identify the two expressions and test them.

   $$M_y=2t=N_t$$
2. Integrate M in t, keeping y fixed.

   $$U=t^2y+g(y)$$
3. Differentiate in y and set it equal to N.

   $$t^2+g^{\prime}(y)=t^2+2y$$
4. The known t² terms cancel, leaving an ordinary integral in y.

   $$g^{\prime}(y)=2y\quad\Rightarrow\quad g(y)=y^2$$
5. Combine the terms and set U equal to a constant.

   $$t^2y+y^2=K$$

**Answer:** $t^2y+y^2=K$. A separate numeric constant inside $g$ can be absorbed into $K$.

**Problem: Try it 3 · Finish the lecture’s missing steps · Example 4.1** (introductory)

For $(2ty+3t^2)\,dt+t^2\,dy=0$, the test gives $M_y=N_t=2t$. After integrating $M$ we have $U=t^2y+t^3+g(y)$.

Find $U_y$, determine $g(y)$, and write the implicit solution.

<details><summary>Solution</summary>

1. Differentiate in y; t³ is a constant for this partial derivative.

   $$U_y=t^2+g^{\prime}(y)$$
2. Match N = t².

   $$g^{\prime}(y)=0$$
3. A constant g is absorbed into the final arbitrary constant.

   $$t^2y+t^3=K$$

**Answer:** $U_y=t^2+g^{\prime}(y)$, $g$ is constant, and $t^2y+t^3=K$.

</details>

You can start from $N$ instead: integrating $t^2$ in $y$ gives $U=t^2y+h(t)$. Matching $U_t=2ty+3t^2$ gives $h^{\prime}(t)=3t^2$, so $h=t^3$ and the same answer results. Choose the easier integral.

**Problem: Try it 4 · A constant chooses a curve · lecture (a), added initial condition** (introductory)

The lecture equation $3t\,dt+4y\,dy=0$ gives $U=\frac32t^2+2y^2$. Write its solution without fractions, then choose the constant for $y(2)=2$.

<details><summary>Solution</summary>

1. Set U equal to a constant and multiply by 2; rename the constant.

   $$3t^2+4y^2=K$$
2. Substitute the starting point.

   $$K=3(2^2)+4(2^2)=28$$

**Answer:** $3t^2+4y^2=28$. Near $(2,2)$, use the positive y-branch.

</details>

**Example: Example 2 · From a slope equation to an IVP · lecture (b), added initial condition**

Solve $y'=(t-y)/(t+y)$, $y(1)=0$.

1. The earlier test showed exactness with M = t − y, N = −t − y.

   $$(t-y)\,dt-(t+y)\,dy=0$$
2. Integrate M in t; y is held fixed.

   $$U=\dfrac{t^2}{2}-ty+g(y)$$
3. Match the y-partial derivative to N.

   $$-t+g^{\prime}(y)=-t-y$$
4. Integrate the remaining y-expression.

   $$g(y)=-\dfrac{y^2}{2}$$
5. Set U constant, multiply by 2, and use the start.

   $$t^2-2ty-y^2=K,\quad K=1$$
6. Check using implicit differentiation and solve for the derivative.

   $$2t-2y-2ty^{\prime}-2yy^{\prime}=0$$

**Answer:** $t^2-2ty-y^2=1$, on the branch through $(1,0)$ where $t+y\ne0$. Differentiating recovers $y^{\prime}=(t-y)/(t+y)$.

**Problem: Try it 5 · A sign decides the test · lecture (c)** (introductory)

A student rewrites $2tyy^{\prime}=t^2-y^2$ as $(t^2-y^2)\,dt+2ty\,dy=0$ and finds that it is not exact.

Correct the rearrangement and solve the corrected equation.

<details><summary>Solution</summary>

1. Moving the dy term left requires a minus sign.

   $$(t^2-y^2)\,dt-2ty\,dy=0$$
2. The corrected cross derivatives agree.

   $$M_y=-2y=N_t$$
3. Integrate M and match N; the remaining g is constant.

   $$U=\dfrac{t^3}{3}-ty^2+g(y),\quad g^{\prime}(y)=0$$
4. Set U constant and multiply by 3.

   $$t^3-3ty^2=K$$

**Answer:** The dy coefficient must be $-2ty$; the solution relation is $t^3-3ty^2=K$.

</details>

To check an answer $U=K$, either compare $U_t$ and $U_y$ with $M,N$, or differentiate along $y(t)$ and recover the original equation. An implicit relation describes possible curves; use a differentiable branch satisfying any original denominators and initial conditions.

## Topic 3: Make a non-exact equation exact

An **integrating factor** $\mu$ multiplies both terms: $\mu M\,dt+\mu N\,dy=0$. We look for a multiplier that makes the new cross derivatives equal; where $\mu$ is finite and nonzero, this preserves the original equation.

First test exactness. If it fails, try the following two tests separately; they find certain integrating factors, not every possible one.

### First try a factor depending only on t

$$\dfrac{M_y-N_t}{N}=f(t)\quad\Rightarrow\quad\mu(t)=e^{\int f(t)\,dt}$$

The ratio must simplify to a function of $t$ only. This follows by expanding $(\mu M)_y=(\mu N)_t$ with $\mu=\mu(t)$: the remaining equation is $\mu^{\prime}/\mu=(M_y-N_t)/N$.

**Example: Example 3 · Find a t-only factor · original**

Solve $(t^2+y^2+t)\,dt+ty\,dy=0$ with $y(1)=1$, taking $t>0$.

1. The cross derivatives are 2y and y, so the equation is not exact.

   $$\dfrac{M_y-N_t}{N}=\dfrac{2y-y}{ty}=\dfrac1t$$
2. Integrate the ratio; on t > 0 the factor is t.

   $$\mu=e^{\ln t}=t$$
3. Multiply both terms and re-test.

   $$(t^3+ty^2+t^2)\,dt+t^2y\,dy=0$$
4. The new cross derivatives are both 2ty. Integrate in t and match N.

   $$U=\dfrac{t^4}{4}+\dfrac{t^2y^2}{2}+\dfrac{t^3}{3}$$
5. Multiply U = constant by 12 and apply the start.

   $$3t^4+6t^2y^2+4t^3=13$$

**Answer:** $3t^4+6t^2y^2+4t^3=13$, using the positive y-branch near $(1,1)$. The multiplier t is nonzero on the chosen domain.

**Problem: Try it 6 · Practise finding the factor only · original** (introductory)

For $2y\,dt+t\,dy=0$ on $t>0$, find the t-only integrating factor. Multiply both terms and check exactness; stop there.

<details><summary>Solution</summary>

1. Here M = 2y, N = t.

   $$\dfrac{M_y-N_t}{N}=\dfrac{2-1}{t}=\dfrac1t$$
2. The factor is t.

   $$2ty\,dt+t^2\,dy=0$$
3. Differentiate the new coefficients across variables.

   $$\dfrac{\partial(2ty)}{\partial y}=2t=\dfrac{\partial(t^2)}{\partial t}$$

**Answer:** $\mu=t$. The multiplied equation is exact.

</details>

### If needed, try a factor depending only on y

$$\dfrac{N_t-M_y}{M}=g(y)\quad\Rightarrow\quad\mu(y)=e^{\int g(y)\,dy}$$

Notice both changes: the subtraction order reverses, and the denominator becomes M. This time the ratio must contain only y. A constant qualifies as a function of either variable.

```steps
title "Repair the lecture equation"
$$ y\,dt+(3+3t-y)\,dy=0 $$
Identify M = y and N = 3 + 3t − y.
$$ M_y=1,\quad N_t=3 $$
The original equation is not exact.
$$ \dfrac{M_y-N_t}{N}=\dfrac{-2}{3+3t-y} $$
The t-only test fails: this still contains y.
$$ \dfrac{N_t-M_y}{M}=\hl{\dfrac2y} $$
The y-only test works away from y = 0.
$$ \mu=e^{2\ln|y|}=\hl{y^2} $$
Integrate 2/y, then exponentiate.
$$ \hl{y^3}\,dt+\hl{y^2}(3+3t-y)\,dy=0 $$
Multiply both terms by the factor.
$$ \dfrac{\partial(y^3)}{\partial y}=\hl{3y^2}=\dfrac{\partial[y^2(3+3t-y)]}{\partial t} $$
Re-test: the new equation is exact.
```

**Problem: Try it 7 · Finish the repaired equation · Pre-tutorial 4** (introductory)

Solve $y^3\,dt+y^2(3+3t-y)\,dy=0$. Start by integrating $M=y^3$ with respect to $t$, then determine the missing function of $y$.

<details><summary>Solution</summary>

1. Treat y³ as constant while integrating in t.

   $$U=ty^3+h(y)$$
2. Match the y-partial derivative to N.

   $$3ty^2+h^{\prime}(y)=3y^2+3ty^2-y^3$$
3. Cancel the shared term, then integrate in y.

   $$h^{\prime}(y)=3y^2-y^3,\quad h=y^3-\dfrac{y^4}{4}$$
4. Set U constant and multiply by 4.

   $$4(t+1)y^3-y^4=K$$

**Answer:** $4(t+1)y^3-y^4=K$.

</details>

We multiplied the original equation by $y^2$, which vanishes on $y=0$. Check that line in the original equation separately: $y=0$ does solve it. Other branches must also be checked where the multiplier is zero or undefined; equivalence was guaranteed only where it was nonzero.

**Problem: Try it 8 · Choose the test instead of memorising its answer · original** (introductory)

For $t\,dt-(t+y)\,dy=0$, compute both ratios. Does either simple test supply a factor?

<details><summary>Solution</summary>

1. For the t-only test, the ratio still contains y.

   $$\dfrac{M_y-N_t}{N}=-\dfrac{1}{t+y}$$
2. For the y-only test, the ratio contains t.

   $$\dfrac{N_t-M_y}{M}=-\dfrac1t$$

**Answer:** Neither test works. This does not prove that no integrating factor exists; these two tests are limited.

</details>

### Connect this to Week 3

Write a linear equation as $(a(t)y-f(t))\,dt+dy=0$. Here $M=a(t)y-f(t)$ and $N=1$, so $(M_y-N_t)/N=a(t)$. The t-only test therefore gives exactly Week 3’s factor $\mu=e^{\int a(t)dt}$.
