"""ELEC 231 Week 5 v2: second-order constant-coefficient ODEs, existence and uniqueness, RLC circuits.

No Week 5 lecture exists: scope = syllabus Week 5 outcomes (SYL p. 4) + Nilsson & Riedel Ch. 8.
Every answer and every tool formula is checked with sympy/numpy below; every schematic is validated.
Run:  .venv/Scripts/python.exe scripts/notes231/build_w5v2.py [--publish]
"""
import json
import math
import re
import urllib.error
import urllib.request

import numpy as np
import sympy as sp

from lib231 import Doc, S, steps_fence

D = Doc(week=5, title='Week 5: Second-Order Linear ODEs and RLC Circuits',
        topic_keys=['second_order_homogeneous', 'existence_uniqueness_second_order', 'rlc_circuits'])
SYL = D.cite('SYL', 4)

t = sp.symbols('t', real=True)
E = sp.exp
R_ = sp.Rational


# ---------------------------------------------------------------- check helpers
def ode(y, a, b, c, rhs=0):
    """Assert y solves a*y'' + b*y' + c*y = rhs."""
    r = sp.simplify(a * y.diff(t, 2) + b * y.diff(t) + c * y - rhs)
    assert r == 0, f'ODE check failed: {r}'


def ic(y, y0, dy0, t0=0):
    assert sp.simplify(y.subs(t, t0) - y0) == 0, f'y({t0}) = {y.subs(t, t0)} != {y0}'
    assert sp.simplify(y.diff(t).subs(t, t0) - dy0) == 0, f"y'({t0}) = {y.diff(t).subs(t, t0)} != {dy0}"


def roots(a, b, c):
    s = sp.symbols('s')
    rts = sp.roots(sp.Poly(a * s**2 + b * s + c, s))
    return sorted([r for r, m in rts.items() for _ in range(m)], key=lambda z: (sp.re(z), sp.im(z)))


def wr(y1, y2):
    return sp.simplify(y1 * y2.diff(t) - y1.diff(t) * y2)


def close(x, v, tol=1e-3):
    x = float(x)
    assert abs(x - v) <= tol * max(1, abs(v)), f'{x} != {v}'


def tool_eval(src, **env):
    """Evaluate a graph-tool expression the way the app does (if(c,a,b): c>0 picks a; sqrt(<0) = NaN)."""
    with np.errstate(all='ignore'):
        ns = {'exp': np.exp, 'cos': np.cos, 'sin': np.sin, 'abs': np.abs,
              'sqrt': lambda v: np.sqrt(np.float64(v)) if v >= 0 else np.nan,
              'iff': lambda c, a, b: a if c > 0 else b}
        ns.update({k: np.float64(v) for k, v in env.items()})
        return float(eval(src.replace('^', '**').replace('if(', 'iff('), ns))


SCH_URL = 'http://127.0.0.1:8000/api/v1/schematics/check'


def check_schematics(blocks):
    """POST every schematic in the note to the checker; fail the build on any error or warning."""
    found = 0
    for b in blocks:
        texts = [b.get('prompt', ''), b.get('text', '')]
        if b['type'] == 'schematic':
            texts.append('```schematic\n' + b['source'] + '\n```')
        for txt in texts:
            for src in re.findall(r'```schematic\n(.*?)```', txt or '', flags=re.S):
                req = urllib.request.Request(SCH_URL, data=json.dumps({'source': src}).encode(), method='POST',
                                             headers={'Content-Type': 'application/json'})
                try:
                    out = json.load(urllib.request.urlopen(req))
                except urllib.error.HTTPError as e:
                    raise SystemExit(f'schematic rejected ({e.code}): {e.read().decode()[:500]}\n{src}')
                assert not out.get('errors'), (out['errors'], src)
                assert not out.get('warnings'), (out['warnings'], src)
                found += 1
    print(f'{found} schematics validated')


def par(Cl, Ll, Rl=None):
    """Textbook Fig. 8.1: C, L (and R) in parallel; v is + at the top, every branch current drawn downward."""
    s = (f'C1 0,3 -> 0,0 "{Cl}" v="$v$" i="$i_C$"\n'
         f'wire 0,3 -> 3,3\n'
         f'L1 3,3 -> 3,0 "{Ll}" i="$i_L$"\n')
    if Rl:
        s += f'wire 3,3 -> 6,3\nR1 6,3 -> 6,0 "{Rl}" i="$i_R$"\nwire 6,0 -> 0,0\n'
    else:
        s += 'wire 3,0 -> 0,0\n'
    return '```schematic\n' + s + 'ground 0,0\n```'


# ================================================================ checks: Topic 1
y_ex1 = 2 * E(-t) - E(-2 * t)
assert roots(1, 3, 2) == [-2, -1]
ode(y_ex1, 1, 3, 2); ic(y_ex1, 1, 0)

assert roots(4, 4, 1) == [-R_(1, 2), -R_(1, 2)]
ode(t * E(-t / 2), 4, 4, 1)
y_ex2 = (4 + 2 * t) * E(-t / 2)
ode(y_ex2, 4, 4, 1); ic(y_ex2, 4, 0)

