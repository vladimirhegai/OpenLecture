"""ELEC 231 Week 4 v2: exact equations and integrating factors (short, example-led, interactive)."""
import sympy as sp

from lib231 import Doc, S, steps_fence

D = Doc(week=4, title='Week 4: Exact Equations and Integrating Factors',
        topic_keys=['exact_equations', 'integrating_factors'])
W = lambda *p: D.cite('W4', *p)  # noqa: E731
T4 = D.cite('T4', 1)

# ---------------------------------------------------------------- checks
t, y = sp.symbols('t y', positive=True)
k, C = sp.symbols('k C')
dd = sp.diff


def zero(e):
    return sp.simplify(e) == 0


def exact(M, N):
    return zero(dd(M, y) - dd(N, t))


def potential(M, N, U):
    """dU/dt = M and dU/dy = N."""
    assert zero(dd(U, t) - M) and zero(dd(U, y) - N), (M, N, U)


def solves(M, N, U):
    """Along U = C, dy/dt = -U_t/U_y must satisfy M + N y' = 0."""
    assert zero(M * dd(U, y) - N * dd(U, t)), (M, N, U)


def explicit(M, N, Y):
    assert zero(M.subs(y, Y) + N.subs(y, Y) * dd(Y, t)), Y


def ratio1(M, N):  # Test 1: (M_y - N_t)/N
    return sp.simplify((dd(M, y) - dd(N, t)) / N)


def ratio2(M, N):  # Test 2: (N_t - M_y)/M
    return sp.simplify((dd(N, t) - dd(M, y)) / M)


