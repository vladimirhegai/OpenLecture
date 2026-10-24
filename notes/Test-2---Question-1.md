# Test 2 - Question 1

**Lectures 7–9.** Random experiments, sample spaces, discrete random variables, PMFs and CDFs.

## Topic 1: Random variables: turning outcomes into numbers

An experiment produces an **outcome** $\omega$ (like HTH).

A **random variable** $X$ attaches a number to every outcome, so we can ask number questions ("how many heads?").

> **Reminder:** **From Test 1 (you'll need this all the time)**
> 
> - **Sample space** $\Omega$ = the set of all outcomes. **Event** = a subset of $\Omega$.
> - **Equally likely outcomes:** $P(A)=\dfrac{|A|}{|\Omega|}$ (count, then divide).
> - **Complement:** $P(A^c)=1-P(A)$. Use it for "at least one".
> - **Independent trials:** multiply, $P(A\cap B)=P(A)\,P(B)$.
> - **Counting** $k$ items from $n$:
> 
> | | order matters | order doesn't |
> |---|---|---|
> | with replacement | $n^k$ | (not needed) |
> | without replacement | $\dfrac{n!}{(n-k)!}$ | $\dbinom{n}{k}=\dfrac{n!}{k!\,(n-k)!}$ |

$$X:\Omega\to\mathbb{R},\qquad \omega\mapsto X(\omega)$$

- $\{X=x\}$ is an **event**: all outcomes $\omega$ with $X(\omega)=x$. Example: 2 tosses, $\{X=1\}=\{HT,TH\}$.
- $P(X=x)$ is just the probability of that event.
- $X$ is **discrete** when its range $R_X=\{X(\omega)\}$ is **countable**: a finite list $\{0,1,2,3\}$ or an endless list $\{0,1,2,\dots\}$.
- The events $\{X=x\}$ for different $x$ never overlap and together cover $\Omega$ (a partition), so their probabilities add to $1$.

**How to find $P(X=x)$ for every $x$:**

1. **List** $\Omega$ (or just count it).
2. **Label** every outcome with its value $X(\omega)$.
3. **Group** the outcomes by value: these groups are the events $\{X=x\}$.
4. **Add** the probabilities in each group (equally likely: count ÷ $|\Omega|$).

**Example: Example 1 · Three tosses, count the heads**

A fair coin is tossed three times. $X$ = number of heads. Find $P(X=x)$ for every value.

1. **List** $\Omega$: $2^3=8$ equally likely outcomes.

   $$\Omega=\{hhh,hht,hth,thh,htt,tht,tth,ttt\}$$
2. **Label and group** by the number of heads.

   $$\begin{gathered}\{X=3\}=\{hhh\},\quad \{X=2\}=\{hht,hth,thh\}\\ \{X=1\}=\{htt,tht,tth\},\quad \{X=0\}=\{ttt\}\end{gathered}$$
3. **Add** (count ÷ 8).

   $$\begin{gathered}P(X=0)=\frac18,\quad P(X=1)=\frac38\\ P(X=2)=\frac38,\quad P(X=3)=\frac18\end{gathered}$$
4. Check: the four groups partition $\Omega$, so the total must be 1.

   $$\frac18+\frac38+\frac38+\frac18=1\;\checkmark$$

**Answer:** $P(X=0)=\tfrac18,\ P(X=1)=\tfrac38,\ P(X=2)=\tfrac38,\ P(X=3)=\tfrac18$

**Problem: Try it 1 · Larger of two dice** (intermediate)

Two fair dice are rolled. Let $X$ be the **larger** of the two numbers. Find $P(X=x)$ for $x=1,\dots,6$.

<details><summary>Solution</summary>

1. **List** $\Omega$: ordered pairs $(a,b)$, $6\cdot6=36$ equally likely outcomes.

   $$|\Omega|=36$$
2. **Group:** $\{X=x\}$ = pairs whose max is $x$. Example $x=3$: $(1,3),(2,3),(3,3),(3,2),(3,1)$.

   $$|\{X=3\}|=5$$
3. In general: $x$ choices for $b$ when $a=x$, plus $x$ choices for $a$ when $b=x$, minus the double-counted $(x,x)$.

   $$|\{X=x\}|=x+x-1=2x-1$$
4. **Divide** by 36.

   $$P(X=x)=\frac{2x-1}{36},\qquad x=1,2,\dots,6$$
5. Check the total.

   $$\frac{1+3+5+7+9+11}{36}=\frac{36}{36}=1\;\checkmark$$

**Answer:** $P(X=x)=\dfrac{2x-1}{36}$: $\tfrac1{36},\tfrac3{36},\tfrac5{36},\tfrac7{36},\tfrac9{36},\tfrac{11}{36}$

</details>

**Problem: Try it 2 · Two balls, no replacement** (intermediate)

An urn has 3 red and 2 blue balls. Two balls are drawn **without replacement** (order not recorded). Let $X$ = number of red balls drawn. Find $P(X=x)$.

<details><summary>Solution</summary>

1. **Count** $\Omega$: unordered pairs from 5 balls.

   $$|\Omega|=\binom52=10$$
2. $X=0$: both blue.

   $$P(X=0)=\frac{\binom30\binom22}{10}=\frac{1}{10}$$
3. $X=1$: one of 3 red **and** one of 2 blue.

   $$P(X=1)=\frac{\binom31\binom21}{10}=\frac{6}{10}$$
4. $X=2$: both red.

   $$P(X=2)=\frac{\binom32\binom20}{10}=\frac{3}{10}$$
5. Check.

   $$\frac1{10}+\frac6{10}+\frac3{10}=1\;\checkmark$$

**Answer:** $P(X=0)=0.1,\ P(X=1)=0.6,\ P(X=2)=0.3$

</details>

## Topic 2: The PMF and the named families

The **probability mass function** (PMF) lists how the total probability $1$ is split among the values of $X$.

$$p_X(x)=P(X=x)$$

- **Rule 1:** $p_X(x)\ge 0$.
- **Rule 2:** $\displaystyle\sum_{x\in R_X} p_X(x)=1$. Use it to find an unknown constant $c$.
- **Sets of values:** $P(X\in B)=\displaystyle\sum_{x\in B}p_X(x)$, e.g. $P(1\le X\le 3)=p_X(1)+p_X(2)+p_X(3)$.
- **"At least one":** $P(X\ge1)=1-p_X(0)$. Much faster than adding forever.

> **Reminder:** **Two sums that make PMFs add to 1**
> 
> - **Geometric series** ($|r|<1$): $\displaystyle\sum_{k=0}^{\infty} r^k=\frac{1}{1-r}$, and starting at $k=1$: $\displaystyle\sum_{k=1}^{\infty} r^k=\frac{r}{1-r}$.
> - **Exponential series:** $\displaystyle\sum_{k=0}^{\infty}\frac{\lambda^k}{k!}=e^{\lambda}$ (this is why the Poisson PMF has $e^{-\lambda}$ in front).
> - **Finite geometric:** $\displaystyle\sum_{k=0}^{m-1} r^k=\frac{1-r^m}{1-r}$.

Many experiments give PMFs with the same shape, so they get names. **Memorise these** (no formula sheet):

| Family | PMF | $k$ | $X$ counts… |
|---|---|---|---|
| Bernoulli$(p)$ | ${p^k(1-p)^{1-k}}$ | ${k=0,1}$ | one yes/no trial (1 = success) |
| Binomial$(n,p)$ | ${\binom{n}{k}p^k(1-p)^{n-k}}$ | ${0,\dots,n}$ | successes in $n$ independent trials |
| Geometric$(p)$ | ${(1-p)^{k-1}p}$ | ${1,2,\dots}$ | trials until the **first** success |
| Poisson$(\lambda)$ | ${e^{-\lambda}\dfrac{\lambda^k}{k!}}$ | ${0,1,2,\dots}$ | events in a fixed time/region, average $\lambda$ |
| Hypergeometric | ${\dfrac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}}$ | ${0,\dots,n}$ | successes in $n$ draws **without** replacement |

