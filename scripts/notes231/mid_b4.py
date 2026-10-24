"""B4: make a non-exact equation exact with an integrating factor (Week 4)."""
import sympy as sp

from midlib import P, S, TAGS, implicit, link, t, y, zero


def build(D):
    W4 = lambda *p: D.cite('W4', *p)
    D.H('B4 · Not exact: make it exact with an integrating factor', level=2, cites=W4(4, 5))
    TAGS(D, (4, 3))
    D.P(r'**What if the exactness test fails?** Multiply the whole equation by a function $\mu$ (an **integrating factor**) '
        r'chosen so that the new equation passes the test. Then finish with ' + link('B3', 'b3') + '.')
    D.P(r'Start from $M\,dt+N\,dy=0$ with $M_y\neq N_t$, and compute the **mismatch**:')
    D.EQ(r'M_y-N_t')
    D.P(r'**Theorem 1.** If this ratio depends on $t$ only, call it $f(t)$:', cites=W4(5))
    D.EQ(r'\dfrac{M_y-N_t}{N}=f(t)\quad\Rightarrow\quad \mu=e^{\int f(t)\,dt}')
    D.P(r'**Theorem 2.** If this ratio depends on $y$ only, call it $g(y)$:')
    D.EQ(r'\dfrac{N_t-M_y}{M}=g(y)\quad\Rightarrow\quad \mu=e^{\int g(y)\,dy}')
    D.P('**Memory aid:**')
    D.L([r'Theorem 1 divides the mismatch by $N$ and must leave only $t$.',
         r'Theorem 2 divides by $M$, with the subtraction **flipped** ($N_t-M_y$), and must leave only $y$.'])
    D.P('**Method:**')
    D.L([r'**Test:** $M_y\neq N_t$ (otherwise it is already exact: ' + link('B3', 'b3') + ').',
         r'**Ratios:** compute both. Keep the one that depends on a single letter.',
         r'**Integrating factor:** $\mu=e^{\int f\,dt}$ or $\mu=e^{\int g\,dy}$ (no $+C$ needed).',
         r'**Multiply the whole equation** by $\mu$: both $M$ and $N$.',
         r'**Re-test** (it must pass now), then solve with the ' + link('B3', 'b3') + ' steps.'],
        ordered=True)
    D.P('**Calculus you need here:**')
    D.T(['Expression', 'Result', 'Note'], [
        [r'$e^{\int\frac{k}{y}dy}$', r'$e^{k\ln|y|}=|y|^k$', r'e.g. $g=\frac2y$ gives $\mu=y^2$; $g=-\frac1y$ gives $\mu=\frac1y$'],
        [r'$e^{\int\frac{k}{t}dt}$', r'$t^k$', r'e.g. $f=-\frac2t$ gives $\mu=t^{-2}=\frac{1}{t^2}$'],
        [r'$e^{\int k\,dt}$', r'$e^{kt}$', r'constant ratio'],
    ])
    D.CO('info', r'**Bonus (skip-safe): where Theorem 1 comes from.** Multiply by $\mu(t)$ and ask for the new equation to pass the test: '
         r'$(\mu M)_y=(\mu N)_t$, i.e. $\mu M_y=\mu\prime N+\mu N_t$. Rearranged:'
         '\n\n$$\n' r'\dfrac{\mu\prime}{\mu}=\dfrac{M_y-N_t}{N}' '\n$$\n\n'
         r'A $\mu$ depending on $t$ alone can only exist if the right side depends on $t$ alone. Then $\ln\mu=\int f\,dt$. Theorem 2 is the same argument with $\mu(y)$.')

    D.EX('W4 · Repair, then finish · lecture exercise (e) and Pre-tutorial 4',
         r'Solve $y\,dt+(3+3t-y)\,dy=0$.',
         [S(r'**Type:** $M\,dt+N\,dy=0$ with $M=y$, $N=3+3t-y$. **Test:** $M_y=1$, $N_t=3$: not exact.'),
          S(r'**Ratios:** Theorem 1 gives $\frac{1-3}{3+3t-y}$, which has both letters. Theorem 2 gives $y$ only.', r'\dfrac{N_t-M_y}{M}=\dfrac{3-1}{y}=\dfrac2y'),
          S(r'**Integrating factor:** $e^{\int\frac2y dy}=e^{2\ln|y|}$.', r'\mu=y^2'),
          S(r'**Multiply the whole equation** by $y^2$.', r'y^3\,dt+(3y^2+3ty^2-y^3)\,dy=0'),
          S(r'**Re-test.**', r'M_y=3y^2=N_t\quad\checkmark'),
          S(r'**Integrate $M$ in $t$** ($y$ fixed).', r'U=ty^3+f(y)'),
          S(r'**Match $N$:** $3ty^2+f\prime(y)=3y^2+3ty^2-y^3$, so $f\prime=3y^2-y^3$.', r'f(y)=y^3-\tfrac14y^4')],
         r'$ty^3+y^3-\dfrac{y^4}{4}=C$.', cites=W4(4, 5) + D.cite('T4', 1))

    P(D, 'W4 · A factor in t only',
      r'Solve $(t^2+y)\,dt-t\,dy=0$ for $t>0$.',
      [S(r'**Type:** $M=t^2+y$, $N=-t$. **Test:** $M_y=1$, $N_t=-1$: not exact.'),
       S(r'**Ratios:** Theorem 1 leaves only $t$.', r'\dfrac{M_y-N_t}{N}=\dfrac{1-(-1)}{-t}=-\dfrac2t'),
       S(r'**Integrating factor:** $e^{\int-\frac2t dt}=e^{-2\ln t}$.', r'\mu=\dfrac{1}{t^2}'),
       S(r'**Multiply the whole equation** by $\frac{1}{t^2}$.', r'\Big(1+\dfrac{y}{t^2}\Big)dt-\dfrac1t\,dy=0'),
       S(r'**Re-test.**', r'M_y=\dfrac{1}{t^2}=N_t\quad\checkmark'),
       S(r'**Integrate $M$ in $t$:** $\int\frac{y}{t^2}dt=-\frac yt$.', r'U=t-\dfrac{y}{t}+f(y)'),
       S(r'**Match $N$:** $-\frac1t+f\prime=-\frac1t$, so $f\prime=0$.', r't-\dfrac yt=C')],
      r'$t-\dfrac{y}{t}=C$, i.e. $y=t^2-Ct$. Check with ' + link('B2', 'b2') + r': the equation is also linear, $y\prime-\frac{y}{t}=t$, and gives the same family.')
    P(D, 'W4 · A factor in y only',
      r'Solve $y\,dt+(2t+y^3)\,dy=0$.',
      [S(r'**Type:** $M=y$, $N=2t+y^3$. **Test:** $M_y=1$, $N_t=2$: not exact.'),
       S(r'**Ratios:** Theorem 1 gives $\frac{-1}{2t+y^3}$ (both letters). Theorem 2:', r'\dfrac{N_t-M_y}{M}=\dfrac{2-1}{y}=\dfrac1y'),
       S(r'**Integrating factor:** $e^{\int\frac1y dy}=e^{\ln|y|}$.', r'\mu=y'),
       S(r'**Multiply the whole equation** by $y$.', r'y^2\,dt+(2ty+y^4)\,dy=0'),
       S(r'**Re-test.**', r'M_y=2y=N_t\quad\checkmark'),
       S(r'**Integrate $M$ in $t$.**', r'U=ty^2+f(y)'),
       S(r'**Match $N$:** $2ty+f\prime=2ty+y^4$, so $f=\frac{y^5}{5}$.', r'ty^2+\dfrac{y^5}{5}=C')],
      r'$ty^2+\dfrac{y^5}{5}=C$.', diff='intermediate')
    P(D, 'W4 · Which theorem applies?',
      r'Find an integrating factor for each equation, then solve it.' '\n\n'
      r'(a) $(2y+3t)\,dt+t\,dy=0$' '\n\n'
      r'(b) $y^2\,dt+(ty+1)\,dy=0$',
      [S(r'(a) **Test:** $M_y=2$, $N_t=1$. Theorem 1: $\frac{2-1}{t}=\frac1t$, only $t$.', r'\mu=e^{\int\frac1t dt}=t'),
       S(r'(a) Multiply by $t$: this is exactly the B3 worked example.', r'(2ty+3t^2)\,dt+t^2\,dy=0'),
       S(r'(a) Its solution (from B3).', r't^2y+t^3=C'),
       S(r'(b) **Test:** $M_y=2y$, $N_t=y$. Theorem 1 gives $\frac{y}{ty+1}$ (both letters). Theorem 2:', r'\dfrac{N_t-M_y}{M}=\dfrac{y-2y}{y^2}=-\dfrac1y'),
       S(r'(b) **Integrating factor:** $e^{-\ln|y|}$.', r'\mu=\dfrac1y'),
       S(r'(b) Multiply by $\frac1y$ and re-test: $M_y=1=N_t$.', r'y\,dt+\Big(t+\dfrac1y\Big)dy=0'),
       S(r'(b) $U=ty+f(y)$; matching $N$ gives $f\prime=\frac1y$, so $f=\ln|y|$.', r'ty+\ln|y|=C')],
      r'(a) $\mu=t$, $\;t^2y+t^3=C$. (b) $\mu=\dfrac1y$, $\;ty+\ln|y|=C$.', diff='advanced')


