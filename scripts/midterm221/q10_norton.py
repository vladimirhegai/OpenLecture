r"""Midterm Questions Q10: Norton at a-b, then two loads by current divider.
Short a-b -> three meshes; the 2 A source sits between meshes 2 and 3 -> supermesh (I_3 - I_2 = 2).
I_1 = 4.8 A, I_2 = 4 A, I_N = I_3 = 6 A. R_N = (10 || 15) + 3 = 9 Ω. Loads: 9 Ω -> 3 A, 3 Ω -> 4.5 A.
Inspired by Textbook P4.64 / P4.67."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

TOPIC = 'Norton (independent sources only)'
MARKS = 10
TITLE = 'Norton: one equivalent, two loads'
SOURCE = 'Textbook P4.64 and P4.67'
PROMPT = (r'**(a)** Find the Norton equivalent of the circuit at the terminals $a$–$b$. '
          r'**(b)** A load resistor $R_L$ is connected from $a$ to $b$. Use your Norton circuit to find the current '
          r'$i_L$ in the load for $R_L=9\,\Omega$ and for $R_L=3\,\Omega$.')

O = r'\,\Omega'
V = r'\,\mathrm{V}'
A = r'\,\mathrm{A}'

V1 = f'V1 0,3 -> 0,0 "$60{V}$"'
R1 = f'R1 0,3 -> 3,3 "$10{O}$"'
R2 = f'R2 3,3 -> 3,0 "$15{O}$"'
R3 = f'R3 3,3 -> 6,3 "$3{O}$"'
I1 = f'I1 6,0 -> 6,3 "$2{A}$"'
TERMS = '\n'.join(['wire 6,3 -> 9,3', 'terminal 9,3 "$a$" right', 'wire 0,0 -> 9,0', 'terminal 9,0 "$b$" right',
                   'ground 0,0'])
NODES = 'label 3,3 "$m$" above\nlabel 6,3 "$n$" above'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(V1, R1, R2, R3, I1, TERMS, NODES)
SHORT = j(GIVEN, 'wire 9,3 -> 9,0', '#= text 9.8,1.5 "short"')
MESHES = j('#= mesh 1.3,1.4 "$I_1$" cw r=0.55', '#= mesh 4.6,1.4 "$I_2$" cw r=0.55', '#= mesh 7.5,1.5 "$I_3$" cw r=0.7')
CONSTRAINT = '#= text 6,-0.8 "$I_3-I_2=2$" color=purple'
SIGNS1 = j('#= sign 1.0,2.6 +', '#= sign 2.1,2.6 -',          # 10 Ω: I_1 goes right
           '#= sign 2.6,2.1 +', '#= sign 2.6,0.8 -')          # 15 Ω: I_1 goes down
SIGNS_SUPER = j('#= sign 3.4,0.8 +', '#= sign 3.4,2.1 -',     # 15 Ω: the walk goes up
                '#= sign 4.0,2.6 +', '#= sign 5.1,2.6 -')     # 3 Ω: the walk goes right
WALK = '#= path 3,0.4 -> 3,3 -> 6,3 -> 9,3 -> 9,0 -> 3.4,0'
OFF = j('wire 0,3 -> 0,0', R1, R2, R3, TERMS, NODES)
NORTON = j(f'IN 4,0 -> 4,3 "$6{A}$"', f'RN 6.5,3 -> 6.5,0 "$9{O}$"', 'wire 4,3 -> 9,3', 'wire 4,0 -> 9,0',
           'terminal 9,3 "$a$" right', 'terminal 9,0 "$b$" right')

STEPS = [
    ('The circuit', GIVEN, r'''
Norton equivalent = a current source $I_N$ in parallel with $R_N$.

**Plan**
1. $I_N$: short $a$–$b$, find the current in the short (mesh + Ohm).
2. $R_N$: sources off, look in from $a$–$b$.
3. Each load: one current divider on the Norton circuit.
'''),
    ('Short $a$–$b$', SHORT, r'''
A wire from $a$ to $b$. The current in it is $I_N$.

The wire is drawn on the far right, but it also shorts $n$ to $b$.
'''),
    ('Mesh currents', j(SHORT, MESHES, CONSTRAINT), r'''
Three windows → $I_1$, $I_2$, $I_3$, all clockwise. $I_3$ is the current down the short.

The $2\,\mathrm{A}$ sits between $I_2$ and $I_3$ → **supermesh**.

Its arrow points **up**:
- $I_3$ goes up through it → $+I_3$
- $I_2$ goes down through it → $-I_2$

$$
I_3-I_2=2
$$
'''),
    ('KVL in mesh $I_1$', j(SHORT, MESHES, CONSTRAINT, SIGNS1), r'''
Sign you **enter** each element by:
- $60\,\mathrm{V}$: enter $-$ → $-60$
- $10\,\Omega$: $+10I_1$
- $15\,\Omega$ (shared with $I_2$): $+15(I_1-I_2)$

$$
-60+10I_1+15(I_1-I_2)=0
$$

$$
25I_1-15I_2=60
$$
'''),
    ('KVL around the supermesh', j(SHORT, MESHES, CONSTRAINT, WALK, SIGNS_SUPER), r'''
Walk around $I_2$ and $I_3$ **together**, skipping the $2\,\mathrm{A}$ branch:
- $15\,\Omega$ (shared with $I_1$): $+15(I_2-I_1)$
- $3\,\Omega$: $+3I_2$
- the short: $0$

$$
15(I_2-I_1)+3I_2=0
$$

$$
18I_2=15I_1 \;\Rightarrow\; I_2=\tfrac56 I_1
$$
'''),
    ('Solve → $I_N$', j(SHORT, '#= path 6.6,3 -> 9,3 -> 9,0.6 "$6\\,\\mathrm{A}$"',
                        r'#+ $I_1=4.8\,\mathrm{A}$', r'#+ $I_2=4\,\mathrm{A}$', r'#+ $I_N=6\,\mathrm{A}$'), r'''
Put $I_2=\tfrac56I_1$ into mesh 1:

$$
25I_1-12.5I_1=60 \;\Rightarrow\; I_1=4.8\,\mathrm{A}
$$

$$
I_2=4\,\mathrm{A} \qquad I_3=I_2+2=6\,\mathrm{A}
$$

$I_3$ runs **down** the short, from $a$ to $b$:

$$
\boxed{I_N=6\,\mathrm{A}}
$$

KCL check at $n$: $4\,\mathrm{A}$ from the $3\,\Omega$ $+$ $2\,\mathrm{A}$ from the source $=6\,\mathrm{A}$ ✓
'''),
    ('$R_N$: sources off', j(OFF, '#= path 10.6,1.5 -> 9.3,1.5 thin color=accent',
                             '#= text 10.1,1.95 "$R_N$" color=accent', r'#+ $R_N=9\,\Omega$'), r'''
- $60\,\mathrm{V}$ → **wire**
- $2\,\mathrm{A}$ → **open** (gone)

Look in from $a$: $3\,\Omega$, then $m$, where $10\,\Omega$ and $15\,\Omega$ both go to $b$ → parallel.

$$
10\parallel 15=\frac{(10)(15)}{25}=6\,\Omega
$$

$$
R_N=3+6=9\,\Omega
$$
'''),
    ('(a) Norton circuit', NORTON, r'''
$$
\boxed{I_N=6\,\mathrm{A}\ (\text{up, into } a)\;\parallel\;R_N=9\,\Omega}
$$

Check: $V_{oc}=I_NR_N=(6)(9)=54\,\mathrm{V}$. (Open $a$–$b$: the $2\,\mathrm{A}$ must go back through the $3\,\Omega$, and the source with $10\parallel15$ is $36\,\mathrm{V}$ behind $6\,\Omega$, so $V_n=36+2(9)=54\,\mathrm{V}$ ✓)
'''),
    ('(b) Load $9\\,\\Omega$', j(NORTON, f'RL 9,3 -> 9,0 "$9{O}$" i="$i_L$"', r'#+ $i_L=3\,\mathrm{A}\ (9\,\Omega)$'), r'''
$I_N$ splits between $R_N$ and $R_L$ (current divider: the **other** resistor goes on top):

$$
i_L=I_N\frac{R_N}{R_N+R_L}=6\cdot\frac{9}{9+9}
$$

$$
\boxed{i_L=3\,\mathrm{A}}
$$

Equal resistors → the current splits in half.
'''),
    ('(b) Load $3\\,\\Omega$', j(NORTON, f'RL 9,3 -> 9,0 "$3{O}$" i="$i_L$"', r'#+ $i_L=4.5\,\mathrm{A}\ (3\,\Omega)$'), r'''
Swap the load. Same Norton circuit, one line:

$$
i_L=6\cdot\frac{9}{9+3}
$$

$$
\boxed{i_L=4.5\,\mathrm{A}}
$$

Without Norton, each new load means solving three meshes again. With it, each load is one divider.
'''),
]


def _net(rl=None):
    net = [('V', 'V1', 's', '0', 60), ('R', 'R1', 's', 'm', 10), ('R', 'R2', 'm', '0', 15), ('R', 'R3', 'm', 'a', 3),
           ('I', 'I1', '0', 'a', 2)]
    return net + ([('R', 'RL', 'a', '0', rl)] if rl else [])


def checks(check):
    els, _ = check(GIVEN)
    s, m = els['R1']
    a = els['R3'][1]
    assert els['V1'] == (s, '0') and els['R2'] == (m, '0') and els['R3'][0] == m and els['I1'] == ('0', a), els
    for d in (SHORT, OFF, NORTON):
        check(d)
    I1 = F(24, 5)
    I2 = F(5, 6) * I1
    I3 = I2 + 2
    assert -60 + 10 * I1 + 15 * (I1 - I2) == 0 and 25 * I1 - 15 * I2 == 60
    assert 15 * (I2 - I1) + 3 * I2 == 0 and 18 * I2 == 15 * I1
    assert (I1, I2, I3) == (F(24, 5), 4, 6) and 25 * I1 - F(25, 2) * I1 == 60
    _, I, _ = solve(_net() + [('V', 'S', 'a', '0', 0)])
    assert abs(I['S'] - 6) < 1e-9 and abs(I['R1'] - 4.8) < 1e-9 and abs(I['R3'] - 4) < 1e-9
    assert F(10 * 15, 25) == 6 and 3 + 6 == 9
    Vn, _, _ = solve(_net())
    assert abs(Vn['a'] - 54) < 1e-9 and 36 + 2 * 9 == 54 and F(60 * 15, 25) == 36
    for rl, il in ((9, 3), (3, F(9, 2))):
        assert 6 * F(9, 9 + rl) == il
        _, Il, _ = solve(_net(rl))
        assert abs(Il['RL'] - il) < 1e-9
