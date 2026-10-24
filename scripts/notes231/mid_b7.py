"""B7: reduction of order (Week 6)."""
import sympy as sp

from midlib import P, S, TAGS, link, second, t, zero


def build(D):
    W6 = lambda *p: D.cite('W6', *p)
    D.H('B7 · Reduction of order', level=2, cites=W6(1, 2))
    TAGS(D, (6, 1))
    D.P(r'**What if the coefficients have $t$ in them?** Like $y\prime\prime-ty\prime+y=0$. The characteristic equation (' + link('B5', 'b5') +
        r') only works when the coefficients are numbers. But if the question **gives you one solution** $y_1$, reduction of order finds the second one.')
    D.P(r'Write the equation with $y\prime\prime$ alone (divide by its coefficient):')
    D.EQ(r'y\prime\prime+p(t)\,y\prime+q(t)\,y=0')
    D.L([r'$p(t)$ = the coefficient of $y\prime$ (sign included)',
         r'$q(t)$ = the coefficient of $y$',
         r'$y_1(t)$ = the solution you are given. Check it first: it must give $0$.'])
    D.P('Mini examples:')
    D.L([r'$y\prime\prime-ty\prime+y=0$ with $y_1=t$: here $p=-t$, $q=1$. Check: $0-t\cdot1+t=0$ ✓.',
         r'$t^2y\prime\prime-3ty\prime+4y=0$ with $y_1=t^2$: divide by $t^2$, so $p=-\frac3t$, $q=\frac4{t^2}$.'])

    D.P(r'**The idea.** Look for the second solution as the known one times an unknown function $v(t)$:')
    D.EQ(r'y=y_1\,v')
    D.P(r'Substituting makes every plain-$v$ term cancel, so only $v\prime$ and $v\prime\prime$ are left. '
        r'Setting $z=v\prime$ turns that into a **first-order** equation: the order went down by one.')
    D.P('**Method:**')
    D.L([r'**Substitute** $y=y_1v$, with $y\prime=y_1\prime v+y_1v\prime$ and $y\prime\prime=y_1\prime\prime v+2y_1\prime v\prime+y_1v\prime\prime$.',
         r'**Collect** terms: the plain-$v$ terms cancel, because $y_1$ is a solution.',
         r'**Set $z=v\prime$** and solve the first-order equation for $z$ (usually separable, ' + link('B1', 'b1') + '; or linear, ' + link('B2', 'b2') + ').',
         r'**Integrate:** $v=\int z\,dt$, plus a constant.',
         r'**Multiply back:** $y=y_1v$. The constant from step 4 gives back $C\,y_1$, the solution you started with.'],
        ordered=True)
    D.P('**Check with the formula.** Reduction of order always ends at')
    D.EQ(r'y_2=y_1\int\dfrac{e^{-\int p\,dt}}{y_1^{\,2}}\,dt')
    D.P(r'Use it to check your answer, or as a shortcut if the question allows it.')
    D.P('**Calculus you need here:**')
    D.T(['Expression', 'Result', 'Note'], [
        [r'$(y_1v)\prime$', r'$y_1\prime v+y_1v\prime$', 'product rule'],
        [r'$(y_1v)\prime\prime$', r'$y_1\prime\prime v+2y_1\prime v\prime+y_1v\prime\prime$', 'product rule twice; the middle terms combine'],
        [r'$\int\frac1z\,dz$', r'$\ln|z|$', r'for the separable $z$ equation'],
        [r'$e^{-2\ln t}$', r'$\dfrac{1}{t^2}$', r'$e^{k\ln t}=t^k$'],
        [r'$\int\dfrac{e^{t^2/2}}{t^2}\,dt$', 'no formula', 'leave it as an integral: that is a full answer'],
    ])
    D.CO('info', r'**Bonus (skip-safe): why the plain-$v$ terms cancel.** After substituting, collect everything that multiplies $v$ itself: '
         r'it is $v\,(y_1\prime\prime+p\,y_1\prime+q\,y_1)$. The bracket is the ODE applied to $y_1$, which is $0$ because $y_1$ is a solution.')
    D.STEPS('Lecture: reduce y″ − t y′ + y = 0, given y₁ = t', [
        (r"y''-ty'+y=0,\qquad y_1=t", r'Check: $y_1=t$ gives $0-t+t=0$.'),
        (r'y=\hl{tv}', r'Multiply the known solution by an unknown $v$.'),
        (r"y'=\hl{v+tv'},\qquad y''=\hl{2v'+tv''}", 'Product rule (calculus table).'),
        (r"(2v'+tv'')-t(v+tv')+tv=0", 'Substitute all three into the ODE.'),
        (r"\hl{tv''+(2-t^2)v'}=0", r'Collect terms. The $-tv$ and $+tv$ cancel.'),
        (r"t\hl{z'}+(2-t^2)\hl{z}=0", r'Set $z=v\prime$: first order in $z$.'),
    ], intro='The professor’s example, step by step:')
    D.EX('W6 · Finish the lecture example · handwritten notes p. 1–2',
         r"Solve $tz'+(2-t^2)z=0$ (from the stepper above), then find the general solution of $y''-ty'+y=0$ for $t\neq0$.",
         [S(r'**Type:** the $z$ equation is separable. Divide by $tz$ and move the $t$ terms right.', r'\dfrac{dz}{z}=\dfrac{t^2-2}{t}\,dt=\left(t-\dfrac2t\right)dt'),
          S(r'**Integrate** both sides: $\int\frac1z\,dz=\ln|z|$.', r'\ln|z|=\dfrac{t^2}2-2\ln|t|+C'),
          S(r'Exponentiate; $e^{-2\ln|t|}=1/t^2$.', r'z=C_1\,\dfrac{e^{t^2/2}}{t^2}'),
          S(r'**Integrate** again, $v=\int z\,dt$. This integral has no formula, so it stays.', r'v=C_1\int\dfrac{e^{t^2/2}}{t^2}\,dt+C_2'),
          S(r'**Multiply back** by $y_1=t$.', r'y=tv')],
         r'$y=C_2\,t+C_1\,t\displaystyle\int\frac{e^{t^2/2}}{t^2}\,dt$. Formula check: $p=-t$, so $e^{-\int p\,dt}=e^{t^2/2}$ and $y_1^2=t^2$. ✓',
         cites=W6(1, 2))

    P(D, 'W5 + W6 · Where the repeated-root t comes from',
      r"$y''+4y'+4y=0$ has the repeated characteristic root $s=-2$, so $y_1=e^{-2t}$. Use reduction of order to find the general solution.",
      [S(r'**Type:** one solution given: reduction of order. **Substitute** $y=e^{-2t}v$.', r"y'=e^{-2t}(v'-2v)"),
       S('Differentiate again.', r"y''=e^{-2t}(v''-4v'+4v)"),
       S(r'**Collect:** substitute and divide by $e^{-2t}$. The $v\prime$ terms cancel too.', r"(v''-4v'+4v)+4(v'-2v)+4v=v''=0"),
       S(r'**Integrate** twice.', r'v=C_1+C_2t'),
       S(r'**Multiply back.**', r'y=(C_1+C_2t)\,e^{-2t}')],
      r'$y=(C_1+C_2t)e^{-2t}$: exactly the repeated-root row of ' + link('B5', 'b5') + r'. The extra $t$ is $v$.')
    P(D, 'W6 · A second solution with a logarithm',
      r"For $t>0$, $y_1=t^2$ solves $t^2y''-3ty'+4y=0$. Find the general solution.",
      [S(r'**Type:** variable coefficients, one solution given. **Substitute** $y=t^2v$.', r"y'=2tv+t^2v',\qquad y''=2v+4tv'+t^2v''"),
       S(r'**Collect:** the plain $v$ terms cancel ($2-6+4=0$).', r"t^4v''+t^3v'=0"),
       S(r'Divide by $t^4$ and **set $z=v\prime$**.', r"z'+\dfrac zt=0"),
       S(r'Separate: $\int\frac{dz}{z}=-\int\frac{dt}{t}$, so $\ln|z|=-\ln t+C$.', r'z=\dfrac{C_2}t'),
       S(r'**Integrate:** $\int\frac1t\,dt=\ln t$ for $t>0$.', r'v=C_1+C_2\ln t'),
       S(r'**Multiply back** by $t^2$.', r'y=C_1t^2+C_2t^2\ln t')],
      r'$y=C_1t^2+C_2t^2\ln t$. Formula check: $p=-\frac3t$, $e^{-\int p}=t^3$, $\int\frac{t^3}{t^4}dt=\ln t$. ✓', diff='intermediate')


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
