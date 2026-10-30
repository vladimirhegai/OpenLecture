"""Shared builder for the ELEC 231 week notes (Open Lecture documents).

Usage in a week script:
    from lib231 import Doc, S
    D = Doc(week=3, title='Week 3: ...', topic_keys=['separable_odes', ...])
    D.H('Topic 1: ...'); D.P('...'); D.EX(...); D.PR(...)
    D.save()                 # writes out/w3.json (always)
    D.publish()              # only when run with --publish: creates or replaces the course document

Citations: D.cite('W3', 2) -> lecture Week 3 page 2; tags W1-W4 (lectures), T1-T4 (pre-tutorials), SYL (syllabus).
Textbook problems: D.tb('8.3') once the Nilsson textbook in this course is indexed.
Charts: D.CHART(order=1, a=-500, y0=4, duration=0.01, caption='...') plots dy/dt = a*y + forcing
        (order=2: y'' = a*y' + b*y + forcing, with y0, dy0). Cards are cached in out/charts.json.
"""
import json
import os
import sys
import urllib.error
import urllib.request
import uuid

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)
COURSE = '206af2a6-c1f1-4700-ac44-5eba708c676b'
API = f'http://127.0.0.1:8000/api/v1/courses/{COURSE}'
CITES = json.load(open(os.path.join(HERE, 'cites.json'), encoding='utf-8'))
DOCS = os.path.join(OUT, 'docs.json')
CHARTS = os.path.join(OUT, 'charts.json')


def _get(url):
    return json.load(urllib.request.urlopen(url))


def _send(url, body, method):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method=method,
                                 headers={'Content-Type': 'application/json'})
    try:
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        raise SystemExit(f'HTTP {e.code}: {e.read().decode()[:3000]}')


def S(explanation, latex=''):
    """One solution step: a plain-language sentence, then (optionally) the math. A tuple of latex lines is stacked,
    one centred equation per line."""
    if isinstance(latex, tuple):
        latex = '\\begin{gathered}' + ' \\\\ '.join(latex) + '\\end{gathered}' if len(latex) > 1 else latex[0]
    return {"explanation": explanation, "latex": latex}


def flow(src, *lines):
    """Make a schematic live (animated current, clickable switches): appends `#~ flow` plus any extra `#~` lines,
    e.g. flow(src, 'init C1 2'). Values come from the labels; see skills/schematic.md "Current flow"."""
    return src.rstrip('\n') + '\n#~ flow' + ''.join('\n#~ ' + line for line in lines)


def steps_fence(title, steps):
    """A ```steps fence as text, for D.STEPS or for a solution / step explanation: steps = [(latex, note), ...]."""
    out = ['```steps', f'title "{title}"'] if title else ['```steps']
    for latex, note in steps:
        assert '$$' not in latex and '\n' not in note, 'stepper latex/note: no $$ or newlines'
        out.append(f'$$ {latex} $$')
        if note:
            out.append(note)
    return '\n'.join(out + ['```'])


