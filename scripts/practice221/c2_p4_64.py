r"""Textbook P4.64: Norton equivalent at a-b. Short-circuit current by mesh analysis, R_N with the source off."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'C'
TITLE = 'Norton: a shorted internal branch'
SOURCE = 'Textbook P4.64'
CITES = [{"chunk_id": "b0340958-02ef-4cf3-a7c0-cbd0e26f0065", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1}]
PROMPT = 'Find the Norton equivalent at $a$–$b$.'

O = r'\,\Omega'
A = r'\,\mathrm{A}'
I1 = f'I1 0,0 -> 0,4 "$15{A}$"'
R1 = f'R1 3,4 -> 3,0 "$8{O}$"'
R2 = f'R2 3,4 -> 6,4 "$2{O}$"'
R3 = f'R3 6,4 -> 6,0 "$12{O}$"'
R4 = f'R4 3,0 -> 6,0 "$10{O}$"'
TERMS = '\n'.join(['wire 6,4 -> 9,4', 'terminal 9,4 "$a$" right', 'wire 6,0 -> 9,0', 'terminal 9,0 "$b$" right'])
NODES = '\n'.join(['label 3,4 "$p$" above', 'label 3,0 "$q$" below', 'ground 6,0'])
LEFT = '\n'.join(['wire 0,4 -> 3,4', 'wire 0,0 -> 3,0'])


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(I1, 'wire 0,4 -> 3,4', R1, R2, R3, 'wire 6,4 -> 9,4', 'terminal 9,4 "$a$" right', 'wire 0,0 -> 3,0', R4,
          'wire 6,0 -> 9,0', 'terminal 9,0 "$b$" right', 'label 3,4 "$p$" above', 'label 3,0 "$q$" below', 'ground 6,0')
BASE = j(I1, LEFT, R1, R2, R3, R4, TERMS, NODES)
SHORT = 'wire 9,4 -> 9,0'
MESHES = j('#= mesh 1.4,2 "$I_1$" cw r=0.6', '#= mesh 4.5,2 "$I_2$" cw r=0.75')
SIGNS = j('#= sign 3.35,1.25 +', '#= sign 3.35,2.75 -',
          '#= sign 3.6,3.62 +', '#= sign 5.4,3.62 -',
          '#= sign 5.4,0.38 +', '#= sign 3.6,0.38 -')

STEPS = [
    ('The circuit', GIVEN, r'''
Norton equivalent = current source $I_N$ in parallel with $R_N$.

**Plan**
1. $I_N$: short $a$–$b$, find the current in the short.
2. $R_N$: source off, look in from $a$–$b$.
3. Draw $I_N \parallel R_N$.
'''),
    ('Short $a$–$b$', j(BASE, SHORT), r'''
A wire from $a$ to $b$. The current in it is $I_N$.

The $12\,\Omega$ now sits right across the short → $0\,\mathrm{V}$ across it → **no current** in it.
'''),
    ('Mesh currents', j(BASE, SHORT, MESHES, f'#+ $I_1=15{A}$'), r'''
Two windows carry current: $I_1$ (left) and $I_2$ (middle), both clockwise.

The $15\,\mathrm{A}$ source sits only in mesh 1, pointing the same way:

$$
I_1=15\,\mathrm{A}
$$
'''),
    ('Signs + KVL on mesh 2', j(BASE, SHORT, MESHES, SIGNS, f'#+ $I_2=6{A}$'), r'''
$+$ where $I_2$ **enters** each resistor. The $8\,\Omega$ is shared: it carries $I_2-I_1$.
- $8\,\Omega$: $+8(I_2-I_1)$
- $2\,\Omega$: $+2I_2$
- short: no voltage
- $10\,\Omega$: $+10I_2$

$$
8(I_2-15)+2I_2+10I_2=0
$$

$$
20I_2=120 \;\Rightarrow\; I_2=6\,\mathrm{A}
$$
'''),
    ('$I_N$ = current in the short', j(BASE, SHORT, '#= path 6.6,4 -> 9,4 -> 9,0.6 "$6\\,\\mathrm{A}$"',
                                         f'#+ $I_N=6{A}$'), r'''
The short is on mesh 2's right side, so its current is $I_2$, flowing $a \to b$:

$$
\boxed{I_N=6\,\mathrm{A}}
$$

In the Norton circuit, this current comes **out of the top** of the source into $a$.
'''),
    ('$R_N$: source off', j(R1, R2, R3, R4, TERMS, NODES,
                            '#= path 10.6,2 -> 9.3,2 thin color=accent', '#= text 10.1,2.45 "$R_N$" color=accent',
                            f'#+ $R_N=7.5{O}$'), r'''
Current source off = **open** (it disappears).

From $a$: the $12\,\Omega$ goes straight to $b$.

The other way: $2\,\Omega$ → $p$ → $8\,\Omega$ → $q$ → $10\,\Omega$ → $b$, all in **series**: $20\,\Omega$.

$$
R_N=12\parallel 20=\frac{(12)(20)}{12+20}=7.5\,\Omega
$$
'''),
    ('Norton circuit', j(f'IN 4,0 -> 4,4 "$6{A}$"', f'RN 6.5,4 -> 6.5,0 "$7.5{O}$"',
                         'wire 4,4 -> 9,4', 'terminal 9,4 "$a$" right', 'wire 4,0 -> 9,0', 'terminal 9,0 "$b$" right',
                         ), r'''
$$
\boxed{I_N=6\,\mathrm{A}\ (\text{up, into } a)\;\parallel\;R_N=7.5\,\Omega}
$$

**Check** ($a$–$b$ open, mesh 2 now goes through the $12\,\Omega$):

$$
8(I_2-15)+2I_2+12I_2+10I_2=0 \;\Rightarrow\; I_2=3.75\,\mathrm{A}
$$

$$
V_{oc}=12(3.75)=45\,\mathrm{V}=I_NR_N=(6)(7.5)
$$

✓ Same circuit.
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    p, q = els['R1']
    assert els['I1'] == (q, p), els                 # 15 A pushes from q up into p
    a = els['R2'][1]
    assert els['R2'][0] == p and els['R3'][0] == a and els['R4'] == (q, els['R3'][1]), els
    b = els['R3'][1]
    # Short circuit: R3 shorted -> a = b
    net = [('I', 'I1', 'q', 'p', 15), ('R', 'R1', 'p', 'q', 8), ('R', 'R2', 'p', 'a', 2), ('R', 'R3', 'a', '0', 12),
           ('R', 'R4', 'q', '0', 10)]
    V, I, _ = solve(net + [('V', 'S', 'a', '0', 0)])
    assert abs(I['S'] - 6) < 1e-9                    # 6 A flows a -> b through the short
    I2 = 8 * 15 / 20
    assert I2 == 6
    V, I, _ = solve(net)
    assert abs(V['a'] - 45) < 1e-9
    assert abs(12 * 20 / 32 - 7.5) < 1e-12 and abs(V['a'] / 6 - 7.5) < 1e-9
    I2o = 8 * 15 / 32
    assert I2o == 3.75 and 12 * I2o == 45 == 6 * 7.5
