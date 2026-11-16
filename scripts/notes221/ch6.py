r"""ELEC 221 Midterm 2 - Ch 6: inductors and capacitors (Week 6 lecture, Tutorial 6, Ch 6 Assessment Problems).

Gradual-Parts style (memory notes-gradual-parts): plain-words intro -> overview table -> Part A (one element),
Part B (several elements). Each topic: question -> rule -> short example -> one plain "why" line -> Try it.
Every number below is computed here and checked with near().
"""
import math

from lib221 import Doc, S, cite, near, sch

E = math.exp
D = Doc('ch6', 'Midterm 2 · 1. Inductors and Capacitors', ['inductance', 'capacitance'])

# ------------------------------------------------------------------------------------------ numbers
# Lecture example (W6 p15-17, Nilsson Ex 6.1): L = 100 mH, i = 10 t e^{-5t}
i_pk = 10 * 0.2 * E(-1)                                   # 0.7358 A at t = 0.2 s
w_pk = 0.5 * 0.1 * i_pk ** 2                              # 27.07 mJ
near(i_pk, 0.7358); near(w_pk * 1e3, 27.07)
# Tutorial 6 Q3 = AP 6.1: L = 50 uH, i = 18 t e^{-10t}
v02 = 0.9e-3 * E(-2) * (1 - 2); i02 = 18 * 0.2 * E(-2)
near(v02 * 1e6, -121.8); near(i02 * 1e3, 487.2); near(v02 * i02 * 1e6, -59.34, rel=3e-3)
near(0.5 * 50e-6 * i02 ** 2 * 1e6, 5.934, rel=3e-3)
imax = 18 * 0.1 * E(-1); near(imax * 1e3, 662.2); near(0.5 * 50e-6 * imax ** 2 * 1e6, 10.96, rel=3e-3)
# AP 6.2-6.3: C = 5 uF, v = 500 t e^{-2500t}
t1 = 100e-6
v1 = 500 * t1 * E(-2500 * t1); i1 = 2.5e-3 * E(-2500 * t1) * (1 - 2500 * t1)
near(v1 * 1e3, 38.94); near(i1 * 1e3, 1.460, rel=3e-3); near(v1 * i1 * 1e6, 56.86, rel=3e-3)
near(0.5 * 5e-6 * v1 ** 2 * 1e9, 3.79, rel=3e-3)
vmax = 500 * 0.4e-3 * E(-1); near(vmax * 1e3, 73.58); near(0.5 * 5e-6 * vmax ** 2 * 1e9, 13.53, rel=3e-3)
# A2 example: C = 4 uF, v = 20 e^{-1000t}  ->  i = -80 e^{-1000t} mA
near(4e-6 * 20 * -1000, -0.08)
# A2 try: C = 2 uF, i = 6 mA for 0..5 ms, v(0) = 3 V -> v = 3 + 3000 t ; v(5 ms) = 18 V
near(3 + 6e-3 / 2e-6 * 5e-3, 18)
# A4: 12 V, 2 ohm, L || 4 ohm: i_L = 6 A ; Try: C = 10 uF instead -> v_C = 8 V, w = 320 uJ
near(12 / 2, 6); near(12 * 4 / 6, 8); near(0.5 * 10e-6 * 64 * 1e6, 320)
# AP 6.4: 48 mH (i1(0) = -0.6) || 24 mH (i2(0) = 0.2), v = 0.1 e^{-25t}
Leq = 48 * 24 / 72; near(Leq, 16)
k = 0.1 / 25  # integral of 0.1 e^{-25x} from 0 to inf
near(k / 0.016, 0.25); near(k / 0.048, 0.08333); near(k / 0.024, 0.16667)
near(0.25 - 0.4, -0.15); near(0.08333 - 0.6, -0.51667); near(0.16667 + 0.2, 0.36667)
# AP 6.5: 100 uF (15 V) series 25 uF (-10 V), i = 0.05 e^{-200t}
q = 0.05 / 200
near(q / 20e-6, 12.5); near(q / 100e-6, 2.5); near(q / 25e-6, 10); near(0.5 * 100e-6 * 17.5 ** 2 * 1e3, 15.3125)
# Lecture series caps (W6 p38): C1 = 1 uF, C2 = C3 = 2 uF, v_s = 3 sin 2t, v_C1(0) = 10
Ceq = 1 / (1 / 1 + 1 / 2 + 1 / 2); near(Ceq, 0.5)
# Tutorial 6 Q2 (black box)
near(0.5 * 8 * 100 + 0.5 * 32 * 25 + 0.5 * 3.6 * 25, 845); near(0.5 * 10 * 25, 125)
near(0.5 * 8 * 36 + 0.5 * 32 * 36, 720)
# B2 try: 6 H (3 A) || 3 H (-1 A) into a resistor
near(0.5 * 6 * 9 + 0.5 * 3 * 1, 28.5); near(0.5 * 2 * 4, 4); near(0.5 * 6 * (7 / 3) ** 2 + 0.5 * 3 * (7 / 3) ** 2, 24.5)
# Practice Q3: 0.5 uF cap, i = 2 mA for 0..1 ms then -1 mA for 1..3 ms, v(0) = 0
near(2e-3 * 1e-3 / 0.5e-6, 4); near(4 - 1e-3 * 2e-3 / 0.5e-6, 0); near(0.5 * 0.5e-6 * 16 * 1e6, 4)
# Practice Q4: 30 V, 5 ohm, L = 2 H to node a; a: 10 ohm and C = 50 uF to ground
near(30 / 15 * 10, 20); near(30 / 15, 2); near(0.5 * 2 * 4, 4); near(0.5 * 50e-6 * 400 * 1e3, 10)

