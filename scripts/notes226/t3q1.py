r"""Test 3 - Question 1: marginal distributions and independence (Lectures 17-20, Tutorials 7-8).

Rewritten 2026-11-15 to the user's outline: Part A discrete tables, Part B continuous densities, Part C joint CDFs.
Each topic = 1-3 line rule -> one worked example -> one Try it. Covariance and Gaussian pairs moved to t3x.py (Extra).
Practice = 6 test-style questions (10 marks each, Test 2 difficulty).
"""
from lib226 import Doc, S, cite

D = Doc('t3q1', 'Test 3 - Question 1', ['joint_distribution', 'marginal_distribution', 'independence'])

# =====================================================================================================
D.P(r'**Test 3, Question 1 · Marginal distributions and independence** (10 marks)')
D.P(r'You get two random variables, $X$ and $Y$, described together: a table (discrete) or a formula $f_{X,Y}(x,y)$ (continuous). You pull out $X$ alone and $Y$ alone (the **marginals**). Then you decide if they are **independent**.')
D.CO('tip', r'''**Formula sheet lines for this question.** They are on the sheet, so a question that needs them is very likely:

$$
f_X(x)=\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dy\qquad f_Y(y)=\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dx
$$

$$
F_X(x)=\sum_{t\le x}p_X(t)\qquad F_X(x)=\int_{-\infty}^{x}f_X(t)\,dt
$$

Expect: **find $c$ → a probability → marginals → independent? → a CDF**.''')

# =====================================================================================================
# PART A
# =====================================================================================================
D.H('Part A · Discrete (PMF tables)')

# ---- A1 ----------------------------------------------------------------------------------------------
D.H('A1 · Joint probability tables', level=2)
D.P(r'Each cell is the chance that **both** happen: $p_{X,Y}(x,y)=P(X=x,\ Y=y)$.', cites=cite('L17', 5))
D.L([r'Every cell is $\ge0$, and all cells add to $1$. An unknown $c$ comes from that.',
     r'For any event, add the cells that fit it.'])
D.EX('Find $c$, then add cells ★ (Lecture 17 table)',
     r'''Find $c$, $P(X=1,\ Y\le1)$ and $P(X+Y\le2)$.

| | $y=0$ | $y=1$ | $y=2$ |
|---|---|---|---|
| $x=0$ | $0.10$ | $0.15$ | $0.05$ |
| $x=1$ | $0.20$ | $c$ | $0.20$ |''',
     [S(r'**Find $c$:** all cells add to $1$.', r'0.70+c=1\quad\Longrightarrow\quad c=0.30'),
      S(r'**$P(X=1,\ Y\le1)$:** row $x=1$, columns $y=0,1$.', r'0.20+0.30=0.50'),
      S(r'**$P(X+Y\le2)$:** only $(1,2)$ has $x+y>2$. Take it away from $1$.', r'1-0.20=0.80')],
     r'$c=0.30$; $0.50$; $0.80$', cites=cite('L17', 6) + cite('T7', 1))
D.TRY('Build the table from an experiment',
      r'Toss a fair coin twice. $X$ = number of heads, $Y=1$ if the first toss is heads and $Y=0$ if not. Write the joint PMF table and find $P(X\ge Y)$.',
      [S(r'**List the 4 outcomes** (each $\tfrac14$) as $(x,y)$: $HH\to(2,1)$, $HT\to(1,1)$, $TH\to(1,0)$, $TT\to(0,0)$.'),
       S(r'**Table** (rows $x=0,1,2$, columns $y=0,1$).', (r'x=0:\ \ \tfrac14,\ 0', r'x=1:\ \ \tfrac14,\ \tfrac14', r'x=2:\ \ 0,\ \tfrac14')),
       S(r'**$P(X\ge Y)$:** every outcome has $x\ge y$.', r'P(X\ge Y)=1')],
      r'Table above; $P(X\ge Y)=1$', diff='introductory')

# ---- A2 ----------------------------------------------------------------------------------------------
D.H('A2 · Finding marginals', level=2)
D.P(r'$p_X(x)$ = the chance of $X=x$ whatever $Y$ is. So add the whole row of $x$. For $p_Y$, add the column.', cites=cite('L17', 7))
D.EQ(r'p_X(x)=\sum_y p_{X,Y}(x,y)\qquad\qquad p_Y(y)=\sum_x p_{X,Y}(x,y)')
D.EX('Row and column totals ★ (Lecture 17)',
     r'''Find $p_X$ and $p_Y$.

| | $y=0$ | $y=1$ | $y=2$ |
|---|---|---|---|
| $x=0$ | $0.10$ | $0.15$ | $0.05$ |
| $x=1$ | $0.20$ | $0.30$ | $0.20$ |''',
     [S(r'**Row totals** give $p_X$.', (r'p_X(0)=0.10+0.15+0.05=0.30', r'p_X(1)=0.20+0.30+0.20=0.70')),
      S(r'**Column totals** give $p_Y$.', r'p_Y(0)=0.30,\quad p_Y(1)=0.45,\quad p_Y(2)=0.25'),
      S(r'**Check:** each marginal adds to $1$. Both are $0$ at any other value.')],
     r'$p_X=0.30,\ 0.70$; $p_Y=0.30,\ 0.45,\ 0.25$', cites=cite('L17', 7))
