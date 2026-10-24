# Calculus Refresher

**Week 0 · ELEC 231 · preparation for weeks 1–5**

Read in order: each example uses only rules already introduced. Try the short questions before opening their solutions; use **Next** to follow the equation changes.

## Algebra and notation

$t$ is time, usually in seconds. $y(t)$ means “the value of $y$ at time $t$”; it does **not** mean $y$ multiplied by $t$.

| Symbol | Meaning here |
|---|---|
| $y(t)$ | A general unknown function. |
| $i(t)$, $v(t)$ | Current in amperes (A), voltage in volts (V). |
| $R$, $L$, $C$ | Resistance, inductance, capacitance: fixed component values. |
| $K$, $K_1$, $K_2$ | Unknown constants to determine; we use K so it is not confused with capacitance C. |
| $y(0)=3$ | The function starts at 3 when t = 0. |
| $y(t)\to 3$ as $t\to\infty$ | As time grows, y approaches 3. |

### Exponentials and logarithms

An **exponential** has the variable in its exponent: $e^t$, where $e\approx2.718$. For $a>0$, $e^{-at}$ starts at 1 and approaches 0; a larger $a$ makes it fall faster.

| Rule | Example |
|---|---|
| $t^{-n}=\dfrac{1}{t^n}$; $t^{1/2}=\sqrt t$ | $t^{-2}=\dfrac1{t^2}$ |
| $e^0=1$; $e^{A+B}=e^Ae^B$ | $e^{2-2t}=e^2e^{-2t}$ |
| $\ln(e^A)=A$; $e^{\ln A}=A$ for $A>0$ | $e^{-2t}=\dfrac12\ \Rightarrow\ -2t=-\ln2$ |
| $\ln(AB)=\ln A+\ln B$ for $A,B>0$ | $\ln(4e^{-2t})=\ln4-2t$ |

$\ln$ is the **natural logarithm**: it undoes an exponential with base $e$. It lets you bring an exponent down so you can solve for time.

**Example: Example 1 · When has a current halved?**

A current is $i(t)=4e^{-2t}\,\mathrm A$. Find when it reaches $2\,\mathrm A$. No calculus yet.

1. ```steps
$$ 2=4e^{-2t} $$
Put the requested current into the formula.
$$ \hl{\dfrac12}=e^{-2t} $$
Divide both sides by 4.
$$ \hl{\ln(1/2)}=\hl{-2t} $$
Take ln of both sides; ln undoes the exponential.
$$ t=\hl{\dfrac{\ln2}{2}}\approx0.347\,\mathrm s $$
Since ln(1/2) = −ln 2, dividing by −2 gives a positive time.
```

**Answer:** $t=\dfrac{\ln2}{2}\approx0.347\,\mathrm s$.

**Problem: Try it 1 · Solve for time** (introductory)

A voltage is $v(t)=12(1-e^{-3t})\,\mathrm V$. When does it reach $9\,\mathrm V$?

<details><summary>Solution</summary>

1. ```steps
$$ 9=12(1-e^{-3t}) $$
Substitute the requested voltage.
$$ e^{-3t}=\hl{\dfrac14} $$
Divide by 12, then isolate the exponential.
$$ -3t=\hl{\ln(1/4)=-\ln4} $$
Take ln of both sides.
$$ t=\hl{\dfrac{\ln4}{3}}\approx0.462\,\mathrm s $$
Divide by −3.
```

**Answer:** $t=\dfrac{\ln4}{3}\approx0.462\,\mathrm s$.

</details>

## Derivatives

### Basic derivative rules (Week 2 & Week 3)

A **derivative** is the slope of a function at one instant. A rising curve has a positive derivative; a falling curve has a negative one.

$$y^{\prime}(t)=\dfrac{dy}{dt}$$

These are two names for the same derivative. If $i$ is in amperes and $t$ in seconds, $\dfrac{di}{dt}$ is in A/s; it tells you how fast the current changes.

| Function | Derivative with respect to t |
|---|---|
| $k$ (constant) | $0$ |
| $t^n$ | $nt^{n-1}$ |
| $e^t$ | $e^t$ |
| $\ln|t|$ ($t\ne0$) | $\dfrac1t$ |
| $\sin t$ | $\cos t$ |
| $\cos t$ | $-\sin t$ |

Differentiate sums term by term; keep constant multipliers. For trig derivatives, angles must be in **radians** ($\pi$ radians $=180^\circ$).

**Example: Example 2 · Differentiate term by term**

Find the derivative of $y(t)=3t^2-4t+2$.

1. ```steps
$$ y=3t^2-4t+2 $$
Start with the function.
$$ y^{\prime}=3\hl{(2t)}-4\hl{(1)}+\hl{0} $$
Use the power rule; the derivative of a constant is zero.
$$ y^{\prime}=\hl{6t-4} $$
Collect the terms.
```

**Answer:** $y^{\prime}=6t-4$.

**Problem: Try it 2 · A slope at a particular time** (introductory)

For $y(t)=t^3-2t$, find $\dfrac{dy}{dt}$ and its value at $t=1$. Is the curve rising or falling there?

<details><summary>Solution</summary>

1. ```steps
$$ y^{\prime}=\hl{3t^2-2} $$
Use the power rule on each term.
$$ y^{\prime}(1)=3(1)^2-2=\hl{1} $$
Differentiate first, then put in t = 1.
```

**Answer:** $y^{\prime}=3t^2-2$; $y^{\prime}(1)=1>0$, so it is rising there.

</details>

### Chain rule (Week 2 & Week 3)

In $e^{-2t}$, the outside function is the exponential and the inside is $-2t$. Differentiate the outside, keep the inside, then **multiply by the derivative of the inside**.

$$\dfrac{d}{dt}f(g(t))=f^{\prime}(g(t))g^{\prime}(t)$$

**Example: Example 3 · The rate of an exponential decay**

Find $\dfrac{di}{dt}$ for $i(t)=4e^{-2t}\,\mathrm A$.

1. ```steps
$$ i=4e^{-2t} $$
The 4 stays as a constant multiplier.
$$ \dfrac{di}{dt}=4e^{-2t}\hl{(-2)} $$
The exponential stays; multiply by the derivative of −2t.
$$ \dfrac{di}{dt}=\hl{-8e^{-2t}} $$
The negative sign means the current is decreasing.
```

