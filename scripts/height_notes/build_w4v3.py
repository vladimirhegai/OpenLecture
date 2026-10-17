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

EX('w4S', 'Example 0 · One unknown height',
   r'Find the height of $x$ and the power of each source.',
   fence('w4S', [view(C['w4S']['net'], [('V1', 0), ('R1', 1), ('R2', 1), ('I1', 2)], names={'t': 'top', 'x': '$x$', '0': 'ground'}, steps=[
       (r"Ground the bottom wire. The source puts the top at $12\,\mathrm{V}$.", []),
       (r"The pump pushes $1\,\mathrm{A}$ into $x$. KCL at $x$: $\dfrac{12-x}{4}+1=\dfrac{x}{4}$, so $x=8\,\mathrm{V}$.", ['x']),
       (r"Currents = fall ÷ R: $1\,\mathrm{A}$ through the top $4\,\Omega$, $2\,\mathrm{A}$ down the other.", ['eR1', 'eR2', 'eV1']),
       (r"Power: the source lifts $1\,\mathrm{A}$ by $12\,\mathrm{V}$ ($12\,\mathrm{W}$), the pump $1\,\mathrm{A}$ by $8\,\mathrm{V}$ ($8\,\mathrm{W}$). Falls: $4+16=20\,\mathrm{W}$.", []),
   ])], spoiler=False, inline=True),
   [S(r'KCL at $x$.', r'\frac{12-x}{4}+1=\frac{x}{4}\;\Rightarrow\;x=8\,\mathrm{V}'),
    S('Power: climbs = falls.', r'(12)(1)+(8)(1)=20\,\mathrm{W}=(4)(1)+(8)(2)')],
   r'$x=8\,\mathrm{V}$; the source delivers $12\,\mathrm{W}$, the pump $8\,\mathrm{W}$.')


H(1, 'Topic 1: Shortcuts: pick the method, swap sources', D.oc('Topic 1: Choosing'))
CO('tip', "**How it looks in heights.**\n\n"
          "- **Pick the method:** node voltages need one equation per unknown height (batteries from ground give heights for free); meshes need one per window (edge pumps give loop currents for free). Take the smaller count.\n"
          "- **Swap:** a battery $V$ in series with $R$ is the same, seen from outside, as a pump $\\dfrac{V}{R}$ in parallel with the same $R$ (arrow toward the $+$ end).\n"
          "- Same terminal height for **every** load; the inside is different, so go back to the original for powers.\n"
          "- A resistor across a battery, or in series with a pump, changes no other height: drop it while you solve (it still uses power).")

n = C['lec300']['net']
EX('lec300', 'Example 1 · Which method? Power in the 300 Ω (Lecture 4)',
   r'Decide which method needs fewer equations, then find the power in the $300\,\Omega$ resistor.',
   fence('lec300', [view(n, [('V1', 0), ('V2', 0), ('R1', 1), ('R7', 1), ('R6', 1), ('R2', 2), ('R5', 2), ('R4', 2), ('E1', 3), ('R3', 4)],
                         gnd='low', elabel={'E1': r'$50i_\Delta$'},
                         names={'s': '256 V top', 'a': '$a$', '0': 'bottom wire', 'c': '$c$', 'b': '$b$', 'd': '$d$'}, steps=[
       (r"Ground node $d$, the lowest point: the $128\,\mathrm{V}$ source has its $+$ on the bottom wire, so $d$ hangs below it. The text's voltages are measured from the bottom wire; here every height is $128\,\mathrm{V}$ more.", []),
       (r"Fixed heights: the bottom wire is one $128\,\mathrm{V}$ step above $d$; the $256\,\mathrm{V}$ source's top is $384\,\mathrm{V}$.", ['z0', 's']),
       (r"Unknowns: $a$ and $c$ ($b$ hangs from the bottom wire by the dependent step). KCL at both with $v_b=50i_\Delta=\dfrac{v_c-v_a}{6}$: $v_a=62.5$, $v_c=-8\,\mathrm{V}$ (heights $190.5$ and $120$).", ['a', 'c']),
       (r"Control: $i_\Delta=\dfrac{v_c-v_a}{300}=-0.235\,\mathrm{A}$, so the real current runs $a\to c$. The dependent step $50i_\Delta=-11.75\,\mathrm{V}$ puts $b$ **below** the bottom wire.", ['b', 'eE1', 'eR7']),
       (r"Every other current = fall ÷ R.", ['eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eR6', 'eV1', 'eV2']),
       (r"Answer: the $300\,\Omega$ falls $70.5\,\mathrm{V}$ carrying $0.235\,\mathrm{A}$: $p=16.57\,\mathrm{W}$.", []),
   ])]),
   [S(r'Mesh: $4$ essential nodes, $8$ essential branches, no current source.', r'N_{\text{mesh}}=8-4+1=5'),
    S(r'Node: ground the bottom wire. Both sources fix heights ($256$, $-128$); $b$ is set by the dependent source. Only $a$ and $c$ are unknown.', r'N_{\text{node}}=2'),
    S(r'KCL at $a$ and $c$ (×600 and ×6000), with $6v_b=v_c-v_a$.', r'\begin{aligned}16v_a-3v_c&=1024\\-16v_a+67v_c&=-1536\end{aligned}'),
    S('Add, then back-substitute.', r'v_c=-8\,\mathrm{V},\qquad v_a=62.5\,\mathrm{V}'),
    S('Control and power.', r'i_\Delta=\frac{-8-62.5}{300}=-0.235\,\mathrm{A},\qquad p=i_\Delta^2(300)=16.57\,\mathrm{W}')],
   r'Node-voltage (2 equations vs 5). $p_{300\,\Omega}\approx16.57\,\mathrm{W}$.', D.oc('Which method? Power'))

EQ(r'i_s=\frac{v_s}{R},\qquad v_s=R\,i_s')
SCH(r'''V1 0,3 -> 0,0 "$v_s$"
R1 0,3 -> 3,3 "$R$"
wire 0,0 -> 3,0
terminal 3,3 "$a$" right
terminal 3,0 "$b$" right
I1 6,0 -> 6,3 "$i_s=\tfrac{v_s}{R}$"
wire 6,3 -> 8,3
R2 8,3 -> 8,0 "$R$"
wire 6,0 -> 8,0
wire 8,3 -> 10,3
wire 8,0 -> 10,0
terminal 10,3 "$a$" right
terminal 10,0 "$b$" right''', 'Voltage form (left) and current form (right): the same at $a$–$b$.', D.oc('Voltage-source form'))

