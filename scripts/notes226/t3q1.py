r"""Test 3 - Question 1: marginal distributions and independence (Lectures 17-20, Tutorials 7-8).

Starts with joint tables, moves to slices of a joint density, and uses both to explain independence.
Supplementary topics, practice questions, and the formula sheet follow the worked examples.
"""
from fractions import Fraction as Fr
from math import log

from lib226 import Doc, S, cite

D = Doc('t3q1', 'Test 3 - Question 1', ['joint_distribution', 'marginal_distribution', 'independence'])

D.P(r'**Test 3, Question 1 · Marginal distributions and independence**')
D.P(r'A **joint distribution** describes $X$ and $Y$ together. A **marginal distribution** describes one of them on its own. For example, to find the chance that $X=0$, count every way $X=0$ can happen across all possible values of $Y$.',
    cites=cite('L17', 3, 7) + cite('L18', 5))
D.P(r'If you get a table of probabilities (a PMF), add across it. If you get a density (a PDF), integrate over a slice. Once you have both marginals, you can test whether the variables are independent.')

# =====================================================================================================
D.H('Read the marginals from a table')
D.P(r'Each cell gives the chance of one pair of values. The cell at $x=0$ and $y=1$ gives $P(X=0,Y=1)$. To find $P(X=0)$, keep $x=0$ fixed and add the cells for all $y$.', cites=cite('L17', 5, 7))
D.EQ(r'p_X(x)=P(X=x)=\sum_y p_{X,Y}(x,y)')
D.P(r'To find $P(Y=y)$, hold $y$ fixed and add over $x$. Follow the variable labels on the table. Either variable can appear in the rows.')
D.EQ(r'p_Y(y)=P(Y=y)=\sum_x p_{X,Y}(x,y)')
D.P(r'A valid table has nonnegative cells that add to $1$. If a cell contains an unknown $c$, set the total equal to $1$ and solve for $c$. Each marginal should add to $1$ on its own.')

D.EX('Add across the rows and down the columns',
     r'''Find the marginal distributions of $X$ and $Y$. Then find $P(X=1,\,Y\le1)$ and $P(X+Y\le2)$.

| | $y=0$ | $y=1$ | $y=2$ |
|---|---|---|---|
| $x=0$ | $0.10$ | $0.15$ | $0.05$ |
| $x=1$ | $0.20$ | $0.30$ | $0.20$ |''',
     [S(r'**Keep $X$ fixed.** For $X=0$, add all three cells in the first row. Repeat for $X=1$.',
        (r'p_X(0)=0.10+0.15+0.05=0.30', r'p_X(1)=0.20+0.30+0.20=0.70')),
      S(r'**Keep $Y$ fixed.** For $Y=0$, add the two cells in the first column. Repeat for the other columns.',
        (r'p_Y(0)=0.10+0.20=0.30', r'p_Y(1)=0.15+0.30=0.45', r'p_Y(2)=0.05+0.20=0.25')),
      S(r'**Apply both conditions.** Stay in row $x=1$ and use the columns where $y\le1$.',
        r'P(X=1,\,Y\le1)=0.20+0.30=0.50'),
      S(r'**Check the sum in each cell.** The pair $(1,2)$ is the only one where $x+y>2$. Subtract its probability from $1$.',
        r'P(X+Y\le2)=1-0.20=0.80')],
     r'$p_X(0)=0.30$, $p_X(1)=0.70$. $p_Y(0)=0.30$, $p_Y(1)=0.45$, $p_Y(2)=0.25$. The two event probabilities are $0.50$ and $0.80$.',
     cites=cite('L17', 6, 7) + cite('T7', 1))

D.H('Check independence in a table')
D.P(r'If $X$ and $Y$ are independent, learning $Y$ leaves the probabilities for $X$ unchanged. In the joint table, every cell then equals the product of the two marginal probabilities for that cell.', cites=cite('L19', 2))
D.EQ(r'p_{X,Y}(x,y)=p_X(x)\,p_Y(y)\quad\text{for every pair }(x,y)')
D.P(r'In the previous table, the chance of $X=0,Y=0$ is $0.10$. Independence would give $0.30\times0.30=0.09$. That one mismatch shows that $X$ and $Y$ are dependent.')

D.EX('Joint PMF table · independent ★ (Lecture 19)',
     r'''Are $X$ and $Y$ independent?

| | $Y=0$ | $Y=1$ |
|---|---|---|
| $X=0$ | $0.12$ | $0.18$ |
| $X=1$ | $0.28$ | $0.42$ |''',
     [S(r'**Marginals.**', (r'p_X(0)=0.30,\quad p_X(1)=0.70', r'p_Y(0)=0.40,\quad p_Y(1)=0.60')),
      S(r'**Compare** every cell with row × column.', (r'0.30\times0.40=0.12\ \checkmark\qquad 0.30\times0.60=0.18\ \checkmark', r'0.70\times0.40=0.28\ \checkmark\qquad 0.70\times0.60=0.42\ \checkmark')),
      S(r'All four match.')],
     r'Independent', cites=cite('L19', 2))

