"""Topic C: does exactly one solution exist? (Week 3 Topic 3, Week 5 Topic 2, Week 6 outcomes)."""
import sympy as sp

from midlib import P, S, TAGS, link, t, y, zero


def build(D):
    W3 = lambda *p: D.cite('W3', *p)
    D.H('Topic C: Does exactly one solution exist?', cites=W3(5))
    TAGS(D, (3, 3), (5, 2))
    D.P(r'Some midterm questions ask **whether** a problem has exactly one solution, or **where** it is guaranteed, without solving anything. '
        'Two theorems answer that: one for first-order equations, one for second-order linear ones.')
    D.P('The answer is always found the same way: write the equation in a standard form, then look for the places where something breaks (division by zero, a log of a negative, a square root of a negative).')

    # ------------------------------------------------------------------ C1
    D.H('C1 · First order: is there exactly one solution through this point?', level=2, cites=W3(5))
    TAGS(D, (3, 3))
    D.P(r'**When:** the question gives $\dfrac{dy}{dt}=F(t,y)$ and a starting point $(t_0,y_0)$, and asks if a unique solution passes through it.')
    D.P('Write the equation with the derivative alone:')
    D.EQ(r'\dfrac{dy}{dt}=F(t,y)')
    D.L([r'$F(t,y)$ = everything on the right side once $\dfrac{dy}{dt}$ is alone',
         r'$\dfrac{\partial F}{\partial y}$ = its **partial derivative** in $y$: differentiate in $y$ while treating $t$ as a constant'])
    D.P('**The theorem** (Spiegel, used in the Week 3 lecture):')
    D.CO('info', r'If $F$ and $\dfrac{\partial F}{\partial y}$ are both continuous (finite, defined) in a region around $(t_0,y_0)$, '
         r'then **exactly one** solution passes through $(t_0,y_0)$.')
    D.L([r'**Conditions hold** → existence and uniqueness are guaranteed (near $t_0$).',
         r'**Conditions fail** → the theorem says **nothing**. There may be no solution, one, or many. The conditions are sufficient, not necessary.'])
    D.P('Mini examples:')
    D.L([r'$y\prime=t^2+3ty$: $F_y=3t$. Both are fine everywhere → unique through **every** point.',
         r'$y\prime=\dfrac{t}{y}$: $F_y=-\dfrac{t}{y^2}$. Both break on the line $y=0$ → guaranteed only at points with $y_0\neq0$.'])
    D.P('**Method:**')
    D.L([r'**Write $F$:** get $\dfrac{dy}{dt}$ alone.',
         r'**Differentiate:** find $\dfrac{\partial F}{\partial y}$, holding $t$ fixed.',
         r'**Find the bad set:** where is $F$ or $\dfrac{\partial F}{\partial y}$ undefined (divide by 0, $\ln$ of $\le0$, $\sqrt{\ }$ of $<0$, $y^{-1/2}$ at $y=0$)?',
         r'**Check the point:** is $(t_0,y_0)$ away from the bad set? Yes → unique solution. No → no conclusion.'],
        ordered=True)
    D.P('**Calculus you need here:**')
    D.T(['$F$', r'$\dfrac{\partial F}{\partial y}$', 'Note'], [
        [r'$t^2+3ty$', r'$3t$', r'$t$ is a constant: $t^2$ disappears'],
        [r'$\dfrac{t}{y}=t\,y^{-1}$', r'$-t\,y^{-2}$', 'power rule in $y$'],
        [r'$\sqrt{y}=y^{1/2}$', r'$\dfrac{1}{2\sqrt y}$', r'undefined at $y=0$'],
        [r'$\dfrac{2t-(\ln t)\,y}{t-3}$', r'$-\dfrac{\ln t}{t-3}$', r'only the $y$ term survives'],
    ])
    D.GRAPH(r'''
    title "$y\prime=\sqrt{y}$: one solution through $(1,4)$, many through $(1,0)$"
    x -1 5 label="$t$"
    y -0.5 6 label="$y$"
    field "sqrt(max(y,0))" density=18
    hline "0" label="$y=0$ is a solution" color=1
    family c 1 3 0.5 "if(x>c,(x-c)^2/4,0)" color=2 label="also solutions through $(1,0)$"
    curve "((x+3)/2)^2" from=-3 label="the only solution through $(1,4)$" color=3
    point "1" "0" color=1
    point "1" "4" color=3
    caption "At $y=0$, $\partial F/\partial y=1/(2\sqrt y)$ is undefined, so the theorem gives no guarantee, and indeed many curves leave $(1,0)$: each stays at 0, then rises as $(t-c)^2/4$. Above the axis everything is smooth and the solution is unique."
    ''')
    D.CO('info', r'**Bonus (skip-safe): why a blown-up $\partial F/\partial y$ allows several solutions.** $\partial F/\partial y$ measures how strongly nearby curves are pushed apart. '
         r'If it stays finite, two solutions that start together can never separate. At $y=0$ for $\sqrt y$ it is infinite, so a curve can “peel off” the axis at any moment.')

    P(D, 'W3 · Same equation, two starting points',
      r'For $\dfrac{dy}{dt}=\sqrt{y}$: (a) does the theorem guarantee a unique solution through $(1,4)$? (b) through $(1,0)$? '
      r'For (b), check that $y=0$ and $y=\dfrac{(t-1)^2}{4}$ (for $t\ge1$) both pass through $(1,0)$ and solve the ODE.',
      [S(r'**Type:** existence and uniqueness, first order. $F=\sqrt y$.'),
       S(r'**Differentiate** in $y$.', r'\dfrac{\partial F}{\partial y}=\dfrac{1}{2\sqrt y}'),
       S(r'**Bad set:** $F$ needs $y\ge0$; $F_y$ is undefined at $y=0$. So the bad set is $y\le0$.'),
       S(r'(a) $(1,4)$ has $y_0=4>0$: both are continuous around it → unique.'),
       S(r'(b) $(1,0)$ lies on $y=0$ → no conclusion from the theorem.'),
       S(r'Check $y=\frac{(t-1)^2}{4}$: $y\prime=\frac{t-1}{2}$ and $\sqrt y=\frac{t-1}{2}$ for $t\ge1$ ✓. And $y=0$: $0=\sqrt0$ ✓. Both equal 0 at $t=1$.')],
      r'(a) Yes, exactly one solution through $(1,4)$. (b) The theorem gives no guarantee, and in fact at least two solutions pass through $(1,0)$.',
      cites=W3(5))
    P(D, 'W3 · Which points are guaranteed?',
      r'For $\dfrac{dy}{dt}=\dfrac{t}{y}$, decide whether the theorem guarantees a unique solution through (a) $(2,1)$, (b) $(0,3)$, (c) $(2,0)$.',
      [S(r'**Type:** existence and uniqueness, first order. $F=\dfrac ty$.'),
       S(r'**Differentiate** in $y$ (power rule).', r'\dfrac{\partial F}{\partial y}=-\dfrac{t}{y^2}'),
       S(r'**Bad set:** both divide by $y$, so the line $y=0$.'),
       S(r'**Check the points:** (a) $y_0=1$ and (b) $y_0=3$ are off the line; (c) $y_0=0$ is on it.')],
      r'(a) Yes. (b) Yes. (c) No guarantee: $F$ itself is undefined at $(2,0)$.', cites=W3(5))
    P(D, 'W3 · A strip, not a point',
      r'For $(t-3)\,y\prime+(\ln t)\,y=2t$, $\;y(1)=2$, find the region containing the starting point where the theorem applies. Do not solve.',
      [S(r'**Type:** existence and uniqueness. **Write $F$:** isolate $y\prime$.', r'F=\dfrac{2t-(\ln t)\,y}{t-3}'),
       S(r'**Differentiate** in $y$; only the $y$ term survives.', r'\dfrac{\partial F}{\partial y}=-\dfrac{\ln t}{t-3}'),
       S(r'**Bad set:** $\ln t$ needs $t>0$; division needs $t\neq3$. Nothing restricts $y$.'),
       S(r'**Check the point:** $t_0=1$ lies between $0$ and $3$.', r'0<t<3,\quad\text{any }y')],
      r'The strip $0<t<3$ (all $y$). The start $(1,2)$ is inside it, so exactly one solution passes through it.',
      diff='intermediate')

    # ------------------------------------------------------------------ C2
    D.H('C2 · Second order linear: interval, zero start, independent solutions', level=2, cites=D.cite('SYL', 4))
    TAGS(D, (5, 2))
    D.P(r'**When:** a second-order **linear** equation with two conditions $y(t_0)$, $y\prime(t_0)$, and the question asks on what interval exactly one solution exists, '
        'or whether two given solutions can build the general solution.')
    D.P(r'First divide by the coefficient of $y\prime\prime$ so it stands alone:')
    D.EQ(r'y\prime\prime+p(t)\,y\prime+q(t)\,y=g(t)')
    D.L([r'$p(t)$ = the coefficient of $y\prime$ (after dividing)',
         r'$q(t)$ = the coefficient of $y$ (after dividing)',
         r'$g(t)$ = the forcing (after dividing)'])
    D.CO('info', r'**The theorem.** If $p$, $q$ and $g$ are continuous on an open interval $I$ containing $t_0$, then for **any** values of $y(t_0)$ and $y\prime(t_0)$ '
         r'there is **exactly one** solution, and it exists on the **whole** interval $I$.')
    D.L([r'The largest such $I$ runs from the nearest “trouble point” on the left of $t_0$ to the nearest on the right.',
         r'Constant coefficients ($ay\prime\prime+by\prime+cy=g$ with continuous $g$): no trouble points, $I$ is the whole real line.'])
    D.P(r'Mini example: $t\,y\prime\prime+y=0$ → divide by $t$: $q=\dfrac1t$, trouble at $t=0$. For $t_0=5$: $I=(0,\infty)$. For $t_0=-2$: $I=(-\infty,0)$.')
    D.P('**Method (interval):**')
    D.L([r'**Divide** by the coefficient of $y\prime\prime$; read $p,q,g$.',
         r'**Trouble points:** where $p$, $q$ or $g$ is undefined (zero denominators, $\ln$ of $\le0$, …).',
         r'**Pick the piece** of the $t$-axis between trouble points that contains $t_0$. Use open ends.'],
        ordered=True)

    D.P(r'**Zero start.** If the equation is linear and **homogeneous** ($g=0$) and both conditions are zero, $y(t_0)=0$ and $y\prime(t_0)=0$, then:')
    D.EQ(r'y(t)\equiv0')
    D.P(r'Reason in one line: $y=0$ obviously solves it and fits both conditions, and the theorem says there is only one solution. No solving needed.')

    D.P(r'**Two solutions → the general solution?** If $y_1$ and $y_2$ solve the same homogeneous linear equation, compute their **Wronskian**:')
    D.EQ(r'W=y_1\,y_2\prime-y_1\prime\,y_2')
    D.L([r'$W\neq0$ → $y_1,y_2$ are **independent**, and $y=c_1y_1+c_2y_2$ is the general solution.',
         r'$W=0$ → one is a multiple of the other; they give only one real constant, so they are **not** enough.'])
    D.P(r'This is why the repeated-root case in ' + link('B5', 'b5') + r' uses $(c_1+c_2t)e^{st}$ and not $c_1e^{st}+c_2e^{st}$.')
    D.CO('info', r'**Bonus (skip-safe): why the Wronskian decides it.** Fitting $c_1y_1+c_2y_2$ to $y(t_0)$ and $y\prime(t_0)$ gives two equations:'
         '\n\n$$\n' r'c_1y_1+c_2y_2=y(t_0),\quad c_1y_1\prime+c_2y_2\prime=y\prime(t_0)' '\n$$\n\n'
         r'That $2\times2$ system has a unique answer exactly when its determinant $y_1y_2\prime-y_1\prime y_2=W$ is not zero. '
         r'$W\neq0$ means every pair of starting values can be matched.')

    P(D, 'W5 · Find the interval; do not solve',
      r'For $(t-1)\,y\prime\prime+y\prime+y=\ln t$, find the largest interval on which the theorem guarantees exactly one solution for (a) $t_0=2$, (b) $t_0=\tfrac12$.',
      [S(r'**Type:** existence and uniqueness, second-order linear. **Divide** by $t-1$.', r'p=\dfrac1{t-1},\qquad q=\dfrac1{t-1},\qquad g=\dfrac{\ln t}{t-1}'),
       S(r'**Trouble points:** $\ln t$ needs $t>0$; the denominator needs $t\neq1$. So the pieces are $(0,1)$ and $(1,\infty)$.'),
       S(r'**Pick the piece:** $t_0=2$ is in $(1,\infty)$; $t_0=\tfrac12$ is in $(0,1)$.')],
      r'(a) $(1,\infty)$. (b) $(0,1)$.', diff='intermediate')
    P(D, 'W5 · Which pair gives the general solution?',
      r'Both pairs solve $y\prime\prime+4y\prime+4y=0$: (a) $e^{-2t}$ and $3e^{-2t}$; (b) $e^{-2t}$ and $te^{-2t}$. Compute each Wronskian and decide which pair gives the general solution.',
      [S(r'**Type:** independence: compute $W=y_1y_2\prime-y_1\prime y_2$.'),
       S(r'(a) $y_2\prime=-6e^{-2t}$, $y_1\prime=-2e^{-2t}$.', r'W=e^{-2t}(-6e^{-2t})-(-2e^{-2t})(3e^{-2t})=0'),
       S(r'(b) Product rule: $(te^{-2t})\prime=(1-2t)e^{-2t}$.', r'W=e^{-2t}(1-2t)e^{-2t}-(-2e^{-2t})\,te^{-2t}=e^{-4t}'),
       S(r'$e^{-4t}$ is never zero, so pair (b) is independent.')],
      r'(a) $W=0$: not enough (they are multiples). (b) $W=e^{-4t}\neq0$: general solution $y=(c_1+c_2t)e^{-2t}$.',
      diff='intermediate')
    P(D, 'W5 + W6 · The answer without solving',
      r'Solve $y\prime\prime+t\,y\prime+e^{t}\,y=0$, $\;y(0)=0$, $\;y\prime(0)=0$.',
      [S(r'**Type:** looks unsolvable with our methods ($t$ and $e^t$ coefficients), but it is linear, homogeneous, with a **zero start**.'),
       S(r'**Interval:** $p=t$, $q=e^t$, $g=0$ are continuous everywhere, so exactly one solution exists on the whole real line.'),
       S(r'**Guess the obvious one:** $y=0$ gives $0+0+0=0$ ✓, and $y(0)=0$, $y\prime(0)=0$ ✓.'),
       S(r'By uniqueness, that is **the** solution.')],
      r'$y(t)\equiv0$ for all $t$.', diff='advanced')


