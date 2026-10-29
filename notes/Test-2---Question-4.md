# Test 2 - Question 4

**Lectures 12–15 · Tutorial 6.** You know $X$. Find the CDF and PDF of a new random variable $Y=g(X)$.

## Question 4 in plain words

**You’ll see:** “$X$ is … Find the CDF and PDF of $Y=g(X)$.” For example:

$$X\sim U(-1,1),\qquad Y=X^3$$

**The move: always go through the CDF.** Three steps, every time:

$$\text{Range}\ \longrightarrow\ F_Y(y)=P\big(g(X)\le y\big)\ \longrightarrow\ f_Y(y)=\frac{d}{dy}F_Y(y)$$

- **Range:** where can $Y$ land? Below that, $F_Y=0$. Above it, $F_Y=1$.
- **Accumulate:** rewrite “$g(X)\le y$” as a statement about $X$, then use $X$’s CDF.
- **Differentiate:** the PDF is the slope of the CDF.

**Which case?** Look at the shape of $g$:

| $g$ looks like | Example | Go to |
|---|---|---|
| $X$ discrete, or $g$ a staircase | $X^2$ of a die | Case 1 |
| only goes up | $X^3$, $e^X$ | Case 2 |
| only goes down | $-3X+2$, $-\ln X$ | Case 3 |
| turns around | $X^2$, $|X|$, $\cos X$ | Case 4 |
| goes flat somewhere | $\max\{X,0\}$ | Case 5 |

**First, spot what type $Y$ is.** It tells you what the answer looks like:

- **Discrete** (a PMF): $X$ discrete, or $g$ a staircase. Example: a 1-bit converter, $B=0$ or $1$.
- **Continuous** (a PDF): $X$ continuous and $g$ has no flat piece. Example: $X^3$.
- **Mixed** (a jump and a slope): $g$ is flat on some interval. Example: $\max\{X,0\}$.

## Case 1: discrete Y (add what lands on the same value)

**You’ll see:** $X$ takes a list of values (or $g$ is a staircase). Find the PMF of $Y$.

**The move:** push each value of $X$ through $g$. If several $x$ land on the same $y$, **add** their chances:

$$p_Y(y)=\sum_{x:\ g(x)=y}p_X(x)$$

**Short example:** $X$ equally likely $-2,-1,0,1,2$, and $Y=X^2$:

$$(\pm1)^2=1\quad\Longrightarrow\quad p_Y(1)=\frac15+\frac15=\frac25$$

<details><summary>Full example (like Lecture 13): a 3-level quantizer</summary>

Step 1 · $X\sim U(-1,1)$. $Y=-1$ if $X<-0.5$, $Y=0$ if $-0.5\le X\le0.5$, $Y=1$ if $X>0.5$.

Step 2 · **Spot:** $g$ is a staircase with three outputs, so $Y$ is **discrete**.

$$
Y\in\{-1,\,0,\,1\}
$$

Step 3 · Each value gets the chance of its $x$-interval: length × height $\tfrac12$.

$$
P(Y=-1)=P(X<-0.5)=0.5\cdot\frac12=\frac14
$$

$$
P(Y=0)=1\cdot\frac12=\frac12
$$

$$
P(Y=1)=\frac14
$$

Step 4 · **Check:** they add to 1.

$$
\frac14+\frac12+\frac14=1
$$

**Answer:**

$$
p_Y(-1)=\frac14,\quad p_Y(0)=\frac12,\quad p_Y(1)=\frac14
$$

</details>

## Case 2: g only goes up

**You’ll see:** $Y=X^3$, $e^X$, $\ln X$, $\sqrt X$, $aX+b$ with $a>0$.

**The move:** an increasing $g$ keeps the $\le$. So $g(X)\le y$ is just $X\le g^{-1}(y)$:

$$F_Y(y)=F_X\big(g^{-1}(y)\big)$$

**Steps**

1. **Spot:** $g$ only goes up.
2. **Range:** push the ends of $X$’s range through $g$.
3. **Invert:** solve $y=g(x)$ for $x$. That’s $g^{-1}(y)$.
4. **Accumulate:** $F_Y(y)=F_X(g^{-1}(y))$ inside the range, $0$ below, $1$ above.
5. **Differentiate:** $f_Y(y)=F_Y^{\prime}(y)$.

**Short example:** $X\sim U(0,1)$ (so $F_X(x)=x$), $Y=e^X$:

$$F_Y(y)=F_X(\ln y)=\ln y\quad\Longrightarrow\quad f_Y(y)=\frac1y,\qquad 1<y<e$$

<details><summary>Full example (Lecture 14): $\;X\sim U(-1,1)$, $\;Y=X^3$</summary>

Step 1 · **Spot:** $x^3$ only goes up. $X$ is continuous, so $Y$ is continuous.

$$
g(x)=x^3
$$

Step 2 · **Range:** $(-1)^3=-1$ and $1^3=1$.

$$
-1\le Y\le1
$$

Step 3 · **Invert.**

$$
y=x^3\quad\Longrightarrow\quad x=\sqrt[3]{y}
$$

Step 4 · **Accumulate:** $X$’s CDF is $F_X(x)=\dfrac{x+1}{2}$ on $[-1,1]$. Put $\sqrt[3]y$ in for $x$.

