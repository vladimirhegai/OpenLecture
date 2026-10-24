# Test 2 - Question 4

**Lectures 12–15 · Tutorial 6.** Functions of a continuous random variable: what kind of random variable $Y=g(X)$ is, and how to find its CDF and PDF.

## Topic 1: What kind of random variable is $Y=g(X)$?

You know the distribution of $X$. A new random variable is made from it: $Y=g(X)$ (power $=X^2$, a clipped voltage, a quantizer…).

Before computing anything, decide **what kind** $Y$ is: discrete, continuous or mixed. That decides the answer's shape.

> **Reminder:** **What you need from Questions 1–2**
> 
> - **CDF:** $F_Y(y)=P(Y\le y)$, for every real $y$. It goes from $0$ to $1$ and never decreases.
> - **Jump** in a CDF at $c$ = $P(Y=c)$. No jumps → continuous; only jumps → discrete; both → **mixed**.
> - **Continuous $X$:** $P(X=x)=0$, so $<$ and $\le$ give the same probability.
> - **PDF from CDF:** $f_Y(y)=\dfrac{d}{dy}F_Y(y)$.
> - **CDFs you will plug in all the time:**
>   - $X\sim U(a,b)$: $F_X(x)=\dfrac{x-a}{b-a}$ for $a\le x\le b$ (area = width × height $\tfrac{1}{b-a}$).
>   - $X\sim$ Exp$(\lambda)$: $F_X(x)=1-e^{-\lambda x}$ for $x\ge0$, so $P(X>x)=e^{-\lambda x}$.
>   - $X\sim N(\mu,\sigma^2)$: $F_X(x)=\Phi\!\left(\frac{x-\mu}{\sigma}\right)$, and $\Phi(-z)=1-\Phi(z)$.

| $X$ | shape of $g$ | $Y$ is | Lecture example |
|---|---|---|---|
| discrete | anything | **discrete** | $Y=2X+1$ |
| continuous | a staircase (few output values) | **discrete** | 1-bit converter |
| continuous | no flat pieces | **continuous** | $Y=X^2$, $Y=X^3$ |
| continuous | flat on some interval | **mixed** | $Y=\max\{X,0\}$ |

- **Discrete $X$:** $Y$ can only take the values $g(x_1),g(x_2),\dots$, so it is discrete. Several $x$ may give the **same** $y$: add their probabilities.
- **Flat piece:** if $g(x)=c$ for all $x$ in $[a,b]$, then $P(Y=c)\ge P(a\le X\le b)>0$. That is a point with positive probability: a **jump** in $F_Y$.
- **No flat pieces** ($g^{\prime}(x)$ is not $0$ on a whole interval): $Y$ is continuous.

$$p_Y(y)=P(g(X)=y)=\sum_{x:\;g(x)=y}p_X(x)$$

**Example: Example 1 · Discrete in, discrete out**

The number of failed packet transmissions $X$ has $p_X(0)=0.4,\ p_X(1)=0.3,\ p_X(2)=0.2,\ p_X(3)=0.1$. The retransmission cost is $Y=2X+1$, and the "distance from one failure" is $W=|X-1|$. Find the PMFs of $Y$ and $W$.

1. **Values of $Y$:** $g(x)=2x+1$ sends $0,1,2,3$ to $1,3,5,7$. No two $x$ share a $y$, so the probabilities just move.

   $$p_Y(1)=0.4,\quad p_Y(3)=0.3,\quad p_Y(5)=0.2,\quad p_Y(7)=0.1$$
2. **Values of $W$:** $x=0\to1$, $x=1\to0$, $x=2\to1$, $x=3\to2$. Now $x=0$ and $x=2$ **both** give $W=1$.

   $$\{W=1\}=\{X=0\}\cup\{X=2\}$$
3. **Add** the probabilities of every $x$ that lands on the same $w$.

   $$p_W(0)=0.3,\quad p_W(1)=0.4+0.2=0.6,\quad p_W(2)=0.1$$
4. Check: each PMF adds to 1.

   $$0.3+0.6+0.1=1\;\checkmark$$

**Answer:** $p_Y$: $0.4,0.3,0.2,0.1$ at $1,3,5,7$. $\;p_W(0)=0.3,\ p_W(1)=0.6,\ p_W(2)=0.1$.

**Example: Example 2 · Clipping makes a mixed random variable**

$X\sim U(-1,1)$ and $Y=\max\{X,0\}$ (a half-wave rectifier). Find the CDF of $Y$. What kind of random variable is $Y$?

1. **Range:** negative $X$ become $0$, positive $X$ stay. So $Y$ lives in $[0,1]$.

   $$R_Y=[0,1]$$
2. **CDF, $y<0$:** $Y\ge0$ always, so $Y\le y$ is impossible.

   $$F_Y(y)=0$$
3. **CDF, $0\le y\le1$:** $\max\{X,0\}\le y$ exactly when $X\le y$ (the $0$ is already $\le y$).

   $$F_Y(y)=P(X\le y)=\int_{-1}^{y}\frac12\,dx=\frac{y+1}{2}$$
4. **CDF, $y>1$:** $Y\le1$ always.

   $$F_Y(y)=1$$
5. **Kind:** at $y=0$ the CDF jumps from $0$ to $\tfrac12$. The whole interval $-1<X\le0$ is squashed onto $Y=0$.

   $$P(Y=0)=P(X\le0)=\frac12$$
6. Between $0$ and $1$ it rises smoothly, so $Y$ has a continuous part too: **mixed**.

   $$F_Y(y)=\begin{cases}0,&y<0\\ \dfrac{y+1}{2},&0\le y\le1\\ 1,&y>1\end{cases}$$

