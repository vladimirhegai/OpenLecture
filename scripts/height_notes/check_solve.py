"""For every Week 3 circuit: drawing topology == netlist topology (via /schematics/check), labels match values, then solve."""
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from circuits import C  # noqa: E402
from mna import solve  # noqa: E402


def check(src):
    req = urllib.request.Request('http://127.0.0.1:8000/api/v1/schematics/check',
                                 data=json.dumps({"source": src}).encode(), headers={'Content-Type': 'application/json'})
    return json.load(urllib.request.urlopen(req))['elements']


def label_value(label):
    m = re.search(r'([\d.]+)\\,\\mathrm\{(k?)\\Omega\}|([\d.]+)\\,\\Omega', label)
    if not m:
        m2 = re.search(r'([\d.]+)\\,\\mathrm\{(m?)([AV])\}', label)
        if m2:
            return float(m2.group(1)) * (1e-3 if m2.group(2) else 1)
        return None
    if m.group(3):
        return float(m.group(3))
    return float(m.group(1)) * (1e3 if m.group(2) else 1)


def topo(key, c):
    els = {e['name']: e for e in check(c['sch'])}
    net = {e[1]: e for e in c['net']}
    probs = []
    if set(els) != set(net):
        probs.append(f'element sets differ: drawing-only {set(els) - set(net)}, net-only {set(net) - set(els)}')
    mp = {}
    for n, e in net.items():
        if n not in els:
            continue
        d = els[n]
        for dn, nn in ((d['from'], e[2]), (d['to'], e[3])):
            if mp.setdefault(dn, nn) != nn:
                probs.append(f'{n}: drawing node {dn} maps to both {mp[dn]} and {nn}')
        if e[0] in 'RVI':
            lv = label_value(d['label'] or '')
            if lv is not None and abs(lv - e[4]) > 1e-9 * max(1, abs(e[4])):
                probs.append(f'{n}: label {d["label"]} vs net {e[4]}')
    inv = {}
    for dn, nn in mp.items():
        if inv.setdefault(nn, dn) != dn:
            probs.append(f'net node {nn} maps from two drawing nodes {inv[nn]} and {dn}')
    if '0' in mp and mp['0'] != '0':
        probs.append(f'drawing ground maps to net {mp["0"]}')
    return probs, mp


def fmt(x):
    return f'{x:.6g}'


if __name__ == '__main__':
    keys = sys.argv[1:] or list(C)
    for k in keys:
        c = C[k]
        probs, mp = topo(k, c)
        V, I, P = solve(c['net'])
        print(f'== {k}: ' + ('TOPOLOGY OK' if not probs else 'PROBLEMS'))
        for p in probs:
            print('   !!', p)
        print('   heights:', {n: fmt(v) for n, v in sorted(V.items(), key=lambda t: -t[1])})
        print('   currents:', {n: fmt(v) for n, v in I.items()})
        print('   absorbed:', {n: fmt(v) for n, v in P.items()}, 'sum', fmt(sum(P.values())))
