"""ELEC 231 Week 2 v2: classifying ODEs, solutions and IVPs, first-order RC/RL circuits (short, example-led, interactive)."""
import json
import math
import urllib.request

import sympy as sp

from lib231 import Doc, S, flow, steps_fence

D = Doc(week=2, title='Week 2: Classifying ODEs, Initial Value Problems and RC/RL Circuits',
        topic_keys=['ode_classification', 'initial_value_problems', 'first_order_circuits'])
W = lambda *p: D.cite('W2', *p)  # noqa: E731
T2 = D.cite('T2', 1)

# ---------------------------------------------------------------- schematics (checked against the server)
SCHEMATICS = []


def sch(src, *flow_lines):
    """Register a live drawing (current flow on) for the server check; return it as a fence for a prompt."""
    src = flow(src.strip('\n'), *flow_lines)
    SCHEMATICS.append(src)
    return '```schematic\n' + src + '\n```'


def validate_schematics():
    for src in SCHEMATICS:
        req = urllib.request.Request('http://127.0.0.1:8000/api/v1/schematics/check',
                                     data=json.dumps({'source': src}).encode(), method='POST',
                                     headers={'Content-Type': 'application/json'})
        out = json.load(urllib.request.urlopen(req))
        assert not out['errors'], f'schematic errors {out["errors"]} in\n{src}'
        conn = ', '.join(f"{e['name']}:{e['from']}-{e['to']}" for e in out['elements'])
        print('  schematic ok:', conn, ('WARN ' + str(out['warnings'])) if out['warnings'] else '')


# ---------------------------------------------------------------- checks
t = sp.symbols('t', real=True)
tp = sp.symbols('t', positive=True)
y, iF, vF = sp.Function('y'), sp.Function('i'), sp.Function('v')
K, A = sp.symbols('K A')
R, L, C, Is, Vs, V0, I0, VT, w, a_, b_ = sp.symbols('R L C I_s V_s V_0 I_0 V_T omega a b', positive=True)


def zero(e):
    return sp.simplify(sp.expand(e)) == 0


def classify(expr, f=y, var=t):
    """expr == 0 is the ODE. Returns (order, linear, homogeneous, constcoef, autonomous); None = does not apply."""
    n = sp.ode_order(expr, f(var))
    ds = sp.symbols(f'd0:{n + 1}')
    e = sp.expand(expr)
    for k in range(n, 0, -1):
        e = e.subs(f(var).diff(var, k), ds[k])
    e = e.subs(f(var), ds[0])
    linear = all(sp.simplify(sp.diff(e, p, q)) == 0 for p in ds for q in ds)
    hom = cc = None
    if linear:
        hom = sp.simplify(e.subs({d: 0 for d in ds})) == 0
        cc = all(not sp.simplify(sp.diff(e, d)).has(var) for d in ds)
    return n, linear, hom, cc, not e.has(var)


