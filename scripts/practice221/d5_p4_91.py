r"""Textbook P4.91: max power with a current-controlled voltage source (20 i_beta). Thévenin seen by R_L (p to
ground): V_oc by three meshes, I_sc by three meshes with the 40 ohm shorted out (the dependent source stays on, so
R_Th = V_oc/I_sc), then the matched load on the Thévenin circuit."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'D'
TITLE = 'Max power: a current-controlled source stays on'
SOURCE = 'Textbook P4.91'
CITES = [{"chunk_id": "08f8634b-5721-46a7-80a8-660010b60390", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1}]
PROMPT = (r'Find **(a)** $R_L$ for maximum power transfer and **(b)** the maximum power. '
          r'The source on the left has $+$ at its bottom; $i_\beta$ points right through the $6\,\Omega$.')

O = r'\,\Omega'
V = r'\,\mathrm{V}'
A = r'\,\mathrm{A}'
W = r'\,\mathrm{W}'
V1 = f'V1 0,0 -> 0,4 "$480{V}$"'
R1 = f'R1 0,4 -> 4,4 "$6{O}$" i="$i_\\beta$"'
R2 = f'R2 4,4 -> 4,0 "$40{O}$"'
R3 = f'R3 6,4 -> 8,4 "$8{O}$"'
E1 = 'E1 8,0 -> 8,4 "$20i_\\beta$"'
R4 = f'R4 0,0 -> 4,0 "$4{O}$"'
R5 = f'R5 6,0 -> 8,0 "$2{O}$"'
TOP = '\n'.join(['wire 0,4 -> 0,6', f'R6 0,6 -> 8,6 "$4{O}$"', 'wire 8,6 -> 8,4'])
MID = '\n'.join(['wire 4,4 -> 6,4', 'wire 4,0 -> 6,0'])
LABELS = '\n'.join(['label 0,4 "$a$" left', 'label 4,4 "$p$" above', 'ground 4,0'])
RL = 'RL 5,4 -> 5,0 "$R_L$"'
TERMS = '\n'.join(['terminal 5,4', 'terminal 5,0'])


def j(*parts):
    return '\n'.join(parts)


BASE = j(V1, R1, R3, E1, R4, R5, TOP, MID, LABELS)
GIVEN = j(BASE, R2, RL)
OPEN = j(BASE, R2, TERMS, 'gap 5,4 -> 5,0 v="$V_{oc}$"')
SHORT = j(BASE, TERMS, 'wire 5,4 -> 5,0', '#= text 5.55,2.6 "short"')

M1 = '#= mesh 2,2 "$I_1$" cw r=0.75'
M2 = '#= mesh 6.3,2 "$I_2$" cw r=0.65'
M1s = '#= mesh 2.5,2 "$I_1$" cw r=0.75'
M3 = '#= mesh 5.5,5.15 "$I_3$" cw r=0.42'
MESHES = j(M1, M2, M3)
# + where each mesh current enters
S1 = j('#= sign 0.45,3.6 +', '#= sign 3.55,3.6 -', '#= sign 3.55,3.05 +', '#= sign 3.55,0.95 -',
       '#= sign 3.55,0.35 +', '#= sign 0.45,0.35 -')
S2 = j('#= sign 6.45,3.6 +', '#= sign 7.55,3.6 -', '#= sign 7.55,0.35 +', '#= sign 6.45,0.35 -',
       '#= sign 4.45,0.95 +', '#= sign 4.45,3.05 -')
S3 = j('#= sign 0.45,5.6 +', '#= sign 7.55,5.6 -', '#= sign 7.55,3.6 +', '#= sign 6.45,3.6 -',
       '#= sign 3.55,3.6 +', '#= sign 0.45,3.6 -')
WALK = '#= path 5,4 -> 4,4 -> 4,0 -> 4.85,0'

THEV = j(f'VTH 0,4 -> 0,0 "$48{V}$"', f'RTH 0,4 -> 3,4 "$12{O}$"', 'wire 3,4 -> 5,4',
         f'RL 5,4 -> 5,0 "$R_L=12{O}$"', 'wire 0,0 -> 5,0', 'label 5,4 "$p$" above', 'ground 0,0',
         '#= mesh 2.2,2 "$I$" cw r=0.8')

STEPS = [
    ('The circuit', GIVEN, r'''
$R_L$ sits between $p$ and ground → find the Thévenin circuit it sees.

The $20i_\beta$ source can't be turned off → $R_{Th}=V_{oc}/I_{sc}$.

**Plan**
1. $V_{oc}$ with $R_L$ removed (three meshes).
2. $I_{sc}$ with $p$ shorted to ground.
3. $R_L=R_{Th}$, then $p_{max}$.
'''),
    ('Pull out $R_L$', OPEN, r'''
$R_L$ is gone → $p$ is open.

$V_{oc}$ is the voltage of $p$ above ground: the voltage across the $40\,\Omega$.
'''),
    ('Three meshes', j(OPEN, MESHES), r'''
All clockwise: $I_1$ left, $I_2$ right, $I_3$ top.

The $6\,\Omega$ carries $I_1$ to the right and $I_3$ to the left:

$$
i_\beta=I_1-I_3
$$
'''),
    ('Mesh 1 KVL', j(OPEN, MESHES, S1), r'''
Signs you **enter** by, going with $I_1$:
- $480\,\mathrm{V}$: enter $+$ (bottom) → $+480$
- $6\,\Omega$: $+6(I_1-I_3)$
- $40\,\Omega$: $+40(I_1-I_2)$
- bottom $4\,\Omega$: $+4I_1$

$$
480+6(I_1-I_3)+40(I_1-I_2)+4I_1=0
$$
'''),
    ('Mesh 2 KVL', j(OPEN, MESHES, S2), r'''
Going with $I_2$:
- $8\,\Omega$: $+8(I_2-I_3)$
- $20i_\beta$: enter $-$ (top) → $-20i_\beta=-20(I_1-I_3)$
- $2\,\Omega$: $+2I_2$
- $40\,\Omega$ (up): $+40(I_2-I_1)$

$$
8(I_2-I_3)-20(I_1-I_3)+2I_2+40(I_2-I_1)=0
$$
'''),
    ('Mesh 3 KVL → solve', j(OPEN, MESHES, S3), r'''
Going with $I_3$: top $4\,\Omega$, then back along the $8\,\Omega$ and $6\,\Omega$:

$$
4I_3+8(I_3-I_2)+6(I_3-I_1)=0
$$

All three in standard form:

$$
\begin{aligned}50I_1-40I_2-6I_3&=-480\\-60I_1+50I_2+12I_3&=0\\-6I_1-8I_2+18I_3&=0\end{aligned}
$$

Solve: $I_1=-99.6\,\mathrm{A}$, $I_2=-100.8\,\mathrm{A}$, $I_3=-78\,\mathrm{A}$.
'''),
    ('Walk to $V_{oc}$', j(OPEN, WALK, f'#+ $V_{{Th}}=48{V}$'), r'''
Walk from $p$ down the $40\,\Omega$ to ground. Down it flows $I_1-I_2=1.2\,\mathrm{A}$ → enter $+$:

$$
V_{oc}=40(I_1-I_2)=40(1.2)=48\,\mathrm{V}
$$
'''),
    ('Short $p$ to ground', j(SHORT, M1s, M2, M3, f'#+ $I_{{sc}}=4{A}$'), r'''
The short puts both ends of the $40\,\Omega$ at $0\,\mathrm{V}$ → no current: drop it. Same meshes, no $40$ terms:

$$
\begin{aligned}10I_1-6I_3&=-480\\-20I_1+10I_2+12I_3&=0\\-6I_1-8I_2+18I_3&=0\end{aligned}
$$

Solve: $I_1=-92\,\mathrm{A}$, $I_2=-96\,\mathrm{A}$, $I_3=-73.3\,\mathrm{A}$.

Down the short: $I_{sc}=I_1-I_2=4\,\mathrm{A}$.
'''),
    ('Thévenin circuit, matched load', j(THEV, f'#+ $R_L=R_{{Th}}=12{O}$', f'#+ $p_{{max}}=48{W}$'), r'''
$$
R_{Th}=\frac{V_{oc}}{I_{sc}}=\frac{48}{4}=12\,\Omega
$$

Max power → $R_L=12\,\Omega$. KVL with $I$:

$$
-48+12I+12I=0\;\Rightarrow\;I=2\,\mathrm{A}
$$

$$
p_{max}=I^2R_L=(2)^2(12)=48\,\mathrm{W}
$$
'''),
]


def _mna(extra):
    el = [('V', 'V1', 'l', 'a', 480), ('R', 'R1', 'a', 'p', 6), ('R', 'R3', 'p', 'c', 8),
          ('E', 'E1', 'r', 'c', {'a': 20 / 6, 'p': -20 / 6}, 0), ('R', 'R4', 'l', '0', 4), ('R', 'R5', '0', 'r', 2),
          ('R', 'R6', 'a', 'c', 4)]
    return solve(el + extra)


def checks(check):
    els, _ = check(GIVEN)
    g = '0'
    assert els['V1'][1] == els['R1'][0] == els['R6'][0], els            # a: + of V1 is at the bottom
    assert els['R1'][1] == els['R2'][0] == els['R3'][0] == els['RL'][0], els   # p
    assert els['R2'][1] == els['RL'][1] == els['R4'][1] == els['R5'][0] == g, els
    assert els['E1'][1] == els['R3'][1] == els['R6'][1], els            # c: - of 20 i_beta
    assert els['E1'][0] == els['R5'][1] and els['V1'][0] == els['R4'][0], els
    I1, I2, I3 = F('-99.6'), F('-100.8'), F(-78)
    assert 480 + 6 * (I1 - I3) + 40 * (I1 - I2) + 4 * I1 == 0
    assert 8 * (I2 - I3) - 20 * (I1 - I3) + 2 * I2 + 40 * (I2 - I1) == 0
    assert 4 * I3 + 8 * (I3 - I2) + 6 * (I3 - I1) == 0
    assert 50 * I1 - 40 * I2 - 6 * I3 == -480 and -60 * I1 + 50 * I2 + 12 * I3 == 0 and -6 * I1 - 8 * I2 + 18 * I3 == 0
    assert I1 - I2 == F('1.2') and 40 * (I1 - I2) == 48
    Vo, _, _ = _mna([('R', 'R2', 'p', '0', 40)])
    assert abs(Vo['p'] - 48) < 1e-9 and abs((Vo['a'] - Vo['p']) / 6 - float(I1 - I3)) < 1e-9
    I1, I2, I3 = F(-92), F(-96), F(-220, 3)
    assert 10 * I1 - 6 * I3 == -480 and -20 * I1 + 10 * I2 + 12 * I3 == 0 and -6 * I1 - 8 * I2 + 18 * I3 == 0
    assert I1 - I2 == 4 and round(float(I3), 1) == -73.3
    _, Is, _ = _mna([('R', 'R2', 'p', '0', 40), ('V', 'VS', 'p', '0', 0)])
    assert abs(Is['VS'] - 4) < 1e-9
    assert F(48, 4) == 12 and F(48, 24) == 2 and 2 ** 2 * 12 == 48
    Vl, _, _ = _mna([('R', 'R2', 'p', '0', 40), ('R', 'RL', 'p', '0', 12)])
    assert abs(Vl['p'] ** 2 / 12 - 48) < 1e-9
