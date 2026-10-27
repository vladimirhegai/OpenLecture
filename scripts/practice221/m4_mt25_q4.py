r"""ELEC 221 Midterm Fall 2025, Question 4: (a) write the mesh equations (supermesh around the shared 2 A source,
plus the control equation of the 5 i_Δ source), (b) solve for i_Δ, then check with Ohm's law."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'M'
TITLE = 'Q4: Dependent source, equations then solve'
SOURCE = 'ELEC 221 Midterm, Fall 2025, Question 4'
PROMPT = (r'**(a)** Write (but do not solve) the set of simultaneous equations needed to solve the circuit, using '
          r'either the node-voltage or the mesh-current method. **(b)** Solve for $i_\Delta$ any way you choose.')

O = r'\,\Omega'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j('E1 0,3 -> 0,0 "$5i_\\Delta$"', 'wire 0,3 -> 0,5', f'RT 6,5 -> 0,5 "$10{O}$" i="$i_\\Delta$"',
          'wire 6,5 -> 6,3', f'RA 0,3 -> 3,3 "$10{O}$"', f'RB 3,3 -> 6,3 "$10{O}$"',
          'I1 3,0 -> 3,3 "$2\\,\\mathrm{A}$"', f'R30 6,3 -> 6,0 "$30{O}$"', 'wire 0,0 -> 6,0', 'ground 0,0')

MESHES = j('#= mesh 1.5,1.5 "$I_1$" cw r=0.7', '#= mesh 4.5,1.5 "$I_2$" cw r=0.7', '#= mesh 3,4 "$I_3$" cw r=0.5')
CONSTRAINT = '#= text 3,-0.8 "$I_2-I_1=2$" color=purple'
WALK = '#= path 0,0 -> 0,3 -> 6,3 -> 6,0 -> 0.45,0'
SIGNS_SUPER = j('#= sign 0.5,2.6 +', '#= sign 2.5,2.6 -',       # 10 Ω left: walk goes right
                '#= sign 3.5,2.6 +', '#= sign 5.5,2.6 -',       # 10 Ω right: walk goes right
                '#= sign 6.4,2.4 +', '#= sign 6.4,0.6 -')       # 30 Ω: walk goes down
SIGNS_3 = j('#= sign 0.5,4.6 +', '#= sign 5.5,4.6 -',           # top 10 Ω: I_3 goes right
            '#= sign 5.5,3.4 +', '#= sign 3.5,3.4 -',           # 10 Ω right: I_3 goes left
            '#= sign 2.5,3.4 +', '#= sign 0.5,3.4 -')           # 10 Ω left: I_3 goes left

STEPS = [
    ('The circuit', GIVEN, r'''
**Method: mesh.** Three windows.
- The $2\,\mathrm{A}$ sits between two windows → **supermesh**.
- The $5i_\Delta$ source is dependent → one extra equation: $i_\Delta$ in mesh currents.
'''),
    ('Mesh currents', j(GIVEN, MESHES, CONSTRAINT), r'''
$I_1$, $I_2$ (bottom windows) and $I_3$ (top), all clockwise.

The $2\,\mathrm{A}$ arrow points **up**:
- $I_2$ goes up through it → $+I_2$
- $I_1$ goes down through it → $-I_1$

$$
I_2-I_1=2
$$
'''),
    ('KVL around the supermesh', j(GIVEN, MESHES, CONSTRAINT, WALK, SIGNS_SUPER), r'''
Walk around $I_1$ and $I_2$ **together**, skipping the $2\,\mathrm{A}$ branch.

Sign you **enter** each element by:
- $5i_\Delta$: enter $-$ → $-5i_\Delta$
- $10\,\Omega$ left (shared with $I_3$): $+10(I_1-I_3)$
- $10\,\Omega$ right (shared with $I_3$): $+10(I_2-I_3)$
- $30\,\Omega$: $+30I_2$

$$
-5i_\Delta+10(I_1-I_3)+10(I_2-I_3)+30I_2=0
$$
'''),
    ('KVL in mesh $I_3$', j(GIVEN, MESHES, CONSTRAINT, SIGNS_3), r'''
Walk with $I_3$ (right along the top, back left through the two lower $10\,\Omega$):

$$
10I_3+10(I_3-I_2)+10(I_3-I_1)=0
$$
'''),
    ('(a) The control equation', j(GIVEN, MESHES, '#= path 5.5,5 -> 0.5,5 thin color=orange'), r'''
$i_\Delta$ flows **left** in the top $10\,\Omega$. Only $I_3$ runs there, going **right**:

$$
i_\Delta=-I_3
$$

**(a) answer:** four equations, four unknowns.

$$
\begin{aligned}
I_2-I_1&=2\\
-5i_\Delta+10(I_1-I_3)+10(I_2-I_3)+30I_2&=0\\
10I_3+10(I_3-I_2)+10(I_3-I_1)&=0\\
i_\Delta&=-I_3
\end{aligned}
$$
'''),
    ('(b) Solve', j(GIVEN, MESHES, r'#+ $I_1=-1.75\,\mathrm{A}$', r'#+ $I_2=0.25\,\mathrm{A}$',
                    r'#+ $I_3=-0.5\,\mathrm{A}$', r'#+ $i_\Delta=0.5\,\mathrm{A}$'), r'''
Put $i_\Delta=-I_3$ in the supermesh, divide by 5; divide mesh $I_3$ by 10:

$$
2I_1+8I_2-3I_3=0 \qquad 3I_3=I_1+I_2
$$

Put $I_1=I_2-2$ into both:

$$
3I_3=2I_2-2 \qquad 2(I_2-2)+8I_2-3I_3=0
$$

$$
10I_2-4-(2I_2-2)=0 \;\Rightarrow\; I_2=0.25\,\mathrm{A}
$$

$$
I_3=\frac{0.5-2}{3}=-0.5\,\mathrm{A} \qquad I_1=-1.75\,\mathrm{A}
$$

$$
\boxed{i_\Delta=-I_3=0.5\,\mathrm{A}}
$$
'''),
    ("Check with Ohm's law", j(GIVEN, '#= text 6.9,3.5 "$7.5\\,\\mathrm{V}$" color=pink',
                               '#= text -0.9,3.5 "$2.5\\,\\mathrm{V}$" color=pink'), r'''
- $30\,\Omega$ carries $I_2$: top-right node $=(30)(0.25)=7.5\,\mathrm{V}$.
- Dependent source: left node $=5i_\Delta=(5)(0.5)=2.5\,\mathrm{V}$.

Ohm's law on the top $10\,\Omega$ (right to left):

$$
i_\Delta=\frac{7.5-2.5}{10}=0.5\,\mathrm{A}\;✓
$$
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    L, m, r = els['RA'][0], els['RA'][1], els['RB'][1]
    assert els['E1'] == (L, '0') and els['RT'] == (r, L) and els['RB'][0] == m, els   # i_Δ: r -> L
    assert els['I1'] == ('0', m) and els['R30'] == (r, '0'), els
    I1, I2, I3 = F(-7, 4), F(1, 4), F(-1, 2)
    iD = -I3
    assert I2 - I1 == 2
    assert -5 * iD + 10 * (I1 - I3) + 10 * (I2 - I3) + 30 * I2 == 0
    assert 10 * I3 + 10 * (I3 - I2) + 10 * (I3 - I1) == 0
    assert 2 * I1 + 8 * I2 - 3 * I3 == 0 and 3 * I3 == I1 + I2 and 3 * I3 == 2 * I2 - 2
    assert 10 * I2 - 4 - (2 * I2 - 2) == 0 and (F(1, 2) - 2) / 3 == I3
    Vn, I, _ = solve([('E', 'E1', 'L', '0', {'r': 0.5, 'L': -0.5}, 0), ('R', 'RT', 'r', 'L', 10),
                      ('R', 'RA', 'L', 'm', 10), ('R', 'RB', 'm', 'r', 10), ('I', 'I1', '0', 'm', 2),
                      ('R', 'R30', 'r', '0', 30)])
    assert abs(I['RT'] - 0.5) < 1e-9 and abs(Vn['r'] - 7.5) < 1e-9 and abs(Vn['L'] - 2.5) < 1e-9
    assert abs(I['RA'] - (I1 - I3)) < 1e-9 and abs(I['R30'] - I2) < 1e-9
