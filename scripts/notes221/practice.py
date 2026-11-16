r"""ELEC 221 Midterm 2 Practice Questions (2026-11-14): 12 test-style questions, 4 per topic note.

Scope from the posted midterm announcement: textbook 6.1-6.3, 7.1-7.5, 8.1-8.3 (parallel RLC only).
Questions 1-8 and 9, 11, 12 were the end-of-note practice of ch6/ch7/ch8 (moved here, made standalone);
question 10 is new (a parallel RLC whose starting values come from a DC circuit before the switch).
Every number is computed and checked with near(); RLC answers are checked against their ODE.
"""
import math

from lib221 import Doc, S, cite, near, sch

E, LN, SQ = math.exp, math.log, math.sqrt
D = Doc('practice', 'Midterm 2 Practice Questions', ['inductance', 'capacitance', 'rl_circuits', 'rc_circuits',
                                                     'rlc_circuits'])

# ------------------------------------------------------------------------------------------ numbers
# Q1 = Tutorial 6 Q3 = AP 6.1: L = 50 uH, i = 18 t e^{-10t}
v02 = 0.9e-3 * E(-2) * (1 - 2); i02 = 18 * 0.2 * E(-2)
near(v02 * 1e6, -121.8); near(i02 * 1e3, 487.2); near(v02 * i02 * 1e6, -59.34, rel=3e-3)
imax = 18 * 0.1 * E(-1); near(imax * 1e3, 662.2)
# Q2 = AP 6.5
q = 0.05 / 200; near(q / 20e-6, 12.5); near(q / 100e-6, 2.5); near(q / 25e-6, 10)
near(0.5 * 100e-6 * 17.5 ** 2 * 1e3, 15.3125)
# Q3 / Q4 (own)
near(2e-3 * 1e-3 / 0.5e-6, 4); near(4 - 1e-3 * 2e-3 / 0.5e-6, 0); near(0.5 * 0.5e-6 * 16 * 1e6, 4)
near(30 / 15 * 10, 20); near(30 / 15, 2); near(0.5 * 2 * 4, 4); near(0.5 * 50e-6 * 400 * 1e3, 10)
# Q5 = Week 8 Tutorial Q1
near(30e-3 * 1e3 / 10e3, 3e-3)
Lq1 = 10 / (1000 * LN(2)); near(Lq1 * 1e3, 14.43, rel=3e-3); near(1 - E(-2 * 1e-3 / (Lq1 / 10)), 0.75)
# Q6 = AP 7.5
near((30 - 250) / 55e3 * 1e3, -4); near(0.2 / 30e3 * 1e6, 6.667, rel=3e-3)
# Q7 = Week 8 Tutorial Q3
near(1.25 + 10 * 6 / 16, 5); near(3.75 / 5 * 15000, 11250); near(11250 / (6 * 1500), 1.25)
# Q8 = AP 7.9
v20 = 40 * E(-2)
w20k = 1600 / 20e3 / 200 * (1 - E(-4)) + v20 ** 2 / 20e3 / 250; near(w20k * 1e6, 398.5, rel=3e-3)
w80k = v20 ** 2 / 80e3 / 250; near(w80k * 1e6, 1.465, rel=3e-3); near(w20k + w80k, 0.5 * 0.5e-6 * 1600)


def solve(alpha, w0, x0, dx0, xf=0.0):
    d = alpha ** 2 - w0 ** 2
    if abs(d) < 1e-9 * w0 ** 2:
        D2 = x0 - xf; D1 = dx0 + alpha * D2
        return 'crit', (D1, D2), lambda t: xf + (D1 * t + D2) * E(-alpha * t)
    if d > 0:
        s1, s2 = -alpha + SQ(d), -alpha - SQ(d)
        A2 = (dx0 - s1 * (x0 - xf)) / (s2 - s1); A1 = x0 - xf - A2
        return 'over', (s1, s2, A1, A2), lambda t: xf + A1 * E(s1 * t) + A2 * E(s2 * t)
    wd = SQ(-d); B1 = x0 - xf; B2 = (dx0 + alpha * B1) / wd
    return 'under', (wd, B1, B2), lambda t: xf + E(-alpha * t) * (B1 * math.cos(wd * t) + B2 * math.sin(wd * t))


def ode_ok(f, alpha, w0, xf, ts=(1e-5, 1e-4, 3e-4)):
    for t in ts:
        h = 1e-4 / max(alpha, w0)
        d1 = (f(t + h) - f(t - h)) / (2 * h); d2 = (f(t + h) - 2 * f(t) + f(t - h)) / h ** 2
        res = d2 + 2 * alpha * d1 + w0 ** 2 * (f(t) - xf)
        assert abs(res) <= 1e-3 * (abs(d2) + abs(2 * alpha * d1) + abs(w0 ** 2 * (f(t) - xf))) + 1e-6, res


