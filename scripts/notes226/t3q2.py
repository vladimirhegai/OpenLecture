r"""Test 3 - Question 2: discrete conditional distributions and conditional expectation."""
from fractions import Fraction as Fr

from lib226 import Doc, S, cite

D = Doc('t3q2', 'Test 3 - Question 2', ['conditional_pmf', 'conditional_cdf', 'conditional_expectation', 'independence'])

D.P(r'**Test 3, Question 2 · Discrete conditional distributions and expectation**')
D.P(r'Read the bar $\mid$ as “given.” In $P(X=x\mid Y=y)$, you already know that $Y=y$. The question is how likely $X=x$ is among the outcomes that fit that information.',
    cites=cite('L21', 1))
D.P(r'First turn the selected outcomes into a probability distribution. Then use those probabilities to find a running total (a CDF) or a weighted average (a conditional expectation).', cites=cite('L22', 4))

# =====================================================================================================
D.H('Find a conditional PMF')
D.P(r'A **conditional PMF** gives the probability of each possible value after you learn the condition. When you know $Y=y$, keep the cells labeled with that value of $Y$.', cites=cite('L21', 1))
D.L([r'**Select.** Find the row or column labeled $Y=y$.',
     r'**Add.** Its total is $p_Y(y)$, the chance of the condition itself.',
     r'**Divide.** Divide each selected cell by that total. The new probabilities should add to $1$.'], ordered=True)
D.EQ(r'p_{X|Y}(x\mid y)=\frac{p_{X,Y}(x,y)}{p_Y(y)}\qquad\text{for }p_Y(y)>0')
D.P(r'The numerator is the chance that both conditions hold. The denominator makes the selected group the whole set you are working with. If its total is zero, the formula is undefined.')

D.EX('Condition on a row or column ★ (Tutorial 7 Q3)',
     r'''Using the table, find $p_{X|Y}(x\mid1)$ and $p_{Y|X}(y\mid1)$.

| | $y=0$ | $y=1$ | $y=2$ |
|---|---|---|---|
| $x=0$ | $0.10$ | $0.15$ | $0.05$ |
| $x=1$ | $0.20$ | $0.30$ | $0.20$ |''',
     [S(r'**Given $Y=1$.** The selected column contains $0.15$ and $0.30$. Its total is $0.45$.'),
      S(r'**Divide each cell by $0.45$.** The cell for $X=1$ is twice as large as the one for $X=0$. After dividing, it still has twice the probability.',
        (r'p_{X|Y}(0\mid1)=\frac{0.15}{0.45}=\frac13', r'p_{X|Y}(1\mid1)=\frac{0.30}{0.45}=\frac23')),
      S(r'**Given $X=1$.** This time use the row labeled $X=1$. Its total is $0.20+0.30+0.20=0.70$.',
        (r'p_{Y|X}(0\mid1)=\frac{0.20}{0.70}=\frac27', r'p_{Y|X}(1\mid1)=\frac{0.30}{0.70}=\frac37', r'p_{Y|X}(2\mid1)=\frac{0.20}{0.70}=\frac27')),
      S(r'**Check.** The two probabilities in the first calculation add to $1$. The three in the second calculation also add to $1$.')],
     r'Given $Y=1$, use $\tfrac13,\tfrac23$ at $x=0,1$. Given $X=1$, use $\tfrac27,\tfrac37,\tfrac27$ at $y=0,1,2$.', cites=cite('T7', 1))

D.H('Turn the conditional PMF into a CDF')
D.P(r'The **conditional CDF** adds the conditional probabilities up to and including a cutoff. For instance, $F_{X|Y}(0.8\mid1)=\tfrac13$ in the table above because only $X=0$ is at or below $0.8$.', cites=cite('L21', 1))
D.EQ(r'F_{X|Y}(x\mid y)=P(X\le x\mid Y=y)=\sum_{a\le x}p_{X|Y}(a\mid y)')
D.P(r'The total jumps at each possible value of $X$. It stays flat between jumps because there are no new values to count. At a jump, include the probability at that value.')

