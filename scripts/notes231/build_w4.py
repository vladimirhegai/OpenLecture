"""ELEC 231 Week 4 study note: exact equations and integrating factors.

Run:  .venv/Scripts/python.exe scripts/notes231/build_w4.py      (writes out/w4.json)
Every answer below is checked with sympy in check() before any block is built.
"""
import sympy as sp

from lib231 import Doc, S
from figs_w234 import make_w4  # noqa: E402
FIGS = make_w4()

t, y = sp.symbols('t y', positive=True)
k = sp.symbols('k')


# ====================================================================== sympy checks
def zero(e):
    return sp.simplify(e) == 0


def dd(e, v):
    return sp.diff(e, v)


def is_exact(M, N):
    return zero(dd(M, y) - dd(N, t))


def potential(M, N, U):
    """U is a potential: dU/dt = M and dU/dy = N."""
    assert zero(dd(U, t) - M), (U, M)
    assert zero(dd(U, y) - N), (U, N)


def solves(M, N, U):
    """Implicit differentiation: along U(t,y)=C, dy/dt = -U_t/U_y; this must satisfy M + N dy/dt = 0."""
    assert zero(M * dd(U, y) - N * dd(U, t)), (M, N, U)


def explicit(M, N, Y):
    """y = Y(t) substituted into M + N dy/dt = 0."""
    assert zero(M.subs(y, Y) + N.subs(y, Y) * dd(Y, t)), Y


def same_up_to_const(a, b):
    r = sp.simplify(a / b)
    assert not r.has(t) and not r.has(y), (a, b, r)


def mu_t(M, N):
    r = sp.simplify((dd(M, y) - dd(N, t)) / N)
    assert not r.has(y), r
    return r, sp.simplify(sp.exp(sp.integrate(r, t)))


def mu_y(M, N):
    r = sp.simplify((dd(N, t) - dd(M, y)) / M)
    assert not r.has(t), r
    return r, sp.simplify(sp.exp(sp.integrate(r, y)))


def check():
    # ---------------- Topic 1
    # Ex1 lecture (a): 3t dt + 4y dy = 0
    M, N = 3 * t, 4 * y
    assert is_exact(M, N)
    potential(M, N, sp.Rational(3, 2) * t**2 + 2 * y**2)
    solves(M, N, 3 * t**2 + 4 * y**2)
    # Ex2 lecture Example 4.1
    M, N = 2 * t * y + 3 * t**2, t**2
    assert dd(M, y) == 2 * t and dd(N, t) == 2 * t
    U = t**2 * y + t**3
    potential(M, N, U)
    C = sp.symbols('C')
    explicit(M, N, (C - t**3) / t**2)
    assert sp.integrate(N, y) == t**2 * y  # N-first route: U = t^2 y + g(t), g' = 3t^2
    assert zero(dd(t**2 * y, t) - 2 * t * y) and sp.integrate(3 * t**2, t) == t**3
    # Ex3 lecture (b): y' = (t-y)/(t+y)  ->  (t-y)dt - (t+y)dy = 0
    M, N = t - y, -(t + y)
    assert is_exact(M, N)
    potential(M, N, t**2 / 2 - t * y - y**2 / 2)
    U = t**2 - 2 * t * y - y**2
    solves(M, N, U)
    assert zero(-dd(U, t) / dd(U, y) - (t - y) / (t + y))
    # Ex4 lecture (c): 2ty y' = t^2 - y^2 -> (t^2-y^2)dt - 2ty dy = 0
    M, N = t**2 - y**2, -2 * t * y
    assert is_exact(M, N)
    assert not is_exact(M, -N)  # wrong-sign rewrite looks "not exact"
    potential(M, N, t**3 / 3 - t * y**2)
    U = t**3 - 3 * t * y**2
    solves(M, N, U)
    assert zero(2 * t * y * (-dd(U, t) / dd(U, y)) - (t**2 - y**2))
    # Ex5 lecture (d): y' = t/(t+y) -> t dt - (t+y) dy = 0, not exact
    M, N = t, -(t + y)
    assert dd(M, y) == 0 and dd(N, t) == -1 and not is_exact(M, N)
    # Ex6 original: (e^t y + 2t)dt + (e^t + 3y^2)dy = 0, y(0)=1
    M, N = sp.exp(t) * y + 2 * t, sp.exp(t) + 3 * y**2
    assert is_exact(M, N)
    U = sp.exp(t) * y + t**2 + y**3
    potential(M, N, U)
    assert U.subs({t: 0, y: 1}) == 2
    # Try it 1
    assert is_exact(2 * t + y, t + 2 * y)
    assert dd(t - y, y) == -1 and dd(t + y, t) == 1
    assert is_exact(sp.cos(y), -t * sp.sin(y))
    # Try it 2
    potential(2 * t + y, t + 2 * y, t**2 + t * y + y**2)
    # Try it 3
    M, N = y**2 + y * sp.cos(t), 2 * t * y + sp.sin(t)
    assert is_exact(M, N)
    U = t * y**2 + y * sp.sin(t)
    potential(M, N, U)
    assert zero(U.subs({t: sp.pi / 2, y: 1}) - (sp.pi / 2 + 1))
    # Try it 4
    M, N = sp.exp(t) + 2 * t * y**2, 2 * t**2 * y + 3 * y**2
    assert is_exact(M, N)
    U = sp.exp(t) + t**2 * y**2 + y**3
    potential(M, N, U)
    assert zero(-M / N + (sp.exp(t) + 2 * t * y**2) / (2 * t**2 * y + 3 * y**2))
    assert U.subs({t: 0, y: 1}) == 2
    # Try it 5
    Mk, Nk = 2 * t * sp.sin(y) + y, t**2 * sp.cos(y) + k * t
    assert sp.solve(sp.Eq(dd(Mk, y), dd(Nk, t)), k) == [1]
    M, N = Mk, Nk.subs(k, 1)
    U = t**2 * sp.sin(y) + t * y
    potential(M, N, U)
    assert zero(U.subs({t: 1, y: sp.pi / 2}) - (1 + sp.pi / 2))

    # ---------------- Topic 2
    # Ex7 lecture (e): y dt + (3+3t-y) dy = 0, mu = y^2
    M, N = y, 3 + 3 * t - y
    assert not is_exact(M, N)
    r1 = sp.simplify((dd(M, y) - dd(N, t)) / N)
    assert r1.has(y) and r1.has(t)  # Theorem 1 fails
    r, mu = mu_y(M, N)
    assert zero(r - 2 / y) and zero(mu - y**2)
    assert is_exact(mu * M, mu * N)
    # Try it 6 = pre-tutorial 4: finish it
    U = t * y**3 + y**3 - y**4 / 4
    potential(mu * M, mu * N, U)
    solves(M, N, 4 * (t + 1) * y**3 - y**4)
    assert zero(M.subs(y, 0))  # y = 0 solves the original and sits in C = 0
    # Ex8 Theorem 1: (t^2+y^2+t)dt + ty dy = 0, y(1)=1, mu = t
    M, N = t**2 + y**2 + t, t * y
    r, mu = mu_t(M, N)
    assert zero(r - 1 / t) and zero(mu - t)
    U = t**4 / 4 + t**2 * y**2 / 2 + t**3 / 3
    potential(mu * M, mu * N, U)
    assert (12 * U).subs({t: 1, y: 1}) == 13
    explicit(M, N, sp.sqrt((13 - 3 * t**4 - 4 * t**3) / (6 * t**2)))
    assert sp.sqrt((13 - 3 * t**4 - 4 * t**3) / (6 * t**2)).subs(t, 1) == 1
    # Ex9 Theorem 1 giving e^t: (2t + y^2)dt + 2y dy = 0, y(0)=1
    M, N = 2 * t + y**2, 2 * y
    r, mu = mu_t(M, N)
    assert r == 1 and zero(mu - sp.exp(t))
    assert zero(sp.integrate(2 * t * sp.exp(t), t) - (2 * t * sp.exp(t) - 2 * sp.exp(t)))
    U = sp.exp(t) * (y**2 + 2 * t - 2)
    potential(mu * M, mu * N, U)
    assert U.subs({t: 0, y: 1}) == -1
    Y = sp.sqrt(2 - 2 * t - sp.exp(-t))
    explicit(M, N, Y)
    assert Y.subs(t, 0) == 1
    # Ex10 linear: dy/dt + 2y = 4, y(0)=0
    M, N = 2 * y - 4, sp.Integer(1)
    r, mu = mu_t(M, N)
    assert r == 2 and zero(mu - sp.exp(2 * t))
    U = (y - 2) * sp.exp(2 * t)
    potential(mu * M, mu * N, U)
    assert U.subs({t: 0, y: 0}) == -2
    Y = 2 - 2 * sp.exp(-2 * t)
    explicit(M, N, Y)
    assert zero(dd(Y, t) + 2 * Y - 4) and Y.subs(t, 0) == 0
    # general linear case: (a y - b) dt + dy = 0 -> ratio a(t)
    a, b = sp.Function('a')(t), sp.Function('b')(t)
    assert zero((dd(a * y - b, y) - 0) / 1 - a)
    # Ex11: y dt - t dy = 0, two factors, lost solution
    M, N = y, -t
    r, mu = mu_t(M, N)
    assert zero(r + 2 / t) and zero(mu - t**-2)
    r, mu2 = mu_y(M, N)
    assert zero(r + 2 / y) and zero(mu2 - y**-2)
    potential(mu2 * M, mu2 * N, t / y)
    potential(mu * M, mu * N, -y / t)
    kk = sp.symbols('kk')
    explicit(M, N, kk * t)
    explicit(M, N, sp.Integer(0))
    # Try it 7: y dt + (2t + y^2) dy = 0, mu = y
    M, N = y, 2 * t + y**2
    r, mu = mu_y(M, N)
    assert zero(r - 1 / y) and zero(mu - y)
    potential(mu * M, mu * N, t * y**2 + y**4 / 4)
    # Try it 8: (3ty + y^2)dt + (t^2 + ty)dy = 0, mu = t
    M, N = 3 * t * y + y**2, t**2 + t * y
    r, mu = mu_t(M, N)
    assert zero(r - 1 / t) and zero(mu - t)
    potential(mu * M, mu * N, t**3 * y + t**2 * y**2 / 2)
    # Try it 9: lecture (d), neither theorem works
    M, N = t, -(t + y)
    r1 = sp.simplify((dd(M, y) - dd(N, t)) / N)
    r2 = sp.simplify((dd(N, t) - dd(M, y)) / M)
    assert zero(r1 + 1 / (t + y)) and r1.has(y)
    assert zero(r2 + 1 / t) and r2.has(t)
    # Try it 10: dy/dt + y/t = 3t, y(1)=2
    M, N = y / t - 3 * t, sp.Integer(1)
    r, mu = mu_t(M, N)
    assert zero(r - 1 / t) and zero(mu - t)
    U = t * y - t**3
    potential(mu * M, mu * N, U)
    assert U.subs({t: 1, y: 2}) == 1
    Y = t**2 + 1 / t
    explicit(M, N, Y)
    assert zero(dd(Y, t) + Y / t - 3 * t) and Y.subs(t, 1) == 2

    # ---------------- Mixed practice
    # P1
    assert is_exact(y + 2 * t, t + 1)
    potential(y + 2 * t, t + 1, t * y + t**2 + y)
    r, mu = mu_t(t * y + 1, t**2)
    assert zero(r + 1 / t) and zero(mu - 1 / t)
    assert is_exact((t * y + 1) / t, t)
    assert not is_exact(t * y + 1, t**2)
    # P2
    M, N = 3 * t**2 * y - sp.sin(t), t**3 + y
    assert is_exact(M, N)
    U = t**3 * y + sp.cos(t) + y**2 / 2
    potential(M, N, U)
    assert U.subs({t: 0, y: 2}) == 3
    Y = -t**3 + sp.sqrt(t**6 - 2 * sp.cos(t) + 6)
    assert zero(U.subs(y, Y) - 3) and Y.subs(t, 0) == 2
    explicit(M, N, Y)
    # P3: dy/dt = e^(t-y), y(0) = ln 2
    Y = sp.log(sp.exp(t) + 1)
    assert zero(dd(Y, t) - sp.exp(t - Y)) and zero(Y.subs(t, 0) - sp.log(2))
    assert is_exact(sp.exp(t), -sp.exp(y))
    potential(sp.exp(t), -sp.exp(y), sp.exp(t) - sp.exp(y))
    # P4: (2y^2 + 3t)dt + 2ty dy = 0, y(1)=2
    M, N = 2 * y**2 + 3 * t, 2 * t * y
    r, mu = mu_t(M, N)
    assert zero(r - 1 / t) and zero(mu - t)
    U = t**2 * y**2 + t**3
    potential(mu * M, mu * N, U)
    assert U.subs({t: 1, y: 2}) == 5
    Y = sp.sqrt(5 - t**3) / t
    explicit(M, N, Y)
    assert Y.subs(t, 1) == 2
    # P5: dt + (t + 2y) dy = 0, y(0)=0 (t as a function of y)
    M, N = sp.Integer(1), t + 2 * y
    r1 = sp.simplify((dd(M, y) - dd(N, t)) / N)
    assert r1.has(y)
    r, mu = mu_y(M, N)
    assert r == 1 and zero(mu - sp.exp(y))
    assert zero(sp.integrate(2 * y * sp.exp(y), y) - (2 * y * sp.exp(y) - 2 * sp.exp(y)))
    U = sp.exp(y) * (t + 2 * y - 2)
    potential(mu * M, mu * N, U)
    assert U.subs({t: 0, y: 0}) == -2
    T = 2 - 2 * y - 2 * sp.exp(-y)
    assert zero(dd(T, y) + (T + 2 * y)) and T.subs(y, 0) == 0
    # P6: spot the mistake
    M, N = 2 * t * y + 1, t**2 + 4 * y
    assert is_exact(M, N)
    wrong = 2 * t**2 * y + t + 2 * y**2
    assert not zero(dd(wrong, t) - M)
    U = t**2 * y + t + 2 * y**2
    potential(M, N, U)
    assert U.subs({t: 0, y: 1}) == 2
    # P7: lecture (e) as an IVP, y(0)=1
    M, N = y, 3 + 3 * t - y
    U4 = 4 * (t + 1) * y**3 - y**4
    solves(M, N, U4)
    assert U4.subs({t: 0, y: 1}) == 3
    T = (3 + y**4) / (4 * y**3) - 1
    assert zero(U4.subs(t, T) - 3) and T.subs(y, 1) == 0
    # dt/dy = -(3 + 3t - y)/y along the solution
    assert zero(dd(T, y) + (3 + 3 * T - y) / y)
    print('all sympy checks passed')