**Which family?** Read the story:

- **Fixed number $n$** of independent yes/no trials, same $p$ → **Binomial**.
- **"Until the first success"** → **Geometric**. (Counting *failures before* it instead: $P=(1-p)^k p$, $k=0,1,\dots$)
- **"On average $\lambda$ per hour/page/year"** → **Poisson**. Scale $\lambda$ to the interval asked: 7 per week → $\lambda=1$ per day.
- **Draw without replacement** from a box with $K$ "good" out of $N$ → **Hypergeometric** (or just count, as in Try it 2).

> **Tip:** **Why the binomial looks like that:** one particular outcome with $k$ successes, like $SS\dots SF\dots F$, has probability $p^k(1-p)^{n-k}$ (independent trials multiply). There are $\binom{n}{k}$ ways to choose **which** trials are the successes.

```graph
title "Poisson PMF: drag $\lambda$ and watch where the mass sits"
x -0.5 14.5 label="$k$" height=260
y 0 0.42 label="$p_X(k)$"
slider L 0.5 10 4 step=0.1 label="$\lambda$"
segment "0" "0" "0" "exp(-L)*L^0/1" color=1
point "0" "exp(-L)*L^0/1" color=1
segment "1" "0" "1" "exp(-L)*L^1/1" color=1
point "1" "exp(-L)*L^1/1" color=1
segment "2" "0" "2" "exp(-L)*L^2/2" color=1
point "2" "exp(-L)*L^2/2" color=1
segment "3" "0" "3" "exp(-L)*L^3/6" color=1
point "3" "exp(-L)*L^3/6" color=1
segment "4" "0" "4" "exp(-L)*L^4/24" color=1
point "4" "exp(-L)*L^4/24" color=1
segment "5" "0" "5" "exp(-L)*L^5/120" color=1
point "5" "exp(-L)*L^5/120" color=1
segment "6" "0" "6" "exp(-L)*L^6/720" color=1
point "6" "exp(-L)*L^6/720" color=1
segment "7" "0" "7" "exp(-L)*L^7/5040" color=1
point "7" "exp(-L)*L^7/5040" color=1
segment "8" "0" "8" "exp(-L)*L^8/40320" color=1
point "8" "exp(-L)*L^8/40320" color=1
segment "9" "0" "9" "exp(-L)*L^9/362880" color=1
point "9" "exp(-L)*L^9/362880" color=1
segment "10" "0" "10" "exp(-L)*L^10/3628800" color=1
point "10" "exp(-L)*L^10/3628800" color=1
segment "11" "0" "11" "exp(-L)*L^11/39916800" color=1
point "11" "exp(-L)*L^11/39916800" color=1
segment "12" "0" "12" "exp(-L)*L^12/479001600" color=1
point "12" "exp(-L)*L^12/479001600" color=1
segment "13" "0" "13" "exp(-L)*L^13/6227020800" color=1
point "13" "exp(-L)*L^13/6227020800" color=1
segment "14" "0" "14" "exp(-L)*L^14/87178291200" color=1
point "14" "exp(-L)*L^14/87178291200" color=1
readout "$P(X=3)$" "exp(-L)*L^3/6"
readout "$P(X=4)$" "exp(-L)*L^4/24"
readout "$P(X\ge1)=1-e^{-\lambda}$" "1-exp(-L)"
```