D.CO('warning', r'Read the labels. If $y$ is down the side, the **row** totals are $p_Y$.')
D.TRY('Marginals, then use them',
      r'''Find $p_X$, $p_Y$, $P(X\ge2)$.

| | $x=1$ | $x=2$ | $x=3$ |
|---|---|---|---|
| $y=0$ | $0.10$ | $0.20$ | $0.10$ |
| $y=1$ | $0.15$ | $0.25$ | $0.20$ |''',
      [S(r'Here $x$ is across the top, so **column totals** give $p_X$.', r'p_X(1)=0.25,\quad p_X(2)=0.45,\quad p_X(3)=0.30'),
       S(r'**Row totals** give $p_Y$.', r'p_Y(0)=0.40,\quad p_Y(1)=0.60'),
       S(r'**Add** the marginal for $x=2,3$.', r'P(X\ge2)=0.45+0.30=0.75')],
      r'$p_X=0.25,\,0.45,\,0.30$; $p_Y=0.40,\,0.60$; $0.75$', diff='introductory')

# ---- A3 ----------------------------------------------------------------------------------------------
D.H('A3 · Checking independence', level=2)
D.P(r'Independent means every cell = its row total × its column total.', cites=cite('L19', 2))
D.EQ(r'p_{X,Y}(x,y)=p_X(x)\,p_Y(y)\quad\text{for EVERY }(x,y)')
D.L([r'**Dependent:** show one cell that fails. Done.',
     r'**Independent:** you must check every cell.',
     r'**Shortcut:** a $0$ cell whose row and column totals are not $0$ means dependent.'])
D.EX('Every cell passes ★ (Lecture 19)',
     r'''Are $X$ and $Y$ independent?

| | $Y=0$ | $Y=1$ |
|---|---|---|
| $X=0$ | $0.12$ | $0.18$ |
| $X=1$ | $0.28$ | $0.42$ |''',
     [S(r'**Marginals.**', r'p_X=0.30,\ 0.70\qquad p_Y=0.40,\ 0.60'),
      S(r'**Check all 4 cells.**', (r'0.30\times0.40=0.12\ \checkmark\qquad0.30\times0.60=0.18\ \checkmark', r'0.70\times0.40=0.28\ \checkmark\qquad0.70\times0.60=0.42\ \checkmark'))],
     r'Independent', cites=cite('L19', 2))
D.P(r'The Lecture 17 table (A2) is **dependent**: $p_X(0)\,p_Y(0)=0.30\times0.30=0.09\ne0.10$.')
D.TRY('Independent or not?',
      r'''(a)

| | $Y=0$ | $Y=1$ |
|---|---|---|
| $X=0$ | $0.06$ | $0.14$ |
| $X=1$ | $0.24$ | $0.56$ |

(b) The coin table from the A1 Try it.''',
      [S(r'(a) **Marginals** $p_X=0.20,\,0.80$ and $p_Y=0.30,\,0.70$. **Check all 4.**', (r'0.06,\ 0.14,\ 0.24,\ 0.56\ \text{all match}\ \checkmark')),
       S(r'(b) **Zero cell:** $p_{X,Y}(2,0)=0$, but $p_X(2)\,p_Y(0)=\tfrac14\cdot\tfrac12=\tfrac18\ne0$.')],
      r'(a) independent (b) dependent', diff='introductory')

# =====================================================================================================
# PART B
# =====================================================================================================
D.H('Part B · Continuous (PDFs)')
D.P(r'Same ideas as Part A. Add up cells → **integrate**.')

# ---- B1 ----------------------------------------------------------------------------------------------
D.H('B1 · Joint PDFs and finding $c$', level=2)
D.P(r'The joint PDF $f_{X,Y}(x,y)$ is a height over the $xy$-plane. Probability = volume under it. Total volume $=1$, which gives $c$.', cites=cite('L18', 2))
D.EQ(r'\iint_{\text{region}} f_{X,Y}(x,y)\,dx\,dy=1')
D.P(r'**Shortcut.** On a rectangle, if $f$ is an $x$-part times a $y$-part, integrate each part alone and multiply.')
D.EX('Find $c$ ★ (Tutorial 8 Q1)',
     r'$f_{X,Y}(x,y)=c\,xy$ for $0\le x\le1,\ 0\le y\le2$, and $0$ otherwise. Find $c$.',
     [S(r'**Rectangle** and $xy$ splits. Integrate each part.', (r'\int_0^1x\,dx=\frac12', r'\int_0^2y\,dy=2')),
      S(r'**Set the volume to $1$.**', r'c\cdot\frac12\cdot2=1\quad\Longrightarrow\quad c=1')],
     r'$c=1$', cites=cite('T8', 1))
D.TRY('Two more $c$’s',
      r'(a) $f=k(x+y)$ on $0\le x\le1,\ 0\le y\le1$ (Tutorial 8 Q8). (b) $f=c$ (a constant) on the triangle $0\le y\le x\le2$.',
      [S(r'(a) $x+y$ does not split, so integrate in two steps.', r'k\int_0^1\Big(x+\frac12\Big)dx=k\Big(\frac12+\frac12\Big)=k=1'),
       S(r'(b) A flat $f$: volume $=c\times$ area. The triangle has area $\tfrac12\cdot2\cdot2=2$.', r'2c=1\quad\Longrightarrow\quad c=\frac12')],
      r'(a) $k=1$ (b) $c=\tfrac12$', diff='introductory', cites=cite('T8', 2))

