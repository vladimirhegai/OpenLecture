"""Solve the new Week 4 circuits (topology check + values), including the two 'find the source value' problems."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import circuits4v3 as c4  # noqa: E402
from check_solve import topo  # noqa: E402
from circuits45 import C  # noqa: E402
from mna import solve  # noqa: E402
from w45lib import thevenin  # noqa: E402


def show(tag, net, gnd=None):
    V, I, P = solve(net)
    if gnd == 'low':
        gnd = min(V, key=lambda n: V[n])
    h0 = V[gnd] if gnd else 0
    print(tag, 'gnd', gnd, {n: round(float(v - h0), 4) for n, v in sorted(V.items(), key=lambda t: -t[1])})
    print('   I', {k: round(float(x), 5) for k, x in I.items()}, '\n   P', {k: round(float(x), 3) for k, x in P.items()})


for k in ['swap2', 'p461', 'p462', 'p466', 'p467', 'p470', 'p477']:
    probs, _ = topo(k, C[k])
    print('==', k, 'TOPOLOGY OK' if not probs else probs)
    show(k, C[k]['net'], 'low')

# P4.58: v_dc such that i_o (30 ohm, a->b) = 0. Linear in v_dc.
io = lambda v: solve(c4.p458_net(v))[1]['R3']  # noqa: E731
v0, v1 = io(0), io(100)
vdc = -v0 * 100 / (v1 - v0)
print('== p458', topo('p458', {'sch': C['p458']['sch'], 'net': c4.p458_net(vdc)})[0] or 'TOPOLOGY OK', 'vdc =', vdc)
show('p458', c4.p458_net(vdc), 'low')

# P4.56: i_dc such that the 15 A source develops 3750 W (it lifts 15 A from q to p by 250 V).
lift = lambda i: (lambda V: V['p'] - V['q'])(solve(c4.p456_net(i))[0])  # noqa: E731
l0, l1 = lift(0), lift(1)
idc = (250 - l0) / (l1 - l0)
print('== p456', topo('p456', {'sch': C['p456']['sch'], 'net': c4.p456_net(idc)})[0] or 'TOPOLOGY OK', 'idc =', idc)
show('p456', c4.p456_net(idc), 'low')

for k, a, b in [('p466', 'a', '0'), ('p467', 'a', '0'), ('p477', 'a', 'b')]:
    print('Thevenin', k, [round(float(x), 5) for x in thevenin(C[k]['net'], a, b)])
gnet = [e for e in C['p470']['net'] if e[1] != 'RG']
print('Thevenin p470 (l-r)', [round(float(x), 6) for x in thevenin(gnet, 'l', 'r')])