# ==================================================================================================== intro
D.P(r'**Note 1 of 3 · Textbook 6.1–6.3.** Inductors, capacitors, and combining them. (6.4 mutual inductance is not on the midterm.)')
D.P(r'The one idea: $L$ and $C$ **store** energy instead of burning it, and each one resists sudden change. An inductor resists a jump in its **current**, a capacitor a jump in its **voltage**. RL/RC and RLC circuits (notes 2 and 3) are just consequences of that.',
    cites=cite('W6', 14))
D.P(r'A typical question gives you $i(t)$ or $v(t)$ for one element and asks for the other one, the power and the stored energy. Or it gives a few $L$s or $C$s to combine, and asks where the energy ends up.')
D.T(['Topic', 'What you are learning', 'Where'],
    [[r'1. Inductor $v$ and $i$', r'Turn $i(t)$ into $v(t)$, and back', 'A1'],
     [r'2. Capacitor $v$ and $i$', 'The same moves for a capacitor', 'A2'],
     ['3. Power and energy', 'Absorbing or delivering? Stored energy, max energy', 'A3'],
     ['4. DC rules', r'$L$ = wire, $C$ = gap, what cannot jump', 'A4'],
     ['5. Series and parallel', r'Combine $L$s and $C$s with their starting values', 'B1'],
     ['6. Trapped energy', 'The "black box" question', 'B2']])
D.L([r'**Part A · One element.** The four rules you use in every question.',
     r'**Part B · Several elements.** Combine them, then track where the energy goes.'])
D.P(r'Every topic runs the same way: what it is → the formula → a worked example → a **Try it** (attempt it before opening the solution). ★ = from your lectures, tutorials or Assessment Problems. A formula summary is at the end; mixed test-style questions are in **Midterm 2 Practice Questions**.')

# ==================================================================================================== PART A
D.H('Part A · One element')
D.P(r'Goal: given $i(t)$ or $v(t)$ for one $L$ or one $C$, find everything else.')

# ---- A1 -------------------------------------------------------------------------------------------
D.H('A1 · Inductor: from $i$ to $v$, and back', level=2, cites=cite('W6', 11, 12))
D.P(r'You know the current through an inductor. What is its voltage?')
D.EQ(r'v=L\,\frac{di}{dt}')
D.P(r'The voltage depends on how **fast** the current changes, not on how big it is.')
D.L([r'Current constant: $\dfrac{di}{dt}=0$, so $v=0$.',
     r'Current rising fast: big positive $v$.',
     r'Current falling: negative $v$.'])
D.EX('★ Lecture example: voltage from current',
     r'''The current through a $100\,\mathrm{mH}$ inductor is $i=10te^{-5t}\ \mathrm{A}$ for $t\ge0$ (and $0$ before). Find $v(t)$.

''' + sch(r'''
I1 0,0 -> 0,3 "$i(t)$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$100\,\mathrm{mH}$" v="$v$" i="$i$"
wire 3,0 -> 0,0
'''),
     [S(r'**Check the signs.** $i$ enters the $+$ end of $v$, so use $v=+L\,\dfrac{di}{dt}$.'),
      S(r'**Differentiate** with the product rule ($t$ times $e^{-5t}$).',
        (r'\frac{di}{dt}=10\left[e^{-5t}+t(-5e^{-5t})\right]', r'=10e^{-5t}(1-5t)')),
      S(r'**Multiply** by $L=0.1\,\mathrm{H}$.', r'v=0.1\cdot10e^{-5t}(1-5t)=e^{-5t}(1-5t)\ \mathrm{V}')],
     r'$v=e^{-5t}(1-5t)\ \mathrm{V}$ for $t>0$', cites=cite('W6', 15, 17))