assert roots(1, 2, 5) == [-1 - 2 * sp.I, -1 + 2 * sp.I]
y_ex3 = E(-t) * (sp.cos(2 * t) + sp.sin(2 * t))
ode(y_ex3, 1, 2, 5); ic(y_ex3, 1, 1)

k = sp.symbols('k')
assert sp.expand(2**2 - 4 * k) == 4 - 4 * k
assert roots(1, 2, 1) == [-1, -1] and roots(1, 2, 0) == [-2, 0]
ode(sp.Integer(1) + 0 * t, 1, 2, 0); ode(E(-2 * t), 1, 2, 0)

ode(E(-3 * t) * sp.cos(4 * t), 1, 6, 25)
assert sp.expand((t + 3 - 4 * sp.I) * (t + 3 + 4 * sp.I)) == t**2 + 6 * t + 25
y_tr2 = 2 * E(-3 * t) * sp.sin(4 * t)
ode(y_tr2, 1, 6, 25); ic(y_tr2, 0, 8)

# root-plane tool: the point formulas give the true roots of s^2 + b s + c
S1X = 'if(b^2-4*c>=0,(-b+sqrt(b^2-4*c))/2,-b/2)'
S1Y = 'if(b^2-4*c>=0,0,sqrt(4*c-b^2)/2)'
S2X = 'if(b^2-4*c>=0,(-b-sqrt(b^2-4*c))/2,-b/2)'
S2Y = 'if(b^2-4*c>=0,0,-sqrt(4*c-b^2)/2)'
for bb, cc in [(1, 4), (4, 4), (6, 2), (-1, 3), (0, 9), (2, 0)]:
    got = sorted([complex(tool_eval(S1X, b=bb, c=cc), tool_eval(S1Y, b=bb, c=cc)),
                  complex(tool_eval(S2X, b=bb, c=cc), tool_eval(S2Y, b=bb, c=cc))], key=lambda z: (z.real, z.imag))
    want = sorted(np.roots([1, bb, cc]), key=lambda z: (z.real, z.imag))
    assert all(abs(g - w) < 1e-6 for g, w in zip(got, want)), (bb, cc, got, want)

# ================================================================ checks: Topic 2
assert set(sp.solve(t**2 - 9, t)) == {-3, 3}
assert sp.pi / 2 < 2 < 3 < 3 * sp.pi / 2
assert wr(E(-2 * t), 3 * E(-2 * t)) == 0 and wr(E(-2 * t), t * E(-2 * t)) == E(-4 * t)
ode(t * E(-2 * t), 1, 4, 4)
ode(sp.Integer(0) * t, 1, t, E(t))

# ================================================================ checks: Topic 3
# RLC tool: L = 1 H, C = 0.25 F, V = 10 V, v(0) = 0, i(0) = 0  ->  v'' + R v' + 4 v = 40
A_, DD = '(R/2)', '(R^2/4-4)'
RR, WD = f'sqrt({DD})', 'sqrt(4-R^2/4)'
OVER = f'((-{A_}+{RR})*exp((-{A_}-{RR})*t)-(-{A_}-{RR})*exp((-{A_}+{RR})*t))/(2*{RR})'
UNDER = f'exp(-{A_}*t)*(cos({WD}*t)+{A_}/{WD}*sin({WD}*t))'
CRIT = f'(1+{A_}*t)*exp(-{A_}*t)'
VC = f'10*(1-if({DD}-0.001,{OVER},if(-{DD}-0.001,{UNDER},{CRIT})))'
for Rv in (0, 1, 3.9, 4, 4.1, 6, 10):
    yy = sp.Function('v')
    sol = sp.dsolve(yy(t).diff(t, 2) + sp.nsimplify(Rv) * yy(t).diff(t) + 4 * yy(t) - 40, yy(t),
                    ics={yy(0): 0, yy(t).diff(t).subs(t, 0): 0}).rhs
    for tv in (0, 0.3, 1, 2.5, 6):
        close(tool_eval(VC, R=Rv, t=tv), float(sol.subs(t, tv)), 1e-6)

# Ex 7: textbook 8.53 (series, step, critically damped)
Rs, Ls, Cs = 4, R_(4, 100), R_(1, 100)
vo = 100 + (5000 * t + 100) * E(-50 * t)
ode(vo, Ls * Cs, Rs * Cs, 1, rhs=100); ic(vo, 200, 0)
assert Rs / (2 * Ls) == 50 and 1 / sp.sqrt(Ls * Cs) == 50

# Ex 8: textbook 8.7 (parallel, natural, underdamped)
Lp, Cp, V0, I0 = R_(1, 4), R_(1, 10**8), sp.Integer(90), R_(-3, 100)
R87 = R_(12500, 3)
v87 = E(-12000 * t) * (90 * sp.cos(16000 * t) + 120 * sp.sin(16000 * t))
ode(v87, 1, 1 / (R87 * Cp), 1 / (Lp * Cp)); ic(v87, V0, (-V0 / R87 - I0) / Cp)
assert 1 / (2 * R87 * Cp) == 12000 and 1 / sp.sqrt(Lp * Cp) == 20000 and sp.sqrt(20000**2 - 12000**2) == 16000
assert -V0 / R87 - I0 == R_(84, 10000)