D.EX('List the dice rolls that fit the condition ★ (Lecture 21)',
     r'Roll two fair dice. $X$ is the first die and $Y$ is their sum. Find the conditional PMF and CDF of $X$ given $Y=7$.',
     [S(r'**Select.** Only six rolls have sum $7$. They are $(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)$.'),
      S(r'**Divide.** The six rolls are equally likely. Exactly one has first die $x$, so each possible $x$ has one sixth of the selected probability.',
        r'p_{X|Y}(x\mid7)=\frac{1/36}{6/36}=\frac16,\qquad x=1,2,\ldots,6'),
      S(r'**Add up to the cutoff.** At $x=2.5$, include $1$ and $2$. At $x=3$, include $3$ as well.',
        (r'F_{X|Y}(2.5\mid7)=\frac16+\frac16=\frac26', r'F_{X|Y}(3\mid7)=\frac36')),
      S(r'**Write the whole CDF.** Between $k$ and the next integer, exactly $k$ values count.',
        r'F_{X|Y}(x\mid7)=\begin{cases}0,&x<1\\ \frac k6,&k\le x<k+1,\ k=1,\ldots,5\\ 1,&x\ge6\end{cases}')],
     r'The PMF is $\tfrac16$ at $1,\ldots,6$ and zero elsewhere. The CDF jumps by $\tfrac16$ at each of those values.',
     cites=cite('L21', 2, 3))

# =====================================================================================================
D.H('Take a weighted average')
D.P(r'The **conditional expectation** $E[X\mid Y=y]$ is the average of $X$ among the outcomes with $Y=y$. Multiply each possible $x$ by its conditional probability, then add the products.', cites=cite('L22', 4))
D.EQ(r'E[X\mid Y=y]=\sum_x x\,p_{X|Y}(x\mid y)')
D.P(r'For a fixed condition such as $Y=7$, the answer is one number. If you leave the condition as $Y=y$, the answer can be a function of $y$.')

D.EX('Dice ★ (Lecture 22)',
     r'Two dice, $X$ = the first die, $Y$ = the sum. Find $E[X\mid Y=7]$.',
     [S(r'**Use the conditional PMF.** After keeping the rolls with sum $7$, each of the six first-die values has probability $\tfrac16$.'),
      S(r'**Weight and add.** The weights are all the same here, so this is the usual average of the six values.',
        r'E[X\mid Y=7]=\sum_{x=1}^{6}x\cdot\frac16=\frac{1+2+3+4+5+6}{6}=3.5')],
     r'$3.5$', cites=cite('L22', 5))

D.H('Conditional second moment and variance', level=2)
D.P(r'To get the conditional second moment, square each possible value before you weight it. Use the same conditional probabilities.')
D.EQ(r'E[X^2\mid Y=y]=\sum_x x^2\,p_{X|Y}(x\mid y)')
D.EQ(r'\operatorname{Var}(X\mid Y=y)=E[X^2\mid Y=y]-\big(E[X\mid Y=y]\big)^2')
D.P(r'The same idea works for any $E[g(X)\mid Y=y]$. Use the value $g(x)$ with each weight.')

D.EX('From a table: mean, square, variance',
     r'Use the conditional probabilities from the first worked table. Find $E[X\mid Y=1]$, $E[Y\mid X=1]$ and $\operatorname{Var}(Y\mid X=1)$.',
     [S(r'**Weight the values of $X$.** Given $Y=1$, $X=0$ has weight $\tfrac13$ and $X=1$ has weight $\tfrac23$.', r'E[X\mid Y=1]=0\cdot\frac13+1\cdot\frac23=\frac23'),
      S(r'$p_{Y|X}(\cdot\mid1)=\tfrac27,\tfrac37,\tfrac27$ at $y=0,1,2$. **Mean.**', r'E[Y\mid X=1]=0\cdot\frac27+1\cdot\frac37+2\cdot\frac27=\frac77=1'),
      S(r'**Square** inside the sum.', r'E[Y^2\mid X=1]=0+1\cdot\frac37+4\cdot\frac27=\frac{11}7'),
      S(r'**Subtract.**', r'\operatorname{Var}(Y\mid X=1)=\frac{11}7-1^2=\frac47')],
     r'$E[X\mid Y=1]=\tfrac23$, $E[Y\mid X=1]=1$, $\operatorname{Var}(Y\mid X=1)=\tfrac47$', cites=cite('T7', 1))

