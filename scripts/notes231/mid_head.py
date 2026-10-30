"""Start here: the cram plan (10:00-18:00), what to skip, and where each kind of question is taught."""
from midlib import link


def build(D):
    D.H('Start here: what the midterm asks')
    D.P('**Midterm:** 2 hours · 30 marks · Casio 991 only. Everything up to Monday Oct 26’s lecture and this week’s tutorial. '
        '**No Laplace transforms.**')
    D.CO('tip', r'**The prof reuses his own problems.** If you can do every lecture example and tutorial problem, you’re fine: '
         r'the midterm is that hard or easier. In this note they are marked **★**. '
         r'Do the ★ ones first. The rest are short, easier warm-ups.')

    D.P('**Today’s plan (10:00–18:00).** Each block: read the steps, then do that section’s ★ problems with the answer closed.')
    D.T(['Time', 'Do', 'The ★ problems'], [
        ['10:00–10:30', link('Topic A', 'topic-a') + ' complex numbers', 'Ex 1.1 divide, Ex 1.2 roots'],
        ['10:30–11:45', link('B0', 'topic-b') + ', ' + link('B1', 'b1') + ', ' + link('B2', 'b2') + ' name it, separable, linear',
         'Ex 2.1, Ex 3.1–3.4, RL circuit, Pre-tut 3'],
        ['11:45–12:00', 'break', ''],
        ['12:00–13:00', link('B3', 'b3') + ', ' + link('B4', 'b4') + ' exact, make it exact', 'Ex 4.1–4.6, Pre-tut 4'],
        ['13:00–13:45', 'lunch', ''],
        ['13:45–14:30', link('D1', 'd1') + ' RC / RL circuits', 'Pre-tut 1, Pre-tut 2, RC natural/step'],
        ['14:30–15:30', link('B5', 'b5') + ', ' + link('D2', 'd2') + ' characteristic equation, RLC', 'Ex 5.2 (24 mA)'],
        ['15:30–15:45', 'break', ''],
        ['15:45–16:45', link('B6', 'b6') + ', ' + link('B7', 'b7') + ' undetermined coefficients, reduction of order',
         r'Pre-tut 5 ($6\cos^2t$), $y\prime\prime-ty\prime+y=0$'],
        ['16:45–17:05', link('Topic C', 'topic-c') + ' does a unique solution exist?', 'the two theorems'],
        ['17:05–18:00', link('Topic E', 'topic-e') + ' final run', 'redo every ★ from memory'],
    ])
    D.P('**Behind? Cut from the bottom of each block, never the ★ problems.** If you’re really short on time, skip '
        + link('Topic C', 'topic-c') + ' and the non-★ warm-ups.')
    D.P('**Not taught, so not in this note:** Wronskians, the “multiply the guess by $t$” fix, guesses for $e^{at}$ or '
        'polynomial right sides, textbook circuit problems, Thévenin inside a circuit, Laplace.')

    D.P('Every solution in this note has the same shape. Use it on the exam too:')
    D.L([r'**Type:** say what kind of problem it is, and the clue. Example: “$y\prime=t^2y$ is separable: a $t$-part times a $y$-part.”',
         r'**Steps:** run that section’s numbered steps, using its words. Every method starts with **Write**.',
         r'**Plug in:** use the given values to find the constants. Example: $y=Ce^{2t}$ with $y(0)=5$ gives $C=5$.'],
        ordered=True)
    D.P('**Where do I go?** Find what the question gives you, then click the link. The browser’s Back button brings you back.')
    D.T(['The question gives you…', 'Go to'], [
        ['a complex number to convert, multiply, divide, power, roots', link('Topic A', 'topic-a')],
        ['an ODE to classify (order, linear, …)', link('Topic B', 'topic-b')],
        [r'a first-order ODE where you can split the $y$’s from the $t$’s', link('B1 · Separable', 'b1')],
        [r'$y\prime+p(t)\,y=f(t)$', link('B2 · Integrating factor', 'b2')],
        [r'$M\,dt+N\,dy=0$', link('B3 · Exact', 'b3') + ', ' + link('B4 · Make it exact', 'b4')],
        [r'$ay\prime\prime+by\prime+cy=0$ (numbers $a,b,c$)', link('B5 · Characteristic equation', 'b5')],
        [r'$ay\prime\prime+by\prime+cy=f(t)$', link('B6 · Undetermined coefficients', 'b6')],
        [r'$t$ in the coefficients, and one solution given', link('B7 · Reduction of order', 'b7')],
        ['“does a unique solution exist?”, or an interval', link('Topic C', 'topic-c')],
        [r'a circuit with a switch: find $v(t)$ or $i(t)$', link('Topic D', 'topic-d')],
    ])


def verify():
    pass
