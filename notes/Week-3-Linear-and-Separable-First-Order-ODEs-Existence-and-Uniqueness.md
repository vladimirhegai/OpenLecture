# Week 3: Linear and Separable First-Order ODEs; Existence and Uniqueness

## Calculus refresher: integrate, then check by differentiating

Week 2 gave you solution families. This week you learn how to find them: rearrange the equation until integrating can undo its derivatives.

Add an arbitrary constant $K$ to each indefinite integral below.

| Integral | Detail that is easy to forget |
|---|---|
| $\int t^n\,dt=\dfrac{t^{n+1}}{n+1}$ | Increase the power by one and divide by the new power; this excludes $n=-1$. |
| $\int\dfrac{1}{t}\,dt=\ln|t|$ | The logarithm is the special case. Work on an interval that avoids $t=0$. |
| $\int e^{at}\,dt=\dfrac{1}{a}e^{at}$ | Divide by the constant $a\ne0$; differentiation would multiply by it. |

**Substitution** reverses the chain rule. For $\int\dfrac{2t}{1+t^2}\,dt$, choose $u=1+t^2$; then $du=2t\,dt$, so the integral becomes $\int du/u=\ln(1+t^2)+K$.

Keep the differential with its variable: integrate $y\,dy$ with respect to $y$, and $t\,dt$ with respect to $t$. After integrating both sides of an equation, one free constant is enough because two constants can be combined.

**Problem: Try it 1 · Two small integration checks · original** (introductory)

Find: (a) $\int y^{-2}\,dy$; (b) $\int 6e^{3t}\,dt$. Check each by differentiating.

<details><summary>Solution</summary>

1. For (a), the new power is −1; divide by −1.

   $$\int y^{-2}\,dy=-y^{-1}+K$$
2. For (b), divide by the exponent coefficient 3.

   $$\int6e^{3t}\,dt=2e^{3t}+K$$

**Answer:** (a) $-1/y+K$, for $y\ne0$. (b) $2e^{3t}+K$.

</details>

## Week 3 overview

First learn separation, which puts each variable on its own side. Then learn the integrating factor for linear equations. Finally, ask what can be guaranteed about an IVP before solving it; those guarantees are a different task from finding a formula.

## Topic 1: Separable equations

### Separate first; integrate second

An equation is **separable** when $y'=g(t)h(y)$: a function of $t$ multiplied by a function of $y$. The aim is to put the $y$-expression beside $dy$ and the $t$-expression beside $dt$.

$$\dfrac{1}{h(y)}\,dy=g(t)\,dt$$

This rearrangement assumes $h(y)\ne0$. Whenever you divide by an expression involving the unknown, check its zero cases in the original equation too.

**Example: Example 1 · A first complete separation · original**

Solve $y'=2ty$ with $y(0)=3$.

1. For $y\ne0$, separate the variables.

   $$\dfrac{dy}{y}=2t\,dt$$
2. Integrate each side in its own variable.

   $$\ln|y|=t^2+K$$
3. Exponentiate. Combine the constant and the possible sign into $A$.

   $$y=Ae^{t^2}$$
4. Use $y(0)=3$, so $A=3$.

   $$y=3e^{t^2}$$

**Answer:** $y=3e^{t^2}$. The divided-out case $y=0$ also solves the ODE, but fails this initial condition.

**Problem: Try it 2 · Only do the separation · warm-up and lecture equation** (introductory)

Rearrange each equation so it is ready to integrate. **Stop before integrating.**

1. $y'=t(1+y^2)$
2. $y'=\dfrac{3t+ty^2}{y+t^2y}$

<details><summary>Solution</summary>

1. 1. Divide by the positive expression 1 + y².

   $$\dfrac{dy}{1+y^2}=t\,dt$$
2. 2. Factor numerator and denominator before rearranging.

   $$y'=\dfrac{t(3+y^2)}{y(1+t^2)}$$
3. Keep every y-term on the left.

   $$\dfrac{y}{3+y^2}\,dy=\dfrac{t}{1+t^2}\,dt$$

**Answer:** 1. $dy/(1+y^2)=t\,dt$. 2. $\dfrac{y}{3+y^2}\,dy=\dfrac{t}{1+t^2}\,dt$; the original equation requires $y\ne0$.

</details>

**Example: Example 2 · Finish the factored equation · lecture Example 3.3**