D.CO('reminder', r'''**Product rule** (you need it in almost every Ch 6 question):

$$
\frac{d}{dt}\left(t\,e^{-at}\right)=e^{-at}(1-at)
$$

Example: $\dfrac{d}{dt}\left(te^{-10t}\right)=e^{-10t}(1-10t)$.''')
D.CO('warning', r'**Sign check.** $v=+L\dfrac{di}{dt}$ only when the arrow for $i$ points **into the $+$ end** of $v$. If it points into the $-$ end, use $v=-L\dfrac{di}{dt}$.')
D.P(r'Now the other way. You know $v(t)$. What is $i(t)$?')
D.EQ(r'i(t)=\frac{1}{L}\int_{t_0}^{t}v\,d\tau+i(t_0)')
D.P(r'Add up the voltage over time, divide by $L$, then add the current you **started** with.')
D.P(r'**Example.** $L=0.5\,\mathrm{H}$, $i(0)=1\,\mathrm{A}$, and $v=6\,\mathrm{V}$ for $0\le t\le2\,\mathrm{s}$, then $v=0$.')
D.EQ(r'\begin{gathered}i(t)=\frac{1}{0.5}\int_0^t 6\,d\tau+1 \\ i(t)=1+12t\ \mathrm{A}\qquad(0\le t\le2\,\mathrm{s})\end{gathered}')
D.P(r'At $t=2\,\mathrm{s}$ the current is $1+24=25\,\mathrm{A}$. After that, $v=0$ so nothing is added: the current **stays** at $25\,\mathrm{A}$. It does not fall back to $0$.')
D.TRY('★ Tutorial 6 Q1: a voltage pulse',
      r'''The voltage across a $200\,\mu\mathrm{H}$ inductor is $5\,\mathrm{mV}$ for $0\le t\le2\,\mathrm{ms}$ and $0$ after. The current is $0$ for $t\le0$, and it enters the $+$ end of $v$.

(a) Find $i(t)$ for $0\le t\le2\,\mathrm{ms}$. (b) Find $i(t)$ for $t\ge2\,\mathrm{ms}$. (c) Sketch $i(t)$.''',
      [S(r'**Integrate** over the pulse, starting from $i(0)=0$.',
         (r'i(t)=\frac{1}{200\times10^{-6}}\int_0^t 5\times10^{-3}\,d\tau+0', r'i(t)=25t\ \mathrm{A}\qquad(t\ \text{in seconds})')),
       S(r'**End of the pulse.** Plug in $t=2\,\mathrm{ms}$.', r'i(2\,\mathrm{ms})=25(0.002)=50\,\mathrm{mA}'),
       S(r'**After the pulse** $v=0$, so the current stays where it was.', r'i(t)=50\,\mathrm{mA}\qquad(t\ge2\,\mathrm{ms})'),
       S(r'**Sketch:** a straight ramp from $0$ to $50\,\mathrm{mA}$ over $2\,\mathrm{ms}$, then flat.')],
      r'(a) $i=25t\ \mathrm{A}$ (b) $i=50\,\mathrm{mA}$ (c) ramp, then flat', diff='introductory',
      cites=cite('T6', 1))

# ---- A2 -------------------------------------------------------------------------------------------
D.H('A2 · Capacitor: the same moves, $v$ and $i$ swapped', level=2, cites=cite('W6', 25))
D.P(r'For a capacitor, the current depends on how fast the **voltage** changes.')
D.EQ(r'i=C\,\frac{dv}{dt}')
D.EQ(r'v(t)=\frac{1}{C}\int_{t_0}^{t}i\,d\tau+v(t_0)')
D.P(r'**Example.** $C=4\,\mu\mathrm{F}$ and $v=20e^{-1000t}\ \mathrm{V}$, with $i$ entering the $+$ end.')
D.EQ(r'\begin{gathered}i=4\times10^{-6}\cdot\left(-20000\,e^{-1000t}\right) \\ i=-0.08\,e^{-1000t}\ \mathrm{A}=-80\,e^{-1000t}\ \mathrm{mA}\end{gathered}')
D.P(r'The minus sign means the current really flows the other way: the capacitor is discharging.')
D.P(r'Here is the same toolbox side by side. Learn one column, and the other is the same with $v\leftrightarrow i$ and $L\leftrightarrow C$.')
D.T(['', 'Inductor $L$', 'Capacitor $C$'],
    [['Rule', r'$v=L\dfrac{di}{dt}$', r'$i=C\dfrac{dv}{dt}$'],
     ['Integral', r'$i=\dfrac{1}{L}\displaystyle\int v\,d\tau+i(t_0)$', r'$v=\dfrac{1}{C}\displaystyle\int i\,d\tau+v(t_0)$'],
     ['Energy', r'$w=\tfrac12Li^2$', r'$w=\tfrac12Cv^2$'],
     ['Cannot jump', r'current $i_L$', r'voltage $v_C$'],
     ['At DC', 'a wire (short)', 'a gap (open)']])
