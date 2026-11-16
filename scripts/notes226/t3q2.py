r"""Test 3 - Question 2: conditional distributions for discrete random variables and conditional expectation
(Lectures 21-23, Tutorial 7).

Rewritten 2026-11-15 (same shape as t3q1): Part A conditional PMF, Part B conditional CDF, Part C conditional
expectation (incl. E[g(X)|Y], conditional variance, total expectation from Lecture 23). Discrete only: the
continuous material lives in t3q3.py. Practice = 6 test-style questions (10 marks each).
"""
from fractions import Fraction as Fr

from lib226 import Doc, S, cite

D = Doc('t3q2', 'Test 3 - Question 2', ['conditional_pmf', 'conditional_cdf', 'conditional_expectation'])

# =====================================================================================================
D.P(r'**Test 3, Question 2 · Discrete conditional distributions and conditional expectation** (10 marks)')
D.P(r'"Given $Y=y$" means: you already know $Y$. Keep only the outcomes with that $y$, and rescale them so they add to $1$. That new PMF gives probabilities, a CDF, and an average.')
D.CO('tip', r'''**Formula sheet lines for this question:**

$$
p_{X|Y}(x\mid y)=\frac{p_{X,Y}(x,y)}{p_Y(y)}
$$

$$
F_X(x)=\sum_{t\le x}p_X(t)\qquad\text{(use it with }p_{X|Y}\text{ for the conditional CDF)}
$$

$$
E[X\mid Y=y]=\sum_x x\,p_{X|Y}(x\mid y)
$$

Expect: **conditional PMF → conditional CDF or probability → $E[X\mid Y=y]$ → independent?**''')

# =====================================================================================================
# PART A
# =====================================================================================================
D.H('Part A · Conditional PMF')

# ---- A1 ----------------------------------------------------------------------------------------------
D.H('A1 · From a table', level=2)
D.EQ(r'p_{X|Y}(x\mid y)=\frac{p_{X,Y}(x,y)}{p_Y(y)}', cites=cite('L21', 1))
D.L([r'**Select** the row or column of the given value.',
     r'**Total** it. That total is $p_Y(y)$.',
     r'**Divide** each cell in it by the total. The new numbers add to $1$.'], ordered=True)
D.EX('Given a column, given a row ★ (Lecture 17 / Tutorial 7 table)',
     r'''Find $p_{X|Y}(x\mid1)$ and $p_{Y|X}(y\mid1)$.

| | $y=0$ | $y=1$ | $y=2$ |
|---|---|---|---|
| $x=0$ | $0.10$ | $0.15$ | $0.05$ |
| $x=1$ | $0.20$ | $0.30$ | $0.20$ |''',
     [S(r'**Given $Y=1$:** column $y=1$ is $0.15,\ 0.30$. Total $0.45$.', r'p_{X|Y}(0\mid1)=\frac{0.15}{0.45}=\frac13,\qquad p_{X|Y}(1\mid1)=\frac{0.30}{0.45}=\frac23'),
      S(r'**Given $X=1$:** row $x=1$ is $0.20,\ 0.30,\ 0.20$. Total $0.70$.', r'p_{Y|X}(y\mid1)=\frac27,\ \frac37,\ \frac27\quad(y=0,1,2)')],
     r'$\tfrac13,\ \tfrac23$; $\tfrac27,\ \tfrac37,\ \tfrac27$', cites=cite('T7', 1))
D.TRY('Your turn',
      r'''Same table. Find $p_{X|Y}(x\mid2)$ and $p_{Y|X}(y\mid0)$.''',
      [S(r'**Column $y=2$:** $0.05,\ 0.20$, total $0.25$.', r'p_{X|Y}(x\mid2)=0.2,\ 0.8\quad(x=0,1)'),
       S(r'**Row $x=0$:** $0.10,\ 0.15,\ 0.05$, total $0.30$.', r'p_{Y|X}(y\mid0)=\frac13,\ \frac12,\ \frac16\quad(y=0,1,2)')],
      r'$0.2,\,0.8$; $\tfrac13,\,\tfrac12,\,\tfrac16$', diff='introductory')

