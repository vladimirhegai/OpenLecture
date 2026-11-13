r"""Test 3 - Question 3: conditional distributions for continuous random variables."""
from math import exp

from lib226 import Doc, S, cite

D = Doc('t3q3', 'Test 3 - Question 3', ['conditional_pdf', 'conditional_cdf', 'conditional_probability', 'independence'])

D.P(r'**Test 3, Question 3 · Continuous conditional distributions**',
    cites=cite('L21', 4) + cite('L22', 1))
D.P(r'“Given $Y=y$” means you hold $y$ fixed and ask how $X$ can vary. On the $xy$-plane, this means working along the horizontal line at height $y$.')
D.P(r'First find the conditional density on that line. Once you have it, you can calculate probabilities, a CDF, or a mean with a one-variable integral.')

# =====================================================================================================
D.H('Find the slice and its conditional density')
D.P(r'For continuous $Y$, the event $Y=y$ has probability zero. The denominator you need is the **marginal density** $f_Y(y)$, which is the integral of the joint density along the selected slice.', cites=cite('L21', 4))
D.EQ(r'f_{X|Y}(x\mid y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}\qquad\text{wherever }f_Y(y)>0', cites=cite('L21', 4))
D.L([r'**Slice.** Hold $y$ fixed. Use the inequalities in the question to find the possible $x$ values.',
     r'**Integrate.** Add up the joint density along those $x$ values to get $f_Y(y)$.',
     r'**Divide.** Dividing by the slice total makes the conditional density integrate to $1$. For an allowed $y$, the conditional density is zero outside the slice.'], ordered=True)
D.P(r'If the question gives $X=x$, hold $x$ fixed and use a vertical slice. Integrate in $y$ to get $f_X(x)$, then divide by $f_X(x)$.')

D.REGION('Horizontal slice through $0<x<y<1$', '(x>0)*(y>x)*(y<1)', x=(-0.1, 1.15), y=(-0.1, 1.15),
         extra=['slider s 0.05 0.95 0.5 label="$y$"', 'curve "x" from=0 to=1 color=0 dash label="$y=x$"',
                'segment "0" "s" "s" "s" color=2 label="slice at $Y=y$: $x$ from $0$ to $y$"'],
         intro=r'Set $y=\tfrac12$ in the graph. Which $x$ values are still possible? Move $y$ up and watch what happens to the right endpoint.')
D.EX('Find the density on a horizontal slice ★ (Lectures 21–22)',
     r'$f_{X,Y}(x,y)=2$ for $0<x<y<1$ and zero elsewhere. Find $f_Y(y)$ and $f_{X|Y}(x\mid y)$.',
     [S(r'**Read the range.** For a fixed $y$ between $0$ and $1$, the inequality $0<x<y$ says the slice starts at $0$ and ends at $y$.'),
      S(r'**Find the marginal.** The joint density is $2$ along the whole slice, so its integral is $2$ times the length $y$.',
        r'f_Y(y)=\int_0^y 2\,dx=2y,\qquad 0<y<1'),
      S(r'**Divide.** The denominator $2y$ is the total from that same slice.',
        r'f_{X|Y}(x\mid y)=\frac{2}{2y}=\frac1y,\qquad 0<x<y'),
      S(r'**Check.** The conditional density has height $1/y$ and width $y$. Its area is $1$.')],
     r'$f_Y(y)=2y$ for $0<y<1$ and zero elsewhere. For those $y$, $f_{X|Y}(x\mid y)=\tfrac1y$ on $(0,y)$ and zero outside that slice.',
     cites=cite('L21', 5) + cite('L22', 1, 2, 3))

D.P(r'When the joint density is constant along a slice, the conditional density is uniform on that slice. Its height is $1$ divided by the slice length, since its total area has to be $1$.')

