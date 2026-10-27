r"""ELEC 221 Midterm Fall 2025, Question 1: Thévenin seen by R_L, matched load, maximum power.
V_Th by mesh + Ohm (the 3 A source sits between two windows -> supermesh), R_Th with sources off.
R_L is drawn straight instead of diagonal (same nodes, asserted)."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'M'
TITLE = 'Q1: Thévenin and maximum power'
SOURCE = 'ELEC 221 Midterm, Fall 2025, Question 1 (Fig. P1)'
PROMPT = (r'**(a)** Find the Thévenin equivalent circuit seen by $R_L$. '
          r'**(b)** Find the $R_L$ that receives the maximum power. '
          r'**(c)** With this $R_L$, find the maximum power delivered to $R_L$.'
          '\n\n'
          r'*$R_L$ is drawn straight here instead of diagonal: it still goes from the top-right node $a$ '
          r'down to the bottom wire $b$.*')

O = r'\,\Omega'
V = r'\,\mathrm{V}'
A = r'\,\mathrm{A}'

V1 = f'V1 0,3 -> 0,0 "$5{V}$"'
R2A = f'R2A 0,3 -> 3,3 "$2{O}$"'
R4 = '\n'.join(['wire 0,3 -> 0,5', f'R4 0,5 -> 6,5 "$4{O}$"', 'wire 6,5 -> 6,3'])
I1 = f'I1 3,0 -> 3,3 "$3{A}$"'
R2B = f'R2B 3,3 -> 6,3 "$2{O}$"'
RL = f'RL 6,3 -> 6,0 "$R_L=12{O}$" v="$V_L$"'
RIGHT = '\n'.join(['wire 6,3 -> 9,3', f'R1 9,3 -> 9,0 "$1{O}$"', f'R5 9,0 -> 6,0 "$5{O}$"'])
BOTTOM = 'wire 0,0 -> 6,0'
LABELS = '\n'.join(['label 7,3 "$a$" above', 'label 6,0 "$b$" below', 'ground 0,0'])


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(V1, R2A, R4, I1, R2B, RL, RIGHT, BOTTOM, LABELS)
OPEN = j(V1, R2A, R4, I1, R2B, RIGHT, BOTTOM, LABELS, 'gap 6,3 -> 6,0 v="$V_{oc}$"')
OFF = j('wire 0,3 -> 0,0', R2A, R4, R2B, RIGHT, BOTTOM, LABELS)
PAR = j(f'RA 2,3 -> 2,0 "$4{O}$"', f'RB 5,3 -> 5,0 "$2+2=4{O}$"', f'RC 8,3 -> 8,0 "$1+5=6{O}$"',
        'wire 2,3 -> 10,3', 'wire 2,0 -> 10,0', 'terminal 10,3 "$a$" right', 'terminal 10,0 "$b$" right')
TH = j(f'VTH 0,3 -> 0,0 "$6{V}$"', f'RTH 0,3 -> 3,3 "$1.5{O}$"', 'wire 3,3 -> 8,3', 'wire 0,0 -> 8,0',
       'terminal 8,3 "$a$" right', 'terminal 8,0 "$b$" right')

MESHES = j('#= mesh 1.5,1.5 "$I_1$" cw r=0.7', '#= mesh 3,4 "$I_2$" cw r=0.5', '#= mesh 4.5,1.5 "$I_3$" cw r=0.6')
CONSTRAINT = '#= text 3,-0.8 "$I_3-I_1=3$" color=purple'
WALK = '#= path 0,0 -> 0,3 -> 6,3 -> 9,3 -> 9,0 -> 6,0 -> 0.45,0'
SIGNS_SUPER = j('#= sign 0.5,2.6 +', '#= sign 2.5,2.6 -',       # 2 Ω left: walk goes right
                '#= sign 3.5,2.6 +', '#= sign 5.5,2.6 -',       # 2 Ω right: walk goes right
                '#= sign 9.4,2.4 +', '#= sign 9.4,0.6 -',       # 1 Ω: walk goes down
                '#= sign 8.5,-0.4 +', '#= sign 6.5,-0.4 -')     # 5 Ω: walk goes left
SIGNS_2 = j('#= sign 0.5,4.6 +', '#= sign 5.5,4.6 -',           # 4 Ω: I_2 goes right
            '#= sign 5.5,3.4 +', '#= sign 3.5,3.4 -',           # 2 Ω right: I_2 goes left
            '#= sign 2.5,3.4 +', '#= sign 0.5,3.4 -')           # 2 Ω left: I_2 goes left
SIGNS_OUT = j('#= sign 9.4,2.4 +', '#= sign 9.4,0.6 -', '#= sign 8.5,-0.4 +', '#= sign 6.5,-0.4 -')

STEPS = [
    ('The circuit', GIVEN, r'''
$R_L$ is the **load**: Thévenin replaces everything else with one source and one resistor.

**Plan**
1. Pull out $R_L$ → $V_{Th}=V_{oc}$ with mesh + Ohm.
2. $R_{Th}$: sources off, look in from $a$–$b$.
3. Max power: $R_L=R_{Th}$, then $P_{max}$.
'''),
    ('Pull out the load', OPEN, r'''
$R_L$ is gone → $a$–$b$ is **open**. The voltage across it is $V_{oc}=V_{Th}$.

The $1\,\Omega$ and $5\,\Omega$ **stay**: they are part of the circuit, not the load.
'''),
    ('Mesh currents', j(OPEN, MESHES, CONSTRAINT), r'''
Three windows → $I_1$, $I_2$, $I_3$, all clockwise.

The $3\,\mathrm{A}$ sits between $I_1$ and $I_3$ → **supermesh**.

Its arrow points **up**:
- $I_3$ goes up through it → $+I_3$
- $I_1$ goes down through it → $-I_1$

$$
I_3-I_1=3
$$
'''),
    ('KVL around the supermesh', j(OPEN, MESHES, CONSTRAINT, WALK, SIGNS_SUPER), r'''
Walk around $I_1$ and $I_3$ **together**, skipping the $3\,\mathrm{A}$ branch.

Sign you **enter** each element by:
- $5\,\mathrm{V}$: enter $-$ → $-5$
- $2\,\Omega$ left (shared with $I_2$): $+2(I_1-I_2)$
- $2\,\Omega$ right (shared with $I_2$): $+2(I_3-I_2)$
- $1\,\Omega$ and $5\,\Omega$: $+1I_3$, $+5I_3$

$$
-5+2(I_1-I_2)+2(I_3-I_2)+6I_3=0
$$

$$
2I_1-4I_2+8I_3=5
$$
'''),
    ('KVL in mesh $I_2$', j(OPEN, MESHES, CONSTRAINT, SIGNS_2), r'''
Walk with $I_2$ (right along the top, back left through the two $2\,\Omega$):

$$
4I_2+2(I_2-I_3)+2(I_2-I_1)=0
$$

$$
-2I_1+8I_2-2I_3=0
$$
'''),
    ('Solve', j(OPEN, MESHES, r'#+ $I_1=-2\,\mathrm{A}$', r'#+ $I_2=-0.25\,\mathrm{A}$', r'#+ $I_3=1\,\mathrm{A}$'), r'''
Put $I_1=I_3-3$ into both:

$$
10I_3-4I_2=11 \qquad 8I_2=4I_3-6
$$

Second one: $4I_2=2I_3-3$. Into the first:

$$
10I_3-(2I_3-3)=11 \;\Rightarrow\; 8I_3=8
$$

$$
I_3=1\,\mathrm{A} \qquad I_2=-0.25\,\mathrm{A} \qquad I_1=-2\,\mathrm{A}
$$

(Or type the 3 equations into the fx-991 equation solver.)
'''),
    ('KVL walk to $V_{oc}$', j(OPEN, SIGNS_OUT, '#= path 6,3 -> 9,3 -> 9,0 -> 6.4,0',
                                '#= text 8.3,1.5 "$1\\,\\mathrm{V}$" color=pink',
                                '#= text 7.5,-1 "$5\\,\\mathrm{V}$" color=pink', r'#+ $V_{Th}=6\,\mathrm{V}$'), r'''
Only $I_3=1\,\mathrm{A}$ runs through the $1\,\Omega$ and $5\,\Omega$. Ohm's law:

$$
V_{1\Omega}=(1)(1)=1\,\mathrm{V} \qquad V_{5\Omega}=(5)(1)=5\,\mathrm{V}
$$

Walk from $a$ to $b$ that way; you enter both at $+$:

$$
\boxed{V_{Th}=V_{oc}=1+5=6\,\mathrm{V}}
$$
'''),
    ('$R_{Th}$: sources off', j(OFF, '#= text 6.6,1.5 "$R_{Th}$" color=accent'), r'''
- $5\,\mathrm{V}$ → **wire**
- $3\,\mathrm{A}$ → **open** (gone)

Now the left ends of the $4\,\Omega$ and the left $2\,\Omega$ are wired straight to $b$.
'''),
    ('Three paths from $a$ to $b$', j(PAR, r'#+ $R_{Th}=1.5\,\Omega$'), r'''
- $4\,\Omega$: from $a$ straight to $b$.
- $2\,\Omega+2\,\Omega$: the middle node touches only these two now → series, $4\,\Omega$.
- $1\,\Omega+5\,\Omega$: series, $6\,\Omega$.

All three go from $a$ to $b$ → parallel:

$$
4\parallel 4=2\,\Omega \qquad 2\parallel 6=\frac{(2)(6)}{2+6}
$$

$$
\boxed{R_{Th}=1.5\,\Omega}
$$
'''),
    ('(a) Thévenin circuit', TH, r'''
$$
V_{Th}=6\,\mathrm{V}\ \text{in series with}\ R_{Th}=1.5\,\Omega
$$

This is all $R_L$ "sees".
'''),
    ('(b), (c) Matched load', j(TH, f'RL 6,3 -> 6,0 "$R_L=1.5{O}$"', '#= mesh 3,1.5 "$I$" cw r=0.8',
                                 '#= sign 0.6,2.62 +', '#= sign 2.4,2.62 -', '#= sign 5.65,2.3 +', '#= sign 5.65,0.7 -',
                                 r'#+ $R_L=1.5\,\Omega$', r'#+ $P_{max}=6\,\mathrm{W}$'), r'''
Max power when the load matches: $\boxed{R_L=R_{Th}=1.5\,\Omega}$

Mesh on the Thévenin circuit:

$$
-6+1.5I+1.5I=0 \;\Rightarrow\; I=2\,\mathrm{A}
$$

$$
\boxed{P_{max}=I^2R_L=(2)^2(1.5)=6\,\mathrm{W}}
$$

Formula check: $\dfrac{V_{Th}^2}{4R_{Th}}=\dfrac{36}{6}=6\,\mathrm{W}$ ✓

The drawn $12\,\Omega$ would get only $(6/13.5)^2(12)=2.37\,\mathrm{W}$.
'''),
]


NET = [('V', 'V1', 'A', '0', 5), ('R', 'R2A', 'A', 'm', 2), ('R', 'R4', 'A', 'a', 4), ('I', 'I1', '0', 'm', 3),
       ('R', 'R2B', 'm', 'a', 2), ('R', 'R1', 'a', 'c', 1), ('R', 'R5', 'c', '0', 5)]


def checks(check):
    els, _ = check(GIVEN)
    top, a = els['V1'][0], els['RL'][0]
    m, c = els['R2A'][1], els['R1'][1]
    assert els['V1'][1] == '0' and els['RL'][1] == '0' and els['R5'] == (c, '0'), els
    assert els['R2A'][0] == top and els['R4'] == (top, a) and els['I1'] == ('0', m), els
    assert els['R2B'] == (m, a) and els['R1'] == (a, c), els
    for d in (OPEN, OFF, PAR, TH):
        check(d)
    # mesh equations
    I1, I2, I3 = F(-2), F(-1, 4), F(1)
    assert I3 - I1 == 3
    assert -5 + 2 * (I1 - I2) + 2 * (I3 - I2) + 6 * I3 == 0 and 2 * I1 - 4 * I2 + 8 * I3 == 5
    assert 4 * I2 + 2 * (I2 - I3) + 2 * (I2 - I1) == 0 and -2 * I1 + 8 * I2 - 2 * I3 == 0
    assert 10 * I3 - 4 * I2 == 11 and 8 * I2 == 4 * I3 - 6 and 4 * I2 == 2 * I3 - 3
    # against an independent nodal solve
    Vn, I, _ = solve(NET)
    assert abs(Vn['a'] - 6) < 1e-9 and abs(I['R1'] - I3) < 1e-9 and abs(I['R4'] - I2) < 1e-9
    assert abs(I['R2A'] - (I1 - I2)) < 1e-9
    # R_Th by a 1 V test source with sources off
    _, It, _ = solve([('V', 'V1', 'A', '0', 0), ('R', 'R2A', 'A', 'm', 2), ('R', 'R4', 'A', 'a', 4),
                      ('R', 'R2B', 'm', 'a', 2), ('R', 'R1', 'a', 'c', 1), ('R', 'R5', 'c', '0', 5),
                      ('V', 'VT', 'a', '0', 1)])
    assert abs(1 / -It['VT'] - 1.5) < 1e-9
    assert F(4 * 4, 8) == 2 and F(2 * 6, 8) == F(3, 2)
    # matched load
    Vl, Il, Pl = solve(NET + [('R', 'RL', 'a', '0', 1.5)])
    assert abs(Il['RL'] - 2) < 1e-9 and abs(Pl['RL'] - 6) < 1e-9 and F(36, 6) == 6
    _, _, P12 = solve(NET + [('R', 'RL', 'a', '0', 12)])
    assert abs(P12['RL'] - 2.37) < 0.005