**Example: Example 2 · Emails per hour (Poisson)**

The number of emails in one hour is Poisson with an average of 4 per hour. Compare $P(X=3)$ and $P(X=4)$.

1. **Family:** "on average 4 per hour", counting in one hour → Poisson with $\lambda=4$.

   $$p_X(k)=e^{-4}\frac{4^k}{k!}$$
2. Plug in $k=3$.

   $$P(X=3)=e^{-4}\frac{4^3}{3!}=e^{-4}\cdot\frac{64}{6}\approx 0.1954$$
3. Plug in $k=4$.

   $$P(X=4)=e^{-4}\frac{4^4}{4!}=e^{-4}\cdot\frac{256}{24}\approx 0.1954$$
4. They are **equal**: $\frac{4^4}{4!}=\frac{4}{4}\cdot\frac{4^3}{3!}$. In general $p(k)=p(k-1)\cdot\frac{\lambda}{k}$, so the top is near $\lambda$.

   $$P(X=3)=P(X=4)\approx 0.1954$$

**Answer:** Both $\approx 0.1954$: the PMF peaks at $k=3$ and $k=4$ together.

**Problem: Try it 3 · Find the constant** (introductory)

Can $p_X(x)=c\left(\tfrac23\right)^x$ for $x=1,2,3,\dots$ (and $0$ elsewhere) be a PMF? If so, find $c$.

<details><summary>Solution</summary>

1. **Rule 1:** for $c>0$ every value is positive. **Rule 2:** the total must be 1.

   $$\sum_{x=1}^{\infty}c\left(\frac23\right)^x=1$$
