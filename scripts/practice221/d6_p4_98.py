r"""Textbook P4.98: superposition with a dependent current source that stays on in every subproblem. Mesh + Ohm:
the dependent source fixes the top mesh (2.2 i_phi), its control i_phi is recomputed each time."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'D'
TITLE = 'Superposition: the dependent source stays on'
SOURCE = 'Textbook P4.98'
CITES = [{"chunk_id": "08f8634b-5721-46a7-80a8-660010b60390", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1}]
PROMPT = r'Use superposition to find $v_o$.'

K = r'\,\mathrm{k\Omega}'
MA = r'\,\mathrm{mA}'
V = r'\,\mathrm{V}'
V1 = f'V1 0,3 -> 0,0 "$25{V}$"'
R1 = f'R1 4,3 -> 0,3 "$4{K}$" i="$i_\\phi$"'
I1 = f'I1 4,3 -> 4,0 "$5{MA}$"'
R2 = f'R2 8,3 -> 8,0 "$20{K}$" v="$v_o$"'
G1 = '\n'.join(['wire 0,3 -> 0,5', 'G1 0,5 -> 8,5 "$2.2i_\\phi$"', 'wire 8,5 -> 8,3'])
WIRES = '\n'.join(['wire 4,3 -> 8,3', 'wire 0,0 -> 8,0'])
LABELS = '\n'.join(['label 4,3 "$n$" above', 'ground 0,0'])


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(V1, R1, I1, R2, G1, WIRES, LABELS)
ALONE25 = j(V1, R1, R2, G1, WIRES, LABELS)
ALONE5 = j('wire 0,3 -> 0,0', R1, I1, R2, G1, WIRES, LABELS)

MT = '#= mesh 6,4 "$I_T$" cw r=0.45'
ML_BIG = '#= mesh 3,1.5 "$I_L$" cw r=0.75'
ML = '#= mesh 2,1.5 "$I_L$" cw r=0.7'
MR = '#= mesh 6,1.5 "$I_R$" cw r=0.7'
SUPER = '#= region -0.35,-0.3 7.75,2.7 "supermesh"'
S25 = j('#= sign 0.45,2.6 +', '#= sign 3.55,2.6 -', '#= sign 7.55,2.3 +', '#= sign 7.55,0.7 -')
VO1 = f"#+ $v_o'=30{V}$"
VO2 = f"#+ $v_o''=20{V}$"
VO = f'#+ $v_o=50{V}$'

STEPS = [
    ('The circuit', GIVEN, r'''
Two independent sources → two subproblems, then add.

The $2.2i_\phi$ source is **dependent**: it stays on every time, with $i_\phi$ recomputed in each subproblem.
'''),
    ('$25\\,\\mathrm{V}$ alone', j(ALONE25, ML_BIG, MT), r'''
$5\,\mathrm{mA}$ off → **open**. Two meshes left: $I_L$ (bottom) and $I_T$ (top).

$I_T$ is fixed by the dependent source; $i_\phi$ (right to left in the $4\,\mathrm{k\Omega}$) is $I_T-I_L$:

$$
I_T=2.2(I_T-I_L)\;\Rightarrow\;I_T=\tfrac{11}{6}I_L
$$
'''),
    ('KVL for $I_L$', j(ALONE25, ML_BIG, MT, S25, VO1), r'''
Signs you **enter** by, going with $I_L$:

$$
-25+4k(I_L-I_T)+20kI_L=0
$$

$$
24kI_L-\tfrac{22}{3}kI_L=25\;\Rightarrow\;I_L=1.5\,\mathrm{mA}
$$

$$
v_o'=20k\,I_L=(20k)(1.5m)=30\,\mathrm{V}
$$
'''),
    ('$5\\,\\mathrm{mA}$ alone', j(ALONE5, ML, MR, MT, SUPER), r'''
$25\,\mathrm{V}$ off → **wire**. Three meshes; still $I_T=\tfrac{11}{6}I_L$.

The $5\,\mathrm{mA}$ sits between $I_L$ and $I_R$ → **supermesh**. It points down, $I_L$ goes down it:

$$
I_L-I_R=5\,\mathrm{mA}
$$
'''),
    ('Supermesh KVL', j(ALONE5, ML, MR, MT, SUPER, VO2), r'''
Walk around the outside of the supermesh:

$$
4k(I_L-I_T)+20kI_R=0
$$

$$
4k\left(-\tfrac56 I_L\right)+20kI_R=0\;\Rightarrow\;I_L=6I_R
$$

$$
6I_R-I_R=5m\;\Rightarrow\;I_R=1\,\mathrm{mA}
$$

$$
v_o''=(20k)(1m)=20\,\mathrm{V}
$$
'''),
    ('Add', j(GIVEN, VO), r'''
$$
v_o=v_o'+v_o''=30+20=50\,\mathrm{V}
$$

Adding works for voltages and currents only, never for power.
'''),
]


def _mna(v, i):
    return solve([('V', 'V1', 's', '0', v), ('R', 'R1', 'n', 's', 4e3), ('I', 'I1', 'n', '0', i),
                  ('R', 'R2', 'n', '0', 20e3), ('G', 'G1', 's', 'n', {'n': 2.2 / 4e3, 's': -2.2 / 4e3})])


def checks(check):
    els, _ = check(GIVEN)
    s, n = els['V1'][0], els['R1'][0]
    assert els['V1'][1] == '0' and els['R1'] == (n, s) and els['I1'] == (n, '0') and els['R2'] == (n, '0'), els
    assert els['G1'] == (s, n), els
    k, m = 1000, F(1, 1000)
    # 25 V alone
    IL = F(3, 2) * m
    IT = F(11, 6) * IL
    assert IT == F(22, 10) * (IT - IL) and -25 + 4 * k * (IL - IT) + 20 * k * IL == 0 and 20 * k * IL == 30
    # 5 mA alone
    IR = 1 * m
    IL = 6 * IR
    IT = F(11, 6) * IL
    assert IL - IR == 5 * m and 4 * k * (IL - IT) + 20 * k * IR == 0 and IT == F(22, 10) * (IT - IL)
    assert 20 * k * IR == 20 and 30 + 20 == 50
    for args, vo in (((25, 0), 30), ((0, 5e-3), 20), ((25, 5e-3), 50)):
        Vn, _, _ = _mna(*args)
        assert abs(Vn['n'] - vo) < 1e-9
