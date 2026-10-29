# Test 2 - Question 2

**Lectures 9–11.** $X$ can be any number in an interval (a time, a voltage). Find $c$, the CDF, and probabilities.

## Question 2 in plain words

**You’ll see:** a PDF or CDF formula, or a story with “uniform”, “exponential” or “normal”. Then parts (a), (b), (c).

**The move: probability is area under the PDF.** The CDF is the area so far:

$$P(a<X\le b)=\int_a^b f_X(x)\,dx=F_X(b)-F_X(a)$$

- **Accumulate:** $F_X(x)=P(X\le x)$ = the area left of $x$. Same word as the running total in Question 1.
- **Differentiate:** the PDF is the slope of the CDF, $f_X=F_X^{\prime}$.
- **One exact value has chance $0$:** $P(X=2)=0$. So $<$ and $\le$ give the same answer.

**Short example:** $X$ uniform on $[0,4]$ is flat at $\tfrac14$:

$$P(1<X<3)=\underbrace{2}_{\text{width}}\cdot\underbrace{\frac14}_{\text{height}}=\frac12$$

**Which case?** Look for the clue:

| The question says… | Go to |
|---|---|
| “$f_X(x)=c\cdot(\dots)$, find $c$” | Case 1 |
| “find the CDF / PDF / $P(a<X<b)$” | Case 2 |
| “uniformly at random between…” | Case 3 |
| “exponential”, a lifetime, a waiting time | Case 4 |
| “normal” / “Gaussian” with $\mu$, $\sigma$ | Case 5 |
| “with probability $q$ it is exactly…”, a CDF with a jump | Case 6 |

## Case 1: find c (total area = 1)

**You’ll see:** “$f_X(x)=c\cdot(\dots)$. Find $c$”, or “show this is a PDF”.

**The move:** the whole area under a PDF is $1$. Write it, set it to $1$, solve:

$$\int_{-\infty}^{\infty}f_X(x)\,dx=1$$

1. **Spot:** the unknown is $c$.
2. **Find $c$:** integrate $f_X$ over the range where it isn’t $0$ (split at every break), set it to $1$.
3. **Check:** $f_X\ge0$ everywhere. It may be bigger than $1$, that’s fine.

**Short example:** $f_X(x)=c(1-x^4)$ on $[-1,1]$:

$$c\Big[x-\frac{x^5}{5}\Big]_{-1}^{1}=\frac{8c}{5}=1\quad\Longrightarrow\quad c=\frac58$$

<details><summary>Full example (Practice 02 Q1): $\;f_X(x)=c(1-x^4)$ on $[-1,1]$: find $c$, the CDF, $P(|X|<\tfrac12)$</summary>

Step 1 · **Find $c$:** total area $=1$.

$$
c\Big[x-\frac{x^5}{5}\Big]_{-1}^{1}=\frac{8c}{5}=1\quad\Longrightarrow\quad c=\frac58
$$

Step 2 · **Accumulate:** the area from $-1$ up to $x$. It’s $0$ before $-1$ and $1$ after $1$.

$$
F_X(x)=\frac58\int_{-1}^{x}(1-t^4)\,dt=\frac58\Big(x-\frac{x^5}{5}+\frac45\Big),\qquad -1\le x\le1
$$

Step 3 · **Rewrite:** $|X|<\tfrac12$ means $-\tfrac12<X<\tfrac12$. The PDF is symmetric, so double the area on $[0,\tfrac12]$.

$$
P\big(|X|<\tfrac12\big)=2\cdot\frac58\Big[x-\frac{x^5}{5}\Big]_0^{1/2}=\frac{79}{128}\approx 0.6172
$$

**Answer:**

$$
c=\frac58,\qquad P\big(|X|<\tfrac12\big)=\frac{79}{128}\approx 0.6172
$$

</details>

<details><summary>Shortcut: a triangle or rectangle PDF → use its area formula</summary>

Tutorial 4 Q2: $f(x)=\tfrac12-\tfrac14|x-3|$ on $[1,5]$ is a triangle: base $4$, peak height $f(3)=\tfrac12$.

$$
\text{area}=\frac12\cdot4\cdot\frac12=1\quad\checkmark
$$

Unknown height $c$, base $2a$ (Practice 02 Q2):

$$
\frac12\cdot2a\cdot c=1\quad\Longrightarrow\quad c=\frac1a
$$

</details>

<details><summary>Integrals you’ll need</summary>

Power rule:

$$
\int x^n\,dx=\frac{x^{n+1}}{n+1}
$$

Exponential (and $e^{-\lambda x}\to0$ as $x\to\infty$):

