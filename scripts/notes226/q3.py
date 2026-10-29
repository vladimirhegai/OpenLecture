r"""Test 2 - Question 3: expected values, variances, properties of expectation and variance (Lectures 11-13).

Layout (REWRITE_PLAN.md): you'll see -> the move -> Case 1-5 (formula, short example, full example in a
closed card, shortcut card) -> practice. Step words: Spot, Mean, Square, Subtract, Root; for the rules: Expand, Swap,
Plug in (the same words in every solution).
"""
from fractions import Fraction as Fr
from math import pi, sqrt

from lib226 import Doc, S, cite, sci

D = Doc('q3', 'Test 2 - Question 3', ['expected_value', 'variance', 'standard_deviation', 'linearity', 'moments'])

D.P(r'**Lectures 11–13.** The mean (the long-run average) and the variance (the spread) of a random variable.',
    cites=cite('L11', 6) + cite('L12', 6) + cite('L13', 2))

# =====================================================================================================
D.H('Question 3 in plain words')
D.P(r'**You’ll see:** a PMF, a PDF, a CDF, a named family, or just “$E[X]=3$, $\operatorname{Var}(X)=9$”. Then “find $E[X]$, $\operatorname{Var}(X)$, $\sigma_X$”.')
D.P(r'**The move: four steps, every time.**')
D.L([r'**Mean:** each value × its chance, then add (a sum for a PMF, an integral for a PDF).',
     r'**Square:** the same, with $x^2$ in place of $x$. That’s $E[X^2]$.',
     r'**Subtract:** $\operatorname{Var}(X)=E[X^2]-(E[X])^2$.',
     r'**Root:** $\sigma_X=\sqrt{\operatorname{Var}(X)}$.'], ordered=True)
D.EQ(r'E[X]=\sum_x x\,p_X(x)\quad\text{or}\quad\int x\,f_X(x)\,dx,\qquad \operatorname{Var}(X)=E[X^2]-\big(E[X]\big)^2', cites=cite('L12', 2) + cite('L12', 6))
D.P(r'**Short example:** a die. $E[X]=3.5$, $E[X^2]=\tfrac{91}{6}$:')
D.EQ(r'\operatorname{Var}(X)=\frac{91}{6}-3.5^2=\frac{35}{12}\approx2.92,\qquad \sigma_X\approx1.71')
D.P(r'**Which case?**')
D.T(['You’re given…', 'Go to'],
    [['a PMF (a list of values and chances)', 'Case 1'],
     ['a PDF $f_X(x)$', 'Case 2'],
     ['a CDF $F_X(x)$', 'Case 3'],
     ['“$X$ is Poisson / uniform / …”', 'Case 4'],
     [r'only $E[X]$ and $\operatorname{Var}(X)$', 'Case 5']])
D.CO('warning', r'**$E[X^2]\ne(E[X])^2$.** Square **inside** the sum or integral, not after. A die: $E[X^2]=\tfrac{91}{6}\approx15.17$, but $3.5^2=12.25$.',
     cites=cite('L12', 2))

# =====================================================================================================
D.H('Case 1: from a PMF')
D.P(r'**You’ll see:** a table of values and chances, or an experiment you turn into one.')
D.EQ(r'E[X]=\sum_x x\,p_X(x),\qquad E[X^2]=\sum_x x^2\,p_X(x)', cites=cite('L11', 7))
D.P(r'**Short example** (Lecture 12): $X=4$ V or $6$ V, each half the time:')
D.EQ(r'E[X]=4(0.5)+6(0.5)=5,\qquad E[X^2]=16(0.5)+36(0.5)=26')
D.EQ(r'\operatorname{Var}(X)=26-5^2=1\ \text{V}^2,\qquad \sigma_X=1\ \text{V}')
D.CARD(r'Full example (Lecture 11): a fair die, $\;X$ = the number',
       [(r'**Mean:** each face has chance $\tfrac16$.', r'E[X]=\frac16(1+2+3+4+5+6)=\frac{21}{6}=3.5'),
        (r'**Square:** square each value **inside** the sum.', r'E[X^2]=\frac16(1+4+9+16+25+36)=\frac{91}{6}'),
        (r'**Subtract.**', r'\operatorname{Var}(X)=\frac{91}{6}-\Big(\frac72\Big)^2=\frac{182-147}{12}=\frac{35}{12}'),
        (r'**Root.**', r'\sigma_X=\sqrt{35/12}\approx1.71')],
       r'E[X]=3.5,\quad \operatorname{Var}(X)=\frac{35}{12},\quad \sigma_X\approx1.71', cites=cite('L11', 8) + cite('L12', 2))
D.CARD(r'Any function: $\;E[g(X)]=\sum g(x)\,p_X(x)$',
       [(r'Put $g(x)$ in place of $x$. Example: a voltage $X=4$ or $6$ V (half each) across $R=2\ \Omega$: average power $E[X^2/R]$.',
         r'E\Big[\frac{X^2}{2}\Big]=\frac{16}{2}(0.5)+\frac{36}{2}(0.5)=13\ \text{W}')], numbered=False, cites=cite('L12', 2))