# Lecture Example 4.1 (stepper), both integration orders
M, N = 2 * t * y + 3 * t**2, t**2
assert dd(M, y) == 2 * t == dd(N, t)
assert sp.integrate(M, t) == t**2 * y + t**3
potential(M, N, t**2 * y + t**3)
assert sp.integrate(N, y) == t**2 * y and zero(dd(t**2 * y, t) - 2 * t * y)
# Ex 1: lecture (a)
M, N = 3 * t, 4 * y
assert exact(M, N)
potential(M, N, sp.Rational(3, 2) * t**2 + 2 * y**2)
solves(M, N, 3 * t**2 + 4 * y**2)
assert (3 * t**2 + 4 * y**2).subs({t: 2, y: 2}) == 28
# Ex 2: lecture (b) with y(1) = 0
M, N = t - y, -(t + y)
assert dd(M, y) == -1 == dd(N, t)
U = t**2 / 2 - t * y - y**2 / 2
potential(M, N, U)
U2 = t**2 - 2 * t * y - y**2
solves(M, N, U2)
assert U2.subs({t: 1, y: 0}) == 1
assert zero(-dd(U2, t) / dd(U2, y) - (t - y) / (t + y))
# Ex 3: lecture (d), not exact; neither test gives mu
M, N = t, -(t + y)
assert dd(M, y) == 0 and dd(N, t) == -1
assert zero(ratio1(M, N) + 1 / (t + y)) and ratio1(M, N).has(y)
assert zero(ratio2(M, N) + 1 / t) and ratio2(M, N).has(t)
# Try it 1: lecture (c), sign trap
M, N = t**2 - y**2, -2 * t * y
assert exact(M, N) and not exact(M, -N)
assert dd(M, y) == -2 * y and dd(-N, t) == 2 * y
potential(M, N, t**3 / 3 - t * y**2)
U = t**3 - 3 * t * y**2
solves(M, N, U)
assert zero(2 * t * y * (-dd(U, t) / dd(U, y)) - (t**2 - y**2))
# Try it 2: choose k
Mk, Nk = 2 * t * sp.sin(y) + y, t**2 * sp.cos(y) + k * t
assert sp.solve(sp.Eq(dd(Mk, y), dd(Nk, t)), k) == [1]
M, N = Mk, Nk.subs(k, 1)
U = t**2 * sp.sin(y) + t * y
potential(M, N, U)
assert zero(U.subs({t: 1, y: sp.pi / 2}) - (1 + sp.pi / 2))
# Ex 4: lecture (e): mu = y^2
M, N = y, 3 + 3 * t - y
assert dd(M, y) == 1 and dd(N, t) == 3
assert zero(ratio1(M, N) + 2 / (3 + 3 * t - y)) and ratio1(M, N).has(y)
assert zero(ratio2(M, N) - 2 / y)
mu = sp.simplify(sp.exp(sp.integrate(2 / y, y)))
assert zero(mu - y**2)
assert zero(sp.expand(mu * N) - (3 * y**2 + 3 * t * y**2 - y**3))
assert dd(mu * M, y) == 3 * y**2 and zero(dd(mu * N, t) - 3 * y**2)
# Ex 5: pre-tutorial 4
M2, N2 = y**3, sp.expand(y**2 * (3 + 3 * t - y))
assert sp.integrate(M2, t) == t * y**3
assert zero(N2 - dd(t * y**3, y) - (3 * y**2 - y**3))
assert sp.integrate(3 * y**2 - y**3, y) == y**3 - y**4 / 4
potential(M2, N2, t * y**3 + y**3 - y**4 / 4)
U4 = 4 * (t + 1) * y**3 - y**4
assert zero(4 * (t * y**3 + y**3 - y**4 / 4) - U4)
solves(M, N, U4)
explicit(M, N, sp.Integer(0))  # y = 0 solves the original ...
assert U4.subs(y, 0) == 0  # ... and is the C = 0 curve
explicit(M, N, 4 * (t + 1))  # the other half of the C = 0 level set
# Ex 6: Test 1 gives mu = t, y(1) = 1
M, N = t**2 + y**2 + t, t * y
assert dd(M, y) == 2 * y and dd(N, t) == y
assert zero(ratio1(M, N) - 1 / t)
mu = sp.simplify(sp.exp(sp.integrate(1 / t, t)))
assert zero(mu - t)
assert exact(mu * M, mu * N) and zero(dd(mu * M, y) - 2 * t * y)
U = t**4 / 4 + t**2 * y**2 / 2 + t**3 / 3
potential(mu * M, mu * N, U)
assert zero(12 * U - (3 * t**4 + 6 * t**2 * y**2 + 4 * t**3))
assert (12 * U).subs({t: 1, y: 1}) == 13
Y = sp.sqrt((13 - 3 * t**4 - 4 * t**3) / (6 * t**2))
explicit(M, N, Y)
assert Y.subs(t, 1) == 1
# Try it 3: y dt - t dy = 0, two factors, a lost solution
M, N = y, -t
assert dd(M, y) == 1 and dd(N, t) == -1
assert zero(ratio1(M, N) + 2 / t) and zero(ratio2(M, N) + 2 / y)
assert zero(sp.exp(sp.integrate(-2 / t, t)) - t**-2) and zero(sp.exp(sp.integrate(-2 / y, y)) - y**-2)
potential(M / y**2, N / y**2, t / y)
potential(M / t**2, N / t**2, -y / t)
explicit(M, N, k * t)
explicit(M, N, sp.Integer(0))
# Try it 4: linear equations, Test 1 ratio = a(t); dy/dt + 2y = 4, y(0) = 0
a, b = sp.Function('a')(t), sp.Function('b')(t)
assert zero(ratio1(a * y - b, sp.Integer(1)) - a)
M, N = 2 * y - 4, sp.Integer(1)
assert ratio1(M, N) == 2
mu = sp.exp(2 * t)
assert exact(mu * M, mu * N)
assert sp.integrate(mu * N, y) == y * sp.exp(2 * t)
assert zero(sp.integrate(-4 * sp.exp(2 * t), t) + 2 * sp.exp(2 * t))
U = (y - 2) * sp.exp(2 * t)
potential(mu * M, mu * N, U)
assert U.subs({t: 0, y: 0}) == -2
Y = 2 - 2 * sp.exp(-2 * t)
assert zero(dd(Y, t) + 2 * Y - 4) and Y.subs(t, 0) == 0

