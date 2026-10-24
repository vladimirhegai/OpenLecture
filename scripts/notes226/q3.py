r"""Test 2 - Question 3: expected values, variances, properties of expectation and variance (Lectures 11-13)."""
from fractions import Fraction as Fr
from math import pi, sqrt

from lib226 import Doc, S, cite, num

D = Doc('q3', 'Test 2 - Question 3', ['expected_value', 'variance', 'standard_deviation', 'linearity', 'moments'])


def stepper(title, rows):
    """An equation stepper with each $$ on its own line (the multi-line form of the ```steps grammar)."""
    out = ['```steps', f'title "{title}"']
    for latex, note in rows:
        out += ['$$', latex, '$$', note]
    D.P('\n'.join(out + ['```']))

D.P('**Lectures 11–13.** Expected values, variances, and the properties of expectation and variance.',
    cites=cite('L11', 6) + cite('L12', 6) + cite('L13', 2))

# =====================================================================================================
D.H('Topic 1: Expected value')
D.P('The **expected value** (mean) $E[X]=\\mu_X$ is the **long-run average** of $X$ if you repeat the experiment many times.')
D.P('Each value is weighted by how likely it is: a **probability-weighted average**.')
D.EQ(r'E[X]=\sum_{x\in R_X} x\,p_X(x)\quad\text{(discrete)}', cites=cite('L11', 7))
D.EQ(r'E[X]=\int_{-\infty}^{\infty} x\,f_X(x)\,dx\quad\text{(continuous)}', cites=cite('L11', 7))
D.L([r'**Why it works:** repeat $N$ times; value $x_k$ shows up about $N p_k$ times, so the average is $\approx\sum x_k p_k$.',
     r'**Continuous:** the sum becomes an integral, with $p_k$ replaced by $f_X(x)\,dx$.',
     r'$E[X]$ **need not be a possible value**: a die averages $3.5$.',
     r'**Mixed** $X$ (a point mass plus a density): add the two parts, $\sum x\,P(X=x)+\int x\,f(x)\,dx$.'],
    cites=cite('L11', 6))
D.P('**Expected value of a function** $g(X)$: no need to find the distribution of $Y=g(X)$ first. Just weight $g(x)$ instead of $x$:')
D.EQ(r'E[g(X)]=\sum_{x} g(x)\,p_X(x)\qquad E[g(X)]=\int_{-\infty}^{\infty} g(x)\,f_X(x)\,dx', cites=cite('L12', 2))
D.CO('warning', r'**$E[X^2]\ne(E[X])^2$** in general. Square inside the sum/integral, not after.', cites=cite('L12', 2))
D.REMIND(r'''**Calculus you need for $E[X]$**

- **Power rule:** $\displaystyle\int x^n\,dx=\frac{x^{n+1}}{n+1}$.
- **Exponential:** $\displaystyle\int e^{-\lambda x}\,dx=-\frac{1}{\lambda}e^{-\lambda x}$.
- **By parts:** $\displaystyle\int u\,dv=uv-\int v\,du$. For $\int x\,e^{-\lambda x}dx$ take $u=x$, $dv=e^{-\lambda x}dx$.
- **Shortcut (memorise):** $\displaystyle\int_0^{\infty}x^n e^{-\lambda x}\,dx=\frac{n!}{\lambda^{n+1}}$.
- **Symmetry:** an **odd** function ($g(-x)=-g(x)$, like $x$, $x^3$) on $[-a,a]$ integrates to $0$.''')
D.P('**Method:**')
D.L(['**Write** the PMF/PDF and where it is nonzero.',
     '**Multiply** by $x$ (or by $g(x)$).',
     '**Add/integrate** only over the nonzero range (outside it the integrand is $0$).'], ordered=True)
D.EX('A die and a uniform',
     r'(a) A fair die is rolled; $X$ = the number. Find $E[X]$ and $E[X^2]$. '
     r'(b) $X$ is uniform on $[0,2]$: $f_X(x)=\tfrac12$ on $[0,2]$. Find $E[X]$.',
     [S('(a) **Weight** each face by $\\tfrac16$.', r'E[X]=\tfrac16(1+2+3+4+5+6)=\tfrac{21}{6}=3.5'),
      S('$E[X^2]$: square **inside** the sum.', r'E[X^2]=\tfrac16(1+4+9+16+25+36)=\tfrac{91}{6}\approx15.17'),
      S('Compare: $(E[X])^2=12.25\\ne15.17$.', r'E[X^2]\ne(E[X])^2'),
      S('(b) **Integrate** over $[0,2]$ only.', r'E[X]=\int_0^2 x\cdot\tfrac12\,dx=\tfrac12\left[\tfrac{x^2}{2}\right]_0^2=1')],
     r'(a) $E[X]=3.5$, $E[X^2]=\tfrac{91}{6}$ (b) $E[X]=1$, the middle of $[0,2]$.', cites=cite('L11', 8) + cite('L12', 2))
D.GRAPH(['title "Exponential PDF: the mean $1/\\lambda$ is not the peak"', 'x 0 6 label="$x$" height=240', 'y 0 2.1 label="$f_X(x)$"',
         'slider L 0.3 2 1 step=0.05 label="$\\lambda$"',
         'curve "L*exp(-L*x)" from=0 to=6 label="$\\lambda e^{-\\lambda x}$"',
         'vline "1/L" label="$E[X]=1/\\lambda$" color=2',
         'readout "$E[X]=1/\\lambda$" "1/L"'],
        intro='The mean is the **balance point** of the PDF. A long right tail pulls it to the right of the peak.')
