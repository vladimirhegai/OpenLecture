"""Assemble build_w5v3.py from verified pieces of build_w5.py (by line range) and the new sections in w5v3_new.py,
then number the worked examples and Try its in page order."""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
old = open(os.path.join(HERE, 'build_w5.py'), encoding='utf-8').read().split('\n')
new = {}
cur = None
for line in open(os.path.join(HERE, 'w5v3_new.py'), encoding='utf-8').read().split('\n'):
    m = re.match(r'#### SECTION (\w+)', line)
    if m:
        cur = m.group(1)
        new[cur] = []
    else:
        new[cur].append(line)


def O(a, b):
    """Lines a..b (1-based, inclusive) of build_w5.py."""
    return '\n'.join(old[a - 1:b])


def N(name):
    return '\n'.join(new[name]).strip('\n')


parts = [
    N('header'),
    O(41, 61),                      # Example 0 (open, short, sources off) + signs note
    N('topic1'),
    O(71, 71),                      # test-source equation
    O(442, 448),                    # w5A: a diamond lowers the climb
    O(77, 91), O(92, 113),          # lecneg, lecm4
    O(114, 134), O(135, 149),       # Try: AP 4.19, P4.80
    N('p474'), N('p481'),
    N('topic2'),
    O(157, 157),                    # max power equation
    O(452, 464),                    # w5B matched vs not
    O(158, 180), O(181, 202),       # lec360, lecmp
    O(203, 219), O(220, 244),       # Try: P4.84, P4.88
    N('p483'), N('p487'),
    N('topic3'),
    O(252, 252),                    # superposition equation
    O(468, 482),                    # w5C two pictures one sum
    O(253, 277), O(278, 304),       # lecsup, lecsupd
    O(305, 330), O(331, 353),       # Try: P4.94, P4.96
    N('p495'),
    N('practice'),
    O(377, 406), O(407, 435),       # P4.93, AP 4.21 + P4.86
    N('p498'),
    N('cheat'),
    "D.save(os.path.join(HERE, 'w45', 'w5v3_blocks.json'))",
]
src = '\n\n'.join(parts) + '\n'

# Number titles in page order: EX -> "Example k", PR before the practice set -> "Try it k".
practice_at = src.index("H(1, 'Practice set')")
counts = {'EX': 0, 'PR': 0}


def retitle(m):
    kind, key, title = m.group(1), m.group(2), m.group(3)
    clean = re.sub(r'^(Try it \d+|[A-Z]\d? ?|S) · ', '', title)
    tb = re.match(r'^Textbook (P[\d.]+) · (.*)$', clean)
    if tb and (kind == 'EX' or m.start() < practice_at):
        clean = f'{tb.group(2)} (Textbook {tb.group(1)})'
    if kind == 'EX':
        t = f'Example {counts["EX"]} · {clean}'
        counts['EX'] += 1
    elif m.start() < practice_at:
        counts['PR'] += 1
        t = f'Try it {counts["PR"]} · {clean}'
    else:
        t = title
    return f"{kind}('{key}', '{t}'"


src = re.sub(r"\b(EX|PR)\('(\w+)', '([^']*)'", retitle, src)
open(os.path.join(HERE, 'build_w5v3.py'), 'w', encoding='utf-8').write(src)
print('examples', counts['EX'], 'try its', counts['PR'])
