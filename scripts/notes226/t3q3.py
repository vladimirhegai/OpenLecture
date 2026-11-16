r"""Test 3 - Question 3: conditional distributions for continuous random variables (Lectures 21-23, Tutorials 7-8).

Rewritten 2026-11-15 (same shape as t3q1): Part A conditional PDF, Part B conditional CDF and probabilities,
Part C conditional expectation (incl. E[g(X)|Y] from Lecture 23 and the Lecture 22 independence check).
Practice = 6 test-style questions (10 marks each).
"""
from lib226 import Doc, S, cite

D = Doc('t3q3', 'Test 3 - Question 3', ['conditional_pdf', 'conditional_cdf', 'conditional_expectation'])

# =====================================================================================================
D.P(r'**Test 3, Question 3 · Conditional distributions for continuous random variables** (10 marks)')
D.P(r'Same idea as Question 2, but with a formula $f_{X,Y}$. "Given $Y=y$" = stand on the horizontal line at height $y$. The conditional PDF is the joint PDF along that line, rescaled to have area $1$.')
D.CO('tip', r'''**Formula sheet lines for this question** (it chains all of them):

$$
f_Y(y)=\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dx\quad\longrightarrow\quad f_{X|Y}(x\mid y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}
$$

$$
F_X(x)=\int_{-\infty}^{x}f_X(t)\,dt\qquad\text{(use it with }f_{X|Y}\text{ for the conditional CDF)}
$$

$$
E[X\mid Y=y]=\int_{-\infty}^{\infty}x\,f_{X|Y}(x\mid y)\,dx
$$

Expect the Lecture 21–22 chain: **$f_Y$ → $f_{X|Y}$ → $F_{X|Y}$ → a probability → $E[X\mid Y=y]$ → independent?**''')

# =====================================================================================================
# PART A
# =====================================================================================================
D.H('Part A · Conditional PDF')
D.EQ(r'f_{X|Y}(x\mid y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}\qquad\text{for }y\text{ with }f_Y(y)>0', cites=cite('L21', 4))
D.L([r'**Slice:** fix $y$. Read the $x$ range off the inequalities (it may contain $y$).',
     r'**Marginal:** integrate $f_{X,Y}$ over that $x$ range to get $f_Y(y)$.',
     r'**Divide**, and write the range: "for $0<x<y$, and $0$ otherwise; valid for $0<y<1$".'], ordered=True)
D.P(r'Given $X=x$ instead? Swap the roles: vertical slice, $f_X(x)$, divide by $f_X(x)$.')
D.REGION('Horizontal slice through $0<x<y<1$', '(x>0)*(y>x)*(y<1)', x=(-0.1, 1.15), y=(-0.1, 1.15),
         extra=['slider s 0.05 0.95 0.5 label="$y$"', 'curve "x" from=0 to=1 color=0 dash label="$y=x$"',
                'segment "0" "s" "s" "s" color=2 label="slice at $Y=y$: $x$ from $0$ to $y$"'],
         intro=r'Move $y$. Where does the slice start and stop?')
D.EX('A flat triangle ★ (Lectures 21–22)',
     r'$f_{X,Y}(x,y)=2$ for $0<x<y<1$, and $0$ otherwise. Find $f_Y(y)$ and $f_{X|Y}(x\mid y)$.',
     [S(r'**Slice** at $y$: $x$ from $0$ to $y$.'),
      S(r'**Marginal.**', r'f_Y(y)=\int_0^y2\,dx=2y,\qquad0<y<1'),
      S(r'**Divide.**', r'f_{X|Y}(x\mid y)=\frac{2}{2y}=\frac1y,\qquad0<x<y\quad(0<y<1)')],
     r'$f_Y=2y$ on $(0,1)$; $f_{X|Y}=\tfrac1y$ on $(0,y)$: uniform on the slice', cites=cite('L21', 5) + cite('L22', 2))
