import json, re, sys, os, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_views as AV
B = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'w3_blocks.json'), encoding='utf-8'))
ids = [b['id'] for b in B]; assert len(ids) == len(set(ids)), 'dup ids'
bad = 0
for b in B:
    for s in b.get('steps', []):
        if 'aligned' in s['latex'] and '\\' not in s['latex']:
            bad += 1; print('NO ROWBREAK', b.get('title'))
    for m in re.finditer(r'```schematic\n(.*?)```', b.get('prompt', ''), re.S):
        src = m.group(1)
        req = urllib.request.Request('http://127.0.0.1:8000/api/v1/schematics/check', data=json.dumps({"source": src}).encode(), headers={'Content-Type': 'application/json'})
        try: urllib.request.urlopen(req)
        except urllib.error.HTTPError as e: print('PARSE ERROR', b.get('title'), e.read()[:300])
        if '#@' in src:
            AV.audit(b.get('title', '')[:40], src)
print('aligned problems', bad)
