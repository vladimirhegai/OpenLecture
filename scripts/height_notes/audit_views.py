"""Physics audit of #@ height views: downhill resistors, 'falls X' labels, R = fall/i, KCL per level, power balance."""
import re
import shlex
import sys

sys.path.insert(0, __file__.rsplit('/', 1)[0].rsplit('\\', 1)[0])


PFX = {'m': 1e-3, 'u': 1e-6, 'k': 1e3, '': 1}


def num(s):
    """'$4.167\\,\\mathrm{mA}$' -> 0.004167 ; returns None if no number."""
    m = re.search(r'(-?[\d.]+)\\?,?\s*\\?(?:mathrm\{)?\s*([mku]?)(?:A|V|\\Omega)', s.replace('\\,', ' '))
    if not m:
        return None
    return float(m.group(1)) * PFX[m.group(2)]


def audit(key, src):
    views, cur = [], None
    for line in src.splitlines():
        if not line.startswith('#@'):
            continue
        toks = shlex.split(line[2:].strip(), posix=True)
        if not toks:
            continue
        if toks[0] == 'view' or cur is None:
            cur = {'title': toks[1] if toks[0] == 'view' else '(single)', 'nodes': {}, 'gnd': set(), 'els': []}
            views.append(cur)
            if toks[0] == 'view':
                continue
        if toks[0] == 'node':
            cur['nodes'][toks[1]] = float(toks[2])
            if 'ground' in toks[4:]:
                cur['gnd'].add(toks[1])
        elif toks[0] == 'el':
            kind, a, b, label = toks[1:5]
            opts = dict(t.split('=', 1) for t in toks[5:] if '=' in t)
            cur['els'].append((kind, a, b, label, opts))
    for v in views:
        H = v['nodes']
        canon = lambda n: 'GND' if n in v['gnd'] else n  # noqa: E731
        net = {}
        ptot = 0.0
        probs = []
        for kind, a, b, label, o in v['els']:
            i = num(o['i']) if 'i' in o else 0.0
            if 'i' in o and 'to' not in o:
                probs.append(f'{label}: i without to')
            to = o.get('to')
            frm = (b if to == a else a) if to else None
            if to and to not in (a, b):
                probs.append(f'{label}: to={to} not an end')
            if to:
                net[canon(frm)] = net.get(canon(frm), 0) - i
                net[canon(to)] = net.get(canon(to), 0) + i
                ptot += i * (H[frm] - H[to])  # absorbed
            fall = abs(H[a] - H[b])
            fm = re.search(r'falls \$([\d.]+)\\,\\mathrm\{(m?)V\}', label)
            if fm:
                stated = float(fm.group(1)) * (1e-3 if fm.group(2) else 1)
                if abs(stated - fall) > max(0.006 * fall, 0.006):
                    probs.append(f'{label}: says falls {stated}, heights give {fall:.4f}')
            if kind == 'R':
                if to and H[to] > H[frm] + 1e-9:
                    probs.append(f'{label}: current runs UPHILL')
                if i and fall > 1e-9:
                    print(f'   {v["title"][:22]:22s} R {a}->{b}: fall {fall:.4g} V, i {i:.4g} A, R=fall/i {fall / i:.5g}  [{label[:40]}]')
                if not i and fall > 1e-6:
                    probs.append(f'{label}: resistor with a fall but no current')
            if kind in 'VE':
                step = H[a] - H[b]
                print(f'   {v["title"][:22]:22s} {kind} +{a}/-{b}: step {step:.4g} V  [{label[:40]}]')
        for n, s in net.items():
            if abs(s) > 1e-3 * max(1e-3, max(abs(x) for x in net.values())):
                probs.append(f'KCL at {n}: net {s:.5g} A')
        print(f'== {key} / {v["title"]}: power absorbed total {ptot:.4g} W', '| OK' if not probs else '')
        for p in probs:
            print('   !!', p)


if __name__ == "__main__":
  from new_blocks import SCHEMATICS
  for k, s in SCHEMATICS.items():
    audit(k, s)