# Try 5: textbook 8.14 (LC, no resistor)
L14, C14 = R_(2, 5), R_(1, 4)
v14 = 12 / sp.sqrt(10) * sp.sin(sp.sqrt(10) * t)
ode(v14, 1, 0, 1 / (L14 * C14)); ic(v14, 0, 3 / C14)
close(12 / sp.sqrt(10), 3.795); close(sp.sqrt(10), 3.162)

# Try 6: textbook 8.2 (from v(t) back to the circuit)
C2 = R_(18, 10**6)
v2 = -12 * (E(-200 * t) + E(-1800 * t))
assert sp.expand((t + 200) * (t + 1800)) == t**2 + 2000 * t + 360000
R2 = 1 / (2000 * C2); L2 = 1 / (360000 * C2)
ode(v2, 1, 1 / (R2 * C2), 1 / (L2 * C2))
iC0 = C2 * v2.diff(t).subs(t, 0); iR0 = v2.subs(t, 0) / R2
assert iC0 == R_(432, 1000) and iR0 == R_(-864, 1000) and -iC0 - iR0 == R_(432, 1000)
close(R2, 27.78)

# ================================================================ Topic 1
D.H('Topic 1: Second-order equations: guess $e^{st}$', cites=SYL)
D.P(r"A **second-order** ODE contains $y''=\dfrac{d^2y}{dt^2}$, the derivative of the derivative."
    "\n\n"
    r"This week it has the form $ay''+by'+cy=0$:"
    "\n"
    r"- $a,b,c$: **constant** numbers"
    "\n"
    r"- right side $0$: **homogeneous** (no source)"
    "\n\n"
    r"**Guess $y=e^{st}$.** Each derivative of it is the same exponential times the number $s$, so everything can cancel.",
    cites=SYL)
D.STEPS('From the ODE to the characteristic equation', [
    (r"ay''+by'+cy=0", r'$a$, $b$, $c$ are constants.'),
    (r"y=e^{st},\quad y'=\hl{s}e^{st},\quad y''=\hl{s^2}e^{st}", r'Each derivative brings out a factor $s$ (chain rule: $\frac{d}{dt}e^{st}=se^{st}$).'),
    (r'a\hl{s^2e^{st}}+b\hl{se^{st}}+c\hl{e^{st}}=0', 'Substitute the three pieces.'),
    (r'\hl{(as^2+bs+c)}\,e^{st}=0', r'Factor out $e^{st}$.'),
    (r'as^2+bs+c=0', r'$e^{st}$ is never $0$, so the bracket is. This is the **characteristic equation**.'),
    (r's_{1,2}=\dfrac{-b\pm\sqrt{\hl{b^2-4ac}}}{2a}', r'Quadratic formula. The sign of $b^2-4ac$ decides the kind of roots.'),
])
D.T(['Roots', 'General solution'], [
    [r'two real, $s_1\neq s_2$ ($b^2-4ac>0$)', r'$y=C_1e^{s_1t}+C_2e^{s_2t}$'],
    [r'one repeated, $s$ ($b^2-4ac=0$)', r'$y=(C_1+C_2t)\,e^{st}$'],
    [r'complex pair, $\sigma\pm j\omega$ ($b^2-4ac<0$)', r'$y=e^{\sigma t}(C_1\cos\omega t+C_2\sin\omega t)$'],
])
D.P(r"Two constants need two conditions:"
    "\n"
    r"- $y(0)$: the start **value**"
    "\n"
    r"- $y'(0)$: the start **slope**"
    "\n\n"
    r"Each example below is one row of the table.")
D.GRAPH(rf'''
title "Where the roots of $s^2+bs+c=0$ sit"
x -8.5 3.5 label="Re $s$"
y -3.6 3.6 label="Im $s$"
equal
slider b -2 8 1 step=0.1 label="$b$" animate
slider c 0 10 4 step=0.25 label="$c$"
region "x>0" color=6 label="right half: $e^{{st}}$ grows"
circle "0" "0" "sqrt(c)" dash color=0 label="circle $|s|=\sqrt c$"
point "{S1X}" "{S1Y}" color=1
point "{S2X}" "{S2Y}" color=3
text "{S1X}+0.12" "{S1Y}+0.12" "$s_1$" color=1
text "{S2X}+0.12" "{S2Y}-0.55" "$s_2$" color=3
text "if(b^2-4*c-0.05,-8.2,sqrt(-1))" "3.1" "**two real roots**"
text "if(abs(b^2-4*c)<0.05,-8.2,sqrt(-1))" "3.1" "**one repeated root**"
text "if(4*c-b^2-0.05,-8.2,sqrt(-1))" "3.1" "**complex pair** $\sigma\pm j\omega$"
readout "$b^2-4c=$" "b^2-4*c"
readout "$s_1=$" "(-b+sqrt(b^2-4*c))/2"
readout "$s_2=$" "(-b-sqrt(b^2-4*c))/2"
readout "$\sigma=$" "if(4*c-b^2,-b/2,sqrt(-1))"
readout "$\omega=$" "sqrt(4*c-b^2)/2"
caption "Press play on $b$ and watch the two roots move."
''')
D.P(r"What happens as $b$ changes (with $c=4$):"
    "\n"
    r"- **From $b=1$:** the complex pair slides round the dashed circle."
    "\n"
    r"- **At $b=4$:** the roots meet on the real axis (repeated)."
    "\n"
    r"- **Above $b=4$:** they split into two real roots."
    "\n"
    r"- **Negative $b$:** the roots move into the shaded half: growing solutions.")

