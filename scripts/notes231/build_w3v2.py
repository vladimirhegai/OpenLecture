"""ELEC 231 Week 3 v2: linear ODEs (integrating factor), separable ODEs, existence and uniqueness.

Short, example-led, interactive (style guide: STYLE.md). Every answer is checked with sympy below.
Run:  .venv/Scripts/python.exe scripts/notes231/build_w3v2.py [--publish]
"""
import json
import urllib.request

import sympy as sp

from lib231 import Doc, S, steps_fence

D = Doc(week=3, title='Week 3: Linear and Separable First-Order ODEs; Existence and Uniqueness',
        topic_keys=['linear_first_order', 'separable_odes', 'existence_uniqueness'])
W = lambda *p: D.cite('W3', *p)  # noqa: E731
T3 = D.cite('T3', 1)

SCH_RL = r'''V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$10\,\Omega$"
L1 6,3 -> 6,0 "$2\,\mathrm{H}$" i="$i$"
wire 6,0 -> 0,0
ground 0,0'''

# ---------------------------------------------------------------- checks
t = sp.Symbol('t', real=True)
tp = sp.Symbol('t', positive=True)
y = sp.Symbol('y', real=True)
yp = sp.Symbol('y', positive=True)
A, C, c = sp.symbols('A C c', real=True)
E = sp.exp


def zero(e, msg):
    assert sp.simplify(e) == 0, f'{msg}: {sp.simplify(e)}'


def solves(Y, F, var, msg):
    """Y(var) solves dy/dvar = F(var, y)."""
    zero(sp.diff(Y, var) - F.subs(y, Y), msg)


def implicit(G, F, tv, yv, msg):
    """G(t, y) = const is an implicit solution of dy/dt = F(t, y)."""
    zero(-sp.diff(G, tv) / sp.diff(G, yv) - F, msg)


# Topic 1: the integrating factor turns the left side into d/dt[mu y]
a_, f_ = sp.Function('a')(t), sp.Function('f')(t)
Y_ = sp.Function('y')(t)
mu = E(sp.Integral(a_, t))
zero(sp.diff(mu * Y_, t) - mu * (sp.diff(Y_, t) + a_ * Y_), 'mu derivation')
# Ex1 RL (lecture): 2 i' + 10 i = 100, i(0) = 0
i1 = 10 - 10 * E(-5 * t)
zero(2 * sp.diff(i1, t) + 10 * i1 - 100, 'RL KVL')
assert i1.subs(t, 0) == 0
zero(sp.integrate(50 * E(5 * t), t) - 10 * E(5 * t), 'int 50e^5t')
# Ex2 lecture Example 3.1
a2 = 10 / (2 * tp + 5)
zero(sp.integrate(a2, tp) - 5 * sp.log(2 * tp + 5), 'int a(t)')
zero(E(5 * sp.log(2 * tp + 5)) - (2 * tp + 5) ** 5, 'mu = (2t+5)^5')
zero(sp.integrate(10 * (2 * t + 5) ** 5, t) - (sp.Rational(5, 6) * (2 * t + 5) ** 6 - sp.Rational(5, 6) * 5 ** 6), 'int 10u^5')
y2 = sp.Rational(5, 6) * (2 * t + 5) - sp.Integer(5) ** 7 / (6 * (2 * t + 5) ** 5)
zero(sp.diff(y2, t) + a2.subs(tp, t) * y2 - 10, 'Ex 3.1')
assert y2.subs(t, 0) == 0
assert abs(-5 ** 7 / 6 + 13020.83) < 0.01
# Ex3 ramp: y' + 2y = 4t, y(0) = 1
zero(sp.diff(2 * t * E(2 * t) - E(2 * t), t) - 4 * t * E(2 * t), 'by parts')
y3 = 2 * t - 1 + 2 * E(-2 * t)
zero(sp.diff(y3, t) + 2 * y3 - 4 * t, 'ramp')
assert y3.subs(t, 0) == 1
# Try it 1: y' = 3y + 6, y(0) = 0
q = 2 * E(3 * t) - 2
solves(q, 3 * y + 6, t, 'TI1')
assert q.subs(t, 0) == 0
zero(sp.integrate(6 * E(-3 * t), t) + 2 * E(-3 * t), 'int 6e^-3t')
# Try it 2: t y' + 2y = 4t^2, y(1) = 2
q = tp ** 2 + tp ** -2
zero(tp * sp.diff(q, tp) + 2 * q - 4 * tp ** 2, 'TI2')
assert q.subs(tp, 1) == 2
zero(E(sp.integrate(2 / tp, tp)) - tp ** 2, 'mu t^2')
zero(sp.diff(tp ** 2 * q, tp) - 4 * tp ** 3, 'd/dt[t^2 y] = 4t^3')

