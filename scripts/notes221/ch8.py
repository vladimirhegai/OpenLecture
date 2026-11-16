r"""ELEC 221 Midterm 2 - Ch 8: RLC circuits (Eren W8-W9, Bakhshai W8, Ch 8 Assessment Problems).

Gradual-Parts style: plain-words intro -> overview table -> Part A (which damping), Part B (parallel natural),
Part C (parallel step), Part D (series: same recipe, swap v and i) -> 4 practice questions.
Step words everywhere: Shape, Start, Constants, Plug in (+ Final for step responses).
Every number is computed and checked here (solve() below), and every v(t)/i(t) is checked against its ODE.
"""
import math

from lib221 import Doc, S, cite, near, sch

E, SQ = math.exp, math.sqrt
D = Doc('ch8', 'Midterm 2 · 3. Parallel RLC Circuits', ['rlc_circuits', 'second_order_response'])


def solve(alpha, w0, x0, dx0, xf=0.0):
    """Constants for x(t) = xf + natural part, given x(0+) and x'(0+). Returns (case, consts, func)."""
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


def ode_ok(f, alpha, w0, xf, ts=(1e-5, 3e-4, 1e-3)):
    """x'' + 2 alpha x' + w0^2 x = w0^2 xf, checked numerically."""
    for t in ts:
        h = 1e-4 / max(alpha, w0)
        d1 = (f(t + h) - f(t - h)) / (2 * h); d2 = (f(t + h) - 2 * f(t) + f(t - h)) / h ** 2
        res = d2 + 2 * alpha * d1 + w0 ** 2 * (f(t) - xf)
        assert abs(res) <= 1e-3 * (abs(d2) + abs(2 * alpha * d1) + abs(w0 ** 2 * (f(t) - xf))) + 1e-6, res


# ------------------------------------------------------------------------------------------ numbers
# A: Eren W8 p13 (Nilsson 8.1): L = 50 mH, C = 0.2 uF
L1, C1 = 0.05, 0.2e-6
w01 = 1 / SQ(L1 * C1); near(w01, 1e4)
near(1 / (2 * 200 * C1), 12500); near(1 / (2 * 312.5 * C1), 8000); near(SQ(1e8 - 8000 ** 2), 6000)
near(1 / (2 * w01 * C1), 250); near(0.5 * SQ(L1 / C1), 250)
# AP 8.1: R = 1000, L = 12.5 H, C = 2 uF
near(1 / (2 * 1000 * 2e-6), 250); near(1 / (12.5 * 2e-6), 40000); near(1 / (2 * 1562.5 * 2e-6), 160)
near(1 / (2 * 200 * 2e-6), 1250)
# B over: Eren W8 p16 (Nilsson 8.2): R = 200, v0 = 12, iL0 = 30 mA
dv = -(30e-3 + 12 / 200) / C1; near(dv, -450000)
case, (s1, s2, A1, A2), f = solve(12500, w01, 12, dv); assert case == 'over'
near(s1, -5000); near(s2, -20000); near(A1, -14); near(A2, 26); ode_ok(f, 12500, w01, 0)
# B under: Eren W8 p19 (Nilsson 8.4): C = 0.125 uF, L = 8 H, R = 20k, V0 = 0, I0 = -12.25 mA
a4 = 1 / (2 * 20e3 * 0.125e-6); w04 = 1 / SQ(8 * 0.125e-6); near(a4, 200); near(w04, 1000)
dv4 = 12.25e-3 / 0.125e-6; near(dv4, 98000)
case, (wd4, B1, B2), f4 = solve(a4, w04, 0, dv4); assert case == 'under'
near(wd4, 979.80); near(B2, 100.02); ode_ok(f4, a4, w04, 0)
# B critical (own): same circuit as 8.1 with R = 250, v0 = 12, iL0 = 30 mA
dvc = -(30e-3 + 12 / 250) / C1; near(dvc, -390000)
case, (Dc1, Dc2), fc = solve(1e4, w01, 12, dvc); assert case == 'crit'; near(Dc1, -270000); near(Dc2, 12); ode_ok(fc, 1e4, w01, 0)
# AP 8.2: R = 5k, L = 6.25 H, C = 40 nF, v0 = -10, iL0 = 8 mA (i_R = -2 mA)
a82 = 1 / (2 * 5e3 * 40e-9); w082 = 1 / SQ(6.25 * 40e-9); near(a82, 2500); near(w082, 2000)
dv82 = -(8e-3 + -10 / 5e3) / 40e-9; near(dv82, -150000)
case, (s1b, s2b, A1b, A2b), f82 = solve(a82, w082, -10, dv82); assert case == 'over'
near(s1b, -1000); near(s2b, -4000); near(A1b, -63.33); near(A2b, 53.33); ode_ok(f82, a82, w082, 0)
# AP 8.3 (branch currents of AP 8.2), in mA
iR = (A2b / 5, A1b / 5)                       # coefficients of e^{-4000t}, e^{-1000t} [mA]
iC = (40e-9 * -4000 * A2b * 1e3, 40e-9 * -1000 * A1b * 1e3)
iL = (-(iR[0] + iC[0]), -(iR[1] + iC[1]))
near(iR[0], 10.67); near(iR[1], -12.67); near(iC[0], -8.533); near(iC[1], 2.533)
near(iL[0], -2.133); near(iL[1], 10.133); near(iL[0] + iL[1], 8)
# AP 8.4: alpha = 400, wd = 300, C = 250 uF, v = e^{-400t}(120 cos 300t + 80 sin 300t)
near(1 / ((300 ** 2 + 400 ** 2) * 250e-6) * 1e3, 16); near(1 / (2 * 400 * 250e-6), 5)
near(250e-6 * (-400 * 120 + 300 * 80), -6); near(-120 / 5 - (-6), -18)
# AP 8.5: critical, alpha = 500, L = 4 H -> C = 1 uF, R = 1k; v0 = 8, iL0 = -10 mA
near(1 / (500 ** 2 * 4) * 1e6, 1); near(1 / (2 * 500 * 1e-6), 1000)
dv85 = -(-10e-3 + 8 / 1000) / 1e-6; near(dv85, 2000)
case, (D85a, D85b), f85 = solve(500, 500, 8, dv85); assert case == 'crit'; near(D85a, 6000); near(D85b, 8)
# C: Eren W9 p7-8 (Nilsson 8.7): I = 24 mA, L = 25 mH, C = 25 nF; zero initial energy
w0c = 1 / SQ(25e-3 * 25e-9); near(w0c, 40000)
case, (s1c, s2c, A1c, A2c), fC1 = solve(1 / (2 * 400 * 25e-9), w0c, 0, 0, xf=24)
assert case == 'over'; near(s1c, -20000); near(s2c, -80000); near(A1c, -32); near(A2c, 8)
case, (wdc, B1c, B2c), fC2 = solve(1 / (2 * 625 * 25e-9), w0c, 0, 0, xf=24)
assert case == 'under'; near(wdc, 24000); near(B1c, -24); near(B2c, -32)
case, (D1c, D2c), fC3 = solve(1 / (2 * 500 * 25e-9), w0c, 0, 0, xf=24)
assert case == 'crit'; near(D1c, -960000); near(D2c, -24)
for fx, a in ((fC1, 50000), (fC2, 32000), (fC3, 40000)):
    ode_ok(fx, a, w0c, 24, ts=(1e-6, 2e-5, 6e-5))
