"""B4: make a non-exact equation exact with an integrating factor (Week 4).

Layout (REWRITE_PLAN.md). Shared letters: M, N, U, h(y) from B3; g(t) / h(y) = a ratio with only t / only y
(as in B1); mu = the integrating factor (as in B2). Step words: Write, Test, Find mu (Case 1 / Case 2), Multiply,
Re-test, then the B3 steps, Plug in.
"""
import sympy as sp

from midlib import CARD, P, S, TAGS, implicit, link, t, y, zero


def build(D):
    W4 = lambda *p: D.cite('W4', *p)
    D.H('B4 · Not exact: make it exact with μ', level=2, cites=W4(4, 5))
    TAGS(D, (4, 3))
    D.P(r'**Use this when** it’s written with $dt$ and $dy$, but the ' + link('B3', 'b3') + r' test **fails**:')
    D.EQ(r'y\,dt+(3+3t-y)\,dy=0\qquad M_y=1\neq3=N_t')
    D.P(r'**The move: multiply everything by a factor $\mu$** that makes it pass the test. Then finish it like ' + link('B3', 'b3') + '.')
    D.P(r'Same idea as $\mu$ in ' + link('B2', 'b2') + r': multiply by the right thing and the equation becomes easy.')
    D.P(r'To find $\mu$, start from the mismatch $M_y-N_t$ and try two ratios. One of them should have **only one letter** left.')

    D.H('Case 1: only t left', level=3)
    D.P(r'Divide the mismatch by $N$. If only $t$ is left, call it $g(t)$:')
    D.EQ(r'\dfrac{M_y-N_t}{N}=g(t)\quad\Longrightarrow\quad \mu=e^{\int g\,dt}')
    D.P(r'**Short example:** $(t^2+y)\,dt-t\,dy=0$:')
    D.EQ(r'\dfrac{1-(-1)}{-t}=-\dfrac2t\quad\Longrightarrow\quad \mu=e^{-2\ln t}=\dfrac{1}{t^2}')

    D.H('Case 2: only y left', level=3)
    D.P(r'Flip the subtraction and divide by $M$. If only $y$ is left, call it $h(y)$:')
    D.EQ(r'\dfrac{N_t-M_y}{M}=h(y)\quad\Longrightarrow\quad \mu=e^{\int h\,dy}')
    D.P(r'**Short example:** $y\,dt+(3+3t-y)\,dy=0$:')
    D.EQ(r'\dfrac{3-1}{y}=\dfrac2y\quad\Longrightarrow\quad \mu=e^{2\ln y}=y^2')
    D.P(r'(The lecture calls these Theorem 1 and Theorem 2.)', cites=W4(5))
    D.WHY('Where does Case 1 come from?',
          r'Multiply by $\mu(t)$ and ask the new equation to pass the test, $(\mu M)_y=(\mu N)_t$. '
          r'On the left, $\mu$ has no $y$, so it just comes out. On the right, use the product rule:'
          '\n\n$$\n' r'\mu\,M_y=\mu\prime N+\mu\,N_t\quad\Longrightarrow\quad \dfrac{\mu\prime}{\mu}=\dfrac{M_y-N_t}{N}' '\n$$\n\n'
          r'The left side only has $t$, so the right side must too. Then $\ln\mu=\int g\,dt$. Case 2 is the same with $\mu(y)$.')

    D.H('Steps and examples', level=3)
    D.L([r'**Write** it as $M\,dt+N\,dy=0$. Read $M$ and $N$ with their signs.',
         r'**Test:** $M_y\neq N_t$. (Equal? It’s already exact: ' + link('B3', 'b3') + '.)',
         r'**Find $\mu$:** try Case 1, then Case 2. Keep the ratio with only one letter. No $+C$ in this integral.',
         r'**Multiply** the whole equation by $\mu$: both $M$ and $N$.',
         r'**Re-test:** it must pass now. If not, recheck your algebra.',
         r'**Finish like B3:** integrate $M$ in $t$, match $N$, answer $U=C$, plug in.'], ordered=True)
    CARD(D, r'Full example (Pre-tutorial 4): $\;y\,dt+(3+3t-y)\,dy=0$',
         [(r'**Write.**', r'M=y,\qquad N=3+3t-y'),
          (r'**Test:** they don’t match.', r'M_y=1,\qquad N_t=3'),
          (r'**Find $\mu$:** Case 1 gives $\frac{1-3}{3+3t-y}$, both letters. Case 2 leaves only $y$.', r'\dfrac{N_t-M_y}{M}=\dfrac{3-1}{y}=\dfrac2y'),
          (r'$e$ and $\ln$ cancel: $e^{2\ln y}=y^2$.', r'\mu=e^{\int\frac2y\,dy}=y^2'),
          (r'**Multiply** the whole equation by $y^2$.', r'y^3\,dt+(3y^2+3ty^2-y^3)\,dy=0'),
          (r'**Re-test:** now $M=y^3$ and $N=3y^2+3ty^2-y^3$.', r'M_y=3y^2,\qquad N_t=3y^2\quad\checkmark'),
          (r'**Integrate $M$ in $t$** ($y$ is a number).', r'U=ty^3+h(y)'),
          (r'**Match $N$.**', (r'U_y=3ty^2+h\prime(y)=3y^2+3ty^2-y^3', r'h\prime=3y^2-y^3\quad\Rightarrow\quad h=y^3-\tfrac14y^4')),
          (r'**Answer:** $U=C$.', r'ty^3+y^3-\tfrac14y^4=C')],
         r'ty^3+y^3-\dfrac{y^4}{4}=C')
    CARD(D, r'Full example (Case 1): $\;(t^2+y)\,dt-t\,dy=0$, $\;t>0$',
         [(r'**Write.**', r'M=t^2+y,\qquad N=-t'),
          (r'**Test.**', r'M_y=1,\qquad N_t=-1'),
          (r'**Find $\mu$:** Case 1 leaves only $t$.', (r'\dfrac{M_y-N_t}{N}=\dfrac{1-(-1)}{-t}=-\dfrac2t', r'\mu=e^{-2\ln t}=\dfrac{1}{t^2}')),
          (r'**Multiply** by $\frac{1}{t^2}$.', r'\Big(1+\dfrac{y}{t^2}\Big)dt-\dfrac1t\,dy=0'),
          (r'**Re-test.**', r'M_y=\dfrac{1}{t^2},\qquad N_t=\dfrac{1}{t^2}\quad\checkmark'),
          (r'**Integrate $M$ in $t$:** $\int1\,dt=t$ and $\int\frac{y}{t^2}dt=-\frac yt$.', r'U=t-\dfrac{y}{t}+h(y)'),
          (r'**Match $N$:** $U_y=-\frac1t+h\prime$ must equal $-\frac1t$.', r'h\prime=0'),
          (r'**Answer.**', r't-\dfrac yt=C')],
         r't-\dfrac yt=C\qquad(y=t^2-Ct)')
    CARD(D, r'$e$ and $\ln$ cancel: $\;e^{\int\frac{k}{y}dy}=y^k$, $\;e^{\int\frac{k}{t}dt}=t^k$',
         [(r'$h=\frac2y$:', r'\mu=e^{2\ln y}=y^2'),
          (r'$h=-\frac1y$:', r'\mu=e^{-\ln y}=\dfrac1y'),
          (r'$g=-\frac2t$:', r'\mu=e^{-2\ln t}=\dfrac{1}{t^2}')])
    D.CO('warning', r'**The two ratios are different.** Case 1: $M_y-N_t$ over $N$. Case 2: $N_t-M_y$ (flipped) over $M$. Mix them up and the sign of $\mu$’s power flips.')

    D.H('Practice: B4', level=3)
    P(D, 'W4 · A factor in y only',
      r'Solve $y\,dt+(2t+y^3)\,dy=0$.',
      [S(r'**Type:** $dt$, $dy$ form → test for B3.'),
       S(r'**Write.**', r'M=y,\qquad N=2t+y^3'),
       S(r'**Test:** not exact → B4.', r'M_y=1,\qquad N_t=2'),
       S(r'**Find $\mu$:** Case 1 gives $\frac{-1}{2t+y^3}$, both letters. Case 2 leaves only $y$.', (r'\dfrac{N_t-M_y}{M}=\dfrac{2-1}{y}=\dfrac1y', r'\mu=e^{\ln y}=y')),
       S(r'**Multiply** by $y$.', r'y^2\,dt+(2ty+y^4)\,dy=0'),
       S(r'**Re-test.**', r'M_y=2y,\qquad N_t=2y\quad\checkmark'),
       S(r'**Integrate $M$ in $t$.**', r'U=ty^2+h(y)'),
       S(r'**Match $N$:** $U_y=2ty+h\prime$ must equal $2ty+y^4$.', r'h\prime=y^4\quad\Rightarrow\quad h=\dfrac{y^5}{5}'),
       S(r'**Answer.**', r'ty^2+\dfrac{y^5}{5}=C')],
      r'$ty^2+\dfrac{y^5}{5}=C$.')
    P(D, 'W4 · Which case applies?',
      r'Find an integrating factor for each equation, then solve it.' '\n\n'
      r'(a) $(2y+3t)\,dt+t\,dy=0$' '\n\n'
      r'(b) $y^2\,dt+(ty+1)\,dy=0$',
      [S(r'(a) **Write** and **test:** $M=2y+3t$, $N=t$.', r'M_y=2,\qquad N_t=1'),
       S(r'(a) **Find $\mu$:** Case 1 leaves only $t$.', (r'\dfrac{M_y-N_t}{N}=\dfrac{2-1}{t}=\dfrac1t', r'\mu=e^{\ln t}=t')),
       S(r'(a) **Multiply** by $t$: it’s exactly the B3 lecture example.', r'(2ty+3t^2)\,dt+t^2\,dy=0'),
       S(r'(a) **Answer:** from B3.', r't^2y+t^3=C'),
       S(r'(b) **Write** and **test:** $M=y^2$, $N=ty+1$.', r'M_y=2y,\qquad N_t=y'),
       S(r'(b) **Find $\mu$:** Case 1 gives $\frac{y}{ty+1}$, both letters. Case 2:', (r'\dfrac{N_t-M_y}{M}=\dfrac{y-2y}{y^2}=-\dfrac1y', r'\mu=e^{-\ln y}=\dfrac1y')),
       S(r'(b) **Multiply** by $\frac1y$ and **re-test.**', (r'y\,dt+\Big(t+\dfrac1y\Big)dy=0', r'M_y=1,\qquad N_t=1\quad\checkmark')),
       S(r'(b) **Integrate $M$** and **match $N$:** $U=ty+h(y)$, and $U_y=t+h\prime$ must equal $t+\frac1y$.', r'h\prime=\dfrac1y\quad\Rightarrow\quad h=\ln|y|'),
       S(r'(b) **Answer.**', r'ty+\ln|y|=C')],
      r'(a) $\mu=t$, $\;t^2y+t^3=C$. (b) $\mu=\dfrac1y$, $\;ty+\ln|y|=C$.', diff='advanced')


