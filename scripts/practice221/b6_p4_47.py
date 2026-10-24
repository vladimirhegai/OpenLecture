r"""Textbook P4.47: a perimeter current source fixes I1; a dependent voltage source (200 i_Δ) is controlled by the
shared-branch current i_Δ, which points against mesh 1 → i_Δ = I2 − I1. Mesh + Ohm, then KVL walks for the
source voltages and the delivered powers. Units kΩ and mA (k·m = 1)."""
from fractions import Fraction as F

SECTION = 'B'
TITLE = 'A dependent source watches the shared branch'
SOURCE = 'Textbook P4.47'
CITES = [{"chunk_id": "6011993f-3c2e-4dd5-90d1-9ba11990ec2a", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1}]
PROMPT = (r'Find **(a)** $i_\Delta$; **(b)** the power delivered by the independent current source; '
          r'**(c)** the power delivered by the dependent voltage source.')

K = r'\,\mathrm{k\Omega}'


def j(*parts):
    return '\n'.join(parts)


I1 = r'I1 0,0 -> 0,3 "$8\,\mathrm{mA}$"'
R1 = r'R1 0,3 -> 3.5,3 "$980\,\Omega$"'
R2 = f'R2 3.5,3 -> 3.5,0 "$3.3{K}$" i_rev="$i_\\Delta$"'
R3 = f'R3 3.5,3 -> 7.5,3 "$1.8{K}$"'
E1 = r'E1 7.5,3 -> 7.5,0 "$200i_\Delta$"'
R4 = f'R4 7.5,0 -> 3.5,0 "$4.7{K}$"'
REST = j('wire 3.5,0 -> 0,0', 'label 0,3 "$s$" above', 'label 3.5,3 "$a$" above', 'ground 0,0')
GIVEN = j(I1, R1, R2, R3, E1, R4, REST)

MESHES = j('#= mesh 1.6,1.5 "$I_1$" cw r=0.5', '#= mesh 5.4,1.5 "$I_2$" cw r=0.5')
I1_FIXED = r'#= text 1.6,0.45 "$I_1=8\,\mathrm{mA}$" color=purple'
CONTROL = j('#= path 3.5,0.35 -> 3.5,2.65 thin color=orange', r'#= text 4.4,2.4 "$I_2-I_1$" color=orange')
SIGNS_2 = j('#= sign 4.3,2.65 +', '#= sign 7.1,2.65 -',       # 1.8 kΩ: I2 goes right
            '#= sign 7.1,0.35 +', '#= sign 4.3,0.35 -',       # 4.7 kΩ: I2 goes left
            '#= sign 3.85,0.7 +', '#= sign 3.85,2.3 -')       # 3.3 kΩ: I2 goes up
WALK = '#= path 0,3 -> 3.5,3 -> 3.5,0 -> 0.45,0'