# Q9 = AP 8.4
near(1 / ((300 ** 2 + 400 ** 2) * 250e-6) * 1e3, 16); near(1 / (2 * 400 * 250e-6), 5)
near(250e-6 * (-400 * 120 + 300 * 80), -6); near(-120 / 5 - (-6), -18)
# Q10 (own): 30 mA source disconnected at t=0 from C = 0.2 uF || L = 50 mH || R = 312.5
a10 = 1 / (2 * 312.5 * 0.2e-6); w010 = 1 / SQ(0.05 * 0.2e-6); near(a10, 8000); near(w010, 1e4)
case, (wd10, B110, B210), f10 = solve(a10, w010, 0, -0.03 / 0.2e-6)
assert case == 'under'; near(wd10, 6000); near(B110, 0, abs_=1e-9); near(B210, -25); ode_ok(f10, a10, w010, 0)
near(-25 / 312.5 * 1e3, -80)
# Q11 = AP 8.3 (branch currents of AP 8.2's v = -63.33 e^{-1000t} + 53.33 e^{-4000t})
case, (s1b, s2b, A1b, A2b), _ = solve(2500, 2000, -10, -(8e-3 - 10 / 5e3) / 40e-9)
near(A1b, -63.33); near(A2b, 53.33)
iR = (A1b / 5, A2b / 5); iC = (40e-9 * -1000 * A1b * 1e3, 40e-9 * -4000 * A2b * 1e3)
iL = (-(iR[0] + iC[0]), -(iR[1] + iC[1]))
near(iR[0], -12.67); near(iR[1], 10.67); near(iC[0], 2.533); near(iC[1], -8.533)
near(iL[0], 10.133); near(iL[1], -2.133); near(iL[0] + iL[1], 8)
# Q12 = Eren W9 p9 (Nilsson 8.8): I = 24 mA, L = 25 mH, C = 25 nF, R = 500, I0 = 29 mA, V0 = 50 V
case, (D1e, D2e), fE = solve(40000, 40000, 0.029, 50 / 0.025, xf=0.024)
assert case == 'crit'; near(D1e, 2200); near(D2e, 0.005); ode_ok(fE, 40000, 40000, 0.024, ts=(1e-6, 2e-5, 6e-5))
vE = lambda t: 0.025 * (fE(t + 1e-9) - fE(t - 1e-9)) / 2e-9
near(vE(1e-5), (50 - 2.2e6 * 1e-5) * E(-0.4), rel=1e-3)

# ==================================================================================================== intro
D.P(r'**Midterm 2 · 12 test-style questions.** Four per note, in the same order as the notes. ★ = a problem from your lectures, tutorials or Assessment Problems (the profs reuse these, so do those first).')
D.P(r'Each answer ends with where to review if you got stuck. The real formula sheet gets posted on OnQ next week; until then use the **Formula summary** at the end of each note.')
D.P(r'**Name the question before you solve it.** It is almost always one of these:')
D.T(['You see…', 'It is…', 'First move', 'Note'],
    [[r'$i(t)$ or $v(t)$ of one $L$/$C$', r'$v$–$i$, power, energy', r'differentiate / integrate + start value', '1 · A'],
     [r'several $L$s or $C$s', 'combine', 'equivalent + add the starting values', '1 · B'],
     [r'switch, one $L$ or $C$, no source after', 'natural response', r'Before, $\tau$, Plug in', '2 · B'],
     [r'switch, one $L$ or $C$, source after', 'step response', 'the six steps (Thévenin if messy)', '2 · C'],
     ['two switch times', 'sequential switching', 'window, hand-off, restart the clock', '2 · D'],
     [r'$R$, $L$, $C$ all in parallel', 'parallel RLC', r'$\alpha$ vs $\omega_0$, then two starting values', '3']])

