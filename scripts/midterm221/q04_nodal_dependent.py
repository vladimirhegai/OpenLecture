r"""Midterm Questions Q4: 60 V source -> 10 Ω -> node a (10 Ω to ground carries i_x) -> 5 Ω -> node b (5 Ω to ground,
v_o), and a current source 3 i_x pushing up into b. Two KCLs plus the control equation:
V_a = 40, v_o = V_b = 50 V, i_x = 4 A; the dependent source delivers 600 W, the 60 V source 120 W, resistors absorb 720 W.
The a-b current is drawn a -> b and comes out -2 A (a lesson in negative currents). Inspired by Textbook P4.47 and
the Week 4 tutorial."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

TOPIC = 'Nodal analysis'
MARKS = 10
TITLE = 'A current source that watches a resistor'
SOURCE = 'Textbook P4.47 and the Week 4 tutorial'
PROMPT = (r'**(a)** Write the node-voltage equations for the circuit, including an equation for the controlling '
          r'current $i_x$. '
          r'**(b)** Find $v_o$. '
          r'**(c)** Find the power of the dependent source, and say whether it absorbs or delivers it. '
          r'**(d)** Show that the total power delivered equals the total power absorbed.')

O = r'\,\Omega'


def j(*parts):
    return '\n'.join(parts)


V1 = r'V1 0,3 -> 0,0 "$60\,\mathrm{V}$"'
R1 = f'R1 0,3 -> 3,3 "$10{O}$"'
R2 = f'R2 3,3 -> 3,0 "$10{O}$" i="$i_x$"'
R3 = f'R3 3,3 -> 6,3 "$5{O}$"'
R4 = f'R4 6,3 -> 6,0 "$5{O}$" v="$v_o$"'
G1 = '\n'.join(['wire 6,3 -> 8.5,3', r'G1 8.5,0 -> 8.5,3 "$3i_x$"'])
BOT = 'wire 0,0 -> 8.5,0\nground 0,0'
GIVEN = j(V1, R1, R2, R3, R4, G1, BOT)

NODES = j('label 3,3 "$a$" above', 'label 6,3 "$b$" above', 'dot 3,3', 'dot 6,3')
CURR = j(V1, f'R1 0,3 -> 3,3 "$10{O}$" i="$i_1$"', R2, f'R3 3,3 -> 6,3 "$5{O}$" i="$i_3$"',
         f'R4 6,3 -> 6,0 "$5{O}$" v="$v_o$" i="$i_o$"', G1, BOT)
KCL_A = '#= region 2.55,2.55 3.45,3.6 color=green'
KCL_B = '#= region 5.55,2.55 6.45,3.6 color=green'
CONTROL = '#= path 3,2.6 -> 3,0.4 thin color=orange'

STEPS = [
    ('The circuit', GIVEN, r'''
**Method: nodal.** Two unknown nodes ($a$ and $b$), and the dependent source is a **current** source: in KCL it is just one more current.

**Plan**
1. Write every current with $V_a$, $V_b$, including $i_x$.
2. KCL at $a$ and at $b$ → (a).
3. Solve → $v_o$, then the powers.
'''),
    ('Name the nodes', j(GIVEN, NODES), r'''
- Bottom wire = ground. The top of the $60\,\mathrm{V}$ source is then $60\,\mathrm{V}$ (known, no name needed).
- $a$ and $b$ → $V_a$, $V_b$.
- $v_o$ is across the right $5\,\Omega$ → $v_o=V_b$.
'''),
    ('Currents', j(CURR, NODES), r'''
Current = (start − end) / $R$:

$$
i_1=\frac{60-V_a}{10} \qquad i_x=\frac{V_a}{10}
$$

$$
i_3=\frac{V_a-V_b}{5} \qquad i_o=\frac{V_b}{5}
$$

$i_3$ is drawn $a\to b$. If $V_b>V_a$ it comes out negative, and that's fine.
'''),
    ('The control equation', j(CURR, NODES, CONTROL), r'''
$i_x$ is the current down the $10\,\Omega$ at $a$:

$$
i_x=\frac{V_a}{10}
$$

So the dependent source pushes $3i_x=0.3V_a$ up into $b$.

Write this **before** the KCLs: then every equation has only $V_a$ and $V_b$ in it.
'''),
    ('KCL at $a$', j(CURR, NODES, KCL_A), r'''
Entering $+$, leaving $-$. $i_1$ enters; $i_x$ and $i_3$ leave:

$$
\frac{60-V_a}{10}-\frac{V_a}{10}-\frac{V_a-V_b}{5}=0
$$
'''),
    ('(a) KCL at $b$', j(CURR, NODES, KCL_B), r'''
$i_3$ and $3i_x$ enter; $i_o$ leaves:

$$
\frac{V_a-V_b}{5}+3\left(\frac{V_a}{10}\right)-\frac{V_b}{5}=0
$$

**Answer (a):** KCL at $a$, KCL at $b$, and $i_x=\frac{V_a}{10}$.
'''),
    ('(b) Solve', j(CURR, NODES, r'#= text 3,4.3 "$40\,\mathrm{V}$" color=purple',
                    r'#= text 6,4.3 "$50\,\mathrm{V}$" color=purple',
                    r'#+ $V_a=40\,\mathrm{V}$', r'#+ $v_o=V_b=50\,\mathrm{V}$', r'#+ $i_x=4\,\mathrm{A}$'), r'''
Both equations $\times 10$:

$$
60-4V_a+2V_b=0 \;\Rightarrow\; 2V_a-V_b=30
$$

$$
2V_a-4V_b+3V_a=0 \;\Rightarrow\; 5V_a=4V_b
$$

So $V_b=1.25V_a$. Into the first: $0.75V_a=30$ → $V_a=40\,\mathrm{V}$.

$$
\boxed{v_o=V_b=50\,\mathrm{V}}
$$

Then $i_x=\frac{40}{10}=4\,\mathrm{A}$, $i_o=\frac{50}{5}=10\,\mathrm{A}$, and $i_3=\frac{40-50}{5}=-2\,\mathrm{A}$: really $2\,\mathrm{A}$ from $b$ to $a$.
'''),
    ('(c) Dependent source power', j(CURR, NODES, r'#= text 9.7,1.5 "$12\,\mathrm{A}$" color=pink',
                                     '#= sign 9,2.4 +', '#= sign 9,0.6 -', r'#+ $p_{dep}=600\,\mathrm{W}$'), r'''
Its current: $3i_x=3(4)=12\,\mathrm{A}$, up.

Its voltage: top is $b$ ($50\,\mathrm{V}$), bottom is ground → $50\,\mathrm{V}$, $+$ on top.

The $12\,\mathrm{A}$ leaves at the $+$ end → it **delivers**:

$$
\boxed{p_{dep}=(50)(12)=600\,\mathrm{W}\ \text{delivered}}
$$
'''),
    ('(d) Power balance', j(CURR, NODES, r'#= text 1.5,4.3 "$40\,\mathrm{W}$" color=green',
                            r'#= text 3.95,0.7 "$160\,\mathrm{W}$" color=green',
                            r'#= text 4.5,4.3 "$20\,\mathrm{W}$" color=green',
                            r'#= text 7.2,0.5 "$500\,\mathrm{W}$" color=green'), r'''
**Delivered**
- $60\,\mathrm{V}$ source: $i_1=\frac{60-40}{10}=2\,\mathrm{A}$ leaves its $+$ end → $(60)(2)=120\,\mathrm{W}$
- dependent source: $600\,\mathrm{W}$

**Absorbed** ($i^2R$)
- top $10\,\Omega$: $(2)^2(10)=40\,\mathrm{W}$; $\ 10\,\Omega$ at $a$: $(4)^2(10)=160\,\mathrm{W}$
- top $5\,\Omega$: $(2)^2(5)=20\,\mathrm{W}$; $\ 5\,\Omega$ at $b$: $(10)^2(5)=500\,\mathrm{W}$

$$
120+600=720=40+160+20+500 \ ✓
$$
'''),
]


NET = [('V', 'V1', 's', '0', 60), ('R', 'R1', 's', 'a', 10), ('R', 'R2', 'a', '0', 10), ('R', 'R3', 'a', 'b', 5),
       ('R', 'R4', 'b', '0', 5), ('G', 'G1', '0', 'b', {'a': F(3, 10)})]


def checks(check):
    els, _ = check(GIVEN)
    s, a = els['R1']
    b = els['R3'][1]
    assert els['V1'] == (s, '0') and els['R2'] == (a, '0') and els['R3'][0] == a, els
    assert els['R4'] == (b, '0') and els['G1'] == ('0', b), els
    check(CURR)
    Va, Vb = 40, 50
    ix = F(Va, 10)
    assert F(60 - Va, 10) - F(Va, 10) - F(Va - Vb, 5) == 0
    assert F(Va - Vb, 5) + 3 * ix - F(Vb, 5) == 0
    assert 60 - 4 * Va + 2 * Vb == 0 and 2 * Va - Vb == 30 and 5 * Va == 4 * Vb and F(3, 4) * Va == 30
    i1, i3, io = F(60 - Va, 10), F(Va - Vb, 5), F(Vb, 5)
    assert (ix, i1, i3, io, 3 * ix) == (4, 2, -2, 10, 12)
    absorbed = [i1 ** 2 * 10, ix ** 2 * 10, i3 ** 2 * 5, io ** 2 * 5]
    assert absorbed == [40, 160, 20, 500] and 60 * i1 == 120 and 50 * 3 * ix == 600 and sum(absorbed) == 720
    V, I, P = solve([(e[0], e[1], e[2], e[3], {k: float(v) for k, v in e[4].items()}) if e[0] == 'G' else e
                     for e in NET])
    assert abs(V['a'] - 40) < 1e-9 and abs(V['b'] - 50) < 1e-9
    assert abs(P['G1'] + 600) < 1e-9 and abs(P['V1'] + 120) < 1e-9 and abs(sum(P.values())) < 1e-9, P
