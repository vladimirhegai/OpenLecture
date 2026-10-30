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
D.CO('tip', r'''**Question 1 is always one of these three, in parts (a), (b), (c).** Spot which kind, then run its steps:

1. **PMF and CDF:** build the PMF with List → Label → Add → Check. CDF = running total; jumps = the PMF; $P(a<X\le b)=F(b)-F(a)$; whole numbers: $<$ → $\le$.
2. **Find $c$:** add every chance, set the total to $1$, solve. Then use the PMF like any other.
3. **Poisson:** scale $\lambda$ to the time asked, then $e^{-\lambda}\lambda^k/k!$. “At least one” $=1-e^{-\lambda}$.''')
D.P('Test-style, easy → medium, same level as the practice sets. Solve on paper first, then open the solution.')

# ---- PMF and CDF
D.Q('PMF and CDF · 2 coins',
    r'Toss a fair coin twice. $X$ = the number of heads. Find (a) the PMF of $X$, (b) the CDF of $X$, (c) $P(X\ge1)$.',
    [S(r'(a) **List:** $2^2=4$ equally likely outcomes, each $\tfrac14$.', r'hh,\ ht,\ th,\ tt'),
     S(r'**Label** and **add:** $X=2$: $hh$. $X=1$: $ht,th$. $X=0$: $tt$.', r'p_X(0)=\frac14,\quad p_X(1)=\frac12,\quad p_X(2)=\frac14'),
     S(r'**Check:** they add to $1$.', r'\frac14+\frac12+\frac14=1\ \checkmark'),
     S(r'(b) **Accumulate:** add each chance as you pass $0$, $1$, $2$.',
       r'F_X(x)=\begin{cases}0,&x<0\\ \frac14,&0\le x<1\\ \frac34,&1\le x<2\\ 1,&x\ge2\end{cases}'),
     S(r'(c) **Rewrite:** at least one = one minus none.', r'P(X\ge1)=1-p_X(0)=1-\frac14=\frac34')],
    r'(a) $\tfrac14,\tfrac12,\tfrac14$ for $x=0,1,2$ (b) the staircase $0,\tfrac14,\tfrac34,1$ (c) $\tfrac34$',
    diff='introductory', cites=cite('L7', 4))

D.Q('PMF and CDF · with and without replacement · like Practice 01 Q7',
    'An urn has 2 black balls and 1 white ball. Two balls are drawn one after the other. $X$ = number of black balls drawn. '
    'Find the PMF of $X$ (a) **without** replacement, (b) **with** replacement.',
    [S(r'(a) **List** ordered draws, calling the black balls $B_1,B_2$: 6 equally likely.', r'B_1B_2,\ B_2B_1,\ B_1W,\ B_2W,\ WB_1,\ WB_2'),
     S(r'**Label** and **add:** two have both black, four have one, none have zero.', r'P(X=2)=\frac26=\frac13,\quad P(X=1)=\frac46=\frac23,\quad P(X=0)=0'),
     S(r'(b) With replacement, each draw is black with $\tfrac23$, independently. **Add** the two orders for $X=1$ (BW and WB).',
       (r'P(X=2)=\Big(\frac23\Big)^2=\frac49,\qquad P(X=0)=\Big(\frac13\Big)^2=\frac19', r'P(X=1)=2\cdot\frac23\cdot\frac13=\frac49')),
     S(r'**Check:** both PMFs add to $1$.', r'\frac13+\frac23=1,\qquad \frac49+\frac49+\frac19=1')],
    r'(a) $0,\tfrac23,\tfrac13$ for $x=0,1,2$ (b) $\tfrac19,\tfrac49,\tfrac49$',
    diff='introductory', cites=cite('P1', 1))

D.Q('PMF and CDF · PMF → CDF → probabilities',
    r'$X$ takes the values $-1$, $0$, $2$ with $p_X(-1)=0.2$, $p_X(0)=0.5$, $p_X(2)=0.3$. '
    r'Find (a) the CDF, (b) $F_X(1)$, (c) $P(X<2)$, (d) $P(-1<X\le2)$, (e) $P(X>0)$.',
    [S(r'(a) **Accumulate:** start at $0$, add each chance as you pass $-1$, $0$, $2$.',
       r'F_X(x)=\begin{cases}0,&x<-1\\ 0.2,&-1\le x<0\\ 0.7,&0\le x<2\\ 1,&x\ge2\end{cases}'),
     S(r'(b) $x=1$ sits on the flat step $[0,2)$.', r'F_X(1)=0.7'),
     S(r'(c) **Rewrite:** whole steps, so “$<2$” is the step just left of $2$.', r'P(X<2)=0.2+0.5=0.7'),
     S(r'(d) **Rewrite** as a difference.', r'P(-1<X\le2)=F_X(2)-F_X(-1)=1-0.2=0.8'),
     S(r'(e) **Rewrite** as one minus.', r'P(X>0)=1-F_X(0)=1-0.7=0.3')],
    r'(a) staircase $0,\ 0.2,\ 0.7,\ 1$ (b) $0.7$ (c) $0.7$ (d) $0.8$ (e) $0.3$', diff='introductory')

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
    r'(a) $0.2,0.3,0.5$ at $1,2,4$ (b) $0.5$ (c) $0.8$ (d) $0.5$ (e) $0$', cites=cite('P3', 3))

