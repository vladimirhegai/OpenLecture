r"""Test 2 - Question 4: functions of a random variable and their distributions (Lectures 12-15, Tutorial 6).

Layout (REWRITE_PLAN.md, v3): short top -> Topic 1 (what type is Y, discrete Y) -> Topic 2 (continuous Y: the CDF
method, one method for every g) -> Extras (flat pieces / mixed Y, the shortcut formula) -> practice.
Each topic: explanation + formulas first (open), then open worked examples (D.EX), one per kind of question.
Step words: Spot, Range, Rewrite, Accumulate, Differentiate, Jump.
"""
from math import acos, erf, exp, log, pi, sqrt

from lib226 import Doc, S, cite

D = Doc('q4', 'Test 2 - Question 4', ['functions_of_random_variables', 'cdf_method', 'monotonic_transformations',
                                     'dad_method', 'mixed_random_variables'])


def Phi(z):
    return 0.5 * (1 + erf(z / sqrt(2)))


D.P(r'**Lectures 12–15 · Tutorial 6.** **Question 4 asks:** you know $X$. Find the CDF and PDF (or PMF) of a new random variable $Y=g(X)$. For example, $X\sim U(-1,1)$ and $Y=X^3$.',
    cites=cite('L13', 5) + cite('L14', 5) + cite('L15', 5) + cite('T6', 1))

# =====================================================================================================
D.H('Topic 1: what type is Y, and discrete Y')
D.P(r'**First, look at $X$ and $g$.** They tell you what kind of answer to give:')
D.T(['When', '$Y$ is', 'Answer with', 'Example'],
    [[r'$X$ discrete, or $g$ a staircase', '**discrete**', 'a PMF (this topic)', r'$X^2$ of a die'],
     [r'$X$ continuous, $g$ never flat', '**continuous**', 'a CDF and a PDF (Topic 2)', r'$X^3$, $e^X$'],
     [r'$X$ continuous, $g$ flat somewhere', '**mixed**', 'a CDF with a jump (Extras)', r'$\max\{X,0\}$']], cites=cite('L14', 1))
D.P(r'**Discrete $Y$:** push each value of $X$ through $g$. If several $x$ land on the same $y$, **add** their chances:')
D.EQ(r'p_Y(y)=\sum_{x:\ g(x)=y}p_X(x)', cites=cite('L13', 5))
D.L([r'$p_X(x)$ = the chance $X$ takes the value $x$.',
     r'The sum runs over every $x$ that $g$ sends to this $y$.'])
D.P(r'Why it works: $Y=y$ happens when $X$ is **any** of those $x$. They can’t happen together, so their chances add.')

D.EX(r'Two values land on one: $Y=X^2$',
     r'$X$ is equally likely to be $-2,-1,0,1,2$. Find the PMF of $Y=X^2$.',
     [S(r'**Spot:** $X$ is discrete, so $Y$ is discrete. Answer with a PMF.'),
      S(r'**List** where each $x$ goes. Each $x$ has chance $\tfrac15$.', r'(-2,-1,0,1,2)\ \longrightarrow\ (4,\,1,\,0,\,1,\,4)'),
      S(r'**Add** the chances that land on the same $y$: $\pm1$ both give $1$, $\pm2$ both give $4$.',
        r'p_Y(0)=\frac15,\qquad p_Y(1)=\frac15+\frac15=\frac25,\qquad p_Y(4)=\frac25'),
      S(r'**Check:** they add to 1.', r'\frac15+\frac25+\frac25=1')],
     r'$p_Y(0)=\tfrac15$, $p_Y(1)=\tfrac25$, $p_Y(4)=\tfrac25$.')
D.EX(r'A staircase $g$: a 3-level quantizer (like Lecture 13)',
     r'$X\sim U(-1,1)$. $Y=-1$ if $X<-0.5$, $Y=0$ if $-0.5\le X\le0.5$, $Y=1$ if $X>0.5$. Find the PMF of $Y$.',
     [S(r'**Spot:** $X$ is continuous, but $g$ is a staircase with 3 outputs. So $Y$ is **discrete**.', r'Y\in\{-1,\,0,\,1\}'),
      S(r'Each value of $Y$ gets the chance of its $x$-interval. For $U(-1,1)$ that’s length × height $\tfrac12$.',
        (r'P(Y=-1)=P(X<-0.5)=0.5\cdot\frac12=\frac14', r'P(Y=0)=P(-0.5\le X\le0.5)=1\cdot\frac12=\frac12', r'P(Y=1)=P(X>0.5)=\frac14')),
      S(r'**Check:** they add to 1.', r'\frac14+\frac12+\frac14=1')],
     r'$p_Y(-1)=\tfrac14$, $p_Y(0)=\tfrac12$, $p_Y(1)=\tfrac14$.', cites=cite('L13', 6))

# =====================================================================================================
D.H('Topic 2: continuous Y, the CDF method (one method for every g)')
D.P(r'**The idea:** you don’t know $Y$’s CDF, but you know $X$’s. So turn the question about $Y$ into a question about $X$:')
D.EQ(r'F_Y(y)=P(Y\le y)=P\big(g(X)\le y\big)', cites=cite('L14', 5))
D.P(r'Then the PDF is the slope of the CDF:')
D.EQ(r'f_Y(y)=\frac{d}{dy}F_Y(y)')
D.P(r'**Steps** (the same for every $g$):')
D.L([r'**Range:** where can $Y$ land? Push the ends of $X$’s range through $g$. Below the range $F_Y=0$, above it $F_Y=1$.',
     r'**Rewrite:** solve “$g(X)\le y$” for $X$, so it says something about $X$ alone.',
     r'**Accumulate:** find $X$’s chance of that, using $F_X$ (or the area under $f_X$).',
     r'**Differentiate:** $f_Y(y)=F_Y^{\prime}(y)$.'], ordered=True)
D.P(r'**Only the Rewrite step changes**, and it depends on the shape of $g$:')
D.T(['$g$', 'Example', r'$g(X)\le y$ becomes', r'so $F_Y(y)=$'],
    [['only goes up', r'$X^3$, $e^X$, $2X-3$', r'$X\le g^{-1}(y)$', r'$F_X\big(g^{-1}(y)\big)$'],
     ['only goes down', r'$-3X+2$, $-\ln X$', r'$X\ge g^{-1}(y)$ (flipped)', r'$1-F_X\big(g^{-1}(y)\big)$'],
     ['turns around', r'$X^2$, $|X|$, $\cos X$', r'an interval, e.g. $-\sqrt y\le X\le\sqrt y$', r'$F_X(\sqrt y)-F_X(-\sqrt y)$']],
    cites=cite('L14', 5) + cite('L15', 1, 5))
