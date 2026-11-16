"""Shared builder for the ELEC 221 Midterm 2 notes (Ch 6, 7, 8): one Open Lecture document per chapter.

Same block helpers as scripts/notes226/lib226.py (H, P, EQ, L, T, CO, BOX, CARD, EX, TRY, Q, GRAPH, STEPS), plus:
    sch(src)            a ```schematic fence (parsed with open_lecture.schematic at save time)
    D.CIRCUIT(src, intro)   a paragraph holding one drawing
    near(a, b)          assert two numbers agree (relative 0.2 %), used by every builder's checks
Citations: cite('E7', 9) -> Eren Week 7 slide 9. Tags below.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request
import uuid

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'src'))
from open_lecture import schematic as _schematic  # noqa: E402

OUT = os.path.join(HERE, 'out')
COURSE = '4f61c7c9-90ce-4e64-8e1b-b7fb2f198e0b'
API = f'http://127.0.0.1:8000/api/v1/courses/{COURSE}'
_CITES = json.load(open(os.path.join(OUT, 'citations.json'), encoding='utf-8'))
FILES = {
    'W6': 'ELEC221-F2026-Week6-Sec001.pdf',          # Week 6 lecture (Ch 6 + start of Ch 7)
    'E7': 'ELEC 221 Week 7.pdf', 'E8': 'ELEC 221 Week 8.pdf', 'E9': 'ELEC 221 Week 9.pdf',   # Suzan Eren
    'B7': 'ELEC 221 Fall 2026 Week 7.pdf', 'B8': 'ELEC 221 Fall 2026 Week 8.pdf',          # Alireza Bakhshai
    'T6': 'Tutorial 6 Solutions (1).pdf', 'T8': 'Week 8 Tutorial F2023.pdf',
    'AP6': 'Ch6 Assessment Problems.pdf', 'AP7': 'Ch7 Assessment Problems.pdf', 'AP8': 'Ch8 Assessment Problems.pdf',
}


def cite(tag, *pages):
    return [_CITES[FILES[tag]][str(p)] for p in pages]


def near(a, b, rel=2e-3, abs_=1e-9):
    a, b = float(a), float(b)
    assert abs(a - b) <= max(abs_, rel * max(abs(a), abs(b))), f'{a} != {b}'
    return a


def S(explanation, latex=''):
    """One solution step: a short plain line, then (optionally) the math. A tuple of latex lines is stacked."""
    if isinstance(latex, tuple):
        latex = '\\begin{gathered}' + ' \\\\ '.join(latex) + '\\end{gathered}' if len(latex) > 1 else latex[0]
    return {"explanation": explanation, "latex": latex}


def sch(src):
    return '```schematic\n' + '\n'.join(l.strip() for l in src.strip().split('\n')) + '\n```'


def _get(url):
    return json.load(urllib.request.urlopen(url))


def _send(url, body, method):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method=method,
                                 headers={'Content-Type': 'application/json'})
    try:
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        raise SystemExit(f'HTTP {e.code}: {e.read().decode()[:3000]}')


class Doc:
    def __init__(self, key, title, topic_keys):
        self.key, self.title, self.topic_keys = key, title, topic_keys
        self.B = []
        self.ex = self.tr = self.q = 0

    def _add(self, b, k):
        b['id'] = str(uuid.uuid5(uuid.NAMESPACE_URL, f'elec221/{self.key}/{len(self.B)}/{k}'))
        b.setdefault('citations', [])
        self.B.append(b)

    def H(self, text, level=1, cites=()):
        self._add({"type": "heading", "level": level, "text": text, "citations": list(cites)}, 'h' + text)

    def P(self, text, cites=()):
        self._add({"type": "paragraph", "text": text, "citations": list(cites)}, 'p' + text[:60])

    def CIRCUIT(self, src, intro=''):
        self.P((intro + '\n\n' if intro else '') + sch(src))

    def CO(self, tone, text, cites=()):
        assert tone in ('info', 'warning', 'tip', 'reminder'), tone
        self._add({"type": "callout", "tone": tone, "text": text, "citations": list(cites)}, 'c' + text[:60])

    def BOX(self, title, text, cites=()):
        self._add({"type": "solution", "title": title, "text": text, "collapsed": True, "citations": list(cites)},
                  'w' + title)

    def CARD(self, title, steps_, answer=None, cites=(), numbered=True):
        """Closed card: steps_ = [(text, latex), ...]; each step its own line, its math centred below."""
        parts = []
        for i, (text, latex) in enumerate(steps_, 1):
            parts.append(f'Step {i} · {text}' if numbered else text)
            for line in (latex,) if isinstance(latex, str) else latex:
                if line:
                    parts.append(f'$$\n{line}\n$$')
        if answer:
            parts.append(f'**Answer:**\n\n$$\n{answer}\n$$')
        self.BOX(title, '\n\n'.join(parts), cites)

    def L(self, items, ordered=False, cites=()):
        self._add({"type": "list", "items": list(items), "ordered": ordered, "citations": list(cites)},
                  'l' + items[0][:60])

    def T(self, columns, rows, cites=()):
        assert all(len(r) == len(columns) for r in rows), 'table rows must match columns'
        self._add({"type": "table", "columns": columns, "rows": rows, "citations": list(cites)},
                  't' + columns[0] + rows[0][0][:40])

    def EQ(self, latex, cites=()):
        self._add({"type": "equation", "latex": latex, "display": True, "citations": list(cites)}, 'e' + latex[:60])

    def EX(self, title, prompt, steps_, answer, cites=()):
        self.ex += 1
        self._add({"type": "worked_example", "title": f'Example {self.ex} · {title}', "prompt": prompt,
                   "steps": steps_, "answer": answer, "citations": list(cites)}, 'x' + title)

    def _prob(self, label, title, prompt, steps_, answer, diff, cites):
        self._add({"type": "practice_problem", "title": f'{label} · {title}', "difficulty": diff,
                   "origin": "source" if cites else "original", "prompt": prompt, "solution": "",
                   "steps": steps_, "answer": answer, "citations": list(cites)}, 'q' + label + title)

    def TRY(self, title, prompt, steps_, answer, diff='intermediate', cites=()):
        self.tr += 1
        self._prob(f'Try it {self.tr}', title, prompt, steps_, answer, diff, cites)

    def Q(self, title, prompt, steps_, answer, diff='intermediate', cites=()):
        self.q += 1
        self._prob(f'Question {self.q}', title, prompt, steps_, answer, diff, cites)

    def GRAPH(self, lines, intro=''):
        body = '\n'.join(l.strip() for l in lines if l.strip())
        self._add({"type": "paragraph", "text": (intro + '\n\n' if intro else '') + f'```graph\n{body}\n```',
                   "citations": []}, 'g' + body[:80])

    # ---------------------------------------------------------------- output
    def save(self):
        for b in self.B:
            if b['type'] == 'equation':
                b['latex'] = b['latex'].replace('\\tfrac', '\\frac')
            for st in b.get('steps', []):
                st['latex'] = st['latex'].replace('\\tfrac', '\\frac')
                assert st['explanation'].strip(), f"empty step explanation in {b.get('title')}"
        n_sch = 0
        for b in self.B:
            for s in _strings(b):
                for line in s.split('\n'):
                    assert not (line.strip().startswith('$$') and line.strip() != '$$'), 'put $$ on its own line: ' + line[:80]
                assert not any(ord(c) < 32 and c != '\n' for c in s), 'control character (lost backslash?): ' + s[:120]
                if '```graph' not in s:
                    assert s.replace('\\$', '').count('$') % 2 == 0, 'odd number of $ in: ' + s[:160]
                for src in re.findall(r'```schematic\n(.*?)```', s, re.S):
                    t = _schematic.topology(src)
                    assert not t['errors'], f"schematic errors {t['errors']} in:\n{src}"
                    n_sch += 1
        ids = [b['id'] for b in self.B]
        assert len(ids) == len(set(ids)), 'duplicate block ids'
        path = os.path.join(OUT, f'{self.key}.json')
        json.dump({"title": self.title, "topic_keys": self.topic_keys, "blocks": self.B},
                  open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f'{self.key}: {len(self.B)} blocks ({self.ex} examples, {self.tr} try-its, {self.q} questions, '
              f'{n_sch} circuits) -> {path}')
        if '--publish' in sys.argv:
            self.publish()

    def publish(self):
        idfile = os.path.join(OUT, f'doc_{self.key}.txt')
        if not os.path.exists(idfile):
            body = {"title": self.title, "document_type": "study_notes", "academic_week": None,
                    "topic_keys": self.topic_keys, "blocks": self.B, "actor": "agent",
                    "idempotency_key": f'elec221-mt2-{self.key}-v1'}
            _send(f'{API}/documents', body, 'POST')
            hits = [d for d in _get(f'{API}/documents?limit=100') if d['title'] == self.title]
            open(idfile, 'w').write(hits[0]['document_id'])
            print('created', hits[0]['document_id'])
            return
        url = f'{API}/documents/{open(idfile).read().strip()}'
        doc = _get(url)
        ops = [{"op": "remove", "block_id": b['id']} for b in doc['blocks']]
        prev = None
        for b in self.B:
            b = dict(b, id=str(uuid.uuid4()))
            ops.append({"op": "insert", "block": b, "after_id": prev})
            prev = b['id']
        rev = doc['revision']
        for k in range(0, len(ops), 100):
            out = _send(url, {"expected_revision": rev, "operations": ops[k:k + 100], "actor": "agent",
                              **({"title": self.title} if k == 0 else {})}, 'PATCH')
            rev = out['revision']
        print('replaced', url.rsplit('/', 1)[1], 'revision', rev, 'blocks', len(out['blocks']))


def _strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, list):
        for v in x:
            yield from _strings(v)
    elif isinstance(x, dict):
        for k, v in x.items():
            if k not in ('id', 'citations'):
                yield from _strings(v)
