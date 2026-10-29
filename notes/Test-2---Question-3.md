# Test 2 - Question 3

**Lectures 11–13.** The mean (the long-run average) and the variance (the spread) of a random variable.

## Question 3 in plain words

**You’ll see:** a PMF, a PDF, a CDF, a named family, or just “$E[X]=3$, $\operatorname{Var}(X)=9$”. Then “find $E[X]$, $\operatorname{Var}(X)$, $\sigma_X$”.

**The move: four steps, every time.**

1. **Mean:** each value × its chance, then add (a sum for a PMF, an integral for a PDF).
2. **Square:** the same, with $x^2$ in place of $x$. That’s $E[X^2]$.
3. **Subtract:** $\operatorname{Var}(X)=E[X^2]-(E[X])^2$.
4. **Root:** $\sigma_X=\sqrt{\operatorname{Var}(X)}$.

$$E[X]=\sum_x x\,p_X(x)\quad\text{or}\quad\int x\,f_X(x)\,dx,\qquad \operatorname{Var}(X)=E[X^2]-\big(E[X]\big)^2$$

**Short example:** a die. $E[X]=3.5$, $E[X^2]=\tfrac{91}{6}$:

$$\operatorname{Var}(X)=\frac{91}{6}-3.5^2=\frac{35}{12}\approx2.92,\qquad \sigma_X\approx1.71$$

**Which case?**

| You’re given… | Go to |
|---|---|
| a PMF (a list of values and chances) | Case 1 |
| a PDF $f_X(x)$ | Case 2 |
| a CDF $F_X(x)$ | Case 3 |
| “$X$ is Poisson / uniform / …” | Case 4 |
| only $E[X]$ and $\operatorname{Var}(X)$ | Case 5 |

> **Warning:** **$E[X^2]\ne(E[X])^2$.** Square **inside** the sum or integral, not after. A die: $E[X^2]=\tfrac{91}{6}\approx15.17$, but $3.5^2=12.25$.

## Case 1: from a PMF

**You’ll see:** a table of values and chances, or an experiment you turn into one.

$$E[X]=\sum_x x\,p_X(x),\qquad E[X^2]=\sum_x x^2\,p_X(x)$$

**Short example** (Lecture 12): $X=4$ V or $6$ V, each half the time:

$$E[X]=4(0.5)+6(0.5)=5,\qquad E[X^2]=16(0.5)+36(0.5)=26$$

$$\operatorname{Var}(X)=26-5^2=1\ \text{V}^2,\qquad \sigma_X=1\ \text{V}$$

<details><summary>Full example (Lecture 11): a fair die, $\;X$ = the number</summary>

Step 1 · **Mean:** each face has chance $\tfrac16$.

$$
E[X]=\frac16(1+2+3+4+5+6)=\frac{21}{6}=3.5
$$

Step 2 · **Square:** square each value **inside** the sum.

$$
E[X^2]=\frac16(1+4+9+16+25+36)=\frac{91}{6}
$$

Step 3 · **Subtract.**

$$
\operatorname{Var}(X)=\frac{91}{6}-\Big(\frac72\Big)^2=\frac{182-147}{12}=\frac{35}{12}
$$

Step 4 · **Root.**

$$
\sigma_X=\sqrt{35/12}\approx1.71
$$

**Answer:**

$$
E[X]=3.5,\quad \operatorname{Var}(X)=\frac{35}{12},\quad \sigma_X\approx1.71
$$

</details>

<details><summary>Any function: $\;E[g(X)]=\sum g(x)\,p_X(x)$</summary>

Put $g(x)$ in place of $x$. Example: a voltage $X=4$ or $6$ V (half each) across $R=2\ \Omega$: average power $E[X^2/R]$.

$$
E\Big[\frac{X^2}{2}\Big]=\frac{16}{2}(0.5)+\frac{36}{2}(0.5)=13\ \text{W}
$$

</details>

**Problem: Try it 1 · Case 1 · A binary random variable · Tutorial 5 Q1** (introductory)

$X$ is $0$ with probability $p$ and $1$ with probability $1-p$. Find $E[X]$, $\operatorname{Var}(X)$ and $E[X^5]$.

<details><summary>Solution</summary>

