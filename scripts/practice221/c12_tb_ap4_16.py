r"""Textbook Assessment Problem 4.16 (p. 122): Norton equivalent at a-b. Short-circuit current by mesh analysis,
R_N with the source off. (Not the course sheet's AP 4.16, which is a different edition's problem.)"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'C'
TITLE = 'Norton: a current divider in disguise'
SOURCE = 'Textbook Assessment Problem 4.16'
CITES = [{"chunk_id": "ccc0fffb-6caf-42ef-aee7-cdb1af9d8c3f", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1}]
PROMPT = 'Find the Norton equivalent circuit with respect to the terminals $a$, $b$.'

K = r'\,\mathrm{k\Omega}'
MA = r'\,\mathrm{mA}'
I1 = f'I1 0,0 -> 0,3 "$75{MA}$"'
R4 = f'R1 2.5,3 -> 2.5,0 "$4{K}$"'
R2 = f'R2 2.5,3 -> 5.5,3 "$2{K}$"'
R3 = f'R3 5.5,3 -> 5.5,0 "$3{K}$"'
LEFT = '\n'.join(['wire 0,3 -> 2.5,3', 'wire 0,0 -> 2.5,0'])
TERMS = '\n'.join(['wire 5.5,3 -> 8,3', 'terminal 8,3 "$a$" right', 'wire 2.5,0 -> 8,0', 'terminal 8,0 "$b$" right'])
SHORT = 'wire 8,3 -> 8,0'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(I1, LEFT, R4, R2, R3, TERMS)
MESHES = j('#= mesh 1.25,1.5 "$I_1$" cw r=0.55', '#= mesh 4,1.5 "$I_2$" cw r=0.7')
SIGNS = j('#= sign 2.85,0.7 +', '#= sign 2.85,2.3 -',
          '#= sign 3.1,2.62 +', '#= sign 4.9,2.62 -')

STEPS = [
    ('The circuit', GIVEN, r'''
Norton equivalent = current source $I_N$ in parallel with $R_N$.

**Plan**
1. $I_N$: short $a$–$b$, find the current in the short.
2. $R_N$: source off, look in from $a$–$b$.
3. Draw $I_N \parallel R_N$.
'''),
    ('Short $a$–$b$', j(GIVEN, SHORT), r'''
A wire from $a$ to $b$. The current in it is $I_N$.

The $3\,\mathrm{k\Omega}$ sits right across the short → $0\,\mathrm{V}$ across it → **no current** in it.
'''),
    ('Mesh currents', j(GIVEN, SHORT, MESHES, f'#+ $I_1=75{MA}$'), r'''
Two windows carry current: $I_1$ (left) and $I_2$ (right, through the short), both clockwise.

The $75\,\mathrm{mA}$ source sits only in mesh 1, pointing the same way (up the left side):

$$
I_1=75\,\mathrm{mA}
$$
'''),
    ('Signs + KVL on mesh 2', j(GIVEN, SHORT, MESHES, SIGNS, f'#+ $I_2=50{MA}$'), r'''
$+$ where $I_2$ **enters** each resistor. The $4\,\mathrm{k\Omega}$ is shared: it carries $I_2-I_1$.
- $4\,\mathrm{k\Omega}$: $+4k(I_2-I_1)$
- $2\,\mathrm{k\Omega}$: $+2kI_2$
- short: no voltage

$$
4k(I_2-75m)+2kI_2=0
$$

$$
6kI_2=(4k)(75m)=300 \;\Rightarrow\; I_2=\frac{300}{6k}=50\,\mathrm{mA}
$$
'''),
    ('$I_N$ = current in the short', j(GIVEN, SHORT, '#= path 6.1,3 -> 8,3 -> 8,0.6 "$50\\,\\mathrm{mA}$"',
                                         f'#+ $I_N=50{MA}$'), r'''
The short is on mesh 2's right side, so its current is $I_2$, flowing $a \to b$:

$$
\boxed{I_N=50\,\mathrm{mA}}
$$

In the Norton circuit, this current comes **out of the top** of the source into $a$.
'''),
    ('$R_N$: source off', j(LEFT, R4, R2, R3, TERMS,
                            '#= path 9.6,1.5 -> 8.3,1.5 thin color=accent', '#= text 9.1,1.95 "$R_N$" color=accent',
                            f'#+ $R_N=2{K}$'), r'''
Current source off = **open** (it disappears).

From $a$: the $3\,\mathrm{k\Omega}$ goes straight to $b$.

The other way: $2\,\mathrm{k\Omega}$ → $4\,\mathrm{k\Omega}$ → $b$, in **series**: $6\,\mathrm{k\Omega}$.

$$
R_N=3k\parallel 6k=\frac{(3k)(6k)}{3k+6k}=\frac{18k^2}{9k}=2\,\mathrm{k\Omega}
$$
'''),
    ('Norton circuit', j(f'IN 4,0 -> 4,3 "$50{MA}$"', f'RN 6,3 -> 6,0 "$2{K}$"',
                         'wire 4,3 -> 8,3', 'terminal 8,3 "$a$" right', 'wire 4,0 -> 8,0', 'terminal 8,0 "$b$" right'),
     r'''
$$
\boxed{I_N=50\,\mathrm{mA}\ (\text{up, into } a)\;\parallel\;R_N=2\,\mathrm{k\Omega}}
$$

**Check** ($a$–$b$ open, mesh 2 now goes through the $3\,\mathrm{k\Omega}$):

$$
4k(I_2-75m)+2kI_2+3kI_2=0 \;\Rightarrow\; I_2=\frac{300}{9k}=33.3\,\mathrm{mA}
$$

$$
V_{oc}=(3k)(33.3m)=100\,\mathrm{V}=I_NR_N=(50m)(2k)
$$

✓ Same circuit.
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    top, bot = els['R1']
    assert els['I1'] == (bot, top), els               # 75 mA pushes up into the top-left node
    a = els['R2'][1]
    assert els['R2'][0] == top and els['R3'] == (a, bot), els
    net = [('I', 'I1', '0', 'p', 0.075), ('R', 'R1', 'p', '0', 4e3), ('R', 'R2', 'p', 'a', 2e3), ('R', 'R3', 'a', '0', 3e3)]
    V, I, _ = solve(net + [('V', 'S', 'a', '0', 0)])
    assert abs(I['S'] - 0.050) < 1e-12                # 50 mA flows a -> b through the short
    I2 = 4e3 * 0.075 / 6e3
    assert abs(I2 - 0.050) < 1e-12 and 4e3 * 0.075 == 300
    V, I, _ = solve(net)
    assert abs(V['a'] - 100) < 1e-9                   # V_oc
    assert abs(3e3 * 6e3 / 9e3 - 2e3) < 1e-9 and abs(V['a'] / 0.050 - 2e3) < 1e-6
    I2o = 300 / 9e3
    assert abs(3e3 * I2o - 100) < 1e-9 and abs(0.050 * 2e3 - 100) < 1e-12