**Answer:** $\dfrac{di}{dt}=-8e^{-2t}\,\mathrm{A/s}$.

```graph
title "Slide the time: current and its slope"
x 0 3 label="$t$ (s)"
y -1 4.5 label="$i$ (A)"
slider T 0 2.5 0.5 step=0.05 label="time $T$ (s)"
curve "4*exp(-2*t)" label="$i(t)=4e^{-2t}$"
curve "4*exp(-2*T)-8*exp(-2*T)*(t-T)" from="max(0,T-0.3)" to="T+0.3" color=2 label="tangent: slope at $T$"
point "T" "4*exp(-2*T)" color=2
readout "$i(T)=$" "4*exp(-2*T)" unit=" A"
readout "$i'(T)=$" "-8*exp(-2*T)" unit=" A/s"
caption "Move T forward: the current still decreases, but the tangent becomes less steep."
```

| Pattern | Derivative |
|---|---|
| $e^{at}$ | $ae^{at}$ |
| $\sin(\omega t)$ | $\omega\cos(\omega t)$ |
| $\cos(\omega t)$ | $-\omega\sin(\omega t)$ |
| $\ln|g(t)|$ | $\dfrac{g^{\prime}(t)}{g(t)}$ where $g(t)\ne0$ |

$a$ and $\omega$ (omega) are constants. For example, $\dfrac{d}{dt}\cos(2t)=-2\sin(2t)$: the extra 2 comes from the inside.

**Problem: Try it 3 · A voltage building up** (intermediate)

For $v(t)=12-10e^{-5t}\,\mathrm V$, find $\dfrac{dv}{dt}$ and the initial rate $v^{\prime}(0)$.

<details><summary>Solution</summary>

1. ```steps
$$ v^{\prime}=0-10e^{-5t}\hl{(-5)} $$
Differentiate the constant and use the chain rule.
$$ v^{\prime}=\hl{50e^{-5t}} $$
The two negative signs cancel.
$$ v^{\prime}(0)=50e^0=\hl{50} $$
At t = 0, the exponential is 1.
```

**Answer:** $v^{\prime}(t)=50e^{-5t}\,\mathrm{V/s}$; $v^{\prime}(0)=50\,\mathrm{V/s}$.

</details>

**Problem: Try it 4 · A changing logarithm** (intermediate)

Differentiate $y(t)=\ln(1+t^2)$.

<details><summary>Solution</summary>

1. ```steps
$$ y=\ln(1+t^2) $$
The outside is ln; the inside is 1 + t².
$$ y^{\prime}=\dfrac{1}{1+t^2}\hl{(2t)} $$
Multiply the outside derivative by the inside derivative.
$$ y^{\prime}=\hl{\dfrac{2t}{1+t^2}} $$
Combine the factors.
```

**Answer:** $y^{\prime}=\dfrac{2t}{1+t^2}$.

</details>

### Product rule and second derivatives (Week 2 & Week 3)

For a product of two changing functions, both contribute to the derivative. You do **not** multiply their derivatives together.

$$\dfrac{d}{dt}(uv)=u^{\prime}v+uv^{\prime}$$

$u$ and $v$ here are any two functions of $t$. A **second derivative**, $y^{\prime\prime}=\dfrac{d^2y}{dt^2}$, means differentiate the result again; it is not $(y^{\prime})^2$.

**Example: Example 4 · A product you will see with repeated roots**

Find $y^{\prime}$ and $y^{\prime\prime}$ for $y=te^{-2t}$.

1. ```steps
$$ y=te^{-2t} $$
There are two changing factors.
$$ y^{\prime}=\hl{1}e^{-2t}+t\hl{(-2e^{-2t})} $$
Differentiate each factor in turn, using the product rule.
$$ y^{\prime}=\hl{(1-2t)e^{-2t}} $$
Factor out the common exponential.
$$ y^{\prime\prime}=\hl{-2}e^{-2t}+(1-2t)\hl{(-2e^{-2t})} $$
Differentiate again with the product rule.
$$ y^{\prime\prime}=\hl{(4t-4)e^{-2t}} $$
Collect the factors multiplying the exponential.
```

**Answer:** $y^{\prime}=(1-2t)e^{-2t}$; $y^{\prime\prime}=(4t-4)e^{-2t}$.

**Problem: Try it 5 · Differentiate twice** (intermediate)

Find $y^{\prime}$ and $y^{\prime\prime}$ for $y=(2+t)e^{-t}$.

<details><summary>Solution</summary>

1. ```steps
$$ y^{\prime}=e^{-t}-(2+t)e^{-t}=\hl{-(1+t)e^{-t}} $$
Apply the product rule and combine.
$$ y^{\prime\prime}=-e^{-t}+(1+t)e^{-t} $$
Apply the product rule again, keeping the initial minus sign.
$$ y^{\prime\prime}=\hl{te^{-t}} $$
Combine the terms.
```

**Answer:** $y^{\prime}=-(1+t)e^{-t}$; $y^{\prime\prime}=te^{-t}$.

</details>

### Quotient rule (Week 2 & Week 3)

For a fraction, use the **quotient rule**: bottom × derivative of top, minus top × derivative of bottom, all over bottom squared.

$$\dfrac{d}{dt}\left(\dfrac uv\right)=\dfrac{vu^{\prime}-uv^{\prime}}{v^2}$$

**Example: Example 5 · A quotient**

Differentiate $y=\dfrac{t}{1+t}$, for $t\ne-1$.

1. ```steps
$$ y^{\prime}=\dfrac{(1+t)\hl{(1)}-t\hl{(1)}}{(1+t)^2} $$
Here the derivatives of both the top and bottom are 1.
$$ y^{\prime}=\hl{\dfrac{1}{(1+t)^2}} $$
The t terms cancel in the numerator.
```

**Answer:** $y^{\prime}=\dfrac1{(1+t)^2}$.

**Problem: Try it 6 · Keep the quotient-rule signs** (introductory)

Differentiate $y=\dfrac{1+t}{1-t}$, for $t\ne1$.

<details><summary>Solution</summary>

1. ```steps
$$ y^{\prime}=\dfrac{(1-t)(1)-(1+t)\hl{(-1)}}{(1-t)^2} $$
The derivative of the bottom is −1.
$$ y^{\prime}=\dfrac{1-t+1+t}{(1-t)^2}=\hl{\dfrac2{(1-t)^2}} $$
Subtracting a negative gives a plus.
```

