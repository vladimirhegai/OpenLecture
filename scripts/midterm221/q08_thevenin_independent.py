r"""Midterm Questions Q8: Thévenin at a-b with independent sources only (40 V, 2 A on the shared wall -> supermesh).
I_1 = 2 A, I_2 = 4 A; walk a -> b: 0 V on the 3 Ω (no current, a-b open) + (6)(4) = 24 V. R_Th = (4+2) || 6 + 3 = 6 Ω.
Then use it: R_L = 10 Ω draws 1.5 A; an 18 Ω voltmeter reads 18 V instead of 24 V (it loads the circuit).
Inspired by Tutorial 4 Problem 3.2, Textbook P4.68 (voltmeter) and the Fall 2025 Q1 supermesh."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

TOPIC = 'Thévenin (independent sources only)'
MARKS = 10
TITLE = 'Thévenin: an open port, then a load and a meter'
SOURCE = 'Tutorial 4 Problem 3.2, Textbook P4.68 and Fall 2025 Question 1'
PROMPT = (r'**(a)** Find the Thévenin equivalent of the circuit at the terminals $a$–$b$. '
          r'**(b)** A load resistor $R_L$ is connected from $a$ to $b$. What value of $R_L$ draws $i_L=1.5\,\mathrm{A}$? '
          r'**(c)** Instead of $R_L$, a voltmeter with internal resistance $18\,\Omega$ is connected from $a$ to $b$. '
          r'What does it read? Compare it with the open-circuit voltage.')

O = r'\,\Omega'
V = r'\,\mathrm{V}'
A = r'\,\mathrm{A}'

V1 = f'V1 0,3 -> 0,0 "$40{V}$"'
R1 = f'R1 0,3 -> 3,3 "$4{O}$"'
I1 = f'I1 3,0 -> 3,3 "$2{A}$"'
R2 = f'R2 3,3 -> 6,3 "$2{O}$"'
R3 = f'R3 6,3 -> 6,0 "$6{O}$"'
R4 = f'R4 6,3 -> 9,3 "$3{O}$"'
TERMS = '\n'.join(['terminal 9,3 "$a$" right', 'wire 0,0 -> 9,0', 'terminal 9,0 "$b$" right', 'ground 0,0'])
NODE = 'label 6,3 "$c$" above'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(V1, R1, I1, R2, R3, R4, TERMS, NODE)
OPEN = j(GIVEN, 'gap 9,3 -> 9,0 v="$V_{oc}$"')
MESHES = j('#= mesh 1.3,1.5 "$I_1$" cw r=0.5', '#= mesh 4.4,1.5 "$I_2$" cw r=0.55')
CONSTRAINT = '#= text 3,-0.8 "$I_2-I_1=2$" color=purple'
WALK = '#= path 0,0 -> 0,3 -> 3,3 -> 6,3 -> 6,0 -> 0.45,0'
SIGNS_SUPER = j('#= sign 0.5,2.6 +', '#= sign 2.5,2.6 -',       # 4 Ω: the walk goes right
                '#= sign 3.5,2.6 +', '#= sign 5.5,2.6 -',       # 2 Ω: the walk goes right
                '#= sign 6.4,2.4 +', '#= sign 6.4,0.6 -')       # 6 Ω: the walk goes down
OFF = j('wire 0,3 -> 0,0', R1, R2, R3, R4, TERMS, NODE)
SER = j(f'RS 3,3 -> 3,0 "$4+2=6{O}$"', 'wire 3,3 -> 6,3', R3, R4, 'terminal 9,3 "$a$" right', 'wire 3,0 -> 9,0',
        'terminal 9,0 "$b$" right', NODE)
PAR = j(f'RP 6,3 -> 6,0 "$6\\parallel 6=3{O}$"', R4, 'terminal 9,3 "$a$" right', 'wire 6,0 -> 9,0',
        'terminal 9,0 "$b$" right', NODE)
TH = j(f'VTH 0,3 -> 0,0 "$24{V}$"', f'RTH 0,3 -> 3,3 "$6{O}$"', 'wire 3,3 -> 9,3', 'wire 0,0 -> 9,0',
       'terminal 9,3 "$a$" right', 'terminal 9,0 "$b$" right')
LOOP_SIGNS = j('#= sign 0.6,2.62 +', '#= sign 2.4,2.62 -', '#= sign 5.65,2.3 +', '#= sign 5.65,0.7 -')

STEPS = [
    ('The circuit', GIVEN, r'''
Thévenin equivalent = one source $V_{Th}$ in series with one resistor $R_{Th}$.

**Plan**
1. $V_{Th}=V_{oc}$: mesh + Ohm, then a KVL walk from $a$ to $b$.
2. $R_{Th}$: sources off, look in from $a$–$b$.
3. Use the small circuit for the load and the meter.
'''),
    ('Mesh currents', j(OPEN, MESHES, CONSTRAINT), r'''
$a$–$b$ is **open**: no current in the $3\,\Omega$. So only two windows carry current: $I_1$, $I_2$, clockwise.

The $2\,\mathrm{A}$ sits between them → **supermesh**.

Its arrow points **up**:
- $I_2$ goes up through it → $+I_2$
- $I_1$ goes down through it → $-I_1$

$$
I_2-I_1=2
$$
'''),
    ('KVL around the supermesh', j(OPEN, MESHES, CONSTRAINT, WALK, SIGNS_SUPER,
                                   r'#+ $I_1=2\,\mathrm{A}$', r'#+ $I_2=4\,\mathrm{A}$'), r'''
Walk around $I_1$ and $I_2$ **together**, skipping the $2\,\mathrm{A}$ branch.

Sign you **enter** each element by:
- $40\,\mathrm{V}$: enter $-$ → $-40$
- $4\,\Omega$: $+4I_1$
- $2\,\Omega$ and $6\,\Omega$: $+2I_2$, $+6I_2$

$$
-40+4I_1+8I_2=0
$$

Put in $I_2=I_1+2$:

$$
4I_1+8I_1+16=40 \;\Rightarrow\; I_1=2\,\mathrm{A} \qquad I_2=4\,\mathrm{A}
$$
'''),
    ('KVL walk to $V_{oc}$', j(OPEN, '#= path 9,3 -> 6,3 -> 6,0 -> 8.6,0', '#= sign 6.4,2.4 +', '#= sign 6.4,0.6 -',
                                '#= text 7.5,3.9 "$0\\,\\mathrm{V}$" color=pink',
                                '#= text 7.2,1.5 "$24\\,\\mathrm{V}$" color=pink', r'#+ $V_{Th}=24\,\mathrm{V}$'), r'''
Walk from $a$ to $b$: through the $3\,\Omega$, then down the $6\,\Omega$.

- $3\,\Omega$: no current (open port) → $(3)(0)=0\,\mathrm{V}$
- $6\,\Omega$: $I_2=4\,\mathrm{A}$ enters at the top → $+(6)(4)=+24\,\mathrm{V}$

$$
\boxed{V_{Th}=V_{oc}=0+24=24\,\mathrm{V}}
$$
'''),
    ('$R_{Th}$: sources off', j(OFF, '#= text 9.8,1.5 "$R_{Th}$" color=accent'), r'''
- $40\,\mathrm{V}$ → **wire**
- $2\,\mathrm{A}$ → **open** (gone)

Now the left end of the $4\,\Omega$ is wired straight to $b$.
'''),
    ('Series', SER, r'''
With the $2\,\mathrm{A}$ gone, the node between $4\,\Omega$ and $2\,\Omega$ touches only those two → **series**:

$$
4+2=6\,\Omega
$$

It runs from $c$ down to $b$.
'''),
    ('Parallel, then series', j(PAR, r'#+ $R_{Th}=6\,\Omega$'), r'''
$6\,\Omega$ and $6\,\Omega$ both go from $c$ to $b$ → parallel:

$$
6\parallel 6=\frac{(6)(6)}{6+6}=3\,\Omega
$$

Then the $3\,\Omega$ to $a$ is in series:

$$
\boxed{R_{Th}=3+3=6\,\Omega}
$$
'''),
    ('(a) Thévenin circuit', TH, r'''
$$
V_{Th}=24\,\mathrm{V}\ \text{in series with}\ R_{Th}=6\,\Omega
$$

Whatever you connect to $a$–$b$ sees only this.
'''),
    ('(b) Load for $1.5\\,\\mathrm{A}$', j(TH, f'RL 6,3 -> 6,0 "$R_L$"', '#= mesh 3,1.5 "$i_L$" cw r=0.8', LOOP_SIGNS,
                                          r'#+ $R_L=10\,\Omega$'), r'''
One loop. KVL with $i_L=1.5\,\mathrm{A}$:

$$
-24+6(1.5)+R_L(1.5)=0
$$

$$
1.5R_L=15 \;\Rightarrow\; \boxed{R_L=10\,\Omega}
$$

Without Thévenin you would redo the supermesh with $R_L$ unknown.
'''),
    ('(c) The meter loads the circuit', j(TH, f'RM 6,3 -> 6,0 "$18{O}$" v="$v_m$"', '#= mesh 3,1.5 "$i$" cw r=0.8',
                                          LOOP_SIGNS, r'#+ $v_m=18\,\mathrm{V}$'), r'''
The meter is just an $18\,\Omega$ resistor across $a$–$b$.

$$
-24+6i+18i=0 \;\Rightarrow\; i=1\,\mathrm{A}
$$

$$
\boxed{v_m=(18)(1)=18\,\mathrm{V}}
$$

The true open-circuit voltage is $24\,\mathrm{V}$: the meter reads $6\,\mathrm{V}$ ($25\,\%$) low, because it draws current through $R_{Th}$.
'''),
]


NET = [('V', 'V1', 's', '0', 40), ('R', 'R1', 's', 'm', 4), ('I', 'I1', '0', 'm', 2), ('R', 'R2', 'm', 'c', 2),
       ('R', 'R3', 'c', '0', 6), ('R', 'R4', 'c', 'a', 3)]


def checks(check):
    els, _ = check(GIVEN)
    s, m = els['R1']
    c, a = els['R4']
    assert els['V1'] == (s, '0') and els['I1'] == ('0', m) and els['R2'] == (m, c) and els['R3'] == (c, '0'), els
    assert a not in (s, m, c, '0'), els
    for d in (OPEN, OFF, SER, PAR, TH):
        check(d)
    # supermesh
    I1, I2 = F(2), F(4)
    assert I2 - I1 == 2 and -40 + 4 * I1 + 8 * I2 == 0
    assert 4 * I1 + 8 * I1 + 16 == 40
    Vth = 0 + 6 * I2
    assert Vth == 24
    # R_Th
    assert 4 + 2 == 6 and F(6 * 6, 12) == 3 and 3 + 3 == 6
    # (b), (c)
    assert -24 + 6 * F(3, 2) + 10 * F(3, 2) == 0
    assert F(24, 24) == 1 and 18 * 1 == 18
    # independent nodal solve of the original circuit
    Vn, I, _ = solve(NET)
    assert abs(Vn['a'] - 24) < 1e-9 and abs(I['R3'] - 4) < 1e-9 and abs(I['R1'] - 2) < 1e-9
    _, It, _ = solve([('V', 'V1', 's', '0', 0), ('R', 'R1', 's', 'm', 4), ('R', 'R2', 'm', 'c', 2),
                      ('R', 'R3', 'c', '0', 6), ('R', 'R4', 'c', 'a', 3), ('V', 'VT', 'a', '0', 1)])
    assert abs(1 / -It['VT'] - 6) < 1e-9
    _, Il, _ = solve(NET + [('R', 'RL', 'a', '0', 10)])
    assert abs(Il['RL'] - 1.5) < 1e-9
    Vm, _, _ = solve(NET + [('R', 'RM', 'a', '0', 18)])
    assert abs(Vm['a'] - 18) < 1e-9
