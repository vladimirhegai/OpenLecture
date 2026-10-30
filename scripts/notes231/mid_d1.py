"""D1: first-order RC and RL circuits (Weeks 1-3)."""
import sympy as sp

from midlib import CARD, P, S, TAGS, link, t, zero

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

LECTURE_RC = r'''
V1 0,3 -> 0,0 "$V_s$"
R1 0,3 -> 3,3 "$R_1$"
S1 3,3 -> 6,3 "$t=0$" action=open
C1 6,3 -> 6,0 "$C$" v="$v$"
S2 6,3 -> 9,3 "$t=0$" action=close
R2 9,3 -> 9,0 "$R$"
wire 9,0 -> 0,0
label 3,3 "$a$" above
label 9,3 "$b$" above
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

def build(D):
    D.H('D1 · One C or one L: first order', level=2, cites=D.cite('W1', 6) + D.cite('W2', 4, 5) + D.cite('W3', 2, 3))
    TAGS(D, (1, 3), (2, 3), (3, 2))
    D.P(r'**Use this when**, after the switch, only **one** capacitor or **one** inductor is left (after combining), plus resistors and DC sources.')
    D.P(r'Call $x$ the thing that can’t jump: $v_C$ in an RC circuit, $i_L$ in an RL circuit.')
    D.P(r'**The move: you don’t need to solve the ODE.** Find three numbers and plug them in:')
    D.EQ(r'x(t)=x_f+\big(x_0-x_f\big)\,e^{-t/\tau}')
    D.L([r'$x_0$ = the **starting value** (from the old circuit)',
         r'$x_f$ = the **final value**, long after the switch (from the new circuit). $0$ if no source is left.',
         r'$\tau$ = the **time constant** in seconds: $\;\tau=R_{th}C\;$ or $\;\tau=\dfrac{L}{R_{th}}$'])
    D.P(r'$R_{th}$ = the resistance the $C$ or $L$ “sees” in the new circuit: turn the sources off (a voltage source → a wire, a current source → a gap), then combine the resistors.')
    D.P('**Short example:**')
    D.EQ(r'x_0=0,\quad x_f=10,\quad \tau=0.2\quad\Longrightarrow\quad x(t)=10-10e^{-5t}')
    D.P('**Steps**')
    D.L([r'**Before:** old circuit, long time ($C$ = gap, $L$ = wire). Find $x(0^-)$.',
         r'**Carry across:** $x_0=x(0^+)=x(0^-)$.',
         r'**After:** new circuit. Final value $x_f$ (long time again). Time constant: $R_{th}$, then $\tau=R_{th}C$ or $L/R_{th}$.',
         r'**Plug in:** $x(t)=x_f+(x_0-x_f)e^{-t/\tau}$.',
         r'**Check:** $x(0)=x_0$ and $x(\infty)=x_f$. Anything else comes from $x(t)$: $i_C=C\frac{dv_C}{dt}$, $v_L=L\frac{di_L}{dt}$, Ohm’s law.'], ordered=True)

    D.H('Case 1: natural response (no source left)', level=3)
    D.P(r'The stored energy drains away through the resistors, so $x_f=0$:')
    D.EQ(r'x(t)=x_0\,e^{-t/\tau}')
    D.P(r'**Short example:** $i_L$ starts at $4\,\mathrm{A}$, $L=8\,\mathrm{mH}$, $R=4\,\Omega$:')
    D.EQ(r'\tau=\dfrac{8\times10^{-3}}{4}=2\,\mathrm{ms}\quad\Longrightarrow\quad i(t)=4e^{-500t}\,\mathrm{A}')

    D.H('Case 2: step response (a source stays on)', level=3)
    D.P(r'The source pushes $x$ to a new value $x_f$:')
    D.EQ(r'x(t)=x_f+\big(x_0-x_f\big)\,e^{-t/\tau}')
    D.P(r'**Short example:** $i$ starts at $0$, ends at $10\,\mathrm{A}$, $\tau=0.2\,\mathrm{s}$:')
    D.EQ(r'i(t)=10+(0-10)e^{-5t}=10\big(1-e^{-5t}\big)\,\mathrm{A}')

    D.H('Examples and handy facts', level=3)
    D.P(r'**★ Lecture example (Week 3 §1.1).** The switch closes at $t=0$. The inductor carries no current before that. Find $i(t)$ for $t\ge0$.'
        '\n\n' + fence(LECTURE_RL), cites=D.cite('W3', 2, 3))
    CARD(D, r'★ Lecture §1.1, the 100 V RL circuit (try it, then open)',
         [(r'**Before:** the switch is open, so no current flows.', r'i(0^-)=0'),
          (r'**Carry across:** an inductor current can’t jump.', r'x_0=i(0^+)=0'),
          (r'**After** (final value): long after, $L$ is a wire, so only the $10\,\Omega$ limits the current.', r'x_f=\dfrac{100}{10}=10\,\mathrm{A}'),
          (r'**After** (time constant): the source is off, so $L$ sees just the $10\,\Omega$.', r'\tau=\dfrac{L}{R}=\dfrac{2}{10}=0.2\,\mathrm{s}'),
          (r'**Plug in.**', r'i(t)=10+(0-10)e^{-t/0.2}=10-10e^{-5t}'),
          (r'**Check** with the ODE (KVL: $100=10i+2\frac{di}{dt}$). Divide by $2$: it’s $i\prime+5i=50$, the ' + link('B2', 'b2') + ' practice problem. Same answer.',
           r'\dfrac{di}{dt}+5i=50')],
         r'i(t)=10\big(1-e^{-5t}\big)\,\mathrm{A}')
    D.P('**Handy facts.** Open a card for an example:')
    CARD(D, r'How fast it settles: after $1\tau$ 37% of the gap is left, after $5\tau$ it’s done',
         [(r'$e^{-1}\approx0.37$, $e^{-2}\approx0.135$, $e^{-5}<0.01$.', r'x(\tau)=x_f+0.37\,(x_0-x_f)'),
          (r'Example: $\tau=2\,\mathrm{ms}$.', r'5\tau=10\,\mathrm{ms}\quad\text{(settled)}')])
    CARD(D, r'Derivative: $\;\dfrac{d}{dt}e^{-t/\tau}=-\dfrac1\tau\,e^{-t/\tau}$',
         [(r'For $i_C=C\frac{dv}{dt}$ or $v_L=L\frac{di}{dt}$. Example: $i=10-10e^{-5t}$, $L=2\,\mathrm{H}$:', r'v_L=2\cdot50e^{-5t}=100e^{-5t}\,\mathrm{V}')])
    CARD(D, r'Energy stored: $\;w_C=\tfrac12Cv^2$, $\;w_L=\tfrac12Li^2$',
         [(r'In joules. The sign of $i$ doesn’t matter (it’s squared). Example: $L=8\,\mathrm{mH}$, $i=12.5\,\mathrm{A}$:', r'w=\tfrac12(8\times10^{-3})(12.5)^2=0.625\,\mathrm{J}')])
    CARD(D, r'Parallel resistors: $\;R_1\parallel R_2=\dfrac{R_1R_2}{R_1+R_2}$',
         [(r'For $R_{th}$. Example:', r'6\parallel3=\dfrac{18}{9}=2\,\Omega')])
    D.H('Practice: D1', level=3)
    P(D, '★ W1 · RL natural response · Pre-tutorial 1',
      r'The switch has been closed for a long time and opens at $t=0$. Use $L=8\,\mathrm{mH}$, $R=4\,\Omega$ and $I_s=4\,\mathrm{A}$. '
      r'Find $i(t)$ for $t\ge0$ (with numbers) and sketch it.' '\n\n' + fence(T1),
      [S(r'**Type:** once the switch opens, only $L$ and the $4\,\Omega$ are left in a loop, with no source. That’s an RL **natural** response. Solve for $i$.'),
       S(r'**Before:** a long time, so $L$ is a wire. That wire shorts out $R_0$ and the $4\,\Omega$, so all of $I_s$ goes down through $L$.', r'i(0^-)=4\,\mathrm{A}=i(0^+)'),
       S(r'**After:** $L$ dumps its energy into the $4\,\Omega$. No source, so $x_f=0$.', r'\tau=\dfrac{L}{R}=\dfrac{8\times10^{-3}}{4}=2\,\mathrm{ms}'),
       S(r'**Plug in:** $\frac1\tau=500\,\mathrm{s^{-1}}$.', r'i(t)=4e^{-500t}\,\mathrm{A}'),
       S(r'**Sketch:** it starts at 4 A, drops to $4e^{-1}\approx1.47\,\mathrm{A}$ at $t=\tau=2\,\mathrm{ms}$, and is basically 0 after $5\tau=10\,\mathrm{ms}$.')],
      r'$i(t)=4e^{-500t}\,\mathrm{A}$, $t\ge0$ ($\tau=2\,\mathrm{ms}$): an exponential decay from 4 A.', cites=D.cite('T1', 1))
    P(D, '★ W2 · Can the capacitor current jump? · Pre-tutorial 2',
      r'The capacitor starts uncharged ($V_0=0$). The switch closes at $t=0$. Use $I_s=2\,\mathrm{A}$ and $R=1\,\mathrm{k\Omega}$. '
      r'Find the capacitor current just before ($t=0^-$, switch open) and just after ($t=0^+$, switch closed). Does the capacitor current jump, even though the capacitor voltage can’t?' '\n\n' + fence(T2),
      [S(r'**Type:** a just-before / just-after question. Use “$v_C$ can’t jump”, then KCL at $0^+$.'),
       S(r'**Before:** the switch is open, so the capacitor isn’t connected to anything.', r'i_C(0^-)=0'),
       S(r'**Carry across:** $v(0^+)=v(0^-)=0$, since it can’t jump. The resistor sits across the capacitor, so its current is $v/R=0$.'),
       S(r'**KCL** at the top node: the resistor takes nothing, so all of the source current goes into the capacitor.', r'i_C(0^+)=I_s-\dfrac{v(0^+)}{R}=2-0=2\,\mathrm{A}'),
       S(r'**Check:** $v$ rises toward $RI_s=2000\,\mathrm{V}$ and $i_C$ dies down to 0.')],
      r'$i_C(0^-)=0$, $i_C(0^+)=2\,\mathrm{A}$. So yes, the capacitor **current** jumps. The capacitor **voltage** doesn’t: it stays at 0.', cites=D.cite('T2', 1))
    P(D, '★ W2 · RC natural and step response · lecture §4 and §5',
      r'(a) **Natural response** (lecture §4). The switch has been at $a$ for a long time, so $C$ is charged by $V_s$ through $R_1$. '
      r'At $t=0$ it moves to $b$, leaving $C$ alone with $R$. Find $v(t)$, $t\ge0$.' '\n\n' + fence(LECTURE_RC) + '\n\n'
      r'(b) **Step response** (lecture §5, the Pre-tutorial 2 circuit above). $I_s$, $R$ and $C$ end up in parallel, $v(0)=V_0$. Find $v(t)$, $t\ge0$.' '\n\n'
      r'(c) In (a), take $V_s=10\,\mathrm{V}$, $R=1\,\mathrm{k\Omega}$, $C=1\,\mu\mathrm{F}$. Find $\tau$ and $v(\tau)$.',
      [S(r'**Type:** one $C$ → first order → D1. (a) has no source after the switch: natural. (b) keeps $I_s$: step.'),
       S(r'(a) **Before:** long time, $C$ is a gap, so no current flows through $R_1$ and $C$ sits at the source voltage.', r'v(0^-)=V_s=v(0^+)'),
       S(r'(a) **After:** only $C$ and $R$ in a loop, no source, so $x_f=0$. $C$ sees just $R$.', r'\tau=RC'),
       S(r'(a) **Plug in.**', r'v(t)=V_s\,e^{-t/RC}'),
       S(r'(b) **After:** long time, $C$ is a gap, so all of $I_s$ goes through $R$.', (r'V_f=RI_s', r'\tau=RC')),
       S(r'(b) **Plug in** with $x_0=V_0$.', r'v(t)=RI_s+(V_0-RI_s)\,e^{-t/RC}'),
       S(r'(b) **Check** with KCL at the top node: $C\frac{dv}{dt}+\frac vR=I_s$ is the ' + link('B2', 'b2') + r' shape, and $t\to\infty$ gives $RI_s$ ✓.'),
       S(r'(c) **Numbers:** $\tau=RC=10^3\times10^{-6}$. After one $\tau$, $e^{-1}\approx0.368$ of the start is left.', (r'\tau=1\,\mathrm{ms}', r'v(\tau)=10e^{-1}\approx3.68\,\mathrm{V}'))],
      r'(a) $v=V_se^{-t/RC}$. (b) $v=RI_s+(V_0-RI_s)e^{-t/RC}$. (c) $\tau=1\,\mathrm{ms}$, $v(\tau)\approx3.68\,\mathrm{V}$ (37% of $V_s$).',
      cites=D.cite('W2', 3, 4, 5))


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
    # lecture RC: natural v = Vs e^{-t/RC}, step C v' + v/R = Is
    Vs, R, C0, Is, V0 = sp.symbols('V_s R C I_s V_0', positive=True)
    nat = Vs * sp.exp(-t / (R * C0))
    zero(C0 * sp.diff(nat, t) + nat / R)
    step = R * Is + (V0 - R * Is) * sp.exp(-t / (R * C0))
    zero(C0 * sp.diff(step, t) + step / R - Is)
    zero(step.subs(t, 0) - V0)
    assert abs(float(10 * sp.exp(-1)) - 3.68) < 0.01