D.H('Use the conditional distribution to check independence')
D.P(r'For independence, the conditional probability must match the ordinary marginal at each $x$, for every $y$ with $p_Y(y)>0$. One mismatch shows dependence.', cites=cite('L21', 3))
D.EQ(r'p_{X|Y}(x\mid y)=p_X(x)\quad\text{for all }x\text{ and all }y\text{ with }p_Y(y)>0')
D.P(r'In the dice example, $Y=2$ forces both dice to show $1$. That gives $p_{X|Y}(1\mid2)=1$, while $p_X(1)=\tfrac16$. The first die and the sum are dependent.')
D.P(r'A changing conditional mean also shows dependence. A constant mean can come from different distributions. For instance, $X=1$ every time and an even split between $X=0$ and $X=2$ both have mean $1$.', cites=cite('L22', 4, 6))

D.H('Conditional expectation with a density')
D.P(r'If $X$ is continuous, use the conditional density as the weight and integrate over its range. Question 3 works through how to find the density.', cites=cite('L22', 4))
D.EQ(r'E[X\mid Y=y]=\int_{-\infty}^{\infty}x\,f_{X|Y}(x\mid y)\,dx')

D.EX('Continuous: $E[X\\mid Y=y]$ and independence ★ (Lecture 22)',
     r'$f_{X,Y}(x,y)=6xy(2-x-y)$ for $0<x<1,\ 0<y<1$. (a) Find $E[X\mid Y=y]$ for $0<y<1$. (b) Are $X$ and $Y$ independent?',
     [S(r'(a) **Marginal** $f_Y$: integrate $x$ out over $0$ to $1$.', r'f_Y(y)=\int_0^1 6xy(2-x-y)\,dx=6y\Big(\frac{2-y}{2}-\frac13\Big)=y(4-3y)'),
      S(r'**Divide** (formula sheet).', r'f_{X|Y}(x\mid y)=\frac{6xy(2-x-y)}{y(4-3y)}=\frac{6x(2-x-y)}{4-3y},\qquad 0<x<1'),
      S(r'**Mean.**', r'E[X\mid Y=y]=\int_0^1x\cdot\frac{6x(2-x-y)}{4-3y}\,dx=\frac{6}{4-3y}\Big(\frac{2-y}{3}-\frac14\Big)'),
      S(r'Tidy up.', r'E[X\mid Y=y]=\frac{5-4y}{2(4-3y)},\qquad 0<y<1'),
      S(r'(b) **Compare two allowed conditions.** The means differ, so $X$ and $Y$ are dependent.',
        (r'E[X\mid Y=\tfrac13]=\frac{11}{18}', r'E[X\mid Y=\tfrac23]=\frac7{12}'))],
     r'(a) $\dfrac{5-4y}{2(4-3y)}$ (b) not independent', cites=cite('L22', 6))

D.EX('Continuous: a flat triangle ★ (Lecture 21–22)',
     r'$f_{X,Y}(x,y)=2$ for $0<x<y<1$. Given $f_{X|Y}(x\mid y)=\tfrac1y$ on $0<x<y$ (Question 3, Example 1), find $E[X\mid Y=y]$.',
     [S(r'**Spot:** $\tfrac1y$ is flat on $(0,y)$: uniform. The mean of a uniform is the midpoint.'),
      S(r'**Mean.**', r'E[X\mid Y=y]=\int_0^y x\cdot\frac1y\,dx=\frac1y\cdot\frac{y^2}{2}=\frac y2')],
     r'$E[X\mid Y=y]=\tfrac y2$', cites=cite('L22', 1))

# =====================================================================================================
D.H('Practice Questions')
D.P('Start with the dice or the table. Write the conditional probabilities before you calculate the CDF or mean. Open each solution after you try it. ★ marks problems based on the lectures or tutorials.')

