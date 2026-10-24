r"""Textbook P2.20: one known current, walked back through Ohm's law, a KVL loop and KCL.

`#+` values accumulate from step to step: declare each one only in the step that finds it.
"""

SECTION = 'A'
TITLE = 'Walk back from one known current'
SOURCE = 'Textbook P2.20'
CITES = [{'chunk_id': 'adc79ac3-8176-48f6-a99a-7689db8dd0a3', 'source_id': '36da61a3-f7f4-45f0-bf0d-37ed16959f48', 'version': 1}]
PROMPT = (r'The current $i_a$ is $2\,\mathrm{mA}$. Find **(a)** $i_o$, **(b)** $i_g$ and '
          r'**(c)** the power delivered by the current source.')

K = r'\,\mathrm{k\Omega}'
IG = 'I1 0,0 -> 0,3 "$i_g$"'
R1 = f'R1 2,3 -> 2,0 "$2{K}$" i="$i_o$"'
R2 = f'R2 2,3 -> 5,3 "$1{K}$" i="$i_a$"'
R3 = f'R3 5,3 -> 5,0 "$4{K}$" flip'
R4 = f'R4 5,0 -> 2,0 "$3{K}$"'
REST = '\n'.join(['wire 0,3 -> 2,3', 'wire 2,0 -> 0,0',
                  'label 2,3 "$a$" above', 'label 5,3 "$b$" above', 'label 5,0 "$c$" right', 'label 0,0 "$d$" left'])


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(IG, R1, R2, R3, R4, REST)

CHAIN = r'#= path 2.3,3 -> 5,3 -> 5,0 -> 2.3,0 "$2\,\mathrm{mA}$" thin'
SIGNS = j('#= sign 2.55,2.62 +', '#= sign 4.45,2.62 -',    # 1k: i_a enters on the left
          '#= sign 4.62,2.2 +', '#= sign 4.62,0.8 -',      # 4k: enters at the top
          '#= sign 4.45,0.38 +', '#= sign 2.55,0.38 -')    # 3k: enters on the right
FALLS = j(r'#= text 3.5,2.2 "$2\,\mathrm{V}$" color=pink', r'#= text 4.15,1.5 "$8\,\mathrm{V}$" color=pink',
          r'#= text 3.5,0.8 "$6\,\mathrm{V}$" color=pink')
SIGNS_2K = '#= sign 1.62,2.2 +\n#= sign 1.62,0.8 -'
WALK = '#= path 2,3 -> 5,3 -> 5,0 -> 2,0 -> 2,2.3'
V2K = r'#= text 1.3,1.5 "$16\,\mathrm{V}$" color=pink'

