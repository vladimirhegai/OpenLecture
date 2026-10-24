# Test 2 - Question 2

**Lectures 9–11.** Continuous random variables, probability density functions (PDFs), probability calculations, and the uniform, exponential, Gaussian and mixed cases.

## Topic 1: PDFs, CDFs and probability as area

Some random quantities (time, voltage, temperature, error) can take **any** value in an interval, not just a list.

Such an $X$ is **continuous**: probability lives on **intervals**, not on single points.

- **Single points have probability 0.** Pick a number uniformly from $[0,1]$: $P(X=0.3)=0$. It is possible, just "infinitely thin".
- So the CDF $F_X(x)=P(X\le x)$ has **no jumps**: it is a continuous curve rising from $0$ to $1$.
- The **PDF** $f_X(x)$ is a **density** (like kg/m along a bar). It is **not** a probability. Integrate it to get one.

$$P(a<X\le b)=\int_a^b f_X(x)\,dx=\text{area under } f_X \text{ from } a \text{ to } b$$

**The rules of a PDF** (memorise, no formula sheet):

- **Never negative:** $f_X(x)\ge0$ (it *can* be bigger than 1).
- **Total area 1:** $\displaystyle\int_{-\infty}^{\infty}f_X(x)\,dx=1$. Use this to find an unknown constant $c$.
- **PDF → CDF:** $F_X(x)=\displaystyle\int_{-\infty}^{x}f_X(t)\,dt$ (area to the left of $x$).
- **CDF → PDF:** $f_X(x)=\dfrac{d}{dx}F_X(x)$ (slope of the CDF).
- **Endpoints don’t matter:** $P(a<X<b)=P(a\le X\le b)$, because $P(X=a)=0$.
- **Right tail:** $P(X>a)=1-F_X(a)$.

> **Reminder:** **Calculus you need here**
> 
> - **Power rule:** $\displaystyle\int x^n\,dx=\frac{x^{n+1}}{n+1}$, e.g. $\displaystyle\int x^2\,dx=\frac{x^3}{3}$, $\displaystyle\int 1\,dx=x$.
> - **Exponential:** $\displaystyle\int e^{-\lambda x}\,dx=-\frac{1}{\lambda}e^{-\lambda x}$, and $e^{-\lambda x}\to0$ as $x\to\infty$.
> - **Definite integral:** $\displaystyle\int_a^b f(x)\,dx=G(b)-G(a)$, where $G$ is the antiderivative.
> - **Piecewise $f$:** split the integral at every break point. Pieces where $f=0$ add nothing.
> - **Derivatives** (CDF → PDF): $\dfrac{d}{dx}x^n=nx^{n-1}$, $\dfrac{d}{dx}e^{-\lambda x}=-\lambda e^{-\lambda x}$, constants → $0$.

**How to solve a "given a PDF" question:**

1. **Sketch** $f_X$: where is it non-zero? This tells you the limits.
2. **Constant:** set the total area equal to 1.
3. **CDF:** integrate from the left end up to $x$, one piece at a time (0 before the start, 1 after the end).
4. **Probabilities:** area between the limits, or $F_X(b)-F_X(a)$.

Drag $a$ and $b$: the shaded area **is** the probability. Here $F_X(x)=x^2/4$ on $[0,2]$.

```graph
title "Probability = shaded area under the PDF $f_X(x)=x/2$ on $[0,2]$"
x -0.5 2.5 label="$x$" height=250
y 0 1.2 label="$f_X(x)$"
slider A -0.5 2.5 0.5 step=0.05 label="$a$"
slider B -0.5 2.5 1.5 step=0.05 label="$b$"
curve "0" from=-0.5 to=0 color=1
curve "x/2" from=0 to=2 color=1 label="$f_X(x)$"
curve "0" from=2 to=2.5 color=1
segment "2" "0" "2" "1" color=1 dash
region "(x>A)*(x<B)*(y>0)*(y<(x>0)*(x<2)*x/2)" color=2
readout "$P(a<X<b)$" "max(min(max(B,0),2)^2-min(max(A,0),2)^2,0)/4"
readout "$F_X(b)$" "min(max(B,0),2)^2/4"
```

**Example: Example 1 · Reading a continuous CDF**

$X$ has CDF

$$
F_X(x)=\begin{cases}0,&x<0\\ x/4,&0\le x\le4\\ 1,&x>4\end{cases}
$$

Find (a) $P(X\le-1)$, (b) $P(X\le1)$, (c) $P(2<X\le3)$, (d) $P(X>1)$, (e) $P(X=1)$, and the PDF.

1. (a) Left of 0 the CDF is 0.

   $$P(X\le-1)=F_X(-1)=0$$
2. (b) Read the CDF directly.

   $$P(X\le1)=F_X(1)=\frac14$$
3. (c) **Difference** of the CDF.

   $$P(2<X\le3)=F_X(3)-F_X(2)=\frac34-\frac24=\frac14$$