**Answer:** $y^{\prime}=\dfrac2{(1-t)^2}$.

</details>

### Partial derivatives (Week 3)

For a function $U(t,y)$ with two inputs, a **partial derivative** changes one input while holding the other fixed. The curly $\partial$ marks this difference.

**Example: Example 6 · Partial and mixed derivatives**

For $U(t,y)=t^2y+3y^2$, find $U_t=\dfrac{\partial U}{\partial t}$ and $U_y=\dfrac{\partial U}{\partial y}$.

1. ```steps
$$ U=t^2y+3y^2 $$
Start with two independent inputs.
$$ U_t=\hl{2ty} $$
Hold y fixed: 3y² is constant with respect to t.
$$ U_y=\hl{t^2+6y} $$
Hold t fixed: the derivative of t²y with respect to y is t².
$$ U_{ty}=\hl{2t}=U_{yt} $$
Differentiate each result in the other variable; these mixed partials agree.
```

**Answer:** $U_t=2ty$; $U_y=t^2+6y$; both mixed partial derivatives are $2t$.

**Problem: Try it 7 · A partial derivative with trig** (introductory)

For $U(t,y)=t^2\sin y+y^3$, find $U_t$ and $U_y$.

<details><summary>Solution</summary>

1. ```steps
$$ U_t=\hl{2t\sin y} $$
Hold y fixed, so sin y is a constant multiplier.
$$ U_y=\hl{t^2\cos y+3y^2} $$
Hold t fixed and differentiate the y terms.
```

**Answer:** $U_t=2t\sin y$; $U_y=t^2\cos y+3y^2$.

</details>

### Implicit differentiation (Week 3)

**Implicit differentiation** is different: now $y=y(t)$ changes along a curve. When differentiating $y^2$ with respect to $t$, the chain rule gives $2yy^{\prime}$.

**Example: Example 7 · Implicit derivative of a circle**

Find $y^{\prime}$ from $t^2+y^2=5$.

1. ```steps
$$ t^2+y^2=5 $$
The equation describes a curve; y depends on t along it.
$$ 2t+\hl{2yy^{\prime}}=0 $$
Differentiate in t; y² needs the chain rule.
$$ y^{\prime}=\hl{-\dfrac ty} $$
Solve for the derivative where y is nonzero.
```

**Answer:** $y^{\prime}=-\dfrac ty$ where $y\ne0$. In contrast, $\partial(y^2)/\partial t=0$ when y is held fixed.

## Integrals

### Indefinite integrals (Week 2)

An **antiderivative** of $f(t)$ is a function whose derivative is $f(t)$. An **indefinite integral** asks for all of those functions, so include an arbitrary constant $K$.

$$\int f(t)\,dt=F(t)+K\quad\text{if }F^{\prime}(t)=f(t)$$

The $dt$ tells you the integration variable. The constant is necessary because $F$, $F+3$ and $F-8$ all have the same derivative.

| Integrand | Indefinite integral |
|---|---|
| $t^n$, $n\ne-1$ | $\dfrac{t^{n+1}}{n+1}+K$ |
| $\dfrac1t$, $t\ne0$ | $\ln|t|+K$ |
| $e^{at}$, constant $a\ne0$ | $\dfrac1a e^{at}+K$ |
| $\sin(\omega t)$, $\omega\ne0$ | $-\dfrac1\omega\cos(\omega t)+K$ |
| $\cos(\omega t)$, $\omega\ne0$ | $\dfrac1\omega\sin(\omega t)+K$ |

Integrate sums term by term and keep constant multipliers. For example, $\int(6t-2)\,dt=3t^2-2t+K$; check it by differentiating.

**Problem: Try it 8 · Undo an exponential derivative** (introductory)

Find $\int e^{-3t}\,dt$, then differentiate your answer to check it.

<details><summary>Solution</summary>

1. ```steps
$$ \int e^{-3t}\,dt=\hl{-\dfrac13e^{-3t}+K} $$
Divide by the exponent coefficient −3.
$$ \dfrac{d}{dt}\left(-\dfrac13e^{-3t}+K\right)=\hl{e^{-3t}} $$
The chain-rule factor −3 cancels −1/3.
```

**Answer:** $-\dfrac13e^{-3t}+K$.

</details>

### Definite integrals (Week 2)

A **definite integral** has a start and an end. It gives net accumulation (signed area), rather than a family of functions.

$$\int_a^b f(t)\,dt=F(b)-F(a)$$

$a$ and $b$ are the integration limits. For example, $\int_0^2 6t\,dt=[3t^2]_0^2=12$; the notation $[F]_a^b$ means $F(b)-F(a)$, and the constant cancels.

### Integration and initial conditions (Week 2)

**Example: Example 8 · Recover a voltage from its rate**

A voltage changes at $\dfrac{dv}{dt}=2+2t$ V/s and starts at $v(0)=1\,\mathrm V$. Find $v(t)$.

1. ```steps
$$ v(t)=\hl{\int(2+2t)\,dt} $$
Undo the derivative by integrating.
$$ v(t)=\hl{2t+t^2+K} $$
Use the power rule; keep the constant.
$$ v(0)=0+0+K=1\ \Rightarrow\ \hl{K=1} $$
Use the starting value to determine the constant.
$$ v(t)=\hl{1+2t+t^2} $$
Put the constant back into the function.
```

**Answer:** $v(t)=1+2t+t^2\,\mathrm V$. Equivalently, $v(t)-v(0)=\int_0^t(2+2s)\,ds$; $s$ is just a placeholder variable.

### Substitution (Week 3)

**Substitution** reverses the chain rule. Replace a complicated inside expression by $u$, and replace its derivative times $dt$ by $du$.

**Example: Example 9 · A fraction that becomes a logarithm**

Find $\int\dfrac{2t}{1+t^2}\,dt$.

1. ```steps
$$ \int\dfrac{2t}{1+t^2}\,dt $$
The numerator is the derivative of the denominator.
$$ u=\hl{1+t^2},\qquad du=\hl{2t\,dt} $$
Choose the denominator as the new variable.
$$ \int\dfrac{\hl{du}}{\hl{u}}=\ln|u|+K $$
Replace both the denominator and the differential.
$$ \hl{\ln(1+t^2)+K} $$
Substitute back; 1 + t² is positive, so absolute-value bars are unnecessary.
```