D.EX('Two real roots: fit the two constants', r"Solve $y''+3y'+2y=0$ with $y(0)=1$, $y'(0)=0$.", [
    S(r'Characteristic equation; it factors ($1\cdot2=2$, $1+2=3$).', r's^2+3s+2=(s+1)(s+2)=0\ \Rightarrow\ s=-1,\ -2'),
    S('Two different real roots: first row of the table.', r'y=C_1e^{-t}+C_2e^{-2t}'),
    S(steps_fence('Fit $C_1$ and $C_2$', [
        (r'y=C_1e^{-t}+C_2e^{-2t}', 'The general solution.'),
        (r"y'=\hl{-C_1e^{-t}-2C_2e^{-2t}}", r'Differentiate each term: $\frac{d}{dt}e^{st}=se^{st}$.'),
        (r'y(0)=\hl{C_1+C_2}=1', r'Put $t=0$ in $y$; every $e^{0}=1$.'),
        (r"y'(0)=\hl{-C_1-2C_2}=0", r"Put $t=0$ in $y'$."),
        (r'\hl{-C_2=1}\ \Rightarrow\ C_2=-1', r'Add the two equations: $C_1$ cancels.'),
        (r'C_1=1-C_2=\hl{2}', 'Back into the first equation.'),
        (r'y=\hl{2}e^{-t}\hl{-}e^{-2t}', r"Check: $y(0)=2-1=1$, $y'(0)=-2+2=0$ ✓"),
    ])),
], r'$y=2e^{-t}-e^{-2t}$ (decays to $0$ without crossing it)')

D.EX('Repeated root: the extra $t$', r"Solve $4y''+4y'+y=0$ with $y(0)=4$, $y'(0)=0$.", [
    S(r'Keep $a=4$ (a common slip is $s^2+4s+1$). The left side is a perfect square.',
      r'4s^2+4s+1=(2s+1)^2=0\ \Rightarrow\ s=-\tfrac12\ \text{twice}'),
    S(r"One root gives only $e^{-t/2}$. Two copies of it are really one constant: it can't match a value **and** a slope.",
      r'C_1e^{-t/2}+C_2e^{-t/2}=(C_1+C_2)\,e^{-t/2}'),
    S(r'The second solution is $te^{-t/2}$:', r'y=(C_1+C_2t)\,e^{-t/2}'),
    S(r"Check that $te^{-t/2}$ is a solution: differentiate with the product rule, substitute, and everything cancels.",
      r"y'=(1-\tfrac t2)e^{-t/2},\qquad y''=(-1+\tfrac t4)e^{-t/2}\qquad 4(-1+\tfrac t4)+4(1-\tfrac t2)+t=0\ \checkmark"),
    S(r"Differentiate the general solution (product rule) and put $t=0$.",
      r"y(0)=C_1=4,\qquad y'(0)=C_2-\tfrac12C_1=0"),
    S(r'So $C_2=\tfrac12\cdot4=2$.', r'y=(4+2t)\,e^{-t/2}'),
], r'$y=(4+2t)\,e^{-t/2}$')

D.EX('Complex roots: where the cosine comes from', r"Solve $y''+2y'+5y=0$ with $y(0)=1$, $y'(0)=1$.", [
    S(r'Quadratic formula; $\sqrt{-16}=j4$.', r's=\frac{-2\pm\sqrt{4-20}}{2}=-1\pm j2'),
    S(r'Euler (Week 1) splits each complex exponential into a cosine and a sine.',
      r'e^{(-1\pm j2)t}=e^{-t}(\cos2t\pm j\sin2t)'),
    S(r"Half their sum, and their difference over $2j$, are solutions too (sums and multiples of solutions are). "
      r"No $j$ is left:",
      r'y=e^{-t}(C_1\cos2t+C_2\sin2t)'),
    S(r'At $t=0$: $\cos0=1$, $\sin0=0$.', r'y(0)=C_1=1'),
    S(r"Product rule, then $t=0$. In general $y'(0)=\sigma C_1+\omega C_2$, here with $\sigma=-1$, $\omega=2$.",
      r"y'(0)=-C_1+2C_2=1\ \Rightarrow\ C_2=1"),
], r'$y=e^{-t}(\cos2t+\sin2t)$: oscillates at $2$ rad/s inside the shrinking envelope $e^{-t}$')