4. (d) **Right tail.**

   $$P(X>1)=1-F_X(1)=1-\frac14=\frac34$$
5. (e) **A single point** of a continuous $X$: squeeze it into $(1-\varepsilon,1]$, whose probability $\varepsilon/4\to0$.

   $$P(X=1)\le F_X(1)-F_X(1-\varepsilon)=\frac{\varepsilon}{4}\to0\;\Rightarrow\;P(X=1)=0$$
6. **PDF** = slope of the CDF: $\tfrac14$ on $[0,4]$, $0$ elsewhere (a uniform $X$).

   $$f_X(x)=\frac{d}{dx}\frac{x}{4}=\frac14,\quad 0\le x\le4$$

**Answer:** (a) $0$ (b) $\tfrac14$ (c) $\tfrac14$ (d) $\tfrac34$ (e) $0$; $f_X=\tfrac14$ on $[0,4]$.

**Problem: Try it 1 · Find $c$, the CDF, and a probability** (intermediate)

$X$ has PDF $f_X(x)=c(1-x^4)$ for $-1\le x\le1$, and $0$ otherwise.
(a) Find $c$. (b) Find the CDF. (c) Find $P(|X|<\tfrac12)$.

<details><summary>Solution</summary>

1. (a) **Total area 1.** Power rule.

   $$c\int_{-1}^{1}(1-x^4)\,dx=c\left[x-\frac{x^5}{5}\right]_{-1}^{1}=c\left(\frac45+\frac45\right)=\frac{8c}{5}=1$$
2. So:

   $$c=\frac58$$
3. (b) **CDF** for $-1\le x\le1$: integrate from the left end $-1$ to $x$.

   $$F_X(x)=\frac58\left[t-\frac{t^5}{5}\right]_{-1}^{x}=\frac58\left(x-\frac{x^5}{5}+\frac45\right)$$
4. With the outside pieces:

   $$F_X(x)=\begin{cases}0,&x<-1\\ \frac58\left(x-\frac{x^5}{5}+\frac45\right),&-1\le x\le1\\ 1,&x>1\end{cases}$$
5. (c) $|X|<\tfrac12$ means $-\tfrac12<X<\tfrac12$. The PDF is symmetric, so take twice the area on $[0,\tfrac12]$.

   $$P(|X|<\frac12)=2\cdot\frac58\left[x-\frac{x^5}{5}\right]_0^{1/2}=\frac54\left(\frac12-\frac1{160}\right)=\frac{79}{128}$$
6. As a decimal:

   $$\frac{79}{128}\approx 0.6172$$

**Answer:** $c=\tfrac58$; $F_X(x)=\tfrac58\left(x-\tfrac{x^5}{5}+\tfrac45\right)$ on $[-1,1]$; $P(|X|<\tfrac12)=\tfrac{79}{128}\approx0.6172$

</details>

**Problem: Try it 2 · A triangle PDF** (intermediate)

Sketch $f(x)=\tfrac12-\tfrac14|x-3|$ for $1\le x\le5$ ($0$ otherwise). (a) Show it is a PDF. (b) Find its CDF $F$ and show $F$ is continuous. (c) Find $P(2<X<4)$.

<details><summary>Solution</summary>

1. (a) **Sketch:** a triangle with peak $\tfrac12$ at $x=3$, falling to $0$ at $x=1$ and $x=5$. It is $\ge0$ there.

   $$f(1)=0,\quad f(3)=\frac12,\quad f(5)=0$$
2. **Area** of the triangle = $\tfrac12\cdot$base$\cdot$height.

   $$\frac12\cdot4\cdot\frac12=1\;\checkmark$$
3. (b) **Left piece** $1\le x\le3$: here $|x-3|=3-x$, so $f(t)=\tfrac{t-1}{4}$.

   $$F(x)=\int_1^x\frac{t-1}{4}\,dt=\frac{(x-1)^2}{8}$$
4. **Right piece** $3\le x\le5$: the area still missing is a small triangle on $[x,5]$, by symmetry.

   $$F(x)=1-\frac{(5-x)^2}{8}$$
5. **Continuous:** both pieces give $\tfrac12$ at $x=3$; $F(1)=0$ and $F(5)=1$ match the outside pieces.

   $$\frac{(3-1)^2}{8}=\frac12=1-\frac{(5-3)^2}{8}$$
6. (c) Use $F(4)-F(2)$.

   $$P(2<X<4)=\left(1-\frac18\right)-\frac18=\frac34$$

**Answer:** Area $=1$; $F=\tfrac{(x-1)^2}{8}$ on $[1,3]$, $1-\tfrac{(5-x)^2}{8}$ on $[3,5]$ ($0$ before, $1$ after); $P(2<X<4)=\tfrac34$.

</details>

## Topic 2: Uniform and exponential