# Topic 1
assert classify(t**3 * y(t).diff(t, 2) + sp.exp(t) * y(t).diff(t) + y(t)) == (2, True, True, False, False)
assert classify(y(t).diff(t) - 3 * y(t)) == (1, True, True, True, True)
assert classify(y(t).diff(t) - 3 * y(t) - 2) == (1, True, False, True, True)
assert classify(y(t).diff(t)**3 + sp.sin(y(t))) == (1, False, None, None, True)
assert classify(iF(t).diff(t, 2) + R / L * iF(t).diff(t) + iF(t) / (L * C), iF) == (2, True, True, True, True)
assert zero(sp.diff(t, t) + t - (1 + t)) and zero(sp.diff(5 * t, t) + 5 * t - (5 + 5 * t))
y1 = 1 / (1 - t)
assert zero(sp.diff(y1, t) - y1**2) and not zero(sp.diff(2 * y1, t) - (2 * y1)**2)
assert classify(C * vF(t).diff(t) + vF(t) / R - I0 * sp.cos(w * t), vF) == (1, True, False, True, False)
assert classify(C * vF(t).diff(t) + I0 * (sp.exp(vF(t) / VT) - 1), vF) == (1, False, None, None, True)
# Topic 2
assert zero(sp.diff(sp.cos(2 * t), t, 2) + 4 * sp.cos(2 * t))
assert zero(sp.diff(sp.sin(t), t, 2) + 4 * sp.sin(t) - 3 * sp.sin(t))
yK = 3 + K * sp.exp(-2 * t)
assert zero(sp.diff(yK, t) - (-2 * yK + 6))
assert sp.solve(yK.subs(t, 0) - 1, K) == [-2]
K1 = sp.solve(yK.subs(t, 1) - 5, K)[0]
assert K1 == 2 * sp.exp(2) and abs(float(K1) - 14.78) < 0.01
assert zero(yK.subs(K, K1) - (3 + 2 * sp.exp(-2 * (t - 1))))
yab = b_ / a_ + K * sp.exp(-a_ * t)
assert zero(sp.diff(yab, t) + a_ * yab - b_) and sp.limit(yab.subs(t, tp), tp, sp.oo) == b_ / a_
# Topic 3
vn = Vs * sp.exp(-t / (R * C))
assert zero(C * sp.diff(vn, t) + vn / R) and vn.subs(t, 0) == Vs
assert abs(math.exp(-1) - 0.37) < 0.005
vs_ = R * Is + (V0 - R * Is) * sp.exp(-t / (R * C))
assert zero(C * sp.diff(vs_, t) + vs_ / R - Is) and zero(vs_.subs(t, 0) - V0)
assert zero(sp.limit(vs_.subs(t, tp), tp, sp.oo) - R * Is)
uF = sp.Function('u')
assert zero(sp.expand(sp.diff(uF(t), t) + (uF(t) + R * Is) / (R * C) - Is / C - (sp.diff(uF(t), t) + uF(t) / (R * C))))
Cpt = sp.symbols('C', positive=True)  # pre-tutorial: V0 = 0, Is = 2 A, R = 1 kOhm, C unknown
vpt = 1000 * 2 * (1 - sp.exp(-t / (1000 * Cpt)))
assert zero(Cpt * sp.diff(vpt, t) + vpt / 1000 - 2) and vpt.subs(t, 0) == 0
assert zero(Cpt * sp.diff(vpt, t) - 2 * sp.exp(-t / (1000 * Cpt))) and zero((Cpt * sp.diff(vpt, t)).subs(t, 0) - 2)
vch = 12 - 10 * sp.exp(-125 * t)  # charging: 12 V, 4 kOhm, 2 uF, v(0) = 2 V
Cch = sp.Rational(2, 10**6)
assert zero(12 - 4000 * Cch * sp.diff(vch, t) - vch) and vch.subs(t, 0) == 2
assert zero(sp.diff(vch, t) + 125 * vch - 1500) and 4000 * Cch == sp.Rational(8, 1000)
tch = sp.log(5) / 125
assert zero(vch.subs(t, tch) - 10) and abs(float(tch) - 0.0129) < 1e-4
iRL = 4 - 4 * sp.exp(-20 * t)  # RL: 24 V, 6 Ohm, 0.3 H
assert zero(24 - 6 * iRL - sp.Rational(3, 10) * sp.diff(iRL, t)) and iRL.subs(t, 0) == 0
assert sp.Rational(3, 10) / 6 == sp.Rational(1, 20) and zero(sp.Rational(3, 10) * sp.diff(iRL, t) - 24 * sp.exp(-20 * t))
v2r = 4 - 4 * sp.exp(-100 * t)  # two resistors: 12 V, 6 k, 3 k, 5 uF
C2r = sp.Rational(5, 10**6)
assert zero((v2r - 12) / 6000 + v2r / 3000 + C2r * sp.diff(v2r, t)) and v2r.subs(t, 0) == 0
assert zero(sp.diff(v2r, t) + 100 * v2r - 400)
assert sp.Rational(6000 * 3000, 9000) * C2r == sp.Rational(1, 100) and 12 * sp.Rational(3, 9) == 4
assert (C2r * sp.diff(v2r, t)).subs(t, 0) == sp.Rational(2, 1000) and sp.Rational(12, 6000) == sp.Rational(2, 1000)
vbk = 8 - 6 * sp.exp(-250 * t)  # read backwards
assert vbk.subs(t, 0) == 2 and sp.limit(vbk.subs(t, tp), tp, sp.oo) == 8 and sp.Rational(1, 250) == sp.Rational(4, 1000)
assert zero(sp.diff(vbk, t) + 250 * vbk - 2000)
assert zero(sp.Rational(4, 10**6) * sp.diff(vbk, t) - sp.Rational(6, 1000) * sp.exp(-250 * t))

# ================================================================ Topic 1
D.H('Topic 1: Classifying a differential equation', cites=W(2, 3))
D.P(r"A **differential equation** is an equation for an unknown *function* that involves its derivatives."
    "\n\n"
    r"It is **ordinary** (an ODE) when the derivatives are taken with respect to one variable only."
    "\n"
    r"- $t$: the **independent variable** (here, time)"
    "\n"
    r"- $i(t)$: the **dependent variable** (the unknown, such as a current)"
    "\n\n"
    r"Week 1's $\dfrac{di}{dt}+\dfrac{R}{L}i=0$ is an ODE."
    "\n\n"
    r"An ODE is **linear** if it can be written as", cites=W(2))
