"""D1: first-order RC and RL circuits (Weeks 1-3)."""
import sympy as sp

from midlib import P, S, TAGS, link, t, zero

TB = 'http://127.0.0.1:8000'  # (schematics are checked by finish())


def fence(src):
    return '```schematic\n' + src.strip() + '\n```'


LECTURE_RL = r'''
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$10\,\Omega$" i="$i$"
L1 6,3 -> 6,0 "$2\,\mathrm{H}$" v="$v$"
wire 6,0 -> 0,0
ground 0,0
'''

T1 = r'''
I1 0,0 -> 0,3 "$I_s=4\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$R_0$"
S1 3,3 -> 6,3 "$t=0$" action=open
L1 6,3 -> 6,0 "$8\,\mathrm{mH}$" i="$i$"
wire 6,3 -> 9,3
R2 9,3 -> 9,0 "$4\,\Omega$" v="$v$"
wire 9,0 -> 0,0
ground 0,0
'''

T2 = r'''
I1 0,0 -> 0,3 "$I_s=2\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$1\,\mathrm{k\Omega}$" i="$v/R$"
S1 3,3 -> 6,3 "$t=0$" action=close
C1 6,3 -> 6,0 "$C$" v="$v$" i="$i_C$"
wire 6,0 -> 0,0
ground 0,0
'''

P742 = r'''
V1 0,3 -> 0,0 "$V_s$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$R$" i="$i$"
L1 6,3 -> 6,0 "$L$" v="$v$"
wire 6,0 -> 0,0
ground 0,0
'''

P722 = r'''
I1 0,0 -> 0,3 "$7.5\,\mathrm{mA}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$80\,\mathrm{k\Omega}$"
R2 3,3 -> 6,3 "$20\,\mathrm{k\Omega}$"
S1 6,3 -> 9,3 "$t=0$" action=open
C1 9,3 -> 9,0 "$0.4\,\mu\mathrm{F}$" v="$v(t)$"
wire 9,3 -> 12,3
R3 12,3 -> 12,0 "$50\,\mathrm{k\Omega}$"
wire 12,0 -> 0,0
ground 0,0
'''

P71 = r'''
V1 0,3 -> 0,0 "$120\,\mathrm{V}$"
R1 0,3 -> 3,3 "$3\,\Omega$"
R2 3,3 -> 3,0 "$30\,\Omega$"
R3 3,3 -> 6,3 "$6\,\Omega$"
S1 6,3 -> 9,3 "$t=0$" action=open
L1 9,0 -> 9,3 "$8\,\mathrm{mH}$" i="$i$"
wire 9,3 -> 12,3
R4 12,3 -> 12,0 "$2\,\Omega$"
wire 12,0 -> 0,0
ground 0,0
'''

P752 = r'''
V1 0,3 -> 0,0 "$120\,\mathrm{V}$"
R1 0,3 -> 2,3 "$10\,\mathrm{k\Omega}$"
S1 2,3 -> 4,3 "$t=0$" action=open
C1 4,3 -> 4,0 "$40\,\mathrm{nF}$" v="$v_C$" i="$i$"
S2 4,3 -> 6,3 "$t=0$" action=close
R2 6,3 -> 8,3 "$12.5\,\mathrm{k\Omega}$"
R3 8,3 -> 8,0 "$150\,\mathrm{k\Omega}$"
R4 8,3 -> 10,3 "$50\,\mathrm{k\Omega}$"
V2 10,0 -> 10,3 "$200\,\mathrm{V}$"
wire 10,0 -> 0,0
label 2,3 "$a$" above
label 6,3 "$b$" above
ground 0,0
'''