1. **Spot:** a PMF with two values → Case 1.
2. **Mean.**

   $$E[X]=0\cdot p+1\cdot(1-p)=1-p$$
3. **Square:** $0^n=0$ and $1^n=1$, so $X^n=X$ for any power.

   $$E[X^2]=E[X^5]=E[X]=1-p$$
4. **Subtract.**

   $$\operatorname{Var}(X)=(1-p)-(1-p)^2=(1-p)\,p$$

**Answer:** $E[X]=1-p$, $\operatorname{Var}(X)=p(1-p)$, $E[X^5]=1-p$.

</details>

## Case 2: from a PDF

**You’ll see:** a formula $f_X(x)$. Same four steps, with integrals over the range where $f_X\ne0$:

$$E[X]=\int x\,f_X(x)\,dx,\qquad E[X^2]=\int x^2\,f_X(x)\,dx$$

**Short example:** $X$ uniform on $[0,2]$, $f_X=\tfrac12$:

$$E[X]=\int_0^2\frac x2\,dx=1,\qquad E[X^2]=\int_0^2\frac{x^2}{2}\,dx=\frac43$$

$$\operatorname{Var}(X)=\frac43-1=\frac13$$

<details><summary>Full example (Practice 03 Q2): exponential, $\;f_X(t)=\lambda e^{-\lambda t}$, $t\ge0$</summary>

Step 1 · **Mean:** integrate over $t\ge0$. Use the shortcut card below with $n=1$.

$$
E[X]=\lambda\int_0^{\infty}t\,e^{-\lambda t}\,dt=\lambda\cdot\frac{1!}{\lambda^2}=\frac1\lambda
$$

Step 2 · **Square:** the shortcut with $n=2$.

$$
E[X^2]=\lambda\cdot\frac{2!}{\lambda^3}=\frac{2}{\lambda^2}
$$

Step 3 · **Subtract.**

$$
\operatorname{Var}(X)=\frac{2}{\lambda^2}-\frac{1}{\lambda^2}=\frac{1}{\lambda^2}
$$

Step 4 · **Root.** (3 customers per minute → mean gap $\tfrac13$ min.)

$$
\sigma_X=\frac1\lambda
$$

**Answer:**

$$
E[X]=\frac1\lambda,\qquad \operatorname{Var}(X)=\frac{1}{\lambda^2}
$$

</details>

<details><summary>Shortcut: $\;\displaystyle\int_0^{\infty}x^n\,e^{-\lambda x}\,dx=\frac{n!}{\lambda^{n+1}}$</summary>

Skips integrating by parts. $n=1$:

$$
\int_0^\infty x\,e^{-2x}\,dx=\frac{1}{4}
$$

$n=2$:

$$
\int_0^\infty x^2\,e^{-x}\,dx=\frac{2}{1}=2
$$

</details>

<details><summary>Shortcut: a symmetric PDF → the mean is the centre</summary>

If $f_X$ looks the same on both sides of $c$, then $E[X]=c$. No integral.

$$
f_X(t)=\tfrac12\lambda e^{-\lambda|t-\gamma|}\quad\Longrightarrow\quad E[X]=\gamma
$$

Same reason: an odd function ($x$, $x^3$) integrated over $[-a,a]$ gives $0$.

$$
\int_{-1}^{1}x\cdot\frac32x^2\,dx=0
$$

</details>

<details><summary>Mixed $X$ (a jump and a density): add both parts</summary>

Step 1 · Lecture 11 signal: $X=0$ with chance $0.2$, otherwise uniform on $(0,10)$, density $0.08$.

Step 2 · **Mean**, jump part.

$$
0\cdot0.2=0
$$

Step 3 · **Mean**, density part.

$$
\int_0^{10}x\,(0.08)\,dx=0.08\cdot\frac{10^2}{2}=4
$$

Step 4 · Add.

$$
E[X]=0+4=4
$$

</details>

## Case 3: from a CDF

**You’ll see:** $F_X(x)$ instead of a PMF or PDF. Turn it into one, then Case 1 or 2:

- **Staircase CDF** (discrete): the **jump sizes** are the PMF → Case 1.
- **Smooth CDF** (continuous): the **slope** is the PDF, $f_X=F_X^{\prime}$ → Case 2.

