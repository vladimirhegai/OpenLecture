r"""Textbook P4.62: source transformations step by step to find v_o, then a mesh check.

Drawn a little narrower than the week-note figure (same circuit): x = 0 (2.5 mA), 2 (a, 8k), 4.5 (b, 80k),
7 (c), 9.5 (d, 5k), 11.5 (12 mA)."""
from fractions import Fraction as F

SECTION = 'B'
TITLE = 'Two current sources at the ends'
SOURCE = 'Textbook P4.62'
CITES = [{"chunk_id": "b0340958-02ef-4cf3-a7c0-cbd0e26f0065", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1}]
PROMPT = r'''**(a)** Make a series of source transformations to find $v_o$.

**(b)** Check your answer with the mesh-current method.'''

K = r'\,\mathrm{k\Omega}'
V = r'\,\mathrm{V}'
MA = r'\,\mathrm{mA}'


def j(*parts):
    return '\n'.join(parts)


I1 = f'I1 0,3 -> 0,0 "$2.5{MA}$"'
R1 = f'R1 2,3 -> 2,0 "$8{K}$"'
R2 = f'R2 2,3 -> 4.5,3 "$24{K}$" v="$v_o$"'
R3 = f'R3 4.5,3 -> 4.5,0 "$80{K}$"'
R4 = f'R4 4.5,3 -> 7,3 "$15{K}$"'
V1 = f'V1 7,3 -> 9.5,3 "$40{V}$"'
R5 = f'R5 9.5,3 -> 9.5,0 "$5{K}$"'
I2 = f'I2 11.5,0 -> 11.5,3 "$12{MA}$"'
BOT = 'wire 0,0 -> 11.5,0'
LA, LB = 'label 2,3 "$a$" above', 'label 4.5,3 "$b$" above'
LC, LD = 'label 7,3 "$c$" above', 'label 9.5,3 "$d$" above'
GIVEN = j(I1, 'wire 0,3 -> 2,3', R1, R2, R3, R4, V1, R5, 'wire 9.5,3 -> 11.5,3', I2, BOT, LA, LB, LC, LD, 'ground 7,0')

# (1) left: 2.5 mA (arrow down) || 8k  ->  20 V (+ at the bottom, where the arrow points) in series with 8k
LEFT_V = j(f'VL 0,0 -> 0,3 "$20{V}$"', f'R1 0,3 -> 2,3 "$8{K}$"')
# (2) right: 12 mA (arrow up) || 5k  ->  60 V (+ at the top) in series with 5k
RIGHT_V = j(f'R5 9.5,3 -> 11.5,3 "$5{K}$"', f'VR 11.5,3 -> 11.5,0 "$60{V}$"')
S1 = j(LEFT_V, R2, R3, R4, V1, R5, 'wire 9.5,3 -> 11.5,3', I2, BOT, LA, LB, LC, LD, 'ground 7,0')
S2 = j(LEFT_V, R2, R3, R4, V1, RIGHT_V, BOT, LA, LB, LC, LD, 'ground 7,0')
# (3) right series chain 15k, 40 V, 5k, 60 V  ->  20k and 100 V
RIGHT_TH = j(f'R4 4.5,3 -> 7,3 "$20{K}$"', 'wire 7,3 -> 11.5,3', f'VR 11.5,3 -> 11.5,0 "$100{V}$"')
S3 = j(LEFT_V, R2, R3, RIGHT_TH, BOT, LA, LB, 'ground 7,0')
# (4) left series 8k + 24k = 32k (v_o is inside it: we come back to the 24k at the end)
S4 = j(f'VL 0,0 -> 0,3 "$20{V}$"', f'R12 0,3 -> 4.5,3 "$32{K}$"', R3, RIGHT_TH, BOT, LB, 'ground 7,0')
# (5) both sides back to current sources: 20/32k = 0.625 mA (down), 100/20k = 5 mA (up)
S5 = j(r'IL 0,3 -> 0,0 "$0.625\,\mathrm{mA}$"', f'R12 2,3 -> 2,0 "$32{K}$"', R3, f'R4 9.5,3 -> 9.5,0 "$20{K}$"',
       f'IR 11.5,0 -> 11.5,3 "$5{MA}$"', 'wire 0,3 -> 11.5,3', BOT, LB, 'ground 7,0')
# (6) parallel: one source 5 - 0.625 = 4.375 mA (up), one resistor 32 || 80 || 20 = 32/3 k
S6 = j(r'IN 11.5,0 -> 11.5,3 "$4.375\,\mathrm{mA}$"', r'REQ 4.5,3 -> 4.5,0 "$10.67\,\mathrm{k\Omega}$"',
       'wire 4.5,3 -> 11.5,3', 'wire 4.5,0 -> 11.5,0', LB, 'ground 7,0')
