r"""Test 2 - Question 3: expected values, variances, properties of expectation and variance (Lectures 11-13).

v3 layout (REWRITE_PLAN.md): Topic 1 (mean and variance from a PMF / PDF / CDF) and Topic 2 (the rules and the named
families): explanation and formulas first, then open worked examples (D.EX); Extras (tail formula, moments, Chebyshev
and Markov); Practice Questions. Step words: Spot, Mean, Square, Subtract, Root; for the rules: Expand, Swap, Plug in.
"""
from fractions import Fraction as Fr
from math import sqrt

from lib226 import Doc, S, cite

D = Doc('q3', 'Test 2 - Question 3', ['expected_value', 'variance', 'standard_deviation', 'linearity', 'moments'])

D.P(r'**Lectures 11–13.** The mean (the long-run average) and the variance (the spread) of a random variable.',
    cites=cite('L11', 6) + cite('L12', 6) + cite('L13', 2))
D.P(r'**Question 3 asks:** find $E[X]$, $\operatorname{Var}(X)$ or $\sigma_X$. You get a PMF, a PDF, a CDF, a named family (“$X$ is Poisson”), or just two numbers like “$E[X]=3$, $\operatorname{Var}(X)=9$”.')

# =====================================================================================================
D.H('Topic 1: mean and variance from a distribution')
D.P(r'**The mean** $E[X]$ is the long-run average: take each value, multiply by its chance, add them all up.')
D.P(r'**The variance** $\operatorname{Var}(X)$ measures the spread: how far $X$ usually lands from its mean. You get it in the same 4 steps every time:')
D.L([r'**Mean:** find $E[X]$.',
     r'**Square:** the same sum or integral with $x^2$ in place of $x$. That’s $E[X^2]$.',
     r'**Subtract:** $\operatorname{Var}(X)=E[X^2]-(E[X])^2$.',
     r'**Root:** $\sigma_X=\sqrt{\operatorname{Var}(X)}$ (the standard deviation, in the same units as $X$).'], ordered=True)
D.P(r'Discrete $X$ uses a **sum** over its values. Continuous $X$ uses an **integral** over where $f_X\ne0$. Otherwise the formulas are the same:')
D.T(['', r'Discrete (PMF $p_X$)', r'Continuous (PDF $f_X$)'],
    [[r'**Mean** $E[X]$', r'$\sum_x x\,p_X(x)$', r'$\int x\,f_X(x)\,dx$'],
     [r'**Square** $E[X^2]$', r'$\sum_x x^2\,p_X(x)$', r'$\int x^2\,f_X(x)\,dx$'],
     [r'**Any function** $E[g(X)]$', r'$\sum_x g(x)\,p_X(x)$', r'$\int g(x)\,f_X(x)\,dx$']], cites=cite('L11', 7) + cite('L12', 2))
D.EQ(r'\operatorname{Var}(X)=E[X^2]-\big(E[X]\big)^2,\qquad \sigma_X=\sqrt{\operatorname{Var}(X)}', cites=cite('L12', 6))
D.CO('warning', r'**$E[X^2]\ne(E[X])^2$.** Square **inside** the sum or integral, not after. A die: $E[X^2]=\tfrac{91}{6}\approx15.17$, but $3.5^2=12.25$.',
     cites=cite('L12', 2))
D.P(r'**Given a CDF $F_X$ instead?** Turn it into a PMF or PDF first, then use the table:')
D.L([r'**Staircase** $F_X$ (discrete): the **jump sizes** are the PMF.',
     r'**Smooth** $F_X$ (continuous): the **slope** is the PDF, $f_X(x)=F_X^{\prime}(x)$.'], cites=cite('L9', 4))
D.P(r'**Shortcut 1, symmetry:** if $f_X$ is a mirror image around some point $c$, then $E[X]=c$. No integral. For example $f_X(x)=\tfrac32x^2$ on $[-1,1]$ is the same on both sides of $0$:')
D.EQ(r'E[X]=\int_{-1}^{1}x\cdot\frac32x^2\,dx=0')
D.P(r'**Shortcut 2, the exponential integral:** it skips integrating by parts.')
D.EQ(r'\int_0^{\infty}x^n\,e^{-\lambda x}\,dx=\frac{n!}{\lambda^{n+1}}\qquad\text{e.g. }\int_0^\infty x^2e^{-x}\,dx=\frac{2!}{1^3}=2')

D.EX('From a PMF · a fair die (Lecture 11)',
     r'$X$ = the number on a fair die. Find $E[X]$, $\operatorname{Var}(X)$ and $\sigma_X$.',
     [S(r'**Spot:** a list of values with chances → a PMF, so use sums. Each face has chance $\tfrac16$.'),
      S(r'**Mean.**', r'E[X]=\frac16(1+2+3+4+5+6)=\frac{21}{6}=3.5'),
      S(r'**Square:** square each value **inside** the sum.', r'E[X^2]=\frac16(1+4+9+16+25+36)=\frac{91}{6}'),
      S(r'**Subtract.**', r'\operatorname{Var}(X)=\frac{91}{6}-\Big(\frac72\Big)^2=\frac{182-147}{12}=\frac{35}{12}'),
      S(r'**Root.**', r'\sigma_X=\sqrt{35/12}\approx1.71')],
     r'$E[X]=3.5$, $\operatorname{Var}(X)=\tfrac{35}{12}$, $\sigma_X\approx1.71$', cites=cite('L11', 8) + cite('L12', 2))