$$
F_Y(y)=\begin{cases}0,&y<-1\\ \dfrac{\sqrt[3]{y}+1}{2},&-1\le y\le1\\ 1,&y>1\end{cases}
$$

Step 5 · **Differentiate:** the derivative of $y^{1/3}$ is $\tfrac13y^{-2/3}$.

$$
f_Y(y)=\frac12\cdot\frac13\,y^{-2/3}=\frac{1}{6\,y^{2/3}},\qquad -1<y<1
$$

**Answer:**

$$
f_Y(y)=\frac{1}{6\,y^{2/3}}\ \ \text{on }(-1,1),\quad 0\ \text{otherwise}
$$

</details>

<details><summary>Shortcut (not from the lectures): $\;f_Y(y)=f_X\big(g^{-1}(y)\big)\cdot|\text{slope of }g^{-1}(y)|$</summary>

Skips the CDF. Use it to go faster, or to check your answer. Works when $g$ only goes up **or** only goes down.

$$
f_Y(y)=f_X\big(g^{-1}(y)\big)\cdot\Big|\frac{d}{dy}g^{-1}(y)\Big|
$$

Check on $Y=X^3$: $f_X=\tfrac12$, $g^{-1}(y)=y^{1/3}$, its derivative is $\tfrac13y^{-2/3}$.

$$
f_Y(y)=\frac12\cdot\frac13\,y^{-2/3}=\frac{1}{6\,y^{2/3}}\quad\checkmark
$$

Check on $Y=e^X$, $X\sim U(0,1)$: $g^{-1}(y)=\ln y$, derivative $\tfrac1y$.

$$
f_Y(y)=1\cdot\frac1y=\frac1y\quad\checkmark
$$

</details>

<details><summary>CDFs you’ll plug in (from Question 2)</summary>

Uniform $U(a,b)$:

$$
F_X(x)=\frac{x-a}{b-a},\qquad a\le x\le b
$$

Exponential $(\lambda)$:

$$
F_X(x)=1-e^{-\lambda x},\qquad x\ge0
$$

$$
P(X>x)=e^{-\lambda x}
$$

Gaussian $N(\mu,\sigma^2)$:

$$
F_X(x)=\Phi\Big(\frac{x-\mu}{\sigma}\Big)
$$

$$
\Phi(-z)=1-\Phi(z)
$$

Chain rule, for the **Differentiate** step:

$$
\frac{d}{dy}F_X\big(h(y)\big)=f_X\big(h(y)\big)\,h^{\prime}(y)
$$

</details>

**Problem: Try it 1 · Case 2 · Log of an exponential · Tutorial 6 Q2** (intermediate)

$X\sim$ Exp$(1)$. Find the PDF of $Y=\ln X$.

<details><summary>Solution</summary>

1. **Spot:** $\ln x$ only goes up → Case 2.
2. **Range:** $X$ is anywhere in $(0,\infty)$, so $\ln X$ can be any real number.

   $$-\infty<Y<\infty$$
3. **Invert.**

   $$y=\ln x\quad\Longrightarrow\quad x=e^{y}$$
4. **Accumulate:** plug $e^y$ into $F_X(x)=1-e^{-x}$.

   $$F_Y(y)=1-e^{-e^{y}}$$
5. **Differentiate:** chain rule; the inside $-e^{y}$ has derivative $-e^{y}$.

   $$f_Y(y)=e^{y}\,e^{-e^{y}}$$

**Answer:** $f_Y(y)=e^{y}\,e^{-e^{y}}$ for all real $y$.

</details>

## Case 3: g only goes down

**You’ll see:** $Y=-3X+2$ ($aX+b$ with $a<0$), $-\ln X$, $\tfrac1X$ for $X>0$, $e^{-X}$.

**The move:** a decreasing $g$ **flips** the $\le$. So $g(X)\le y$ becomes $X\ge g^{-1}(y)$:

$$F_Y(y)=1-F_X\big(g^{-1}(y)\big)$$

Same steps as Case 2. Only the **Accumulate** step changes: $1-F_X(\dots)$.

**Short example:** $X\sim U(0,1)$, $Y=-\ln X$. $\;-\ln X\le y$ means $X\ge e^{-y}$:

$$F_Y(y)=1-F_X(e^{-y})=1-e^{-y}\quad\Longrightarrow\quad f_Y(y)=e^{-y},\qquad y>0$$

<details><summary>Full example (Lecture 15): $\;X\sim U(0,1)$, $\;Y=-3X+2$</summary>

Step 1 · **Spot:** $-3x+2$ only goes down (the slope is $-3$).

Step 2 · **Range:** $x=0$ gives $2$, $x=1$ gives $-1$.

$$
-1\le Y\le2
$$

Step 3 · **Invert.**

$$
y=-3x+2\quad\Longrightarrow\quad x=\frac{2-y}{3}
$$

Step 4 · **Accumulate:** dividing by $-3$ flips the $\le$. Then $F_X(x)=x$.

$$
-3X+2\le y\iff X\ge\frac{2-y}{3}
$$

$$
F_Y(y)=1-\frac{2-y}{3}=\frac{y+1}{3},\qquad -1\le y\le2
$$

Step 5 · **Differentiate.**

$$
f_Y(y)=\frac13,\qquad -1<y<2
$$

**Answer:**