D.EQ(r'a_n(t)\dfrac{d^ny}{dt^n}+\dots+a_1(t)\dfrac{dy}{dt}+a_0(t)\,y=f(t)', cites=W(2))
D.P(r"In this form:"
    "\n"
    r"- $a_k(t)$: the **coefficients** (may depend on $t$, never on $y$)"
    "\n"
    r"- $f(t)$: the **forcing** (the input, a source)"
    "\n\n"
    r"Linear means scaling works: if $y$ solves it with forcing $f$, then $A\,y$ solves it with forcing $A\,f$. "
    r"Double the source, double the response.", cites=W(2))
D.T(['Label', 'Test'], [
    ['**Order**', r'The highest derivative of the unknown. $\dfrac{di}{dt}+\dfrac{R}{L}i=0$ is 1st order; the RLC equation '
                  r'$\dfrac{d^2i}{dt^2}+\dfrac{R}{L}\dfrac{di}{dt}+\dfrac{i}{LC}=0$ is 2nd order.'],
    ['**Linear**', r'Fits the form above: $y$ and its derivatives appear alone, to the first power. Any $y^2$, '
                   r'$y\dfrac{dy}{dt}$, $\sin y$, $e^{y}$, $\dfrac1y$ makes it **nonlinear**.'],
    ['**Homogeneous**', r'Linear, and $f(t)\equiv0$ ("zero for every $t$") once every $y$-term is on the left.'],
    ['**Constant-coefficient**', r'Linear, and every $a_k$ is a constant (like $R$, $L$, $C$).'],
    ['**Autonomous**', r'No $t$ anywhere except inside $y(t)$: the equation does not change with time.'],
], cites=W(2, 3))

D.EX('Functions of t are allowed (lecture Example 2.1)',
     r'Is $t^3\dfrac{d^2y}{dt^2}+e^{t}\dfrac{dy}{dt}+y=0$ linear? Classify it fully.', [
         S(r'The highest derivative is $\dfrac{d^2y}{dt^2}$.', r'\text{order }2'),
         S(r'$y$ and its derivatives each appear alone, to the first power. $t^3$ and $e^{t}$ are functions of $t$ only: '
           r'the linear form allows that.', r'a_2(t)=t^3,\quad a_1(t)=e^{t},\quad a_0=1'),
         S(r'Nothing is left on the right.', r'f(t)=0\ \Rightarrow\ \text{homogeneous}'),
         S(r'But $t^3$ and $e^{t}$ change with time, so it is neither constant-coefficient nor autonomous.',
           r'\text{variable coefficients, not autonomous}'),
     ], 'Yes, linear: second-order, linear, homogeneous, variable-coefficient, not autonomous.'
        '\n\n'
        'Linearity only cares how $y$ appears, not how $t$ appears.', cites=W(3))

D.EX('Move the y-terms left before judging', r'Classify $\dfrac{dy}{dt}=3y$ and $\dfrac{dy}{dt}=3y+2$.', [
    S(r'Put every $y$-term on the left. The first has nothing left over on the right.',
      r'\dfrac{dy}{dt}-3y=0\ \Rightarrow\ \text{homogeneous}'),
    S(r'The second keeps a $2$: that is forcing, so it is not homogeneous.',
      r'\dfrac{dy}{dt}-3y=2\ \Rightarrow\ f(t)=2'),
    S(r'A constant forcing does not change with time, so the second one is still autonomous. Both are first-order, '
      r'linear, constant-coefficient.', r'\text{no }t\text{ anywhere}\ \Rightarrow\ \text{autonomous}'),
], r'Both: first-order, linear, constant-coefficient, autonomous.'
   '\n'
   r'- $\dfrac{dy}{dt}=3y$: homogeneous'
   '\n'
   r'- $\dfrac{dy}{dt}=3y+2$: not homogeneous')

D.EX('A power is not an order', r'Classify $\left(\dfrac{dy}{dt}\right)^3+\sin y=0$.', [
    S(r'The cube is a power, not a derivative: the highest derivative is still the first.', r'\text{order }1'),
    S(r'$\left(\frac{dy}{dt}\right)^3$ (a derivative cubed) and $\sin y$ (the unknown inside a function) are both nonlinear.',
      r'\text{nonlinear}'),
    S(r'"Homogeneous" and "constant-coefficient" only apply to linear equations. No $t$ appears, so it is autonomous.',
      r'\text{autonomous}'),
], 'First-order, nonlinear, autonomous.')

D.PR('Scaling a solution', r'1. $y=t$ solves $\dfrac{dy}{dt}+y=1+t$. Without solving, find a solution of '
     r'$\dfrac{dy}{dt}+y=5+5t$.' '\n\n'
     r'2. $y=\dfrac{1}{1-t}$ solves $\dfrac{dy}{dt}=y^2$. Is $2y=\dfrac{2}{1-t}$ also a solution?', [
         S(r'The new forcing is $5\times$ the old one, and the equation is linear, so $5\times$ the old solution works.',
           r'y=5t'),
         S(r'Check: $\dfrac{d}{dt}(5t)=5$.', r'5+5t=5+5t\ \checkmark'),
         S(r'Part 2: $\dfrac{d}{dt}(1-t)^{-1}=(1-t)^{-2}$ (chain rule), so doubling $y$ doubles the left side but '
           r'quadruples $y^2$.', r'\dfrac{2}{(1-t)^2}\neq\dfrac{4}{(1-t)^2}'),
     ], r'1. $y=5t$.'
        '\n'
        r'2. No: scaling only works for linear equations, and $y^2$ makes this one nonlinear.', cites=W(2))

