# Test 2 - Question 3

**Lectures 11–13.** Expected values, variances, and the properties of expectation and variance.

## Topic 1: Expected value

The **expected value** (mean) $E[X]=\mu_X$ is the **long-run average** of $X$ if you repeat the experiment many times.

Each value is weighted by how likely it is: a **probability-weighted average**.

$$E[X]=\sum_{x\in R_X} x\,p_X(x)\quad\text{(discrete)}$$

$$E[X]=\int_{-\infty}^{\infty} x\,f_X(x)\,dx\quad\text{(continuous)}$$

- **Why it works:** repeat $N$ times; value $x_k$ shows up about $N p_k$ times, so the average is $\approx\sum x_k p_k$.
- **Continuous:** the sum becomes an integral, with $p_k$ replaced by $f_X(x)\,dx$.
- $E[X]$ **need not be a possible value**: a die averages $3.5$.
- **Mixed** $X$ (a point mass plus a density): add the two parts, $\sum x\,P(X=x)+\int x\,f(x)\,dx$.

**Expected value of a function** $g(X)$: no need to find the distribution of $Y=g(X)$ first. Just weight $g(x)$ instead of $x$:

$$E[g(X)]=\sum_{x} g(x)\,p_X(x)\qquad E[g(X)]=\int_{-\infty}^{\infty} g(x)\,f_X(x)\,dx$$

> **Warning:** **$E[X^2]\ne(E[X])^2$** in general. Square inside the sum/integral, not after.

> **Reminder:** **Calculus you need for $E[X]$**
> 
> - **Power rule:** $\displaystyle\int x^n\,dx=\frac{x^{n+1}}{n+1}$.
> - **Exponential:** $\displaystyle\int e^{-\lambda x}\,dx=-\frac{1}{\lambda}e^{-\lambda x}$.
> - **By parts:** $\displaystyle\int u\,dv=uv-\int v\,du$. For $\int x\,e^{-\lambda x}dx$ take $u=x$, $dv=e^{-\lambda x}dx$.
> - **Shortcut (memorise):** $\displaystyle\int_0^{\infty}x^n e^{-\lambda x}\,dx=\frac{n!}{\lambda^{n+1}}$.
> - **Symmetry:** an **odd** function ($g(-x)=-g(x)$, like $x$, $x^3$) on $[-a,a]$ integrates to $0$.

**Method:**

1. **Write** the PMF/PDF and where it is nonzero.
2. **Multiply** by $x$ (or by $g(x)$).
3. **Add/integrate** only over the nonzero range (outside it the integrand is $0$).

**Example: Example 1 · A die and a uniform**

(a) A fair die is rolled; $X$ = the number. Find $E[X]$ and $E[X^2]$. (b) $X$ is uniform on $[0,2]$: $f_X(x)=\tfrac12$ on $[0,2]$. Find $E[X]$.

1. (a) **Weight** each face by $\tfrac16$.

   $$E[X]=\frac16(1+2+3+4+5+6)=\frac{21}{6}=3.5$$
2. $E[X^2]$: square **inside** the sum.

   $$E[X^2]=\frac16(1+4+9+16+25+36)=\frac{91}{6}\approx15.17$$
3. Compare: $(E[X])^2=12.25\ne15.17$.

   $$E[X^2]\ne(E[X])^2$$
4. (b) **Integrate** over $[0,2]$ only.

   $$E[X]=\int_0^2 x\cdot\frac12\,dx=\frac12\left[\frac{x^2}{2}\right]_0^2=1$$

**Answer:** (a) $E[X]=3.5$, $E[X^2]=\tfrac{91}{6}$ (b) $E[X]=1$, the middle of $[0,2]$.

The mean is the **balance point** of the PDF. A long right tail pulls it to the right of the peak.

```graph
title "Exponential PDF: the mean $1/\lambda$ is not the peak"
x 0 6 label="$x$" height=240
y 0 2.1 label="$f_X(x)$"
slider L 0.3 2 1 step=0.05 label="$\lambda$"
curve "L*exp(-L*x)" from=0 to=6 label="$\lambda e^{-\lambda x}$"
vline "1/L" label="$E[X]=1/\lambda$" color=2
readout "$E[X]=1/\lambda$" "1/L"
```

**Problem: Try it 1 · Second moment of a uniform** (introductory)

$X$ is uniform on $[0,2]$. Find $E[X^2]$.

