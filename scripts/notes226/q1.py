r"""Test 2 - Question 1: random experiments, sample spaces, discrete random variables, PMFs and CDFs (Lectures 7-9).

Layout (REWRITE_PLAN.md, v3): two topics, each = explanation + formulas (open) -> open worked examples of the
different kinds of question -> practice. Step words: Spot, List, Label, Add, Check, Find c, Accumulate, Rewrite,
Read off, Plug in, Inside, Outside (the same words as Questions 2-4).
"""
from fractions import Fraction as Fr
from math import comb, exp, factorial, perm

from lib226 import Doc, S, cite, num, sci, steps

D = Doc('q1', 'Test 2 - Question 1', ['discrete_random_variables', 'pmf', 'cdf', 'binomial', 'poisson', 'geometric'])


def pois(lam, k):
    return exp(-lam) * lam ** k / factorial(k)


def binom(n, p, k):
    return comb(n, k) * p ** k * (1 - p) ** (n - k)


def big(n):
    return f'{n:,}'.replace(',', '{,}')


D.P(r'**Lectures 7–9.** Question 1 gives you a random number $X$ that lands on separate values ($0,1,2,\dots$), like the number of heads in 3 tosses. You find the chance of each value (the **PMF**) and the running total (the **CDF**). Two topics cover it: **PMF and CDF**, then **named families**.',
    cites=cite('L7', 2) + cite('L8', 5) + cite('L9', 2))

# =====================================================================================================
D.H('Topic 1: PMF and CDF')
D.P(r'There are two ways to write down the chances of $X$. Both say the same thing.')
D.P(r'**The PMF** = the chance of each value. Every chance is between $0$ and $1$, and together they add to $1$.')
D.EQ(r'p_X(x)=P(X=x),\qquad \sum_{\text{all }x}p_X(x)=1', cites=cite('L7', 3))
D.P(r'Example: toss 3 coins, $X$ = number of heads.')
D.EQ(r'p_X(0)=\frac18,\quad p_X(1)=\frac38,\quad p_X(2)=\frac38,\quad p_X(3)=\frac18')
D.P(r'**The CDF** = the running total: the chance that $X$ is **at most** $x$.')
D.EQ(r'F_X(x)=P(X\le x)=\sum_{k\le x}p_X(k)', cites=cite('L8', 6))
D.P(r'Same example: add the chances as you walk right.')
D.EQ(r'F_X:\quad 0\ \to\ \frac18\ \to\ \frac12\ \to\ \frac78\ \to\ 1')
D.GRAPH(['title "CDF of the number of heads in 3 tosses"', 'x -1 4.5 label="$x$" height=240', 'y 0 1.1 label="$F_X(x)$"']
        + steps([(0, 1 / 8), (1, 3 / 8), (2, 3 / 8), (3, 1 / 8)], -1, 4.5, color=2)
        + ['hline "1"', 'text "0.35" "0.2" "jump $\\tfrac18$"', 'text "1.4" "0.6" "jump $\\tfrac38$"'],
        intro='So the CDF is a **staircase**: flat between values, and it **jumps by $p_X(x)$** at each value. It starts at $0$ and ends at $1$. At a jump, the value is the **top** of the step (the dot).')
D.P(r'**How to go between them:**')
D.T(['You have', 'You want', 'Do this'],
    [['an experiment', 'the PMF', '**List** the outcomes → **Label** each with its $X$ → **Add** the chances per value → **Check** they add to $1$'],
     [r'a PMF with an unknown $c$', '$c$', '**Find $c$:** add every chance, set the total to $1$, solve'],
     ['the PMF', 'the CDF', '**Accumulate:** running total'],
     ['the CDF', 'the PMF', 'the **jump sizes** are the PMF']], cites=cite('L7', 3))
D.P(r'**Any probability from the CDF** (**Rewrite** it with $F$’s):')
D.T(['Asked', 'Write it as'],
    [[r'$P(X\le b)$', r'$F_X(b)$'],
     [r'$P(X>a)$', r'$1-F_X(a)$'],
     [r'$P(a<X\le b)$', r'$F_X(b)-F_X(a)$'],
     [r'$P(X=a)$', r'the jump at $a$ ($0$ if there’s no jump)']], cites=cite('L9', 4))
D.CO('warning', r'**Whole numbers: turn $<$ into $\le$ first.** $P(X<4)=P(X\le3)=F_X(3)$. For a discrete $X$, $<$ and $\le$ give different answers.')
D.P(r'**Sums you’ll need for “find $c$”:** the geometric series ($|r|<1$) and the exponential series.')
D.EQ(r'\sum_{k=0}^{\infty}r^k=\frac{1}{1-r},\qquad \sum_{k=1}^{\infty}r^k=\frac{r}{1-r},\qquad \sum_{k=0}^{\infty}\frac{\lambda^k}{k!}=e^{\lambda}')