# Eren W9 p9 (Nilsson 8.8): R = 500, I0 = 29 mA, V0 = 50 V  (work in A)
case, (D1e, D2e), fE = solve(40000, w0c, 0.029, 50 / 0.025, xf=0.024)
assert case == 'crit'; near(D1e, 2200); near(D2e, 0.005)
vE = lambda t: 0.025 * (fE(t + 1e-9) - fE(t - 1e-9)) / 2e-9
near(vE(1e-5), (50 - 2.2e6 * 1e-5) * E(-0.4), rel=1e-3)
# AP 8.6: I = 2 A, I0 = 1 A, V0 = 50 V, R = 12.5, L = 25 mH, alpha = 640
C86 = 1 / (2 * 12.5 * 640); near(C86 * 1e6, 62.5); near(1 / (0.025 * C86), 640000)
case, (wd86, B186, B286), f86 = solve(640, 800, 1, 50 / 0.025, xf=2)
assert case == 'under'; near(wd86, 480); near(B186, -1); near(B286, 2.8333)
v86 = lambda t: 0.025 * (f86(t + 1e-9) - f86(t - 1e-9)) / 2e-9
for t in (1e-4, 1e-3, 3e-3):
    near(v86(t), E(-640 * t) * (50 * math.cos(480 * t) - 33.333 * math.sin(480 * t)), rel=2e-3, abs_=1e-3)
near(50 / 12.5, 4); near(2 - 4 - 1, -3)
# D natural: Eren W9 p14 (Nilsson 8.5): C = 0.1 uF at 100 V, L = 100 mH, R = 560
aS = 560 / (2 * 0.1); w0S = 1 / SQ(0.1 * 0.1e-6); near(aS, 2800); near(w0S, 1e4)
case, (wdS, B1S, B2S), fS = solve(aS, w0S, 0, 100 / 0.1); assert case == 'under'
near(wdS, 9600); near(B2S, 0.10417); ode_ok(fS, aS, w0S, 0)
near(aS * 100 / wdS, 29.17)
vS = lambda t: E(-aS * t) * (100 * math.cos(wdS * t) + 29.1667 * math.sin(wdS * t))
for t in (1e-5, 2e-4):   # i = -C dv_C/dt
    near(-0.1e-6 * (vS(t + 1e-9) - vS(t - 1e-9)) / 2e-9, fS(t), rel=2e-3)
# D step: Eren W9 p19 (Nilsson 8.11): 48 V, 0.1 H, 280 ohm, 0.4 uF
aT = 280 / 0.2; w0T = 1 / SQ(0.1 * 0.4e-6); near(aT, 1400); near(w0T, 5000)
case, (wdT, B1T, B2T), fT = solve(aT, w0T, 0, 0, xf=48); assert case == 'under'
near(wdT, 4800); near(B1T, -48); near(B2T, -14); ode_ok(fT, aT, w0T, 48)
# AP 8.7-8.9: series, L = 0.25 H, C = 16 uF, v_o(0) = 0, v_o'(0) = 0
w0P = 1 / SQ(0.25 * 16e-6); near(w0P, 500)
case, (wdP, B1P, B2P), _ = solve(200 / 0.5, w0P, 0, 0, xf=16); assert case == 'under'
near(wdP, 300); near(B1P, -16); near(B2P, -21.33)
case, (D1P, D2P), _ = solve(250 / 0.5, w0P, 0, 0, xf=20); assert case == 'crit'; near(D1P, -10000); near(D2P, -20)
case, (s1P, s2P, A1P, A2P), _ = solve(312.5 / 0.5, w0P, 0, 0, xf=25); assert case == 'over'
near(s1P, -250); near(s2P, -1000); near(A1P, -33.33); near(A2P, 8.333)

