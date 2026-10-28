r"""Midterm Questions Q7: a ladder with a 24 V source (in series with 4 Ω) and a 1 A source pulling current out of
node o. Source transformations, one per step: 6 A ∥ 4 Ω -> 6 A ∥ 3 Ω -> 18 V + 3 Ω -> 18 V + 6 Ω -> 3 A ∥ 6 Ω
-> 2 A ∥ 3 Ω, so v_o = 6 V. Then back: R3 carries 2 A, V_b = 12 V, the 24 V source gives 3 A -> 72 W.
Inspired by Assessment Problem 4.15 / Textbook P4.63."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

TOPIC = 'Source transformation'
MARKS = 8
TITLE = 'Shrink the ladder one swap at a time'
SOURCE = 'Assessment Problem 4.15 and Textbook P4.63'
PROMPT = (r'**(a)** Use a series of source transformations to find $v_o$. '
          r'**(b)** Find the power delivered by the $24\,\mathrm{V}$ source.')

O = r'\,\Omega'
V = r'\,\mathrm{V}'
A = r'\,\mathrm{A}'

V1 = f'V1 0,3 -> 0,0 "$24{V}$"'
R1 = f'R1 0,3 -> 3,3 "$4{O}$"'
R2 = f'R2 3,3 -> 3,0 "$12{O}$"'
R3 = f'R3 3,3 -> 6,3 "$3{O}$"'
I1 = f'I1 6,3 -> 6,0 "$1{A}$"'
OUT = '\n'.join(['wire 6,3 -> 8,3', f'R4 8,3 -> 8,0 "$6{O}$" v="$v_o$"'])
BOT = 'wire 0,0 -> 8,0\nground 0,0'
LAB_B = 'label 3,3 "$b$" above'
LAB_O = 'label 6,3 "$o$" above'


def j(*parts):
    return '\n'.join(parts)


RIGHT = j(I1, OUT, BOT, LAB_O)                    # never changes until the last swap
GIVEN = j(V1, R1, R2, R3, RIGHT, LAB_B)
NORTON1 = j(f'IA 0,0 -> 0,3 "$6{A}$"', 'wire 0,3 -> 1.5,3', 'wire 1.5,3 -> 3,3', f'R1 1.5,3 -> 1.5,0 "$4{O}$"',
            R2, R3, RIGHT, LAB_B)
PAR1 = j(f'IA 0,0 -> 0,3 "$6{A}$"', 'wire 0,3 -> 3,3', f'RP 3,3 -> 3,0 "$3{O}$"', R3, RIGHT, LAB_B)
THEV1 = j(f'VB 0,3 -> 0,0 "$18{V}$"', f'RB 0,3 -> 3,3 "$3{O}$"', R3, RIGHT, LAB_B)
SER = j(f'VB 0,3 -> 0,0 "$18{V}$"', f'RS 0,3 -> 6,3 "$3+3=6{O}$"', RIGHT)
NORTON2 = j(f'IC 0,0 -> 0,3 "$3{A}$"', 'wire 0,3 -> 3,3', 'wire 3,3 -> 6,3', f'RN 3,3 -> 3,0 "$6{O}$"', RIGHT)
LAST = j(f'ID 0,0 -> 0,3 "$2{A}$"', 'wire 0,3 -> 8,3', f'RQ 8,3 -> 8,0 "$3{O}$" v="$v_o$"', BOT, LAB_O)

STEPS = [
    ('The circuit', GIVEN, r'''
**Method: source transformation.** Swap sources one at a time until everything sits in parallel with the $6\,\Omega$.

Two swaps you can make:
- voltage source **in series** with $R$ ↔ current source **in parallel** with $R$
- $i=\dfrac{v}{R}$ and $v=iR$, same $R$
'''),
    ('Swap 1: $24\\,\\mathrm{V}$ + $4\\,\\Omega$', NORTON1, r'''
$24\,\mathrm{V}$ in **series** with $4\,\Omega$ → current source in **parallel** with $4\,\Omega$:

$$
i=\frac{24}{4}=6\,\mathrm{A}
$$

$+$ was on top → the arrow points **up** (toward the $+$ end).
'''),
    ('Parallel: $4\\,\\Omega\\parallel12\\,\\Omega$', PAR1, r'''
$4\,\Omega$ and $12\,\Omega$ both go from the top wire to the bottom wire → parallel:

$$
4\parallel12=\frac{(4)(12)}{16}=3\,\Omega
$$
'''),
    ('Swap 2: $6\\,\\mathrm{A}$ ∥ $3\\,\\Omega$', THEV1, r'''
$6\,\mathrm{A}$ in **parallel** with $3\,\Omega$ → voltage source in **series** with $3\,\Omega$:

$$
v=(6)(3)=18\,\mathrm{V}
$$

Arrow was up → $+$ on **top**.
'''),
    ('Series: $3\\,\\Omega+3\\,\\Omega$', SER, r'''
The two $3\,\Omega$ now carry the same current → series:

$$
3+3=6\,\Omega
$$
'''),
    ('Swap 3: $18\\,\\mathrm{V}$ + $6\\,\\Omega$', NORTON2, r'''
$18\,\mathrm{V}$ in **series** with $6\,\Omega$ → current source in **parallel** with $6\,\Omega$:

$$
i=\frac{18}{6}=3\,\mathrm{A}\ \text{up}
$$

Now every element sits between $o$ and ground.
'''),
    ('Combine', LAST, r'''
**Current sources in parallel add** (watch the arrows):
- $3\,\mathrm{A}$ pushes **up** into $o$
- $1\,\mathrm{A}$ pulls **down** out of $o$

$$
3-1=2\,\mathrm{A}\ \text{up}
$$

**Resistors in parallel:** $6\parallel6=3\,\Omega$
'''),
    ("(a) Ohm's law → $v_o$", j(LAST, '#= mesh 4,1.5 "$2\\,\\mathrm{A}$" cw r=0.7', '#= sign 8.38,2.3 +',
                                 '#= sign 8.38,0.7 -', r'#+ $v_o=6\,\mathrm{V}$'), r'''
$2\,\mathrm{A}$ goes around and enters the $3\,\Omega$ at the top → $+$ on top, same as $v_o$:

$$
\boxed{v_o=(2)(3)=6\,\mathrm{V}}
$$
'''),
    ('Back up one picture', j(THEV1, '#= text 6.7,2.5 "$6\\,\\mathrm{V}$" color=pink',
                              '#= path 3.4,3 -> 5.6,3 "$2\\,\\mathrm{A}$" thin', r'#+ $v_o=6\,\mathrm{V}$',
                              r'#+ $i_3=2\,\mathrm{A}$'), r'''
The $18\,\mathrm{V}$ source is **not** the $24\,\mathrm{V}$ source → its power means nothing. Go back to circuits that still hold real parts.

Here the $3\,\Omega$ on the right is the **real** $3\,\Omega$, and $o$ is the real node ($v_o=6\,\mathrm{V}$). The loop current through it:

$$
i_3=\frac{18-6}{3+3}=2\,\mathrm{A}\ \text{toward}\ o
$$
'''),
    ('(b) Power of the $24\\,\\mathrm{V}$', j(GIVEN, '#= text 6.7,2.5 "$6\\,\\mathrm{V}$" color=pink',
                                              '#= text 3.75,2.5 "$12\\,\\mathrm{V}$" color=pink',
                                              '#= path 3.4,3 -> 5.6,3 "$2\\,\\mathrm{A}$" thin',
                                              '#= path 0.4,3 -> 2.6,3 "$3\\,\\mathrm{A}$" thin',
                                              r'#+ $v_o=6\,\mathrm{V}$', r'#+ $i_3=2\,\mathrm{A}$',
                                              r'#+ $p_{24V}=72\,\mathrm{W}\ \text{del.}$'), r'''
Original circuit. Walk from $b$ to $o$ through the $3\,\Omega$:

$$
V_b=v_o+(3)(2)=12\,\mathrm{V}
$$

Ohm's law on the $4\,\Omega$:

$$
i_1=\frac{24-12}{4}=3\,\mathrm{A}
$$

It leaves the $+$ → the source **delivers**:

$$
\boxed{p_{24V}=(24)(3)=72\,\mathrm{W}}
$$

Check at $b$: in $3\,\mathrm{A}$; out $\frac{12}{12}+2=3\,\mathrm{A}$ ✓
'''),
]


NET = [('V', 'V1', 's', '0', 24), ('R', 'R1', 's', 'b', 4), ('R', 'R2', 'b', '0', 12), ('R', 'R3', 'b', 'o', 3),
       ('I', 'I1', 'o', '0', 1), ('R', 'R4', 'o', '0', 6)]


def checks(check):
    els, _ = check(GIVEN)
    s, b = els['R1']
    o = els['R3'][1]
    assert els['V1'] == (s, '0') and els['R2'] == (b, '0') and els['R3'] == (b, o), els
    assert els['I1'] == (o, '0') and els['R4'] == (o, '0'), els      # 1 A arrow points down, out of o
    n1, _ = check(NORTON1)
    assert n1['IA'][0] == '0' and n1['R1'][1] == '0' and n1['R1'][0] == n1['IA'][1] == n1['R2'][0], n1
    for d in (PAR1, THEV1, SER, NORTON2):
        check(d)
    last, _ = check(LAST)
    assert last['ID'] == ('0', last['RQ'][0]), last
    assert F(24, 4) == 6 and F(4 * 12, 16) == 3 and 6 * 3 == 18 and F(18, 6) == 3 and 3 - 1 == 2
    assert F(6 * 6, 12) == 3 and 2 * 3 == 6
    i3 = F(18 - 6, 6)
    Vb = 6 + 3 * i3
    i1 = F(24 - Vb, 4)
    assert i3 == 2 and Vb == 12 and i1 == 3 and 24 * i1 == 72 and F(12, 12) + i3 == i1
    Vn, I, P = solve(NET)
    assert abs(Vn['o'] - 6) < 1e-9 and abs(Vn['b'] - 12) < 1e-9 and abs(I['R3'] - 2) < 1e-9
    assert abs(I['R1'] - 3) < 1e-9 and abs(P['V1'] + 72) < 1e-9, P['V1']