D.EX('Build a PMF · 3 coins (Lecture 7)',
     r'Toss a fair coin 3 times. $X$ = the number of heads. Find the PMF of $X$.',
     [S(r'**Spot:** an experiment, no family named → build the PMF.'),
      S(r'**List:** $2^3=8$ equally likely outcomes, each with chance $\tfrac18$.', r'hhh,\ hht,\ hth,\ thh,\ htt,\ tht,\ tth,\ ttt'),
      S(r'**Label** each outcome with its number of heads.', r'\begin{gathered}X=3:\ hhh\qquad X=2:\ hht,\ hth,\ thh\\ X=1:\ htt,\ tht,\ tth\qquad X=0:\ ttt\end{gathered}'),
      S(r'**Add** the chances in each group.', r'p_X(0)=\frac18,\quad p_X(1)=\frac38,\quad p_X(2)=\frac38,\quad p_X(3)=\frac18'),
      S(r'**Check** they add to $1$.', r'\frac18+\frac38+\frac38+\frac18=1\ \checkmark')],
     r'$p_X=\tfrac18,\ \tfrac38,\ \tfrac38,\ \tfrac18$ for $x=0,1,2,3$', cites=cite('L7', 4))
chips = {s: Fr(sum(1 for a in range(10) for b in range(a + 1, 10) if a + b == s), 45) for s in range(1, 18)}
D.EX('Build a PMF · without replacement (Practice 02 Q5)',
     r'10 chips are numbered $0$ to $9$. You draw 2 without replacement. $S$ = the total of the two numbers. Find the PMF of $S$.',
     [S(r'**List:** a pair of different chips, order doesn’t matter.', r'\binom{10}{2}=45\ \text{ equally likely pairs}'),
      S(r'**Label:** totals run from $0+1=1$ up to $8+9=17$. Count the pairs for each total. For $S=9$:', r'\{0,9\},\{1,8\},\{2,7\},\{3,6\},\{4,5\}\quad\Rightarrow\quad 5\text{ pairs}'),
      S(r'For $S=10$: $\{1,9\},\{2,8\},\{3,7\},\{4,6\}$. Not $\{5,5\}$: one chip can’t be drawn twice.', r'4\text{ pairs}'),
      S(r'**Add:** the counts climb $1,1,2,2,3,3,4,4,5$ up to $S=9$, then fall $4,4,3,3,2,2,1,1$. Divide by $45$.', r'p_S(s)=\frac{\text{pairs with total }s}{45},\qquad p_S(9)=\frac{5}{45}=\frac19'),
      S(r'**Check:** the counts add up to all 45 pairs.', r'\begin{gathered}1+1+2+2+3+3+4+4+5=25\\ 4+4+3+3+2+2+1+1=20\\ 25+20=45\ \checkmark\end{gathered}')],
     r'$p_S(s)=\tfrac{1}{45}\times(1,1,2,2,3,3,4,4,5,4,4,3,3,2,2,1,1)$ for $s=1,\dots,17$', cites=cite('P2', 1))
mx = {x: Fr(2 * x - 1, 36) for x in range(1, 7)}
assert mx == {x: Fr(sum(1 for a in range(1, 7) for b in range(1, 7) if max(a, b) == x), 36) for x in range(1, 7)}
D.EX('Build a PMF · larger of two dice',
     r'Two fair dice are rolled. $X$ = the **larger** of the two numbers. Find $P(X=x)$ for $x=1,\dots,6$.',
     [S(r'**List:** $6\cdot6=36$ equally likely pairs $(a,b)$.', r'36\text{ outcomes}'),
      S(r'**Label** one value first, $x=3$: the pairs whose larger number is 3.', r'(1,3),\ (2,3),\ (3,3),\ (3,2),\ (3,1)\quad\Rightarrow\quad 5\text{ pairs}'),
      S(r'In general: $x$ pairs with $a=x$, plus $x$ pairs with $b=x$, minus $(x,x)$ counted twice.', r'2x-1\text{ pairs}'),
      S(r'**Add:** divide by 36.', r'P(X=x)=\frac{2x-1}{36}'),
      S(r'**Check:** $1+3+5+7+9+11=36$ ✓.')],
     r'$P(X=x)=\dfrac{2x-1}{36}$: $\tfrac1{36},\tfrac3{36},\tfrac5{36},\tfrac7{36},\tfrac9{36},\tfrac{11}{36}$')
D.EX(r'Find $c$ · a geometric series (Tutorial 3 Q2)',
     r'$p_X(x)=c\big(\tfrac23\big)^x$ for $x=1,2,3,\dots$ Find $c$.',
     [S(r'**Spot:** a PMF with an unknown $c$ → the chances must add to $1$.', r'\sum_{x=1}^{\infty}c\Big(\frac23\Big)^x=1'),
      S(r'**Read off:** a geometric series starting at $x=1$, ratio $r=\tfrac23$.', r'\sum_{x=1}^{\infty}r^x=\frac{r}{1-r}=\frac{2/3}{1-2/3}=2'),
      S(r'**Find $c$:** solve.', r'2c=1\quad\Longrightarrow\quad c=\frac12')],
     r'$c=\tfrac12$', cites=cite('T3', 1))
