r"""ELEC 221 Midterm Fall 2025, Question 3: find I_x and V_x in a series/parallel ladder fed by a current source.
The source's value is cut off on the posted exam; the user chose to use 9 A (answers come out whole: 1 A, 3 V).
Collapse from the right, one 2-mesh solve on the reduced circuit, then expand back with Ohm's law."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'M'
TITLE = 'Q3: Series and parallel back and forth'
SOURCE = 'ELEC 221 Midterm, Fall 2025, Question 3 (Fig. P3)'
PROMPT = (r'Find $I_x$ and $V_x$.'
          '\n\n'
          r"*The current source's value is cut off on the posted exam, so we use $9\,\mathrm{A}$ here.*")

O = r'\,\Omega'

IS = 'I1 0,0 -> 0,4 "$9\\,\\mathrm{A}$"'
LEFT = '\n'.join(['wire 0,4 -> 2,4', f'R2 2,4 -> 2,0 "$2{O}$"', f'R1 2,4 -> 5,4 "$1{O}$" v="$V_x$"'])
MID = '\n'.join([f'R4 5,4 -> 5,2 "$4{O}$"', 'wire 4,2 -> 6,2', f'R3 4,2 -> 4,0 "$3{O}$" i="$I_x$"',
                 f'R6 6,2 -> 6,0 "$6{O}$"'])
RIGHT = '\n'.join([f'R12A 5,4 -> 8,4 "$1.2{O}$"', f'R8 8,4 -> 8,0 "$8{O}$"', 'wire 8,4 -> 10,4',
                   f'R12 10,4 -> 10,0 "$12{O}$"'])


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(IS, LEFT, MID, RIGHT, 'wire 0,0 -> 10,0', 'ground 0,0')
PAIRS = j(IS, LEFT, f'R4 5,4 -> 5,2 "$4{O}$"', f'RP 5,2 -> 5,0 "$2{O}$"',
          f'R12A 5,4 -> 8,4 "$1.2{O}$"', f'RQ 8,4 -> 8,0 "$4.8{O}$"', 'wire 0,0 -> 8,0', 'ground 0,0')
SERIES = j(IS, LEFT, f'RS 5,4 -> 5,0 "$6{O}$"', 'wire 5,4 -> 8,4', f'RT 8,4 -> 8,0 "$6{O}$"',
           'wire 0,0 -> 8,0', 'ground 0,0')
LAST = j(IS, LEFT, f'RU 5,4 -> 5,0 "$3{O}$" flip', 'wire 0,0 -> 5,0', 'ground 0,0')

MESHES = j('#= mesh 1,1 "$I_1$" cw r=0.45', '#= mesh 3.5,2 "$I_2$" cw r=0.7')
SIGNS = j('#= sign 4.6,3.0 +', '#= sign 4.6,1.0 -',           # 3 Ω: I_2 goes down (1 Ω: the V_x marks)
          '#= sign 2.4,0.6 +', '#= sign 2.4,3.4 -')           # 2 Ω: I_2 goes up

STEPS = [
    ('The circuit', GIVEN, r'''
One source, and every pair of resistors is plainly in series or in parallel.

**Plan**
1. Collapse the circuit from the right.
2. Solve the small circuit (mesh + Ohm).
3. Expand back, with Ohm's law, to $V_x$ and $I_x$.

The source's value is missing on the exam, so we use $9\,\mathrm{A}$.
'''),
    ('Parallel pairs', PAIRS, r'''
Product over sum:

$$
3\parallel 6=\frac{(3)(6)}{3+6}=2\,\Omega
$$

$$
8\parallel 12=\frac{(8)(12)}{8+12}=4.8\,\Omega
$$
'''),
    ('Series pairs', SERIES, r'''
Each branch is now two resistors in a row:

$$
4+2=6\,\Omega \qquad 1.2+4.8=6\,\Omega
$$
'''),
    ('Two equal branches', LAST, r'''
Two $6\,\Omega$ from the same node to ground → parallel:

$$
6\parallel 6=3\,\Omega
$$

Two equal branches split current **half and half**: remember that for later.
'''),
    ('Mesh + Ohm', j(LAST, MESHES, SIGNS, r'#+ $I_2=3\,\mathrm{A}$', r'#+ $V_x=3\,\mathrm{V}$'), r'''
$I_1$: the source is on its outside edge, arrow up, same way as $I_1$ → $I_1=9\,\mathrm{A}$.

KVL for $I_2$ (sign you **enter** each element by):

$$
1I_2+3I_2+2(I_2-I_1)=0
$$

$$
6I_2=2(9)=18 \;\Rightarrow\; I_2=3\,\mathrm{A}
$$

$I_2$ is the current through the $1\,\Omega$, entering at $+$:

$$
\boxed{V_x=(1)(3)=3\,\mathrm{V}}
$$
'''),
    ('Back out: the two $6\\,\\Omega$', j(SERIES, '#= text 5,4.7 "$9\\,\\mathrm{V}$" color=pink',
                                       '#= text 5.9,1 "$1.5\\,\\mathrm{A}$" color=orange',
                                       '#= text 8.9,1 "$1.5\\,\\mathrm{A}$" color=orange'), r'''
Voltage on the $3\,\Omega$ (Ohm's law):

$$
V=(3)(3)=9\,\mathrm{V}
$$

Both $6\,\Omega$ branches have that same $9\,\mathrm{V}$. Each carries:

$$
\frac{9}{6}=1.5\,\mathrm{A}
$$
'''),
    ('Back out: $I_x$', j(GIVEN, '#= text 5.9,3 "$1.5\\,\\mathrm{A}$" color=orange',
                          '#= text 7,1 "$3\\,\\mathrm{V}$" color=pink', r'#+ $I_x=1\,\mathrm{A}$'), r'''
$1.5\,\mathrm{A}$ goes down the $4\,\Omega$, then into $3\parallel 6=2\,\Omega$.

Voltage across the $3\,\Omega$ and $6\,\Omega$:

$$
V=(2)(1.5)=3\,\mathrm{V}
$$

Ohm's law on the $3\,\Omega$:

$$
\boxed{I_x=\frac{3}{3}=1\,\mathrm{A}}
$$

Check: the $6\,\Omega$ takes $3/6=0.5\,\mathrm{A}$, and $1+0.5=1.5\,\mathrm{A}$ ✓
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    t, n = els['R1']
    p = els['R4'][1]
    assert els['I1'] == ('0', t) and els['R2'] == (t, '0') and els['R4'][0] == n, els
    assert els['R3'] == (p, '0') and els['R6'] == (p, '0'), els
    r = els['R12A'][1]
    assert els['R12A'][0] == n and els['R8'] == (r, '0') and els['R12'] == (r, '0'), els
    for d in (PAIRS, SERIES, LAST):
        check(d)
    assert F(18, 9) == 2 and F(96, 20) == F(24, 5) and F(6) / 2 == 3
    I1, I2 = 9, 3
    assert I2 + 3 * I2 + 2 * (I2 - I1) == 0 and 6 * I2 == 18
    assert 3 * I2 == 9 and F(9, 6) == F(3, 2) and 2 * F(3, 2) == 3 and F(3, 6) + 1 == F(3, 2)
    Vn, I, _ = solve([('I', 'I1', '0', 't', 9), ('R', 'R2', 't', '0', 2), ('R', 'R1', 't', 'n', 1),
                      ('R', 'R4', 'n', 'p', 4), ('R', 'R3', 'p', '0', 3), ('R', 'R6', 'p', '0', 6),
                      ('R', 'R12A', 'n', 'r', 1.2), ('R', 'R8', 'r', '0', 8), ('R', 'R12', 'r', '0', 12)])
    assert abs(I['R3'] - 1) < 1e-9 and abs(Vn['t'] - Vn['n'] - 3) < 1e-9 and abs(Vn['n'] - 9) < 1e-9
    assert abs(I['R4'] - 1.5) < 1e-9 and abs(Vn['p'] - 3) < 1e-9