**Answer:** $F_Y(y)=0$ for $y<0$, $\tfrac{y+1}{2}$ for $0\le y\le1$, $1$ for $y>1$. Mixed: $P(Y=0)=\tfrac12$ plus density $\tfrac12$ on $(0,1)$.

A flat piece of $g$ collects a whole interval of $X$ onto one value of $Y$:

```graph
title "The flat piece of $g$ …"
x -1.2 1.2 label="$x$" height=200
y -0.2 1.15 label="$y$"
curve "max(x,0)" from=-1 to=1 color=1 label="$g(x)=\max(x,0)$"
region "(x>-1)*(x<0)*(y>-0.07)*(y<0.07)" color=4 label="all these $x$ give $Y=0$ (probability $\tfrac12$)"
```

```graph
title "… becomes a jump in $F_Y$"
x -0.6 1.5 label="$y$" height=200
y 0 1.12 label="$F_Y(y)$"
segment "-0.6" "0" "0" "0" color=2
curve "(x+1)/2" from=0 to=1 color=2
segment "1" "1" "1.5" "1" color=2
point "0" "0.5" color=2
segment "0" "0" "0" "0.5" color=2 dash
text "0.42" "0.25" "jump $\tfrac12=P(Y=0)$"
```

**Problem: Try it 1 · Squaring a discrete variable** (introductory)

$X$ is equally likely to be $-2,-1,0,1,2$. Find the PMF of $Y=X^2$.

<details><summary>Solution</summary>

1. **Values:** $(-2)^2=4,\ (-1)^2=1,\ 0^2=0,\ 1^2=1,\ 2^2=4$.

   $$R_Y=\{0,1,4\}$$
2. **Add** the probabilities that land on the same value.

   $$p_Y(0)=\frac15,\quad p_Y(1)=\frac15+\frac15=\frac25,\quad p_Y(4)=\frac25$$

**Answer:** $p_Y(0)=\tfrac15,\ p_Y(1)=\tfrac25,\ p_Y(4)=\tfrac25$

</details>

**Problem: Try it 2 · A 3-level quantizer** (intermediate)

$X\sim U(-1,1)$ is fed to a quantizer: $Y=-1$ if $X<-0.5$, $Y=0$ if $-0.5\le X\le0.5$, $Y=1$ if $X>0.5$. What kind of random variable is $Y$? Find its distribution.

<details><summary>Solution</summary>

1. **Kind:** $g$ is a staircase with only three output values, so $Y$ is **discrete**.

   $$R_Y=\{-1,0,1\}$$
2. **Each value** = probability of the $x$-interval that maps to it (uniform: length × $\tfrac12$).

   $$P(Y=-1)=P(X<-0.5)=0.5\cdot\frac12=\frac14$$
3. Same for the other two.

   $$P(Y=0)=1\cdot\frac12=\frac12,\qquad P(Y=1)=\frac14$$

**Answer:** Discrete: $P(Y=-1)=\tfrac14,\ P(Y=0)=\tfrac12,\ P(Y=1)=\tfrac14$.

</details>

**Problem: Try it 3 · A saturating amplifier** (intermediate)

$X\sim U(0,3)$ and the amplifier output saturates at 2: $Y=\min\{X,2\}$. Find $F_Y(y)$ and $P(Y=2)$.

<details><summary>Solution</summary>

1. **Range:** values above 2 are cut to 2.

   $$R_Y=[0,2]$$
2. **CDF, $0\le y<2$:** $\min\{X,2\}\le y$ exactly when $X\le y$ (since $2>y$).

   $$F_Y(y)=P(X\le y)=\frac{y}{3}$$
3. **CDF, $y\ge2$:** $Y\le2$ always.

   $$F_Y(y)=1$$
4. **Jump at 2:** just below 2 the CDF is $\tfrac23$, at 2 it is 1. The flat piece $X\ge2$ is collected at $Y=2$.

   $$P(Y=2)=P(X\ge2)=\frac13$$
5. So $Y$ is **mixed**.

   $$F_Y(y)=\begin{cases}0,&y<0\\ y/3,&0\le y<2\\ 1,&y\ge2\end{cases}$$

**Answer:** $F_Y=0$ ($y<0$), $\tfrac y3$ ($0\le y<2$), $1$ ($y\ge2$); $P(Y=2)=\tfrac13$, mixed.

</details>

## Topic 2: Monotonic $g$: the CDF method

If $g$ only goes **up** (or only **down**), every $y$ comes from exactly one $x=g^{-1}(y)$.

Then the event "$Y\le y$" is just an event about $X$, and you can read it off $F_X$.

> **Reminder:** **Calculus and algebra you need here**
> 
> | function of $y$ | derivative |
> |---|---|
> | $y^n$ (incl. $\sqrt y=y^{1/2}$, $\sqrt[3]y=y^{1/3}$) | $n\,y^{n-1}$ (so $\tfrac{1}{2\sqrt y}$, $\tfrac{1}{3\sqrt[3]{y^2}}$) |
> | $\ln y$ | $\dfrac1y$ |
> | $e^{ay}$ | $a\,e^{ay}$ |
> | $\arccos y$ | $-\dfrac{1}{\sqrt{1-y^2}}$ |
> | **chain rule:** $F(h(y))$ | $F^{\prime}(h(y))\,h^{\prime}(y)=f(h(y))\,h^{\prime}(y)$ |
> 
> - **An inequality flips** when you multiply/divide by a negative number: $-2x\le y\iff x\ge-\tfrac y2$.
> - It also flips when you apply a **decreasing** function: $e^{-x}\le y\iff -x\le\ln y\iff x\ge-\ln y$.