# ==================================================================================================== 1
D.H('Inductors and capacitors (note 1)')
D.Q('★ Tutorial 6 Q3 = AP 6.1: inductor, all parts',
    r'''The current in a $50\,\mu\mathrm{H}$ inductor is $i=18te^{-10t}\ \mathrm{A}$ for $t\ge0$ (passive sign convention).

(a) Find $v$ for $t>0$. (b) Find the power at $t=200\,\mathrm{ms}$. (c) Is the inductor absorbing or delivering then? (d) Find the stored energy at $200\,\mathrm{ms}$. (e) Find the maximum stored energy and when it happens.''',
    [S(r'**Differentiate** (product rule), then multiply by $L$.',
       (r'\frac{di}{dt}=18e^{-10t}(1-10t)', r'v=50\times10^{-6}\cdot18e^{-10t}(1-10t)=0.9e^{-10t}(1-10t)\ \mathrm{mV}')),
     S(r'**Plug in** $t=0.2\,\mathrm{s}$, so $10t=2$.',
       (r'i=18(0.2)e^{-2}=' + f'{i02 * 1e3:.1f}' + r'\,\mathrm{mA}', r'v=0.9e^{-2}(1-2)\,\mathrm{mV}=' + f'{v02 * 1e6:.1f}' + r'\,\mu\mathrm{V}')),
     S(r'**Power (b, c).** It is negative, so the inductor is delivering.', r'p=vi=' + f'{v02 * i02 * 1e6:.2f}' + r'\,\mu\mathrm{W}'),
     S(r'**Energy (d).**', r'w=\tfrac12(50\times10^{-6})(' + f'{i02:.4f}' + r')^2=' + f'{0.5 * 50e-6 * i02 ** 2 * 1e6:.2f}' + r'\,\mu\mathrm{J}'),
     S(r'**Max (e).** $\dfrac{di}{dt}=0$ when $1-10t=0$.',
       (r't=0.1\,\mathrm{s}=100\,\mathrm{ms}', r'i_{\max}=18(0.1)e^{-1}=' + f'{imax * 1e3:.1f}' + r'\,\mathrm{mA}',
        r'w_{\max}=\tfrac12(50\times10^{-6})(' + f'{imax:.4f}' + r')^2=' + f'{0.5 * 50e-6 * imax ** 2 * 1e6:.2f}' + r'\,\mu\mathrm{J}')),
     S(r'**Review:** note 1, A1 and A3.')],
    r'(a) $0.9e^{-10t}(1-10t)\,\mathrm{mV}$ (b) $' + f'{v02 * i02 * 1e6:.2f}' + r'\,\mu\mathrm{W}$ (c) delivering (d) $'
    + f'{0.5 * 50e-6 * i02 ** 2 * 1e6:.2f}' + r'\,\mu\mathrm{J}$ (e) $' + f'{0.5 * 50e-6 * imax ** 2 * 1e6:.2f}' + r'\,\mu\mathrm{J}$ at $100\,\mathrm{ms}$',
    cites=cite('T6', 6))
D.Q('★ AP 6.5: two capacitors in series',
    r'''A $100\,\mu\mathrm{F}$ capacitor ($v_1(0)=15\,\mathrm{V}$) and a $25\,\mu\mathrm{F}$ capacitor ($v_2(0)=-10\,\mathrm{V}$) are in series. For $t\ge0$ the current $i=0.05e^{-200t}\ \mathrm{A}$ flows into the $+$ end of $v$.

''' + sch(r'''
X1 0,4 -> 0,0 "rest of circuit" i="$i$" i_rev
wire 0,4 -> 3,4
C1 3,4 -> 3,2 "$100\,\mu\mathrm{F}$" v="$v_1$"
C2 3,2 -> 3,0 "$25\,\mu\mathrm{F}$" v="$v_2$"
wire 3,0 -> 0,0
gap 5,4 -> 5,0 v="$v$"
wire 3,4 -> 5,4
wire 3,0 -> 5,0
''') + r'''

Find (a) $C_{eq}$, (b) $v(0)$, (c) $v(t)$, (d) $v_1(t)$ and $v_2(t)$, (e) the energy left in the capacitors as $t\to\infty$.''',
    [S(r'**Combine.**', r'C_{eq}=\frac{100\cdot25}{125}=20\,\mu\mathrm{F}'),
     S(r'**Start:** add the starting voltages.', r'v(0)=15+(-10)=5\,\mathrm{V}'),
     S(r'**Integrate** the current once.', r'\int_0^t0.05e^{-200\tau}\,d\tau=2.5\times10^{-4}\left(1-e^{-200t}\right)'),
     S(r'**Total voltage (c).**', (r'v=\frac{2.5\times10^{-4}}{20\times10^{-6}}\left(1-e^{-200t}\right)+5', r'v=17.5-12.5e^{-200t}\ \mathrm{V}')),
     S(r'**Each capacitor (d):** own $C$, own start.',
       (r'v_1=2.5\left(1-e^{-200t}\right)+15=17.5-2.5e^{-200t}\ \mathrm{V}', r'v_2=10\left(1-e^{-200t}\right)-10=-10e^{-200t}\ \mathrm{V}')),
     S(r'**Energy left (e).** As $t\to\infty$: $v_1=17.5\,\mathrm{V}$, $v_2=0$.', r'w=\tfrac12(100\times10^{-6})(17.5)^2=15.31\,\mathrm{mJ}'),
     S(r'**Review:** note 1, B1.')],
    r'(a) $20\,\mu\mathrm{F}$ (b) $5\,\mathrm{V}$ (c) $17.5-12.5e^{-200t}\,\mathrm{V}$ (d) $v_1=17.5-2.5e^{-200t}$, $v_2=-10e^{-200t}\,\mathrm{V}$ (e) $15.31\,\mathrm{mJ}$',
    cites=cite('AP6', 2, 3))
