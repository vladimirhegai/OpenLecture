"""ELEC 231 Week 2 study note: classifying ODEs, IVPs, first-order RC/RL circuits.

Run:  .venv/Scripts/python.exe scripts/notes231/build_w2.py      (writes out/w2.json)
Every answer is checked with sympy below; every schematic is checked with /api/v1/schematics/check.
"""
import json
import urllib.request

import sympy as sp

from lib231 import Doc, S
from figs_w234 import make_w2  # noqa: E402
FIGS = make_w2()

D = Doc(week=2, title='Week 2: Classifying ODEs, Initial Value Problems and First-Order RC/RL Circuits',
        topic_keys=['ode_classification', 'initial_value_problems', 'first_order_circuits'])


def J(*lines):
    return '\n'.join(lines)


def sch(src):
    return '```schematic\n' + src.strip('\n') + '\n```'


# ====================================================================== sympy helpers
t = sp.symbols('t', real=True)
tp = sp.symbols('t', positive=True)
y = sp.Function('y')
K = sp.symbols('K')


def zero(e):
    return sp.simplify(sp.expand(e)) == 0


def check(cond, msg):
    assert cond, 'CHECK FAILED: ' + msg


def classify(expr, f=y, var=t):
    """expr == 0 is the ODE. Returns (order, linear, homogeneous, constcoef, autonomous)."""
    n = sp.ode_order(expr, f(var))
    ds = sp.symbols(f'd0:{n + 1}')
    e = sp.expand(expr)
    for k in range(n, 0, -1):
        e = e.subs(f(var).diff(var, k), ds[k])
    e = e.subs(f(var), ds[0])
    linear = all(sp.simplify(sp.diff(e, a, b)) == 0 for a in ds for b in ds)
    hom = cc = None
    if linear:
        coef = [sp.simplify(sp.diff(e, d)) for d in ds]
        rest = sp.simplify(e.subs({d: 0 for d in ds}))
        hom = rest == 0
        cc = all(not c.has(var) for c in coef)
    auto = not e.has(var)
    return n, linear, hom, cc, auto


def cls_is(expr, claim, f=y, var=t):
    got = classify(expr, f, var)
    check(got == claim, f'classification of {expr}: got {got}, claimed {claim}')


def ode1_solution_ok(x, a, forcing, x0):
    """x(t) solves dx/dt = a x + forcing with x(0) = x0."""
    check(zero(sp.diff(x, t) - (a * x + forcing)), f'{x} fails the ODE')
    check(zero(x.subs(t, 0) - x0), f'{x} fails x(0)={x0}')


def close(a, b, tol=1e-3):
    check(abs(float(a) - float(b)) <= tol * max(1, abs(float(b))), f'{a} != {b}')


# ====================================================================== schematic validation
SCHEMATICS = []


def S_(src):
    """Register a drawing for the endpoint check and return its fenced form."""
    SCHEMATICS.append(src.strip('\n'))
    return sch(src)


def validate_schematics():
    for src in SCHEMATICS:
        req = urllib.request.Request('http://127.0.0.1:8000/api/v1/schematics/check',
                                     data=json.dumps({'source': src}).encode(), method='POST',
                                     headers={'Content-Type': 'application/json'})
        out = json.load(urllib.request.urlopen(req))
        assert not out['errors'], f'schematic errors {out["errors"]} in\n{src}'
        conn = ', '.join(f"{e['name']}:{e['from']}-{e['to']}" for e in out['elements'])
        print('  schematic ok:', conn, ('WARN ' + str(out['warnings'])) if out['warnings'] else '')


# ====================================================================== overview
D.CO('info', J(
    r'**Week 2 in one sentence:** a differential equation is an equation for an unknown *function*; we learn to '
    r'name its type, to check a proposed solution, to pin down one solution with an initial condition, and to '
    r'write and solve the first-order equations that RC and RL circuits produce.',
    '',
    '**By the end you can:**',
    r'- classify an ODE: order, linear or nonlinear, homogeneous, constant-coefficient, autonomous;',
    r'- check whether a function solves an ODE by substituting it back, and solve an initial value problem for the constant;',
    r'- use $i=C\dfrac{dv}{dt}$ and $v=L\dfrac{di}{dt}$, and find $v_C$ and $i_L$ just before and just after a switch moves;',
    r'- write the ODE of an RC or RL circuit and solve it: natural response $x_0e^{-t/\tau}$ and step response '
    r'$x_f+(x_0-x_f)e^{-t/\tau}$.'))

D.CO('tip', J(
    '**What you need from earlier weeks**',
    '',
    r'- Week 1 RL natural response: an inductor current that starts at $I_s$ and flows through a resistor decays as '
    r'$i(t)=I_s e^{-t/\tau}$ with $\tau=L/R$. This week the capacitor does the same thing with $\tau=RC$.',
    r'- The number $e\approx 2.718$ and the exponential $e^{x}$: $e^{0}=1$, $e^{-1}\approx 0.37$, and $e^{-x}\to 0$ as $x\to\infty$.',
    r'- Kirchhoff\u2019s laws: KVL (the voltages around any closed loop add to zero) and KCL (the currents leaving any node add to zero).'
).replace(r'\u2019', '\u2019'))

# ====================================================================== TOPIC 1
D.H('Topic 1: What a differential equation is')

D.P(r'A **differential equation** is an equation whose unknown is a *function*, say $y(t)$, and which involves its '
    r'derivatives $\dfrac{dy}{dt}$, $\dfrac{d^2y}{dt^2}$, and so on. It does not ask "which number?" but "which curve?". '
    r'Circuits give us these equations because capacitors and inductors relate a voltage to the *rate of change* of a '
    r'current (or the reverse). Before solving anything we **classify** the equation, the same way you would look at an '
    r'algebra equation and say "this one is quadratic": the type tells you which method works. Shorthand used in quick '
    r'drills: $y\'$ means $\dfrac{dy}{dt}$ and $y\'\'$ means $\dfrac{d^2y}{dt^2}$; $y^{(n)}$ means the $n$-th derivative.'
    .replace("\\'", "'"))

D.CO('tip', J(
    '**The method: classifying an ODE**',
    '',
    r'1. Name the **dependent variable** (the unknown function, e.g. $y$, $i$, $v$) and the **independent variable** '
    r'(here always time $t$). Only one independent variable means it is an *ordinary* differential equation (ODE).',
    r'2. **Order** = the highest derivative of the unknown that appears.',
    r'3. **Linear?** Go term by term: the unknown and its derivatives may only appear on their own, to the first power, '
    r'multiplied by a number or a function of $t$. Any $y^2$, $y\,\dfrac{dy}{dt}$, $\sin y$, $e^{y}$, $\dfrac1y$ makes it **nonlinear**.',
    r'4. If linear, move every term with the unknown to the left; whatever is left on the right is $f(t)$. '
    r'**Homogeneous** means $f(t)=0$. **Constant-coefficient** means every number multiplying the unknown or a derivative is a constant.',
    r'5. **Autonomous?** Cover up every $y(t)$ and its derivatives: if no $t$ is left anywhere, the equation is autonomous.'))

D.P(r'The lecture\u2019s definition of a **linear** ODE of order $n$ is any equation that can be written in the form below. '
    r'The $a_k(t)$ are the **coefficients** (they may depend on $t$ but never on $y$), and $f(t)$ is the **forcing** '
    r'(the input, such as a source; it depends on $t$ only).'.replace(r'\u2019', '\u2019'), cites=D.cite('W2', 2))
D.EQ(r'\begin{aligned}&a_n(t)\dfrac{d^ny}{dt^n}+\dots+a_1(t)\dfrac{dy}{dt}\\&\qquad+a_0(t)\,y=f(t)\end{aligned}',
     cites=D.cite('W2', 2))

D.L([
    r'**Ordinary:** derivatives are taken with respect to only one independent variable (time $t$). '
    r'(An equation with $\partial u/\partial t$ and $\partial u/\partial x$ would be a *partial* differential equation, not in this course.)',
    r'**Order:** the highest derivative of the dependent variable. $\dfrac{di}{dt}+\dfrac{R}{L}i=0$ is first order; '
    r'the series RLC equation $\dfrac{d^2i}{dt^2}+\dfrac{R}{L}\dfrac{di}{dt}+\dfrac{i}{LC}=0$ is second order.',
    r'**Linear:** fits the form above. Useful consequence (from the lecture): if $y(t)$ solves it with input '
    r'$f(t)$, then $A\,y(t)$ solves it with input $A\,f(t)$. Double the source, double the response.',
    r'**Homogeneous** (linear equations only): $f(t)\equiv 0$, where $\equiv$ means "equal to zero for every $t$". '
    r'In a circuit this is the *natural response*: no source is driving it.',
    r'**Constant-coefficient** (linear equations only): $a_0,a_1,\dots,a_n$ are all constants, like $R$, $L$, $C$.',
    r'**Autonomous:** the equation does not depend on $t$ except through $y(t)$; the rule does not change with time.',
], cites=D.cite('W2', 2, 3))

D.T(['Term in the equation', 'Linear?', 'Why'], [
    [r'$5y$, $\;3\dfrac{dy}{dt}$', 'Yes', r'the unknown to the first power times a constant'],
    [r'$t^2\dfrac{d^2y}{dt^2}$, $\;e^{t}y$, $\;(\sin t)\,y$', 'Yes', r'the coefficient may be any function of $t$'],
    [r'$\sin t$, $\;e^{-t}$, $\;10$ (alone)', 'Yes', r'no $y$ at all: this is forcing $f(t)$, it only makes the equation nonhomogeneous'],
    [r'$y^2$, $\;y^3$, $\;\sqrt{y}$, $\;\dfrac{1}{y}$', 'No', r'the unknown is raised to a power other than 1'],
    [r'$y\dfrac{dy}{dt}$, $\;\left(\dfrac{dy}{dt}\right)^2$', 'No', r'the unknown (or its derivative) is multiplied by itself'],
    [r'$\sin y$, $\;e^{y}$, $\;\ln y$', 'No', r'the unknown sits inside a function'],
])

# ---- Example 1
D.EX('Classify the RL natural-response equation',
     r'Classify $\dfrac{di}{dt}+\dfrac{R}{L}\,i=0$, the Week 1 equation for the current $i(t)$ in an inductor $L$ '
     r'discharging through a resistor $R$.',
     [S(r'Name the variables: the unknown function is the current $i(t)$, the dependent variable, and it depends only '
        r'on time $t$, the independent variable. One independent variable, so this is an ODE.', r'i=i(t)'),
      S(r'Find the order: the highest derivative of $i$ that appears is the first derivative, so the equation is first order.',
        r'\text{highest derivative: } \dfrac{di}{dt}\;\Rightarrow\;\text{order }1'),
      S(r'Test linearity term by term: $\dfrac{di}{dt}$ appears alone and $i$ appears to the first power times the '
        r'constant $R/L$, so it matches the linear form with $a_1=1$, $a_0=R/L$.', r'1\cdot\dfrac{di}{dt}+\dfrac{R}{L}\,i=0'),
      S(r'Look at the right side: $f(t)=0$, so the equation is homogeneous (no source drives the circuit).', r'f(t)=0'),
      S(r'The coefficients $1$ and $R/L$ are fixed component values, so it has constant coefficients; and no $t$ appears '
        r'outside $i(t)$, so it is autonomous.', r'a_1=1,\quad a_0=\dfrac{R}{L}\ \text{(constants)}')],
     'First-order, linear, homogeneous, constant-coefficient, autonomous ODE.', cites=D.cite('W2', 2))
iF = sp.Function('i')
R, L, C = sp.symbols('R L C', positive=True)
cls_is(iF(t).diff(t) + R / L * iF(t), (1, True, True, True, True), f=iF)
cls_is(iF(t).diff(t, 2) + R / L * iF(t).diff(t) + iF(t) / (L * C), (2, True, True, True, True), f=iF)