D.L([r'$g^{-1}(y)$ = solve $y=g(x)$ for $x$. Example: $y=x^3$ gives $g^{-1}(y)=\sqrt[3]{y}$.',
     r'**Why the flip:** a decreasing $g$ reverses the order. Bigger $x$ gives smaller $y$. Example: $-3X+2\le y$, divide by $-3$: $X\ge\frac{2-y}{3}$.',
     r'**Why an interval:** when $g$ turns around, two $x$ give the same $y$ (for $x^2$: $\pm0.5$ both give $0.25$). So $g(X)\le y$ holds on a whole stretch of $x$. The lecture calls this DAD (Distribution, Accumulation, Differentiation): it’s the same steps.'])
D.GRAPH(['title "$Y=X^2$, $X\\sim U(-1,1)$: drag $y$"', 'x -1.3 1.3 label="$x$" height=250', 'y -0.25 1.25 label="$x^2$"',
         'slider h 0 1.2 0.36 step=0.01 label="$y$"',
         'curve "x^2" from=-1 to=1 color=1 label="$g(x)=x^2$"', 'hline "h" color=2',
         'region "(x*x<=h)*(x>=-1)*(x<=1)*(y>-0.2)*(y<-0.06)" color=4 label="$x$-set: $-\\sqrt y\\le x\\le\\sqrt y$"',
         'readout "$F_Y(y)$ = shaded length × $\\tfrac12$" "min(sqrt(h),1)"'],
        intro='**Turns around: finding the $x$-set.** Drag $y$. The shaded $x$-set is where the curve is below the line.')
D.P(r'**Special case $Y=aX+b$** (Lecture 15). It’s a line, so it only goes up ($a>0$) or only down ($a<0$):')
D.EQ(r'\begin{gathered}a>0:\quad F_Y(y)=F_X\Big(\frac{y-b}{a}\Big)\\ a<0:\quad F_Y(y)=1-F_X\Big(\frac{y-b}{a}\Big)\\ a=0:\quad Y=b\text{ always}\end{gathered}', cites=cite('L15', 2))
D.P(r'**CDFs you’ll plug in** (from Question 2), and the chain rule for the Differentiate step:')
D.L([r'Uniform $U(a,b)$: $\;F_X(x)=\dfrac{x-a}{b-a}$ for $a\le x\le b$.',
     r'Exponential$(\lambda)$: $\;F_X(x)=1-e^{-\lambda x}$ for $x\ge0$, so $P(X>x)=e^{-\lambda x}$.',
     r'Gaussian $N(\mu,\sigma^2)$: $\;F_X(x)=\Phi\Big(\dfrac{x-\mu}{\sigma}\Big)$, and $\Phi(-z)=1-\Phi(z)$.',
     r'Chain rule: $\;\dfrac{d}{dy}F_X\big(h(y)\big)=f_X\big(h(y)\big)\,h^{\prime}(y)$.'], cites=cite('L11', 1))
D.CO('warning', r'**Flip the $\le$** whenever you divide by a negative number or undo a decreasing function. Forgetting it gives $F_X(\dots)$ instead of $1-F_X(\dots)$.')
D.CO('warning', r'**Keep only $x$ that $X$ can take.** $X\sim U(-1,2)$, $Y=X^2$, $y=4$: the $x$-set $[-2,2]$ gets cut down to $[-1,2]$.')

D.EX(r'Goes up: $Y=X^3$ (Lecture 14)',
     r'$X\sim U(-1,1)$. Find the CDF and PDF of $Y=X^3$.',
     [S(r'**Spot:** $x^3$ only goes up, and $X$ is continuous. Use the first row of the table.', r'F_Y(y)=F_X\big(g^{-1}(y)\big)'),
      S(r'**Range:** $(-1)^3=-1$ and $1^3=1$.', r'-1\le Y\le1'),
      S(r'**Rewrite:** take the cube root of both sides.', r'X^3\le y\quad\Longleftrightarrow\quad X\le\sqrt[3]{y}'),
      S(r'**Accumulate:** $X$’s CDF is $F_X(x)=\tfrac{x+1}{2}$ on $[-1,1]$. Put $\sqrt[3]{y}$ in for $x$.',
        r'F_Y(y)=\begin{cases}0,&y<-1\\ \dfrac{\sqrt[3]{y}+1}{2},&-1\le y\le1\\ 1,&y>1\end{cases}'),
      S(r'**Differentiate:** the derivative of $y^{1/3}$ is $\tfrac13y^{-2/3}$.', r'f_Y(y)=\frac12\cdot\frac13\,y^{-2/3}=\frac{1}{6\,y^{2/3}},\qquad -1<y<1')],
     r'$F_Y(y)=\dfrac{\sqrt[3]{y}+1}{2}$ on $[-1,1]$; $f_Y(y)=\dfrac{1}{6\,y^{2/3}}$ on $(-1,1)$.', cites=cite('L14', 6, 7))
D.EX(r'Goes up, with the chain rule: $Y=\ln X$ (Tutorial 6 Q2)',
     r'$X\sim$ Exp$(1)$. Find the PDF of $Y=\ln X$.',
     [S(r'**Spot:** $\ln x$ only goes up.', r'F_Y(y)=F_X\big(g^{-1}(y)\big)'),
      S(r'**Range:** $X$ is anywhere in $(0,\infty)$, so $\ln X$ can be any real number.', r'-\infty<Y<\infty'),
      S(r'**Rewrite:** undo the $\ln$.', r'\ln X\le y\quad\Longleftrightarrow\quad X\le e^{y}'),
      S(r'**Accumulate:** plug $e^y$ into $F_X(x)=1-e^{-x}$.', r'F_Y(y)=1-e^{-e^{y}}'),
      S(r'**Differentiate:** chain rule. The inside, $-e^{y}$, has derivative $-e^{y}$.', r'f_Y(y)=e^{y}\,e^{-e^{y}}')],
     r'$f_Y(y)=e^{y}\,e^{-e^{y}}$ for all real $y$.', cites=cite('T6', 1))
