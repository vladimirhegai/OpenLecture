"""Validation and single-document Markdown export for the revised learning notes."""
import ast
import json
import re
import os
import tempfile
import urllib.request
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
t, y = sp.symbols('t y', real=True)
K = sp.symbols('K', real=True)


def zero(expr):
    assert sp.simplify(expr) == 0, sp.simplify(expr)


def first(solution, rhs, initial=None):
    zero(sp.diff(solution, t) - rhs.subs(y, solution))
    if initial:
        at, value = initial
        zero(solution.subs(t, at) - value)


def potential(M, N, U):
    zero(sp.diff(U, t) - M)
    zero(sp.diff(U, y) - N)


def implicit(M, N, U):
    zero(M * sp.diff(U, y) - N * sp.diff(U, t))


def second(solution, a, b, c, rhs=0, initial=None):
    zero(a*sp.diff(solution, t, 2) + b*sp.diff(solution, t) + c*solution - rhs)
    if initial:
        at, value, slope = initial
        zero(solution.subs(t, at) - value)
        zero(sp.diff(solution, t).subs(t, at) - slope)


def finish(doc, filename):
    """Validate embedded circuits, save/publish, and export only the requested note."""
    def primes(value):
        if isinstance(value, str):
            return re.sub(r'\\prime(?:\\prime)?', lambda m: '^{' + m.group(0) + '}', value)
        if isinstance(value, list):
            return [primes(item) for item in value]
        if isinstance(value, dict):
            return {key: primes(item) for key, item in value.items()}
        return value

    doc.B = primes(doc.B)
    schematics = []
    for block in doc.B:
        if block['type'] == 'schematic':
            schematics.append(block['source'])
        for field in ('text', 'prompt'):
            schematics.extend(re.findall(r'```schematic\n(.*?)```', block.get(field, ''), re.S))
    for source in schematics:
        request = urllib.request.Request('http://127.0.0.1:8000/api/v1/schematics/check',
                                         json.dumps({'source': source}).encode(),
                                         {'Content-Type': 'application/json'})
        checked = json.load(urllib.request.urlopen(request))
        assert not checked['errors'], checked['errors']
        assert not checked['warnings'], checked['warnings']
        print('Circuit connections:', [(e['name'], e['from'], e['to']) for e in checked['elements']])
    doc.save()
    # Reuse the existing Markdown renderer without invoking its all-notes export.
    parsed = ast.parse((ROOT / 'scripts/export_notes.py').read_text(encoding='utf-8'))
    functions = [n for n in parsed.body if isinstance(n, ast.FunctionDef) and n.name in ('steps', 'block')]
    namespace = {}
    exec(compile(ast.Module(body=functions, type_ignores=[]), 'export_notes_renderer', 'exec'), namespace)
    markdown = '# ' + doc.title + '\n\n' + '\n\n'.join(filter(None, (namespace['block'](b) for b in doc.B))) + '\n'
    target = ROOT / 'notes' / filename
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', newline='\n',
                                     dir=target.parent, suffix='.md.tmp', delete=False) as staged:
        staged.write(markdown)
        staged_path = staged.name
    os.replace(staged_path, target)
    print('Exported:', target)
    print('Verified mathematical answers and', len(schematics), 'circuit drawings.')