D.P(r'Flat $f$ → the conditional is uniform: height $=1/(\text{slice length})$.')
D.EX('A formula that is not flat ★ (Tutorial 7 Q5)',
     r'$f_{X,Y}(x,y)=x+y$ for $0<x<1,\ 0<y<1$. Find $f_{X|Y}(x\mid y)$.',
     [S(r'**Slice** at $y$: $x$ from $0$ to $1$. **Marginal.**', r'f_Y(y)=\int_0^1(x+y)\,dx=\frac12+y'),
      S(r'**Divide.**', r'f_{X|Y}(x\mid y)=\frac{x+y}{y+\frac12},\qquad0<x<1\quad(0<y<1)')],
     r'$\dfrac{x+y}{y+1/2}$ on $(0,1)$', cites=cite('T7', 2))
D.TRY('Vertical slice, curved region',
      r'(a) Same triangle $f=2$ on $0<x<y<1$: find $f_{Y|X}(y\mid x)$. (b) $f=\tfrac{5y}{4}$ on $-1\le x\le1,\ x^2\le y\le1$, with $f_Y=\tfrac52y^{3/2}$: find $f_{X|Y}(x\mid y)$. ★ Lecture 18',
      [S(r'(a) **Vertical slice:** $y$ from $x$ to $1$.', (r'f_X(x)=\int_x^12\,dy=2(1-x)', r'f_{Y|X}(y\mid x)=\frac{1}{1-x},\qquad x<y<1')),
       S(r'(b) **Horizontal slice:** $-\sqrt y\le x\le\sqrt y$. **Divide.**', r'f_{X|Y}(x\mid y)=\frac{5y/4}{\frac52y^{3/2}}=\frac1{2\sqrt y},\qquad|x|\le\sqrt y')],
      r'(a) $\tfrac1{1-x}$ on $(x,1)$ (b) $\tfrac1{2\sqrt y}$ on $[-\sqrt y,\sqrt y]$', cites=cite('L18', 6))

# =====================================================================================================
# PART B
# =====================================================================================================
D.H('Part B · Conditional CDF and probabilities')
D.EQ(r'F_{X|Y}(x\mid y)=P(X\le x\mid Y=y)=\int_{-\infty}^{x}f_{X|Y}(u\mid y)\,du', cites=cite('L21', 4))
D.L([r'Three pieces: **$0$** before the slice, **$\int$ from the slice start to $x$** inside, **$1$** after.',
     r'For a probability, put the number $y$ in first. Then $P(a<X<b\mid Y=y)=\int_a^b f_{X|Y}(x\mid y)\,dx$, using only the part inside the slice.',
     r'Continuous: $<$ and $\le$ give the same answer.'])
D.EX('Triangle CDF ★ (Lecture 22)',
     r'With $f_{X|Y}=\tfrac1y$ on $0<x<y$ (Part A), find $F_{X|Y}(x\mid y)$ and $P(X<\tfrac14\mid Y=\tfrac12)$.',
     [S(r'**Inside** ($0<x<y$).', r'\int_0^x\frac1y\,du=\frac xy'),
      S(r'**All three pieces.**', r'F_{X|Y}(x\mid y)=\begin{cases}0,&x\le0\\ \dfrac xy,&0<x<y\\ 1,&x\ge y\end{cases}\qquad(0<y<1)'),
      S(r'**Plug in** $x=\tfrac14,\ y=\tfrac12$.', r'P\big(X<\tfrac14\ \big|\ Y=\tfrac12\big)=\frac{1/4}{1/2}=\frac12')],
     r'$0$, $\tfrac xy$, $1$; $\tfrac12$', cites=cite('L22', 3))
D.TRY('Not flat ★ (Tutorial 7 Q5 PDF)',
      r'$f_{X|Y}(x\mid y)=\dfrac{x+y}{y+\frac12}$ on $0<x<1$ (Part A). Find $F_{X|Y}(x\mid y)$ and $P(X<\tfrac12\mid Y=\tfrac12)$.',
      [S(r'**Inside.**', r'F_{X|Y}(x\mid y)=\int_0^x\frac{u+y}{y+\frac12}\,du=\frac{\frac{x^2}{2}+xy}{y+\frac12},\qquad0<x<1'),
       S(r'$0$ for $x\le0$, $1$ for $x\ge1$. **Plug in** $y=\tfrac12$ (bottom $=1$), $x=\tfrac12$.', r'\frac18+\frac14=\frac38')],
      r'$\dfrac{x^2/2+xy}{y+1/2}$ on $(0,1)$; $\tfrac38$', cites=cite('T7', 2))