<details><summary>Solution</summary>

1. **Use** $E[g(X)]=\int g(x)f_X(x)\,dx$ with $g(x)=x^2$.

   $$E[X^2]=\int_0^2 x^2\cdot\frac12\,dx$$
2. **Power rule.**

   $$=\frac12\left[\frac{x^3}{3}\right]_0^2=\frac12\cdot\frac83=\frac43$$

**Answer:** $E[X^2]=\tfrac43$ (not $(E[X])^2=1$).

</details>

**Problem: Try it 2 · Mean time between customers** (intermediate)

The time $X$ between customer arrivals is exponential: $f_X(t)=\lambda e^{-\lambda t}$ for $t\ge0$. Find the mean $E[X]$.

<details><summary>Solution</summary>

1. **Set up** over $[0,\infty)$.

   $$E[X]=\int_0^{\infty}t\,\lambda e^{-\lambda t}\,dt$$
2. **By parts:** $u=t$, $dv=\lambda e^{-\lambda t}dt$, so $du=dt$, $v=-e^{-\lambda t}$.

   $$=\Big[-t\,e^{-\lambda t}\Big]_0^{\infty}+\int_0^{\infty}e^{-\lambda t}\,dt$$
3. The boundary term is $0$ (exponential beats $t$).

   $$=0+\Big[-\frac1\lambda e^{-\lambda t}\Big]_0^{\infty}=\frac1\lambda$$

**Answer:** $E[X]=\dfrac1\lambda$. (Rate 3 per minute → mean gap $\tfrac13$ min.)

</details>

**Problem: Try it 3 · Mean of a symmetric PDF** (intermediate)

$X$ has PDF $f_X(t)=\tfrac{\lambda}{2}e^{-\lambda|t-\gamma|}$ for all $t$ (a Laplace density centred at $\gamma$). Find $E[X]$.

<details><summary>Solution</summary>

1. **Shift:** let $u=t-\gamma$, so $t=u+\gamma$.

   $$E[X]=\int_{-\infty}^{\infty}(u+\gamma)\,\frac{\lambda}{2}e^{-\lambda|u|}\,du$$
2. **Split.** $u\,e^{-\lambda|u|}$ is **odd**, so its integral is $0$; the rest is $\gamma$ times the total area $1$.

   $$=\underbrace{\int u\,\frac{\lambda}{2}e^{-\lambda|u|}du}_{0}+\gamma\underbrace{\int\frac{\lambda}{2}e^{-\lambda|u|}du}_{1}$$
3. So the mean is the centre of symmetry.

   $$E[X]=\gamma$$

**Answer:** $E[X]=\gamma$: a PDF symmetric about $c$ has mean $c$.

</details>

**Problem: Try it 4 · Mean of a mixed random variable** (intermediate)

A received signal level $X$ is $0$ with probability $0.2$ (signal lost). Otherwise (probability $0.8$) it is uniform on $(0,10)$, so the continuous part has density $0.8\cdot\tfrac1{10}=0.08$ on $(0,10)$. Find $E[X]$.

<details><summary>Solution</summary>

1. **Discrete part:** the point mass at $0$.

   $$0\cdot P(X=0)=0\cdot0.2=0$$
2. **Continuous part:** integrate $x$ times the density $0.08$.

   $$\int_0^{10}x\,(0.08)\,dx=0.08\cdot\frac{10^2}{2}=4$$
3. **Add** the parts.

   $$E[X]=0+4=4$$

**Answer:** $E[X]=4$ (the 20% of zeros pull the average down from 5).

</details>

## Topic 2: Variance and standard deviation

The mean gives the **centre**. Two variables can share a centre but spread very differently:

- $X=9$ or $11$ (each $\tfrac12$): $E[X]=10$, stays close.
- $Y=0$ or $20$ (each $\tfrac12$): $E[Y]=10$, far more spread out.
- The average deviation $E[X-\mu_X]$ is always $0$ (the $+$ and $-$ cancel), so we **square** the deviation.

$$\operatorname{Var}(X)=E\big[(X-\mu_X)^2\big]$$

**Shortcut** (almost always faster):

$$\operatorname{Var}(X)=E[X^2]-\big(E[X]\big)^2$$