D.EX('Switch to a vertical slice',
     r'Same $f_{X,Y}=2$ on $0<x<y<1$. Find $f_{Y|X}(y\mid x)$ and $P(Y<0.6\mid X=0.5)$.',
     [S(r'**Fix $x$.** The line goes up from $y=x$ to $y=1$. Its length is $1-x$.',
        r'f_X(x)=\int_x^1 2\,dy=2(1-x),\qquad 0<x<1'),
      S(r'**Divide by $f_X(x)$.** This gives the new height for $Y$ along the vertical slice.',
        r'f_{Y|X}(y\mid x)=\frac{2}{2(1-x)}=\frac1{1-x},\qquad x<y<1'),
      S(r'**Use the requested slice.** At $x=0.5$, $Y$ ranges from $0.5$ to $1$. The part below $0.6$ has length $0.1$ out of the full length $0.5$.',
        r'P(Y<0.6\mid X=0.5)=\int_{0.5}^{0.6}\frac{1}{0.5}\,dy=\frac{0.1}{0.5}=0.2')],
     r'For $0<x<1$, the density is $\tfrac1{1-x}$ on $(x,1)$ and zero elsewhere. The probability is $0.2$.')

D.EX('A curved region ★ (Lecture 18 joint PDF)',
     r'$f_{X,Y}(x,y)=\dfrac{5y}{4}$ on $-1\le x\le1,\ x^2\le y\le1$, with $f_X=\tfrac58(1-x^4)$, $f_Y=\tfrac52y^{3/2}$ (Question 1). Find $f_{X|Y}(x\mid y)$ and $f_{Y|X}(y\mid x)$.',
     [S(r'**Hold $y$ fixed.** Solve $x^2\le y$ to get the horizontal slice. For $0<y\le1$, the denominator $f_Y(y)$ is positive.',
        r'f_{X|Y}(x\mid y)=\frac{5y/4}{\frac52y^{3/2}}=\frac{1}{2\sqrt y},\qquad -\sqrt y\le x\le\sqrt y'),
      S(r'**Hold $x$ fixed.** The vertical slice runs from $x^2$ to $1$. For $-1<x<1$, the denominator $f_X(x)$ is positive.',
        r'f_{Y|X}(y\mid x)=\frac{5y/4}{\frac58(1-x^4)}=\frac{2y}{1-x^4},\qquad x^2\le y\le1'),
      S(r'**Check:** $\int_{x^2}^1\frac{2y}{1-x^4}\,dy=\frac{1-x^4}{1-x^4}=1$ ✓.')],
     r'$f_{X|Y}=\tfrac1{2\sqrt y}$ on $|x|\le\sqrt y$; $f_{Y|X}=\tfrac{2y}{1-x^4}$ on $x^2\le y\le1$', cites=cite('L18', 6))

# =====================================================================================================
D.H('Get the conditional CDF and probabilities')
D.P(r'The **conditional CDF** gives the area to the left of a cutoff $x$ on your slice. The letter $u$ runs through the values you integrate over, while $x$ stays fixed at the cutoff.', cites=cite('L21', 4) + cite('L22', 2, 3))
D.EQ(r'F_{X|Y}(x\mid y)=P(X\le x\mid Y=y)=\int_{-\infty}^x f_{X|Y}(u\mid y)\,du')
D.L([r'**Before the slice**, the area is $0$.',
     r'**Inside the slice**, integrate from the left endpoint to the cutoff.',
     r'**After the slice**, the area is $1$.'])

D.EX('Turn the triangle density into a CDF ★ (Lecture 22)',
     r'Use $f_{X|Y}(x\mid y)=1/y$ on $0<x<y$, for $0<y<1$. Find $F_{X|Y}(x\mid y)$ and $P(X<\tfrac14\mid Y=\tfrac12)$.',
     [S(r'**Inside the slice.** The rectangle from $0$ to $x$ has width $x$ and height $1/y$.',
        r'\int_0^x\frac1y\,du=\frac xy'),
      S(r'**Include the endpoints.** At the left endpoint you have collected zero area. At the right endpoint you have collected all of it.',
        r'F_{X|Y}(x\mid y)=\begin{cases}0,&x\le0\\ \dfrac xy,&0<x<y\\ 1,&x\ge y\end{cases}'),
      S(r'**Use the given $y$.** When $y=\tfrac12$, the slice is $(0,\tfrac12)$. The cutoff $\tfrac14$ is halfway through it. A single point has zero probability, so the CDF also gives the strict inequality.',
        r'P(X<\tfrac14\mid Y=\tfrac12)=F_{X|Y}(\tfrac14\mid\tfrac12)=\frac{1/4}{1/2}=\frac12')],
     r'The CDF is $0$ up to $0$, $x/y$ inside the slice, and $1$ from $y$ onward. The requested probability is $\tfrac12$.',
     cites=cite('L22', 1, 2, 3))