Use the separated form from question 2, now with $y(1)=3$.

1. On both sides, the numerator is half the derivative of the denominator.

   $$\dfrac12\ln(3+y^2)=\dfrac12\ln(1+t^2)+K$$
2. Multiply by 2 and exponentiate; call the positive constant A.

   $$3+y^2=A(1+t^2)$$
3. Use the initial condition before choosing a square-root branch.

   $$3+3^2=A(1+1^2)\quad\Rightarrow\quad A=6$$
4. The positive branch matches y(1) = 3.

   $$y=\sqrt{6t^2+3}$$

**Answer:** $y=\sqrt{6t^2+3}$ for all real $t$. It stays positive, so the original denominator never vanishes.

**Problem: Try it 3 · Use an initial value and choose the interval · Pre-tutorial 3(a)** (introductory)

Solve $y'=-t/y$ with $y(1)=2$. After finding the formula, identify the largest open interval containing $t=1$ where it satisfies the original ODE.

<details><summary>Solution</summary>

1. Multiply by y and separate.

   $$y\,dy=-t\,dt$$
2. Integrate, then absorb the factor 2 into the constant.

   $$y^2+t^2=K$$
3. Use the starting point and choose its positive branch.

   $$K=2^2+1^2=5,\qquad y=\sqrt{5-t^2}$$
4. The original equation divides by y, so exclude the endpoints where y = 0.

   $$-\sqrt5<t<\sqrt5$$

**Answer:** $y=\sqrt{5-t^2}$ on $(-\sqrt5,\sqrt5)$.

</details>

### Two things integration can hide

**A lost solution:** for $y^{\prime}=y^2/t^3$, separating divides by $y^2$. Integration gives $-1/y=-1/(2t^2)+K$, or $y=2t^2/(1-2Kt^2)$, but $y=0$ also solves the original equation and must be included separately.

Here $t\ne0$, and the displayed denominator must also stay nonzero. Keep the solution on a connected interval avoiding those restrictions.

**An implicit answer:** sometimes integration gives a relation between $t$ and $y$ that you cannot conveniently rearrange into $y=\cdots$. That relation can still describe a solution; check it by implicit differentiation.

**Problem: Try it 4 · Solve in differential form · Pre-tutorial 3(b)** (introductory)

Solve $3t(y^2+1)\,dt+y(t^2+2)\,dy=0$. An implicit answer is enough.

<details><summary>Solution</summary>

1. Move the dt-term and divide by the positive factors.

   $$\dfrac{y}{y^2+1}\,dy=-\dfrac{3t}{t^2+2}\,dt$$
2. Use substitution on both sides.

   $$\dfrac12\ln(y^2+1)=-\dfrac32\ln(t^2+2)+K$$
3. Multiply by 2, combine logs, and exponentiate.

   $$(y^2+1)(t^2+2)^3=A$$

**Answer:** $(y^2+1)(t^2+2)^3=A$, with $A>0$ for real solution points. A differentiable branch must still satisfy the original equation.

</details>

The lecture’s other implicit example is $y\,dt+t^3(y^2+1)\,dy=0$. For $t\ne0$ and $y\ne0$, separation gives $(y+1/y)\,dy=-t^{-3}\,dt$, hence $y^2+2\ln|y|-t^{-2}=K$. Check $y=0$ separately: it also solves the original differential form.

## Topic 2: Linear equations and integrating factors

### Make the derivative stand alone first

A first-order linear equation has standard form $y'+a(t)y=f(t)$. The coefficient $a(t)$ and forcing $f(t)$ may depend on $t$, but not on the unknown $y$.

**Problem: Try it 5 · Identify the coefficient before doing calculus · original** (introductory)

Put each equation into standard form and identify $a(t)$ and $f(t)$.

1. $y'=3y+6$
2. $ty'+2y=4t^2$, with $t>0$.

<details><summary>Solution</summary>

1. 1. Move 3y left and keep its negative sign.

   $$y'-3y=6,\quad a=-3,\quad f=6$$
2. 2. Divide every term by t.

   $$y'+\dfrac2t y=4t,\quad a=\dfrac2t,\quad f=4t$$

**Answer:** 1. $a=-3$, $f=6$. 2. $a=2/t$, $f=4t$.

</details>

### Why multiplying helps

