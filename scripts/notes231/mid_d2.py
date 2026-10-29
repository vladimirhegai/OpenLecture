"""D2: series and parallel RLC circuits (Week 5)."""
import sympy as sp

from midlib import CARD, P, S, TAGS, link, second, t, zero


def sch(src):
    """A circuit drawn inside a problem or example prompt."""
    return '```schematic\n' + src.strip() + '\n```'


SERIES = r'''
V1 0,3 -> 0,0 "$V_s$"
R1 0,3 -> 3,3 "$R$" i="$i$"
L1 3,3 -> 6,3 "$L$"
C1 6,3 -> 6,0 "$C$" v="$v_C$"
wire 6,0 -> 0,0
ground 0,0
'''

PARALLEL = r'''
C1 0,3 -> 0,0 "$C$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$L$" i="$i_L$"
wire 3,3 -> 6,3
R1 6,3 -> 6,0 "$R$" i="$i_R$"
wire 6,0 -> 0,0
ground 0,0
'''

P853 = r'''
V1 0,3 -> 0,0 "$200\to100\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$" i="$i$"
L1 3,3 -> 6,3 "$40\,\mathrm{mH}$"
C1 6,3 -> 6,0 "$10\,\mathrm{mF}$" v="$v_C$"
wire 6,0 -> 0,0
ground 0,0
'''

P814 = r'''
C1 0,3 -> 0,0 "$250\,\mathrm{mF}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$0.4\,\mathrm{H}$" i="$i_L$"
wire 3,0 -> 0,0
ground 0,0
'''

P83 = r'''
C1 0,3 -> 0,0 "$50\,\mathrm{nF}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$L$" i="$i_L$"
wire 3,3 -> 6,3
R1 6,3 -> 6,0 "$R$" i="$i_R$"
wire 6,0 -> 0,0
ground 0,0
'''

P844 = r'''
V1 0,3 -> 0,0 "$70\,\mathrm{V}$"
R1 0,3 -> 3,3 "$50\,\Omega$"
S1 3,3 -> 6,3 "$t=0$" action=open
C1 6,3 -> 6,0 "$200\,\mathrm{nF}$" v="$v_C$"
S2 6,3 -> 9,3 "$t=0$" action=close
R2 9,3 -> 12,3 "$200\,\Omega$" i="$i$"
L1 12,3 -> 12,0 "$100\,\mathrm{mH}$"
wire 12,0 -> 0,0
ground 0,0
label 3,3 "$a$" above
label 9,3 "$b$" above
'''

P87 = r'''
C1 0,3 -> 0,0 "$10\,\mathrm{nF}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$250\,\mathrm{mH}$" i="$i_L$"
wire 3,3 -> 6,3
R1 6,3 -> 6,0 "$\tfrac{12500}{3}\,\Omega$" i="$i_R$"
wire 6,0 -> 0,0
ground 0,0
'''

P842 = r'''
C1 0,3 -> 0,0 "$160\,\mathrm{nF}$" v="$v_C$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$R$" i="$i$"
L1 6,3 -> 6,0 "$250\,\mathrm{mH}$"
wire 6,0 -> 0,0
ground 0,0
'''

P824 = r'''
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 3,3 "$400\,\Omega$"
L1 3,3 -> 3,0 "$1.25\,\mathrm{H}$" i="$i_L$"
S1 3,3 -> 6,3 "$t=0$" action=close
C1 6,3 -> 6,0 "$1.25\,\mu\mathrm{F}$" v="$v_o$"
wire 6,0 -> 0,0
ground 0,0
'''