D.EX('From a PMF · $E[g(X)]$, average power (Lecture 12)',
     r'A voltage $X$ is $4$ V or $6$ V, each half the time. Find $E[X]$, $\operatorname{Var}(X)$, and the average power $E[X^2/R]$ across $R=2\ \Omega$.',
     [S(r'**Spot:** two values, each with chance $0.5$ → a PMF.'),
      S(r'**Mean.**', r'E[X]=4(0.5)+6(0.5)=5\ \text{V}'),
      S(r'**Square.**', r'E[X^2]=16(0.5)+36(0.5)=26'),
      S(r'**Subtract.**', r'\operatorname{Var}(X)=26-5^2=1\ \text{V}^2'),
      S(r'**Any function:** put $g(x)=x^2/2$ in place of $x$, same chances.', r'E\Big[\frac{X^2}{2}\Big]=\frac{16}{2}(0.5)+\frac{36}{2}(0.5)=13\ \text{W}')],
     r'$E[X]=5$ V, $\operatorname{Var}(X)=1\ \text{V}^2$, average power $13$ W', cites=cite('L12', 2))

D.EX('From a PMF · a 0/1 variable (Tutorial 5 Q1)',
     r'$X$ is $0$ with probability $p$ and $1$ with probability $1-p$. Find $E[X]$, $\operatorname{Var}(X)$ and $E[X^5]$.',
     [S(r'**Spot:** two values → a PMF.'),
      S(r'**Mean.**', r'E[X]=0\cdot p+1\cdot(1-p)=1-p'),
      S(r'**Square:** $0^n=0$ and $1^n=1$, so $X^n=X$ for any power.', r'E[X^2]=E[X^5]=E[X]=1-p'),
      S(r'**Subtract.**', r'\operatorname{Var}(X)=(1-p)-(1-p)^2=(1-p)\,p')],
     r'$E[X]=1-p$, $\operatorname{Var}(X)=p(1-p)$, $E[X^5]=1-p$', cites=cite('T5', 1))

D.EX('From a PDF · exponential (Practice 03 Q2)',
     r'$X$ is the time between customers, with PDF $f_X(t)=\lambda e^{-\lambda t}$ for $t\ge0$. Find $E[X]$ and $\operatorname{Var}(X)$.',
     [S(r'**Spot:** a formula $f_X$ → a PDF, so use integrals over $t\ge0$.'),
      S(r'**Mean:** Shortcut 2 with $n=1$.', r'E[X]=\lambda\int_0^{\infty}t\,e^{-\lambda t}\,dt=\lambda\cdot\frac{1!}{\lambda^2}=\frac1\lambda'),
      S(r'**Square:** Shortcut 2 with $n=2$.', r'E[X^2]=\lambda\cdot\frac{2!}{\lambda^3}=\frac{2}{\lambda^2}'),
      S(r'**Subtract.**', r'\operatorname{Var}(X)=\frac{2}{\lambda^2}-\frac{1}{\lambda^2}=\frac{1}{\lambda^2}'),
      S(r'**Root.** So 3 customers per minute ($\lambda=3$) means a mean gap of $\tfrac13$ min.', r'\sigma_X=\frac1\lambda')],
     r'$E[X]=\tfrac1\lambda$, $\operatorname{Var}(X)=\tfrac1{\lambda^2}$', cites=cite('P3', 1))

D.EX('From a PDF with a jump · mixed $X$ (Lecture 11)',
     r'A received signal $X$ is exactly $0$ with chance $0.2$. Otherwise it is spread evenly over $(0,10)$, with density $0.08$. Find $E[X]$.',
     [S(r'**Spot:** an exact value with real chance (a jump) **plus** a density → mixed. Do each part, then add.'),
      S(r'**Mean**, jump part: value × its chance.', r'0\cdot0.2=0'),
      S(r'**Mean**, density part: the integral.', r'\int_0^{10}x\,(0.08)\,dx=0.08\cdot\frac{10^2}{2}=4'),
      S(r'Add the two parts.', r'E[X]=0+4=4')],
     r'$E[X]=4$', cites=cite('L11', 4))

st = {1: Fr(1, 5), 2: Fr(1, 2), 4: Fr(3, 10)}
st_m = sum(x * p for x, p in st.items())
st_s = sum(x * x * p for x, p in st.items())
st_v = st_s - st_m ** 2
assert sum(st.values()) == 1 and (st_m, st_s, st_v) == (Fr(12, 5), Fr(7), Fr(31, 25))
D.EX('From a CDF · a staircase',
     r'''Find $E[X]$, $\operatorname{Var}(X)$ and $\sigma_X$:

$$
F_X(x)=\begin{cases}0,&x<1\\ 0.2,&1\le x<2\\ 0.7,&2\le x<4\\ 1,&x\ge4\end{cases}
$$''',
     [S(r'**Spot:** $F_X$ jumps → discrete. The **jump sizes** are the PMF.', r'p_X(1)=0.2,\quad p_X(2)=0.7-0.2=0.5,\quad p_X(4)=1-0.7=0.3'),
      S(r'**Mean.**', r'E[X]=1(0.2)+2(0.5)+4(0.3)=2.4'),
      S(r'**Square.**', r'E[X^2]=1(0.2)+4(0.5)+16(0.3)=7'),
      S(r'**Subtract.**', r'\operatorname{Var}(X)=7-2.4^2=1.24'),
      S(r'**Root.**', r'\sigma_X=\sqrt{1.24}\approx' + f'{sqrt(st_v):.3f}')],
     f'$E[X]=2.4$, $\\operatorname{{Var}}(X)=1.24$, $\\sigma_X\\approx {sqrt(st_v):.3f}$')