$$g\text{ increasing:}\quad F_Y(y)=P(X\le g^{-1}(y))=F_X\!\left(g^{-1}(y)\right)$$

$$g\text{ decreasing:}\quad F_Y(y)=P(X\ge g^{-1}(y))=1-F_X\!\left(g^{-1}(y)\right)$$

**The method** (every solution in this note follows it):

1. **Range:** where can $Y$ be? Below the range $F_Y=0$, above it $F_Y=1$.
2. **Invert:** solve $y=g(x)$ for $x=g^{-1}(y)$. Increasing or decreasing?
3. **CDF:** rewrite $\{g(X)\le y\}$ as an event about $X$ (flip the inequality if $g$ is decreasing), then use $F_X$.
4. **PDF:** differentiate, $f_Y(y)=F_Y^{\prime}(y)$, inside the range; $0$ outside.

> **Tip:** **Shortcut to check your PDF** (the chain rule applied to the two formulas above):
> 
> $$
> f_Y(y)=f_X\!\left(g^{-1}(y)\right)\left|\frac{d}{dy}g^{-1}(y)\right|
> $$
> 
> The absolute value covers the decreasing case, where the derivative of $1-F_X(g^{-1}(y))$ gets a minus sign that cancels the negative slope. Show the CDF steps on the test; use this to check.

**Example: Example 3 · Cubing a uniform**

$X\sim U(-1,1)$ and $Y=X^3$. Find the CDF and PDF of $Y$.

1. **Range:** $x^3$ maps $[-1,1]$ onto $[-1,1]$.

   $$R_Y=[-1,1]$$
2. **Invert:** $y=x^3$ is increasing on all of $\mathbb R$.

   $$g^{-1}(y)=\sqrt[3]{y}$$
3. **CDF:** $X^3\le y\iff X\le\sqrt[3]y$. Plug into $F_X(x)=\tfrac{x+1}{2}$ for $-1\le x\le1$.

   $$F_Y(y)=F_X(\sqrt[3]y)=\frac{\sqrt[3]{y}+1}{2},\qquad -1\le y\le1$$
4. Outside the range.

   $$F_Y(y)=\begin{cases}0,&y<-1\\ \dfrac{\sqrt[3]y+1}{2},&-1\le y\le1\\ 1,&y>1\end{cases}$$
5. **PDF:** $\frac{d}{dy}y^{1/3}=\frac13y^{-2/3}$. Not defined at $y=0$, which does not matter (one point).

   $$f_Y(y)=\frac{1}{6\sqrt[3]{y^2}},\qquad -1<y<1,\ y\ne0$$
6. Check with the shortcut: $f_X=\tfrac12$ and $\left|\tfrac{d}{dy}y^{1/3}\right|=\tfrac{1}{3\sqrt[3]{y^2}}$.

   $$\frac12\cdot\frac{1}{3\sqrt[3]{y^2}}=\frac{1}{6\sqrt[3]{y^2}}\;\checkmark$$

**Answer:** $F_Y(y)=\dfrac{\sqrt[3]y+1}{2}$ on $[-1,1]$; $f_Y(y)=\dfrac{1}{6\sqrt[3]{y^2}}$ for $-1<y<1$.

Both densities have area 1. Numbers near 0 get much closer to 0 when cubed ($0.5^3=0.125$), so $Y$ crowds there:

```graph
title "Cubing squeezes values toward 0, so the density piles up there"
x -1.15 1.15 label="$y$" height=230
y 0 2.6 label="density"
hline "0.5" color=1 label="$f_X=\tfrac12$ (before cubing)"
curve "1/(6*abs(x)^(2/3))" from=-1 to=-0.004 color=2
curve "1/(6*abs(x)^(2/3))" from=0.004 to=1 color=2 label="$f_Y(y)$ for $Y=X^3$"
```

**Example: Example 4 · A linear function $Y=aX+b$**

$X$ is continuous with CDF $F_X$ and PDF $f_X$. Write the CDF and PDF of $Y=aX+b$ in terms of $F_X$ and $f_X$.

1. **$a>0$ (increasing):** divide by $a$, the inequality stays.

   $$F_Y(y)=P\!\left(X\le\frac{y-b}{a}\right)=F_X\!\left(\frac{y-b}{a}\right)$$
2. **$a<0$ (decreasing):** dividing by $a<0$ **flips** the inequality.

   $$F_Y(y)=P\!\left(X\ge\frac{y-b}{a}\right)=1-F_X\!\left(\frac{y-b}{a}\right)$$
3. **PDF:** differentiate; the chain rule brings out $\tfrac1a$ (and a minus sign when $a<0$). Both cases together:

   $$f_Y(y)=\frac{1}{|a|}\,f_X\!\left(\frac{y-b}{a}\right)$$
4. **$a=0$:** $Y=b$ always. That is a constant, a discrete random variable with $P(Y=b)=1$.

   $$F_Y(y)=\begin{cases}0,&y<b\\1,&y\ge b\end{cases}$$

**Answer:** $a>0$: $F_Y=F_X(\tfrac{y-b}{a})$; $a<0$: $F_Y=1-F_X(\tfrac{y-b}{a})$; $f_Y(y)=\tfrac{1}{|a|}f_X(\tfrac{y-b}{a})$.

**Problem: Try it 4 · Exponential of a uniform · Tutorial 6 Q3** (introductory)

$X\sim U(0,1)$. Find the PDF of $Y=e^X$.

<details><summary>Solution</summary>

1. **Range:** $e^0=1$ to $e^1=e$.

   $$R_Y=(1,e)$$
2. **Invert:** $e^x$ is increasing.

   $$g^{-1}(y)=\ln y$$
