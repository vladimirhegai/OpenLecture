"""Week 6, v3 layout: two topics (C and L at DC; switching with three snapshots), height pictures for every circuit.

Snapshot rules: at DC a capacitor is a gap and an inductor is a wire. Right after a switch, a capacitor is a battery
holding its old voltage and an inductor is a pump holding its old current. Old prompts/steps are reused from w6_now.json.
"""
import copy
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import circuits6 as c6  # noqa: E402
from blocks45 import Doc, S  # noqa: E402
from w45lib import C, view, fence  # noqa: E402
from weekkit import card  # noqa: E402

D = Doc('w6-v3', 6, 'w6_now.json')
H, P, CO, L, T, EQ, SCH, PR = D.H, D.P, D.CO, D.L, D.T, D.EQ, D.SCH, D.PR
TB = {}
for f in ('tb6.json', 'tb7.json'):
    TB.update({p['number']: p['citation'] for p in json.load(open(os.path.join(HERE, 'w45', f), encoding='utf-8'))})
tb = lambda n: [TB[n]]  # noqa: E731
E1 = math.exp(-1)


def EX(key, title, intro, fig, steps, answer, cites=(), after=''):
    """Worked examples show their height picture in the page."""
    if '#@ inline' not in fig:
        fig = fig.replace('\n#@ spoiler', '\n#@ inline', 1)
    D.EX(key, title, intro, fig, steps, answer, cites, after)


def split(prompt):
    """An old prompt around its schematic fence: (intro, after)."""
    m = re.search(r'```schematic\n.*?\n```', prompt, re.S)
    return prompt[:m.start()].rstrip(), prompt[m.end():].lstrip()


def reuse(prefix, title, kind=None, diff=None):
    """Copy an old block (prompt, steps, answer, citations) under a new title."""
    b = copy.deepcopy(D.ob(prefix))
    b['title'] = title
    b['id'] = D.nid('r' + prefix)
    if diff:
        b['difficulty'] = diff
    D.B.append(b)


def ob_steps(prefix, skip=()):
    return [s for i, s in enumerate(D.ob(prefix)['steps']) if i not in skip]


WIRE_DC = ('L', r'$L$ at DC: a wire')
CLOSED = ('W', 'switch closed')
gapC = lambda v: ('C', rf'$C$ at DC: a gap, holds ${v}\,\mathrm{{V}}$')  # noqa: E731
holdC = lambda v: ('C', rf'$C$ holds ${v}\,\mathrm{{V}}$')  # noqa: E731
holdL = lambda i: ('L', rf'$L$ holds ${i}\,\mathrm{{A}}$')  # noqa: E731
drop = lambda net, *names: [e for e in net if e[1] not in names]  # noqa: E731


def ren(net, old, new):
    return [e[:2] + tuple(new if x == old else x for x in e[2:4]) + e[4:] for e in net]


card(D, "**Week 6 in one line:** two new parts that **remember**. A capacitor remembers its **voltage** (a height step), "
        "an inductor remembers its **current** (a flow). Topic 1: what they do at DC. Topic 2: what happens when a switch flips.",
     "at DC a capacitor is a **gap** and an inductor is a **wire**. Right after a switch, a capacitor is a **battery** holding "
     "its old step and an inductor is a **pump** holding its old current.")

# ================================================================ Topic 1
H(1, 'Topic 1: Capacitors and inductors')
CO('tip', "**How it looks in heights.**\n\n"
          "- **Capacitor** $C$: a height step that can't jump. $i=C\\dfrac{dv}{dt}$. At DC nothing changes, so $i=0$: a **gap**. "
          "It still sits across its two heights and stores $w=\\tfrac12Cv^2$.\n"
          "- **Inductor** $L$: a flow that can't jump. $v=L\\dfrac{di}{dt}$. At DC nothing changes, so $v=0$: a **wire** (no step). "
          "It still carries its current and stores $w=\\tfrac12Li^2$.\n"
          "- **Combining:** $L$ adds like $R$ (series adds). $C$ adds like $\\tfrac1R$ (parallel adds, series uses reciprocals).")
