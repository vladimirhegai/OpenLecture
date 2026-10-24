r"""Assessment Problem 4.20: Thévenin at a-b with a current-controlled voltage source.

V_Th: 4 A || 60 ohm -> 240 V in series with 60 ohm, 60 + 20 = 80, then two meshes + Ohm.
R_Th: the 240 V off (same as the 4 A open), dependent source kept, 1 V test source, Ohm per branch.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'C'
TITLE = 'Thévenin: a dependent source needs a test source'
SOURCE = 'Assessment Problem 4.20'
CITES = [{"chunk_id": "779ae69c-1fee-4836-824c-5ceac9749991", "source_id": "3b287f2d-b408-41eb-a523-b299688ff303", "version": 1},
         {"chunk_id": "b0235d23-0c76-4c5a-a836-0e357eaa83a0", "source_id": "3b287f2d-b408-41eb-a523-b299688ff303", "version": 1}]
PROMPT = r'Find the Thévenin equivalent at $a$–$b$. The dependent source is controlled by $i_\Delta$, the current down the $40\,\Omega$.'

O = r'\,\Omega'
V = r'\,\mathrm{V}'
R60 = f'R1 0,3 -> 0,0 "$60{O}$"'
I4 = 'I1 2,0 -> 2,3 "$4\\,\\mathrm{A}$"'
R20 = f'R2 2,3 -> 4,3 "$20{O}$"'
E = r'E1 4,3 -> 6,3 "$160i_\Delta$"'          # + on the left
R80 = f'R3 6,3 -> 6,0 "$80{O}$"'
R40 = f'R4 9,3 -> 9,0 "$40{O}$" i="$i_\\Delta$"'
TAIL = '\n'.join(['wire 6,3 -> 9,3', 'wire 9,3 -> 10.5,3', 'wire 0,0 -> 10.5,0',
                  'terminal 10.5,3 "$a$" right', 'terminal 10.5,0 "$b$" right', 'ground 6,0'])


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(R60, 'wire 0,3 -> 2,3', I4, R20, E, R80, R40, TAIL)
# 4 A || 60 ohm  ->  240 V (+ toward the top node) in series with 60 ohm
V240 = f'V1 0,3 -> 0,0 "$240{V}$"'
T1 = j(V240, f'R5 0,3 -> 2,3 "$60{O}$"', R20, E, R80, R40, TAIL)
R80T = f'R6 0,3 -> 4,3 "$80{O}$"'
LOOP = j(V240, R80T, E, R80, R40, TAIL)
MESH = j('#= mesh 3,1.5 "$I_1$" cw r=0.85', '#= mesh 7.5,1.5 "$I_2$" cw r=0.65')
SIGNS1 = j('#= sign 1.2,2.62 +', '#= sign 2.8,2.62 -', '#= sign 5.62,2.3 +', '#= sign 5.62,0.7 -')
SIGNS2 = j('#= sign 6.38,0.7 +', '#= sign 6.38,2.3 -', '#= sign 8.62,2.3 +', '#= sign 8.62,0.7 -')
OFF = j('wire 0,3 -> 0,0', R80T, E, R80, R40, TAIL)
TEST = j(OFF, 'V9 10.5,3 -> 10.5,0 "$1\\,\\mathrm{V}$"')

STEPS = [
    ('The circuit', GIVEN, r'''
A dependent source $160i_\Delta$ sits inside.

**Plan**
1. $V_{Th}=V_{oc}$: tidy the left side, then mesh + Ohm.
2. $R_{Th}$: a test source (the dependent source can't be switched off).
3. Draw the Thévenin circuit.
'''),
    ('Source transformation', T1, r'''
$4\,\mathrm{A}$ in parallel with $60\,\Omega$ → a voltage source in series with $60\,\Omega$:

$$
V=IR=(4)(60)=240\,\mathrm{V}
$$

The arrow pointed up → $+$ on top.
'''),
    ('Series: $60+20$', LOOP, r'''
$60\,\Omega$ and $20\,\Omega$ now carry the same current → one $80\,\Omega$.
'''),
    ('Mesh 1', j(LOOP, MESH, SIGNS1), r'''
Two meshes, both clockwise. $i_\Delta$ runs down the $40\,\Omega$ → $i_\Delta=I_2$.

KVL around $I_1$ (sign you **enter** by):
- $240\,\mathrm{V}$: enter $-$ → $-240$
- $80\,\Omega$ (top): enter $+$ → $+80I_1$
- $160i_\Delta$: enter $+$ → $+160I_2$
- $80\,\Omega$ (shared): $+80(I_1-I_2)$

$$
160I_1+80I_2=240
$$
'''),
    ('Mesh 2 + solve', j(LOOP, MESH, SIGNS2, r'#+ $I_1=1.125\,\mathrm{A}$', r'#+ $I_2=0.75\,\mathrm{A}$'), r'''
KVL around $I_2$:
- $80\,\Omega$ (shared): enter $+$ → $+80(I_2-I_1)$
- $40\,\Omega$: enter $+$ → $+40I_2$

$$
120I_2=80I_1 \;\Rightarrow\; I_2=\tfrac23 I_1
$$

Into mesh 1:

$$
160I_1+\tfrac{160}{3}I_1=240 \;\Rightarrow\; I_1=1.125\,\mathrm{A}
$$

$$
I_2=0.75\,\mathrm{A}
$$
'''),
    ("Ohm's law → $V_{Th}$", j(LOOP, SIGNS2, '#= text 9.8,1.5 "$30\\,\\mathrm{V}$" color=pink', r'#+ $V_{Th}=30\,\mathrm{V}$'), r'''
$a$–$b$ sits right across the $40\,\Omega$. $I_2$ enters it at the top → $+$ at $a$.

$$
V_{Th}=40I_2=(40)(0.75)=30\,\mathrm{V}
$$
'''),
    ('Sources off', OFF, r'''
Independent sources off: $240\,\mathrm{V}$ → **wire** (same as opening the $4\,\mathrm{A}$ in the original: $60+20$ stays in series).

The dependent source **stays on**: it is controlled by $i_\Delta$, which is still there.
'''),
    ('Test source', TEST, r'''
Put $1\,\mathrm{V}$ across $a$–$b$ and find the current $i_T$ it pushes in.

$$
R_{Th}=\frac{1\,\mathrm{V}}{i_T}
$$
'''),
    ("Ohm's law per branch", j(TEST, '#= text 9.75,0.45 "$25\\,\\mathrm{mA}$" color=pink',
                                 '#= text 7,0.45 "$12.5\\,\\mathrm{mA}$" color=pink',
                                 '#= text 2,2.35 "$62.5\\,\\mathrm{mA}$" color=pink',
                                 r'#+ $R_{Th}=10\,\Omega$'), r'''
Every branch runs from $a$ (1 V) to ground:
- $40\,\Omega$: $i_\Delta=\frac{1}{40}=25\,\mathrm{mA}$
- $80\,\Omega$: $\frac{1}{80}=12.5\,\mathrm{mA}$
- left: the source lifts it to $1+160i_\Delta=1+4=5\,\mathrm{V}$, so $\frac{5}{80}=62.5\,\mathrm{mA}$

KCL at $a$ (entering $+$, leaving $-$):

$$
i_T-25m-12.5m-62.5m=0 \;\Rightarrow\; i_T=100\,\mathrm{mA}
$$

$$
R_{Th}=\frac{1}{100m}=10\,\Omega
$$
'''),
    ('Thévenin circuit', j(f'V7 0,3 -> 0,0 "$30{V}$"', f'R7 0,3 -> 4,3 "$10{O}$"', 'wire 4,3 -> 10.5,3',
                           'wire 0,0 -> 10.5,0', 'terminal 10.5,3 "$a$" right', 'terminal 10.5,0 "$b$" right'), r'''
$$
\boxed{V_{Th}=30\,\mathrm{V},\quad R_{Th}=10\,\Omega}
$$

Any load on $a$–$b$ now sees just this.
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    a = els['R4'][0]
    assert els['R3'][0] == a and els['E1'][1] == a, els            # 80, 40 and the source's - end share node a
    assert els['R2'][0] == els['I1'][1] == els['R1'][0], els        # 60, 4 A (arrow in) and 20 meet at v
    assert els['R2'][1] == els['E1'][0], els                        # 20 ohm -> + end of 160 i_D
    assert {els['R1'][1], els['I1'][0], els['R3'][1], els['R4'][1]} == {'0'}, els
    # Full original circuit (nodes v, w, a): E1 w-a = 160 * i_D = 160 * Va/40 = 4 Va
    Vn, _, _ = solve([('R', 'R1', 'v', '0', 60), ('I', 'I1', '0', 'v', 4), ('R', 'R2', 'v', 'w', 20),
                      ('E', 'E1', 'w', 'a', {'a': 4}, 0), ('R', 'R3', 'a', '0', 80), ('R', 'R4', 'a', '0', 40)])
    assert abs(Vn['a'] - 30) < 1e-9 and abs(Vn['v'] - 172.5) < 1e-9
    # Transformed circuit, meshes
    assert 4 * 60 == 240 and 60 + 20 == 80
    I1, I2 = 1.125, 0.75
    assert abs(160 * I1 + 80 * I2 - 240) < 1e-12          # mesh 1: -240 + 80I1 + 160I2 + 80(I1-I2) = 0
    assert abs(-240 + 80 * I1 + 160 * I2 + 80 * (I1 - I2)) < 1e-12
    assert abs(80 * (I2 - I1) + 40 * I2) < 1e-12 and abs(I2 - 2 / 3 * I1) < 1e-12
    assert abs((160 + 160 / 3) * I1 - 240) < 1e-12
    assert 40 * I2 == 30
    # Test source: 4 A open, 1 V at a
    Vt, It, _ = solve([('R', 'R12', 'w', '0', 80), ('E', 'E1', 'w', 'a', {'a': 4}, 0), ('R', 'R3', 'a', '0', 80),
                       ('R', 'R4', 'a', '0', 40), ('V', 'VT', 'a', '0', 1)])
    iT = -It['VT']                       # current out of the + terminal into the circuit
    assert abs(iT - 0.1) < 1e-12 and abs(1 / iT - 10) < 1e-9
    assert abs(Vt['w'] - 5) < 1e-12 and 1 + 160 * (1 / 40) == 5
    assert abs(1 / 40 - 0.025) < 1e-15 and 1 / 80 == 0.0125 and 5 / 80 == 0.0625
    assert abs(0.025 + 0.0125 + 0.0625 - 0.1) < 1e-15
