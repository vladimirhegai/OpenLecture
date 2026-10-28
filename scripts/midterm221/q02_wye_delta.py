r"""Midterm Questions Q2: a Y (R_1 = 10 at a, R_2 = 15 at b, R_3 = 30 at c) with a resistor across every pair of
its corners (a-b 20, a-c 20, b-c 10). Y -> Δ gives R_c = 30, R_b = 60, R_a = 90, each parallel with an existing
resistor (12, 15, 9) -> R_eq = 12 || 24 = 8 Ω, v = 40 V, P = 200 W, V_c = 15 V -> i_o = 1.5 A.
Not a balanced bridge (20/10 != 10/15), so the centre arm carries current and the Y -> Δ is needed.
Inspired by Assessment Problem 3.7 and the Chapter 3 Δ-Y problems."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

TOPIC = 'Y–Δ'
FORMULAS = ['delta_wye']           # the exam's formula sheet, shown under the question
MARKS = 8
TITLE = 'A Y with a resistor across every pair of corners'
SOURCE = 'Assessment Problem 3.7 and the Chapter 3 Δ–Y problems'
PROMPT = (r'**(a)** Use a Y-to-Δ transformation to find the equivalent resistance $R_{eq}$ seen by the '
          r'$5\,\mathrm{A}$ source. '
          r'**(b)** Find $v$. '
          r'**(c)** Find the power delivered by the source. '
          r'**(d)** Find $i_o$.')

O = r'\,\Omega'

IS = r'I1 -1,0 -> -1,3 "$5\,\mathrm{A}$" v_rev="$v$"'
FEED = 'wire -1,3 -> 2,3'
RXAB = f'RXAB 2,3 -> 2,0 "$20{O}$"'
RXAC = '\n'.join(['wire 2,3 -> 2,5', f'RXAC 2,5 -> 8,5 "$20{O}$"', 'wire 8,5 -> 8,3'])
RXBC = f'RXBC 8,3 -> 8,0 "$10{O}$" i="$i_o$"'
RY1 = f'RY1 2,3 -> 5,3 "$10{O}$"'
RY3 = f'RY3 5,3 -> 8,3 "$30{O}$"'
RY2 = f'RY2 5,3 -> 5,0 "$15{O}$"'
BOT = 'wire -1,0 -> 8,0\nground -1,0'
NODES = 'label 2,4 "$a$" left\nlabel 5,3 "$n$" above\nlabel 8,4 "$c$" right\nlabel 6.5,0 "$b$" below'

# the Y in the formula sheet's names: arm R_1 at a, R_2 at b, R_3 at c
NAMED = '\n'.join([f'RY1 2,3 -> 5,3 "$R_1=10{O}$"', f'RY3 5,3 -> 8,3 "$R_3=30{O}$"', f'RY2 5,3 -> 5,0 "$R_2=15{O}$"'])
# the new Δ: R_c across a-b, R_b across a-c, R_a across b-c (each named for the corner it faces)
RDC = '\n'.join(['wire 2,3 -> 4.5,3', f'RDC 4.5,3 -> 4.5,0 "$R_c=30{O}$"'])
RDB = f'RDB 4.5,3 -> 8,3 "$R_b=60{O}$"'
RDA = '\n'.join(['wire 8,3 -> 10.5,3', f'RDA 10.5,3 -> 10.5,0 "$R_a=90{O}$" flip', 'wire 8,0 -> 10.5,0'])
DNODES = 'label 2,4 "$a$" left\nlabel 8,4 "$c$" right\nlabel 6.5,0 "$b$" below'
# the reduced circuits: a is the top-left corner (4.5,3), c the top-right one (8,3)
RNODES = 'label 4.5,3 "$a$" above\nlabel 8,3 "$c$" right\nlabel 6.5,0 "$b$" below'


def j(*parts):
    return '\n'.join(parts)


GIVEN = j(IS, FEED, RXAB, RXAC, RY1, RY3, RY2, RXBC, BOT)
SPOT = j(IS, FEED, RXAB, RXAC, NAMED, RXBC, BOT, NODES)
DELTA = j(IS, FEED, RXAB, RXAC, RDC, RDB, RXBC, RDA, BOT, DNODES)
SIDES = [r'#+ $R_a=90\,\Omega$', r'#+ $R_b=60\,\Omega$', r'#+ $R_c=30\,\Omega$']
PAIRS = j(IS, 'wire -1,3 -> 4.5,3', f'RPAB 4.5,3 -> 4.5,0 "$20\\parallel30=12{O}$"',
          f'RPAC 4.5,3 -> 8,3 "$20\\parallel60=15{O}$"', f'RPBC 8,3 -> 8,0 "$10\\parallel90=9{O}$" flip', BOT, RNODES)
SERIES = j(IS, 'wire -1,3 -> 4.5,3', f'RPAB 4.5,3 -> 4.5,0 "$12{O}$"', 'wire 4.5,3 -> 8,3',
           f'RPS 8,3 -> 8,0 "$15+9=24{O}$" flip', BOT)
LAST = j(IS, 'wire -1,3 -> 4.5,3', f'REQ 4.5,3 -> 4.5,0 "$8{O}$"', 'wire -1,0 -> 4.5,0\nground -1,0')
BACK = j(IS, 'wire -1,3 -> 4.5,3', f'RPAB 4.5,3 -> 4.5,0 "$12{O}$"', f'RPAC 4.5,3 -> 8,3 "$15{O}$"',
         f'RPBC 8,3 -> 8,0 "$9{O}$"', BOT, RNODES)

STEPS = [
    ('The circuit', GIVEN, r'''
No two resistors are in series or in parallel.

**Plan**
1. Turn the Y into a Δ → every new Δ side lands on top of an old resistor → parallel pairs → $R_{eq}$.
2. $v=(5\,\mathrm{A})(R_{eq})$, then the power.
3. Find $V_c$ in the reduced circuit ($c$ survives every step), then $i_o$ by Ohm's law.
'''),
    ('Spot the Y', j(SPOT, '#= region 2.4,0.4 8.4,3.9 "Y"'), r'''
$10\,\Omega$, $15\,\Omega$ and $30\,\Omega$ meet at one centre node $n$, with outer ends at $a$, $b$, $c$.

**Match the formula sheet:** each Y arm is named for the corner it touches.
- $R_1$: arm at $a$ → $10\,\Omega$
- $R_2$: arm at $b$ → $15\,\Omega$
- $R_3$: arm at $c$ → $30\,\Omega$
'''),
    ('Y → Δ', j(DELTA, *SIDES), r'''
$n$ disappears. Corners $a$, $b$, $c$ stay; now one resistor joins each pair.

Formula sheet, Y → Δ. Top of every fraction:

$$
R_1R_2+R_2R_3+R_3R_1=150+450+300=900
$$

$$
R_a=\frac{900}{R_1}=\frac{900}{10}=90\,\Omega\quad(b\text{–}c)
$$

$$
R_b=\frac{900}{R_2}=\frac{900}{15}=60\,\Omega\quad(a\text{–}c)
$$

$$
R_c=\frac{900}{R_3}=\frac{900}{30}=30\,\Omega\quad(a\text{–}b)
$$
'''),
    ('Three parallel pairs', PAIRS, r'''
Every Δ side joins the same two nodes as an old resistor → parallel.

- $a$–$b$: $\dfrac{(20)(30)}{50}=12\,\Omega$
- $a$–$c$: $\dfrac{(20)(60)}{80}=15\,\Omega$
- $b$–$c$: $\dfrac{(10)(90)}{100}=9\,\Omega$
'''),
    ('Series', SERIES, r'''
$15\,\Omega$ ($a$–$c$) and $9\,\Omega$ ($c$–$b$) meet at $c$ with nothing else there → series:

$$
15+9=24\,\Omega
$$
'''),
    ('(a) Parallel → $R_{eq}$', j(LAST, r'#+ $R_{eq}=8\,\Omega$'), r'''
$12\,\Omega$ and $24\,\Omega$ both join $a$ to $b$:

$$
R_{eq}=\frac{(12)(24)}{12+24}=\frac{288}{36}
$$

$$
\boxed{R_{eq}=8\,\Omega}
$$
'''),
    ('(b), (c) $v$ and power', j(LAST, '#= mesh 1.75,1.5 "$5\\,\\mathrm{A}$" cw r=0.7', '#= sign 4.88,2.4 +',
                                 '#= sign 4.88,0.6 -', r'#+ $v=40\,\mathrm{V}$', r'#+ $P=200\,\mathrm{W}$'), r'''
The source pushes $5\,\mathrm{A}$ up and into the top of $R_{eq}$ → $+$ on top, same as $v$:

$$
\boxed{v=(5)(8)=40\,\mathrm{V}}
$$

The $5\,\mathrm{A}$ leaves the source at its $+$ end → it delivers:

$$
\boxed{P=(40)(5)=200\,\mathrm{W}}
$$
'''),
    ('Back to $V_c$', j(BACK, '#= path 4.9,3 -> 8,3 -> 8,0.4 "$1.67\\,\\mathrm{A}$" thin',
                        '#= text 9.2,1.5 "$15\\,\\mathrm{V}$" color=pink', r'#+ $V_c=15\,\mathrm{V}$'), r'''
Go back one step: $40\,\mathrm{V}$ sits across the $15\,\Omega + 9\,\Omega$ path.

$$
i=\frac{40}{24}=\frac{5}{3}\,\mathrm{A}
$$

Ohm's law on the $9\,\Omega$ (from $c$ down to $b$):

$$
V_c=\left(\frac{5}{3}\right)(9)=15\,\mathrm{V}
$$
'''),
    ('(d) $i_o$', j(GIVEN, NODES, '#= text 9.2,1.5 "$15\\,\\mathrm{V}$" color=pink', r'#+ $i_o=1.5\,\mathrm{A}$'), r'''
$c$ is a real node of the **original** circuit, so $V_c=15\,\mathrm{V}$ there too.

$i_o$ runs down the $10\,\Omega$ from $c$ to $b$ (ground):

$$
\boxed{i_o=\frac{15}{10}=1.5\,\mathrm{A}}
$$

Why you needed the Y → Δ: the ratios $20:10$ and $10:15$ differ, so $c$ and $n$ sit at different voltages. The $30\,\Omega$ carries current and can't just be dropped.
'''),
]


NET = [('I', 'I1', '0', 'a', 5), ('R', 'RXAB', 'a', '0', 20), ('R', 'RXAC', 'a', 'c', 20), ('R', 'RXBC', 'c', '0', 10),
       ('R', 'RY1', 'a', 'n', 10), ('R', 'RY3', 'n', 'c', 30), ('R', 'RY2', 'n', '0', 15)]


def checks(check):
    els, _ = check(GIVEN)
    a, n = els['RY1']
    c = els['RY3'][1]
    assert els['I1'] == ('0', a) and els['RXAB'] == (a, '0') and els['RXAC'] == (a, c), els
    assert els['RXBC'] == (c, '0') and els['RY3'][0] == n and els['RY2'] == (n, '0'), els
    d, _ = check(DELTA)
    a2, c2 = d['RDB']
    assert d['RDC'] == (a2, '0') and d['RXAB'][0] == a2 and d['RXAC'] == (a2, c2), d
    assert d['RXBC'] == (c2, '0') and d['RDA'] == (c2, '0'), d
    for x in (SPOT, PAIRS, SERIES, LAST, BACK):
        check(x)
    R1, R2, R3 = 10, 15, 30
    S = R1 * R2 + R2 * R3 + R3 * R1
    assert (R1 * R2, R2 * R3, R3 * R1, S) == (150, 450, 300, 900)
    Ra, Rb, Rc = F(S, R1), F(S, R2), F(S, R3)
    assert (Ra, Rb, Rc) == (90, 60, 30)

    def par(x, y):
        return F(x * y, x + y)

    assert (par(20, Rc), par(20, Rb), par(10, Ra)) == (12, 15, 9)
    assert 15 + 9 == 24 and par(12, 24) == 8 == F(288, 36)
    assert 5 * 8 == 40 and 40 * 5 == 200
    assert F(40, 24) == F(5, 3) and F(5, 3) * 9 == 15 and F(15, 10) == F(3, 2)
    assert F(20, 10) != F(R1, R2)  # not balanced
    V, I, P = solve(NET)
    assert abs(V['a'] - 40) < 1e-9 and abs(V['c'] - 15) < 1e-9 and abs(I['RXBC'] - 1.5) < 1e-9
    assert abs(P['I1'] + 200) < 1e-9 and abs(I['RY3']) > 0.1, (P['I1'], I['RY3'])