**Shortcut for $X\ge0$** (the tail formula): skip the PDF.

$$E[X]=\int_0^{\infty}\big(1-F_X(t)\big)\,dt\qquad\qquad E[N]=\sum_{k=0}^{\infty}P(N>k)\ \ (\text{whole numbers})$$

**Short example:** exponential, $1-F_X(t)=e^{-\lambda t}$:

$$E[X]=\int_0^{\infty}e^{-\lambda t}\,dt=\frac1\lambda$$

<details><summary>Full example: $\;F_X(x)=x^2$ on $[0,1]$. Find $E[X]$ two ways</summary>

Step 1 · **Way 1:** the slope is the PDF.

$$
f_X(x)=2x,\qquad 0\le x\le1
$$

Step 2 · **Mean** from the PDF.

$$
E[X]=\int_0^1x\cdot2x\,dx=\frac23
$$

Step 3 · **Way 2:** the tail formula. $1-F=0$ after $x=1$.

$$
E[X]=\int_0^1(1-t^2)\,dt=1-\frac13=\frac23
$$

**Answer:**

$$
E[X]=\frac23\ \text{ both ways}
$$

</details>

## Case 4: a named family (read it off)

**You’ll see:** “$X$ is Binomial / Poisson / uniform / …”. Don’t integrate: each family’s mean and variance are known. Open a card:

<details><summary>Bernoulli$(p)$: $\;E=p$, $\;\operatorname{Var}=p(1-p)$</summary>

One yes/no try, $1$ with chance $p$. Example $p=0.3$:

$$
E[X]=0.3,\qquad \operatorname{Var}(X)=0.3\cdot0.7=0.21
$$

</details>

<details><summary>Binomial$(n,p)$: $\;E=np$, $\;\operatorname{Var}=np(1-p)$</summary>

$n$ tries, count successes. Example $n=10$, $p=0.3$:

$$
E[X]=3,\qquad \operatorname{Var}(X)=10(0.3)(0.7)=2.1
$$

</details>

<details><summary>Geometric: $\;E=\dfrac1p$ (or $\dfrac{1-p}{p}$), $\;\operatorname{Var}=\dfrac{1-p}{p^2}$</summary>

Counting tries until the first success ($k=1,2,\dots$):

$$
E[X]=\frac1p
$$

Counting failures before it ($k=0,1,\dots$), one less:

$$
E[N]=\frac1p-1=\frac{1-p}{p}
$$

Same variance both ways. Example $p=0.2$, tries:

$$
E[X]=5,\qquad \operatorname{Var}(X)=\frac{0.8}{0.04}=20
$$

</details>

<details><summary>Poisson$(\lambda)$: $\;E=\lambda$, $\;\operatorname{Var}=\lambda$</summary>

Mean and variance are the same number. Example $\lambda=3$:

$$
E[X]=3,\qquad \operatorname{Var}(X)=3
$$

</details>

<details><summary>Uniform$(a,b)$: $\;E=\dfrac{a+b}{2}$, $\;\operatorname{Var}=\dfrac{(b-a)^2}{12}$</summary>

The middle, and the length squared over 12. Example $U(2,8)$:

$$
E[X]=5,\qquad \operatorname{Var}(X)=\frac{36}{12}=3
$$

</details>

<details><summary>Exponential$(\lambda)$: $\;E=\dfrac1\lambda$, $\;\operatorname{Var}=\dfrac{1}{\lambda^2}$</summary>

Example $\lambda=0.25$ per minute:

$$
E[X]=4\text{ min},\qquad \operatorname{Var}(X)=16
$$

</details>

<details><summary>Gaussian $N(\mu,\sigma^2)$: $\;E=\mu$, $\;\operatorname{Var}=\sigma^2$</summary>

Already in the name. Example $N(12,4)$:

$$
E[X]=12,\qquad \sigma_X=2
$$

</details>

**Need $E[X^2]$?** Turn the variance around:

$$E[X^2]=\operatorname{Var}(X)+\big(E[X]\big)^2\qquad\text{Poisson}(3):\ E[X^2]=3+9=12$$

**Problem: Try it 2 · Case 4 · Three families** (introductory)