D.EX('PMF → CDF · the 3-coin staircase (Lecture 9)',
     r'$X$ = the number of heads in 3 tosses, with PMF $\tfrac18,\tfrac38,\tfrac38,\tfrac18$ at $0,1,2,3$. Find the CDF and $P(1<X\le3)$.',
     [S(r'**Accumulate:** start at $0$, then add each jump as you pass $0$, $1$, $2$, $3$.',
        r'F_X(x)=\begin{cases}0,&x<0\\ \frac18,&0\le x<1\\ \frac12,&1\le x<2\\ \frac78,&2\le x<3\\ 1,&x\ge3\end{cases}'),
      S(r'**Rewrite** $P(1<X\le3)$ as a difference of $F$’s.', r'P(1<X\le3)=F_X(3)-F_X(1)=1-\frac12=\frac12')],
     r'the staircase above; $P(1<X\le3)=\tfrac12$', cites=cite('L9', 2))
D.EX('CDF → PMF · read the jumps (Practice 03 Q9)',
     r'$F_X(x)=0$ for $x<-3$, $\tfrac38$ on $[-3,0)$, $\tfrac34$ on $[0,6)$, and $1$ for $x\ge6$. Find the PMF, $P(-3<X\le6)$ and $P(X<0)$.',
     [S(r'**Spot:** a staircase → $X$ is discrete. It jumps at $-3$, $0$, $6$.', r'X\in\{-3,\ 0,\ 6\}'),
      S(r'The **jump sizes** are the PMF.', r'p_X(-3)=\frac38,\quad p_X(0)=\frac34-\frac38=\frac38,\quad p_X(6)=1-\frac34=\frac14'),
      S(r'**Rewrite** $P(-3<X\le6)$.', r'F_X(6)-F_X(-3)=1-\frac38=\frac58'),
      S(r'**Rewrite** $P(X<0)$: the step just left of $0$.', r'P(X<0)=\frac38')],
     r'$p_X=\tfrac38,\ \tfrac38,\ \tfrac14$ at $-3,\ 0,\ 6$; $P(-3<X\le6)=\tfrac58$; $P(X<0)=\tfrac38$', cites=cite('P3', 3))

# =====================================================================================================
D.H('Topic 2: named families')
D.P(r'Some stories follow a pattern. Then you don’t build the PMF: it’s ready-made. A **clue word** tells you which one.')
D.T(['Clue in the question', 'Family', 'PMF'],
    [['**one** yes/no try', 'Bernoulli$(p)$', r'$P(1)=p,\ P(0)=1-p$'],
     ['**fixed number $n$** of tries, count successes', 'Binomial$(n,p)$', r'$\binom nk p^k(1-p)^{n-k}$, $k=0..n$'],
     ['tries **until the first** success', 'Geometric$(p)$', r'$(1-p)^{k-1}p$, $k=1,2,..$'],
     ['tries **until the $r$-th** success', 'Negative Binomial$(r,p)$', r'$\binom{k-1}{r-1}p^r(1-p)^{k-r}$, $k=r,r+1,..$'],
     ['draw $n$ **without replacement**', 'Hypergeometric', r'$\binom Kk\binom{N-K}{n-k}\big/\binom Nn$'],
     [r'“**on average** $\lambda$ per hour/page/year”', r'Poisson$(\lambda)$', r'$e^{-\lambda}\lambda^k/k!$, $k=0,1,2,..$']], cites=cite('L8', 5))
D.P(r'**What the letters mean:**')
D.L([r'$p$ = the chance one try “succeeds”. **Success** = whatever the question counts, even a bad thing (a wrong bit, a defect).',
     r'$n$ = how many tries (Binomial), or how many you grab (Hypergeometric).',
     r'$k$ = the value the question asks about: how many successes, which try, or how many arrivals.',
     r'$r$ = how many successes you wait for (Negative Binomial).',
     r'$N$ = items in the box, $K$ = the special ones in the box (Hypergeometric).',
     r'$\lambda$ = the average count **for the time window asked** (Poisson).'])
D.P(r'**The steps, every time:**')
D.L([r'**Spot** the family from the clue word.',
     r'**Read off** its numbers from the story ($n=\dots$, $p=\dots$, $k=\dots$).',
     r'**Plug in** to the PMF.'], ordered=True)
D.P(r'**Three shortcuts:**')
D.L([r'**At least one** = one minus none: $P(X\ge1)=1-P(X=0)$.',
     r'**At least $m$** = one minus the few below: $P(X\ge4)=1-\big[P(0)+P(1)+P(2)+P(3)\big]$.',
     r'**Geometric, more than $k$ tries** = the first $k$ all failed: $P(X>k)=(1-p)^k$.'])
