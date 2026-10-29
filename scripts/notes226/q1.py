r"""Test 2 - Question 1: random experiments, sample spaces, discrete random variables, PMFs and CDFs (Lectures 7-9).

Layout (REWRITE_PLAN.md): you'll see -> the move -> Case 1-5 (formula, short example, full example in
a closed card, shortcut card) -> practice. Step words: Spot, List, Label, Add, Check, Find c, Accumulate, Rewrite,
Write, Plug in, Inside, Outside (the same words as Questions 2-4).
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


D.P(r'**Lectures 7–9.** $X$ turns the result of an experiment into a number that lands on separate values ($0,1,2,\dots$). Find its PMF and CDF.',
    cites=cite('L7', 2) + cite('L8', 5) + cite('L9', 2))

# =====================================================================================================
D.H('Question 1 in plain words')
D.P(r'**You’ll see:** an experiment (coins, dice, chips), a PMF with a $c$, a CDF, or a story with a clue word (“on average”, “until”). Then parts (a), (b), (c).')
D.P(r'**The move:** the **PMF** lists every value of $X$ and its chance. The chances add to $1$. The **CDF** is the running total:')
D.EQ(r'p_X(x)=P(X=x),\qquad \sum_x p_X(x)=1,\qquad F_X(x)=P(X\le x)', cites=cite('L7', 3) + cite('L8', 6))
D.P(r'**Short example:** toss 3 coins, $X$ = number of heads:')
D.EQ(r'p_X(0,1,2,3)=\frac18,\ \frac38,\ \frac38,\ \frac18\qquad\Longrightarrow\qquad F_X(1)=\frac18+\frac38=\frac12')
D.P(r'**Which case?**')
D.T(['The question gives you…', 'Go to'],
    [['an experiment that matches no family', 'Case 1'],
     [r'“$p_X(x)=c\cdot(\dots)$, find $c$”', 'Case 2'],
     ['a CDF, or asks for one', 'Case 3'],
     ['a story with a clue word (“on average”, “until”, “without replacement”)', 'Case 4'],
     ['“in exactly 3 of the next 8 years…”', 'Case 5']])


# =====================================================================================================
D.H('Case 1: build the PMF from an experiment')
D.P(r'**You’ll see:** coins, dice, chips, balls, but no family fits. “Find the PMF of $X$.”')
D.P(r'**The move:** list the outcomes, turn each into a number, and add up the chances of each number.')
D.L([r'**List** all the outcomes (equally likely? count them).',
     r'**Label** each outcome with its value of $X$.',
     r'**Add** the chances of outcomes with the same value.',
     r'**Check:** the PMF adds to $1$.'], ordered=True, cites=cite('L7', 3))
D.P(r'**Short example:** 3 coins: $X=2$ for $hht$, $hth$, $thh$:')
D.EQ(r'P(X=2)=\frac18+\frac18+\frac18=\frac38')
D.CARD(r'Full example (Lecture 7): toss a coin 3 times, $\;X$ = number of heads',
       [(r'**List:** $2^3=8$ equally likely outcomes, each $\tfrac18$.', r'hhh,\ hht,\ hth,\ thh,\ htt,\ tht,\ tth,\ ttt'),
        (r'**Label** each with its number of heads.', (r'X=3:\ hhh\qquad X=2:\ hht,\ hth,\ thh', r'X=1:\ htt,\ tht,\ tth\qquad X=0:\ ttt')),
        (r'**Add** the chances in each group.', r'p_X(0)=\frac18,\quad p_X(1)=\frac38,\quad p_X(2)=\frac38,\quad p_X(3)=\frac18'),
        (r'**Check.** (Practice 02 Q6, boys in a 3-child family, is the same question.)', r'\frac18+\frac38+\frac38+\frac18=1\ \checkmark')],
       r'p_X=\frac18,\ \frac38,\ \frac38,\ \frac18\ \text{ for }x=0,1,2,3', cites=cite('L7', 4))
chips = {s: Fr(sum(1 for a in range(10) for b in range(a + 1, 10) if a + b == s), 45) for s in range(1, 18)}
D.CARD(r'Full example (Practice 02 Q5): the total of two chips',
       [(r'10 chips numbered 0–9; draw 2 without replacement; $S$ = their total. **List:** a pair of different chips, order doesn’t matter.', r'\binom{10}{2}=45\ \text{ equally likely pairs}'),
        (r'**Label:** totals run from $0+1=1$ up to $8+9=17$. Count the pairs for each total. Example $S=9$:', r'\{0,9\},\{1,8\},\{2,7\},\{3,6\},\{4,5\}\quad\Rightarrow\quad 5\text{ pairs}'),
        (r'$S=10$: $\{1,9\},\{2,8\},\{3,7\},\{4,6\}$ (not $\{5,5\}$: one chip can’t be drawn twice).', r'4\text{ pairs}'),
        (r'**Add:** the counts climb $1,1,2,2,3,3,4,4,5$ up to $S=9$, then fall back $4,4,3,3,2,2,1,1$.', r'p_S(s)=\frac{\text{pairs with total }s}{45},\qquad p_S(9)=\frac{5}{45}=\frac19'),
        (r'**Check.**', r'1+1+2+2+3+3+4+4+5+4+4+3+3+2+2+1+1=45\ \checkmark')],
       r'p_S(s)=\frac{1}{45}\times(1,1,2,2,3,3,4,4,5,4,4,3,3,2,2,1,1)\ \text{ for }s=1,\dots,17', cites=cite('P2', 1))
mx = {x: Fr(2 * x - 1, 36) for x in range(1, 7)}
assert mx == {x: Fr(sum(1 for a in range(1, 7) for b in range(1, 7) if max(a, b) == x), 36) for x in range(1, 7)}
D.TRY('Case 1 · Larger of two dice',
      'Two fair dice are rolled. Let $X$ be the **larger** of the two numbers. Find $P(X=x)$ for $x=1,\\dots,6$.',
      [S(r'**List:** $6\cdot6=36$ equally likely pairs $(a,b)$.', r'36\text{ outcomes}'),
       S(r'**Label** $x=3$ as an example: $(1,3),(2,3),(3,3),(3,2),(3,1)$.', r'5\text{ pairs}'),
       S(r'In general: $x$ pairs with $a=x$, plus $x$ with $b=x$, minus $(x,x)$ counted twice.', r'2x-1\text{ pairs}'),
       S(r'**Add:** divide by 36.', r'P(X=x)=\frac{2x-1}{36}'),
       S(r'**Check:** $1+3+5+7+9+11=36$ ✓.')],
      r'$P(X=x)=\dfrac{2x-1}{36}$: $\tfrac1{36},\tfrac3{36},\tfrac5{36},\tfrac7{36},\tfrac9{36},\tfrac{11}{36}$')

# =====================================================================================================
D.H('Case 2: find c (the chances add to 1)')
D.P(r'**You’ll see:** “$p_X(x)=c\cdot(\dots)$. Find $c$.”')
D.P(r'**The move:** add up every chance, set it to $1$, solve. (Same as Question 2, with a sum instead of an area.)')
D.EQ(r'\sum_{\text{all }x}c\cdot(\dots)=1', cites=cite('L7', 5))
D.P(r'**Short example:** $p_X(x)=c(x+1)$ for $x=0,1,2,3$:')
D.EQ(r'c(1+2+3+4)=10c=1\quad\Longrightarrow\quad c=\frac1{10}')
D.CARD(r'Full example (Tutorial 3 Q2): $\;p_X(x)=c\big(\tfrac23\big)^x$, $\;x=1,2,3,\dots$',
       [(r'**Find $c$:** add every chance.', r'\sum_{x=1}^{\infty}c\Big(\frac23\Big)^x=1'),
        (r'Geometric series starting at $1$, ratio $r=\tfrac23$ (card below).', r'\sum_{x=1}^{\infty}\Big(\frac23\Big)^x=\frac{2/3}{1-2/3}=2'),
        (r'Solve.', r'2c=1\quad\Longrightarrow\quad c=\frac12')],
       r'c=\frac12', cites=cite('T3', 1))
D.CARD(r'Sums you’ll need',
       [(r'Geometric series ($|r|<1$), starting at $0$ or at $1$:', r'\sum_{k=0}^{\infty}r^k=\frac{1}{1-r},\qquad \sum_{k=1}^{\infty}r^k=\frac{r}{1-r}'),
        (r'The exponential series (it’s why the Poisson PMF adds to 1):', r'\sum_{k=0}^{\infty}\frac{\lambda^k}{k!}=e^{\lambda}')], numbered=False)

# =====================================================================================================
D.H('Case 3: the CDF (a staircase)')
D.P(r'**You’ll see:** “find the CDF”, “find the PMF from this CDF”, “find $P(a<X\le b)$”.')
D.P(r'**The move:** the CDF is a **staircase**. It’s flat between values and **jumps by $p_X(x)$** at each value:')
D.EQ(r'F_X(x)=P(X\le x)=\sum_{k\le x}p_X(k)', cites=cite('L8', 6))
D.L([r'**Accumulate** (PMF → CDF): keep a running total, adding each jump as you pass a value.',
     r'**Jumps** (CDF → PMF): the jump sizes are the PMF.',
     r'**Rewrite** the probability asked with $F$’s (card below).'], ordered=True)
D.P(r'**Short example:** 3 coins, the running total:')
D.EQ(r'0\ \to\ \frac18\ \to\ \frac12\ \to\ \frac78\ \to\ 1')
D.CARD(r'Rewrite: turn any probability into $F$’s',
       [(r'Up to $b$:', r'P(X\le b)=F_X(b)'),
        (r'Above $a$:', r'P(X>a)=1-F_X(a)'),
        (r'Between:', r'P(a<X\le b)=F_X(b)-F_X(a)'),
        (r'One value: the jump there ($0$ if no jump).', r'P(X=a)=\text{jump at }a'),
        (r'**For whole numbers, turn $<$ into $\le$ first:**', r'P(X<4)=P(X\le3)=F_X(3)')], numbered=False, cites=cite('L9', 4))
D.CARD(r'Full example (Lecture 9): the CDF of the 3-coin count',
       [(r'**Accumulate:** start at $0$, jump $\tfrac18$ at $0$, $\tfrac38$ at $1$, $\tfrac38$ at $2$, $\tfrac18$ at $3$.',
         r'F_X(x)=\begin{cases}0,&x<0\\ \frac18,&0\le x<1\\ \frac12,&1\le x<2\\ \frac78,&2\le x<3\\ 1,&x\ge3\end{cases}'),
        (r'**Rewrite** $P(1<X\le3)$.', r'F_X(3)-F_X(1)=1-\frac12=\frac12')],
       r'\text{a staircase }0\to\frac18\to\frac12\to\frac78\to1', cites=cite('L9', 2))
D.GRAPH(['title "CDF of the number of heads in 3 tosses"', 'x -1 4.5 label="$x$" height=240', 'y 0 1.1 label="$F_X(x)$"']
        + steps([(0, 1 / 8), (1, 3 / 8), (2, 3 / 8), (3, 1 / 8)], -1, 4.5, color=2)
        + ['hline "1"', 'text "0.35" "0.2" "jump $\\tfrac18$"', 'text "1.4" "0.6" "jump $\\tfrac38$"'],
        intro='**What does it look like?** At each jump, the value is the **top** of the step (the dot).')
D.CARD(r'Full example (Practice 03 Q9): from a CDF back to the PMF',
       [(r'$F_X=0$ for $x<-3$, $\tfrac38$ on $[-3,0)$, $\tfrac34$ on $[0,6)$, $1$ for $x\ge6$. It’s a staircase, so $X$ is **discrete**.', r'X\in\{-3,\ 0,\ 6\}'),
        (r'**Jumps** = the PMF.', r'p_X(-3)=\frac38,\quad p_X(0)=\frac34-\frac38=\frac38,\quad p_X(6)=1-\frac34=\frac14'),
        (r'**Rewrite** $P(-3<X\le6)$.', r'F_X(6)-F_X(-3)=1-\frac38=\frac58'),
        (r'**Rewrite** $P(X<0)$: the step just left of $0$.', r'P(X<0)=\frac38')],
       r'p_X=\frac38,\ \frac38,\ \frac14\ \text{ at }-3,\ 0,\ 6', cites=cite('P3', 3))

# =====================================================================================================
D.H('Case 4: a named family (spot the clue word)')
D.P(r'**You’ll see:** a story. A clue word tells you the family; its PMF is ready-made. **Spot** the clue:')
D.T(['Clue in the question', 'Family'],
    [['**one** yes/no try', 'Bernoulli'],
     ['**fixed number $n$** of tries, count successes', 'Binomial'],
     ['tries **until the first** success', 'Geometric'],
     ['tries **until the $r$-th** success', 'Negative Binomial'],
     ['draw $n$ **without replacement**', 'Hypergeometric'],
     ['“**on average** $\\lambda$ per hour/page/year”', 'Poisson']], cites=cite('L8', 5))
D.L([r'**Spot** the family and its numbers ($n$, $p$, $\lambda$, …).',
     r'**Write** its PMF with those numbers.',
     r'**Plug in** $k$. “At least” → $1-$ (the few below).'], ordered=True)
D.P(r'Open a card for the formula and a short example:')
D.CARD(r'Bernoulli$(p)$: $\;P(1)=p$, $\;P(0)=1-p$',
       [(r'One yes/no try. Example: is the first of 12 accidents on June 13?', r'P(Y=1)=\frac1{30},\qquad P(Y=0)=\frac{29}{30}')], numbered=False)
D.CARD(r'Binomial$(n,p)$: $\;\dbinom nk\,p^k(1-p)^{n-k}$, $\;k=0,\dots,n$',
       [(r'$n$ independent tries, count the successes. Example: 8 bits, each wrong with $p=0.1$, exactly 1 wrong:',
         r'\binom81(0.1)(0.9)^7\approx' + f'{binom(8, 0.1, 1):.4f}'),
        (r'$\binom nk$ = “choose $k$ of $n$”, the only counting you need. On the Casio: `n nCr k`.', r'\binom{8}{1}=8,\qquad \binom{10}{2}=45'),
        (r'With replacement → Binomial. Without → Hypergeometric.', '')], numbered=False)
D.CARD(r'Geometric$(p)$: $\;(1-p)^{k-1}p$, $\;k=1,2,\dots$',
       [(r'Tries until the first success: $k-1$ failures, then a success. Example: each try works with $0.2$; succeed on try 3:', r'(0.8)^2(0.2)=0.128'),
        (r'Shortcut: “more than $k$ tries” = the first $k$ all failed.', r'P(X>k)=(1-p)^k')], numbered=False)
nb5 = comb(4, 2) * 0.7 ** 3 * 0.3 ** 2
D.CARD(r'Negative Binomial$(r,p)$: $\;\dbinom{k-1}{r-1}p^r(1-p)^{k-r}$, $\;k=r,r+1,\dots$',
       [(r'Tries until the $r$-th success. The **last** try is a success; $\binom{k-1}{r-1}$ picks where the other $r-1$ go among the first $k-1$.', ''),
        (r'Example: free throws with $0.7$; the 3rd basket on shot 5.', r'\binom42(0.7)^3(0.3)^2\approx' + f'{nb5:.4f}')], numbered=False)
hy = {k: Fr(comb(3, k) * comb(7, 4 - k), comb(10, 4)) for k in range(4)}
assert hy == {0: Fr(1, 6), 1: Fr(1, 2), 2: Fr(3, 10), 3: Fr(1, 30)}
D.CARD(r'Hypergeometric: $\;\dfrac{\binom Kk\binom{N-K}{n-k}}{\binom Nn}$',
       [(r'Draw $n$ from $N$ without replacement, $K$ of them “good”. Pick $k$ good **and** $n-k$ bad.', ''),
        (r'Example: 10 chips, 3 defective, choose 4. Exactly 1 defective:', r'\frac{\binom31\binom73}{\binom{10}{4}}=\frac{3\cdot35}{210}=\frac12')], numbered=False)
p3, p4 = pois(4, 3), pois(4, 4)
assert abs(p3 - p4) < 1e-12 and abs(p3 - 0.1954) < 5e-5
D.CARD(r'Poisson$(\lambda)$: $\;e^{-\lambda}\dfrac{\lambda^k}{k!}$, $\;k=0,1,2,\dots$',
       [(r'“On average $\lambda$ per …”. **Scale $\lambda$ to the time asked.** Example (Lecture 8): 4 emails per hour, exactly 3 next hour:', r'P(X=3)=e^{-4}\frac{4^3}{3!}\approx' + f'{p3:.4f}'),
        (r'Same rate, a 30-minute window: $\lambda=2$.', r'P(X=0)=e^{-2}\approx' + f'{exp(-2):.4f}')], numbered=False, cites=cite('L8', 3))
D.CO('warning', r'**Poisson: scale $\lambda$ to the time asked.** 7 per week, a question about one day → $\lambda=1$.')
D.CARD(r'Shortcut: “at least” → one minus the rest',
       [(r'At least one:', r'P(X\ge1)=1-P(X=0)'),
        (r'At least 4 (Binomial, Poisson): subtract the few values below.', r'P(X\ge4)=1-\big[P(0)+P(1)+P(2)+P(3)\big]')], numbered=False)
g3, g4 = 0.8 ** 2 * 0.2, 0.8 ** 3
D.TRY('Case 4 · Retransmit until it works',
      'A packet is sent again and again until one gets through. Each try works with probability $0.2$, independently. '
      '$X$ = number of tries. Find $P(X=3)$ and $P(X>3)$.',
      [S(r'**Spot:** “until it works” → Geometric, $p=0.2$.'),
       S(r'**Write** the PMF.', r'P(X=k)=(0.8)^{k-1}(0.2)'),
       S(r'**Plug in** $k=3$: fail, fail, work.', r'P(X=3)=(0.8)^2(0.2)=' + num(g3)),
       S(r'$X>3$: the first 3 all failed (shortcut).', r'P(X>3)=(0.8)^3=' + num(g4))],
      f'$P(X=3)={num(g3)}$, $P(X>3)={num(g4)}$')

# =====================================================================================================
D.H('Case 5: two families in one question')
D.P(r'**You’ll see:** “in exactly 3 of the next 8 years…”, “the first day with no…”.')
D.P(r'**The move:** one family **inside** gives the chance $q$ that a single year/day/page is “good”. Then **outside**, each year is a yes/no try with chance $q$.')
D.L([r'**Inside:** use the first family (often Poisson with $k=0$) to get $q$.',
     r'**Outside:** count the good ones → Binomial$(n,q)$. Wait for the first → Geometric$(q)$.'], ordered=True)
D.P(r'**Short example:** typos are Poisson, 2 per page. A page is clean with $q=e^{-2}$. Exactly 1 of 5 pages clean:')
D.EQ(r'\binom51\,q\,(1-q)^4,\qquad q=e^{-2}')

# =====================================================================================================
D.H('Practice Questions')
D.CO('tip', r'''**Question 1 is always these cases, in parts (a), (b), (c).** Spot the case, run its steps:

1. **No family:** List → Label → Add → Check.
2. **A $c$:** add every chance, set it to $1$.
3. **CDF:** running total; jumps = the PMF; $P(a<X\le b)=F(b)-F(a)$; whole numbers: $<$ → $\le$.
4. **Clue word:** Spot → Write → Plug in. Scale Poisson’s $\lambda$. “At least” → $1-$ the rest.
5. **Two families:** Inside gives $q$, Outside is Binomial or Geometric.''')
D.P('Test-style, easy → hard. Solve on paper first, then open the solution.')

d1, d2, d3 = pois(1, 2), 1 - exp(-1), 1 - exp(-1 / 3)
D.Q('Case 4 (Poisson) · Tutorial 3 Q3, Q5',
    'A mail-order house gets on average **7 wrong-number calls per week** (Poisson). Find the probability that tomorrow they get '
    '(a) exactly two wrong-number calls, (b) at least one. '
    '(c) A book has on average one typo every **three pages** (Poisson). Find the chance a given page has at least one typo.',
    [S(r'**Spot:** “on average” → Poisson. Scale $\lambda$ to one day.', r'\lambda=\frac{7}{7}=1'),
     S(r'(a) **Write** and **plug in** $k=2$.', r'P(X=2)=e^{-1}\frac{1^2}{2!}\approx ' + f'{d1:.4f}'),
     S(r'(b) **At least one** → one minus none.', r'P(X\ge1)=1-e^{-1}\approx ' + f'{d2:.4f}'),
     S(r'(c) Scale to one page: $\lambda=\tfrac13$. Then one minus none.', r'P(X\ge1)=1-e^{-1/3}\approx ' + f'{d3:.4f}')],
    f'(a) $\\approx {d1:.4f}$ (b) $\\approx {d2:.4f}$ (c) $\\approx {d3:.4f}$', diff='introductory', cites=cite('T3', 1))

D.Q('Case 1 · with and without replacement · like Practice 01 Q7',
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

D.Q('Case 2 + 3 · find $c$, then the CDF',
    r'(a) $p_X(x)=c\,(x+1)$ for $x=0,1,2,3$. Find $c$, then $F_X(1.5)$ and $P(X\ge2)$. '
    r'(b) $p_X(k)=c\,\dfrac{3^k}{k!}$ for $k=0,1,2,\dots$ Find $c$. Which family is this?',
    [S(r'(a) **Find $c$:** add every chance.', r'c(1+2+3+4)=10c=1\quad\Longrightarrow\quad c=\frac1{10}'),
     S(r'So the PMF is $0.1,0.2,0.3,0.4$. **Accumulate** every value $\le1.5$: $x=0,1$.', r'F_X(1.5)=0.1+0.2=0.3'),
     S(r'**Rewrite:** $X\ge2$ is one minus $X\le1$.', r'P(X\ge2)=1-F_X(1)=1-0.3=0.7'),
     S(r'(b) **Find $c$** with the exponential series, $\sum\frac{3^k}{k!}=e^3$.', r'c\,e^{3}=1\quad\Longrightarrow\quad c=e^{-3}'),
     S(r'That’s the Poisson PMF with $\lambda=3$.', r'X\sim\text{Poisson}(3)')],
    r'(a) $c=\tfrac1{10}$, $F_X(1.5)=0.3$, $P(X\ge2)=0.7$ (b) $c=e^{-3}$, Poisson$(3)$')

D.Q('Case 3 · CDF → PMF',
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
D.Q('Case 4 (Hypergeometric) · Lecture 7',
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
D.Q('Case 4 (Binomial, Bernoulli) · Tutorial 3 Q7',
    'A town had 12 accidents in June (30 days). Each accident is equally likely to be on any day, independently. '
    '(a) Let $Y=1$ if the first accident is on June 13, else $Y=0$. Name the family of $Y$ and give its PMF. '
    '(b) Find the probability that **at least 4** of the 12 fall on June 13.',
    [S(r'(a) **Spot:** one yes/no try → Bernoulli.', r'P(Y=1)=\frac1{30},\qquad P(Y=0)=\frac{29}{30}'),
     S(r'(b) **Spot:** 12 tries, “success” = lands on June 13 → Binomial.', r'n=12,\qquad p=\frac1{30}'),
     S(r'**Write** and use the “at least” shortcut: one minus $k=0,1,2,3$.', r'P(X\ge4)=1-\sum_{k=0}^{3}\binom{12}{k}\Big(\frac1{30}\Big)^k\Big(\frac{29}{30}\Big)^{12-k}'),
     S(r'**Plug in.**', r'P(X\ge4)\approx ' + f'{acc:.5f}')],
    f'(a) Bernoulli$(\\tfrac1{{30}})$ (b) $\\approx {acc:.5f}$, so 4 on one day is very unlikely by chance.', cites=cite('T3', 1))

D.Q('Case 1 · toss until a head, at most 4 tosses',
    r'A coin with $P(H)=p$ is tossed until the first head **or** until 4 tosses have been made. '
    r'(a) Write the sample space. (b) Let $X$ = number of tosses. Find the PMF of $X$. (c) Evaluate it for $p=\tfrac12$.',
    [S(r'(a) **List:** stop at the first $H$, or after 4 tosses.', r'\Omega=\{H,\ TH,\ TTH,\ TTTH,\ TTTT\}'),
     S(r'(b) **Label:** $X=1,2,3,4,4$. The tosses are independent, so multiply.', r'p_X(1)=p,\quad p_X(2)=(1-p)p,\quad p_X(3)=(1-p)^2p'),
     S(r'**Add:** **two** outcomes give $X=4$.', r'p_X(4)=(1-p)^3p+(1-p)^4=(1-p)^3'),
     S(r'(c) $p=\tfrac12$. **Check:** they add to $1$.', r'\frac12+\frac14+\frac18+\frac18=1')],
    r'$p,\ (1-p)p,\ (1-p)^2p,\ (1-p)^3$; for $p=\tfrac12$: $\tfrac12,\tfrac14,\tfrac18,\tfrac18$.')

nb4 = 0.7 ** 3 + comb(3, 2) * 0.7 ** 3 * 0.3
b35 = comb(5, 3) * 0.7 ** 3 * 0.3 ** 2
D.Q('Case 4 (Negative Binomial)',
    'A player makes each free throw with probability $0.7$, independently. $X$ = number of shots needed to make **3** baskets. '
    '(a) Name the family. (b) Find $P(X=5)$. (c) Find $P(X\\le4)$. '
    '(d) Compare: the chance of exactly 3 baskets in 5 shots.',
    [S(r'(a) **Spot:** “until the 3rd success” → Negative Binomial, $r=3$, $p=0.7$.'),
     S(r'**Write** the PMF.', r'P(X=k)=\binom{k-1}{2}(0.7)^3(0.3)^{k-3}'),
     S(r'(b) **Plug in** $k=5$: shot 5 goes in, and 2 of the first 4.', r'P(X=5)=\binom42(0.7)^3(0.3)^2\approx ' + f'{nb5:.4f}'),
     S(r'(c) Add $k=3$ and $k=4$.', r'P(X\le4)=(0.7)^3+\binom32(0.7)^3(0.3)\approx ' + f'{nb4:.4f}'),
     S(r'(d) Binomial$(5,0.7)$: the 3 baskets can be **any** 3 of the 5, so it’s bigger.', r'\binom53(0.7)^3(0.3)^2\approx ' + f'{b35:.4f}')],
    f'(a) NB$(3,0.7)$ (b) $\\approx {nb5:.4f}$ (c) $\\approx {nb4:.4f}$ (d) $\\approx {b35:.4f}$')

D.Q('Case 4 + 3 (Geometric and its CDF) · Practice 03 Q7',
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
D.Q('Case 5 (Poisson → Binomial, Geometric) · Tutorial 3 Q6',
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