# Topic 2: separable
# Ex4 RL by separation
zero(sp.diff(-sp.Rational(1, 5) * sp.log(50 - 5 * y), y) - 1 / (50 - 5 * y), 'RL sep integral')
zero((50 - 5 * i1) - 50 * E(-5 * t), 'A = 50')
# Ex5 Spiegel (i)
solves(2 * t ** 2 / (1 - 2 * C * t ** 2), y ** 2 / t ** 3, t, 'Spiegel i')
solves(sp.S(0), y ** 2 / t ** 3, t, 'Spiegel i, y = 0')
zero(1 / (2 * t ** 2) - C - (1 - 2 * C * t ** 2) / (2 * t ** 2), 'common denominator')
# Ex6 Spiegel (ii)
Fii = (3 * t + t * y ** 2) / (y + t ** 2 * y)
zero(Fii - t * (3 + y ** 2) / (y * (1 + t ** 2)), 'factor')
q = sp.sqrt(6 * t ** 2 + 3)
solves(q, Fii, t, 'Spiegel ii')
assert q.subs(t, 1) == 3
zero(sp.diff(sp.log(3 + y ** 2) / 2, y) - y / (3 + y ** 2), 'half log')
# Ex7 Spiegel (iii): y dt + (t^3 y^2 + t^3) dy = 0
implicit(yp ** 2 + 2 * sp.log(yp) - tp ** -2, -yp / (tp ** 3 * (yp ** 2 + 1)), tp, yp, 'Spiegel iii')
zero(-sp.integrate(tp ** -3, tp) - tp ** -2 / 2, '-int t^-3')
# Try it 3: pre-tutorial 3
q = sp.sqrt(5 - t ** 2)
solves(q, -t / y, t, 'T3a')
assert q.subs(t, 1) == 2
implicit((yp ** 2 + 1) * (tp ** 2 + 2) ** 3, -3 * tp * (yp ** 2 + 1) / (yp * (tp ** 2 + 2)), tp, yp, 'T3b')
solves(A * E(4 * t ** 2 + 3 * t), 8 * t * y + 3 * y, t, 'T3c')
zero(sp.diff(E(-(4 * t ** 2 + 3 * t)) * A * E(4 * t ** 2 + 3 * t), t), 'T3c via mu')
# Try it 4: classify (separable: F factors as g(t) h(y); linear: F is first-degree in y)
sep = lambda F: sp.separatevars(F, symbols=[t, y], dict=True) is not None  # noqa: E731
lin = lambda F: sp.diff(F, y, 2) == 0  # noqa: E731
assert (sep(t ** 2 + y), lin(t ** 2 + y)) == (False, True)
assert (sep(E(t + y)), lin(E(t + y))) == (True, False)
assert (sep(2 * y - 6), lin(2 * y - 6)) == (True, True)
assert (sep(t + y ** 2), lin(t + y ** 2)) == (False, False)

# Topic 3: existence and uniqueness
zero(sp.diff((t + y) / (t - y), y) - 2 * t / (t - y) ** 2, 'quotient rule')
zero(sp.diff(yp ** sp.Rational(1, 3), yp) - 1 / (3 * yp ** sp.Rational(2, 3)), 'dF/dy of y^(1/3)')
q = (2 * tp / 3) ** sp.Rational(3, 2)
zero(sp.diff(q, tp) - q ** sp.Rational(1, 3), 'y^(1/3) second solution')
zero(sp.integrate(yp ** sp.Rational(-1, 3), yp) - sp.Rational(3, 2) * yp ** sp.Rational(2, 3), 'int y^-1/3')
for cc in (0.5, 1.0, 2.5):  # the graph's family: 0 until t = c, then (2(t-c)/3)^(3/2); each solves y' = y^(1/3)
    g = sp.Piecewise((0, tp < cc), ((2 * (tp - cc) / 3) ** sp.Rational(3, 2), True))
    for tv in (cc + 0.3, cc + 2):
        assert abs(float(sp.diff(g, tp).subs(tp, tv)) - float(g.subs(tp, tv)) ** (1 / 3)) < 1e-9
q = 1 / (1 - t)
solves(q, y ** 2, t, 'y^2')
assert q.subs(t, 0) == 1 and sp.limit(q, t, 1, '-') == sp.oo
y0_, t0_ = sp.symbols('y_0 t_0', positive=True)
q = y0_ / (1 - y0_ * (t - t0_))  # the graph's readout: blow-up at t0 + 1/y0
solves(q, y ** 2, t, 'y^2 general start')
assert q.subs(t, t0_) == y0_ and sp.solve(1 - y0_ * (t - t0_), t) == [t0_ + 1 / y0_]
# Try it 5: (t-3) y' + (ln t) y = 2t
F5 = (2 * t - sp.log(t) * y) / (t - 3)
zero(sp.diff(F5, y) + sp.log(t) / (t - 3), 'TI5 dF/dy')
# Try it 6: t y' = y
zero(t * sp.diff(c * t, t) - c * t, 'y = ct')
assert sp.diff(y / t, y) == 1 / t