# ---- Example 2 (lecture Example 2.1)
D.EX('Is it linear? (lecture Example 2.1)',
     r'Is $t^3\dfrac{d^2y}{dt^2}+e^{t}\dfrac{dy}{dt}+y=0$ a linear ODE? Give its full classification.',
     [S(r'Find the order: the highest derivative of $y$ is the second derivative.', r'\text{order }2'),
      S(r'Test each term for linearity: $\dfrac{d^2y}{dt^2}$, $\dfrac{dy}{dt}$ and $y$ each appear on their own, to the '
        r'first power. The multipliers $t^3$ and $e^{t}$ depend on $t$ only, which the linear form allows.',
        r'a_2(t)=t^3,\quad a_1(t)=e^{t},\quad a_0=1'),
      S(r'Read off the right side: $f(t)=0$, so the equation is homogeneous.', r'f(t)=0'),
      S(r'Check the coefficients: $t^3$ and $e^{t}$ change with time, so this is **not** constant-coefficient; for the '
        r'same reason $t$ appears outside $y$, so it is **not** autonomous.', r'')],
     'Yes, it is linear: second-order, linear, homogeneous, with variable (non-constant) coefficients, not autonomous. '
     'Linearity only cares how $y$ appears, not how $t$ appears.', cites=D.cite('W2', 3))
cls_is(t**3 * y(t).diff(t, 2) + sp.exp(t) * y(t).diff(t) + y(t), (2, True, True, False, False))

# ---- Example 3 (six equations)
six = [
    (r'\dfrac{dy}{dt}=3y+2', y(t).diff(t) - 3 * y(t) - 2, (1, True, False, True, True)),
    (r'\dfrac{d^2y}{dt^2}+t\,y=0', y(t).diff(t, 2) + t * y(t), (2, True, True, False, False)),
    (r'\dfrac{dy}{dt}=y^2', y(t).diff(t) - y(t)**2, (1, False, None, None, True)),
    (r'\dfrac{d^2y}{dt^2}+y\dfrac{dy}{dt}=\sin t', y(t).diff(t, 2) + y(t) * y(t).diff(t) - sp.sin(t), (2, False, None, None, False)),
    (r't\dfrac{dy}{dt}+y=t^2', t * y(t).diff(t) + y(t) - t**2, (1, True, False, False, False)),
    (r'\dfrac{d^3y}{dt^3}+4\dfrac{dy}{dt}=0', y(t).diff(t, 3) + 4 * y(t).diff(t), (3, True, True, True, True)),
]
for _, e, c in six:
    cls_is(e, c)
D.EX('Classify six equations',
     J('Classify each ODE (order; linear or nonlinear; if linear, homogeneous or not and constant-coefficient or not; autonomous or not).',
       '',
       *[f'{k}. ${s}$' for k, (s, _, _) in enumerate(six, 1)]),
     [S(r'Equation 1: first derivative only, so first order. Rewrite it with the unknown on the left: $\dfrac{dy}{dt}-3y=2$. '
        r'Linear, $f(t)=2\neq 0$ so nonhomogeneous, constant coefficients $1$ and $-3$, and no $t$ anywhere so autonomous.',
        r'\dfrac{dy}{dt}-3y=2'),
      S(r'Equation 2: second order. The term $t\,y$ is $y$ to the first power times a function of $t$, so it is linear '
        r'and homogeneous; but the coefficient $t$ varies, so it is not constant-coefficient and not autonomous.',
        r'a_0(t)=t'),
      S(r'Equation 3: first order. The term $y^2$ is the unknown squared, so the equation is **nonlinear** (homogeneous and '
        r'constant-coefficient only apply to linear equations). No $t$ appears, so it is autonomous.', r'y^2\ \text{is nonlinear}'),
      S(r'Equation 4: second order. The product $y\dfrac{dy}{dt}$ multiplies the unknown by its own derivative, so it is '
        r'nonlinear. The $\sin t$ shows $t$ explicitly, so it is not autonomous.', r'y\dfrac{dy}{dt}\ \text{is nonlinear}'),
      S(r'Equation 5: first order. Both $t\dfrac{dy}{dt}$ and $y$ are linear terms; $f(t)=t^2\neq 0$, so nonhomogeneous; '
        r'the coefficient $t$ varies, so not constant-coefficient and not autonomous.', r'a_1(t)=t,\ a_0=1,\ f(t)=t^2'),
      S(r'Equation 6: the highest derivative is the third, so third order. Every term is linear with constant coefficients '
        r'and $f=0$, so it is homogeneous and autonomous. (Notice the $y$ term itself is missing; that is allowed, $a_0=0$.)',
        r'a_3=1,\ a_2=0,\ a_1=4,\ a_0=0')],
     J('1. first order, linear, nonhomogeneous, constant-coefficient, autonomous.',
       '2. second order, linear, homogeneous, variable-coefficient, not autonomous.',
       '3. first order, nonlinear, autonomous.',
       '4. second order, nonlinear, not autonomous.',
       '5. first order, linear, nonhomogeneous, variable-coefficient, not autonomous.',
       '6. third order, linear, homogeneous, constant-coefficient, autonomous.'))
D.T(['Equation', 'Order', 'Linear?', 'Homogeneous?', 'Constant coeff.?', 'Autonomous?'], [
    [f'${s}$', str(c[0]), 'yes' if c[1] else 'no',
     '\u2014' if c[2] is None else ('yes' if c[2] else 'no'),
     '\u2014' if c[3] is None else ('yes' if c[3] else 'no'), 'yes' if c[4] else 'no'] for s, _, c in six])

D.CO('warning', J(
    '**Common mistakes**',
    '',
    r'- Calling $e^{t}\dfrac{dy}{dt}+y=0$ nonlinear because of $e^{t}$. Functions of $t$ are allowed; only functions of $y$ ($e^{y}$, $y^2$, $\sin y$) make it nonlinear.',
    r'- Deciding "homogeneous" before moving all $y$-terms to the left. $\dfrac{dy}{dt}=3y$ is homogeneous ($\dfrac{dy}{dt}-3y=0$); $\dfrac{dy}{dt}=3y+2$ is not.',
    r'- Reading the order from the power instead of the derivative: $\left(\dfrac{dy}{dt}\right)^3$ is still first order (it makes the equation nonlinear).'))

# ---- Try its topic 1
D.PR('Order and type',
     r'Classify $\dfrac{d^2y}{dt^2}+3\dfrac{dy}{dt}+2y=e^{-t}$.',
     [S(r'The highest derivative is the second, so it is second order.', r'\text{order }2'),
      S(r'Each of $\dfrac{d^2y}{dt^2}$, $\dfrac{dy}{dt}$, $y$ appears alone to the first power, times the constants 1, 3, 2, so it is linear with constant coefficients.',
        r'a_2=1,\ a_1=3,\ a_0=2'),
      S(r'The right side $e^{-t}$ has no $y$ in it, so it is the forcing $f(t)$; since it is not zero the equation is nonhomogeneous.', r'f(t)=e^{-t}\neq 0'),
      S(r'The forcing contains $t$ explicitly, so the equation is not autonomous.', r'')],
     'Second-order, linear, nonhomogeneous, constant-coefficient, not autonomous.')
cls_is(y(t).diff(t, 2) + 3 * y(t).diff(t) + 2 * y(t) - sp.exp(-t), (2, True, False, True, False))

lin6 = [
    (r'\dfrac{dy}{dt}+y^3=0', y(t).diff(t) + y(t)**3, False, r'$y^3$ is a power of the unknown'),
    (r'\dfrac{dy}{dt}+t^3y=0', y(t).diff(t) + t**3 * y(t), True, r'$t^3$ is a coefficient that depends on $t$ only'),
    (r'y\dfrac{dy}{dt}=1', y(t) * y(t).diff(t) - 1, False, r'the unknown multiplies its own derivative'),
    (r'\dfrac{d^2y}{dt^2}+\sin y=0', y(t).diff(t, 2) + sp.sin(y(t)), False, r'the unknown sits inside $\sin$'),
    (r'\dfrac{d^2y}{dt^2}+(\sin t)\,y=0', y(t).diff(t, 2) + sp.sin(t) * y(t), True, r'$\sin t$ is a coefficient depending on $t$'),
    (r'\dfrac{dy}{dt}=e^{y}', y(t).diff(t) - sp.exp(y(t)), False, r'the unknown sits inside the exponential'),
]
for _, e, ok, _ in lin6:
    check(classify(e)[1] == ok, f'lin6 {e}')
D.PR('Linear or nonlinear?',
     J('Which of these ODEs are linear? Give the reason for each.', '', *[f'{k}. ${s}$' for k, (s, _, _, _) in enumerate(lin6, 1)]),
     [S(f'Equation {k}: ' + ('**linear**, because ' if ok else '**nonlinear**, because ') + why + '.', s)
      for k, (s, _, ok, why) in enumerate(lin6, 1)],
     'Linear: 2 and 5. Nonlinear: 1, 3, 4, 6.')

auto5 = [
    (r'\dfrac{dy}{dt}=y(1-y)', y(t).diff(t) - y(t) * (1 - y(t)), True),
    (r'\dfrac{dy}{dt}=t-y', y(t).diff(t) - t + y(t), False),
    (r'L\dfrac{di}{dt}+Ri=10', None, True),
    (r'L\dfrac{di}{dt}+Ri=10\cos(100t)', None, False),
    (r'\dfrac{d^2y}{dt^2}+2\dfrac{dy}{dt}+5y=0', y(t).diff(t, 2) + 2 * y(t).diff(t) + 5 * y(t), True),
]
check(classify(L * iF(t).diff(t) + R * iF(t) - 10, iF)[4] is True, 'auto L')
check(classify(L * iF(t).diff(t) + R * iF(t) - 10 * sp.cos(100 * t), iF)[4] is False, 'auto Lcos')
for _, e, ok in auto5:
    if e is not None:
        check(classify(e)[4] == ok, f'auto {e}')
D.PR('Autonomous or not?',
     J('Which of these ODEs are autonomous? ($L$ and $R$ are constants.)', '', *[f'{k}. ${s}$' for k, (s, _, _) in enumerate(auto5, 1)]),
     [S(r'Equation 1: cover up $y$; nothing with $t$ is left, so it is autonomous (even though it is nonlinear: autonomy does not care about linearity).', r'y(1-y)'),
      S(r'Equation 2: a bare $t$ remains on the right, so it is not autonomous.', r't-y'),
      S(r'Equation 3: the source is the constant 10, so the rule never changes with time: autonomous.', r'f=10\ \text{(constant)}'),
      S(r'Equation 4: the source $10\cos(100t)$ changes with time, so it is not autonomous.', r'f(t)=10\cos(100t)'),
      S(r'Equation 5: only constants multiply $y$ and its derivatives, and no forcing: autonomous.', r'')],
     'Autonomous: 1, 3 and 5. Not autonomous: 2 and 4.')

# ====================================================================== TOPIC 2
D.H('Topic 2: Solutions and initial value problems')

D.P(r'A **solution** of an ODE is a function that makes the equation true for *every* $t$ in an interval when you substitute '
    r'it in. To **check** a proposed solution you never need to solve anything: differentiate it, substitute into the left '
    r'and right sides, and simplify until both sides are visibly the same. A first-order ODE usually has a whole **family** '
    r'of solutions with one free constant $K$ (the *general solution*). An **initial value problem (IVP)** is the ODE plus '
    r'one **initial condition** $y(t_0)=y_0$ (the value at a starting time $t_0$, usually $0$); the condition picks out the one '
    r'curve of the family that passes through that starting point. A second-order equation needs two conditions, $y(t_0)$ and $\dfrac{dy}{dt}(t_0)$.')
D.CO('tip', J(
    '**The method: checking a solution and solving an IVP**',
    '',
    r'1. Differentiate the proposed $y(t)$ as many times as the order of the equation.',
    r'2. Substitute $y$ and its derivatives into the left side and simplify; do the same for the right side.',
    r'3. If the two sides agree for every $t$, it is a solution. If a leftover term remains (like $3\sin t$), it is not.',
    r'4. For an IVP: set $t=t_0$ in the general solution, set it equal to $y_0$, and solve for the constant $K$.',
    r'5. Write the final answer with the number in place of $K$ and check $y(t_0)=y_0$ once more.'))
D.P(r'The key formula is the IVP itself: an ODE plus the value at the starting time. For example, the family '
    r'$y=3+Ke^{-2t}$ below solves $\dfrac{dy}{dt}=-2y+6$ for every $K$, and $y(0)=1$ picks $K=-2$.')
