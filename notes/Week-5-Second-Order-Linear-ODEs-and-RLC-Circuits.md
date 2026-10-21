# Week 5: Second-Order Linear ODEs and RLC Circuits

## Calculus refresher: second derivatives and products

A second derivative means differentiate twice: $y''=(y')'$. For $y=e^{st}$ with constant $s$, this gives $y'=se^{st}$ and $y''=s^2e^{st}$.

| Expression | Derivative | Rule |
|---|---|---|
| $te^{st}$ | $e^{st}+ste^{st}$ | Product rule: differentiate each factor in turn. |
| $\cos(\omega t)$ | $-\omega\sin(\omega t)$ | Chain rule: retain the frequency factor. |
| $\sin(\omega t)$ | $\omega\cos(\omega t)$ | The cosine term has a positive sign. |

For an exponential times a bracket, keep the bracket intact while applying the product rule. For example, if $y=e^{-t}(A\cos2t+B\sin2t)$, then:

$$\begin{aligned}y'={}&-e^{-t}(A\cos2t+B\sin2t)\\&+e^{-t}(-2A\sin2t+2B\cos2t)\end{aligned}$$

At $t=0$, use $e^0=1$, $\cos0=1$, and $\sin0=0$. The expressions simplify to $y(0)=A$ and $y^{\prime}(0)=-A+2B$.

**Problem: Try it 1 · Differentiate before applying conditions · original** (introductory)

Find (a) $y^{\prime}$ and $y^{\prime\prime}$ for $y=e^{-3t}$; (b) $y^{\prime}(0)$ for $y=(A+Bt)e^{-2t}$.

<details><summary>Solution</summary>

1. Each derivative of the exponential brings out −3.

   $$y'=-3e^{-3t},\qquad y''=9e^{-3t}$$
2. Use the product rule before setting t to zero.

   $$y'=Be^{-2t}-2(A+Bt)e^{-2t}$$
3. At zero, the t term disappears.

   $$y'(0)=B-2A$$

**Answer:** (a) $-3e^{-3t}$ and $9e^{-3t}$. (b) $B-2A$.

</details>

## Week 5 overview

A second-order equation tracks both a value and its rate of change. First learn to turn a constant-coefficient equation into a quadratic, then build solutions for each type of root. RLC circuits use those same solutions, with starting conditions obtained from stored voltage and current.

Coverage follows the syllabus and Nilsson & Riedel Chapter 8. No Week 5 lecture file is currently uploaded; the mathematical explanations and original exercises below support that coverage.

## Topic 1: Second-order equations, one root case at a time

### Why an exponential turns the ODE into a quadratic

Consider $ay''+by'+cy=0$, where $a,b,c$ are constants and $a\ne0$. It is linear and homogeneous; try $y=e^{st}$, where $s$ is a number to be found.

```steps
title "Find the characteristic equation"
$$ ay''+by'+cy=0 $$
Start with the homogeneous ODE.
$$ y=e^{st},\quad y^{\prime}=se^{st},\quad y^{\prime\prime}=s^2e^{st} $$
Differentiate the trial function.
$$ a\hl{s^2e^{st}}+b\hl{se^{st}}+c\hl{e^{st}}=0 $$
Substitute into the ODE.
$$ \hl{(as^2+bs+c)}e^{st}=0 $$
Factor out the common exponential.
$$ \hl{as^2+bs+c=0} $$
The exponential never vanishes, so the quadratic must be zero.
```

This quadratic is the **characteristic equation**. Factor it when possible, otherwise use $s=(-b\pm\sqrt{b^2-4ac})/(2a)$; the roots decide which form of solution to use.

The two constants in the general solution are fixed by two starting conditions: $y(t_0)$ gives the starting value, and $y^{\prime}(t_0)$ gives the starting slope. Apply these to the solution and its derivative, not to the root equation.

### Case 1: two different real roots

Each root produces an exponential. With roots $s_1\ne s_2$, the general solution is $y=Ae^{s_1t}+Be^{s_2t}$; sums and constant multiples remain solutions because the ODE is linear and homogeneous.

**Example: Example 1 · Two roots, then two constants · original**

Solve $y''+3y'+2y=0$ with $y(0)=1$, $y'(0)=0$.

1. Factor the characteristic equation.

   $$s^2+3s+2=(s+1)(s+2)=0$$
2. Use roots −1 and −2, then differentiate the general solution.

   $$y=Ae^{-t}+Be^{-2t}$$
3. Apply the value and slope at zero.

   $$A+B=1,\qquad -A-2B=0$$
4. Add the equations to eliminate A, then substitute back.

   $$B=-1,\qquad A=2$$

**Answer:** $y=2e^{-t}-e^{-2t}$. Its derivative is $-2e^{-t}+2e^{-2t}$, so both starting conditions check.

**Problem: Try it 2 · Fit the constants yourself · original** (introductory)

Solve $y''+5y'+6y=0$, $y(0)=2$, $y'(0)=-5$.

<details><summary>Solution</summary>

1. Factor the quadratic.

   $$(s+2)(s+3)=0$$
2. Write the solution and apply both starting conditions.

   $$y=Ae^{-2t}+Be^{-3t}$$
3. Solve the two simultaneous equations.

   $$A+B=2,\quad -2A-3B=-5\quad\Rightarrow\quad A=B=1$$

**Answer:** $y=e^{-2t}+e^{-3t}$.

</details>

### Case 2: one repeated real root

If the quadratic has the same root $s$ twice, $Ae^{st}+Be^{st}=(A+B)e^{st}$ only supplies one adjustable constant. A second independent solution is $te^{st}$, giving:

$$y=(A+Bt)e^{st}$$

The factor $t$ makes a different function, not a different constant. You can verify $te^{st}$ by differentiating twice and substituting into the ODE with the repeated root.

**Problem: Try it 3 · Use the extra t · original** (introductory)

Solve $4y''+4y'+y=0$, $y(0)=4$, $y'(0)=0$.

Start with $(2s+1)^2=0$, so $s=-1/2$. Write the form, then use the product rule to apply the slope condition.

<details><summary>Solution</summary>

1. Use the repeated-root form.

   $$y=(A+Bt)e^{-t/2}$$
2. The starting value gives A = 4.

   $$y(0)=A=4$$
3. The product rule gives the slope at zero.

   $$y'(0)=B-\dfrac A2=0$$
4. So B = 2.

   $$y=(4+2t)e^{-t/2}$$

**Answer:** $y=(4+2t)e^{-t/2}$.

</details>

### Case 3: a complex-conjugate pair

Remember $j^2=-1$. Roots $s=\sigma\pm j\omega$ contain a real part $\sigma$ and imaginary parts $\pm\omega$; Euler’s relation $e^{j\omega t}=\cos\omega t+j\sin\omega t$ converts the exponentials into real functions.

$$y=e^{\sigma t}(A\cos\omega t+B\sin\omega t)$$

- $e^{\sigma t}$ controls the envelope: decay if $\sigma<0$, growth if $\sigma>0$.
- $\omega>0$ is the oscillation frequency in radians per unit time.
- If $\sigma=0$, the envelope is constant rather than decaying.

**Example: Example 2 · Complex roots without complex-valued answers · original**

Solve $y''+2y'+5y=0$, $y(0)=1$, $y'(0)=1$.

1. Use the quadratic formula; √(−16) = j4.

   $$s=\dfrac{-2\pm\sqrt{4-20}}2=-1\pm j2$$
2. Use σ = −1 and ω = 2 in the real solution form.

   $$y=e^{-t}(A\cos2t+B\sin2t)$$
3. At zero, the value is A.

   $$A=1$$
4. Use the derivative from the refresher.

   $$y'(0)=-A+2B=1\quad\Rightarrow\quad B=1$$

**Answer:** $y=e^{-t}(\cos2t+\sin2t)$.

**Problem: Try it 4 · Read a different complex root pair · original** (introductory)

The roots are $-3\pm j4$. Write the general solution, then select $y(0)=0$, $y'(0)=8$. Do not expand the derivative more than necessary.

<details><summary>Solution</summary>

1. The real part is −3 and the frequency is 4.

   $$y=e^{-3t}(A\cos4t+B\sin4t)$$
2. The starting value is zero, so A = 0.

   $$A=0$$
3. At zero, the product rule gives −3A + 4B = 8.

   $$B=2$$

**Answer:** $y=2e^{-3t}\sin4t$.

</details>

### Now compare the cases

| Quadratic discriminant | Roots | General solution |
|---|---|---|
| $b^2-4ac>0$ | Distinct real | $Ae^{s_1t}+Be^{s_2t}$ |
| $b^2-4ac=0$ | Repeated real | $(A+Bt)e^{st}$ |
| $b^2-4ac<0$ | $\sigma\pm j\omega$ | $e^{\sigma t}(A\cos\omega t+B\sin\omega t)$ |

**Problem: Try it 5 · Choose a form before calculating constants · original** (introductory)

For $y''+2y'+ky=0$, find which values of $k$ give each root case. At $k=0$, write the general solution and decide whether every solution tends to zero.

<details><summary>Solution</summary>

1. The discriminant is 4 − 4k.

   $$\begin{gathered}k<1:\text{ distinct real}\\k=1:\text{ repeated}\\k>1:\text{ complex}\end{gathered}$$
2. At k = 0, factor s(s + 2) = 0. The zero root gives e⁰ᵗ = 1.

   $$y=A+Be^{-2t}$$
3. The exponential decays but the constant remains.

   $$y(t)\to A$$

**Answer:** $k<1$, $k=1$, $k>1$ give the three cases respectively. At $k=0$, $y=A+Be^{-2t}$ need not decay to zero.

</details>

```graph
title "Compare the three root cases with the same starting values"
x 0 8 label="$t$"
y -0.5 1.2 label="$y$"
curve "2*exp(-t)-exp(-2*t)" label="distinct real roots" color=1
curve "(1+t)*exp(-t)" label="repeated root" color=2
curve "exp(-t)*(cos(2*t)+0.5*sin(2*t))" label="complex pair" color=3
caption "All three start at y=1 with slope zero. Their equations differ. The complex-root response oscillates; the other two shown approach zero without oscillating."
```

## Topic 2: Why two conditions select one solution

### Check the interval where the theorem applies

First divide by the coefficient of $y''$ to write $y''+p(t)y'+q(t)y=g(t)$. If $p,q,g$ are continuous on an open interval containing $t_0$, then specifying $y(t_0)$ and $y'(t_0)$ gives exactly one solution throughout that interval.

For constant coefficients the theorem applies on the whole real line. With variable coefficients, locate the points where the normalised expressions fail, then choose the interval containing the starting time.

**Problem: Try it 6 · Find the interval; do not solve · original** (introductory)

For $(t-1)y''+y'+y=\ln t$, find the largest interval guaranteed by the theorem for (a) $t_0=2$ and (b) $t_0=1/2$.

<details><summary>Solution</summary>

1. Divide by t − 1 and inspect all three expressions.

   $$p=q=\dfrac1{t-1},\qquad g=\dfrac{\ln t}{t-1}$$
2. The log excludes t ≤ 0, and the denominator excludes t = 1.
3. Choose the connected interval containing each starting time.

   $$\text{(a) }(1,\infty),\qquad\text{(b) }(0,1)$$

**Answer:** (a) $(1,\infty)$. (b) $(0,1)$.

</details>

### Two functions must supply two independent choices

Suppose $y_1,y_2$ are solutions of the same homogeneous linear ODE. Fitting $Ay_1+By_2$ to a value and slope gives two simultaneous equations; their determinant is the **Wronskian**:

$$W(t)=y_1y_2^{\prime}-y_1^{\prime} y_2$$

If $W(t_0)\ne0$, the constants can be uniquely fitted at that point. Two scalar multiples of the same function have $W=0$, so they do not supply two independent choices.

**Problem: Try it 7 · Why the repeated-root form works · original** (introductory)

For $y''+4y'+4y=0$, compare the pairs (a) $e^{-2t},3e^{-2t}$ and (b) $e^{-2t},te^{-2t}$. Compute their Wronskians and decide which pair can form a general solution.

<details><summary>Solution</summary>

1. For (a), differentiate both functions and substitute.

   $$W=e^{-2t}(-6e^{-2t})-(-2e^{-2t})(3e^{-2t})=0$$
2. For (b), the derivative of te⁻²ᵗ is (1 − 2t)e⁻²ᵗ.

   $$W=e^{-2t}(1-2t)e^{-2t}+2te^{-4t}=e^{-4t}$$
3. The second Wronskian never vanishes, so its two constants remain independent.

**Answer:** (a) $W=0$: not a fundamental pair. (b) $W=e^{-4t}\ne0$: the form is $(A+Bt)e^{-2t}$.

</details>

A useful application of uniqueness: if a regular homogeneous linear ODE has $y(t_0)=0$ and $y'(t_0)=0$, then $y=0$ is the unique solution. It already satisfies the equation and both conditions.

## Topic 3: RLC circuits — translate the circuit into the same math

### A series circuit gives value and slope from stored energy

Use capacitor voltage $v_C$ as the unknown in a series RLC circuit. The loop current enters its positive terminal, so $i=Cv_C^{\prime}$; capacitor voltage and inductor current carry over through an ordinary switch or source step.

- **Starting value:** $v_C(0^+)=V_0$, the stored capacitor voltage.
- **Starting slope:** $v_C^{\prime}(0^+)=I_0/C$, where $I_0$ is the series inductor current in the shown direction.
- **Post-step source:** a constant $V_s$ supplies the forcing term in the ODE.

```schematic
V1 0,3 -> 0,0 "$V_s$"
R1 0,3 -> 3,3 "$4\,\Omega$" i="$i$"
L1 3,3 -> 6,3 "$40\,\mathrm{mH}$"
C1 6,3 -> 6,0 "$10\,\mathrm{mF}$" v="$v_C$"
wire 6,0 -> 0,0
ground 0,0
#~ flow
#~ value V1 100
#~ init C1 200
#~ init L1 0
#@ view "Before the source changes"
#@ node a 200 "$V_s$: $200\,\mathrm{V}$"
#@ node b 200 "R end: $200\,\mathrm{V}$"
#@ node c 200 "$C$: $200\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$200\,\mathrm{V}$" col=0
#@ el R a b "$4\,\Omega$" col=1
#@ el L b c "$40\,\mathrm{mH}$" col=2
#@ el C c g "$10\,\mathrm{mF}$" col=3 plus=c v="$v_C$"
#@ note "Ground the bottom wire. In DC steady state i = 0, so R and L have no step. The capacitor holds the source voltage, 200 V."
#@ view "Just after the source changes"
#@ node a 100 "$V_s$: $100\,\mathrm{V}$"
#@ node b 100 "R end: $100\,\mathrm{V}$"
#@ node c 200 "$C$: $200\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$100\,\mathrm{V}$" col=0 id=src
#@ el R a b "$4\,\Omega$" col=1 id=res
#@ el L b c "$40\,\mathrm{mH}$" col=2 id=ind
#@ el C c g "$10\,\mathrm{mF}$" col=3 plus=c v="$v_C$" id=cap
#@ step "Ground the bottom wire." show=g
#@ step "The new source fixes its top at 100 V." show=a,src
#@ step "Inductor current stays zero, so R has no fall." show=b,res
#@ step "Capacitor voltage stays 200 V; the inductor voltage from left to right is −100 V." show=c,cap,ind
#@ view "At 20 ms"
#@ node a 100 "$V_s$: $100\,\mathrm{V}$"
#@ node b 173.575888 "R end: $173.58\,\mathrm{V}$"
#@ node c 173.575888 "$C$: $173.58\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$100\,\mathrm{V}$" col=0 i="$18.39\,\mathrm{A}$" to=g
#@ el R a b "$4\,\Omega$" col=1 i="$18.39\,\mathrm{A}$" to=a
#@ el L b c "$40\,\mathrm{mH}$" col=2 i="$18.39\,\mathrm{A}$" to=b
#@ el C c g "$10\,\mathrm{mF}$" col=3 plus=c v="$v_C$" i="$18.39\,\mathrm{A}$" to=c
#@ note "Ground the bottom wire. At 20 ms, i = −50/e A in the clockwise reference; actual current runs back toward the source. The capacitor releases energy."
#@ view "Final DC state"
#@ node a 100 "$V_s$: $100\,\mathrm{V}$"
#@ node b 100 "R end: $100\,\mathrm{V}$"
#@ node c 100 "$C$: $100\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$100\,\mathrm{V}$" col=0
#@ el R a b "$4\,\Omega$" col=1
#@ el L b c "$40\,\mathrm{mH}$" col=2
#@ el C c g "$10\,\mathrm{mF}$" col=3 plus=c v="$v_C$"
#@ note "Ground the bottom wire. Current tends to zero, so the capacitor approaches the new 100 V source."
```

**Problem: Try it 8 · Find only the starting conditions · P8.53 setup** (introductory)

The circuit above ran for a long time with $V_s=200\,\mathrm{V}$. At $t=0$, the source becomes $100\,\mathrm{V}$. Before solving any ODE, find $v_C(0^-)$, $i(0^-)$, $v_C(0^+)$, and $v_C^{\prime}(0^+)$.

<details><summary>Solution</summary>

1. Before the step, the capacitor is a DC open circuit, so series current is zero.

   $$i(0^-)=0$$
2. With no resistor fall and no inductor voltage, the capacitor holds the old source voltage.

   $$v_C(0^-)=200\,\mathrm{V}$$
3. The two stored quantities are continuous.

   $$v_C(0^+)=200\,\mathrm{V},\quad i(0^+)=0$$
4. Translate series current into the starting voltage slope.

   $$v_C^{\prime}(0^+)=\dfrac{0}{0.01}=0$$

**Answer:** $v_C(0^-)=v_C(0^+)=200\,\mathrm{V}$, $i(0^-)=0$, and $v_C^{\prime}(0^+)=0$. The capacitor does not instantly become 100 V.

</details>

```steps
title "Derive the series RLC equation"
$$ V_s=Ri+Li^{\prime}+v_C $$
KVL: the three element voltages sum to the source.
$$ i=\hl{Cv_C^{\prime}} $$
The series loop current equals capacitor current.
$$ V_s=RCv_C^{\prime}+LCv_C^{\prime\prime}+v_C $$
Substitute the current and its derivative.
$$ v_C^{\prime\prime}+\hl{\dfrac RL}v_C^{\prime}+\hl{\dfrac1{LC}}v_C=\hl{\dfrac{V_s}{LC}} $$
Divide by LC to normalise the equation.
$$ v_C=\hl{V_s}+u $$
For constant source voltage, subtract the constant particular solution.
$$ u^{\prime\prime}+\dfrac RL u^{\prime}+\dfrac1{LC}u=0 $$
The remaining transient obeys a homogeneous equation.
```

**Example: Example 3 · Finish the same circuit · textbook P8.53**

Find $v_C(t)$ for $t\ge0$, using the starting conditions already found above.

1. Convert mH and mF to H and F, then form the normalised equation.

   $$v_C^{\prime\prime}+100v_C^{\prime}+2500v_C=250000$$
2. Subtract the final value 100 V; the transient has a repeated root.

   $$s^2+100s+2500=(s+50)^2$$
3. Keep the final-value term as well as the repeated-root transient.

   $$v_C=100+(A+Bt)e^{-50t}$$
4. The starting voltage is 200 V.

   $$100+A=200\quad\Rightarrow\quad A=100$$
5. The starting slope is zero; use the product rule.

   $$B-50A=0\quad\Rightarrow\quad B=5000$$

**Answer:** $v_C=100+(100+5000t)e^{-50t}\,\mathrm{V}$ for $t\ge0$, with $t$ in seconds. It starts at 200 V with slope zero and approaches 100 V.

### Name the response only after finding its roots

Write the transient equation as $u^{\prime\prime}+2\alpha u^{\prime}+\omega_0^2u=0$. For series RLC, $\alpha=R/(2L)$ and $\omega_0=1/\sqrt{LC}$; the roots are $-\alpha\pm\sqrt{\alpha^2-\omega_0^2}$.

| Compare | Root case | Circuit name |
|---|---|---|
| $\alpha>\omega_0$ | Distinct real | Overdamped |
| $\alpha=\omega_0$ | Repeated real | Critically damped |
| $0<\alpha<\omega_0$ | Complex pair with negative real part | Underdamped |
| $\alpha=0$, $\omega_0>0$ | Purely imaginary pair | Undamped |

For an underdamped response, the oscillation frequency is $\omega_d=\sqrt{\omega_0^2-\alpha^2}$. In P8.53, $\alpha=\omega_0=50\,\mathrm{s^{-1}}$, so the response is critically damped.

### Parallel RLC: the starting slope comes from KCL

In a source-free parallel RLC circuit, all branches share voltage $v$ and all reference currents below point down. KCL gives $Cv^{\prime}+i_L+v/R=0$; differentiating and using $i_L^{\prime}=v/L$ gives the second-order voltage equation.

$$v^{\prime\prime}+\dfrac1{RC}v^{\prime}+\dfrac1{LC}v=0$$

The natural frequency is still $1/\sqrt{LC}$, but now $\alpha=1/(2RC)$. Most importantly, the starting slope is **not** $I_0/C$ as in the series circuit:

$$v^{\prime}(0^+)=-\dfrac{I_0+V_0/R}{C}$$

```schematic
C1 0,3 -> 0,0 "$10\,\mathrm{nF}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$250\,\mathrm{mH}$" i="$i_L$"
wire 3,3 -> 6,3
R1 6,3 -> 6,0 "$\dfrac{12500}{3}\,\Omega$" i="$i_R$"
wire 6,0 -> 0,0
ground 0,0
#@ view "Initial state"
#@ node a 90 "top: $90\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el C a g "$10\,\mathrm{nF}$" col=0 plus=a v="$v$" i="$8.4\,\mathrm{mA}$" to=g id=cap
#@ el L a g "$250\,\mathrm{mH}$" col=1 i="$30\,\mathrm{mA}$" to=a id=ind
#@ el R a g "$4166.67\,\Omega$" col=2 i="$21.6\,\mathrm{mA}$" to=g id=res
#@ step "Ground the bottom wire." show=g
#@ step "The given capacitor voltage sets the common top node at 90 V." show=a,cap
#@ step "Resistor current is 90/R = 21.6 mA downward; inductor current is 30 mA upward." show=ind,res
#@ step "KCL leaves 8.4 mA downward through C; divide by C to obtain its voltage slope." show=cap
#@ view "Final state"
#@ node a 0 "top: $0\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el C a g "$10\,\mathrm{nF}$" col=0 plus=a v="$v$"
#@ el L a g "$250\,\mathrm{mH}$" col=1
#@ el R a g "$4166.67\,\Omega$" col=2
#@ note "Ground the bottom wire. With no external source and finite positive R, the stored energy dissipates and the branch currents and voltage tend to zero."
```

**Problem: Try it 9 · Find the parallel-circuit slope first · P8.7 setup** (introductory)

For the circuit above, $V_0=90\,\mathrm{V}$ and $I_0=-30\,\mathrm{mA}$ in the downward inductor reference. Find $i_R(0^+)$, $i_C(0^+)$ and $v^{\prime}(0^+)$.

<details><summary>Solution</summary>

1. Use the common voltage across R.

   $$i_R=\dfrac{90}{12500/3}=0.0216\,\mathrm{A}$$
2. KCL uses the signed inductor current.

   $$i_C=-i_L-i_R=0.0300-0.0216=0.0084\,\mathrm{A}$$
3. Divide capacitor current by capacitance.

   $$v^{\prime}(0^+)=\dfrac{0.0084}{10^{-8}}=840000\,\mathrm{V/s}$$

**Answer:** $i_R=21.6\,\mathrm{mA}$, $i_C=8.4\,\mathrm{mA}$ and $v^{\prime}(0^+)=8.4\times10^5\,\mathrm{V/s}$.

</details>

**Example: Example 4 · Use that slope to complete the response · textbook P8.7**

Find $v(t)$ in the parallel circuit. Its initial voltage and slope are now known.

1. Use the parallel formula for damping and the common natural-frequency formula.

   $$\alpha=12000,\quad\omega_0=20000\quad(\mathrm{s^{-1}})$$
2. The roots are complex; compute the damped oscillation frequency.

   $$\omega_d=\sqrt{20000^2-12000^2}=16000\,\mathrm{rad/s}$$
3. Write the underdamped form and apply v(0) = 90.

   $$v=e^{-12000t}(90\cos16000t+B\sin16000t)$$
4. Use the product rule at zero and the slope from the preceding question.

   $$-12000(90)+16000B=840000$$
5. Solve for B.

   $$B=120$$

**Answer:** $v=e^{-12000t}(90\cos16000t+120\sin16000t)\,\mathrm{V}$ for $t\ge0$.

### Remove the resistor: oscillation without a decaying envelope

**Problem: Try it 10 · An ideal LC response · textbook P8.14** (introductory)

This is the P8.13 circuit with its resistor removed. Initially $v(0)=0$ and $i_L(0)=-3\,\mathrm{A}$ in the downward reference.

```schematic
C1 0,3 -> 0,0 "$250\,\mathrm{mF}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$0.4\,\mathrm{H}$" i="$i_L$"
wire 3,0 -> 0,0
ground 0,0
#@ spoiler
#@ view "Initial state"
#@ node a 0 "top: $0\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el C a g "$250\,\mathrm{mF}$" col=0 plus=a v="$v$" i="$3\,\mathrm{A}$" to=g id=cap
#@ el L a g "$0.4\,\mathrm{H}$" col=1 i="$3\,\mathrm{A}$" to=a id=ind
#@ step "Ground the bottom wire; the given capacitor voltage is zero." show=g,a
#@ step "The given inductor current is 3 A upward; KCL requires 3 A downward through C." show=cap,ind
#@ note "The voltage is instantaneously zero, but the inductor still stores energy. Capacitor voltage begins increasing at 3/0.25 = 12 V/s."
```

Find (a) $v(t)$, (b) its angular frequency and (c) its maximum amplitude. With no resistor branch, KCL is $i_C+i_L=0$.

<details><summary>Solution</summary>

1. Without a resistor, the voltage equation is undamped.

   $$v^{\prime\prime}+\dfrac1{LC}v=v^{\prime\prime}+10v=0$$
2. The starting voltage removes the cosine term.

   $$v=B\sin(\sqrt{10}\,t)$$
3. KCL gives the starting slope.

   $$v^{\prime}(0)=\dfrac3{0.25}=12$$
4. Apply the slope to determine the sine coefficient.

   $$B\sqrt{10}=12\quad\Rightarrow\quad B=\dfrac{12}{\sqrt{10}}$$

**Answer:** (a) $v=\dfrac{12}{\sqrt{10}}\sin(\sqrt{10}\,t)\,\mathrm{V}$. (b) $\omega_0=\sqrt{10}\approx3.162\,\mathrm{rad/s}$. (c) Amplitude $12/\sqrt{10}\approx3.795\,\mathrm{V}$; it does not decay in this ideal model.

</details>