D.P(r'For an interval, use the difference between the CDF at the two cutoffs. If you integrate directly, use just the part of the interval that overlaps the slice.')
D.EQ(r'P(a<X<b\mid Y=y)=F_{X|Y}(b\mid y)-F_{X|Y}(a\mid y)')
D.P(r'For example, on the triangle at $y=\tfrac12$, the event $0.3<X<0.8$ overlaps the slice from $0.3$ to $0.5$. Its probability is $1-0.3/0.5=0.4$.')

D.EX('On a square ★ (Tutorial 7 Q5 joint PDF)',
     r'$f_{X,Y}(x,y)=x+y$ on $0<x<1,\ 0<y<1$. Find $f_{X|Y}(x\mid y)$, $F_{X|Y}(x\mid y)$ and $P(X<\tfrac12\mid Y=\tfrac12)$.',
     [S(r'**Slice** at $y$: $x$ from $0$ to $1$. **Marginal.**', r'f_Y(y)=\int_0^1(x+y)\,dx=y+\frac12'),
      S(r'**Divide.**', r'f_{X|Y}(x\mid y)=\frac{x+y}{y+\frac12},\qquad 0<x<1'),
      S(r'**Accumulate** from $0$. Here the height changes with $x$, so integrate the density over the slice up to the cutoff.',
        r'F_{X|Y}(x\mid y)=\int_0^x\frac{u+y}{y+\frac12}\,du=\frac{\frac{x^2}2+xy}{y+\frac12},\qquad 0<x<1'),
      S(r'**Complete the CDF.** It is $0$ for $x\le0$ and $1$ for $x\ge1$.'),
      S(r'**Plug in** $y=\tfrac12$ and $x=\tfrac12$. The denominator becomes $1$.', r'P\big(X<\tfrac12\ \big|\ Y=\tfrac12\big)=\frac18+\frac14=\frac38')],
     r'On $(0,1)$, the density is $\tfrac{x+y}{y+1/2}$ and the CDF is $\tfrac{x^2/2+xy}{y+1/2}$. The probability is $\tfrac38$.', cites=cite('T7', 2))

D.H('Use the density for a mean or an independence check')
D.P(r'To find a conditional mean, multiply the density by $x$ before you integrate. For a uniform slice, the mean is its midpoint. For the triangle above, that gives $E[X\mid Y=y]=y/2$.', cites=cite('L22', 4))
D.EQ(r'E[X\mid Y=y]=\int_{-\infty}^{\infty} x\,f_{X|Y}(x\mid y)\,dx')
D.P(r'For independence, the conditional density must match $f_X(x)$, the density before you learn $Y$. Compare the range of $x$ as well as the formula.')
D.P(r'In the triangle, the upper endpoint moves with $y$. For instance, $x=0.4$ is possible when $y=0.5$, and its density is zero when $y=0.25$. Learning $Y$ changes the distribution of $X$.')

D.EX('Independent: the conditional is the marginal ★ (Tutorial 7 Q4 joint PDF)',
     r'$f_{X,Y}(x,y)=12xy(1-x)$ on the unit square. Find $f_{X|Y}(x\mid y)$ and $P(X<\tfrac12\mid Y=0.3)$.',
     [S(r'**Find the marginal.** Integrate over $x$ from $0$ to $1$.',
        r'f_Y(y)=12y\int_0^1x(1-x)\,dx=2y'),
      S(r'**Divide and compare.** For every $0<y<1$, the conditional density equals the marginal $f_X$ and has the same range $0<x<1$.',
        r'f_{X|Y}(x\mid y)=\frac{12xy(1-x)}{2y}=6x(1-x)=f_X(x)'),
      S(r'**Integrate.** Because $X$ and $Y$ are independent, you get the same probability for any of those values of $y$.',
        r'P(X<\tfrac12\mid Y=0.3)=\int_0^{1/2}6x(1-x)\,dx=\frac12')],
     r'$6x(1-x)$; $\tfrac12$', cites=cite('T7', 1))