$$
f_Y(y)=\frac13\ \text{ on }(-1,2):\quad Y\sim U(-1,2)
$$

</details>

<details><summary>$Y=aX+b$, all three cases (Lecture 15)</summary>

$a>0$ (goes up, Case 2):

$$
F_Y(y)=F_X\Big(\frac{y-b}{a}\Big)
$$

$a<0$ (goes down, Case 3):

$$
F_Y(y)=1-F_X\Big(\frac{y-b}{a}\Big)
$$

$a=0$: $Y=b$ always, a single step at $b$.

$$
F_Y(y)=\begin{cases}0,&y<b\\ 1,&y\ge b\end{cases}
$$

</details>

<details><summary>Shortcut: a line keeps the family</summary>

Gaussian in, Gaussian out. The mean and variance follow the Question 3 rules.

$$
X\sim N(\mu,\sigma^2)\quad\Longrightarrow\quad aX+b\sim N(a\mu+b,\ a^2\sigma^2)
$$

Uniform in, uniform out: push the two ends through.

$$
X\sim U(0,1),\ Y=-3X+2\quad\Longrightarrow\quad Y\sim U(-1,2)
$$

</details>

> **Warning:** **Flip the $\le$** whenever you divide by a negative number or undo a decreasing function: $-2x\le y\iff x\ge-\tfrac y2$. Forgetting the flip gives $F_X(\dots)$ instead of $1-F_X(\dots)$.

## Case 4: g turns around (DAD)

**You’ll see:** $Y=X^2$, $|X|$, $\cos X$, or a drawn curve with bumps.

**The move:** one $y$ can come from **several** $x$, so there’s no single inverse. Instead, find **every** $x$ with $g(x)\le y$, and add up $X$’s chance there:

$$F_Y(y)=P\big(X\text{ is in }\{x:\ g(x)\le y\}\big)$$

**Steps** (the lecture calls them DAD: Distribution, Accumulation, Differentiation)

1. **Range:** where can $Y$ land? Start from $X$’s range.
2. **Accumulate:** draw $g$ and a flat line at height $y$. The $x$-set is wherever the curve is **below** the line. Keep only $x$ that $X$ can take. $F_Y(y)$ = $X$’s chance on that set.
3. **Differentiate:** $f_Y(y)=F_Y^{\prime}(y)$.

**Short example:** $X\sim U(-1,1)$, $Y=X^2$. $\;X^2\le y$ means $-\sqrt y\le X\le\sqrt y$: length $2\sqrt y$, height $\tfrac12$:

$$F_Y(y)=2\sqrt y\cdot\frac12=\sqrt y\quad\Longrightarrow\quad f_Y(y)=\frac{1}{2\sqrt y},\qquad 0<y<1$$

**Finding the $x$-set:** drag $y$. The shaded $x$-set is where the curve is below the line.

```graph
title "$Y=X^2$, $X\sim U(-1,1)$: drag $y$"
x -1.3 1.3 label="$x$" height=250
y -0.25 1.25 label="$x^2$"
slider h 0 1.2 0.36 step=0.01 label="$y$"
curve "x^2" from=-1 to=1 color=1 label="$g(x)=x^2$"
hline "h" color=2
region "(x*x<=h)*(x>=-1)*(x<=1)*(y>-0.2)*(y<-0.06)" color=4 label="$x$-set: $-\sqrt y\le x\le\sqrt y$"
readout "$F_Y(y)$ = shaded length × $\tfrac12$" "min(sqrt(h),1)"
```

<details><summary>Full example (Lecture 15): $\;X\sim U(-1,1)$, $\;Y=X^2$, all three pieces</summary>

Step 1 · **Range:** $X$ is in $[-1,1]$, so $X^2$ is in $[0,1]$.

$$
0\le Y\le1
$$

Step 2 · **Accumulate**, $y<0$: a square is never negative.

$$
F_Y(y)=0
$$

Step 3 · **Accumulate**, $0\le y\le1$: the $x$-set is $[-\sqrt y,\sqrt y]$, inside $[-1,1]$.

$$
F_Y(y)=\int_{-\sqrt y}^{\sqrt y}\frac12\,dx=\sqrt y
$$

Step 4 · **Accumulate**, $y>1$: $X^2\le1$ always.

$$
F_Y(y)=1
$$

Step 5 · **Differentiate** the middle piece.

$$
f_Y(y)=\frac{1}{2\sqrt y},\qquad 0<y<1
$$

**Answer:**

$$
F_Y(y)=\sqrt y\ \text{ on }[0,1];\qquad f_Y(y)=\frac{1}{2\sqrt y}\ \text{ on }(0,1)
$$

</details>

<details><summary>Full example (Tutorial 6 Q4): $\;X\sim U(-1,1)$, $\;Y=|X|$</summary>

Step 1 · **Range:** $|x|$ on $[-1,1]$ runs from $0$ to $1$.

$$
0\le Y\le1
$$

Step 2 · **Accumulate:** $|X|\le y$ means $-y\le X\le y$. Length $2y$, height $\tfrac12$.

$$
F_Y(y)=2y\cdot\frac12=y
$$

Step 3 · **Differentiate.**

$$
f_Y(y)=1,\qquad 0<y<1
$$

Step 4 · Part (a) asked $P(|X|>\tfrac12)$: that’s $1-F_Y(\tfrac12)$.