3. **CDF:** $e^X\le y\iff X\le\ln y$, and $F_X(x)=x$ on $[0,1]$.

   $$F_Y(y)=\begin{cases}0,&y<1\\ \ln y,&1\le y\le e\\ 1,&y>e\end{cases}$$
4. **PDF:** differentiate $\ln y$.

   $$f_Y(y)=\begin{cases}\dfrac1y,&1<y<e\\ 0,&\text{otherwise}\end{cases}$$

**Answer:** $f_Y(y)=\dfrac1y$ for $1<y<e$, $0$ otherwise.

</details>

**Problem: Try it 5 · Log of an exponential · Tutorial 6 Q2** (intermediate)

$X\sim$ Exp$(1)$. Find the PDF of $Y=\ln X$ (natural log).

<details><summary>Solution</summary>

1. **Range:** $X$ runs over $(0,\infty)$, so $\ln X$ runs over all real numbers.

   $$R_Y=(-\infty,\infty)$$
2. **Invert:** $\ln x$ is increasing.

   $$g^{-1}(y)=e^y$$
3. **CDF:** $\ln X\le y\iff X\le e^y$. Use $F_X(x)=1-e^{-x}$.

   $$F_Y(y)=1-e^{-e^{y}},\qquad -\infty<y<\infty$$
4. **PDF:** chain rule, the inner derivative of $-e^{y}$ is $-e^y$.

   $$f_Y(y)=e^{-e^{y}}\cdot e^{y}=e^{\,y-e^{y}},\qquad -\infty<y<\infty$$

**Answer:** $f_Y(y)=e^{y}\,e^{-e^{y}}$ for all real $y$.

</details>

**Problem: Try it 6 · Standardising a normal** (intermediate)

$X\sim N(\mu,\sigma^2)$. Show that $Z=\dfrac{X-\mu}{\sigma}$ is standard normal, $N(0,1)$.

<details><summary>Solution</summary>

1. **Type:** $Z=aX+b$ with $a=\tfrac1\sigma>0$ (increasing) and $b=-\tfrac\mu\sigma$. Inverse: $x=\mu+\sigma z$.

   $$g^{-1}(z)=\mu+\sigma z$$
2. **CDF:** use $F_X(x)=\Phi\!\left(\tfrac{x-\mu}{\sigma}\right)$.

   $$F_Z(z)=F_X(\mu+\sigma z)=\Phi\!\left(\frac{\mu+\sigma z-\mu}{\sigma}\right)=\Phi(z)$$
3. **PDF:** $f_Z(z)=\sigma f_X(\mu+\sigma z)$; the $\sigma$ cancels the $\tfrac1\sigma$ in front of $f_X$.

   $$f_Z(z)=\sigma\cdot\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(\sigma z)^2}{2\sigma^2}}=\frac{1}{\sqrt{2\pi}}e^{-z^2/2}$$

**Answer:** $F_Z(z)=\Phi(z)$ and $f_Z(z)=\tfrac{1}{\sqrt{2\pi}}e^{-z^2/2}$: $Z\sim N(0,1)$. This is why every normal question goes through the $\Phi$ table.

</details>

## Topic 3: Non-monotonic $g$: the DAD method

When $g$ goes up **and** down (like $x^2$ or $\cos x$), one $y$ comes from several $x$, so there is no single $g^{-1}$.

Work straight from the definition $F_Y(y)=P(g(X)\le y)$. This **DAD** method works for **every** $g$, monotonic or not.

1. **Distribution:** find the range of $Y=g(X)$ (use the range of $X$!).
2. **Accumulation:** for each case of $y$, find the set of $x$ where $g(x)\le y$, then add up $X$'s probability on it: $F_Y(y)=P(g(X)\le y)$.
3. **Differentiation:** $f_Y(y)=\dfrac{d}{dy}F_Y(y)$ wherever the derivative exists.

**Finding the $x$-set:** draw $g$, draw a horizontal line at height $y$. The $x$-set is wherever the curve is **below** the line. It can be one interval or several.

Drag $y$. At $y=1$ the line cuts the curve at $x_2<x_3<x_4$, and the curve is below the line for $x\le x_2$ and for $x_3\le x\le x_4$:

```graph
title "The $x$-set $\{x: g(x)\le y\}$ for a wiggly $g$"
x -2.2 2.4 label="$x$" height=280
y -3.3 3.3 label="$g(x)$"
slider h -2.6 2.6 1 step=0.05 label="$y$"
curve "x^3-3*x" from=-2.2 to=2.4 color=1 label="$g(x)$"
hline "h" color=2 label="height $y$"
region "(x^3-3*x<=h)*(y>-3.25)*(y<-2.85)" color=4 label="$x$-set: $g(x)\le y$"
```

$$F_Y(y)=P(X\le x_2)+P(x_3\le X\le x_4)=F_X(x_2)+F_X(x_4)-F_X(x_3)$$

Each interval contributes "$F_X$ at its right end minus $F_X$ at its left end". Above the top of the hump the set becomes a single interval again.

**Example: Example 5 · Squaring a uniform**

$X\sim U(-1,1)$ and $Y=X^2$. Find the CDF and PDF of $Y$.

1. **Distribution:** $x^2$ on $[-1,1]$ goes from $0$ (at $x=0$) to $1$ (at $x=\pm1$).

   $$R_Y=[0,1]$$
2. **Accumulation, $y<0$:** a square is never negative.

   $$F_Y(y)=0$$
3. **Accumulation, $0\le y\le1$:** $x^2\le y\iff -\sqrt y\le x\le\sqrt y$. Uniform: length $2\sqrt y$ × height $\tfrac12$.

   $$F_Y(y)=P(-\sqrt y\le X\le\sqrt y)=\int_{-\sqrt y}^{\sqrt y}\frac12\,dx=\sqrt y$$
