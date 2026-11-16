r"""ELEC 221 Midterm 2 - Ch 7: first-order RL and RC circuits (Eren W7-W8, Bakhshai W7, Week 8 Tutorial, Ch 7 APs).

Gradual-Parts style: plain-words intro -> overview table -> Part A (start value, tau), Part B (natural response),
Part C (step response: one formula, six steps, Thevenin first), Part D (sequential switching) -> 4 practice questions.
Step words everywhere: Before, Jump, After, tau, Plug in, Other.  Every number is computed and checked here.
"""
import math

from lib221 import Doc, S, cite, near, sch

E, LN = math.exp, math.log
D = Doc('ch7', 'Midterm 2 · 2. RL and RC Circuits', ['rl_circuits', 'rc_circuits', 'transient_response'])


def par(*r):
    return 1 / sum(1 / x for x in r)


# ------------------------------------------------------------------------------------------ numbers
# Ex: Eren W7 p9 (Nilsson 7.1)
Req1 = 2 + par(10, 40); near(Req1, 10); tau1 = 2 / Req1; near(tau1, 0.2)
w0_1 = 0.5 * 2 * 20 ** 2; near(w0_1, 400)
w10 = 160 ** 2 / 10 / 10; near(w10, 256)      # int_0^inf 2560 e^{-10t} dt
near(w10 / w0_1, 0.64)
# Ex: Eren W7 p16 (Nilsson 7.3)
Req2 = 32e3 + par(240e3, 60e3); near(Req2, 80e3); tau2 = Req2 * 0.5e-6; near(tau2, 0.04)
near(par(240e3, 60e3) / Req2 * 100, 60); near(60 / 60e3 * 1e3, 1)
w60k = 60 ** 2 / 60e3 / 50; near(w60k * 1e3, 1.2); near(0.5 * 0.5e-6 * 100 ** 2 * 1e3, 2.5)
# Tutorial Q2 = AP 7.3
near(5e3 + par(30e3, 60e3), 25e3); near(25e3 * 40e-9, 1e-3); near(0.5 * 40e-9 * 150 ** 2 * 1e6, 450)
# Tutorial Q1
Lq1 = 10 / (1000 * LN(2)); near(Lq1 * 1e3, 14.43, rel=3e-3); near(30e-3 * 1e3 / 10e3, 3e-3)
near(1 - E(-2 * 1e-3 / (Lq1 / 10)), 0.75)
near(0.5 * Lq1 * 3e-3 ** 2 * 1e9, 64.94, rel=3e-3)
# Tutorial Q3
Leq3 = 1.25 + par(10, 6); near(Leq3, 5); near(Leq3 / 7.5e3, 1 / 1500)
near(7.5e3 * 2 * par(10, 6) / Leq3, 11250); near(11250 / (6 * 1500), 1.25)
# Ex: Eren W7 p20 (Nilsson 7.5)
near(24 / 2, 12); near(0.2 / 2, 0.1); near(0.2 * 20 * 10, 40)
t24 = LN(40 / 24) / 10; near(t24 * 1e3, 51.08, rel=3e-3)
# Ex: Eren W7 p25 (Nilsson 7.6)
near(40 * 60 / 80, 30); near(-75 * 160 / 200, -60); near(8e3 + par(160e3, 40e3), 40e3); near(40e3 * 0.25e-6, 0.01)
near(0.25e-6 * 90 * 100 * 1e3, 2.25)
# Eren W8 p3 / Bakhshai W7 p13 (Nilsson 7.9)
near(7.5e-3 * 20e3, 150); near(150 / 50e3 * 1e3, 3); near(50e3 * 0.1e-6, 5e-3); near(150 - 20e3 * 3e-3, 90)
# AP 7.6
near(20 / 25 * -30, -24); near(par(20, 5), 4); near(4 * 25e-3, 0.1); near((-24 + 50) / 4, 6.5); near(25e-3 * 10 * 26, 6.5)
# Own dependent-source example: 12 V, 4 ohm, a: 4 ohm (i_x down) and CCCS 0.5 i_x down, L = 1 H
voc = 12 / 2.5; near(voc, 4.8); isc = 12 / 4; near(voc / isc, 1.6); near(par(4, 4, 8), 1.6); near(1 / 1.6, 0.625)
# AP 7.8
near(75 * 10 / 15, 50); near(-100 * 40 / 50, -80); near(par(40e3, 10e3), 8e3); near(8e3 * 40e-9, 0.32e-3)
near(1 / 0.32e-3, 3125); near((130 + 20) / 10, 15)  # i_o(0+) = 15 mA
# Eren W8 p6 (Nilsson 7.11)
Ra = par(12, par(6, 3)); va = 60 * Ra / (4 + Ra); near(va, 18); near(va / 3, 6)
near(par(18, 9), 6); near(0.15 / 6, 0.025); i35 = 6 * E(-40 * 0.035); near(i35, 1.4796); near(0.15 / 9, 1 / 60)
# Eren W8 p5 (Nilsson 7.12)
v15 = 400 * (1 - E(-1.5)); near(v15, 310.75)
near(LN(2) / 100 * 1e3, 6.93, rel=3e-3); t200 = 0.015 + LN(v15 / 200) / 200; near(t200 * 1e3, 17.20, rel=3e-3)
# AP 7.9
v20 = 40 * E(-2); near(v20, 5.4134)
w20k = 1600 / 20e3 / 200 * (1 - E(-4)) + v20 ** 2 / 20e3 / 250; near(w20k * 1e6, 398.5, rel=3e-3)
w80k = v20 ** 2 / 80e3 / 250; near(w80k * 1e6, 1.465, rel=3e-3); near(0.5 * 0.5e-6 * 40 ** 2 * 1e6, 400)
near(par(20e3, 60e3) / (par(20e3, 60e3) + 15e3) * 80, 40)
# AP 7.5
near((30 - 250) / 55e3 * 1e3, -4); near(0.2 / 30e3 * 1e6, 6.667, rel=3e-3)
# AP 7.10
near(10 / 5, 2)

# ==================================================================================================== intro
D.P(r'**Note 2 of 3 · Textbook 7.1–7.5.** First-order RL and RC circuits: natural response, step response, the general method, sequential switching. (7.6 unbounded response and 7.7 the integrating amplifier are not on the midterm.)')
D.P(r'Setup: a switch flips at $t=0$ in a circuit with **one** $L$ or **one** $C$ (or several you can combine into one). Before the flip everything has settled (DC). After it, $i_L$ or $v_C$ slides exponentially from its old value to a new one.',
    cites=cite('E7', 2))
