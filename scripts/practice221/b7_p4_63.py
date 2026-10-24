r"""Textbook P4.63: source transformations shrink the circuit to one loop for v_o; the source powers then need the
ORIGINAL circuit (a transformed source does not carry the original source's power). Uses three methods:
source transformation, mesh/KVL with the user's sign rule, and Ohm's law + KCL back in the original circuit.
Drawn 9.5 × 5 instead of 12 × 7: the 340 V source and the 80 Ω swap rows (same topology, asserted)."""
from fractions import Fraction as F

SECTION = 'B'
TITLE = 'Shrink it for one voltage, then go back for the powers'
SOURCE = 'Textbook P4.63'
CITES = [{"chunk_id": "b0340958-02ef-4cf3-a7c0-cbd0e26f0065", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1}]
PROMPT = (r'**(a)** Find $v_o$. **(b)** Find the power developed by the $340\,\mathrm{V}$ source and **(c)** by the '
          r'$5\,\mathrm{A}$ source. **(d)** Check the power balance.')

O = r'\,\Omega'


def j(*parts):
    return '\n'.join(parts)


I1 = r'I1 0,0 -> 0,3 "$5\,\mathrm{A}$"'
R1 = f'R1 0,3 -> 2.5,3 "$8{O}$"'
R2 = f'R2 2.5,3 -> 2.5,0 "$20{O}$"'
V1 = r'V1 2.5,3 -> 5,3 "$340\,\mathrm{V}$"'
R3 = j('wire 2.5,3 -> 2.5,5', f'R3 2.5,5 -> 5,5 "$80{O}$"', 'wire 5,5 -> 5,3')
RIGHT = j(f'R4 5,3 -> 7.5,3 "$5{O}$"', 'wire 7.5,3 -> 9.5,3', f'R5 9.5,3 -> 9.5,0 "$45{O}$"',
          'wire 0,0 -> 2.5,0', f'R6 2.5,0 -> 7.5,0 "$10{O}$"', 'wire 7.5,0 -> 9.5,0', 'gap 7.5,3 -> 7.5,0 v="$v_o$"',
          'label 2.5,3 "$q$" above', 'label 5,3 "$r$" below', 'label 7.5,0 "$m$" below', 'ground 0,0')
GIVEN = j(I1, R1, R2, V1, R3, RIGHT)

NO8 = j(I1, 'wire 0,3 -> 2.5,3', R2, V1, R3, RIGHT)
NO80 = j(I1, 'wire 0,3 -> 2.5,3', R2, V1, RIGHT)
LOOP = j(r'VS 0,3 -> 0,0 "$100\,\mathrm{V}$"', f'R2 0,3 -> 2.5,3 "$20{O}$"', V1, RIGHT)

MESH = '#= mesh 5,1.5 "$i$" cw r=0.6'
SIGNS = j('#= sign 0.4,2.65 +', '#= sign 2.1,2.65 -', '#= sign 5.4,2.65 +', '#= sign 7.1,2.65 -',
          '#= sign 9.15,2.6 +', '#= sign 9.15,0.4 -', '#= sign 7.1,0.35 +', '#= sign 2.9,0.35 -')
I_LOOP = r'#= text 5,0.55 "$i=-3\,\mathrm{A}$" color=purple'

