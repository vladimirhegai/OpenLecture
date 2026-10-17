"""verify45.py <blocks.json>: drawings parse, height views pass the physics audit, step ids exist, aligned rows intact."""
import json
import os
import re
import shlex
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_views as AV  # noqa: E402

B = json.load(open(sys.argv[1], encoding='utf-8'))
quiet = '-q' in sys.argv
probs = 0


def latexes(b):
    out = [b.get('latex', '')]
    for s in b.get('steps', []):
        out.append(s.get('latex', ''))
    for k in ('text', 'prompt', 'answer'):
        out += re.findall(r'\$\$(.*?)\$\$', b.get(k, '') or '', re.S)
    return out


for b in B:
    name = (b.get('title') or b.get('text') or b.get('caption') or '')[:50]
    for lx in latexes(b):
        for env in ('aligned', 'array'):
            if env in lx and '\\\\' not in lx:
                probs += 1
                print('NO ROW BREAK', name)
    srcs = [m.group(1) for m in re.finditer(r'```schematic\n(.*?)```', b.get('prompt', '') or '', re.S)]
    if b['type'] == 'schematic':
        srcs.append(b['source'])
    for src in srcs:
        req = urllib.request.Request('http://127.0.0.1:8000/api/v1/schematics/check', data=json.dumps({"source": src}).encode(),
                                     headers={'Content-Type': 'application/json'})
        try:
            urllib.request.urlopen(req)
        except urllib.error.HTTPError as e:
            probs += 1
            print('PARSE ERROR', name, e.read()[:300])
        if '#@' not in src:
            continue
        # step ids must name nodes / element ids of their own view
        view = None
        known = {}
        for line in src.splitlines():
            if not line.startswith('#@'):
                continue
            t = shlex.split(line[2:].strip())
            if t[0] == 'view' or view is None:
                view = t[1] if t[0] == 'view' else '(single)'
                known[view] = set()
            if t[0] == 'node':
                known[view].add(t[1])
            elif t[0] == 'el':
                for x in t[5:]:
                    if x.startswith('id='):
                        known[view].add(x[3:])
            elif t[0] == 'step':
                for x in t[2:]:
                    if x.startswith('show='):
                        for sid in x[5:].split(','):
                            if sid not in known[view]:
                                probs += 1
                                print(f'BAD SHOW ID {sid!r} in {name} / {view}')
        if quiet:
            import io
            import contextlib
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                AV.audit(name, src)
            for ln in buf.getvalue().splitlines():
                if '!!' in ln or ln.startswith('=='):
                    if '!!' in ln:
                        probs += 1
                    print(ln)
        else:
            AV.audit(name, src)
print('PROBLEMS:', probs)