# ---- A2 ----------------------------------------------------------------------------------------------
D.H('A2 · From an experiment', level=2)
D.P(r'No table? List the equally likely outcomes that fit the condition, then count.', cites=cite('L21', 2))
D.EQ(r'p_{X|Y}(x\mid y)=\frac{\#\text{ outcomes with }X=x\text{ and }Y=y}{\#\text{ outcomes with }Y=y}')
D.EX('Two dice ★ (Lecture 21)',
     r'Roll two fair dice. $X$ = first die, $Y$ = sum. Find $p_{X|Y}(x\mid7)$.',
     [S(r'**Outcomes with sum $7$:** $(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)$. That is $6$.'),
      S(r'**Each $x$ appears once.**', r'p_{X|Y}(x\mid7)=\frac16,\qquad x=1,2,\ldots,6\quad(0\text{ otherwise})')],
     r'$\tfrac16$ for $x=1,\ldots,6$', cites=cite('L21', 2, 3))
D.TRY('Three coins',
      r'Toss a fair coin 3 times. $X$ = number of heads, $Y=1$ if the first toss is heads, else $0$. Find $p_{X|Y}(x\mid1)$.',
      [S(r'**Outcomes with first toss $H$:** $HHH,\ HHT,\ HTH,\ HTT$ (4 of them).'),
       S(r'**Count heads:** $3,\ 2,\ 2,\ 1$.', r'p_{X|Y}(x\mid1)=\frac14,\ \frac24,\ \frac14\quad(x=1,2,3)')],
      r'$\tfrac14,\ \tfrac12,\ \tfrac14$ at $x=1,2,3$', diff='introductory')

# ---- A3 ----------------------------------------------------------------------------------------------
D.H('A3 · Independence from the conditional PMF', level=2)
D.P(r'Independent means knowing $Y$ changes nothing:', cites=cite('L21', 1))
D.EQ(r'p_{X|Y}(x\mid y)=p_X(x)\quad\text{for every }x\text{ and every possible }y')
D.P(r'One mismatch → dependent.')
D.EX('The dice are dependent ★ (Lecture 21)',
     r'$X$ = first die, $Y$ = sum. Are $X$ and $Y$ independent?',
     [S(r'**Pick an extreme $y$.** $Y=2$ forces $(1,1)$.', r'p_{X|Y}(1\mid2)=1'),
      S(r'**Compare** with no information.', r'p_X(1)=\frac16\ne1')],
     r'Not independent', cites=cite('L21', 3))
D.TRY('Table check',
      r'In the A1 table, compare $p_{X|Y}(0\mid1)$ with $p_X(0)$.',
      [S(r'From A1, $p_{X|Y}(0\mid1)=\tfrac13$. The row total is $p_X(0)=0.30$.', r'\frac13\ne0.30\quad\Rightarrow\quad\text{dependent}')],
      r'Dependent', diff='introductory')

# =====================================================================================================
# PART B
# =====================================================================================================
D.H('Part B · Conditional CDF')
D.P(r'Add the conditional PMF up to and including $x$. It is a staircase.', cites=cite('L21', 1))
D.EQ(r'F_{X|Y}(x\mid y)=P(X\le x\mid Y=y)=\sum_{t\le x}p_{X|Y}(t\mid y)')
D.L([r'Jump at each possible value, flat in between. $0$ before the first value, $1$ after the last.',
     r'Use $\le$ at each step: write "$1\le x<2$", not "$1<x\le2$".',
     r'Discrete only: $P(X<2\mid\cdot)$ is **not** $F(2\mid\cdot)$. It is $F(1\mid\cdot)$ when the values are integers.'])
D.EX('Dice ★ (Lecture 21)',
     r'$X$ = first die, $Y$ = sum. Find $F_{X|Y}(x\mid7)$ and $P(X\le3\mid Y=7)$.',
     [S(r'**From A2:** $\tfrac16$ at each of $1,\ldots,6$. **Add up.**',
        r'F_{X|Y}(x\mid7)=\begin{cases}0,&x<1\\ \frac16,&1\le x<2\\ \frac26,&2\le x<3\\ \frac36,&3\le x<4\\ \frac46,&4\le x<5\\ \frac56,&5\le x<6\\ 1,&x\ge6\end{cases}'),
      S(r'**Read off.**', r'P(X\le3\mid Y=7)=F_{X|Y}(3\mid7)=\frac36=\frac12')],
     r'Staircase in steps of $\tfrac16$; $\tfrac12$', cites=cite('L21', 3))