D.P(r'So every answer is "final value plus a gap that shrinks", and you only need **three numbers**: start, final, and $\tau$.')
D.EQ(r'x(t)=x(\infty)+\big[x(0^+)-x(\infty)\big]\,e^{-t/\tau}')
D.P(r'Here $x$ is whatever you are asked for: usually $i_L$ or $v_C$.')
D.T(['Topic', 'What you are learning', 'Where'],
    [['1. The start value', r'Find $i_L$ or $v_C$ before the switch (DC)', 'A1'],
     [r'2. The time constant $\tau$', r'$\tau=L/R$ or $RC$, with the right $R$', 'A2'],
     ['3. Natural response', 'No source after the switch: decay to 0, energy %', 'B'],
     ['4. Step response', 'A source after the switch: the one formula, six steps', 'C1'],
     ['5. Thévenin first', 'Messy circuits and dependent sources', 'C2'],
     ['6. Sequential switching', 'Two switch times: restart the clock', 'D']])
D.L([r'**Part A · The three numbers.** Start value and $\tau$. Used in every question.',
     r'**Part B · Natural response.** The source is gone after the switch, so everything dies out.',
     r'**Part C · Step response.** A source is still there, so it settles at a new value.',
     r'**Part D · Sequential switching.** Two flips. Same method, done twice.'])
D.P(r'Every topic: what it is → the formula → a worked example → a **Try it**. ★ = from your lectures, tutorials or Assessment Problems. Formula summary at the end; mixed questions in **Midterm 2 Practice Questions**.')
D.CO('reminder', r'''**What you need from note 1 (A4):**

- Long time (DC): an inductor is a **wire**, a capacitor is a **gap**.
- At the switch: $i_L(0^+)=i_L(0^-)$ and $v_C(0^+)=v_C(0^-)$. Everything else may jump.''')

# ==================================================================================================== PART A
D.H('Part A · The three numbers: start, final, $\\tau$')
D.P(r'Goal: find the start value and the time constant. (The final value is the same DC trick as the start value, so it gets its own spot in Part C.)')

# ---- A1 -------------------------------------------------------------------------------------------
D.H('A1 · The start value: the circuit before the switch', level=2, cites=cite('B7', 9))
D.P(r'The switch has been closed for a long time. What is $i_L$ just before it opens?')
D.P(r'"A long time" means DC. So redraw the circuit with:')
D.L([r'the **inductor** replaced by a **wire**, or', r'the **capacitor** replaced by a **gap**.'])
D.P(r'Solve that plain resistor circuit for $i_L(0^-)$ or $v_C(0^-)$. It carries straight over to $0^+$:')
D.EQ(r'i_L(0^+)=i_L(0^-)\qquad\qquad v_C(0^+)=v_C(0^-)')
D.EX('★ Lecture example: inductor current before the switch',
     r'''The switch has been closed for a long time and opens at $t=0$. Find $i_L(0^-)$.

''' + sch(r'''
I1 0,0 -> 0,3 "$20\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$0.1\,\Omega$"
S1 3,3 -> 6,3 "$t=0$" state=closed action=open
L1 6,3 -> 6,0 "$2\,\mathrm{H}$" i="$i_L$"
R2 6,3 -> 9,3 "$2\,\Omega$"
R3 9,3 -> 9,0 "$10\,\Omega$"
wire 9,3 -> 12,3
R4 12,3 -> 12,0 "$40\,\Omega$" i="$i_o$" v="$v_o$"
wire 12,0 -> 0,0
label 3,3 "$a$" above
label 6,3 "$b$" above
ground 0,0
'''),
     [S(r'**Before:** replace the inductor by a wire. Node $b$ is now tied to ground, so $v_b=0$.'),
      S(r'**Spot** what that does. The switch is closed, so $v_a=v_b=0$ too. Every resistor ($0.1$, $2$, $10$, $40\,\Omega$) has $0\,\mathrm{V}$ across it and carries no current.'),
      S(r'**Solve:** the whole $20\,\mathrm{A}$ goes through the switch and down the wire (the inductor).', r'i_L(0^-)=20\,\mathrm{A}=i_L(0^+)')],
     r'$i_L(0^-)=i_L(0^+)=20\,\mathrm{A}$', cites=cite('E7', 9))
D.CO('tip', r'**Shortcut:** a wire (the inductor at DC) in parallel with resistors steals **all** the current. Those resistors get $0\,\mathrm{A}$.')
D.TRY('★ Week 8 Tutorial Q1: starting current',
      r'''The switch has been closed for a long time and opens at $t=0$. Find $i_L(0^-)$, with $i_L$ pointing down.

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
'''),
      [S(r'**Before:** $L$ is a wire, so it shorts out the $10\,\Omega$ (no current there).'),
       S(r'**Split** the $30\,\mathrm{mA}$ between $1\,\mathrm{k\Omega}$ and the $9\,\mathrm{k\Omega}$ path (current divider).',
         r'i_L(0^-)=30\,\mathrm{mA}\cdot\frac{1\,\mathrm{k}}{1\,\mathrm{k}+9\,\mathrm{k}}=3\,\mathrm{mA}')],
      r'$i_L(0^-)=3\,\mathrm{mA}$', diff='introductory', cites=cite('T8', 1, 3))

# ---- A2 -------------------------------------------------------------------------------------------
D.H('A2 · The time constant $\\tau$', level=2, cites=cite('E7', 8, 15))
D.P(r'How fast does the circuit settle?')
D.EQ(r'\tau=\frac{L}{R_{eq}}\qquad\qquad \tau=R_{eq}\,C')
D.P(r'$R_{eq}$ is the resistance the inductor or capacitor **sees** from its two ends, after the switch, with every independent source turned off:')
D.L([r'voltage source off $\to$ a **wire**', r'current source off $\to$ a **gap**'])
D.P(r'**Example.** In the lecture example above, after the switch opens the inductor sees $2\,\Omega$ in series with $10\parallel40$.')
D.EQ(r'\begin{gathered}R_{eq}=2+\frac{10\cdot40}{10+40}=2+8=10\,\Omega \\ \tau=\frac{2}{10}=0.2\,\mathrm{s}\end{gathered}')
D.P(r'After $5\tau$ the curve has done more than $99\%$ of its move ($e^{-5}=0.0067$). Treat it as finished.')
D.P(r'Fact worth knowing: at $t=\tau$ there is always $e^{-1}\approx37\%$ of the gap left, whatever $\tau$ is.')
D.TRY('★ Week 8 Tutorial Q3: $\\tau$ with three inductors',
      r'''After the switches move, the $1.25\,\mathrm{H}$ inductor is in series with $(10\,\mathrm{H}\parallel6\,\mathrm{H})$, and that combination discharges through a $7.5\,\mathrm{k\Omega}$ resistor. Find $\tau$.''',
      [S(r'**Combine** the inductors first.', r'L_{eq}=1.25+\frac{10\cdot6}{10+6}=1.25+3.75=5\,\mathrm{H}'),
       S(r'**Divide** by the resistance it sees.', r'\tau=\frac{5}{7500}=\frac{1}{1500}\,\mathrm{s}\approx0.667\,\mathrm{ms}')],
      r'$\tau=\dfrac{1}{1500}\,\mathrm{s}\approx0.667\,\mathrm{ms}$', diff='introductory', cites=cite('T8', 7))

