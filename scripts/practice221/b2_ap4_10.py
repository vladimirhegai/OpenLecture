r"""Assessment Problem 4.10: three meshes, the outer 16 A source fixes mesh 3. Mesh analysis with the user's
sign rule (+ where the mesh current enters; KVL = sum of the sign you enter each element by)."""
from fractions import Fraction as F

SECTION = 'B'
TITLE = 'Power in the middle resistor'
SOURCE = 'Assessment Problem 4.10'
CITES = [
    {"chunk_id": "b424062b-f59f-47c1-b08b-81c45ecae319", "source_id": "3b287f2d-b408-41eb-a523-b299688ff303", "version": 1},
    {"chunk_id": "41f6ae5a-5f7a-4739-a989-3c42552040fb", "source_id": "3b287f2d-b408-41eb-a523-b299688ff303", "version": 1},
]
PROMPT = r'Find the power dissipated in the $2\,\Omega$ resistor.'

O = r'\,\Omega'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(r'V1 0,3 -> 0,0 "$30\,\mathrm{V}$"', f'R1 0,3 -> 3,3 "$3{O}$"', f'R2 0,0 -> 3,0 "$6{O}$"',
          f'R3 3,3 -> 3,0 "$2{O}$"', f'R4 3,3 -> 6,3 "$8{O}$"', f'R5 3,0 -> 6,0 "$4{O}$"', f'R6 6,3 -> 6,0 "$5{O}$"',
          'wire 6,3 -> 9,3', r'I1 9,0 -> 9,3 "$16\,\mathrm{A}$"', 'wire 9,0 -> 6,0')

MESHES = j('#= mesh 1.35,1.5 "$I_1$" cw r=0.55', '#= mesh 4.35,1.5 "$I_2$" cw r=0.55', '#= mesh 7.05,1.5 "$I_3$" cw r=0.55')
I3 = r'#= text 7.5,2.6 "$I_3=-16\,\mathrm{A}$" color=purple'
# + where the mesh current enters each resistor
SIGNS_1 = j('#= sign 2.65,2.6 +', '#= sign 2.65,0.4 -', '#= sign 2.6,3.4 -', '#= sign 0.4,3.4 +',
            '#= sign 2.6,-0.4 +', '#= sign 0.4,-0.4 -')
SIGNS_2 = j('#= sign 3.4,3.4 +', '#= sign 5.6,3.4 -', '#= sign 5.65,2.6 +', '#= sign 5.65,0.4 -',
            '#= sign 5.6,-0.4 +', '#= sign 3.4,-0.4 -', '#= sign 3.35,0.4 +', '#= sign 3.35,2.6 -')

STEPS = [
    ('The circuit', GIVEN, r'''
**Method: mesh.** 3 meshes, and the $16\,\mathrm{A}$ source sits on the outer edge, so it fixes mesh 3 → only 2 unknowns (nodal would need 4).
'''),
    ('Mesh currents', j(GIVEN, MESHES), r'''
One clockwise mesh current per window: $I_1$, $I_2$, $I_3$.

A resistor shared by two meshes carries (own − neighbour).
'''),
    ('Mesh 3 is fixed', j(GIVEN, MESHES, I3, r'#+ $I_3=-16\,\mathrm{A}$'), r'''
Only $I_3$ passes through the $16\,\mathrm{A}$ source.

$I_3$ goes **down** the right edge; the source pushes **up** → opposite:

$$
I_3=-16\,\mathrm{A}
$$
'''),
    ('KVL in mesh 1', j(GIVEN, MESHES, I3, SIGNS_1), r'''
Walk with $I_1$; sign you **enter** each element by:
- $3\,\Omega$: $+3I_1$
- $2\,\Omega$ (shared): $+2(I_1-I_2)$
- $6\,\Omega$: $+6I_1$
- $30\,\mathrm{V}$: enter $-$ → $-30$

$$
3I_1+2(I_1-I_2)+6I_1-30=0
$$

$$
11I_1-2I_2=30
$$
'''),
    ('KVL in mesh 2', j(GIVEN, MESHES, I3, SIGNS_2), r'''
Walk with $I_2$:
- $8\,\Omega$: $+8I_2$
- $5\,\Omega$ (shared): $+5(I_2-I_3)$
- $4\,\Omega$: $+4I_2$
- $2\,\Omega$ (shared): $+2(I_2-I_1)$

$$
8I_2+5(I_2-I_3)+4I_2+2(I_2-I_1)=0
$$

With $I_3=-16$:

$$
-2I_1+19I_2=-80
$$
'''),
    ('Solve', j(GIVEN, MESHES, I3, r'#= text 1.5,2.6 "$I_1=2\,\mathrm{A}$" color=purple',
                r'#= text 4.5,2.6 "$I_2=-4\,\mathrm{A}$" color=purple',
                r'#+ $I_1=2\,\mathrm{A}$', r'#+ $I_2=-4\,\mathrm{A}$'), r'''
Mesh 1: $I_1=\dfrac{30+2I_2}{11}$. Into mesh 2, $\times 11$:

$$
-60-4I_2+209I_2=-880
$$

$$
205I_2=-820 \;\Rightarrow\; I_2=-4\,\mathrm{A}
$$

$$
I_1=\frac{30+2(-4)}{11}=2\,\mathrm{A}
$$
'''),
    ("Ohm's law on the $2\\,\\Omega$", j(GIVEN, MESHES, I3, '#= path 3,2.6 -> 3,0.4 thin color=orange',
                                          r'#= text 3.5,0.6 "$6\,\mathrm{A}$" color=orange',
                                          r'#+ $i_{2\Omega}=6\,\mathrm{A}$', r'#+ $p_{2\Omega}=72\,\mathrm{W}$'), r'''
The $2\,\Omega$ carries $I_1-I_2$ (down):

$$
I_1-I_2=2-(-4)=6\,\mathrm{A}
$$

$$
V_{2\Omega}=(6)(2)=12\,\mathrm{V}
$$

$$
p=V\,i=(12)(6)
$$

$$
\boxed{p_{2\Omega}=72\,\mathrm{W}}
$$
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    top_l, bot_l = els['R1'][1], els['R2'][1]
    assert els['V1'] == (els['R1'][0], els['R2'][0]), els
    assert els['R3'] == (top_l, bot_l) and els['R4'][0] == top_l and els['R5'][0] == bot_l, els
    assert els['R6'] == (els['R4'][1], els['R5'][1]) and els['I1'] == (els['R5'][1], els['R4'][1]), els
    I3 = -16
    I2 = F(-820, 205)
    I1 = (30 + 2 * I2) / 11
    assert (I1, I2) == (2, -4)
    assert 3 * I1 + 2 * (I1 - I2) + 6 * I1 - 30 == 0 and 11 * I1 - 2 * I2 == 30
    assert 8 * I2 + 5 * (I2 - I3) + 4 * I2 + 2 * (I2 - I1) == 0 and -2 * I1 + 19 * I2 == -80
    assert -60 - 4 * I2 + 209 * I2 == -880 and 19 * 11 == 209 and -80 * 11 == -880
    assert I1 - I2 == 6 and 6 * 2 == 12 and 12 * 6 == 72 and (I1 - I2) ** 2 * 2 == 72
