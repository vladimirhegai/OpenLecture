r"""Textbook P4.69: recover the Thévenin equivalent of a box from two load measurements.
Ohm's law gives each load current; KVL around the Thévenin model gives two equations in V_Th and R_Th."""
from fractions import Fraction as F

SECTION = 'C'
TITLE = 'Thévenin: work backwards from two measurements'
SOURCE = 'Textbook P4.69'
CITES = [{"chunk_id": "0da028c8-138a-47c7-8ee5-99ac30e9dc71", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1}]
PROMPT = (r'A box holds an unknown linear circuit. A $15\,\mathrm{k\Omega}$ load on $a$–$b$ reads $v_{ab}=45\,\mathrm{V}$; '
          r'a $5\,\mathrm{k\Omega}$ load reads $25\,\mathrm{V}$. Find the Thévenin equivalent.')

K = r'\,\mathrm{k\Omega}'
TERMS = '\n'.join(['terminal 5,3 "$a$" above', 'terminal 5,0 "$b$" below', 'ground 0,0'])
BOX = '\n'.join(['X1 0,3 -> 0,0 "network"', 'wire 0,3 -> 5,3', 'wire 0,0 -> 5,0'])


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(BOX, 'RL 5,3 -> 5,0 "$R_L$" flip', TERMS)
MEAS1 = j(BOX, f'RL 5,3 -> 5,0 "$15{K}$" i="$I_1$" v="$45\\,\\mathrm{{V}}$"', TERMS)
MEAS2 = j(BOX, f'RL 5,3 -> 5,0 "$5{K}$" i="$I_2$" v="$25\\,\\mathrm{{V}}$"', TERMS)


def model(vth, rth, rl, v):
    return j(f'VTH 0,3 -> 0,0 "{vth}"', f'RTH 0,3 -> 3,3 "{rth}"', 'wire 3,3 -> 5,3', 'wire 0,0 -> 5,0',
             f'RL 5,3 -> 5,0 "{rl}" v="{v}"', TERMS)


MODEL = model(r'$V_{Th}$', r'$R_{Th}$', r'$R_L$', r'$v$')
FINAL = model(r'$75\,\mathrm{V}$', f'$10{K}$', r'$R_L$', r'$v$')
CHECK = model(r'$75\,\mathrm{V}$', f'$10{K}$', f'$15{K}$', r'$45\,\mathrm{V}$')
MESH = '#= mesh 2.5,1.5 "$I$" cw r=0.75'
SIGNS = '\n'.join(['#= sign 0.8,2.65 +', '#= sign 2.2,2.65 -', '#= sign 4.65,2.3 +', '#= sign 4.65,0.7 -'])

STEPS = [
    ('Measurement 1', j(MEAS1, r'#+ $I_1=3\,\mathrm{mA}$'), r'''
We can't see inside the box, but every linear box looks like $V_{Th}$ in series with $R_{Th}$.

Ohm's law on the $15\,\mathrm{k\Omega}$ load:

$$
I_1=\frac{45}{15k}=3\,\mathrm{mA}
$$
'''),
    ('Measurement 2', j(MEAS2, r'#+ $I_2=5\,\mathrm{mA}$'), r'''
Ohm's law on the $5\,\mathrm{k\Omega}$ load:

$$
I_2=\frac{25}{5k}=5\,\mathrm{mA}
$$

A smaller load pulls more current, so less voltage is left at $a$–$b$.
'''),
    ('Swap the box for its Thévenin model', j(MODEL, MESH, SIGNS), r'''
One loop → mesh current $I$ (clockwise). Signs you enter by:
- $V_{Th}$: enter $-$ → $-V_{Th}$
- $R_{Th}$: $+R_{Th}I$
- load: $+v$

$$
-V_{Th}+R_{Th}I+v=0 \;\Rightarrow\; V_{Th}=v+R_{Th}I
$$
'''),
    ('Two equations, two unknowns', j(FINAL, MESH, SIGNS, r'#+ $R_{Th}=10\,\mathrm{k\Omega}$',
                                      r'#+ $V_{Th}=75\,\mathrm{V}$'), r'''
Plug in both measurements:

$$
V_{Th}=45+(3m)R_{Th}
$$

$$
V_{Th}=25+(5m)R_{Th}
$$

Subtract: $0=20-(2m)R_{Th}$

$$
R_{Th}=\frac{20}{2m}=10\,\mathrm{k\Omega} \qquad V_{Th}=45+(3m)(10k)=75\,\mathrm{V}
$$

$$
\boxed{V_{Th}=75\,\mathrm{V} \qquad R_{Th}=10\,\mathrm{k\Omega}}
$$
'''),
    ('Check with the $15\\,\\mathrm{k\\Omega}$ load', j(CHECK, MESH, SIGNS), r'''
$$
-75+10kI+15kI=0 \;\Rightarrow\; I=\frac{75}{25k}=3\,\mathrm{mA}
$$

$$
v=(15k)(3m)=45\,\mathrm{V} \;✓
$$

Same with $5\,\mathrm{k\Omega}$: $I=\frac{75}{15k}=5\,\mathrm{mA}$, $v=25\,\mathrm{V}$ ✓
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    assert els['X1'] == (els['RL'][0], els['RL'][1]) and els['RL'][1] == '0', els
    els, _ = check(MODEL)
    assert els['VTH'][0] == els['RTH'][0] and els['RTH'][1] == els['RL'][0] and els['VTH'][1] == els['RL'][1] == '0', els
    I1, I2 = F(45, 15), F(25, 5)  # mA (V / kΩ)
    assert (I1, I2) == (3, 5)
    Rth = F(45 - 25, I2 - I1)     # kΩ
    Vth = 45 + I1 * Rth
    assert Rth == 10 and Vth == 75 and 25 + I2 * Rth == 75
    for RL, v in ((15, 45), (5, 25)):
        I = Vth / (Rth + RL)
        assert -Vth + Rth * I + RL * I == 0 and RL * I == v
    assert F(75, 25) == 3 and F(75, 15) == 5