# ==================================================================================================== PART B
D.H('Part B · Natural response: no source after the switch', cites=cite('E7', 4, 5, 11, 12))
D.P(r'Goal: the stored energy drains into the resistors and everything dies out.')
D.P(r'After the switch the inductor or capacitor is alone with resistors. So the final value is $0$, and the formula shrinks to:')
D.EQ(r'x(t)=x(0^+)\,e^{-t/\tau}')
D.L([r'RL: $\ i_L(t)=I_0\,e^{-t/\tau}$, with $\tau=\dfrac{L}{R}$', r'RC: $\ v_C(t)=V_0\,e^{-t/\tau}$, with $\tau=RC$'])
D.P(r'The recipe has four steps. Use the same words every time:')
D.T(['Step', 'Do this'],
    [['1. **Before**', r'DC circuit: find $i_L(0^-)$ or $v_C(0^-)$'],
     [r'2. **$\tau$**', r'$R_{eq}$ seen by $L$ or $C$ after the switch'],
     ['3. **Plug in**', r'$x(t)=x(0^+)e^{-t/\tau}$'],
     ['4. **Other**', 'Other currents and voltages from $x(t)$'],])
D.P(r'In step 4 you use plain circuit rules on the circuit **after** the switch: Ohm\'s law, current division, voltage division. Those answers hold for $t\ge0^+$ only, because they can jump at the switch.')

D.EX('★ Lecture example: RL natural response and energy',
     r'''Same circuit as in A1: the switch opens at $t=0$ after a long time closed.

''' + sch(r'''
I1 0,0 -> 0,3 "$20\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$0.1\,\Omega$"
S1 3,3 -> 6,3 "$t=0$" state=closed action=open
L1 6,3 -> 6,0 "$2\,\mathrm{H}$" i="$i_L$"
R2 6,3 -> 9,3 "$2\,\Omega$"
R3 9,3 -> 9,0 "$10\,\Omega$"
wire 9,3 -> 12,3
R4 12,3 -> 12,0 "$40\,\Omega$" i="$i_o$" v="$v_o$"
wire 12,0 -> 0,0
ground 0,0
''') + r'''

Find (a) $i_L(t)$, (b) $i_o(t)$, (c) $v_o(t)$, (d) the percentage of the inductor's initial energy that ends up in the $10\,\Omega$ resistor.''',
     [S(r'**Before** (from A1).', r'i_L(0^+)=20\,\mathrm{A}'),
      S(r'**$\tau$** (from A2).', r'R_{eq}=2+10\parallel40=10\,\Omega,\qquad \tau=\frac{2}{10}=0.2\,\mathrm{s}'),
      S(r'**Plug in** (a).', r'i_L(t)=20e^{-5t}\ \mathrm{A},\qquad t\ge0'),
      S(r'**Other (b).** The inductor current comes back up through $10\parallel40$. The $40\,\Omega$ takes $\frac{10}{10+40}$ of it, flowing **up**, against the $i_o$ arrow.',
        r'i_o(t)=-\frac{10}{50}\,i_L=-4e^{-5t}\ \mathrm{A},\qquad t\ge0^+'),
      S(r'**Other (c).** Ohm\'s law on the $40\,\Omega$.', r'v_o(t)=40\,i_o=-160e^{-5t}\ \mathrm{V},\qquad t\ge0^+'),
      S(r'**Energy (d).** Initial energy, then the $10\,\Omega$ power ($v_o$ is across it too), then integrate to $\infty$.',
        (r'w(0)=\tfrac12(2)(20)^2=400\,\mathrm{J}', r'p_{10\Omega}=\frac{v_o^2}{10}=2560e^{-10t}\ \mathrm{W}',
         r'w_{10\Omega}=\int_0^\infty2560e^{-10t}\,dt=\frac{2560}{10}=256\,\mathrm{J}', r'\frac{256}{400}=64\%'))],
     r'(a) $20e^{-5t}\,\mathrm{A}$ (b) $-4e^{-5t}\,\mathrm{A}$ (c) $-160e^{-5t}\,\mathrm{V}$ (d) $64\%$', cites=cite('E7', 9))
D.CO('tip', r'''**Shortcut for energy integrals:**

$$
\int_0^\infty A\,e^{-at}\,dt=\frac{A}{a}
$$

Example: $\int_0^\infty2560e^{-10t}\,dt=256$. And if there is only **one** resistor, it gets all the energy: by time $t$ it has taken $w(0)\left(1-e^{-2t/\tau}\right)$.''')
D.CO('warning', r'Power has $e^{-2t/\tau}$, not $e^{-t/\tau}$, because $p$ uses $v^2$ or $i^2$. Forgetting the 2 is the most common mistake here.')