D.EX(r'Goes down: $Y=-3X+2$ (Lecture 15)',
     r'$X\sim U(0,1)$. Find the CDF and PDF of $Y=-3X+2$.',
     [S(r'**Spot:** the slope is $-3$, so $g$ only goes down. Use the second row: the $\le$ flips.', r'F_Y(y)=1-F_X\big(g^{-1}(y)\big)'),
      S(r'**Range:** $x=0$ gives $2$, $x=1$ gives $-1$.', r'-1\le Y\le2'),
      S(r'**Rewrite:** subtract 2, then divide by $-3$. That flips the $\le$.', r'-3X+2\le y\quad\Longleftrightarrow\quad X\ge\frac{2-y}{3}'),
      S(r'**Accumulate:** $F_X(x)=x$, so $P(X\ge t)=1-t$.', r'F_Y(y)=1-\frac{2-y}{3}=\frac{y+1}{3},\qquad -1\le y\le2'),
      S(r'**Differentiate.**', r'f_Y(y)=\frac13,\qquad -1<y<2')],
     r'$f_Y(y)=\tfrac13$ on $(-1,2)$, so $Y\sim U(-1,2)$.', cites=cite('L15', 2))
D.EX(r'Turns around: $Y=X^2$ (Lecture 15)',
     r'$X\sim U(-1,1)$. Find the CDF and PDF of $Y=X^2$.',
     [S(r'**Spot:** $x^2$ turns around at $0$. Use the third row: an interval.', r'F_Y(y)=F_X(\sqrt y)-F_X(-\sqrt y)'),
      S(r'**Range:** $X$ is in $[-1,1]$, so $X^2$ is in $[0,1]$.', r'0\le Y\le1'),
      S(r'**Rewrite:** a square is at most $y$ when $x$ is within $\sqrt y$ of $0$.', r'X^2\le y\quad\Longleftrightarrow\quad -\sqrt y\le X\le\sqrt y'),
      S(r'**Accumulate:** that interval has length $2\sqrt y$, and the height of $f_X$ is $\tfrac12$.', r'F_Y(y)=2\sqrt y\cdot\frac12=\sqrt y,\qquad 0\le y\le1'),
      S(r'**Differentiate.**', r'f_Y(y)=\frac{1}{2\sqrt y},\qquad 0<y<1')],
     r'$F_Y(y)=\sqrt y$ on $[0,1]$ ($0$ below, $1$ above); $f_Y(y)=\dfrac{1}{2\sqrt y}$ on $(0,1)$.', cites=cite('L15', 3, 4))
D.EX(r'Turns around: $Y=|X|$ (Tutorial 6 Q4)',
     r'$X\sim U(-1,1)$. Find the PDF of $Y=|X|$, then $P(|X|>\tfrac12)$.',
     [S(r'**Spot:** $|x|$ turns around at $0$. An interval again.'),
      S(r'**Range:** $|x|$ on $[-1,1]$ runs from $0$ to $1$.', r'0\le Y\le1'),
      S(r'**Rewrite.**', r'|X|\le y\quad\Longleftrightarrow\quad -y\le X\le y'),
      S(r'**Accumulate:** length $2y$, height $\tfrac12$.', r'F_Y(y)=2y\cdot\frac12=y'),
      S(r'**Differentiate.**', r'f_Y(y)=1,\qquad 0<y<1'),
      S(r'The probability is one minus the CDF.', r'P\big(|X|>\tfrac12\big)=1-F_Y\big(\tfrac12\big)=1-\frac12=\frac12')],
     r'$f_Y(y)=1$ on $(0,1)$, so $|X|\sim U(0,1)$; $P(|X|>\tfrac12)=\tfrac12$.', cites=cite('T6', 1))
gl = 1 - Phi(1)
D.EX(r'A Gaussian through a line: $Y=2X+1$',
     r'$X\sim N(0,1)$. Write $F_Y(y)$ for $Y=2X+1$ using $\Phi$. What distribution is $Y$? Find $P(Y>3)$.',
     [S(r'**Spot:** slope $2>0$, so $g$ only goes up. **Read off** $a$ and $b$ for the $aX+b$ formula.', r'a=2,\qquad b=1'),
      S(r'**Rewrite.**', r'2X+1\le y\quad\Longleftrightarrow\quad X\le\frac{y-1}{2}'),
      S(r'**Accumulate:** $X$ is standard normal, so $F_X=\Phi$.', r'F_Y(y)=\Phi\Big(\frac{y-1}{2}\Big)'),
      S(r'That’s the CDF of a Gaussian with $\mu=1$, $\sigma=2$.', r'Y\sim N(1,\,4)'),
      S(r'Complement, then the table: $\Phi(1)=0.8413$.', r'P(Y>3)=1-\Phi\Big(\frac{3-1}{2}\Big)=1-\Phi(1)\approx' + f'{gl:.4f}')],
     f'$F_Y(y)=\\Phi\\left(\\tfrac{{y-1}}{{2}}\\right)$, so $Y\\sim N(1,4)$; $P(Y>3)\\approx {gl:.4f}$.')

# =====================================================================================================
D.H('Extras: flat pieces (mixed Y) and a shortcut formula')
D.P(r'**When $g$ goes flat.** Clipping, a rectifier, a limiter, a timeout: $\max\{X,0\}$, $\min\{X,1\}$. A flat piece at height $c$ sends a whole interval of $X$ to the single value $c$. So $Y=c$ has real chance, and $F_Y$ **jumps** there:')
D.EQ(r'P(Y=c)=P\big(X\text{ is in the flat part}\big)', cites=cite('L14', 4))
D.L([r'**Range:** as always.',
     r'**Jump:** one per flat piece, sized $P(X$ in that piece$)$.',
     r'**Accumulate** everywhere else, as in Topic 2.',
     r'**Spot:** jumps plus a slope means $Y$ is **mixed**.'], ordered=True)
D.EX(r'Flat piece: a half-wave rectifier $Y=\max\{X,0\}$ (Lecture 14)',
     r'$X\sim U(-1,1)$. Find the CDF of $Y=\max\{X,0\}$. What type is $Y$?',
     [S(r'**Range:** negative $X$ become $0$, positive $X$ stay.', r'0\le Y\le1'),
      S(r'**Jump** at $0$: the flat part is every $X\le0$.', r'P(Y=0)=P(X\le0)=\frac12'),
      S(r'**Accumulate**, $0\le y\le1$: $\max\{X,0\}\le y$ just means $X\le y$.', r'F_Y(y)=P(X\le y)=\frac{y+1}{2}'),
      S(r'Put the pieces together.', r'F_Y(y)=\begin{cases}0,&y<0\\ \dfrac{y+1}{2},&0\le y\le1\\ 1,&y>1\end{cases}'),
      S(r'**Spot:** a jump of $\tfrac12$ at $0$, then a slope.', r'\text{mixed}')],
     r'Mixed: $P(Y=0)=\tfrac12$, plus density $\tfrac12$ on $(0,1)$.', cites=cite('L14', 2, 3))
