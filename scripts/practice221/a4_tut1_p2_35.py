r"""Tutorial 1, P2.35: two networks joined by one wire (KCL says it carries nothing), a mesh on the left,
a dependent current source and a KVL walk on the right.

`#+` values accumulate from step to step: declare each one only in the step that finds it.
"""

SECTION = 'A'
TITLE = 'Two circuits joined by one wire'
SOURCE = 'Tutorial 1, P2.35'
CITES = [{'chunk_id': '04048b9d-3ebb-47c7-9f80-9fff26984c75', 'source_id': 'a27e0480-0d8e-4205-adf6-ee6eb12fabf7', 'version': 1}]
PROMPT = r'Find $i_o$ (the current in the wire joining the two networks), $i_1$ and $i_2$.'

O = r'\,\Omega'
LEFT = '\n'.join([
    r'V1 0,3 -> 0,0 "$18\,\mathrm{V}$"',
    f'R1 0,3 -> 3,3 "$12{O}$"',
    f'R2 3,3 -> 3,0 "$6{O}$" v="$v_\\Delta$"',
    'wire 3,0 -> 0,0',
])
JOIN = 'wire 3,0 -> 5,0\nlabel 4,0 "$\\leftarrow i_o$" below'
RIGHT = '\n'.join([
    r'G1 5,3 -> 5,0 "$\dfrac{v_\Delta}{2}$"',
    'wire 5,3 -> 10,3',
    'wire 5,0 -> 10,0',
    f'R3 7.5,3 -> 7.5,0 "$10{O}$" i="$i_1$"',
    f'R4 10,3 -> 10,0 "$5{O}$" i="$i_2$"',
])


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(LEFT, JOIN, RIGHT)

BOX = '#= region -1.3,-0.55 3.7,3.75 "left half" color=green'
ZERO = r'#= text 4,0.45 "$i_o=0$" color=pink'
MESH = '#= mesh 1.5,1.5 "$I$" cw r=0.7'
SIGNS = j('#= sign 0.55,2.62 +', '#= sign 2.45,2.62 -',    # 12: I enters on the left
          '#= sign 2.62,2.2 +', '#= sign 2.62,0.8 -')      # 6: I enters at the top
VD = r'#= text 2.2,1.5 "$6\,\mathrm{V}$" color=pink'
G3 = r'#= text 5.75,1.5 "$3\,\mathrm{A}$" color=pink'
TOPNODE = '#= region 4.6,2.6 10.4,3.4 "node" color=green'
WALK = '#= path 7.5,1.6 -> 7.5,3 -> 10,3 -> 10,0 -> 7.5,0 -> 7.5,1.0'
RSIGNS = j('#= sign 9.62,2.2 +', '#= sign 9.62,0.8 -',      # 5: i2 reference, + on top
           '#= sign 7.88,2.2 +', '#= sign 7.88,0.8 -')     # 10: i1 reference, + on top

STEPS = [
    ('The circuit', GIVEN, r'''
Two networks touch through **one** wire.

Find $i_o$ in that wire, then $i_1$ and $i_2$.
'''),
    ('KCL around the left half', j(GIVEN, BOX, ZERO, r'#+ $i_o=0$'), r'''
Draw a box around the left half. Only **one** wire crosses it.

KCL for the whole box: what goes in must come out.

There is no second wire to bring current back, so

$$
i_o=0
$$

The wire only puts both bottoms at the same voltage.
'''),
    ('Left loop: mesh + KVL', j(GIVEN, ZERO, MESH, SIGNS, r'#+ $I=1\,\mathrm{A}$'), r'''
With $i_o=0$ the left side is one loop. Mesh current $I$, clockwise.

Sign you **enter** each element by:
- $18\,\mathrm{V}$: enter $-$ → $-18$
- $12\,\Omega$: enter $+$ → $+12I$
- $6\,\Omega$: enter $+$ → $+6I$

$$
-18+12I+6I=0 \;\Rightarrow\; I=1\,\mathrm{A}
$$
'''),
    ("Ohm's law → $v_\\Delta$", j(GIVEN, ZERO, MESH, VD, r'#+ $v_\Delta=6\,\mathrm{V}$'), r'''
$I$ enters the $6\,\Omega$ at the top, the $+$ end of $v_\Delta$.

$$
v_\Delta=(6)(1)=6\,\mathrm{V}
$$
'''),
    ('The dependent source + KCL', j(GIVEN, ZERO, VD, G3, TOPNODE), r'''
The diamond pulls $\dfrac{v_\Delta}{2}=\dfrac{6}{2}=3\,\mathrm{A}$ **down** out of the right top node.

KCL at that node (leaving $-$): $i_1$, $i_2$ and the $3\,\mathrm{A}$ all leave.

$$
-i_1-i_2-3=0 \;\Rightarrow\; i_1+i_2=-3
$$
'''),
    ('KVL around the right window', j(GIVEN, ZERO, G3, WALK, RSIGNS, r'#+ $i_1=-1\,\mathrm{A}$', r'#+ $i_2=-2\,\mathrm{A}$'), r'''
Walk clockwise: across the top, down the $5\,\Omega$, back, up the $10\,\Omega$.
- $5\,\Omega$: enter $+$ → $+5i_2$
- $10\,\Omega$ (going up): enter $-$ → $-10i_1$

$$
5i_2-10i_1=0 \;\Rightarrow\; i_2=2i_1
$$

Into the KCL:

$$
3i_1=-3 \;\Rightarrow\; i_1=-1\,\mathrm{A},\quad i_2=-2\,\mathrm{A}
$$

Negative: both really flow **up**, against their arrows.
'''),
]


def checks(check):
    els, raw = check(GIVEN)
    bot = els['V1'][1]
    assert els['R2'][1] == bot and els['G1'][1] == bot and els['R3'][1] == bot and els['R4'][1] == bot, els
    assert els['V1'][0] == els['R1'][0] and els['R1'][1] == els['R2'][0], els
    top = els['G1'][0]
    assert els['R3'][0] == top and els['R4'][0] == top and top != els['R2'][0], els
    from fractions import Fraction as F
    io = 0                                                    # one wire, KCL around the left half
    I = F(18, 12 + 6)                                         # -18 + 12I + 6I = 0
    assert I == 1
    vd = 6 * I
    assert vd == 6
    g = vd / 2
    assert g == 3
    i1 = F(-3, 3)                                             # i1 + i2 = -3 and i2 = 2 i1
    i2 = 2 * i1
    assert (i1, i2) == (-1, -2) and i1 + i2 + g == 0 and 5 * i2 - 10 * i1 == 0
    # independent check: nodal solve of both halves together (shared bottom = ground)
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
    from mna import solve
    V, Ic, P = solve([('V', 'vs', 't', '0', 18.0), ('R', 'r12', 't', 'm', 12), ('R', 'r6', 'm', '0', 6),
                      ('G', 'g', 'c', '0', {'m': 0.5}), ('R', 'r10', 'c', '0', 10), ('R', 'r5', 'c', '0', 5)])
    assert abs(V['m'] - 6) < 1e-9 and abs(Ic['r10'] + 1) < 1e-9 and abs(Ic['r5'] + 2) < 1e-9, (V, Ic)
    assert io == 0