STEPS = [
    ('The circuit', GIVEN, r'''
**Method: mesh.** The $8\,\mathrm{mA}$ source is on the outer edge → it fixes one mesh, leaving 1 unknown.

The dependent source is controlled by a **branch** current → write $i_\Delta$ from mesh currents.
'''),
    ('Mesh currents', j(GIVEN, MESHES, I1_FIXED, r'#+ $I_1=8\,\mathrm{mA}$'), r'''
Clockwise $I_1$ (left) and $I_2$ (right).

Only $I_1$ runs through the $8\,\mathrm{mA}$ source, same way as its arrow (up the left edge):

$$
I_1=8\,\mathrm{mA}
$$
'''),
    ('The control current from mesh currents', j(GIVEN, MESHES, I1_FIXED, CONTROL), r'''
$i_\Delta$ points **up** the $3.3\,\mathrm{k\Omega}$:
- $I_2$ goes **up** there → $+I_2$
- $I_1$ goes **down** there → $-I_1$

$$
i_\Delta=I_2-I_1
$$

So the dependent source is $200(I_2-I_1)=0.2k(I_2-I_1)$.
'''),
    ('KVL in mesh 2', j(GIVEN, MESHES, I1_FIXED, SIGNS_2), r'''
Walk with $I_2$; sign you **enter** each element by:
- $1.8\,\mathrm{k\Omega}$: $+1.8kI_2$
- $200i_\Delta$: enter $+$ → $+0.2k(I_2-I_1)$
- $4.7\,\mathrm{k\Omega}$: $+4.7kI_2$
- $3.3\,\mathrm{k\Omega}$ (shared): $+3.3k(I_2-I_1)$

$$
1.8kI_2+0.2k(I_2-I_1)+4.7kI_2+3.3k(I_2-I_1)=0
$$

$$
10kI_2=3.5kI_1=3.5k(8m)
$$
'''),
    ('Solve', j(GIVEN, MESHES, I1_FIXED, r'#= text 5.4,0.45 "$I_2=2.8\,\mathrm{mA}$" color=purple',
                r'#+ $I_2=2.8\,\mathrm{mA}$', r'#+ $i_\Delta=-5.2\,\mathrm{mA}$'), r'''
$$
I_2=\frac{3.5(8m)}{10}=2.8\,\mathrm{mA}
$$

$$
\boxed{i_\Delta=I_2-I_1=2.8m-8m=-5.2\,\mathrm{mA}}
$$

Negative → $5.2\,\mathrm{mA}$ really flows **down** the $3.3\,\mathrm{k\Omega}$.
'''),
    ('Voltage across the $8\\,\\mathrm{mA}$ source', j(GIVEN, WALK, r'#= text 1.75,2.5 "$7.84\,\mathrm{V}$" color=pink',
                                                      r'#= text 2.6,1.5 "$17.16\,\mathrm{V}$" color=pink',
                                                      r'#+ $v_s=25\,\mathrm{V}$'), r'''
Walk from $s$ down to ground through the $980\,\Omega$ and the $3.3\,\mathrm{k\Omega}$ (Ohm's law on each):
- $980\,\Omega$ carries $I_1=8\,\mathrm{mA}$ to the right → $+$ on the left: $(8m)(980)=7.84\,\mathrm{V}$
- $3.3\,\mathrm{k\Omega}$ carries $5.2\,\mathrm{mA}$ down → $+$ on top: $(5.2m)(3.3k)=17.16\,\mathrm{V}$

$$
v_s=7.84+17.16=25\,\mathrm{V}
$$
'''),
    ('Delivered powers', j(GIVEN, r'#= text 1.6,1.5 "$200\,\mathrm{mW}$" color=green',
                           r'#= text 8.5,0.6 "$2.912\,\mathrm{mW}$" color=green',
                           r'#+ $p_{8\mathrm{mA}}=200\,\mathrm{mW}$', r'#+ $p_{dep}=2.912\,\mathrm{mW}$'), r'''
**$8\,\mathrm{mA}$ source:** its current leaves the top ($+$) → delivers

$$
\boxed{p=v_sI_1=(25)(8m)=200\,\mathrm{mW}}
$$

**Dependent source:** $v=200i_\Delta=0.2k(-5.2m)=-1.04\,\mathrm{V}$ ($+$ on top).

$I_2$ enters its $+$ → it absorbs $vI_2=(-1.04)(2.8m)=-2.912\,\mathrm{mW}$, so it delivers

$$
\boxed{p=2.912\,\mathrm{mW}}
$$
'''),
]


def _mna():
    import os
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
    import mna
    return mna


def checks(check):
    els, _ = check(GIVEN)
    s, a = els['R1']
    assert els['I1'] == ('0', s) and els['R2'] == (a, '0') and els['R3'][0] == a, els
    top, bot = els['R3'][1], els['E1'][1]
    assert els['E1'][0] == top and bot != '0' and els['R4'] == (bot, '0'), els
    # independent solve (ohms, amps): i_Δ = current up the 3.3k = (0 - Va)/3300
    V, I, P = _mna().solve([('I', 'I1', '0', 's', 0.008), ('R', 'R1', 's', 'a', 980), ('R', 'R2', 'a', '0', 3300),
                            ('R', 'R3', 'a', 't', 1800), ('E', 'E1', 't', 'b', {'a': -200 / 3300}, 0),
                            ('R', 'R4', 'b', '0', 4700)])
    i_d = -V['a'] / 3300
    assert abs(i_d - (-0.0052)) < 1e-12 and abs(V['s'] - 25) < 1e-9
    assert abs(-P['I1'] - 0.2) < 1e-12 and abs(-P['E1'] - 0.002912) < 1e-12
    # the arithmetic in the notes (mA, kΩ)
    I1, I2 = 8, F(28, 10)
    assert F(35, 10) * I1 / 10 == I2
    assert F(18, 10) * I2 + F(2, 10) * (I2 - I1) + F(47, 10) * I2 + F(33, 10) * (I2 - I1) == 0
    assert I2 - I1 == F(-52, 10)
    assert F(784, 100) == I1 * F(98, 100) and F(1716, 100) == F(52, 10) * F(33, 10) and F(784, 100) + F(1716, 100) == 25
    assert 25 * I1 == 200
    v_dep = F(2, 10) * (I2 - I1)
    assert v_dep == F(-104, 100) and v_dep * I2 == F(-2912, 1000)