$$
P\big(|X|>\tfrac12\big)=1-\frac12=\frac12
$$

**Answer:**

$$
f_Y(y)=1\ \text{ on }(0,1):\quad |X|\sim U(0,1)
$$

</details>

<details><summary>Shortcut (not from the lectures): $\;Y=X^2$ and $\;Y=|X|$</summary>

Both $\pm\sqrt y$ land on the same $y$, so add both:

$$
Y=X^2:\qquad f_Y(y)=\frac{f_X(\sqrt y)+f_X(-\sqrt y)}{2\sqrt y},\quad y>0
$$

Both $\pm y$ land on the same $y$:

$$
Y=|X|:\qquad f_Y(y)=f_X(y)+f_X(-y),\quad y>0
$$

Check on $X\sim U(-1,1)$ ($f_X=\tfrac12$):

$$
\frac{\frac12+\frac12}{2\sqrt y}=\frac{1}{2\sqrt y}\quad\checkmark
$$

If $X$ can’t be negative, drop the $f_X(-\dots)$ term (it’s $0$).

</details>

> **Warning:** **Keep only $x$ that $X$ can take.** $X\sim U(-1,2)$, $Y=X^2$, $y=4$: the $x$-set $[-2,2]$ is cut down to $[-1,2]$.

**Problem: Try it 2 · Case 4 · Squaring a uniform on $[0,2]$ · Lecture 12** (intermediate)

$X\sim U[0,2]$ and $Y=X^2$. (a) Find the CDF and PDF of $Y$. (b) Find $E[Y]$ from $f_Y$, and check it against $E[X^2]$.

<details><summary>Solution</summary>

1. **Spot:** $x^2$ turns around at $0$ → Case 4 (here $X\ge0$, so only one side is used).
2. **Range:** $0\le X\le2$, so $0\le Y\le4$.

   $$0\le Y\le4$$
3. **Accumulate:** $x^2\le y$ means $-\sqrt y\le x\le\sqrt y$, but $X$ is never negative. Only $[0,\sqrt y]$ counts.

   $$F_Y(y)=\sqrt y\cdot\frac12=\frac{\sqrt y}{2},\qquad 0\le y\le4$$
4. **Differentiate.**

   $$f_Y(y)=\frac{1}{4\sqrt y},\qquad 0<y<4$$
5. (b) Both ways give the same mean.

   $$\int_0^4 y\cdot\frac{1}{4\sqrt y}\,dy=\frac43=\int_0^2x^2\cdot\frac12\,dx$$

**Answer:** $F_Y=\tfrac{\sqrt y}{2}$ on $[0,4]$; $f_Y=\dfrac{1}{4\sqrt y}$ on $(0,4)$; $E[Y]=\tfrac43$ both ways.

</details>

## Case 5: g goes flat (a jump: mixed Y)

**You’ll see:** clipping, a rectifier, a limiter, a timeout: $\max\{X,0\}$, $\min\{X,1\}$.

**The move:** a flat piece at height $c$ sends a whole interval of $X$ to $c$. That’s a **jump** in $F_Y$:

$$P(Y=c)=P\big(X\text{ is in the flat part}\big)$$

1. **Range:** as always.
2. **Jump:** one per flat piece, sized $P(X$ in that piece$)$.
3. **Accumulate** everywhere else, as in Cases 2–4.
4. **Spot:** jumps plus a slope → **mixed**.

**Short example:** $X\sim U(-1,1)$, $Y=\max\{X,0\}$. Every $X\le0$ lands on $0$:

$$P(Y=0)=P(X\le0)=\frac12$$

<details><summary>Full example (Lecture 14): $\;X\sim U(-1,1)$, $\;Y=\max\{X,0\}$ (a half-wave rectifier)</summary>

Step 1 · **Range:** negative $X$ become $0$, positive $X$ stay.

$$
0\le Y\le1
$$

Step 2 · **Jump** at $0$: the flat part is $X\le0$.

$$
P(Y=0)=\frac12
$$

Step 3 · **Accumulate**, $0\le y\le1$: $\max\{X,0\}\le y$ just means $X\le y$.

$$
F_Y(y)=P(X\le y)=\frac{y+1}{2}
$$

Step 4 · Put the pieces together.

$$
F_Y(y)=\begin{cases}0,&y<0\\ \dfrac{y+1}{2},&0\le y\le1\\ 1,&y>1\end{cases}
$$

Step 5 · **Spot:** a jump of $\tfrac12$ at $0$, then a slope → **mixed**.

**Answer:**

$$
\text{mixed: }P(Y=0)=\frac12,\ \text{ plus density }\frac12\text{ on }(0,1)
$$

</details>

**What does the jump look like?**

```graph
title "$F_Y$ for $Y=\max\{X,0\}$: the flat piece becomes a jump"
x -0.6 1.5 label="$y$" height=200
y 0 1.12 label="$F_Y(y)$"
segment "-0.6" "0" "0" "0" color=2
curve "(x+1)/2" from=0 to=1 color=2
segment "1" "1" "1.5" "1" color=2
point "0" "0.5" color=2
segment "0" "0" "0" "0.5" color=2 dash
text "0.42" "0.25" "jump $\tfrac12=P(Y=0)$"
```

## Practice Questions