D.EQ(r'\begin{gathered}\text{ODE: }\dfrac{dy}{dt}=F(t,y) \\ \text{initial condition: }y(t_0)=y_0\end{gathered}')

# ---- calculus reminder (derivatives)
D.CO('info', J(
    r'**Calculus reminder: the derivatives you need this week.** To check a solution you differentiate it, so keep these at hand ($a$, $k$ are constants):',
    '',
    r'- **Constant rule:** $\dfrac{d}{dt}k=0$. **Constant multiple:** $\dfrac{d}{dt}\big(k\,g(t)\big)=k\,\dfrac{dg}{dt}$. **Sums:** differentiate term by term.',
    r'- **Power rule:** $\dfrac{d}{dt}t^n=n\,t^{n-1}$ (so $\dfrac{d}{dt}t^2=2t$, $\dfrac{d}{dt}t=1$).',
    r'- **Exponential, by the chain rule:** $\dfrac{d}{dt}e^{at}=a\,e^{at}$. The chain rule says: differentiate the outside function '
    r'(here $e^{u}\to e^{u}$), then multiply by the derivative of the inside ($u=at\to a$). Example: $\dfrac{d}{dt}e^{-2t}=-2e^{-2t}$.',
    r'- **Sine and cosine, by the chain rule:** $\dfrac{d}{dt}\sin(at)=a\cos(at)$, $\;\dfrac{d}{dt}\cos(at)=-a\sin(at)$.',
    r'- **Product rule:** $\dfrac{d}{dt}\big(g\,h\big)=\dfrac{dg}{dt}\,h+g\,\dfrac{dh}{dt}$ (used for things like $t\,e^{-t}$).'))

# ---- Example 4 (check solutions)
D.EX('Checking solutions by substitution',
     J(r'1. Show that $y=5e^{-2t}$ solves $\dfrac{dy}{dt}+2y=0$.',
       r'2. Which of $y=\cos 2t$, $\;y=\sin t$, $\;y=3\sin 2t$ solve $\dfrac{d^2y}{dt^2}+4y=0$?'),
     [S(r'Part 1: differentiate with the chain rule, $\dfrac{d}{dt}e^{-2t}=-2e^{-2t}$, keeping the constant 5 in front.',
        r'\dfrac{dy}{dt}=5\cdot(-2)e^{-2t}=-10e^{-2t}'),
      S(r'Substitute $y$ and $\dfrac{dy}{dt}$ into the left side; the two terms cancel, matching the right side $0$ for every $t$.',
        r'-10e^{-2t}+2\cdot 5e^{-2t}=0\ \checkmark'),
      S(r'Part 2, $y=\cos 2t$: differentiate twice with the chain rule (each time a factor 2 comes out).',
        r'\begin{gathered}\dfrac{dy}{dt}=-2\sin 2t \\ \dfrac{d^2y}{dt^2}=-4\cos 2t\end{gathered}'),
      S(r'Substitute: the left side becomes zero, so $\cos 2t$ is a solution.', r'-4\cos 2t+4\cos 2t=0\ \checkmark'),
      S(r'$y=\sin t$: the second derivative is $-\sin t$. Substituting leaves $3\sin t$, which is not zero for every $t$, so this is **not** a solution.',
        r'-\sin t+4\sin t=3\sin t\neq 0'),
      S(r'$y=3\sin 2t$: the second derivative is $3\cdot(-4)\sin 2t=-12\sin 2t$; substituting gives zero, so it is a solution.',
        r'-12\sin 2t+4\cdot 3\sin 2t=0\ \checkmark')],
     r'1. Yes, $y=5e^{-2t}$ is a solution (and so is $Ke^{-2t}$ for any constant $K$). 2. $\cos 2t$ and $3\sin 2t$ are solutions; $\sin t$ is not.')
check(zero(sp.diff(5 * sp.exp(-2 * t), t) + 2 * 5 * sp.exp(-2 * t)), 'ex4 a')
for fn, ok in [(sp.cos(2 * t), True), (sp.sin(t), False), (3 * sp.sin(2 * t), True)]:
    check(zero(sp.diff(fn, t, 2) + 4 * fn) == ok, f'ex4 {fn}')

# ---- Example 5 (IVP) + charts
D.EX('An initial value problem picks one curve',
     J(r'1. Show that $y=3+Ke^{-2t}$ solves $\dfrac{dy}{dt}=-2y+6$ for **every** constant $K$.',
       r'2. Solve the IVP with $y(0)=1$.',
       r'3. Solve it again with $y(0)=5$ and describe both curves.'),
     [S(r'Differentiate the proposed solution: the constant 3 has derivative 0 and the chain rule gives $\dfrac{d}{dt}e^{-2t}=-2e^{-2t}$.',
        r'\dfrac{dy}{dt}=-2Ke^{-2t}'),
      S(r'Compute the right side with the same $y$: expand $-2(3+Ke^{-2t})$ and add 6; the 6s cancel.',
        r'-2(3+Ke^{-2t})+6=-2Ke^{-2t}'),
      S(r'Both sides equal $-2Ke^{-2t}$ no matter what $K$ is, so the whole family is a family of solutions.', r'\text{left}=\text{right}\ \checkmark'),
      S(r'Part 2: set $t=0$ in the general solution (using $e^{0}=1$) and make it equal the initial value 1; solve for $K$.',
        r'y(0)=3+K=1\;\Rightarrow\;K=-2'),
      S(r'Put $K=-2$ back in: this curve starts at 1 and rises toward 3.', r'y(t)=3-2e^{-2t}'),
      S(r'Part 3: the same step with $y(0)=5$ gives $K=2$, a curve that starts at 5 and falls toward 3. As $t\to\infty$, '
        r'$e^{-2t}\to 0$, so every member of the family settles at $y=3$; the initial condition only decides where it starts.',
        r'\begin{gathered}3+K=5\;\Rightarrow\;K=2 \\ y(t)=3+2e^{-2t}\end{gathered}')],
     r'1. Shown above. 2. $y=3-2e^{-2t}$. 3. $y=3+2e^{-2t}$. Both settle at 3; one rises from 1, the other falls from 5.')
yK = 3 + K * sp.exp(-2 * t)
check(zero(sp.diff(yK, t) - (-2 * yK + 6)), 'ex5 family')
ode1_solution_ok(3 - 2 * sp.exp(-2 * t), -2, 6, 1)
ode1_solution_ok(3 + 2 * sp.exp(-2 * t), -2, 6, 5)
D.FIG(FIGS['family'], r'Example 5 in one picture. The grey dashed curves are other members of the family $y=3+Ke^{-2t}$; the initial condition picks one: $y(0)=1$ gives the blue curve, $y(0)=5$ the orange one. Every curve settles at $y=3$.')

D.CO('warning', J(
    '**Common mistakes**',
    '',
    r'- Checking at one time only. A solution must make both sides agree for **every** $t$; $y=\sin t$ in Example 4 leaves $3\sin t$, which is zero at $t=0$ but not in general, so it is not a solution.',
    r'- Using $y(0)$ before writing the constant $K$: you need the whole family first, then the initial condition chooses $K$.',
    r'- Giving a second-order IVP only one condition. It needs two, $y(t_0)$ and $\dfrac{dy}{dt}(t_0)$, because there are two constants to find.'))

# ---- Try its topic 2
D.PR('Check a solution with the product rule',
     r'Show that $y=t\,e^{-t}$ solves $\dfrac{d^2y}{dt^2}+2\dfrac{dy}{dt}+y=0$.',
     [S(r'Differentiate with the product rule, taking $g=t$ (so $\dfrac{dg}{dt}=1$) and $h=e^{-t}$ (so $\dfrac{dh}{dt}=-e^{-t}$ by the chain rule).',
        r'\dfrac{dy}{dt}=1\cdot e^{-t}+t\cdot(-e^{-t})=e^{-t}-te^{-t}'),
      S(r'Differentiate again: $e^{-t}$ gives $-e^{-t}$, and $-te^{-t}$ gives (product rule again) $-e^{-t}+te^{-t}$.',
        r'\dfrac{d^2y}{dt^2}=-e^{-t}-e^{-t}+te^{-t}=-2e^{-t}+te^{-t}'),
      S(r'Substitute all three into the left side and collect the $e^{-t}$ terms and the $te^{-t}$ terms separately.',
        r'\begin{aligned}&(-2e^{-t}+te^{-t})+2(e^{-t}-te^{-t})\\&\quad+te^{-t}=0\end{aligned}'),
      S(r'The $e^{-t}$ terms give $-2+2=0$ and the $te^{-t}$ terms give $1-2+1=0$, so the left side is zero for every $t$.', r'0=0\ \checkmark')],
     r'Yes: substituting gives $0$ for every $t$, so $y=te^{-t}$ is a solution.', diff='intermediate')
yy = t * sp.exp(-t)
check(zero(sp.diff(yy, t, 2) + 2 * sp.diff(yy, t) + yy), 'try te^-t')

D.PR('Solve a first-order IVP',
     J(r'1. Show that $y=2+Ke^{-3t}$ solves $\dfrac{dy}{dt}+3y=6$ for every constant $K$.',
       r'2. Find the solution with $y(0)=-1$.', r'3. What value does it approach as $t\to\infty$?'),
     [S(r'Differentiate: the constant 2 gives 0 and the chain rule gives $\dfrac{d}{dt}e^{-3t}=-3e^{-3t}$.', r'\dfrac{dy}{dt}=-3Ke^{-3t}'),
      S(r'Substitute into the left side; the $K$ terms cancel and 6 is left, which is the right side.',
        r'-3Ke^{-3t}+3(2+Ke^{-3t})=6\ \checkmark'),
      S(r'Use the initial condition: at $t=0$, $e^{0}=1$, so $y(0)=2+K$. Set it equal to $-1$ and solve.', r'2+K=-1\;\Rightarrow\;K=-3'),
      S(r'Write the solution and let $t\to\infty$: $e^{-3t}\to 0$, so $y\to 2$.', r'y(t)=2-3e^{-3t}\;\to\;2')],
     r'1. Shown. 2. $y(t)=2-3e^{-3t}$. 3. It approaches 2.', diff='intermediate')
check(zero(sp.diff(2 + K * sp.exp(-3 * t), t) + 3 * (2 + K * sp.exp(-3 * t)) - 6), 'try family 2+K')
ode1_solution_ok(2 - 3 * sp.exp(-3 * t), -3, 6, -1)

r_ = sp.symbols('r')
D.PR('Exponential guesses and a second-order IVP',
     J(r'1. For which numbers $r$ does $y=e^{rt}$ solve $\dfrac{d^2y}{dt^2}-\dfrac{dy}{dt}-6y=0$?',
       r'2. Check that $y=c_1e^{3t}+c_2e^{-2t}$ solves it for any constants $c_1,c_2$.',
       r'3. Find $c_1,c_2$ so that $y(0)=0$ and $\dfrac{dy}{dt}(0)=5$.'),
     [S(r'Differentiate $e^{rt}$ with the chain rule: each derivative brings out a factor $r$.', r'\begin{gathered}\dfrac{dy}{dt}=re^{rt} \\ \dfrac{d^2y}{dt^2}=r^2e^{rt}\end{gathered}'),
      S(r'Substitute and factor out $e^{rt}$. Since $e^{rt}$ is never zero, the bracket must be zero.', r'(r^2-r-6)\,e^{rt}=0\;\Rightarrow\;r^2-r-6=0'),
      S(r'Factor the quadratic: two numbers that multiply to $-6$ and add to $-1$ are $-3$ and $2$.', r'(r-3)(r+2)=0\;\Rightarrow\;r=3\ \text{or}\ r=-2'),
      S(r'Part 2: the equation is linear and homogeneous, so a sum of solutions is a solution. Directly: each piece makes its own bracket zero, so the sum gives $0+0$.',
        r'c_1(9-3-6)e^{3t}+c_2(4+2-6)e^{-2t}=0'),
      S(r'Part 3: a second-order IVP needs two conditions. Use $y(0)=0$ with $e^0=1$.', r'c_1+c_2=0'),
      S(r'Differentiate $y$ and use $\dfrac{dy}{dt}(0)=5$.', r'\dfrac{dy}{dt}=3c_1e^{3t}-2c_2e^{-2t}\;\Rightarrow\;3c_1-2c_2=5'),
      S(r'Solve the pair: from the first equation $c_2=-c_1$; substitute into the second to get $5c_1=5$.', r'c_1=1,\quad c_2=-1')],
     r'1. $r=3$ or $r=-2$. 2. Shown. 3. $y=e^{3t}-e^{-2t}$.', diff='advanced')