4. **Accumulation, $y>1$:** $X^2\le1$ always.

   $$F_Y(y)=1$$
5. **Differentiation.**

   $$f_Y(y)=\frac{d}{dy}\sqrt y=\frac{1}{2\sqrt y},\qquad 0<y<1$$

**Answer:** $F_Y(y)=0$ ($y<0$), $\sqrt y$ ($0\le y\le1$), $1$ ($y>1$); $f_Y(y)=\dfrac{1}{2\sqrt y}$ on $(0,1)$.

```graph
title "$Y=X^2$, $X\sim U(-1,1)$: drag $y$"
x -1.3 1.3 label="$x$" height=250
y -0.25 1.25 label="$x^2$"
slider h 0 1.2 0.36 step=0.01 label="$y$"
curve "x^2" from=-1 to=1 color=1 label="$g(x)=x^2$"
hline "h" color=2
region "(x*x<=h)*(x>=-1)*(x<=1)*(y>-0.2)*(y<-0.06)" color=4 label="$-\sqrt y\le x\le\sqrt y$"
readout "$\sqrt y$" "sqrt(h)"
readout "$F_Y(y)$ = shaded length × $\tfrac12$" "min(sqrt(h),1)"
```

**Problem: Try it 7 · Absolute value · Tutorial 6 Q4** (introductory)

$X\sim U(-1,1)$. (a) Find $P(|X|>\tfrac12)$. (b) Find the PDF of $Y=|X|$.

<details><summary>Solution</summary>

1. (a) $|X|>\tfrac12$ means $X<-\tfrac12$ or $X>\tfrac12$: total length $1$, height $\tfrac12$.

   $$P(|X|>\frac12)=\frac12$$
2. (b) **Distribution:** $|x|$ on $[-1,1]$ goes from $0$ to $1$.

   $$R_Y=[0,1]$$
3. **Accumulation, $0\le y\le1$:** $|X|\le y\iff -y\le X\le y$, length $2y$.

   $$F_Y(y)=2y\cdot\frac12=y,\qquad F_Y(y)=\begin{cases}0,&y<0\\ y,&0\le y\le1\\ 1,&y>1\end{cases}$$
4. **Differentiation.**

   $$f_Y(y)=1,\qquad 0<y<1$$

**Answer:** (a) $\tfrac12$ (b) $f_Y(y)=1$ on $(0,1)$: $|X|\sim U(0,1)$.

</details>

**Problem: Try it 8 · Squaring a uniform on $[0,2]$ · Lecture 12** (intermediate)

$X\sim U[0,2]$, $Y=X^2$. (a) Find the CDF and PDF of $Y$. (b) Use $f_Y$ to compute $E[Y]$, and compare with $E[X^2]=\int x^2f_X(x)\,dx$.

<details><summary>Solution</summary>

1. (a) **Distribution:** $0\le X\le2$ gives $0\le Y\le4$.

   $$R_Y=[0,4]$$
2. **Accumulation, $0\le y\le4$:** $x^2\le y\iff-\sqrt y\le x\le\sqrt y$, but $f_X=0$ for $x<0$, so only $[0,\sqrt y]$ counts.

   $$F_Y(y)=\int_0^{\sqrt y}\frac12\,dx=\frac{\sqrt y}{2}$$
3. Outside the range: $0$ below, $1$ above.

   $$F_Y(y)=\begin{cases}0,&y<0\\ \sqrt y/2,&0\le y\le4\\ 1,&y>4\end{cases}$$
4. **Differentiation.**

   $$f_Y(y)=\frac{1}{4\sqrt y},\qquad 0<y<4$$
5. (b) $y\cdot\frac{1}{4\sqrt y}=\frac{\sqrt y}{4}$.

   $$E[Y]=\int_0^4\frac{\sqrt y}{4}\,dy=\frac14\cdot\frac23\,y^{3/2}\Big|_0^4=\frac43$$
6. Directly from $X$, no $f_Y$ needed (the two must match).

   $$E[X^2]=\int_0^2x^2\cdot\frac12\,dx=\frac{x^3}{6}\Big|_0^2=\frac43\;\checkmark$$

**Answer:** $F_Y=\tfrac{\sqrt y}{2}$, $f_Y=\dfrac{1}{4\sqrt y}$ on $(0,4)$; $E[Y]=\tfrac43=E[X^2]$.

</details>

**Problem: Try it 9 · Cosine of a uniform angle · Lecture 15** (advanced)

$X\sim U[-\pi,\pi]$ (a random phase). Find the CDF and PDF of $Y=\cos X$. Then write $F_Y$ for a **general** continuous $X$ on $[-\pi,\pi]$ in terms of $F_X$.

<details><summary>Solution</summary>

1. **Distribution:** cosine takes every value in $[-1,1]$.

   $$R_Y=[-1,1]$$
2. **Accumulation, $-1\le y\le1$:** on $[-\pi,\pi]$, $\cos x$ is largest at $0$ and falls toward $\pm\pi$. So $\cos x\le y$ on the two outer pieces, past $\pm\arccos y$.

   $$\{\cos X\le y\}=\{X\le-\arccos y\}\cup\{X\ge\arccos y\}$$
3. Uniform: the two pieces have total length $2(\pi-\arccos y)$, height $\tfrac{1}{2\pi}$.

   $$F_Y(y)=\frac{2(\pi-\arccos y)}{2\pi}=1-\frac{\arccos y}{\pi}$$
4. Outside the range.

   $$F_Y(y)=\begin{cases}0,&y<-1\\ 1-\dfrac{\arccos y}{\pi},&-1\le y\le1\\ 1,&y>1\end{cases}$$