D.EX('From a CDF · a smooth one',
     r'$F_X(x)=x^2$ for $0\le x\le1$ ($0$ before, $1$ after). Find $E[X]$ and $\operatorname{Var}(X)$.',
     [S(r'**Spot:** $F_X$ rises smoothly → continuous. The **slope** is the PDF.', r'f_X(x)=\frac{d}{dx}x^2=2x,\qquad 0\le x\le1'),
      S(r'**Mean.**', r'E[X]=\int_0^1x\cdot2x\,dx=\frac23'),
      S(r'**Square.**', r'E[X^2]=\int_0^1x^2\cdot2x\,dx=\frac12'),
      S(r'**Subtract.**', r'\operatorname{Var}(X)=\frac12-\frac49=\frac1{18}')],
     r'$E[X]=\tfrac23$, $\operatorname{Var}(X)=\tfrac1{18}$')

# =====================================================================================================
D.H('Topic 2: shortcuts: the rules and the named families')
D.P(r'Often you don’t need any sum or integral. Two kinds of question let you skip them.')
D.P(r'**The rules.** Say you know $E[X]$ and $\operatorname{Var}(X)$, and you want them for a new variable $aX+b$ ($a$, $b$ = any numbers):')
D.EQ(r'E[aX+b]=a\,E[X]+b\qquad\qquad \operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)', cites=cite('L12', 5) + cite('L12', 9))
D.L([r'**Adding $b$** shifts every value by $b$. The mean moves by $b$, but the spread stays the same, so $b$ drops out of Var.',
     r'**Multiplying by $a$** stretches every distance by $a$. So Var gets $a^2$, and $\sigma$ gets $|a|$. Example: $\operatorname{Var}(X)=9$ gives $\operatorname{Var}(2X-3)=4\cdot9=36$.'])
D.P(r'**Need $E[X^2]$?** Turn the variance formula around (call it the **Swap**):')
D.EQ(r'E[X^2]=\operatorname{Var}(X)+\big(E[X]\big)^2')
D.P(r'**A square like $E[(2-X)^2]$?** **Expand** it first, then take $E$ of each term:')
D.EQ(r'E[(2-X)^2]=E[4-4X+X^2]=4-4E[X]+E[X^2]')
D.P(r'**Named families.** If the question says “$X$ is Binomial / Poisson / uniform / …”, read the mean and variance off this table:')
D.T(['Family', 'The letters', r'$E[X]$', r'$\operatorname{Var}(X)$'],
    [[r'Bernoulli$(p)$', r'$p$ = chance of a $1$', r'$p$', r'$p(1-p)$'],
     [r'Binomial$(n,p)$', r'$n$ = tries, $p$ = chance each succeeds', r'$np$', r'$np(1-p)$'],
     [r'Geometric$(p)$', r'$p$ = chance each try succeeds; $X$ = tries until the first success', r'$\dfrac1p$', r'$\dfrac{1-p}{p^2}$'],
     [r'Poisson$(\lambda)$', r'$\lambda$ = the average count', r'$\lambda$', r'$\lambda$'],
     [r'Uniform$(a,b)$', r'$a$, $b$ = the two ends', r'$\dfrac{a+b}{2}$', r'$\dfrac{(b-a)^2}{12}$'],
     [r'Exponential$(\lambda)$', r'$\lambda$ = rate per unit time', r'$\dfrac1\lambda$', r'$\dfrac1{\lambda^2}$'],
     [r'Gaussian $N(\mu,\sigma^2)$', r'$\mu$ = mean, $\sigma^2$ = variance', r'$\mu$', r'$\sigma^2$']], cites=cite('L12', 8))
D.CO('warning', r'**Geometric counting failures** ($N$ = failures before the first success, $k=0,1,\dots$) is one less than the tries: $E[N]=\tfrac1p-1=\tfrac{1-p}{p}$. Same variance.')

e13a = 4 - 4 * 3 + (9 + 3 ** 2)
assert e13a == 10
D.EX('Only $E[X]$ and Var given · expand a square (Lecture 13)',
     r'$E[X]=3$ and $\operatorname{Var}(X)=9$. Find $E[(2-X)^2]$ and $\operatorname{Var}(2X-3)$.',
     [S(r'**Spot:** no PMF or PDF, just two numbers → the rules.'),
      S(r'**Expand**, then take $E$ of each term.', r'E[(2-X)^2]=E[4-4X+X^2]=4-4E[X]+E[X^2]'),
      S(r'**Swap** for $E[X^2]$.', r'E[X^2]=9+3^2=18'),
      S(r'**Plug in.**', r'E[(2-X)^2]=4-4(3)+18=10'),
      S(r'**Var rule:** $a=2$, $b=-3$. The $-3$ drops out, the $2$ gets squared.', r'\operatorname{Var}(2X-3)=2^2\cdot9=36')],
     r'$E[(2-X)^2]=10$, $\operatorname{Var}(2X-3)=36$', cites=cite('L13', 3))