# ================================================================ Topic 1
D.H('Topic 1: Exact equations', cites=W(1, 4))
D.P(r"Every first-order ODE can be written as $M\,dt+N\,dy=0$."
    "\n"
    r"- $M$, $N$: expressions in $t$ and $y$"
    "\n"
    r"- $U(t,y)$: one function whose two slopes are $M$ and $N$ (if it exists)"
    "\n"
    r"- $\dfrac{\partial U}{\partial t}$: a **partial derivative** (differentiate in $t$ while treating $y$ as a fixed number)"
    "\n\n"
    r"The equation is **exact** when $M=\dfrac{\partial U}{\partial t}$ and $N=\dfrac{\partial U}{\partial y}$."
    "\n\n"
    r"Then the left side is the change of $U$ for a small step ($dU$). So the equation says $U$ doesn't change:",
    cites=W(1, 2))
D.EQ(r'M\,dt+N\,dy=\dfrac{\partial U}{\partial t}dt+\dfrac{\partial U}{\partial y}dy=dU=0', cites=W(1))
D.P(r"So $U$ never changes along a solution: **every solution is a curve $U(t,y)=C$**."
    "\n\n"
    r"You can check an equation is exact without knowing $U$ (Theorem 4.1)."
    "\n\n"
    r"It works because both sides equal “differentiate $U$ once in $t$ and once in $y$”, and the order doesn't matter:",
    cites=W(1))
D.EQ(r'M\,dt+N\,dy=0\ \text{is exact}\iff\dfrac{\partial M}{\partial y}=\dfrac{\partial N}{\partial t}', cites=W(1))
D.STEPS('Finding $U$ (lecture Example 4.1)', [
    (r'(2ty+3t^2)\,dt+t^2\,dy=0', r'Here $M=2ty+3t^2$ and $N=t^2$.'),
    (r'\dfrac{\partial M}{\partial y}=\hl{2t},\qquad \dfrac{\partial N}{\partial t}=\hl{2t}',
     r'Test: hold $t$ fixed to get $\partial(2ty)/\partial y=2t$; hold $y$ fixed to get $\partial(t^2)/\partial t=2t$. Equal, so exact.'),
    (r'\dfrac{\partial U}{\partial t}=2ty+3t^2', r'So some $U$ has $M$ as its $t$-slope. Undo that slope by integrating in $t$.'),
    (r'U=\hl{t^2y+t^3+f(y)}', r'With $y$ fixed, $\int 2ty\,dt=t^2y$ and $\int 3t^2dt=t^3$. The "constant" can be any $f(y)$, since $\partial f(y)/\partial t=0$.'),
    (r'\dfrac{\partial U}{\partial y}=\hl{t^2+f^{\prime}(y)}=t^2', r'Differentiate in $y$ and set it equal to $N=t^2$.'),
    (r'f^{\prime}(y)=\hl{0}\ \Rightarrow\ f(y)=\text{const}', r'The $t^2$ cancels. What is left must contain only $y$ (if a $t$ survives, you made a mistake).'),
    (r'\hl{t^2y+t^3=C}', r'The solution is $U=C$ (the constant from $f$ is absorbed into $C$).'),
])
D.P(r"The lecture also does it in the other order:"
    "\n"
    r"- **Integrate $N$ in $y$:** $U=\int t^2\,dy=t^2y+g(t)$"
    "\n"
    r"- **Match $M$:** $g^{\prime}(t)=3t^2$, so $g=t^3$"
    "\n\n"
    r"Same $U$. Start with whichever integral is easier.", cites=W(2))

