#### SECTION header
"""Week 5, v3 layout (assembled by make_w5v3.py from build_w5.py pieces + w5v3_new.py). Do not edit by hand."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import circuits5v3  # noqa: E402,F401
from blocks45 import Doc, S  # noqa: E402
from w45lib import C, view, fence, off  # noqa: E402
from weekkit import card  # noqa: E402

D = Doc('w5-v3', 5)
H, P, CO, L, T, EQ, SCH, PR = D.H, D.P, D.CO, D.L, D.T, D.EQ, D.SCH, D.PR


def EX(key, title, intro, fig, steps, answer, cites=(), after=''):
    """Worked examples always show their height picture in the page."""
    if '#@ inline' not in fig:
        fig = fig.replace('\n#@ spoiler', '\n#@ inline', 1) if '\n#@ spoiler' in fig else fig.replace('\n#@ ', '\n#@ inline\n#@ ', 1)
    D.EX(key, title, intro, fig, steps, answer, cites, after)


OFFV = lambda v: ('W', rf'${v}\,\mathrm{{V}}$ off: a wire')  # noqa: E731
OFFI = lambda i: ('S', rf'${i}\,\mathrm{{A}}$ off: a gap')  # noqa: E731
SHORT = ('W', 'short: no step')
TEST = ('I', r'test $1\,\mathrm{A}$')
SC = lambda a='a': ('V', 'SC', a, '0', 0)  # noqa: E731
IT = lambda a='a', amps=1: ('I', 'IT', '0', a, amps)  # noqa: E731
drop = lambda net, *names: [e for e in net if e[1] not in names]  # noqa: E731
alone = lambda net, keep: drop(off(net, keep=(keep,)), *[e[1] for e in net if e[0] == 'I' and e[1] != keep])  # noqa: E731

card(D, "**Week 5 in one line:** finish Thévenin (diamonds inside), then use it twice: **maximum power** (the best load sits at half the open height) and **superposition** (one source at a time, then add the heights).",
     "a diamond **never** turns off, and when you split a circuit into one-source pictures, **heights add but powers don't**.")

#### SECTION topic1
H(1, 'Topic 1: Thévenin with diamonds inside', D.oc('Topic 1: Thévenin and Norton'))
CO('tip', "**How it looks in heights.**\n\n"
          "- A diamond **never turns off**: keep it in every picture, with what it depends on.\n"
          "- **Push $1\\,\\mathrm{A}$ into $a$** (independent sources off): $a$'s height is $R_{\\mathrm{Th}}$. If $a$ goes **up** when you pull current out, $R_{\\mathrm{Th}}$ is negative: the diamond is giving energy.\n"
          "- No independent source at all: nothing lifts $a$, so $V_{\\mathrm{Th}}=0$ and only the push finds $R_{\\mathrm{Th}}$.\n"
          "- One shot: keep everything on and push $i_T$: then $a=V_{\\mathrm{Th}}+R_{\\mathrm{Th}}\\,i_T$ (start height + slope).")

#### SECTION p474
n = C['p474']['net']
nm = {'n': '$n$', 'm': '$m$', 'a': '$a$', '0': '$b$'}
el = {'E1': r'$160i_\Delta$'}
PR('p474', 'A diamond battery on the top wire (Textbook P4.74)', 'intermediate',
   r'Find the Thévenin equivalent at $a$–$b$.',
   fence('p474', [
       view(n, [('I1', 0), ('R1', 1), ('R2', 2), ('E1', 2), ('R3', 3), ('R4', 4)], title='Open', names=nm, elabel=el, terminals={'a'}, steps=[
           (r"Ground $b$. The $4\,\mathrm{A}$ pump pushes into $n$.", []),
           (r"The diamond is a battery of $160i_\Delta$ with $+$ at $m$, where $i_\Delta=\dfrac{a}{40}$ (the current down the $40\,\Omega$). So $m=a+4a=5a$.", []),
           (r"In = out at $n$: $4=\dfrac{n}{60}+\dfrac{n-m}{20}$. In = out for the bubble $\{m,a\}$: $\dfrac{n-m}{20}=\dfrac{a}{80}+\dfrac{a}{40}$. So $a=30\,\mathrm{V}=V_{\mathrm{Th}}$, $m=150$, $n=172.5\,\mathrm{V}$.", ['a', 'm', 'n']),
           (r"Currents: $2.875\,\mathrm{A}$ down the $60\,\Omega$; $1.125\,\mathrm{A}$ through the $20\,\Omega$ and **down** through the diamond (it absorbs); $0.375+0.75\,\mathrm{A}$ down the $80\,\Omega$ and $40\,\Omega$.", ['eR1', 'eR2', 'eR3', 'eR4', 'eE1', 'eI1']),
       ]),
       view(off(n) + [IT()], [('IT', 0), ('R3', 1), ('R4', 2), ('E1', 3), ('R2', 4), ('R1', 4), ('I1', 5)], title='Sources off, push 1 A', names=nm, elabel=el,
            terminals={'a'}, disp={'I1': OFFI(4), 'IT': TEST}, steps=[
           (r"Same ground. The pump → gap. The diamond **stays on**.", []),
           (r"Push $1\,\mathrm{A}$ into $a$. Still $m=5a$. Paths from $a$: down the $80\,\Omega$ and $40\,\Omega$, or up through the diamond to $m$ and down $20+60\,\Omega$: $1=\dfrac{a}{80}+\dfrac{a}{40}+\dfrac{5a}{80}=\dfrac{a}{10}$.", []),
           (r"$a=10\,\mathrm{V}$ per amp: $R_{\mathrm{Th}}=10\,\Omega$. The diamond lifts $0.625\,\mathrm{A}$ from $a$ up to $m$ (it gives energy), which is why $a$ only climbs $10\,\mathrm{V}$.", ['a', 'm', 'n', 'eR1', 'eR2', 'eR3', 'eR4', 'eE1', 'eIT']),
       ]),
   ]),
   [S(r'Control: $i_\Delta=\dfrac{v_a}{40}$, so the diamond gives $v_m=v_a+160i_\Delta=5v_a$.', r'4=\frac{v_n}{60}+\frac{v_n-5v_a}{20},\qquad \frac{v_n-5v_a}{20}=\frac{v_a}{80}+\frac{v_a}{40}'),
    S('Solve.', r'v_a=V_{\mathrm{Th}}=30\,\mathrm{V},\qquad v_n=172.5\,\mathrm{V}'),
    S('Test current, pump off.', r'1=\frac{v_a}{80}+\frac{v_a}{40}+\frac{5v_a}{80}=\frac{v_a}{10}\;\Rightarrow\;R_{\mathrm{Th}}=10\,\Omega')],
   r'$V_{\mathrm{Th}}=30\,\mathrm{V}$, $R_{\mathrm{Th}}=10\,\Omega$', D.tb('4.74'))

#### SECTION p481
n = C['p481']['net']
PR('p481', 'Only a diamond inside (Textbook P4.81)', 'intermediate',
   r'Find the Thévenin equivalent at $a$–$b$.',
   fence('p481', [view(n + [IT()], [('E1', 0), ('R2', 0), ('R1', 1), ('R3', 2), ('R4', 3), ('R5', 4), ('IT', 5)], title='Push 1 A into a', gnd='low',
                       names={'a': '$a$', 'm': '$m$', 't': '$t$', 'k': '$k$', '0': '$b$'}, elabel={'E1': r'$6.5i_x$'}, terminals={'a'}, disp={'IT': TEST}, steps=[
       (r"Ground $k$, the lowest wire (the diamond's $-$ end). No independent source, so with nothing attached every height is $0$: $V_{\mathrm{Th}}=0$.", []),
       (r"Push $1\,\mathrm{A}$ into $a$. It slides down the $12\,\Omega$ to $m$, so $m=a-12$.", ['eR5', 'eIT']),
       (r"The diamond is a battery of $6.5i_x$ ($+$ at $b$) with $i_x=\dfrac{m}{25}$. In = out at $m$ and at $t$ (from $b$): $m=8$, $t=1.2$, $a=20\,\mathrm{V}$.", ['m', 't', 'a', 'z0']),
       (r"$a$ sits $20\,\mathrm{V}$ above $b$ for $1\,\mathrm{A}$: $R_{\mathrm{Th}}=20\,\Omega$. With $V_{\mathrm{Th}}=0$ the terminals act like a plain $20\,\Omega$ resistor.", ['eR1', 'eR2', 'eR3', 'eR4', 'eE1']),
   ])]),
   [S('No independent source.', r'V_{\mathrm{Th}}=0'),
    S(r'Test current $1\,\mathrm{A}$ into $a$; $i_x=\dfrac{v_m}{25}$, diamond: $v_k=-6.5i_x$. In = out at $m$ and $t$.', r'\begin{aligned}1&=\tfrac{v_m}{25}+\tfrac{v_m-v_t}{10}\\\tfrac{v_m-v_t}{10}&=\tfrac{v_t}{50}+\tfrac{v_t+6.5v_m/25}{5}\end{aligned}'),
    S('Solve.', r'v_m=8\,\mathrm{V},\quad v_t=1.2\,\mathrm{V},\quad v_a=8+12=20\,\mathrm{V}\;\Rightarrow\;R_{\mathrm{Th}}=20\,\Omega')],
   r'$V_{\mathrm{Th}}=0$, $R_{\mathrm{Th}}=20\,\Omega$', D.tb('4.81'))

#### SECTION topic2
H(1, 'Topic 2: Maximum power: half the open height', D.oc('Topic 2: Maximum power'))
CO('tip', "**How it looks in heights.**\n\n"
          "- A load on a Thévenin source sits at some height $h$ and gets current $\\dfrac{V_{\\mathrm{Th}}-h}{R_{\\mathrm{Th}}}$. Its power $h\\cdot\\dfrac{V_{\\mathrm{Th}}-h}{R_{\\mathrm{Th}}}$ is biggest when $h=\\dfrac{V_{\\mathrm{Th}}}{2}$: the **half-height rule**. That happens when $R_L=R_{\\mathrm{Th}}$.\n"
          "- Half of $V_{\\mathrm{Th}}$, not half the battery.\n"
          "- Maximum power is not maximum efficiency. For efficiency, go back to the original circuit and compare the load's power with every source's climb.\n"
          "- Load fixed and a series resistor is the knob? That resistor only steals height: the best value is $0$.")

#### SECTION p483
n = C['p483']['net']
PR('p483', 'Match the load on a diamond circuit (Textbook P4.83)', 'intermediate',
   r'$R_o$ is connected across $a$–$b$ of the circuit in Try it 1 and adjusted for maximum power. **(a)** Find $R_o$. **(b)** Find $p_{\max}$. **(c)** What percentage of the power developed reaches $R_o$?',
   fence('p483', [view(n + [('R', 'RO', 'a', '0', 1)], [('V1', 0), ('R1', 1), ('G1', 2), ('I1', 3), ('R2', 4), ('RO', 5)], title='Matched: 1 Ω',
                       names={'s': 'battery top', 'a': '$a$', '0': '$b$'}, elabel={'G1': '$3i_x$'}, steps=[
       (r"Ground $b$. From Try it 1: $V_{\mathrm{Th}}=8\,\mathrm{V}$, $R_{\mathrm{Th}}=1\,\Omega$. So $R_o=1\,\Omega$.", []),
       (r"Half-height rule: $a$ sits at $4\,\mathrm{V}$. $p_{\max}=\dfrac{4^2}{1}=16\,\mathrm{W}$.", ['a', 'eRO']),
       (r"Climbs in the real circuit: the battery lifts $8.5\,\mathrm{A}$ by $24\,\mathrm{V}$ ($204\,\mathrm{W}$), the diamond $1.5\,\mathrm{A}$ by $20\,\mathrm{V}$ ($30\,\mathrm{W}$). The $4\,\mathrm{A}$ pump falls $4\,\mathrm{V}$ (it absorbs). $R_o$ gets $\dfrac{16}{234}=6.8\%$.", ['eV1', 'eR1', 'eG1', 'eI1', 'eR2']),
   ])]),
   [S('Match.', r'R_o=R_{\mathrm{Th}}=1\,\Omega,\qquad p_{\max}=\frac{8^2}{4(1)}=16\,\mathrm{W}'),
    S(r'Original circuit with $R_o=1\,\Omega$ ($v_a=4\,\mathrm{V}$, $i_x=0.5\,\mathrm{A}$).', r'p_{\text{dev}}=24(8.5)+20(1.5)=234\,\mathrm{W},\qquad \frac{16}{234}=6.84\%')],
   r'**(a)** $1\,\Omega$ **(b)** $16\,\mathrm{W}$ **(c)** $6.84\%$', D.tb('4.82'))

#### SECTION p487
n = C['p487']['net']
nm = {'s': 'battery top', 'p': '$p$', 'q': '$q$', 'k': 'diamond top', '0': '$b$'}
el = {'E1': r'$13i_\Delta$', 'G1': r'$v_\Delta$'}
PR('p487', 'Maximum power, and most of it gets there (Textbook P4.87)', 'advanced',
   r'$R_o$ is adjusted for maximum power. **(a)** Find $R_o$. **(b)** Find $p_{\max}$. **(c)** What percentage of the power developed reaches $R_o$?',
   fence('p487', [
       view(n, [('V1', 0), ('E1', 1), ('R2', 2), ('R1', 3), ('R3', 4), ('G1', 5)], title='Open', names=nm, elabel=el, refs={'R3': ('p', r'$v_\Delta$')}, steps=[
           (r"Ground the bottom wire. The battery lifts its top to $100\,\mathrm{V}$.", []),
           (r"Open: the pump pushes $v_\Delta=p-q$ into $q$, and only the $4\,\Omega$ can take it away: $\dfrac{p-q}{4}+(p-q)=0$, so $p=q$ and the $4\,\Omega$ lies flat.", ['eR3', 'eG1']),
           (r"Left loop: $100=2i_\Delta+5i_\Delta+13i_\Delta$, so $i_\Delta=5\,\mathrm{A}$ and $p=90\,\mathrm{V}$: $V_{\mathrm{Th}}=90\,\mathrm{V}$. (A short gives $I_N=100\,\mathrm{A}$, so $R_{\mathrm{Th}}=0.9\,\Omega$.)", ['p', 'q', 'k', 'eR1', 'eR2', 'eE1', 'eV1']),
       ]),
       view(n + [('R', 'RO', 'q', '0', 0.9)], [('V1', 0), ('E1', 1), ('R2', 2), ('R1', 3), ('R3', 3), ('RO', 3), ('G1', 4)], title='Matched: 0.9 Ω', names=nm, elabel=el,
            refs={'R3': ('p', r'$v_\Delta$')}, steps=[
           (r"Same ground. Matched: $q$ sits at half of $90$, $45\,\mathrm{V}$. $p_{\max}=\dfrac{45^2}{0.9}=2250\,\mathrm{W}$.", ['q', 'eRO']),
           (r"Climbs: battery $750\,\mathrm{W}$, diamond $243.75\,\mathrm{W}$, pump $40\,\mathrm{A}$ by $45\,\mathrm{V}=1800\,\mathrm{W}$. $R_o$ gets $\dfrac{2250}{2793.75}=80.5\%$: the diamond pump does most of the lifting.", ['p', 'k', 'eR1', 'eR2', 'eR3', 'eE1', 'eG1', 'eV1']),
       ]),
   ]),
   [S(r'Open: the pump forces $v_\Delta=0$; left loop.', r'\begin{aligned}&100=(2+5+13)\,i_\Delta\;\Rightarrow\;i_\Delta=5\,\mathrm{A}\\&V_{\mathrm{Th}}=100-2(5)=90\,\mathrm{V}\end{aligned}'),
    S(r'Short ($q=0$): $i_{sc}=100\,\mathrm{A}$.', r'R_{\mathrm{Th}}=\frac{90}{100}=0.9\,\Omega'),
    S('Match and efficiency.', r'p_{\max}=\frac{90^2}{4(0.9)}=2250\,\mathrm{W},\qquad \frac{2250}{750+243.75+1800}=80.5\%')],
   r'**(a)** $0.9\,\Omega$ **(b)** $2250\,\mathrm{W}$ **(c)** $80.5\%$', D.tb('4.87'))

#### SECTION topic3
H(1, 'Topic 3: Superposition: add heights, not powers', D.oc('Topic 3: Superposition'))
CO('tip', "**How it looks in heights.**\n\n"
          "- One picture per independent source: the other batteries become wires, the other pumps become gaps. **Diamonds stay on.**\n"
          "- **Add the heights** (voltages) and the currents from the pictures. **Never add powers**: power is a product, so compute it once from the sums.\n"
          "- Keep the same reference directions in every picture.\n"
          "- Worth it when each one-source picture is a simple divider; otherwise one node-voltage solve is faster.")

#### SECTION p495
n = C['p495']['net']
nm = {'s': '$s$', 'p': '$p$', 'q': '$q$', 'r': '$r$', '0': 'bottom'}
PR('p495', 'A battery and a pump (Textbook P4.95)', 'intermediate',
   r'Use superposition to find $i_o$ and $v_o$.',
   fence('p495', [
       view(drop(n, 'I1'), [('V1', 0), ('R1', 1), ('R2', 1), ('R6', 2), ('R4', 3), ('R3', 3), ('R5', 4)], title='180 V alone', names=nm, refs={'R3': ('q', '$v_o$')}, steps=[
           (r"Ground the bottom wire. The $7.5\,\mathrm{A}$ pump is off (a gap, left out). The battery lifts $s$ to $180\,\mathrm{V}$.", []),
           (r"In = out at $q$ and $r$ (and $p$ is a plain divider, $120\,\mathrm{V}$): $q=48$, $r=60\,\mathrm{V}$. So $v_o'=48\,\mathrm{V}$ and the battery sends $i_o'=5\,\mathrm{A}$.", ['p', 'q', 'r', 'eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eR6', 'eV1']),
       ]),
       view(off(n, keep=('I1',)), [('I1', 0), ('R1', 1), ('V1', 1), ('R2', 2), ('R6', 2), ('R5', 3), ('R4', 3), ('R3', 4)], title='7.5 A alone', gnd='low', names=nm,
            refs={'R3': ('q', '$v_o$')}, disp={'V1': OFFV(180)}, steps=[
           (r"Ground $q$, the lowest wire: the pump pulls its $7.5\,\mathrm{A}$ out of $q$. The battery → wire.", []),
           (r"In = out (from the bottom wire): $q=-184$, $p=150$, $r=-80\,\mathrm{V}$. So $v_o''=-184\,\mathrm{V}$, and $3\,\mathrm{A}$ flows **down** through the battery's spot: $i_o''=-3\,\mathrm{A}$.", ['p', 'r', 's', 'eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eR6', 'eV1', 'eI1']),
       ]),
       view(n, [('I1', 0), ('R1', 1), ('V1', 1), ('R5', 1), ('R4', 1), ('R6', 2), ('R2', 3), ('R3', 4)], title='Both: add', gnd='low', names=nm, refs={'R3': ('q', '$v_o$')}, steps=[
           (r"Ground $q$ again. Add: $v_o=48-184=-136\,\mathrm{V}$, $i_o=5-3=2\,\mathrm{A}$ (climbing through the battery).", ['eV1', 'z0']),
       ]),
   ]),
   [S(r'$180\,\mathrm{V}$ alone (pump open): node equations at $q$ and $r$.', r'v_o\'=48\,\mathrm{V},\qquad i_o\'=5\,\mathrm{A}'),
    S(r'$7.5\,\mathrm{A}$ alone (battery shorted).', r'v_o\'\'=-184\,\mathrm{V},\qquad i_o\'\'=-3\,\mathrm{A}'),
    S('Add.', r'v_o=48-184=-136\,\mathrm{V},\qquad i_o=5-3=2\,\mathrm{A}')],
   r'$i_o=2\,\mathrm{A}$, $v_o=-136\,\mathrm{V}$', D.tb('4.95'))

#### SECTION practice
H(1, 'Practice set')
P('Exam-style, mixing all three topics. Try each for 10–15 minutes before opening the solution, then check your picture against the height view.')

#### SECTION p498
n = C['p498']['net']
nm = {'s': '$s$', 'n': '$n$', '0': 'bottom'}
el = {'G1': r'$2.2i_\phi$'}
PR('p498', 'Textbook P4.98 · Superposition with a diamond that stays on', 'intermediate',
   r'Use superposition to find $v_o$.',
   fence('p498', [
       view(drop(n, 'I1'), [('V1', 0), ('G1', 1), ('R1', 2), ('R2', 3)], title='25 V alone', unit='mA', names=nm, elabel=el, refs={'R2': ('n', '$v_o$')}, steps=[
           (r"Ground the bottom wire. The $5\,\mathrm{mA}$ pump is off (a gap, left out). The battery lifts $s$ to $25\,\mathrm{V}$. The diamond stays on.", []),
           (r"The diamond pumps $2.2i_\phi$ from $s$ to $n$, with $i_\phi=\dfrac{n-25}{4}\,\mathrm{mA}$. In = out at $n$ (mA, kΩ): $2.2\dfrac{n-25}{4}=\dfrac{n-25}{4}+\dfrac{n}{20}$, so $n=30\,\mathrm{V}$: $v_o'=30\,\mathrm{V}$.", ['n', 'eG1', 'eR1', 'eR2', 'eV1']),
       ]),
       view(off(n, keep=('I1',)), [('V1', 0), ('G1', 1), ('R1', 2), ('I1', 3), ('R2', 4)], title='5 mA alone', unit='mA', names=nm, elabel=el, flip=('V1',),
            refs={'R2': ('n', '$v_o$')}, disp={'V1': OFFV(25)}, steps=[
           (r"Same ground. The battery → wire ($s=0$). The diamond stays on.", []),
           (r"In = out at $n$: $2.2\dfrac{n}{4}=\dfrac{n}{4}+5+\dfrac{n}{20}$, so $n=20\,\mathrm{V}$: $v_o''=20\,\mathrm{V}$. The diamond lifts $11\,\mathrm{mA}$; $5\,\mathrm{mA}$ falls back through the $4\,\mathrm{k\Omega}$ and $5\,\mathrm{mA}$ down through the pump.", ['n', 'eG1', 'eR1', 'eR2', 'eI1', 'eV1']),
       ]),
       view(n, [('V1', 0), ('G1', 1), ('R1', 2), ('I1', 3), ('R2', 4)], title='Both: add', unit='mA', names=nm, elabel=el, refs={'R2': ('n', '$v_o$')}, steps=[
           (r"Same ground. Add: $v_o=30+20=50\,\mathrm{V}$ ✓", ['n']),
       ]),
   ]),
   [S(r'$25\,\mathrm{V}$ alone, $i_\phi=\dfrac{v_o-25}{4}$ (mA, kΩ).', r'2.2\,\frac{v_o-25}{4}=\frac{v_o-25}{4}+\frac{v_o}{20}\;\Rightarrow\;v_o\'=30\,\mathrm{V}'),
    S(r'$5\,\mathrm{mA}$ alone, $i_\phi=\dfrac{v_o}{4}$.', r'2.2\,\frac{v_o}{4}=\frac{v_o}{4}+5+\frac{v_o}{20}\;\Rightarrow\;v_o\'\'=20\,\mathrm{V}'),
    S('Add.', r'v_o=30+20=50\,\mathrm{V}')],
   r'$v_o=50\,\mathrm{V}$', D.tb('4.98'))

#### SECTION cheat
H(1, 'Cheat sheet')
T(['Idea', 'In heights', 'Write'], [
    ['Thévenin with diamonds', 'push $1\\,\\mathrm{A}$ into $a$ (independent sources off)', r'$R_{\mathrm{Th}}=\dfrac{v_T}{i_T}$'],
    ['One-shot test source', 'start height + slope', r'$v_T=V_{\mathrm{Th}}+R_{\mathrm{Th}}i_T$'],
    ['No independent source', 'nothing lifts $a$', r'$V_{\mathrm{Th}}=I_N=0$'],
    ['Maximum power', 'load at half the open height', r'$R_L=R_{\mathrm{Th}}$, $p_{\max}=\dfrac{V_{\mathrm{Th}}^2}{4R_{\mathrm{Th}}}$'],
    ['Efficiency', 'load power ÷ all the climbs (original circuit)', r'$\eta=\dfrac{p_L}{\sum p_{\text{dev}}}$'],
    ['Superposition', 'one picture per source; add heights', r'$y=y_1+y_2+\cdots$, $p\neq p_1+p_2$'],
])