D.EX('★ Lecture example: RC natural response',
     r'''The switch has been at $x$ for a long time. At $t=0$ it moves to $y$.

''' + sch(r'''
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
R1 0,3 -> 3,3 "$10\,\mathrm{k\Omega}$"
S1 3,3 -> 5,3 "$x$" state=closed action=open
C1 5,3 -> 5,0 "$0.5\,\mu\mathrm{F}$" v="$v_C$"
S2 5,3 -> 7,3 "$y$" action=close
R2 7,3 -> 10,3 "$32\,\mathrm{k\Omega}$"
R3 10,3 -> 10,0 "$240\,\mathrm{k\Omega}$" v="$v_o$"
wire 10,3 -> 13,3
R4 13,3 -> 13,0 "$60\,\mathrm{k\Omega}$" i="$i_o$"
wire 13,0 -> 0,0
ground 0,0
''') + r'''

Find (a) $v_C(t)$, (b) $v_o(t)$, (c) $i_o(t)$, (d) the total energy dissipated in the $60\,\mathrm{k\Omega}$ resistor.''',
     [S(r'**Before:** $C$ is a gap, so no current flows in the $10\,\mathrm{k\Omega}$. The capacitor charges to the full source.', r'v_C(0^+)=v_C(0^-)=100\,\mathrm{V}'),
      S(r'**$\tau$:** the capacitor sees $32\,\mathrm{k}$ in series with $240\,\mathrm{k}\parallel60\,\mathrm{k}=48\,\mathrm{k}$.',
        (r'R_{eq}=32+48=80\,\mathrm{k\Omega}', r'\tau=(80\times10^3)(0.5\times10^{-6})=40\,\mathrm{ms}')),
      S(r'**Plug in** (a).', r'v_C(t)=100e^{-25t}\ \mathrm{V},\qquad t\ge0'),
      S(r'**Other (b):** voltage divider, $48\,\mathrm{k}$ out of $80\,\mathrm{k}$.', r'v_o=\frac{48}{80}\,v_C=60e^{-25t}\ \mathrm{V},\qquad t\ge0^+'),
      S(r'**Other (c):** Ohm\'s law.', r'i_o=\frac{v_o}{60\,\mathrm{k}}=e^{-25t}\ \mathrm{mA},\qquad t\ge0^+'),
      S(r'**Energy (d).**', (r'p_{60k}=\frac{v_o^2}{60\,\mathrm{k}}=\frac{3600}{60000}e^{-50t}=0.06e^{-50t}\ \mathrm{W}',
                              r'w_{60k}=\frac{0.06}{50}=1.2\,\mathrm{mJ}'))],
     r'(a) $100e^{-25t}\,\mathrm{V}$ (b) $60e^{-25t}\,\mathrm{V}$ (c) $e^{-25t}\,\mathrm{mA}$ (d) $1.2\,\mathrm{mJ}$', cites=cite('E7', 16))
D.P(r'Two switches with the letters $x$ and $y$ mean one switch arm that moves from $x$ to $y$.')
D.TRY('★ Week 8 Tutorial Q2 = AP 7.3: RC natural response',
      r'''The switch has been on the left for a long time. At $t=0$ it moves right and stays there.

''' + sch(r'''
V1 0,3 -> 0,0 "$150\,\mathrm{V}$"
R1 0,3 -> 3,3 "$10\,\mathrm{k\Omega}$"
S1 3,3 -> 5,3 "$t=0$" state=closed action=open
C1 5,3 -> 5,0 "$40\,\mathrm{nF}$" v="$v$"
S2 5,3 -> 7,3 "$t=0$" action=close
R2 7,3 -> 10,3 "$5\,\mathrm{k\Omega}$"
R3 10,3 -> 10,0 "$30\,\mathrm{k\Omega}$"
wire 10,3 -> 13,3
R4 13,3 -> 13,0 "$60\,\mathrm{k\Omega}$"
wire 13,0 -> 0,0
ground 0,0
''') + r'''

Find (a) $v(0)$, (b) the initial stored energy, (c) $\tau$, (d) $v(t)$.''',
      [S(r'**Before:** $C$ is a gap, no current in $10\,\mathrm{k}$.', r'v(0)=150\,\mathrm{V}'),
       S(r'**Energy.**', r'w(0)=\tfrac12(40\times10^{-9})(150)^2=450\,\mu\mathrm{J}'),
       S(r'**$\tau$:** $5\,\mathrm{k}+30\,\mathrm{k}\parallel60\,\mathrm{k}$.', (r'R_{eq}=5+20=25\,\mathrm{k\Omega}', r'\tau=(25\times10^3)(40\times10^{-9})=1\,\mathrm{ms}')),
       S(r'**Plug in.**', r'v(t)=150e^{-1000t}\ \mathrm{V},\qquad t\ge0')],
      r'(a) $150\,\mathrm{V}$ (b) $450\,\mu\mathrm{J}$ (c) $1\,\mathrm{ms}$ (d) $150e^{-1000t}\,\mathrm{V}$', diff='introductory',
      cites=cite('T8', 4, 5) + cite('AP7', 2, 3))

# ==================================================================================================== PART C
D.H('Part C · Step response: a source is still there')
D.P(r'Goal: one formula and six steps that solve every first-order question, natural or step.')

# ---- C1 -------------------------------------------------------------------------------------------
D.H('C1 · One formula, six steps', level=2, cites=cite('E8', 2) + cite('B7', 8))
D.P(r'Now a source is still connected after the switch. Where does the curve end up?')
D.P(r'At a new DC value, $x(\infty)$. You find it the same way as the start value: inductor = wire, capacitor = gap, but with the switch in its **new** position.')
D.EQ(r'x(t)=x(\infty)+\big[x(0^+)-x(\infty)\big]\,e^{-t/\tau}')
D.L([r'$x(0^+)$: the **start** value, just after the switch.',
     r'$x(\infty)$: the **final** value, long after the switch.',
     r'$\tau$: how fast. Same $\tau$ for every current and voltage in the circuit.'])
D.P(r'Natural response is the special case $x(\infty)=0$.')
D.P(r'The curve always heads straight for $x(\infty)$, fast at first, then slower. It never overshoots (that only happens with RLC).')
D.P(r'Your course solves every question with the same six steps:')
D.T(['Step', 'Do this'],
    [['1. **Before** ($0^-$)', r'$L$ = wire, $C$ = gap. Find $i_L(0^-)$ or $v_C(0^-)$'],
     ['2. **Jump** ($0^+$)', r'Carry it over: $i_L(0^+)=i_L(0^-)$, $v_C(0^+)=v_C(0^-)$'],
     ['3. **After** ($\\infty$)', r'Switch in new position, $L$ = wire, $C$ = gap. Find $x(\infty)$'],
     [r'4. **$\tau$**', r'$R_{eq}$ seen by $L$ or $C$, sources off'],
     ['5. **Plug in**', 'The formula above'],
     ['6. **Other**', r'$v_L=L\dfrac{di_L}{dt}$, $i_C=C\dfrac{dv_C}{dt}$, Ohm\'s law']], cites=cite('B7', 9, 10, 11, 12))
D.CO('warning', r'Steps 1–5 work best on $i_L$ (for an RL circuit) or $v_C$ (for an RC circuit), because those cannot jump. For any other quantity, get its start value from the $0^+$ circuit: the inductor becomes a **current source** $i_L(0^+)$, the capacitor a **voltage source** $v_C(0^+)$.')