D.PR('One equation, every case', r"""Consider $y''+2y'+ky=0$.

1. For which $k$ are the roots two real, repeated, or complex? (Check in the graph: $b=2$, slide $c$.)
2. At $k=0$ one root is $s=0$. What is the general solution, and does every solution die out?""", [
    S(r'The case is the sign of $b^2-4ac$ with $a=1$, $b=2$, $c=k$.', r'b^2-4ac=4-4k'),
    S(r'Positive, zero, negative:', r'k<1:\ \text{two real},\quad k=1:\ \text{repeated},\quad k>1:\ \text{complex}'),
    S(r'$k=0$: $s^2+2s=s(s+2)=0$. The root $s=0$ gives $e^{0t}=1$, a constant.', r'y=C_1+C_2e^{-2t}'),
    S(r'$e^{-2t}\to0$ but $C_1$ stays: the solution settles at $C_1$, not $0$ (a root on the vertical axis does not decay).', r'y\to C_1'),
], r"""1. $k<1$: two real; $k=1$: repeated; $k>1$: complex.
2. $y=C_1+C_2e^{-2t}\to C_1$, so no.""")

D.PR('Work backwards from a solution', r"""One solution of $y''+by'+cy=0$ is $e^{-3t}\cos4t$.

1. Find $b$ and $c$.
2. Solve with $y(0)=0$, $y'(0)=8$.""", [
    S(r'$e^{\sigma t}\cos\omega t$ comes from the roots $\sigma\pm j\omega$.', r's=-3\pm j4'),
    S(r'Rebuild the quadratic as $(s-s_1)(s-s_2)$; note $(j4)^2=-16$.',
      r'(s+3)^2-(j4)^2=s^2+6s+25\ \Rightarrow\ b=6,\ c=25'),
    S(r"Complex row; $y(0)=C_1=0$ and $y'(0)=\sigma C_1+\omega C_2=4C_2=8$.", r'C_1=0,\quad C_2=2'),
], r"""1. $b=6$, $c=25$
2. $y=2e^{-3t}\sin4t$""", diff='intermediate')

# ================================================================ Topic 2
D.H('Topic 2: Existence and uniqueness: why two conditions are enough', cites=SYL + D.cite('W3', 5))
D.P(r"A second-order equation needs two starting facts:"
    "\n"
    r"- $y(t_0)$: the start **value**"
    "\n"
    r"- $y'(t_0)$: the start **slope**"
    "\n\n"
    r"In a circuit they come from the capacitor voltage and the inductor current."
    "\n\n"
    r"With both given there is **exactly one** solution. So once a formula fits both, it *is* the answer."
    "\n\n"
    r"This is the second-order version of Week 3's theorem.", cites=SYL + D.cite('W3', 5))
D.CO('info', r"""**Theorem.** Divide by the coefficient of $y''$ to get $y''+p(t)\,y'+q(t)\,y=g(t)$.

- **If** $p$, $q$, $g$ are continuous on an open interval $I$ containing $t_0$,
- **then** for any numbers $Y_0$, $Y_1$ the problem $y(t_0)=Y_0$, $y'(t_0)=Y_1$ has **exactly one** solution, and it exists on all of $I$.

Constant coefficients are continuous everywhere, so Topic 1's solutions hold for all $t$.""", cites=D.cite('W3', 5))
D.P(r"**Why $C_1y_1+C_2y_2$ can always be fitted.** The two conditions are two linear equations for $C_1$, $C_2$."
    "\n\n"
    r"They have a solution for every $Y_0$, $Y_1$ exactly when their determinant, the **Wronskian**, is not zero:")
D.EQ(r"W=\begin{vmatrix}y_1&y_2\\ y_1'&y_2'\end{vmatrix}=y_1y_2'-y_1'y_2\neq0")

D.EX('Largest interval: division by zero', r"""$(t^2-9)\,y''+t\,y'+4y=e^t$, $\ y(1)=0$, $\ y'(1)=2$.

Find the largest interval on which this surely has exactly one solution.""", [
    S(r"Divide by $t^2-9$, the coefficient of $y''$.", r"y''+\frac{t}{t^2-9}\,y'+\frac{4}{t^2-9}\,y=\frac{e^t}{t^2-9}"),
    S(r'$p$, $q$, $g$ break only where the bottom is $0$.', r't^2-9=0\ \Rightarrow\ t=\pm3'),
    S(r'Take the piece between the bad points that contains $t_0=1$. (Starting at $t_0=5$ would give $t>3$ instead.)', r'-3<t<3'),
], r'$-3<t<3$')

D.EX('Largest interval: the nearest trouble on each side', r"Same question for $(t-2)\,y''+y'+(t-2)(\tan t)\,y=0$, $y(3)=1$, $y'(3)=0$.", [
    S(r"Divide by $t-2$; in the last term it cancels.", r"y''+\frac{1}{t-2}\,y'+(\tan t)\,y=0"),
    S(r"The $y'$ coefficient breaks at $t=2$. $\tan t$ (sine over cosine) breaks where $\cos t=0$.",
      r't=2,\qquad t=\pm\tfrac{\pi}{2}\approx\pm1.57,\ \pm\tfrac{3\pi}{2}\approx\pm4.71,\ \dots'),
    S(r'Nearest bad point left of $t_0=3$ is $2$; nearest on the right is $3\pi/2$.', r'2<t<\dfrac{3\pi}{2}'),
], r'$2<t<\dfrac{3\pi}{2}\approx4.71$')