T(['', 'Capacitor', 'Inductor'], [
    ['Law', '$i=C\\,\\dfrac{dv}{dt}$', '$v=L\\,\\dfrac{di}{dt}$'],
    ['Other way round', '$v=\\dfrac1C\\displaystyle\\int i\\,dt+v(t_0)$', '$i=\\dfrac1L\\displaystyle\\int v\\,dt+i(t_0)$'],
    ['Energy', '$\\tfrac12Cv^2$', '$\\tfrac12Li^2$'],
    ['At DC (settled)', 'gap: $i=0$', 'wire: $v=0$'],
    ['Can\'t jump', 'its voltage $v_C$', 'its current $i_L$'],
    ['Series', '$\\dfrac1{C_{eq}}=\\sum\\dfrac1{C_k}$', '$L_{eq}=\\sum L_k$'],
    ['Parallel', '$C_{eq}=\\sum C_k$', '$\\dfrac1{L_{eq}}=\\sum\\dfrac1{L_k}$'],
])

n = C['dc1']['net']
EX('dc1', 'Example 1 · Settled circuit: gap and wire',
   r'The circuit has been on for a long time. Find $i_L$, $v_C$ and the energy in each part.',
   fence('dc1', [view(n, [('V1', 0), ('R1', 1), ('L1', 1), ('R2', 2), ('C1', 3)], title='Settled (DC)',
                      names={'s': 'source top', 'a': '$a$', 'b': '$b$', '0': 'bottom'},
                      disp={'L1': WIRE_DC, 'C1': gapC(8)}, steps=[
       (r"Ground the bottom. The battery lifts the top to $12\,\mathrm{V}$.", ['s', 'eV1']),
       (r"$L$ is a wire, so $a=b$. $C$ is a gap, so no current goes that way. One loop: $2+4=6\,\Omega$, $i=\dfrac{12}{6}=2\,\mathrm{A}$.", ['a', 'b', 'eR1', 'eL1', 'eR2']),
       (r"$b$ sits $2\times4=8\,\mathrm{V}$ up, so the capacitor holds $v_C=8\,\mathrm{V}$.", ['eC1']),
   ])], spoiler=False, inline=True),
   [S('DC: $L$ a wire, $C$ a gap.', r'i_L=\frac{12}{2+4}=2\,\mathrm{A},\qquad v_C=2\cdot4=8\,\mathrm{V}'),
    S('Energy.', r'w_L=\tfrac12(0.5)(2)^2=1\,\mathrm{J},\qquad w_C=\tfrac12(100\times10^{-6})(8)^2=3.2\,\mathrm{mJ}')],
   r'$i_L=2\,\mathrm{A}$, $v_C=8\,\mathrm{V}$, $w_L=1\,\mathrm{J}$, $w_C=3.2\,\mathrm{mJ}$.')

reuse('Lecture example: inductor driven', r'Example 2 · $v=L\,\frac{di}{dt}$ on a real current (Lecture 6)')
reuse('Lecture example: three inductors in series', 'Example 3 · Series inductors add (Lecture 6)')
reuse('Lecture example: three inductors in parallel', 'Example 4 · Parallel inductors, with starting currents (Lecture 6)')
reuse('Lecture example: three capacitors in series', 'Example 5 · Series capacitors (Lecture 6)')

