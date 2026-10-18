# Week 5: Second-Order Linear ODEs and RLC Circuits

## Topic 1: Second-order equations: guess $e^{st}$

A **second-order** ODE contains $y''=\dfrac{d^2y}{dt^2}$, the derivative of the derivative.

This week it has the form $ay''+by'+cy=0$:
- $a,b,c$: **constant** numbers
- right side $0$: **homogeneous** (no source)

**Guess $y=e^{st}$.** Each derivative of it is the same exponential times the number $s$, so everything can cancel.

```steps
title "From the ODE to the characteristic equation"
$$ ay''+by'+cy=0 $$
$a$, $b$, $c$ are constants.
$$ y=e^{st},\quad y'=\hl{s}e^{st},\quad y''=\hl{s^2}e^{st} $$
Each derivative brings out a factor $s$ (chain rule: $\frac{d}{dt}e^{st}=se^{st}$).
$$ a\hl{s^2e^{st}}+b\hl{se^{st}}+c\hl{e^{st}}=0 $$
Substitute the three pieces.
$$ \hl{(as^2+bs+c)}\,e^{st}=0 $$
Factor out $e^{st}$.
$$ as^2+bs+c=0 $$
$e^{st}$ is never $0$, so the bracket is. This is the **characteristic equation**.
$$ s_{1,2}=\dfrac{-b\pm\sqrt{\hl{b^2-4ac}}}{2a} $$
Quadratic formula. The sign of $b^2-4ac$ decides the kind of roots.
```

| Roots | General solution |
|---|---|
| two real, $s_1\neq s_2$ ($b^2-4ac>0$) | $y=C_1e^{s_1t}+C_2e^{s_2t}$ |
| one repeated, $s$ ($b^2-4ac=0$) | $y=(C_1+C_2t)\,e^{st}$ |
| complex pair, $\sigma\pm j\omega$ ($b^2-4ac<0$) | $y=e^{\sigma t}(C_1\cos\omega t+C_2\sin\omega t)$ |

Two constants need two conditions:
- $y(0)$: the start **value**
- $y'(0)$: the start **slope**

Each example below is one row of the table.

```graph
title "Where the roots of $s^2+bs+c=0$ sit"
x -8.5 3.5 label="Re $s$"
y -3.6 3.6 label="Im $s$"
equal
slider b -2 8 1 step=0.1 label="$b$" animate
slider c 0 10 4 step=0.25 label="$c$"
region "x>0" color=6 label="right half: $e^{st}$ grows"
circle "0" "0" "sqrt(c)" dash color=0 label="circle $|s|=\sqrt c$"
point "if(b^2-4*c>=0,(-b+sqrt(b^2-4*c))/2,-b/2)" "if(b^2-4*c>=0,0,sqrt(4*c-b^2)/2)" color=1
point "if(b^2-4*c>=0,(-b-sqrt(b^2-4*c))/2,-b/2)" "if(b^2-4*c>=0,0,-sqrt(4*c-b^2)/2)" color=3
text "if(b^2-4*c>=0,(-b+sqrt(b^2-4*c))/2,-b/2)+0.12" "if(b^2-4*c>=0,0,sqrt(4*c-b^2)/2)+0.12" "$s_1$" color=1
text "if(b^2-4*c>=0,(-b-sqrt(b^2-4*c))/2,-b/2)+0.12" "if(b^2-4*c>=0,0,-sqrt(4*c-b^2)/2)-0.55" "$s_2$" color=3
text "if(b^2-4*c-0.05,-8.2,sqrt(-1))" "3.1" "**two real roots**"
text "if(abs(b^2-4*c)<0.05,-8.2,sqrt(-1))" "3.1" "**one repeated root**"
text "if(4*c-b^2-0.05,-8.2,sqrt(-1))" "3.1" "**complex pair** $\sigma\pm j\omega$"
readout "$b^2-4c=$" "b^2-4*c"
readout "$s_1=$" "(-b+sqrt(b^2-4*c))/2"
readout "$s_2=$" "(-b-sqrt(b^2-4*c))/2"
readout "$\sigma=$" "if(4*c-b^2,-b/2,sqrt(-1))"
readout "$\omega=$" "sqrt(4*c-b^2)/2"
caption "Press play on $b$ and watch the two roots move."
```