D.TRY('Second moment of a uniform',
      r'$X$ is uniform on $[0,2]$. Find $E[X^2]$.',
      [S('**Use** $E[g(X)]=\\int g(x)f_X(x)\\,dx$ with $g(x)=x^2$.', r'E[X^2]=\int_0^2 x^2\cdot\tfrac12\,dx'),
       S('**Power rule.**', r'=\tfrac12\left[\tfrac{x^3}{3}\right]_0^2=\tfrac12\cdot\tfrac83=\tfrac43')],
      r'$E[X^2]=\tfrac43$ (not $(E[X])^2=1$).', diff='introductory', cites=cite('L12', 3))
D.TRY('Mean time between customers',
      r'The time $X$ between customer arrivals is exponential: $f_X(t)=\lambda e^{-\lambda t}$ for $t\ge0$. Find the mean $E[X]$.',
      [S('**Set up** over $[0,\\infty)$.', r'E[X]=\int_0^{\infty}t\,\lambda e^{-\lambda t}\,dt'),
       S('**By parts:** $u=t$, $dv=\\lambda e^{-\\lambda t}dt$, so $du=dt$, $v=-e^{-\\lambda t}$.',
         r'=\Big[-t\,e^{-\lambda t}\Big]_0^{\infty}+\int_0^{\infty}e^{-\lambda t}\,dt'),
       S('The boundary term is $0$ (exponential beats $t$).', r'=0+\Big[-\tfrac1\lambda e^{-\lambda t}\Big]_0^{\infty}=\tfrac1\lambda')],
      r'$E[X]=\dfrac1\lambda$. (Rate 3 per minute → mean gap $\tfrac13$ min.)', cites=cite('P3', 1))
D.TRY('Mean of a symmetric PDF',
      r'$X$ has PDF $f_X(t)=\tfrac{\lambda}{2}e^{-\lambda|t-\gamma|}$ for all $t$ (a Laplace density centred at $\gamma$). Find $E[X]$.',
      [S('**Shift:** let $u=t-\\gamma$, so $t=u+\\gamma$.', r'E[X]=\int_{-\infty}^{\infty}(u+\gamma)\,\tfrac{\lambda}{2}e^{-\lambda|u|}\,du'),
       S('**Split.** $u\\,e^{-\\lambda|u|}$ is **odd**, so its integral is $0$; the rest is $\\gamma$ times the total area $1$.',
         r'=\underbrace{\int u\,\tfrac{\lambda}{2}e^{-\lambda|u|}du}_{0}+\gamma\underbrace{\int\tfrac{\lambda}{2}e^{-\lambda|u|}du}_{1}'),
       S('So the mean is the centre of symmetry.', r'E[X]=\gamma')],
      r'$E[X]=\gamma$: a PDF symmetric about $c$ has mean $c$.', cites=cite('P3', 1))
D.TRY('Mean of a mixed random variable',
      r'A received signal level $X$ is $0$ with probability $0.2$ (signal lost). Otherwise (probability $0.8$) it is uniform on $(0,10)$, '
      r'so the continuous part has density $0.8\cdot\tfrac1{10}=0.08$ on $(0,10)$. Find $E[X]$.',
      [S('**Discrete part:** the point mass at $0$.', r'0\cdot P(X=0)=0\cdot0.2=0'),
       S('**Continuous part:** integrate $x$ times the density $0.08$.', r'\int_0^{10}x\,(0.08)\,dx=0.08\cdot\tfrac{10^2}{2}=4'),
       S('**Add** the parts.', r'E[X]=0+4=4')],
      r'$E[X]=4$ (the 20% of zeros pull the average down from 5).', cites=cite('L10', 8))

# =====================================================================================================
D.H('Topic 2: Variance and standard deviation')
D.P('The mean gives the **centre**. Two variables can share a centre but spread very differently:')
D.L([r'$X=9$ or $11$ (each $\tfrac12$): $E[X]=10$, stays close.',
     r'$Y=0$ or $20$ (each $\tfrac12$): $E[Y]=10$, far more spread out.',
     r'The average deviation $E[X-\mu_X]$ is always $0$ (the $+$ and $-$ cancel), so we **square** the deviation.'],
    cites=cite('L12', 5))
D.EQ(r'\operatorname{Var}(X)=E\big[(X-\mu_X)^2\big]', cites=cite('L12', 6))
D.P('**Shortcut** (almost always faster):')
D.EQ(r'\operatorname{Var}(X)=E[X^2]-\big(E[X]\big)^2', cites=cite('L12', 6))
stepper('Where the shortcut comes from',
        [(r'E\big[(X-\mu)^2\big]', 'Start from the definition, with $\\mu=E[X]$ a constant.'),
         (r'E\big[\hl{X^2-2\mu X+\mu^2}\big]', 'Expand the square.'),
         (r'\hl{E[X^2]-2\mu\,E[X]+\mu^2}', 'Linearity: constants come out of $E$.'),
         (r'E[X^2]-2\mu\cdot\hl{\mu}+\mu^2', 'Use $E[X]=\\mu$.'),
         (r'\hl{E[X^2]-\mu^2}', 'Done: mean of the square minus square of the mean.')])
D.L([r'**Units:** variance has **squared** units (V → V²).',
     r'**Standard deviation** $\sigma_X=\sqrt{\operatorname{Var}(X)}$ is back in the units of $X$: a typical distance from the mean.',
     r'$\operatorname{Var}(X)\ge0$, and $=0$ only when $X$ is a constant.',
     r'For a Gaussian $N(\mu,\sigma^2)$: mean $\mu$, standard deviation $\sigma$ (the width of the bell).'],
    cites=cite('L12', 8))