# =====================================================================================================
# PART C
# =====================================================================================================
D.H('Part C · Conditional expectation')

# ---- C1 ----------------------------------------------------------------------------------------------
D.H('C1 · $E[X\\mid Y=y]$', level=2)
D.EQ(r'E[X\mid Y=y]=\int_{-\infty}^{\infty}x\,f_{X|Y}(x\mid y)\,dx', cites=cite('L22', 4))
D.L([r'Integrate over the slice only. The answer is usually a formula in $y$.',
     r'**Shortcut:** uniform on $(a,b)$ → mean $=\tfrac{a+b}2$. Triangle: $E[X\mid Y=y]=\tfrac y2$.',
     r'Independent → $E[X\mid Y=y]=E[X]$, a fixed number. If it **changes with $y$**, they are dependent, even on a rectangle.'])
D.EX('Mean, then independence ★ (Lecture 22)',
     r'$f_{X,Y}(x,y)=6xy(2-x-y)$ for $0<x<1,\ 0<y<1$. (a) Find $E[X\mid Y=y]$. (b) Are $X$ and $Y$ independent?',
     [S(r'(a) **Marginal.**', r'f_Y(y)=\int_0^1 6xy(2-x-y)\,dx=6y\Big(1-\frac13-\frac y2\Big)=y(4-3y)'),
      S(r'**Divide.**', r'f_{X|Y}(x\mid y)=\frac{6x(2-x-y)}{4-3y},\qquad0<x<1'),
      S(r'**Mean.**', (r'E[X\mid Y=y]=\frac{6}{4-3y}\int_0^1x^2(2-x-y)\,dx', r'=\frac{6}{4-3y}\Big(\frac23-\frac14-\frac y3\Big)', r'=\frac{5-4y}{2(4-3y)},\qquad0<y<1')),
      S(r'(b) It **changes with $y$** (e.g. $\tfrac58$ near $y=0$, $\tfrac12$ near $y=1$) → **dependent**, even though the region is a square.')],
     r'(a) $\dfrac{5-4y}{2(4-3y)}$ (b) dependent', cites=cite('L22', 6))
D.TRY('Two quick means',
      r'(a) $f=x+y$ on the unit square. Find $E[X\mid Y=y]$. (b) $f=e^{-y}$ for $0<x<y$. Find $f_{X|Y}$ and $E[X\mid Y=y]$.',
      [S(r'(a) **Weight** $\tfrac{x+y}{y+1/2}$ (Part A).', r'E[X\mid Y=y]=\frac{\int_0^1x(x+y)\,dx}{y+\frac12}=\frac{\frac13+\frac y2}{y+\frac12}=\frac{2+3y}{3(1+2y)}'),
       S(r'(b) **Slice** $0<x<y$: $f_Y=ye^{-y}$, so $f_{X|Y}=\tfrac1y$. Uniform → midpoint.', r'E[X\mid Y=y]=\frac y2')],
      r'(a) $\dfrac{2+3y}{3(1+2y)}$ (b) $\tfrac1y$ on $(0,y)$; $\tfrac y2$', cites=cite('T7', 2))

# ---- C2 ----------------------------------------------------------------------------------------------
D.H('C2 · $E[g(X)\\mid Y=y]$ (Lecture 23)', level=2)
D.P(r'Put $g(x)$ in front instead of $x$. For the variance use $g(x)=x^2$, then subtract the mean squared.', cites=cite('L23', 1))
D.EQ(r'E[g(X)\mid Y=y]=\int_{-\infty}^{\infty}g(x)\,f_{X|Y}(x\mid y)\,dx')
D.EX('$E[g(X)\\mid Y=1]$ ★ (Lecture 23)',
     r'$f_{X,Y}(x,y)=\tfrac12\,y\,e^{-xy}$ for $0<x<\infty,\ 0<y<2$. Find $E[e^{X/2}\mid Y=1]$.',
     [S(r'**Marginal:** slice $x$ from $0$ to $\infty$.', r'f_Y(y)=\int_0^\infty\frac12ye^{-xy}\,dx=\frac12,\qquad0<y<2'),
      S(r'**Divide**, then put $y=1$.', r'f_{X|Y}(x\mid y)=ye^{-xy}\quad\Rightarrow\quad f_{X|Y}(x\mid1)=e^{-x},\ x>0'),
      S(r'**Put $g(x)=e^{x/2}$ in front.**', (r'E[e^{X/2}\mid Y=1]=\int_0^\infty e^{x/2}e^{-x}\,dx=\int_0^\infty e^{-x/2}\,dx', r'=\Big[-2e^{-x/2}\Big]_0^\infty=2'))],
     r'$2$', cites=cite('L23', 2, 3))
