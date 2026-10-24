"""B2: first-order linear equations and the integrating factor (Week 3)."""
import sympy as sp

from midlib import P, S, TAGS, first, link, t, y, zero


def build(D):
    W3 = lambda *p: D.cite('W3', *p)
    D.H('B2 · Linear equations: the integrating factor', level=2, cites=W3(1, 2, 3))
    TAGS(D, (3, 2))
    D.P(r'**What if you can’t separate the variables?** $\dfrac{dy}{dt}=t-y$ won’t split into ($t$-part)×($y$-part), so ' + link('B1', 'b1') +
        r' fails. But if the equation is **linear**, an integrating factor solves it every time.')
    D.P('First-order linear equations can be written as:')
    D.EQ(r'\dfrac{dy}{dt}+a(t)\,y=f(t)')
    D.L([r'$a(t)$ = the coefficient of $y$: everything multiplying $y$, **sign included**',
         r'$f(t)$ = the forcing: everything left over, with no $y$ in it'])
    D.P(r'Examples:')
    D.L([r'$y\prime=t-y$ → move $y$ left: $y\prime+y=t$. So $a(t)=1$, $f(t)=t$.',
         r'$ty\prime+2y=t^2$ → divide by $t$: $y\prime+\frac2t\,y=t$. So $a(t)=\frac2t$, $f(t)=t$.',
         r'$y\prime=(8t+3)y$ → $y\prime-(8t+3)y=0$. So $a(t)=-(8t+3)$, $f(t)=0$.'])
    D.CO('warning', r'Get $y\prime$ **alone** first (coefficient 1). Read $a(t)$ only after dividing: in $ty\prime+2y=t^2$, $a(t)$ is $\frac2t$, not $2$.')

    D.P(r'**The integrating factor.** An integrating factor is a special function $\mu(t)$ that we multiply the entire equation by, '
        r'to turn its left side into **one derivative**. The formula is:')
    D.EQ(r'\mu(t)=e^{\int a(t)\,dt}')
    D.P(r'After multiplying by $\mu$, the left side is exactly $(\mu y)\prime$, so the equation becomes:')
    D.EQ(r'\dfrac{d}{dt}\big(\mu\,y\big)=\mu\,f')
    D.P('Integrate both sides:')
    D.EQ(r'\mu\,y=\int\mu\,f\,dt+C')
    D.P('**Method:**')
    D.L([r'**Standard form:** get $y\prime$ alone; read $a(t)$ and $f(t)$.',
         r'**Integrating factor:** $\mu=e^{\int a\,dt}$. Leave out the $+C$ in this integral.',
         r'**Rewrite:** $(\mu y)\prime=\mu f$.',
         r'**Integrate:** $\mu y=\int\mu f\,dt+C$. This is where the constant goes; don’t forget it.',
         r'**Divide by $\mu$**, then use the condition to find $C$.'],
        ordered=True)
    D.STEPS('The method on y′ + 2y = 4', [
        (r"y'+2y=4", r'Standard form already: $a=2$, $f=4$.'),
        (r'\mu=e^{\int2\,dt}=\hl{e^{2t}}', 'Integrating factor.'),
        (r"\hl{e^{2t}}y'+\hl{2e^{2t}}y=\hl{4e^{2t}}", r'Multiply every term by $\mu$.'),
        (r'\hl{\big(e^{2t}y\big)\prime}=4e^{2t}', 'The left side is one derivative (product rule backwards).'),
        (r'e^{2t}y=2e^{2t}+\hl{C}', r'Integrate both sides: $\int4e^{2t}dt=2e^{2t}$.'),
        (r'y=2+Ce^{-2t}', r'Divide by $e^{2t}$.'),
    ])
    D.P('**Calculus you need here:**')
    D.T(['Expression', 'Result', 'Note'], [
        [r'$e^{\int k\,dt}$', r'$e^{kt}$', r'constant $a(t)=k$'],
        [r'$e^{\int\frac{k}{t}dt}$', r'$e^{k\ln t}=t^k$', r'e.g. $a=\frac2t$ gives $\mu=t^2$; $a=-\frac1t$ gives $\mu=\frac1t$'],
        [r'$\int(2t+5)^5\,dt$', r'$\dfrac{(2t+5)^6}{12}$', r'substitution $u=2t+5$, $du=2\,dt$'],
        [r'$\int t\,e^{t}\,dt$', r'$(t-1)\,e^{t}$', r'integration by parts; check by differentiating'],
        [r'$\int t\,e^{t^2}dt$', r'$\tfrac12e^{t^2}$', r'substitution $u=t^2$'],
    ])
    D.CO('tip', r'**Shortcut for constant $a=k$ and constant $f=F$:** $\;y=\dfrac{F}{k}+Ce^{-kt}$. Every RC and RL circuit equation has this shape (see ' + link('D1', 'd1') + ').')
    D.CO('info', r'**Bonus (skip-safe): why does the integrating factor work?** Recall the **product rule** from calculus: $(\mu y)\prime=\mu y\prime+\mu\prime y$. '
         r'With $\mu=e^{\int a\,dt}$, the chain rule gives $\mu\prime=a\,\mu$. So'
         '\n\n$$\n' r'(\mu y)\prime=\mu y\prime+a\mu y=\mu\,(y\prime+ay)' '\n$$\n\n'
         r'which is exactly $\mu$ times the left side of the equation. Multiplying by $\mu$ turns “$y\prime+ay$” into a single derivative you can integrate.')
    D.CO('info', r'**Both separable and linear?** For example $y\prime=(8t+3)y$, or any equation with constant $a$ and $f$. Then either method works: separating is usually faster.')

    D.EX('W3 · A coefficient that varies with t · lecture Example 3.1',
         r'Solve $\dfrac{dy}{dt}+\dfrac{10\,y}{2t+5}=10$, $\;y(0)=0$.',
         [S(r'**Type:** linear, $y\prime$ already alone. $a(t)=\dfrac{10}{2t+5}$, $f(t)=10$.'),
          S(r'**Integrating factor:** $\int\frac{10}{2t+5}dt=5\ln(2t+5)$, and $e^{5\ln(2t+5)}=(2t+5)^5$.', r'\mu=(2t+5)^5'),
          S(r'**Rewrite:** $(\mu y)\prime=\mu f$.', r'\dfrac{d}{dt}\big[(2t+5)^5y\big]=10(2t+5)^5'),
          S(r'**Integrate** with $u=2t+5$, $du=2\,dt$: $\;10\int u^5\frac{du}{2}=\frac56u^6$.', r'(2t+5)^5y=\tfrac56(2t+5)^6+C'),
          S(r'**Condition** $y(0)=0$: $\;0=\frac56\cdot5^6+C$.', r'C=-\dfrac{5^7}{6}'),
          S(r'**Divide** by $(2t+5)^5$.', r'y=\tfrac56(2t+5)-\dfrac{5^7}{6(2t+5)^5}')],
         r'$y=\dfrac56(2t+5)-\dfrac{5^7}{6(2t+5)^5}$.', cites=W3(1, 2))

    P(D, 'W3 · The lecture’s RL equation · lecture §1.1',
      r'Solve $\dfrac{di}{dt}+5i=50$, $\;i(0)=0$ (the series RL circuit of the Week 3 lecture, $i$ in amperes).',
      [S(r'**Type:** linear with constant $a=5$, $f=50$.'),
       S(r'**Integrating factor** and rewrite.', r'\mu=e^{5t},\qquad \big(e^{5t}i\big)\prime=50e^{5t}'),
       S(r'**Integrate:** $\int50e^{5t}dt=10e^{5t}$.', r'e^{5t}i=10e^{5t}+C'),
       S(r'**Condition:** $0=10+C$, so $C=-10$. Divide by $e^{5t}$.', r'i=10-10e^{-5t}')],
      r'$i(t)=10(1-e^{-5t})\,\mathrm{A}$. It rises from 0 towards 10 A (the shortcut: $F/k=50/5=10$).', cites=W3(3))
    P(D, 'W3 · Linear and separable: solve it both ways · Pre-tutorial 3(c)',
      r'Find the general solution of $\dfrac{dy}{dt}=8ty+3y$ with an integrating factor, then check it by separating.',
      [S(r'**Type:** linear. Standard form: $y\prime-(8t+3)y=0$, so $a=-(8t+3)$, $f=0$.'),
       S(r'**Integrating factor:** $\int-(8t+3)\,dt=-4t^2-3t$.', r'\mu=e^{-4t^2-3t}'),
       S(r'**Rewrite and integrate:** $f=0$, so the right side integrates to just $C$.', r'\big(\mu y\big)\prime=0\quad\Rightarrow\quad e^{-4t^2-3t}y=C'),
       S(r'**Divide** by $\mu$.', r'y=Ce^{4t^2+3t}'),
       S(r'**Check by separating:** $\dfrac{dy}{y}=(8t+3)\,dt$ gives $\ln|y|=4t^2+3t+c$, the same family.')],
      r'$y=Ce^{4t^2+3t}$.', cites=D.cite('T3', 1))
    P(D, 'W3 · An integral that needs parts',
      r'Solve $y\prime+y=t$, $\;y(0)=0$.',
      [S(r'**Type:** linear, $a=1$, $f=t$. Not separable ($t-y$ is a sum).'),
       S(r'**Integrating factor** and rewrite.', r'\mu=e^{t},\qquad\big(e^{t}y\big)\prime=te^{t}'),
       S(r'**Integrate** with the calculus table: $\int te^tdt=(t-1)e^t$.', r'e^{t}y=(t-1)e^{t}+C'),
       S(r'Divide by $e^t$.', r'y=t-1+Ce^{-t}'),
       S(r'**Condition:** $0=-1+C$, so $C=1$.', r'y=t-1+e^{-t}')],
      r'$y=t-1+e^{-t}$.', diff='intermediate')
    P(D, 'W3 · Divide first, then a power of t',
      r'Solve $t\,y\prime+2y=t^2$, $\;y(1)=0$, for $t>0$.',
      [S(r'**Type:** linear. Divide by $t$ to get $y\prime$ alone.', r"y'+\dfrac{2}{t}\,y=t"),
       S(r'**Integrating factor:** $e^{\int\frac2t dt}=e^{2\ln t}=t^2$.', r'\big(t^2y\big)\prime=t^3'),
       S(r'**Integrate.**', r't^2y=\dfrac{t^4}{4}+C'),
       S(r'**Condition:** $0=\frac14+C$, so $C=-\frac14$. Divide by $t^2$.', r'y=\dfrac{t^2}{4}-\dfrac{1}{4t^2}')],
      r'$y=\dfrac{t^2}{4}-\dfrac{1}{4t^2}$.', diff='intermediate')
    P(D, 'W3 · An integrating factor with t²',
      r'Solve $y\prime+2t\,y=t$, $\;y(0)=1$.',
      [S(r'**Type:** linear, $a=2t$, $f=t$.'),
       S(r'**Integrating factor:** $\int2t\,dt=t^2$.', r'\mu=e^{t^2},\qquad\big(e^{t^2}y\big)\prime=te^{t^2}'),
       S(r'**Integrate** with $u=t^2$: $\int te^{t^2}dt=\frac12e^{t^2}$.', r'e^{t^2}y=\tfrac12e^{t^2}+C'),
       S(r'Divide by $e^{t^2}$.', r'y=\tfrac12+Ce^{-t^2}'),
       S(r'**Condition:** $1=\frac12+C$, so $C=\frac12$.', r'y=\tfrac12+\tfrac12e^{-t^2}')],
      r'$y=\dfrac12\big(1+e^{-t^2}\big)$. (It is also separable: $y\prime=t(1-2y)$.)', diff='advanced')


def verify():
    C = sp.symbols('C')
    first(2 + C * sp.exp(-2 * t), 4 - 2 * y)
    ys = sp.Rational(5, 6) * (2 * t + 5) - 5 ** 7 / (6 * (2 * t + 5) ** 5)
    first(ys, 10 - 10 * y / (2 * t + 5), (0, 0))
    first(10 - 10 * sp.exp(-5 * t), 50 - 5 * y, (0, 0))
    first(C * sp.exp(4 * t ** 2 + 3 * t), 8 * t * y + 3 * y)
    first(t - 1 + sp.exp(-t), t - y, (0, 0))
    first(t ** 2 / 4 - 1 / (4 * t ** 2), (t ** 2 - 2 * y) / t, (1, 0))
    first((1 + sp.exp(-t ** 2)) / 2, t - 2 * t * y, (0, 1))
    zero(sp.diff((t - 1) * sp.exp(t), t) - t * sp.exp(t))
    zero(sp.diff((2 * t + 5) ** 6 / 12, t) - (2 * t + 5) ** 5)
