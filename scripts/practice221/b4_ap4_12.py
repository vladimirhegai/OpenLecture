r"""Assessment Problem 4.12: a 2 A source shared by two meshes (supermesh), then mesh c, then the 1 Ω power.
Mesh analysis with the user's sign rule (+ where the walk enters a resistor; KVL = sum of the sign you enter by).
Drawn 4 units tall instead of the week note's 6 (same topology, asserted)."""
from fractions import Fraction as F

SECTION = 'B'
TITLE = 'A current source between two windows'
SOURCE = 'Assessment Problem 4.12'
CITES = [{"chunk_id": "cc04109f-7d5d-4f90-8089-ceb5166c591c", "source_id": "3b287f2d-b408-41eb-a523-b299688ff303", "version": 1}]
PROMPT = r'Find the power dissipated in the $1\,\Omega$ resistor.'

O = r'\,\Omega'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(r'V1 0,2 -> 0,0 "$10\,\mathrm{V}$"', r'I1 0,2 -> 3,2 "$2\,\mathrm{A}$"', 'wire 0,2 -> 0,4',
          f'R1 0,4 -> 6,4 "$2{O}$"', 'wire 6,4 -> 6,2', f'R2 3,2 -> 6,2 "$2{O}$"', f'R3 3,2 -> 3,0 "$2{O}$"',
          r'V2 6,0 -> 6,2 "$6\,\mathrm{V}$"', f'R4 6,0 -> 3,0 "$1{O}$"', 'wire 3,0 -> 0,0',
          'label 3,2 "$m$" above', 'label 6,2 "$r$" right', 'label 6,0 "$q$" right', 'ground 0,0')

MESHES = j('#= mesh 1.5,1 "$I_a$" cw r=0.5', '#= mesh 4.6,3 "$I_b$" cw r=0.5', '#= mesh 4.35,1 "$I_c$" cw r=0.45')
CONSTRAINT = r'#= text 1.5,2.55 "$I_a-I_b=2$" color=purple'
# the supermesh walk: around meshes a and b together, skipping the shared 2 A source
WALK = '#= path 0,0 -> 0,4 -> 6,4 -> 6,2 -> 3,2 -> 3,0 -> 0.45,0'
SIGNS_SUPER = j('#= sign 0.5,3.6 +', '#= sign 5.5,3.6 -',      # 2 Ω top: walk goes right
                '#= sign 5.6,2.4 +', '#= sign 3.4,2.4 -',      # 2 Ω middle: walk goes left (r → m)
                '#= sign 2.65,1.6 +', '#= sign 2.65,0.4 -')    # 2 Ω down: walk goes down
SIGNS_C = j('#= sign 3.8,1.65 +', '#= sign 5.4,1.65 -',        # 2 Ω middle: I_c goes right
            '#= sign 5.6,-0.4 +', '#= sign 3.4,-0.4 -',        # 1 Ω: I_c goes left
            '#= sign 3.3,0.45 +', '#= sign 3.3,1.55 -')        # 2 Ω down: I_c goes up