The product rule says $(\mu y)'=\mu y'+\mu'y$, where $\mu$ is a function of $t$. If we choose $\mu$ so that $\mu'=a\mu$, multiplying the linear ODE by it makes the entire left side one derivative.

```steps
title "Build the integrating-factor method"
$$ y'+a(t)y=f(t) $$
Start in standard form.
$$ \mu=e^{\int a(t)\,dt} $$
This choice has derivative μ′ = aμ.
$$ \mu y'+\hl{\mu a}y=\mu f $$
Multiply every term by μ.
$$ \hl{(\mu y)'}=\mu f $$
Recognise the product rule backwards.
$$ \mu y=\hl{\int\mu f\,dt+K} $$
Integrate once.
$$ y=\hl{\dfrac{1}{\mu}}\left(\int\mu f\,dt+K\right) $$
Divide by μ, then use the initial condition.
```

Use one convenient antiderivative inside $\mu$; you do not need an extra integration constant there. Multiplying $\mu$ by a nonzero constant would give an equivalent method.

**Example: Example 3 · Use the method with simple numbers · original**

Solve $y'+2y=6$, $y(0)=1$. This recovers Week 2’s solution without being given its family.

1. The coefficient is 2, so compute the factor.

   $$\mu=e^{\int2\,dt}=e^{2t}$$
2. Multiply and recognise the product derivative.

   $$\dfrac{d}{dt}(e^{2t}y)=6e^{2t}$$
3. Integrate; divide by 2 when integrating the exponential.

   $$e^{2t}y=3e^{2t}+K$$
4. Divide by the factor and use the starting value.

   $$y=3+Ke^{-2t},\quad 1=3+K$$
5. The initial condition sets K = −2.

   $$y=3-2e^{-2t}$$

**Answer:** $y=3-2e^{-2t}$.

**Problem: Try it 6 · A coefficient that varies with time · original** (introductory)

Finish $ty'+2y=4t^2$, $y(1)=2$, on $t>0$. You already found its standard form above. Find the integrating factor, integrate, and apply the condition.

<details><summary>Solution</summary>

1. Integrate 2/t and simplify the exponential.

   $$\mu=e^{2\ln t}=t^2$$
2. Multiply the standard form by t².

   $$\dfrac{d}{dt}(t^2y)=4t^3$$
3. Integrate and divide by t².

   $$t^2y=t^4+K,\qquad y=t^2+\dfrac{K}{t^2}$$
4. At t = 1, the given value is 2.

   $$2=1+K\quad\Rightarrow\quad K=1$$

**Answer:** $y=t^2+1/t^2$ on $t>0$.

</details>

### Choose a method, then handle a harder integral

**Problem: Try it 7 · Separable, linear, both, or neither? · original** (introductory)

Identify the method; do not solve.

1. $y'=t^2+y$
2. $y'=e^{t+y}$
3. $y'=2y-6$
4. $y'=t+y^2$

<details><summary>Solution</summary>

1. 1. Linear; its sum does not separate into a t-factor times a y-factor.
2. 2. Write $e^{t+y}=e^te^y$: separable, nonlinear.
3. 3. Linear and separable; the right side is a function of y alone.
4. 4. Neither linear nor separable.

**Answer:** 1. Linear only. 2. Separable only. 3. Both. 4. Neither.

</details>

**Example: Example 4 · Use substitution inside the method · lecture Example 3.1**

Solve $y'+\dfrac{10}{2t+5}y=10$, $y(0)=0$.

1. Use $u=2t+5$, $du=2\,dt$ to integrate the coefficient.

   $$\int\dfrac{10}{2t+5}\,dt=5\ln|2t+5|$$
2. The interval containing 0 has $t>-5/2$, so $2t+5>0$.

   $$\mu=(2t+5)^5$$
3. Multiply; the left side becomes a product derivative.

   $$\dfrac{d}{dt}\big[(2t+5)^5y\big]=10(2t+5)^5$$
4. Use the same substitution on the right.

   $$(2t+5)^5y=\dfrac56(2t+5)^6+K$$
5. Apply y(0) = 0 before dividing.

   $$0=\dfrac56\,5^6+K\quad\Rightarrow\quad K=-\dfrac{5^7}{6}$$
6. Divide by the integrating factor.

   $$y=\dfrac56(2t+5)-\dfrac{5^7}{6(2t+5)^5}$$

