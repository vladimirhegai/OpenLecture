"""Topic C: does exactly one solution exist? (Week 3 Topic 3, Week 5 Topic 2, Week 6 outcomes).

Layout (REWRITE_PLAN.md). Shared letters: F(t, y) = the right side of y' = F (C1); y'' + p y' + q y = f (C2, the same
p, q, f as B2/B6/B7). C1 step words: Write, Differentiate, Find where it breaks, Check the point. C2: three cases,
one per kind of question.
"""
import sympy as sp

from midlib import CARD, P, S, TAGS, link, t, y, zero


def build(D):
    W3 = lambda *p: D.cite('W3', *p)
    D.H('Topic C: Does exactly one solution exist?', cites=W3(5))
    TAGS(D, (3, 3), (5, 2))
    D.P(r'**Use this when** the question asks “is there exactly one solution?” or “on what interval is one guaranteed?”.')
    D.P(r'**The move: don’t solve anything.** Write the equation in its form, then look for where something **breaks**:')
    D.EQ(r'\dfrac{t}{y}\ \text{breaks at}\ y=0,\qquad \ln t\ \text{breaks at}\ t\le0,\qquad \sqrt{y}\ \text{breaks at}\ y<0')
    D.L([r'First order, like $y\prime=\dfrac ty$ → ' + link('C1', 'c1') + '.',
         r'Second-order linear, like $t\,y\prime\prime+y=0$ → ' + link('C2', 'c2') + '.'])

    # ------------------------------------------------------------------ C1
    D.H('C1 · First order: exactly one solution through this point?', level=2, cites=W3(5))
    TAGS(D, (3, 3))
    D.P(r'**Use this when** you get $y\prime=F(t,y)$ and a starting point $(t_0,y_0)$:')
    D.EQ(r'\dfrac{dy}{dt}=\dfrac{t}{y},\qquad y(2)=1')
    D.P(r'**The rule:** check $F$ and its $y$-derivative $F_y$ near the point.')
    D.L([r'**Both fine** (no blow-ups) → yes, **exactly one** solution through the point.',
         r'**One breaks** → the theorem says **nothing**. That means “don’t know”, not “no”.'])
    D.WHY('The theorem, and why $F_y$ matters',
          r'**Theorem** (Spiegel, Week 3 lecture): if $F$ and $\dfrac{\partial F}{\partial y}$ are both continuous near $(t_0,y_0)$, then exactly one solution passes through $(t_0,y_0)$.'
          '\n\n'
          r'$F_y$ says how fast the slope changes as you move up or down. If it stays finite, two solutions that start at the same point can never drift apart. '
          r'For $\sqrt y$ it is infinite at $y=0$, so a curve can sit on the axis and then “peel off” at any moment (graph below).')
    D.P('**Steps**')
    D.L([r'**Write** it as $y\prime=F(t,y)$: get $y\prime$ alone.',
         r'**Differentiate** $F$ in $y$, treating $t$ like a number. That’s $F_y$.',
         r'**Find where it breaks:** where $F$ or $F_y$ has a $0$ in a denominator, $\ln$ of $\le0$, or $\sqrt{\ }$ of $<0$.',
         r'**Check the point:** away from those spots → exactly one solution. On them → no conclusion.'], ordered=True)
    D.P('**Short examples:**')
    D.EQ(r'F=t^2+3ty\quad\Longrightarrow\quad F_y=3t\quad\text{(never breaks: every point is fine)}')
    D.EQ(r'F=\dfrac ty\quad\Longrightarrow\quad F_y=-\dfrac{t}{y^2}\quad\text{(breaks at }y=0)')
    CARD(D, r'Differentiate in $y$: $\;\dfrac{\partial}{\partial y}\Big(\dfrac{2t-(\ln t)\,y}{t-3}\Big)=-\dfrac{\ln t}{t-3}$',
         [(r'Treat $t$ like a number. Split the fraction: the $2t$ part has no $y$, so it gives $0$.', r'\dfrac{2t}{t-3}-\dfrac{\ln t}{t-3}\,y\quad\Longrightarrow\quad F_y=-\dfrac{\ln t}{t-3}'),
          (r'Power rule in $y$:', r'\dfrac{\partial}{\partial y}\big(t\,y^{-1}\big)=-t\,y^{-2},\qquad \dfrac{\partial}{\partial y}\sqrt y=\dfrac{1}{2\sqrt y}')])
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
    caption "At $y=0$, $F_y=1/(2\sqrt y)$ blows up, so no guarantee. And in fact many curves leave $(1,0)$. Above the axis nothing breaks, and only one curve goes through each point."
    ''', intro='**What does “no guarantee” look like?**')

    D.H('Practice: C1', level=3)
    P(D, 'W3 · Same equation, two starting points',
      r'For $\dfrac{dy}{dt}=\sqrt{y}$: (a) does the theorem guarantee a unique solution through $(1,4)$? (b) through $(1,0)$? '
      r'For (b), check that $y=0$ and $y=\dfrac{(t-1)^2}{4}$ (for $t\ge1$) both pass through $(1,0)$ and solve the ODE.',
      [S(r'**Type:** exactly one solution? First order → C1.'),
       S(r'**Write.**', r'F=\sqrt y'),
       S(r'**Differentiate** in $y$.', r'F_y=\dfrac{1}{2\sqrt y}'),
       S(r'**Find where it breaks:** $F$ needs $y\ge0$, and $F_y$ blows up at $y=0$.', r'y\le0'),
       S(r'**Check the points:** (a) $(1,4)$ has $y_0=4>0$ → unique. (b) $(1,0)$ is on $y=0$ → no guarantee.'),
       S(r'**Two solutions through $(1,0)$:** for $y=\frac{(t-1)^2}{4}$, $y\prime=\frac{t-1}{2}=\sqrt y$ when $t\ge1$ ✓. For $y=0$: $0=\sqrt0$ ✓.')],
      r'(a) Yes, exactly one solution through $(1,4)$. (b) No guarantee, and in fact at least two solutions pass through $(1,0)$.',
      cites=W3(5))
    P(D, 'W3 · Which points are guaranteed?',
      r'For $\dfrac{dy}{dt}=\dfrac{t}{y}$, decide whether the theorem guarantees a unique solution through (a) $(2,1)$, (b) $(0,3)$, (c) $(2,0)$.',
      [S(r'**Type:** C1.'),
       S(r'**Write.**', r'F=\dfrac ty'),
       S(r'**Differentiate** in $y$ (power rule).', r'F_y=-\dfrac{t}{y^2}'),
       S(r'**Find where it breaks:** both divide by $y$.', r'y=0'),
       S(r'**Check the points:** (a) $y_0=1$ and (b) $y_0=3$ are off the line. (c) $y_0=0$ is on it.')],
      r'(a) Yes. (b) Yes. (c) No guarantee: $F$ itself is undefined at $(2,0)$.', cites=W3(5))
    P(D, 'W3 · A strip, not a point',
      r'For $(t-3)\,y\prime+(\ln t)\,y=2t$, $\;y(1)=2$, find the region containing the starting point where the theorem applies. Do not solve.',
      [S(r'**Type:** C1.'),
       S(r'**Write:** get $y\prime$ alone.', r'F=\dfrac{2t-(\ln t)\,y}{t-3}'),
       S(r'**Differentiate** in $y$. Only the $y$ term survives.', r'F_y=-\dfrac{\ln t}{t-3}'),
       S(r'**Find where it breaks:** $\ln t$ needs $t>0$, and the denominator needs $t\neq3$. Nothing limits $y$.'),
       S(r'**Check the point:** $t_0=1$ lies between $0$ and $3$.', r'0<t<3,\quad\text{any }y')],
      r'The strip $0<t<3$ (all $y$). The start $(1,2)$ is inside it, so exactly one solution passes through it.',
      diff='intermediate')

    # ------------------------------------------------------------------ C2
    D.H('C2 · Second order linear: interval, zero start, two solutions', level=2, cites=D.cite('SYL', 4))
    TAGS(D, (5, 2))
    D.P(r'**Use this when** it’s a second-order **linear** equation. First **write** it with $y\prime\prime$ alone (same letters as ' + link('B7', 'b7') + '):')
    D.EQ(r'y\prime\prime+p(t)\,y\prime+q(t)\,y=f(t)')
    D.P('**Short example:**')
    D.EQ(r't\,y\prime\prime+y=0\quad\Longrightarrow\quad y\prime\prime+\dfrac1t\,y=0\quad\Longrightarrow\quad p=0,\ q=\dfrac1t,\ f=0')
    D.P(r'**The rule:** if $p$, $q$, $f$ don’t break on an interval around $t_0$, there’s **exactly one** solution there, for any starting values.')
    D.WHY('The theorem, word for word',
          r'If $p$, $q$ and $f$ are continuous on an open interval $I$ that contains $t_0$, then for **any** starting values $y(t_0)$ and $y\prime(t_0)$ '
          r'there is **exactly one** solution, and it works on the **whole** interval $I$.')
    D.P('The question is always one of three cases:')

    D.H('Case 1: what interval?', level=3)
    D.L([r'**Write** it with $y\prime\prime$ alone. Read $p$, $q$, $f$.',
         r'**Find where they break** (trouble points): a $0$ in a denominator, $\ln$ of $\le0$, …',
         r'**Pick the piece** of the $t$-axis between trouble points that contains $t_0$. Round brackets.'], ordered=True)
    D.P('**Short examples:**')
    D.EQ(r't\,y\prime\prime+y=0:\quad q=\dfrac1t\ \text{breaks at}\ 0\quad\Longrightarrow\quad t_0=5:\ (0,\infty)')
    D.EQ(r'y\prime\prime+3y\prime+2y=\cos t:\quad\text{nothing breaks}\quad\Longrightarrow\quad(-\infty,\infty)')

    D.H('Case 2: right side 0 and both starting values 0', level=3)
    D.P(r'Then the answer is zero, no solving:')
    D.EQ(r'f=0,\quad y(t_0)=0,\quad y\prime(t_0)=0\quad\Longrightarrow\quad y(t)\equiv0')
    D.P(r'Why: $y=0$ solves it and fits both starting values, and there’s only one solution. It needs $f=0$: in $y\prime\prime+y=1$, $y=0$ gives $0=1$.')

    D.H('Case 3: do y₁ and y₂ give the general solution?', level=3)
    D.P(r'Compute the **Wronskian**:')
    D.EQ(r'W=y_1\,y_2\prime-y_1\prime\,y_2')
    D.L([r'$W\neq0$ → independent: $y=c_1y_1+c_2y_2$ **is** the general solution.',
         r'$W=0$ → one is a multiple of the other: **not** enough.'])
    D.P('**Short example:**')
    D.EQ(r'e^{t},\ e^{2t}:\quad W=e^{t}\cdot2e^{2t}-e^{t}\cdot e^{2t}=e^{3t}\neq0')
    D.P(r'That’s why the repeated root in ' + link('B5', 'b5') + r' uses $(c_1+c_2t)e^{st}$: $c_1e^{st}+c_2e^{st}$ is really one constant.')
    D.WHY('Why the Wronskian decides it',
          r'Fitting $c_1y_1+c_2y_2$ to $y(t_0)$ and $y\prime(t_0)$ gives two equations:'
          '\n\n$$\n' r'c_1y_1+c_2y_2=y(t_0),\qquad c_1y_1\prime+c_2y_2\prime=y\prime(t_0)' '\n$$\n\n'
          r'A $2\times2$ system has exactly one answer when its determinant, $y_1y_2\prime-y_1\prime y_2=W$, is not zero.')

    D.H('Practice: C2', level=3)
    P(D, 'W5 · Find the interval; do not solve',
      r'For $(t-1)\,y\prime\prime+y\prime+y=\ln t$, find the largest interval on which the theorem guarantees exactly one solution for (a) $t_0=2$, (b) $t_0=\tfrac12$.',
      [S(r'**Type:** C2, Case 1.'),
       S(r'**Write:** divide by $t-1$.', r'p=\dfrac1{t-1},\quad q=\dfrac1{t-1},\quad f=\dfrac{\ln t}{t-1}'),
       S(r'**Find where they break:** $\ln t$ needs $t>0$, the denominator needs $t\neq1$. Pieces: $(0,1)$ and $(1,\infty)$.'),
       S(r'**Pick the piece:** $t_0=2$ is in $(1,\infty)$. $t_0=\tfrac12$ is in $(0,1)$.')],
      r'(a) $(1,\infty)$. (b) $(0,1)$.', diff='intermediate')
    P(D, 'W5 · Which pair gives the general solution?',
      r'Both pairs solve $y\prime\prime+4y\prime+4y=0$: (a) $e^{-2t}$ and $3e^{-2t}$; (b) $e^{-2t}$ and $te^{-2t}$. Compute each Wronskian and decide which pair gives the general solution.',
      [S(r'**Type:** C2, Case 3: compute $W=y_1y_2\prime-y_1\prime y_2$.'),
       S(r'**Pair (a):** $y_1\prime=-2e^{-2t}$, $y_2\prime=-6e^{-2t}$.', r'W=e^{-2t}(-6e^{-2t})-(-2e^{-2t})(3e^{-2t})=0'),
       S(r'**Pair (b):** product rule, $(te^{-2t})\prime=(1-2t)e^{-2t}$.', r'W=e^{-2t}(1-2t)e^{-2t}-(-2e^{-2t})\,te^{-2t}=e^{-4t}'),
       S(r'**Decide:** $e^{-4t}$ is never zero, so pair (b) is independent.')],
      r'(a) $W=0$: not enough (they are multiples). (b) $W=e^{-4t}\neq0$: general solution $y=(c_1+c_2t)e^{-2t}$.',
      diff='intermediate')
    P(D, 'W5 + W6 · The answer without solving',
      r'Solve $y\prime\prime+t\,y\prime+e^{t}\,y=0$, $\;y(0)=0$, $\;y\prime(0)=0$.',
      [S(r'**Type:** $t$ and $e^t$ in front look impossible. But it’s linear, $f=0$, and both starting values are $0$: C2, Case 2.'),
       S(r'**Write:** $p=t$, $q=e^t$, $f=0$. None of them ever breaks, so exactly one solution exists everywhere.'),
       S(r'**Try $y=0$:** $0+0+0=0$ ✓, and $y(0)=0$, $y\prime(0)=0$ ✓.'),
       S(r'There’s only one solution, and $y=0$ works, so it is **the** solution.')],
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