# ==================================================================================================== intro
D.P(r'**Note 3 of 3 · Textbook 8.1–8.3.** The parallel RLC circuit: natural response and step response. (8.4–8.5 series RLC is **not** on the midterm, so it is left out.)')
D.P(r'With both $L$ and $C$, energy sloshes back and forth between them; $R$ is the friction. How much friction decides the shape of the response:',
    cites=cite('E8', 7))
D.L([r'**Overdamped:** lots of friction. Creeps back to rest, no swinging.',
     r'**Critically damped:** just enough friction. Fastest return without swinging.',
     r'**Underdamped:** little friction. Swings past zero with shrinking swings.'])
D.P(r'Every question is the same three moves: find the shape, find **two** starting values (two storage elements, so two), solve for two constants.')
D.T(['Topic', 'What you are learning', 'Where'],
    [['1. Which damping?', r'$\alpha$, $\omega_0$, the roots, the $R$ for critical damping', 'A'],
     ['2. Natural response', r'$v(t)$ from $v(0^+)$ and $\dfrac{dv}{dt}(0^+)$', 'B'],
     ['3. Step response', r'$i_L(t)$ when a DC current source turns on', 'C']])
D.P(r'Every topic: what it is → the formula → a worked example → a **Try it**. ★ = from your lectures or Assessment Problems. Formula summary at the end; mixed questions in **Midterm 2 Practice Questions**.')

# ==================================================================================================== PART A
D.H('Part A · Which damping?', cites=cite('E8', 11, 12) + cite('E9', 12))
D.P(r'Goal: from $R$, $L$, $C$, decide the shape and find the roots.')
D.P(r'You are given $R$, $L$ and $C$. Will the response swing?')
D.P(r'Compute two numbers. The **neper frequency** $\alpha$ measures the friction. The **resonant frequency** $\omega_0$ measures how fast it wants to swing.')
D.EQ(r'\alpha=\frac{1}{2RC}')
D.EQ(r'\omega_0=\frac{1}{\sqrt{LC}}')
D.P(r'Then compare them:')
D.T(['Compare', 'Shape', 'Roots'],
    [[r'$\alpha>\omega_0$', 'overdamped', r'two real: $s_{1,2}=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}$'],
     [r'$\alpha=\omega_0$', 'critically damped', r'one repeated: $s=-\alpha$'],
     [r'$\alpha<\omega_0$', 'underdamped', r'complex: $s=-\alpha\pm j\omega_d$']])
D.P(r'For the underdamped case, $\omega_d$ is the swing frequency:')
D.EQ(r'\omega_d=\sqrt{\omega_0^2-\alpha^2}')
D.EX('★ Lecture example: three values of $R$',
     r'''A parallel RLC circuit has $L=50\,\mathrm{mH}$ and $C=0.2\,\mu\mathrm{F}$.

(a) Find the roots for $R=200\,\Omega$. Which shape? (b) Repeat for $R=312.5\,\Omega$. (c) Which $R$ gives critical damping?''',
     [S(r'**$\omega_0$** (same for every $R$).', (r'\omega_0^2=\frac{1}{(0.05)(0.2\times10^{-6})}=10^8', r'\omega_0=10\,000\ \mathrm{rad/s}')),
      S(r'**(a) $\alpha$** for $200\,\Omega$. It is bigger than $\omega_0$: overdamped.',
        (r'\alpha=\frac{1}{2(200)(0.2\times10^{-6})}=12\,500', r's_{1,2}=-12\,500\pm\sqrt{12\,500^2-10^8}=-12\,500\pm7500',
         r's_1=-5000,\qquad s_2=-20\,000\ \mathrm{rad/s}')),
      S(r'**(b) $\alpha$** for $312.5\,\Omega$. Now it is smaller than $\omega_0$: underdamped.',
        (r'\alpha=\frac{1}{2(312.5)(0.2\times10^{-6})}=8000', r'\omega_d=\sqrt{10^8-8000^2}=6000', r's_{1,2}=-8000\pm j6000\ \mathrm{rad/s}')),
      S(r'**(c) Critical:** set $\alpha=\omega_0$ and solve for $R$.', (r'\frac{1}{2R(0.2\times10^{-6})}=10\,000', r'R=250\,\Omega'))],
     r'(a) $-5000$, $-20\,000\,\mathrm{rad/s}$, overdamped (b) $-8000\pm j6000\,\mathrm{rad/s}$, underdamped (c) $250\,\Omega$',
     cites=cite('E8', 13))
