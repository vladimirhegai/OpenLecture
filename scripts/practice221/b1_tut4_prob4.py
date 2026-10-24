r"""Tutorial 4, Problem 4: a bridge fed by a 1 A source, solved by nodal analysis (the user's convention:
currents toward ground / high -> low, current = (start - end)/R, KCL leaving -, entering +)."""
from fractions import Fraction as F

SECTION = 'B'
TITLE = 'A bridge fed by a current source'
SOURCE = 'Tutorial 4, Problem 4'
CITES = [
    {"chunk_id": "087e8718-a332-4caf-b01e-160758731932", "source_id": "6aad60b9-910d-4700-985f-68a4fa9278b3", "version": 1},
    {"chunk_id": "1746e892-6453-4f04-b7da-73b907b47031", "source_id": "6aad60b9-910d-4700-985f-68a4fa9278b3", "version": 1},
    {"chunk_id": "19d01aed-f19b-4677-ae23-19f2f7e3fe25", "source_id": "6aad60b9-910d-4700-985f-68a4fa9278b3", "version": 1},
]
PROMPT = 'Find $i_o$, $i_1$, $i_2$ and the power delivered by the current source.'

O = r'\,\Omega'


def j(*parts):
    return '\n'.join(parts)


I1 = r'I1 0,0 -> 0,3 "$1\,\mathrm{A}$"'
R3 = f'R3 6,3 -> 6,0 "$100{O}$" i="$i_2$"'
R5 = f'R5 9,3 -> 9,0 "$600{O}$" i="$i_o$"'
R6 = f'R6 3,5 -> 9,5 "$320{O}$" i="$i_1$"'
REST = j('wire 0,3 -> 3,3', 'wire 3,3 -> 3,5', 'wire 9,5 -> 9,3', 'wire 9,0 -> 0,0',
         'label 3,5 "$a$" left', 'label 6,3 "$b$" above', 'label 9,3 "$c$" right', 'ground 0,0')
GIVEN = j(I1, f'R1 3,3 -> 3,0 "$240{O}$"', f'R2 3,3 -> 6,3 "$20{O}$"', R3, f'R4 6,3 -> 9,3 "$50{O}$"', R5, R6, REST)
# every resistor current drawn toward ground / from the high node to the low node
ARROWS = j(I1, f'R1 3,3 -> 3,0 "$240{O}$" i', f'R2 3,3 -> 6,3 "$20{O}$" i', R3, f'R4 6,3 -> 9,3 "$50{O}$" i', R5, R6, REST)

NODE_A = '#= region -0.4,2.6 3.4,5.4 color=green'
NODE_B = '#= region 5.55,2.55 6.45,3.45 color=green'
NODE_C = '#= region 8.55,2.6 9.45,5.4 color=green'
VA = r'#= text 1.6,4.3 "$72.96\,\mathrm{V}$" color=green'
VB = r'#= text 6,4.15 "$60\,\mathrm{V}$" color=green'
VC = r'#= text 10.4,4.15 "$57.6\,\mathrm{V}$" color=green'
VALS = j(VA, VB, VC)