What happens as $b$ changes (with $c=4$):
- **From $b=1$:** the complex pair slides round the dashed circle.
- **At $b=4$:** the roots meet on the real axis (repeated).
- **Above $b=4$:** they split into two real roots.
- **Negative $b$:** the roots move into the shaded half: growing solutions.

**Example: Example 1 · Two real roots: fit the two constants**

Solve $y''+3y'+2y=0$ with $y(0)=1$, $y'(0)=0$.

1. Characteristic equation; it factors ($1\cdot2=2$, $1+2=3$).

   $$s^2+3s+2=(s+1)(s+2)=0\ \Rightarrow\ s=-1,\ -2$$
2. Two different real roots: first row of the table.

   $$y=C_1e^{-t}+C_2e^{-2t}$$
3. ```steps
title "Fit $C_1$ and $C_2$"
$$ y=C_1e^{-t}+C_2e^{-2t} $$
The general solution.
$$ y'=\hl{-C_1e^{-t}-2C_2e^{-2t}} $$
Differentiate each term: $\frac{d}{dt}e^{st}=se^{st}$.
$$ y(0)=\hl{C_1+C_2}=1 $$
Put $t=0$ in $y$; every $e^{0}=1$.
$$ y'(0)=\hl{-C_1-2C_2}=0 $$
Put $t=0$ in $y'$.
$$ \hl{-C_2=1}\ \Rightarrow\ C_2=-1 $$
Add the two equations: $C_1$ cancels.
$$ C_1=1-C_2=\hl{2} $$
Back into the first equation.
$$ y=\hl{2}e^{-t}\hl{-}e^{-2t} $$
Check: $y(0)=2-1=1$, $y'(0)=-2+2=0$ ✓
```

**Answer:** $y=2e^{-t}-e^{-2t}$ (decays to $0$ without crossing it)

**Example: Example 2 · Repeated root: the extra $t$**

Solve $4y''+4y'+y=0$ with $y(0)=4$, $y'(0)=0$.

1. Keep $a=4$ (a common slip is $s^2+4s+1$). The left side is a perfect square.

   $$4s^2+4s+1=(2s+1)^2=0\ \Rightarrow\ s=-\tfrac12\ \text{twice}$$
2. One root gives only $e^{-t/2}$. Two copies of it are really one constant: it can't match a value **and** a slope.

   $$C_1e^{-t/2}+C_2e^{-t/2}=(C_1+C_2)\,e^{-t/2}$$
3. The second solution is $te^{-t/2}$:

   $$y=(C_1+C_2t)\,e^{-t/2}$$
4. Check that $te^{-t/2}$ is a solution: differentiate with the product rule, substitute, and everything cancels.

   $$\begin{gathered}y'=(1-\tfrac t2)e^{-t/2}, \\ y''=(-1+\tfrac t4)e^{-t/2} \\ 4(-1+\tfrac t4)+4(1-\tfrac t2)+t=0\ \checkmark\end{gathered}$$
5. Differentiate the general solution (product rule) and put $t=0$.

   $$y(0)=C_1=4,\qquad y'(0)=C_2-\tfrac12C_1=0$$
6. So $C_2=\tfrac12\cdot4=2$.

   $$y=(4+2t)\,e^{-t/2}$$

**Answer:** $y=(4+2t)\,e^{-t/2}$

**Example: Example 3 · Complex roots: where the cosine comes from**

Solve $y''+2y'+5y=0$ with $y(0)=1$, $y'(0)=1$.

1. Quadratic formula; $\sqrt{-16}=j4$.

   $$s=\frac{-2\pm\sqrt{4-20}}{2}=-1\pm j2$$
2. Euler (Week 1) splits each complex exponential into a cosine and a sine.

   $$e^{(-1\pm j2)t}=e^{-t}(\cos2t\pm j\sin2t)$$
3. Half their sum, and their difference over $2j$, are solutions too (sums and multiples of solutions are). No $j$ is left:

   $$y=e^{-t}(C_1\cos2t+C_2\sin2t)$$
4. At $t=0$: $\cos0=1$, $\sin0=0$.

   $$y(0)=C_1=1$$