check()

# ====================================================================== the note
D = Doc(week=4, title='Week 4: Exact Equations and Integrating Factors',
        topic_keys=['exact_equations', 'integrating_factors'])
W = lambda *p: D.cite('W4', *p)  # noqa: E731

D.CO('info', r"""**Week 4 in one sentence:** some first-order ODEs, written as $M\,dt+N\,dy=0$, are secretly "the change of one function $U(t,y)$ equals zero", so the answer is simply $U(t,y)=C$; and when an equation is *almost* like that, multiplying by a well-chosen factor $\mu$ makes it so.

**By the end you can:**
- rewrite any first-order ODE $\dfrac{dy}{dt}=\dots$ in the form $M\,dt+N\,dy=0$;
- test whether it is exact with $\partial M/\partial y=\partial N/\partial t$;
- find the function $U(t,y)$ and write the solution $U(t,y)=C$, using an initial condition to fix $C$;
- find an integrating factor $\mu(t)$ or $\mu(y)$ with the two tests from the lecture, and solve the resulting exact equation;
- check any answer by implicit differentiation.""", cites=W(1))

D.CO('info', r"""**Where is the second-order material?** The Week 4 lecture also starts second-order equations ($y''$ terms). To keep each topic in one place, all of that is in the **Week 5 note**. This note is only about first-order equations.""",
     cites=W(1))

# ====================================================================== Topic 1
D.H('Topic 1: Exact equations')

D.P(r"""**The big idea.** Any first-order ODE can be written as $M(t,y)\,dt+N(t,y)\,dy=0$, where $M$ and $N$ are expressions in $t$ and $y$ (for example $\dfrac{dy}{dt}=\dfrac{t-y}{t+y}$ becomes $(t-y)\,dt-(t+y)\,dy=0$). Think of a function $U(t,y)$ as a **height map** over the $(t,y)$ plane, like a hiking map with contour lines (or an electric potential with its equipotential lines). If you take a tiny step $dt$ in $t$ and $dy$ in $y$, the height changes by $dU=\dfrac{\partial U}{\partial t}\,dt+\dfrac{\partial U}{\partial y}\,dy$: (how steep the map is in the $t$-direction) $\times$ (step in $t$) $+$ (how steep it is in the $y$-direction) $\times$ (step in $y$). The equation is called **exact** when $M$ and $N$ are exactly these two slopes, $M=\dfrac{\partial U}{\partial t}$ and $N=\dfrac{\partial U}{\partial y}$. Then the ODE says $dU=0$: along a solution the height never changes, so every solution curve is a **contour line** $U(t,y)=C$. Use it when the equation is neither separable nor linear. The exactness test takes 30 seconds, so do it first whenever an equation is given as $M\,dt+N\,dy=0$.""",
    cites=W(1, 2))

D.CO('tip', r"""**The method (exact equations)**

1. **Rewrite** the ODE as $M\,dt+N\,dy=0$: multiply $\dfrac{dy}{dt}=\dfrac{P}{Q}$ across to get $Q\,dy=P\,dt$, then move everything to the left: $P\,dt-Q\,dy=0$. Read off $M$ (everything multiplying $dt$) and $N$ (everything multiplying $dy$, *with its sign*).
2. **Test:** compute $\partial M/\partial y$ (treat $t$ as a constant) and $\partial N/\partial t$ (treat $y$ as a constant). Equal: exact, carry on. Not equal: go to Topic 2.
3. **Integrate $M$ with respect to $t$** (holding $y$ fixed) and add an unknown $f(y)$: $U=\int M\,dt+f(y)$.
4. **Match $N$:** differentiate this $U$ with respect to $y$, set it equal to $N$, solve for $f'(y)$ (it must contain no $t$) and integrate it to get $f(y)$.
5. **Answer:** $U(t,y)=C$. Put in the initial condition to find $C$. Solve for $y$ only if it is easy.
6. **Check** by implicit differentiation: $\dfrac{d}{dt}U(t,y)=0$ should give back the original ODE.""",
     cites=W(1, 2))

D.P(r"""The three key formulas: the change of $U$ for a small step (this is what $M\,dt+N\,dy$ must look like), the exactness test, and what "solving" means.""")
D.EQ(r'dU=\dfrac{\partial U}{\partial t}\,dt+\dfrac{\partial U}{\partial y}\,dy', cites=W(1))
D.EQ(r'M\,dt+N\,dy=0\ \text{is exact}\iff\dfrac{\partial M}{\partial y}=\dfrac{\partial N}{\partial t}', cites=W(1))
D.EQ(r'\begin{gathered}\dfrac{\partial U}{\partial t}=M,\quad \dfrac{\partial U}{\partial y}=N \\ \Longrightarrow\ U(t,y)=C\end{gathered}', cites=W(2))

D.CO('info', r"""**Calculus reminder: partial derivatives and "partial" integrals.**

- $\dfrac{\partial U}{\partial t}$ (read "partial $U$ by partial $t$") means: differentiate with respect to $t$ while **treating $y$ as a fixed number**. $\dfrac{\partial U}{\partial y}$ means: differentiate with respect to $y$ while treating $t$ as a fixed number.
- Example: $U=t^2y+t^3$. Holding $y$ fixed, $t^2y$ is "a constant times $t^2$", so $\dfrac{\partial U}{\partial t}=2ty+3t^2$. Holding $t$ fixed, $t^2y$ is "a constant times $y$" and $t^3$ is just a constant, so $\dfrac{\partial U}{\partial y}=t^2$.
- Power rule: $\dfrac{d}{dt}t^n=n\,t^{n-1}$ and $\displaystyle\int t^n\,dt=\dfrac{t^{n+1}}{n+1}$ (for $n\neq-1$); a constant factor just comes along.
- Integrating "with respect to $t$, holding $y$ fixed" undoes $\partial/\partial t$. The "constant" of integration may then be **any function of $y$**, $f(y)$, because $\dfrac{\partial}{\partial t}f(y)=0$.
- Why the test works: if $M=\partial U/\partial t$ and $N=\partial U/\partial y$, then $\partial M/\partial y$ and $\partial N/\partial t$ are both "differentiate $U$ once by $t$ and once by $y$", and the order does not matter for the functions we meet, so they must be equal.""")

