"""Block constructors shared by build_w4.py and build_w5.py (same shapes as build_w3.py)."""
import json
import os
import uuid

HERE = os.path.dirname(os.path.abspath(__file__))
TB = {p['number']: p['citation'] for p in json.load(open(os.path.join(HERE, 'w45', 'tb4.json'), encoding='utf-8'))}


def old_cites(week, oldfile=None):
    """Citations of the pre-rewrite note, keyed by the first 30 characters of each block's title/text/caption."""
    d = json.load(open(os.path.join(HERE, 'w45', oldfile or f'w{week}_before.json'), encoding='utf-8'))
    out = {}
    for b in d['blocks']:
        k = (b.get('title') or b.get('text') or b.get('caption') or '')[:30]
        if b.get('citations'):
            out[k] = b['citations']
    return out


class Doc:
    def __init__(self, tag, week, oldfile=None):
        self.B = []
        self.tag = tag
        self.old = old_cites(week, oldfile)
        self.oldblocks = json.load(open(os.path.join(HERE, 'w45', oldfile or f'w{week}_before.json'), encoding='utf-8'))['blocks']

    def ob(self, prefix):
        """An old block by title prefix (to reuse a verified prompt, solution steps and answer)."""
        hits = [b for b in self.oldblocks if (b.get('title') or '').startswith(prefix)]
        assert len(hits) == 1, (prefix, len(hits))
        return hits[0]

    def oc(self, prefix):
        hits = [v for k, v in self.old.items() if k.startswith(prefix[:30])]
        assert hits, prefix
        return hits[0]

    def tb(self, n):
        return [TB[n]]

    def nid(self, k):
        return str(uuid.uuid5(uuid.NAMESPACE_URL, f'{self.tag}/{len(self.B)}/' + k))

    def H(self, level, text, cites=()):
        self.B.append({"type": "heading", "id": self.nid('h' + text), "level": level, "text": text, "citations": list(cites)})

    def P(self, text):
        self.B.append({"type": "paragraph", "id": self.nid('p' + text[:60]), "text": text, "citations": []})

    def CO(self, tone, text):
        self.B.append({"type": "callout", "id": self.nid('c' + text[:60]), "tone": tone, "text": text, "citations": []})

    def L(self, items):
        self.B.append({"type": "list", "id": self.nid('l' + items[0][:60]), "items": items, "ordered": False, "citations": []})

    def T(self, cols, rows):
        self.B.append({"type": "table", "id": self.nid('t' + cols[0] + rows[0][0][:40]), "columns": cols, "rows": rows,
                       "citations": []})

    def EQ(self, latex):
        self.B.append({"type": "equation", "id": self.nid('e' + latex[:60]), "latex": latex, "display": True, "citations": []})

    def SCH(self, source, caption, cites=()):
        self.B.append({"type": "schematic", "id": self.nid('s' + caption[:60]), "source": source, "caption": caption,
                       "citations": list(cites)})

    def EX(self, key, title, intro, fig, steps, answer, cites=(), after=''):
        prompt = intro + '\n\n' + fig + ('\n\n' + after if after else '')
        self.B.append({"type": "worked_example", "id": self.nid('x' + key), "title": title, "prompt": prompt,
                       "steps": steps, "answer": answer, "citations": list(cites)})

    def PR(self, key, title, diff, intro, fig, steps, answer, cites, after=''):
        prompt = intro + '\n\n' + fig + ('\n\n' + after if after else '')
        self.B.append({"type": "practice_problem", "id": self.nid('q' + key), "title": title, "difficulty": diff,
                       "origin": "source", "prompt": prompt, "solution": "", "steps": steps, "answer": answer,
                       "citations": list(cites)})

    def save(self, path):
        # r'...\'s...' keeps the backslash; LaTeX never needs \' here, so strip it everywhere.
        def clean(x):
            if isinstance(x, str):
                return x.replace("\\'", "'")
            if isinstance(x, list):
                return [clean(v) for v in x]
            if isinstance(x, dict):
                return {k: clean(v) for k, v in x.items()}
            return x
        self.B = clean(self.B)
        ids = [b['id'] for b in self.B]
        assert len(ids) == len(set(ids)), 'duplicate ids'
        json.dump(self.B, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(len(self.B), 'blocks ->', path)


def S(e, l=''):
    return {"explanation": e, "latex": l}
