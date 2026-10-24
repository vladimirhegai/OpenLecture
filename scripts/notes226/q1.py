r"""Test 2 - Question 1: random experiments, sample spaces, discrete random variables, PMFs and CDFs (Lectures 7-9)."""
from fractions import Fraction as Fr
from math import comb, exp, factorial

from lib226 import Doc, S, cite, num, sci, steps

D = Doc('q1', 'Test 2 - Question 1', ['discrete_random_variables', 'pmf', 'cdf', 'binomial', 'poisson', 'geometric'])


def pois(lam, k):
    return exp(-lam) * lam ** k / factorial(k)


def binom(n, p, k):
    return comb(n, k) * p ** k * (1 - p) ** (n - k)


D.P('**Lectures 7–9.** Random experiments, sample spaces, discrete random variables, PMFs and CDFs.',
    cites=cite('L7', 2) + cite('L8', 5) + cite('L9', 2))

# =====================================================================================================
D.H('Topic 1: Random variables: turning outcomes into numbers')
D.P('An experiment produces an **outcome** $\\omega$ (like HTH).\n\n'
    'A **random variable** $X$ attaches a number to every outcome, so we can ask number questions ("how many heads?").')
D.REMIND(r'''**From Test 1 (you'll need this all the time)**

- **Sample space** $\Omega$ = the set of all outcomes. **Event** = a subset of $\Omega$.
- **Equally likely outcomes:** $P(A)=\dfrac{|A|}{|\Omega|}$ (count, then divide).
- **Complement:** $P(A^c)=1-P(A)$. Use it for "at least one".
- **Independent trials:** multiply, $P(A\cap B)=P(A)\,P(B)$.
- **Counting** $k$ items from $n$:

| | order matters | order doesn't |
|---|---|---|
| with replacement | $n^k$ | (not needed) |
| without replacement | $\dfrac{n!}{(n-k)!}$ | $\dbinom{n}{k}=\dfrac{n!}{k!\,(n-k)!}$ |''', cites=cite('L7', 1))
D.EQ(r'X:\Omega\to\mathbb{R},\qquad \omega\mapsto X(\omega)', cites=cite('L7', 2))
D.L([r'$\{X=x\}$ is an **event**: all outcomes $\omega$ with $X(\omega)=x$. Example: 2 tosses, $\{X=1\}=\{HT,TH\}$.',
     r'$P(X=x)$ is just the probability of that event.',
     r'$X$ is **discrete** when its range $R_X=\{X(\omega)\}$ is **countable**: a finite list $\{0,1,2,3\}$ or an endless list $\{0,1,2,\dots\}$.',
     r'The events $\{X=x\}$ for different $x$ never overlap and together cover $\Omega$ (a partition), so their probabilities add to $1$.'],
    cites=cite('L7', 3))
D.P('**How to find $P(X=x)$ for every $x$:**')
D.L(['**List** $\\Omega$ (or just count it).',
     '**Label** every outcome with its value $X(\\omega)$.',
     '**Group** the outcomes by value: these groups are the events $\\{X=x\\}$.',
     '**Add** the probabilities in each group (equally likely: count ÷ $|\\Omega|$).'], ordered=True)
D.EX('Three tosses, count the heads',
     'A fair coin is tossed three times. $X$ = number of heads. Find $P(X=x)$ for every value.',
     [S('**List** $\\Omega$: $2^3=8$ equally likely outcomes.',
        r'\Omega=\{hhh,hht,hth,thh,htt,tht,tth,ttt\}'),
      S('**Label and group** by the number of heads.',
        r'\begin{gathered}\{X=3\}=\{hhh\},\quad \{X=2\}=\{hht,hth,thh\}\\ \{X=1\}=\{htt,tht,tth\},\quad \{X=0\}=\{ttt\}\end{gathered}'),
      S('**Add** (count ÷ 8).', r'\begin{gathered}P(X=0)=\tfrac18,\quad P(X=1)=\tfrac38\\ P(X=2)=\tfrac38,\quad P(X=3)=\tfrac18\end{gathered}'),
      S('Check: the four groups partition $\\Omega$, so the total must be 1.', r'\tfrac18+\tfrac38+\tfrac38+\tfrac18=1\;\checkmark')],
     r'$P(X=0)=\tfrac18,\ P(X=1)=\tfrac38,\ P(X=2)=\tfrac38,\ P(X=3)=\tfrac18$', cites=cite('L7', 4))