```steps
title "Where the shortcut comes from"
$$
E\big[(X-\mu)^2\big]
$$
Start from the definition, with $\mu=E[X]$ a constant.
$$
E\big[\hl{X^2-2\mu X+\mu^2}\big]
$$
Expand the square.
$$
\hl{E[X^2]-2\mu\,E[X]+\mu^2}
$$
Linearity: constants come out of $E$.
$$
E[X^2]-2\mu\cdot\hl{\mu}+\mu^2
$$
Use $E[X]=\mu$.
$$
\hl{E[X^2]-\mu^2}
$$
Done: mean of the square minus square of the mean.
```

- **Units:** variance has **squared** units (V → V²).
- **Standard deviation** $\sigma_X=\sqrt{\operatorname{Var}(X)}$ is back in the units of $X$: a typical distance from the mean.
- $\operatorname{Var}(X)\ge0$, and $=0$ only when $X$ is a constant.
- For a Gaussian $N(\mu,\sigma^2)$: mean $\mu$, standard deviation $\sigma$ (the width of the bell).

Drag $d$: the mean never moves, but the variance grows like $d^2$. ($d=1$ is $X$ above, $d=10$ is $Y$.)

```graph
title "Same mean, different spread: $X=10\pm d$, each with probability $\tfrac12$"
x -1 21 label="$x$" height=220
y 0 0.65 label="$p_X(x)$"
slider d 0 10 1 step=0.5 label="$d$"
segment "10-d" "0" "10-d" "0.5" color=1
point "10-d" "0.5" color=1
segment "10+d" "0" "10+d" "0.5" color=1
point "10+d" "0.5" color=1
vline "10" label="$E[X]=10$" color=2
readout "$E[X]$" "10"
readout "$\mathrm{Var}(X)=d^2$" "d^2"
readout "$\sigma_X=d$" "d"
```

**Method:**

1. **Find** $E[X]$.
2. **Find** $E[X^2]$ (square inside the sum/integral).
3. **Subtract:** $\operatorname{Var}=E[X^2]-(E[X])^2$; then $\sigma=\sqrt{\operatorname{Var}}$.

**Example: Example 2 · A two-level sensor voltage**

A sensor reads $X=4\text{ V}$ or $X=6\text{ V}$, each with probability $0.5$. Find $E[X]$, $E[X^2]$, $\operatorname{Var}(X)$ and $\sigma_X$.

1. **Mean.**

   $$E[X]=4(0.5)+6(0.5)=5\text{ V}$$
2. **Second moment.**

   $$E[X^2]=16(0.5)+36(0.5)=26\text{ V}^2$$
3. **Subtract.**

   $$\operatorname{Var}(X)=26-5^2=1\text{ V}^2$$
4. **Standard deviation** (back to volts).

   $$\sigma_X=\sqrt1=1\text{ V}$$

**Answer:** $E[X]=5$ V, $E[X^2]=26$ V², $\operatorname{Var}(X)=1$ V², $\sigma_X=1$ V.

**Problem: Try it 5 · A binary random variable** (introductory)

$X$ takes only the values $0$ and $1$, with $P(X=0)=p$ and $P(X=1)=1-p$. Find $E[X]$, $\operatorname{Var}(X)$ and $E[X^5]$.

<details><summary>Solution</summary>

1. **Mean.**

   $$E[X]=0\cdot p+1\cdot(1-p)=1-p$$
2. **Trick:** $0^n=0$ and $1^n=1$, so $X^n=X$ for every $n\ge1$.

   $$E[X^2]=E[X^5]=E[X]=1-p$$
3. **Subtract.**

   $$\operatorname{Var}(X)=(1-p)-(1-p)^2=(1-p)\,p$$

**Answer:** $E[X]=1-p$, $\operatorname{Var}(X)=p(1-p)$, $E[X^5]=1-p$.

</details>

**Problem: Try it 6 · Variance from a staircase CDF** (intermediate)

$X$ has CDF

$$
F_X(x)=\begin{cases}0,&x<-3\\ 3/8,&-3\le x<0\\ 3/4,&0\le x<6\\ 1,&x\ge6\end{cases}
$$

Is $X$ discrete or continuous? Find $\operatorname{Var}(X)$ and $\sigma_X$.

<details><summary>Solution</summary>

1. **Staircase** → discrete. The **jumps** give the PMF.

   $$p_X(-3)=\frac38,\quad p_X(0)=\frac38,\quad p_X(6)=\frac14$$
