"""Build the Week 3 note (height-method rewrite) as a list of blocks -> w3_blocks.json."""
import json
import os
import sys
import uuid

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from circuits import C  # noqa: E402
from gen import fence, view  # noqa: E402

LEC = '03e42107-1bed-45b1-88bc-73ce82fd2acb'
AP = '3b287f2d-b408-41eb-a523-b299688ff303'
TUT = '6aad60b9-910d-4700-985f-68a4fa9278b3'
LEC_PAGE = {3: 'dbf6e3d8-f41a-47ba-bb2a-ce4261d25e08', 6: '2a95a9c7-149f-4bdb-a8ea-05012ec272e1',
            7: '281e662e-bfd9-4a81-9104-c7f5a079f666', 8: '24bf0c2c-f280-47ba-aac2-35b547edb6d8',
            11: '3d430349-a0f3-4dca-91dd-086cb8c6da41', 12: 'b1e890e2-d4f2-4448-9e3b-206d39b90486',
            13: 'd1fceda6-5105-4189-97c0-4991a3fa3b2f', 14: 'd7aac84b-e088-4388-bb21-fcbc266d3289',
            15: '7e82cc00-3297-4348-9376-98aa2d6f2788', 16: '15a937fa-3a2a-4dc6-8e5f-eb13383e1092',
            17: '591a590f-ec96-408a-930d-645cc903a2da', 18: '1a74a548-e571-4119-9cc5-0ebe24fca7f9',
            19: '43c51a64-1f93-459f-8c66-8b6c91ffba0e', 20: 'b208bed4-cc39-40fa-8d73-0d31aaa14429',
            21: '2523e6e0-c912-411e-bd8f-6a70dce44d39', 22: '2dd511b9-76b3-409e-8179-fdb1f7907a12'}
AP_PAGE = {5: '871ad2b4-3d46-4914-8093-1c82fcbb764b', 7: 'b424062b-f59f-47c1-b08b-81c45ecae319',
           8: '41f6ae5a-5f7a-4739-a989-3c42552040fb', 9: 'cc04109f-7d5d-4f90-8089-ceb5166c591c',
           10: 'b477b4ec-60b8-40a7-9700-ef0c8f55590e'}
TB = json.load(open(os.path.join(HERE, 'cites4.json')))
OLD = json.load(open(os.path.join(HERE, 'w3_rev8_backup.json'), encoding='utf-8'))
TUT_CITES = [b for b in OLD['blocks'] if b['id'].startswith('bad31857')][0]['citations']


def lec(*pages):
    return [{"source_id": LEC, "version": 1, "chunk_id": LEC_PAGE[p]} for p in pages]


def ap(*pages):
    return [{"source_id": AP, "version": 1, "chunk_id": AP_PAGE[p]} for p in pages]


def tb(n):
    return [TB[n]]


def nid(k):
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f'w3-v2/{len(B)}/' + k))


B = []


def H(level, text, cites=()):
    B.append({"type": "heading", "id": nid('h' + text), "level": level, "text": text, "citations": list(cites)})


def P(text):
    B.append({"type": "paragraph", "id": nid('p' + text[:60]), "text": text, "citations": []})


def CO(tone, text):
    B.append({"type": "callout", "id": nid('c' + text[:60]), "tone": tone, "text": text, "citations": []})


def L(items):
    B.append({"type": "list", "id": nid('l' + items[0][:60]), "items": items, "ordered": False, "citations": []})


def T(cols, rows):
    B.append({"type": "table", "id": nid('t' + cols[0] + rows[0][0][:40]), "columns": cols, "rows": rows, "citations": []})


def EQ(latex):
    B.append({"type": "equation", "id": nid('e' + latex[:60]), "latex": latex, "display": True, "citations": []})


def S(e, l=''):
    return {"explanation": e, "latex": l}


def EX(key, title, intro, fig, steps, answer, cites=(), after=''):
    prompt = intro + '\n\n' + fig + ('\n\n' + after if after else '')
    B.append({"type": "worked_example", "id": nid('x' + key), "title": title, "prompt": prompt, "steps": steps,
              "answer": answer, "citations": list(cites)})


def PR(key, title, diff, intro, fig, steps, answer, cites, after=''):
    prompt = intro + '\n\n' + fig + ('\n\n' + after if after else '')
    B.append({"type": "practice_problem", "id": nid('q' + key), "title": title, "difficulty": diff, "origin": "source",
              "prompt": prompt, "solution": "", "steps": steps, "answer": answer, "citations": list(cites)})


# =====================================================================================================
H(1, 'Overview')
CO('info', "Week 3 gives two systematic ways to solve circuits that don't reduce to series and parallel. **Node voltages:** name the unknown node heights, write KCL at each. **Mesh currents:** give each window of the circuit a loop current, write KVL around each. The node-voltage method *is* the height method, written as equations.")
H(2, 'Topic map')
T(['#', 'Topic', 'Key result', 'In heights'], [
    ['1', 'Circuit terminology', '$M=b-n+1$ meshes', 'each node is one level; essential nodes are the unknown heights'],
    ['2', 'Node-voltage method', 'KCL at each unknown node', 'a node sits at the weighted average of its neighbours'],
    ['3', 'Fixed heights, supernodes, dependent sources', '$v_p-v_q=V_s$; control first', 'a voltage source between two unknown nodes is a rigid rod'],
    ['4', 'Mesh-current method', 'KVL per mesh; a shared $R$ carries $I_k-I_\\ell$', 'a mesh equation is a loop walk: climbs = falls'],
])
CO('tip', "**How to use this note.** Shaky on Week 2? Read **Start here** first. Each topic: short rules → worked example → **Try it** (answer on paper first). Every circuit has a **Height view** with a **Walk me through it**. The **Summary** at the end is a visual crash course that maps every practice problem to what you need.")

# ---------------------------------------------------------------- Start here
H(1, 'Start here: the only Week 2 you need')
CO('tip', "**Week 2 still settling?** Week 3 only needs these five rules. Every new method this week is these rules applied to more nodes at once.")
T(['#', 'Rule', 'Picture it as'], [
    ['1', '**Every node has one height.** Ground one node ($0\\,\\mathrm{V}$); a node voltage is that node\'s height.', 'floors of a building'],
    ['2', '**Voltage source** = a fixed step: its $+$ end is exactly $V_s$ higher. Any current.', 'an escalator'],
    ['3', '**Current source** = a fixed current. Its step is whatever the circuit needs.', 'a pump'],
    ['4', '**Resistor:** current flows downhill, $i=\\dfrac{\\text{high}-\\text{low}}{R}$.', 'a slide'],
    ['5', '**KCL:** at every node, current in = current out. **Dependent source:** find its control first.', 'pipes joining'],
])
EX('S1', 'S1 · One unknown height',
   'Find the height of $x$, every current, and the power of each source.',
   fence('S1', [view('S1', names={'t': 'top', 'x': '$x$', '0': 'bottom'}, cols=[('V1', 0), ('R1', 1), ('R2', 1), ('I1', 2)],
                     straight_off=True, steps=[
       ("Rule 1: ground the bottom wire. Rule 2: the source puts the top at $10\\,\\mathrm{V}$.", []),
       ("Rule 3: the current source pushes $1\\,\\mathrm{A}$ into $x$, whatever $x$'s height is. Call that height $x$.", ['eI1']),
       ("Rules 4 and 5: KCL at $x$. In through the $2\\,\\Omega$, plus the $1\\,\\mathrm{A}$ = out down the $4\\,\\Omega$: $\\dfrac{10-x}{2}+1=\\dfrac{x}{4}$, so $x=8\\,\\mathrm{V}$.", ['x']),
       ("Currents = fall ÷ R: the $2\\,\\Omega$ falls $2\\,\\mathrm{V}$ ($1\\,\\mathrm{A}$), the $4\\,\\Omega$ falls $8\\,\\mathrm{V}$ ($2\\,\\mathrm{A}$). KCL: $1+1=2$.", ['eR1', 'eR2', 'eV1']),
       ("Power = current × height change. Both sources climb: $(1)(10)+(1)(8)=18\\,\\mathrm{W}$. The falls absorb $(2)(1)+(8)(2)=18\\,\\mathrm{W}$.", []),
   ])], spoiler=False, inline=True),
   [S('Ground the bottom wire; the top is at $10\\,\\mathrm{V}$. Call the middle height $x$.'),
    S('KCL at $x$: in through the $2\\,\\Omega$ plus the $1\\,\\mathrm{A}$ pushed in = out down the $4\\,\\Omega$.',
      '\\frac{10-x}{2}+1=\\frac{x}{4}\\;\\Rightarrow\\;20-2x+4=x\\;\\Rightarrow\\;x=8\\,\\mathrm{V}'),
    S('Currents = fall ÷ R.', 'i_{2\\Omega}=\\frac{10-8}{2}=1\\,\\mathrm{A},\\qquad i_{4\\Omega}=\\frac{8}{4}=2\\,\\mathrm{A}'),
    S('Power: climbs = falls.', '(10)(1)+(8)(1)=18\\,\\mathrm{W}=(2)(1)+(8)(2)')],
   '$x=8\\,\\mathrm{V}$; $1\\,\\mathrm{A}$ through the $2\\,\\Omega$, $2\\,\\mathrm{A}$ down the $4\\,\\Omega$. The sources deliver $10+8=18\\,\\mathrm{W}$; the resistors absorb $18\\,\\mathrm{W}$.')
CO('info', "**Signs, in two lines.** A labelled voltage whose $+$ sits on the **low** end is negative. A current that comes out negative flows **opposite** its arrow; keep the arrow.")

# ---------------------------------------------------------------- Topic 1
H(1, 'Topic 1: Circuit terminology', lec(3, 6, 7, 8))
T(['Term', 'Meaning', 'In heights'], [
    ['Node', 'a connected wire, however many bends', 'one level'],
    ['Essential node', 'three or more elements meet', 'an unknown height to solve for (minus ground)'],
    ['Branch / essential branch', 'one element / a path between essential nodes', 'one element / one column between two unknown levels'],
    ['Loop / mesh', 'a closed path / a loop with no loop inside it', 'a loop walk returns to its starting height'],
    ['Planar', 'can be drawn with no crossings', 'needed for meshes only'],
])
EQ('\\text{node equations}=n_e-1,\\qquad \\text{meshes}\\;M=b-n+1=b_e-n_e+1')
L(['Node-voltage method: one KCL per essential node **except ground** ($n_e-1$ unknown heights).',
   'Mesh-current method: one KVL per mesh ($M$ loop currents). Planar circuits only.',
   'A crossing without a dot is not a connection. Two elements between the same two nodes are still two branches.',
   'A known source fixes one unknown: a voltage source to ground fixes a height; a current source on a mesh edge fixes a mesh current.'])
EX('struct', 'Reading a circuit\'s structure (Lecture 3)',
   'Count the nodes, essential nodes, branches, essential branches and meshes.',
   '```schematic\n' + r'''V1 0,6 -> 0,3 "$v_1$"
V2 0,3 -> 0,0 "$v_2$"
R1 0,6 -> 4,6 "$R_1$"
R5 4,6 -> 4,3 "$R_5$"
R2 0,3 -> 2,3 "$R_2$"
R3 2,3 -> 4,3 "$R_3$"
R6 4,3 -> 4,0 "$R_6$"
R4 0,0 -> 4,0 "$R_4$"
wire 4,6 -> 9,6
wire 4,0 -> 9,0
R7 6.5,6 -> 6.5,0 "$R_7$"
I1 9,0 -> 9,6 "$I$"
label 0,6 "$a$" left
label 4,6 "$b$" above
label 0,3 "$c$" left
label 2,3 "$d$" above
label 4,3 "$e$" right
label 0,0 "$f$" left
label 4,0 "$g$" below''' + '\n```',
   [S('Nodes $a$–$g$; ten elements, so ten branches.', 'n=7,\\qquad b=10'),
    S('Essential nodes meet three or more elements: $b$, $c$, $e$, $g$. ($a$, $d$, $f$ only join two.)', 'n_e=4'),
    S('Essential branches: $c$–$a$–$b$, $c$–$f$–$g$, $c$–$d$–$e$, $b$–$e$, $e$–$g$, and the two $b$–$g$ paths ($R_7$ and $I$).', 'b_e=7'),
    S('Meshes, checked both ways.', 'M=10-7+1=7-4+1=4')],
   '$7$ nodes, $4$ essential nodes, $10$ branches, $7$ essential branches, $4$ meshes. Node-voltage would need $4-1=3$ unknown heights.',
   lec(7))