# max of two dice: (2x-1)/36
mx = {x: Fr(2 * x - 1, 36) for x in range(1, 7)}
assert mx == {x: Fr(sum(1 for a in range(1, 7) for b in range(1, 7) if max(a, b) == x), 36) for x in range(1, 7)}
D.TRY('Larger of two dice',
      'Two fair dice are rolled. Let $X$ be the **larger** of the two numbers. Find $P(X=x)$ for $x=1,\\dots,6$.',
      [S('**List** $\\Omega$: ordered pairs $(a,b)$, $6\\cdot6=36$ equally likely outcomes.', r'|\Omega|=36'),
       S('**Group:** $\\{X=x\\}$ = pairs whose max is $x$. Example $x=3$: $(1,3),(2,3),(3,3),(3,2),(3,1)$.',
         r'|\{X=3\}|=5'),
       S('In general: $x$ choices for $b$ when $a=x$, plus $x$ choices for $a$ when $b=x$, minus the double-counted $(x,x)$.',
         r'|\{X=x\}|=x+x-1=2x-1'),
       S('**Divide** by 36.', r'P(X=x)=\frac{2x-1}{36},\qquad x=1,2,\dots,6'),
       S('Check the total.', r'\tfrac{1+3+5+7+9+11}{36}=\tfrac{36}{36}=1\;\checkmark')],
      r'$P(X=x)=\dfrac{2x-1}{36}$: $\tfrac1{36},\tfrac3{36},\tfrac5{36},\tfrac7{36},\tfrac9{36},\tfrac{11}{36}$')

ur = {k: Fr(comb(3, k) * comb(2, 2 - k), comb(5, 2)) for k in range(3)}
assert ur == {0: Fr(1, 10), 1: Fr(3, 5), 2: Fr(3, 10)}
D.TRY('Two balls, no replacement',
      'An urn has 3 red and 2 blue balls. Two balls are drawn **without replacement** (order not recorded). '
      'Let $X$ = number of red balls drawn. Find $P(X=x)$.',
      [S('**Count** $\\Omega$: unordered pairs from 5 balls.', r'|\Omega|=\binom52=10'),
       S('$X=0$: both blue.', r'P(X=0)=\frac{\binom30\binom22}{10}=\frac{1}{10}'),
       S('$X=1$: one of 3 red **and** one of 2 blue.', r'P(X=1)=\frac{\binom31\binom21}{10}=\frac{6}{10}'),
       S('$X=2$: both red.', r'P(X=2)=\frac{\binom32\binom20}{10}=\frac{3}{10}'),
       S('Check.', r'\tfrac1{10}+\tfrac6{10}+\tfrac3{10}=1\;\checkmark')],
      r'$P(X=0)=0.1,\ P(X=1)=0.6,\ P(X=2)=0.3$')

# =====================================================================================================
D.H('Topic 2: The PMF and the named families')
D.P('The **probability mass function** (PMF) lists how the total probability $1$ is split among the values of $X$.')
D.EQ(r'p_X(x)=P(X=x)', cites=cite('L7', 5))
D.L([r'**Rule 1:** $p_X(x)\ge 0$.',
     r'**Rule 2:** $\displaystyle\sum_{x\in R_X} p_X(x)=1$. Use it to find an unknown constant $c$.',
     r'**Sets of values:** $P(X\in B)=\displaystyle\sum_{x\in B}p_X(x)$, e.g. $P(1\le X\le 3)=p_X(1)+p_X(2)+p_X(3)$.',
     r'**"At least one":** $P(X\ge1)=1-p_X(0)$. Much faster than adding forever.'])
D.REMIND(r'''**Two sums that make PMFs add to 1**

- **Geometric series** ($|r|<1$): $\displaystyle\sum_{k=0}^{\infty} r^k=\frac{1}{1-r}$, and starting at $k=1$: $\displaystyle\sum_{k=1}^{\infty} r^k=\frac{r}{1-r}$.
- **Exponential series:** $\displaystyle\sum_{k=0}^{\infty}\frac{\lambda^k}{k!}=e^{\lambda}$ (this is why the Poisson PMF has $e^{-\lambda}$ in front).
- **Finite geometric:** $\displaystyle\sum_{k=0}^{m-1} r^k=\frac{1-r^m}{1-r}$.''')
D.P('Many experiments give PMFs with the same shape, so they get names. **Memorise these** (no formula sheet):')
D.T(['Family', 'PMF', '$k$', '$X$ counts…'],
    [['Bernoulli$(p)$', '${p^k(1-p)^{1-k}}$', '${k=0,1}$', 'one yes/no trial (1 = success)'],
     ['Binomial$(n,p)$', '${\\binom{n}{k}p^k(1-p)^{n-k}}$', '${0,\\dots,n}$', 'successes in $n$ independent trials'],
     ['Geometric$(p)$', '${(1-p)^{k-1}p}$', '${1,2,\\dots}$', 'trials until the **first** success'],
     ['Poisson$(\\lambda)$', '${e^{-\\lambda}\\dfrac{\\lambda^k}{k!}}$', '${0,1,2,\\dots}$', 'events in a fixed time/region, average $\\lambda$'],
     ['Hypergeometric', '${\\dfrac{\\binom{K}{k}\\binom{N-K}{n-k}}{\\binom{N}{n}}}$', '${0,\\dots,n}$', 'successes in $n$ draws **without** replacement']],
    cites=cite('L8', 5))