$$
\int e^{-\lambda x}\,dx=-\frac1\lambda\,e^{-\lambda x}
$$

By parts, for $x\,e^{-x}$ (take $u=x$):

$$
\int x\,e^{-x}\,dx=-(x+1)\,e^{-x}
$$

Shortcut (not from the lectures):

$$
\int_0^{\infty}x^n\,e^{-\lambda x}\,dx=\frac{n!}{\lambda^{n+1}}
$$

</details>

## Case 2: PDF → CDF → probabilities

**You’ll see:** “find the CDF”, “find the PDF from this CDF”, “find $P(a<X<b)$”.

**The move:** go back and forth between the two, then turn every probability into $F$’s:

$$F_X(x)=\int_{-\infty}^{x}f_X(t)\,dt\qquad\Longleftrightarrow\qquad f_X(x)=F_X^{\prime}(x)$$

1. **Accumulate** (PDF → CDF): the area from the left end up to $x$. Do it piece by piece. $0$ before the range, $1$ after.
2. **Differentiate** (CDF → PDF): the slope of each piece.
3. **Rewrite** the probability with $F$’s (card below), then **plug in**.

<details><summary>Rewrite: turn any probability into $F$’s</summary>

Example: $F_X(x)=\tfrac x4$ on $[0,4]$.

Up to $b$:

$$
P(X\le b)=F_X(b)\qquad\qquad P(X\le1)=\frac14
$$

Above $a$:

$$
P(X>a)=1-F_X(a)\qquad\qquad P(X>1)=\frac34
$$

Between:

$$
P(a<X<b)=F_X(b)-F_X(a)\qquad\qquad P(2<X<3)=\frac34-\frac24=\frac14
$$

One point:

$$
P(X=a)=0
$$

</details>

**Short example:** $f_X(x)=\tfrac x2$ on $[0,2]$:

$$F_X(x)=\int_0^x\frac t2\,dt=\frac{x^2}{4}\quad\Longrightarrow\quad P(X>1)=1-\frac14=\frac34$$

<details><summary>Full example (Lecture 9): read a CDF, $\;F_X(x)=\tfrac x4$ on $[0,4]$</summary>

Step 1 · (a) $P(X\le-1)$: left of the range.

$$
F_X(-1)=0
$$

Step 2 · (b) $P(X\le1)$.

$$
F_X(1)=\frac14
$$

Step 3 · (c) $P(2<X\le3)$: **Rewrite** as a difference.

$$
F_X(3)-F_X(2)=\frac34-\frac24=\frac14
$$

Step 4 · (d) $P(X>1)$: one minus.

$$
1-F_X(1)=\frac34
$$

Step 5 · (e) $P(X=1)$: one point.

$$
0
$$

Step 6 · **Differentiate** for the PDF.

$$
f_X(x)=\frac14,\qquad 0\le x\le4\quad(0\text{ elsewhere})
$$

**Answer:**

$$
0,\ \ \frac14,\ \ \frac14,\ \ \frac34,\ \ 0;\qquad f_X=\frac14\ \text{on }[0,4]
$$

</details>

<details><summary>Full example (Tutorial 4 Q2): a triangle PDF, piece by piece</summary>

Step 1 · $f(x)=\tfrac12-\tfrac14|x-3|$ on $[1,5]$. Split at the peak: left $\tfrac{x-1}{4}$, right $\tfrac{5-x}{4}$.

Step 2 · **Accumulate**, left half: the area of a small triangle.

$$
F(x)=\int_1^x\frac{t-1}{4}\,dt=\frac{(x-1)^2}{8},\qquad 1\le x\le3
$$

Step 3 · **Accumulate**, right half: $1$ minus the small triangle still to come.

$$
F(x)=1-\frac{(5-x)^2}{8},\qquad 3\le x\le5
$$

Step 4 · **Rewrite** $P(2<X<3.5)$.

$$
F(3.5)-F(2)=\Big(1-\frac{1.5^2}{8}\Big)-\frac18=\frac{19}{32}\approx0.5938
$$

**Answer:**

$$
F(x)=\begin{cases}0,&x<1\\ \frac{(x-1)^2}{8},&1\le x\le3\\ 1-\frac{(5-x)^2}{8},&3\le x\le5\\ 1,&x>5\end{cases}
$$

</details>

## Case 3: uniform

**You’ll see:** “uniformly at random between $a$ and $b$”.

**The move:** a flat PDF, so every probability is **length ÷ total length**:

$$f_X(x)=\frac{1}{b-a},\qquad F_X(x)=\frac{x-a}{b-a},\qquad a\le x\le b$$