check(set(sp.solve(r_**2 - r_ - 6, r_)) == {3, -2}, 'roots')
c1, c2 = sp.symbols('c1 c2')
yc = c1 * sp.exp(3 * t) + c2 * sp.exp(-2 * t)
check(zero(sp.diff(yc, t, 2) - sp.diff(yc, t) - 6 * yc), 'family 2nd')
sol = sp.solve([yc.subs(t, 0), sp.diff(yc, t).subs(t, 0) - 5], [c1, c2])
check(sol == {c1: 1, c2: -1}, 'c1 c2')

# ====================================================================== TOPIC 3
D.H('Topic 3: First-order circuits make first-order ODEs')

D.P(r'A circuit with resistors and **one** capacitor (an RC circuit) or **one** inductor (an RL circuit) always gives a '
    r'first-order, linear, constant-coefficient ODE, because the capacitor and inductor laws contain one derivative. When a '
    r'switch moves at $t=0$, the capacitor voltage $v_C$ (or inductor current $i_L$) slides exponentially from where it was '
    r'(its **initial value**) to where the new circuit wants it (its **final value**). How fast is set by the **time constant** '
    r'$\tau$ (tau): the time to cover about 63% of the remaining change. Think of filling a bucket through a narrow pipe: fast '
    r'at first, slower as it nears the top. You use this whenever a problem says "the switch has been in position a for a long time and moves at $t=0$".')

D.CO('tip', J(
    '**The method: any RC or RL circuit after a switch**',
    '',
    r'1. **Before** ($t<0$, "a long time"): the circuit is in DC steady state, so a capacitor is an open circuit and an inductor is a short. Find $v_C(0^-)$ or $i_L(0^-)$.',
    r'2. **Carry over:** $v_C$ and $i_L$ cannot jump, so $v_C(0^+)=v_C(0^-)$ and $i_L(0^+)=i_L(0^-)$. Write $x$ for whichever of $v_C$, $i_L$ the circuit has; this carried-over value is the initial value $x_0$.',
    r'3. **After** ($t\ge 0$): write KCL or KVL using $i=C\dfrac{dv}{dt}$ or $v=L\dfrac{di}{dt}$, and divide so the derivative stands alone: $\dfrac{dx}{dt}+\dfrac{x}{\tau}=\dfrac{x_f}{\tau}$.',
    r'4. Read off $\tau$ ($RC$ for a capacitor, $L/R$ for an inductor, with $R$ the resistance the element sees after the switch moves) and the final value $x_f$ (DC steady state again, or set $\dfrac{dx}{dt}=0$). With no source left, $x_f=0$: the natural response $x_0e^{-t/\tau}$.',
    r'5. Write $x(t)=x_f+(x_0-x_f)e^{-t/\tau}$ and check $x(0)=x_0$ and $x(\infty)=x_f$.'))

D.P(r'Both laws use the **passive sign convention**: the reference current arrow enters the $+$ terminal of the element\u2019s '
    r'voltage. $L$ is the **inductance** in henries (H) and $C$ the **capacitance** in farads (F). In **DC steady state** nothing '
    r'changes, so every derivative is zero: the inductor has $v=0$ (a **short**, a plain wire) and the capacitor has $i=0$ (an '
    r'**open circuit**, a break). The same laws explain why $v_C$ and $i_L$ **cannot jump**: a sudden jump in $v_C$ would make '
    r'$\dfrac{dv}{dt}$ infinite and need an infinite current, and a jump in $i_L$ would need an infinite voltage. Other quantities '
    r'(the capacitor *current*, the inductor *voltage*, resistor voltages) can and often do jump. We write $0^-$ for "just before the switch" and $0^+$ for "just after".'
    .replace(r'\u2019', '\u2019'), cites=D.cite('W2', 1, 2))
D.EQ(r'\begin{gathered}v=L\dfrac{di}{dt} \\ i=C\dfrac{dv}{dt}\end{gathered}', cites=D.cite('W2', 1, 2))
SRC_ELEM = '''
L1 0,3 -> 0,0 "$L$" i="$i$" v="$v$"
terminal 0,3 "" left
terminal 0,0 "" left
C1 4,3 -> 4,0 "$C$" i="$i$" v="$v$"
terminal 4,3 "" left
terminal 4,0 "" left
'''
SCHEMATICS.append(SRC_ELEM.strip('\n'))
D.SCH(SRC_ELEM.strip('\n'), r'The inductor and the capacitor with the passive sign convention: the current $i$ enters the $+$ end of $v$ (lecture Figures 2.1 and 2.2).',
      cites=D.cite('W2', 1, 2))

# ---- Example 6
D.EX('Current from voltage and voltage from current',
     J(r'1. The voltage across a $2\,\mu\mathrm{F}$ capacitor is $v(t)=10e^{-50t}\,\mathrm{V}$. Find its current $i(t)$ (passive sign convention).',
       r'2. The current in a $0.2\,\mathrm{H}$ inductor is $i(t)=3e^{-100t}\,\mathrm{A}$. Find its voltage $v(t)$.',
       r'3. What is the capacitor current if its voltage is held at a constant $5\,\mathrm{V}$?'),
     [S(r'Part 1: differentiate the voltage with the chain rule, $\dfrac{d}{dt}e^{-50t}=-50e^{-50t}$.', r'\dfrac{dv}{dt}=10\cdot(-50)e^{-50t}=-500e^{-50t}\ \mathrm{V/s}'),
      S(r'Multiply by $C=2\,\mu\mathrm{F}=2\times10^{-6}\,\mathrm{F}$.', r'i=C\dfrac{dv}{dt}=2\times10^{-6}(-500)e^{-50t}=-10^{-3}e^{-50t}\ \mathrm{A}'),
      S(r'The minus sign means the current actually flows out of the $+$ terminal: the capacitor is discharging, giving energy back to the circuit.', r'i(t)=-e^{-50t}\ \mathrm{mA}'),
      S(r'Part 2: differentiate the current with the chain rule and multiply by $L=0.2\,\mathrm{H}$.', r'v=L\dfrac{di}{dt}=0.2\cdot 3\cdot(-100)e^{-100t}=-60e^{-100t}\ \mathrm{V}'),
      S(r'Part 3: a constant has zero derivative, so the capacitor current is zero: in DC it acts as an open circuit.', r'i=C\cdot\dfrac{d}{dt}(5)=0')],
     r'1. $i(t)=-e^{-50t}\,\mathrm{mA}$. 2. $v(t)=-60e^{-100t}\,\mathrm{V}$. 3. $i=0$ (open circuit in DC).')
check(zero(sp.Rational(2, 10**6) * sp.diff(10 * sp.exp(-50 * t), t) + sp.Rational(1, 1000) * sp.exp(-50 * t)), 'ex6 a')
check(zero(sp.Rational(1, 5) * sp.diff(3 * sp.exp(-100 * t), t) + 60 * sp.exp(-100 * t)), 'ex6 b')

# ---- calculus reminder (integrals, ln)
D.CO('info', J(
    r'**Calculus reminder: integrals, logs and exponentials for the next example.**',
    '',
    r'- An **antiderivative** undoes a derivative: $\displaystyle\int k\,dt=kt+K$ and $\displaystyle\int\dfrac{1}{x}\,dx=\ln|x|+K$ ($K$ is the constant of integration; add it once).',
    r'- **Separation of variables:** put everything with $v$ on one side (with $dv$) and everything with $t$ on the other (with $dt$), then integrate both sides.',
    r'- **ln and exp undo each other:** $e^{\ln A}=A$ and $\ln(e^{x})=x$. Also $e^{a+b}=e^{a}e^{b}$ and $\ln\dfrac{a}{b}=\ln a-\ln b$, $\ln\dfrac1a=-\ln a$.',
    r'- **Solving for time:** $e^{-t/\tau}=p$ gives $-t/\tau=\ln p$, so $t=\tau\ln\dfrac{1}{p}$.'))

# ---- Example 7 (lecture natural response)
SRC_NAT = '''
V1 0,3 -> 0,0 "$V_s$"
R1 0,3 -> 3,3 "$R_1$"
S1 3,3 -> 5,3 "$t=0$" action=open
C1 5,3 -> 5,0 "$C$" v="$v$"
S2 5,3 -> 8,3 "$t=0$" action=close
R2 8,3 -> 8,0 "$R$" i="$i$"
wire 8,0 -> 0,0
label 3,3 "$a$" above
label 8,3 "$b$" above
ground 0,0
'''
D.EX('RC natural response (lecture Figures 2.3 and 2.4)',
     J(r'The switch has connected the capacitor to the source side (position a: $V_s$ through $R_1$) for a long time. '
       r'At $t=0$ it moves to position b, so the capacitor is disconnected from the source and connected across $R$ alone. '
       r'(The drawing shows the single a-to-b switch as two switches that act together at $t=0$.) Find $v(t)$ for $t\ge 0$.',
       '', S_(SRC_NAT)),
     [S(r'Before $t=0$ the circuit is in DC steady state, so the capacitor is an open circuit: no current flows through $R_1$, '
        r'so $R_1$ has no voltage across it and the capacitor sees the full source voltage.', r'v(0^-)=V_s'),
      S(r'The capacitor voltage cannot jump, so the initial value for $t\ge0$ is the same.', r'v(0)=v(0^+)=V_s'),
      S(r'For $t\ge 0$ only the loop $C$–$R$ is left. Apply KCL at the top node: the capacitor current $C\dfrac{dv}{dt}$ '
        r'(downward, passive convention) plus the resistor current $\dfrac{v}{R}$ (downward) must add to zero.',
        r'C\dfrac{dv}{dt}+\dfrac{v}{R}=0'),
      S(r'Divide by $C$ so the derivative stands alone; this is a first-order, linear, homogeneous ODE, the same shape as the Week 1 RL equation.',
        r'\dfrac{dv}{dt}+\dfrac{v}{RC}=0'),
      S(r'Separate the variables: move $\dfrac{v}{RC}$ to the right, divide by $v$ and multiply by $dt$.', r'\dfrac{dv}{v}=-\dfrac{1}{RC}\,dt'),
      S(r'Integrate both sides, using $\int\dfrac{dv}{v}=\ln|v|$ on the left and $\int k\,dt=kt$ on the right, with one constant $K$.',
        r'\ln|v|=-\dfrac{t}{RC}+K'),
      S(r'Exponentiate both sides ($e^{\ln|v|}=|v|$) and split $e^{-t/RC+K}=e^{K}e^{-t/RC}$; call the constant $A=\pm e^{K}$.',
        r'v(t)=A\,e^{-t/RC}'),
      S(r'Use the initial condition: at $t=0$, $e^0=1$, so $A=v(0)=V_s$. Define the time constant $\tau=RC$.', r'v(t)=V_s\,e^{-t/\tau},\quad \tau=RC,\ t\ge 0')],
     r'$v(t)=V_s\,e^{-t/RC}$ for $t\ge 0$: the capacitor discharges exponentially through $R$ with time constant $\tau=RC$.',
     cites=D.cite('W2', 3, 4))
Vs, Is, V0 = sp.symbols('V_s I_s V_0', real=True)
vn = Vs * sp.exp(-t / (R * C))
check(zero(C * sp.diff(vn, t) + vn / R), 'natural ODE')
check(zero(vn.subs(t, 0) - Vs), 'natural IC')
check(sp.dsolve(sp.Eq(sp.Function('v')(t).diff(t) + sp.Function('v')(t) / (R * C), 0),
                ics={sp.Function('v')(0): Vs}).rhs.equals(vn), 'dsolve natural')

D.CHART(r'Natural response with sample values $V_s=10\,\mathrm{V}$, $\tau=RC=1\,\mathrm{ms}$: the voltage starts at 10 V, is down to '
        r'$10e^{-1}\approx 3.7\,\mathrm{V}$ at $t=\tau=1\,\mathrm{ms}$, and is practically zero by $5\tau=5\,\mathrm{ms}$. The slope at the start is steepest.',
        order=1, a=-1000.0, y0=10.0, duration=0.005)