D.P('**Which family?** Read the story:')
D.L([r'**Fixed number $n$** of independent yes/no trials, same $p$ → **Binomial**.',
     r'**"Until the first success"** → **Geometric**. (Counting *failures before* it instead: $P=(1-p)^k p$, $k=0,1,\dots$)',
     r'**"On average $\lambda$ per hour/page/year"** → **Poisson**. Scale $\lambda$ to the interval asked: 7 per week → $\lambda=1$ per day.',
     r'**Draw without replacement** from a box with $K$ "good" out of $N$ → **Hypergeometric** (or just count, as in Try it 2).'])
D.CO('tip', r'**Why the binomial looks like that:** one particular outcome with $k$ successes, like $SS\dots SF\dots F$, has probability $p^k(1-p)^{n-k}$ (independent trials multiply). '
            r'There are $\binom{n}{k}$ ways to choose **which** trials are the successes.', cites=cite('L8', 4))
lines = ['title "Poisson PMF: drag $\\lambda$ and watch where the mass sits"',
         'x -0.5 14.5 label="$k$" height=260', 'y 0 0.42 label="$p_X(k)$"',
         'slider L 0.5 10 4 step=0.1 label="$\\lambda$"']
for k in range(15):
    lines += [f'segment "{k}" "0" "{k}" "exp(-L)*L^{k}/{factorial(k)}" color=1',
              f'point "{k}" "exp(-L)*L^{k}/{factorial(k)}" color=1']
lines += ['readout "$P(X=3)$" "exp(-L)*L^3/6"', 'readout "$P(X=4)$" "exp(-L)*L^4/24"', 'readout "$P(X\\ge1)=1-e^{-\\lambda}$" "1-exp(-L)"']
D.GRAPH(lines)
p3, p4 = pois(4, 3), pois(4, 4)
assert abs(p3 - p4) < 1e-12 and abs(p3 - 0.1954) < 5e-5
D.EX('Emails per hour (Poisson)',
     'The number of emails in one hour is Poisson with an average of 4 per hour. Compare $P(X=3)$ and $P(X=4)$.',
     [S('**Family:** "on average 4 per hour", counting in one hour → Poisson with $\\lambda=4$.',
        r'p_X(k)=e^{-4}\frac{4^k}{k!}'),
      S('Plug in $k=3$.', r'P(X=3)=e^{-4}\frac{4^3}{3!}=e^{-4}\cdot\frac{64}{6}\approx ' + f'{p3:.4f}'),
      S('Plug in $k=4$.', r'P(X=4)=e^{-4}\frac{4^4}{4!}=e^{-4}\cdot\frac{256}{24}\approx ' + f'{p4:.4f}'),
      S('They are **equal**: $\\frac{4^4}{4!}=\\frac{4}{4}\\cdot\\frac{4^3}{3!}$. In general $p(k)=p(k-1)\\cdot\\frac{\\lambda}{k}$, so the top is near $\\lambda$.',
        r'P(X=3)=P(X=4)\approx 0.1954')],
     r'Both $\approx 0.1954$: the PMF peaks at $k=3$ and $k=4$ together.', cites=cite('L8', 3))
D.TRY('Find the constant',
      r'Can $p_X(x)=c\left(\tfrac23\right)^x$ for $x=1,2,3,\dots$ (and $0$ elsewhere) be a PMF? If so, find $c$.',
      [S('**Rule 1:** for $c>0$ every value is positive. **Rule 2:** the total must be 1.',
         r'\sum_{x=1}^{\infty}c\left(\tfrac23\right)^x=1'),
       S(r'Geometric series starting at $x=1$ with $r=\tfrac23$.', r'\sum_{x=1}^{\infty}\left(\tfrac23\right)^x=\frac{2/3}{1-2/3}=2'),
       S('Solve.', r'2c=1\;\Rightarrow\; c=\tfrac12')],
      r'Yes, with $c=\tfrac12$.', diff='introductory', cites=cite('T3', 1))
pt = 1 - exp(-1 / 3)
D.TRY('Typos on a page',
      'A book has on average one typo every three pages. The number of typos on one page is Poisson. '
      'Find the probability of at least one typo on a given page.',
      [S('**Scale $\\lambda$** to one page: 1 per 3 pages → $\\tfrac13$ per page.', r'\lambda=\tfrac13'),
       S('**At least one** → complement.', r'P(X\ge1)=1-P(X=0)=1-e^{-1/3}'),
       S('Evaluate.', r'1-e^{-1/3}\approx ' + f'{pt:.4f}')],
      f'$1-e^{{-1/3}}\\approx {pt:.4f}$', cites=cite('T3', 1))