D.CO('warning', r'**Poisson: scale $\lambda$ to the time asked.** 7 per week, a question about one day → $\lambda=1$. **With replacement** → Binomial; **without** → Hypergeometric.')

D.EX(r'Bernoulli · one free throw',
     r'You take **one** free throw and make it with chance $0.7$. $Y=1$ if you make it, $0$ if you miss. Find the PMF of $Y$.',
     [S(r'**Spot:** one yes/no try → Bernoulli. $p$ = the chance the one try succeeds.'),
      S(r'**Read off:**', r'p=0.7'),
      S(r'**Plug in:**', r'P(Y=1)=0.7,\qquad P(Y=0)=1-0.7=0.3')],
     r'$P(Y=1)=0.7$, $P(Y=0)=0.3$')
D.EX(r'Binomial · wrong bits',
     r'You send $8$ bits. Each one arrives wrong with chance $0.1$, independently. $X$ = how many arrive wrong. Find $P(X=1)$, exactly one wrong.',
     [S(r'**Spot:** a fixed number of tries (8 bits), count the successes (“wrong”) → Binomial.'),
      S(r'**Read off:** $n$ = tries, $p$ = chance of a wrong bit, $k$ = how many wrong we want.', r'n=8,\qquad p=0.1,\qquad k=1'),
      S(r'**Plug in:**', r'\binom81(0.1)^1(0.9)^{7}=8(0.1)(0.9)^7\approx' + f'{binom(8, 0.1, 1):.4f}'),
      S(r'Why it works: $\binom81=8$ picks **which** bit is wrong, $(0.1)^1$ is that bit going wrong, $(0.9)^7$ is the other 7 being fine.')],
     f'$P(X=1)\\approx {binom(8, 0.1, 1):.4f}$')
g3, g4 = 0.8 ** 2 * 0.2, 0.8 ** 3
D.EX(r'Geometric · retransmit until it works',
     r'A packet is sent again and again until one gets through. Each try works with chance $0.2$, independently. $X$ = the try that finally works. Find $P(X=3)$ and $P(X>3)$.',
     [S(r'**Spot:** “until it works” → Geometric.'),
      S(r'**Read off:** $p$ = the chance one try works, $k$ = the try where the first success happens.', r'p=0.2,\qquad k=3'),
      S(r'**Plug in:** try 1 fails, try 2 fails, try 3 works.', r'(1-0.2)^{3-1}(0.2)=(0.8)^2(0.2)=' + num(g3)),
      S(r'$X>3$ means the first 3 tries all failed (shortcut).', r'P(X>3)=(0.8)^3=' + num(g4))],
     f'$P(X=3)={num(g3)}$, $P(X>3)={num(g4)}$')
nb5 = comb(4, 2) * 0.7 ** 3 * 0.3 ** 2
D.EX(r'Negative Binomial · the 3rd basket',
     r'Each free throw goes in with chance $0.7$. $X$ = the shot where you make your **3rd** basket. Find $P(X=5)$.',
     [S(r'**Spot:** “until the 3rd success” → Negative Binomial.'),
      S(r'**Read off:** $r$ = successes you wait for, $p$ = chance per shot, $k$ = the shot where the 3rd one lands.', r'r=3,\qquad p=0.7,\qquad k=5'),
      S(r'**Plug in:**', r'\binom{5-1}{3-1}(0.7)^3(0.3)^{5-3}=\binom42(0.7)^3(0.3)^2\approx' + f'{nb5:.4f}'),
      S(r'Why it works: shot 5 must be the 3rd basket, so the first 4 shots hold the other 2. $\binom42=6$ ways to place them; 3 baskets at $0.7$, 2 misses at $0.3$.')],
     f'$P(X=5)\\approx {nb5:.4f}$')
hy = {k: Fr(comb(3, k) * comb(7, 4 - k), comb(10, 4)) for k in range(4)}
assert hy == {0: Fr(1, 6), 1: Fr(1, 2), 2: Fr(3, 10), 3: Fr(1, 30)}
D.EX(r'Hypergeometric · defective chips',
     r'A box has 10 chips, 3 of them defective. You grab 4 (no putting back). $X$ = how many of your 4 are defective. Find $P(X=1)$.',
     [S(r'**Spot:** grab without replacement → Hypergeometric. “Defective” is the special kind.'),
      S(r'**Read off:** $N$ = chips in the box, $K$ = defective ones in the box, $n$ = how many you grab, $k$ = defective ones we want in the grab.', r'N=10,\qquad K=3,\qquad n=4,\qquad k=1'),
      S(r'**Plug in:**', r'\frac{\binom31\binom{10-3}{4-1}}{\binom{10}{4}}=\frac{\binom31\binom73}{\binom{10}{4}}=\frac{3\cdot35}{210}=\frac12'),
      S(r'Why it works: top = pick 1 of the 3 defective **and** 3 of the 7 good. Bottom = every possible grab of 4.')],
     r'$P(X=1)=\tfrac12$')