$$P(\text{X lands in a piece})=\frac{\text{length of the piece}}{b-a}$$

**Short example** (Tutorial 2 Q5): a bus comes uniformly between 1:00 and 1:30. Wait at least 10 minutes:

$$P(X\ge10)=\frac{30-10}{30}=\frac23$$

<details><summary>Full example (Tutorial 3 Q1): pick $X$ uniformly in $(0,\tfrac\pi2)$. Chance $\sin X>\cos X$?</summary>

Step 1 · **Spot:** uniform on $(0,\tfrac\pi2)$, total length $\tfrac\pi2$.

Step 2 · **Rewrite** the event: $\sin x$ passes $\cos x$ at $x=\tfrac\pi4$.

$$
\sin X>\cos X\iff X>\frac\pi4
$$

Step 3 · Length ÷ total length.

$$
P=\frac{\frac\pi2-\frac\pi4}{\frac\pi2}=\frac12
$$

**Answer:**

$$
\frac12
$$

</details>

## Case 4: exponential

**You’ll see:** a lifetime or a waiting time, “exponential with $\lambda=\dots$” ($\lambda$ = the rate, per hour/minute).

**The move:** use the **tail**. You’ll need it more than the CDF:

$$f_X(x)=\lambda e^{-\lambda x},\qquad F_X(x)=1-e^{-\lambda x},\qquad P(X>x)=e^{-\lambda x}\qquad(x\ge0)$$

1. **Spot:** exponential, and read $\lambda$. Given the **mean** instead? Then $\lambda=\dfrac{1}{\text{mean}}$.
2. **Rewrite** with tails: $P(a<X<b)=e^{-\lambda a}-e^{-\lambda b}$.
3. **Plug in.**

**Short example:** lifetime with $\lambda=0.002$ per hour. Lasts at least 500 hours:

$$P(X>500)=e^{-0.002\cdot500}=e^{-1}\approx 0.3679$$

<details><summary>Memoryless: $\;P(X>s+t\mid X>s)=P(X>t)$</summary>

Time already waited doesn’t matter: an old part is as good as new.

To use it: “already lasted $s$, chance of $t$ more” is a ratio of tails.

$$
\frac{P(X>s+t)}{P(X>s)}=\frac{e^{-\lambda(s+t)}}{e^{-\lambda s}}=e^{-\lambda t}
$$

</details>

<details><summary>Full example (Tutorial 4 Q3): a TV tube is 10 years old, $\lambda=0.1$. Chance it lasts another 10?</summary>

Step 1 · **Spot:** exponential, $\lambda=0.1$, and “already lasted” → memoryless.

$$
P(X>20\mid X>10)
$$

Step 2 · **Rewrite** as a ratio of tails.

$$
\frac{P(X>20)}{P(X>10)}=\frac{e^{-2}}{e^{-1}}=e^{-1}
$$

Step 3 · Same as a new tube lasting 10 years.

$$
P(X>10)=e^{-0.1\cdot10}=e^{-1}\approx 0.3679
$$

**Answer:**

$$
e^{-1}\approx 0.3679
$$

</details>

## Case 5: Gaussian (normal)

**You’ll see:** “normal with mean $\mu$ and standard deviation $\sigma$” (or variance $\sigma^2$): $X\sim N(\mu,\sigma^2)$.

**The move:** you can’t integrate the bell curve. **Standardise** to $z$ and read $\Phi(z)=P(Z\le z)$ from the table:

$$F_X(x)=\Phi\Big(\frac{x-\mu}{\sigma}\Big),\qquad \Phi(-z)=1-\Phi(z)$$

1. **Spot:** read $\mu$ and $\sigma$. Given the **variance**? Take its square root first.
2. **Standardise** every number: $z=\dfrac{x-\mu}{\sigma}$.
3. **Rewrite** with $\Phi$: $P(X>x)=1-\Phi(z)$, $\;P(a<X<b)=\Phi(z_b)-\Phi(z_a)$. Negative $z$? $\Phi(-z)=1-\Phi(z)$.
4. **Table.**

| $z$ | 0.5 | 1.0 | 1.28 | 1.5 | 1.645 | 1.96 | 2.0 | 2.5 |
|---|---|---|---|---|---|---|---|---|
| $\Phi(z)$ | 0.6915 | 0.8413 | 0.8997 | 0.9332 | 0.95 | 0.9750 | 0.97725 | 0.99379 |

**Short example:** $\mu=0$, $\sigma=0.5$, find $P(X<1)$:

$$z=\frac{1-0}{0.5}=2\quad\Longrightarrow\quad P(X<1)=\Phi(2)=0.97725$$

<details><summary>Shortcut: a symmetric interval, $\;P(|X-\mu|<k\sigma)=2\Phi(k)-1$</summary>

Both tails are the same size, so take $\Phi(k)$ and remove one tail twice.

$$
\Phi(k)-\Phi(-k)=\Phi(k)-\big(1-\Phi(k)\big)=2\Phi(k)-1
$$

Example: within $1.5\sigma$ of the mean.

$$
2(0.9332)-1=0.8664
$$

</details>

<details><summary>Backwards: given a probability, find $x$ $\;\Longrightarrow\;x=\mu+z\sigma$</summary>

Find the $z$ in the table whose $\Phi(z)$ is the probability **below** $x$, then undo the standardising.

$$
x=\mu+z\,\sigma
$$

Top $5\%$ → $95\%$ below → $z=1.645$. Middle $95\%$ → $\Phi(z)=0.975$ → $z=1.96$.

</details>

<details><summary>Full example (Lecture 11): sensor error, $\;\mu=0$, $\;\sigma=0.5$. Chance $|X|<0.8$?</summary>

Step 1 · **Rewrite:** $|X|<0.8$ means $-0.8<X<0.8$.

Step 2 · **Standardise** both ends.

$$
z=\frac{\pm0.8-0}{0.5}=\pm1.6
$$

Step 3 · Negative $z$: flip it.

$$
\Phi(1.6)-\Phi(-1.6)=\Phi(1.6)-\big(1-\Phi(1.6)\big)=2\Phi(1.6)-1
$$

Step 4 · **Table:** $\Phi(1.6)=0.9452$.

$$
2(0.9452)-1=0.8904
$$

**Answer:**

$$
0.8904
$$

</details>

<details><summary>Full example (Tutorial 4 Q4): scores $N(500,100^2)$. Which score is the top $10\%$?</summary>

Step 1 · **Rewrite:** top $10\%$ means $90\%$ below.

$$
\Phi\Big(\frac{x-500}{100}\Big)=0.90
$$

Step 2 · **Table, backwards:** $\Phi(1.28)=0.8997$ is closest to $0.90$.

$$
z\approx1.28
$$

Step 3 · Undo the standardising.

$$
x=500+1.28\cdot100=628
$$

**Answer:**

$$
\text{about }628
$$

</details>

> **Warning:** **Variance or standard deviation?** “$\sigma^2=2.25$” means $\sigma=1.5$. Dividing by $2.25$ is the most common lost mark.

**Problem: Try it 1 · Case 5 · Blood pressure · Practice 03 Q8** (intermediate)

Diastolic blood pressure is normal with $\mu=80$, $\sigma=7$ (mm Hg). $\ge95$ is hypertensive; strictly between $89$ and $95$ is mild hypertension. What percent of people are in each group?

<details><summary>Solution</summary>

1. **Spot:** Gaussian, $\mu=80$, $\sigma=7$.
2. **Standardise** both cut-offs (2 decimals, like the table).

   $$\begin{gathered}z_{95}=\frac{95-80}{7}\approx2.14 \\ z_{89}=\frac{89-80}{7}\approx1.29\end{gathered}$$
3. **Rewrite**, hypertensive: the right tail. **Table.**

   $$P(X\ge95)=1-\Phi(2.14)=1-0.98382=0.01618$$
4. **Rewrite**, mild: between the two. **Table.**

   $$\begin{gathered}P(89<X<95)=\Phi(2.14)-\Phi(1.29) \\ =0.98382-0.9015=0.0823\end{gathered}$$

**Answer:** Mild ≈ 8.23%, hypertensive ≈ 1.62%

</details>

## Case 6: mixed (a jump and a ramp)

**You’ll see:** “with probability $q$ it is exactly $x_0$, otherwise it is spread over…”, or a CDF that jumps **and** ramps.

**The move:** the jump is an exact chance. The spread part only has the **leftover** area $1-q$:

$$P(X=x_0)=\text{jump size},\qquad f_{\text{spread}}=(1-q)\times(\text{its usual PDF})$$

1. **Jump:** $P(X=x_0)=q$ (or read the jump size off the CDF).
2. **Spread:** the usual PDF times $1-q$.
3. **Rewrite:** any probability = the jumps inside the range + the area over the range.

**Short example:** signal lost ($X=0$) with chance $0.2$, otherwise uniform on $(0,10)$:

$$f_{\text{spread}}=0.8\cdot\frac1{10}=0.08\quad\Longrightarrow\quad P(2<X<5)=0.08\cdot3=0.24$$