> **Tip:** **Question 4 is always one of these.** Spot the shape of $g$, then run its steps:
> 
> 1. **$X$ discrete / staircase:** add the chances that land on the same value.
> 2. **Only up:** Range → Invert → $F_Y=F_X(g^{-1}(y))$ → Differentiate.
> 3. **Only down:** same, but $F_Y=1-F_X(g^{-1}(y))$.
> 4. **Turns around:** Range → the $x$-set where $g(x)\le y$ → Differentiate (DAD).
> 5. **Goes flat:** a jump $P(X$ in the flat part$)$, then accumulate the rest.

Test-style, easy → hard. Solve on paper first, then open the solution.

**Problem: Question 1 · Case 1 · what type is $Y$ · Lecture 13 Examples 1–2** (introductory)

$X$ = number of failed packet sends, with $P(X=0,1,2,3)=0.4,\ 0.3,\ 0.2,\ 0.1$. (a) Find the PMF of $Y=2X+1$. (b) Find the PMF of $Z=(X-1)^2$. (c) $V\sim U(0,1)$ goes into a 1-bit converter: $B=0$ if $V<0.5$, $B=1$ if $V\ge0.5$. What type is $B$? Find its PMF.

<details><summary>Solution</summary>

1. **Type:** $X$ discrete → Case 1. (a) Each $x$ gives a different $y$, so the chances just move.

   $$p_Y(1)=0.4,\ \ p_Y(3)=0.3,\ \ p_Y(5)=0.2,\ \ p_Y(7)=0.1$$
2. (b) **Values:** $x=0,1,2,3$ give $Z=1,0,1,4$.

   $$Z\in\{0,1,4\}$$
3. $x=0$ and $x=2$ both give $Z=1$: **add** them.

   $$p_Z(0)=0.3,\quad p_Z(1)=0.4+0.2=0.6,\quad p_Z(4)=0.1$$
4. (c) **Spot:** a staircase $g$ → **discrete**. Each value gets the chance of its interval.

   $$P(B=0)=P(V<0.5)=\frac12,\quad P(B=1)=\frac12$$

**Answer:** (a) $0.4,0.3,0.2,0.1$ at $1,3,5,7$ (b) $0.3,0.6,0.1$ at $0,1,4$ (c) discrete, $\tfrac12,\tfrac12$.

</details>

**Problem: Question 2 · Case 2 · Exponential of a uniform · Tutorial 6 Q3** (introductory)

$X\sim U(0,1)$. Find the CDF and PDF of $Y=e^X$.

<details><summary>Solution</summary>

1. **Type:** $e^x$ only goes up → Case 2.
2. **Range:** $e^0=1$ to $e^1=e$.

   $$1\le Y\le e$$
3. **Invert.**

   $$y=e^{x}\quad\Longrightarrow\quad x=\ln y$$
4. **Accumulate:** $F_X(x)=x$ on $[0,1]$.

   $$F_Y(y)=\ln y,\qquad 1\le y\le e$$
5. **Differentiate.**

   $$f_Y(y)=\frac1y,\qquad 1<y<e$$

**Answer:** $F_Y=\ln y$ on $[1,e]$ ($0$ below, $1$ above); $f_Y(y)=\dfrac1y$ for $1<y<e$.

</details>

**Problem: Question 3 · Case 3 · decreasing $g$** (intermediate)

(a) $X\sim$ Exp$(\lambda)$. Find the CDF and PDF of $Y=-2X+3$. (b) $X\sim U(0,1)$. Find the CDF and PDF of $Y=-\ln X$.

<details><summary>Solution</summary>

1. (a) **Type:** slope $-2$, only goes down → Case 3. **Range:** $X\ge0$, so $Y=3-2X\le3$.

   $$Y\le3$$
2. **Invert.**

   $$y=-2x+3\quad\Longrightarrow\quad x=\frac{3-y}{2}$$
3. **Accumulate:** the $\le$ flips. Then $P(X\ge x)=e^{-\lambda x}$.

   $$\begin{gathered}-2X+3\le y\iff X\ge\frac{3-y}{2} \\ F_Y(y)=e^{-\lambda(3-y)/2},\qquad y\le3\end{gathered}$$
4. **Differentiate** (chain rule: the inside has slope $\tfrac\lambda2$).

   $$f_Y(y)=\frac{\lambda}{2}\,e^{-\lambda(3-y)/2},\qquad y<3$$
5. (b) **Type:** $-\ln x$ only goes down → Case 3. **Range:** $X\in(0,1)$, so $-\ln X\in(0,\infty)$.

   $$Y>0$$
6. **Invert.**

   $$y=-\ln x\quad\Longrightarrow\quad x=e^{-y}$$
7. **Accumulate:** the $\le$ flips, and $P(X\ge t)=1-t$.

   $$F_Y(y)=1-e^{-y},\qquad y\ge0$$
8. **Differentiate.** That’s the Exp$(1)$ PDF.

   $$f_Y(y)=e^{-y},\qquad y>0$$

**Answer:** (a) $F_Y=e^{-\lambda(3-y)/2}$ for $y\le3$, $f_Y=\tfrac\lambda2e^{-\lambda(3-y)/2}$ (b) $F_Y=1-e^{-y}$, $f_Y=e^{-y}$: $Y\sim$ Exp$(1)$.

</details>