D.GRAPH(['title "$F_Y$ for $Y=\\max\\{X,0\\}$: the flat piece becomes a jump"', 'x -0.6 1.5 label="$y$" height=200',
         'y 0 1.12 label="$F_Y(y)$"',
         'segment "-0.6" "0" "0" "0" color=2', 'curve "(x+1)/2" from=0 to=1 color=2', 'segment "1" "1" "1.5" "1" color=2',
         'point "0" "0.5" color=2', 'segment "0" "0" "0" "0.5" color=2 dash', 'text "0.42" "0.25" "jump $\\tfrac12=P(Y=0)$"'],
        intro='**What the jump looks like:**')

D.P(r'**The shortcut formula** (not from the lectures: use it to check your answer). It skips the CDF. It works when $g$ only goes up **or** only goes down:')
D.EQ(r'f_Y(y)=f_X\big(g^{-1}(y)\big)\cdot\Big|\frac{d}{dy}g^{-1}(y)\Big|')
D.P(r'When $g$ turns around, add one term per $x$ that lands on $y$:')
D.EQ(r'\begin{gathered}Y=X^2:\quad f_Y(y)=\frac{f_X(\sqrt y)+f_X(-\sqrt y)}{2\sqrt y}\\ Y=|X|:\quad f_Y(y)=f_X(y)+f_X(-y)\end{gathered}\qquad y>0')
D.P(r'**A line keeps the family:** Gaussian in, Gaussian out. Uniform in, uniform out (push the two ends through).')
D.EQ(r'X\sim N(\mu,\sigma^2)\quad\Longrightarrow\quad aX+b\sim N(a\mu+b,\ a^2\sigma^2)')
D.EX(r'Shortcut check: $Y=X^3$ and $Y=X^2$',
     r'Check the Topic 2 answers for $X\sim U(-1,1)$ with the shortcut formulas.',
     [S(r'$Y=X^3$: **read off** $f_X=\tfrac12$, $g^{-1}(y)=y^{1/3}$, its derivative is $\tfrac13y^{-2/3}$.', r'f_Y(y)=\frac12\cdot\frac13\,y^{-2/3}=\frac{1}{6\,y^{2/3}}\quad\checkmark'),
      S(r'$Y=X^2$: **read off** $f_X(\sqrt y)=f_X(-\sqrt y)=\tfrac12$.', r'f_Y(y)=\frac{\frac12+\frac12}{2\sqrt y}=\frac{1}{2\sqrt y}\quad\checkmark')],
     r'Both match the CDF-method answers.')

# =====================================================================================================
D.H('Practice Questions')
D.CO('tip', r'''**Question 4 is always one of these.** Spot the type of $Y$ and the shape of $g$, then run the steps:

1. **Discrete $Y$** ($X$ discrete or $g$ a staircase): add the chances that land on the same value.
2. **Continuous $Y$:** Range → Rewrite $g(X)\le y$ as a statement about $X$ → Accumulate with $F_X$ → Differentiate.
   - only up: $F_X(g^{-1}(y))$ · only down: $1-F_X(g^{-1}(y))$ · turns around: an interval of $x$.
3. **Flat piece (mixed $Y$):** a jump $P(X$ in the flat part$)$, then accumulate the rest.''')
D.P('Test-style, easy → hard. Solve on paper first, then open the solution.')

D.Q('Discrete Y · what type is $Y$ · Lecture 13 Examples 1–2',
    r'$X$ = number of failed packet sends, with $P(X=0,1,2,3)=0.4,\ 0.3,\ 0.2,\ 0.1$. '
    r'(a) Find the PMF of $Y=2X+1$. (b) Find the PMF of $Z=(X-1)^2$. '
    r'(c) $V\sim U(0,1)$ goes into a 1-bit converter: $B=0$ if $V<0.5$, $B=1$ if $V\ge0.5$. What type is $B$? Find its PMF.',
    [S(r'**Type:** $X$ discrete → discrete $Y$ (Topic 1). (a) Each $x$ gives a different $y$, so the chances just move.', r'p_Y(1)=0.4,\ \ p_Y(3)=0.3,\ \ p_Y(5)=0.2,\ \ p_Y(7)=0.1'),
     S(r'(b) **Values:** $x=0,1,2,3$ give $Z=1,0,1,4$.', r'Z\in\{0,1,4\}'),
     S(r'$x=0$ and $x=2$ both give $Z=1$: **add** them.', r'p_Z(0)=0.3,\quad p_Z(1)=0.4+0.2=0.6,\quad p_Z(4)=0.1'),
     S(r'(c) **Spot:** a staircase $g$ → **discrete**. Each value gets the chance of its interval.', r'P(B=0)=P(V<0.5)=\frac12,\quad P(B=1)=\frac12')],
    r'(a) $0.4,0.3,0.2,0.1$ at $1,3,5,7$ (b) $0.3,0.6,0.1$ at $0,1,4$ (c) discrete, $\tfrac12,\tfrac12$.',
    diff='introductory', cites=cite('L13', 5, 6))

D.Q('CDF method, goes up · Exponential of a uniform · Tutorial 6 Q3',
    r'$X\sim U(0,1)$. Find the CDF and PDF of $Y=e^X$.',
    [S(r'**Type:** $e^x$ only goes up → CDF method, first row.'),
     S(r'**Range:** $e^0=1$ to $e^1=e$.', r'1\le Y\le e'),
     S(r'**Rewrite:** solve $y=g(x)$ for $x$.', r'y=e^{x}\quad\Longrightarrow\quad x=\ln y'),
     S(r'**Accumulate:** $F_X(x)=x$ on $[0,1]$.', r'F_Y(y)=\ln y,\qquad 1\le y\le e'),
     S(r'**Differentiate.**', r'f_Y(y)=\frac1y,\qquad 1<y<e')],
    r'$F_Y=\ln y$ on $[1,e]$ ($0$ below, $1$ above); $f_Y(y)=\dfrac1y$ for $1<y<e$.', diff='introductory', cites=cite('T6', 1))