5. Product rule, then $t=0$. In general $y'(0)=\sigma C_1+\omega C_2$, here with $\sigma=-1$, $\omega=2$.

   $$y'(0)=-C_1+2C_2=1\ \Rightarrow\ C_2=1$$

**Answer:** $y=e^{-t}(\cos2t+\sin2t)$: oscillates at $2$ rad/s inside the shrinking envelope $e^{-t}$

**Problem: Try it 1 · One equation, every case** (introductory)

Consider $y''+2y'+ky=0$.

1. For which $k$ are the roots two real, repeated, or complex? (Check in the graph: $b=2$, slide $c$.)
2. At $k=0$ one root is $s=0$. What is the general solution, and does every solution die out?

<details><summary>Solution</summary>

1. The case is the sign of $b^2-4ac$ with $a=1$, $b=2$, $c=k$.

   $$b^2-4ac=4-4k$$
2. Positive, zero, negative:

   $$k<1:\ \text{two real},\quad k=1:\ \text{repeated},\quad k>1:\ \text{complex}$$
3. $k=0$: $s^2+2s=s(s+2)=0$. The root $s=0$ gives $e^{0t}=1$, a constant.

   $$y=C_1+C_2e^{-2t}$$
4. $e^{-2t}\to0$ but $C_1$ stays: the solution settles at $C_1$, not $0$ (a root on the vertical axis does not decay).

   $$y\to C_1$$

**Answer:** 1. $k<1$: two real; $k=1$: repeated; $k>1$: complex.
2. $y=C_1+C_2e^{-2t}\to C_1$, so no.

</details>

**Problem: Try it 2 · Work backwards from a solution** (intermediate)

One solution of $y''+by'+cy=0$ is $e^{-3t}\cos4t$.

1. Find $b$ and $c$.
2. Solve with $y(0)=0$, $y'(0)=8$.

<details><summary>Solution</summary>

1. $e^{\sigma t}\cos\omega t$ comes from the roots $\sigma\pm j\omega$.

   $$s=-3\pm j4$$
2. Rebuild the quadratic as $(s-s_1)(s-s_2)$; note $(j4)^2=-16$.

   $$(s+3)^2-(j4)^2=s^2+6s+25\ \Rightarrow\ b=6,\ c=25$$
3. Complex row; $y(0)=C_1=0$ and $y'(0)=\sigma C_1+\omega C_2=4C_2=8$.

   $$C_1=0,\quad C_2=2$$

**Answer:** 1. $b=6$, $c=25$
2. $y=2e^{-3t}\sin4t$

</details>

## Topic 2: Existence and uniqueness: why two conditions are enough

A second-order equation needs two starting facts:
- $y(t_0)$: the start **value**
- $y'(t_0)$: the start **slope**

In a circuit they come from the capacitor voltage and the inductor current.

With both given there is **exactly one** solution. So once a formula fits both, it *is* the answer.

This is the second-order version of Week 3's theorem.

> **Info:** **Theorem.** Divide by the coefficient of $y''$ to get $y''+p(t)\,y'+q(t)\,y=g(t)$.
> 
> - **If** $p$, $q$, $g$ are continuous on an open interval $I$ containing $t_0$,
> - **then** for any numbers $Y_0$, $Y_1$ the problem $y(t_0)=Y_0$, $y'(t_0)=Y_1$ has **exactly one** solution, and it exists on all of $I$.
> 
> Constant coefficients are continuous everywhere, so Topic 1's solutions hold for all $t$.

**Why $C_1y_1+C_2y_2$ can always be fitted.** The two conditions are two linear equations for $C_1$, $C_2$.

They have a solution for every $Y_0$, $Y_1$ exactly when their determinant, the **Wronskian**, is not zero:

$$W=\begin{vmatrix}y_1&y_2\\ y_1'&y_2'\end{vmatrix}=y_1y_2'-y_1'y_2\neq0$$

**Example: Example 4 · Largest interval: division by zero**

$(t^2-9)\,y''+t\,y'+4y=e^t$, $\ y(1)=0$, $\ y'(1)=2$.

Find the largest interval on which this surely has exactly one solution.

1. Divide by $t^2-9$, the coefficient of $y''$.

   $$y''+\frac{t}{t^2-9}\,y'+\frac{4}{t^2-9}\,y=\frac{e^t}{t^2-9}$$