STEPS = [
    ('The circuit', GIVEN, r'''
**Methods:** source transformations to shrink it to **one loop** for $v_o$, then KVL + Ohm's law back in the **original** circuit for the source powers.
'''),
    ('Drop the $8\\,\\Omega$', NO8, r'''
The $8\,\Omega$ is in **series with the $5\,\mathrm{A}$ source** → its current is $5\,\mathrm{A}$ no matter what.

It changes nothing else → leave it out for now (it still absorbs power: back in (d)).
'''),
    ('Drop the $80\\,\\Omega$', NO80, r'''
The $80\,\Omega$ is in **parallel with the $340\,\mathrm{V}$ source** → its voltage is $340\,\mathrm{V}$ no matter what.

It changes nothing else → leave it out for now.
'''),
    ('Current source → voltage source', LOOP, r'''
$5\,\mathrm{A}$ in **parallel** with $20\,\Omega$ → a voltage source in **series** with $20\,\Omega$:

$$
v=(5)(20)=100\,\mathrm{V}
$$

The current source pushed **up** → $+$ on **top**.
'''),
    ('KVL around the loop', j(LOOP, MESH, SIGNS, r'#+ $i=-3\,\mathrm{A}$'), r'''
One loop, clockwise $i$. Sign you **enter** each element by:
- $100\,\mathrm{V}$: enter $-$ → $-100$
- $20\,\Omega$: $+20i$
- $340\,\mathrm{V}$: enter $+$ → $+340$
- $5$, $45$, $10\,\Omega$: $+5i+45i+10i$

$$
-100+20i+340+60i=0
$$

$$
80i=-240 \;\Rightarrow\; i=-3\,\mathrm{A}
$$
'''),
    ("Ohm's law → $v_o$", j(LOOP, I_LOOP, '#= path 7.5,3 -> 9.5,3 -> 9.5,0 -> 7.75,0', r'#+ $v_o=-135\,\mathrm{V}$'), r'''
$v_o$ is across the $45\,\Omega$ ($+$ on top). Walk from $+$ to $-$ down the $45\,\Omega$, with $i$:

$$
\boxed{v_o=45i=45(-3)=-135\,\mathrm{V}}
$$
'''),
    ('Back to the original circuit', j(GIVEN, I_LOOP, '#= path 2.5,3 -> 9.5,3 -> 9.5,0 -> 2.85,0',
                                       r'#+ $V_q=160\,\mathrm{V}$'), r'''
The transformed $100\,\mathrm{V}$ source is **not** the $5\,\mathrm{A}$ source, and the dropped resistors still take power → the powers need the **original** circuit.

The $5$, $45$, $10\,\Omega$ were never touched → they still carry $i=-3\,\mathrm{A}$.

Walk from $q$ to ground (sign you enter by):

$$
V_q=340+5i+45i+10i=340-180=160\,\mathrm{V}
$$
'''),
    ('Power of the $340\\,\\mathrm{V}$ source', j(GIVEN, I_LOOP, r'#= text 3.75,5.55 "$4.25\,\mathrm{A}$" color=orange',
                                                  r'#= text 3.75,2.25 "$7.25\,\mathrm{A}$" color=green',
                                                  r'#+ $p_{340}=2465\,\mathrm{W}$'), r'''
$80\,\Omega$ (Ohm): $\dfrac{340}{80}=4.25\,\mathrm{A}$ from $q$ to $r$.

The pair together carries $i=-3\,\mathrm{A}$ from $q$ to $r$ (KCL):

$$
i_{340}=-3-4.25=-7.25\,\mathrm{A}\ (q\to r)
$$

So $7.25\,\mathrm{A}$ flows $r\to q$ through the source: out of its $+$ → it **delivers**

$$
\boxed{p_{340}=(340)(7.25)=2465\,\mathrm{W}}
$$
'''),
    ('Power of the $5\\,\\mathrm{A}$ source', j(GIVEN, '#= path 0,3 -> 2.5,3 -> 2.5,0.4', r'#= text 1.25,3.6 "$40\,\mathrm{V}$" color=pink',
                                                r'#= text 3.35,1.5 "$160\,\mathrm{V}$" color=pink', r'#+ $p_{5A}=1000\,\mathrm{W}$'), r'''
Ohm's law: the $20\,\Omega$ carries $\dfrac{160}{20}=8\,\mathrm{A}$ down; the $8\,\Omega$ carries $5\,\mathrm{A}$.

Walk from the top of the source to ground:

$$
v_{5A}=(5)(8)+160=200\,\mathrm{V}
$$

Current leaves its top ($+$) → it **delivers**

$$
\boxed{p_{5A}=(200)(5)=1000\,\mathrm{W}}
$$
'''),
    ('Power balance', j(GIVEN, r'#= text 1.25,2.35 "$200\,\mathrm{W}$" color=orange', r'#= text 1.8,1.5 "$1280\,\mathrm{W}$" color=orange',
                        r'#= text 3.75,4.45 "$1445\,\mathrm{W}$" color=orange', r'#= text 6.25,3.6 "$45\,\mathrm{W}$" color=orange',
                        r'#= text 8.6,1.5 "$405\,\mathrm{W}$" color=orange', r'#= text 5,-0.6 "$90\,\mathrm{W}$" color=orange'), r'''
**Delivered:** $2465+1000=3465\,\mathrm{W}$

**Absorbed** ($i^2R$):
- $8\,\Omega$: $5^2(8)=200$
- $20\,\Omega$: $8^2(20)=1280$
- $80\,\Omega$: $4.25^2(80)=1445$
- $5\,\Omega$, $45\,\Omega$, $10\,\Omega$: $3^2(5)=45$, $3^2(45)=405$, $3^2(10)=90$

$$
\boxed{200+1280+1445+45+405+90=3465\,\mathrm{W}}
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
    p, q = els['R1']
    r, n = els['R4']
    assert els['I1'] == ('0', p) and els['R2'] == (q, '0') and els['V1'] == (q, r) and els['R3'] == (q, r), els
    m = els['R6'][1]
    assert els['R5'] == (n, m) and els['R6'] == ('0', m), els
    lels, _ = check(LOOP)
    assert lels['VS'][1] == '0' and lels['R2'][0] == lels['VS'][0] and lels['V1'][0] == lels['R2'][1], lels
    V, I, P = _mna().solve([('I', 'I1', '0', 'p', 5), ('R', 'R1', 'p', 'q', 8), ('R', 'R2', 'q', '0', 20),
                            ('V', 'V1', 'q', 'r', 340), ('R', 'R3', 'q', 'r', 80), ('R', 'R4', 'r', 'n', 5),
                            ('R', 'R5', 'n', 'm', 45), ('R', 'R6', '0', 'm', 10)])
    assert abs((V['n'] - V['m']) - (-135)) < 1e-9 and abs(V['q'] - 160) < 1e-9 and abs(V['p'] - 200) < 1e-9
    assert abs(-P['V1'] - 2465) < 1e-6 and abs(-P['I1'] - 1000) < 1e-6
    absorbed = [P[k] for k in ('R1', 'R2', 'R3', 'R4', 'R5', 'R6')]
    assert [round(x, 6) for x in absorbed] == [200, 1280, 1445, 45, 405, 90]
    # the arithmetic in the notes
    assert 5 * 20 == 100
    i = F(-240, 80)
    assert i == -3 and -100 + 20 * i + 340 + 60 * i == 0 and 45 * i == -135
    assert 340 + 60 * i == 160 and F(340, 80) == F(425, 100) and -3 - F(425, 100) == F(-725, 100)
    assert 340 * F(725, 100) == 2465 and F(160, 20) == 8 and 5 * 8 + 160 == 200 and 200 * 5 == 1000
    assert 25 * 8 == 200 and 64 * 20 == 1280 and F(425, 100) ** 2 * 80 == 1445 and (9 * 5, 9 * 45, 9 * 10) == (45, 405, 90)
    assert 200 + 1280 + 1445 + 45 + 405 + 90 == 3465 == 2465 + 1000
