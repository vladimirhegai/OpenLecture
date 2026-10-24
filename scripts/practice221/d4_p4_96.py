r"""Textbook P4.96: superposition when a source is added to a circuit already solved. The old answer (8 V and
10 mA on) is given, so only the new 5 mA source alone is needed; mesh + Ohm, then a full mesh check."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'D'
TITLE = 'Superposition: add a source to a solved circuit'
SOURCE = 'Textbook P4.96'
CITES = [{"chunk_id": "08f8634b-5721-46a7-80a8-660010b60390", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1}]
PROMPT = (r'Before the $5\,\mathrm{mA}$ source is attached between $a$ and $b$, $i_o=3.5\,\mathrm{mA}$. '
          r'**(a)** Use superposition to find $i_o$ after it is attached. **(b)** Check with all three sources on.')

K = r'\,\mathrm{k\Omega}'
MA = r'\,\mathrm{mA}'
V1 = 'V1 0,3 -> 0,0 "$8\\,\\mathrm{V}$"'
R1 = f'R1 3,3 -> 3,0 "$5{K}$"'
R2 = f'R2 3,3 -> 6,3 "$2{K}$"'
R3 = f'R3 6,3 -> 6,0 "$6{K}$" i="$i_o$"'
I1 = f'I1 9,0 -> 9,3 "$10{MA}$" flip'
I2 = '\n'.join(['wire 3,3 -> 3,5', f'I2 6,5 -> 3,5 "$5{MA}$"', 'wire 6,5 -> 6,3'])
WIRES = '\n'.join(['wire 0,3 -> 3,3', 'wire 6,3 -> 9,3', 'wire 0,0 -> 9,0'])
LABELS = '\n'.join(['label 3,3 "$a$" below', 'label 6,3 "$b$" below', 'ground 0,0'])


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(V1, R1, R2, R3, I1, I2, WIRES, LABELS)
ALONE5 = j('wire 0,3 -> 0,0', R1, R2, R3, I2, WIRES, LABELS)

MA_ = '#= mesh 4.15,1.5 "$I_A$" cw r=0.6'
MB = '#= mesh 4.5,4.25 "$I_B$" cw r=0.38'
M0 = '#= mesh 1.5,1.5 "$I_0$" cw r=0.7'
MC = '#= mesh 7.5,1.5 "$I_C$" cw r=0.7'
SA = j('#= sign 3.6,2.55 +', '#= sign 5.4,2.55 -', '#= sign 6.45,2.3 +', '#= sign 6.45,0.7 -')
IO1 = f'#+ $i_o\'=3.5{MA}$'
IO2 = f'#+ $i_o\'\'=-1.25{MA}$'
IO = f'#+ $i_o=2.25{MA}$'

STEPS = [
    ('The circuit', j(GIVEN, IO1), r'''
Before the $5\,\mathrm{mA}$ was attached, $i_o=3.5\,\mathrm{mA}$: that is the $8\,\mathrm{V}$ + $10\,\mathrm{mA}$ part.

Superposition → only the **new source alone** is missing. Then add.
'''),
    ('$5\\,\\mathrm{mA}$ alone', ALONE5, r'''
- $8\,\mathrm{V}$ off → **wire**
- $10\,\mathrm{mA}$ off → **open**

The $5\,\mathrm{k\Omega}$ now has both ends on ground → no current, no KVL term.
'''),
    ('Meshes', j(ALONE5, MA_, MB), r'''
$I_A$: the window with the $2\,\mathrm{k\Omega}$ and $6\,\mathrm{k\Omega}$.

$I_B$: the top window. The $5\,\mathrm{mA}$ points **left**, clockwise goes right:

$$
I_B=-5\,\mathrm{mA}
$$
'''),
    ('KVL for $I_A$', j(ALONE5, MA_, MB, SA, IO2), r'''
Signs you **enter** by, going with $I_A$:

$$
2k(I_A-I_B)+6kI_A=0
$$

$$
8kI_A=2kI_B=2k(-5m)=-10\;\Rightarrow\;I_A=-1.25\,\mathrm{mA}
$$

$I_A$ is the only current down the $6\,\mathrm{k\Omega}$ → $i_o''=-1.25\,\mathrm{mA}$.
'''),
    ('Add', j(GIVEN, IO), r'''
$$
i_o=i_o'+i_o''=3.5+(-1.25)=2.25\,\mathrm{mA}
$$
'''),
    ('Check: all three on', j(GIVEN, M0, MA_, MB, MC), r'''
$I_B=-5\,\mathrm{mA}$; the $10\,\mathrm{mA}$ points up, clockwise goes down → $I_C=-10\,\mathrm{mA}$.

- Mesh $I_0$: $-8+5k(I_0-I_A)=0$
- Mesh $I_A$: $5k(I_A-I_0)+2k(I_A-I_B)+6k(I_A-I_C)=0$

Add them (the $5\,\mathrm{k\Omega}$ terms cancel):

$$
-8+2k(I_A+5m)+6k(I_A+10m)=0\;\Rightarrow\;I_A=-7.75\,\mathrm{mA}
$$

$$
i_o=I_A-I_C=-7.75+10=2.25\,\mathrm{mA}\;✓
$$
'''),
]


def _mna(v, i10, i5):
    return solve([('V', 'V1', 'a', '0', v), ('R', 'R1', 'a', '0', 5e3), ('R', 'R2', 'a', 'b', 2e3),
                  ('R', 'R3', 'b', '0', 6e3), ('I', 'I1', '0', 'b', i10), ('I', 'I2', 'b', 'a', i5)])


def checks(check):
    els, _ = check(GIVEN)
    a, b = els['R2']
    assert els['V1'] == (a, '0') and els['R1'] == (a, '0') and els['R3'] == (b, '0'), els
    assert els['I1'] == ('0', b) and els['I2'] == (b, a), els
    m = F(1, 1000)
    # old answer (given) checks out: I_B = 0
    IA = F(8 - 60, 8000)
    assert IA - (-10 * m) == F('3.5') * m
    IB = -5 * m
    IA = 2000 * IB / 8000
    assert IA == F('-1.25') * m and 2000 * (IA - IB) + 6000 * IA == 0
    assert F('3.5') + F('-1.25') == F('2.25')
    IC = -10 * m
    IA = (8 - 2000 * 5 * m - 6000 * 10 * m) / 8000
    assert IA == F('-7.75') * m and -8 + 2000 * (IA - IB) + 6000 * (IA - IC) == 0 and IA - IC == F('2.25') * m
    for args, io in (((8, 10e-3, 0), 3.5e-3), ((0, 0, 5e-3), -1.25e-3), ((8, 10e-3, 5e-3), 2.25e-3)):
        _, I, _ = _mna(*args)
        assert abs(I['R3'] - io) < 1e-12
