"""D2: RLC circuits (Week 5). Built around what the lecture taught: the parallel RLC natural response, the step
response i_L = I + natural response, and Example 5.2 (24 mA, 400 ohm, 25 nF, 25 mH)."""
import sympy as sp

from midlib import CARD, P, S, TAGS, link, second, t, zero


def sch(src):
    """A circuit drawn inside a problem or example prompt."""
    return '```schematic\n' + src.strip() + '\n```'


PARALLEL = r'''
C1 0,3 -> 0,0 "$C$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$L$" i="$i_L$"
wire 3,3 -> 6,3
R1 6,3 -> 6,0 "$R$" i="$i_R$"
wire 6,0 -> 0,0
ground 0,0
'''

EX52 = r'''
I1 0,0 -> 0,3 "$24\,\mathrm{mA}$"
S1 0,3 -> 3,3 "$t=0$" action=close
C1 3,3 -> 3,0 "$25\,\mathrm{nF}$" v="$v$" i="$i_C$"
wire 3,3 -> 6,3
L1 6,3 -> 6,0 "$25\,\mathrm{mH}$" i="$i_L$"
wire 6,3 -> 9,3
R1 9,3 -> 9,0 "$R$" i="$i_R$"
wire 9,0 -> 0,0
ground 0,0
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


def build(D):
    W5 = lambda *p: D.cite('W5', *p)
    D.H('D2 · An L and a C: RLC circuits (second order)', level=2, cites=W5(1, 2, 4, 5, 6))
    TAGS(D, (5, 3))
    D.P(r'**Use this when**, after the switch, there’s an inductor **and** a capacitor.')
    D.P(r'**The move: it’s ' + link('B5', 'b5') + r' with circuit names.** The lecture’s parallel RLC gives this quadratic:')
    D.EQ(r's^2+\dfrac{1}{RC}\,s+\dfrac{1}{LC}=0')
    D.SCH(PARALLEL.strip(), 'Parallel RLC (lecture Fig. 1): the same voltage $v$ sits across every element. All three current arrows point down.')
    D.P(r'Name the two numbers in it:')
    D.EQ(r'\alpha=\dfrac{1}{2RC},\qquad \omega_0=\dfrac{1}{\sqrt{LC}}')
    D.P(r'Then the roots are (lecture eq. 5.7):')
    D.EQ(r's_{1,2}=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}')
    D.P(r'**Short example** (lecture Example 5.2): $R=400\,\Omega$, $C=25\,\mathrm{nF}$, $L=25\,\mathrm{mH}$:')
    D.EQ(r'\alpha=\dfrac{1}{2(400)(25\times10^{-9})}=50\,000,\qquad \omega_0=\dfrac{1}{\sqrt{(25\times10^{-3})(25\times10^{-9})}}=40\,000')
    D.P(r'(Series RLC, seen once in Week 2: $\;i\prime\prime+\frac RL\,i\prime+\frac1{LC}\,i=0$, so $\alpha=\frac{R}{2L}$ instead. Same $\omega_0$.)')

    D.H('The three cases (same as B5)', level=3)
    D.T(['Compare', 'Name', 'B5 case', 'Form'], [
        [r'$\alpha>\omega_0$', '**overdamped**', 'Case 1', r'$c_1e^{s_1t}+c_2e^{s_2t}$'],
        [r'$\alpha=\omega_0$', '**critically damped**', 'Case 2', r'$(c_1+c_2t)e^{-\alpha t}$'],
        [r'$\alpha<\omega_0$', '**underdamped**', 'Case 3', r'$e^{-\alpha t}(c_1\cos\omega_dt+c_2\sin\omega_dt)$'],
    ], cites=W5(2, 3))
    D.P(r'Underdamped swings at $\omega_d$ (the B5 $\omega$; and $\sigma=-\alpha$):')
    D.EQ(r'\omega_d=\sqrt{\omega_0^2-\alpha^2}')
    D.P(r'**Short examples:**')
    D.EQ(r'\alpha=50\,000,\ \omega_0=40\,000\quad\Longrightarrow\quad s=-50\,000\pm30\,000\quad\text{(overdamped)}')
    D.EQ(r'\alpha=\omega_0=40\,000\quad\Longrightarrow\quad (c_1+c_2t)e^{-40\,000t}\quad\text{(critical)}')
    D.EQ(r'\alpha=32\,000,\ \omega_0=40\,000\quad\Longrightarrow\quad \omega_d=24\,000\quad\text{(underdamped)}')

    D.H('Step response: final value + natural response', level=3)
    D.P(r'A DC source switched on (lecture §3): the answer is the **final value** plus the natural response, like $y_p+y_c$ in ' + link('B6', 'b6') + ':')
    D.EQ(r'i_L(t)=I+(\text{the B5 form})')
    D.P(r'Why $I$: long after, $L$ is a wire, so it carries **all** of the source current. (That’s the lecture’s $I_P=I$.)', cites=W5(5))

    D.P('**Steps**')
    D.L([r'**Before:** old circuit. “No initial energy” means $v(0)=0$ and $i_L(0)=0$ (since $\tfrac12Cv^2=\tfrac12Li^2=0$).',
         r'**Carry across:** $v(0^+)=v(0^-)$, $i_L(0^+)=i_L(0^-)$. Then the slope (cards below).',
         r'**After:** compute $\alpha$, $\omega_0$. Final value: $I$ for $i_L$ with a source on, $0$ with none.',
         r'**Pick** the case (compare $\alpha$, $\omega_0$) and write $x=x_f+$ the form.',
         r'**Plug in** $t=0$: the value gives one equation, the slope gives the other. Use the **whole** answer, $x_f$ included.',
         r'**Check:** $t\to\infty$ gives $x_f$.'], ordered=True)
    CARD(D, r'Slope of $i_L$: $\;\dfrac{di_L}{dt}(0^+)=\dfrac{v(0^+)}{L}$',
         [(r'From $v=L\frac{di_L}{dt}$. The lecture uses this in Example 5.2: $v(0)=0$, so the slope is $0$.', r'\dfrac{di_L}{dt}(0^+)=\dfrac{0}{L}=0')])
    CARD(D, r'Slope of $v$: KCL, $\;i_C=-(i_L+i_R)$, then $\;v\prime(0^+)=\dfrac{i_C(0^+)}{C}$',
         [(r'All three arrows point down, so the currents add to $0$ (plus any source current coming in). $i_R=\frac{v(0^+)}{R}$.', r'i_C(0^+)=-\big(i_L(0^+)+i_R(0^+)\big)'),
          (r'Example: $v=10\,\mathrm{V}$, $R=5\,\Omega$, $i_L=1\,\mathrm{A}$, $C=0.5\,\mathrm{F}$.', (r'i_C=-(1+2)=-3\,\mathrm{A}', r'v\prime(0^+)=\dfrac{-3}{0.5}=-6\,\mathrm{V/s}'))])
    D.CO('warning', r'**Fit the constants to the whole answer, the final value included.** $i_L=24+A_1e^{s_1t}+A_2e^{s_2t}$ with $i_L(0)=0$: $\;24+A_1+A_2=0$, not $A_1+A_2=0$.')
    D.CO('warning', r'**Units first.** $1\,\mathrm{mH}=10^{-3}\,\mathrm{H}$, $1\,\mu\mathrm{F}=10^{-6}\,\mathrm{F}$, $1\,\mathrm{nF}=10^{-9}\,\mathrm{F}$. '
         r'Keep currents in mA and the constants come out in mA.')

    D.H('Practice: D2', level=3)
    P(D, '★ W5 · Parallel RLC step response · lecture Example 5.2',
      r'The initial energy stored in the circuit is zero. At $t=0$ a DC current source of $24\,\mathrm{mA}$ is switched on. '
      r'$R=400\,\Omega$, $C=25\,\mathrm{nF}$, $L=25\,\mathrm{mH}$. Find $i_L(t)$, $t\ge0$.' '\n\n' + sch(EX52),
      [S(r'**Type:** an $L$ and a $C$ → second order → D2. A source stays on → step response: $i_L=24+$ natural.'),
       S(r'**Before:** zero energy, so nothing is stored.', r'v(0)=0,\qquad i_L(0)=0'),
       S(r'**Carry across** (slope): $L\frac{di_L}{dt}=v$, and $v(0)=0$.', r'\dfrac{di_L}{dt}(0)=0'),
       S(r'**After:** $\alpha$ and $\omega_0$.', (r'\alpha=\dfrac{1}{2RC}=\dfrac{1}{2(400)(25\times10^{-9})}=50\,000', r'\omega_0=\dfrac{1}{\sqrt{LC}}=40\,000')),
       S(r'**Pick:** $\alpha>\omega_0$, overdamped (B5 Case 1). Roots:', (r's=-50\,000\pm\sqrt{50\,000^2-40\,000^2}=-50\,000\pm30\,000', r's_1=-20\,000,\qquad s_2=-80\,000')),
       S(r'Write the whole answer (mA).', r'i_L=24+A_1e^{-20\,000t}+A_2e^{-80\,000t}'),
       S(r'**Plug in** $i_L(0)=0$.', r'24+A_1+A_2=0'),
       S(r'**Plug in** the slope: differentiate, then $t=0$.', r'-20\,000A_1-80\,000A_2=0\quad\Rightarrow\quad A_1=-4A_2'),
       S(r'Solve: $-4A_2+A_2=-24$.', r'A_2=8,\qquad A_1=-32'),
       S(r'**Check:** $t\to\infty$ gives $24\,\mathrm{mA}$ ✓ (all the source current through the wire-like $L$).')],
      r'$i_L(t)=24-32e^{-20\,000t}+8e^{-80\,000t}\ \mathrm{mA}$, $t\ge0$.', cites=W5(5, 6))
    P(D, 'W5 · Same circuit, R = 500 Ω: critically damped · like lecture Example 5.2',
      r'Repeat lecture Example 5.2 with $R=500\,\Omega$ (zero initial energy, $24\,\mathrm{mA}$, $25\,\mathrm{nF}$, $25\,\mathrm{mH}$). Find $i_L(t)$.',
      [S(r'**Type:** same as Example 5.2: $i_L=24+$ natural, with $i_L(0)=0$ and $i_L\prime(0)=0$.'),
       S(r'**After:** only $\alpha$ changes.', (r'\alpha=\dfrac{1}{2(500)(25\times10^{-9})}=40\,000', r'\omega_0=40\,000')),
       S(r'**Pick:** $\alpha=\omega_0$, critically damped (B5 Case 2), root $-40\,000$ twice.', r'i_L=24+(D_1t+D_2)\,e^{-40\,000t}'),
       S(r'**Plug in** $i_L(0)=0$.', r'24+D_2=0\quad\Rightarrow\quad D_2=-24'),
       S(r'**Plug in** the slope. Product rule: $i_L\prime(0)=D_1-40\,000D_2$.', r'D_1-40\,000(-24)=0\quad\Rightarrow\quad D_1=-960\,000')],
      r'$i_L(t)=24-960\,000\,t\,e^{-40\,000t}-24e^{-40\,000t}\ \mathrm{mA}$.', diff='intermediate')
    P(D, 'W5 · Same circuit, R = 625 Ω: underdamped · like lecture Example 5.2',
      r'Repeat lecture Example 5.2 with $R=625\,\Omega$. Find $i_L(t)$.',
      [S(r'**Type:** same as Example 5.2: $i_L=24+$ natural, with $i_L(0)=0$ and $i_L\prime(0)=0$.'),
       S(r'**After:**', (r'\alpha=\dfrac{1}{2(625)(25\times10^{-9})}=32\,000', r'\omega_0=40\,000')),
       S(r'**Pick:** $\alpha<\omega_0$, underdamped (B5 Case 3).', (r'\omega_d=\sqrt{40\,000^2-32\,000^2}=24\,000', r'i_L=24+e^{-32\,000t}(B_1\cos24\,000t+B_2\sin24\,000t)')),
       S(r'**Plug in** $i_L(0)=0$.', r'24+B_1=0\quad\Rightarrow\quad B_1=-24'),
       S(r'**Plug in** the slope ($\sigma c_1+\omega c_2$ from B5).', r'-32\,000B_1+24\,000B_2=0\quad\Rightarrow\quad B_2=-32')],
      r'$i_L(t)=24-e^{-32\,000t}\big(24\cos24\,000t+32\sin24\,000t\big)\ \mathrm{mA}$.', diff='intermediate')
    P(D, 'W5 · Natural response: the slope comes from KCL · textbook P8.7',
      r'$R=\tfrac{12500}{3}\,\Omega$, $L=250\,\mathrm{mH}$ and $C=10\,\mathrm{nF}$ are in parallel, with no source. At the start, $v(0)=90\,\mathrm{V}$ and $i_L(0)=-30\,\mathrm{mA}$ (arrows as drawn). Find $v(t)$ for $t\ge0$.'
      '\n\n' + sch(P87),
      [S(r'**Type:** parallel RLC, no source: a natural response, final value $0$.'),
       S(r'**Carry across** (slope): first the resistor current, $i_R=\dfrac{90}{12500/3}=21.6\,\mathrm{mA}$. KCL (all arrows down): $i_C=-(i_L+i_R)$.', r'i_C(0^+)=-(-30+21.6)=8.4\,\mathrm{mA}'),
       S(r'Divide by $C$ to get the slope.', r"v'(0^+)=\dfrac{8.4\times10^{-3}}{10^{-8}}=8.4\times10^5\,\mathrm{V/s}"),
       S(r'**After:** $\alpha=\dfrac{1}{2RC}=12\,000$ and $\omega_0=\dfrac{1}{\sqrt{LC}}=20\,000$. $\alpha<\omega_0$, so underdamped.', r'\omega_d=\sqrt{20\,000^2-12\,000^2}=16\,000'),
       S(r'**Pick:** the cosine coefficient is $v(0)=90$.', r'v=e^{-12\,000t}(90\cos16\,000t+c_2\sin16\,000t)'),
       S(r'**Plug in** the slope: $-\alpha(90)+\omega_dc_2=8.4\times10^5$.', r'-12\,000(90)+16\,000c_2=840\,000\ \Rightarrow\ c_2=120')],
      r'$v=e^{-12\,000t}(90\cos16\,000t+120\sin16\,000t)\,\mathrm{V}$, $t\ge0$.',
      diff='intermediate', cites=D.tb('8.7'))


def verify():
    E = sp.exp
    L, C, I = sp.Rational(25, 1000), sp.Rational(25, 10 ** 9), 24
    for R, il in ((400, 24 - 32 * E(-20000 * t) + 8 * E(-80000 * t)),
                  (500, 24 - 960000 * t * E(-40000 * t) - 24 * E(-40000 * t)),
                  (625, 24 - E(-32000 * t) * (24 * sp.cos(24000 * t) + 32 * sp.sin(24000 * t)))):
        second(il, 1, 1 / (R * C), 1 / (L * C), I / (L * C), initial=(0, 0, 0))
    assert 1 / (2 * 400 * C) == 50000 and 1 / sp.sqrt(L * C) == 40000
    assert 1 / (2 * 500 * C) == 40000 and 1 / (2 * 625 * C) == 32000
    # P8.7
    C, L, R = sp.Rational(1, 10 ** 8), sp.Rational(1, 4), sp.Rational(12500, 3)
    vp = E(-12000 * t) * (90 * sp.cos(16000 * t) + 120 * sp.sin(16000 * t))
    slope = -(sp.Rational(-30, 1000) + 90 / R) / C
    assert slope == 840000
    second(vp, 1, 1 / (R * C), 1 / (L * C), initial=(0, 90, slope))
    il = -C * sp.diff(vp, t) - vp / R
    zero(il.subs(t, 0) + sp.Rational(30, 1000))
    zero(L * sp.diff(il, t) - vp)
