r"""Textbook P3.58: convert the 28-20-10 ohm delta to a wye, reduce, then v = (2 A)(R_in)."""

SECTION = 'A'
TITLE = 'A triangle with no series or parallel pairs'
SOURCE = 'Textbook P3.58'
CITES = [{'chunk_id': '9c36b847-99b2-4be9-a772-4855b2e5575d', 'source_id': '36da61a3-f7f4-45f0-bf0d-37ed16959f48', 'version': 1}]
PROMPT = 'Use a delta-to-wye transformation to find $v$.'

O = r'\,\Omega'
IS = r'I1 0,0 -> 0,3 "$2\,\mathrm{A}$" v_rev="$v$"'
LEFT = 'wire 0,3 -> 0,5'
RIGHT = 'wire 8,5 -> 8,3'
BOT = 'wire 0,0 -> 4,0\nwire 4,0 -> 8,0'
D28 = f'R1 0,5 -> 8,5 "$28{O}$"'
D20 = f'R2 0,3 -> 4,3 "$20{O}$"'
D10 = f'R3 4,3 -> 8,3 "$10{O}$"'
R5 = f'R4 4,3 -> 4,0 "$5{O}$"'
R105 = f'R5 8,3 -> 8,0 "$105{O}$"'
NODES = 'label 0,4 "$a$" right\nlabel 4,3 "$b$" above\nlabel 8,4 "$c$" left'
YNODES = 'label 0,4 "$a$" right\nlabel 4,3 "$b$" right\nlabel 8,4 "$c$" left'

# wye arms (n at 4,5)
YA = f'RA 0,5 -> 4,5 "$9.66{O}$"'
YC = f'RC 4,5 -> 8,5 "$4.83{O}$"'
YB = f'RB 4,5 -> 4,3 "$3.45{O}$"'
NLAB = 'label 4,5 "$n$" above'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(IS, LEFT, D28, RIGHT, D20, D10, R5, R105, BOT)
WYE = j(IS, LEFT, YA, YC, RIGHT, YB, R5, R105, BOT)
ARMS = [r'#+ $R_{an}=9.66\,\Omega$', r'#+ $R_{bn}=3.45\,\Omega$', r'#+ $R_{cn}=4.83\,\Omega$']

