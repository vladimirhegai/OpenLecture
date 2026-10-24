r"""Textbook P4.27: a dependent voltage source (value i_x, i.e. 1 Ω · i_x) floats between nodes b and c → supernode.
Nodal with the user's convention: currents drawn toward ground (or from the fixed 12 V node into the circuit),
current = (start − end)/R, KCL with leaving −, entering +. Drawn 10 units wide instead of 12 (same topology)."""
from fractions import Fraction as F

SECTION = 'B'
TITLE = 'A voltage source that floats between two nodes'
SOURCE = 'Textbook P4.27'
CITES = [{"chunk_id": "03690d12-5cc2-452b-8d95-ea17d0ba1ae7", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1}]
PROMPT = r'Find $v$.'

O = r'\,\Omega'


def j(*parts):
    return '\n'.join(parts)


I1 = r'I1 0,0 -> 0,3 "$4.8\,\mathrm{A}$"'
R1 = f'R1 2.5,3 -> 2.5,0 "$7.5{O}$" i="$i_x$"'
R2 = f'R2 2.5,3 -> 5,3 "$2.5{O}$"'
R3 = f'R3 5,3 -> 5,0 "$10{O}$" v="$v$"'
E1 = r'E1 7.5,3 -> 5,3 "$i_x$"'
R4 = f'R4 7.5,3 -> 7.5,0 "$2.5{O}$"'
R5 = f'R5 7.5,3 -> 10,3 "$1{O}$"'
V1 = r'V1 10,3 -> 10,0 "$12\,\mathrm{V}$"'
REST = j('wire 0,3 -> 2.5,3', 'wire 10,0 -> 0,0', 'label 2.5,3 "$a$" above', 'label 5,3 "$b$" above',
         'label 7.5,3 "$c$" above', 'ground 0,0')
GIVEN = j(I1, R1, R2, R3, E1, R4, R5, V1, REST)

NODES = j(REST, 'label 10,3 "$d$" above', 'dot 2.5,3', 'dot 5,3', 'dot 7.5,3', 'dot 10,3')
# currents toward ground; the 1 Ω current is drawn from the 12 V node d into c
CURR = j(R1, f'R2 2.5,3 -> 5,3 "$2.5{O}$" i="$i_1$"', f'R3 5,3 -> 5,0 "$10{O}$" v="$v$" i="$i_2$"', E1,
         f'R4 7.5,3 -> 7.5,0 "$2.5{O}$" i="$i_3$"', f'R5 7.5,3 -> 10,3 "$1{O}$" i_rev="$i_4$"', I1, V1)
PLAIN = j(I1, R1, R2, R3, E1, R4, R5, V1)
SUPER = '#= region 4.55,2.45 7.95,4.15'  # unlabelled: the step title names it (a tag here sits on the wire)
KCL_A = '#= region 2.1,2.45 2.9,4.15 color=green'