D.PR('Circuit equations', r'Classify each ($C$, $R$, $I_0$, $\omega$, $V_T$ are constants):' '\n\n'
     r'1. $C\dfrac{dv}{dt}+\dfrac{v}{R}=I_0\cos(\omega t)$ (an RC circuit driven by an AC source)' '\n\n'
     r'2. $C\dfrac{dv}{dt}+I_0\big(e^{v/V_T}-1\big)=0$ (a capacitor discharging through a diode)', [
         S(r'1: $v$ and $\dfrac{dv}{dt}$ appear linearly, times the constants $C$ and $\dfrac1R$. The forcing $I_0\cos(\omega t)$ '
           r'is not zero and depends on $t$.', r'\text{constant coefficients, but }t\text{ in the forcing}'),
         S(r'2: the unknown $v$ sits inside an exponential, so it is nonlinear. No $t$ appears.', r'e^{v/V_T}\ \Rightarrow\ \text{nonlinear}'),
     ], '1. First-order, linear, nonhomogeneous, constant-coefficient, not autonomous.'
        '\n'
        '2. First-order, nonlinear, autonomous.')

# ================================================================ Topic 2
D.H('Topic 2: Solutions and initial value problems', cites=W(1, 4))
D.P(r"A **solution** is a function that makes the equation true for **every** $t$."
    "\n\n"
    r"To check one:"
    "\n"
    r"1. differentiate it"
    "\n"
    r"2. substitute into the equation"
    "\n"
    r"3. simplify both sides"
    "\n\n"
    r"Two more terms:"
    "\n"
    r"- **General solution**: the whole **family** of solutions of a first-order ODE, with one free constant $K$."
    "\n"
    r"- **Initial value problem** (IVP): the ODE plus an **initial condition** $y(t_0)=y_0$ (the value at a starting "
    r"time). That picks out one curve of the family."
    "\n\n"
    r"A second-order ODE needs two conditions: $y(t_0)$ and $\dfrac{dy}{dt}(t_0)$.", cites=W(4))
D.GRAPH(r'''
title "$\dfrac{dy}{dt}=-2y+6$: drag the initial point"
x 0 3 label="$t$"
y -1 7 label="$y$"
field "-2*y+6"
family K -4 4 1 "3+K*exp(-2*t)" color=0
hline "3" label="$y=3$"
drag P 0 1 label="$(t_0,y_0)$" snap=0.25
solution "-2*y+6" x0="P_x" y0="P_y" label="the IVP solution"
readout "$K=(y_0-3)e^{2t_0}=$" "(P_y-3)*exp(2*P_x)"
caption "Faint curves: the family $y=3+Ke^{-2t}$. Each starting point picks one. Slide the point along its own curve: $K$ stays the same."
''')

D.EX('True for every t, not just one', r'Which of $y=\cos 2t$ and $y=\sin t$ solve $\dfrac{d^2y}{dt^2}+4y=0$?', [
    S(steps_fence('', [
        (r'y=\cos 2t', 'The candidate.'),
        (r'\dfrac{dy}{dt}=\hl{-2\sin 2t}', r'Chain rule: $\frac{d}{dt}\cos(at)=-a\sin(at)$.'),
        (r'\dfrac{d^2y}{dt^2}=\hl{-4\cos 2t}', r'Again: $\frac{d}{dt}\sin(at)=a\cos(at)$.'),
        (r'\dfrac{d^2y}{dt^2}+4y=\hl{-4\cos 2t+4\cos 2t}', 'Substitute into the left side.'),
        (r'\dfrac{d^2y}{dt^2}+4y=\hl{0}\ \checkmark', r'Zero for every $t$: a solution.'),
    ])),
    S(r'For $y=\sin t$: $\dfrac{d^2y}{dt^2}=-\sin t$. Substituting leaves $3\sin t$.', r'-\sin t+4\sin t=3\sin t'),
    S(r'That is $0$ at $t=0$, but not at $t=\frac{\pi}{2}$, so it is **not** a solution.', r'3\sin t\neq0'),
], r'$\cos 2t$ is a solution; $\sin t$ is not.')