D.TRY('CDF from a table',
      r'Use $p_{Y|X}(y\mid1)=\tfrac27,\tfrac37,\tfrac27$ at $y=0,1,2$ (A1). Find $F_{Y|X}(y\mid1)$ and $P(Y<2\mid X=1)$.',
      [S(r'**Add up.**', r'F_{Y|X}(y\mid1)=\begin{cases}0,&y<0\\ \frac27,&0\le y<1\\ \frac57,&1\le y<2\\ 1,&y\ge2\end{cases}'),
       S(r'**$Y<2$** means $Y\le1$.', r'P(Y<2\mid X=1)=F_{Y|X}(1\mid1)=\frac57')],
      r'Staircase $\tfrac27,\tfrac57,1$; $\tfrac57$', diff='introductory')

# =====================================================================================================
# PART C
# =====================================================================================================
D.H('Part C · Conditional expectation')

# ---- C1 ----------------------------------------------------------------------------------------------
D.H('C1 · $E[X\\mid Y=y]$', level=2)
D.P(r'The average of $X$ using the **conditional** probabilities as weights.', cites=cite('L22', 4))
D.EQ(r'E[X\mid Y=y]=\sum_x x\,p_{X|Y}(x\mid y)')
D.L([r'For one value ($Y=7$) it is a number. With $y$ left as a letter it can be a formula in $y$.',
     r'Independent → $E[X\mid Y=y]=E[X]$ for every $y$. So if it changes with $y$, they are **dependent**.'])
D.EX('Dice and a table ★ (Lecture 22)',
     r'(a) $X$ = first die, $Y$ = sum. Find $E[X\mid Y=7]$. (b) In the A1 table, find $E[Y\mid X=1]$.',
     [S(r'(a) **Weights** $\tfrac16$ each (A2).', r'E[X\mid Y=7]=\frac{1+2+3+4+5+6}{6}=3.5'),
      S(r'(b) **Weights** $\tfrac27,\tfrac37,\tfrac27$ at $y=0,1,2$.', r'E[Y\mid X=1]=0\cdot\frac27+1\cdot\frac37+2\cdot\frac27=1')],
     r'(a) $3.5$ (b) $1$', cites=cite('L22', 5))
D.TRY('Does the mean change?',
      r'A1 table. Find $E[Y\mid X=0]$ and compare with $E[Y\mid X=1]=1$.',
      [S(r'**Weights** $\tfrac13,\tfrac12,\tfrac16$ (A1 Try it).', r'E[Y\mid X=0]=0+\frac12+2\cdot\frac16=\frac56'),
       S(r'$\tfrac56\ne1$: the mean changes with $x$ → dependent.')],
      r'$\tfrac56$; dependent', diff='introductory')

# ---- C2 ----------------------------------------------------------------------------------------------
D.H('C2 · $E[g(X)\\mid Y=y]$ and conditional variance', level=2)
D.P(r'Same weights, but put $g(x)$ in front instead of $x$.', cites=cite('L22', 4))
D.EQ(r'E[g(X)\mid Y=y]=\sum_x g(x)\,p_{X|Y}(x\mid y)')
D.EQ(r'\operatorname{Var}(X\mid Y=y)=E[X^2\mid Y=y]-\big(E[X\mid Y=y]\big)^2')
D.EX('Conditional variance from a table',
     r'A1 table. Find $\operatorname{Var}(Y\mid X=1)$.',
     [S(r'**Mean** (C1).', r'E[Y\mid X=1]=1'),
      S(r'**Square** each value, same weights.', r'E[Y^2\mid X=1]=0\cdot\frac27+1\cdot\frac37+4\cdot\frac27=\frac{11}7'),
      S(r'**Subtract.**', r'\operatorname{Var}(Y\mid X=1)=\frac{11}7-1^2=\frac47')],
     r'$\tfrac47$', cites=cite('T7', 1))