5. **Differentiation:** $\frac{d}{dy}\arccos y=-\frac{1}{\sqrt{1-y^2}}$.

   $$f_Y(y)=\frac{1}{\pi\sqrt{1-y^2}},\qquad -1<y<1$$
6. **General $X$:** same $x$-set, written with $F_X$.

   $$F_Y(y)=F_X(-\arccos y)+1-F_X(\arccos y),\qquad -1\le y\le1$$

**Answer:** $F_Y(y)=1-\dfrac{\arccos y}{\pi}$, $f_Y(y)=\dfrac{1}{\pi\sqrt{1-y^2}}$ on $(-1,1)$. General: $F_X(-\arccos y)+1-F_X(\arccos y)$.

</details>

## Practice Questions

Test-style questions for Question 4, roughly easy → hard. Every solution follows **Range → CDF → PDF**. Solve on paper first.

**Problem: Question 1 · A decreasing linear function** (introductory)

$X\sim$ Exp$(\lambda)$. Find the CDF and PDF of $Y=-2X+3$.

<details><summary>Solution</summary>

1. **Range:** $X\ge0$, so $Y=3-2X\le3$.

   $$R_Y=(-\infty,3]$$
2. **CDF, $y\le3$:** $g$ is decreasing; dividing by $-2$ **flips** the inequality.

   $$-2X+3\le y\iff X\ge\frac{3-y}{2}$$
3. Use $P(X\ge x)=e^{-\lambda x}$ (here $x=\tfrac{3-y}{2}\ge0$).

   $$F_Y(y)=\begin{cases}e^{-\lambda(3-y)/2},&y\le3\\ 1,&y>3\end{cases}$$
4. **PDF:** chain rule, the inner derivative of $-\lambda(3-y)/2$ is $\tfrac\lambda2$.

   $$f_Y(y)=\frac{\lambda}{2}\,e^{-\lambda(3-y)/2},\qquad y<3$$

**Answer:** $F_Y(y)=e^{-\lambda(3-y)/2}$ for $y\le3$ (1 above); $f_Y(y)=\tfrac\lambda2e^{-\lambda(3-y)/2}$ for $y<3$.

</details>

**Problem: Question 2 · Rounding down an exponential** (intermediate)

$X\sim$ Exp$(\lambda)$ is rounded down to an integer: $Y=\lfloor X\rfloor$. What kind of random variable is $Y$? Find its distribution.

<details><summary>Solution</summary>

1. **Kind:** $\lfloor x\rfloor$ is a staircase, so $Y$ is **discrete**.

   $$R_Y=\{0,1,2,\dots\}$$
2. **PMF:** $Y=k$ exactly when $k\le X<k+1$.

   $$P(Y=k)=F_X(k+1)-F_X(k)=e^{-\lambda k}-e^{-\lambda(k+1)}$$
3. Factor it.

   $$P(Y=k)=\left(e^{-\lambda}\right)^k\left(1-e^{-\lambda}\right),\qquad k=0,1,2,\dots$$
4. This is the geometric PMF (counting failures before the first success) with success probability $p=1-e^{-\lambda}$.

   $$\sum_{k\ge0}(e^{-\lambda})^k(1-e^{-\lambda})=\frac{1-e^{-\lambda}}{1-e^{-\lambda}}=1\;\checkmark$$

**Answer:** Discrete: $P(Y=k)=e^{-\lambda k}(1-e^{-\lambda})$, $k=0,1,\dots$ (geometric with $p=1-e^{-\lambda}$).

</details>

**Problem: Question 3 · A reciprocal on $(1,2)$** (intermediate)

$X\sim U(1,2)$. Find the CDF and PDF of $Y=\dfrac1X$.

<details><summary>Solution</summary>

1. **Range:** $\tfrac1x$ maps $(1,2)$ onto $(\tfrac12,1)$.

   $$R_Y=\left(\frac12,1\right)$$
2. **CDF:** $\tfrac1x$ is decreasing for $x>0$. Since $X>0$: $\tfrac1X\le y\iff X\ge\tfrac1y$.

   $$F_Y(y)=1-F_X\!\left(\frac1y\right)=1-\left(\frac1y-1\right)=2-\frac1y$$
3. Outside the range.

   $$F_Y(y)=\begin{cases}0,&y<\frac12\\ 2-\dfrac1y,&\frac12\le y\le1\\ 1,&y>1\end{cases}$$
4. **PDF.** Check with the shortcut: $f_X(1/y)\cdot|{-1/y^2}|=1\cdot\tfrac{1}{y^2}$ ✓

   $$f_Y(y)=\frac{1}{y^2},\qquad \frac12<y<1$$

**Answer:** $F_Y(y)=2-\tfrac1y$ on $[\tfrac12,1]$; $f_Y(y)=\dfrac{1}{y^2}$ on $(\tfrac12,1)$.

</details>

**Problem: Question 4 · A decaying exponential** (intermediate)

$X\sim$ Exp$(\lambda)$. Find the CDF and PDF of $Y=e^{-X}$. What happens when $\lambda=1$?

<details><summary>Solution</summary>

1. **Range:** $X\in[0,\infty)$, so $e^{-X}$ goes from $1$ down toward $0$.

   $$R_Y=(0,1]$$
2. **CDF, $0<y\le1$:** $e^{-x}$ is decreasing: take $\ln$, then multiply by $-1$ (flip).

   $$e^{-X}\le y\iff -X\le\ln y\iff X\ge-\ln y$$
3. Use $P(X\ge x)=e^{-\lambda x}$ with $x=-\ln y\ge0$.

   $$F_Y(y)=e^{\lambda\ln y}=y^{\lambda}$$
