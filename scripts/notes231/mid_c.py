"""Topic C: does exactly one solution exist? (Week 3 Topic 3, Week 5 Topic 2, Week 6 outcomes)."""
import sympy as sp

from midlib import P, S, TAGS, link, t, y, zero


def build(D):
    W3 = lambda *p: D.cite('W3', *p)
    D.H('Topic C: Does exactly one solution exist?', cites=W3(5))
    TAGS(D, (3, 3), (5, 2))
    D.P(r'**Can you answer without solving?** Some questions ask “is there exactly one solution?” or “on what interval is one guaranteed?”. '
        'You don’t solve the ODE. You check a theorem instead:')
    D.L([r'**First order,** like $y\prime=\dfrac ty$ → ' + link('C1', 'c1') + '.',
         r'**Second-order linear,** like $t\,y\prime\prime+y=0$ → ' + link('C2', 'c2') + '.'])
    D.P('Both checks work the same way. Write the equation in a standard form, then look for the spots where something breaks:')
    D.L([r'**Division by zero:** $\dfrac ty$ breaks at $y=0$.',
         r'**$\ln$ of zero or a negative:** $\ln t$ breaks at $t\le0$.',
         r'**Square root of a negative:** $\sqrt y$ breaks at $y<0$.'])

    # ------------------------------------------------------------------ C1
    D.H('C1 · First order: is there exactly one solution through this point?', level=2, cites=W3(5))
    TAGS(D, (3, 3))
    D.P(r'**When:** you get $\dfrac{dy}{dt}=F(t,y)$ and a starting point $(t_0,y_0)$. The question asks if exactly one solution goes through that point.')
    D.P('First get the derivative alone on the left:')
    D.EQ(r'\dfrac{dy}{dt}=F(t,y)')
    D.L([r'$F(t,y)$ = everything on the right side',
         r'$\dfrac{\partial F}{\partial y}$ (or $F_y$) = the **partial derivative** in $y$: differentiate in $y$ and treat $t$ like a number. '
         r'Example: $F=y^2+t$ gives $F_y=2y$ (the $t$ is a constant, so it disappears).'])
    D.P('**The theorem** (Spiegel, used in the Week 3 lecture):')
    D.CO('info', r'If $F$ and $\dfrac{\partial F}{\partial y}$ are both continuous (no blow-ups, no gaps) near $(t_0,y_0)$, '
         r'then **exactly one** solution passes through $(t_0,y_0)$.')
    D.P('So there are two outcomes:')
    D.L([r'**Both are fine** → yes, exactly one solution (at least for $t$ near $t_0$).',
         r'**One breaks** → the theorem says **nothing**. There could be no solution, one, or many. A fail means “don’t know”, not “no”.'])
    D.P(r'Why $F_y$ matters: it says how fast the slope changes as you move up or down. If it blows up, solutions can split apart (see the graph below).')
    D.P('Mini examples:')
    D.L([r'$y\prime=t^2+3ty$: $F_y=3t$. Both are fine everywhere → exactly one solution through **every** point.',
         r'$y\prime=\dfrac{t}{y}$: $F_y=-\dfrac{t}{y^2}$. Both break on the line $y=0$ → guaranteed only at points with $y_0\neq0$.'])
    D.P('**Method:**')
    D.L([r'**Write $F$:** get $\dfrac{dy}{dt}$ alone.',
         r'**Differentiate:** find $\dfrac{\partial F}{\partial y}$, treating $t$ as a number.',
         r'**Find the bad set:** where does $F$ or $\dfrac{\partial F}{\partial y}$ break? Look for a 0 in a denominator, $\ln$ of $\le0$, $\sqrt{\ }$ of $<0$. '
         r'Example: $y^{-1/2}=\dfrac{1}{\sqrt y}$ breaks at $y=0$.',
         r'**Check the point:** is $(t_0,y_0)$ away from the bad set? Yes → exactly one solution. No → no conclusion.'],
        ordered=True)
    D.P('**Calculus you need here:**')
    D.T(['$F$', r'$\dfrac{\partial F}{\partial y}$', 'Note'], [
        [r'$t^2+3ty$', r'$3t$', r'$t$ is a number here, so $t^2$ disappears'],
        [r'$\dfrac{t}{y}=t\,y^{-1}$', r'$-t\,y^{-2}$', 'power rule in $y$'],
        [r'$\sqrt{y}=y^{1/2}$', r'$\dfrac{1}{2\sqrt y}$', r'breaks at $y=0$'],
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
    caption "At $y=0$, $\partial F/\partial y=1/(2\sqrt y)$ blows up, so the theorem gives no guarantee. And in fact many curves leave $(1,0)$: each sits at 0 for a while, then rises as $(t-c)^2/4$. Above the axis nothing breaks, and only one curve goes through each point."
    ''')
    D.CO('info', r'**Bonus (skip-safe): why a blown-up $\partial F/\partial y$ allows several solutions.** $\partial F/\partial y$ says how much the slope changes when you move a little up or down. '
         r'If it stays finite, two solutions that start at the same point can never drift apart. For $\sqrt y$ it is infinite at $y=0$, so a curve can sit on the axis and then “peel off” at any moment.')

    P(D, 'W3 · Same equation, two starting points',
      r'For $\dfrac{dy}{dt}=\sqrt{y}$: (a) does the theorem guarantee a unique solution through $(1,4)$? (b) through $(1,0)$? '
      r'For (b), check that $y=0$ and $y=\dfrac{(t-1)^2}{4}$ (for $t\ge1$) both pass through $(1,0)$ and solve the ODE.',
      [S(r'**Type:** existence and uniqueness, first order. $F=\sqrt y$.'),
       S(r'**Differentiate** in $y$.', r'\dfrac{\partial F}{\partial y}=\dfrac{1}{2\sqrt y}'),
       S(r'**Bad set:** $F$ needs $y\ge0$, and $F_y$ breaks at $y=0$. So the bad set is $y\le0$.'),
       S(r'**Check (a):** $(1,4)$ has $y_0=4>0$, so both are fine around it → unique.'),
       S(r'**Check (b):** $(1,0)$ sits on $y=0$, in the bad set → the theorem tells you nothing.'),
       S(r'**Two solutions:** for $y=\frac{(t-1)^2}{4}$, $y\prime=\frac{t-1}{2}$ and $\sqrt y=\frac{t-1}{2}$ when $t\ge1$ ✓. For $y=0$, $0=\sqrt0$ ✓. Both equal 0 at $t=1$.')],
      r'(a) Yes, exactly one solution through $(1,4)$. (b) The theorem gives no guarantee, and in fact at least two solutions pass through $(1,0)$.',
      cites=W3(5))
    P(D, 'W3 · Which points are guaranteed?',
      r'For $\dfrac{dy}{dt}=\dfrac{t}{y}$, decide whether the theorem guarantees a unique solution through (a) $(2,1)$, (b) $(0,3)$, (c) $(2,0)$.',
      [S(r'**Type:** existence and uniqueness, first order. $F=\dfrac ty$.'),
       S(r'**Differentiate** in $y$ (power rule).', r'\dfrac{\partial F}{\partial y}=-\dfrac{t}{y^2}'),
       S(r'**Bad set:** both divide by $y$, so the line $y=0$.'),
       S(r'**Check the points:** (a) $y_0=1$ and (b) $y_0=3$ are off the line. (c) $y_0=0$ is on it.')],
      r'(a) Yes. (b) Yes. (c) No guarantee: $F$ itself is undefined at $(2,0)$.', cites=W3(5))
    P(D, 'W3 · A strip, not a point',
      r'For $(t-3)\,y\prime+(\ln t)\,y=2t$, $\;y(1)=2$, find the region containing the starting point where the theorem applies. Do not solve.',
      [S(r'**Type:** existence and uniqueness. **Write $F$:** get $y\prime$ alone.', r'F=\dfrac{2t-(\ln t)\,y}{t-3}'),
       S(r'**Differentiate** in $y$. Only the $y$ term survives.', r'\dfrac{\partial F}{\partial y}=-\dfrac{\ln t}{t-3}'),
       S(r'**Bad set:** $\ln t$ needs $t>0$, and the denominator needs $t\neq3$. Nothing limits $y$.'),
       S(r'**Check the point:** $t_0=1$ lies between $0$ and $3$.', r'0<t<3,\quad\text{any }y')],
      r'The strip $0<t<3$ (all $y$). The start $(1,2)$ is inside it, so exactly one solution passes through it.',
      diff='intermediate')

    # ------------------------------------------------------------------ C2
    D.H('C2 · Second order linear: interval, zero start, independent solutions', level=2, cites=D.cite('SYL', 4))
    TAGS(D, (5, 2))
    D.P(r'**When:** a second-order **linear** equation, usually with two starting values $y(t_0)$ and $y\prime(t_0)$. The question asks one of three things:')
    D.L([r'**Interval:** on what interval is exactly one solution guaranteed?',
         r'**Zero start:** what is the solution if both starting values are 0?',
         r'**Two solutions:** do two given solutions give the general solution?'])
    D.P(r'For all three, first divide by whatever multiplies $y\prime\prime$, so $y\prime\prime$ stands alone:')
    D.EQ(r'y\prime\prime+p(t)\,y\prime+q(t)\,y=g(t)')
    D.L([r'$p(t)$ = what multiplies $y\prime$ (after dividing)',
         r'$q(t)$ = what multiplies $y$ (after dividing)',
         r'$g(t)$ = the right side, called the forcing (after dividing)'])
    D.P(r'Example: $t\,y\prime\prime+y=0$ → divide by $t$ → $y\prime\prime+\dfrac1t\,y=0$. So $p=0$, $q=\dfrac1t$, $g=0$.')
    D.CO('info', r'**The theorem.** If $p$, $q$ and $g$ are continuous on an open interval $I$ that contains $t_0$, then for **any** starting values $y(t_0)$ and $y\prime(t_0)$ '
         r'there is **exactly one** solution, and it works on the **whole** interval $I$.')

    D.P(r'**Interval.** A **trouble point** is a $t$ where $p$, $q$ or $g$ breaks. '
        r'The biggest $I$ runs from the nearest trouble point left of $t_0$ to the nearest one on the right.')
    D.L([r'$t\,y\prime\prime+y=0$: $q=\dfrac1t$ breaks at $t=0$. For $t_0=5$, $I=(0,\infty)$. For $t_0=-2$, $I=(-\infty,0)$.',
         r'$y\prime\prime+3y\prime+2y=\cos t$: nothing breaks, so $I$ is the whole real line. Same for any constant-coefficient equation whose $g$ never breaks.'])
    D.P('**Method (interval):**')
    D.L([r'**Divide** by what multiplies $y\prime\prime$. Read off $p,q,g$.',
         r'**Trouble points:** where $p$, $q$ or $g$ breaks (0 in a denominator, $\ln$ of $\le0$, …).',
         r'**Pick the piece** of the $t$-axis between trouble points that contains $t_0$. Use open ends (round brackets).'],
        ordered=True)

    D.P(r'**Zero start.** Take a linear equation with right side $g=0$ and both starting values zero, $y(t_0)=0$ and $y\prime(t_0)=0$. The answer is:')
    D.EQ(r'y(t)\equiv0')
    D.P(r'Why: $y=0$ solves any such equation and fits both starting values. The theorem says there is only one solution, so $y=0$ is it.')
    D.P(r'Example: $y\prime\prime+3y\prime+2y=0$, $y(1)=0$, $y\prime(1)=0$ → $y\equiv0$, no solving needed. '
        r'But it needs $g=0$: in $y\prime\prime+y=1$, $y=0$ gives $0=1$, so it is not a solution.')

    D.P(r'**Two solutions → the general solution?** Say $y_1$ and $y_2$ both solve the same linear equation with $g=0$. Compute their **Wronskian**:')
    D.EQ(r'W=y_1\,y_2\prime-y_1\prime\,y_2')
    D.L([r'$W\neq0$ → $y_1,y_2$ are **independent** (neither is a multiple of the other), and $y=c_1y_1+c_2y_2$ is the general solution.',
         r'$W=0$ → one is a multiple of the other. Then $c_1y_1+c_2y_2$ really has only one constant, so it is **not** enough.'])
    D.P(r'Example: $e^{t}$ and $e^{2t}$ give $W=e^t\cdot2e^{2t}-e^t\cdot e^{2t}=e^{3t}$. That is never zero → independent.')
    D.P(r'This is why the repeated-root case in ' + link('B5', 'b5') + r' uses $(c_1+c_2t)e^{st}$: '
        r'$c_1e^{st}+c_2e^{st}$ is just $(c_1+c_2)e^{st}$, one constant.')
    D.CO('info', r'**Bonus (skip-safe): why the Wronskian decides it.** Fitting $c_1y_1+c_2y_2$ to $y(t_0)$ and $y\prime(t_0)$ gives two equations:'
         '\n\n$$\n' r'c_1y_1+c_2y_2=y(t_0),\quad c_1y_1\prime+c_2y_2\prime=y\prime(t_0)' '\n$$\n\n'
         r'A $2\times2$ system like this has exactly one answer when its determinant, $y_1y_2\prime-y_1\prime y_2=W$, is not zero. '
         r'So $W\neq0$ means you can match any pair of starting values.')

    P(D, 'W5 · Find the interval; do not solve',
      r'For $(t-1)\,y\prime\prime+y\prime+y=\ln t$, find the largest interval on which the theorem guarantees exactly one solution for (a) $t_0=2$, (b) $t_0=\tfrac12$.',
      [S(r'**Type:** existence and uniqueness, second-order linear. **Divide** by $t-1$.', r'p=\dfrac1{t-1},\quad q=\dfrac1{t-1},\quad g=\dfrac{\ln t}{t-1}'),
       S(r'**Trouble points:** $\ln t$ needs $t>0$, and the denominator needs $t\neq1$. So the pieces are $(0,1)$ and $(1,\infty)$.'),
       S(r'**Pick the piece:** $t_0=2$ is in $(1,\infty)$. $t_0=\tfrac12$ is in $(0,1)$.')],
      r'(a) $(1,\infty)$. (b) $(0,1)$.', diff='intermediate')
    P(D, 'W5 · Which pair gives the general solution?',
      r'Both pairs solve $y\prime\prime+4y\prime+4y=0$: (a) $e^{-2t}$ and $3e^{-2t}$; (b) $e^{-2t}$ and $te^{-2t}$. Compute each Wronskian and decide which pair gives the general solution.',
      [S(r'**Type:** independence, so compute $W=y_1y_2\prime-y_1\prime y_2$.'),
       S(r'**Pair (a):** $y_2\prime=-6e^{-2t}$, $y_1\prime=-2e^{-2t}$.', r'W=e^{-2t}(-6e^{-2t})-(-2e^{-2t})(3e^{-2t})=0'),
       S(r'**Pair (b):** product rule, $(te^{-2t})\prime=(1-2t)e^{-2t}$.', r'W=e^{-2t}(1-2t)e^{-2t}-(-2e^{-2t})\,te^{-2t}=e^{-4t}'),
       S(r'**Decide:** $e^{-4t}$ is never zero, so pair (b) is independent.')],
      r'(a) $W=0$: not enough (they are multiples). (b) $W=e^{-4t}\neq0$: general solution $y=(c_1+c_2t)e^{-2t}$.',
      diff='intermediate')
    P(D, 'W5 + W6 · The answer without solving',
      r'Solve $y\prime\prime+t\,y\prime+e^{t}\,y=0$, $\;y(0)=0$, $\;y\prime(0)=0$.',
      [S(r'**Type:** the $t$ and $e^t$ coefficients look impossible with our methods. But it is linear, $g=0$, and both starting values are 0: a **zero start**.'),
       S(r'**Interval:** $p=t$, $q=e^t$, $g=0$ never break, so exactly one solution exists on the whole real line.'),
       S(r'**Try $y=0$:** $0+0+0=0$ ✓, and $y(0)=0$, $y\prime(0)=0$ ✓.'),
       S(r'**Conclude:** there is only one solution, and $y=0$ works, so it is **the** solution.')],
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