D.Q('Capacitor charged by a current pulse',
    r'A $0.5\,\mu\mathrm{F}$ capacitor starts uncharged. The current into its $+$ end is $2\,\mathrm{mA}$ for $0<t<1\,\mathrm{ms}$, then $-1\,\mathrm{mA}$ for $1<t<3\,\mathrm{ms}$, then $0$. (a) Find $v$ at $1\,\mathrm{ms}$ and at $3\,\mathrm{ms}$. (b) What is the largest stored energy? (c) When is the capacitor delivering power?',
    [S(r'**First piece:** constant current, start at $0$.', r'v(1\,\mathrm{ms})=\frac{2\times10^{-3}\cdot10^{-3}}{0.5\times10^{-6}}+0=4\,\mathrm{V}'),
     S(r'**Second piece:** start from $4\,\mathrm{V}$, current now negative for $2\,\mathrm{ms}$.', r'v(3\,\mathrm{ms})=4+\frac{(-10^{-3})(2\times10^{-3})}{0.5\times10^{-6}}=0\,\mathrm{V}'),
     S(r'**Max energy** is at the largest $|v|$, which is $4\,\mathrm{V}$ at $1\,\mathrm{ms}$.', r'w_{\max}=\tfrac12(0.5\times10^{-6})(4)^2=4\,\mu\mathrm{J}'),
     S(r'**Delivering** means $p=vi<0$. For $1<t<3\,\mathrm{ms}$, $v>0$ and $i<0$.'),
     S(r'**Review:** note 1, A2 and A3.')],
    r'(a) $4\,\mathrm{V}$, $0\,\mathrm{V}$ (b) $4\,\mu\mathrm{J}$ (c) for $1<t<3\,\mathrm{ms}$', diff='introductory')
D.Q('DC circuit with both $L$ and $C$',
    r'''The circuit has been on for a long time. Find $i_L$, $v_C$, and the energy stored in each element.

''' + sch(r'''
V1 0,3 -> 0,0 "$30\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\Omega$"
L1 3,3 -> 6,3 "$2\,\mathrm{H}$" i="$i_L$"
R2 6,3 -> 6,0 "$10\,\Omega$"
wire 6,3 -> 9,3
C1 9,3 -> 9,0 "$50\,\mu\mathrm{F}$" v="$v_C$"
wire 9,0 -> 0,0
ground 0,0
'''),
    [S(r'**Replace** $L$ by a wire and $C$ by a gap.'),
     S(r'**Solve** the loop that is left: $5\,\Omega$ and $10\,\Omega$ in series.', r'i_L=\frac{30}{5+10}=2\,\mathrm{A}'),
     S(r'**Read** $v_C$: it sits across the $10\,\Omega$.', r'v_C=2\cdot10=20\,\mathrm{V}'),
     S(r'**Energies.**', (r'w_L=\tfrac12(2)(2)^2=4\,\mathrm{J}', r'w_C=\tfrac12(50\times10^{-6})(20)^2=10\,\mathrm{mJ}')),
     S(r'**Review:** note 1, A4.')],
    r'$i_L=2\,\mathrm{A}$, $v_C=20\,\mathrm{V}$, $w_L=4\,\mathrm{J}$, $w_C=10\,\mathrm{mJ}$', diff='introductory')

# ==================================================================================================== 2
D.H('RL and RC circuits (note 2)')
D.Q('★ Week 8 Tutorial Q1: start value, choose $L$, energy %',
    r'''The switch has been closed for a long time and opens at $t=0$. After that, $L$ discharges into the $10\,\Omega$ alone.

''' + sch(r'''
I1 0,0 -> 0,3 "$30\,\mathrm{mA}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$1\,\mathrm{k\Omega}$"
S1 3,3 -> 5,3 "$t=0$" state=closed action=open
R2 5,3 -> 8,3 "$9\,\mathrm{k\Omega}$"
R3 8,3 -> 8,0 "$10\,\Omega$"
wire 8,3 -> 11,3
L1 11,3 -> 11,0 "$L$" i="$i_L$" v="$v_o$"
wire 11,0 -> 0,0
ground 0,0
''') + r'''

(a) Find $i_L(0^-)$. (b) Find $L$ so that $v_o(1\,\mathrm{ms})=0.5\,v_o(0^+)$. (c) What percentage of the stored energy has gone into the $10\,\Omega$ by $t=1\,\mathrm{ms}$?''',
    [S(r'**Before (a):** $L$ is a wire, so it shorts the $10\,\Omega$. The $30\,\mathrm{mA}$ splits between $1\,\mathrm{k}$ and the $9\,\mathrm{k}$ path.',
       r'i_L(0^-)=30\,\mathrm{mA}\cdot\frac{1\,\mathrm{k}}{1\,\mathrm{k}+9\,\mathrm{k}}=3\,\mathrm{mA}'),
     S(r'**Half after 1 ms (b):** $v_o$ decays as $e^{-t/\tau}$ with $\tau=\dfrac{L}{10}$.',
       (r'e^{-0.001/\tau}=0.5', r'\tau=\frac{0.001}{\ln2}=1.443\,\mathrm{ms}', r'L=10\,\tau=' + f'{Lq1 * 1e3:.2f}' + r'\,\mathrm{mH}')),
     S(r'**Energy % (c):** the $10\,\Omega$ is the only resistor, so it gets everything that leaves. Power goes as $e^{-2t/\tau}$, and $e^{-t/\tau}=0.5$ at $1\,\mathrm{ms}$.',
       r'\frac{w_{10\Omega}}{w(0)}=1-e^{-2t/\tau}=1-(0.5)^2=75\%'),
     S(r'**Review:** note 2, A1 and B.')],
    r'(a) $3\,\mathrm{mA}$ (b) $L=' + f'{Lq1 * 1e3:.2f}' + r'\,\mathrm{mH}$ (c) $75\%$', cites=cite('T8', 1, 2, 3))