D.TRY('Voltage from a constant current',
      r'A $2\,\mu\mathrm{F}$ capacitor starts at $v(0)=3\,\mathrm{V}$. A constant $6\,\mathrm{mA}$ flows into its $+$ end for $5\,\mathrm{ms}$. Find $v(t)$ and $v(5\,\mathrm{ms})$.',
      [S(r'**Integrate** the constant current, then add the starting voltage.',
         (r'v(t)=\frac{1}{2\times10^{-6}}\int_0^t 6\times10^{-3}\,d\tau+3', r'v(t)=3+3000t\ \mathrm{V}')),
       S(r'**Plug in** $t=5\,\mathrm{ms}$.', r'v(5\,\mathrm{ms})=3+3000(0.005)=18\,\mathrm{V}')],
      r'$v=3+3000t\ \mathrm{V}$; $v(5\,\mathrm{ms})=18\,\mathrm{V}$', diff='introductory')

# ---- A3 -------------------------------------------------------------------------------------------
D.H('A3 · Power and energy', level=2, cites=cite('W6', 13, 26))
D.P(r'Is the element taking energy in right now, or giving it back?')
D.EQ(r'p=v\,i')
D.L([r'$p>0$: **absorbing**. The element is storing energy.',
     r'$p<0$: **delivering**. It is giving stored energy back.'])
D.P(r'How much energy is stored right now?')
D.EQ(r'w_L=\tfrac12Li^2\qquad\qquad w_C=\tfrac12Cv^2')
D.P(r'Energy is never negative, because $i$ and $v$ are squared. It only depends on the current (for $L$) or voltage (for $C$) at that moment.')
D.P(r'**Maximum energy.** $w_L$ is biggest when $|i|$ is biggest. So set $\dfrac{di}{dt}=0$, solve for $t$, and plug that $t$ into $w$. For a capacitor, use $\dfrac{dv}{dt}=0$ instead. Also compare with the values at $t=0$ and $t\to\infty$, in case the biggest value sits at an end.')
D.EX('★ Lecture example continued: power and maximum energy',
     r'Same inductor: $L=100\,\mathrm{mH}$, $i=10te^{-5t}\ \mathrm{A}$, $v=e^{-5t}(1-5t)\ \mathrm{V}$. When is the inductor storing energy, and when is it delivering? What is the maximum stored energy?',
     [S(r'**Power** is $v$ times $i$.', r'p=vi=10t\,e^{-10t}(1-5t)\ \mathrm{W}'),
      S(r'**Read the sign.** $10te^{-10t}$ is positive for $t>0$. So the sign comes from $(1-5t)$.',
        (r'p>0\quad\text{for }0<t<0.2\,\mathrm{s}\quad\text{(storing)}', r'p<0\quad\text{for }t>0.2\,\mathrm{s}\quad\text{(delivering)}')),
      S(r'**Max current:** set $\dfrac{di}{dt}=10e^{-5t}(1-5t)=0$.',
        (r't=0.2\,\mathrm{s}', r'i_{\max}=10(0.2)e^{-1}=' + f'{i_pk:.4f}' + r'\ \mathrm{A}')),
      S(r'**Max energy.** At the ends, $i(0)=0$ and $i(\infty)=0$, so the peak really is at $0.2\,\mathrm{s}$.',
        r'w_{\max}=\tfrac12(0.1)(' + f'{i_pk:.4f}' + r')^2=' + f'{w_pk * 1e3:.2f}' + r'\ \mathrm{mJ}')],
     r'Storing for $0<t<0.2\,\mathrm{s}$, delivering after; $w_{\max}=' + f'{w_pk * 1e3:.2f}' + r'\,\mathrm{mJ}$ at $t=0.2\,\mathrm{s}$',
     cites=cite('W6', 15, 18))