<details><summary>Full example (Lectures 10–11): received signal level, the CDF</summary>

Step 1 · **Jump** at $0$: the lost signal.

$$
P(X=0)=0.2
$$

Step 2 · **Spread:** uniform on $(0,10)$ scaled by $0.8$.

$$
f(x)=0.8\cdot\frac1{10}=0.08,\qquad 0<x<10
$$

Step 3 · **Accumulate:** jump first, then the ramp.

$$
F_X(x)=\begin{cases}0,&x<0\\ 0.2+0.08x,&0\le x<10\\ 1,&x\ge10\end{cases}
$$

Step 4 · **Rewrite** $P(2<X<5)$: the jump at $0$ isn’t inside, so only area.

$$
F_X(5)-F_X(2)=0.6-0.36=0.24
$$

**Answer:**

$$
\text{jump }0.2\text{ at }0,\ \text{then a ramp up to }1\text{ at }x=10
$$

</details>

**Discrete = all jumps, continuous = all slope, mixed = both.**

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

**Problem: Try it 2 · Case 6 · Daily rainfall** (intermediate)

On a given day it doesn’t rain with probability $0.6$ ($X=0$). If it rains, the amount $X$ (mm) is exponential with $\lambda=0.5$. (a) Find the CDF of $X$. (b) Find $P(X>2)$. (c) Find $P(X\le1)$.

<details><summary>Solution</summary>

1. **Spot:** an exact value with chance $0.6$, plus a spread → Case 6.
2. (a) **Jump** of $0.6$ at $0$, then **spread:** the exponential CDF scaled by $0.4$.

   $$F_X(x)=\begin{cases}0,&x<0\\ 0.6+0.4\left(1-e^{-0.5x}\right),&x\ge0\end{cases}$$
3. (b) **Rewrite:** only rainy days can go above 2. Exponential tail times $0.4$.

   $$P(X>2)=0.4\,e^{-0.5\cdot2}=0.4e^{-1}\approx 0.1472$$
4. (c) **Rewrite:** $F_X(1)$, which includes the jump at $0$.

   $$P(X\le1)=0.6+0.4(1-e^{-0.5})\approx 0.7574$$

**Answer:** (a) jump $0.6$ at $0$, then $0.6+0.4(1-e^{-0.5x})$ (b) $\approx 0.1472$ (c) $\approx 0.7574$

</details>

## Practice Questions

> **Tip:** **Question 2 is always these cases, in parts (a), (b), (c).** Spot the clue, run its steps:
> 
> 1. **Find $c$:** total area $=1$ (triangle/rectangle: area formula).
> 2. **PDF ↔ CDF:** Accumulate (area so far), Differentiate (slope), Rewrite with $F$'s.
> 3. **Uniform:** length ÷ total length.
> 4. **Exponential:** $P(X>x)=e^{-\lambda x}$; “already lasted” → memoryless.
> 5. **Gaussian:** $z=\frac{x-\mu}{\sigma}$ → $\Phi$ table; $\Phi(-z)=1-\Phi(z)$; backwards $x=\mu+z\sigma$.
> 6. **Mixed:** jump = exact chance; spread × $(1-q)$; add jumps + area.

Test-style, easy → hard. Solve on paper first, then open the solution.

**Problem: Question 1 · Case 3 · Uniform · Tutorial 4 Q5** (introductory)

Flights leave every half hour (9:00, 9:30, 10:00, …). A passenger arrives at a uniform random time between 8:45 and 9:45 A.M. Find the probability the passenger waits (a) **at most 10 minutes**, (b) **at least 15 minutes**.

<details><summary>Solution</summary>

1. **Type:** uniform → Case 3. $T$ = minutes after 8:45, total length $60$. Flights leave at $T=15,\ 45,\ 75$.

   $$f_T(t)=\frac1{60},\quad 0\le t\le60$$
2. (a) **Rewrite:** wait $\le10$ means arriving in the 10 minutes before a flight.

   $$T\in[5,15]\cup[35,45]$$
3. Length ÷ total length.

   $$P=\frac{10+10}{60}=\frac13$$
4. (b) **Rewrite:** wait $\ge15$ means the next flight is 15+ minutes away.

   $$T\in[15,30]\cup[45,60]$$
5. Length ÷ total length.

   $$P=\frac{15+15}{60}=\frac12$$

**Answer:** (a) $\tfrac13$ (b) $\tfrac12$

</details>

**Problem: Question 2 · Case 4 · Exponential, memoryless · like Lecture 10** (introductory)

