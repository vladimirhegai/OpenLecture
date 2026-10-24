r"""Tutorial 4, Problem 3.2: a loaded divider solved the Thévenin way (mesh + Ohm's law).

(a) and (b) are terminal questions, so the Thévenin circuit answers them. (c) and (d) ask about resistors
inside the original circuit, so those steps go back to the original drawing.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'C'
TITLE = 'Thévenin: one equivalent, any load'
SOURCE = 'Tutorial 4, Problem 3.2'
CITES = [
    {'chunk_id': '3fde84d0-2994-46c7-ad14-14200bebf152', 'source_id': '6aad60b9-910d-4700-985f-68a4fa9278b3', 'version': 1},
    {'chunk_id': '3846e90d-5eff-48c4-a7b5-1f87d4698715', 'source_id': '6aad60b9-910d-4700-985f-68a4fa9278b3', 'version': 1},
]
PROMPT = r'''
a) Find the no-load value of $v_o$.

b) Find $v_o$ when $R_L=150\,\mathrm{k\Omega}$.

c) How much power is dissipated in the $25\,\mathrm{k\Omega}$ resistor if the load terminals are accidentally short-circuited?

d) What is the maximum power dissipated in the $75\,\mathrm{k\Omega}$ resistor?
'''

K = r'\,\mathrm{k\Omega}'
V = r'\,\mathrm{V}'
VS = f'V1 0,3 -> 0,0 "$200{V}$"'
R25 = f'R1 0,3 -> 3,3 "$25{K}$"'
R75 = f'R2 3,3 -> 3,0 "$75{K}$"'
FRAME = '\n'.join(['wire 3,3 -> 5,3', 'wire 0,0 -> 5,0', 'terminal 5,3', 'terminal 5,0'])
LOAD = '\n'.join(['wire 5,3 -> 7,3', 'R3 7,3 -> 7,0 "$R_L$"', 'wire 5,0 -> 7,0'])
VO = 'gap 5,3 -> 5,0 v="$v_o$"'
VOC = 'gap 5,3 -> 5,0 v="$V_{oc}$"'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(VS, R25, R75, FRAME, LOAD, VO)
OPEN = j(VS, R25, R75, FRAME, VOC)
MESH = '#= mesh 1.25,1.5 "$I$" cw r=0.6'
S25 = j('#= sign 0.6,2.65 +', '#= sign 2.4,2.65 -')
S75 = j('#= sign 3.35,2.3 +', '#= sign 3.35,0.7 -')
SIGNS = j(S25, S75)

TH = j(f'VTH 0,3 -> 0,0 "$150{V}$"', f'RTH 0,3 -> 3,3 "$18.75{K}$"', 'wire 3,3 -> 5,3', 'wire 0,0 -> 5,0',
       'terminal 5,3', 'terminal 5,0')
TH_LOAD = j(TH, 'wire 5,3 -> 7,3', f'R3 7,3 -> 7,0 "$150{K}$"', 'wire 5,0 -> 7,0', VO)
TH_SIGNS = j('#= sign 0.6,2.65 +', '#= sign 2.4,2.65 -', '#= sign 7.35,2.3 +', '#= sign 7.35,0.7 -')

STEPS = [
    ('The circuit', GIVEN, r'''
$R_L$ sits across the output terminals → it's the **load**.

**Plan**
1. Pull out $R_L$ → Thévenin equivalent ($V_{Th}$, $R_{Th}$).
2. (a), (b): put each load on the Thévenin circuit.
3. (c), (d): these ask about resistors **inside** → back to the original circuit.
'''),
    ('Pull out the load', OPEN, r'''
$R_L$ is gone → the terminals are **open**.

The voltage across them is $V_{oc}=V_{Th}$.
'''),
    ('Mesh current', j(OPEN, MESH, SIGNS, r'#+ $I=2\,\mathrm{mA}$'), r'''
One loop. $+$ where $I$ **enters** each resistor.

KVL (sign you enter by):

$$
-200+25kI+75kI=0
$$

$$
100kI=200 \;\Rightarrow\; I=2\,\mathrm{mA}
$$
'''),
    ('Ohm → $V_{oc}$', j(OPEN, SIGNS, '#= path 4.8,3 -> 3,3 -> 3,0 -> 4.7,0', r'#+ $V_{Th}=150\,\mathrm{V}$'), r'''
Walk from the $+$ terminal to the $-$ terminal: down the $75\,\mathrm{k\Omega}$, entering $+$.

$$
V_{oc}=I\cdot 75k=(2m)(75k)=150\,\mathrm{V}
$$

**(a)** No load → $v_o=V_{oc}$:

$$
\boxed{v_o=150\,\mathrm{V}}
$$
'''),
    ('$R_{Th}$: source off', j(R25, 'wire 0,3 -> 0,0', R75, FRAME,
                              '#= path 6.6,1.5 -> 5.25,1.5 thin color=accent', '#= text 6,1.95 "$R_{Th}$" color=accent',
                              r'#+ $R_{Th}=18.75\,\mathrm{k\Omega}$'), r'''
Voltage source off → **wire**.

From the terminals, $25\,\mathrm{k\Omega}$ and $75\,\mathrm{k\Omega}$ both go from the top wire to the bottom wire → **parallel**:

$$
R_{Th}=\frac{(25k)(75k)}{25k+75k}=\frac{1875M}{100k}=18.75\,\mathrm{k\Omega}
$$
'''),
    ('(b) Thévenin circuit + $150\\,\\mathrm{k\\Omega}$', j(TH_LOAD, '#= mesh 3.25,1.5 "$I_b$" cw r=0.8', TH_SIGNS,
                                                         r'#+ $v_o=133.33\,\mathrm{V}$ (b)'), r'''
$V_{Th}$ in series with $R_{Th}$; the $150\,\mathrm{k\Omega}$ load on the terminals.

KVL:

$$
-150+18.75kI_b+150kI_b=0
$$

$$
I_b=\frac{150}{168.75k}=0.889\,\mathrm{mA}
$$

Ohm on the load:

$$
v_o=I_b\cdot150k=\frac{150}{168.75k}(150k)
$$

$$
\boxed{v_o=133.33\,\mathrm{V}}
$$
'''),
    ('(c) Load terminals shorted', j(VS, R25, R75, FRAME, 'wire 5,3 -> 5,0', '#= mesh 1.25,1.5 "$I_c$" cw r=0.6', S25,
                                     r'#+ $p_{25k}=1.6\,\mathrm{W}$ (c)'), r'''
The $25\,\mathrm{k\Omega}$ is **inside** the equivalent → back to the original circuit.

The short sits across the $75\,\mathrm{k\Omega}$ → it carries no current.

KVL (left loop):

$$
-200+25kI_c=0 \;\Rightarrow\; I_c=8\,\mathrm{mA}
$$

Check: $V_{Th}/R_{Th}=150/18.75k=8\,\mathrm{mA}$ ✓

$$
p=I_c^2\cdot25k=(8m)^2(25k)=(64\mu)(25k)
$$

$$
\boxed{p_{25k}=1.6\,\mathrm{W}}
$$
'''),
    ('(d) Most power in the $75\\,\\mathrm{k\\Omega}$', j(OPEN, MESH, S75,
                                                        r'#+ $p_{75k,\max}=0.3\,\mathrm{W}$ (d)'), r'''
$p_{75k}=v_o^2/75k$ → largest when $v_o$ is largest.

Any load pulls $v_o$ below $V_{Th}$ ($v_o=150\cdot\frac{R_L}{18.75k+R_L}<150$) → **no load** is the worst case.

No load: $I=2\,\mathrm{mA}$ (step 3).

$$
p=I^2\cdot75k=(2m)^2(75k)=(4\mu)(75k)
$$

$$
\boxed{p_{75k,\max}=0.3\,\mathrm{W}}
$$
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    assert els['V1'] == (els['R1'][0], els['R2'][1]), els           # + at the top node, - at the bottom
    assert els['R1'][1] == els['R2'][0] == els['R3'][0], els        # middle node carries the 75k and the load
    assert els['R2'][1] == els['R3'][1] == els['V1'][1], els        # one bottom wire
    # (a) open: mesh current, V_oc
    I = 200 / (25e3 + 75e3)
    assert abs(I - 2e-3) < 1e-12
    Voc = I * 75e3
    assert abs(Voc - 150) < 1e-9
    V, _, _ = solve([('V', 'V1', 't', '0', 200), ('R', 'R1', 't', 'm', 25e3), ('R', 'R2', 'm', '0', 75e3)])
    assert abs(V['m'] - 150) < 1e-9
    # R_Th
    Rth = 25e3 * 75e3 / 100e3
    assert abs(Rth - 18.75e3) < 1e-9 and abs(25e3 * 75e3 / 1e6 - 1875) < 1e-9
    # (b) 150k load on the equivalent, and on the original circuit
    Ib = 150 / (Rth + 150e3)
    assert abs(Ib - 0.889e-3) < 5e-7
    vo = Ib * 150e3
    assert abs(vo - 133.33) < 5e-3
    V, _, _ = solve([('V', 'V1', 't', '0', 200), ('R', 'R1', 't', 'm', 25e3), ('R', 'R2', 'm', '0', 75e3),
                     ('R', 'R3', 'm', '0', 150e3)])
    assert abs(V['m'] - vo) < 1e-9
    # (c) short across the load
    Ic = 200 / 25e3
    assert abs(Ic - 8e-3) < 1e-12 and abs(Voc / Rth - Ic) < 1e-12
    assert abs(Ic ** 2 * 25e3 - 1.6) < 1e-12 and abs((8e-3) ** 2 - 64e-6) < 1e-18
    # (d) no load gives the largest v_o, hence the largest p_75k
    assert all(150 * RL / (Rth + RL) < 150 for RL in (1e3, 150e3, 1e9))
    assert abs(I ** 2 * 75e3 - 0.3) < 1e-12 and abs(150 ** 2 / 75e3 - 0.3) < 1e-12
