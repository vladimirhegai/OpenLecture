"""Tiny modified-nodal-analysis solver with dependent sources, for checking answers and generating height views.

Elements (node '0' is ground):
  ('R', name, a, b, ohms)                     current a->b = (Va-Vb)/R
  ('V', name, p, n, volts)                    Vp - Vn = volts; branch current p->n through source
  ('I', name, a, b, amps)                     pushes amps from a through the source to b (arrow a->b)
  ('E', name, p, n, {node: k, ...}, const)    Vp - Vn = sum k*V(node) + const   (controlled voltage)
  ('G', name, a, b, {node: k, ...})           current a->b through source = sum k*V(node)
A control "current through resistor R" is written as {a: 1/R, b: -1/R}.
"""
import numpy as np


def solve(elems):
    nodes = sorted({n for e in elems for n in e[2:4]} - {'0'})
    idx = {n: i for i, n in enumerate(nodes)}
    vs = [e for e in elems if e[0] in 'VE']
    N, M = len(nodes), len(vs)
    A = np.zeros((N + M, N + M))
    z = np.zeros(N + M)

    def add(r, node, val):
        if node != '0':
            A[r, idx[node]] += val

    for e in elems:
        k, name, a, b = e[:4]
        if k == 'R':
            g = 1 / e[4]
            for (x, s1) in ((a, 1), (b, -1)):
                if x == '0':
                    continue
                add(idx[x], a, s1 * g)
                add(idx[x], b, -s1 * g)
        elif k == 'I':
            if a != '0':
                z[idx[a]] -= e[4]
            if b != '0':
                z[idx[b]] += e[4]
        elif k == 'G':
            for node, kk in e[4].items():
                if a != '0':
                    add(idx[a], node, kk)
                if b != '0':
                    add(idx[b], node, -kk)
    for j, e in enumerate(vs):
        k, name, p, n = e[:4]
        r = N + j
        if p != '0':
            A[idx[p], r] += 1
            A[r, idx[p]] += 1
        if n != '0':
            A[idx[n], r] -= 1
            A[r, idx[n]] -= 1
        if k == 'V':
            z[r] = e[4]
        else:
            for node, kk in e[4].items():
                add(r, node, -kk)
            z[r] = e[5]
    x = np.linalg.solve(A, z)
    V = {n: x[idx[n]] for n in nodes}
    V['0'] = 0.0
    I = {}
    for j, e in enumerate(vs):
        I[e[1]] = x[N + j]  # current p->n through the source
    for e in elems:
        k, name, a, b = e[:4]
        if k == 'R':
            I[name] = (V[a] - V[b]) / e[4]
        elif k == 'I':
            I[name] = e[4]
        elif k == 'G':
            I[name] = sum(kk * V[nd] for nd, kk in e[4].items())
    # absorbed power: current a->b times (Va - Vb)
    P = {e[1]: I[e[1]] * (V[e[2]] - V[e[3]]) for e in elems}
    return V, I, P