def build(D):
    D.H('D1 · First-order RC and RL circuits', level=2, cites=D.cite('W1', 6) + D.cite('W2', 4, 5) + D.cite('W3', 2, 3))
    TAGS(D, (1, 3), (2, 3), (3, 2))
    D.P(r'**When:** after the switch, the circuit has **one** capacitor or **one** inductor (after combining), plus resistors and DC sources. '
        'Then the ODE is first order, and it always has the same shape.')
    D.P(r'Call $x$ the quantity that can’t jump ($v_C$ or $i_L$). For $t>0$, KCL or KVL always gives:')
    D.EQ(r'\dfrac{dx}{dt}+\dfrac{x}{\tau}=\dfrac{x_f}{\tau}')
    D.L([r'$x$ = $v_C$ in an RC circuit, $i_L$ in an RL circuit',
         r'$\tau$ = the **time constant** (seconds): $\;\tau=R_{th}C\;$ or $\;\tau=\dfrac{L}{R_{th}}$',
         r'$x_f$ = the **final value** $x(\infty)$, from the DC steady state after the switch ($x_f=0$ if no source is left)',
         r'$R_{th}$ = the resistance the $C$ or $L$ “sees”: turn the sources off (voltage source → short, current source → open) '
         r'and combine the resistors between its two terminals, in the $t>0$ circuit'])
    D.P(r'This is a ' + link('B2', 'b2') + r' equation with constant $a=\frac1\tau$ and constant $f=\frac{x_f}{\tau}$. '
        r'Its shortcut solution, with the starting value $x(0)=x_0$, is the one formula you need:')
    D.EQ(r'x(t)=x_f+\big(x_0-x_f\big)\,e^{-t/\tau},\qquad t\ge0')
    D.P('**Method** (the D0 recipe, specialised):')
    D.L([r'**$x_0$:** from the $t<0$ DC circuit ($C$ open, $L$ short), carried over to $0^+$.',
         r'**$x_f$:** from the $t\to\infty$ DC circuit, with the switch in its **new** position.',
         r'**$\tau$:** find $R_{th}$ seen by the $C$ or $L$ in the $t>0$ circuit; $\tau=R_{th}C$ or $L/R_{th}$.',
         r'**Plug in:** $x(t)=x_f+(x_0-x_f)e^{-t/\tau}$.',
         r'**Anything else** from $x(t)$: Ohm’s law, KCL, $i_C=C\frac{dv_C}{dt}$, $v_L=L\frac{di_L}{dt}$.'],
        ordered=True)
    D.T(['', 'Natural response', 'Step response'], [
        ['When', r'no source is left after $t=0$: stored energy dies out', r'a DC source drives the circuit after $t=0$'],
        ['Final value', r'$x_f=0$', r'$x_f$ from the new DC steady state'],
        ['Answer', r'$x_0\,e^{-t/\tau}$', r'$x_f+(x_0-x_f)\,e^{-t/\tau}$'],
    ])
    D.P(r'**Reading the curve:** after $1\tau$, $e^{-1}=37\%$ of the starting gap $x_0-x_f$ is left (63% done); after $2\tau$, 13.5%; after $5\tau$, under 1% (“done”).')
    D.GRAPH(r'''
    title "Drag the sliders: the curve always heads for $x_f$, and the tangent at $t=0$ reaches $x_f$ at $t=\tau$"
    x 0 8 label="$t$"
    y -12 12 label="$x$"
    slider x0 -10 10 10 step=1 label="$x_0$"
    slider xf -10 10 2 step=1 label="$x_f$"
    slider tau 0.2 3 1 step=0.1 label="$\tau$"
    curve "xf+(x0-xf)*exp(-x/tau)" label="$x(t)=x_f+(x_0-x_f)e^{-t/\tau}$" color=1
    curve "x0+(xf-x0)*x/tau" from=0 to="tau" label="tangent at $t=0$" color=0 dash
    hline "xf" label="$x_f$" color=3
    point "tau" "xf+(x0-xf)*exp(-1)" label="at $t=\tau$: 37% of the gap left" color=2
    readout "$x(5\tau)$" "xf+(x0-xf)*exp(-5)"
    caption "Set $x_f=0$ for a natural response. A bigger $\tau$ (bigger $RC$ or $L/R$) means a slower circuit."
    ''')
    D.P('**Formulas you’ll also need:**')
    D.T(['Quantity', 'Formula', 'Note'], [
        [r'derivative of the exponential', r'$\dfrac{d}{dt}e^{-t/\tau}=-\dfrac1\tau e^{-t/\tau}$', r'for $i_C=C\frac{dv}{dt}$ and $v_L=L\frac{di}{dt}$'],
        ['energy stored', r'$w_C=\tfrac12Cv^2,\quad w_L=\tfrac12Li^2$', 'in joules'],
        ['parallel resistors', r'$R_1\parallel R_2=\dfrac{R_1R_2}{R_1+R_2}$', r'for $R_{th}$'],
    ])
    D.CO('info', r'**Bonus (skip-safe): where the formula comes from (the lecture’s RC step response).** A current source $I_s$, a resistor $R$ and a capacitor $C$ in parallel. '
         r'KCL at the top node: capacitor current plus resistor current equals the source current:'
         '\n\n$$\n' r'C\dfrac{dv}{dt}+\dfrac{v}{R}=I_s\quad\Rightarrow\quad\dfrac{dv}{dt}+\dfrac{v}{RC}=\dfrac{I_s}{C}' '\n$$\n\n'
         r'That is the standard form with $\tau=RC$ and $x_f=RI_s$, so $v=RI_s+(V_0-RI_s)e^{-t/RC}$. '
         r'It is ' + link('B2', 'b2') + r' with constant coefficients, and it also separates (' + link('B1', 'b1') + r'), as the lecture showed for the RL circuit.')

    D.EX('W3 · Circuit → ODE → answer · lecture §1.1',
         'The switch closes at $t=0$; the inductor carries no current before. Find $i(t)$ for $t\\ge0$.\n\n' + fence(LECTURE_RL),
         [S(r'**Type:** one inductor, one DC source → first-order RL step response. Solve for $i$ (the inductor current).'),
          S(r'**Before:** the switch is open, so no current: $i(0^-)=0$, and $i(0^+)=0$ (it can’t jump).'),
          S(r'**After:** KVL around the loop: the source equals the resistor voltage plus the inductor voltage.', r'2\dfrac{di}{dt}+10i=100'),
          S(r'Divide by $L=2$ to get the standard form: $\frac1\tau=5$, so $\tau=0.2\,\mathrm{s}$ (check: $L/R=2/10$).', r'\dfrac{di}{dt}+5i=50'),
          S(r'**Final value:** at $t\to\infty$ the inductor is a short, so $i_f=100/10=10\,\mathrm{A}$.'),
          S(r'**Plug in** $x_0=0$, $x_f=10$, $\tau=0.2$.', r'i(t)=10+(0-10)e^{-5t}')],
         r'$i(t)=10\big(1-e^{-5t}\big)\,\mathrm{A}$, the same answer the integrating factor gave (Problem in ' + link('B2', 'b2') + ').',
         cites=D.cite('W3', 2, 3))

    P(D, 'W1 · RL natural response · Pre-tutorial 1',
      r'The switch has been closed for a long time and opens at $t=0$. With $L=8\,\mathrm{mH}$, $R=4\,\Omega$ and $I_s=4\,\mathrm{A}$, '
      r'find the numerical expression for $i(t)$, $t\ge0$, and sketch it.' '\n\n' + fence(T1),
      [S(r'**Type:** after the switch opens, only the $L$–$R$ loop is left, with no source: RL **natural** response. Solve for $i$.'),
       S(r'**Before:** DC steady state, so $L$ is a short. It shorts $R_0$ and $R$, so all of $I_s$ flows down through $L$.', r'i(0^-)=4\,\mathrm{A}=i(0^+)'),
       S(r'**After:** $L$ discharges through $R$. No source, so $x_f=0$.', r'\tau=\dfrac{L}{R}=\dfrac{8\times10^{-3}}{4}=2\,\mathrm{ms}'),
       S(r'**Plug in:** $\frac1\tau=500\,\mathrm{s^{-1}}$.', r'i(t)=4e^{-500t}\,\mathrm{A}'),
       S(r'**Sketch:** starts at 4 A, is $4e^{-1}\approx1.47\,\mathrm{A}$ at $t=2\,\mathrm{ms}$, and is essentially 0 after $5\tau=10\,\mathrm{ms}$.')],
      r'$i(t)=4e^{-500t}\,\mathrm{A}$, $t\ge0$ ($\tau=2\,\mathrm{ms}$): an exponential decay from 4 A.', cites=D.cite('T1', 1))
    P(D, 'W2 · Can the capacitor current jump? · Pre-tutorial 2',
      r'The capacitor is uncharged ($V_0=0$). The switch closes at $t=0$, with $I_s=2\,\mathrm{A}$ and $R=1\,\mathrm{k\Omega}$. '
      r'Find the capacitor current at $t=0^-$ (switch open) and at $t=0^+$ (switch closed). Is there a discontinuity in the capacitor current, unlike the capacitor voltage?' '\n\n' + fence(T2),
      [S(r'**Type:** a $0^-$/$0^+$ question: use “$v_C$ can’t jump”, then KCL at $0^+$.'),
       S(r'**Before:** the switch is open, so the capacitor is disconnected.', r'i_C(0^-)=0'),
       S(r'**Just after:** $v(0^+)=v(0^-)=0$ (can’t jump). So the resistor current is $v/R=0$.'),
       S(r'KCL at the top node: all of the source current must go into the capacitor.', r'i_C(0^+)=I_s-\dfrac{v(0^+)}{R}=2-0=2\,\mathrm{A}'),
       S(r'**Afterwards:** $v$ rises towards $RI_s=2000\,\mathrm{V}$ and $i_C$ decays to 0.')],
      r'$i_C(0^-)=0$, $i_C(0^+)=2\,\mathrm{A}$: yes, the capacitor **current** jumps; the capacitor **voltage** stays continuous at 0.', cites=D.cite('T2', 1))
    P(D, 'W2–W3 · Read the circuit from its response · textbook P7.42',
      r'In this circuit the switch closes at $t=0$, and for $t\ge0$:' '\n\n'
      r'$i(t)=\big(10-10e^{-500t}\big)\,\mathrm{A},\qquad v(t)=200e^{-500t}\,\mathrm{V}\ (t\ge0^+)$' '\n\n'
      r'Find $V_s$, $R$, the initial current $I_0$ and $L$.' '\n\n' + fence(P742),
      [S(r'**Type:** RL step response read backwards: match $x_f+(x_0-x_f)e^{-t/\tau}$ term by term.'),
       S(r'**Starting value:** $I_0=i(0)=10-10=0$.'),
       S(r'**Just after:** $i=0$, so the resistor has no voltage and the whole source appears across $L$.', r'V_s=v(0^+)=200\,\mathrm{V}'),
       S(r'**Final value:** $L$ is a short, so $i_f=V_s/R$.', r'10=\dfrac{200}{R}\quad\Rightarrow\quad R=20\,\Omega'),
       S(r'**Time constant:** $\frac1\tau=500$, so $\tau=2\,\mathrm{ms}=L/R$.', r'L=20\times0.002=40\,\mathrm{mH}'),
       S(r'**Check:** $L\frac{di}{dt}=0.04\times5000e^{-500t}=200e^{-500t}$ ✓.')],
      r'$V_s=200\,\mathrm{V}$, $R=20\,\Omega$, $I_0=0$, $L=40\,\mathrm{mH}$.', diff='intermediate', cites=D.tb('7.42'))
    P(D, 'W2 · RC natural response with a divider first · textbook P7.22',
      r'The switch has been closed for a long time and opens at $t=0$. Find (a) $v(0)$, (b) $\tau$ for $t>0$, (c) $v(t)$, (d) the initial energy stored in the capacitor.' '\n\n' + fence(P722),
      [S(r'**Type:** after the switch opens, only $C$ and $50\,\mathrm{k\Omega}$ are left, no source: RC **natural** response. Solve for $v$.'),
       S(r'**Before:** $C$ is open, so the source current splits between $80\,\mathrm{k\Omega}$ and the $20+50=70\,\mathrm{k\Omega}$ path (current divider).',
         r'i_{70}=7.5\,\mathrm{mA}\cdot\dfrac{80}{80+70}=4\,\mathrm{mA}'),
       S(r'(a) $v$ is the voltage across $50\,\mathrm{k\Omega}$.', r'v(0^-)=4\,\mathrm{mA}\times50\,\mathrm{k\Omega}=200\,\mathrm{V}=v(0^+)'),
       S(r'(b) **After:** $C$ sees only $50\,\mathrm{k\Omega}$.', r'\tau=RC=50\times10^3\times0.4\times10^{-6}=20\,\mathrm{ms}'),
       S(r'(c) **Plug in** $x_f=0$, $\frac1\tau=50\,\mathrm{s^{-1}}$.', r'v(t)=200e^{-50t}\,\mathrm{V}'),
       S(r'(d) **Energy.**', r'w=\tfrac12Cv^2=\tfrac12(0.4\times10^{-6})(200)^2=8\,\mathrm{mJ}')],
      r'(a) $200\,\mathrm{V}$. (b) $20\,\mathrm{ms}$. (c) $v(t)=200e^{-50t}\,\mathrm{V}$, $t\ge0$. (d) $8\,\mathrm{mJ}$.', diff='intermediate', cites=D.tb('7.22'))
    P(D, 'W1–W2 · The sign of the reference arrow · textbook P7.1',
      r'The switch has been closed for a long time and opens at $t=0$. Note the direction of $i$ (**up** through the inductor). Find (a) the initial value of $i$, '
      r'(b) the initial energy stored in the inductor, (c) the time constant for $t>0$, (d) the numerical expression for $i(t)$, $t\ge0$.' '\n\n' + fence(P71),
      [S(r'**Type:** after the switch opens, only $L$ and $2\,\Omega$ are left, no source: RL **natural** response. Solve for $i$.'),
       S(r'**Before:** $L$ is a short, which also shorts the $2\,\Omega$. The source sees $3\,\Omega$ in series with $30\parallel6=5\,\Omega$.', r'I=\dfrac{120}{3+5}=15\,\mathrm{A}'),
       S(r'The middle node is at $120-15\times3=75\,\mathrm{V}$, so $75/6=12.5\,\mathrm{A}$ flows right through $6\,\Omega$ and then **down** through $L$.'),
       S(r'(a) The arrow points **up**, against the real current, so the value is negative.', r'i(0^-)=i(0^+)=-12.5\,\mathrm{A}'),
       S(r'(b) **Energy** (the sign doesn’t matter: $i$ is squared).', r'w=\tfrac12(8\times10^{-3})(12.5)^2=0.625\,\mathrm{J}'),
       S(r'(c) **After:** $L$ sees only $2\,\Omega$.', r'\tau=\dfrac{L}{R}=\dfrac{8\times10^{-3}}{2}=4\,\mathrm{ms}'),
       S(r'(d) **Plug in** $x_0=-12.5$, $x_f=0$, $\frac1\tau=250$.', r'i(t)=-12.5e^{-250t}\,\mathrm{A}')],
      r'(a) $-12.5\,\mathrm{A}$. (b) $0.625\,\mathrm{J}$. (c) $4\,\mathrm{ms}$. (d) $i(t)=-12.5e^{-250t}\,\mathrm{A}$, $t\ge0$.', diff='intermediate', cites=D.tb('7.1'))
    P(D, 'W2 · Step response that needs a Thévenin equivalent · textbook P7.52(a)',
      r'The switch has been in position $a$ for a long time. At $t=0$ it moves to position $b$ and stays there. '
      r'Find the initial and final values of the capacitor voltage, the time constant for $t\ge0$, and $v_C(t)$ for $t\ge0$. (The $200\,\mathrm{V}$ source has its $-$ on top. The two $t=0$ switches are one two-position switch: at $t=0$ the contact at $a$ opens and the contact at $b$ closes.)' '\n\n' + fence(P752),
      [S(r'**Type:** one capacitor, a DC source after the switch: RC **step** response. Solve for $v_C$.'),
       S(r'**Before (position $a$):** $C$ is open, so no current flows through $10\,\mathrm{k\Omega}$: the capacitor holds the full source.', r'v_C(0^-)=120\,\mathrm{V}=v_C(0^+)'),
       S(r'**After (position $b$):** replace everything right of $b$ by its Thévenin equivalent. With $C$ removed, no current flows in $12.5\,\mathrm{k\Omega}$; '
         r'the divider gives the node voltage (the source’s top is at $-200\,\mathrm{V}$).', r'V_{th}=-200\cdot\dfrac{150}{150+50}=-150\,\mathrm{V}'),
       S(r'Sources off (the $200\,\mathrm{V}$ source becomes a short): $12.5\,\mathrm{k\Omega}$ plus $150\parallel50$.', r'R_{th}=12.5+37.5=50\,\mathrm{k\Omega}'),
       S(r'**Final value and time constant:** $C$ ends at $V_{th}$.', r'v_f=-150\,\mathrm{V},\qquad\tau=(50\times10^{3})(40\times10^{-9})=2\,\mathrm{ms}'),
       S(r'**Plug in:** $x_0-x_f=120-(-150)=270$, $\frac1\tau=500$.', r'v_C(t)=-150+270e^{-500t}\,\mathrm{V}')],
      r'$v_C(0)=120\,\mathrm{V}$, $v_C(\infty)=-150\,\mathrm{V}$, $\tau=2\,\mathrm{ms}$, $v_C(t)=-150+270e^{-500t}\,\mathrm{V}$, $t\ge0$.',
      diff='advanced', cites=D.tb('7.52'))


