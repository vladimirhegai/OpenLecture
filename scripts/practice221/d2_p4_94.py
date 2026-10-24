r"""Textbook P4.94: superposition for i_o. 6 A alone (mesh), 10 A alone (supermesh), 75 V alone (one-node nodal)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'D'
TITLE = 'Superposition with three sources'
SOURCE = 'Textbook P4.94'
CITES = [{"chunk_id": "08f8634b-5721-46a7-80a8-660010b60390", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1}]
PROMPT = 'Use superposition to find $i_o$.'

O = r'\,\Omega'
A = r'\,\mathrm{A}'
V = r'\,\mathrm{V}'
I1 = f'I1 0,0 -> 0,4 "$6{A}$"'
R1 = f'R1 2,4 -> 2,0 "$20{O}$"'
R2 = f'R2 2,4 -> 4.5,4 "$1{O}$" i="$i_o$"'
I2 = f'I2 4.5,4 -> 4.5,0 "$10{A}$"'
R3 = f'R3 6.5,4 -> 6.5,0 "$60{O}$"'
R4 = f'R4 8.5,4 -> 8.5,2 "$5{O}$"'
V1 = f'V1 8.5,2 -> 8.5,0 "$75{V}$"'
R5 = f'R5 10.5,4 -> 10.5,0 "$30{O}$"'
TOP = 'wire 4.5,4 -> 10.5,4'
BOTTOM = 'wire 0,0 -> 10.5,0'
LEFT = 'wire 0,4 -> 2,4'
# p is labelled on the left wire (same node) so it clears the i_o arrow; that wire stays when the 6 A is off (open stub)
LABELS = '\n'.join(['label 1.1,4 "$p$" above', 'label 4.5,4 "$q$" above', 'label 8.5,2 "$k$" right', 'ground 0,0'])


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(I1, LEFT, R1, R2, I2, TOP, R3, R4, V1, R5, BOTTOM, LABELS)

# 6 A alone: 10 A open, 75 V a wire
ALONE6 = j(I1, LEFT, R1, R2, TOP, R3, R4, 'wire 8.5,2 -> 8.5,0', R5, BOTTOM, LABELS)
# right side 60 || 5 || 30 = 4 ohm, drawn where the 60 ohm was
REQ = f'REQ 7.5,4 -> 7.5,0 "$4{O}$"'
SMALL = j('wire 4.5,4 -> 7.5,4', 'wire 0,0 -> 7.5,0', 'label 1.1,4 "$p$" above', 'label 4.5,4 "$q$" above', 'ground 0,0')
EQ6 = j(I1, LEFT, R1, R2, REQ, SMALL)
ALONE10 = j(LEFT, R1, R2, I2, TOP, R3, R4, 'wire 8.5,2 -> 8.5,0', R5, BOTTOM, LABELS)
EQ10 = j(LEFT, R1, R2, I2, REQ, SMALL)
R2u = f'R2 2,4 -> 4.5,4 "$1{O}$"'
ALONE75 = j(LEFT, R1, R2, TOP, R3, R4, V1, R5, BOTTOM, LABELS)
NODAL75 = j(LEFT, R1, R2u, TOP, 'dot 4.5,4', f'R3 6.5,4 -> 6.5,0 "$60{O}$" i="$i_3$"', f'R4 8.5,4 -> 8.5,2 "$5{O}$" i="$i_4$"',
            V1, f'R5 10.5,4 -> 10.5,0 "$30{O}$" i="$i_5$"', BOTTOM, LABELS,
            '#= path 4.2,3.6 -> 2.35,3.6 -> 2.35,0.4 thin color=orange', '#= text 3.3,2.2 "$i_{21}$" color=orange')

P1 = r'#+ $i_o{}^{\prime}=4.8\,\mathrm{A}$'
P2 = r"#+ $i_o{}^{\prime\prime}=1.6\,\mathrm{A}$"
P3 = r"#+ $i_o{}^{\prime\prime\prime}=-2.4\,\mathrm{A}$"

STEPS = [
    ('The circuit', GIVEN, r'''
Three independent sources → three small problems, then add.

**Turning a source off**
- voltage source → **wire**
- current source → **open** (it disappears)
'''),
    ('$6\\,\\mathrm{A}$ alone', ALONE6, r'''
$10\,\mathrm{A}$ off → open. $75\,\mathrm{V}$ off → wire.

Now the $60\,\Omega$, $5\,\Omega$ and $30\,\Omega$ all run from $q$ to ground → **parallel**:

$$
\frac{1}{60}+\frac{1}{5}+\frac{1}{30}=\frac{1+12+2}{60}=\frac{1}{4}
$$

So they act like one $4\,\Omega$.
'''),
    ('$6\\,\\mathrm{A}$ alone: mesh', j(EQ6, '#= mesh 1,1.1 "$I_1$" cw r=0.45', '#= mesh 4.6,2 "$I_2$" cw r=0.8',
                                         '#= sign 2.35,1.2 +', '#= sign 2.35,2.8 -', '#= sign 2.5,3.62 +', '#= sign 4.0,3.62 -',
                                         '#= sign 7.15,2.8 +', '#= sign 7.15,1.2 -', P1), r'''
Mesh 1 holds the $6\,\mathrm{A}$ source (same direction): $I_1=6\,\mathrm{A}$.

Mesh 2 (signs you enter by; the $20\,\Omega$ carries $I_2-I_1$):

$$
20(I_2-6)+1I_2+4I_2=0
$$

$$
25I_2=120 \;\Rightarrow\; I_2=4.8\,\mathrm{A}
$$

$i_o$ is mesh 2's top current: $i_o{}^{\prime}=4.8\,\mathrm{A}$.
'''),
    ('$10\\,\\mathrm{A}$ alone', ALONE10, r'''
$6\,\mathrm{A}$ off → open. $75\,\mathrm{V}$ off → wire.

Same $60\parallel5\parallel30=4\,\Omega$ on the right.
'''),
    ('$10\\,\\mathrm{A}$ alone: supermesh', j(EQ10, '#= mesh 3.0,1.6 "$I_A$" cw r=0.5', '#= mesh 5.85,1.5 "$I_B$" cw r=0.45',
                                               '#= region 1.55,-0.8 7.95,4.45 "supermesh"',
                                               '#= sign 2.35,1.2 +', '#= sign 2.35,2.8 -', '#= sign 2.5,3.62 +', '#= sign 4.0,3.62 -',
                                               '#= sign 7.15,2.8 +', '#= sign 7.15,1.2 -', P2), r'''
The $10\,\mathrm{A}$ source is shared by meshes $A$ and $B$ → **supermesh** (walk around the outside).

Source constraint (down the source: $I_A$ down, $I_B$ up):

$$
I_A-I_B=10
$$

KVL around the outside:

$$
20I_A+1I_A+4I_B=0
$$

Substitute $I_B=I_A-10$:

$$
25I_A=40 \;\Rightarrow\; I_A=1.6\,\mathrm{A}
$$

$i_o{}^{\prime\prime}=I_A=1.6\,\mathrm{A}$.
'''),
    ('$75\\,\\mathrm{V}$ alone', ALONE75, r'''
Both current sources off → open.

$20\,\Omega$ and $1\,\Omega$ are now in **series** from $q$ to ground ($21\,\Omega$), and $i_o$ flows through them.

Only one unknown node, $q$ → **nodal** is quickest.
'''),
    ('$75\\,\\mathrm{V}$ alone: nodal at $q$', j(NODAL75, P3), r'''
Currents leaving $q$ toward ground ((start − end)/R; $V_k=75\,\mathrm{V}$):

$$
-\frac{V_q-0}{21}-\frac{V_q-0}{60}-\frac{V_q-75}{5}-\frac{V_q-0}{30}=0
$$

Multiply by $-420$:

$$
20V_q+7V_q+84(V_q-75)+14V_q=0 \;\Rightarrow\; 125V_q=6300
$$

$$
V_q=50.4\,\mathrm{V} \qquad i_{21}=\frac{50.4}{21}=2.4\,\mathrm{A}\ (q\to p)
$$

$i_o$ points $p\to q$, so $i_o{}^{\prime\prime\prime}=-2.4\,\mathrm{A}$.
'''),
    ('Add the three', j(GIVEN, f'#+ $i_o=4{A}$'), r'''
$$
i_o=i_o{}^{\prime}+i_o{}^{\prime\prime}+i_o{}^{\prime\prime\prime}=4.8+1.6-2.4
$$

$$
\boxed{i_o=4\,\mathrm{A}}
$$

Add currents and voltages only, **never powers**.
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    p, q = els['R2']
    g = els['R1'][1]
    assert els['I1'] == (g, p) and els['R1'] == (p, g) and els['I2'] == (q, g), els
    assert els['R3'] == (q, g) and els['R5'] == (q, g) and els['R4'][0] == q and els['V1'][1] == g, els
    k = els['R4'][1]
    assert els['V1'][0] == k
    base = [('R', 'R1', 'p', '0', 20), ('R', 'R2', 'p', 'q', 1), ('R', 'R3', 'q', '0', 60), ('R', 'R4', 'q', 'k', 5),
            ('R', 'R5', 'q', '0', 30)]
    src = {'I1': ('I', 'I1', '0', 'p', 6), 'I2': ('I', 'I2', 'q', '0', 10), 'V1': ('V', 'V1', 'k', '0', 75)}
    off = {'V1': ('V', 'V1', 'k', '0', 0)}

    def io(on):
        net = base + [src[s] for s in on] + ([] if 'V1' in on else [off['V1']])
        return solve(net)[1]['R2']
    assert abs(io(['I1', 'I2', 'V1']) - 4) < 1e-9
    assert abs(io(['I1']) - 4.8) < 1e-9 and abs(io(['I2']) - 1.6) < 1e-9 and abs(io(['V1']) + 2.4) < 1e-9
    assert abs(1 / (1 / 60 + 1 / 5 + 1 / 30) - 4) < 1e-12
    assert 20 * (4.8 - 6) + 4.8 + 4 * 4.8 < 1e-9 and 25 * 4.8 == 120
    IA = 40 / 25
    assert IA == 1.6 and abs(21 * IA + 4 * (IA - 10)) < 1e-9
    Vq = 6300 / 125
    assert Vq == 50.4 and abs(-Vq / 21 - Vq / 60 - (Vq - 75) / 5 - Vq / 30) < 1e-9
    assert 20 + 7 + 84 + 14 == 125 and 84 * 75 == 6300 and abs(Vq / 21 - 2.4) < 1e-12
