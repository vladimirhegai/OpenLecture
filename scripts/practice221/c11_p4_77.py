r"""Textbook P4.77, as a Norton problem: I_N = i_sc (supermesh with a-b shorted), R_N = V_oc / i_sc, and R_N again
with the sources off (series/parallel); both agree. Ends on the Norton circuit."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'C'
TITLE = r'Norton two ways: $i_{sc}$ vs. sources off'
SOURCE = 'Textbook P4.77'
CITES = [{"chunk_id": "11bd02ab-ca60-4fbc-9f85-243a3e08a576", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1}]
PROMPT = (r'**(a)** Find the Norton equivalent at $a$–$b$ from the short-circuit current and the open-circuit voltage. '
          r'**(b)** Find $R_N$ by removing the sources and compare.')

O = r'\,\Omega'
V1 = 'V1 0,3 -> 0,0 "$17.4\\,\\mathrm{V}$"'
I1 = 'I1 4,3 -> 8,3 "$100\\,\\mathrm{mA}$"'
REST = '\n'.join([
    f'R1 0,3 -> 4,3 "$40{O}$"',
    f'R2 4,3 -> 4,0 "$15{O}$"',
    'wire 0,3 -> 0,5',
    f'R3 0,5 -> 8,5 "$26{O}$"',
    'wire 8,5 -> 8,3',
    f'R4 8,3 -> 8,0 "$10{O}$"',
    'wire 0,0 -> 4,0',
    f'R5 4,0 -> 8,0 "$4{O}$"',
    'wire 8,3 -> 10,3',
    'wire 8,0 -> 10,0',
    'terminal 10,3 "$a$" right',
    'terminal 10,0 "$b$" right',
    'ground 0,0',
])


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(V1, I1, REST, 'label 4,3 "$p$" above')
BASE = j(V1, I1, REST)
SHORT = j(BASE, 'wire 10,3 -> 10,0')
MESH = j('#= mesh 2,1.5 "$I_1$" cw r=0.8', '#= mesh 6,1.5 "$I_2$" cw r=0.8', '#= mesh 4,4 "$I_3$" cw r=0.6')
# + where each mesh current enters
SIGNS1 = j('#= sign 1.2,2.62 +', '#= sign 2.8,2.62 -', '#= sign 3.62,2.3 +', '#= sign 3.62,0.7 -')
SUPER_SC = '#= path 0,3 -> 0,5 -> 8,5 -> 8,3 -> 10,3 -> 10,0 -> 4,0 -> 4,3 -> 0.15,3'  # through the short, not the 10 ohm
SIGNS_SC = j('#= sign 3.2,4.62 +', '#= sign 4.8,4.62 -',
             '#= sign 6.8,0.38 +', '#= sign 5.2,0.38 -', '#= sign 4.38,0.7 +', '#= sign 4.38,2.3 -',
             '#= sign 2.8,3.38 +', '#= sign 1.2,3.38 -')
OFF = j('wire 0,3 -> 0,0', REST)

STEPS = [
    ('The circuit', GIVEN, r'''
Norton equivalent = current source $I_N$ in parallel with $R_N$. $b$ is **not** ground here.

**Plan**
1. (a) Short $a$–$b$ → $I_N=i_{sc}$. Then $V_{oc}$ → $R_N=V_{oc}/i_{sc}$.
2. (b) Sources off → $R_N$ again. Both must agree.
'''),
    ('Short $a$–$b$ + mesh currents', j(SHORT, MESH, '#= text 10.75,1.5 "short"'), r'''
The short also sits across the $10\,\Omega$ (same two nodes) → $0\,\mathrm{V}$ → it carries **nothing**. $I_2$ goes through the short.

Three windows, all clockwise: $I_1$ (left), $I_2$ (right), $I_3$ (top).

The $100\,\mathrm{mA}$ source sits between $I_2$ and $I_3$ → **supermesh**. Constraint (arrow points right; $I_2$ goes right there, $I_3$ goes left):

$$
I_2-I_3=0.1
$$
'''),
    ('Mesh 1', j(SHORT, MESH, SIGNS1), r'''
KVL around $I_1$ (sign you **enter** by):
- $17.4\,\mathrm{V}$: enter $-$ → $-17.4$
- $40\,\Omega$: enter $+$ → $+40(I_1-I_3)$
- $15\,\Omega$: enter $+$ → $+15(I_1-I_2)$

$$
55I_1-15I_2-40I_3=17.4
$$
'''),
    ('Supermesh', j(SHORT, MESH, SUPER_SC, SIGNS_SC), r'''
Walk the outside of $I_2$ + $I_3$ (skip the current source; the short adds nothing):
- $26\,\Omega$: $+26I_3$
- $4\,\Omega$: $+4I_2$
- $15\,\Omega$ (shared with $I_1$): $+15(I_2-I_1)$
- $40\,\Omega$ (shared with $I_1$): $+40(I_3-I_1)$

$$
-55I_1+19I_2+66I_3=0
$$
'''),
    ('Solve → $I_N$', j(SHORT, MESH, '#= path 8.6,3 -> 10,3 -> 10,0.6 "$\\tfrac23\\,\\mathrm{A}$"',
                        r'#+ $I_N=\tfrac23\,\mathrm{A}$'), r'''
Add the two KVLs: $I_1$ cancels.

$$
4I_2+26I_3=17.4
$$

With $I_2=I_3+0.1$:

$$
30I_3+0.4=17.4 \;\Rightarrow\; I_3=\tfrac{17}{30}\,\mathrm{A}
$$

$$
\boxed{I_N=i_{sc}=I_2=\tfrac{17}{30}+0.1=\tfrac23\,\mathrm{A}}
$$

Positive: it flows $a \to b$ through the short.
'''),
    ('Open $a$–$b$ → $V_{oc}$', j(BASE, '#= sign 7.62,2.3 +', '#= sign 7.62,0.7 -',
                                  '#= text 9,1.5 "$5\\,\\mathrm{V}$" color=pink', r'#+ $R_N=7.5\,\Omega$'), r'''
Short removed: the $10\,\Omega$ is back, so the supermesh walk gains $+10I_2$:

$$
14I_2+26I_3=17.4 \;\Rightarrow\; I_3=0.4\,\mathrm{A},\; I_2=0.5\,\mathrm{A}
$$

$a$–$b$ is right across the $10\,\Omega$ ($I_2$ enters at $a$):

$$
V_{oc}=10I_2=5\,\mathrm{V}
$$

$$
R_N=\frac{V_{oc}}{i_{sc}}=\frac{5}{2/3}=7.5\,\Omega
$$
'''),
    ('(b) Sources off', OFF, r'''
$17.4\,\mathrm{V}$ → **wire**. $100\,\mathrm{mA}$ → **open**.

The $40\,\Omega$ and $15\,\Omega$ now hang off a dead end ($p$): no current, ignore them.

From $a$: $26\,\Omega$ to the bottom wire, then $4\,\Omega$ to $b$ → $26+4=30\,\Omega$, in parallel with the $10\,\Omega$:

$$
R_N=\frac{(10)(30)}{10+30}=7.5\,\Omega \;✓
$$
'''),
    ('Norton circuit', j('IN 4,0 -> 4,3 "$\\tfrac23\\,\\mathrm{A}$"', f'RN 7,3 -> 7,0 "$7.5{O}$"', 'wire 4,3 -> 10,3',
                         'wire 4,0 -> 10,0', 'terminal 10,3 "$a$" right', 'terminal 10,0 "$b$" right'), r'''
$$
\boxed{I_N=\tfrac23\,\mathrm{A}\ (\text{up, into } a)\;\parallel\;R_N=7.5\,\Omega}
$$

Both ways give the same $R_N$.

**Check:** $I_NR_N=(\tfrac23)(7.5)=5\,\mathrm{V}=V_{oc}$ ✓
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    top, p, a, b = els['V1'][0], els['R1'][1], els['R4'][0], els['R4'][1]
    assert els['V1'][1] == '0' and els['R1'][0] == top and els['R3'] == (top, a), els
    assert els['R2'] == (p, '0') and els['I1'] == (p, a) and els['R5'] == ('0', b), els
    # Open circuit (nodal solve with mna)
    net = [('V', 'V1', 't', '0', 17.4), ('R', 'R1', 't', 'p', 40), ('R', 'R2', 'p', '0', 15),
           ('I', 'I1', 'p', 'a', 0.1), ('R', 'R3', 't', 'a', 26), ('R', 'R4', 'a', 'b', 10), ('R', 'R5', '0', 'b', 4)]
    V, I, _ = solve(net)
    assert abs(V['a'] - V['b'] - 5) < 1e-9
    # Mesh equations as written (open circuit)
    I3 = 0.4
    I2 = I3 + 0.1
    I1 = (17.4 + 15 * I2 + 40 * I3) / 55
    assert abs(-17.4 + 40 * (I1 - I3) + 15 * (I1 - I2)) < 1e-12
    assert abs(26 * I3 + 10 * I2 + 4 * I2 + 15 * (I2 - I1) + 40 * (I3 - I1)) < 1e-12
    assert abs(14 * I2 + 26 * I3 - 17.4) < 1e-12 and abs(40 * I3 + 1.4 - 17.4) < 1e-12
    assert abs(I['R4'] - I2) < 1e-9 and abs(10 * I2 - 5) < 1e-12
    # Short circuit: R4 shorted
    Vs, Is, _ = solve([e for e in net if e[1] != 'R4'] + [('V', 'VS', 'a', 'b', 0)])
    isc = Is['VS']
    assert abs(isc - 2 / 3) < 1e-9
    I3s = 17 / 30
    I2s = I3s + 0.1
    I1s = (17.4 + 15 * I2s + 40 * I3s) / 55
    assert abs(26 * I3s + 4 * I2s + 15 * (I2s - I1s) + 40 * (I3s - I1s)) < 1e-12
    assert abs(4 * I2s + 26 * I3s - 17.4) < 1e-12 and abs(30 * I3s + 0.4 - 17.4) < 1e-12
    assert abs(I2s - isc) < 1e-9 and abs(5 / (2 / 3) - 7.5) < 1e-12
    assert abs(-55 * I1s + 19 * I2s + 66 * I3s) < 1e-12 and abs(55 * I1s - 15 * I2s - 40 * I3s - 17.4) < 1e-12
    assert abs((2 / 3) * 7.5 - 5) < 1e-12
    # Sources off
    assert 10 * 30 / (10 + 30) == 7.5 and 26 + 4 == 30