n = C['dc2']['net']
PR('dc2', 'Try it 1 · A pump, a gap and a wire', 'introductory',
   r'The circuit has been on for a long time. Find $i_L$, $v_C$, $w_L$ and $w_C$.',
   fence('dc2', [view(n, [('I1', 0), ('C1', 1), ('R1', 2), ('L1', 2), ('R2', 3)], title='Settled (DC)',
                      names={'a': '$a$', 'b': '$b$', '0': 'bottom'}, disp={'L1': WIRE_DC, 'C1': gapC(12)}, steps=[
       (r"Ground the bottom. The pump lifts $5\,\mathrm{A}$ to the top wire.", ['eI1']),
       (r"$L$ is a wire, so $a=b$: the $4\,\Omega$ and $6\,\Omega$ hang side by side ($2.4\,\Omega$). Height $=5\times2.4=12\,\mathrm{V}$.", ['a', 'b', 'eR1', 'eL1', 'eR2']),
       (r"Split: $\dfrac{12}{4}=3\,\mathrm{A}$, $\dfrac{12}{6}=2\,\mathrm{A}$ through the inductor. $C$ holds $12\,\mathrm{V}$.", ['eC1']),
   ])]),
   [S('DC: $C$ a gap, $L$ a wire.', r'v=5\,(4\parallel6)=12\,\mathrm{V},\qquad i_L=\frac{12}{6}=2\,\mathrm{A},\qquad v_C=12\,\mathrm{V}'),
    S('Energy.', r'w_L=\tfrac12(2\times10^{-3})(2)^2=4\,\mathrm{mJ},\qquad w_C=\tfrac12(10\times10^{-6})(12)^2=0.72\,\mathrm{mJ}')],
   r'$i_L=2\,\mathrm{A}$, $v_C=12\,\mathrm{V}$, $w_L=4\,\mathrm{mJ}$, $w_C=0.72\,\mathrm{mJ}$.', [])

reuse('Textbook P6.15', 'Try it 2 · Capacitor voltage, power, energy (Textbook P6.15)')
reuse('Textbook P6.2 ', 'Try it 3 · Inductor voltage, power, energy (Textbook P6.2)')
reuse('Textbook P6.25', 'Try it 4 · Parallel inductors and trapped energy (Textbook P6.25)')

# ================================================================ Topic 2
H(1, 'Topic 2: Switching: three snapshots')
CO('tip', "**How it looks in heights.** Draw three height pictures, then connect them with one slide.\n\n"
          "- **$0^-$ (old circuit, settled):** $C$ a gap, $L$ a wire. Read off $v_C$ or $i_L$.\n"
          "- **$0^+$ (new circuit, one instant later):** $C$ is a **battery** holding that $v_C$; $L$ is a **pump** holding that $i_L$. "
          "Everything else can jump.\n"
          "- **$\\infty$ (new circuit, settled):** $C$ a gap, $L$ a wire again.\n"
          "- **The slide between them:** one time constant $\\tau=R_{\\mathrm{Th}}C$ or $\\tau=\\dfrac{L}{R_{\\mathrm{Th}}}$, "
          "with $R_{\\mathrm{Th}}$ = what $C$ or $L$ sees with the sources off. (Lecture slide 62 prints $\\tfrac RL$: a typo.)")
EQ(r'x(t)=x(\infty)+\big[x(0^+)-x(\infty)\big]\,e^{-t/\tau}')
T(['Time', '$e^{-t/\\tau}$', 'How far it has gone'], [
    ['$\\tau$', '$0.368$', '$63\\%$'],
    ['$2\\tau$', '$0.135$', '$86\\%$'],
    ['$3\\tau$', '$0.050$', '$95\\%$'],
    ['$5\\tau$', '$0.007$', '$99\\%$ (call it done)'],
])

