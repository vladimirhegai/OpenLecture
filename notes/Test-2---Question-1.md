# Test 2 - Question 1

**Lectures 7–9.** $X$ turns the result of an experiment into a number that lands on separate values ($0,1,2,\dots$). Find its PMF and CDF.

## Question 1 in plain words

**You’ll see:** an experiment (coins, dice, chips), a PMF with a $c$, a CDF, or a story with a clue word (“on average”, “until”). Then parts (a), (b), (c).

**The move:** the **PMF** lists every value of $X$ and its chance. The chances add to $1$. The **CDF** is the running total:

$$p_X(x)=P(X=x),\qquad \sum_x p_X(x)=1,\qquad F_X(x)=P(X\le x)$$

**Short example:** toss 3 coins, $X$ = number of heads:

$$p_X(0,1,2,3)=\frac18,\ \frac38,\ \frac38,\ \frac18\qquad\Longrightarrow\qquad F_X(1)=\frac18+\frac38=\frac12$$

**Which case?**

| The question gives you… | Go to |
|---|---|
| an experiment that matches no family | Case 1 |
| “$p_X(x)=c\cdot(\dots)$, find $c$” | Case 2 |
| a CDF, or asks for one | Case 3 |
| a story with a clue word (“on average”, “until”, “without replacement”) | Case 4 |
| “in exactly 3 of the next 8 years…” | Case 5 |

## Case 1: build the PMF from an experiment

**You’ll see:** coins, dice, chips, balls, but no family fits. “Find the PMF of $X$.”

**The move:** list the outcomes, turn each into a number, and add up the chances of each number.

1. **List** all the outcomes (equally likely? count them).
2. **Label** each outcome with its value of $X$.
3. **Add** the chances of outcomes with the same value.
4. **Check:** the PMF adds to $1$.

**Short example:** 3 coins: $X=2$ for $hht$, $hth$, $thh$:

$$P(X=2)=\frac18+\frac18+\frac18=\frac38$$

<details><summary>Full example (Lecture 7): toss a coin 3 times, $\;X$ = number of heads</summary>

Step 1 · **List:** $2^3=8$ equally likely outcomes, each $\tfrac18$.

$$
hhh,\ hht,\ hth,\ thh,\ htt,\ tht,\ tth,\ ttt
$$

Step 2 · **Label** each with its number of heads.

$$
X=3:\ hhh\qquad X=2:\ hht,\ hth,\ thh
$$

$$
X=1:\ htt,\ tht,\ tth\qquad X=0:\ ttt
$$

Step 3 · **Add** the chances in each group.

$$
p_X(0)=\frac18,\quad p_X(1)=\frac38,\quad p_X(2)=\frac38,\quad p_X(3)=\frac18
$$

Step 4 · **Check.** (Practice 02 Q6, boys in a 3-child family, is the same question.)

$$
\frac18+\frac38+\frac38+\frac18=1\ \checkmark
$$

**Answer:**

$$
p_X=\frac18,\ \frac38,\ \frac38,\ \frac18\ \text{ for }x=0,1,2,3
$$

</details>

<details><summary>Full example (Practice 02 Q5): the total of two chips</summary>

Step 1 · 10 chips numbered 0–9; draw 2 without replacement; $S$ = their total. **List:** a pair of different chips, order doesn’t matter.

$$
\binom{10}{2}=45\ \text{ equally likely pairs}
$$

Step 2 · **Label:** totals run from $0+1=1$ up to $8+9=17$. Count the pairs for each total. Example $S=9$:

$$
\{0,9\},\{1,8\},\{2,7\},\{3,6\},\{4,5\}\quad\Rightarrow\quad 5\text{ pairs}
$$

Step 3 · $S=10$: $\{1,9\},\{2,8\},\{3,7\},\{4,6\}$ (not $\{5,5\}$: one chip can’t be drawn twice).

$$
4\text{ pairs}
$$

Step 4 · **Add:** the counts climb $1,1,2,2,3,3,4,4,5$ up to $S=9$, then fall back $4,4,3,3,2,2,1,1$.

$$
p_S(s)=\frac{\text{pairs with total }s}{45},\qquad p_S(9)=\frac{5}{45}=\frac19
$$

Step 5 · **Check.**

$$
1+1+2+2+3+3+4+4+5+4+4+3+3+2+2+1+1=45\ \checkmark
$$