D.EX('One family, one condition', r'Show that $y=3+Ke^{-2t}$ solves $\dfrac{dy}{dt}=-2y+6$ for every constant $K$. '
     r'Then solve the IVP with $y(0)=1$.', [
         S(r'Left side: the $3$ gives $0$, and $\frac{d}{dt}e^{-2t}=-2e^{-2t}$ (chain rule).', r'\dfrac{dy}{dt}=-2Ke^{-2t}'),
         S(r'Right side with the same $y$: the $6$s cancel. Both sides match for any $K$.', r'-2(3+Ke^{-2t})+6=-2Ke^{-2t}\ \checkmark'),
         S(r'Now put in the condition: at $t=0$, $e^{0}=1$.', r'y(0)=3+K=1\ \Rightarrow\ K=-2'),
     ], r'$y(t)=3-2e^{-2t}$.'
        '\n\n'
        r'In the graph above, put the point at $(0,1)$: the readout shows $K=-2$.')

D.PR('Starting the clock later', r'Same family $y=3+Ke^{-2t}$. Solve the IVP with $y(1)=5$.', [
    S(r'Put $t=1$, not $t=0$: now $e^{-2}$ does not become $1$.', r'3+Ke^{-2}=5\ \Rightarrow\ K=2e^{2}\approx14.78'),
    S(r'Substitute and combine the exponentials ($e^{2}e^{-2t}=e^{-2(t-1)}$).', r'y(t)=3+2e^{-2(t-1)}'),
], r'$y(t)=3+2e^{-2(t-1)}$ ($K=2e^2\approx14.78$; drag the point to $(1,5)$ to see it).')

D.PR('The solution that never moves', r'For $\dfrac{dy}{dt}+ay=b$ with constants $a>0$ and $b$:'
     '\n'
     r'1. Which constant function $y=c$ is a solution?'
     '\n'
     r'2. Use the family $y=\dfrac{b}{a}+Ke^{-at}$ to show every solution ends up there.', [
         S(r'A constant has derivative $0$.', r'0+ac=b\ \Rightarrow\ c=\dfrac{b}{a}'),
         S(r'It is the $K=0$ member of the family. For the others, $e^{-at}\to0$ as $t\to\infty$.',
           r'y(t)=\dfrac{b}{a}+Ke^{-at}\ \to\ \dfrac{b}{a}'),
     ], r'$y=\dfrac{b}{a}$. Every solution approaches it (in the graph: $y=3$).'
        '\n\n'
        r"Topic 3 finds a circuit's final value this way, by setting the derivative to $0$.")

# ================================================================ Topic 3
D.H('Topic 3: First-order RC and RL circuits', cites=W(1, 5))
D.P(r"A circuit with one capacitor or one inductor gives a first-order linear ODE, because each element's law has one "
    r"derivative."
    "\n\n"
    r"Both laws use the **passive sign convention** (the current arrow enters the $+$ end)."
    "\n\n"
    r"Two moments matter at a switch:"
    "\n"
    r"- $0^-$: just before the switch moves"
    "\n"
    r"- $0^+$: just after", cites=W(1, 2))
D.T(['', r'Capacitor $C$ (farads)', r'Inductor $L$ (henries)'], [
    ['Law', r'$i=C\dfrac{dv}{dt}$', r'$v=L\dfrac{di}{dt}$'],
    ['DC steady state (nothing changes)', r'open circuit: $i=0$', r'short: $v=0$'],
    [r"Can't jump at a switch", r'its voltage $v_C$', r'its current $i_L$'],
    ['Time constant', r'$\tau=RC$', r'$\tau=L/R$'],
], cites=W(1, 2, 4))

D.EX('RC natural response (lecture Figures 2.3–2.4)',
     r'The switch has been at $a$ for a long time and moves to $b$ at $t=0$ (drawn as two switches acting together).'
     '\n\n'
     r'Find $v(t)$ for $t\ge0$.' '\n\n' + sch(r'''
V1 0,3 -> 0,0 "$V_s$"
R1 0,3 -> 3,3 "$R_1$"
S1 3,3 -> 5,3 "$t=0$" action=open
C1 5,3 -> 5,0 "$C$" v="$v$"
S2 5,3 -> 8,3 "$t=0$" action=close
R2 8,3 -> 8,0 "$R$" i="$i$"
wire 8,0 -> 0,0
label 3,3 "$a$" above
label 8,3 "$b$" above
ground 0,0'''), [
         S(r'Before $t=0$ the capacitor is open (DC), so no current flows in $R_1$, $R_1$ has no voltage, and $C$ sees all of $V_s$.',
           r'v(0^-)=V_s'),
         S(r"$v_C$ can't jump.", r'v(0^+)=V_s'),
         S(r'For $t\ge0$ only $C$ and $R$ are left. KCL at the top node (current down $C$ + current down $R$ = 0), '
           r'with $v(0)=V_s$, is an IVP.', r'C\dfrac{dv}{dt}+\dfrac{v}{R}=0'),
         S(r'Divide by $C$. Same shape as Week 1\'s $\frac{di}{dt}+\frac{R}{L}i=0$, so the same solution, with $\tau=RC$.'
           .replace("\\'", "'"), r'\dfrac{dv}{dt}+\dfrac{v}{RC}=0\ \Rightarrow\ v=V_se^{-t/\tau}'),
         S(r'After one time constant, $e^{-1}\approx0.37$ is left.', r'v(\tau)\approx0.37\,V_s'),
     ], r'$v(t)=V_se^{-t/\tau}$, $\tau=RC$, $t\ge0$.'
        '\n\n'
        r'$R_1$ does not appear: after the switch it is cut off.', cites=W(3, 4))

