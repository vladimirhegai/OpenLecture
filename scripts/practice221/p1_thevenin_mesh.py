r"""Problem 1: find V_o with Thévenin, solved by mesh analysis + Ohm's law.

Sign rule (the user's): walk the mesh in the arrow's direction and write the sign of the terminal
you ENTER each element by. The same rule gives V_oc: walk from the + terminal to the - terminal.
"""

SECTION = 'C'
TITLE = 'Thévenin'
SOURCE = 'Practice problem (from your list)'
PROMPT = "Find $V_o$ using Thévenin's theorem."

K = r'\,\mathrm{k\Omega}'
V = r'\,\mathrm{V}'
R1 = f'R1 0,3 -> 0,0 "$2{K}$"'
R2 = f'R2 3,3 -> 3,0 "$4{K}$"'
RL = f'R3 6,3 -> 6,0 "$2{K}$"'
V1 = f'V1 0,3 -> 3,3 "$6{V}$"'   # + on the left
V2 = f'V2 6,3 -> 3,3 "$12{V}$"'  # + on the right
FRAME = '\n'.join(['wire 6,3 -> 8,3', 'wire 0,0 -> 8,0', 'terminal 8,3', 'terminal 8,0'])
VO = 'gap 8,3 -> 8,0 v="$V_o$"'
VOC = 'gap 8,3 -> 8,0 v="$V_{oc}$"'

MESH = '#= mesh 1.5,1.5 "$I_1$" ccw r=0.75'
MESH_SOLVED = '#= mesh 1.5,1.5 "$I_1$" ccw r=0.75'
SIGNS_2K = '#= sign 0.35,2.3 +\n#= sign 0.35,0.7 -'
SIGNS_4K = '#= sign 2.65,0.7 +\n#= sign 2.65,2.3 -'
WALK = '#= path 7.75,3 -> 0,3 -> 0,0 -> 7.7,0'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(R1, V1, R2, V2, RL, FRAME, VO)
OPEN = j(R1, V1, R2, V2, FRAME, VOC)

TH_LOOP = j(f'VTH 0,3 -> 0,0 "$8{V}$"', r'RTH 0,3 -> 3,3 "$\tfrac{4}{3}\,\mathrm{k\Omega}$"', 'wire 3,3 -> 6,3', RL, FRAME, VO)