STEPS = [
    ('The circuit', GIVEN, r'''
Only one number is given: $i_a=2\,\mathrm{mA}$.

Follow it: from $a$ it goes through the $1$, $4$ and $3\,\mathrm{k\Omega}$ back to $d$.
'''),
    ('Same current down the chain', j(GIVEN, CHAIN), r'''
$b$ and $c$ each join just **two** elements.

KCL at a two-element node: what comes in goes out.

So the $1$, $4$ and $3\,\mathrm{k\Omega}$ all carry $2\,\mathrm{mA}$.
'''),
    ("Ohm's law on each", j(GIVEN, SIGNS, FALLS, r'#+ $V_{1k}=2\,\mathrm{V}$', r'#+ $V_{4k}=8\,\mathrm{V}$', r'#+ $V_{3k}=6\,\mathrm{V}$'), r'''
$+$ where the $2\,\mathrm{mA}$ **enters** each resistor.

- $1\,\mathrm{k\Omega}$: $(2m)(1k)=2\,\mathrm{V}$
- $4\,\mathrm{k\Omega}$: $(2m)(4k)=8\,\mathrm{V}$
- $3\,\mathrm{k\Omega}$: $(2m)(3k)=6\,\mathrm{V}$

$m\cdot k=1$, so the prefixes cancel.
'''),
    ('KVL around the right loop', j(GIVEN, SIGNS, FALLS, SIGNS_2K, WALK, r'#+ $V_{2k}=16\,\mathrm{V}$'), r'''
Walk clockwise from $a$; write the sign you **enter** each element by:
- $1\,\mathrm{k\Omega}$: enter $+$ → $+2$
- $4\,\mathrm{k\Omega}$: enter $+$ → $+8$
- $3\,\mathrm{k\Omega}$: enter $+$ → $+6$
- $2\,\mathrm{k\Omega}$ (going up): enter $-$ → $-V_{2k}$

$$
2+8+6-V_{2k}=0 \;\Rightarrow\; V_{2k}=16\,\mathrm{V}
$$
'''),
    ("Ohm's law → $i_o$", j(GIVEN, SIGNS_2K, V2K, r'#+ $i_o=8\,\mathrm{mA}$'), r'''
The $2\,\mathrm{k\Omega}$ has $16\,\mathrm{V}$ across it, $+$ on top.

$$
i_o=\frac{16}{2k}=8\,\mathrm{mA}
$$

Positive: it flows down, the way its arrow points.
'''),
    ('KCL at $a$ → $i_g$', j(GIVEN, V2K, r'#= text 1,3.5 "$i_g=10\,\mathrm{mA}$" color=pink', r'#+ $i_g=10\,\mathrm{mA}$'), r'''
Into $a$: $i_g$. Out of $a$: $i_o$ and $i_a$.

$$
i_g-i_o-i_a=0
$$

$$
i_g=8m+2m=10\,\mathrm{mA}
$$
'''),
    ('Power of the source', j(GIVEN, r'#= text -0.95,0.85 "$160\,\mathrm{mW}$" color=green', r'#+ $p_g=160\,\mathrm{mW}$'), r'''
The source sits between $d$ and $a$: $16\,\mathrm{V}$ across it, pushing $10\,\mathrm{mA}$ up into $a$.

$$
p_g=(16)(10m)=160\,\mathrm{mW}\ \text{delivered}
$$

**Check**, $V\cdot I$ for each resistor:

$$
(16)(8m)+(2)(2m)+(8)(2m)+(6)(2m)
$$

$$
=128+4+16+12=160\,\mathrm{mW}\ ✓
$$
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    a, d = els['R1']
    assert els['I1'] == (d, a), els                            # source arrow points up into a
    assert els['R2'][0] == a and els['R2'][1] == els['R3'][0], els
    assert els['R3'][1] == els['R4'][0] and els['R4'][1] == d, els
    from fractions import Fraction as F
    ia = F(2, 1000)
    v1, v4, v3 = ia * 1000, ia * 4000, ia * 3000
    assert (v1, v4, v3) == (2, 8, 6)
    v2k = v1 + v4 + v3                                         # 2 + 8 + 6 - V2k = 0
    assert v2k == 16
    io = v2k / 2000
    assert io == F(8, 1000)
    ig = io + ia
    assert ig == F(10, 1000)
    pg = v2k * ig
    assert pg == F(160, 1000)
    assert v2k * io + v1 * ia + v4 * ia + v3 * ia == pg
    assert [v2k * io * 1000, v1 * ia * 1000, v4 * ia * 1000, v3 * ia * 1000] == [128, 4, 16, 12]
    # independent check: drive the circuit with i_g = 10 mA and solve it
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
    from mna import solve
    V, I, P = solve([('I', 'ig', '0', 'a', 0.010), ('R', 'r2', 'a', '0', 2000), ('R', 'r1', 'a', 'b', 1000),
                     ('R', 'r4', 'b', 'c', 4000), ('R', 'r3', 'c', '0', 3000)])
    assert abs(I['r1'] - 0.002) < 1e-12 and abs(I['r2'] - 0.008) < 1e-12 and abs(V['a'] - 16) < 1e-9, (V, I)