D.EX('★ Lecture example: RL step response',
     r'''The switch has been at $a$ for a long time. At $t=0$ it moves to $b$ (make-before-break, so the inductor current is never interrupted).

''' + sch(r'''
V1 0,3 -> 0,0 "$24\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
S1 3,3 -> 6,3 "$b$" action=close
S2 9,3 -> 6,3 "$a$" state=closed action=open
L1 6,3 -> 6,0 "$200\,\mathrm{mH}$" i="$i$" v="$v$"
R2 9,3 -> 9,0 "$10\,\Omega$"
wire 9,3 -> 12,3
I1 12,3 -> 12,0 "$8\,\mathrm{A}$"
wire 0,0 -> 6,0 -> 9,0 -> 12,0
ground 0,0
#~ flow
''') + r'''

(a) Find $i(t)$. (b) Find $v(0^+)$. (c) When does $v$ equal $24\,\mathrm{V}$?''',
     [S(r'**Before:** the inductor (a wire) sits on the right side with the $10\,\Omega$ and the $8\,\mathrm{A}$ source. The wire shorts the $10\,\Omega$. The source pulls $8\,\mathrm{A}$ **down** on its side, so it pulls $8\,\mathrm{A}$ **up** through the inductor, against the $i$ arrow.',
        r'i(0^-)=-8\,\mathrm{A}'),
      S(r'**Jump.**', r'i(0^+)=-8\,\mathrm{A}'),
      S(r'**After:** the inductor (a wire) is now in a loop with $24\,\mathrm{V}$ and $2\,\Omega$.', r'i(\infty)=\frac{24}{2}=12\,\mathrm{A}'),
      S(r'**$\tau$:** turn the $24\,\mathrm{V}$ off (wire). The inductor sees $2\,\Omega$.', r'\tau=\frac{0.2}{2}=0.1\,\mathrm{s}'),
      S(r'**Plug in** (a).', (r'i(t)=12+(-8-12)e^{-10t}', r'i(t)=12-20e^{-10t}\ \mathrm{A},\qquad t\ge0')),
      S(r'**Other (b):** $v=L\dfrac{di}{dt}$.', (r'v=0.2\cdot200e^{-10t}=40e^{-10t}\ \mathrm{V}', r'v(0^+)=40\,\mathrm{V}')),
      S(r'**Solve (c)** $40e^{-10t}=24$.', (r'e^{-10t}=0.6', r't=\frac{\ln(1/0.6)}{10}=' + f'{t24 * 1e3:.2f}' + r'\,\mathrm{ms}'))],
     r'(a) $i=12-20e^{-10t}\,\mathrm{A}$ (b) $40\,\mathrm{V}$ (c) $' + f'{t24 * 1e3:.2f}' + r'\,\mathrm{ms}$', cites=cite('E7', 20, 21))
D.P(r'Check (b) with the $0^+$ circuit: the inductor is an $-8\,\mathrm{A}$ source, so the $2\,\Omega$ carries $-8\,\mathrm{A}$ and drops $-16\,\mathrm{V}$. Then $v=24-(-16)=40\,\mathrm{V}$. Same answer.')

D.EX('★ Lecture example: RC step response',
     r'''The switch has been in position 1 for a long time. At $t=0$ it moves to position 2.

''' + sch(r'''
V1 0,3 -> 0,0 "$40\,\mathrm{V}$"
R1 0,3 -> 3,3 "$20\,\mathrm{k\Omega}$"
R2 3,3 -> 3,0 "$60\,\mathrm{k\Omega}$"
S1 3,3 -> 5,3 "$1$" state=closed action=open
C1 5,3 -> 5,0 "$0.25\,\mu\mathrm{F}$" v="$v_o$"
S2 5,3 -> 7,3 "$2$" action=close
R3 10,3 -> 7,3 "$8\,\mathrm{k\Omega}$" i="$i_o$"
R4 10,3 -> 10,0 "$160\,\mathrm{k\Omega}$"
R5 10,3 -> 13,3 "$40\,\mathrm{k\Omega}$"
V2 13,0 -> 13,3 "$75\,\mathrm{V}$"
wire 13,0 -> 0,0
label 10,3 "$B$" above
ground 0,0
''') + r'''

(a) Find $v_o(t)$. (b) Find $i_o(t)$.''',
     [S(r'**Before:** $C$ is a gap. The $40\,\mathrm{V}$ divides over $20\,\mathrm{k}$ and $60\,\mathrm{k}$.', r'v_o(0^-)=40\cdot\frac{60}{20+60}=30\,\mathrm{V}'),
      S(r'**Jump.**', r'v_o(0^+)=30\,\mathrm{V}'),
      S(r'**After:** $C$ is a gap, so no current in the $8\,\mathrm{k}$ and $v_o=v_B$. The $75\,\mathrm{V}$ source has its $+$ at the bottom, so node $B$ is negative.',
        r'v_o(\infty)=-75\cdot\frac{160}{160+40}=-60\,\mathrm{V}'),
      S(r'**$\tau$:** source off; $8\,\mathrm{k}$ plus $160\,\mathrm{k}\parallel40\,\mathrm{k}$.', (r'R_{eq}=8+32=40\,\mathrm{k\Omega}', r'\tau=(40\times10^3)(0.25\times10^{-6})=10\,\mathrm{ms}')),
      S(r'**Plug in** (a).', (r'v_o(t)=-60+(30+60)e^{-100t}', r'v_o(t)=-60+90e^{-100t}\ \mathrm{V},\qquad t\ge0')),
      S(r'**Other (b):** $i_o$ flows into the $+$ end of the capacitor, so $i_o=C\dfrac{dv_o}{dt}$.', r'i_o=0.25\times10^{-6}\cdot(-9000e^{-100t})=-2.25e^{-100t}\ \mathrm{mA},\qquad t\ge0^+')],
     r'(a) $-60+90e^{-100t}\,\mathrm{V}$ (b) $-2.25e^{-100t}\,\mathrm{mA}$', cites=cite('E7', 25))