Two named continuous families. **Memorise** both PDFs and CDFs.

**Uniform$(a,b)$:** every value in $[a,b]$ is equally likely, so the PDF is flat.

$$f_X(x)=\begin{cases}\dfrac{1}{b-a},&a\le x\le b\\ 0,&\text{otherwise}\end{cases}\qquad F_X(x)=\begin{cases}0,&x<a\\ \dfrac{x-a}{b-a},&a\le x\le b\\ 1,&x>b\end{cases}$$

- The height $\frac1{b-a}$ is forced: the rectangle must have area 1.
- **Shortcut:** probability = (length of the part inside $[a,b]$) ÷ (total length $b-a$).

**Exponential$(\lambda)$:** waiting times and lifetimes. $\lambda>0$ is the rate.

$$f_X(x)=\lambda e^{-\lambda x}\ (x\ge0),\qquad F_X(x)=1-e^{-\lambda x}\ (x\ge0)$$

$$P(X>x)=e^{-\lambda x}$$

- Both are $0$ for $x<0$ (a lifetime can’t be negative).
- **Tail formula** $P(X>x)=e^{-\lambda x}$ is the one you’ll use most.
- **Interval:** $P(s<X<t)=e^{-\lambda s}-e^{-\lambda t}$.

> **Reminder:** **Conditional probability (Test 1):** $P(A\mid B)=\dfrac{P(A\cap B)}{P(B)}$.
> 
> If $A$ is inside $B$ (e.g. $\{X>20\}\subset\{X>10\}$), then $A\cap B=A$, so $P(A\mid B)=\dfrac{P(A)}{P(B)}$.

**Memoryless property** (exponential only): having already waited $s$ doesn’t change the future.

$$P(X>s+t\mid X>s)=\frac{e^{-\lambda(s+t)}}{e^{-\lambda s}}=e^{-\lambda t}=P(X>t)$$

Bigger $\lambda$ = a taller start and a faster drop = shorter waits.

```graph
title "Exponential PDF: the shaded tail is $P(X>t)=e^{-\lambda t}$"
x 0 6 label="$x$" height=250
y 0 2.2 label="$f_X(x)$"
slider L 0.2 2 1 step=0.05 label="$\lambda$"
slider T 0 5 1 step=0.05 label="$t$"
curve "L*exp(-L*x)" from=0 to=6 color=1 label="$\lambda e^{-\lambda x}$"
region "(x>T)*(y>0)*(y<L*exp(-L*x))" color=2
readout "$P(X>t)$" "exp(-L*T)"
readout "$F_X(t)$" "1-exp(-L*T)"
```

**Example: Example 2 · Component lifetime**

The lifetime $X$ (hours) of a component is exponential with $\lambda=0.002$. Find the probability it works for **at least 500 hours**.

1. **Family:** exponential → use the tail formula.

   $$P(X\ge500)=P(X>500)=e^{-\lambda\cdot500}$$
2. Or from the PDF, to see where it comes from:

   $$\int_{500}^{\infty}0.002e^{-0.002x}\,dx=\Big[-e^{-0.002x}\Big]_{500}^{\infty}=0+e^{-1}$$
3. Evaluate.

   $$e^{-0.002\cdot500}=e^{-1}\approx 0.3679$$

**Answer:** $e^{-1}\approx 0.3679$

**Problem: Try it 3 · Waiting for the bus** (introductory)

A bus arrives at a random time, uniform between 1:00 and 1:30 P.M. You arrive at 1:00. Find the probability you wait **at least 10 minutes**.

<details><summary>Solution</summary>

1. **Family:** $X$ = minutes after 1:00, Uniform$(0,30)$.

   $$f_X(x)=\frac1{30},\quad 0\le x\le30$$
2. Waiting $\ge10$ minutes means the bus comes at $X\ge10$. **Length ratio.**

   $$P(X\ge10)=\frac{30-10}{30}=\frac23$$

**Answer:** $\tfrac23$

</details>

**Problem: Try it 4 · Sine beats cosine** (intermediate)

A number $X$ is chosen uniformly from $[0,\tfrac{\pi}{2}]$. Find $P(\sin X>\cos X)$.

<details><summary>Solution</summary>

1. **Turn the event into an interval.** On $[0,\tfrac{\pi}{2}]$, $\sin x>\cos x$ exactly when $x>\tfrac{\pi}{4}$ (they cross at $45^\circ$).

   $$\{\sin X>\cos X\}=\{X>\frac{\pi}{4}\}$$
2. **Length ratio.**

   $$P=\frac{\pi/2-\pi/4}{\pi/2}=\frac12$$

**Answer:** $\tfrac12$

</details>

**Problem: Try it 5 · Old TV still working** (intermediate)

A TV tube’s lifetime (years) is exponential with $\lambda=0.1$. The TV is already 10 years old. Find the probability the tube lasts **another 10 years**.

<details><summary>Solution</summary>