nm = {'s': 'source top', 'p': '$p$', 'n': '$n$', '0': 'bottom'}
EX('rc1', 'Example 6 · A capacitor charges',
   r'The capacitor is empty and the switch closes at $t=0$. Find $v_C(t)$.',
   fence('rc1', [
       view(c6.rc1(0), [('V1', 0), ('S1', 0), ('R1', 1), ('C1', 2)], title='0+', unit='mA', names=nm,
            disp={'S1': CLOSED, 'C1': holdC(0)}, steps=[
           (r"Ground the bottom. Empty capacitor: a $0\,\mathrm{V}$ battery, so $n$ starts on the floor.", ['n', 'eC1']),
           (r"The whole $10\,\mathrm{V}$ falls across the $2\,\mathrm{k\Omega}$: $i=5\,\mathrm{mA}$, the biggest it gets.", ['s', 'p', 'eV1', 'eS1', 'eR1']),
       ]),
       view(c6.rc1(10 * (1 - E1)), [('V1', 0), ('S1', 0), ('R1', 1), ('C1', 2)], title='t = tau', unit='mA', names=nm,
            disp={'S1': CLOSED, 'C1': holdC('6.32')}, steps=[
           (r"Same ground. After one $\tau=RC=2\,\mathrm{ms}$, $n$ has climbed $63\%$ of the way: $6.32\,\mathrm{V}$. Less fall, less current.", ['n', 'eC1', 'eR1']),
       ]),
       view(c6.rc1(10), [('V1', 0), ('S1', 0), ('R1', 1)], title='Settled', unit='mA', names=nm, disp={'S1': CLOSED},
            notes=[r"Settled: the capacitor is a gap again (no current), so it is left out; it holds $10\,\mathrm{V}$."], steps=[
           (r"Same ground. $n$ reaches the top: no fall, no current. $v_C(\infty)=10\,\mathrm{V}$.", ['n', 'eR1']),
       ]),
   ], spoiler=False, inline=True),
   [S('Snapshots.', r'v_C(0^+)=0,\qquad v_C(\infty)=10\,\mathrm{V},\qquad \tau=RC=(2000)(10^{-6})=2\,\mathrm{ms}'),
    S('One slide between them.', r'v_C(t)=10+(0-10)e^{-500t}=10\left(1-e^{-500t}\right)\,\mathrm{V}')],
   r'$v_C(t)=10\left(1-e^{-500t}\right)\,\mathrm{V}$, $\tau=2\,\mathrm{ms}$.')

old = D.ob('Lecture example: RL step response')
intro, after = split(old['prompt'])
nm = {'s': 'source top', 'b': '$b$', 'x': '$x$', '0': 'bottom'}
cols = [('V1', 0), ('R1', 1), ('S1', 1), ('L1', 2)]
EX('lecrl', 'Example 7 · An inductor current reverses (Lecture 6)', intro,
   fence('lecrl', [
       view(c6.lecrl(-8), cols, title='0+', names=nm, disp={'S1': CLOSED, 'L1': holdL(-8)},
            refs={'L1': ('x', '$v$')}, notes=[r"Only the left loop matters now; the right part is cut off by switch $a$."], steps=[
           (r"$0^-$: the inductor is a wire, so it shorts the $8\,\mathrm{A}$ pump. All $8\,\mathrm{A}$ goes **up** through it: $i(0^-)=-8\,\mathrm{A}$ (against the arrow).", []),
           (r"$0^+$: ground the bottom. The inductor is now a pump still pushing $8\,\mathrm{A}$ up.", ['eL1']),
           (r"Those $8\,\mathrm{A}$ must slide down the $2\,\Omega$ into the battery: $b$ sits $16\,\mathrm{V}$ **above** the $24\,\mathrm{V}$ top. $v(0^+)=40\,\mathrm{V}$.", ['s', 'b', 'x', 'eR1', 'eS1', 'eV1']),
       ]),
       view(c6.lecrl(12 - 20 * E1), cols, title='t = tau', names=nm, disp={'S1': CLOSED, 'L1': holdL('4.64')},
            refs={'L1': ('x', '$v$')}, steps=[
           (r"Same ground. After $\tau=\dfrac{L}{R}=\dfrac{0.2}{2}=0.1\,\mathrm{s}$ the current has turned round: $12-20(0.368)=4.64\,\mathrm{A}$ down. $x$ is now below the top.", ['x', 'eL1', 'eR1']),
       ]),
       view(drop(ren(c6.lecrl(12), 'b', 'x'), 'S1'), [('V1', 0), ('R1', 1), ('L1', 1)], title='Settled', names=nm,
            disp={'L1': WIRE_DC}, refs={'L1': ('x', '$v$')}, steps=[
           (r"Same ground. The inductor is a wire: $x$ on the floor, the $2\,\Omega$ falls all $24\,\mathrm{V}$: $i(\infty)=12\,\mathrm{A}$, $v=0$.", ['x', 'eR1', 'eL1']),
       ]),
   ], spoiler=False, inline=True),
   [S(r'$0^-$: the wire shorts the pump; the current is held.', r'i(0^+)=i(0^-)=-8\,\mathrm{A}'),
    S(r'$\infty$ and $\tau$.', r'i(\infty)=\frac{24}{2}=12\,\mathrm{A},\qquad \tau=\frac{0.2}{2}=0.1\,\mathrm{s}'),
    S('One slide.', r'i(t)=12+(-8-12)e^{-10t}=12-20e^{-10t}\,\mathrm{A}'),
    S(r'Voltage (matches the $0^+$ picture).', r'v=0.2\,\frac{di}{dt}=40e^{-10t}\,\mathrm{V},\qquad v(0^+)=24-2(-8)=40\,\mathrm{V}'),
    S(r'When is $v=24\,\mathrm{V}$?', r'40e^{-10t}=24\;\Rightarrow\;t=\frac{\ln(5/3)}{10}\approx51.1\,\mathrm{ms}')],
   old['answer'], old['citations'], after)