D.TRY('★ Lecture example: use the formula on any current',
      r'''The switch has been open for a long time and the capacitor is uncharged. It closes at $t=0$. Find $i(t)$ and $v(t)$ for $t\ge0^+$.

''' + sch(r'''
I1 0,0 -> 0,3 "$7.5\,\mathrm{mA}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$20\,\mathrm{k\Omega}$" v="$v$"
S1 3,3 -> 5,3 "$t=0$" action=close
C1 5,3 -> 8,3 "$0.1\,\mu\mathrm{F}$" i="$i$"
R2 8,3 -> 8,0 "$30\,\mathrm{k\Omega}$"
wire 8,0 -> 0,0
ground 0,0
'''),
      [S(r'**Before:** uncharged, so $v_C(0^-)=0$.'),
       S(r'**Jump:** in the $0^+$ circuit the capacitor is a $0\,\mathrm{V}$ source (a wire). The $7.5\,\mathrm{mA}$ splits between $20\,\mathrm{k}$ and $30\,\mathrm{k}$.',
         r'i(0^+)=7.5\cdot\frac{20}{20+30}=3\,\mathrm{mA}'),
       S(r'**After:** the capacitor is a gap.', r'i(\infty)=0'),
       S(r'**$\tau$:** current source off (gap). The capacitor sees $20\,\mathrm{k}+30\,\mathrm{k}$.', r'\tau=(50\times10^3)(0.1\times10^{-6})=5\,\mathrm{ms}'),
       S(r'**Plug in.**', r'i(t)=3e^{-200t}\ \mathrm{mA},\qquad t\ge0^+'),
       S(r'**Other:** KCL at the top node: the $20\,\mathrm{k}$ gets $7.5-i$.', r'v=20\,\mathrm{k}\,(7.5-3e^{-200t})\,\mathrm{mA}=150-60e^{-200t}\ \mathrm{V}')],
      r'$i=3e^{-200t}\,\mathrm{mA}$; $v=150-60e^{-200t}\,\mathrm{V}$', cites=cite('E8', 3) + cite('B7', 13, 14, 15))

# ---- C2 -------------------------------------------------------------------------------------------
D.H('C2 · Thévenin first: messy circuits and dependent sources', level=2, cites=cite('B7', 4, 5, 6))
D.P(r'Lots of resistors, or a dependent source. How do you get $\tau$ and the final value?')
D.P(r'Replace everything the $L$ or $C$ sees by its Thévenin equivalent ($V_{Th}$ in series with $R_{Th}$). Then read off:')
D.T(['', 'RC circuit', 'RL circuit'],
    [['Final value', r'$v_C(\infty)=V_{Th}$', r'$i_L(\infty)=\dfrac{V_{Th}}{R_{Th}}=I_N$'],
     [r'$\tau$', r'$R_{Th}\,C$', r'$\dfrac{L}{R_{Th}}$']])
D.P(r'Why: at DC the capacitor is a gap, so it sees the open-circuit voltage. The inductor is a wire, so it carries the short-circuit current.')
D.EX('★ AP 7.6: Thévenin for an RC step',
     r'''For $t\ge0$ the $25\,\mathrm{mF}$ capacitor sits in this circuit, and $v_c(0^+)=-50\,\mathrm{V}$.

''' + sch(r'''
V1 0,0 -> 0,3 "$30\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\Omega$"
R2 3,3 -> 3,0 "$20\,\Omega$"
wire 3,3 -> 6,3
C1 6,3 -> 6,0 "$25\,\mathrm{mF}$" v="$v_c$" i="$i$"
wire 6,0 -> 0,0
ground 0,0
''') + r'''

Find $V_{Th}$, $R_{Th}$, $\tau$, $v_c(t)$, and $i(t)$.''',
     [S(r'**Thévenin voltage:** remove $C$. The $30\,\mathrm{V}$ (its $+$ at the bottom) divides over $5$ and $20\,\Omega$.', r'V_{Th}=\frac{20}{25}(-30)=-24\,\mathrm{V}'),
      S(r'**Thévenin resistance:** source off (wire), so $5\parallel20$.', r'R_{Th}=\frac{5\cdot20}{25}=4\,\Omega'),
      S(r'**$\tau$** and **After**.', (r'\tau=4\cdot0.025=0.1\,\mathrm{s}', r'v_c(\infty)=V_{Th}=-24\,\mathrm{V}')),
      S(r'**Plug in.**', (r'v_c=-24+(-50+24)e^{-10t}', r'v_c=-24-26e^{-10t}\ \mathrm{V},\qquad t\ge0')),
      S(r'**Other:** $i=C\dfrac{dv_c}{dt}$.', r'i=0.025\cdot(260e^{-10t})=6.5e^{-10t}\ \mathrm{A},\qquad t\ge0^+')],
     r'$V_{Th}=-24\,\mathrm{V}$, $R_{Th}=4\,\Omega$, $\tau=0.1\,\mathrm{s}$, $v_c=-24-26e^{-10t}\,\mathrm{V}$, $i=6.5e^{-10t}\,\mathrm{A}$',
     cites=cite('AP7', 4, 5))
D.P(r'**Dependent source?** Use your Midterm 1 rule for $R_{Th}$, and keep the dependent source **on**:')
D.L([r'dependent **and** independent sources: $R_{Th}=\dfrac{V_{oc}}{I_{sc}}$',
     r'dependent sources only: a test source, $R_{Th}=\dfrac{V_{test}}{I_{test}}$'])
D.EX('Own example: RL step with a dependent source',
     r'''The inductor has no current before the switch closes at $t=0$. The diamond is a current source $0.5\,i_x$ pointing down, where $i_x$ is the current down through the right $4\,\Omega$.

''' + sch(r'''
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$"
R2 3,3 -> 3,0 "$4\,\Omega$" i="$i_x$"
wire 3,3 -> 6,3
G1 6,3 -> 6,0 "$0.5\,i_x$"
wire 6,3 -> 8,3
S1 8,3 -> 10,3 "$t=0$" action=close
L1 10,3 -> 10,0 "$1\,\mathrm{H}$" i="$i_L$"
wire 10,0 -> 0,0
label 3,3 "$a$" above
ground 0,0
''') + r'''

Find $i_L(t)$.''',
     [S(r'**Open circuit** (no inductor). Node $a$ at voltage $v$, so $i_x=\dfrac v4$. KCL at $a$: in from the left = out through $4\,\Omega$ and the diamond.',
        (r'\frac{12-v}{4}=\frac v4+0.5\cdot\frac v4', r'12-v=1.5v\quad\Longrightarrow\quad V_{oc}=4.8\,\mathrm{V}')),
      S(r'**Short circuit** (a wire from $a$ to ground). Then $v=0$, so $i_x=0$ and the diamond is $0$.', r'I_{sc}=\frac{12}{4}=3\,\mathrm{A}'),
      S(r'**Thévenin resistance.**', r'R_{Th}=\frac{V_{oc}}{I_{sc}}=\frac{4.8}{3}=1.6\,\Omega'),
      S(r'**After:** at DC the inductor **is** the short, so its final current is $I_{sc}$.', r'i_L(\infty)=3\,\mathrm{A}'),
      S(r'**$\tau$** and **Plug in** (start at $0$).', (r'\tau=\frac{1}{1.6}=0.625\,\mathrm{s}', r'i_L(t)=3-3e^{-1.6t}\ \mathrm{A},\qquad t\ge0'))],
     r'$i_L=3-3e^{-1.6t}\,\mathrm{A}$')