**Answer:**

$$
p_S(s)=\frac{1}{45}\times(1,1,2,2,3,3,4,4,5,4,4,3,3,2,2,1,1)\ \text{ for }s=1,\dots,17
$$

</details>

**Problem: Try it 1 · Case 1 · Larger of two dice** (intermediate)

Two fair dice are rolled. Let $X$ be the **larger** of the two numbers. Find $P(X=x)$ for $x=1,\dots,6$.

<details><summary>Solution</summary>

1. **List:** $6\cdot6=36$ equally likely pairs $(a,b)$.

   $$36\text{ outcomes}$$
2. **Label** $x=3$ as an example: $(1,3),(2,3),(3,3),(3,2),(3,1)$.

   $$5\text{ pairs}$$
3. In general: $x$ pairs with $a=x$, plus $x$ with $b=x$, minus $(x,x)$ counted twice.

   $$2x-1\text{ pairs}$$
4. **Add:** divide by 36.

   $$P(X=x)=\frac{2x-1}{36}$$
5. **Check:** $1+3+5+7+9+11=36$ ✓.

**Answer:** $P(X=x)=\dfrac{2x-1}{36}$: $\tfrac1{36},\tfrac3{36},\tfrac5{36},\tfrac7{36},\tfrac9{36},\tfrac{11}{36}$

</details>

## Case 2: find c (the chances add to 1)

**You’ll see:** “$p_X(x)=c\cdot(\dots)$. Find $c$.”

**The move:** add up every chance, set it to $1$, solve. (Same as Question 2, with a sum instead of an area.)

$$\sum_{\text{all }x}c\cdot(\dots)=1$$

**Short example:** $p_X(x)=c(x+1)$ for $x=0,1,2,3$:

$$c(1+2+3+4)=10c=1\quad\Longrightarrow\quad c=\frac1{10}$$

<details><summary>Full example (Tutorial 3 Q2): $\;p_X(x)=c\big(\tfrac23\big)^x$, $\;x=1,2,3,\dots$</summary>

Step 1 · **Find $c$:** add every chance.

$$
\sum_{x=1}^{\infty}c\Big(\frac23\Big)^x=1
$$

Step 2 · Geometric series starting at $1$, ratio $r=\tfrac23$ (card below).

$$
\sum_{x=1}^{\infty}\Big(\frac23\Big)^x=\frac{2/3}{1-2/3}=2
$$

Step 3 · Solve.

$$
2c=1\quad\Longrightarrow\quad c=\frac12
$$

**Answer:**

$$
c=\frac12
$$

</details>

<details><summary>Sums you’ll need</summary>

Geometric series ($|r|<1$), starting at $0$ or at $1$:

$$
\sum_{k=0}^{\infty}r^k=\frac{1}{1-r},\qquad \sum_{k=1}^{\infty}r^k=\frac{r}{1-r}
$$

The exponential series (it’s why the Poisson PMF adds to 1):

$$
\sum_{k=0}^{\infty}\frac{\lambda^k}{k!}=e^{\lambda}
$$

</details>

## Case 3: the CDF (a staircase)

**You’ll see:** “find the CDF”, “find the PMF from this CDF”, “find $P(a<X\le b)$”.

**The move:** the CDF is a **staircase**. It’s flat between values and **jumps by $p_X(x)$** at each value:

$$F_X(x)=P(X\le x)=\sum_{k\le x}p_X(k)$$

1. **Accumulate** (PMF → CDF): keep a running total, adding each jump as you pass a value.
2. **Jumps** (CDF → PMF): the jump sizes are the PMF.
3. **Rewrite** the probability asked with $F$’s (card below).

**Short example:** 3 coins, the running total:

$$0\ \to\ \frac18\ \to\ \frac12\ \to\ \frac78\ \to\ 1$$

<details><summary>Rewrite: turn any probability into $F$’s</summary>

Up to $b$:

$$
P(X\le b)=F_X(b)
$$

Above $a$:

$$
P(X>a)=1-F_X(a)
$$

Between:

$$
P(a<X\le b)=F_X(b)-F_X(a)
$$

One value: the jump there ($0$ if no jump).

$$
P(X=a)=\text{jump at }a
$$

**For whole numbers, turn $<$ into $\le$ first:**