lines = ['title "Same mean, different spread: $X=10\\pm d$, each with probability $\\tfrac12$"',
         'x -1 21 label="$x$" height=220', 'y 0 0.65 label="$p_X(x)$"',
         'slider d 0 10 1 step=0.5 label="$d$"',
         'segment "10-d" "0" "10-d" "0.5" color=1', 'point "10-d" "0.5" color=1',
         'segment "10+d" "0" "10+d" "0.5" color=1', 'point "10+d" "0.5" color=1',
         'vline "10" label="$E[X]=10$" color=2',
         'readout "$E[X]$" "10"', 'readout "$\\mathrm{Var}(X)=d^2$" "d^2"', 'readout "$\\sigma_X=d$" "d"']
D.GRAPH(lines, intro='Drag $d$: the mean never moves, but the variance grows like $d^2$. ($d=1$ is $X$ above, $d=10$ is $Y$.)')
D.P('**Method:**')
D.L(['**Find** $E[X]$.', '**Find** $E[X^2]$ (square inside the sum/integral).', '**Subtract:** $\\operatorname{Var}=E[X^2]-(E[X])^2$; then $\\sigma=\\sqrt{\\operatorname{Var}}$.'],
    ordered=True)
D.EX('A two-level sensor voltage',
     r'A sensor reads $X=4\text{ V}$ or $X=6\text{ V}$, each with probability $0.5$. Find $E[X]$, $E[X^2]$, $\operatorname{Var}(X)$ and $\sigma_X$.',
     [S('**Mean.**', r'E[X]=4(0.5)+6(0.5)=5\text{ V}'),
      S('**Second moment.**', r'E[X^2]=16(0.5)+36(0.5)=26\text{ V}^2'),
      S('**Subtract.**', r'\operatorname{Var}(X)=26-5^2=1\text{ V}^2'),
      S('**Standard deviation** (back to volts).', r'\sigma_X=\sqrt1=1\text{ V}')],
     r'$E[X]=5$ V, $E[X^2]=26$ V², $\operatorname{Var}(X)=1$ V², $\sigma_X=1$ V.', cites=cite('L12', 7))
D.TRY('A binary random variable',
      r'$X$ takes only the values $0$ and $1$, with $P(X=0)=p$ and $P(X=1)=1-p$. Find $E[X]$, $\operatorname{Var}(X)$ and $E[X^5]$.',
      [S('**Mean.**', r'E[X]=0\cdot p+1\cdot(1-p)=1-p'),
       S('**Trick:** $0^n=0$ and $1^n=1$, so $X^n=X$ for every $n\\ge1$.', r'E[X^2]=E[X^5]=E[X]=1-p'),
       S('**Subtract.**', r'\operatorname{Var}(X)=(1-p)-(1-p)^2=(1-p)\,p')],
      r'$E[X]=1-p$, $\operatorname{Var}(X)=p(1-p)$, $E[X^5]=1-p$.', diff='introductory', cites=cite('T5', 1))
e9 = Fr(-3) * Fr(3, 8) + 0 * Fr(3, 8) + 6 * Fr(1, 4)
e9s = 9 * Fr(3, 8) + 0 + 36 * Fr(1, 4)
v9 = e9s - e9 ** 2
assert (e9, e9s, v9) == (Fr(3, 8), Fr(99, 8), Fr(783, 64))
D.TRY('Variance from a staircase CDF',
      r'''$X$ has CDF

$$
F_X(x)=\begin{cases}0,&x<-3\\ 3/8,&-3\le x<0\\ 3/4,&0\le x<6\\ 1,&x\ge6\end{cases}
$$

Is $X$ discrete or continuous? Find $\operatorname{Var}(X)$ and $\sigma_X$.''',
      [S('**Staircase** → discrete. The **jumps** give the PMF.', r'p_X(-3)=\tfrac38,\quad p_X(0)=\tfrac38,\quad p_X(6)=\tfrac14'),
       S('**Mean.**', r'E[X]=-3\cdot\tfrac38+0+6\cdot\tfrac14=-\tfrac98+\tfrac{12}{8}=\tfrac38'),
       S('**Second moment.**', r'E[X^2]=9\cdot\tfrac38+0+36\cdot\tfrac14=\tfrac{27}{8}+\tfrac{72}{8}=\tfrac{99}{8}'),
       S('**Subtract**, then take the root.', r'\operatorname{Var}(X)=\tfrac{99}{8}-\tfrac{9}{64}=\tfrac{783}{64}\approx' + f'{float(v9):.3f}' + r',\quad \sigma_X\approx' + f'{sqrt(v9):.3f}')],
      r'Discrete; $\operatorname{Var}(X)=\tfrac{783}{64}\approx' + f'{float(v9):.3f}' + r'$, $\sigma_X\approx' + f'{sqrt(v9):.3f}' + '$.',
      cites=cite('P3', 3))
D.TRY('A PDF with a constant: mean and variance',
      r'$f_X(x)=Cx^2$ for $|x|\le1$, and $0$ otherwise. (a) Find $C$ and the CDF. (b) Find $E[X]$ and $\operatorname{Var}(X)$.',
      [S('(a) **Total area = 1.**', r'\int_{-1}^{1}Cx^2\,dx=C\cdot\tfrac23=1\;\Rightarrow\;C=\tfrac32'),
       S('**CDF** on $[-1,1]$: integrate from $-1$.', r'F_X(x)=\int_{-1}^{x}\tfrac32t^2\,dt=\tfrac{x^3+1}{2}\quad(0\text{ left of }-1,\ 1\text{ right of }1)'),
       S('(b) **Mean:** $x\\cdot x^2=x^3$ is odd on $[-1,1]$.', r'E[X]=\int_{-1}^{1}\tfrac32x^3\,dx=0'),
       S('**Second moment.**', r'E[X^2]=\int_{-1}^{1}\tfrac32x^4\,dx=\tfrac32\cdot\tfrac25=\tfrac35'),
       S('**Subtract.**', r'\operatorname{Var}(X)=\tfrac35-0^2=\tfrac35')],
      r'$C=\tfrac32$, $F_X(x)=\tfrac{x^3+1}{2}$ on $[-1,1]$; $E[X]=0$, $\operatorname{Var}(X)=\tfrac35$.', cites=cite('T5', 1))