D.EX('Lecture (a): the answer is a family of curves', r'Solve $3t\,dt+4y\,dy=0$.', [
    S(r'$M=3t$ has no $y$ and $N=4y$ has no $t$, so both test derivatives are $0$: exact.',
      r'\dfrac{\partial M}{\partial y}=0=\dfrac{\partial N}{\partial t}'),
    S(r'Integrate $M$ in $t$ ($\int t\,dt=\tfrac{t^2}{2}$) and add $f(y)$.', r'U=\tfrac32t^2+f(y)'),
    S(r'Match $N$. This time $f$ is not constant: $\int 4y\,dy=2y^2$.', r'f^{\prime}(y)=4y\ \Rightarrow\ f(y)=2y^2'),
    S(r'Set $U=C$ and double it to clear the fraction ($2C$ is just another constant, so call it $C$ again).', r'3t^2+4y^2=C'),
], r'$3t^2+4y^2=C$: one ellipse for each $C>0$', cites=W(3))
D.GRAPH3D(r'''
title "Solutions are level curves of $U$ (lecture (a))"
x -2 2 label="$t$"
y -2 2 label="$y$"
z 0 28 label="$U$"
view az=-55 el=30
slider C 1 24 8 step=1 label="$C$"
surface "3*x^2+4*y^2" label="$U=3t^2+4y^2$" mesh=30
plane "C" label="where $U=C$: one solution curve"
caption "Slide the plane: each height $C$ cuts the bowl in one ellipse, and its shadow on the floor is the solution $3t^2+4y^2=C$. An initial condition picks the height."
''')

D.EX('Lecture (b): start from $dy/dt$, then use a starting point',
     r'Solve $\dfrac{dy}{dt}=\dfrac{t-y}{t+y}$ with $y(1)=0$.', [
    S(r'Multiply both sides by $(t+y)\,dt$, then move everything to the left. The minus sign belongs to $N$.',
      r'(t-y)\,dt-(t+y)\,dy=0'),
    S(r'Test with $M=t-y$ and $N=-t-y$.', r'\dfrac{\partial M}{\partial y}=-1=\dfrac{\partial N}{\partial t}'),
    S(r'Integrate $M$ in $t$; with $y$ fixed, $\int y\,dt=ty$.', r'U=\dfrac{t^2}{2}-ty+f(y)'),
    S(r'Match $N$: $-t+f^{\prime}(y)=-t-y$, so $f^{\prime}(y)=-y$.', r'f(y)=-\tfrac{y^2}{2}'),
    S(r'Set $U=C$ and double.', r't^2-2ty-y^2=C'),
    S(r'The starting point picks the curve: put $t=1$, $y=0$ into the left side.', r'C=1-0-0=1'),
    S(r'Check by differentiating in $t$, with $y=y(t)$.'
      '\n\n'
      r'**Product rule:** $\frac{d}{dt}(2ty)=2y+2ty^{\prime}$.'
      '\n\n'
      r'**Chain rule:** $\frac{d}{dt}y^2=2yy^{\prime}$.',
      r'2t-2y-2ty^{\prime}-2yy^{\prime}=0\ \Rightarrow\ y^{\prime}=\dfrac{t-y}{t+y}\ \checkmark'),
], r'$t^2-2ty-y^2=1$', cites=W(3))

D.EX('Lecture (d): when the test fails', r'Is $\dfrac{dy}{dt}=\dfrac{t}{t+y}$ exact?', [
    S('Cross-multiply and move everything to the left.', r't\,dt-(t+y)\,dy=0'),
    S(r'Test with $M=t$ and $N=-(t+y)$.', r'\dfrac{\partial M}{\partial y}=0\ \neq\ -1=\dfrac{\partial N}{\partial t}'),
    S(r'No $U$ exists, so the recipe can’t start.'
      '\n\n'
      r'Topic 2 repairs some equations like this one, but not this one: both of its tests fail here.', ''),
], r'Not exact', cites=W(4))

D.PR('Lecture (c): find the mistake',
     r'A classmate rewrites $2ty\,\dfrac{dy}{dt}=t^2-y^2$ as $(t^2-y^2)\,dt+2ty\,dy=0$.'
     '\n\n'
     r'They find $\dfrac{\partial M}{\partial y}=-2y\neq2y=\dfrac{\partial N}{\partial t}$ and give up.'
     '\n\n'
     r'What went wrong? Solve it.', [
    S(r'Moving $2ty\,dy$ to the left flips its sign, so $N=-2ty$, not $+2ty$.', r'(t^2-y^2)\,dt-2ty\,dy=0'),
    S(r'Now the test passes.', r'\dfrac{\partial M}{\partial y}=-2y=\dfrac{\partial N}{\partial t}'),
    S(r'Integrate $M$ in $t$ ($y^2$ is a constant here, so $\int y^2dt=ty^2$).', r'U=\dfrac{t^3}{3}-ty^2+f(y)'),
    S(r'Match $N$: $-2ty+f^{\prime}(y)=-2ty$, so $f$ is constant. Set $U=C$ and multiply by 3.', r't^3-3ty^2=C'),
], r'A lost minus sign. The solution is $t^3-3ty^2=C$.', cites=W(4))

