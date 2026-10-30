r"""Test 2 - Question 4: functions of a random variable and their distributions (Lectures 12-15, Tutorial 6).

Layout (REWRITE_PLAN.md, v3): short top -> Topic 1 (what type is Y, discrete Y) -> Topic 2 (continuous Y: the CDF
method, one method for every g) -> Extras (flat pieces / mixed Y, the shortcut formula) -> practice.
Each topic: explanation + formulas first (open), then open worked examples (D.EX), one per kind of question.
Step words: Spot, Range, Rewrite, Accumulate, Differentiate, Jump.
"""
from math import erf, exp, log, sqrt

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
D.CO('tip', r'''**Question 4 is always: you know $X$, find the distribution of $Y=g(X)$.** Spot the type of $Y$, then run the steps:

1. **Discrete $Y$** ($X$ discrete, or $g$ a staircase): list where each $x$ goes, **add** the chances that land on the same $y$.
2. **Continuous $Y$:** Range → Rewrite $g(X)\le y$ as a statement about $X$ → Accumulate with $F_X$ → Differentiate.
   - only up: $F_X(g^{-1}(y))$ · only down: $1-F_X(g^{-1}(y))$ · turns around: an interval of $x$.''')
D.P('Test-style, easy → medium, same level as the practice sets. Solve on paper first, then open the solution.')

# ---- Discrete Y
D.Q('Discrete $Y$ · push the PMF through $g$ · Lecture 13 Examples 1–2',
    r'$X$ = number of failed packet sends, with $P(X=0,1,2,3)=0.4,\ 0.3,\ 0.2,\ 0.1$. '
    r'(a) Find the PMF of $Y=2X+1$. (b) Find the PMF of $Z=(X-1)^2$.',
    [S(r'**Spot:** $X$ discrete → $Y$ discrete. (a) Each $x$ gives a different $y$, so the chances just move.', r'(0,1,2,3)\ \longrightarrow\ (1,3,5,7)'),
     S(r'So:', r'p_Y(1)=0.4,\ \ p_Y(3)=0.3,\ \ p_Y(5)=0.2,\ \ p_Y(7)=0.1'),
     S(r'(b) **List** where each $x$ goes.', r'(0,1,2,3)\ \longrightarrow\ (1,0,1,4)'),
     S(r'$x=0$ and $x=2$ both give $Z=1$: **add** them.', r'p_Z(0)=0.3,\quad p_Z(1)=0.4+0.2=0.6,\quad p_Z(4)=0.1'),
     S(r'**Check:** they add to 1.', r'0.3+0.6+0.1=1')],
    r'(a) $0.4,0.3,0.2,0.1$ at $1,3,5,7$ (b) $0.3,0.6,0.1$ at $0,1,4$',
    diff='introductory', cites=cite('L13', 5))

D.Q('Discrete $Y$ · a die through $|x-3|$',
    r'$X$ is a fair die. Find the PMF of $Y=|X-3|$, then $P(Y\le1)$.',
    [S(r'**Spot:** $X$ discrete → $Y$ discrete. Each face has chance $\tfrac16$.'),
     S(r'**List** where each $x$ goes.', r'(1,2,3,4,5,6)\ \longrightarrow\ (2,1,0,1,2,3)'),
     S(r'**Add** the chances that land on the same $y$.', r'p_Y(0)=\frac16,\quad p_Y(1)=\frac26,\quad p_Y(2)=\frac26,\quad p_Y(3)=\frac16'),
     S(r'**Check:** they add to 1. Then add $y=0,1$.', r'P(Y\le1)=\frac16+\frac26=\frac12')],
    r'$p_Y=\tfrac16,\tfrac13,\tfrac13,\tfrac16$ at $0,1,2,3$; $P(Y\le1)=\tfrac12$', diff='introductory')

