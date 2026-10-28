"""ELEC 221 "Midterm Questions" note: a practice midterm paper; each solution is a ```circuitsteps fence.

    .venv/Scripts/python.exe scripts/midterm221/build_midterm.py            # check every question, write out/midterm.json
    .venv/Scripts/python.exe scripts/midterm221/build_midterm.py --publish  # also create / replace the course document

One module per question, same interface as scripts/practice221 (see its README) plus MARKS and TOPIC.
A module that is missing, fails to import or fails its checks is reported and left out.
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

# Exam order; questions are numbered 1, 2, 3, ... in this order.
MODULES = [
    'q01_delta_wye', 'q02_wye_delta', 'q03_nodal_supernode', 'q04_nodal_dependent', 'q05_mesh_supermesh',
    'q06_mesh_dependent', 'q07_source_transformation',
    # Thévenin and Norton: one with independent sources only, one with a dependent source too
    'q08_thevenin_independent', 'q09_thevenin_max_power', 'q10_norton', 'q11_norton_dependent',
    'q12_superposition',
]

INTRO = r'''A practice midterm in the style of the Fall 2025 paper, longer so every topic gets a question.

| Topic | Questions |
|---|---|
| Δ–Y and Y–Δ | 1, 2 |
| Nodal analysis | 3, 4 |
| Mesh analysis | 5, 6 |
| Source transformation | 7 |
| Thévenin (independent sources only) | 8 |
| Thévenin with a dependent source, and maximum power transfer | 9 |
| Norton (independent sources only) | 10 |
| Norton with a dependent source | 11 |
| Superposition | 12 |

**How to use it:** set a timer, solve each question on paper (calculator allowed), then open the solution.
Use whichever method you like unless the question names one.
Where the exam's formula sheet applies, its formulas sit under the question, as they would on your desk.'''

# The exam's formula sheet, in its own names: a module lists the parts it needs in FORMULAS (shown under the
# question). Only horizontal/vertical lines can be drawn, so the sheet's triangle has a right angle at the top.
FORMULA_SHEET = {
    'delta_wye': r'''**Formula sheet: Δ ↔ Y** (given on the exam)

```schematic
terminal 0,4 "$a$" left
RC 0,4 -> 6,4 "$R_c$"
RB 0,4 -> 0,1 "$R_b$"
wire 0,1 -> 0,0
wire 0,0 -> 3,0
RA 6,4 -> 6,1 "$R_a$" flip
wire 6,1 -> 6,0
wire 6,0 -> 3,0
terminal 6,4 "$b$" right
terminal 3,0 "$c$" below
terminal 9,4 "$a$" left
R1 9,4 -> 12,4 "$R_1$"
R2 12,4 -> 15,4 "$R_2$"
R3 12,4 -> 12,0 "$R_3$"
terminal 15,4 "$b$" right
terminal 12,0 "$c$" below
```

| Δ → Y | Y → Δ |
|---|---|
| $R_1=\dfrac{R_bR_c}{R_a+R_b+R_c}$ | $R_a=\dfrac{R_1R_2+R_2R_3+R_3R_1}{R_1}$ |
| $R_2=\dfrac{R_cR_a}{R_a+R_b+R_c}$ | $R_b=\dfrac{R_1R_2+R_2R_3+R_3R_1}{R_2}$ |
| $R_3=\dfrac{R_aR_b}{R_a+R_b+R_c}$ | $R_c=\dfrac{R_1R_2+R_2R_3+R_3R_1}{R_3}$ |''',
    'max_power': r'''**Formula sheet: maximum power transfer** (given on the exam)

```schematic
V1 0,3 -> 0,0 "$V_{Th}$"
RTH 0,3 -> 4,3 "$R_{Th}$" i="$i_o$"
RL 4,3 -> 4,0 "$R_L$" v="$v_o$"
wire 0,0 -> 4,0
```

$$
\frac{dp_L}{dR_L}=0\;\Rightarrow\;\left[\frac{(R_{Th}+R_L)-2R_L}{(R_{Th}+R_L)^3}\right]V_{Th}^2=0\;\Rightarrow\;\boxed{R_L=R_{Th}}
$$

$$
(p_L)_{max}=p_L\big|_{R_L=R_{Th}}=\frac{R_{Th}}{(R_{Th}+R_{Th})^2}V_{Th}^2\;\Rightarrow\;\boxed{(p_L)_{max}=\frac{V_{Th}^2}{4R_{Th}}=\frac{V_{Th}^2}{4R_L}}
$$''',
}


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


# ---------------------------------------------------------------- questions
sys.path.insert(0, HERE)
questions, failed = [], []
for name in MODULES:
    try:
        m = importlib.import_module(name)
        check(m.GIVEN)
        for step in m.STEPS:
            check(step[1])
        m.checks(check)
        questions.append(m)
    except ModuleNotFoundError as e:
        if e.name != name:
            failed.append((name, traceback.format_exc(limit=3)))
        else:
            print(f'.. {name} not written yet')
    except Exception:
        failed.append((name, traceback.format_exc(limit=3)))
for name, err in failed:
    print(f'!! {name} left out:\n{err}')

# ---------------------------------------------------------------- document
TITLE = 'Midterm Questions'
B = []


def add(b, key):
    b['id'] = str(uuid.uuid5(uuid.NAMESPACE_URL, f'elec221/midterm/{key}'))
    b.setdefault('citations', [])
    B.append(b)


total = sum(m.MARKS for m in questions)
add({'type': 'paragraph', 'text': INTRO + f'\n\n**Total:** {total} marks.'}, 'intro')
for m in questions:
    n = MODULES.index(m.__name__) + 1  # fixed by exam position, even while other questions are missing
    title = f'Question {n} · {m.TITLE}'
    add({'type': 'heading', 'level': 2, 'text': f'{title} ({m.MARKS} marks)'}, m.__name__ + 'h')
    text = f'*{m.TOPIC} · inspired by {m.SOURCE}*\n\n{m.PROMPT.strip()}\n\n```schematic\n{m.GIVEN.strip()}\n```'
    add({'type': 'paragraph', 'text': text, 'citations': list(getattr(m, 'CITES', []))}, m.__name__ + 'q')
    for key in getattr(m, 'FORMULAS', []):
        add({'type': 'callout', 'tone': 'info', 'text': FORMULA_SHEET[key]}, f'{m.__name__}f{key}')
    add({'type': 'solution', 'title': 'Show solution', 'collapsed': True,
         'text': circuit_steps(title, m.STEPS)}, m.__name__ + 's')

for b in B:
    assert not any(ord(c) < 32 and c != '\n' for c in b.get('text', '')), 'control char (lost backslash?) in ' + b.get('text', '')[:80]

path = os.path.join(OUT, 'midterm.json')
json.dump({'title': TITLE, 'blocks': B}, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{len(questions)} questions, {total} marks, {len(B)} blocks -> {path}')

if '--publish' in sys.argv:
    docs = json.load(open(DOCS)) if os.path.exists(DOCS) else {}
    if 'midterm' not in docs:
        out = _send(f'{API}/documents', {'title': TITLE, 'document_type': 'practice_set', 'academic_week': None,
                                         'topic_keys': [], 'blocks': B, 'actor': 'agent',
                                         'idempotency_key': 'elec221-midterm-questions-v1'})
        did = out.get('document_id') or out.get('document', {}).get('document_id') or out.get('id')
        docs['midterm'] = did
        json.dump(docs, open(DOCS, 'w'), indent=1)
        print('created', did)
    else:
        # Remove everything, then insert in order (ids are stable per question, so collapsed state follows them).
        # Retries because several builders may publish at once (expected_revision conflict).
        did = docs['midterm']
        for attempt in range(8):
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