def check_schematic(src):
    req = urllib.request.Request('http://127.0.0.1:8000/api/v1/schematics/check', data=json.dumps({'source': src}).encode(),
                                 method='POST', headers={'Content-Type': 'application/json'})
    out = json.load(urllib.request.urlopen(req))
    assert not out['errors'], out['errors']


check_schematic(SCH_RL)
print('all sympy checks passed; schematic valid')

# ================================================================ Topic 1
D.H('Topic 1: Linear ODEs and the integrating factor', cites=W(1))
D.P(r"A first-order ODE is **linear** if it can be written in standard form."
    "\n\n"
    r"**Standard form** $\dfrac{dy}{dt}+a(t)\,y=f(t)$:"
    "\n"
    r"- $a(t)$: the **coefficient** of $y$"
    "\n"
    r"- $f(t)$: the **forcing** (the input, e.g. a source)"
    "\n\n"
    r"**The trick:** multiply both sides by the **integrating factor** $\mu(t)=e^{\int a(t)\,dt}$ (mu)."
    "\n"
    r"- The left side becomes the derivative of one product, $\mu y$."
    "\n"
    r"- A single derivative can be undone by integrating.", cites=W(1))
D.STEPS('Why the integrating factor works (lecture)', [
    (r'\dfrac{dy}{dt}+a(t)\,y=f(t)', 'Start from standard form.'),
    (r'\hl{\mu}\dfrac{dy}{dt}+\hl{\mu}\,a\,y=\hl{\mu}\,f', r'Multiply every term by $\mu=e^{\int a\,dt}$.'),
    (r'\mu\dfrac{dy}{dt}+\hl{\dfrac{d\mu}{dt}}\,y=\mu f',
     r'Chain rule: $\frac{d}{dt}e^{\int a\,dt}=a\,e^{\int a\,dt}$, so $\mu a$ is just $\frac{d\mu}{dt}$.'),
    (r'\hl{\dfrac{d}{dt}\big[\mu\,y\big]}=\mu f',
     r'Product rule backwards: $\frac{d}{dt}[\mu y]=\mu\frac{dy}{dt}+\frac{d\mu}{dt}y$ is exactly the left side.'),
    (r'\mu\,y=\hl{\int\mu f\,dt+C}', r'Integrate both sides. The $+C$ appears here.'),
    (r'y=\hl{\dfrac{1}{\mu}}\Big[\int\mu f\,dt+C\Big]', r'Divide by $\mu$. Then the initial condition $y(t_0)=y_0$ fixes $C$.'),
])
D.EQ(r'\mu(t)=e^{\int a(t)\,dt},\qquad y(t)=\dfrac{1}{\mu}\Big[\int\mu\,f\,dt+C\Big]', cites=W(1))

D.EX('An RL circuit (lecture)',
     r'The switch closes at $t=0$ and the inductor carries no current before that, so $i(0)=0$. Find $i(t)$.'
     '\n\n```schematic\n' + SCH_RL + '\n```', [
         S(r'KVL: the resistor drop $Ri$ plus the inductor drop $L\,di/dt$ equals the source.', r'2\dfrac{di}{dt}+10\,i=100'),
         S(r'Divide by $L=2$ first. The trap: here $a=5$, not $10$.', r'\dfrac{di}{dt}+5\,i=50'),
         S(r'$a$ is a constant, so $\int5\,dt=5t$. (No $+C$ is needed inside $\mu$.)', r'\mu=e^{5t}'),
         S(r'Multiply by $\mu$; the left side collapses into one derivative.', r'\dfrac{d}{dt}\big[i\,e^{5t}\big]=50\,e^{5t}'),
         S(r'Integrate, using $\int e^{kt}dt=\frac1k e^{kt}$.', r'i\,e^{5t}=10\,e^{5t}+C'),
         S(r'Put in $i(0)=0$ ($e^0=1$).', r'0=10+C\ \Rightarrow\ C=-10'),
         S(r'Divide by $e^{5t}$.', r'i(t)=10-10\,e^{-5t}=10\big(1-e^{-5t}\big)\ \mathrm{A}'),
     ], r'$i(t)=10\big(1-e^{-5t}\big)\ \mathrm{A}$', cites=W(2, 3))
D.GRAPH(r'''
title "The lecture's sketch: change $R$ and watch $i(t)$"
x 0 1.2 label="$t$ (s)"
y 0 21 label="$i$ (A)"
slider R 5 20 10 step=1 label="$R$ ($\Omega$)"
curve "(100/R)*(1-exp(-R*t/2))" label="$i(t)$" color=1
hline "100/R" color=3 label="final value $100/R$"
vline "2/R" label="$t=\tau=L/R$"
readout "final current $=$" "100/R" unit=" A"
readout "$\tau=$" "2/R" unit=" s"
caption "Starts at 0 (an inductor's current can't jump), settles at $100/R$, and is $63\%$ of the way there at $t=\tau$. At $R=10\,\Omega$: 10 A, $\tau=0.2$ s."
''')