def build(D):
    D.H('D2 · An L and a C: RLC circuits (second order)', level=2, cites=D.tb('8.53'))
    TAGS(D, (5, 3))
    D.P(r'**Use this when**, after the switch, there’s an inductor **and** a capacitor (combine series/parallel ones first, so you have one of each).')
    D.P(r'**The move: it’s ' + link('B5', 'b5') + r' with circuit names.** Same quadratic, same three cases. Write the quadratic as:')
    D.EQ(r's^2+2\alpha s+\omega_0^2=0')
    D.L([r'$\alpha$ (“alpha”) = the **damping**: how fast it dies out',
         r'$\omega_0$ (“omega-zero”) = the **natural frequency**: how fast it would swing with no $R$',
         r'Both come straight from $R$, $L$, $C$ (below), so you never have to derive the ODE on the exam.'])
    D.P(r'A source still on after the switch? Then add the final value $V_f$ on top, like $y_p$ in ' + link('B6', 'b6') + ':')
    D.EQ(r'v(t)=V_f+(\text{the B5 form})')

    D.H('Series or parallel: α and ω₀', level=3)
    D.SCH(SERIES.strip(), 'Series RLC: one loop. The same current $i$ flows through every element.')
    D.P(r'**Series** (solve for $v_C$):')
    D.EQ(r'\alpha=\dfrac{R}{2L},\qquad \omega_0=\dfrac{1}{\sqrt{LC}}')
    D.P(r'**Short example:** $R=4\,\Omega$, $L=1\,\mathrm{H}$, $C=0.25\,\mathrm{F}$:')
    D.EQ(r'\alpha=\dfrac{4}{2}=2,\qquad \omega_0=\dfrac{1}{\sqrt{0.25}}=2')
    D.SCH(PARALLEL.strip(), 'Parallel RLC: two nodes. The same voltage $v$ sits across every element. All three current arrows point down.')
    D.P(r'**Parallel** (solve for the shared $v$). Only $\alpha$ changes:')
    D.EQ(r'\alpha=\dfrac{1}{2RC},\qquad \omega_0=\dfrac{1}{\sqrt{LC}}')
    D.P(r'**Short example:** $R=800\,\Omega$, $C=50\,\mathrm{nF}$:')
    D.EQ(r'\alpha=\dfrac{1}{2(800)(50\times10^{-9})}=12500\,\mathrm{s^{-1}}')
    D.WHY('Where do the equations come from?',
          r'**Series:** KVL around the loop, $V_s=Ri+Li\prime+v_C$, with $i=Cv_C\prime$. Divide by $LC$:'
          '\n\n$$\n' r'v_C\prime\prime+\dfrac RL\,v_C\prime+\dfrac1{LC}\,v_C=\dfrac{V_s}{LC}' '\n$$\n\n'
          r'Match with $s^2+2\alpha s+\omega_0^2$: $2\alpha=\frac RL$ and $\omega_0^2=\frac1{LC}$.'
          '\n\n'
          r'**Parallel:** KCL at the top node, $Cv\prime+i_L+\frac vR=0$. Differentiate once, use $i_L\prime=\frac vL$, divide by $C$:'
          '\n\n$$\n' r'v\prime\prime+\dfrac{1}{RC}\,v\prime+\dfrac{1}{LC}\,v=0' '\n$$\n\n'
          r'So $2\alpha=\frac{1}{RC}$. A big parallel $R$ takes almost no current, so it barely drains energy: less damping.')

    D.H('The three cases (same as B5)', level=3)
    D.P(r'Compare $\alpha$ with $\omega_0$. The roots are:')
    D.EQ(r's=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}')
    D.T(['Compare', 'Name', 'B5 case', 'Form'], [
        [r'$\alpha>\omega_0$', '**overdamped**', 'Case 1', r'$c_1e^{s_1t}+c_2e^{s_2t}$'],
        [r'$\alpha=\omega_0$', '**critically damped**', 'Case 2', r'$(c_1+c_2t)e^{-\alpha t}$'],
        [r'$\alpha<\omega_0$', '**underdamped**', 'Case 3', r'$e^{-\alpha t}(c_1\cos\omega_dt+c_2\sin\omega_dt)$'],
    ])
    D.P(r'Underdamped swings at $\omega_d$ (the B5 $\omega$; and $\sigma=-\alpha$):')
    D.EQ(r'\omega_d=\sqrt{\omega_0^2-\alpha^2}')
    D.P(r'**Short examples:**')
    D.EQ(r'\alpha=5,\ \omega_0=3\quad\Longrightarrow\quad s=-5\pm4=-1,\,-9\quad\text{(overdamped)}')
    D.EQ(r'\alpha=50,\ \omega_0=50\quad\Longrightarrow\quad (c_1+c_2t)e^{-50t}\quad\text{(critical)}')
    D.EQ(r'\alpha=3,\ \omega_0=5\quad\Longrightarrow\quad \omega_d=4,\ \ e^{-3t}(c_1\cos4t+c_2\sin4t)')
    D.P(r'No $R$ at all ($\alpha=0$, an ideal LC): $\;c_1\cos\omega_0t+c_2\sin\omega_0t$, swinging forever.')
    D.GRAPH(r'''
    title "Slide R through the three cases (series RLC, $L=1\,\mathrm{H}$, $C=0.25\,\mathrm{F}$)"
    x 0 6 label="$t$ (s)"
    y -8 11 label="$v_C$ (V)"
    slider R 0 10 1 step=0.1 label="$R$ ($\Omega$)" animate
    let a "R/2"
    let wd "sqrt(abs(4-a^2))"
    let s1 "-a+wd"
    let s2 "-a-wd"
    curve "if(abs(a-2)<0.001, 10*(1+2*t)*exp(-2*t), if(a<2, 10*exp(-a*t)*(cos(wd*t)+a/wd*sin(wd*t)), 10*(s2*exp(s1*t)-s1*exp(s2*t))/(s2-s1)))" label="$v_C(t)$, from $10\,\mathrm{V}$ with $i=0$" color=1
    hline "0"
    readout "$\alpha=R/2L$" "a"
    readout "$\omega_0=1/\sqrt{LC}$" "2"
    caption "$\omega_0=2$ never changes; only $\alpha=R/2$ moves. $R<4$: underdamped, it swings below zero before settling. $R=4$: critically damped, fastest with no overshoot. $R>4$: overdamped, a slow creep back."
    ''', intro='**What do the three cases look like?**')

    D.H('Steps: the two starting values', level=3)
    D.P(r'Second order needs **two** starting values: $v(0)$ and the slope $v\prime(0)$. The value carries across. The slope comes from the capacitor current:')
    D.EQ(r'v_C\prime(0^+)=\dfrac{i_C(0^+)}{C}')
    D.L([r'**Before:** old circuit, long time ($C$ = gap, $L$ = wire). Find $v_C(0^-)$ and $i_L(0^-)$.',
         r'**Carry across:** $v_C(0^+)=v_C(0^-)$, $i_L(0^+)=i_L(0^-)$. Then find $i_C(0^+)$ and the slope (cards below).',
         r'**After:** series or parallel? Compute $\alpha$, $\omega_0$. Final value $V_f$: $0$ if no source is left, else the new DC state.',
         r'**Pick** the case (compare $\alpha$, $\omega_0$) and write $v=V_f+$ the form.',
         r'**Plug in** $t=0$: the value gives $c_1$, the slope (product rule) gives $c_2$. Use the **whole** answer, $V_f$ included.',
         r'**Check:** $t\to\infty$ gives $V_f$.'], ordered=True)
    CARD(D, r'Slope in a series circuit: $\;i_C=$ the loop current $=i_L$',
         [(r'The loop current is the inductor current, so it carries across. Sign: $+$ if the arrow enters the $+$ end of $C$.', r'v_C\prime(0^+)=\dfrac{i_L(0^+)}{C}'),
          (r'Example: $i(0^-)=0$.', r'v_C\prime(0^+)=0')])
    CARD(D, r'Slope in a parallel circuit: KCL, $\;i_C=-(i_L+i_R)$',
         [(r'All three arrows point down, so the currents add to $0$. $i_R=\frac{v(0^+)}{R}$.', r'i_C(0^+)=-\big(i_L(0^+)+i_R(0^+)\big)'),
          (r'Example: $v=10\,\mathrm{V}$, $R=5\,\Omega$, $i_L=1\,\mathrm{A}$, $C=0.5\,\mathrm{F}$.', (r'i_C=-(1+2)=-3\,\mathrm{A}', r'v\prime(0^+)=\dfrac{-3}{0.5}=-6\,\mathrm{V/s}'))])
    CARD(D, r'Solving for $i$ in a series circuit: $\;i\prime(0^+)=\dfrac{v_L(0^+)}{L}$',
         [(r'$i(0^+)=i_L(0^-)$. For the slope, KVL around the new loop gives $v_L$.', r'v_L(0^+)=v_C(0^+)-R\,i(0^+)'),
          (r'Example: $v_C=70\,\mathrm{V}$, $i=0$, $L=0.1\,\mathrm{H}$.', r'i\prime(0^+)=\dfrac{70}{0.1}=700\,\mathrm{A/s}')])
    D.CO('warning', r'**Fit the constants to the whole answer, $V_f$ included.** $v_C=100+(c_1+c_2t)e^{-50t}$ with $v_C(0)=200$: $\;100+c_1=200$, so $c_1=100$, not $200$.')
    D.CO('warning', r'**Units first.** $1\,\mathrm{mH}=10^{-3}\,\mathrm{H}$, $1\,\mu\mathrm{F}=10^{-6}\,\mathrm{F}$, $1\,\mathrm{nF}=10^{-9}\,\mathrm{F}$. '
         r'Example: $L=250\,\mathrm{mH}$, $C=10\,\mathrm{nF}$ → $\omega_0=\dfrac{1}{\sqrt{0.25\times10^{-8}}}=20000$.')

    D.P(r'**Textbook example (P8.53).** The circuit has been running for a long time with $V_s=200\,\mathrm{V}$. At $t=0$ the source drops to $100\,\mathrm{V}$. Find $v_C(t)$ for $t\ge0$.'
        '\n\n' + sch(P853), cites=D.tb('8.53'))
    CARD(D, r'Full solution: a series step response',
         [(r'**Before:** long time, so $C$ is a gap and $i=0$. With no current, $R$ and $L$ drop nothing, so $C$ holds the whole $200\,\mathrm{V}$.', r'v_C(0^-)=200\,\mathrm{V},\qquad i(0^-)=0'),
          (r'**Carry across:** neither can jump. The slope is $i/C$, and $i=0$.', (r'v_C(0^+)=200', r'v_C\prime(0^+)=\dfrac{0}{0.01}=0')),
          (r'**After:** series, so $\alpha=\frac{R}{2L}$. Long after, $C$ is a gap again and holds the new source.', (r'\alpha=\dfrac{4}{2(0.04)}=50,\qquad \omega_0=\dfrac{1}{\sqrt{0.04\times0.01}}=50', r'V_f=100\,\mathrm{V}')),
          (r'**Pick:** $\alpha=\omega_0$, critically damped (B5 Case 2). Add $V_f$.', r'v_C=100+(c_1+c_2t)\,e^{-50t}'),
          (r'Differentiate (product rule).', r'v_C\prime=c_2e^{-50t}-50(c_1+c_2t)e^{-50t}'),
          (r'**Plug in** $t=0$.', (r'100+c_1=200\quad\Rightarrow\quad c_1=100', r'c_2-50c_1=0\quad\Rightarrow\quad c_2=5000')),
          (r'**Check:** $t\to\infty$ gives $100\,\mathrm{V}$ ✓.', '')],
         r'v_C=100+(100+5000t)\,e^{-50t}\,\mathrm{V}')

    D.H('Practice: D2', level=3)
    P(D, 'W5 · No resistor: an ideal LC circuit · textbook P8.14',
      r'A $250\,\mathrm{mF}$ capacitor and a $0.4\,\mathrm{H}$ inductor are in parallel. At the start, $v(0)=0$ and $i_L(0)=-3\,\mathrm{A}$ (arrow pointing down). '
      r'Find (a) $v(t)$, (b) its frequency in rad/s, (c) its maximum amplitude.' '\n\n' + sch(P814),
      [S(r'**Type:** parallel with no $R$, so $\alpha=0$: undamped. $\frac{1}{LC}=\frac{1}{0.25\times0.4}=10$.', r"v''+\dfrac{1}{LC}v=v''+10v=0"),
       S(r'**Pick:** $\omega_0=\sqrt{10}$. The cosine coefficient is $v(0)=0$, so only the sine is left.', r'v=c_2\sin(\sqrt{10}\,t)'),
       S(r'**Carry across** (slope): KCL at the top node: $i_C+i_L=0$, so $i_C(0^+)=+3\,\mathrm{A}$ (down). Divide by $C$.', r"v'(0^+)=\dfrac{3}{0.25}=12\,\mathrm{V/s}"),
       S(r'**Plug in:** the slope of $c_2\sin(\sqrt{10}\,t)$ at $0$ is $\sqrt{10}\,c_2$. Set it equal to 12.', r'c_2=\dfrac{12}{\sqrt{10}}\approx3.795')],
      r'(a) $v=\dfrac{12}{\sqrt{10}}\sin(\sqrt{10}\,t)\,\mathrm{V}$. (b) $\omega_0=\sqrt{10}\approx3.162\,\mathrm{rad/s}$. (c) $3.795\,\mathrm{V}$. With no $R$, nothing uses up the energy, so it never dies out.',
      cites=D.tb('8.14'))
    P(D, 'W5 · Read the circuit back from its response · textbook P8.3',
      r'In a parallel RLC circuit, $C=50\,\mathrm{nF}$ and the voltage is $v=-5e^{-5000t}+20e^{-20000t}\,\mathrm{V}$ for $t\ge0$. '
      r'Find $\alpha$, $\omega_0$, $L$ and $R$.' '\n\n' + sch(P83),
      [S(r'**Type:** two decaying exponentials means two real roots: overdamped. The exponents are the roots, $s_1=-5000$ and $s_2=-20000$.'),
       S(r'**Roots → equation:** multiply out $(s+5000)(s+20000)$ and line it up with $s^2+2\alpha s+\omega_0^2$.', r's^2+25000s+10^8=0'),
       S(r'Read off: $2\alpha=25000$ and $\omega_0^2=10^8$.', r'\alpha=12500\,\mathrm{s^{-1}},\quad\omega_0=10^4\,\mathrm{rad/s}'),
       S(r'**$L$:** use $\omega_0^2=\dfrac{1}{LC}$.', r'L=\dfrac{1}{10^8\times50\times10^{-9}}=0.2\,\mathrm{H}'),
       S(r'**$R$:** it is parallel, so use $\alpha=\dfrac{1}{2RC}$.', r'R=\dfrac{1}{2(12500)(50\times10^{-9})}=800\,\Omega')],
      r'$\alpha=12500\,\mathrm{s^{-1}}$, $\omega_0=10^4\,\mathrm{rad/s}$, $L=0.2\,\mathrm{H}$, $R=800\,\Omega$.',
      cites=D.tb('8.3'))
    P(D, 'W5 · Switch to a series loop · textbook P8.44',
      r'The switch has been at $a$ for a long time. At $t=0$ it moves to $b$. Find $i(t)$ for $t\ge0$.' '\n\n' + sch(P844),
      [S(r'**Type:** after the switch, $C$, the $200\,\Omega$ and $L$ form one loop with no source: a series RLC natural response. We solve for $i$, the inductor current.'),
       S(r'**Before:** at $a$, $C$ is open (steady state), so no current flows in the $50\,\Omega$ and $C$ charges to the full 70 V. $L$ isn’t connected, so its current is 0.', r'v_C(0^-)=70\,\mathrm{V},\quad i(0^-)=0'),
       S(r'**Carry across** (slope): KVL around the new loop is $v_C=Ri+L\,i\prime$. At $0^+$, $v_C=70$ and $i=0$.', r"i'(0^+)=\dfrac{70-200(0)}{0.1}=700\,\mathrm{A/s}"),
       S(r'**After:** $\alpha=\dfrac{R}{2L}=\dfrac{200}{2(0.1)}=1000$ and $\omega_0^2=\dfrac{1}{LC}=\dfrac{1}{0.1\times200\times10^{-9}}=5\times10^7$. $\alpha^2=10^6$ is smaller, so underdamped.', r'\omega_d=\sqrt{5\times10^7-10^6}=7000\,\mathrm{rad/s}'),
       S(r'**Pick:** the cosine coefficient is $i(0)=0$, so only the sine is left.', r'i=c_2\,e^{-1000t}\sin7000t'),
       S(r'**Plug in:** the slope of this at $t=0$ is $7000c_2$. Set it equal to 700.', r'c_2=0.1')],
      r'$i=0.1\,e^{-1000t}\sin7000t\ \mathrm{A}$ $=100\,e^{-1000t}\sin7000t\ \mathrm{mA}$, $t\ge0$.',
      diff='intermediate', cites=D.tb('8.44'))
    P(D, 'W5 · The slope comes from KCL · textbook P8.7',
      r'$R=\tfrac{12500}{3}\,\Omega$, $L=250\,\mathrm{mH}$ and $C=10\,\mathrm{nF}$ are in parallel. At the start, $v(0)=90\,\mathrm{V}$ and $i_L(0)=-30\,\mathrm{mA}$ (arrows as drawn). Find $v(t)$ for $t\ge0$.'
      '\n\n' + sch(P87),
      [S(r'**Type:** parallel RLC, no source: a natural response.'),
       S(r'**Carry across** (slope): first the resistor current, $i_R=\dfrac{90}{12500/3}=21.6\,\mathrm{mA}$. KCL at the top node (all arrows down): $i_C+i_L+i_R=0$, so $i_C=-(-30)-21.6$.', r'i_C(0^+)=30-21.6=8.4\,\mathrm{mA}'),
       S(r'Divide by $C$ to get the slope.', r"v'(0^+)=\dfrac{8.4\times10^{-3}}{10^{-8}}=8.4\times10^5\,\mathrm{V/s}"),
       S(r'**After:** $\alpha=\dfrac{1}{2RC}=12000$ and $\omega_0=\dfrac{1}{\sqrt{LC}}=20000$. $\alpha<\omega_0$, so underdamped.', r'\omega_d=\sqrt{20000^2-12000^2}=16000'),
       S(r'**Pick:** the cosine coefficient is $v(0)=90$.', r'v=e^{-12000t}(90\cos16000t+c_2\sin16000t)'),
       S(r'**Plug in:** the slope at $0$ is $-\alpha(90)+\omega_dc_2$ (the $y\prime(0)$ column of the B5 table). Set it equal to $8.4\times10^5$.', r'-12000(90)+16000c_2=840000\ \Rightarrow\ c_2=120')],
      r'$v=e^{-12000t}(90\cos16000t+120\sin16000t)\,\mathrm{V}$, $t\ge0$.',
      diff='intermediate', cites=D.tb('8.7'))
    P(D, 'W5 · Choose R for critical damping · textbook P8.42',
      r'$R$ is set so the circuit is critically damped. When the switch closes, $v_C=90\,\mathrm{V}$ and the inductor current is $i=24\,\mathrm{mA}$. '
      r'Find (a) $R$, (b) $i$ and $\dfrac{di}{dt}$ just after closing, (c) $i(t)$ and $v_C(t)$ for $t\ge0$.' '\n\n' + sch(P842),
      [S(r'**Type:** one loop, no source: a series RLC natural response. Critically damped means $\alpha=\omega_0$.'),
       S(r'**(a)** $\omega_0=\dfrac{1}{\sqrt{0.25\times160\times10^{-9}}}=5000$. Set $\alpha=\dfrac{R}{2L}=5000$ and solve for $R$.', r'R=2(0.25)(5000)=2500\,\Omega'),
       S(r'**(b)** $i$ is the inductor current, so it can’t jump: $i(0^+)=24\,\mathrm{mA}$. For the slope, use KVL around the loop, $v_C=Ri+L\,i\prime$, at $0^+$.', r"i'(0^+)=\dfrac{90-2500(0.024)}{0.25}=120\,\mathrm{A/s}"),
       S(r'**(c) Pick:** critically damped, so one repeated root $s=-\alpha=-5000$.', r'i=(c_1+c_2t)e^{-5000t}'),
       S(r'**Plug in:** $c_1=i(0)=0.024$. The slope at $0$ is $c_2-5000c_1$; set it equal to 120.', r'c_2=240'),
       S(r'For $v_C$, use the same KVL: $v_C=Ri+L\,i\prime$. (Check: $i=-C\,v_C\prime$, with a minus because $i$ leaves the $+$ of $C$.)', r'v_C=(90+3\times10^5\,t)e^{-5000t}')],
      r'(a) $R=2500\,\Omega$. (b) $i(0^+)=24\,\mathrm{mA}$, $i\prime(0^+)=120\,\mathrm{A/s}$. (c) $i=(0.024+240t)e^{-5000t}\,\mathrm{A}$, $v_C=(90+3\times10^5t)e^{-5000t}\,\mathrm{V}$.',
      diff='advanced', cites=D.tb('8.42'))
    P(D, 'W5 + W6 · The answer is zero · textbook P8.24',
      r'The switch has been open for a long time and the capacitor is uncharged. At $t=0$ the switch closes. Find $v_o(t)$ for $t\ge0$.' '\n\n' + sch(P824),
      [S(r'**Type:** after closing, $L$ and $C$ sit across the same two nodes, fed by the source through $400\,\Omega$: a parallel RLC with a DC source.'),
       S(r'**Before:** steady state, so $L$ is a short and takes the whole source current. $C$ isn’t connected and has no charge.', r'i_L(0^-)=\dfrac{12}{400}=30\,\mathrm{mA},\quad v_o(0^-)=0'),
       S(r'**Carry across** (slope): at $0^+$, $v_o=0$, so the $400\,\Omega$ still carries $30\,\mathrm{mA}$. $L$ still takes all 30 mA (it can’t jump). KCL at the top node leaves nothing for $C$.', r'i_C(0^+)=30-30=0\ \Rightarrow\ v_o\prime(0^+)=0'),
       S(r'**After:** KCL at the top node is $\dfrac{v_o-12}{400}+i_L+Cv_o\prime=0$. Differentiate once: the constant 12 disappears, so the right side is $0$.', r"Cv_o''+\dfrac{v_o'}{400}+\dfrac{v_o}{L}=0"),
       S(r'**Plug in:** right side $0$, $v_o(0)=0$ and $v_o\prime(0)=0$. The only solution that fits is $v_o=0$ (the zero-start rule in ' + link('Topic C', 'topic-c') + ').')],
      r'$v_o(t)=0$ for all $t\ge0$. The inductor already carries the whole source current, so nothing ever flows into the capacitor.',
      diff='advanced', cites=D.tb('8.24'))


