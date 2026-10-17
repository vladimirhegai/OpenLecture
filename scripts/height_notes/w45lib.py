"""Height-view generator for Weeks 4-5 (Full loop only), plus Thévenin helpers. Every number comes from mna.solve."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from circuits45 import C  # noqa: E402
from gen import num, amps, ohms  # noqa: E402
from mna import solve  # noqa: E402

TINY = 1e-9


DIGITS = [2]  # decimals for heights and falls; view(..., digits=4) raises it for one view


def hnum(x):
    """Heights and falls: up to 2 decimals (116.25, 27.46), never 4-significant-figure rounding."""
    if abs(x) < 1:
        return num(x)
    s = f'{x:.{DIGITS[0]}f}'.rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s


def volts(x):
    return f'${hnum(x)}\\,\\mathrm{{V}}$'


def off(net, keep=()):
    """Independent sources off: V -> 0 V (a wire), I -> 0 A (a gap). Dependent sources stay."""
    out = []
    for e in net:
        if e[0] == 'V' and e[1] not in keep:
            out.append(e[:4] + (0,))
        elif e[0] == 'I' and e[1] not in keep:
            out.append(e[:4] + (0,))
        else:
            out.append(e)
    return out


def thevenin(net, a, b='0'):
    """(V_Th, R_Th, I_N) at a-b with v_ab + at a; I_N is the short-circuit current a->b."""
    V, _, _ = solve(net)
    vth = V[a] - V[b]
    Vt, _, _ = solve(off(net) + [('I', 'IT', b, a, 1.0)])
    rth = Vt[a] - Vt[b]
    _, I, _ = solve(net + [('V', 'SC', a, b, 0)])
    return vth, rth, I['SC']


def view(net, cols, title=None, gnd='0', names=None, unit='A', refs=None, elabel=None, disp=None, terminals=(),
         steps=(), notes=(), flip=(), straight_off=True, digits=2):
    """'#@' lines for one view. gnd='low' grounds the lowest node. disp={name: (kind, label)} redraws an element
    (e.g. a 0 V source as a flat 'W' wire, a 0 A source as an 'S' gap, a short across a-b)."""
    DIGITS[0] = digits
    try:
        return _view(net, cols, title, gnd, names, unit, refs, elabel, disp, terminals, steps, notes, flip, straight_off)
    finally:
        DIGITS[0] = 2


def _view(net, cols, title, gnd, names, unit, refs, elabel, disp, terminals, steps, notes, flip, straight_off):
    names = names or {}
    refs = refs or {}
    elabel = elabel or {}
    disp = disp or {}
    V, I, _ = solve(net)
    if gnd == 'low':
        gnd = min(V, key=lambda n: (round(V[n], 9), n != '0'))
    h0 = V[gnd]
    H = {n: v - h0 for n, v in V.items()}
    rn = (lambda n: 'z0' if n == '0' else n)
    lines = []
    if title:
        lines.append(f'#@ view "{title}"')
    if straight_off:
        lines.append('#@ straight off')
    gcount = [0]
    gnodes = []

    def end(n):
        if n == gnd:
            gcount[0] += 1
            g = 'g' if gcount[0] == 1 else f'g{gcount[0]}'
            gnodes.append(g)
            return g
        return rn(n)

    used, els = [], []
    byname = {e[1]: e for e in net}
    for name, col in cols:
        e = byname[name]
        kind, _, a, b = e[:4]
        cur = I[name]
        to = b if cur > 0 else a
        if name in disp:
            kind, lab = disp[name]
        elif kind == 'R':
            fall = abs(H[a] - H[b])
            lab = f'${ohms(e[4])}$: ' + (f'falls {volts(fall)}' if fall > 1e-7 else 'no fall')
        elif kind == 'V':
            lab = f'${num(e[4])}\\,\\mathrm{{V}}$'
        elif kind == 'E':
            lab = f'{elabel[name]}: {volts(H[a] - H[b])}'
        elif kind == 'I':
            lab = amps(e[4], unit)
        elif kind == 'G':
            lab = f'{elabel[name]}: {amps(cur, unit)}'
        else:
            raise ValueError(kind)
        A, B = (b, a) if name in flip else (a, b)
        ea, eb = end(A), end(B)
        to_n = ea if to == A else eb
        for n in (A, B):
            if n != gnd and n not in used:
                used.append(n)
        s = f'#@ el {kind} {ea} {eb} "{lab}" col={col}'
        if abs(cur) > TINY:
            s += f' i="{amps(cur, unit)}" to={to_n}'
        s += f' id=e{name}'
        if name in refs:
            pn, vn = refs[name]
            s += f' plus={ea if pn == A else eb} v="{vn}"'
        els.append(s)
    # Nodes at one height share one axis label ("$v_1$ = $a$"), or the merged labels get clipped.
    nm = lambda n: names.get(n, '$' + n + '$')  # noqa: E731
    order = sorted(used, key=lambda n: -H[n]) + [gnd]
    same = {}
    for n in order:
        key = round(H[n], 6)
        if nm(n) not in same.setdefault(key, []):
            same[key].append(nm(n))
    label = lambda n: ' = '.join(same[round(H[n], 6)])  # noqa: E731
    for n in sorted(used, key=lambda n: -H[n]):
        hv = hnum(H[n]) if abs(H[n]) > 5e-10 else 0
        t = ' terminal' if n in terminals else ''
        lines.append(f'#@ node {rn(n)} {hv} "{label(n)}: {volts(H[n])}"{t}')
    for g in gnodes:
        t = ' terminal' if gnd in terminals and g == 'g' else ''
        lines.append(f'#@ node {g} 0 "{label(gnd)}: $0\\,\\mathrm{{V}}$" ground{t}')
    lines += els
    for text, show in steps:
        assert '"' not in text, text
        lines.append(f'#@ step "{text}"' + (f' show={",".join(show)}' if show else ''))
    for n in notes:
        assert '"' not in n, n
        lines.append(f'#@ note "{n}"')
    return lines


def fence(key, views, spoiler=True, inline=False):
    head = (['#@ inline'] if inline else []) + (['#@ spoiler'] if spoiler else [])
    body = [ln for v in views for ln in v]
    return '```schematic\n' + C[key]['sch'] + '\n' + '\n'.join(head + body) + '\n```'


def plain(key):
    return '```schematic\n' + C[key]['sch'] + '\n```'


def fence_c(CC, key, views, spoiler=True, inline=False):
    """Like fence(), for a circuit from another dictionary (e.g. the Week 3 circuits.C)."""
    head = (['#@ inline'] if inline else []) + (['#@ spoiler'] if spoiler else [])
    body = [ln for v in views for ln in v]
    return '```schematic\n' + CC[key]['sch'] + '\n' + '\n'.join(head + body) + '\n```'