D.EX('The Wronskian: why the repeated root needs $t$', r"""For $y''+4y'+4y=0$ (root $s=-2$ twice), test two pairs:

1. $e^{-2t}$ and $3e^{-2t}$
2. $e^{-2t}$ and $te^{-2t}$""", [
    S(r"**Pair 1:** $y_2'=-6e^{-2t}$, and the two products cancel.",
      r'W=e^{-2t}(-6e^{-2t})-(-2e^{-2t})(3e^{-2t})=0'),
    S(r"$W=0$ because $3e^{-2t}$ is just a multiple of $e^{-2t}$: this pair can't fit both conditions."),
    S(r"**Pair 2:** product rule gives $y_2'=(1-2t)e^{-2t}$; use $e^{-2t}e^{-2t}=e^{-4t}$.",
      r'W=(1-2t)e^{-4t}+2t\,e^{-4t}=e^{-4t}\neq0'),
], r"""Only $e^{-2t}$ with $te^{-2t}$ works ($W=e^{-4t}\neq0$).

So $(C_1+C_2t)e^{-2t}$ is the general solution.""")

D.PR('Logarithms: the start decides', r"""For $(t-1)\,y''+y'+y=\ln t$, find the largest guaranteed interval when the conditions are given at:

1. $t_0=2$
2. $t_0=\tfrac12$""", [
    S(r"Divide by $t-1$.", r"y''+\frac{1}{t-1}\,y'+\frac{1}{t-1}\,y=\frac{\ln t}{t-1}"),
    S(r'Bad points: $t=1$ (division by zero) and $t\le0$ (no $\ln$ there).', r't\le0,\qquad t=1'),
    S(r'From $t_0=2$: nothing stops it on the right. From $t_0=\tfrac12$: trapped between $0$ and $1$.', r'(1)\ t>1,\qquad (2)\ 0<t<1'),
], r"""1. $t>1$
2. $0<t<1$""", diff='intermediate')

D.PR('Uniqueness as a shortcut', r"""1. Solve $y''+t\,y'+e^t\,y=0$ with $y(2)=0$, $y'(2)=0$ without any formula.
2. Why can $y=t^2$ never solve an equation $y''+p(t)\,y'+q(t)\,y=0$ with $p$, $q$ continuous near $t=0$?""", [
    S(r'$y=0$ satisfies the equation and both conditions. $p=t$, $q=e^t$ are continuous, so it is the only solution.', r'y(t)=0'),
    S(r"$y=t^2$ has $y(0)=0$ and $y'(0)=0$: the same start as $y=0$.", r"y(0)=0,\quad y'(0)=0"),
    S(r'Uniqueness would force $t^2=0$ near $t=0$, which is false. So no such equation exists.', r't^2\not\equiv0'),
], r"""1. $y=0$.
2. $t^2$ and $0$ share the same start, so uniqueness would make them equal.""", diff='advanced')

# ================================================================ Topic 3
D.H('Topic 3: RLC circuits', cites=SYL)
D.SCH('''V1 0,3 -> 0,0 "$V$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$R$" i="$i$"
L1 6,3 -> 9,3 "$L$"
C1 9,3 -> 9,0 "$C$" v="$v_C$"
wire 9,0 -> 0,0
ground 0,0''', 'Series RLC with a constant impressed voltage $V$, switched in at $t=0$.', cites=SYL)
D.P(r"The circuit stores energy in two places, so it gives a second-order equation:"
    "\n"
    r"- the **capacitor** (its voltage $v_C$)"
    "\n"
    r"- the **inductor** (its current $i$)"
    "\n\n"
    r"Neither can jump at the switch, so the two starting facts are:"
    "\n"
    r"- $V_0=v_C(0^+)$"
    "\n"
    r"- $I_0=i(0^+)$")
