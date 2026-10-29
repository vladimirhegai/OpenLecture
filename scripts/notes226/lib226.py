"""Shared builder for the ELEC 226 Test 2 notes (one Open Lecture document per test question).

Usage in a note module:
    from lib226 import Doc, S, cite
    D = Doc('q1', 'Test 2 - Question 1', ['discrete_rv', ...])
    D.H('Topic 1: ...'); D.P('...'); D.EQ(r'...'); D.EX(...); D.TRY(...); D.Q(...)
    D.save()        # writes out/q1.json; with --publish also creates or replaces the course document

Callout tones: info | tip | warning | reminder (purple: Test 1 / calculus material the topic relies on).
Citations: cite('L10', 4) -> Lecture 10 page 4; tags L1-L15, T2-T6 (tutorials), P1-P3 (practice sets).
Graphs: D.GRAPH(lines) writes a ```graph fence (grammar in src/open_lecture/skills/math-tools.md);
stems() and steps() generate PMF stem plots and step-CDF plots.
"""
import json
import os
import sys
import urllib.error
import urllib.request
import uuid

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
COURSE = '149e587a-a62f-415a-91de-6337ea2f0006'
API = f'http://127.0.0.1:8000/api/v1/courses/{COURSE}'
_CITES = json.load(open(os.path.join(OUT, 'citations.json'), encoding='utf-8'))
FILES = {
    **{f'L{n}': f'ELEC226_326 Lec{n:02}{s}.pdf' for n, s in
       [(1, '-1'), (2, '-1'), (3, '-1'), (4, '-1'), (5, '-1'), (6, '-2'), (7, '-1'), (8, ''), (9, ''), (10, ''),
        (11, ''), (12, ''), (13, ''), (14, ''), (15, '')]},
    'T2': 'Tutorial 2-2.pdf', 'T3': 'Tutorial 3-2.pdf', 'T4': 'Tutorial 4.pdf', 'T5': 'Tutorial 5.pdf',
    'T6': 'Tutorial 6.pdf', 'P1': 'Practice 01 (week1&2)-1.pdf', 'P2': 'Practice 02.pdf', 'P3': 'Practice 03.pdf',
}


def cite(tag, *pages):
    return [_CITES[FILES[tag]][str(p)] for p in pages]


def S(explanation, latex=''):
    """One solution step: a short plain-language line, then (optionally) the math. A tuple of latex lines is stacked,
    one centred equation per line."""
    if isinstance(latex, tuple):
        latex = '\\begin{gathered}' + ' \\\\ '.join(latex) + '\\end{gathered}' if len(latex) > 1 else latex[0]
    return {"explanation": explanation, "latex": latex}


def _get(url):
    return json.load(urllib.request.urlopen(url))


def _send(url, body, method):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method=method,
                                 headers={'Content-Type': 'application/json'})
    try:
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        raise SystemExit(f'HTTP {e.code}: {e.read().decode()[:3000]}')


def num(v, d=4):
    """Short number for graph expressions."""
    return f'{v:.{d}g}'


def sci(v, d=3):
    """LaTeX scientific notation: 4.24\\times10^{-8}."""
    m, e = f'{v:.{d - 1}e}'.split('e')
    return f'{m}\\times10^{{{int(e)}}}'


def stems(pairs, color=1, label=None):
    """PMF stem plot lines: a vertical segment and a dot for every (x, p)."""
    out = []
    for i, (x, p) in enumerate(pairs):
        lab = f' label="{label}"' if label and i == 0 else ''
        out.append(f'segment "{x}" "0" "{x}" "{p}" color={color}{lab}')
        out.append(f'point "{x}" "{p}" color={color}')
    return out


def steps(pairs, x0, x1, color=1):
    """Step-CDF plot lines from sorted (x, P(X=x)) pairs over [x0, x1]: flat pieces, a dot at each closed left end."""
    out, total, prev = [], 0.0, x0
    for x, p in pairs:
        out.append(f'segment "{prev}" "{num(total)}" "{x}" "{num(total)}" color={color}')
        total += float(p)
        out.append(f'point "{x}" "{num(total)}" color={color}')
        prev = x
    out.append(f'segment "{prev}" "{num(total)}" "{x1}" "{num(total)}" color={color}')
    return out


