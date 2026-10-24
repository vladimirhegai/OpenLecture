# Week 6: Reduction of Order and Undetermined Coefficients

## Calculus refresher: the product rule twice, and squared trig

This week you substitute $y=y_1v$, where $y_1$ is a known function and $v$ an unknown one. Differentiating a product twice gives a middle term with a 2 in front:

| Expression | Result | Rule |
|---|---|---|
| $(y_1v)^{\prime}$ | $y_1^{\prime} v+y_1v^{\prime}$ | Product rule. |
| $(y_1v)^{\prime\prime}$ | $y_1^{\prime\prime} v+2y_1^{\prime} v^{\prime}+y_1v^{\prime\prime}$ | Product rule again; the two middle terms combine. |
| $\int\frac1z\,dz$ | $\ln|z|$ | Used when separating a first-order equation. |
| $\cos^2t$ | $\frac12+\frac12\cos2t$ | Double-angle identity: removes the square. |
| $\sin^2t$ | $\frac12-\frac12\cos2t$ | Same identity, opposite sign. |

Some integrals, such as $\int e^{t^2/2}/t^2\,dt$, have no formula in ordinary functions. Leave them as an integral: that is a complete answer.

**Problem: Try it 1 · Differentiate a product twice; remove a square · original** (introductory)

(a) Find $(tv)^{\prime\prime}$, where $v(t)$ is unknown. (b) Write $8\sin^2t$ as a constant plus a cosine.

<details><summary>Solution</summary>

1. First derivative: product rule.

   $$(tv)'=v+tv'$$
2. Differentiate again; v′ appears twice.

   $$(tv)''=v'+v'+tv''=2v'+tv''$$
3. Multiply the sin² identity by 8.

   $$8\sin^2t=4-4\cos2t$$

**Answer:** (a) $tv''+2v'$. (b) $4-4\cos2t$.

</details>

## Week 6 overview

Week 6 has two methods for second-order linear ODEs:

- **Reduction of order:** you know one solution $y_1$ of a homogeneous equation; find the second one.
- **Undetermined coefficients:** the equation has a forcing term $g(t)$; guess the form of a particular solution from $g$.

Both come from the professor’s handwritten notes (Spiegel, *Applied Differential Equations*). The Week 6 tutorial problem is Example 4. The notes write $\dot y,\ \ddot y$ for $y^{\prime},\ y^{\prime\prime}$.

## Topic 1: Reduction of order

### Multiply the known solution by an unknown function

Suppose $y_1$ solves a second-order linear homogeneous ODE. Look for the second solution as $y=y_1v$, where $v(t)$ is unknown.

The recipe:

- **Substitute** $y=y_1v$, using the product rule for $y^{\prime}$ and $y^{\prime\prime}$.
- **Collect terms:** every term with plain $v$ cancels, because $y_1$ is a solution.
- **Set $z=v^{\prime}$:** what remains is a first-order equation in $z$ (the order went down by one).
- **Solve for $z$**, then integrate once more: $v=\int z\,dt$.
- **Multiply back:** $y=y_1v$.

The professor’s example, step by step:

```steps
title "Lecture: reduce y″ − t y′ + y = 0, given y = t"
$$ y''-ty'+y=0,\qquad y_1=t $$
Check: $y_1=t$ gives $0-t+t=0$.
$$ y=\hl{tv} $$
Multiply the known solution by an unknown $v$.
$$ y'=\hl{v+tv'},\qquad y''=\hl{2v'+tv''} $$
Product rule (refresher table).
$$ (2v'+tv'')-t(v+tv')+tv=0 $$
Substitute all three into the ODE.
$$ \hl{tv''+(2-t^2)v'}=0 $$
Collect terms. The $-tv$ and $+tv$ cancel, as promised.
$$ t\hl{z'}+(2-t^2)\hl{z}=0,\qquad z=v' $$
Only $v^{\prime}$ and $v^{\prime\prime}$ remain: first order in $z$.
```

**Example: Example 1 · Finish the lecture example · handwritten notes p. 1–2**

Solve $tz'+(2-t^2)z=0$ (from the stepper above), then find the general solution of $y''-ty'+y=0$ for $t\ne0$.

1. The equation is separable. Divide by $tz$ and move the $t$ terms right.

   $$\dfrac{dz}{z}=\dfrac{t^2-2}{t}\,dt=\left(t-\dfrac2t\right)dt$$
2. Integrate both sides: $\int\frac1z\,dz=\ln|z|$.

   $$\ln|z|=\dfrac{t^2}2-2\ln|t|+C$$
3. Exponentiate; $e^{-2\ln|t|}=1/t^2$.

   $$z=C_1\,\dfrac{e^{t^2/2}}{t^2}$$
4. $z=v^{\prime}$, so integrate again. The integral has no closed form, so it stays.

   $$v=C_1\int\dfrac{e^{t^2/2}}{t^2}\,dt+C_2$$
5. Multiply back by $y_1=t$.

   $$y=tv$$