$$
P(X<4)=P(X\le3)=F_X(3)
$$

</details>

<details><summary>Full example (Lecture 9): the CDF of the 3-coin count</summary>

Step 1 · **Accumulate:** start at $0$, jump $\tfrac18$ at $0$, $\tfrac38$ at $1$, $\tfrac38$ at $2$, $\tfrac18$ at $3$.

$$
F_X(x)=\begin{cases}0,&x<0\\ \frac18,&0\le x<1\\ \frac12,&1\le x<2\\ \frac78,&2\le x<3\\ 1,&x\ge3\end{cases}
$$

Step 2 · **Rewrite** $P(1<X\le3)$.

$$
F_X(3)-F_X(1)=1-\frac12=\frac12
$$

**Answer:**

$$
\text{a staircase }0\to\frac18\to\frac12\to\frac78\to1
$$

</details>

**What does it look like?** At each jump, the value is the **top** of the step (the dot).

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

<details><summary>Full example (Practice 03 Q9): from a CDF back to the PMF</summary>

Step 1 · $F_X=0$ for $x<-3$, $\tfrac38$ on $[-3,0)$, $\tfrac34$ on $[0,6)$, $1$ for $x\ge6$. It’s a staircase, so $X$ is **discrete**.

$$
X\in\{-3,\ 0,\ 6\}
$$

Step 2 · **Jumps** = the PMF.

$$
p_X(-3)=\frac38,\quad p_X(0)=\frac34-\frac38=\frac38,\quad p_X(6)=1-\frac34=\frac14
$$

Step 3 · **Rewrite** $P(-3<X\le6)$.

$$
F_X(6)-F_X(-3)=1-\frac38=\frac58
$$

Step 4 · **Rewrite** $P(X<0)$: the step just left of $0$.

$$
P(X<0)=\frac38
$$

**Answer:**

$$
p_X=\frac38,\ \frac38,\ \frac14\ \text{ at }-3,\ 0,\ 6
$$

</details>

## Case 4: a named family (spot the clue word)

**You’ll see:** a story. A clue word tells you the family; its PMF is ready-made. **Spot** the clue:

| Clue in the question | Family |
|---|---|
| **one** yes/no try | Bernoulli |
| **fixed number $n$** of tries, count successes | Binomial |
| tries **until the first** success | Geometric |
| tries **until the $r$-th** success | Negative Binomial |
| draw $n$ **without replacement** | Hypergeometric |
| “**on average** $\lambda$ per hour/page/year” | Poisson |

1. **Spot** the family and its numbers ($n$, $p$, $\lambda$, …).
2. **Write** its PMF with those numbers.
3. **Plug in** $k$. “At least” → $1-$ (the few below).

Open a card for the formula and a short example:

<details><summary>Bernoulli$(p)$: $\;P(1)=p$, $\;P(0)=1-p$</summary>

One yes/no try. Example: is the first of 12 accidents on June 13?

$$
P(Y=1)=\frac1{30},\qquad P(Y=0)=\frac{29}{30}
$$

</details>

<details><summary>Binomial$(n,p)$: $\;\dbinom nk\,p^k(1-p)^{n-k}$, $\;k=0,\dots,n$</summary>

$n$ independent tries, count the successes. Example: 8 bits, each wrong with $p=0.1$, exactly 1 wrong:

$$
\binom81(0.1)(0.9)^7\approx0.3826
$$

$\binom nk$ = “choose $k$ of $n$”, the only counting you need. On the Casio: `n nCr k`.

$$
\binom{8}{1}=8,\qquad \binom{10}{2}=45
$$

With replacement → Binomial. Without → Hypergeometric.

</details>

<details><summary>Geometric$(p)$: $\;(1-p)^{k-1}p$, $\;k=1,2,\dots$</summary>

Tries until the first success: $k-1$ failures, then a success. Example: each try works with $0.2$; succeed on try 3:

$$
(0.8)^2(0.2)=0.128
$$

Shortcut: “more than $k$ tries” = the first $k$ all failed.

$$
P(X>k)=(1-p)^k
$$

</details>

<details><summary>Negative Binomial$(r,p)$: $\;\dbinom{k-1}{r-1}p^r(1-p)^{k-r}$, $\;k=r,r+1,\dots$</summary>

