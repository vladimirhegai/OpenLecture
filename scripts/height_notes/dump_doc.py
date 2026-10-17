"""Save a course document's JSON and a readable text dump.  usage: dump_doc.py <docId> <out_prefix> [--full]"""
import json
import sys
import urllib.request

C = '4f61c7c9-90ce-4e64-8e1b-b7fb2f198e0b'
doc_id, out = sys.argv[1], sys.argv[2]
full = '--full' in sys.argv
doc = json.load(urllib.request.urlopen(f'http://127.0.0.1:8000/api/v1/courses/{C}/documents/{doc_id}'))
json.dump(doc, open(out + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def strip_views(s):
    if full:
        return s
    return '\n'.join(ln for ln in s.splitlines() if not ln.startswith('#@ ') or ln.startswith('#@ step'))


lines = [f'# {doc["title"]}  (rev {doc["revision"]}, {len(doc["blocks"])} blocks)']
for i, b in enumerate(doc['blocks']):
    t = b['type']
    head = f'\n[{i}] <{t}> {b["id"][:8]}'
    if t == 'heading':
        lines.append(head + ' ' + '#' * b['level'] + ' ' + b['text'])
    elif t in ('paragraph', 'callout'):
        lines.append(head + (' ' + b.get('tone', '') if t == 'callout' else '') + '\n' + strip_views(b['text']))
    elif t == 'list':
        lines.append(head + '\n' + '\n'.join('- ' + x for x in b['items']))
    elif t == 'table':
        lines.append(head + '\n| ' + ' | '.join(b['columns']) + ' |\n' + '\n'.join('| ' + ' | '.join(r) + ' |' for r in b['rows']))
    elif t == 'equation':
        lines.append(head + '\n$$' + b['latex'] + '$$')
    elif t in ('worked_example', 'practice_problem'):
        lines.append(head + f' TITLE: {b.get("title")}\nPROMPT: ' + strip_views(b['prompt']))
        for s in b.get('steps', []):
            lines.append('  STEP: ' + s['explanation'] + ('  $$' + s['latex'] + '$$' if s.get('latex') else ''))
        if b.get('solution'):
            lines.append('  SOLUTION: ' + b['solution'])
        lines.append('  ANSWER: ' + str(b.get('answer')))
    else:
        lines.append(head + ' ' + json.dumps(b, ensure_ascii=False)[:1500])
open(out + '.txt', 'w', encoding='utf-8').write('\n'.join(lines))
print(out, doc['revision'], len(doc['blocks']), 'blocks', sum(len(x) for x in lines), 'chars')
