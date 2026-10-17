# Week 3: Linear and Separable First-Order ODEs; Existence and Uniqueness

> **Info:** **Week 3 in one sentence:** most first-order ODEs you will meet by hand are solved by one of two methods (the *integrating factor* for linear equations, or *separation of variables* for separable ones), and the *existence and uniqueness theorem* tells you when an initial value problem has exactly one answer.
> 
> **By the end you can:**
> - put a linear first-order ODE into standard form and solve it with an integrating factor;
> - spot a separable ODE, separate it, integrate both sides and fix the constant from an initial condition;
> - tell whether an ODE is linear, separable, both, or neither;
> - check the conditions of the existence and uniqueness theorem;
> - find the largest interval on which a linear initial value problem is guaranteed a unique solution.

## Topic 1: Linear first-order ODEs and the integrating factor

A first-order ODE is **linear** when $y$ and $\dfrac{dy}{dt}$ appear only to the first power and are never multiplied together; you can always rearrange it into the **standard form** $\dfrac{dy}{dt}+a(t)\,y=f(t)$, where $a(t)$ is the *coefficient* (the number or function in front of $y$) and $f(t)$ is the *forcing* (the input, e.g. a source voltage). The trick is to multiply the whole equation by a cleverly chosen function, the **integrating factor** $\mu(t)$ (mu), that turns the left side into the derivative of one product, $\dfrac{d}{dt}\big[\mu(t)\,y\big]$. Once the left side is a single derivative you just integrate both sides and divide by $\mu$. Use it for every RL or RC circuit with one energy-storing element, and for any linear first-order ODE, even when $a(t)$ changes with time. (Shorthand used in a few places below: $y'$ means $\dfrac{dy}{dt}$.)

> **Tip:** **The method (integrating factor)**
> 
> 1. **Standard form.** Divide by whatever multiplies $\dfrac{dy}{dt}$ so the equation reads $\dfrac{dy}{dt}+a(t)\,y=f(t)$. Read off $a(t)$ *with its sign*.
> 2. **Integrating factor.** Compute $\mu(t)=e^{\int a(t)\,dt}$. No $+C$ is needed here (any one antiderivative works).
> 3. **Multiply and collapse.** Multiply both sides by $\mu$; the left side is now exactly $\dfrac{d}{dt}\big[\mu\,y\big]$.
> 4. **Integrate both sides.** $\mu\,y=\int \mu\,f\,dt+C$. Do **not** forget the $+C$.
> 5. **Divide by $\mu$**, then use the initial condition $y(t_0)=y_0$ to find $C$.

**Why it works.** Take $\mu=e^{\int a\,dt}$. By the chain rule its derivative is $\mu'=a(t)\,\mu$. Now apply the product rule to $\mu y$: $\dfrac{d}{dt}[\mu y]=\mu\dfrac{dy}{dt}+\mu' y=\mu\dfrac{dy}{dt}+a\,\mu\,y=\mu\Big(\dfrac{dy}{dt}+a\,y\Big)$. The bracket is the left side of the ODE, so multiplying the ODE by $\mu$ gives $\dfrac{d}{dt}[\mu y]=\mu f$: one derivative on the left, which we can undo by integrating.

$$\begin{gathered}\mu(t)=e^{\int a(t)\,dt} \\ \frac{d}{dt}\big[\mu\,y\big]=\mu\,f(t)\end{gathered}$$

$$y(t)=\frac{1}{\mu(t)}\left[\int \mu(t)\,f(t)\,dt+C\right]$$

> **Info:** **Calculus reminder (for Example 1):**
> - **Product rule:** $\dfrac{d}{dt}\big[u\,v\big]=u'\,v+u\,v'$.
> - **Exponentials:** $\dfrac{d}{dt}e^{kt}=k\,e^{kt}$, so $\displaystyle\int e^{kt}\,dt=\frac{1}{k}e^{kt}+C$ (for a constant $k\neq 0$).
> - **Constant $a$:** if $a(t)=a$ is a constant, $\int a\,dt=a\,t$ and the integrating factor is simply $e^{at}$.

**Example: Example 1 · RL circuit: current after the switch closes**

A $100\,\mathrm{V}$ source, a switch, a $10\,\Omega$ resistor and a $2\,\mathrm{H}$ inductor are in series. The switch closes at $t=0$ and the inductor carries no current before that, so $i(0)=0$. Find the current $i(t)$ for $t\ge 0$.

```schematic
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$10\,\Omega$"
L1 6,3 -> 6,0 "$2\,\mathrm{H}$" i="$i$"
wire 6,0 -> 0,0
ground 0,0
```

1. Apply KVL (Kirchhoff’s voltage law: the voltage drops around a closed loop add up to the source voltage). The resistor drops $R\,i$ and the inductor drops $L\,\dfrac{di}{dt}$, where $R=10\,\Omega$ is the resistance and $L=2\,\mathrm{H}$ the inductance.

   $$\begin{gathered}L\frac{di}{dt}+R\,i=100 \\ 2\frac{di}{dt}+10\,i=100\end{gathered}$$
2. Divide both sides by $L=2$ so the $\dfrac{di}{dt}$ term stands alone; this is the standard form with $a=5$ (a constant) and $f=50$.

   $$\frac{di}{dt}+5\,i=50$$
3. Compute the integrating factor. Since $a=5$ is constant, $\int 5\,dt=5t$.

   $$\mu=e^{\int 5\,dt}=e^{5t}$$
4. Multiply every term by $e^{5t}$.

   $$e^{5t}\frac{di}{dt}+5e^{5t}\,i=50\,e^{5t}$$
5. Recognise the left side as a product-rule derivative: $\dfrac{d}{dt}\big[i\,e^{5t}\big]=e^{5t}\dfrac{di}{dt}+i\cdot 5e^{5t}$, which is exactly what we have.

   $$\frac{d}{dt}\big[i\,e^{5t}\big]=50\,e^{5t}$$
6. Integrate both sides with respect to $t$. On the right, $\int e^{5t}\,dt=\tfrac15 e^{5t}$, so $\int 50e^{5t}\,dt=\tfrac{50}{5}e^{5t}=10e^{5t}$; add one constant $C$.

   $$i\,e^{5t}=10\,e^{5t}+C$$
7. Use $i(0)=0$: put $t=0$, where $e^{0}=1$.

   $$0=10+C\ \Rightarrow\ C=-10$$
8. Substitute $C$ and divide both sides by $e^{5t}$ (dividing by $e^{5t}$ is the same as multiplying by $e^{-5t}$).

   $$\begin{aligned}i(t)&=10-10\,e^{-5t} \\ &=10\big(1-e^{-5t}\big)\ \mathrm{A}\end{aligned}$$
9. Sanity check: at $t=0$ the current is $0$, and as $t\to\infty$ it approaches $100/10=10\,\mathrm{A}$, the current when the inductor acts like a plain wire. The *time constant* $\tau$ (tau) $=L/R=0.2\,\mathrm{s}$ is the time to cover 63% of the change.

   $$\tau=\frac{L}{R}=\frac{2}{10}=0.2\ \mathrm{s}$$

**Answer:** $i(t)=10\big(1-e^{-5t}\big)\ \mathrm{A}$ for $t\ge 0$

> **Info:** **Calculus reminder (for Examples 2–4):**
> - **Log integral:** $\displaystyle\int \frac{1}{u}\,du=\ln|u|+C$. More generally $\displaystyle\int \frac{g'(t)}{g(t)}\,dt=\ln|g(t)|+C$ (top is the derivative of the bottom).
> - **Undoing a log:** $e^{\ln A}=A$ for $A>0$, and $e^{k\ln u}=e^{\ln u^{k}}=u^{k}$. Also $e^{-\ln u}=1/u$.
> - **Substitution:** to find $\int (2t+5)^5\,dt$, set $u=2t+5$; then $du=2\,dt$, so $dt=\tfrac12\,du$ and the integral becomes $\tfrac12\int u^5\,du=\tfrac12\cdot\tfrac{u^6}{6}$.
> - **Power rule:** $\displaystyle\int u^{n}\,du=\frac{u^{n+1}}{n+1}+C$ for $n\neq -1$.

**Example: Example 2 · Lecture Example 3.1: a time-varying coefficient**

Solve $\dfrac{dy}{dt}+\dfrac{10\,y}{2t+5}=10$ with $y(0)=0$.

1. The equation is already in standard form; read off the coefficient of $y$ and the forcing.

   $$\begin{gathered}a(t)=\frac{10}{2t+5} \\ f(t)=10\end{gathered}$$
2. Integrate $a(t)$ by substitution: $u=2t+5$, $du=2\,dt$, so $dt=\tfrac12 du$. Then use $\int du/u=\ln|u|$. Near $t=0$, $2t+5>0$, so the absolute value bars can go.

   $$\int \frac{10}{2t+5}\,dt=\int\frac{10}{u}\cdot\frac{du}{2}=5\ln(2t+5)$$
3. Build the integrating factor. Write $5\ln(2t+5)=\ln(2t+5)^5$ and use $e^{\ln A}=A$.

   $$\begin{aligned}\mu&=e^{5\ln(2t+5)}=e^{\ln(2t+5)^5} \\ &=(2t+5)^5\end{aligned}$$
4. Multiplying the ODE by $\mu$ turns the left side into the derivative of $y\,\mu$ (that is the whole point of $\mu$), and the right side becomes $10\,\mu$.

   $$\frac{d}{dt}\Big[y\,(2t+5)^5\Big]=10\,(2t+5)^5$$
5. Integrate both sides. On the right use the same substitution $u=2t+5$, $dt=\tfrac12du$, then the power rule $\int u^5du=u^6/6$.

   $$10\int (2t+5)^5dt=\frac{10}{2}\int u^5\,du=\frac{5}{6}u^6$$
6. So, with one constant $C$:

   $$y\,(2t+5)^5=\frac{5}{6}(2t+5)^6+C$$
7. Apply $y(0)=0$: at $t=0$, $2t+5=5$.

   $$\begin{gathered}0=\frac{5}{6}\,5^6+C \\ C=-\frac{5^7}{6}\approx-13\,020.83\end{gathered}$$
8. Divide both sides by $(2t+5)^5$. In the first term $(2t+5)^6/(2t+5)^5=(2t+5)$.

   $$y(t)=\frac{5}{6}(2t+5)-\frac{5^7}{6\,(2t+5)^5}$$

**Answer:** $y(t)=\dfrac{5}{6}(2t+5)-\dfrac{5^7}{6\,(2t+5)^5}$

**Example: Example 3 · Divide first: $a(t)=2/t$**

Solve $t\,\dfrac{dy}{dt}+2y=4t^2$ with $y(1)=2$, for $t>0$.

1. The $\dfrac{dy}{dt}$ term has a $t$ in front, so divide every term by $t$ (allowed because $t>0$) to reach standard form.

   $$\begin{gathered}\frac{dy}{dt}+\frac{2}{t}\,y=4t \\ a(t)=\frac{2}{t},\quad f(t)=4t\end{gathered}$$
2. Integrate $a$: $\int \frac{2}{t}\,dt=2\ln t$ (no bars needed since $t>0$). Then $e^{2\ln t}=e^{\ln t^2}=t^2$.

   $$\mu=e^{2\ln t}=t^2$$
3. Multiply by $t^2$; the left side becomes $\dfrac{d}{dt}[t^2y]$ (check: product rule gives $t^2\dfrac{dy}{dt}+2t\,y$, which is $t^2$ times the left side).

   $$\frac{d}{dt}\big[t^2y\big]=4t\cdot t^2=4t^3$$
4. Integrate both sides with the power rule, $\int 4t^3dt=t^4$, and add $C$.

   $$t^2y=t^4+C$$
5. Divide by $t^2$.

   $$y=t^2+\frac{C}{t^2}$$
6. Use $y(1)=2$.

   $$2=1+C\ \Rightarrow\ C=1$$
7. Write the answer.

   $$y(t)=t^2+\frac{1}{t^2},\quad t>0$$

**Answer:** $y(t)=t^2+\dfrac{1}{t^2}$ for $t>0$

**Example: Example 4 · A trigonometric coefficient: $a(t)=\tan t$**

Solve $\dfrac{dy}{dt}+(\tan t)\,y=\cos t$ with $y(0)=2$, on $-\tfrac{\pi}{2}<t<\tfrac{\pi}{2}$.

1. Already in standard form, with $a(t)=\tan t$ and $f(t)=\cos t$.

   $$a(t)=\tan t=\frac{\sin t}{\cos t}$$
2. Integrate $\tan t$ by substitution: $u=\cos t$, $du=-\sin t\,dt$, so $\sin t\,dt=-du$. On this interval $\cos t>0$, so no bars.

   $$\int\frac{\sin t}{\cos t}\,dt=\int\frac{-du}{u}=-\ln(\cos t)$$
3. Build $\mu$ using $e^{-\ln u}=1/u$. ($\sec t$ means $1/\cos t$.)

   $$\mu=e^{-\ln\cos t}=\frac{1}{\cos t}=\sec t$$
4. Multiply the ODE by $\sec t$; the left side collapses to $\dfrac{d}{dt}[y\sec t]$ and the right side is $\cos t\cdot\dfrac{1}{\cos t}=1$.

   $$\frac{d}{dt}\big[y\sec t\big]=1$$
5. Integrate both sides: $\int 1\,dt=t$.

   $$y\sec t=t+C$$
6. Multiply by $\cos t$ (the same as dividing by $\sec t$).

   $$y=(t+C)\cos t$$
7. Use $y(0)=2$: $\cos 0=1$.

   $$2=(0+C)\cdot 1\ \Rightarrow\ C=2$$
8. Final answer.

   $$y(t)=(t+2)\cos t$$

**Answer:** $y(t)=(t+2)\cos t$ on $-\tfrac{\pi}{2}<t<\tfrac{\pi}{2}$

> **Info:** **Calculus reminder (for Example 5): integration by parts.**
> $\displaystyle\int u\,dv=u\,v-\int v\,du$. Use it for a product like $t\,e^{2t}$: let $u$ be the part that gets simpler when differentiated ($u=t$, so $du=dt$) and $dv$ the part you can integrate ($dv=e^{2t}dt$, so $v=\tfrac12e^{2t}$).

**Example: Example 5 · Ramp input: needs integration by parts**

Solve $\dfrac{dy}{dt}+2y=4t$ with $y(0)=1$. (This is, for example, an RC circuit with time constant $0.5\,\mathrm{s}$ driven by a ramp.)

1. Standard form already: $a=2$ (constant), $f=4t$. The integrating factor is $e^{2t}$.

   $$\mu=e^{\int 2\,dt}=e^{2t}$$
2. Multiply by $e^{2t}$ and collapse the left side into one derivative.

   $$\frac{d}{dt}\big[y\,e^{2t}\big]=4t\,e^{2t}$$
3. Integrate the right side by parts with $u=4t$ ($du=4\,dt$) and $dv=e^{2t}dt$ ($v=\tfrac12e^{2t}$).

   $$\begin{aligned}\int 4t\,e^{2t}dt&=4t\cdot\tfrac12e^{2t} \\ &\quad-\int\tfrac12e^{2t}\cdot 4\,dt\end{aligned}$$
4. Simplify: the first term is $2t\,e^{2t}$, and the leftover integral is $\int 2e^{2t}dt=e^{2t}$.

   $$\int 4t\,e^{2t}dt=2t\,e^{2t}-e^{2t}+C$$
5. So $y\,e^{2t}=2te^{2t}-e^{2t}+C$; divide every term by $e^{2t}$.

   $$y=2t-1+C\,e^{-2t}$$
6. Use $y(0)=1$.

   $$1=0-1+C\ \Rightarrow\ C=2$$
7. Final answer. After the exponential dies out, $y\approx2t-1=2(t-0.5)$: the line $2t$ (where $y$ would sit if it could keep up instantly) delayed by $0.5\,\mathrm{s}$, exactly one time constant.

   $$y(t)=2t-1+2e^{-2t}$$

**Answer:** $y(t)=2t-1+2e^{-2t}$

> **Warning:** **Common mistakes**
> 
> - **Skipping standard form.** For $2\dfrac{di}{dt}+10i=100$ the coefficient is $a=5$, not $10$: divide by the $2$ first. For $t\dfrac{dy}{dt}+2y=4t^2$ you must divide by $t$, which also changes $f$ to $4t$.
> - **Losing the sign of $a(t)$.** $\dfrac{dy}{dt}=3y+6$ becomes $\dfrac{dy}{dt}-3y=6$, so $a=-3$ and $\mu=e^{-3t}$, not $e^{3t}$.
> - **Adding $C$ too late.** The constant appears when you integrate, and then it gets divided by $\mu$ too: $y=10+Ce^{-5t}$, not $y=10e^{-5t}\cdot\ldots+C$.
> - **Using $y(0)$ before integrating.** Find $C$ only after you have the general solution.

**Problem: Try it 1 · Constant coefficient** (introductory)

Solve $\dfrac{dy}{dt}+4y=8$ with $y(0)=5$.

<details><summary>Solution</summary>

1. Standard form with $a=4$, $f=8$; the integrating factor is $e^{4t}$.

   $$\mu=e^{4t}$$
2. Multiply through and collapse the left side.

   $$\frac{d}{dt}\big[y\,e^{4t}\big]=8\,e^{4t}$$
3. Integrate: $\int 8e^{4t}dt=\tfrac84e^{4t}=2e^{4t}$; add $C$.

   $$y\,e^{4t}=2e^{4t}+C$$
4. Divide by $e^{4t}$.

   $$y=2+C\,e^{-4t}$$
5. Use $y(0)=5$.

   $$5=2+C\ \Rightarrow\ C=3$$
6. Answer: starts at 5 and decays to the steady value 2.

   $$y(t)=2+3e^{-4t}$$

**Answer:** $y(t)=2+3e^{-4t}$

</details>

**Problem: Try it 2 · Watch the sign** (introductory)

Solve $\dfrac{dy}{dt}=3y+6$ with $y(0)=0$.

<details><summary>Solution</summary>

1. Move the $y$ term to the left to reach standard form. Its coefficient is $-3$.

   $$\begin{gathered}\frac{dy}{dt}-3y=6 \\ a=-3\end{gathered}$$
2. Integrating factor: $\int(-3)\,dt=-3t$.

   $$\mu=e^{-3t}$$
3. Multiply through and collapse the left side.

   $$\frac{d}{dt}\big[y\,e^{-3t}\big]=6\,e^{-3t}$$
4. Integrate: $\int 6e^{-3t}dt=\tfrac{6}{-3}e^{-3t}=-2e^{-3t}$.

   $$y\,e^{-3t}=-2e^{-3t}+C$$
5. Divide by $e^{-3t}$ (the same as multiplying by $e^{3t}$).

   $$y=-2+C\,e^{3t}$$
6. Use $y(0)=0$.

   $$0=-2+C\ \Rightarrow\ C=2$$
7. Answer. Because $a<0$ the solution grows instead of settling.

   $$y(t)=2e^{3t}-2$$

**Answer:** $y(t)=2e^{3t}-2$

</details>

**Problem: Try it 3 · RC circuit charging** (intermediate)

A $12\,\mathrm{V}$ source charges an initially uncharged $100\,\mu\mathrm{F}$ capacitor through a $1\,\mathrm{k}\Omega$ resistor; the switch closes at $t=0$, so the capacitor voltage starts at $v(0)=0$.

```schematic
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$1\,\mathrm{k}\Omega$" i="$i$"
C1 6,3 -> 6,0 "$100\,\mu\mathrm{F}$" v="$v$"
wire 6,0 -> 0,0
ground 0,0
```

1. Write the ODE for the capacitor voltage $v(t)$.
2. Solve it.
3. When does $v$ reach $6\,\mathrm{V}$?

<details><summary>Solution</summary>

1. KVL around the loop: the resistor drop $R\,i$ plus the capacitor voltage $v$ equals $12$. The capacitor current is $i=C\dfrac{dv}{dt}$, where $C=100\,\mu\mathrm{F}$ is the capacitance (so here we call the integration constant $K$ instead of $C$).

   $$RC\,\frac{dv}{dt}+v=12$$
2. Compute $RC=1000\times 100\times10^{-6}=0.1\,\mathrm{s}$; then divide by $0.1$ for standard form.

   $$\begin{gathered}0.1\frac{dv}{dt}+v=12 \\ \frac{dv}{dt}+10\,v=120\end{gathered}$$
3. Integrating factor $e^{10t}$; multiply and collapse.

   $$\frac{d}{dt}\big[v\,e^{10t}\big]=120\,e^{10t}$$
4. Integrate: $\int 120e^{10t}dt=12e^{10t}$; add $K$.

   $$v\,e^{10t}=12e^{10t}+K$$
5. Divide by $e^{10t}$ and use $v(0)=0$: $0=12+K$, so $K=-12$.

   $$v(t)=12\big(1-e^{-10t}\big)\ \mathrm{V}$$
6. For part 3 set $v=6$: $1-e^{-10t}=\tfrac12$, so $e^{-10t}=\tfrac12$. Take $\ln$ of both sides ($\ln\tfrac12=-\ln2$).

   $$\begin{gathered}-10t=-\ln 2 \\ t=\frac{\ln 2}{10}\approx 0.0693\ \mathrm{s}\end{gathered}$$

**Answer:** (1) $\dfrac{dv}{dt}+10v=120$  (2) $v(t)=12(1-e^{-10t})$ V  (3) $t=\ln2/10\approx 69.3$ ms

</details>

**Problem: Try it 4 · Divide by $t$ first** (intermediate)

Solve $t\,\dfrac{dy}{dt}+3y=10t^2$ with $y(1)=3$, for $t>0$.

<details><summary>Solution</summary>

1. Divide by $t$ to get standard form.

   $$\frac{dy}{dt}+\frac{3}{t}\,y=10t$$
2. Integrate $a$: $\int\frac3t\,dt=3\ln t$, and $e^{3\ln t}=t^3$.

   $$\mu=t^3$$
3. Multiply by $t^3$ and collapse.

   $$\frac{d}{dt}\big[t^3y\big]=10t^4$$
4. Integrate with the power rule: $\int 10t^4dt=2t^5$.

   $$t^3y=2t^5+C$$
5. Divide by $t^3$.

   $$y=2t^2+\frac{C}{t^3}$$
6. Use $y(1)=3$.

   $$3=2+C\ \Rightarrow\ C=1$$
7. Answer.

   $$y(t)=2t^2+\frac{1}{t^3}$$

**Answer:** $y(t)=2t^2+t^{-3}$, $t>0$

</details>

**Problem: Try it 5 · Coefficient $\cot t$** (advanced)

Solve $\dfrac{dy}{dt}+(\cot t)\,y=2\cos t$ with $y(\pi/2)=3$, on $0<t<\pi$. ($\cot t=\cos t/\sin t$.)

<details><summary>Solution</summary>

1. Standard form already: $a=\cot t=\dfrac{\cos t}{\sin t}$. The top is the derivative of the bottom, so (substitution $u=\sin t$, $du=\cos t\,dt$) the integral is a log. On $0<t<\pi$, $\sin t>0$.

   $$\int\frac{\cos t}{\sin t}dt=\int\frac{du}{u}=\ln(\sin t)$$
2. Integrating factor via $e^{\ln A}=A$.

   $$\mu=e^{\ln\sin t}=\sin t$$
3. Multiply by $\sin t$ and collapse the left side.

   $$\frac{d}{dt}\big[y\sin t\big]=2\sin t\cos t$$
4. Integrate the right side by substitution $u=\sin t$, $du=\cos t\,dt$: $\int 2u\,du=u^2$.

   $$y\sin t=\sin^2t+C$$
5. Divide by $\sin t$.

   $$y=\sin t+\frac{C}{\sin t}$$
6. Use $y(\pi/2)=3$: $\sin(\pi/2)=1$.

   $$3=1+C\ \Rightarrow\ C=2$$
7. Answer.

   $$y(t)=\sin t+\frac{2}{\sin t}$$

**Answer:** $y(t)=\sin t+\dfrac{2}{\sin t}$ on $0<t<\pi$

</details>

## Topic 2: Separable ODEs

An ODE is **separable** when you can put every $y$ (together with $dy$) on one side and every $t$ (together with $dt$) on the other; in the lecture's notation it has the form $N(y)\,\dfrac{dy}{dt}=M(t)$, where $N$ depends only on $y$ and $M$ only on $t$. Equivalently, $\dfrac{dy}{dt}=g(t)\,h(y)$: the right side *factors* into a $t$-part times a $y$-part. Then you integrate each side with respect to its own variable, which is why the method is called **separation of variables**. It works for many *nonlinear* equations (like $\dfrac{dy}{dt}=y^2$) where the integrating factor cannot be used. Sometimes the result is **explicit** ($y=$ a formula in $t$) and sometimes only **implicit** (an equation linking $t$ and $y$ that you cannot solve for $y$); both count as solutions.

> **Tip:** **The method (separation of variables)**
> 
> 1. **Test:** can you write $\dfrac{dy}{dt}=g(t)\,h(y)$? If the right side is a *sum* that will not factor (like $t+y$), it is not separable.
> 2. **Separate:** move all $y$'s and $dy$ to the left, all $t$'s and $dt$ to the right: $\dfrac{dy}{h(y)}=g(t)\,dt$.
> 3. **Integrate both sides** and add **one** constant $C$ (on the $t$ side).
> 4. **Fix the constant** with the initial condition, then solve for $y$ if you can (if the answer has $\pm$, the initial value picks the sign).
> 5. **Look for lost solutions:** any constant $y=c$ with $h(c)=0$ (you divided by it in step 2) is also a solution.

$$\begin{gathered}N(y)\,\frac{dy}{dt}=M(t) \\ \Downarrow \\ \int N(y)\,dy=\int M(t)\,dt+C\end{gathered}$$

> **Info:** **Calculus reminder (for Topic 2):**
> - $\displaystyle\int\frac{dy}{y}=\ln|y|+C$, and $\displaystyle\int y^{-2}dy=\frac{y^{-1}}{-1}=-\frac1y$ (power rule with $n=-2$).
> - **Exponentiating both sides:** if $\ln|y|=G(t)+C$ then $|y|=e^{G(t)+C}=e^{C}\,e^{G(t)}$ (because $e^{a+b}=e^a e^b$). Then $y=\pm e^{C}e^{G(t)}$; rename $A=\pm e^{C}$, a single constant that can be positive or negative.
> - **Log rules:** $\ln a+\ln b=\ln(ab)$, $k\ln a=\ln a^k$.

**Example: Example 6 · A first separable equation**

Solve $\dfrac{dy}{dt}=3t^2y$ with $y(0)=2$.

1. The right side is already a $t$-part times a $y$-part: $g(t)=3t^2$, $h(y)=y$. So the equation is separable.

   $$\frac{dy}{dt}=\underbrace{3t^2}_{g(t)}\cdot\underbrace{y}_{h(y)}$$
2. Separate: divide both sides by $y$ (assuming $y\neq0$ for now) and multiply by $dt$.

   $$\frac{dy}{y}=3t^2\,dt$$
3. Integrate each side with respect to its own variable: $\int dy/y=\ln|y|$ and $\int 3t^2dt=t^3$. One constant is enough.

   $$\ln|y|=t^3+C$$
4. Exponentiate both sides to undo the $\ln$, splitting $e^{t^3+C}=e^Ce^{t^3}$.

   $$|y|=e^{C}\,e^{t^3}$$
5. Drop the bars by writing $y=A\,e^{t^3}$ with $A=\pm e^C$. The value $A=0$ gives $y=0$, the solution we set aside when dividing by $y$, so $A$ may be any constant.

   $$y=A\,e^{t^3}$$
6. Use $y(0)=2$: $e^0=1$.

   $$2=A\ \Rightarrow\ y(t)=2e^{t^3}$$

**Answer:** $y(t)=2e^{t^3}$

**Example: Example 7 · Lecture RL circuit again, by separation**

Solve the RL circuit equation $\dfrac{di}{dt}+5i=50$, $i(0)=0$ (from Example 1: $100\,\mathrm{V}$, $10\,\Omega$, $2\,\mathrm{H}$) by separating variables.

1. Move $5i$ to the right: $\dfrac{di}{dt}=50-5i$. The right side depends only on $i$ (times $g(t)=1$), so it is separable as well as linear.

   $$\frac{di}{dt}=50-5i$$
2. Separate: all the $i$ on the left, all the $t$ on the right.

   $$\frac{di}{50-5i}=dt$$
3. Integrate the left side by substitution $u=50-5i$, $du=-5\,di$, so $di=-\tfrac15du$. The right side gives $t$. (Constants from both sides combine into one, $C_2$.)

   $$\int\frac{di}{50-5i}=-\frac15\int\frac{du}{u}=-\frac15\ln|50-5i|$$
4. So the integrated equation is:

   $$-\frac15\ln|50-5i|=t+C_2$$
5. Multiply by $-5$ and rename the constant $C_3=-5C_2$.

   $$\ln|50-5i|=-5t+C_3$$
6. Exponentiate both sides: $|50-5i|=e^{C_3}e^{-5t}$. Drop the bars by letting the constant carry the sign: $A=\pm e^{C_3}$ may be positive or negative.

   $$50-5i=A\,e^{-5t}$$
7. Use $i(0)=0$ now: at $t=0$, $e^0=1$ and $50-5\cdot0=A$, so $A=50$. The initial value settles the sign for us.

   $$A=50$$
8. Solve for $i$: move $5i$ to one side and divide by 5. Same answer as with the integrating factor.

   $$\begin{gathered}5i=50-50e^{-5t} \\ i(t)=10\big(1-e^{-5t}\big)\ \mathrm{A}\end{gathered}$$

**Answer:** $i(t)=10(1-e^{-5t})$ A (identical to Example 1)

**Example: Example 8 · Spiegel (i): $dy/dt=y^2/t^3$**

Find the general solution of $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$.

1. The right side is $y^2\cdot t^{-3}$, a product, so separate: divide by $y^2$ (for $y\neq0$), multiply by $dt$.

   $$\frac{dy}{y^2}=\frac{dt}{t^3}$$
2. Integrate with the power rule on both sides: $\int y^{-2}dy=\dfrac{y^{-1}}{-1}$ and $\int t^{-3}dt=\dfrac{t^{-2}}{-2}$.

   $$-\frac1y=-\frac{1}{2t^2}+C$$
3. Multiply by $-1$.

   $$\frac1y=\frac{1}{2t^2}-C$$
4. Combine over a common denominator, $\frac{1}{2t^2}-C=\frac{1-2Ct^2}{2t^2}$, then flip both sides.

   $$y=\frac{2t^2}{1-2Ct^2}$$
5. Lost solution: we divided by $y^2$, which is $0$ when $y=0$. Check $y=0$ directly: left side $0$, right side $0/t^3=0$. So $y=0$ is also a solution, and no value of $C$ produces it.

   $$y\equiv 0$$

**Answer:** $y=\dfrac{2t^2}{1-2Ct^2}$ (any constant $C$), plus the extra solution $y=0$

**Example: Example 9 · Spiegel (ii): factor first, then separate**

Solve $\dfrac{dy}{dt}=\dfrac{3t+t\,y^2}{y+t^2y}$ with $y(1)=3$.

1. It does not look separable yet. Factor $t$ out of the top and $y$ out of the bottom.

   $$\frac{dy}{dt}=\frac{t\,(3+y^2)}{y\,(1+t^2)}$$
2. Now it is a $t$-part times a $y$-part. Multiply by $\dfrac{y}{3+y^2}$ and by $dt$.

   $$\frac{y}{3+y^2}\,dy=\frac{t}{t^2+1}\,dt$$
3. Integrate each side by substitution. Left: $u=3+y^2$, $du=2y\,dy$, so $\int\frac{y\,dy}{3+y^2}=\frac12\int\frac{du}{u}$. Right: same idea with $u=t^2+1$. Both are $\tfrac12\ln$ of the bottom (both bottoms are positive, so no bars).

   $$\tfrac12\ln(3+y^2)=\tfrac12\ln(t^2+1)+c$$
4. Multiply by 2 and exponentiate; $C_1=e^{2c}$ is a positive constant.

   $$3+y^2=C_1\,(t^2+1)$$
5. Use $y(1)=3$: left side $3+9=12$, right side $C_1\cdot 2$.

   $$12=2C_1\ \Rightarrow\ C_1=6$$
6. So $y^2+3=6(t^2+1)$, i.e. $y^2=6t^2+3$. Take the square root; the **positive** root is the one with $y(1)=+3$.

   $$y(t)=\sqrt{6t^2+3}$$

**Answer:** $y^2+3=6(t^2+1)$, i.e. $y(t)=\sqrt{6t^2+3}$

**Example: Example 10 · Spiegel (iii): an implicit answer**

Solve $y\,dt+(t^3y^2+t^3)\,dy=0$.

1. This is written in *differential form* $M\,dt+N\,dy=0$. Collect $t^3$ in the $dy$ term and move the $dt$ term to the right.

   $$t^3\,(y^2+1)\,dy=-y\,dt$$
2. Separate: divide both sides by $y\,t^3$ (for $y\neq0$, $t\neq0$).

   $$\frac{y^2+1}{y}\,dy=-t^{-3}\,dt$$
3. Split the left fraction: $\dfrac{y^2+1}{y}=y+\dfrac1y$.

   $$\Big(y+\frac1y\Big)dy=-t^{-3}\,dt$$
4. Integrate: $\int y\,dy=\tfrac{y^2}{2}$, $\int\frac{dy}{y}=\ln|y|$, and $-\int t^{-3}dt=-\frac{t^{-2}}{-2}=\frac{t^{-2}}{2}$.

   $$\frac{y^2}{2}+\ln|y|=\frac{t^{-2}}{2}+C$$
5. Multiply by 2 and move the $t$ term left; $C_1=2C$.

   $$y^2+2\ln|y|-t^{-2}=C_1$$
6. **Explicit vs implicit:** we cannot isolate $y$ (it appears both as $y^2$ and inside $\ln$), so we leave the answer in this **implicit** form. It is still a full solution: every curve $y^2+2\ln|y|-t^{-2}=C_1$ satisfies the ODE. (Also $y=0$ works: then $dy=0$ and $y\,dt=0$.)

**Answer:** $y^2+2\ln|y|-t^{-2}=C_1$ (implicit), plus $y=0$

> **Warning:** **Common mistakes**
> 
> - **Losing solutions when dividing.** Dividing by $y$ (or $y^2$, or $y(1-y)$) throws away $y=0$ (or $y=1$). Always check those constants in the original ODE; in $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$, $y=0$ is a solution that no $C$ gives.
> - **Mishandling $e^{\ln|y|+C}$.** It is $e^C e^{\ln|y|}$, *not* $|y|+e^C$; and $e^C$ is positive, so after dropping the bars the constant becomes $A=\pm e^C$.
> - **Wrong square-root sign.** From $y^2=6t^2+3$ with $y(1)=3$ take $+\sqrt{\ }$; if the initial value were negative you would need $-\sqrt{\ }$.
> - **Trying to separate a sum.** $\dfrac{dy}{dt}=t+y$ is *not* separable (no way to write it as $g(t)h(y)$); use the integrating factor instead.

**Problem: Try it 6 · Pre-tutorial 3 (a)** (introductory)

Solve $\dfrac{dy}{dt}=-\dfrac{t}{y}$ with $y=2$ when $t=1$.

<details><summary>Solution</summary>

1. Multiply both sides by $y$ and by $dt$ to separate.

   $$y\,dy=-t\,dt$$
2. Integrate both sides with the power rule.

   $$\frac{y^2}{2}=-\frac{t^2}{2}+C$$
3. Multiply by 2 and move $t^2$ left; call the new constant $K=2C$.

   $$y^2+t^2=K$$
4. Use $y(1)=2$: $4+1=5$.

   $$y^2+t^2=5$$
5. This is a circle of radius $\sqrt5$. Solve for $y$, taking the **positive** root because $y(1)=2>0$. The square root needs $5-t^2>0$, so the solution lives on $-\sqrt5<t<\sqrt5$.

   $$y(t)=\sqrt{5-t^2},\quad -\sqrt5<t<\sqrt5$$

**Answer:** $y^2+t^2=5$, i.e. $y(t)=\sqrt{5-t^2}$ for $|t|<\sqrt5$

</details>

**Problem: Try it 7 · Linear, separable, both, or neither?** (introductory)

For each ODE say whether it is linear, separable, both, or neither (no need to solve):
1. $\dfrac{dy}{dt}=t^2+y$
2. $\dfrac{dy}{dt}=e^{t+y}$
3. $\dfrac{dy}{dt}=2y-6$
4. $\dfrac{dy}{dt}=t+y^2$

<details><summary>Solution</summary>

1. Tests: **linear** means $y$ appears only to the first power (no $y^2$, $e^y$, $\sqrt y$...). **Separable** means the right side factors as $g(t)\,h(y)$.
2. (1) $y$ appears to the first power, so it is linear ($y^{\prime}-y=t^2$). But $t^2+y$ is a sum that cannot be factored into $g(t)h(y)$, so it is not separable.

   $$\text{linear only}$$
3. (2) Use $e^{a+b}=e^ae^b$: $e^{t+y}=e^t\cdot e^y$, a product, so separable. $e^y$ is not first-power in $y$, so not linear.

   $$\text{separable only}$$
4. (3) $2y-6=1\cdot 2(y-3)$ is a $t$-part ($1$) times a $y$-part, so separable; and $y$ appears to the first power, so linear too.

   $$\text{both}$$
5. (4) $y^2$ makes it nonlinear, and $t+y^2$ is a sum that does not factor.

   $$\text{neither}$$

**Answer:** (1) linear only  (2) separable only  (3) both  (4) neither

</details>

**Problem: Try it 8 · Pre-tutorial 3 (b): differential form** (intermediate)

Solve $3t\,(y^2+1)\,dt+y\,(t^2+2)\,dy=0$.

<details><summary>Solution</summary>

1. Move the $dt$ term to the right.

   $$y\,(t^2+2)\,dy=-3t\,(y^2+1)\,dt$$
2. Separate: divide both sides by $(y^2+1)(t^2+2)$ (both are always positive, so nothing is lost).

   $$\frac{y}{y^2+1}\,dy=-\frac{3t}{t^2+2}\,dt$$
3. Left: substitution $u=y^2+1$, $du=2y\,dy$, gives $\tfrac12\ln(y^2+1)$. Right: $u=t^2+2$, $du=2t\,dt$, so $-3\int\frac{t\,dt}{t^2+2}=-\tfrac32\ln(t^2+2)$.

   $$\tfrac12\ln(y^2+1)=-\tfrac32\ln(t^2+2)+c$$
4. Multiply by 2 and bring the log to the left using $\ln a+3\ln b=\ln(ab^3)$.

   $$\ln\!\big[(y^2+1)(t^2+2)^3\big]=2c$$
5. Exponentiate; $K=e^{2c}$ is a positive constant. This implicit form is a fine final answer (solving gives $y=\pm\sqrt{K/(t^2+2)^3-1}$).

   $$(y^2+1)(t^2+2)^3=K$$

**Answer:** $(y^2+1)(t^2+2)^3=K$ (implicit; $K>0$ constant)

</details>

**Problem: Try it 9 · Pre-tutorial 3 (c): separable and linear** (intermediate)

Find the general solution of $\dfrac{dy}{dt}=8ty+3y$, (1) by separation and (2) by the integrating factor.

<details><summary>Solution</summary>

1. (1) Factor out $y$: the right side is $(8t+3)\,y$, a $t$-part times a $y$-part. Separate (for $y\neq0$).

   $$\frac{dy}{y}=(8t+3)\,dt$$
2. Integrate: $\ln|y|=4t^2+3t+C$ (power rule: $\int 8t\,dt=4t^2$).

   $$\ln|y|=4t^2+3t+C$$
3. Exponentiate and set $A=\pm e^C$; $A=0$ restores the lost solution $y=0$.

   $$y=A\,e^{4t^2+3t}$$
4. (2) Standard form: $\dfrac{dy}{dt}-(8t+3)y=0$, so $a=-(8t+3)$ and $\int a\,dt=-(4t^2+3t)$.

   $$\mu=e^{-(4t^2+3t)}$$
5. Multiply and collapse; the right side is $0$, so the bracket is a constant.

   $$\begin{gathered}\frac{d}{dt}\Big[y\,e^{-(4t^2+3t)}\Big]=0 \\ y\,e^{-(4t^2+3t)}=A\end{gathered}$$
6. Multiply by $e^{4t^2+3t}$: the same answer, and this route never divides by $y$, so nothing is lost.

   $$y=A\,e^{4t^2+3t}$$

**Answer:** $y(t)=A\,e^{4t^2+3t}$ ($A$ any constant, including $0$)

</details>

**Problem: Try it 10 · Logistic growth: partial fractions** (advanced)

Solve $\dfrac{dy}{dt}=y(1-y)$ with $y(0)=\tfrac12$. Also list the constant solutions.

<details><summary>Solution</summary>

1. Separate (for $y\neq0,1$).

   $$\frac{dy}{y(1-y)}=dt$$
2. Split the left fraction with *partial fractions*: $\dfrac{1}{y(1-y)}=\dfrac{1}{y}+\dfrac{1}{1-y}$ (check: the common denominator gives $\frac{(1-y)+y}{y(1-y)}$).

   $$\Big(\frac1y+\frac{1}{1-y}\Big)dy=dt$$
3. Integrate: $\int\frac{dy}{y}=\ln|y|$; for the second use $u=1-y$, $du=-dy$, giving $-\ln|1-y|$. Combine with $\ln a-\ln b=\ln\frac ab$.

   $$\ln\Big|\frac{y}{1-y}\Big|=t+C$$
4. Exponentiate; $A=\pm e^C$.

   $$\frac{y}{1-y}=A\,e^{t}$$
5. Use $y(0)=\tfrac12$: $\dfrac{1/2}{1/2}=1=A$.

   $$\frac{y}{1-y}=e^{t}$$
6. Solve for $y$: $y=e^t-e^ty$, so $y(1+e^t)=e^t$. Divide, then divide top and bottom by $e^t$.

   $$y(t)=\frac{e^t}{1+e^t}=\frac{1}{1+e^{-t}}$$
7. Constant solutions: the values we divided out, $y=0$ and $y=1$, both make $y(1-y)=0$, so they solve the ODE.

   $$y\equiv0,\quad y\equiv1$$

**Answer:** $y(t)=\dfrac{1}{1+e^{-t}}$; constant solutions $y=0$ and $y=1$

</details>

## Topic 3: Existence and uniqueness

Before solving an initial value problem (IVP: an ODE plus a starting value $y(t_0)=y_0$), it is fair to ask two questions: **does a solution exist**, and **is there only one**? For a circuit this is the question "does the model predict one definite response?". The theorem below answers both for $\dfrac{dy}{dt}=F(t,y)$ by checking two smoothness conditions on the right side $F$. In pictures: where the conditions hold, exactly one solution curve passes through each point, so **solution curves never cross or touch** there. The theorem is only a *sufficient* condition: when its conditions fail it says nothing (there might be no solution, one, or many), and it only promises a solution *near* $t_0$, not for all time.

> **Tip:** **The method**
> 
> *General ODE $\dfrac{dy}{dt}=F(t,y)$:*
> 1. Solve for $\dfrac{dy}{dt}$ to identify $F(t,y)$.
> 2. Compute $\dfrac{\partial F}{\partial y}$ (differentiate with respect to $y$, treating $t$ as a constant).
> 3. Find where $F$ and $\dfrac{\partial F}{\partial y}$ are continuous. Trouble spots: division by zero, $\ln$ of a non-positive number, even roots of negatives, fractional powers like $y^{-2/3}$ at $y=0$.
> 4. If the starting point $(t_0,y_0)$ is inside a region where both are continuous: exactly one solution through it. Otherwise: the theorem is silent.
> 
> *Linear ODE:*
> 1. Divide to standard form $\dfrac{dy}{dt}+a(t)y=f(t)$.
> 2. List the $t$-values where $a(t)$ or $f(t)$ is not continuous; they cut the $t$-axis into intervals.
> 3. The answer is the one interval that contains $t_0$.

$$\begin{gathered}\frac{dy}{dt}=F(t,y),\quad y(t_0)=y_0 \\ F\ \text{and}\ \frac{\partial F}{\partial y}\ \text{continuous near the start} \\ \Downarrow \\ \text{exactly one solution near } t_0\end{gathered}$$

**Linear version.** If $a(t)$ and $f(t)$ in $\dfrac{dy}{dt}+a(t)\,y=f(t)$ are continuous on an open interval $I$ containing $t_0$, then the IVP has exactly one solution, and it exists on **the whole interval $I$** (no blow-ups inside). This is stronger than the general theorem, which only promises a solution for a short while around $t_0$. You can see why from the integrating-factor formula: every step only needs $a$ and $f$ to be integrable.

> **Info:** **Calculus reminder: partial derivative.** $\dfrac{\partial F}{\partial y}$ ("partial F partial y") means: differentiate $F(t,y)$ with respect to $y$ while treating $t$ as a fixed number. Example: $F=t\,y^2+\sin t$ gives $\dfrac{\partial F}{\partial y}=2t\,y$ (the $\sin t$ is a constant, so its derivative is $0$). For a quotient use the quotient rule $\Big(\dfrac{u}{v}\Big)'=\dfrac{u'v-u\,v'}{v^2}$.

**Example: Example 11 · Conditions hold everywhere**

Does $\dfrac{dy}{dt}=t\,y+\sin t$ have exactly one solution through every starting point $(t_0,y_0)$?

1. Identify the right side.

   $$F(t,y)=t\,y+\sin t$$
2. Differentiate with respect to $y$, treating $t$ as a constant: $\frac{\partial}{\partial y}(ty)=t$ and $\frac{\partial}{\partial y}\sin t=0$.

   $$\frac{\partial F}{\partial y}=t$$
3. Both $ty+\sin t$ and $t$ are built from polynomials and $\sin$, which are continuous everywhere: no division, no roots, no logs.
4. So the conditions hold in the whole $ty$-plane and every IVP has exactly one solution. (The equation is also linear with $a(t)=-t$ and $f(t)=\sin t$ continuous for all $t$, so each solution exists for all $t$.)

**Answer:** Yes: $F$ and $\partial F/\partial y=t$ are continuous everywhere, so every IVP has exactly one solution.

**Example: Example 12 · Where is uniqueness guaranteed?**

For $\dfrac{dy}{dt}=\dfrac{t+y}{t-y}$, find where the theorem guarantees a unique solution. Is it guaranteed for $y(0)=1$? For $y(2)=2$?

1. $F=\dfrac{t+y}{t-y}$ is continuous except where its denominator is zero, i.e. on the line $y=t$.

   $$F(t,y)=\frac{t+y}{t-y},\quad t-y\neq0$$
2. Quotient rule in $y$: $u=t+y$ ($u_y=1$), $v=t-y$ ($v_y=-1$).

   $$\begin{aligned}\frac{\partial F}{\partial y}&=\frac{1\cdot(t-y)-(t+y)(-1)}{(t-y)^2} \\ &=\frac{2t}{(t-y)^2}\end{aligned}$$
3. $\dfrac{\partial F}{\partial y}$ has the same bad set: the line $y=t$. So both conditions hold at every point **off** the line $y=t$.
4. $y(0)=1$ is the point $(0,1)$: $t-y=-1\neq0$, so exactly one solution passes through it.

   $$(0,1):\ \text{guaranteed}$$
5. $y(2)=2$ is the point $(2,2)$, which lies on $y=t$; $F$ is not even defined there, so the theorem says nothing.

   $$(2,2):\ \text{no guarantee}$$

**Answer:** Unique solution guaranteed through every point with $y\neq t$; yes for $y(0)=1$; no guarantee for $y(2)=2$.

**Example: Example 13 · Two solutions: $dy/dt=y^{1/3}$, $y(0)=0$**

Show that $\dfrac{dy}{dt}=y^{1/3}$ with $y(0)=0$ has (at least) two different solutions, and explain why this does not contradict the theorem.

1. Check the conditions. $F=y^{1/3}$ (the cube root) is continuous everywhere, but its $y$-derivative has $y$ in a denominator.

   $$\frac{\partial F}{\partial y}=\frac13y^{-2/3}=\frac{1}{3\,y^{2/3}}$$
2. At $y=0$ this is $\tfrac10$: not continuous. Our starting point $(0,0)$ is on the line $y=0$, so the theorem gives **no** guarantee here.
3. Solution 1: the constant $y=0$. Its derivative is $0$ and $0^{1/3}=0$, so it works, and $y(0)=0$.

   $$y_1(t)=0$$
4. Solution 2: separate (for $y>0$): $y^{-1/3}dy=dt$. Power rule: $\int y^{-1/3}dy=\dfrac{y^{2/3}}{2/3}=\tfrac32y^{2/3}$.

   $$\tfrac32\,y^{2/3}=t+C$$
5. Use $y(0)=0$: $C=0$. Then $y^{2/3}=\tfrac{2t}{3}$; raise both sides to the power $\tfrac32$.

   $$y_2(t)=\Big(\frac{2t}{3}\Big)^{3/2},\quad t\ge0$$
6. Check $y_2$: by the chain rule $y_2^{\prime}=\tfrac32\big(\tfrac{2t}{3}\big)^{1/2}\cdot\tfrac23=\big(\tfrac{2t}{3}\big)^{1/2}$, and $y_2^{1/3}=\big(\tfrac{2t}{3}\big)^{1/2}$. Equal, so it solves the ODE.
7. Two different curves leave the same point $(0,0)$, so uniqueness fails exactly where the theorem warned us ($\partial F/\partial y$ blows up). No contradiction: the theorem only promises uniqueness when its conditions hold.

**Answer:** $y=0$ and $y=(2t/3)^{3/2}$ ($t\ge0$) both solve the IVP; allowed because $\partial F/\partial y=\tfrac13y^{-2/3}$ is not continuous at $y=0$.

![Example 13 as a picture: from the same starting point $(0,0)$ the blue curve, the orange line $y=0$, and every grey curve (sit at 0 for a while, then lift off) all solve $dy/dt=y^{1/3}$. Uniqueness fails exactly where $\partial F/\partial y=\tfrac13y^{-2/3}$ blows up: at $y=0$.](/figures/elec231/w3_cube_root.svg)

*Example 13 as a picture: from the same starting point $(0,0)$ the blue curve, the orange line $y=0$, and every grey curve (sit at 0 for a while, then lift off) all solve $dy/dt=y^{1/3}$. Uniqueness fails exactly where $\partial F/\partial y=\tfrac13y^{-2/3}$ blows up: at $y=0$.*

**Example: Example 14 · Blow-up: $dy/dt=y^2$, $y(0)=1$**

Solve $\dfrac{dy}{dt}=y^2$, $y(0)=1$, and find the interval on which the solution exists.

1. Conditions: $F=y^2$ and $\dfrac{\partial F}{\partial y}=2y$ are continuous everywhere, so there is exactly one solution.

   $$F=y^2,\quad \frac{\partial F}{\partial y}=2y$$
2. Separate and integrate: $\int y^{-2}dy=-y^{-1}$ and $\int dt=t$.

   $$\frac{dy}{y^2}=dt\ \Rightarrow\ -\frac1y=t+C$$
3. Use $y(0)=1$: $-1=0+C$, so $C=-1$.

   $$-\frac1y=t-1$$
4. Solve for $y$: flip both sides and change sign.

   $$y(t)=\frac{1}{1-t}$$
5. As $t\to1$ from below, the denominator $\to0^+$ and $y\to+\infty$: the solution **blows up** in finite time, so it exists only for $t<1$. The theorem was right (one solution) but only promised it near $t_0=0$.

   $$\text{exists on } -\infty<t<1$$

**Answer:** $y(t)=\dfrac{1}{1-t}$, which exists only on $-\infty<t<1$ (it blows up at $t=1$)

![Example 14: $y=1/(1-t)$ starts at 1 and reaches infinity at $t=1$. The theorem only promises a solution near the starting point, and this is why: even with nice $F=y^2$, the solution can run off to infinity.](/figures/elec231/w3_blowup.svg)

*Example 14: $y=1/(1-t)$ starts at 1 and reaches infinity at $t=1$. The theorem only promises a solution near the starting point, and this is why: even with nice $F=y^2$, the solution can run off to infinity.*

**Example: Example 15 · Largest interval for a linear IVP**

Without solving, find the largest interval on which $(t-3)\dfrac{dy}{dt}+(\ln t)\,y=2t$, $y(1)=2$, is guaranteed to have a unique solution.

1. Divide by $t-3$ to reach standard form (this division is exactly what creates a trouble spot at $t=3$).

   $$\frac{dy}{dt}+\frac{\ln t}{t-3}\,y=\frac{2t}{t-3}$$
2. Read off the coefficient and forcing.

   $$\begin{gathered}a(t)=\frac{\ln t}{t-3} \\ f(t)=\frac{2t}{t-3}\end{gathered}$$
3. Trouble spots: $\ln t$ needs $t>0$; dividing by $t-3$ needs $t\neq3$. So $a$ and $f$ are both continuous on $0<t<3$ and on $t>3$.

   $$(0,3)\quad\text{and}\quad(3,\infty)$$
4. The starting time is $t_0=1$, which lies in $(0,3)$. That whole interval is the answer.

   $$0<t<3$$

**Answer:** $0<t<3$

> **Warning:** **Common mistakes**
> 
> - **"The conditions fail, so there is no solution."** Wrong: the theorem is only *sufficient*. When it fails it is silent; $\dfrac{dy}{dt}=y^{1/3}$, $y(0)=0$ has two solutions, not zero.
> - **Checking only $F$.** You must also check $\dfrac{\partial F}{\partial y}$; $y^{1/3}$ is continuous but its $y$-derivative is not.
> - **Reading $a(t)$ before standard form.** In $(t-3)y^{\prime}+(\ln t)y=2t$ the break at $t=3$ only shows up after dividing by $t-3$.
> - **Giving a union of intervals.** The answer is the *single* interval containing $t_0$, e.g. $0<t<3$, not "$t>0,\ t\neq3$".

**Problem: Try it 11 · Check the conditions** (introductory)

Does the theorem guarantee exactly one solution of $\dfrac{dy}{dt}=\dfrac{y}{t}$ with $y(2)=1$? Then find it.

<details><summary>Solution</summary>

1. Identify $F$ and differentiate in $y$ ($t$ is a constant).

   $$\begin{gathered}F=\frac yt \\ \frac{\partial F}{\partial y}=\frac1t\end{gathered}$$
2. Both are continuous wherever $t\neq0$. The starting point $(2,1)$ has $t=2\neq0$, so yes: exactly one solution.
3. Solve by separation: $\dfrac{dy}{y}=\dfrac{dt}{t}$, so $\ln|y|=\ln|t|+C$, and exponentiating gives $y=At$.

   $$y=A\,t$$
4. Use $y(2)=1$: $1=2A$, so $A=\tfrac12$.

   $$y(t)=\frac t2$$

**Answer:** Yes (guaranteed since $t_0=2\neq0$); $y(t)=t/2$

</details>

**Problem: Try it 12 · Non-uniqueness with $\sqrt{y}$** (intermediate)

Consider $\dfrac{dy}{dt}=\sqrt{y}$ for $y\ge0$.
1. Where does the theorem guarantee a unique solution?
2. Show that $y(0)=0$ has two solutions: $y=0$ and $y=t^2/4$ (for $t\ge0$).

<details><summary>Solution</summary>

1. $F=\sqrt y=y^{1/2}$ is continuous for $y\ge0$. Its $y$-derivative (power rule) is $\tfrac12y^{-1/2}$.

   $$\frac{\partial F}{\partial y}=\frac{1}{2\sqrt y}$$
2. This is undefined at $y=0$, so both conditions hold only for $y>0$: every starting point above the $t$-axis has exactly one solution.

   $$\text{guaranteed for } y_0>0$$
3. Check $y=0$: derivative $0$, and $\sqrt0=0$. Works, with $y(0)=0$.
4. Check $y=t^2/4$: derivative $t/2$; and $\sqrt{t^2/4}=t/2$ for $t\ge0$. Works, and $y(0)=0$.

   $$\frac{d}{dt}\frac{t^2}{4}=\frac t2=\sqrt{\frac{t^2}{4}}$$
5. Two solutions through $(0,0)$; this is possible because $(0,0)$ is on the line $y=0$ where $\partial F/\partial y$ is not continuous.

**Answer:** (1) for every starting point with $y_0>0$  (2) both functions satisfy the ODE and $y(0)=0$, so the IVP is not unique

</details>

**Problem: Try it 13 · Largest intervals: three starting times** (intermediate)

For $(t^2-9)\,\dfrac{dy}{dt}+t\,y=\ln(t+5)$, find the largest interval on which a unique solution is guaranteed when the initial condition is
1. $y(0)=1$
2. $y(-4)=0$
3. $y(5)=2$

<details><summary>Solution</summary>

1. Divide by $t^2-9$ to reach standard form.

   $$\begin{gathered}a(t)=\frac{t}{t^2-9} \\ f(t)=\frac{\ln(t+5)}{t^2-9}\end{gathered}$$
2. Trouble spots: $t^2-9=0$ at $t=\pm3$; and $\ln(t+5)$ needs $t+5>0$, i.e. $t>-5$.

   $$t>-5,\quad t\neq-3,\quad t\neq3$$
3. These cut the allowed $t$-axis into three intervals.

   $$(-5,-3),\quad(-3,3),\quad(3,\infty)$$
4. Pick the interval containing each $t_0$: $0\in(-3,3)$, $-4\in(-5,-3)$, $5\in(3,\infty)$.

**Answer:** (1) $-3<t<3$  (2) $-5<t<-3$  (3) $t>3$

</details>

**Problem: Try it 14 · Blow-up time depends on the start** (advanced)

Solve $\dfrac{dy}{dt}=y^2$ with $y(0)=y_0$, where $y_0>0$. On what interval does the solution exist? Compare $y_0=2$ with $y_0=\tfrac12$. What happens if $y_0=0$?

<details><summary>Solution</summary>

1. Separate and integrate as in Example 14: $-\dfrac1y=t+C$.

   $$-\frac1y=t+C$$
2. At $t=0$: $-\dfrac{1}{y_0}=C$.

   $$-\frac1y=t-\frac1{y_0}=\frac{y_0t-1}{y_0}$$
3. Flip and change sign.

   $$y(t)=\frac{y_0}{1-y_0t}$$
4. The denominator hits $0$ at $t=1/y_0$, where $y\to\infty$. So the solution exists for $t<1/y_0$.

   $$-\infty<t<\frac{1}{y_0}$$
5. $y_0=2$: blows up at $t=\tfrac12$. $y_0=\tfrac12$: blows up at $t=2$. A bigger start blows up sooner.
6. $y_0=0$: the constant $y=0$ solves the ODE and, by uniqueness ($F$ and $2y$ are continuous), it is the only solution; it exists for all $t$.

**Answer:** $y(t)=\dfrac{y_0}{1-y_0t}$ on $t<1/y_0$ (blow-up at $t=\tfrac12$ for $y_0=2$, at $t=2$ for $y_0=\tfrac12$); $y_0=0$ gives $y=0$ for all $t$

</details>

**Problem: Try it 15 · Sufficient, not necessary** (advanced)

The ODEs below have $a(t)=\pm1/t$, which is not continuous at $t=0$, so the theorem says nothing about starting at $t_0=0$. Show that all three outcomes really happen:
1. $t\,\dfrac{dy}{dt}+y=0$, $y(0)=0$: exactly one solution.
2. $t\,\dfrac{dy}{dt}+y=0$, $y(0)=1$: no solution.
3. $t\,\dfrac{dy}{dt}-y=0$, $y(0)=0$: infinitely many solutions.

<details><summary>Solution</summary>

1. For 1 and 2, the left side is a product-rule derivative: $\dfrac{d}{dt}[t\,y]=y+t\dfrac{dy}{dt}$. So the ODE says $t\,y$ is constant.

   $$\frac{d}{dt}[t\,y]=0\ \Rightarrow\ t\,y=C$$
2. Any solution defined at $t=0$ must satisfy $t\,y=C$ there too: $0\cdot y(0)=C$, so $C=0$. Then $t\,y=0$, so $y=0$ for every $t\neq0$.

   $$C=0\ \Rightarrow\ y(t)=0\ (t\neq0)$$
3. Part 1: $y\equiv0$ satisfies $y(0)=0$, and it is the only possibility, so there is exactly one solution.

   $$y\equiv0$$
4. Part 2: the only candidate is $y=0$ for $t\neq0$, and a solution must be continuous, so $y(0)$ would have to be $0$, not $1$. No solution exists.
5. Part 3: separate, $\dfrac{dy}{y}=\dfrac{dt}{t}$, giving $y=c\,t$. Check: $t\cdot c-c\,t=0$. Every line $y=ct$ passes through $(0,0)$, so every value of $c$ gives a solution.

   $$y=c\,t\quad(\text{any } c)$$
6. Lesson: when the conditions fail you can get one, none or infinitely many solutions; the theorem is silent, not negative.

**Answer:** (1) only $y=0$  (2) none  (3) $y=ct$ for every constant $c$

</details>

## Mixed practice (exam style)

Mixed topics, like the midterm. Try each one before opening the solution.

**Problem: Practice 1 · Separable with a log answer** (introductory)

Solve $e^{y}\,\dfrac{dy}{dt}=2t$ with $y(0)=0$.

<details><summary>Solution</summary>

1. Separable: multiply by $dt$.

   $$e^{y}\,dy=2t\,dt$$
2. Integrate: $\int e^ydy=e^y$, $\int2t\,dt=t^2$.

   $$e^{y}=t^2+C$$
3. Use $y(0)=0$: $e^0=1=0+C$.

   $$e^{y}=t^2+1$$
4. Take $\ln$ of both sides ($\ln e^y=y$). Since $t^2+1>0$ this works for all $t$.

   $$y(t)=\ln(t^2+1)$$

**Answer:** $y(t)=\ln(t^2+1)$

</details>

**Problem: Practice 2 · One equation, two methods** (introductory)

Solve $\dfrac{dy}{dt}=2y+4$, $y(0)=1$:
1. by separation of variables;
2. by the integrating factor.

<details><summary>Solution</summary>

1. (1) Separate (for $2y+4\neq0$).

   $$\frac{dy}{2y+4}=dt$$
2. Integrate the left by substitution $u=2y+4$, $du=2\,dy$: $\int\frac{dy}{2y+4}=\tfrac12\ln|2y+4|$.

   $$\tfrac12\ln|2y+4|=t+C$$
3. Multiply by 2 and exponentiate; $A=\pm e^{2C}$.

   $$2y+4=A\,e^{2t}$$
4. Use $y(0)=1$: $6=A$. Solve for $y$.

   $$y=3e^{2t}-2$$
5. (2) Standard form: $\dfrac{dy}{dt}-2y=4$, so $a=-2$ and $\mu=e^{-2t}$.

   $$\frac{d}{dt}\big[y\,e^{-2t}\big]=4e^{-2t}$$
6. Integrate: $\int4e^{-2t}dt=-2e^{-2t}$.

   $$y\,e^{-2t}=-2e^{-2t}+C$$
7. Divide by $e^{-2t}$ and use $y(0)=1$: $1=-2+C$, $C=3$. Same answer.

   $$y=3e^{2t}-2$$

**Answer:** $y(t)=3e^{2t}-2$ (both methods)

</details>

**Problem: Practice 3 · Pick the right square root** (intermediate)

Solve $\dfrac{dy}{dt}=\dfrac{t\,e^{t^2}}{y}$ with $y(0)=-2$. Give $y$ explicitly.

<details><summary>Solution</summary>

1. Separate: multiply by $y$ and $dt$.

   $$y\,dy=t\,e^{t^2}dt$$
2. Right side by substitution $u=t^2$, $du=2t\,dt$: $\int te^{t^2}dt=\tfrac12\int e^udu=\tfrac12e^{t^2}$. Left: $\tfrac{y^2}{2}$.

   $$\frac{y^2}{2}=\frac12e^{t^2}+C$$
3. Use $y(0)=-2$: $\tfrac42=\tfrac12+C$, so $C=\tfrac32$.

   $$y^2=e^{t^2}+3$$
4. Take the square root. The initial value is **negative**, so choose the minus sign (check: $-\sqrt{1+3}=-2$).

   $$y(t)=-\sqrt{e^{t^2}+3}$$

**Answer:** $y(t)=-\sqrt{e^{t^2}+3}$

</details>

**Problem: Practice 4 · RL circuit with a decaying source** (intermediate)

A source $v_s(t)=10e^{-t}\,\mathrm{V}$, a switch, a $2\,\Omega$ resistor and a $1\,\mathrm{H}$ inductor are in series. The switch closes at $t=0$ and $i(0)=0$.

```schematic
V1 0,3 -> 0,0 "$10e^{-t}\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$2\,\Omega$"
L1 6,3 -> 6,0 "$1\,\mathrm{H}$" i="$i$"
wire 6,0 -> 0,0
ground 0,0
```

1. Write the ODE for $i(t)$.
2. Solve it.
3. When is the current largest, and what is the maximum current?

<details><summary>Solution</summary>

1. KVL: $L\dfrac{di}{dt}+Ri=v_s$ with $L=1$, $R=2$. Already in standard form.

   $$\frac{di}{dt}+2i=10e^{-t}$$
2. Integrating factor $e^{2t}$. Multiply; on the right $e^{-t}e^{2t}=e^{t}$.

   $$\frac{d}{dt}\big[i\,e^{2t}\big]=10\,e^{t}$$
3. Integrate: $\int10e^tdt=10e^t$.

   $$i\,e^{2t}=10e^{t}+C$$
4. Divide by $e^{2t}$, then use $i(0)=0$: $0=10+C$, $C=-10$.

   $$i(t)=10\big(e^{-t}-e^{-2t}\big)\ \mathrm{A}$$
5. Part 3: the maximum is where $\dfrac{di}{dt}=0$.

   $$\frac{di}{dt}=10\big(-e^{-t}+2e^{-2t}\big)=0$$
6. Divide by $e^{-2t}$: $-e^{t}+2=0$, so $e^t=2$ and $t=\ln2$.

   $$t=\ln2\approx0.693\ \mathrm{s}$$
7. Substitute: $e^{-\ln2}=\tfrac12$ and $e^{-2\ln2}=\tfrac14$.

   $$i_{\max}=10\Big(\frac12-\frac14\Big)=2.5\ \mathrm{A}$$

**Answer:** (1) $\dfrac{di}{dt}+2i=10e^{-t}$  (2) $i(t)=10(e^{-t}-e^{-2t})$ A  (3) at $t=\ln2\approx0.693$ s, $i_{\max}=2.5$ A

</details>

**Problem: Practice 5 · Interval first, then solve** (intermediate)

Consider $(t+1)\,\dfrac{dy}{dt}+y=4t$, $y(1)=2$.
1. Find the largest interval on which a unique solution is guaranteed.
2. Solve the IVP.
3. What happens to $y$ as $t$ approaches the left end of that interval?

<details><summary>Solution</summary>

1. Standard form: divide by $t+1$.

   $$\begin{gathered}a(t)=\frac{1}{t+1} \\ f(t)=\frac{4t}{t+1}\end{gathered}$$
2. Both are continuous except at $t=-1$. The interval containing $t_0=1$ is $(-1,\infty)$.

   $$-1<t<\infty$$
3. Integrating factor: $\int\frac{dt}{t+1}=\ln(t+1)$ (positive on our interval), so $\mu=t+1$. Multiplying the standard form by $t+1$ just gives back the original, whose left side is the product-rule derivative of $(t+1)y$.

   $$\frac{d}{dt}\big[(t+1)\,y\big]=4t$$
4. Integrate: $\int4t\,dt=2t^2$.

   $$(t+1)\,y=2t^2+C$$
5. Use $y(1)=2$: $2\cdot2=2+C$, so $C=2$. Divide by $t+1$.

   $$y(t)=\frac{2t^2+2}{t+1}$$
6. As $t\to-1^+$: numerator $\to4$, denominator $\to0^+$, so $y\to+\infty$. The solution really cannot be continued past $t=-1$.

   $$y\to+\infty$$

**Answer:** (1) $-1<t<\infty$  (2) $y(t)=\dfrac{2(t^2+1)}{t+1}$  (3) $y\to+\infty$ as $t\to-1^+$

</details>

**Problem: Practice 6 · Uniqueness can fail** (advanced)

Consider $\dfrac{dy}{dt}=(y-1)^{2/3}$.
1. Compute $\dfrac{\partial F}{\partial y}$ and say where the theorem guarantees a unique solution.
2. Show that $y=1$ and $y=1+\dfrac{t^3}{27}$ both satisfy the ODE and $y(0)=1$.
3. Does this contradict the theorem?

<details><summary>Solution</summary>

1. Power rule (chain rule factor is $1$): $\dfrac{\partial}{\partial y}(y-1)^{2/3}=\tfrac23(y-1)^{-1/3}$.

   $$\frac{\partial F}{\partial y}=\frac{2}{3\,(y-1)^{1/3}}$$
2. $F$ is continuous everywhere, but $\partial F/\partial y$ is undefined when $y=1$. So uniqueness is guaranteed through every point with $y_0\neq1$.

   $$y_0\neq1$$
3. $y=1$: derivative $0$, and $(1-1)^{2/3}=0$. Works, and $y(0)=1$.
4. $y=1+t^3/27$: derivative $\tfrac{3t^2}{27}=\tfrac{t^2}{9}$. And $y-1=\tfrac{t^3}{27}=\big(\tfrac t3\big)^3$, so $(y-1)^{2/3}=\big(\tfrac t3\big)^2=\tfrac{t^2}{9}$. Works, and $y(0)=1$.

   $$\frac{d}{dt}\Big(1+\frac{t^3}{27}\Big)=\frac{t^2}{9}=\Big(\frac{t^3}{27}\Big)^{2/3}$$
5. No contradiction: the starting point $(0,1)$ lies on $y=1$, where $\partial F/\partial y$ is not continuous, so the theorem made no promise there.

**Answer:** (1) $\partial F/\partial y=\tfrac23(y-1)^{-1/3}$; unique for $y_0\neq1$  (2) both check  (3) no: the condition fails at $y=1$

</details>

## Summary

| Problem type | How to recognise it | What to do |
|---|---|---|
| Linear first-order | $y$ and $y^{\prime}$ only to the first power; rearranges to $y^{\prime}+a(t)y=f(t)$ | Standard form, $\mu=e^{\int a\,dt}$, $\frac{d}{dt}[\mu y]=\mu f$, integrate, $+C$, divide by $\mu$, use the IC |
| Separable | Right side factors as $g(t)\,h(y)$ (or given as $N(y)\,y^{\prime}=M(t)$) | Separate, integrate both sides, one $+C$, use the IC, solve for $y$ (pick the root sign from the IC) |
| Both | e.g. $y^{\prime}=ay+b$ with constants, or $y^{\prime}=g(t)\,y$ | Either method; the integrating factor never loses solutions |
| Lost solutions | You divided by $h(y)$ | Check each constant $y=c$ with $h(c)=0$ in the original ODE |
| Implicit answer | You cannot isolate $y$ (e.g. $y^2+2\ln|y|=\ldots$) | Leave it as $G(t,y)=C$ and fix $C$ with the IC |
| Existence and uniqueness | "Is there exactly one solution through $(t_0,y_0)$?" | Check $F$ and $\partial F/\partial y$ are continuous near the point; if not, the theorem is silent |
| Largest interval (linear IVP) | "On what interval is the solution guaranteed?" | Standard form; mark where $a(t)$ or $f(t)$ break; take the interval containing $t_0$ |

| Formula or fact | Meaning |
|---|---|
| $\mu(t)=e^{\int a(t)\,dt}$ | Integrating factor for $y^{\prime}+a(t)y=f(t)$ (no $+C$ needed) |
| $y=\frac{1}{\mu}\left[\int\mu f\,dt+C\right]$ | General solution of the linear ODE |
| $\int N(y)\,dy=\int M(t)\,dt+C$ | Solution of the separable ODE $N(y)\,y^{\prime}=M(t)$ |
| $\int\frac{du}{u}=\ln|u|$, $e^{k\ln u}=u^k$ | The two facts behind most integrating factors |
| $\int u\,dv=uv-\int v\,du$ | Integration by parts, for forcing like $t\,e^{kt}$ |
| $\tau=L/R$ (RL), $\tau=RC$ (RC) | Time constant: 63% of the change after one $\tau$, essentially done after $5\tau$ |