FIG26 = flow(r'''I1 0,0 -> 0,3 "$I_s$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$R$" i="$v/R$"
S1 3,3 -> 6,3 "$t=0$" action=close
C1 6,3 -> 6,0 "$C$" v="$v$" i="$i$"
wire 6,0 -> 0,0
ground 0,0''', 'init C1 4')
SCHEMATICS.append(FIG26)
D.SCH(FIG26, r'Lecture Fig. 2.6: the step response. The switch closes at $t=0$; $C$ starts at $v(0)=V_0$. '
      r'**Click the switch** and watch $v$ go from $V_0$ to $V_f$.', cites=W(4))
D.STEPS('Solving the step response (lecture)', [
    (r'C\dfrac{dv}{dt}+\dfrac{v}{R}=I_s', r'KCL at the top node for $t\ge0$: $I_s$ in = current down $C$ + current down $R$.'),
    (r'\dfrac{dv}{dt}+\dfrac{v}{\hl{RC}}=\hl{\dfrac{I_s}{C}}', r'Divide by $C$. Same left side as the natural response, so $\tau=RC$.'),
    (r'0+\dfrac{V_f}{RC}=\dfrac{I_s}{C}\ \Rightarrow\ \hl{V_f=RI_s}', r'Final value $V_f$: in the end nothing changes, so $\frac{dv}{dt}=0$.'),
    (r'\dfrac{du}{dt}+\dfrac{u+\hl{RI_s}}{RC}=\dfrac{I_s}{C}', r'Let $u=v-V_f$, the distance still to go. $V_f$ is constant, so $\frac{du}{dt}=\frac{dv}{dt}$.'),
    (r'\dfrac{du}{dt}+\dfrac{u}{RC}=\hl{0}', r'$\frac{RI_s}{RC}=\frac{I_s}{C}$ cancels the right side.'),
    (r'u(t)=\hl{(V_0-V_f)}\,e^{-t/\tau}', r'The natural response again, starting from $u(0)=V_0-V_f$.'),
    (r'v(t)=\hl{V_f+}(V_0-V_f)\,e^{-t/\tau}', r'Add $V_f$ back: $v=u+V_f$.'),
    (r'v(t)=\hl{RI_s}+(V_0-\hl{RI_s})\,e^{-t/RC}', 'For this circuit (lecture Eq. 2.5).'),
])
D.CO('tip', r'**Any RC or RL circuit after a switch:** $x(t)=x_f+(x_0-x_f)\,e^{-t/\tau}$, where $x$ is $v_C$ or $i_L$.' '\n\n'
     r'- $x_0$: its value just before the switch (it can\'t jump).'.replace("\\'", "'") + '\n'
     r'- $x_f$: its value long after (DC: $C$ open, $L$ short). No source left means $x_f=0$: the natural response.' '\n'
     r'- $\tau=RC$ or $L/R$, with $R$ the resistance the element sees after the switch.', cites=W(5))
D.GRAPH(r'''
title "$v(t)=V_f+(V_0-V_f)e^{-t/RC}$"
x 0 60 label="$t$ (ms)"
y -1 14 label="$v$ (V)"
slider V0 0 12 2 step=0.5 label="$V_0$ (V)"
slider Vf 0 12 12 step=0.5 label="$V_f$ (V)"
slider R 0.5 5 4 step=0.1 label="$R$ (k$\Omega$)"
slider C 0.2 4 2 step=0.1 label="$C$ ($\mu$F)"
curve "Vf+(V0-Vf)*exp(-t/(R*C))" label="$v(t)$"
hline "Vf" color=0 label="$V_f$"
vline "R*C" color=2 label="$t=\tau$"
point "R*C" "Vf+(V0-Vf)*exp(-1)" color=2
vline "5*R*C" color=0 label="$t=5\tau$"
readout "$\tau=RC=$" "R*C" unit=" ms"
readout "$v(\tau)=$" "Vf+(V0-Vf)*exp(-1)" unit=" V"
caption "By $t=\tau$ it has covered $63\%$ of the way from $V_0$ to $V_f$; by $5\tau$, over $99\%$. Set $V_f=0$ for the natural response. Defaults: Example 8."
''')