# =====================================================================================================
D.H('Set up a probability from a joint density')
D.P(r'A joint PDF gives a height at each point $(x,y)$. To get a probability, integrate that height over the part of the plane where the event happens.', cites=cite('L18', 2))
D.EQ(r'P\big((X,Y)\in A\big)=\iint_A f_{X,Y}(x,y)\,dx\,dy')
D.L([r'**Sketch** the region where the density is positive. This region is the support. For an event like $Y>X$, keep only the part above the line $y=x$.',
     r'**Choose the inner limits.** Hold $x$ fixed and draw a vertical line. Read the lowest and highest $y$ on that slice. These are the limits for $dy$.',
     r'**Choose the outer limits.** Move the line from the first $x$ that hits the region to the last $x$ that hits it. These are the limits for $dx$.'], ordered=True)
D.P(r'To find an unknown constant $c$, use the entire support and set the double integral equal to $1$.')

c15 = Fr(1, 15)
D.EX('Find $c$ and two probabilities ★ (Lecture 18)',
     r'$f_{X,Y}(x,y)=c$ for $0\le x\le5,\ 0\le y\le3$, and $0$ otherwise. (1) Find $c$. (2) $P(2\le X<3,\ 1\le Y<3)$. (3) $P(Y>X)$.',
     [S(r'**Sketch:** a $5\times3$ rectangle.'),
      S(r'(1) **Find $c$:** a flat height $c$ over area $15$ has volume $15c$.', r'\int_0^3\!\!\int_0^5c\,dx\,dy=15c=1\quad\Longrightarrow\quad c=\frac1{15}'),
      S(r'(2) A small rectangle, $1\times2$, under the same flat height.', r'P=\int_2^3\!\!\int_1^3\frac1{15}\,dy\,dx=\frac{(3-2)(3-1)}{15}=\frac2{15}'),
      S(r'(3) **Inner limits.** A vertical slice starts at $y=x$ and stops at the top of the box, $y=3$.'),
      S(r'**Outer limits.** Once $x$ reaches $3$, the slice runs out of room above $y=x$. So the outer integral stops at $x=3$.',
        r'P(Y>X)=\int_0^3\!\!\int_x^3\frac1{15}\,dy\,dx'),
      S(r'**Integrate.** The inner integral gives the slice length $3-x$ times the density $1/15$.',
        r'P(Y>X)=\frac1{15}\int_0^3(3-x)\,dx=\frac1{15}\Big(9-\frac92\Big)=\frac3{10}')],
     r'(1) $c=\tfrac1{15}$ (2) $\tfrac2{15}$ (3) $\tfrac3{10}$', cites=cite('L18', 3, 4))

D.H('Find a marginal density with one slice')
D.P(r'To find $f_X(x)$, pick a value of $x$ and add up the density along its vertical slice. Integrate over $y$ and leave $x$ in the answer.', cites=cite('L18', 5))
D.EQ(r'f_X(x)=\int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dy')
D.P(r'To find $f_Y(y)$, hold $y$ fixed and integrate along a horizontal slice. The slice gives the limits because the density is zero outside the support.')
D.EQ(r'f_Y(y)=\int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dx')
D.P(r'For example, in the triangle $0<x<y<1$, a vertical slice at $x=0.4$ runs from $y=0.4$ to $1$. For a general $x$, its limits are $x$ and $1$. The marginal $f_X$ is zero outside the possible $x$ values.')
D.REGION('Vertical slice through $x^2\\le y\\le1$', '(y>x^2)*(y<1)', x=(-1.2, 1.2), y=(-0.2, 1.2),
         extra=['slider s -1 1 0.5 label="$x$"', 'curve "x^2" from=-1.1 to=1.1 color=0 dash label="$y=x^2$"',
                'segment "s" "s^2" "s" "1" color=2 label="vertical slice: $y$ from $x^2$ to $1$"'],
         intro=r'Drag $x$ along the region for the next example. Which end of the slice moves as $x$ changes?')
D.EX('Marginals on a curved region ★ (Lecture 18)',
     r'$f_{X,Y}(x,y)=\dfrac{5y}{4}$ for $-1\le x\le1,\ x^2\le y\le1$, and $0$ otherwise. Find $f_X(x)$ and $f_Y(y)$.',
     [S(r'**Keep $x$ fixed.** The vertical slice starts at the curve $y=x^2$ and ends at the line $y=1$. A slice exists for $-1\le x\le1$.',
        r'f_X(x)=\int_{x^2}^1\frac{5y}{4}\,dy=\frac58\big(1-x^4\big)'),
      S(r'**Keep $y$ fixed.** Solve $x^2\le y$ for $x$. The horizontal slice runs from $-\sqrt y$ to $\sqrt y$, for $0\le y\le1$.'),
      S(r'**Integrate in $x$.** The height $5y/4$ stays constant along this horizontal slice. Multiply by the slice length $2\sqrt y$.',
        r'f_Y(y)=\int_{-\sqrt y}^{\sqrt y}\frac{5y}{4}\,dx=\frac{5y}{4}\cdot2\sqrt y=\frac52\,y^{3/2}'),
      S(r'**State the ranges.** Each marginal is zero outside its own range.')],
     r'$f_X(x)=\tfrac58(1-x^4)$ on $[-1,1]$; $f_Y(y)=\tfrac52y^{3/2}$ on $[0,1]$; $0$ elsewhere', cites=cite('L18', 5, 6))