D.Q('Two dice, another sum · like Lecture 21–22',
    r'Two fair dice. $X$ = the first die, $Y$ = the sum. Find (a) $p_{X|Y}(x\mid4)$, (b) $F_{X|Y}(x\mid4)$, (c) $E[X\mid Y=4]$.',
    [S(r'**Column $Y=4$:** $(1,3),(2,2),(3,1)$, three equally likely outcomes.', r'P(Y=4)=\frac3{36}=\frac1{12}'),
     S(r'(a) **Divide.**', r'p_{X|Y}(x\mid4)=\frac{1/36}{3/36}=\frac13,\qquad x=1,2,3'),
     S(r'(b) **Accumulate.**', r'F_{X|Y}(x\mid4)=\begin{cases}0,&x<1\\ \frac13,&1\le x<2\\ \frac23,&2\le x<3\\ 1,&x\ge3\end{cases}'),
     S(r'(c) **Mean.**', r'E[X\mid Y=4]=\frac{1+2+3}{3}=2')],
    r'(a) $\tfrac13$ at $x=1,2,3$ (b) staircase $\tfrac13,\tfrac23,1$ (c) $2$', diff='introductory', cites=cite('L21', 2))

D.Q('Two dice, the other way round',
    r'Two fair dice, $X$ = the first die, $Y$ = the sum. Find $p_{Y|X}(y\mid2)$ and $E[Y\mid X=2]$. What is $E[Y\mid X=x]$ in general?',
    [S(r'**Spot:** given $X=2$, $Y=2+(\text{second die})$, and the second die is still fair.'),
     S(r'**Divide** (or just read it off).', r'p_{Y|X}(y\mid2)=\frac{1/36}{1/6}=\frac16,\qquad y=3,4,\dots,8'),
     S(r'**Mean.**', r'E[Y\mid X=2]=\frac{3+4+5+6+7+8}{6}=5.5'),
     S(r'In general: $x$ plus the second die’s mean.', r'E[Y\mid X=x]=x+3.5')],
    r'$\tfrac16$ for $y=3..8$; $5.5$; $x+3.5$', diff='introductory')

TB = {(1, 1): Fr(1, 10), (2, 1): Fr(1, 5), (3, 1): Fr(1, 10), (1, 2): Fr(3, 10), (2, 2): Fr(1, 10), (3, 2): Fr(1, 5)}
assert sum(TB.values()) == 1


def cond(T, y):
    tot = sum(v for (a, b), v in T.items() if b == y)
    return {a: v / tot for (a, b), v in T.items() if b == y}


c1, c2 = cond(TB, 1), cond(TB, 2)
m1 = sum(a * p for a, p in c1.items()); s1 = sum(a * a * p for a, p in c1.items())
m2 = sum(a * p for a, p in c2.items())
assert (m1, s1 - m1 ** 2, m2) == (2, Fr(1, 2), Fr(11, 6))
D.Q('A table: PMF, CDF, mean, variance given $Y$',
    r'''$X\in\{1,2,3\}$, $Y\in\{1,2\}$ with the joint PMF below. Find (a) $p_{X|Y}(x\mid1)$, $E[X\mid Y=1]$, $\operatorname{Var}(X\mid Y=1)$ (b) $p_{X|Y}(x\mid2)$, $F_{X|Y}(x\mid2)$, $E[X\mid Y=2]$ (c) are $X$, $Y$ independent?

| | $x=1$ | $x=2$ | $x=3$ |
|---|---|---|---|
| $y=1$ | $0.10$ | $0.20$ | $0.10$ |
| $y=2$ | $0.30$ | $0.10$ | $0.20$ |''',
    [S(r'(a) **Select** the row labeled $Y=1$. Its total is $0.4$. Divide each cell in that row by $0.4$.', r'p_{X|Y}(x\mid1)=\frac14,\ \frac12,\ \frac14\quad(x=1,2,3)'),
     S(r'**Mean**, **Square**, **Subtract.**', (r'E[X\mid Y=1]=\frac14+1+\frac34=2', r'E[X^2\mid Y=1]=\frac14+2+\frac94=4.5', r'\operatorname{Var}(X\mid Y=1)=4.5-2^2=0.5')),
     S(r'(b) $Y=2$: total $p_Y(2)=0.6$. **Divide.**', r'p_{X|Y}(x\mid2)=\frac{0.3}{0.6},\ \frac{0.1}{0.6},\ \frac{0.2}{0.6}=\frac12,\ \frac16,\ \frac13'),
     S(r'**Accumulate.**', r'F_{X|Y}(x\mid2)=\begin{cases}0,&x<1\\ \frac12,&1\le x<2\\ \frac23,&2\le x<3\\ 1,&x\ge3\end{cases}'),
     S(r'**Mean.**', r'E[X\mid Y=2]=\frac12+\frac26+\frac36=\frac{11}6'),
     S(r'(c) $E[X\mid Y=1]=2\ne\tfrac{11}6=E[X\mid Y=2]$: it changes with $y$ → **not** independent.')],
    r'(a) $\tfrac14,\tfrac12,\tfrac14$; $2$; $0.5$ (b) $\tfrac12,\tfrac16,\tfrac13$; staircase $\tfrac12,\tfrac23,1$; $\tfrac{11}6$ (c) not independent')