D.EX('Lecture (a): the simplest exact equation',
     r'Test $3t\,dt+4y\,dy=0$ for exactness and, if exact, solve it.',
     [S(r'Read off $M$ (the expression multiplying $dt$) and $N$ (the expression multiplying $dy$).', r'M=3t,\qquad N=4y'),
      S(r'Test: $M=3t$ has no $y$ in it, so holding $t$ fixed it is a constant and $\partial M/\partial y=0$. Likewise $N=4y$ has no $t$, so $\partial N/\partial t=0$. They are equal, so the equation is exact.',
        r'\dfrac{\partial M}{\partial y}=0=\dfrac{\partial N}{\partial t}'),
      S(r'Integrate $M$ with respect to $t$ using the power rule ($\int t\,dt=\tfrac{t^2}{2}$), and add an unknown function $f(y)$ in place of the usual $+C$.',
        r'U=\int 3t\,dt=\dfrac{3}{2}t^2+f(y)'),
      S(r'Match $N$: differentiate $U$ with respect to $y$. The $\tfrac32 t^2$ part has no $y$, so it gives $0$, and we are left with $f^{\prime}(y)$, which must equal $N=4y$.',
        r'\dfrac{\partial U}{\partial y}=f^{\prime}(y)=4y'),
      S(r'Integrate $f^{\prime}(y)=4y$ with the power rule: $\int 4y\,dy=2y^2$. (No constant needed here; it gets absorbed into $C$ at the end.)', r'f(y)=2y^2'),
      S(r'So $U=\tfrac32t^2+2y^2$ and the solution is $U=C$. Multiply by 2 to clear the fraction ($2C$ is still just "some constant", so we call it $C$ again).',
        r'3t^2+4y^2=C'),
      S(r'Picture: for each $C>0$ this is an ellipse in the $(t,y)$ plane. Each ellipse is one contour line of $U$, i.e. one solution curve.', '')],
     r'$3t^2+4y^2=C$ (a family of ellipses).', cites=W(3))

D.CO('info', r"""**Calculus reminder: product rule and implicit differentiation** (used to check answers).

- Product rule: $\dfrac{d}{dt}\big(u\,v\big)=u'v+uv'$. Example: $\dfrac{d}{dt}(t^2y)=2t\,y+t^2\dfrac{dy}{dt}$ when $y$ depends on $t$.
- Chain rule for $y=y(t)$: $\dfrac{d}{dt}y^3=3y^2\dfrac{dy}{dt}$ (differentiate as if $y$ were the variable, then multiply by $\dfrac{dy}{dt}$).
- **Implicit differentiation** of an answer $U(t,y)=C$: differentiate both sides with respect to $t$, remembering $y$ depends on $t$. The right side gives $0$. This always gives $\dfrac{\partial U}{\partial t}+\dfrac{\partial U}{\partial y}\dfrac{dy}{dt}=0$, which should be the original ODE.
- Shorthand used in these checks: $y'$ (or $y^\prime$) means $\dfrac{dy}{dt}$, and $f'(y)$ means $\dfrac{df}{dy}$.""")

D.FIG(FIGS['levels'], r'The answer to Example 1 is a whole family of curves $3t^2+4y^2=C$: ellipses, one for each $C$. Think of $U(t,y)=\tfrac32t^2+2y^2$ as a height map; each solution is a contour line (a path of constant height), and the initial condition picks which one.')
D.EX('Lecture Example 4.1, solved both ways',
     r'Solve $(2ty+3t^2)\,dt+t^2\,dy=0$. Find $U$ twice, once by integrating $M$ first and once by integrating $N$ first, and check the answer.',
     [S(r'Read off $M$ and $N$.', r'M=2ty+3t^2,\qquad N=t^2'),
      S(r'Test: holding $t$ fixed, $\partial(2ty)/\partial y=2t$ and $\partial(3t^2)/\partial y=0$. Holding $y$ fixed, $\partial(t^2)/\partial t=2t$. Equal, so exact: there is a $U$ with $\partial U/\partial t=M$ and $\partial U/\partial y=N$.',
        r'\dfrac{\partial M}{\partial y}=2t=\dfrac{\partial N}{\partial t}'),
      S(r'**Way 1 (M first).** Integrate $M$ in $t$ with $y$ held fixed: $2ty$ is "$2y$ times $t$", whose integral is $2y\cdot\tfrac{t^2}{2}=t^2y$; and $\int3t^2\,dt=t^3$. Add $f(y)$.',
        r'U=\int(2ty+3t^2)\,dt=t^2y+t^3+f(y)'),
      S(r'Match $N$: differentiate in $y$ (holding $t$ fixed). $t^2y\to t^2$, $t^3\to0$, $f(y)\to f^{\prime}(y)$. Set equal to $N=t^2$.',
        r't^2+f^{\prime}(y)=t^2\ \Longrightarrow\ f^{\prime}(y)=0\ \Longrightarrow\ f(y)=\text{const}'),
      S(r'So $U=t^2y+t^3$ (the constant is absorbed into $C$).', r'U=t^2y+t^3'),
      S(r'**Way 2 (N first).** Integrate $N=t^2$ in $y$ with $t$ held fixed: $t^2$ is a constant, so $\int t^2\,dy=t^2y$. Now the unknown "constant" may depend on $t$, so we add $g(t)$.',
        r'U=\int t^2\,dy=t^2y+g(t)'),
      S(r'Match $M$: differentiate in $t$ (holding $y$ fixed): $\partial(t^2y)/\partial t=2ty$, plus $g^{\prime}(t)$. Set equal to $M=2ty+3t^2$; the $2ty$ cancels.',
        r'2ty+g^{\prime}(t)=2ty+3t^2\ \Longrightarrow\ g^{\prime}(t)=3t^2'),
      S(r'Integrate with the power rule: $\int3t^2\,dt=t^3$. Same $U$ as Way 1, as it must be.', r'g(t)=t^3\ \Longrightarrow\ U=t^2y+t^3'),
      S(r'The solution is $U=C$. Here we can even solve for $y$: subtract $t^3$ and divide by $t^2$.', r't^2y+t^3=C\quad\Longrightarrow\quad y=\dfrac{C}{t^2}-t'),
      S(r'**Check** by implicit differentiation: the product rule on $t^2y$ gives $2ty+t^2\dfrac{dy}{dt}$, and $\dfrac{d}{dt}t^3=3t^2$. Multiplying by $dt$ gives back the original equation.',
        r'2ty+t^2\dfrac{dy}{dt}+3t^2=0\iff(2ty+3t^2)\,dt+t^2\,dy=0')],
     r'$t^2y+t^3=C$, i.e. $y=\dfrac{C}{t^2}-t$. Both integration orders give $U=t^2y+t^3$.', cites=W(1, 2))

D.EX('Lecture (b): rewriting y′ = (t − y)/(t + y)',
     r'Write $\dfrac{dy}{dt}=\dfrac{t-y}{t+y}$ in the form $M\,dt+N\,dy=0$, test it for exactness, and solve it.',
     [S(r'Cross-multiply: multiply both sides by $(t+y)\,dt$ to clear the fraction.', r'(t+y)\,dy=(t-y)\,dt'),
      S(r'Move everything to the left side. Whatever multiplies $dt$ is $M$; whatever multiplies $dy$ (including the minus sign) is $N$.',
        r'\begin{gathered}(t-y)\,dt-(t+y)\,dy=0 \\ M=t-y,\quad N=-t-y\end{gathered}'),
      S(r'Test: $\partial(t-y)/\partial y=-1$ (the $t$ is a constant) and $\partial(-t-y)/\partial t=-1$ (the $y$ is a constant). Equal, so exact.',
        r'\dfrac{\partial M}{\partial y}=-1=\dfrac{\partial N}{\partial t}'),
      S(r'Integrate $M$ in $t$: $\int t\,dt=\tfrac{t^2}{2}$ and $\int y\,dt=yt$ (with $y$ fixed it is a constant). Add $f(y)$.',
        r'U=\int(t-y)\,dt=\dfrac{t^2}{2}-ty+f(y)'),
      S(r'Match $N$: differentiating in $y$ gives $-t+f^{\prime}(y)$; set equal to $N=-t-y$. The $-t$ cancels, leaving only $y$, as it should.',
        r'-t+f^{\prime}(y)=-t-y\ \Longrightarrow\ f^{\prime}(y)=-y'),
      S(r'Integrate: $\int(-y)\,dy=-\tfrac{y^2}{2}$.', r'f(y)=-\dfrac{y^2}{2}\ \Longrightarrow\ U=\dfrac{t^2}{2}-ty-\dfrac{y^2}{2}'),
      S(r'Set $U=C$ and multiply by 2 to clear fractions.', r't^2-2ty-y^2=C'),
      S(r'Check: differentiate implicitly. $\tfrac{d}{dt}(2ty)=2y+2t\,y^\prime$ (product rule) and $\tfrac{d}{dt}y^2=2y\,y^\prime$ (chain rule). Collect the $y^\prime$ terms and solve: we get the original ODE back.',
        r'2t-2y-2ty^\prime-2yy^\prime=0\ \Longrightarrow\ y^\prime=\dfrac{t-y}{t+y}')],
     r'$t^2-2ty-y^2=C$.', cites=W(3))

D.EX('Lecture (c): 2ty y′ = t² − y²',
     r'Solve $2ty\,\dfrac{dy}{dt}=t^2-y^2$.',
     [S(r'Multiply both sides by $dt$, then move the $dy$ term to the left. Watch the sign: the $dy$ term goes over with a minus.',
        r'\begin{gathered}2ty\,dy=(t^2-y^2)\,dt \\ \Longrightarrow\ (t^2-y^2)\,dt-2ty\,dy=0\end{gathered}'),
      S(r'Read off $M$ and $N$; the minus sign belongs to $N$.', r'M=t^2-y^2,\qquad N=-2ty'),
      S(r'Test: holding $t$ fixed, $\partial(t^2-y^2)/\partial y=-2y$; holding $y$ fixed, $\partial(-2ty)/\partial t=-2y$. Equal, so exact.',
        r'\dfrac{\partial M}{\partial y}=-2y=\dfrac{\partial N}{\partial t}'),
      S(r'Integrate $M$ in $t$: $\int t^2\,dt=\tfrac{t^3}{3}$ and $\int y^2\,dt=y^2t$ ($y^2$ is a constant here).',
        r'U=\dfrac{t^3}{3}-ty^2+f(y)'),
      S(r'Match $N$: $\partial U/\partial y=-2ty+f^{\prime}(y)$ must equal $-2ty$.', r'f^{\prime}(y)=0\ \Longrightarrow\ f(y)=\text{const}'),
      S(r'Set $U=C$ and multiply by 3.', r't^3-3ty^2=C'),
      S(r'Check: $\tfrac{d}{dt}(3ty^2)=3y^2+6ty\,y^\prime$ (product and chain rule), so $3t^2-3y^2-6ty\,y^\prime=0$. Divide by 3 and rearrange: $2ty\,y^\prime=t^2-y^2$. Correct.', '')],
     r'$t^3-3ty^2=C$.', cites=W(4))

