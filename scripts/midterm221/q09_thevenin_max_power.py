r"""Midterm Questions Q9: Thévenin seen by R_L with a current-controlled voltage source 2 i_x, then maximum power.
V_Th: the load is open, so the 2 Ω and 2 i_x carry nothing -> one mesh (i_x = 2.5 A), walk a -> b: 5 + 30 = 35 V.
R_Th = V_oc / I_sc (mixed sources: the user's method, no test source): short a-b, two meshes with the dependent
source on, i_x = I_1; mesh 2 gives I_2 = I_1, mesh 1 gives I_1 = 10 A -> I_sc = I_2 = 10 A (a -> b), R_Th = 3.5 Ω.
Matched load 3.5 Ω: 5 A, 87.5 W; in the original circuit I_1 = 6.25 A, so the 40 V source gives 250 W -> 35 %.
Inspired by Fall 2025 Q1 and Assessment Problems 4.19-4.21."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

TOPIC = 'Thévenin with a dependent source, and maximum power transfer'
MARKS = 12
FORMULAS = ['max_power']
TITLE = 'Thévenin: a dependent source and a matched load'
SOURCE = 'Fall 2025 Question 1 and Assessment Problems 4.19–4.21'
PROMPT = (r'The dependent source is controlled by $i_x$, the current in the $4\,\Omega$ resistor. '
          r'**(a)** Find the Thévenin equivalent circuit seen by $R_L$. '
          r'**(b)** Find the $R_L$ that receives the maximum power. '
          r'**(c)** Find that maximum power. '
          r'**(d)** With this $R_L$ connected, what percentage of the power delivered by the $40\,\mathrm{V}$ source '
          r'reaches $R_L$?')

O = r'\,\Omega'
V = r'\,\mathrm{V}'
A = r'\,\mathrm{A}'

V1 = f'V1 0,3 -> 0,0 "$40{V}$"'
R1 = f'R1 0,3 -> 3,3 "$4{O}$" i="$i_x$"'
R2 = f'R2 3,3 -> 3,0 "$12{O}$"'
H1 = 'H1 6,3 -> 3,3 "$2i_x$"'                     # + on the right (node n)
R3 = f'R3 6,3 -> 8,3 "$2{O}$"'
TOP = 'wire 8,3 -> 10,3'
BOT = 'wire 0,0 -> 10,0\nground 0,0'
NODES = 'label 3,3 "$m$" below\nlabel 6,3 "$n$" above'
RL = f'RL 10,3 -> 10,0 "$R_L$"'
AB = 'label 10,3 "$a$" right\nlabel 10,0 "$b$" right'
TERMS = 'terminal 10,3 "$a$" right\nterminal 10,0 "$b$" right'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(V1, R1, R2, H1, R3, TOP, RL, BOT, NODES, AB)
OPEN = j(V1, R1, R2, H1, R3, TOP, BOT, NODES, TERMS, 'gap 10,3 -> 10,0 v="$V_{oc}$"')
SHORT = j(V1, R1, R2, H1, R3, TOP, 'wire 10,3 -> 10,0', BOT, NODES, TERMS, '#= text 11,0.7 "short" color=accent')
TH = j(f'VTH 0,3 -> 0,0 "$35{V}$"', f'RTH 0,3 -> 3,3 "$3.5{O}$"', 'wire 3,3 -> 10,3', BOT, TERMS)
LOADED = j(V1, R1, R2, H1, R3, TOP, f'RL 10,3 -> 10,0 "$3.5{O}$"', BOT, NODES, AB)

MESH = '#= mesh 1.3,1.4 "$I$" cw r=0.55'
SIGNS1 = j('#= sign 1.0,2.6 +', '#= sign 2.1,2.6 -',          # 4 Ω: I goes right
           '#= sign 2.6,2.1 +', '#= sign 2.6,0.8 -')          # 12 Ω: I goes down
SIGNS12 = '#= sign 3.4,2.3 +\n#= sign 3.4,0.7 -'               # 12 Ω seen from the walk (+ on top)
M1 = MESH.replace('"$I$"', '"$I_1$"')
M2 = '#= mesh 6.5,1.5 "$I_2$" cw r=0.8'
CONTROL = '#= text 5,-0.8 "$i_x=I_1$" color=purple'
SIGNS2 = j('#= sign 3.4,0.8 +', '#= sign 3.4,2.1 -',          # 12 Ω: I_2 goes up
           '#= sign 6.5,2.6 +', '#= sign 7.5,2.6 -')          # 2 Ω: I_2 goes right
ISC = '#= path 10,2.6 -> 10,0.4 "$I_{sc}$"'

STEPS = [
    ('The circuit', GIVEN, r'''
$R_L$ is the **load**. Thévenin replaces everything else with one source and one resistor.

The diamond $2i_x$ is a **dependent** source: its voltage is $2\times$ the current in the $4\,\Omega$.

**Plan** (independent and dependent sources → $V_{oc}$ and $I_{sc}$)
1. Pull out $R_L$ → $V_{Th}=V_{oc}$ with mesh + Ohm.
2. Short $a$–$b$ → $I_{sc}$ with mesh + Ohm.
3. $R_{Th}=V_{oc}/I_{sc}$.
4. Max power: formula sheet, $R_L=R_{Th}$ and $(p_L)_{max}=\dfrac{V_{Th}^2}{4R_{Th}}$.
5. Back to the real circuit for the percentage.
'''),
    ('Pull out the load', OPEN, r'''
$R_L$ is gone → $a$–$b$ is **open**.

Nothing flows out of $a$, so the $2\,\Omega$ and the $2i_x$ source carry **no current**.

Only the left window is a closed loop.
'''),
    ('Mesh + Ohm', j(OPEN, MESH, SIGNS1, r'#+ $i_x=2.5\,\mathrm{A}\ (\text{open})$'), r'''
One mesh $I$, clockwise. It is the current in the $4\,\Omega$ → $i_x=I$.

Sign you **enter** each element by:
- $40\,\mathrm{V}$: enter $-$ → $-40$
- $4\,\Omega$: $+4I$
- $12\,\Omega$: $+12I$

$$
-40+4I+12I=0
$$

$$
I=i_x=2.5\,\mathrm{A}
$$
'''),
    ('KVL walk to $V_{oc}$', j(OPEN, SIGNS12, '#= path 9.6,3 -> 3,3 -> 3,0 -> 9.6,0',
                                '#= text 4.5,2.3 "$5\\,\\mathrm{V}$" color=pink',
                                '#= text 4.1,1.5 "$30\\,\\mathrm{V}$" color=pink', r'#+ $V_{oc}=35\,\mathrm{V}$'), r'''
Walk from $a$ to $b$ through $n$ and $m$:
- $2\,\Omega$: no current → $0$
- $2i_x$: enter $+$ → $+2(2.5)=+5$
- $12\,\Omega$: $I$ enters at the top → $+12(2.5)=+30$

$$
V_{oc}=0+5+30
$$

$$
\boxed{V_{Th}=V_{oc}=35\,\mathrm{V}}
$$

$a$ is the $+$ end of $V_{oc}$, $b$ the $-$ end.
'''),
    ('Short $a$–$b$', j(SHORT, M1, M2, CONTROL), r'''
Put a wire from $a$ to $b$. The $2i_x$ **stays on**: it is not a real source, it follows $i_x$.

$I_{sc}$ is the current down the short, from $a$ (the $+$ of $V_{oc}$) to $b$ (the $-$).

Two windows → $I_1$, $I_2$, clockwise. $I_2$ goes **down** the short → $I_{sc}=I_2$.

Control equation: only $I_1$ runs through the $4\,\Omega$:

$$
i_x=I_1
$$
'''),
    ('KVL in mesh $I_1$', j(SHORT, M1, M2, CONTROL, SIGNS1), r'''
Same loop as before, but the $12\,\Omega$ is now shared with $I_2$:

$$
-40+4I_1+12(I_1-I_2)=0
$$

$$
16I_1-12I_2=40
$$
'''),
    ('KVL in mesh $I_2$ → solve', j(SHORT, M1, M2, CONTROL, SIGNS2, r'#+ $I_1=10\,\mathrm{A}$'), r'''
Walk with $I_2$ (up the $12\,\Omega$, right across the top, down the short):
- $12\,\Omega$: $+12(I_2-I_1)$
- $2i_x$: enter $-$ → $-2i_x=-2I_1$
- $2\,\Omega$: $+2I_2$
- short: $0$

$$
12(I_2-I_1)-2I_1+2I_2=0 \;\Rightarrow\; 14I_2=14I_1 \;\Rightarrow\; I_2=I_1
$$

Into mesh $I_1$: $16I_1-12I_1=40$

$$
I_1=I_2=10\,\mathrm{A}
$$

($I_1-I_2=0$: the $12\,\Omega$ carries nothing here.)
'''),
    ('$I_{sc}$, then $R_{Th}$', j(SHORT, M1, M2, ISC, r'#+ $I_{sc}=10\,\mathrm{A}$', r'#+ $R_{Th}=3.5\,\Omega$'), r'''
$I_2=10\,\mathrm{A}$ goes down the short, $a$ → $b$:

$$
I_{sc}=10\,\mathrm{A}
$$

Divide:

$$
R_{Th}=\frac{V_{oc}}{I_{sc}}=\frac{35}{10}
$$

$$
\boxed{R_{Th}=3.5\,\Omega}
$$
'''),
    ('(a) Thévenin circuit', TH, r'''
$$
V_{Th}=35\,\mathrm{V}\ \text{in series with}\ R_{Th}=3.5\,\Omega
$$

This is all $R_L$ "sees".

Check: short $a$–$b$ here → $35/3.5=10\,\mathrm{A}$, the same $I_{sc}$ ✓
'''),
    ('(b), (c) Matched load', j(TH, f'RL 10,3 -> 10,0 "$R_L=3.5{O}$"', '#= mesh 5,1.5 "$i_o$" cw r=0.8',
                                 '#= sign 0.6,2.62 +', '#= sign 2.4,2.62 -', '#= sign 9.6,2.3 +', '#= sign 9.6,0.7 -',
                                 r'#+ $R_L=3.5\,\Omega$', r'#+ $(p_L)_{max}=87.5\,\mathrm{W}$'), r'''
Formula sheet: the load gets the most power when it matches.

$$
\boxed{R_L=R_{Th}=3.5\,\Omega}
$$

Formula sheet:

$$
(p_L)_{max}=\frac{V_{Th}^2}{4R_{Th}}=\frac{(35)^2}{4(3.5)}=\frac{1225}{14}
$$

$$
\boxed{(p_L)_{max}=87.5\,\mathrm{W}}
$$

Check with mesh + Ohm: $-35+3.5i_o+3.5i_o=0$ → $i_o=5\,\mathrm{A}$, $p_L=i_o^2R_L=(5)^2(3.5)=87.5\,\mathrm{W}$ ✓
'''),
    ('(d) Back to the real circuit', j(LOADED, M1, '#= mesh 6.5,1.5 "$I_2$" cw r=0.8',
                                       SIGNS1, r'#+ $I_1=6.25\,\mathrm{A}$', r'#+ $P_{40V}=250\,\mathrm{W}$'), r'''
The Thévenin circuit is exact at $a$–$b$, so the load current is the same here: $I_2=i_o=5\,\mathrm{A}$.

Only mesh 1 is left to find ($12\,\Omega$ shared → $I_1-I_2$):

$$
-40+4I_1+12(I_1-5)=0 \;\Rightarrow\; 16I_1=100 \;\Rightarrow\; I_1=6.25\,\mathrm{A}
$$

The $40\,\mathrm{V}$ source carries $I_1$:

$$
P_{40V}=(40)(6.25)=250\,\mathrm{W}
$$

$$
\boxed{\frac{(p_L)_{max}}{P_{40V}}=\frac{87.5}{250}=35\,\%}
$$
'''),
]


def _net(rl=None):
    # i_x = current s -> m in the 4 Ω = (V_s - V_m)/4;  V_n - V_m = 2 i_x
    net = [('V', 'V1', 's', '0', 40), ('R', 'R1', 's', 'm', 4), ('R', 'R2', 'm', '0', 12),
           ('E', 'H1', 'n', 'm', {'s': F(2, 4), 'm': -F(2, 4)}, 0), ('R', 'R3', 'n', 'a', 2)]
    return net + ([('R', 'RL', 'a', '0', rl)] if rl else [])


def checks(check):
    els, _ = check(GIVEN)
    s, m = els['R1']
    n, a = els['R3']
    assert els['V1'] == (s, '0') and els['R2'] == (m, '0') and els['H1'] == (n, m) and els['RL'] == (a, '0'), els
    for d in (OPEN, TH, LOADED):
        check(d)
    sh, _ = check(SHORT)
    assert sh['R3'][1] == '0' and sh['R2'] == (sh['R1'][1], '0'), sh      # a is wired to b
    # V_Th by one mesh + walk
    I = F(40, 16)
    assert -40 + 4 * I + 12 * I == 0 and I == F(5, 2)
    assert 2 * I == 5 and 12 * I == 30 and 5 + 30 == 35
    Vn, _, _ = solve(_net())
    assert abs(Vn['a'] - 35) < 1e-9
    # I_sc by two meshes with a-b shorted, i_x = I_1
    I1, I2 = F(10), F(10)
    assert 16 * I1 - 12 * I2 == 40 and -40 + 4 * I1 + 12 * (I1 - I2) == 0
    assert 12 * (I2 - I1) - 2 * I1 + 2 * I2 == 0 and 16 * I1 - 12 * I1 == 40
    assert F(35) / I2 == F(7, 2)
    Vs, Is, _ = solve(_net() + [('V', 'VS', 'a', '0', 0)])               # the short, current a -> b
    assert abs(Is['VS'] - 10) < 1e-9 and abs(Is['R1'] - 10) < 1e-9 and abs(Is['R2']) < 1e-9, Is
    # matched load and efficiency
    IL = F(35, 7)
    assert IL == 5 and IL ** 2 * F(7, 2) == F(175, 2) and F(35 ** 2, 14) == F(175, 2)
    I1 = F(100, 16)
    assert -40 + 4 * I1 + 12 * (I1 - 5) == 0 and I1 == F(25, 4) and 40 * I1 == 250
    assert F(175, 2) / 250 == F(35, 100)
    Vl, Il, Pl = solve(_net(3.5))
    assert abs(Il['RL'] - 5) < 1e-9 and abs(Pl['RL'] - 87.5) < 1e-9 and abs(Il['R1'] - 6.25) < 1e-9
    assert abs(Pl['V1'] + 250) < 1e-9, Pl['V1']