e2 = exp(-2)
D.Q('Discrete $Y$ · a staircase $g$ (a quantizer) · like Lecture 13',
    r'(a) $X\sim U(0,4)$. $Y=0$ if $X<1$, $Y=1$ if $1\le X<3$, $Y=2$ if $X\ge3$. Find the PMF of $Y$. '
    r'(b) A part’s lifetime is $X\sim$ Exp$(1)$. $B=1$ if it lasts more than 2 years, else $B=0$. Find the PMF of $B$.',
    [S(r'(a) **Spot:** $X$ is continuous, but $g$ is a staircase with 3 outputs. So $Y$ is **discrete**.', r'Y\in\{0,1,2\}'),
     S(r'Each value of $Y$ gets the chance of its $x$-interval: length × height $\tfrac14$.',
       r'P(Y=0)=\frac14,\qquad P(Y=1)=\frac24=\frac12,\qquad P(Y=2)=\frac14'),
     S(r'(b) **Spot:** two outputs → discrete (a 0/1 variable). Use the exponential tail.',
       (r'P(B=1)=P(X>2)=e^{-2}\approx' + f'{e2:.4f}', r'P(B=0)=1-e^{-2}\approx' + f'{1 - e2:.4f}'))],
    f'(a) $\\tfrac14,\\tfrac12,\\tfrac14$ at $0,1,2$ (b) $P(B=1)=e^{{-2}}\\approx {e2:.4f}$, $P(B=0)\\approx {1 - e2:.4f}$',
    diff='introductory', cites=cite('L13', 6))

# ---- Continuous Y
D.Q('Continuous $Y$, goes up · $e^X$ · Tutorial 6 Q3',
    r'$X\sim U(0,1)$. Find the CDF and PDF of $Y=e^X$.',
    [S(r'**Spot:** $e^x$ only goes up → $F_Y(y)=F_X(g^{-1}(y))$.'),
     S(r'**Range:** $e^0=1$ to $e^1=e$.', r'1\le Y\le e'),
     S(r'**Rewrite:** undo the $e$.', r'e^X\le y\quad\Longleftrightarrow\quad X\le\ln y'),
     S(r'**Accumulate:** $F_X(x)=x$ on $[0,1]$.', r'F_Y(y)=\ln y,\qquad 1\le y\le e'),
     S(r'**Differentiate.**', r'f_Y(y)=\frac1y,\qquad 1<y<e')],
    r'$F_Y=\ln y$ on $[1,e]$ ($0$ below, $1$ above); $f_Y(y)=\dfrac1y$ for $1<y<e$.', diff='introductory', cites=cite('T6', 1))

D.Q('Continuous $Y$ · a line, up and down · Lecture 15',
    r'$X\sim U(0,2)$. Find the CDF and PDF of (a) $Y=3X+1$, (b) $W=4-2X$. What distributions are they?',
    [S(r'(a) **Spot:** slope $3>0$, only goes up. **Range:** $x=0\to1$, $x=2\to7$.', r'1\le Y\le7'),
     S(r'**Rewrite.**', r'3X+1\le y\quad\Longleftrightarrow\quad X\le\frac{y-1}{3}'),
     S(r'**Accumulate:** $F_X(x)=\tfrac x2$.', r'F_Y(y)=\frac{y-1}{6},\qquad 1\le y\le7'),
     S(r'**Differentiate.**', r'f_Y(y)=\frac16\ \text{ on }(1,7)\quad\Rightarrow\quad Y\sim U(1,7)'),
     S(r'(b) **Spot:** slope $-2<0$, only goes down: the $\le$ flips. **Range:** $x=0\to4$, $x=2\to0$.', r'0\le W\le4'),
     S(r'**Rewrite:** subtract 4, divide by $-2$ (flip).', r'4-2X\le w\quad\Longleftrightarrow\quad X\ge\frac{4-w}{2}'),
     S(r'**Accumulate:** $P(X\ge t)=1-\tfrac t2$.', r'F_W(w)=1-\frac{4-w}{4}=\frac w4,\qquad 0\le w\le4'),
     S(r'**Differentiate.**', r'f_W(w)=\frac14\ \text{ on }(0,4)\quad\Rightarrow\quad W\sim U(0,4)')],
    r'(a) $F_Y=\tfrac{y-1}{6}$, $Y\sim U(1,7)$ (b) $F_W=\tfrac w4$, $W\sim U(0,4)$', diff='introductory', cites=cite('L15', 2))

