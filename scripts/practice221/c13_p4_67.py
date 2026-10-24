r"""Textbook P4.67: Norton at a-b. Short a-b, mesh + supermesh -> I_N comes out negative (-1 mA), so the Norton
source arrow flips. R_N = 15k || 5k with the sources off."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'C'
TITLE = 'Norton: a negative Norton current'
SOURCE = 'Textbook P4.67'
CITES = [{"chunk_id": "b0340958-02ef-4cf3-a7c0-cbd0e26f0065", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1}]
PROMPT = 'Find the Norton equivalent at $a$–$b$.'

K = r'\,\mathrm{k\Omega}'
MA = r'\,\mathrm{mA}'
I1 = f'I1 0,0 -> 0,3 "$10{MA}$"'
R1 = f'R1 2,3 -> 2,0 "$10{K}$"'
V1 = r'V1 4,3 -> 4,0 "$30\,\mathrm{V}$"'
R2 = f'R2 4,3 -> 7,3 "$15{K}$"'
I2 = f'I2 7,3 -> 7,0 "$3{MA}$"'
R3 = f'R3 9,3 -> 9,0 "$5{K}$" flip'
LEFT = 'wire 0,3 -> 4,3'
FRAME = '\n'.join(['wire 7,3 -> 12,3', 'terminal 12,3 "$a$" right', 'terminal 12,0 "$b$" right', 'wire 0,0 -> 12,0',
                   'ground 0,0'])


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(I1, R1, V1, LEFT, R2, I2, R3, FRAME)
SHORT = j(GIVEN, 'wire 12,3 -> 12,0')
MESHES = j('#= mesh 5.15,1.5 "$I_A$" cw r=0.55', '#= mesh 8,1.5 "$I_B$" cw r=0.6', '#= mesh 10.6,1.5 "$I_C$" cw r=0.7')
SIGNS_C = j('#= sign 9.38,0.7 +', '#= sign 9.38,2.3 -')
SIGNS_S = j('#= sign 4.6,2.62 +', '#= sign 6.4,2.62 -', '#= sign 8.62,2.3 +', '#= sign 8.62,0.7 -')
WALK = '#= path 4,0.15 -> 4,3 -> 9,3 -> 9,0 -> 4.2,0'
OFF = j('wire 0,3 -> 4,3', 'wire 4,3 -> 4,0', R1, R2, R3, FRAME, 'wire 7,3 -> 7,2.2', 'wire 7,0 -> 7,0.8')

STEPS = [
    ('The circuit', GIVEN, r'''
Norton equivalent = current source $I_N$ in parallel with $R_N$.

**Plan**
1. $I_N$: short $a$–$b$, find the current in the short ($a \to b$).
2. $R_N$: sources off, look in from $a$–$b$.
3. Draw $I_N \parallel R_N$.
'''),
    ('Short $a$–$b$', j(SHORT, '#= text 12.75,1.5 "short"'), r'''
The $5\,\mathrm{k\Omega}$ now sits right across the short → $0\,\mathrm{V}$ → **no current** in it.

Left of the $30\,\mathrm{V}$: the ideal source alone fixes that voltage, so the $10\,\mathrm{mA}$ and $10\,\mathrm{k\Omega}$ change nothing on the right. Ignore them.
'''),
    ('Mesh currents', j(SHORT, MESHES), r'''
Three windows right of the $30\,\mathrm{V}$, all clockwise: $I_A$, $I_B$, $I_C$ (the short's window).

The $3\,\mathrm{mA}$ source is shared by $I_A$ and $I_B$ → **supermesh**.

Constraint (arrow points down; $I_A$ goes down there, $I_B$ goes up):

$$
I_A-I_B=3m
$$
'''),
    ('Mesh $C$', j(SHORT, MESHES, SIGNS_C), r'''
KVL around $I_C$ (sign you **enter** by):
- $5\,\mathrm{k\Omega}$: enter $+$ → $+5k(I_C-I_B)$
- short: no voltage

$$
5k(I_C-I_B)=0 \;\Rightarrow\; I_C=I_B
$$
'''),
    ('Supermesh', j(SHORT, MESHES, SIGNS_S, WALK, f'#+ $I_A=2{MA}$'), r'''
Walk around $I_A$ + $I_B$ (skip the current source):
- $30\,\mathrm{V}$: enter $-$ → $-30$
- $15\,\mathrm{k\Omega}$: enter $+$ → $+15kI_A$
- $5\,\mathrm{k\Omega}$: enter $+$ → $+5k(I_B-I_C)=0$

$$
-30+15kI_A=0 \;\Rightarrow\; I_A=\frac{30}{15k}=2\,\mathrm{mA}
$$
'''),
    ('$I_N$ comes out negative', j(SHORT, MESHES, '#= path 9.6,3 -> 12,3 -> 12,0.6 "$-1\\,\\mathrm{mA}$"',
                                    f'#+ $I_N=-1{MA}$'), r'''
$$
I_B=I_A-3m=2m-3m=-1\,\mathrm{mA}
$$

The short is $I_C$'s right side ($a \to b$), and $I_C=I_B$:

$$
\boxed{I_N=i_{sc}=-1\,\mathrm{mA}}
$$

Negative: $1\,\mathrm{mA}$ really flows **up** the short, $b \to a$.
'''),
    ('$R_N$: sources off', j(OFF, '#= path 13.6,1.5 -> 12.3,1.5 thin color=accent',
                             '#= text 13.1,1.95 "$R_N$" color=accent', f'#+ $R_N=3.75{K}$'), r'''
$30\,\mathrm{V}$ → **wire**: it shorts the $10\,\mathrm{k\Omega}$ and the left side, so the $15\,\mathrm{k\Omega}$'s left end is on the bottom wire.

$10\,\mathrm{mA}$ and $3\,\mathrm{mA}$ → **open**.

From $a$: $5\,\mathrm{k\Omega}$ to $b$, and $15\,\mathrm{k\Omega}$ to $b$ → **parallel**:

$$
R_N=\frac{(15k)(5k)}{15k+5k}=\frac{75k^2}{20k}=3.75\,\mathrm{k\Omega}
$$
'''),
    ('Norton circuit (arrow flipped)', j(f'IN 6,3 -> 6,0 "$1{MA}$"', f'RN 8.5,3 -> 8.5,0 "$3.75{K}$"',
                                         'wire 6,3 -> 12,3', 'terminal 12,3 "$a$" right', 'wire 6,0 -> 12,0',
                                         'terminal 12,0 "$b$" right'), r'''
$I_N=-1\,\mathrm{mA}$ "toward $a$" is the same as $1\,\mathrm{mA}$ **toward $b$**, so the arrow points **down**.

$$
\boxed{1\,\mathrm{mA}\ (\text{down, toward } b)\;\parallel\;R_N=3.75\,\mathrm{k\Omega}}
$$

**Check** ($a$–$b$ open; supermesh with the $5\,\mathrm{k\Omega}$ term $5kI_B$):

$$
-30+15kI_A+5k(I_A-3m)=0 \;\Rightarrow\; I_A=2.25\,\mathrm{mA},\; I_B=-0.75\,\mathrm{mA}
$$

$$
V_{oc}=5kI_B=-3.75\,\mathrm{V}=I_NR_N=(-1m)(3.75k)\;✓
$$
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    top, a = els['V1'][0], els['R2'][1]
    assert els['V1'][1] == '0' and els['R1'] == (top, '0') and els['I1'] == ('0', top), els
    assert els['R2'] == (top, a) and els['I2'] == (a, '0') and els['R3'] == (a, '0'), els
    net = [('I', 'I1', '0', 't', 0.010), ('R', 'R1', 't', '0', 10e3), ('V', 'V1', 't', '0', 30),
           ('R', 'R2', 't', 'a', 15e3), ('I', 'I2', 'a', '0', 0.003), ('R', 'R3', 'a', '0', 5e3)]
    # Short a-b: current a -> b through the short
    _, I, _ = solve(net + [('V', 'S', 'a', '0', 0)])
    assert abs(I['S'] - (-1e-3)) < 1e-12
    # Mesh equations as written (short)
    IA = 30 / 15e3
    IB = IA - 3e-3
    IC = IB
    assert abs(IA - 2e-3) < 1e-15 and abs(IB + 1e-3) < 1e-15
    assert abs(-30 + 15e3 * IA + 5e3 * (IB - IC)) < 1e-12 and abs(IC - I['S']) < 1e-12
    # Open circuit check
    V, _, _ = solve(net)
    IAo = (30 + 15) / 20e3
    IBo = IAo - 3e-3
    assert abs(IAo - 2.25e-3) < 1e-15 and abs(IBo + 0.75e-3) < 1e-15
    assert abs(-30 + 15e3 * IAo + 5e3 * IBo) < 1e-12
    assert abs(V['a'] - 5e3 * IBo) < 1e-9 and abs(V['a'] + 3.75) < 1e-9
    # R_N, and V_oc = I_N R_N
    RN = 15e3 * 5e3 / 20e3
    assert RN == 3750 and abs(-1e-3 * RN - V['a']) < 1e-9
    # Sources off (30 V shorted, current sources open), 1 A test source into a: V_a = R_N
    Vt, _, _ = solve([('R', 'R1', 't', '0', 10e3), ('V', 'V1', 't', '0', 0), ('R', 'R2', 't', 'a', 15e3),
                      ('R', 'R3', 'a', '0', 5e3), ('I', 'T', '0', 'a', 1)])
    assert abs(Vt['a'] - RN) < 1e-6