**Answer:** The displayed solution holds on $t>-5/2$, the interval containing the starting time.

**A brief integration-by-parts refresher:** if multiplying by $\mu$ leaves an integral such as $\int4te^{2t}\,dt$, use $\int u\,dv=uv-\int v\,du$. Choose $u=4t$, $dv=e^{2t}dt$; then $du=4dt$ and $v=e^{2t}/2$.

$$\int4te^{2t}\,dt=2te^{2t}-e^{2t}+K$$

**Problem: Try it 8 · When the integral needs parts · original** (introductory)

Solve $y'+2y=4t$, $y(0)=1$. Use the integral just shown rather than learning a new ODE method.

<details><summary>Solution</summary>

1. The factor is still e²ᵗ; only the right-hand integral changes.

   $$\dfrac{d}{dt}(e^{2t}y)=4te^{2t}$$
2. Use the integration-by-parts result.

   $$e^{2t}y=2te^{2t}-e^{2t}+K$$
3. Divide and apply the initial condition.

   $$y=2t-1+Ke^{-2t},\quad K=2$$

**Answer:** $y=2t-1+2e^{-2t}$.

</details>

**Problem: Try it 9 · One equation, two methods · Pre-tutorial 3(c)** (introductory)

For $y'=8ty+3y$, find the general solution using separation. Then identify the integrating factor and explain how it gives the same family, including the zero solution.

<details><summary>Solution</summary>

1. Factor y, divide by it for nonzero solutions, and integrate.

   $$\ln|y|=4t^2+3t+K$$
2. Exponentiate; restore the divided-out solution by allowing A = 0.

   $$y=Ae^{4t^2+3t}$$
3. In linear form, a(t) = −(8t + 3).

   $$\mu=e^{-(4t^2+3t)}$$
4. The product derivative is zero, so its value is an arbitrary constant.

   $$\dfrac{d}{dt}(\mu y)=0\quad\Rightarrow\quad\mu y=A$$

**Answer:** $y=Ae^{4t^2+3t}$ for any real $A$. The integrating-factor route never divides by $y$, so $A=0$ is included directly.

</details>

### Circuit connection: the lecture’s RL equation

The lecture uses $2i^{\prime}+10i=100$, $i(0)=0$. The drawing below follows that KVL equation, with the source positive at the top; the printed circuit figure has its source polarity reversed.

```schematic
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$10\,\Omega$"
L1 6,3 -> 6,0 "$2\,\mathrm{H}$" i="$i$" v="$v_L$"
wire 6,0 -> 0,0
ground 0,0
#~ flow
#~ init L1 0
#@ view "Just after closing"
#@ node a 100 "source: $100\,\mathrm{V}$"
#@ node b 100 "after switch: $100\,\mathrm{V}$"
#@ node c 100 "inductor: $100\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$100\,\mathrm{V}$" col=0 id=src
#@ el W a b "closed" col=1
#@ el R b c "$10\,\Omega$" col=2 id=res
#@ el L c g "$2\,\mathrm{H}$" col=3 plus=c v="$v_L$" id=ind
#@ step "Ground the bottom wire." show=g
#@ step "The source fixes the top at 100 V; the closed switch has no step." show=a,b,src
#@ step "Current starts at zero, so R has no fall; L takes all 100 V." show=c,res,ind
#@ view "At one time constant"
#@ node a 100 "source: $100\,\mathrm{V}$"
#@ node b 100 "after switch: $100\,\mathrm{V}$"
#@ node c 36.787944 "inductor: $36.79\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$100\,\mathrm{V}$" col=0 i="$6.32\,\mathrm{A}$" to=a
#@ el W a b "closed" col=1 i="$6.32\,\mathrm{A}$" to=b
#@ el R b c "$10\,\Omega$" col=2 i="$6.32\,\mathrm{A}$" to=c
#@ el L c g "$2\,\mathrm{H}$" col=3 plus=c v="$v_L$" i="$6.32\,\mathrm{A}$" to=g
#@ note "Ground the bottom wire. At t = 0.2 s, i = 10(1 - 1/e) A. The 100 V source equals the resistor fall plus the inductor voltage."
#@ view "DC final value"
#@ node a 100 "source: $100\,\mathrm{V}$"
#@ node b 100 "after switch: $100\,\mathrm{V}$"
#@ node c 0 "inductor: $0\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$100\,\mathrm{V}$" col=0 i="$10\,\mathrm{A}$" to=a
#@ el W a b "closed" col=1 i="$10\,\mathrm{A}$" to=b
#@ el R b c "$10\,\Omega$" col=2 i="$10\,\mathrm{A}$" to=c
#@ el L c g "$2\,\mathrm{H}$" col=3 plus=c v="$v_L$" i="$10\,\mathrm{A}$" to=g
#@ note "Ground the bottom wire. The inductor is a DC short; i = 100/10 = 10 A."
```