D.EX('Only $E[X]$ and Var given · another one (Tutorial 5 Q2)',
     r'$X\ge0$ has $E[X]=3$ and $\operatorname{Var}(X)=1$. Find (a) $E[(3X-2)^2]$, (b) $\operatorname{Var}(2X+1)$.',
     [S(r'**Spot:** only $E$ and Var → the rules. **Swap** first.', r'E[X^2]=1+3^2=10'),
      S(r'(a) **Expand**, then take $E$ of each term.', r'E[(3X-2)^2]=E[9X^2-12X+4]=9E[X^2]-12E[X]+4'),
      S(r'**Plug in.**', r'9(10)-12(3)+4=58'),
      S(r'(b) **Var rule:** $a=2$, $b=1$. The $+1$ drops out, the $2$ gets squared.', r'\operatorname{Var}(2X+1)=2^2\cdot1=4')],
     r'(a) $58$ (b) $4$', cites=cite('T5', 1))

D.EX('A named family · read it off',
     r'(a) $X\sim$ Binomial$(10,\,0.3)$: find $E[X]$ and $\operatorname{Var}(X)$. '
     r'(b) $X\sim$ Uniform$(2,8)$: find $\operatorname{Var}(X)$ and $\sigma_X$. '
     r'(c) $X\sim$ Poisson$(3)$: find $E[(X-1)^2]$.',
     [S(r'(a) **Spot:** Binomial. **Read off** $n=10$, $p=0.3$, then use $np$ and $np(1-p)$.', r'E[X]=10(0.3)=3,\qquad \operatorname{Var}(X)=10(0.3)(0.7)=2.1'),
      S(r'(b) **Spot:** uniform. **Read off** $a=2$, $b=8$. **Root** for $\sigma$.', r'\operatorname{Var}(X)=\frac{(8-2)^2}{12}=3,\qquad \sigma_X=\sqrt3\approx1.732'),
      S(r'(c) **Spot:** Poisson, $\lambda=3$, so $E[X]=\operatorname{Var}(X)=3$. **Swap.**', r'E[X^2]=3+3^2=12'),
      S(r'**Expand** and plug in.', r'E[(X-1)^2]=E[X^2]-2E[X]+1=12-6+1=7')],
     r'(a) $3$, $2.1$ (b) $3$, $\sqrt3\approx1.732$ (c) $7$')

# =====================================================================================================
D.H('Extras: the tail formula, moments, Chebyshev and Markov')
D.P(r'**The tail formula.** If $X$ can’t be negative ($X\ge0$), you can get the mean straight from the CDF, without finding the PDF first:')
D.EQ(r'E[X]=\int_0^{\infty}\big(1-F_X(t)\big)\,dt\qquad\qquad E[N]=\sum_{k=0}^{\infty}P(N>k)\ \ (N=0,1,2,\dots)', cites=cite('P3', 1))
D.P(r'$1-F_X(t)=P(X>t)$ is the chance $X$ is still bigger than $t$. Adding those chances up gives the mean.')
D.EX('Tail formula · smooth and whole-number',
     r'(a) $F_X(x)=x^2$ on $[0,1]$. Find $E[X]$ with the tail formula. (b) $N$ is $1$, $2$ or $3$, each with chance $\tfrac13$. Find $E[N]$ the same way.',
     [S(r'(a) **Spot:** $X\ge0$ and a CDF is given. $1-F_X=1-t^2$ up to $t=1$, then $0$.', r'E[X]=\int_0^1(1-t^2)\,dt=1-\frac13=\frac23'),
      S(r'Same answer as the slope method in Topic 1.'),
      S(r'(b) List $P(N>k)$ until it hits $0$.', (r'P(N>0)=1,\quad P(N>1)=\frac23', r'P(N>2)=\frac13,\quad P(N>3)=0')),
      S(r'Add them.', r'E[N]=1+\frac23+\frac13=2')],
     r'(a) $\tfrac23$ (b) $2$')
D.P(r'**Moments** (Lecture 13). The $n$th **moment** is $E[X^n]$: $E[X]$ is the 1st, $E[X^2]$ the 2nd. A **central** moment measures from the mean instead. The variance is the 2nd central moment:', cites=cite('L13', 4))
D.EQ(r'\operatorname{Var}(X)=E\big[(X-\mu_X)^2\big],\qquad \mu_X=E[X]')
D.P(r'**Chebyshev and Markov** (Practice 03, not in the lectures). They give an upper limit on a chance when you only know $E$ and Var. $\varepsilon$ = how far from the mean; $a$ = a cutoff:', cites=cite('P3', 3))
D.EQ(r'\text{Chebyshev: }\ P\big(|Y-\mu_Y|\ge\varepsilon\big)\le\frac{\operatorname{Var}(Y)}{\varepsilon^2}')
D.EQ(r'\text{Markov }(Y\ge0)\text{: }\ P(Y\ge a)\le\frac{E[Y]}{a}')
D.EX('Chebyshev and Markov · plug in',
     r'(a) $\operatorname{Var}(Y)=1$. How likely is $Y$ to land $2$ or more from its mean, at most? (b) $Y\ge0$ with $E[Y]=3$. Bound $P(Y\ge10)$.',
     [S(r'(a) **Chebyshev:** read off $\operatorname{Var}(Y)=1$, $\varepsilon=2$.', r'P\big(|Y-\mu|\ge2\big)\le\frac{1}{2^2}=\frac14'),
      S(r'(b) **Markov:** read off $E[Y]=3$, $a=10$.', r'P(Y\ge10)\le\frac{3}{10}=0.3')],
     r'(a) at most $\tfrac14$ (b) at most $0.3$')