p3, p4 = pois(4, 3), pois(4, 4)
assert abs(p3 - p4) < 1e-12 and abs(p3 - 0.1954) < 5e-5
D.EX(r'Poisson · emails per hour (Lecture 8)',
     r'Emails arrive at 4 per hour on average. (a) Find the chance of exactly 3 emails in the next hour. (b) Find the chance of no emails in the next 30 minutes.',
     [S(r'**Spot:** “on average … per hour” → Poisson.'),
      S(r'(a) **Read off:** the window is one hour, so $\lambda=4$. $k$ = the count asked.', r'\lambda=4,\qquad k=3'),
      S(r'**Plug in:**', r'P(X=3)=e^{-4}\frac{4^3}{3!}\approx' + f'{p3:.4f}'),
      S(r'(b) **Read off:** half the window → half the average.', r'\lambda=2,\qquad k=0'),
      S(r'**Plug in:**', r'P(X=0)=e^{-2}\frac{2^0}{0!}=e^{-2}\approx' + f'{exp(-2):.4f}')],
     f'(a) $\\approx {p3:.4f}$ (b) $\\approx {exp(-2):.4f}$', cites=cite('L8', 3))
qt = exp(-2)
t1 = 5 * qt * (1 - qt) ** 4
D.EX(r'Two families in one question · clean pages',
     r'Typos follow a Poisson law, on average 2 per page. Find the chance that **exactly 1 of the next 5 pages** has no typos.',
     [S(r'**Spot:** two layers. **Inside**, one page is Poisson. **Outside**, each page is a yes/no try: clean or not.'),
      S(r'**Inside:** the chance one page is clean is Poisson with $\lambda=2$, $k=0$. Call it $q$.', r'q=e^{-2}\frac{2^0}{0!}=e^{-2}\approx' + f'{qt:.4f}'),
      S(r'**Outside:** 5 pages, count the clean ones → Binomial. **Read off:**', r'n=5,\qquad p=q,\qquad k=1'),
      S(r'**Plug in:**', r'\binom51\,q\,(1-q)^4\approx' + f'{t1:.4f}'),
      S(r'If the question asked for the **first** clean page instead, the outside would be Geometric$(q)$.')],
     f'$\\approx {t1:.4f}$')

# =====================================================================================================
D.H('Practice Questions')
D.CO('tip', r'''**Question 1 is always these, in parts (a), (b), (c).** Spot which kind, then run its steps:

1. **Build a PMF** (no family): List → Label → Add → Check.
2. **Find $c$:** add every chance, set it to $1$.
3. **CDF:** running total; jumps = the PMF; $P(a<X\le b)=F(b)-F(a)$; whole numbers: $<$ → $\le$.
4. **Named family:** Spot → Read off → Plug in. Scale Poisson’s $\lambda$. “At least” → $1-$ the rest.
5. **Two families:** Inside gives $q$, Outside is Binomial or Geometric.''')
D.P('Test-style, easy → hard. Solve on paper first, then open the solution.')

d1, d2, d3 = pois(1, 2), 1 - exp(-1), 1 - exp(-1 / 3)
D.Q('Named family (Poisson) · Tutorial 3 Q3, Q5',
    'A mail-order house gets on average **7 wrong-number calls per week** (Poisson). Find the probability that tomorrow they get '
    '(a) exactly two wrong-number calls, (b) at least one. '
    '(c) A book has on average one typo every **three pages** (Poisson). Find the chance a given page has at least one typo.',
    [S(r'**Spot:** “on average” → Poisson. Scale $\lambda$ to one day.', r'\lambda=\frac{7}{7}=1'),
     S(r'(a) **Write** and **plug in** $k=2$.', r'P(X=2)=e^{-1}\frac{1^2}{2!}\approx ' + f'{d1:.4f}'),
     S(r'(b) **At least one** → one minus none.', r'P(X\ge1)=1-e^{-1}\approx ' + f'{d2:.4f}'),
     S(r'(c) Scale to one page: $\lambda=\tfrac13$. Then one minus none.', r'P(X\ge1)=1-e^{-1/3}\approx ' + f'{d3:.4f}')],
    f'(a) $\\approx {d1:.4f}$ (b) $\\approx {d2:.4f}$ (c) $\\approx {d3:.4f}$', diff='introductory', cites=cite('T3', 1))

