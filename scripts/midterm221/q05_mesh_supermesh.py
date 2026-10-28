r"""Midterm Questions Q5: three windows in a row; the 5 A source sits between windows 2 and 3 -> supermesh.
I1 = -1 A, I2 = -3 A, I3 = 2 A. The 20 V source ABSORBS 20 W (I1 < 0), the 5 A source delivers 150 W, the
resistors take 130 W. Inspired by Assessment Problem 4.12 / Textbook P4.62 and the Fall 2025 Q1 supermesh."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

TOPIC = 'Mesh analysis'
MARKS = 10
TITLE = 'A current source between two windows'
SOURCE = 'Assessment Problem 4.12, Textbook P4.62 and Fall 2025 Question 1'
PROMPT = (r'**(a)** Use the mesh-current method to find the three mesh currents. '
          r'**(b)** Find the power of each source, and say whether it absorbs or delivers. '
          r'**(c)** Check that the power balances.')

O = r'\,\Omega'
V = r'\,\mathrm{V}'
A = r'\,\mathrm{A}'

V1 = f'V1 0,3 -> 0,0 "$20{V}$"'
R1 = f'R1 0,3 -> 3,3 "$4{O}$"'
R2 = f'R2 3,3 -> 3,0 "$12{O}$"'
R3 = f'R3 3,3 -> 6,3 "$2{O}$"'
I1 = f'I1 6,0 -> 6,3 "$5{A}$"'
R4 = f'R4 6,3 -> 9,3 "$5{O}$"'
R5 = f'R5 9,3 -> 9,0 "$10{O}$"'
BOT = 'wire 0,0 -> 9,0\nground 0,0'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(V1, R1, R2, R3, I1, R4, R5, BOT)

MESHES = j('#= mesh 1.5,1.5 "$I_1$" cw r=0.6', '#= mesh 4.5,1.5 "$I_2$" cw r=0.6', '#= mesh 7.5,1.5 "$I_3$" cw r=0.6')
CONSTRAINT = '#= text 6,-0.8 "$I_3-I_2=5$" color=purple'
SIGNS_1 = j('#= sign 0.75,2.6 +', '#= sign 2.25,2.6 -',           # 4 Ω: I_1 goes right
            '#= sign 2.6,2.05 +', '#= sign 2.6,0.95 -')           # 12 Ω: I_1 goes down
WALK = '#= path 3,0.4 -> 3,3 -> 9,3 -> 9,0 -> 3.4,0'
SIGNS_SUPER = j('#= sign 3.4,0.95 +', '#= sign 3.4,2.05 -',       # 12 Ω: the walk goes up
                '#= sign 3.75,2.6 +', '#= sign 5.25,2.6 -',       # 2 Ω: right
                '#= sign 6.75,2.6 +', '#= sign 8.25,2.6 -',       # 5 Ω: right
                '#= sign 8.6,2.05 +', '#= sign 8.6,0.95 -')       # 10 Ω: down
FOUND = [r'#+ $I_1=-1\,\mathrm{A}$', r'#+ $I_2=-3\,\mathrm{A}$', r'#+ $I_3=2\,\mathrm{A}$']

STEPS = [
    ('The circuit', GIVEN, r'''
**Method: mesh.** Three windows → three mesh currents.

The $5\,\mathrm{A}$ sits on the wall between windows 2 and 3 → **supermesh** around those two.
'''),
    ('Mesh currents', j(GIVEN, MESHES, CONSTRAINT), r'''
$I_1$, $I_2$, $I_3$, all clockwise.

The $5\,\mathrm{A}$ arrow points **up**:
- $I_3$ goes up through it → $+I_3$
- $I_2$ goes down through it → $-I_2$

$$
I_3-I_2=5
$$
'''),
    ('KVL in mesh $I_1$', j(GIVEN, MESHES, CONSTRAINT, SIGNS_1), r'''
Walk with $I_1$. Sign you **enter** each element by:
- $20\,\mathrm{V}$: enter $-$ → $-20$
- $4\,\Omega$: $+4I_1$
- $12\,\Omega$ (shared with $I_2$): $+12(I_1-I_2)$

$$
-20+4I_1+12(I_1-I_2)=0
$$

$$
4I_1-3I_2=5
$$
'''),
    ('KVL around the supermesh', j(GIVEN, MESHES, CONSTRAINT, WALK, SIGNS_SUPER), r'''
Walk around $I_2$ and $I_3$ **together**, skipping the $5\,\mathrm{A}$ branch.

- $12\,\Omega$ (going up, shared with $I_1$): $+12(I_2-I_1)$
- $2\,\Omega$: $+2I_2$
- $5\,\Omega$ and $10\,\Omega$: $+5I_3+10I_3$

$$
12(I_2-I_1)+2I_2+15I_3=0
$$

$$
-12I_1+14I_2+15I_3=0
$$
'''),
    ('(a) Solve', j(GIVEN, MESHES, *FOUND), r'''
Put $I_3=I_2+5$ into the supermesh:

$$
-12I_1+29I_2=-75
$$

From mesh 1, $I_1=\dfrac{5+3I_2}{4}$, so $12I_1=15+9I_2$:

$$
-15-9I_2+29I_2=-75 \;\Rightarrow\; I_2=-3\,\mathrm{A}
$$

$$
\boxed{I_1=-1\,\mathrm{A} \qquad I_2=-3\,\mathrm{A} \qquad I_3=2\,\mathrm{A}}
$$

(Or type the 3 equations into the fx-991 equation solver.)
'''),
    ('Voltage across the $5\\,\\mathrm{A}$', j(GIVEN, '#= path 6,3 -> 9,3 -> 9,0 -> 6.4,0',
                                                  '#= sign 6.75,2.6 +', '#= sign 8.25,2.6 -',
                                                  '#= sign 8.6,2.05 +', '#= sign 8.6,0.95 -',
                                                  '#= text 7.2,1.5 "$v=30\\,\\mathrm{V}$" color=pink', *FOUND,
                                                  r'#+ $v_{5A}=30\,\mathrm{V}$'), r'''
A current source has no fixed voltage → find it with a KVL walk.

Walk from its top, through $5\,\Omega$ and $10\,\Omega$, to its bottom. Only $I_3=2\,\mathrm{A}$ runs there, the same way:

$$
v=5(2)+10(2)=30\,\mathrm{V}\ \ (+\ \text{on top})
$$
'''),
    ('(b) Source powers', j(GIVEN, '#= mesh 1.5,1.5 "$-1\\,\\mathrm{A}$" cw r=0.6',
                            '#= text 7.2,1.5 "$30\\,\\mathrm{V}$" color=pink', *FOUND,
                            r'#+ $p_{20V}=20\,\mathrm{W}\ \text{abs.}$', r'#+ $p_{5A}=150\,\mathrm{W}\ \text{del.}$'), r'''
**$20\,\mathrm{V}$:** $I_1$ would leave its $+$, but $I_1=-1\,\mathrm{A}$ → $1\,\mathrm{A}$ **enters** the $+$ → it **absorbs** (it is being charged):

$$
\boxed{p_{20V}=(20)(1)=20\,\mathrm{W}\ \text{absorbed}}
$$

**$5\,\mathrm{A}$:** its $5\,\mathrm{A}$ leaves the $+$ (top) → it **delivers**:

$$
\boxed{p_{5A}=(30)(5)=150\,\mathrm{W}\ \text{delivered}}
$$
'''),
    ('(c) Power balance', j(GIVEN, '#= text 1.5,3.7 "$1\\,\\mathrm{A}$" color=pink', '#= text 3.65,1.5 "$2\\,\\mathrm{A}$" color=pink',
                            '#= text 4.5,3.7 "$3\\,\\mathrm{A}$" color=pink', '#= text 7.5,3.7 "$2\\,\\mathrm{A}$" color=pink',
                            '#= text 9.9,1.5 "$2\\,\\mathrm{A}$" color=pink', *FOUND), r'''
Current in each resistor:
- $4\,\Omega$: $|I_1|=1\,\mathrm{A}$
- $12\,\Omega$: $|I_1-I_2|=|-1+3|=2\,\mathrm{A}$
- $2\,\Omega$: $|I_2|=3\,\mathrm{A}$
- $5\,\Omega$, $10\,\Omega$: $I_3=2\,\mathrm{A}$

$$
p_R=4(1)^2+12(2)^2+2(3)^2+5(2)^2+10(2)^2
$$

$$
p_R=4+48+18+20+40=130\,\mathrm{W}
$$

Delivered $150\,\mathrm{W}$ = absorbed $130+20=150\,\mathrm{W}$ ✓
'''),
]


NET = [('V', 'V1', 's', '0', 20), ('R', 'R1', 's', 'a', 4), ('R', 'R2', 'a', '0', 12), ('R', 'R3', 'a', 'b', 2),
       ('I', 'I1', '0', 'b', 5), ('R', 'R4', 'b', 'c', 5), ('R', 'R5', 'c', '0', 10)]


def checks(check):
    els, _ = check(GIVEN)
    s, a = els['R1']
    b, c = els['R4']
    assert els['V1'] == (s, '0') and els['R2'] == (a, '0') and els['R3'] == (a, b), els
    assert els['I1'] == ('0', b) and els['R5'] == (c, '0'), els
    I1, I2, I3 = F(-1), F(-3), F(2)
    assert I3 - I2 == 5
    assert -20 + 4 * I1 + 12 * (I1 - I2) == 0 and 4 * I1 - 3 * I2 == 5
    assert 12 * (I2 - I1) + 2 * I2 + 15 * I3 == 0 and -12 * I1 + 14 * I2 + 15 * I3 == 0
    assert -12 * I1 + 29 * I2 == -75 and 12 * I1 == 15 + 9 * I2 and -15 - 9 * I2 + 29 * I2 == -75
    v = 5 * I3 + 10 * I3
    assert v == 30 and v * 5 == 150 and 20 * -I1 == 20
    pr = 4 * I1 ** 2 + 12 * (I1 - I2) ** 2 + 2 * I2 ** 2 + 5 * I3 ** 2 + 10 * I3 ** 2
    assert pr == 130 and pr + 20 == 150
    Vn, I, P = solve(NET)
    assert abs(I['R1'] - I1) < 1e-9 and abs(I['R3'] - I2) < 1e-9 and abs(I['R4'] - I3) < 1e-9
    assert abs(Vn['b'] - 30) < 1e-9 and abs(P['V1'] - 20) < 1e-9 and abs(P['I1'] + 150) < 1e-9, (P['V1'], P['I1'])