STEPS = [
    ('The circuit', GIVEN, r'''
**Method: nodal with a supernode.** The dependent voltage source sits between $b$ and $c$, neither of them ground.
'''),
    ('Name the nodes', j(PLAIN, NODES, r'#+ $V_d=12\,\mathrm{V}$'), r'''
- Nodes $a$, $b$, $c$, $d$ → $V_a$, $V_b$, $V_c$, $V_d$. Ground is the bottom wire (no name).
- $d$ sits on top of the grounded $12\,\mathrm{V}$ source → $V_d=12\,\mathrm{V}$.
- $v$ is across the $10\,\Omega$ → $v=V_b$.
'''),
    ('Currents', j(CURR, NODES), r'''
Draw the currents toward ground; the $1\,\Omega$ one from the $12\,\mathrm{V}$ node into $c$.

$V/R$ is (start − end):

$$
i_x=\frac{V_a}{7.5} \qquad i_1=\frac{V_a-V_b}{2.5} \qquad i_2=\frac{V_b}{10}
$$

$$
i_3=\frac{V_c}{2.5} \qquad i_4=\frac{12-V_c}{1}
$$
'''),
    ('Supernode', j(CURR, NODES, SUPER), r'''
$b$ and $c$ are joined by a voltage source → one **supernode** $\{b,c\}$.

**Source constraint** ($+$ side minus $-$ side), the source is $1\,\Omega\cdot i_x$:

$$
V_c-V_b=i_x=\frac{V_a}{7.5}
$$
'''),
    ('KCL at $a$', j(CURR, NODES, SUPER, KCL_A), r'''
Entering $+$, leaving $-$:

$$
4.8-\frac{V_a}{7.5}-\frac{V_a-V_b}{2.5}=0
$$

$\times 7.5$:

$$
36-V_a-3V_a+3V_b=0 \;\Rightarrow\; V_a=9+0.75V_b
$$

So the constraint becomes $V_c=V_b+1.2+0.1V_b=1.1V_b+1.2$.
'''),
    ('KCL on the supernode', j(CURR, NODES, SUPER), r'''
$i_1$ and $i_4$ enter, $i_2$ and $i_3$ leave:

$$
\frac{V_a-V_b}{2.5}-\frac{V_b}{10}-\frac{V_c}{2.5}+\frac{12-V_c}{1}=0
$$

$\times 10$:

$$
4V_a-5V_b-14V_c+120=0
$$
'''),
    ('Solve', j(CURR, NODES, r'#= text 2.5,4.0 "$15\,\mathrm{V}$" color=purple', r'#= text 5,4.0 "$8\,\mathrm{V}$" color=purple',
                r'#= text 7.5,4.0 "$10\,\mathrm{V}$" color=purple',
                r'#+ $V_a=15\,\mathrm{V}$', r'#+ $V_c=10\,\mathrm{V}$', r'#+ $v=V_b=8\,\mathrm{V}$'), r'''
Substitute $V_a=9+0.75V_b$ and $V_c=1.1V_b+1.2$:

$$
36+3V_b-5V_b-15.4V_b-16.8+120=0
$$

$$
17.4V_b=139.2 \;\Rightarrow\; \boxed{v=V_b=8\,\mathrm{V}}
$$

$V_a=15\,\mathrm{V}$, $V_c=10\,\mathrm{V}$, $i_x=2\,\mathrm{A}$. Check: $V_c-V_b=2=i_x$ ✓
'''),
]


def _mna():
    import os
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
    import mna
    return mna


def checks(check):
    els, _ = check(GIVEN)
    a, b, c = els['R2'][0], els['R2'][1], els['R4'][0]
    d = els['R5'][1]
    assert els['I1'] == ('0', a) and els['R1'] == (a, '0') and els['R3'] == (b, '0'), els
    assert els['E1'] == (c, b) and els['R4'] == (c, '0') and els['R5'][0] == c and els['V1'] == (d, '0'), els
    V, I, P = _mna().solve([('I', 'I1', '0', 'a', 4.8), ('R', 'R1', 'a', '0', 7.5), ('R', 'R2', 'a', 'b', 2.5),
                            ('R', 'R3', 'b', '0', 10), ('E', 'E1', 'c', 'b', {'a': 1 / 7.5}, 0),
                            ('R', 'R4', 'c', '0', 2.5), ('R', 'R5', 'c', 'd', 1), ('V', 'V1', 'd', '0', 12)])
    assert abs(V['a'] - 15) < 1e-9 and abs(V['b'] - 8) < 1e-9 and abs(V['c'] - 10) < 1e-9
    Va, Vb, Vc = 15, 8, 10
    assert F(Va, 1) / F(75, 10) == 2 and Vc - Vb == 2
    assert F(48, 10) - F(Va) / F(75, 10) - (Va - Vb) / F(25, 10) == 0
    assert 36 - Va - 3 * Va + 3 * Vb == 0 and 9 + F(3, 4) * Vb == Va and F(11, 10) * Vb + F(12, 10) == Vc
    assert (Va - Vb) / F(25, 10) - F(Vb, 10) - Vc / F(25, 10) + (12 - Vc) == 0
    assert 4 * Va - 5 * Vb - 14 * Vc + 120 == 0
    assert 36 + 3 * Vb - 5 * Vb - F(154, 10) * Vb - F(168, 10) + 120 == 0 and F(1392, 10) / F(174, 10) == 8