D.Q('Continuous $Y$, goes down · decreasing $g$',
    r'(a) $X\sim$ Exp$(\lambda)$. Find the CDF and PDF of $Y=-2X+3$. (b) $X\sim U(0,1)$. Find the CDF and PDF of $Y=-\ln X$.',
    [S(r'(a) **Spot:** slope $-2$, only goes down → the $\le$ flips. **Range:** $X\ge0$, so $Y=3-2X\le3$.', r'Y\le3'),
     S(r'**Rewrite:** subtract 3, divide by $-2$ (flip).', r'-2X+3\le y\quad\Longleftrightarrow\quad X\ge\frac{3-y}{2}'),
     S(r'**Accumulate:** the exponential tail, $P(X\ge x)=e^{-\lambda x}$.', r'F_Y(y)=e^{-\lambda(3-y)/2},\qquad y\le3'),
     S(r'**Differentiate** (chain rule: the inside has slope $\tfrac\lambda2$).', r'f_Y(y)=\frac{\lambda}{2}\,e^{-\lambda(3-y)/2},\qquad y<3'),
     S(r'(b) **Spot:** $-\ln x$ only goes down → the $\le$ flips. **Range:** $X\in(0,1)$, so $-\ln X\in(0,\infty)$.', r'Y>0'),
     S(r'**Rewrite:** multiply by $-1$ (flip), then undo the $\ln$.', r'-\ln X\le y\quad\Longleftrightarrow\quad X\ge e^{-y}'),
     S(r'**Accumulate:** $P(X\ge t)=1-t$.', r'F_Y(y)=1-e^{-y},\qquad y\ge0'),
     S(r'**Differentiate.** That’s the Exp$(1)$ PDF.', r'f_Y(y)=e^{-y},\qquad y>0')],
    r'(a) $F_Y=e^{-\lambda(3-y)/2}$ for $y\le3$, $f_Y=\tfrac\lambda2e^{-\lambda(3-y)/2}$ (b) $F_Y=1-e^{-y}$, $f_Y=e^{-y}$: $Y\sim$ Exp$(1)$.')

D.Q('Continuous $Y$, goes down · $1/X$ · like Tutorial 6 Q1',
    r'$X\sim U(1,2)$. Find the CDF and PDF of $Y=\dfrac1X$.',
    [S(r'**Spot:** $X$ is positive and $\tfrac1x$ only goes down there → the $\le$ flips.'),
     S(r'**Range:** $x=1\to1$, $x=2\to\tfrac12$.', r'\frac12\le Y\le1'),
     S(r'**Rewrite:** both sides are positive, so turn both upside down. That flips the $\le$.', r'\frac1X\le y\quad\Longleftrightarrow\quad X\ge\frac1y'),
     S(r'**Accumulate:** $F_X(x)=x-1$ on $[1,2]$, so $P(X\ge t)=1-(t-1)=2-t$.', r'F_Y(y)=2-\frac1y,\qquad \frac12\le y\le1'),
     S(r'**Check** the ends: $F_Y(\tfrac12)=0$, $F_Y(1)=1$ ✓. **Differentiate.**', r'f_Y(y)=\frac1{y^2},\qquad \frac12<y<1')],
    r'$F_Y=2-\tfrac1y$ on $[\tfrac12,1]$; $f_Y=\dfrac1{y^2}$ on $(\tfrac12,1)$', cites=cite('T6', 1))

D.Q('Continuous $Y$, goes up · powers of a positive $X$',
    r'(a) $X\sim U(0,3)$. Find the CDF and PDF of $Y=X^2$. (b) $X\sim$ Exp$(\lambda)$. Find the CDF and PDF of $Y=\sqrt X$.',
    [S(r'(a) **Spot:** $X\ge0$, and $x^2$ only goes up for $x\ge0$. So no interval needed. **Range:**', r'0\le Y\le9'),
     S(r'**Rewrite:** take the root; $X$ can’t be negative.', r'X^2\le y\quad\Longleftrightarrow\quad X\le\sqrt y'),
     S(r'**Accumulate:** $F_X(x)=\tfrac x3$.', r'F_Y(y)=\frac{\sqrt y}{3},\qquad 0\le y\le9'),
     S(r'**Differentiate.**', r'f_Y(y)=\frac{1}{6\sqrt y},\qquad 0<y<9'),
     S(r'(b) **Spot:** $\sqrt x$ only goes up. **Range:** $Y\ge0$. **Rewrite:** square both sides.', r'\sqrt X\le y\quad\Longleftrightarrow\quad X\le y^2'),
     S(r'**Accumulate:** $F_X(x)=1-e^{-\lambda x}$.', r'F_Y(y)=1-e^{-\lambda y^2},\qquad y\ge0'),
     S(r'**Differentiate** (chain rule: the inside $-\lambda y^2$ has slope $-2\lambda y$).', r'f_Y(y)=2\lambda y\,e^{-\lambda y^2},\qquad y>0')],
    r'(a) $F_Y=\tfrac{\sqrt y}{3}$ on $[0,9]$, $f_Y=\tfrac1{6\sqrt y}$ (b) $F_Y=1-e^{-\lambda y^2}$, $f_Y=2\lambda y\,e^{-\lambda y^2}$ for $y>0$')