# =====================================================================================================
D.H('Practice Questions')
D.P('Start each problem by writing down which variable is fixed and the range of the other variable. Open each solution after you try it. ★ marks problems based on the lectures or tutorials.')

D.Q('The mirror triangle ★ · Tutorial 8 Q2 joint PDF',
    r'$f_{X,Y}(x,y)=2$ for $0\le y\le x\le1$. Find (a) $f_X$ and $f_{Y|X}(y\mid x)$, (b) $F_{Y|X}(y\mid x)$, (c) $P(Y<\tfrac14\mid X=\tfrac12)$, (d) $f_{X|Y}(x\mid y)$. (e) Independent?',
    [S(r'**Sketch:** the triangle **below** the line $y=x$.'),
     S(r'(a) **Slice** at $x$: $y$ from $0$ to $x$. **Marginal**, then **Divide**.', (r'f_X(x)=\int_0^x2\,dy=2x,\qquad 0<x\le1', r'f_{Y|X}(y\mid x)=\frac{2}{2x}=\frac1x,\qquad 0\le y\le x')),
     S(r'(b) **Accumulate** from $0$.', r'F_{Y|X}(y\mid x)=\begin{cases}0,&y<0\\ \dfrac yx,&0\le y\le x\\ 1,&y>x\end{cases}'),
     S(r'(c) **Plug in.**', r'P\big(Y<\tfrac14\ \big|\ X=\tfrac12\big)=\frac{1/4}{1/2}=\frac12'),
     S(r'(d) **Slice** at $y$: $x$ from $y$ to $1$ (length $1-y$). Flat → uniform.', r'f_Y(y)=2(1-y),\qquad f_{X|Y}(x\mid y)=\frac1{1-y},\qquad y\le x\le1'),
     S(r'(e) A triangle → **not** independent.')],
    r'(a) $2x$; $\tfrac1x$ on $[0,x]$ (b) $0,\ \tfrac yx,\ 1$ (c) $\tfrac12$ (d) $\tfrac1{1-y}$ on $[y,1]$ (e) no', diff='introductory', cites=cite('T8', 1))

D.Q('A triangle with $24xy$ ★ · Tutorial 7 Q6 joint PDF',
    r'$f_{X,Y}(x,y)=24xy$ for $x,y\ge0,\ x+y\le1$. Find $f_{X|Y}(x\mid y)$, $F_{X|Y}(x\mid y)$, $P(X<\tfrac14\mid Y=\tfrac12)$ and $E[X\mid Y=y]$.',
    [S(r'**Slice** at $y$: $x$ from $0$ to $1-y$. **Marginal.**', r'f_Y(y)=\int_0^{1-y}24xy\,dx=12y(1-y)^2,\qquad 0<y<1'),
     S(r'**Divide.**', r'f_{X|Y}(x\mid y)=\frac{24xy}{12y(1-y)^2}=\frac{2x}{(1-y)^2},\qquad 0\le x\le1-y'),
     S(r'**Accumulate.**', r'F_{X|Y}(x\mid y)=\frac{x^2}{(1-y)^2}\quad(0\le x\le1-y);\ \ 0\text{ before},\ 1\text{ after}'),
     S(r'**Plug in** $y=\tfrac12$, $x=\tfrac14$.', r'P\big(X<\tfrac14\ \big|\ Y=\tfrac12\big)=\frac{1/16}{1/4}=\frac14'),
     S(r'**Mean.**', r'E[X\mid Y=y]=\int_0^{1-y}\frac{2x^2}{(1-y)^2}\,dx=\frac{2(1-y)}3')],
    r'$\tfrac{2x}{(1-y)^2}$ on $[0,1-y]$; $\tfrac{x^2}{(1-y)^2}$; $\tfrac14$; $\tfrac23(1-y)$', cites=cite('T7', 2))