D.EX('A coefficient that changes with time (lecture Example 3.1)',
     r'Solve $\dfrac{dy}{dt}+\dfrac{10\,y}{2t+5}=10$ with $y(0)=0$.', [
         S('It is already in standard form.', r'a(t)=\dfrac{10}{2t+5},\qquad f(t)=10'),
         S(r'Integrate $a$ with the substitution $u=2t+5$, $du=2\,dt$, and $\int\frac{du}{u}=\ln u$.',
           r'\int\dfrac{10}{2t+5}\,dt=5\ln(2t+5)'),
         S(r'Move the 5 into the log ($k\ln u=\ln u^k$), then use $e^{\ln A}=A$.', r'\mu=e^{\ln(2t+5)^5}=(2t+5)^5'),
         S(r'Multiply by $\mu$ and collapse the left side.', r'\dfrac{d}{dt}\Big[y\,(2t+5)^5\Big]=10\,(2t+5)^5'),
         S(r'Integrate with the same $u$ ($dt=\frac{du}{2}$) and the power rule $\int u^5du=\frac{u^6}{6}$.',
           r'y\,(2t+5)^5=\dfrac56(2t+5)^6+C'),
         S(r'Put in $y(0)=0$; at $t=0$, $2t+5=5$.', r'0=\dfrac56\,5^6+C\ \Rightarrow\ C=-\dfrac{5^7}{6}\approx-13\,020.83'),
         S(r'Divide by $(2t+5)^5$.', r'y(t)=\dfrac56(2t+5)-\dfrac{5^7}{6\,(2t+5)^5}'),
     ], r'$y(t)=\dfrac56(2t+5)-\dfrac{5^7}{6\,(2t+5)^5}$', cites=W(1, 2))

D.EX('A ramp input: the integral needs parts',
     r'Solve $\dfrac{dy}{dt}+2y=4t$ with $y(0)=1$.', [
         S(r'$a=2$, so $\mu=e^{2t}$. Multiply and collapse.', r'\dfrac{d}{dt}\big[y\,e^{2t}\big]=4t\,e^{2t}'),
         S(r'The right side is a product, so integrate by parts with $u=4t$, $dv=e^{2t}dt$ (so $v=\frac12e^{2t}$): $\int u\,dv=uv-\int v\,du$.',
           r'\int4t\,e^{2t}dt=2t\,e^{2t}-\int2e^{2t}dt'),
         S(r'The leftover integral is $\int2e^{2t}dt=e^{2t}$.', r'y\,e^{2t}=2t\,e^{2t}-e^{2t}+C'),
         S(r'Divide by $e^{2t}$.', r'y=2t-1+C\,e^{-2t}'),
         S(r'Put in $y(0)=1$: $1=-1+C$, so $C=2$.', r'y(t)=2t-1+2e^{-2t}'),
     ], r'$y(t)=2t-1+2e^{-2t}$'
        '\n\n'
        r'The $e^{-2t}$ part dies out, leaving the line $2t-1$ that tracks the ramp.')

D.PR('Not in standard form yet', r'Solve $\dfrac{dy}{dt}=3y+6$ with $y(0)=0$.', [
    S(r'Move $3y$ to the left. The coefficient of $y$ is $a=-3$: keep the sign.', r'\dfrac{dy}{dt}-3y=6'),
    S(r'$\int(-3)\,dt=-3t$.', r'\mu=e^{-3t}'),
    S(r'Multiply, collapse, integrate ($\int6e^{-3t}dt=-2e^{-3t}$).', r'y\,e^{-3t}=-2e^{-3t}+C'),
    S(r'Divide by $e^{-3t}$ and put in $y(0)=0$: $0=-2+C$.', r'y(t)=2e^{3t}-2'),
], r'$y(t)=2e^{3t}-2$'
   '\n\n'
   r'With $a<0$ the solution grows instead of settling.')

D.PR(r'A $t$ in front of the derivative', r'Solve $t\dfrac{dy}{dt}+2y=4t^2$ with $y(1)=2$, for $t>0$.', [
    S(r'Divide every term by $t$, the right side too.', r'\dfrac{dy}{dt}+\dfrac2t\,y=4t'),
    S(r'$\int\frac2t\,dt=2\ln t$, and $e^{2\ln t}=e^{\ln t^2}=t^2$.', r'\mu=t^2'),
    S(r'Multiply by $t^2$, collapse, and integrate ($\int4t^3dt=t^4$).', r'\dfrac{d}{dt}\big[t^2y\big]=4t^3\ \Rightarrow\ t^2y=t^4+C'),
    S(r'Divide by $t^2$; $y(1)=2$ gives $2=1+C$, so $C=1$.', r'y(t)=t^2+\dfrac{1}{t^2}'),
], r'$y(t)=t^2+\dfrac{1}{t^2}$', diff='intermediate')

