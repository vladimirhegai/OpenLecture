"""Flag non-raw string literals whose backslashes would be eaten by Python (\\t -> TAB, \\f, \\b, '\\ ', ...).

Usage: python lintstr.py q1.py [q2.py ...]   (exit 1 if anything is found)
LaTeX belongs in r'...' strings; a plain '...' string may only contain doubled backslashes.
"""
import io
import re
import sys
import tokenize

bad = 0
for path in sys.argv[1:]:
    with open(path, encoding='utf-8') as fh:
        raw_f = []  # Python 3.12+: is each open f-string raw (rf'...')? Its middle tokens carry no prefix.
        for tok in tokenize.generate_tokens(io.StringIO(fh.read()).readline):
            if tok.type == getattr(tokenize, 'FSTRING_START', -1):
                raw_f.append('r' in tok.string.lower())
            elif tok.type == getattr(tokenize, 'FSTRING_END', -1):
                raw_f.pop()
            if tok.type not in (tokenize.STRING, getattr(tokenize, 'FSTRING_MIDDLE', -1)):
                continue
            text = tok.string
            if tok.type == tokenize.STRING:
                prefix = re.match(r'[a-zA-Z]*', text).group().lower()
                if 'r' in prefix:
                    continue
            elif raw_f and raw_f[-1]:
                continue
            # a single backslash (not part of a \\ pair) that is not \n or a quote escape
            for m in re.finditer(r'(?<!\\)(?:\\\\)*\\([^\\\n\'"])', text):
                if m.group(1) == 'n' and not re.match(r'[a-z]', text[m.end():m.end() + 1] or ' '):
                    continue  # a genuine newline escape such as '\n\n'
                print(f'{path}:{tok.start[0]}: single backslash before {m.group(1)!r}: {text[:90]}')
                bad += 1
                break
sys.exit(1 if bad else 0)