D.EX('Lecture (d): an equation that is NOT exact',
     r'Is $\dfrac{dy}{dt}=\dfrac{t}{t+y}$ exact?',
     [S(r'Cross-multiply and move everything to the left side.', r'(t+y)\,dy=t\,dt\ \Longrightarrow\ t\,dt-(t+y)\,dy=0'),
      S(r'Read off $M$ and $N$.', r'M=t,\qquad N=-t-y'),
      S(r'Test: $M=t$ has no $y$, so $\partial M/\partial y=0$. Holding $y$ fixed, $\partial(-t-y)/\partial t=-1$. These differ.',
        r'\dfrac{\partial M}{\partial y}=0\neq-1=\dfrac{\partial N}{\partial t}'),
      S(r'So there is **no** $U$ with $\partial U/\partial t=M$ and $\partial U/\partial y=N$, and the recipe of this topic cannot be used. The next step would be to look for an integrating factor (Topic 2); Try it 9 shows that for this particular equation even that fails, so it needs a different method.', '')],
     r'Not exact ($\partial M/\partial y=0$ but $\partial N/\partial t=-1$).', cites=W(4))

D.CO('info', r"""**Calculus reminder: exponentials and trig functions.**

- $\dfrac{d}{dt}e^t=e^t$ and $\displaystyle\int e^t\,dt=e^t$.
- $\dfrac{d}{dt}\sin t=\cos t$, $\dfrac{d}{dt}\cos t=-\sin t$; so $\displaystyle\int\cos t\,dt=\sin t$ and $\displaystyle\int\sin t\,dt=-\cos t$.
- With partial derivatives the other variable is just a constant factor: $\dfrac{\partial}{\partial y}(e^t\,y)=e^t$ and $\dfrac{\partial}{\partial t}(y\sin t)=y\cos t$.""")

D.EX('With eᵗ and an initial condition',
     r'Solve $(e^ty+2t)\,dt+(e^t+3y^2)\,dy=0$ with $y(0)=1$.',
     [S(r'Read off $M$ and $N$.', r'M=e^ty+2t,\qquad N=e^t+3y^2'),
      S(r'Test: holding $t$ fixed, $e^ty$ is "a constant times $y$", so $\partial M/\partial y=e^t$. Holding $y$ fixed, $\partial(e^t)/\partial t=e^t$ and $3y^2$ is a constant. Equal, so exact.',
        r'\dfrac{\partial M}{\partial y}=e^t=\dfrac{\partial N}{\partial t}'),
      S(r'Integrate $M$ in $t$: $\int e^ty\,dt=y\,e^t$ ($y$ is a constant factor) and $\int2t\,dt=t^2$. Add $f(y)$.', r'U=e^ty+t^2+f(y)'),
      S(r'Match $N$: $\partial U/\partial y=e^t+f^{\prime}(y)$ must equal $e^t+3y^2$.', r'f^{\prime}(y)=3y^2\ \Longrightarrow\ f(y)=\int3y^2\,dy=y^3'),
      S(r'The general solution is $U=C$.', r'e^ty+t^2+y^3=C'),
      S(r'Use the initial condition: put $t=0$, $y=1$ into $U$. Remember $e^0=1$.', r'C=e^0\cdot1+0^2+1^3=2'),
      S(r'Check: differentiating $e^ty+t^2+y^3=2$ implicitly gives $e^ty+e^t\,y^\prime+2t+3y^2y^\prime=0$, i.e. $(e^ty+2t)+(e^t+3y^2)\,y^\prime=0$, the original ODE. Solving the cubic for $y$ is not needed: the implicit answer is a complete answer.', '')],
     r'$e^ty+t^2+y^3=2$.')

D.CO('warning', r"""**Common mistakes**

- **Losing a sign when rewriting.** For $2ty\,y^\prime=t^2-y^2$ the correct form is $(t^2-y^2)\,dt-2ty\,dy=0$, so $N=-2ty$. Writing $+2ty\,dy$ gives $\partial N/\partial t=+2y\neq-2y$ and you wrongly conclude "not exact".
- **Testing the wrong derivatives.** The test is $M$ differentiated by $y$ against $N$ differentiated by $t$ (the letters "cross over"), not $\partial M/\partial t$.
- **Adding the two integrals.** $\int M\,dt+\int N\,dy$ counts shared terms twice (Practice 6). Integrate one of them, then *match* the other to find $f(y)$.
- **Forgetting $f(y)$, or stopping at $U$.** The answer is the equation $U(t,y)=C$, and $C$ is fixed by the initial condition, not set to zero.""")

D.PR('Exact or not?',
     r"""Test each equation for exactness (do not solve).
1. $(2t+y)\,dt+(t+2y)\,dy=0$
2. $(t-y)\,dt+(t+y)\,dy=0$
3. $\cos y\,dt-t\sin y\,dy=0$""",
     [S(r'(1) $M=2t+y$, $N=t+2y$. Holding $t$ fixed, $\partial M/\partial y=1$; holding $y$ fixed, $\partial N/\partial t=1$. Equal: exact.', r'1=1'),
      S(r'(2) $M=t-y$, $N=t+y$. $\partial M/\partial y=-1$ but $\partial N/\partial t=+1$. Not exact.', r'-1\neq1'),
      S(r'(3) $M=\cos y$, $N=-t\sin y$. $\partial(\cos y)/\partial y=-\sin y$; holding $y$ fixed, $-t\sin y$ is "a constant times $t$", so $\partial N/\partial t=-\sin y$. Equal: exact.',
        r'-\sin y=-\sin y')],
     r'(1) exact (2) not exact (3) exact.', 'introductory')

D.PR('Your first full solve',
     r'Solve $(2t+y)\,dt+(t+2y)\,dy=0$.',
     [S(r'From Try it 1 this is exact with $M=2t+y$, $N=t+2y$.', r'\dfrac{\partial M}{\partial y}=1=\dfrac{\partial N}{\partial t}'),
      S(r'Integrate $M$ in $t$, holding $y$ fixed: $\int2t\,dt=t^2$ and $\int y\,dt=ty$.', r'U=t^2+ty+f(y)'),
      S(r'Match $N$: $\partial U/\partial y=t+f^{\prime}(y)=t+2y$, so $f^{\prime}(y)=2y$ and by the power rule $f(y)=y^2$.', r'f(y)=\int2y\,dy=y^2'),
      S(r'Write the solution as $U=C$.', r't^2+ty+y^2=C'),
      S(r'Check: implicitly, $2t+y+t\,y^\prime+2y\,y^\prime=0$, i.e. $(2t+y)+(t+2y)\,y^\prime=0$. Correct.', '')],
     r'$t^2+ty+y^2=C$.', 'introductory')

D.PR('Products and trig, with a starting point',
     r'Solve $(y^2+y\cos t)\,dt+(2ty+\sin t)\,dy=0$ with $y(\pi/2)=1$.',
     [S(r'Read off $M$ and $N$ and test. Holding $t$ fixed: $\partial(y^2)/\partial y=2y$ and $\partial(y\cos t)/\partial y=\cos t$. Holding $y$ fixed: $\partial(2ty)/\partial t=2y$ and $\partial(\sin t)/\partial t=\cos t$. Equal, so exact.',
        r'\dfrac{\partial M}{\partial y}=2y+\cos t=\dfrac{\partial N}{\partial t}'),
      S(r'Integrate $M$ in $t$: $\int y^2\,dt=ty^2$ and $\int y\cos t\,dt=y\sin t$.', r'U=ty^2+y\sin t+f(y)'),
      S(r'Match $N$: $\partial U/\partial y=2ty+\sin t+f^{\prime}(y)=2ty+\sin t$, so $f^{\prime}(y)=0$.', r'U=ty^2+y\sin t'),
      S(r'Apply $y(\pi/2)=1$: $\sin(\pi/2)=1$.', r'C=\dfrac{\pi}{2}\cdot1^2+1\cdot1=\dfrac{\pi}{2}+1'),
      S(r'Check: implicitly, $y^2+2ty\,y^\prime+y^\prime\sin t+y\cos t=0$, which regroups as $(y^2+y\cos t)+(2ty+\sin t)\,y^\prime=0$.', '')],
     r'$ty^2+y\sin t=\dfrac{\pi}{2}+1$.', 'intermediate')

D.PR('Start from y′ = …',
     r'Solve $\dfrac{dy}{dt}=-\dfrac{e^t+2ty^2}{2t^2y+3y^2}$ with $y(0)=1$.',
     [S(r'Cross-multiply: multiply by $(2t^2y+3y^2)\,dt$, then move everything to the left.',
        r'\begin{gathered}(2t^2y+3y^2)\,dy=-(e^t+2ty^2)\,dt \\ \Longrightarrow\ (e^t+2ty^2)\,dt \\ +\,(2t^2y+3y^2)\,dy=0\end{gathered}'),
      S(r'Test: $\partial(e^t+2ty^2)/\partial y=4ty$ and $\partial(2t^2y+3y^2)/\partial t=4ty$. Exact.', r'\dfrac{\partial M}{\partial y}=4ty=\dfrac{\partial N}{\partial t}'),
      S(r'Integrate $M$ in $t$: $\int e^t\,dt=e^t$ and $\int2ty^2\,dt=t^2y^2$.', r'U=e^t+t^2y^2+f(y)'),
      S(r'Match $N$: $\partial U/\partial y=2t^2y+f^{\prime}(y)=2t^2y+3y^2$, so $f^{\prime}(y)=3y^2$ and $f(y)=y^3$.', r'U=e^t+t^2y^2+y^3'),
      S(r'Apply $y(0)=1$.', r'C=e^0+0+1^3=2')],
     r'$e^t+t^2y^2+y^3=2$.', 'intermediate')

