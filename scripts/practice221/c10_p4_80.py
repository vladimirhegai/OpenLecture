r"""Textbook P4.80: Thévenin at a-b of a network with only a dependent source (V_Th = 0, R_Th by a 1 V test source).

With the test voltage fixing a and the dependent source fixing x = 10 i_D, only node m is unknown,
so one KCL at m (user's nodal convention) does it.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'height_notes'))
from mna import solve  # noqa: E402

SECTION = 'C'
TITLE = 'Thévenin: only a dependent source'
SOURCE = 'Textbook P4.80'
CITES = [{"chunk_id": "11bd02ab-ca60-4fbc-9f85-243a3e08a576", "source_id": "36da61a3-f7f4-45f0-bf0d-37ed16959f48", "version": 1}]
PROMPT = r'Find the Thévenin equivalent at $a$–$b$. The dependent source is controlled by $i_\Delta$ in the $12\,\Omega$.'

O = r'\,\Omega'
BASE = '\n'.join([
    'E1 0,3 -> 0,0 "$10i_\\Delta$"',
    'wire 0,3 -> 0,5',
    f'R1 0,5 -> 8,5 "$6{O}$"',
    'wire 8,5 -> 8,3',
    f'R2 0,3 -> 4,3 "$10{O}$"',
    f'R3 8,3 -> 4,3 "$12{O}$" i="$i_\\Delta$"',
    f'R4 4,3 -> 4,0 "$2.5{O}$"',
    'wire 8,3 -> 10,3',
    'wire 0,0 -> 10,0',
    'terminal 10,3 "$a$" right',
    'terminal 10,0 "$b$" right',
    'label 0,3 "$x$" left',
    'label 4,3 "$m$" above',
    'ground 0,0',
])
GIVEN = BASE
TEST = BASE + '\nV9 10,3 -> 10,0 "$1\\,\\mathrm{V}$"'
NODE_M = '#= region 3.55,2.55 4.45,3.45 color=green'


def j(*parts):
    return '\n'.join(parts)


STEPS = [
    ('The circuit', GIVEN, r'''
No independent source: only $10i_\Delta$, controlled by $i_\Delta$ in the $12\,\Omega$.

**Plan**
1. $V_{Th}$.
2. $R_{Th}$ with a test source.
'''),
    ('$V_{Th}=0$', j(GIVEN, '#= text 11,1.5 "$V_{oc}=0$" color=pink', r'#+ $V_{Th}=0$'), r'''
Nothing drives this circuit. With $a$–$b$ open every current is $0$, so $i_\Delta=0$ and the dependent source is $0$ too.

$$
V_{Th}=0
$$
'''),
    ('Test source', TEST, r'''
Put $1\,\mathrm{V}$ across $a$–$b$ and find the current $i_T$ it pushes in.

The dependent source **stays on**: the test source makes $i_\Delta$ flow, so it wakes up.

$$
R_{Th}=\frac{1\,\mathrm{V}}{i_T}
$$
'''),
    ('What we know', j(TEST, '#= text 1,4.15 "$V_x=10i_\\Delta$" color=pink'), r'''
- $V_a=1\,\mathrm{V}$ (the test source).
- $V_x=10i_\Delta$ (the dependent source, $+$ on top, bottom at ground).
- $V_m$: the only unknown node.

Ohm on the $12\,\Omega$ (start − end, $a$ → $m$):

$$
i_\Delta=\frac{1-V_m}{12} \;\Rightarrow\; V_m=1-12i_\Delta
$$
'''),
    ('KCL at $m$', j(TEST, '#= text 1,4.15 "$V_x=10i_\\Delta$" color=pink', NODE_M, r'#+ $i_\Delta=62.5\,\mathrm{mA}$'), r'''
Entering $+$, leaving $-$:
- from $a$ (12 Ω): $+i_\Delta$
- from $x$ (10 Ω): $+\dfrac{V_x-V_m}{10}$
- down the 2.5 Ω: $-\dfrac{V_m}{2.5}$

$$
i_\Delta+\frac{10i_\Delta-(1-12i_\Delta)}{10}-\frac{1-12i_\Delta}{2.5}=0
$$

Multiply by $10$:

$$
10i_\Delta+22i_\Delta-1-4+48i_\Delta=0 \;\Rightarrow\; 80i_\Delta=5
$$

$$
i_\Delta=\tfrac{1}{16}\,\mathrm{A}=62.5\,\mathrm{mA}
$$
'''),
    ('Node voltages', j(TEST, NODE_M, '#= text 1,4.15 "$0.625\\,\\mathrm{V}$" color=pink',
                        '#= text 5,3.85 "$0.25\\,\\mathrm{V}$" color=pink'), r'''
$$
V_m=1-12\left(\tfrac{1}{16}\right)=0.25\,\mathrm{V}
$$

$$
V_x=10\left(\tfrac{1}{16}\right)=0.625\,\mathrm{V}
$$
'''),
    ('Test current', j(TEST, '#= text 1,4.15 "$0.625\\,\\mathrm{V}$" color=pink',
                       '#= text 5,3.85 "$0.25\\,\\mathrm{V}$" color=pink', r'#+ $R_{Th}=8\,\Omega$'), r'''
$i_T$ enters $a$ and leaves through the $6\,\Omega$ and the $12\,\Omega$:

$$
i_T=\frac{1-0.625}{6}+\frac{1}{16}=0.0625+0.0625=0.125\,\mathrm{A}
$$

$$
R_{Th}=\frac{1}{0.125}=8\,\Omega
$$
'''),
    ('Thévenin circuit', j(f'R7 8,3 -> 8,0 "$8{O}$"', 'wire 8,3 -> 10,3', 'wire 8,0 -> 10,0',
                           'terminal 10,3 "$a$" right', 'terminal 10,0 "$b$" right'), r'''
$V_{Th}=0$, so the source is just a wire:

$$
\boxed{V_{Th}=0,\quad R_{Th}=8\,\Omega}
$$

From outside, $a$–$b$ looks like a plain $8\,\Omega$ resistor.
'''),
]


def checks(check):
    els, _ = check(GIVEN)
    x, m, a = els['E1'][0], els['R2'][1], els['R3'][0]
    assert els['E1'][1] == '0' and els['R4'] == (m, '0'), els
    assert els['R1'] == (x, a) and els['R2'] == (x, m) and els['R3'] == (a, m), els
    # 1 V test: i_D = (Va - Vm)/12, E1: Vx = 10 i_D
    V, I, _ = solve([('E', 'E1', 'x', '0', {'a': 10 / 12, 'm': -10 / 12}, 0), ('R', 'R1', 'x', 'a', 6),
                     ('R', 'R2', 'x', 'm', 10), ('R', 'R3', 'a', 'm', 12), ('R', 'R4', 'm', '0', 2.5),
                     ('V', 'VT', 'a', '0', 1)])
    iD = I['R3']
    assert abs(iD - 1 / 16) < 1e-12 and abs(V['m'] - 0.25) < 1e-12 and abs(V['x'] - 0.625) < 1e-12
    assert abs(-I['VT'] - 0.125) < 1e-12
    # the hand algebra
    d = 1 / 16
    assert abs(d + (10 * d - (1 - 12 * d)) / 10 - (1 - 12 * d) / 2.5) < 1e-12
    assert 10 + 22 + 48 == 80 and -1 - 4 == -5 and 5 / 80 == d == 0.0625
    assert 1 - 12 * d == 0.25 and 10 * d == 0.625
    assert (1 - 0.625) / 6 == 0.0625 and 0.0625 + 0.0625 == 0.125 and 1 / 0.125 == 8
