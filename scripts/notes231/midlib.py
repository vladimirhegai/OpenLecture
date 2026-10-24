"""Shared helpers for the ELEC 231 midterm note (build_midterm.py and its mid_*.py section modules).

Every subtopic follows one layout (see MIDTERM_STYLE.md):
    heading -> week tags -> why/when -> standard form (equation + "->" bullets) -> mini example
    -> the method (formula + numbered steps) -> calculus table if needed -> optional Bonus callout
    -> worked example (only if needed) -> problems, easy to hard.
"""
import json
import os
import urllib.request

import sympy as sp

from lib231 import API, COURSE, S, steps_fence  # noqa: F401  (re-exported for the section modules)

HERE = os.path.dirname(os.path.abspath(__file__))
t, y = sp.symbols('t y', real=True)

_WEEK_DOCS = json.load(open(os.path.join(HERE, 'out', 'docs.json')))
_HEADINGS = {}


def _headings(week):
    if week not in _HEADINGS:
        doc = json.load(urllib.request.urlopen(f"{API}/documents/{_WEEK_DOCS[str(week)]}"))
        _HEADINGS[week] = [(b['id'], b['text']) for b in doc['blocks'] if b['type'] == 'heading']
    return _HEADINGS[week]


def week_tag(week, topic):
    """A chip linking to 'Topic <topic>' of the Week <week> note (resolved to the live block id at build time)."""
    doc = _WEEK_DOCS[str(week)]
    hits = [bid for bid, text in _headings(week) if text.startswith(f'Topic {topic}:')]
    assert hits, f'Week {week} has no heading "Topic {topic}:"'
    return f'[Week {week} · Topic {topic}](/courses/{COURSE}/docs/{doc}#{hits[0]})'


def TAGS(D, *refs):
    """The tag row under a heading: TAGS(D, (3, 2), (2, 1)) -> 'Week 3 · Topic 2' 'Week 2 · Topic 1' chips."""
    D.P(' '.join(week_tag(w, k) for w, k in refs))


def link(label, target):
    """In-note link to a heading of this note: link('B2', 'b2') -> [B2](#b2); the target is the heading's start."""
    return f'[{label}](#{target})'


def P(D, title, prompt, steps, answer, diff='introductory', cites=()):
    """A practice problem numbered through the whole note: 'Problem n · <title>'. Title starts with the week tag."""
    D.pnum = getattr(D, 'pnum', 0) + 1
    D.PR(title, prompt, steps, answer, diff=diff, cites=cites, label=f'Problem {D.pnum}')


# ---------------------------------------------------------------- sympy checks
def zero(expr):
    assert sp.simplify(expr) == 0, sp.simplify(expr)


def first(solution, rhs, initial=None):
    """solution(t) solves y' = rhs(t, y) (and passes through initial=(t0, y0))."""
    zero(sp.diff(solution, t) - rhs.subs(y, solution))
    if initial:
        zero(solution.subs(t, initial[0]) - initial[1])


def implicit(F, rhs, point=None):
    """The whole family F(t, y) = C solves y' = rhs(t, y): along F = C, y' = -F_t / F_y. Pass F without the constant
    (the family, not one member); with point=(t0, y0) it returns the C of the member through that point."""
    zero(sp.simplify(-sp.diff(F, t) / sp.diff(F, y) - rhs))
    if point:
        return F.subs({t: point[0], y: point[1]})


def second(solution, a, b, c, rhs=0, initial=None):
    zero(a * sp.diff(solution, t, 2) + b * sp.diff(solution, t) + c * solution - rhs)
    if initial:
        at, value, slope = initial
        zero(solution.subs(t, at) - value)
        zero(sp.diff(solution, t).subs(t, at) - slope)