**Answer:** $\ln(1+t^2)+K$.

**Problem: Try it 9 · The numerator is almost the derivative** (intermediate)

Find $\int\dfrac{t}{t^2+4}\,dt$.

<details><summary>Solution</summary>

1. ```steps
$$ u=t^2+4,\qquad du=2t\,dt $$
Choose the denominator as u.
$$ \int\dfrac{t}{t^2+4}\,dt=\hl{\dfrac12}\int\dfrac{du}{u} $$
Only t dt is present, so use du/2.
$$ \hl{\dfrac12\ln(t^2+4)+K} $$
Integrate and substitute back.
```

**Answer:** $\dfrac12\ln(t^2+4)+K$.

</details>

### Integration by parts (Week 3)

**Integration by parts** reverses the product rule. Use it for products such as $te^{2t}$, where differentiating the polynomial makes the remaining integral easier.

$$\int u\,dv=uv-\int v\,du$$

Choose $u$ to differentiate and $dv$ to integrate. Here $u$ and $v$ are temporary names, unrelated to a circuit voltage.

**Example: Example 10 · A polynomial times an exponential**

Find $\int te^{2t}\,dt$.

1. ```steps
$$ u=t,\quad du=dt $$
Differentiate the polynomial.
$$ dv=e^{2t}dt,\quad v=\hl{\dfrac12e^{2t}} $$
Integrate the exponential.
$$ \int te^{2t}dt=\hl{\dfrac t2e^{2t}-\dfrac12\int e^{2t}dt} $$
Put the choices into the integration-by-parts formula.
$$ \hl{\dfrac t2e^{2t}-\dfrac14e^{2t}+K} $$
Integrate the remaining exponential.
```

**Answer:** $\dfrac t2e^{2t}-\dfrac14e^{2t}+K$.

**Problem: Try it 10 · By parts with a negative exponent** (intermediate)

Find $\int te^{-t}\,dt$.

<details><summary>Solution</summary>

1. ```steps
$$ u=t,\quad dv=e^{-t}dt,\quad v=\hl{-e^{-t}} $$
Choose the polynomial to differentiate.
$$ \int te^{-t}dt=\hl{-te^{-t}+\int e^{-t}dt} $$
The minus in the formula cancels the minus in v.
$$ \hl{-(t+1)e^{-t}+K} $$
Integrate once more and factor.
```

**Answer:** $-(t+1)e^{-t}+K$.

</details>

## First-order differential equations (Week 2 & Week 3)

### Classification and initial conditions (Week 2)

A **differential equation** gives a relationship between a function and its derivatives. Solving it means finding the function, such as $i(t)$, rather than finding one number.

For an inductor, $v_L=L\dfrac{di}{dt}$: its voltage is proportional to how fast its current changes. A resistor has $v_R=Ri$; when their voltages add to zero, $L\dfrac{di}{dt}+Ri=0$.

Dividing by $L$ gives $\dfrac{di}{dt}=-\dfrac RL i$. With $R,L>0$, positive current has a negative slope: it decays, and the slope becomes gentler as the current falls.

| Label | How to recognize it |
|---|---|
| Ordinary (ODE) | Derivatives with respect to one independent variable, here t. |
| First / second order | Highest derivative is $y^{\prime}$ / $y^{\prime\prime}$; powers do not set the order. |
| Linear | $y$, $y^{\prime}$, etc. appear to the first power, not multiplied together; coefficients may depend on $t$. |
| Homogeneous (linear ODE) | After moving all y terms left, the right side is zero. |
| Constant coefficients | The coefficients multiplying y and its derivatives are constants. |
| Autonomous | The equation has no explicit t outside the unknown function and its derivatives. |

A **general solution** contains free constants. An **initial value problem** (IVP) adds a starting value, such as $i(0)=4$, to select a particular solution.

**Example: Example 11 · Check a proposed solution**

Does $i(t)=4e^{-2t}$ satisfy $i^{\prime}+2i=0$ and $i(0)=4$?

1. ```steps
$$ i^{\prime}=\hl{-8e^{-2t}} $$
Differentiate the proposed current.
$$ i^{\prime}+2i=-8e^{-2t}+8e^{-2t}=\hl{0} $$
Substitute; it must work for every t, not just t = 0.
$$ i(0)=4e^0=\hl{4} $$
Check the initial condition separately.
```

**Answer:** Yes. The ODE is first-order, linear, homogeneous, constant-coefficient and autonomous.

### Separation of variables (Week 3)

To **solve** a separable equation, gather the $y$ terms with $dy$ and the $t$ terms with $dt$, then integrate each side. This is the separation-of-variables rule; use one integration constant after combining the two sides.

**Example: Example 12 · Derive the Week 1 decay**

Solve $\dfrac{di}{dt}=-2i$ with $i(0)=4$.

1. ```steps
$$ \dfrac{di}{dt}=-2i $$
Start with the rate equation.
$$ \hl{\dfrac1i\,di}=\hl{-2\,dt} $$
Separate on an interval where i is nonzero.
$$ \hl{\int\dfrac1i\,di}=\hl{\int-2\,dt} $$
Integrate both sides.
$$ \hl{\ln|i|=-2t+K} $$
Use the logarithm integral.
$$ i=\hl{Ae^{-2t}} $$
Exponentiate; A absorbs e to the constant and the sign.
$$ i(0)=A=4\ \Rightarrow\ i=\hl{4e^{-2t}} $$
Use the initial condition.
```

**Answer:** $i(t)=4e^{-2t}$. The general family $Ae^{-2t}$ also includes $i=0$ by allowing $A=0$; division by $i$ temporarily excluded it.

In the RL model, $2$ is replaced by $R/L=1/\tau$. Thus $i(t)=I_0e^{-t/\tau}$ with $\tau=L/R$; $I_0=i(0)$ and $\tau$ (tau) is the time constant.

**Problem: Try it 11 · Solve a decay and keep every solution** (intermediate)

Solve $y^{\prime}=-3y$ with $y(0)=6$. Also state the general solution and identify the solution excluded when dividing by $y$.

<details><summary>Solution</summary>

