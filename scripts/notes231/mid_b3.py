"""B3: exact equations (Week 4)."""
import sympy as sp

from midlib import P, S, TAGS, implicit, link, t, y, zero


def build(D):
    W4 = lambda *p: D.cite('W4', *p)
    D.H('B3 · Exact equations', level=2, cites=W4(1, 2, 3, 4))
    TAGS(D, (4, 1), (4, 2))
    D.P(r'**When the equation comes in “$dt$ and $dy$” form.** Some first-order equations are neither separable nor linear, '
        r'but their left side is the change of one hidden function $U(t,y)$. Then the solution is simply $U(t,y)=C$.')
    D.P('Write the equation with everything on the left:')
    D.EQ(r'M(t,y)\,dt+N(t,y)\,dy=0')
    D.L([r'$M$ = everything multiplying $dt$, **sign included**',
         r'$N$ = everything multiplying $dy$, **sign included**'])
    D.P('Examples:')
    D.L([r'$3t\,dt+4y\,dy=0$: $\;M=3t$, $N=4y$.',
         r'$y\prime=\dfrac{t-y}{t+y}$ → cross-multiply: $(t+y)\,dy=(t-y)\,dt$ → move all left: $(t-y)\,dt-(t+y)\,dy=0$. '
         r'So $M=t-y$, $N=-(t+y)$.',
         r'$2ty\,y\prime=t^2-y^2$ → $(t^2-y^2)\,dt-2ty\,dy=0$. So $M=t^2-y^2$, $N=-2ty$.'])
    D.CO('warning', r'Moving the $dy$ term across the $=$ sign flips its sign. In $y\prime=\frac{t-y}{t+y}$, $N$ is $-(t+y)$, not $t+y$. '
         r'One wrong sign makes the test fail.')

    D.P(r'**The exactness test.** The equation is **exact** when the cross derivatives match:')
    D.EQ(r'\dfrac{\partial M}{\partial y}=\dfrac{\partial N}{\partial t}')
    D.P(r'Then there is a function $U(t,y)$ with')
    D.EQ(r'\dfrac{\partial U}{\partial t}=M,\quad \dfrac{\partial U}{\partial y}=N')
    D.P(r'and the general solution is')
    D.EQ(r'U(t,y)=C')
    D.P('**Method:**')
    D.L([r'**Rewrite** as $M\,dt+N\,dy=0$ (everything on the left).',
         r'**Test:** is $M_y=N_t$? ($M_y$ means $\partial M/\partial y$.) If not, go to ' + link('B4', 'b4') + '.',
         r'**Integrate $M$ in $t$:** $U=\int M\,dt+f(y)$. The “constant” is a whole function $f(y)$.',
         r'**Match $N$:** differentiate that $U$ in $y$, set it equal to $N$, solve for $f\prime(y)$, integrate.',
         r'**Answer:** $U(t,y)=C$. Use the condition to find $C$.'],
        ordered=True)
    D.P('**Calculus you need here** (partial derivatives: hold the other letter fixed, like a number):')
    D.T(['Expression', 'Result', 'Note'], [
        [r'$\dfrac{\partial}{\partial t}(t^2y)$', r'$2ty$', r'$y$ is a constant multiplier'],
        [r'$\dfrac{\partial}{\partial y}(t^2y)$', r'$t^2$', r'$t^2$ is a constant multiplier'],
        [r'$\dfrac{\partial}{\partial y}(t-y)$', r'$-1$', r'$t$ is a constant: its derivative is 0'],
        [r'$\int(2ty+3t^2)\,dt$', r'$t^2y+t^3+f(y)$', r'integrate in $t$ with $y$ fixed; anything with only $y$ vanishes under $\partial/\partial t$, so the constant is $f(y)$'],
    ])
    D.CO('info', r'**Bonus (skip-safe): why the test works, and what the answer means.** If $U$ exists, then $M_y=U_{ty}$ and $N_t=U_{yt}$. '
         r'Mixed partial derivatives are equal, so $M_y=N_t$ must hold. '
         r'Along a solution, $dU=U_t\,dt+U_y\,dy=M\,dt+N\,dy=0$: $U$ never changes. So each solution is a **level curve** $U(t,y)=C$ of the surface $z=U(t,y)$.')
    D.GRAPH3D(r'''
    title "Solutions of $3t\,dt+4y\,dy=0$ are level curves of $3t^2+4y^2$"
    x -3 3 label="$t$"
    y -3 3 label="$y$"
    z 0 30 label="$U$"
    view az=-55 el=28
    slider C 1 24 12 step=1 label="$C$"
    surface "3*x^2+4*y^2" label="$U=3t^2+4y^2$"
    plane "C" label="height $C$"
    ''', intro='Slide $C$: the plane cuts the surface along one solution curve (an ellipse), drawn again on the floor.')

    D.EX('W4 · Test, integrate, match · lecture Example 4.1',
         r'Solve $(2ty+3t^2)\,dt+t^2\,dy=0$.',
         [S(r'**Type:** $M\,dt+N\,dy=0$ form, with $M=2ty+3t^2$ and $N=t^2$.'),
          S(r'**Test:** hold $t$ fixed for $M_y$, hold $y$ fixed for $N_t$.', r'M_y=2t=N_t\quad\checkmark'),
          S(r'**Integrate $M$ in $t$** ($y$ fixed).', r'U=t^2y+t^3+f(y)'),
          S(r'**Match $N$:** $U_y$ must equal $t^2$.', r't^2+f\prime(y)=t^2\quad\Rightarrow\quad f\prime(y)=0'),
          S(r'So $f$ is a plain constant, which joins $C$.', r't^2y+t^3=C')],
         r'$t^2y+t^3=C$ (explicitly, $y=\dfrac{C-t^3}{t^2}$).', cites=W4(1, 2))

    P(D, 'W4 · Test, then solve · lecture exercise (a)',
      r'Test $3t\,dt+4y\,dy=0$ for exactness, and if so, solve.',
      [S(r'**Type:** $M\,dt+N\,dy=0$ with $M=3t$, $N=4y$.'),
       S(r'**Test:** $M$ has no $y$, $N$ has no $t$.', r'M_y=0=N_t\quad\checkmark'),
       S(r'**Integrate $M$ in $t$.**', r'U=\tfrac32t^2+f(y)'),
       S(r'**Match $N$:** $f\prime(y)=4y$, so $f=2y^2$.', r'U=\tfrac32t^2+2y^2'),
       S(r'**Answer:** $U=C$; multiply by 2 and rename the constant.', r'3t^2+4y^2=C')],
      r'Exact. $3t^2+4y^2=C$ (ellipses: the graph above). It is also separable.', cites=W4(3))
    P(D, 'W4 · Test before you integrate · lecture exercise (d)',
      r'Is $y\prime=\dfrac{t}{t+y}$ exact?',
      [S(r'**Type:** a slope formula: rewrite it in $M\,dt+N\,dy=0$ form first.', r't\,dt-(t+y)\,dy=0'),
       S(r'**Read** $M=t$ and $N=-(t+y)$.'),
       S(r'**Test.**', r'M_y=0,\qquad N_t=-1'),
       S(r'$0\neq-1$: **not exact**. The next move would be ' + link('B4', 'b4') + r', but neither of its ratios works here: '
         r'$\frac{M_y-N_t}{N}=-\frac{1}{t+y}$ has both letters, and $\frac{N_t-M_y}{M}=-\frac1t$ has no $y$. The lecture stops at “not exact”.')],
      r'Not exact: $M_y=0\neq-1=N_t$.', cites=W4(4))
    P(D, 'W4 · Cross-multiply, then use a condition · lecture exercise (b)',
      r'Solve $y\prime=\dfrac{t-y}{t+y}$, $\;y(0)=1$.',
      [S(r'**Type:** slope formula → cross-multiply and move everything left.', r'(t-y)\,dt-(t+y)\,dy=0'),
       S(r'**Test:** $M=t-y$, $N=-t-y$.', r'M_y=-1=N_t\quad\checkmark'),
       S(r'**Integrate $M$ in $t$.**', r'U=\tfrac12t^2-ty+f(y)'),
       S(r'**Match $N$:** $-t+f\prime(y)=-t-y$, so $f\prime=-y$ and $f=-\frac12y^2$.', r'\tfrac12t^2-ty-\tfrac12y^2=C'),
       S(r'Multiply by 2 (rename the constant).', r't^2-2ty-y^2=C'),
       S(r'**Condition** $y(0)=1$: $\;0-0-1=C$.', r'C=-1')],
      r'$t^2-2ty-y^2=-1$.', diff='intermediate', cites=W4(3))
    P(D, 'W4 · The sign trap · lecture exercise (c)',
      r'Solve $2ty\,y\prime=t^2-y^2$.',
      [S(r'**Type:** write $y\prime=\frac{dy}{dt}$, multiply by $dt$ and move the $dy$ term left: it becomes **negative**.', r'(t^2-y^2)\,dt-2ty\,dy=0'),
       S(r'**Test:** $M=t^2-y^2$, $N=-2ty$.', r'M_y=-2y=N_t\quad\checkmark'),
       S(r'**Integrate $M$ in $t$.**', r'U=\tfrac13t^3-ty^2+f(y)'),
       S(r'**Match $N$:** $-2ty+f\prime(y)=-2ty$, so $f\prime=0$.', r'\tfrac13t^3-ty^2=C'),
       S('Multiply by 3 (rename the constant).', r't^3-3ty^2=C')],
      r'$t^3-3ty^2=C$. With $+2ty\,dy$ (wrong sign) the test gives $-2y\neq2y$ and fails.', diff='intermediate', cites=W4(4))


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