# =====================================================================================================
D.H('Practice Questions')
D.CO('tip', r'''**Question 3 is always: find $E[X]$, $\operatorname{Var}(X)$ and $\sigma_X$.** Same 4 steps every time: **Mean → Square → Subtract → Root.** Only the start changes:

1. **From a PMF:** sums, $\sum x\,p_X(x)$ and $\sum x^2\,p_X(x)$.
2. **From a PDF:** integrals, $\int x\,f_X\,dx$ and $\int x^2 f_X\,dx$. Symmetric → mean = the centre. $\int_0^\infty x^ne^{-\lambda x}dx=\tfrac{n!}{\lambda^{n+1}}$.
3. **From a CDF:** staircase → the jumps are the PMF; smooth → the slope is the PDF. Then 1 or 2.''')
D.P('Test-style, easy → medium, same level as the practice sets. Solve on paper first, then open the solution.')


def mvs(pmf):
    m = sum(x * p for x, p in pmf.items())
    s = sum(x * x * p for x, p in pmf.items())
    assert sum(pmf.values()) == 1
    return m, s, s - m ** 2


# ---- From a PMF
c3 = {0: Fr(1, 8), 1: Fr(3, 8), 2: Fr(3, 8), 3: Fr(1, 8)}
assert mvs(c3) == (Fr(3, 2), Fr(3), Fr(3, 4))
D.Q('From a PMF · 3 coins',
    r'Toss a fair coin 3 times. $X$ = the number of heads, with PMF $\tfrac18,\tfrac38,\tfrac38,\tfrac18$ at $x=0,1,2,3$. Find $E[X]$, $\operatorname{Var}(X)$ and $\sigma_X$.',
    [S(r'**Spot:** a PMF → sums.'),
     S(r'**Mean.**', r'E[X]=0\cdot\frac18+1\cdot\frac38+2\cdot\frac38+3\cdot\frac18=\frac{12}{8}=1.5'),
     S(r'**Square:** square each value **inside** the sum.', r'E[X^2]=0\cdot\frac18+1\cdot\frac38+4\cdot\frac38+9\cdot\frac18=\frac{24}{8}=3'),
     S(r'**Subtract.**', r'\operatorname{Var}(X)=3-1.5^2=0.75'),
     S(r'**Root.**', r'\sigma_X=\sqrt{0.75}\approx' + f'{sqrt(0.75):.3f}')],
    f'$E[X]=1.5$, $\\operatorname{{Var}}(X)=0.75$, $\\sigma_X\\approx {sqrt(0.75):.3f}$', diff='introductory', cites=cite('L11', 8))

pm = {-1: Fr(1, 10), 0: Fr(2, 5), 1: Fr(3, 10), 2: Fr(1, 5)}
m1, s1, v1 = mvs(pm)
assert (m1, s1, v1) == (Fr(3, 5), Fr(6, 5), Fr(21, 25))
D.Q('From a PMF · a table with $c$',
    r'''$X$ has the PMF below.

| $x$ | $-1$ | $0$ | $1$ | $2$ |
|---|---|---|---|---|
| $p_X(x)$ | $0.1$ | $c$ | $0.3$ | $0.2$ |

Find (a) $c$, (b) $E[X]$, $\operatorname{Var}(X)$ and $\sigma_X$.''',
    [S(r'(a) **Find $c$:** the chances add to $1$.', r'0.1+c+0.3+0.2=1\quad\Longrightarrow\quad c=0.4'),
     S(r'(b) **Mean.**', r'E[X]=-1(0.1)+0(0.4)+1(0.3)+2(0.2)=0.6'),
     S(r'**Square:** $(-1)^2=1$, so the negative value adds, not subtracts.', r'E[X^2]=1(0.1)+0(0.4)+1(0.3)+4(0.2)=1.2'),
     S(r'**Subtract.**', r'\operatorname{Var}(X)=1.2-0.6^2=0.84'),
     S(r'**Root.**', r'\sigma_X=\sqrt{0.84}\approx' + f'{sqrt(0.84):.3f}')],
    f'$c=0.4$; $E[X]=0.6$, $\\operatorname{{Var}}(X)=0.84$, $\\sigma_X\\approx {sqrt(0.84):.3f}$', diff='introductory')

px = {x: Fr(x, 10) for x in range(1, 5)}
assert mvs(px) == (3, 10, 1)
D.Q('From a PMF · a formula',
    r'$p_X(x)=\dfrac{x}{10}$ for $x=1,2,3,4$. Find $E[X]$, $\operatorname{Var}(X)$ and $\sigma_X$.',
    [S(r'**Spot:** a PMF given as a formula. Write out the chances first.', r'p_X(1)=0.1,\quad p_X(2)=0.2,\quad p_X(3)=0.3,\quad p_X(4)=0.4'),
     S(r'**Mean.**', r'E[X]=1(0.1)+2(0.2)+3(0.3)+4(0.4)=3'),
     S(r'**Square.**', r'E[X^2]=1(0.1)+4(0.2)+9(0.3)+16(0.4)=10'),
     S(r'**Subtract.**', r'\operatorname{Var}(X)=10-3^2=1'),
     S(r'**Root.**', r'\sigma_X=\sqrt1=1')],
    r'$E[X]=3$, $\operatorname{Var}(X)=1$, $\sigma_X=1$', diff='introductory')