def verify():
    s = sp.symbols('s', positive=True)  # t - 1 >= 0 for the peeled-off solution, t + 3 > 0 for the upper one
    sol = s ** 2 / 4  # y = (t-1)^2/4 with s = t - 1
    zero(sp.diff(sol, s) - sp.sqrt(sol))
    up = ((s) / 2) ** 2  # y = ((t+3)/2)^2 with s = t + 3
    zero(sp.diff(up, s) - sp.sqrt(up))
    assert up.subs(s, 4) == 4  # passes through (1, 4)
    zero(sp.diff(sp.sqrt(y), y) - 1 / (2 * sp.sqrt(y)))
    zero(sp.diff(t / y, y) + t / y ** 2)
    zero(sp.diff(t ** 2 + 3 * t * y, y) - 3 * t)
    zero(sp.diff((2 * t - sp.log(t) * y) / (t - 3), y) + sp.log(t) / (t - 3))
    f, g = sp.exp(-2 * t), 3 * sp.exp(-2 * t)
    zero(f * sp.diff(g, t) - sp.diff(f, t) * g)
    g = t * sp.exp(-2 * t)
    zero(f * sp.diff(g, t) - sp.diff(f, t) * g - sp.exp(-4 * t))
    for sol2 in (sp.exp(-2 * t), t * sp.exp(-2 * t)):
        zero(sp.diff(sol2, t, 2) + 4 * sp.diff(sol2, t) + 4 * sol2)