D.Q('Independent table ★ · Lecture 19 table',
    r'''Find $p_{X|Y}(x\mid1)$ and $E[X\mid Y=1]$. Compare with $p_X$ and $E[X]$.

| | $Y=0$ | $Y=1$ |
|---|---|---|
| $X=0$ | $0.12$ | $0.18$ |
| $X=1$ | $0.28$ | $0.42$ |''',
    [S(r'**Column** $Y=1$: total $0.60$. **Divide.**', r'p_{X|Y}(0\mid1)=\frac{0.18}{0.60}=0.3,\qquad p_{X|Y}(1\mid1)=\frac{0.42}{0.60}=0.7'),
     S(r'**Mean.**', r'E[X\mid Y=1]=0.7'),
     S(r'Plain marginal: $p_X=0.30,\,0.70$ and $E[X]=0.7$. Exactly the same, as it must be: these $X$, $Y$ are independent.')],
    r'$0.3,\,0.7$; $E[X\mid Y=1]=0.7=E[X]$', diff='introductory', cites=cite('L19', 2))

D.Q('A die and “even”',
    r'Roll a fair die. $X$ = the number, $Y=1$ if it is even and $Y=0$ if odd. Find $p_{X|Y}(x\mid1)$, $E[X\mid Y=1]$ and $E[X\mid Y=0]$. Independent?',
    [S(r'**Column** $Y=1$: the outcomes $2,4,6$, each $\tfrac16$, total $\tfrac12$. **Divide.**', r'p_{X|Y}(x\mid1)=\frac{1/6}{1/2}=\frac13,\qquad x=2,4,6'),
     S(r'**Mean.**', r'E[X\mid Y=1]=\frac{2+4+6}{3}=4'),
     S(r'Same for odd ($x=1,3,5$).', r'E[X\mid Y=0]=\frac{1+3+5}{3}=3'),
     S(r'$4\ne3$ → **not** independent (of course: $Y$ is built from $X$).')],
    r'$\tfrac13$ on $\{2,4,6\}$; $4$; $3$; not independent', diff='introductory')