D.CO('warning', r'In a **parallel** RLC, a bigger $R$ means a **smaller** $\alpha=\dfrac{1}{2RC}$: less damping, more swinging. (Feels backwards: a big parallel $R$ draws almost no current, so it barely brakes anything.)')
D.CO('tip', r'''**Shortcut: $R$ for critical damping** (set $\alpha=\omega_0$ and solve once):

$$
R=\frac12\sqrt{\frac LC}
$$

Example: $\dfrac12\sqrt{\dfrac{0.05}{0.2\times10^{-6}}}=\dfrac12(500)=250\,\Omega$, as above.''')
D.GRAPH([r'title "Parallel RLC: $v(t)$ for $L=50\,\mathrm{mH}$, $C=0.2\,\mu\mathrm{F}$, $v(0)=0$, $i_L(0)=-12\,\mathrm{mA}$"',
         'x 0 1.5 label="$t$ (ms)"', 'y -5 7 label="$v$ (V)"',
         r'slider R 100 600 150 step=10 label="$R$ ($\Omega$)"',
         'let C "2/10000000"', 'let L "0.05"', 'let a "1/(2*R*C)"', 'let w "1/sqrt(L*C)"', 'let d "a^2-w^2"',
         'let q "sqrt(abs(d))"', 'let D0 "0.012/C"',
         'curve "if(d>1000000, (D0/(2*q))*(exp((-a+q)*x/1000)-exp((-a-q)*x/1000)), if(d<-1000000, (D0/q)*exp(-a*x/1000)*sin(q*x/1000), D0*(x/1000)*exp(-a*x/1000)))" color=1 label="$v(t)$"',
         'hline "0"', r'readout "$\alpha$" "a" unit=" rad/s"', r'readout "$\omega_0$" "w" unit=" rad/s"'],
        intro=r'Slide $R$ from $100\,\Omega$ up. At which $R$ does the curve start to swing below zero and back?')
D.P(r'Up to $250\,\Omega$ the curve rises once and dies out (overdamped, then critically damped at exactly $250\,\Omega$). Above $250\,\Omega$, $\alpha<\omega_0$ and it swings (underdamped).')
D.CO('warning', r'"No swinging" does not mean "never crosses zero". With other starting values an overdamped $v$ can cross zero **once** (the first example in Part B does). Only the underdamped shape crosses again and again.')
D.TRY('★ AP 8.1: roots and critical $R$',
      r'A parallel RLC circuit has $R=1\,\mathrm{k\Omega}$, $L=12.5\,\mathrm{H}$, $C=2\,\mu\mathrm{F}$. (a) Find the roots. (b) Which shape? (c) Find the roots for $R=1562.5\,\Omega$. (d) Which $R$ gives critical damping?',
      [S(r'**$\alpha$ and $\omega_0^2$.**', (r'\alpha=\frac{1}{2(1000)(2\times10^{-6})}=250', r'\omega_0^2=\frac{1}{(12.5)(2\times10^{-6})}=40\,000\quad(\omega_0=200)')),
       S(r'**(a, b) Roots.** $\alpha>\omega_0$: overdamped.', (r's_{1,2}=-250\pm\sqrt{250^2-40\,000}=-250\pm150', r's_1=-100,\qquad s_2=-400\ \mathrm{rad/s}')),
       S(r'**(c)** New $\alpha$, now below $\omega_0$.', (r'\alpha=\frac{1}{2(1562.5)(2\times10^{-6})}=160', r's_{1,2}=-160\pm j\sqrt{40\,000-160^2}=-160\pm j120\ \mathrm{rad/s}')),
       S(r'**(d)** Set $\alpha=\omega_0=200$.', r'R=\frac{1}{2(200)(2\times10^{-6})}=1250\,\Omega')],
      r'(a) $-100$, $-400\,\mathrm{rad/s}$ (b) overdamped (c) $-160\pm j120\,\mathrm{rad/s}$ (d) $1250\,\Omega$',
      diff='introductory', cites=cite('AP8', 1))

# ==================================================================================================== PART B
D.H('Part B · Natural response', cites=cite('E8', 8, 14, 15) + cite('E9', 2, 3, 4))
D.P(r'Goal: the capacitor is charged and the inductor carries current. At $t=0$ they are left alone with $R$. Find $v(t)$.')
D.P(r'In a parallel circuit all three elements share **one** voltage $v$. So solve for $v$ first; every branch current follows from it.')
D.P(r'**Each shape has its own formula** with two unknown constants:')
D.T(['Shape', r'$v(t)$'],
    [['overdamped', r'$A_1e^{s_1t}+A_2e^{s_2t}$'],
     ['critically damped', r'$D_1te^{-\alpha t}+D_2e^{-\alpha t}$'],
     ['underdamped', r'$B_1e^{-\alpha t}\cos\omega_dt+B_2e^{-\alpha t}\sin\omega_dt$']])
D.P(r'You find the two constants from two starting values: $v(0^+)$ and the starting slope $\dfrac{dv}{dt}(0^+)$.')
D.P(r'**The starting slope** is the one new move. The capacitor rule $i_C=C\dfrac{dv}{dt}$ gives it, once you know $i_C(0^+)$. Get that from KCL at the top node (all three branch currents pointing down):')
D.EQ(r'\begin{gathered}i_C(0^+)=-\,i_L(0^+)-\frac{v(0^+)}{R} \\ \frac{dv}{dt}(0^+)=\frac{i_C(0^+)}{C}\end{gathered}')
D.P(r'The recipe, with the same words every time:')
D.T(['Step', 'Do this'],
    [['1. **Shape**', r'$\alpha$, $\omega_0$: which case, and the roots'],
     ['2. **Start**', r'$v(0^+)=V_0$ and $\dfrac{dv}{dt}(0^+)=\dfrac{i_C(0^+)}{C}$'],
     ['3. **Constants**', 'Two equations, two unknowns (below)'],
     ['4. **Plug in**', 'Constants into the formula']])