D.Q('★ AP 7.5: RL step',
    r'''The circuits below are already simplified (source transformations done). Before $t=0$:

''' + sch(r'''
V1 0,3 -> 0,0 "$250\,\mathrm{V}$"
R1 0,3 -> 3,3 "$25\,\mathrm{k\Omega}$"
L1 6,3 -> 3,3 "$200\,\mathrm{mH}$" i="$i$"
R2 9,3 -> 6,3 "$30\,\mathrm{k\Omega}$"
V2 9,3 -> 9,0 "$30\,\mathrm{V}$"
wire 9,0 -> 0,0
''') + r'''

After $t=0$ the left part is replaced by a wire:

''' + sch(r'''
wire 3,3 -> 3,0
L1 6,3 -> 3,3 "$200\,\mathrm{mH}$" i="$i$"
R2 9,3 -> 6,3 "$30\,\mathrm{k\Omega}$"
V2 9,3 -> 9,0 "$30\,\mathrm{V}$"
wire 9,0 -> 3,0
''') + r'''

Find (a) $i(0^+)$, (b) $i(\infty)$, (c) $\tau$, (d) $i(t)$.''',
    [S(r'**Before:** $L$ is a wire. One loop; the $30\,\mathrm{V}$ pushes $i$ its way, the $250\,\mathrm{V}$ pushes against it.', r'i(0^-)=\frac{30-250}{25\,\mathrm{k}+30\,\mathrm{k}}=-4\,\mathrm{mA}'),
     S(r'**Jump.**', r'i(0^+)=-4\,\mathrm{mA}'),
     S(r'**After.**', r'i(\infty)=\frac{30}{30\,\mathrm{k}}=1\,\mathrm{mA}'),
     S(r'**$\tau$.**', r'\tau=\frac{0.2}{30\,000}=6.67\,\mu\mathrm{s}'),
     S(r'**Plug in.**', r'i(t)=1+(-4-1)e^{-150\,000t}=1-5e^{-150\,000t}\ \mathrm{mA}'),
     S(r'**Review:** note 2, C1.')],
    r'(a) $-4\,\mathrm{mA}$ (b) $1\,\mathrm{mA}$ (c) $6.67\,\mu\mathrm{s}$ (d) $1-5e^{-150\,000t}\,\mathrm{mA}$', cites=cite('AP7', 4))
D.Q('★ Week 8 Tutorial Q3: two switches, three inductors',
    r'''Both switches have been in place for a long time and move together at $t=0$: the top switch moves from $a$ to $b$, and the bottom one closes.

''' + sch(r'''
R1 0,4 -> 0,0 "$10\,\Omega$"
wire 0,4 -> 2,4
I1 2,4 -> 2,0 "$2\,\mathrm{A}$"
wire 2,4 -> 4,4
S1 4,4 -> 6,4 "$a$" state=closed action=open
S2 8,4 -> 6,4 "$b$" action=close
R2 8,4 -> 8,0 "$7.5\,\mathrm{k\Omega}$"
L1 6,4 -> 6,2 "$1.25\,\mathrm{H}$"
L2 6,2 -> 6,0 "$10\,\mathrm{H}$" v="$v_o$"
S3 6,2 -> 4,2 "$t=0$" action=close
L3 4,0 -> 4,2 "$6\,\mathrm{H}$" i="$i_o$"
wire 8,0 -> 0,0
ground 0,0
''') + r'''

Find (a) $v_o(t)$ and (b) $i_o(t)$ for $t\ge0$.''',
    [S(r'**Before:** inductors are wires, so they short the $10\,\Omega$. The whole $2\,\mathrm{A}$ runs up through the $10\,\mathrm{H}$ and $1.25\,\mathrm{H}$. The $6\,\mathrm{H}$ is disconnected.',
       (r'i_{1.25}(0)=2\,\mathrm{A}\ \text{(upward)}', r'i_o(0)=0')),
     S(r'**Combine** the inductors the resistor sees.', r'L_{eq}=1.25+10\parallel6=5\,\mathrm{H}'),
     S(r'**$\tau$** and the current through the $7.5\,\mathrm{k}$ (no source, so natural response).', (r'\tau=\frac{5}{7500}=\frac{1}{1500}\,\mathrm{s}', r'i=2e^{-1500t}\ \mathrm{A}')),
     S(r'**Resistor voltage**, then the share across $10\parallel6=3.75\,\mathrm{H}$ (voltages split like the inductances).',
       (r'v_{7.5k}=7500\cdot2e^{-1500t}=15000e^{-1500t}\ \mathrm{V}', r'v_o=\frac{3.75}{5}\cdot15000e^{-1500t}=11250e^{-1500t}\ \mathrm{V}')),
     S(r'**Other (b):** $i_o$ points into the $-$ end of $v_o$, so use a minus. Start at $0$.',
       (r'i_o=-\frac16\int_0^t11250e^{-1500\tau}\,d\tau+0', r'i_o=1.25e^{-1500t}-1.25\ \mathrm{A}')),
     S(r'**Review:** note 2, A2 and B; note 1, A1 (the integral).')],
    r'(a) $v_o=11250e^{-1500t}\,\mathrm{V}$ (b) $i_o=1.25e^{-1500t}-1.25\,\mathrm{A}$', cites=cite('T8', 6, 7, 8))