2. Geometric series starting at $x=1$ with $r=\tfrac23$.

   $$\sum_{x=1}^{\infty}\left(\frac23\right)^x=\frac{2/3}{1-2/3}=2$$
3. Solve.

   $$2c=1\;\Rightarrow\; c=\frac12$$

**Answer:** Yes, with $c=\tfrac12$.

</details>

**Problem: Try it 4 · Typos on a page** (intermediate)

A book has on average one typo every three pages. The number of typos on one page is Poisson. Find the probability of at least one typo on a given page.

<details><summary>Solution</summary>

1. **Scale $\lambda$** to one page: 1 per 3 pages → $\tfrac13$ per page.

   $$\lambda=\frac13$$
2. **At least one** → complement.

   $$P(X\ge1)=1-P(X=0)=1-e^{-1/3}$$
3. Evaluate.

   $$1-e^{-1/3}\approx 0.2835$$

**Answer:** $1-e^{-1/3}\approx 0.2835$

</details>

**Problem: Try it 5 · Bit errors in a byte** (intermediate)

Each bit of an 8-bit byte is flipped independently with probability $0.1$. Find the probability that the byte has **at most one** flipped bit.

<details><summary>Solution</summary>

1. **Family:** fixed $n=8$ independent trials, "success" = flipped, $p=0.1$ → Binomial$(8,0.1)$.

   $$P(X=k)=\binom8k(0.1)^k(0.9)^{8-k}$$
2. "At most one" = $X=0$ or $X=1$.

   $$P(X\le1)=(0.9)^8+8(0.1)(0.9)^7$$
3. Evaluate.

   $$0.4305+0.3826\approx 0.8131$$

**Answer:** $P(X\le1)\approx 0.8131$

</details>

**Problem: Try it 6 · Retransmit until it works** (intermediate)

A packet is sent again and again until one gets through. Each attempt succeeds independently with probability $0.2$. Let $X$ = number of attempts. Find $P(X=3)$ and $P(X>3)$.

<details><summary>Solution</summary>

1. **Family:** "until the first success" → Geometric$(0.2)$.

   $$P(X=k)=(0.8)^{k-1}(0.2),\quad k=1,2,\dots$$
2. $X=3$: fail, fail, succeed.

   $$P(X=3)=(0.8)^2(0.2)=0.128$$
3. $X>3$ means the first 3 attempts all failed (no sum needed).

   $$P(X>3)=(0.8)^3=0.512$$

**Answer:** $P(X=3)=0.128$, $P(X>3)=0.512$

</details>

## Topic 3: The CDF

The **cumulative distribution function** (CDF) answers "what is the chance $X$ is **at most** $x$?" for **every** real $x$.

$$F_X(x)=P(X\le x)=\sum_{x_i\le x}p_X(x_i)$$

- Defined for **all** real $x$, not only the values of $X$ (e.g. $F_X(2.7)$ makes sense).
- For a discrete $X$ it is a **staircase**: flat between values, a **jump of size $p_X(x_i)$** at each value $x_i$.
- It never goes down, starts at $0$ (far left) and ends at $1$ (far right).
- At a jump, $F_X(x_i)$ takes the **upper** value: $\le$ includes $x_i$ itself (the solid dot).

**Reading probabilities off the CDF:**

| You want | Use |
|---|---|
| $P(X\le b)$ | $F_X(b)$ |
| $P(X>a)$ | $1-F_X(a)$ |
| $P(a<X\le b)$ | $F_X(b)-F_X(a)$ |
| $P(X=a)$ | jump at $a$ = $F_X(a)-F_X(a^-)$ |
| $P(X<a)$ | $F_X(a^-)$ = height just **left** of $a$ |

> **Warning:** **$<$ vs $\le$ matters for discrete $X$.** With dice, $P(X<4)=F_X(3)$ but $P(X\le4)=F_X(4)$. Rewrite every question as "$\le$" before reading the CDF.

**Example: Example 3 · CDF of the three-toss count**

For Example 1 ($p_X(0)=\tfrac18,\ p_X(1)=\tfrac38,\ p_X(2)=\tfrac38,\ p_X(3)=\tfrac18$), find and sketch $F_X(x)$.

1. **Left of 0**, $X\le x$ is impossible.

   $$x<0:\quad F_X(x)=0$$