D.Q('CDF method, goes down · decreasing $g$',
    r'(a) $X\sim$ Exp$(\lambda)$. Find the CDF and PDF of $Y=-2X+3$. (b) $X\sim U(0,1)$. Find the CDF and PDF of $Y=-\ln X$.',
    [S(r'(a) **Type:** slope $-2$, only goes down → CDF method, the $\le$ flips. **Range:** $X\ge0$, so $Y=3-2X\le3$.', r'Y\le3'),
     S(r'**Rewrite:** solve $y=g(x)$ for $x$.', r'y=-2x+3\quad\Longrightarrow\quad x=\frac{3-y}{2}'),
     S(r'**Accumulate:** the $\le$ flips. Then $P(X\ge x)=e^{-\lambda x}$.', (r'-2X+3\le y\iff X\ge\frac{3-y}{2}', r'F_Y(y)=e^{-\lambda(3-y)/2},\qquad y\le3')),
     S(r'**Differentiate** (chain rule: the inside has slope $\tfrac\lambda2$).', r'f_Y(y)=\frac{\lambda}{2}\,e^{-\lambda(3-y)/2},\qquad y<3'),
     S(r'(b) **Type:** $-\ln x$ only goes down → CDF method, the $\le$ flips. **Range:** $X\in(0,1)$, so $-\ln X\in(0,\infty)$.', r'Y>0'),
     S(r'**Rewrite:** solve $y=g(x)$ for $x$.', r'y=-\ln x\quad\Longrightarrow\quad x=e^{-y}'),
     S(r'**Accumulate:** the $\le$ flips, and $P(X\ge t)=1-t$.', r'F_Y(y)=1-e^{-y},\qquad y\ge0'),
     S(r'**Differentiate.** That’s the Exp$(1)$ PDF.', r'f_Y(y)=e^{-y},\qquad y>0')],
    r'(a) $F_Y=e^{-\lambda(3-y)/2}$ for $y\le3$, $f_Y=\tfrac\lambda2e^{-\lambda(3-y)/2}$ (b) $F_Y=1-e^{-y}$, $f_Y=e^{-y}$: $Y\sim$ Exp$(1)$.')

g7 = 1 - Phi(1)
D.Q('CDF method, goes up · a Gaussian through a line · like Lecture 13 sensor',
    r'A sensor reading is $X\sim N(2,9)$. It is calibrated to $Y=2X-3$. '
    r'(a) Write $F_Y(y)$ using $\Phi$. (b) What are the mean and variance of $Y$? (c) Find $P(Y>7)$.',
    [S(r'**Type:** slope $2>0$, only goes up → CDF method, first row.'),
     S(r'**Rewrite:** solve $y=g(x)$ for $x$.', r'y=2x-3\quad\Longrightarrow\quad x=\frac{y+3}{2}'),
     S(r'(a) **Accumulate**, then standardise with $\mu=2$, $\sigma=3$.', r'F_Y(y)=\Phi\Big(\frac{\frac{y+3}{2}-2}{3}\Big)=\Phi\Big(\frac{y-1}{6}\Big)'),
     S(r'(b) That’s the CDF of $N(1,36)$. The line shortcut agrees: $2\cdot2-3=1$, $2^2\cdot9=36$.', r'Y\sim N(1,\,36)'),
     S(r'(c) Complement, then the table: $\Phi(1)=0.8413$.', r'P(Y>7)=1-\Phi\Big(\frac{7-1}{6}\Big)=1-\Phi(1)\approx' + f'{g7:.4f}')],
    f'(a) $\\Phi\\left(\\tfrac{{y-1}}{{6}}\\right)$ (b) mean $1$, variance $36$ (c) $\\approx {g7:.4f}$', cites=cite('L13', 3))

D.Q('CDF method · $Y=aX+b$, in general · Lecture 15',
    r'$X$ is continuous with CDF $F_X$. (a) Write $F_Y$ for $Y=aX+b$ when $a>0$, $a<0$ and $a=0$. '
    r'(b) Use it for $X\sim U(0,1)$ and $Y=-3X+2$: find $F_Y$ and $f_Y$. What is $Y$?',
    [S(r'(a) **$a>0$:** goes up. Dividing by $a$ keeps the $\le$.', r'F_Y(y)=P\Big(X\le\frac{y-b}{a}\Big)=F_X\Big(\frac{y-b}{a}\Big)'),
     S(r'**$a<0$:** goes down. Dividing by $a$ **flips** it.', r'F_Y(y)=P\Big(X\ge\frac{y-b}{a}\Big)=1-F_X\Big(\frac{y-b}{a}\Big)'),
     S(r'**$a=0$:** $Y=b$ always: one step from $0$ to $1$ at $b$.', r'F_Y(y)=\begin{cases}0,&y<b\\ 1,&y\ge b\end{cases}'),
     S(r'(b) **Range:** $X\in[0,1]$ gives $Y\in[-1,2]$. **Accumulate** with $a=-3$, $F_X(x)=x$.',
       r'F_Y(y)=1-\frac{2-y}{3}=\frac{y+1}{3},\qquad -1\le y\le2'),
     S(r'**Differentiate.**', r'f_Y(y)=\frac13\ \text{ on }(-1,2)\quad\Rightarrow\quad Y\sim U(-1,2)')],
    r'(a) $F_X(\tfrac{y-b}{a})$; $1-F_X(\tfrac{y-b}{a})$; a step at $b$ (b) $F_Y=\tfrac{y+1}{3}$ on $[-1,2]$, $Y\sim U(-1,2)$.',
    cites=cite('L15', 2))

m1 = exp(-1)
D.Q('Extras: flat pieces · timeout and limiter',
    r'(a) A job takes $X\sim$ Exp$(1)$ seconds, but it is stopped after 1 second: $Y=\min\{X,1\}$. Find $F_Y$ and $P(Y=1)$. '
    r'(b) $X\sim U(-2,2)$ goes through a limiter: $W=-1$ if $X<-1$, $W=X$ if $-1\le X\le1$, $W=1$ if $X>1$. Find $F_W$. What type is $W$?',
    [S(r'(a) **Type:** flat at $1$ → a jump (mixed $Y$). **Range:** times above 1 are recorded as 1.', r'0\le Y\le1'),
     S(r'**Jump** at $1$: every $X\ge1$ lands there.', r'P(Y=1)=P(X\ge1)=e^{-1}\approx ' + f'{m1:.4f}'),
     S(r'**Accumulate**, $0\le y<1$: $\min\{X,1\}\le y$ just means $X\le y$.', r'F_Y(y)=1-e^{-y}'),
     S(r'(b) **Type:** flat at $-1$ and at $1$ → two jumps. **Jumps:** each flat part has length 1, height $\tfrac14$.',
       (r'P(W=-1)=P(X<-1)=\frac14', r'P(W=1)=P(X>1)=\frac14')),
     S(r'**Accumulate** in the middle: $W\le w$ means $X\le w$, and $F_X(x)=\tfrac{x+2}{4}$.',
       r'F_W(w)=\begin{cases}0,&w<-1\\ \dfrac{w+2}{4},&-1\le w<1\\ 1,&w\ge1\end{cases}'),
     S(r'**Spot:** jumps plus a slope → **mixed**.')],
    f'(a) $F_Y=1-e^{{-y}}$ on $[0,1)$, $1$ for $y\\ge1$; $P(Y=1)=e^{{-1}}\\approx {m1:.4f}$ '
    r'(b) $F_W=\tfrac{w+2}{4}$ on $[-1,1)$, jumps of $\tfrac14$ at $\pm1$: mixed.')