PR('p41', 'Try it 1 · Count everything (Textbook P4.1)', 'introductory',
   'Find the number of **(a)** branches, **(b)** branches with unknown current, **(c)** essential branches, **(d)** essential branches with unknown current, **(e)** nodes, **(f)** essential nodes, **(g)** meshes.',
   '```schematic\n' + r'''V1 0,4 -> 0,0 "$18\,\mathrm{V}$"
wire 0,4 -> 0,7
R1 0,7 -> 10,7 "$R_1$"
wire 10,7 -> 10,4
R2 0,6 -> 3,6 "$R_2$" i_rev="$i_\Delta$"
R3 0,4 -> 3,4 "$R_3$"
wire 3,6 -> 3,4
G1 3,6 -> 10,6 "$2v_\Delta$"
R6 3,4 -> 3,0 "$R_6$" v="$v_\Delta$"
R4 3,4 -> 6,4 "$R_4$"
R5 6,4 -> 10,4 "$R_5$"
E1 6,4 -> 6,0 "$25i_\Delta$"
R7 10,4 -> 10,0 "$R_7$"
wire 10,4 -> 13,4
I1 13,0 -> 13,4 "$5\,\mathrm{mA}$"
wire 13,0 -> 0,0
label 0,4 "$a$" left
label 3,6 "$b$" above
label 6,4 "$c$" above
label 10,7 "$d$" right
label 13,0 "$e$" right''' + '\n```',
   [S('Branches: seven resistors and four sources.', 'b=11'),
    S('Only the $5\\,\\mathrm{mA}$ source has a known current; the diamond $2v_\\Delta$ depends on an unknown, so it does not count as known.', 'b_{\\text{unknown}}=10'),
    S('Nodes: $a$ (top-left wire), $b$, $c$, $d$ and the bottom wire $e$. Each joins at least three elements.', 'n=n_e=5'),
    S('Every branch runs between essential nodes, so every branch is essential.', 'b_e=11,\\quad b_{e,\\text{unknown}}=10'),
    S('Meshes.', 'M=b-n+1=11-5+1=7')],
   '**(a)** $11$ **(b)** $10$ **(c)** $11$ **(d)** $10$ **(e)** $5$ **(f)** $5$ **(g)** $7$', tb('4.1'))

# ---------------------------------------------------------------- Topic 2
H(1, 'Topic 2: The node-voltage method', lec(11, 12, 13))
L(['**Recipe:** ground one node → name every unknown height → KCL at each (currents out $=\\dfrac{v_k-v_j}{R}$) → solve → currents = fall ÷ R → check power.',
   'Pick ground at the node with the most connections, or the $-$ end of a voltage source (then that source fixes a height for free).',
   '**Averaging rule:** a node joined only by resistors sits at the **conductance-weighted average** of its neighbours\' heights, lifted by any current pushed into it. One unknown node? This *is* the KCL answer.',
   'So with only voltage sources and resistors, no node rises above the highest source. **Current sources can** push a node higher.'])
