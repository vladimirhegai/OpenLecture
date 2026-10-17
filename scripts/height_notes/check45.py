"""Weeks 4-5: every drawing parses, its topology matches the netlist, then solve and print heights."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from check_solve import check, topo, fmt  # noqa: E402
from circuits45 import C  # noqa: E402
from mna import solve  # noqa: E402

keys = sys.argv[1:] or list(C)
for k in keys:
    c = C[k]
    if not c['net']:
        els = check(c['sch'])
        print(f'== {k}: parses, {len(els)} elements (no netlist)')
        continue
    probs, mp = topo(k, c)
    V, I, P = solve(c['net'])
    print(f'== {k}: ' + ('TOPOLOGY OK' if not probs else 'PROBLEMS'))
    for p in probs:
        print('   !!', p)
    print('   heights:', {n: fmt(v) for n, v in sorted(V.items(), key=lambda t: -t[1])})
    print('   currents:', {n: fmt(v) for n, v in I.items()})
    print('   absorbed:', {n: fmt(v) for n, v in P.items()}, 'sum', fmt(sum(P.values())))