(a) $X\sim$ Binomial$(10,\,0.3)$: find $E[X]$ and $\operatorname{Var}(X)$. (b) $X\sim$ Uniform$(2,8)$: find $\operatorname{Var}(X)$ and $\sigma_X$. (c) $X\sim$ Poisson$(3)$: find $E[(X-1)^2]$.

<details><summary>Solution</summary>

1. (a) **Spot:** Binomial → $np$ and $np(1-p)$.

   $$E[X]=10(0.3)=3,\qquad \operatorname{Var}(X)=10(0.3)(0.7)=2.1$$
2. (b) **Spot:** uniform → $\frac{(b-a)^2}{12}$. **Root.**

   $$\operatorname{Var}(X)=\frac{6^2}{12}=3,\qquad \sigma_X=\sqrt3\approx1.732$$
3. (c) **Spot:** Poisson. **Swap:** $E[X^2]=\lambda+\lambda^2=12$. **Expand** (Case 5).

   $$E[(X-1)^2]=E[X^2]-2E[X]+1=12-6+1=7$$

**Answer:** (a) $3$, $2.1$ (b) $3$, $\sqrt3\approx1.732$ (c) $7$

</details>

## Case 5: only E[X] and Var(X) given (the rules)

**You’ll see:** “$E[X]=3$, $\operatorname{Var}(X)=9$. Find $E[(2-X)^2]$” or “find $\operatorname{Var}(2X-3)$”. No PMF or PDF needed.

**The move:** two rules.

$$E[aX+b]=a\,E[X]+b\qquad\qquad \operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$$

1. **Expand** any square, like $(2-X)^2$, then take $E$ of each term.
2. **Swap** in $E[X^2]=\operatorname{Var}(X)+(E[X])^2$ wherever $E[X^2]$ appears.
3. **Plug in.** For Var: the $+b$ drops out, the $a$ gets squared.

**Short example:** $\operatorname{Var}(X)=9$:

$$\operatorname{Var}(2X-3)=2^2\cdot9=36,\qquad \operatorname{Var}(-X)=\operatorname{Var}(X),\qquad \sigma_{aX+b}=|a|\,\sigma_X$$

<details><summary>Full example (Lecture 13): $\;E[X]=3$, $\;\operatorname{Var}(X)=9$. Find $E[(2-X)^2]$ and $\operatorname{Var}(2X-3)$</summary>

Step 1 · **Expand**, then take $E$ of each term.

$$
E[(2-X)^2]=E[4-4X+X^2]=4-4E[X]+E[X^2]
$$

Step 2 · **Swap** for $E[X^2]$.

$$
E[X^2]=9+3^2=18
$$

Step 3 · **Plug in.**

$$
E[(2-X)^2]=4-12+18=10
$$

Step 4 · Var: the $-3$ drops out, the $2$ gets squared.

$$
\operatorname{Var}(2X-3)=2^2\cdot9=36
$$

**Answer:**

$$
E[(2-X)^2]=10,\qquad \operatorname{Var}(2X-3)=36
$$

</details>

<details><summary>Moments: $\;E[X^n]$ (raw), $\;E[(X-\mu)^n]$ (central)</summary>

The $n$th moment is $E[X^n]$: $E[X]$ is the 1st, $E[X^2]$ the 2nd.

The variance is the 2nd **central** moment: distances from the mean.

$$
\operatorname{Var}(X)=E\big[(X-\mu_X)^2\big]
$$

</details>

<details><summary>Chebyshev and Markov (Practice 03, not in the lectures)</summary>

**Chebyshev:** far from the mean is unlikely when the variance is small.

$$
P\big(|Y-\mu_Y|\ge\varepsilon\big)\le\frac{\operatorname{Var}(Y)}{\varepsilon^2}
$$

Example: $\operatorname{Var}=1$, $\varepsilon=2$.

$$
P\big(|Y-\mu|\ge2\big)\le\frac14
$$

**Markov**, for $Y\ge0$:

$$
P(Y\ge a)\le\frac{E[Y]}{a}
$$

</details>

**Problem: Try it 3 · Case 5 · Given only the mean and variance · Tutorial 5 Q2** (introductory)

