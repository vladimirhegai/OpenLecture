"""ELEC 231 midterm note: Weeks 1-6 organised by problem type (one note, Topics A-D).

    python build_midterm.py                  build every section, verify, save out/wmid.json, export Markdown
    python build_midterm.py --publish        ... and replace the live note
    python build_midterm.py --preview b1 b2  build only those sections into a separate preview note and publish it
                                             (for checking a section in the browser; ids in out/docs.json 'prev-...')

Each section lives in mid_<part>.py with build(D) and verify(). The layout rules are in MIDTERM_STYLE.md.
"""
import importlib
import os
import sys

import lib231
from learning_notes import finish
from lib231 import Doc

PARTS = ['head', 'a', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'c', 'd0', 'd1', 'd2', 'e']
TITLE = 'ELEC 231 Midterm: Weeks 1–6 by Problem Type'
KEYS = ['complex_numbers', 'separable_odes', 'linear_first_order', 'exact_equations', 'integrating_factors',
        'second_order_homogeneous', 'undetermined_coefficients', 'reduction_of_order',
        'existence_uniqueness', 'rc_rl_circuits', 'rlc_circuits']


def fold_equations(D):
    """The server caps a note at 500 blocks. A line of text and the centred equations right under it render the same as
    one paragraph with $$ displays in it, so fold them together (only blocks without citations)."""
    out = []
    for b in D.B:
        prev = out[-1] if out else None
        if (b['type'] == 'equation' and not b['citations'] and prev and prev['type'] == 'paragraph'
                and not prev['citations'] and '```' not in prev['text']):
            prev['text'] += '\n\n$$\n' + lib231._wrap(b['latex']) + '\n$$'
        else:
            out.append(b)
    D.B = out


def main():
    args = sys.argv[1:]
    preview = [a for a in args[args.index('--preview') + 1:] if not a.startswith('--')] if '--preview' in args else None
    parts = preview or PARTS
    modules = []
    for part in parts:
        try:
            modules.append(importlib.import_module(f'mid_{part}'))
        except ModuleNotFoundError as e:
            if preview or e.name != f'mid_{part}':
                raise
            print(f'(section {part} not written yet: skipped)')
    if preview:
        key = 'prev-' + '-'.join(parts)
        # A note with no week is identified by its topic keys, so each preview needs its own (else HTTP 409).
        D = Doc(key, '[preview] Midterm sections ' + ', '.join(parts), [f'midterm_{key}'.replace('-', '_')])
        # Previews run in parallel: keep their ids out of the shared out/docs.json (which also holds the week notes).
        lib231.DOCS = os.path.join(lib231.OUT, f'docs_{key}.json')
        if '--publish' not in sys.argv:
            sys.argv.append('--publish')
    else:
        D = Doc('mid', TITLE, KEYS)
    for module in modules:
        module.verify()
        module.build(D)
    fold_equations(D)
    finish(D, 'ELEC-231-Midterm-Weeks-1-6-by-Problem-Type.md' if not preview else f'../scripts/notes231/out/{key}.md')


if __name__ == '__main__':
    main()