**Problem: Question 4 · Case 2 · a Gaussian through a line · like Lecture 13 sensor** (intermediate)

A sensor reading is $X\sim N(2,9)$. It is calibrated to $Y=2X-3$. (a) Write $F_Y(y)$ using $\Phi$. (b) What are the mean and variance of $Y$? (c) Find $P(Y>7)$.

<details><summary>Solution</summary>

1. **Type:** slope $2>0$, only goes up → Case 2.
2. **Invert.**

   $$y=2x-3\quad\Longrightarrow\quad x=\frac{y+3}{2}$$
3. (a) **Accumulate**, then standardise with $\mu=2$, $\sigma=3$.

   $$F_Y(y)=\Phi\Big(\frac{\frac{y+3}{2}-2}{3}\Big)=\Phi\Big(\frac{y-1}{6}\Big)$$
4. (b) That’s the CDF of $N(1,36)$. The line shortcut agrees: $2\cdot2-3=1$, $2^2\cdot9=36$.

   $$Y\sim N(1,\,36)$$
5. (c) Complement, then the table: $\Phi(1)=0.8413$.

   $$P(Y>7)=1-\Phi\Big(\frac{7-1}{6}\Big)=1-\Phi(1)\approx0.1587$$

**Answer:** (a) $\Phi\left(\tfrac{y-1}{6}\right)$ (b) mean $1$, variance $36$ (c) $\approx 0.1587$

</details>

**Problem: Question 5 · Case 3 · $Y=aX+b$, in general · Lecture 15** (intermediate)

$X$ is continuous with CDF $F_X$. (a) Write $F_Y$ for $Y=aX+b$ when $a>0$, $a<0$ and $a=0$. (b) Use it for $X\sim U(0,1)$ and $Y=-3X+2$: find $F_Y$ and $f_Y$. What is $Y$?

<details><summary>Solution</summary>

1. (a) **$a>0$:** goes up (Case 2). Dividing by $a$ keeps the $\le$.

   $$F_Y(y)=P\Big(X\le\frac{y-b}{a}\Big)=F_X\Big(\frac{y-b}{a}\Big)$$
2. **$a<0$:** goes down (Case 3). Dividing by $a$ **flips** it.

   $$F_Y(y)=P\Big(X\ge\frac{y-b}{a}\Big)=1-F_X\Big(\frac{y-b}{a}\Big)$$
3. **$a=0$:** $Y=b$ always: one step from $0$ to $1$ at $b$.

   $$F_Y(y)=\begin{cases}0,&y<b\\ 1,&y\ge b\end{cases}$$
4. (b) **Range:** $X\in[0,1]$ gives $Y\in[-1,2]$. **Accumulate** with $a=-3$, $F_X(x)=x$.

   $$F_Y(y)=1-\frac{2-y}{3}=\frac{y+1}{3},\qquad -1\le y\le2$$
5. **Differentiate.**

   $$f_Y(y)=\frac13\ \text{ on }(-1,2)\quad\Rightarrow\quad Y\sim U(-1,2)$$

**Answer:** (a) $F_X(\tfrac{y-b}{a})$; $1-F_X(\tfrac{y-b}{a})$; a step at $b$ (b) $F_Y=\tfrac{y+1}{3}$ on $[-1,2]$, $Y\sim U(-1,2)$.

</details>

**Problem: Question 6 · Case 5 · flat pieces: timeout and limiter** (intermediate)

(a) A job takes $X\sim$ Exp$(1)$ seconds, but it is stopped after 1 second: $Y=\min\{X,1\}$. Find $F_Y$ and $P(Y=1)$. (b) $X\sim U(-2,2)$ goes through a limiter: $W=-1$ if $X<-1$, $W=X$ if $-1\le X\le1$, $W=1$ if $X>1$. Find $F_W$. What type is $W$?

<details><summary>Solution</summary>

1. (a) **Type:** flat at $1$ → Case 5. **Range:** times above 1 are recorded as 1.

   $$0\le Y\le1$$
2. **Jump** at $1$: every $X\ge1$ lands there.

   $$P(Y=1)=P(X\ge1)=e^{-1}\approx 0.3679$$
3. **Accumulate**, $0\le y<1$: $\min\{X,1\}\le y$ just means $X\le y$.

   $$F_Y(y)=1-e^{-y}$$
4. (b) **Type:** flat at $-1$ and at $1$ → Case 5. **Jumps:** each flat part has length 1, height $\tfrac14$.

   $$\begin{gathered}P(W=-1)=P(X<-1)=\frac14 \\ P(W=1)=P(X>1)=\frac14\end{gathered}$$
5. **Accumulate** in the middle: $W\le w$ means $X\le w$, and $F_X(x)=\tfrac{x+2}{4}$.

   $$F_W(w)=\begin{cases}0,&w<-1\\ \dfrac{w+2}{4},&-1\le w<1\\ 1,&w\ge1\end{cases}$$
6. **Spot:** jumps plus a slope → **mixed**.

**Answer:** (a) $F_Y=1-e^{-y}$ on $[0,1)$, $1$ for $y\ge1$; $P(Y=1)=e^{-1}\approx 0.3679$ (b) $F_W=\tfrac{w+2}{4}$ on $[-1,1)$, jumps of $\tfrac14$ at $\pm1$: mixed.