D.Q('★ AP 7.9: sequential RC with energy',
    r'''Before $t=0$ (long time) the $0.5\,\mu\mathrm{F}$ capacitor is across $20\,\mathrm{k}\parallel60\,\mathrm{k}$, fed from $80\,\mathrm{V}$ through $15\,\mathrm{k}$:

''' + sch(r'''
V1 0,3 -> 0,0 "$80\,\mathrm{V}$"
R1 0,3 -> 3,3 "$15\,\mathrm{k\Omega}$"
R2 3,3 -> 3,0 "$60\,\mathrm{k\Omega}$"
wire 3,3 -> 6,3
C1 6,3 -> 6,0 "$0.5\,\mu\mathrm{F}$" v="$v_C$"
wire 6,3 -> 9,3
R3 9,3 -> 9,0 "$20\,\mathrm{k\Omega}$"
wire 9,0 -> 0,0
''') + r'''

For $0\le t\le20\,\mathrm{ms}$ the capacitor is connected only to the $20\,\mathrm{k\Omega}$. For $t\ge20\,\mathrm{ms}$ an $80\,\mathrm{k\Omega}$ resistor is added in parallel. Find (a) $v_C$ in the first window, (b) $v_C$ for $t\ge20\,\mathrm{ms}$, (c) the energy dissipated in the $20\,\mathrm{k}$ and (d) in the $80\,\mathrm{k}$.''',
    [S(r'**Before:** divider, with $20\parallel60=15\,\mathrm{k}$ against $15\,\mathrm{k}$.', r'v_C(0)=80\cdot\frac{15}{15+15}=40\,\mathrm{V}'),
     S(r'**Window 1 (a).**', (r'\tau_1=(20\,\mathrm{k})(0.5\,\mu)=10\,\mathrm{ms}', r'v_C=40e^{-100t}\ \mathrm{V}')),
     S(r'**Hand-off** at $20\,\mathrm{ms}$.', r'v_C(0.02)=40e^{-2}=' + f'{v20:.3f}' + r'\,\mathrm{V}'),
     S(r'**Window 2 (b).** $80\parallel20=16\,\mathrm{k}$.', (r'\tau_2=(16\,\mathrm{k})(0.5\,\mu)=8\,\mathrm{ms}', r'v_C=' + f'{v20:.3f}' + r'\,e^{-125(t-0.02)}\ \mathrm{V}')),
     S(r'**Energy in $20\,\mathrm{k}$ (c):** both windows, power $\dfrac{v^2}{R}$.',
       (r'w=\int_0^{0.02}\frac{1600e^{-200t}}{20\,000}dt+\int_{0.02}^{\infty}\frac{' + f'{v20:.3f}' + r'^2e^{-250(t-0.02)}}{20\,000}dt',
        r'=' + f'{1600 / 20e3 / 200 * (1 - E(-4)) * 1e6:.1f}' + '+' + f'{v20 ** 2 / 20e3 / 250 * 1e6:.2f}' + '=' + f'{w20k * 1e6:.1f}' + r'\,\mu\mathrm{J}')),
     S(r'**Energy in $80\,\mathrm{k}$ (d):** window 2 only.', r'w=\frac{' + f'{v20:.3f}' + r'^2}{80\,000\cdot250}=' + f'{w80k * 1e6:.1f}' + r'\,\mu\mathrm{J}'),
     S(r'**Check:** together they must equal the starting energy.', r'\tfrac12(0.5\,\mu)(40)^2=400\,\mu\mathrm{J}=' + f'{w20k * 1e6:.1f}' + '+' + f'{w80k * 1e6:.1f}' + r'\ \checkmark'),
     S(r'**Review:** note 2, B (energy) and D (sequential).')],
    r'(a) $40e^{-100t}\,\mathrm{V}$ (b) $' + f'{v20:.3f}' + r'\,e^{-125(t-0.02)}\,\mathrm{V}$ (c) $' + f'{w20k * 1e6:.1f}' + r'\,\mu\mathrm{J}$ (d) $' + f'{w80k * 1e6:.1f}' + r'\,\mu\mathrm{J}$',
    cites=cite('AP7', 7, 8))