# ---- B2 ----------------------------------------------------------------------------------------------
D.H('B2 · Double integrals and bounds', level=2)
D.EQ(r'P\big((X,Y)\in A\big)=\iint_A f_{X,Y}(x,y)\,dy\,dx', cites=cite('L18', 2))
D.P(r'The limits are the hard part. Do this every time:')
D.L([r'**Sketch** where $f\ne0$, plus the event’s edge (e.g. the line $x+y=1$).',
     r'**Slice:** a vertical line at $x$. Where it enters and leaves the shaded part = the $dy$ limits.',
     r'**Sweep:** first to last $x$ that has a slice = the $dx$ limits.',
     r'**Integrate** $dy$ first (treat $x$ as a number), then $dx$.'], ordered=True)
D.P(r'Drag the slice. Where does it start and stop?')
D.REGION('The event $X+Y<1$ inside the unit square', '(x>0)*(x<1)*(y>0)*(y<1)', x=(-0.2, 1.3), y=(-0.2, 1.3),
         label='the square where $f\\ne0$',
         extra=['region "(x>0)*(y>0)*(x+y<1)" color=2 label="the event $X+Y<1$"',
                'slider s 0 1 0.3 label="$x$"',
                'segment "s" "0" "s" "1-s" color=3 label="slice: $y$ from $0$ to $1-x$"'])
D.EX('Probability under a slanted line ★ (Tutorial 7 Q5)',
     r'$f_{X,Y}(x,y)=x+y$ for $0<x<1,\ 0<y<1$. Find $P(X+Y<1)$.',
     [S(r'**Sketch:** the triangle under the line $y=1-x$.'),
      S(r'**Slice** at $x$: $y$ from $0$ to $1-x$. **Sweep:** $x$ from $0$ to $1$.', r'P=\int_0^1\!\!\int_0^{1-x}(x+y)\,dy\,dx'),
      S(r'**Inner** ($dy$).', r'\int_0^{1-x}(x+y)\,dy=x(1-x)+\frac{(1-x)^2}{2}=\frac{1-x^2}{2}'),
      S(r'**Outer** ($dx$).', r'\int_0^1\frac{1-x^2}{2}\,dx=\frac12\Big(1-\frac13\Big)=\frac13')],
     r'$\tfrac13$', cites=cite('T7', 2))
D.TRY('Two regions ★ (Tutorial 8 Q1, Q8)',
      r'(a) $f=xy$ on $0\le x\le1,\ 0\le y\le2$. Find $P(X^2+Y^2\le1)$. (b) $f=x+y$ on the unit square. Find $P(Y<X^2)$.',
      [S(r'(a) **Sketch:** a quarter circle of radius $1$. **Slice:** $y$ from $0$ to $\sqrt{1-x^2}$, for $0\le x\le1$.', r'\int_0^1\!\!\int_0^{\sqrt{1-x^2}}xy\,dy\,dx=\int_0^1\frac{x(1-x^2)}{2}\,dx=\frac18'),
       S(r'(b) **Slice:** $y$ from $0$ to $x^2$, for $0\le x\le1$.', (r'\int_0^1\!\!\int_0^{x^2}(x+y)\,dy\,dx=\int_0^1\Big(x^3+\frac{x^4}{2}\Big)dx', r'=\frac14+\frac1{10}=\frac7{20}'))],
      r'(a) $\tfrac18$ (b) $\tfrac7{20}$', cites=cite('T8', 1, 2))

# ---- B3 ----------------------------------------------------------------------------------------------
D.H('B3 · Finding marginal densities', level=2)
D.P(r'Integrate the **other** variable away. Same slice idea as B2, but you keep $x$ as a letter.', cites=cite('L18', 5))
D.EQ(r'f_X(x)=\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dy\qquad f_Y(y)=\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dx')
D.L([r'**$f_X$:** vertical slice at $x$ → $y$ limits (they can contain $x$).',
     r'**$f_Y$:** horizontal slice at $y$ → $x$ limits (they can contain $y$).',
     r'**State the range** ("$0<x<1$, and $0$ otherwise"). Marks are lost without it.'])
D.REGION('Slices through $-1\\le x\\le1,\\ x^2\\le y\\le1$', '(y>x^2)*(y<1)', x=(-1.3, 1.3), y=(-0.2, 1.3),
         extra=['slider s -1 1 0.5 label="$x$"', 'slider t 0 1 0.5 label="$y$"',
                'segment "s" "s^2" "s" "1" color=2 label="vertical: $y$ from $x^2$ to $1$"',
                'segment "-sqrt(t)" "t" "sqrt(t)" "t" color=3 label="horizontal: $x$ from $-\\sqrt y$ to $\\sqrt y$"'],
         intro=r'For the next example: drag both slices. Which ends move?')