Tries until the $r$-th success. The **last** try is a success; $\binom{k-1}{r-1}$ picks where the other $r-1$ go among the first $k-1$.

Example: free throws with $0.7$; the 3rd basket on shot 5.

$$
\binom42(0.7)^3(0.3)^2\approx0.1852
$$

</details>

<details><summary>Hypergeometric: $\;\dfrac{\binom Kk\binom{N-K}{n-k}}{\binom Nn}$</summary>

Draw $n$ from $N$ without replacement, $K$ of them “good”. Pick $k$ good **and** $n-k$ bad.

Example: 10 chips, 3 defective, choose 4. Exactly 1 defective:

$$
\frac{\binom31\binom73}{\binom{10}{4}}=\frac{3\cdot35}{210}=\frac12
$$

</details>

<details><summary>Poisson$(\lambda)$: $\;e^{-\lambda}\dfrac{\lambda^k}{k!}$, $\;k=0,1,2,\dots$</summary>

“On average $\lambda$ per …”. **Scale $\lambda$ to the time asked.** Example (Lecture 8): 4 emails per hour, exactly 3 next hour:

$$
P(X=3)=e^{-4}\frac{4^3}{3!}\approx0.1954
$$

Same rate, a 30-minute window: $\lambda=2$.

$$
P(X=0)=e^{-2}\approx0.1353
$$

</details>

> **Warning:** **Poisson: scale $\lambda$ to the time asked.** 7 per week, a question about one day → $\lambda=1$.

<details><summary>Shortcut: “at least” → one minus the rest</summary>

At least one:

$$
P(X\ge1)=1-P(X=0)
$$

At least 4 (Binomial, Poisson): subtract the few values below.

$$
P(X\ge4)=1-\big[P(0)+P(1)+P(2)+P(3)\big]
$$

</details>

**Problem: Try it 2 · Case 4 · Retransmit until it works** (intermediate)

A packet is sent again and again until one gets through. Each try works with probability $0.2$, independently. $X$ = number of tries. Find $P(X=3)$ and $P(X>3)$.

<details><summary>Solution</summary>

1. **Spot:** “until it works” → Geometric, $p=0.2$.
2. **Write** the PMF.

   $$P(X=k)=(0.8)^{k-1}(0.2)$$
3. **Plug in** $k=3$: fail, fail, work.

   $$P(X=3)=(0.8)^2(0.2)=0.128$$
4. $X>3$: the first 3 all failed (shortcut).

   $$P(X>3)=(0.8)^3=0.512$$

**Answer:** $P(X=3)=0.128$, $P(X>3)=0.512$

</details>

## Case 5: two families in one question

**You’ll see:** “in exactly 3 of the next 8 years…”, “the first day with no…”.

**The move:** one family **inside** gives the chance $q$ that a single year/day/page is “good”. Then **outside**, each year is a yes/no try with chance $q$.

1. **Inside:** use the first family (often Poisson with $k=0$) to get $q$.
2. **Outside:** count the good ones → Binomial$(n,q)$. Wait for the first → Geometric$(q)$.

**Short example:** typos are Poisson, 2 per page. A page is clean with $q=e^{-2}$. Exactly 1 of 5 pages clean:

$$\binom51\,q\,(1-q)^4,\qquad q=e^{-2}$$

## Practice Questions

> **Tip:** **Question 1 is always these cases, in parts (a), (b), (c).** Spot the case, run its steps:
> 
> 1. **No family:** List → Label → Add → Check.
> 2. **A $c$:** add every chance, set it to $1$.
> 3. **CDF:** running total; jumps = the PMF; $P(a<X\le b)=F(b)-F(a)$; whole numbers: $<$ → $\le$.
> 4. **Clue word:** Spot → Write → Plug in. Scale Poisson’s $\lambda$. “At least” → $1-$ the rest.
> 5. **Two families:** Inside gives $q$, Outside is Binomial or Geometric.

Test-style, easy → hard. Solve on paper first, then open the solution.

**Problem: Question 1 · Case 4 (Poisson) · Tutorial 3 Q3, Q5** (introductory)

A mail-order house gets on average **7 wrong-number calls per week** (Poisson). Find the probability that tomorrow they get (a) exactly two wrong-number calls, (b) at least one. (c) A book has on average one typo every **three pages** (Poisson). Find the chance a given page has at least one typo.

<details><summary>Solution</summary>