class Doc:
    def __init__(self, week, title, topic_keys):
        """week: the academic week (int), or a key such as 'mid' for a note that belongs to no single week."""
        self.week, self.title, self.topic_keys = week, title, topic_keys
        self.academic_week = week if isinstance(week, int) else None
        self.B = []
        self.ex = 0  # running example number
        self.tr = 0  # running try-it number

    # ---------------------------------------------------------------- citations
    def cite(self, tag, *pages):
        return [CITES[tag][str(p)] for p in pages]

    def tb(self, number):
        tbid = _textbook_id()
        probs = _get(f'{API}/textbook/problems?chapter={number.split(".")[0]}&limit=100')
        hits = [p for p in probs if p['number'] == number and p['citation']['source_id'] == tbid]
        assert hits, f'textbook problem {number} not indexed'
        return [hits[0]['citation']]

    # ---------------------------------------------------------------- blocks
    def _id(self, k):
        return str(uuid.uuid5(uuid.NAMESPACE_URL, f'elec231/w{self.week}/{len(self.B)}/{k}'))

    def _add(self, b, key):
        b['id'] = self._id(key)
        b.setdefault('citations', [])
        self.B.append(b)

    def H(self, text, level=1, cites=()):
        self._add({"type": "heading", "level": level, "text": text, "citations": list(cites)}, 'h' + text)

    def P(self, text, cites=()):
        self._add({"type": "paragraph", "text": text, "citations": list(cites)}, 'p' + text[:60])

    def CO(self, tone, text, cites=()):
        assert tone in ('info', 'warning', 'tip'), tone
        self._add({"type": "callout", "tone": tone, "text": text, "citations": list(cites)}, 'c' + text[:60])

    def BOX(self, title, text):
        """A closed card (click the title to open), e.g. a shortcut with its short example."""
        self._add({"type": "solution", "title": title, "text": text, "collapsed": True}, 'w' + title)

    def WHY(self, title, text):
        """A closed box for skip-safe theory: WHY('Why are we allowed to do this?', '...') -> '… (optional)'."""
        self.BOX(f'{title} (optional)', text)

    def L(self, items, ordered=False, cites=()):
        self._add({"type": "list", "items": list(items), "ordered": ordered, "citations": list(cites)}, 'l' + items[0][:60])

    def T(self, columns, rows, cites=()):
        assert all(len(r) == len(columns) for r in rows), 'table rows must match columns'
        self._add({"type": "table", "columns": columns, "rows": rows, "citations": list(cites)}, 't' + columns[0] + rows[0][0][:40])

    def EQ(self, latex, cites=()):
        self._add({"type": "equation", "latex": latex, "display": True, "citations": list(cites)}, 'e' + latex[:60])

    def SCH(self, source, caption, cites=()):
        self._add({"type": "schematic", "source": source, "caption": caption, "citations": list(cites)}, 's' + caption[:60])

    def EX(self, title, prompt, steps, answer, cites=()):
        """Worked example (shown solved). Title gets 'Example k · '."""
        self.ex += 1
        self._add({"type": "worked_example", "title": f'Example {self.ex} · {title}', "prompt": prompt,
                   "steps": steps, "answer": answer, "citations": list(cites)}, 'x' + title)

    def PR(self, title, prompt, steps, answer, diff='introductory', cites=(), label=None):
        """Practice problem (solution hidden until opened). Title gets 'Try it k · ' unless label is given
        (e.g. label='Practice 3' in the mixed set). Problems copied from a source must cite it."""
        if label is None:
            self.tr += 1
            label = f'Try it {self.tr}'
        self._add({"type": "practice_problem", "title": f'{label} · {title}', "difficulty": diff,
                   "origin": "source" if cites else "original", "prompt": prompt, "solution": "",
                   "steps": steps, "answer": answer, "citations": list(cites)}, 'q' + title)

    def FIG(self, url, caption, cites=()):
        """A diagram made with svgfig.Fig(...).save(name) (pass the URL it returns), with an italic caption under it."""
        self._add({"type": "paragraph", "text": f'![{caption}]({url})\n\n*{caption}*', "citations": list(cites)},
                  'f' + url)

    def STEPS(self, title, steps, intro=''):
        """An equation stepper (```steps fence): steps = [(latex, note), ...]. Use \\hl{...} on what changed."""
        self._add({"type": "paragraph", "text": (intro + '\n\n' if intro else '') + steps_fence(title, steps),
                   "citations": []}, 'st' + title)

    def GRAPH(self, source, intro='', kind='graph'):
        """An interactive plot (```graph or ```graph3d fence); grammar in src/open_lecture/skills/math-tools.md."""
        body = '\n'.join(l.strip() for l in source.strip().splitlines())
        self._add({"type": "paragraph", "text": (intro + '\n\n' if intro else '') + f'```{kind}\n{body}\n```',
                   "citations": []}, 'g' + body[:60])

    def GRAPH3D(self, source, intro=''):
        self.GRAPH(source, intro, kind='graph3d')

    def CHART(self, caption, order=1, a=0.0, b=0.0, forcing=0.0, y0=0.0, dy0=0.0, duration=1.0, samples=201):
        """A computed plot of y(t). order 1: y' = a*y + forcing. order 2: y'' = a*y' + b*y + forcing."""
        params = {"order": order, "a": a, "forcing": forcing, "y0": y0, "duration": duration, "samples": samples}
        if order == 2:
            params.update(b=b, dy0=dy0)
        key = json.dumps(params, sort_keys=True)
        charts = CHARTS.replace('.json', f'_w{self.week}.json')  # one cache per week: weeks are built in parallel
        cache = json.load(open(charts)) if os.path.exists(charts) else {}
        if key not in cache:
            cache[key] = _send(f'{API}/math-cards/linear-ode', params, 'POST')['id']
            json.dump(cache, open(charts, 'w'), indent=1)
        self._add({"type": "artifact_reference", "artifact_id": cache[key], "caption": caption, "citations": []},
                  'a' + caption[:60])

    # ---------------------------------------------------------------- output
    def save(self):
        for b in self.B:  # the note column is ~600 px: long "A,\qquad B" displays go on separate lines
            if b['type'] == 'equation':
                b['latex'] = _wrap(b['latex'])
            for st in b.get('steps', []):
                st['latex'] = _wrap(st.get('latex', ''))
        for b in self.B:
            for st in b.get('steps', []):
                assert st['explanation'].strip(), f"empty step explanation in {b.get('title')} (the server rejects it)"
        ids = [b['id'] for b in self.B]
        assert len(ids) == len(set(ids)), 'duplicate block ids'
        for b in self.B:
            for s in _strings(b):
                assert "\\'" not in s, 'stray \\\' in ' + s[:80]
                # \t, \b, \f, \r from a collapsed backslash (e.g. "\tfrac" -> TAB + "frac") break the LaTeX silently
                assert not any(ord(c) < 32 and c != '\n' for c in s), 'control character (lost backslash?) in: ' + s[:120]
                body = s.replace('\\$', '')
                if '```schematic' not in s:
                    assert body.count('$') % 2 == 0, 'odd number of $ in: ' + s[:120]
        path = os.path.join(OUT, f'w{self.week}.json')
        json.dump({"title": self.title, "week": self.week, "topic_keys": self.topic_keys, "blocks": self.B},
                  open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f'{len(self.B)} blocks ({self.ex} examples, {self.tr} try-its) -> {path}')
        if '--publish' in sys.argv:
            self.publish()

    def publish(self):
        docs = json.load(open(DOCS)) if os.path.exists(DOCS) else {}
        key = str(self.week)
        if key not in docs:
            body = {"title": self.title, "document_type": "study_notes", "academic_week": self.academic_week,
                    "topic_keys": self.topic_keys, "blocks": self.B, "actor": "agent",
                    # previews are created and deleted again and again: a fixed key would hit HTTP 409 the second time
                    "idempotency_key": f'elec231-w{self.week}-' + (uuid.uuid4().hex[:8] if str(self.week).startswith('prev') else 'v1')}
            out = _send(f'{API}/documents', body, 'POST')
            # The create response shape varies; look the new note up by week and title instead.
            query = f'?academic_week={self.academic_week}' if self.academic_week is not None else '?limit=100'
            hits = [d for d in _get(f'{API}/documents{query}') if d['title'] == self.title]
            docs[key] = hits[0]['document_id']
            json.dump(docs, open(DOCS, 'w'), indent=1)
            print('created', docs[key])
            return
        url = f'{API}/documents/{docs[key]}'
        doc = _get(url)
        old = [b['id'] for b in doc['blocks']]
        ops = [{"op": "remove", "block_id": i} for i in old]
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
        print('replaced', docs[key], 'revision', rev, 'blocks', len(out['blocks']))


