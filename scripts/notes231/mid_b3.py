"""B3: exact equations (Week 4).

Layout (REWRITE_PLAN.md). Shared letters: M dt + N dy = 0, U(t, y) = C, h(y) = a piece with only y (as in B1),
C = the constant. Step words: Write, Test, Integrate M, Match N, Answer, Plug in.
"""
import sympy as sp

from midlib import CARD, P, S, TAGS, implicit, link, t, y, zero


def build(D):
    W4 = lambda *p: D.cite('W4', *p)
    D.H('B3 · Exact equations', level=2, cites=W4(1, 2, 3, 4))
    TAGS(D, (4, 1), (4, 2))
    D.P(r'**Use this when** it’s neither separable nor linear, and it’s written with $dt$ and $dy$:')
    D.EQ(r'(2ty+3t^2)\,dt+t^2\,dy=0')
    D.P('Every exact equation is written like this, with everything on the left:')
    D.EQ(r'M\,dt+N\,dy=0')
    D.L([r'$M$ = everything multiplying $dt$, **sign included**',
         r'$N$ = everything multiplying $dy$, **sign included**'])
    D.P('**Short examples:**')
    D.EQ(r'(2ty+3t^2)\,dt+t^2\,dy=0\quad\Longrightarrow\quad M=2ty+3t^2,\quad N=t^2')
    D.P(r'Given $y\prime$ as a fraction? Cross-multiply, then move everything left:')
    D.EQ(r'y\prime=\dfrac{t-y}{t+y}\quad\Longrightarrow\quad (t-y)\,dt-(t+y)\,dy=0')
    D.EQ(r'M=t-y,\qquad N=-(t+y)')

    D.P(r'**The move: find one function $U(t,y)$** whose $t$-derivative is $M$ and whose $y$-derivative is $N$. The answer is:')
    D.EQ(r'U(t,y)=C')
    D.P(r'But first check it’s exact, with the **cross test**:')
    D.EQ(r'M_y=N_t')
    D.L([r'$M_y$ = differentiate $M$ in $y$, treating $t$ like a number',
         r'$N_t$ = differentiate $N$ in $t$, treating $y$ like a number',
         r'Not equal? Not exact: go to ' + link('B4', 'b4') + '.'])
    D.WHY('Why the cross test, and why $U=C$?',
          r'If $U$ exists, then $M=U_t$ and $N=U_y$. So $M_y$ is $U$ differentiated in $t$, then $y$. And $N_t$ is $U$ differentiated in $y$, then $t$. '
          r'The order doesn’t change the result, so the two must match.'
          '\n\n'
          r'$M\,dt+N\,dy$ is the small change in $U$. The equation sets that change to $0$, so $U$ stays at one constant value: $U=C$. '
          r'Each solution is a contour line of the surface $z=U(t,y)$, like on a map.')

    D.P('**Steps**')
    D.L([r'**Write** it as $M\,dt+N\,dy=0$, everything on the left. Read $M$ and $N$ with their signs.',
         r'**Test:** is $M_y=N_t$? If not, go to ' + link('B4', 'b4') + '.',
         r'**Integrate $M$ in $t$**, treating $y$ like a number. Instead of $+C$, add $h(y)$: a piece with only $y$.',
         r'**Match $N$:** differentiate $U$ in $y$ and set it equal to $N$. Everything cancels except $h\prime(y)$. Integrate it.',
         r'**Answer:** $U(t,y)=C$.',
         r'**Plug in** the condition to find $C$.'], ordered=True)
    D.EQ(r'U=\int M\,dt+h(y)')
    D.P(r'Why $h(y)$ and not $C$: anything with only $y$ in it disappears when you differentiate in $t$. So it could be hiding there.')
    D.P('**Short example:**')
    D.EQ(r'M=2ty+3t^2\quad\Longrightarrow\quad U=t^2y+t^3+h(y)')
    CARD(D, r'Full example (lecture 4.1): $\;(2ty+3t^2)\,dt+t^2\,dy=0$',
         [(r'**Write:** already in form.', r'M=2ty+3t^2,\qquad N=t^2'),
          (r'**Test:** for $M_y$ treat $t$ as a number. For $N_t$ treat $y$ as a number.', r'M_y=2t,\qquad N_t=2t\quad\checkmark'),
          (r'**Integrate $M$ in $t$** ($y$ is a number). Add $h(y)$.', r'U=t^2y+t^3+h(y)'),
          (r'**Match $N$:** differentiate $U$ in $y$, set it equal to $N=t^2$.', (r'U_y=t^2+h\prime(y)=t^2', r'h\prime(y)=0\quad\Rightarrow\quad h=\text{a number}')),
          (r'**Answer:** the number in $h$ merges into $C$.', r't^2y+t^3=C')],
         r't^2y+t^3=C\qquad\Big(y=\dfrac{C-t^3}{t^2}\Big)')
    CARD(D, r'Full example (lecture (b)): $\;y\prime=\dfrac{t-y}{t+y}$, $\;y(0)=1$',
         [(r'**Write:** cross-multiply, $(t+y)\,dy=(t-y)\,dt$, then move everything left. Moving $dy$ across flips its sign.',
           (r'(t-y)\,dt-(t+y)\,dy=0', r'M=t-y,\qquad N=-t-y')),
          (r'**Test.**', r'M_y=-1,\qquad N_t=-1\quad\checkmark'),
          (r'**Integrate $M$ in $t$.**', r'U=\tfrac12t^2-ty+h(y)'),
          (r'**Match $N$.**', (r'U_y=-t+h\prime(y)=-t-y', r'h\prime=-y\quad\Rightarrow\quad h=-\tfrac12y^2')),
          (r'**Answer:** set $U=C$, then multiply by $2$ ($2C$ is a new $C$).', r't^2-2ty-y^2=C'),
          (r'**Plug in** $t=0$, $y=1$.', r'0-0-1=C\quad\Rightarrow\quad C=-1')],
         r't^2-2ty-y^2=-1')

    D.P('**Partial derivatives.** Differentiate in one letter, treat the other like a plain number. Open a card:')
    CARD(D, r'In $t$: $\;\dfrac{\partial}{\partial t}(t^2y)=2ty$',
         [(r'$y$ acts like a number, like $5$: the derivative of $5t^2$ is $10t$.', r'\dfrac{\partial}{\partial t}(t^2y)=2t\cdot y')])
    CARD(D, r'In $y$: $\;\dfrac{\partial}{\partial y}(t^2y)=t^2$',
         [(r'$t^2$ acts like a number: the derivative of $5y$ is $5$.', r'\dfrac{\partial}{\partial y}(t^2y)=t^2'),
          (r'A term with no $y$ at all gives $0$.', r'\dfrac{\partial}{\partial y}(t-y)=0-1=-1')])
    CARD(D, r'Integrate in $t$: $\;\displaystyle\int(2ty+3t^2)\,dt=t^2y+t^3+h(y)$',
         [(r'$y$ acts like a number. The “constant” is $h(y)$.', r'\int 2ty\,dt=y\,t^2,\qquad \int3t^2\,dt=t^3')])
    D.CO('warning', r'**Moving the $dy$ term across the $=$ flips its sign.** In $y\prime=\frac{t-y}{t+y}$, $N$ is $-(t+y)$, not $t+y$. '
         r'One wrong sign and the test fails.')

    D.H('Practice: B3', level=3)
    P(D, 'W4 · Test, then solve · lecture exercise (a)',
      r'Test $3t\,dt+4y\,dy=0$ for exactness, and if so, solve.',
      [S(r'**Type:** $M\,dt+N\,dy=0$ → test for B3.'),
       S(r'**Write:** already in form.', r'M=3t,\qquad N=4y'),
       S(r'**Test:** $M$ has no $y$ and $N$ has no $t$, so both are $0$.', r'M_y=0,\qquad N_t=0\quad\checkmark'),
       S(r'**Integrate $M$ in $t$.**', r'U=\tfrac32t^2+h(y)'),
       S(r'**Match $N$:** $U_y=h\prime(y)$ must equal $4y$.', r'h\prime=4y\quad\Rightarrow\quad h=2y^2'),
       S(r'**Answer:** $U=C$. Multiply by $2$ ($2C$ is a new $C$).', r'3t^2+4y^2=C')],
      r'Exact. $3t^2+4y^2=C$: ellipses. (It’s also separable: $4y\,dy=-3t\,dt$.)', cites=W4(3))
    P(D, 'W4 · Test before you integrate · lecture exercise (d)',
      r'Is $y\prime=\dfrac{t}{t+y}$ exact?',
      [S(r'**Type:** a slope fraction → write it with $dt$, $dy$ and test.'),
       S(r'**Write:** cross-multiply, $(t+y)\,dy=t\,dt$, then move everything left.', (r't\,dt-(t+y)\,dy=0', r'M=t,\qquad N=-(t+y)')),
       S(r'**Test:** $M$ has no $y$.', r'M_y=0,\qquad N_t=-1'),
       S(r'$0\neq-1$, so it’s **not exact**. You’d try ' + link('B4', 'b4') + r' next, but neither ratio has just one letter. The lecture stops at “not exact”.',
         r'\dfrac{M_y-N_t}{N}=-\dfrac{1}{t+y},\qquad \dfrac{N_t-M_y}{M}=-\dfrac1t')],
      r'Not exact: $M_y=0\neq-1=N_t$.', cites=W4(4))
    P(D, 'W4 · The sign trap · lecture exercise (c)',
      r'Solve $2ty\,y\prime=t^2-y^2$.',
      [S(r'**Type:** not separable, not linear ($y^2$) → write with $dt$, $dy$ and test for B3.'),
       S(r'**Write:** $2ty\,dy=(t^2-y^2)\,dt$. Moving $2ty\,dy$ left makes it **negative**.', (r'(t^2-y^2)\,dt-2ty\,dy=0', r'M=t^2-y^2,\qquad N=-2ty')),
       S(r'**Test.**', r'M_y=-2y,\qquad N_t=-2y\quad\checkmark'),
       S(r'**Integrate $M$ in $t$.**', r'U=\tfrac13t^3-ty^2+h(y)'),
       S(r'**Match $N$:** $U_y=-2ty+h\prime$ must equal $-2ty$.', r'h\prime=0'),
       S(r'**Answer:** $U=C$. Multiply by $3$ ($3C$ is a new $C$).', r't^3-3ty^2=C')],
      r'$t^3-3ty^2=C$. Keep $+2ty\,dy$ (wrong sign) and the test gives $-2y\neq2y$.', diff='intermediate', cites=W4(4))