1. ```steps
$$ \dfrac{dy}{y}=-3\,dt $$
Separate for y nonzero.
$$ \ln|y|=\hl{-3t+K} $$
Integrate both sides.
$$ y=\hl{Ae^{-3t}} $$
Absorb the sign and exponential constant into A.
$$ y(0)=A=6\ \Rightarrow\ y=\hl{6e^{-3t}} $$
Use the initial condition.
```

**Answer:** IVP: $y=6e^{-3t}$. General solution: $y=Ae^{-3t}$, including the temporarily excluded solution $y=0$ when $A=0$.

</details>

**Problem: Try it 12 · Separate when the final value is nonzero** (intermediate)

Solve $y^{\prime}=6-2y$ with $y(0)=1$. Hint: $6-2y=-2(y-3)$, and $y=3$ is a constant solution.

<details><summary>Solution</summary>

1. ```steps
$$ \dfrac{dy}{y-3}=\hl{-2\,dt} $$
Separate for y different from 3.
$$ \ln|y-3|=\hl{-2t+K} $$
Integrate using the logarithm rule.
$$ y-3=\hl{Ae^{-2t}} $$
Exponentiate and absorb the sign into A.
$$ 1-3=A\ \Rightarrow\ y=\hl{3-2e^{-2t}} $$
The initial condition gives A = −2.
```

**Answer:** $y=3-2e^{-2t}$. It starts at 1 and approaches 3; the general family also includes $y=3$ when $A=0$.

</details>

### RC and RL responses (Week 2)

This is the Week 2 pattern: $x(t)=x_f+(x_0-x_f)e^{-t/\tau}$ for a stable first-order circuit with a constant source. The gap from the final value shrinks exponentially.

| Quantity x | Starts continuously at the switch | Time constant |
|---|---|---|
| Inductor current | $i_L(0^+)=i_L(0^-)$ | $\tau=L/R$ |
| Capacitor voltage | $v_C(0^+)=v_C(0^-)$ | $\tau=RC$ |

$0^-$ and $0^+$ mean just before and just after switching; these continuity rules assume ordinary switching without impulses. Use the resistance seen by the component after switching; at DC steady state a capacitor acts open and an inductor acts like a wire.

### Linear ODEs and integrating factors (Week 3)

Separation does not always work. A first-order **linear** equation has the form below, with $a(t)$ and $f(t)$ known functions.

$$y^{\prime}+a(t)y=f(t)$$

The **integrating factor** $\mu(t)$ (mu) is chosen so multiplying the equation makes the left side one product derivative. This uses the product rule you already know.

$$\mu(t)=e^{\int a(t)\,dt}$$

$$\dfrac{d}{dt}[\mu(t)y(t)]=\mu(t)f(t)$$

Then integrate both sides, divide by $\mu$, and use the initial condition. Choose any convenient antiderivative in $\mu$; its extra constant multiplier is unnecessary.

**Example: Example 13 · A changing input: combine the earlier rules**

Solve $y^{\prime}+2y=4t$, $y(0)=1$.

1. ```steps
$$ \mu=e^{\int2\,dt}=\hl{e^{2t}} $$
The coefficient of y is 2.
$$ e^{2t}y^{\prime}+2e^{2t}y=4te^{2t} $$
Multiply the entire equation by the integrating factor.
$$ \hl{\dfrac{d}{dt}(e^{2t}y)}=4te^{2t} $$
The left side is the product rule in reverse.
$$ e^{2t}y=\hl{2te^{2t}-e^{2t}+K} $$
Integrate; the right side uses the by-parts example multiplied by 4.
$$ y=\hl{2t-1+Ke^{-2t}} $$
Divide every term by e to the 2t.
$$ 1=-1+K\ \Rightarrow\ \hl{K=2} $$
Use y(0) = 1.
$$ y=\hl{2t-1+2e^{-2t}} $$
Substitute the constant.
```

**Answer:** $y=2t-1+2e^{-2t}$.

**Problem: Try it 13 · A constant input builds up** (intermediate)

Solve $y^{\prime}+2y=8$, $y(0)=0$, using an integrating factor.

<details><summary>Solution</summary>

1. ```steps
$$ \mu=e^{2t} $$
Integrate the coefficient of y, then exponentiate.
$$ \dfrac{d}{dt}(e^{2t}y)=\hl{8e^{2t}} $$
Multiply and recognize the product derivative.
$$ e^{2t}y=\hl{4e^{2t}+K} $$
Integrate both sides.
$$ y=4+Ke^{-2t},\quad 0=4+K $$
Divide, then apply the starting value.
$$ y=\hl{4(1-e^{-2t})} $$
K = −4; the response approaches 4.
```

**Answer:** $y=4(1-e^{-2t})$.

</details>

**Problem: Try it 14 · A coefficient that depends on time** (intermediate)

For $t>0$, solve $ty^{\prime}+2y=4t^2$, $y(1)=2$.

<details><summary>Solution</summary>

1. ```steps
$$ y^{\prime}+\hl{\dfrac2t}y=4t $$
Divide by t so the coefficient of the derivative is 1.
$$ \mu=e^{\int(2/t)dt}=e^{2\ln t}=\hl{t^2} $$
On t > 0, ln t is defined and exponentiation simplifies.
$$ \dfrac{d}{dt}(t^2y)=\hl{4t^3} $$
Multiply through and use the product rule in reverse.
$$ t^2y=\hl{t^4+K} $$
Integrate.
$$ y=t^2+\dfrac K{t^2},\quad 2=1+K $$
Divide by t² and apply the condition at t = 1.
$$ y=\hl{t^2+\dfrac1{t^2}} $$
The initial condition gives K = 1.
```

**Answer:** $y=t^2+t^{-2}$ for $t>0$.

</details>

### Existence and uniqueness (Week 3)

For existence and uniqueness, **continuous** means the function has no break at the point in question. Start with domain checks: denominators cannot be zero, and real logarithms need positive arguments.

For $y^{\prime}=F(t,y)$, if $F$ and $\partial F/\partial y$ are continuous in a region around the starting point, there is exactly one solution locally. If this test fails, it makes no promise; failure does not itself prove there are several solutions.

**Problem: Try it 15 · Where is the uniqueness test safe?** (introductory)

For $y^{\prime}=\dfrac{y}{t-2}$, find $\partial F/\partial y$. Does the test apply at $(t,y)=(0,1)$? At $(2,1)$?

<details><summary>Solution</summary>