2. **Mean.**

   $$E[X]=-3\cdot\frac38+0+6\cdot\frac14=-\frac98+\frac{12}{8}=\frac38$$
3. **Second moment.**

   $$E[X^2]=9\cdot\frac38+0+36\cdot\frac14=\frac{27}{8}+\frac{72}{8}=\frac{99}{8}$$
4. **Subtract**, then take the root.

   $$\operatorname{Var}(X)=\frac{99}{8}-\frac{9}{64}=\frac{783}{64}\approx12.234,\quad \sigma_X\approx3.498$$

**Answer:** Discrete; $\operatorname{Var}(X)=\tfrac{783}{64}\approx12.234$, $\sigma_X\approx3.498$.

</details>

**Problem: Try it 7 · A PDF with a constant: mean and variance** (intermediate)

$f_X(x)=Cx^2$ for $|x|\le1$, and $0$ otherwise. (a) Find $C$ and the CDF. (b) Find $E[X]$ and $\operatorname{Var}(X)$.

<details><summary>Solution</summary>

1. (a) **Total area = 1.**

   $$\int_{-1}^{1}Cx^2\,dx=C\cdot\frac23=1\;\Rightarrow\;C=\frac32$$
2. **CDF** on $[-1,1]$: integrate from $-1$.

   $$F_X(x)=\int_{-1}^{x}\frac32t^2\,dt=\frac{x^3+1}{2}\quad(0\text{ left of }-1,\ 1\text{ right of }1)$$
3. (b) **Mean:** $x\cdot x^2=x^3$ is odd on $[-1,1]$.

   $$E[X]=\int_{-1}^{1}\frac32x^3\,dx=0$$
4. **Second moment.**

   $$E[X^2]=\int_{-1}^{1}\frac32x^4\,dx=\frac32\cdot\frac25=\frac35$$
5. **Subtract.**

   $$\operatorname{Var}(X)=\frac35-0^2=\frac35$$

**Answer:** $C=\tfrac32$, $F_X(x)=\tfrac{x^3+1}{2}$ on $[-1,1]$; $E[X]=0$, $\operatorname{Var}(X)=\tfrac35$.

</details>

## Topic 3: Properties of expectation and variance

These rules turn most "find $E$ / Var of something" questions into one line.

$$E[aX+b]=a\,E[X]+b\qquad E[aX+bY]=a\,E[X]+b\,E[Y]$$

$$\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)\qquad \sigma_{aX+b}=|a|\,\sigma_X$$

- **Shifting** by $b$ moves the centre but **not** the spread: $b$ disappears from Var.
- **Scaling** by $a$ scales the spread by $|a|$, so Var by $a^2$. A minus sign never makes Var negative: $\operatorname{Var}(-X)=\operatorname{Var}(X)$.
- $E[b]=b$ and $\operatorname{Var}(b)=0$ for a constant $b$.
- **Turn the shortcut around:** $E[X^2]=\operatorname{Var}(X)+(E[X])^2$. Use it whenever you are given $E$ and Var.

```steps
title "Why $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$"
$$
\operatorname{Var}(aX+b)=E\big[(aX+b-E[aX+b])^2\big]
$$
Definition, with $Y=aX+b$.
$$
=E\big[(aX+b-\hl{aE[X]-b})^2\big]
$$
Linearity of $E$.
$$
=E\big[\hl{a^2}(X-E[X])^2\big]
$$
The $b$ cancels; pull out $a$ and square it.
$$
=\hl{a^2\operatorname{Var}(X)}
$$
$a^2$ is a constant, so it comes out of $E$.
```

**Moments:** $E[X^n]$ is the $n$th (raw) **moment**; $E[(X-\mu_X)^n]$ is the $n$th **central moment**. So $E[X]$ = 1st moment, $E[X^2]$ = 2nd moment, and Var = 2nd central moment.

**Means and variances to memorise** (no formula sheet). Each can be found with Topics 1–2:

| Distribution | $E[X]$ | $\operatorname{Var}(X)$ | Where you saw it |
|---|---|---|---|
| Bernoulli$(p)$ | ${p}$ | ${p(1-p)}$ | Try it 5 (there $P(X=1)=1-p$) |
| Binomial$(n,p)$ | ${np}$ | ${np(1-p)}$ | memorise |
| Geometric, $k=1,2,\dots$ | ${\dfrac1p}$ | ${\dfrac{1-p}{p^2}}$ | memorise |
| Geometric, $k=0,1,\dots$ | ${\dfrac{1-p}{p}}$ | ${\dfrac{1-p}{p^2}}$ | Practice 03 Q5 |
| Poisson$(\lambda)$ | ${\lambda}$ | ${\lambda}$ | memorise |
| Uniform$(a,b)$ | ${\dfrac{a+b}{2}}$ | ${\dfrac{(b-a)^2}{12}}$ | Question 2 |
| Exponential$(\lambda)$ | ${\dfrac1\lambda}$ | ${\dfrac{1}{\lambda^2}}$ | Try it 2, Question 3 |
| Gaussian $N(\mu,\sigma^2)$ | ${\mu}$ | ${\sigma^2}$ | Lecture 12 |

**Example: Example 3 · Sensor calibration**

A sensor output $X$ has $E[X]=3$ and $\operatorname{Var}(X)=9$. (a) Find the mean squared error $E[(2-X)^2]$. (b) The reading is calibrated as $Y=2X-3$. Find $\operatorname{Var}(Y)$.

1. (a) **Expand**, then use linearity.

   $$E[(2-X)^2]=E[4-4X+X^2]=4-4E[X]+E[X^2]$$
2. **Turn the shortcut around** to get $E[X^2]$.

   $$E[X^2]=\operatorname{Var}(X)+(E[X])^2=9+9=18$$
3. Substitute.

   $$E[(2-X)^2]=4-12+18=10$$
4. (b) **Shift drops out, scale squares.**

   $$\operatorname{Var}(2X-3)=2^2\cdot9=36$$

**Answer:** (a) $10$ (b) $36$

**Problem: Try it 8 · Given only the mean and variance** (introductory)

A nonnegative random variable $X$ has $E[X]=3$ and $\operatorname{Var}(X)=1$. Find (a) $E[(3X-2)^2]$, (b) $\operatorname{Var}(2X+1)$.

<details><summary>Solution</summary>

1. **Second moment** from the shortcut.

   $$E[X^2]=1+3^2=10$$
2. (a) **Expand** and use linearity.

   $$E[(3X-2)^2]=9E[X^2]-12E[X]+4=90-36+4=58$$
3. (b) **Scale squares, shift drops.**

   $$\operatorname{Var}(2X+1)=4\cdot1=4$$

**Answer:** (a) $58$ (b) $4$

</details>

**Problem: Try it 9 · A Gaussian with mean 12** (intermediate)

$X$ is Gaussian with mean $12$ and variance $4$. (a) Find $c$ with $P(X\ge c)=0.5$. (b) Find $E[X^2]$.

<details><summary>Solution</summary>

1. (a) The bell is **symmetric** about its mean, so half the area is on each side of $12$.

   $$c=\mu=12$$
2. (b) **Turn the shortcut around.**

   $$E[X^2]=\operatorname{Var}(X)+\mu^2=4+144=148$$

**Answer:** (a) $c=12$ (b) $E[X^2]=148$

</details>

**Problem: Try it 10 · Variance of a transformed reading** (intermediate)

For $f_X(x)=\tfrac32x^2$ on $|x|\le1$ (Try it 7: $\operatorname{Var}(X)=\tfrac35$), find $E[3X-1]$ and $\operatorname{Var}(3X-1)$. Also find $E[Y^2]$ for $Y=|X|$.

<details><summary>Solution</summary>

1. **Linearity** with $E[X]=0$.

   $$E[3X-1]=3\cdot0-1=-1$$
2. **Scale squares, shift drops.**

   $$\operatorname{Var}(3X-1)=9\cdot\frac35=\frac{27}{5}$$
3. $Y^2=|X|^2=X^2$, so no new integral is needed.

   $$E[Y^2]=E[X^2]=\frac35$$

**Answer:** $E[3X-1]=-1$, $\operatorname{Var}(3X-1)=\tfrac{27}{5}$, $E[|X|^2]=\tfrac35$.

</details>

## Practice Questions

Test-style questions for Question 3, roughly easy → hard. Solve on paper first, then open the solution.

**Problem: Question 1 · A PMF table with an unknown** (introductory)

$X$ has the PMF below.

| $x$ | $-1$ | $0$ | $1$ | $2$ |
|---|---|---|---|---|
| $p_X(x)$ | $0.1$ | $c$ | $0.3$ | $0.2$ |