# =====================================================================================================
D.H('Check independence for continuous variables')
D.P(r'Compute $f_X$ and $f_Y$, multiply them, and compare the product with the joint density. Include the ranges where each density is positive.', cites=cite('L19', 2, 4))
D.EQ(r'X,Y\text{ independent}\iff f_{X,Y}(x,y)=f_X(x)\,f_Y(y)\quad\text{almost everywhere}')
D.P(r'For densities, “almost everywhere” means differences on a boundary or at an isolated point have zero probability. To show dependence in these examples, look for a mismatch inside a region where it persists around the point you pick.')
D.P(r'**Use the shape as a clue.** If $x$ and $y$ each have positive marginal density but a whole region of those pairs is missing from the joint support, the product test fails. On a rectangle, compare the formulas inside it.')

D.EX('Independent ★ (Lecture 19)',
     r'$f_{X,Y}(x,y)=4xy$ for $0<x<1,\ 0<y<1$, and $0$ otherwise. Are $X$ and $Y$ independent?',
     [S(r'**Spot:** a square, and $4xy=(2x)(2y)$ splits. Expect independent.'),
      S(r'**Marginals:** slice at $x$, $y$ runs $0$ to $1$; and the same the other way.', (r'f_X(x)=\int_0^1 4xy\,dy=2x,\qquad 0<x<1', r'f_Y(y)=\int_0^1 4xy\,dx=2y,\qquad 0<y<1')),
      S(r'**Compare inside the square.**', r'f_X(x)\,f_Y(y)=2x\cdot2y=4xy=f_{X,Y}(x,y)'),
      S(r'**Check outside.** At least one marginal is zero there, and the joint density is zero too.')],
     r'Independent', cites=cite('L19', 3))

D.EX('Not independent: the region ★ (Lecture 19)',
     r'$f_{X,Y}(x,y)=\dfrac{5y}{4}$ on $-1\le x\le1,\ x^2\le y\le1$ (Example 4). Are $X$ and $Y$ independent?',
     [S(r'**Look for a missing pair.** The marginals allow $x=0.9$ and $y=0.25$. Can they occur together?'),
      S(r'**Marginals** from Example 4.', r'f_X(x)\,f_Y(y)=\frac58(1-x^4)\cdot\frac52y^{3/2}=\frac{25}{16}(1-x^4)\,y^{3/2}'),
      S(r'**Compare** below the parabola. At $(0.9,0.25)$ and nearby, $y<x^2$, so the joint density is zero and both marginals are positive.', r'f_{X,Y}(0.9,\,0.25)=0\ne f_X(0.9)\,f_Y(0.25)\approx' + f'{5 / 8 * (1 - 0.9 ** 4) * 5 / 2 * 0.25 ** 1.5:.3f}')],
     r'Not independent', cites=cite('L19', 4))

D.EX('Not independent: the formula ★ (Tutorial 7 Q5)',
     r'$f_{X,Y}(x,y)=x+y$ for $0<x<1,\ 0<y<1$. (a) Find $f_X$ and $f_Y$. (b) Are they independent? (c) $P(X+Y<1)$.',
     [S(r'(a) **Marginals.**', (r'f_X(x)=\int_0^1(x+y)\,dy=x+\frac12,\qquad 0<x<1', r'f_Y(y)=y+\frac12,\qquad 0<y<1\ \ \text{(same by symmetry)}')),
      S(r'(b) **Compare** at $(\tfrac14,\tfrac14)$ inside the square. The formulas are continuous there, so the mismatch persists nearby.',
        r'f_X\big(\tfrac14\big)f_Y\big(\tfrac14\big)=\frac34\cdot\frac34=\frac9{16}\ne\frac12=f_{X,Y}\big(\tfrac14,\tfrac14\big)'),
      S(r'(c) **Sketch** the line $x+y=1$; below it. **Slice** at $x$: $y$ from $0$ to $1-x$.', (r'P(X+Y<1)=\int_0^1\!\!\int_0^{1-x}(x+y)\,dy\,dx', r'=\int_0^1\Big(x(1-x)+\frac{(1-x)^2}{2}\Big)dx')),
      S(r'**Integrate.**', r'=\frac16+\frac16=\frac13')],
     r'(a) $x+\tfrac12$, $y+\tfrac12$ (b) not independent (c) $\tfrac13$', cites=cite('T7', 2))

# =====================================================================================================
D.H('Review the joint CDF and covariance')
D.H('Joint CDF', level=2)
D.P(r'The joint CDF $F_{X,Y}(a,b)$ is the chance that both $X\le a$ and $Y\le b$. In Example 1, $F_{X,Y}(0,1)$ uses just the first row and first two columns, so it equals $0.10+0.15=0.25$.', cites=cite('L17', 3, 4))
D.P(r'To find a rectangle probability from a joint CDF, start with the probability below and left of $(b,d)$. Subtract the strips left of $a$ and below $c$. Add their overlap back once.')
D.EQ(r'P(a<X\le b,\ c<Y\le d)=F(b,d)-F(a,d)-F(b,c)+F(a,c)', cites=cite('L17', 4))
D.EX('Rectangle from the joint CDF ★ (Tutorial 7 Q2)',
     r'$F_{X,Y}(3,5)=0.85$, $F_{X,Y}(1,5)=0.30$, $F_{X,Y}(3,2)=0.40$, $F_{X,Y}(1,2)=0.15$. Find $P(1<X\le3,\ 2<Y\le5)$. Also: how do you get $F_X(x)$ from $F_{X,Y}$?',
     [S(r'**Plug in** with $a=1,b=3,c=2,d=5$.', r'0.85-0.30-0.40+0.15=0.30'),
      S(r'**Marginal CDF:** let $y\to\infty$ (no limit on $Y$).', r'F_X(x)=F_{X,Y}(x,\infty)')],
     r'$0.30$; $F_X(x)=F_{X,Y}(x,\infty)$', cites=cite('T7', 1))