STEPS = [
    ('The circuit', GIVEN, r'''
**Method: nodal.** Only 3 unknown nodes ($a$, $b$, $c$), and the current source just feeds $1\,\mathrm{A}$ into $a$.

- Nodes $a$, $b$, $c$ → $V_a$, $V_b$, $V_c$.
- Bottom wire = ground = $0\,\mathrm{V}$.
'''),
    ('Currents: toward ground, high → low', ARROWS, r'''
Every resistor current points down to ground, or from the higher node to the lower one ($a$ is fed by the source, so $a \to b \to c$).

Current $=$ (start − end) $/R$.

KCL: leaving $-$, entering $+$.
'''),
    ('KCL at $a$', j(ARROWS, NODE_A), r'''
$1\,\mathrm{A}$ enters; three currents leave.

$$
+1-\frac{V_a-0}{240}-\frac{V_a-V_b}{20}-\frac{V_a-V_c}{320}=0
$$

Multiply by $-960$:

$$
55V_a-48V_b-3V_c=960
$$
'''),
    ('KCL at $b$', j(ARROWS, NODE_B), r'''
$$
+\frac{V_a-V_b}{20}-\frac{V_b-0}{100}-\frac{V_b-V_c}{50}=0
$$

Multiply by $100$:

$$
5V_a-8V_b+2V_c=0
$$
'''),
    ('KCL at $c$', j(ARROWS, NODE_C), r'''
$$
+\frac{V_b-V_c}{50}+\frac{V_a-V_c}{320}-\frac{V_c-0}{600}=0
$$

Multiply by $4800$:

$$
15V_a+96V_b-119V_c=0
$$
'''),
    ('Solve the node voltages', j(ARROWS, VALS, r'#+ $V_a=72.96\,\mathrm{V}$', r'#+ $V_b=60\,\mathrm{V}$',
                                  r'#+ $V_c=57.6\,\mathrm{V}$'), r'''
From $b$:

$$
V_b=\tfrac58V_a+\tfrac14V_c
$$

Into $c$: $75V_a-95V_c=0$, so

$$
V_c=\tfrac{15}{19}V_a \qquad V_b=\tfrac{125}{152}V_a
$$

Into $a$:

$$
\tfrac{250}{19}V_a=960 \;\Rightarrow\; V_a=72.96\,\mathrm{V}
$$

$$
V_b=60\,\mathrm{V} \qquad V_c=57.6\,\mathrm{V}
$$
'''),
    ("Ohm's law → $i_o$, $i_1$, $i_2$", j(ARROWS, VALS,
                                          r'#= text 10.25,1.5 "$0.096\,\mathrm{A}$" color=orange',
                                          r'#= text 6.75,0.7 "$0.6\,\mathrm{A}$" color=orange',
                                          r'#= text 6,5.95 "$0.048\,\mathrm{A}$" color=orange',
                                          r'#+ $i_o=0.096\,\mathrm{A}$', r'#+ $i_1=0.048\,\mathrm{A}$',
                                          r'#+ $i_2=0.6\,\mathrm{A}$'), r'''
$$
i_o=\frac{V_c-0}{600}=\frac{57.6}{600}=0.096\,\mathrm{A}
$$

$$
i_1=\frac{V_a-V_c}{320}=\frac{15.36}{320}=0.048\,\mathrm{A}
$$

$$
i_2=\frac{V_b-0}{100}=\frac{60}{100}=0.6\,\mathrm{A}
$$
'''),
    ('Power of the source', j(ARROWS, VALS, r'#= text -1.4,0.6 "$72.96\,\mathrm{W}$" color=orange',
                              r'#+ $p=72.96\,\mathrm{W}$'), r'''
The source pushes $1\,\mathrm{A}$ up from ground ($0\,\mathrm{V}$) into $a$ ($72.96\,\mathrm{V}$): it lifts the current, so it **delivers**.

$$
p=V_a\cdot 1=72.96\cdot 1
$$

$$
\boxed{p=72.96\,\mathrm{W}\text{ delivered}}
$$
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    a, b, c = els['R2'][0], els['R3'][0], els['R5'][0]
    assert els['I1'] == ('0', a) and els['R1'] == (a, '0') and els['R2'] == (a, b), els
    assert els['R4'] == (b, c) and els['R6'] == (a, c) and els['R3'][1] == els['R5'][1] == '0', els
    assert check(ARROWS)[0] == els
    # KCL equations (scaled) and the substitutions
    Va = F(960 * 19, 250)
    assert Va == F('72.96')
    Vc = F(15, 19) * Va
    Vb = F(5, 8) * Va + F(1, 4) * Vc
    assert Vb == F(125, 152) * Va == 60 and Vc == F('57.6')
    assert 1 - Va / 240 - (Va - Vb) / 20 - (Va - Vc) / 320 == 0
    assert 55 * Va - 48 * Vb - 3 * Vc == 960
    assert (Va - Vb) / 20 - Vb / 100 - (Vb - Vc) / 50 == 0 and 5 * Va - 8 * Vb + 2 * Vc == 0
    assert (Vb - Vc) / 50 + (Va - Vc) / 320 - Vc / 600 == 0 and 15 * Va + 96 * Vb - 119 * Vc == 0
    assert 15 * 5 == 75 and 96 * F(1, 4) - 119 == -95 and 55 - 48 * F(125, 152) - 3 * F(15, 19) == F(250, 19)
    assert Vc / 600 == F('0.096') and Va - Vc == F('15.36') and (Va - Vc) / 320 == F('0.048') and Vb / 100 == F('0.6')
    assert Va * 1 == F('72.96')
    # high -> low ordering used for the arrows
    assert Va > Vb > Vc > 0