1. **Conditional:** we want $P(X>20\mid X>10)$. $\{X>20\}$ is inside $\{X>10\}$.

   $$P(X>20\mid X>10)=\frac{P(X>20)}{P(X>10)}=\frac{e^{-2}}{e^{-1}}=e^{-1}$$
2. **Memoryless:** same as a brand-new tube lasting 10 years.

   $$P(X>10)=e^{-0.1\cdot10}=e^{-1}\approx 0.3679$$

**Answer:** $e^{-1}\approx 0.3679$ (the 10 years already used don’t matter)

</details>

**Problem: Try it 6 · Catching a flight** (intermediate)

Flights leave every half hour starting at 5:00 A.M. (so 9:00, 9:30, 10:00, …). A passenger arrives at a uniform random time between 8:45 and 9:45 A.M. Find the probability she waits (a) **at most 10 minutes**, (b) **at least 15 minutes**.

<details><summary>Solution</summary>

1. **Family:** $T$ = minutes after 8:45, Uniform$(0,60)$. Flights leave at $T=15,\ 45,\ 75$.

   $$f_T(t)=\frac1{60},\quad 0\le t\le60$$
2. (a) Wait $\le10$: arrive in the 10 minutes before a flight.

   $$T\in[5,15]\cup[35,45]\;\Rightarrow\;P=\frac{10+10}{60}=\frac13$$
3. (b) Wait $\ge15$: the next flight is at least 15 minutes away.

   $$T\in[15,30]\cup[45,60]\;\Rightarrow\;P=\frac{15+15}{60}=\frac12$$

**Answer:** (a) $\tfrac13$ (b) $\tfrac12$

</details>

## Topic 3: Gaussian (normal) random variables

The bell curve: noise, measurement error, sums of many small effects. $X\sim N(\mu,\sigma^2)$.

$$f_X(x)=\frac{1}{\sqrt{2\pi\sigma^2}}\,e^{-(x-\mu)^2/(2\sigma^2)}$$

- $\mu$ = the **centre** of the bell (any real number).
- $\sigma>0$ = the **width**: small $\sigma$ → narrow and tall, large $\sigma$ → wide and flat.
- Symmetric about $\mu$, so $P(X\le\mu)=\tfrac12$.
- This PDF has **no antiderivative** you can write down. That is why we use a table.

**Standard normal** $Z\sim N(0,1)$: its CDF has a name, $\Phi(z)=P(Z\le z)$, and is printed in a table (Lecture 10/11).

$$F_X(x)=\Phi\!\left(\frac{x-\mu}{\sigma}\right)\qquad\text{and}\qquad \Phi(-z)=1-\Phi(z)$$

**Recipe** (the skill tested is standardising; $\Phi$ values come from the table):

1. **Standardise:** $z=\dfrac{x-\mu}{\sigma}$ ("how many $\sigma$’s from the centre").
2. **Rewrite with $\le$:** $P(X>x)=1-\Phi(z)$, $\;P(a<X<b)=\Phi(z_b)-\Phi(z_a)$.
3. **Negative $z$:** the table has only $z\ge0$, so use $\Phi(-z)=1-\Phi(z)$.
4. **Symmetric interval:** $P(|X-\mu|<k\sigma)=2\Phi(k)-1$.
5. **Backwards** (given a probability, find $x$): find $z$ in the table, then $x=\mu+z\sigma$.

| $z$ | 0.5 | 1.0 | 1.28 | 1.5 | 1.645 | 1.96 | 2.0 | 2.5 |
|---|---|---|---|---|---|---|---|---|
| $\Phi(z)$ | 0.6915 | 0.8413 | 0.8997 | 0.9332 | 0.95 | 0.9750 | 0.97725 | 0.99379 |

> **Tip:** **Handy landmarks:** $\Phi(1.28)\approx0.90$ (top 10%), $\Phi(1.645)\approx0.95$ (between the table’s 1.64 and 1.65), $\Phi(1.96)=0.975$ (middle 95%). About 68% of values lie within $1\sigma$ of $\mu$, 95% within $2\sigma$.

Only the $z$-values matter: shift $\mu$ and the interval together, or scale $\sigma$ and the interval together, and the area stays the same.