Find (a) $c$, (b) $E[X]$ and $\operatorname{Var}(X)$, (c) $E[5-2X]$ and $\operatorname{Var}(5-2X)$.

<details><summary>Solution</summary>

1. (a) **Total = 1.**

   $$0.1+c+0.3+0.2=1\;\Rightarrow\;c=0.4$$
2. (b) **Mean.**

   $$E[X]=-0.1+0+0.3+0.4=0.6$$
3. **Second moment.**

   $$E[X^2]=0.1+0+0.3+0.8=1.2$$
4. **Subtract.**

   $$\operatorname{Var}(X)=1.2-0.36=0.84$$
5. (c) **Linearity**, then **scale squares** (the minus sign disappears).

   $$E[5-2X]=5-1.2=3.8,\quad \operatorname{Var}(5-2X)=4(0.84)=3.36$$

**Answer:** $c=0.4$; $E[X]=0.6$, $\operatorname{Var}(X)=0.84$; $E[5-2X]=3.8$, $\operatorname{Var}(5-2X)=3.36$.

</details>

**Problem: Question 2 · Mean and variance of a uniform** (introductory)

$X$ is uniform on $[a,b]$: $f_X(x)=\dfrac{1}{b-a}$ on $[a,b]$. Show that $E[X]=\dfrac{a+b}{2}$ and $\operatorname{Var}(X)=\dfrac{(b-a)^2}{12}$.

<details><summary>Solution</summary>

1. **Mean.** Use $b^2-a^2=(b-a)(b+a)$.

   $$E[X]=\frac{1}{b-a}\int_a^b x\,dx=\frac{b^2-a^2}{2(b-a)}=\frac{a+b}{2}$$
2. **Second moment.** Use $b^3-a^3=(b-a)(b^2+ab+a^2)$.

   $$E[X^2]=\frac{1}{b-a}\int_a^b x^2\,dx=\frac{b^3-a^3}{3(b-a)}=\frac{a^2+ab+b^2}{3}$$
3. **Subtract** over a common denominator 12.

   $$\begin{gathered}\operatorname{Var}(X)=\frac{4(a^2+ab+b^2)-3(a+b)^2}{12}\\ =\frac{a^2-2ab+b^2}{12}=\frac{(b-a)^2}{12}\end{gathered}$$

**Answer:** $E[X]=\tfrac{a+b}{2}$ (the midpoint), $\operatorname{Var}(X)=\tfrac{(b-a)^2}{12}$.

</details>

**Problem: Question 3 · Variance of an exponential** (intermediate)

$X$ is exponential with parameter $\lambda$: $f_X(x)=\lambda e^{-\lambda x}$ for $x\ge0$. Using $E[X]=\tfrac1\lambda$, find $\operatorname{Var}(X)$ and $\sigma_X$.

<details><summary>Solution</summary>

1. **Second moment** with the shortcut $\int_0^\infty x^n e^{-\lambda x}dx=\frac{n!}{\lambda^{n+1}}$ ($n=2$).

   $$E[X^2]=\lambda\int_0^{\infty}x^2e^{-\lambda x}\,dx=\lambda\cdot\frac{2}{\lambda^3}=\frac{2}{\lambda^2}$$
2. **Subtract.**

   $$\operatorname{Var}(X)=\frac{2}{\lambda^2}-\frac{1}{\lambda^2}=\frac{1}{\lambda^2}$$
3. **Root:** for an exponential, $\sigma$ equals the mean.

   $$\sigma_X=\frac1\lambda$$

**Answer:** $\operatorname{Var}(X)=\tfrac{1}{\lambda^2}$, $\sigma_X=\tfrac1\lambda=E[X]$.

</details>

**Problem: Question 4 · Average power from a random voltage** (intermediate)

A voltage $V$ (in volts) has PDF $f_V(v)=\tfrac{v}{2}$ for $0\le v\le2$, and $0$ otherwise. It is applied across an $8\ \Omega$ resistor, so the power is $P=V^2/8$. Find $E[V]$, $\operatorname{Var}(V)$ and the average power $E[P]$.

<details><summary>Solution</summary>

1. **Mean.**

   $$E[V]=\int_0^2 v\cdot\frac v2\,dv=\frac12\left[\frac{v^3}{3}\right]_0^2=\frac43\text{ V}$$