D.TRY('★ AP 7.8: RC step with two circuits',
      r'''Before $t=0$ the capacitor sits in circuit (1) for a long time. At $t=0$ it is moved into circuit (2).

(1) before:

''' + sch(r'''
V1 0,3 -> 0,0 "$75\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\mathrm{k\Omega}$"
R2 3,3 -> 3,0 "$10\,\mathrm{k\Omega}$"
wire 3,3 -> 6,3
C1 6,3 -> 6,0 "$40\,\mathrm{nF}$" v="$v_o$"
wire 6,0 -> 0,0
''') + r'''

(2) after:

''' + sch(r'''
C1 0,3 -> 0,0 "$40\,\mathrm{nF}$" v="$v_o$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$40\,\mathrm{k\Omega}$"
R2 3,3 -> 6,3 "$10\,\mathrm{k\Omega}$" i="$i_o$"
V1 6,0 -> 6,3 "$100\,\mathrm{V}$"
wire 6,0 -> 0,0
''') + r'''

Find (a) $v_o(t)$ and (b) $i_o(t)$ for $t\ge0$.''',
      [S(r'**Before:** divider in circuit (1).', r'v_o(0^-)=75\cdot\frac{10}{15}=50\,\mathrm{V}'),
       S(r'**After:** divider in circuit (2). The $100\,\mathrm{V}$ has its $+$ at the bottom.', r'v_o(\infty)=\frac{40}{50}(-100)=-80\,\mathrm{V}'),
       S(r'**$\tau$:** source off, $40\,\mathrm{k}\parallel10\,\mathrm{k}$.', (r'R_{eq}=8\,\mathrm{k\Omega}', r'\tau=(8000)(40\times10^{-9})=0.32\,\mathrm{ms}')),
       S(r'**Plug in** (a).', r'v_o=-80+(50+80)e^{-3125t}=-80+130e^{-3125t}\ \mathrm{V}'),
       S(r'**Other (b):** Ohm\'s law on the $10\,\mathrm{k}$. Its right end sits at $-100\,\mathrm{V}$.', r'i_o=\frac{v_o-(-100)}{10\,\mathrm{k}}=13e^{-3125t}+2\ \mathrm{mA}')],
      r'(a) $v_o=-80+130e^{-3125t}\,\mathrm{V}$ (b) $i_o=13e^{-3125t}+2\,\mathrm{mA}$', cites=cite('AP7', 6))

# ==================================================================================================== PART D
D.H('Part D · Sequential switching', cites=cite('E8', 4))
D.P(r'Goal: two switches flip at different times. Solve one time window at a time.')
D.P(r'A second switch flips at $t=35\,\mathrm{ms}$. What now?')
D.L([r'**Window 1** ($0\le t\le t_1$): the usual six steps.',
     r'**Hand-off:** plug $t_1$ into window 1. That value is the start of window 2, because $i_L$ and $v_C$ cannot jump.',
     r'**Window 2** ($t\ge t_1$): new circuit, new $\tau$, new final value. **Restart the clock** with $t-t_1$.'])
D.EQ(r'x(t)=x(\infty)+\big[x(t_1^+)-x(\infty)\big]\,e^{-(t-t_1)/\tau_2},\qquad t\ge t_1')
D.EX('★ Lecture example: two switches, one inductor',
     r'''Both switches have been closed for a long time. Switch 1 opens at $t=0$. Switch 2 opens at $t=35\,\mathrm{ms}$.

''' + sch(r'''
V1 0,3 -> 0,0 "$60\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$"
R2 3,3 -> 3,0 "$12\,\Omega$"
S1 3,3 -> 6,3 "$t=0$" state=closed action=open
R3 6,3 -> 6,0 "$6\,\Omega$"
R4 6,3 -> 9,3 "$3\,\Omega$"
L1 9,3 -> 9,0 "$150\,\mathrm{mH}$" i="$i_L$" v="$v_L$"
S2 9,3 -> 12,3 "$t=35\,\mathrm{ms}$" state=closed action=open
R5 12,3 -> 12,0 "$18\,\Omega$"
wire 12,0 -> 0,0
label 3,3 "$a$" above
ground 0,0
''') + r'''

Find $i_L(t)$ for (a) $0\le t\le35\,\mathrm{ms}$ and (b) $t\ge35\,\mathrm{ms}$.''',
     [S(r'**Before:** $L$ is a wire, so the $18\,\Omega$ is shorted and the $3\,\Omega$ goes to ground. Right of the switch: $6\parallel3=2\,\Omega$. Node $a$ sees $12\parallel2=\frac{12}{7}\,\Omega$.',
        (r'v_a=60\cdot\frac{12/7}{4+12/7}=18\,\mathrm{V}', r'i_L(0^-)=\frac{18}{3}=6\,\mathrm{A}')),
      S(r'**Window 1 $\tau$:** switch 1 open, so the source side is gone. $L$ sees $18\,\Omega\parallel(3+6)\,\Omega$.', (r'R=18\parallel9=6\,\Omega', r'\tau_1=\frac{0.15}{6}=25\,\mathrm{ms}')),
      S(r'**Window 1 (a):** no source, so it decays to $0$.', r'i_L=6e^{-40t}\ \mathrm{A},\qquad 0\le t\le35\,\mathrm{ms}'),
      S(r'**Hand-off** at $35\,\mathrm{ms}$.', r'i_L(0.035)=6e^{-1.4}=' + f'{i35:.3f}' + r'\,\mathrm{A}'),
      S(r'**Window 2 $\tau$:** switch 2 open too. Only $3+6\,\Omega$ is left.', r'\tau_2=\frac{0.15}{9}=16.67\,\mathrm{ms}'),
      S(r'**Window 2 (b):** restart the clock at $35\,\mathrm{ms}$.', r'i_L=' + f'{i35:.2f}' + r'\,e^{-60(t-0.035)}\ \mathrm{A},\qquad t\ge35\,\mathrm{ms}')],
     r'(a) $6e^{-40t}\,\mathrm{A}$ (b) $' + f'{i35:.2f}' + r'\,e^{-60(t-0.035)}\,\mathrm{A}$', cites=cite('E8', 6))