D.STEPS('KVL gives a Topic 1 equation (Nilsson & Riedel 8.4)', [
    (r'V=Ri+L\dfrac{di}{dt}+v_C', r'KVL around the loop for $t>0$.'),
    (r'V=\hl{RC\dfrac{dv_C}{dt}}+\hl{LC\dfrac{d^2v_C}{dt^2}}+v_C', r'The loop current is the capacitor current: $i=C\frac{dv_C}{dt}$.'),
    (r'\dfrac{d^2v_C}{dt^2}+\hl{\dfrac{R}{L}}\dfrac{dv_C}{dt}+\hl{\dfrac{1}{LC}}v_C=\hl{\dfrac{V}{LC}}', r'Divide by $LC$.'),
    (r'v_C=\hl{V}+v_n(t)', r'A constant solves it only if it equals $V$ (its derivatives are $0$): the **final value**. The rest, $v_n$, solves the same equation with $0$ on the right.'),
    (r's^2+\hl{2\alpha}s+\hl{\omega_0^2}=0,\quad \alpha=\dfrac{R}{2L},\ \ \omega_0=\dfrac{1}{\sqrt{LC}}', r'Characteristic equation of $v_n$. Textbook names: $\alpha$ (alpha, s$^{-1}$), $\omega_0$ (omega-zero, rad/s).'),
    (r's_{1,2}=-\alpha\pm\sqrt{\hl{\alpha^2-\omega_0^2}}', r'Quadratic formula: compare $\alpha$ with $\omega_0$.'),
])
D.T(['Case', 'Test', r'$v_C(t)$ for $t\ge0$'], [
    ['**overdamped**', r'$\alpha>\omega_0$', r'$V+A_1e^{s_1t}+A_2e^{s_2t}$'],
    ['**critically damped**', r'$\alpha=\omega_0$', r'$V+(D_1t+D_2)\,e^{-\alpha t}$'],
    ['**underdamped**', r'$\alpha<\omega_0$', r'$V+e^{-\alpha t}(B_1\cos\omega_dt+B_2\sin\omega_dt)$, $\ \omega_d=\sqrt{\omega_0^2-\alpha^2}$'],
])
D.CO('tip', r"""**The two conditions at $t=0^+$:**
- **Value:** $v_C(0^+)=V_0$
- **Slope:** $\dfrac{dv_C}{dt}(0^+)=\dfrac{i_C(0^+)}{C}$, from $i_C=C\dfrac{dv_C}{dt}$
- **Series loop:** $i_C=i$, so the slope is $I_0/C$

**Parallel** RLC (no source, Fig. 8.1): KCL gives the same equation for $v$, with:
- $\alpha=\dfrac{1}{2RC}$
- no $V$
- $\omega_0$ unchanged""")
D.GRAPH(rf'''
title "Slide $R$ through the three cases"
x 0 8 label="$t$ (s)"
y 0 24 label="$v_C$ (V)"
slider R 0 10 1 step=0.1 label="$R$ ($\Omega$)" animate
hline "10" label="final value $V$"
curve "{VC}" color=1 label="$v_C(t)$"
text "if({DD}-0.001,4.2,sqrt(-1))" "22.6" "**overdamped**"
text "if(abs({DD})<0.001,4.2,sqrt(-1))" "22.6" "**critically damped**"
text "if((-{DD}-0.001)*(R>0.001),4.2,sqrt(-1))" "22.6" "**underdamped**"
text "if(R<0.001,4.2,sqrt(-1))" "22.6" "**undamped** (LC: $\alpha=0$)"
readout "$\alpha=$" "R/2"
readout "$\omega_0=$" "2"
readout "$s_1=$" "-R/2+sqrt(R^2/4-4)"
readout "$s_2=$" "-R/2-sqrt(R^2/4-4)"
readout "$\omega_d=$" "sqrt(4-R^2/4)"
caption "$L=1$ H, $C=0.25$ F, $V=10$ V, starting from $v_C(0)=0$, $i(0)=0$. A dash in a readout means that kind of root doesn't exist."
''')
D.P(r"Critical at $R=4\,\Omega$, where $\alpha=\omega_0=2$:"
    "\n"
    r"- **Below it:** the voltage overshoots and rings ($R=0$: forever)."
    "\n"
    r"- **Above it:** it creeps up.")

D.EX('Constant impressed voltage: a step response (textbook 8.53)', r"""The circuit has run for a long time with $v_s=200\,\mathrm{V}$. At $t=0$ the source drops to $100\,\mathrm{V}$.

Find $v_o(t)$ for $t\ge0$.

```schematic
V1 0,3 -> 0,0 "$v_s$"
R1 0,3 -> 3,3 "$4\,\Omega$" i="$i$"
L1 3,3 -> 6,3 "$40\,\mathrm{mH}$"
C1 6,3 -> 6,0 "$10\,\mathrm{mF}$" v="$v_o$"
wire 6,0 -> 0,0
ground 0,0
```""", [
    S(r'Before $t=0$ (DC for a long time) the capacitor is an open circuit: no current, so it holds all $200$ V.', r'V_0=200\ \mathrm{V},\qquad I_0=0'),
    S(r'After the drop, $V=100$ V. Series formulas ($L=0.04$ H, $C=0.01$ F):', r'\alpha=\frac{4}{2(0.04)}=50,\qquad \omega_0=\frac{1}{\sqrt{0.04\cdot0.01}}=50'),
    S(r'$\alpha=\omega_0$: critically damped, root $-50$ twice. The final value is the new source voltage.', r'v_o=100+(D_1t+D_2)\,e^{-50t}'),
    S(r'Value at $t=0$: the $D_1t$ term is $0$. Keep the $100$ (forgetting it is the classic slip).', r'100+D_2=200\ \Rightarrow\ D_2=100'),
    S(r'Slope at $0^+$ is $I_0/C=0$. The form has slope $D_1-50D_2$ at $t=0$ (product rule).', r'D_1-50(100)=0\ \Rightarrow\ D_1=5000'),
], r'$v_o(t)=100+(5000t+100)\,e^{-50t}$ V: from $200$ V down to $100$ V with no overshoot', cites=D.tb('8.53'))

