"""ELEC 221 "Practice Problems" note: sections of problems; each solution is a ```circuitsteps fence.

    .venv/Scripts/python.exe scripts/practice221/build_practice.py            # check every problem, write out/practice.json
    .venv/Scripts/python.exe scripts/practice221/build_practice.py --publish  # also create / replace the course document

One module per problem (interface and solving conventions: scripts/practice221/README.md). A module that fails to
import or fails its checks is reported and left out, so the rest of the note still builds.
Write these files with the Write tool, never a shell heredoc (heredocs collapse \\ in LaTeX).
"""
import importlib
import json
import os
import sys
import time
import traceback
import urllib.error
import urllib.request
import uuid

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)
COURSE = '4f61c7c9-90ce-4e64-8e1b-b7fb2f198e0b'
ROOT = 'http://127.0.0.1:8000/api/v1'
API = f'{ROOT}/courses/{COURSE}'
DOCS = os.path.join(OUT, 'docs.json')

SECTIONS = [
    ('A', "Kirchhoff's laws and Ohm's law (meters, bridges, Δ–Y)"),
    ('B', 'Nodal, mesh and source transformation'),
    ('C', 'Thévenin and Norton'),
    ('D', 'Maximum power transfer and superposition'),
    ('M', 'Midterm Practice'),
]
# Document order; problems are numbered 1, 2, 3, ... in this order.
MODULES = [
    'a5_p2_20', 'a1_tut1_p2_19', 'a4_tut1_p2_35', 'a2_ap3_7', 'a3_p3_58',
    'b1_tut4_prob4', 'b2_ap4_10', 'b4_ap4_12', 'b6_p4_47', 'b5_p4_27', 'b3_p4_62', 'b7_p4_63',
    # Thévenin, easiest first, then Norton
    'c3_tut4_p3_2', 'p1_thevenin_mesh', 'c4_ap4_16', 'c5_ap4_18', 'c9_ap4_20',
    # Norton, easiest first
    'c2_p4_64', 'c13_p4_67', 'c14_tb_ap4_19',
    # max power, then superposition
    'd1_ap4_19', 'd3_ap4_21', 'd5_p4_91', 'd2_p4_94', 'd4_p4_96', 'd6_p4_98',
    # past midterm (Fall 2025), in exam order
    'm1_mt25_q1', 'm2_mt25_q2', 'm3_mt25_q3', 'm4_mt25_q4',
]
# Built and checked but left out (the user wants about 8 Thévenin/Norton problems, 2026-10-23):
# c6_p4_68 (≈ AP 4.16), c7_p4_73 (≈ AP 4.18), c10_p4_80 (≈ AP 4.20), c8_p4_69 (works backwards),
# c12_tb_ap4_16 (≈ P4.64), c11_p4_77 (Norton two ways).
UNUSED = [
    'c6_p4_68', 'c7_p4_73', 'c10_p4_80', 'c8_p4_69', 'c12_tb_ap4_16', 'c11_p4_77',
]


class HTTPFail(Exception):
    pass


def _send(url, body, method='POST'):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method=method,
                                 headers={'Content-Type': 'application/json'})
    try:
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        raise HTTPFail(f'HTTP {e.code}: {e.read().decode()[:3000]}')


def check(drawing):
    """Parse a drawing on the server and return ({element: (from, to)}, raw) so the topology can be asserted."""
    drawing = '\n'.join(l for l in drawing.splitlines() if not l.strip().startswith(('#=', '#+')))
    out = _send(f'{ROOT}/schematics/check', {'source': drawing})
    assert not out['errors'], out['errors']
    return {e['name']: (e['from'], e['to']) for e in out['elements']}, out


def circuit_steps(title, steps):
    """steps = [(step title, drawing, notes)]; a drawing may hold `#=` overlay and `#+` value lines."""
    out = ['```circuitsteps', f'title "{title}"']
    for name, drawing, notes in steps:
        assert '```' not in notes and '\n==' not in '\n' + notes, f'step "{name}": notes may not hold ``` or start a line with =='
        for line in notes.splitlines():  # one-line $$...$$ renders inline-sized: display math goes on its own lines
            s = line.strip()
            assert not (s.startswith('$$') and s.endswith('$$') and len(s) > 4), f'step "{name}": put $$ on their own lines: {s}'
        out += [f'== {name}', drawing.strip(), '--', notes.strip()]
    return '\n'.join(out + ['```'])


