"""Topic B opening: name the equation, pick the method (Week 2 classification), what a general solution is."""
import sympy as sp

from midlib import P, S, TAGS, link, second, t, y, zero


def build(D):
    W2 = lambda *p: D.cite('W2', *p)
    D.H('Topic B: Find the general solution', cites=W2(2, 3))
    TAGS(D, (2, 1), (2, 2))
    D.P(r'This is the core of the midterm. You get an ODE (ordinary differential equation) and you have to find $y(t)$.')
    D.P(r'There are seven methods, B1–B7. Which one you use depends only on **what the equation looks like**. '
        'So the first move is always to name the equation.')

    D.P('**Step 1: name it.** Ask these five questions:')
    D.T(['Label', 'Question', 'Yes, like…', 'No, like…'], [
        ['**Order**', 'What is the highest derivative?', r'$y\prime\prime+y=0$: 2nd', '—'],
        ['**Linear**', r'Is every $y$, $y\prime$, $y\prime\prime$ to the power 1, on its own? (No $y^2$, $yy\prime$, $\sin y$. $t$ can be anywhere.)',
         r'$ty\prime\prime+y=0$', r'$y\prime=y^2$'],
        ['**Homogeneous**', r'Move every $y$ term to the left. Is the right side $0$?', r'$y\prime\prime+4y=0$', r'$y\prime\prime+4y=8$'],
        ['**Constant coefficients**', r'Are the things in front of $y$, $y\prime$, $y\prime\prime$ just numbers?', r'$y\prime\prime+3y\prime+2y=0$', r'$ty\prime\prime+y=0$'],
        ['**Autonomous**', r'Is there no $t$ anywhere?', r'$y\prime=3y$', r'$y\prime=t-y$'],
    ], cites=W2(2, 3))

    D.P('**Step 2: pick the method.** Look at the **order** first. 1st-order and 2nd-order equations use completely different methods.')

    # ---------------------------------------------------------------- 1st order
    D.P(r'**1st order** (the highest derivative is $y\prime$). Check these in order and stop at the first one that fits:')
    D.T(['Check', 'Method', 'Go to'], [
        ['1. Can you split it into a $t$-part times a $y$-part?', 'separate the variables', link('B1', 'b1')],
        ['2. Is it linear?', 'integrating factor', link('B2', 'b2')],
        ['3. Neither? Write it as $M\\,dt+N\\,dy=0$. Is it exact?', 'exact equation', link('B3', 'b3')],
        ['4. Not exact?', 'make it exact first', link('B4', 'b4')],
    ])

    D.P(r'**1. Separable** → ' + link('B1', 'b1') + r'. The right side is a $t$-part **times** a $y$-part:')
    D.EQ(r'\dfrac{dy}{dt}=g(t)\,h(y)')
    D.L([r'**Example:** $y\prime=t^2y$. Here $g=t^2$ and $h=y$.',
         r'**Method:** get all the $y$’s on one side and all the $t$’s on the other, then integrate both sides: $\dfrac{dy}{y}=t^2\,dt$.',
         r'**Autonomous equations are always separable.** $y\prime=3y$ has no $t$ at all, so you can always write $\dfrac{dy}{3y}=dt$.'])

    D.P(r'**2. Linear** → ' + link('B2', 'b2') + r'. You can’t split it, but $y$ and $y\prime$ only appear to the power 1:')
    D.EQ(r'y\prime+a(t)\,y=f(t)')
    D.L([r'**Example:** $y\prime+y=t$. Here $a=1$ and $f=t$.',
         r'**Why not B1?** $y\prime=t-y$ is a $t$ **plus** a $y$, and a sum can’t be split into a product.',
         r'**Method:** multiply everything by $\mu=e^{\int a\,dt}$ (here $e^t$). The left side becomes one derivative, $(e^ty)\prime$, so you can integrate.'])

    D.P(r'**3. Exact** → ' + link('B3', 'b3') + r'. Not separable, not linear. Write it with $dt$ and $dy$:')
    D.EQ(r'M\,dt+N\,dy=0')
    D.L([r'**Example:** $(t-y)\,dt-(t+y)\,dy=0$. Here $M=t-y$ and $N=-(t+y)$.',
         r'**Test:** take $\dfrac{\partial M}{\partial y}=-1$ and $\dfrac{\partial N}{\partial t}=-1$. They match, so it’s exact.',
         r'**Method:** find one function $U(t,y)$ whose $t$-derivative is $M$ and whose $y$-derivative is $N$. The answer is $U=C$.'])

    D.P(r'**4. Not exact** → ' + link('B4', 'b4') + '. Same form, but the test fails:')
    D.L([r'**Example:** $y\,dt+(3+3t-y)\,dy=0$. Here $\dfrac{\partial M}{\partial y}=1$ but $\dfrac{\partial N}{\partial t}=3$. No match.',
         r'**Method:** multiply the whole equation by a factor that fixes the mismatch (here $y^2$). Now it passes the test, so finish it like B3.'])

    # ---------------------------------------------------------------- 2nd order
    D.P(r'**2nd order** (the highest derivative is $y\prime\prime$). In Weeks 1–6 these are all **linear**, so you only ask two questions:')
    D.L([r'Are the things in front of $y\prime\prime$, $y\prime$, $y$ just **numbers**?',
         r'Is the **right side $0$**?'], ordered=True)
    D.T(['In front of $y$', r'Right side $0$', r'Right side $g(t)$'], [
        [r'**Numbers in front**', link('B5', 'b5') + ' characteristic equation', link('B6', 'b6') + ' undetermined coefficients'],
        [r'**$t$ in front**', link('B7', 'b7') + ' reduction of order', 'not on the midterm'],
    ])

    D.P(r'**Numbers in front, right side 0** → ' + link('B5', 'b5') + '.')
    D.EQ(r'a\,y\prime\prime+b\,y\prime+c\,y=0')
    D.L([r'**Example:** $y\prime\prime+3y\prime+2y=0$.',
         r'**Method:** guess $y=e^{st}$. That turns the ODE into $s^2+3s+2=0$, so $s=-1$ or $s=-2$, and $y=Ae^{-t}+Be^{-2t}$.',
         r'**Why it works:** every derivative of $e^{st}$ is still $e^{st}$ times a number. So $e^{st}$ cancels and you’re left with a plain quadratic in $s$.'])

    D.P(r'**Numbers in front, right side not 0** → ' + link('B6', 'b6') + '.')
    D.EQ(r'a\,y\prime\prime+b\,y\prime+c\,y=g(t)')
    D.L([r'**Example:** $y\prime\prime+3y\prime+2y=4$.',
         r'**Method:** first solve the version with $0$ on the right (B5): $y_c=c_1e^{-t}+c_2e^{-2t}$. '
         r'Then guess a $y_p$ that looks like $g(t)$. Here $g=4$ is a constant, so guess $y_p=A$: $2A=4$, $A=2$.',
         r'**Answer:** add them. $y=c_1e^{-t}+c_2e^{-2t}+2$.',
         r'**Why two pieces?** $y_c$ always gives $0$ on the left side. You need one extra piece, $y_p$, that gives the $4$.'])

    D.P(r'**$t$ in front, right side 0** → ' + link('B7', 'b7') + '.')
    D.EQ(r'y\prime\prime+p(t)\,y\prime+q(t)\,y=0')
    D.L([r'**Example:** $y\prime\prime-t\,y\prime+y=0$, and the question gives you one solution, $y_1=t$.',
         r'**Why not B5?** With $t$ in front, the $e^{st}$ guess no longer cancels. So you need that given $y_1$.',
         r'**Method:** guess $y=y_1\,v=t\,v$. After substituting, you get $t\,v\prime\prime+(2-t^2)\,v\prime=0$. '
         r'Set $z=v\prime$ and it’s a 1st-order equation (separable, B1).'])

    D.CO('tip', r'**Where does “autonomous” matter?** Only for 1st order: no $t$ means separable. For 2nd order, ignore it.')

    D.P('**Step 3: fix the constants.** Every method gives a **general solution**: a formula with unknown constants in it.')
    D.L([r'1st order → one constant, $C$. One condition, like $y(1)=2$, pins it down.',
         r'2nd order → two constants, $c_1$ and $c_2$. You need two conditions, usually $y(0)$ and $y\prime(0)$.',
         r'A problem that gives you conditions is called an **initial value problem** (IVP). Plug the conditions into the general solution and solve for the constants.'])

    D.P(r'**Checking a solution** (Week 2 asks this). Plug $y$ and its derivatives into the ODE. If both sides match for **every** $t$, it’s a solution.')
    D.P(r'Example: is $y=e^{-2t}$ a solution of $y\prime+2y=0$? $\;-2e^{-2t}+2e^{-2t}=0$ ✓. Yes.')

    P(D, 'W2 · Name it, then route it · lecture Example 2.1 and others',
      'For each equation, give its order, and say whether it is linear, homogeneous, constant-coefficient and autonomous. Then say which method (B1–B7) solves it.\n\n'
      r'(a) $t^3y\prime\prime+e^ty\prime+y=0$' '\n\n'
      r'(b) $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$' '\n\n'
      r'(c) $y\prime\prime+2y\prime+5y=10$' '\n\n'
      r'(d) $\dfrac{di}{dt}+5i=50$' '\n\n'
      r'(e) $(t-y)\,dt-(t+y)\,dy=0$',
      [S(r'(a) Highest derivative is $y\prime\prime$, so 2nd order. Every $y$ is to the power 1, so linear. Right side is $0$, so homogeneous. '
         r'But $t^3$ and $e^t$ are in front, not numbers. That’s the “$t$ in front” case → ' + link('B7', 'b7') + ' (once they give you one solution).'),
       S(r'(b) $y^2$ is not power 1, so nonlinear. But it splits: $\frac{1}{t^3}\cdot y^2$ is a $t$-part times a $y$-part → ' + link('B1', 'b1') + '.'),
       S(r'(c) 2nd order, linear, numbers in front. Right side is $10$, not $0$ → ' + link('B6', 'b6') + '.'),
       S(r'(d) 1st order, linear ($a=5$, $f=50$) → ' + link('B2', 'b2') + r'. It has no $t$, so it’s also autonomous, and B1 works too: $\frac{di}{50-5i}=dt$.'),
       S(r'(e) Solve for $y\prime$: $y\prime=\frac{t-y}{t+y}$. $y$ is in a denominator, so nonlinear, and it won’t split. '
         r'Test $M=t-y$, $N=-(t+y)$: both partials are $-1$ → exact, ' + link('B3', 'b3') + '.')],
      r'(a) B7. (b) B1. (c) B6. (d) B2 (or B1). (e) B3.',
      cites=W2(3))
    P(D, 'W2 · Check, then pick the member that fits',
      r'Which of $y=t^2$, $\;y=t^2+1$, $\;y=5t^2$ solve $ty\prime-2y=0$? Which one also satisfies $y(1)=5$?',
      [S(r'**Type:** checking solutions. Plug each one in and see if you get $0$.'),
       S(r'$y=t^2$: $y\prime=2t$.', r't(2t)-2t^2=0\ \checkmark'),
       S(r'$y=t^2+1$: $y\prime=2t$.', r't(2t)-2(t^2+1)=-2\neq0\ \times'),
       S(r'$y=5t^2$: $y\prime=10t$.', r't(10t)-2(5t^2)=0\ \checkmark'),
       S(r'**Condition:** at $t=1$, $t^2=1$ and $5t^2=5$. Only $5t^2$ gives $5$.')],
      r'$t^2$ and $5t^2$ are solutions (both are $Ct^2$); $t^2+1$ is not. Only $y=5t^2$ satisfies $y(1)=5$.')


