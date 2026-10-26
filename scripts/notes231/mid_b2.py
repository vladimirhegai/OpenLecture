"""B2: first-order linear equations and the integrating factor (Week 3)."""
import sympy as sp

from midlib import P, S, TAGS, first, link, t, y, zero


def build(D):
    W3 = lambda *p: D.cite('W3', *p)
    D.H('B2 · Linear equations: the integrating factor', level=2, cites=W3(1, 2, 3))
    TAGS(D, (3, 2))
    D.P(r'**What if you can’t separate the variables?** Take $y\prime=t-y$. The right side is a sum, so it won’t split into a $t$-piece times a $y$-piece, and ' +
        link('B1', 'b1') + r' fails.')
    D.P(r'But it is **linear**: $y$ and $y\prime$ show up only to the first power (no $y^2$, no $\sin y$). '
        r'Every linear equation can be solved with an **integrating factor**.')
    D.P('First get it into this shape:')
    D.EQ(r'\dfrac{dy}{dt}+a(t)\,y=f(t)')
    D.L([r'$a(t)$ = whatever multiplies $y$, **sign included**',
         r'$f(t)$ = everything else, the part with no $y$ in it (called the forcing)'])
    D.P('Reading the form:')
    D.L([r'$y\prime=t-y$ → move $y$ left: $y\prime+y=t$. So $a=1$, $f=t$.',
         r'$ty\prime+2y=t^2$ → divide by $t$: $y\prime+\frac2t\,y=t$. So $a=\frac2t$, $f=t$.',
         r'$y\prime=(8t+3)y$ → move it left: $y\prime-(8t+3)y=0$. So $a=-(8t+3)$, $f=0$.'])
    D.CO('warning', r'**Get $y\prime$ alone first.** The number in front of $y\prime$ must be 1 before you read $a(t)$. '
         r'Example: in $ty\prime+2y=t^2$, divide by $t$ first. Then $a(t)=\frac2t$, not $2$.')

    D.P(r'**The trick.** Multiply the whole equation by a function $\mu(t)$, called the **integrating factor**:')
    D.EQ(r'\mu(t)=e^{\int a(t)\,dt}')
    D.P(r'Example: $y\prime+2y=4$ has $a=2$, so $\mu=e^{\int2\,dt}=e^{2t}$.')
    D.P(r'Why: after you multiply by this $\mu$, the left side is exactly one derivative, $(\mu y)\prime$ (the product rule backwards). So the equation becomes:')
    D.EQ(r'\dfrac{d}{dt}\big(\mu\,y\big)=\mu\,f')
    D.P('A single derivative is easy to undo. Integrate both sides:')
    D.EQ(r'\mu\,y=\int\mu\,f\,dt+C')
    D.P('**The method:**')
    D.L([r'**Standard form:** get $y\prime$ alone, then read $a(t)$ and $f(t)$.',
         r'**Integrating factor:** $\mu=e^{\int a\,dt}$. No $+C$ in this integral: any one $\mu$ works.',
         r'**Rewrite:** the equation becomes $(\mu y)\prime=\mu f$.',
         r'**Integrate:** $\mu y=\int\mu f\,dt+C$. This is where the $+C$ goes. Don’t forget it.',
         r'**Divide by $\mu$** to get $y$, then use the condition to find $C$.'],
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
        [r'$e^{\int\frac{k}{t}dt}$', r'$e^{k\ln t}=t^k$', r'for $t>0$, e.g. $a=\frac2t$ gives $\mu=t^2$; $a=-\frac1t$ gives $\mu=\frac1t$'],
        [r'$\int(2t+5)^5\,dt$', r'$\dfrac{(2t+5)^6}{12}$', r'substitution $u=2t+5$, $du=2\,dt$'],
        [r'$\int t\,e^{t}\,dt$', r'$(t-1)\,e^{t}$', r'integration by parts; check by differentiating'],
        [r'$\int t\,e^{t^2}dt$', r'$\tfrac12e^{t^2}$', r'substitution $u=t^2$'],
    ])
    D.CO('tip', r'**Shortcut when $a=k$ and $f=F$ are both constants:** $\;y=\dfrac{F}{k}+Ce^{-kt}$. '
         r'Example: $y\prime+2y=4$ gives $y=2+Ce^{-2t}$, same as the stepper. Every RC and RL circuit equation has this shape (see ' + link('D1', 'd1') + ').')
    D.CO('info', r'**Bonus (skip-safe): why does the integrating factor work?** The product rule says $(\mu y)\prime=\mu y\prime+\mu\prime y$. '
         r'With $\mu=e^{\int a\,dt}$, the chain rule gives $\mu\prime=a\,\mu$. So'
         '\n\n$$\n' r'(\mu y)\prime=\mu y\prime+a\mu y=\mu\,(y\prime+ay)' '\n$$\n\n'
         r'That’s $\mu$ times the left side of your equation. So multiplying by $\mu$ is exactly what turns $y\prime+ay$ into one derivative.')
    D.CO('info', r'**Both separable and linear?** Some equations are both. Then either method works, and separating is usually faster.'
         '\n\n'
         r'**When $f=0$:** $y\prime=(8t+3)y$ separates as $\dfrac{dy}{y}=(8t+3)\,dt$.'
         '\n\n'
         r'**When $a$ and $f$ are both constants:** $y\prime+2y=4$ separates as $\dfrac{dy}{4-2y}=dt$.')

    D.EX('W3 · A coefficient that varies with t · lecture Example 3.1',
         r'Solve $\dfrac{dy}{dt}+\dfrac{10\,y}{2t+5}=10$, $\;y(0)=0$.',
         [S(r'**Type:** linear, and $y\prime$ is already alone. So $a(t)=\dfrac{10}{2t+5}$ and $f(t)=10$.'),
          S(r'**Integrating factor:** $\int\frac{10}{2t+5}dt=5\ln(2t+5)$. Then $e^{5\ln(2t+5)}=(2t+5)^5$, same rule as $e^{k\ln t}=t^k$.', r'\mu=(2t+5)^5'),
          S(r'**Rewrite:** the left side is now one derivative, $(\mu y)\prime=\mu f$.', r'\dfrac{d}{dt}\big[(2t+5)^5y\big]=10(2t+5)^5'),
          S(r'**Integrate** the right side with $u=2t+5$, $du=2\,dt$: $\;10\int u^5\frac{du}{2}=\frac56u^6$.', r'(2t+5)^5y=\tfrac56(2t+5)^6+C'),
          S(r'**Condition** $y(0)=0$: $\;0=\frac56\cdot5^6+C$.', r'C=-\dfrac{5^7}{6}'),
          S(r'**Divide** by $(2t+5)^5$.', r'y=\tfrac56(2t+5)-\dfrac{5^7}{6(2t+5)^5}')],
         r'$y=\dfrac56(2t+5)-\dfrac{5^7}{6(2t+5)^5}$.', cites=W3(1, 2))

    P(D, 'W3 · The lecture’s RL equation · lecture §1.1',
      r'Solve $\dfrac{di}{dt}+5i=50$, $\;i(0)=0$ (the series RL circuit of the Week 3 lecture, $i$ in amperes).',
      [S(r'**Type:** linear, with constant $a=5$ and $f=50$.'),
       S(r'**Integrating factor:** $\mu=e^{5t}$. **Rewrite** the left side as one derivative.', r'\mu=e^{5t},\qquad \big(e^{5t}i\big)\prime=50e^{5t}'),
       S(r'**Integrate:** $\int50e^{5t}dt=10e^{5t}$.', r'e^{5t}i=10e^{5t}+C'),
       S(r'**Condition:** $0=10+C$, so $C=-10$. Then divide by $e^{5t}$.', r'i=10-10e^{-5t}')],
      r'$i(t)=10(1-e^{-5t})\,\mathrm{A}$. It starts at 0 and climbs toward 10 A. The shortcut gives the 10 straight away: $F/k=50/5$.', cites=W3(3))
    P(D, 'W3 · Linear and separable: solve it both ways · Pre-tutorial 3(c)',
      r'Find the general solution of $\dfrac{dy}{dt}=8ty+3y$ with an integrating factor, then check it by separating.',
      [S(r'**Type:** linear. Move the $y$ terms left: $y\prime-(8t+3)y=0$. So $a=-(8t+3)$ and $f=0$.'),
       S(r'**Integrating factor:** $\int-(8t+3)\,dt=-4t^2-3t$.', r'\mu=e^{-4t^2-3t}'),
       S(r'**Rewrite and integrate:** $f=0$, so the right side is 0 and integrates to just $C$.', r'\big(\mu y\big)\prime=0\quad\Rightarrow\quad e^{-4t^2-3t}y=C'),
       S(r'**Divide** by $\mu$.', r'y=Ce^{4t^2+3t}'),
       S(r'**Check by separating:** $\dfrac{dy}{y}=(8t+3)\,dt$ gives $\ln|y|=4t^2+3t+c$. Raise $e$ to both sides: $y=Ce^{4t^2+3t}$, the same answer.')],
      r'$y=Ce^{4t^2+3t}$.', cites=D.cite('T3', 1))
    P(D, 'W3 · An integral that needs parts',
      r'Solve $y\prime+y=t$, $\;y(0)=0$.',
      [S(r'**Type:** linear, $a=1$, $f=t$. It doesn’t separate: $y\prime=t-y$ is a sum.'),
       S(r'**Integrating factor:** $\mu=e^{t}$. **Rewrite** the left side as one derivative.', r'\mu=e^{t},\qquad\big(e^{t}y\big)\prime=te^{t}'),
       S(r'**Integrate** with the calculus table: $\int te^tdt=(t-1)e^t$.', r'e^{t}y=(t-1)e^{t}+C'),
       S(r'**Divide** by $e^t$.', r'y=t-1+Ce^{-t}'),
       S(r'**Condition:** $0=-1+C$, so $C=1$.', r'y=t-1+e^{-t}')],
      r'$y=t-1+e^{-t}$.', diff='intermediate')
    P(D, 'W3 · Divide first, then a power of t',
      r'Solve $t\,y\prime+2y=t^2$, $\;y(1)=0$, for $t>0$.',
      [S(r'**Type:** linear. Divide by $t$ so $y\prime$ is alone.', r"y'+\dfrac{2}{t}\,y=t"),
       S(r'**Integrating factor:** $e^{\int\frac2t dt}=e^{2\ln t}=t^2$. **Rewrite:** $(t^2y)\prime=t^2\cdot t$.', r'\big(t^2y\big)\prime=t^3'),
       S(r'**Integrate** each side.', r't^2y=\dfrac{t^4}{4}+C'),
       S(r'**Condition:** $0=\frac14+C$, so $C=-\frac14$. Then divide by $t^2$.', r'y=\dfrac{t^2}{4}-\dfrac{1}{4t^2}')],
      r'$y=\dfrac{t^2}{4}-\dfrac{1}{4t^2}$.', diff='intermediate')
    P(D, 'W3 · An integrating factor with t²',
      r'Solve $y\prime+2t\,y=t$, $\;y(0)=1$.',
      [S(r'**Type:** linear, $a=2t$, $f=t$.'),
       S(r'**Integrating factor:** $\int2t\,dt=t^2$, so $\mu=e^{t^2}$. **Rewrite** the left side as one derivative.', r'\mu=e^{t^2},\qquad\big(e^{t^2}y\big)\prime=te^{t^2}'),
       S(r'**Integrate** with $u=t^2$: $\int te^{t^2}dt=\frac12e^{t^2}$.', r'e^{t^2}y=\tfrac12e^{t^2}+C'),
       S(r'**Divide** by $e^{t^2}$.', r'y=\tfrac12+Ce^{-t^2}'),
       S(r'**Condition:** $1=\frac12+C$, so $C=\frac12$.', r'y=\tfrac12+\tfrac12e^{-t^2}')],
      r'$y=\dfrac12\big(1+e^{-t^2}\big)$. It also separates, $y\prime=t(1-2y)$, so you could check it with ' + link('B1', 'b1') + '.', diff='advanced')


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