bb = binom(8, 0.1, 0) + binom(8, 0.1, 1)
D.TRY('Bit errors in a byte',
      'Each bit of an 8-bit byte is flipped independently with probability $0.1$. '
      'Find the probability that the byte has **at most one** flipped bit.',
      [S('**Family:** fixed $n=8$ independent trials, "success" = flipped, $p=0.1$ → Binomial$(8,0.1)$.',
         r'P(X=k)=\binom8k(0.1)^k(0.9)^{8-k}'),
       S('"At most one" = $X=0$ or $X=1$.', r'P(X\le1)=(0.9)^8+8(0.1)(0.9)^7'),
       S('Evaluate.', f'{binom(8, .1, 0):.4f}+{binom(8, .1, 1):.4f}\\approx {bb:.4f}')],
      f'$P(X\\le1)\\approx {bb:.4f}$')
g3, g4 = 0.8 ** 2 * 0.2, 0.8 ** 3
D.TRY('Retransmit until it works',
      'A packet is sent again and again until one gets through. Each attempt succeeds independently with probability $0.2$. '
      'Let $X$ = number of attempts. Find $P(X=3)$ and $P(X>3)$.',
      [S('**Family:** "until the first success" → Geometric$(0.2)$.', r'P(X=k)=(0.8)^{k-1}(0.2),\quad k=1,2,\dots'),
       S('$X=3$: fail, fail, succeed.', r'P(X=3)=(0.8)^2(0.2)=' + num(g3)),
       S('$X>3$ means the first 3 attempts all failed (no sum needed).', r'P(X>3)=(0.8)^3=' + num(g4))],
      f'$P(X=3)={num(g3)}$, $P(X>3)={num(g4)}$')

# =====================================================================================================
D.H('Topic 3: The CDF')
D.P('The **cumulative distribution function** (CDF) answers "what is the chance $X$ is **at most** $x$?" for **every** real $x$.')
D.EQ(r'F_X(x)=P(X\le x)=\sum_{x_i\le x}p_X(x_i)', cites=cite('L8', 6))
D.L([r'Defined for **all** real $x$, not only the values of $X$ (e.g. $F_X(2.7)$ makes sense).',
     r'For a discrete $X$ it is a **staircase**: flat between values, a **jump of size $p_X(x_i)$** at each value $x_i$.',
     r'It never goes down, starts at $0$ (far left) and ends at $1$ (far right).',
     r'At a jump, $F_X(x_i)$ takes the **upper** value: $\le$ includes $x_i$ itself (the solid dot).'],
    cites=cite('L8', 6))
D.P('**Reading probabilities off the CDF:**')
D.T(['You want', 'Use'],
    [['$P(X\\le b)$', '$F_X(b)$'],
     ['$P(X>a)$', '$1-F_X(a)$'],
     ['$P(a<X\\le b)$', '$F_X(b)-F_X(a)$'],
     ['$P(X=a)$', 'jump at $a$ = $F_X(a)-F_X(a^-)$'],
     ['$P(X<a)$', '$F_X(a^-)$ = height just **left** of $a$']], cites=cite('L9', 4))
D.CO('warning', r'**$<$ vs $\le$ matters for discrete $X$.** With dice, $P(X<4)=F_X(3)$ but $P(X\le4)=F_X(4)$. '
                r'Rewrite every question as "$\le$" before reading the CDF.')
D.EX('CDF of the three-toss count',
     r'For Example 1 ($p_X(0)=\tfrac18,\ p_X(1)=\tfrac38,\ p_X(2)=\tfrac38,\ p_X(3)=\tfrac18$), find and sketch $F_X(x)$.',
     [S('**Left of 0**, $X\\le x$ is impossible.', r'x<0:\quad F_X(x)=0'),
      S('**Add each jump** as you pass a value, keep it flat in between.',
        r'F_X(x)=\begin{cases}0,&x<0\\ \tfrac18,&0\le x<1\\ \tfrac48=\tfrac12,&1\le x<2\\ \tfrac78,&2\le x<3\\ 1,&x\ge3\end{cases}'),
      S('**Sketch:** a staircase with jumps $\\tfrac18,\\tfrac38,\\tfrac38,\\tfrac18$ at $0,1,2,3$ (graph below).',
        r'F_X(3)=1')],
     r'Staircase: $0 \to \tfrac18 \to \tfrac12 \to \tfrac78 \to 1$ with jumps at $x=0,1,2,3$.', cites=cite('L9', 2))