STEPS = [
    ('The circuit', GIVEN, r'''
Find $V_o$: the voltage across the right $2\,\mathrm{k\Omega}$.

That $2\,\mathrm{k\Omega}$ sits right across the output → it's the **load** $R_L$.

**Plan**
1. Pull out $R_L$.
2. $V_{Th}=V_{oc}$ with mesh + Ohm's law.
3. $R_{Th}$: sources off.
4. Put $R_L$ back on the Thévenin circuit.
'''),
    ('Pull out the load', OPEN, r'''
$R_L$ is gone → the terminals are **open**.

The voltage across them is $V_{oc}=V_{Th}$.

Open terminals → **no current** in the $12\,\mathrm{V}$ branch.
'''),
    ('Mesh current', j(OPEN, MESH), r'''
Only one closed loop is left: $2\,\mathrm{k\Omega}$ → $6\,\mathrm{V}$ → $4\,\mathrm{k\Omega}$.

Give it a mesh current $I_1$ (counter-clockwise here; either way works).
'''),
    ('Signs + KVL', j(OPEN, MESH, SIGNS_2K, SIGNS_4K, r'#+ $I_1=1\,\mathrm{mA}$'), r'''
Mark $+$ where $I_1$ **enters** each resistor.

Walk the loop with $I_1$; write the sign you **enter** each element by:
- $4\,\mathrm{k\Omega}$: enter $+$ → $+4kI_1$
- $6\,\mathrm{V}$: enter $-$ → $-6$
- $2\,\mathrm{k\Omega}$: enter $+$ → $+2kI_1$

$$
4kI_1-6+2kI_1=0
$$

$$
6kI_1=6 \;\Rightarrow\; I_1=\frac{6}{6k}=1\,\mathrm{mA}
$$
'''),
    ("Ohm's law on the $2\\,\\mathrm{k\\Omega}$", j(OPEN, MESH, SIGNS_2K, '#= text 1.1,1.5 "$2\\,\\mathrm{V}$" color=pink', r'#+ $V_{2k}=2\,\mathrm{V}$'), r'''
$$
V_{2k}=I_1\cdot 2k=(1m)(2k)=2\,\mathrm{V}
$$

$m\cdot k=1$, so the prefixes cancel.

$+$ is on top (where $I_1$ enters).
'''),
    ('KVL walk to $V_{oc}$', j(OPEN, SIGNS_2K, '#= text 1.1,1.5 "$2\\,\\mathrm{V}$" color=pink', WALK, r'#+ $V_{Th}=8\,\mathrm{V}$'), r'''
Walk from the $+$ terminal to the $-$ terminal. Same rule: the sign you **enter** each element by.
- $12\,\mathrm{V}$: enter $+$ → $+12$
- $6\,\mathrm{V}$: enter $-$ → $-6$
- $2\,\mathrm{k\Omega}$: enter $+$ → $+2$

$$
V_{oc}=12-6+2=8\,\mathrm{V}
$$

$$
\boxed{V_{Th}=8\,\mathrm{V}}
$$
'''),
    ('$R_{Th}$: sources off', j(R1, 'wire 0,3 -> 3,3', R2, 'wire 3,3 -> 6,3', FRAME,
                                 '#= path 9.6,1.5 -> 8.25,1.5 thin color=accent',
                                 '#= text 9.1,1.95 "$R_{Th}$" color=accent', r'#+ $R_{Th}=\tfrac43\,\mathrm{k\Omega}$'), r'''
Voltage source off = **short** (a wire).

Looking in from the terminals: $2\,\mathrm{k\Omega}$ and $4\,\mathrm{k\Omega}$ both span the top wire to the bottom wire → **parallel**.

$$
R_{Th}=\frac{(2k)(4k)}{2k+4k}=\frac{8k^2}{6k}=\tfrac{4}{3}\,\mathrm{k\Omega}
$$
'''),
    ('Thévenin circuit + load back', TH_LOOP, r'''
$V_{Th}=8\,\mathrm{V}$ in series with $R_{Th}=\tfrac43\,\mathrm{k\Omega}$.

$R_L=2\,\mathrm{k\Omega}$ is back. One loop again → mesh.
'''),
    ('Mesh + Ohm → $V_o$', j(TH_LOOP, '#= mesh 3,1.5 "$I$" cw r=0.8',
                              '#= sign 0.65,2.62 +', '#= sign 2.35,2.62 -', '#= sign 5.65,2.3 +', '#= sign 5.65,0.7 -',
                              r'#+ $I=2.4\,\mathrm{mA}$', r'#+ $V_o=4.8\,\mathrm{V}$'), r'''
KVL with $I$ (signs you enter by):

$$
-8+\tfrac43kI+2kI=0
$$

$$
\tfrac{10}{3}kI=8 \;\Rightarrow\; I=\frac{8}{\tfrac{10}{3}k}=2.4\,\mathrm{mA}
$$

Ohm's law on $R_L$:

$$
V_o=I\cdot 2k=(2.4m)(2k)
$$

$$
\boxed{V_o=4.8\,\mathrm{V}}
$$
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    assert els['V1'][1] == els['R2'][0] == els['V2'][1], els      # 6 V and 12 V meet at the top of the 4k
    assert els['V1'][0] == els['R1'][0] and els['V2'][0] == els['R3'][0], els
    assert els['R1'][1] == els['R2'][1] == els['R3'][1], els     # one bottom wire
    for _name, drawing, _notes in STEPS:
        check('\n'.join(l for l in drawing.splitlines() if not l.startswith('#=')))
    # Arithmetic: CCW mesh, then the walk, R_Th, divider; cross-check with node voltages (bottom = 0).
    I1 = 6 / 6                      # mA
    assert I1 * 2 == 2
    Voc = 12 - 6 + I1 * 2
    assert Voc == 8
    Va = I1 * 2; Vb = Va - 6; Vc = Vb + 12   # nodal: -Va/2k - Vb/4k = 0 must hold
    assert Vc == Voc and abs(-Va / 2 - Vb / 4) < 1e-12
    Rth = 2 * 4 / 6
    I = 8 / (Rth + 2)
    assert abs(I - 2.4) < 1e-12 and abs(I * 2 - 4.8) < 1e-12
    Va_full = -6 / 5                # full circuit, load in: -Va/2 - (Va-6)/4 - (Va+6)/2 = 0
    assert abs(-Va_full / 2 - (Va_full - 6) / 4 - (Va_full + 6) / 2) < 1e-12 and abs(Va_full + 6 - 4.8) < 1e-12