D.EX('Curved region ★ (Lecture 18)',
     r'$f_{X,Y}(x,y)=\dfrac{5y}{4}$ for $-1\le x\le1,\ x^2\le y\le1$, and $0$ otherwise. Find $f_X$ and $f_Y$.',
     [S(r'**$f_X$:** vertical slice, $y$ from $x^2$ to $1$.', r'f_X(x)=\int_{x^2}^{1}\frac{5y}{4}\,dy=\frac58\big(1-x^4\big),\qquad -1\le x\le1'),
      S(r'**$f_Y$:** horizontal slice. $x^2\le y$ means $-\sqrt y\le x\le\sqrt y$.', r'f_Y(y)=\int_{-\sqrt y}^{\sqrt y}\frac{5y}{4}\,dx=\frac{5y}{4}\cdot2\sqrt y=\frac52y^{3/2},\qquad 0\le y\le1'),
      S(r'**Range:** both are $0$ outside those intervals.')],
     r'$f_X=\tfrac58(1-x^4)$ on $[-1,1]$; $f_Y=\tfrac52y^{3/2}$ on $[0,1]$', cites=cite('L18', 5, 6))
D.TRY('Triangle ★ (Tutorial 7 Q6)',
      r'$f_{X,Y}(x,y)=24xy$ for $x\ge0,\ y\ge0,\ x+y\le1$. Find $f_X(x)$ and $f_Y(y)$.',
      [S(r'**$f_X$:** slice at $x$, $y$ from $0$ to $1-x$.', r'f_X(x)=\int_0^{1-x}24xy\,dy=12x(1-x)^2,\qquad0\le x\le1'),
       S(r'**$f_Y$:** same shape with $x$ and $y$ swapped.', r'f_Y(y)=12y(1-y)^2,\qquad0\le y\le1')],
      r'$f_X=12x(1-x)^2$, $f_Y=12y(1-y)^2$, both on $[0,1]$', cites=cite('T7', 2))

# ---- B4 ----------------------------------------------------------------------------------------------
D.H('B4 · Checking independence', level=2)
D.EQ(r'X,Y\text{ independent}\iff f_{X,Y}(x,y)=f_X(x)\,f_Y(y)\text{ for all }x,y', cites=cite('L19', 2))
D.T(['You see', 'Answer', 'Justify with'],
    [['region is NOT a rectangle (triangle, curve)', 'dependent', r'a point outside the region where $f_X f_Y>0$'],
     ['rectangle, and $f$ = ($x$-part)×($y$-part)', 'independent', r'$f_X\,f_Y=f_{X,Y}$'],
     ['rectangle, $f$ does not split (e.g. $x+y$)', 'dependent', r'one point where $f_X f_Y\ne f_{X,Y}$']])
D.P(r'A rectangle alone does not prove independence. The formula must split too.', cites=cite('L19', 4))
D.EX('Show it with the marginals ★ (Tutorial 7 Q4)',
     r'$f_{X,Y}(x,y)=12xy(1-x)$ for $0<x<1,\ 0<y<1$. Find $f_X$, $f_Y$. Are $X$ and $Y$ independent?',
     [S(r'**Marginals.**', (r'f_X(x)=\int_0^1 12xy(1-x)\,dy=6x(1-x),\qquad0<x<1', r'f_Y(y)=\int_0^1 12xy(1-x)\,dx=12y\Big(\frac12-\frac13\Big)=2y,\qquad0<y<1')),
      S(r'**Multiply** and compare.', r'f_X(x)\,f_Y(y)=6x(1-x)\cdot2y=12xy(1-x)=f_{X,Y}(x,y)'),
      S(r'Outside the square both sides are $0$. So it holds everywhere.')],
     r'Independent', cites=cite('T7', 1))
D.TRY('Dependent: say why',
      r'(a) $f=24xy$ on the triangle $x+y\le1$ (B3). (b) $f=x+y$ on the unit square, with $f_X=x+\tfrac12$, $f_Y=y+\tfrac12$.',
      [S(r'(a) **Not a rectangle.** At $(0.9,\,0.9)$: $x+y>1$, so $f_{X,Y}=0$, but $f_X(0.9)\,f_Y(0.9)=(0.108)(0.108)>0$.'),
       S(r'(b) **Doesn’t split.** At $(0,0)$:', r'f_X(0)\,f_Y(0)=\frac12\cdot\frac12=\frac14\ne0=f_{X,Y}(0,0)')],
      r'Both dependent', cites=cite('T7', 2))

# =====================================================================================================
# PART C
# =====================================================================================================
D.H('Part C · Joint CDFs')

# ---- C1 ----------------------------------------------------------------------------------------------
D.H('C1 · What a joint CDF is', level=2)
D.EQ(r'F_{X,Y}(x,y)=P(X\le x,\ Y\le y)', cites=cite('L17', 3))
D.P(r'It is everything to the **lower left** of the point $(x,y)$.')
D.L([r'**Table:** add the cells with $x$-value $\le x$ and $y$-value $\le y$. Lecture 17 table: $F_{X,Y}(0,1)=0.10+0.15=0.25$.',
     r'**Density:** integrate from the bottom-left corner of the region up to $(x,y)$.'])
