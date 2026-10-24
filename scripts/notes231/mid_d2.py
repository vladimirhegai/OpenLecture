"""D2: series and parallel RLC circuits (Week 5)."""
import sympy as sp

from midlib import P, S, TAGS, link, second, t, zero


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
    D.H('D2 · RLC circuits (second order)', level=2, cites=D.tb('8.53'))
    TAGS(D, (5, 3))
    D.P(r'**When the circuit has one inductor and one capacitor** (after combining), its equation is **second order**. '
        r'The math is ' + link('B5', 'b5') + ' (and ' + link('B6', 'b6') + ' when a source stays on). '
        'The new part is getting the equation and the two starting values from the circuit.')
    D.P(r'Before anything, find the starting values with the switching recipe in ' + link('Topic D', 'topic-d') +
        r': $v_C(0^+)$ and $i_L(0^+)$ carry over from just before the switch.')

    D.P('**The two circuits you will meet:**')
    D.SCH(SERIES.strip(), 'Series RLC: one loop, one current $i$ through all four elements.')
    D.SCH(PARALLEL.strip(), 'Parallel RLC: two nodes, one voltage $v$ across all three elements; all currents point down.')
    D.T(['', 'Series', 'Parallel'], [
        ['Unknown', r'$v_C$ (or the loop current $i$)', r'the common voltage $v$'],
        ['Equation', r'$v_C\prime\prime+\dfrac{R}{L}v_C\prime+\dfrac{1}{LC}v_C=\dfrac{V_s}{LC}$', r'$v\prime\prime+\dfrac{1}{RC}v\prime+\dfrac{1}{LC}v=0$'],
        [r'Damping $\alpha$', r'$\dfrac{R}{2L}$', r'$\dfrac{1}{2RC}$'],
        [r'Natural frequency $\omega_0$', r'$\dfrac{1}{\sqrt{LC}}$', r'$\dfrac{1}{\sqrt{LC}}$ (the same)'],
        ['Starting value', r'$v_C(0^+)=v_C(0^-)$', r'$v(0^+)=v_C(0^-)$'],
        ['Starting slope', r'$v_C\prime(0^+)=\dfrac{i(0^+)}{C}$, with $i=i_L$ entering the $+$ of $C$',
         r'$v\prime(0^+)=\dfrac{i_C(0^+)}{C}$, with $i_C(0^+)$ from KCL'],
    ])
    D.P('Both equations have the shape below, so the characteristic equation and its roots are:')
    D.EQ(r's^2+2\alpha s+\omega_0^2=0')
    D.EQ(r's=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}')

    D.P(r'**Compare $\alpha$ with $\omega_0$ to know the shape before solving.** These are the three root cases of ' + link('B5', 'b5') + ' with circuit names:')
    D.T(['Compare', 'Roots', 'Name', 'Form of the response'], [
        [r'$\alpha>\omega_0$', 'two real', '**overdamped**', r'$A_1e^{s_1t}+A_2e^{s_2t}$'],
        [r'$\alpha=\omega_0$', 'one repeated', '**critically damped**', r'$(A_1+A_2t)e^{-\alpha t}$'],
        [r'$\alpha<\omega_0$', r'$-\alpha\pm j\omega_d$', '**underdamped**', r'$e^{-\alpha t}(B_1\cos\omega_dt+B_2\sin\omega_dt)$'],
        [r'$\alpha=0$ (no $R$)', r'$\pm j\omega_0$', '**undamped** (LC)', r'$B_1\cos\omega_0t+B_2\sin\omega_0t$'],
    ])
    D.P(r'Here $\omega_d=\sqrt{\omega_0^2-\alpha^2}$ is the **damped frequency**: how fast an underdamped response oscillates.')
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
    caption "$\omega_0=2$ is fixed. $R<4$: $\alpha<\omega_0$, underdamped (it swings below zero). $R=4$: critically damped, the fastest return without overshoot. $R>4$: overdamped, a slow creep back. $R=0$: undamped, it never dies out."
    ''')
    D.P(r'**With a source that stays on** (a step response), the answer is a **final value** plus a part that dies out. '
        r'The final value comes from the DC steady state ($C$ open, $L$ short): it is the constant $y_p$ of ' + link('B6', 'b6') + '. '
        r'Fit the constants to $v_C=V_f+(\text{transient})$, not to the transient alone.')
    D.P('**Method:**')
    D.L([r'**Before:** DC steady state for $t<0$ gives $v_C(0^-)$ and $i_L(0^-)$.',
         r'**Starting values:** $v_C(0^+)=v_C(0^-)$, $i_L(0^+)=i_L(0^-)$, then the starting slope (table above).',
         r'**Equation:** series or parallel? Compute $\alpha$ and $\omega_0$; compare them to pick the form.',
         r'**Final value:** $0$ with no source; otherwise the DC steady state after the switch.',
         r'**Constants:** use the starting value and slope on the full expression (product rule for the slope).'],
        ordered=True)
    D.CO('warning', r'**Units.** Convert $\mathrm{mH}$, $\mathrm{mF}$, $\mu\mathrm{F}$, $\mathrm{nF}$ to H and F before computing $\alpha$ and $\omega_0$. '
         r'$1\,\mathrm{nF}=10^{-9}\,\mathrm{F}$, $1\,\mu\mathrm{F}=10^{-6}\,\mathrm{F}$, $1\,\mathrm{mH}=10^{-3}\,\mathrm{H}$.')
    D.CO('info', r'**Bonus (skip-safe): where the series equation comes from.** KVL around the loop, then replace the current by $Cv_C\prime$:' '\n\n'
         '```steps\n'
         r'$$ V_s=Ri+Li\prime+v_C $$' '\n'
         'KVL: the three element voltages add up to the source.\n'
         r'$$ i=\hl{Cv_C\prime} $$' '\n'
         'The loop current is the capacitor current.\n'
         r'$$ V_s=RC\,v_C\prime+LC\,v_C\prime\prime+v_C $$' '\n'
         'Substitute the current and its derivative.\n'
         r'$$ v_C\prime\prime+\hl{\dfrac RL}v_C\prime+\hl{\dfrac1{LC}}v_C=\hl{\dfrac{V_s}{LC}} $$' '\n'
         r'Divide by $LC$.' '\n'
         '```\n\n'
         r'For the parallel circuit, KCL at the top node is $Cv\prime+i_L+\dfrac vR=0$. Differentiate once and use $i_L\prime=\dfrac vL$.')

    D.EX('W5 · A series step response · textbook P8.53',
         r'The circuit has been in operation for a long time with $V_s=200\,\mathrm{V}$. At $t=0$ the source drops to $100\,\mathrm{V}$. Find $v_C(t)$ for $t\ge0$.'
         '\n\n' + sch(P853),
         [S(r'**Type:** one $L$, one $C$ in one loop with a source that stays on: series RLC step response.'),
          S(r'**Before:** DC steady state, $C$ open so $i=0$. No drop on $R$ or $L$, so $C$ holds the old source voltage.', r'v_C(0^-)=200\,\mathrm{V},\quad i(0^-)=0'),
          S(r'**Starting values:** both carry over. The slope is $i/C$.', r"v_C(0^+)=200,\quad v_C'(0^+)=\dfrac{0}{0.01}=0"),
          S(r'**Equation:** $\alpha=\frac{4}{2(0.04)}=50$, $\omega_0=\frac{1}{\sqrt{0.04\times0.01}}=50$. Equal: critically damped.', r"v_C''+100v_C'+2500v_C=250000"),
          S(r'**Final value:** new DC steady state, $C$ open again, so $v_C\to100\,\mathrm{V}$. Write final value + repeated-root transient.', r'v_C=100+(A_1+A_2t)e^{-50t}'),
          S(r'**Constants:** the value gives $A_1$.', r'100+A_1=200\ \Rightarrow\ A_1=100'),
          S(r'The slope (product rule) gives $A_2$.', r'A_2-50A_1=0\ \Rightarrow\ A_2=5000')],
         r'$v_C=100+(100+5000t)e^{-50t}\,\mathrm{V}$, $t\ge0$ ($t$ in seconds). It starts at 200 V, flat, and settles at 100 V without overshoot.',
         cites=D.tb('8.53'))

    P(D, 'W5 · No resistor: an ideal LC circuit · textbook P8.14',
      r'$C=250\,\mathrm{mF}$ and $L=0.4\,\mathrm{H}$ are in parallel. Initially $v(0)=0$ and $i_L(0)=-3\,\mathrm{A}$ (reference downward). '
      r'Find (a) $v(t)$, (b) its frequency in rad/s, (c) its maximum amplitude.' '\n\n' + sch(P814),
      [S(r'**Type:** parallel, no $R$: $\alpha=0$, undamped.', r"v''+\dfrac{1}{LC}v=v''+10v=0"),
       S(r'**Form:** $\omega_0=\sqrt{10}$; the cosine term is zero because $v(0)=0$.', r'v=B\sin(\sqrt{10}\,t)'),
       S(r'**Starting slope:** KCL $i_C+i_L=0$, so $i_C(0^+)=3\,\mathrm{A}$ downward.', r"v'(0^+)=\dfrac{3}{0.25}=12\,\mathrm{V/s}"),
       S(r'**Constant:** $v\prime(0)=\sqrt{10}\,B=12$.', r'B=\dfrac{12}{\sqrt{10}}\approx3.795')],
      r'(a) $v=\dfrac{12}{\sqrt{10}}\sin(\sqrt{10}\,t)\,\mathrm{V}$. (b) $\omega_0=\sqrt{10}\approx3.162\,\mathrm{rad/s}$. (c) $3.795\,\mathrm{V}$; with no $R$ it never decays.',
      cites=D.tb('8.14'))
    P(D, 'W5 · Read the circuit back from its response · textbook P8.3',
      r'In a parallel RLC circuit, $C=50\,\mathrm{nF}$ and the voltage is $v=-5e^{-5000t}+20e^{-20000t}\,\mathrm{V}$ for $t\ge0$. '
      r'Find $\alpha$, $\omega_0$, $L$ and $R$.' '\n\n' + sch(P83),
      [S(r'**Type:** two decaying exponentials = overdamped. The exponents are the roots $s_1=-5000$, $s_2=-20000$.'),
       S(r'**Roots → equation:** $s^2+2\alpha s+\omega_0^2=(s+5000)(s+20000)$. Compare: $2\alpha$ is the sum, $\omega_0^2$ the product.', r's^2+25000s+10^8=0'),
       S(r'So $\alpha=12500\,\mathrm{s^{-1}}$ and $\omega_0=10^4\,\mathrm{rad/s}$.'),
       S(r'$\omega_0^2=\dfrac{1}{LC}$ gives $L$.', r'L=\dfrac{1}{10^8\times50\times10^{-9}}=0.2\,\mathrm{H}'),
       S(r'Parallel: $\alpha=\dfrac{1}{2RC}$ gives $R$.', r'R=\dfrac{1}{2(12500)(50\times10^{-9})}=800\,\Omega')],
      r'$\alpha=12500\,\mathrm{s^{-1}}$, $\omega_0=10^4\,\mathrm{rad/s}$, $L=0.2\,\mathrm{H}$, $R=800\,\Omega$.',
      cites=D.tb('8.3'))
    P(D, 'W5 · Switch to a series loop · textbook P8.44',
      r'The switch has been in position $a$ for a long time. At $t=0$ it moves to $b$. Find $i(t)$ for $t\ge0$.' '\n\n' + sch(P844),
      [S(r'**Type:** after the switch, $C$, $200\,\Omega$ and $L$ form one loop with no source: series RLC natural response.'),
       S(r'**Before:** in position $a$, $C$ is open in steady state, so no current in $50\,\Omega$ and $C$ charges to the source. $L$ is disconnected.', r'v_C(0^-)=70\,\mathrm{V},\quad i(0^-)=0'),
       S(r'**Starting slope:** KVL round the new loop, $v_C=Ri+L\,i\prime$, at $0^+$.', r"i'(0^+)=\dfrac{70-200(0)}{0.1}=700\,\mathrm{A/s}"),
       S(r'**Equation:** $\alpha=\dfrac{200}{2(0.1)}=1000$, $\omega_0^2=\dfrac{1}{0.1\times200\times10^{-9}}=5\times10^7$. $\alpha<\omega_0$: underdamped.', r'\omega_d=\sqrt{5\times10^7-10^6}=7000\,\mathrm{rad/s}'),
       S(r'**Form:** $i(0)=0$ removes the cosine.', r'i=B\,e^{-1000t}\sin7000t'),
       S(r'**Constant:** at $t=0$ the slope is $7000B=700$.', r'B=0.1')],
      r'$i=0.1\,e^{-1000t}\sin7000t\ \mathrm{A}$ $=100\,e^{-1000t}\sin7000t\ \mathrm{mA}$, $t\ge0$.',
      diff='intermediate', cites=D.tb('8.44'))
    P(D, 'W5 · The slope comes from KCL · textbook P8.7',
      r'$R=\tfrac{12500}{3}\,\Omega$, $L=250\,\mathrm{mH}$, $C=10\,\mathrm{nF}$ in parallel. Initially $v(0)=90\,\mathrm{V}$ and $i_L(0)=-30\,\mathrm{mA}$ (references as drawn). Find $v(t)$ for $t\ge0$.'
      '\n\n' + sch(P87),
      [S(r'**Type:** parallel RLC, no source: natural response.'),
       S(r'**Starting slope:** $i_R=\dfrac{90}{12500/3}=21.6\,\mathrm{mA}$. KCL $i_C+i_L+i_R=0$.', r'i_C(0^+)=30-21.6=8.4\,\mathrm{mA}'),
       S(r'Divide by $C$.', r"v'(0^+)=\dfrac{8.4\times10^{-3}}{10^{-8}}=8.4\times10^5\,\mathrm{V/s}"),
       S(r'**Equation:** $\alpha=\dfrac{1}{2RC}=12000$, $\omega_0=\dfrac{1}{\sqrt{LC}}=20000$. $\alpha<\omega_0$: underdamped.', r'\omega_d=\sqrt{20000^2-12000^2}=16000'),
       S(r'**Form** with $v(0)=90$ as the cosine coefficient.', r'v=e^{-12000t}(90\cos16000t+B_2\sin16000t)'),
       S(r'**Constant:** slope at 0 is $-\alpha(90)+\omega_dB_2$.', r'-12000(90)+16000B_2=840000\ \Rightarrow\ B_2=120')],
      r'$v=e^{-12000t}(90\cos16000t+120\sin16000t)\,\mathrm{V}$, $t\ge0$.',
      diff='intermediate', cites=D.tb('8.7'))
    P(D, 'W5 · Choose R for critical damping · textbook P8.42',
      r'$R$ is adjusted for critical damping. At the moment the switch closes, $v_C=90\,\mathrm{V}$ and the inductor current is $i=24\,\mathrm{mA}$. '
      r'Find (a) $R$, (b) $i$ and $\dfrac{di}{dt}$ just after closing, (c) $i(t)$ and $v_C(t)$ for $t\ge0$.' '\n\n' + sch(P842),
      [S(r'**Type:** one loop, no source: series RLC natural response. Critical means $\alpha=\omega_0$.'),
       S(r'**(a)** $\omega_0=\dfrac{1}{\sqrt{0.25\times160\times10^{-9}}}=5000$. Set $\dfrac{R}{2L}=5000$.', r'R=2(0.25)(5000)=2500\,\Omega'),
       S(r'**(b)** $i$ is an inductor current, so it carries over. KVL round the loop: $v_C=Ri+L\,i\prime$.', r"i'(0^+)=\dfrac{90-2500(0.024)}{0.25}=120\,\mathrm{A/s}"),
       S(r'**(c) Form:** repeated root $-5000$.', r'i=(A_1+A_2t)e^{-5000t}'),
       S(r'**Constants:** $A_1=i(0)=0.024$; slope $A_2-5000A_1=120$.', r'A_2=240'),
       S(r'Then $v_C=Ri+L\,i\prime$ (or check: $i=-C\,v_C\prime$, since $i$ leaves the $+$ of $C$).', r'v_C=(90+3\times10^5\,t)e^{-5000t}')],
      r'(a) $R=2500\,\Omega$. (b) $i(0^+)=24\,\mathrm{mA}$, $i\prime(0^+)=120\,\mathrm{A/s}$. (c) $i=(0.024+240t)e^{-5000t}\,\mathrm{A}$, $v_C=(90+3\times10^5t)e^{-5000t}\,\mathrm{V}$.',
      diff='advanced', cites=D.tb('8.42'))
    P(D, 'W5 + W6 · The answer is zero · textbook P8.24',
      r'The switch has been open a long time; the capacitor is uncharged. At $t=0$ it closes. Find $v_o(t)$ for $t\ge0$.' '\n\n' + sch(P824),
      [S(r'**Type:** after closing, $L$ and $C$ share the top node, fed through $400\,\Omega$: a parallel RLC with a DC source.'),
       S(r'**Before:** $L$ is a short in steady state, so it carries all the source current; $C$ is disconnected and uncharged.', r'i_L(0^-)=\dfrac{12}{400}=30\,\mathrm{mA},\quad v_o(0^-)=0'),
       S(r'**Starting slope:** at $0^+$, $v_o=0$ so the $400\,\Omega$ still carries $30\,\mathrm{mA}$, and all of it goes into $L$. KCL leaves nothing for $C$.', r'i_C(0^+)=30-30=0\ \Rightarrow\ v_o\prime(0^+)=0'),
       S(r'**Equation:** KCL $\dfrac{v_o-12}{400}+i_L+Cv_o\prime=0$. Differentiating removes the constant 12, so the equation is homogeneous.', r"Cv_o''+\dfrac{v_o'}{400}+\dfrac{v_o}{L}=0"),
       S(r'**Condition:** a homogeneous linear equation with $v_o(0)=0$ and $v_o\prime(0)=0$ has only the zero solution (the zero-start rule in ' + link('Topic C', 'topic-c') + ').')],
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