D.T(['Time since the switch', 'Fraction of the change still left: $e^{-t/\\tau}$', 'Fraction done: $1-e^{-t/\\tau}$'], [
    [r'$t=\tau$', '36.8% (about 37%)', '63.2% (about 63%)'],
    [r'$t=2\tau$', '13.5%', '86.5%'],
    [r'$t=3\tau$', '5.0%', '95.0%'],
    [r'$t=4\tau$', '1.8%', '98.2%'],
    [r'$t=5\tau$', '0.7%', '99.3%: treat as "settled"'],
], cites=D.cite('W2', 4))
for n_, left in [(1, 36.8), (2, 13.5), (3, 5.0), (4, 1.8), (5, 0.7)]:
    check(abs(float(100 * sp.exp(-n_)) - left) < 0.05, f'e^-{n_}')

# ---- Example 8 (lecture step response)
SRC_STEP = '''
I1 0,0 -> 0,3 "$I_s$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$R$" i="$v/R$"
S1 3,3 -> 6,3 "$t=0$" action=close
C1 6,3 -> 6,0 "$C$" v="$v$" i="$i$"
wire 6,0 -> 0,0
ground 0,0
'''
D.EX('RC step response (lecture Figure 2.6)',
     J(r'A DC current source $I_s$ and a resistor $R$ are connected in parallel. At $t=0$ the switch closes and connects the capacitor $C$, '
       r'whose initial voltage is $V_0$, in parallel with them. Find $v(t)$ for $t\ge 0$.', '', S_(SRC_STEP)),
     [S(r'For $t\ge0$ all three elements share the top node. KCL: the source current $I_s$ entering the node equals the resistor current $\dfrac{v}{R}$ plus the capacitor current $C\dfrac{dv}{dt}$ leaving it.',
        r'C\dfrac{dv}{dt}+\dfrac{v}{R}=I_s'),
      S(r'Divide by $C$: the left side has the same shape as the natural response, so the time constant is again $\tau=RC$; the right side is a constant forcing, so the equation is nonhomogeneous.',
        r'\dfrac{dv}{dt}+\dfrac{v}{RC}=\dfrac{I_s}{C}'),
      S(r'Find the final value: as $t\to\infty$ the circuit reaches DC steady state, $\dfrac{dv}{dt}\to0$ (capacitor open), and all of $I_s$ goes through $R$.',
        r'0+\dfrac{V_f}{RC}=\dfrac{I_s}{C}\;\Rightarrow\;V_f=RI_s'),
      S(r'Substitution: let $u=v-V_f$, the distance still to go. Since $V_f$ is a constant, $\dfrac{du}{dt}=\dfrac{dv}{dt}$, and $v=u+V_f$. Substituting, the $I_s/C$ terms cancel.',
        r'\dfrac{du}{dt}+\dfrac{u+RI_s}{RC}=\dfrac{I_s}{C}\;\Rightarrow\;\dfrac{du}{dt}+\dfrac{u}{RC}=0'),
      S(r'This is exactly the natural-response equation of Example 7, so its solution is $u(0)\,e^{-t/RC}$, with $u(0)=V_0-V_f$.',
        r'u(t)=(V_0-V_f)\,e^{-t/\tau}'),
      S(r'Undo the substitution, $v=V_f+u$, and check the ends: at $t=0$ we get $V_0$; as $t\to\infty$ we get $V_f$.',
        r'v(t)=RI_s+(V_0-RI_s)\,e^{-t/RC}')],
     r'$v(t)=V_f+(V_0-V_f)e^{-t/\tau}$ with $V_f=RI_s$ and $\tau=RC$, i.e. $v(t)=RI_s+(V_0-RI_s)e^{-t/RC}$, $t\ge 0$.',
     cites=D.cite('W2', 4, 5))
vs_ = R * Is + (V0 - R * Is) * sp.exp(-t / (R * C))
check(zero(C * sp.diff(vs_, t) + vs_ / R - Is), 'step ODE')
check(zero(vs_.subs(t, 0) - V0), 'step IC')
check(zero(sp.limit(vs_.subs(t, tp), tp, sp.oo) - R * Is), 'step final')

D.EQ(r'\begin{gathered}\text{natural: } x(t)=x_0\,e^{-t/\tau} \\ \text{step: } x(t)=x_f+(x_0-x_f)\,e^{-t/\tau}\end{gathered}', cites=D.cite('W2', 5))

# ---- Example 9 (charging through a voltage source)
SRC_CH = r'''
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$4\,\mathrm{k\Omega}$"
C1 6,3 -> 6,0 "$50\,\mu\mathrm{F}$" v="$v$" i="$i$"
wire 6,0 -> 0,0
ground 0,0
'''
D.EX('Charging a capacitor from a voltage source',
     J(r'The $50\,\mu\mathrm{F}$ capacitor holds $2\,\mathrm{V}$ (left from earlier) while the switch is open. At $t=0$ the switch closes, connecting the $12\,\mathrm{V}$ source through $4\,\mathrm{k\Omega}$.',
       r'1. Write the ODE for $v(t)$, $t\ge 0$.', r'2. Find $\tau$ and $v(t)$.', r'3. Find the current $i(t)$.', r'4. When does $v$ reach $10\,\mathrm{V}$?',
       '', S_(SRC_CH)),
     [S(r'KVL around the loop for $t\ge0$: the source voltage equals the resistor voltage $Ri$ plus the capacitor voltage $v$, and the series current is the capacitor current $i=C\dfrac{dv}{dt}$.',
        r'\begin{gathered}12=4000\,i+v \\ i=50\times10^{-6}\dfrac{dv}{dt}\end{gathered}'),
      S(r'Substitute the capacitor law; $4000\times 50\times10^{-6}=0.2$. Divide by $0.2$ so the derivative stands alone.',
        r'0.2\dfrac{dv}{dt}+v=12\;\Rightarrow\;\dfrac{dv}{dt}+5v=60'),
      S(r'Read off the pieces: $\tau=RC=0.2\,\mathrm{s}$; the final value (capacitor open, no current, no voltage across $R$) is the full source; the initial value is the stored 2 V.',
        r'\tau=0.2\,\mathrm{s},\quad V_f=12\,\mathrm{V},\quad V_0=2\,\mathrm{V}'),
      S(r'Plug into the step-response formula; $1/\tau=5\ \mathrm{s^{-1}}$.', r'v(t)=12+(2-12)e^{-5t}=12-10e^{-5t}\ \mathrm{V}'),
      S(r'Current from the capacitor law, differentiating with the chain rule. Check: at $t=0^+$ the resistor sees $12-2=10\,\mathrm{V}$, and $10/4000=2.5\,\mathrm{mA}$, which matches.',
        r'i=C\dfrac{dv}{dt}=50\times10^{-6}\cdot 50e^{-5t}=2.5e^{-5t}\ \mathrm{mA}'),
      S(r'Part 4: set $v=10$, isolate the exponential, then take $\ln$ of both sides (ln undoes exp).',
        r'12-10e^{-5t}=10\;\Rightarrow\;e^{-5t}=0.2\;\Rightarrow\;-5t=\ln 0.2'),
      S(r'Solve for $t$, using $\ln 0.2=-\ln 5$.', r't=\dfrac{\ln 5}{5}\approx 0.322\ \mathrm{s}')],
     r'1. $\dfrac{dv}{dt}+5v=60$. 2. $\tau=0.2\,\mathrm{s}$, $v(t)=12-10e^{-5t}\,\mathrm{V}$. 3. $i(t)=2.5e^{-5t}\,\mathrm{mA}$. 4. $t=\tfrac{\ln 5}{5}\approx 0.322\,\mathrm{s}$.')
v9 = 12 - 10 * sp.exp(-5 * t)
ode1_solution_ok(v9, -5, 60, 2)
Cv, Rv = sp.Rational(50, 10**6), 4000
check(zero(12 - Rv * Cv * sp.diff(v9, t) - v9), 'ex9 KVL')
check(zero(Cv * sp.diff(v9, t) - sp.Rational(25, 10000) * sp.exp(-5 * t)), 'ex9 current')
close(sp.nsolve(v9 - 10, t, 0.3), 0.3219)
close(sp.log(5) / 5, 0.3219)
D.CHART(r'Example 9: $v(t)=12-10e^{-5t}$. It starts at the stored 2 V (no jump), rises fastest at first, reaches about $2+0.63\cdot10\approx 8.3\,\mathrm{V}$ at $t=\tau=0.2\,\mathrm{s}$, and is essentially at 12 V by $5\tau=1\,\mathrm{s}$.',
        order=1, a=-5.0, forcing=60.0, y0=2.0, duration=1.0)

# ---- Example 10 (two resistors: tau uses the parallel resistance)
SRC_TWO = r'''
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
S1 0,3 -> 2,3 "$t=0$" action=close
R1 2,3 -> 5,3 "$6\,\mathrm{k\Omega}$"
R2 5,3 -> 5,0 "$3\,\mathrm{k\Omega}$"
wire 5,3 -> 8,3
C1 8,3 -> 8,0 "$5\,\mu\mathrm{F}$" v="$v$" i="$i$"
wire 8,0 -> 0,0
label 5,3 "$a$" above
ground 0,0
'''
D.EX('Two resistors: which R goes in the time constant?',
     J(r'The capacitor is uncharged ($v(0^-)=0$) and the switch closes at $t=0$. Find the ODE, $\tau$, $v(t)$ and the capacitor current at $t=0^+$.',
       '', S_(SRC_TWO)),
     [S(r'Initial value: the capacitor was uncharged and its voltage cannot jump.', r'v(0^+)=v(0^-)=0'),
      S(r'For $t\ge0$ write KCL at node $a$ (the node voltage is $v$, measured from ground): current leaving through $R_1$ back toward the source, plus through $R_2$, plus into $C$, adds to zero.',
        r'\dfrac{v-12}{6000}+\dfrac{v}{3000}+5\times10^{-6}\dfrac{dv}{dt}=0'),
      S(r'Multiply every term by 6000 to clear fractions ($6000\times5\times10^{-6}=0.03$), collect $v$ terms, then divide by 0.03.',
        r'0.03\dfrac{dv}{dt}+3v=12\;\Rightarrow\;\dfrac{dv}{dt}+100v=400'),
      S(r'Read off $\tau=1/100\,\mathrm{s}=10\,\mathrm{ms}$. Notice this equals $(R_1\parallel R_2)\,C$: the capacitor sees $6\,\mathrm{k\Omega}$ and $3\,\mathrm{k\Omega}$ in parallel, $\dfrac{6\cdot3}{6+3}=2\,\mathrm{k\Omega}$, and $2000\times5\times10^{-6}=0.01$.',
        r'\tau=(R_1\parallel R_2)\,C=10\,\mathrm{ms}'),
      S(r'Final value: set $\dfrac{dv}{dt}=0$, or use the capacitor-open voltage divider $12\cdot\dfrac{3}{6+3}$.', r'V_f=\dfrac{400}{100}=4\,\mathrm{V}'),
      S(r'Step-response formula with $V_0=0$, $V_f=4$, $1/\tau=100$.', r'v(t)=4-4e^{-100t}\ \mathrm{V}'),
      S(r'Capacitor current: $i=C\dfrac{dv}{dt}=5\times10^{-6}\cdot400e^{-100t}$; at $t=0^+$ it is 2 mA. Check: with $v=0$, $R_2$ carries nothing and all of $12/6000=2\,\mathrm{mA}$ flows into the capacitor.',
        r'i(0^+)=2\,\mathrm{mA}')],
     r'$\dfrac{dv}{dt}+100v=400$; $\tau=10\,\mathrm{ms}$; $v(t)=4-4e^{-100t}\,\mathrm{V}$; $i(0^+)=2\,\mathrm{mA}$ (it was 0 before the switch closed).')
