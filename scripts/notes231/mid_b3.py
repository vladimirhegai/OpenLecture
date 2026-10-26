"""B3: exact equations (Week 4)."""
import sympy as sp

from midlib import P, S, TAGS, implicit, link, t, y, zero


def build(D):
    W4 = lambda *p: D.cite('W4', *p)
    D.H('B3 · Exact equations', level=2, cites=W4(1, 2, 3, 4))
    TAGS(D, (4, 1), (4, 2))
    D.P(r'**What if it’s neither separable nor linear?** Take $y\prime=\dfrac{t-y}{t+y}$. It won’t split into '
        r'($t$-part)×($y$-part), and $y$ sits in the bottom, so ' + link('B1', 'b1') + ' and ' + link('B2', 'b2') + ' both fail.')
    D.P(r'Some of these equations are **exact**. Then the answer is one formula in $t$ and $y$ set equal to a constant, '
        r'$U(t,y)=C$, and you find $U$ by integrating.')
    D.P(r'**First, write it in $dt$, $dy$ form,** with everything on the left:')
    D.EQ(r'M(t,y)\,dt+N(t,y)\,dy=0')
    D.L([r'$M$ = everything multiplying $dt$, **sign included**',
         r'$N$ = everything multiplying $dy$, **sign included**'])
    D.P('Examples:')
    D.L([r'$3t\,dt+4y\,dy=0$ → already in form. $M=3t$, $N=4y$.',
         r'$y\prime=\dfrac{t-y}{t+y}$ → cross-multiply: $(t+y)\,dy=(t-y)\,dt$. Move it all left: $(t-y)\,dt-(t+y)\,dy=0$. '
         r'So $M=t-y$, $N=-(t+y)$.',
         r'$2ty\,y\prime=t^2-y^2$ → $2ty\,dy=(t^2-y^2)\,dt$ → $(t^2-y^2)\,dt-2ty\,dy=0$. So $M=t^2-y^2$, $N=-2ty$.'])
    D.CO('warning', r'Moving the $dy$ term to the other side of the $=$ flips its sign. In $y\prime=\frac{t-y}{t+y}$, $N$ is $-(t+y)$, not $t+y$. '
         r'One wrong sign and the test below fails.')

    D.P(r'**Is it exact? Do the cross test.** Differentiate $M$ in $y$, and $N$ in $t$. If you get the same thing, it’s **exact**:')
    D.EQ(r'\dfrac{\partial M}{\partial y}=\dfrac{\partial N}{\partial t}')
    D.L([r'$M_y$ = derivative of $M$ in $y$, treating $t$ like a number',
         r'$N_t$ = derivative of $N$ in $t$, treating $y$ like a number'])
    D.P(r'Example: $(2ty+3t^2)\,dt+t^2\,dy=0$ has $M_y=2t$ and $N_t=2t$. Same, so it’s exact.')
    D.P(r'**If it’s exact, find $U$.** $U$ is the function whose two partial derivatives are $M$ and $N$:')
    D.EQ(r'\dfrac{\partial U}{\partial t}=M,\quad \dfrac{\partial U}{\partial y}=N')
    D.P('and the general solution is')
    D.EQ(r'U(t,y)=C')
    D.P(r'Example: for the equation above, $U=t^2y+t^3$. Check: $U_t=2ty+3t^2=M$ and $U_y=t^2=N$. So the answer is $t^2y+t^3=C$.')
    D.P(r'Why $U=C$: $M\,dt+N\,dy$ is the small change in $U$. The equation sets that change to 0, so $U$ stays at one constant value.')
    D.P('**Method:**')
    D.L([r'**Rewrite:** everything on the left, $M\,dt+N\,dy=0$. Read $M$ and $N$ with their signs.',
         r'**Test:** is $M_y=N_t$? If not, it isn’t exact: go to ' + link('B4', 'b4') + '.',
         r'**Integrate $M$ in $t$**, treating $y$ like a number: $U=\int M\,dt+f(y)$. '
         r'The “$+C$” becomes $f(y)$, because anything with only $y$ in it vanishes when you differentiate in $t$.',
         r'**Match $N$:** differentiate this $U$ in $y$ and set it equal to $N$. The $t$ terms cancel, leaving $f\prime(y)$. Integrate it.',
         r'**Answer:** write $U(t,y)=C$. If you’re given a starting value, plug it in to find $C$.'],
        ordered=True)
    D.P(r'**Calculus you need here: partial derivatives.** Differentiate in one letter and treat the other like a plain number:')
    D.T(['Expression', 'Result', 'Why'], [
        [r'$\dfrac{\partial}{\partial t}(t^2y)$', r'$2ty$', r'$y$ acts like a number'],
        [r'$\dfrac{\partial}{\partial y}(t^2y)$', r'$t^2$', r'$t^2$ acts like a number'],
        [r'$\dfrac{\partial}{\partial y}(t-y)$', r'$-1$', r'$t$ is a constant, so it gives 0'],
        [r'$\int(2ty+3t^2)\,dt$', r'$t^2y+t^3+f(y)$', r'$y$ acts like a number; the constant is $f(y)$'],
    ])
    D.CO('info', r'**Bonus (skip-safe): why the cross test works.** If $U$ exists, then $M=U_t$ and $N=U_y$. '
         r'So $M_y$ is $U$ differentiated in $t$ then $y$, and $N_t$ is $U$ differentiated in $y$ then $t$. '
         r'The order doesn’t change the result, so the two must match. '
         r'The picture: each solution is a **level curve** $U(t,y)=C$ of the surface $z=U(t,y)$, like a contour line on a map.')
    D.GRAPH3D(r'''
    title "Solutions of $3t\,dt+4y\,dy=0$ are level curves of $3t^2+4y^2$"
    x -3 3 label="$t$"
    y -3 3 label="$y$"
    z 0 30 label="$U$"
    view az=-55 el=28
    slider C 1 24 12 step=1 label="$C$"
    surface "3*x^2+4*y^2" label="$U=3t^2+4y^2$"
    plane "C" label="height $C$"
    ''', intro='Slide $C$: the plane at height $C$ cuts the surface along one solution curve (an ellipse). The same curve is drawn on the floor.')

    D.EX('W4 · Test, integrate, match · lecture Example 4.1',
         r'Solve $(2ty+3t^2)\,dt+t^2\,dy=0$.',
         [S(r'**Type:** already in $M\,dt+N\,dy=0$ form. $M=2ty+3t^2$, $N=t^2$.'),
          S(r'**Test:** for $M_y$ treat $t$ as a number; for $N_t$ treat $y$ as a number. They match.', r'M_y=2t=N_t\quad\checkmark'),
          S(r'**Integrate $M$ in $t$** ($y$ is a number). The constant is $f(y)$.', r'U=t^2y+t^3+f(y)'),
          S(r'**Match $N$:** $U_y$ must equal $N=t^2$.', r't^2+f\prime(y)=t^2\quad\Rightarrow\quad f\prime(y)=0'),
          S(r'**Answer:** $f$ is just a number, so it merges into $C$.', r't^2y+t^3=C')],
         r'$t^2y+t^3=C$ (solved for $y$: $y=\dfrac{C-t^3}{t^2}$).', cites=W4(1, 2))

    P(D, 'W4 · Test, then solve · lecture exercise (a)',
      r'Test $3t\,dt+4y\,dy=0$ for exactness, and if so, solve.',
      [S(r'**Type:** already in form. $M=3t$, $N=4y$.'),
       S(r'**Test:** $M$ has no $y$ and $N$ has no $t$, so both derivatives are 0.', r'M_y=0=N_t\quad\checkmark'),
       S(r'**Integrate $M$ in $t$.**', r'U=\tfrac32t^2+f(y)'),
       S(r'**Match $N$:** $U_y=f\prime(y)$ must equal $4y$, so $f=2y^2$.', r'U=\tfrac32t^2+2y^2'),
       S(r'**Answer:** set $U=C$. Multiply by 2 to clear the fraction ($2C$ is still just a constant: call it $C$).', r'3t^2+4y^2=C')],
      r'Exact. $3t^2+4y^2=C$: ellipses, the curves in the graph above. (It’s also separable: $4y\,dy=-3t\,dt$.)', cites=W4(3))
    P(D, 'W4 · Test before you integrate · lecture exercise (d)',
      r'Is $y\prime=\dfrac{t}{t+y}$ exact?',
      [S(r'**Type:** a slope formula. Cross-multiply, $(t+y)\,dy=t\,dt$, then move everything left.', r't\,dt-(t+y)\,dy=0'),
       S(r'**Read** $M=t$ and $N=-(t+y)$. The minus came from moving the $dy$ term left.'),
       S(r'**Test:** $M$ has no $y$, so $M_y=0$. But $N_t=-1$.', r'M_y=0,\qquad N_t=-1'),
       S(r'**Answer:** $0\neq-1$, so it’s **not exact**. Next you’d try ' + link('B4', 'b4') + r', but neither ratio there works: '
         r'the first still has both letters, the second has no $y$. The lecture stops at “not exact”.',
         r'\frac{M_y-N_t}{N}=-\frac{1}{t+y},\quad \frac{N_t-M_y}{M}=-\frac1t')],
      r'Not exact: $M_y=0\neq-1=N_t$.', cites=W4(4))
    P(D, 'W4 · Cross-multiply, then use a condition · lecture exercise (b)',
      r'Solve $y\prime=\dfrac{t-y}{t+y}$, $\;y(0)=1$.',
      [S(r'**Type:** a slope formula. Cross-multiply, $(t+y)\,dy=(t-y)\,dt$, and move everything left.', r'(t-y)\,dt-(t+y)\,dy=0'),
       S(r'**Test:** $M=t-y$, $N=-t-y$.', r'M_y=-1=N_t\quad\checkmark'),
       S(r'**Integrate $M$ in $t$.**', r'U=\tfrac12t^2-ty+f(y)'),
       S(r'**Match $N$:** $U_y=-t+f\prime(y)$ must equal $-t-y$. So $f\prime=-y$ and $f=-\frac12y^2$.', r'\tfrac12t^2-ty-\tfrac12y^2=C'),
       S(r'Multiply by 2 to clear the fractions (call $2C$ just $C$ again).', r't^2-2ty-y^2=C'),
       S(r'**Condition** $y(0)=1$: plug in $t=0$, $y=1$: $\;0-0-1=C$.', r'C=-1')],
      r'$t^2-2ty-y^2=-1$.', diff='intermediate', cites=W4(3))
    P(D, 'W4 · The sign trap · lecture exercise (c)',
      r'Solve $2ty\,y\prime=t^2-y^2$.',
      [S(r'**Type:** write $y\prime=\frac{dy}{dt}$ and multiply by $dt$: $2ty\,dy=(t^2-y^2)\,dt$. Moving $2ty\,dy$ left makes it **negative**.', r'(t^2-y^2)\,dt-2ty\,dy=0'),
       S(r'**Test:** $M=t^2-y^2$, $N=-2ty$.', r'M_y=-2y=N_t\quad\checkmark'),
       S(r'**Integrate $M$ in $t$.**', r'U=\tfrac13t^3-ty^2+f(y)'),
       S(r'**Match $N$:** $U_y=-2ty+f\prime(y)$ must equal $-2ty$, so $f\prime=0$.', r'\tfrac13t^3-ty^2=C'),
       S(r'Multiply by 3 to clear the fraction (call $3C$ just $C$ again).', r't^3-3ty^2=C')],
      r'$t^3-3ty^2=C$. If you keep $+2ty\,dy$ (wrong sign), the test gives $-2y\neq2y$ and fails.', diff='intermediate', cites=W4(4))


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