# ================================================================ Topic 2
D.H('Topic 2: Separable ODEs', cites=W(3, 4))
D.P(r"An ODE is **separable** if it can be written $N(y)\,\dfrac{dy}{dt}=M(t)$ (lecture Definition 3.1):"
    "\n"
    r"- $N(y)$: a function of $y$ only"
    "\n"
    r"- $M(t)$: a function of $t$ only"
    "\n\n"
    r"Equivalently, $\dfrac{dy}{dt}$ factors into a $t$-part times a $y$-part."
    "\n\n"
    r"**How to solve:**"
    "\n"
    r"- **Separate:** every $y$ with $dy$ on one side, every $t$ with $dt$ on the other."
    "\n"
    r"- **Integrate:** each side in its own variable. One $+C$ is enough."
    "\n\n"
    r"Unlike the integrating factor, this also works for nonlinear equations.", cites=W(4))
D.EQ(r'N(y)\,\dfrac{dy}{dt}=M(t)\quad\Rightarrow\quad\int N(y)\,dy=\int M(t)\,dt+C', cites=W(4))

D.EX('The same RL circuit, by separation (lecture)',
     r'Solve $\dfrac{di}{dt}+5i=50$, $i(0)=0$ (Example 1) by separating the variables.', [
         S(steps_fence('', [
             (r'\dfrac{di}{dt}=50-5i', r'Move $5i$ to the right. There is no $t$ at all, so it factors trivially.'),
             (r'\dfrac{\hl{di}}{\hl{50-5i}}=\hl{dt}', r'Separate: every $i$ on the left, every $t$ on the right.'),
             (r'\hl{-\tfrac15\ln|50-5i|}=\hl{t}+C_1', r'Integrate. Left: $u=50-5i$, $du=-5\,di$, and $\int\frac{du}{u}=\ln|u|$.'),
             (r'\ln|50-5i|=\hl{-5t+C_2}', r'Multiply by $-5$. A constant times $-5$ is just a new constant, $C_2$.'),
             (r'|50-5i|=\hl{e^{C_2}}\,e^{-5t}', r'Exponentiate both sides ($e^{a+b}=e^ae^b$).'),
             (r'50-5i=\hl{A}\,e^{-5t}', r'Drop the bars: the constant $A=\pm e^{C_2}$ carries the sign.'),
             (r'50-0=A\ \Rightarrow\ \hl{A=50}', r'Put in $i(0)=0$ ($e^0=1$).'),
             (r'i(t)=\hl{10\big(1-e^{-5t}\big)}\ \mathrm{A}', r'Solve for $i$: $5i=50-50e^{-5t}$, then divide by 5.'),
         ])),
     ], r'$i(t)=10\big(1-e^{-5t}\big)\ \mathrm{A}$, the same as Example 1.'
        '\n\n'
        r'This ODE is both linear and separable.',
     cites=W(3))

D.EX('Dividing can lose a solution (lecture, Spiegel i)',
     r'Find the general solution of $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$.', [
         S(r'Divide by $y^2$ (only allowed if $y\neq0$) and multiply by $dt$.', r'\dfrac{dy}{y^2}=\dfrac{dt}{t^3}'),
         S(r'Power rule on both sides: $\int y^{-2}dy=-y^{-1}$ and $\int t^{-3}dt=-\frac12t^{-2}$.', r'-\dfrac1y=-\dfrac{1}{2t^2}+C'),
         S(r'Multiply by $-1$, write the right side over $2t^2$, and flip both sides.', r'\dfrac1y=\dfrac{1-2Ct^2}{2t^2}\ \Rightarrow\ y=\dfrac{2t^2}{1-2Ct^2}'),
         S(r'Now check the case the division threw away. $y=0$ gives $0=\frac{0}{t^3}$ ✓, and no value of $C$ produces it.',
           r'y\equiv0\ \text{is a solution too}'),
     ], r'$y=\dfrac{2t^2}{1-2Ct^2}$ for any constant $C$, plus $y=0$', cites=W(4))

D.EX('Factor first (lecture, Spiegel ii)',
     r'Solve $\dfrac{dy}{dt}=\dfrac{3t+t\,y^2}{y+t^2y}$ with $y(1)=3$.', [
         S(r"It doesn't look separable until you factor $t$ out of the top and $y$ out of the bottom.",
           r'\dfrac{dy}{dt}=\dfrac{t\,(3+y^2)}{y\,(1+t^2)}'),
         S('Now separate.', r'\dfrac{y}{3+y^2}\,dy=\dfrac{t}{t^2+1}\,dt'),
         S(r'Each top is half the derivative of its bottom, so each side is $\frac12\ln(\text{bottom})$ (substitute $u=$ bottom).',
           r'\tfrac12\ln(3+y^2)=\tfrac12\ln(t^2+1)+c'),
         S(r'Multiply by 2 and exponentiate; $C_1=e^{2c}$.', r'3+y^2=C_1\,(t^2+1)'),
         S(r'Put in $y(1)=3$: $12=2C_1$.', r'C_1=6\ \Rightarrow\ y^2=6t^2+3'),
         S(r'Take the $+$ square root, because $y(1)=+3$.', r'y(t)=\sqrt{6t^2+3}'),
     ], r'$y^2+3=6(t^2+1)$, i.e. $y(t)=\sqrt{6t^2+3}$', cites=W(4))

