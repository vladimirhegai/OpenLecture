r"""Assessment AP4.19 (Textbook P4.75, P4.83): Thévenin by nodal at a, R_Th by a test source, Norton, matched load,
then the efficiency back in the original circuit. One unknown node (a), so nodal is the natural method."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'D'
TITLE = 'Matched load and efficiency'
SOURCE = 'Assessment Problem 4.19 (Textbook P4.75, P4.83)'
CITES = [{"chunk_id": "e9afc18b-d6ad-428f-a81c-685ede4bcf36", "source_id": "3b287f2d-b408-41eb-a523-b299688ff303", "version": 1},
         {"chunk_id": "779ae69c-1fee-4836-824c-5ceac9749991", "source_id": "3b287f2d-b408-41eb-a523-b299688ff303", "version": 1},
         {"chunk_id": "0da028c8-138a-47c7-8ee5-99ac30e9dc71", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1},
         {"chunk_id": "11bd02ab-ca60-4fbc-9f85-243a3e08a576", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1}]
PROMPT = (r'Find **(a)** $V_{\mathrm{Th}}$; **(b)** $R_{\mathrm{Th}}$ using a test source; **(c)** the Norton equivalent; '
          r'**(d)** the adjustable load $R_o$ for maximum power, and that power; **(e)** the percentage of the total '
          r'developed power delivered to that load.')

O = r'\,\Omega'
V = r'\,\mathrm{V}'
A = r'\,\mathrm{A}'
W = r'\,\mathrm{W}'
V1 = f'V1 0,3 -> 0,0 "$24{V}$"'
R1 = f'R1 0,3 -> 3,3 "$2{O}$"'
R1i = f'R1 0,3 -> 3,3 "$2{O}$" i_rev="$i_1$"'
G1 = '\n'.join(['wire 0,3 -> 0,5', 'G1 3,5 -> 0,5 "$3i_x$"', 'wire 3,5 -> 3,3'])
I1 = f'I1 5,3 -> 5,0 "$4{A}$"'
R2 = f'R2 7,3 -> 7,0 "$8{O}$" i="$i_x$"'
WIRES = '\n'.join(['wire 3,3 -> 5,3', 'wire 5,3 -> 7,3', 'wire 7,3 -> 9,3', 'wire 0,0 -> 9,0'])
TERMS = '\n'.join(['terminal 9,3 "$a$" right', 'terminal 9,0 "$b$" right', 'ground 0,0'])
DOT_A = 'dot 3,3'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(V1, R1, G1, 'wire 3,3 -> 5,3', I1, 'wire 5,3 -> 7,3', R2, 'wire 7,3 -> 9,3', TERMS, 'wire 0,0 -> 9,0')
OPEN = j(V1, R1i, G1, I1, R2, WIRES, TERMS, DOT_A)
OFF = j('wire 0,3 -> 0,0', R1i, G1, R2, WIRES, TERMS, DOT_A)
TEST = j(OFF, 'VT 9,3 -> 9,0 "$v_T$" i_rev="$i_T$"')
SHORTED = j(V1, R1i, G1, I1, R2, WIRES, TERMS, DOT_A, 'wire 9,3 -> 9,0')
VTH = f'#+ $V_{{Th}}=8{V}$'
RTH = f'#+ $R_{{Th}}=1{O}$'
IN = f'#+ $I_N=8{A}$'
PMAX = f'#+ $P_{{max}}=16{W}$'
LOADED = j(V1, R1i, G1, I1, R2, WIRES, 'terminal 9,3 "$a$" right', 'terminal 9,0 "$b$" right', 'ground 0,0', DOT_A,
           f'RO 9,3 -> 9,0 "$R_o=1{O}$" flip')

STEPS = [
    ('The circuit', GIVEN, r'''
Only one unknown node ($a$; the top of the $24\,\mathrm{V}$ is fixed at $24\,\mathrm{V}$) → **nodal** at $a$.

**Plan**
1. $V_{Th}$: $a$–$b$ open, KCL at $a$.
2. $R_{Th}$: sources off, push a test voltage $v_T$.
3. Norton: short $a$–$b$.
4. Max power: $R_o=R_{Th}$.
5. Efficiency: put $R_o$ on the original circuit.
'''),
    ('(a) $V_{Th}$: KCL at $a$', j(OPEN, VTH), r'''
Currents **leaving** $a$ (each is (start − end)/R):
- $i_1=\dfrac{V_a-24}{2}$ (toward the $24\,\mathrm{V}$ node)
- $3i_x$ (source arrow points away from $a$)
- $4\,\mathrm{A}$
- $i_x=\dfrac{V_a-0}{8}$

KCL (leaving $-$):

$$
-\frac{V_a-24}{2}-3\frac{V_a}{8}-4-\frac{V_a}{8}=0
$$

Multiply by $-8$:

$$
4(V_a-24)+3V_a+32+V_a=0 \;\Rightarrow\; 8V_a=64
$$

$$
\boxed{V_{Th}=V_a=8\,\mathrm{V}}
$$
'''),
    ('(b) Sources off', OFF, r'''
Independent sources off:
- $24\,\mathrm{V}$ → **wire**
- $4\,\mathrm{A}$ → **open**

The dependent $3i_x$ **stays** (it is controlled by $i_x$, which is still in the circuit).
'''),
    ('(b) Test source $v_T$', j(TEST, RTH), r'''
Push $v_T$ into $a$; it sends $i_T$ in. Now $V_a=v_T$ and the left end of the $2\,\Omega$ is $0\,\mathrm{V}$.

KCL at $a$ (entering $+$, leaving $-$):

$$
i_T-\frac{v_T}{2}-3\frac{v_T}{8}-\frac{v_T}{8}=0
$$

$$
i_T=\frac{4v_T+3v_T+v_T}{8}=v_T
$$

$$
\boxed{R_{Th}=\frac{v_T}{i_T}=1\,\Omega}
$$
'''),
    ('(c) Norton: short $a$–$b$', j(SHORTED, '#= path 7.8,3 -> 9,3 -> 9,0.6 "$8\\,\\mathrm{A}$"', IN), r'''
Short → $V_a=0$ → $i_x=0$ → $3i_x=0$.

Ohm's law on the $2\,\Omega$ ($24\,\mathrm{V}$ → $0\,\mathrm{V}$):

$$
\frac{24-0}{2}=12\,\mathrm{A}\ \text{into } a
$$

$4\,\mathrm{A}$ leaves through the source; the rest goes down the short:

$$
\boxed{I_N=12-4=8\,\mathrm{A}}
$$

Check: $I_N=V_{Th}/R_{Th}=8/1=8\,\mathrm{A}$ ✓
'''),
    ('(c) Norton equivalent', j(f'IN 5,0 -> 5,3 "$8{A}$"', f'RN 7,3 -> 7,0 "$1{O}$"', 'wire 5,3 -> 9,3', 'wire 5,0 -> 9,0',
                                'terminal 9,3 "$a$" right', 'terminal 9,0 "$b$" right'), r'''
$$
I_N=8\,\mathrm{A}\ (\text{from } b \text{ up to } a)\;\parallel\;R_N=1\,\Omega
$$
'''),
    ('(d) Matched load', j(f'VTH 0,3 -> 0,0 "$8{V}$"', f'RTH 0,3 -> 3,3 "$1{O}$"', 'wire 3,3 -> 9,3', 'wire 0,0 -> 9,0',
                           'terminal 9,3 "$a$" right', 'terminal 9,0 "$b$" right', f'RO 9,3 -> 9,0 "$R_o=1{O}$" flip',
                           '#= mesh 4.5,1.5 "$I$" cw r=0.8', '#= sign 0.6,2.62 +', '#= sign 2.4,2.62 -',
                           '#= sign 8.65,2.3 +', '#= sign 8.65,0.7 -',
                           f'#+ $R_o=1{O}$', PMAX), r'''
Max power: $R_o=R_{Th}=1\,\Omega$.

Mesh on the Thévenin circuit:

$$
-8+1I+1I=0 \;\Rightarrow\; I=4\,\mathrm{A}
$$

$$
\boxed{P_{max}=I^2R_o=(4)^2(1)=16\,\mathrm{W}}
$$

$V_a=IR_o=4\,\mathrm{V}$ (half of $V_{Th}$).
'''),
    ('(e) Load on the original circuit', j(LOADED, '#= text 3.9,3.55 "$4\\,\\mathrm{V}$" color=pink',
                                           f'#+ $i_{{24}}=8.5{A}$'), r'''
$V_a=4\,\mathrm{V}$ (from (d)). Ohm's law:

$$
i_x=\frac{4}{8}=0.5\,\mathrm{A} \qquad 3i_x=1.5\,\mathrm{A}
$$

$$
i_1=\frac{24-4}{2}=10\,\mathrm{A}\ \text{(into } a)
$$

KCL at the $24\,\mathrm{V}$ node: $1.5\,\mathrm{A}$ arrives from $3i_x$, $10\,\mathrm{A}$ leaves through the $2\,\Omega$:

$$
i_{24}=10-1.5=8.5\,\mathrm{A}\ \text{(out of the + end)}
$$
'''),
    ('(e) Efficiency', j(LOADED, '#= text 3.9,3.55 "$4\\,\\mathrm{V}$" color=pink',
                         '#= text 4.0,5 "$30\\,\\mathrm{W}$" color=green', '#= text -1.0,2.55 "$204\\,\\mathrm{W}$" color=green',
                         r'#+ $\eta=6.84\,\%$'), r'''
Developed (current climbs from $-$ to $+$):
- $24\,\mathrm{V}$: $(24)(8.5)=204\,\mathrm{W}$
- $3i_x$: $1.5\,\mathrm{A}$ pushed from $4\,\mathrm{V}$ up to $24\,\mathrm{V}$: $(1.5)(20)=30\,\mathrm{W}$

The $4\,\mathrm{A}$ source **absorbs** $(4)(4)=16\,\mathrm{W}$.

$$
\eta=\frac{16}{204+30}\cdot100=\boxed{6.84\,\%}
$$

Check: $200+2+16+16=234\,\mathrm{W}$ absorbed ✓
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    top, gnd = els['V1']
    a = els['R1'][1]
    assert els['R1'][0] == top and els['G1'] == (a, top), els      # 3ix pushes from a into the 24 V node
    assert els['I1'] == (a, gnd) and els['R2'] == (a, gnd), els
    for d in (OPEN, OFF, TEST, SHORTED, LOADED):
        check(d)
    # i_x = current down the 8 ohm = Va/8; G: current a -> top = 3*Va/8
    net = [('V', 'V1', 't', '0', 24), ('R', 'R1', 't', 'a', 2), ('G', 'G1', 'a', 't', {'a': 3 / 8}),
           ('I', 'I1', 'a', '0', 4), ('R', 'R2', 'a', '0', 8)]
    Vn, I, P = solve(net)
    assert abs(Vn['a'] - 8) < 1e-9
    assert 4 * (8 - 24) + 3 * 8 + 32 + 8 == 0
    Vt, It, _ = solve([('V', 'VT', 'a', '0', 1), ('R', 'R1', 't', 'a', 2), ('V', 'V1', 't', '0', 0),
                       ('G', 'G1', 'a', 't', {'a': 3 / 8}), ('R', 'R2', 'a', '0', 8)])
    assert abs(-It['VT'] - 1) < 1e-9                                 # i_T = 1 A for v_T = 1 V -> 1 ohm
    _, Is, _ = solve(net + [('V', 'S', 'a', '0', 0)])
    assert abs(Is['S'] - 8) < 1e-9 and 24 / 2 - 4 == 8
    assert 8 / 2 == 4 and 4 ** 2 * 1 == 16
    Vl, Il, Pl = solve(net + [('R', 'RO', 'a', '0', 1)])
    assert abs(Vl['a'] - 4) < 1e-9 and abs(Il['R1'] - 10) < 1e-9     # 10 A flows t -> a
    assert abs(Il['V1'] + 8.5) < 1e-9                                 # 8.5 A out of the + end
    dev = -Pl['V1'] - Pl['G1']
    assert abs(-Pl['V1'] - 204) < 1e-9 and abs(-Pl['G1'] - 30) < 1e-9 and abs(Pl['I1'] - 16) < 1e-9
    assert abs(dev - 234) < 1e-9 and round(16 / 234 * 100, 2) == 6.84
    assert abs(Pl['R1'] - 200) < 1e-9 and abs(Pl['R2'] - 2) < 1e-9 and abs(Pl['RO'] - 16) < 1e-9
