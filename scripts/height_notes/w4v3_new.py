#### SECTION header
"""Week 4, v3 layout (assembled by make_w4v3.py from build_w4.py pieces + w4v3_new.py). Do not edit by hand."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import circuits4v3 as c4  # noqa: E402
from blocks45 import Doc, S  # noqa: E402
from w45lib import C, view, fence, off  # noqa: E402
from weekkit import card  # noqa: E402

D = Doc('w4-v3', 4)
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

card(D, "**Week 4 in one line:** shortcuts. **Pick** the method with fewer equations, **swap** sources to simplify, and **shrink** a whole circuit to two numbers ($V_{\\mathrm{Th}}$, $R_{\\mathrm{Th}}$) that a load can see.",
     "a source swap or a Thévenin equivalent keeps the heights **at the terminals** and redraws the inside. Never read inside powers from the redrawn circuit.")

#### SECTION topic1
H(1, 'Topic 1: Shortcuts: pick the method, swap sources', D.oc('Topic 1: Choosing'))
CO('tip', "**How it looks in heights.**\n\n"
          "- **Pick the method:** node voltages need one equation per unknown height (batteries from ground give heights for free); meshes need one per window (edge pumps give loop currents for free). Take the smaller count.\n"
          "- **Swap:** a battery $V$ in series with $R$ is the same, seen from outside, as a pump $\\dfrac{V}{R}$ in parallel with the same $R$ (arrow toward the $+$ end).\n"
          "- Same terminal height for **every** load; the inside is different, so go back to the original for powers.\n"
          "- A resistor across a battery, or in series with a pump, changes no other height: drop it while you solve (it still uses power).")

#### SECTION swap2
EX('swap2', 'Two swaps make one loop', r'Find the heights of $p$ and $q$ and the power of each source.',
   fence('swap2', [view(C['swap2']['net'], [('I1', 0), ('R1', 1), ('R2', 2), ('R3', 2), ('V1', 3)], names={'p': '$p$', 'q': '$q$', 't': 'battery top', '0': 'ground'}, steps=[
       (r"Ground the bottom wire. The $24\,\mathrm{V}$ battery lifts its top to $24\,\mathrm{V}$.", []),
       (r"Swap the $2\,\mathrm{A}$ pump and its $6\,\Omega$ for a $12\,\mathrm{V}$ battery behind $6\,\Omega$ ($2\times6=12$, $+$ on top). Now it is one loop: $24\,\mathrm{V}$ pushing one way, $12\,\mathrm{V}$ the other, through $6+4+2=12\,\Omega$.", []),
       (r"Loop current $=\dfrac{24-12}{12}=1\,\mathrm{A}$, flowing right to left through the $2\,\Omega$ and $4\,\Omega$.", ['eR2', 'eR3', 'eV1']),
       (r"Walk down from $24\,\mathrm{V}$: $q=24-2=22\,\mathrm{V}$, $p=22-4=18\,\mathrm{V}$.", ['q', 'p']),
       (r"Back in the real circuit: $\dfrac{18}{6}=3\,\mathrm{A}$ goes down the $6\,\Omega$ = $1\,\mathrm{A}$ from the right + $2\,\mathrm{A}$ from the pump ✓. The pump lifts $2\,\mathrm{A}$ by $18\,\mathrm{V}$ ($36\,\mathrm{W}$), the battery gives $24\,\mathrm{W}$.", ['eR1', 'eI1']),
   ])], spoiler=False, inline=True),
   [S('Swap the pump.', r'2\,\mathrm{A}\parallel6\,\Omega\;\to\;12\,\mathrm{V}+6\,\Omega'),
    S('One loop.', r'\begin{aligned}&i=\frac{24-12}{6+4+2}=1\,\mathrm{A}\\&q=24-2(1)=22\,\mathrm{V},\quad p=22-4(1)=18\,\mathrm{V}\end{aligned}'),
    S('Powers (original circuit).', r'p_{2\mathrm{A}}=2(18)=36\,\mathrm{W},\qquad p_{24\mathrm{V}}=24(1)=24\,\mathrm{W}')],
   r'$p=18\,\mathrm{V}$, $q=22\,\mathrm{V}$; the pump gives $36\,\mathrm{W}$, the battery $24\,\mathrm{W}$.')

#### SECTION p458
nm = {'a': '$a$', 'b': '$b$', 'm': '$m$', 'k': '115 V top', 'r': '$r$', 'l': '$l$', '0': 'bottom middle'}
PR('p458', 'Find the battery that silences a resistor (Textbook P4.58)', 'intermediate',
   r'The variable battery $v_{dc}$ is adjusted so that $i_o=0$. **(a)** Node or mesh? **(b)** Find $v_{dc}$. **(c)** Check the power balance.',
   fence('p458', [view(c4.p458_net(195), [('V1', 0), ('R1', 1), ('R4', 1), ('V2', 1), ('R5', 1), ('R3', 2), ('R2', 3), ('V3', 4), ('R6', 4)], gnd='low', names=nm, steps=[
       (r"Ground $l$, the lowest wire. Heights here are measured from $l$.", []),
       (r"The key fact: $i_o=0$ means the $30\,\Omega$ has **no fall**, so its two ends $a$ and $b$ sit at the **same height**.", ['eR3']),
       (r"So the $5\,\Omega$ and the $15\,\Omega$ both fall from that height down to $m$: the $5\,\Omega$ carries $3\times$ the current of the $15\,\Omega$. In = out at $m$ and around the left loop give $3\,\mathrm{A}$ and $1\,\mathrm{A}$; $4\,\mathrm{A}$ goes down the $10\,\Omega$ into the $115\,\mathrm{V}$ battery (it absorbs).", ['m', 'k', 'eR1', 'eR2', 'eR4', 'eR5', 'eV1', 'eV2']),
       (r"The $1\,\mathrm{A}$ through the $15\,\Omega$ comes up the right side: $1\,\mathrm{A}$ through the $25\,\Omega$ and up through $v_{dc}$. Height difference across it: $v_{dc}=195\,\mathrm{V}$.", ['r', 'z0', 'eR6', 'eV3']),
       (r"Power: $230\,\mathrm{V}$ gives $690\,\mathrm{W}$, $v_{dc}$ gives $195\,\mathrm{W}$; slides $425\,\mathrm{W}$ + the $115\,\mathrm{V}$ battery $460\,\mathrm{W}$ = $885\,\mathrm{W}$ ✓", []),
   ])]),
   [S(r'(a) Node voltages: the condition $i_o=0$ is a statement about heights, $v_a=v_b$. Ground the bottom-middle wire.', r'v_a=v_b,\qquad v_l=v_a-230'),
    S(r'In = out at $m$, and the left battery loop (no current in the $30\,\Omega$).', r'\begin{aligned}(v_a-v_m)\big(\tfrac15+\tfrac1{15}\big)&=\tfrac{v_m-115}{10}\\\tfrac{v_a-v_m}{5}&=\tfrac{230-v_a}{20}\end{aligned}\;\Rightarrow\;v_a=170,\;v_m=155\,\mathrm{V}'),
    S(r'(b) The $1\,\mathrm{A}$ in the $15\,\Omega$ flows through the $25\,\Omega$ and $v_{dc}$.', r'v_r=-25\,\mathrm{V},\qquad v_{dc}=v_b-v_r=195\,\mathrm{V}'),
    S('(c) Power balance.', r'230(3)+195(1)=885\,\mathrm{W}=45+15+160+180+25+460')],
   r'**(a)** Node voltages. **(b)** $v_{dc}=195\,\mathrm{V}$. **(c)** $885\,\mathrm{W}$ developed $=885\,\mathrm{W}$ absorbed.', D.tb('4.58'))

#### SECTION p461
nm = {'s': 'battery $-$', 'p': '$p$', 'q': '$q$', 'r': '$r$', 'l': '$l$', '0': 'bottom right'}
PR('p461', 'A battery hung upside down (Textbook P4.61)', 'intermediate',
   r'**(a)** Use source transformations to find $i_o$. **(b)** Work back to find the power developed by the $100\,\mathrm{V}$ source.',
   fence('p461', [view(C['p461']['net'], [('R1', 0), ('V1', 1), ('R3', 2), ('R2', 2), ('R7', 2), ('I1', 3), ('R4', 4), ('R5', 5), ('R6', 5)], gnd='low', unit='mA', names=nm, steps=[
       (r"Ground the lowest wire: the battery's $-$ end, on top. Heights are from there; the question's voltages are from the bottom-right wire.", []),
       (r"Swap from the left (kΩ, mA): the battery and $20\,\mathrm{k\Omega}$ become a $5\,\mathrm{mA}$ pump; beside the $80\,\mathrm{k\Omega}$ that is $16\,\mathrm{k\Omega}$; swap back and add the $3$ and $1\,\mathrm{k\Omega}$: the whole left side is $80\,\mathrm{V}$ behind $20\,\mathrm{k\Omega}$, pulling $q$ toward $-80\,\mathrm{V}$.", []),
       (r"In = out at $q$ (from the bottom-right wire): $\dfrac{q+80}{20}+\dfrac{q}{60}+\dfrac{q}{15}=12$, so $q=60\,\mathrm{V}$ and $i_o=\dfrac{60}{15}=4\,\mathrm{mA}$.", ['q', 'r', 'eR4', 'eR5', 'eR6', 'eI1']),
       (r"Back in the original: $7\,\mathrm{mA}$ leaves $q$ to the left; $6.6\,\mathrm{mA}$ of it goes through the battery from $-$ to $+$, so it **climbs** $100\,\mathrm{V}$: $660\,\mathrm{mW}$ developed.", ['p', 'l', 'z0', 'eR1', 'eR2', 'eR3', 'eR7', 'eV1']),
   ])]),
   [S(r'Left side, swapped down to one source (kΩ, mA, V measured from the bottom-right wire).', r'\tfrac{100}{20}=5\,\mathrm{mA};\;\;20\parallel80=16;\;\;5(16)=80\,\mathrm{V};\;\;16+3+1=20\,\mathrm{k\Omega}'),
    S(r'In = out at $q$.', r'\frac{q+80}{20}+\frac{q}{60}+\frac{q}{15}=12\;\Rightarrow\;q=60\,\mathrm{V},\qquad i_o=\frac{60}{5+10}=4\,\mathrm{mA}'),
    S('Back to the original for the battery.', r'p_{100\mathrm{V}}=100(6.6\,\mathrm{mA})=660\,\mathrm{mW}\text{ developed}')],
   r'**(a)** $i_o=4\,\mathrm{mA}$. **(b)** The $100\,\mathrm{V}$ source develops $660\,\mathrm{mW}$.', D.tb('4.61'))

#### SECTION p462
nm = {'a': '$a$', 'b': '$b$', 'c': '$c$', 'd': '$d$', '0': 'bottom wire'}
PR('p462', 'Swaps on both ends (Textbook P4.62)', 'intermediate',
   r'**(a)** Make a series of source transformations to find $v_o$. **(b)** Check with the mesh-current method.',
   fence('p462', [view(C['p462']['net'], [('R2', 0), ('I1', 1), ('R1', 2), ('R4', 3), ('R3', 3), ('V1', 4), ('R5', 4), ('I2', 5)], gnd='low', unit='mA', names=nm,
                       refs={'R2': ('a', '$v_o$')}, steps=[
       (r"Ground $a$, the lowest wire: the $2.5\,\mathrm{mA}$ pump drags it below the bottom wire.", []),
       (r"Swaps (kΩ, mA): $2.5\,\mathrm{mA}\parallel8\,\mathrm{k\Omega}$ → $20\,\mathrm{V}$ behind $8\,\mathrm{k\Omega}$, pulling down; $12\,\mathrm{mA}\parallel5\,\mathrm{k\Omega}$ → $60\,\mathrm{V}$ behind $5\,\mathrm{k\Omega}$; add the $40\,\mathrm{V}$ battery and $15\,\mathrm{k\Omega}$: the right side is $100\,\mathrm{V}$ behind $20\,\mathrm{k\Omega}$.", []),
       (r"In = out at $b$ (from the bottom wire): $\dfrac{b-100}{20}+\dfrac{b+20}{32}+\dfrac{b}{80}=0$, so $b=46.67\,\mathrm{V}$.", ['b', 'c', 'd']),
       (r"The $24\,\mathrm{k\Omega}$ carries $\dfrac{46.67+20}{32}=2.08\,\mathrm{mA}$ from $b$ to $a$ and falls $50\,\mathrm{V}$. Its $+$ end ($a$) is the **lower** one: $v_o=-50\,\mathrm{V}$.", ['z0', 'eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eV1', 'eI1', 'eI2']),
   ])]),
   [S('Swap both pumps (kΩ, mA, V).', r'\begin{aligned}&2.5(8)=20\,\mathrm{V},\qquad 12(5)=60\,\mathrm{V}\\&\text{right side: }60+40=100\,\mathrm{V}\text{ behind }20\,\mathrm{k\Omega}\end{aligned}'),
    S(r'In = out at $b$ (the left side is $-20\,\mathrm{V}$ behind $8+24=32\,\mathrm{k\Omega}$).', r'\frac{v_b-100}{20}+\frac{v_b+20}{32}+\frac{v_b}{80}=0\;\Rightarrow\;v_b=46.67\,\mathrm{V}'),
    S('The $24\\,\\mathrm{k\\Omega}$.', r'i=\frac{46.67+20}{32}=2.083\,\mathrm{mA},\qquad v_o=-24(2.083)=-50\,\mathrm{V}')],
   r'$v_o=-50\,\mathrm{V}$', D.tb('4.62'))

#### SECTION topic2
H(1, 'Topic 2: Thévenin and Norton', D.oc('Topic 3: Thévenin and Norton'))
CO('tip', "**How it looks in heights.**\n\n"
          "- Seen from $a$–$b$, any circuit is **one battery $V_{\\mathrm{Th}}$ behind one slide $R_{\\mathrm{Th}}$**. Ground $b$.\n"
          "- **Open** (nothing attached): $a$ sits at $V_{\\mathrm{Th}}$. **Short** ($a$ wired to $b$): the current that flows is $I_N$.\n"
          "- **Sources off** (battery → wire, pump → gap), push $1\\,\\mathrm{A}$ into $a$: $a$'s height is $R_{\\mathrm{Th}}$. Or use $R_{\\mathrm{Th}}=\\dfrac{V_{\\mathrm{Th}}}{I_N}$.\n"
          "- A load drawing $i$ makes $a$ **sag**: $v_{ab}=V_{\\mathrm{Th}}-R_{\\mathrm{Th}}\\,i$. Norton is the swap of Thévenin: $I_N$ in parallel with $R_{\\mathrm{Th}}$.")

#### SECTION p466
n = C['p466']['net']
nm = {'s': 'battery top', 'm': '$m$', 'a': '$a$', '0': '$b$'}
PR('p466', 'Norton with a bypass (Textbook P4.66)', 'intermediate',
   r'Find the Norton equivalent at $a$–$b$.',
   fence('p466', [
       view(n + [SC()], [('V1', 0), ('R1', 1), ('R3', 2), ('R2', 3), ('R4', 4), ('SC', 4)], title='Short', names=nm, disp={'SC': SHORT}, steps=[
           (r"Ground $b$. The battery lifts its top to $72\,\mathrm{V}$. A wire pins $a$ to $b$.", []),
           (r"Now $m$ is the only unknown. In = out at $m$: $\dfrac{72-m}{5}=\dfrac{m}{20}+\dfrac{m}{8}$, so $m=38.4\,\mathrm{V}$.", ['m']),
           (r"Into the short: $\dfrac{72}{12}+\dfrac{38.4}{8}=6+4.8=10.8\,\mathrm{A}=I_N$.", ['eR2', 'eR4', 'eSC', 'eR1', 'eR3', 'eV1']),
       ]),
       view(off(n) + [IT()], [('R4', 0), ('V1', 0), ('R2', 1), ('R1', 2), ('R3', 3), ('IT', 4)], title='Sources off, push 1 A', names=nm, terminals={'a'},
            disp={'V1': OFFV(72), 'IT': TEST}, steps=[
           (r"Same ground. Battery → wire. Push $1\,\mathrm{A}$ into $a$: $12\,\Omega$ straight down, or $8+(5\parallel20)=12\,\Omega$. Half each.", ['eR1', 'eR2', 'eR3', 'eR4', 'eV1']),
           (r"$a=(0.5)(12)=6\,\mathrm{V}$: $R_N=6\,\Omega$. (Check: open height $=I_NR_N=64.8\,\mathrm{V}$.)", ['a', 'm', 'eIT']),
       ]),
   ]),
   [S('Short: in = out at $m$.', r'\begin{aligned}&\frac{72-v_m}{5}=\frac{v_m}{20}+\frac{v_m}{8}\;\Rightarrow\;v_m=38.4\,\mathrm{V}\\&I_N=\frac{72}{12}+\frac{38.4}{8}=10.8\,\mathrm{A}\end{aligned}'),
    S('Sources off.', r'R_N=12\parallel\big(8+(5\parallel20)\big)=12\parallel12=6\,\Omega')],
   r'$I_N=10.8\,\mathrm{A}$ (toward $a$) in parallel with $R_N=6\,\Omega$.', D.tb('4.66'))

#### SECTION p467
n = C['p467']['net']
nm = {'n': 'battery top', 'a': '$a$', '0': '$b$'}
PR('p467', 'Norton when a battery fixes a wire (Textbook P4.67)', 'intermediate',
   r'Find the Norton equivalent at $a$–$b$.',
   fence('p467', [
       view(n, [('I1', 0), ('R1', 1), ('V1', 2), ('I2', 3), ('R3', 4), ('R2', 5)], title='Open', gnd='low', unit='mA',
            names={'n': 'battery top', 'a': '$a$', '0': '$b$ (bottom)'}, terminals={'a'}, steps=[
           (r"Ground $a$, the lowest wire: the $3\,\mathrm{mA}$ pump drags it below $b$. The $30\,\mathrm{V}$ battery fixes the top-left wire $30\,\mathrm{V}$ above $b$; the $10\,\mathrm{mA}$ pump and $10\,\mathrm{k\Omega}$ beside it change nothing at $a$–$b$.", []),
           (r"In = out at $a$ (from $b$): $\dfrac{30-a}{15}=3+\dfrac{a}{5}$, so $a=-3.75\,\mathrm{V}$: $V_{\mathrm{Th}}=-3.75\,\mathrm{V}$.", ['z0', 'n', 'eR2', 'eR3', 'eI2']),
           (r"With a short, $a$ would be pulled up to $b$: $I_N=\dfrac{V_{\mathrm{Th}}}{R_N}=-1\,\mathrm{mA}$ (tab 2 gives $R_N$). Directly: $\dfrac{30}{15}-3=-1\,\mathrm{mA}$.", ['eR1', 'eV1', 'eI1']),
       ]),
       view([e for e in off(n) if e[1] not in ('R1', 'I1')] + [IT(amps=1e-3)], [('V1', 0), ('R2', 1), ('I2', 2), ('R3', 3), ('IT', 4)], title='Sources off, push 1 mA', unit='mA',
            names=nm, terminals={'a'}, disp={'V1': OFFV(30), 'I2': ('S', r'$3\,\mathrm{mA}$ off: a gap'), 'IT': ('I', r'test $1\,\mathrm{mA}$')},
            notes=[r"The $10\,\mathrm{k\Omega}$ and the $10\,\mathrm{mA}$ pump sit across the flattened battery, so they are left out."], steps=[
           (r"Same ground. Battery → wire, pumps → gaps. Push $1\,\mathrm{mA}$ into $a$: $15\parallel5=3.75\,\mathrm{k\Omega}$, so $a$ climbs $3.75\,\mathrm{V}$: $R_N=3.75\,\mathrm{k\Omega}$.", ['a', 'eR2', 'eR3', 'eIT', 'eV1']),
           (r"Check: open height $=I_NR_N=-3.75\,\mathrm{V}$, so with nothing attached $a$ sits **below** $b$.", []),
       ]),
   ]),
   [S('Short: the battery fixes the left wire; in = out at $a$ (mA, kΩ).', r'\frac{30}{15}-3+I_N^{\,\text{in}}=0\;\Rightarrow\;I_N=\frac{30}{15}-3=-1\,\mathrm{mA}'),
    S('Sources off.', r'R_N=15\parallel5=3.75\,\mathrm{k\Omega}')],
   r'$I_N=-1\,\mathrm{mA}$ (so $1\,\mathrm{mA}$ points from $a$ to $b$ inside the source) in parallel with $R_N=3.75\,\mathrm{k\Omega}$.', D.tb('4.67'))

#### SECTION p477
n = C['p477']['net']
nm = {'s': '$s$', 'p': '$p$', 'a': '$a$', 'b': '$b$', '0': 'bottom'}
PR('p477', 'Thévenin two ways (Textbook P4.77)', 'intermediate',
   r'**(a)** Find the Thévenin equivalent at $a$–$b$ from the open-circuit voltage and the short-circuit current. **(b)** Find $R_{\mathrm{Th}}$ by removing the sources and compare.',
   fence('p477', [
       view(n, [('V1', 0), ('R1', 1), ('R2', 1), ('I1', 2), ('R3', 3), ('R4', 4), ('R5', 4)], title='Open', names=nm, terminals={'a'}, steps=[
           (r"Ground the bottom-left wire. The battery lifts its top to $17.4\,\mathrm{V}$.", []),
           (r"Unknowns $p$, $a$, $b$. The pump forces $0.1\,\mathrm{A}$ from $p$ to $a$. In = out at each: $p=3.65$, $a=7$, $b=2\,\mathrm{V}$.", ['p', 'a', 'b']),
           (r"$v_{ab}=a-b=5\,\mathrm{V}=V_{\mathrm{Th}}$. (A short across $a$–$b$ would carry $I_N=0.667\,\mathrm{A}$, so $R_{\mathrm{Th}}=\dfrac{5}{0.667}=7.5\,\Omega$.)", ['eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eV1', 'eI1']),
       ]),
       view([e for e in off(n) if e[1] not in ('R1', 'R2', 'I1')] + [('I', 'IT', 'b', 'a', 1)], [('R3', 0), ('V1', 0), ('R5', 1), ('R4', 2), ('IT', 3)],
            title='Sources off, push 1 A', gnd='low', names=nm, terminals={'a'}, disp={'V1': OFFV(17.4), 'IT': ('I', r'test $1\,\mathrm{A}$ from $b$ to $a$')},
            notes=[r"The $40\,\Omega$ and $15\,\Omega$ only reach $a$ through the pump's gap: no current, so they are left out."], steps=[
           (r"Ground $b$ (the lowest here). Battery → wire, pump → gap. Push $1\,\mathrm{A}$ from $b$ into $a$.", []),
           (r"Two paths from $a$ back to $b$: the $10\,\Omega$, or $26+4=30\,\Omega$. $10\parallel30=7.5\,\Omega$, so $a$ climbs $7.5\,\mathrm{V}$: $R_{\mathrm{Th}}=7.5\,\Omega$, the same.", ['a', 'eR3', 'eR4', 'eR5', 'eIT', 'eV1']),
       ]),
   ]),
   [S('Open: three node equations give the heights.', r'v_p=3.65,\quad v_a=7,\quad v_b=2\,\mathrm{V}\;\Rightarrow\;V_{\mathrm{Th}}=5\,\mathrm{V}'),
    S('Short circuit.', r'i_{sc}=0.667\,\mathrm{A}\;\Rightarrow\;R_{\mathrm{Th}}=\frac{5}{0.667}=7.5\,\Omega'),
    S('(b) Sources off.', r'R_{\mathrm{Th}}=10\parallel(26+4)=7.5\,\Omega\;\checkmark')],
   r'$V_{\mathrm{Th}}=5\,\mathrm{V}$, $R_{\mathrm{Th}}=7.5\,\Omega$ (both ways).', D.tb('4.77'))

#### SECTION practice
H(1, 'Practice set')
P('Exam-style, mixing both topics. Try each for 10–15 minutes before opening the solution, then check your picture against the height view.')

#### SECTION p456
nm = {'s': 'battery top', 'p': '$p$', 'q': '$q$', 'm': '$m$', '0': 'ground'}
PR('p456', 'Textbook P4.56 · Read power as a height difference', 'intermediate',
   r'The variable current source $i_{dc}$ is adjusted so that the $15\,\mathrm{A}$ source develops $3750\,\mathrm{W}$. **(a)** Node or mesh? **(b)** Find $i_{dc}$.',
   fence('p456', [view(c4.p456_net(2), [('V1', 0), ('R1', 1), ('R2', 1), ('I1', 2), ('R3', 3), ('I2', 4), ('R4', 5), ('R5', 6)], names=nm,
                       disp={'R5': ('R', r'$40\,\Omega$')}, steps=[
       (r"Ground the bottom wire. The battery lifts its top to $420\,\mathrm{V}$.", []),
       (r"The key fact: the $15\,\mathrm{A}$ pump lifts its current from $q$ up to $p$. Developing $3750\,\mathrm{W}$ means it lifts $15\,\mathrm{A}$ by $250\,\mathrm{V}$: $p-q=250\,\mathrm{V}$.", ['eI1']),
       (r"In = out at $p$: $\dfrac{420-p}{7.2}+15=\dfrac{p}{20}+\dfrac{250}{15}$, so $p=300$ and $q=50\,\mathrm{V}$.", ['p', 'q', 'eR1', 'eR2', 'eR3', 'eV1']),
       (r"In = out at $q$ and $m$: $m=66.67\,\mathrm{V}$ and $i_{dc}=2\,\mathrm{A}$. ($m$ is above $q$: $0.33\,\mathrm{A}$ slides back from $m$ to $q$, and the $i_{dc}$ pump lifts $2\,\mathrm{A}$ from $q$ to $m$.)", ['m', 'eR4', 'eR5', 'eI2']),
   ])]),
   [S(r'(a) Node voltages: the given power is a statement about the height difference across the pump.', r'15\,(v_p-v_q)=3750\;\Rightarrow\;v_p-v_q=250\,\mathrm{V}'),
    S(r'In = out at $p$.', r'\frac{420-v_p}{7.2}+15=\frac{v_p}{20}+\frac{250}{15}\;\Rightarrow\;v_p=300,\;v_q=50\,\mathrm{V}'),
    S(r'In = out at $q$ and $m$.', r'\begin{aligned}\tfrac{250}{15}&=15+\tfrac{50-v_m}{50}+i_{dc}\\\tfrac{50-v_m}{50}+i_{dc}&=\tfrac{v_m}{40}\end{aligned}\;\Rightarrow\;v_m=66.67\,\mathrm{V},\;i_{dc}=2\,\mathrm{A}')],
   r'**(a)** Node voltages. **(b)** $i_{dc}=2\,\mathrm{A}$.', D.tb('4.56'))

#### SECTION p470
n = C['p470']['net']
nm = {'s': 'battery top', 'l': '$l$', 'r': '$r$', '0': 'ground'}
PR('p470', 'Textbook P4.70 · A bridge just off balance', 'advanced',
   r'The bridge is balanced when $R_3=1200\,\Omega$. With $R_3=1204\,\Omega$, how much current does the $30\,\Omega$ galvanometer detect? (Hint: find the Thévenin equivalent across the galvanometer.)',
   fence('p470', [
       view([e for e in n if e[1] != 'RG'], [('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2), ('R4', 2)], title='Galvanometer removed', unit='mA', names=nm, digits=4, steps=[
           (r"Ground the bottom wire. The battery lifts the top to $120\,\mathrm{V}$.", []),
           (r"With the galvanometer removed, each side is a divider: $l=120\cdot\tfrac{600}{1500}=48\,\mathrm{V}$, $r=120\cdot\tfrac{800}{2004}=47.904\,\mathrm{V}$. The midpoints are only $95.8\,\mathrm{mV}$ apart: $V_{\mathrm{Th}}=95.8\,\mathrm{mV}$.", ['l', 'r']),
           (r"Battery flattened: $R_{\mathrm{Th}}=(900\parallel600)+(1204\parallel800)=360+480.6=840.6\,\Omega$.", []),
       ]),
       view(n, [('V1', 0), ('R1', 1), ('R2', 1), ('RG', 2), ('R3', 3), ('R4', 3)], title='Galvanometer attached', unit='mA', names=nm, digits=4,
            disp={'RG': ('R', r'galvanometer')}, steps=[
           (r"Same ground. The galvanometer is a load on the Thévenin source: $i=\dfrac{0.0958}{840.6+30}=0.110\,\mathrm{mA}$, from $l$ (higher) to $r$.", ['eRG']),
       ], notes=[r"Levels this close are spread apart so they stay readable: the real gap is a few millivolts."]),
   ]),
   [S('Thévenin across the galvanometer: two dividers.', r'V_{\mathrm{Th}}=120\Big(\frac{600}{1500}-\frac{800}{2004}\Big)=95.8\,\mathrm{mV}'),
    S('Battery flattened.', r'R_{\mathrm{Th}}=900\parallel600+1204\parallel800=840.6\,\Omega'),
    S('The galvanometer is the load.', r'i=\frac{0.0958}{840.6+30}=110\,\mu\mathrm{A}')],
   r'About $110\,\mu\mathrm{A}$, from $l$ to $r$.', D.tb('4.70'))

#### SECTION cheat
H(1, 'Cheat sheet')
T(['Idea', 'In heights', 'Write'], [
    ['Node or mesh', 'count unknown heights vs windows', r'node: $(n_e-1)-$fixed; mesh: $(b_e-n_e+1)-$fixed'],
    ['Source swap', 'same terminal height, different inside', r'$i_s=\dfrac{v_s}{R}$, $v_s=Ri_s$, arrow toward $+$'],
    ['Thévenin voltage', 'open height of $a$', r'$V_{\mathrm{Th}}=v_{oc}$'],
    ['Norton current', 'current when $a$ is wired to $b$', r'$I_N=i_{sc}=\dfrac{V_{\mathrm{Th}}}{R_{\mathrm{Th}}}$'],
    ['Thévenin resistance', 'height of $a$ per amp pushed in (sources off)', r'$R_{\mathrm{Th}}=\dfrac{v_{oc}}{i_{sc}}$'],
    ['Loaded terminal', 'the sag', r'$v_{ab}=V_{\mathrm{Th}}-R_{\mathrm{Th}}i=V_{\mathrm{Th}}\dfrac{R_L}{R_{\mathrm{Th}}+R_L}$'],
    ['Sources off', 'battery → wire, pump → gap', 'dependent sources stay on'],
])