D.PR('Choose the constant that makes it exact',
     r"""Consider $(2t\sin y+y)\,dt+(t^2\cos y+kt)\,dy=0$.
1. Find the constant $k$ that makes the equation exact.
2. With that $k$, solve it with $y(1)=\pi/2$.""",
     [S(r'Compute both test derivatives. Holding $t$ fixed: $\partial(2t\sin y)/\partial y=2t\cos y$ and $\partial y/\partial y=1$. Holding $y$ fixed: $\partial(t^2\cos y)/\partial t=2t\cos y$ and $\partial(kt)/\partial t=k$.',
        r'\dfrac{\partial M}{\partial y}=2t\cos y+1,\qquad\dfrac{\partial N}{\partial t}=2t\cos y+k'),
      S(r'They are equal for every $t,y$ only when $k=1$.', r'k=1'),
      S(r'Integrate $M$ in $t$: $\int2t\sin y\,dt=t^2\sin y$ ($\sin y$ is a constant factor) and $\int y\,dt=ty$.', r'U=t^2\sin y+ty+f(y)'),
      S(r'Match $N=t^2\cos y+t$: $\partial U/\partial y=t^2\cos y+t+f^{\prime}(y)$, so $f^{\prime}(y)=0$.', r'U=t^2\sin y+ty'),
      S(r'Apply $y(1)=\pi/2$, using $\sin(\pi/2)=1$.', r'C=1\cdot1+1\cdot\dfrac{\pi}{2}=1+\dfrac{\pi}{2}')],
     r'(1) $k=1$. (2) $t^2\sin y+ty=1+\dfrac{\pi}{2}$.', 'advanced')

# ====================================================================== Topic 2
D.H('Topic 2: Making an equation exact: integrating factors')

D.P(r"""**The big idea.** Multiplying an equation by a nonzero function $\mu(t,y)$ (Greek "mu", called an **integrating factor**) does not change which curves solve it: $\mu\,(M\,dt+N\,dy)=0$ holds exactly where $M\,dt+N\,dy=0$ does. But it *does* change $M$ and $N$ into $\mu M$ and $\mu N$, and therefore changes the partial derivatives in the exactness test. So a non-exact equation can sometimes be "repaired" into an exact one. Guessing $\mu$ is hard in general, but the lecture (from Spiegel's textbook) gives two quick tests that find a $\mu$ depending on **only $t$** or **only $y$**: compute a certain ratio, and if one variable cancels out, the factor is $e^{\int(\text{ratio})}$. You already used one of these: the Week 3 integrating factor for linear equations is exactly Test 1 (Example 10).""",
    cites=W(4, 5))

D.CO('tip', r"""**The method (integrating factors)**

1. Write $M\,dt+N\,dy=0$ and compute $\partial M/\partial y$ and $\partial N/\partial t$. If equal, it is already exact (Topic 1).
2. **Test 1:** simplify $\dfrac{1}{N}\Big(\dfrac{\partial M}{\partial y}-\dfrac{\partial N}{\partial t}\Big)$. If **only $t$** is left (call it $f(t)$), then $\mu=e^{\int f(t)\,dt}$.
3. **Test 2:** otherwise simplify $\dfrac{1}{M}\Big(\dfrac{\partial N}{\partial t}-\dfrac{\partial M}{\partial y}\Big)$ (note: order swapped, divide by $M$). If **only $y$** is left (call it $g(y)$), then $\mu=e^{\int g(y)\,dy}$.
4. Multiply **both** $M$ and $N$ by $\mu$, and re-test: it must now be exact.
5. Solve with the Topic 1 recipe ($U=C$). Finally check whether $\mu$ was zero or undefined somewhere (e.g. $\mu=1/y^2$ at $y=0$): such a line may be a **lost solution** of the original equation.""",
     cites=W(5))

D.P(r"""The two tests (Spiegel's Theorems 1 and 2 in the lecture). The $f(t)$ and $g(y)$ here are new names for "the ratio", unrelated to the $f(y)$ of Topic 1. They work because if $\mu$ depends on $t$ alone, the test for $\mu M\,dt+\mu N\,dy$ reads $\mu\,\partial M/\partial y=\mu^\prime N+\mu\,\partial N/\partial t$, i.e. $\mu^\prime/\mu=$ the Test 1 ratio, whose solution is $\mu=e^{\int f\,dt}$ (and the same with $t$ and $y$ swapped for Test 2). The third formula is the repaired equation, which is exact and is solved as in Topic 1.""",
    cites=W(5))
D.EQ(r'\begin{gathered}\dfrac{1}{N}\Big(\dfrac{\partial M}{\partial y}-\dfrac{\partial N}{\partial t}\Big)=f(t) \\ \Longrightarrow\ \mu=e^{\int f(t)\,dt}\end{gathered}', cites=W(5))
D.EQ(r'\begin{gathered}\dfrac{1}{M}\Big(\dfrac{\partial N}{\partial t}-\dfrac{\partial M}{\partial y}\Big)=g(y) \\ \Longrightarrow\ \mu=e^{\int g(y)\,dy}\end{gathered}', cites=W(5))
D.EQ(r'(\mu M)\,dt+(\mu N)\,dy=0', cites=W(5))

D.CO('info', r"""**Calculus reminder: logarithms and exponentials** (every $\mu$ is $e^{\int\dots}$).

- $\displaystyle\int\dfrac{1}{y}\,dy=\ln|y|$, and more generally $\displaystyle\int\dfrac{a}{y}\,dy=a\ln|y|$.
- $e^{\ln A}=A$, and $a\ln A=\ln(A^a)$. So $e^{2\ln|y|}=e^{\ln(y^2)}=y^2$, $e^{\ln|t|}=|t|$, and $e^{-2\ln|t|}=\dfrac{1}{t^2}$.
- $\displaystyle\int k\,dt=kt$, so a constant ratio $k$ gives $\mu=e^{kt}$.
- Any constant multiple of an integrating factor also works, so we drop absolute values and constants when convenient (e.g. use $\mu=t$ for $t>0$).
- Power rule with negative powers: $\dfrac{d}{dy}\Big(\dfrac1y\Big)=\dfrac{d}{dy}y^{-1}=-y^{-2}=-\dfrac{1}{y^2}$.""")

D.EX('Lecture (e): finding μ = y² with Test 2',
     r'Show that $y\,dt+(3+3t-y)\,dy=0$ is not exact, find an integrating factor, and check that the new equation is exact.',
     [S(r'Read off $M$, $N$ and test. $\partial y/\partial y=1$; holding $y$ fixed, $\partial(3+3t-y)/\partial t=3$. Not equal, so not exact.',
        r'M=y,\quad N=3+3t-y,\qquad \dfrac{\partial M}{\partial y}=1\neq3=\dfrac{\partial N}{\partial t}'),
      S(r'Try Test 1: divide $\partial M/\partial y-\partial N/\partial t$ by $N$. Both $t$ and $y$ remain, so Test 1 fails.',
        r'\dfrac{1}{N}(1-3)=\dfrac{-2}{3+3t-y}'),
      S(r'Try Test 2: divide $\partial N/\partial t-\partial M/\partial y$ by $M$. Only $y$ remains, so Test 2 works.',
        r'\dfrac{1}{M}(3-1)=\dfrac{2}{y}=g(y)'),
      S(r'Build $\mu$: integrate $g(y)=\tfrac{2}{y}$ using $\int\tfrac1y\,dy=\ln|y|$, then simplify the exponential with $e^{2\ln|y|}=e^{\ln y^2}=y^2$.',
        r'\mu=e^{\int\frac{2}{y}\,dy}=e^{2\ln|y|}=y^2'),
      S(r'Multiply **both** $M$ and $N$ by $y^2$ (this is Eq. (4.13) of the lecture).', r'y^3\,dt+(3y^2+3ty^2-y^3)\,dy=0'),
      S(r'Re-test with the new $M=y^3$ and $N=3y^2+3ty^2-y^3$: $\partial(y^3)/\partial y=3y^2$; holding $y$ fixed, only $3ty^2$ depends on $t$, giving $3y^2$. Equal: now exact. (Finishing the solution is pre-tutorial 4: Try it 6.)',
        r'\begin{gathered}\dfrac{\partial (y^3)}{\partial y}=3y^2 \\ \dfrac{\partial}{\partial t}(3y^2+3ty^2-y^3)=3y^2\end{gathered}')],
     r'Not exact; Test 2 gives $\mu=y^2$, and $y^3\,dt+(3y^2+3ty^2-y^3)\,dy=0$ is exact.', cites=W(4, 5))

D.EX('Test 1 gives μ = t',
     r'Solve $(t^2+y^2+t)\,dt+ty\,dy=0$ with $y(1)=1$ (take $t>0$).',
     [S(r'Test: holding $t$ fixed, $\partial(t^2+y^2+t)/\partial y=2y$; holding $y$ fixed, $\partial(ty)/\partial t=y$. Not exact.',
        r'\dfrac{\partial M}{\partial y}=2y\neq y=\dfrac{\partial N}{\partial t}'),
      S(r'Test 1: divide $\partial M/\partial y-\partial N/\partial t=2y-y$ by $N=ty$. The $y$ cancels, leaving a function of $t$ only.', r'\dfrac{2y-y}{ty}=\dfrac{1}{t}=f(t)'),
      S(r'Build $\mu$: $\int\tfrac1t\,dt=\ln t$ (for $t>0$) and $e^{\ln t}=t$.', r'\mu=e^{\int\frac1t\,dt}=e^{\ln t}=t'),
      S(r'Multiply both parts by $t$ and re-test: $\partial(t^3+ty^2+t^2)/\partial y=2ty$ and $\partial(t^2y)/\partial t=2ty$. Exact.',
        r'(t^3+ty^2+t^2)\,dt+t^2y\,dy=0'),
      S(r'Integrate the new $M$ in $t$ with the power rule ($y^2$ is a constant factor).', r'U=\dfrac{t^4}{4}+\dfrac{t^2y^2}{2}+\dfrac{t^3}{3}+f(y)'),
      S(r'Match the new $N=t^2y$: $\partial U/\partial y=t^2y+f^{\prime}(y)$, so $f^{\prime}(y)=0$. Multiply $U=C$ by 12 to clear fractions.',
        r'3t^4+6t^2y^2+4t^3=C'),
      S(r'Apply $y(1)=1$.', r'C=3+6+4=13'),
      S(r'Solve for $y$: isolate $y^2$, then take the positive square root because $y(1)=1>0$.', r'y=\sqrt{\dfrac{13-3t^4-4t^3}{6t^2}}')],
     r'$3t^4+6t^2y^2+4t^3=13$, i.e. $y=\sqrt{\dfrac{13-3t^4-4t^3}{6t^2}}$.')

D.CO('info', r"""**Calculus reminder: integrating $e^{kt}$ and integration by parts.**

- $\displaystyle\int e^{kt}\,dt=\dfrac{e^{kt}}{k}$ (check: differentiating $e^{kt}$ gives $k\,e^{kt}$, so divide by $k$). Example: $\displaystyle\int e^{2t}\,dt=\tfrac12e^{2t}$.
- **Integration by parts:** $\displaystyle\int u\,dv=uv-\int v\,du$. For $\displaystyle\int2t\,e^t\,dt$ take $u=2t$ (so $du=2\,dt$) and $dv=e^t\,dt$ (so $v=e^t$): the result is $2te^t-\displaystyle\int2e^t\,dt=2te^t-2e^t$.""")