2. **Add each jump** as you pass a value, keep it flat in between.

   $$F_X(x)=\begin{cases}0,&x<0\\ \frac18,&0\le x<1\\ \frac48=\frac12,&1\le x<2\\ \frac78,&2\le x<3\\ 1,&x\ge3\end{cases}$$
3. **Sketch:** a staircase with jumps $\tfrac18,\tfrac38,\tfrac38,\tfrac18$ at $0,1,2,3$ (graph below).

   $$F_X(3)=1$$

**Answer:** Staircase: $0 \to \tfrac18 \to \tfrac12 \to \tfrac78 \to 1$ with jumps at $x=0,1,2,3$.

Each jump is one PMF value. The solid dot shows the step belongs to the **upper** value.

```graph
title "CDF of the number of heads in 3 tosses"
x -1 4.5 label="$x$" height=240
y 0 1.1 label="$F_X(x)$"
segment "-1" "0" "0" "0" color=2
point "0" "0.125" color=2
segment "0" "0.125" "1" "0.125" color=2
point "1" "0.5" color=2
segment "1" "0.5" "2" "0.5" color=2
point "2" "0.875" color=2
segment "2" "0.875" "3" "0.875" color=2
point "3" "1" color=2
segment "3" "1" "4.5" "1" color=2
hline "1"
text "0.35" "0.2" "jump $\tfrac18$"
text "1.4" "0.6" "jump $\tfrac38$"
```

**Problem: Try it 7 · From a CDF back to the PMF** (intermediate)

$X$ has CDF

$$
F_X(x)=\begin{cases}0,&x<-3\\ 3/8,&-3\le x<0\\ 3/4,&0\le x<6\\ 1,&x\ge6\end{cases}
$$

(a) Is $X$ discrete or continuous? (b) Find its PMF. (c) Find $P(-3<X\le6)$ and $P(X<0)$.

<details><summary>Solution</summary>

1. (a) The CDF is a staircase (it jumps), so **$X$ is discrete**, with values at the jumps.

   $$R_X=\{-3,\;0,\;6\}$$
2. (b) **Jump sizes** are the PMF.

   $$p_X(-3)=\frac38,\quad p_X(0)=\frac34-\frac38=\frac38,\quad p_X(6)=1-\frac34=\frac14$$
3. (c) Use $F(b)-F(a)$.

   $$P(-3<X\le6)=F_X(6)-F_X(-3)=1-\frac38=\frac58$$
4. $X<0$: height just left of $0$.

   $$P(X<0)=F_X(0^-)=\frac38$$

**Answer:** Discrete; $p_X(-3)=\tfrac38,\ p_X(0)=\tfrac38,\ p_X(6)=\tfrac14$; $P(-3<X\le6)=\tfrac58$, $P(X<0)=\tfrac38$.

</details>

**Problem: Try it 8 · CDF of the larger die** (intermediate)

For $X$ = larger of two dice (Try it 1), find $F_X(x)$ for $x=1,\dots,6$ **without** adding the PMF, then find $P(2<X\le5)$.

<details><summary>Solution</summary>

1. $X\le x$ means **both** dice are $\le x$. The dice are independent.

   $$F_X(x)=P(\text{die}_1\le x)\,P(\text{die}_2\le x)=\frac{x}{6}\cdot\frac{x}{6}=\frac{x^2}{36}$$
2. Check with the PMF: $F_X(2)=\tfrac{1}{36}+\tfrac{3}{36}=\tfrac{4}{36}$. ✓

   $$F_X(2)=\frac{4}{36}$$
3. Use $F(b)-F(a)$.

   $$P(2<X\le5)=F_X(5)-F_X(2)=\frac{25-4}{36}=\frac{21}{36}=\frac{7}{12}$$

**Answer:** $F_X(x)=\dfrac{x^2}{36}$ at $x=1,\dots,6$ (flat in between); $P(2<X\le5)=\tfrac{7}{12}$.

</details>

## Practice Questions

Test-style questions for Question 1, roughly easy → hard. Solve on paper first, then open the solution.

**Problem: Question 1 · Wrong-number calls · Tutorial 3 Q3** (introductory)

A mail-order house gets on average **7 wrong-number calls per week** (Poisson). Find the probability that tomorrow they get (a) exactly two wrong-number calls, (b) at least one.