```graph
title "Normal PDF: slide $\mu$, $\sigma$ and the interval $[a,b]$"
x -6 6 label="$x$" height=260
y 0 1.02 label="$f_X(x)$"
slider M -3 3 0 step=0.1 label="$\mu$"
slider S 0.4 3 1 step=0.05 label="$\sigma$"
slider A -6 6 -1 step=0.05 label="$a$"
slider B -6 6 1 step=0.05 label="$b$"
let za "(A-M)/(S*sqrt(2))"
let zb "(B-M)/(S*sqrt(2))"
let ta "1/(1+0.3275911*abs(za))"
let tb "1/(1+0.3275911*abs(zb))"
let ea "sign(za)*(1-((((1.061405429*ta-1.453152027)*ta+1.421413741)*ta-0.284496736)*ta+0.254829592)*ta*exp(-za^2))"
let eb "sign(zb)*(1-((((1.061405429*tb-1.453152027)*tb+1.421413741)*tb-0.284496736)*tb+0.254829592)*tb*exp(-zb^2))"
curve "exp(-(x-M)^2/(2*S^2))/(S*sqrt(2*pi))" from=-6 to=6 color=1 label="$f_X(x)$"
vline "M" color=1
region "(x>A)*(x<B)*(y>0)*(y<exp(-(x-M)^2/(2*S^2))/(S*sqrt(2*pi)))" color=2
readout "$z_a=(a-\mu)/\sigma$" "(A-M)/S"
readout "$z_b$" "(B-M)/S"
readout "$P(a<X<b)=\Phi(z_b)-\Phi(z_a)$" "max(0.5*(eb-ea),0)"
```

**Example: Example 3 · Sensor measurement error**

A temperature sensor’s error $X$ (°C) is Gaussian with $\mu=0$, $\sigma=0.5$. The sensor is accurate enough if $|X|<0.8$. Find the probability of that.

1. **Rewrite** the event as an interval.

   $$P(|X|<0.8)=P(-0.8<X<0.8)=F_X(0.8)-F_X(-0.8)$$
2. **Standardise** both ends.

   $$z=\frac{\pm0.8-0}{0.5}=\pm1.6\;\Rightarrow\;\Phi(1.6)-\Phi(-1.6)$$
3. **Negative $z$:** $\Phi(-1.6)=1-\Phi(1.6)$.

   $$\Phi(1.6)-\big(1-\Phi(1.6)\big)=2\Phi(1.6)-1$$
4. **Table:** $\Phi(1.6)=0.9452$.

   $$2(0.9452)-1=0.8904$$

**Answer:** $2\Phi(1.6)-1=0.8904$

**Problem: Try it 7 · Top 10% of a test** (intermediate)

Scores are normal with $\mu=500$, $\sigma=100$. What score puts a student in the **top 10%**?

<details><summary>Solution</summary>

1. **Backwards question:** find $x$ with $P(X\le x)=0.90$.

   $$\Phi\!\left(\frac{x-500}{100}\right)=0.90$$
2. **Table:** $\Phi(1.28)=0.8997$ and $\Phi(1.29)=0.9015$, so $z\approx1.28$.

   $$z\approx1.28$$
3. **Un-standardise:** $x=\mu+z\sigma$.

   $$x=500+1.28(100)=628$$

**Answer:** About $628$ or more.

</details>

**Problem: Try it 8 · Rover distance estimate** (intermediate)

A rover’s distance travelled is $X\sim N(\mu,\sigma^2)$ with $\mu=500$ m and $\sigma^2=2.25$ m². Find (a) $P(X<500)$, (b) $P(X=501)$, (c) $P(X>501)$ and $P(X>505)$.

<details><summary>Solution</summary>

1. **Careful:** the variance is given, so $\sigma=\sqrt{2.25}=1.5$.

   $$\sigma=1.5$$
2. (a) $500=\mu$: half the bell is below the centre.

   $$P(X<500)=\Phi(0)=0.5$$
3. (b) A single point of a continuous $X$.

   $$P(X=501)=0$$
4. (c) Standardise: $z=\tfrac{1}{1.5}\approx0.67$.

   $$P(X>501)=1-\Phi(0.67)=1-0.7486=0.2514$$
5. $z=\tfrac{5}{1.5}\approx3.33$ is past the end of the table ($\Phi\approx1$).

   $$P(X>505)=1-\Phi(3.33)\approx 0.0004$$

**Answer:** (a) $0.5$ (b) $0$ (c) $\approx0.2514$ and $\approx0.0004$

</details>

**Problem: Try it 9 · Blood pressure** (intermediate)

Diastolic blood pressure is normal with $\mu=80$, $\sigma=7$ (mm Hg). $\ge95$ is hypertensive; strictly between $89$ and $95$ is mild hypertension. What percent of people are in each group?

<details><summary>Solution</summary>

1. **Standardise** both cut-offs (round to the table’s 2 decimals).

   $$z_{95}=\frac{95-80}{7}\approx2.14,\qquad z_{89}=\frac{89-80}{7}\approx1.29$$
2. **Hypertensive:** right tail.

   $$P(X\ge95)=1-\Phi(2.14)=1-0.98382=0.01618$$
3. **Mild:** between the two.

   $$\begin{gathered}P(89<X<95)=\Phi(2.14)-\Phi(1.29)\\ =0.98382-0.9015=0.0823\end{gathered}$$

**Answer:** Mild ≈ 8.23%, hypertensive ≈ 1.62%

</details>

## Topic 4: Mixed random variables