D.Q('Build a PMF · with and without replacement · like Practice 01 Q7',
    'An urn has 2 black balls and 1 white ball. Two balls are drawn one after the other. $X$ = number of black balls drawn. '
    'Find the PMF of $X$ (a) **without** replacement, (b) **with** replacement. (c) Which one is a named family?',
    [S(r'(a) **List** ordered draws, calling the black balls $B_1,B_2$: 6 equally likely.', r'B_1B_2,\ B_2B_1,\ B_1W,\ B_2W,\ WB_1,\ WB_2'),
     S(r'**Label** and **add:** two have both black, four have one, none have zero.', r'P(X=2)=\frac26=\frac13,\quad P(X=1)=\frac46=\frac23,\quad P(X=0)=0'),
     S(r'(b) With replacement, each draw is black with $\tfrac23$, independently. **Add** the orders for $X=1$.',
       (r'P(X=2)=\Big(\frac23\Big)^2=\frac49,\qquad P(X=0)=\Big(\frac13\Big)^2=\frac19', r'P(X=1)=2\cdot\frac23\cdot\frac13=\frac49')),
     S(r'**Check:** both PMFs add to $1$.', r'\frac13+\frac23=1,\qquad \frac49+\frac49+\frac19=1'),
     S(r'(c) With replacement = independent tries → **Binomial**$(2,\tfrac23)$. Without → Hypergeometric.')],
    r'(a) $0,\tfrac23,\tfrac13$ for $x=0,1,2$ (b) $\tfrac19,\tfrac49,\tfrac49$ (c) (b) is Binomial$(2,\tfrac23)$',
    diff='introductory', cites=cite('P1', 1))

D.Q('PMF and CDF · find $c$, then the CDF',
    r'(a) $p_X(x)=c\,(x+1)$ for $x=0,1,2,3$. Find $c$, then $F_X(1.5)$ and $P(X\ge2)$. '
    r'(b) $p_X(k)=c\,\dfrac{3^k}{k!}$ for $k=0,1,2,\dots$ Find $c$. Which family is this?',
    [S(r'(a) **Find $c$:** add every chance.', r'c(1+2+3+4)=10c=1\quad\Longrightarrow\quad c=\frac1{10}'),
     S(r'So the PMF is $0.1,0.2,0.3,0.4$. **Accumulate** every value $\le1.5$: $x=0,1$.', r'F_X(1.5)=0.1+0.2=0.3'),
     S(r'**Rewrite:** $X\ge2$ is one minus $X\le1$.', r'P(X\ge2)=1-F_X(1)=1-0.3=0.7'),
     S(r'(b) **Find $c$** with the exponential series, $\sum\frac{3^k}{k!}=e^3$.', r'c\,e^{3}=1\quad\Longrightarrow\quad c=e^{-3}'),
     S(r'That’s the Poisson PMF with $\lambda=3$.', r'X\sim\text{Poisson}(3)')],
    r'(a) $c=\tfrac1{10}$, $F_X(1.5)=0.3$, $P(X\ge2)=0.7$ (b) $c=e^{-3}$, Poisson$(3)$')

D.Q('PMF and CDF · CDF → PMF',
    r'''$X$ has CDF

$$
F_X(x)=\begin{cases}0,&x<1\\ 0.2,&1\le x<2\\ 0.5,&2\le x<4\\ 1,&x\ge4\end{cases}
$$

Find (a) the PMF, (b) $P(X<4)$, (c) $P(1<X\le4)$, (d) $P(X>2)$, (e) $P(X=3)$.''',
    [S(r'(a) **Jumps** at $1$, $2$, $4$ are the PMF.', r'p_X(1)=0.2,\quad p_X(2)=0.5-0.2=0.3,\quad p_X(4)=1-0.5=0.5'),
     S(r'(b) **Rewrite:** “$<4$” is the step just left of $4$.', r'P(X<4)=0.5'),
     S(r'(c) **Rewrite** as a difference.', r'P(1<X\le4)=F(4)-F(1)=1-0.2=0.8'),
     S(r'(d) **Rewrite** as one minus.', r'P(X>2)=1-F(2)=1-0.5=0.5'),
     S(r'(e) No jump at $3$.', r'P(X=3)=0')],
    r'(a) $0.2,0.3,0.5$ at $1,2,4$ (b) $0.5$ (c) $0.8$ (d) $0.5$ (e) $0$')

qn = {k: comb(4, k) * comb(48, 7 - k) / comb(52, 7) for k in range(5)}
assert abs(sum(qn.values()) - 1) < 1e-12 and abs(qn[0] - 0.55036) < 5e-6
D.Q('Named family (Hypergeometric) · Lecture 7',
    'You get 7 cards from a 52-card deck, without replacement. $X$ = number of queens. '
    'Find $P(X=k)$ for $k=0,1,2,3,4$, and $P(X\\ge1)$.',
    [S(r'**Spot:** without replacement, 4 queens out of 52 → Hypergeometric.'),
     S(r'**Write:** pick $k$ queens **and** $7-k$ non-queens.', r'P(X=k)=\frac{\binom4k\binom{48}{7-k}}{\binom{52}{7}}'),
     S(r'**Plug in** $k=0,\dots,4$.', (r'P(0)\approx ' + f'{qn[0]:.4f}' + r',\quad P(1)\approx ' + f'{qn[1]:.4f}' + r',\quad P(2)\approx ' + f'{qn[2]:.4f}',
                                      r'P(3)\approx ' + f'{qn[3]:.4f}' + r',\quad P(4)\approx ' + f'{qn[4]:.5f}')),
     S(r'At least one → one minus none.', r'P(X\ge1)=1-P(X=0)\approx ' + f'{1 - qn[0]:.4f}')],
    f'$\\approx {qn[0]:.4f},\\ {qn[1]:.4f},\\ {qn[2]:.4f},\\ {qn[3]:.4f},\\ {qn[4]:.5f}$; $P(X\\ge1)\\approx {1 - qn[0]:.4f}$',
    cites=cite('L7', 1))

