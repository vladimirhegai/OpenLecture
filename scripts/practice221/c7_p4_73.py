r"""Textbook P4.73: a 100 kΩ voltmeter on a-b. V_oc by mesh + Ohm (a supermesh around the 8 mA source),
R_Th with the sources off, then the meter as a load on the Thévenin circuit."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'C'
TITLE = 'Thévenin: a voltmeter that loads the circuit'
SOURCE = 'Textbook P4.73'
CITES = [{"chunk_id": "0da028c8-138a-47c7-8ee5-99ac30e9dc71", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1}]
PROMPT = (r'A $100\,\mathrm{k\Omega}$ voltmeter measures $v_{ab}$. **(a)** What does it read? '
          r'**(b)** What is the percentage error, $\dfrac{\text{measured}-\text{actual}}{\text{actual}}\times100$?')

K = r'\,\mathrm{k\Omega}'
R1 = f'R1 0,4 -> 0,2 "$10{K}$"'
V1 = r'V1 0,2 -> 0,0 "$30\,\mathrm{V}$"'
R2 = f'R2 3,4 -> 3,0 "$40{K}$"'
R3 = f'R3 3,4 -> 6,4 "$4{K}$"'
I1 = r'I1 6,0 -> 6,4 "$8\,\mathrm{mA}$"'
R4 = f'R4 6,4 -> 9,4 "$3{K}$"'
R5 = f'R5 9,4 -> 9,0 "$10{K}$"'
FRAME = '\n'.join(['wire 0,4 -> 3,4', 'wire 9,4 -> 11,4', 'terminal 11,4 "$a$" right', 'terminal 11,0 "$b$" right',
                   'wire 0,0 -> 11,0', 'label 3,4 "$p$" above', 'label 6,4 "$q$" above', 'ground 0,0'])
VOC = 'gap 11,4 -> 11,0 v="$V_{oc}$"'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(R1, V1, R2, R3, I1, R4, R5, FRAME)
CIRCUIT = j(R1, V1, R2, R3, I1, R4, R5, FRAME, VOC)

# rings in the upper half of each window: the vertical elements' labels sit at mid-height inside the windows
MESHES = '\n'.join(['#= mesh 1.5,2.9 "$I_1$" cw r=0.45', '#= mesh 4.6,2.85 "$I_2$" cw r=0.45', '#= mesh 7.5,2.85 "$I_3$" cw r=0.45'])
SUPER = '#= region 3.2,0.2 8.8,3.8 "supermesh"'
# mesh 1: up the 10 kΩ, down the 40 kΩ
SIGNS_1 = '\n'.join(['#= sign 0.35,2.35 +', '#= sign 0.35,3.65 -', '#= sign 2.65,2.8 +', '#= sign 2.65,1.2 -'])
# supermesh: up the 40 kΩ (I_2), right along 4 kΩ and 3 kΩ, down the 10 kΩ (I_3)
SIGNS_S = '\n'.join(['#= sign 3.35,1.2 +', '#= sign 3.35,2.8 -', '#= sign 3.7,3.65 +', '#= sign 5.3,3.65 -',
                     '#= sign 6.7,3.65 +', '#= sign 8.3,3.65 -', '#= sign 8.65,2.8 +', '#= sign 8.65,1.2 -'])
WALK = '#= path 10.75,4 -> 9,4 -> 9,0 -> 10.7,0'
WALK_SIGNS = '#= sign 8.65,2.8 +\n#= sign 8.65,1.2 -'

OFF = j(R1, 'wire 0,2 -> 0,0', R2, R3, R4, R5, 'wire 6,0 -> 6,0.6', 'wire 6,4 -> 6,3.4', FRAME)
LOOK = '#= path 12.4,2 -> 11.25,2 thin color=accent\n#= text 12,2.45 "$R_{Th}$" color=accent'

METER = j(r'VTH 0,4 -> 0,0 "$48\,\mathrm{V}$"', f'RTH 0,4 -> 6,4 "$6{K}$"', 'wire 6,4 -> 9,4',
          f'RM 9,4 -> 9,0 "$100{K}$"', 'wire 9,4 -> 11,4', 'terminal 11,4 "$a$" right', 'terminal 11,0 "$b$" right',
          'wire 0,0 -> 11,0', 'ground 0,0', 'gap 11,4 -> 11,0 v="$v_m$"')

STEPS = [
    ('The circuit', CIRCUIT, r'''
**Actual** $v_{ab}$ = the open-circuit voltage $V_{oc}$ (an ideal meter draws no current).

**Measured** = the voltage with the $100\,\mathrm{k\Omega}$ meter hung on $a$–$b$: a **load**.

**Plan**
1. $V_{Th}=V_{oc}$ with mesh + Ohm.
2. $R_{Th}$: sources off.
3. Thévenin circuit + meter → reading.
'''),
    ('Mesh currents + supermesh', j(CIRCUIT, MESHES, SUPER), r'''
Three windows → $I_1$, $I_2$, $I_3$ (clockwise).

The $8\,\mathrm{mA}$ source sits between $I_2$ and $I_3$ → **supermesh** around both.

Up the source: $I_3$ goes up, $I_2$ goes down:

$$
I_3-I_2=8m
$$
'''),
    ('KVL mesh 1', j(CIRCUIT, MESHES, SUPER, SIGNS_1), r'''
Signs you enter by:
- $30\,\mathrm{V}$: enter $-$ → $-30$
- $10\,\mathrm{k\Omega}$: $+10kI_1$
- $40\,\mathrm{k\Omega}$ (shared with $I_2$): $+40k(I_1-I_2)$

$$
-30+10kI_1+40k(I_1-I_2)=0
$$

$$
50kI_1-40kI_2=30
$$
'''),
    ('KVL around the supermesh', j(CIRCUIT, MESHES, SUPER, SIGNS_S, r'#+ $I_1=-1.96\,\mathrm{mA}$',
                                   r'#+ $I_2=-3.2\,\mathrm{mA}$', r'#+ $I_3=4.8\,\mathrm{mA}$'), r'''
Walk the outside of the box:

$$
40k(I_2-I_1)+4kI_2+3kI_3+10kI_3=0
$$

Use $I_3=I_2+8m$ (so $13k\cdot8m=104$):

$$
-40kI_1+57kI_2=-104
$$

With mesh 1, $I_1=0.6m+0.8I_2$:

$$
25kI_2=-80 \;\Rightarrow\; I_2=-3.2\,\mathrm{mA}
$$

$$
I_1=-1.96\,\mathrm{mA} \qquad I_3=4.8\,\mathrm{mA}
$$
'''),
    ('KVL walk to $V_{oc}$', j(CIRCUIT, WALK, WALK_SIGNS, r'#+ $V_{Th}=48\,\mathrm{V}$'), r'''
Walk from $a$ to $b$: down the $10\,\mathrm{k\Omega}$, walking with $I_3$ → enter $+$.

$$
V_{oc}=10k\cdot I_3=(10k)(4.8m)=48\,\mathrm{V}
$$

$$
\boxed{V_{Th}=48\,\mathrm{V}}
$$
'''),
    ('$R_{Th}$: sources off', j(OFF, LOOK, r'#+ $R_{Th}=6\,\mathrm{k\Omega}$'), r'''
$30\,\mathrm{V}$ off → **wire**. $8\,\mathrm{mA}$ off → **open**.

Look in from $a$:
- $10k$ and $40k$ both go from $p$ to the bottom → parallel: $8k$
- then $4k$ and $3k$ in series: $8k+4k+3k=15k$
- that is in parallel with the right $10k$

$$
R_{Th}=\frac{(15k)(10k)}{15k+10k}=6\,\mathrm{k\Omega}
$$
'''),
    ('Thévenin circuit + the meter', j(METER, '#= mesh 4.5,2 "$I$" cw r=0.8'), r'''
$48\,\mathrm{V}$ in series with $6\,\mathrm{k\Omega}$; the meter is a $100\,\mathrm{k\Omega}$ load.

One loop → one mesh current $I$.
'''),
    ('Mesh + Ohm → reading and error',
     j(METER, '#= mesh 4.5,2 "$I$" cw r=0.8', '#= sign 2.2,3.65 +', '#= sign 3.8,3.65 -', '#= sign 8.65,2.8 +',
       '#= sign 8.65,1.2 -', r'#+ $v_m=45.28\,\mathrm{V}$', r'#+ $\text{error}=-5.66\%$'), r'''
$$
-48+6kI+100kI=0 \;\Rightarrow\; I=\frac{48}{106k}=0.4528\,\mathrm{mA}
$$

Ohm on the meter:

$$
v_m=(100k)(0.4528m)=45.28\,\mathrm{V}
$$

$$
\text{error}=\frac{45.28-48}{48}\times100=-5.66\%
$$

$$
\boxed{\text{(a) } 45.28\,\mathrm{V} \qquad \text{(b) } -5.66\%}
$$
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    top, mid = els['R1']
    p = els['R2'][0]
    q, a = els['R4']
    assert els['V1'] == (mid, '0') and p == top and els['R3'] == (p, q), els
    assert els['I1'] == ('0', q) and els['R5'] == (a, '0') and els['R2'] == (p, '0'), els
    # mesh equations, exact (kΩ, mA, V)
    I2 = F(-16, 5)
    I1 = F(3, 5) + F(4, 5) * I2
    I3 = I2 + 8
    assert (I1, I3) == (F(-49, 25), F(24, 5))
    assert -30 + 10 * I1 + 40 * (I1 - I2) == 0 and 50 * I1 - 40 * I2 == 30
    assert 40 * (I2 - I1) + 4 * I2 + 3 * I3 + 10 * I3 == 0 and -40 * I1 + 57 * I2 == -104 and 13 * 8 == 104
    assert -24 - 32 * I2 + 57 * I2 == -104 and 25 * I2 == -80
    Vth = 10 * I3
    assert Vth == 48
    assert F(10 * 40, 50) == 8 and 8 + 4 + 3 == 15 and F(15 * 10, 25) == 6
    I = F(48, 106)
    vm = 100 * I
    assert -48 + 6 * I + 100 * I == 0 and round(float(I), 4) == 0.4528 and round(float(vm), 2) == 45.28
    assert round(float((vm - 48) / 48 * 100), 2) == -5.66
    # independent nodal solves (kΩ, mA)
    net = [('R', 'R1', 'top', 'mid', 10), ('V', 'V1', 'mid', '0', 30), ('R', 'R2', 'top', '0', 40),
           ('R', 'R3', 'top', 'q', 4), ('I', 'I1', '0', 'q', 8), ('R', 'R4', 'q', 'a', 3), ('R', 'R5', 'a', '0', 10)]
    V, _, _ = solve(net)
    assert abs(V['a'] - 48) < 1e-9
    V, _, _ = solve(net + [('R', 'RM', 'a', '0', 100)])
    assert abs(V['a'] - float(vm)) < 1e-9