2. $p$, $q$, $g$ break only where the bottom is $0$.

   $$t^2-9=0\ \Rightarrow\ t=\pm3$$
3. Take the piece between the bad points that contains $t_0=1$. (Starting at $t_0=5$ would give $t>3$ instead.)

   $$-3<t<3$$

**Answer:** $-3<t<3$

**Example: Example 5 · Largest interval: the nearest trouble on each side**

Same question for $(t-2)\,y''+y'+(t-2)(\tan t)\,y=0$, $y(3)=1$, $y'(3)=0$.

1. Divide by $t-2$; in the last term it cancels.

   $$y''+\frac{1}{t-2}\,y'+(\tan t)\,y=0$$
2. The $y'$ coefficient breaks at $t=2$. $\tan t$ (sine over cosine) breaks where $\cos t=0$.

   $$\begin{gathered}t=2, \\ t=\pm\tfrac{\pi}{2}\approx\pm1.57,\ \pm\tfrac{3\pi}{2}\approx\pm4.71,\ \dots\end{gathered}$$
3. Nearest bad point left of $t_0=3$ is $2$; nearest on the right is $3\pi/2$.

   $$2<t<\dfrac{3\pi}{2}$$

**Answer:** $2<t<\dfrac{3\pi}{2}\approx4.71$

**Example: Example 6 · The Wronskian: why the repeated root needs $t$**

For $y''+4y'+4y=0$ (root $s=-2$ twice), test two pairs:

1. $e^{-2t}$ and $3e^{-2t}$
2. $e^{-2t}$ and $te^{-2t}$

1. **Pair 1:** $y_2'=-6e^{-2t}$, and the two products cancel.

   $$W=e^{-2t}(-6e^{-2t})-(-2e^{-2t})(3e^{-2t})=0$$
2. $W=0$ because $3e^{-2t}$ is just a multiple of $e^{-2t}$: this pair can't fit both conditions.
3. **Pair 2:** product rule gives $y_2'=(1-2t)e^{-2t}$; use $e^{-2t}e^{-2t}=e^{-4t}$.

   $$W=(1-2t)e^{-4t}+2t\,e^{-4t}=e^{-4t}\neq0$$

**Answer:** Only $e^{-2t}$ with $te^{-2t}$ works ($W=e^{-4t}\neq0$).

So $(C_1+C_2t)e^{-2t}$ is the general solution.

**Problem: Try it 3 · Logarithms: the start decides** (intermediate)

For $(t-1)\,y''+y'+y=\ln t$, find the largest guaranteed interval when the conditions are given at:

1. $t_0=2$
2. $t_0=\tfrac12$

<details><summary>Solution</summary>

1. Divide by $t-1$.

   $$y''+\frac{1}{t-1}\,y'+\frac{1}{t-1}\,y=\frac{\ln t}{t-1}$$
2. Bad points: $t=1$ (division by zero) and $t\le0$ (no $\ln$ there).

   $$t\le0,\qquad t=1$$
3. From $t_0=2$: nothing stops it on the right. From $t_0=\tfrac12$: trapped between $0$ and $1$.

   $$(1)\ t>1,\qquad (2)\ 0<t<1$$

**Answer:** 1. $t>1$
2. $0<t<1$

</details>

**Problem: Try it 4 · Uniqueness as a shortcut** (advanced)

1. Solve $y''+t\,y'+e^t\,y=0$ with $y(2)=0$, $y'(2)=0$ without any formula.
2. Why can $y=t^2$ never solve an equation $y''+p(t)\,y'+q(t)\,y=0$ with $p$, $q$ continuous near $t=0$?

<details><summary>Solution</summary>

1. $y=0$ satisfies the equation and both conditions. $p=t$, $q=e^t$ are continuous, so it is the only solution.

   $$y(t)=0$$
2. $y=t^2$ has $y(0)=0$ and $y'(0)=0$: the same start as $y=0$.

   $$y(0)=0,\quad y'(0)=0$$
3. Uniqueness would force $t^2=0$ near $t=0$, which is false. So no such equation exists.

   $$t^2\not\equiv0$$

