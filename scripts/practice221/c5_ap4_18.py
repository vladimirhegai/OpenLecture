r"""Assessment Problem 4.18: Thévenin by source transformations, then a 100 kΩ voltmeter as the load.

Figure rebuilt from the course's Chapter 4 assessment solutions, p. 4-13 (the textbook in the course is a
different edition): a branch of a 36 V source (+ at the bottom, i.e. the solution's "-36 V") in series with
12 kΩ, an 18 mA source pointing up, 60 kΩ, then 15 kΩ out to terminal A; B is the bottom wire.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'C'
TITLE = 'Thévenin by source transformations, then a voltmeter'
SOURCE = 'Assessment Problem 4.18'
CITES = [{'chunk_id': '87b0d37f-e208-4e6d-b574-b0fead11d2c9', 'source_id': '3b287f2d-b408-41eb-a523-b299688ff303', 'version': 1}]
PROMPT = r'''
A voltmeter with an internal resistance of $100\,\mathrm{k\Omega}$ is used to measure $v_{AB}$.

Use source transformations to find the Thévenin equivalent at $A$, $B$, then find the voltmeter reading.
'''

K = r'\,\mathrm{k\Omega}'
V = r'\,\mathrm{V}'
MA = r'\,\mathrm{mA}'
FRAME = '\n'.join(['wire 0,0 -> 9,0', 'terminal 9,3', 'terminal 9,0',
                   'label 9,3 "$A$" above', 'label 9,0 "$B$" below'])
R15 = f'R3 6,3 -> 9,3 "$15{K}$"'
VAB = 'gap 9,3 -> 9,0 v="$v_{AB}$"'
I18 = f'I1 3.5,0 -> 3.5,3 "$18{MA}$" flip'
R60 = f'R2 6,3 -> 6,0 "$60{K}$" flip'
R12V = f'R1 1.5,3 -> 1.5,0 "$12{K}$" flip'  # label on its right: the 3 mA source is close on the left


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(f'V1 0,0 -> 0,3 "$36{V}$"', f'R1 0,3 -> 3.5,3 "$12{K}$"', I18, 'wire 3.5,3 -> 6,3', R60, R15, FRAME, VAB)
ST1 = j(f'IA 0,3 -> 0,0 "$3{MA}$"', 'wire 0,3 -> 6,3', R12V, I18, R60, R15, FRAME, VAB)
SUM_I = j(f'IA 0,0 -> 0,3 "$15{MA}$"', 'wire 0,3 -> 6,3', R12V, R60, R15, FRAME, VAB)
SUM_R = j(f'IA 0,0 -> 0,3 "$15{MA}$"', 'wire 0,3 -> 6,3', f'R2 6,3 -> 6,0 "$10{K}$" flip', R15, FRAME, VAB)
ST2 = j(f'VA 0,3 -> 0,0 "$150{V}$"', f'R2 0,3 -> 3,3 "$10{K}$"', 'wire 3,3 -> 6,3', R15, FRAME, VAB)
TH_PARTS = (f'VA 0,3 -> 0,0 "$150{V}$"', 'wire 0,3 -> 3,3', f'RTH 3,3 -> 6,3 "$25{K}$"', 'wire 6,3 -> 9,3', FRAME)
TH = j(*TH_PARTS, VAB)
# the meter carries the v_AB marks itself (+ on top, where the mesh current enters)
METER = j(*TH_PARTS, 'wire 9,3 -> 10.5,3', f'RM 10.5,3 -> 10.5,0 "$100{K}$" v="$v_{{AB}}$"', 'wire 9,0 -> 10.5,0')

STEPS = [
    ('The circuit', GIVEN, r'''
The voltmeter goes on $A$, $B$ → it is the **load**: a $100\,\mathrm{k\Omega}$ resistor.

**Plan**
1. Source transformations until one source and one resistor are left: that's the Thévenin circuit.
2. Put the $100\,\mathrm{k\Omega}$ meter on it → mesh + Ohm.
'''),
    ('$36\\,\\mathrm{V}$ + $12\\,\\mathrm{k\\Omega}$ → current source', ST1, r'''
The $36\,\mathrm{V}$ source and $12\,\mathrm{k\Omega}$ are in **series** → swap for a current source **parallel** with $12\,\mathrm{k\Omega}$.

$$
i=\frac{36}{12k}=3\,\mathrm{mA}
$$

Direction: the source pushes current out of its $+$ end. $+$ is at the **bottom** → the arrow points **down**.
'''),
    ('Add the current sources', SUM_I, r'''
$3\,\mathrm{mA}$ down and $18\,\mathrm{mA}$ up, between the same two wires → add them (up $+$):

$$
-3m+18m=15\,\mathrm{mA} \text{ up}
$$
'''),
    ('Combine the parallel resistors', SUM_R, r'''
$12\,\mathrm{k\Omega}$ and $60\,\mathrm{k\Omega}$ both span the top and bottom wires → **parallel**:

$$
\frac{(12k)(60k)}{12k+60k}=\frac{720M}{72k}=10\,\mathrm{k\Omega}
$$
'''),
    ('Current source → voltage source', ST2, r'''
$15\,\mathrm{mA}$ **parallel** with $10\,\mathrm{k\Omega}$ → a voltage source in **series** with $10\,\mathrm{k\Omega}$:

$$
v=(15m)(10k)=150\,\mathrm{V}
$$

The current source pushed **up** → $+$ at the **top**.
'''),
    ('Series → Thévenin circuit', j(TH, r'#+ $V_{Th}=150\,\mathrm{V}$', r'#+ $R_{Th}=25\,\mathrm{k\Omega}$'), r'''
$10\,\mathrm{k\Omega}$ and $15\,\mathrm{k\Omega}$ in series:

$$
R_{Th}=10k+15k=25\,\mathrm{k\Omega}
$$

$$
\boxed{V_{Th}=150\,\mathrm{V},\; R_{Th}=25\,\mathrm{k\Omega}}
$$

An ideal meter (no current) would read $150\,\mathrm{V}$.
'''),
    ('Meter on → mesh + Ohm', j(METER, '#= mesh 5,1.5 "$I$" cw r=0.8',
                              '#= sign 3.4,2.65 +', '#= sign 5.6,2.65 -',
                              r'#+ $I=1.2\,\mathrm{mA}$', r'#+ $v_{AB}=120\,\mathrm{V}$'), r'''
The meter is a $100\,\mathrm{k\Omega}$ load. $I$ enters it at the top → $+$ on top, same as $v_{AB}$.

KVL (sign you enter by):

$$
-150+25kI+100kI=0
$$

$$
125kI=150 \;\Rightarrow\; I=1.2\,\mathrm{mA}
$$

Ohm on the meter:

$$
v_{AB}=I\cdot100k=(1.2m)(100k)
$$

$$
\boxed{v_{AB}=120\,\mathrm{V}}
$$
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    bot = els['R2'][1]
    top = els['R2'][0]
    assert els['V1'][0] == bot, els                                  # + at the bottom wire
    assert els['R1'][1] == top and els['V1'][1] == els['R1'][0], els  # 12k in series with the source, into the top node
    assert els['I1'] == (bot, top), els                               # 18 mA points up into the top node
    assert els['R3'][0] == top, els
    # transformations
    assert abs(36 / 12e3 - 3e-3) < 1e-15
    assert abs(-3e-3 + 18e-3 - 15e-3) < 1e-15
    Rp = 12e3 * 60e3 / 72e3
    assert abs(Rp - 10e3) < 1e-9 and abs(12e3 * 60e3 / 1e6 - 720) < 1e-9
    assert abs(15e-3 * 10e3 - 150) < 1e-12 and 10e3 + 15e3 == 25e3
    # independent solve of the original circuit: open-circuit V_AB, short-circuit current, and with the meter
    def net(load):
        e = [('V', 'V1', 'g', 'n', 36), ('R', 'R1', 'n', 't', 12e3), ('I', 'I1', 'g', 't', 18e-3),
             ('R', 'R2', 't', 'g', 60e3), ('R', 'R3', 't', 'A', 15e3)]
        e = [('V', 'V1', 'g', 'n', 36) if x[1] == 'V1' else x for x in e]
        return e + ([('R', 'RL', 'A', 'g', load)] if load else [])
    # ground the bottom wire: rename 'g' to '0'
    fix = lambda es: [tuple('0' if v == 'g' else v for v in x[:4]) + x[4:] for x in es]  # noqa: E731
    Vo, _, _ = solve(fix(net(None)))
    assert abs(Vo['A'] - 150) < 1e-6
    Vs, Is, _ = solve(fix(net(1e-6)))
    assert abs(150 / Is['RL'] - 25e3) < 1e-3
    Vm, _, _ = solve(fix(net(100e3)))
    assert abs(Vm['A'] - 120) < 1e-6
    I = 150 / 125e3
    assert abs(I - 1.2e-3) < 1e-15 and abs(I * 100e3 - 120) < 1e-9