D.Q('Given $X$ on a square ★ · Tutorial 8 Q8 joint PDF',
    r'$f_{X,Y}(x,y)=x+y$ on the unit square. Find $f_{Y|X}(y\mid x)$ and $P(Y>\tfrac12\mid X=\tfrac12)$.',
    [S(r'**Slice** at $x$: $y$ from $0$ to $1$. **Marginal.**', r'f_X(x)=x+\frac12'),
     S(r'**Divide.**', r'f_{Y|X}(y\mid x)=\frac{x+y}{x+\frac12},\qquad 0<y<1'),
     S(r'**Plug in** $x=\tfrac12$. The denominator becomes $1$.',
       r'P(Y>\tfrac12\mid X=\tfrac12)=\int_{1/2}^{1}(\tfrac12+y)\,dy=\frac58')],
    r'$\tfrac{x+y}{x+1/2}$ on $0<y<1$; $\tfrac58$', diff='introductory', cites=cite('T8', 2))

D.Q('Find a probability from a conditional density ★ · Lecture 22',
    r'$f_{X,Y}(x,y)=6xy(2-x-y)$ on the unit square, with $f_Y(y)=y(4-3y)$ as in the Question 2 note. Find $P(X<\tfrac12\mid Y=\tfrac12)$.',
    [S(r'**Divide**, then **Plug in** $y=\tfrac12$: $4-3y=\tfrac52$.', r'f_{X|Y}\big(x\ \big|\ \tfrac12\big)=\frac{6x(\frac32-x)}{\frac52}=\frac{12}{5}\,x\Big(\frac32-x\Big),\qquad 0<x<1'),
     S(r'Integrate from $0$ to $\tfrac12$.', r'P=\frac{12}5\Big(\frac32\cdot\frac18-\frac1{24}\Big)=\frac{12}5\cdot\frac{7}{48}=\frac7{20}')],
    r'$\tfrac7{20}$', cites=cite('L22', 6))

D.Q('An exponential pair',
    r'$f_{X,Y}(x,y)=e^{-y}$ for $0<x<y$. Find (a) $f_{X|Y}(x\mid y)$ and $P(X<1\mid Y=3)$, (b) $f_{Y|X}(y\mid x)$ and $P(Y>3\mid X=1)$.',
    [S(r'**Sketch:** above the line $y=x$, in the first quadrant, going up forever.'),
     S(r'(a) **Slice** at $y$: $x$ from $0$ to $y$. **Marginal**, **Divide.**', (r'f_Y(y)=\int_0^ye^{-y}\,dx=y\,e^{-y}', r'f_{X|Y}(x\mid y)=\frac1y,\qquad 0<x<y')),
     S(r'Uniform on $(0,3)$.', r'P(X<1\mid Y=3)=\frac13'),
     S(r'(b) **Slice** at $x$: $y$ from $x$ to $\infty$. **Marginal**, **Divide.**', (r'f_X(x)=\int_x^{\infty}e^{-y}\,dy=e^{-x}', r'f_{Y|X}(y\mid x)=e^{-(y-x)},\qquad y>x')),
     S(r'**Plug in** $x=1$.', r'P(Y>3\mid X=1)=\int_3^{\infty}e^{-(y-1)}\,dy=e^{-2}\approx' + f'{exp(-2):.4f}')],
    f'(a) $\\tfrac1y$ on $(0,y)$; $\\tfrac13$ (b) $e^{{-(y-x)}}$ for $y>x$; $e^{{-2}}\\approx{exp(-2):.4f}$')

D.Q('The parabola region ★ · Lecture 18 joint PDF',
    r'$f_{X,Y}(x,y)=\dfrac{5y}{4}$ on $-1\le x\le1,\ x^2\le y\le1$. Find $P(Y>\tfrac12\mid X=0)$ and $E[Y\mid X=0]$.',
    [S(r'From the curved region example, $f_{Y|X}(y\mid x)=\dfrac{2y}{1-x^4}$ on $x^2\le y\le1$. **Plug in** $x=0$.', r'f_{Y|X}(y\mid0)=2y,\qquad 0\le y\le1'),
     S(r'Probability.', r'P\big(Y>\tfrac12\ \big|\ X=0\big)=\int_{1/2}^12y\,dy=\frac34'),
     S(r'**Mean.**', r'E[Y\mid X=0]=\int_0^1y\cdot2y\,dy=\frac23')],
    r'$\tfrac34$; $\tfrac23$', diff='introductory', cites=cite('L18', 5))