</details>

**Problem: Question 7 · Case 4 · $|X|$ of a $Cx^2$ variable · Tutorial 5 Q5** (intermediate)

$f_X(x)=Cx^2$ for $|x|\le1$, $0$ otherwise. (a) Find $C$. (b) Find the PDF of $Y=|X|$. (c) Find $E[Y^2]$ and $\mathrm{Var}[3X-1]$.

<details><summary>Solution</summary>

1. (a) **Find $c$:** total area $=1$.

   $$\int_{-1}^{1}Cx^2\,dx=\frac{2C}{3}=1\quad\Rightarrow\quad C=\frac32$$
2. (b) **Type:** $|x|$ turns around at $0$ → Case 4. **Range:** $0\le Y\le1$.

   $$0\le Y\le1$$
3. **Accumulate:** $|X|\le y$ means $-y\le X\le y$.

   $$F_Y(y)=\int_{-y}^{y}\frac32x^2\,dx=y^3$$
4. **Differentiate.** (Shortcut check: $f_X(y)+f_X(-y)=\tfrac32y^2+\tfrac32y^2=3y^2$ ✓.)

   $$f_Y(y)=3y^2,\qquad 0<y<1$$
5. (c) $E[Y^2]$ from $f_Y$.

   $$E[Y^2]=\int_0^1y^2\cdot3y^2\,dy=\frac35$$
6. $f_X$ is symmetric, so $E[X]=0$ and $\mathrm{Var}(X)=E[X^2]=E[Y^2]$. Then $\mathrm{Var}(aX+b)=a^2\mathrm{Var}(X)$.

   $$\mathrm{Var}[3X-1]=9\cdot\frac35=\frac{27}{5}$$

**Answer:** (a) $C=\tfrac32$ (b) $f_Y(y)=3y^2$ on $(0,1)$ (c) $E[Y^2]=\tfrac35$, $\mathrm{Var}[3X-1]=\tfrac{27}{5}$.

</details>

**Problem: Question 8 · Case 4 · power of a Gaussian noise voltage** (intermediate)

A noise voltage is $X\sim N(0,1)$. Its power is $Y=X^2$. (a) Write $F_Y(y)$ using $\Phi$. (b) Find $f_Y(y)$. (c) Find $P(Y\le1)$.

<details><summary>Solution</summary>

1. **Type:** $x^2$ turns around → Case 4. **Range:** $Y\ge0$.

   $$Y\ge0$$
2. (a) **Accumulate:** $X^2\le y$ means $-\sqrt y\le X\le\sqrt y$. Then $\Phi(-z)=1-\Phi(z)$.

   $$F_Y(y)=\Phi(\sqrt y)-\Phi(-\sqrt y)=2\Phi(\sqrt y)-1,\qquad y\ge0$$
3. (b) **Differentiate:** $\Phi^{\prime}(z)=\tfrac{1}{\sqrt{2\pi}}e^{-z^2/2}$, times the inside derivative $\tfrac{1}{2\sqrt y}$.

   $$f_Y(y)=2\cdot\frac{1}{\sqrt{2\pi}}e^{-y/2}\cdot\frac{1}{2\sqrt y}=\frac{e^{-y/2}}{\sqrt{2\pi y}},\qquad y>0$$
4. (c) Table: $\Phi(1)=0.8413$.

   $$P(Y\le1)=2(0.8413)-1=0.6826$$

**Answer:** $F_Y(y)=2\Phi(\sqrt y)-1$ for $y\ge0$; $f_Y(y)=\dfrac{e^{-y/2}}{\sqrt{2\pi y}}$ for $y>0$; $P(Y\le1)\approx0.6827$.

</details>

**Problem: Question 9 · Case 4 · squaring a lopsided uniform** (advanced)

$X\sim U(-1,2)$. Find the CDF and PDF of $Y=X^2$.

<details><summary>Solution</summary>

1. **Type:** $x^2$ turns around → Case 4. **Range:** smallest at $x=0$, largest at $x=2$.

   $$0\le Y\le4$$
2. **Accumulate**, $0\le y\le1$: both $\pm\sqrt y$ are inside $(-1,2)$. Length $2\sqrt y$, height $\tfrac13$.

   $$F_Y(y)=\frac{2\sqrt y}{3}$$
3. **Accumulate**, $1<y\le4$: $-\sqrt y$ is below $-1$, where $X$ never goes. Only $[-1,\sqrt y]$ is left.

   $$F_Y(y)=\frac{\sqrt y+1}{3}$$
4. **Differentiate** each piece.

   $$f_Y(y)=\begin{cases}\dfrac{1}{3\sqrt y},&0<y<1\\ \dfrac{1}{6\sqrt y},&1<y<4\\ 0,&\text{otherwise}\end{cases}$$

**Answer:** Two pieces: $\dfrac{1}{3\sqrt y}$ on $(0,1)$, $\dfrac{1}{6\sqrt y}$ on $(1,4)$. Above $y=1$ only $+\sqrt y$ is possible.

</details>

**Problem: Question 10 · Case 4 · $F_Y$ from a picture · Lecture 15** (advanced)

$X$ is continuous with CDF $F_X$, and $Y=g(X)$ with $g(x)=x^3-3x$ (graph below: it peaks at $(-1,2)$ and dips to $(1,-2)$). Write (a) $F_Y(3)$, (b) $F_Y(0)$, (c) $F_Y(-3)$ using $F_X$. (d) Find $F_Y(0)$ when $X\sim U(-2,2)$.

