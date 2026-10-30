"""B2: first-order linear equations and the integrating factor (Week 3).

Layout (REWRITE_PLAN.md). Shared letters: y' + p(t) y = f(t) (p = what multiplies y once y' stands alone,
f = the right side, the same p and f as B6/B7/C2), mu = the integrating factor (also B4), C = the constant.
Step words: Write, Find mu, Multiply, Integrate, Divide, Plug in.
"""
import sympy as sp

from midlib import CARD, P, S, TAGS, first, link, t, y, zero


def build(D):
    W3 = lambda *p: D.cite('W3', *p)
    D.H('B2 · Linear first order: the integrating factor', level=2, cites=W3(1, 2, 3))
    TAGS(D, (3, 2))
    D.P(r'**Use this when** it won’t separate, but $y$ and $y\prime$ only appear to the power 1:')
    D.EQ(r'y\prime+2y=4')
    D.P(r'Every linear first-order equation can be written like this:')
    D.EQ(r'y\prime+p(t)\,y=f(t)')
    D.L([r'$p(t)$ = what multiplies $y$, **sign included**, once $y\prime$ stands alone',
         r'$f(t)$ = the right side: everything with no $y$ in it'])
    D.P('**Short examples:**')
    D.EQ(r'y\prime=t-y\quad\Longrightarrow\quad y\prime+y=t\quad\Longrightarrow\quad p=1,\quad f=t')
    D.EQ(r'ty\prime+2y=t^2\quad\Longrightarrow\quad y\prime+\tfrac2t\,y=t\quad\Longrightarrow\quad p=\tfrac2t,\quad f=t')
    D.P(r'In the second one you **divide by $t$ first**, so $y\prime$ stands alone.')

    D.P(r'**The move: multiply everything by $\mu$.** Then the left side becomes one derivative, and you just integrate.')
    D.EQ(r'\mu=e^{\int p\,dt}')
    D.P(r'After multiplying, the equation always turns into:')
    D.EQ(r'(\mu\,y)\prime=\mu\,f')
    D.P('**Steps**')
    D.L([r'**Write** it as $y\prime+p(t)\,y=f(t)$. Divide first if something multiplies $y\prime$. Read $p$ and $f$.',
         r'**Find $\mu$** $=e^{\int p\,dt}$. No $+C$ here: any one $\mu$ works.',
         r'**Multiply** everything by $\mu$. The left side becomes $(\mu y)\prime$, so you get $(\mu y)\prime=\mu f$.',
         r'**Integrate** both sides: $\mu y=\int\mu f\,dt+C$. **This** is where the $+C$ goes.',
         r'**Divide** by $\mu$ to get $y$.',
         r'**Plug in** the condition to find $C$.'], ordered=True)
    D.P('**Short example:**')
    D.EQ(r'y\prime+2y=4\quad\Longrightarrow\quad \mu=e^{2t}\quad\Longrightarrow\quad (e^{2t}y)\prime=4e^{2t}')
    CARD(D, r'Full example: $\;y\prime+2y=4$, $\;y(0)=0$',
         [(r'**Write:** $y\prime$ is already alone.', r'p=2,\qquad f=4'),
          (r'**Find $\mu$.**', r'\mu=e^{\int2\,dt}=e^{2t}'),
          (r'**Multiply** every term by $e^{2t}$. The left side is now one derivative (the product rule backwards).',
           (r'e^{2t}y\prime+2e^{2t}y=4e^{2t}', r'(e^{2t}y)\prime=4e^{2t}')),
          (r'**Integrate** both sides: $\int4e^{2t}\,dt=2e^{2t}$.', r'e^{2t}y=2e^{2t}+C'),
          (r'**Divide** by $e^{2t}$.', r'y=2+Ce^{-2t}'),
          (r'**Plug in** $y(0)=0$.', r'0=2+C\quad\Rightarrow\quad C=-2')],
         r'y=2-2e^{-2t}')
    CARD(D, r'★ Lecture Example 3.1 (try it, then open): $\;y\prime+\dfrac{10\,y}{2t+5}=10$, $\;y(0)=0$',
         [(r'**Write:** $y\prime$ is already alone.', r'p=\dfrac{10}{2t+5},\qquad f=10'),
          (r'**Find $\mu$:** $\int\frac{10}{2t+5}dt=5\ln(2t+5)$, and $e^{5\ln(2t+5)}=(2t+5)^5$ (card “$e$ and $\ln$ cancel”).',
           r'\mu=(2t+5)^5'),
          (r'**Multiply:** the left side becomes $(\mu y)\prime$.', r'\big[(2t+5)^5y\big]\prime=10(2t+5)^5'),
          (r'**Integrate** with $u=2t+5$, $du=2\,dt$: $\;10\int u^5\,\frac{du}{2}=\frac56u^6$.', r'(2t+5)^5y=\tfrac56(2t+5)^6+C'),
          (r'**Divide** by $(2t+5)^5$.', r'y=\tfrac56(2t+5)+\dfrac{C}{(2t+5)^5}'),
          (r'**Plug in** $y(0)=0$.', (r'0=\tfrac56\cdot5+\dfrac{C}{5^5}', r'C=-\dfrac{5^7}{6}'))],
         r'y=\tfrac56(2t+5)-\dfrac{5^7}{6(2t+5)^5}')

    D.P('**Calculus that shows up.** Open a card for an example:')
    CARD(D, r'$e$ and $\ln$ cancel: $\;e^{\int\frac{k}{t}dt}=e^{k\ln t}=t^k$',
         [(r'$p=\frac2t$:', r'\mu=e^{2\ln t}=t^2'),
          (r'$p=-\frac1t$:', r'\mu=e^{-\ln t}=\dfrac1t')])
    CARD(D, r'Constant $p$: $\;e^{\int k\,dt}=e^{kt}$',
         [(r'$p=5$:', r'\mu=e^{5t}')])
    D.CO('tip', r'**Shortcut when $p=k$ and $f=F$ are both plain numbers:** $\;y=\dfrac{F}{k}+Ce^{-kt}$. '
         r'Example: $y\prime+2y=4$ gives $y=2+Ce^{-2t}$. Every RC and RL circuit has this shape (' + link('D1', 'd1') + ').')
    D.CO('warning', r'**Get $y\prime$ alone first.** In $ty\prime+2y=t^2$, divide by $t$ first. Then $p=\frac2t$, not $2$.')
    D.CO('warning', r'**Multiply the right side by $\mu$ too.** It’s $\int\mu f\,dt$, not $\int f\,dt$.')
    D.CO('tip', r'**Both separable and linear?** Either method works (the prof solves the RL circuit $i\prime+5i=50$ both ways). '
         r'Happens when $f=0$, or when $p$ and $f$ are plain numbers: $\;\dfrac{di}{50-5i}=dt$.')

    D.H('Practice: B2', level=3)
    P(D, '★ W3 · The lecture’s RL equation · lecture §1.1',
      r'Solve $\dfrac{di}{dt}+5i=50$, $\;i(0)=0$ (the series RL circuit of the Week 3 lecture, $i$ in amperes).',
      [S(r'**Type:** linear → B2. Here the unknown is $i$ instead of $y$.'),
       S(r'**Write:** $i\prime$ is already alone.', r'p=5,\qquad f=50'),
       S(r'**Find $\mu$.**', r'\mu=e^{5t}'),
       S(r'**Multiply:** the left side becomes one derivative.', r'(e^{5t}i)\prime=50e^{5t}'),
       S(r'**Integrate:** $\int50e^{5t}\,dt=10e^{5t}$.', r'e^{5t}i=10e^{5t}+C'),
       S(r'**Divide** by $e^{5t}$.', r'i=10+Ce^{-5t}'),
       S(r'**Plug in** $i(0)=0$.', r'0=10+C\quad\Rightarrow\quad C=-10')],
      r'$i(t)=10(1-e^{-5t})\,\mathrm{A}$. It climbs from 0 to 10 A. The shortcut gives the 10 straight away: $F/k=50/5$.', cites=W3(3))
    P(D, '★ W3 · Linear and separable: solve it both ways · Pre-tutorial 3(c)',
      r'Find the general solution of $\dfrac{dy}{dt}=8ty+3y$ with an integrating factor, then check it by separating.',
      [S(r'**Type:** linear → B2.'),
       S(r'**Write:** move the $y$ terms left.', (r'y\prime-(8t+3)\,y=0', r'p=-(8t+3),\qquad f=0')),
       S(r'**Find $\mu$:** $\int-(8t+3)\,dt=-4t^2-3t$.', r'\mu=e^{-4t^2-3t}'),
       S(r'**Multiply:** $f=0$, so the right side is $0$.', r'(\mu y)\prime=0'),
       S(r'**Integrate:** the integral of $0$ is just $C$.', r'e^{-4t^2-3t}\,y=C'),
       S(r'**Divide** by $\mu$.', r'y=Ce^{4t^2+3t}'),
       S(r'**Check by separating** (B1): $\dfrac{dy}{y}=(8t+3)\,dt$ gives $\ln|y|=4t^2+3t+C$, so $y=Ce^{4t^2+3t}$. Same answer.')],
      r'$y=Ce^{4t^2+3t}$.', cites=D.cite('T3', 1))
    P(D, 'W3 · Divide first, then a power of t',
      r'Solve $t\,y\prime+2y=t^2$, $\;y(1)=0$, for $t>0$.',
      [S(r'**Type:** linear → B2.'),
       S(r'**Write:** divide by $t$ so $y\prime$ stands alone.', (r'y\prime+\dfrac{2}{t}\,y=t', r'p=\dfrac2t,\qquad f=t')),
       S(r'**Find $\mu$:** $e$ and $\ln$ cancel.', r'\mu=e^{\int\frac2t dt}=e^{2\ln t}=t^2'),
       S(r'**Multiply:** $\mu f=t^2\cdot t$.', r'(t^2y)\prime=t^3'),
       S(r'**Integrate.**', r't^2y=\dfrac{t^4}{4}+C'),
       S(r'**Divide** by $t^2$.', r'y=\dfrac{t^2}{4}+\dfrac{C}{t^2}'),
       S(r'**Plug in** $y(1)=0$.', r'0=\tfrac14+C\quad\Rightarrow\quad C=-\tfrac14')],
      r'$y=\dfrac{t^2}{4}-\dfrac{1}{4t^2}$.', diff='intermediate')
def verify():
    C = sp.symbols('C')
    first(2 + C * sp.exp(-2 * t), 4 - 2 * y)
    first(2 - 2 * sp.exp(-2 * t), 4 - 2 * y, (0, 0))
    ys = sp.Rational(5, 6) * (2 * t + 5) - 5 ** 7 / (6 * (2 * t + 5) ** 5)
    first(ys, 10 - 10 * y / (2 * t + 5), (0, 0))
    first(10 - 10 * sp.exp(-5 * t), 50 - 5 * y, (0, 0))
    first(C * sp.exp(4 * t ** 2 + 3 * t), 8 * t * y + 3 * y)
    first(t ** 2 / 4 - 1 / (4 * t ** 2), (t ** 2 - 2 * y) / t, (1, 0))
    zero(sp.diff((2 * t + 5) ** 6 / 12, t) - (2 * t + 5) ** 5)