def verify():
    def exact(M, N):
        zero(sp.diff(M, y) - sp.diff(N, t))

    # lecture (e) / Pre-tutorial 4
    M, N = y, 3 + 3 * t - y
    assert sp.diff(M, y) != sp.diff(N, t)
    assert sp.simplify((sp.diff(M, y) - sp.diff(N, t)) / N).has(y)
    zero(sp.simplify((sp.diff(N, t) - sp.diff(M, y)) / M) - 2 / y)
    exact(y ** 2 * M, y ** 2 * N)
    implicit(t * y ** 3 + y ** 3 - y ** 4 / 4, -M / N)
    # factor in t only
    tp = sp.symbols('tp', positive=True)
    M, N = t ** 2 + y, -t
    g = sp.simplify((sp.diff(M, y) - sp.diff(N, t)) / N)
    zero(g + 2 / t)
    zero(sp.exp(sp.integrate(g.subs(t, tp), tp)) - 1 / tp ** 2)
    exact(M / t ** 2, N / t ** 2)
    implicit(t - y / t, -M / N)
    C = sp.symbols('C')
    zero(sp.diff(t ** 2 - C * t, t) - (t ** 2 - C * t) / t - t)
    # factor in y only
    M, N = y, 2 * t + y ** 3
    zero(sp.simplify((sp.diff(N, t) - sp.diff(M, y)) / M) - 1 / y)
    exact(y * M, y * N)
    implicit(t * y ** 2 + y ** 5 / 5, -M / N)
    # which case
    M, N = 2 * y + 3 * t, t
    zero(sp.simplify((sp.diff(M, y) - sp.diff(N, t)) / N) - 1 / t)
    assert sp.simplify((sp.diff(N, t) - sp.diff(M, y)) / M).has(t)
    exact(t * M, t * N)
    implicit(t ** 2 * y + t ** 3, -M / N)
    M, N = y ** 2, t * y + 1
    assert sp.simplify((sp.diff(M, y) - sp.diff(N, t)) / N).has(y)
    zero(sp.simplify((sp.diff(N, t) - sp.diff(M, y)) / M) + 1 / y)
    exact(M / y, N / y)
    implicit(t * y + sp.log(y), -M / N)