D.PR('Choose the constant',
     r'Find the number $k$ that makes $(2t\sin y+y)\,dt+(t^2\cos y+kt)\,dy=0$ exact.'
     '\n\n'
     r'Then solve it with $y(1)=\dfrac{\pi}{2}$.', [
    S(r'Both test derivatives, using $\frac{d}{dy}\sin y=\cos y$.', r'\dfrac{\partial M}{\partial y}=2t\cos y+1,\qquad \dfrac{\partial N}{\partial t}=2t\cos y+k'),
    S(r'They agree for every $t$ and $y$ only if $k=1$.', r'k=1'),
    S(r'Integrate $M$ in $t$ ($\sin y$ is a constant factor).', r'U=t^2\sin y+ty+f(y)'),
    S(r'Match $N=t^2\cos y+t$: $\partial U/\partial y=t^2\cos y+t+f^{\prime}(y)$, so $f^{\prime}=0$.', r'U=t^2\sin y+ty'),
    S(r'Put in $t=1$, $y=\frac{\pi}{2}$, with $\sin\frac{\pi}{2}=1$.', r'C=1+\dfrac{\pi}{2}'),
], r'$k=1$; $\ t^2\sin y+ty=1+\dfrac{\pi}{2}$', diff='intermediate')

# ================================================================ Topic 2
D.H('Topic 2: Integrating factors', cites=W(4, 5))
D.P(r"If an equation isn't exact, multiply it by a function $\mu(t,y)$ (“mu”, an **integrating factor**)."
    "\n\n"
    r"The new equation $\mu M\,dt+\mu N\,dy=0$ has:"
    "\n"
    r"- **the same solution curves** (wherever $\mu\neq0$)"
    "\n"
    r"- **new coefficients**, which may pass the test"
    "\n\n"
    r"The lecture's two tests (Spiegel's Theorems 1 and 2) find a $\mu$ that depends on one variable only:",
    cites=W(4, 5))
D.T(['', 'Compute', 'Works if only this is left', 'Integrating factor'], [
    ['Test 1', r'$\dfrac{1}{N}\Big(\dfrac{\partial M}{\partial y}-\dfrac{\partial N}{\partial t}\Big)$', r'$t$: call it $f(t)$', r'$\mu=e^{\int f(t)\,dt}$'],
    ['Test 2', r'$\dfrac{1}{M}\Big(\dfrac{\partial N}{\partial t}-\dfrac{\partial M}{\partial y}\Big)$', r'$y$: call it $g(y)$', r'$\mu=e^{\int g(y)\,dy}$'],
], cites=W(5))
D.P(r"Note:"
    "\n"
    r"- The two tests divide by different things and subtract in opposite orders."
    "\n"
    r"- A constant counts as “only $t$” and “only $y$”."
    "\n\n"
    r"Then multiply **both** $M$ and $N$ by $\mu$, re-test, and solve as in Topic 1.")