STEPS = [
    ('The circuit', GIVEN, r'''
**Method: mesh.** 3 windows, and the $2\,\mathrm{A}$ source sits between two of them → a **supermesh** handles it.
'''),
    ('Mesh currents', j(GIVEN, MESHES), r'''
One clockwise mesh current per window: $I_a$ (lower left), $I_b$ (top), $I_c$ (lower right).

A shared resistor carries (own − neighbour).
'''),
    ('The shared current source', j(GIVEN, MESHES, CONSTRAINT), r'''
The $2\,\mathrm{A}$ source sits between mesh $a$ (below) and mesh $b$ (above).

Its arrow points **right**:
- $I_a$ goes right through it → $+I_a$
- $I_b$ goes left through it → $-I_b$

$$
I_a-I_b=2
$$

Its voltage is unknown → no KVL through it.
'''),
    ('KVL around the supermesh', j(GIVEN, MESHES, CONSTRAINT, WALK, SIGNS_SUPER), r'''
Walk around meshes $a$ and $b$ **together**, skipping the $2\,\mathrm{A}$ branch.

Sign you **enter** each element by:
- $10\,\mathrm{V}$: enter $-$ → $-10$
- $2\,\Omega$ top: $+2I_b$
- $2\,\Omega$ middle (shared with $c$): $+2(I_b-I_c)$
- $2\,\Omega$ down (shared with $c$): $+2(I_a-I_c)$

$$
-10+2I_b+2(I_b-I_c)+2(I_a-I_c)=0
$$

$$
2I_a+4I_b-4I_c=10
$$
'''),
    ('KVL in mesh $c$', j(GIVEN, MESHES, CONSTRAINT, SIGNS_C), r'''
Walk with $I_c$:
- $2\,\Omega$ middle: $+2(I_c-I_b)$
- $6\,\mathrm{V}$: enter $-$ → $-6$
- $1\,\Omega$: $+1I_c$
- $2\,\Omega$ down: $+2(I_c-I_a)$

$$
2(I_c-I_b)-6+I_c+2(I_c-I_a)=0
$$

$$
-2I_a-2I_b+5I_c=6
$$
'''),
    ('Solve', j(GIVEN, MESHES, r'#= text 1.5,0.3 "$I_a=7\,\mathrm{A}$" color=purple',
                r'#= text 2.4,3.0 "$I_b=5\,\mathrm{A}$" color=purple', r'#= text 4.6,0.3 "$I_c=6\,\mathrm{A}$" color=purple',
                r'#+ $I_a=7\,\mathrm{A}$', r'#+ $I_b=5\,\mathrm{A}$', r'#+ $I_c=6\,\mathrm{A}$'), r'''
Put $I_a=I_b+2$ into both:

$$
6I_b-4I_c=6 \qquad -4I_b+5I_c=10
$$

First one: $I_b=\dfrac{3+2I_c}{3}$. Into the second, $\times 3$:

$$
-12-8I_c+15I_c=30 \;\Rightarrow\; I_c=6\,\mathrm{A}
$$

$$
I_b=5\,\mathrm{A} \qquad I_a=7\,\mathrm{A}
$$
'''),
    ('Power in the $1\\,\\Omega$', j(GIVEN, MESHES, '#= path 6,-0.0 -> 3.4,0 thin color=orange',
                                     r'#= text 4.5,-0.75 "$36\,\mathrm{W}$" color=orange',
                                     r'#+ $p_{1\Omega}=36\,\mathrm{W}$'), r'''
Only $I_c$ runs through the $1\,\Omega$.

$$
p=I_c^2R=(6)^2(1)
$$

$$
\boxed{p_{1\Omega}=36\,\mathrm{W}}
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
    n1, m, r, q = els['V1'][0], els['R3'][0], els['R2'][1], els['V2'][0]
    assert els['V1'][1] == '0' and els['R3'][1] == '0' and els['R4'] == (q, '0'), els
    assert els['I1'] == (n1, m) and els['R1'] == (n1, r) and els['R2'] == (m, r) and els['V2'] == (q, r), els
    # independent nodal solve
    v = _mna().solve([('V', 'V1', 'n1', '0', 10), ('I', 'I1', 'n1', 'm', 2), ('R', 'R1', 'n1', 'r', 2),
                      ('R', 'R2', 'm', 'r', 2), ('R', 'R3', 'm', '0', 2), ('V', 'V2', 'q', 'r', 6), ('R', 'R4', 'q', '0', 1)])
    v = v[0] if isinstance(v, tuple) else v
    Ia, Ib, Ic = 7, 5, 6
    assert abs(v['q'] / 1 - Ic) < 1e-9                      # 1 Ω current q -> ground = I_c
    assert abs(v['m'] / 2 - (Ia - Ic)) < 1e-9                # 2 Ω down: I_a - I_c
    assert abs((v['n1'] - v['r']) / 2 - Ib) < 1e-9           # top 2 Ω: I_b
    assert Ia - Ib == 2
    assert -10 + 2 * Ib + 2 * (Ib - Ic) + 2 * (Ia - Ic) == 0 and 2 * Ia + 4 * Ib - 4 * Ic == 10
    assert 2 * (Ic - Ib) - 6 + Ic + 2 * (Ic - Ia) == 0 and -2 * Ia - 2 * Ib + 5 * Ic == 6
    assert 6 * Ib - 4 * Ic == 6 and -4 * Ib + 5 * Ic == 10 and F(3 + 2 * Ic, 3) == Ib
    assert -12 - 8 * Ic + 15 * Ic == 30
    assert Ic ** 2 * 1 == 36
