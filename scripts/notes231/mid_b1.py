"""B1: separable equations (Week 3).

Layout (REWRITE_PLAN.md): use this when -> the form -> the move -> Why? box -> steps -> examples (cards) ->
integral cards -> traps -> practice. Shared letters across B1-B4: f(t) = a piece with only t, h(y) = a piece with
only y, C = the constant. Step words: Write, Separate, Integrate, Solve for y, Plug in.
"""
import sympy as sp

from midlib import CARD, P, S, TAGS, first, implicit, link, t, y, zero


def build(D):
    W3 = lambda *p: D.cite('W3', *p)
    D.H('B1 · Separable: a t-part times a y-part', level=2, cites=W3(4))
    TAGS(D, (3, 1))
    D.P(r'**Use this when** the right side splits into a $t$-part **times** a $y$-part, and you want $y(t)$:')
    D.EQ(r'\dfrac{dy}{dt}=2t\,y')
    D.P('Every separable equation has this shape:')
    D.EQ(r'\dfrac{dy}{dt}=f(t)\cdot h(y)')
    D.L([r'$f(t)$ = a piece with **only $t$** in it',
         r'$h(y)$ = a piece with **only $y$** in it'])
    D.P('**Short examples:**')
    D.EQ(r'\dfrac{dy}{dt}=\dfrac{y^2}{t^3}\quad\Longrightarrow\quad f=\dfrac{1}{t^3},\quad h=y^2')
    D.EQ(r'\dfrac{dy}{dt}=3y\quad\Longrightarrow\quad f=3,\quad h=y')
    D.P(r'No $t$ at all (like $3y$) is fine: $f$ is just a number.')
    D.P(r'**Not separable:** $\dfrac{dy}{dt}=t+y$. That’s a **sum**, and a sum won’t split into a product. Go to ' + link('B2', 'b2') + '.')

    D.P(r'**The move: put every $y$ with $dy$ and every $t$ with $dt$, then integrate both sides.**')
    D.EQ(r'\dfrac{dy}{dt}=2t\,y\quad\longrightarrow\quad \dfrac{dy}{y}=2t\,dt')
    D.P('In general:')
    D.EQ(r'\int\dfrac{dy}{h(y)}=\int f(t)\,dt+C')
    D.P('**Steps**')
    D.L([r'**Write** it as $\dfrac{dy}{dt}=f(t)\,h(y)$. Factor first if you have to.',
         r'**Separate:** divide by $h(y)$, multiply by $dt$. You get $\dfrac{dy}{h(y)}=f(t)\,dt$.',
         r'**Integrate** both sides. Write **one** constant $C$, on the $t$ side.',
         r'**Solve for $y$** if you can. If you can’t, the answer with $y$ mixed in (like $t^2+y^2=5$) is a full answer.',
         r'**Plug in** the condition, like $y(0)=3$, to find $C$.'], ordered=True)
    D.P('**Short example:**')
    D.EQ(r'\dfrac{dy}{y}=2t\,dt\quad\Longrightarrow\quad \ln|y|=t^2+C\quad\Longrightarrow\quad y=Ce^{t^2}')
    CARD(D, r'Full example: $\;\dfrac{dy}{dt}=2t\,y$, $\;y(0)=3$',
         [(r'**Write:** it’s $f(t)=2t$ times $h(y)=y$.', r'\dfrac{dy}{dt}=2t\cdot y'),
          (r'**Separate:** divide by $y$, multiply by $dt$.', r'\dfrac{dy}{y}=2t\,dt'),
          (r'**Integrate** each side. One constant, on the $t$ side.', r'\ln|y|=t^2+C'),
          (r'**Solve for $y$:** raise $e$ to both sides. $e^{t^2+C}=e^{C}e^{t^2}$, and $e^{C}$ is just a new constant: call it $C$ again.',
           r'y=C\,e^{t^2}'),
          (r'**Plug in** $y(0)=3$: $e^{0}=1$.', r'3=C')],
         r'y=3e^{t^2}')
    CARD(D, r'★ Lecture Example 3.3 (try it, then open): $\;\dfrac{dy}{dt}=\dfrac{3t+ty^2}{y+t^2y}$, $\;y(1)=3$',
         [(r'**Write:** pull $t$ out of the top and $y$ out of the bottom. Now it’s a $t$-part times a $y$-part.',
           r'\dfrac{dy}{dt}=\dfrac{t}{1+t^2}\cdot\dfrac{3+y^2}{y}'),
          (r'**Separate:** everything with $y$ goes with $dy$, everything with $t$ goes with $dt$.',
           r'\dfrac{y}{3+y^2}\,dy=\dfrac{t}{1+t^2}\,dt'),
          (r'**Integrate:** on each side the top is half the derivative of the bottom (integral card “top = derivative of bottom”).',
           r'\tfrac12\ln(3+y^2)=\tfrac12\ln(1+t^2)+C'),
          (r'**Solve for $y$:** multiply by $2$, raise $e$ to both sides. $e^{2C}$ is a new constant: call it $C$.',
           (r'3+y^2=C\,(1+t^2)',)),
          (r'**Plug in** $y(1)=3$.', (r'3+9=C\cdot2', r'C=6')),
          (r'Put $C=6$ back and take the $+$ root, because $y(1)=3$ is positive.', r'y^2=6t^2+3')],
         r'y=\sqrt{6t^2+3}')

    D.P('**Integrals that show up.** Open a card for an example:')
    CARD(D, r'Power rule: $\;\displaystyle\int t^n\,dt=\dfrac{t^{n+1}}{n+1}$ (any $n\neq-1$)',
         [(r'Add one to the power, divide by the new power. Works for negative powers too.', r'\int t^{-3}\,dt=\dfrac{t^{-2}}{-2}=-\dfrac{1}{2t^2}')])
    CARD(D, r'One over: $\;\displaystyle\int\dfrac{1}{y}\,dy=\ln|y|$',
         [(r'This is the $n=-1$ case the power rule skips.', r'\int\dfrac{dy}{y}=\ln|y|'),
          (r'Undo the $\ln$ with $e$: $e^{\ln A}=A$. A constant $e^{C}$ is just a new constant.', r'\ln|y|=t^2+C\quad\Longrightarrow\quad y=Ce^{t^2}')])
    CARD(D, r'Top = derivative of bottom: $\;\displaystyle\int\dfrac{f\prime(t)}{f(t)}\,dt=\ln|f(t)|$',
         [(r'The derivative of $t^2+1$ is $2t$. The top is only $t$, so you get half.', r'\int\dfrac{t}{t^2+1}\,dt=\tfrac12\ln(t^2+1)')])
    CARD(D, r'Exponential: $\;\displaystyle\int e^{at}\,dt=\dfrac1a\,e^{at}$',
         [(r'Divide by the number in front of $t$.', r'\int e^{2t}\,dt=\tfrac12e^{2t}')])
    CARD(D, r'Combine logs: $\;k\ln A+\ln B=\ln(A^kB)$',
         [(r'Pull the number up as a power, then multiply inside one $\ln$.', r'3\ln A+\ln B=\ln(A^3B)')])

    D.CO('warning', r'**Dividing by $h(y)$ can lose a solution.** If $h$ is $0$ at some number, that flat line is a solution too. '
         r'Example: in $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$, $h=y^2$ is $0$ at $y=0$, and $y=0$ works ($0=0$). List it next to your answer.')
    D.CO('warning', r'**Only one $C$.** Put it on the $t$ side right when you integrate. Two constants ($C_1$ left, $C_2$ right) are really one.')

    D.H('Practice: B1', level=3)
    P(D, '★ W3 · Separate and use a starting value · Pre-tutorial 3(a)',
      r'Solve $\dfrac{dy}{dt}=-\dfrac{t}{y}$, $\;y=2$ when $t=1$.',
      [S(r'**Type:** $-\dfrac{t}{y}=(-t)\cdot\dfrac1y$, a $t$-part times a $y$-part → B1.'),
       S(r'**Separate:** multiply both sides by $y\,dt$.', r'y\,dy=-t\,dt'),
       S(r'**Integrate** each side.', r'\dfrac{y^2}{2}=-\dfrac{t^2}{2}+C'),
       S(r'**Plug in** $t=1$, $y=2$.', (r'2=-\tfrac12+C\quad\Rightarrow\quad C=\tfrac52')),
       S(r'Put $C$ back and multiply by $2$.', r't^2+y^2=5'),
       S(r'**Solve for $y$.** Keep the $+$ root, since $y(1)=2$ is positive.', r'y=\sqrt{5-t^2}')],
      r'$y=\sqrt{5-t^2}$. It’s the top half of the circle $t^2+y^2=5$, so it only exists for $-\sqrt5<t<\sqrt5$.', cites=D.cite('T3', 1))
    P(D, '★ W3 · A general solution with a power · lecture Example 3.2',
      r'Find the general solution of $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$.',
      [S(r'**Type:** $\dfrac{y^2}{t^3}=\dfrac{1}{t^3}\cdot y^2$ → B1, with $f=t^{-3}$, $h=y^2$.'),
       S(r'**Separate:** divide by $y^2$, multiply by $dt$.', r'y^{-2}\,dy=t^{-3}\,dt'),
       S(r'**Integrate** with the power rule ($n=-2$ on the left, $n=-3$ on the right).', r'-y^{-1}=-\tfrac12t^{-2}+C'),
       S(r'**Solve for $y$:** multiply by $-1$ (call $-C$ just $C$ again).', r'\dfrac1y=\dfrac{1}{2t^2}+C=\dfrac{1+2Ct^2}{2t^2}'),
       S(r'Flip both sides.', r'y=\dfrac{2t^2}{1+2Ct^2}')],
      r'$y=\dfrac{2t^2}{1+2Ct^2}$, plus $y=0$. We divided by $y^2$, which skips $y=0$ (see the warning).', cites=W3(4))
    P(D, '★ W3 · Differential form · Pre-tutorial 3(b)',
      r'Solve $3t(y^2+1)\,dt+y(t^2+2)\,dy=0$.',
      [S(r'**Type:** each term is a $t$-part times a $y$-part → B1.'),
       S(r'**Separate:** divide every term by $(y^2+1)(t^2+2)$. Now only $t$ sits with $dt$, only $y$ with $dy$.',
         r'\dfrac{3t}{t^2+2}\,dt+\dfrac{y}{y^2+1}\,dy=0'),
       S(r'**Integrate:** both are “top = derivative of bottom”, times $\frac32$ and $\frac12$.', r'\tfrac32\ln(t^2+2)+\tfrac12\ln(y^2+1)=C'),
       S(r'Multiply by $2$, then combine the logs (card above).', r'\ln\!\big[(t^2+2)^3(y^2+1)\big]=2C'),
       S(r'Raise $e$ to both sides. $e^{2C}$ is a new constant: call it $C$.', r'(t^2+2)^3(y^2+1)=C')],
      r'$(t^2+2)^3(y^2+1)=C$, with $C>0$. You can’t easily get $y$ alone, so this is a full answer.', diff='intermediate', cites=D.cite('T3', 1))
    P(D, '★ W3 · Collect before separating · lecture Example 3.4',
      r'Solve $y\,dt+(t^3y^2+t^3)\,dy=0$.',
      [S(r'**Type:** the $dy$ term has a common factor, $t^3y^2+t^3=t^3(y^2+1)$. Now each term is a $t$-part times a $y$-part → B1.'),
       S(r'**Separate:** divide every term by $t^3y$.', r't^{-3}\,dt+\dfrac{y^2+1}{y}\,dy=0'),
       S(r'Split the fraction so each part is easy: $\dfrac{y^2+1}{y}=y+\dfrac1y$.', r'\int t^{-3}\,dt+\int\left(y+\dfrac1y\right)dy=C'),
       S(r'**Integrate** each part.', r'-\dfrac{1}{2t^2}+\dfrac{y^2}{2}+\ln|y|=C'),
       S(r'Multiply by $2$ to clear the fractions ($2C$ is a new $C$).', r'y^2+2\ln|y|-t^{-2}=C')],
      r'$y^2+2\ln|y|-t^{-2}=C$, plus $y=0$, which we skipped by dividing by $y$.', diff='advanced', cites=W3(4))


def verify():
    assert implicit((3 + y ** 2) / (1 + t ** 2), t * (3 + y ** 2) / (y * (1 + t ** 2)), (1, 3)) == 6
    first(sp.sqrt(6 * t ** 2 + 3), t * (3 + y ** 2) / (y * (1 + t ** 2)), (1, 3))
    first(3 * sp.exp(t ** 2), 2 * t * y, (0, 3))
    first(sp.sqrt(5 - t ** 2), -t / y, (1, 2))
    C = sp.symbols('C')
    first(C * sp.exp(t ** 2), 2 * t * y)
    first(2 * t ** 2 / (1 + 2 * C * t ** 2), y ** 2 / t ** 3)
    implicit((t ** 2 + 2) ** 3 * (y ** 2 + 1), -3 * t * (y ** 2 + 1) / (y * (t ** 2 + 2)))
    implicit(y ** 2 + 2 * sp.log(y) - t ** -2, -y / (t ** 3 * y ** 2 + t ** 3))
    zero(sp.integrate(t / (t ** 2 + 1), t) - sp.log(t ** 2 + 1) / 2)
    zero(sp.integrate(t ** -3, t) + 1 / (2 * t ** 2))