The length $X$ (minutes) of a phone call is exponential with $\lambda=0.25$. Find (a) $P(X>4)$, (b) $P(2<X<6)$, (c) the chance a call that has already lasted 3 minutes lasts **more than 7** in total, (d) the time $t$ with $P(X>t)=\tfrac12$.

<details><summary>Solution</summary>

1. **Type:** exponential, $\lambda=0.25$ → Case 4.
2. (a) **Rewrite** as a tail. **Plug in.**

   $$P(X>4)=e^{-0.25\cdot4}=e^{-1}\approx 0.3679$$
3. (b) **Rewrite:** difference of two tails.

   $$P(2<X<6)=e^{-0.5}-e^{-1.5}\approx 0.3834$$
4. (c) **Memoryless:** 4 more minutes, as if new.

   $$P(X>7\mid X>3)=P(X>4)=e^{-1}\approx 0.3679$$
5. (d) **Backwards:** set the tail to $\tfrac12$, take $\ln$.

   $$e^{-0.25t}=\frac12\quad\Longrightarrow\quad t=4\ln2\approx 2.77\text{ min}$$

**Answer:** (a) $\approx 0.3679$ (b) $\approx 0.3834$ (c) $\approx 0.3679$ (d) $4\ln2\approx 2.77$ min

</details>

**Problem: Question 3 · Case 2 · CDF → probabilities and PDF · Practice 02 Q4** (intermediate)

The Rayleigh random variable $R$ has CDF

$$
F_R(r)=\begin{cases}0,&r<0\\ 1-e^{-r^2/(2\sigma^2)},&r\ge0\end{cases}
$$

(a) Find $P(\sigma\le R\le2\sigma)$ and $P(R>3\sigma)$. (b) Find the PDF of $R$.

<details><summary>Solution</summary>

1. **Type:** a CDF is given → Case 2.
2. (a) **Rewrite** as a difference. $\sigma$ cancels in each power.

   $$P(\sigma\le R\le2\sigma)=F_R(2\sigma)-F_R(\sigma)=e^{-1/2}-e^{-2}\approx 0.4712$$
3. **Rewrite** as one minus: $\tfrac{(3\sigma)^2}{2\sigma^2}=\tfrac92$.

   $$P(R>3\sigma)=1-F_R(3\sigma)=e^{-9/2}\approx 0.0111$$
4. (b) **Differentiate** (chain rule: the inside $-\tfrac{r^2}{2\sigma^2}$ has slope $-\tfrac{r}{\sigma^2}$).

   $$f_R(r)=\frac{r}{\sigma^2}\,e^{-r^2/(2\sigma^2)},\qquad r\ge0$$

**Answer:** (a) $e^{-1/2}-e^{-2}\approx 0.4712$; $e^{-9/2}\approx 0.0111$ (b) $\dfrac{r}{\sigma^2}e^{-r^2/(2\sigma^2)}$ for $r\ge0$

</details>

**Problem: Question 4 · Case 1 + 2 · Find $c$, then the CDF · Tutorial 5 Q5** (intermediate)

$X$ has PDF $f_X(x)=Cx^2$ for $|x|\le1$, and $0$ otherwise. (a) Find $C$. (b) Find the CDF. (c) Find $P(X>\tfrac12)$ and $P(|X|<\tfrac12)$.

<details><summary>Solution</summary>

1. (a) **Type:** unknown constant → Case 1. **Find $c$:** total area $=1$.

   $$C\int_{-1}^{1}x^2\,dx=\frac{2C}{3}=1\quad\Longrightarrow\quad C=\frac32$$
2. (b) **Accumulate** from $-1$ up to $x$ (Case 2).

   $$F_X(x)=\int_{-1}^{x}\frac32t^2\,dt=\frac{x^3+1}{2},\qquad -1\le x\le1$$
3. (c) **Rewrite** as one minus.

   $$P(X>\frac12)=1-\frac{\frac18+1}{2}=\frac{7}{16}$$
4. **Rewrite** as a difference. Small, because the PDF is near $0$ around $x=0$.

   $$F(\frac12)-F(-\frac12)=\frac{\frac98-\frac78}{2}=\frac18$$

**Answer:** (a) $C=\tfrac32$ (b) $\tfrac{x^3+1}{2}$ on $[-1,1]$ (c) $\tfrac7{16}$ and $\tfrac18$

</details>

**Problem: Question 5 · Case 1 + 2 · Find $c$ by parts · Tutorial 4 Q1** (intermediate)