D.Q('Continuous $Y$, turns around · $X^2$ and $|X|$ · Lecture 15, Tutorial 6 Q4',
    r'$X\sim U(-2,2)$. Find the CDF and PDF of (a) $Y=X^2$, (b) $W=|X|$. (c) Find $P(X^2>1)$.',
    [S(r'(a) **Spot:** $x^2$ turns around at $0$ → an interval. **Range:** $X\in[-2,2]$, so $X^2\in[0,4]$.', r'0\le Y\le4'),
     S(r'**Rewrite.**', r'X^2\le y\quad\Longleftrightarrow\quad -\sqrt y\le X\le\sqrt y'),
     S(r'**Accumulate:** length $2\sqrt y$, height $\tfrac14$.', r'F_Y(y)=2\sqrt y\cdot\frac14=\frac{\sqrt y}{2},\qquad 0\le y\le4'),
     S(r'**Differentiate.**', r'f_Y(y)=\frac{1}{4\sqrt y},\qquad 0<y<4'),
     S(r'(b) **Spot:** $|x|$ turns around → an interval. **Range:** $0\le W\le2$. **Rewrite.**', r'|X|\le w\quad\Longleftrightarrow\quad -w\le X\le w'),
     S(r'**Accumulate:** length $2w$, height $\tfrac14$. **Differentiate.**', r'F_W(w)=\frac w2,\qquad f_W(w)=\frac12\ \text{ on }(0,2)\quad\Rightarrow\quad W\sim U(0,2)'),
     S(r'(c) One minus the CDF of $Y$.', r'P(X^2>1)=1-F_Y(1)=1-\frac12=\frac12')],
    r'(a) $F_Y=\tfrac{\sqrt y}2$ on $[0,4]$, $f_Y=\tfrac1{4\sqrt y}$ (b) $F_W=\tfrac w2$, $W\sim U(0,2)$ (c) $\tfrac12$', cites=cite('L15', 3) + cite('T6', 1))

