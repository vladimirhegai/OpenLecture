r"""Tutorial 1, P2.19: a current source feeding two branches; mesh + Ohm's law, then a power check.

`#+` values accumulate from step to step: declare each one only in the step that finds it.
"""

SECTION = 'A'
TITLE = 'Split currents and check power'
SOURCE = 'Tutorial 1, P2.19'
CITES = [{'chunk_id': 'b6759a4a-d0c8-4bd7-a5b0-99b9a76fad36', 'source_id': 'a27e0480-0d8e-4205-adf6-ee6eb12fabf7', 'version': 1}]
PROMPT = 'Find $i_1$, $i_2$ and $v_o$, and check that the power balances.'

O = r'\,\Omega'
IS = r'I1 0,0 -> 0,3 "$1.5\,\mathrm{A}$" v_rev="$v_o$"'
R1 = f'R1 4,3 -> 4,0 "$100{O}$" i="$i_1$"'
R2 = f'R2 4,3 -> 8,3 "$150{O}$" i="$i_2$"'
R3 = f'R3 8,3 -> 8,0 "$250{O}$"'
WIRES = 'wire 0,3 -> 4,3\nwire 8,0 -> 0,0'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(IS, WIRES, R1, R2, R3)

M1 = '#= mesh 2,1.5 "$I_1$" cw r=0.7'
M2 = '#= mesh 5.9,1.5 "$I_2$" cw r=0.7'
SIGNS2 = j('#= sign 5.25,2.62 +', '#= sign 6.75,2.62 -',   # 150: I2 enters on the left
           '#= sign 7.62,2.2 +', '#= sign 7.62,0.8 -',     # 250: I2 enters at the top
           '#= sign 4.38,0.8 +', '#= sign 4.38,2.2 -')     # 100: I2 goes up, enters at the bottom
CURRENTS = j(r'#= text 4.8,1.5 "$1.2\,\mathrm{A}$" color=pink', r'#= text 6,2.5 "$0.3\,\mathrm{A}$" color=pink')

STEPS = [
    ('The circuit', GIVEN, r'''
Find $i_1$, $i_2$ and $v_o$.

Two windows → two mesh currents.

The current source sits alone on the left edge.
'''),
    ('Mesh currents', j(GIVEN, M1, M2, r'#+ $I_1=1.5\,\mathrm{A}$'), r'''
$I_1$ and $I_2$, both clockwise.

The $1.5\,\mathrm{A}$ source is only in mesh 1 and points the same way as $I_1$:

$$
I_1=1.5\,\mathrm{A}
$$

No KVL for mesh 1: a current source has no fixed voltage.
'''),
    ('KVL around mesh 2', j(GIVEN, M1, M2, SIGNS2, r'#+ $I_2=0.3\,\mathrm{A}$'), r'''
Mark $+$ where $I_2$ **enters** each resistor.

The $100\,\Omega$ is shared: in $I_2$'s direction it carries $I_2-I_1$.
- $150\,\Omega$: enter $+$ → $+150I_2$
- $250\,\Omega$: enter $+$ → $+250I_2$
- $100\,\Omega$: enter $+$ → $+100(I_2-I_1)$

$$
150I_2+250I_2+100(I_2-1.5)=0
$$

$$
500I_2=150 \;\Rightarrow\; I_2=0.3\,\mathrm{A}
$$
'''),
    ('Branch currents', j(GIVEN, CURRENTS, r'#+ $i_1=1.2\,\mathrm{A}$', r'#+ $i_2=0.3\,\mathrm{A}$'), r'''
$i_2$ is only in mesh 2:

$$
i_2=I_2=0.3\,\mathrm{A}
$$

Down the $100\,\Omega$: $I_1$ goes down, $I_2$ goes up.

$$
i_1=I_1-I_2=1.5-0.3=1.2\,\mathrm{A}
$$
'''),
    ("Ohm's law → $v_o$", j(GIVEN, CURRENTS, '#= sign 3.62,2.2 +', '#= sign 3.62,0.8 -', r'#+ $v_o=120\,\mathrm{V}$'), r'''
The source and the $100\,\Omega$ sit between the same top and bottom wires → same voltage.

$i_1$ enters the $100\,\Omega$ at the top → $+$ on top, same as $v_o$.

$$
v_o=i_1\cdot100=(1.2)(100)=120\,\mathrm{V}
$$
'''),
    ('Power check', j(GIVEN, r'#= text -0.95,0.85 "$180\,\mathrm{W}$" color=green', r'#= text 4.85,1.5 "$144\,\mathrm{W}$" color=orange',
                      r'#= text 6,2.5 "$13.5\,\mathrm{W}$" color=orange', r'#= text 8.95,1.5 "$22.5\,\mathrm{W}$" color=orange',
                      r'#+ $p=180\,\mathrm{W}$'), r'''
**Delivered** by the source (green):

$$
p=v_o\cdot1.5=(120)(1.5)=180\,\mathrm{W}
$$

**Absorbed**, $i^2R$ (orange):
- $100\,\Omega$: $(1.2)^2(100)=144\,\mathrm{W}$
- $150\,\Omega$: $(0.3)^2(150)=13.5\,\mathrm{W}$
- $250\,\Omega$: $(0.3)^2(250)=22.5\,\mathrm{W}$

$$
144+13.5+22.5=180\,\mathrm{W}\ ✓
$$
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    top, bot = els['R1'][0], els['R1'][1]
    assert els['I1'] == (bot, top), els                       # source arrow points up into the top node
    assert els['R2'][0] == top and els['R3'][1] == bot and els['R2'][1] == els['R3'][0], els
    from fractions import Fraction as F
    I1 = F(3, 2)
    I2 = F(100) * I1 / 500                                    # 150I2 + 250I2 + 100(I2 - I1) = 0
    assert I2 == F(3, 10)
    i1, i2 = I1 - I2, I2
    assert (i1, i2) == (F(6, 5), F(3, 10))
    vo = i1 * 100
    assert vo == 120 and (150 + 250) * i2 == vo               # both branches span the same voltage
    pa = [i1 ** 2 * 100, i2 ** 2 * 150, i2 ** 2 * 250]
    assert pa == [144, F(27, 2), F(45, 2)] and sum(pa) == vo * I1 == 180
