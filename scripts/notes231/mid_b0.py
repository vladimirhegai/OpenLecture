"""Topic B opening: name the equation, pick the method (Week 2 classification), what a general solution is."""
import sympy as sp

from midlib import P, S, TAGS, link, t, zero


def build(D):
    W2 = lambda *p: D.cite('W2', *p)
    D.H('Topic B: Find the general solution', cites=W2(2, 3))
    TAGS(D, (2, 1), (2, 2))
    D.P(r'This is the core of the midterm: you are given an ODE (ordinary differential equation) and must find $y(t)$. '
        'There are seven methods, B1–B7. Which one works depends only on what the equation looks like, so the first move is always to **name the equation**.')

    D.P('**Step 1: name it.** Ask these five questions:')
    D.T(['Label', 'Ask', 'Yes', 'No'], [
        ['**Order**', 'What is the highest derivative?', r'$y\prime\prime+y=0$: 2nd order', '—'],
        ['**Linear**', r'Do $y,y\prime,y\prime\prime$ appear only to the first power, never multiplied together or inside a function? ($t$ may appear anywhere.)',
         r'$t^3y\prime\prime+e^ty\prime+y=0$', r'$yy\prime=t$, $\ y\prime=\sin y$, $\ y\prime=y^2$'],
        ['**Homogeneous** (linear only)', r'With every $y$-term on the left, is the right side $0$?', r'$y\prime\prime+4y=0$', r'$y\prime\prime+4y=8$'],
        ['**Constant coefficients**', r'Are the numbers in front of $y,y\prime,y\prime\prime$ constants?', r'$y\prime\prime+3y\prime+2y=0$', r'$ty\prime\prime+y=0$'],
        ['**Autonomous**', r'Is $t$ missing from the equation completely?', r'$y\prime=y(1-y)$', r'$y\prime=t-y$'],
    ], cites=W2(2, 3))

    D.P('**Step 2: pick the method.**')
    D.T(['If the equation is…', 'Method', 'Go to'], [
        [r'1st order, $\dfrac{dy}{dt}=g(t)\,h(y)$', 'separate the variables', link('B1', 'b1')],
        [r'1st order, linear: $y\prime+a(t)\,y=f(t)$', 'integrating factor', link('B2', 'b2')],
        [r'$M\,dt+N\,dy=0$ with $\dfrac{\partial M}{\partial y}=\dfrac{\partial N}{\partial t}$', 'exact equation', link('B3', 'b3')],
        [r'$M\,dt+N\,dy=0$, but the test fails', 'integrating factor that makes it exact', link('B4', 'b4')],
        [r'$ay\prime\prime+by\prime+cy=0$, constants $a,b,c$', 'characteristic equation', link('B5', 'b5')],
        [r'$ay\prime\prime+by\prime+cy=g(t)$', 'undetermined coefficients', link('B6', 'b6')],
        [r'2nd order, $t$ in the coefficients, one solution $y_1$ given', 'reduction of order', link('B7', 'b7')],
    ])

    D.P('**Step 3: fix the constants.** Every method ends with a **general solution**: a formula with arbitrary constants.')
    D.L([r'1st order: one constant, $C$. One condition, like $y(1)=2$, fixes it.',
         r'2nd order: two constants, $c_1,c_2$. Two conditions fix them: usually $y(0)$ and $y\prime(0)$.',
         r'A problem with a condition is an **initial value problem** (IVP). Substitute the condition into the general solution and solve for the constant.'])

    D.P('**Checking a solution** (a Week 2 question type): substitute $y$ and its derivatives into the ODE. '
        'It is a solution if the two sides match for **every** $t$. For an IVP, also check the starting value.')
    D.P(r'Example: $y=e^{-2t}$ and $y\prime+2y=0$: $\;-2e^{-2t}+2e^{-2t}=0$ ✓.')

    P(D, 'W2 · Name it, then route it · lecture Example 2.1 and others',
      'For each equation, give its order, and say whether it is linear, homogeneous, constant-coefficient and autonomous. Then name the subtopic (B1–B7) that solves it.\n\n'
      r'(a) $t^3y\prime\prime+e^ty\prime+y=0$' '\n\n'
      r'(b) $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$' '\n\n'
      r'(c) $y\prime\prime+2y\prime+5y=10$' '\n\n'
      r'(d) $\dfrac{di}{dt}+5i=50$' '\n\n'
      r'(e) $(t-y)\,dt-(t+y)\,dy=0$',
      [S(r'(a) Highest derivative $y\prime\prime$; $y$ terms are first power with $t$-only coefficients; right side 0; coefficients $t^3,e^t$ vary; $t$ appears.'
         r' 2nd order, linear, homogeneous, **not** constant-coefficient, not autonomous → ' + link('B7', 'b7') + ' (once one solution is given).'),
       S(r'(b) $y^2$ is not first power, so nonlinear; $t$ appears. It splits as $\frac{1}{t^3}\cdot y^2$ → ' + link('B1', 'b1') + '.'),
       S(r'(c) 2nd order, linear, right side $10\neq0$ so **non**homogeneous, constant coefficients, autonomous → ' + link('B6', 'b6') + '.'),
       S(r'(d) 1st order, linear, nonhomogeneous, constant coefficients, autonomous → ' + link('B2', 'b2') + r' (it also separates: $\frac{di}{50-5i}=dt$).'),
       S(r'(e) As $y\prime=\frac{t-y}{t+y}$: $y$ sits in a denominator, so nonlinear. In $M\,dt+N\,dy$ form, test exactness → ' + link('B3', 'b3') + '.')],
      r'(a) 2nd, linear, homogeneous, variable coefficients → B7. (b) 1st, nonlinear → B1. (c) 2nd, linear, nonhomogeneous, constant → B6. (d) 1st, linear, constant → B2. (e) 1st, nonlinear → B3.',
      cites=W2(3))
    P(D, 'W2 · Check, then pick the member that fits',
      r'Which of $y=t^2$, $\;y=t^2+1$, $\;y=5t^2$ solve $ty\prime-2y=0$? Which one also satisfies $y(1)=5$?',
      [S(r'**Type:** checking solutions: substitute each one.'),
       S(r'$y=t^2$: $y\prime=2t$.', r't(2t)-2t^2=0\ \checkmark'),
       S(r'$y=t^2+1$: $y\prime=2t$.', r't(2t)-2(t^2+1)=-2\neq0\ \times'),
       S(r'$y=5t^2$: $y\prime=10t$.', r't(10t)-2(5t^2)=0\ \checkmark'),
       S(r'**Condition:** at $t=1$, $t^2=1$ and $5t^2=5$.')],
      r'$t^2$ and $5t^2$ are solutions (both are $Ct^2$); $t^2+1$ is not. Only $y=5t^2$ satisfies $y(1)=5$.')


def verify():
    for sol, ok in ((t ** 2, True), (t ** 2 + 1, False), (5 * t ** 2, True)):
        assert (sp.simplify(t * sp.diff(sol, t) - 2 * sol) == 0) == ok
    zero(sp.diff(sp.exp(-2 * t), t) + 2 * sp.exp(-2 * t))