class Doc:
    def __init__(self, key, title, topic_keys):
        self.key, self.title, self.topic_keys = key, title, topic_keys
        self.B = []
        self.ex = 0   # running example number
        self.tr = 0   # running try-it number
        self.q = 0    # running practice-question number

    def _add(self, b, k):
        b['id'] = str(uuid.uuid5(uuid.NAMESPACE_URL, f'elec226/{self.key}/{len(self.B)}/{k}'))
        b.setdefault('citations', [])
        self.B.append(b)

    def H(self, text, level=1, cites=()):
        self._add({"type": "heading", "level": level, "text": text, "citations": list(cites)}, 'h' + text)

    def P(self, text, cites=()):
        self._add({"type": "paragraph", "text": text, "citations": list(cites)}, 'p' + text[:60])

    def CO(self, tone, text, cites=()):
        assert tone in ('info', 'warning', 'tip', 'reminder'), tone
        self._add({"type": "callout", "tone": tone, "text": text, "citations": list(cites)}, 'c' + text[:60])

    def REMIND(self, text, cites=()):
        """Purple reminder box: what you need from Test 1 (or calculus) for this topic."""
        self.CO('reminder', text, cites)

    def BOX(self, title, text, cites=()):
        """A closed card (click the title to open)."""
        self._add({"type": "solution", "title": title, "text": text, "collapsed": True, "citations": list(cites)},
                  'w' + title)

    def WHY(self, title, text):
        """A closed box for skip-safe theory: WHY('Why does this work?', '...') -> '… (optional)'."""
        self.BOX(f'{title} (optional)', text)

    def CARD(self, title, steps_, answer=None, cites=(), numbered=True):
        """A closed example card with room to breathe: steps_ = [(text, latex), ...]. Each step is its own line
        ('Step 1 · **Range** …'), its math centred below it; latex may be a tuple for several centred lines.
        numbered=False for a reference card (formulas, shortcuts) whose lines aren't steps."""
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
        """Worked example (shown solved)."""
        self.ex += 1
        self._add({"type": "worked_example", "title": f'Example {self.ex} · {title}', "prompt": prompt,
                   "steps": steps_, "answer": answer, "citations": list(cites)}, 'x' + title)

    def _prob(self, label, title, prompt, steps_, answer, diff, cites):
        self._add({"type": "practice_problem", "title": f'{label} · {title}', "difficulty": diff,
                   "origin": "source" if cites else "original", "prompt": prompt, "solution": "",
                   "steps": steps_, "answer": answer, "citations": list(cites)}, 'q' + label + title)

    def TRY(self, title, prompt, steps_, answer, diff='intermediate', cites=()):
        """A short practice problem inside a topic (solution hidden)."""
        self.tr += 1
        self._prob(f'Try it {self.tr}', title, prompt, steps_, answer, diff, cites)

    def Q(self, title, prompt, steps_, answer, diff='intermediate', cites=()):
        """A test-style question in the final Practice Questions section."""
        self.q += 1
        self._prob(f'Question {self.q}', title, prompt, steps_, answer, diff, cites)

    def STEPS(self, title, rows, intro=''):
        """An equation stepper: rows = [(latex, note), ...]; use \\hl{...} on what changed."""
        out = ['```steps', f'title "{title}"']
        for latex, note in rows:
            assert '$$' not in latex and '\n' not in note
            out += ['$$', latex, '$$', note]  # multi-line step form (the $$-own-line check in save() needs it)
        self._add({"type": "paragraph", "text": (intro + '\n\n' if intro else '') + '\n'.join(out + ['```']),
                   "citations": []}, 'st' + title)

    def GRAPH(self, lines, intro=''):
        body = '\n'.join(l.strip() for l in lines if l.strip())
        self._add({"type": "paragraph", "text": (intro + '\n\n' if intro else '') + f'```graph\n{body}\n```',
                   "citations": []}, 'g' + body[:80])

    # ---------------------------------------------------------------- output
    def save(self):
        for b in self.B:  # display math: full-size fractions (\tfrac is for inline text only)
            if b['type'] == 'equation':
                b['latex'] = b['latex'].replace('\\tfrac', '\\frac')
            for st in b.get('steps', []):
                st['latex'] = st['latex'].replace('\\tfrac', '\\frac')
                assert st['explanation'].strip(), f"empty step explanation in {b.get('title')}"
        for b in self.B:  # a $$ display inside Markdown text must sit on its own lines or it renders inline
            for s in _strings(b):
                for line in s.split('\n'):
                    assert not (line.strip().startswith('$$') and line.strip() != '$$'), 'put $$ on its own line: ' + line[:80]
        ids = [b['id'] for b in self.B]
        assert len(ids) == len(set(ids)), 'duplicate block ids'
        for b in self.B:
            for s in _strings(b):
                assert not any(ord(c) < 32 and c != '\n' for c in s), 'control character (lost backslash?): ' + s[:120]
                body = s.replace('\\$', '')
                if '```graph' not in s:
                    assert body.count('$') % 2 == 0, 'odd number of $ in: ' + s[:160]
        path = os.path.join(OUT, f'{self.key}.json')
        json.dump({"title": self.title, "topic_keys": self.topic_keys, "blocks": self.B},
                  open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f'{self.key}: {len(self.B)} blocks ({self.ex} examples, {self.tr} try-its, {self.q} questions) -> {path}')
        if '--publish' in sys.argv:
            self.publish()

    def publish(self):
        # one id file per note (out/doc_<key>.txt), so notes can be published in parallel
        idfile = os.path.join(OUT, f'doc_{self.key}.txt')
        if not os.path.exists(idfile):
            body = {"title": self.title, "document_type": "study_notes", "academic_week": None,
                    "topic_keys": self.topic_keys, "blocks": self.B, "actor": "agent",
                    "idempotency_key": f'elec226-test2-{self.key}-v1'}
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
            b = dict(b, id=str(uuid.uuid4()))  # fresh ids: an old block with the same id may not be removed yet
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