<details><summary>Solution</summary>

1. **Family:** average rate, count in an interval → Poisson. **Scale** to one day.

   $$\lambda=\frac{7}{7}=1$$
2. (a)

   $$P(X=2)=e^{-1}\frac{1^2}{2!}=\frac{e^{-1}}{2}\approx 0.1839$$
3. (b) **At least one** → complement.

   $$P(X\ge1)=1-e^{-1}\approx 0.6321$$

**Answer:** (a) $\approx 0.1839$ (b) $\approx 0.6321$

</details>

**Problem: Question 2 · A PMF with a constant** (introductory)

$p_X(x)=c\,x$ for $x=1,2,3,4$ and $0$ otherwise. (a) Find $c$. (b) Find and sketch the CDF. (c) Find $P(1<X\le3)$ and $P(X<3)$.

<details><summary>Solution</summary>

1. (a) **Total = 1.**

   $$c(1+2+3+4)=10c=1\;\Rightarrow\;c=\frac1{10}$$
2. (b) **Add the jumps** $0.1, 0.2, 0.3, 0.4$ at $x=1,2,3,4$.

   $$F_X(x)=\begin{cases}0,&x<1\\0.1,&1\le x<2\\0.3,&2\le x<3\\0.6,&3\le x<4\\1,&x\ge4\end{cases}$$
3. (c) $F(b)-F(a)$.

   $$P(1<X\le3)=F_X(3)-F_X(1)=0.6-0.1=0.5$$
4. $X<3$ = $X\le2$ for integer values.

   $$P(X<3)=F_X(2)=0.3$$

**Answer:** $c=0.1$; staircase $0,0.1,0.3,0.6,1$; $P(1<X\le3)=0.5$, $P(X<3)=0.3$.

</details>

**Problem: Question 3 · Toss until a head, at most 4 tosses** (intermediate)

A coin with $P(H)=p$ is tossed until the first head **or** until 4 tosses have been made, whichever comes first. (a) Write the sample space. (b) Let $X$ = number of tosses made. Find the PMF of $X$. (c) Evaluate it for $p=\tfrac12$.

<details><summary>Solution</summary>

1. (a) Stop at the first $H$, or after 4 tosses.

   $$\Omega=\{H,\;TH,\;TTH,\;TTTH,\;TTTT\}$$
2. (b) **Label:** $X(H)=1,\ X(TH)=2,\ X(TTH)=3$, and **two** outcomes give 4 tosses.

   $$\{X=4\}=\{TTTH,\;TTTT\}$$
3. Independent tosses multiply.

   $$p_X(1)=p,\quad p_X(2)=(1-p)p,\quad p_X(3)=(1-p)^2p$$
4. $X=4$: the first three were tails (the 4th can be anything).

   $$p_X(4)=(1-p)^3p+(1-p)^4=(1-p)^3$$
5. (c) $p=\tfrac12$. Check: the total is 1.

   $$\frac12,\ \frac14,\ \frac18,\ \frac18$$

**Answer:** $p_X(1)=p,\ p_X(2)=(1-p)p,\ p_X(3)=(1-p)^2p,\ p_X(4)=(1-p)^3$; for $p=\tfrac12$: $\tfrac12,\tfrac14,\tfrac18,\tfrac18$.

</details>

**Problem: Question 4 · Defective chips** (intermediate)

A box has 10 chips, 3 of them defective. Four chips are chosen at random **without replacement**. Let $X$ = number of defective chips chosen. (a) Find the PMF of $X$. (b) Find $F_X(1)$ and $P(X\ge2)$.

<details><summary>Solution</summary>

1. **Count** $\Omega$: unordered choices of 4 from 10.

   $$|\Omega|=\binom{10}{4}=210$$
2. **$X=k$:** $k$ of the 3 defective **and** $4-k$ of the 7 good.

   $$p_X(k)=\frac{\binom3k\binom7{4-k}}{210}$$
3. Evaluate $k=0,1,2,3$.

   $$\begin{gathered}p_X(0)=\frac{35}{210}=\frac16,\quad p_X(1)=\frac{105}{210}=\frac12\\ p_X(2)=\frac{63}{210}=\frac3{10},\quad p_X(3)=\frac{7}{210}=\frac1{30}\end{gathered}$$
