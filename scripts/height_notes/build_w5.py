"""Week 5 rewrite (height method, Full loop views) -> w45/w5_blocks.json"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from blocks45 import Doc, S  # noqa: E402
from w45lib import C, view, fence, off  # noqa: E402

D = Doc('w5-v2', 5)
H, P, CO, L, T, EQ, SCH, EX, PR = D.H, D.P, D.CO, D.L, D.T, D.EQ, D.SCH, D.EX, D.PR
OFFV = lambda v: ('W', rf'${v}\,\mathrm{{V}}$ off: a wire')  # noqa: E731
OFFI = lambda i: ('S', rf'${i}\,\mathrm{{A}}$ off: a gap')  # noqa: E731
SHORT = ('W', 'short: no step')
TEST = ('I', r'test $1\,\mathrm{A}$')
SC = lambda a='a': ('V', 'SC', a, '0', 0)  # noqa: E731
IT = lambda a='a', amps=1: ('I', 'IT', '0', a, amps)  # noqa: E731
drop = lambda net, *names: [e for e in net if e[1] not in names]  # noqa: E731
alone = lambda net, keep: drop(off(net, keep=(keep,)), *[e[1] for e in net if e[0] == 'I' and e[1] != keep])  # noqa: E731

# =========================================================================== Overview
H(1, 'Overview')
CO('info', r"Week 5 finishes Thévenin (dependent sources inside), then uses it twice. **Maximum power:** the best load sits at **half the open height**. **Superposition:** one source at a time, then **add the voltages** (never the powers).")
H(2, 'Topic map')
T(['#', 'Topic', 'Key result', 'In heights'], [
    ['1', 'Thévenin with dependent sources', r'$R_{\mathrm{Th}}=\dfrac{v_T}{i_T}$', r'push current into $a$ and watch how far it climbs'],
    ['2', 'Maximum power transfer', r'$R_L=R_{\mathrm{Th}}$', r'the load sits at $\dfrac{V_{\mathrm{Th}}}{2}$'],
    ['3', 'Superposition', r'$y=y_1+y_2+\cdots$', 'one picture per source; add the height differences'],
])
CO('tip', "**How to use this note.** Shaky on Week 4? Read **Start here**. Each topic: rules → example → **Try it** (answer on paper first). Every circuit has a **Height view** (Full loop) with **Walk me through it**. The **Summary** at the end is a one-read crash course.")

# =========================================================================== Start here
H(1, 'Start here: the only Week 4 you need')
T(['#', 'Rule', 'Picture it as'], [
    ['1', r'Seen from $a$–$b$, a circuit is **one step $V_{\mathrm{Th}}$ + one slope $R_{\mathrm{Th}}$**.', 'an escalator, then a ramp'],
    ['2', r'**$V_{\mathrm{Th}}$** = height of $a$ with nothing attached (ground $b$).', 'open terminal'],
    ['3', r'**$I_N$** = current through a wire $a\to b$. $R_{\mathrm{Th}}=\dfrac{V_{\mathrm{Th}}}{I_N}$.', 'pull $a$ down to $b$'],
    ['4', r'**Sources off:** voltage → wire, current → gap. Push $1\,\mathrm{A}$ into $a$: its height is $R_{\mathrm{Th}}$.', 'sag per amp'],
    ['5', r'**A load** draws $i$, so $a$ sags: $v_{ab}=V_{\mathrm{Th}}-R_{\mathrm{Th}}i$.', 'the ramp'],
])
n = C['w5S']['net']
nm = {'s': 'source top', 'a': '$a$', '0': '$b$'}
EX('w5S', 'S · Open, short, sources off',
   r'Find $V_{\mathrm{Th}}$, $I_N$ and $R_{\mathrm{Th}}$ at $a$–$b$.',
   fence('w5S', [
       view(n, [('V1', 0), ('R1', 1), ('R2', 1)], title='Open', names=nm, terminals={'a'}, steps=[
           (r"Ground $b$. The source steps up $24\,\mathrm{V}$.", []),
           (r"Divider: $\dfrac{24}{16}=1.5\,\mathrm{A}$; the $4\,\Omega$ falls $6\,\mathrm{V}$, so $a=18\,\mathrm{V}=V_{\mathrm{Th}}$.", ['a', 'eR1', 'eR2', 'eV1']),
       ]),
       view(drop(n, 'R2') + [SC()], [('V1', 0), ('R1', 1), ('SC', 1)], title='Short', names=nm, disp={'SC': SHORT},
            notes=[r"The $12\,\Omega$ sits across the short (no fall, no current), so it is left out of this tab."], steps=[
           (r"Same ground. A wire pins $a$ to $b$. The $4\,\Omega$ falls all $24\,\mathrm{V}$: $I_N=6\,\mathrm{A}$, so $R_{\mathrm{Th}}=\dfrac{18}{6}=3\,\Omega$.", ['a', 'eR1', 'eSC', 'eV1']),
       ]),
       view(off(n) + [IT()], [('V1', 0), ('R1', 1), ('R2', 2), ('IT', 3)], title='Sources off, push 1 A', names=nm, terminals={'a'},
            disp={'V1': OFFV(24), 'IT': TEST}, steps=[
           (r"Same ground. Flatten the $24\,\mathrm{V}$. $1\,\mathrm{A}$ into $4\parallel12=3\,\Omega$: $a=3\,\mathrm{V}$, so $R_{\mathrm{Th}}=3\,\Omega$ ✓.", ['a', 'eR1', 'eR2', 'eIT']),
       ]),
   ], spoiler=False, inline=True),
   [S('Three numbers, one check.', r'V_{\mathrm{Th}}=24\cdot\tfrac{12}{16}=18\,\mathrm{V},\quad I_N=\tfrac{24}{4}=6\,\mathrm{A},\quad R_{\mathrm{Th}}=4\parallel12=3\,\Omega=\tfrac{18}{6}')],
   r'$V_{\mathrm{Th}}=18\,\mathrm{V}$, $I_N=6\,\mathrm{A}$, $R_{\mathrm{Th}}=3\,\Omega$.')
CO('info', r"**Signs.** $V_{\mathrm{Th}}<0$ means $a$ sits **below** $b$ when nothing is attached; then $I_N<0$ too (it flows $b\to a$) and $R_{\mathrm{Th}}=\dfrac{V_{\mathrm{Th}}}{I_N}$ stays positive.")

# =========================================================================== Topic 1
H(1, 'Topic 1: Thévenin with dependent sources', D.oc('Topic 1: Thévenin and Norton'))
L([r'A dependent source **can\'t be turned off**: keep it in every picture, with its control.',
   r'**Test source:** independent sources off, push $1\,\mathrm{A}$ into $a$. $a$\'s height per amp $=R_{\mathrm{Th}}$.',
   r'**One shot (all sources on):** push $i_T$ into $a$; then $a=V_{\mathrm{Th}}+R_{\mathrm{Th}}\,i_T$. Intercept = $V_{\mathrm{Th}}$, slope = $R_{\mathrm{Th}}$.',
   r'**No independent source** → nothing lifts $a$: $V_{\mathrm{Th}}=0$, $I_N=0$. Only a test source gives $R_{\mathrm{Th}}$.',
   r'**$R_{\mathrm{Th}}$ can be negative:** pull current out of $a$ and $a$ *rises*. The dependent source is delivering; don\'t draw it as a slope.',
   'Keep a dependent source and its control on the same side of $a$–$b$.'])
EQ(r'R_{\mathrm{Th}}=\frac{v_T}{i_T}\;(\text{independent sources off}),\qquad v_T=V_{\mathrm{Th}}+R_{\mathrm{Th}}\,i_T\;(\text{all on})')
T(['Inside the circuit', 'Fastest route to $R_{\\mathrm{Th}}$'], [
    ['independent sources only', 'sources off, combine resistors (or $V_{\\mathrm{Th}}/I_N$)'],
    ['independent + dependent', '$V_{\\mathrm{Th}}/I_N$, or a test source'],
    ['dependent only', 'test source ($V_{\\mathrm{Th}}=I_N=0$)'],
])
n = C['lecneg']['net']
EX('lecneg', 'Pull current out, and a rises (Lecture 5)',
   r'The network has only a dependent source. Find $V_{\mathrm{Th}}$ and $R_{\mathrm{Th}}$.',
   fence('lecneg', [view(n + [('I', 'IT', 'a', '0', 1)], [('E1', 0), ('R1', 1), ('R2', 1), ('IT', 2)], title='Pull 1 A out of a',
                         names={'s': '$s$', 'a': '$a$', '0': '$b$'}, terminals={'a'}, elabel={'E1': r'$12i_\Delta$'},
                         disp={'IT': ('I', r'test: pulls $1\,\mathrm{A}$ out')}, steps=[
       (r"Ground $b$. No independent source: with nothing attached every height is $0$, so $V_{\mathrm{Th}}=0$ and $I_N=0$. Only a test source can find $R_{\mathrm{Th}}$.", []),
       (r"Pull $1\,\mathrm{A}$ out of $a$. Control: $i_\Delta=\dfrac{a}{4}$, so the diamond's step is $12i_\Delta=3a$.", ['eIT']),
       (r"KCL at $a$: in from the $2\,\Omega$, $\dfrac{3a-a}{2}=a$; out, $\dfrac{a}{4}+1$. So $a=\tfrac43\,\mathrm{V}$ and $s=4\,\mathrm{V}$.", ['a', 's']),
       (r"A normal circuit sags when you pull current out. Here $a$ **rises**: $R_{\mathrm{Th}}=\dfrac{4/3}{-1}=-\tfrac43\,\Omega$. The diamond climbs $1.33\,\mathrm{A}$ through $4\,\mathrm{V}$: it delivers $5.33\,\mathrm{W}$.", ['eE1', 'eR1', 'eR2']),
   ], notes=[r"A negative $R_{\mathrm{Th}}$ is a source that pushes back, not a resistor."])]),
   [S(r'No independent source.', r'V_{\mathrm{Th}}=0,\qquad I_N=0'),
    S(r'Test current $i_T$ into $a$, control $i_\Delta=\dfrac{v_T}{4}$; KCL at $a$.', r'i_T+\frac{12i_\Delta-v_T}{2}=i_\Delta\;\Rightarrow\;i_T=-\tfrac34v_T'),
    S('Ratio.', r'R_{\mathrm{Th}}=\frac{v_T}{i_T}=-\tfrac43\,\Omega')],
   r'$V_{\mathrm{Th}}=0$, $R_{\mathrm{Th}}=-\tfrac43\,\Omega$.', D.oc('Lecture example · Test source on'))
n = C['lecm4']['net']
nm = {'s': '5 V top', 'm': '$m$', 'a': '$a$', '0': '$b$'}
EX('lecm4', 'One shot: the test source as a variable (Lecture 5)',
   r'Keep every source on and push a test current $i_T$ into $a$. Find $v_T$ as a function of $i_T$, then read off $V_{\mathrm{Th}}$, $R_{\mathrm{Th}}$ and $I_N$.',
   fence('lecm4', [
       view(n, [('R1', 0), ('V1', 1), ('E1', 2), ('G1', 3), ('R2', 4)], title='Open (no test current)', gnd='low', unit='mA', names=nm, terminals={'a'},
            elabel={'E1': '$3v$', 'G1': '$20i$'}, refs={'R2': ('a', '$v$')}, steps=[
           (r"Ground $m$, the lowest node. Every answer is a height **above $b$** (the bottom wire).", []),
           (r"All sources on, test current $i_T$ in. KCL at $a$: $i_T=\dfrac{v}{25}+20i$. Left loop: $5=2000i+3v$. With $v=v_T$: $v_T=100\,i_T-5$.", []),
           (r"With $i_T=0$, $a$ sits $5\,\mathrm{V}$ **below** $b$: $V_{\mathrm{Th}}=-5\,\mathrm{V}$. The diamond pump lifts $200\,\mathrm{mA}$ from $a$ up to $b$.", ['a', 'eG1', 'eR2']),
       ]),
       view(n + [('I', 'IT', '0', 'a', 0.1)], [('V1', 0), ('R1', 1), ('E1', 2), ('G1', 3), ('R2', 4), ('IT', 5)], title='Push 0.1 A into a', gnd='low', unit='mA',
            names=nm, terminals={'a'}, elabel={'E1': '$3v$', 'G1': '$20i$'}, refs={'R2': ('a', '$v$')}, disp={'IT': ('I', r'test $100\,\mathrm{mA}$')}, steps=[
           (r"Ground $b$ (now the lowest node). Push $0.1\,\mathrm{A}$ into $a$.", []),
           (r"$a$ rises to $100(0.1)-5=5\,\mathrm{V}$: $10\,\mathrm{V}$ higher for $0.1\,\mathrm{A}$, so $R_{\mathrm{Th}}=100\,\Omega$. And $I_N=\dfrac{-5}{100}=-50\,\mathrm{mA}$.", ['a', 'eIT', 'eR2', 'eG1']),
       ]),
   ]),
   [S(r'KCL at $a$ ($v=v_T$).', r'v_T=25\,(i_T-20i)'),
    S('Left loop.', r'5=2000\,i+3v_T\;\Rightarrow\;i=\frac{5-3v_T}{2000}'),
    S('Substitute.', r'v_T=25\,i_T-1.25+0.75\,v_T\;\Rightarrow\;v_T=100\,i_T-5'),
    S('Read off.', r'V_{\mathrm{Th}}=-5\,\mathrm{V},\quad R_{\mathrm{Th}}=100\,\Omega,\quad I_N=\frac{-5}{100}=-50\,\mathrm{mA}')],
   r'$v_T=100\,i_T-5$: $V_{\mathrm{Th}}=-5\,\mathrm{V}$, $R_{\mathrm{Th}}=100\,\Omega$, $I_N=-50\,\mathrm{mA}$.', D.oc('Lecture example · One analysis'))
n = C['ap419']['net']
nm = {'s': 'source top', 'a': '$a$', '0': '$b$'}
PR('ap419', 'Try it 1 · A diamond that feeds back (Assessment AP 4.19)', 'intermediate',
   r'Find the Thévenin equivalent at $a$–$b$. **(a)** $V_{\mathrm{Th}}$ **(b)** $R_{\mathrm{Th}}$ with a test source **(c)** check with $I_N$.',
   fence('ap419', [
       view(n, [('V1', 0), ('R1', 1), ('G1', 2), ('I1', 3), ('R2', 4)], title='Open', names=nm, terminals={'a'}, elabel={'G1': '$3i_x$'}, steps=[
           (r"Ground $b$. The source fixes its top at $24\,\mathrm{V}$.", []),
           (r"Control: $i_x=\dfrac{a}{8}$. KCL at $a$: $\dfrac{a-24}{2}+\dfrac{3a}{8}+4+\dfrac{a}{8}=0$, so $a=8\,\mathrm{V}=V_{\mathrm{Th}}$.", ['a']),
           (r"$8\,\mathrm{A}$ falls into $a$; the diamond lifts $3\,\mathrm{A}$ back up (delivers), the $4\,\mathrm{A}$ pump carries its current **down** (absorbs), $1\,\mathrm{A}$ goes down the $8\,\Omega$.", ['eR1', 'eG1', 'eI1', 'eR2', 'eV1']),
       ]),
       view(off(n) + [IT()], [('V1', 0), ('R1', 1), ('G1', 2), ('I1', 3), ('R2', 4), ('IT', 5)], title='Sources off, push 1 A', names=nm, terminals={'a'},
            elabel={'G1': '$3i_x$'}, disp={'V1': OFFV(24), 'I1': OFFI(4), 'IT': TEST}, steps=[
           (r"Same ground. $24\,\mathrm{V}$ → wire, $4\,\mathrm{A}$ → gap. The diamond **stays on**.", []),
           (r"Push $1\,\mathrm{A}$ into $a$: $1=\dfrac{a}{2}+\dfrac{3a}{8}+\dfrac{a}{8}=a$. So $a=1\,\mathrm{V}$: $R_{\mathrm{Th}}=1\,\Omega$.", ['a', 'eR1', 'eG1', 'eR2', 'eIT', 'eV1']),
           (r"Check with a short: $a=b$ makes $i_x=0$ (diamond off), so $I_N=\dfrac{24}{2}-4=8\,\mathrm{A}$ and $\dfrac{8}{8}=1\,\Omega$ ✓.", []),
       ]),
   ]),
   [S(r'Open, KCL at $a$ with $i_x=\dfrac{v_a}{8}$.', r'\frac{v_a-24}{2}+\frac{3v_a}{8}+4+\frac{v_a}{8}=0\;\Rightarrow\;V_{\mathrm{Th}}=8\,\mathrm{V}'),
    S('Test source, independent sources off.', r'i_T=\frac{v_T}{2}+\frac{3v_T}{8}+\frac{v_T}{8}=v_T\;\Rightarrow\;R_{\mathrm{Th}}=1\,\Omega'),
    S('Check.', r'i_{sc}=\tfrac{24}{2}-4=8\,\mathrm{A},\qquad \tfrac{8}{8}=1\,\Omega')],
   r'**(a)** $8\,\mathrm{V}$ **(b)** $1\,\Omega$ **(c)** $I_N=8\,\mathrm{A}$ ✓', D.oc('Assessment AP 4.19'))
n = C['p480']['net']
PR('p480', 'Try it 2 · No independent source (Textbook P4.80)', 'intermediate',
   r'Find the Thévenin equivalent at $a$–$b$. The dependent source is controlled by $i_\Delta$ in the $12\,\Omega$.',
   fence('p480', [view(n + [IT()], [('E1', 0), ('R1', 1), ('R2', 1), ('R4', 1), ('R3', 2), ('IT', 3)], title='Push 1 A into a',
                       names={'x': '$x$', 'm': '$m$', 'a': '$a$', '0': '$b$'}, terminals={'a'}, elabel={'E1': r'$10i_\Delta$'}, disp={'IT': TEST}, steps=[
       (r"Ground $b$. No independent source, so with nothing attached every height is $0$: $V_{\mathrm{Th}}=0$.", []),
       (r"Push $1\,\mathrm{A}$ into $a$. Control: $i_\Delta=\dfrac{a-m}{12}$, and the diamond holds $x=10i_\Delta$.", ['eIT']),
       (r"KCL at $a$ and $m$: $a=8$, $m=2$, $x=5\,\mathrm{V}$ ($i_\Delta=0.5\,\mathrm{A}$).", ['a', 'm', 'x']),
       (r"Currents = fall ÷ R; the diamond carries $0.2\,\mathrm{A}$ **down** (it absorbs here). $a$ sits at $8\,\mathrm{V}$ per amp: $R_{\mathrm{Th}}=8\,\Omega$.", ['eE1', 'eR1', 'eR2', 'eR3', 'eR4']),
   ])]),
   [S(r'No independent source.', r'V_{\mathrm{Th}}=0'),
    S(r'Test voltage $v_T$ at $a$; $x=10i_\Delta$, $v_m=v_T-12i_\Delta$. KCL at $m$.', r'i_\Delta+\frac{10i_\Delta-v_m}{10}=\frac{v_m}{2.5}\;\Rightarrow\;i_\Delta=\frac{v_T}{16}'),
    S(r'Test current: through the $6\,\Omega$ and the $12\,\Omega$.', r'i_T=\frac{v_T-10i_\Delta}{6}+i_\Delta=\frac{v_T}{8}\;\Rightarrow\;R_{\mathrm{Th}}=8\,\Omega')],
   r'$V_{\mathrm{Th}}=0$, $R_{\mathrm{Th}}=8\,\Omega$: the terminals act like an $8\,\Omega$ resistor.', D.tb('4.80'))

# =========================================================================== Topic 2
H(1, 'Topic 2: Maximum power transfer', D.oc('Topic 2: Maximum power'))
L([r'A load on a Thévenin source sits at height $h$. It gets current $\dfrac{V_{\mathrm{Th}}-h}{R_{\mathrm{Th}}}$, so $p=h\cdot\dfrac{V_{\mathrm{Th}}-h}{R_{\mathrm{Th}}}$.',
   r'$h$ and $V_{\mathrm{Th}}-h$ add to $V_{\mathrm{Th}}$. Their product is largest when they are equal: **$h=\dfrac{V_{\mathrm{Th}}}{2}$**, which happens at $R_L=R_{\mathrm{Th}}$.',
   r'Half of $V_{\mathrm{Th}}$, **not** half of the supply.',
   r'Max power ≠ max efficiency: at the match $R_{\mathrm{Th}}$ burns as much as the load, and the real sources may waste more. For efficiency, go back to the original circuit.',
   r'Load fixed, series $R$ adjustable? That $R$ only steals height: pick $0$.'])
EQ(r'R_L=R_{\mathrm{Th}},\qquad h=\frac{V_{\mathrm{Th}}}{2},\qquad p_{\max}=\frac{V_{\mathrm{Th}}^2}{4R_{\mathrm{Th}}}')
n = C['lec360']['net']
nm = {'s': 'source top', 'a': '$a$', '0': 'ground'}
cols360 = [('V1', 0), ('R1', 1), ('R2', 2), ('R3', 3)]
EX('lec360', 'Half the open height (Lecture 5)',
   r'$R_L$ is adjustable. **(a)** Which $R_L$ gets the most power? **(b)** How much? **(c)** What fraction of the source\'s power reaches $R_L$?',
   fence('lec360', [
       view(n, cols360[:3], title='Open', names=nm, terminals={'a'}, steps=[
           (r"Ground the bottom wire. Open: divider, $a=360\cdot\tfrac{150}{180}=300\,\mathrm{V}=V_{\mathrm{Th}}$. Sources off: $R_{\mathrm{Th}}=30\parallel150=25\,\Omega$.", ['a']),
       ]),
       view(n + [('R', 'R3', 'a', '0', 5)], cols360, title='Load 5 Ω', names=nm,
            notes=[r"Too small: $a$ sits low ($50\,\mathrm{V}$). Load gets $50\times10=500\,\mathrm{W}$."]),
       view(n + [('R', 'R3', 'a', '0', 25)], cols360, title='Load 25 Ω (matched)', names=nm, steps=[
           (r"Same ground. Matched: $a$ sits at half the open height, $150\,\mathrm{V}$.", ['a']),
           (r"Load current $\dfrac{150}{25}=6\,\mathrm{A}$: $p_{\max}=(150)(6)=900\,\mathrm{W}$.", ['eR3']),
           (r"Source: $\dfrac{360-150}{30}=7\,\mathrm{A}$ climbs $360\,\mathrm{V}$: $2520\,\mathrm{W}$. Only $\dfrac{900}{2520}=35.7\%$ reaches the load.", ['eR1', 'eR2', 'eV1']),
       ]),
       view(n + [('R', 'R3', 'a', '0', 100)], cols360, title='Load 100 Ω', names=nm,
            notes=[r"Too big: $a$ sits high ($240\,\mathrm{V}$) but little current. Load gets $240\times2.4=576\,\mathrm{W}$."]),
   ]),
   [S('Thévenin.', r'V_{\mathrm{Th}}=360\cdot\frac{150}{180}=300\,\mathrm{V},\qquad R_{\mathrm{Th}}=30\parallel150=25\,\Omega'),
    S('Match.', r'R_L=25\,\Omega,\qquad p_{\max}=\frac{300^2}{4(25)}=900\,\mathrm{W}'),
    S('Back to the original.', r'v_a=150\,\mathrm{V},\quad i_s=\frac{360-150}{30}=7\,\mathrm{A},\quad \eta=\frac{900}{360(7)}=35.7\%')],
   r'**(a)** $25\,\Omega$ **(b)** $900\,\mathrm{W}$ **(c)** $35.7\%$', D.oc('Lecture example · Maximum power is not'))
n = C['lecmp']['net']
nm = {'a': '$a$', 'm': '$m$', '0': '$b$', 'c': '$c$'}
EX('lecmp', 'Two sources, then match (Lecture 5)',
   r'$R_L$ is adjustable. Find the Thévenin equivalent at $a$–$b$ ($b$ is the bottom wire), then the best $R_L$ and $p_{\max}$.',
   fence('lecmp', [
       view(n, [('R2', 0), ('R1', 1), ('R3', 1), ('V1', 2), ('I1', 3)], title='Open', gnd='low', unit='mA', names=nm, terminals={'a'}, steps=[
           (r"Ground $c$, the lowest node: the $3\,\mathrm{V}$ source hangs it below $b$. Read every answer as a height **above $b$**.", []),
           (r"The pump forces $2\,\mathrm{mA}$ through $R_1$: it falls $8\,\mathrm{V}$.", ['eI1', 'eR1']),
           (r"Lower mesh: $i_2=\dfrac{3(2)-3}{3+6}=\tfrac13\,\mathrm{mA}$ down $R_3$, so $m$ is $2\,\mathrm{V}$ above $b$ and $a$ is $10\,\mathrm{V}$ above: $V_{\mathrm{Th}}=10\,\mathrm{V}$.", ['m', 'a', 'eR2', 'eR3', 'eV1']),
           (r"Sources off: pump → gap, $3\,\mathrm{V}$ → wire, so $R_{\mathrm{Th}}=4+(3\parallel6)=6\,\mathrm{k\Omega}$.", []),
       ]),
       view(n + [('R', 'R4', 'a', '0', 6000)], [('R2', 0), ('R1', 1), ('R3', 1), ('R4', 2), ('V1', 2), ('I1', 3)], title='Matched: 6 kΩ', gnd='low', unit='mA',
            names=nm, steps=[
           (r"Same ground. Matched: $a$ sits $5\,\mathrm{V}$ above $b$, half of $V_{\mathrm{Th}}$.", ['a']),
           (r"The load carries $\dfrac{5}{6}\,\mathrm{mA}$: $p_{\max}=\dfrac{10^2}{4(6000)}=4.17\,\mathrm{mW}$.", ['eR4']),
       ]),
   ]),
   [S(r'Pump fixes mesh 1; KVL on the lower mesh (kΩ, mA).', r'3+3(i_2-2)+6i_2=0\;\Rightarrow\;i_2=\tfrac13\,\mathrm{mA}'),
    S(r'Open height of $a$.', r'V_{\mathrm{Th}}=4(2)+6(\tfrac13)=10\,\mathrm{V}'),
    S('Sources off.', r'R_{\mathrm{Th}}=4+(3\parallel6)=6\,\mathrm{k\Omega}'),
    S('Match.', r'R_L=6\,\mathrm{k\Omega},\qquad p_{\max}=\frac{10^2}{4(6000)}=4.17\,\mathrm{mW}')],
   r'$V_{\mathrm{Th}}=10\,\mathrm{V}$, $R_{\mathrm{Th}}=6\,\mathrm{k\Omega}$; $R_L=6\,\mathrm{k\Omega}$ gets $4.17\,\mathrm{mW}$.', D.oc('Lecture example · Maximum power from'))
nm = {'s': 'source top', 'a': '$a$', '0': 'ground'}
PR('p484', 'Try it 3 · The matching trap (Textbook P4.84)', 'introductory',
   r'**(a)** Which $R_o$ gives the most power in the $6\,\Omega$? (Hint: hasty conclusions could be hazardous to your career.) **(b)** What is that power?',
   fence('p484', [
       view([('V', 'V1', 's', '0', 30), ('R', 'R1', 's', 'a', 6), ('R', 'R2', 'a', '0', 6)], [('V1', 0), ('R1', 1), ('R2', 1)], title='6 Ω (the trap)',
            names=nm, disp={'R1': ('R', r'$R_o=6\,\Omega$: falls $15\,\mathrm{V}$')}, steps=[
           (r"Ground the bottom wire. Matching says $R_o=6\,\Omega$: $a$ sits at $15\,\mathrm{V}$, $p_6=\dfrac{15^2}{6}=37.5\,\mathrm{W}$.", ['a', 'eR1', 'eR2']),
       ]),
       view([('V', 'V1', 's', '0', 30), ('V', 'R1', 's', 'a', 0), ('R', 'R2', 'a', '0', 6)], [('V1', 0), ('R1', 1), ('R2', 2)], title='0 Ω',
            names=nm, disp={'R1': ('W', r'$R_o=0$: no step')}, steps=[
           (r"Same ground. But here the **load is fixed** and $R_o$ is the knob. $R_o$ only steals height, so set it to $0$: $a$ sits at the full $30\,\mathrm{V}$.", ['a']),
           (r"$p_6=\dfrac{30^2}{6}=150\,\mathrm{W}$, four times the trap.", ['eR2', 'eR1']),
       ]),
   ]),
   [S('Write the load power directly.', r'p_6=\Big(\frac{30}{R_o+6}\Big)^2(6)'),
    S(r'It falls as $R_o$ grows: pick the smallest.', r'R_o=0,\qquad p_{\max}=\frac{30^2}{6}=150\,\mathrm{W}')],
   r'**(a)** $R_o=0$ (not $6\,\Omega$) **(b)** $150\,\mathrm{W}$', D.oc('Textbook P4.84'))
n = C['p488']['net']
nm = {'s': 'source top', 'n': '$n$', '0': '$b$', 'a': '$a$', 'k': '$k$'}
c488 = [('V1', 0), ('R1', 1), ('R2', 1), ('E1', 2), ('R3', 4), ('R4', 4)]
PR('p488', 'Try it 4 · Two loads, same power (Textbook P4.88)', 'advanced',
   r'$R_o$ is adjusted until it dissipates $1.5\,\mathrm{W}$. Find **both** values of $R_o$.',
   fence('p488', [
       view(n, c488, title='Open', gnd='low', names=nm, terminals={'a'}, elabel={'E1': '$60i_x$'}, steps=[
           (r"Ground $k$, the lowest node (the diamond hangs it below $b$). Read answers as heights relative to $b$.", []),
           (r"Open: $i_x$ runs through $60+40\,\Omega$ into the diamond. $a=-20i_x$, $n=40i_x$; KCL at $n$: $\dfrac{100-n}{50}=\dfrac{n}{200}+i_x$, so $i_x=1\,\mathrm{A}$.", ['n', 'eR3', 'eR4', 'eE1']),
           (r"$a$ sits $20\,\mathrm{V}$ **below** $b$: $V_{\mathrm{Th}}=-20\,\mathrm{V}$. With a short, $I_N=-0.4\,\mathrm{A}$, so $R_{\mathrm{Th}}=50\,\Omega$.", ['a', 'eR1', 'eR2', 'eV1']),
       ]),
       view(n + [('R', 'R5', 'a', '0', 50 / 3)], c488 + [('R5', 3)], title='16.7 Ω', gnd='low', names=nm, elabel={'E1': '$60i_x$'}, steps=[
           (r"Same ground. Let the load's fall be $h$: $p=h\cdot\dfrac{20-h}{50}=1.5$, so $h^2-20h+75=0$: $h=5$ or $15\,\mathrm{V}$.", []),
           (r"$h=5\,\mathrm{V}$: current $\dfrac{20-5}{50}=0.3\,\mathrm{A}$, so $R_o=\dfrac{5}{0.3}=16.7\,\Omega$.", ['a', 'eR5']),
       ]),
       view(n + [('R', 'R5', 'a', '0', 150)], c488 + [('R5', 3)], title='150 Ω', gnd='low', names=nm, elabel={'E1': '$60i_x$'}, steps=[
           (r"Same ground ($k$). $h=15\,\mathrm{V}$: current $\dfrac{5}{50}=0.1\,\mathrm{A}$, so $R_o=150\,\Omega$.", ['a', 'eR5']),
       ], notes=[r"The two loads fall $5$ and $15\,\mathrm{V}$: mirror images around half of $|V_{\mathrm{Th}}|=10\,\mathrm{V}$, where the power would peak ($2\,\mathrm{W}$)."]),
   ]),
   [S(r'Open circuit ($i_x$ through $60+40\,\Omega$ and the diamond).', r'\begin{aligned}&v_a=-20i_x,\quad v_n=40i_x,\quad \frac{100-v_n}{50}=\frac{v_n}{200}+i_x\\&\Rightarrow\;i_x=1\,\mathrm{A},\quad V_{\mathrm{Th}}=-20\,\mathrm{V}\end{aligned}'),
    S(r'Short circuit gives $I_N=-0.4\,\mathrm{A}$.', r'R_{\mathrm{Th}}=\frac{-20}{-0.4}=50\,\Omega'),
    S('Power equation.', r'\Big(\frac{20}{50+R_o}\Big)^2R_o=1.5\;\Rightarrow\;3R_o^2-500R_o+7500=0'),
    S('Two roots.', r'R_o=\frac{500\pm400}{6}=150\,\Omega\;\text{ or }\;16.7\,\Omega')],
   r'$R_o=16.7\,\Omega$ or $R_o=150\,\Omega$.', D.tb('4.88'))

# =========================================================================== Topic 3
H(1, 'Topic 3: Superposition', D.oc('Topic 3: Superposition'))
L(['Linear circuit: every voltage and current = the sum of what each **independent** source makes alone.',
   'One picture per source. Other voltage sources → wires; other current sources → gaps (left out of the pictures below). **Dependent sources stay on.**',
   r'**Add voltages (height differences) and currents. Never powers:** $p$ is current × fall, a product. Compute it once from the sums.',
   'Keep the same reference directions in every picture. A partial picture may run a resistor "backwards"; only the sum must run downhill.',
   'Worth it when each one-source picture is a divider or a series–parallel reduction.'])
EQ(r'y=y_1+y_2+\cdots,\qquad p=(v_1+v_2)(i_1+i_2)\neq p_1+p_2')
n = C['lecsup']['net']
nm = {'s': '$s$', 'n1': 'node 1', 'n2': 'node 2', '0': 'bottom'}
EX('lecsup', 'One source at a time (Lecture 5)',
   r'Use superposition to find $v_o$ and $i_o$.',
   fence('lecsup', [
       view(drop(n, 'I1'), [('V1', 0), ('R1', 1), ('R3', 2), ('R2', 3), ('R4', 3)], title='120 V alone', names=nm, refs={'R4': ('n2', '$v_o$')}, steps=[
           (r"Ground the bottom wire. The $12\,\mathrm{A}$ pump is off (a gap).", []),
           (r"$2+4=6\,\Omega$ beside $3\,\Omega$: $2\,\Omega$; plus $6\,\Omega$: $8\,\Omega$. So $15\,\mathrm{A}$, and node 1 sits at $30\,\mathrm{V}$.", ['n1', 'eR1', 'eV1']),
           (r"$i_o'=\dfrac{30}{3}=10\,\mathrm{A}$; divider on the right: $v_o'=30\cdot\tfrac46=20\,\mathrm{V}$.", ['n2', 'eR2', 'eR3', 'eR4']),
       ]),
       view(off(n, keep=('I1',)), [('V1', 0), ('R1', 0), ('R3', 1), ('R2', 2), ('R4', 3), ('I1', 4)], title='12 A alone', gnd='low', names=nm,
            refs={'R4': ('n2', '$v_o$')}, disp={'V1': OFFV(120)}, steps=[
           (r"Ground node 2, the lowest: the pump drags $12\,\mathrm{A}$ out of it. The $120\,\mathrm{V}$ step flattens to a wire.", []),
           (r"From node 2: $4\,\Omega$ beside $2+(6\parallel3)=4\,\Omega$, so $2\,\Omega$. Node 2 sits $24\,\mathrm{V}$ below the bottom wire: $v_o''=-24\,\mathrm{V}$.", ['z0', 'eR4', 'eI1']),
           (r"Node 1 sits halfway: $v_1''=-12\,\mathrm{V}$, so $i_o''=\dfrac{-12}{3}=-4\,\mathrm{A}$ (it flows **up** the $3\,\Omega$).", ['n1', 'eR1', 'eR2', 'eR3', 'eV1']),
       ]),
       view(n, [('V1', 0), ('R1', 1), ('R3', 2), ('R4', 3), ('I1', 4), ('R2', 5)], title='Both: add', gnd='low', names=nm, refs={'R4': ('n2', '$v_o$')}, steps=[
           (r"Ground node 2 again. Add the voltages: $v_o=20-24=-4\,\mathrm{V}$, $i_o=10-4=6\,\mathrm{A}$.", ['z0', 'n1', 's']),
           (r"Check: the $3\,\Omega$ falls $18\,\mathrm{V}$ ($6\,\mathrm{A}$) ✓. The $4\,\Omega$ absorbs $\dfrac{4^2}{4}=4\,\mathrm{W}$, not $100+144$.", ['eR1', 'eR2', 'eR3', 'eR4', 'eV1', 'eI1']),
       ]),
   ]),
   [S(r'$120\,\mathrm{V}$ alone (pump open).', r'i_s=\frac{120}{6+(3\parallel6)}=15\,\mathrm{A},\quad v_1\'=30,\quad i_o\'=10\,\mathrm{A},\quad v_o\'=20\,\mathrm{V}'),
    S(r'$12\,\mathrm{A}$ alone (source shorted).', r'v_o\'\'=-12\,(4\parallel4)=-24\,\mathrm{V},\quad v_1\'\'=-12,\quad i_o\'\'=-4\,\mathrm{A}'),
    S('Add.', r'v_o=20-24=-4\,\mathrm{V},\qquad i_o=10-4=6\,\mathrm{A}')],
   r'$v_o=-4\,\mathrm{V}$, $i_o=6\,\mathrm{A}$.', D.oc('Lecture example · Superposition with two'))
n = C['lecsupd']['net']
nm = {'s': '$s$', 'a': '$a$', 'd': '$d$', 'c': '$c$', '0': 'bottom'}
el = {'G1': r'$0.4v_\Delta$', 'E1': r'$2i_\Delta$'}
EX('lecsupd', 'Dependent sources stay on (Lecture 5)',
   r'Use superposition on the two independent sources to find $v_o$. The pump is $0.4v_\Delta$ (A/V) and the rod is $2i_\Delta$ (Ω).',
   fence('lecsupd', [
       view(drop(n, 'I1'), [('V1', 0), ('R1', 1), ('R2', 1), ('G1', 2), ('R3', 3), ('E1', 4)], title='10 V alone', names=nm, elabel=el,
            refs={'R2': ('a', '$v_o$'), 'R3': ('d', r'$v_\Delta$')}, steps=[
           (r"Ground the bottom wire. The $5\,\mathrm{A}$ pump is off (a gap); both diamonds stay on.", []),
           (r"KCL at $d$: nothing comes in, so $0.4v_\Delta'+\dfrac{v_\Delta'}{10}=0$: $v_\Delta'=0$. The diamond pump is off **because its control is zero**.", ['eG1', 'eR3']),
           (r"The left side is a plain divider: $v_o'=10\cdot\tfrac{20}{25}=8\,\mathrm{V}$. ($i_\Delta=0.4\,\mathrm{A}$, so the rod still lifts $c$ and $d$ to $0.8\,\mathrm{V}$.)", ['a', 'c', 'd', 'eR1', 'eR2', 'eE1']),
       ]),
       view(off(n, keep=('I1',)), [('R1', 0), ('V1', 0), ('R2', 1), ('G1', 2), ('R3', 3), ('I1', 4), ('E1', 5)], title='5 A alone', gnd='low', names=nm, elabel=el,
            refs={'R2': ('a', '$v_o$'), 'R3': ('d', r'$v_\Delta$')}, disp={'V1': OFFV(10)}, steps=[
           (r"Ground $c$, the lowest node; $v_o$ is $a$'s height minus the bottom wire's. The $10\,\mathrm{V}$ step flattens to a wire.", []),
           (r"KCL at $d$: $5=0.4v_\Delta''+\dfrac{v_\Delta''}{10}$, so $v_\Delta''=10\,\mathrm{V}$ and the diamond pushes $4\,\mathrm{A}$ into $a$.", ['d', 'eG1', 'eR3', 'eI1']),
           (r"$a$ sees $5\parallel20=4\,\Omega$ down to the bottom wire: $v_o''=(4)(4)=16\,\mathrm{V}$.", ['a', 'eR1', 'eR2', 'eV1', 'eE1']),
       ]),
       view(n, [('R1', 0), ('V1', 0), ('E1', 0), ('R2', 1), ('G1', 2), ('R3', 3), ('I1', 4)], title='Both: add', gnd='low', names=nm, elabel=el,
            refs={'R2': ('a', '$v_o$'), 'R3': ('d', r'$v_\Delta$')}, steps=[
           (r"Ground $c$. Add: $v_o=8+16=24\,\mathrm{V}$: $a$ sits $24\,\mathrm{V}$ above the bottom wire ✓.", ['a', 's', 'z0']),
       ]),
   ]),
   [S(r'$10\,\mathrm{V}$ alone: KCL at $d$ forces $v_\Delta\'=0$; divider on the left.', r'v_o\'=10\cdot\frac{20}{25}=8\,\mathrm{V}'),
    S(r'$5\,\mathrm{A}$ alone: KCL at $d$, then $a$.', r'5=0.4v_\Delta\'\'+\frac{v_\Delta\'\'}{10}\Rightarrow v_\Delta\'\'=10,\quad v_o\'\'=4\,(5\parallel20)=16\,\mathrm{V}'),
    S('Add.', r'v_o=8+16=24\,\mathrm{V}')],
   r'$v_o=24\,\mathrm{V}$', D.oc('Lecture example · Superposition with dep'))
n = C['p494']['net']
nm = {'p': '$p$', 'q': '$q$', 'k': '$k$', '0': 'bottom'}
PR('p494', 'Try it 5 · Three sources (Textbook P4.94)', 'intermediate',
   r'Use superposition to find $i_o$.',
   fence('p494', [
       view(alone(n, 'I1'), [('I1', 0), ('R1', 1), ('R2', 2), ('R3', 3), ('R4', 4), ('V1', 4), ('R5', 5)], title='6 A alone', gnd='low', names=nm, disp={'V1': OFFV(75)}, steps=[
           (r"Ground the bottom wire. $10\,\mathrm{A}$ off (gap), $75\,\mathrm{V}$ → wire. Right side: $60\parallel5\parallel30=4\,\Omega$.", []),
           (r"Divider of currents: $20\,\Omega$ vs $1+4=5\,\Omega$. $i_o'=6\cdot\tfrac{20}{25}=4.8\,\mathrm{A}$.", ['eR2', 'p', 'q', 'eR1', 'eR3', 'eR4', 'eR5', 'eV1']),
       ]),
       view(alone(n, 'I2'), [('R1', 0), ('R2', 0), ('I2', 1), ('R3', 2), ('R4', 3), ('V1', 3), ('R5', 4)], title='10 A alone', gnd='low', names=nm, disp={'V1': OFFV(75)}, steps=[
           (r"Ground $q$, the lowest: the pump drags $10\,\mathrm{A}$ out of it. Its $10\,\mathrm{A}$ comes back via $4\,\Omega$ (right) or $1+20=21\,\Omega$ (left).", []),
           (r"Left share: $10\cdot\tfrac{4}{25}=1.6\,\mathrm{A}$, falling $p\to q$ through the $1\,\Omega$: $i_o''=+1.6\,\mathrm{A}$.", ['eR2', 'p', 'eR1', 'eR3', 'eR4', 'eR5', 'eV1']),
       ]),
       view(alone(n, 'V1'), [('V1', 0), ('R4', 1), ('R2', 1), ('R1', 1), ('R3', 2), ('R5', 3)], title='75 V alone', gnd='low', names=nm, steps=[
           (r"Ground the bottom wire; both pumps off. Node $q$: $\dfrac{q-75}{5}+\dfrac{q}{60}+\dfrac{q}{30}+\dfrac{q}{21}=0$, so $q=50.4\,\mathrm{V}$.", ['q']),
           (r"Current runs $q\to p$ through $1+20\,\Omega$: $\dfrac{50.4}{21}=2.4\,\mathrm{A}$, against $i_o$: $i_o'''=-2.4\,\mathrm{A}$.", ['p', 'eR1', 'eR2', 'eR3', 'eR4', 'eR5']),
       ]),
       view(n, [('V1', 0), ('R4', 1), ('R5', 1), ('I1', 2), ('R2', 3), ('R3', 3), ('R1', 4), ('I2', 5)], title='All three: add', gnd='low', names=nm, steps=[
           (r"Ground the bottom wire. Add: $i_o=4.8+1.6-2.4=4\,\mathrm{A}$. Check: $p=40$, $q=36\,\mathrm{V}$, the $1\,\Omega$ falls $4\,\mathrm{V}$ ✓.", ['p', 'q', 'eR2']),
       ]),
   ]),
   [S(r'$6\,\mathrm{A}$ alone.', r'i_o\'=6\cdot\frac{20}{20+(1+4)}=4.8\,\mathrm{A}'),
    S(r'$10\,\mathrm{A}$ alone.', r'i_o\'\'=10\cdot\frac{4}{4+21}=1.6\,\mathrm{A}'),
    S(r'$75\,\mathrm{V}$ alone.', r'\frac{v-75}{5}+\frac{v}{60}+\frac{v}{30}+\frac{v}{21}=0\Rightarrow v=50.4,\;\;i_o\'\'\'=-\frac{50.4}{21}=-2.4\,\mathrm{A}'),
    S('Add.', r'i_o=4.8+1.6-2.4=4\,\mathrm{A}')],
   r'$i_o=4\,\mathrm{A}$ ($4.8$, $1.6$, $-2.4$).', D.tb('4.94'))
n = C['p496']['net']
nm = {'a': '$a$', 'b': '$b$', '0': 'bottom'}
PR('p496', 'Try it 6 · Adding one more source (Textbook P4.96)', 'intermediate',
   r'Before the $5\,\mathrm{mA}$ source is attached between $a$ and $b$, $i_o=3.5\,\mathrm{mA}$. **(a)** Use superposition to find $i_o$ after it is attached. **(b)** Check with all three sources on.',
   fence('p496', [
       view(drop(n, 'I2'), [('V1', 0), ('R1', 1), ('R2', 2), ('R3', 3), ('I1', 4)], title='Before: 8 V and 10 mA', unit='mA', names=nm, steps=[
           (r"Ground the bottom wire. The $8\,\mathrm{V}$ source fixes $a=8\,\mathrm{V}$.", []),
           (r"KCL at $b$: $\dfrac{b-8}{2}+\dfrac{b}{6}=10$, so $b=21\,\mathrm{V}$ and $i_o=\dfrac{21}{6}=3.5\,\mathrm{mA}$ ✓ (given).", ['b', 'eR2', 'eR3', 'eI1']),
       ]),
       view(drop(off(n, keep=('I2',)), 'R1', 'I1'), [('I2', 0), ('R2', 1), ('V1', 1), ('R3', 2)], title='5 mA alone', gnd='low', unit='mA', names=nm,
            disp={'V1': OFFV(8)}, notes=[r"$8\,\mathrm{V}$ → wire, so the $5\,\mathrm{k\Omega}$ has no fall (left out); $10\,\mathrm{mA}$ → gap."], steps=[
           (r"Ground $b$, the lowest: the new pump moves $5\,\mathrm{mA}$ from $b$ to $a$.", []),
           (r"From $b$ the pump sees $2\parallel6=1.5\,\mathrm{k\Omega}$: $b$ sits $7.5\,\mathrm{V}$ below the bottom wire, so $i_o''=-\dfrac{7.5}{6}=-1.25\,\mathrm{mA}$.", ['a', 'z0', 'eR2', 'eR3', 'eV1']),
       ]),
       view(n, [('V1', 0), ('R1', 1), ('R2', 2), ('I2', 3), ('R3', 4), ('I1', 5)], title='All three', unit='mA', names=nm, steps=[
           (r"Ground the bottom wire. Add: $i_o=3.5-1.25=2.25\,\mathrm{mA}$. Check: $b=13.5\,\mathrm{V}$, $\dfrac{13.5}{6}=2.25\,\mathrm{mA}$ ✓. The new pump carries its current **down** from $b$ to $a$: it absorbs.", ['b', 'eR3', 'eR2', 'eI2']),
       ]),
   ]),
   [S(r'The new source alone ($8\,\mathrm{V}$ shorted, $10\,\mathrm{mA}$ open).', r'i_o\'\'=-5\cdot\frac{2}{2+6}=-1.25\,\mathrm{mA}'),
    S('Add to the old answer.', r'i_o=3.5-1.25=2.25\,\mathrm{mA}'),
    S(r'Check: KCL at $b$ with all three.', r'\frac{v_b-8}{2}+\frac{v_b}{6}+5=10\;\Rightarrow\;v_b=13.5\,\mathrm{V},\;\;i_o=2.25\,\mathrm{mA}')],
   r'$i_o=2.25\,\mathrm{mA}$', D.tb('4.96'))

# =========================================================================== Practice
H(1, 'Practice problems')
P('Exam-style, each mixing topics. Give each a real try before opening the solution, then check your picture against the height view.')
n = C['ap416']['net']
nm = {'s': 'source top', 'n': '$v_1$', 'a': '$a$', '0': '$b$'}
PR('ap416', 'Assessment AP 4.16 · Thévenin with a bypass', 'intermediate',
   r'Find the Thévenin equivalent at $a$–$b$.',
   fence('ap416', [
       view(n, [('V1', 0), ('R1', 1), ('R2', 1), ('R4', 2), ('R3', 3)], title='Open', names=nm, terminals={'a'}, steps=[
           (r"Ground $b$. The source fixes its top at $72\,\mathrm{V}$.", []),
           (r"Two unknowns, $v_1$ and $a$. KCL: $\dfrac{v_1-72}{5}+\dfrac{v_1}{20}+\dfrac{v_1-a}{8}=0$ and $\dfrac{a-v_1}{8}+\dfrac{a-72}{12}=0$. So $v_1=60$, $a=64.8\,\mathrm{V}=V_{\mathrm{Th}}$.", ['n', 'a']),
           (r"$0.6\,\mathrm{A}$ comes down the $12\,\Omega$ bypass and falls on through the $8\,\Omega$ to $v_1$.", ['eR1', 'eR2', 'eR3', 'eR4', 'eV1']),
       ]),
       view(off(n) + [IT()], [('R4', 0), ('V1', 0), ('R3', 1), ('R1', 2), ('R2', 3), ('IT', 4)], title='Sources off, push 1 A', names=nm, terminals={'a'},
            disp={'V1': OFFV(72), 'IT': TEST}, steps=[
           (r"Same ground; $72\,\mathrm{V}$ → wire. Push $1\,\mathrm{A}$ into $a$: $12\,\Omega$ straight down, or $8+(5\parallel20)=12\,\Omega$. Half each.", ['eR3', 'eR4', 'eR1', 'eR2', 'eV1']),
           (r"$a=(0.5)(12)=6\,\mathrm{V}$: $R_{\mathrm{Th}}=6\,\Omega$.", ['a', 'n', 'eIT']),
       ]),
   ]),
   [S('Sources off.', r'R_{\mathrm{Th}}=12\parallel\big((5\parallel20)+8\big)=12\parallel12=6\,\mathrm{\Omega}'),
    S('Open: KCL at $v_1$ and $a$.', r'\begin{aligned}\tfrac{v_1-72}{5}+\tfrac{v_1}{20}+\tfrac{v_1-v_a}{8}&=0\\\tfrac{v_a-v_1}{8}+\tfrac{v_a-72}{12}&=0\end{aligned}'),
    S('Solve.', r'v_1=60\,\mathrm{V},\qquad V_{\mathrm{Th}}=v_a=64.8\,\mathrm{V}')],
   r'$V_{\mathrm{Th}}=64.8\,\mathrm{V}$, $R_{\mathrm{Th}}=6\,\Omega$', D.oc('Assessment AP 4.16'))
n = C['p493']['net']
nm = {'p': '$p$', 'm': '$m$', 'n': '$n$', 'k': '$k$', 'r': '$r$', '0': 'bottom'}
PR('p493', 'Textbook P4.93 · A hidden balanced bridge', 'advanced',
   r'Use superposition to find $i_o$, the current in the $45\,\mathrm{V}$ source.',
   fence('p493', [
       view(alone(n, 'V1'), [('V1', 0), ('R1', 1), ('R2', 1), ('V2', 2), ('R5', 4), ('R4', 4), ('R3', 5)], title='45 V alone', gnd='low', names=nm,
            disp={'V2': OFFV(10)}, steps=[
           (r"Ground the bottom-left wire. $10\,\mathrm{V}$ → wire, $8\,\mathrm{A}$ → gap.", []),
           (r"$10+30=40\,\Omega$ beside $40\,\Omega$: $20\,\Omega$; plus $5+15$: $40\,\Omega$. So $i_o'=\dfrac{45}{40}=1.125\,\mathrm{A}$.", ['m', 'n', 'r', 'k', 'eV1', 'eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eV2']),
       ]),
       view(alone(n, 'V2'), [('V2', 0), ('R2', 1), ('R1', 1), ('V1', 2), ('R4', 4), ('R5', 4), ('R3', 5)], title='10 V alone', gnd='low', names=nm,
            disp={'V1': OFFV(45)}, steps=[
           (r"Ground $r$, the lowest. $45\,\mathrm{V}$ → wire, $8\,\mathrm{A}$ → gap.", []),
           (r"The $10\,\mathrm{V}$ source sees $10+\big(40\parallel(5+15)\big)+30=53.3\,\Omega$: $0.1875\,\mathrm{A}$. Its share through the $5\,\Omega$, $0.125\,\mathrm{A}$, flows **down** the shorted $45\,\mathrm{V}$ spot: $i_o''=-0.125\,\mathrm{A}$.", ['m', 'k', 'p', 'eV2', 'eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eV1']),
       ]),
       view(alone(n, 'I1'), [('R1', 1), ('R2', 1), ('R4', 2), ('R5', 2), ('V1', 1), ('R3', 1), ('V2', 1), ('I1', 3)], title='8 A alone', gnd='r', names=nm,
            disp={'V1': OFFV(45), 'V2': OFFV(10)}, steps=[
           (r"Ground $r$ (and $n$: the $10\,\mathrm{V}$ is now a wire). Both voltage sources flatten.", []),
           (r"Bridge check: $\dfrac{10}{5}=\dfrac{30}{15}$, so $m$ and $k$ sit at **one height**: the $40\,\Omega$ lies flat, no current.", ['m', 'k', 'eR3']),
           (r"The $8\,\mathrm{A}$ splits: $5+10=15\,\Omega$ vs $15+30=45\,\Omega$: $6\,\mathrm{A}$ and $2\,\mathrm{A}$. The $6\,\mathrm{A}$ comes up through the $45\,\mathrm{V}$ spot: $i_o'''=6\,\mathrm{A}$.", ['p', 'eR1', 'eR2', 'eR4', 'eR5', 'eV1', 'eV2']),
       ]),
       view(n, [('V1', 0), ('I1', 1), ('R4', 2), ('R5', 2), ('R3', 3), ('R1', 4), ('R2', 4), ('V2', 4)], title='All three: add', gnd='low', names=nm, steps=[
           (r"Ground $r$ again (the lowest). Add: $i_o=1.125-0.125+6=7\,\mathrm{A}$, climbing through the $45\,\mathrm{V}$ source.", ['eV1']),
       ]),
   ]),
   [S(r'$45\,\mathrm{V}$ alone.', r'i_o\'=\frac{45}{5+(40\parallel40)+15}=1.125\,\mathrm{A}'),
    S(r'$10\,\mathrm{V}$ alone.', r'i_{10}=\frac{10}{53.33}=0.1875\,\mathrm{A},\quad i_o\'\'=-0.1875\cdot\frac{40}{60}=-0.125\,\mathrm{A}'),
    S(r'$8\,\mathrm{A}$ alone: balanced bridge ($\tfrac{10}{5}=\tfrac{30}{15}$), no current in the $40\,\Omega$.', r'i_o\'\'\'=8\cdot\frac{45}{15+45}=6\,\mathrm{A}'),
    S('Add.', r'i_o=1.125-0.125+6=7\,\mathrm{A}')],
   r'$i_o=7\,\mathrm{A}$ ($1.125$, $-0.125$, $6$).', D.tb('4.93'))
n = C['ap421']['net']
nm = {'t': 'diamond +', 'a': '$a$', 's': '100 V top', 'c': '$c$', 'd': '20 V top', '0': '$b$'}
PR('ap421', 'Assessment AP 4.21 + P4.86 · Matched, and how efficient?', 'advanced',
   r'$R_o$ is set for maximum power; $v_\phi$ is the voltage across the $4\,\Omega$ in series with the $20\,\mathrm{V}$ source. **(a)** Find $R_o$. **(b)** Find $p_{\max}$. **(c)** (P4.86) What percentage of the power developed reaches $R_o$?',
   fence('ap421', [
       view(n, [('V1', 0), ('E1', 0), ('R1', 1), ('R4', 2), ('R2', 2), ('R3', 3), ('V2', 3)], title='Open', names=nm, terminals={'a'},
            elabel={'E1': r'$v_\phi$'}, refs={'R3': ('c', r'$v_\phi$')}, steps=[
           (r"Ground $b$. The source fixes $100\,\mathrm{V}$; the rod $v_\phi=c-20$ puts the diamond's top at $80+c$.", []),
           (r"Open: KCL at $a$ gives $a=40+c$; KCL at $c$ gives $c=80$. So $a=120\,\mathrm{V}=V_{\mathrm{Th}}$.", ['c', 'a', 't']),
           (r"Currents = fall ÷ R. The $20\,\mathrm{V}$ source carries $15\,\mathrm{A}$ **down**: it absorbs.", ['eR1', 'eR2', 'eR3', 'eR4', 'eV1', 'eV2', 'eE1']),
       ]),
       view(drop(n) + [SC()], [('V1', 0), ('E1', 0), ('R1', 1), ('R2', 2), ('R3', 3), ('V2', 3), ('R4', 4), ('SC', 4)], title='Short', names=nm,
            elabel={'E1': r'$v_\phi$'}, refs={'R3': ('c', r'$v_\phi$')}, disp={'SC': SHORT}, steps=[
           (r"Same ground; $a$ pinned to $b$. KCL at $c$: $c=40\,\mathrm{V}$, so the diamond's top is $120\,\mathrm{V}$.", ['c', 't']),
           (r"Into the short: $\dfrac{120}{4}+\dfrac{40}{4}=40\,\mathrm{A}=I_N$. So $R_{\mathrm{Th}}=\dfrac{120}{40}=3\,\Omega$.", ['eR4', 'eR2', 'eSC', 'eR1', 'eR3', 'eV1', 'eV2', 'eE1']),
       ]),
       view(n + [('R', 'R5', 'a', '0', 3)], [('V1', 0), ('E1', 0), ('R1', 1), ('R3', 1), ('V2', 1), ('R2', 1), ('R4', 2), ('R5', 2)], title='Matched: 3 Ω',
            names=nm, elabel={'E1': r'$v_\phi$'}, refs={'R3': ('c', r'$v_\phi$')}, steps=[
           (r"Same ground. Matched: $a$ sits at half the open height, $60\,\mathrm{V}$. $p_{\max}=\dfrac{60^2}{3}=1200\,\mathrm{W}$.", ['a', 'eR5']),
           (r"Note $c$ is also $60\,\mathrm{V}$: the $4\,\Omega$ between $c$ and $a$ lies flat.", ['c', 't', 'eR2']),
           (r"Climbs: the $100\,\mathrm{V}$ source lifts $30\,\mathrm{A}$ ($3000\,\mathrm{W}$), the diamond $20\,\mathrm{A}$ through $40\,\mathrm{V}$ ($800\,\mathrm{W}$). The $20\,\mathrm{V}$ source absorbs $200\,\mathrm{W}$. Load share: $\dfrac{1200}{3800}=31.6\%$.", ['eR1', 'eR3', 'eR4', 'eV1', 'eV2', 'eE1']),
       ]),
   ]),
   [S(r'Open: $v_\phi=v_c-20$, diamond top $=80+v_c$; KCL at $a$, then $c$.', r'v_a=40+v_c,\qquad v_c=80\;\Rightarrow\;V_{\mathrm{Th}}=120\,\mathrm{V}'),
    S(r'Short: KCL at $c$.', r'v_c=40\,\mathrm{V},\qquad I_N=\frac{120}{4}+\frac{40}{4}=40\,\mathrm{A}'),
    S('Match.', r'R_o=R_{\mathrm{Th}}=\frac{120}{40}=3\,\Omega,\qquad p_{\max}=\frac{120^2}{4(3)}=1200\,\mathrm{W}'),
    S(r'Back to the original with $R_o=3\,\Omega$.', r'\eta=\frac{1200}{100(30)+40(20)}=\frac{1200}{3800}=31.6\%')],
   r'**(a)** $3\,\Omega$ **(b)** $1200\,\mathrm{W}$ **(c)** $31.6\%$', D.oc('Assessment AP 4.21') + D.tb('4.86'))

# =========================================================================== Summary
H(1, 'Summary: Week 5 in one read')
CO('tip', r"Same picture: **voltage is height**, and every circuit seen from $a$–$b$ is one step plus one slope.")
H(2, 'A · Dependent sources: use a test source')
L([r'Independent sources off, dependent sources **on**. Push $1\,\mathrm{A}$ in: $a$\'s height $=R_{\mathrm{Th}}$.',
   r'No independent source → $V_{\mathrm{Th}}=0$. $a$ rises when you pull current out → $R_{\mathrm{Th}}<0$.'])
n = C['w5A']['net']
EX('w5A', 'A1 · A diamond lowers the climb', r'Find $R_{\mathrm{Th}}$ at $a$–$b$. The diamond draws $\tfrac{v}{3}$ from $a$ to $b$.',
   fence('w5A', [view(n + [IT()], [('IT', 0), ('R1', 1), ('G1', 2)], title='Push 1 A', names={'a': '$a$', '0': '$b$'}, terminals={'a'},
                      elabel={'G1': r'$\tfrac{v}{3}$'}, refs={'R1': ('a', '$v$')}, disp={'IT': TEST}, steps=[
       (r"Ground $b$, push $1\,\mathrm{A}$ in. KCL: $1=\dfrac{a}{6}+\dfrac{a}{3}=\dfrac{a}{2}$, so $a=2\,\mathrm{V}$: $R_{\mathrm{Th}}=2\,\Omega$, not $6$.", ['a', 'eR1', 'eG1']),
   ])], spoiler=False, inline=True),
   [S('Test current.', r'1=\frac{v}{6}+\frac{v}{3}\;\Rightarrow\;v=2\,\mathrm{V},\quad R_{\mathrm{Th}}=2\,\Omega')], r'$R_{\mathrm{Th}}=2\,\Omega$')
H(2, 'B · Maximum power: half height')
L([r'Best load sits at $\dfrac{V_{\mathrm{Th}}}{2}$ ($R_L=R_{\mathrm{Th}}$): $p_{\max}=\dfrac{V_{\mathrm{Th}}^2}{4R_{\mathrm{Th}}}$.',
   r'Two loads with the same power sit at mirror heights around $\dfrac{V_{\mathrm{Th}}}{2}$.'])
th = lambda rl: [('V', 'V1', 't', '0', 20), ('R', 'R1', 't', 'a', 5), ('R', 'RL', 'a', '0', rl)]  # noqa: E731
nm = {'t': 'top', 'a': '$a$', '0': '$b$'}
dth = {'V1': ('V', r'$V_{\mathrm{Th}}$: $20\,\mathrm{V}$')}
EX('w5B', 'B1 · Matched vs not', r'$V_{\mathrm{Th}}=20\,\mathrm{V}$, $R_{\mathrm{Th}}=5\,\Omega$. Compare $R_L=5$, $20$ and $1.25\,\Omega$.',
   fence('w5B', [
       view(th(5), [('V1', 0), ('R1', 1), ('RL', 1)], title='Load 5 Ω (matched)', names=nm, disp=dth, steps=[
           (r"Ground $b$. $a$ at half height, $10\,\mathrm{V}$; $2\,\mathrm{A}$; $p=20\,\mathrm{W}$ (the most).", ['a', 'eRL']),
       ]),
       view(th(20), [('V1', 0), ('R1', 1), ('RL', 1)], title='Load 20 Ω', names=nm, disp=dth, notes=[r"$a=16\,\mathrm{V}$, $0.8\,\mathrm{A}$: $12.8\,\mathrm{W}$."]),
       view(th(1.25), [('V1', 0), ('R1', 1), ('RL', 1)], title='Load 1.25 Ω', names=nm, disp=dth, notes=[r"$a=4\,\mathrm{V}$, $3.2\,\mathrm{A}$: also $12.8\,\mathrm{W}$. $4$ and $16$ mirror around $10$."]),
   ], spoiler=False, inline=True),
   [S('Power at height $h$.', r'p=h\cdot\frac{20-h}{5}:\quad h=10\to20\,\mathrm{W},\quad h=4\text{ or }16\to12.8\,\mathrm{W}')],
   r'Matched: $20\,\mathrm{W}$; the other two: $12.8\,\mathrm{W}$ each.')
H(2, 'C · Superposition: add heights, not powers')
L(['One picture per independent source (others: V → wire, I → gap). Dependent sources stay on.',
   'Add voltages and currents; compute power once, from the sums.'])
n = C['w5C']['net']
nm = {'t': 'source top', 'm': '$m$', '0': 'ground'}
EX('w5C', 'C1 · Two pictures, one sum', r'Find the height of $m$ by superposition.',
   fence('w5C', [
       view(drop(n, 'I1'), [('V1', 0), ('R1', 1), ('R2', 1)], title='12 V alone', names=nm, steps=[
           (r"Ground the bottom wire. Pump off: a divider, $m'=6\,\mathrm{V}$.", ['m', 'eR1', 'eR2']),
       ]),
       view(off(n, keep=('I1',)), [('V1', 0), ('R1', 1), ('R2', 2), ('I1', 3)], title='2 A alone', names=nm, disp={'V1': OFFV(12)}, steps=[
           (r"Same ground. $12\,\mathrm{V}$ → wire. $2\,\mathrm{A}$ into $4\parallel4=2\,\Omega$: $m''=4\,\mathrm{V}$.", ['m', 'eR1', 'eR2']),
       ]),
       view(n, [('V1', 0), ('R1', 1), ('R2', 1), ('I1', 2)], title='Both: add', names=nm, steps=[
           (r"Same ground. $m=6+4=10\,\mathrm{V}$. Power in the lower $4\,\Omega$: $\dfrac{10^2}{4}=25\,\mathrm{W}$, not $9+4$.", ['m', 'eR1', 'eR2']),
       ]),
   ], spoiler=False, inline=True),
   [S('Add the heights.', r'm=6+4=10\,\mathrm{V},\qquad p_{4\Omega}=\frac{10^2}{4}=25\,\mathrm{W}\neq9+4')], r'$m=10\,\mathrm{V}$')
H(2, 'Which part do I need? (practice problem map)')
T(['Problem', 'Use', 'First move'], [
    ['Try its 1–2 · AP 4.19, P4.80', 'A', r'Keep the diamond; push $1\,\mathrm{A}$ into $a$.'],
    ['Try its 3–4 · P4.84, P4.88', 'B', r'Fixed load → series $R=0$. Fixed power → $h(V_{\mathrm{Th}}-h)=pR_{\mathrm{Th}}$.'],
    ['Try its 5–6 · P4.94, P4.96', 'C', 'One picture per source; add.'],
    ['AP 4.16 · Thévenin with a bypass', 'Week 4 + A', r'Two KCLs for $V_{\mathrm{Th}}$; sources off for $R_{\mathrm{Th}}$.'],
    ['P4.93 · A hidden balanced bridge', 'C', r'In the $8\,\mathrm{A}$ picture, check the bridge ratio first.'],
    ['AP 4.21 + P4.86 · Matched, how efficient?', 'A, B', r'$V_{\mathrm{Th}}$ and $I_N$ (diamond on); match; back to the original for efficiency.'],
])
CO('warning', r"**Traps.** (1) Never turn off a dependent source. (2) Max power: half of $V_{\mathrm{Th}}$, not half the supply; and only when the **load** is the knob. (3) Never add powers. (4) Same reference directions in every superposition picture. (5) Efficiency comes from the original circuit, not the equivalent.")
H(2, 'Formula sheet')
T(['Result', 'Formula', 'In heights'], [
    ['Test source', r'$R_{\mathrm{Th}}=\dfrac{v_T}{i_T}$ (independent off)', '$a$\'s height per amp pushed in'],
    ['One shot', r'$v_T=V_{\mathrm{Th}}+R_{\mathrm{Th}}i_T$ (all on)', 'intercept and slope of the sag line'],
    ['Load power', r'$p_L=\dfrac{V_{\mathrm{Th}}^2R_L}{(R_{\mathrm{Th}}+R_L)^2}=h\dfrac{V_{\mathrm{Th}}-h}{R_{\mathrm{Th}}}$', 'height × current'],
    ['Maximum power', r'$R_L=R_{\mathrm{Th}}$, $p_{\max}=\dfrac{V_{\mathrm{Th}}^2}{4R_{\mathrm{Th}}}$', r'load at $\dfrac{V_{\mathrm{Th}}}{2}$'],
    ['Superposition', r'$y=\sum_k y_k$; $p\neq\sum p_k$', 'add height differences'],
])

D.save(os.path.join(HERE, 'w45', 'w5_blocks.json'))