1. ```steps
$$ F(t,y)=\dfrac{y}{t-2} $$
Treat t as fixed when taking the y partial derivative.
$$ \dfrac{\partial F}{\partial y}=\hl{\dfrac1{t-2}} $$
The derivative of y is 1.
$$ \hl{t\ne2} $$
Both functions are continuous away from t = 2.
```

**Answer:** At $(0,1)$: yes, a unique local solution is guaranteed. At $(2,1)$: the ODE itself is undefined, so this is not a valid starting point.

</details>

## Exact differential equations

### Exactness test and solutions (Week 4)

Week 4 writes some equations as $M(t,y)\,dt+N(t,y)\,dy=0$. The goal is to find a function $U$ with $U_t=M$ and $U_y=N$.

Along a solution curve, the chain rule says $\dfrac{dU}{dt}=U_t+U_y y^{\prime}=0$, so $U$ stays constant. That gives the implicit answer $U(t,y)=K$.

$$\dfrac{\partial M}{\partial y}=\dfrac{\partial N}{\partial t}$$

This is the **exactness test**: on a small region where the first partial derivatives are continuous, matching these mixed slopes lets us rebuild $U$. The examples here use such regions.

**Example: Example 14 · The integration constant becomes a function**

Solve $2ty\,dt+(t^2+6y)\,dy=0$.

1. ```steps
$$ M=2ty,\quad N=t^2+6y $$
Read off the coefficients of dt and dy.
$$ M_y=\hl{2t}=N_t $$
The exactness test passes.
$$ U=\int2ty\,dt=\hl{t^2y+g(y)} $$
Integrate in t, holding y fixed; any function of y vanishes under a t partial derivative.
$$ U_y=t^2+g^{\prime}(y)=\hl{t^2+6y} $$
Differentiate in y and match the given N.
$$ g^{\prime}(y)=6y\ \Rightarrow\ g(y)=\hl{3y^2} $$
Integrate the missing y part; its constant is absorbed into K.
$$ \hl{t^2y+3y^2=K} $$
The reconstructed function stays constant along solutions.
```

**Answer:** $t^2y+3y^2=K$.

**Problem: Try it 16 · Rebuild U, then use a starting point** (intermediate)

Solve $(ty^2+3t^2)\,dt+t^2y\,dy=0$ with $y(1)=2$. You may leave the answer implicit.

<details><summary>Solution</summary>

1. ```steps
$$ M_y=\hl{2ty}=N_t $$
Check exactness first.
$$ U=\hl{\dfrac12t^2y^2+t^3+g(y)} $$
Integrate M with respect to t, holding y fixed.
$$ U_y=t^2y+g^{\prime}(y)=t^2y $$
Match the result to N.
$$ g^{\prime}(y)=\hl{0} $$
The missing function is constant, absorbed into K.
$$ K=\dfrac12(1)^2(2)^2+1^3=\hl{3} $$
Use the initial point.
$$ \hl{\dfrac12t^2y^2+t^3=3} $$
Leave the answer as a relation between t and y.
```

**Answer:** $\dfrac12t^2y^2+t^3=3$.

</details>

### Integrating factors (Week 4)

If the test fails, an integrating factor sometimes repairs it. For an equation in differential form, these are two useful tests; each must reduce to a function of only the indicated variable.

| If the ratio depends only on… | Use this integrating factor |
|---|---|
| $t$: $\dfrac{M_y-N_t}{N}=h(t)$ | $\mu(t)=e^{\int h(t)\,dt}$ |
| $y$: $\dfrac{N_t-M_y}{M}=h(y)$ | $\mu(y)=e^{\int h(y)\,dy}$ |

These ratios require their denominators to be nonzero on the region used. Multiply **both** $M$ and $N$ by $\mu$, then repeat the exact-equation method.

**Example: Example 15 · Repair an equation using a t factor**

For $t>0$, solve $y\,dt+3t\,dy=0$.

1. ```steps
$$ M_y=1,\quad N_t=3 $$
The equation is not exact yet.
$$ \dfrac{M_y-N_t}{N}=\hl{-\dfrac2{3t}} $$
The ratio depends only on t.
$$ \mu=e^{\int-2/(3t)\,dt}=\hl{t^{-2/3}} $$
Use the logarithm integral; t is positive.
$$ t^{-2/3}y\,dt+3t^{1/3}\,dy=0 $$
Multiply the entire equation by mu.
$$ U=\hl{3t^{1/3}y+g(y)} $$
Integrate the new M in t using the power rule.
$$ U_y=3t^{1/3}+g^{\prime}(y)=3t^{1/3} $$
Match the new N; g is constant.
$$ \hl{t^{1/3}y=K} $$
Set U constant and absorb the factor of 3 into K.
```

**Answer:** $t^{1/3}y=K$, or $y=Kt^{-1/3}$, for $t>0$.

**Problem: Try it 17 · Repair with a y factor** (intermediate)

On a region where $y>0$, solve $y\,dt-t\,dy=0$ using the y-only test above.

<details><summary>Solution</summary>

1. ```steps
$$ M=y,\quad N=-t,\quad M_y=1,\quad N_t=-1 $$
Read the coefficients and differentiate.
$$ \dfrac{N_t-M_y}{M}=\hl{-\dfrac2y} $$
The ratio depends only on y.
$$ \mu=e^{\int-2/y\,dy}=\hl{y^{-2}} $$
Integrate and exponentiate on y > 0.
$$ \dfrac1y\,dt-\dfrac t{y^2}\,dy=0 $$
Multiply the original equation by mu.
$$ U=\hl{\dfrac ty}+g(y) $$
Integrate the new M in t.
$$ U_y=-\dfrac t{y^2}+g^{\prime}(y)=-\dfrac t{y^2} $$
Match N, so g is constant.
$$ \hl{\dfrac ty=K} $$
Set the reconstructed function constant.
```

**Answer:** $t/y=K$ on the chosen region; a graph $y(t)$ there must have $K\ne0$.

</details>

## Second-order differential equations (Week 5)

### Characteristic equation

For $ay^{\prime\prime}+by^{\prime}+cy=0$, $a,b,c$ are constants and $a\ne0$. Trying $y=e^{st}$ works because differentiating just multiplies by $s$.