# ---- From a PDF
D.Q('From a PDF · a power of $x$',
    r'$f_X(x)=3x^2$ for $0\le x\le1$, and $0$ elsewhere. Find $E[X]$, $\operatorname{Var}(X)$ and $\sigma_X$.',
    [S(r'**Spot:** a PDF → integrals over $[0,1]$.'),
     S(r'**Mean.**', r'E[X]=\int_0^1x\cdot3x^2\,dx=3\cdot\frac{x^4}{4}\Big|_0^1=\frac34'),
     S(r'**Square.**', r'E[X^2]=\int_0^1x^2\cdot3x^2\,dx=3\cdot\frac{x^5}{5}\Big|_0^1=\frac35'),
     S(r'**Subtract.**', r'\operatorname{Var}(X)=\frac35-\Big(\frac34\Big)^2=\frac{48-45}{80}=\frac3{80}'),
     S(r'**Root.**', r'\sigma_X=\sqrt{3/80}\approx' + f'{sqrt(3 / 80):.3f}')],
    f'$E[X]=\\tfrac34$, $\\operatorname{{Var}}(X)=\\tfrac3{{80}}$, $\\sigma_X\\approx {sqrt(3 / 80):.3f}$', diff='introductory')

D.Q('From a PDF · a flat one',
    r'$f_X(x)=\tfrac14$ for $2\le x\le6$, and $0$ elsewhere. Find $E[X]$, $\operatorname{Var}(X)$ and $\sigma_X$.',
    [S(r'**Spot:** a PDF (flat, so uniform on $[2,6]$) → integrals.'),
     S(r'**Mean:** flat is symmetric, so the mean is the centre. Check with the integral:', r'E[X]=\int_2^6\frac x4\,dx=\frac{36-4}{8}=4'),
     S(r'**Square.**', r'E[X^2]=\int_2^6\frac{x^2}{4}\,dx=\frac{216-8}{12}=\frac{52}{3}'),
     S(r'**Subtract.** (Same as the uniform shortcut $\tfrac{(b-a)^2}{12}=\tfrac{16}{12}$.)', r'\operatorname{Var}(X)=\frac{52}3-4^2=\frac43'),
     S(r'**Root.**', r'\sigma_X=\sqrt{4/3}\approx' + f'{sqrt(4 / 3):.3f}')],
    f'$E[X]=4$, $\\operatorname{{Var}}(X)=\\tfrac43$, $\\sigma_X\\approx {sqrt(4 / 3):.3f}$')

D.Q('From a PDF · find $C$ first · Tutorial 5 Q5',
    r'$f_X(x)=Cx^2$ for $|x|\le1$, and $0$ otherwise. (a) Find $C$. (b) Find $E[X]$, $\operatorname{Var}(X)$ and $\sigma_X$.',
    [S(r'(a) **Find $c$:** total area $=1$.', r'\int_{-1}^{1}Cx^2\,dx=\frac{2C}{3}=1\quad\Longrightarrow\quad C=\frac32'),
     S(r'(b) **Mean:** $x^2$ is the same on both sides of $0$ (symmetric), so the mean is the centre.', r'E[X]=0'),
     S(r'**Square.**', r'E[X^2]=\int_{-1}^{1}\frac32x^4\,dx=\frac32\cdot\frac25=\frac35'),
     S(r'**Subtract.**', r'\operatorname{Var}(X)=\frac35-0^2=\frac35'),
     S(r'**Root.**', r'\sigma_X=\sqrt{3/5}\approx' + f'{sqrt(0.6):.3f}')],
    f'(a) $C=\\tfrac32$ (b) $E[X]=0$, $\\operatorname{{Var}}(X)=\\tfrac35$, $\\sigma_X\\approx {sqrt(0.6):.3f}$', cites=cite('T5', 1))

D.Q('From a PDF · symmetric, with a shift · Practice 03 Q3',
    r'$X$ has PDF $f_X(t)=\tfrac12\lambda e^{-\lambda|t-\gamma|}$ for all $t$. Find (a) $E[X]$, (b) $\operatorname{Var}(X)$ and $\sigma_X$.',
    [S(r'(a) **Mean:** the PDF is symmetric around $t=\gamma$ (same value at $\gamma\pm u$), so the mean is the centre.', r'E[X]=\gamma'),
     S(r'(b) Use $\operatorname{Var}(X)=E[(X-\gamma)^2]$. Let $u=t-\gamma$; both halves match, so double the right half.',
       r'\operatorname{Var}(X)=2\int_0^{\infty}u^2\cdot\frac12\lambda e^{-\lambda u}\,du=\lambda\int_0^{\infty}u^2e^{-\lambda u}\,du'),
     S(r'The exponential integral with $n=2$.', r'=\lambda\cdot\frac{2!}{\lambda^3}=\frac{2}{\lambda^2}'),
     S(r'**Root.**', r'\sigma_X=\frac{\sqrt2}{\lambda}')],
    r'(a) $E[X]=\gamma$ (b) $\operatorname{Var}(X)=\dfrac2{\lambda^2}$, $\sigma_X=\dfrac{\sqrt2}\lambda$', cites=cite('P3', 1))