v10 = 4 - 4 * sp.exp(-100 * t)
C10 = sp.Rational(5, 10**6)
check(zero((v10 - 12) / 6000 + v10 / 3000 + C10 * sp.diff(v10, t)), 'ex10 KCL')
ode1_solution_ok(v10, -100, 400, 0)
check(zero(C10 * sp.diff(v10, t).subs(t, 0) - sp.Rational(2, 1000)), 'ex10 i0')
check(zero(sp.Rational(6000 * 3000, 9000) * C10 - sp.Rational(1, 100)), 'ex10 tau')

D.CO('warning', J(
    '**Common mistakes**',
    '',
    r'- Assuming the capacitor *current* (or inductor *voltage*) is continuous. Only $v_C$ and $i_L$ carry over from $0^-$ to $0^+$; in Example 10 the capacitor current jumps from 0 to 2 mA.',
    r'- Using the wrong resistance in $\tau$. Use the resistance seen by $C$ or $L$ after the switch moves, with sources switched off (Example 10: $R_1\parallel R_2$, not $R_1$).',
    r'- Mixing up $\tau=RC$ (capacitor) and $\tau=L/R$ (inductor). A bigger $R$ makes an RC circuit slower but an RL circuit faster.',
    r'- Writing $e^{-t\tau}$ instead of $e^{-t/\tau}$, or forgetting unit prefixes: $\mu\mathrm{F}=10^{-6}\,\mathrm{F}$, $\mathrm{k\Omega}=10^{3}\,\Omega$, $\mathrm{mH}=10^{-3}\,\mathrm{H}$.'))

# ---- Try its topic 2
SRC_T7 = r'''
C1 0,3 -> 0,0 "$47\,\mu\mathrm{F}$" v="$v$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$10\,\mathrm{k\Omega}$"
wire 3,0 -> 0,0
ground 0,0
'''
D.PR('Time constant in numbers',
     J(r'The capacitor starts at $v(0)=9\,\mathrm{V}$ and discharges through the resistor. Find $\tau$, $v(t)$, the voltage after one time constant, and roughly how long until it is fully discharged.',
       '', S_(SRC_T7)),
     [S(r'Compute the time constant, converting units: $10\,\mathrm{k\Omega}=10^4\,\Omega$ and $47\,\mu\mathrm{F}=47\times10^{-6}\,\mathrm{F}$.', r'\tau=RC=10^4\cdot47\times10^{-6}=0.47\,\mathrm{s}'),
      S(r'There is no source, so this is a natural response: initial value times the decaying exponential.', r'v(t)=9e^{-t/0.47}\ \mathrm{V}'),
      S(r'After one time constant the exponent is $-1$, and $e^{-1}\approx0.368$.', r'v(\tau)=9e^{-1}\approx 3.31\,\mathrm{V}'),
      S(r'After $5\tau$ less than 1% remains, which we treat as fully discharged.', r'5\tau=2.35\,\mathrm{s},\quad v(5\tau)=9e^{-5}\approx 0.06\,\mathrm{V}')],
     r'$\tau=0.47\,\mathrm{s}$; $v(t)=9e^{-t/0.47}\,\mathrm{V}$; $v(\tau)\approx3.31\,\mathrm{V}$; about $5\tau\approx2.35\,\mathrm{s}$ to discharge.')
close(10**4 * 47e-6, 0.47)
close(9 * sp.exp(-1), 3.311)
close(9 * sp.exp(-5), 0.0606)

SRC_T8 = r'''
I1 0,0 -> 0,3 "$2\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$1\,\mathrm{k\Omega}$" i="$v/R$"
S1 3,3 -> 6,3 "$t=0$" action=close
C1 6,3 -> 6,0 "$C$" v="$v$" i="$i$"
wire 6,0 -> 0,0
ground 0,0
'''
D.PR('Capacitor current at 0⁻ and 0⁺ (Pre-tutorial 2)',
     J(r'In the step-response circuit below, $V_0=v(0^-)=0$, $I_s=2\,\mathrm{A}$ and $R=1\,\mathrm{k\Omega}$; the switch closes at $t=0$. '
       r'What is the capacitor current $i$ at $t=0^-$ (switch open) and at $t=0^+$ (switch closed)? Is the capacitor current discontinuous at $t=0$, unlike the capacitor voltage?',
       '', S_(SRC_T8)),
     [S(r'At $t=0^-$ the switch is open, so the capacitor branch is broken: no current can flow in it.', r'i(0^-)=0'),
      S(r'The capacitor voltage cannot jump, so just after closing it is still zero.', r'v(0^+)=v(0^-)=V_0=0'),
      S(r'With $v=0$ the resistor current $v/R$ is zero. KCL at the top node then sends the entire source current into the capacitor.',
        r'i(0^+)=I_s-\dfrac{v(0^+)}{R}=2-0=2\,\mathrm{A}'),
      S(r'Cross-check with the formula: $v=RI_s(1-e^{-t/RC})$, so $i=C\dfrac{dv}{dt}=C\cdot RI_s\cdot\dfrac{1}{RC}e^{-t/RC}=I_se^{-t/RC}$, which is $2\,\mathrm{A}$ at $t=0^+$ for any $C$.',
        r'i(t)=I_s\,e^{-t/RC}\;\Rightarrow\;i(0^+)=2\,\mathrm{A}'),
      S(r'So the current jumps from 0 to 2 A while the voltage stays at 0: the capacitor current is discontinuous, the capacitor voltage is not.', r'\begin{gathered}i:\ 0\to 2\,\mathrm{A} \\ v:\ 0\to 0\end{gathered}')],
     r'$i(0^-)=0$, $i(0^+)=2\,\mathrm{A}$. Yes, the capacitor current is discontinuous at $t=0$ (it jumps by 2 A), while $v$ stays continuous at 0.',
     diff='intermediate', cites=D.cite('T2', 1))
Cs = sp.symbols('C', positive=True)
vt8 = 1000 * 2 * (1 - sp.exp(-t / (1000 * Cs)))
it8 = Cs * sp.diff(vt8, t)
check(zero(it8.subs(t, 0) - 2), 'pretut i0+')
check(zero(Cs * sp.diff(vt8, t) + vt8 / 1000 - 2), 'pretut KCL')

SRC_T9 = r'''
V1 0,3 -> 0,0 "$24\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$6\,\Omega$"
L1 6,3 -> 6,0 "$0.3\,\mathrm{H}$" i="$i$" v="$v_L$"
wire 6,0 -> 0,0
ground 0,0
'''
D.PR('RL step response',
     J(r'The inductor carries no current before the switch closes at $t=0$. Find the ODE for $i(t)$, the time constant, $i(t)$ and the inductor voltage $v_L(t)$.',
       '', S_(SRC_T9)),
     [S(r'Initial value: the inductor current cannot jump, so it starts at zero.', r'i(0^+)=i(0^-)=0'),
      S(r'KVL around the loop for $t\ge0$: the source equals the resistor voltage plus the inductor voltage $L\dfrac{di}{dt}$.', r'24=6i+0.3\dfrac{di}{dt}'),
      S(r'Divide by $0.3$ so the derivative stands alone.', r'\dfrac{di}{dt}+20i=80'),
      S(r'Time constant $\tau=L/R$; final value from DC steady state (inductor is a short, so $i=24/6$).', r'\begin{gathered}\tau=\dfrac{0.3}{6}=0.05\,\mathrm{s} \\ I_f=4\,\mathrm{A}\end{gathered}'),
      S(r'Step-response formula with $I_0=0$, $I_f=4$, $1/\tau=20$.', r'i(t)=4-4e^{-20t}\ \mathrm{A}'),
      S(r'Inductor voltage from $v=L\dfrac{di}{dt}$ (chain rule). It jumps to the full 24 V at $0^+$ and decays to 0, consistent with the inductor becoming a short.',
        r'v_L=0.3\cdot80e^{-20t}=24e^{-20t}\ \mathrm{V}')],
     r'$\dfrac{di}{dt}+20i=80$; $\tau=0.05\,\mathrm{s}$; $i(t)=4-4e^{-20t}\,\mathrm{A}$; $v_L(t)=24e^{-20t}\,\mathrm{V}$.', diff='intermediate')
i9 = 4 - 4 * sp.exp(-20 * t)
check(zero(24 - 6 * i9 - sp.Rational(3, 10) * sp.diff(i9, t)), 'T9 KVL')
ode1_solution_ok(i9, -20, 80, 0)
check(zero(sp.Rational(3, 10) * sp.diff(i9, t) - 24 * sp.exp(-20 * t)), 'T9 vL')

SRC_T10 = r'''
V1 0,3 -> 0,0 "$V_s$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$R$"
C1 6,3 -> 6,0 "$C$" v="$v$" i="$i$"
wire 6,0 -> 0,0
ground 0,0
'''
D.PR('Write the ODE and classify it',
     J(r'For the series RC circuit below (switch closes at $t=0$), write the ODE for the capacitor voltage $v(t)$, classify it, and state its final value.',
       '', S_(SRC_T10)),
     [S(r'KVL around the loop for $t\ge0$: source voltage equals resistor voltage plus capacitor voltage.', r'V_s=Ri+v'),
      S(r'The same current flows through the capacitor, so substitute $i=C\dfrac{dv}{dt}$.', r'RC\dfrac{dv}{dt}+v=V_s'),
      S(r'Divide by $RC$ to get standard form; $\tau=RC$.', r'\dfrac{dv}{dt}+\dfrac{v}{RC}=\dfrac{V_s}{RC}'),
      S(r'Classify: first derivative only (first order); $v$ and $\dfrac{dv}{dt}$ appear linearly; constant forcing $V_s/RC\neq0$ (nonhomogeneous); $R$, $C$ constant (constant-coefficient); no explicit $t$ (autonomous).', r''),
      S(r'Final value: set $\dfrac{dv}{dt}=0$ (capacitor open, no current, no voltage across $R$).', r'V_f=V_s')],
     r'$\dfrac{dv}{dt}+\dfrac{v}{RC}=\dfrac{V_s}{RC}$: first-order, linear, nonhomogeneous, constant-coefficient, autonomous. Final value $V_s$.')
vF = sp.Function('v')
cls_is(vF(t).diff(t) + vF(t) / (R * C) - Vs / (R * C), (1, True, False, True, True), f=vF)

D.PR('How long does it take?',
     J(r'A capacitor voltage follows the natural response $v(t)=10e^{-t/\tau}\,\mathrm{V}$ with $\tau=2\,\mathrm{ms}$.',
       r'1. When does it reach $1\,\mathrm{V}$?', r'2. When does it reach half its starting value?'),
     [S(r'Set $v=1$ and divide by 10 to isolate the exponential.', r'e^{-t/\tau}=0.1'),
      S(r'Take $\ln$ of both sides ($\ln e^{x}=x$), then use $\ln0.1=-\ln10$.', r'-\dfrac{t}{\tau}=\ln 0.1=-\ln 10'),
      S(r'Multiply by $-\tau$.', r't=\tau\ln10=2\,\mathrm{ms}\times2.303\approx4.61\,\mathrm{ms}'),
      S(r'Part 2: the same steps with the fraction $0.5$; $\ln 2\approx0.693$. This "half-life" is about $0.69\tau$ for any first-order circuit.',
        r'e^{-t/\tau}=0.5\;\Rightarrow\;t=\tau\ln2\approx1.39\,\mathrm{ms}')],
     r'1. $t=\tau\ln10\approx4.61\,\mathrm{ms}$. 2. $t=\tau\ln2\approx1.39\,\mathrm{ms}$.', diff='intermediate')
close(2 * sp.log(10), 4.605)
close(2 * sp.log(2), 1.386)