# ---------------------------------------------------------------- problems
sys.path.insert(0, HERE)
problems, failed = [], []
for name in MODULES:
    try:
        m = importlib.import_module(name)
        assert m.SECTION in dict(SECTIONS), f'unknown SECTION {m.SECTION!r}'
        check(m.GIVEN)
        for step in m.STEPS:
            check(step[1])
        m.checks(check)
        problems.append(m)
    except ModuleNotFoundError as e:
        if e.name != name:
            failed.append((name, traceback.format_exc(limit=3)))
    except Exception:
        failed.append((name, traceback.format_exc(limit=3)))
for name, err in failed:
    print(f'!! {name} left out:\n{err}')

# ---------------------------------------------------------------- document
TITLE = 'Practice Problems'
B = []


def add(b, key):
    b['id'] = str(uuid.uuid5(uuid.NAMESPACE_URL, f'elec221/practice/{key}'))
    b.setdefault('citations', [])
    B.append(b)


n = 0
for key, heading in SECTIONS:
    mods = [m for m in problems if m.SECTION == key]
    if not mods:
        continue
    add({'type': 'heading', 'level': 1, 'text': heading}, 'sec' + key)
    for m in mods:
        n += 1
        add({'type': 'heading', 'level': 2, 'text': f'Problem {n} · {m.TITLE}'}, m.__name__ + 'h')
        text = f'*{m.SOURCE}*\n\n{m.PROMPT.strip()}\n\n```schematic\n{m.GIVEN.strip()}\n```'
        add({'type': 'paragraph', 'text': text, 'citations': list(getattr(m, 'CITES', []))}, m.__name__ + 'q')
        add({'type': 'solution', 'title': 'Show solution', 'collapsed': True,
             'text': circuit_steps(f'Problem {n} · {m.TITLE}', m.STEPS)}, m.__name__ + 's')

for b in B:
    assert not any(ord(c) < 32 and c != '\n' for c in b.get('text', '')), 'control char (lost backslash?) in ' + b.get('text', '')[:80]

path = os.path.join(OUT, 'practice.json')
json.dump({'title': TITLE, 'blocks': B}, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{n} problems, {len(B)} blocks -> {path}')

if '--publish' in sys.argv:
    docs = json.load(open(DOCS)) if os.path.exists(DOCS) else {}
    if 'practice' not in docs:
        out = _send(f'{API}/documents', {'title': TITLE, 'document_type': 'practice_set', 'academic_week': None,
                                         'topic_keys': [], 'blocks': B, 'actor': 'agent',
                                         'idempotency_key': 'elec221-practice-v1'})
        did = out.get('document_id') or out.get('document', {}).get('document_id') or out.get('id')
        docs['practice'] = did
        json.dump(docs, open(DOCS, 'w'), indent=1)
        print('created', did)
    else:
        # Remove everything, then insert in order (ids are stable per problem, so collapsed state follows them).
        # Retries because several builders may publish at once (expected_revision conflict).
        did = docs['practice']
        for attempt in range(6):
            cur = json.load(urllib.request.urlopen(f'{API}/documents/{did}'))
            old = [b['id'] for b in cur['blocks']]
            ops = [{'op': 'remove', 'block_id': oid} for oid in old]
            prev = None
            for b in B:
                ops.append({'op': 'insert', 'block': b, **({'after_id': prev} if prev else {})})
                prev = b['id']
            try:
                for i in range(0, len(ops), 100):  # max 100 operations per edit
                    cur = _send(f'{API}/documents/{did}', {'expected_revision': cur['revision'],
                                                           'operations': ops[i:i + 100], 'actor': 'agent'}, 'PATCH')
                print('replaced', did, 'rev', cur.get('revision'))
                break
            except HTTPFail as e:
                print('retrying:', str(e)[:200])
                time.sleep(1 + attempt)
        else:
            raise SystemExit('publish failed')