D.EQ(r'F_{X,Y}(x,y)=\int_{-\infty}^{x}\!\int_{-\infty}^{y}f_{X,Y}(u,v)\,dv\,du', cites=cite('L19', 1))
D.EX('Joint CDF on a square ★ (Tutorial 8 Q8d)',
     r'$f_{X,Y}(x,y)=x+y$ for $0\le x\le1,\ 0\le y\le1$. Find $F_{X,Y}(x,y)$ for all $x,y$.',
     [S(r'**Inside the square** ($0\le x,y\le1$): integrate from $(0,0)$.', r'F=\int_0^x\!\!\int_0^y(u+v)\,dv\,du=\frac{x^2y+xy^2}{2}'),
      S(r'**Past an edge:** that variable is "everything", so put in the edge value ($1$).', (r'x>1,\ 0\le y\le1:\quad F=\frac{y+y^2}{2}', r'y>1,\ 0\le x\le1:\quad F=\frac{x^2+x}{2}')),
      S(r'**Past both edges** $F=1$. **Left of or below** the square $F=0$.')],
     r'$\tfrac{x^2y+xy^2}2$ inside; $\tfrac{y+y^2}2$, $\tfrac{x^2+x}2$ past one edge; $1$ past both; $0$ below/left',
     cites=cite('T8', 2))
D.TRY('Joint CDF with a split formula',
      r'$f_{X,Y}(x,y)=4xy$ on $0\le x\le1,\ 0\le y\le1$. Find $F_{X,Y}(x,y)$ inside the square and $F_{X,Y}(0.5,\,2)$.',
      [S(r'**Inside.**', r'F=\int_0^x2u\,du\int_0^y2v\,dv=x^2y^2'),
       S(r'**$y=2$ is past the top**, so use $y=1$.', r'F(0.5,\,2)=F(0.5,\,1)=0.25')],
      r'$x^2y^2$; $0.25$', diff='introductory')

# ---- C2 ----------------------------------------------------------------------------------------------
D.H('C2 · Finding probabilities using CDFs', level=2)
D.P(r'For a rectangle: top-right corner, minus the two side strips, plus the bottom-left corner (it was taken away twice).', cites=cite('L17', 4))
D.REGION('Which corner is subtracted twice?', '(x<3)*(y<5)', x=(-0.5, 4), y=(-0.5, 6),
         label='$F(b,d)$: lower-left of $(b,d)$',
         extra=['region "(x>1)*(x<3)*(y>2)*(y<5)" color=2 label="the rectangle we want"',
                'point "1" "2" color=0', 'point "3" "2" color=0', 'point "1" "5" color=0', 'point "3" "5" color=0',
                'text "0.55" "1.7" "$(a,c)$"', 'text "3.45" "1.7" "$(b,c)$"',
                'text "0.55" "5.3" "$(a,d)$"', 'text "3.45" "5.3" "$(b,d)$"'])
D.EQ(r'P(a<X\le b,\ c<Y\le d)=F(b,d)-F(a,d)-F(b,c)+F(a,c)')
D.EX('Four corner values ★ (Tutorial 7 Q2)',
     r'$F_{X,Y}(3,5)=0.85$, $F_{X,Y}(1,5)=0.30$, $F_{X,Y}(3,2)=0.40$, $F_{X,Y}(1,2)=0.15$. Find $P(1<X\le3,\ 2<Y\le5)$.',
     [S(r'**Match:** $a=1,\ b=3,\ c=2,\ d=5$.'),
      S(r'**Plug in** with signs $+,-,-,+$.', r'0.85-0.30-0.40+0.15=0.30')],
     r'$0.30$', cites=cite('T7', 1))
D.TRY('Rectangle from a CDF formula',
      r'$F_{X,Y}(x,y)=x^2y^2$ on the unit square (C1 Try it). Find $P(0.5<X\le1,\ 0<Y\le0.5)$.',
      [S(r'**Match:** $a=0.5,\ b=1,\ c=0,\ d=0.5$. Anything with $y=0$ is $0$.', r'F(1,0.5)-F(0.5,0.5)-0+0=0.25-0.0625=0.1875')],
      r'$0.1875=\tfrac3{16}$', diff='introductory')

# ---- C3 ----------------------------------------------------------------------------------------------
D.H('C3 · Getting marginal CDFs', level=2)
D.P(r'For $F_X$, let $Y$ be anything: push $y$ to $\infty$. In practice, put in the top edge of the region.', cites=cite('L17', 3))
D.EQ(r'F_X(x)=F_{X,Y}(x,\infty)\qquad F_Y(y)=F_{X,Y}(\infty,y)')
D.P(r'Other route (formula sheet): find $f_X$ first, then $F_X(x)=\int_{-\infty}^{x}f_X(t)\,dt$. Both give the same answer.')
D.EX('Marginal CDF from the joint CDF',
     r'From C1, $F_{X,Y}=\dfrac{x^2y+xy^2}{2}$ on the unit square. Find $F_X(x)$.',
     [S(r'**Put in the top edge** $y=1$.', r'F_X(x)=F_{X,Y}(x,1)=\frac{x^2+x}{2},\qquad0\le x\le1'),
      S(r'**Full answer.**', r'F_X(x)=\begin{cases}0,&x<0\\ \dfrac{x^2+x}{2},&0\le x\le1\\ 1,&x>1\end{cases}'),
      S(r'**Check** with the formula sheet: $f_X=x+\tfrac12$ (B4 Try it).', r'\int_0^x\Big(t+\frac12\Big)dt=\frac{x^2}{2}+\frac x2\ \checkmark')],
     r'$F_X(x)=\tfrac{x^2+x}{2}$ on $[0,1]$')