D.P(r'Notice: the current peak ($t=0.2\,\mathrm{s}$) is exactly where $v=0$ and where $p$ flips sign. Before the peak the inductor charges up, after it gives energy back.')
D.TRY('★ AP 6.2–6.3: a capacitor, absorbing or delivering?',
      r'''The voltage across a $5\,\mu\mathrm{F}$ capacitor is $v=500te^{-2500t}\ \mathrm{V}$ for $t\ge0$ (passive sign convention).

(a) Find $i(t)$. (b) Find $p$ at $t=100\,\mu\mathrm{s}$. Is the capacitor absorbing or delivering? (c) Find the stored energy at $100\,\mu\mathrm{s}$. (d) Find the maximum stored energy.''',
      [S(r'**Differentiate** with the product rule, then multiply by $C$.',
         (r'\frac{dv}{dt}=500e^{-2500t}(1-2500t)', r'i=5\times10^{-6}\cdot500e^{-2500t}(1-2500t)', r'i=2.5e^{-2500t}(1-2500t)\ \mathrm{mA}')),
       S(r'**Plug in** $t=100\,\mu\mathrm{s}$, so $2500t=0.25$.',
         (r'v=500(10^{-4})e^{-0.25}=' + f'{v1 * 1e3:.2f}' + r'\,\mathrm{mV}', r'i=2.5e^{-0.25}(0.75)=' + f'{i1 * 1e3:.3f}' + r'\,\mathrm{mA}')),
       S(r'**Power.** It is positive, so the capacitor is absorbing.', r'p=vi=' + f'{v1 * i1 * 1e6:.2f}' + r'\,\mu\mathrm{W}'),
       S(r'**Energy now.**', r'w=\tfrac12(5\times10^{-6})(' + f'{v1:.5f}' + r')^2=' + f'{0.5 * 5e-6 * v1 ** 2 * 1e9:.2f}' + r'\,\mathrm{nJ}'),
       S(r'**Max energy:** set $\dfrac{dv}{dt}=0$, so $1-2500t=0$.',
         (r't=0.4\,\mathrm{ms},\qquad v_{\max}=500(0.0004)e^{-1}=' + f'{vmax * 1e3:.2f}' + r'\,\mathrm{mV}',
          r'w_{\max}=\tfrac12(5\times10^{-6})(' + f'{vmax:.5f}' + r')^2=' + f'{0.5 * 5e-6 * vmax ** 2 * 1e9:.2f}' + r'\,\mathrm{nJ}'))],
      r'(a) $i=2.5e^{-2500t}(1-2500t)\ \mathrm{mA}$ (b) $' + f'{v1 * i1 * 1e6:.2f}' + r'\,\mu\mathrm{W}$, absorbing (c) $'
      + f'{0.5 * 5e-6 * v1 ** 2 * 1e9:.2f}' + r'\,\mathrm{nJ}$ (d) $' + f'{0.5 * 5e-6 * vmax ** 2 * 1e9:.2f}' + r'\,\mathrm{nJ}$ at $0.4\,\mathrm{ms}$',
      cites=cite('AP6', 2))

# ---- A4 -------------------------------------------------------------------------------------------
D.H('A4 · DC rules and what cannot jump', level=2, cites=cite('W6', 28, 40))
D.P(r'This topic is short, but Ch 7 and Ch 8 use it in every question.')
D.P(r'What does an inductor look like after a switch has been still for a long time? All values are constant (DC).')
D.L([r'**Inductor at DC:** $i$ is constant, so $v=L\dfrac{di}{dt}=0$. It acts like a **wire** (short circuit).',
     r'**Capacitor at DC:** $v$ is constant, so $i=C\dfrac{dv}{dt}=0$. It acts like a **gap** (open circuit).'])
D.P(r'What happens at the instant a switch flips ($t=0^-$ is just before, $t=0^+$ just after)?')
D.EQ(r'i_L(0^+)=i_L(0^-)\qquad\qquad v_C(0^+)=v_C(0^-)')
D.P(r'A sudden jump in $i_L$ would need $\dfrac{di}{dt}=\infty$, which means infinite voltage. Same for $v_C$. Everything else **can** jump: $v_L$, $i_C$, and every resistor current.')
D.EX('Inductor current at DC',
     r'''The circuit has been on for a long time. Find $i_L$ and the current in the $4\,\Omega$ resistor.

''' + sch(r'''
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
L1 3,3 -> 3,0 "$L$" i="$i_L$"
wire 3,3 -> 6,3
R2 6,3 -> 6,0 "$4\,\Omega$"
wire 6,0 -> 0,0
ground 0,0
'''),
     [S(r'**Replace** the inductor by a wire (DC).'),
      S(r'**Spot** the short: the wire is in parallel with $4\,\Omega$, so the $4\,\Omega$ has $0\,\mathrm{V}$ across it.', r'i_{4\Omega}=0'),
      S(r'**Solve** the loop: all the current goes through $2\,\Omega$ and the wire.', r'i_L=\frac{12}{2}=6\,\mathrm{A}')],
     r'$i_L=6\,\mathrm{A}$, $i_{4\Omega}=0$')
D.TRY('Capacitor voltage at DC',
      r'Same circuit, but the inductor is replaced by a $10\,\mu\mathrm{F}$ capacitor (with $v_C$ $+$ at the top). It has been on for a long time. Find $v_C$, $i_C$, and the stored energy.',
      [S(r'**Replace** the capacitor by a gap. No current flows in it.', r'i_C=0'),
       S(r'**Divide** the voltage: $2\,\Omega$ and $4\,\Omega$ are now in series.', r'v_C=12\cdot\frac{4}{2+4}=8\,\mathrm{V}'),
       S(r'**Energy.**', r'w=\tfrac12(10\times10^{-6})(8)^2=320\,\mu\mathrm{J}')],
      r'$v_C=8\,\mathrm{V}$, $i_C=0$, $w=320\,\mu\mathrm{J}$', diff='introductory')