4. (b) Add up to 1, then use the complement.

   $$F_X(1)=\frac16+\frac12=\frac23,\qquad P(X\ge2)=1-\frac23=\frac13$$

**Answer:** $\tfrac16,\tfrac12,\tfrac3{10},\tfrac1{30}$ for $k=0..3$; $F_X(1)=\tfrac23$, $P(X\ge2)=\tfrac13$.

</details>

**Problem: Question 5 · Alpha particles · Tutorial 3 Q4** (intermediate)

One gram of a radioactive element emits on average 3.9 alpha particles per second (Poisson). For the next second, find (a) $P(\text{at most }6)$, (b) $P(\text{at least }2)$, (c) $P(\text{at least 3 and at most 6})$.

<details><summary>Solution</summary>

1. **Family:** Poisson with $\lambda=3.9$ (already per second).

   $$p(k)=e^{-3.9}\frac{3.9^k}{k!}$$
2. (a) Add $k=0$ to $6$. Shortcut: each term is the previous one times $\tfrac{3.9}{k}$.

   $$P(X\le6)=e^{-3.9}\left(1+3.9+\frac{3.9^2}{2}+\dots+\frac{3.9^6}{720}\right)\approx 0.8995$$
3. (b) **Complement** of $\{0,1\}$.

   $$P(X\ge2)=1-e^{-3.9}(1+3.9)\approx 0.9008$$
4. (c) $3\le X\le6$ = (at most 6) minus (at most 2).

   $$P(3\le X\le6)=P(X\le6)-P(X\le2)\approx 0.6464$$

**Answer:** (a) $\approx 0.8995$ (b) $\approx 0.9008$ (c) $\approx 0.6464$

</details>

**Problem: Question 6 · Total of two chips · Practice 02 Q5** (intermediate)

An urn has 10 chips numbered $0$ to $9$. Two chips are drawn at random without replacement. Find the PMF of their **total** $X$.

<details><summary>Solution</summary>

1. **Count** $\Omega$: unordered pairs of different chips, all equally likely.

   $$|\Omega|=\binom{10}{2}=45,\qquad R_X=\{1,2,\dots,17\}$$
2. **Group** pairs $\{a<b\}$ by $a+b$. Example $X=9$: $\{0,9\},\{1,8\},\{2,7\},\{3,6\},\{4,5\}$.

   $$|\{X=9\}|=5$$
3. For $s\le9$: $a$ runs from $0$ while $a<s-a$. For $s\ge10$ use symmetry: total $s$ ↔ total $18-s$ (replace each chip $c$ by $9-c$).

   $$\begin{gathered}|\{X=s\}|=\left\lfloor\frac{s+1}{2}\right\rfloor\quad (s\le9)\\ |\{X=s\}|=|\{X=18-s\}|\quad (s\ge10)\end{gathered}$$
4. So the counts for $s=1,\dots,17$ are:

   $$1,1,2,2,3,3,4,4,5,4,4,3,3,2,2,1,1$$
5. Divide by 45 and check the counts add to 45.

   $$p_X(s)=\frac{\text{count}(s)}{45},\qquad \textstyle\sum \text{counts}=45\;\checkmark$$

**Answer:** $p_X(s)=\tfrac{1}{45}\times(1,1,2,2,3,3,4,4,5,4,4,3,3,2,2,1,1)$ for $s=1,\dots,17$.

</details>

**Problem: Question 7 · Four accidents on one day · Tutorial 3 Q7** (intermediate)

A town had 12 accidents in June (30 days), 4 of them on June 13. Assume each accident is equally likely to fall on any day, independently. Find the probability that **at least 4** of the 12 accidents fall on June 13.

<details><summary>Solution</summary>

1. **Family:** 12 independent accidents, "success" = it lands on June 13, $p=\tfrac1{30}$ → Binomial$(12,\tfrac1{30})$.

   $$P(X=k)=\binom{12}{k}\left(\frac1{30}\right)^k\left(\frac{29}{30}\right)^{12-k}$$
2. **At least 4** → complement of $0,1,2,3$.

   $$P(X\ge4)=1-\sum_{k=0}^{3}\binom{12}{k}\left(\frac1{30}\right)^k\left(\frac{29}{30}\right)^{12-k}$$
3. The four terms.

   $$\approx 1-(0.6658+0.2755+0.0522+0.0060)$$