D.P(r'Step 3 always uses $t=0$ in $v$ and in $\dfrac{dv}{dt}$. Each case gives its own pair of equations:')
D.CARD('Overdamped constants, with an example', [
    (r'Set $t=0$ in $v$ and in its derivative:', (r'v(0^+)=A_1+A_2', r'\frac{dv}{dt}(0^+)=s_1A_1+s_2A_2')),
    (r'Example: $s_1=-5000$, $s_2=-20\,000$, $v(0^+)=12$, $\dfrac{dv}{dt}(0^+)=-450\,000$. Solve the pair:',
     (r'A_1+A_2=12', r'-5000A_1-20\,000A_2=-450\,000', r'A_1=-14,\qquad A_2=26'))], numbered=False)
D.CARD('Critically damped constants, with an example', [
    (r'At $t=0$ the $t\,e^{-\alpha t}$ term is $0$, so $D_2$ comes for free:', (r'v(0^+)=D_2', r'\frac{dv}{dt}(0^+)=D_1-\alpha D_2')),
    (r'Example: $\alpha=10\,000$, $v(0^+)=12$, $\dfrac{dv}{dt}(0^+)=-390\,000$.', (r'D_2=12', r'D_1=-390\,000+10\,000(12)=-270\,000'))], numbered=False)
D.CARD('Underdamped constants, with an example', [
    (r'At $t=0$, $\cos=1$ and $\sin=0$, so $B_1$ comes for free:', (r'v(0^+)=B_1', r'\frac{dv}{dt}(0^+)=-\alpha B_1+\omega_dB_2')),
    (r'Example: $\alpha=200$, $\omega_d=979.8$, $v(0^+)=0$, $\dfrac{dv}{dt}(0^+)=98\,000$.', (r'B_1=0', r'B_2=\frac{98\,000}{979.8}=100.02'))], numbered=False)

D.EX('★ Lecture example: overdamped',
     r'''For the circuit below, $v(0^+)=12\,\mathrm{V}$ and $i_L(0^+)=30\,\mathrm{mA}$.

''' + sch(r'''
C1 0,3 -> 0,0 "$0.2\,\mu\mathrm{F}$" i="$i_C$" v="$v$"
wire 0,3 -> 3,3 -> 6,3
L1 3,3 -> 3,0 "$50\,\mathrm{mH}$" i="$i_L$"
R1 6,3 -> 6,0 "$200\,\Omega$" i="$i_R$"
wire 6,0 -> 0,0
''') + r'''

(a) Find the starting current in each branch. (b) Find $\dfrac{dv}{dt}(0^+)$. (c) Find $v(t)$.''',
     [S(r'**Shape** (from Part A): overdamped.', r's_1=-5000,\qquad s_2=-20\,000\ \mathrm{rad/s}'),
      S(r'**Start (a):** $i_L$ is given, $i_R$ from Ohm\'s law, $i_C$ from KCL.',
        (r'i_L(0^+)=30\,\mathrm{mA},\qquad i_R(0^+)=\frac{12}{200}=60\,\mathrm{mA}', r'i_C(0^+)=-30-60=-90\,\mathrm{mA}')),
      S(r'**Start (b):** the slope.', r'\frac{dv}{dt}(0^+)=\frac{-0.09}{0.2\times10^{-6}}=-450\,000\ \mathrm{V/s}'),
      S(r'**Constants.**', (r'A_1+A_2=12', r'-5000A_1-20\,000A_2=-450\,000', r'A_1=-14,\qquad A_2=26')),
      S(r'**Plug in (c).**', r'v(t)=-14e^{-5000t}+26e^{-20\,000t}\ \mathrm{V},\qquad t\ge0')],
     r'(a) $i_L=30$, $i_R=60$, $i_C=-90\,\mathrm{mA}$ (b) $-450\,000\,\mathrm{V/s}$ (c) $v=-14e^{-5000t}+26e^{-20\,000t}\,\mathrm{V}$',
     cites=cite('E8', 16))
D.EX('★ Lecture example: underdamped',
     r'''Parallel RLC with $C=0.125\,\mu\mathrm{F}$, $L=8\,\mathrm{H}$, $R=20\,\mathrm{k\Omega}$. At $t=0$: $V_0=0$ and $I_0=-12.25\,\mathrm{mA}$ (inductor current, pointing down).

''' + sch(r'''
C1 0,3 -> 0,0 "$0.125\,\mu\mathrm{F}$" i="$i_C$" v="$v$"
wire 0,3 -> 3,3 -> 6,3
L1 3,3 -> 3,0 "$8\,\mathrm{H}$" i="$i_L$"
R1 6,3 -> 6,0 "$20\,\mathrm{k\Omega}$" i="$i_R$"
wire 6,0 -> 0,0
''') + r'''

(a) Find the roots. (b) Find $v$ and $\dfrac{dv}{dt}$ at $t=0^+$. (c) Find $v(t)$.''',
     [S(r'**Shape (a).** $\alpha<\omega_0$: underdamped.',
        (r'\alpha=\frac{1}{2(20\,000)(0.125\times10^{-6})}=200', r'\omega_0=\frac{1}{\sqrt{8(0.125\times10^{-6})}}=1000',
         r'\omega_d=\sqrt{1000^2-200^2}=979.8', r's_{1,2}=-200\pm j979.8\ \mathrm{rad/s}')),
      S(r'**Start (b).** $v(0^+)=0$, so $i_R(0^+)=0$ too.',
        (r'i_C(0^+)=-(-12.25)-0=12.25\,\mathrm{mA}', r'\frac{dv}{dt}(0^+)=\frac{12.25\times10^{-3}}{0.125\times10^{-6}}=98\,000\ \mathrm{V/s}')),
      S(r'**Constants.**', (r'B_1=v(0^+)=0', r'-200(0)+979.8\,B_2=98\,000\quad\Longrightarrow\quad B_2=100.02\ \mathrm{V}')),
      S(r'**Plug in (c).**', r'v(t)=100.02\,e^{-200t}\sin979.8t\ \mathrm{V},\qquad t\ge0')],
     r'(a) $-200\pm j979.8\,\mathrm{rad/s}$ (b) $0$, $98\,000\,\mathrm{V/s}$ (c) $v=100.02\,e^{-200t}\sin979.8t\,\mathrm{V}$',
     cites=cite('E8', 19))
