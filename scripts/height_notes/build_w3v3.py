"""Week 3, v3 layout: height-method card, 2 topics (example ladders + Try its), practice set, cheat sheet."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import circuits3  # noqa: E402,F401  (adds the new circuits to circuits.C)
from blocks45 import Doc, S  # noqa: E402
from circuits import C  # noqa: E402
from w45lib import view, fence_c  # noqa: E402
from weekkit import card  # noqa: E402

D = Doc('w3-v3', 3, 'w3_now.json')
H, P, CO, L, T, EQ = D.H, D.P, D.CO, D.L, D.T, D.EQ


def intro(prefix):
    return D.ob(prefix)['prompt'].split('```schematic')[0].strip()


def old(prefix):
    b = D.ob(prefix)
    return b['steps'], b['answer']


def EX(key, title, text, views, steps, answer, cites=()):
    D.EX(key, title, text, fence_c(C, key, views, spoiler=False, inline=True), steps, answer, cites)


def TRY(key, title, diff, text, views, steps, answer, cites):
    D.PR(key, title, diff, text, fence_c(C, key, views), steps, answer, cites)


def V(key, cols, steps, **kw):
    return view(C[key]['net'], cols, steps=steps, **kw)


# =========================================================================== card
card(D, "**Week 3 in one line:** two step-by-step ways to find every voltage in a big circuit. "
        "**Node voltages** = give each unknown height a letter and use in = out. **Mesh currents** = give each window a loop current and use climbs = falls.",
     "**node voltages are just heights.** The whole node-voltage method is the recipe above, done carefully.")
EX('S1', 'Example 0 · The recipe on one small circuit', 'Find the height of $x$, every current, and the power of each source.',
   [V('S1', [('V1', 0), ('R1', 1), ('R2', 1), ('I1', 2)], names={'t': 'top', 'x': '$x$', '0': 'ground'}, steps=[
       (r"① Ground: the bottom wire is $0\,\mathrm{V}$.", []),
       (r"② The battery lifts its top to $10\,\mathrm{V}$.", ['t', 'eV1']),
       (r"③ One unknown height, $x$. The pump pushes $1\,\mathrm{A}$ into it. In = out at $x$: in from the $2\,\Omega$ slide, $\dfrac{10-x}{2}$, plus the pump's $1\,\mathrm{A}$; out down the $4\,\Omega$, $\dfrac{x}{4}$.", ['eI1']),
       (r"④ Solve $\dfrac{10-x}{2}+1=\dfrac{x}{4}$: $x=8\,\mathrm{V}$.", ['x']),
       (r"⑤ Currents = fall ÷ R: the $2\,\Omega$ falls $2\,\mathrm{V}$ ($1\,\mathrm{A}$), the $4\,\Omega$ falls $8\,\mathrm{V}$ ($2\,\mathrm{A}$). In = out: $1+1=2$ ✓", ['eR1', 'eR2']),
       (r"⑥ Power: the battery lifts $1\,\mathrm{A}$ by $10\,\mathrm{V}$ ($10\,\mathrm{W}$), the pump lifts $1\,\mathrm{A}$ by $8\,\mathrm{V}$ ($8\,\mathrm{W}$). The slides use $2+16=18\,\mathrm{W}$ ✓", []),
   ])],
   [S(r'In = out at $x$.', r'\frac{10-x}{2}+1=\frac{x}{4}\;\Rightarrow\;x=8\,\mathrm{V}'),
    S('Power: climbs = falls.', r'(10)(1)+(8)(1)=18\,\mathrm{W}=(2)(1)+(8)(2)')],
   r'$x=8\,\mathrm{V}$; $1\,\mathrm{A}$ and $2\,\mathrm{A}$; the battery gives $10\,\mathrm{W}$, the pump $8\,\mathrm{W}$.')

# =========================================================================== Topic 1
H(1, 'Topic 1: Node voltages are heights', D.oc('Topic 2: The node-voltage'))
CO('tip', "**How it looks in heights.**\n\n"
          "- Every unknown wire gets a letter (its height). At each one: **in = out**, with every slide's current $=\\dfrac{\\text{fall}}{R}$.\n"
          "- A battery from ground gives a height for free. A pump never fixes a height; it pushes current in (up) or pulls it out (down).\n"
          "- A battery (or diamond) **between two unknown wires** locks them a fixed distance apart. Draw a **bubble** around both and write in = out for the whole bubble (a *supernode*).\n"
          "- A **diamond**: first write the thing it depends on using your letters.")
EX('N1', 'Example 1 · One pump, two slides', r'Find the height of $x$ and the current in each resistor.',
   [V('N1', [('I1', 0), ('R1', 1), ('R2', 2)], names={'x': '$x$', '0': 'ground'}, steps=[
       (r"Ground the bottom wire. No battery here, only a pump.", []),
       (r"The pump pushes $3\,\mathrm{A}$ up into $x$. All of it has to slide back down through the $4\,\Omega$ and the $12\,\Omega$.", ['eI1']),
       (r"In = out at $x$: $3=\dfrac{x}{4}+\dfrac{x}{12}=\dfrac{x}{3}$, so $x=9\,\mathrm{V}$.", ['x']),
       (r"Currents = fall ÷ R: $\dfrac94=2.25\,\mathrm{A}$ and $\dfrac{9}{12}=0.75\,\mathrm{A}$. The easier slide (smaller $R$) takes more.", ['eR1', 'eR2']),
       (r"Power: the pump lifts $3\,\mathrm{A}$ by $9\,\mathrm{V}=27\,\mathrm{W}$; the slides use $20.25+6.75=27\,\mathrm{W}$ ✓", []),
   ])],
   [S(r'In = out at $x$.', r'3=\frac{x}{4}+\frac{x}{12}\;\Rightarrow\;x=9\,\mathrm{V}')],
   r'$x=9\,\mathrm{V}$; $2.25\,\mathrm{A}$ in the $4\,\Omega$, $0.75\,\mathrm{A}$ in the $12\,\Omega$.')
s, a = old('One node, three neighbours')
EX('lec_one', 'Example 2 · A battery and a pump feed one wire (Lecture 3)', intro('One node, three neighbours'),
   [V('lec_one', [('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2), ('I1', 3)], names={'s': 'battery top', 'a': '$a$', '0': 'ground'}, steps=[
       (r"Ground the bottom wire. The battery lifts its top to $50\,\mathrm{V}$.", []),
       (r"One unknown height, $a$. In = out at $a$: in from the $5\,\Omega$, $\dfrac{50-a}{5}$, plus the pump's $3\,\mathrm{A}$; out down the $10\,\Omega$ and $40\,\Omega$.", []),
       (r"$\dfrac{50-a}{5}+3=\dfrac{a}{10}+\dfrac{a}{40}$, so $a=40\,\mathrm{V}$.", ['a']),
       (r"Currents = fall ÷ R: $i_a=\dfrac{10}{5}=2$, $i_b=\dfrac{40}{10}=4$, $i_c=\dfrac{40}{40}=1\,\mathrm{A}$. In = out: $2+3=4+1$ ✓", ['eR1', 'eR2', 'eR3', 'eV1', 'eI1']),
       (r"Power: battery $2\times50=100\,\mathrm{W}$, pump $3\times40=120\,\mathrm{W}$; the slides use $20+160+40=220\,\mathrm{W}$.", []),
   ])], s, a, D.oc('One node, three neighbours'))
EX('A1', 'Example 3 · Two batteries pull on one wire', r'Find the height of $x$.',
   [V('A1', [('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2), ('V2', 2)], names={'s': 'left top', 'x': '$x$', 'r': 'right top', '0': 'ground'}, steps=[
       (r"Ground the bottom wire. Left battery top: $12\,\mathrm{V}$. Right battery top: $6\,\mathrm{V}$.", []),
       (r"$x$ is joined by slides to $12\,\mathrm{V}$ ($2\,\Omega$), to $0$ ($4\,\Omega$) and to $6\,\mathrm{V}$ ($4\,\Omega$). In = out: $\dfrac{12-x}{2}=\dfrac{x}{4}+\dfrac{x-6}{4}$, so $x=7.5\,\mathrm{V}$.", ['x']),
       (r"$x$ always lands **between** its neighbours, closest to the one with the smallest $R$ (that slide pulls hardest). Here: closest to $12\,\mathrm{V}$.", []),
       (r"Currents: $2.25\,\mathrm{A}$ in from the left, $1.875\,\mathrm{A}$ down, $0.375\,\mathrm{A}$ on to the right, where it falls **into** the $6\,\mathrm{V}$ battery (that battery absorbs).", ['eR1', 'eR2', 'eR3', 'eV1', 'eV2']),
   ])],
   [S(r'In = out at $x$.', r'\frac{12-x}{2}=\frac{x}{4}+\frac{x-6}{4}\;\Rightarrow\;x=7.5\,\mathrm{V}')],
   r'$x=7.5\,\mathrm{V}$, between $6$ and $12\,\mathrm{V}$ and closest to $12\,\mathrm{V}$.')
s, a = old('Two unknown heights')
EX('lec_two', 'Example 4 · Two unknown heights (Lecture 3)', intro('Two unknown heights'),
   [V('lec_two', [('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2), ('R4', 3), ('I1', 4)], names={'s': 'battery top', 'n1': 'node 1', 'n2': 'node 2', '0': 'ground'},
      refs={'R2': ('n1', '$v_1$'), 'R4': ('n2', '$v_2$')}, steps=[
       (r"Ground the bottom wire. The battery lifts its top to $10\,\mathrm{V}$.", []),
       (r"Two unknown heights, $v_1$ and $v_2$: one in = out for each. Node 1: $\dfrac{10-v_1}{1}+\dfrac{v_2-v_1}{2}=\dfrac{v_1}{5}$. Node 2: $2=\dfrac{v_2-v_1}{2}+\dfrac{v_2}{10}$.", []),
       (r"Solve the pair: $v_1=9.09\,\mathrm{V}$, $v_2=10.91\,\mathrm{V}$. Node 2 is **higher than the battery**: the pump pushed it up there.", ['n1', 'n2']),
       (r"Currents = fall ÷ R: $0.909\,\mathrm{A}$ from the battery, $1.818\,\mathrm{A}$ down the $5\,\Omega$, $0.909\,\mathrm{A}$ from node 2 **back** to node 1, $1.091\,\mathrm{A}$ down the $10\,\Omega$.", ['eR1', 'eR2', 'eR3', 'eR4', 'eV1', 'eI1']),
       (r"Power: battery $9.09\,\mathrm{W}$ + pump $2\times10.91=21.82\,\mathrm{W}$ = what the four slides use.", []),
   ])], s, a, D.oc('Two unknown heights'))
s, a = old('A source to ground fixes')
EX('lec_known', 'Example 5 · A battery from ground gives a height for free (Lecture 3)', intro('A source to ground fixes'),
   [V('lec_known', [('V1', 0), ('R1', 1), ('R2', 2), ('R3', 3), ('I1', 4)], names={'n1': 'node 1', 'n2': 'node 2', '0': 'ground'},
      refs={'R1': ('n1', '$v_1$'), 'R3': ('n2', '$v_2$')}, steps=[
       (r"Ground the bottom wire. The $100\,\mathrm{V}$ battery goes straight from ground to node 1: $v_1=100\,\mathrm{V}$, no equation needed.", ['n1']),
       (r"Only $v_2$ is unknown. In = out at node 2: $5=\dfrac{v_2-100}{10}+\dfrac{v_2}{50}$, so $v_2=125\,\mathrm{V}$.", ['n2']),
       (r"Currents: $2.5\,\mathrm{A}$ slides from node 2 down to node 1 and $2.5\,\mathrm{A}$ down the $50\,\Omega$. Node 1 sends $4\,\mathrm{A}$ down the $25\,\Omega$, so the battery only adds $1.5\,\mathrm{A}$.", ['eR1', 'eR2', 'eR3', 'eV1', 'eI1']),
       (r"Power: battery $1.5\times100=150\,\mathrm{W}$ + pump $5\times125=625\,\mathrm{W}$ = slides $400+62.5+312.5=775\,\mathrm{W}$ ✓", []),
   ])], s, a, D.oc('A source to ground fixes'))
s, a = old('Two pumps, no battery')
EX('multi', 'Example 6 · Two pumps, no battery: ground the lowest wire', intro('Two pumps, no battery'),
   [V('multi', [('R1', 0), ('I1', 1), ('R2', 2), ('I2', 3), ('R3', 4), ('R4', 5)], gnd='n1', unit='mA',
      names={'n1': 'node 1', 'n2': 'node 2', '0': 'bottom wire'}, refs={'R1': ('n1', '$V_1$')}, steps=[
       (r"Ground **node 1**, the lowest wire (step 2 shows why). Moving ground never changes an answer: $V_1$ is still node 1 measured from the bottom wire.", []),
       (r"Read the pumps: both pull current **out of** their node and push it into the bottom wire. That current must slide back down to the nodes, so the bottom wire sits **above** both of them.", ['eI1', 'eI2']),
       (r"In = out at each node (mA, kΩ, measured from the bottom wire): $\dfrac{V_1}{3}+6+\dfrac{V_1-V_2}{2}=0$ and $\dfrac{V_2-V_1}{2}+4+\dfrac{V_2}{2}+\dfrac{V_2}{2}=0$. So $V_1=-11$, $V_2=-6.33\,\mathrm{V}$: here the bottom wire is $11\,\mathrm{V}$ up and node 2 is $4.67\,\mathrm{V}$ up.", ['z0', 'n2']),
       (r"Currents = fall ÷ R: $3.67\,\mathrm{mA}$ slides from the bottom wire to node 1, $2.33\,\mathrm{mA}$ from node 2 to node 1, $3.17\,\mathrm{mA}$ in each right $2\,\mathrm{k\Omega}$. All flow **up** the drawing, so $I_1=-3.67$, $I_2=-2.33$, $I_3=I_4=-3.17\,\mathrm{mA}$.", ['eR1', 'eR2', 'eR3', 'eR4']),
       (r"Power: both pumps lift current up to the bottom wire ($66+25.3=91.3\,\mathrm{mW}$); the slides use the same.", []),
   ])], s, a)
s, a = old('Three pumps, two of them')
EX('multi2', 'Example 7 · Three pumps, two of them absorbing', intro('Three pumps, two of them'),
   [V('multi2', [('R2', 0), ('R1', 0), ('I1', 1), ('I3', 1), ('I2', 2), ('R3', 3), ('R4', 4)], unit='mA',
      names={'a': '$a$ (top)', 'b': '$b$ (middle)', '0': 'ground'}, steps=[
       (r"Ground the bottom wire. No battery, so no height is given: $a$ (top wire) and $b$ (middle wire) are both unknown.", []),
       (r"Read the pumps: $6\,\mathrm{mA}$ pushed up into $b$; $4\,\mathrm{mA}$ moved from $b$ to $a$; $2\,\mathrm{mA}$ drained from $a$ to ground.", ['eI1', 'eI2', 'eI3']),
       (r"In = out (mA, kΩ). At $a$: $4=\dfrac{a}{2}+\dfrac{a-b}{4}+2$. At $b$: $6=\dfrac{b-a}{4}+\dfrac{b}{12}+\dfrac{b}{4}+4$. So $a=4.44$, $b=5.33\,\mathrm{V}$.", ['a', 'b']),
       (r"$I_0=\dfrac{5.33}{12}=0.444\,\mathrm{mA}$. And $b$ is above $a$, so $0.222\,\mathrm{mA}$ slides from $b$ to $a$.", ['eR1', 'eR2', 'eR3', 'eR4']),
       (r"Power: only the $6\,\mathrm{mA}$ pump climbs ($32\,\mathrm{mW}$). The other two carry current **downhill**, so they absorb.", []),
   ])], s, a)
EX('B1', 'Example 8 · A battery between two unknown wires: the bubble', r'Find $p$ and $q$.',
   [V('B1', [('I1', 0), ('R1', 1), ('V1', 2), ('R2', 3)], names={'p': '$p$', 'q': '$q$', '0': 'ground'}, steps=[
       (r"Ground the bottom wire. The $6\,\mathrm{V}$ battery sits between $p$ and $q$, and **neither** is known. It locks them: $q=p+6$, always.", []),
       (r"So draw a bubble around $p$ and $q$ and treat it as one wire. In = out for the bubble: the pump pushes $3\,\mathrm{A}$ in; it leaves down the $2\,\Omega$ and the $4\,\Omega$: $3=\dfrac{p}{2}+\dfrac{p+6}{4}$, so $p=2$, $q=8\,\mathrm{V}$.", ['p', 'q']),
       (r"Currents: $1\,\mathrm{A}$ down the $2\,\Omega$, $2\,\mathrm{A}$ down the $4\,\Omega$. The other $2\,\mathrm{A}$ climbs through the battery from $p$ to $q$. (The battery's own current never goes into the bubble equation: it stays inside.)", ['eR1', 'eR2', 'eV1', 'eI1']),
   ])],
   [S('Bubble (supernode): the battery fixes the difference; in = out for the bubble.', r'q=p+6,\qquad 3=\frac{p}{2}+\frac{p+6}{4}\;\Rightarrow\;p=2\,\mathrm{V},\;q=8\,\mathrm{V}')],
   r'$p=2\,\mathrm{V}$, $q=8\,\mathrm{V}$')
s, a = old('A dependent source: control')
EX('lec_dep', 'Example 9 · A diamond: find what it depends on first (Lecture 3)', intro('A dependent source: control'),
   [V('lec_dep', [('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2), ('R4', 2), ('R5', 3), ('E1', 3)], elabel={'E1': r'$8i_\Phi$'},
      names={'s': 'battery top', 'a': '$a$', 'b': '$b$', 'c': '$c$', '0': 'ground'}, steps=[
       (r"Ground the bottom wire. The $20\,\mathrm{V}$ battery lifts its top to $20\,\mathrm{V}$.", []),
       (r"The diamond is a battery of $8i_\Phi$ volts from ground to $c$. It depends on $i_\Phi$, the current in the $5\,\Omega$: $i_\Phi=\dfrac{a-b}{5}$. So $c=8i_\Phi=1.6(a-b)$.", []),
       (r"Unknowns $a$ and $b$ (with $c=1.6(a-b)$). In = out at $a$ and at $b$ gives $a=16\,\mathrm{V}$, $b=10\,\mathrm{V}$.", ['a', 'b']),
       (r"Now the diamond: $i_\Phi=\dfrac{16-10}{5}=1.2\,\mathrm{A}$, so $c=8(1.2)=9.6\,\mathrm{V}$.", ['c', 'eR3', 'eE1']),
       (r"The rest: $2\,\mathrm{A}$ from the battery, $0.8$ and $1\,\mathrm{A}$ down the $20\,\Omega$ and $10\,\Omega$, $0.2\,\mathrm{A}$ from $b$ to $c$ that then falls through the diamond (it absorbs). The $5\,\Omega$ uses $1.2\times6=7.2\,\mathrm{W}$.", ['eR1', 'eR2', 'eR4', 'eR5', 'eV1']),
   ])], s, a, D.oc('A dependent source: control'))
s, a = old('A supernode is a rigid rod')
EX('lec_super', 'Example 10 · A bubble with a diamond inside (Lecture 3)', intro('A supernode is a rigid rod'),
   [V('lec_super', [('I1', 0), ('R4', 1), ('E1', 2), ('R3', 2), ('R2', 3), ('R1', 3), ('V1', 4)], elabel={'E1': r'$10i_\Phi$'},
      names={'a': '$a$', 'b': '$b$', 'c': '$c$', '0': 'ground'}, steps=[
       (r"Ground the bottom wire. The $50\,\mathrm{V}$ battery fixes $a=50\,\mathrm{V}$.", ['a']),
       (r"The diamond ($10i_\Phi$) sits between $b$ and $c$, both unknown: it locks $c=b+10i_\Phi$. It depends on $i_\Phi$, the current from $b$ to $a$ through $5\,\Omega$: $i_\Phi=\dfrac{b-50}{5}$. So $c=3b-100$.", []),
       (r"Bubble around $b$ and $c$. In = out for the bubble: the $4\,\mathrm{A}$ pump comes in; out go $\dfrac{b-50}{5}$, $\dfrac{b}{50}$ and $\dfrac{c}{100}$. So $b=60$, $c=80\,\mathrm{V}$.", ['b', 'c', 'eE1']),
       (r"Currents: $i_\Phi=2\,\mathrm{A}$ from $b$ to $a$, $1.2\,\mathrm{A}$ down the $50\,\Omega$, $0.8\,\mathrm{A}$ down the $100\,\Omega$. The other $3.2\,\mathrm{A}$ goes **down** through the diamond (it absorbs).", ['eR2', 'eR3', 'eR4', 'eI1']),
       (r"At $a$: $2\,\mathrm{A}$ arrives, the $40\,\Omega$ takes $1.25\,\mathrm{A}$, so $0.75\,\mathrm{A}$ falls into the $50\,\mathrm{V}$ battery (it absorbs). Only the pump climbs: $4\times80=320\,\mathrm{W}$.", ['eR1', 'eV1']),
   ])], s, a, D.oc('A supernode is a rigid rod'))
CO('warning', "**Bubble traps.** The two wires in a bubble are **not** equal: they differ by the battery's $V$. The battery's own current never appears in the bubble's in = out. And a diamond's control arrow decides the sign: $\\dfrac{b-a}{R}$ is not $\\dfrac{a-b}{R}$.")

# ---- Try its, Topic 1
TRY('p46', 'Try it 1 · How much does the pump take? (Textbook P4.6)', 'introductory',
    r'Use the node-voltage method to find how much power the $2\,\mathrm{A}$ source extracts from the circuit.',
    [V('p46', [('I1', 0), ('R1', 1), ('R3', 2), ('R2', 3), ('V1', 4)], gnd='low', names={'a': '$a$', 'c': 'battery top', 'd': '$d$', '0': 'bottom-left'}, steps=[
        (r"Ground $d$, the lowest wire (the $55\,\mathrm{V}$ battery's $-$ end). Answers are still read from the bottom-left wire.", []),
        (r"The right side is one path: $a$ → $2\,\Omega$ → battery → $3\,\Omega$ → bottom-left. Its current toward $a$ is $\dfrac{55-a}{5}$ (the battery climbs $55$, the slides fall $5\,\Omega$ worth).", []),
        (r"In = out at $a$ (from the bottom-left wire): $\dfrac{55-a}{5}=\dfrac{a}{4}+2$, so $a=20\,\mathrm{V}$.", ['a']),
        (r"So $7\,\mathrm{A}$ climbs the battery and slides into $a$; $5\,\mathrm{A}$ goes down the $4\,\Omega$ and $2\,\mathrm{A}$ down through the pump.", ['c', 'z0', 'eR1', 'eR2', 'eR3', 'eV1']),
        (r"The pump carries $2\,\mathrm{A}$ **downhill** by $20\,\mathrm{V}$: it extracts $40\,\mathrm{W}$.", ['eI1']),
    ])],
    [S(r'One unknown, $a$. The right branch: battery and $2+3\,\Omega$ in series.', r'\frac{55-v_a}{5}=\frac{v_a}{4}+2\;\Rightarrow\;v_a=20\,\mathrm{V}'),
     S('The pump carries its current from $a$ down to the bottom wire.', r'p=(20)(2)=40\,\mathrm{W}\text{ absorbed}')],
    r'The $2\,\mathrm{A}$ source extracts (absorbs) $40\,\mathrm{W}$.', D.tb('4.7'))
TRY('p48', 'Try it 2 · Find v_o, then every power (Textbook P4.8 and P4.9)', 'introductory',
    r'**(a)** Use the node-voltage method to find $v_o$. **(b)** Find the power developed by the $5\,\mathrm{A}$ source and by the $180\,\mathrm{V}$ source, and check the balance.',
    [V('p48', [('V1', 0), ('R1', 1), ('R2', 1), ('R3', 1), ('I1', 2)], names={'s': 'battery top', 't': '$t$', 'o': '$v_o$', '0': 'ground'}, refs={'R3': ('o', '$v_o$')}, steps=[
        (r"Ground the bottom wire. The battery lifts its top to $180\,\mathrm{V}$.", []),
        (r"The $12\,\Omega$ and $5\,\Omega$ are one path ($17\,\Omega$) from $180\,\mathrm{V}$ to $v_o$. In = out at $v_o$: $\dfrac{180-v_o}{17}=\dfrac{v_o}{2}+5$, so $v_o=10\,\mathrm{V}$.", ['o', 't']),
        (r"Currents: $10\,\mathrm{A}$ down the $12\,\Omega$ and $5\,\Omega$, $5\,\mathrm{A}$ down the $2\,\Omega$, $5\,\mathrm{A}$ down through the pump.", ['eR1', 'eR2', 'eR3', 'eI1', 'eV1']),
        (r"Power: the battery lifts $10\,\mathrm{A}$ by $180\,\mathrm{V}$: $1800\,\mathrm{W}$. The pump carries $5\,\mathrm{A}$ **down** $10\,\mathrm{V}$: it absorbs $50\,\mathrm{W}$ (develops $-50\,\mathrm{W}$). Slides: $1200+500+50=1750$ ✓", []),
    ])],
    [S(r'In = out at $v_o$.', r'\frac{180-v_o}{12+5}=\frac{v_o}{2}+5\;\Rightarrow\;v_o=10\,\mathrm{V}'),
     S('Powers.', r'\begin{aligned}p_{180}&=180(10)=1800\,\mathrm{W}\text{ developed}\\p_{5\mathrm{A}}&=-(10)(5)=-50\,\mathrm{W}\text{ developed}\end{aligned}')],
    r'**(a)** $v_o=10\,\mathrm{V}$. **(b)** $180\,\mathrm{V}$: $1800\,\mathrm{W}$; $5\,\mathrm{A}$: $-50\,\mathrm{W}$ (it absorbs $50\,\mathrm{W}$). Total $1750\,\mathrm{W}$ developed = dissipated.', D.tb('4.8') + D.tb('4.9'))
s, a = old('Try it 2 · One node above')
TRY('ap413', 'Try it 3 · One wire above both batteries (Assessment AP 4.13)', 'introductory', intro('Try it 2 · One node above'),
    [V('ap413', [('I1', 0), ('R1', 1), ('V1', 1), ('R2', 2), ('V2', 2)], names={'s': 'left top', 'n1': '$v_1$', 'r': 'right top', '0': 'ground'}, steps=[
        (r"Ground the bottom wire. Left battery top: $20\,\mathrm{V}$. Right battery top: $25\,\mathrm{V}$.", []),
        (r"One unknown, $v_1$. In = out: $2=\dfrac{v_1-20}{15}+\dfrac{v_1-25}{10}$, so $v_1=35\,\mathrm{V}$.", ['n1']),
        (r"$v_1$ is above both batteries, so $1\,\mathrm{A}$ slides away on each side and falls **into** both batteries (both absorb).", ['eR1', 'eR2', 'eV1', 'eV2']),
        (r"The pump lifts $2\,\mathrm{A}$ by $35\,\mathrm{V}$: it delivers $70\,\mathrm{W}=20+25+15+10$.", ['eI1']),
    ])], *old('Try it 2 · One node above'), D.oc('Try it 2 · One node above'))
s, a = old('Try it 3 · Two current')
TRY('p413', 'Try it 4 · Two pumps, no battery (Textbook P4.13)', 'introductory', intro('Try it 3 · Two current'),
    [V('p413', [('I2', 0), ('R4', 1), ('R3', 2), ('R2', 3), ('R1', 4), ('I1', 5)], names={'n1': '$v_1$', 'n2': '$v_2$', '0': 'ground'},
       refs={'R1': ('n1', '$v_1$'), 'R4': ('n2', '$v_2$')}, steps=[
        (r"Ground the bottom wire. No battery: $v_1$ and $v_2$ are both unknown.", []),
        (r"In = out at each. Node 1: $\dfrac{v_1}{125}+\dfrac{v_1-v_2}{25}+2.4=0$. Node 2: $\dfrac{v_2}{250}+\dfrac{v_2}{375}+\dfrac{v_2-v_1}{25}=3.2$.", []),
        (r"Solve: $v_1=25\,\mathrm{V}$, $v_2=90\,\mathrm{V}$.", ['n1', 'n2']),
        (r"$2.6\,\mathrm{A}$ slides from node 2 to node 1; $0.2\,\mathrm{A}$ goes down the $125\,\Omega$ and $2.4\,\mathrm{A}$ down through the left pump (it absorbs). Only the $3.2\,\mathrm{A}$ pump climbs.", ['eR1', 'eR2', 'eR3', 'eR4', 'eI1', 'eI2']),
    ])], s, a, D.tb('4.13'))
TRY('p416', 'Try it 5 · The top wire lands at the average (Textbook P4.16)', 'introductory',
    r'**(a)** Show that $v_o$ is the average of the source voltages. **(b)** Find $v_o$ if $v_1=150\,\mathrm{V}$, $v_2=200\,\mathrm{V}$ and $v_3=-50\,\mathrm{V}$.',
    [V('p416', [('V2', 0), ('V1', 1), ('V3', 1), ('R1', 2), ('R2', 3), ('R3', 3)], gnd='low',
       names={'p1': '$v_1$ top', 'p2': '$v_2$ top', 'p3': '$v_3$ top', 'o': '$v_o$', '0': 'bottom'}, steps=[
        (r"Ground the lowest wire, the top of $v_3$ ($-50\,\mathrm{V}$). Answers are still read from the bottom wire.", []),
        (r"In = out at the top wire, all slides equal: $\dfrac{v_1-v_o}{R}+\dfrac{v_2-v_o}{R}+\dfrac{v_3-v_o}{R}=0$, so $v_o=\dfrac{v_1+v_2+v_3}{3}$.", []),
        (r"$v_o=\dfrac{150+200-50}{3}=100\,\mathrm{V}$: the top wire settles at the **average** height of the three battery tops.", ['o']),
        (r"Drawn with $R=10\,\Omega$: $5$ and $10\,\mathrm{A}$ slide in from $v_1$ and $v_2$; $15\,\mathrm{A}$ slides down into $v_3$ (that battery absorbs).", ['eR1', 'eR2', 'eR3', 'eV1', 'eV2', 'eV3']),
    ], notes=[r"Any $R$ gives the same $v_o$; only the currents change."])],
    [S('In = out at the top wire.', r'\sum_k\frac{v_k-v_o}{R}=0\;\Rightarrow\;v_o=\frac{v_1+v_2+\cdots+v_n}{n}'),
     S('Numbers.', r'v_o=\frac{150+200-50}{3}=100\,\mathrm{V}')],
    r'$v_o$ is the average; with these values $v_o=100\,\mathrm{V}$.', D.tb('4.16'))
TRY('p411', 'Try it 6 · Three unknown heights (Textbook P4.11)', 'intermediate',
    r'**(a)** Use the node-voltage method to find the branch currents $i_a$ to $i_f$. **(b)** Find the total power developed.',
    [V('p411', [('V1', 0), ('R1', 1), ('R2', 2), ('R5', 2), ('R3', 3), ('R6', 3), ('R4', 4)], unit='mA',
       names={'s': 'battery top', 'p': '$p$', 'q': '$q$', 'r': '$r$', '0': 'ground'}, steps=[
        (r"Ground the bottom wire. The battery lifts its top to $80\,\mathrm{V}$.", []),
        (r"Three unknowns: $p$, $q$, $r$. In = out at each (mA, kΩ). $p$: $\dfrac{80-p}{0.8}=\dfrac{p-q}{0.5}+\dfrac{p-r}{1}$. $q$: $\dfrac{p-q}{0.5}=\dfrac{q}{3}+\dfrac{q-r}{2}$. $r$: $\dfrac{p-r}{1}+\dfrac{q-r}{2}=\dfrac{r}{0.25}$.", []),
        (r"Solve: $p=40$, $q=30$, $r=10\,\mathrm{V}$.", ['p', 'q', 'r']),
        (r"Currents = fall ÷ R: $i_b=50$, $i_c=20$, $i_d=10$, $i_a=30$, $i_e=10$, $i_f=40\,\mathrm{mA}$.", ['eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eR6', 'eV1']),
        (r"Power: the battery lifts $50\,\mathrm{mA}$ by $80\,\mathrm{V}$: $4\,\mathrm{W}$, all used by the slides.", []),
    ])],
    [S('In = out at $p$, $q$, $r$ (mA, kΩ).', r'\begin{aligned}&\tfrac{80-p}{0.8}=\tfrac{p-q}{0.5}+\tfrac{p-r}{1}\\&\tfrac{p-q}{0.5}=\tfrac{q}{3}+\tfrac{q-r}{2}\\&\tfrac{p-r}{1}+\tfrac{q-r}{2}=\tfrac{r}{0.25}\end{aligned}'),
     S('Solve.', r'p=40,\quad q=30,\quad r=10\,\mathrm{V}'),
     S('Currents and power.', r'\begin{aligned}&i_a=30,\;i_b=50,\;i_c=20,\;i_d=10,\;i_e=10,\;i_f=40\,\mathrm{mA}\\&p=80(0.05)=4\,\mathrm{W}\end{aligned}')],
    r'$i_a=30$, $i_b=50$, $i_c=20$, $i_d=10$, $i_e=10$, $i_f=40\,\mathrm{mA}$; $4\,\mathrm{W}$ developed.', D.tb('4.11'))
TRY('p425', 'Try it 7 · A pump lifts a wire above the battery (Textbook P4.25)', 'intermediate',
    r'Use the node-voltage method to find $v_o$.',
    [V('p425', [('V1', 0), ('R5', 1), ('R1', 2), ('R2', 2), ('R3', 3), ('I1', 4), ('R4', 5)], names={'s': 'battery top', 'm': '$m$', 'r': '$r$', '0': 'ground'},
       refs={'R5': ('r', '$v_o$')}, steps=[
        (r"Ground the bottom wire. The battery lifts its top to $50\,\mathrm{V}$.", []),
        (r"Unknowns $m$ and $r$. In = out at $m$: $\dfrac{50-m}{80}+\dfrac{r-m}{40}=\dfrac{m}{50}$. At $r$: $0.75=\dfrac{r-m}{40}+\dfrac{r}{200}+\dfrac{r-50}{800}$.", []),
        (r"Solve: $m=34\,\mathrm{V}$, $r=53.2\,\mathrm{V}$. The pump lifted $r$ above the battery.", ['m', 'r']),
        (r"$v_o$ is $r$ measured from the $800\,\Omega$'s left end (the battery top): $v_o=53.2-50=3.2\,\mathrm{V}$. Only $4\,\mathrm{mA}$ trickles back through it.", ['eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eV1', 'eI1']),
    ])],
    [S('In = out at $m$ and $r$.', r'\begin{aligned}&\tfrac{50-m}{80}+\tfrac{r-m}{40}=\tfrac{m}{50}\\&0.75=\tfrac{r-m}{40}+\tfrac{r}{200}+\tfrac{r-50}{800}\end{aligned}'),
     S('Solve and subtract.', r'm=34,\quad r=53.2\,\mathrm{V},\qquad v_o=r-50=3.2\,\mathrm{V}')],
    r'$v_o=3.2\,\mathrm{V}$', D.tb('4.25'))
s, a = old('Try it 4 · A controlled rod')
TRY('p427', 'Try it 8 · A diamond between two unknown wires (Textbook P4.27)', 'advanced', intro('Try it 4 · A controlled rod'),
    [V('p427', [('I1', 0), ('R1', 1), ('R2', 2), ('R3', 2), ('E1', 3), ('R4', 4), ('R5', 5), ('V1', 6)], elabel={'E1': '$i_x$'},
       names={'a': '$a$', 'b': '$b$ ($v$)', 'c': '$c$', 'd': '12 V top', '0': 'ground'}, refs={'R3': ('b', '$v$')}, steps=[
        (r"Ground the bottom wire. The $12\,\mathrm{V}$ battery lifts its top to $12\,\mathrm{V}$.", []),
        (r"The diamond sits between $b$ and $c$: it locks $c=v+i_x$ (it is $1\,\Omega\times i_x$ volts). It depends on $i_x=\dfrac{a}{7.5}$, the current down the $7.5\,\Omega$.", []),
        (r"In = out at $a$: $4.8=\dfrac{a}{7.5}+\dfrac{a-v}{2.5}$. Bubble around $b$ and $c$: $\dfrac{a-v}{2.5}+\dfrac{12-c}{1}=\dfrac{v}{10}+\dfrac{c}{2.5}$. Solve: $a=15$, $v=8$, $c=10\,\mathrm{V}$.", ['a', 'b', 'c', 'eE1']),
        (r"Currents: $i_x=2\,\mathrm{A}$, $2.8\,\mathrm{A}$ from $a$ to $b$, $0.8\,\mathrm{A}$ down the $10\,\Omega$, $4\,\mathrm{A}$ down the $2.5\,\Omega$ at $c$, $2\,\mathrm{A}$ into $c$ from the $12\,\mathrm{V}$ side.", ['eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eV1', 'eI1']),
    ])], s, a, D.tb('4.27'))
s, a = old('Try it 5 · A rod hanging')
TRY('ap46', 'Try it 9 · A diamond hanging from a battery (Assessment AP 4.6)', 'advanced', intro('Try it 5 · A rod hanging'),
    [V('ap46', [('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2), ('E1', 3), ('R4', 3)], elabel={'E1': r'$6i_\phi$'},
       names={'s': 'battery top', 'n1': '$v_1$', 'r': 'right wire', '0': 'ground'}, steps=[
        (r"Ground the bottom wire. The $60\,\mathrm{V}$ battery lifts the left wire to $60\,\mathrm{V}$.", []),
        (r"The diamond hangs from that wire: the right wire is $6i_\phi$ above it (below it if $i_\phi$ is negative). $i_\phi$ is the current from the right wire to $v_1$ through $3\,\Omega$.", []),
        (r"In = out at $v_1$, with the right wire at $60+6i_\phi$ and $i_\phi=\dfrac{60+6i_\phi-v_1}{3}$: $i_\phi=-4\,\mathrm{A}$, $v_1=48\,\mathrm{V}$, right wire $36\,\mathrm{V}$.", ['n1', 'r', 'eE1']),
        (r"Negative $i_\phi$: $4\,\mathrm{A}$ really flows from $v_1$ to the right wire. The diamond steps **down** $24\,\mathrm{V}$ and $8\,\mathrm{A}$ falls through it (it absorbs $192\,\mathrm{W}$).", ['eR1', 'eR2', 'eR3', 'eR4', 'eV1']),
    ])], s, a, D.oc('Try it 5 · A rod hanging'))

# =========================================================================== Topic 2
H(1, 'Topic 2: Mesh currents are loop walks', D.oc('Topic 4: The mesh-current'))
CO('tip', "**How it looks in heights.**\n\n"
          "- Give each window of the circuit a **loop current** (clockwise). Walk around each window: **climbs = falls**.\n"
          "- A resistor shared by two windows carries the **difference** of their loop currents.\n"
          "- A pump on a window's **outside edge** gives that loop current for free. A pump **between** two windows: walk around both windows as one big loop, skipping the pump (a *supermesh*), and add *difference of the two loop currents = pump current*.\n"
          "- Loop currents are bookkeeping. Turn them into real currents, then place the heights by walking down the slides.")
EX('M1', 'Example 11 · One window', r'Find the loop current and the height of $x$.',
   [V('M1', [('V1', 0), ('R1', 1), ('R2', 1)], names={'s': 'battery top', 'x': '$x$', '0': 'ground'}, steps=[
       (r"Ground the bottom wire. One window, one loop current $I$ (clockwise).", []),
       (r"Walk around: climb $12\,\mathrm{V}$ through the battery, fall $2I$ and $4I$ through the slides. Climbs = falls: $12=6I$, so $I=2\,\mathrm{A}$.", ['eR1', 'eR2', 'eV1']),
       (r"Place heights by walking down: $x=12-(2)(2)=8\,\mathrm{V}$. That is the whole mesh method: one loop walk per window.", ['x']),
   ])],
   [S('Loop walk.', r'12=2I+4I\;\Rightarrow\;I=2\,\mathrm{A},\qquad x=4I=8\,\mathrm{V}')], r'$I=2\,\mathrm{A}$, $x=8\,\mathrm{V}$')
EX('C1', 'Example 12 · Two windows (same answer as node voltages)', r'Find the loop currents and the height of $x$.',
   [V('C1', [('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2), ('V2', 2)], names={'s': 'left top', 'x': '$x$', 'r': 'right top', '0': 'ground'}, steps=[
       (r"Ground the bottom wire. Battery tops: $12\,\mathrm{V}$ (left) and $6\,\mathrm{V}$ (right).", []),
       (r"Loop currents $I_1$ (left window) and $I_2$ (right), both clockwise. The middle $4\,\Omega$ is shared: it carries $I_1-I_2$.", []),
       (r"Left walk: $12=2I_1+4(I_1-I_2)$. Right walk: $0=4(I_2-I_1)+2I_2+6$ (walking down through the $6\,\mathrm{V}$ battery is a fall). So $I_1=2.4$, $I_2=0.6\,\mathrm{A}$.", []),
       (r"Real currents: $2.4\,\mathrm{A}$ in, $1.8\,\mathrm{A}$ down the middle, $0.6\,\mathrm{A}$ into the $6\,\mathrm{V}$ battery. Height: $x=(1.8)(4)=7.2\,\mathrm{V}$. In = out at $x$ (Topic 1) gives the same $7.2\,\mathrm{V}$.", ['x', 'eR1', 'eR2', 'eR3', 'eV1', 'eV2']),
   ])],
   [S('Two loop walks.', r'6I_1-4I_2=12,\qquad -4I_1+6I_2=-6\;\Rightarrow\;I_1=2.4\,\mathrm{A},\;I_2=0.6\,\mathrm{A}'),
    S('Height.', r'x=4(I_1-I_2)=7.2\,\mathrm{V}')], r'$I_1=2.4\,\mathrm{A}$, $I_2=0.6\,\mathrm{A}$, $x=7.2\,\mathrm{V}$')
EX('M2', 'Example 13 · A pump on the outside edge', r'Find both loop currents and the heights of $m$ and $r$.',
   [V('M2', [('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2), ('I1', 2)], names={'s': 'battery top', 'm': '$m$', 'r': '$r$', '0': 'ground'}, steps=[
       (r"Ground the bottom wire. The battery lifts the left top to $20\,\mathrm{V}$.", []),
       (r"The $2\,\mathrm{A}$ pump is on the right window's outside edge, pointing the same way as the clockwise loop. So $I_2=2\,\mathrm{A}$: no equation needed.", ['eI1']),
       (r"Only the left walk is left: $20=4I_1+6(I_1-2)$, so $I_1=3.2\,\mathrm{A}$.", ['eR1']),
       (r"Heights: $m=20-(3.2)(4)=7.2\,\mathrm{V}$; the $6\,\Omega$ carries $1.2\,\mathrm{A}$ down ($7.2\,\mathrm{V}$ ✓); $r=7.2-(2)(3)=1.2\,\mathrm{V}$.", ['m', 'r', 'eR2', 'eR3', 'eV1']),
       (r"The pump carries $2\,\mathrm{A}$ **down** from $1.2\,\mathrm{V}$ to $0$: it absorbs $2.4\,\mathrm{W}$.", []),
   ])],
   [S('The pump fixes the right loop.', r'I_2=2\,\mathrm{A}'),
    S('Left loop walk.', r'20=4I_1+6(I_1-2)\;\Rightarrow\;I_1=3.2\,\mathrm{A}'),
    S('Heights.', r'm=6(3.2-2)=7.2\,\mathrm{V},\qquad r=7.2-3(2)=1.2\,\mathrm{V}')],
   r'$I_1=3.2\,\mathrm{A}$, $I_2=2\,\mathrm{A}$; $m=7.2\,\mathrm{V}$, $r=1.2\,\mathrm{V}$')
s, a = old('Three meshes')
EX('lec_3mesh', 'Example 14 · Three windows (Lecture 3)', intro('Three meshes'),
   [V('lec_3mesh', [('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2), ('R4', 2), ('R5', 3), ('V2', 4)], refs={'R2': ('a', '$v_o$')},
      names={'s': '40 V top', 'a': '$a$', 'b': '$b$', 'c': '20 V top', '0': 'ground'}, steps=[
       (r"Ground the bottom wire. Battery tops: $40\,\mathrm{V}$ and $20\,\mathrm{V}$.", []),
       (r"Three clockwise loop currents. One walk per window: $10I_1-8I_2=40$, $-8I_1+20I_2-6I_3=0$, $-6I_2+10I_3=-20$.", []),
       (r"Solve: $I_1=5.6$, $I_2=2$, $I_3=-0.8\,\mathrm{A}$. Real currents: $5.6\,\mathrm{A}$ in the $2\,\Omega$, $3.6\,\mathrm{A}$ down the $8\,\Omega$, $2\,\mathrm{A}$ across, $2.8\,\mathrm{A}$ down the right $6\,\Omega$, $0.8\,\mathrm{A}$ leftward in the $4\,\Omega$.", ['eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eV1', 'eV2']),
       (r"Walk down from $40\,\mathrm{V}$: $a=40-(5.6)(2)=28.8\,\mathrm{V}=v_o$, $b=28.8-(2)(6)=16.8\,\mathrm{V}$. From the right: $20-(0.8)(4)=16.8$ ✓", ['a', 'b']),
       (r"Both batteries climb: they deliver $224\,\mathrm{W}$ and $16\,\mathrm{W}$.", []),
   ])], s, a, D.oc('Three meshes'))
s, a = old('A supermesh skips')
EX('ap412', 'Example 15 · A pump between two windows: walk around both (Assessment AP 4.12)', intro('A supermesh skips'),
   [V('ap412', [('V1', 0), ('R1', 1), ('I1', 2), ('R3', 2), ('R2', 3), ('V2', 4), ('R4', 5)], names={'s': 'battery top', 'm': '$m$', 'r': '$r$', 'q': '$q$', '0': 'ground'}, steps=[
       (r"Ground the bottom wire. The $10\,\mathrm{V}$ battery lifts its top to $10\,\mathrm{V}$.", []),
       (r"The $2\,\mathrm{A}$ pump sits between windows $a$ and $b$: $I_a-I_b=2$. Its height change is unknown, so walk around $a$ and $b$ together, skipping it: $-10+2I_b+2(I_b-I_c)+2(I_a-I_c)=0$.", []),
       (r"Window $c$: $-6+I_c+2(I_c-I_a)+2(I_c-I_b)=0$. Solve: $I_a=7$, $I_b=5$, $I_c=6\,\mathrm{A}$.", []),
       (r"Real currents → heights: $5\,\mathrm{A}$ down the top $2\,\Omega$ to $r$ ($0\,\mathrm{V}$); $m=2\,\mathrm{V}$; $q=6\,\mathrm{V}$ above the $1\,\Omega$, which carries $6\,\mathrm{A}$: $36\,\mathrm{W}$.", ['m', 'q', 'r', 'eR1', 'eR2', 'eR3', 'eR4', 'eV1', 'eV2']),
       (r"The pump carries $2\,\mathrm{A}$ **down** from $10\,\mathrm{V}$ to $2\,\mathrm{V}$: it absorbs $16\,\mathrm{W}$.", ['eI1']),
   ])], s, a, D.oc('A supermesh skips'))
s, a = old('A dependent source in a mesh')
EX('lec_meshdep', 'Example 16 · A diamond in a window (Lecture 3)', intro('A dependent source in a mesh'),
   [V('lec_meshdep', [('V1', 0), ('R1', 1), ('R3', 1), ('R2', 2), ('E1', 2), ('R4', 3)], elabel={'E1': r'$15i_\phi$'},
      names={'s': 'battery top', 'a': '$a$', 'b': '$b$', '0': 'ground'}, steps=[
       (r"Ground the bottom wire. The battery lifts its top to $50\,\mathrm{V}$.", []),
       (r"The diamond is a battery of $15i_\phi$. It depends on $i_\phi$, the current down the $20\,\Omega$: $i_\phi=I_a-I_c$ (two windows share it).", []),
       (r"Three loop walks with that control: $I_a=29.6$, $I_b=26$, $I_c=28\,\mathrm{A}$, so $i_\phi=1.6\,\mathrm{A}$.", []),
       (r"Heights: $a=20i_\phi=32\,\mathrm{V}$, the diamond's top $b=15i_\phi=24\,\mathrm{V}$. The $4\,\Omega$ falls $8\,\mathrm{V}$ with $2\,\mathrm{A}$: $16\,\mathrm{W}$.", ['a', 'b', 'eR1', 'eR2', 'eR3', 'eR4', 'eV1', 'eE1']),
   ])], s, a, D.oc('A dependent source in a mesh'))
b = D.ob("Reading a circuit's structure")
D.EX('struct', 'Example 17 · Count the unknowns before you start (Lecture 3)', b['prompt'], '', b['steps'],
     b['answer'] + r' **So:** node voltages need $n_e-1$ equations, mesh currents need $b_e-n_e+1$.', D.oc("Reading a circuit's structure"))
CO('warning', "**Loop-walk traps.** Through a battery from $-$ to $+$ is a **climb**; $+$ to $-$ is a **fall**. A shared resistor carries a **difference** of loop currents. A pump's height change is unknown: never write $R\\times I$ for it (that is why you walk around it).")

# ---- Try its, Topic 2
b = D.ob('Try it 1 · Count everything')
D.PR('p41', 'Try it 10 · Count everything (Textbook P4.1)', 'introductory', b['prompt'], '', b['steps'], b['answer'], D.tb('4.1'))
s, a = old('Try it 6 · A current source on the edge')
TRY('ap410', 'Try it 11 · A pump on the outside edge (Assessment AP 4.10)', 'intermediate', intro('Try it 6 · A current source on the edge'),
    [V('ap410', [('V1', 0), ('R1', 1), ('R3', 1), ('R2', 1), ('R4', 2), ('R5', 2), ('R6', 3), ('I1', 4)], gnd='low',
       names={'s': 'battery top', 'm': 'top middle', 'q': 'bottom middle', 'r': 'top right', 'p': 'bottom right', '0': 'bottom-left'}, steps=[
        (r"Ground the bottom-right wire, the lowest. Heights are measured from it (the bottom-left wire sits $4\,\mathrm{V}$ up).", []),
        (r"The $16\,\mathrm{A}$ pump is on mesh 3's outside edge, pointing **against** clockwise: $I_3=-16\,\mathrm{A}$.", ['eI1']),
        (r"Walk meshes 1 and 2: $11I_1-2I_2=30$ and $-2I_1+19I_2=-80$, so $I_1=2$, $I_2=-4\,\mathrm{A}$.", []),
        (r"The $2\,\Omega$ carries $I_1-I_2=6\,\mathrm{A}$: $6^2\times2=72\,\mathrm{W}$.", ['eR3']),
        (r"All real currents → heights. The pump lifts $16\,\mathrm{A}$ by $60\,\mathrm{V}$: the big climb in this circuit.", ['s', 'm', 'q', 'r', 'eR1', 'eR2', 'eR4', 'eR5', 'eR6', 'eV1']),
    ])], s, a, D.oc('Try it 6 · A current source on the edge'))
s, a = old('Try it 7 · Flip one source')
nm437 = {'s': 'battery top', 'm': 'top middle', 'q': 'bottom middle', 'r': 'top right', 'p': 'bottom right', '0': 'bottom-left'}
c437 = [('V1', 0), ('R1', 1), ('R4', 1), ('R5', 2), ('R3', 2), ('R2', 3), ('V2', 4)]
c437b = [('V2', 0), ('R4', 1), ('R1', 1), ('V1', 1), ('R2', 1), ('R5', 1), ('R3', 2)]
TRY('p437', 'Try it 12 · Flip one battery (Textbook P4.37)', 'intermediate', intro('Try it 7 · Flip one source'),
    [V('p437', c437, title='As drawn', gnd='low', names=nm437, steps=[
        (r"Ground the lowest wire, the $64\,\mathrm{V}$ battery's $-$ end. Answers don't change.", []),
        (r"Loop currents $I_L$, $I_R$ (clockwise): $i_a=I_L$, $i_b=I_L-I_R$, $i_c=-I_R$. Walks: $50I_L-45I_R=40$ and $-45I_L+50.5I_R=64$, so $I_L=9.8$, $I_R=10\,\mathrm{A}$.", []),
        (r"So $i_a=9.8\,\mathrm{A}$, $i_b=-0.2\,\mathrm{A}$ ($0.2\,\mathrm{A}$ goes **up** the $45\,\Omega$), $i_c=-10\,\mathrm{A}$.", ['eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eV1', 'eV2']),
     ]),
     view(C['p437b']['net'], c437b, title='64 V flipped', gnd='low', names=nm437, steps=[
        (r"Ground the lowest wire again. Only the $64\,\mathrm{V}$ walk sign changes: $-45I_L+50.5I_R=-64$.", []),
        (r"$I_L=-1.72$, $I_R=-2.8\,\mathrm{A}$: $i_a=-1.72$, $i_b=1.08$, $i_c=2.8\,\mathrm{A}$.", ['eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eV1', 'eV2']),
     ])], s, a, D.tb('4.37'))
TRY('p436', 'Try it 13 · Three batteries, three windows (Textbook P4.36)', 'intermediate',
    r'**(a)** Use the mesh-current method to find the total power developed. **(b)** Check that it equals the total power dissipated.',
    [V('p436', [('V1', 0), ('R3', 1), ('V2', 1), ('R2', 2), ('R6', 2), ('R1', 3), ('R4', 3), ('V3', 4), ('R5', 5)], gnd='low',
       names={'a': '$a$', 'b': '$b$', 'm': '$m$', 'n': '12 V top', 'r': '$r$', 'l': '$l$', '0': 'bottom middle'}, steps=[
        (r"Ground $l$, the lowest wire (the $110\,\mathrm{V}$ battery's $-$ end). Heights are measured from $l$.", []),
        (r"Clockwise loops: $i_1$ lower left, $i_2$ lower right, $i_3$ top. Walks: $17i_1-3i_2-10i_3=122$, $-3i_1+17i_2-12i_3=-82$, $-10i_1-12i_2+28i_3=0$.", []),
        (r"Solve: $i_1=8$, $i_2=-2$, $i_3=2\,\mathrm{A}$. Real currents: $6\,\mathrm{A}$ in the $10\,\Omega$, $4\,\mathrm{A}$ from $b$ to $m$, $2\,\mathrm{A}$ in the $6\,\Omega$, $10\,\mathrm{A}$ down the $3\,\Omega$ and up through the $12\,\mathrm{V}$ battery, $8\,\mathrm{A}$ in the $4\,\Omega$, $2\,\mathrm{A}$ in the $2\,\Omega$.", ['eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eR6']),
        (r"Heights by walking down the slides.", ['a', 'b', 'm', 'n', 'r', 'z0']),
        (r"All three batteries climb: $880+140+120=1140\,\mathrm{W}$ developed = $1140\,\mathrm{W}$ in the six slides.", ['eV1', 'eV2', 'eV3']),
    ])],
    [S('Loop walks (clockwise; $-\\to+$ through a battery is a climb).', r'\begin{aligned}17i_1-3i_2-10i_3&=122\\-3i_1+17i_2-12i_3&=-82\\-10i_1-12i_2+28i_3&=0\end{aligned}'),
     S('Solve.', r'i_1=8\,\mathrm{A},\quad i_2=-2\,\mathrm{A},\quad i_3=2\,\mathrm{A}'),
     S('Developed power.', r'110(8)+70(2)+12(10)=880+140+120=1140\,\mathrm{W}'),
     S('Dissipated.', r'360+192+24+300+256+8=1140\,\mathrm{W}')],
    r'$1140\,\mathrm{W}$ developed $=1140\,\mathrm{W}$ dissipated.', D.tb('4.36'))
TRY('p442', 'Try it 14 · A diamond controlled by a shared resistor (Textbook P4.42)', 'intermediate',
    r'Use the mesh-current method to find the power dissipated in the $10\,\Omega$ resistor.',
    [V('p442', [('V1', 0), ('R1', 1), ('R2', 1), ('R4', 1), ('R3', 2), ('E1', 3), ('R5', 4)], gnd='low', elabel={'E1': r'$\tfrac{v_\Delta}{2}$'},
       refs={'R2': ('m', r'$v_\Delta$')}, names={'s': 'battery top', 'm': '$m$', 't': 'diamond $-$', 'r': '$r$', 'l': '$l$', '0': 'bottom middle'}, steps=[
        (r"Ground $l$, the lowest wire. Heights are measured from $l$.", []),
        (r"The diamond is a battery of $\dfrac{v_\Delta}{2}$ ($+$ at the bottom). It depends on $v_\Delta$, across the shared $10\,\Omega$: $v_\Delta=10(i_1-i_2)$.", []),
        (r"Walk both windows: left $60=4i_1+10(i_1-i_2)+2i_1$; right $2.5i_2-\dfrac{v_\Delta}{2}+20i_2+10(i_2-i_1)=0$. So $i_1=5$, $i_2=2\,\mathrm{A}$, $v_\Delta=30\,\mathrm{V}$.", ['eE1']),
        (r"The $10\,\Omega$ carries $3\,\mathrm{A}$ and falls $30\,\mathrm{V}$: $90\,\mathrm{W}$.", ['m', 'eR2']),
        (r"The rest: the diamond lifts $2\,\mathrm{A}$ by $15\,\mathrm{V}$ (gives $30\,\mathrm{W}$); the battery gives $300\,\mathrm{W}$.", ['t', 'r', 'eR1', 'eR3', 'eR4', 'eR5', 'eV1']),
    ])],
    [S('Control.', r'v_\Delta=10(i_1-i_2)'),
     S('Loop walks.', r'\begin{aligned}60&=4i_1+10(i_1-i_2)+2i_1\\0&=2.5i_2-\tfrac{v_\Delta}{2}+20i_2+10(i_2-i_1)\end{aligned}'),
     S('Solve.', r'i_1=5\,\mathrm{A},\quad i_2=2\,\mathrm{A},\quad v_\Delta=30\,\mathrm{V},\qquad p_{10\Omega}=\frac{30^2}{10}=90\,\mathrm{W}')],
    r'$p_{10\,\Omega}=90\,\mathrm{W}$', D.tb('4.42'))

# =========================================================================== Practice
H(1, 'Practice set')
P('Exam-style, mixing both topics. Try each for 10–15 minutes before opening the solution, then check your picture against the height view.')
s, a = old('Textbook P4.30')
TRY('p430', 'P4.30 · Where should ground go?', 'intermediate', intro('Textbook P4.30'),
    [V('p430', [('I1', 0), ('V1', 1), ('R1', 1), ('R2', 2), ('R3', 3), ('R4', 3)], refs={'R2': ('c', '$v_o$')}, names={'b': '$b$', 'c': '$c$', 'd': '$d$', '0': '$a$'}, steps=[
        (r"Ground $a$ (the bottom wire).", []),
        (r"The $12\,\mathrm{V}$ battery joins $b$ and $c$, both unknown: $c=b+12$. Bubble around them: the $0.5\,\mathrm{A}$ pump comes in; out go $\dfrac{b}{40}$, $\dfrac{c}{100}$ and $\dfrac{c}{200}$. So $b=8$, $c=20\,\mathrm{V}=v_o$.", ['b', 'c']),
        (r"Currents: $0.2\,\mathrm{A}$, $0.2\,\mathrm{A}$, and $0.1\,\mathrm{A}$ through $150+50\,\Omega$ ($d=5\,\mathrm{V}$). The pump lifts $0.5\,\mathrm{A}$ by $8\,\mathrm{V}$: $4\,\mathrm{W}$.", ['d', 'eR1', 'eR2', 'eR3', 'eR4', 'eV1', 'eI1']),
        (r"(b) Grounding $b$ instead just shifts every height down $8\,\mathrm{V}$: $v_o=c-a$ is still $20\,\mathrm{V}$. (c) $b$ is better: the battery then gives $c=12\,\mathrm{V}$ directly, so one plain in = out is enough.", []),
    ])], s, a, D.tb('4.30'))
s, a = old('Textbook P4.24')
TRY('p424', 'P4.24 · Wires below ground', 'intermediate', intro('Textbook P4.24'),
    [V('p424', [('R1', 0), ('V1', 1), ('R2', 1), ('I1', 1), ('R4', 2), ('R3', 3), ('V2', 4)], gnd='low', unit='mA',
       names={'s': 'battery top', 'a': '$a$', 'b': '$b$', '0': 'bottom wire'}, steps=[
        (r"Ground $b$, the lowest wire: the $10\,\mathrm{V}$ battery hangs it $10\,\mathrm{V}$ below the bottom wire. The question's voltages are from the bottom wire.", []),
        (r"One unknown, $a$. In = out at $a$ (mA, kΩ, from the bottom wire): $\dfrac{20-a}{25}=\dfrac{a}{0.25}+11+\dfrac{a+10}{0.5}$, so $a=-5\,\mathrm{V}$.", ['a']),
        (r"Currents: $i_1=1\,\mathrm{mA}$; $20\,\mathrm{mA}$ slides **up** the $250\,\Omega$ to $a$ ($i_2=-20$); $i_3=31\,\mathrm{mA}$ through the $10\,\mathrm{V}$ battery.", ['eR1', 'eR2', 'eR3', 'eR4', 'eV1', 'eV2']),
        (r"The pump carries $11\,\mathrm{mA}$ **down** from $a$ to $b$: it absorbs $55\,\mathrm{mW}$. The batteries give $20+310=330\,\mathrm{mW}$.", ['eI1']),
    ])], s, a, D.tb('4.24'))
s, a = old('Textbook P4.18')
TRY('p418', 'P4.18 · A diamond that gives power', 'intermediate', intro('Textbook P4.18'),
    [V('p418', [('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2), ('E1', 3), ('R4', 4)], elabel={'E1': r'$75i_\sigma$'},
       names={'s': 'battery top', 'a': '$a$', 'c': '$c$', 'd': '$d$', '0': 'ground'}, steps=[
        (r"Ground the bottom-left wire. The battery lifts its top to $80\,\mathrm{V}$.", []),
        (r"The diamond locks $d=c+75i_\sigma$, with $i_\sigma=\dfrac{a}{50}$ (the current down the $50\,\Omega$).", []),
        (r"In = out at $a$, and for the bubble around $c$ and $d$: $a=50$, $c=0$, $d=75\,\mathrm{V}$, $i_\sigma=1\,\mathrm{A}$.", ['a', 'c', 'd']),
        (r"$5\,\mathrm{A}$ slides from $a$ to $c$, **climbs** $75\,\mathrm{V}$ through the diamond, then falls down the $15\,\Omega$. Climbing means it gives $5\times75=375\,\mathrm{W}$.", ['eR1', 'eR2', 'eR3', 'eR4', 'eV1', 'eE1']),
    ])], s, a, D.tb('4.18'))
s, a = old('Textbook P4.49')
TRY('p449', 'P4.49 · A battery that gets charged', 'intermediate', intro('Textbook P4.49'),
    [V('p449', [('R1', 0), ('V1', 0), ('R3', 0), ('I1', 1), ('R4', 2), ('V2', 3), ('R2', 4)], gnd='low',
       names={'s': 'battery top', 'm': '$m$', 'r': 'top right', 'p': 'bottom right', 'q': '$q$', '0': 'bottom-left'}, steps=[
        (r"Ground the lowest wire (top right). Heights are measured from it.", []),
        (r"The $3\,\mathrm{A}$ pump is shared: $I_b-I_a=3$. Walk around the outside, skipping it: $5I_a+15I_b=33$. So $I_a=-0.6$, $I_b=2.4\,\mathrm{A}$.", []),
        (r"Real currents → heights. The slides use $88.2\,\mathrm{W}$.", ['s', 'm', 'p', 'q', 'z0', 'eR1', 'eR2', 'eR3', 'eR4']),
        (r"$0.6\,\mathrm{A}$ falls **into** the $18\,\mathrm{V}$ battery: it absorbs $10.8\,\mathrm{W}$. The pump ($63\,\mathrm{W}$) and the $15\,\mathrm{V}$ battery ($36\,\mathrm{W}$) climb.", ['eV1', 'eV2', 'eI1']),
    ])], s, a, D.tb('4.49'))
s, a = old('Week 4 tutorial Problem 4')
TRY('tut_bridge', 'Tutorial · A bridge by node voltages', 'advanced', intro('Week 4 tutorial Problem 4'),
    [V('tut_bridge', [('I1', 0), ('R1', 1), ('R2', 2), ('R3', 2), ('R4', 3), ('R5', 3), ('R6', 4)], names={'a': '$a$', 'b': '$b$', 'c': '$c$', '0': 'ground'}, steps=[
        (r"Ground the bottom wire. The $1\,\mathrm{A}$ pump pushes into $a$.", []),
        (r"Three unknowns $a$, $b$, $c$: one in = out each. Solve: $a=72.96$, $b=60$, $c=57.6\,\mathrm{V}$.", ['a', 'b', 'c']),
        (r"Currents = fall ÷ R: $i_o=\dfrac{57.6}{600}=0.096\,\mathrm{A}$, $i_1=0.048\,\mathrm{A}$, $i_2=\dfrac{60}{100}=0.6\,\mathrm{A}$.", ['eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eR6']),
        (r"The pump lifts $1\,\mathrm{A}$ by $72.96\,\mathrm{V}$: $72.96\,\mathrm{W}$.", ['eI1']),
    ])], s, a, D.oc('Week 4 tutorial Problem 4'))
s, a = old('Lecture 3 p.22')
TRY('lec22', 'Lecture 3 p.22 · A shared pump', 'advanced', intro('Lecture 3 p.22'),
    [V('lec22', [('V1', 0), ('R2', 1), ('R3', 1), ('V2', 1), ('R5', 1), ('R4', 1), ('I1', 2), ('R1', 3)], refs={'I1': ('m', '$v$')},
       names={'l': 'battery top', 'm': '$m$', 'r': '$r$', 'p': '$p$', 'q': '$q$', '0': 'ground'}, steps=[
        (r"Ground the bottom wire. The $100\,\mathrm{V}$ battery lifts its top to $100\,\mathrm{V}$.", []),
        (r"The $5\,\mathrm{A}$ pump is shared by windows $a$ and $c$: $i_c-i_a=5$. Walk around $a$ and $c$ together (skip the pump), and around $b$: $i_a=1.75$, $i_b=1.25$, $i_c=6.75\,\mathrm{A}$.", []),
        (r"Heights: $m=100-3(0.5)=98.5\,\mathrm{V}$, $q=6(1.75)=10.5\,\mathrm{V}$. The pump spans them: $v=88\,\mathrm{V}$.", ['m', 'q']),
        (r"$6.75\,\mathrm{A}$ falls through the $50\,\mathrm{V}$ battery ($r=87.5$ down to $p=37.5$): it absorbs. The pump lifts $5\,\mathrm{A}$ by $88\,\mathrm{V}$: $440\,\mathrm{W}$.", ['r', 'p', 'eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eV1', 'eV2', 'eI1']),
    ])], s, a, D.oc('Lecture 3 p.22'))
s, a = old('Textbook P4.41')
TRY('p441', 'P4.41 · A diamond in three windows', 'advanced', intro('Textbook P4.41'),
    [V('p441', [('V1', 0), ('R1', 1), ('R3', 1), ('V2', 1), ('R2', 2), ('R4', 2), ('R5', 3), ('E1', 4)], gnd='low', elabel={'E1': r'$-3v_\phi$'},
       refs={'R2': ('m', r'$v_\phi$')}, names={'s': 'battery top', 'm': '$m$', 'n': '10 V top', 'r': 'right wire', 'x': 'diamond $+$', '0': 'bottom'}, steps=[
        (r"Ground the lowest wire, the diamond's $+$ end. Heights are measured from it.", []),
        (r"The diamond depends on $v_\phi=3(i_3-i_2)$. Walk the three windows: $i_1=4$, $i_2=-1$, $i_3=3\,\mathrm{A}$, $v_\phi=12\,\mathrm{V}$.", []),
        (r"The diamond is a battery of $-3v_\phi=-36\,\mathrm{V}$: its $+$ end sits $36\,\mathrm{V}$ **below** its $-$ end.", ['eE1']),
        (r"$1\,\mathrm{A}$ falls down the $14\,\Omega$ to the diamond, then climbs $36\,\mathrm{V}$ through it: it delivers $36\,\mathrm{W}$.", ['s', 'm', 'n', 'r', 'z0', 'eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eV1', 'eV2']),
    ])], s, a, D.tb('4.41'))

# =========================================================================== Cheat sheet
H(1, 'Cheat sheet')
T(['Idea', 'In heights', 'Write'], [
    ['Node voltage', 'height of a wire above ground', '$v_k$'],
    ['In = out (KCL)', 'what slides in = what slides out', r'$\sum\dfrac{v_k-v_j}{R}=$ pump current in'],
    ['Battery from ground', 'a height for free', '$v_k=V$'],
    ['Battery between two unknown wires', 'a locked pair: one bubble', r'$v_p-v_q=V$, in = out for the bubble'],
    ['Diamond', 'a source whose size is set elsewhere', 'write its control in your letters first'],
    ['Loop walk (KVL)', 'around a window: climbs = falls', r'$\sum$ climbs $=\sum$ falls'],
    ['Shared resistor', 'carries the difference', '$I_1-I_2$'],
    ['Pump on an outside edge', 'gives that loop current', r'$I=\pm I_s$'],
    ['Pump between two windows', 'walk around both, skip the pump', r'$I_a-I_b=I_s$'],
    ['How many equations', 'unknown heights / windows', r'node: $n_e-1$; mesh: $b_e-n_e+1$'],
    ['Power', 'current × height change', 'climb gives, fall uses'],
])

D.save(os.path.join(HERE, 'w45', 'w3v3_blocks.json'))
