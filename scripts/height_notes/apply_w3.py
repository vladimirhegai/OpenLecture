import json, urllib.request, sys, copy
URL = 'http://127.0.0.1:8000/api/v1/courses/4f61c7c9-90ce-4e64-8e1b-b7fb2f198e0b/documents/290341c7-0912-433a-9885-eee77e12fb27'
doc = json.load(urllib.request.urlopen(URL))
old = [b['id'] for b in doc['blocks']]
new = json.load(open('w3_blocks.json', encoding='utf-8'))
ops = []
for i, b in enumerate(new):
    b = copy.deepcopy(b)
    if i < len(old):
        b['id'] = old[i]
        ops.append({"op": "replace", "block_id": old[i], "block": b})
    else:
        ops.append({"op": "insert", "block": b, "after_id": ops[-1]['block']['id']})
for oid in old[len(new):]:
    ops.append({"op": "remove", "block_id": oid})
print(len(ops), 'ops, revision', doc['revision'])
assert len(ops) <= 100
body = {"expected_revision": doc['revision'], "operations": ops, "actor": "agent"}
req = urllib.request.Request(URL, data=json.dumps(body).encode(), method='PATCH', headers={'Content-Type': 'application/json'})
try:
    out = json.load(urllib.request.urlopen(req)); print('revision', out['revision'], 'blocks', len(out['blocks']))
except urllib.error.HTTPError as e:
    print('ERROR', e.code, e.read().decode()[:2000])
