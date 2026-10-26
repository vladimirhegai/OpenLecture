"""B1: separable equations (Week 3)."""
import sympy as sp

from midlib import P, S, TAGS, first, implicit, link, t, y, zero


def build(D):
    W3 = lambda *p: D.cite('W3', *p)
    D.H('B1 · Separable equations', level=2, cites=W3(4))
    TAGS(D, (3, 1))
    D.P(r'**Start here: can you pull the $y$’s and the $t$’s apart?** If every $y$ can go on one side and every $t$ on the other, '
        r'you just integrate each side. That kind of equation is called **separable**.')
    D.P('It looks like this:')
    D.EQ(r'\dfrac{dy}{dt}=g(t)\,h(y)')
    D.L([r'$g(t)$ = a piece with only $t$ in it',
         r'$h(y)$ = a piece with only $y$ in it'])
    D.P('Reading the form:')
    D.L([r'$\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$ → separable: $g=\dfrac{1}{t^3}$, $h=y^2$.',
         r'$\dfrac{dy}{dt}=3y$ → separable: $g=3$, $h=y$. No $t$ at all is fine.',
         r'$\dfrac{dy}{dt}=t+y$ → **not** separable. A sum won’t split into a product, so go to ' + link('B2', 'b2') + '.',
         r'$t^{-3}\,dt+y\,dy=0$ → already separated: only $t$ sits with $dt$, only $y$ sits with $dy$.'])
    D.P(r'Why it works: once it reads $\dfrac{dy}{h(y)}=g(t)\,dt$, each side has only one letter, so you can integrate each side on its own.')

    D.P('**The method:**')
    D.EQ(r'\int\dfrac{dy}{h(y)}=\int g(t)\,dt+C')
    D.L([r'**Separate:** divide by $h(y)$ and multiply by $dt$, so you get $\dfrac{dy}{h(y)}=g(t)\,dt$.',
         r'**Integrate** both sides. Write just one constant $C$, on the $t$ side.',
         r'**Condition:** plug in the given point to find $C$.',
         r'**Solve for $y$** if you can. If you can’t, an implicit answer like $y^2+3=6(t^2+1)$ is a full answer.'],
        ordered=True)
    D.STEPS('The method on dy/dt = 2ty, y(0) = 3', [
        (r'\dfrac{dy}{dt}=2t\,y', r'Separable: $g=2t$, $h=y$.'),
        (r'\hl{\dfrac{dy}{y}}=\hl{2t\,dt}', r'**Separate:** divide by $y$, multiply by $dt$.'),
        (r'\ln|y|=t^2+\hl{C}', r'**Integrate** each side. One constant, on the $t$ side.'),
        (r'\ln3=0+C\;\Rightarrow\;\hl{C=\ln3}', r'**Condition** $y(0)=3$.'),
        (r'|y|=e^{t^2+\ln3}=\hl{3e^{t^2}}', r'**Solve for $y$:** raise $e$ to both sides, and use $e^{a+b}=e^a\,e^b$.'),
        (r'\hl{y}=3e^{t^2}', r'$y(0)=3$ is positive, so take the $+$ sign.'),
    ])
    D.P('**Calculus you need here:**')
    D.T(['Integral', 'Result', 'Note'], [
        [r'$\int t^n\,dt$', r'$\dfrac{t^{n+1}}{n+1}$', r'any $n\neq-1$, e.g. $\int t^{-3}dt=-\dfrac{1}{2t^2}$'],
        [r'$\int \dfrac1y\,dy$', r'$\ln|y|$', r'the $n=-1$ case'],
        [r'$\int \dfrac{f\prime(t)}{f(t)}\,dt$', r'$\ln|f(t)|$', r'top = derivative of bottom, e.g. $\int\dfrac{t}{t^2+1}dt=\dfrac12\ln(t^2+1)$'],
        [r'$\int e^{at}\,dt$', r'$\dfrac{1}{a}e^{at}$', r'e.g. $\int e^{2t}dt=\dfrac12e^{2t}$'],
        [r'undo $\ln$', r'$e^{\ln A}=A$', r'$e^{C}$ is just a new constant'],
        [r'combine logs', r'$k\ln A+\ln B=\ln(A^kB)$', r'e.g. $3\ln A+\ln B=\ln(A^3B)$'],
    ])
    D.CO('warning', r'**Dividing by $h(y)$ can lose a solution.** If $h(y_0)=0$ for some number $y_0$, the flat line $y=y_0$ is a solution too. '
         r'You can’t divide by zero, so the separated answer skips it.'
         '\n\n'
         r'Example: in $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$, $h=y^2$ is zero at $y=0$. And $y=0$ works ($0=0$), so list it next to your answer.')
    D.CO('info', r'**Bonus (skip-safe): why can you move $dy$ and $dt$ around like fractions?** Divide by $h$: $\dfrac{1}{h(y)}\dfrac{dy}{dt}=g(t)$. '
         r'Now integrate both sides with respect to $t$. '
         r'The chain rule says $\int\dfrac{1}{h(y)}\dfrac{dy}{dt}\,dt=\int\dfrac{1}{h(y)}\,dy$. Moving “$dt$” across is a shortcut for exactly this.')

    D.EX('W3 · Separate after factoring · lecture Example 3.3',
         r'Solve $\dfrac{dy}{dt}=\dfrac{3t+ty^2}{y+t^2y}$, $\;y(1)=3$.',
         [S(r'**Type:** pull $t$ out of the top and $y$ out of the bottom. Now it’s a $t$-piece times a $y$-piece, so it’s separable.',
            r'\dfrac{dy}{dt}=\dfrac{t(3+y^2)}{y(1+t^2)}'),
          S(r'**Separate:** everything with $y$ goes with $dy$, everything with $t$ goes with $dt$.', r'\dfrac{y}{3+y^2}\,dy=\dfrac{t}{1+t^2}\,dt'),
          S(r'**Integrate:** on each side the top is half the derivative of the bottom, so each side gives $\tfrac12\ln(\text{bottom})$.',
            r'\tfrac12\ln(3+y^2)=\tfrac12\ln(1+t^2)+c'),
          S(r'**Undo the $\ln$:** multiply by 2, then raise $e$ to both sides. $e^{2c}$ is just a new constant, $C_1$.', r'3+y^2=C_1(1+t^2)'),
          S(r'**Condition** $y(1)=3$: $\;3+9=C_1(2)$.', r'C_1=6'),
          S(r'**Solve for $y$.** Take the $+$ root, because $y(1)=3$ is positive.', r'y^2=6t^2+3')],
         r'$y^2+3=6(t^2+1)$, so $y=\sqrt{6t^2+3}$.', cites=W3(4))

    P(D, 'W3 · Separate and use a starting value · Pre-tutorial 3(a)',
      r'Solve $\dfrac{dy}{dt}=-\dfrac{t}{y}$, $\;y=2$ when $t=1$.',
      [S(r'**Type:** $-\dfrac{t}{y}=(-t)\cdot\dfrac1y$, a $t$-piece times a $y$-piece. Separable.'),
       S(r'**Separate:** multiply both sides by $y\,dt$.', r'y\,dy=-t\,dt'),
       S(r'**Integrate** each side.', r'\dfrac{y^2}{2}=-\dfrac{t^2}{2}+C'),
       S(r'**Condition:** $\frac{4}{2}=-\frac12+C$, so $C=\frac52$. Then multiply by 2.', r't^2+y^2=5'),
       S(r'**Solve for $y$.** Keep the $+$ root, since $y(1)=2$ is positive.', r'y=\sqrt{5-t^2}')],
      r'$y=\sqrt{5-t^2}$. It’s the top half of the circle $t^2+y^2=5$, so it only exists for $-\sqrt5<t<\sqrt5$.', cites=D.cite('T3', 1))
    P(D, 'W3 · A general solution with a power · lecture Example 3.2',
      r'Find the general solution of $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$.',
      [S(r'**Type:** $\dfrac{y^2}{t^3}=\dfrac{1}{t^3}\cdot y^2$, so separable with $g=t^{-3}$, $h=y^2$.'),
       S(r'**Separate:** divide by $y^2$, multiply by $dt$.', r'y^{-2}\,dy=t^{-3}\,dt'),
       S(r'**Integrate** with the power rule ($n=-2$ on the left, $n=-3$ on the right).', r'-y^{-1}=-\tfrac12t^{-2}+C'),
       S(r'**Solve for $y$:** multiply by $-1$ (and call $-C$ just $C$ again), then flip both sides.',
         r'\dfrac1y=\dfrac{1}{2t^2}+C\quad\Rightarrow\quad y=\dfrac{2t^2}{1+2Ct^2}')],
      r'$y=\dfrac{2t^2}{1+2Ct^2}$, plus $y=0$. We divided by $y^2$, which skips $y=0$ (see the warning above).', cites=W3(4))
    P(D, 'W3 · An exponential of y',
      r'Solve $\dfrac{dy}{dt}=2t\,e^{-y}$, $\;y(0)=0$.',
      [S(r'**Type:** $2t\cdot e^{-y}$ is a $t$-piece times a $y$-piece. Separable.'),
       S(r'**Separate:** dividing by $e^{-y}$ is the same as multiplying by $e^{y}$.', r'e^{y}\,dy=2t\,dt'),
       S(r'**Integrate** each side.', r'e^{y}=t^2+C'),
       S(r'**Condition:** $e^0=0+C$, so $C=1$.', r'e^{y}=t^2+1'),
       S(r'**Solve for $y$:** take $\ln$ of both sides.', r'y=\ln(t^2+1)')],
      r'$y=\ln(t^2+1)$.', diff='intermediate')
    P(D, 'W3 · Differential form · Pre-tutorial 3(b)',
      r'Solve $3t(y^2+1)\,dt+y(t^2+2)\,dy=0$.',
      [S(r'**Type:** each term is a $t$-piece times a $y$-piece. Separable.'),
       S(r'**Separate:** divide every term by $(y^2+1)(t^2+2)$. Now only $t$ sits with $dt$ and only $y$ with $dy$.',
         r'\dfrac{3t}{t^2+2}\,dt+\dfrac{y}{y^2+1}\,dy=0'),
       S(r'**Integrate:** both are “top = derivative of bottom”, times $\frac32$ and $\frac12$.', r'\tfrac32\ln(t^2+2)+\tfrac12\ln(y^2+1)=c'),
       S(r'Multiply by 2, then combine the logs: $3\ln A+\ln B=\ln(A^3B)$.', r'\ln\!\big[(t^2+2)^3(y^2+1)\big]=2c'),
       S(r'**Undo the $\ln$:** raise $e$ to both sides. $e^{2c}$ is a new constant $C$.', r'(t^2+2)^3(y^2+1)=C')],
      r'$(t^2+2)^3(y^2+1)=C$, with $C>0$. This implicit form is a full answer.', diff='intermediate', cites=D.cite('T3', 1))
    P(D, 'W3 · Collect before separating · lecture Example 3.4',
      r'Solve $y\,dt+(t^3y^2+t^3)\,dy=0$.',
      [S(r'**Type:** the $dy$ term has a common factor: $t^3y^2+t^3=t^3(y^2+1)$. So each term is a $t$-piece times a $y$-piece. Separable.'),
       S(r'**Separate:** divide every term by $t^3y$.', r't^{-3}\,dt+\dfrac{y^2+1}{y}\,dy=0'),
       S(r'Split the fraction so each part is easy to integrate: $\dfrac{y^2+1}{y}=y+\dfrac1y$.', r'\int t^{-3}\,dt+\int\left(y+\dfrac1y\right)dy=C'),
       S(r'**Integrate** each part.', r'-\dfrac{1}{2t^2}+\dfrac{y^2}{2}+\ln|y|=C'),
       S(r'Multiply by 2 to clear the fractions (call $2C$ the new constant $C_1$).', r'y^2+2\ln|y|-t^{-2}=C_1')],
      r'$y^2+2\ln|y|-t^{-2}=C_1$ (implicit), plus $y=0$, which we skipped by dividing by $y$.', diff='advanced', cites=W3(4))


def verify():
    assert implicit((3 + y ** 2) / (1 + t ** 2), t * (3 + y ** 2) / (y * (1 + t ** 2)), (1, 3)) == 6
    first(sp.sqrt(6 * t ** 2 + 3), t * (3 + y ** 2) / (y * (1 + t ** 2)), (1, 3))
    first(3 * sp.exp(t ** 2), 2 * t * y, (0, 3))
    first(sp.sqrt(5 - t ** 2), -t / y, (1, 2))
    C = sp.symbols('C')
    first(2 * t ** 2 / (1 + 2 * C * t ** 2), y ** 2 / t ** 3)
    first(sp.log(t ** 2 + 1), 2 * t * sp.exp(-y), (0, 0))
    implicit((t ** 2 + 2) ** 3 * (y ** 2 + 1), -3 * t * (y ** 2 + 1) / (y * (t ** 2 + 2)))
    implicit(y ** 2 + 2 * sp.log(y) - t ** -2, -y / (t ** 3 * y ** 2 + t ** 3))
    zero(sp.integrate(t / (t ** 2 + 1), t) - sp.log(t ** 2 + 1) / 2)