D.EX('Joint CDF from a PDF ★ (Lecture 18 Practice 2, Tutorial 8 Q2)',
     r'$f_{X,Y}(x,y)=2$ for $0\le y\le x\le1$. Find $F_{X,Y}(x,y)$.',
     [S(r'**Sketch:** the triangle under $y=x$. $F(x,y)$ = $2\times$ (the triangle’s area to the lower-left of $(x,y)$).'),
      S(r'Inside, $0\le y\le x\le1$: the corner cuts a trapezoid of area $xy-\tfrac{y^2}2$.', r'F=\int_0^y\!\!\int_v^x2\,du\,dv=2xy-y^2'),
      S(r'$0\le x<y$, $x\le1$: the corner holds the whole triangle up to $x$.', r'F=\int_0^x\!\!\int_0^u2\,dv\,du=x^2'),
      S(r'$x>1$, $0\le y\le1$: put $x=1$ in the inside formula. $y>1$, $0\le x\le1$: $x^2$. Both past $1$: $1$. Any negative: $0$.', r'F=2y-y^2\ \ (x>1),\qquad F=1\ \ (x,y\ge1)')],
     r'$F=0$ if $x<0$ or $y<0$; $2xy-y^2$ for $0\le y\le x\le1$; $x^2$ for $0\le x\le1,\ y\ge x$; $2y-y^2$ for $x>1,\ 0\le y\le1$; $1$ for $x,y\ge1$',
     cites=cite('L18', 4) + cite('T8', 1))

D.H('Covariance and jointly Gaussian variables', level=2)
D.P(r'**Covariance** (Lectures 19–20) measures whether $X$ and $Y$ tend to move together. To get $E[XY]$, weight each product $xy$ by the joint distribution using a double sum or integral.', cites=cite('L19', 7))
D.EQ(r'\operatorname{Cov}[X,Y]=E[XY]-E[X]\,E[Y]\qquad\qquad \rho_{X,Y}=\frac{\operatorname{Cov}[X,Y]}{\sigma_X\sigma_Y}', cites=cite('L20', 2))
D.L([r'Independent $\Rightarrow E[XY]=E[X]E[Y]\Rightarrow\operatorname{Cov}=0$. **Not** the other way round in general.',
     r'**Jointly Gaussian** is the exception: there, $\operatorname{Cov}=0\iff$ independent.',
     r'A Gaussian pair has $f=c\,e^{-(\dots)}$. **No $xy$ term** in the exponent → $\rho=0$ → independent. Match each square to $\dfrac{(x-\mu)^2}{2\sigma^2}$ to read off $\mu$ and $\sigma^2$.'],
     cites=cite('L20', 2, 4))
D.EX('A Gaussian pair ★ (Tutorial 8 Q9)',
     r'$f_{X,Y}(x,y)=c\exp\Big(-2x^2-\dfrac{y^2}{2}\Big)$. (a) What is it, and what is $c$? (b) Independent? (c) $E[X],E[Y],\operatorname{Var}(X),\operatorname{Var}(Y)$. (d) The PDF of $Z=aX+bY$.',
     [S(r'(a) **Spot:** $e^{-(\text{squares})}$ → bivariate Gaussian. Match $2x^2=\dfrac{x^2}{2\sigma_X^2}$ and $\dfrac{y^2}2=\dfrac{y^2}{2\sigma_Y^2}$.', r'\sigma_X^2=\frac14,\qquad \sigma_Y^2=1,\qquad \mu_X=\mu_Y=0'),
      S(r'With $\rho=0$ the constant is $\dfrac1{2\pi\sigma_X\sigma_Y}$.', r'c=\frac{1}{2\pi\cdot\frac12\cdot1}=\frac1\pi'),
      S(r'(b) No $xy$ term, so $f$ splits: $f=\big(\text{only }x\big)\big(\text{only }y\big)$ → **independent** (and uncorrelated).'),
      S(r'(c) Read off.', r'E[X]=E[Y]=0,\qquad \operatorname{Var}(X)=\frac14,\qquad \operatorname{Var}(Y)=1'),
      S(r'(d) A combination of independent Gaussians is Gaussian. Means add; variances add with $a^2$, $b^2$.', r'Z\sim N\Big(0,\ \frac{a^2}{4}+b^2\Big),\qquad f_Z(z)=\frac{1}{\sqrt{2\pi\big(\frac{a^2}4+b^2\big)}}\,e^{-z^2/\left(2\left(\frac{a^2}4+b^2\right)\right)}')],
     r'(a) Gaussian, $c=\tfrac1\pi$ (b) independent (c) $0,0,\tfrac14,1$ (d) $Z\sim N(0,\tfrac{a^2}4+b^2)$', cites=cite('T8', 2) + cite('L20', 4, 6))