D.Q('A triangle with $6x$',
    r'$f_{X,Y}(x,y)=6x$ for $0<x<y<1$. Find $f_Y$, $f_{X|Y}(x\mid y)$, $F_{X|Y}(x\mid y)$, $P(X<\tfrac12\mid Y=\tfrac34)$ and $E[X\mid Y=y]$.',
    [S(r'**Slice** at $y$: $x$ from $0$ to $y$. **Marginal.**', r'f_Y(y)=\int_0^y6x\,dx=3y^2,\qquad 0<y<1'),
     S(r'**Divide.**', r'f_{X|Y}(x\mid y)=\frac{6x}{3y^2}=\frac{2x}{y^2},\qquad 0<x<y'),
     S(r'**Accumulate.**', r'F_{X|Y}(x\mid y)=\frac{x^2}{y^2}\quad(0<x<y);\ \ 0\text{ before},\ 1\text{ after}'),
     S(r'**Plug in.**', r'P\big(X<\tfrac12\ \big|\ Y=\tfrac34\big)=\frac{(1/2)^2}{(3/4)^2}=\frac49'),
     S(r'**Mean.**', r'E[X\mid Y=y]=\int_0^y\frac{2x^2}{y^2}\,dx=\frac{2y}3')],
    r'$3y^2$; $\tfrac{2x}{y^2}$; $\tfrac{x^2}{y^2}$; $\tfrac49$; $\tfrac{2y}3$')

D.Q('Find $c$ first',
    r'$f_{X,Y}(x,y)=cx$ for $0\le y\le x\le1$. Find $c$, $f_{Y|X}(y\mid x)$, $f_{X|Y}(x\mid y)$ and $P(X>\tfrac12\mid Y=\tfrac14)$.',
    [S(r'**Find $c$:** slice at $x$, $y$ from $0$ to $x$.', r'\int_0^1\!\!\int_0^x cx\,dy\,dx=\int_0^1cx^2\,dx=\frac c3=1\quad\Longrightarrow\quad c=3'),
     S(r'Given $X=x$: **Marginal** $f_X=3x^2$, **Divide**. Flat in $y$ → uniform.', r'f_{Y|X}(y\mid x)=\frac{3x}{3x^2}=\frac1x,\qquad 0\le y\le x'),
     S(r'Given $Y=y$: slice $x$ from $y$ to $1$. **Marginal**, **Divide.**', (r'f_Y(y)=\int_y^13x\,dx=\frac32(1-y^2)', r'f_{X|Y}(x\mid y)=\frac{2x}{1-y^2},\qquad y\le x\le1')),
     S(r'**Plug in** $y=\tfrac14$: $1-y^2=\tfrac{15}{16}$.', r'P\big(X>\tfrac12\ \big|\ Y=\tfrac14\big)=\int_{1/2}^1\frac{2x}{15/16}\,dx=\frac{3/4}{15/16}=\frac45')],
    r'$c=3$; $\tfrac1x$; $\tfrac{2x}{1-y^2}$; $\tfrac45$')

D.Q('Uniform on a disk',
    r'$(X,Y)$ is uniform on the unit disk: $f_{X,Y}=\tfrac1\pi$ for $x^2+y^2\le1$. Find $f_{X|Y}(x\mid y)$, $P(X<\tfrac12\mid Y=0.6)$ and $E[X\mid Y=y]$. Independent?',
    [S(r'**Slice** at $y$: $x$ from $-\sqrt{1-y^2}$ to $\sqrt{1-y^2}$. Flat → uniform on that slice.', r'f_{X|Y}(x\mid y)=\frac{1}{2\sqrt{1-y^2}},\qquad |x|\le\sqrt{1-y^2}'),
     S(r'**Plug in** $y=0.6$: the slice is $-0.8<x<0.8$, length $1.6$.', r'P(X<0.5\mid Y=0.6)=\frac{0.5-(-0.8)}{1.6}=\frac{13}{16}'),
     S(r'**Mean:** the midpoint of the slice.', r'E[X\mid Y=y]=0'),
     S(r'The slice length changes with $y$ (a disk, not a rectangle) → **not** independent, even though $E[X\mid Y=y]$ is constant.')],
    r'$\tfrac{1}{2\sqrt{1-y^2}}$ on $|x|\le\sqrt{1-y^2}$; $\tfrac{13}{16}$; $0$; not independent')

