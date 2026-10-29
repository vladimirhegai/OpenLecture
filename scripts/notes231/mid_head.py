"""Start here: what the midterm asks, and where each kind of question is taught."""
from midlib import link


def build(D):
    D.H('Start here: what the midterm asks')
    D.P('**Midterm:** Friday Oct 30 · 2 hours · 30 marks · Casio 991 only.')
    D.P(r'**What’s on it** (announced in class): everything up to and including Monday Oct 26’s lecture '
        r'(the comments on undetermined coefficients), plus this week’s tutorials (Mon Oct 26 and Wed Oct 28). '
        r'That is every section of this note.')
    D.L([r'**Not on it: Laplace transforms.** Skip them for now.',
         r'**This week’s tutorial problem** is Pre-tutorial 5: $y\prime\prime+y=6\cos^2t$ with $y(0)=0$, $y(\pi/2)=0$. '
         r'It’s the “know this cold” card in ' + link('B6', 'b6') + r'. Practise it until you can do it without looking.'])
    D.P('Every solution in this note has the same shape. Use it on the exam too. '
        'Naming the type first is what tells you which steps to run.')
    D.L([r'**Type:** say what kind of problem it is, and the clue that told you. '
         r'Example: “$y\prime=t^2y$ is separable: the right side is a $t$-part times a $y$-part.”',
         r'**Steps:** run that section’s numbered steps, using its words. Every method starts with **Write** (put it in its form).',
         r'**Plug in:** use the given values to find the constants. Example: $y=Ce^{2t}$ with $y(0)=5$ gives $C=5$. '
         r'(In a circuit, the values come from the circuit just before the switch moves.)'],
        ordered=True)
    D.P('**Where do I go?** Find what your question gives you in the left column, then click the link. '
        'The browser’s Back button brings you back here.')
    D.T(['The question gives you…', 'Go to', 'Weeks'], [
        ['a complex number to convert, multiply, divide, raise to a power or take roots of', link('Topic A', 'topic-a'), '1'],
        ['an ODE to classify, or a function to check as a solution', link('Topic B', 'topic-b'), '2'],
        [r'a first-order ODE where you can split the $y$’s from the $t$’s', link('B1 · Separable', 'b1'), '3'],
        [r'$y\prime+p(t)\,y=f(t)$', link('B2 · Integrating factor', 'b2'), '3'],
        [r'$M\,dt+N\,dy=0$', link('B3 · Exact', 'b3') + ', ' + link('B4 · Make it exact', 'b4'), '4'],
        [r'$ay\prime\prime+by\prime+cy=0$ (numbers $a,b,c$)', link('B5 · Characteristic equation', 'b5'), '4–5'],
        [r'$ay\prime\prime+by\prime+cy=f(t)$', link('B6 · Undetermined coefficients', 'b6'), '6'],
        [r'a second-order ODE with $t$ in the coefficients, and one solution given', link('B7 · Reduction of order', 'b7'), '6'],
        ['“does a unique solution exist?”, an interval, or two solutions to compare', link('Topic C', 'topic-c'), '3, 5, 6'],
        [r'a circuit with a switch: find $v(t)$ or $i(t)$', link('Topic D', 'topic-d'), '1–3, 5'],
        ['a mixed set of exam-style problems, to practise like the real thing', link('Topic E', 'topic-e'), '1–6'],
    ])


def verify():
    pass