SRC_T12 = r'''
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
S1 3,3 -> 5,3 "$t=0$" action=open
L1 5,3 -> 5,0 "$0.4\,\mathrm{H}$" i="$i_L$"
wire 5,3 -> 8,3
R2 8,3 -> 8,0 "$6\,\Omega$" v="$v_a$"
wire 8,0 -> 0,0
label 5,3 "$a$" above
ground 0,0
'''
D.PR('Switch opens on an inductor',
     J(r'The switch has been closed for a long time and opens at $t=0$. Find $i_L(0^-)$, $i_L(t)$ for $t\ge0$, and the voltage $v_a(t)$ across the $6\,\Omega$ resistor. Does $v_a$ jump?',
       '', S_(SRC_T12)),
     [S(r'Before $t=0$ (DC steady state) the inductor is a short from $a$ to ground. That short also sits across the $6\,\Omega$ resistor, so $v_a=0$ and the $6\,\Omega$ carries nothing; all the current goes through $2\,\Omega$ and the inductor.',
        r'\begin{gathered}i_L(0^-)=\dfrac{12}{2}=6\,\mathrm{A} \\ v_a(0^-)=0\end{gathered}'),
      S(r'The inductor current cannot jump.', r'i_L(0^+)=6\,\mathrm{A}'),
      S(r'For $t\ge0$ the source branch is cut off; only the loop inductor–$6\,\Omega$ remains. The inductor current flows down through $L$ and back up through $R_2$, so the downward current in $R_2$ is $-i_L$ and $v_a=-6\,i_L$. The inductor voltage is the same $v_a$.',
        r'v_a=L\dfrac{di_L}{dt}=-6\,i_L'),
      S(r'Rearrange into standard form; $\tau=L/R=0.4/6=1/15\,\mathrm{s}$.', r'\dfrac{di_L}{dt}+15\,i_L=0'),
      S(r'Natural response from 6 A.', r'i_L(t)=6e^{-15t}\ \mathrm{A}'),
      S(r'Then $v_a=-6i_L$. It jumps from 0 at $0^-$ to $-36\,\mathrm{V}$ at $0^+$; that is allowed, because only $i_L$ has to be continuous.',
        r'v_a(t)=-36e^{-15t}\ \mathrm{V}')],
     r'$i_L(0^-)=6\,\mathrm{A}$; $i_L(t)=6e^{-15t}\,\mathrm{A}$; $v_a(t)=-36e^{-15t}\,\mathrm{V}$. Yes, $v_a$ jumps from $0$ to $-36\,\mathrm{V}$.', diff='advanced')
iL12 = 6 * sp.exp(-15 * t)
check(zero(sp.Rational(2, 5) * sp.diff(iL12, t) - (-6 * iL12)), 'T12 KVL')
check(zero(-6 * iL12 + 36 * sp.exp(-15 * t)), 'T12 va')

# ====================================================================== MIXED PRACTICE
D.H('Mixed practice (exam style)')
D.P('Mixed topics, like the midterm. Try each one before opening the solution.')

D.PR('Classify, check, solve',
     J(r'Consider $\dfrac{dy}{dt}+4y=8$.', r'1. Classify it.', r'2. Show that $y=2+Ke^{-4t}$ is a solution for every constant $K$.',
       r'3. Solve the IVP with $y(0)=0$.', r'4. What does $y$ approach as $t\to\infty$?'),
     [S(r'Classify: first order; linear ($y$ and $\dfrac{dy}{dt}$ to the first power); forcing $8\neq0$ so nonhomogeneous; coefficients $1$, $4$ constant; no explicit $t$, so autonomous.', r''),
      S(r'Differentiate the proposed solution (constant rule and chain rule) and substitute; the $K$ terms cancel.',
        r'-4Ke^{-4t}+4(2+Ke^{-4t})=8\ \checkmark'),
      S(r'Initial condition: at $t=0$, $2+K=0$.', r'K=-2\;\Rightarrow\;y(t)=2-2e^{-4t}'),
      S(r'As $t\to\infty$, $e^{-4t}\to0$.', r'y\to 2')],
     r'1. First-order, linear, nonhomogeneous, constant-coefficient, autonomous. 2. Shown. 3. $y=2-2e^{-4t}$. 4. $2$.', label='Practice 1')
cls_is(y(t).diff(t) + 4 * y(t) - 8, (1, True, False, True, True))
check(zero(sp.diff(2 + K * sp.exp(-4 * t), t) + 4 * (2 + K * sp.exp(-4 * t)) - 8), 'P1 family')
ode1_solution_ok(2 - 2 * sp.exp(-4 * t), -4, 8, 0)

SRC_P2 = r'''
V1 0,3 -> 0,0 "$10\,\mathrm{V}$"
S1 0,3 -> 2,3 "$t=0$" action=open
R1 2,3 -> 5,3 "$2\,\mathrm{k\Omega}$"
R2 5,3 -> 5,0 "$3\,\mathrm{k\Omega}$"
wire 5,3 -> 8,3
C1 8,3 -> 8,0 "$10\,\mu\mathrm{F}$" v="$v$" i="$i$"
wire 8,0 -> 0,0
ground 0,0
'''
D.PR('Switch opens on a charged capacitor',
     J(r'The switch has been closed for a long time and opens at $t=0$.', r'1. Find $v(0^-)$.', r'2. Write the ODE for $v(t)$, $t\ge0$, and find $\tau$.',
       r'3. Find $v(t)$.', r'4. Find the capacitor current $i$ at $t=0^-$ and $t=0^+$.', '', S_(SRC_P2)),
     [S(r'Before $t=0$, DC steady state: the capacitor is open, so the source, $2\,\mathrm{k\Omega}$ and $3\,\mathrm{k\Omega}$ form a voltage divider, and $v$ is the voltage across $3\,\mathrm{k\Omega}$.',
        r'v(0^-)=10\cdot\dfrac{3}{2+3}=6\,\mathrm{V}'),
      S(r'After the switch opens, $2\,\mathrm{k\Omega}$ hangs from an open end and carries nothing; the capacitor discharges through $3\,\mathrm{k\Omega}$ only. KCL at the top node:',
        r'10^{-5}\dfrac{dv}{dt}+\dfrac{v}{3000}=0\;\Rightarrow\;\dfrac{dv}{dt}+\dfrac{v}{0.03}=0'),
      S(r'So $\tau=R_2C=3000\times10^{-5}=0.03\,\mathrm{s}=30\,\mathrm{ms}$, and the voltage starts at 6 V (no jump).', r'v(t)=6e^{-t/0.03}\ \mathrm{V}'),
      S(r'At $0^-$ the capacitor is in DC steady state: $i(0^-)=0$. At $0^+$, $i=C\dfrac{dv}{dt}=-\dfrac{v}{R_2}$ from the KCL equation.',
        r'i(0^+)=-\dfrac{6}{3000}=-2\,\mathrm{mA}'),
      S(r'The minus sign means current flows up out of the $+$ terminal: the capacitor is discharging into $3\,\mathrm{k\Omega}$.', r'')],
     r'1. $6\,\mathrm{V}$. 2. $\dfrac{dv}{dt}+\dfrac{v}{0.03}=0$, $\tau=30\,\mathrm{ms}$. 3. $v(t)=6e^{-t/0.03}\,\mathrm{V}$. 4. $i(0^-)=0$, $i(0^+)=-2\,\mathrm{mA}$.',
     diff='intermediate', label='Practice 2')
vP2 = 6 * sp.exp(-t / sp.Rational(3, 100))
check(zero(sp.Rational(1, 10**5) * sp.diff(vP2, t) + vP2 / 3000), 'P2 KCL')
check(zero(sp.Rational(1, 10**5) * sp.diff(vP2, t).subs(t, 0) + sp.Rational(2, 1000)), 'P2 i0+')

D.PR('Read a response backwards',
     J(r'The capacitor voltage in a first-order circuit is $v(t)=8-6e^{-250t}\,\mathrm{V}$ for $t\ge0$.',
       r'1. Find the initial value $V_0$, the final value $V_f$ and the time constant $\tau$.', r'2. Which ODE does $v$ satisfy?',
       r'3. If $C=4\,\mu\mathrm{F}$, find the capacitor current $i(t)$.'),
     [S(r'Match with $V_f+(V_0-V_f)e^{-t/\tau}$: the constant is $V_f$, setting $t=0$ gives $V_0$, and the exponent gives $1/\tau=250$.',
        r'V_f=8\,\mathrm{V},\quad V_0=8-6=2\,\mathrm{V},\quad \tau=4\,\mathrm{ms}'),
      S(r'The standard form is $\dfrac{dv}{dt}+\dfrac{v}{\tau}=\dfrac{V_f}{\tau}$; with $1/\tau=250$ the right side is $250\cdot8=2000$.', r'\dfrac{dv}{dt}+250v=2000'),
      S(r'Check by substitution: $\dfrac{dv}{dt}=1500e^{-250t}$ (chain rule) and $250v=2000-1500e^{-250t}$; they add to 2000.', r'1500e^{-250t}+2000-1500e^{-250t}=2000\ \checkmark'),
      S(r'Current from $i=C\dfrac{dv}{dt}$ with $C=4\times10^{-6}$.', r'i=4\times10^{-6}\cdot1500e^{-250t}=6e^{-250t}\ \mathrm{mA}')],
     r'1. $V_0=2\,\mathrm{V}$, $V_f=8\,\mathrm{V}$, $\tau=4\,\mathrm{ms}$. 2. $\dfrac{dv}{dt}+250v=2000$. 3. $i(t)=6e^{-250t}\,\mathrm{mA}$.',
     diff='intermediate', label='Practice 3')
vP3 = 8 - 6 * sp.exp(-250 * t)
ode1_solution_ok(vP3, -250, 2000, 2)
check(zero(sp.Rational(4, 10**6) * sp.diff(vP3, t) - sp.Rational(6, 1000) * sp.exp(-250 * t)), 'P3 i')

D.PR('Scaling fails for a nonlinear equation',
     J(r'1. Show that $y=\dfrac{1}{1-t}$ solves the IVP $\dfrac{dy}{dt}=y^2$, $y(0)=1$ (for $t<1$).',
       r'2. Is $y=\dfrac{2}{1-t}$ also a solution of $\dfrac{dy}{dt}=y^2$? What does this say about the equation?'),
     [S(r'Write $y=(1-t)^{-1}$ and differentiate with the chain rule: outside power rule gives $-(1-t)^{-2}$, inside $\dfrac{d}{dt}(1-t)=-1$.',
        r'\dfrac{dy}{dt}=-(1-t)^{-2}\cdot(-1)=\dfrac{1}{(1-t)^2}'),
      S(r'The right side is $y^2=\dfrac{1}{(1-t)^2}$, the same; and $y(0)=\dfrac{1}{1}=1$.', r'\dfrac{dy}{dt}=y^2\ \checkmark,\quad y(0)=1\ \checkmark'),
      S(r'For $y=\dfrac{2}{1-t}$ the derivative doubles but $y^2$ quadruples, so the two sides differ.', r'\dfrac{dy}{dt}=\dfrac{2}{(1-t)^2}\neq\dfrac{4}{(1-t)^2}=y^2'),
      S(r'For a linear homogeneous equation, $2\times$(a solution) is always a solution. Here it is not, which confirms that $\dfrac{dy}{dt}=y^2$ is nonlinear (the $y^2$ term).', r'')],
     r'1. Yes. 2. No: $\dfrac{dy}{dt}=\dfrac{2}{(1-t)^2}$ but $y^2=\dfrac{4}{(1-t)^2}$. Multiplying a solution by a constant does not give a solution, because the equation is nonlinear.',
     diff='intermediate', label='Practice 4')
y4 = 1 / (1 - t)
check(zero(sp.diff(y4, t) - y4**2) and y4.subs(t, 0) == 1, 'P4 a')
check(not zero(sp.diff(2 * y4, t) - (2 * y4)**2), 'P4 b')

SRC_P5 = r'''
C1 0,3 -> 0,0 "$C$" v="$v$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$1\,\mathrm{k\Omega}$"
wire 3,0 -> 0,0
ground 0,0
'''
D.PR('Find the capacitance from a measurement',
     J(r'A charged capacitor discharges through $1\,\mathrm{k\Omega}$ (below). An oscilloscope shows $v$ falling from $20\,\mathrm{V}$ at $t=0$ to $5\,\mathrm{V}$ at $t=3\,\mathrm{ms}$.',
       r'1. Find $\tau$ and $C$.', r'2. Predict $v$ at $t=6\,\mathrm{ms}$.', '', S_(SRC_P5)),
     [S(r'Natural response: $v=20e^{-t/\tau}$. Put in the measurement and divide by 20.', r'20e^{-0.003/\tau}=5\;\Rightarrow\;e^{-0.003/\tau}=\tfrac14'),
      S(r'Take $\ln$ of both sides, using $\ln\tfrac14=-\ln4$.', r'-\dfrac{0.003}{\tau}=-\ln4\;\Rightarrow\;\tau=\dfrac{0.003}{\ln4}\approx2.16\,\mathrm{ms}'),
      S(r'Since $\tau=RC$, divide by $R=1000\,\Omega$.', r'C=\dfrac{\tau}{R}\approx2.16\,\mu\mathrm{F}'),
      S(r'Part 2: $6\,\mathrm{ms}$ is twice $3\,\mathrm{ms}$, so the factor $\tfrac14$ applies twice: $e^{-0.006/\tau}=\left(e^{-0.003/\tau}\right)^2$.', r'v(6\,\mathrm{ms})=20\cdot\left(\tfrac14\right)^2=1.25\,\mathrm{V}')],
     r'1. $\tau=\dfrac{3\,\mathrm{ms}}{\ln4}\approx2.16\,\mathrm{ms}$, $C\approx2.16\,\mu\mathrm{F}$. 2. $1.25\,\mathrm{V}$.', diff='intermediate', label='Practice 5')