D.TRY('Conditional variance',
      r'$f=e^{-y}$ for $0<x<y$, so $f_{X|Y}=\tfrac1y$ on $(0,y)$. Find $\operatorname{Var}(X\mid Y=y)$.',
      [S(r'**Square.**', r'E[X^2\mid Y=y]=\int_0^y\frac{x^2}{y}\,dx=\frac{y^2}{3}'),
       S(r'**Subtract** the mean squared ($\tfrac y2$).', r'\frac{y^2}3-\frac{y^2}4=\frac{y^2}{12}')],
      r'$\tfrac{y^2}{12}$')

# ---- C3 ----------------------------------------------------------------------------------------------
D.H('C3 · Total expectation (Lecture 23)', level=2)
D.P(r'Same rule as Question 2, with an integral: weight $E[X\mid Y=y]$ by $f_Y(y)$.', cites=cite('L23', 5))
D.EQ(r'E[X]=\int_{-\infty}^{\infty}E[X\mid Y=y]\,f_Y(y)\,dy')
D.EX('Back to the triangle',
     r'$f_{X,Y}=2$ on $0<x<y<1$. Use $E[X\mid Y=y]=\tfrac y2$ (C1) and $f_Y=2y$ (Part A) to find $E[X]$.',
     [S(r'**Weight and integrate.**', r'E[X]=\int_0^1\frac y2\cdot2y\,dy=\int_0^1y^2\,dy=\frac13'),
      S(r'**Check** with $f_X=2(1-x)$ (Part A Try it).', r'\int_0^1x\cdot2(1-x)\,dx=1-\frac23=\frac13\ \checkmark')],
     r'$\tfrac13$')
D.TRY('Your turn',
      r'$f=e^{-y}$ for $0<x<y$. You know $E[X\mid Y=y]=\tfrac y2$ and $f_Y=ye^{-y}$ for $y>0$. Find $E[X]$.',
      [S(r'**Weight and integrate.** Use $\int_0^\infty y^2e^{-y}\,dy=2$.', r'E[X]=\int_0^\infty\frac y2\cdot ye^{-y}\,dy=\frac12\cdot2=1')],
      r'$1$')

# =====================================================================================================
D.H('Practice Questions')
D.P('Test 2 difficulty, 10 marks each. Formula sheet only. ★ = from the lectures/tutorials.')

D.Q('[10 marks] The mirror triangle ★ (Tutorial 8 Q2 PDF)',
    r'$f_{X,Y}(x,y)=2$ for $0\le y\le x\le1$, and $0$ otherwise. (a) Find $f_X(x)$. (2 marks) (b) Find $f_{Y|X}(y\mid x)$. (2 marks) (c) Find $F_{Y|X}(y\mid x)$. (2 marks) (d) Find $P(Y<\tfrac14\mid X=\tfrac12)$. (2 marks) (e) Find $E[Y\mid X=x]$. Are $X,Y$ independent? (2 marks)',
    [S(r'(a) **Vertical slice:** $y$ from $0$ to $x$.', r'f_X(x)=\int_0^x2\,dy=2x,\qquad0<x\le1'),
     S(r'(b) **Divide.**', r'f_{Y|X}(y\mid x)=\frac{2}{2x}=\frac1x,\qquad0\le y\le x'),
     S(r'(c) **Three pieces.**', r'F_{Y|X}(y\mid x)=\begin{cases}0,&y<0\\ \dfrac yx,&0\le y\le x\\ 1,&y>x\end{cases}'),
     S(r'(d) **Plug in.**', r'F_{Y|X}\big(\tfrac14\mid\tfrac12\big)=\frac{1/4}{1/2}=\frac12'),
     S(r'(e) **Uniform on $(0,x)$** → midpoint. It changes with $x$ → **dependent**.', r'E[Y\mid X=x]=\frac x2')],
    r'(a) $2x$ (b) $\tfrac1x$ on $[0,x]$ (c) $0,\ \tfrac yx,\ 1$ (d) $\tfrac12$ (e) $\tfrac x2$; dependent', cites=cite('T8', 1))