# ---- Try its
old = D.ob('Textbook P7.1 ')
intro, after = split(old['prompt'])
n0 = drop(ren(C['p71']['net'], 'q', 'r'), 'R4', 'S1')
nm = {'s': 'source top', 'p': '$p$', 'q': '$q$', 'r': '$r$', '0': 'bottom'}
PR('p71', 'Try it 5 · An inductor lets go (Textbook P7.1)', 'intermediate', intro,
   fence('p71', [
       view(n0, [('V1', 0), ('R1', 1), ('R2', 2), ('R3', 3), ('L1', 3)], title='0-', names=nm,
            disp={'L1': WIRE_DC},
            notes=[r"The $2\,\Omega$ sits across the inductor wire (no fall, no current), so it is left out of this tab."], steps=[
           (r"Ground the bottom. Switch closed and the inductor is a wire, so $r$ sits on the floor.", ['r', 'eL1']),
           (r"$30\parallel6=5\,\Omega$; $\dfrac{120}{3+5}=15\,\mathrm{A}$; $p=120-45=75\,\mathrm{V}$. The $6\,\Omega$ drops $\dfrac{75}{6}=12.5\,\mathrm{A}$ down the inductor: $i(0^-)=-12.5\,\mathrm{A}$.", ['p', 'eR1', 'eR2', 'eR3']),
       ]),
       view(c6.p71(-12.5), [('L1', 0), ('R4', 1)], title='0+', gnd='low', names=nm, disp={'L1': holdL(-12.5)}, steps=[
           (r"Switch open: only the inductor and the $2\,\Omega$ are left. The inductor keeps pushing $12.5\,\mathrm{A}$ down through itself, so the same $12.5\,\mathrm{A}$ must flow round through the $2\,\Omega$.", []),
           (r"Ground the lowest wire, $r$. The $2\,\Omega$ falls $12.5\times2=25\,\mathrm{V}$ from the bottom wire to $r$.", ['z0', 'eR4', 'eL1']),
       ]),
       view(c6.p71(-12.5 * E1), [('L1', 0), ('R4', 1)], title='t = tau', gnd='low', names=nm, disp={'L1': holdL('4.6')}, steps=[
           (r"Same ground. $\tau=\dfrac{8\,\mathrm{mH}}{2\,\Omega}=4\,\mathrm{ms}$: the current is down to $37\%$, $4.6\,\mathrm{A}$.", ['z0', 'eR4', 'eL1']),
       ]),
   ]),
   old['steps'], old['answer'], old['citations'], after)