VB = r'#= text 5.6,1.5 "$46.67\,\mathrm{V}$" color=green'
# (7) back to the circuit after step 3, with V_b known
S7 = j(LEFT_V, R2, R3, RIGHT_TH, BOT, LA, LB, 'ground 7,0')

MESHES = j('#= mesh 0.95,2.3 "$I_A$" cw r=0.35', '#= mesh 2.75,1.5 "$I_B$" cw r=0.38',
           '#= mesh 7,1.5 "$I_C$" cw r=0.7', '#= mesh 10.3,2.3 "$I_D$" cw r=0.35')
FIXED = j(r'#= text 1,-0.45 "$I_A=-2.5\,\mathrm{mA}$" color=purple', r'#= text 10.5,-0.45 "$I_D=-12\,\mathrm{mA}$" color=purple')
# R2's own v_o marks already read + (left) / - (right) for I_B, so R2 gets no boxes
SIGNS_B = j('#= sign 4.85,2.6 +', '#= sign 4.85,0.4 -', '#= sign 1.65,0.4 +', '#= sign 1.65,2.6 -')
SIGNS_C = j('#= sign 5.35,2.6 +', '#= sign 6.65,2.6 -', '#= sign 9.15,2.6 +', '#= sign 9.15,0.4 -',
            '#= sign 4.85,0.4 +', '#= sign 4.85,2.2 -')

