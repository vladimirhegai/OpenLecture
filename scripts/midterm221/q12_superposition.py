r"""Midterm Questions Q12: superposition with 30 V, 6 A and 8 V (+ at the bottom), v_o across the 12 Ω.
30 V alone: (2+2) || 12 = 3 Ω, one mesh -> 10 V. 6 A alone: divider 2 Ω vs 2 + (6 || 12) = 6 Ω -> 1.5 A -> 6 V.
8 V alone: one loop of 8 Ω -> 1 A up through 6 || 12 -> -4 V. Sum 12 V.
Linearity: 6 A doubled -> 18 V; v_o = 0 needs the 30 V part to be -2 V -> V_1 = -6 V.
Inspired by Textbook P4.94 and Fall 2025 Q2."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

TOPIC = 'Superposition'
MARKS = 12
TITLE = 'Three sources, then change one'
SOURCE = 'Textbook P4.94 and Fall 2025 Question 2'
PROMPT = (r'**(a)** Use superposition to find $v_o$. '
          r'**(b)** The $6\,\mathrm{A}$ source is doubled to $12\,\mathrm{A}$. What is $v_o$ now? '
          r'Answer from your part (a) results, without solving the circuit again. '
          r'**(c)** With the original $6\,\mathrm{A}$, what value of the left source (now $30\,\mathrm{V}$) makes '
          r'$v_o=0$?')

O = r'\,\Omega'
V = r'\,\mathrm{V}'
A = r'\,\mathrm{A}'

V1 = f'V1 0,4 -> 0,0 "$30{V}$"'
R1 = f'R1 0,4 -> 3,4 "$6{O}$"'
R2 = f'R2 3,4 -> 3,0 "$12{O}$" v="$v_o$"'
R3 = f'R3 3,4 -> 6,4 "$2{O}$"'
I1 = f'I1 6,0 -> 6,4 "$6{A}$"'
R4 = '\n'.join(['wire 6,4 -> 9,4', f'R4 9,4 -> 9,2 "$2{O}$"'])
V2 = f'V2 9,0 -> 9,2 "$8{V}$"'                  # + at the bottom
V2_OFF = 'wire 9,0 -> 9,2'
BOT = 'wire 0,0 -> 9,0\nground 0,0'
NODES = 'label 3,4 "$a$" above\nlabel 6,4 "$c$" above'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(V1, R1, R2, R3, I1, R4, V2, BOT, NODES)
# 30 V alone: 6 A open, 8 V wire
A30 = j(V1, R1, R2.replace('v_o', "v_o'"), R3, R4, V2_OFF, BOT, NODES)
E30 = j(V1, R1, f"RP 3,4 -> 3,0 \"$3{O}$\" v=\"$v_o'$\"",'wire 0,0 -> 3,0\nground 0,0',
        'label 3,4 "$a$" above')
# 6 A alone: 30 V wire, 8 V wire
A6 = j('wire 0,4 -> 0,0', R1, R2.replace('v_o', "v_o''"), R3, I1, R4, V2_OFF, BOT, NODES)
E6 = j(f"RP 3,4 -> 3,0 \"$6\\parallel 12=4{O}$\" v=\"$v_o''$\"", R3, I1, R4, V2_OFF, 'wire 3,0 -> 9,0\nground 3,0',
       NODES)
# 8 V alone: 30 V wire, 6 A open
A8 = j('wire 0,4 -> 0,0', R1, R2.replace('v_o', "v_o'''"), R3, R4, V2, BOT, NODES)
E8 = j(f"RP 3,4 -> 3,0 \"$4{O}$\" v=\"$v_o'''$\"",R3, R4, V2, 'wire 3,0 -> 9,0\nground 3,0', NODES)

STEPS = [
    ('The circuit', GIVEN, r'''
Three sources. Superposition: turn on **one at a time**, find its part of $v_o$, then add.

Turning a source off:
- voltage source → **wire** (0 V)
- current source → **open** (0 A)

Note the $8\,\mathrm{V}$ has its $+$ at the **bottom**.
'''),
    ('$30\\,\\mathrm{V}$ alone', A30, r'''
- $6\,\mathrm{A}$ → open (gone)
- $8\,\mathrm{V}$ → wire

Now $c$ only joins the $2\,\Omega$ and $2\,\Omega$ → they are in **series**.
'''),
    ('$30\\,\\mathrm{V}$ alone: mesh + Ohm', j(E30, '#= mesh 1.3,1.9 "$I$" cw r=0.6', '#= sign 1.0,3.6 +',
                                                '#= sign 2.1,3.6 -', '#= sign 2.6,3.0 +', '#= sign 2.6,1.0 -',
                                                r"#+ $v_o'=10\,\mathrm{V}$"), r'''
$2+2=4\,\Omega$, in parallel with the $12\,\Omega$ (both from $a$ to the bottom):

$$
12\parallel 4=\frac{(12)(4)}{16}=3\,\Omega
$$

One loop, sign you **enter** each element by:

$$
-30+6I+3I=0 \;\Rightarrow\; I=\tfrac{10}{3}\,\mathrm{A}
$$

$$
v_o'=(3)\left(\tfrac{10}{3}\right)=10\,\mathrm{V}
$$
'''),
    ('$6\\,\\mathrm{A}$ alone', A6, r'''
- $30\,\mathrm{V}$ → wire
- $8\,\mathrm{V}$ → wire

Now the $6\,\Omega$ runs from $a$ to the bottom, side by side with the $12\,\Omega$ → **parallel**.
'''),
    ('$6\\,\\mathrm{A}$ alone: current divider', j(E6, '#= path 5.6,4 -> 3,4 -> 3,0.6 thin', '#= text 2.2,0.7 "$1.5\\,\\mathrm{A}$" color=pink',
                                                    r"#+ $v_o''=6\,\mathrm{V}$"), r'''
$$
6\parallel 12=\frac{(6)(12)}{18}=4\,\Omega
$$

The $6\,\mathrm{A}$ comes up into $c$ and has two ways down:
- right: $2\,\Omega$
- left: $2+4=6\,\Omega$

Current divider (the **other** path on top):

$$
i_{left}=6\cdot\frac{2}{2+6}=1.5\,\mathrm{A}
$$

It flows **down** through the $4\,\Omega$ → $+$ on top:

$$
v_o''=(1.5)(4)=6\,\mathrm{V}
$$
'''),
    ('$8\\,\\mathrm{V}$ alone', A8, r'''
- $30\,\mathrm{V}$ → wire
- $6\,\mathrm{A}$ → open (gone)

Again $6\,\Omega\parallel12\,\Omega=4\,\Omega$, and everything is one loop.
'''),
    ('$8\\,\\mathrm{V}$ alone: mesh + Ohm', j(E8, '#= mesh 6,2 "$I$" cw r=0.8',
                                              '#= sign 2.6,1.0 +', '#= sign 2.6,3.0 -',
                                              '#= sign 3.9,3.6 +', '#= sign 5.1,3.6 -',
                                              '#= sign 8.6,3.6 +', '#= sign 8.6,2.4 -',
                                              r"#+ $v_o'''=-4\,\mathrm{V}$"), r"""