# ---- From a CDF
cdf_pm = {-3: Fr(3, 8), 0: Fr(3, 8), 6: Fr(1, 4)}
cm, cs, cv = mvs(cdf_pm)
assert (cm, cs, cv) == (Fr(3, 8), Fr(99, 8), Fr(783, 64))
D.Q('From a CDF · a staircase · Practice 03 Q9',
    r'''Say if $X$ is discrete or continuous, then find $E[X]$, $\operatorname{Var}(X)$ and $\sigma_X$:

$$
F(x)=\begin{cases}0,&x<-3\\ 3/8,&-3\le x<0\\ 3/4,&0\le x<6\\ 1,&x\ge6\end{cases}
$$''',
    [S(r'**Spot:** a staircase → discrete. The **jump sizes** are the PMF.', r'p(-3)=\frac38,\quad p(0)=\frac34-\frac38=\frac38,\quad p(6)=1-\frac34=\frac14'),
     S(r'**Mean.**', r'E[X]=-3\cdot\frac38+0+6\cdot\frac14=-\frac98+\frac{12}8=\frac38'),
     S(r'**Square.**', r'E[X^2]=9\cdot\frac38+0+36\cdot\frac14=\frac{27}8+9=\frac{99}8'),
     S(r'**Subtract.**', r'\operatorname{Var}(X)=\frac{99}8-\frac9{64}=\frac{783}{64}\approx' + f'{float(cv):.3f}'),
     S(r'**Root.**', r'\sigma_X\approx' + f'{sqrt(cv):.3f}')],
    f'Discrete; $E[X]=\\tfrac38$, $\\operatorname{{Var}}(X)=\\tfrac{{783}}{{64}}\\approx {float(cv):.3f}$, $\\sigma_X\\approx {sqrt(cv):.3f}$',
    cites=cite('P3', 3))

D.Q('From a CDF · a smooth one',
    r'$F_X(x)=\dfrac{x^2}{4}$ for $0\le x\le2$ ($0$ before, $1$ after). Find $E[X]$, $\operatorname{Var}(X)$ and $\sigma_X$.',
    [S(r'**Spot:** $F_X$ rises smoothly → continuous. The **slope** is the PDF.', r'f_X(x)=\frac{d}{dx}\,\frac{x^2}{4}=\frac x2,\qquad 0\le x\le2'),
     S(r'**Mean.**', r'E[X]=\int_0^2x\cdot\frac x2\,dx=\frac{x^3}{6}\Big|_0^2=\frac86=\frac43'),
     S(r'**Square.**', r'E[X^2]=\int_0^2x^2\cdot\frac x2\,dx=\frac{x^4}{8}\Big|_0^2=2'),
     S(r'**Subtract.**', r'\operatorname{Var}(X)=2-\Big(\frac43\Big)^2=\frac{18-16}{9}=\frac29'),
     S(r'**Root.**', r'\sigma_X=\frac{\sqrt2}{3}\approx' + f'{sqrt(2) / 3:.3f}')],
    f'$E[X]=\\tfrac43$, $\\operatorname{{Var}}(X)=\\tfrac29$, $\\sigma_X\\approx {sqrt(2) / 3:.3f}$')

D.Q('From a CDF · exponential',
    r'$F_X(x)=1-e^{-2x}$ for $x\ge0$ ($0$ before). Find $E[X]$, $\operatorname{Var}(X)$ and $\sigma_X$.',
    [S(r'**Spot:** smooth → continuous. **Slope** = the PDF.', r'f_X(x)=2e^{-2x},\qquad x\ge0'),
     S(r'**Mean:** the exponential integral with $n=1$, $\lambda=2$.', r'E[X]=2\int_0^{\infty}x\,e^{-2x}\,dx=2\cdot\frac{1!}{2^2}=\frac12'),
     S(r'**Square:** $n=2$.', r'E[X^2]=2\int_0^{\infty}x^2e^{-2x}\,dx=2\cdot\frac{2!}{2^3}=\frac12'),
     S(r'**Subtract.** (Same as the exponential’s $\tfrac1{\lambda^2}$.)', r'\operatorname{Var}(X)=\frac12-\Big(\frac12\Big)^2=\frac14'),
     S(r'**Root.**', r'\sigma_X=\frac12')],
    r'$E[X]=\tfrac12$, $\operatorname{Var}(X)=\tfrac14$, $\sigma_X=\tfrac12$')