def verify():
    def exact(M, N):
        zero(sp.diff(M, y) - sp.diff(N, t))

    # lecture (e) / Pre-tutorial 4
    M, N = y, 3 + 3 * t - y
    assert sp.diff(M, y) != sp.diff(N, t)
    assert sp.simplify((sp.diff(M, y) - sp.diff(N, t)) / N).has(y)
    g = sp.simplify((sp.diff(N, t) - sp.diff(M, y)) / M)
    zero(g - 2 / y)
    mu = y ** 2
    exact(mu * M, mu * N)
    implicit(t * y ** 3 + y ** 3 - y ** 4 / 4, -M / N)
    # factor in t only
    tp = sp.symbols('tp', positive=True)
    M, N = t ** 2 + y, -t
    f = sp.simplify((sp.diff(M, y) - sp.diff(N, t)) / N)
    zero(f + 2 / t)
    zero(sp.exp(sp.integrate(f.subs(t, tp), tp)) - 1 / tp ** 2)
    exact(M / t ** 2, N / t ** 2)
    implicit(t - y / t, -M / N)
    C = sp.symbols('C')
    zero(sp.diff(t ** 2 - C * t, t) - (t ** 2 - C * t) / t - t)
    # factor in y only
    M, N = y, 2 * t + y ** 3
    zero(sp.simplify((sp.diff(N, t) - sp.diff(M, y)) / M) - 1 / y)
    exact(y * M, y * N)
    implicit(t * y ** 2 + y ** 5 / 5, -M / N)
    # which theorem
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