EX('stx', 'Example 2 · Same load, two forms',
   r'Attach a $2\,\Omega$ load to $12\,\mathrm{V}$ + $4\,\Omega$, then to its swap, $3\,\mathrm{A}$ ∥ $4\,\Omega$. Compare the height of $a$ and the source powers.',
   fence('stx', [
       view(C['stx']['net'], [('V1', 0), ('R1', 1), ('R2', 1)], title='Voltage form', names={'s': 'source top', 'a': '$a$', '0': '$b$'}, terminals={'a'}, steps=[
           (r"Ground $b$. The source steps up $12\,\mathrm{V}$.", []),
           (r"One loop: $\dfrac{12}{4+2}=2\,\mathrm{A}$. The $4\,\Omega$ falls $8\,\mathrm{V}$, so $a$ sits at $4\,\mathrm{V}$.", ['a', 'eR1', 'eR2', 'eV1']),
           (r"The source lifts $2\,\mathrm{A}$ by $12\,\mathrm{V}$: $24\,\mathrm{W}$.", []),
       ]),
       view([('I', 'Is', '0', 'a', 3), ('R', 'Rp', 'a', '0', 4), ('R', 'R2', 'a', '0', 2)], [('Is', 0), ('Rp', 1), ('R2', 2)],
            title='Current form: 3 A ∥ 4 Ω', names={'a': '$a$', '0': '$b$'}, terminals={'a'}, steps=[
           (r"Same ground. $i_s=\dfrac{12}{4}=3\,\mathrm{A}$ is pumped into $a$.", []),
           (r"Two paths down, side by side: $4\parallel2=\tfrac43\,\Omega$. So $a=(3)(\tfrac43)=4\,\mathrm{V}$: **the same height**.", ['a', 'eRp', 'eR2']),
           (r"But this pump lifts $3\,\mathrm{A}$ by $4\,\mathrm{V}$: only $12\,\mathrm{W}$. Inside powers differ.", []),
       ], notes=[r"Terminal heights match; inside powers do not. Go back to the original circuit for any source's power."]),
   ], spoiler=False, inline=True),
   [S('Voltage form.', r'i=\frac{12}{6}=2\,\mathrm{A},\quad v_a=(2)(2)=4\,\mathrm{V},\quad p_s=24\,\mathrm{W}'),
    S('Current form.', r'v_a=3\,(4\parallel2)=4\,\mathrm{V},\quad p_s=(3)(4)=12\,\mathrm{W}')],
   r'$a$ sits at $4\,\mathrm{V}$ in both; the sources deliver $24\,\mathrm{W}$ and $12\,\mathrm{W}$.')

