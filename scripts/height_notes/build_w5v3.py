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

n = C['w5S']['net']
nm = {'s': 'source top', 'a': '$a$', '0': '$b$'}
EX('w5S', 'Example 0 · Open, short, sources off',
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

H(1, 'Topic 1: Thévenin with diamonds inside', D.oc('Topic 1: Thévenin and Norton'))
CO('tip', "**How it looks in heights.**\n\n"
          "- A diamond **never turns off**: keep it in every picture, with what it depends on.\n"
          "- **Push $1\\,\\mathrm{A}$ into $a$** (independent sources off): $a$'s height is $R_{\\mathrm{Th}}$. If $a$ goes **up** when you pull current out, $R_{\\mathrm{Th}}$ is negative: the diamond is giving energy.\n"
          "- No independent source at all: nothing lifts $a$, so $V_{\\mathrm{Th}}=0$ and only the push finds $R_{\\mathrm{Th}}$.\n"
          "- One shot: keep everything on and push $i_T$: then $a=V_{\\mathrm{Th}}+R_{\\mathrm{Th}}\\,i_T$ (start height + slope).")

EQ(r'R_{\mathrm{Th}}=\frac{v_T}{i_T}\;(\text{independent sources off}),\qquad v_T=V_{\mathrm{Th}}+R_{\mathrm{Th}}\,i_T\;(\text{all on})')

n = C['w5A']['net']
EX('w5A', 'Example 1 · A diamond lowers the climb', r'Find $R_{\mathrm{Th}}$ at $a$–$b$. The diamond draws $\tfrac{v}{3}$ from $a$ to $b$.',
   fence('w5A', [view(n + [IT()], [('IT', 0), ('R1', 1), ('G1', 2)], title='Push 1 A', names={'a': '$a$', '0': '$b$'}, terminals={'a'},
                      elabel={'G1': r'$\tfrac{v}{3}$'}, refs={'R1': ('a', '$v$')}, disp={'IT': TEST}, steps=[
       (r"Ground $b$, push $1\,\mathrm{A}$ in. KCL: $1=\dfrac{a}{6}+\dfrac{a}{3}=\dfrac{a}{2}$, so $a=2\,\mathrm{V}$: $R_{\mathrm{Th}}=2\,\Omega$, not $6$.", ['a', 'eR1', 'eG1']),
   ])], spoiler=False, inline=True),
   [S('Test current.', r'1=\frac{v}{6}+\frac{v}{3}\;\Rightarrow\;v=2\,\mathrm{V},\quad R_{\mathrm{Th}}=2\,\Omega')], r'$R_{\mathrm{Th}}=2\,\Omega$')

n = C['lecneg']['net']
EX('lecneg', 'Example 2 · Pull current out, and a rises (Lecture 5)',
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
EX('lecm4', 'Example 3 · One shot: the test source as a variable (Lecture 5)',
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


n = C['p474']['net']
nm = {'n': '$n$', 'm': '$m$', 'a': '$a$', '0': '$b$'}
el = {'E1': r'$160i_\Delta$'}
PR('p474', 'Try it 3 · A diamond battery on the top wire (Textbook P4.74)', 'intermediate',
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

n = C['p481']['net']
PR('p481', 'Try it 4 · Only a diamond inside (Textbook P4.81)', 'intermediate',
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

H(1, 'Topic 2: Maximum power: half the open height', D.oc('Topic 2: Maximum power'))
CO('tip', "**How it looks in heights.**\n\n"
          "- A load on a Thévenin source sits at some height $h$ and gets current $\\dfrac{V_{\\mathrm{Th}}-h}{R_{\\mathrm{Th}}}$. Its power $h\\cdot\\dfrac{V_{\\mathrm{Th}}-h}{R_{\\mathrm{Th}}}$ is biggest when $h=\\dfrac{V_{\\mathrm{Th}}}{2}$: the **half-height rule**. That happens when $R_L=R_{\\mathrm{Th}}$.\n"
          "- Half of $V_{\\mathrm{Th}}$, not half the battery.\n"
          "- Maximum power is not maximum efficiency. For efficiency, go back to the original circuit and compare the load's power with every source's climb.\n"
          "- Load fixed and a series resistor is the knob? That resistor only steals height: the best value is $0$.")

EQ(r'R_L=R_{\mathrm{Th}},\qquad h=\frac{V_{\mathrm{Th}}}{2},\qquad p_{\max}=\frac{V_{\mathrm{Th}}^2}{4R_{\mathrm{Th}}}')

th = lambda rl: [('V', 'V1', 't', '0', 20), ('R', 'R1', 't', 'a', 5), ('R', 'RL', 'a', '0', rl)]  # noqa: E731
nm = {'t': 'top', 'a': '$a$', '0': '$b$'}
dth = {'V1': ('V', r'$V_{\mathrm{Th}}$: $20\,\mathrm{V}$')}
EX('w5B', 'Example 4 · Matched vs not', r'$V_{\mathrm{Th}}=20\,\mathrm{V}$, $R_{\mathrm{Th}}=5\,\Omega$. Compare $R_L=5$, $20$ and $1.25\,\Omega$.',
   fence('w5B', [
       view(th(5), [('V1', 0), ('R1', 1), ('RL', 1)], title='Load 5 Ω (matched)', names=nm, disp=dth, steps=[
           (r"Ground $b$. $a$ at half height, $10\,\mathrm{V}$; $2\,\mathrm{A}$; $p=20\,\mathrm{W}$ (the most).", ['a', 'eRL']),
       ]),
       view(th(20), [('V1', 0), ('R1', 1), ('RL', 1)], title='Load 20 Ω', names=nm, disp=dth, notes=[r"$a=16\,\mathrm{V}$, $0.8\,\mathrm{A}$: $12.8\,\mathrm{W}$."]),
       view(th(1.25), [('V1', 0), ('R1', 1), ('RL', 1)], title='Load 1.25 Ω', names=nm, disp=dth, notes=[r"$a=4\,\mathrm{V}$, $3.2\,\mathrm{A}$: also $12.8\,\mathrm{W}$. $4$ and $16$ mirror around $10$."]),
   ], spoiler=False, inline=True),
   [S('Power at height $h$.', r'p=h\cdot\frac{20-h}{5}:\quad h=10\to20\,\mathrm{W},\quad h=4\text{ or }16\to12.8\,\mathrm{W}')],
   r'Matched: $20\,\mathrm{W}$; the other two: $12.8\,\mathrm{W}$ each.')

n = C['lec360']['net']
nm = {'s': 'source top', 'a': '$a$', '0': 'ground'}
cols360 = [('V1', 0), ('R1', 1), ('R2', 2), ('R3', 3)]
EX('lec360', 'Example 5 · Half the open height (Lecture 5)',
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
EX('lecmp', 'Example 6 · Two sources, then match (Lecture 5)',
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
PR('p484', 'Try it 5 · The matching trap (Textbook P4.84)', 'introductory',
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
PR('p488', 'Try it 6 · Two loads, same power (Textbook P4.88)', 'advanced',
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


n = C['p483']['net']
PR('p483', 'Try it 7 · Match the load on a diamond circuit (Textbook P4.83)', 'intermediate',
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

n = C['p487']['net']
nm = {'s': 'battery top', 'p': '$p$', 'q': '$q$', 'k': 'diamond top', '0': '$b$'}
el = {'E1': r'$13i_\Delta$', 'G1': r'$v_\Delta$'}
PR('p487', 'Try it 8 · Maximum power, and most of it gets there (Textbook P4.87)', 'advanced',
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

H(1, 'Topic 3: Superposition: add heights, not powers', D.oc('Topic 3: Superposition'))
CO('tip', "**How it looks in heights.**\n\n"
          "- One picture per independent source: the other batteries become wires, the other pumps become gaps. **Diamonds stay on.**\n"
          "- **Add the heights** (voltages) and the currents from the pictures. **Never add powers**: power is a product, so compute it once from the sums.\n"
          "- Keep the same reference directions in every picture.\n"
          "- Worth it when each one-source picture is a simple divider; otherwise one node-voltage solve is faster.")

EQ(r'y=y_1+y_2+\cdots,\qquad p=(v_1+v_2)(i_1+i_2)\neq p_1+p_2')

n = C['w5C']['net']
nm = {'t': 'source top', 'm': '$m$', '0': 'ground'}
EX('w5C', 'Example 7 · Two pictures, one sum', r'Find the height of $m$ by superposition.',
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

n = C['lecsup']['net']
nm = {'s': '$s$', 'n1': 'node 1', 'n2': 'node 2', '0': 'bottom'}
EX('lecsup', 'Example 8 · One source at a time (Lecture 5)',
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
EX('lecsupd', 'Example 9 · Dependent sources stay on (Lecture 5)',
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
PR('p494', 'Try it 9 · Three sources (Textbook P4.94)', 'intermediate',
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
PR('p496', 'Try it 10 · Adding one more source (Textbook P4.96)', 'intermediate',
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


n = C['p495']['net']
nm = {'s': '$s$', 'p': '$p$', 'q': '$q$', 'r': '$r$', '0': 'bottom'}
PR('p495', 'Try it 11 · A battery and a pump (Textbook P4.95)', 'intermediate',
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

H(1, 'Practice set')
P('Exam-style, mixing all three topics. Try each for 10–15 minutes before opening the solution, then check your picture against the height view.')

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

H(1, 'Cheat sheet')
T(['Idea', 'In heights', 'Write'], [
    ['Thévenin with diamonds', 'push $1\\,\\mathrm{A}$ into $a$ (independent sources off)', r'$R_{\mathrm{Th}}=\dfrac{v_T}{i_T}$'],
    ['One-shot test source', 'start height + slope', r'$v_T=V_{\mathrm{Th}}+R_{\mathrm{Th}}i_T$'],
    ['No independent source', 'nothing lifts $a$', r'$V_{\mathrm{Th}}=I_N=0$'],
    ['Maximum power', 'load at half the open height', r'$R_L=R_{\mathrm{Th}}$, $p_{\max}=\dfrac{V_{\mathrm{Th}}^2}{4R_{\mathrm{Th}}}$'],
    ['Efficiency', 'load power ÷ all the climbs (original circuit)', r'$\eta=\dfrac{p_L}{\sum p_{\text{dev}}}$'],
    ['Superposition', 'one picture per source; add heights', r'$y=y_1+y_2+\cdots$, $p\neq p_1+p_2$'],
])

D.save(os.path.join(HERE, 'w45', 'w5v3_blocks.json'))