1. **Spot:** “on average” → Poisson. Scale $\lambda$ to one day.

   $$\lambda=\frac{7}{7}=1$$
2. (a) **Write** and **plug in** $k=2$.

   $$P(X=2)=e^{-1}\frac{1^2}{2!}\approx 0.1839$$
3. (b) **At least one** → one minus none.

   $$P(X\ge1)=1-e^{-1}\approx 0.6321$$
4. (c) Scale to one page: $\lambda=\tfrac13$. Then one minus none.

   $$P(X\ge1)=1-e^{-1/3}\approx 0.2835$$

**Answer:** (a) $\approx 0.1839$ (b) $\approx 0.6321$ (c) $\approx 0.2835$

</details>

**Problem: Question 2 · Case 1 · with and without replacement · like Practice 01 Q7** (introductory)

An urn has 2 black balls and 1 white ball. Two balls are drawn one after the other. $X$ = number of black balls drawn. Find the PMF of $X$ (a) **without** replacement, (b) **with** replacement. (c) Which one is a named family?

<details><summary>Solution</summary>

1. (a) **List** ordered draws, calling the black balls $B_1,B_2$: 6 equally likely.

   $$B_1B_2,\ B_2B_1,\ B_1W,\ B_2W,\ WB_1,\ WB_2$$
2. **Label** and **add:** two have both black, four have one, none have zero.

   $$P(X=2)=\frac26=\frac13,\quad P(X=1)=\frac46=\frac23,\quad P(X=0)=0$$
3. (b) With replacement, each draw is black with $\tfrac23$, independently. **Add** the orders for $X=1$.

   $$\begin{gathered}P(X=2)=\Big(\frac23\Big)^2=\frac49,\qquad P(X=0)=\Big(\frac13\Big)^2=\frac19 \\ P(X=1)=2\cdot\frac23\cdot\frac13=\frac49\end{gathered}$$
4. **Check:** both PMFs add to $1$.

   $$\frac13+\frac23=1,\qquad \frac49+\frac49+\frac19=1$$
5. (c) With replacement = independent tries → **Binomial**$(2,\tfrac23)$. Without → Hypergeometric.

**Answer:** (a) $0,\tfrac23,\tfrac13$ for $x=0,1,2$ (b) $\tfrac19,\tfrac49,\tfrac49$ (c) (b) is Binomial$(2,\tfrac23)$

</details>

**Problem: Question 3 · Case 2 + 3 · find $c$, then the CDF** (intermediate)

(a) $p_X(x)=c\,(x+1)$ for $x=0,1,2,3$. Find $c$, then $F_X(1.5)$ and $P(X\ge2)$. (b) $p_X(k)=c\,\dfrac{3^k}{k!}$ for $k=0,1,2,\dots$ Find $c$. Which family is this?

<details><summary>Solution</summary>

1. (a) **Find $c$:** add every chance.

   $$c(1+2+3+4)=10c=1\quad\Longrightarrow\quad c=\frac1{10}$$
2. So the PMF is $0.1,0.2,0.3,0.4$. **Accumulate** every value $\le1.5$: $x=0,1$.

   $$F_X(1.5)=0.1+0.2=0.3$$
3. **Rewrite:** $X\ge2$ is one minus $X\le1$.

   $$P(X\ge2)=1-F_X(1)=1-0.3=0.7$$
4. (b) **Find $c$** with the exponential series, $\sum\frac{3^k}{k!}=e^3$.

   $$c\,e^{3}=1\quad\Longrightarrow\quad c=e^{-3}$$
5. That’s the Poisson PMF with $\lambda=3$.

   $$X\sim\text{Poisson}(3)$$

**Answer:** (a) $c=\tfrac1{10}$, $F_X(1.5)=0.3$, $P(X\ge2)=0.7$ (b) $c=e^{-3}$, Poisson$(3)$

</details>

**Problem: Question 4 · Case 3 · CDF → PMF** (intermediate)

$X$ has CDF

$$
F_X(x)=\begin{cases}0,&x<1\\ 0.2,&1\le x<2\\ 0.5,&2\le x<4\\ 1,&x\ge4\end{cases}
$$

Find (a) the PMF, (b) $P(X<4)$, (c) $P(1<X\le4)$, (d) $P(X>2)$, (e) $P(X=3)$.