EQ('\\text{KCL at }k:\\;\\sum_j\\frac{v_k-v_j}{R_{kj}}=I_{\\text{in}}\\qquad\\Longleftrightarrow\\qquad v_k=\\frac{\\sum_j G_j v_j+I_{\\text{in}}}{\\sum_j G_j},\\quad G=\\frac{1}{R}')
EX('lec_one', 'One node, three neighbours (Lecture 3)',
   'Use the node-voltage method to find $i_a$, $i_b$ and $i_c$.',
   fence('lec_one', [view('lec_one', names={'s': 'top', 'a': '$a$', '0': 'bottom'},
                          cols=[('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2), ('I1', 3)], steps=[
       ("Ground the bottom wire; the source fixes the left end of the $5\\,\\Omega$ at $50\\,\\mathrm{V}$. Only $a$'s height is unknown.", []),
       ("Averaging rule: $a$ is joined to $50\\,\\mathrm{V}$ (through $5\\,\\Omega$) and to ground twice ($10$, $40\\,\\Omega$), with $3\\,\\mathrm{A}$ pushed in: $a=\\dfrac{50/5+3}{1/5+1/10+1/40}=\\dfrac{13}{0.325}=40\\,\\mathrm{V}$.", ['a']),
       ("Currents = fall ÷ R: $i_a=\\dfrac{10}{5}=2$, $i_b=\\dfrac{40}{10}=4$, $i_c=\\dfrac{40}{40}=1\\,\\mathrm{A}$. KCL at $a$: $2+3=4+1$.", ['eR1', 'eR2', 'eR3', 'eV1', 'eI1']),
       ("Power: the voltage source lifts $2\\,\\mathrm{A}$ through $50\\,\\mathrm{V}$ ($100\\,\\mathrm{W}$), the current source $3\\,\\mathrm{A}$ through $40\\,\\mathrm{V}$ ($120\\,\\mathrm{W}$); the falls absorb $20+160+40=220\\,\\mathrm{W}$.", []),
   ])], spoiler=False),
   [S('Ground the bottom wire; only $a$ is unknown. KCL at $a$, currents out; the $3\\,\\mathrm{A}$ comes in.',
      '\\frac{v_a-50}{5}+\\frac{v_a}{10}+\\frac{v_a}{40}=3'),
    S('Multiply by 40 and solve.', '8v_a-400+4v_a+v_a=120\\;\\Rightarrow\\;v_a=40\\,\\mathrm{V}'),
    S('Currents = fall ÷ R, in the arrow directions.', 'i_a=\\frac{50-40}{5}=2\\,\\mathrm{A},\\quad i_b=4\\,\\mathrm{A},\\quad i_c=1\\,\\mathrm{A}'),
    S('Check KCL at $a$.', '2+3=4+1')],
   '$v_a=40\\,\\mathrm{V}$; $i_a=2\\,\\mathrm{A}$, $i_b=4\\,\\mathrm{A}$, $i_c=1\\,\\mathrm{A}$', lec(13))
EX('lec_two', 'Two unknown heights (Lecture 3)',
   'Use the node-voltage method to find $v_1$ and $v_2$.',
   fence('lec_two', [view('lec_two', names={'s': 'source +', 'n1': 'node 1', 'n2': 'node 2', '0': 'bottom'},
                          cols=[('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2), ('R4', 3), ('I1', 4)],
                          refs={'R2': ('n1', '$v_1$'), 'R4': ('n2', '$v_2$')}, rails=('I1',), steps=[
       ("Ground the bottom wire; the source puts its $+$ end at $10\\,\\mathrm{V}$. Two unknown heights: $v_1$ and $v_2$.", []),
       ("KCL at each (out = in). Node 1: $\\dfrac{v_1-10}{1}+\\dfrac{v_1}{5}+\\dfrac{v_1-v_2}{2}=0$. Node 2: $\\dfrac{v_2-v_1}{2}+\\dfrac{v_2}{10}=2$.", []),
       ("Solve: $v_1=\\dfrac{100}{11}=9.09\\,\\mathrm{V}$, $v_2=\\dfrac{120}{11}=10.91\\,\\mathrm{V}$. Node 2 sits **above** the $10\\,\\mathrm{V}$ source: the current source pumped it there.", ['n1', 'n2']),
       ("Currents = fall ÷ R: $0.909\\,\\mathrm{A}$ through the $1\\,\\Omega$, $1.818\\,\\mathrm{A}$ down the $5\\,\\Omega$, $0.909\\,\\mathrm{A}$ from node 2 **back** to node 1, $1.091\\,\\mathrm{A}$ down the $10\\,\\Omega$.", ['eR1', 'eR2', 'eR3', 'eR4', 'eV1', 'eI1']),
       ("Power: climbs $(0.909)(10)+(2)(10.91)=30.91\\,\\mathrm{W}$; the four falls absorb the same.", []),
   ])], spoiler=False),
   [S('Ground the bottom wire. KCL at node 1 (currents out).', '\\frac{v_1-10}{1}+\\frac{v_1}{5}+\\frac{v_1-v_2}{2}=0'),
    S('KCL at node 2; the $2\\,\\mathrm{A}$ comes in.', '\\frac{v_2-v_1}{2}+\\frac{v_2}{10}=2'),
    S('Multiply both by 10.', '17v_1-5v_2=100,\\qquad -5v_1+6v_2=20'),
    S('Solve.', 'v_1=\\frac{100}{11}\\approx9.09\\,\\mathrm{V},\\qquad v_2=\\frac{120}{11}\\approx10.91\\,\\mathrm{V}'),
    S('The $2\\,\\Omega$ current from 1 to 2 is negative: it really flows from 2 to 1.', 'i_{1\\to2}=\\frac{v_1-v_2}{2}=-\\frac{10}{11}\\,\\mathrm{A}')],
   '$v_1=\\dfrac{100}{11}\\approx9.09\\,\\mathrm{V}$, $v_2=\\dfrac{120}{11}\\approx10.91\\,\\mathrm{V}$', lec(12))
PR('ap413', 'Try it 2 · One node above both sources (Assessment AP 4.13)', 'introductory',
   'Use the node-voltage method to find $v_1$ and the power delivered by the $2\\,\\mathrm{A}$ current source.',
   fence('ap413', [view('ap413', names={'s': 'left source +', 'n1': '$v_1$', 'r': 'right source +', '0': 'bottom'},
                        cols=[('I1', 0), ('R1', 1), ('V1', 1), ('R2', 2), ('V2', 2)], rails=('I1',), steps=[
       ("Ground the bottom wire. The sources fix the two ends: left $+$ at $20\\,\\mathrm{V}$, right $+$ at $25\\,\\mathrm{V}$. Only $v_1$ is unknown.", []),
       ("Averaging rule: $v_1$ hangs between $20\\,\\mathrm{V}$ (through $15\\,\\Omega$) and $25\\,\\mathrm{V}$ (through $10\\,\\Omega$), with $2\\,\\mathrm{A}$ pushed in: $v_1=\\dfrac{20/15+25/10+2}{1/15+1/10}=35\\,\\mathrm{V}$.", ['n1']),
       ("$v_1$ is above both sources, so current falls **away** from it on both sides: $\\dfrac{15}{15}=1\\,\\mathrm{A}$ left, $\\dfrac{10}{10}=1\\,\\mathrm{A}$ right. KCL: $2=1+1$.", ['eR1', 'eR2', 'eI1']),
       ("Both voltage sources have current falling into them: they **absorb** $20\\,\\mathrm{W}$ and $25\\,\\mathrm{W}$. The current source lifts $2\\,\\mathrm{A}$ through $35\\,\\mathrm{V}$: it delivers $70\\,\\mathrm{W}=20+25+15+10$.", ['eV1', 'eV2']),
   ])]),
   [S('Ground the bottom wire. KCL at $v_1$ (currents out); the $2\\,\\mathrm{A}$ comes in.', '\\frac{v_1-20}{15}+\\frac{v_1-25}{10}=2'),
    S('Multiply by 30.', '2v_1-40+3v_1-75=60\\;\\Rightarrow\\;v_1=35\\,\\mathrm{V}'),
    S('The source lifts $2\\,\\mathrm{A}$ from $0$ to $35\\,\\mathrm{V}$.', 'p_{2\\mathrm{A}}=(35)(2)=70\\,\\mathrm{W}\\text{ delivered}')],
   '$v_1=35\\,\\mathrm{V}$; the $2\\,\\mathrm{A}$ source delivers $70\\,\\mathrm{W}$.', ap(9, 10))
PR('p413', 'Try it 3 · Two current sources, no fixed height (Textbook P4.13)', 'introductory',
   'Use the node-voltage method to find $v_1$ and $v_2$.',
   fence('p413', [view('p413', names={'n1': '$v_1$', 'n2': '$v_2$', '0': 'bottom'},
                       cols=[('I2', 0), ('R4', 1), ('R3', 2), ('R2', 3), ('R1', 4), ('I1', 5)],
                       refs={'R1': ('n1', '$v_1$'), 'R4': ('n2', '$v_2$')}, rails=('I2',), steps=[
       ("Ground the bottom wire. No voltage source, so no height is fixed: $v_1$ and $v_2$ are both unknown.", []),
       ("KCL, currents out = in. Node 1: $\\dfrac{v_1}{125}+\\dfrac{v_1-v_2}{25}+2.4=0$. Node 2: $\\dfrac{v_2}{250}+\\dfrac{v_2}{375}+\\dfrac{v_2-v_1}{25}=3.2$.", []),
       ("Solve: $v_1=25\\,\\mathrm{V}$, $v_2=90\\,\\mathrm{V}$.", ['n1', 'n2']),
       ("Currents = fall ÷ R: $2.6\\,\\mathrm{A}$ falls from node 2 to node 1; node 1 sends $0.2\\,\\mathrm{A}$ down the $125\\,\\Omega$ and $2.4\\,\\mathrm{A}$ down through the left source.", ['eR1', 'eR2', 'eR3', 'eR4', 'eI1', 'eI2']),
       ("Power: only the $3.2\\,\\mathrm{A}$ source climbs ($288\\,\\mathrm{W}$). The $2.4\\,\\mathrm{A}$ source's current falls $25\\,\\mathrm{V}$: it absorbs $60\\,\\mathrm{W}$; the resistors take $228\\,\\mathrm{W}$.", []),
   ])]),
   [S('Ground the bottom wire. KCL at node 1 (out = in; the $2.4\\,\\mathrm{A}$ leaves).', '\\frac{v_1}{125}+\\frac{v_1-v_2}{25}=-2.4'),
    S('KCL at node 2 (the $3.2\\,\\mathrm{A}$ comes in).', '\\frac{v_2}{250}+\\frac{v_2}{375}+\\frac{v_2-v_1}{25}=3.2'),
    S('Clear fractions (×125 and ×750).', '6v_1-5v_2=-300,\\qquad -30v_1+35v_2=2400'),
    S('Add 5× the first to the second.', '10v_2=900\\;\\Rightarrow\\;v_2=90\\,\\mathrm{V},\\quad v_1=25\\,\\mathrm{V}')],
   '$v_1=25\\,\\mathrm{V}$, $v_2=90\\,\\mathrm{V}$', tb('4.13'))

# ---------------------------------------------------------------- Topic 3
H(1, 'Topic 3: Fixed heights, supernodes and dependent sources', lec(14, 15, 16, 17))
L(['**Voltage source to ground:** it fixes that node\'s height. No equation for it.',
   '**Voltage source between two unknown nodes (supernode):** a **rigid rod**. It locks their difference ($v_p-v_q=V_s$) but the rod floats until **KCL around the whole rod** pins it. The rod\'s own current stays inside: leave it out.',
   '**Dependent source:** write its control in node heights first (e.g. $i_\\Phi=\\dfrac{v_a-v_b}{R}$), then treat it like any source. A dependent voltage source is a rod whose length you read off the picture.',
   'Dependent sources often **absorb** (current falls through them). Read it off the arrow colour.'])
EQ('\\text{rod: }v_p-v_q=V_s\\qquad\\qquad \\text{KCL around the rod: }\\sum i_{\\text{out of the rod}}=0')
EX('lec_known', 'A source to ground fixes a height (Lecture 3)',
   'Solve for $v_1$ and $v_2$.',
   fence('lec_known', [view('lec_known', names={'n1': 'node 1', 'n2': 'node 2', '0': 'bottom'},
                            cols=[('V1', 0), ('R1', 1), ('R2', 2), ('R3', 3), ('I1', 4)],
                            refs={'R1': ('n1', '$v_1$'), 'R3': ('n2', '$v_2$')}, rails=('I1',), steps=[
       ("Ground the bottom wire. The $100\\,\\mathrm{V}$ source runs from ground straight to node 1: $v_1=100\\,\\mathrm{V}$ is **given**. No equation needed.", ['n1']),
       ("One unknown left. KCL at node 2: $\\dfrac{v_2-100}{10}+\\dfrac{v_2}{50}=5$, so $v_2=125\\,\\mathrm{V}$, above the source again.", ['n2']),
       ("Currents = fall ÷ R: $2.5\\,\\mathrm{A}$ from node 2 down to node 1, $2.5\\,\\mathrm{A}$ down the $50\\,\\Omega$; node 1 sends $4\\,\\mathrm{A}$ down the $25\\,\\Omega$, so the source only supplies $4-2.5=1.5\\,\\mathrm{A}$.", ['eR1', 'eR2', 'eR3', 'eV1', 'eI1']),
       ("Power: climbs $(1.5)(100)+(5)(125)=775\\,\\mathrm{W}$; falls $400+62.5+312.5=775\\,\\mathrm{W}$.", []),
   ])], spoiler=False),
   [S('Ground the bottom wire. The $100\\,\\mathrm{V}$ source sits between node 1 and ground.', 'v_1=100\\,\\mathrm{V}'),
    S('KCL at node 2 only (the $5\\,\\mathrm{A}$ comes in).', '\\frac{v_2-100}{10}+\\frac{v_2}{50}=5'),
    S('Multiply by 50.', '5v_2-500+v_2=250\\;\\Rightarrow\\;v_2=125\\,\\mathrm{V}')],
   '$v_1=100\\,\\mathrm{V}$, $v_2=125\\,\\mathrm{V}$', lec(15))
EX('lec_dep', 'A dependent source: control first (Lecture 3)',
   'Use the node-voltage method to find the power dissipated in the $5\\,\\Omega$ resistor.',
   fence('lec_dep', [view('lec_dep', names={'s': 'source +', 'a': '$a$', 'b': '$b$', 'c': '$c$', '0': 'bottom'},
                          cols=[('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2), ('R4', 2), ('R5', 3), ('E1', 3)],
                          elabel={'E1': '$8i_\\Phi$'}, steps=[
       ("Ground the bottom wire; the $20\\,\\mathrm{V}$ source fixes the left end. Unknown heights $a$, $b$, and $c$, but $c$ is not free: the diamond holds it at $8i_\\Phi$, with $i_\\Phi=\\dfrac{a-b}{5}$.", []),
       ("KCL at $a$ and $b$, with $c=1.6(a-b)$: $\\dfrac{a-20}{2}+\\dfrac{a}{20}+\\dfrac{a-b}{5}=0$ and $\\dfrac{b-a}{5}+\\dfrac{b}{10}+\\dfrac{b-c}{2}=0$. So $a=16\\,\\mathrm{V}$, $b=10\\,\\mathrm{V}$.", ['a', 'b']),
       ("Control first: $i_\\Phi=\\dfrac{16-10}{5}=1.2\\,\\mathrm{A}$, so the diamond's step is $8(1.2)=9.6\\,\\mathrm{V}$: $c=9.6\\,\\mathrm{V}$.", ['c', 'eR3', 'eE1']),
       ("The other falls: $2\\,\\mathrm{A}$ through the $2\\,\\Omega$, $0.8$ and $1\\,\\mathrm{A}$ down the $20$ and $10\\,\\Omega$, $0.2\\,\\mathrm{A}$ from $b$ to $c$. That $0.2\\,\\mathrm{A}$ falls through the diamond: it **absorbs** $1.92\\,\\mathrm{W}$.", ['eR1', 'eR2', 'eR4', 'eR5', 'eV1']),
       ("The $5\\,\\Omega$ absorbs $(1.2)(6)=7.2\\,\\mathrm{W}$. Check: the source lifts $2\\,\\mathrm{A}$ through $20\\,\\mathrm{V}$, $40\\,\\mathrm{W}=8+12.8+7.2+10+0.08+1.92$.", []),
   ])], spoiler=False),
   [S('Ground the bottom wire. Control first: the diamond fixes $v_c$ in terms of $a$ and $b$.', 'i_\\Phi=\\frac{v_a-v_b}{5},\\qquad v_c=8i_\\Phi=1.6(v_a-v_b)'),
    S('KCL at $a$ and $b$.', '\\begin{aligned}&\\frac{v_a-20}{2}+\\frac{v_a}{20}+\\frac{v_a-v_b}{5}=0\\\\&\\frac{v_b-v_a}{5}+\\frac{v_b}{10}+\\frac{v_b-v_c}{2}=0\\end{aligned}'),
    S('Substitute $v_c$ and collect.', '0.75v_a-0.2v_b=10,\\qquad -v_a+1.6v_b=0'),
    S('Solve.', 'v_a=16\\,\\mathrm{V},\\quad v_b=10\\,\\mathrm{V},\\quad i_\\Phi=1.2\\,\\mathrm{A}'),
    S('Power in the $5\\,\\Omega$.', 'p_{5\\Omega}=(1.2)^2(5)=7.2\\,\\mathrm{W}')],
   '$v_a=16\\,\\mathrm{V}$, $v_b=10\\,\\mathrm{V}$, $i_\\Phi=1.2\\,\\mathrm{A}$; $p_{5\\Omega}=7.2\\,\\mathrm{W}$', lec(14))
EX('lec_super', 'A supernode is a rigid rod (Lecture 3)',
   'Use a supernode around $b$ and $c$ to find the node voltages.',
   fence('lec_super', [view('lec_super', names={'a': '$a$', 'b': '$b$', 'c': '$c$', '0': 'bottom'},
                            cols=[('I1', 0), ('R4', 1), ('E1', 2), ('R3', 2), ('R2', 3), ('R1', 3), ('V1', 4)],
                            elabel={'E1': '$10i_\\Phi$'}, rails=('I1',), steps=[
       ("Ground the bottom wire; the $50\\,\\mathrm{V}$ source fixes $a=50\\,\\mathrm{V}$. The diamond joins two unknown nodes: a **rigid rod**, $c=b+10i_\\Phi$.", ['a']),
       ("Control first: $i_\\Phi$ runs from $b$ to $a$ through $5\\,\\Omega$, so $i_\\Phi=\\dfrac{b-50}{5}$ and the rod is $c=b+2(b-50)=3b-100$.", []),
       ("KCL around the whole rod (the diamond's own current stays inside): $\\dfrac{b-50}{5}+\\dfrac{b}{50}+\\dfrac{c}{100}=4$. With $c=3b-100$: $b=60$, $c=80\\,\\mathrm{V}$.", ['b', 'c', 'eE1']),
       ("Currents = fall ÷ R: $i_\\Phi=2\\,\\mathrm{A}$ from $b$ to $a$, $1.2\\,\\mathrm{A}$ down the $50\\,\\Omega$, $0.8\\,\\mathrm{A}$ down the $100\\,\\Omega$. KCL at $c$: the other $3.2\\,\\mathrm{A}$ goes **down through** the rod.", ['eR2', 'eR3', 'eR4', 'eI1']),
       ("At $a$, $2\\,\\mathrm{A}$ arrives but the $40\\,\\Omega$ takes only $1.25\\,\\mathrm{A}$: $0.75\\,\\mathrm{A}$ falls into the $50\\,\\mathrm{V}$ source, which absorbs $37.5\\,\\mathrm{W}$. Only the $4\\,\\mathrm{A}$ source climbs: $320\\,\\mathrm{W}$.", ['eR1', 'eV1']),
   ])], spoiler=False),
   [S('Ground the bottom wire. The grounded source fixes $v_a$; the control uses the leftward arrow.', 'v_a=50\\,\\mathrm{V},\\qquad i_\\Phi=\\frac{v_b-50}{5}'),
    S('The rod: the diamond fixes $v_c-v_b$.', 'v_c-v_b=10i_\\Phi=2(v_b-50)\\;\\Rightarrow\\;v_c=3v_b-100'),
    S('KCL around the rod: only currents crossing its boundary.', '\\frac{v_b-50}{5}+\\frac{v_b}{50}+\\frac{v_c}{100}=4'),
    S('Substitute and solve.', '0.25v_b=15\\;\\Rightarrow\\;v_b=60\\,\\mathrm{V},\\quad v_c=80\\,\\mathrm{V},\\quad i_\\Phi=2\\,\\mathrm{A}')],
   '$v_a=50\\,\\mathrm{V}$, $v_b=60\\,\\mathrm{V}$, $v_c=80\\,\\mathrm{V}$, $i_\\Phi=2\\,\\mathrm{A}$', lec(16, 17))
CO('warning', "**Supernode traps.** (1) The two rod ends are **not** equal: they differ by $V_s$. (2) Never write the rod's own current into the KCL. (3) Reversing a control arrow flips its sign: $\\dfrac{v_b-v_a}{R}$ vs $\\dfrac{v_a-v_b}{R}$.")
PR('p427', 'Try it 4 · A controlled rod (Textbook P4.27)', 'intermediate',
   'Use the node-voltage method to find $v$.',
   fence('p427', [view('p427', names={'a': '$a$', 'b': '$b$ ($v$)', 'c': '$c$', 'd': '$12\\,\\mathrm{V}$ node', '0': 'bottom'},
                       cols=[('I1', 0), ('R1', 1), ('R2', 2), ('R3', 2), ('E1', 3), ('R4', 4), ('R5', 5), ('V1', 6)],
                       elabel={'E1': '$i_x$'}, refs={'R3': ('b', '$v$')}, rails=('I1',), steps=[
       ("Ground the bottom wire; the $12\\,\\mathrm{V}$ source fixes its $+$ end. Unknowns $a$, $v$ and $c$, but the diamond is a rod: $c=v+i_x$ (gain $1\\,\\Omega$).", []),
       ("Control first: $i_x=\\dfrac{a}{7.5}$. KCL at $a$: $\\dfrac{a}{7.5}+\\dfrac{a-v}{2.5}=4.8$, so $a=9+0.75v$.", []),
       ("KCL around the rod $b$–$c$: $\\dfrac{v-a}{2.5}+\\dfrac{v}{10}+\\dfrac{c}{2.5}+\\dfrac{c-12}{1}=0$, with $c=1.1v+1.2$. Solving: $v=8$, $a=15$, $c=10\\,\\mathrm{V}$.", ['a', 'b', 'c', 'eE1']),
       ("Currents = fall ÷ R: $i_x=2\\,\\mathrm{A}$, $2.8\\,\\mathrm{A}$ from $a$ to $b$, $0.8\\,\\mathrm{A}$ down the $10\\,\\Omega$, $4\\,\\mathrm{A}$ down the $2.5\\,\\Omega$ at $c$, $2\\,\\mathrm{A}$ **into** $c$ from the $12\\,\\mathrm{V}$ side. KCL around the rod: $2.8+2=0.8+4$.", ['eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eV1', 'eI1']),
       ("Power: three climbs, $72$ (current source) $+24$ ($12\\,\\mathrm{V}$ source) $+4\\,\\mathrm{W}$ ($2\\,\\mathrm{A}$ up the diamond's $2\\,\\mathrm{V}$ step). The falls absorb $30+19.6+6.4+40+4=100\\,\\mathrm{W}$.", []),
   ])]),
   [S('Ground the bottom wire. $b$ and $c$ form a supernode (the diamond joins them). Control: $i_x$ runs down the $7.5\\,\\Omega$.', 'i_x=\\frac{v_a}{7.5},\\qquad v_c-v=(1\\,\\Omega)\\,i_x'),
    S('KCL at $a$ (the $4.8\\,\\mathrm{A}$ comes in).', '\\frac{v_a}{7.5}+\\frac{v_a-v}{2.5}=4.8\\;\\Rightarrow\\;v_a=9+0.75v'),
    S('So the rod is', 'v_c=v+\\frac{v_a}{7.5}=1.1v+1.2'),
    S('KCL around the rod.', '\\frac{v-v_a}{2.5}+\\frac{v}{10}+\\frac{v_c}{2.5}+\\frac{v_c-12}{1}=0'),
    S('Substitute and solve.', '1.74v-13.92=0\\;\\Rightarrow\\;v=8\\,\\mathrm{V},\\quad v_a=15\\,\\mathrm{V},\\quad v_c=10\\,\\mathrm{V}')],
   '$v=8\\,\\mathrm{V}$ (with $v_a=15\\,\\mathrm{V}$, $v_c=10\\,\\mathrm{V}$, $i_x=2\\,\\mathrm{A}$)', tb('4.27'))
PR('ap46', 'Try it 5 · A rod hanging from a source (Assessment AP 4.6)', 'intermediate',
   'Use the node-voltage method to find $v_1$ and $i_\\phi$.',
   fence('ap46', [view('ap46', names={'s': 'source +', 'n1': '$v_1$', 'r': 'right node', '0': 'bottom'},
                       cols=[('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2), ('E1', 3), ('R4', 3)],
                       elabel={'E1': '$6i_\\phi$'}, steps=[
       ("Ground the bottom wire; the $60\\,\\mathrm{V}$ source fixes the left node. The diamond hangs from it: the right node is a rod's length away, $60+6i_\\phi$.", []),
       ("Control: $i_\\phi$ runs from the right node to $v_1$ through $3\\,\\Omega$: $i_\\phi=\\dfrac{60+6i_\\phi-v_1}{3}$, so $v_1=60+3i_\\phi$.", []),
       ("KCL at $v_1$: $\\dfrac{v_1-60}{2}+\\dfrac{v_1}{24}+\\dfrac{v_1-(60+6i_\\phi)}{3}=0$. With step 2: $i_\\phi=-4\\,\\mathrm{A}$, $v_1=48\\,\\mathrm{V}$, right node $36\\,\\mathrm{V}$.", ['n1', 'r', 'eE1']),
       ("The rod points **down**: its step is $6(-4)=-24\\,\\mathrm{V}$. Falls ÷ R: $6\\,\\mathrm{A}$ through the $2\\,\\Omega$, $2\\,\\mathrm{A}$ down the $24\\,\\Omega$, $4\\,\\mathrm{A}$ from $v_1$ to the right node (against $i_\\phi$), $12\\,\\mathrm{A}$ down the right $3\\,\\Omega$.", ['eR1', 'eR2', 'eR3', 'eR4']),
       ("KCL at the right node: $12-4=8\\,\\mathrm{A}$ arrives through the diamond, falling $24\\,\\mathrm{V}$: it absorbs $192\\,\\mathrm{W}$. The $60\\,\\mathrm{V}$ source lifts $14\\,\\mathrm{A}$: $840\\,\\mathrm{W}=72+96+48+432+192$.", ['eV1']),
   ])]),
   [S('Ground the bottom wire. The right node is the $60\\,\\mathrm{V}$ node plus the diamond\'s step.', 'v_r=60+6i_\\phi'),
    S('KCL at $v_1$.', '\\frac{v_1-60}{2}+\\frac{v_1}{24}+\\frac{v_1-(60+6i_\\phi)}{3}=0'),
    S('Control: $i_\\phi$ flows from the right node to $v_1$.', 'i_\\phi=\\frac{60+6i_\\phi-v_1}{3}\\;\\Rightarrow\\;v_1=60+3i_\\phi'),
    S('Substitute and solve.', 'i_\\phi=-4\\,\\mathrm{A},\\qquad v_1=48\\,\\mathrm{V}')],
   '$v_1=48\\,\\mathrm{V}$, $i_\\phi=-4\\,\\mathrm{A}$', ap(5))

# ---------------------------------------------------------------- Topic 4
H(1, 'Topic 4: The mesh-current method', lec(18, 19, 20, 21, 22))
L(['**Recipe:** a clockwise current in each window → one **loop walk** (KVL) per mesh → solve → branch currents → heights → power.',
   '**In heights:** a loop walk is "climbs = falls" around the window. Mesh currents themselves have **no** height: they are bookkeeping. Only branch currents are real.',
   'A resistor shared by two meshes carries the **difference**: $I_k-I_\\ell$ in mesh $k$\'s direction.',
   '**Current source on the edge** of one mesh: it fixes that mesh current (watch the arrow vs clockwise).',
   '**Current source shared** by two meshes: its step is unknown, so the walk **skips** it: walk around both meshes together (supermesh) and add $I_a-I_b=I_s$.',
   'Once branch currents are known, walk down the falls to place every height. That also gives a current source\'s step for free.'])
EQ('\\text{shared }R:\\;i=I_k-I_\\ell,\\qquad\\text{supermesh: }I_a-I_b=I_s')
EX('lec_3mesh', 'Three meshes (Lecture 3)',
   'Use the mesh-current method to find **(a)** the power of each voltage source and **(b)** $v_o$.',
   fence('lec_3mesh', [view('lec_3mesh', names={'s': '$40\\,\\mathrm{V}$ node', 'a': '$a$ ($v_o$)', 'b': '$b$', 'c': '$20\\,\\mathrm{V}$ node', '0': 'bottom'},
                            cols=[('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2), ('R4', 2), ('R5', 3), ('V2', 4)],
                            refs={'R2': ('a', '$v_o$')}, steps=[
       ("Ground the bottom wire; both sources' $+$ ends are fixed: $40\\,\\mathrm{V}$ and $20\\,\\mathrm{V}$.", []),
       ("Clockwise mesh currents $I_1$, $I_2$, $I_3$. Each loop walk, climbs = falls: $10I_1-8I_2=40$, $-8I_1+20I_2-6I_3=0$, $-6I_2+10I_3=-20$.", []),
       ("Solve: $I_1=5.6$, $I_2=2$, $I_3=-0.8\\,\\mathrm{A}$. Branch currents: $5.6\\,\\mathrm{A}$ through the $2\\,\\Omega$, $I_1-I_2=3.6\\,\\mathrm{A}$ down the $8\\,\\Omega$, $2\\,\\mathrm{A}$ through the $6\\,\\Omega$, $I_2-I_3=2.8\\,\\mathrm{A}$ down the other $6\\,\\Omega$, $0.8\\,\\mathrm{A}$ leftward through the $4\\,\\Omega$.", ['eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eV1', 'eV2']),
       ("Walk down the falls: $a=40-(5.6)(2)=28.8\\,\\mathrm{V}=v_o$, $b=28.8-(2)(6)=16.8\\,\\mathrm{V}$. From the right: $20-(0.8)(4)=16.8$ ✓.", ['a', 'b']),
       ("Power: both sources climb, $(5.6)(40)=224\\,\\mathrm{W}$ and $(0.8)(20)=16\\,\\mathrm{W}$ delivered.", []),
   ])], spoiler=False),
   [S('KVL around each mesh, clockwise. Shared resistors carry differences; walking down through the $20\\,\\mathrm{V}$ source is a fall.',
      '\\begin{aligned}&-40+2I_1+8(I_1-I_2)=0\\\\&8(I_2-I_1)+6I_2+6(I_2-I_3)=0\\\\&6(I_3-I_2)+4I_3+20=0\\end{aligned}'),
    S('Collect.', '\\begin{aligned}10I_1-8I_2&=40\\\\-8I_1+20I_2-6I_3&=0\\\\-6I_2+10I_3&=-20\\end{aligned}'),
    S('Solve.', 'I_1=5.6\\,\\mathrm{A},\\quad I_2=2\\,\\mathrm{A},\\quad I_3=-0.8\\,\\mathrm{A}'),
    S('**(b)** The $8\\,\\Omega$ carries $I_1-I_2$.', 'v_o=8(5.6-2)=28.8\\,\\mathrm{V}'),
    S('**(a)** Absorbed power uses the current entering $+$. Negative = delivering.', 'p_{40\\mathrm{V}}=-40(5.6)=-224\\,\\mathrm{W},\\qquad p_{20\\mathrm{V}}=20(-0.8)=-16\\,\\mathrm{W}')],
   '**(a)** The $40\\,\\mathrm{V}$ source delivers $224\\,\\mathrm{W}$; the $20\\,\\mathrm{V}$ source delivers $16\\,\\mathrm{W}$. **(b)** $v_o=28.8\\,\\mathrm{V}$', lec(20))
EX('lec_meshdep', 'A dependent source in a mesh (Lecture 3)',
   'Use the mesh-current method to find the power dissipated in the $4\\,\\Omega$ resistor. Mesh $a$ is lower-left, $b$ the top triangle, $c$ lower-right (all clockwise).',
   fence('lec_meshdep', [view('lec_meshdep', names={'s': 'source +', 'a': '$a$', 'b': '$b$', '0': 'bottom'},
                              cols=[('V1', 0), ('R1', 1), ('R3', 1), ('R2', 2), ('E1', 2), ('R4', 3)],
                              elabel={'E1': '$15i_\\phi$'}, steps=[
       ("Ground the bottom wire; the $50\\,\\mathrm{V}$ source fixes the left node. The diamond's step is $15i_\\phi$, and $i_\\phi$ is the $20\\,\\Omega$ current, $I_a-I_c$.", []),
       ("Three loop walks with the control substituted: $25I_a-5I_b-20I_c=50$, $-5I_a+10I_b-4I_c=0$, $-5I_a-4I_b+9I_c=0$.", []),
       ("Solve: $I_a=29.6$, $I_b=26$, $I_c=28\\,\\mathrm{A}$, so $i_\\phi=1.6\\,\\mathrm{A}$ and the diamond's step is $24\\,\\mathrm{V}$.", ['eE1', 'eR3']),
       ("Branch currents → heights: the $1\\,\\Omega$ carries $I_b=26\\,\\mathrm{A}$, so $b=50-26=24\\,\\mathrm{V}$ (the diamond's top ✓). The $5\\,\\Omega$ carries $3.6\\,\\mathrm{A}$: $a=32\\,\\mathrm{V}$. The $4\\,\\Omega$ carries $I_c-I_b=2\\,\\mathrm{A}$ from $a$ to $b$.", ['a', 'b', 'eR1', 'eR2', 'eR4', 'eV1']),
       ("The $4\\,\\Omega$ absorbs $(2)(8)=16\\,\\mathrm{W}$. The diamond has $28\\,\\mathrm{A}$ falling through it: it absorbs $672\\,\\mathrm{W}$ of the $1480\\,\\mathrm{W}$ the source delivers.", []),
   ])], spoiler=False),
   [S('Control first: both lower meshes cross the $20\\,\\Omega$.', 'i_\\phi=I_a-I_c'),
    S('Loop walks.', '\\begin{aligned}&-50+5(I_a-I_b)+20(I_a-I_c)=0\\\\&I_b+4(I_b-I_c)+5(I_b-I_a)=0\\\\&15i_\\phi+20(I_c-I_a)+4(I_c-I_b)=0\\end{aligned}'),
    S('Substitute the control and collect.', '\\begin{aligned}25I_a-5I_b-20I_c&=50\\\\-5I_a+10I_b-4I_c&=0\\\\-5I_a-4I_b+9I_c&=0\\end{aligned}'),
    S('Solve.', 'I_a=29.6\\,\\mathrm{A},\\quad I_b=26\\,\\mathrm{A},\\quad I_c=28\\,\\mathrm{A},\\quad i_\\phi=1.6\\,\\mathrm{A}'),
    S('The $4\\,\\Omega$ carries $I_c-I_b$.', 'p_{4\\Omega}=4(28-26)^2=16\\,\\mathrm{W}')],
   '$i_\\phi=1.6\\,\\mathrm{A}$; $p_{4\\Omega}=16\\,\\mathrm{W}$', lec(21))
EX('ap412', 'A supermesh skips the current source (Assessment AP 4.12)',
   'Use the mesh-current method to find the power dissipated in the $1\\,\\Omega$ resistor. Mesh $a$ is lower-left, $b$ the top, $c$ lower-right (all clockwise).',
   fence('ap412', [view('ap412', names={'s': 'source +', 'm': '$m$', 'r': '$r$', 'q': '$q$', '0': 'bottom'},
                        cols=[('V1', 0), ('R1', 1), ('I1', 2), ('R3', 2), ('R2', 3), ('V2', 4), ('R4', 5)], steps=[
       ("Ground the bottom wire; the $10\\,\\mathrm{V}$ source fixes the top-left node at $10\\,\\mathrm{V}$.", []),
       ("The $2\\,\\mathrm{A}$ source is shared by meshes $a$ and $b$. Its step is unknown, so the walk **skips** it: go around both meshes at once (supermesh) and let the source supply the other equation, $I_a-I_b=2$.", []),
       ("Supermesh walk: $-10+2I_b+2(I_b-I_c)+2(I_a-I_c)=0$. Mesh $c$: $-6+I_c+2(I_c-I_a)+2(I_c-I_b)=0$. Solve: $I_a=7$, $I_b=5$, $I_c=6\\,\\mathrm{A}$.", []),
       ("Branch currents: top $2\\,\\Omega$ $I_b=5\\,\\mathrm{A}$; middle $2\\,\\Omega$ $I_a-I_c=1\\,\\mathrm{A}$ down; right $2\\,\\Omega$ $I_c-I_b=1\\,\\mathrm{A}$; $1\\,\\Omega$ $I_c=6\\,\\mathrm{A}$.", ['eR1', 'eR2', 'eR3', 'eR4', 'eV1', 'eV2', 'eI1']),
       ("Heights from the falls: $r=10-10=0$, $m=2\\,\\mathrm{V}$, $q=6\\,\\mathrm{V}$ (a $6\\,\\mathrm{V}$ step above $r$ ✓). Now the current source's step shows: $2\\,\\mathrm{A}$ falls $8\\,\\mathrm{V}$ through it, so it **absorbs** $16\\,\\mathrm{W}$.", ['r', 'm', 'q']),
       ("The $1\\,\\Omega$ absorbs $(6)(6)=36\\,\\mathrm{W}$. Check: climbs $70+36=106\\,\\mathrm{W}$; falls $16+50+2+2+36=106\\,\\mathrm{W}$.", []),
   ], notes=["Node $r$ happens to sit at $0\\,\\mathrm{V}$, level with ground, but it is not connected to ground."])], spoiler=False),
   [S('The $2\\,\\mathrm{A}$ source is shared by meshes $a$ and $b$.', 'I_a-I_b=2'),
    S('KVL around the supermesh (skip the source branch).', '-10+2I_b+2(I_b-I_c)+2(I_a-I_c)=0'),
    S('KVL around mesh $c$.', '-6+I_c+2(I_c-I_a)+2(I_c-I_b)=0'),
    S('Solve the three equations.', 'I_a=7\\,\\mathrm{A},\\quad I_b=5\\,\\mathrm{A},\\quad I_c=6\\,\\mathrm{A}'),
    S('The $1\\,\\Omega$ is only in mesh $c$.', 'p_{1\\Omega}=I_c^2(1)=36\\,\\mathrm{W}')],
   '$I_a=7\\,\\mathrm{A}$, $I_b=5\\,\\mathrm{A}$, $I_c=6\\,\\mathrm{A}$; $p_{1\\Omega}=36\\,\\mathrm{W}$', ap(9))
CO('warning', "**Mesh traps.** (1) Walking $-\\to+$ through a source is a climb; $+\\to-$ is a fall. (2) A shared resistor carries a **difference** of mesh currents, never one alone. (3) Never write $RI$ for a current source's voltage: its step is unknown, which is exactly why the supermesh skips it.")
PR('ap410', 'Try it 6 · A current source on the edge (Assessment AP 4.10)', 'intermediate',
   'Use the mesh-current method to find the power dissipated in the $2\\,\\Omega$ resistor.',
   fence('ap410', [view('ap410', names={'s': 'source +', 'm': 'top middle', 'q': 'bottom middle', 'r': 'top right', 'p': 'bottom right', '0': 'ground'},
                        cols=[('V1', 0), ('R1', 1), ('R3', 1), ('R2', 1), ('R4', 2), ('R5', 2), ('R6', 3), ('I1', 4)], steps=[
       ("Ground the bottom-left node (the $30\\,\\mathrm{V}$ source's $-$); its $+$ end is at $30\\,\\mathrm{V}$.", []),
       ("The $16\\,\\mathrm{A}$ source is on the edge of mesh 3 only, so it fixes that mesh: clockwise $I_3$ runs down that branch, against the arrow: $I_3=-16\\,\\mathrm{A}$.", []),
       ("Two loop walks left: $11I_1-2I_2=30$ and $-2I_1+19I_2=-80$. So $I_1=2$, $I_2=-4\\,\\mathrm{A}$, and the $2\\,\\Omega$ carries $I_1-I_2=6\\,\\mathrm{A}$ down: $72\\,\\mathrm{W}$.", ['eR3']),
       ("Other branches: $2\\,\\mathrm{A}$ around the left loop, $4\\,\\mathrm{A}$ right-to-left through the $8$ and $4\\,\\Omega$, $I_2-I_3=12\\,\\mathrm{A}$ down the $5\\,\\Omega$.", ['eR1', 'eR2', 'eR4', 'eR5', 'eR6', 'eV1', 'eI1']),
       ("Heights from the falls: $24$ and $12\\,\\mathrm{V}$ in the middle, $56\\,\\mathrm{V}$ top right, $-4\\,\\mathrm{V}$ bottom right. The current source lifts $16\\,\\mathrm{A}$ through $60\\,\\mathrm{V}$: $960\\,\\mathrm{W}$.", ['m', 'q', 'r', 'p']),
   ])]),
   [S('The perimeter source fixes mesh 3: clockwise $I_3$ opposes its upward arrow.', 'I_3=-16\\,\\mathrm{A}'),
    S('KVL in mesh 1.', '-30+3I_1+2(I_1-I_2)+6I_1=0\\;\\Rightarrow\\;11I_1-2I_2=30'),
    S('KVL in mesh 2.', '8I_2+5(I_2-I_3)+4I_2+2(I_2-I_1)=0\\;\\Rightarrow\\;-2I_1+19I_2=-80'),
    S('Solve.', 'I_1=2\\,\\mathrm{A},\\qquad I_2=-4\\,\\mathrm{A}'),
    S('The $2\\,\\Omega$ carries $I_1-I_2$ downward.', 'p_{2\\Omega}=(6)^2(2)=72\\,\\mathrm{W}')],
   '$p_{2\\Omega}=72\\,\\mathrm{W}$', ap(7, 8))
PR('p437', 'Try it 7 · Flip one source (Textbook P4.37)', 'intermediate',
   '**(a)** Use the mesh-current method to find $i_a$, $i_b$ and $i_c$. **(b)** Repeat with the polarity of the $64\\,\\mathrm{V}$ source reversed.',
   fence('p437', [
       view('p437', title='As drawn', names={'s': 'source +', 'm': 'top middle', 'q': 'bottom middle', 'r': 'top right', 'p': 'bottom right', '0': 'ground'},
            cols=[('V1', 0), ('R1', 1), ('R3', 2), ('R5', 3), ('R2', 4), ('R4', 5), ('V2', 6)], steps=[
           ("Ground the bottom-left node; the $40\\,\\mathrm{V}$ source's $+$ end is at $40\\,\\mathrm{V}$.", []),
           ("Clockwise $I_L$, $I_R$. Loop walks: $50I_L-45I_R=40$ and $-45I_L+50.5I_R=64$ (clockwise through the $64\\,\\mathrm{V}$ source goes $-\\to+$: a climb).", []),
           ("Solve: $I_L=9.8$, $I_R=10\\,\\mathrm{A}$. So $i_a=9.8\\,\\mathrm{A}$, $i_b=I_L-I_R=-0.2\\,\\mathrm{A}$, $i_c=-I_R=-10\\,\\mathrm{A}$.", ['eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eV1', 'eV2']),
           ("Walk down the falls: top middle $40-29.4=10.6\\,\\mathrm{V}$, bottom middle $19.6\\,\\mathrm{V}$. The bottom one is **higher**, so $0.2\\,\\mathrm{A}$ falls upward through the $45\\,\\Omega$: that is why $i_b$ is negative. The $64\\,\\mathrm{V}$ source spans $34.6$ down to $-29.4\\,\\mathrm{V}$.", ['m', 'q', 'p', 'r']),
       ]),
       view('p437', title='64 V reversed', net=C['p437b']['net'],
            names={'s': 'source +', 'm': 'top middle', 'q': 'bottom middle', 'r': 'top right', 'p': 'bottom right', '0': 'ground'},
            cols=[('V1', 0), ('R1', 1), ('R3', 2), ('R5', 3), ('R2', 4), ('R4', 5), ('V2', 6)], steps=[
           ("Same ground. Only the right walk changes sign: $-45I_L+50.5I_R=-64$. So $I_L=-1.72$, $I_R=-2.8\\,\\mathrm{A}$.", []),
           ("$i_a=-1.72$, $i_b=1.08$, $i_c=2.8\\,\\mathrm{A}$. Every current changed: now $1.72\\,\\mathrm{A}$ falls **into** the $40\\,\\mathrm{V}$ source (it absorbs), and the $64\\,\\mathrm{V}$ source drives everything.", ['eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eV1', 'eV2', 'm', 'q', 'p', 'r']),
       ]),
   ]),
   [S('Clockwise mesh currents $I_L$, $I_R$. From the arrows: $i_a=I_L$, $i_b=I_L-I_R$, $i_c=-I_R$ (it points left).'),
    S('Left mesh.', '-40+(3+2)I_L+45(I_L-I_R)=0\\;\\Rightarrow\\;50I_L-45I_R=40'),
    S('**(a)** Right mesh: clockwise through the $64\\,\\mathrm{V}$ source is a climb.', '45(I_R-I_L)+5.5I_R-64=0\\;\\Rightarrow\\;-45I_L+50.5I_R=64'),
    S('Solve.', 'I_R=10\\,\\mathrm{A},\\quad I_L=9.8\\,\\mathrm{A}'),
    S('**(b)** Only the source sign flips.', '-45I_L+50.5I_R=-64\\;\\Rightarrow\\;I_R=-2.8\\,\\mathrm{A},\\quad I_L=-1.72\\,\\mathrm{A}')],
   '**(a)** $i_a=9.8\\,\\mathrm{A}$, $i_b=-0.2\\,\\mathrm{A}$, $i_c=-10\\,\\mathrm{A}$. **(b)** $i_a=-1.72\\,\\mathrm{A}$, $i_b=1.08\\,\\mathrm{A}$, $i_c=2.8\\,\\mathrm{A}$.', tb('4.37'))

# ---------------------------------------------------------------- Practice
H(1, 'Practice problems')
P('Exam-style, each mixing topics. Give each a real try (10–15 minutes) before opening the solution. Then open the height view and check your picture.')
PR('p430', 'Textbook P4.30 · Move the ground', 'intermediate',
   '**(a)** Use the node-voltage method with node $a$ as the reference to find $v_o$ and the power delivered by the $0.5\\,\\mathrm{A}$ source. **(b)** Repeat with node $b$ as the reference. **(c)** Which reference is better, and why?',
   fence('p430', [
       view('p430', title='Reference a', names={'b': '$b$', 'c': '$c$', 'd': '$d$', '0': '$a$'},
            cols=[('I1', 0), ('V1', 1), ('R1', 1), ('R2', 2), ('R3', 3), ('R4', 3)], refs={'R2': ('c', '$v_o$')}, steps=[
           ("Ground $a$ (the bottom wire). The $12\\,\\mathrm{V}$ source joins $b$ and $c$, both unknown: a rigid rod, $c=b+12$.", []),
           ("KCL around the rod: the $0.5\\,\\mathrm{A}$ in leaves down the $40\\,\\Omega$, the $100\\,\\Omega$ and the $150+50\\,\\Omega$ path: $0.5=\\dfrac{b}{40}+\\dfrac{b+12}{100}+\\dfrac{b+12}{200}$, so $b=8$, $c=20\\,\\mathrm{V}=v_o$.", ['b', 'c', 'eV1']),
           ("Currents: $0.2\\,\\mathrm{A}$ down the $40\\,\\Omega$, $0.2\\,\\mathrm{A}$ down the $100\\,\\Omega$, $0.1\\,\\mathrm{A}$ through the $150$ and $50\\,\\Omega$ ($d=5\\,\\mathrm{V}$). So $0.3\\,\\mathrm{A}$ climbs the rod.", ['eR1', 'eR2', 'eR3', 'eR4', 'd', 'eI1']),
           ("The current source lifts $0.5\\,\\mathrm{A}$ through $8\\,\\mathrm{V}$: it delivers $4\\,\\mathrm{W}$.", []),
       ]),
       view('p430', title='Reference b', gnd='b', names={'b': '$b$', 'c': '$c$', 'd': '$d$', '0': '$a$'},
            cols=[('I1', 0), ('V1', 1), ('R1', 1), ('R2', 2), ('R3', 3), ('R4', 3)], refs={'R2': ('c', '$v_o$')}, steps=[
           ("Ground $b$ instead. Now the $12\\,\\mathrm{V}$ source runs from ground to $c$: $c=12\\,\\mathrm{V}$ is **given**, and only $a$ is unknown.", ['c', 'eV1']),
           ("KCL at $a$: $\\dfrac{a}{40}+\\dfrac{a-12}{100}+\\dfrac{a-12}{200}+0.5=0$, so $a=-8\\,\\mathrm{V}$. Every height dropped by the same $8\\,\\mathrm{V}$: $v_o=12-(-8)=20\\,\\mathrm{V}$.", ['z0', 'd']),
           ("Same falls, same currents, same $4\\,\\mathrm{W}$: moving ground only relabels the levels.", ['eR1', 'eR2', 'eR3', 'eR4', 'eI1']),
       ], notes=["Moving ground shifts every height by the same amount; no voltage difference, current or power changes."]),
   ]),
   [S('**(a)** Reference $a$: $b$ and $c$ form a supernode with $v_c=v_b+12$. KCL around it (the $0.5\\,\\mathrm{A}$ comes in).',
      '\\frac{v_b}{40}+\\frac{v_b+12}{100}+\\frac{v_b+12}{200}=0.5'),
    S('Multiply by 200 and solve.', '8v_b+36=100\\;\\Rightarrow\\;v_b=8\\,\\mathrm{V},\\quad v_o=v_c=20\\,\\mathrm{V}'),
    S('The source lifts $0.5\\,\\mathrm{A}$ from $a$ to $b$.', 'p=(8)(0.5)=4\\,\\mathrm{W}\\text{ delivered}'),
    S('**(b)** Reference $b$: the source fixes $v_c=12\\,\\mathrm{V}$. One KCL, at $a$ (the $0.5\\,\\mathrm{A}$ leaves $a$).',
      '\\frac{v_a}{40}+\\frac{v_a-12}{100}+\\frac{v_a-12}{200}+0.5=0\\;\\Rightarrow\\;v_a=-8\\,\\mathrm{V}'),
    S('Same answers.', 'v_o=v_c-v_a=20\\,\\mathrm{V},\\qquad p=(0-(-8))(0.5)=4\\,\\mathrm{W}'),
    S('**(c)** Reference $b$ is better: the voltage source then fixes a node directly, so one plain KCL replaces the supernode.')],
   '**(a)** $v_o=20\\,\\mathrm{V}$; the source delivers $4\\,\\mathrm{W}$. **(b)** Same: $v_o=20\\,\\mathrm{V}$, $4\\,\\mathrm{W}$ (with $v_a=-8\\,\\mathrm{V}$). **(c)** $b$: the $12\\,\\mathrm{V}$ source then fixes $v_c$, leaving one equation.',
   tb('4.30'))
PR('p424', 'Textbook P4.24 · Heights below ground', 'intermediate',
   '**(a)** Use the node-voltage method to find $i_1$, $i_2$ and $i_3$. **(b)** Check by showing the power dissipated equals the power developed.',
   fence('p424', [view('p424', names={'s': 'source +', 'a': '$a$', 'b': '$b$', '0': 'ground'}, unit='mA',
                       cols=[('V1', 0), ('R1', 1), ('R2', 2), ('I1', 3), ('R4', 4), ('R3', 5), ('V2', 6)], steps=[
       ("Ground the bottom wire. Two fixed heights: the $20\\,\\mathrm{V}$ source's $+$ end, and node $b$, the **$-$** end of the $10\\,\\mathrm{V}$ source whose $+$ is grounded: $b=-10\\,\\mathrm{V}$.", ['b']),
       ("One unknown, $a$. KCL at $a$ (mA and kΩ): $\\dfrac{20-a}{25}=\\dfrac{a}{0.25}+11+\\dfrac{a+10}{0.5}$, so $a=-5\\,\\mathrm{V}$: below ground.", ['a']),
       ("Currents = fall ÷ R: $i_1=\\dfrac{25}{25}=1\\,\\mathrm{mA}$. Ground is above $a$, so $20\\,\\mathrm{mA}$ falls **up** the $250\\,\\Omega$ into $a$: $i_2=-20\\,\\mathrm{mA}$. $10\\,\\mathrm{mA}$ falls from $a$ to $b$ through the $500\\,\\Omega$, and $10\\,\\mathrm{mA}$ from ground down to $b$ through the $1\\,\\mathrm{k\\Omega}$.", ['eR1', 'eR2', 'eR3', 'eR4', 'eI1', 'eV1']),
       ("KCL at $b$: $11+10+10=31\\,\\mathrm{mA}$ arrive, and all of it climbs back to ground through the $10\\,\\mathrm{V}$ source: $i_3=31\\,\\mathrm{mA}$.", ['eV2']),
       ("Power: climbs $(20)(1)+(10)(31)=330\\,\\mathrm{mW}$. Falls $25+100+50+100=275\\,\\mathrm{mW}$ in the resistors, plus $55\\,\\mathrm{mW}$ in the $11\\,\\mathrm{mA}$ source (its current falls $5\\,\\mathrm{V}$).", []),
   ])]),
   [S('Ground the bottom wire. The $10\\,\\mathrm{V}$ source has its $+$ at ground, so $v_b=-10\\,\\mathrm{V}$. KCL at $a$ (currents out, in mA and kΩ).',
      '\\frac{v_a-20}{25}+\\frac{v_a}{0.25}+11+\\frac{v_a+10}{0.5}=0'),
    S('Multiply by 25.', 'v_a-20+100v_a+275+50v_a+500=0\\;\\Rightarrow\\;v_a=-5\\,\\mathrm{V}'),
    S('Branch currents in their arrow directions.', 'i_1=\\frac{20-(-5)}{25}=1\\,\\mathrm{mA},\\qquad i_2=\\frac{-5}{0.25}=-20\\,\\mathrm{mA}'),
    S('KCL at $b$: in from the source ($11$), the $500\\,\\Omega$ ($10$) and the $1\\,\\mathrm{k\\Omega}$ ($10$); out down through the $10\\,\\mathrm{V}$ source.', 'i_3=11+\\frac{-5+10}{0.5}+\\frac{0+10}{1}=31\\,\\mathrm{mA}'),
    S('**(b)** Developed: both voltage sources. Dissipated: the resistors plus the $11\\,\\mathrm{mA}$ source (which absorbs).', '20(1)+10(31)=330\\,\\mathrm{mW}=25+100+50+100+55')],
   '**(a)** $i_1=1\\,\\mathrm{mA}$, $i_2=-20\\,\\mathrm{mA}$, $i_3=31\\,\\mathrm{mA}$. **(b)** $330\\,\\mathrm{mW}$ developed $=330\\,\\mathrm{mW}$ absorbed.', tb('4.24'))
PR('p418', 'Textbook P4.18 · A controlled rod that delivers', 'intermediate',
   'Use the node-voltage method to find the power delivered by the dependent voltage source.',
   fence('p418', [view('p418', names={'s': 'source +', 'a': '$a$', 'c': '$c$', 'd': '$d$', '0': 'ground'},
                       cols=[('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2), ('E1', 3), ('R4', 4)],
                       elabel={'E1': '$75i_\\sigma$'}, steps=[
       ("Ground the bottom-left wire; the $80\\,\\mathrm{V}$ source fixes its $+$ end. The diamond is a rod between $c$ and $d$: $d=c+75i_\\sigma$, with $i_\\sigma=\\dfrac{a}{50}$.", []),
       ("KCL at $a$: $\\dfrac{a-80}{5}+\\dfrac{a}{50}+\\dfrac{a-c}{10}=0$. KCL around the rod: what arrives through the $10\\,\\Omega$ leaves through the $15\\,\\Omega$, $\\dfrac{a-c}{10}=\\dfrac{d}{15}$.", []),
       ("With $d=c+1.5a$ the rod equation gives $c=0$, then $a=50\\,\\mathrm{V}$ and $d=75\\,\\mathrm{V}$. So $i_\\sigma=1\\,\\mathrm{A}$ and the rod is $75\\,\\mathrm{V}$ long.", ['a', 'c', 'd', 'eE1']),
       ("Currents: $6\\,\\mathrm{A}$ through the $5\\,\\Omega$, $1\\,\\mathrm{A}$ down the $50\\,\\Omega$, $5\\,\\mathrm{A}$ from $a$ to $c$, up the rod, and down the $15\\,\\Omega$ back to ground.", ['eR1', 'eR2', 'eR3', 'eR4', 'eV1']),
       ("The diamond lifts $5\\,\\mathrm{A}$ through $75\\,\\mathrm{V}$: it **delivers** $375\\,\\mathrm{W}$. Check: climbs $480+375=855\\,\\mathrm{W}$; falls $180+50+250+375=855\\,\\mathrm{W}$.", []),
   ])]),
   [S('Ground the bottom-left wire. Name $a$, the diamond\'s $-$ end $c$ and $+$ end $d$. Control and rod.', 'i_\\sigma=\\frac{v_a}{50},\\qquad v_d-v_c=75i_\\sigma=1.5v_a'),
    S('KCL at $a$, times 50.', '10(v_a-80)+v_a+5(v_a-v_c)=0\\;\\Rightarrow\\;16v_a-5v_c=800'),
    S('KCL around the rod: in through the $10\\,\\Omega$, out through the $15\\,\\Omega$.', '\\frac{v_a-v_c}{10}=\\frac{v_d}{15}=\\frac{v_c+1.5v_a}{15}\\;\\Rightarrow\\;v_c=0'),
    S('So', 'v_a=50\\,\\mathrm{V},\\quad i_\\sigma=1\\,\\mathrm{A},\\quad v_d=75\\,\\mathrm{V},\\quad i=\\frac{50-0}{10}=5\\,\\mathrm{A}'),
    S('The $5\\,\\mathrm{A}$ enters the diamond\'s $-$ end and leaves its $+$ end: it climbs.', 'p=(75)(5)=375\\,\\mathrm{W}\\text{ delivered}')],
   'The dependent source delivers $375\\,\\mathrm{W}$ ($i_\\sigma=1\\,\\mathrm{A}$, $75\\,\\mathrm{V}$ step, $5\\,\\mathrm{A}$).', tb('4.18'))
PR('p449', 'Textbook P4.49 · A supermesh where a source absorbs', 'intermediate',
   'Use the mesh-current method to find the total power dissipated in the circuit.',
   fence('p449', [view('p449', names={'s': 'source +', 'm': '$m$', 'r': 'top right', 'p': 'bottom right', 'q': '$q$', '0': 'ground'},
                       cols=[('V1', 0), ('R1', 1), ('R2', 2), ('V2', 3), ('R4', 4), ('I1', 5), ('R3', 6)], steps=[
       ("Ground the bottom-left node; the $18\\,\\mathrm{V}$ source's $+$ end is at $18\\,\\mathrm{V}$.", []),
       ("The $3\\,\\mathrm{A}$ source is shared by both meshes: skip it. Supermesh walk around the outside: $-18+3I_a+9I_b-15+6I_b+2I_a=0$. The source gives $I_b-I_a=3$.", []),
       ("So $5I_a+15I_b=33$ with $I_b=I_a+3$: $I_a=-0.6$, $I_b=2.4\\,\\mathrm{A}$. The left loop runs backwards: $0.6\\,\\mathrm{A}$ goes **down** through the $18\\,\\mathrm{V}$ source.", ['eR1', 'eR2', 'eR3', 'eR4', 'eV1', 'eV2', 'eI1']),
       ("Heights from the falls: $m=18+1.8=19.8$, $q=-1.2$, top right $19.8-21.6=-1.8$, bottom right $-1.8+15=13.2\\,\\mathrm{V}$. The current source's step shows: $21\\,\\mathrm{V}$.", ['m', 'q', 'r', 'p']),
       ("Power: climbs $3\\times21=63$ and $2.4\\times15=36\\,\\mathrm{W}$. Falls: the $18\\,\\mathrm{V}$ source absorbs $10.8\\,\\mathrm{W}$; the resistors dissipate $1.08+51.84+0.72+34.56=88.2\\,\\mathrm{W}$.", []),
   ])]),
   [S('Clockwise $I_a$ (left) and $I_b$ (right). The shared $3\\,\\mathrm{A}$ source points up; $I_b$ goes up through it and $I_a$ down.', 'I_b-I_a=3'),
    S('Supermesh KVL around the outside (the $15\\,\\mathrm{V}$ source is walked $-\\to+$: a climb).', '-18+3I_a+9I_b-15+6I_b+2I_a=0\\;\\Rightarrow\\;5I_a+15I_b=33'),
    S('Solve.', 'I_a=-0.6\\,\\mathrm{A},\\qquad I_b=2.4\\,\\mathrm{A}'),
    S('Resistor powers.', '(0.6)^2(3+2)+(2.4)^2(9+6)=1.8+86.4=88.2\\,\\mathrm{W}'),
    S('Check: developed $63+36=99\\,\\mathrm{W}$; absorbed $88.2\\,\\mathrm{W}$ plus $10.8\\,\\mathrm{W}$ in the $18\\,\\mathrm{V}$ source.')],
   '$88.2\\,\\mathrm{W}$ dissipated in the resistors (and the $18\\,\\mathrm{V}$ source absorbs another $10.8\\,\\mathrm{W}$).', tb('4.49'))
PR('tut', 'Week 4 tutorial Problem 4 · A bridge by node voltages', 'advanced',
   'Find $i_o$, $i_1$, $i_2$ and the power delivered by the current source. (The tutorial uses a Y–Δ swap; solve it with node voltages.)',
   fence('tut_bridge', [view('tut_bridge', names={'a': '$a$', 'b': '$b$', 'c': '$c$', '0': 'ground'},
                             cols=[('I1', 0), ('R1', 1), ('R2', 2), ('R3', 2), ('R4', 3), ('R5', 3), ('R6', 4)], rails=('I1',), steps=[
       ("Ground the bottom wire. The $1\\,\\mathrm{A}$ source fixes a current, not a height: three unknown heights $a$, $b$, $c$.", []),
       ("KCL at each: $\\dfrac{a}{240}+\\dfrac{a-b}{20}+\\dfrac{a-c}{320}=1$, $\\dfrac{b}{100}+\\dfrac{b-a}{20}+\\dfrac{b-c}{50}=0$, $\\dfrac{c}{600}+\\dfrac{c-b}{50}+\\dfrac{c-a}{320}=0$.", []),
       ("Averaging shortcut ($b$ and $c$ get no pushed-in current): $b=\\dfrac58a+\\dfrac14c$, then $c=\\dfrac{15}{19}a$. The first equation gives $a=72.96$, $b=60$, $c=57.6\\,\\mathrm{V}$.", ['a', 'b', 'c']),
       ("Currents = fall ÷ R: $i_2=\\dfrac{60}{100}=0.6\\,\\mathrm{A}$, $i_o=\\dfrac{57.6}{600}=0.096\\,\\mathrm{A}$, $i_1=\\dfrac{72.96-57.6}{320}=0.048\\,\\mathrm{A}$.", ['eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eR6', 'eI1']),
       ("Power: the source lifts $1\\,\\mathrm{A}$ to $72.96\\,\\mathrm{V}$: $72.96\\,\\mathrm{W}$ delivered.", []),
   ])]),
   [S('Ground the bottom wire; KCL at $a$, $b$, $c$.', '\\begin{aligned}&\\frac{v_a}{240}+\\frac{v_a-v_b}{20}+\\frac{v_a-v_c}{320}=1\\\\&\\frac{v_b}{100}+\\frac{v_b-v_a}{20}+\\frac{v_b-v_c}{50}=0\\\\&\\frac{v_c}{600}+\\frac{v_c-v_b}{50}+\\frac{v_c-v_a}{320}=0\\end{aligned}'),
    S('The second gives $v_b$ as a weighted average; substitute into the third.', 'v_b=\\tfrac58v_a+\\tfrac14v_c,\\qquad v_c=\\tfrac{15}{19}v_a,\\qquad v_b=\\tfrac{125}{152}v_a'),
    S('Substitute into the first.', 'v_a=72.96\\,\\mathrm{V},\\quad v_b=60\\,\\mathrm{V},\\quad v_c=57.6\\,\\mathrm{V}'),
    S('Currents and source power.', 'i_o=\\frac{57.6}{600}=0.096\\,\\mathrm{A},\\quad i_1=0.048\\,\\mathrm{A},\\quad i_2=0.6\\,\\mathrm{A},\\quad p=72.96\\,\\mathrm{W}')],
   '$i_o=0.096\\,\\mathrm{A}$, $i_1=0.048\\,\\mathrm{A}$, $i_2=0.6\\,\\mathrm{A}$; the source delivers $72.96\\,\\mathrm{W}$.', TUT_CITES)
PR('lec22', 'Lecture 3 p.22 · A shared current source', 'advanced',
   'Use the mesh-current method to find the clockwise mesh currents $i_a$ (lower left), $i_b$ (top), $i_c$ (lower right) and the voltage $v$ across the current source.',
   fence('lec22', [view('lec22', names={'l': 'source +', 'm': '$m$', 'r': '$r$', 'p': '$p$', 'q': '$q$', '0': 'ground'},
                        cols=[('V1', 0), ('R2', 1), ('R3', 1), ('V2', 1), ('R5', 1), ('R4', 1), ('I1', 2), ('R1', 3)],
                        refs={'I1': ('m', '$v$')}, steps=[
       ("Ground the bottom-left node; the $100\\,\\mathrm{V}$ source's $+$ end is at $100\\,\\mathrm{V}$.", []),
       ("The $5\\,\\mathrm{A}$ source is shared by meshes $a$ and $c$: $i_c-i_a=5$. The supermesh walk skips it: $-100+3(i_a-i_b)+2(i_c-i_b)+50+4i_c+6i_a=0$. Top mesh: $10i_b+2(i_b-i_c)+3(i_b-i_a)=0$.", []),
       ("Solve: $i_a=1.75$, $i_b=1.25$, $i_c=6.75\\,\\mathrm{A}$. Branch currents: $1.25$ ($10\\,\\Omega$), $0.5$ ($3\\,\\Omega$), $5.5$ ($2\\,\\Omega$), $1.75$ ($6\\,\\Omega$), $6.75\\,\\mathrm{A}$ ($4\\,\\Omega$).", ['eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eV1', 'eV2', 'eI1']),
       ("Heights: $m=100-(0.5)(3)=98.5\\,\\mathrm{V}$, $q=(1.75)(6)=10.5\\,\\mathrm{V}$. The current source spans them: $v=98.5-10.5=88\\,\\mathrm{V}$.", ['m', 'q']),
       ("Also $r=87.5$ and $p=37.5\\,\\mathrm{V}$: $6.75\\,\\mathrm{A}$ falls through the $50\\,\\mathrm{V}$ source, which **absorbs** $337.5\\,\\mathrm{W}$. The current source lifts $5\\,\\mathrm{A}$ through $88\\,\\mathrm{V}$: $440\\,\\mathrm{W}$.", ['r', 'p']),
   ])]),
   [S('The shared source points up; $i_c$ goes up through it, $i_a$ down.', 'i_c-i_a=5'),
    S('Top mesh.', '10i_b+2(i_b-i_c)+3(i_b-i_a)=0\\;\\Rightarrow\\;15i_b-3i_a-2i_c=0'),
    S('Supermesh around the bottom two meshes, skipping the source.', '\\begin{aligned}&-100+3(i_a-i_b)+2(i_c-i_b)+50+4i_c+6i_a=0\\\\&\\Rightarrow\\;9i_a-5i_b+6i_c=50\\end{aligned}'),
    S('Substitute $i_c=i_a+5$: $i_a=3i_b-2$ from the top mesh, then $15i_a-5i_b=20$.', 'i_b=1.25\\,\\mathrm{A},\\quad i_a=1.75\\,\\mathrm{A},\\quad i_c=6.75\\,\\mathrm{A}'),
    S('Heights at the source\'s ends.', 'v=\\big(100-3(0.5)\\big)-6(1.75)=98.5-10.5=88\\,\\mathrm{V}')],
   '$i_a=1.75\\,\\mathrm{A}$, $i_b=1.25\\,\\mathrm{A}$, $i_c=6.75\\,\\mathrm{A}$; $v=88\\,\\mathrm{V}$', lec(22))
PR('p441', 'Textbook P4.41 · A dependent source in three meshes', 'advanced',
   'Use the mesh-current method to find the power developed in the dependent voltage source. Mesh 1 is lower left, mesh 2 the top, mesh 3 lower right (all clockwise).',
   fence('p441', [view('p441', names={'s': 'source +', 'm': '$m$', 'n': '$10\\,\\mathrm{V}$ +', 'r': 'right node', 'x': 'diamond +', '0': 'ground'},
                       cols=[('V1', 0), ('R1', 1), ('R3', 1), ('V2', 1), ('R2', 2), ('R4', 2), ('R5', 3), ('E1', 4)],
                       elabel={'E1': '$-3v_\\phi$'}, refs={'R2': ('m', '$v_\\phi$')}, steps=[
       ("Ground the bottom wire; the $25\\,\\mathrm{V}$ and $10\\,\\mathrm{V}$ sources fix their $+$ ends.", []),
       ("Control: $v_\\phi=3(i_3-i_2)$. Loop walks: $-25+2(i_1-i_2)+5(i_1-i_3)+10=0$; $3v_\\phi+14i_2+3(i_2-i_3)+2(i_2-i_1)=0$; $i_3-10+5(i_3-i_1)+3(i_3-i_2)=0$.", []),
       ("Solve: $i_1=4$, $i_2=-1$, $i_3=3\\,\\mathrm{A}$, $v_\\phi=12\\,\\mathrm{V}$. The diamond's step is $-36\\,\\mathrm{V}$: its $+$ end sits $36\\,\\mathrm{V}$ **below** its $-$ end.", ['eE1']),
       ("Branch currents → heights: $5\\,\\mathrm{A}$ through the $2\\,\\Omega$ ($m=15$), $1\\,\\mathrm{A}$ down the $5\\,\\Omega$, $4\\,\\mathrm{A}$ through the $3\\,\\Omega$ (right node $3\\,\\mathrm{V}$), $3\\,\\mathrm{A}$ down the $1\\,\\Omega$, $1\\,\\mathrm{A}$ through the $14\\,\\Omega$ down to $-11\\,\\mathrm{V}$.", ['m', 'r', 'x', 'eR1', 'eR2', 'eR3', 'eR4', 'eR5', 'eV1', 'eV2']),
       ("That $1\\,\\mathrm{A}$ climbs $36\\,\\mathrm{V}$ through the diamond back to the $25\\,\\mathrm{V}$ node: it **delivers** $36\\,\\mathrm{W}$. Check: climbs $100+36$; falls $50+48+5+10+9+14=136\\,\\mathrm{W}$.", []),
   ])]),
   [S('Control first: $v_\\phi$ is across the $3\\,\\Omega$ shared by meshes 2 and 3.', 'v_\\phi=3(i_3-i_2)'),
    S('Loop walks.', '\\begin{aligned}&-25+2(i_1-i_2)+5(i_1-i_3)+10=0\\\\&3v_\\phi+14i_2+3(i_2-i_3)+2(i_2-i_1)=0\\\\&i_3-10+5(i_3-i_1)+3(i_3-i_2)=0\\end{aligned}'),
    S('Solve with the control.', 'i_1=4\\,\\mathrm{A},\\quad i_2=-1\\,\\mathrm{A},\\quad i_3=3\\,\\mathrm{A},\\quad v_\\phi=12\\,\\mathrm{V}'),
    S('The diamond carries $i_2$; absorbed power with current entering $-$ means delivering.', 'p=-(-3v_\\phi)\\,i_2=3(12)(-1)=-36\\,\\mathrm{W}')],
   'The dependent source delivers $36\\,\\mathrm{W}$ (absorbs $-36\\,\\mathrm{W}$).', tb('4.41'))

# ---------------------------------------------------------------- Summary
H(1, 'Summary: Week 3 in one read')
CO('tip', "Same picture as Weeks 1–2: **voltage is height**. Week 3 adds bookkeeping for when several heights depend on each other. Three ideas, one picture each.")
H(2, 'A · Node voltages are heights')
L(['Ground a node; every essential node gets an unknown height; KCL at each.',
   'One unknown node? It sits at the **conductance-weighted average** of its neighbours (plus any current pushed in ÷ total conductance).'])
EX('A1', 'A1 · The averaging rule (like Lecture 3 and AP 4.13)', 'Find the height of $x$.',
   fence('A1', [view('A1', names={'s': 'left +', 'x': '$x$', 'r': 'right +', '0': 'ground'},
                     cols=[('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2), ('V2', 2)], straight_off=True, steps=[
       ("Ground the bottom wire; the sources fix $12$ and $6\\,\\mathrm{V}$.", []),
       ("$x$'s neighbours sit at $12$ (through $2\\,\\Omega$), $0$ and $6\\,\\mathrm{V}$ (through $4\\,\\Omega$ each). Weights $\\tfrac12,\\tfrac14,\\tfrac14$: $x=\\dfrac{6+0+1.5}{1}=7.5\\,\\mathrm{V}$.", ['x']),
       ("Currents = fall ÷ R: $2.25\\,\\mathrm{A}$ in from the left, $1.875\\,\\mathrm{A}$ down, $0.375\\,\\mathrm{A}$ on to the right, where it falls **into** the $6\\,\\mathrm{V}$ source.", ['eR1', 'eR2', 'eR3', 'eV1', 'eV2']),
   ])], spoiler=False, inline=True),
   [S('Weighted average with $G=\\dfrac1R$.', 'x=\\frac{12(\\frac12)+0(\\frac14)+6(\\frac14)}{\\frac12+\\frac14+\\frac14}=7.5\\,\\mathrm{V}')],
   '$x=7.5\\,\\mathrm{V}$: closest to $12\\,\\mathrm{V}$, because that neighbour has the strongest pull (smallest $R$).')
H(2, 'B · Fixed heights and rigid rods')
L(['Voltage source to ground: that height is **given**.',
   'Voltage source between two unknown nodes: a **rigid rod** ($v_p-v_q=V_s$). KCL around the whole rod.',
   'Dependent source: write the control in heights first; then it is a rod (voltage) or a pump (current).'])
EX('B1', 'B1 · KCL around a rod (like Lecture 3 and P4.30)', 'Find $p$ and $q$.',
   fence('B1', [view('B1', names={'p': '$p$', 'q': '$q$', '0': 'ground'},
                     cols=[('I1', 0), ('R1', 1), ('V1', 2), ('R2', 3)], straight_off=True, steps=[
       ("Ground the bottom wire. The $6\\,\\mathrm{V}$ source joins two unknown nodes: a rod, $q=p+6$.", []),
       ("KCL around the whole rod: $3=\\dfrac{p}{2}+\\dfrac{p+6}{4}$, so $p=2\\,\\mathrm{V}$, $q=8\\,\\mathrm{V}$.", ['p', 'q']),
       ("Currents: $1\\,\\mathrm{A}$ down the $2\\,\\Omega$, $2\\,\\mathrm{A}$ down the $4\\,\\Omega$; the other $2\\,\\mathrm{A}$ climbs the rod.", ['eR1', 'eR2', 'eV1', 'eI1']),
   ])], spoiler=False, inline=True),
   [S('KCL around the rod (its own current stays inside).', '3=\\frac{p}{2}+\\frac{p+6}{4}\\;\\Rightarrow\\;p=2\\,\\mathrm{V},\\quad q=8\\,\\mathrm{V}')],
   '$p=2\\,\\mathrm{V}$, $q=8\\,\\mathrm{V}$')
H(2, 'C · Mesh currents are loop walks')
L(['Clockwise current per window; KVL = walk the window, climbs = falls.',
   'A shared resistor carries $I_k-I_\\ell$. A shared current source: skip it (supermesh) and add $I_a-I_b=I_s$.',
   'Mesh currents have no height. Turn them into branch currents, then walk down the falls to place the heights.'])
EX('C1', 'C1 · Same answer both ways (like Lecture 3)', 'Find the mesh currents and the height of $x$.',
   fence('C1', [view('C1', names={'s': 'left +', 'x': '$x$', 'r': 'right +', '0': 'ground'},
                     cols=[('V1', 0), ('R1', 1), ('R2', 1), ('R3', 2), ('V2', 2)], straight_off=True, steps=[
       ("Ground the bottom wire; the sources fix $12$ and $6\\,\\mathrm{V}$.", []),
       ("Loop walks, clockwise: $12=2I_1+4(I_1-I_2)$ and $0=4(I_2-I_1)+2I_2+6$. So $I_1=2.4$, $I_2=0.6\\,\\mathrm{A}$.", []),
       ("Real currents: $2.4\\,\\mathrm{A}$ in, $I_1-I_2=1.8\\,\\mathrm{A}$ down the $4\\,\\Omega$, $0.6\\,\\mathrm{A}$ out. Height: $x=(1.8)(4)=7.2\\,\\mathrm{V}$, the same as the averaging rule gives.", ['eR1', 'eR2', 'eR3', 'eV1', 'eV2', 'x']),
   ])], spoiler=False, inline=True),
   [S('Two loop walks.', '6I_1-4I_2=12,\\qquad -4I_1+6I_2=-6\\;\\Rightarrow\\;I_1=2.4\\,\\mathrm{A},\\;I_2=0.6\\,\\mathrm{A}'),
    S('Check with the averaging rule.', 'x=\\frac{12(\\frac12)+0(\\frac14)+6(\\frac12)}{\\frac12+\\frac14+\\frac12}=7.2\\,\\mathrm{V}')],
   '$I_1=2.4\\,\\mathrm{A}$, $I_2=0.6\\,\\mathrm{A}$, $x=7.2\\,\\mathrm{V}$')
H(2, 'Which part do I need? (practice problem map)')
T(['Practice problem', 'Use', 'First move'], [
    ['P4.30 · Move the ground', 'B, A', 'Reference $a$: rod $b$–$c$, KCL around it. Reference $b$: the source fixes $c$; one KCL at $a$.'],
    ['P4.24 · Heights below ground', 'B, A', 'The $10\\,\\mathrm{V}$ source fixes $b=-10\\,\\mathrm{V}$; one KCL at $a$.'],
    ['P4.18 · A controlled rod that delivers', 'B', 'Rod $d=c+75i_\\sigma$ with $i_\\sigma=\\dfrac{a}{50}$; KCL at $a$ and around the rod.'],
    ['P4.49 · A supermesh where a source absorbs', 'C', 'Skip the $3\\,\\mathrm{A}$ source: outer walk plus $I_b-I_a=3$.'],
    ['Tutorial bridge', 'A', 'Three KCLs; averaging shortcut for $b$ and $c$.'],
    ['Lecture p.22 · A shared current source', 'C', 'Supermesh; then $v$ = height difference across the source.'],
    ['P4.41 · A dependent source in three meshes', 'C, B', 'Three walks plus the control $v_\\phi=3(i_3-i_2)$.'],
])
CO('warning', "**Traps.** (1) Supernode: the two ends differ by $V_s$; leave the source's current out of KCL. (2) Control first, with its arrow or $+/-$. (3) Shared resistor = difference of mesh currents. (4) A current source's voltage is unknown: never $RI$. (5) A node above every voltage source is fine **only** if a current or dependent source pumps it there.")
H(2, 'Formula sheet')
T(['Result', 'Formula', 'In heights'], [
    ['Resistor current', '$i_{k\\to j}=\\dfrac{v_k-v_j}{R}$', 'fall ÷ R, downhill'],
    ['Node equation', '$\\sum_j\\dfrac{v_k-v_j}{R_{kj}}=I_{\\text{in}}$', 'KCL at an unknown height'],
    ['Averaging rule', '$v_k=\\dfrac{\\sum G_jv_j+I_{\\text{in}}}{\\sum G_j}$', 'weighted average of neighbours'],
    ['Grounded source', '$v_p=V_s$', 'a given height'],
    ['Supernode', '$v_p-v_q=V_s$ + KCL around both', 'a rigid rod'],
    ['Shared mesh resistor', '$i=I_k-I_\\ell$', 'only branch currents are real'],
    ['Supermesh', '$I_a-I_b=I_s$ + one walk around both', 'skip the stretchy step'],
    ['Counts', 'node eqs $=n_e-1$; $M=b-n+1$', 'unknown heights; windows'],
    ['Power', '$p=vi$; climbs deliver, falls absorb', 'current × height change'],
])

# ---------------------------------------------------------------- Extra: several sources
H(1, 'Extra: many sources at once')
L(['**No source is "the main one".** Only ground is special. Every source is just one more element on the picture.',
   '**Each voltage source** fixes a height (one end grounded) or a rigid rod (between two unknown nodes). Two batteries → two fixed heights. The Straight line view uses the tallest as the rail and draws the rest as steps.',
   '**Each current source** fixes a current, never a height. Arrow **into** a node pushes it up; arrow **out of** a node drags it down. No voltage source at all? Then *every* height is unknown and comes from KCL.',
   '**Then the usual recipe:** ground → fixed heights → name the unknown heights → KCL at each → solve → currents = fall ÷ R → power.',
   '**Sanity check:** a node can only rise above every voltage source, or sink below ground, when a current source (or dependent source) puts it there.',
   'This *is* nodal analysis: the node voltages are the heights, and each KCL equation says "what falls in = what falls out". See also AP 4.13 (two batteries + a pump) and P4.13 (two pumps, no battery).'])
EX('multi', 'Two pumps, no battery: every height from KCL',
   'Find $V_1$ and the currents $I_1$–$I_4$. (The diagonal $4\\,\\mathrm{mA}$ source is redrawn straight down from node 2; it still joins node 2 to the bottom wire.)',
   fence('multi', [view('multi', gnd='n1', names={'n1': 'node 1', 'n2': 'node 2', '0': 'bottom wire'}, unit='mA',
                        cols=[('R1', 0), ('I1', 1), ('R2', 2), ('I2', 3), ('R3', 4), ('R4', 5)],
                        refs={'R1': ('n1', '$V_1$')}, steps=[
       ("Ground **node 1**, the lowest point (step 2 shows why it's the lowest). The drawing's ground symbol is on the bottom wire, but you may measure heights from any node: moving ground shifts every height by the same amount, so no voltage, current or answer changes. Picking the lowest node keeps ground at the bottom of the picture.", []),
       ("Read the pumps. Both arrows point **out of** their node into the bottom wire: $6\\,\\mathrm{mA}$ leaves node 1, $4\\,\\mathrm{mA}$ leaves node 2. That charge must come back through the resistors, and resistor current only flows downhill, so the bottom wire must sit **above** both nodes.", ['eI1', 'eI2']),
       ("Find the heights with KCL, using the drawing's voltages (measured from the bottom wire, mA and kΩ): $\\dfrac{V_1}{3}+6+\\dfrac{V_1-V_2}{2}=0$ and $\\dfrac{V_2-V_1}{2}+4+\\dfrac{V_2}{2}+\\dfrac{V_2}{2}=0$, so $V_1=-11\\,\\mathrm{V}$, $V_2=-6.33\\,\\mathrm{V}$. Measured up from node 1: the bottom wire sits at $11\\,\\mathrm{V}$, node 2 at $11-6.33=4.67\\,\\mathrm{V}$.", ['z0', 'n2']),
       ("Currents = fall ÷ R, always downhill. The $3\\,\\mathrm{k\\Omega}$ falls $11\\,\\mathrm{V}$ from the bottom wire to node 1: $3.67\\,\\mathrm{mA}$, **up** the drawing, so $I_1=-3.67\\,\\mathrm{mA}$. $2.33\\,\\mathrm{mA}$ falls from node 2 to node 1: $I_2=-2.33\\,\\mathrm{mA}$. Each right $2\\,\\mathrm{k\\Omega}$ falls $6.33\\,\\mathrm{V}$ from the bottom wire to node 2, against its arrow: $I_3=I_4=-3.17\\,\\mathrm{mA}$.", ['eR1', 'eR2', 'eR3', 'eR4']),
       ("Check KCL. Node 1: in $3.67+2.33=6\\,\\mathrm{mA}$ = the $6\\,\\mathrm{mA}$ out. Node 2: in $3.17+3.17=6.33$ = out $4+2.33$.", []),
       ("Power: each pump lifts its current from a low node back **up** to the bottom wire, so both deliver: $(6)(11)=66\\,\\mathrm{mW}$ and $(4)(6.33)=25.3\\,\\mathrm{mW}$. The four falls absorb $40.3+10.9+20.1+20.1=91.3\\,\\mathrm{mW}$.", []),
   ], notes=["$V_1$ is node 1 minus the bottom wire: $0-11=-11\\,\\mathrm{V}$, the same answer whichever node you ground. Its blue $+$ sits on the lower end, which is what makes it negative."])],
         spoiler=False, inline=False),
   [S('Ground the bottom wire. No voltage source, so both node heights are unknown. KCL at node 1 (currents out, mA and kΩ).', '\\frac{V_1}{3}+6+\\frac{V_1-V_2}{2}=0'),
    S('KCL at node 2.', '\\frac{V_2-V_1}{2}+4+\\frac{V_2}{2}+\\frac{V_2}{2}=0\\;\\Rightarrow\\;V_1=3V_2+8'),
    S('Substitute into node 1.', '\\tfrac56(3V_2+8)-\\tfrac12V_2=-6\\;\\Rightarrow\\;V_2=-\\tfrac{19}{3}\\,\\mathrm{V},\\quad V_1=-11\\,\\mathrm{V}'),
    S('Branch currents in their arrow directions.', '\\begin{aligned}&I_1=\\frac{V_1}{3}=-3.67\\,\\mathrm{mA},\\quad I_2=\\frac{V_1-V_2}{2}=-2.33\\,\\mathrm{mA}\\\\&I_3=I_4=\\frac{V_2}{2}=-3.17\\,\\mathrm{mA}\\end{aligned}'),
    S('Power check: both sources deliver, the resistors absorb.', '(6)(11)+(4)(6.33)=91.3\\,\\mathrm{mW}=40.3+10.9+20.1+20.1')],
   '$V_1=-11\\,\\mathrm{V}$ ($V_2=-6.33\\,\\mathrm{V}$); $I_1=-3.67\\,\\mathrm{mA}$, $I_2=-2.33\\,\\mathrm{mA}$, $I_3=I_4=-3.17\\,\\mathrm{mA}$. Both current sources deliver power.')

EX('multi2', 'Three pumps, two of them absorbing: find $I_0$',
   'Find $I_0$. The right edge runs down into the bottom wire, so the $2\\,\\mathrm{mA}$ source and the horizontal $4\\,\\mathrm{k\\Omega}$ both end on the ground node.',
   fence('multi2', [view('multi2', names={'a': '$a$ (top wire)', 'b': '$b$ (middle wire)', '0': 'ground'}, unit='mA',
                         cols=[('R2', 0), ('R1', 0), ('I1', 1), ('I3', 1), ('I2', 2), ('R3', 3), ('R4', 4)], steps=[
       ("Ground the bottom wire. No voltage source, so **no height is given**: the top wire $a$ and the middle wire $b$ are both unknown.", []),
       ("Read the pumps: $6\\,\\mathrm{mA}$ is pushed up into $b$, $4\\,\\mathrm{mA}$ is moved from $b$ to $a$, and $2\\,\\mathrm{mA}$ is drained from $a$ into ground. Each node gets a net $2\\,\\mathrm{mA}$ pushed in, which can only leave by falling through resistors, so both nodes sit **above** ground.", ['eI1', 'eI2', 'eI3']),
       ("KCL at each node (mA, kΩ, V; out = in). At $a$: $\\dfrac{a}{2}+\\dfrac{a-b}{4}+2=4$. At $b$: $\\dfrac{b-a}{4}+\\dfrac{b}{12}+\\dfrac{b}{4}+4=6$. Solve: $a=\\dfrac{40}{9}\\approx4.44\\,\\mathrm{V}$, $b=\\dfrac{16}{3}\\approx5.33\\,\\mathrm{V}$.", ['a', 'b']),
       ("Currents = fall ÷ R. $I_0=\\dfrac{5.33}{12}=0.444\\,\\mathrm{mA}$ down the $12\\,\\mathrm{k\\Omega}$. Also $1.33\\,\\mathrm{mA}$ down the horizontal $4\\,\\mathrm{k\\Omega}$, $2.22\\,\\mathrm{mA}$ down the $2\\,\\mathrm{k\\Omega}$, and since $b$ is higher than $a$, $0.222\\,\\mathrm{mA}$ falls from $b$ to $a$ through the vertical $4\\,\\mathrm{k\\Omega}$.", ['eR1', 'eR2', 'eR3', 'eR4']),
       ("Check KCL. At $a$: in $4+0.222=4.222$, out $2.222+2=4.222\\,\\mathrm{mA}$. At $b$: in $6$, out $4+0.222+0.444+1.333=6\\,\\mathrm{mA}$.", []),
       ("Power: only the $6\\,\\mathrm{mA}$ source climbs ($0\\to5.33\\,\\mathrm{V}$): it delivers $32\\,\\mathrm{mW}$. The $4\\,\\mathrm{mA}$ source carries its current **down** from $b$ to $a$ and the $2\\,\\mathrm{mA}$ source **down** from $a$ to ground, so both absorb ($3.56$ and $8.89\\,\\mathrm{mW}$). Resistors: $9.88+0.20+2.37+7.11$. Total absorbed: $32\\,\\mathrm{mW}$.", []),
   ], notes=["A current source's arrow doesn't tell you whether it delivers; the heights do. Two of these three pumps push current downhill, so they absorb power."])],
         spoiler=False, inline=False),
   [S('Ground the bottom wire; name the top wire $a$ and the middle wire $b$. KCL at $a$ (mA and kΩ): the $4\\,\\mathrm{mA}$ comes in, the $2\\,\\mathrm{mA}$ goes out.', '\\frac{a}{2}+\\frac{a-b}{4}+2=4\\;\\Rightarrow\\;3a-b=8'),
    S('KCL at $b$: the $6\\,\\mathrm{mA}$ comes in, the $4\\,\\mathrm{mA}$ goes out.', '\\frac{b-a}{4}+\\frac{b}{12}+\\frac{b}{4}+4=6\\;\\Rightarrow\\;-3a+7b=24'),
    S('Add the two equations.', '6b=32\\;\\Rightarrow\\;b=\\tfrac{16}{3}\\,\\mathrm{V},\\qquad a=\\tfrac{40}{9}\\,\\mathrm{V}'),
    S('$I_0$ is the current down the $12\\,\\mathrm{k\\Omega}$.', 'I_0=\\frac{16/3}{12}=\\frac{4}{9}\\approx0.444\\,\\mathrm{mA}')],
   '$I_0=\\dfrac{4}{9}\\,\\mathrm{mA}\\approx0.444\\,\\mathrm{mA}$ (with $a=4.44\\,\\mathrm{V}$, $b=5.33\\,\\mathrm{V}$). Only the $6\\,\\mathrm{mA}$ source delivers power; the other two absorb.')

json.dump(B, open(os.path.join(HERE, 'w3_blocks.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'blocks')