D.TRY('Marginal CDFs and independence',
      r'$F_{X,Y}=x^2y^2$ on the unit square. Find $F_X$ and $F_Y$. Are $X,Y$ independent?',
      [S(r'**Top edges.**', r'F_X(x)=F(x,1)=x^2,\qquad F_Y(y)=F(1,y)=y^2'),
       S(r'**Independent** when the joint CDF splits: $F_{X,Y}=F_X\,F_Y$ (Lecture 19).', r'x^2\cdot y^2=x^2y^2\ \checkmark')],
      r'$x^2$, $y^2$; independent', diff='introductory', cites=cite('L19', 2))

# =====================================================================================================
D.H('Practice Questions')
D.P('Test 2 difficulty, 10 marks each like the real test. Do them closed-book with the formula sheet only. ★ = from the tutorials.')

D.Q('[10 marks] A table with $c$',
    r'''(a) Find $c$. (2 marks) (b) Find $p_X(x)$ and $p_Y(y)$. (3 marks) (c) Find $P(X+Y\le2)$ and $F_{X,Y}(1,1)$. (2 marks) (d) Are $X$ and $Y$ independent? Justify. (3 marks)

| | $y=0$ | $y=1$ | $y=2$ |
|---|---|---|---|
| $x=1$ | $0.10$ | $0.20$ | $c$ |
| $x=2$ | $0.15$ | $0.30$ | $0.15$ |''',
    [S(r'(a) **Cells add to $1$.**', r'0.90+c=1\ \Rightarrow\ c=0.10'),
     S(r'(b) **Row / column totals.**', (r'p_X(1)=0.40,\quad p_X(2)=0.60', r'p_Y(0)=0.25,\quad p_Y(1)=0.50,\quad p_Y(2)=0.25')),
     S(r'(c) $x+y\le2$: cells $(1,0),(1,1),(2,0)$. $F(1,1)$: $x\le1,\ y\le1$.', (r'P(X+Y\le2)=0.10+0.20+0.15=0.45', r'F_{X,Y}(1,1)=0.10+0.20=0.30')),
     S(r'(d) **Check all 6 cells.**', (r'0.4(0.25)=0.10,\ \ 0.4(0.5)=0.20,\ \ 0.4(0.25)=0.10', r'0.6(0.25)=0.15,\ \ 0.6(0.5)=0.30,\ \ 0.6(0.25)=0.15')),
     S(r'All match → **independent**.')],
    r'(a) $0.10$ (b) $0.4,\,0.6$; $0.25,\,0.5,\,0.25$ (c) $0.45$; $0.30$ (d) independent')

COIN = {}
for a in 'HT':
    for b in 'HT':
        for c_ in 'HT':
            k = ((a + b).count('H'), (b + c_).count('H'))
            COIN[k] = COIN.get(k, 0) + 1
D.Q('[10 marks] Build the table from coins',
    r'A fair coin is tossed 3 times. $X$ = number of heads in tosses 1–2, $Y$ = number of heads in tosses 2–3. (a) List the outcomes and write the joint PMF table. (4 marks) (b) Find $p_X$ and $p_Y$. (2 marks) (c) Find $P(X=Y)$. (1 mark) (d) Are $X$ and $Y$ independent? Justify. (3 marks)',
    [S(r'(a) **8 outcomes**, each $\tfrac18$. As $(x,y)$: $HHH(2,2)$, $HHT(2,1)$, $HTH(1,1)$, $HTT(1,0)$, $THH(1,2)$, $THT(1,1)$, $TTH(0,1)$, $TTT(0,0)$.'),
     S(r'**Count** each pair (in eighths). Rows $x=0,1,2$; columns $y=0,1,2$.', (r'x=0:\ \ 1,\ 1,\ 0', r'x=1:\ \ 1,\ 2,\ 1', r'x=2:\ \ 0,\ 1,\ 1')),
     S(r'(b) **Totals.**', r'p_X=p_Y=\frac28,\ \frac48,\ \frac28\quad(\text{at }0,1,2)'),
     S(r'(c) **Diagonal.**', r'P(X=Y)=\frac{1+2+1}{8}=\frac12'),
     S(r'(d) **Zero cell** $(0,2)$:', r'p_{X,Y}(0,2)=0\ne\frac28\cdot\frac28=p_X(0)\,p_Y(2)'),
     S(r'→ **dependent** (they share toss 2).')],
    r'(b) $\tfrac14,\tfrac12,\tfrac14$ each (c) $\tfrac12$ (d) dependent')

D.Q('[10 marks] A triangle ★ (Tutorial 7 Q6)',
    r'$f_{X,Y}(x,y)=24xy$ for $x\ge0,\ y\ge0,\ x+y\le1$, and $0$ otherwise. (a) Sketch the region. (1 mark) (b) Show it is a valid joint PDF. (3 marks) (c) Find $f_X(x)$. (3 marks) (d) Are $X$ and $Y$ independent? Explain. (3 marks)',
    [S(r'(a) **Sketch:** the triangle with corners $(0,0)$, $(1,0)$, $(0,1)$.'),
     S(r'(b) $24xy\ge0$ there. **Volume:** slice $y$ from $0$ to $1-x$.', (r'\int_0^1\!\!\int_0^{1-x}24xy\,dy\,dx=\int_0^1 12x(1-x)^2\,dx', r'=12\Big(\frac12-\frac23+\frac14\Big)=1\ \checkmark')),
     S(r'(c) **The inner integral above** is $f_X$.', r'f_X(x)=12x(1-x)^2,\quad 0\le x\le1;\quad 0\text{ otherwise}'),
     S(r'(d) **Not a rectangle → dependent.** At $(0.9,0.9)$, $f_{X,Y}=0$ but $f_X(0.9)\,f_Y(0.9)>0$ (by symmetry $f_Y=12y(1-y)^2$).')],
    r'(c) $12x(1-x)^2$ on $[0,1]$ (d) dependent', cites=cite('T7', 2))

