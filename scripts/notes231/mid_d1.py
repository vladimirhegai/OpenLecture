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
    D.WHY('Where does the formula come from?',
          r'KVL or KCL after the switch always gives this ' + link('B2', 'b2') + r' equation, with $p=\frac1\tau$ and $f=\frac{x_f}{\tau}$:'
          '\n\n$$\n' r'\dfrac{dx}{dt}+\dfrac{x}{\tau}=\dfrac{x_f}{\tau}' '\n$$\n\n'
          r'Solve it once with $x(0)=x_0$ and you get the formula. Check: at $t=0$, $e^0=1$, so $x=x_0$ ✓. As $t\to\infty$, $e^{-t/\tau}\to0$, so $x\to x_f$ ✓.'
          '\n\n'
          r'Example (the lecture’s RC step response): $I_s$, $R$, $C$ in parallel. KCL: $C\frac{dv}{dt}+\frac vR=I_s$, so $\tau=RC$ and $x_f=RI_s$.'
          '\n\n'
          r'Why the sources go off for $R_{th}$: they only set $x_f$ (the right side). The speed $\tau$ comes from the left side: just the resistors and the $C$ or $L$.')

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
    D.P(r'**Lecture example (§1.1).** The switch closes at $t=0$. The inductor carries no current before that. Find $i(t)$ for $t\ge0$.'
        '\n\n' + fence(LECTURE_RL), cites=D.cite('W3', 2, 3))
    CARD(D, r'Full solution: the lecture’s RL step response',
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
    D.GRAPH(r'''
    title "Drag the sliders: the curve always heads for $x_f$"
    x 0 8 label="$t$"
    y -12 12 label="$x$"
    slider x0 -10 10 10 step=1 label="$x_0$"
    slider xf -10 10 2 step=1 label="$x_f$"
    slider tau 0.2 3 1 step=0.1 label="$\tau$"
    curve "xf+(x0-xf)*exp(-x/tau)" label="$x(t)=x_f+(x_0-x_f)e^{-t/\tau}$" color=1
    hline "xf" label="$x_f$" color=3
    point "tau" "xf+(x0-xf)*exp(-1)" label="at $t=\tau$: 37% of the gap left" color=2
    caption "Set $x_f=0$ for a natural response. A bigger $\tau$ (bigger $RC$ or $L/R$) means a slower circuit."
    ''', intro='**What does the formula look like?**')

    D.H('Practice: D1', level=3)
    P(D, 'W1 · RL natural response · Pre-tutorial 1',
      r'The switch has been closed for a long time and opens at $t=0$. Use $L=8\,\mathrm{mH}$, $R=4\,\Omega$ and $I_s=4\,\mathrm{A}$. '
      r'Find $i(t)$ for $t\ge0$ (with numbers) and sketch it.' '\n\n' + fence(T1),
      [S(r'**Type:** once the switch opens, only $L$ and the $4\,\Omega$ are left in a loop, with no source. That’s an RL **natural** response. Solve for $i$.'),
       S(r'**Before:** a long time, so $L$ is a wire. That wire shorts out $R_0$ and the $4\,\Omega$, so all of $I_s$ goes down through $L$.', r'i(0^-)=4\,\mathrm{A}=i(0^+)'),
       S(r'**After:** $L$ dumps its energy into the $4\,\Omega$. No source, so $x_f=0$.', r'\tau=\dfrac{L}{R}=\dfrac{8\times10^{-3}}{4}=2\,\mathrm{ms}'),
       S(r'**Plug in:** $\frac1\tau=500\,\mathrm{s^{-1}}$.', r'i(t)=4e^{-500t}\,\mathrm{A}'),
       S(r'**Sketch:** it starts at 4 A, drops to $4e^{-1}\approx1.47\,\mathrm{A}$ at $t=\tau=2\,\mathrm{ms}$, and is basically 0 after $5\tau=10\,\mathrm{ms}$.')],
      r'$i(t)=4e^{-500t}\,\mathrm{A}$, $t\ge0$ ($\tau=2\,\mathrm{ms}$): an exponential decay from 4 A.', cites=D.cite('T1', 1))
    P(D, 'W2 · Can the capacitor current jump? · Pre-tutorial 2',
      r'The capacitor starts uncharged ($V_0=0$). The switch closes at $t=0$. Use $I_s=2\,\mathrm{A}$ and $R=1\,\mathrm{k\Omega}$. '
      r'Find the capacitor current just before ($t=0^-$, switch open) and just after ($t=0^+$, switch closed). Does the capacitor current jump, even though the capacitor voltage can’t?' '\n\n' + fence(T2),
      [S(r'**Type:** a just-before / just-after question. Use “$v_C$ can’t jump”, then KCL at $0^+$.'),
       S(r'**Before:** the switch is open, so the capacitor isn’t connected to anything.', r'i_C(0^-)=0'),
       S(r'**Carry across:** $v(0^+)=v(0^-)=0$, since it can’t jump. The resistor sits across the capacitor, so its current is $v/R=0$.'),
       S(r'**KCL** at the top node: the resistor takes nothing, so all of the source current goes into the capacitor.', r'i_C(0^+)=I_s-\dfrac{v(0^+)}{R}=2-0=2\,\mathrm{A}'),
       S(r'**Check:** $v$ rises toward $RI_s=2000\,\mathrm{V}$ and $i_C$ dies down to 0.')],
      r'$i_C(0^-)=0$, $i_C(0^+)=2\,\mathrm{A}$. So yes, the capacitor **current** jumps. The capacitor **voltage** doesn’t: it stays at 0.', cites=D.cite('T2', 1))
    P(D, 'W2–W3 · Read the circuit from its response · textbook P7.42',
      r'The switch closes at $t=0$. For $t\ge0$ you measure:' '\n\n'
      r'$i(t)=\big(10-10e^{-500t}\big)\,\mathrm{A},\qquad v(t)=200e^{-500t}\,\mathrm{V}\ (t\ge0^+)$' '\n\n'
      r'Find $V_s$, $R$, the starting current $I_0$ and $L$.' '\n\n' + fence(P742),
      [S(r'**Type:** RL step response, read backwards. Match each piece to $x_f+(x_0-x_f)e^{-t/\tau}$.'),
       S(r'**Carry across:** put $t=0$ into $i(t)$: $I_0=10-10=0$.'),
       S(r'**Carry across:** $i=0$, so the resistor has 0 V across it. The whole source voltage sits on $L$.', r'V_s=v(0^+)=200\,\mathrm{V}'),
       S(r'**After** (final value): long after, $L$ is a wire, so $i_f=V_s/R$. From $i(t)$, $i_f=10$.', r'10=\dfrac{200}{R}\quad\Rightarrow\quad R=20\,\Omega'),
       S(r'**After** (time constant): the exponent is $-500t$, so $\frac1\tau=500$ and $\tau=2\,\mathrm{ms}$. Use $\tau=L/R$.', r'L=20\times0.002=40\,\mathrm{mH}'),
       S(r'**Check:** $L\frac{di}{dt}=0.04\times5000e^{-500t}=200e^{-500t}$, which matches $v(t)$ ✓.')],
      r'$V_s=200\,\mathrm{V}$, $R=20\,\Omega$, $I_0=0$, $L=40\,\mathrm{mH}$.', diff='intermediate', cites=D.tb('7.42'))
    P(D, 'W2 · RC natural response with a divider first · textbook P7.22',
      r'The switch has been closed for a long time and opens at $t=0$. Find (a) $v(0)$, (b) $\tau$ for $t>0$, (c) $v(t)$, (d) the energy stored in the capacitor at $t=0$.' '\n\n' + fence(P722),
      [S(r'**Type:** once the switch opens, only $C$ and the $50\,\mathrm{k\Omega}$ are left, with no source. RC **natural** response. Solve for $v$.'),
       S(r'**Before:** $C$ is a gap, so the source current has two paths: the $80\,\mathrm{k\Omega}$, or $20+50=70\,\mathrm{k\Omega}$. Current divider:',
         r'i_{70}=7.5\,\mathrm{mA}\cdot\dfrac{80}{80+70}=4\,\mathrm{mA}'),
       S(r'(a) $v$ is the voltage across the $50\,\mathrm{k\Omega}$ (it sits on the same two nodes as $C$).', r'v(0^-)=4\,\mathrm{mA}\times50\,\mathrm{k\Omega}=200\,\mathrm{V}=v(0^+)'),
       S(r'(b) **After:** $C$ only sees the $50\,\mathrm{k\Omega}$.', r'\tau=RC=50\times10^3\times0.4\times10^{-6}=20\,\mathrm{ms}'),
       S(r'(c) **Plug in** $x_f=0$, $\frac1\tau=50\,\mathrm{s^{-1}}$.', r'v(t)=200e^{-50t}\,\mathrm{V}'),
       S(r'(d) **Energy:** use $w=\frac12Cv^2$ with $v(0)=200\,\mathrm{V}$.', r'w=\tfrac12Cv^2=\tfrac12(0.4\times10^{-6})(200)^2=8\,\mathrm{mJ}')],
      r'(a) $200\,\mathrm{V}$. (b) $20\,\mathrm{ms}$. (c) $v(t)=200e^{-50t}\,\mathrm{V}$, $t\ge0$. (d) $8\,\mathrm{mJ}$.', diff='intermediate', cites=D.tb('7.22'))
    P(D, 'W1–W2 · The sign of the reference arrow · textbook P7.1',
      r'The switch has been closed for a long time and opens at $t=0$. Watch the direction of $i$: it points **up** through the inductor. Find (a) the starting value of $i$, '
      r'(b) the energy stored in the inductor at $t=0$, (c) the time constant for $t>0$, (d) $i(t)$ for $t\ge0$, with numbers.' '\n\n' + fence(P71),
      [S(r'**Type:** once the switch opens, only $L$ and the $2\,\Omega$ are left, with no source. RL **natural** response. Solve for $i$.'),
       S(r'**Before:** $L$ is a wire, and it shorts out the $2\,\Omega$. So the source sees $3\,\Omega$ in series with $30\parallel6=5\,\Omega$.', r'I=\dfrac{120}{3+5}=15\,\mathrm{A}'),
       S(r'The middle node sits at $120-15\times3=75\,\mathrm{V}$. So $75/6=12.5\,\mathrm{A}$ goes right through the $6\,\Omega$, then **down** through $L$.'),
       S(r'(a) The arrow points **up**, but the real current goes down, so the value is negative.', r'i(0^-)=i(0^+)=-12.5\,\mathrm{A}'),
       S(r'(b) **Energy:** the sign doesn’t matter, because $i$ gets squared.', r'w=\tfrac12(8\times10^{-3})(12.5)^2=0.625\,\mathrm{J}'),
       S(r'(c) **After:** $L$ only sees the $2\,\Omega$.', r'\tau=\dfrac{L}{R}=\dfrac{8\times10^{-3}}{2}=4\,\mathrm{ms}'),
       S(r'(d) **Plug in** $x_0=-12.5$, $x_f=0$, $\frac1\tau=250$.', r'i(t)=-12.5e^{-250t}\,\mathrm{A}')],
      r'(a) $-12.5\,\mathrm{A}$. (b) $0.625\,\mathrm{J}$. (c) $4\,\mathrm{ms}$. (d) $i(t)=-12.5e^{-250t}\,\mathrm{A}$, $t\ge0$.', diff='intermediate', cites=D.tb('7.1'))
    P(D, 'W2 · Step response that needs a Thévenin equivalent · textbook P7.52(a)',
      r'The switch has been at $a$ for a long time. At $t=0$ it moves to $b$ and stays there. '
      r'Find the starting and final capacitor voltage, the time constant for $t\ge0$, and $v_C(t)$ for $t\ge0$. (The $200\,\mathrm{V}$ source has its $-$ on top. The two $t=0$ switches are one two-position switch: at $t=0$ the contact at $a$ opens and the contact at $b$ closes.)' '\n\n' + fence(P752),
      [S(r'**Type:** one capacitor, and a DC source still connected after the switch. RC **step** response. Solve for $v_C$.'),
       S(r'**Before (at $a$):** $C$ is a gap, so no current flows through the $10\,\mathrm{k\Omega}$ and it drops 0 V. The capacitor gets the full source.', r'v_C(0^-)=120\,\mathrm{V}=v_C(0^+)'),
       S(r'**After (at $b$):** shrink everything right of $b$ into one source $V_{th}$ plus one resistor $R_{th}$ (Thévenin). Then it’s a plain RC loop.'),
       S(r'**$V_{th}$:** take $C$ out. No current flows in the $12.5\,\mathrm{k\Omega}$, so $V_{th}$ is the voltage on the $150\,\mathrm{k\Omega}$: a divider with the $50\,\mathrm{k\Omega}$. '
         r'The source’s top is at $-200\,\mathrm{V}$.', r'V_{th}=-200\cdot\dfrac{150}{150+50}=-150\,\mathrm{V}'),
       S(r'**$R_{th}$:** turn the source off (it becomes a wire). That leaves $12.5\,\mathrm{k\Omega}$ in series with $150\parallel50=37.5\,\mathrm{k\Omega}$.', r'R_{th}=12.5+37.5=50\,\mathrm{k\Omega}'),
       S(r'**Final value and time constant:** in the end $C$ is a gap again, so no current flows and $C$ sits at $V_{th}$.', r'v_f=-150\,\mathrm{V},\qquad\tau=(50\times10^{3})(40\times10^{-9})=2\,\mathrm{ms}'),
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