D.GRAPH(['title "$i_L(t)$ in the two windows"', 'x 0 0.12 label="$t$ (s)"', 'y 0 6.5 label="$i_L$ (A)"',
         f'curve "if(x<0.035, 6*exp(-40*x), {i35:.4f}*exp(-60*(x-0.035)))" color=1 label="$i_L$"',
         'vline "0.035" label="switch 2 opens"'],
        intro=r'Look at the curve at $t=35\,\mathrm{ms}$. Does $i_L$ jump there, or does only its slope change?')
D.P(r'Only the slope changes. The current is continuous; it just starts falling faster because $\tau_2<\tau_1$.')
D.TRY('★ Lecture example: three-position switch (RC)',
      r'''The capacitor is uncharged, with the switch at an open position $a$. At $t=0$ the switch moves to $b$. After $15\,\mathrm{ms}$ it moves to $c$ and stays there.

''' + sch(r'''
V1 0,3 -> 0,0 "$400\,\mathrm{V}$"
R1 0,3 -> 3,3 "$100\,\mathrm{k\Omega}$"
S1 3,3 -> 6,3 "$b$" action=close
C1 6,3 -> 6,0 "$0.1\,\mu\mathrm{F}$" v="$v$"
S2 6,3 -> 9,3 "$c$"
R2 9,3 -> 9,0 "$50\,\mathrm{k\Omega}$"
wire 9,0 -> 0,0
ground 0,0
''') + r'''

(a) Find $v(t)$. (b) When is $v=200\,\mathrm{V}$?''',
      [S(r'**Window 1** (at $b$): start $0$, final $400\,\mathrm{V}$, $\tau_1=(100\,\mathrm{k})(0.1\,\mu\mathrm{F})=10\,\mathrm{ms}$.', r'v=400-400e^{-100t}\ \mathrm{V},\qquad 0\le t\le15\,\mathrm{ms}'),
       S(r'**Hand-off** at $15\,\mathrm{ms}$.', r'v(0.015)=400\left(1-e^{-1.5}\right)=' + f'{v15:.2f}' + r'\,\mathrm{V}'),
       S(r'**Window 2** (at $c$): no source, $\tau_2=(50\,\mathrm{k})(0.1\,\mu\mathrm{F})=5\,\mathrm{ms}$. Restart the clock.', r'v=' + f'{v15:.2f}' + r'\,e^{-200(t-0.015)}\ \mathrm{V},\qquad t\ge15\,\mathrm{ms}'),
       S(r'**200 V on the way up** (window 1).', (r'400-400e^{-100t}=200', r't=\frac{\ln2}{100}=6.93\,\mathrm{ms}')),
       S(r'**200 V on the way down** (window 2).', (r'' + f'{v15:.2f}' + r'\,e^{-200(t-0.015)}=200', r't=0.015+\frac{1}{200}\ln\frac{' + f'{v15:.2f}' + r'}{200}=' + f'{t200 * 1e3:.2f}' + r'\,\mathrm{ms}'))],
      r'(a) $400-400e^{-100t}\,\mathrm{V}$, then $' + f'{v15:.2f}' + r'\,e^{-200(t-0.015)}\,\mathrm{V}$ (b) $6.93\,\mathrm{ms}$ and $' + f'{t200 * 1e3:.2f}' + r'\,\mathrm{ms}$',
      cites=cite('E8', 5))
D.TRY('★ AP 7.10: an inductor shorted out ($\\tau=\\infty$)',
      r'''Before $t=0$, a $5\,\mathrm{H}$ inductor carries $i_L(0^-)=2\,\mathrm{A}$ (from a $10\,\mathrm{V}$ source and $5\,\Omega$). At $t=0$ a wire is connected straight across the inductor, so it sees $0\,\Omega$. At $t=5\,\mathrm{s}$ everything except a $1\,\Omega$ resistor is disconnected, leaving the inductor with only that $1\,\Omega$. Find $i_L(t)$.''',
      [S(r'**Window 1:** the inductor sees $R=0$.', r'\tau_1=\frac{L}{0}=\infty\quad\Longrightarrow\quad e^{-t/\tau_1}=1'),
       S(r'So the current just stays where it was. A shorted inductor keeps its current.', r'i_L=2\,\mathrm{A},\qquad 0\le t\le5\,\mathrm{s}'),
       S(r'**Window 2:** only $1\,\Omega$.', r'\tau_2=\frac51=5\,\mathrm{s}'),
       S(r'**Restart the clock** at $5\,\mathrm{s}$.', r'i_L=2e^{-0.2(t-5)}\ \mathrm{A},\qquad t\ge5\,\mathrm{s}')],
      r'$2\,\mathrm{A}$ for $0\le t\le5\,\mathrm{s}$; $2e^{-0.2(t-5)}\,\mathrm{A}$ after', cites=cite('AP7', 8, 9))

# ==================================================================================================== SUMMARY
D.H('Formula summary')
D.EQ(r'x(t)=x(\infty)+\big[x(0^+)-x(\infty)\big]\,e^{-t/\tau}')
D.T(['What', 'Formula / move'],
    [['Time constant', r'$\tau=\dfrac{L}{R_{eq}}$ or $\tau=R_{eq}C$ ($R_{eq}$ seen by $L$/$C$, sources off)'],
     ['Sources off', r'voltage source $\to$ wire, current source $\to$ gap'],
     ['Start', r'DC before the switch: $L$ = wire, $C$ = gap; carry $i_L$, $v_C$ over to $0^+$'],
     ['Final', r'DC after the switch; natural response: $x(\infty)=0$'],
     ['Thévenin', r'$v_C(\infty)=V_{Th}$, $i_L(\infty)=\dfrac{V_{Th}}{R_{Th}}$, $\tau=R_{Th}C$ or $\dfrac{L}{R_{Th}}$'],
     ['Dependent source', r'$R_{Th}=\dfrac{V_{oc}}{I_{sc}}$ (or a test source if no independent source)'],
     ['Other quantities', r'$v_L=L\dfrac{di_L}{dt}$, $i_C=C\dfrac{dv_C}{dt}$, Ohm, dividers (valid for $t\ge0^+$)'],
     ['Energy', r'$p_R\propto e^{-2t/\tau}$; $\displaystyle\int_0^\infty Ae^{-at}dt=\dfrac{A}{a}$'],
     ['Sequential', r'$x(t)=x(\infty)+[x(t_1)-x(\infty)]e^{-(t-t_1)/\tau_2}$ for $t\ge t_1$']])
D.P(r'Six steps every time: **Before, Jump, After, $\tau$, Plug in, Other.** Practice: questions 5–8 in **Midterm 2 Practice Questions**.')

D.save()