TC = {(0, 0): Fr(1, 10), (0, 1): Fr(1, 5), (0, 2): Fr(1, 10), (1, 0): Fr(1, 5), (1, 1): Fr(1, 10), (1, 2): Fr(3, 10)}
assert sum(TC.values()) == 1
D.Q('Find $c$, then condition',
    r'''Find $c$, then $p_{Y|X}(y\mid1)$, $E[Y\mid X=1]$ and $E[Y\mid X=0]$.

| | $y=0$ | $y=1$ | $y=2$ |
|---|---|---|---|
| $x=0$ | $c$ | $2c$ | $c$ |
| $x=1$ | $2c$ | $c$ | $3c$ |''',
    [S(r'**Find $c$:** $10c=1$, so $c=0.1$.'),
     S(r'Given $X=1$: the row $0.2,\,0.1,\,0.3$, total $p_X(1)=0.6$. **Divide.**', r'p_{Y|X}(y\mid1)=\frac13,\ \frac16,\ \frac12\quad(y=0,1,2)'),
     S(r'**Mean.**', r'E[Y\mid X=1]=0+\frac16+2\cdot\frac12=\frac76'),
     S(r'Given $X=0$: the row $0.1,\,0.2,\,0.1$, total $0.4$ → $\tfrac14,\tfrac12,\tfrac14$.', r'E[Y\mid X=0]=\frac12+2\cdot\frac14=1')],
    r'$c=0.1$; $\tfrac13,\tfrac16,\tfrac12$; $\tfrac76$; $1$')

D.Q('Three coins',
    r'Toss a fair coin 3 times. $X=1$ if the first toss is heads (else $0$); $Y$ = the total number of heads. Find $p_{X|Y}(x\mid2)$, $E[X\mid Y=2]$, $p_{Y|X}(y\mid1)$ and $E[Y\mid X=1]$.',
    [S(r'**Column** $Y=2$: $HHT,\ HTH,\ THH$, equally likely. The first toss is $H$ in two of them.', r'p_{X|Y}(1\mid2)=\frac23,\qquad p_{X|Y}(0\mid2)=\frac13'),
     S(r'**Mean.**', r'E[X\mid Y=2]=\frac23'),
     S(r'Given $X=1$: $Y=1+$ (heads in the last two tosses): $HTT$; $HHT,HTH$; $HHH$.', r'p_{Y|X}(y\mid1)=\frac14,\ \frac12,\ \frac14\quad(y=1,2,3)'),
     S(r'**Mean.**', r'E[Y\mid X=1]=\frac14+1+\frac34=2')],
    r'$\tfrac13,\tfrac23$; $\tfrac23$; $\tfrac14,\tfrac12,\tfrac14$; $2$')

D.H('Practice with continuous conditional expectation', level=2)

D.Q('Continuous: on the square ★ · Tutorial 7 Q5 joint PDF',
    r'$f_{X,Y}(x,y)=x+y$ for $0<x<1,\ 0<y<1$. Find $E[X\mid Y=y]$. Use it to show $X$, $Y$ are not independent.',
    [S(r'**Marginal.**', r'f_Y(y)=\int_0^1(x+y)\,dx=y+\frac12'),
     S(r'**Divide.**', r'f_{X|Y}(x\mid y)=\frac{x+y}{y+\frac12},\qquad 0<x<1'),
     S(r'**Mean.**', r'E[X\mid Y=y]=\frac{\int_0^1x(x+y)\,dx}{y+\frac12}=\frac{\frac13+\frac y2}{y+\frac12}=\frac{2+3y}{3(1+2y)}'),
     S(r'At $y=\tfrac14$ the mean is $\tfrac{11}{18}$. At $y=\tfrac12$ it is $\tfrac7{12}$. The change shows dependence.')],
    r'$E[X\mid Y=y]=\dfrac{2+3y}{3(1+2y)}$; not independent', cites=cite('T7', 2))

D.Q('Continuous: a triangle ★ · Tutorial 7 Q6 joint PDF',
    r'$f_{X,Y}(x,y)=24xy$ for $x,y\ge0,\ x+y\le1$. Find $E[X\mid Y=y]$ for $0<y<1$.',
    [S(r'**Marginal:** slice at $y$, $x$ from $0$ to $1-y$.', r'f_Y(y)=\int_0^{1-y}24xy\,dx=12y(1-y)^2'),
     S(r'**Divide.**', r'f_{X|Y}(x\mid y)=\frac{24xy}{12y(1-y)^2}=\frac{2x}{(1-y)^2},\qquad 0\le x\le1-y'),
     S(r'**Mean.**', r'E[X\mid Y=y]=\int_0^{1-y}\frac{2x^2}{(1-y)^2}\,dx=\frac{2(1-y)^3}{3(1-y)^2}=\frac{2(1-y)}{3}')],
    r'$E[X\mid Y=y]=\tfrac23(1-y)$', cites=cite('T7', 2))

