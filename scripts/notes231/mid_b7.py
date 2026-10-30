"""B7: reduction of order (Week 6).

Layout (REWRITE_PLAN.md). Shared letters: y'' + p(t) y' + q(t) y = 0 (p, q as in C2; p as in B2), y1 = the
given solution, v = the unknown multiplier, z = v', c1, c2 = the constants (as in B5/B6).
Step words: Write, Substitute, Plug in and collect, Solve for z, Integrate, Multiply back, Plug in.
"""
import sympy as sp

from midlib import CARD, P, S, TAGS, link, second, t, zero


def build(D):
    W6 = lambda *p: D.cite('W6', *p)
    D.H('B7 · Reduction of order: t in front, one solution given', level=2, cites=W6(1, 2))
    TAGS(D, (6, 1))
    D.P(r'**Use this when** it’s second order with $t$ in front (so ' + link('B5', 'b5') + r' fails), and they **give you one solution** $y_1$:')
    D.EQ(r'y\prime\prime-t\,y\prime+y=0,\qquad y_1=t')
    D.P(r'Write it with $y\prime\prime$ alone (divide by whatever multiplies it):')
    D.EQ(r'y\prime\prime+p(t)\,y\prime+q(t)\,y=0')
    D.L([r'$p(t)$ = what multiplies $y\prime$, sign included',
         r'$q(t)$ = what multiplies $y$',
         r'$y_1$ = the solution you’re given. Check it: plug it in, you should get $0$.'])
    D.P(r'**Short example:**')
    D.EQ(r't^2y\prime\prime-3ty\prime+4y=0\quad\Longrightarrow\quad y\prime\prime-\dfrac3t\,y\prime+\dfrac4{t^2}\,y=0')
    D.EQ(r'p=-\dfrac3t,\qquad q=\dfrac{4}{t^2}')

    D.P(r'**The move: guess $y=y_1\,v$.** The known solution times an unknown function $v(t)$.')
    D.EQ(r'y=y_1\,v')
    D.P(r'When you plug it in, every term with a plain $v$ **cancels**. Only $v\prime$ and $v\prime\prime$ are left. '
        r'Call $z=v\prime$ and it’s a **first-order** equation (' + link('B1', 'b1') + ' or ' + link('B2', 'b2') + ').')
    D.P('**Steps**')
    D.L([r'**Write** it with $y\prime\prime$ alone. Read $p$, $q$. Check $y_1$.',
         r'**Substitute** $y=y_1v$. Use the product rule for $y\prime$ and $y\prime\prime$ (below).',
         r'**Plug in and collect.** The plain-$v$ terms cancel.',
         r'**Solve for $z$:** set $z=v\prime$. It’s first order: separate it (' + link('B1', 'b1') + ').',
         r'**Integrate:** $v=\int z\,dt+c_2$.',
         r'**Multiply back:** $y=y_1v$. The $c_2$ gives back $c_2\,y_1$, the solution you started with.',
         r'**Plug in** the conditions, if they give any.'], ordered=True)
    D.P(r'The product rule for $y=y_1v$:')
    D.EQ(r'y\prime=y_1\prime\,v+y_1\,v\prime')
    D.EQ(r'y\prime\prime=y_1\prime\prime\,v+2y_1\prime\,v\prime+y_1\,v\prime\prime')
    D.P(r'**Short example:** with $y_1=t$:')
    D.EQ(r'y=tv\quad\Longrightarrow\quad y\prime=v+tv\prime,\quad y\prime\prime=2v\prime+tv\prime\prime')

    D.STEPS('★ Lecture (Week 6): reduce y″ − t y′ + y = 0, given y₁ = t', [
        (r'y\prime\prime-ty\prime+y=0,\qquad y_1=t', r'**Write.** Check: $y_1=t$ gives $0-t+t=0$.'),
        (r'y=\hl{tv}', r'**Substitute:** the known solution times an unknown $v$.'),
        (r'y\prime=\hl{v+tv\prime},\qquad y\prime\prime=\hl{2v\prime+tv\prime\prime}', 'Product rule.'),
        (r'(2v\prime+tv\prime\prime)-t(v+tv\prime)+tv=0', '**Plug in** all three.'),
        (r'\hl{tv\prime\prime+(2-t^2)v\prime}=0', r'**Collect.** The $-tv$ and $+tv$ cancel.'),
        (r't\hl{z\prime}+(2-t^2)\hl{z}=0', r'Set $z=v\prime$: now it’s first order in $z$.'),
    ], intro='**★ The prof’s example**, step by step (press the arrows). Then finish it yourself:')
    CARD(D, r'★ Finish the lecture example (try it, then open): solve $\;tz\prime+(2-t^2)z=0$, then find $y$',
         [(r'**Solve for $z$:** it separates. Divide by $tz$ and move the $t$ terms right.', r'\dfrac{dz}{z}=\dfrac{t^2-2}{t}\,dt=\left(t-\dfrac2t\right)dt'),
          (r'Integrate both sides.', r'\ln|z|=\dfrac{t^2}2-2\ln|t|+C'),
          (r'Raise $e$ to both sides. $e^{-2\ln|t|}=\frac1{t^2}$, and $e^{C}$ is a new constant $c_1$.', r'z=c_1\,\dfrac{e^{t^2/2}}{t^2}'),
          (r'**Integrate** $v=\int z\,dt$. This integral has no formula, so leave it as is.', r'v=c_1\int\dfrac{e^{t^2/2}}{t^2}\,dt+c_2'),
          (r'**Multiply back** by $y_1=t$.', r'y=tv')],
         r'y=c_2\,t+c_1\,t\displaystyle\int\frac{e^{t^2/2}}{t^2}\,dt')
    CARD(D, r'Full example: $\;t^2y\prime\prime-3ty\prime+4y=0$, $\;y_1=t^2$, $\;t>0$',
         [(r'**Write:** divide by $t^2$. Check $y_1$: $2t^2-6t^2+4t^2=0$ ✓.', r'y\prime\prime-\dfrac3t\,y\prime+\dfrac4{t^2}\,y=0'),
          (r'**Substitute** $y=t^2v$ (product rule).', (r'y\prime=2tv+t^2v\prime', r'y\prime\prime=2v+4tv\prime+t^2v\prime\prime')),
          (r'**Plug in and collect** (into the original, times $t^2$). The plain-$v$ terms cancel: $2-6+4=0$.', r't^4v\prime\prime+t^3v\prime=0'),
          (r'**Solve for $z$:** divide by $t^4$, set $z=v\prime$, separate.', (r'z\prime+\dfrac zt=0', r'\dfrac{dz}{z}=-\dfrac{dt}{t}\quad\Rightarrow\quad z=\dfrac{c_1}{t}')),
          (r'**Integrate:** $\int\frac1t\,dt=\ln t$ for $t>0$.', r'v=c_1\ln t+c_2'),
          (r'**Multiply back** by $t^2$.', r'y=c_1t^2\ln t+c_2t^2')],
         r'y=c_1t^2\ln t+c_2t^2')
    CARD(D, r'Check your answer: $\;y_2=y_1\displaystyle\int\dfrac{e^{-\int p\,dt}}{y_1^{\,2}}\,dt$',
         [(r'All the steps above always end at this formula. Use it to check, or as a shortcut if the question lets you. Same $p$ as in ' + link('B2', 'b2') + '.',
           r'y_2=y_1\int\dfrac{e^{-\int p\,dt}}{y_1^{\,2}}\,dt'),
          (r'Example: $t^2y\prime\prime-3ty\prime+4y=0$, $y_1=t^2$. Here $p=-\frac3t$.', r'e^{-\int p\,dt}=e^{3\ln t}=t^3'),
          (r'Plug in.', r'y_2=t^2\int\dfrac{t^3}{t^4}\,dt=t^2\ln t\quad\checkmark')])
    D.CO('warning', r'**Divide first.** $p$ is what multiplies $y\prime$ **after** $y\prime\prime$ stands alone. In $t^2y\prime\prime-3ty\prime+4y=0$, $p=-\frac3t$, not $-3t$.')
    D.CO('tip', r'**An integral with no formula**, like $\int\frac{e^{t^2/2}}{t^2}dt$, can stay as an integral. That counts as a full answer.')

    D.H('Practice: B7', level=3)
    P(D, 'W5 + W6 · Where the repeated-root t comes from',
      r'$y\prime\prime+4y\prime+4y=0$ has the repeated root $s=-2$, so $y_1=e^{-2t}$. Use reduction of order to find the general solution.',
      [S(r'**Type:** one solution given → B7.'),
       S(r'**Substitute** $y=e^{-2t}v$ (product rule).', (r'y\prime=e^{-2t}(v\prime-2v)', r'y\prime\prime=e^{-2t}(v\prime\prime-4v\prime+4v)')),
       S(r'**Plug in and collect**, then divide by $e^{-2t}$. This time the $v\prime$ terms cancel too.', r'(v\prime\prime-4v\prime+4v)+4(v\prime-2v)+4v=v\prime\prime=0'),
       S(r'**Solve for $z$:** $z=v\prime$, and $z\prime=0$.', r'z=c_2'),
       S(r'**Integrate.**', r'v=c_1+c_2t'),
       S(r'**Multiply back.**', r'y=(c_1+c_2t)\,e^{-2t}')],
      r'$y=(c_1+c_2t)e^{-2t}$. That’s ' + link('B5', 'b5') + r' Case 2: the extra $t$ came from $v$.')
    P(D, 'W6 · A second solution with a logarithm',
      r'For $t>0$, $y_1=t$ solves $t^2y\prime\prime-ty\prime+y=0$. Find the general solution.',
      [S(r'**Type:** $t$ in front, one solution given → B7.'),
       S(r'**Substitute** $y=tv$ (product rule).', (r'y\prime=v+tv\prime', r'y\prime\prime=2v\prime+tv\prime\prime')),
       S(r'**Plug in and collect.** The plain-$v$ terms cancel: $-tv+tv=0$.', (r't^2(2v\prime+tv\prime\prime)-t(v+tv\prime)+tv=0', r't^3v\prime\prime+t^2v\prime=0')),
       S(r'**Solve for $z$:** divide by $t^3$, set $z=v\prime$, separate.', (r'z\prime+\dfrac zt=0', r'z=\dfrac{c_1}{t}')),
       S(r'**Integrate.**', r'v=c_1\ln t+c_2'),
       S(r'**Multiply back** by $t$.', r'y=c_1t\ln t+c_2t')],
      r'$y=c_1t\ln t+c_2t$. Formula check: $p=-\frac1t$, $e^{-\int p\,dt}=t$, $y_2=t\int\frac{t}{t^2}dt=t\ln t$ ✓.', diff='intermediate')