```steps
title "Replace the derivatives by a quadratic"
$$ y=e^{st} $$
Try an exponential with an unknown constant s.
$$ y^{\prime}=\hl{se^{st}},\quad y^{\prime\prime}=\hl{s^2e^{st}} $$
Differentiate once and twice using the chain rule.
$$ \hl{(as^2+bs+c)}e^{st}=0 $$
Substitute into the differential equation.
$$ \hl{as^2+bs+c=0} $$
The exponential is never zero, so its multiplier must be zero.
```

This is the **characteristic equation**. Find its roots by factoring or using $s=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$.

### Real roots

| Roots | General solution |
|---|---|
| Two different real roots $s_1,s_2$ | $y=K_1e^{s_1t}+K_2e^{s_2t}$ |
| One repeated real root $s$ | $y=(K_1+K_2t)e^{st}$ |

A second-order IVP gives both $y(0)$ and $y^{\prime}(0)$. Put them into the solution and its derivative to find the two constants.

**Example: Example 16 · Two different real roots**

Solve $y^{\prime\prime}+3y^{\prime}+2y=0$, $y(0)=1$, $y^{\prime}(0)=0$.

1. ```steps
$$ s^2+3s+2=(s+1)(s+2)=0 $$
Factor the characteristic equation.
$$ s=\hl{-1,-2} $$
Each factor gives one root.
$$ y=\hl{K_1e^{-t}+K_2e^{-2t}} $$
Use one exponential for each distinct root.
$$ y(0)=\hl{K_1+K_2=1} $$
At zero both exponentials equal 1.
$$ y^{\prime}(0)=\hl{-K_1-2K_2=0} $$
Differentiate, then apply the starting slope.
$$ K_2=\hl{-1},\quad K_1=\hl{2} $$
Solve the two simultaneous equations.
$$ y=\hl{2e^{-t}-e^{-2t}} $$
Substitute the constants.
```

**Answer:** $y=2e^{-t}-e^{-2t}$.

**Example: Example 17 · A repeated root needs the extra t**

Solve $y^{\prime\prime}+4y^{\prime}+4y=0$, $y(0)=1$, $y^{\prime}(0)=0$.

1. ```steps
$$ s^2+4s+4=\hl{(s+2)^2}=0 $$
There is one root −2, repeated twice.
$$ y=\hl{(K_1+K_2t)e^{-2t}} $$
Two copies of the same exponential would combine into only one constant.
$$ y(0)=K_1=\hl{1} $$
Use the starting value.
$$ y^{\prime}=\hl{[K_2-2(K_1+K_2t)]e^{-2t}} $$
Use the product rule.
$$ y^{\prime}(0)=K_2-2K_1=0\ \Rightarrow\ \hl{K_2=2} $$
Use the starting slope.
$$ y=\hl{(1+2t)e^{-2t}} $$
Substitute the constants.
```

**Answer:** $y=(1+2t)e^{-2t}$.

**Problem: Try it 18 · Fit the two constants** (intermediate)

Solve $y^{\prime\prime}+4y^{\prime}+3y=0$, $y(0)=0$, $y^{\prime}(0)=2$.

<details><summary>Solution</summary>

1. ```steps
$$ s^2+4s+3=\hl{(s+1)(s+3)}=0 $$
The roots are −1 and −3.
$$ y=K_1e^{-t}+K_2e^{-3t} $$
Write the two-exponential solution.
$$ K_1+K_2=0,\quad -K_1-3K_2=2 $$
Use the starting value and derivative.
$$ K_1=\hl{1},\quad K_2=\hl{-1} $$
Solve the two equations.
$$ y=\hl{e^{-t}-e^{-3t}} $$
Substitute the constants.
```

**Answer:** $y=e^{-t}-e^{-3t}$.

</details>

**Problem: Try it 19 · A repeated root with a starting slope** (intermediate)

Solve $y^{\prime\prime}+2y^{\prime}+y=0$, $y(0)=0$, $y^{\prime}(0)=3$.

<details><summary>Solution</summary>

1. ```steps
$$ (s+1)^2=0\ \Rightarrow\ y=(K_1+K_2t)e^{-t} $$
The root −1 is repeated.
$$ y(0)=K_1=\hl{0} $$
The initial value removes the constant term in the bracket.
$$ y^{\prime}(0)=K_2-K_1=3\ \Rightarrow\ \hl{K_2=3} $$
Differentiate by the product rule and set t = 0.
$$ y=\hl{3te^{-t}} $$
Substitute both constants.
```

**Answer:** $y=3te^{-t}$.

</details>

### Wronskian

The **Wronskian** checks whether two proposed solutions provide independent choices. For $y_1,y_2$, compute $W=y_1y_2^{\prime}-y_1^{\prime}y_2$; a nonzero value at the initial time lets you fit any starting value and slope.

For $e^{-2t}$ and $te^{-2t}$, $W=e^{-4t}\ne0$. Two multiples such as $e^{-2t}$ and $3e^{-2t}$ give $W=0$: they provide the same shape.

### Existence and uniqueness

For $y^{\prime\prime}+p(t)y^{\prime}+q(t)y=g(t)$, continuity of $p,q,g$ on an interval containing the starting time guarantees one solution on that interval for any starting value and slope. Divide by the original leading coefficient before checking continuity.

### Complex roots

The remaining case is a negative discriminant. Use $j^2=-1$, so $\sqrt{-16}=4j$ and, for example, $s^2+2s+5=0$ gives $s=-1\pm2j$.

These are **complex conjugates**: the same real part, with opposite imaginary parts. Euler’s formula connects complex exponentials to real oscillations; $\theta$ is an angle in radians.

$$e^{j\theta}=\cos\theta+j\sin\theta$$

```steps
title "Turn a complex exponential into real oscillations"
$$ e^{(-1+2j)t} $$
Start with one of the characteristic roots.
$$ \hl{e^{-t}e^{j2t}} $$
Split the exponential using the exponent sum rule.
$$ e^{-t}\hl{(\cos2t+j\sin2t)} $$
Use Euler’s formula.
$$ \hl{e^{-t}\cos2t},\quad\hl{e^{-t}\sin2t} $$
With real coefficients, the real and imaginary parts each solve the ODE.
```

For roots $s=\sigma\pm j\omega$, with $\omega>0$, the real general solution is:

$$y=e^{\sigma t}(K_1\cos\omega t+K_2\sin\omega t)$$