D.EX('Critically damped (own variant of the first example)',
     r'Same circuit as the overdamped example, but $R=250\,\Omega$ (the critical value from Part A). Still $v(0^+)=12\,\mathrm{V}$ and $i_L(0^+)=30\,\mathrm{mA}$. Find $v(t)$.',
     [S(r'**Shape:** critically damped.', r'\alpha=\omega_0=10\,000\ \mathrm{rad/s}'),
      S(r'**Start.**', (r'i_R(0^+)=\frac{12}{250}=48\,\mathrm{mA},\qquad i_C(0^+)=-30-48=-78\,\mathrm{mA}',
                        r'\frac{dv}{dt}(0^+)=\frac{-0.078}{0.2\times10^{-6}}=-390\,000\ \mathrm{V/s}')),
      S(r'**Constants.**', (r'D_2=12', r'D_1=-390\,000+10\,000(12)=-270\,000\ \mathrm{V/s}')),
      S(r'**Plug in.**', r'v(t)=(12-270\,000\,t)\,e^{-10\,000t}\ \mathrm{V},\qquad t\ge0')],
     r'$v=(12-270\,000\,t)\,e^{-10\,000t}\,\mathrm{V}$')
D.P(r'**Branch currents** come from $v(t)$ afterwards: $i_R=\dfrac vR$, $i_C=C\dfrac{dv}{dt}$, and $i_L=-i_R-i_C$ (KCL).')
D.TRY('★ AP 8.2: overdamped',
      r'A parallel RLC has $R=5\,\mathrm{k\Omega}$, $L=6.25\,\mathrm{H}$, $C=40\,\mathrm{nF}$. At $t=0$: $v(0^+)=-10\,\mathrm{V}$ and $i_L(0^+)=8\,\mathrm{mA}$ (down). Find (a) $i_R(0^+)$, (b) $i_C(0^+)$, (c) $\dfrac{dv}{dt}(0^+)$, (d) $v(t)$.',
      [S(r'**Shape.**', (r'\alpha=\frac{1}{2(5000)(40\times10^{-9})}=2500', r'\omega_0=\frac{1}{\sqrt{6.25(40\times10^{-9})}}=2000', r's_1=-1000,\qquad s_2=-4000\ \mathrm{rad/s}')),
       S(r'**Start (a, b).**', (r'i_R(0^+)=\frac{-10}{5000}=-2\,\mathrm{mA}', r'i_C(0^+)=-8-(-2)=-6\,\mathrm{mA}')),
       S(r'**Start (c).**', r'\frac{dv}{dt}(0^+)=\frac{-0.006}{40\times10^{-9}}=-150\,000\ \mathrm{V/s}'),
       S(r'**Constants.**', (r'A_1+A_2=-10', r'-1000A_1-4000A_2=-150\,000', r'A_1=-63.33,\qquad A_2=53.33')),
       S(r'**Plug in (d).**', r'v(t)=-63.33e^{-1000t}+53.33e^{-4000t}\ \mathrm{V}')],
      r'(a) $-2\,\mathrm{mA}$ (b) $-6\,\mathrm{mA}$ (c) $-150\,000\,\mathrm{V/s}$ (d) $v=-63.33e^{-1000t}+53.33e^{-4000t}\,\mathrm{V}$',
      cites=cite('AP8', 1, 2))