D.Q('CDF method, turns around · $|X|$ of a $Cx^2$ variable · Tutorial 5 Q5',
    r'$f_X(x)=Cx^2$ for $|x|\le1$, $0$ otherwise. (a) Find $C$. (b) Find the PDF of $Y=|X|$. (c) Find $E[Y^2]$ and $\mathrm{Var}[3X-1]$.',
    [S(r'(a) **Find $c$:** total area $=1$.', r'\int_{-1}^{1}Cx^2\,dx=\frac{2C}{3}=1\quad\Rightarrow\quad C=\frac32'),
     S(r'(b) **Type:** $|x|$ turns around at $0$ → CDF method, an interval. **Range:** $0\le Y\le1$.', r'0\le Y\le1'),
     S(r'**Accumulate:** $|X|\le y$ means $-y\le X\le y$.', r'F_Y(y)=\int_{-y}^{y}\frac32x^2\,dx=y^3'),
     S(r'**Differentiate.** (Shortcut check: $f_X(y)+f_X(-y)=\tfrac32y^2+\tfrac32y^2=3y^2$ ✓.)', r'f_Y(y)=3y^2,\qquad 0<y<1'),
     S(r'(c) $E[Y^2]$ from $f_Y$.', r'E[Y^2]=\int_0^1y^2\cdot3y^2\,dy=\frac35'),
     S(r'$f_X$ is symmetric, so $E[X]=0$ and $\mathrm{Var}(X)=E[X^2]=E[Y^2]$. Then $\mathrm{Var}(aX+b)=a^2\mathrm{Var}(X)$.',
       r'\mathrm{Var}[3X-1]=9\cdot\frac35=\frac{27}{5}')],
    r'(a) $C=\tfrac32$ (b) $f_Y(y)=3y^2$ on $(0,1)$ (c) $E[Y^2]=\tfrac35$, $\mathrm{Var}[3X-1]=\tfrac{27}{5}$.', cites=cite('T5', 1))

p1 = 2 * Phi(1) - 1
D.Q('CDF method, turns around · power of a Gaussian noise voltage',
    r'A noise voltage is $X\sim N(0,1)$. Its power is $Y=X^2$. (a) Write $F_Y(y)$ using $\Phi$. (b) Find $f_Y(y)$. (c) Find $P(Y\le1)$.',
    [S(r'**Type:** $x^2$ turns around → CDF method, an interval. **Range:** $Y\ge0$.', r'Y\ge0'),
     S(r'(a) **Accumulate:** $X^2\le y$ means $-\sqrt y\le X\le\sqrt y$. Then $\Phi(-z)=1-\Phi(z)$.',
       r'F_Y(y)=\Phi(\sqrt y)-\Phi(-\sqrt y)=2\Phi(\sqrt y)-1,\qquad y\ge0'),
     S(r'(b) **Differentiate:** $\Phi^{\prime}(z)=\tfrac{1}{\sqrt{2\pi}}e^{-z^2/2}$, times the inside derivative $\tfrac{1}{2\sqrt y}$.',
       r'f_Y(y)=2\cdot\frac{1}{\sqrt{2\pi}}e^{-y/2}\cdot\frac{1}{2\sqrt y}=\frac{e^{-y/2}}{\sqrt{2\pi y}},\qquad y>0'),
     S(r'(c) Table: $\Phi(1)=0.8413$.', r'P(Y\le1)=2(0.8413)-1=' + f'{2 * 0.8413 - 1:.4f}')],
    r'$F_Y(y)=2\Phi(\sqrt y)-1$ for $y\ge0$; $f_Y(y)=\dfrac{e^{-y/2}}{\sqrt{2\pi y}}$ for $y>0$; $P(Y\le1)\approx' + f'{p1:.4f}$.',
    cites=cite('L12', 1))

D.Q('CDF method, turns around · squaring a lopsided uniform',
    r'$X\sim U(-1,2)$. Find the CDF and PDF of $Y=X^2$.',
    [S(r'**Type:** $x^2$ turns around → CDF method, an interval. **Range:** smallest at $x=0$, largest at $x=2$.', r'0\le Y\le4'),
     S(r'**Accumulate**, $0\le y\le1$: both $\pm\sqrt y$ are inside $(-1,2)$. Length $2\sqrt y$, height $\tfrac13$.', r'F_Y(y)=\frac{2\sqrt y}{3}'),
     S(r'**Accumulate**, $1<y\le4$: $-\sqrt y$ is below $-1$, where $X$ never goes. Only $[-1,\sqrt y]$ is left.', r'F_Y(y)=\frac{\sqrt y+1}{3}'),
     S(r'**Differentiate** each piece.', r'f_Y(y)=\begin{cases}\dfrac{1}{3\sqrt y},&0<y<1\\ \dfrac{1}{6\sqrt y},&1<y<4\\ 0,&\text{otherwise}\end{cases}')],
    r'Two pieces: $\dfrac{1}{3\sqrt y}$ on $(0,1)$, $\dfrac{1}{6\sqrt y}$ on $(1,4)$. Above $y=1$ only $+\sqrt y$ is possible.',
    diff='advanced')

# the one real root of x^3 - 3x = 3, by bisection
lo, hi = 2.0, 2.2
for _ in range(80):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if mid ** 3 - 3 * mid < 3 else (lo, mid)
x3 = lo
D.Q('CDF method, turns around · $F_Y$ from a picture · Lecture 15',
    r'$X$ is continuous with CDF $F_X$, and $Y=g(X)$ with $g(x)=x^3-3x$ (graph below: it peaks at $(-1,2)$ and dips to $(1,-2)$). '
    r'Write (a) $F_Y(3)$, (b) $F_Y(0)$, (c) $F_Y(-3)$ using $F_X$. (d) Find $F_Y(0)$ when $X\sim U(-2,2)$.',
    [S(r'**Type:** $g$ turns around twice → CDF method, intervals. **Accumulate:** for each height, find where the curve is below the line.'),
     S(r'(a) $y=3$ is above the bump: it cuts the curve **once**, at $x\approx' + f'{x3:.3f}' + r'$. Below the line = everything left of it.',
       r'F_Y(3)=F_X(' + f'{x3:.3f}' + r')'),
     S(r'(b) $y=0$ cuts **three** times: $x^3-3x=0$ at $-\sqrt3,\ 0,\ \sqrt3$. Below on $x\le-\sqrt3$ and on $0\le x\le\sqrt3$.',
       r'F_Y(0)=F_X(-\sqrt3)+F_X(\sqrt3)-F_X(0)'),
     S(r'(c) $y=-3$ is below the dip: one cut, at $x\approx-' + f'{x3:.3f}' + r'$.', r'F_Y(-3)=F_X(-' + f'{x3:.3f}' + r')'),
     S(r'(d) Plug in $F_X(x)=\tfrac{x+2}{4}$.', r'\frac{2-\sqrt3}{4}+\frac{2+\sqrt3}{4}-\frac24=\frac12')],
    f'(a) $F_X({x3:.3f})$ (b) $F_X(-\\sqrt3)+F_X(\\sqrt3)-F_X(0)$ (c) $F_X(-{x3:.3f})$ (d) $\\tfrac12$', diff='advanced', cites=cite('L15', 5))