A **mixed** $X$ has a **point with positive probability** (a jump in the CDF) **plus** a continuous part (a sloped CDF).

- **Spot it:** the story has "with probability $q$ it is exactly $x_0$, otherwise it is spread over an interval".
- **The jump:** $P(X=x_0)$ = size of the jump in $F_X$ at $x_0$.
- **The continuous part:** its density is scaled by the leftover probability, so its area is $1-q$, not 1.
- **Probability of an interval** = (point masses inside it) + (area of the continuous part over it).

**Example: Example 4 · Received signal level**

A receiver loses the signal completely with probability $0.2$, so $P(X=0)=0.2$. Otherwise (probability $0.8$) the level $X$ is uniform on $(0,10)$. (a) Find $P(2<X<5)$. (b) Find and sketch the CDF.

1. **Continuous part:** uniform on $(0,10)$, scaled by $0.8$.

   $$f(x)=0.8\cdot\frac1{10}=0.08,\quad 0<x<10$$
2. (a) The point $X=0$ is **not** in $(2,5)$, so only area counts.

   $$P(2<X<5)=\int_2^5 0.08\,dx=0.08\cdot3=0.24$$
3. (b) **CDF:** $0$ before $0$; **jump of $0.2$** at $0$; then rises with slope $0.08$; reaches $1$ at $10$.

   $$F_X(x)=\begin{cases}0,&x<0\\ 0.2+0.08x,&0\le x<10\\ 1,&x\ge10\end{cases}$$
4. Check: at $x=10$, $0.2+0.8=1$. ✓

   $$F_X(10)=1$$

**Answer:** (a) $0.24$ (b) jump $0.2$ at $0$, then a straight ramp up to $1$ at $x=10$.

A discrete $X$ is all jumps, a continuous $X$ is all slope, a mixed $X$ has both.

```graph
title "CDF of the received signal: a jump, then a ramp"
x -2 12 label="$x$" height=230
y 0 1.1 label="$F_X(x)$"
segment "-2" "0" "0" "0" color=2
segment "0" "0.2" "10" "1" color=2
segment "10" "1" "12" "1" color=2
point "0" "0.2" color=2
segment "0" "0" "0" "0.2" color=0 dash
text "1.6" "0.12" "jump $=0.2$"
text "6.8" "0.6" "slope $0.08$"
```

## Practice Questions

Test-style questions for Question 2, roughly easy → hard. Solve on paper first, then open the solution.

**Problem: Question 1 · Uniform voltage** (introductory)

A voltage $X$ is uniform on $[-2,3]$ V. Find (a) the PDF and CDF, (b) $P(|X|<1)$, (c) $P(X>2\mid X>0)$.

<details><summary>Solution</summary>

1. (a) **Uniform$(-2,3)$:** height $\tfrac1{5}$.

   $$f_X(x)=\frac15\ (-2\le x\le3),\qquad F_X(x)=\frac{x+2}{5}\ (-2\le x\le3)$$
2. (b) $|X|<1$ is $(-1,1)$, length 2, inside $[-2,3]$.

   $$P(|X|<1)=\frac{2}{5}$$
3. (c) **Conditional**, and $\{X>2\}\subset\{X>0\}$.

   $$P(X>2\mid X>0)=\frac{P(X>2)}{P(X>0)}=\frac{1/5}{3/5}=\frac13$$

**Answer:** $f=\tfrac15$, $F=\tfrac{x+2}{5}$ on $[-2,3]$; (b) $\tfrac25$ (c) $\tfrac13$

</details>

**Problem: Question 2 · Battery lifetime** (intermediate)

A battery’s lifetime $X$ (hours) is exponential with $\lambda=0.05$. Find (a) $P(X>30)$, (b) $P(10<X<30)$, (c) the **median** $m$ (the time with $P(X\le m)=\tfrac12$).

<details><summary>Solution</summary>

1. (a) **Tail formula.**

   $$P(X>30)=e^{-0.05\cdot30}=e^{-1.5}\approx 0.2231$$
2. (b) **Difference of tails.**

   $$P(10<X<30)=e^{-0.5}-e^{-1.5}\approx 0.3834$$
3. (c) Set the CDF to $\tfrac12$ and take $\ln$ of both sides.

   $$1-e^{-0.05m}=\frac12\;\Rightarrow\;e^{-0.05m}=\frac12\;\Rightarrow\;-0.05m=\ln\frac12$$
4. Solve ($\ln\tfrac12=-\ln2$).

   $$m=\frac{\ln2}{0.05}\approx 13.86\text{ h}$$

**Answer:** (a) $\approx 0.2231$ (b) $\approx 0.3834$ (c) $m=\ln 2/0.05\approx 13.86$ h

</details>

**Problem: Question 3 · Power-law PDF** (intermediate)

$X$ has PDF $f_X(x)=kx^2$ for $0\le x\le3$, $0$ otherwise. Find (a) $k$, (b) the CDF, (c) $P(1<X<2)$, (d) the value $a$ with $P(X\le a)=\tfrac18$.