acc = 1 - sum(binom(12, 1 / 30, k) for k in range(4))
D.Q('Named family (Binomial, Bernoulli) · Tutorial 3 Q7',
    'A town had 12 accidents in June (30 days). Each accident is equally likely to be on any day, independently. '
    '(a) Let $Y=1$ if the first accident is on June 13, else $Y=0$. Name the family of $Y$ and give its PMF. '
    '(b) Find the probability that **at least 4** of the 12 fall on June 13.',
    [S(r'(a) **Spot:** one yes/no try → Bernoulli.', r'P(Y=1)=\frac1{30},\qquad P(Y=0)=\frac{29}{30}'),
     S(r'(b) **Spot:** 12 tries, “success” = lands on June 13 → Binomial.', r'n=12,\qquad p=\frac1{30}'),
     S(r'**Write** and use the “at least” shortcut: one minus $k=0,1,2,3$.', r'P(X\ge4)=1-\sum_{k=0}^{3}\binom{12}{k}\Big(\frac1{30}\Big)^k\Big(\frac{29}{30}\Big)^{12-k}'),
     S(r'**Plug in.**', r'P(X\ge4)\approx ' + f'{acc:.5f}')],
    f'(a) Bernoulli$(\\tfrac1{{30}})$ (b) $\\approx {acc:.5f}$, so 4 on one day is very unlikely by chance.', cites=cite('T3', 1))

D.Q('Build a PMF · toss until a head, at most 4 tosses',
    r'A coin with $P(H)=p$ is tossed until the first head **or** until 4 tosses have been made. '
    r'(a) Write the sample space. (b) Let $X$ = number of tosses. Find the PMF of $X$. (c) Evaluate it for $p=\tfrac12$.',
    [S(r'(a) **List:** stop at the first $H$, or after 4 tosses.', r'\Omega=\{H,\ TH,\ TTH,\ TTTH,\ TTTT\}'),
     S(r'(b) **Label:** $X=1,2,3,4,4$. The tosses are independent, so multiply.', r'p_X(1)=p,\quad p_X(2)=(1-p)p,\quad p_X(3)=(1-p)^2p'),
     S(r'**Add:** **two** outcomes give $X=4$.', r'p_X(4)=(1-p)^3p+(1-p)^4=(1-p)^3'),
     S(r'(c) $p=\tfrac12$. **Check:** they add to $1$.', r'\frac12+\frac14+\frac18+\frac18=1')],
    r'$p,\ (1-p)p,\ (1-p)^2p,\ (1-p)^3$; for $p=\tfrac12$: $\tfrac12,\tfrac14,\tfrac18,\tfrac18$.')

nb4 = 0.7 ** 3 + comb(3, 2) * 0.7 ** 3 * 0.3
b35 = comb(5, 3) * 0.7 ** 3 * 0.3 ** 2
D.Q('Named family (Negative Binomial)',
    'A player makes each free throw with probability $0.7$, independently. $X$ = number of shots needed to make **3** baskets. '
    '(a) Name the family. (b) Find $P(X=5)$. (c) Find $P(X\\le4)$. '
    '(d) Compare: the chance of exactly 3 baskets in 5 shots.',
    [S(r'(a) **Spot:** “until the 3rd success” → Negative Binomial, $r=3$, $p=0.7$.'),
     S(r'**Write** the PMF.', r'P(X=k)=\binom{k-1}{2}(0.7)^3(0.3)^{k-3}'),
     S(r'(b) **Plug in** $k=5$: shot 5 goes in, and 2 of the first 4.', r'P(X=5)=\binom42(0.7)^3(0.3)^2\approx ' + f'{nb5:.4f}'),
     S(r'(c) Add $k=3$ and $k=4$.', r'P(X\le4)=(0.7)^3+\binom32(0.7)^3(0.3)\approx ' + f'{nb4:.4f}'),
     S(r'(d) Binomial$(5,0.7)$: the 3 baskets can be **any** 3 of the 5, so it’s bigger.', r'\binom53(0.7)^3(0.3)^2\approx ' + f'{b35:.4f}')],
    f'(a) NB$(3,0.7)$ (b) $\\approx {nb5:.4f}$ (c) $\\approx {nb4:.4f}$ (d) $\\approx {b35:.4f}$')