$X\ge0$ has $E[X]=3$ and $\operatorname{Var}(X)=1$. Find (a) $E[(3X-2)^2]$, (b) $\operatorname{Var}(2X+1)$.

<details><summary>Solution</summary>

1. **Spot:** only $E$ and Var → Case 5. **Swap** first.

   $$E[X^2]=1+3^2=10$$
2. (a) **Expand**, then take $E$ of each term.

   $$E[(3X-2)^2]=9E[X^2]-12E[X]+4$$
3. **Plug in.**

   $$9(10)-12(3)+4=58$$
4. (b) The $+1$ drops out, the $2$ gets squared.

   $$\operatorname{Var}(2X+1)=4\cdot1=4$$

**Answer:** (a) $58$ (b) $4$

</details>

## Practice Questions

> **Tip:** **Question 3 is always these cases, in parts (a)–(c).** Run **Mean → Square → Subtract → Root**:
> 
> 1. **PMF:** $\sum x\,p$ and $\sum x^2p$.
> 2. **PDF:** $\int x\,f$ and $\int x^2f$ (symmetric → mean = centre; $\int_0^\infty x^ne^{-\lambda x}=\frac{n!}{\lambda^{n+1}}$).
> 3. **CDF:** jumps → PMF, slope → PDF; or the tail formula for $X\ge0$.
> 4. **Named family:** read the card.
> 5. **Only $E$ and Var:** Expand → Swap $E[X^2]=\text{Var}+\mu^2$ → Plug in; $\text{Var}(aX+b)=a^2\text{Var}(X)$.

Test-style, easy → hard. Solve on paper first, then open the solution.

**Problem: Question 1 · Case 1 + 5 · PMF table** (introductory)

$X$ has the PMF below.

| $x$ | $-1$ | $0$ | $1$ | $2$ |
|---|---|---|---|---|
| $p_X(x)$ | $0.1$ | $c$ | $0.3$ | $0.2$ |

Find (a) $c$, (b) $E[X]$ and $\operatorname{Var}(X)$, (c) $E[5-2X]$ and $\operatorname{Var}(5-2X)$.

<details><summary>Solution</summary>

1. (a) **Find $c$:** the chances add to $1$.

   $$0.1+c+0.3+0.2=1\quad\Longrightarrow\quad c=0.4$$
2. (b) **Type:** a PMF → Case 1. **Mean.**

   $$E[X]=-1(0.1)+0+1(0.3)+2(0.2)=0.6$$
3. **Square.**

   $$E[X^2]=1(0.1)+0+1(0.3)+4(0.2)=1.2$$
4. **Subtract.**

   $$\operatorname{Var}(X)=1.2-0.6^2=0.84$$
5. (c) **Rules** (Case 5): the $5$ drops out of Var, the $-2$ gets squared.

   $$\begin{gathered}E[5-2X]=5-2(0.6)=3.8 \\ \operatorname{Var}(5-2X)=4(0.84)=3.36\end{gathered}$$

**Answer:** $c=0.4$; $E[X]=0.6$, $\operatorname{Var}(X)=0.84$; $E[5-2X]=3.8$, $\operatorname{Var}(5-2X)=3.36$.

</details>

**Problem: Question 2 · Case 4 + 5 · Gaussian · Tutorial 5 Q4** (introductory)

$X$ is normal with mean $12$ and variance $4$. (a) Find $c$ so that $P(X\ge c)=0.5$. (b) Find $E[X^2]$.

<details><summary>Solution</summary>

1. **Type:** named family (Gaussian) → Case 4: $E[X]=12$, $\operatorname{Var}(X)=4$.
2. (a) The bell is symmetric around its mean, so half the area is above $12$.

   $$c=\mu=12$$
3. (b) **Swap** (Case 5).

   $$E[X^2]=\operatorname{Var}(X)+\mu^2=4+144=148$$

**Answer:** (a) $c=12$ (b) $E[X^2]=148$

</details>

**Problem: Question 3 · Case 5 · Prove the Var rule · Practice 03 Q4** (introductory)

Show that $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$ for any constants $a,b$. Use $\operatorname{Var}(Y)=E\big[(Y-E[Y])^2\big]$.

<details><summary>Solution</summary>