D.TRY('Dice, a function of $X$',
      r'$X$ = first die, $Y$ = sum. Find $E[X^2\mid Y=7]$ and $E[2^X\mid Y=7]$.',
      [S(r'**Weights** $\tfrac16$.', r'E[X^2\mid Y=7]=\frac{1+4+9+16+25+36}{6}=\frac{91}6'),
       S(r'**Put $2^x$ in front.**', r'E[2^X\mid Y=7]=\frac{2+4+8+16+32+64}{6}=\frac{126}6=21')],
      r'$\tfrac{91}6$; $21$', diff='introductory')

# ---- C3 ----------------------------------------------------------------------------------------------
D.H('C3 · Total expectation (Lecture 23)', level=2)
D.P(r'$E[X\mid Y]$ (no "$=y$") is a **random variable**: write $g(y)=E[X\mid Y=y]$, then $E[X\mid Y]=g(Y)$. It is your best guess of $X$ once you see $Y$.', cites=cite('L23', 4))
D.P(r'Its average is the plain average of $X$. In words: weight each case’s average by how likely the case is.')
D.EQ(r'E[X]=E\big[E[X\mid Y]\big]=\sum_y E[X\mid Y=y]\;p_Y(y)', cites=cite('L23', 5))
D.EX('Router modes ★ (Lecture 23)',
     r'A router is in normal mode or high-traffic mode, each with probability $\tfrac12$. Packets per second $X$ are Poisson with mean $2$ in normal mode and $5$ in high mode. Find $E[X]$.',
     [S(r'**Name the cases:** $Y=1$ normal, $Y=0$ high. A Poisson mean is its $\lambda$.', (r'E[X\mid Y=1]=2,\quad E[X\mid Y=0]=5', r'P(Y=1)=P(Y=0)=\frac12')),
      S(r'**Weight and add.**', r'E[X]=2\cdot\frac12+5\cdot\frac12=3.5')],
     r'$3.5$', cites=cite('L23', 6))
D.TRY('Check it on the table',
      r'A1 table. Use $E[X\mid Y=y]$ for $y=0,1,2$ to get $E[X]$. Check against $p_X$.',
      [S(r'**Case averages** ($X$ is $0$ or $1$, so it is the share of the column in row $x=1$).', (r'E[X\mid Y=0]=\frac{0.20}{0.30}=\frac23,\quad E[X\mid Y=1]=\frac{0.30}{0.45}=\frac23', r'E[X\mid Y=2]=\frac{0.20}{0.25}=0.8')),
       S(r'**Weight** by $p_Y=0.30,\ 0.45,\ 0.25$.', r'E[X]=\frac23(0.30)+\frac23(0.45)+0.8(0.25)=0.2+0.3+0.2=0.7'),
       S(r'**Check:** $E[X]=0\cdot0.30+1\cdot0.70=0.7\ \checkmark$')],
      r'$0.7$')

# =====================================================================================================
D.H('Practice Questions')
D.P('Test 2 difficulty, 10 marks each. Formula sheet only. ★ = from the lectures/tutorials.')

D.Q('[10 marks] Two dice, sum 4 ★ (like Lecture 21–22)',
    r'Two fair dice. $X$ = first die, $Y$ = sum. (a) Find $p_{X|Y}(x\mid4)$. (3 marks) (b) Find $F_{X|Y}(x\mid4)$. (3 marks) (c) Find $E[X\mid Y=4]$. (2 marks) (d) Use (a) to show $X$ and $Y$ are not independent. (2 marks)',
    [S(r'(a) **Sum 4:** $(1,3),(2,2),(3,1)$. Each $x$ once.', r'p_{X|Y}(x\mid4)=\frac13,\qquad x=1,2,3'),
     S(r'(b) **Add up.**', r'F_{X|Y}(x\mid4)=\begin{cases}0,&x<1\\ \frac13,&1\le x<2\\ \frac23,&2\le x<3\\ 1,&x\ge3\end{cases}'),
     S(r'(c) **Mean.**', r'E[X\mid Y=4]=\frac{1+2+3}{3}=2'),
     S(r'(d) **Compare:** $p_{X|Y}(4\mid4)=0$ but $p_X(4)=\tfrac16$. Not equal → dependent.')],
    r'(a) $\tfrac13$ at $1,2,3$ (b) $0,\tfrac13,\tfrac23,1$ (c) $2$ (d) $0\ne\tfrac16$', cites=cite('L21', 2))