4. So 4 on one day is very unlikely by chance.

   $$P(X\ge4)\approx 0.00049$$

**Answer:** $P(X\ge4)\approx 0.00049$ (about 4.9 in 10 000).

</details>

**Problem: Question 8 · Quiet years · Tutorial 3 Q6** (intermediate)

Earthquakes in a region follow a Poisson model with on average 7 per year. (a) Find the probability of no earthquakes in one year. (b) Find the probability that in **exactly three of the next eight years** there are no earthquakes.

<details><summary>Solution</summary>

1. (a) **Poisson**, $\lambda=7$ per year, $k=0$.

   $$q=P(X=0)=e^{-7}\approx 0.000912$$
2. (b) Each year is a trial: "success" = a quiet year, with probability $q$. 8 independent years → **Binomial$(8,q)$**.

   $$P(Y=3)=\binom83q^3(1-q)^5$$
3. Evaluate.

   $$56\,(e^{-7})^3(1-e^{-7})^5\approx 4.23\times10^{-8}$$

**Answer:** (a) $e^{-7}\approx 0.000912$ (b) $\approx 4.23\times10^{-8}$

</details>

**Problem: Question 9 · Error-free pixels · Tutorial 6 Q7** (intermediate)

A rover sends pixels one after another; each pixel is corrupted independently with probability $p=0.03$. (a) Let $N$ = number of **error-free** pixels between two erroneous ones. Find the PMF of $N$. (b) A new rover needs a 99% chance that at least 1000 pixels in a row arrive correctly before a bad one. How small must $p$ be?

<details><summary>Solution</summary>

1. (a) After an error, count good pixels until the next bad one. $N=k$: $k$ good, then 1 bad.

   $$P(N=k)=(0.97)^k(0.03),\qquad k=0,1,2,\dots$$
2. This is the geometric "failures before the first success" form (starts at $k=0$).

   $$\sum_{k\ge0}(0.97)^k(0.03)=\frac{0.03}{1-0.97}=1\;\checkmark$$
3. (b) **At least 1000 good in a row** = the first 1000 pixels are all good.

   $$P(N\ge1000)=(1-p)^{1000}\ge0.99$$
4. Solve for $p$.

   $$1-p\ge0.99^{1/1000}\;\Rightarrow\;p\le1-0.99^{1/1000}\approx 1.01\times10^{-5}$$

**Answer:** (a) $P(N=k)=0.97^k\cdot0.03$, $k=0,1,\dots$ (b) $p\lesssim 1.0\times10^{-5}$

</details>

**Problem: Question 10 · Geometric, all the way · Practice 03 Q7** (advanced)

$N\sim$ Geometric$(p)$: $P(N=k)=(1-p)^{k-1}p$, $k=1,2,\dots$ Find (a) $P(N>k)$, (b) the CDF of $N$, (c) $P(N\text{ is even})$, (d) $P(N=k\mid N\le m)$.

<details><summary>Solution</summary>

1. (a) $N>k$ means the first $k$ trials all failed.

   $$P(N>k)=(1-p)^k$$
2. (b) **Complement**, flat between integers.

   $$F_N(x)=\begin{cases}0,&x<1\\1-(1-p)^{\lfloor x\rfloor},&x\ge1\end{cases}$$
3. (c) Add $k=2,4,6,\dots$: a geometric series with ratio $(1-p)^2$.

   $$P(\text{even})=\sum_{m=1}^{\infty}(1-p)^{2m-1}p=\frac{p(1-p)}{1-(1-p)^2}=\frac{1-p}{2-p}$$
4. (d) **Conditional probability:** $P(A\mid B)=\dfrac{P(A\cap B)}{P(B)}$. For $k\le m$, $\{N=k\}$ is inside $\{N\le m\}$.

   $$P(N=k\mid N\le m)=\frac{(1-p)^{k-1}p}{1-(1-p)^m},\qquad k=1,\dots,m$$
5. For $k>m$ the intersection is empty.

   $$P(N=k\mid N\le m)=0,\qquad k>m$$

**Answer:** (a) $(1-p)^k$ (b) $1-(1-p)^{\lfloor x\rfloor}$ for $x\ge1$ (c) $\dfrac{1-p}{2-p}$ (d) $\dfrac{(1-p)^{k-1}p}{1-(1-p)^m}$ for $1\le k\le m$

</details>