D.EX('Parallel, underdamped (textbook 8.7)', r"""Source-free parallel RLC:
- **Parts:** $R=12\,500/3\,\Omega$, $L=250\,\mathrm{mH}$, $C=10\,\mathrm{nF}$
- **Start:** $V_0=v(0)=90\,\mathrm{V}$, $I_0=i_L(0)=-30\,\mathrm{mA}$

Find $v(t)$.

""" + par(r'$10\,\mathrm{nF}$', r'$250\,\mathrm{mH}$', r'$R$'), [
    S(r'Parallel uses $\alpha=1/(2RC)$; dividing by $12\,500/3$ puts the $3$ on top.', r'\alpha=\frac{3}{2(12\,500)(10^{-8})}=12\,000\ \mathrm{s^{-1}}'),
    S(r'$\omega_0$ is bigger than $\alpha$: underdamped.',
      r'\omega_0=\frac{1}{\sqrt{(0.25)(10^{-8})}}=20\,000,\qquad \omega_d=\sqrt{20\,000^2-12\,000^2}=16\,000\ \mathrm{rad/s}'),
    S(r'Underdamped form (no source, so no $V$); at $t=0$ it gives $B_1=V_0$.', r'v=e^{-12\,000t}(B_1\cos16\,000t+B_2\sin16\,000t),\quad B_1=90'),
    S(r'Slope from KCL ($i_C+i_L+i_R=0$). $I_0$ is $-30$ mA, so $-I_0=+0.03$: watch the sign.', r'i_C(0^+)=-\frac{90}{12\,500/3}+0.03=0.0084\ \mathrm{A}'),
    S(r'Starting slope $i_C/C=8.4\times10^5$ V/s. The form has slope $-\alpha B_1+\omega_dB_2$ at $t=0$.',
      r'-12\,000(90)+16\,000B_2=8.4\times10^5\ \Rightarrow\ B_2=120'),
], r'$v(t)=e^{-12\,000t}(90\cos16\,000t+120\sin16\,000t)$ V', cites=D.tb('8.7'))

D.PR('No resistor (textbook 8.14)', r"""Remove the resistor: $C=250\,\mathrm{mF}$ in parallel with $L=0.4\,\mathrm{H}$. The start:
- $v(0)=0$
- $i_L(0)=-3\,\mathrm{A}$ (drawn downward)

""" + par(r'$250\,\mathrm{mF}$', r'$0.4\,\mathrm{H}$') + r"""

Find $v(t)$, its frequency in rad/s and its amplitude.""", [
    S(r'No $R$ means no $\frac{1}{RC}$ term, so $\alpha=0$. And $LC=0.4\cdot0.25=0.1$.', r"v''+10v=0\ \Rightarrow\ s=\pm j\sqrt{10}"),
    S(r'$\sigma=0$: the envelope is $e^{0t}=1$. $v(0)=0$ removes the cosine.', r'v=B_2\sin\sqrt{10}\,t'),
    S(r"KCL with two branches gives $i_C(0)=-i_L(0)=3$ A. The slope is $i_C/C$; the form's slope at $0$ is $\sqrt{10}\,B_2$.",
      r"v'(0)=\frac{3}{0.25}=12=\sqrt{10}\,B_2\ \Rightarrow\ B_2=\frac{12}{\sqrt{10}}\approx3.795\ \mathrm{V}"),
], r"""$v=3.795\sin(3.162\,t)$ V
- frequency $\sqrt{10}\approx3.162$ rad/s
- amplitude $3.795$ V
- it never dies out""", diff='intermediate', cites=D.tb('8.14'))

D.PR('From the response back to the circuit (textbook 8.2)', r"""In this source-free parallel RLC:
- $C=18\,\mu\mathrm{F}$
- $v(t)=-12\left(e^{-200t}+e^{-1800t}\right)$ V for $t\ge0$

Find $R$ and $i_L(0^+)$.

""" + par(r'$18\,\mu\mathrm{F}$', r'$L$', r'$R$'), [
    S(r'The exponents are the roots $-200$, $-1800$. Rebuild the characteristic equation and match it to $s^2+\frac{1}{RC}s+\frac{1}{LC}$.',
      r'(s+200)(s+1800)=s^2+2000s+360\,000'),
    S(r'So $\frac{1}{RC}=2000$.', r'R=\frac{1}{2000\,(18\times10^{-6})}\approx27.78\ \Omega'),
    S(r"Read the start off $v(t)$ ($\frac{d}{dt}e^{st}=se^{st}$), then $i_C=Cv'$ and $i_R=v/R$.",
      r"v(0)=-24\ \mathrm{V},\qquad v'(0)=-12(-200-1800)=24\,000\ \mathrm{V/s}\qquad i_C=0.432\ \mathrm{A},\quad i_R=-0.864\ \mathrm{A}"),
    S(r'KCL: $i_L=-i_C-i_R$.', r'i_L(0^+)=-0.432+0.864=0.432\ \mathrm{A}'),
], r'$R\approx27.78\,\Omega$, $i_L(0^+)=432$ mA', diff='intermediate', cites=D.tb('8.2'))

check_schematics(D.B)
D.save()