old = D.ob('Textbook P7.22')
intro, after = split(old['prompt'])
nm = {'p': '$p$', 'q': '$q$', 'r': '$r$', '0': 'bottom'}
PR('p722', 'Try it 6 · A capacitor lets go (Textbook P7.22)', 'intermediate', intro,
   fence('p722', [
       view(C['p722']['net'], [('I1', 0), ('R1', 1), ('R2', 2), ('S1', 2), ('C1', 3), ('R3', 4)], title='0-', unit='mA', names=nm,
            disp={'S1': CLOSED, 'C1': gapC(200)}, steps=[
           (r"Ground the bottom. $C$ is a gap. The pump's $7.5\,\mathrm{mA}$ splits: $80\,\mathrm{k\Omega}$ vs $20+50=70\,\mathrm{k\Omega}$.", ['eI1', 'eR1']),
           (r"$4\,\mathrm{mA}$ goes right; the $50\,\mathrm{k\Omega}$ falls $200\,\mathrm{V}$. $v(0^-)=200\,\mathrm{V}$.", ['p', 'q', 'r', 'eR2', 'eS1', 'eR3', 'eC1']),
       ]),
       view(c6.p722(200), [('C1', 0), ('R3', 1)], title='0+', unit='mA', names=nm, disp={'C1': holdC(200)}, steps=[
           (r"Switch open: only $C$ and the $50\,\mathrm{k\Omega}$. Ground the bottom. $C$ is a $200\,\mathrm{V}$ battery: $4\,\mathrm{mA}$ slides down.", ['r', 'eC1', 'eR3']),
       ]),
       view(c6.p722(200 * E1), [('C1', 0), ('R3', 1)], title='t = tau', unit='mA', names=nm, disp={'C1': holdC('73.6')}, steps=[
           (r"Same ground. $\tau=RC=50\,\mathrm{k}\times0.4\,\mu=20\,\mathrm{ms}$: $200\times0.368=73.6\,\mathrm{V}$ left.", ['r', 'eC1', 'eR3']),
       ]),
   ]),
   old['steps'], old['answer'], old['citations'], after)

nm = {'s': 'source top', 'p': '$p$', 'n': '$n$', '0': 'bottom'}
PR('p723', 'Try it 7 · Find the start, then let go (Textbook P7.23)', 'introductory',
   r'The switch has been closed for a long time and opens at $t=0$. Find $v_o(t)$ for $t\ge0$.',
   fence('p723', [
       view(C['p723']['net'], [('V1', 0), ('R1', 1), ('S1', 1), ('C1', 2), ('R2', 3)], title='0-', unit='mA', names=nm,
            disp={'S1': CLOSED, 'C1': gapC(15)}, steps=[
           (r"Ground the bottom. $C$ is a gap: a divider, $60\times\dfrac{25}{100}=15\,\mathrm{V}$.", ['s', 'p', 'n', 'eV1', 'eR1', 'eS1', 'eR2', 'eC1']),
       ]),
       view(c6.p723(15), [('C1', 0), ('R2', 1)], title='0+', unit='mA', names=nm, disp={'C1': holdC(15)}, steps=[
           (r"Switch open. $C$ holds $15\,\mathrm{V}$ and drains through $25\,\mathrm{k\Omega}$: $0.6\,\mathrm{mA}$. $\tau=25\,\mathrm{k}\times5\,\mathrm{n}=125\,\mu\mathrm{s}$.", ['n', 'eC1', 'eR2']),
       ]),
   ]),
   [S(r'$0^-$: divider.', r'v_o(0^-)=60\cdot\frac{25}{75+25}=15\,\mathrm{V}'),
    S('After: only the $25\\,\\mathrm{k\\Omega}$.', r'\tau=(25\times10^{3})(5\times10^{-9})=125\,\mu\mathrm{s},\quad \frac1\tau=8000\,\mathrm{s}^{-1}'),
    S('Let go (ends at 0).', r'v_o(t)=15e^{-8000t}\,\mathrm{V}')],
   r'$v_o(t)=15e^{-8000t}\,\mathrm{V}$ for $t\ge0$.', tb('7.23'))

# ================================================================ Practice set
H(1, 'Practice set')
P('Full switching problems: three snapshots, then one slide. Try each before opening the pictures.')