D.Q('Product form · Lecture 19 joint PDF',
    r'$f_{X,Y}(x,y)=4xy$ on the unit square. Find $f_{X|Y}(x\mid y)$ and $P(X>\tfrac12\mid Y=\tfrac13)$.',
    [S(r'**Marginal** $f_Y=2y$. **Divide.**', r'f_{X|Y}(x\mid y)=\frac{4xy}{2y}=2x=f_X(x),\qquad 0<x<1'),
     S(r'No $y$ left → **independent**; the $\tfrac13$ doesn’t matter.', r'P\big(X>\tfrac12\ \big|\ Y=\tfrac13\big)=\int_{1/2}^12x\,dx=\frac34')],
    r'$2x$; $\tfrac34$', diff='introductory', cites=cite('L19', 3))

D.H('Test 3 formula sheet')
D.SHEET3()


def verify():
    import sympy as sp
    x, y, u = sp.symbols('x y u', positive=True)
    I = sp.integrate
    R = sp.Rational
    assert I(2, (x, 0, y)) == 2 * y and I(1 / y, (u, 0, x)) == x / y and R(1, 4) / R(1, 2) == R(1, 2)
    assert I(2, (y, x, 1)) == 2 * (1 - x) and I(2, (y, R(1, 2), R(3, 5))) == R(1, 5)
    fy = R(5, 2) * y ** R(3, 2)
    assert sp.simplify(R(5, 4) * y / fy - 1 / (2 * sp.sqrt(y))) == 0
    assert sp.simplify(I(2 * y / (1 - x ** 4), (y, x ** 2, 1))) == 1
    cdf = I((u + y) / (y + R(1, 2)), (u, 0, x))
    assert sp.simplify(cdf - (x ** 2 / 2 + x * y) / (y + R(1, 2))) == 0 and cdf.subs({y: R(1, 2), x: R(1, 2)}) == R(3, 8)
    assert I(6 * x * (1 - x), (x, 0, R(1, 2))) == R(1, 2)
    # practice
    assert I(2 * y / (1 - x ** 4), (y, R(1, 2), 1)).subs(x, 0) == R(3, 4) and I(2 * y * y, (y, 0, 1)) == R(2, 3)
    fy24 = I(24 * x * y, (x, 0, 1 - y))
    assert sp.simplify(fy24 - 12 * y * (1 - y) ** 2) == 0
    assert I(2 * x / R(1, 4), (x, 0, R(1, 4))) == R(1, 4)
    assert I(R(1, 2) + y, (y, R(1, 2), 1)) == R(5, 8)
    f6 = 6 * x * y * (2 - x - y)
    fy6 = I(f6, (x, 0, 1))
    assert I((f6 / fy6).subs(y, R(1, 2)), (x, 0, R(1, 2))) == R(7, 20)
    assert I(sp.exp(-(y - 1)), (y, 3, sp.oo)) == sp.exp(-2) and I(sp.exp(-y), (y, x, sp.oo)) == sp.exp(-x)
    assert I(6 * x, (x, 0, y)) == 3 * y ** 2 and (R(1, 2) / R(3, 4)) ** 2 == R(4, 9)
    assert sp.simplify(I(x * 2 * x / y ** 2, (x, 0, y)) - 2 * y / 3) == 0
    c = sp.Symbol('c')
    assert sp.solve(I(c * x, (y, 0, x), (x, 0, 1)) - 1, c) == [3]
    assert sp.simplify(I(3 * x, (x, y, 1)) - R(3, 2) * (1 - y ** 2)) == 0
    assert I(2 * x / (1 - R(1, 16)), (x, R(1, 2), 1)) == R(4, 5)
    assert (R(1, 2) + R(4, 5)) / R(8, 5) == R(13, 16)
    assert I(2 * x, (x, R(1, 2), 1)) == R(3, 4)
    print('t3q3 verify ok')


if __name__ == '__main__':
    verify()
    D.save()