def verify():
    import sympy as sp
    x, t, u, v = sp.symbols('x t u v', real=True)
    lam, p, a, mu = sp.symbols('lambda p a mu', positive=True)
    sig = sp.Symbol('sigma', positive=True)
    k = sp.Symbol('k', integer=True, nonnegative=True)
    I = sp.integrate
    # Type 1
    assert sp.Rational(sum(range(1, 7)), 6) == sp.Rational(7, 2) and sp.Rational(sum(i * i for i in range(1, 7)), 6) == sp.Rational(91, 6)
    assert I(x / 2, (x, 0, 2)) == 1 and I(x ** 2 / 2, (x, 0, 2)) == sp.Rational(4, 3)
    assert sp.simplify(I(t * lam * sp.exp(-lam * t), (t, 0, sp.oo)) - 1 / lam) == 0
    assert I(x * sp.Rational(8, 100), (x, 0, 10)) == 4
    # Type 1: named-family table
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
        assert sp.simplify(sp.summation((1 - pv) ** k, (k, 0, sp.oo)) - 1 / pv) == 0  # tail sum
    bb = sp.Symbol('bb', positive=True)
    um = I(x / (bb), (x, a, a + bb)); uv = sp.simplify(I(x ** 2 / bb, (x, a, a + bb)) - um ** 2)
    assert sp.simplify(um - (2 * a + bb) / 2) == 0 and sp.simplify(uv - bb ** 2 / 12) == 0
    e2 = I(x ** 2 * lam * sp.exp(-lam * x), (x, 0, sp.oo))
    assert sp.simplify(e2 - 2 / lam ** 2) == 0
    gm = I(x * sp.exp(-(x - mu) ** 2 / (2 * sig ** 2)) / sp.sqrt(2 * sp.pi * sig ** 2), (x, -sp.oo, sp.oo))
    gv = I((x - mu) ** 2 * sp.exp(-(x - mu) ** 2 / (2 * sig ** 2)) / sp.sqrt(2 * sp.pi * sig ** 2), (x, -sp.oo, sp.oo))
    assert sp.simplify(gm - mu) == 0 and sp.simplify(gv - sig ** 2) == 0
    # Type 1: named-family try-it
    assert 10 * sp.Rational(3, 10) == 3 and 10 * sp.Rational(3, 10) * sp.Rational(7, 10) == sp.Rational(21, 10)
    assert I(x ** 2 / 6, (x, 2, 8)) - I(x / 6, (x, 2, 8)) ** 2 == 3
    L3 = sp.Integer(3)
    assert sp.simplify(sp.summation((k - 1) ** 2 * sp.exp(-L3) * L3 ** k / sp.factorial(k), (k, 0, sp.oo)) - 7) == 0
    # Topic 1 / Extras: CDF examples
    assert I(x * sp.diff(x ** 2, x), (x, 0, 1)) == sp.Rational(2, 3) == I(1 - t ** 2, (t, 0, 1))
    assert I(x ** 2 * sp.diff(x ** 2, x), (x, 0, 1)) - sp.Rational(4, 9) == sp.Rational(1, 18)
    assert sp.Rational(12, 5) ** 2 + sp.Rational(31, 25) == 7
    assert 1 + sp.Rational(2, 3) + sp.Rational(1, 3) == sum(sp.Rational(n, 3) for n in (1, 2, 3)) == 2
    assert I(x * sp.Rational(3, 2) * x ** 2, (x, -1, 1)) == 0 and I(x ** 2 * sp.exp(-x), (x, 0, sp.oo)) == 2
    assert 9 * 10 - 12 * 3 + 4 == 58
    # Practice questions
    C = sp.Symbol('C')
    Cv = sp.solve(I(C * x ** 2, (x, -1, 1)) - 1, C)[0]
    assert Cv == sp.Rational(3, 2)
    assert I(Cv * x ** 3, (x, -1, 1)) == 0 and I(Cv * x ** 4, (x, -1, 1)) == sp.Rational(3, 5)
    assert I(sp.Abs(x) * Cv * x ** 2, (x, -1, 1)) == sp.Rational(3, 4) and 9 * sp.Rational(3, 5) == sp.Rational(27, 5)
    gam = sp.Symbol('gamma', real=True)
    lap = lam / 2 * sp.exp(-lam * sp.Abs(t - gam))
    lv = I(u ** 2 * lam * sp.exp(-lam * u), (u, 0, sp.oo))  # 2 * (half the integral) = lam * int u^2 e^{-lam u}
    assert sp.simplify(lv - 2 / lam ** 2) == 0
    assert sp.simplify(I(lap.subs(gam, 0), (t, -sp.oo, sp.oo)) - 1) == 0
    assert sp.simplify(I(t * lap.subs(gam, 0), (t, -sp.oo, sp.oo))) == 0
    assert sp.simplify(I(sp.exp(-lam * t), (t, 0, sp.oo)) - 1 / lam) == 0
    die = [sp.Rational(1, 6)] * 6
    assert sum(k * k * w for k, w in zip(range(1, 7), die)) - sp.Rational(7, 2) ** 2 == sp.Rational(35, 12)
    assert sp.Rational(16, 2) * sp.Rational(1, 2) + sp.Rational(36, 2) * sp.Rational(1, 2) == 13
    assert I(x ** 2 / 2, (x, 0, 2)) - I(x / 2, (x, 0, 2)) ** 2 == sp.Rational(1, 3)
    # new practice: 3x^2, flat 1/4 on [2,6], x^2/4 CDF, 1-e^{-2x} CDF
    def mv(f, lo, hi):
        m = I(x * f, (x, lo, hi))
        return m, I(x ** 2 * f, (x, lo, hi)) - m ** 2
    assert mv(3 * x ** 2, 0, 1) == (sp.Rational(3, 4), sp.Rational(3, 80))
    assert mv(sp.Rational(1, 4), 2, 6) == (4, sp.Rational(4, 3))
    assert mv(sp.diff(x ** 2 / 4, x), 0, 2) == (sp.Rational(4, 3), sp.Rational(2, 9))
    assert mv(sp.diff(1 - sp.exp(-2 * x), x), 0, sp.oo) == (sp.Rational(1, 2), sp.Rational(1, 4))
    print('q3 verify ok')


if __name__ == '__main__':
    verify()
    D.save()