D.Q('PMF and CDF · toss until a head, at most 4 tosses',
    r'A coin with $P(H)=p$ is tossed until the first head **or** until 4 tosses have been made. '
    r'(a) Write the sample space. (b) Let $X$ = number of tosses. Find the PMF of $X$. (c) Evaluate it for $p=\tfrac12$ and find $F_X(2)$.',
    [S(r'(a) **List:** stop at the first $H$, or after 4 tosses.', r'\Omega=\{H,\ TH,\ TTH,\ TTTH,\ TTTT\}'),
     S(r'(b) **Label:** $X=1,2,3,4,4$. The tosses are independent, so multiply.', r'p_X(1)=p,\quad p_X(2)=(1-p)p,\quad p_X(3)=(1-p)^2p'),
     S(r'**Add:** **two** outcomes give $X=4$.', r'p_X(4)=(1-p)^3p+(1-p)^4=(1-p)^3'),
     S(r'(c) $p=\tfrac12$. **Check:** they add to $1$.', r'\frac12+\frac14+\frac18+\frac18=1\ \checkmark'),
     S(r'**Accumulate** up to $2$.', r'F_X(2)=\frac12+\frac14=\frac34')],
    r'$p,\ (1-p)p,\ (1-p)^2p,\ (1-p)^3$; for $p=\tfrac12$: $\tfrac12,\tfrac14,\tfrac18,\tfrac18$ and $F_X(2)=\tfrac34$.')

# ---- Find c
D.Q('Find $c$ · a finite PMF',
    r'(a) $p_X(x)=c\,(x+1)$ for $x=0,1,2,3$. Find $c$, then $F_X(1.5)$ and $P(X\ge2)$. '
    r'(b) $p_X(x)=c\,x^2$ for $x=1,2,3$. Find $c$ and $P(X\le2)$.',
    [S(r'(a) **Find $c$:** add every chance, set to $1$.', r'c(1+2+3+4)=10c=1\quad\Longrightarrow\quad c=\frac1{10}'),
     S(r'So the PMF is $0.1,0.2,0.3,0.4$. **Accumulate** every value $\le1.5$: $x=0,1$.', r'F_X(1.5)=0.1+0.2=0.3'),
     S(r'**Rewrite:** $X\ge2$ is one minus $X\le1$.', r'P(X\ge2)=1-F_X(1)=1-0.3=0.7'),
     S(r'(b) **Find $c$:**', r'c(1+4+9)=14c=1\quad\Longrightarrow\quad c=\frac1{14}'),
     S(r'**Accumulate** $x=1,2$.', r'P(X\le2)=\frac{1+4}{14}=\frac5{14}')],
    r'(a) $c=\tfrac1{10}$, $F_X(1.5)=0.3$, $P(X\ge2)=0.7$ (b) $c=\tfrac1{14}$, $P(X\le2)=\tfrac5{14}$', diff='introductory')

D.Q('Find $c$ · an infinite PMF · like Tutorial 3 Q2',
    r'(a) $p_X(k)=c\big(\tfrac13\big)^k$ for $k=0,1,2,\dots$ Find $c$ and $P(X\ge1)$. '
    r'(b) $p_X(k)=c\,\dfrac{2^k}{k!}$ for $k=0,1,2,\dots$ Find $c$ and $P(X=1)$. Which family is this?',
    [S(r'(a) **Find $c$:** a geometric series starting at $k=0$, ratio $r=\tfrac13$.', r'\sum_{k=0}^{\infty}\Big(\frac13\Big)^k=\frac{1}{1-\frac13}=\frac32\quad\Longrightarrow\quad \frac32c=1\quad\Longrightarrow\quad c=\frac23'),
     S(r'**Rewrite:** at least one = one minus $k=0$.', r'P(X\ge1)=1-c\Big(\frac13\Big)^0=1-\frac23=\frac13'),
     S(r'(b) **Find $c$** with the exponential series, $\sum\frac{2^k}{k!}=e^2$.', r'c\,e^{2}=1\quad\Longrightarrow\quad c=e^{-2}'),
     S(r'**Plug in** $k=1$.', r'P(X=1)=e^{-2}\frac{2^1}{1!}=2e^{-2}\approx' + f'{2 * exp(-2):.4f}'),
     S(r'That’s the Poisson PMF with $\lambda=2$.', r'X\sim\text{Poisson}(2)')],
    f'(a) $c=\\tfrac23$, $P(X\\ge1)=\\tfrac13$ (b) $c=e^{{-2}}$, $P(X=1)\\approx {2 * exp(-2):.4f}$, Poisson$(2)$', cites=cite('T3', 1))