def verify():
    for sol, ok in ((t ** 2, True), (t ** 2 + 1, False), (5 * t ** 2, True)):
        assert (sp.simplify(t * sp.diff(sol, t) - 2 * sol) == 0) == ok
    zero(sp.diff(sp.exp(-2 * t), t) + 2 * sp.exp(-2 * t))
    # Step 2 cards
    zero(sp.diff(t - y, y) - sp.diff(-(t + y), t))                       # (t-y)dt-(t+y)dy is exact
    assert sp.diff(y, y) != sp.diff(3 + 3 * t - y, t)                    # y dt+(3+3t-y)dy is not
    zero(sp.diff(y ** 2 * y, y) - sp.diff(y ** 2 * (3 + 3 * t - y), t))  # ... until multiplied by y^2
    c1, c2 = sp.symbols('c1 c2')
    assert set(sp.solve(sp.Symbol('r') ** 2 + 3 * sp.Symbol('r') + 2)) == {-1, -2}
    second(c1 * sp.exp(-t) + c2 * sp.exp(-2 * t), 1, 3, 2)
    second(c1 * sp.exp(-t) + c2 * sp.exp(-2 * t) + 2, 1, 3, 2, rhs=4)
    v = sp.Function('v')(t)
    yy = t * v
    lhs = sp.diff(yy, t, 2) - t * sp.diff(yy, t) + yy
    zero(sp.expand(lhs - (t * sp.diff(v, t, 2) + (2 - t ** 2) * sp.diff(v, t))))