2. **Second moment.**

   $$E[V^2]=\int_0^2 v^2\cdot\frac v2\,dv=\frac12\left[\frac{v^4}{4}\right]_0^2=2\text{ V}^2$$
3. **Subtract.**

   $$\operatorname{Var}(V)=2-\frac{16}{9}=\frac29\text{ V}^2$$
4. **Power** is a function of $V$: use $E[g(V)]$ and linearity.

   $$E[P]=\frac18E[V^2]=\frac28=0.25\text{ W}$$

**Answer:** $E[V]=\tfrac43$ V, $\operatorname{Var}(V)=\tfrac29$ V², $E[P]=0.25$ W. (Not $(E[V])^2/8\approx0.22$ W.)

</details>

**Problem: Question 5 · Average run of good pixels · Tutorial 6 Q7** (intermediate)

Pixels arrive one after another; each is corrupted independently with probability $p=0.03$. $N$ = number of error-free pixels between two erroneous ones, so $P(N=k)=(1-p)^k p$, $k=0,1,2,\dots$ Find $E[N]$.

<details><summary>Solution</summary>

1. **Set up** the sum, with $q=1-p$.

   $$E[N]=\sum_{k=0}^{\infty}k\,q^k p=p\sum_{k=1}^{\infty}k\,q^k$$
2. **Series fact:** differentiate $\sum q^k=\frac{1}{1-q}$ and multiply by $q$.

   $$\sum_{k=1}^{\infty}k\,q^k=\frac{q}{(1-q)^2}=\frac{q}{p^2}$$
3. **Combine.**

   $$E[N]=p\cdot\frac{q}{p^2}=\frac{1-p}{p}$$
4. **Plug in** $p=0.03$.

   $$E[N]=\frac{0.97}{0.03}\approx32.33$$

**Answer:** $E[N]=\dfrac{1-p}{p}\approx 32.33$ good pixels between errors.

</details>

**Problem: Question 6 · A sensor that saturates** (intermediate)

A sensor reading $X$ saturates: with probability $0.3$ it reads exactly $X=5$; otherwise (probability $0.7$) it is uniform on $(0,5)$, so the continuous part has density $0.7\cdot\tfrac15=0.14$ on $(0,5)$. Find $E[X]$ and $\operatorname{Var}(X)$.

<details><summary>Solution</summary>

1. **Mean:** point mass + integral.

   $$\begin{gathered}E[X]=5(0.3)+\int_0^5x(0.14)\,dx\\ =1.5+0.14\cdot\frac{25}{2}=1.5+1.75=3.25\end{gathered}$$
2. **Second moment:** same split, with $x^2$.

   $$E[X^2]=25(0.3)+\int_0^5x^2(0.14)\,dx=7.5+0.14\cdot\frac{125}{3}=\frac{40}{3}$$
3. **Subtract.**

   $$\operatorname{Var}(X)=\frac{40}{3}-3.25^2=\frac{133}{48}\approx2.771$$

**Answer:** $E[X]=3.25$, $\operatorname{Var}(X)=\tfrac{133}{48}\approx2.771$.

</details>

**Problem: Question 7 · Mars canisters · Practice 03 Q6** (intermediate)

A rover returns 560 g of material in four canisters A, B, C, D holding $140$, $112$, $125$ and $183$ g. First a **canister** is chosen at random (each $\tfrac14$); $x$ = grams in it. Then a **1-gram sample** is chosen at random from all 560 g; $y$ = grams in the canister it came from. (a) Which of $E[x]$, $E[y]$ should be larger, and why? (b) Compute both.

<details><summary>Solution</summary>

1. (a) For $y$, a canister is picked with probability **proportional to its mass**, so heavy canisters count more. Expect $E[y]>E[x]$.

   $$P(y=m)=\frac{m}{560}$$
2. (b) **$E[x]$:** equal weights.

   $$E[x]=\frac14(140+112+125+183)=140\text{ g}$$
3. **$E[y]$:** weight each mass $m$ by $\frac{m}{560}$.

   $$E[y]=\frac{140^2+112^2+125^2+183^2}{560}=\frac{81258}{560}$$
4. Evaluate.

   $$E[y]\approx145.10\text{ g}>140\text{ g}$$

**Answer:** $E[x]=140$ g, $E[y]\approx 145.10$ g. Sampling by gram favours the big canisters.