D.Q('[10 marks] A triangle with $24xy$ ★ (Tutorial 7 Q6 PDF)',
    r'$f_{X,Y}(x,y)=24xy$ for $x\ge0,\ y\ge0,\ x+y\le1$. (a) Find $f_Y(y)$. (3 marks) (b) Find $f_{X|Y}(x\mid y)$. (2 marks) (c) Find $P(X<\tfrac14\mid Y=\tfrac12)$. (2 marks) (d) Find $E[X\mid Y=y]$. (3 marks)',
    [S(r'(a) **Horizontal slice:** $x$ from $0$ to $1-y$.', r'f_Y(y)=\int_0^{1-y}24xy\,dx=12y(1-y)^2,\qquad0\le y\le1'),
     S(r'(b) **Divide.**', r'f_{X|Y}(x\mid y)=\frac{24xy}{12y(1-y)^2}=\frac{2x}{(1-y)^2},\qquad0\le x\le1-y'),
     S(r'(c) **Put $y=\tfrac12$:** $f=8x$ on $(0,\tfrac12)$.', r'\int_0^{1/4}8x\,dx=4\cdot\frac1{16}=\frac14'),
     S(r'(d) **Mean.**', r'E[X\mid Y=y]=\int_0^{1-y}\frac{2x^2}{(1-y)^2}\,dx=\frac{2(1-y)^3}{3(1-y)^2}=\frac{2(1-y)}{3}')],
    r'(a) $12y(1-y)^2$ (b) $\tfrac{2x}{(1-y)^2}$ on $[0,1-y]$ (c) $\tfrac14$ (d) $\tfrac23(1-y)$', cites=cite('T7', 2))

D.Q('[10 marks] Given $X$ on a square ★ (Tutorial 8 Q8 PDF)',
    r'$f_{X,Y}(x,y)=x+y$ for $0\le x\le1,\ 0\le y\le1$. (a) Find $f_{Y|X}(y\mid x)$. (3 marks) (b) Find $P(Y>\tfrac12\mid X=0)$. (2 marks) (c) Find $E[Y\mid X=x]$. (3 marks) (d) Use (c) to decide if $X,Y$ are independent. (2 marks)',
    [S(r'(a) **Marginal** $f_X=x+\tfrac12$. **Divide.**', r'f_{Y|X}(y\mid x)=\frac{x+y}{x+\frac12},\qquad0\le y\le1'),
     S(r'(b) **Put $x=0$:** $f=2y$.', r'\int_{1/2}^1 2y\,dy=1-\frac14=\frac34'),
     S(r'(c) **Mean.**', r'E[Y\mid X=x]=\frac{\int_0^1y(x+y)\,dy}{x+\frac12}=\frac{\frac x2+\frac13}{x+\frac12}=\frac{3x+2}{3(2x+1)}'),
     S(r'(d) At $x=0$ it is $\tfrac23$, at $x=1$ it is $\tfrac59$. It changes → **dependent**.')],
    r'(a) $\tfrac{x+y}{x+1/2}$ (b) $\tfrac34$ (c) $\tfrac{3x+2}{3(2x+1)}$ (d) dependent', cites=cite('T8', 2))