D.Q('Continuous $Y$, turns around · $|X|$ of a $Cx^2$ variable · Tutorial 5 Q5',
    r'$f_X(x)=Cx^2$ for $|x|\le1$, $0$ otherwise. (a) Find $C$. (b) Find the CDF and PDF of $Y=|X|$.',
    [S(r'(a) **Find $c$:** total area $=1$.', r'\int_{-1}^{1}Cx^2\,dx=\frac{2C}{3}=1\quad\Rightarrow\quad C=\frac32'),
     S(r'(b) **Spot:** $|x|$ turns around at $0$ → an interval. **Range:**', r'0\le Y\le1'),
     S(r'**Rewrite.**', r'|X|\le y\quad\Longleftrightarrow\quad -y\le X\le y'),
     S(r'**Accumulate:** the PDF isn’t flat, so integrate it over the interval.', r'F_Y(y)=\int_{-y}^{y}\frac32x^2\,dx=\frac{x^3}{2}\Big|_{-y}^{y}=y^3,\qquad 0\le y\le1'),
     S(r'**Differentiate.**', r'f_Y(y)=3y^2,\qquad 0<y<1')],
    r'(a) $C=\tfrac32$ (b) $F_Y=y^3$ on $[0,1]$, $f_Y(y)=3y^2$ on $(0,1)$', cites=cite('T5', 1))


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
    # practice: discrete Y
    pX = {0: 0.4, 1: 0.3, 2: 0.2, 3: 0.1}
    pZ = {}
    for k, v in pX.items():
        pZ[(k - 1) ** 2] = pZ.get((k - 1) ** 2, 0) + v
    assert {k: round(v, 10) for k, v in pZ.items()} == {1: 0.6, 0: 0.3, 4: 0.1}
    die = np.abs(rng.integers(1, 7, N) - 3)
    assert all(abs(np.mean(die == k) - w) < 0.005 for k, w in [(0, 1 / 6), (1, 1 / 3), (2, 1 / 3), (3, 1 / 6)])
    Q = U(0, 4)
    q3 = np.where(Q < 1, 0, np.where(Q < 3, 1, 2))
    assert abs(np.mean(q3 == 1) - 0.5) < 0.005 and abs(np.mean(q3 == 2) - 0.25) < 0.005
    assert abs(np.mean(rng.exponential(1, N) > 2) - exp(-2)) < 0.005
    # practice: lines up and down, X ~ U(0,2)
    X2 = U(0, 2)
    mc(3 * X2 + 1, lambda s: (s - 1) / 6, [2, 4, 6.5])
    mc(4 - 2 * X2, lambda s: s / 4, [0.5, 2, 3.5])
    # practice: decreasing
    L = 1.5
    E = rng.exponential(1 / L, N)
    mc(-2 * E + 3, lambda s: exp(-L * (3 - s) / 2) if s <= 3 else 1, [-1, 1, 2.8])
    assert sp.simplify(sp.diff(sp.exp(-lam * (3 - t) / 2), t) - lam / 2 * sp.exp(-lam * (3 - t) / 2)) == 0
    mc(-np.log(U(0, 1)), lambda s: 1 - exp(-s), [0.2, 1, 2.5])
    # practice: 1/X, X ~ U(1,2)
    dens(2 - 1 / y, 1 / y ** 2, sp.Rational(1, 2), 1)
    mc(1 / U(1, 2), lambda s: 2 - 1 / s, [0.55, 0.7, 0.9])
    # practice: powers of a positive X
    dens(sp.sqrt(y) / 3, 1 / (6 * sp.sqrt(y)), 0, 9)
    mc(U(0, 3) ** 2, lambda s: sqrt(s) / 3, [0.5, 4, 8])
    dens(1 - sp.exp(-lam * y ** 2), 2 * lam * y * sp.exp(-lam * y ** 2), 0, sp.oo)
    mc(np.sqrt(rng.exponential(1 / L, N)), lambda s: 1 - exp(-L * s * s), [0.3, 0.8, 1.5])
    # practice: X ~ U(-2,2), X^2 and |X|
    X4 = U(-2, 2)
    dens(sp.sqrt(y) / 2, 1 / (4 * sp.sqrt(y)), 0, 4)
    mc(X4 ** 2, lambda s: sqrt(s) / 2, [0.25, 1, 3])
    mc(np.abs(X4), lambda s: s / 2, [0.3, 1, 1.7])
    assert abs(np.mean(X4 ** 2 > 1) - 0.5) < 0.005
    # practice: Cx^2
    C = sp.Symbol('C')
    assert sp.solve(sp.integrate(C * x ** 2, (x, -1, 1)) - 1, C) == [sp.Rational(3, 2)]
    assert sp.integrate(sp.Rational(3, 2) * x ** 2, (x, -y, y)) == y ** 3
    dens(y ** 3, 3 * y ** 2, 0, 1)
    Xc = np.cbrt(rng.uniform(-1, 1, N))  # F_X = (x^3+1)/2  ->  inverse-CDF sample
    mc(np.abs(Xc), lambda s: s ** 3, [0.3, 0.6, 0.9])
    assert abs(gl - 0.1587) < 1e-4
    mc(-3 * U(0, 1) + 2, lambda s: min(max((s + 1) / 3, 0), 1), [-0.5, 0.5, 1.5])  # Topic 2 example
    mc(2 * rng.standard_normal(N) + 1, lambda s: Phi((s - 1) / 2), [-1, 1, 3])
    print('q4 verify ok')


if __name__ == '__main__':
    verify()
    D.save()