D.EX('Test 1 gives μ = eᵗ',
     r'Solve $(2t+y^2)\,dt+2y\,dy=0$ with $y(0)=1$.',
     [S(r'Test: $\partial(2t+y^2)/\partial y=2y$ but $\partial(2y)/\partial t=0$. Not exact.', r'\dfrac{\partial M}{\partial y}=2y\neq0=\dfrac{\partial N}{\partial t}'),
      S(r'Test 1: the ratio is the constant 1, which counts as "a function of $t$ only".', r'\dfrac{1}{N}(2y-0)=\dfrac{2y}{2y}=1=f(t)'),
      S(r'Build $\mu$: $\int1\,dt=t$.', r'\mu=e^{\int1\,dt}=e^t'),
      S(r'Multiply both parts by $e^t$ and re-test: $\partial(2te^t+y^2e^t)/\partial y=2ye^t$ and $\partial(2ye^t)/\partial t=2ye^t$. Exact.',
        r'(2te^t+y^2e^t)\,dt+2ye^t\,dy=0'),
      S(r'This time integrate $N$ first, because $\int2ye^t\,dy$ is easy ($e^t$ is a constant factor, $\int2y\,dy=y^2$). The unknown "constant" is now a function $g(t)$.',
        r'U=\int2ye^t\,dy=y^2e^t+g(t)'),
      S(r'Match $M$: $\partial U/\partial t=y^2e^t+g^{\prime}(t)$ must equal $2te^t+y^2e^t$.', r'g^{\prime}(t)=2te^t'),
      S(r'Integrate by parts with $u=2t$, $dv=e^t\,dt$ (see the reminder above).', r'g(t)=2te^t-2e^t'),
      S(r'Collect: $U=y^2e^t+2te^t-2e^t=e^t(y^2+2t-2)$. Apply $y(0)=1$ with $e^0=1$.', r'C=1\cdot(1+0-2)=-1'),
      S(r'Solve for $y$: divide $e^t(y^2+2t-2)=-1$ by $e^t$ (i.e. multiply by $e^{-t}$), then take the positive root since $y(0)=1>0$.',
        r'y^2=2-2t-e^{-t}\ \Longrightarrow\ y=\sqrt{2-2t-e^{-t}}')],
     r'$e^t(y^2+2t-2)=-1$, i.e. $y=\sqrt{2-2t-e^{-t}}$ (valid while the root is real).')

D.EX('A linear ODE is a special case (the Week 3 factor)',
     r'Solve $\dfrac{dy}{dt}+2y=4$ with $y(0)=0$ using an integrating factor from Test 1. (This is an RC capacitor charging toward $2\,\mathrm{V}$ with time constant $\tau=0.5\,\mathrm{s}$; $\tau$, "tau", is the time to cover 63% of the change.)',
     [S(r'Multiply by $dt$ and bring everything to the left: the $dy$ term has coefficient 1.', r'(2y-4)\,dt+1\,dy=0,\qquad M=2y-4,\quad N=1'),
      S(r'Test: $\partial M/\partial y=2$, $\partial N/\partial t=0$. Not exact.', r'2\neq0'),
      S(r'Test 1: the ratio is 2, a function of $t$ only (a constant). In general, for $\dfrac{dy}{dt}+a(t)\,y=b(t)$ (Week 3 called the forcing $f(t)$; we write $b(t)$ here because $f$ is already the Test 1 ratio) we get $M=a(t)y-b(t)$, $N=1$ and the ratio is exactly $a(t)$, so $\mu=e^{\int a(t)\,dt}$: the Week 3 integrating factor.',
        r'\dfrac{1}{N}(2-0)=2\ \Longrightarrow\ \mu=e^{\int2\,dt}=e^{2t}'),
      S(r'Multiply both parts by $e^{2t}$ and re-test: $\partial[(2y-4)e^{2t}]/\partial y=2e^{2t}$ and $\partial(e^{2t})/\partial t=2e^{2t}$. Exact.',
        r'(2y-4)e^{2t}\,dt+e^{2t}\,dy=0'),
      S(r'Integrate $N$ first: $\int e^{2t}\,dy=ye^{2t}$ ($e^{2t}$ is a constant factor). Add $g(t)$.', r'U=ye^{2t}+g(t)'),
      S(r'Match $M$: $\partial U/\partial t=2ye^{2t}+g^{\prime}(t)$ must equal $2ye^{2t}-4e^{2t}$, so $g^{\prime}(t)=-4e^{2t}$. Integrate using $\int e^{2t}\,dt=\tfrac12e^{2t}$.',
        r'g(t)=-4\cdot\tfrac12e^{2t}=-2e^{2t}\ \Longrightarrow\ U=(y-2)e^{2t}'),
      S(r'Apply $y(0)=0$, then solve for $y$ by multiplying by $e^{-2t}$ and adding 2.', r'C=(0-2)\cdot1=-2\ \Longrightarrow\ y=2-2e^{-2t}')],
     r'$y(t)=2-2e^{-2t}$ (same as with the Week 3 method).')

D.CHART(r'Example 10: $y=2-2e^{-2t}$ rises from 0 and levels off at 2. At $t=\tau=0.5$ it has covered 63% of the way (about 1.26); after about $5\tau=2.5$ it is essentially at 2.',
        order=1, a=-2.0, forcing=4.0, y0=0.0, duration=3.0)

D.EX('Two integrating factors and a lost solution',
     r'Solve $y\,dt-t\,dy=0$ and make sure no solution is lost.',
     [S(r'Test: $\partial y/\partial y=1$, $\partial(-t)/\partial t=-1$. Not exact.', r'M=y,\quad N=-t,\qquad 1\neq-1'),
      S(r'Here **both** tests work. Test 1: $\dfrac1N\Big(\dfrac{\partial M}{\partial y}-\dfrac{\partial N}{\partial t}\Big)=\dfrac{1-(-1)}{-t}=-\dfrac2t$ (only $t$), so $\mu=e^{\int -2/t\,dt}=e^{-2\ln|t|}=\dfrac1{t^2}$. Test 2 also gives a function of $y$ only:', r'\dfrac{1}{M}\Big(\dfrac{\partial N}{\partial t}-\dfrac{\partial M}{\partial y}\Big)=\dfrac{-1-1}{y}=-\dfrac{2}{y}'),
      S(r'Use Test 2: $\int-\tfrac2y\,dy=-2\ln|y|$, and $e^{-2\ln|y|}=\tfrac{1}{y^2}$.', r'\mu=\dfrac{1}{y^2}'),
      S(r'Multiply both parts by $1/y^2$ and re-test (power rule: $\tfrac{d}{dy}\tfrac1y=-\tfrac1{y^2}$). Exact.',
        r'\begin{gathered}\dfrac{1}{y}\,dt-\dfrac{t}{y^2}\,dy=0 \\ \dfrac{\partial}{\partial y}\Big(\dfrac1y\Big)=-\dfrac{1}{y^2} \\ \dfrac{\partial}{\partial t}\Big(-\dfrac{t}{y^2}\Big)=-\dfrac{1}{y^2}\end{gathered}'),
      S(r'Integrate $M=1/y$ in $t$: $\int\tfrac1y\,dt=\tfrac{t}{y}$. Matching $N$: $\partial U/\partial y=-t/y^2+f^{\prime}(y)=-t/y^2$, so $f$ is constant.',
        r'U=\dfrac{t}{y}=C\ \Longrightarrow\ y=\dfrac{t}{C}'),
      S(r'**Lost solution check.** $\mu=1/y^2$ is undefined at $y=0$, and $t/y=C$ can never give $y=0$. But $y\equiv0$ does solve the original: $dy=0$ and $M=0$, so $0\,dt-t\cdot0=0$. So add it back. Writing $k=1/C$, all solutions are the lines $y=kt$, including $k=0$.',
        r'y=kt'),
      S(r'(With Test 1 instead, $\mu=1/t^2$ gives $U=-y/t=C$, i.e. $y=-Ct$: the same family. That route keeps $y=0$ but cannot describe the vertical line $t=0$.)', '')],
     r'$y=kt$ for any constant $k$; the solution $y=0$ ($k=0$) is lost by $\mu=1/y^2$ and must be added back.')

D.CO('warning', r"""**Common mistakes**

- **Mixing up the two ratios.** Test 1 is $(\partial M/\partial y-\partial N/\partial t)$ divided by $N$; Test 2 is the *opposite* difference $(\partial N/\partial t-\partial M/\partial y)$ divided by $M$.
- **Accepting the wrong variable.** Test 2 needs a function of $y$ only. In lecture (d) the Test 2 ratio is $-1/t$: that depends on $t$, so Test 2 *fails* (Try it 9).
- **Multiplying only one part.** $\mu$ multiplies both $M$ and $N$; always re-test exactness before integrating.
- **Simplifying $e^{2\ln|y|}$ as $2y$.** It is $y^2$ (because $2\ln|y|=\ln y^2$). And remember to check lines where $\mu$ is $0$ or undefined (like $y=0$ for $\mu=1/y^2$) for lost solutions.""")

D.PR('Pre-tutorial 4: finish lecture (e)',
     r'Find the solution of $y^3\,dt+y^2(3+3t-y)\,dy=0$ (Eq. (4.13): the lecture equation $y\,dt+(3+3t-y)\,dy=0$ multiplied by $\mu=y^2$).',
     [S(r'Expand $N$ and confirm exactness: $M=y^3$, $N=3y^2+3ty^2-y^3$, and both test derivatives equal $3y^2$ (Example 7).',
        r'\dfrac{\partial M}{\partial y}=3y^2=\dfrac{\partial N}{\partial t}'),
      S(r'Integrate $M$ in $t$: with $y$ fixed, $y^3$ is a constant, so $\int y^3\,dt=ty^3$. Add $f(y)$.', r'U=ty^3+f(y)'),
      S(r'Match $N$: $\partial U/\partial y=3ty^2+f^{\prime}(y)$. Set equal to $3y^2+3ty^2-y^3$; the $3ty^2$ cancels.', r'f^{\prime}(y)=3y^2-y^3'),
      S(r'Integrate with the power rule: $\int3y^2\,dy=y^3$ and $\int y^3\,dy=\tfrac{y^4}{4}$.', r'f(y)=y^3-\dfrac{y^4}{4}'),
      S(r'Write $U=C$ and multiply by 4 (renaming $4C$ as $C$).', r'ty^3+y^3-\dfrac{y^4}{4}=C\ \Longrightarrow\ 4(t+1)y^3-y^4=C'),
      S(r'Lost solutions? $\mu=y^2$ is zero at $y=0$. But $y\equiv0$ is already in the family ($C=0$), so nothing is lost.', ''),
      S(r'Check: differentiate implicitly: $4y^3+12(t+1)y^2y^\prime-4y^3y^\prime=0$. Divide by $4y^2$: $y+(3+3t-y)\,y^\prime=0$, the original equation.', ''),
      S(r'Bonus: the answer is linear in $t$, so you can write $t$ as a function of $y$ instead of $y$ as a function of $t$.', r't=\dfrac{C+y^4}{4y^3}-1')],
     r'$ty^3+y^3-\dfrac{y^4}{4}=C$, equivalently $4(t+1)y^3-y^4=C$.', 'intermediate', cites=D.cite('T4', 1) + W(5))