D.Q('[10 marks] An exponential pair',
    r'$f_{X,Y}(x,y)=e^{-y}$ for $0<x<y$, and $0$ otherwise. (a) Find $f_X(x)$ and $f_{Y|X}(y\mid x)$. (4 marks) (b) Find $P(Y>x+1\mid X=x)$. (2 marks) (c) Find $E[Y\mid X=x]$. (2 marks) (d) Find $f_{X|Y}(x\mid y)$. (2 marks)',
    [S(r'(a) **Vertical slice:** $y$ from $x$ to $\infty$.', (r'f_X(x)=\int_x^\infty e^{-y}\,dy=e^{-x},\qquad x>0', r'f_{Y|X}(y\mid x)=\frac{e^{-y}}{e^{-x}}=e^{-(y-x)},\qquad y>x')),
     S(r'(b) **Integrate** from $x+1$.', r'\int_{x+1}^\infty e^{-(y-x)}\,dy=e^{-1}\approx0.368'),
     S(r'(c) **Mean** (substitute $t=y-x$).', r'E[Y\mid X=x]=\int_x^\infty y\,e^{-(y-x)}\,dy=x+1'),
     S(r'(d) **Horizontal slice** $0<x<y$: $f_Y=ye^{-y}$.', r'f_{X|Y}(x\mid y)=\frac{e^{-y}}{ye^{-y}}=\frac1y,\qquad0<x<y')],
    r'(a) $e^{-x}$; $e^{-(y-x)}$ on $y>x$ (b) $e^{-1}$ (c) $x+1$ (d) $\tfrac1y$ on $(0,y)$')

D.Q('[10 marks] Like Lecture 23',
    r'$f_{X,Y}(x,y)=\tfrac12\,y\,e^{-xy}$ for $x>0,\ 0<y<2$. (a) Find $f_Y(y)$ and $f_{X|Y}(x\mid y)$. (3 marks) (b) Find $P(X>1\mid Y=2)$. (2 marks) (c) Find $E[X\mid Y=y]$. (2 marks) (d) Find $E[e^{X}\mid Y=2]$. (3 marks)',
    [S(r'(a) **Slice** $x$ from $0$ to $\infty$.', (r'f_Y(y)=\frac12,\quad0<y<2', r'f_{X|Y}(x\mid y)=ye^{-xy},\quad x>0')),
     S(r'(b) **Put $y=2$:** $f=2e^{-2x}$.', r'\int_1^\infty2e^{-2x}\,dx=e^{-2}\approx0.135'),
     S(r'(c) **Mean** (exponential with rate $y$).', r'E[X\mid Y=y]=\int_0^\infty x\,ye^{-xy}\,dx=\frac1y'),
     S(r'(d) **$g(x)=e^x$**, $y=2$.', r'\int_0^\infty e^{x}\cdot2e^{-2x}\,dx=2\int_0^\infty e^{-x}\,dx=2')],
    r'(a) $\tfrac12$; $ye^{-xy}$ (b) $e^{-2}$ (c) $\tfrac1y$ (d) $2$')

D.Q('[10 marks] Find $c$ first',
    r'$f_{X,Y}(x,y)=c\,x$ for $0<y<x<1$, and $0$ otherwise. (a) Find $c$. (2 marks) (b) Find $f_Y(y)$ and $f_{X|Y}(x\mid y)$. (4 marks) (c) Find $P(X>\tfrac12\mid Y=0.2)$. (2 marks) (d) Find $f_{Y|X}(y\mid x)$ and $E[Y\mid X=x]$. (2 marks)',
    [S(r'(a) **Slice** $y$ from $0$ to $x$.', r'\int_0^1\!\!\int_0^x cx\,dy\,dx=c\int_0^1x^2\,dx=\frac c3=1\ \Rightarrow\ c=3'),
     S(r'(b) **Horizontal slice:** $x$ from $y$ to $1$.', (r'f_Y(y)=\int_y^13x\,dx=\frac32(1-y^2),\qquad0<y<1', r'f_{X|Y}(x\mid y)=\frac{3x}{\frac32(1-y^2)}=\frac{2x}{1-y^2},\qquad y<x<1')),
     S(r'(c) **Put $y=0.2$:** $1-y^2=0.96$.', r'\int_{0.5}^1\frac{2x}{0.96}\,dx=\frac{1-0.25}{0.96}=\frac{0.75}{0.96}=0.78125'),
     S(r'(d) $f_X=3x^2$. **Divide:** flat in $y$ → uniform on $(0,x)$.', r'f_{Y|X}(y\mid x)=\frac{3x}{3x^2}=\frac1x,\quad0<y<x;\qquad E[Y\mid X=x]=\frac x2')],
    r'(a) $3$ (b) $\tfrac32(1-y^2)$; $\tfrac{2x}{1-y^2}$ on $(y,1)$ (c) $0.78125=\tfrac{25}{32}$ (d) $\tfrac1x$; $\tfrac x2$')