D.TRY('Case 1 · A binary random variable · Tutorial 5 Q1',
      r'$X$ is $0$ with probability $p$ and $1$ with probability $1-p$. Find $E[X]$, $\operatorname{Var}(X)$ and $E[X^5]$.',
      [S(r'**Spot:** a PMF with two values → Case 1.'),
       S(r'**Mean.**', r'E[X]=0\cdot p+1\cdot(1-p)=1-p'),
       S(r'**Square:** $0^n=0$ and $1^n=1$, so $X^n=X$ for any power.', r'E[X^2]=E[X^5]=E[X]=1-p'),
       S(r'**Subtract.**', r'\operatorname{Var}(X)=(1-p)-(1-p)^2=(1-p)\,p')],
      r'$E[X]=1-p$, $\operatorname{Var}(X)=p(1-p)$, $E[X^5]=1-p$.', diff='introductory', cites=cite('T5', 1))

# =====================================================================================================
D.H('Case 2: from a PDF')
D.P(r'**You’ll see:** a formula $f_X(x)$. Same four steps, with integrals over the range where $f_X\ne0$:')
D.EQ(r'E[X]=\int x\,f_X(x)\,dx,\qquad E[X^2]=\int x^2\,f_X(x)\,dx', cites=cite('L12', 2))
D.P(r'**Short example:** $X$ uniform on $[0,2]$, $f_X=\tfrac12$:')
D.EQ(r'E[X]=\int_0^2\frac x2\,dx=1,\qquad E[X^2]=\int_0^2\frac{x^2}{2}\,dx=\frac43')
D.EQ(r'\operatorname{Var}(X)=\frac43-1=\frac13')
D.CARD(r'Full example (Practice 03 Q2): exponential, $\;f_X(t)=\lambda e^{-\lambda t}$, $t\ge0$',
       [(r'**Mean:** integrate over $t\ge0$. Use the shortcut card below with $n=1$.', r'E[X]=\lambda\int_0^{\infty}t\,e^{-\lambda t}\,dt=\lambda\cdot\frac{1!}{\lambda^2}=\frac1\lambda'),
        (r'**Square:** the shortcut with $n=2$.', r'E[X^2]=\lambda\cdot\frac{2!}{\lambda^3}=\frac{2}{\lambda^2}'),
        (r'**Subtract.**', r'\operatorname{Var}(X)=\frac{2}{\lambda^2}-\frac{1}{\lambda^2}=\frac{1}{\lambda^2}'),
        (r'**Root.** (3 customers per minute → mean gap $\tfrac13$ min.)', r'\sigma_X=\frac1\lambda')],
       r'E[X]=\frac1\lambda,\qquad \operatorname{Var}(X)=\frac{1}{\lambda^2}', cites=cite('P3', 1))
D.CARD(r'Shortcut: $\;\displaystyle\int_0^{\infty}x^n\,e^{-\lambda x}\,dx=\frac{n!}{\lambda^{n+1}}$',
       [(r'Skips integrating by parts. $n=1$:', r'\int_0^\infty x\,e^{-2x}\,dx=\frac{1}{4}'),
        (r'$n=2$:', r'\int_0^\infty x^2\,e^{-x}\,dx=\frac{2}{1}=2')], numbered=False)
D.CARD(r'Shortcut: a symmetric PDF → the mean is the centre',
       [(r'If $f_X$ looks the same on both sides of $c$, then $E[X]=c$. No integral.', r'f_X(t)=\tfrac12\lambda e^{-\lambda|t-\gamma|}\quad\Longrightarrow\quad E[X]=\gamma'),
        (r'Same reason: an odd function ($x$, $x^3$) integrated over $[-a,a]$ gives $0$.', r'\int_{-1}^{1}x\cdot\frac32x^2\,dx=0')], numbered=False)
D.CARD(r'Mixed $X$ (a jump and a density): add both parts',
       [(r'Lecture 11 signal: $X=0$ with chance $0.2$, otherwise uniform on $(0,10)$, density $0.08$.', ''),
        (r'**Mean**, jump part.', r'0\cdot0.2=0'),
        (r'**Mean**, density part.', r'\int_0^{10}x\,(0.08)\,dx=0.08\cdot\frac{10^2}{2}=4'),
        (r'Add.', r'E[X]=0+4=4')], cites=cite('L11', 4))

# =====================================================================================================
D.H('Case 3: from a CDF')
D.P(r'**You’ll see:** $F_X(x)$ instead of a PMF or PDF. Turn it into one, then Case 1 or 2:')
D.L([r'**Staircase CDF** (discrete): the **jump sizes** are the PMF → Case 1.',
     r'**Smooth CDF** (continuous): the **slope** is the PDF, $f_X=F_X^{\prime}$ → Case 2.'], cites=cite('L9', 4))