The time $X$ (minutes) between seeing two runners has PDF $f(x)=\lambda x e^{-x}$ for $x>0$. (a) Find $\lambda$. (b) Find the CDF. (c) Find the probability the next runner is seen in 2 to 5 minutes, and in at least 7 minutes.

<details><summary>Solution</summary>

1. **Type:** unknown constant → Case 1. First the integral, **by parts** ($u=x$, $dv=e^{-x}dx$):

   $$\int xe^{-x}\,dx=-xe^{-x}+\int e^{-x}\,dx=-(x+1)e^{-x}$$
2. (a) **Find $c$:** total area $=1$. (Shortcut: $\int_0^\infty xe^{-x}dx=\tfrac{1!}{1^2}=1$.)

   $$\lambda\Big[-(x+1)e^{-x}\Big]_0^{\infty}=\lambda(0+1)=1\quad\Longrightarrow\quad\lambda=1$$
3. (b) **Accumulate** from $0$ to $x$ ($0$ for $x<0$).

   $$F(x)=\Big[-(t+1)e^{-t}\Big]_0^{x}=1-(1+x)e^{-x}$$
4. (c) **Rewrite** as a difference.

   $$P(2<X<5)=F(5)-F(2)=3e^{-2}-6e^{-5}\approx 0.3656$$
5. **Rewrite** as one minus.

   $$P(X\ge7)=1-F(7)=8e^{-7}\approx 0.0073$$

**Answer:** $\lambda=1$; $F(x)=1-(1+x)e^{-x}$; $\approx 0.3656$ and $\approx 0.0073$

</details>

**Problem: Question 6 · Case 1 + 2 · a triangle, then work backwards · Practice 02 Q2** (intermediate)

$X$ has a triangle PDF: $0$ at $x=-a$, peak height $c$ at $x=0$, back to $0$ at $x=a$. (a) Find $c$ and $f_X(x)$. (b) Find the CDF. (c) Find $b$ with $P(|X|<b)=\tfrac12$.

<details><summary>Solution</summary>

1. (a) **Type:** unknown height → Case 1. **Find $c$** with the triangle shortcut: base $2a$, height $c$.

   $$\frac12(2a)c=1\quad\Longrightarrow\quad c=\frac1a$$
2. The two sides are straight lines down from the peak.

   $$f_X(x)=\frac1a\Big(1-\frac{|x|}{a}\Big),\qquad |x|\le a$$
3. (b) **Accumulate:** left half = a small triangle; right half = $1$ minus the small triangle still to come.

   $$F_X(x)=\begin{cases}0,&x<-a\\ \frac{(a+x)^2}{2a^2},&-a\le x\le0\\ 1-\frac{(a-x)^2}{2a^2},&0\le x\le a\\ 1,&x>a\end{cases}$$
4. (c) **Rewrite:** $F(b)-F(-b)$. Each tail outside $[-b,b]$ is $\tfrac{(a-b)^2}{2a^2}$.

   $$1-\frac{(a-b)^2}{a^2}=\frac12\quad\Longrightarrow\quad\frac{a-b}{a}=\frac1{\sqrt2}$$
5. Solve for $b$.

   $$b=a\Big(1-\frac1{\sqrt2}\Big)\approx 0.293\,a$$

**Answer:** (a) $c=\tfrac1a$ (b) as above (c) $b=a(1-\tfrac1{\sqrt2})\approx0.293a$

</details>

**Problem: Question 7 · Case 5 · Gaussian · Tutorial 6 Q5** (intermediate)

A rover’s distance travelled is $X\sim N(\mu,\sigma^2)$ with $\mu=500$ m and $\sigma^2=2.25$ m². Find (a) $P(X<500)$, (b) $P(X=501)$, (c) $P(X>501)$ and $P(X>505)$.

<details><summary>Solution</summary>

1. **Type:** normal → Case 5. **Spot:** that’s the variance, so take the root.

   $$\sigma=\sqrt{2.25}=1.5$$
2. (a) $500$ is the centre: half the bell is below it.

   $$P(X<500)=0.5$$
3. (b) One point of a continuous $X$.

   $$P(X=501)=0$$
4. (c) **Standardise**, then **Rewrite** as one minus. **Table.**

   $$\begin{gathered}z=\frac{501-500}{1.5}\approx0.67 \\ P(X>501)=1-\Phi(0.67)=1-0.7486=0.2514\end{gathered}$$
5. $z=\tfrac{5}{1.5}\approx3.33$ is off the table ($\Phi\approx1$).

   $$P(X>505)=1-\Phi(3.33)\approx 0.0004$$

**Answer:** (a) $0.5$ (b) $0$ (c) $\approx0.2514$ and $\approx0.0004$