<details><summary>Solution</summary>

1. (a) **Jumps** at $1$, $2$, $4$ are the PMF.

   $$p_X(1)=0.2,\quad p_X(2)=0.5-0.2=0.3,\quad p_X(4)=1-0.5=0.5$$
2. (b) **Rewrite:** “$<4$” is the step just left of $4$.

   $$P(X<4)=0.5$$
3. (c) **Rewrite** as a difference.

   $$P(1<X\le4)=F(4)-F(1)=1-0.2=0.8$$
4. (d) **Rewrite** as one minus.

   $$P(X>2)=1-F(2)=1-0.5=0.5$$
5. (e) No jump at $3$.

   $$P(X=3)=0$$

**Answer:** (a) $0.2,0.3,0.5$ at $1,2,4$ (b) $0.5$ (c) $0.8$ (d) $0.5$ (e) $0$

</details>

**Problem: Question 5 · Case 4 (Hypergeometric) · Lecture 7** (intermediate)

You get 7 cards from a 52-card deck, without replacement. $X$ = number of queens. Find $P(X=k)$ for $k=0,1,2,3,4$, and $P(X\ge1)$.

<details><summary>Solution</summary>

1. **Spot:** without replacement, 4 queens out of 52 → Hypergeometric.
2. **Write:** pick $k$ queens **and** $7-k$ non-queens.

   $$P(X=k)=\frac{\binom4k\binom{48}{7-k}}{\binom{52}{7}}$$
3. **Plug in** $k=0,\dots,4$.

   $$\begin{gathered}P(0)\approx 0.5504,\quad P(1)\approx 0.3669,\quad P(2)\approx 0.0768 \\ P(3)\approx 0.0058,\quad P(4)\approx 0.00013\end{gathered}$$
4. At least one → one minus none.

   $$P(X\ge1)=1-P(X=0)\approx 0.4496$$

**Answer:** $\approx 0.5504,\ 0.3669,\ 0.0768,\ 0.0058,\ 0.00013$; $P(X\ge1)\approx 0.4496$

</details>

**Problem: Question 6 · Case 4 (Binomial, Bernoulli) · Tutorial 3 Q7** (intermediate)

A town had 12 accidents in June (30 days). Each accident is equally likely to be on any day, independently. (a) Let $Y=1$ if the first accident is on June 13, else $Y=0$. Name the family of $Y$ and give its PMF. (b) Find the probability that **at least 4** of the 12 fall on June 13.

<details><summary>Solution</summary>

1. (a) **Spot:** one yes/no try → Bernoulli.

   $$P(Y=1)=\frac1{30},\qquad P(Y=0)=\frac{29}{30}$$
2. (b) **Spot:** 12 tries, “success” = lands on June 13 → Binomial.

   $$n=12,\qquad p=\frac1{30}$$
3. **Write** and use the “at least” shortcut: one minus $k=0,1,2,3$.

   $$P(X\ge4)=1-\sum_{k=0}^{3}\binom{12}{k}\Big(\frac1{30}\Big)^k\Big(\frac{29}{30}\Big)^{12-k}$$
4. **Plug in.**

   $$P(X\ge4)\approx 0.00049$$

**Answer:** (a) Bernoulli$(\tfrac1{30})$ (b) $\approx 0.00049$, so 4 on one day is very unlikely by chance.

</details>

**Problem: Question 7 · Case 1 · toss until a head, at most 4 tosses** (intermediate)

A coin with $P(H)=p$ is tossed until the first head **or** until 4 tosses have been made. (a) Write the sample space. (b) Let $X$ = number of tosses. Find the PMF of $X$. (c) Evaluate it for $p=\tfrac12$.

<details><summary>Solution</summary>

1. (a) **List:** stop at the first $H$, or after 4 tosses.

   $$\Omega=\{H,\ TH,\ TTH,\ TTTH,\ TTTT\}$$
2. (b) **Label:** $X=1,2,3,4,4$. The tosses are independent, so multiply.

   $$p_X(1)=p,\quad p_X(2)=(1-p)p,\quad p_X(3)=(1-p)^2p$$
3. **Add:** **two** outcomes give $X=4$.

   $$p_X(4)=(1-p)^3p+(1-p)^4=(1-p)^3$$
