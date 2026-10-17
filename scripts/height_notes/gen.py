"""Generate #@ height-view lines from a solved netlist, so every height, fall and current label comes from the solver."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from circuits import C  # noqa: E402
from mna import solve  # noqa: E402

TINY = 1e-9


def num(x):
    if abs(x) < 5e-10:
        return '0'
    if abs(x - round(x)) < 1e-7:
        return str(int(round(x)))
    s = f'{x:.4g}'
    return s


def volts(x):
    return f'${num(x)}\\,\\mathrm{{V}}$'


def amps(x, unit):
    if unit == 'mA':
        return f'${num(abs(x) * 1000)}\\,\\mathrm{{mA}}$'
    return f'${num(abs(x))}\\,\\mathrm{{A}}$'


def ohms(r):
    if r >= 1000:
        return f'{num(r / 1000)}\\,\\mathrm{{k\\Omega}}'
    return f'{num(r)}\\,\\Omega'


def view(key, title=None, gnd='0', names=None, unit='A', cols=None, refs=None, elabel=None, rails=(),
         straight_off=False, steps=(), notes=(), net=None, flip=()):
    """Return the '#@' lines of one view."""
    names = names or {}
    refs = refs or {}
    elabel = elabel or {}
    net = net or C[key]['net']
    V, I, _ = solve(net)
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

    used = []
    els = []
    byname = {e[1]: e for e in net}
    for name, col in cols:
        e = byname[name]
        kind, _, a, b = e[:4]
        cur = I[name]
        if kind == 'R':
            fall = abs(H[a] - H[b])
            lab = f'${ohms(e[4])}$: ' + (f'falls {volts(fall)}' if fall > 1e-7 else 'no fall')
            to = (b if cur > 0 else a)
        elif kind == 'V':
            lab = f'${num(e[4])}\\,\\mathrm{{V}}$'
            to = (b if cur > 0 else a)
        elif kind == 'E':
            lab = f'{elabel[name]}: {volts(H[a] - H[b])}'
            to = (b if cur > 0 else a)
        elif kind == 'I':
            lab = amps(e[4], unit) if unit == 'mA' else f'${num(e[4])}\\,\\mathrm{{A}}$'
            to = (b if cur > 0 else a)
        elif kind == 'G':
            lab = f'{elabel[name]}: {amps(cur, unit)}'
            to = (b if cur > 0 else a)
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
        if name in rails:
            s += ' rail'
        els.append(s)
    for n in sorted(used, key=lambda n: -H[n]):
        lines.append(f'#@ node {rn(n)} {num(H[n]) if abs(H[n]) > 5e-10 else 0} "{names.get(n, "$" + n + "$")}: {volts(H[n])}"')
    gname = names.get(gnd, 'ground')
    for g in gnodes:
        lines.append(f'#@ node {g} 0 "{gname}: $0\\,\\mathrm{{V}}$" ground')
    lines += els
    for text, show in steps:
        assert '"' not in text, text
        lines.append(f'#@ step "{text}"' + (f' show={",".join(show)}' if show else ''))
    for n in notes:
        assert '"' not in n
        lines.append(f'#@ note "{n}"')
    return lines


def fence(key, views, spoiler=True, inline=False, sch=None):
    head = []
    if inline:
        head.append('#@ inline')
    if spoiler:
        head.append('#@ spoiler')
    body = [ln for v in views for ln in v]
    return '```schematic\n' + (sch or C[key]['sch']) + '\n' + '\n'.join(head + body) + '\n```'
