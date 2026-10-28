r"""Midterm Questions Q6: three windows in a row, a CCVS 4 i_x on the wall between windows 2 and 3, controlled by
the current i_x down the shared 2 Ω. (a) three KVL + the control equation i_x = I1 - I2, (b) I1 = 2, I2 = -2,
I3 = 1 A, i_x = 4 A, (c) the 16 V dependent source delivers 48 W. Inspired by Fall 2025 Q4 and Textbook P4.47."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

TOPIC = 'Mesh analysis'
MARKS = 10
TITLE = 'A dependent source on the middle wall'
SOURCE = 'Fall 2025 Question 4 and Textbook P4.47'
PROMPT = (r'**(a)** Write (but do not solve) the mesh-current equations for the circuit, including the equation '
          r'for the dependent source. **(b)** Solve for $i_x$. '
          r'**(c)** Find the power of the dependent source, and say whether it absorbs or delivers.')

O = r'\,\Omega'
V = r'\,\mathrm{V}'

V1 = f'V1 0,3 -> 0,0 "$24{V}$"'
R1 = f'R1 0,3 -> 3,3 "$8{O}$"'
R2 = f'R2 3,3 -> 3,0 "$2{O}$" i="$i_x$"'
R3 = f'R3 3,3 -> 6,3 "$4{O}$"'
E1 = 'E1 6,3 -> 6,0 "$4i_x$"'
R4 = f'R4 6,3 -> 9,3 "$6{O}$"'
R5 = f'R5 9,3 -> 9,0 "$10{O}$"'
BOT = 'wire 0,0 -> 9,0\nground 0,0'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(V1, R1, R2, R3, E1, R4, R5, BOT)

MESHES = j('#= mesh 1.5,1.5 "$I_1$" cw r=0.6', '#= mesh 4.5,1.5 "$I_2$" cw r=0.6', '#= mesh 7.5,1.5 "$I_3$" cw r=0.6')
SIGNS_1 = j('#= sign 0.75,2.6 +', '#= sign 2.25,2.6 -',           # 8 Ω: I_1 goes right
            '#= sign 2.6,2.05 +', '#= sign 2.6,0.95 -')           # 2 Ω: I_1 goes down
SIGNS_2 = j('#= sign 3.4,0.95 +', '#= sign 3.4,2.05 -',           # 2 Ω: I_2 goes up
            '#= sign 3.75,2.6 +', '#= sign 5.25,2.6 -')           # 4 Ω: I_2 goes right
SIGNS_3 = j('#= sign 6.75,2.6 +', '#= sign 8.25,2.6 -',           # 6 Ω: I_3 goes right
            '#= sign 8.6,2.05 +', '#= sign 8.6,0.95 -')           # 10 Ω: I_3 goes down
FOUND = [r'#+ $I_1=2\,\mathrm{A}$', r'#+ $I_2=-2\,\mathrm{A}$', r'#+ $I_3=1\,\mathrm{A}$', r'#+ $i_x=4\,\mathrm{A}$']

STEPS = [
    ('The circuit', GIVEN, r'''
**Method: mesh.** Three windows, no current sources → one KVL per window.

The $4i_x$ source is **dependent** → one extra equation that writes $i_x$ in mesh currents.
'''),
    ('Mesh currents', j(GIVEN, MESHES), r'''
$I_1$, $I_2$, $I_3$, all clockwise.

Treat $4i_x$ like a normal voltage source while writing KVL; deal with $i_x$ at the end.
'''),
    ('KVL in mesh $I_1$', j(GIVEN, MESHES, SIGNS_1), r'''
Sign you **enter** each element by:
- $24\,\mathrm{V}$: enter $-$ → $-24$
- $8\,\Omega$: $+8I_1$
- $2\,\Omega$ (shared with $I_2$): $+2(I_1-I_2)$

$$
-24+8I_1+2(I_1-I_2)=0
$$
'''),
    ('KVL in mesh $I_2$', j(GIVEN, MESHES, SIGNS_2), r'''
- $2\,\Omega$ (going up, shared with $I_1$): $+2(I_2-I_1)$
- $4\,\Omega$: $+4I_2$
- $4i_x$ (going down): enter $+$ → $+4i_x$

$$
2(I_2-I_1)+4I_2+4i_x=0
$$
'''),
    ('KVL in mesh $I_3$', j(GIVEN, MESHES, SIGNS_3), r'''
- $6\,\Omega$ and $10\,\Omega$: $+6I_3+10I_3$
- $4i_x$ (going up): enter $-$ → $-4i_x$

$$
16I_3-4i_x=0
$$
'''),
    ('(a) The control equation', j(GIVEN, MESHES, '#= path 3,2.6 -> 3,0.4 thin color=orange'), r'''
$i_x$ flows **down** the $2\,\Omega$. There $I_1$ goes down and $I_2$ goes up:

$$
i_x=I_1-I_2
$$

**(a) answer:** four equations, four unknowns.

$$
\begin{aligned}
-24+8I_1+2(I_1-I_2)&=0\\
2(I_2-I_1)+4I_2+4i_x&=0\\
16I_3-4i_x&=0\\
i_x&=I_1-I_2
\end{aligned}
$$
'''),
    ('(b) Solve', j(GIVEN, MESHES, *FOUND), r'''
Put $i_x=I_1-I_2$ into mesh 2:

$$
2I_2-2I_1+4I_2+4I_1-4I_2=0 \;\Rightarrow\; 2I_1+2I_2=0
$$

So $I_2=-I_1$. Mesh 1 is $10I_1-2I_2=24$:

$$
12I_1=24 \;\Rightarrow\; I_1=2\,\mathrm{A} \qquad I_2=-2\,\mathrm{A}
$$

$$
\boxed{i_x=I_1-I_2=4\,\mathrm{A}}
$$

Mesh 3: $16I_3=4(4)$ → $I_3=1\,\mathrm{A}$.

Check with Ohm: top of the $2\,\Omega$ is $(2)(4)=8\,\mathrm{V}$, so the $8\,\Omega$ carries $\frac{24-8}{8}=2\,\mathrm{A}=I_1$ ✓
'''),
    ('(c) Power of $4i_x$', j(GIVEN, '#= text 7.0,2.1 "$16\\,\\mathrm{V}$" color=pink',
                              '#= text 7.0,0.9 "$3\\,\\mathrm{A}\\uparrow$" color=pink', *FOUND,
                              r'#+ $p_{dep}=48\,\mathrm{W}\ \text{del.}$'), r'''
Its voltage: $4i_x=4(4)=16\,\mathrm{V}$, $+$ on top.

Current down through it: $I_2-I_3=-2-1=-3\,\mathrm{A}$ → $3\,\mathrm{A}$ flows **up**, out of the $+$ → it **delivers**:

$$
\boxed{p_{dep}=(16)(3)=48\,\mathrm{W}\ \text{delivered}}
$$

Balance: $24\,\mathrm{V}$ delivers $(24)(2)=48$; resistors take $32+32+16+6+10=96=48+48$ ✓
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    s, a = els['R1']
    b, c = els['R4']
    assert els['V1'] == (s, '0') and els['R2'] == (a, '0') and els['R3'] == (a, b), els   # i_x: a -> ground
    assert els['E1'] == (b, '0') and els['R5'] == (c, '0'), els
    I1, I2, I3 = F(2), F(-2), F(1)
    ix = I1 - I2
    assert ix == 4
    assert -24 + 8 * I1 + 2 * (I1 - I2) == 0 and 10 * I1 - 2 * I2 == 24
    assert 2 * (I2 - I1) + 4 * I2 + 4 * ix == 0 and 2 * I1 + 2 * I2 == 0
    assert 16 * I3 - 4 * ix == 0 and 12 * I1 == 24
    assert 2 * ix == 8 and (24 - 8) / F(8) == I1
    assert 4 * ix == 16 and I2 - I3 == -3 and 16 * 3 == 48
    pr = 8 * I1 ** 2 + 2 * ix ** 2 + 4 * I2 ** 2 + 6 * I3 ** 2 + 10 * I3 ** 2
    assert (8 * I1 ** 2, 2 * ix ** 2, 4 * I2 ** 2, 6 * I3 ** 2, 10 * I3 ** 2) == (32, 32, 16, 6, 10)
    assert pr == 96 == 24 * I1 + 48
    Vn, I, P = solve([('V', 'V1', 's', '0', 24), ('R', 'R1', 's', 'a', 8), ('R', 'R2', 'a', '0', 2),
                      ('R', 'R3', 'a', 'b', 4), ('E', 'E1', 'b', '0', {'a': 4 / 2}, 0),
                      ('R', 'R4', 'b', 'c', 6), ('R', 'R5', 'c', '0', 10)])
    assert abs(I['R2'] - 4) < 1e-9 and abs(I['R1'] - 2) < 1e-9 and abs(I['R3'] + 2) < 1e-9 and abs(I['R4'] - 1) < 1e-9
    assert abs(Vn['b'] - 16) < 1e-9 and abs(P['E1'] + 48) < 1e-9, P['E1']