# =====================================================================================================
D.H('Practice Questions')
D.P('Try the table first, then practise choosing the limits for a density. Open each solution after you try it. ★ marks problems based on the lectures or tutorials.')

# ---- tables
TA = {(1, 0): Fr(1, 10), (1, 1): Fr(1, 5), (1, 2): Fr(1, 10), (2, 0): Fr(3, 20), (2, 1): Fr(3, 10), (2, 2): Fr(3, 20)}
assert sum(TA.values()) == 1
pxA = {x: sum(v for (a, _), v in TA.items() if a == x) for x in (1, 2)}
pyA = {y: sum(v for (_, b), v in TA.items() if b == y) for y in (0, 1, 2)}
assert all(TA[x, y] == pxA[x] * pyA[y] for x, y in TA)
TB = {(0, 0): Fr(1, 5), (0, 1): Fr(1, 10), (1, 0): Fr(1, 10), (1, 1): Fr(3, 10), (2, 0): Fr(1, 10), (2, 1): Fr(1, 5)}
assert sum(TB.values()) == 1
D.Q('Joint PMF table · find $c$, marginals, independence',
    r'''(a) Find $c$, the marginals, $P(X+Y\le2)$ and $F_{X,Y}(1,1)$. Are $X$ and $Y$ independent?

| | $y=0$ | $y=1$ | $y=2$ |
|---|---|---|---|
| $x=1$ | $0.10$ | $0.20$ | $c$ |
| $x=2$ | $0.15$ | $0.30$ | $0.15$ |

(b) Same question for this table: are $X$ and $Y$ independent? Find $P(X<Y)$.

| | $y=0$ | $y=1$ |
|---|---|---|
| $x=0$ | $0.2$ | $0.1$ |
| $x=1$ | $0.1$ | $0.3$ |
| $x=2$ | $0.1$ | $0.2$ |''',
    [S(r'(a) **Find $c$:** the cells add to $1$.', r'0.9+c=1\quad\Longrightarrow\quad c=0.10'),
     S(r'**Marginals:** row and column totals.', (r'p_X(1)=0.40,\quad p_X(2)=0.60', r'p_Y(0)=0.25,\quad p_Y(1)=0.50,\quad p_Y(2)=0.25')),
     S(r'$x+y\le2$: cells $(1,0),(1,1),(2,0)$.', r'P(X+Y\le2)=0.10+0.20+0.15=0.45'),
     S(r'Lower-left of $(1,1)$: $x\le1$, $y\le1$.', r'F_{X,Y}(1,1)=0.10+0.20=0.30'),
     S(r'**Compare** all 6 cells with row × column.', (r'0.4(0.25)=0.10,\ \ 0.4(0.5)=0.20,\ \ 0.4(0.25)=0.10', r'0.6(0.25)=0.15,\ \ 0.6(0.5)=0.30,\ \ 0.6(0.25)=0.15')),
     S(r'All match → **independent**.'),
     S(r'(b) **Marginals**, then **Compare** one cell.', r'p_X(0)\,p_Y(0)=0.3\times0.4=0.12\ne0.2'),
     S(r'**Not** independent. $x<y$ only in cell $(0,1)$.', r'P(X<Y)=0.1')],
    r'(a) $c=0.1$; $p_X=0.4,0.6$; $p_Y=0.25,0.5,0.25$; $0.45$; $0.30$; independent (b) not independent; $0.1$', diff='introductory')

D.Q('Find $c$ and a circle probability ★ · Tutorial 8 Q1',
    r'$f_{X,Y}(x,y)=cxy$ for $0\le x\le1,\ 0\le y\le2$. Find $c$ and $P(X^2+Y^2\le1)$.',
    [S(r'**Find $c$:** the formula splits, so the double integral is a product.', r'c\int_0^1x\,dx\int_0^2y\,dy=c\cdot\frac12\cdot2=c=1'),
     S(r'**Sketch:** a quarter circle of radius $1$ (it fits inside the box, since $x\le1$, $y\le1<2$).'),
     S(r'**Slice** at $x$: $y$ from $0$ to $\sqrt{1-x^2}$.', r'P=\int_0^1\!\!\int_0^{\sqrt{1-x^2}}xy\,dy\,dx=\int_0^1x\cdot\frac{1-x^2}{2}\,dx'),
     S(r'**Integrate.**', r'=\frac12\Big(\frac12-\frac14\Big)=\frac18')],
    r'$c=1$, $P=\tfrac18$', cites=cite('T8', 1) + cite('L18', 4))

D.Q('Marginals and independence ★ · Tutorial 7 Q4',
    r'$f_{X,Y}(x,y)=12xy(1-x)$ for $0<x<1,\ 0<y<1$. (a) $f_X$, $f_Y$. (b) Independent? (c) $P(X<\tfrac12,\ Y<\tfrac12)$.',
    [S(r'(a) **Marginals.**', (r'f_X(x)=\int_0^1 12xy(1-x)\,dy=6x(1-x),\qquad 0<x<1', r'f_Y(y)=\int_0^1 12xy(1-x)\,dx=12y\Big(\frac12-\frac13\Big)=2y,\qquad 0<y<1')),
     S(r'(b) **Compare.**', (r'f_X\,f_Y=6x(1-x)\cdot2y=12xy(1-x)=f_{X,Y}', r'\Rightarrow\quad\text{independent}')),
     S(r'(c) Independent, so the joint probability is a product of the two single ones.', (r'P\big(X<\tfrac12\big)=\int_0^{1/2}6x(1-x)\,dx=\frac12', r'P\big(Y<\tfrac12\big)=\int_0^{1/2}2y\,dy=\frac14')),
     S(r'Multiply.', r'P=\frac12\cdot\frac14=\frac18')],
    r'(a) $6x(1-x)$, $2y$ (b) independent (c) $\tfrac18$', cites=cite('T7', 1))