Divide by $2$: $i'+5i=50$, so $\mu=e^{5t}$. Integrating $(e^{5t}i)'=50e^{5t}$ gives $i=10+Ke^{-5t}$; $i(0)=0$ sets $K=-10$, hence $i=10(1-e^{-5t})\,\mathrm{A}$.

Separation gives the same result: $di/(50-5i)=dt$, then $-\frac15\ln|50-5i|=t+K$. Its final current $10\,\mathrm{A}$ and time constant $2/10=0.2\,\mathrm{s}$ match Week 2’s circuit reasoning.

## Topic 3: Existence and uniqueness

### Calculus reminder: a partial derivative holds t fixed

For a function of two variables, $F(t,y)$, the symbol $\partial F/\partial y$ means differentiate with respect to $y$ while treating $t$ as a constant. For example, if $F=t^2+3ty$, then $\partial F/\partial y=3t$.

Write the ODE as $y'=F(t,y)$. If $F$ and $\partial F/\partial y$ are real-valued and continuous on an open region around the initial point, the IVP has exactly one solution on some interval near its starting time.

- **Existence:** there is a solution through the starting point.
- **Uniqueness:** there is only one such solution locally.
- **If the conditions fail:** this theorem gives no conclusion; inspect the equation separately.
- **Local guarantee:** even smooth formulas do not guarantee that a solution survives for all time.

**Example: Example 5 · Check the point, without solving the ODE · original**

For $y'=(t+y)/(t-y)$, check whether the theorem guarantees a unique local solution through $(0,1)$ and through $(2,2)$.

1. The denominator vanishes on the line t = y.

   $$F=\dfrac{t+y}{t-y}$$
2. Use the quotient rule in y, holding t fixed.

   $$\dfrac{\partial F}{\partial y}=\dfrac{2t}{(t-y)^2}$$
3. Both expressions are continuous near (0,1), which is off that line.
4. At (2,2), the original right side is undefined; it cannot define a classical solution through that point.

**Answer:** (0,1): a unique local solution is guaranteed. (2,2): the theorem does not apply, and the ODE itself is undefined there.

**Problem: Try it 10 · Find a region containing the start · original** (introductory)

For $(t-3)y'+(\ln t)y=2t$ with $y(1)=2$, find the region containing the starting point where the theorem applies. Do not solve.

<details><summary>Solution</summary>

1. First isolate the derivative.

   $$F=\dfrac{2t-(\ln t)y}{t-3}$$
2. Differentiate only with respect to y.

   $$\dfrac{\partial F}{\partial y}=-\dfrac{\ln t}{t-3}$$
3. The log requires t > 0, and division excludes t = 3. The start has t = 1.

   $$0<t<3,\qquad\text{any real }y$$

**Answer:** The strip $0<t<3$ contains the initial point and gives the local uniqueness guarantee.

</details>

**A local solution can end:** $y'=y^2$, $y(0)=1$ has solution $y=1/(1-t)$ on $t<1$. It blows up at $t=1$ despite smooth $F$ and $F_y$.

**A failed test can allow multiple solutions:** for $y'=y^{1/3}$ at $y=0$, $F$ is continuous but $F_y$ is not. Both $y=0$ and a function that stays zero for $t\le0$ then follows $(2t/3)^{3/2}$ for $t>0$ solve the IVP with $y(0)=0$.

```graph
title "A failed uniqueness test can allow several curves"
x -1 4 label="$t$"
y -0.2 3 label="$y$"
family c 0 2 0.5 "if(t>c,(2*max(0,t-c)/3)^1.5,0)" color=2
hline "0" label="zero solution" color=1
caption "Each purple solution stays at zero until its own departure time. They all pass through (0,0); the y-partial derivative of F fails there."
```