# =====================================================================================================
D.H('Topic 3: Properties of expectation and variance')
D.P('These rules turn most "find $E$ / Var of something" questions into one line.')
D.EQ(r'E[aX+b]=a\,E[X]+b\qquad E[aX+bY]=a\,E[X]+b\,E[Y]', cites=cite('L12', 5))
D.EQ(r'\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)\qquad \sigma_{aX+b}=|a|\,\sigma_X', cites=cite('L12', 9))
D.L([r'**Shifting** by $b$ moves the centre but **not** the spread: $b$ disappears from Var.',
     r'**Scaling** by $a$ scales the spread by $|a|$, so Var by $a^2$. A minus sign never makes Var negative: $\operatorname{Var}(-X)=\operatorname{Var}(X)$.',
     r'$E[b]=b$ and $\operatorname{Var}(b)=0$ for a constant $b$.',
     r'**Turn the shortcut around:** $E[X^2]=\operatorname{Var}(X)+(E[X])^2$. Use it whenever you are given $E$ and Var.'],
    cites=cite('L13', 2))
stepper('Why $\\operatorname{Var}(aX+b)=a^2\\operatorname{Var}(X)$',
        [(r'\operatorname{Var}(aX+b)=E\big[(aX+b-E[aX+b])^2\big]', 'Definition, with $Y=aX+b$.'),
         (r'=E\big[(aX+b-\hl{aE[X]-b})^2\big]', 'Linearity of $E$.'),
         (r'=E\big[\hl{a^2}(X-E[X])^2\big]', 'The $b$ cancels; pull out $a$ and square it.'),
         (r'=\hl{a^2\operatorname{Var}(X)}', '$a^2$ is a constant, so it comes out of $E$.')])
D.P('**Moments:** $E[X^n]$ is the $n$th (raw) **moment**; $E[(X-\\mu_X)^n]$ is the $n$th **central moment**. '
    'So $E[X]$ = 1st moment, $E[X^2]$ = 2nd moment, and Var = 2nd central moment.', cites=cite('L13', 4))
D.P('**Means and variances to memorise** (no formula sheet). Each can be found with Topics 1–2:')
D.T(['Distribution', '$E[X]$', '$\\operatorname{Var}(X)$', 'Where you saw it'],
    [['Bernoulli$(p)$', '${p}$', '${p(1-p)}$', 'Try it 5 (there $P(X=1)=1-p$)'],
     ['Binomial$(n,p)$', '${np}$', '${np(1-p)}$', 'memorise'],
     ['Geometric, $k=1,2,\\dots$', '${\\dfrac1p}$', '${\\dfrac{1-p}{p^2}}$', 'memorise'],
     ['Geometric, $k=0,1,\\dots$', '${\\dfrac{1-p}{p}}$', '${\\dfrac{1-p}{p^2}}$', 'Practice 03 Q5'],
     ['Poisson$(\\lambda)$', '${\\lambda}$', '${\\lambda}$', 'memorise'],
     ['Uniform$(a,b)$', '${\\dfrac{a+b}{2}}$', '${\\dfrac{(b-a)^2}{12}}$', 'Question 2'],
     ['Exponential$(\\lambda)$', '${\\dfrac1\\lambda}$', '${\\dfrac{1}{\\lambda^2}}$', 'Try it 2, Question 3'],
     ['Gaussian $N(\\mu,\\sigma^2)$', '${\\mu}$', '${\\sigma^2}$', 'Lecture 12']],
    cites=cite('L12', 8))
e13a = 4 - 4 * 3 + (9 + 3 ** 2)
assert e13a == 10
D.EX('Sensor calibration',
     r'A sensor output $X$ has $E[X]=3$ and $\operatorname{Var}(X)=9$. (a) Find the mean squared error $E[(2-X)^2]$. '
     r'(b) The reading is calibrated as $Y=2X-3$. Find $\operatorname{Var}(Y)$.',
     [S('(a) **Expand**, then use linearity.', r'E[(2-X)^2]=E[4-4X+X^2]=4-4E[X]+E[X^2]'),
      S('**Turn the shortcut around** to get $E[X^2]$.', r'E[X^2]=\operatorname{Var}(X)+(E[X])^2=9+9=18'),
      S('Substitute.', r'E[(2-X)^2]=4-12+18=10'),
      S('(b) **Shift drops out, scale squares.**', r'\operatorname{Var}(2X-3)=2^2\cdot9=36')],
     r'(a) $10$ (b) $36$', cites=cite('L13', 3))
D.TRY('Given only the mean and variance',
      r'A nonnegative random variable $X$ has $E[X]=3$ and $\operatorname{Var}(X)=1$. Find (a) $E[(3X-2)^2]$, (b) $\operatorname{Var}(2X+1)$.',
      [S('**Second moment** from the shortcut.', r'E[X^2]=1+3^2=10'),
       S('(a) **Expand** and use linearity.', r'E[(3X-2)^2]=9E[X^2]-12E[X]+4=90-36+4=58'),
       S('(b) **Scale squares, shift drops.**', r'\operatorname{Var}(2X+1)=4\cdot1=4')],
      r'(a) $58$ (b) $4$', diff='introductory', cites=cite('T5', 1))