D.P(r'**Shortcut for $X\ge0$** (the tail formula): skip the PDF.')
D.EQ(r'E[X]=\int_0^{\infty}\big(1-F_X(t)\big)\,dt\qquad\qquad E[N]=\sum_{k=0}^{\infty}P(N>k)\ \ (\text{whole numbers})', cites=cite('P3', 1))
D.P(r'**Short example:** exponential, $1-F_X(t)=e^{-\lambda t}$:')
D.EQ(r'E[X]=\int_0^{\infty}e^{-\lambda t}\,dt=\frac1\lambda')
D.CARD(r'Full example: $\;F_X(x)=x^2$ on $[0,1]$. Find $E[X]$ two ways',
       [(r'**Way 1:** the slope is the PDF.', r'f_X(x)=2x,\qquad 0\le x\le1'),
        (r'**Mean** from the PDF.', r'E[X]=\int_0^1x\cdot2x\,dx=\frac23'),
        (r'**Way 2:** the tail formula. $1-F=0$ after $x=1$.', r'E[X]=\int_0^1(1-t^2)\,dt=1-\frac13=\frac23')],
       r'E[X]=\frac23\ \text{ both ways}')

# =====================================================================================================
D.H('Case 4: a named family (read it off)')
D.P(r'**You’ll see:** “$X$ is Binomial / Poisson / uniform / …”. Don’t integrate: each family’s mean and variance are known. Open a card:')
D.CARD(r'Bernoulli$(p)$: $\;E=p$, $\;\operatorname{Var}=p(1-p)$',
       [(r'One yes/no try, $1$ with chance $p$. Example $p=0.3$:', r'E[X]=0.3,\qquad \operatorname{Var}(X)=0.3\cdot0.7=0.21')], numbered=False)
D.CARD(r'Binomial$(n,p)$: $\;E=np$, $\;\operatorname{Var}=np(1-p)$',
       [(r'$n$ tries, count successes. Example $n=10$, $p=0.3$:', r'E[X]=3,\qquad \operatorname{Var}(X)=10(0.3)(0.7)=2.1')], numbered=False)
D.CARD(r'Geometric: $\;E=\dfrac1p$ (or $\dfrac{1-p}{p}$), $\;\operatorname{Var}=\dfrac{1-p}{p^2}$',
       [(r'Counting tries until the first success ($k=1,2,\dots$):', r'E[X]=\frac1p'),
        (r'Counting failures before it ($k=0,1,\dots$), one less:', r'E[N]=\frac1p-1=\frac{1-p}{p}'),
        (r'Same variance both ways. Example $p=0.2$, tries:', r'E[X]=5,\qquad \operatorname{Var}(X)=\frac{0.8}{0.04}=20')], numbered=False)
D.CARD(r'Poisson$(\lambda)$: $\;E=\lambda$, $\;\operatorname{Var}=\lambda$',
       [(r'Mean and variance are the same number. Example $\lambda=3$:', r'E[X]=3,\qquad \operatorname{Var}(X)=3')], numbered=False)
D.CARD(r'Uniform$(a,b)$: $\;E=\dfrac{a+b}{2}$, $\;\operatorname{Var}=\dfrac{(b-a)^2}{12}$',
       [(r'The middle, and the length squared over 12. Example $U(2,8)$:', r'E[X]=5,\qquad \operatorname{Var}(X)=\frac{36}{12}=3')], numbered=False)
D.CARD(r'Exponential$(\lambda)$: $\;E=\dfrac1\lambda$, $\;\operatorname{Var}=\dfrac{1}{\lambda^2}$',
       [(r'Example $\lambda=0.25$ per minute:', r'E[X]=4\text{ min},\qquad \operatorname{Var}(X)=16')], numbered=False)
D.CARD(r'Gaussian $N(\mu,\sigma^2)$: $\;E=\mu$, $\;\operatorname{Var}=\sigma^2$',
       [(r'Already in the name. Example $N(12,4)$:', r'E[X]=12,\qquad \sigma_X=2')], numbered=False, cites=cite('L12', 8))