D.PR('Test 2 gives μ = y',
     r'Solve $y\,dt+(2t+y^2)\,dy=0$ (take $y>0$).',
     [S(r'Test: $\partial y/\partial y=1$, $\partial(2t+y^2)/\partial t=2$. Not exact.', r'1\neq2'),
      S(r'Test 1 ratio: $(1-2)/(2t+y^2)$ still contains $y$, so it fails. Test 2 ratio: only $y$.', r'\dfrac{1}{M}(2-1)=\dfrac{1}{y}=g(y)'),
      S(r'Build $\mu$: $\int\tfrac1y\,dy=\ln y$ and $e^{\ln y}=y$.', r'\mu=y'),
      S(r'Multiply both parts by $y$ and re-test: $\partial(y^2)/\partial y=2y$ and $\partial(2ty+y^3)/\partial t=2y$. Exact.', r'y^2\,dt+(2ty+y^3)\,dy=0'),
      S(r'Integrate $M=y^2$ in $t$: $\int y^2\,dt=ty^2$. Match $N$: $2ty+f^{\prime}(y)=2ty+y^3$, so $f^{\prime}(y)=y^3$ and $f(y)=\tfrac{y^4}{4}$.',
        r'U=ty^2+\dfrac{y^4}{4}')],
     r'$ty^2+\dfrac{y^4}{4}=C$ (or $4ty^2+y^4=C$).', 'introductory')

D.PR('Test 1 after factoring',
     r'Solve $(3ty+y^2)\,dt+(t^2+ty)\,dy=0$ (take $t>0$).',
     [S(r'Test: $\partial(3ty+y^2)/\partial y=3t+2y$ and $\partial(t^2+ty)/\partial t=2t+y$. Not exact; the difference is $t+y$.', r'(3t+2y)-(2t+y)=t+y'),
      S(r'Test 1: factor $N=t^2+ty=t(t+y)$, and the $(t+y)$ cancels.', r'\dfrac{t+y}{t(t+y)}=\dfrac1t=f(t)\ \Longrightarrow\ \mu=e^{\ln t}=t'),
      S(r'Multiply both parts by $t$; re-test: both derivatives are $3t^2+2ty$. Exact.', r'(3t^2y+ty^2)\,dt+(t^3+t^2y)\,dy=0'),
      S(r'Integrate $M$ in $t$: $\int3t^2y\,dt=t^3y$, $\int ty^2\,dt=\tfrac{t^2y^2}{2}$.', r'U=t^3y+\dfrac{t^2y^2}{2}+f(y)'),
      S(r'Match $N$: $\partial U/\partial y=t^3+t^2y+f^{\prime}(y)=t^3+t^2y$, so $f$ is constant.', r't^3y+\dfrac{t^2y^2}{2}=C')],
     r'$t^3y+\dfrac{t^2y^2}{2}=C$ (or $2t^3y+t^2y^2=C$).', 'intermediate')

D.PR('When neither test works',
     r'For lecture (d), $\dfrac{dy}{dt}=\dfrac{t}{t+y}$, written as $t\,dt-(t+y)\,dy=0$: show that neither integrating-factor test gives a $\mu$.',
     [S(r'From Example 5: $M=t$, $N=-t-y$, $\partial M/\partial y=0$, $\partial N/\partial t=-1$.', r'\dfrac{\partial M}{\partial y}-\dfrac{\partial N}{\partial t}=0-(-1)=1'),
      S(r'Test 1 divides by $N$. The result contains $y$, so it is not a function of $t$ alone: Test 1 fails.', r'\dfrac{1}{N}\cdot1=-\dfrac{1}{t+y}'),
      S(r'Test 2 divides the opposite difference by $M$. The result $-1/t$ is a function of $t$, but Test 2 needs a function of $y$ only: Test 2 fails too.',
        r'\dfrac{1}{M}\Big(\dfrac{\partial N}{\partial t}-\dfrac{\partial M}{\partial y}\Big)=\dfrac{-1}{t}'),
      S(r'Conclusion: these two tests only find factors depending on one variable. This equation needs a different method, which is not part of this week.', '')],
     r'Test 1 ratio $=-\dfrac{1}{t+y}$ (has $y$), Test 2 ratio $=-\dfrac{1}{t}$ (has $t$): neither applies.', 'intermediate', cites=W(4))

D.PR('A linear IVP by the exact route',
     r'Solve $\dfrac{dy}{dt}+\dfrac{y}{t}=3t$ for $t>0$ with $y(1)=2$, by writing it as $M\,dt+N\,dy=0$ and using Test 1.',
     [S(r'Multiply by $dt$ and move everything left.', r'\Big(\dfrac{y}{t}-3t\Big)dt+1\,dy=0'),
      S(r'Test 1: $\partial M/\partial y=\tfrac1t$, $\partial N/\partial t=0$, $N=1$. Ratio $\tfrac1t$, so $\mu=e^{\ln t}=t$.', r'\mu=t'),
      S(r'Multiply both parts by $t$; re-test: $\partial(y-3t^2)/\partial y=1=\partial t/\partial t$. Exact.', r'(y-3t^2)\,dt+t\,dy=0'),
      S(r'Integrate $N=t$ in $y$: $\int t\,dy=ty$, plus $g(t)$. Match $M$: $y+g^{\prime}(t)=y-3t^2$, so $g^{\prime}=-3t^2$ and $g=-t^3$.', r'U=ty-t^3'),
      S(r'Apply $y(1)=2$, then solve for $y$ (add $t^3$, divide by $t$).', r'C=2-1=1\ \Longrightarrow\ y=\dfrac{1+t^3}{t}=t^2+\dfrac1t'),
      S(r'Check: $y^\prime=2t-\tfrac1{t^2}$ and $\tfrac{y}{t}=t+\tfrac{1}{t^2}$; their sum is $3t$. And $y(1)=1+1=2$.', '')],
     r'$y=t^2+\dfrac1t$.', 'advanced')

# ====================================================================== Mixed practice
D.H('Mixed practice (exam style)')
D.P('Mixed topics, like the midterm. Try each one before opening the solution.')

D.PR('Which method?',
     r"""For each equation, say which method fits: separable, linear (Week 3), exact, or exact after an integrating factor (give $\mu$).
1. $\dfrac{dy}{dt}=ty^2$
2. $\dfrac{dy}{dt}+3y=e^t$
3. $(y+2t)\,dt+(t+1)\,dy=0$
4. $(ty+1)\,dt+t^2\,dy=0$ ($t>0$)

Then solve equation 3.""",
     [S(r'(1) The right side is a function of $t$ times a function of $y$, so it is separable: $\dfrac{dy}{y^2}=t\,dt$.', ''),
      S(r'(2) It has the form $\dfrac{dy}{dt}+a(t)y=b(t)$ with $a=3$: linear, with $\mu=e^{3t}$.', ''),
      S(r'(3) $\partial(y+2t)/\partial y=1$ and $\partial(t+1)/\partial t=1$: exact.', ''),
      S(r'(4) $\partial(ty+1)/\partial y=t$, $\partial(t^2)/\partial t=2t$: not exact. Test 1 ratio is a function of $t$ only, so integrate it ($\int-\tfrac1t\,dt=-\ln t$).',
        r'\dfrac{t-2t}{t^2}=-\dfrac1t\ \Longrightarrow\ \mu=e^{-\ln t}=\dfrac1t'),
      S(r'Solve (3): integrate $M$ in $t$: $\int y\,dt=ty$, $\int2t\,dt=t^2$. Match $N$: $t+f^{\prime}(y)=t+1$, so $f(y)=y$.', r'ty+t^2+y=C')],
     r'(1) separable (2) linear, $\mu=e^{3t}$ (3) exact (4) integrating factor $\mu=1/t$. Equation 3: $ty+t^2+y=C$.', 'introductory', label='Practice 1')

D.PR('Exact IVP, then an explicit y',
     r"""Consider $(3t^2y-\sin t)\,dt+(t^3+y)\,dy=0$ with $y(0)=2$.
1. Show that the equation is exact.
2. Solve the initial-value problem (implicit form).
3. Solve for $y(t)$ explicitly.""",
     [S(r'(1) Holding $t$ fixed, $\partial(3t^2y-\sin t)/\partial y=3t^2$. Holding $y$ fixed, $\partial(t^3+y)/\partial t=3t^2$. Exact.', r'\dfrac{\partial M}{\partial y}=3t^2=\dfrac{\partial N}{\partial t}'),
      S(r'(2) Integrate $M$ in $t$: $\int3t^2y\,dt=t^3y$ and $\int(-\sin t)\,dt=\cos t$ (because $\tfrac{d}{dt}\cos t=-\sin t$).', r'U=t^3y+\cos t+f(y)'),
      S(r'Match $N$: $t^3+f^{\prime}(y)=t^3+y$, so $f^{\prime}(y)=y$ and $f(y)=\tfrac{y^2}{2}$.', r'U=t^3y+\cos t+\dfrac{y^2}{2}'),
      S(r'Apply $y(0)=2$ with $\cos0=1$.', r'C=0+1+\dfrac{4}{2}=3'),
      S(r'(3) Multiply $U=3$ by 2 and collect powers of $y$: it is a quadratic in $y$.', r'y^2+2t^3y+(2\cos t-6)=0'),
      S(r'Quadratic formula with $a=1$, $b=2t^3$, $c=2\cos t-6$; the $\pm\sqrt{\ }$ simplifies after dividing by 2.', r'y=-t^3\pm\sqrt{t^6-2\cos t+6}'),
      S(r'Pick the sign from $y(0)=2$: the plus sign gives $0+\sqrt{0-2+6}=2$ (the minus sign would give $-2$).', r'y=-t^3+\sqrt{t^6-2\cos t+6}')],
     r'(1) exact (2) $t^3y+\cos t+\dfrac{y^2}{2}=3$ (3) $y=-t^3+\sqrt{t^6-2\cos t+6}$.', 'advanced', label='Practice 2')