D.GRAPH(['title "$g(x)=x^3-3x$: drag the line to height $y$"', 'x -2.6 2.6 label="$x$" height=280', 'y -4 4 label="$g(x)$"',
         'slider h -3.5 3.5 0 step=0.1 label="$y$"',
         'curve "x^3-3*x" from=-2.2 to=2.2 color=1 label="$g(x)$"', 'hline "h" color=2'],
        intro='For the question above: drag $y$ and count where the curve is below the line.')

D.Q('CDF method, turns around · $Y=\\cos X$ · Lecture 15',
    r'$X$ is continuous and takes values in $[-\pi,\pi]$. (a) Write $F_Y(y)$ for $Y=\cos X$ using $F_X$, for $-1\le y\le1$. '
    r'(b) Find $F_Y$ and $f_Y$ when $X\sim U(-\pi,\pi)$.',
    [S(r'**Type:** $\cos x$ goes up then down → CDF method, intervals. **Range:** $-1\le\cos X\le1$.', r'-1\le Y\le1'),
     S(r'(a) **Accumulate:** $\cos x$ is highest at $x=0$, so $\cos x\le y$ on the **two ends**: $x\le-\arccos y$ or $x\ge\arccos y$.',
       r'F_Y(y)=F_X(-\arccos y)+1-F_X(\arccos y)'),
     S(r'(b) Plug in $F_X(x)=\tfrac{x+\pi}{2\pi}$, writing $a=\arccos y$.', r'F_Y(y)=\frac{\pi-a}{2\pi}+1-\frac{a+\pi}{2\pi}=1-\frac{\arccos y}{\pi}'),
     S(r'**Differentiate:** the derivative of $\arccos y$ is $-\dfrac{1}{\sqrt{1-y^2}}$.', r'f_Y(y)=\frac{1}{\pi\sqrt{1-y^2}},\qquad -1<y<1')],
    r'(a) $F_X(-\arccos y)+1-F_X(\arccos y)$ (b) $F_Y=1-\dfrac{\arccos y}{\pi}$, $f_Y=\dfrac{1}{\pi\sqrt{1-y^2}}$ on $(-1,1)$.',
    diff='advanced', cites=cite('L15', 6))

D.Q('CDF method, goes down on two sides · the reciprocal, in general · Tutorial 6 Q1',
    r'$X$ is continuous with CDF $F_X$ and PDF $f_X$. Write the CDF and PDF of $Y=\dfrac1X$ using $F_X$ and $f_X$.',
    [S(r'**Type:** $\tfrac1x$ goes down on each side of $0$, but jumps across it. So split by the sign and handle each side. **Range:** any nonzero number.', r'Y\ne0'),
     S(r'**Accumulate**, $y>0$: every negative $X$ works ($\tfrac1X<0<y$). A positive $X$ works when $X\ge\tfrac1y$ (flip: $\tfrac1x$ goes down).',
       r'F_Y(y)=F_X(0)+1-F_X\Big(\frac1y\Big)'),
     S(r'**Accumulate**, $y=0$: only negative $X$ work.', r'F_Y(0)=F_X(0)'),
     S(r'**Accumulate**, $y<0$: only negative $X$ can work, and then $\tfrac1X\le y$ means $\tfrac1y\le X<0$.',
       r'F_Y(y)=F_X(0)-F_X\Big(\frac1y\Big)'),
     S(r'**Differentiate:** both pieces have $-F_X(\tfrac1y)$, and the derivative of $\tfrac1y$ is $-\tfrac{1}{y^2}$.',
       r'f_Y(y)=\frac{1}{y^2}\,f_X\Big(\frac1y\Big),\qquad y\ne0')],
    r'$F_Y(y)=F_X(0)+1-F_X(\tfrac1y)$ for $y>0$, $F_X(0)$ at $y=0$, $F_X(0)-F_X(\tfrac1y)$ for $y<0$; $f_Y(y)=\dfrac{1}{y^2}f_X(\tfrac1y)$.',
    diff='advanced', cites=cite('T6', 1))