4. (c) $p=\tfrac12$. **Check:** they add to $1$.

   $$\frac12+\frac14+\frac18+\frac18=1$$

**Answer:** $p,\ (1-p)p,\ (1-p)^2p,\ (1-p)^3$; for $p=\tfrac12$: $\tfrac12,\tfrac14,\tfrac18,\tfrac18$.

</details>

**Problem: Question 8 · Case 4 (Negative Binomial)** (intermediate)

A player makes each free throw with probability $0.7$, independently. $X$ = number of shots needed to make **3** baskets. (a) Name the family. (b) Find $P(X=5)$. (c) Find $P(X\le4)$. (d) Compare: the chance of exactly 3 baskets in 5 shots.

<details><summary>Solution</summary>

1. (a) **Spot:** “until the 3rd success” → Negative Binomial, $r=3$, $p=0.7$.
2. **Write** the PMF.

   $$P(X=k)=\binom{k-1}{2}(0.7)^3(0.3)^{k-3}$$
3. (b) **Plug in** $k=5$: shot 5 goes in, and 2 of the first 4.

   $$P(X=5)=\binom42(0.7)^3(0.3)^2\approx 0.1852$$
4. (c) Add $k=3$ and $k=4$.

   $$P(X\le4)=(0.7)^3+\binom32(0.7)^3(0.3)\approx 0.6517$$
5. (d) Binomial$(5,0.7)$: the 3 baskets can be **any** 3 of the 5, so it’s bigger.

   $$\binom53(0.7)^3(0.3)^2\approx 0.3087$$

**Answer:** (a) NB$(3,0.7)$ (b) $\approx 0.1852$ (c) $\approx 0.6517$ (d) $\approx 0.3087$

</details>

**Problem: Question 9 · Case 4 + 3 (Geometric and its CDF) · Practice 03 Q7** (advanced)

$N\sim$ Geometric$(p)$, so $P(N=k)=(1-p)^{k-1}p$ for $k=1,2,\dots$ (a) Find $P(N>k)$. (b) Find the CDF of $N$. (c) Find $P(N\text{ is even})$. (d) Find $P(N=k\mid N\le m)$.

<details><summary>Solution</summary>

1. (a) $N>k$ means the first $k$ tries all failed (shortcut).

   $$P(N>k)=(1-p)^k$$
2. (b) **Rewrite:** one minus the tail. Flat between whole numbers.

   $$F_N(k)=1-(1-p)^k,\quad k=1,2,\dots$$
3. (c) Add $k=2,4,6,\dots$: a geometric series with ratio $(1-p)^2$.

   $$\sum_{j=1}^{\infty}(1-p)^{2j-1}p=\frac{(1-p)p}{1-(1-p)^2}=\frac{1-p}{2-p}$$
4. (d) Conditional = (both) / (given). For $k\le m$, “$N=k$ and $N\le m$” is just $N=k$.

   $$P(N=k\mid N\le m)=\frac{(1-p)^{k-1}p}{1-(1-p)^m},\quad k=1,\dots,m$$

**Answer:** (a) $(1-p)^k$ (b) $1-(1-p)^k$ (c) $\dfrac{1-p}{2-p}$ (d) $\dfrac{(1-p)^{k-1}p}{1-(1-p)^m}$

</details>

**Problem: Question 10 · Case 5 (Poisson → Binomial, Geometric) · Tutorial 3 Q6** (advanced)

Earthquakes: on average 7 per year (Poisson). (a) Find the probability of no earthquakes in one year. (b) Find the probability that **exactly three of the next eight years** have no earthquakes. (c) Find the probability that the **first** quiet year is year 3.

<details><summary>Solution</summary>

1. (a) **Inside:** Poisson, $\lambda=7$, $k=0$.

   $$q=e^{-7}\approx 0.000912$$
2. (b) **Outside:** each year is a yes/no try (“quiet”, chance $q$), 8 years → Binomial$(8,q)$.

   $$P=\binom83q^3(1-q)^5\approx 4.23\times10^{-8}$$
3. (c) **Outside:** “first quiet year” → Geometric$(q)$: two loud years, then a quiet one.

   $$P=(1-q)^2q\approx 9.10\times10^{-4}$$

**Answer:** (a) $\approx 0.000912$ (b) $\approx 4.23\times10^{-8}$ (c) $\approx 9.10\times10^{-4}$

</details>
