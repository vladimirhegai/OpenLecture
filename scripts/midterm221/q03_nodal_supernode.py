r"""Midterm Questions Q3: a 10 V source floats between b and c (+ at c) -> supernode {b, c}; a 4 A source feeds a,
which reaches b through 10 Ω and c through 20 Ω; b and c go to ground through 5 Ω and 10 Ω.
V_a = 40, V_b = 10, V_c = 20 V; 1 A leaves the source's + end -> it delivers 10 W.
Fall 2025 Q4 style: (a) write the equations, (b) solve, (c) source power. Inspired by Textbook P4.27."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

TOPIC = 'Nodal analysis'
MARKS = 10
TITLE = 'A voltage source between two nodes'
SOURCE = 'Textbook P4.27 and Fall 2025 Midterm Question 4'
PROMPT = (r'**(a)** Write (but do not solve) the node-voltage equations needed to solve the circuit. '
          r'**(b)** Solve them for $V_a$, $V_b$ and $V_c$. '
          r'**(c)** Find the power of the $10\,\mathrm{V}$ source, and say whether it absorbs or delivers it.')

O = r'\,\Omega'


def j(*parts):
    return '\n'.join(parts)


I1 = r'I1 0,0 -> 0,3 "$4\,\mathrm{A}$"'
FEED = 'wire 0,3 -> 2,3'
R2 = f'R2 2,3 -> 5,3 "$10{O}$"'
R3 = f'R3 5,3 -> 5,0 "$5{O}$"'
V1 = r'V1 8,3 -> 5,3 "$10\,\mathrm{V}$"'
R4 = f'R4 8,3 -> 8,0 "$10{O}$"'
TOP = '\n'.join(['wire 2,3 -> 2,5', f'R5 2,5 -> 8,5 "$20{O}$"', 'wire 8,5 -> 8,3'])
BOT = 'wire 0,0 -> 8,0\nground 0,0'
GIVEN = j(I1, FEED, R2, R3, V1, R4, TOP, BOT,
          'label 2,4 "$a$" left', 'label 5,3 "$b$" above', 'label 8,4 "$c$" right')

NODES = j('label 2,4 "$a$" left', 'label 5,3 "$b$" above', 'label 8,4 "$c$" right', 'dot 2,3', 'dot 5,3', 'dot 8,3')
# currents drawn high -> low: a to b, a to c, and down to ground
CURR = j(I1, FEED, f'R2 2,3 -> 5,3 "$10{O}$" i="$i_1$"', f'R3 5,3 -> 5,0 "$5{O}$" i="$i_3$"', V1,
         f'R4 8,3 -> 8,0 "$10{O}$" i="$i_4$"',
         '\n'.join(['wire 2,3 -> 2,5', f'R5 2,5 -> 8,5 "$20{O}$" i="$i_2$"', 'wire 8,5 -> 8,3']), BOT)
SUPER = '#= region 4.5,2.5 8.5,4.1'  # unlabelled: the step title names it
KCL_A = '#= region 1.55,2.55 2.45,3.6 color=green'

STEPS = [
    ('The circuit', GIVEN, r'''
**Method: nodal with a supernode.** The $10\,\mathrm{V}$ source sits between $b$ and $c$, and neither of them is ground.

**Plan**
1. Currents in terms of $V_a$, $V_b$, $V_c$.
2. Source constraint, KCL at $a$, KCL on the supernode $\{b,c\}$ → three equations: that is (a).
3. Solve, then KCL at $c$ for the source current.
'''),
    ('Name the nodes', j(I1, FEED, R2, R3, V1, R4, TOP, BOT, NODES), r'''
- Bottom wire = ground, $0\,\mathrm{V}$.
- Three other nodes → $V_a$, $V_b$, $V_c$: three unknowns, so you need three equations.
'''),
    ('Currents', j(CURR, NODES), r'''
Draw every current from high to low (toward ground). Current = (start − end) / $R$:

$$
i_1=\frac{V_a-V_b}{10} \qquad i_2=\frac{V_a-V_c}{20}
$$

$$
i_3=\frac{V_b}{5} \qquad i_4=\frac{V_c}{10}
$$

No formula for the current through the $10\,\mathrm{V}$ source: a voltage source has no $V/R$.
'''),
    ('Supernode', j(CURR, NODES, SUPER), r'''
The source joins $b$ and $c$ → treat them as one **supernode** $\{b,c\}$.

**Source constraint** ($+$ side minus $-$ side):

$$
V_c-V_b=10
$$
'''),
    ('KCL at $a$', j(CURR, NODES, SUPER, KCL_A), r'''
Entering $+$, leaving $-$. The $4\,\mathrm{A}$ enters; $i_1$ and $i_2$ leave:

$$
4-\frac{V_a-V_b}{10}-\frac{V_a-V_c}{20}=0
$$
'''),
    ('(a) KCL on the supernode', j(CURR, NODES, SUPER), r'''
Around the whole box: $i_1$ and $i_2$ enter, $i_3$ and $i_4$ leave. (The source current stays **inside** the box.)

$$
\frac{V_a-V_b}{10}+\frac{V_a-V_c}{20}-\frac{V_b}{5}-\frac{V_c}{10}=0
$$

**Answer (a):** this equation, KCL at $a$, and $V_c-V_b=10$.
'''),
    ('(b) Solve', j(CURR, NODES, r'#= text 1.2,4.3 "$40\,\mathrm{V}$" color=purple',
                    r'#= text 4.2,1.5 "$10\,\mathrm{V}$" color=purple', r'#= text 9.1,1.5 "$20\,\mathrm{V}$" color=purple',
                    r'#+ $V_a=40\,\mathrm{V}$', r'#+ $V_b=10\,\mathrm{V}$', r'#+ $V_c=20\,\mathrm{V}$'), r'''
**Shortcut:** add the two KCL equations. $i_1$ and $i_2$ cancel:

$$
4-\frac{V_b}{5}-\frac{V_c}{10}=0 \;\Rightarrow\; 2V_b+V_c=40
$$

Put in $V_c=V_b+10$: $3V_b+10=40$ → $V_b=10\,\mathrm{V}$, $V_c=20\,\mathrm{V}$.

KCL at $a$, $\times 20$: $80-2(V_a-10)-(V_a-20)=0$ → $3V_a=120$:

$$
\boxed{V_a=40\,\mathrm{V} \quad V_b=10\,\mathrm{V} \quad V_c=20\,\mathrm{V}}
$$

(Or type the three equations into the fx-991 equation solver.)
'''),
    ('(c) Current through the source', j(CURR, NODES, '#= path 5.4,3 -> 7.6,3 "$1\\,\\mathrm{A}$" thin',
                                         r'#= text 9.1,1.5 "$2\,\mathrm{A}$" color=pink',
                                         r'#= text 5,5.9 "$1\,\mathrm{A}$" color=pink', r'#+ $P=10\,\mathrm{W}$'), r'''
KCL at $c$ (on its own, not the supernode):
- in from the $20\,\Omega$: $i_2=\frac{40-20}{20}=1\,\mathrm{A}$
- out down the $10\,\Omega$: $i_4=\frac{20}{10}=2\,\mathrm{A}$

The missing $1\,\mathrm{A}$ comes through the source, from $b$ into $c$.

It leaves the source at its $+$ end → the source **delivers**:

$$
\boxed{P=(10)(1)=10\,\mathrm{W}\ \text{delivered}}
$$

Check at $b$: in $i_1=3\,\mathrm{A}$; out $i_3=2\,\mathrm{A}$ plus $1\,\mathrm{A}$ into the source ✓
'''),
]


NET = [('I', 'I1', '0', 'a', 4), ('R', 'R2', 'a', 'b', 10), ('R', 'R3', 'b', '0', 5), ('V', 'V1', 'c', 'b', 10),
       ('R', 'R4', 'c', '0', 10), ('R', 'R5', 'a', 'c', 20)]


def checks(check):
    els, _ = check(GIVEN)
    a, b = els['R2']
    c = els['R4'][0]
    assert els['I1'] == ('0', a) and els['R3'] == (b, '0') and els['V1'] == (c, b), els
    assert els['R4'] == (c, '0') and els['R5'] == (a, c), els
    check(CURR)
    Va, Vb, Vc = 40, 10, 20
    assert Vc - Vb == 10
    assert 4 - F(Va - Vb, 10) - F(Va - Vc, 20) == 0
    assert F(Va - Vb, 10) + F(Va - Vc, 20) - F(Vb, 5) - F(Vc, 10) == 0
    assert 2 * Vb + Vc == 40 and 3 * Vb + 10 == 40 and 80 - 2 * (Va - 10) - (Va - 20) == 0 and 3 * Va == 120
    i2, i4, i1, i3 = F(Va - Vc, 20), F(Vc, 10), F(Va - Vb, 10), F(Vb, 5)
    assert (i2, i4, i1, i3) == (1, 2, 3, 2) and i4 - i2 == 1 and i1 - i3 == 1
    V, I, P = solve(NET)
    assert abs(V['a'] - 40) < 1e-9 and abs(V['b'] - 10) < 1e-9 and abs(V['c'] - 20) < 1e-9
    # mna: I['V1'] is the current c -> b inside the source; -1 means 1 A flows b -> c (out of the + end)
    assert abs(I['V1'] + 1) < 1e-9 and abs(P['V1'] + 10) < 1e-9, (I['V1'], P['V1'])
