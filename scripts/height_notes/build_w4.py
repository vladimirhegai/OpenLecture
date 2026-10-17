"""Week 4 rewrite (height method, Full loop views) -> w45/w4_blocks.json"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from blocks45 import Doc, S  # noqa: E402
from w45lib import C, view, fence, plain, off  # noqa: E402

D = Doc('w4-v2', 4)
H, P, CO, L, T, EQ, SCH, EX, PR = D.H, D.P, D.CO, D.L, D.T, D.EQ, D.SCH, D.EX, D.PR
OFFV = lambda v: ('W', rf'${v}\,\mathrm{{V}}$ off: a wire')  # noqa: E731
OFFI = lambda i: ('S', rf'${i}\,\mathrm{{A}}$ off: a gap')  # noqa: E731
SHORT = ('W', 'short: no step')
TEST = ('I', r'test $1\,\mathrm{A}$')
SC = lambda a='a': ('V', 'SC', a, '0', 0)  # noqa: E731
IT = lambda a='a', amps=1: ('I', 'IT', '0', a, amps)  # noqa: E731

# =========================================================================== Overview
H(1, 'Overview')
CO('info', r"Three shortcuts this week. **Pick the cheaper method** (node or mesh). **Swap sources** ($V$ + series $R$ ⇄ $I$ ∥ $R$). **Shrink a circuit to two numbers** a load can see: $V_{\mathrm{Th}}$ and $R_{\mathrm{Th}}$. In heights, every shortcut keeps the **terminal heights** and throws away the inside ones.")
H(2, 'Topic map')
T(['#', 'Topic', 'Key result', 'In heights'], [
    ['1', 'Node or mesh?', 'count the equations first', 'a voltage source fixes a height; a current source fixes a mesh'],
    ['2', 'Source transformations', r'$v_s=Ri_s$', 'same terminal height for every load; inside heights change'],
    ['3', 'Thévenin and Norton', r'$V_{\mathrm{Th}}=v_{oc}$, $I_N=i_{sc}$, $R_{\mathrm{Th}}=\dfrac{V_{\mathrm{Th}}}{I_N}$', r'terminal $a$ sags $R_{\mathrm{Th}}$ volts per amp drawn'],
])
CO('tip', "**How to use this note.** Shaky on Week 3? Read **Start here**. Each topic: rules → example → **Try it** (answer on paper first). Every circuit has a **Height view** (Full loop) with **Walk me through it**. The **Summary** at the end is a one-read crash course.")

# =========================================================================== Start here
H(1, 'Start here: the only Week 3 you need')
T(['#', 'Rule', 'Picture it as'], [
    ['1', '**Node voltage = height** above the node you ground.', 'one floor per node'],
    ['2', '**Voltage source:** fixes a step. To ground, it fixes a height; between two unknown nodes, it is a rigid rod.', 'an escalator'],
    ['3', '**Current source:** fixes a current, never a height.', 'a pump'],
    ['4', r'**Unknown height → KCL there:** what flows in = what flows out. Resistor current $=\dfrac{\text{fall}}{R}$, always downhill.', 'pipes and slides'],
    ['5', '**Power** = current × height change. Climbing delivers, falling absorbs.', 'lifting vs dropping'],
])
EX('w4S', 'S · One unknown height',
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

# =========================================================================== Topic 1
H(1, 'Topic 1: Node or mesh?', D.oc('Topic 1: Choosing'))
L([r'**Node:** unknowns $=(n_e-1)$, minus every height a voltage source fixes. A supernode still saves one.',
   r'**Mesh:** unknowns $=(b_e-n_e+1)$, minus every mesh current a current source fixes. A supermesh saves one.',
   'A dependent source adds no unknown once its control is written in your unknowns.',
   'Tie-break: asked for a node voltage → node; asked for a branch current → mesh.'])
EQ(r'\begin{aligned}N_{\text{node}}&=(n_e-1)-(\text{fixed heights})\\N_{\text{mesh}}&=(b_e-n_e+1)-(\text{fixed meshes})\end{aligned}')
CO('warning', r"Count only **essential** nodes and branches. Elements in series are one essential branch.")
n = C['lec300']['net']
EX('lec300', 'Which method? Power in the 300 Ω (Lecture 4)',
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

# =========================================================================== Topic 2
H(1, 'Topic 2: Source transformations', D.oc('Topic 2: Source transformations'))
L([r'A voltage source $v_s$ **in series** with $R$ ⇄ a current source $i_s=\dfrac{v_s}{R}$ **in parallel** with the same $R$. The arrow points to the $+$ end.',
   r'**Same terminal height for every load.** The inside is different: never take a source\'s power from the swapped circuit.',
   r'$R$ **across** an ideal voltage source: changes no other height (drop it; it still burns power). $R$ **in series** with an ideal current source: changes only the height between them (drop it).',
   'Strategy: swap toward what you want; merge parallel current sources and series voltage sources; repeat; go back to the original for powers.'])
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
EX('stx', 'Same load, two forms',
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
n = C['lec250']['net']
EX('lec250', 'Swap, solve, go back (Lecture 4)',
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
n = C['p459']['net']
PR('p459', 'Try it 2 · Two pumps become one loop (Textbook P4.59)', 'intermediate',
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
PR('lecp9', 'Try it 3 · Is the 6 V source delivering? (Lecture 4)', 'intermediate',
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

# =========================================================================== Topic 3
H(1, 'Topic 3: Thévenin and Norton', D.oc('Topic 3: Thévenin and Norton'))
L([r'Seen from $a$–$b$, any linear circuit is **one step $V_{\mathrm{Th}}$ and one slope $R_{\mathrm{Th}}$**.',
   r'$V_{\mathrm{Th}}$ = height of $a$ with nothing attached. $I_N$ = current through a wire from $a$ to $b$.',
   r'$R_{\mathrm{Th}}=\dfrac{V_{\mathrm{Th}}}{I_N}$. Or: sources off (voltage → wire, current → gap), push $1\,\mathrm{A}$ into $a$, read $a$\'s height.',
   r'A load draws $i$, so $a$ **sags**: $v_{ab}=V_{\mathrm{Th}}-R_{\mathrm{Th}}i$. Norton = the source transformation: $I_N$ ∥ $R_{\mathrm{Th}}$.',
   r'Ground $b$, so $a$\'s height is $v_{ab}$ (if a node dips below $b$, ground the lowest node and subtract).',
   'Dependent sources inside? Keep them on. That is Week 5 Topic 1.'])
EQ(r'V_{\mathrm{Th}}=v_{oc},\qquad I_N=i_{sc},\qquad R_{\mathrm{Th}}=\frac{V_{\mathrm{Th}}}{I_N},\qquad v_{ab}=V_{\mathrm{Th}}-R_{\mathrm{Th}}\,i')
tp = [('V', 'V1', 't', '0', 32), ('R', 'R1', 't', 'a', 8)]
EX('thpic', 'The terminal sags',
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
n = C['lecth']['net']
nm = {'s': 'source top', 'n': '$v_1$', 'a': '$a$', '0': '$b$'}
EX('lecth', 'Open, short, sources off (Lecture 4)',
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
PR('p465', 'Try it 4 · A loaded divider (Textbook P4.65)', 'introductory',
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
PR('p464', 'Try it 5 · Norton by a short (Textbook P4.64)', 'intermediate',
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
eq69 = lambda rl: [('V', 'VT', 't', '0', 75), ('R', 'RT', 't', 'a', 10e3), ('R', 'RL', 'a', '0', rl)]  # noqa: E731
nm = {'t': 'inside: top of the step', 'a': '$a$', '0': '$b$'}
PR('p469', 'Try it 6 · Thévenin from two measurements (Textbook P4.69)', 'intermediate',
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

# =========================================================================== Practice
H(1, 'Practice problems')
P('Exam-style, each mixing topics. Give each a real try before opening the solution, then check your picture against the height view.')
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
n = C['p460']['net']
PR('p460', 'Textbook P4.60 · A pump across a resistor', 'intermediate',
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
n = C['p468']['net']
nm = {'s': 'source top', 'm': '$m$', 'a': '$a$', '0': '$b$'}
PR('p468', 'Textbook P4.68 · A pump that feeds back', 'intermediate',
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

# =========================================================================== Summary
H(1, 'Summary: Week 4 in one read')
CO('tip', r"Same picture as before: **voltage is height**. All three shortcuts keep the heights at the terminals and redraw the inside.")
H(2, 'A · Node or mesh?')
L([r'Count first: node $=(n_e-1)-$fixed heights; mesh $=(b_e-n_e+1)-$fixed meshes.',
   'Voltage sources favour node; current sources favour mesh. Pick the smaller count.'])
H(2, 'B · Swap sources')
L([r'$V$ + series $R$ ⇄ $\dfrac{V}{R}$ ∥ $R$. Arrow toward $+$.',
   r'Same $a$ for any load; different inside. Powers: go back to the original.'])
EX('w4A', 'B1 · Same terminal, two insides', r'Find $a$ with a $6\,\Omega$ load, before and after the swap.',
   fence('w4A', [
       view(C['w4A']['net'], [('V1', 0), ('R1', 1), ('R2', 1)], title='9 V + 3 Ω', names={'s': 'source top', 'a': '$a$', '0': '$b$'}, terminals={'a'}, steps=[
           (r"Ground $b$. One loop: $\dfrac{9}{3+6}=1\,\mathrm{A}$; the $3\,\Omega$ falls $3\,\mathrm{V}$, so $a=6\,\mathrm{V}$.", ['a', 'eR1', 'eR2']),
       ]),
       view([('I', 'Is', '0', 'a', 3), ('R', 'Rp', 'a', '0', 3), ('R', 'R2', 'a', '0', 6)], [('Is', 0), ('Rp', 1), ('R2', 2)], title='3 A ∥ 3 Ω',
            names={'a': '$a$', '0': '$b$'}, terminals={'a'}, steps=[
           (r"Same ground. $3\,\mathrm{A}$ into $3\parallel6=2\,\Omega$: $a=6\,\mathrm{V}$. Same height.", ['a', 'eRp', 'eR2']),
       ]),
   ], spoiler=False, inline=True),
   [S('Both forms.', r'a=9\cdot\frac{6}{9}=6\,\mathrm{V}=3\,(3\parallel6)')], r'$a=6\,\mathrm{V}$ both ways.')
H(2, 'C · Thévenin = one step + one slope')
L([r'Open: $a$ sits at $V_{\mathrm{Th}}$. Short: $I_N$ flows. $R_{\mathrm{Th}}=\dfrac{V_{\mathrm{Th}}}{I_N}$ = sag per amp.',
   r'Sources off (wire / gap), push $1\,\mathrm{A}$ in: $a$\'s height $=R_{\mathrm{Th}}$.'])
n = C['w4C']['net']
nm = {'s': 'source top', 'a': '$a$', '0': '$b$'}
EX('w4C', 'C1 · All three tabs', r'Find $V_{\mathrm{Th}}$, $I_N$ and $R_{\mathrm{Th}}$ at $a$–$b$.',
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
H(2, 'Which part do I need? (practice problem map)')
T(['Problem', 'Use', 'First move'], [
    ['Try it 1 · P4.54', 'A', r'Pump fixes one mesh: 2 mesh equations.'],
    ['Try its 2–3 · P4.59, Lecture p.9', 'B', 'Swap pumps ⇄ batteries until one loop or one node is left.'],
    ['Try its 4–6 · P4.65, P4.64, P4.69', 'C', r'Open → $V_{\mathrm{Th}}$; short → $I_N$; sources off → $R_{\mathrm{Th}}$; two loads → two points on the sag line.'],
    ['P4.63 · Swaps, then every power', 'B', 'Drop the 8 Ω and 80 Ω; one loop; then back to the original.'],
    ['P4.60 · A pump across a resistor', 'B', r'Swap both pumps; averaging at $r$.'],
    ['P4.68 · A pump that feeds back', 'C', r'Two KCLs for $V_{\mathrm{Th}}$; sources off for $R_{\mathrm{Th}}$.'],
    ['P4.73 · A voltmeter is a load', 'C', 'Thévenin first; the meter sags the terminal.'],
])
CO('warning', r"**Traps.** (1) Swapped circuit → terminal values only, never inside powers. (2) Arrow points to the $+$ end. (3) Sources off: voltage → wire, current → gap; dependent sources stay on. (4) $v_{ab}$ is $+$ at $a$; $i_{sc}$ flows $a\to b$ through the short. (5) A source with no series/parallel $R$ can't be swapped.")
H(2, 'Formula sheet')
T(['Result', 'Formula', 'In heights'], [
    ['Equation count', r'$N_{\text{node}}=(n_e-1)-$fixed; $N_{\text{mesh}}=(b_e-n_e+1)-$fixed', 'fixed heights / fixed meshes'],
    ['Source swap', r'$i_s=\dfrac{v_s}{R}$, $v_s=Ri_s$', 'same terminal height'],
    ['Thévenin voltage', r'$V_{\mathrm{Th}}=v_{oc}$', 'open height of $a$'],
    ['Norton current', r'$I_N=i_{sc}=\dfrac{V_{\mathrm{Th}}}{R_{\mathrm{Th}}}$', '$a$ pulled down to $b$'],
    ['Thévenin resistance', r'$R_{\mathrm{Th}}=\dfrac{v_{oc}}{i_{sc}}$, or sources off', 'sag per amp; height for a 1 A push'],
    ['Loaded terminal', r'$v_{ab}=V_{\mathrm{Th}}-R_{\mathrm{Th}}i=V_{\mathrm{Th}}\dfrac{R_L}{R_{\mathrm{Th}}+R_L}$', 'the sag'],
])

D.save(os.path.join(HERE, 'w45', 'w4_blocks.json'))