tau5 = sp.Rational(3, 1000) / sp.log(4)
close(tau5, 0.0021640)
close(20 * sp.exp(-sp.Rational(6, 1000) / tau5), 1.25)

six2 = [
    (r'\dfrac{d^2i}{dt^2}+\dfrac{R}{L}\dfrac{di}{dt}+\dfrac{i}{LC}=0', 'series RLC, natural response'),
    (r'C\dfrac{dv}{dt}+I_0\big(e^{v/V_T}-1\big)=0', 'a capacitor discharging through a diode; $I_0$, $V_T$ constants'),
    (r'C\dfrac{dv}{dt}+\dfrac{v}{R}=I_0\cos(\omega t)', r'parallel RC driven by an AC current source; $\omega$ is a constant'),
    (r'L\dfrac{di}{dt}+R_0(1+t)\,i=0', 'an inductor discharging into a resistor that heats up, $R=R_0(1+t)$'),
]
I0, VT, w, R0 = sp.symbols('I_0 V_T omega R_0', positive=True)
cls_is(iF(t).diff(t, 2) + R / L * iF(t).diff(t) + iF(t) / (L * C), (2, True, True, True, True), f=iF)
cls_is(C * vF(t).diff(t) + I0 * (sp.exp(vF(t) / VT) - 1), (1, False, None, None, True), f=vF)
cls_is(C * vF(t).diff(t) + vF(t) / R - I0 * sp.cos(w * t), (1, True, False, True, False), f=vF)
cls_is(L * iF(t).diff(t) + R0 * (1 + t) * iF(t), (1, True, True, False, False), f=iF)
D.PR('Classify circuit equations',
     J('Classify each circuit equation (order; linear or not; homogeneous; constant-coefficient; autonomous).', '',
       *[f'{k}. ${s}$ ({d})' for k, (s, d) in enumerate(six2, 1)]),
     [S(r'Equation 1: second order; $i$, $\dfrac{di}{dt}$, $\dfrac{d^2i}{dt^2}$ appear linearly with constant coefficients; right side 0; no explicit $t$.', six2[0][0]),
      S(r'Equation 2: first order; the unknown $v$ sits inside an exponential, $e^{v/V_T}$, so it is nonlinear; no explicit $t$, so autonomous.', six2[1][0]),
      S(r'Equation 3: first order, linear, constant coefficients $C$ and $1/R$; the source $I_0\cos(\omega t)$ is nonzero forcing that depends on $t$.', six2[2][0]),
      S(r'Equation 4: first order, linear (the coefficient $R_0(1+t)$ depends on $t$ only), homogeneous; that coefficient changes with time, so not constant-coefficient and not autonomous.', six2[3][0])],
     J('1. Second-order, linear, homogeneous, constant-coefficient, autonomous.', '2. First-order, nonlinear, autonomous.',
       '3. First-order, linear, nonhomogeneous, constant-coefficient, not autonomous.', '4. First-order, linear, homogeneous, variable-coefficient, not autonomous.'),
     label='Practice 6')

SRC_P7 = r'''
I1 0,0 -> 0,3 "$3\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$10\,\Omega$" v="$v$"
S1 3,3 -> 6,3 "$t=0$" action=close
R2 6,3 -> 9,3 "$5\,\Omega$"
L1 9,3 -> 9,0 "$0.25\,\mathrm{H}$" i="$i$"
wire 9,0 -> 0,0
ground 0,0
'''
D.PR('RL circuit with a current source (multi-part)',
     J(r'The switch has been open for a long time and closes at $t=0$.', r'1. Find $i(0^+)$ and $v(0^+)$.',
       r'2. Write the ODE for the inductor current $i(t)$ and find $\tau$.', r'3. Find $i(t)$ and the inductor voltage $v_L(t)$.',
       r'4. Find $v(t)$ and check it at $t=0^+$ and $t\to\infty$.', '', S_(SRC_P7)),
     [S(r'Before the switch closes the inductor branch is cut off, so $i(0^-)=0$; the inductor current cannot jump. At $0^+$ all 3 A therefore still goes through $10\,\Omega$.',
        r'\begin{gathered}i(0^+)=0 \\ v(0^+)=10\cdot3=30\,\mathrm{V}\end{gathered}'),
      S(r'For $t\ge0$, KCL at the top node: the source current splits between $10\,\Omega$ and the $5\,\Omega$–inductor branch. The node voltage $v$ is also the voltage across that branch, $5i+0.25\dfrac{di}{dt}$ (KVL).',
        r'\begin{gathered}3=\dfrac{v}{10}+i \\ v=5i+0.25\dfrac{di}{dt}\end{gathered}'),
      S(r'Substitute $v$ into the KCL equation and multiply by 10.', r'30=5i+0.25\dfrac{di}{dt}+10i\;\Rightarrow\;0.25\dfrac{di}{dt}+15i=30'),
      S(r'Divide by 0.25. The time constant is $L/R$ with $R=10+5=15\,\Omega$ (the resistance the inductor sees with the current source switched off, i.e. opened).',
        r'\begin{gathered}\dfrac{di}{dt}+60i=120 \\ \tau=\dfrac{0.25}{15}=\dfrac{1}{60}\,\mathrm{s}\end{gathered}'),
      S(r'Final value: set $\dfrac{di}{dt}=0$ (inductor short). Current divider check: $3\cdot\dfrac{10}{10+5}=2\,\mathrm{A}$.', r'I_f=\dfrac{120}{60}=2\,\mathrm{A}'),
      S(r'Step-response formula with $I_0=0$, then $v_L=L\dfrac{di}{dt}$ by the chain rule.', r'\begin{gathered}i(t)=2-2e^{-60t}\ \mathrm{A} \\ v_L=0.25\cdot120e^{-60t}=30e^{-60t}\ \mathrm{V}\end{gathered}'),
      S(r'Then $v=10(3-i)$ from KCL. Check: $v(0^+)=30\,\mathrm{V}$ as in part 1, and $v(\infty)=10\,\mathrm{V}$ (1 A through $10\,\Omega$).', r'v(t)=10+20e^{-60t}\ \mathrm{V}')],
     r'1. $i(0^+)=0$, $v(0^+)=30\,\mathrm{V}$. 2. $\dfrac{di}{dt}+60i=120$, $\tau=\tfrac{1}{60}\,\mathrm{s}\approx16.7\,\mathrm{ms}$. 3. $i(t)=2-2e^{-60t}\,\mathrm{A}$, $v_L(t)=30e^{-60t}\,\mathrm{V}$. 4. $v(t)=10+20e^{-60t}\,\mathrm{V}$.',
     diff='advanced', label='Practice 7')
iP7 = 2 - 2 * sp.exp(-60 * t)
vP7 = 10 * (3 - iP7)
check(zero(vP7 - (5 * iP7 + sp.Rational(1, 4) * sp.diff(iP7, t))), 'P7 KVL branch')
ode1_solution_ok(iP7, -60, 120, 0)
check(zero(vP7 - (10 + 20 * sp.exp(-60 * t))), 'P7 v')
check(zero(sp.Rational(1, 4) * sp.diff(iP7, t) - 30 * sp.exp(-60 * t)), 'P7 vL')

# ====================================================================== SUMMARY
D.H('Summary')
D.T(['Problem type', 'How to recognise it', 'What to do'], [
    ['Classify an ODE', r'"Find the order / is it linear, homogeneous, autonomous?"',
     r'Order = highest derivative. Linear: the unknown and its derivatives only to the first power, never multiplied together or inside $\sin$, $e^{(\cdot)}$. Move unknown terms left: $f=0$ means homogeneous. Constant multipliers: constant-coefficient. No bare $t$: autonomous.'],
    ['Check a solution', r'"Show that $y=\dots$ solves \dots"', r'Differentiate, substitute into both sides, simplify; both sides must agree for every $t$.'],
    ['Initial value problem', r'A family with a constant $K$ plus $y(t_0)=y_0$', r'Set $t=t_0$, solve for $K$, write the single solution.'],
    ['Element law', r'Given $v(t)$ of a capacitor or $i(t)$ of an inductor', r'$i=C\dfrac{dv}{dt}$, $v=L\dfrac{di}{dt}$ (passive sign convention; a minus sign means the actual direction is reversed).'],
    ['Initial values at a switch', r'"The switch has been in position a for a long time"', r'DC steady state before: $C$ open, $L$ short. Carry over only $v_C$ and $i_L$ to $0^+$; then use KCL/KVL for anything else at $0^+$.'],
    ['First-order response', r'One $C$ or one $L$ plus resistors and DC sources, after a switch', r'Find $x_0$, $x_f$, $\tau$ ($RC$ or $L/R$ with the resistance the element sees); $x(t)=x_f+(x_0-x_f)e^{-t/\tau}$.'],
    ['Timing question', r'"When does $v$ reach \dots?" or "find $\tau$ from a measurement"', r'Isolate $e^{-t/\tau}$, take $\ln$: $t=\tau\ln\dfrac{1}{p}$ where $p$ is the fraction of the change still left.'],
])
D.T(['Formula', 'Meaning'], [
    [r'$a_n(t)y^{(n)}+\dots+a_0(t)y=f(t)$', 'linear ODE of order $n$; homogeneous if $f\\equiv0$'],
    [r'$v=L\dfrac{di}{dt}$, $\;i=C\dfrac{dv}{dt}$', 'inductor and capacitor laws (passive sign convention)'],
    [r'$\tau=RC$, $\;\tau=L/R$', 'time constant of an RC / RL circuit'],
    [r'$x(t)=x_0e^{-t/\tau}$', 'natural response (no source after the switch)'],
    [r'$x(t)=x_f+(x_0-x_f)e^{-t/\tau}$', 'step response (DC source after the switch)'],
    [r'$e^{-1}\approx0.37$, $\;e^{-5}\approx0.007$', 'after $\\tau$: 63% of the change done; after $5\\tau$: settled'],
])

# ====================================================================== output
import re


def _width(row):
    """Rough count of rendered characters in one display-math row."""
    s = row
    for _ in range(4):  # \dfrac{a}{b} -> the wider of a and b
        s = re.sub(r'\\[dt]?frac\{([^{}]*)\}\{([^{}]*)\}', lambda m: max(m.group(1), m.group(2), key=len), s)
    s = re.sub(r'\\text\{([^{}]*)\}', r'\1', s)
    s = s.replace('\\' + 'qquad', '    ').replace(r'\quad', '  ')
    s = re.sub(r'\\(mathrm|left|right|big|Big|displaystyle|tfrac|,|;|!)', '', s)
    s = re.sub(r'\\[A-Za-z]+', 'x', s)   # any other command is about one glyph
    s = re.sub(r'[{}&^_]', '', s)
    return len(s)


def width_report(limit=44):
    bad = []
    for b in D.B:
        lat = []
        if b['type'] == 'equation':
            lat.append(b['latex'])
        for st in b.get('steps', []):
            lat.append(st['latex'])
        for x in lat:
            body = re.sub(r'\\(begin|end)\{[a-z]+\}', '', x)
            for row in body.split(r'\\'):
                if _width(row) > limit:
                    bad.append((_width(row), row))
    for w_, r_ in bad:
        print(f'  WIDE {w_}: {r_}')
    assert not bad, f'{len(bad)} display rows look wider than the column'


width_report()
print('validating schematics ...')
validate_schematics()
D.save()