D.Q('[10 marks] Find $k$, marginals, CDF ★ (Tutorial 8 Q8)',
    r'$f_{X,Y}(x,y)=k(x+y)$ for $0\le x\le1,\ 0\le y\le1$, and $0$ otherwise. (a) Find $k$. (2 marks) (b) Find $f_X$ and $f_Y$. (2 marks) (c) Are $X$ and $Y$ independent? (2 marks) (d) Find $F_{X,Y}(x,y)$ for $0\le x,y\le1$ and $F_X(x)$. (2 marks) (e) Find $P(X<Y)$. (2 marks)',
    [S(r'(a) **Volume $=1$.**', r'k\int_0^1\!\!\int_0^1(x+y)\,dy\,dx=k=1'),
     S(r'(b) **Integrate the other variable away.**', r'f_X(x)=x+\frac12,\quad f_Y(y)=y+\frac12\quad(\text{on }[0,1])'),
     S(r'(c) **Doesn’t split.** At $(0,0)$: $f_Xf_Y=\tfrac14\ne0$ → dependent.'),
     S(r'(d) **From $(0,0)$**, then the top edge $y=1$.', (r'F_{X,Y}=\frac{x^2y+xy^2}{2}', r'F_X(x)=\frac{x^2+x}{2}')),
     S(r'(e) **Slice** at $x$: $y$ from $x$ to $1$.', r'\int_0^1\!\!\int_x^1(x+y)\,dy\,dx=\int_0^1\Big(x+\frac12-\frac{3x^2}{2}\Big)dx=\frac12+\frac12-\frac12=\frac12')],
    r'(a) $1$ (b) $x+\tfrac12$, $y+\tfrac12$ (c) dependent (d) $\tfrac{x^2y+xy^2}2$; $\tfrac{x^2+x}2$ (e) $\tfrac12$', cites=cite('T8', 2))

D.Q('[10 marks] Exponential pair',
    r'$f_{X,Y}(x,y)=c\,e^{-x-2y}$ for $x>0,\ y>0$, and $0$ otherwise. (a) Find $c$. (2 marks) (b) Find $f_X$ and $f_Y$. (3 marks) (c) Are $X$ and $Y$ independent? (1 mark) (d) Find $F_{X,Y}(x,y)$ and $F_X(x)$. (2 marks) (e) Find $P(X<Y)$. (2 marks)',
    [S(r'(a) **Splits** ($e^{-x}\cdot e^{-2y}$) on a (infinite) rectangle.', r'c\int_0^\infty e^{-x}dx\int_0^\infty e^{-2y}dy=c\cdot1\cdot\frac12=1\ \Rightarrow\ c=2'),
     S(r'(b) **Integrate away.**', (r'f_X(x)=\int_0^\infty2e^{-x-2y}dy=e^{-x}\quad(x>0)', r'f_Y(y)=\int_0^\infty2e^{-x-2y}dx=2e^{-2y}\quad(y>0)')),
     S(r'(c) $f_Xf_Y=2e^{-x-2y}=f_{X,Y}$ → **independent**.'),
     S(r'(d) **From $(0,0)$.** Then $y\to\infty$.', (r'F_{X,Y}=\int_0^x e^{-u}du\int_0^y2e^{-2v}dv=(1-e^{-x})(1-e^{-2y})', r'F_X(x)=1-e^{-x},\quad x>0')),
     S(r'(e) **Slice:** $y$ from $x$ to $\infty$.', r'\int_0^\infty e^{-x}\Big(\int_x^\infty2e^{-2y}dy\Big)dx=\int_0^\infty e^{-3x}\,dx=\frac13')],
    r'(a) $2$ (b) $e^{-x}$, $2e^{-2y}$ (c) independent (d) $(1-e^{-x})(1-e^{-2y})$; $1-e^{-x}$ (e) $\tfrac13$')

D.Q('[10 marks] A flat triangle',
    r'$f_{X,Y}(x,y)=c$ for $0\le y\le x\le2$, and $0$ otherwise. (a) Find $c$. (2 marks) (b) Find $f_X(x)$ and $f_Y(y)$. (4 marks) (c) Are $X$ and $Y$ independent? (2 marks) (d) Find $P(X+Y\le2)$. (2 marks)',
    [S(r'(a) **Area** of the triangle is $\tfrac12\cdot2\cdot2=2$.', r'2c=1\ \Rightarrow\ c=\frac12'),
     S(r'(b) **$f_X$:** $y$ from $0$ to $x$. **$f_Y$:** $x$ from $y$ to $2$.', (r'f_X(x)=\int_0^x\frac12\,dy=\frac x2,\qquad0\le x\le2', r'f_Y(y)=\int_y^2\frac12\,dx=\frac{2-y}{2},\qquad0\le y\le2')),
     S(r'(c) **Triangle → dependent.** At $(0.5,\,1.5)$: $f_{X,Y}=0$ (needs $y\le x$), but $f_X(0.5)f_Y(1.5)=\tfrac14\cdot\tfrac14>0$.'),
     S(r'(d) **Sketch:** inside the triangle and under $x+y=2$. Slice horizontally: $x$ from $y$ to $2-y$, for $0\le y\le1$.', r'\int_0^1\!\!\int_y^{2-y}\frac12\,dx\,dy=\int_0^1(1-y)\,dy=\frac12')],
    r'(a) $\tfrac12$ (b) $\tfrac x2$; $\tfrac{2-y}2$ (c) dependent (d) $\tfrac12$')