**Answer:** 1. $y=0$.
2. $t^2$ and $0$ share the same start, so uniqueness would make them equal.

</details>

## Topic 3: RLC circuits

```schematic
V1 0,3 -> 0,0 "$V$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$R$" i="$i$"
L1 6,3 -> 9,3 "$L$"
C1 9,3 -> 9,0 "$C$" v="$v_C$"
wire 9,0 -> 0,0
ground 0,0
```

The circuit stores energy in two places, so it gives a second-order equation:
- the **capacitor** (its voltage $v_C$)
- the **inductor** (its current $i$)

Neither can jump at the switch, so the two starting facts are:
- $V_0=v_C(0^+)$
- $I_0=i(0^+)$

```steps
title "KVL gives a Topic 1 equation (Nilsson & Riedel 8.4)"
$$ V=Ri+L\dfrac{di}{dt}+v_C $$
KVL around the loop for $t>0$.
$$ V=\hl{RC\dfrac{dv_C}{dt}}+\hl{LC\dfrac{d^2v_C}{dt^2}}+v_C $$
The loop current is the capacitor current: $i=C\frac{dv_C}{dt}$.
$$ \dfrac{d^2v_C}{dt^2}+\hl{\dfrac{R}{L}}\dfrac{dv_C}{dt}+\hl{\dfrac{1}{LC}}v_C=\hl{\dfrac{V}{LC}} $$
Divide by $LC$.
$$ v_C=\hl{V}+v_n(t) $$
A constant solves it only if it equals $V$ (its derivatives are $0$): the **final value**. The rest, $v_n$, solves the same equation with $0$ on the right.
$$ s^2+\hl{2\alpha}s+\hl{\omega_0^2}=0,\quad \alpha=\dfrac{R}{2L},\ \ \omega_0=\dfrac{1}{\sqrt{LC}} $$
Characteristic equation of $v_n$. Textbook names: $\alpha$ (alpha, s$^{-1}$), $\omega_0$ (omega-zero, rad/s).
$$ s_{1,2}=-\alpha\pm\sqrt{\hl{\alpha^2-\omega_0^2}} $$
Quadratic formula: compare $\alpha$ with $\omega_0$.
```

| Case | Test | $v_C(t)$ for $t\ge0$ |
|---|---|---|
| **overdamped** | $\alpha>\omega_0$ | $V+A_1e^{s_1t}+A_2e^{s_2t}$ |
| **critically damped** | $\alpha=\omega_0$ | $V+(D_1t+D_2)\,e^{-\alpha t}$ |
| **underdamped** | $\alpha<\omega_0$ | $V+e^{-\alpha t}(B_1\cos\omega_dt+B_2\sin\omega_dt)$, $\ \omega_d=\sqrt{\omega_0^2-\alpha^2}$ |

> **Tip:** **The two conditions at $t=0^+$:**
> - **Value:** $v_C(0^+)=V_0$
> - **Slope:** $\dfrac{dv_C}{dt}(0^+)=\dfrac{i_C(0^+)}{C}$, from $i_C=C\dfrac{dv_C}{dt}$
> - **Series loop:** $i_C=i$, so the slope is $I_0/C$
> 
> **Parallel** RLC (no source, Fig. 8.1): KCL gives the same equation for $v$, with:
> - $\alpha=\dfrac{1}{2RC}$
> - no $V$
> - $\omega_0$ unchanged

