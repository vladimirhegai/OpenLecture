r"""Assessment Problem 4.16: Thévenin equivalent at a, b. V_oc by mesh + Ohm (two meshes), R_Th with the source off.

Figure: the course's Chapter 4 assessment solutions, p. 4-12 (the textbook in the course is a different edition,
where AP 4.16 is another circuit). The bottom-right window (20 Ω, 8 Ω, open terminals) carries no mesh current.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'C'
TITLE = 'Thévenin: two meshes, then a walk'
SOURCE = 'Assessment Problem 4.16'
CITES = [{'chunk_id': '3cd5f2a4-e171-47b0-85b3-23c63b510b6b', 'source_id': '3b287f2d-b408-41eb-a523-b299688ff303', 'version': 1}]
PROMPT = r'Find the Thévenin equivalent circuit with respect to the terminals $a$, $b$.'

O = r'\,\Omega'
V = r'\,\mathrm{V}'
VS = f'V1 0,2.5 -> 0,0 "$72{V}$"'
R5 = f'R1 0,2.5 -> 3,2.5 "$5{O}$"'
R20 = f'R2 3,2.5 -> 3,0 "$20{O}$"'
R8 = f'R3 3,2.5 -> 6,2.5 "$8{O}$"'
TOP = '\n'.join(['wire 0,2.5 -> 0,4.5 -> 1.5,4.5', f'R4 1.5,4.5 -> 4.5,4.5 "$12{O}$"', 'wire 4.5,4.5 -> 6,4.5 -> 6,2.5'])
FRAME = '\n'.join(['wire 6,2.5 -> 7.5,2.5', 'wire 0,0 -> 7.5,0', 'terminal 7.5,2.5', 'terminal 7.5,0',
                   'label 7.5,2.5 "$a$" right', 'label 7.5,0 "$b$" right'])
VTH = 'gap 7.5,2.5 -> 7.5,0 v="$V_{Th}$"'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(VS, R5, R20, R8, TOP, FRAME)
OPEN = j(GIVEN, VTH)
M1 = '#= mesh 1.3,1.25 "$I_1$" cw r=0.6'
M2 = '#= mesh 3,3.5 "$I_2$" cw r=0.6'
S5_M1 = j('#= sign 0.5,2.15 +', '#= sign 2.5,2.15 -')
S20 = j('#= sign 3.35,2.0 +', '#= sign 3.35,0.5 -')
S12 = j('#= sign 1.85,4.15 +', '#= sign 4.15,4.15 -')
S8 = j('#= sign 5.5,2.85 +', '#= sign 3.5,2.85 -')
S5_M2 = j('#= sign 2.5,2.85 +', '#= sign 0.5,2.85 -')

STEPS = [
    ('The circuit', OPEN, r'''
Nothing is connected to $a$, $b$ → they are already **open**: their voltage is $V_{Th}$.

**Plan**
1. $V_{Th}=V_{oc}$: mesh currents, then a KVL walk from $a$ to $b$.
2. $R_{Th}$: source off.
'''),
    ('Mesh currents', j(OPEN, M1, M2), r'''
Two closed windows: $I_1$ (source, $5\,\Omega$, $20\,\Omega$) and $I_2$ (top: $12\,\Omega$, $8\,\Omega$, $5\,\Omega$).

The window right of the $20\,\Omega$ ends at the **open** terminals → no mesh current there.

The $5\,\Omega$ is shared → it carries $I_1-I_2$ (in $I_1$'s direction).
'''),
    ('KVL: mesh 1', j(OPEN, M1, M2, S5_M1, S20), r'''
$+$ where $I_1$ **enters**. Sign you enter by:

$$
-72+5(I_1-I_2)+20I_1=0
$$

$$
25I_1-5I_2=72
$$
'''),
    ('KVL: mesh 2 → solve', j(OPEN, M1, M2, S12, S8, S5_M2, r'#+ $I_1=3\,\mathrm{A}$', r'#+ $I_2=0.6\,\mathrm{A}$'), r'''
$+$ where $I_2$ **enters** (the $5\,\Omega$ signs flip):

$$
12I_2+8I_2+5(I_2-I_1)=0
$$

$$
25I_2=5I_1 \;\Rightarrow\; I_1=5I_2
$$

Into mesh 1:

$$
25(5I_2)-5I_2=72 \;\Rightarrow\; 120I_2=72
$$

$$
I_2=0.6\,\mathrm{A} \qquad I_1=3\,\mathrm{A}
$$
'''),
    ('Walk from $a$ to $b$', j(OPEN, S8, S20, '#= path 7.3,2.5 -> 3,2.5 -> 3,0 -> 7.3,0', r'#+ $V_{Th}=64.8\,\mathrm{V}$'), r'''
Walk $a$ → $8\,\Omega$ → $20\,\Omega$ → $b$. Sign you enter by:
- $8\,\Omega$: carries $I_2$ from $a$; enter $+$ → $+8I_2=+4.8$
- $20\,\Omega$: carries $I_1$ down; enter $+$ → $+20I_1=+60$

$$
V_{oc}=4.8+60=64.8\,\mathrm{V}
$$

$$
\boxed{V_{Th}=64.8\,\mathrm{V}}
$$
'''),
    ('$R_{Th}$: source off', j(R5, R20, R8, TOP, FRAME, 'wire 0,2.5 -> 0,0',
                              '#= path 8.9,1.25 -> 7.8,1.25 thin color=accent', '#= text 8.5,1.7 "$R_{Th}$" color=accent',
                              r'#+ $R_{Th}=6\,\Omega$'), r'''
$72\,\mathrm{V}$ off → **wire**: the left node joins $b$.

- $5\,\Omega$ and $20\,\Omega$ both run from $b$ to the middle node → parallel: $\frac{(5)(20)}{25}=4\,\Omega$
- then the $8\,\Omega$ in series: $4+8=12\,\Omega$ (from $b$ to $a$)
- the $12\,\Omega$ on top also runs from $b$ to $a$ → parallel:

$$
R_{Th}=\frac{(12)(12)}{12+12}=6\,\Omega
$$
'''),
    ('Thévenin circuit', j(f'VTH 0,2.5 -> 0,0 "$64.8{V}$"', f'RTH 0,2.5 -> 3,2.5 "$6{O}$"', 'wire 3,2.5 -> 6,2.5', FRAME, VTH), r'''
The whole circuit, as seen from $a$, $b$:

$$
\boxed{V_{Th}=64.8\,\mathrm{V} \text{ in series with } R_{Th}=6\,\Omega}
$$

$+$ at $a$.
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    top, mid, a, bot = els['V1'][0], els['R2'][0], els['R3'][1], els['V1'][1]
    assert els['R1'] == (top, mid) and els['R2'] == (mid, bot) and els['R3'] == (mid, a), els
    assert set(els['R4']) == {top, a}, els                          # 12 Ω from the source's + node to a
    # mesh solve
    I2 = 72 / 120
    I1 = 5 * I2
    assert abs(I2 - 0.6) < 1e-12 and abs(I1 - 3) < 1e-12
    assert abs(25 * I1 - 5 * I2 - 72) < 1e-12 and abs(12 * I2 + 8 * I2 + 5 * (I2 - I1)) < 1e-12
    Voc = 8 * I2 + 20 * I1
    assert abs(8 * I2 - 4.8) < 1e-12 and abs(20 * I1 - 60) < 1e-12 and abs(Voc - 64.8) < 1e-12
    Vn, _, _ = solve([('V', 'V1', 't', '0', 72), ('R', 'R1', 't', 'm', 5), ('R', 'R2', 'm', '0', 20),
                      ('R', 'R3', 'm', 'a', 8), ('R', 'R4', 't', 'a', 12)])
    assert abs(Vn['a'] - 64.8) < 1e-9 and abs(Vn['m'] - 60) < 1e-9
    # R_Th
    p = 5 * 20 / 25
    assert p == 4 and p + 8 == 12 and 12 * 12 / 24 == 6
    # R_Th = V_oc / I_sc as an independent check
    Vs, Is, _ = solve([('V', 'V1', 't', '0', 72), ('R', 'R1', 't', 'm', 5), ('R', 'R2', 'm', '0', 20),
                       ('R', 'R3', 'm', '0', 8), ('R', 'R4', 't', '0', 12)])
    isc = Is['R3'] + Is['R4']
    assert abs(64.8 / isc - 6) < 1e-9