D.H('Test 3 formula sheet')
D.SHEET3()


def verify():
    import sympy as sp
    x, y, u, v = sp.symbols('x y u v', positive=True)
    X, Y = sp.symbols('X Y', positive=True)
    I = sp.integrate
    R = sp.Rational
    t = [[R(10, 100), R(15, 100), R(5, 100)], [R(20, 100), R(30, 100), R(20, 100)]]
    assert sum(map(sum, t)) == 1 and t[1][0] + t[1][1] == R(1, 2) and 1 - t[1][2] == R(4, 5)
    px = [sum(r) for r in t]; py = [t[0][j] + t[1][j] for j in range(3)]
    assert px == [R(3, 10), R(7, 10)] and py == [R(3, 10), R(45, 100), R(25, 100)] and px[0] * py[0] == R(9, 100)
    e = [[R(10, 100), R(20, 100), R(10, 100)], [R(15, 100), R(25, 100), R(20, 100)]]
    assert [e[0][j] + e[1][j] for j in range(3)] == [R(1, 4), R(45, 100), R(3, 10)] and [sum(r) for r in e] == [R(2, 5), R(3, 5)]
    for tt in ([[R(12, 100), R(18, 100)], [R(28, 100), R(42, 100)]], [[R(6, 100), R(14, 100)], [R(24, 100), R(56, 100)]]):
        a = [sum(r) for r in tt]; b = [tt[0][j] + tt[1][j] for j in range(2)]
        assert all(tt[i][j] == a[i] * b[j] for i in range(2) for j in range(2))
    # B
    assert I(x, (x, 0, 1)) * I(y, (y, 0, 2)) == 1 and I(x + y, (y, 0, 1), (x, 0, 1)) == 1
    assert I(x + y, (y, 0, 1 - x), (x, 0, 1)) == R(1, 3) and sp.expand(I(x + y, (y, 0, 1 - x)) - (1 - x ** 2) / 2) == 0
    assert I(x * y, (y, 0, sp.sqrt(1 - x ** 2)), (x, 0, 1)) == R(1, 8) and I(x + y, (y, 0, x ** 2), (x, 0, 1)) == R(7, 20)
    xx = sp.symbols('xx', real=True)
    assert sp.simplify(I(5 * y / 4, (y, xx ** 2, 1)) - R(5, 8) * (1 - xx ** 4)) == 0
    assert sp.simplify(I(5 * y / 4, (xx, -sp.sqrt(y), sp.sqrt(y))) - R(5, 2) * y ** R(3, 2)) == 0
    assert sp.expand(I(24 * x * y, (y, 0, 1 - x)) - 12 * x * (1 - x) ** 2) == 0 and I(12 * x * (1 - x) ** 2, (x, 0, 1)) == 1
    g = 12 * x * y * (1 - x)
    assert sp.expand(I(g, (y, 0, 1)) - 6 * x * (1 - x)) == 0 and I(g, (x, 0, 1)) == 2 * y
    assert abs(12 * 0.9 * 0.1 ** 2 - 0.108) < 1e-12
    # C
    assert sp.expand(I(u + v, (v, 0, Y), (u, 0, X)) - (X ** 2 * Y + X * Y ** 2) / 2) == 0
    assert sp.expand(I(4 * u * v, (v, 0, Y), (u, 0, X)) - X ** 2 * Y ** 2) == 0
    F = lambda a, b: R(a) ** 2 * R(b) ** 2
    assert F(1, '0.5') - F('0.5', '0.5') == R(3, 16)
    assert R(85, 100) - R(30, 100) - R(40, 100) + R(15, 100) == R(3, 10)
    assert sp.expand(I(u + R(1, 2), (u, 0, X)) - (X ** 2 + X) / 2) == 0
    # practice
    assert COIN == {(2, 2): 1, (2, 1): 1, (1, 1): 2, (1, 0): 1, (1, 2): 1, (0, 1): 1, (0, 0): 1}
    assert I(x + y, (y, x, 1), (x, 0, 1)) == R(1, 2)
    assert I(2 * sp.exp(-x - 2 * y), (x, 0, sp.oo), (y, 0, sp.oo)) == 1
    assert I(2 * sp.exp(-x - 2 * y), (y, x, sp.oo), (x, 0, sp.oo)) == R(1, 3)
    assert I(R(1, 2), (y, 0, x), (x, 0, 2)) == 1 and I(R(1, 2), (x, y, 2 - y), (y, 0, 1)) == R(1, 2)
    print('t3q1 verify ok')


if __name__ == '__main__':
    verify()
    D.save()