<details><summary>Solution</summary>

1. **Type:** $g$ turns around twice → Case 4. **Accumulate:** for each height, find where the curve is below the line.
2. (a) $y=3$ is above the bump: it cuts the curve **once**, at $x\approx2.104$. Below the line = everything left of it.

   $$F_Y(3)=F_X(2.104)$$
3. (b) $y=0$ cuts **three** times: $x^3-3x=0$ at $-\sqrt3,\ 0,\ \sqrt3$. Below on $x\le-\sqrt3$ and on $0\le x\le\sqrt3$.

   $$F_Y(0)=F_X(-\sqrt3)+F_X(\sqrt3)-F_X(0)$$
4. (c) $y=-3$ is below the dip: one cut, at $x\approx-2.104$.

   $$F_Y(-3)=F_X(-2.104)$$
5. (d) Plug in $F_X(x)=\tfrac{x+2}{4}$.

   $$\frac{2-\sqrt3}{4}+\frac{2+\sqrt3}{4}-\frac24=\frac12$$

**Answer:** (a) $F_X(2.104)$ (b) $F_X(-\sqrt3)+F_X(\sqrt3)-F_X(0)$ (c) $F_X(-2.104)$ (d) $\tfrac12$

</details>

For the question above: drag $y$ and count where the curve is below the line.

```graph
title "$g(x)=x^3-3x$: drag the line to height $y$"
x -2.6 2.6 label="$x$" height=280
y -4 4 label="$g(x)$"
slider h -3.5 3.5 0 step=0.1 label="$y$"
curve "x^3-3*x" from=-2.2 to=2.2 color=1 label="$g(x)$"
hline "h" color=2
```

**Problem: Question 11 · Case 4 · $Y=\cos X$ · Lecture 15** (advanced)

$X$ is continuous and takes values in $[-\pi,\pi]$. (a) Write $F_Y(y)$ for $Y=\cos X$ using $F_X$, for $-1\le y\le1$. (b) Find $F_Y$ and $f_Y$ when $X\sim U(-\pi,\pi)$.

<details><summary>Solution</summary>

1. **Type:** $\cos x$ goes up then down → Case 4. **Range:** $-1\le\cos X\le1$.

   $$-1\le Y\le1$$
2. (a) **Accumulate:** $\cos x$ is highest at $x=0$, so $\cos x\le y$ on the **two ends**: $x\le-\arccos y$ or $x\ge\arccos y$.

   $$F_Y(y)=F_X(-\arccos y)+1-F_X(\arccos y)$$
3. (b) Plug in $F_X(x)=\tfrac{x+\pi}{2\pi}$, writing $a=\arccos y$.

   $$F_Y(y)=\frac{\pi-a}{2\pi}+1-\frac{a+\pi}{2\pi}=1-\frac{\arccos y}{\pi}$$
4. **Differentiate:** the derivative of $\arccos y$ is $-\dfrac{1}{\sqrt{1-y^2}}$.

   $$f_Y(y)=\frac{1}{\pi\sqrt{1-y^2}},\qquad -1<y<1$$

**Answer:** (a) $F_X(-\arccos y)+1-F_X(\arccos y)$ (b) $F_Y=1-\dfrac{\arccos y}{\pi}$, $f_Y=\dfrac{1}{\pi\sqrt{1-y^2}}$ on $(-1,1)$.

</details>

**Problem: Question 12 · Case 3 + 4 · the reciprocal, in general · Tutorial 6 Q1** (advanced)

$X$ is continuous with CDF $F_X$ and PDF $f_X$. Write the CDF and PDF of $Y=\dfrac1X$ using $F_X$ and $f_X$.

<details><summary>Solution</summary>

1. **Type:** $\tfrac1x$ goes down on each side of $0$, but jumps across it. So split by the sign, like Case 4. **Range:** any nonzero number.

   $$Y\ne0$$
2. **Accumulate**, $y>0$: every negative $X$ works ($\tfrac1X<0<y$). A positive $X$ works when $X\ge\tfrac1y$ (flip, Case 3).

   $$F_Y(y)=F_X(0)+1-F_X\Big(\frac1y\Big)$$
3. **Accumulate**, $y=0$: only negative $X$ work.

   $$F_Y(0)=F_X(0)$$
4. **Accumulate**, $y<0$: only negative $X$ can work, and then $\tfrac1X\le y$ means $\tfrac1y\le X<0$.

   $$F_Y(y)=F_X(0)-F_X\Big(\frac1y\Big)$$
5. **Differentiate:** both pieces have $-F_X(\tfrac1y)$, and the derivative of $\tfrac1y$ is $-\tfrac{1}{y^2}$.

   $$f_Y(y)=\frac{1}{y^2}\,f_X\Big(\frac1y\Big),\qquad y\ne0$$

**Answer:** $F_Y(y)=F_X(0)+1-F_X(\tfrac1y)$ for $y>0$, $F_X(0)$ at $y=0$, $F_X(0)-F_X(\tfrac1y)$ for $y<0$; $f_Y(y)=\dfrac{1}{y^2}f_X(\tfrac1y)$.

</details>