D.GRAPH(['title "CDF of the number of heads in 3 tosses"', 'x -1 4.5 label="$x$" height=240', 'y 0 1.1 label="$F_X(x)$"']
        + steps([(0, 1 / 8), (1, 3 / 8), (2, 3 / 8), (3, 1 / 8)], -1, 4.5, color=2)
        + ['hline "1"', 'text "0.35" "0.2" "jump $\\tfrac18$"', 'text "1.4" "0.6" "jump $\\tfrac38$"'],
        intro='Each jump is one PMF value. The solid dot shows the step belongs to the **upper** value.')
D.TRY('From a CDF back to the PMF',
      r'''$X$ has CDF

$$
F_X(x)=\begin{cases}0,&x<-3\\ 3/8,&-3\le x<0\\ 3/4,&0\le x<6\\ 1,&x\ge6\end{cases}
$$

(a) Is $X$ discrete or continuous? (b) Find its PMF. (c) Find $P(-3<X\le6)$ and $P(X<0)$.''',
      [S('(a) The CDF is a staircase (it jumps), so **$X$ is discrete**, with values at the jumps.', r'R_X=\{-3,\;0,\;6\}'),
       S('(b) **Jump sizes** are the PMF.', r'p_X(-3)=\tfrac38,\quad p_X(0)=\tfrac34-\tfrac38=\tfrac38,\quad p_X(6)=1-\tfrac34=\tfrac14'),
       S('(c) Use $F(b)-F(a)$.', r'P(-3<X\le6)=F_X(6)-F_X(-3)=1-\tfrac38=\tfrac58'),
       S('$X<0$: height just left of $0$.', r'P(X<0)=F_X(0^-)=\tfrac38')],
      r'Discrete; $p_X(-3)=\tfrac38,\ p_X(0)=\tfrac38,\ p_X(6)=\tfrac14$; $P(-3<X\le6)=\tfrac58$, $P(X<0)=\tfrac38$.',
      cites=cite('P3', 3))
D.TRY('CDF of the larger die',
      'For $X$ = larger of two dice (Try it 1), find $F_X(x)$ for $x=1,\\dots,6$ **without** adding the PMF, then find $P(2<X\\le5)$.',
      [S('$X\\le x$ means **both** dice are $\\le x$. The dice are independent.', r'F_X(x)=P(\text{die}_1\le x)\,P(\text{die}_2\le x)=\frac{x}{6}\cdot\frac{x}{6}=\frac{x^2}{36}'),
       S('Check with the PMF: $F_X(2)=\\tfrac{1}{36}+\\tfrac{3}{36}=\\tfrac{4}{36}$. ✓', r'F_X(2)=\tfrac{4}{36}'),
       S('Use $F(b)-F(a)$.', r'P(2<X\le5)=F_X(5)-F_X(2)=\tfrac{25-4}{36}=\tfrac{21}{36}=\tfrac{7}{12}')],
      r'$F_X(x)=\dfrac{x^2}{36}$ at $x=1,\dots,6$ (flat in between); $P(2<X\le5)=\tfrac{7}{12}$.')

# =====================================================================================================
D.H('Practice Questions')
D.P('Test-style questions for Question 1, roughly easy → hard. Solve on paper first, then open the solution.')

d1, d2 = pois(1, 2), 1 - exp(-1)
D.Q('Wrong-number calls · Tutorial 3 Q3',
    'A mail-order house gets on average **7 wrong-number calls per week** (Poisson). Find the probability that tomorrow they get '
    '(a) exactly two wrong-number calls, (b) at least one.',
    [S('**Family:** average rate, count in an interval → Poisson. **Scale** to one day.', r'\lambda=\tfrac{7}{7}=1'),
     S('(a)', r'P(X=2)=e^{-1}\frac{1^2}{2!}=\frac{e^{-1}}{2}\approx ' + f'{d1:.4f}'),
     S('(b) **At least one** → complement.', r'P(X\ge1)=1-e^{-1}\approx ' + f'{d2:.4f}')],
    f'(a) $\\approx {d1:.4f}$ (b) $\\approx {d2:.4f}$', diff='introductory', cites=cite('T3', 1))