</details>

**Problem: Question 8 · Case 5 · Gaussian, backwards · like Tutorial 4 Q4** (intermediate)

Resistances are normal with $\mu=100\ \Omega$ and variance $4\ \Omega^2$. (a) What fraction are within $100\pm3\ \Omega$? (b) Find $t$ so that $95\%$ are within $100\pm t$. (c) Which value is exceeded by only $5\%$?

<details><summary>Solution</summary>

1. **Type:** normal → Case 5. **Spot:** variance $4$, so $\sigma=2$.

   $$\sigma=2$$
2. (a) **Standardise:** $z=\tfrac32=1.5$. Symmetric interval shortcut.

   $$2\Phi(1.5)-1=2(0.9332)-1=0.8664$$
3. (b) **Backwards:** $2\Phi(z)-1=0.95$, so $\Phi(z)=0.975$. Then $t=z\sigma$.

   $$z=1.96\quad\Longrightarrow\quad t=1.96\cdot2=3.92\ \Omega$$
4. (c) **Backwards**, one tail: $\Phi(z)=0.95$, so $z=1.645$. Then $x=\mu+z\sigma$.

   $$x=100+1.645\cdot2=103.29\ \Omega$$

**Answer:** (a) $0.8664$ (b) $t=3.92\ \Omega$ (c) $103.29\ \Omega$

</details>

**Problem: Question 9 · Case 6 · a CDF with two jumps** (intermediate)

A clipped sensor reading $X$ has CDF

$$
F_X(x)=\begin{cases}0,&x<0\\ 0.25+\tfrac x2,&0\le x<1\\ 1,&x\ge1\end{cases}
$$

(a) Why is $X$ mixed? (b) Find $P(X=0)$ and $P(X=1)$. (c) Find $P(0<X<1)$ and $P(X\le0.5)$. (d) Find the PDF of the spread part.

<details><summary>Solution</summary>

1. (a) **Type:** $F$ jumps (exact values with real chance) **and** ramps → Case 6.

   $$\text{jumps at }0\text{ and }1,\ \text{ramp in between}$$
2. (b) **Jump** sizes. At $1$, $F$ goes from $0.25+0.5=0.75$ up to $1$.

   $$P(X=0)=0.25,\qquad P(X=1)=1-0.75=0.25$$
3. (c) **Rewrite:** only the ramp is strictly inside $(0,1)$.

   $$P(0<X<1)=0.75-0.25=0.5$$
4. $P(X\le0.5)$ is just $F(0.5)$, jump at $0$ included.

   $$P(X\le0.5)=F(0.5)=0.25+0.25=0.5$$
5. (d) **Differentiate** the ramp. Check: $0.25+0.25+0.5=1$.

   $$f(x)=\frac12,\qquad 0<x<1$$

**Answer:** (b) $0.25$, $0.25$ (c) $0.5$, $0.5$ (d) $\tfrac12$ on $(0,1)$

</details>

**Problem: Question 10 · Case 6 · Practice 02 Q3** (advanced)

$X$ has CDF

$$
F_X(x)=\begin{cases}0,&x<-1\\ \tfrac13+\tfrac23(x+1)^2,&-1\le x\le0\\ 1,&x>0\end{cases}
$$

Find the probabilities of $A=\{X>\tfrac13\}$, $B=\{|X|\ge1\}$, $C=\{|X-\tfrac13|<1\}$, $D=\{X<0\}$.

<details><summary>Solution</summary>

1. **Type:** $F$ jumps from $0$ to $\tfrac13$ at $x=-1$, then rises smoothly → Case 6.

   $$P(X=-1)=\frac13$$
2. $A$: **Rewrite** as one minus. $X$ is never above $0$.

   $$P(A)=1-F_X(\frac13)=0$$
3. $B$: $X\ge1$ can’t happen, and $X\le-1$ means $X=-1$ (the jump).

   $$P(B)=F_X(-1)=\frac13$$
4. $C$ is $-\tfrac23<X<\tfrac43$. **Rewrite**; no jump at $-\tfrac23$.

   $$P(C)=1-F_X(-\frac23)=1-\Big(\frac13+\frac23\cdot\frac19\Big)=\frac{16}{27}$$
5. $D$: no jump at $0$ ($\tfrac13+\tfrac23=1$), so $P(X<0)=F_X(0)$.

   $$P(D)=F_X(0)=1$$

**Answer:** $P(A)=0$, $P(B)=\tfrac13$, $P(C)=\tfrac{16}{27}$, $P(D)=1$

</details>