# ==================================================================================================== PART B
D.H('Part B · Several inductors or capacitors')
D.P(r'Goal: replace a group by one element, keep track of the starting values, and follow the energy.')

# ---- B1 -------------------------------------------------------------------------------------------
D.H('B1 · Series and parallel, with starting values', level=2, cites=cite('W6', 30, 31, 35, 37))
D.P(r'Two inductors in parallel. Can you swap them for one?')
D.P(r'Yes. Inductors combine like resistors. Capacitors do the **opposite**.')
D.T(['', 'Series', 'Parallel'],
    [['Inductors', r'$L_1+L_2$', r'$\dfrac{L_1L_2}{L_1+L_2}$'],
     ['Capacitors', r'$\dfrac{C_1C_2}{C_1+C_2}$', r'$C_1+C_2$']])
D.L([r'$24\,\mathrm{mH}\parallel48\,\mathrm{mH}=\dfrac{24\cdot48}{72}=16\,\mathrm{mH}$',
     r'$100\,\mu\mathrm{F}$ in series with $25\,\mu\mathrm{F}$: $\dfrac{100\cdot25}{125}=20\,\mu\mathrm{F}$'])
D.P(r'The new element also needs a **starting value**:')
D.L([r'**Parallel inductors:** add the starting currents (KCL). Example: $-0.6\,\mathrm{A}$ and $0.2\,\mathrm{A}$ give $i(0)=-0.4\,\mathrm{A}$.',
     r'**Series capacitors:** add the starting voltages (KVL). Example: $15\,\mathrm{V}$ and $-10\,\mathrm{V}$ give $v(0)=5\,\mathrm{V}$.'])
D.CO('warning', r'Keep the signs. A current that points the other way, or a voltage with its $+$ on the other side, goes in with a minus.')
D.EX('★ AP 6.4: two inductors in parallel',
     r'''Two inductors are in parallel. At $t=0$, $i_1(0)=-0.6\,\mathrm{A}$ and $i_2(0)=0.2\,\mathrm{A}$. For $t\ge0$ the voltage is $v=0.1e^{-25t}\ \mathrm{V}$.

''' + sch(r'''
X1 0,3 -> 0,0 "rest of circuit" i="$i$" i_rev
wire 0,3 -> 6,3
L1 3,3 -> 3,0 "$48\,\mathrm{mH}$" i="$i_1$" v="$v$"
L2 6,3 -> 6,0 "$24\,\mathrm{mH}$" i="$i_2$"
wire 6,0 -> 0,0
''') + r'''

Find (a) $L_{eq}$, (b) $i(0)$, (c) $i(t)$, (d) $i_1(t)$ and $i_2(t)$.''',
     [S(r'**Combine.**', r'L_{eq}=\frac{48\cdot24}{48+24}=16\,\mathrm{mH}'),
      S(r'**Start:** add the starting currents.', r'i(0)=-0.6+0.2=-0.4\,\mathrm{A}'),
      S(r'**Integrate** the voltage once. You reuse this number three times.',
        (r'\int_0^t0.1e^{-25\tau}\,d\tau=0.004\left(1-e^{-25t}\right)',)),
      S(r'**Total current:** divide by $L_{eq}$ and add $i(0)$.',
        (r'i=\frac{0.004}{0.016}\left(1-e^{-25t}\right)-0.4', r'i=-0.15-0.25e^{-25t}\ \mathrm{A}')),
      S(r'**Each branch:** same voltage, own $L$, own start.',
        (r'i_1=\frac{0.004}{0.048}\left(1-e^{-25t}\right)-0.6=-0.5167-0.0833e^{-25t}\ \mathrm{A}',
         r'i_2=\frac{0.004}{0.024}\left(1-e^{-25t}\right)+0.2=0.3667-0.1667e^{-25t}\ \mathrm{A}')),
      S(r'**Check:** $i_1+i_2$ should equal $i$.', (r'i_1+i_2=(-0.5167+0.3667)+(-0.0833-0.1667)e^{-25t}', r'=-0.15-0.25e^{-25t}\ \checkmark'))],
     r'(a) $16\,\mathrm{mH}$ (b) $-0.4\,\mathrm{A}$ (c) $i=-0.15-0.25e^{-25t}\ \mathrm{A}$ (d) $i_1=-0.5167-0.0833e^{-25t}\ \mathrm{A}$, $i_2=0.3667-0.1667e^{-25t}\ \mathrm{A}$',
     cites=cite('AP6', 2))