D.Q('Triangle region ★ · Tutorial 7 Q6',
    r'$f_{X,Y}(x,y)=24xy$ for $x\ge0,\ y\ge0,\ x+y\le1$. (a) Sketch the region. (b) Check it is a valid PDF. (c) $f_X(x)$. (d) Independent?',
    [S(r'(a) **Sketch:** the triangle with corners $(0,0)$, $(1,0)$, $(0,1)$.'),
     S(r'(c) first: **Slice** at $x$, $y$ from $0$ to $1-x$.', r'f_X(x)=\int_0^{1-x}24xy\,dy=12x(1-x)^2,\qquad 0\le x\le1'),
     S(r'(b) $f\ge0$, and the total is $1$:', r'\int_0^1 12x(1-x)^2\,dx=12\Big(\frac12-\frac23+\frac14\Big)=1\ \checkmark'),
     S(r'(d) **Spot:** a triangle, not a rectangle → **not** independent. Proof: by symmetry $f_Y(y)=12y(1-y)^2$; at $(0.9,0.9)$, $f_{X,Y}=0$ (outside) but $f_X f_Y>0$.')],
    r'(b) valid (c) $12x(1-x)^2$ on $[0,1]$ (d) not independent', cites=cite('T7', 2))

D.Q('Find $k$, marginals, joint CDF, two probabilities ★ · Tutorial 8 Q8',
    r'$f_{X,Y}(x,y)=k(x+y)$ for $0\le x\le1,\ 0\le y\le1$. (a) $k$. (b) $f_X$, $f_Y$. (c) Independent? (d) The joint CDF inside the square. (e) $P(X<Y)$ and $P(Y<X^2)$.',
    [S(r'(a) **Find $c$.**', r'k\int_0^1\!\!\int_0^1(x+y)\,dy\,dx=k\Big(\frac12+\frac12\Big)=k=1'),
     S(r'(b) **Marginals** (as Example 7).', r'f_X(x)=x+\frac12,\qquad f_Y(y)=y+\frac12'),
     S(r'(c) At $(\tfrac14,\tfrac14)$ the marginal product is $\tfrac9{16}$ and the joint density is $\tfrac12$. The mismatch persists nearby, so the variables are dependent.'),
     S(r'(d) Integrate from the corner $(0,0)$.', r'F(x,y)=\int_0^x\!\!\int_0^y(u+v)\,dv\,du=\frac{x^2y+xy^2}{2},\qquad 0\le x,y\le1'),
     S(r'(e) $x+y$ is the same if you swap $x$ and $y$, so $X<Y$ and $Y<X$ are equally likely.', r'P(X<Y)=\frac12'),
     S(r'**Slice** at $x$: $y$ from $0$ to $x^2$.', (r'P(Y<X^2)=\int_0^1\!\!\int_0^{x^2}(x+y)\,dy\,dx', r'=\int_0^1\Big(x^3+\frac{x^4}2\Big)dx=\frac14+\frac1{10}=\frac7{20}'))],
    r'(a) $1$ (b) $x+\tfrac12$, $y+\tfrac12$ (c) no (d) $\tfrac{x^2y+xy^2}2$ (e) $\tfrac12$, $\tfrac7{20}$', cites=cite('T8', 2))

D.Q('Region probability ★ · Tutorial 8 Q7',
    r'$f_{X,Y}(x,y)=x-y+1$ for $x,y\in[0,1]$. Find $P(X+Y\ge\tfrac12)$.',
    [S(r'**Spot:** most of the square has $x+y\ge\tfrac12$. Do the small corner and subtract.'),
     S(r'**Sketch:** the corner triangle $x+y<\tfrac12$. **Slice** at $x$: $y$ from $0$ to $\tfrac12-x$, for $0\le x\le\tfrac12$.', r'P\big(X+Y<\tfrac12\big)=\int_0^{1/2}\!\!\int_0^{1/2-x}(x-y+1)\,dy\,dx'),
     S(r'**Integrate.** (The $x-y$ part cancels on this triangle by symmetry; the $1$ gives the area $\tfrac18$.)', r'=\frac18'),
     S(r'Complement.', r'P\big(X+Y\ge\tfrac12\big)=1-\frac18=\frac78')],
    r'$\tfrac78$', cites=cite('T8', 2))