STEPS = [
    ('The circuit', GIVEN, r'''
Find $v$, the voltage across the $2\,\mathrm{A}$ source.

$v=(2\,\mathrm{A})(R_{in})$, so we need the resistance the source sees.

No two resistors are in series or in parallel.
'''),
    ('Spot the Δ', j(GIVEN, NODES, '#= region -0.75,2.55 8.3,5.75 "Δ"'), r'''
$28\,\Omega$, $20\,\Omega$ and $10\,\Omega$ form a triangle between $a$, $b$ and $c$.

That triangle (Δ) is what blocks every series/parallel move.
'''),
    ('Δ → Y', j(WYE, YNODES, NLAB, *ARMS), r'''
Same three corners $a$, $b$, $c$; new centre node $n$.

Each arm = (the two Δ resistors touching that corner) ÷ (sum).

Sum: $28+20+10=58\,\Omega$

$$
R_{an}=\frac{(28)(20)}{58}=\frac{280}{29}\approx9.66\,\Omega
$$

$$
R_{bn}=\frac{(20)(10)}{58}=\frac{100}{29}\approx3.45\,\Omega
$$

$$
R_{cn}=\frac{(28)(10)}{58}=\frac{140}{29}\approx4.83\,\Omega
$$
'''),
    ('Series pairs', j(IS, LEFT, YA, f'RBS 4,5 -> 4,0 "$8.45{O}$"', 'wire 4,5 -> 8,5', f'RCS 8,5 -> 8,0 "$109.83{O}$"', BOT, NLAB,
                       r'#+ $R_b=8.45\,\Omega$', r'#+ $R_c=109.83\,\Omega$'), r'''
From $n$ down to the bottom wire there are now two paths.

Through $b$: $R_{bn}$ and $5\,\Omega$ in series.

$$
R_b=3.45+5=8.45\,\Omega
$$

Through $c$: $R_{cn}$ and $105\,\Omega$ in series.

$$
R_c=4.83+105=109.83\,\Omega
$$
'''),
    ('Parallel pair', j(IS, LEFT, YA, f'RP 4,5 -> 4,0 "$7.84{O}$"', 'wire 0,0 -> 4,0', NLAB,
                        r'#+ $R_p=7.84\,\Omega$'), r'''
Both paths run from $n$ to the bottom wire → parallel.

$$
R_p=\frac{(8.45)(109.83)}{8.45+109.83}\approx7.84\,\Omega
$$
'''),
    ('Series → $R_{in}$', j(IS, 'wire 0,3 -> 0,5\nwire 0,5 -> 4,5', f'RIN 4,5 -> 4,0 "$17.5{O}$"', 'wire 0,0 -> 4,0',
                            r'#+ $R_{in}=17.5\,\Omega$'), r'''
$R_{an}$ and $R_p$ are in series:

$$
R_{in}=9.66+7.84=17.5\,\Omega
$$

(Exactly $17.5$ with the fractions.)
'''),
    ("Ohm's law → $v$", j(IS, 'wire 0,3 -> 0,5\nwire 0,5 -> 4,5', f'RIN 4,5 -> 4,0 "$17.5{O}$"', 'wire 0,0 -> 4,0',
                          '#= mesh 1.6,2.5 "$2\\,\\mathrm{A}$" cw r=0.7', '#= sign 4.38,3.2 +', '#= sign 4.38,1.8 -',
                          r'#+ $v=35\,\mathrm{V}$'), r'''
One loop: the source forces $2\,\mathrm{A}$ through $R_{in}$.

$2\,\mathrm{A}$ enters $R_{in}$ at the top → $+$ on top, same as $v$.

$$
v=(2)(17.5)=35\,\mathrm{V}
$$

$$
\boxed{v=35\,\mathrm{V}}
$$
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    a, b, c = els['R2'][0], els['R2'][1], els['R3'][1]
    assert els['I1'][1] == a and els['R1'] == (a, c) and els['R4'][0] == b and els['R5'][0] == c, els
    g = els['I1'][0]
    assert els['R4'][1] == g and els['R5'][1] == g, els
    w, _ = check(WYE)
    n = w['RA'][1]
    assert w['RA'][0] == w['I1'][1] and w['RC'][0] == n and w['RB'] == (n, w['R4'][0]) and w['RC'][1] == w['R5'][0], w
    from fractions import Fraction as F
    S = 28 + 20 + 10
    ra, rb, rc = F(28 * 20, S), F(20 * 10, S), F(28 * 10, S)
    assert (ra, rb, rc) == (F(280, 29), F(100, 29), F(140, 29))
    assert (round(float(ra), 2), round(float(rb), 2), round(float(rc), 2)) == (9.66, 3.45, 4.83)
    Rb, Rc = rb + 5, rc + 105
    assert (round(float(Rb), 2), round(float(Rc), 2)) == (8.45, 109.83)
    Rp = Rb * Rc / (Rb + Rc)
    assert round(float(Rp), 2) == 7.84
    Rin = ra + Rp
    assert Rin == F(35, 2)
    assert Rin * 2 == 35
    # independent check: nodal solve of the original circuit
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
    from mna import solve
    out = solve([('I', 'is', '0', 'a', 2.0), ('R', 'r28', 'a', 'c', 28), ('R', 'r20', 'a', 'b', 20),
                 ('R', 'r10', 'b', 'c', 10), ('R', 'r5', 'b', '0', 5), ('R', 'r105', 'c', '0', 105)])
    V = out[0] if isinstance(out, tuple) else out
    assert abs(V['a'] - 35) < 1e-9, V