D.EX('Differential form, implicit answer (lecture, Spiegel iii)',
     r'Solve $y\,dt+(t^3y^2+t^3)\,dy=0$.', [
         S(r'Factor $t^3$ out of the $dy$ term and move the $dt$ term across.', r't^3\,(y^2+1)\,dy=-y\,dt'),
         S(r'Divide by $t^3y$ to separate, and split the fraction: $\frac{y^2+1}{y}=y+\frac1y$.',
           r'\Big(y+\dfrac1y\Big)dy=-t^{-3}\,dt'),
         S(r'Integrate: $\int y\,dy=\frac{y^2}{2}$, $\int\frac{dy}{y}=\ln|y|$, $-\int t^{-3}dt=\frac{t^{-2}}{2}$.',
           r'\dfrac{y^2}{2}+\ln|y|=\dfrac{t^{-2}}{2}+C'),
         S(r"Multiply by 2. $y$ can't be isolated (it is squared and inside a log), so leave the answer **implicit**: it is still a complete solution.",
           r'y^2+2\ln|y|-t^{-2}=C_1'),
     ], r'$y^2+2\ln|y|-t^{-2}=C_1$', cites=W(4))

D.PR('Pre-tutorial 3', r'''Solve:
1. $\dfrac{dy}{dt}=-\dfrac{t}{y}$, $y(1)=2$. On what interval does the solution exist?
2. $3t\,(y^2+1)\,dt+y\,(t^2+2)\,dy=0$.
3. $\dfrac{dy}{dt}=8ty+3y$, by separation **and** by the integrating factor. Which route can lose a solution?''', [
    S(r'(1) Multiply by $y\,dt$, integrate (power rule) and double; $y(1)=2$ makes the constant $4+1=5$.',
      r'y\,dy=-t\,dt\ \Rightarrow\ y^2+t^2=5'),
    S(r"A circle. Take the $+$ root since $y(1)>0$. It ends where $y=0$ (at $t=\pm\sqrt5$): there the slope $-\frac ty$ is infinite.",
      r'y=\sqrt{5-t^2},\quad -\sqrt5<t<\sqrt5'),
    S(r'(2) Move the $dt$ term across and divide by $(y^2+1)(t^2+2)$, which is never 0.', r'\dfrac{y}{y^2+1}\,dy=-\dfrac{3t}{t^2+2}\,dt'),
    S(r'As in Example 6, each top is half the derivative of its bottom, so each side is a log.',
      r'\tfrac12\ln(y^2+1)=-\tfrac32\ln(t^2+2)+c'),
    S(r'Multiply by 2, combine the logs ($\ln a+3\ln b=\ln ab^3$) and exponentiate; $K=e^{2c}$.', r'(y^2+1)(t^2+2)^3=K'),
    S(r'(3) Separation: factor out $y$, divide by it, integrate, exponentiate ($A=\pm e^C$). Dividing by $y$ lost $y=0$: put it back by allowing $A=0$.',
      r'\dfrac{dy}{y}=(8t+3)\,dt\ \Rightarrow\ y=A\,e^{4t^2+3t}'),
    S(r'Integrating factor: standard form has $a=-(8t+3)$ and $f=0$.', r'\dfrac{d}{dt}\Big[e^{-(4t^2+3t)}\,y\Big]=0'),
    S(r'So the bracket is a constant $A$. Nothing was divided by $y$, so $A=0$ is included automatically.', r'y=A\,e^{4t^2+3t}'),
], r'- **(1)** $y=\sqrt{5-t^2}$ on $-\sqrt5<t<\sqrt5$'
   '\n'
   r'- **(2)** $(y^2+1)(t^2+2)^3=K$'
   '\n'
   r'- **(3)** $y=Ae^{4t^2+3t}$'
   '\n\n'
   r'Separation loses $y=0$, the integrating factor does not.',
    diff='intermediate', cites=T3)

