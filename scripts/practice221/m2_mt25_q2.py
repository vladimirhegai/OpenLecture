r"""ELEC 221 Midterm Fall 2025, Question 2: the Q1 circuit (R_L = 12 Ω) with a 3 V source added in series with
the 4 Ω. Superposition: the change in V_L is the 3 V source acting alone; series/parallel, then one mesh + Ohm."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'M'
TITLE = 'Q2: Superposition, add a source'
SOURCE = 'ELEC 221 Midterm, Fall 2025, Question 2 (Fig. P2)'
PROMPT = (r'In the circuit of Question 1, the voltage across $R_L=12\,\Omega$ is $V_L$. A voltage source '
          r'$v_x=3\,\mathrm{V}$ is added in series with the $4\,\Omega$, as shown. How much does $V_L$ change? '
          r'*Hint: use superposition.*')

O = r'\,\Omega'
V = r'\,\mathrm{V}'
A = r'\,\mathrm{A}'

V1 = f'V1 0,3 -> 0,0 "$5{V}$"'
R2A = f'R2A 0,3 -> 3,3 "$2{O}$"'
TOP = '\n'.join(['wire 0,3 -> 0,5', f'R4 0,5 -> 3,5 "$4{O}$"', f'VX 6,5 -> 3,5 "$v_x=3{V}$"', 'wire 6,5 -> 6,3'])
I1 = f'I1 3,0 -> 3,3 "$3{A}$"'
R2B = f'R2B 3,3 -> 6,3 "$2{O}$"'
RL = f'RL 6,3 -> 6,0 "$R_L=12{O}$" v="$V_L$"'
RIGHT = '\n'.join(['wire 6,3 -> 9,3', f'R1 9,3 -> 9,0 "$1{O}$"', f'R5 9,0 -> 6,0 "$5{O}$"'])
BOTTOM = 'wire 0,0 -> 6,0'
LABELS = '\n'.join(['label 7,3 "$a$" above', 'label 6,0 "$b$" below', 'ground 0,0'])


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(V1, R2A, TOP, I1, R2B, RL, RIGHT, BOTTOM, LABELS)
ALONE = j('wire 0,3 -> 0,0', R2A, TOP, R2B, RL.replace('v="$V_L$"', 'v="$V_L\'\'$"'), RIGHT, BOTTOM, LABELS)
LOOP = j('wire 0,0 -> 0,5', f'R4 0,5 -> 3,5 "$4{O}$"', f'VX 6,5 -> 3,5 "$v_x=3{V}$"', 'wire 6,5 -> 6,3',
         f'REQ 6,3 -> 6,0 "$2{O}$" v="$V_L\'\'$"', BOTTOM,
         'label 6,3 "$a$" right', 'label 6,0 "$b$" below', 'ground 0,0')

STEPS = [
    ('The circuit', GIVEN, r'''
Before: the $5\,\mathrm{V}$ and $3\,\mathrm{A}$ made $V_L$. Now $v_x=3\,\mathrm{V}$ joins them.

Superposition: the new $V_L$ = (part from $5\,\mathrm{V}$ + $3\,\mathrm{A}$) + (part from $v_x$ alone).

The first part **is** the old $V_L$. So:

$$
\text{change in } V_L=V_L''\ (v_x \text{ alone})
$$
'''),
    ('$v_x$ alone', ALONE, r'''
Turn off the old sources:
- $5\,\mathrm{V}$ → **wire**
- $3\,\mathrm{A}$ → **open** (gone)

Now the left side of the circuit is wired straight to $b$.
'''),
    ('Series, then parallel', j(LOOP, r'#+ $R_{eq}=2\,\Omega$'), r'''
Everything below the top branch, from $a$ to $b$:
- $2\,\Omega+2\,\Omega$ → series, $4\,\Omega$ (the middle node touches nothing else now)
- $1\,\Omega+5\,\Omega$ → series, $6\,\Omega$
- $R_L=12\,\Omega$

All three go from $a$ to $b$ → parallel:

$$
12\parallel 6=4\,\Omega \qquad 4\parallel 4=2\,\Omega
$$

$R_{eq}$ is in parallel with $R_L$, so the voltage across $R_{eq}$ **is** $V_L''$.
'''),
    ('Mesh + Ohm', j(LOOP, '#= mesh 3,2.5 "$I$" cw r=0.8', '#= sign 0.5,4.6 +', '#= sign 2.5,4.6 -',
                     '#= sign 5.6,2.4 +', '#= sign 5.6,0.6 -', r"#+ $V_L''=1\,\mathrm{V}$"), r'''
One loop. Sign you **enter** each element by, going with $I$:
- $4\,\Omega$: $+4I$
- $v_x$: enter $-$ → $-3$
- $2\,\Omega$: $+2I$

$$
4I-3+2I=0 \;\Rightarrow\; I=0.5\,\mathrm{A}
$$

Ohm's law ($+$ on top, where $I$ enters):

$$
V_L''=(2)(0.5)=1\,\mathrm{V}
$$
'''),
    ('Answer', j(GIVEN, '#= text 7.6,1.5 "$+1\\,\\mathrm{V}$" color=green'), r'''
$$
\boxed{V_L \text{ goes up by } 1\,\mathrm{V}}
$$

Check with Question 1's Thévenin circuit ($6\,\mathrm{V}$, $1.5\,\Omega$):

$$
V_L=6\cdot\frac{12}{1.5+12}=5.33\,\mathrm{V}\ \text{before}
$$

With all three sources on, $V_L=6.33\,\mathrm{V}$ ✓
'''),
]


def _net(vx, rl=12):
    return [('V', 'V1', 'A', '0', 5), ('R', 'R2A', 'A', 'm', 2), ('R', 'R4', 'A', 'p', 4), ('V', 'VX', 'a', 'p', vx),
            ('I', 'I1', '0', 'm', 3), ('R', 'R2B', 'm', 'a', 2), ('R', 'RL', 'a', '0', rl),
            ('R', 'R1', 'a', 'c', 1), ('R', 'R5', 'c', '0', 5)]


def checks(check):
    els, _ = check(GIVEN)
    top, a = els['V1'][0], els['RL'][0]
    p, m, c = els['R4'][1], els['R2A'][1], els['R1'][1]
    assert els['V1'][1] == '0' and els['RL'][1] == '0' and els['R5'] == (c, '0'), els
    assert els['R4'][0] == top and els['VX'] == (a, p), els                  # + of v_x on the a side
    assert els['I1'] == ('0', m) and els['R2B'] == (m, a) and els['R1'] == (a, c), els
    check(ALONE)
    check(LOOP)
    assert 12 * 6 / 18 == 4 and 4 * 4 / 8 == 2
    I = 3 / 6
    assert 4 * I - 3 + 2 * I == 0 and 2 * I == 1
    old, _, _ = solve(_net(0))
    new, _, _ = solve(_net(3))
    assert abs(new['a'] - old['a'] - 1) < 1e-9
    assert abs(old['a'] - 6 * 12 / 13.5) < 1e-9 and round(old['a'], 2) == 5.33 and round(new['a'], 2) == 6.33