TB = {(1, 1): Fr(1, 10), (2, 1): Fr(1, 5), (3, 1): Fr(1, 10), (1, 2): Fr(3, 10), (2, 2): Fr(1, 10), (3, 2): Fr(1, 5)}
D.Q('[10 marks] A table, given $Y$',
    r'''(a) Find $p_{X|Y}(x\mid1)$, $E[X\mid Y=1]$ and $\operatorname{Var}(X\mid Y=1)$. (4 marks) (b) Find $p_{X|Y}(x\mid2)$ and $P(X\ge2\mid Y=2)$. (3 marks) (c) Find $E[X\mid Y=2]$. Are $X$ and $Y$ independent? (3 marks)

| | $x=1$ | $x=2$ | $x=3$ |
|---|---|---|---|
| $y=1$ | $0.10$ | $0.20$ | $0.10$ |
| $y=2$ | $0.30$ | $0.10$ | $0.20$ |''',
    [S(r'(a) **Row $y=1$**, total $0.4$. **Divide.**', r'p_{X|Y}(x\mid1)=\frac14,\ \frac12,\ \frac14\quad(x=1,2,3)'),
     S(r'**Mean, square, subtract.**', (r'E[X\mid Y=1]=\frac14+1+\frac34=2', r'E[X^2\mid Y=1]=\frac14+2+\frac94=4.5', r'\operatorname{Var}(X\mid Y=1)=4.5-4=0.5')),
     S(r'(b) **Row $y=2$**, total $0.6$.', r'p_{X|Y}(x\mid2)=\frac12,\ \frac16,\ \frac13'),
     S(r'**Add** $x=2,3$.', r'P(X\ge2\mid Y=2)=\frac16+\frac13=\frac12'),
     S(r'(c) **Mean.**', r'E[X\mid Y=2]=\frac12+\frac26+\frac36=\frac{11}6'),
     S(r'$2\ne\tfrac{11}6$: the mean changes with $y$ → **dependent**.')],
    r'(a) $\tfrac14,\tfrac12,\tfrac14$; $2$; $0.5$ (b) $\tfrac12,\tfrac16,\tfrac13$; $\tfrac12$ (c) $\tfrac{11}6$; dependent')

TC = {(0, 0): Fr(1, 10), (0, 1): Fr(1, 5), (0, 2): Fr(1, 10), (1, 0): Fr(1, 5), (1, 1): Fr(1, 10), (1, 2): Fr(3, 10)}
D.Q('[10 marks] Find $c$, condition, total expectation',
    r'''(a) Find $c$. (1 mark) (b) Find $p_{Y|X}(y\mid1)$ and $F_{Y|X}(y\mid1)$. (4 marks) (c) Find $E[Y\mid X=0]$ and $E[Y\mid X=1]$. (3 marks) (d) Use (c) to find $E[Y]$. (2 marks)

| | $y=0$ | $y=1$ | $y=2$ |
|---|---|---|---|
| $x=0$ | $c$ | $2c$ | $c$ |
| $x=1$ | $2c$ | $c$ | $3c$ |''',
    [S(r'(a) $10c=1$.', r'c=0.1'),
     S(r'(b) **Row $x=1$:** $0.2,\ 0.1,\ 0.3$, total $0.6$.', r'p_{Y|X}(y\mid1)=\frac13,\ \frac16,\ \frac12\quad(y=0,1,2)'),
     S(r'**Add up.**', r'F_{Y|X}(y\mid1)=\begin{cases}0,&y<0\\ \frac13,&0\le y<1\\ \frac12,&1\le y<2\\ 1,&y\ge2\end{cases}'),
     S(r'(c) **Means.** Row $x=0$ gives $\tfrac14,\tfrac12,\tfrac14$.', (r'E[Y\mid X=0]=\frac12+2\cdot\frac14=1', r'E[Y\mid X=1]=\frac16+2\cdot\frac12=\frac76')),
     S(r'(d) **Weight** by $p_X=0.4,\ 0.6$.', r'E[Y]=1(0.4)+\frac76(0.6)=0.4+0.7=1.1')],
    r'(a) $0.1$ (b) $\tfrac13,\tfrac16,\tfrac12$; staircase $\tfrac13,\tfrac12,1$ (c) $1$; $\tfrac76$ (d) $1.1$')