1. **Mean** of $Y=aX+b$, with the first rule.

   $$E[Y]=a\,E[X]+b$$
2. **Subtract** it from $Y$: the $b$ cancels.

   $$Y-E[Y]=aX+b-a\,E[X]-b=a\,(X-E[X])$$
3. **Square** and take $E$: the constant $a^2$ comes out.

   $$\begin{gathered}\operatorname{Var}(Y)=E\big[a^2(X-E[X])^2\big] \\ =a^2\,E\big[(X-E[X])^2\big]=a^2\operatorname{Var}(X)\end{gathered}$$

**Answer:** Shown: $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$, so $\sigma_{aX+b}=|a|\sigma_X$.

</details>

**Problem: Question 4 · Case 1 · Mars canisters · Practice 03 Q6** (intermediate)

A rover brings back 560 g of material in four canisters A, B, C, D holding $140$, $112$, $125$ and $183$ g. First, pick a **canister** at random (each $\tfrac14$); $x$ = grams in it. Then, pick **one gram** at random from all 560 g; $y$ = grams in the canister it came from. (a) Which should be larger, $E[x]$ or $E[y]$? Why? (b) Compute both.

<details><summary>Solution</summary>

1. **Type:** two PMFs → Case 1. The difference is the chances.
2. (a) A random gram lands in a big canister more often: each canister gets chance (its mass)/560. So expect $E[y]>E[x]$.

   $$P(y=m)=\frac{m}{560}$$
3. (b) **Mean** of $x$: equal chances.

   $$E[x]=\frac14(140+112+125+183)=140\text{ g}$$
4. **Mean** of $y$: each mass $m$ times its chance $\frac{m}{560}$.

   $$E[y]=\frac{140^2+112^2+125^2+183^2}{560}=\frac{81258}{560}\approx145.10\text{ g}$$

**Answer:** $E[x]=140$ g, $E[y]\approx 145.10$ g. Picking by the gram favours the big canisters.

</details>

**Problem: Question 5 · Case 2 + 5 · $E[g(X)]$ from a PDF · Tutorial 5 Q5** (intermediate)

$f_X(x)=Cx^2$ for $|x|\le1$, and $0$ otherwise. (a) Find $C$. (b) Find $E[X]$ and $\operatorname{Var}(X)$. (c) Let $Y=|X|$. Find $E[Y]$, $E[Y^2]$ and $\operatorname{Var}(3X-1)$.

<details><summary>Solution</summary>

1. (a) **Find $c$:** total area $=1$.

   $$\int_{-1}^{1}Cx^2\,dx=\frac{2C}{3}=1\quad\Longrightarrow\quad C=\frac32$$
2. (b) **Type:** a PDF → Case 2. **Mean:** symmetric around $0$ (shortcut).

   $$E[X]=0$$
3. **Square.**

   $$E[X^2]=\int_{-1}^{1}\frac32x^4\,dx=\frac32\cdot\frac25=\frac35$$
4. **Subtract.**

   $$\operatorname{Var}(X)=\frac35-0^2=\frac35$$
5. (c) $E[g(X)]$ with $g(x)=|x|$. Both halves match, so double the right half.

   $$E[Y]=2\int_0^1 x\cdot\frac32x^2\,dx=3\cdot\frac14=\frac34$$
6. $|X|^2=X^2$, so no new work.

   $$E[Y^2]=E[X^2]=\frac35$$
7. **Rules** (Case 5): the $-1$ drops out, the $3$ gets squared.

   $$\operatorname{Var}(3X-1)=9\cdot\frac35=\frac{27}{5}$$

**Answer:** (a) $C=\tfrac32$ (b) $E[X]=0$, $\operatorname{Var}(X)=\tfrac35$ (c) $E[Y]=\tfrac34$, $E[Y^2]=\tfrac35$, $\operatorname{Var}(3X-1)=\tfrac{27}5$

</details>

**Problem: Question 6 · Case 3 · Variance from a CDF · Practice 03 Q9** (intermediate)

Find the variance and standard deviation of $X$, and say if $X$ is discrete or continuous:

$$
F(x)=\begin{cases}0,&x<-3\\ 3/8,&-3\le x<0\\ 3/4,&0\le x<6\\ 1,&x\ge6\end{cases}
$$