D.P(r'**Need $E[X^2]$?** Turn the variance around:')
D.EQ(r'E[X^2]=\operatorname{Var}(X)+\big(E[X]\big)^2\qquad\text{Poisson}(3):\ E[X^2]=3+9=12')
D.TRY('Case 4 · Three families',
      r'(a) $X\sim$ Binomial$(10,\,0.3)$: find $E[X]$ and $\operatorname{Var}(X)$. '
      r'(b) $X\sim$ Uniform$(2,8)$: find $\operatorname{Var}(X)$ and $\sigma_X$. '
      r'(c) $X\sim$ Poisson$(3)$: find $E[(X-1)^2]$.',
      [S(r'(a) **Spot:** Binomial → $np$ and $np(1-p)$.', r'E[X]=10(0.3)=3,\qquad \operatorname{Var}(X)=10(0.3)(0.7)=2.1'),
       S(r'(b) **Spot:** uniform → $\frac{(b-a)^2}{12}$. **Root.**', r'\operatorname{Var}(X)=\frac{6^2}{12}=3,\qquad \sigma_X=\sqrt3\approx1.732'),
       S(r'(c) **Spot:** Poisson. **Swap:** $E[X^2]=\lambda+\lambda^2=12$. **Expand** (Case 5).', r'E[(X-1)^2]=E[X^2]-2E[X]+1=12-6+1=7')],
      r'(a) $3$, $2.1$ (b) $3$, $\sqrt3\approx1.732$ (c) $7$', diff='introductory')

# =====================================================================================================
D.H('Case 5: only E[X] and Var(X) given (the rules)')
D.P(r'**You’ll see:** “$E[X]=3$, $\operatorname{Var}(X)=9$. Find $E[(2-X)^2]$” or “find $\operatorname{Var}(2X-3)$”. No PMF or PDF needed.')
D.P(r'**The move:** two rules.')
D.EQ(r'E[aX+b]=a\,E[X]+b\qquad\qquad \operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)', cites=cite('L12', 5) + cite('L12', 9))
D.L([r'**Expand** any square, like $(2-X)^2$, then take $E$ of each term.',
     r'**Swap** in $E[X^2]=\operatorname{Var}(X)+(E[X])^2$ wherever $E[X^2]$ appears.',
     r'**Plug in.** For Var: the $+b$ drops out, the $a$ gets squared.'], ordered=True)
D.P(r'**Short example:** $\operatorname{Var}(X)=9$:')
D.EQ(r'\operatorname{Var}(2X-3)=2^2\cdot9=36,\qquad \operatorname{Var}(-X)=\operatorname{Var}(X),\qquad \sigma_{aX+b}=|a|\,\sigma_X')
e13a = 4 - 4 * 3 + (9 + 3 ** 2)
assert e13a == 10
D.CARD(r'Full example (Lecture 13): $\;E[X]=3$, $\;\operatorname{Var}(X)=9$. Find $E[(2-X)^2]$ and $\operatorname{Var}(2X-3)$',
       [(r'**Expand**, then take $E$ of each term.', r'E[(2-X)^2]=E[4-4X+X^2]=4-4E[X]+E[X^2]'),
        (r'**Swap** for $E[X^2]$.', r'E[X^2]=9+3^2=18'),
        (r'**Plug in.**', r'E[(2-X)^2]=4-12+18=10'),
        (r'Var: the $-3$ drops out, the $2$ gets squared.', r'\operatorname{Var}(2X-3)=2^2\cdot9=36')],
       r'E[(2-X)^2]=10,\qquad \operatorname{Var}(2X-3)=36', cites=cite('L13', 3))
D.CARD(r'Moments: $\;E[X^n]$ (raw), $\;E[(X-\mu)^n]$ (central)',
       [(r'The $n$th moment is $E[X^n]$: $E[X]$ is the 1st, $E[X^2]$ the 2nd.', ''),
        (r'The variance is the 2nd **central** moment: distances from the mean.', r'\operatorname{Var}(X)=E\big[(X-\mu_X)^2\big]')],
       numbered=False, cites=cite('L13', 4))
D.CARD(r'Chebyshev and Markov (Practice 03, not in the lectures)',
       [(r'**Chebyshev:** far from the mean is unlikely when the variance is small.', r'P\big(|Y-\mu_Y|\ge\varepsilon\big)\le\frac{\operatorname{Var}(Y)}{\varepsilon^2}'),
        (r'Example: $\operatorname{Var}=1$, $\varepsilon=2$.', r'P\big(|Y-\mu|\ge2\big)\le\frac14'),
        (r'**Markov**, for $Y\ge0$:', r'P(Y\ge a)\le\frac{E[Y]}{a}')], numbered=False, cites=cite('P3', 3))
D.TRY('Case 5 · Given only the mean and variance · Tutorial 5 Q2',
      r'$X\ge0$ has $E[X]=3$ and $\operatorname{Var}(X)=1$. Find (a) $E[(3X-2)^2]$, (b) $\operatorname{Var}(2X+1)$.',
      [S(r'**Spot:** only $E$ and Var → Case 5. **Swap** first.', r'E[X^2]=1+3^2=10'),
       S(r'(a) **Expand**, then take $E$ of each term.', r'E[(3X-2)^2]=9E[X^2]-12E[X]+4'),
       S(r'**Plug in.**', r'9(10)-12(3)+4=58'),
       S(r'(b) The $+1$ drops out, the $2$ gets squared.', r'\operatorname{Var}(2X+1)=4\cdot1=4')],
      r'(a) $58$ (b) $4$', diff='introductory', cites=cite('T5', 1))