old = D.ob('Lecture 6 example · RC step')
intro, after = split(old['prompt'])
n0 = [e for e in C['lecrc']['net'] if e[1] in ('V1', 'R1', 'R2', 'S1', 'C1')]
nm = {'s': 'source top', 'p': '$p$', 'x': '$x$', 'y': '$y$', 'c': '$c$', 'd': '$d$', '0': 'bottom'}
c2 = [('V2', 0), ('R5', 1), ('R4', 2), ('R3', 3), ('S2', 3), ('C1', 4)]
PR('lecrc', 'Lecture 6 · Two-position switch (RC)', 'advanced', intro,
   fence('lecrc', [
       view(n0, [('V1', 0), ('R1', 1), ('R2', 2), ('S1', 2), ('C1', 3)], title='0-', unit='mA', names=nm,
            disp={'S1': CLOSED, 'C1': gapC(30)}, steps=[
           (r"Ground the bottom. Position 1: $C$ a gap across the $60\,\mathrm{k\Omega}$ of a divider: $40\times\dfrac{60}{80}=30\,\mathrm{V}$.", ['s', 'p', 'x', 'eR1', 'eR2', 'eC1']),
       ]),
       view(c6.lecrc(30), c2, title='0+', unit='mA', gnd='low', names=nm, disp={'S2': CLOSED, 'C1': holdC(30)}, steps=[
           (r"Position 2. Ground the lowest wire, $d$: the $75\,\mathrm{V}$ battery puts the bottom wire $75\,\mathrm{V}$ above it.", ['z0', 'eV2']),
           (r"$C$ is a $30\,\mathrm{V}$ battery: $x=75+30=105$. In = out at $c$ gives $c=87$ (i.e. $12\,\mathrm{V}$ above the bottom).", ['x', 'y', 'c', 'eC1', 'eS2', 'eR5', 'eR4']),
           (r"The $8\,\mathrm{k\Omega}$ falls $105-87=18\,\mathrm{V}$ from $y$ to $c$: $2.25\,\mathrm{mA}$ against the $i_o$ arrow, so $i_o(0^+)=-2.25\,\mathrm{mA}$.", ['eR3']),
       ]),
       view(c6.lecrc(), c2, title='Settled', unit='mA', gnd='low', names=nm, disp={'S2': CLOSED, 'C1': gapC(-60)}, steps=[
           (r"Same ground. $C$ is a gap, the $8\,\mathrm{k\Omega}$ carries nothing: $x=c$. Divider: $c$ sits $75\times\dfrac{40}{200}=15\,\mathrm{V}$ above $d$, i.e. $60\,\mathrm{V}$ **below** the bottom. $v_C(\infty)=-60\,\mathrm{V}$.", ['x', 'y', 'c', 'eR5', 'eR4', 'eR3']),
           (r"Sources off, $C$ sees $8+(160\parallel40)=40\,\mathrm{k\Omega}$: $\tau=40\,\mathrm{k}\times0.25\,\mu=10\,\mathrm{ms}$.", []),
       ]),
   ]),
   old['steps'], old['answer'], old['citations'], after)