4. Outside the range.

   $$F_Y(y)=\begin{cases}0,&y\le0\\ y^\lambda,&0<y\le1\\ 1,&y>1\end{cases}$$
5. **PDF.** With $\lambda=1$: $f_Y=1$ on $(0,1)$, so $Y\sim U(0,1)$.

   $$f_Y(y)=\lambda\,y^{\lambda-1},\qquad 0<y<1$$

**Answer:** $F_Y(y)=y^\lambda$, $f_Y(y)=\lambda y^{\lambda-1}$ on $(0,1)$; for $\lambda=1$, $Y\sim U(0,1)$.

</details>

**Problem: Question 5 · A timeout (mixed)** (intermediate)

A job takes $X\sim$ Exp$(1)$ seconds, but it is stopped after 1 second. The recorded time is $Y=\min\{X,1\}$. Find $F_Y(y)$, $P(Y=1)$, and describe the distribution of $Y$.

<details><summary>Solution</summary>

1. **Range:** times above 1 are recorded as 1.

   $$R_Y=[0,1]$$
2. **CDF, $0\le y<1$:** $\min\{X,1\}\le y\iff X\le y$ (because $1>y$).

   $$F_Y(y)=1-e^{-y}$$
3. **CDF, $y\ge1$:** $Y\le1$ always.

   $$F_Y(y)=\begin{cases}0,&y<0\\ 1-e^{-y},&0\le y<1\\ 1,&y\ge1\end{cases}$$
4. **Jump at 1:** just below 1 the CDF is $1-e^{-1}$, at 1 it is 1.

   $$P(Y=1)=P(X\ge1)=e^{-1}\approx 0.3679$$
5. **Mixed:** a density on $(0,1)$ plus a point mass at 1. Check: the total is 1.

   $$\int_0^1e^{-y}\,dy+e^{-1}=(1-e^{-1})+e^{-1}=1\;\checkmark$$

**Answer:** $F_Y=1-e^{-y}$ on $[0,1)$, $1$ for $y\ge1$; $P(Y=1)=e^{-1}\approx 0.3679$; mixed (density $e^{-y}$ on $(0,1)$).

</details>

**Problem: Question 6 · Absolute value of a $Cx^2$ variable · Tutorial 5 Q5** (intermediate)

$f_X(x)=Cx^2$ for $|x|\le1$, $0$ otherwise. (a) Find $C$. (b) Find the PDF of $Y=|X|$. (c) Find $E[Y^2]$ and $\mathrm{Var}[3X-1]$.

<details><summary>Solution</summary>

1. (a) **Total area 1.**

   $$\int_{-1}^{1}Cx^2\,dx=\frac{2C}{3}=1\;\Rightarrow\;C=\frac32$$
2. (b) **Range:** $|x|$ on $[-1,1]$.

   $$R_Y=[0,1]$$
3. **CDF, $0\le y\le1$:** $|X|\le y\iff-y\le X\le y$.

   $$F_Y(y)=\int_{-y}^{y}\frac32x^2\,dx=\frac{x^3}{2}\Big|_{-y}^{y}=y^3$$
4. **PDF.**

   $$f_Y(y)=3y^2,\qquad 0<y<1$$
5. (c) $E[Y^2]$ from $f_Y$.

   $$E[Y^2]=\int_0^1y^2\cdot3y^2\,dy=\frac35$$
6. $E[X]=0$ (symmetric $f_X$) and $E[X^2]=E[Y^2]=\tfrac35$, so $\mathrm{Var}(X)=\tfrac35$. Then $\mathrm{Var}(aX+b)=a^2\mathrm{Var}(X)$.

   $$\mathrm{Var}[3X-1]=9\cdot\frac35=\frac{27}{5}$$

**Answer:** (a) $C=\tfrac32$ (b) $f_Y(y)=3y^2$ on $(0,1)$ (c) $E[Y^2]=\tfrac35$, $\mathrm{Var}[3X-1]=\tfrac{27}{5}$.

</details>

**Problem: Question 7 · Power of a Gaussian noise voltage** (intermediate)

A noise voltage is $X\sim N(0,1)$. Its power (into $1\,\Omega$) is $Y=X^2$. (a) Write $F_Y(y)$ in terms of $\Phi$. (b) Find $f_Y(y)$. (c) Find $P(Y\le1)$.

<details><summary>Solution</summary>

1. **Range:** a square is never negative.

   $$R_Y=[0,\infty)$$
2. **CDF, $y\ge0$:** $X^2\le y\iff-\sqrt y\le X\le\sqrt y$. Then use $\Phi(-z)=1-\Phi(z)$.

   $$F_Y(y)=\Phi(\sqrt y)-\Phi(-\sqrt y)=2\Phi(\sqrt y)-1$$
3. **PDF:** $\Phi^{\prime}(z)=\tfrac{1}{\sqrt{2\pi}}e^{-z^2/2}$, chain rule with $\tfrac{d}{dy}\sqrt y=\tfrac{1}{2\sqrt y}$.

   $$f_Y(y)=2\cdot\frac{1}{\sqrt{2\pi}}e^{-y/2}\cdot\frac{1}{2\sqrt y}=\frac{e^{-y/2}}{\sqrt{2\pi y}},\qquad y>0$$
4. (c) Table: $\Phi(1)=0.8413$.

   $$P(Y\le1)=2\Phi(1)-1=2(0.8413)-1=0.6826$$

**Answer:** $F_Y(y)=2\Phi(\sqrt y)-1$ for $y\ge0$; $f_Y(y)=\dfrac{e^{-y/2}}{\sqrt{2\pi y}}$ for $y>0$; $P(Y\le1)\approx0.6827$.