<details><summary>Solution</summary>

1. (a) **Total area 1.**

   $$k\int_0^3x^2\,dx=k\cdot\frac{27}{3}=9k=1\;\Rightarrow\;k=\frac19$$
2. (b) **CDF** on $[0,3]$.

   $$F_X(x)=\int_0^x\frac{t^2}{9}\,dt=\frac{x^3}{27}\quad(0\le x\le3),\quad 0\text{ before},\ 1\text{ after}$$
3. (c) $F(2)-F(1)$.

   $$P(1<X<2)=\frac{8-1}{27}=\frac{7}{27}$$
4. (d) Solve $F(a)=\tfrac18$.

   $$\frac{a^3}{27}=\frac18\;\Rightarrow\;a^3=\frac{27}{8}\;\Rightarrow\;a=\frac32$$

**Answer:** (a) $\tfrac19$ (b) $\tfrac{x^3}{27}$ on $[0,3]$ (c) $\tfrac7{27}$ (d) $a=1.5$

</details>

**Problem: Question 4 · Two-sided exponential** (intermediate)

$X$ has PDF $f_X(x)=c\,e^{-2|x|}$ for all real $x$. Find (a) $c$, (b) $P(X>1)$, (c) $P(|X|<0.5)$.

<details><summary>Solution</summary>

1. (a) **Symmetric:** total area = twice the area on $[0,\infty)$.

   $$2c\int_0^{\infty}e^{-2x}\,dx=2c\cdot\frac12=c=1$$
2. (b) Only the right side.

   $$P(X>1)=\int_1^{\infty}e^{-2x}\,dx=\frac{e^{-2}}{2}\approx 0.0677$$
3. (c) Twice the area on $[0,0.5]$.

   $$P(|X|<0.5)=2\int_0^{0.5}e^{-2x}\,dx=1-e^{-1}\approx 0.6321$$

**Answer:** (a) $c=1$ (b) $\approx 0.0677$ (c) $\approx 0.6321$

</details>

**Problem: Question 5 · Rayleigh · Practice 02 Q4** (intermediate)

$R$ has CDF

$$
F_R(r)=\begin{cases}0,&r<0\\ 1-e^{-r^2/(2\sigma^2)},&r\ge0\end{cases}
$$

Find $P(\sigma\le R\le2\sigma)$ and $P(R>3\sigma)$.

<details><summary>Solution</summary>

1. **Difference of the CDF** (continuous, so endpoints don’t matter).

   $$P(\sigma\le R\le2\sigma)=F_R(2\sigma)-F_R(\sigma)=e^{-1/2}-e^{-2}\approx 0.4712$$
2. **Right tail.** $\sigma$ cancels: $\tfrac{(3\sigma)^2}{2\sigma^2}=\tfrac92$.

   $$P(R>3\sigma)=1-F_R(3\sigma)=e^{-9/2}\approx 0.0111$$
3. **PDF** (if asked): differentiate, chain rule.

   $$f_R(r)=\frac{r}{\sigma^2}e^{-r^2/(2\sigma^2)},\quad r\ge0$$

**Answer:** $e^{-1/2}-e^{-2}\approx 0.4712$; $e^{-9/2}\approx 0.0111$

</details>

**Problem: Question 6 · Seeing runners · Tutorial 4 Q1** (intermediate)

The time $X$ (minutes) between seeing two runners has PDF $f(x)=\lambda x e^{-x}$ for $x>0$. (a) Find $\lambda$. (b) Find the CDF. (c) Find the probability the next runner is seen in 2 to 5 minutes, and in at least 7 minutes.

<details><summary>Solution</summary>

1. **Integration by parts** (you’ll need it): $\int u\,dv=uv-\int v\,du$. With $u=x$, $dv=e^{-x}dx$:

   $$\int xe^{-x}\,dx=-xe^{-x}+\int e^{-x}\,dx=-(x+1)e^{-x}$$
2. (a) **Total area 1.** At $\infty$ the term is $0$; at $0$ it is $-1$.

   $$\lambda\Big[-(x+1)e^{-x}\Big]_0^{\infty}=\lambda(0+1)=1\;\Rightarrow\;\lambda=1$$
3. (b) **CDF** for $x\ge0$ ($0$ for $x<0$).

   $$F(x)=\Big[-(t+1)e^{-t}\Big]_0^{x}=1-(1+x)e^{-x}$$
4. (c) **2 to 5 minutes:** $F(5)-F(2)$.

   $$P(2<X<5)=3e^{-2}-6e^{-5}\approx 0.3656$$
5. **At least 7:** right tail.

   $$P(X\ge7)=1-F(7)=8e^{-7}\approx 0.0073$$

**Answer:** $\lambda=1$; $F(x)=1-(1+x)e^{-x}$; $\approx 0.3656$ and $\approx 0.0073$