D.TRY('A Gaussian with mean 12',
      r'$X$ is Gaussian with mean $12$ and variance $4$. (a) Find $c$ with $P(X\ge c)=0.5$. (b) Find $E[X^2]$.',
      [S('(a) The bell is **symmetric** about its mean, so half the area is on each side of $12$.', r'c=\mu=12'),
       S('(b) **Turn the shortcut around.**', r'E[X^2]=\operatorname{Var}(X)+\mu^2=4+144=148')],
      r'(a) $c=12$ (b) $E[X^2]=148$', cites=cite('T5', 1))
D.TRY('Variance of a transformed reading',
      r'For $f_X(x)=\tfrac32x^2$ on $|x|\le1$ (Try it 7: $\operatorname{Var}(X)=\tfrac35$), find $E[3X-1]$ and $\operatorname{Var}(3X-1)$. '
      r'Also find $E[Y^2]$ for $Y=|X|$.',
      [S('**Linearity** with $E[X]=0$.', r'E[3X-1]=3\cdot0-1=-1'),
       S('**Scale squares, shift drops.**', r'\operatorname{Var}(3X-1)=9\cdot\tfrac35=\tfrac{27}{5}'),
       S('$Y^2=|X|^2=X^2$, so no new integral is needed.', r'E[Y^2]=E[X^2]=\tfrac35')],
      r'$E[3X-1]=-1$, $\operatorname{Var}(3X-1)=\tfrac{27}{5}$, $E[|X|^2]=\tfrac35$.', cites=cite('T5', 1))

# =====================================================================================================
D.H('Practice Questions')
D.P('Test-style questions for Question 3, roughly easy → hard. Solve on paper first, then open the solution.')

pm = {-1: Fr(1, 10), 0: Fr(2, 5), 1: Fr(3, 10), 2: Fr(1, 5)}
assert sum(pm.values()) == 1
m1 = sum(x * p for x, p in pm.items())
s1 = sum(x * x * p for x, p in pm.items())
v1 = s1 - m1 ** 2
assert (m1, s1, v1) == (Fr(3, 5), Fr(6, 5), Fr(21, 25))
D.Q('A PMF table with an unknown',
    r'''$X$ has the PMF below.

| $x$ | $-1$ | $0$ | $1$ | $2$ |
|---|---|---|---|---|
| $p_X(x)$ | $0.1$ | $c$ | $0.3$ | $0.2$ |

Find (a) $c$, (b) $E[X]$ and $\operatorname{Var}(X)$, (c) $E[5-2X]$ and $\operatorname{Var}(5-2X)$.''',
    [S('(a) **Total = 1.**', r'0.1+c+0.3+0.2=1\;\Rightarrow\;c=0.4'),
     S('(b) **Mean.**', r'E[X]=-0.1+0+0.3+0.4=0.6'),
     S('**Second moment.**', r'E[X^2]=0.1+0+0.3+0.8=1.2'),
     S('**Subtract.**', r'\operatorname{Var}(X)=1.2-0.36=0.84'),
     S('(c) **Linearity**, then **scale squares** (the minus sign disappears).', r'E[5-2X]=5-1.2=3.8,\quad \operatorname{Var}(5-2X)=4(0.84)=3.36')],
    r'$c=0.4$; $E[X]=0.6$, $\operatorname{Var}(X)=0.84$; $E[5-2X]=3.8$, $\operatorname{Var}(5-2X)=3.36$.', diff='introductory')

D.Q('Mean and variance of a uniform',
    r'$X$ is uniform on $[a,b]$: $f_X(x)=\dfrac{1}{b-a}$ on $[a,b]$. Show that $E[X]=\dfrac{a+b}{2}$ and $\operatorname{Var}(X)=\dfrac{(b-a)^2}{12}$.',
    [S('**Mean.** Use $b^2-a^2=(b-a)(b+a)$.', r'E[X]=\frac{1}{b-a}\int_a^b x\,dx=\frac{b^2-a^2}{2(b-a)}=\frac{a+b}{2}'),
     S('**Second moment.** Use $b^3-a^3=(b-a)(b^2+ab+a^2)$.', r'E[X^2]=\frac{1}{b-a}\int_a^b x^2\,dx=\frac{b^3-a^3}{3(b-a)}=\frac{a^2+ab+b^2}{3}'),
     S('**Subtract** over a common denominator 12.', r'\begin{gathered}\operatorname{Var}(X)=\frac{4(a^2+ab+b^2)-3(a+b)^2}{12}\\ =\frac{a^2-2ab+b^2}{12}=\frac{(b-a)^2}{12}\end{gathered}')],
    r'$E[X]=\tfrac{a+b}{2}$ (the midpoint), $\operatorname{Var}(X)=\tfrac{(b-a)^2}{12}$.', diff='introductory')

D.Q('Variance of an exponential',
    r'$X$ is exponential with parameter $\lambda$: $f_X(x)=\lambda e^{-\lambda x}$ for $x\ge0$. Using $E[X]=\tfrac1\lambda$, find $\operatorname{Var}(X)$ and $\sigma_X$.',
    [S('**Second moment** with the shortcut $\\int_0^\\infty x^n e^{-\\lambda x}dx=\\frac{n!}{\\lambda^{n+1}}$ ($n=2$).',
       r'E[X^2]=\lambda\int_0^{\infty}x^2e^{-\lambda x}\,dx=\lambda\cdot\frac{2}{\lambda^3}=\frac{2}{\lambda^2}'),
     S('**Subtract.**', r'\operatorname{Var}(X)=\frac{2}{\lambda^2}-\frac{1}{\lambda^2}=\frac{1}{\lambda^2}'),
     S('**Root:** for an exponential, $\\sigma$ equals the mean.', r'\sigma_X=\frac1\lambda')],
    r'$\operatorname{Var}(X)=\tfrac{1}{\lambda^2}$, $\sigma_X=\tfrac1\lambda=E[X]$.')