Clockwise $I$, sign you **enter** each element by:
- $4\,\Omega$ (going up): $+4I$
- $2\,\Omega$, $2\,\Omega$: $+2I$, $+2I$
- $8\,\mathrm{V}$ (going down): enter $-$ → $-8$

$$
4I+2I+2I-8=0 \;\Rightarrow\; I=1\,\mathrm{A}
$$

$I$ goes **up** through the $4\,\Omega$, but $v_o$ has $+$ on top:

$$
v_o'''=-(4)(1)=-4\,\mathrm{V}
$$
"""),
    ('(a) Add the three', j(GIVEN, r'#+ $v_o=12\,\mathrm{V}$'), r"""
$$
v_o=v_o'+v_o''+v_o'''=10+6-4
$$

$$
\boxed{v_o=12\,\mathrm{V}}
$$

Keep the signs: the $8\,\mathrm{V}$ part is negative.
"""),
    ('(b) Double the current source', j(GIVEN.replace('"$6{A}$"'.format(A=A), '"$12{A}$"'.format(A=A)),
                                        r"#+ $v_o=18\,\mathrm{V}\ (12\,\mathrm{A})$"), r'''
Each part is **proportional** to its own source.

$6\to12\,\mathrm{A}$ doubles $v_o''$: $6\to12\,\mathrm{V}$. The others don't change.

$$
\boxed{v_o=10+12-4=18\,\mathrm{V}}
$$
'''),
    ('(c) Pick the left source', j(GIVEN.replace('"$30{V}$"'.format(V=V), '"$V_1$"'),
                                   r'#+ $V_1=-6\,\mathrm{V}$'), r'''
Back to the original $6\,\mathrm{A}$. Only the left source changes, so only $v_o'$ changes.

From part (a), $v_o'=\frac{10}{30}V_1=\frac{V_1}{3}$. Make the total zero:

$$
\frac{V_1}{3}+6-4=0 \;\Rightarrow\; \boxed{V_1=-6\,\mathrm{V}}
$$

That is a $6\,\mathrm{V}$ source with its $+$ at the bottom.
'''),
]


def _net(v1=30, i1=6, v2=8):
    return [('V', 'V1', 's', '0', v1), ('R', 'R1', 's', 'a', 6), ('R', 'R2', 'a', '0', 12), ('R', 'R3', 'a', 'c', 2),
            ('I', 'I1', '0', 'c', i1), ('R', 'R4', 'c', 'd', 2), ('V', 'V2', '0', 'd', v2)]


def checks(check):
    els, _ = check(GIVEN)
    s, a = els['R1']
    c, d = els['R4']
    assert els['V1'] == (s, '0') and els['R2'] == (a, '0') and els['R3'] == (a, c), els
    assert els['I1'] == ('0', c) and els['V2'] == ('0', d), els               # 6 A up into c; 8 V + at the bottom
    for drawing in (A30, E30, A6, E6, A8, E8):
        check(drawing)
    # 30 V alone
    assert F(12 * 4, 16) == 3
    I = F(30, 9)
    assert -30 + 6 * I + 3 * I == 0 and 3 * I == 10
    # 6 A alone
    assert F(6 * 12, 18) == 4 and 6 * F(2, 8) == F(3, 2) and F(3, 2) * 4 == 6
    # 8 V alone
    I = F(8, 8)
    assert 4 * I + 2 * I + 2 * I - 8 == 0 and -4 * I == -4
    parts = []
    for args in ((30, 0, 0), (0, 6, 0), (0, 0, 8)):
        Vn, _, _ = solve(_net(*args))
        parts.append(Vn['a'])
    assert all(abs(p - q) < 1e-9 for p, q in zip(parts, (10, 6, -4))), parts
    Vn, _, _ = solve(_net())
    assert abs(Vn['a'] - 12) < 1e-9
    Vn, _, _ = solve(_net(i1=12))
    assert abs(Vn['a'] - 18) < 1e-9
    Vn, _, _ = solve(_net(v1=-6))
    assert abs(Vn['a']) < 1e-9