D.Q('[10 marks] Three coins',
    r'A fair coin is tossed 3 times. $X=1$ if the first toss is heads (else $0$); $Y$ = total number of heads. (a) Find $p_{X|Y}(x\mid2)$ and $E[X\mid Y=2]$. (4 marks) (b) Find $p_{Y|X}(y\mid1)$ and $E[Y\mid X=1]$. (4 marks) (c) Are $X$ and $Y$ independent? (2 marks)',
    [S(r'(a) **$Y=2$:** $HHT,\ HTH,\ THH$. First toss $H$ in 2 of 3.', (r'p_{X|Y}(0\mid2)=\frac13,\quad p_{X|Y}(1\mid2)=\frac23', r'E[X\mid Y=2]=\frac23')),
     S(r'(b) **$X=1$:** $HTT,\ HTH,\ HHT,\ HHH$ have $Y=1,2,2,3$.', (r'p_{Y|X}(y\mid1)=\frac14,\ \frac12,\ \frac14\quad(y=1,2,3)', r'E[Y\mid X=1]=\frac14+1+\frac34=2')),
     S(r'(c) $p_{X|Y}(1\mid2)=\tfrac23\ne\tfrac12=p_X(1)$ → **dependent**.')],
    r'(a) $\tfrac13,\tfrac23$; $\tfrac23$ (b) $\tfrac14,\tfrac12,\tfrac14$; $2$ (c) dependent')

D.Q('[10 marks] A die and "even"',
    r'Roll a fair die. $X$ = the number; $Y=1$ if it is even, $Y=0$ if odd. (a) Find $p_{X|Y}(x\mid1)$. (2 marks) (b) Find $E[X\mid Y=1]$ and $\operatorname{Var}(X\mid Y=1)$. (4 marks) (c) Find $E[X\mid Y=0]$, then $E[X]$ by total expectation. (4 marks)',
    [S(r'(a) **Even:** $2,4,6$.', r'p_{X|Y}(x\mid1)=\frac13,\qquad x=2,4,6'),
     S(r'(b) **Mean, square, subtract.**', (r'E[X\mid Y=1]=\frac{2+4+6}{3}=4', r'E[X^2\mid Y=1]=\frac{4+16+36}{3}=\frac{56}3', r'\operatorname{Var}(X\mid Y=1)=\frac{56}3-16=\frac83')),
     S(r'(c) **Odd:** $1,3,5$.', r'E[X\mid Y=0]=3'),
     S(r'**Weight** by $p_Y=\tfrac12,\tfrac12$.', r'E[X]=4\cdot\frac12+3\cdot\frac12=3.5\ \checkmark')],
    r'(a) $\tfrac13$ on $2,4,6$ (b) $4$; $\tfrac83$ (c) $3$; $3.5$')

D.Q('[10 marks] Errors on two channels',
    r'A message is sent on channel $Y=1$ with probability $0.3$ or channel $Y=2$ with probability $0.7$. The number of errors $X$ has: given $Y=1$, $P(X=0,1,2)=0.5,\ 0.3,\ 0.2$; given $Y=2$, $P(X=0,1)=0.8,\ 0.2$. (a) Find $E[X\mid Y=1]$ and $E[X\mid Y=2]$. (3 marks) (b) Find $E[X]$. (2 marks) (c) Build the joint PMF table. (3 marks) (d) Find $p_{Y|X}(1\mid1)$. (2 marks)',
    [S(r'(a) **Means.**', (r'E[X\mid Y=1]=0.3+2(0.2)=0.7', r'E[X\mid Y=2]=0.2')),
     S(r'(b) **Total expectation.**', r'E[X]=0.7(0.3)+0.2(0.7)=0.21+0.14=0.35'),
     S(r'(c) **Joint = conditional × $p_Y$.** Rows $y=1,2$; columns $x=0,1,2$.', (r'y=1:\ \ 0.15,\ 0.09,\ 0.06', r'y=2:\ \ 0.56,\ 0.14,\ 0')),
     S(r'(d) **Column $x=1$:** $0.09,\ 0.14$, total $0.23$.', r'p_{Y|X}(1\mid1)=\frac{0.09}{0.23}=\frac9{23}\approx0.391')],
    r'(a) $0.7$; $0.2$ (b) $0.35$ (c) table above (d) $\tfrac9{23}$')

