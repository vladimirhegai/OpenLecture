r"""Textbook Assessment Problem 4.19 (p. 126): Norton equivalent of a circuit with a current-controlled current source.
I_N from the shorted terminals, V_oc with them open (mesh analysis both times), R_N = V_oc / I_N because the
dependent source cannot be turned off."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'C'
TITLE = 'Norton: a dependent source stays on'
SOURCE = 'Textbook Assessment Problem 4.19'
CITES = [{"chunk_id": "5e45142a-3485-4639-a8b3-f6a6424bd0be", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1}]
PROMPT = 'Find the Norton equivalent circuit with respect to the terminals $a$, $b$.'

K = r'\,\mathrm{k\Omega}'
MA = r'\,\mathrm{mA}'
V = r'\,\mathrm{V}'
VS = f'V1 0,3 -> 0,0 "$280{V}$"'
RA = f'R1 0,3 -> 3,3 "$2{K}$" i="$i_\\Delta$"'
RB = f'R2 3,3 -> 3,0 "$2{K}$"'
RC = f'R3 3,3 -> 6,3 "$2{K}$"'
RL = f'R4 6,3 -> 6,0 "$5.6{K}$"'
DEP = '\n'.join(['wire 3,3 -> 3,5.2', 'F1 3,5.2 -> 6,5.2 "$0.2i_\\Delta$"', 'wire 6,5.2 -> 6,3'])
TERMS = '\n'.join(['wire 6,3 -> 8,3', 'terminal 8,3 "$a$" right', 'wire 0,0 -> 8,0', 'terminal 8,0 "$b$" right'])
SHORT = 'wire 8,3 -> 8,0'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(VS, RA, RB, RC, DEP, RL, TERMS)
MESHES = j('#= mesh 1.5,1.5 "$I_1$" cw r=0.6', '#= mesh 4.1,1.5 "$I_2$" cw r=0.5', '#= mesh 4.5,4.35 "$I_3$" cw r=0.4')
SIGNS1 = j('#= sign 0.6,2.62 +', '#= sign 2.4,2.62 -', '#= sign 2.65,2.3 +', '#= sign 2.65,0.7 -')
SIGNS2 = j('#= sign 3.35,0.7 +', '#= sign 3.35,2.3 -', '#= sign 3.6,2.62 +', '#= sign 5.4,2.62 -')
SIGNS2_OPEN = j(SIGNS2, '#= sign 5.65,2.3 +', '#= sign 5.65,0.7 -')

STEPS = [
    ('The circuit', GIVEN, r'''
Norton equivalent = current source $I_N$ in parallel with $R_N$.

The $0.2i_\Delta$ source is **dependent**: it can't be turned off. So:

**Plan**
1. $I_N$: short $a$–$b$, find the current in the short.
2. $V_{oc}$: terminals open.
3. $R_N=V_{oc}/I_N$, then draw $I_N \parallel R_N$.
'''),
    ('Short $a$–$b$', j(GIVEN, SHORT), r'''
A wire from $a$ to $b$. The current in it is $I_N$.

The $5.6\,\mathrm{k\Omega}$ sits right across the short → **no current** in it.
'''),
    ('Mesh currents', j(GIVEN, SHORT, MESHES), r'''
Three windows, all clockwise: $I_1$ (left), $I_2$ (right, through the short), $I_3$ (top, holds the dependent source).

$i_\Delta$ is the current in the left $2\,\mathrm{k\Omega}$, the same way as $I_1$:

$$
i_\Delta=I_1
$$

The $0.2i_\Delta$ source sits only in mesh 3, pointing the same way (right along the top):

$$
I_3=0.2i_\Delta=0.2I_1
$$
'''),
    ('KVL on mesh 1', j(GIVEN, SHORT, MESHES, SIGNS1), r'''
$+$ where $I_1$ **enters** each element:
- $280\,\mathrm{V}$: enter $-$ → $-280$
- top $2\,\mathrm{k\Omega}$: $+2kI_1$
- middle $2\,\mathrm{k\Omega}$ (shared): $+2k(I_1-I_2)$

$$
-280+2kI_1+2k(I_1-I_2)=0
$$

$$
4kI_1-2kI_2=280
$$
'''),
    ('KVL on mesh 2', j(GIVEN, SHORT, MESHES, SIGNS2), r'''
$+$ where $I_2$ **enters** each element:
- middle $2\,\mathrm{k\Omega}$ (shared with mesh 1): $+2k(I_2-I_1)$
- right $2\,\mathrm{k\Omega}$ (shared with mesh 3): $+2k(I_2-I_3)$
- short: no voltage

$$
2k(I_2-I_1)+2k(I_2-0.2I_1)=0
$$

$$
4kI_2=2.4kI_1 \;\Rightarrow\; I_2=0.6I_1
$$
'''),
    ('Solve → $I_N$', j(GIVEN, SHORT, MESHES, '#= path 6.6,3 -> 8,3 -> 8,0.6 "$60\\,\\mathrm{mA}$"',
                        f'#+ $I_N=60{MA}$'), r'''
Put $I_2=0.6I_1$ into mesh 1:

$$
4kI_1-1.2kI_1=280 \;\Rightarrow\; I_1=\frac{280}{2.8k}=100\,\mathrm{mA}
$$

$$
I_2=0.6(100m)=60\,\mathrm{mA}
$$

The short carries $I_2$, flowing $a\to b$:

$$
\boxed{I_N=60\,\mathrm{mA}}
$$
'''),
    ('Open $a$–$b$: $V_{oc}$', j(GIVEN, MESHES, SIGNS2_OPEN, f'#+ $V_{{oc}}=112{V}$'), r'''
Short removed: mesh 2 now goes down through the $5.6\,\mathrm{k\Omega}$ (enter $+$ → $+5.6kI_2$).

Mesh 2:

$$
2k(I_2-I_1)+2k(I_2-0.2I_1)+5.6kI_2=0 \;\Rightarrow\; I_2=0.25I_1
$$

Mesh 1 is unchanged:

$$
4kI_1-2k(0.25I_1)=280 \;\Rightarrow\; I_1=80\,\mathrm{mA},\quad I_2=20\,\mathrm{mA}
$$

Ohm's law on the $5.6\,\mathrm{k\Omega}$:

$$
V_{oc}=(20m)(5.6k)=112\,\mathrm{V}
$$
'''),
    ('Norton circuit', j(f'IN 4,0 -> 4,3 "$60{MA}$"', f'RN 6,3 -> 6,0 "$1.867{K}$"',
                         'wire 4,3 -> 8,3', 'terminal 8,3 "$a$" right', 'wire 4,0 -> 8,0', 'terminal 8,0 "$b$" right',
                         r'#+ $R_N=1866.67\,\Omega$'), r'''
$$
R_N=\frac{V_{oc}}{I_N}=\frac{112}{60m}=1866.67\,\Omega
$$

$$
\boxed{I_N=60\,\mathrm{mA}\ (\text{up, into } a)\;\parallel\;R_N=1866.67\,\Omega}
$$
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    p = els['R1'][0]
    x = els['R1'][1]
    assert els['V1'] == (p, els['R2'][1]), els        # + at the top-left node, - on the bottom wire
    gnd = els['R2'][1]
    assert els['R2'][0] == x and els['R3'][0] == x, els
    a = els['R3'][1]
    assert els['F1'] == (x, a) and els['R4'] == (a, gnd), els
    # 0.2 i_delta pushes x -> a; i_delta = (Vp - Vx)/2k
    g = 0.2 / 2e3
    net = [('V', 'V1', 'p', '0', 280), ('R', 'R1', 'p', 'x', 2e3), ('R', 'R2', 'x', '0', 2e3),
           ('R', 'R3', 'x', 'a', 2e3), ('G', 'F1', 'x', 'a', {'p': g, 'x': -g}), ('R', 'R4', 'a', '0', 5.6e3)]
    Vs, Is, _ = solve(net + [('V', 'S', 'a', '0', 0)])
    assert abs(Is['S'] - 0.060) < 1e-12               # I_N = 60 mA, a -> b in the short
    assert abs((Vs['p'] - Vs['x']) / 2e3 - 0.100) < 1e-12
    Vo, Io, _ = solve(net)
    assert abs(Vo['a'] - 112) < 1e-9
    assert abs(Vo['a'] / Is['S'] - 1866.6666666) < 1e-3
    # hand algebra in the notes
    I1 = 280 / 2.8e3
    assert abs(I1 - 0.1) < 1e-15 and abs(0.6 * I1 - 0.06) < 1e-15 and abs(4e3 - 2e3 * 0.6 - 2.8e3) < 1e-9
    assert abs(4e3 * 0.6 - 2.4e3) < 1e-9                       # 2k + 2k(0.2) = 2.4k
    assert abs(2.4e3 / 9.6e3 - 0.25) < 1e-15                   # 4k + 5.6k = 9.6k
    I1o = 280 / (4e3 - 2e3 * 0.25)
    assert abs(I1o - 0.08) < 1e-15 and abs(0.25 * I1o - 0.02) < 1e-15 and abs(0.02 * 5.6e3 - 112) < 1e-9
    assert abs(112 / 0.06 - 1866.67) < 0.01
