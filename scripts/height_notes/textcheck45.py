"""textcheck45.py <docId>...: odd '$' counts, stray \\' , walkthroughs whose first step doesn't name ground, 'drop' wording."""
import json
import re
import sys
import urllib.request

C = '4f61c7c9-90ce-4e64-8e1b-b7fb2f198e0b'


def strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, list):
        for v in x:
            yield from strings(v)
    elif isinstance(x, dict):
        for v in x.values():
            yield from strings(v)


for doc_id in sys.argv[1:]:
    doc = json.load(urllib.request.urlopen(f'http://127.0.0.1:8000/api/v1/courses/{C}/documents/{doc_id}'))
    print('==', doc['title'], 'rev', doc['revision'])
    n = 0
    for b in doc['blocks']:
        name = (b.get('title') or b.get('text') or '')[:40]
        for s in strings({k: v for k, v in b.items() if k not in ('id', 'citations')}):
            body = '\n'.join(ln for ln in s.splitlines() if not ln.startswith(('#@', 'V', 'R', 'I', 'E', 'G', 'X', 'wire', 'label', 'ground', 'terminal', 'gap')) or ' ' not in ln)
            if body.replace('\\$', '').count('$') % 2:
                n += 1
                print('  ODD $:', name, '|', body[:120].replace('\n', ' '))
            if "\\'" in s:
                n += 1
                print("  STRAY \\':", name)
            if re.search(r'\bdrops?\b', s):
                print('  wording "drop":', name, '|', re.search(r'.{0,40}\bdrops?\b.{0,40}', s).group(0))
        for m in re.finditer(r'```schematic\n(.*?)```', b.get('prompt', '') or '', re.S):
            views = re.split(r'^#@ view ', m.group(1), flags=re.M)
            for v in views:
                st = re.findall(r'^#@ step "(.*?)"', v, re.M)
                if st and not re.search(r'[Gg]round|Same ground', st[0]):
                    n += 1
                    print('  FIRST STEP NO GROUND:', name, '|', v.split('\n')[0][:30], '|', st[0][:80])
    print('  problems:', n)