STEPS = [
    ('The circuit', GIVEN, r'''
**Method: source transformation** (the question asks for it), then **mesh** to check.

Units: $\mathrm{k\Omega}$, $\mathrm{mA}$, $\mathrm{V}$ ($m\cdot k=1$).
'''),
    ('Left: current source → voltage source', S1, r'''
$2.5\,\mathrm{mA}$ in parallel with $8\,\mathrm{k\Omega}$ → voltage source in **series** with $8\,\mathrm{k\Omega}$:

$$
V=IR=(2.5m)(8k)=20\,\mathrm{V}
$$

$+$ goes where the arrow points (bottom).
'''),
    ('Right: current source → voltage source', S2, r'''
$12\,\mathrm{mA}$ in parallel with $5\,\mathrm{k\Omega}$:

$$
V=(12m)(5k)=60\,\mathrm{V}
$$

The arrow points up → $+$ on top.
'''),
    ('Right: one series chain', S3, r'''
$15\,\mathrm{k\Omega}$, $40\,\mathrm{V}$, $5\,\mathrm{k\Omega}$, $60\,\mathrm{V}$ are all in series.

$$
R=15k+5k=20\,\mathrm{k\Omega}
$$

Walk from $c$ down to ground (sign you enter by): $+40+60$

$$
V=100\,\mathrm{V}\ (+\text{ on top})
$$
'''),
    ('Left: one series resistor', S4, r'''
$$
8k+24k=32\,\mathrm{k\Omega}
$$

$v_o$ is across the $24\,\mathrm{k\Omega}$ inside it: we come back to it at the end.
'''),
    ('Both sides → current sources', S5, r'''
Left: $20\,\mathrm{V}$ behind $32\,\mathrm{k\Omega}$, $+$ at the bottom → arrow **down**:

$$
I=\frac{20}{32k}=0.625\,\mathrm{mA}
$$

Right: $100\,\mathrm{V}$ behind $20\,\mathrm{k\Omega}$, $+$ on top → arrow **up**:

$$
I=\frac{100}{20k}=5\,\mathrm{mA}
$$

Everything is now in parallel.
'''),
    ('Combine, then Ohm → $V_b$', j(S6, VB, r'#+ $V_b=46.67\,\mathrm{V}$'), r'''
Sources: $5-0.625=4.375\,\mathrm{mA}$ up.

Resistors:

$$
\frac{1}{R}=\frac{1}{32k}+\frac{1}{80k}+\frac{1}{20k}=\frac{15}{160k} \;\Rightarrow\; R=\tfrac{32}{3}\,\mathrm{k\Omega}
$$

Ohm's law:

$$
V_b=(4.375m)\left(\tfrac{32}{3}k\right)=46.67\,\mathrm{V}
$$
'''),
    ('Back to the $24\\,\\mathrm{k\\Omega}$', j(S7, VB, '#= path 4.2,3.2 -> 2.3,3.2 thin color=orange',
                                               r'#= text 3.25,1.95 "$2.083\,\mathrm{mA}$" color=orange',
                                               r'#+ $i=2.083\,\mathrm{mA}$', r'#+ $v_o=-50\,\mathrm{V}$'), r'''
The left branch: $b$ at $46.67\,\mathrm{V}$, the bottom of the $8\,\mathrm{k\Omega}$ at $-20\,\mathrm{V}$.

$$
i=\frac{46.67-(-20)}{32k}=2.083\,\mathrm{mA}\ (b\to a)
$$

Ohm on the $24\,\mathrm{k\Omega}$: $(2.083m)(24k)=50\,\mathrm{V}$, falling from $b$ to $a$.

$v_o$ has $+$ at $a$ (the low end):

$$
\boxed{v_o=-50\,\mathrm{V}}
$$
'''),
    ('Check: mesh currents', j(GIVEN, MESHES, FIXED, r'#+ $I_A=-2.5\,\mathrm{mA}$', r'#+ $I_D=-12\,\mathrm{mA}$'), r'''
Back to the original circuit. Four clockwise meshes.

The outer current sources fix $I_A$ and $I_D$:
- $I_A$ goes **up** the left edge; the source points **down** → $I_A=-2.5\,\mathrm{mA}$
- $I_D$ goes **down** the right edge; the source points **up** → $I_D=-12\,\mathrm{mA}$
'''),
    ('Check: KVL in mesh B', j(GIVEN, MESHES, FIXED, SIGNS_B), r'''
Walk with $I_B$ (sign you enter by). The $v_o$ marks already show $+$ where $I_B$ enters the $24\,\mathrm{k\Omega}$.

$$
24I_B+80(I_B-I_C)+8(I_B-I_A)=0
$$

With $I_A=-2.5$:

$$
112I_B-80I_C=-20
$$
'''),
    ('Check: KVL in mesh C → $v_o$', j(GIVEN, MESHES, FIXED, SIGNS_C, r'#+ $I_B=-\tfrac{25}{12}\,\mathrm{mA}$'), r'''
Walk with $I_C$: the $40\,\mathrm{V}$ is entered at $+$:

$$
15I_C+40+5(I_C-I_D)+80(I_C-I_B)=0
$$

With $I_D=-12$:

$$
-80I_B+100I_C=-100
$$

Solve both:

$$
I_B=-\tfrac{25}{12}\,\mathrm{mA} \qquad I_C=-\tfrac83\,\mathrm{mA}
$$

$I_B$ enters the $24\,\mathrm{k\Omega}$ at $v_o$'s $+$:

$$
v_o=(24k)\left(-\tfrac{25}{12}m\right)=-50\,\mathrm{V}\ \checkmark
$$
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    a, b, c, d = els['R2'][0], els['R2'][1], els['V1'][0], els['V1'][1]
    assert els['I1'] == (a, '0') and els['R1'] == (a, '0') and els['R3'] == (b, '0'), els
    assert els['R4'] == (b, c) and els['R5'] == (d, '0') and els['I2'] == ('0', d), els
    s1, _ = check(S1)
    assert s1['VL'][0] == '0' and s1['R1'][1] == s1['R2'][0], s1   # + of the 20 V at ground
    s2, _ = check(S2)
    assert s2['VR'] == (s2['R5'][1], '0') and s2['R5'][0] == s2['V1'][1], s2
    s3, _ = check(S3)
    assert s3['VR'] == (s3['R4'][1], '0'), s3
    s5, _ = check(S5)
    assert s5['IL'][1] == '0' and s5['IR'][0] == '0', s5
    s6, _ = check(S6)
    assert s6['IN'] == ('0', s6['REQ'][0]), s6
    # transformations
    assert F('2.5') * 8 == 20 and 12 * 5 == 60 and 15 + 5 == 20 and 40 + 60 == 100 and 8 + 24 == 32
    assert F(20, 32) == F('0.625') and F(100, 20) == 5 and 5 - F('0.625') == F('4.375')
    assert F(1, 32) + F(1, 80) + F(1, 20) == F(15, 160) and 1 / F(15, 160) == F(32, 3)
    Vb = F('4.375') * F(32, 3)
    assert round(float(Vb), 2) == 46.67
    i = (Vb + 20) / 32
    assert round(float(i), 3) == 2.083 and i * 24 == 50
    vo = -i * 24
    # mesh check
    IA, ID = F('-2.5'), -12
    IB, IC = F(-25, 12), F(-8, 3)
    assert 24 * IB + 80 * (IB - IC) + 8 * (IB - IA) == 0 and 112 * IB - 80 * IC == -20
    assert 15 * IC + 40 + 5 * (IC - ID) + 80 * (IC - IB) == 0 and -80 * IB + 100 * IC == -100
    assert 24 * IB == vo == -50
    # cross-check: V_a from the right (b - 24 i) equals V_a from the left (-20 + 8 i)
    assert Vb - 24 * i == -20 + 8 * i