Fq = [Fr(sum(range(1, x + 1)), 10) for x in range(5)]
D.Q('A PMF with a constant',
    r'$p_X(x)=c\,x$ for $x=1,2,3,4$ and $0$ otherwise. (a) Find $c$. (b) Find and sketch the CDF. (c) Find $P(1<X\le3)$ and $P(X<3)$.',
    [S('(a) **Total = 1.**', r'c(1+2+3+4)=10c=1\;\Rightarrow\;c=\tfrac1{10}'),
     S('(b) **Add the jumps** $0.1, 0.2, 0.3, 0.4$ at $x=1,2,3,4$.',
       r'F_X(x)=\begin{cases}0,&x<1\\0.1,&1\le x<2\\0.3,&2\le x<3\\0.6,&3\le x<4\\1,&x\ge4\end{cases}'),
     S('(c) $F(b)-F(a)$.', r'P(1<X\le3)=F_X(3)-F_X(1)=0.6-0.1=0.5'),
     S('$X<3$ = $X\\le2$ for integer values.', r'P(X<3)=F_X(2)=0.3')],
    r'$c=0.1$; staircase $0,0.1,0.3,0.6,1$; $P(1<X\le3)=0.5$, $P(X<3)=0.3$.', diff='introductory')
assert [float(v) for v in Fq] == [0, .1, .3, .6, 1]

D.Q('Toss until a head, at most 4 tosses',
    r'A coin with $P(H)=p$ is tossed until the first head **or** until 4 tosses have been made, whichever comes first. '
    r'(a) Write the sample space. (b) Let $X$ = number of tosses made. Find the PMF of $X$. (c) Evaluate it for $p=\tfrac12$.',
    [S('(a) Stop at the first $H$, or after 4 tosses.', r'\Omega=\{H,\;TH,\;TTH,\;TTTH,\;TTTT\}'),
     S(r'(b) **Label:** $X(H)=1,\ X(TH)=2,\ X(TTH)=3$, and **two** outcomes give 4 tosses.', r'\{X=4\}=\{TTTH,\;TTTT\}'),
     S('Independent tosses multiply.', r'p_X(1)=p,\quad p_X(2)=(1-p)p,\quad p_X(3)=(1-p)^2p'),
     S('$X=4$: the first three were tails (the 4th can be anything).', r'p_X(4)=(1-p)^3p+(1-p)^4=(1-p)^3'),
     S('(c) $p=\\tfrac12$. Check: the total is 1.', r'\tfrac12,\ \tfrac14,\ \tfrac18,\ \tfrac18')],
    r'$p_X(1)=p,\ p_X(2)=(1-p)p,\ p_X(3)=(1-p)^2p,\ p_X(4)=(1-p)^3$; for $p=\tfrac12$: $\tfrac12,\tfrac14,\tfrac18,\tfrac18$.')

hy = {k: Fr(comb(3, k) * comb(7, 4 - k), comb(10, 4)) for k in range(4)}
assert hy == {0: Fr(1, 6), 1: Fr(1, 2), 2: Fr(3, 10), 3: Fr(1, 30)}
D.Q('Defective chips',
    'A box has 10 chips, 3 of them defective. Four chips are chosen at random **without replacement**. '
    'Let $X$ = number of defective chips chosen. (a) Find the PMF of $X$. (b) Find $F_X(1)$ and $P(X\\ge2)$.',
    [S('**Count** $\\Omega$: unordered choices of 4 from 10.', r'|\Omega|=\binom{10}{4}=210'),
     S('**$X=k$:** $k$ of the 3 defective **and** $4-k$ of the 7 good.', r'p_X(k)=\frac{\binom3k\binom7{4-k}}{210}'),
     S('Evaluate $k=0,1,2,3$.', r'\begin{gathered}p_X(0)=\tfrac{35}{210}=\tfrac16,\quad p_X(1)=\tfrac{105}{210}=\tfrac12\\ p_X(2)=\tfrac{63}{210}=\tfrac3{10},\quad p_X(3)=\tfrac{7}{210}=\tfrac1{30}\end{gathered}'),
     S('(b) Add up to 1, then use the complement.', r'F_X(1)=\tfrac16+\tfrac12=\tfrac23,\qquad P(X\ge2)=1-\tfrac23=\tfrac13')],
    r'$\tfrac16,\tfrac12,\tfrac3{10},\tfrac1{30}$ for $k=0..3$; $F_X(1)=\tfrac23$, $P(X\ge2)=\tfrac13$.')

