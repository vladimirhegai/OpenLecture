"""B4: make a non-exact equation exact with an integrating factor (Week 4)."""
import sympy as sp

from midlib import P, S, TAGS, implicit, link, t, y, zero


def build(D):
    W4 = lambda *p: D.cite('W4', *p)
    D.H('B4 · Not exact: make it exact with an integrating factor', level=2, cites=W4(4, 5))
    TAGS(D, (4, 3))
    D.P(r'**What if the exactness test fails?** Take $y\,dt+(3+3t-y)\,dy=0$: $M_y=1$ but $N_t=3$, so ' + link('B3', 'b3') + r' can’t start.')
    D.P(r'The fix: multiply the whole equation by a function $\mu$, called an **integrating factor**, picked so the new equation '
        r'passes the test. Then solve it with the ' + link('B3', 'b3') + r' steps. Same idea as in ' + link('B2', 'b2') +
        r': multiply by the right thing and the equation becomes easy.')
    D.P(r'**How to find $\mu$.** Start with the mismatch between the two cross derivatives:')
    D.EQ(r'M_y-N_t')
    D.P(r'In the example: $M_y-N_t=1-3=-2$. Now divide it, and see which case you’re in.')
    D.P(r'**Case 1: divide by $N$, and only $t$ is left.** (The lecture calls this Theorem 1.)', cites=W4(5))
    D.EQ(r'\dfrac{M_y-N_t}{N}=f(t)\quad\Rightarrow\quad \mu=e^{\int f(t)\,dt}')
    D.P(r'Example: $(t^2+y)\,dt-t\,dy=0$ gives $\frac{1-(-1)}{-t}=-\frac2t$. Only $t$, so $\mu=e^{\int-\frac2t\,dt}=\frac{1}{t^2}$.')
    D.P(r'**Case 2: flip the subtraction, divide by $M$, and only $y$ is left.** (Theorem 2.)')
    D.EQ(r'\dfrac{N_t-M_y}{M}=g(y)\quad\Rightarrow\quad \mu=e^{\int g(y)\,dy}')
    D.P(r'Example: $y\,dt+(3+3t-y)\,dy=0$ gives $\frac{3-1}{y}=\frac2y$. Only $y$, so $\mu=e^{\int\frac2y\,dy}=y^2$.')
    D.P(r'Why only one letter: $\mu$ will be a function of one letter, so the ratio you integrate to get it can only contain that letter. '
        r'If neither ratio has just one letter, these two cases don’t help.')
    D.P('**Method:**')
    D.L([r'**Test:** check that $M_y\neq N_t$. (If they’re equal, it’s already exact: go to ' + link('B3', 'b3') + '.)',
         r'**Ratios:** compute both. Keep the one that has only one letter in it.',
         r'**Integrating factor:** $\mu=e^{\int f\,dt}$ or $\mu=e^{\int g\,dy}$. No $+C$ needed: any one $\mu$ works.',
         r'**Multiply the whole equation** by $\mu$: both $M$ and $N$.',
         r'**Re-test:** it must pass now (if not, recheck your algebra). Then solve with the ' + link('B3', 'b3') + ' steps.'],
        ordered=True)
    D.P(r'**Calculus you need here** ($e$ and $\ln$ cancel: $e^{k\ln y}=y^k$):')
    D.T(['Expression', 'Result', 'Example'], [
        [r'$e^{\int\frac{k}{y}dy}$', r'$e^{k\ln|y|}=|y|^k$', r'$g=\frac2y$ gives $\mu=y^2$; $g=-\frac1y$ gives $\mu=\frac1y$'],
        [r'$e^{\int\frac{k}{t}dt}$', r'$t^k$', r'$f=-\frac2t$ gives $\mu=t^{-2}=\frac{1}{t^2}$'],
        [r'$e^{\int k\,dt}$', r'$e^{kt}$', r'the ratio is a constant $k$'],
    ])
    D.CO('info', r'**Bonus (skip-safe): where Case 1 comes from.** Multiply by $\mu(t)$ and ask the new equation to pass the test, $(\mu M)_y=(\mu N)_t$. '
         r'On the left, $\mu$ has no $y$, so it just comes out: $\mu M_y$. On the right, the product rule gives $\mu\prime N+\mu N_t$. Rearrange:'
         '\n\n$$\n' r'\dfrac{\mu\prime}{\mu}=\dfrac{M_y-N_t}{N}' '\n$$\n\n'
         r'The left side only has $t$ in it, so the right side must too. Then $\ln\mu=\int f\,dt$. Case 2 is the same argument with $\mu(y)$.')

    D.EX('W4 · Repair, then finish · lecture exercise (e) and Pre-tutorial 4',
         r'Solve $y\,dt+(3+3t-y)\,dy=0$.',
         [S(r'**Type:** $M\,dt+N\,dy=0$ form, with $M=y$, $N=3+3t-y$.'),
          S(r'**Test:** the two cross derivatives don’t match, so it’s not exact.', r'M_y=1\neq3=N_t'),
          S(r'**Ratios:** Case 1 gives $\frac{1-3}{3+3t-y}$, which has both letters. Case 2 leaves only $y$.', r'\dfrac{N_t-M_y}{M}=\dfrac{3-1}{y}=\dfrac2y'),
          S(r'**Integrating factor:** $e^{\int\frac2y dy}=e^{2\ln|y|}$.', r'\mu=y^2'),
          S(r'**Multiply the whole equation** by $y^2$.', r'y^3\,dt+(3y^2+3ty^2-y^3)\,dy=0'),
          S(r'**Re-test:** it passes now.', r'M_y=3y^2=N_t\quad\checkmark'),
          S(r'**Integrate $M$ in $t$** ($y$ is a number).', r'U=ty^3+f(y)'),
          S(r'**Match $N$:** $U_y=3ty^2+f\prime(y)$ must equal $3y^2+3ty^2-y^3$. So $f\prime=3y^2-y^3$.', r'f(y)=y^3-\tfrac14y^4'),
          S(r'**Answer:** set $U=C$.', r'ty^3+y^3-\tfrac14y^4=C')],
         r'$ty^3+y^3-\dfrac{y^4}{4}=C$.', cites=W4(4, 5) + D.cite('T4', 1))

    P(D, 'W4 · A factor in t only',
      r'Solve $(t^2+y)\,dt-t\,dy=0$ for $t>0$.',
      [S(r'**Type:** $M=t^2+y$, $N=-t$. **Test:** $M_y=1$, $N_t=-1$: not exact.'),
       S(r'**Ratios:** Case 1 leaves only $t$.', r'\dfrac{M_y-N_t}{N}=\dfrac{1-(-1)}{-t}=-\dfrac2t'),
       S(r'**Integrating factor:** $e^{\int-\frac2t dt}=e^{-2\ln t}=t^{-2}$.', r'\mu=\dfrac{1}{t^2}'),
       S(r'**Multiply the whole equation** by $\frac{1}{t^2}$.', r'\Big(1+\dfrac{y}{t^2}\Big)dt-\dfrac1t\,dy=0'),
       S(r'**Re-test:** it passes now.', r'M_y=\dfrac{1}{t^2}=N_t\quad\checkmark'),
       S(r'**Integrate $M$ in $t$:** $\int1\,dt=t$, and $\int\frac{y}{t^2}dt=-\frac yt$ ($y$ is a number).', r'U=t-\dfrac{y}{t}+f(y)'),
       S(r'**Match $N$:** $U_y=-\frac1t+f\prime$ must equal $-\frac1t$, so $f\prime=0$.', r't-\dfrac yt=C')],
      r'$t-\dfrac{y}{t}=C$, so $y=t^2-Ct$. Check with ' + link('B2', 'b2') + r': the equation is also linear, $y\prime-\frac{y}{t}=t$, and gives the same family.')
    P(D, 'W4 · A factor in y only',
      r'Solve $y\,dt+(2t+y^3)\,dy=0$.',
      [S(r'**Type:** $M=y$, $N=2t+y^3$. **Test:** $M_y=1$, $N_t=2$: not exact.'),
       S(r'**Ratios:** Case 1 gives $\frac{-1}{2t+y^3}$ (both letters). Case 2 leaves only $y$:', r'\dfrac{N_t-M_y}{M}=\dfrac{2-1}{y}=\dfrac1y'),
       S(r'**Integrating factor:** $e^{\int\frac1y dy}=e^{\ln|y|}$.', r'\mu=y'),
       S(r'**Multiply the whole equation** by $y$.', r'y^2\,dt+(2ty+y^4)\,dy=0'),
       S(r'**Re-test:** it passes now.', r'M_y=2y=N_t\quad\checkmark'),
       S(r'**Integrate $M$ in $t$.**', r'U=ty^2+f(y)'),
       S(r'**Match $N$:** $U_y=2ty+f\prime$ must equal $2ty+y^4$. So $f\prime=y^4$ and $f=\frac{y^5}{5}$.', r'ty^2+\dfrac{y^5}{5}=C')],
      r'$ty^2+\dfrac{y^5}{5}=C$.', diff='intermediate')
    P(D, 'W4 · Which case applies?',
      r'Find an integrating factor for each equation, then solve it.' '\n\n'
      r'(a) $(2y+3t)\,dt+t\,dy=0$' '\n\n'
      r'(b) $y^2\,dt+(ty+1)\,dy=0$',
      [S(r'(a) **Test:** $M_y=2$, $N_t=1$, not exact. **Ratios:** Case 1 gives $\frac{2-1}{t}=\frac1t$, only $t$.', r'\mu=e^{\int\frac1t dt}=t'),
       S(r'(a) **Multiply** by $t$: you get exactly the B3 worked example.', r'(2ty+3t^2)\,dt+t^2\,dy=0'),
       S(r'(a) **Answer:** the solution from B3.', r't^2y+t^3=C'),
       S(r'(b) **Test:** $M_y=2y$, $N_t=y$, not exact. **Ratios:** Case 1 gives $\frac{y}{ty+1}$ (both letters). Case 2:', r'\dfrac{N_t-M_y}{M}=\dfrac{y-2y}{y^2}=-\dfrac1y'),
       S(r'(b) **Integrating factor:** $e^{\int-\frac1y dy}=e^{-\ln|y|}$.', r'\mu=\dfrac1y'),
       S(r'(b) **Multiply** by $\frac1y$ and re-test: $M_y=1=N_t$, it passes.', r'y\,dt+\Big(t+\dfrac1y\Big)dy=0'),
       S(r'(b) **Integrate and match:** $U=ty+f(y)$. $U_y=t+f\prime$ must equal $t+\frac1y$, so $f\prime=\frac1y$ and $f=\ln|y|$.', r'ty+\ln|y|=C')],
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