D.TRY('★ Lecture example: series capacitors',
      r'''A source $v_s=3\sin2t\ \mathrm{V}$ drives $C_1=1\,\mu\mathrm{F}$, $C_2=2\,\mu\mathrm{F}$ and $C_3=2\,\mu\mathrm{F}$ in series. Given $v_{C1}(0)=10\,\mathrm{V}$, find the loop current $i_s(t)$ and $v_{C1}(t)$.

''' + sch(r'''
V1 0,3 -> 0,0 "$v_s(t)$" i="$i_s$" i_rev
C1 0,3 -> 3,3 "$1\,\mu\mathrm{F}$" v="$v_{C1}$"
C2 3,3 -> 6,3 "$2\,\mu\mathrm{F}$"
C3 6,3 -> 6,0 "$2\,\mu\mathrm{F}$"
wire 6,0 -> 0,0
'''),
      [S(r'**Combine** the series capacitors.', (r'\frac{1}{C_{eq}}=\frac11+\frac12+\frac12=2', r'C_{eq}=0.5\,\mu\mathrm{F}')),
       S(r'**Current** from the source voltage: $i_s=C_{eq}\dfrac{dv_s}{dt}$.', r'i_s=0.5\times10^{-6}\cdot6\cos2t=3\cos2t\ \mu\mathrm{A}'),
       S(r'**Integrate** that current through $C_1$ and add its start.',
         (r'v_{C1}=\frac{1}{10^{-6}}\int_0^t3\times10^{-6}\cos2\tau\,d\tau+10', r'v_{C1}=10+1.5\sin2t\ \mathrm{V}'))],
      r'$i_s=3\cos2t\ \mu\mathrm{A}$; $v_{C1}=10+1.5\sin2t\ \mathrm{V}$', cites=cite('W6', 38, 39))

# ---- B2 -------------------------------------------------------------------------------------------
D.H('B2 · Trapped energy (the black box question)', level=2, cites=cite('T6', 2))
D.P(r'Charged inductors are connected to a "black box" at $t=0$. How much energy reaches the box? How much stays stuck in the inductors forever?')
D.P(r'The trick: the **total** current into the box can die out, while each inductor still carries current. That leftover current just circles around the loop of parallel inductors. Its energy is **trapped**.')
D.EQ(r'w_{\text{delivered}}=\tfrac12L_{eq}\,i(0)^2\qquad(\text{when }i(\infty)=0)')
D.EQ(r'w_{\text{trapped}}=w_{\text{initial}}-w_{\text{delivered}}')
D.P(r'Check it with the final currents: $w_{\text{trapped}}=\tfrac12L_1i_1(\infty)^2+\tfrac12L_2i_2(\infty)^2+\dots$')
D.EX('★ Tutorial 6 Q2: three inductors and a black box',
     r'''The switch opens at $t=0$ and connects the inductors to the black box. For $t\ge0$, $v_b=1250e^{-25t}\ \mathrm{V}$. Given $i_1(0)=10\,\mathrm{A}$ and $i_2(0)=-5\,\mathrm{A}$.

''' + sch(r'''
L1 0,0 -> 0,3 "$8\,\mathrm{H}$" i="$i_1$"
L2 3,0 -> 3,3 "$32\,\mathrm{H}$" i="$i_2$"
wire 0,3 -> 3,3 -> 6,3 -> 9,3
wire 0,0 -> 3,0
L3 6,0 -> 3,0 "$3.6\,\mathrm{H}$" i="$i_o$"
wire 6,0 -> 9,0
S1 6,3 -> 6,0 "$t=0$" state=closed action=open
X1 9,3 -> 9,0 "black box" v="$v_b$"
''') + r'''

Find (a) $i_o(0)$, (b) $i_o(t)$, (c) $i_1(t)$ and $i_2(t)$, (d) the initial stored energy, (e) the energy delivered to the box, (f) the trapped energy.''',
     [S(r'**Start (a).** KCL where the three inductors meet.', r'i_o(0)=i_1(0)+i_2(0)=10-5=5\,\mathrm{A}'),
      S(r'**Combine** into one inductor.', r'L_{eq}=(8\parallel32)+3.6=6.4+3.6=10\,\mathrm{H}'),
      S(r'**Integrate (b).** $i_o$ leaves the box at its $-$ end and enters the inductors there. So the sign is minus.',
        (r'i_o=-\frac{1}{10}\int_0^t1250e^{-25\tau}\,d\tau+5', r'=-5\left(1-e^{-25t}\right)+5=5e^{-25t}\ \mathrm{A}')),
      S(r'**Split the voltage.** The $3.6\,\mathrm{H}$ takes $3.6\dfrac{di_o}{dt}$. The parallel pair gets the rest.',
        (r'3.6\cdot\frac{d}{dt}\left(5e^{-25t}\right)=-450e^{-25t}\ \mathrm{V}', r'v_{\text{pair}}=1250e^{-25t}-450e^{-25t}=800e^{-25t}\ \mathrm{V}')),
      S(r'**Each branch (c).** Same minus sign as before, own $L$, own start.',
        (r'i_1=-\frac18\int_0^t800e^{-25\tau}\,d\tau+10=6+4e^{-25t}\ \mathrm{A}', r'i_2=-\frac1{32}\int_0^t800e^{-25\tau}\,d\tau-5=-6+e^{-25t}\ \mathrm{A}')),
      S(r'**Initial energy (d).** Add $\tfrac12Li^2$ for all three.',
        r'\tfrac12(8)(10)^2+\tfrac12(32)(5)^2+\tfrac12(3.6)(5)^2=400+400+45=845\,\mathrm{J}'),
      S(r'**Delivered (e).** The box sees one $10\,\mathrm{H}$ inductor whose current goes from $5\,\mathrm{A}$ to $0$.',
        r'w_{\text{del}}=\tfrac12(10)(5)^2=125\,\mathrm{J}'),
      S(r'**Trapped (f)** and **check** with the final currents $i_1(\infty)=6$, $i_2(\infty)=-6$.',
        (r'845-125=720\,\mathrm{J}', r'\tfrac12(8)(6)^2+\tfrac12(32)(6)^2=144+576=720\,\mathrm{J}\ \checkmark'))],
     r'(a) $5\,\mathrm{A}$ (b) $5e^{-25t}\,\mathrm{A}$ (c) $i_1=6+4e^{-25t}$, $i_2=-6+e^{-25t}\,\mathrm{A}$ (d) $845\,\mathrm{J}$ (e) $125\,\mathrm{J}$ (f) $720\,\mathrm{J}$',
     cites=cite('T6', 2, 3, 4, 5))
