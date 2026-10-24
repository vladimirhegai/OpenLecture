"""Start here: what the midterm asks, and where each kind of question is taught."""
from midlib import link


def build(D):
    D.H('Start here: what the midterm asks')
    D.P('**Midterm:** Friday Oct 30 · 2 hours · 30 marks · Weeks 1–6 · Casio 991 only.')
    D.P('Every solution in this note is written in the same three moves. Use them on the exam too:')
    D.L([r'**Type:** name the kind of problem, and the clue in the question that told you.',
         r'**Method:** follow the numbered steps from that subtopic.',
         r'**Conditions:** use the given values (or the circuit before the switch) to fix the constants.'],
        ordered=True)
    D.P('Find your question in the left column, then jump to its section. Clicking a link scrolls there; the browser’s Back button returns.')
    D.T(['The question gives you…', 'Go to', 'Weeks'], [
        ['a complex number to convert, multiply, divide, raise to a power or take roots of', link('Topic A', 'topic-a'), '1'],
        ['an ODE to classify, or a function to check', link('Topic B', 'topic-b'), '2'],
        [r'a first-order ODE where the $y$’s and $t$’s can be split apart', link('B1 · Separable', 'b1'), '3'],
        [r'$y\prime+a(t)\,y=f(t)$', link('B2 · Integrating factor', 'b2'), '3'],
        [r'$M\,dt+N\,dy=0$', link('B3 · Exact', 'b3') + ', ' + link('B4 · Make it exact', 'b4'), '4'],
        [r'$ay\prime\prime+by\prime+cy=0$ (numbers $a,b,c$)', link('B5 · Characteristic equation', 'b5'), '4–5'],
        [r'$ay\prime\prime+by\prime+cy=g(t)$', link('B6 · Undetermined coefficients', 'b6'), '6'],
        [r'a second-order ODE with $t$ in the coefficients, and one solution given', link('B7 · Reduction of order', 'b7'), '6'],
        ['“does a unique solution exist?”, an interval, or two solutions to compare', link('Topic C', 'topic-c'), '3, 5, 6'],
        [r'a circuit with a switch: find $v(t)$ or $i(t)$', link('Topic D', 'topic-d'), '1–3, 5'],
    ])


def verify():
    pass