# ==================================================================================================== 3
D.H('Parallel RLC circuits (note 3)')
D.Q('★ AP 8.4: work backwards from $v(t)$',
    r'The natural response of a parallel RLC with $C=250\,\mu\mathrm{F}$ is $v(t)=e^{-400t}\left(120\cos300t+80\sin300t\right)\ \mathrm{V}$. Find (a) $L$, (b) $R$, (c) $V_0$, (d) $I_0$ (inductor current, down).',
    [S(r'**Read** $\alpha=400$ and $\omega_d=300$ from the formula.'),
     S(r'**(a)** $\omega_0^2=\omega_d^2+\alpha^2$, then $L=\dfrac{1}{\omega_0^2C}$.', (r'\omega_0^2=300^2+400^2=250\,000', r'L=\frac{1}{250\,000(250\times10^{-6})}=16\,\mathrm{mH}')),
     S(r'**(b)** From $\alpha=\dfrac{1}{2RC}$.', r'R=\frac{1}{2(400)(250\times10^{-6})}=5\,\Omega'),
     S(r'**(c)** Set $t=0$: $\cos=1$, $\sin=0$.', r'V_0=120\,\mathrm{V}'),
     S(r'**(d)** Slope at $0$ is $-\alpha B_1+\omega_dB_2$. Then $i_C=C\dfrac{dv}{dt}$ and KCL.',
       (r'\frac{dv}{dt}(0)=-400(120)+300(80)=-24\,000\ \mathrm{V/s}', r'i_C(0)=250\times10^{-6}(-24\,000)=-6\,\mathrm{A},\qquad i_R(0)=\frac{120}{5}=24\,\mathrm{A}',
        r'I_0=-i_R-i_C=-24+6=-18\,\mathrm{A}')),
     S(r'**Review:** note 3, A and B.')],
    r'(a) $16\,\mathrm{mH}$ (b) $5\,\Omega$ (c) $120\,\mathrm{V}$ (d) $-18\,\mathrm{A}$', cites=cite('AP8', 2))
D.Q('Starting values from the circuit before the switch',
    r'''The switch has been closed for a long time. At $t=0$ it opens and disconnects the source.

''' + sch(r'''
I1 0,0 -> 0,3 "$30\,\mathrm{mA}$"
S1 0,3 -> 3,3 "$t=0$" state=closed action=open
wire 3,3 -> 6,3 -> 9,3
C1 3,3 -> 3,0 "$0.2\,\mu\mathrm{F}$" v="$v$"
L1 6,3 -> 6,0 "$50\,\mathrm{mH}$" i="$i_L$"
R1 9,3 -> 9,0 "$312.5\,\Omega$" i="$i_R$"
wire 9,0 -> 0,0
''') + r'''

Find (a) $V_0$ and $I_0$, (b) the shape and the roots, (c) $\dfrac{dv}{dt}(0^+)$, (d) $v(t)$ and $i_R(t)$ for $t\ge0$.''',
    [S(r'**Before (a):** DC, so $L$ is a wire. It shorts $C$ and $R$: they get $0\,\mathrm{V}$, and the whole source current goes down the inductor.',
       r'V_0=v(0^-)=0,\qquad I_0=i_L(0^-)=30\,\mathrm{mA}'),
     S(r'**Shape (b).** $\alpha<\omega_0$: underdamped.',
       (r'\alpha=\frac{1}{2(312.5)(0.2\times10^{-6})}=8000,\qquad \omega_0=\frac{1}{\sqrt{0.05(0.2\times10^{-6})}}=10\,000',
        r'\omega_d=\sqrt{10\,000^2-8000^2}=6000,\qquad s_{1,2}=-8000\pm j6000\ \mathrm{rad/s}')),
     S(r'**Start slope (c).** KCL at the top node with the source gone; $i_R(0^+)=0$ because $v(0^+)=0$.',
       (r'i_C(0^+)=-I_0-\frac{V_0}{R}=-30\,\mathrm{mA}', r'\frac{dv}{dt}(0^+)=\frac{-0.03}{0.2\times10^{-6}}=-150\,000\ \mathrm{V/s}')),
     S(r'**Constants.**', (r'B_1=v(0^+)=0', r'-8000(0)+6000\,B_2=-150\,000\quad\Longrightarrow\quad B_2=-25\ \mathrm{V}')),
     S(r'**Plug in (d).**', (r'v(t)=-25\,e^{-8000t}\sin6000t\ \mathrm{V}', r'i_R=\frac{v}{312.5}=-80\,e^{-8000t}\sin6000t\ \mathrm{mA}')),
     S(r'**Review:** note 3, B; note 1, A4 for the DC step.')],
    r'(a) $V_0=0$, $I_0=30\,\mathrm{mA}$ (b) underdamped, $-8000\pm j6000\,\mathrm{rad/s}$ (c) $-150\,000\,\mathrm{V/s}$ (d) $v=-25e^{-8000t}\sin6000t\,\mathrm{V}$, $i_R=-80e^{-8000t}\sin6000t\,\mathrm{mA}$')