a6 = sum(pois(3.9, k) for k in range(7))
a2 = 1 - pois(3.9, 0) - pois(3.9, 1)
a36 = sum(pois(3.9, k) for k in range(3, 7))
D.Q('Alpha particles · Tutorial 3 Q4',
    'One gram of a radioactive element emits on average 3.9 alpha particles per second (Poisson). For the next second, find '
    '(a) $P(\\text{at most }6)$, (b) $P(\\text{at least }2)$, (c) $P(\\text{at least 3 and at most 6})$.',
    [S('**Family:** Poisson with $\\lambda=3.9$ (already per second).', r'p(k)=e^{-3.9}\frac{3.9^k}{k!}'),
     S('(a) Add $k=0$ to $6$. Shortcut: each term is the previous one times $\\tfrac{3.9}{k}$.',
       r'P(X\le6)=e^{-3.9}\left(1+3.9+\tfrac{3.9^2}{2}+\dots+\tfrac{3.9^6}{720}\right)\approx ' + f'{a6:.4f}'),
     S('(b) **Complement** of $\\{0,1\\}$.', r'P(X\ge2)=1-e^{-3.9}(1+3.9)\approx ' + f'{a2:.4f}'),
     S('(c) $3\\le X\\le6$ = (at most 6) minus (at most 2).', r'P(3\le X\le6)=P(X\le6)-P(X\le2)\approx ' + f'{a36:.4f}')],
    f'(a) $\\approx {a6:.4f}$ (b) $\\approx {a2:.4f}$ (c) $\\approx {a36:.4f}$', cites=cite('T3', 1))

pairs = {}
for a in range(10):
    for b in range(a + 1, 10):
        pairs[a + b] = pairs.get(a + b, 0) + 1
assert sum(pairs.values()) == 45 and pairs[9] == 5 and pairs[10] == 4 and pairs[1] == 1 and pairs[17] == 1
D.Q('Total of two chips · Practice 02 Q5',
    'An urn has 10 chips numbered $0$ to $9$. Two chips are drawn at random without replacement. Find the PMF of their **total** $X$.',
    [S('**Count** $\\Omega$: unordered pairs of different chips, all equally likely.', r'|\Omega|=\binom{10}{2}=45,\qquad R_X=\{1,2,\dots,17\}'),
     S('**Group** pairs $\\{a<b\\}$ by $a+b$. Example $X=9$: $\\{0,9\\},\\{1,8\\},\\{2,7\\},\\{3,6\\},\\{4,5\\}$.', r'|\{X=9\}|=5'),
     S('For $s\\le9$: $a$ runs from $0$ while $a<s-a$. For $s\\ge10$ use symmetry: total $s$ ↔ total $18-s$ (replace each chip $c$ by $9-c$).',
       r'\begin{gathered}|\{X=s\}|=\left\lfloor\tfrac{s+1}{2}\right\rfloor\quad (s\le9)\\ |\{X=s\}|=|\{X=18-s\}|\quad (s\ge10)\end{gathered}'),
     S('So the counts for $s=1,\\dots,17$ are:', r'1,1,2,2,3,3,4,4,5,4,4,3,3,2,2,1,1'),
     S('Divide by 45 and check the counts add to 45.', r'p_X(s)=\frac{\text{count}(s)}{45},\qquad \textstyle\sum \text{counts}=45\;\checkmark')],
    r'$p_X(s)=\tfrac{1}{45}\times(1,1,2,2,3,3,4,4,5,4,4,3,3,2,2,1,1)$ for $s=1,\dots,17$.', cites=cite('P2', 1))

acc = 1 - sum(binom(12, 1 / 30, k) for k in range(4))
D.Q('Four accidents on one day · Tutorial 3 Q7',
    'A town had 12 accidents in June (30 days), 4 of them on June 13. Assume each accident is equally likely to fall on any day, '
    'independently. Find the probability that **at least 4** of the 12 accidents fall on June 13.',
    [S('**Family:** 12 independent accidents, "success" = it lands on June 13, $p=\\tfrac1{30}$ → Binomial$(12,\\tfrac1{30})$.',
       r'P(X=k)=\binom{12}{k}\left(\tfrac1{30}\right)^k\left(\tfrac{29}{30}\right)^{12-k}'),
     S('**At least 4** → complement of $0,1,2,3$.', r'P(X\ge4)=1-\sum_{k=0}^{3}\binom{12}{k}\left(\tfrac1{30}\right)^k\left(\tfrac{29}{30}\right)^{12-k}'),
     S('The four terms.', '\\approx 1-(' + '+'.join(f'{binom(12, 1 / 30, k):.4f}' for k in range(4)) + ')'),
     S('So 4 on one day is very unlikely by chance.', r'P(X\ge4)\approx ' + f'{acc:.5f}')],
    f'$P(X\\ge4)\\approx {acc:.5f}$ (about {acc * 1e4:.1f} in 10 000).', cites=cite('T3', 1))

e0 = exp(-7)
e3 = comb(8, 3) * e0 ** 3 * (1 - e0) ** 5
D.Q('Quiet years · Tutorial 3 Q6',
    'Earthquakes in a region follow a Poisson model with on average 7 per year. '
    '(a) Find the probability of no earthquakes in one year. (b) Find the probability that in **exactly three of the next eight years** there are no earthquakes.',
    [S('(a) **Poisson**, $\\lambda=7$ per year, $k=0$.', r'q=P(X=0)=e^{-7}\approx ' + f'{e0:.6f}'),
     S('(b) Each year is a trial: "success" = a quiet year, with probability $q$. 8 independent years → **Binomial$(8,q)$**.',
       r'P(Y=3)=\binom83q^3(1-q)^5'),
     S('Evaluate.', r'56\,(e^{-7})^3(1-e^{-7})^5\approx ' + sci(e3))],
    f'(a) $e^{{-7}}\\approx {e0:.6f}$ (b) $\\approx {sci(e3)}$', cites=cite('T3', 1))