EX('swap2', 'Example 3 · Two swaps make one loop', r'Find the heights of $p$ and $q$ and the power of each source.',
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

n = C['lec250']['net']
EX('lec250', 'Example 4 · Swap, solve, go back (Lecture 4)',
   r'Use source transformations to find $v_o$. Then find the power developed by the $250\,\mathrm{V}$ source and by the $8\,\mathrm{A}$ source.',
   fence('lec250', [
       view([('I', 'Is', '0', 'b', 10), ('R', 'R1', 'b', '0', 25), ('R', 'R4', 'b', '0', 100), ('R', 'R56', 'b', '0', 20), ('I', 'I1', 'b', '0', 8)],
            [('Is', 0), ('R1', 1), ('R4', 2), ('R56', 3), ('I1', 4)], title='1 · After the swaps',
            names={'b': '$b$', '0': 'ground'}, disp={'Is': ('I', r'$\tfrac{250}{25}=10\,\mathrm{A}$'), 'R56': ('R', r'$5+15\,\Omega$: falls $20\,\mathrm{V}$')}, steps=[
           (r"Ground the bottom wire. Drop the $125\,\Omega$ (across the $250\,\mathrm{V}$ source) and the $10\,\Omega$ (in series with the $8\,\mathrm{A}$ pump): neither moves $b$.", []),
           (r"Swap $250\,\mathrm{V}$ + $25\,\Omega$ for a $10\,\mathrm{A}$ pump with $25\,\Omega$ beside it. Net into $b$: $10-8=2\,\mathrm{A}$.", ['eIs', 'eI1']),
           (r"Three paths down from $b$: $25\parallel100\parallel20=10\,\Omega$. So $b=(2)(10)=20\,\mathrm{V}=v_o$.", ['b', 'eR1', 'eR4', 'eR56']),
       ]),
       view(n, [('V1', 0), ('R2', 1), ('R1', 2), ('R4', 2), ('R5', 3), ('R6', 3), ('I1', 4), ('R3', 5)], title='2 · Back to the original',
            names={'s': 'source top', 'b': '$b$', 'd': '$d$', 'e': '$e$', '0': 'ground'}, refs={'R4': ('b', '$v_o$')}, steps=[
           (r"Same ground. Copy $b=20\,\mathrm{V}$ from tab 1; the source fixes the top at $250\,\mathrm{V}$.", []),
           (r"Currents = fall ÷ R: $\dfrac{230}{25}=9.2\,\mathrm{A}$, $\dfrac{250}{125}=2\,\mathrm{A}$, $0.2\,\mathrm{A}$ down the $100\,\Omega$, $1\,\mathrm{A}$ through $5+15\,\Omega$.", ['e', 'eR1', 'eR2', 'eR4', 'eR5', 'eR6']),
           (r"The pump's $8\,\mathrm{A}$ falls through the $10\,\Omega$, so $d=80\,\mathrm{V}$. The pump lifts $8\,\mathrm{A}$ from $20$ to $80\,\mathrm{V}$: it **delivers** $480\,\mathrm{W}$.", ['d', 'eR3', 'eI1']),
           (r"The source lifts $9.2+2=11.2\,\mathrm{A}$ by $250\,\mathrm{V}$: $2800\,\mathrm{W}$. Check: the falls absorb $2116+500+4+5+15+640=3280\,\mathrm{W}$.", ['eV1']),
       ]),
   ]),
   [S(r'Drop the $125\,\Omega$ and the $10\,\Omega$; swap the $250\,\mathrm{V}$ + $25\,\Omega$.', r'i_s=\frac{250}{25}=10\,\mathrm{A}'),
    S(r'One node: net $2\,\mathrm{A}$ into $25\parallel100\parallel20=10\,\Omega$.', r'v_o=(10-8)(10)=20\,\mathrm{V}'),
    S(r'Back to the original for the $250\,\mathrm{V}$ source.', r'p=250\Big(\frac{250-20}{25}+\frac{250}{125}\Big)=250(11.2)=2800\,\mathrm{W}'),
    S(r'The $8\,\mathrm{A}$ source: $d=(8)(10)=80\,\mathrm{V}$.', r'p=(80-20)(8)=480\,\mathrm{W}\text{ developed}')],
   r'$v_o=20\,\mathrm{V}$; the $250\,\mathrm{V}$ source develops $2800\,\mathrm{W}$, the $8\,\mathrm{A}$ source $480\,\mathrm{W}$.', D.oc('Source transformations: voltage'))

n = C['p454']['net']
PR('p454', 'Try it 1 · Node or mesh for a bridge? (Textbook P4.54)', 'intermediate',
   r'**(a)** Which method would you use to find the power in the $10\,\Omega$ resistor, and why? **(b)** Find that power. **(c)** Find the power delivered by the $4\,\mathrm{A}$ source.',
   fence('p454', [view(n, [('I1', 0), ('R2', 1), ('R4', 1), ('R5', 2), ('R1', 3), ('R3', 3)],
                       names={'t': '$t$', 'l': '$l$', 'r': '$r$', '0': 'ground'}, steps=[
       (r"Ground the bottom wire. The pump pushes $4\,\mathrm{A}$ up into the top node $t$.", []),
       (r"Mesh walks (the pump fixes mesh 1 at $4\,\mathrm{A}$): $i_2=2.6$, $i_3=2\,\mathrm{A}$. Branch currents: $1.4\,\mathrm{A}$ down the $8\,\Omega$, $2.6$ down the $2\,\Omega$, $2$ down the $1\,\Omega$ and the $4\,\Omega$.", ['eR1', 'eR2', 'eR3', 'eR4']),
       (r"Heights, walking up from ground: $l=(2)(1)=2$, $r=(2)(4)=8$, $t=8+(2.6)(2)=13.2\,\mathrm{V}$.", ['l', 'r', 't']),
       (r"The $10\,\Omega$ joins $r$ ($8$) and $l$ ($2$): it falls $6\,\mathrm{V}$, so $0.6\,\mathrm{A}$ flows $r\to l$, against $i_{10}$. $p=(6)(0.6)=3.6\,\mathrm{W}$.", ['eR5']),
       (r"The pump lifts $4\,\mathrm{A}$ through $13.2\,\mathrm{V}$: it delivers $52.8\,\mathrm{W}$.", []),
   ])]),
   [S(r'Node: $3$ unknown heights. Mesh: $3$ meshes, but the pump fixes one.', r'N_{\text{node}}=3,\qquad N_{\text{mesh}}=2'),
    S('Upper and lower triangles, clockwise.', r'\begin{aligned}20i_2-10i_3&=32\\-10i_2+15i_3&=4\end{aligned}\;\Rightarrow\;i_2=2.6\,\mathrm{A},\;i_3=2\,\mathrm{A}'),
    S(r'The $10\,\Omega$ carries the difference.', r'i_{10}=i_3-i_2=-0.6\,\mathrm{A},\qquad p=(0.6)^2(10)=3.6\,\mathrm{W}'),
    S(r'Pump voltage = falls down the left side.', r'v=8(1.4)+1(2)=13.2\,\mathrm{V},\qquad p=(4)(13.2)=52.8\,\mathrm{W}')],
   r'**(a)** Mesh (2 equations vs 3). **(b)** $3.6\,\mathrm{W}$. **(c)** $52.8\,\mathrm{W}$ delivered.', D.tb('4.54'))


nm = {'a': '$a$', 'b': '$b$', 'm': '$m$', 'k': '115 V top', 'r': '$r$', 'l': '$l$', '0': 'bottom middle'}
PR('p458', 'Try it 2 · Find the battery that silences a resistor (Textbook P4.58)', 'intermediate',
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

n = C['p459']['net']
PR('p459', 'Try it 3 · Two pumps become one loop (Textbook P4.59)', 'intermediate',
   r'**(a)** Use source transformations to find $i_o$. **(b)** Check with the node-voltage method.',
   fence('p459', [view(n, [('I1', 0), ('R1', 1), ('R2', 2), ('R3', 3), ('I2', 4)], gnd='low', unit='mA',
                       names={'a': '$a$', 'b': '$b$', '0': 'bottom wire'}, steps=[
       (r"Ground node $a$, the lowest point: the $6\,\mathrm{mA}$ pump pulls current out of $a$ and drags it down. Moving ground changes no voltage difference.", []),
       (r"Swap each pump with its parallel resistor: $(6)(2.3)=13.8\,\mathrm{V}$ and $(4.2)(1)=4.2\,\mathrm{V}$. One loop: $i_o=\dfrac{13.8+4.2}{2.3+2.7+1}=3\,\mathrm{mA}$.", ['eR2']),
       (r"Place heights: the $2.7\,\mathrm{k\Omega}$ falls $(3)(2.7)=8.1\,\mathrm{V}$ from $b$ to $a$. The $2.3\,\mathrm{k\Omega}$ carries $6-3=3\,\mathrm{mA}$ from the bottom wire down to $a$: $6.9\,\mathrm{V}$.", ['b', 'z0', 'eR1', 'eR3']),
       (r"In the drawing's voltages (bottom wire $=0$): $v_a=-6.9$, $v_b=1.2\,\mathrm{V}$. Both pumps climb: they deliver $41.4$ and $5.04\,\mathrm{mW}$.", []),
   ])]),
   [S(r'Swap both pumps (mA, kΩ, V).', r'6\times2.3=13.8\,\mathrm{V},\qquad 4.2\times1=4.2\,\mathrm{V}'),
    S('One series loop.', r'i_o=\frac{13.8+4.2}{2.3+2.7+1}=3\,\mathrm{mA}'),
    S('Node check (currents out).', r'\begin{aligned}\tfrac{v_a}{2.3}+\tfrac{v_a-v_b}{2.7}+6&=0\\\tfrac{v_b}{1}+\tfrac{v_b-v_a}{2.7}&=4.2\end{aligned}\;\Rightarrow\;v_a=-6.9,\;v_b=1.2'),
    S('Same current.', r'i_o=\frac{1.2-(-6.9)}{2.7}=3\,\mathrm{mA}')],
   r'$i_o=3\,\mathrm{mA}$ (both ways).', D.tb('4.59'))

n = C['lecp9']['net']
PR('lecp9', 'Try it 4 · Is the 6 V source delivering? (Lecture 4)', 'intermediate',
   r'Find the power of the $6\,\mathrm{V}$ source. Is it absorbed or delivered?',
   fence('lecp9', [view(n, [('V2', 0), ('R5', 1), ('R4', 1), ('R3', 2), ('R2', 2), ('R6', 2), ('R1', 3), ('V1', 3)], gnd='low',
                        names={'e': '40 V top', 'd': '$d$', 'c': '$c$', 's': '6 V top', '0': 'bottom-left', 'f': '$f$'}, steps=[
       (r"Ground $f$, the lowest node (bottom-right wire). The text's voltages are measured from the bottom-left wire.", []),
       (r"Swaps, right to left: $40\,\mathrm{V}$ + $5\,\Omega$ → $8\,\mathrm{A}$ ∥ $5\,\Omega$; with the $20\,\Omega$ → $8\,\mathrm{A}$ ∥ $4\,\Omega$ → $32\,\mathrm{V}$ + $4\,\Omega$; plus $6+10\,\Omega$ → $1.6\,\mathrm{A}$ ∥ $20\,\Omega$. Left: $6\,\mathrm{V}$ + $4\,\Omega$ → $1.5\,\mathrm{A}$ ∥ $4\,\Omega$.", []),
       (r"Node $c$: $(1.5+1.6)(4\parallel20\parallel30)=9.3\,\mathrm{V}$ above the bottom-left wire, which is $3.3\,\mathrm{V}$ **above** the $6\,\mathrm{V}$ source's top.", ['c']),
       (r"So current falls from $c$ **into** the source's $+$ end: $\dfrac{3.3}{4}=0.825\,\mathrm{A}$, then down through it. The source **absorbs** $(6)(0.825)=4.95\,\mathrm{W}$.", ['eR1', 'eV1']),
       (r"The rest, in the original circuit: currents = fall ÷ R. Only the $40\,\mathrm{V}$ source climbs: it delivers $100.3\,\mathrm{W}$.", ['d', 'eR2', 'eR3', 'eR4', 'eR5', 'eR6', 'eV2']),
   ])]),
   [S(r'Right side: three swaps.', r'\tfrac{40}{5}=8\,\mathrm{A};\;\;5\parallel20=4\,\Omega;\;\;8\times4=32\,\mathrm{V};\;\;\tfrac{32}{6+4+10}=1.6\,\mathrm{A}'),
    S(r'Left side.', r'\tfrac{6}{4}=1.5\,\mathrm{A}'),
    S(r'One node: both pumps into $4\parallel20\parallel30=3\,\Omega$.', r'v_c=(1.5+1.6)(3)=9.3\,\mathrm{V}'),
    S('Back to the original.', r'i=\frac{6-9.3}{4}=-0.825\,\mathrm{A}\;\Rightarrow\;p=(6)(0.825)=4.95\,\mathrm{W}\text{ absorbed}')],
   r'The $6\,\mathrm{V}$ source **absorbs** $4.95\,\mathrm{W}$.', D.oc('Lecture 4 p. 9'))


n = C['p460']['net']
PR('p460', 'Try it 5 · A pump across a resistor (Textbook P4.60)', 'intermediate',
   r'**(a)** Use source transformations to find $i_o$. **(b)** Check with the mesh-current method.',
   fence('p460', [view(n, [('I1', 0), ('R1', 1), ('R2', 2), ('R3', 2), ('R5', 2), ('I2', 3), ('V1', 4), ('R4', 5)],
                       names={'p': '$p$', 'q': '$q$', 'k': '10 V top', 'r': '$r$', '0': 'ground'}, steps=[
       (r"Ground the bottom wire. The $10\,\mathrm{V}$ source fixes its top at $10\,\mathrm{V}$.", []),
       (r"Swaps: $4\,\mathrm{A}$ ∥ $5\,\Omega$ → $20\,\mathrm{V}$ + $5\,\Omega$; $10\,\mathrm{A}$ ∥ $1\,\Omega$ → $10\,\mathrm{V}$ + $1\,\Omega$ ($+$ toward $q$). Seen from $r$, the left side is $20-10=10\,\mathrm{V}$ behind $5+4+1=10\,\Omega$.", []),
       (r"Averaging at $r$: $\dfrac{10/10+10/40+0/2}{1/10+1/40+1/2}=2\,\mathrm{V}$. So $i_o=\dfrac{2}{2}=1\,\mathrm{A}$.", ['r', 'eR5']),
       (r"Back in the original: $p=16$, $q=12.8\,\mathrm{V}$. The $10\,\mathrm{A}$ pump lifts current from $r$ up to $q$; $10.8\,\mathrm{A}$ falls back through the $1\,\Omega$.", ['p', 'q', 'eR1', 'eR2', 'eR3', 'eR4', 'eI1', 'eI2', 'eV1']),
   ])]),
   [S('Swap both pumps.', r'4\times5=20\,\mathrm{V},\qquad 10\times1=10\,\mathrm{V}'),
    S(r'Node $r$ with three branches: $10\,\mathrm{V}$ behind $10\,\Omega$, $10\,\mathrm{V}$ behind $40\,\Omega$, $2\,\Omega$ to ground.', r'\frac{v_r-10}{10}+\frac{v_r-10}{40}+\frac{v_r}{2}=0\;\Rightarrow\;v_r=2\,\mathrm{V}'),
    S('Answer.', r'i_o=\frac{2}{2}=1\,\mathrm{A}')],
   r'$i_o=1\,\mathrm{A}$.', D.tb('4.60'))

nm = {'s': 'battery $-$', 'p': '$p$', 'q': '$q$', 'r': '$r$', 'l': '$l$', '0': 'bottom right'}
PR('p461', 'Try it 6 · A battery hung upside down (Textbook P4.61)', 'intermediate',
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

nm = {'a': '$a$', 'b': '$b$', 'c': '$c$', 'd': '$d$', '0': 'bottom wire'}
PR('p462', 'Try it 7 · Swaps on both ends (Textbook P4.62)', 'intermediate',
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

H(1, 'Topic 2: Thévenin and Norton', D.oc('Topic 3: Thévenin and Norton'))
CO('tip', "**How it looks in heights.**\n\n"
          "- Seen from $a$–$b$, any circuit is **one battery $V_{\\mathrm{Th}}$ behind one slide $R_{\\mathrm{Th}}$**. Ground $b$.\n"
          "- **Open** (nothing attached): $a$ sits at $V_{\\mathrm{Th}}$. **Short** ($a$ wired to $b$): the current that flows is $I_N$.\n"
          "- **Sources off** (battery → wire, pump → gap), push $1\\,\\mathrm{A}$ into $a$: $a$'s height is $R_{\\mathrm{Th}}$. Or use $R_{\\mathrm{Th}}=\\dfrac{V_{\\mathrm{Th}}}{I_N}$.\n"
          "- A load drawing $i$ makes $a$ **sag**: $v_{ab}=V_{\\mathrm{Th}}-R_{\\mathrm{Th}}\\,i$. Norton is the swap of Thévenin: $I_N$ in parallel with $R_{\\mathrm{Th}}$.")

EQ(r'V_{\mathrm{Th}}=v_{oc},\qquad I_N=i_{sc},\qquad R_{\mathrm{Th}}=\frac{V_{\mathrm{Th}}}{I_N},\qquad v_{ab}=V_{\mathrm{Th}}-R_{\mathrm{Th}}\,i')
tp = [('V', 'V1', 't', '0', 32), ('R', 'R1', 't', 'a', 8)]
EX('thpic', 'Example 5 · The terminal sags',
   r'A Thévenin source, $32\,\mathrm{V}$ behind $8\,\Omega$. Find $v_{ab}$ open, with a $24\,\Omega$ load, and the current with $a$ shorted to $b$.',
   fence('thpic', [
       view(tp, [('V1', 0), ('R1', 1)], title='Open', names={'t': 'top', 'a': '$a$', '0': '$b$'}, terminals={'a'},
            disp={'V1': ('V', r'$V_{\mathrm{Th}}$: $32\,\mathrm{V}$'), 'R1': ('R', r'$R_{\mathrm{Th}}$: no fall')}, steps=[
           (r"Ground $b$. The step lifts the top to $32\,\mathrm{V}$.", []),
           (r"Nothing attached, no current, so $R_{\mathrm{Th}}$ has **no fall**: $a$ sits at $V_{\mathrm{Th}}=32\,\mathrm{V}$.", ['a']),
       ]),
       view(C['thpic']['net'], [('V1', 0), ('R1', 1), ('RL', 1)], title='24 Ω load', names={'t': 'top', 'a': '$a$', '0': '$b$'}, terminals={'a'},
            disp={'V1': ('V', r'$V_{\mathrm{Th}}$: $32\,\mathrm{V}$'), 'R1': ('R', r'$R_{\mathrm{Th}}$: falls $8\,\mathrm{V}$'), 'RL': ('R', r'$24\,\Omega$: falls $24\,\mathrm{V}$')}, steps=[
           (r"Same ground. The load draws $\dfrac{32}{8+24}=1\,\mathrm{A}$.", ['eRL', 'eV1']),
           (r"$R_{\mathrm{Th}}$ falls $(1)(8)=8\,\mathrm{V}$: $a$ **sags** to $32-8=24\,\mathrm{V}$.", ['a', 'eR1']),
       ]),
       view(tp + [SC()], [('V1', 0), ('R1', 1), ('SC', 1)], title='Short', names={'t': 'top', 'a': '$a$', '0': '$b$'}, terminals={'a'},
            disp={'V1': ('V', r'$V_{\mathrm{Th}}$: $32\,\mathrm{V}$'), 'R1': ('R', r'$R_{\mathrm{Th}}$: falls $32\,\mathrm{V}$'), 'SC': SHORT}, steps=[
           (r"Same ground. A wire pins $a$ to $b$.", ['a']),
           (r"$R_{\mathrm{Th}}$ now falls the whole $32\,\mathrm{V}$: $I_N=\dfrac{32}{8}=4\,\mathrm{A}$.", ['eR1', 'eSC', 'eV1']),
       ], notes=[r"Sag per amp $=R_{\mathrm{Th}}$: $8\,\mathrm{V}$ per amp, until $a$ hits $b$ at $4\,\mathrm{A}$."]),
   ], spoiler=False, inline=True),
   [S('Open, loaded, shorted.', r'v_{oc}=32\,\mathrm{V},\qquad v_{ab}=32-8(1)=24\,\mathrm{V},\qquad i_{sc}=\frac{32}{8}=4\,\mathrm{A}')],
   r'$32\,\mathrm{V}$ open, $24\,\mathrm{V}$ with the load, $I_N=4\,\mathrm{A}$.')

n = C['w4C']['net']
nm = {'s': 'source top', 'a': '$a$', '0': '$b$'}
EX('w4C', 'Example 6 · All three tabs', r'Find $V_{\mathrm{Th}}$, $I_N$ and $R_{\mathrm{Th}}$ at $a$–$b$.',
   fence('w4C', [
       view(n, [('V1', 0), ('R1', 1), ('R2', 1)], title='Open', names=nm, terminals={'a'}, steps=[
           (r"Ground $b$. Divider: $2\,\mathrm{A}$; the $6\,\Omega$ falls $12\,\mathrm{V}$, so $a=6\,\mathrm{V}=V_{\mathrm{Th}}$.", ['a', 'eR1', 'eR2']),
       ]),
       view([e for e in n if e[1] != 'R2'] + [SC()], [('V1', 0), ('R1', 1), ('SC', 1)], title='Short', names=nm, disp={'SC': SHORT},
            notes=[r"The $3\,\Omega$ sits across the short (no fall, no current), so it is left out of this tab."], steps=[
           (r"Same ground. A wire pins $a$ to $b$: the $3\,\Omega$ has no fall; the $6\,\Omega$ falls $18\,\mathrm{V}$: $I_N=3\,\mathrm{A}$.", ['a', 'eR1', 'eSC']),
       ]),
       view(off(n) + [IT()], [('V1', 0), ('R1', 1), ('R2', 2), ('IT', 3)], title='Sources off, push 1 A', names=nm, terminals={'a'},
            disp={'V1': OFFV(18), 'IT': TEST}, steps=[
           (r"Same ground. Flatten the $18\,\mathrm{V}$. $1\,\mathrm{A}$ into $6\parallel3=2\,\Omega$: $a=2\,\mathrm{V}$, so $R_{\mathrm{Th}}=2\,\Omega=\dfrac{6}{3}$.", ['a', 'eR1', 'eR2', 'eIT']),
       ]),
   ], spoiler=False, inline=True),
   [S('Three numbers, one check.', r'V_{\mathrm{Th}}=6\,\mathrm{V},\quad I_N=3\,\mathrm{A},\quad R_{\mathrm{Th}}=6\parallel3=2\,\Omega=\frac{6}{3}')],
   r'$V_{\mathrm{Th}}=6\,\mathrm{V}$, $I_N=3\,\mathrm{A}$, $R_{\mathrm{Th}}=2\,\Omega$.')

n = C['lecth']['net']
nm = {'s': 'source top', 'n': '$v_1$', 'a': '$a$', '0': '$b$'}
EX('lecth', 'Example 7 · Open, short, sources off (Lecture 4)',
   r'Find the Thévenin and Norton equivalents at $a$–$b$.',
   fence('lecth', [
       view(n, [('V1', 0), ('R1', 1), ('R2', 2), ('I1', 3), ('R3', 3)], title='Open', names=nm, terminals={'a'}, steps=[
           (r"Ground $b$ (the bottom wire). The source fixes its top at $25\,\mathrm{V}$.", []),
           (r"Open terminal: no current in the $4\,\Omega$, so it lies flat and $a=v_1$. KCL at $v_1$: $\dfrac{v_1-25}{5}+\dfrac{v_1}{20}=3$, so $v_1=32\,\mathrm{V}=V_{\mathrm{Th}}$.", ['n', 'a']),
           (r"The pump lifted $v_1$ **above** the $25\,\mathrm{V}$ source, so $1.4\,\mathrm{A}$ falls back **into** the source.", ['eR1', 'eR2', 'eV1']),
       ]),
       view(n + [SC()], [('V1', 0), ('R1', 1), ('R2', 2), ('I1', 3), ('R3', 4), ('SC', 4)], title='Short', names=nm, disp={'SC': SHORT}, steps=[
           (r"Same ground. A wire pins $a$ to $b$, so the $4\,\Omega$ is a new path down.", []),
           (r"KCL at $v_1$: $\dfrac{v_1-25}{5}+\dfrac{v_1}{20}+\dfrac{v_1}{4}=3$, so $v_1=16\,\mathrm{V}$.", ['n']),
           (r"The $4\,\Omega$ falls $16\,\mathrm{V}$: $I_N=4\,\mathrm{A}$. So $R_{\mathrm{Th}}=\dfrac{32}{4}=8\,\Omega$.", ['eR3', 'eSC', 'eR1', 'eR2', 'eV1']),
       ]),
       view(off(n) + [IT()], [('V1', 0), ('R1', 1), ('R2', 2), ('I1', 3), ('R3', 4), ('IT', 5)], title='Sources off, push 1 A', names=nm, terminals={'a'},
            disp={'V1': OFFV(25), 'I1': OFFI(3), 'IT': TEST}, steps=[
           (r"Same ground. Sources off: the $25\,\mathrm{V}$ step flattens to a wire (its top comes down to $0$), the $3\,\mathrm{A}$ pump becomes a gap.", []),
           (r"Push $1\,\mathrm{A}$ into $a$. It falls $4\,\mathrm{V}$ through the $4\,\Omega$, then $4\,\mathrm{V}$ through $5\parallel20=4\,\Omega$.", ['n', 'eR3', 'eR1', 'eR2', 'eV1']),
           (r"$a$ climbed $8\,\mathrm{V}$ for $1\,\mathrm{A}$: $R_{\mathrm{Th}}=8\,\Omega$, the same as $\dfrac{32}{4}$.", ['a', 'eIT']),
       ]),
   ]),
   [S(r'Open: no current in the $4\,\Omega$; KCL at $v_1$.', r'\frac{v_1-25}{5}+\frac{v_1}{20}=3\;\Rightarrow\;V_{\mathrm{Th}}=v_1=32\,\mathrm{V}'),
    S(r'Short: the $4\,\Omega$ joins $v_1$ to $b$.', r'\frac{v_1-25}{5}+\frac{v_1}{20}+\frac{v_1}{4}=3\;\Rightarrow\;v_1=16,\;\;I_N=\frac{16}{4}=4\,\mathrm{A}'),
    S('Two ways to get the resistance.', r'R_{\mathrm{Th}}=\frac{32}{4}=8\,\Omega=(5\parallel20)+4')],
   r'Thévenin: $32\,\mathrm{V}$ in series with $8\,\Omega$. Norton: $4\,\mathrm{A}$ (toward $a$) ∥ $8\,\Omega$.', D.oc('Thévenin and Norton equivalents, independent'))

n = C['p465']['net']
nm = {'s': 'source top', 'm': '$m$', 'a': '$a$', '0': '$b$'}
PR('p465', 'Try it 8 · A loaded divider (Textbook P4.65)', 'introductory',
   r'Find the Thévenin equivalent at $a$–$b$.',
   fence('p465', [
       view(n, [('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2)], title='Open', names=nm, terminals={'a'}, steps=[
           (r"Ground $b$. The source fixes its top at $80\,\mathrm{V}$.", []),
           (r"Open: no current in the $2.5\,\Omega$ (flat), so $a=m$. A plain divider: $2\,\mathrm{A}$, the $10\,\Omega$ falls $20\,\mathrm{V}$, so $a=60\,\mathrm{V}=V_{\mathrm{Th}}$.", ['m', 'a', 'eR1', 'eR2', 'eV1']),
       ]),
       view(off(n) + [IT()], [('V1', 0), ('R1', 1), ('R2', 2), ('R3', 3), ('IT', 4)], title='Sources off, push 1 A', names=nm, terminals={'a'},
            disp={'V1': OFFV(80), 'IT': TEST}, steps=[
           (r"Same ground. The $80\,\mathrm{V}$ step flattens to a wire.", []),
           (r"Push $1\,\mathrm{A}$ into $a$: it falls $2.5\,\mathrm{V}$, then $7.5\,\mathrm{V}$ through $10\parallel30=7.5\,\Omega$.", ['m', 'eR3', 'eR1', 'eR2', 'eV1']),
           (r"$a$ sits at $10\,\mathrm{V}$ per amp: $R_{\mathrm{Th}}=10\,\Omega$.", ['a', 'eIT']),
       ]),
   ]),
   [S('Open: divider.', r'V_{\mathrm{Th}}=80\cdot\frac{30}{10+30}=60\,\mathrm{V}'),
    S('Sources off.', r'R_{\mathrm{Th}}=(10\parallel30)+2.5=10\,\Omega'),
    S(r'Check with the short-circuit current.', r'i_{sc}=\frac{80}{10+(30\parallel2.5)}\cdot\frac{30}{32.5}=6\,\mathrm{A}=\frac{60}{10}')],
   r'$V_{\mathrm{Th}}=60\,\mathrm{V}$, $R_{\mathrm{Th}}=10\,\Omega$.', D.tb('4.65'))

n = C['p464']['net']
nm = {'p': '$p$', 'q': '$q$', 'a': '$a$', '0': '$b$'}
nms = {'p': '$p$', 'q': '$q$', 'a': '$a$, $b$ (shorted)', '0': '$a$, $b$ (shorted)'}
PR('p464', 'Try it 9 · Norton by a short (Textbook P4.64)', 'intermediate',
   r'Find the Norton equivalent at $a$–$b$.',
   fence('p464', [
       view([e for e in n if e[1] != 'R3'] + [SC()], [('I1', 0), ('R1', 1), ('R2', 2), ('SC', 3), ('R4', 4)], title='Short', gnd='low', names=nms,
            disp={'SC': SHORT}, notes=[r"The $12\,\Omega$ has both ends on the short (no fall, no current), so it is left out of this tab."], steps=[
           (r"Ground $q$, the lowest node: the pump pulls its $15\,\mathrm{A}$ out of $q$.", []),
           (r"A wire across $a$–$b$ shorts the $12\,\Omega$ (no fall). The $15\,\mathrm{A}$ splits: $8\,\Omega$, or $2+10=12\,\Omega$. The $12\,\Omega$ path gets $\dfrac{8}{20}(15)=6\,\mathrm{A}$, through the short: $I_N=6\,\mathrm{A}$.", ['eR2', 'eSC', 'eR4', 'eR1']),
           (r"Heights: $p=(9)(8)=72\,\mathrm{V}$; the $2\,\Omega$ falls $12\,\mathrm{V}$ to $a$, the $10\,\Omega$ falls $60\,\mathrm{V}$ to $q$.", ['p', 'a', 'z0']),
       ]),
       view(off(n) + [IT()], [('IT', 0), ('R3', 1), ('R2', 2), ('R1', 2), ('R4', 2), ('I1', 3)], title='Sources off, push 1 A', names=nm, terminals={'a'},
            disp={'I1': OFFI(15), 'IT': TEST}, steps=[
           (r"Ground $b$ (nothing dips below it now). The pump becomes a gap.", []),
           (r"Push $1\,\mathrm{A}$ into $a$. Two ways down: the $12\,\Omega$, or $2+8+10=20\,\Omega$. $12\parallel20=7.5\,\Omega$, so $a$ climbs $7.5\,\mathrm{V}$: $R_N=7.5\,\Omega$.", ['a', 'p', 'q', 'eR1', 'eR2', 'eR3', 'eR4', 'eIT']),
       ]),
       view(n, [('I1', 0), ('R1', 1), ('R2', 2), ('R3', 2), ('R4', 2)], title='Open (check)', gnd='low', names=nm, terminals={'a'}, steps=[
           (r"Ground $q$ again (lowest).", []),
           (r"Open: $15\,\mathrm{A}$ splits $8$ vs $2+12+10=24\,\Omega$, so $3.75\,\mathrm{A}$ goes through the $12\,\Omega$: $v_{ab}=45\,\mathrm{V}=(6)(7.5)$ ✓.", ['a', 'z0', 'p', 'eR1', 'eR2', 'eR3', 'eR4']),
       ]),
   ]),
   [S(r'Short: current divider between $8\,\Omega$ and $2+10\,\Omega$.', r'I_N=15\cdot\frac{8}{8+12}=6\,\mathrm{A}'),
    S('Pump off (a gap).', r'R_N=12\parallel(2+8+10)=7.5\,\Omega'),
    S('Check.', r'v_{oc}=I_NR_N=45\,\mathrm{V}=(3.75)(12)')],
   r'$I_N=6\,\mathrm{A}$ (toward $a$) ∥ $R_N=7.5\,\Omega$.', D.tb('4.64'))

n = C['p466']['net']
nm = {'s': 'battery top', 'm': '$m$', 'a': '$a$', '0': '$b$'}
PR('p466', 'Try it 10 · Norton with a bypass (Textbook P4.66)', 'intermediate',
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

n = C['p467']['net']
nm = {'n': 'battery top', 'a': '$a$', '0': '$b$'}
PR('p467', 'Try it 11 · Norton when a battery fixes a wire (Textbook P4.67)', 'intermediate',
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

eq69 = lambda rl: [('V', 'VT', 't', '0', 75), ('R', 'RT', 't', 'a', 10e3), ('R', 'RL', 'a', '0', rl)]  # noqa: E731
nm = {'t': 'inside: top of the step', 'a': '$a$', '0': '$b$'}
PR('p469', 'Try it 12 · Thévenin from two measurements (Textbook P4.69)', 'intermediate',
   r'A box holds an unknown linear circuit. A $15\,\mathrm{k\Omega}$ load on $a$–$b$ reads $v_{ab}=45\,\mathrm{V}$; a $5\,\mathrm{k\Omega}$ load reads $25\,\mathrm{V}$. Find the Thévenin equivalent.',
   fence('p469', [
       view(eq69(15e3), [('VT', 0), ('RT', 1), ('RL', 1)], title='15 kΩ load', unit='mA', names=nm, terminals={'a'},
            disp={'VT': ('V', r'$V_{\mathrm{Th}}$: $75\,\mathrm{V}$'), 'RT': ('R', r'$R_{\mathrm{Th}}$: falls $30\,\mathrm{V}$')}, steps=[
           (r"Ground $b$. The box is drawn as its answer: one step and one slope.", []),
           (r"The $15\,\mathrm{k\Omega}$ load sits at $45\,\mathrm{V}$, so it draws $\dfrac{45}{15}=3\,\mathrm{mA}$.", ['eRL']),
           (r"Tab 2: the $5\,\mathrm{k\Omega}$ draws $\dfrac{25}{5}=5\,\mathrm{mA}$. $2\,\mathrm{mA}$ more made $a$ sag $20\,\mathrm{V}$: $R_{\mathrm{Th}}=10\,\mathrm{k\Omega}$.", ['eRT']),
           (r"Open height: $45+(3)(10)=75\,\mathrm{V}=V_{\mathrm{Th}}$.", ['t', 'eVT']),
       ]),
       view(eq69(5e3), [('VT', 0), ('RT', 1), ('RL', 1)], title='5 kΩ load', unit='mA', names=nm, terminals={'a'},
            disp={'VT': ('V', r'$V_{\mathrm{Th}}$: $75\,\mathrm{V}$'), 'RT': ('R', r'$R_{\mathrm{Th}}$: falls $50\,\mathrm{V}$')},
            notes=[r"Same step and slope as tab 1. More current, more sag: $50\,\mathrm{V}$ lost inside, $25\,\mathrm{V}$ left at $a$."]),
   ]),
   [S('Load currents.', r'i_1=\frac{45}{15}=3\,\mathrm{mA},\qquad i_2=\frac{25}{5}=5\,\mathrm{mA}'),
    S(r'Two points on $v=V_{\mathrm{Th}}-R_{\mathrm{Th}}i$ (kΩ, mA).', r'\begin{aligned}45&=V_{\mathrm{Th}}-3R_{\mathrm{Th}}\\25&=V_{\mathrm{Th}}-5R_{\mathrm{Th}}\end{aligned}'),
    S('Subtract.', r'R_{\mathrm{Th}}=10\,\mathrm{k\Omega},\qquad V_{\mathrm{Th}}=75\,\mathrm{V}')],
   r'$V_{\mathrm{Th}}=75\,\mathrm{V}$, $R_{\mathrm{Th}}=10\,\mathrm{k\Omega}$.', D.tb('4.68'))


n = C['p468']['net']
nm = {'s': 'source top', 'm': '$m$', 'a': '$a$', '0': '$b$'}
PR('p468', 'Try it 13 · A pump that feeds back (Textbook P4.68)', 'intermediate',
   r'Find the Thévenin equivalent at $a$–$b$.',
   fence('p468', [
       view(n, [('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2), ('R4', 3), ('I1', 4)], title='Open', names=nm, terminals={'a'}, steps=[
           (r"Ground $b$. The source fixes its top at $300\,\mathrm{V}$.", []),
           (r"Two unknown heights, $m$ and $a$. KCL: $\dfrac{m-300}{40}+\dfrac{m}{8}+\dfrac{m-a}{10}=0$ and $\dfrac{a-300}{150}+\dfrac{a-m}{10}+3=0$. So $m=42$, $a=30\,\mathrm{V}=V_{\mathrm{Th}}$.", ['m', 'a']),
           (r"$1.2+1.8=3\,\mathrm{A}$ arrive at $a$, and the pump lifts all of it back to the top: $810\,\mathrm{W}$ delivered.", ['eR1', 'eR2', 'eR3', 'eR4', 'eV1', 'eI1']),
       ]),
       view(off(n) + [IT()], [('IT', 0), ('R4', 1), ('R3', 2), ('R1', 3), ('V1', 3), ('R2', 4), ('I1', 5)], title='Sources off, push 1 A', names=nm, terminals={'a'},
            disp={'V1': OFFV(300), 'I1': OFFI(3), 'IT': TEST}, steps=[
           (r"Same ground. $300\,\mathrm{V}$ → a wire, $3\,\mathrm{A}$ → a gap.", []),
           (r"Push $1\,\mathrm{A}$ into $a$. Two ways down: the $150\,\Omega$, or $10\,\Omega$ then $40\parallel8=6.67\,\Omega$. $150\parallel16.67=15\,\Omega$.", ['m', 'eR1', 'eR2', 'eR3', 'eR4', 'eV1']),
           (r"$a$ sits at $15\,\mathrm{V}$: $R_{\mathrm{Th}}=15\,\Omega$.", ['a', 'eIT']),
       ]),
   ]),
   [S('Open: KCL at $m$ and $a$.', r'\begin{aligned}\tfrac{m-300}{40}+\tfrac{m}{8}+\tfrac{m-a}{10}&=0\\\tfrac{a-300}{150}+\tfrac{a-m}{10}+3&=0\end{aligned}\;\Rightarrow\;a=30\,\mathrm{V}'),
    S('Sources off.', r'R_{\mathrm{Th}}=150\parallel\big(10+(40\parallel8)\big)=150\parallel16.67=15\,\Omega')],
   r'$V_{\mathrm{Th}}=30\,\mathrm{V}$, $R_{\mathrm{Th}}=15\,\Omega$.', D.tb('4.68'))

n = C['p477']['net']
nm = {'s': '$s$', 'p': '$p$', 'a': '$a$', 'b': '$b$', '0': 'bottom'}
PR('p477', 'Try it 14 · Thévenin two ways (Textbook P4.77)', 'intermediate',
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

H(1, 'Practice set')
P('Exam-style, mixing both topics. Try each for 10–15 minutes before opening the solution, then check your picture against the height view.')

n = C['p463']['net']
PR('p463', 'Textbook P4.63 · Swaps, then every power', 'advanced',
   r'**(a)** Use source transformations to find $v_o$. **(b)** Find the power developed by the $340\,\mathrm{V}$ source and **(c)** by the $5\,\mathrm{A}$ source. **(d)** Check the power balance.',
   fence('p463', [view(n, [('V1', 0), ('R3', 1), ('R1', 2), ('R2', 2), ('R6', 2), ('R5', 2), ('R4', 2), ('I1', 3)], gnd='low',
                       names={'p': 'pump top', 'q': '$q$', '0': 'bottom-left', 'm': '$m$', 's': '$v_o$ +', 'r': '$r$'}, steps=[
       (r"Ground $r$, the lowest node (the $340\,\mathrm{V}$ source's $-$ end). Moving ground changes no answer.", []),
       (r"Drop the $8\,\Omega$ (series with the pump) and the $80\,\Omega$ (across the $340\,\mathrm{V}$). Swap $5\,\mathrm{A}$ ∥ $20\,\Omega$ for $100\,\mathrm{V}$ + $20\,\Omega$. One loop: $100-340=80i$, so $i=-3\,\mathrm{A}$: $3\,\mathrm{A}$ runs counter-clockwise.", ['eR4', 'eR5', 'eR6']),
       (r"Climb from $r$ against that current: $5\,\Omega$ ($15\,\mathrm{V}$), $45\,\Omega$ ($135\,\mathrm{V}$) to $m=150$, $10\,\Omega$ ($30\,\mathrm{V}$) to the bottom-left wire at $180$. So $v_o=15-150=-135\,\mathrm{V}$.", ['s', 'm', 'z0']),
       (r"Original circuit: the $20\,\Omega$ carries $5+3=8\,\mathrm{A}$, so $q=180+160=340$ ✓. The $8\,\Omega$ adds $40\,\mathrm{V}$: the pump lifts $5\,\mathrm{A}$ through $380-180=200\,\mathrm{V}$: $1000\,\mathrm{W}$.", ['p', 'eR1', 'eR2', 'eI1']),
       (r"The $340\,\mathrm{V}$ source lifts $3+4.25=7.25\,\mathrm{A}$ (the loop plus the $80\,\Omega$'s current): $2465\,\mathrm{W}$. Total $3465\,\mathrm{W}$ = the six falls.", ['eV1', 'eR3']),
   ])]),
   [S(r'Drop the $8\,\Omega$ and $80\,\Omega$; swap the pump.', r'5\times20=100\,\mathrm{V}'),
    S('One loop, clockwise.', r'\begin{aligned}100-340&=(20+5+45+10)\,i\;\Rightarrow\;i=-3\,\mathrm{A}\\v_o&=45i=-135\,\mathrm{V}\end{aligned}'),
    S(r'$340\,\mathrm{V}$ source.', r'i=3+\tfrac{340}{80}=7.25\,\mathrm{A},\qquad p=2465\,\mathrm{W}'),
    S(r'$5\,\mathrm{A}$ source.', r'v=20(8)+8(5)=200\,\mathrm{V},\qquad p=1000\,\mathrm{W}'),
    S('Balance.', r'2465+1000=3465=200+1280+1445+45+405+90')],
   r'**(a)** $v_o=-135\,\mathrm{V}$ **(b)** $2465\,\mathrm{W}$ **(c)** $1000\,\mathrm{W}$ **(d)** $3465\,\mathrm{W}$ both ways.', D.tb('4.63'))

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

n = C['p473']['net']
nm = {'q': '$q$', 'p': '$p$', 'a': '$a$', 's': '30 V top', '0': '$b$'}
cols473 = [('I1', 0), ('R3', 1), ('R1', 1), ('V1', 1), ('R2', 2), ('R4', 3), ('R5', 3)]
PR('p473', 'Textbook P4.73 · A voltmeter is a load', 'intermediate',
   r'A $100\,\mathrm{k\Omega}$ voltmeter measures $v_{ab}$. **(a)** What does it read? **(b)** What is the percentage error, $\dfrac{\text{measured}-\text{actual}}{\text{actual}}\times100$?',
   fence('p473', [
       view(n, cols473, title='No meter (actual)', unit='mA', names=nm, terminals={'a'}, steps=[
           (r"Ground $b$. The source fixes its top at $30\,\mathrm{V}$.", []),
           (r"Unknowns $p$ and $q$ ($a$ is a divider below $q$). KCL (mA, kΩ): $p=49.6$, $q=62.4\,\mathrm{V}$, so $a=\tfrac{10}{13}(62.4)=48\,\mathrm{V}=V_{\mathrm{Th}}$.", ['p', 'q', 'a']),
           (r"The pump lifts $8\,\mathrm{mA}$ to $62.4\,\mathrm{V}$. $1.96\,\mathrm{mA}$ falls back **into** the $30\,\mathrm{V}$ source.", ['eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eV1']),
       ]),
       view(n + [('R', 'RM', 'a', '0', 100e3)], cols473 + [('RM', 4)], title='100 kΩ meter attached', unit='mA', names=nm, terminals={'a'},
            disp={'RM': ('R', r'meter: falls $45.28\,\mathrm{V}$')}, steps=[
           (r"Same ground. Sources off: $10\parallel40=8$, $+4=12$, $+3=15$, $\parallel10$: $R_{\mathrm{Th}}=6\,\mathrm{k\Omega}$.", []),
           (r"The meter draws $\dfrac{48}{6+100}=0.453\,\mathrm{mA}$, so $a$ sags $(6)(0.453)=2.72\,\mathrm{V}$: it reads $45.28\,\mathrm{V}$.", ['a', 'eRM']),
           (r"Error: $\dfrac{45.28-48}{48}=-5.66\%$.", ['p', 'q', 'eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eV1']),
       ]),
   ]),
   [S(r'Thévenin at $a$–$b$ (node equations, then sources off).', r'V_{\mathrm{Th}}=48\,\mathrm{V},\qquad R_{\mathrm{Th}}=\big((10\parallel40)+4+3\big)\parallel10=6\,\mathrm{k\Omega}'),
    S('The meter is a load.', r'v_m=48\cdot\frac{100}{106}=45.28\,\mathrm{V}'),
    S('Error.', r'\frac{45.28-48}{48}\times100=-5.66\%')],
   r'**(a)** $45.28\,\mathrm{V}$ **(b)** $-5.66\%$', D.tb('4.72'))


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

D.save(os.path.join(HERE, 'w45', 'w4v3_blocks.json'))