# =====================================================================================================
D.H('Practice Questions')
D.CO('tip', r'''**Question 3 is always these cases, in parts (a)–(c).** Run **Mean → Square → Subtract → Root**:

1. **PMF:** $\sum x\,p$ and $\sum x^2p$.
2. **PDF:** $\int x\,f$ and $\int x^2f$ (symmetric → mean = centre; $\int_0^\infty x^ne^{-\lambda x}=\frac{n!}{\lambda^{n+1}}$).
3. **CDF:** jumps → PMF, slope → PDF; or the tail formula for $X\ge0$.
4. **Named family:** read the card.
5. **Only $E$ and Var:** Expand → Swap $E[X^2]=\text{Var}+\mu^2$ → Plug in; $\text{Var}(aX+b)=a^2\text{Var}(X)$.''')
D.P('Test-style, easy → hard. Solve on paper first, then open the solution.')

pm = {-1: Fr(1, 10), 0: Fr(2, 5), 1: Fr(3, 10), 2: Fr(1, 5)}
assert sum(pm.values()) == 1
m1 = sum(x * p for x, p in pm.items())
s1 = sum(x * x * p for x, p in pm.items())
v1 = s1 - m1 ** 2
assert (m1, s1, v1) == (Fr(3, 5), Fr(6, 5), Fr(21, 25))
assert (5 - 2 * m1, 4 * v1) == (Fr(19, 5), Fr(84, 25))
D.Q('Case 1 + 5 · PMF table',
    r'''$X$ has the PMF below.

| $x$ | $-1$ | $0$ | $1$ | $2$ |
|---|---|---|---|---|
| $p_X(x)$ | $0.1$ | $c$ | $0.3$ | $0.2$ |

Find (a) $c$, (b) $E[X]$ and $\operatorname{Var}(X)$, (c) $E[5-2X]$ and $\operatorname{Var}(5-2X)$.''',
    [S(r'(a) **Find $c$:** the chances add to $1$.', r'0.1+c+0.3+0.2=1\quad\Longrightarrow\quad c=0.4'),
     S(r'(b) **Type:** a PMF → Case 1. **Mean.**', r'E[X]=-1(0.1)+0+1(0.3)+2(0.2)=0.6'),
     S(r'**Square.**', r'E[X^2]=1(0.1)+0+1(0.3)+4(0.2)=1.2'),
     S(r'**Subtract.**', r'\operatorname{Var}(X)=1.2-0.6^2=0.84'),
     S(r'(c) **Rules** (Case 5): the $5$ drops out of Var, the $-2$ gets squared.', (r'E[5-2X]=5-2(0.6)=3.8', r'\operatorname{Var}(5-2X)=4(0.84)=3.36'))],
    r'$c=0.4$; $E[X]=0.6$, $\operatorname{Var}(X)=0.84$; $E[5-2X]=3.8$, $\operatorname{Var}(5-2X)=3.36$.', diff='introductory')

D.Q('Case 4 + 5 · Gaussian · Tutorial 5 Q4',
    r'$X$ is normal with mean $12$ and variance $4$. (a) Find $c$ so that $P(X\ge c)=0.5$. (b) Find $E[X^2]$.',
    [S(r'**Type:** named family (Gaussian) → Case 4: $E[X]=12$, $\operatorname{Var}(X)=4$.'),
     S(r'(a) The bell is symmetric around its mean, so half the area is above $12$.', r'c=\mu=12'),
     S(r'(b) **Swap** (Case 5).', r'E[X^2]=\operatorname{Var}(X)+\mu^2=4+144=148')],
    r'(a) $c=12$ (b) $E[X^2]=148$', diff='introductory', cites=cite('T5', 1))

D.Q('Case 5 · Prove the Var rule · Practice 03 Q4',
    r'Show that $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$ for any constants $a,b$. Use $\operatorname{Var}(Y)=E\big[(Y-E[Y])^2\big]$.',
    [S(r'**Mean** of $Y=aX+b$, with the first rule.', r'E[Y]=a\,E[X]+b'),
     S(r'**Subtract** it from $Y$: the $b$ cancels.', r'Y-E[Y]=aX+b-a\,E[X]-b=a\,(X-E[X])'),
     S(r'**Square** and take $E$: the constant $a^2$ comes out.', (r'\operatorname{Var}(Y)=E\big[a^2(X-E[X])^2\big]', r'=a^2\,E\big[(X-E[X])^2\big]=a^2\operatorname{Var}(X)'))],
    r'Shown: $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$, so $\sigma_{aX+b}=|a|\sigma_X$.', diff='introductory',
    cites=cite('L13', 2) + cite('P3', 1))