<details><summary>Solution</summary>

1. **Type:** a CDF → Case 3. It’s a staircase, so discrete: the **jump sizes** are the PMF.

   $$p(-3)=\frac38,\quad p(0)=\frac38,\quad p(6)=\frac14$$
2. **Mean.**

   $$E[X]=-3\cdot\frac38+0+6\cdot\frac14=-\frac98+\frac{12}8=\frac38$$
3. **Square.**

   $$E[X^2]=9\cdot\frac38+0+36\cdot\frac14=\frac{27}8+9=\frac{99}8$$
4. **Subtract.**

   $$\operatorname{Var}(X)=\frac{99}8-\frac9{64}=\frac{783}{64}\approx12.234$$
5. **Root.**

   $$\sigma_X\approx3.498$$

**Answer:** Discrete; $\operatorname{Var}(X)=\tfrac{783}{64}\approx 12.234$, $\sigma_X\approx 3.498$

</details>

**Problem: Question 7 · Case 2 · Mean by symmetry, then Var · Practice 03 Q3** (intermediate)

$X$ has PDF $f_X(t)=\tfrac12\lambda e^{-\lambda|t-\gamma|}$ for all $t$. (a) Find $E[X]$. (b) Find $\operatorname{Var}(X)$.

<details><summary>Solution</summary>

1. **Type:** a PDF → Case 2. (a) **Mean:** symmetric around $t=\gamma$ (same value at $\gamma\pm u$).

   $$E[X]=\gamma$$
2. (b) Use the definition $E[(X-\gamma)^2]$. Let $u=t-\gamma$; both halves match, so double the right half.

   $$\operatorname{Var}(X)=2\int_0^{\infty}u^2\cdot\frac12\lambda e^{-\lambda u}\,du=\lambda\int_0^{\infty}u^2e^{-\lambda u}\,du$$
3. **Shortcut** with $n=2$.

   $$=\lambda\cdot\frac{2!}{\lambda^3}=\frac{2}{\lambda^2}$$

**Answer:** (a) $E[X]=\gamma$ (b) $\operatorname{Var}(X)=\dfrac2{\lambda^2}$

</details>

**Problem: Question 8 · Case 4 · Geometric · Tutorial 6 Q7** (intermediate)

Spirit sends an image pixel by pixel. Each pixel is wrong with probability $p=0.03$, independently. (a) Find the PMF of $N$, the number of good pixels before the next bad one. (b) Find $E[N]$. (c) A new rover needs a 99% chance that **at least 1000** pixels arrive correctly before a bad one. How small must $p$ be?

<details><summary>Solution</summary>

1. (a) **Spot:** $k$ good pixels, then a bad one → Geometric, counting failures ($k=0,1,\dots$).

   $$P(N=k)=(1-p)^k\,p=(0.97)^k(0.03),\quad k=0,1,2,\dots$$
2. (b) **Read it off** the Geometric card (failures version).

   $$E[N]=\frac{1-p}{p}=\frac{0.97}{0.03}\approx32.33$$
3. (c) “At least 1000 good first” means the first 1000 pixels are all good.

   $$P(N\ge1000)=(1-p)^{1000}\ge0.99$$
4. Solve for $p$.

   $$p\le1-0.99^{1/1000}\approx1.01\times10^{-5}$$

**Answer:** (a) $(0.97)^k(0.03)$ (b) $E[N]\approx 32.33$ (c) $p\le 1.01\times10^{-5}$

</details>

**Problem: Question 9 · Case 3 · The mean from the CDF · Practice 03 Q1 / Tutorial 5 Q3** (advanced)

(a) $X\ge0$ is continuous with CDF $F_X$. Show that $E[X]=\displaystyle\int_0^{\infty}\big(1-F_X(t)\big)\,dt$ (assume $t\,(1-F_X(t))\to0$ as $t\to\infty$). Use it to find the mean of an exponential. (b) Use the whole-number version $E[N]=\sum_{k\ge0}P(N>k)$ to find the mean of a Geometric$(p)$ on $k=1,2,\dots$

<details><summary>Solution</summary>