D.H('Test 3 formula sheet')
D.SHEET3()


def verify():
    R = Fr
    t = {(0, 0): R(1, 10), (0, 1): R(15, 100), (0, 2): R(5, 100), (1, 0): R(2, 10), (1, 1): R(3, 10), (1, 2): R(2, 10)}
    px = lambda a: sum(v for (i, j), v in t.items() if i == a)
    py = lambda b: sum(v for (i, j), v in t.items() if j == b)
    assert t[(0, 1)] / py(1) == R(1, 3) and t[(1, 1)] / py(1) == R(2, 3)
    assert [t[(1, j)] / px(1) for j in range(3)] == [R(2, 7), R(3, 7), R(2, 7)]
    assert [t[(i, 2)] / py(2) for i in range(2)] == [R(1, 5), R(4, 5)]
    assert [t[(0, j)] / px(0) for j in range(3)] == [R(1, 3), R(1, 2), R(1, 6)]
    assert sum(j * t[(1, j)] / px(1) for j in range(3)) == 1 and sum(j * j * t[(1, j)] / px(1) for j in range(3)) == R(11, 7)
    assert sum(j * t[(0, j)] / px(0) for j in range(3)) == R(5, 6)
    assert sum(sum(i * t[(i, j)] for i in range(2)) / py(j) * py(j) for j in range(3)) == R(7, 10)
    assert t[(1, 0)] / py(0) == R(2, 3) and t[(1, 2)] / py(2) == R(4, 5)
    dice = [(a, b) for a in range(1, 7) for b in range(1, 7)]
    s7 = [a for a, b in dice if a + b == 7]
    assert R(sum(s7), 6) == R(7, 2) and R(sum(a * a for a in s7), 6) == R(91, 6) and R(sum(2 ** a for a in s7), 6) == 21
    assert sorted(a for a, b in dice if a + b == 4) == [1, 2, 3]
    coins = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
    assert [sum(s) for s in coins if s[0] == 1].count(2) == 2
    assert R(sum(s[0] for s in coins if sum(s) == 2), 3) == R(2, 3) and R(sum(sum(s) for s in coins if s[0] == 1), 4) == 2
    # practice tables
    assert sum(TB.values()) == 1 and sum(TC.values()) == 1
    c1 = {a: v / R(2, 5) for (a, b), v in TB.items() if b == 1}; c2 = {a: v / R(3, 5) for (a, b), v in TB.items() if b == 2}
    assert c1 == {1: R(1, 4), 2: R(1, 2), 3: R(1, 4)} and c2 == {1: R(1, 2), 2: R(1, 6), 3: R(1, 3)}
    m1 = sum(a * p for a, p in c1.items()); assert m1 == 2 and sum(a * a * p for a, p in c1.items()) - 4 == R(1, 2)
    assert sum(a * p for a, p in c2.items()) == R(11, 6) and c2[2] + c2[3] == R(1, 2)
    r1 = {b: v / R(3, 5) for (a, b), v in TC.items() if a == 1}; r0 = {b: v / R(2, 5) for (a, b), v in TC.items() if a == 0}
    assert r1 == {0: R(1, 3), 1: R(1, 6), 2: R(1, 2)} and sum(b * p for b, p in r1.items()) == R(7, 6)
    assert sum(b * p for b, p in r0.items()) == 1 and R(2, 5) * 1 + R(3, 5) * R(7, 6) == R(11, 10)
    assert sum(b * v for (a, b), v in TC.items()) == R(11, 10)
    assert R(56, 3) - 16 == R(8, 3)
    e1 = R(3, 10) + 2 * R(2, 10); e2 = R(2, 10)
    assert e1 == R(7, 10) and e1 * R(3, 10) + e2 * R(7, 10) == R(35, 100)
    j11, j21 = R(3, 10) * R(3, 10), R(7, 10) * R(2, 10)
    assert j11 / (j11 + j21) == R(9, 23)
    print('t3q2 verify ok')


if __name__ == '__main__':
    verify()
    D.save()