D.EX('Lecture (e): Test 1 fails, Test 2 works', r'Make $y\,dt+(3+3t-y)\,dy=0$ exact.', [
    S(r'$M=y$, $N=3+3t-y$. Not exact.', r'\dfrac{\partial M}{\partial y}=1\ \neq\ 3=\dfrac{\partial N}{\partial t}'),
    S(r'Test 1: the result still contains $y$, so it fails.', r'\dfrac{1}{N}(1-3)=\dfrac{-2}{3+3t-y}'),
    S(r'Test 2: only $y$ is left.', r'\dfrac{1}{M}(3-1)=\dfrac{2}{y}=g(y)'),
    S(r'$\int\frac{1}{y}dy=\ln|y|$, and $2\ln|y|=\ln y^2$, so $e^{2\ln|y|}=y^2$ (not $2y$).',
      r'\mu=e^{\int\frac{2}{y}dy}=e^{2\ln|y|}=y^2'),
    S(r'Multiply **both** parts by $y^2$ (Eq. (4.13)) and re-test: both derivatives are now $3y^2$.',
      r'y^3\,dt+(3y^2+3ty^2-y^3)\,dy=0'),
], r'$\mu=y^2$; the new equation is exact', cites=W(4, 5))

D.EX('Pre-tutorial 4: finish lecture (e)', r'Solve $y^3\,dt+y^2(3+3t-y)\,dy=0$, Eq. (4.13).', [
    S(r'Integrate $M=y^3$ in $t$: with $y$ fixed it is a constant.', r'U=ty^3+f(y)'),
    S(r'Match $N=3y^2+3ty^2-y^3$: the $3ty^2$ cancels.', r'3ty^2+f^{\prime}(y)=3y^2+3ty^2-y^3\ \Rightarrow\ f^{\prime}(y)=3y^2-y^3'),
    S(r'Power rule: $\int y^n dy=\frac{y^{n+1}}{n+1}$.', r'f(y)=y^3-\dfrac{y^4}{4}'),
    S(r'Set $U=C$ and multiply by 4.', r'4(t+1)y^3-y^4=C'),
    S(r'Lost solutions? Multiplying by $\mu=y^2$ can hide the line where $\mu=0$.'
      '\n\n'
      r'$y=0$ does solve the original ($M=0$ and $dy=0$). It is the $C=0$ curve, so nothing is lost.', ''),
], r'$4(t+1)y^3-y^4=C$', cites=T4 + W(5))
D.GRAPH(intro=r"The grey slopes below come from the original $y\,dt+(3+3t-y)\,dy=0$, before multiplying."
    "\n"
    r"- **Drag the point:** the curve $4(t+1)y^3-y^4=C$ through it always follows them."
    "\n"
    r"- **Drag it onto $y=0$:** $C=0$ and the curve is the line $y=0$ (plus the line $y=4t+4$, which also solves the equation).",
    source=r'''
title "Multiplying by $\mu=y^2$ didn't change the solutions"
x -1 3 label="$t$"
y -1 4 label="$y$"
field "-y/(3+3*x-y)"
drag P 0.5 1 label="$(t_0,y_0)$" snap=0.25
level "4*(x+1)*y^3-y^4" value="4*(P_x+1)*P_y^3-P_y^4" label="$4(t+1)y^3-y^4=C$ through your point" color=2
readout "$C=$" "4*(P_x+1)*P_y^3-P_y^4"
''')

D.EX('Test 1 gives μ = t', r'Solve $(t^2+y^2+t)\,dt+ty\,dy=0$ with $y(1)=1$ (take $t>0$).', [
    S(r'Test first: not exact.', r'\dfrac{\partial M}{\partial y}=2y\ \neq\ y=\dfrac{\partial N}{\partial t}'),
    S(r'Test 1: the $y$ cancels, leaving only $t$.', r'\dfrac{1}{N}(2y-y)=\dfrac{y}{ty}=\dfrac1t=f(t)'),
    S(r'$\int\frac1t dt=\ln t$ and $e^{\ln t}=t$.', r'\mu=e^{\ln t}=t'),
    S(r'Multiply both parts by $t$; both test derivatives are now $2ty$.', r'(t^3+ty^2+t^2)\,dt+t^2y\,dy=0'),
    S(r'Integrate the new $M$ in $t$. Matching $N=t^2y$ gives $f^{\prime}(y)=0$.', r'U=\dfrac{t^4}{4}+\dfrac{t^2y^2}{2}+\dfrac{t^3}{3}'),
    S(r'Multiply $U=C$ by 12, then put in $t=1$, $y=1$.', r'3t^4+6t^2y^2+4t^3=C,\qquad C=13'),
    S(r'Here you can solve for $y$: isolate $y^2$, and take the $+$ root because $y(1)=1>0$.', r'y=\sqrt{\dfrac{13-3t^4-4t^3}{6t^2}}'),
], r'$y=\sqrt{\dfrac{13-3t^4-4t^3}{6t^2}}$')