cans = {'A': 140, 'B': 112, 'C': 125, 'D': 183}
tot = sum(cans.values())
Ex = Fr(tot, 4)
sq = sum(m * m for m in cans.values())
Ey = Fr(sq, tot)
assert tot == 560 and Ex == 140 and abs(float(Ey) - 145.10) < 0.01
D.Q('Case 1 · Mars canisters · Practice 03 Q6',
    r'A rover brings back 560 g of material in four canisters A, B, C, D holding $140$, $112$, $125$ and $183$ g. '
    r'First, pick a **canister** at random (each $\tfrac14$); $x$ = grams in it. '
    r'Then, pick **one gram** at random from all 560 g; $y$ = grams in the canister it came from. '
    r'(a) Which should be larger, $E[x]$ or $E[y]$? Why? (b) Compute both.',
    [S(r'**Type:** two PMFs → Case 1. The difference is the chances.'),
     S(r'(a) A random gram lands in a big canister more often: each canister gets chance (its mass)/560. So expect $E[y]>E[x]$.',
       r'P(y=m)=\frac{m}{560}'),
     S(r'(b) **Mean** of $x$: equal chances.', r'E[x]=\frac14(140+112+125+183)=140\text{ g}'),
     S(r'**Mean** of $y$: each mass $m$ times its chance $\frac{m}{560}$.',
       r'E[y]=\frac{140^2+112^2+125^2+183^2}{560}=\frac{' + str(sq) + r'}{560}\approx' + f'{float(Ey):.2f}' + r'\text{ g}')],
    f'$E[x]=140$ g, $E[y]\\approx {float(Ey):.2f}$ g. Picking by the gram favours the big canisters.', cites=cite('P3', 1))

D.Q('Case 2 + 5 · $E[g(X)]$ from a PDF · Tutorial 5 Q5',
    r'$f_X(x)=Cx^2$ for $|x|\le1$, and $0$ otherwise. (a) Find $C$. (b) Find $E[X]$ and $\operatorname{Var}(X)$. '
    r'(c) Let $Y=|X|$. Find $E[Y]$, $E[Y^2]$ and $\operatorname{Var}(3X-1)$.',
    [S(r'(a) **Find $c$:** total area $=1$.', r'\int_{-1}^{1}Cx^2\,dx=\frac{2C}{3}=1\quad\Longrightarrow\quad C=\frac32'),
     S(r'(b) **Type:** a PDF → Case 2. **Mean:** symmetric around $0$ (shortcut).', r'E[X]=0'),
     S(r'**Square.**', r'E[X^2]=\int_{-1}^{1}\frac32x^4\,dx=\frac32\cdot\frac25=\frac35'),
     S(r'**Subtract.**', r'\operatorname{Var}(X)=\frac35-0^2=\frac35'),
     S(r'(c) $E[g(X)]$ with $g(x)=|x|$. Both halves match, so double the right half.', r'E[Y]=2\int_0^1 x\cdot\frac32x^2\,dx=3\cdot\frac14=\frac34'),
     S(r'$|X|^2=X^2$, so no new work.', r'E[Y^2]=E[X^2]=\frac35'),
     S(r'**Rules** (Case 5): the $-1$ drops out, the $3$ gets squared.', r'\operatorname{Var}(3X-1)=9\cdot\frac35=\frac{27}{5}')],
    r'(a) $C=\tfrac32$ (b) $E[X]=0$, $\operatorname{Var}(X)=\tfrac35$ (c) $E[Y]=\tfrac34$, $E[Y^2]=\tfrac35$, $\operatorname{Var}(3X-1)=\tfrac{27}5$',
    cites=cite('T5', 1))

cdf_pm = {-3: Fr(3, 8), 0: Fr(3, 8), 6: Fr(1, 4)}
cm = sum(x * p for x, p in cdf_pm.items())
cs = sum(x * x * p for x, p in cdf_pm.items())
cv = cs - cm ** 2
assert (cm, cs, cv) == (Fr(3, 8), Fr(99, 8), Fr(783, 64))
D.Q('Case 3 · Variance from a CDF · Practice 03 Q9',
    r'''Find the variance and standard deviation of $X$, and say if $X$ is discrete or continuous:

$$
F(x)=\begin{cases}0,&x<-3\\ 3/8,&-3\le x<0\\ 3/4,&0\le x<6\\ 1,&x\ge6\end{cases}
$$''',
    [S(r'**Type:** a CDF → Case 3. It’s a staircase, so discrete: the **jump sizes** are the PMF.', r'p(-3)=\frac38,\quad p(0)=\frac38,\quad p(6)=\frac14'),
     S(r'**Mean.**', r'E[X]=-3\cdot\frac38+0+6\cdot\frac14=-\frac98+\frac{12}8=\frac38'),
     S(r'**Square.**', r'E[X^2]=9\cdot\frac38+0+36\cdot\frac14=\frac{27}8+9=\frac{99}8'),
     S(r'**Subtract.**', r'\operatorname{Var}(X)=\frac{99}8-\frac9{64}=\frac{783}{64}\approx' + f'{float(cv):.3f}'),
     S(r'**Root.**', r'\sigma_X\approx' + f'{sqrt(cv):.3f}')],
    f'Discrete; $\\operatorname{{Var}}(X)=\\tfrac{{783}}{{64}}\\approx {float(cv):.3f}$, $\\sigma_X\\approx {sqrt(cv):.3f}$',
    cites=cite('P3', 3))

