r"""Assessment Problem 3.7: a balanced Wheatstone bridge; find R_x and check the 250 mW ratings."""

SECTION = 'A'
TITLE = 'Balanced bridge and resistor ratings'
SOURCE = 'Assessment Problem 3.7'
CITES = [{'chunk_id': 'e6f9cf47-42bf-471c-a263-7b41a6e37f9f', 'source_id': '48fd3154-0d95-4704-932b-e13c2c2b7ff8', 'version': 1}]
PROMPT = 'The bridge is balanced (no galvanometer current). Find $R_x$, and check whether any resistor exceeds a $250\\,\\mathrm{mW}$ rating.'

O = r'\,\Omega'
VS = r'V1 0,4 -> 0,0 "$5\,\mathrm{V}$"'
R1 = f'R1 3,4 -> 3,2 "$100{O}$"'
R3 = f'R3 3,2 -> 3,0 "$150{O}$"'
R2 = r'R2 6,4 -> 6,2 "$1\,\mathrm{k\Omega}$"'
RX = 'R4 6,2 -> 6,0 "$R_x$"'
AM = 'AM1 3,2 -> 6,2 "galvanometer"'
WIRES = 'wire 0,4 -> 6,4\nwire 6,0 -> 0,0'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(VS, WIRES, R1, R3, R2, RX, AM)
OPEN = j(VS, WIRES, R1, R3, R2, RX)          # galvanometer gone: no current through it
IG0 = r'#= text 4.5,2.35 "$i_g=0$" color=accent'
MESH = '#= mesh 1.5,2 "$I$" cw r=0.75'
SIGNS = j('#= sign 2.65,3.6 +', '#= sign 2.65,2.4 -',   # 100: I enters at the top
          '#= sign 2.65,1.6 +', '#= sign 2.65,0.4 -')   # 150: I enters at the top
V150 = r'#= text 3.75,1.0 "$3\,\mathrm{V}$" color=pink'
VRIGHT = j(r'#= text 6.85,3.0 "$2\,\mathrm{V}$" color=pink', r'#= text 6.85,1.0 "$3\,\mathrm{V}$" color=pink')

STEPS = [
    ('The circuit', GIVEN, r'''
Find $R_x$.

**Balanced** = no current through the galvanometer.
'''),
    ('Balanced → take out the galvanometer', j(OPEN, IG0), r'''
$i_g=0$, so removing the galvanometer changes nothing.

$i_g=0$ through it also means $0\,\mathrm{V}$ across it:

the two midpoints sit at the **same** voltage.
'''),
    ('Mesh current', j(OPEN, MESH), r'''
The left side is now one loop: $5\,\mathrm{V}$ → $100\,\Omega$ → $150\,\Omega$.

Give it a mesh current $I$, clockwise.
'''),
    ('Signs + KVL', j(OPEN, MESH, SIGNS, r'#+ $I=20\,\mathrm{mA}$'), r'''
Signs you **enter** each element by:
- $5\,\mathrm{V}$: enter $-$ → $-5$
- $100\,\Omega$: enter $+$ → $+100I$
- $150\,\Omega$: enter $+$ → $+150I$

$$
-5+100I+150I=0
$$

$$
I=\frac{5}{250}=20\,\mathrm{mA}
$$
'''),
    ("Ohm's law on the $150\\,\\Omega$", j(OPEN, V150, r'#+ $V_{150}=3\,\mathrm{V}$'), r'''
$$
V_{150}=I\cdot150=(20m)(150)=3\,\mathrm{V}
$$

So the left midpoint is $3\,\mathrm{V}$ above the bottom wire.
'''),
    ('Same voltage on the right', j(OPEN, V150, VRIGHT, IG0, r'#+ $V_{R_x}=3\,\mathrm{V}$'), r'''
$0\,\mathrm{V}$ across the galvanometer → the right midpoint is also $3\,\mathrm{V}$ up:

$$
V_{R_x}=3\,\mathrm{V}
$$

The right side spans the whole $5\,\mathrm{V}$:

$$
V_{1k}=5-3=2\,\mathrm{V}
$$
'''),
    ("Ohm's law → $R_x$", j(OPEN, VRIGHT, r'#+ $I_{right}=2\,\mathrm{mA}$', r'#+ $R_x=1.5\,\mathrm{k\Omega}$'), r'''
Current down the right side:

$$
I_{right}=\frac{2}{1k}=2\,\mathrm{mA}
$$

Same current through $R_x$:

$$
R_x=\frac{3}{2m}=1.5\,\mathrm{k\Omega}
$$

Check (balance rule $R_1R_x=R_2R_3$): $R_x=\dfrac{(1k)(150)}{100}=1.5\,\mathrm{k\Omega}$ ✓

$$
\boxed{R_x=1.5\,\mathrm{k\Omega}}
$$
'''),
    ('Power ratings', j(OPEN, r'#= text 3.85,3.0 "$40\,\mathrm{mW}$" color=orange', r'#= text 3.85,1.0 "$60\,\mathrm{mW}$" color=orange',
                        r'#= text 6.9,3.0 "$4\,\mathrm{mW}$" color=orange', r'#= text 6.9,1.0 "$6\,\mathrm{mW}$" color=orange',
                        r'#+ $p_{max}=60\,\mathrm{mW}$'), r'''
$p=VI$ for each resistor:
- $100\,\Omega$: $(2)(20m)=40\,\mathrm{mW}$
- $150\,\Omega$: $(3)(20m)=60\,\mathrm{mW}$
- $1\,\mathrm{k\Omega}$: $(2)(2m)=4\,\mathrm{mW}$
- $R_x$: $(3)(2m)=6\,\mathrm{mW}$

Largest: $60\,\mathrm{mW}<250\,\mathrm{mW}$ → **no resistor exceeds its rating**.
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    top, bot = els['V1']
    assert els['R1'][0] == top and els['R2'][0] == top and els['R3'][1] == bot and els['R4'][1] == bot, els
    assert els['AM1'] == (els['R1'][1], els['R2'][1]) and els['R1'][1] == els['R3'][0] and els['R2'][1] == els['R4'][0], els
    from fractions import Fraction as F
    I = F(5, 100 + 150)
    assert I == F(20, 1000)
    v150 = I * 150
    assert v150 == 3
    v1k = 5 - v150
    assert v1k == 2
    ir = v1k / 1000
    assert ir == F(2, 1000)
    rx = v150 / ir
    assert rx == 1500 and F(1000 * 150, 100) == rx
    p = [(5 - v150) * I, v150 * I, v1k * ir, v150 * ir]
    assert p == [F(40, 1000), F(60, 1000), F(4, 1000), F(6, 1000)] and max(p) < F(250, 1000)
    assert p[0] == I ** 2 * 100 and p[3] == ir ** 2 * rx