def verify():
    E = sp.exp
    v = sp.Function('v')(t)
    y = t * v
    zero(sp.diff(y, t, 2) - t * sp.diff(y, t) + y - (t * sp.diff(v, t, 2) + (2 - t ** 2) * sp.diff(v, t)))
    z = E(t ** 2 / 2) / t ** 2
    zero(t * sp.diff(z, t) + (2 - t ** 2) * z)
    zero(E(-sp.integrate(-t, t)) / t ** 2 - z)
    y = E(-2 * t) * v
    zero((sp.diff(y, t, 2) + 4 * sp.diff(y, t) + 4 * y) / E(-2 * t) - sp.diff(v, t, 2))
    zero(sp.diff(y, t) - E(-2 * t) * (sp.diff(v, t) - 2 * v))
    zero(sp.diff(y, t, 2) - E(-2 * t) * (sp.diff(v, t, 2) - 4 * sp.diff(v, t) + 4 * v))
    C1, C2 = sp.symbols('C1 C2')
    second((C1 + C2 * t) * E(-2 * t), 1, 4, 4)
    tp = sp.symbols('tp', positive=True)
    vv = v.subs(t, tp)
    y = tp ** 2 * vv
    zero(tp ** 2 * sp.diff(y, tp, 2) - 3 * tp * sp.diff(y, tp) + 4 * y - (tp ** 4 * sp.diff(vv, tp, 2) + tp ** 3 * sp.diff(vv, tp)))
    for sol in (tp ** 2, tp ** 2 * sp.log(tp)):
        zero(tp ** 2 * sp.diff(sol, tp, 2) - 3 * tp * sp.diff(sol, tp) + 4 * sol)
    zero(E(-sp.integrate(-3 / tp, tp)) / tp ** 4 - 1 / tp)
    # formula example: t^2 y'' - t y' + y = 0, y1 = t  ->  y2 = t ln t
    for sol in (tp, tp * sp.log(tp)):
        zero(tp ** 2 * sp.diff(sol, tp, 2) - tp * sp.diff(sol, tp) + sol)
    zero(tp * sp.integrate(E(-sp.integrate(-1 / tp, tp)) / tp ** 2, tp) - tp * sp.log(tp))
    # practice: t^2 y'' - t y' + y = 0 with y = t v collects to t^3 v'' + t^2 v'
    w = sp.Function('w')(tp)
    yy = tp * w
    zero(tp ** 2 * sp.diff(yy, tp, 2) - tp * sp.diff(yy, tp) + yy - (tp ** 3 * sp.diff(w, tp, 2) + tp ** 2 * sp.diff(w, tp)))