D.PR('Both tests work, and one loses a solution',
     r'For $y\,dt-t\,dy=0$, show that both tests give an integrating factor.'
     '\n\n'
     r'Solve it with the Test 2 factor. Which solution did that factor lose?', [
    S(r'$M=y$, $N=-t$, so $\frac{\partial M}{\partial y}=1$, $\frac{\partial N}{\partial t}=-1$. Test 1 leaves only $t$.',
      r'\dfrac{1-(-1)}{-t}=-\dfrac{2}{t}\ \Rightarrow\ \mu=e^{-2\ln t}=\dfrac{1}{t^2}'),
    S(r'Test 2 leaves only $y$.', r'\dfrac{-1-1}{y}=-\dfrac{2}{y}\ \Rightarrow\ \mu=e^{-2\ln y}=\dfrac{1}{y^2}'),
    S(r'Multiply by $\frac{1}{y^2}$, integrate $M=\frac1y$ in $t$, and match $N=-\frac{t}{y^2}$ (it already matches, $f$ is constant).',
      r'\dfrac{1}{y}\,dt-\dfrac{t}{y^2}\,dy=0\ \Rightarrow\ \dfrac{t}{y}=C'),
    S(r'$\frac{t}{y}=C$ gives the lines $y=\frac{t}{C}$, but never $y=0$.'
      '\n\n'
      r'Yet $y=0$ solves $y\,dt-t\,dy=0$ ($M=0$ and $dy=0$). It sits where $\mu=\frac{1}{y^2}$ is undefined, so add it back.',
      r'y=kt\quad\text{for any }k\text{, including }k=0'),
], r'- **Test 1:** $\mu=\dfrac{1}{t^2}$'
   '\n'
   r'- **Test 2:** $\mu=\dfrac{1}{y^2}$'
   '\n'
   r'- **Solutions:** $y=kt$; $\mu=\dfrac{1}{y^2}$ loses $y=0$.', diff='intermediate')

D.PR('Linear equations are a special case',
     r'Show that Test 1 always works for a linear equation $\dfrac{dy}{dt}+a(t)\,y=b(t)$, and that it gives the Week 3 '
     r'integrating factor.'
     '\n\n'
     r'Then use it to solve $\dfrac{dy}{dt}+2y=4$ with $y(0)=0$.', [
    S(r'Multiply by $dt$ and move everything left.', r'\big(a(t)\,y-b(t)\big)\,dt+1\,dy=0'),
    S(r'$\frac{\partial M}{\partial y}=a(t)$, $\frac{\partial N}{\partial t}=0$, $N=1$: Test 1 leaves only $t$.',
      r'\dfrac{1}{1}\big(a(t)-0\big)=a(t)\ \Rightarrow\ \mu=e^{\int a(t)\,dt}'),
    S(r'For $\frac{dy}{dt}+2y=4$: $a=2$, so $\mu=e^{2t}$.', r'(2y-4)e^{2t}\,dt+e^{2t}\,dy=0'),
    S(r'Integrating $N$ in $y$ is easier here ($e^{2t}$ is a constant factor). Add $g(t)$.', r'U=ye^{2t}+g(t)'),
    S(r'Match $M$: $g^{\prime}(t)=-4e^{2t}$. Using $\int e^{2t}dt=\frac12e^{2t}$:', r'g(t)=-2e^{2t}\ \Rightarrow\ U=(y-2)e^{2t}'),
    S(r'Put in $t=0$, $y=0$, then solve for $y$.', r'(y-2)e^{2t}=-2\ \Rightarrow\ y=2-2e^{-2t}'),
], r'$\mu=e^{\int a(t)\,dt}$ (the Week 3 factor); $\ y=2-2e^{-2t}$', diff='intermediate')

D.save()