def verify():
    i, v = sp.Function('i')(t), sp.Function('v')(t)
    # lecture RL: 2 i' + 10 i = 100, i(0) = 0
    sol = 10 - 10 * sp.exp(-5 * t)
    zero(2 * sp.diff(sol, t) + 10 * sol - 100)
    zero(sol.subs(t, 0))
    # Pre-tutorial 1: L i' + R i = 0 around the L-R loop, i(0) = 4
    sol = 4 * sp.exp(-500 * t)
    zero(sp.Rational(8, 1000) * sp.diff(sol, t) + 4 * sol)
    zero(sol.subs(t, 0) - 4)
    # Pre-tutorial 2: KCL C v' + v/R = Is, v(0+) = 0 -> i_C(0+) = Is
    C = sp.symbols('C', positive=True)
    vsol = 2000 * (1 - sp.exp(-t / (1000 * C)))
    zero(C * sp.diff(vsol, t) + vsol / 1000 - 2)
    zero((C * sp.diff(vsol, t)).subs(t, 0) - 2)
    # P7.42: series Vs-R-L
    isol = 10 - 10 * sp.exp(-500 * t)
    zero(sp.Rational(4, 100) * sp.diff(isol, t) - 200 * sp.exp(-500 * t))
    zero(sp.Rational(4, 100) * sp.diff(isol, t) + 20 * isol - 200)
    # P7.22: divider before, then natural through 50k
    i70 = sp.Rational(75, 10000) * 80 / (80 + 70)
    assert i70 * 50000 == 200
    vsol = 200 * sp.exp(-50 * t)
    zero(sp.Rational(4, 10 ** 7) * sp.diff(vsol, t) + vsol / 50000)
    assert sp.Rational(1, 2) * sp.Rational(4, 10 ** 7) * 200 ** 2 == sp.Rational(8, 1000)
    # P7.1: nodal before the switch (L short => right node at 0 V), then L i' + 2 i = 0 with i up
    va = sp.symbols('va')
    va = sp.solve((va - 120) / 3 + va / 30 + va / 6, va)[0]
    assert va == 75
    i0 = -(va / 6)
    assert i0 == sp.Rational(-25, 2)
    isol = i0 * sp.exp(-250 * t)
    zero(sp.Rational(8, 1000) * sp.diff(isol, t) + 2 * isol)
    assert sp.Rational(1, 2) * sp.Rational(8, 1000) * i0 ** 2 == sp.Rational(5, 8)
    # P7.52(a): eliminate the internal node and check the ODE for v_C
    vn = sp.symbols('vn')
    vc = -150 + 270 * sp.exp(-500 * t)
    node = sp.solve((vn - vc) / 12500 + vn / 150000 + (vn + 200) / 50000, vn)[0]
    zero(sp.Rational(4, 10 ** 8) * sp.diff(vc, t) + (vc - node) / 12500)
    zero(vc.subs(t, 0) - 120)
    assert sp.limit(vc, t, sp.oo) == -150