D.Q('Continuous: mean and variance given $Y$',
    r'$f_{X,Y}(x,y)=e^{-y}$ for $0<x<y$. Find $f_{X|Y}(x\mid y)$, $E[X\mid Y=y]$ and $\operatorname{Var}(X\mid Y=y)$.',
    [S(r'**Marginal:** slice at $y$, $x$ from $0$ to $y$.', r'f_Y(y)=\int_0^y e^{-y}\,dx=y\,e^{-y},\qquad y>0'),
     S(r'**Divide:** flat on $(0,y)$, so uniform.', r'f_{X|Y}(x\mid y)=\frac{e^{-y}}{y\,e^{-y}}=\frac1y,\qquad 0<x<y'),
     S(r'**Mean** and **Square.**', r'E[X\mid Y=y]=\frac y2,\qquad E[X^2\mid Y=y]=\int_0^y\frac{x^2}{y}\,dx=\frac{y^2}3'),
     S(r'**Subtract.**', r'\operatorname{Var}(X\mid Y=y)=\frac{y^2}3-\frac{y^2}4=\frac{y^2}{12}')],
    r'$\tfrac1y$ on $(0,y)$; $\tfrac y2$; $\tfrac{y^2}{12}$')

D.H('Test 3 formula sheet')
D.SHEET3()


def verify():
    import sympy as sp
    x, y = sp.symbols('x y', positive=True)
    I = sp.integrate
    R = sp.Rational
    # dice by enumeration
    outs = [(a, b) for a in range(1, 7) for b in range(1, 7)]
    for s, xs in ((7, range(1, 7)), (4, range(1, 4))):
        hit = [a for a, b in outs if a + b == s]
        assert sorted(hit) == list(xs) and R(sum(hit), len(hit)) == R(sum(xs), len(xs))
    assert R(sum(range(3, 9)), 6) == R(11, 2)
    assert R(15, 45) == R(1, 3) and R(3, 7) + 2 * R(2, 7) == 1 and R(3, 7) + 4 * R(2, 7) - 1 == R(4, 7)
    # Lec 22 continuous
    f = 6 * x * y * (2 - x - y)
    fy = sp.factor(I(f, (x, 0, 1)))
    assert sp.simplify(fy - y * (4 - 3 * y)) == 0
    e = sp.simplify(I(x * f / fy, (x, 0, 1)))
    assert sp.simplify(e - (5 - 4 * y) / (2 * (4 - 3 * y))) == 0 and e.subs(y, 0) == R(5, 8) and sp.limit(e, y, 1) == R(1, 2)
    assert sp.simplify(I(x / y, (x, 0, y)) - y / 2) == 0
    # coins
    seq = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
    two = [s for s in seq if sum(s) == 2]
    assert R(sum(s[0] for s in two), len(two)) == R(2, 3)
    first = [sum(s) for s in seq if s[0] == 1]
    assert R(sum(first), len(first)) == 2
    # continuous practice
    ex = sp.simplify(I(x * (x + y), (x, 0, 1)) / (y + R(1, 2)))
    assert sp.simplify(ex - (2 + 3 * y) / (3 * (1 + 2 * y))) == 0 and ex.subs(y, 1) == R(5, 9)
    fy2 = I(24 * x * y, (x, 0, 1 - y))
    assert sp.simplify(I(x * 24 * x * y / fy2, (x, 0, 1 - y)) - R(2, 3) * (1 - y)) == 0
    assert sp.simplify(I(x ** 2 / y, (x, 0, y)) - (y / 2) ** 2 - y ** 2 / 12) == 0
    assert TC[(1, 0)] / Fr(3, 5) == Fr(1, 3) and sum(b * v / Fr(3, 5) for (a, b), v in TC.items() if a == 1) == Fr(7, 6)
    assert sum(b * v / Fr(2, 5) for (a, b), v in TC.items() if a == 0) == 1
    print('t3q2 verify ok')


if __name__ == '__main__':
    verify()
    D.save()