e_val = (3 - 2 * log(2)) / 8
D.Q('Two independent uniforms ★ · Lecture 20, Tutorial 8 Q3',
    r'$X$ and $Y$ are independent, each uniform on $[-1,1]$. Find (a) $\operatorname{Cov}[X,Y]$ (b) $P(X^2<\tfrac14,\ |Y-1|>\tfrac12)$ (c) $P(X<Y,\ Y>\tfrac12)$ (d) $P(\max\{X,Y\}<\tfrac12)$ (e) $P(XY>\tfrac14)$.',
    [S(r'**Spot:** independent, so $f_{X,Y}=\tfrac12\cdot\tfrac12=\tfrac14$ on the square $[-1,1]^2$. A probability = $\tfrac14\times$ the area.'),
     S(r'(a) Independent → uncorrelated.', r'\operatorname{Cov}[X,Y]=E[XY]-E[X]E[Y]=0'),
     S(r'(b) Split into one event per variable. $X^2<\tfrac14\iff|X|<\tfrac12$. $|Y-1|>\tfrac12\iff Y<\tfrac12$ (since $Y\le1$).', r'P=P\big(|X|<\tfrac12\big)\,P\big(Y<\tfrac12\big)=\frac12\cdot\frac34=\frac38'),
     S(r'(c) **Slice** at $y\in(\tfrac12,1)$: $x$ from $-1$ to $y$.', r'P=\frac14\int_{1/2}^{1}(y+1)\,dy=\frac14\cdot\frac78=\frac7{32}'),
     S(r'(d) The max is below $\tfrac12$ exactly when **both** are.', r'P=P\big(X<\tfrac12\big)P\big(Y<\tfrac12\big)=\Big(\frac34\Big)^2=\frac9{16}'),
     S(r'(e) $XY>\tfrac14$: both positive or both negative, two mirror-image pieces. Positive piece: $x\in(\tfrac14,1)$, $y$ from $\tfrac1{4x}$ to $1$.', r'\text{area}=\int_{1/4}^{1}\Big(1-\frac1{4x}\Big)dx=\frac34-\frac{\ln4}{4}'),
     S(r'Two pieces, times $\tfrac14$.', r'P=2\cdot\frac14\Big(\frac34-\frac{\ln 4}{4}\Big)=\frac{3-2\ln2}{8}\approx' + f'{e_val:.4f}')],
    f'(a) $0$ (b) $\\tfrac38$ (c) $\\tfrac7{{32}}$ (d) $\\tfrac9{{16}}$ (e) $\\tfrac{{3-2\\ln2}}8\\approx{e_val:.4f}$', cites=cite('L20', 3) + cite('T8', 1))

D.Q('A Gaussian pair · like Tutorial 8 Q9',
    r'$f_{X,Y}(x,y)=c\exp\Big(-\dfrac{x^2}{2}-\dfrac{y^2}{8}\Big)$. Find $c$, $\operatorname{Var}(X)$, $\operatorname{Var}(Y)$; are $X$, $Y$ independent? What is the distribution of $Z=X-2Y$?',
    [S(r'**Spot:** Gaussian, no $xy$ term → $\rho=0$ → **independent**. Match $\dfrac{x^2}{2\sigma_X^2}$, $\dfrac{y^2}{2\sigma_Y^2}$.', r'\sigma_X^2=1,\qquad \sigma_Y^2=4,\qquad\mu_X=\mu_Y=0'),
     S(r'The constant.', r'c=\frac{1}{2\pi\sigma_X\sigma_Y}=\frac1{2\pi\cdot1\cdot2}=\frac1{4\pi}'),
     S(r'$Z=aX+bY$ with $a=1$, $b=-2$: Gaussian, mean $0$, variance $a^2\sigma_X^2+b^2\sigma_Y^2$.', r'\operatorname{Var}(Z)=1\cdot1+4\cdot4=17,\qquad Z\sim N(0,17)')],
    r'$c=\tfrac1{4\pi}$, $\operatorname{Var}(X)=1$, $\operatorname{Var}(Y)=4$, independent, $Z\sim N(0,17)$', cites=cite('T8', 2))

D.Q('A dome on a disk ★ · Tutorial 8 Q5 (a)(b)',
    r'$f_{X,Y}(x,y)=c\sqrt{1-x^2-y^2}$ for $x^2+y^2\le1$. (a) Find $c$. (b) Are $X$ and $Y$ independent?',
    [S(r'(a) **Find $c$:** the graph of $\sqrt{1-x^2-y^2}$ is the top half of a unit ball, volume $\tfrac12\cdot\tfrac43\pi=\tfrac23\pi$.', r'c\cdot\frac{2\pi}{3}=1\quad\Longrightarrow\quad c=\frac{3}{2\pi}'),
     S(r'(Without the ball: polar coordinates, $\int_0^{2\pi}\!\int_0^1\sqrt{1-r^2}\,r\,dr\,d\theta=2\pi\cdot\tfrac13$.)'),
     S(r'(b) **Spot:** a disk is not a rectangle → **not** independent. At $(0.9,0.9)$ the joint PDF is $0$ (outside the disk), but $f_X(0.9)>0$ and $f_Y(0.9)>0$.')],
    r'(a) $c=\tfrac3{2\pi}$ (b) not independent', cites=cite('T8', 1))

D.Q('Covariance from a joint PDF ★ · Lecture 19',
    r'$f_{X,Y}(x,y)=4xy$ on the unit square. Find $E[XY]$ and $\operatorname{Cov}[X,Y]$.',
    [S(r'$E[XY]$: put $xy$ in front of $f$, integrate over the square.', r'E[XY]=\int_0^1\!\!\int_0^1xy\cdot4xy\,dx\,dy=4\cdot\frac13\cdot\frac13=\frac49'),
     S(r'Means from the marginals $2x$ and $2y$ (Example 5).', r'E[X]=\int_0^1x\cdot2x\,dx=\frac23=E[Y]'),
     S(r'**Plug in.**', r'\operatorname{Cov}=\frac49-\frac23\cdot\frac23=0')],
    r'$E[XY]=\tfrac49$, $\operatorname{Cov}=0$ (as expected: they are independent)', cites=cite('L19', 6))