ev, ev2 = Fr(4, 3), Fr(2)
vv = ev2 - ev ** 2
assert vv == Fr(2, 9)
D.Q('Average power from a random voltage',
    r'A voltage $V$ (in volts) has PDF $f_V(v)=\tfrac{v}{2}$ for $0\le v\le2$, and $0$ otherwise. It is applied across an $8\ \Omega$ resistor, '
    r'so the power is $P=V^2/8$. Find $E[V]$, $\operatorname{Var}(V)$ and the average power $E[P]$.',
    [S('**Mean.**', r'E[V]=\int_0^2 v\cdot\tfrac v2\,dv=\tfrac12\left[\tfrac{v^3}{3}\right]_0^2=\tfrac43\text{ V}'),
     S('**Second moment.**', r'E[V^2]=\int_0^2 v^2\cdot\tfrac v2\,dv=\tfrac12\left[\tfrac{v^4}{4}\right]_0^2=2\text{ V}^2'),
     S('**Subtract.**', r'\operatorname{Var}(V)=2-\tfrac{16}{9}=\tfrac29\text{ V}^2'),
     S('**Power** is a function of $V$: use $E[g(V)]$ and linearity.', r'E[P]=\tfrac18E[V^2]=\tfrac28=0.25\text{ W}')],
    r'$E[V]=\tfrac43$ V, $\operatorname{Var}(V)=\tfrac29$ V², $E[P]=0.25$ W. (Not $(E[V])^2/8\approx0.22$ W.)')

p_err = 0.03
EN = (1 - p_err) / p_err
D.Q('Average run of good pixels · Tutorial 6 Q7',
    r'Pixels arrive one after another; each is corrupted independently with probability $p=0.03$. '
    r'$N$ = number of error-free pixels between two erroneous ones, so $P(N=k)=(1-p)^k p$, $k=0,1,2,\dots$ Find $E[N]$.',
    [S('**Set up** the sum, with $q=1-p$.', r'E[N]=\sum_{k=0}^{\infty}k\,q^k p=p\sum_{k=1}^{\infty}k\,q^k'),
     S('**Series fact:** differentiate $\\sum q^k=\\frac{1}{1-q}$ and multiply by $q$.', r'\sum_{k=1}^{\infty}k\,q^k=\frac{q}{(1-q)^2}=\frac{q}{p^2}'),
     S('**Combine.**', r'E[N]=p\cdot\frac{q}{p^2}=\frac{1-p}{p}'),
     S('**Plug in** $p=0.03$.', r'E[N]=\frac{0.97}{0.03}\approx' + f'{EN:.2f}')],
    f'$E[N]=\\dfrac{{1-p}}{{p}}\\approx {EN:.2f}$ good pixels between errors.', cites=cite('T6', 1))

ms, ms2 = Fr(3, 10) * 5 + Fr(7, 10) * Fr(5, 2), Fr(3, 10) * 25 + Fr(7, 10) * Fr(25, 3)
mv = ms2 - ms ** 2
assert (ms, ms2, mv) == (Fr(13, 4), Fr(40, 3), Fr(133, 48))
D.Q('A sensor that saturates',
    r'A sensor reading $X$ saturates: with probability $0.3$ it reads exactly $X=5$; otherwise (probability $0.7$) it is uniform on $(0,5)$, '
    r'so the continuous part has density $0.7\cdot\tfrac15=0.14$ on $(0,5)$. Find $E[X]$ and $\operatorname{Var}(X)$.',
    [S('**Mean:** point mass + integral.', r'\begin{gathered}E[X]=5(0.3)+\int_0^5x(0.14)\,dx\\ =1.5+0.14\cdot\tfrac{25}{2}=1.5+1.75=3.25\end{gathered}'),
     S('**Second moment:** same split, with $x^2$.', r'E[X^2]=25(0.3)+\int_0^5x^2(0.14)\,dx=7.5+0.14\cdot\tfrac{125}{3}=\tfrac{40}{3}'),
     S('**Subtract.**', r'\operatorname{Var}(X)=\tfrac{40}{3}-3.25^2=\tfrac{133}{48}\approx' + f'{float(mv):.3f}')],
    r'$E[X]=3.25$, $\operatorname{Var}(X)=\tfrac{133}{48}\approx' + f'{float(mv):.3f}' + '$.')

cans = {'A': 140, 'B': 112, 'C': 125, 'D': 183}
tot = sum(cans.values())
Ex = Fr(tot, 4)
Ey = Fr(sum(m * m for m in cans.values()), tot)
assert tot == 560 and Ex == 140 and abs(float(Ey) - 145.10) < 0.01
D.Q('Mars canisters · Practice 03 Q6',
    r'A rover returns 560 g of material in four canisters A, B, C, D holding $140$, $112$, $125$ and $183$ g. '
    r'First a **canister** is chosen at random (each $\tfrac14$); $x$ = grams in it. '
    r'Then a **1-gram sample** is chosen at random from all 560 g; $y$ = grams in the canister it came from. '
    r'(a) Which of $E[x]$, $E[y]$ should be larger, and why? (b) Compute both.',
    [S('(a) For $y$, a canister is picked with probability **proportional to its mass**, so heavy canisters count more. Expect $E[y]>E[x]$.',
       r'P(y=m)=\frac{m}{560}'),
     S('(b) **$E[x]$:** equal weights.', r'E[x]=\tfrac14(140+112+125+183)=140\text{ g}'),
     S('**$E[y]$:** weight each mass $m$ by $\\frac{m}{560}$.', r'E[y]=\frac{140^2+112^2+125^2+183^2}{560}=\frac{' + str(sum(m * m for m in cans.values())) + r'}{560}'),
     S('Evaluate.', r'E[y]\approx' + f'{float(Ey):.2f}' + r'\text{ g}>140\text{ g}')],
    f'$E[x]=140$ g, $E[y]\\approx {float(Ey):.2f}$ g. Sampling by gram favours the big canisters.', cites=cite('P3', 1))