1. (a) **By parts:** $u=1-F_X(t)$, $dv=dt$, so $du=-f_X(t)\,dt$ and $v=t$.

   $$\int_0^{\infty}(1-F_X(t))\,dt=\Big[t\,(1-F_X(t))\Big]_0^{\infty}+\int_0^{\infty}t\,f_X(t)\,dt$$
2. The bracket is $0$ at both ends.

   $$=0+E[X]$$
3. **Exponential:** $1-F_X(t)=e^{-\lambda t}$.

   $$E[X]=\int_0^{\infty}e^{-\lambda t}\,dt=\frac1\lambda$$
4. If $X$ can be negative (Tutorial 5 Q3), the same by-parts on $(-\infty,0]$ subtracts one more piece.

   $$E[X]=\int_0^{\infty}(1-F_X)\,dt-\int_{-\infty}^{0}F_X\,dt$$
5. (b) $N>k$ means the first $k$ tries failed. Geometric series.

   $$E[N]=\sum_{k=0}^{\infty}(1-p)^k=\frac{1}{1-(1-p)}=\frac1p$$

**Answer:** (a) Shown; exponential mean $\tfrac1\lambda$ (b) $E[N]=\tfrac1p$

</details>

**Problem: Question 10 · Case 2 + 5 · Find the constants, then the variance · Tutorial 6 Q6** (advanced)

$X$ has PDF

$$
f_X(x)=\frac{C}{1+(x+K)^2},\qquad -K-1\le x\le -K+1,
$$

and $0$ otherwise, where $C>0$ and $K$ are constants. (a) Find $C$ and $K$ so that $E[X]=5$. (b) Find $\operatorname{Var}(X)$.

<details><summary>Solution</summary>

1. **Shift:** let $u=x+K$, so $u$ runs from $-1$ to $1$.

   $$f_U(u)=\frac{C}{1+u^2},\qquad X=U-K$$
2. (a) **Find $c$:** total area $=1$.

   $$C\big[\arctan u\big]_{-1}^{1}=C\cdot\frac{\pi}{2}=1\quad\Longrightarrow\quad C=\frac{2}{\pi}$$
3. **Mean:** $f_U$ is symmetric around $0$, so $E[U]=0$. Then the rule $E[U-K]=E[U]-K$.

   $$E[X]=-K=5\quad\Longrightarrow\quad K=-5$$
4. (b) A shift doesn’t change Var (Case 5), and $E[U]=0$.

   $$\operatorname{Var}(X)=\operatorname{Var}(U)=E[U^2]$$
5. **Square:** write $\frac{u^2}{1+u^2}=1-\frac{1}{1+u^2}$.

   $$E[U^2]=\frac2\pi\int_{-1}^{1}\Big(1-\frac{1}{1+u^2}\Big)du=\frac2\pi\Big(2-\frac\pi2\Big)=\frac4\pi-1\approx0.2732$$

**Answer:** (a) $C=\tfrac2\pi$, $K=-5$ (so $X\in[4,6]$) (b) $\operatorname{Var}(X)=\tfrac4\pi-1\approx0.2732$

</details>

**Problem: Question 11 · Case 5 · Chebyshev · Practice 03 Q11** (advanced)

Chebyshev says $P(|Y-\mu_Y|\ge\varepsilon)\le\dfrac{\operatorname{Var}(Y)}{\varepsilon^2}$. $E[X]=5$, $\operatorname{Var}(X)=5$ and $Y=aX+b$. Find $a$ and $b$ so that $P(|Y-10|\ge0.1)\le0.01$.

<details><summary>Solution</summary>

1. **Type:** only $E$ and Var → Case 5 rules. Make the mean of $Y$ equal $10$.

   $$E[Y]=5a+b=10$$
2. **Plug in** $\operatorname{Var}(Y)=a^2\cdot5$, then make the Chebyshev bound at most $0.01$.

   $$\frac{5a^2}{0.1^2}\le0.01\quad\Longrightarrow\quad a^2\le2\times10^{-5}$$
3. Any such $a$ works, with $b$ from the first line.

   $$|a|\le0.00447,\qquad b=10-5a$$

**Answer:** Any $|a|\le 0.00447$ with $b=10-5a$ (e.g. $a=0.004$, $b=9.98$).

</details>
