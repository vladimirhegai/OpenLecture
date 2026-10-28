r"""Midterm Questions Q1: no series/parallel pair until the Δ (a-b 30, a-c 60, b-c 10) becomes a Y
(18, 3, 6). Then R_in = 30 Ω, i_s = 1 A, and back in the original circuit V_b = 4.5 V, V_c = 3 V -> 0.15 A in the 10 Ω.
Inspired by Textbook P3.58 / Assessment Problem 3.7; numbers chosen so every Y arm is whole."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

TOPIC = 'Δ–Y'
FORMULAS = ['delta_wye']           # the exam's formula sheet, shown under the question
MARKS = 10
TITLE = 'A bridge with no series or parallel pair'
SOURCE = 'Textbook P3.58 and Assessment Problem 3.7'
PROMPT = (r'**(a)** Use a Δ-to-Y transformation to find the resistance $R_{in}$ seen by the $30\,\mathrm{V}$ source. '
          r'**(b)** Find the source current $i_s$. '
          r'**(c)** Find the current in the $10\,\Omega$ resistor, and say which way it flows. '
          r'**(d)** Find the power delivered by the source.')

O = r'\,\Omega'
V = r'\,\mathrm{V}'
A = r'\,\mathrm{A}'

V1 = f'V1 0,3 -> 0,0 "$30{V}$"'
RS = f'RS 0,3 -> 2,3 "$6{O}$" i="$i_s$"'
UP = 'wire 2,3 -> 2,5'
D60 = f'R60 2,5 -> 9,5 "$60{O}$"'
D30 = f'R30 2,3 -> 6,3 "$30{O}$"'
D10 = f'R10 6,3 -> 9,3 "$10{O}$"'
RIGHT = 'wire 9,5 -> 9,3'
R9 = f'R9 6,3 -> 6,0 "$9{O}$"'
R6 = f'R6 9,3 -> 9,0 "$6{O}$"'
BOT = 'wire 0,0 -> 9,0\nground 0,0'
NODES = 'label 2,4 "$a$" left\nlabel 6,3 "$b$" above\nlabel 9,4 "$c$" right'

# Y arms, centre n at 6,5
YA = f'RA 2,5 -> 6,5 "$R_1=18{O}$"'
YC = f'RC 6,5 -> 9,5 "$R_3=6{O}$"'
YB = f'RB 6,5 -> 6,3 "$R_2=3{O}$"'
NLAB = 'label 6,5 "$n$" above'
YNODES = 'label 2,4 "$a$" left\nlabel 6,3 "$b$" right\nlabel 9,4 "$c$" right'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(V1, RS, UP, D60, D30, D10, RIGHT, R9, R6, BOT)
# the Δ in the formula sheet's names: R_c across a-b, R_b across a-c, R_a across b-c (each named for the corner it faces)
NAMED = j(V1, RS, UP, D60.replace('"$60', '"$R_b=60'), D30.replace('"$30', '"$R_c=30'),
          D10.replace('"$10', '"$R_a=10'), RIGHT, R9, R6, BOT)
WYE = j(V1, RS, UP, YA, YC, RIGHT, YB, R9, R6, BOT)
ARMS = [r'#+ $R_1=18\,\Omega$', r'#+ $R_2=3\,\Omega$', r'#+ $R_3=6\,\Omega$']
LEGS = j(V1, RS, UP, YA, f'RBS 6,5 -> 6,0 "$3+9=12{O}$"', 'wire 6,5 -> 9,5', f'RCS 9,5 -> 9,0 "$6+6=12{O}$"', BOT, NLAB)
LOOP = j(V1, RS, UP, YA, f'RP 6,5 -> 6,0 "$6{O}$"', 'wire 0,0 -> 6,0\nground 0,0', NLAB)
SPLIT = j(WYE, YNODES, NLAB, '#= path 6,4.6 -> 6,3.2 -> 6,0.4 "$0.5\\,\\mathrm{A}$" thin',
          '#= path 9,4.6 -> 9,3.2 -> 9,0.4 "$0.5\\,\\mathrm{A}$" thin')

STEPS = [
    ('The circuit', GIVEN, r'''
No two resistors are in series or in parallel.

**Plan**
1. Turn the Δ into a Y → series/parallel works again → $R_{in}$.
2. Ohm's law → $i_s$.
3. Find $V_b$ and $V_c$ in the Y circuit (they are the same nodes), then go back for the $10\,\Omega$.
'''),
    ('Spot the Δ', j(NAMED, NODES, '#= region 1.6,2.6 9.6,5.7 "Δ"'), r'''
$30\,\Omega$, $60\,\Omega$ and $10\,\Omega$ form a triangle between $a$, $b$ and $c$.

That triangle is what blocks every series/parallel move.

**Match the formula sheet:** each Δ resistor is named for the corner it does **not** touch.
- $R_a$: between $b$ and $c$ → $10\,\Omega$
- $R_b$: between $a$ and $c$ → $60\,\Omega$
- $R_c$: between $a$ and $b$ → $30\,\Omega$
'''),
    ('Δ → Y', j(WYE, YNODES, NLAB, *ARMS), r'''
Same corners $a$, $b$, $c$; new centre node $n$. Arm $R_1$ at $a$, $R_2$ at $b$, $R_3$ at $c$.

Formula sheet, Δ → Y. Sum: $R_a+R_b+R_c=10+60+30=100\,\Omega$

$$
R_1=\frac{R_bR_c}{100}=\frac{(60)(30)}{100}=18\,\Omega
$$

$$
R_2=\frac{R_cR_a}{100}=\frac{(30)(10)}{100}=3\,\Omega
$$

$$
R_3=\frac{R_aR_b}{100}=\frac{(10)(60)}{100}=6\,\Omega
$$

Memory check: each arm = (the two Δ resistors touching its corner) ÷ (sum).
'''),
    ('Series legs', LEGS, r'''
From $n$ to the bottom wire there are two paths.

- Through $b$: $R_2+9=3+9=12\,\Omega$
- Through $c$: $R_3+6=6+6=12\,\Omega$
'''),
    ('(a) Parallel, then series', j(LOOP, r'#+ $R_{in}=30\,\Omega$'), r'''
Both legs go from $n$ to the bottom wire → parallel:

$$
12\parallel 12=\frac{(12)(12)}{24}=6\,\Omega
$$

The source now sees one path: $6+R_1+6=6+18+6$.

$$
\boxed{R_{in}=30\,\Omega}
$$
'''),
    ("(b) Ohm's law → $i_s$", j(LOOP, '#= mesh 3,2 "$i_s$" cw r=0.8', r'#+ $i_s=1\,\mathrm{A}$'), r'''
One loop:

$$
-30+6i_s+18i_s+6i_s=0
$$

$$
\boxed{i_s=1\,\mathrm{A}}
$$
'''),
    ('Split at $n$', j(SPLIT, '#= text 7,1.5 "$4.5\\,\\mathrm{V}$" color=pink', '#= text 10,1.5 "$3\\,\\mathrm{V}$" color=pink',
                       r'#+ $V_b=4.5\,\mathrm{V}$', r'#+ $V_c=3\,\mathrm{V}$'), r'''
The two legs are equal ($12\,\Omega$ each) → $1\,\mathrm{A}$ splits evenly, $0.5\,\mathrm{A}$ down each.

The $9\,\Omega$ and $6\,\Omega$ were never touched, so Ohm's law on them gives the real $V_b$ and $V_c$:

$$
V_b=(0.5)(9)=4.5\,\mathrm{V} \qquad V_c=(0.5)(6)=3\,\mathrm{V}
$$
'''),
    ('(c) Back to the Δ', j(GIVEN, NODES, '#= text 6.8,2.4 "$4.5\\,\\mathrm{V}$" color=pink',
                            '#= text 10,2.4 "$3\\,\\mathrm{V}$" color=pink',
                            '#= path 6.3,3 -> 8.7,3 "$0.15\\,\\mathrm{A}$" thin', r'#+ $i_{10}=0.15\,\mathrm{A}$'), r'''
The Y was only a trick. The $10\,\Omega$ lives in the **original** circuit, between $b$ and $c$.

Current flows high → low, $b$ → $c$:

$$
i_{10}=\frac{V_b-V_c}{10}=\frac{4.5-3}{10}
$$

$$
\boxed{i_{10}=0.15\,\mathrm{A}\ \text{from}\ b\ \text{to}\ c}
$$

Check at $b$: in from $30\,\Omega$ $=\frac{24-4.5}{30}=0.65$; out $0.5+0.15=0.65$ ✓ ($V_a=30-6=24\,\mathrm{V}$).
'''),
    ('(d) Source power', j(GIVEN, '#= mesh 1,1.5 "$1\\,\\mathrm{A}$" cw r=0.5', r'#+ $P=30\,\mathrm{W}$'), r'''
$i_s=1\,\mathrm{A}$ leaves the $+$ terminal:

$$
\boxed{P=(30)(1)=30\,\mathrm{W}\ \text{delivered}}
$$
'''),
]


NET = [('V', 'V1', 's', '0', 30), ('R', 'RS', 's', 'a', 6), ('R', 'R60', 'a', 'c', 60), ('R', 'R30', 'a', 'b', 30),
       ('R', 'R10', 'b', 'c', 10), ('R', 'R9', 'b', '0', 9), ('R', 'R6', 'c', '0', 6)]


def checks(check):
    els, _ = check(GIVEN)
    s, a = els['RS']
    b, c = els['R10']
    assert els['V1'] == (s, '0') and els['R60'] == (a, c) and els['R30'] == (a, b), els
    assert els['R9'] == (b, '0') and els['R6'] == (c, '0'), els
    w, _ = check(WYE)
    n = w['RA'][1]
    assert w['RA'][0] == w['RS'][1] and w['RB'] == (n, w['R9'][0]) and w['RC'][0] == n, w
    assert w['RC'][1] == w['R6'][0], w
    assert check(NAMED)[0] == els
    for d in (LEGS, LOOP):
        check(d)
    S = 30 + 60 + 10
    assert (F(30 * 60, S), F(30 * 10, S), F(60 * 10, S)) == (18, 3, 6)
    assert F(12 * 12, 24) == 6 and 6 + 18 + 6 == 30
    i = F(30, 30)
    assert -30 + 30 * i == 0 and i == 1
    Vb, Vc = F(1, 2) * 9, F(1, 2) * 6
    assert (Vb, Vc) == (F(9, 2), 3) and (Vb - Vc) / 10 == F(3, 20)
    assert (24 - Vb) / 30 == F(13, 20) == F(1, 2) + F(3, 20)
    Vn, I, P = solve(NET)
    assert abs(I['RS'] - 1) < 1e-9 and abs(Vn['b'] - 4.5) < 1e-9 and abs(Vn['c'] - 3) < 1e-9
    assert abs(I['R10'] - 0.15) < 1e-9 and abs(I['V1'] + 1) < 1e-9 and abs(P['V1'] + 30) < 1e-9, (I['V1'], P['V1'])