D.H('Test 3 formula sheet')
D.SHEET3()


def verify():
    import sympy as sp
    x, y, u, v, r, th = sp.symbols('x y u v r theta', real=True)
    I = sp.integrate
    R = sp.Rational
    # Lec 18
    assert I(R(1, 15), (x, 2, 3), (y, 1, 3)) == R(2, 15) and I(R(1, 15), (y, x, 3), (x, 0, 3)) == R(3, 10)
    fx = I(5 * y / 4, (y, x ** 2, 1)); fy = I(5 * y / 4, (x, -sp.sqrt(y), sp.sqrt(y)))
    assert sp.simplify(fx - R(5, 8) * (1 - x ** 4)) == 0 and sp.simplify(fy - R(5, 2) * y ** R(3, 2)) == 0
    assert (fx * fy).subs({x: R(9, 10), y: R(1, 4)}) > 0
    # Lec 19 / Tutorial 7 Q5
    assert I(4 * x * y, (y, 0, 1)) == 2 * x
    assert I(x + y, (y, 0, 1)) == x + R(1, 2) and I(x + y, (y, 0, 1 - x), (x, 0, 1)) == R(1, 3)
    # Extras
    assert R(85, 100) - R(30, 100) - R(40, 100) + R(15, 100) == R(3, 10)
    X, Y = sp.symbols('X Y', positive=True)
    assert sp.expand(I(2, (u, v, X), (v, 0, Y)) - (2 * X * Y - Y ** 2)) == 0 and I(2, (v, 0, u), (u, 0, X)) == X ** 2
    sx, sy = R(1, 2), 1
    cG = 1 / (2 * sp.pi * sx * sy)
    assert sp.simplify(I(cG * sp.exp(-2 * x ** 2 - y ** 2 / 2), (x, -sp.oo, sp.oo), (y, -sp.oo, sp.oo)) - 1) == 0
    assert sp.simplify(I(x ** 2 * cG * sp.exp(-2 * x ** 2 - y ** 2 / 2), (x, -sp.oo, sp.oo), (y, -sp.oo, sp.oo)) - R(1, 4)) == 0
    # practice
    assert I(x * y, (x, 0, 1), (y, 0, 2)) == 1 and I(x * y, (y, 0, sp.sqrt(1 - x ** 2)), (x, 0, 1)) == R(1, 8)
    g = 12 * x * y * (1 - x)
    assert sp.expand(I(g, (y, 0, 1)) - 6 * x * (1 - x)) == 0 and sp.expand(I(g, (x, 0, 1)) - 2 * y) == 0
    assert I(g, (x, 0, R(1, 2)), (y, 0, R(1, 2))) == R(1, 8)
    assert sp.expand(I(24 * x * y, (y, 0, 1 - x)) - 12 * x * (1 - x) ** 2) == 0 and I(12 * x * (1 - x) ** 2, (x, 0, 1)) == 1
    assert I(x + y, (y, 0, 1), (x, 0, 1)) == 1
    assert sp.expand(I(u + v, (v, 0, Y), (u, 0, X)) - (X ** 2 * Y + X * Y ** 2) / 2) == 0
    assert I(x + y, (y, x, 1), (x, 0, 1)) == R(1, 2) and I(x + y, (y, 0, x ** 2), (x, 0, 1)) == R(7, 20)
    assert I(x - y + 1, (y, 0, R(1, 2) - x), (x, 0, R(1, 2))) == R(1, 8)
    assert I(x - y + 1, (x, 0, 1), (y, 0, 1)) == 1
    q = R(1, 4)
    assert q * I(1, (x, -R(1, 2), R(1, 2)), (y, -1, R(1, 2))) == R(3, 8)
    assert q * I(1, (x, -1, y), (y, R(1, 2), 1)) == R(7, 32)
    assert q * I(1, (x, -1, R(1, 2)), (y, -1, R(1, 2))) == R(9, 16)
    pe = 2 * q * I(1 - 1 / (4 * x), (x, R(1, 4), 1))
    assert sp.simplify(pe - (3 - 2 * sp.log(2)) / 8) == 0 and abs(float(pe) - e_val) < 1e-12
    cg2 = 1 / (4 * sp.pi)
    assert sp.simplify(I(cg2 * sp.exp(-x ** 2 / 2 - y ** 2 / 8), (x, -sp.oo, sp.oo), (y, -sp.oo, sp.oo)) - 1) == 0
    assert sp.simplify(I(sp.sqrt(1 - r ** 2) * r, (r, 0, 1), (th, 0, 2 * sp.pi)) - 2 * sp.pi / 3) == 0
    assert I(x * y * 4 * x * y, (x, 0, 1), (y, 0, 1)) == R(4, 9) and I(2 * x * x, (x, 0, 1)) == R(2, 3)
    print('t3q1 verify ok')


if __name__ == '__main__':
    verify()
    D.save()