D.EX('What can jump? (Pre-tutorial 2)', r'In Fig. 2.6, $V_0=0$, $I_s=2\,\mathrm{A}$ and $R=1\,\mathrm{k\Omega}$.'
     '\n\n'
     r'Find the capacitor current $i$:'
     '\n'
     r'- at $t=0^-$ (switch open)'
     '\n'
     r'- at $t=0^+$ (switch closed)'
     '\n\n'
     r'Is it discontinuous at $t=0$, unlike $v$?'
     '\n\n' + sch(r'''
I1 0,0 -> 0,3 "$2\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$1\,\mathrm{k\Omega}$" i="$v/R$"
S1 3,3 -> 6,3 "$t=0$" action=close
C1 6,3 -> 6,0 "$C$" v="$v$" i="$i$"
wire 6,0 -> 0,0
ground 0,0'''), [
         S(r'At $0^-$ the switch is open: the capacitor branch is broken.', r'i(0^-)=0'),
         S(r"$v_C$ can't jump, and it started at $V_0=0$.", r'v(0^+)=v(0^-)=0'),
         S(r'So $R$ carries $\frac{v}{R}=0$, and KCL sends all of $I_s$ into the capacitor.',
           r'i(0^+)=I_s-\dfrac{v(0^+)}{R}=2\,\mathrm{A}'),
         S(r'Check with the formula $v=RI_s\big(1-e^{-t/RC}\big)$: then $i=C\frac{dv}{dt}=I_se^{-t/RC}$, which is '
           r'$2\,\mathrm{A}$ at $0^+$ whatever $C$ is.', r'i(t)=2e^{-t/RC}\,\mathrm{A}'),
     ], r'$i(0^-)=0$, $i(0^+)=2\,\mathrm{A}$: yes, the capacitor current jumps, while $v$ stays at $0$.'
        '\n\n'
        r'Only $v_C$ and $i_L$ must be continuous.', cites=T2 + W(5))

D.EX('Charging from a voltage source', r'The $2\,\mu\mathrm{F}$ capacitor holds $2\,\mathrm{V}$ when the switch closes at '
     r'$t=0$. Find $v(t)$ and the time when $v=10\,\mathrm{V}$.' '\n\n' + sch(r'''
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$4\,\mathrm{k\Omega}$" i="$i$"
C1 6,3 -> 6,0 "$2\,\mu\mathrm{F}$" v="$v$"
wire 6,0 -> 0,0
ground 0,0''', 'init C1 2'), [
         S(r'The stored voltage carries over: it starts at $2\,\mathrm{V}$, not $0$.', r'v(0^+)=2\,\mathrm{V}'),
         S(r'KVL round the loop for $t\ge0$. In series one current flows, and it is the capacitor current.',
           r'12=4000\,i+v,\qquad i=2\times10^{-6}\dfrac{dv}{dt}'),
         S(r'Substitute ($4000\times2\times10^{-6}=0.008$), then divide by $0.008$.', r'\dfrac{dv}{dt}+125v=1500'),
         S(r'$\tau=RC=8\,\mathrm{ms}$ ($\frac1\tau=125$). Long after, $C$ is open, $R$ carries nothing, so $v_f=12\,\mathrm{V}$.',
           r'v(t)=12+(2-12)e^{-125t}=12-10e^{-125t}'),
         S(r'Set $v=10$, isolate the exponential, take $\ln$ ($\ln e^{x}=x$, $\ln0.2=-\ln5$).',
           r'e^{-125t}=0.2\ \Rightarrow\ t=\dfrac{\ln5}{125}=12.9\,\mathrm{ms}'),
     ], r'$v(t)=12-10e^{-125t}\,\mathrm{V}$; $v=10\,\mathrm{V}$ at $t\approx12.9\,\mathrm{ms}$ (about $1.6\tau$).')

D.EX('The inductor version: RL step response', r'The inductor has no current before the switch closes at $t=0$. '
     r'Find $i(t)$ and the inductor voltage $v_L(t)$.' '\n\n' + sch(r'''
V1 0,3 -> 0,0 "$24\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$6\,\Omega$"
L1 6,3 -> 6,0 "$0.3\,\mathrm{H}$" i="$i$" v="$v_L$"
wire 6,0 -> 0,0
ground 0,0'''), [
         S(r"$i_L$ can't jump.", r'i(0^+)=0'),
         S(r'KVL for $t\ge0$: source = resistor + inductor. Divide by $0.3$.',
           r'24=6i+0.3\dfrac{di}{dt}\ \Rightarrow\ \dfrac{di}{dt}+20i=80'),
         S(r'$\tau=\frac{L}{R}$: here a bigger $R$ makes it faster (for RC, slower). Long after, $L$ is a short.',
           r'\tau=\dfrac{0.3}{6}=50\,\mathrm{ms},\qquad i_f=\dfrac{24}{6}=4\,\mathrm{A}'),
         S('The step-response formula.', r'i(t)=4+(0-4)e^{-20t}=4-4e^{-20t}'),
         S(r'$v_L=L\frac{di}{dt}$ (chain rule). It jumps from $0$ to $24\,\mathrm{V}$ at $0^+$: an inductor\'s voltage may '
           r'jump, its current may not.'.replace("\\'", "'"), r'v_L=0.3\cdot80e^{-20t}=24e^{-20t}'),
     ], r'$i(t)=4-4e^{-20t}\,\mathrm{A}$, $v_L(t)=24e^{-20t}\,\mathrm{V}$, $\tau=50\,\mathrm{ms}$.')