def verify():
    M, N = 2 * t * y + 3 * t ** 2, t ** 2
    zero(sp.diff(M, y) - sp.diff(N, t))
    implicit(t ** 2 * y + t ** 3, -M / N)
    zero(sp.integrate(M, t) - (t ** 2 * y + t ** 3))
    # (a)
    zero(sp.diff(3 * t, y) - sp.diff(4 * y, t))
    implicit(3 * t ** 2 + 4 * y ** 2, -3 * t / (4 * y))
    # (d) not exact, and neither integrating-factor ratio depends on one variable only
    M, N = t, -(t + y)
    assert sp.diff(M, y) == 0 and sp.diff(N, t) == -1
    assert sp.simplify((sp.diff(M, y) - sp.diff(N, t)) / N).has(y)
    assert sp.simplify((sp.diff(N, t) - sp.diff(M, y)) / M).has(t)
    # (b)
    M, N = t - y, -(t + y)
    zero(sp.diff(M, y) - sp.diff(N, t))
    assert implicit(t ** 2 - 2 * t * y - y ** 2, (t - y) / (t + y), (0, 1)) == -1
    # (c)
    M, N = t ** 2 - y ** 2, -2 * t * y
    zero(sp.diff(M, y) - sp.diff(N, t))
    implicit(t ** 3 - 3 * t * y ** 2, (t ** 2 - y ** 2) / (2 * t * y))
    assert sp.diff(M, y) != sp.diff(2 * t * y, t)