```graph
title "Slide $R$ through the three cases"
x 0 8 label="$t$ (s)"
y 0 24 label="$v_C$ (V)"
slider R 0 10 1 step=0.1 label="$R$ ($\Omega$)" animate
hline "10" label="final value $V$"
curve "10*(1-if((R^2/4-4)-0.001,((-(R/2)+sqrt((R^2/4-4)))*exp((-(R/2)-sqrt((R^2/4-4)))*t)-(-(R/2)-sqrt((R^2/4-4)))*exp((-(R/2)+sqrt((R^2/4-4)))*t))/(2*sqrt((R^2/4-4))),if(-(R^2/4-4)-0.001,exp(-(R/2)*t)*(cos(sqrt(4-R^2/4)*t)+(R/2)/sqrt(4-R^2/4)*sin(sqrt(4-R^2/4)*t)),(1+(R/2)*t)*exp(-(R/2)*t))))" color=1 label="$v_C(t)$"
text "if((R^2/4-4)-0.001,4.2,sqrt(-1))" "22.6" "**overdamped**"
text "if(abs((R^2/4-4))<0.001,4.2,sqrt(-1))" "22.6" "**critically damped**"
text "if((-(R^2/4-4)-0.001)*(R>0.001),4.2,sqrt(-1))" "22.6" "**underdamped**"
text "if(R<0.001,4.2,sqrt(-1))" "22.6" "**undamped** (LC: $\alpha=0$)"
readout "$\alpha=$" "R/2"
readout "$\omega_0=$" "2"
readout "$s_1=$" "-R/2+sqrt(R^2/4-4)"
readout "$s_2=$" "-R/2-sqrt(R^2/4-4)"
readout "$\omega_d=$" "sqrt(4-R^2/4)"
caption "$L=1$ H, $C=0.25$ F, $V=10$ V, starting from $v_C(0)=0$, $i(0)=0$. A dash in a readout means that kind of root doesn't exist."
```

Critical at $R=4\,\Omega$, where $\alpha=\omega_0=2$:
- **Below it:** the voltage overshoots and rings ($R=0$: forever).
- **Above it:** it creeps up.

**Example: Example 7 · Constant impressed voltage: a step response (textbook 8.53)**

The circuit has run for a long time with $v_s=200\,\mathrm{V}$. At $t=0$ the source drops to $100\,\mathrm{V}$.

Find $v_o(t)$ for $t\ge0$.

```schematic
V1 0,3 -> 0,0 "$v_s$"
R1 0,3 -> 3,3 "$4\,\Omega$" i="$i$"
L1 3,3 -> 6,3 "$40\,\mathrm{mH}$"
C1 6,3 -> 6,0 "$10\,\mathrm{mF}$" v="$v_o$"
wire 6,0 -> 0,0
ground 0,0
```

1. Before $t=0$ (DC for a long time) the capacitor is an open circuit: no current, so it holds all $200$ V.

   $$V_0=200\ \mathrm{V},\qquad I_0=0$$
2. After the drop, $V=100$ V. Series formulas ($L=0.04$ H, $C=0.01$ F):

   $$\begin{gathered}\alpha=\frac{4}{2(0.04)}=50, \\ \omega_0=\frac{1}{\sqrt{0.04\cdot0.01}}=50\end{gathered}$$
3. $\alpha=\omega_0$: critically damped, root $-50$ twice. The final value is the new source voltage.

   $$v_o=100+(D_1t+D_2)\,e^{-50t}$$
4. Value at $t=0$: the $D_1t$ term is $0$. Keep the $100$ (forgetting it is the classic slip).

   $$100+D_2=200\ \Rightarrow\ D_2=100$$
5. Slope at $0^+$ is $I_0/C=0$. The form has slope $D_1-50D_2$ at $t=0$ (product rule).

   $$D_1-50(100)=0\ \Rightarrow\ D_1=5000$$

**Answer:** $v_o(t)=100+(5000t+100)\,e^{-50t}$ V: from $200$ V down to $100$ V with no overshoot

**Example: Example 8 · Parallel, underdamped (textbook 8.7)**

Source-free parallel RLC:
- **Parts:** $R=12\,500/3\,\Omega$, $L=250\,\mathrm{mH}$, $C=10\,\mathrm{nF}$
- **Start:** $V_0=v(0)=90\,\mathrm{V}$, $I_0=i_L(0)=-30\,\mathrm{mA}$

Find $v(t)$.

```schematic
C1 0,3 -> 0,0 "$10\,\mathrm{nF}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$250\,\mathrm{mH}$" i="$i_L$"
wire 3,3 -> 6,3
R1 6,3 -> 6,0 "$R$" i="$i_R$"
wire 6,0 -> 0,0
ground 0,0
```

1. Parallel uses $\alpha=1/(2RC)$; dividing by $12\,500/3$ puts the $3$ on top.

   $$\alpha=\frac{3}{2(12\,500)(10^{-8})}=12\,000\ \mathrm{s^{-1}}$$