D.PR('Which method fits?', r'''Linear, separable, both, or neither? (Don't solve.)
1. $\dfrac{dy}{dt}=t^2+y$
2. $\dfrac{dy}{dt}=e^{t+y}$
3. $\dfrac{dy}{dt}=2y-6$
4. $\dfrac{dy}{dt}=t+y^2$''', [
    S(r'**Linear** test: $y$ appears only to the first power.', ''),
    S(r'**Separable** test: the right side factors into (function of $t$)$\times$(function of $y$).', ''),
    S(r'(1) $y$ to the first power: linear. A sum that does not factor: not separable.', r'\text{linear only}'),
    S(r'(2) $e^{t+y}=e^t\,e^y$ factors: separable. $e^y$ is not first power: not linear.', r'\text{separable only}'),
    S(r'(3) $2y-6=2(y-3)$ has no $t$, so it factors; and $y$ is first power.', r'\text{both}'),
    S(r'(4) $y^2$ is not first power, and $t+y^2$ does not factor.', r'\text{neither}'),
], '- **(1)** linear only\n- **(2)** separable only\n- **(3)** both\n- **(4)** neither')

# ================================================================ Topic 3
D.H('Topic 3: Existence and uniqueness', cites=W(5))
D.P(r"An **initial value problem** (IVP) is an ODE plus a starting point:"
    "\n"
    r"- $\dfrac{dy}{dt}=F(t,y)$: the **ODE**"
    "\n"
    r"- $y(t_0)=y_0$: the **starting point**"
    "\n\n"
    r"Before solving, ask: is there a solution through that point, and only one? The theorem answers with two checks on $F$."
    "\n\n"
    r"$\dfrac{\partial F}{\partial y}$ (the **partial derivative**): differentiate $F$ with respect to $y$, treating $t$ as a constant.",
    cites=W(5))
D.CO('info', r"**Existence and uniqueness theorem.** Suppose that in a region $R$ of the $ty$-plane, both $F(t,y)$ and "
     r"$\dfrac{\partial F}{\partial y}$ are:"
     "\n"
     r"- real, finite and single-valued"
     "\n"
     r"- continuous"
     "\n\n"
     r"Then exactly one solution passes through each point of $R$."
     "\n\n"
     r"The conditions are **sufficient, not necessary**: where they fail, the theorem says nothing. Typical failures:"
     "\n"
     r"- dividing by zero"
     "\n"
     r"- $\ln$ of a number $\le0$"
     "\n"
     r"- negative powers of $y$ at $y=0$", cites=W(5))

D.EX('Find where the theorem applies',
     r'For $\dfrac{dy}{dt}=\dfrac{t+y}{t-y}$, is exactly one solution guaranteed through $(0,1)$? Through $(2,2)$?', [
         S(r'$F$ breaks only where its bottom is zero: on the line $y=t$.', r'F=\dfrac{t+y}{t-y},\qquad t\neq y'),
         S(r'Quotient rule in $y$, with $t$ held fixed: the top $t+y$ has $y$-derivative $1$, the bottom $t-y$ has $-1$.',
           r'\dfrac{\partial F}{\partial y}=\dfrac{(t-y)+(t+y)}{(t-y)^2}=\dfrac{2t}{(t-y)^2}'),
         S(r'It breaks on the same line, so $R$ is the whole plane minus the line $y=t$. $(0,1)$ is off it; $(2,2)$ is on it.',
           r'(0,1):\ \text{one solution}\qquad(2,2):\ \text{no promise}'),
     ], r'- **Through $(0,1)$:** yes, exactly one solution.'
        '\n'
        r'- **Through $(2,2)$:** no guarantee. It sits on the line $y=t$, where $F$ is undefined.')

D.EX('Two solutions from one point',
     r'For $\dfrac{dy}{dt}=y^{1/3}$ with $y(0)=0$:'
     '\n'
     r'1. Show that it has two different solutions.'
     '\n'
     r'2. Explain why the theorem allows it.', [
         S(r'$F=y^{1/3}$ is continuous, but its $y$-derivative (power rule) has $y$ in the bottom.',
           r'\dfrac{\partial F}{\partial y}=\dfrac{1}{3\,y^{2/3}}\ \to\ \infty\ \text{at}\ y=0'),
         S(r'The start $(0,0)$ is on the bad line $y=0$, so the theorem promises nothing there. Solution 1 is the constant $y=0$: slope 0, and $0^{1/3}=0$.',
           r'y_1(t)=0'),
         S(r'Solution 2: separate, $y^{-1/3}dy=dt$. Power rule: $\int y^{-1/3}dy=\frac32y^{2/3}$. $y(0)=0$ makes $C=0$.', r'\tfrac32\,y^{2/3}=t'),
         S(r'Raise both sides to the power $\frac32$.', r'y_2(t)=\Big(\dfrac{2t}{3}\Big)^{3/2},\quad t\ge0'),
     ], r'$y=0$ and $y=(2t/3)^{3/2}$ both pass through $(0,0)$.'
        '\n\n'
        r'No contradiction: $\partial F/\partial y$ is infinite on $y=0$.')
