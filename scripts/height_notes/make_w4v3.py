"""Assemble build_w4v3.py from verified pieces of build_w4.py (by line range) and the new sections in w4v3_new.py,
then number the worked examples and Try its in page order."""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
old = open(os.path.join(HERE, 'build_w4.py'), encoding='utf-8').read().split('\n')
new = {}
cur = None
for line in open(os.path.join(HERE, 'w4v3_new.py'), encoding='utf-8').read().split('\n'):
    m = re.match(r'#### SECTION (\w+)', line)
    if m:
        cur = m.group(1)
        new[cur] = []
    else:
        new[cur].append(line)


def O(a, b):
    """Lines a..b (1-based, inclusive) of build_w4.py."""
    return '\n'.join(old[a - 1:b])


def N(name):
    return '\n'.join(new[name]).strip('\n')


parts = [
    N('header'),
    O(39, 50),                      # Example 0: one unknown height
    N('topic1'),
    O(59, 77),                      # lec300 (which method)
    O(101, 114),                    # swap rule + the two forms
    O(115, 132),                    # stx
    N('swap2'),
    O(133, 156),                    # lec250
    O(78, 94),                      # Try: P4.54
    N('p458'),
    O(157, 171), O(172, 188),       # Try: P4.59, lecture p.9
    O(333, 346),                    # Try: P4.60
    N('p461'), N('p462'),
    N('topic2'),
    O(197, 219),                    # Thévenin eq + thpic
    O(413, 430),                    # w4C all three tabs
    O(220, 245),                    # lecth
    O(246, 265), O(266, 291),       # Try: P4.65, P4.64
    N('p466'), N('p467'),
    O(292, 312), O(347, 366),       # Try: P4.69, P4.68
    N('p477'),
    N('practice'),
    O(316, 332),                    # P4.63
    N('p456'),
    O(367, 389),                    # P4.73
    N('p470'),
    N('cheat'),
    "D.save(os.path.join(HERE, 'w45', 'w4v3_blocks.json'))",
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
open(os.path.join(HERE, 'build_w4v3.py'), 'w', encoding='utf-8').write(src)
print('examples', counts['EX'], 'try its', counts['PR'])
