r"""Assessment AP 4.21 (Textbook P4.85(a–b), P4.86): max power with a voltage-controlled voltage source.
V_oc by two meshes, I_sc by three (the dependent source stays on, so R_Th = V_oc/I_sc), matched load on the
Thévenin circuit, then the efficiency back in the original circuit (three meshes again)."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'D'
TITLE = 'Max power: efficiency with a dependent source'
SOURCE = 'Assessment Problem 4.21 (Textbook P4.85, P4.86)'
CITES = [{"chunk_id": "b0235d23-0c76-4c5a-a836-0e357eaa83a0", "source_id": "3b287f2d-b408-41eb-a523-b299688ff303", "version": 1},
         {"chunk_id": "5dd7f364-970c-4123-bcdc-27d3503702c9", "source_id": "3b287f2d-b408-41eb-a523-b299688ff303", "version": 1},
         {"chunk_id": "214ce707-5384-4d62-a006-74f1460864bd", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1}]
PROMPT = (r'$R_o$ is set for maximum power; $v_\phi$ is the voltage across the $4\,\Omega$ in series with the '
          r'$20\,\mathrm{V}$ source. **(a)** Find $R_o$. **(b)** Find $p_{\max}$. '
          r'**(c)** What percentage of the power developed reaches $R_o$?')

O = r'\,\Omega'
V = r'\,\mathrm{V}'
A = r'\,\mathrm{A}'
W = r'\,\mathrm{W}'
V1 = f'V1 0,4 -> 0,0 "$100{V}$"'
R1 = f'R1 0,4 -> 3,4 "$4{O}$"'
R2 = f'R2 3,4 -> 6,4 "$4{O}$"'
R3 = f'R3 3,4 -> 3,2 "$4{O}$" v="$v_\\phi$"'
V2 = f'V2 3,2 -> 3,0 "$20{V}$"'
TOP = '\n'.join(['wire 0,4 -> 0,6', 'E1 3,6 -> 0,6 "$v_\\phi$"', f'R4 3,6 -> 6,6 "$4{O}$"', 'wire 6,6 -> 6,4'])
WIRES = '\n'.join(['wire 6,4 -> 8,4', 'wire 0,0 -> 8,0'])
LABELS = '\n'.join(['label 3,4 "$c$" below', 'label 3,6 "$t$" above', 'label 8,4 "$a$" above', 'ground 0,0'])
TERMS = '\n'.join(['terminal 8,4', 'terminal 8,0'])
RO = f'RO 8,4 -> 8,0 "$R_o$"'


def j(*parts):
    return '\n'.join(parts)


CIRCUIT = j(V1, R1, R2, R3, V2, TOP, WIRES, LABELS)
GIVEN = j(CIRCUIT, RO)
OPEN = j(CIRCUIT, TERMS, 'gap 8,4 -> 8,0 v="$V_{oc}$"')
SHORT = j(CIRCUIT, TERMS, 'wire 8,4 -> 8,0', '#= text 8.6,2 "short"')
LOADED = j(CIRCUIT, f'RO 8,4 -> 8,0 "$3{O}$"')

M1 = '#= mesh 1.5,2 "$I_1$" cw r=0.7'
M3 = '#= mesh 3,5 "$I_3$" cw r=0.55'
M2 = '#= mesh 5.5,2 "$I_2$" cw r=0.7'
# mesh 1 signs: + where I1 enters (R1 left end, R3 top)
S1 = j('#= sign 0.45,3.6 +', '#= sign 2.55,3.6 -', '#= sign 3.45,3.65 +', '#= sign 3.45,2.35 -')
# mesh 3 signs: R4 left end, R2 right end (a), R1 right end (c)
S3 = j('#= sign 3.45,5.6 +', '#= sign 5.55,5.6 -', '#= sign 5.55,4.4 +', '#= sign 3.45,4.4 -',
       '#= sign 2.55,4.4 +', '#= sign 0.45,4.4 -')
WALK = '#= path 8,4 -> 3,4 -> 3,0 -> 7.7,0'

VTH = f'#+ $V_{{Th}}=120{V}$'
ISC = f'#+ $I_{{sc}}=40{A}$'
RTH = f'#+ $R_o=R_{{Th}}=3{O}$'
PMAX = f'#+ $p_{{max}}=1200{W}$'
ETA = r'#+ $\eta=31.6\,\%$'

THEV = j(f'VTH 0,4 -> 0,0 "$120{V}$"', f'RTH 0,4 -> 4,4 "$3{O}$"', 'wire 4,4 -> 8,4',
         f'RO 8,4 -> 8,0 "$R_o=3{O}$"', 'wire 0,0 -> 8,0', 'label 8,4 "$a$" above', 'ground 0,0')

STEPS = [
    ('The circuit', GIVEN, r'''
Max power → $R_o=R_{Th}$, the Thévenin resistance seen by $R_o$.

The dependent source can't be turned off → $R_{Th}=V_{oc}/I_{sc}$.

**Plan**
1. $V_{oc}$ with $R_o$ removed.
2. $I_{sc}$ with $a$ shorted to ground.
3. Matched load on the Thévenin circuit → $p_{max}$.
4. Efficiency back in the original circuit.
'''),
    ('Pull out $R_o$', OPEN, r'''
$R_o$ is gone → $a$ is open.

The window right of the $20\,\mathrm{V}$ is no longer a closed loop → only **two** meshes.
'''),
    ('Two meshes', j(OPEN, M1, M3), r'''
$I_1$: the lower-left window. $I_3$: the top window.

$I_1$ is the only current down the $4\,\Omega$ that carries $v_\phi$ (+ on top):

$$
v_\phi=4I_1
$$
'''),
    ('Mesh 1 KVL', j(OPEN, M1, M3, S1), r'''
Signs you **enter** by, going with $I_1$:
- $100\,\mathrm{V}$: enter $-$ → $-100$
- top $4\,\Omega$: $+4(I_1-I_3)$
- $4\,\Omega$ ($v_\phi$): $+4I_1$
- $20\,\mathrm{V}$: enter $+$ → $+20$

$$
-100+4(I_1-I_3)+4I_1+20=0
$$

$$
8I_1-4I_3=80
$$
'''),
    ('Mesh 3 KVL → solve', j(OPEN, M1, M3, S3, f'#+ $I_1=15{A}$', f'#+ $I_3=10{A}$'), r'''
Going with $I_3$:
- $v_\phi$ source: enter $-$ → $-v_\phi=-4I_1$
- $4\,\Omega$, $4\,\Omega$ (top right, then $a\to c$): $+4I_3+4I_3$
- $4\,\Omega$ ($c$ to the $100\,\mathrm{V}$): $+4(I_3-I_1)$

$$
-4I_1+4I_3+4I_3+4(I_3-I_1)=0\;\Rightarrow\;I_3=\tfrac23 I_1
$$

Into mesh 1:

$$
8I_1-\tfrac83 I_1=80\;\Rightarrow\;I_1=15\,\mathrm{A},\quad I_3=10\,\mathrm{A}
$$
'''),
    ('Walk to $V_{oc}$', j(OPEN, WALK, VTH), r'''
Walk from $a$ down to ground, signs you **enter** by:
- $4\,\Omega$ ($a\to c$, with $I_3$): $+4I_3=+40$
- $4\,\Omega$ (down, with $I_1$): $+4I_1=+60$
- $20\,\mathrm{V}$: enter $+$ → $+20$

$$
V_{oc}=40+60+20=120\,\mathrm{V}
$$
'''),
    ('Short $a$: three meshes', j(SHORT, M1, M2, M3, ISC), r'''
The short closes the right window → mesh $I_2$. Now $v_\phi=4(I_1-I_2)$.

$$
-100+4(I_1-I_3)+4(I_1-I_2)+20=0
$$

$$
4(I_2-I_3)-20+4(I_2-I_1)=0
$$

$$
-4(I_1-I_2)+4I_3+4(I_3-I_2)+4(I_3-I_1)=0
$$

Solve: $I_1=45\,\mathrm{A}$, $I_2=40\,\mathrm{A}$, $I_3=30\,\mathrm{A}$.

$I_2$ is the only current down the short → $I_{sc}=40\,\mathrm{A}$.
'''),
    ('Thévenin circuit, matched load', j(THEV, '#= mesh 4,2 "$I$" cw r=0.8', RTH, PMAX), r'''
$$
R_{Th}=\frac{V_{oc}}{I_{sc}}=\frac{120}{40}=3\,\Omega
$$

Max power → $R_o=3\,\Omega$. KVL with $I$:

$$
-120+3I+3I=0\;\Rightarrow\;I=20\,\mathrm{A}
$$

$$
p_{max}=I^2R_o=(20)^2(3)=1200\,\mathrm{W}
$$
'''),
    ('Efficiency: back to the original', j(LOADED, M1, M2, M3, ETA), r'''
The equivalent can't give the sources' powers → original circuit with $R_o=3\,\Omega$ (mesh 2 gains $+3I_2$):

$I_1=30\,\mathrm{A}$, $I_2=20\,\mathrm{A}$ (through $R_o$ ✓), $I_3=20\,\mathrm{A}$, $v_\phi=4(I_1-I_2)=40\,\mathrm{V}$.

Developed (current leaves the $+$ end):
- $100\,\mathrm{V}$: $(100)(30)=3000\,\mathrm{W}$
- $v_\phi$ source: $(40)(20)=800\,\mathrm{W}$
- ($20\,\mathrm{V}$ absorbs $(20)(10)=200\,\mathrm{W}$)

$$
\eta=\frac{1200}{3000+800}=31.6\,\%
$$
'''),
]


def _mna(extra):
    el = [('V', 'V1', 'n', '0', 100), ('R', 'R1', 'n', 'c', 4), ('R', 'R2', 'c', 'a', 4), ('R', 'R3', 'c', 'd', 4),
          ('V', 'V2', 'd', '0', 20), ('E', 'E1', 't', 'n', {'c': 1, 'd': -1}, 0), ('R', 'R4', 't', 'a', 4)]
    return solve(el + extra)


def checks(check):
    els, _ = check(GIVEN)
    assert els['V1'][0] == els['R1'][0] and els['R1'][1] == els['R2'][0] == els['R3'][0], els
    assert els['R3'][1] == els['V2'][0] and els['V2'][1] == '0' and els['RO'][1] == '0', els
    assert els['E1'][0] == els['R4'][0] and els['E1'][1] == els['V1'][0] and els['R4'][1] == els['R2'][1] == els['RO'][0], els
    # open: two meshes
    I1, I3 = F(15), F(10)
    assert 8 * I1 - 4 * I3 == 80 and -4 * I1 + 4 * I3 + 4 * I3 + 4 * (I3 - I1) == 0
    assert 4 * I3 + 4 * I1 + 20 == 120
    Vo, _, _ = _mna([])
    assert abs(Vo['a'] - 120) < 1e-9
    # short: three meshes
    I1, I2, I3 = F(45), F(40), F(30)
    assert -100 + 4 * (I1 - I3) + 4 * (I1 - I2) + 20 == 0
    assert 4 * (I2 - I3) - 20 + 4 * (I2 - I1) == 0
    assert -4 * (I1 - I2) + 4 * I3 + 4 * (I3 - I2) + 4 * (I3 - I1) == 0
    _, Is, _ = _mna([('V', 'VS', 'a', '0', 0)])
    assert abs(Is['VS'] - 40) < 1e-9
    assert F(120, 40) == 3 and F(120, 6) == 20 and 20 ** 2 * 3 == 1200
    # loaded, R_o = 3
    I1, I2, I3 = F(30), F(20), F(20)
    assert -100 + 4 * (I1 - I3) + 4 * (I1 - I2) + 20 == 0
    assert 4 * (I2 - I3) - 20 + 4 * (I2 - I1) + 3 * I2 == 0
    assert -4 * (I1 - I2) + 4 * I3 + 4 * (I3 - I2) + 4 * (I3 - I1) == 0
    Vl, Il, Pl = _mna([('R', 'RO', 'a', '0', 3)])
    assert abs(Pl['V1'] + 3000) < 1e-6 and abs(Pl['E1'] + 800) < 1e-6 and abs(Pl['V2'] - 200) < 1e-6
    assert abs(Pl['RO'] - 1200) < 1e-6 and 4 * (I1 - I2) == 40 and I1 - I2 == 10
    assert round(1200 / 3800 * 100, 1) == 31.6