# ---- Poisson
d1, d2, d3 = pois(1, 2), 1 - exp(-1), 1 - exp(-1 / 3)
D.Q('Poisson · Tutorial 3 Q3, Q5',
    'A mail-order house gets on average **7 wrong-number calls per week** (Poisson). Find the probability that tomorrow they get '
    '(a) exactly two wrong-number calls, (b) at least one. '
    '(c) A book has on average one typo every **three pages** (Poisson). Find the chance a given page has at least one typo.',
    [S(r'**Spot:** “on average” → Poisson. **Read off:** scale $\lambda$ to one day.', r'\lambda=\frac{7}{7}=1'),
     S(r'(a) **Plug in** $k=2$.', r'P(X=2)=e^{-1}\frac{1^2}{2!}\approx ' + f'{d1:.4f}'),
     S(r'(b) **At least one** → one minus none.', r'P(X\ge1)=1-e^{-1}\approx ' + f'{d2:.4f}'),
     S(r'(c) Scale to one page: $\lambda=\tfrac13$. Then one minus none.', r'P(X\ge1)=1-e^{-1/3}\approx ' + f'{d3:.4f}')],
    f'(a) $\\approx {d1:.4f}$ (b) $\\approx {d2:.4f}$ (c) $\\approx {d3:.4f}$', diff='introductory', cites=cite('T3', 1))

c2, c_le2, c0 = pois(3, 2), exp(-3) * (1 + 3 + 4.5), exp(-1)
D.Q('Poisson · customers per hour',
    'Customers arrive at a counter at **3 per hour** on average (Poisson). Find the chance of '
    '(a) exactly 2 customers in the next hour, (b) **at most** 2 customers in the next hour, (c) no customers in the next 20 minutes.',
    [S(r'**Spot:** “on average … per hour” → Poisson. (a) **Read off:** one hour, so $\lambda=3$.', r'\lambda=3,\qquad k=2'),
     S(r'**Plug in:**', r'P(X=2)=e^{-3}\frac{3^2}{2!}=4.5\,e^{-3}\approx' + f'{c2:.4f}'),
     S(r'(b) **At most 2** = add $k=0,1,2$.', r'P(X\le2)=e^{-3}\Big(1+3+\frac{9}{2}\Big)=8.5\,e^{-3}\approx' + f'{c_le2:.4f}'),
     S(r'(c) **Read off:** 20 minutes is a third of an hour → a third of the average.', r'\lambda=\frac{3}{3}=1,\qquad k=0'),
     S(r'**Plug in:**', r'P(X=0)=e^{-1}\approx' + f'{c0:.4f}')],
    f'(a) $\\approx {c2:.4f}$ (b) $\\approx {c_le2:.4f}$ (c) $\\approx {c0:.4f}$')

t0, t2, t6 = exp(-2), 1 - 3 * exp(-2), exp(-6)
D.Q('Poisson · typos per page',
    'A report has on average **2 typos per page** (Poisson). Find the chance that '
    '(a) a given page has no typos, (b) a given page has **at least 2** typos, (c) a 3-page section has no typos.',
    [S(r'(a) **Read off:** one page, $\lambda=2$, $k=0$. **Plug in:**', r'P(X=0)=e^{-2}\approx' + f'{t0:.4f}'),
     S(r'(b) **At least 2** = one minus $k=0,1$.', r'P(X\ge2)=1-e^{-2}\Big(1+2\Big)=1-3e^{-2}\approx' + f'{t2:.4f}'),
     S(r'(c) **Read off:** 3 pages → $\lambda=3\cdot2=6$, $k=0$.', r'P(X=0)=e^{-6}\approx' + f'{t6:.5f}')],
    f'(a) $\\approx {t0:.4f}$ (b) $\\approx {t2:.4f}$ (c) $\\approx {t6:.5f}$')


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
    assert sp.solve(sp.summation(c * sp.Rational(1, 3) ** k0, (k0, 0, sp.oo)) - 1, c) == [sp.Rational(2, 3)]
    assert sp.solve(c * sum(x ** 2 for x in (1, 2, 3)) - 1, c) == [sp.Rational(1, 14)]
    print('q1 verify ok')


if __name__ == '__main__':
    verify()
    D.save()