def verify():
    import numpy as np
    import sympy as sp
    rng = np.random.default_rng(226)
    N = 400_000
    y, x, lam = sp.symbols('y x lambda', positive=True)

    def mc(samples, F, pts, tol=0.006):
        for p in pts:
            emp = np.mean(samples <= p)
            assert abs(emp - F(p)) < tol, (p, emp, F(p))

    def dens(F, f, a, b, total=1):
        assert sp.simplify(sp.diff(F, y) - f) == 0, (F, f)
        assert abs(float(sp.integrate(f, (y, a, b))) - total) < 1e-9, (f, a, b)

    U = lambda a, b: rng.uniform(a, b, N)
    # type 1
    X = U(-1, 1)
    q = np.where(X < -0.5, -1, np.where(X > 0.5, 1, 0))
    assert abs(np.mean(q == 0) - 0.5) < 0.005 and abs(np.mean(q == 1) - 0.25) < 0.005
    D5 = rng.integers(-2, 3, N) ** 2
    assert abs(np.mean(D5 == 1) - 0.4) < 0.005 and abs(np.mean(D5 == 4) - 0.4) < 0.005
    # type 2
    dens((sp.cbrt(y) + 1) / 2, 1 / (6 * y ** sp.Rational(2, 3)), 0, 1, sp.Rational(1, 2))
    mc(X ** 3, lambda t: (np.cbrt(t) + 1) / 2, [-0.8, -0.1, 0.05, 0.7])
    dens(sp.log(y), 1 / y, 1, sp.E)
    mc(np.exp(U(0, 1)), lambda t: log(t), [1.2, 2.0, 2.6])
    t = sp.Symbol('t', real=True)
    Fln, fln = 1 - sp.exp(-sp.exp(t)), sp.exp(t) * sp.exp(-sp.exp(t))
    assert sp.simplify(sp.diff(Fln, t) - fln) == 0 and sp.integrate(fln, (t, -sp.oo, sp.oo)) == 1
    mc(np.log(rng.exponential(1, N)), lambda s: 1 - exp(-exp(s)), [-2, 0, 1])
    # type 3
    dens(sp.sqrt(y), 1 / (2 * sp.sqrt(y)), 0, 1)
    mc(X ** 2, lambda s: sqrt(s), [0.04, 0.36, 0.81])
    mc(np.abs(X), lambda s: s, [0.2, 0.5, 0.9])
    assert abs(np.mean(np.abs(X) > 0.5) - 0.5) < 0.005
    dens(sp.sqrt(y) / 2, 1 / (4 * sp.sqrt(y)), 0, 4)
    mc(U(0, 2) ** 2, lambda s: sqrt(s) / 2, [0.5, 2, 3.5])
    assert sp.integrate(y / (4 * sp.sqrt(y)), (y, 0, 4)) == sp.Rational(4, 3) == sp.integrate(x ** 2 / 2, (x, 0, 2))
    # type 4
    mc(np.maximum(X, 0), lambda t: 0 if t < 0 else min((t + 1) / 2, 1), [-0.1, 0, 0.3, 0.9])
    assert abs(np.mean(np.maximum(X, 0) == 0) - 0.5) < 0.005
    # practice: what type
    pX = {0: 0.4, 1: 0.3, 2: 0.2, 3: 0.1}
    pZ = {}
    for k, v in pX.items():
        pZ[(k - 1) ** 2] = pZ.get((k - 1) ** 2, 0) + v
    assert {k: round(v, 10) for k, v in pZ.items()} == {1: 0.6, 0: 0.3, 4: 0.1}
    # practice: aX+b with a<0
    mc(-3 * U(0, 1) + 2, lambda s: min(max((s + 1) / 3, 0), 1), [-0.5, 0.5, 1.5])
    # practice: decreasing
    L = 1.5
    E = rng.exponential(1 / L, N)
    mc(-2 * E + 3, lambda s: exp(-L * (3 - s) / 2) if s <= 3 else 1, [-1, 1, 2.8])
    assert sp.simplify(sp.diff(sp.exp(-lam * (3 - t) / 2), t) - lam / 2 * sp.exp(-lam * (3 - t) / 2)) == 0
    mc(-np.log(U(0, 1)), lambda s: 1 - exp(-s), [0.2, 1, 2.5])
    # practice: Gaussian through a line
    mc(2 * rng.normal(2, 3, N) - 3, lambda s: Phi((s - 1) / 6), [-5, 1, 7])
    mc(2 * rng.standard_normal(N) + 1, lambda s: Phi((s - 1) / 2), [-1, 1, 3])
    assert abs(gl - 0.1587) < 1e-4
    D5b = rng.integers(-2, 3, N) ** 2
    assert abs(np.mean(D5b == 0) - 0.2) < 0.005
    assert abs(g7 - 0.1587) < 1e-4
    # practice: timeout and limiter
    E1 = rng.exponential(1, N)
    mc(np.minimum(E1, 1), lambda s: 1 - exp(-s) if s < 1 else 1, [0.3, 0.99, 1.0])
    assert abs(np.mean(np.minimum(E1, 1) == 1) - exp(-1)) < 0.005
    W = np.clip(U(-2, 2), -1, 1)
    mc(W, lambda s: 0 if s < -1 else ((s + 2) / 4 if s < 1 else 1), [-1.0, -0.5, 0.5, 0.999, 1.0])
    assert abs(np.mean(W == -1) - 0.25) < 0.005 and abs(np.mean(W == 1) - 0.25) < 0.005
    # practice: Cx^2
    C = sp.Symbol('C')
    assert sp.solve(sp.integrate(C * x ** 2, (x, -1, 1)) - 1, C) == [sp.Rational(3, 2)]
    assert sp.integrate(sp.Rational(3, 2) * x ** 2, (x, -y, y)) == y ** 3
    dens(y ** 3, 3 * y ** 2, 0, 1)
    assert sp.integrate(y ** 2 * 3 * y ** 2, (y, 0, 1)) == sp.Rational(3, 5)
    Xc = np.cbrt(rng.uniform(-1, 1, N))  # F_X = (x^3+1)/2  ->  inverse-CDF sample
    mc(np.abs(Xc), lambda s: s ** 3, [0.3, 0.6, 0.9])
    assert abs(9 * np.var(Xc) - 27 / 5) < 0.03
    # practice: cubic picture
    assert abs(x3 ** 3 - 3 * x3 - 3) < 1e-12 and len([r for r in np.roots([1, 0, -3, -3]) if abs(r.imag) < 1e-9]) == 1
    Xu = U(-2, 2)
    g = Xu ** 3 - 3 * Xu
    assert abs(np.mean(g <= 0) - 0.5) < 0.005
    FU = lambda s: min(max((s + 2) / 4, 0), 1)
    mc(g, lambda s: FU(x3) if s == 3 else FU(-x3), [3, -3])
    # practice: Gaussian power
    G = rng.standard_normal(N)
    mc(G ** 2, lambda s: 2 * Phi(sqrt(s)) - 1, [0.2, 1, 3])
    fchi = sp.exp(-y / 2) / sp.sqrt(2 * sp.pi * y)
    Fchi = sp.erf(sp.sqrt(y) / sp.sqrt(2))  # = 2*Phi(sqrt y) - 1
    assert sp.simplify(sp.diff(Fchi, y) - fchi) == 0
    assert abs(2 * 0.8413 - 1 - p1) < 2e-4
    # practice: lopsided uniform: X ~ U(-1,2), Y = X^2
    mc(rng.uniform(-1, 2, N) ** 2, lambda s: 2 * s ** 0.5 / 3 if s <= 1 else (s ** 0.5 + 1) / 3, [0.25, 0.81, 1.44, 3.24])
    # practice: cos X, X ~ U(-pi, pi)
    mc(np.cos(U(-pi, pi)), lambda s: 1 - acos(s) / pi, [-0.9, 0, 0.5, 0.95])
    yy = sp.Symbol('yy')
    assert sp.simplify(sp.diff(1 - sp.acos(yy) / sp.pi, yy) - 1 / (sp.pi * sp.sqrt(1 - yy ** 2))) == 0
    # practice: reciprocal
    Xn = rng.normal(0.5, 1, N)
    with np.errstate(divide='ignore'):
        R = 1 / Xn
    FXn = lambda s: Phi(s - 0.5)
    mc(R, lambda s: FXn(0) + 1 - FXn(1 / s) if s > 0 else (FXn(0) if s == 0 else FXn(0) - FXn(1 / s)), [-2, -0.5, 0, 0.5, 3])
    print('q4 verify ok')


if __name__ == '__main__':
    verify()
    D.save()