D.Q('Named family + CDF (Geometric) · Practice 03 Q7',
    r'$N\sim$ Geometric$(p)$, so $P(N=k)=(1-p)^{k-1}p$ for $k=1,2,\dots$ '
    r'(a) Find $P(N>k)$. (b) Find the CDF of $N$. (c) Find $P(N\text{ is even})$. (d) Find $P(N=k\mid N\le m)$.',
    [S(r'(a) $N>k$ means the first $k$ tries all failed (shortcut).', r'P(N>k)=(1-p)^k'),
     S(r'(b) **Rewrite:** one minus the tail. Flat between whole numbers.', r'F_N(k)=1-(1-p)^k,\quad k=1,2,\dots'),
     S(r'(c) Add $k=2,4,6,\dots$: a geometric series with ratio $(1-p)^2$.',
       r'\sum_{j=1}^{\infty}(1-p)^{2j-1}p=\frac{(1-p)p}{1-(1-p)^2}=\frac{1-p}{2-p}'),
     S(r'(d) Conditional = (both) / (given). For $k\le m$, “$N=k$ and $N\le m$” is just $N=k$.',
       r'P(N=k\mid N\le m)=\frac{(1-p)^{k-1}p}{1-(1-p)^m},\quad k=1,\dots,m')],
    r'(a) $(1-p)^k$ (b) $1-(1-p)^k$ (c) $\dfrac{1-p}{2-p}$ (d) $\dfrac{(1-p)^{k-1}p}{1-(1-p)^m}$', diff='advanced', cites=cite('P3', 2))

e0 = exp(-7)
e3 = comb(8, 3) * e0 ** 3 * (1 - e0) ** 5
eg = (1 - e0) ** 2 * e0
D.Q('Two families (Poisson → Binomial, Geometric) · Tutorial 3 Q6',
    'Earthquakes: on average 7 per year (Poisson). '
    '(a) Find the probability of no earthquakes in one year. '
    '(b) Find the probability that **exactly three of the next eight years** have no earthquakes. '
    '(c) Find the probability that the **first** quiet year is year 3.',
    [S(r'(a) **Inside:** Poisson, $\lambda=7$, $k=0$.', r'q=e^{-7}\approx ' + f'{e0:.6f}'),
     S(r'(b) **Outside:** each year is a yes/no try (“quiet”, chance $q$), 8 years → Binomial$(8,q)$.', r'P=\binom83q^3(1-q)^5\approx ' + sci(e3)),
     S(r'(c) **Outside:** “first quiet year” → Geometric$(q)$: two loud years, then a quiet one.', r'P=(1-q)^2q\approx ' + sci(eg))],
    f'(a) $\\approx {e0:.6f}$ (b) $\\approx {sci(e3)}$ (c) $\\approx {sci(eg)}$', diff='advanced', cites=cite('T3', 1))


def verify():
    import sympy as sp
    k = sp.symbols('k', integer=True, positive=True)
    c = sp.Symbol('c')
    assert sp.solve(sp.summation(c * sp.Rational(2, 3) ** k, (k, 1, sp.oo)) - 1, c) == [sp.Rational(1, 2)]
    q = sp.Rational(1, 2)
    assert [q, (1 - q) * q, (1 - q) ** 2 * q, (1 - q) ** 3] == [sp.Rational(1, 2), sp.Rational(1, 4), sp.Rational(1, 8), sp.Rational(1, 8)]
    k0 = sp.symbols('k0', integer=True, nonnegative=True)
    assert sp.simplify(sp.summation(c * 3 ** k0 / sp.factorial(k0), (k0, 0, sp.oo)) - c * sp.exp(3)) == 0
    p = sp.Symbol('p', positive=True)
    j = sp.symbols('j', integer=True, positive=True)
    even = sp.summation((1 - p) ** (2 * j - 1) * p, (j, 1, sp.oo))
    assert sp.simplify(even.subs(p, sp.Rational(1, 3)) - sp.Rational(2, 5)) == 0  # (1-p)/(2-p) at p=1/3
    assert comb(8, 5) * factorial(5) == perm(8, 5)
    # with replacement, the urn count is Binomial(2, 2/3); without it, Hypergeometric(3, 2, 2)
    assert [Fr(comb(2, x) * comb(1, 2 - x), comb(3, 2)) for x in range(3)] == [0, Fr(2, 3), Fr(1, 3)]
    # Practice 02 Q5: totals of two different chips 0-9
    assert [int(v * 45) for v in chips.values()] == [1, 1, 2, 2, 3, 3, 4, 4, 5, 4, 4, 3, 3, 2, 2, 1, 1] and sum(chips.values()) == 1
    assert Fr(comb(3, 1) * comb(7, 3), comb(10, 4)) == Fr(1, 2)
    assert abs(0.8 ** 2 * 0.2 - 0.128) < 1e-12
    print('q1 verify ok')


if __name__ == '__main__':
    verify()
    D.save()