</details>

**Problem: Question 8 · Squaring a lopsided uniform** (advanced)

$X\sim U(-1,2)$. Find the CDF and PDF of $Y=X^2$.

<details><summary>Solution</summary>

1. **Range:** smallest at $x=0$, largest at $x=2$.

   $$R_Y=[0,4]$$
2. **CDF, $0\le y\le1$:** $-\sqrt y\le X\le\sqrt y$ lies inside $(-1,2)$. Length $2\sqrt y$, height $\tfrac13$.

   $$F_Y(y)=\frac{2\sqrt y}{3}$$
3. **CDF, $1<y\le4$:** now $-\sqrt y<-1$, where $X$ never goes. The set shrinks to $[-1,\sqrt y]$.

   $$F_Y(y)=P(-1\le X\le\sqrt y)=\frac{\sqrt y+1}{3}$$
4. Collect the cases (both formulas give $\tfrac23$ at $y=1$, so no jump).

   $$F_Y(y)=\begin{cases}0,&y<0\\ \dfrac{2\sqrt y}{3},&0\le y\le1\\ \dfrac{\sqrt y+1}{3},&1<y\le4\\ 1,&y>4\end{cases}$$
5. **PDF:** differentiate each piece.

   $$f_Y(y)=\begin{cases}\dfrac{1}{3\sqrt y},&0<y<1\\ \dfrac{1}{6\sqrt y},&1<y<4\\ 0,&\text{otherwise}\end{cases}$$

**Answer:** $f_Y=\dfrac{1}{3\sqrt y}$ on $(0,1)$ and $\dfrac{1}{6\sqrt y}$ on $(1,4)$. Two regimes: below $y=1$ both $\pm\sqrt y$ are possible, above only $+\sqrt y$.

</details>

**Problem: Question 9 · The reciprocal, in general · Tutorial 6 Q1** (advanced)

$X$ is a continuous random variable with CDF $F_X$ and PDF $f_X$. Write the CDF and PDF of $Y=\dfrac1X$ in terms of $F_X$ and $f_X$.

<details><summary>Solution</summary>

1. **Range:** any nonzero real number (ignore $X=0$, probability $0$). The sign of $X$ matters, so split by the sign of $y$.

   $$R_Y\subseteq(-\infty,0)\cup(0,\infty)$$
2. **CDF, $y>0$:** if $X<0$ then $\tfrac1X<0<y$ always. If $X>0$: $\tfrac1X\le y\iff X\ge\tfrac1y$.

   $$F_Y(y)=P(X<0)+P\!\left(X\ge\frac1y\right)=F_X(0)+1-F_X\!\left(\frac1y\right)$$
3. **CDF, $y=0$:** $\tfrac1X\le0\iff X<0$.

   $$F_Y(0)=F_X(0)$$
4. **CDF, $y<0$:** only $X<0$ can work. Multiply $\tfrac1X\le y$ by $X<0$ (flip): $1\ge yX$; divide by $y<0$ (flip again): $X\ge\tfrac1y$.

   $$F_Y(y)=P\!\left(\frac1y\le X<0\right)=F_X(0)-F_X\!\left(\frac1y\right)$$
5. **PDF:** both nonzero cases contain $-F_X(1/y)$, and $\frac{d}{dy}\frac1y=-\frac{1}{y^2}$.

   $$f_Y(y)=-f_X\!\left(\frac1y\right)\cdot\left(-\frac{1}{y^2}\right)=\frac{1}{y^2}\,f_X\!\left(\frac1y\right),\qquad y\ne0$$

**Answer:** $F_Y(y)=F_X(0)+1-F_X(\tfrac1y)$ for $y>0$, $F_X(0)$ at $y=0$, $F_X(0)-F_X(\tfrac1y)$ for $y<0$; $f_Y(y)=\dfrac{1}{y^2}f_X(\tfrac1y)$.

</details>

**Problem: Question 10 · Squared distance from 1** (advanced)

$X\sim$ Exp$(1)$. Find the CDF and PDF of $Y=(X-1)^2$.

<details><summary>Solution</summary>

1. **Range:** smallest ($0$) at $x=1$; no upper limit.

   $$R_Y=[0,\infty)$$
2. **$x$-set:** $(x-1)^2\le y\iff 1-\sqrt y\le x\le1+\sqrt y$. But $X\ge0$, so it matters whether $1-\sqrt y$ is negative.

   $$1-\sqrt y\ge0\iff y\le1$$
3. **CDF, $0\le y\le1$:** the whole interval is in $[0,\infty)$. Use $F_X(x)=1-e^{-x}$.

   $$F_Y(y)=F_X(1+\sqrt y)-F_X(1-\sqrt y)=e^{-(1-\sqrt y)}-e^{-(1+\sqrt y)}$$
4. **CDF, $y>1$:** the left end is cut at $0$.

   $$F_Y(y)=F_X(1+\sqrt y)=1-e^{-(1+\sqrt y)}$$
5. **PDF:** $\tfrac{d}{dy}(1\pm\sqrt y)=\pm\tfrac{1}{2\sqrt y}$.

   $$f_Y(y)=\begin{cases}\dfrac{e^{-(1-\sqrt y)}+e^{-(1+\sqrt y)}}{2\sqrt y},&0<y<1\\ \dfrac{e^{-(1+\sqrt y)}}{2\sqrt y},&y>1\end{cases}$$

**Answer:** $F_Y=e^{-(1-\sqrt y)}-e^{-(1+\sqrt y)}$ on $[0,1]$, $1-e^{-(1+\sqrt y)}$ for $y>1$; differentiate for $f_Y$ (two pieces).

</details>