D.Q('Case 2 · Mean by symmetry, then Var · Practice 03 Q3',
    r'$X$ has PDF $f_X(t)=\tfrac12\lambda e^{-\lambda|t-\gamma|}$ for all $t$. (a) Find $E[X]$. (b) Find $\operatorname{Var}(X)$.',
    [S(r'**Type:** a PDF → Case 2. (a) **Mean:** symmetric around $t=\gamma$ (same value at $\gamma\pm u$).', r'E[X]=\gamma'),
     S(r'(b) Use the definition $E[(X-\gamma)^2]$. Let $u=t-\gamma$; both halves match, so double the right half.',
       r'\operatorname{Var}(X)=2\int_0^{\infty}u^2\cdot\frac12\lambda e^{-\lambda u}\,du=\lambda\int_0^{\infty}u^2e^{-\lambda u}\,du'),
     S(r'**Shortcut** with $n=2$.', r'=\lambda\cdot\frac{2!}{\lambda^3}=\frac{2}{\lambda^2}')],
    r'(a) $E[X]=\gamma$ (b) $\operatorname{Var}(X)=\dfrac2{\lambda^2}$', cites=cite('P3', 1))

pe = 0.03
EN = (1 - pe) / pe
pmax = 1 - 0.99 ** (1 / 1000)
assert abs(EN - 97 / 3) < 1e-12 and abs((1 - pmax) ** 1000 - 0.99) < 1e-12
D.Q('Case 4 · Geometric · Tutorial 6 Q7',
    r'Spirit sends an image pixel by pixel. Each pixel is wrong with probability $p=0.03$, independently. '
    r'(a) Find the PMF of $N$, the number of good pixels before the next bad one. (b) Find $E[N]$. '
    r'(c) A new rover needs a 99% chance that **at least 1000** pixels arrive correctly before a bad one. How small must $p$ be?',
    [S(r'(a) **Spot:** $k$ good pixels, then a bad one → Geometric, counting failures ($k=0,1,\dots$).', r'P(N=k)=(1-p)^k\,p=(0.97)^k(0.03),\quad k=0,1,2,\dots'),
     S(r'(b) **Read it off** the Geometric card (failures version).', r'E[N]=\frac{1-p}{p}=\frac{0.97}{0.03}\approx' + f'{EN:.2f}'),
     S(r'(c) “At least 1000 good first” means the first 1000 pixels are all good.', r'P(N\ge1000)=(1-p)^{1000}\ge0.99'),
     S(r'Solve for $p$.', r'p\le1-0.99^{1/1000}\approx' + sci(pmax))],
    f'(a) $(0.97)^k(0.03)$ (b) $E[N]\\approx {EN:.2f}$ (c) $p\\le {sci(pmax)}$', cites=cite('T6', 1))

D.Q('Case 3 · The mean from the CDF · Practice 03 Q1 / Tutorial 5 Q3',
    r'(a) $X\ge0$ is continuous with CDF $F_X$. Show that $E[X]=\displaystyle\int_0^{\infty}\big(1-F_X(t)\big)\,dt$ '
    r'(assume $t\,(1-F_X(t))\to0$ as $t\to\infty$). Use it to find the mean of an exponential. '
    r'(b) Use the whole-number version $E[N]=\sum_{k\ge0}P(N>k)$ to find the mean of a Geometric$(p)$ on $k=1,2,\dots$',
    [S(r'(a) **By parts:** $u=1-F_X(t)$, $dv=dt$, so $du=-f_X(t)\,dt$ and $v=t$.',
       r'\int_0^{\infty}(1-F_X(t))\,dt=\Big[t\,(1-F_X(t))\Big]_0^{\infty}+\int_0^{\infty}t\,f_X(t)\,dt'),
     S(r'The bracket is $0$ at both ends.', r'=0+E[X]'),
     S(r'**Exponential:** $1-F_X(t)=e^{-\lambda t}$.', r'E[X]=\int_0^{\infty}e^{-\lambda t}\,dt=\frac1\lambda'),
     S(r'If $X$ can be negative (Tutorial 5 Q3), the same by-parts on $(-\infty,0]$ subtracts one more piece.',
       r'E[X]=\int_0^{\infty}(1-F_X)\,dt-\int_{-\infty}^{0}F_X\,dt'),
     S(r'(b) $N>k$ means the first $k$ tries failed. Geometric series.', r'E[N]=\sum_{k=0}^{\infty}(1-p)^k=\frac{1}{1-(1-p)}=\frac1p')],
    r'(a) Shown; exponential mean $\tfrac1\lambda$ (b) $E[N]=\tfrac1p$', diff='advanced',
    cites=cite('T5', 1) + cite('P3', 1))