D.Q('Triangle PDF',
    r'$X$ has the triangular PDF $f_X(x)=x$ on $[0,1]$, $f_X(x)=2-x$ on $[1,2]$, and $0$ otherwise. '
    r'Find $E[X]$, $\operatorname{Var}(X)$, and $\operatorname{Var}(2X+3)$.',
    [S('**Mean:** the triangle is symmetric about $x=1$.', r'E[X]=1'),
     S('**Second moment:** split the integral at $x=1$.', r'E[X^2]=\int_0^1x^3\,dx+\int_1^2x^2(2-x)\,dx'),
     S('Integrate each piece.', r'=\tfrac14+\left[\tfrac{2x^3}{3}-\tfrac{x^4}{4}\right]_1^2=\tfrac14+\tfrac{11}{12}=\tfrac76'),
     S('**Subtract.**', r'\operatorname{Var}(X)=\tfrac76-1=\tfrac16'),
     S('**Scale squares.**', r'\operatorname{Var}(2X+3)=4\cdot\tfrac16=\tfrac23')],
    r'$E[X]=1$, $\operatorname{Var}(X)=\tfrac16$, $\operatorname{Var}(2X+3)=\tfrac23$.')

D.Q('The mean from the CDF · Tutorial 5 Q3 / Practice 03 Q1',
    r'For a **nonnegative** continuous $X$ with CDF $F_X$, show that $E[X]=\displaystyle\int_0^{\infty}\big(1-F_X(t)\big)\,dt$ '
    r'(assume $t\,(1-F_X(t))\to0$ as $t\to\infty$). Then use it to find the mean of an exponential.',
    [S('**By parts** with $u=1-F_X(t)$ and $dv=dt$: then $du=-f_X(t)\\,dt$ and $v=t$.',
       r'\int_0^{\infty}(1-F_X(t))\,dt=\Big[t\,(1-F_X(t))\Big]_0^{\infty}+\int_0^{\infty}t\,f_X(t)\,dt'),
     S('The boundary term is $0$ at both ends (given at $\\infty$; $t=0$ at the bottom).', r'=0+E[X]'),
     S('**Exponential:** $1-F_X(t)=e^{-\\lambda t}$.', r'E[X]=\int_0^{\infty}e^{-\lambda t}\,dt=\frac1\lambda')],
    r'Shown; for the exponential $E[X]=\tfrac1\lambda$ with no by-parts on $x e^{-\lambda x}$.', diff='advanced',
    cites=cite('T5', 1) + cite('P3', 1))

C6 = 2 / pi
V6 = 4 / pi - 1
D.Q('Find the constants, then the variance · Tutorial 6 Q6',
    r'''$X$ has PDF

$$
f_X(x)=\frac{C}{1+(x+K)^2},\qquad -K-1\le x\le -K+1,
$$

and $0$ otherwise, where $C>0$ and $K$ are constants. (a) Find $C$ and $K$ so that $E[X]=5$. (b) Find $\operatorname{Var}(X)$.''',
    [S('**Shift:** let $u=x+K$, so $u\\in[-1,1]$ and $X=U-K$ with $f_U(u)=\\frac{C}{1+u^2}$.', r'\int_{-1}^{1}\frac{C}{1+u^2}\,du=C\big[\arctan u\big]_{-1}^{1}=C\cdot\frac{\pi}{2}'),
     S('(a) **Total area = 1.**', r'C=\frac{2}{\pi}'),
     S('$f_U$ is **even**, so $E[U]=0$. Then use linearity.', r'E[X]=E[U]-K=-K=5\;\Rightarrow\;K=-5'),
     S('(b) A shift does not change Var, and $E[U]=0$.', r'\operatorname{Var}(X)=\operatorname{Var}(U)=E[U^2]'),
     S('Write $\\frac{u^2}{1+u^2}=1-\\frac{1}{1+u^2}$.', r'E[U^2]=\frac2\pi\int_{-1}^{1}\Big(1-\frac{1}{1+u^2}\Big)du=\frac2\pi\Big(2-\frac\pi2\Big)'),
     S('Simplify.', r'\operatorname{Var}(X)=\frac4\pi-1\approx' + f'{V6:.4f}')],
    r'(a) $C=\tfrac2\pi$, $K=-5$ (so $X\in[4,6]$) (b) $\operatorname{Var}(X)=\tfrac4\pi-1\approx' + f'{V6:.4f}' + '$',
    diff='advanced', cites=cite('T6', 1))
assert abs(C6 - 0.63662) < 1e-5


