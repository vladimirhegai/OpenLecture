r"""Textbook P4.68: Thévenin equivalent at a-b. V_oc by mesh + Ohm (three windows, the top one fixed by the 3 A
source) and a KVL walk; R_Th with the sources off."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'C'
TITLE = 'Thévenin: two sources and an open port'
SOURCE = 'Textbook P4.68'
CITES = [{"chunk_id": "0da028c8-138a-47c7-8ee5-99ac30e9dc71", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1}]
PROMPT = 'Find the Thévenin equivalent at $a$–$b$.'

O = r'\,\Omega'
V1 = r'V1 0,3 -> 0,0 "$300\,\mathrm{V}$"'
R1 = f'R1 0,3 -> 4,3 "$40{O}$"'
R2 = f'R2 4,3 -> 4,0 "$8{O}$"'
R3 = f'R3 4,3 -> 8,3 "$10{O}$"'
R4 = f'R4 0,5 -> 8,5 "$150{O}$"'
I1 = r'I1 8,7 -> 0,7 "$3\,\mathrm{A}$"'
STUBS = '\n'.join(['wire 0,3 -> 0,5', 'wire 8,5 -> 8,3', 'wire 0,5 -> 0,7', 'wire 8,7 -> 8,5'])
FRAME = '\n'.join(['wire 8,3 -> 10,3', 'terminal 10,3 "$a$" right', 'terminal 10,0 "$b$" right',
                   'wire 0,0 -> 10,0', 'label 4,3 "$m$" above', 'ground 0,0'])
VOC = 'gap 10,3 -> 10,0 v="$V_{oc}$"'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(V1, R1, R2, R3, 'wire 0,3 -> 0,5', R4, 'wire 8,5 -> 8,3', 'wire 0,5 -> 0,7', I1, 'wire 8,7 -> 8,5', FRAME)
CIRCUIT = j(V1, R1, R2, R3, R4, I1, STUBS, FRAME, VOC)

MESHES = '\n'.join(['#= mesh 2,1.5 "$I_1$" cw r=0.7', '#= mesh 6.6,4.2 "$I_2$" cw r=0.5', '#= mesh 1.6,6 "$I_3$" cw r=0.55'])
# + where each mesh current enters: mesh 1 (right along the 40 Ω, down the 8 Ω)
SIGNS_1 = '\n'.join(['#= sign 1.2,2.65 +', '#= sign 2.8,2.65 -', '#= sign 3.65,2.3 +', '#= sign 3.65,0.7 -'])
# mesh 2 (right along the 150 Ω, left along the 10 Ω and the 40 Ω)
SIGNS_2 = '\n'.join(['#= sign 3.2,4.65 +', '#= sign 4.8,4.65 -', '#= sign 6.8,3.35 +', '#= sign 5.2,3.35 -',
                     '#= sign 2.8,3.35 +', '#= sign 1.2,3.35 -'])
WALK = '#= path 9.75,3 -> 4,3 -> 4,0 -> 9.7,0'
WALK_SIGNS = '\n'.join(['#= sign 6.8,3.35 +', '#= sign 5.2,3.35 -', '#= sign 3.65,2.3 +', '#= sign 3.65,0.7 -'])

OFF = j(R1, R2, R3, R4, 'wire 0,3 -> 0,0', 'wire 0,3 -> 0,5', 'wire 8,5 -> 8,3', 'wire 0,5 -> 0,7',
        'wire 8,7 -> 8,5', FRAME)
LOOK = '#= path 11.4,1.5 -> 10.25,1.5 thin color=accent\n#= text 11,1.95 "$R_{Th}$" color=accent'

THEV = j(r'VTH 0,3 -> 0,0 "$30\,\mathrm{V}$"', f'RTH 0,3 -> 4,3 "$15{O}$"', 'wire 4,3 -> 8,3',
         'wire 8,3 -> 10,3', 'terminal 10,3 "$a$" right', 'terminal 10,0 "$b$" right', 'wire 0,0 -> 10,0', 'ground 0,0')

STEPS = [
    ('The circuit', CIRCUIT, r'''
Find the Thévenin equivalent at $a$–$b$. No load here: $a$–$b$ stays open.

**Plan**
1. $V_{Th}=V_{oc}$ with mesh + Ohm.
2. $R_{Th}$: sources off.
3. Draw $V_{Th}$ in series with $R_{Th}$.
'''),
    ('Mesh currents', j(CIRCUIT, MESHES, r'#+ $I_3=-3\,\mathrm{A}$'), r'''
Three closed windows → $I_1$, $I_2$, $I_3$ (all clockwise).

The space under the $10\,\Omega$ is **not** a mesh: it is open at $a$–$b$.

$I_3$ is the only current through the $3\,\mathrm{A}$ source.

The source points **left**, $I_3$ goes **right** along the top:

$$
I_3=-3\,\mathrm{A}
$$
'''),
    ('KVL mesh 1', j(CIRCUIT, MESHES, SIGNS_1), r'''
$+$ where $I_1$ enters. Signs you enter by:
- $300\,\mathrm{V}$: enter $-$ → $-300$
- $40\,\Omega$ (shared with $I_2$): $+40(I_1-I_2)$
- $8\,\Omega$: $+8I_1$

$$
-300+40(I_1-I_2)+8I_1=0
$$

$$
48I_1-40I_2=300
$$
'''),
    ('KVL mesh 2', j(CIRCUIT, MESHES, SIGNS_2, r'#+ $I_1=5.25\,\mathrm{A}$', r'#+ $I_2=-1.2\,\mathrm{A}$'), r'''
- $150\,\Omega$ (shared with $I_3$): $+150(I_2-I_3)$
- $10\,\Omega$: $+10I_2$
- $40\,\Omega$ (shared with $I_1$): $+40(I_2-I_1)$

$$
150(I_2+3)+10I_2+40(I_2-I_1)=0
$$

$$
-40I_1+200I_2=-450
$$

With mesh 1, $I_1=\dfrac{300+40I_2}{48}$:

$$
I_2=-1.2\,\mathrm{A} \qquad I_1=5.25\,\mathrm{A}
$$
'''),
    ('KVL walk to $V_{oc}$', j(CIRCUIT, WALK, WALK_SIGNS, r'#+ $V_{Th}=30\,\mathrm{V}$'), r'''
Walk from $a$ to $b$: through the $10\,\Omega$, down the $8\,\Omega$.

Sign you enter by:
- $10\,\Omega$: only $I_2$, walking with it → $+10I_2=-12$
- $8\,\Omega$: only $I_1$, walking with it → $+8I_1=42$

$$
V_{oc}=-12+42=30\,\mathrm{V}
$$

$$
\boxed{V_{Th}=30\,\mathrm{V}}
$$
'''),
    ('$R_{Th}$: sources off', j(OFF, LOOK, r'#+ $R_{Th}=15\,\Omega$'), r'''
$300\,\mathrm{V}$ off → **wire**. $3\,\mathrm{A}$ off → **open**.

Look in from $a$:
- $40\,\Omega$ and $8\,\Omega$ both go from $m$ to the bottom → parallel
- then in series with the $10\,\Omega$
- the $150\,\Omega$ goes from $a$ to the bottom → parallel with all that

$$
40\parallel8=\frac{(40)(8)}{48}=\tfrac{20}{3}\,\Omega
$$

$$
R_{Th}=150\parallel\left(10+\tfrac{20}{3}\right)=150\parallel\tfrac{50}{3}=15\,\Omega
$$
'''),
    ('Thévenin circuit', THEV, r'''
$$
\boxed{V_{Th}=30\,\mathrm{V} \qquad R_{Th}=15\,\Omega}
$$

Any load on $a$–$b$ now sees just these two parts.
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    top, m, a = els['R1'][0], els['R1'][1], els['R3'][1]
    assert els['V1'] == (top, '0') and els['R2'] == (m, '0') and els['R3'] == (m, a), els
    assert els['R4'] == (top, a) and els['I1'] == (a, top), els   # 3 A pushed from a toward the 300 V node
    # mesh equations, exact
    I3 = F(-3)
    I2 = F(-6, 5)
    I1 = (300 + 40 * I2) / 48
    assert I1 == F(21, 4)
    assert -300 + 40 * (I1 - I2) + 8 * I1 == 0 and 48 * I1 - 40 * I2 == 300
    assert 150 * (I2 - I3) + 10 * I2 + 40 * (I2 - I1) == 0 and -40 * I1 + 200 * I2 == -450
    assert 10 * I2 == -12 and 8 * I1 == 42 and -12 + 42 == 30
    assert F(40 * 8, 48) == F(20, 3) and 10 + F(20, 3) == F(50, 3)
    assert 150 * F(50, 3) / (150 + F(50, 3)) == 15
    # independent nodal solve (b = ground)
    V, I, _ = solve([('V', 'V1', 'L', '0', 300), ('R', 'R1', 'L', 'm', 40), ('R', 'R2', 'm', '0', 8),
                     ('R', 'R3', 'm', 'a', 10), ('R', 'R4', 'L', 'a', 150), ('I', 'I1', 'a', 'L', 3)])
    assert abs(V['a'] - 30) < 1e-9 and abs(I['R2'] - 5.25) < 1e-9 and abs(I['R3'] - 1.2) < 1e-9
    # R_Th by a 1 A test source into a with the sources off
    V, _, _ = solve([('R', 'R1', 'L', 'm', 40), ('R', 'R2', 'm', '0', 8), ('R', 'R3', 'm', 'a', 10),
                     ('R', 'R4', 'L', 'a', 150), ('V', 'V1', 'L', '0', 0), ('I', 'T', '0', 'a', 1)])
    assert abs(V['a'] - 15) < 1e-9