def _wrap(latex, limit=55):
    """Split a long display at top-level ',\\qquad' / '\\qquad' into a gathered block (one part per line)."""
    if len(latex) <= limit or '\\begin{' in latex or '\\qquad' not in latex:
        return latex
    parts, depth, cur, i = [], 0, '', 0
    while i < len(latex):
        if latex.startswith(',\\qquad', i) and depth == 0:
            parts.append(cur + ','); cur = ''; i += len(',\\qquad'); continue  # noqa: E702
        if latex.startswith('\\qquad', i) and depth == 0:
            parts.append(cur); cur = ''; i += len('\\qquad'); continue  # noqa: E702
        ch = latex[i]
        depth += ch == '{'
        depth -= ch == '}'
        cur += ch
        i += 1
    parts.append(cur)
    parts = [p.strip() for p in parts if p.strip()]
    return latex if len(parts) < 2 else '\\begin{gathered}' + ' \\\\ '.join(parts) + '\\end{gathered}'


def _strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, list):
        for v in x:
            yield from _strings(v)
    elif isinstance(x, dict):
        for k, v in x.items():
            if k not in ('id', 'citations', 'artifact_id'):
                yield from _strings(v)


_TB = []


def _textbook_id():
    if not _TB:
        _TB.append([s['id'] for s in _get(f'{API}/sources') if s['kind'] == 'textbook'][0])
    return _TB[0]