D.TRY('Trapped energy, two inductors',
      r'A $6\,\mathrm{H}$ inductor with $i_1(0)=3\,\mathrm{A}$ and a $3\,\mathrm{H}$ inductor with $i_2(0)=-1\,\mathrm{A}$ (both arrows pointing the same way) are connected in parallel across a resistor at $t=0$. The total current dies out. Find the initial energy, the energy delivered to the resistor, and the trapped energy.',
      [S(r'**Start and combine.**', (r'i(0)=3+(-1)=2\,\mathrm{A}', r'L_{eq}=\frac{6\cdot3}{6+3}=2\,\mathrm{H}')),
       S(r'**Initial energy.**', r'\tfrac12(6)(3)^2+\tfrac12(3)(1)^2=27+1.5=28.5\,\mathrm{J}'),
       S(r'**Delivered.**', r'\tfrac12(2)(2)^2=4\,\mathrm{J}'),
       S(r'**Trapped.**', r'28.5-4=24.5\,\mathrm{J}')],
      r'$28.5\,\mathrm{J}$; $4\,\mathrm{J}$ delivered; $24.5\,\mathrm{J}$ trapped')

# ==================================================================================================== SUMMARY
D.H('Formula summary')
D.P(r'Everything from this note on one screen. Swap $v\leftrightarrow i$ and $L\leftrightarrow C$ to go from one column to the other.')
D.T(['', 'Inductor $L$', 'Capacitor $C$'],
    [['Rule', r'$v=L\dfrac{di}{dt}$', r'$i=C\dfrac{dv}{dt}$'],
     ['Integral', r'$i=\dfrac{1}{L}\displaystyle\int_{t_0}^{t} v\,d\tau+i(t_0)$', r'$v=\dfrac{1}{C}\displaystyle\int_{t_0}^{t} i\,d\tau+v(t_0)$'],
     ['Power', r'$p=vi$ ($>0$ storing, $<0$ delivering)', r'$p=vi$'],
     ['Energy', r'$w=\tfrac12Li^2$', r'$w=\tfrac12Cv^2$'],
     ['Max energy', r'at $\dfrac{di}{dt}=0$', r'at $\dfrac{dv}{dt}=0$'],
     ['At DC', 'wire (short)', 'gap (open)'],
     ['Cannot jump', r'$i_L(0^+)=i_L(0^-)$', r'$v_C(0^+)=v_C(0^-)$'],
     ['Series', r'$L_1+L_2$', r'$\dfrac{C_1C_2}{C_1+C_2}$, add starting $v$s'],
     ['Parallel', r'$\dfrac{L_1L_2}{L_1+L_2}$, add starting $i$s', r'$C_1+C_2$'],
     ['Trapped energy', r'$w_{\text{del}}=\tfrac12L_{eq}i(0)^2$, trapped $=$ initial $-$ delivered', '']])
D.P(r'Product rule you keep needing: $\dfrac{d}{dt}\left(te^{-at}\right)=e^{-at}(1-at)$. Practice: questions 1–4 in **Midterm 2 Practice Questions**.')

D.save()
