"""B1: separable equations (Week 3)."""
import sympy as sp

from midlib import P, S, TAGS, first, implicit, link, t, y, zero


def build(D):
    W3 = lambda *p: D.cite('W3', *p)
    D.H('B1 · Separable equations', level=2, cites=W3(4))
    TAGS(D, (3, 1))
    D.P(r'**The simplest case.** If you can move every $y$ to one side and every $t$ to the other, you can integrate each side on its own.')
    D.P('A first-order ODE is **separable** when it can be written as:')
    D.EQ(r'\dfrac{dy}{dt}=g(t)\,h(y)')
    D.L([r'$g(t)$ = a part with only $t$ in it',
         r'$h(y)$ = a part with only $y$ in it'])
    D.P(r'Example: $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$ has $g=\dfrac{1}{t^3}$ and $h=y^2$. '
        r'Not separable: $\dfrac{dy}{dt}=t+y$, because a **sum** can’t be split into a product (that one goes to ' + link('B2', 'b2') + ').')
    D.P(r'An equation already written as $M(t)\,dt+N(y)\,dy=0$, with only $t$ in $M$ and only $y$ in $N$, is separated already.')

    D.P('**Method:**')
    D.L([r'**Separate:** divide by $h(y)$ and multiply by $dt$:  $\dfrac{dy}{h(y)}=g(t)\,dt$.',
         r'**Integrate** both sides. Write one constant $C$, on the $t$ side.',
         r'**Condition:** substitute the given point to find $C$.',
         r'**Solve for $y$** if you can. If you can’t, the implicit answer (like $y^2+3=6(t^2+1)$) is a full answer.'],
        ordered=True)
    D.P('**Calculus you need here:**')
    D.T(['Integral', 'Result', 'Note'], [
        [r'$\int t^n\,dt$', r'$\dfrac{t^{n+1}}{n+1}$', r'any $n\neq-1$, e.g. $\int t^{-3}dt=-\dfrac{1}{2t^2}$'],
        [r'$\int \dfrac1y\,dy$', r'$\ln|y|$', r'the $n=-1$ case'],
        [r'$\int \dfrac{f\prime(t)}{f(t)}\,dt$', r'$\ln|f(t)|$', r'spot “top = derivative of bottom”: $\int\dfrac{t}{t^2+1}dt=\dfrac12\ln(t^2+1)$'],
        [r'$\int e^{at}\,dt$', r'$\dfrac{1}{a}e^{at}$', ''],
        [r'undo $\ln$', r'$e^{\ln A}=A$', r'$e^{C}$ is just another constant; $\ln A+\ln B=\ln(AB)$'],
    ])
    D.CO('warning', r'**Dividing by $h(y)$ hides constant solutions.** If $h(y_0)=0$ for a number $y_0$, then $y=y_0$ is a solution too. '
         r'For $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$, $y=0$ is a solution that the separated formula misses.')
    D.CO('info', r'**Bonus (skip-safe): why separating is allowed.** Divide by $h$: $\dfrac{1}{h(y)}\dfrac{dy}{dt}=g(t)$. Integrate both sides with respect to $t$. '
         r'By the chain rule, $\int\dfrac{1}{h(y)}\dfrac{dy}{dt}\,dt=\int\dfrac{1}{h(y)}\,dy$. Writing “$dy$” and “$dt$” as separate pieces is shorthand for exactly this.')

    D.EX('W3 · Separate after factoring · lecture Example 3.3',
         r'Solve $\dfrac{dy}{dt}=\dfrac{3t+ty^2}{y+t^2y}$, $\;y(1)=3$.',
         [S(r'**Type:** factor top and bottom; it becomes $g(t)\,h(y)$, so separable.', r'\dfrac{dy}{dt}=\dfrac{t(3+y^2)}{y(1+t^2)}'),
          S(r'**Separate:** $y$’s left, $t$’s right.', r'\dfrac{y}{3+y^2}\,dy=\dfrac{t}{1+t^2}\,dt'),
          S(r'**Integrate:** both are “top = half the derivative of bottom”.', r'\tfrac12\ln(3+y^2)=\tfrac12\ln(1+t^2)+c'),
          S(r'Multiply by 2 and exponentiate; $e^{2c}$ becomes a new constant $C_1$.', r'3+y^2=C_1(1+t^2)'),
          S(r'**Condition** $y(1)=3$: $\;3+9=C_1(2)$.', r'C_1=6'),
          S(r'Solve for $y$; take the $+$ root because $y(1)=3>0$.', r'y^2=6t^2+3')],
         r'$y^2+3=6(t^2+1)$, i.e. $y=\sqrt{6t^2+3}$.', cites=W3(4))

    P(D, 'W3 · Separate and use a starting value · Pre-tutorial 3(a)',
      r'Solve $\dfrac{dy}{dt}=-\dfrac{t}{y}$, $\;y=2$ when $t=1$.',
      [S(r'**Type:** $-\dfrac{t}{y}=(-t)\cdot\dfrac1y$: separable.'),
       S(r'**Separate:** multiply by $y\,dt$.', r'y\,dy=-t\,dt'),
       S(r'**Integrate.**', r'\dfrac{y^2}{2}=-\dfrac{t^2}{2}+C'),
       S(r'**Condition:** $\frac{4}{2}=-\frac12+C$, so $C=\frac52$. Multiply by 2.', r't^2+y^2=5'),
       S(r'Solve for $y$, keeping the $+$ root since $y(1)=2>0$.', r'y=\sqrt{5-t^2}')],
      r'$y=\sqrt{5-t^2}$ (a circle of radius $\sqrt5$, upper half), valid for $-\sqrt5<t<\sqrt5$.', cites=D.cite('T3', 1))
    P(D, 'W3 · A general solution with a power · lecture Example 3.2',
      r'Find the general solution of $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$.',
      [S(r'**Type:** separable, $g=t^{-3}$, $h=y^2$.', r'y^{-2}\,dy=t^{-3}\,dt'),
       S(r'**Integrate** with the power rule ($n=-2$ and $n=-3$).', r'-y^{-1}=-\tfrac12t^{-2}+C'),
       S(r'Multiply by $-1$ and flip (rename $-C$ as $C$).', r'\dfrac1y=\dfrac{1}{2t^2}+C\quad\Rightarrow\quad y=\dfrac{2t^2}{1+2Ct^2}')],
      r'$\dfrac1y=\dfrac{1}{2t^2}+C$, i.e. $y=\dfrac{2t^2}{1+2Ct^2}$. Also $y=0$ (the constant solution lost by dividing by $y^2$).', cites=W3(4))
    P(D, 'W3 · An exponential of y',
      r'Solve $\dfrac{dy}{dt}=2t\,e^{-y}$, $\;y(0)=0$.',
      [S(r'**Type:** $2t\cdot e^{-y}$: separable. Dividing by $e^{-y}$ is multiplying by $e^{y}$.', r'e^{y}\,dy=2t\,dt'),
       S(r'**Integrate.**', r'e^{y}=t^2+C'),
       S(r'**Condition:** $e^0=0+C$, so $C=1$.', r'e^{y}=t^2+1'),
       S(r'Take $\ln$ of both sides.', r'y=\ln(t^2+1)')],
      r'$y=\ln(t^2+1)$.', diff='intermediate')
    P(D, 'W3 · Differential form · Pre-tutorial 3(b)',
      r'Solve $3t(y^2+1)\,dt+y(t^2+2)\,dy=0$.',
      [S(r'**Type:** each term is (t-part)(y-part), so dividing by $(y^2+1)(t^2+2)$ separates it.',
         r'\dfrac{3t}{t^2+2}\,dt+\dfrac{y}{y^2+1}\,dy=0'),
       S(r'**Integrate:** both are “top = derivative of bottom” (times $\frac32$ and $\frac12$).', r'\tfrac32\ln(t^2+2)+\tfrac12\ln(y^2+1)=c'),
       S(r'Multiply by 2, then combine the logs: $3\ln A+\ln B=\ln(A^3B)$.', r'\ln\!\big[(t^2+2)^3(y^2+1)\big]=2c'),
       S('Exponentiate.', r'(t^2+2)^3(y^2+1)=C')],
      r'$(t^2+2)^3(y^2+1)=C$ (implicit; $C>0$).', diff='intermediate', cites=D.cite('T3', 1))
    P(D, 'W3 · Collect before separating · lecture Example 3.4',
      r'Solve $y\,dt+(t^3y^2+t^3)\,dy=0$.',
      [S(r'**Type:** factor $t^3$ out of the $dy$ term: $y\,dt+t^3(y^2+1)\,dy=0$. Dividing by $t^3y$ separates it.',
         r't^{-3}\,dt+\dfrac{y^2+1}{y}\,dy=0'),
       S(r'Split the fraction: $\dfrac{y^2+1}{y}=y+\dfrac1y$.', r'\int t^{-3}\,dt+\int\left(y+\dfrac1y\right)dy=C'),
       S(r'**Integrate.**', r'-\dfrac{1}{2t^2}+\dfrac{y^2}{2}+\ln|y|=C'),
       S('Multiply by 2 (rename $2C$ as $C_1$).', r'y^2+2\ln|y|-t^{-2}=C_1')],
      r'$y^2+2\ln|y|-t^{-2}=C_1$ (implicit), plus the constant solution $y=0$.', diff='advanced', cites=W3(4))


def verify():
    assert implicit((3 + y ** 2) / (1 + t ** 2), t * (3 + y ** 2) / (y * (1 + t ** 2)), (1, 3)) == 6
    first(sp.sqrt(6 * t ** 2 + 3), t * (3 + y ** 2) / (y * (1 + t ** 2)), (1, 3))
    first(sp.sqrt(5 - t ** 2), -t / y, (1, 2))
    C = sp.symbols('C')
    first(2 * t ** 2 / (1 + 2 * C * t ** 2), y ** 2 / t ** 3)
    first(sp.log(t ** 2 + 1), 2 * t * sp.exp(-y), (0, 0))
    implicit((t ** 2 + 2) ** 3 * (y ** 2 + 1), -3 * t * (y ** 2 + 1) / (y * (t ** 2 + 2)))
    implicit(y ** 2 + 2 * sp.log(y) - t ** -2, -y / (t ** 3 * y ** 2 + t ** 3))
    zero(sp.integrate(t / (t ** 2 + 1), t) - sp.log(t ** 2 + 1) / 2)