V6 = 4 / pi - 1
assert abs(2 / pi - 0.63662) < 1e-5
D.Q('Case 2 + 5 · Find the constants, then the variance · Tutorial 6 Q6',
    r'''$X$ has PDF

$$
f_X(x)=\frac{C}{1+(x+K)^2},\qquad -K-1\le x\le -K+1,
$$

and $0$ otherwise, where $C>0$ and $K$ are constants. (a) Find $C$ and $K$ so that $E[X]=5$. (b) Find $\operatorname{Var}(X)$.''',
    [S(r'**Shift:** let $u=x+K$, so $u$ runs from $-1$ to $1$.', r'f_U(u)=\frac{C}{1+u^2},\qquad X=U-K'),
     S(r'(a) **Find $c$:** total area $=1$.', r'C\big[\arctan u\big]_{-1}^{1}=C\cdot\frac{\pi}{2}=1\quad\Longrightarrow\quad C=\frac{2}{\pi}'),
     S(r'**Mean:** $f_U$ is symmetric around $0$, so $E[U]=0$. Then the rule $E[U-K]=E[U]-K$.', r'E[X]=-K=5\quad\Longrightarrow\quad K=-5'),
     S(r'(b) A shift doesn’t change Var (Case 5), and $E[U]=0$.', r'\operatorname{Var}(X)=\operatorname{Var}(U)=E[U^2]'),
     S(r'**Square:** write $\frac{u^2}{1+u^2}=1-\frac{1}{1+u^2}$.',
       r'E[U^2]=\frac2\pi\int_{-1}^{1}\Big(1-\frac{1}{1+u^2}\Big)du=\frac2\pi\Big(2-\frac\pi2\Big)=\frac4\pi-1\approx' + f'{V6:.4f}')],
    r'(a) $C=\tfrac2\pi$, $K=-5$ (so $X\in[4,6]$) (b) $\operatorname{Var}(X)=\tfrac4\pi-1\approx' + f'{V6:.4f}' + '$',
    diff='advanced', cites=cite('T6', 1))

amax = sqrt(1e-4 / 5)
assert abs(amax - 0.004472) < 1e-6
D.Q('Case 5 · Chebyshev · Practice 03 Q11',
    r'Chebyshev says $P(|Y-\mu_Y|\ge\varepsilon)\le\dfrac{\operatorname{Var}(Y)}{\varepsilon^2}$. '
    r'$E[X]=5$, $\operatorname{Var}(X)=5$ and $Y=aX+b$. Find $a$ and $b$ so that $P(|Y-10|\ge0.1)\le0.01$.',
    [S(r'**Type:** only $E$ and Var → Case 5 rules. Make the mean of $Y$ equal $10$.', r'E[Y]=5a+b=10'),
     S(r'**Plug in** $\operatorname{Var}(Y)=a^2\cdot5$, then make the Chebyshev bound at most $0.01$.', r'\frac{5a^2}{0.1^2}\le0.01\quad\Longrightarrow\quad a^2\le2\times10^{-5}'),
     S(r'Any such $a$ works, with $b$ from the first line.', r'|a|\le' + f'{amax:.5f}' + r',\qquad b=10-5a')],
    f'Any $|a|\\le {amax:.5f}$ with $b=10-5a$ (e.g. $a=0.004$, $b=9.98$).', diff='advanced', cites=cite('P3', 3))


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
    # Type 1: CDF try-it
    assert I(x * sp.diff(x ** 2, x), (x, 0, 1)) == sp.Rational(2, 3) == I(1 - t ** 2, (t, 0, 1))
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
    Cs = sp.solve(I(C / (1 + u ** 2), (u, -1, 1)) - 1, C)[0]
    assert sp.simplify(Cs - 2 / sp.pi) == 0
    K = sp.Symbol('K')
    EX = I(x * Cs / (1 + (x + K) ** 2), (x, -K - 1, -K + 1))
    assert sp.solve(sp.simplify(EX) - 5, K) == [-5]
    var6 = I((x - 5) ** 2 * Cs / (1 + (x - 5) ** 2), (x, 4, 6))
    assert sp.simplify(var6 - (4 / sp.pi - 1)) == 0
    die = [sp.Rational(1, 6)] * 6
    assert sum(k * k * w for k, w in zip(range(1, 7), die)) - sp.Rational(7, 2) ** 2 == sp.Rational(35, 12)
    assert sp.Rational(16, 2) * sp.Rational(1, 2) + sp.Rational(36, 2) * sp.Rational(1, 2) == 13
    assert I(x ** 2 / 2, (x, 0, 2)) - I(x / 2, (x, 0, 2)) ** 2 == sp.Rational(1, 3)
    print('q3 verify ok')


if __name__ == '__main__':
    verify()
    D.save()