</details>

**Problem: Question 8 · Triangle PDF** (intermediate)

$X$ has the triangular PDF $f_X(x)=x$ on $[0,1]$, $f_X(x)=2-x$ on $[1,2]$, and $0$ otherwise. Find $E[X]$, $\operatorname{Var}(X)$, and $\operatorname{Var}(2X+3)$.

<details><summary>Solution</summary>

1. **Mean:** the triangle is symmetric about $x=1$.

   $$E[X]=1$$
2. **Second moment:** split the integral at $x=1$.

   $$E[X^2]=\int_0^1x^3\,dx+\int_1^2x^2(2-x)\,dx$$
3. Integrate each piece.

   $$=\frac14+\left[\frac{2x^3}{3}-\frac{x^4}{4}\right]_1^2=\frac14+\frac{11}{12}=\frac76$$
4. **Subtract.**

   $$\operatorname{Var}(X)=\frac76-1=\frac16$$
5. **Scale squares.**

   $$\operatorname{Var}(2X+3)=4\cdot\frac16=\frac23$$

**Answer:** $E[X]=1$, $\operatorname{Var}(X)=\tfrac16$, $\operatorname{Var}(2X+3)=\tfrac23$.

</details>

**Problem: Question 9 · The mean from the CDF · Tutorial 5 Q3 / Practice 03 Q1** (advanced)

For a **nonnegative** continuous $X$ with CDF $F_X$, show that $E[X]=\displaystyle\int_0^{\infty}\big(1-F_X(t)\big)\,dt$ (assume $t\,(1-F_X(t))\to0$ as $t\to\infty$). Then use it to find the mean of an exponential.

<details><summary>Solution</summary>

1. **By parts** with $u=1-F_X(t)$ and $dv=dt$: then $du=-f_X(t)\,dt$ and $v=t$.

   $$\int_0^{\infty}(1-F_X(t))\,dt=\Big[t\,(1-F_X(t))\Big]_0^{\infty}+\int_0^{\infty}t\,f_X(t)\,dt$$
2. The boundary term is $0$ at both ends (given at $\infty$; $t=0$ at the bottom).

   $$=0+E[X]$$
3. **Exponential:** $1-F_X(t)=e^{-\lambda t}$.

   $$E[X]=\int_0^{\infty}e^{-\lambda t}\,dt=\frac1\lambda$$

**Answer:** Shown; for the exponential $E[X]=\tfrac1\lambda$ with no by-parts on $x e^{-\lambda x}$.

</details>

**Problem: Question 10 · Find the constants, then the variance · Tutorial 6 Q6** (advanced)

$X$ has PDF

$$
f_X(x)=\frac{C}{1+(x+K)^2},\qquad -K-1\le x\le -K+1,
$$

and $0$ otherwise, where $C>0$ and $K$ are constants. (a) Find $C$ and $K$ so that $E[X]=5$. (b) Find $\operatorname{Var}(X)$.

<details><summary>Solution</summary>

1. **Shift:** let $u=x+K$, so $u\in[-1,1]$ and $X=U-K$ with $f_U(u)=\frac{C}{1+u^2}$.

   $$\int_{-1}^{1}\frac{C}{1+u^2}\,du=C\big[\arctan u\big]_{-1}^{1}=C\cdot\frac{\pi}{2}$$
2. (a) **Total area = 1.**

   $$C=\frac{2}{\pi}$$
3. $f_U$ is **even**, so $E[U]=0$. Then use linearity.

   $$E[X]=E[U]-K=-K=5\;\Rightarrow\;K=-5$$
4. (b) A shift does not change Var, and $E[U]=0$.

   $$\operatorname{Var}(X)=\operatorname{Var}(U)=E[U^2]$$
5. Write $\frac{u^2}{1+u^2}=1-\frac{1}{1+u^2}$.

   $$E[U^2]=\frac2\pi\int_{-1}^{1}\Big(1-\frac{1}{1+u^2}\Big)du=\frac2\pi\Big(2-\frac\pi2\Big)$$
6. Simplify.

   $$\operatorname{Var}(X)=\frac4\pi-1\approx0.2732$$

**Answer:** (a) $C=\tfrac2\pi$, $K=-5$ (so $X\in[4,6]$) (b) $\operatorname{Var}(X)=\tfrac4\pi-1\approx0.2732$

</details>