D.PR('Two resistors: which R is in τ?', r'The capacitor is uncharged and the switch closes at $t=0$. Find $\tau$, '
     r'$v(t)$ and $i(0^+)$.' '\n\n' + sch(r'''
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
S1 0,3 -> 2,3 "$t=0$" action=close
R1 2,3 -> 5,3 "$6\,\mathrm{k\Omega}$"
R2 5,3 -> 5,0 "$3\,\mathrm{k\Omega}$"
wire 5,3 -> 8,3
C1 8,3 -> 8,0 "$5\,\mu\mathrm{F}$" v="$v$" i="$i$"
wire 8,0 -> 0,0
label 5,3 "$a$" above
ground 0,0'''), [
         S(r'KCL at node $a$ (voltage $v$): current out through $6\,\mathrm{k\Omega}$, through $3\,\mathrm{k\Omega}$, and into $C$ adds to $0$.',
           r'\dfrac{v-12}{6000}+\dfrac{v}{3000}+5\times10^{-6}\dfrac{dv}{dt}=0'),
         S(r'Multiply by $6000$, then divide by $0.03$.', r'\dfrac{dv}{dt}+100v=400'),
         S(r'So $\tau=10\,\mathrm{ms}$. That is $(6\,\mathrm{k}\parallel3\,\mathrm{k})\,C=2\,\mathrm{k\Omega}\times5\,\mu\mathrm{F}$: '
           r'with the source off, $C$ sees both resistors in parallel.', r'\tau=(R_1\parallel R_2)\,C=10\,\mathrm{ms}'),
         S(r'Final value: $C$ open, so a voltage divider; $V_0=0$.', r'v_f=12\cdot\tfrac{3}{9}=4\ \Rightarrow\ v(t)=4-4e^{-100t}'),
         S(r'At $0^+$, $v=0$, so $3\,\mathrm{k\Omega}$ carries nothing and all of $\frac{12}{6000}$ goes into $C$.',
           r'i(0^+)=2\,\mathrm{mA}'),
     ], r'- $\tau=10\,\mathrm{ms}$ (not $6\,\mathrm{k\Omega}\times C$)'
        '\n'
        r'- $v(t)=4-4e^{-100t}\,\mathrm{V}$'
        '\n'
        r'- $i(0^+)=2\,\mathrm{mA}$',
     diff='intermediate')

D.PR('Read a response backwards', r'A capacitor voltage is $v(t)=8-6e^{-250t}\,\mathrm{V}$ for $t\ge0$. Find:'
     '\n'
     r'- $V_0$, $V_f$ and $\tau$'
     '\n'
     r'- the ODE it satisfies'
     '\n'
     r'- the current if $C=4\,\mu\mathrm{F}$', [
         S(r'Match with $V_f+(V_0-V_f)e^{-t/\tau}$: the constant is $V_f$, $t=0$ gives $V_0$, the exponent gives $\frac1\tau$.',
           r'V_f=8,\quad V_0=8-6=2,\quad \tau=\tfrac{1}{250}\,\mathrm{s}=4\,\mathrm{ms}'),
         S(r'Every such response solves $\frac{dv}{dt}+\frac{v}{\tau}=\frac{V_f}{\tau}$ (its constant solution is $V_f$, '
           r'as in Try it 4). Here $\frac1\tau=250$.', r'\dfrac{dv}{dt}+250v=2000'),
         S(r'$\frac{d}{dt}e^{-250t}=-250e^{-250t}$ (chain rule), so $\frac{dv}{dt}=(-6)(-250)e^{-250t}=1500e^{-250t}$. '
           r'Multiply by $C$.', r'i=4\times10^{-6}\cdot1500e^{-250t}=6e^{-250t}\,\mathrm{mA}'),
     ], r'- $V_0=2\,\mathrm{V}$, $V_f=8\,\mathrm{V}$, $\tau=4\,\mathrm{ms}$'
        '\n'
        r'- ODE: $\dfrac{dv}{dt}+250v=2000$'
        '\n'
        r'- $i(t)=6e^{-250t}\,\mathrm{mA}$',
     diff='intermediate')

print('validating schematics ...')
validate_schematics()
D.save()