D.TRY('★ AP 8.5: critically damped',
      r'A parallel RLC with $L=4\,\mathrm{H}$ is critically damped with $\alpha=500\,\mathrm{rad/s}$. At $t=0$: $v(0^+)=8\,\mathrm{V}$ and $i_L(0^+)=-10\,\mathrm{mA}$ (down). Find (a) $C$, (b) $R$, (c) $v(t)$, (d) $i_C(t)$.',
      [S(r'**(a)** Critical means $\omega_0=\alpha=500$.', r'\frac{1}{LC}=500^2\quad\Longrightarrow\quad C=\frac{1}{500^2(4)}=1\,\mu\mathrm{F}'),
       S(r'**(b)** From $\alpha=\dfrac{1}{2RC}$.', r'R=\frac{1}{2(500)(10^{-6})}=1\,\mathrm{k\Omega}'),
       S(r'**Start.**', (r'i_R(0^+)=\frac{8}{1000}=8\,\mathrm{mA},\qquad i_C(0^+)=-(-10)-8=2\,\mathrm{mA}', r'\frac{dv}{dt}(0^+)=\frac{0.002}{10^{-6}}=2000\ \mathrm{V/s}')),
       S(r'**Constants.**', (r'D_2=8', r'D_1=2000+500(8)=6000\ \mathrm{V/s}')),
       S(r'**Plug in (c).**', r'v(t)=6000\,te^{-500t}+8e^{-500t}\ \mathrm{V}'),
       S(r'**(d)** $i_C=C\dfrac{dv}{dt}$ (product rule on the $t\,e^{-500t}$ term).',
         (r'\frac{dv}{dt}=(2000-3\times10^6\,t)\,e^{-500t}', r'i_C=(2-3000\,t)\,e^{-500t}\ \mathrm{mA}'))],
      r'(a) $1\,\mu\mathrm{F}$ (b) $1\,\mathrm{k\Omega}$ (c) $v=6000te^{-500t}+8e^{-500t}\,\mathrm{V}$ (d) $i_C=(2-3000t)e^{-500t}\,\mathrm{mA}$',
      cites=cite('AP8', 3))

# ==================================================================================================== PART C
D.H('Part C · Step response', cites=cite('E9', 5, 6))
D.P(r'Goal: a DC current source $I$ is switched in at $t=0$. Find $i_L(t)$.')
D.P(r'Where does $i_L$ end up? After a long time the inductor is a wire, so it carries the **whole** source current:')
D.EQ(r'i_L(\infty)=I')
D.P(r'The answer is that final value plus the same three natural shapes as Part B (constants get a prime):')
D.EQ(r'i_L(t)=I+\big(\text{natural shape}\big)')
D.L([r'overdamped: $\ i_L=I+A_1^{\prime}e^{s_1t}+A_2^{\prime}e^{s_2t}$',
     r'critically damped: $\ i_L=I+D_1^{\prime}te^{-\alpha t}+D_2^{\prime}e^{-\alpha t}$',
     r'underdamped: $\ i_L=I+B_1^{\prime}e^{-\alpha t}\cos\omega_dt+B_2^{\prime}e^{-\alpha t}\sin\omega_dt$'])
D.P(r'**The two starting values** come from the inductor this time. The inductor rule $v=L\dfrac{di_L}{dt}$ gives the slope:')
D.EQ(r'i_L(0^+)=I_0\qquad\qquad \frac{di_L}{dt}(0^+)=\frac{v(0^+)}{L}=\frac{V_0}{L}')
D.P(r'The constants come out exactly as in Part B, except you subtract $I$ from the start: $D_2^{\prime}=I_0-I$, $B_1^{\prime}=I_0-I$, and $A_1^{\prime}+A_2^{\prime}=I_0-I$. The slope equations do not change.')
D.EX('★ Lecture example: one circuit, three resistors',
     r'''No energy is stored at $t=0$, when a $24\,\mathrm{mA}$ source is switched in (the switch across it opens).

''' + sch(r'''
I1 0,0 -> 0,3 "$24\,\mathrm{mA}$"
S1 2,3 -> 2,0 "$t=0$" state=closed action=open
wire 0,3 -> 2,3 -> 4,3 -> 7,3 -> 10,3
C1 4,3 -> 4,0 "$25\,\mathrm{nF}$" i="$i_C$" v="$v$"
L1 7,3 -> 7,0 "$25\,\mathrm{mH}$" i="$i_L$"
R1 10,3 -> 10,0 "$R$" i="$i_R$"
wire 10,0 -> 0,0
''') + r'''

(a) Find $i_L(0^+)$ and $\dfrac{di_L}{dt}(0^+)$. (b) Find $i_L(t)$ for $R=400\,\Omega$. (c) For $R=625\,\Omega$. (d) For $R=500\,\Omega$.''',
     [S(r'**Start (a).** No stored energy: $I_0=0$ and $V_0=0$.', r'i_L(0^+)=0,\qquad \frac{di_L}{dt}(0^+)=\frac{0}{L}=0'),
      S(r'**Final.**', r'i_L(\infty)=24\,\mathrm{mA}'),
      S(r'**$\omega_0$** (same for all three).', r'\omega_0=\frac{1}{\sqrt{(25\times10^{-3})(25\times10^{-9})}}=40\,000\ \mathrm{rad/s}'),
      S(r'**(b) $R=400$:** $\alpha=\dfrac{1}{2(400)(25\times10^{-9})}=50\,000>\omega_0$. Overdamped.',
        (r's_{1,2}=-50\,000\pm30\,000=-20\,000,\ -80\,000', r'A_1^{\prime}+A_2^{\prime}=0-24', r'-20\,000A_1^{\prime}-80\,000A_2^{\prime}=0',
         r'A_1^{\prime}=-32,\qquad A_2^{\prime}=8', r'i_L=24-32e^{-20\,000t}+8e^{-80\,000t}\ \mathrm{mA}')),
      S(r'**(c) $R=625$:** $\alpha=32\,000<\omega_0$. Underdamped.',
        (r'\omega_d=\sqrt{40\,000^2-32\,000^2}=24\,000', r'B_1^{\prime}=0-24=-24', r'-32\,000(-24)+24\,000B_2^{\prime}=0\Rightarrow B_2^{\prime}=-32',
         r'i_L=24-24e^{-32\,000t}\cos24\,000t', r'\qquad-32e^{-32\,000t}\sin24\,000t\ \mathrm{mA}')),
      S(r'**(d) $R=500$:** $\alpha=40\,000=\omega_0$. Critically damped.',
        (r'D_2^{\prime}=0-24=-24,\qquad D_1^{\prime}-40\,000(-24)=0\Rightarrow D_1^{\prime}=-960\,000', r'i_L=24-960\,000\,te^{-40\,000t}-24e^{-40\,000t}\ \mathrm{mA}'))],
     r'(b) $24-32e^{-20000t}+8e^{-80000t}$ (c) $24-24e^{-32000t}\cos24000t-32e^{-32000t}\sin24000t$ (d) $24-960000te^{-40000t}-24e^{-40000t}$, all in mA',
     cites=cite('E9', 7, 8))