pc = 1 - 0.99 ** (1 / 1000)
D.Q('Error-free pixels · Tutorial 6 Q7',
    'A rover sends pixels one after another; each pixel is corrupted independently with probability $p=0.03$. '
    '(a) Let $N$ = number of **error-free** pixels between two erroneous ones. Find the PMF of $N$. '
    '(b) A new rover needs a 99% chance that at least 1000 pixels in a row arrive correctly before a bad one. How small must $p$ be?',
    [S('(a) After an error, count good pixels until the next bad one. $N=k$: $k$ good, then 1 bad.', r'P(N=k)=(0.97)^k(0.03),\qquad k=0,1,2,\dots'),
     S('This is the geometric "failures before the first success" form (starts at $k=0$).', r'\sum_{k\ge0}(0.97)^k(0.03)=\frac{0.03}{1-0.97}=1\;\checkmark'),
     S('(b) **At least 1000 good in a row** = the first 1000 pixels are all good.', r'P(N\ge1000)=(1-p)^{1000}\ge0.99'),
     S('Solve for $p$.', r'1-p\ge0.99^{1/1000}\;\Rightarrow\;p\le1-0.99^{1/1000}\approx ' + sci(pc))],
    r'(a) $P(N=k)=0.97^k\cdot0.03$, $k=0,1,\dots$ (b) $p\lesssim 1.0\times10^{-5}$', cites=cite('T6', 1))
assert abs(pc - 1.005e-5) < 1e-8

D.Q('Geometric, all the way · Practice 03 Q7',
    r'$N\sim$ Geometric$(p)$: $P(N=k)=(1-p)^{k-1}p$, $k=1,2,\dots$ Find (a) $P(N>k)$, (b) the CDF of $N$, (c) $P(N\text{ is even})$, (d) $P(N=k\mid N\le m)$.',
    [S('(a) $N>k$ means the first $k$ trials all failed.', r'P(N>k)=(1-p)^k'),
     S('(b) **Complement**, flat between integers.', r'F_N(x)=\begin{cases}0,&x<1\\1-(1-p)^{\lfloor x\rfloor},&x\ge1\end{cases}'),
     S('(c) Add $k=2,4,6,\\dots$: a geometric series with ratio $(1-p)^2$.',
       r'P(\text{even})=\sum_{m=1}^{\infty}(1-p)^{2m-1}p=\frac{p(1-p)}{1-(1-p)^2}=\frac{1-p}{2-p}'),
     S('(d) **Conditional probability:** $P(A\\mid B)=\\dfrac{P(A\\cap B)}{P(B)}$. For $k\\le m$, $\\{N=k\\}$ is inside $\\{N\\le m\\}$.',
       r'P(N=k\mid N\le m)=\frac{(1-p)^{k-1}p}{1-(1-p)^m},\qquad k=1,\dots,m'),
     S('For $k>m$ the intersection is empty.', r'P(N=k\mid N\le m)=0,\qquad k>m')],
    r'(a) $(1-p)^k$ (b) $1-(1-p)^{\lfloor x\rfloor}$ for $x\ge1$ (c) $\dfrac{1-p}{2-p}$ (d) $\dfrac{(1-p)^{k-1}p}{1-(1-p)^m}$ for $1\le k\le m$',
    diff='advanced', cites=cite('P3', 2))


def verify():
    import sympy as sp
    p, m = sp.symbols('p m', positive=True)
    k = sp.symbols('k', integer=True, positive=True)
    even = sp.summation((1 - p) ** (2 * k - 1) * p, (k, 1, sp.oo))
    assert sp.simplify(sp.piecewise_fold(even).args[0][0] - (1 - p) / (2 - p)) == 0
    c = sp.Symbol('c')
    assert sp.solve(sp.summation(c * sp.Rational(2, 3) ** k, (k, 1, sp.oo)) - 1, c) == [sp.Rational(1, 2)]
    q = sp.Rational(1, 2)
    assert [q, (1 - q) * q, (1 - q) ** 2 * q, (1 - q) ** 3] == [sp.Rational(1, 2), sp.Rational(1, 4), sp.Rational(1, 8), sp.Rational(1, 8)]
    print('q1 verify ok')


if __name__ == '__main__':
    verify()
    D.save()