2. $\omega_0$ is bigger than $\alpha$: underdamped.

   $$\begin{gathered}\omega_0=\frac{1}{\sqrt{(0.25)(10^{-8})}}=20\,000, \\ \omega_d=\sqrt{20\,000^2-12\,000^2}=16\,000\ \mathrm{rad/s}\end{gathered}$$
3. Underdamped form (no source, so no $V$); at $t=0$ it gives $B_1=V_0$.

   $$v=e^{-12\,000t}(B_1\cos16\,000t+B_2\sin16\,000t),\quad B_1=90$$
4. Slope from KCL ($i_C+i_L+i_R=0$). $I_0$ is $-30$ mA, so $-I_0=+0.03$: watch the sign.

   $$i_C(0^+)=-\frac{90}{12\,500/3}+0.03=0.0084\ \mathrm{A}$$
5. Starting slope $i_C/C=8.4\times10^5$ V/s. The form has slope $-\alpha B_1+\omega_dB_2$ at $t=0$.

   $$-12\,000(90)+16\,000B_2=8.4\times10^5\ \Rightarrow\ B_2=120$$

**Answer:** $v(t)=e^{-12\,000t}(90\cos16\,000t+120\sin16\,000t)$ V

**Problem: Try it 5 · No resistor (textbook 8.14)** (intermediate)

Remove the resistor: $C=250\,\mathrm{mF}$ in parallel with $L=0.4\,\mathrm{H}$. The start:
- $v(0)=0$
- $i_L(0)=-3\,\mathrm{A}$ (drawn downward)

```schematic
C1 0,3 -> 0,0 "$250\,\mathrm{mF}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$0.4\,\mathrm{H}$" i="$i_L$"
wire 3,0 -> 0,0
ground 0,0
```

Find $v(t)$, its frequency in rad/s and its amplitude.

<details><summary>Solution</summary>

1. No $R$ means no $\frac{1}{RC}$ term, so $\alpha=0$. And $LC=0.4\cdot0.25=0.1$.

   $$v''+10v=0\ \Rightarrow\ s=\pm j\sqrt{10}$$
2. $\sigma=0$: the envelope is $e^{0t}=1$. $v(0)=0$ removes the cosine.

   $$v=B_2\sin\sqrt{10}\,t$$
3. KCL with two branches gives $i_C(0)=-i_L(0)=3$ A. The slope is $i_C/C$; the form's slope at $0$ is $\sqrt{10}\,B_2$.

   $$v'(0)=\frac{3}{0.25}=12=\sqrt{10}\,B_2\ \Rightarrow\ B_2=\frac{12}{\sqrt{10}}\approx3.795\ \mathrm{V}$$

**Answer:** $v=3.795\sin(3.162\,t)$ V
- frequency $\sqrt{10}\approx3.162$ rad/s
- amplitude $3.795$ V
- it never dies out

</details>

**Problem: Try it 6 · From the response back to the circuit (textbook 8.2)** (intermediate)

In this source-free parallel RLC:
- $C=18\,\mu\mathrm{F}$
- $v(t)=-12\left(e^{-200t}+e^{-1800t}\right)$ V for $t\ge0$

Find $R$ and $i_L(0^+)$.

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

1. The exponents are the roots $-200$, $-1800$. Rebuild the characteristic equation and match it to $s^2+\frac{1}{RC}s+\frac{1}{LC}$.

   $$(s+200)(s+1800)=s^2+2000s+360\,000$$
2. So $\frac{1}{RC}=2000$.

   $$R=\frac{1}{2000\,(18\times10^{-6})}\approx27.78\ \Omega$$
3. Read the start off $v(t)$ ($\frac{d}{dt}e^{st}=se^{st}$), then $i_C=Cv'$ and $i_R=v/R$.

   $$\begin{gathered}v(0)=-24\ \mathrm{V}, \\ v'(0)=-12(-200-1800)=24\,000\ \mathrm{V/s} \\ i_C=0.432\ \mathrm{A},\quad i_R=-0.864\ \mathrm{A}\end{gathered}$$
4. KCL: $i_L=-i_C-i_R$.

   $$i_L(0^+)=-0.432+0.864=0.432\ \mathrm{A}$$

**Answer:** $R\approx27.78\,\Omega$, $i_L(0^+)=432$ mA

</details>