D.TRY('★ AP 8.6: underdamped step with stored energy',
      r'A parallel RLC has $R=12.5\,\Omega$, $L=25\,\mathrm{mH}$, $C=62.5\,\mu\mathrm{F}$. A $2\,\mathrm{A}$ DC source is switched in at $t=0$. At that instant $V_0=50\,\mathrm{V}$ and $I_0=1\,\mathrm{A}$ (inductor current, down). Find (a) $i_R(0^+)$, (b) $i_C(0^+)$, (c) $\dfrac{di_L}{dt}(0^+)$, (d) the roots, (e) $i_L(t)$, (f) $v(t)$.',
      [S(r'**Start (a, b).** KCL: the source current splits three ways.', (r'i_R(0^+)=\frac{50}{12.5}=4\,\mathrm{A}', r'i_C(0^+)=2-4-1=-3\,\mathrm{A}')),
       S(r'**Start (c).**', r'\frac{di_L}{dt}(0^+)=\frac{50}{0.025}=2000\ \mathrm{A/s}'),
       S(r'**Shape (d).**', (r'\alpha=\frac{1}{2(12.5)(62.5\times10^{-6})}=640', r'\omega_0^2=\frac{1}{(0.025)(62.5\times10^{-6})}=640\,000', r's_{1,2}=-640\pm j480\ \mathrm{rad/s}')),
       S(r'**Constants.** Final value $I=2\,\mathrm{A}$.', (r"B_1^{\prime}=1-2=-1", r"-640(-1)+480B_2^{\prime}=2000\quad\Longrightarrow\quad B_2^{\prime}=2.833")),
       S(r'**Plug in (e).**', r'i_L=2+e^{-640t}\left(-\cos480t+2.833\sin480t\right)\ \mathrm{A}'),
       S(r'**(f)** $v=L\dfrac{di_L}{dt}$ (work it out, or check: $v(0)$ must be $50\,\mathrm{V}$).', r'v=e^{-640t}\left(50\cos480t-33.33\sin480t\right)\ \mathrm{V}')],
      r'(a) $4\,\mathrm{A}$ (b) $-3\,\mathrm{A}$ (c) $2000\,\mathrm{A/s}$ (d) $-640\pm j480$ (e) $i_L=2+e^{-640t}(-\cos480t+2.833\sin480t)\,\mathrm{A}$ (f) $v=e^{-640t}(50\cos480t-33.33\sin480t)\,\mathrm{V}$',
      cites=cite('AP8', 3, 4))

# ==================================================================================================== SUMMARY
D.H('Formula summary')
D.EQ(r'\alpha=\frac{1}{2RC}\qquad \omega_0=\frac{1}{\sqrt{LC}}\qquad \omega_d=\sqrt{\omega_0^2-\alpha^2}\qquad s_{1,2}=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}')
D.T(['Shape', 'When', 'Natural $v(t)$', r"Constants ($x_0$ = start value, $x_0^{\prime}$ = start slope)"],
    [['overdamped', r'$\alpha>\omega_0$', r'$A_1e^{s_1t}+A_2e^{s_2t}$', r'$A_1+A_2=x_0$, $\ s_1A_1+s_2A_2=x_0^{\prime}$'],
     ['critical', r'$\alpha=\omega_0$', r'$D_1te^{-\alpha t}+D_2e^{-\alpha t}$', r'$D_2=x_0$, $\ D_1-\alpha D_2=x_0^{\prime}$'],
     ['underdamped', r'$\alpha<\omega_0$', r'$e^{-\alpha t}(B_1\cos\omega_dt+B_2\sin\omega_dt)$', r'$B_1=x_0$, $\ -\alpha B_1+\omega_dB_2=x_0^{\prime}$']])
D.T(['', 'Natural response', 'Step response (DC source $I$)'],
    [['Solve for', r'$v$', r'$i_L=I+$ natural shape'],
     ['Start value', r'$v(0^+)=V_0$', r'$i_L(0^+)=I_0$'],
     ['Start slope', r'$\dfrac{dv}{dt}(0^+)=\dfrac{i_C(0^+)}{C}$, $\ i_C=-I_0-\dfrac{V_0}{R}$', r'$\dfrac{di_L}{dt}(0^+)=\dfrac{V_0}{L}$'],
     [r'$x_0$ in the constants', r'$V_0$', r'$I_0-I$ (subtract the final value)']])
D.P(r'Critical damping: $R=\dfrac12\sqrt{L/C}$. Branch currents: $i_R=\dfrac vR$, $i_C=C\dfrac{dv}{dt}$, $i_L=-i_R-i_C$. Practice: questions 9–12 in **Midterm 2 Practice Questions**.')

D.save()