D.Q('★ AP 8.3: branch currents',
    r'A parallel RLC ($R=5\,\mathrm{k\Omega}$, $L=6.25\,\mathrm{H}$, $C=40\,\mathrm{nF}$) has the natural response $v=-63.33e^{-1000t}+53.33e^{-4000t}\ \mathrm{V}$ (this is AP 8.2, Try it in note 3). Find (a) $i_R(t)$, (b) $i_C(t)$, (c) $i_L(t)$, all pointing down.',
    [S(r'**(a) Ohm\'s law.**', r'i_R=\frac{v}{5000}=-12.67e^{-1000t}+10.67e^{-4000t}\ \mathrm{mA}'),
     S(r'**(b)** $i_C=C\dfrac{dv}{dt}$.', (r'\frac{dv}{dt}=63\,330e^{-1000t}-213\,320e^{-4000t}', r'i_C=2.533e^{-1000t}-8.533e^{-4000t}\ \mathrm{mA}')),
     S(r'**(c) KCL:** $i_L=-i_R-i_C$.', r'i_L=10.13e^{-1000t}-2.133e^{-4000t}\ \mathrm{mA}'),
     S(r'**Check:** at $t=0$ this gives $10.13-2.13=8\,\mathrm{mA}$, the given $i_L(0^+)$. (Your solution sheet prints this line with both signs flipped, which would give $-8\,\mathrm{mA}$.)'),
     S(r'**Review:** note 3, B (branch currents).')],
    r'(a) $-12.67e^{-1000t}+10.67e^{-4000t}$ (b) $2.533e^{-1000t}-8.533e^{-4000t}$ (c) $10.13e^{-1000t}-2.133e^{-4000t}$, all in mA',
    cites=cite('AP8', 2))
D.Q('★ Lecture example: step response with stored energy',
    r'''A $24\,\mathrm{mA}$ DC source is switched in at $t=0$ (the switch across it opens). At that instant the inductor carries $I_0=29\,\mathrm{mA}$ (down) and the capacitor has $V_0=50\,\mathrm{V}$.

''' + sch(r'''
I1 0,0 -> 0,3 "$24\,\mathrm{mA}$"
S1 2,3 -> 2,0 "$t=0$" state=closed action=open
wire 0,3 -> 2,3 -> 4,3 -> 7,3 -> 10,3
C1 4,3 -> 4,0 "$25\,\mathrm{nF}$" i="$i_C$" v="$v$"
L1 7,3 -> 7,0 "$25\,\mathrm{mH}$" i="$i_L$"
R1 10,3 -> 10,0 "$500\,\Omega$" i="$i_R$"
wire 10,0 -> 0,0
''') + r'''

Find (a) $i_L(0^+)$, (b) $\dfrac{di_L}{dt}(0^+)$, (c) $i_L(t)$, (d) $v(t)$.''',
    [S(r'**Shape.**', (r'\alpha=\frac{1}{2(500)(25\times10^{-9})}=40\,000,\qquad \omega_0=\frac{1}{\sqrt{(25\times10^{-3})(25\times10^{-9})}}=40\,000', r'\alpha=\omega_0\quad\text{(critically damped)}')),
     S(r'**Start (a, b).**', (r'i_L(0^+)=29\,\mathrm{mA}', r'\frac{di_L}{dt}(0^+)=\frac{V_0}{L}=\frac{50}{0.025}=2000\ \mathrm{A/s}')),
     S(r'**Constants** (in amps). Final value $I=0.024\,\mathrm{A}$.', (r"D_2^{\prime}=0.029-0.024=0.005\,\mathrm{A}", r"D_1^{\prime}=2000+40\,000(0.005)=2200\ \mathrm{A/s}")),
     S(r'**Plug in (c).**', r'i_L=24+2.2\times10^6\,te^{-40\,000t}+5e^{-40\,000t}\ \mathrm{mA}'),
     S(r'**(d)** $v=L\dfrac{di_L}{dt}$ with the product rule.',
       (r'\frac{di_L}{dt}=\left(2200-88\times10^6\,t-200\right)e^{-40\,000t}\ \mathrm{A/s}', r'v=0.025(\dots)=50e^{-40\,000t}-2.2\times10^6\,te^{-40\,000t}\ \mathrm{V}')),
     S(r'**Review:** note 3, C.')],
    r'(a) $29\,\mathrm{mA}$ (b) $2000\,\mathrm{A/s}$ (c) $i_L=24+2.2\times10^6te^{-40000t}+5e^{-40000t}\,\mathrm{mA}$ (d) $v=50e^{-40000t}-2.2\times10^6te^{-40000t}\,\mathrm{V}$',
    cites=cite('E9', 9))

D.save()