D.PR('Separable, and also exact',
     r"""Consider $\dfrac{dy}{dt}=e^{t-y}$ with $y(0)=\ln2$.
1. Solve it by separating variables (Week 3).
2. Show that the separated form $e^t\,dt-e^y\,dy=0$ is exact and gives the same answer.""",
     [S(r'(1) Split the exponential with $e^{t-y}=e^t\,e^{-y}$, then multiply both sides by $e^y\,dt$ to separate.', r'e^y\,dy=e^t\,dt'),
      S(r'Integrate both sides ($\int e^y\,dy=e^y$, $\int e^t\,dt=e^t$).', r'e^y=e^t+C'),
      S(r'Apply $y(0)=\ln2$: $e^{\ln2}=2$ and $e^0=1$.', r'2=1+C\ \Longrightarrow\ C=1'),
      S(r'Take $\ln$ of both sides to get $y$.', r'y=\ln(e^t+1)'),
      S(r'(2) $M=e^t$ has no $y$ and $N=-e^y$ has no $t$, so both test derivatives are $0$: exact. (Every separated equation is exact for this reason.) Careful with names: Week 3 wrote separable equations as $N(y)\,\dfrac{dy}{dt}=M(t)$; in this week’s form $M\,dt+N\,dy=0$ that becomes $M\,dt-N\,dy=0$, which is why this week’s $N=-e^y$ has a minus sign.',r'U=\int e^t\,dt+f(y)=e^t+f(y),\quad f^{\prime}(y)=-e^y'),
      S(r'So $U=e^t-e^y=C$, which is the same as $e^y=e^t-C$. With $y(0)=\ln2$, $C=1-2=-1$, giving $e^y=e^t+1$ again.', '')],
     r'$y=\ln(e^t+1)$; the exact route gives $e^t-e^y=-1$, the same curve.', 'intermediate', label='Practice 3')

D.PR('Integrating factor with an initial condition',
     r'Solve $(2y^2+3t)\,dt+2ty\,dy=0$ with $y(1)=2$ (take $t>0$).',
     [S(r'Test: $\partial(2y^2+3t)/\partial y=4y$ and $\partial(2ty)/\partial t=2y$. Not exact.', r'4y\neq2y'),
      S(r'Test 1: the $y$ cancels.', r'\dfrac{4y-2y}{2ty}=\dfrac{1}{t}\ \Longrightarrow\ \mu=e^{\ln t}=t'),
      S(r'Multiply both parts by $t$; re-test: both derivatives are $4ty$. Exact.', r'(2ty^2+3t^2)\,dt+2t^2y\,dy=0'),
      S(r'Integrate $M$ in $t$: $\int2ty^2\,dt=t^2y^2$, $\int3t^2\,dt=t^3$. Match $N$: $2t^2y+f^{\prime}(y)=2t^2y$, so $f$ is constant.', r'U=t^2y^2+t^3'),
      S(r'Apply $y(1)=2$.', r'C=1\cdot4+1=5'),
      S(r'Solve: $y^2=\dfrac{5-t^3}{t^2}$; take the positive root because $y(1)=2>0$.', r'y=\dfrac{\sqrt{5-t^3}}{t}\quad(0<t<5^{1/3})')],
     r'$t^2y^2+t^3=5$, i.e. $y=\dfrac{\sqrt{5-t^3}}{t}$.', 'intermediate', label='Practice 4')

D.PR('Test 2 gives an exponential',
     r'Solve $dt+(t+2y)\,dy=0$ with $y=0$ when $t=0$. Give the answer as $t$ in terms of $y$.',
     [S(r'Here $M=1$ and $N=t+2y$. Test: $\partial M/\partial y=0$, $\partial N/\partial t=1$. Not exact.', r'0\neq1'),
      S(r'Test 1 ratio $(0-1)/(t+2y)$ contains $y$: fails. Test 2 ratio: only a constant, which counts as a function of $y$.', r'\dfrac{1}{M}(1-0)=1\ \Longrightarrow\ \mu=e^{\int1\,dy}=e^y'),
      S(r'Multiply both parts by $e^y$; re-test: $\partial(e^y)/\partial y=e^y$ and $\partial[e^y(t+2y)]/\partial t=e^y$. Exact.', r'e^y\,dt+e^y(t+2y)\,dy=0'),
      S(r'Integrate $M=e^y$ in $t$: $\int e^y\,dt=te^y$. Match $N$: $te^y+f^{\prime}(y)=te^y+2ye^y$.', r'f^{\prime}(y)=2ye^y'),
      S(r'Integrate by parts with $u=2y$, $dv=e^y\,dy$: $\int2ye^y\,dy=2ye^y-\int2e^y\,dy=2ye^y-2e^y$.', r'U=e^y(t+2y-2)'),
      S(r'Apply $t=0$, $y=0$: $C=1\cdot(0+0-2)=-2$. Divide by $e^y$ and solve for $t$.', r't=2-2y-2e^{-y}'),
      S(r'Check: $\tfrac{dt}{dy}=-2+2e^{-y}$, while the ODE says $\tfrac{dt}{dy}=-(t+2y)=-(2-2e^{-y})$. Equal.', '')],
     r'$e^y(t+2y-2)=-2$, i.e. $t=2-2y-2e^{-y}$.', 'advanced', label='Practice 5')

D.PR('Spot the mistake',
     r"""A student solves $(2ty+1)\,dt+(t^2+4y)\,dy=0$ by computing $\int M\,dt=t^2y+t$ and $\int N\,dy=t^2y+2y^2$ and adding them, to get $U=2t^2y+t+2y^2$.
1. Show that this $U$ is wrong.
2. Find the correct solution with $y(0)=1$.""",
     [S(r'(1) A correct $U$ must satisfy $\partial U/\partial t=M$. Here $\partial U/\partial t=4ty+1\neq2ty+1$: the shared term $t^2y$ was counted twice.', r'\dfrac{\partial}{\partial t}(2t^2y+t+2y^2)=4ty+1\neq M'),
      S(r'(2) Check exactness: $\partial M/\partial y=2t=\partial N/\partial t$. Then integrate only $M$: $U=t^2y+t+f(y)$.', r'U=t^2y+t+f(y)'),
      S(r'Match $N$: $t^2+f^{\prime}(y)=t^2+4y$, so $f^{\prime}(y)=4y$ and $f(y)=2y^2$.', r'U=t^2y+t+2y^2'),
      S(r'Apply $y(0)=1$.', r'C=0+0+2=2')],
     r'(1) its $t$-derivative is $4ty+1\neq M$. (2) $t^2y+t+2y^2=2$.', 'intermediate', label='Practice 6')

D.PR('Lecture (e) as an initial-value problem',
     r"""Consider $y\,dt+(3+3t-y)\,dy=0$ with $y(0)=1$.
1. Show that it is not exact.
2. Find an integrating factor.
3. Solve the initial-value problem.
4. Write $t$ as a function of $y$.""",
     [S(r'(1) $\partial M/\partial y=1$ and $\partial N/\partial t=3$: not exact.', r'1\neq3'),
      S(r'(2) Test 2: $(3-1)/y=2/y$, a function of $y$ only, so $\mu=e^{2\ln y}=y^2$.', r'\mu=y^2'),
      S(r'(3) The multiplied equation $y^3\,dt+(3y^2+3ty^2-y^3)\,dy=0$ is exact; integrating $M=y^3$ in $t$ gives $ty^3+f(y)$, and matching $N$ gives $f^{\prime}(y)=3y^2-y^3$, so $f=y^3-\tfrac{y^4}{4}$.', r'U=ty^3+y^3-\dfrac{y^4}{4}'),
      S(r'Multiply by 4 and apply $y(0)=1$.', r'4(t+1)y^3-y^4=C,\qquad C=4\cdot1\cdot1-1=3'),
      S(r'(4) The equation is linear in $t$: add $y^4$, divide by $4y^3$, subtract 1.', r't=\dfrac{3+y^4}{4y^3}-1')],
     r'(2) $\mu=y^2$ (3) $4(t+1)y^3-y^4=3$ (4) $t=\dfrac{3+y^4}{4y^3}-1$.', 'advanced', label='Practice 7', cites=W(4, 5))

# ====================================================================== Summary
D.H('Summary')
D.T(['Problem type', 'How to recognise it', 'What to do'], [
    ['Exact', r'In $M\,dt+N\,dy=0$: $\partial M/\partial y=\partial N/\partial t$', r'$U=\int M\,dt+f(y)$, match $N$ to find $f$, answer $U=C$'],
    ['Integrating factor in $t$', r'Not exact, and $\frac{1}{N}(\partial M/\partial y-\partial N/\partial t)$ has only $t$', r'$\mu=e^{\int f(t)\,dt}$, multiply both parts, solve as exact'],
    ['Integrating factor in $y$', r'Not exact, and $\frac{1}{M}(\partial N/\partial t-\partial M/\partial y)$ has only $y$', r'$\mu=e^{\int g(y)\,dy}$, multiply both parts, solve as exact'],
    ['Linear (Week 3)', r'$\frac{dy}{dt}+a(t)y=b(t)$', r'$\mu=e^{\int a(t)\,dt}$: the same as Test 1'],
    ['Separable (Week 3)', r'$\frac{dy}{dt}=g(t)\,h(y)$', r'Separate and integrate (the separated form is exact)'],
    ['Neither test works', r'Both ratios still contain the wrong variable', r'Not solvable with this week’s tools; try another method'],
])
D.T(['Formula', 'What it means'], [
    [r'$dU=\frac{\partial U}{\partial t}dt+\frac{\partial U}{\partial y}dy$', r'Small change of $U$ for a small step in $t$ and $y$'],
    [r'$\frac{\partial M}{\partial y}=\frac{\partial N}{\partial t}$', 'Exactness test'],
    [r'$U(t,y)=C$', 'Solution of an exact equation; $C$ from the initial condition'],
    [r'$\mu=e^{\int f(t)\,dt}$, $f=\frac{1}{N}\big(\frac{\partial M}{\partial y}-\frac{\partial N}{\partial t}\big)$', 'Integrating factor, Test 1'],
    [r'$\mu=e^{\int g(y)\,dy}$, $g=\frac{1}{M}\big(\frac{\partial N}{\partial t}-\frac{\partial M}{\partial y}\big)$', 'Integrating factor, Test 2'],
    [r'$\frac{\partial U}{\partial t}+\frac{\partial U}{\partial y}\frac{dy}{dt}=0$', 'Implicit differentiation check of $U=C$'],
], cites=W(1, 5))

D.save()