nm = {'a': '$a$', 'x': '$x$', 'y': '$y$', 'b': '$b$', 'k': '$k$', '0': 'bottom'}
n0 = [e for e in C['p737']['net'] if e[1] in ('I1', 'R1', 'S1', 'R3', 'R4', 'L1')]
c2 = [('V1', 0), ('R2', 1), ('S2', 1), ('R3', 2), ('R4', 3), ('L1', 4)]
PR('p737', 'Textbook P7.37 · Two-position switch (RL)', 'advanced',
   r'The switch has been in position $a$ for a long time and moves to position $b$ at $t=0$. Find $i_o(t)$ and $v_o(t)$ for $t\ge0$.',
   fence('p737', [
       view(n0, [('I1', 0), ('R1', 1), ('S1', 1), ('R3', 2), ('R4', 3), ('L1', 3)], title='0-', gnd='low', names=nm,
            disp={'S1': CLOSED, 'L1': WIRE_DC}, refs={'R3': ('x', '$v_o$')}, steps=[
           (r"Position $a$, $L$ a wire. The $40\,\mathrm{A}$ pump pulls current **out** of $a$, so $a$ is the lowest wire: ground it.", ['eI1']),
           (r"$4\parallel20\parallel5=2\,\Omega$, so the bottom wire sits $40\times2=80\,\mathrm{V}$ above $a$: $v_o(0^-)=-80\,\mathrm{V}$.", ['z0', 'y', 'eR1', 'eR3', 'eS1']),
           (r"The $5\,\Omega$ falls $80\,\mathrm{V}$ from $y$ to $x$: $16\,\mathrm{A}$ against the $i_o$ arrow. $i_o(0^-)=-16\,\mathrm{A}$.", ['eR4', 'eL1']),
       ]),
       view(c6.p737(-16), c2, title='0+', names=nm, disp={'S2': CLOSED, 'L1': holdL(-16)}, refs={'R3': ('x', '$v_o$')}, steps=[
           (r"Position $b$. Ground the bottom. The battery lifts $k$ to $240\,\mathrm{V}$. $L$ is a pump still pushing $16\,\mathrm{A}$ up to $y$.", ['k', 'eV1', 'eL1']),
           (r"In = out at $x$: $16=\dfrac{x}{20}+\dfrac{x-240}{60}$, so $x=300\,\mathrm{V}$: $v_o(0^+)=300\,\mathrm{V}$ (a big jump).", ['x', 'b', 'y', 'eR3', 'eR2', 'eS2', 'eR4']),
       ]),
       view(c6.p737(), c2, title='Settled', names=nm, disp={'S2': CLOSED, 'L1': WIRE_DC}, refs={'R3': ('x', '$v_o$')}, steps=[
           (r"Same ground. $L$ a wire: $y$ on the floor. In = out at $x$: $\dfrac{240-x}{60}=\dfrac{x}{20}+\dfrac{x}{5}$, so $x=15\,\mathrm{V}$: $i_o=3\,\mathrm{A}$, $v_o=15\,\mathrm{V}$.", ['x', 'b', 'eR2', 'eR3', 'eR4', 'eL1']),
           (r"Sources off, $L$ sees $5+(20\parallel60)=20\,\Omega$: $\tau=\dfrac{10\,\mathrm{mH}}{20}=0.5\,\mathrm{ms}$.", []),
       ]),
   ]),
   [S(r'$0^-$: $L$ a wire, the pump into $4\parallel20\parallel5=2\,\Omega$.', r'v_o(0^-)=-40\cdot2=-80\,\mathrm{V},\qquad i_o(0^-)=\frac{-80}{5}=-16\,\mathrm{A}=i_o(0^+)'),
    S(r'$\infty$ and $\tau$.', r'i_o(\infty)=3\,\mathrm{A},\qquad \tau=\frac{0.01}{5+20\parallel60}=0.5\,\mathrm{ms}'),
    S('One slide.', r'i_o(t)=3+(-16-3)e^{-2000t}=3-19e^{-2000t}\,\mathrm{A}'),
    S(r'$v_o$ from in = out at $x$: $\dfrac{v_o}{15}=4-i_o$.', r'v_o(t)=15+285e^{-2000t}\,\mathrm{V},\quad t\ge0^+')],
   r'$i_o(t)=3-19e^{-2000t}\,\mathrm{A}$ for $t\ge0$; $v_o(t)=15+285e^{-2000t}\,\mathrm{V}$ for $t\ge0^+$.', tb('7.37'))

H(1, 'Cheat sheet')
T(['Idea', 'In heights', 'Write'], [
    ['Capacitor', 'a height step that can\'t jump', '$i=C\\,\\dfrac{dv}{dt}$, $w=\\tfrac12Cv^2$'],
    ['Inductor', 'a flow that can\'t jump', '$v=L\\,\\dfrac{di}{dt}$, $w=\\tfrac12Li^2$'],
    ['Settled (DC)', '$C$ a gap, $L$ a wire', '$i_C=0$, $v_L=0$'],
    ['Just after a switch', '$C$ a battery, $L$ a pump', '$v_C(0^+)=v_C(0^-)$, $i_L(0^+)=i_L(0^-)$'],
    ['Combine', '$L$ like $R$, $C$ like $\\tfrac1R$', '$L_s=\\sum L$, $C_p=\\sum C$'],
    ['Time constant', 'what $C$ or $L$ sees, sources off', '$\\tau=R_{\\mathrm{Th}}C$, $\\tau=\\dfrac{L}{R_{\\mathrm{Th}}}$'],
    ['The slide', 'start $\\to$ end, $63\\%$ per $\\tau$', '$x(t)=x(\\infty)+[x(0^+)-x(\\infty)]e^{-t/\\tau}$'],
    ['Energy left', '', '$w(t)=w(0)\\,e^{-2t/\\tau}$'],
])

D.save(os.path.join(HERE, 'w45', 'w6v3_blocks.json'))