D.H('Test 3 formula sheet')
D.SHEET3()


def verify():
    import sympy as sp
    x, y, u, t = sp.symbols('x y u t', positive=True)
    I = sp.integrate
    R = sp.Rational
    S_ = sp.simplify
    assert I(2, (x, 0, y)) == 2 * y and I(1 / y, (u, 0, x)) == x / y
    assert S_(I(x + y, (x, 0, 1)) - (y + R(1, 2))) == 0
    assert S_(I((u + y) / (y + R(1, 2)), (u, 0, x)) - (x ** 2 / 2 + x * y) / (y + R(1, 2))) == 0
    assert ((x ** 2 / 2 + x * y) / (y + R(1, 2))).subs({x: R(1, 2), y: R(1, 2)}) == R(3, 8)
    xx = sp.symbols('xx', real=True)
    assert S_(I(5 * y / 4, (xx, -sp.sqrt(y), sp.sqrt(y))) - R(5, 2) * y ** R(3, 2)) == 0
    f = 6 * x * y * (2 - x - y); fy = I(f, (x, 0, 1))
    assert S_(fy - y * (4 - 3 * y)) == 0
    e = S_(I(x * f / fy, (x, 0, 1)))
    assert S_(e - (5 - 4 * y) / (2 * (4 - 3 * y))) == 0 and e.subs(y, 0) == R(5, 8) and sp.limit(e, y, 1) == R(1, 2)
    assert S_(I(x * (x + y), (x, 0, 1)) / (y + R(1, 2)) - (2 + 3 * y) / (3 * (1 + 2 * y))) == 0
    assert S_(I(sp.exp(-y), (x, 0, y)) - y * sp.exp(-y)) == 0 and S_(I(x ** 2 / y, (x, 0, y)) - y ** 2 / 4 - y ** 2 / 12) == 0
    g = R(1, 2) * y * sp.exp(-x * y)
    assert S_(I(g, (x, 0, sp.oo)) - R(1, 2)) == 0
    assert I(sp.exp(x / 2) * sp.exp(-x), (x, 0, sp.oo)) == 2 and I(sp.exp(x) * 2 * sp.exp(-2 * x), (x, 0, sp.oo)) == 2
    assert I(2 * sp.exp(-2 * x), (x, 1, sp.oo)) == sp.exp(-2) and S_(I(x * y * sp.exp(-x * y), (x, 0, sp.oo)) - 1 / y) == 0
    assert I(y / 2 * 2 * y, (y, 0, 1)) == R(1, 3) and I(x * 2 * (1 - x), (x, 0, 1)) == R(1, 3)
    assert I(y / 2 * y * sp.exp(-y), (y, 0, sp.oo)) == 1
    # practice
    fy2 = I(24 * x * y, (x, 0, 1 - y))
    assert sp.expand(fy2 - 12 * y * (1 - y) ** 2) == 0
    cond = S_(24 * x * y / fy2)
    assert I(cond.subs(y, R(1, 2)), (x, 0, R(1, 4))) == R(1, 4) and S_(I(x * cond, (x, 0, 1 - y)) - R(2, 3) * (1 - y)) == 0
    ey = S_(I(y * (x + y), (y, 0, 1)) / (x + R(1, 2)))
    assert S_(ey - (3 * x + 2) / (3 * (2 * x + 1))) == 0 and ey.subs(x, 0) == R(2, 3) and ey.subs(x, 1) == R(5, 9)
    assert I(2 * y, (y, R(1, 2), 1)) == R(3, 4)
    assert S_(I(sp.exp(-y), (y, x, sp.oo)) - sp.exp(-x)) == 0 and S_(I(sp.exp(-(y - x)), (y, x + 1, sp.oo)) - sp.exp(-1)) == 0
    assert S_(I(y * sp.exp(-(y - x)), (y, x, sp.oo)) - (x + 1)) == 0
    assert I(3 * x, (y, 0, x), (x, 0, 1)) == 1 and S_(I(3 * x, (x, y, 1)) - R(3, 2) * (1 - y ** 2)) == 0
    assert I(2 * x / R(96, 100), (x, R(1, 2), 1)) == R(25, 32)
    print('t3q3 verify ok')


if __name__ == '__main__':
    verify()
    D.save()
