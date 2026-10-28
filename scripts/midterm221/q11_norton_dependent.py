r"""Midterm Questions Q11: Norton at a-b with a voltage-controlled current source v_x/8 (v_x across the 12 Ω).
Mixed sources, so the user's method: V_oc first (a-b open, two meshes, I_2 = -v_x/8 -> V_oc = 72 V), then a-b
shorted (supermesh -> I_sc = 4.5 A down the short, a -> b), R_N = V_oc / I_sc = 16 Ω. The dependent source stays on
in both circuits; no test source. (b) R_L = 8 Ω draws 3 A (current divider)."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

TOPIC = 'Norton with a dependent source'
MARKS = 10
TITLE = 'Norton: open, then short, then pick the load'
SOURCE = 'Assessment Problem 4.19 and Textbook P4.80'
PROMPT = (r'**(a)** Find the Norton equivalent of the circuit at terminals $a$–$b$. '
          r'**(b)** What load resistor $R_L$, connected across $a$–$b$, draws $3\,\mathrm{A}$?')

O = r'\,\Omega'
V = r'\,\mathrm{V}'
A = r'\,\mathrm{A}'

V1 = f'V1 0,3 -> 0,0 "$36{V}$"'
R1 = f'R1 0,3 -> 3,3 "$6{O}$"'
R2 = f'R2 3,3 -> 3,0 "$12{O}$" v="$v_x$"'
R3 = f'R3 3,3 -> 7,3 "$4{O}$"'
G1 = 'G1 7,0 -> 7,3 "$v_x/8$"'
TERMS = '\n'.join(['wire 7,3 -> 9,3', 'terminal 9,3 "$a$" right', 'wire 0,0 -> 9,0', 'terminal 9,0 "$b$" right'])
NODES = 'label 3,3 "$m$" above\nground 0,0'
SHORT = 'wire 9,3 -> 9,0\n#= text 10,1.5 "short" color=accent'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(V1, R1, R2, R3, G1, TERMS, NODES)
OPEN = j(GIVEN, 'gap 9,3 -> 9,0 v="$V_{oc}$"')
SHORTED = j(GIVEN, SHORT)
# 12 Ω signs go on its left: its v_x marks sit on the right
SIGNS_1 = j('#= sign 0.7,2.62 +', '#= sign 2.3,2.62 -',        # 6 Ω: I_1 goes right
            '#= sign 2.62,2.1 +', '#= sign 2.62,0.9 -')        # 12 Ω: I_1 goes down
SIGNS_S = j('#= sign 2.62,0.9 +', '#= sign 2.62,2.1 -',        # 12 Ω: I_2 goes up
            '#= sign 4.1,2.62 +', '#= sign 5.9,2.62 -')        # 4 Ω: I_2 goes right
# open circuit: two meshes (nothing flows right of the dependent source)
MESHES_O = j('#= mesh 1.5,1.5 "$I_1$" cw r=0.6', '#= mesh 5,1.5 "$I_2$" cw r=0.6')
CONSTRAINT_O = '#= text 5,-0.8 "$I_2=-v_x/8$" color=purple'
# short circuit: three meshes
MESHES = j('#= mesh 1.5,1.5 "$I_1$" cw r=0.6', '#= mesh 5,1.5 "$I_2$" cw r=0.6', '#= mesh 8,1.5 "$I_3$" cw r=0.4')
CONSTRAINT = '#= text 5,-0.8 "$I_3-I_2=v_x/8$" color=purple'
# the walk from a to b with a-b open: actual drops, + where you enter
WALK_SIGNS = j('#= sign 5.9,2.62 +', '#= sign 4.1,2.62 -',     # 4 Ω: 6 A really flows a -> m, so + on the a side
               '#= sign 2.62,2.1 +', '#= sign 2.62,0.9 -')     # 12 Ω: v_x = 48 V, + on top
VOC = r'#+ $V_{oc}=72\,\mathrm{V}$'
NORTON = j(f'IN 5,0 -> 5,3 "$4.5{A}$"', f'RN 7,3 -> 7,0 "$16{O}$"', 'wire 5,3 -> 9,3', 'wire 5,0 -> 9,0')
NTERMS = 'terminal 9,3 "$a$" right\nterminal 9,0 "$b$" right'

STEPS = [
    ('The circuit', GIVEN, r'''
Norton equivalent = current source $I_N$ in parallel with $R_N$.

The circuit has a **dependent** source and an **independent** one → no test source.

**Plan**
1. $a$–$b$ open → $V_{oc}$.
2. $a$–$b$ shorted → $I_{sc}$ (this is $I_N$).
3. $R_N=V_{oc}/I_{sc}$.

The $v_x/8$ source copies $v_x$, so it stays **on** in both circuits.
'''),
    ('Open $a$–$b$: two meshes', j(OPEN, MESHES_O, CONSTRAINT_O), r'''
Nothing is connected at $a$–$b$ → no current right of the $v_x/8$ source. Two windows: $I_1$, $I_2$, clockwise.

Only $I_2$ passes the $v_x/8$ source. Its arrow points **up**; $I_2$ goes **down** through it:

$$
-I_2=\frac{v_x}{8}
$$

Control: $v_x$ is across the $12\,\Omega$, $+$ on top. $I_1$ goes down through it, $I_2$ goes up:

$$
v_x=12(I_1-I_2)
$$
'''),
    ('KVL in mesh $I_1$, solve', j(OPEN, MESHES_O, CONSTRAINT_O, SIGNS_1), r'''
Walk with $I_1$; sign you **enter** each element by:

$$
-36+6I_1+12(I_1-I_2)=0
$$

Constraint + control: $I_2=-\frac{12(I_1-I_2)}{8}=-1.5I_1+1.5I_2$ → $I_2=3I_1$. Into KVL:

$$
18I_1-12(3I_1)=36 \;\Rightarrow\; I_1=-2\,\mathrm{A},\quad I_2=-6\,\mathrm{A}
$$

$$
v_x=12(-2+6)=48\,\mathrm{V}
$$

$I_2<0$: the $6\,\mathrm{A}$ really runs **counter**clockwise, $a\to m$ in the $4\,\Omega$.
'''),
    ('Walk from $a$ to $b$ → $V_{oc}$', j(OPEN, WALK_SIGNS, '#= path 9,3 -> 7,3 -> 3,3 -> 3,0 -> 8.6,0',
                                       '#= text 5,2.1 "$24\\,\\mathrm{V}$" color=pink',
                                       '#= text 1.9,0.55 "$48\\,\\mathrm{V}$" color=pink', VOC), r'''
Ohm's law on the $4\,\Omega$: $(4)(6)=24\,\mathrm{V}$, $+$ on the $a$ side (the current enters there).

The $12\,\Omega$ holds $v_x=48\,\mathrm{V}$, $+$ on top.

Walk from $a$ (the $+$ of $V_{oc}$) to $b$; you enter both at $+$:

$$
\boxed{V_{oc}=24+48=72\,\mathrm{V}}
$$
'''),
    ('Short $a$–$b$: three meshes', j(SHORTED, MESHES, CONSTRAINT), r'''
A wire from $a$ down to $b$. The current in it, $a\to b$, is $I_{sc}$.

Three windows → $I_1$, $I_2$, $I_3$. $I_3$ is the current in the short.

The $v_x/8$ source now sits between $I_2$ and $I_3$ → **supermesh**:

$$
I_3-I_2=\frac{v_x}{8}
$$

Mesh $I_1$ and the control $v_x=12(I_1-I_2)$ are the same as before.
'''),
    ('KVL around the supermesh', j(SHORTED, MESHES, CONSTRAINT, SIGNS_S,
                                   '#= path 3,0 -> 3,3 -> 7,3 -> 9,3 -> 9,0 -> 3.4,0'), r'''
Walk around $I_2$ and $I_3$ **together**, skipping the $v_x/8$ branch:
- $12\,\Omega$ (shared with $I_1$): $+12(I_2-I_1)$
- $4\,\Omega$: $+4I_2$
- the short: $0\,\mathrm{V}$

$$
12(I_2-I_1)+4I_2=0 \;\Rightarrow\; I_2=0.75I_1
$$

Mesh $I_1$ (same as before):

$$
18I_1-12I_2=36
$$
'''),
    ('Solve → $I_{sc}$', j(SHORTED, '#= path 9,3 -> 9,0.4 "$I_{sc}=4.5\\,\\mathrm{A}$"', VOC,
                         r'#+ $I_N=I_{sc}=4.5\,\mathrm{A}$'), r'''
$$
18I_1-9I_1=36 \;\Rightarrow\; I_1=4\,\mathrm{A},\quad I_2=3\,\mathrm{A}
$$

$$
v_x=12(4-3)=12\,\mathrm{V} \qquad I_3=I_2+\frac{v_x}{8}=3+1.5
$$

$I_3$ runs **down** the short, from $a$ ($+$ of $V_{oc}$) to $b$ ($-$):

$$
\boxed{I_N=I_{sc}=4.5\,\mathrm{A}}
$$
'''),
    ('$R_N=V_{oc}/I_{sc}$', j(OPEN, VOC, r'#+ $R_N=16\,\Omega$', '#= text 10.4,1.5 "$72\\,\\mathrm{V}$" color=pink'), r'''
$$
R_N=\frac{V_{oc}}{I_{sc}}=\frac{72}{4.5}
$$

$$
\boxed{R_N=16\,\Omega}
$$

The dependent source was on in both circuits, so $R_N$ already includes it.
'''),
    ('(a) Norton circuit', j(NORTON, NTERMS), r'''
$$
\boxed{I_N=4.5\,\mathrm{A}\ (\text{up, into } a)\;\parallel\;R_N=16\,\Omega}
$$

Check: open $a$–$b$ → all $4.5\,\mathrm{A}$ goes through $R_N$:

$$
(4.5)(16)=72\,\mathrm{V}=V_{oc}\ ✓
$$
'''),
    ('(b) Pick the load', j(NORTON, f'RL 9,3 -> 9,0 "$R_L$" i="$i_L$"', 'label 9,3 "$a$" right',
                            'label 9,0 "$b$" right', r'#+ $R_L=8\,\Omega$'), r'''
$4.5\,\mathrm{A}$ splits between $R_N$ and $R_L$. Current divider:

$$
i_L=I_N\,\frac{R_N}{R_N+R_L} \;\Rightarrow\; 3=\frac{(4.5)(16)}{16+R_L}
$$

$$
16+R_L=24 \;\Rightarrow\; \boxed{R_L=8\,\Omega}
$$

No need to touch the dependent source again: the Norton circuit already holds it.
'''),
]


def _net(vs=36):
    return [('V', 'V1', 's', '0', vs), ('R', 'R1', 's', 'm', 6), ('R', 'R2', 'm', '0', 12), ('R', 'R3', 'm', 'a', 4),
            ('G', 'G1', '0', 'a', {'m': 1 / 8})]


def checks(check):
    els, _ = check(GIVEN)
    s, m = els['R1']
    a = els['R3'][1]
    assert els['V1'] == (s, '0') and els['R2'] == (m, '0') and els['R3'][0] == m, els
    assert els['G1'] == ('0', a), els                                  # v_x/8 pushes up into a
    for d in (OPEN, SHORTED, NORTON, j(NORTON, NTERMS)):
        check(d)
    # open circuit by mesh: -I2 = vx/8, vx = 12(I1 - I2)
    I1, I2 = F(-2), F(-6)
    vx = 12 * (I1 - I2)
    assert vx == 48 and -I2 == vx / 8
    assert I2 == -F(3, 2) * I1 + F(3, 2) * I2 and I2 == 3 * I1
    assert -36 + 6 * I1 + 12 * (I1 - I2) == 0 and 18 * I1 - 12 * (3 * I1) == 36
    Voc = 4 * (-I2) + vx                                               # 6 A a -> m in the 4 Ω, then v_x
    assert Voc == 72 and 4 * 6 == 24
    # short circuit by mesh
    J1, J2 = F(4), F(3)
    wx = 12 * (J1 - J2)
    J3 = J2 + wx / 8
    assert -36 + 6 * J1 + 12 * (J1 - J2) == 0 and 18 * J1 - 12 * J2 == 36
    assert 12 * (J2 - J1) + 4 * J2 == 0 and J2 == F(3, 4) * J1 and 18 * J1 - 9 * J1 == 36
    assert wx == 12 and J3 == F(9, 2)
    assert Voc / J3 == 16
    # load
    assert J3 * 16 / (16 + 8) == 3
    # independent solves
    net = _net()
    Vn, I, _ = solve(net)
    assert abs(Vn['a'] - 72) < 1e-9 and abs(Vn['m'] - 48) < 1e-9
    assert abs(I['R3'] + 6) < 1e-9                                     # m -> a is -6 A: 6 A flows a -> m
    _, I, _ = solve(net + [('V', 'S', 'a', '0', 0)])
    assert abs(I['S'] - 4.5) < 1e-9                                    # 4.5 A a -> b through the short
    _, I, _ = solve(net + [('R', 'RL', 'a', '0', 8)])
    assert abs(I['RL'] - 3) < 1e-9