def verify():
    E = sp.exp
    # graph formulas (series natural, L=1, C=1/4, v(0)=10, v'(0)=0): y'' + R y' + 4 y = 0
    for R in (1, 4, 6):
        a = sp.Rational(R, 2)
        if R < 4:
            wd = sp.sqrt(4 - a ** 2)
            v = 10 * E(-a * t) * (sp.cos(wd * t) + a / wd * sp.sin(wd * t))
        elif R == 4:
            v = 10 * (1 + 2 * t) * E(-2 * t)
        else:
            wd = sp.sqrt(a ** 2 - 4)
            s1, s2 = -a + wd, -a - wd
            v = 10 * (s2 * E(s1 * t) - s1 * E(s2 * t)) / (s2 - s1)
        second(v, 1, R, 4, initial=(0, 10, 0))
    # P8.53
    vs = 100 + (100 + 5000 * t) * E(-50 * t)
    L, C, R = sp.Rational(4, 100), sp.Rational(1, 100), 4
    assert R / (2 * L) == 50 and 1 / sp.sqrt(L * C) == 50
    second(vs, 1, R / L, 1 / (L * C), 100 / (L * C), initial=(0, 200, 0))
    # P8.14
    vlc = 12 / sp.sqrt(10) * sp.sin(sp.sqrt(10) * t)
    second(vlc, 1, 0, 1 / (sp.Rational(1, 4) * sp.Rational(2, 5)), initial=(0, 0, 12))
    zero(sp.Rational(1, 4) * sp.diff(vlc, t).subs(t, 0) - 3)
    # P8.3
    C = sp.Rational(5, 10 ** 8)
    v3 = -5 * E(-5000 * t) + 20 * E(-20000 * t)
    R, L = 800, sp.Rational(1, 5)
    second(v3, 1, 1 / (R * C), 1 / (L * C))
    assert 1 / (2 * R * C) == 12500 and 1 / (L * C) == 10 ** 8
    # P8.44: loop C-R-L, vC = R i + L i', i = -C vC'
    R, L, C = 200, sp.Rational(1, 10), sp.Rational(2, 10 ** 7)
    i = sp.Rational(1, 10) * E(-1000 * t) * sp.sin(7000 * t)
    vC = R * i + L * sp.diff(i, t)
    zero(-C * sp.diff(vC, t) - i)
    zero(vC.subs(t, 0) - 70)
    zero(i.subs(t, 0))
    # P8.7
    C, L, R = sp.Rational(1, 10 ** 8), sp.Rational(1, 4), sp.Rational(12500, 3)
    vp = E(-12000 * t) * (90 * sp.cos(16000 * t) + 120 * sp.sin(16000 * t))
    slope = -(sp.Rational(-30, 1000) + 90 / R) / C
    assert slope == 840000
    second(vp, 1, 1 / (R * C), 1 / (L * C), initial=(0, 90, slope))
    il = -C * sp.diff(vp, t) - vp / R
    zero(il.subs(t, 0) + sp.Rational(30, 1000))
    zero(L * sp.diff(il, t) - vp)
    # P8.42
    C, L = sp.Rational(16, 10 ** 8), sp.Rational(1, 4)
    w0 = 1 / sp.sqrt(L * C)
    assert w0 == 5000
    R = 2 * L * w0
    assert R == 2500
    i = (sp.Rational(24, 1000) + 240 * t) * E(-5000 * t)
    second(i, 1, R / L, 1 / (L * C), initial=(0, sp.Rational(24, 1000), 120))
    vC = R * i + L * sp.diff(i, t)
    zero(vC - (90 + 300000 * t) * E(-5000 * t))
    zero(-C * sp.diff(vC, t) - i)
    # P8.24: steady state values and zero slope
    assert sp.Rational(12, 400) == sp.Rational(3, 100)
    second(sp.Integer(0) * t, sp.Rational(5, 4 * 10 ** 6), sp.Rational(1, 400), sp.Rational(4, 5), initial=(0, 0, 0))