</details>

**Problem: Question 7 · Resistor tolerance** (intermediate)

Resistances are $R\sim N(100,\,4)$ Ω (so $\sigma=2$). (a) A resistor passes if $97\le R\le103$. What fraction passes? (b) What fraction is above $104$ Ω? (c) Find $t$ so that $95\%$ lie in $100\pm t$.

<details><summary>Solution</summary>

1. (a) **Symmetric** interval, $k=\tfrac{3}{2}=1.5$ standard deviations.

   $$P(|R-100|\le3)=2\Phi(1.5)-1=2(0.9332)-1=0.8664$$
2. (b) $z=\tfrac{104-100}{2}=2$.

   $$P(R>104)=1-\Phi(2)=1-0.97725=0.02275$$
3. (c) **Backwards:** $2\Phi(k)-1=0.95$ means $\Phi(k)=0.975$, so $k=1.96$.

   $$t=1.96\,\sigma=1.96\cdot2=3.92\ \Omega$$

**Answer:** (a) $0.8664$ (b) $0.02275$ (c) $t=3.92$ Ω

</details>

**Problem: Question 8 · Noise level** (intermediate)

Noise $X\sim N(0,\sigma^2)$ (volts). Find $\sigma$ so that $|X|$ exceeds $1$ V only $5\%$ of the time.

<details><summary>Solution</summary>

1. **Rewrite:** $P(|X|>1)=0.05$ means $P(|X|\le1)=0.95$.

   $$2\Phi\!\left(\frac{1}{\sigma}\right)-1=0.95\;\Rightarrow\;\Phi\!\left(\frac1\sigma\right)=0.975$$
2. **Table:** $\Phi(1.96)=0.975$.

   $$\frac1\sigma=1.96\;\Rightarrow\;\sigma=\frac{1}{1.96}\approx 0.510\text{ V}$$

**Answer:** $\sigma\approx 0.510$ V

</details>

**Problem: Question 9 · Daily rainfall (mixed)** (intermediate)

On a given day it doesn’t rain with probability $0.6$ ($X=0$). If it rains, the amount $X$ (mm) is exponential with $\lambda=0.5$. (a) Find the CDF of $X$. (b) Find $P(X>2)$. (c) Find $P(X\le1)$.

<details><summary>Solution</summary>

1. **Mixed:** a jump of $0.6$ at $0$, then the exponential CDF scaled by $0.4$.

   $$F_X(x)=\begin{cases}0,&x<0\\ 0.6+0.4\left(1-e^{-0.5x}\right),&x\ge0\end{cases}$$
2. (b) **Right tail:** only the rainy part can exceed 2.

   $$P(X>2)=0.4\,e^{-0.5\cdot2}=0.4e^{-1}\approx 0.1472$$
3. (c) Includes the jump at $0$.

   $$P(X\le1)=0.6+0.4(1-e^{-0.5})\approx 0.7574$$

**Answer:** (a) jump $0.6$ at $0$, then $0.6+0.4(1-e^{-0.5x})$ (b) $\approx 0.1472$ (c) $\approx 0.7574$

</details>

**Problem: Question 10 · A CDF with a jump · Practice 02 Q3** (advanced)

$X$ has CDF

$$
F_X(x)=\begin{cases}0,&x<-1\\ \tfrac13+\tfrac23(x+1)^2,&-1\le x\le0\\ 1,&x>0\end{cases}
$$

Find the probabilities of $A=\{X>\tfrac13\}$, $B=\{|X|\ge1\}$, $C=\{|X-\tfrac13|<1\}$, $D=\{X<0\}$.

<details><summary>Solution</summary>

1. **Spot the type:** $F$ jumps from $0$ to $\tfrac13$ at $x=-1$, then rises smoothly. **Mixed**, with $P(X=-1)=\tfrac13$.

   $$P(X=-1)=F_X(-1)-F_X(-1^-)=\frac13$$
2. $A$: $X$ never exceeds $0$.

   $$P(A)=1-F_X(\frac13)=1-1=0$$
3. $B$: $X\ge1$ is impossible, and $X\le-1$ means $X=-1$ exactly (the jump).

   $$P(B)=P(X\le-1)=F_X(-1)=\frac13$$
4. $C$: $-\tfrac23<X<\tfrac43$. $F$ has no jump at $-\tfrac23$.

   $$P(C)=1-F_X(-\frac23)=1-\left(\frac13+\frac23\cdot\frac19\right)=1-\frac{11}{27}=\frac{16}{27}$$
5. $D$: $F$ is continuous at $0$ ($\tfrac13+\tfrac23=1$), so $P(X=0)=0$.

   $$P(D)=F_X(0^-)=1$$

**Answer:** $P(A)=0$, $P(B)=\tfrac13$, $P(C)=\tfrac{16}{27}$, $P(D)=1$

</details>