def verify():
    import sympy as sp
    x, t, u, v = sp.symbols('x t u v', real=True)
    lam, p, a, b, gam, mu = sp.symbols('lambda p a b gamma mu', positive=True)
    sig = sp.Symbol('sigma', positive=True)
    k = sp.Symbol('k', integer=True, nonnegative=True)
    n = sp.Symbol('n', integer=True, positive=True)
    I = sp.integrate
    # Topic 1
    assert sp.Rational(sum(range(1, 7)), 6) == sp.Rational(7, 2) and sp.Rational(sum(i * i for i in range(1, 7)), 6) == sp.Rational(91, 6)
    assert I(x / 2, (x, 0, 2)) == 1 and I(x ** 2 / 2, (x, 0, 2)) == sp.Rational(4, 3)
    assert sp.simplify(I(t * lam * sp.exp(-lam * t), (t, 0, sp.oo)) - 1 / lam) == 0
    lap = lam / 2 * sp.exp(-lam * sp.Abs(t - gam))
    lap_mean = I((u + gam) * lam / 2 * sp.exp(-lam * u), (u, 0, sp.oo)) + I((u + gam) * lam / 2 * sp.exp(lam * u), (u, -sp.oo, 0))
    assert sp.simplify(lap_mean - gam) == 0 and lap is not None
    assert I(x * sp.Rational(8, 100), (x, 0, 10)) == 4
    # Topic 2
    C = sp.Symbol('C')
    Cv = sp.solve(I(C * x ** 2, (x, -1, 1)) - 1, C)[0]
    assert Cv == sp.Rational(3, 2)
    assert sp.expand(I(Cv * t ** 2, (t, -1, x)) - (x ** 3 + 1) / 2) == 0
    assert I(Cv * x ** 3, (x, -1, 1)) == 0 and I(Cv * x ** 4, (x, -1, 1)) == sp.Rational(3, 5)
    # Topic 3 table
    q = 1 - p
    pois = sp.exp(-lam) * lam ** k / sp.factorial(k)
    pm1 = sp.simplify(sp.summation(k * pois, (k, 0, sp.oo)))
    pm2 = sp.simplify(sp.summation(k ** 2 * pois, (k, 0, sp.oo)))
    assert sp.simplify(pm1 - lam) == 0 and sp.simplify(pm2 - pm1 ** 2 - lam) == 0
    for nn in range(1, 7):  # binomial, checked for small n
        pmf = [sp.binomial(nn, j) * p ** j * q ** (nn - j) for j in range(nn + 1)]
        e1 = sp.expand(sum(j * pmf[j] for j in range(nn + 1)))
        e2 = sp.expand(sum(j * j * pmf[j] for j in range(nn + 1)))
        assert sp.simplify(e1 - nn * p) == 0 and sp.simplify(e2 - e1 ** 2 - nn * p * q) == 0
    for pv in (sp.Rational(1, 5), sp.Rational(1, 2), sp.Rational(3, 100)):  # geometric (both conventions), numerically exact
        g1 = sp.summation(k * (1 - pv) ** (k - 1) * pv, (k, 1, sp.oo)); g2 = sp.summation(k ** 2 * (1 - pv) ** (k - 1) * pv, (k, 1, sp.oo))
        assert sp.simplify(g1 - 1 / pv) == 0 and sp.simplify(g2 - g1 ** 2 - (1 - pv) / pv ** 2) == 0
        h1 = sp.summation(k * (1 - pv) ** k * pv, (k, 0, sp.oo)); h2 = sp.summation(k ** 2 * (1 - pv) ** k * pv, (k, 0, sp.oo))
        assert sp.simplify(h1 - (1 - pv) / pv) == 0 and sp.simplify(h2 - h1 ** 2 - (1 - pv) / pv ** 2) == 0
    bb = sp.Symbol('bb', positive=True)
    um = I(x / (bb), (x, a, a + bb)); uv = sp.simplify(I(x ** 2 / bb, (x, a, a + bb)) - um ** 2)
    assert sp.simplify(um - (2 * a + bb) / 2) == 0 and sp.simplify(uv - bb ** 2 / 12) == 0
    e2 = I(x ** 2 * lam * sp.exp(-lam * x), (x, 0, sp.oo))
    assert sp.simplify(e2 - 2 / lam ** 2) == 0
    gm = I(x * sp.exp(-(x - mu) ** 2 / (2 * sig ** 2)) / sp.sqrt(2 * sp.pi * sig ** 2), (x, -sp.oo, sp.oo))
    gv = I((x - mu) ** 2 * sp.exp(-(x - mu) ** 2 / (2 * sig ** 2)) / sp.sqrt(2 * sp.pi * sig ** 2), (x, -sp.oo, sp.oo))
    assert sp.simplify(gm - mu) == 0 and sp.simplify(gv - sig ** 2) == 0
    # Practice questions
    assert I(v * v / 2, (v, 0, 2)) == sp.Rational(4, 3) and I(v ** 3 / 2, (v, 0, 2)) == 2
    p_ = sp.Rational(3, 100)
    assert sp.simplify(sp.summation(k * (1 - p_) ** k * p_, (k, 0, sp.oo)) - (1 - p_) / p_) == 0
    assert 5 * sp.Rational(3, 10) + I(x * sp.Rational(14, 100), (x, 0, 5)) == sp.Rational(13, 4)
    assert 25 * sp.Rational(3, 10) + I(x ** 2 * sp.Rational(14, 100), (x, 0, 5)) == sp.Rational(40, 3)
    tri_m = I(x * x, (x, 0, 1)) + I(x * (2 - x), (x, 1, 2))
    tri_2 = I(x ** 3, (x, 0, 1)) + I(x ** 2 * (2 - x), (x, 1, 2))
    assert tri_m == 1 and tri_2 == sp.Rational(7, 6) and 4 * (tri_2 - 1) == sp.Rational(2, 3)
    assert sp.simplify(I(sp.exp(-lam * t), (t, 0, sp.oo)) - 1 / lam) == 0
    Cs = sp.solve(I(C / (1 + u ** 2), (u, -1, 1)) - 1, C)[0]
    assert sp.simplify(Cs - 2 / sp.pi) == 0
    K = sp.Symbol('K')
    EX = I(x * Cs / (1 + (x + K) ** 2), (x, -K - 1, -K + 1))
    assert sp.solve(sp.simplify(EX) - 5, K) == [-5]
    var6 = I((x - 5) ** 2 * Cs / (1 + (x - 5) ** 2), (x, 4, 6))
    assert sp.simplify(var6 - (4 / sp.pi - 1)) == 0
    print('q3 verify ok')


if __name__ == '__main__':
    verify()
    D.save()