$\sigma$ (sigma) sets decay or growth; $\omega$ sets the oscillation rate in rad/s. Negative $\sigma$ gives decaying oscillations; zero $\sigma$ gives oscillations with a constant amplitude.

**Example: Example 18 · Complex roots and two initial conditions**

Solve $y^{\prime\prime}+2y^{\prime}+5y=0$, $y(0)=1$, $y^{\prime}(0)=1$.

1. ```steps
$$ s=\dfrac{-2\pm\sqrt{4-20}}2=\hl{-1\pm2j} $$
Apply the quadratic formula.
$$ y=\hl{e^{-t}(K_1\cos2t+K_2\sin2t)} $$
Use sigma = −1 and omega = 2.
$$ y(0)=K_1=\hl{1} $$
At zero, cosine is 1 and sine is 0.
$$ B(t)=K_1\cos2t+K_2\sin2t $$
Call the trig bracket B to keep the product rule readable.
$$ y^{\prime}=\hl{e^{-t}(B^{\prime}-B)} $$
Use the product rule on y = e to the −t times B.
$$ B^{\prime}=\hl{-2K_1\sin2t+2K_2\cos2t} $$
Differentiate the bracket using the chain rule.
$$ y^{\prime}(0)=\hl{-K_1+2K_2}=1 $$
At zero, combine both contributions to the derivative.
$$ K_2=1\ \Rightarrow\ y=\hl{e^{-t}(\cos2t+\sin2t)} $$
With K₁ = 1, the slope condition gives K₂ = 1.
```

**Answer:** $y=e^{-t}(\cos2t+\sin2t)$.

In general, evaluating that product derivative at zero gives $y^{\prime}(0)=\sigma K_1+\omega K_2$. It is a shortcut from the product and chain rules, not a separate rule to memorize.

**Problem: Try it 20 · A decaying oscillation** (intermediate)

Solve $y^{\prime\prime}+4y^{\prime}+13y=0$, $y(0)=0$, $y^{\prime}(0)=3$.

<details><summary>Solution</summary>

1. ```steps
$$ s=\dfrac{-4\pm\sqrt{16-52}}2=\hl{-2\pm3j} $$
Find the characteristic roots.
$$ y=e^{-2t}(K_1\cos3t+K_2\sin3t) $$
Write the real solution.
$$ K_1=\hl{0} $$
Use y(0) = 0.
$$ y^{\prime}(0)=-2K_1+3K_2=3\ \Rightarrow\ \hl{K_2=1} $$
Apply the derivative at zero.
$$ y=\hl{e^{-2t}\sin3t} $$
Substitute the constants.
```

**Answer:** $y=e^{-2t}\sin3t$.

</details>

**Problem: Try it 21 · Oscillation without decay** (intermediate)

Solve $y^{\prime\prime}+4y=0$, $y(0)=1$, $y^{\prime}(0)=0$. What changes when the real part of the roots is zero?

<details><summary>Solution</summary>

1. ```steps
$$ s^2+4=0\ \Rightarrow\ s=\hl{\pm2j} $$
The roots have sigma = 0.
$$ y=\hl{K_1\cos2t+K_2\sin2t} $$
The exponential factor is e⁰ = 1.
$$ K_1=1,\quad 2K_2=0 $$
Use the initial value and initial slope.
$$ y=\hl{\cos2t} $$
There is no shrinking exponential envelope.
```

**Answer:** $y=\cos2t$; its amplitude stays constant.

</details>

## Circuit applications

### Capacitors and inductors (Week 2)

A capacitor obeys $i_C=C\dfrac{dv_C}{dt}$; an inductor obeys $v_L=L\dfrac{di_L}{dt}$. Once a voltage or current function is known, these laws just ask for a derivative.

**Example: Example 19 · Read a response and find the capacitor current**

A capacitor has $C=0.2\,\mathrm F$ and $v_C(t)=12-10e^{-5t}\,\mathrm V$. The current enters its positive-voltage terminal. Find the starting voltage, final voltage, time constant and current.

1. ```steps
$$ v_C(0)=12-10=\hl{2\,\mathrm V} $$
Set t = 0 to read the starting value.
$$ v_C(t)\to\hl{12\,\mathrm V} $$
The exponential approaches zero as time grows.
$$ \dfrac1\tau=5\ \Rightarrow\ \tau=\hl{0.2\,\mathrm s} $$
Match the exponent to −t/τ.
$$ \dfrac{dv_C}{dt}=\hl{50e^{-5t}} $$
Use the chain rule.
$$ i_C=C\dfrac{dv_C}{dt}=0.2(50e^{-5t})=\hl{10e^{-5t}\,\mathrm A} $$
Multiply by the capacitance, using the stated current direction.
```

**Answer:** $V_0=2\,\mathrm V$, $V_f=12\,\mathrm V$, $\tau=0.2\,\mathrm s$, $i_C=10e^{-5t}\,\mathrm A$.

### RLC circuits (Week 5)

In a **series RLC circuit**, a resistor, inductor and capacitor give a second-order equation. With a constant applied voltage $V$, its capacitor voltage satisfies the model below; the course derives it from the circuit laws.

$$LCv_C^{\prime\prime}+RCv_C^{\prime}+v_C=V$$

The final constant solution is $v_C=V$. Put $y=v_C-V$ to describe the remaining deviation; its derivatives are the same as those of $v_C$, so $y$ satisfies a homogeneous equation.

$$y^{\prime\prime}+\dfrac RL y^{\prime}+\dfrac1{LC}y=0$$

| Characteristic roots | Circuit response |
|---|---|
| Two different negative real roots | Overdamped: two decaying exponential terms. |
| One repeated negative real root | Critically damped: an exponential times a linear expression in t. |
| A conjugate pair with negative real part | Underdamped: decaying sine/cosine oscillations. |

For example, $L=0.5\,\mathrm H$, $R=2\,\Omega$, $C=0.25\,\mathrm F$ give $y^{\prime\prime}+4y^{\prime}+8y=0$. Its roots are $-2\pm2j$, so $v_C=V+e^{-2t}(K_1\cos2t+K_2\sin2t)$.

The two starting facts are $v_C(0)=V_0$ and $v_C^{\prime}(0)=I_0/C$, where $I_0$ is the series current entering the capacitor’s positive terminal. They determine $K_1,K_2$ using the same two-condition method above.