fam = 'if(t>c,(2*(t-c)/3)^1.5,0)'
D.GRAPH(rf'''
title "$dy/dt=y^{{1/3}}$: one curve per point, except on $y=0$"
x -3 4 label="$t$"
y -1.5 3 label="$y$"
region "abs(y)>0.1" color=3 label="conditions hold ($y\neq0$)"
field "cbrt(y)"
family c 0 3 0.5 "{fam}" color=4 label="solutions through $(0,0)$"
hline "0" color=2 label="$\partial F/\partial y=\infty$"
drag P -1 1 label="start" color=1
solution "cbrt(y)" x0="P_x" y0="P_y" color=1 label="solution through your start"
caption "Drag the start anywhere off the axis: exactly one curve. The purple curves sit on $y=0$ and then lift off, so through any point on the axis pass many solutions."
''')

D.EX(r'A smooth $F$, yet the solution blows up',
     r'Solve $\dfrac{dy}{dt}=y^2$ with $y(0)=1$. For which $t$ does the solution exist?', [
         S(r"Check the theorem first: $F$ and its $y$-derivative are continuous everywhere, so there is exactly one solution.",
           r'F=y^2,\qquad\dfrac{\partial F}{\partial y}=2y'),
         S(r'Separate and integrate with the power rule, $\int y^{-2}dy=-\frac1y$.', r'\dfrac{dy}{y^2}=dt\ \Rightarrow\ -\dfrac1y=t+C'),
         S(r'Put in $y(0)=1$: $C=-1$. Solve for $y$.', r'-\dfrac1y=t-1\ \Rightarrow\ y=\dfrac{1}{1-t}'),
         S(r'As $t\to1$ the bottom goes to 0 and $y\to\infty$. The theorem only promises a solution **near** $t_0$; this one ends at $t=1$.',
           r'\text{exists only for } t<1'),
     ], r'$y(t)=\dfrac{1}{1-t}$, which exists only for $t<1$ (it blows up at $t=1$)')
D.GRAPH(r'''
title "$dy/dt=y^2$: drag the start, find the blow-up"
x -2 3 label="$t$"
y -2 6 label="$y$"
field "y^2"
drag P 0 1 label="$(t_0,y_0)$" color=1 snap=0.25
solution "y^2" x0="P_x" y0="P_y" color=1 label="the one solution"
vline "P_x+1/P_y" color=2 label="blow-up $t=t_0+1/y_0$"
readout "blows up at $t=$" "P_x+1/P_y"
caption "Start higher and it blows up sooner; start at $y_0=0$ and it stays $0$ forever. Below the axis it blows up to $-\infty$ in the past."
''')

D.PR('A linear equation: the region is a strip',
     r"For $(t-3)\dfrac{dy}{dt}+(\ln t)\,y=2t$ with $y(1)=2$:"
     "\n"
     r"1. Where do the theorem's conditions hold?"
     "\n"
     r"2. Is exactly one solution through the start guaranteed?", [
         S(r'Solve for $dy/dt$ to get $F$.', r'F=\dfrac{2t-(\ln t)\,y}{t-3}'),
         S(r'Differentiate in $y$ ($t$ held fixed): only the $y$ term survives.', r'\dfrac{\partial F}{\partial y}=-\dfrac{\ln t}{t-3}'),
         S(r'$\ln t$ needs $t>0$; dividing needs $t\neq3$. Neither depends on $y$, so the good regions are vertical strips.',
           r'0<t<3\quad\text{or}\quad t>3\qquad(\text{any }y)'),
         S(r'The start $(1,2)$ has $t=1$, inside $0<t<3$.', r'\text{exactly one solution}'),
     ], r'- **Conditions hold:** for $0<t<3$ and for $t>3$, at every $y$.'
        '\n'
        r'- **Guaranteed?** Yes: the start is in $0<t<3$.', diff='intermediate')

D.PR('Silent, not negative',
     r'For $t\dfrac{dy}{dt}=y$: how many solutions pass through $(0,0)$? Through $(0,1)$?', [
         S(r'Both break at $t=0$, so the theorem says nothing about either start.', r'F=\dfrac yt,\quad\dfrac{\partial F}{\partial y}=\dfrac1t'),
         S(r'Separate and integrate ($\ln|y|=\ln|t|+C$): every solution is a line through the origin.',
           r'\dfrac{dy}{y}=\dfrac{dt}{t}\ \Rightarrow\ y=c\,t\quad(\text{any } c)'),
         S(r'Every line $y=ct$ passes through $(0,0)$: infinitely many solutions.', r'(0,0):\ \infty\ \text{solutions}'),
         S(r'Put $t=0$ into the ODE itself: every solution has $y(0)=0$, so none reaches $(0,1)$.',
           r'0\cdot\dfrac{dy}{dt}=y(0)\ \Rightarrow\ y(0)=0'),
     ], r'- **Through $(0,0)$:** infinitely many (all $y=ct$).'
        '\n'
        r'- **Through $(0,1)$:** none.'
        '\n\n'
        r'Where the conditions fail, anything can happen.',
     diff='intermediate')

D.save()