**Answer:** $y=C_2\,t+C_1\,t\displaystyle\int\frac{e^{t^2/2}}{t^2}\,dt$. The known solution $t$ reappears as the $C_2$ term.

### Where the repeated-root $te^{st}$ comes from

**Example: Example 2 · Reduce a constant-coefficient equation · original**

$y''+4y'+4y=0$ has the repeated root $s=-2$, so $y_1=e^{-2t}$. Use reduction of order to find the second solution.

1. Set $y=e^{-2t}v$ and differentiate with the product rule.

   $$y'=e^{-2t}(v'-2v)$$
2. Differentiate again.

   $$y''=e^{-2t}(v''-4v'+4v)$$
3. Substitute and divide by $e^{-2t}$. The $v^{\prime}$ terms cancel too.

   $$(v''-4v'+4v)+4(v'-2v)+4v=v''=0$$
4. Integrate twice.

   $$v=C_1+C_2t$$

**Answer:** $y=(C_1+C_2t)e^{-2t}$: exactly the Week 5 repeated-root form. The extra $t$ is $v$.

> **Tip:** **Check with the formula.** Write the ODE as $y^{\prime\prime}+p(t)y^{\prime}+q(t)y=0$. Reduction of order always ends at
> 
> $$
> y_2=y_1\int\frac{e^{-\int p\,dt}}{y_1^2}\,dt
> $$
> 
> Lecture example: $p=-t$, so $e^{-\int p\,dt}=e^{t^2/2}$ and $y_1^2=t^2$, matching Example 1.

**Problem: Try it 2 · A second solution with a logarithm · original** (introductory)

For $t>0$, $y_1=t^2$ solves $t^2y''-3ty'+4y=0$. Find the general solution.

<details><summary>Solution</summary>

1. Set $y=t^2v$ and use the product rule twice.

   $$y'=2tv+t^2v',\qquad y''=2v+4tv'+t^2v''$$
2. Substitute; the plain $v$ terms cancel ($2-6+4=0$).

   $$t^4v''+t^3v'=0$$
3. Divide by $t^4$ and set $z=v^{\prime}$.

   $$z'+\dfrac zt=0$$
4. Separate: $\int\frac{dz}{z}=-\int\frac{dt}{t}$, so $\ln|z|=-\ln t+C$.

   $$z=\dfrac{C_2}t$$
5. Integrate: $\int\frac1t\,dt=\ln t$ for $t>0$.

   $$v=C_1+C_2\ln t$$

**Answer:** $y=C_1t^2+C_2t^2\ln t$.

</details>

## Topic 2: Undetermined coefficients

### Total solution = complementary + particular

Now the right side is a forcing term: $ay^{\prime\prime}+by^{\prime}+cy=g(t)$.

- $y_c$: the **complementary solution**, the general solution with $g=0$ (Week 5). It holds the two constants.
- $y_p$: one **particular solution**, any single function that produces $g(t)$. No constants.
- $y=y_c+y_p$: the general solution.

To find $y_p$, guess a form that looks like $g(t)$ with unknown coefficients, substitute, and match coefficients on both sides.

| Term in $g(t)$ | Guess for $y_p$ |
|---|---|
| constant or polynomial of degree $n$ | $A_nt^n+\dots+A_1t+A_0$ (all lower powers) |
| $e^{at}$ | $Ae^{at}$ |
| $\sin rt$ or $\cos rt$ | $A\cos rt+B\sin rt$ (always both) |
| $e^{at}\cos rt$ or $e^{at}\sin rt$ | $e^{at}(A\cos rt+B\sin rt)$ |
| a sum of these | the sum of their guesses |

**Example: Example 3 · A polynomial guess needs every lower power · original**

Find the general solution of $y''+y'-2y=2t$.

1. Complementary: $s^2+s-2=(s+2)(s-1)$.

   $$y_c=C_1e^t+C_2e^{-2t}$$
2. $2t$ has degree 1, so guess $At+B$. The $B$ is needed even though $g$ has no constant.

   $$y_p=At+B,\quad y_p'=A,\quad y_p''=0$$
3. Substitute.

   $$A-2(At+B)=2t$$
4. Match the $t$ terms, then the constants.

   $$-2A=2,\qquad A-2B=0$$
5. Solve.

   $$A=-1,\qquad B=-\tfrac12$$

**Answer:** $y=C_1e^t+C_2e^{-2t}-t-\tfrac12$. Guessing only $At$ fails: the constant $A$ left over has nothing to match.

**Example: Example 4 · The Week 6 tutorial problem (also the lecture example) · tutorial 6, notes p. 3–4**

Solve $\ddot y+y=6\cos^2t$ with $y(0)=0$ and $y(\pi/2)=0$. The tutorial gives the forms $y_c=c_1\sin t+c_2\cos t$ and $y_p=A+B\cos2t+D\sin2t$.

1. Complementary: $s^2+1=0$ gives $s=\pm j$.

   $$y_c=c_1\sin t+c_2\cos t$$
2. Remove the square with the identity, so the guess table applies.

   $$6\cos^2t=3+3\cos2t$$
3. Constant → $A$; cos 2t → both cos 2t and sin 2t.

   $$y_p=A+B\cos2t+D\sin2t$$
4. Differentiate twice: each derivative brings out a 2.

   $$y_p''=-4B\cos2t-4D\sin2t$$
5. Substitute $y_p^{\prime\prime}+y_p$ and collect.

   $$A-3B\cos2t-3D\sin2t=3+3\cos2t$$
6. Match constants, cosines and sines.

   $$A=3,\qquad B=-1,\qquad D=0$$
7. Add $y_c$ **before** using the conditions: they apply to the whole $y$.

   $$y=3-\cos2t+c_1\sin t+c_2\cos t$$
8. $y(0)=0$: $\sin0=0$, $\cos0=1$.

   $$3-1+c_2=0\quad\Rightarrow\quad c_2=-2$$
9. $y(\pi/2)=0$: $\cos\pi=-1$, $\sin\frac\pi2=1$, $\cos\frac\pi2=0$.

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

### When the guess is already in $y_c$: multiply by $t$

If a term of your guess already solves the homogeneous equation, substituting it gives $0$, so it can never produce $g$.

**Fix:** multiply that guess by $t$. If the result is still in $y_c$ (a repeated root), multiply by $t^2$.

**Example: Example 5 · The guess is already in the complementary solution · original**

Find a particular solution of $y''-y'-2y=3e^{2t}$.

1. Complementary: $s^2-s-2=(s-2)(s+1)$.

   $$y_c=C_1e^{2t}+C_2e^{-t}$$
2. The table says $Ae^{2t}$, but that is in $y_c$: it gives $0=3e^{2t}$. Multiply by $t$.

   $$y_p=Ate^{2t}$$
3. Product rule, twice.

   $$y_p'=A(1+2t)e^{2t},\qquad y_p''=A(4+4t)e^{2t}$$
4. Substitute and divide by $e^{2t}$. The $t$ terms cancel.

   $$A\big[(4+4t)-(1+2t)-2t\big]=3A=3$$
5. Solve.

   $$A=1$$

**Answer:** $y_p=te^{2t}$, so $y=C_1e^{2t}+C_2e^{-t}+te^{2t}$.

```graph
title "Why the extra t: forcing at the natural frequency"
x 0 12 label="$t$"
y -25 25 label="$y$"
slider w 1 3 1.5 step=0.05 label="$\omega$" animate
curve "if(abs(w-2)<0.001, sin(2*x)-2*x*cos(2*x), 8/(4-w^2)*(sin(w*x)-w/2*sin(2*x)))" label="$y(t)$, starting at rest" color=1
curve "2*x" label="$\pm2t$" color=0 dash
curve "-2*x" color=0 dash
caption "Solutions of $y''+4y=8\sin\omega t$ with $y(0)=y'(0)=0$. Here $y_c$ contains $\sin2t$ and $\cos2t$. For $\omega$ far from 2 the swing stays small. At $\omega=2$ the forcing is in $y_c$, the particular solution has the extra $t$, and the swing grows along $\pm2t$."
```

**Problem: Try it 3 · Choose the form; do not solve · original** (introductory)

For $y''-2y'+y=g(t)$, write the guess for $y_p$ when $g$ is (a) $t^2$, (b) $e^{-t}$, (c) $e^t$, (d) $\cos t$.

<details><summary>Solution</summary>

1. Complementary first: $s^2-2s+1=(s-1)^2$, a repeated root.

   $$y_c=(C_1+C_2t)e^t$$
2. (a) Degree 2: all lower powers.

   $$At^2+Bt+C$$
3. (b) $e^{-t}$ is not in $y_c$.

   $$Ae^{-t}$$
4. (c) $Ae^t$ and $Ate^t$ are both in $y_c$, so multiply by $t^2$.

   $$At^2e^t$$
5. (d) Cosine needs both cosine and sine.

   $$A\cos t+B\sin t$$

**Answer:** (a) $At^2+Bt+C$. (b) $Ae^{-t}$. (c) $At^2e^t$. (d) $A\cos t+B\sin t$.

</details>

**Problem: Try it 4 · A trig guess that is already in the complementary solution · original** (introductory)

Find a particular solution of $y''+9y=12\cos3t$. Use $(tf)^{\prime\prime}=tf^{\prime\prime}+2f^{\prime}$ from Try it 1.

<details><summary>Solution</summary>

1. $y_c=c_1\cos3t+c_2\sin3t$ already contains $\cos3t$, so multiply the guess by $t$.

   $$y_p=t\,f,\qquad f=A\cos3t+B\sin3t$$
2. Since $f^{\prime\prime}=-9f$, the $t$ terms cancel in $y_p^{\prime\prime}+9y_p$.

   $$y_p''+9y_p=t(f''+9f)+2f'=2f'$$
3. Differentiate $f$.

   $$2f'=-6A\sin3t+6B\cos3t$$
4. Match with 12 cos 3t.

   $$6B=12,\qquad -6A=0$$

**Answer:** $A=0$, $B=2$: $y_p=2t\sin3t$. The swing grows like $2t$, as in the graph above.

</details>
