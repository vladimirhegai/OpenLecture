"""B5: second-order linear homogeneous equations with constant coefficients (Weeks 4-5).

Layout (REWRITE_PLAN.md): use this when -> the move -> Why? box -> steps -> Case 1/2/3 (formula, short example,
full example in a closed card) -> traps and shortcut cards -> practice. Every solution uses the step words
Write/Solve/Pick/Differentiate/Plug in. Give the math room: one step per line, equations centred.
"""
import sympy as sp

from midlib import CARD, P, S, TAGS, link, second, t, zero


def build(D):
    D.H('B5 · Second order, numbers in front, right side 0', level=2)
    TAGS(D, (5, 1))
    D.P(r'**Use this when** the equation looks like this, and you want $y(t)$:')
    D.EQ(r'y\prime\prime+3y\prime+2y=0')
    D.P(r'That is: a $y\prime\prime$, plain numbers in front of $y\prime\prime$, $y\prime$ and $y$, and $0$ on the right.')
    D.L([r'Right side not $0$, like $y\prime\prime+y=3$? → ' + link('B6', 'b6') + '.',
         r'$t$ in front, like $ty\prime\prime+y=0$? → ' + link('B7', 'b7') + '.'])

    D.P(r'**The move: turn the ODE into a quadratic.**')
    D.P(r'Swap $y\prime\prime\to s^2$, $y\prime\to s$, $y\to1$. Keep the numbers in front.')
    D.EQ(r'y\prime\prime+3y\prime+2y=0\quad\longrightarrow\quad s^2+3s+2=0')
    D.P('Two more:')
    D.EQ(r'4y\prime\prime+4y\prime+y=0\quad\longrightarrow\quad 4s^2+4s+1=0')
    D.EQ(r'y\prime\prime+9y=0\quad\longrightarrow\quad s^2+9=0')
    D.P(r'No $y\prime$ means no $s$ term. This quadratic is called the **characteristic equation**.')
    D.WHY('Why are we allowed to do this?',
          r'Guess $y=e^{st}$. Each derivative pulls out one more $s$:'
          '\n\n$$\n' r'y\prime=s\,e^{st},\qquad y\prime\prime=s^2e^{st}' '\n$$\n\n'
          r'Plug them into $y\prime\prime+3y\prime+2y=0$:'
          '\n\n$$\n' r's^2e^{st}+3s\,e^{st}+2e^{st}=0' '\n$$\n\n'
          r'Pull out the $e^{st}$:'
          '\n\n$$\n' r'(s^2+3s+2)\,e^{st}=0' '\n$$\n\n'
          r'$e^{st}$ is never $0$, so the bracket must be $0$. That bracket is the quadratic.'
          '\n\n'
          r'So every root $s$ gives a solution $e^{st}$. Two roots give two solutions, and the general solution is $c_1$ times one plus $c_2$ times the other.')

    D.P('**Steps**')
    D.L([r'**Write** the quadratic: $as^2+bs+c=0$.',
         r'**Solve** it. Factor if you can. If not, use the quadratic formula (below).',
         r'**Pick** the case from what the roots look like. It tells you the form of $y$.',
         r'**Differentiate** $y$ to get $y\prime$ (only if they give you $y\prime(0)$).',
         r'**Plug in** $t=0$: $y(0)$ and $y\prime(0)$ give two equations. Solve them for $c_1$ and $c_2$.'], ordered=True)
    D.P('The quadratic formula:')
    D.EQ(r's=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}')
    D.P(r'The number under the root, $b^2-4ac$, tells you the case:')
    D.T([r'$b^2-4ac$', 'Roots', 'Go to'], [
        [r'$>0$', 'two different real numbers', 'Case 1'],
        [r'$=0$', 'one number, twice', 'Case 2'],
        [r'$<0$', r'a complex pair ($\pm j$)', 'Case 3'],
    ])

    D.H('Case 1: two different real roots', level=3)
    D.P(r'The quadratic gives two different numbers, $s_1$ and $s_2$.')
    D.P('Each one gives an exponential:')
    D.EQ(r'y=c_1e^{s_1t}+c_2e^{s_2t}')
    D.P('**Short example:**')
    D.EQ(r's=-1,\ -2\quad\Longrightarrow\quad y=c_1e^{-t}+c_2e^{-2t}')
    CARD(D, r'Full example: $\;y\prime\prime+3y\prime+2y=0$, $\;y(0)=1$, $\;y\prime(0)=0$',
         [(r'**Write** the quadratic.', r's^2+3s+2=0'),
          (r'**Solve:** it factors. Two numbers that multiply to $2$ and add to $3$: $1$ and $2$.',
           (r'(s+1)(s+2)=0', r's_1=-1,\qquad s_2=-2')),
          (r'**Pick:** two different real roots, so Case 1.', r'y=c_1e^{-t}+c_2e^{-2t}'),
          (r'**Differentiate:** the derivative of $e^{kt}$ is $k\,e^{kt}$.', r'y\prime=-c_1e^{-t}-2c_2e^{-2t}'),
          (r'**Plug in** $t=0$. Every $e^{0}=1$.', (r'y(0)=c_1+c_2=1', r'y\prime(0)=-c_1-2c_2=0')),
          (r'**Solve for $c_1$ and $c_2$:** add the two equations. The $c_1$’s cancel.', (r'-c_2=1\quad\Rightarrow\quad c_2=-1', r'c_1=1-c_2=2'))],
         r'y=2e^{-t}-e^{-2t}')

    D.H('Case 2: one repeated root', level=3)
    D.P(r'The quadratic gives the same number $s$ twice.')
    D.P(r'$c_1e^{st}+c_2e^{st}$ would really be just one term. So the second piece gets an extra $t$:')
    D.EQ(r'y=(c_1+c_2t)\,e^{st}')
    D.P('**Short example:**')
    D.EQ(r's=-2\ \text{(twice)}\quad\Longrightarrow\quad y=(c_1+c_2t)\,e^{-2t}')
    CARD(D, r'Full example: $\;y\prime\prime+4y\prime+4y=0$, $\;y(0)=1$, $\;y\prime(0)=1$',
         [(r'**Write** the quadratic.', r's^2+4s+4=0'),
          (r'**Solve:** it’s a perfect square. (Check: $b^2-4ac=16-16=0$, so Case 2.)',
           (r'(s+2)^2=0', r's=-2\ \text{(twice)}')),
          (r'**Pick:** repeated root, so Case 2.', r'y=(c_1+c_2t)\,e^{-2t}'),
          (r'**Differentiate** with the product rule: (front)$\prime$ times $e^{-2t}$, plus front times $(e^{-2t})\prime$.',
           r'y\prime=c_2\,e^{-2t}-2(c_1+c_2t)\,e^{-2t}'),
          (r'**Plug in** $t=0$. The $c_2t$ becomes $0$, and $e^{0}=1$.', (r'y(0)=c_1=1', r'y\prime(0)=c_2-2c_1=1')),
          (r'**Solve for $c_1$ and $c_2$:** put $c_1=1$ into the second equation.', r'c_2-2=1\quad\Rightarrow\quad c_2=3')],
         r'y=(1+3t)\,e^{-2t}')
    D.WHY('Why the extra $t$?',
          r'$c_1e^{st}$ and $c_2e^{st}$ are the same function, so together they only give one constant. You need a second, different solution.'
          '\n\n'
          r'When the root is repeated, $te^{st}$ also solves the ODE. Check with $y=te^{-2t}$ in $y\prime\prime+4y\prime+4y$: you get $0$.'
          '\n\n'
          r'It comes from reduction of order: see the first practice problem in ' + link('B7', 'b7') + '.')

    D.H('Case 3: complex roots', level=3)
    D.P(r'The number under the square root is negative. That’s fine.')
    D.P(r'Pull out a $j$, where $j=\sqrt{-1}$:')
    D.EQ(r'\sqrt{-16}=\sqrt{16}\cdot\sqrt{-1}=4j')
    D.P(r'So the two roots come out as a pair: the same real part, and $\pm$ a $j$ part.')
    D.EQ(r's=\sigma\pm j\omega')
    D.L([r'$\sigma$ (“sigma”) = the **real part**: the number without $j$.',
         r'$\omega$ (“omega”) = the **$j$ part**: the number next to $j$, without the $\pm$.'])
    D.P('For example:')
    D.EQ(r's=-1\pm j2\quad\Longrightarrow\quad \sigma=-1,\quad \omega=2')
    D.P(r'The answer has **no $j$ in it**. The real part goes in the exponential. The $j$ part goes inside $\cos$ and $\sin$:')
    D.EQ(r'y=e^{\sigma t}\,(c_1\cos\omega t+c_2\sin\omega t)')
    D.P('**Short example:**')
    D.EQ(r's=-1\pm j2\quad\Longrightarrow\quad y=e^{-t}(c_1\cos2t+c_2\sin2t)')
    CARD(D, r'Full example: $\;y\prime\prime+2y\prime+5y=0$, $\;y(0)=1$, $\;y\prime(0)=1$',
         [(r'**Write** the quadratic.', r's^2+2s+5=0'),
          (r'**Solve:** it doesn’t factor, so use the formula with $a=1$, $b=2$, $c=5$. Start with the part under the root. It’s negative, so Case 3.',
           (r'b^2-4ac=4-20=-16', r'\sqrt{-16}=j4', r's=\dfrac{-2\pm j4}{2}=-1\pm j2')),
          (r'**Pick:** Case 3 with real part $\sigma=-1$ and $j$ part $\omega=2$.', r'y=e^{-t}(c_1\cos2t+c_2\sin2t)'),
          (r'**Differentiate** with the product rule: $(e^{-t})\prime$ times the bracket, plus $e^{-t}$ times (the bracket)$\prime$.',
           r'\begin{aligned}y\prime&=-e^{-t}(c_1\cos2t+c_2\sin2t)\\&\quad+e^{-t}(-2c_1\sin2t+2c_2\cos2t)\end{aligned}'),
          (r'**Plug in** $t=0$: $e^{0}=1$, $\cos0=1$, $\sin0=0$.', (r'y(0)=c_1=1', r'y\prime(0)=-c_1+2c_2=1')),
          (r'**Solve for $c_1$ and $c_2$:** put $c_1=1$ into the second equation.', r'2c_2=2\quad\Rightarrow\quad c_2=1')],
         r'y=e^{-t}(\cos2t+\sin2t)')
    D.P(r'**No $y\prime$ term?** Like $y\prime\prime+9y=0$:')
    D.EQ(r's^2+9=0\quad\Longrightarrow\quad s^2=-9\quad\Longrightarrow\quad s=\pm j3')
    D.P(r'So $\sigma=0$ and $\omega=3$. Since $e^{0t}=1$, the exponential disappears:')
    D.EQ(r'y=c_1\cos3t+c_2\sin3t')
    D.WHY('Why $\\cos$ and $\\sin$, and where did the $j$ go?',
          r'The two roots give $e^{(\sigma+j\omega)t}$ and $e^{(\sigma-j\omega)t}$. Euler’s formula splits each one:'
          '\n\n$$\n' r'e^{(\sigma\pm j\omega)t}=e^{\sigma t}\,(\cos\omega t\pm j\sin\omega t)' '\n$$\n\n'
          r'Adding and subtracting the two solutions cancels the $j$’s. What’s left is $e^{\sigma t}\cos\omega t$ and $e^{\sigma t}\sin\omega t$.'
          '\n\n'
          r'Both are real solutions, so the general solution is $c_1$ times one plus $c_2$ times the other.')

    D.H('Traps and a quick check', level=3)
    D.CO('warning', r'**Differentiate first, then plug in $t=0$.** In Cases 2 and 3 the product rule gives an extra term. '
         r'Skip it and you get the wrong $c_2$. Example: in Case 2 above, $y\prime(0)=c_2-2c_1$, not just $c_2$.')
    D.CO('warning', r'**$\sigma$ keeps its sign.** $s=-1\pm j2$ gives $e^{-t}$, not $e^{t}$. Only $\omega$ drops the sign.')
    D.P(r'**Shortcut to check $c_1$ and $c_2$.** At $t=0$, each case always gives the same two equations. Open a card for a short example.')
    D.P(r'(Only for conditions at $t=0$. At another time, like $y(1)$, differentiate yourself.)')
    CARD(D, r'Case 1: $\;y(0)=c_1+c_2,\quad y\prime(0)=s_1c_1+s_2c_2$',
         [(r'Roots $-2$ and $-3$, with $y(0)=2$ and $y\prime(0)=-5$. Case 1:', r'y=c_1e^{-2t}+c_2e^{-3t}'),
          (r'$y(0)$: just add the constants.', r'c_1+c_2=2'),
          (r'$y\prime(0)$: each root times its constant.', r'-2c_1-3c_2=-5'),
          (r'Multiply the first by $2$ and add: $-c_2=-1$.', (r'c_2=1', r'c_1=1')),
          (r'Where it comes from: differentiate, then every $e^{0}=1$.', r'y\prime=s_1c_1e^{s_1t}+s_2c_2e^{s_2t}\quad\Rightarrow\quad y\prime(0)=s_1c_1+s_2c_2')])
    CARD(D, r'Case 2: $\;y(0)=c_1,\quad y\prime(0)=sc_1+c_2$',
         [(r'Root $-\tfrac12$ twice, with $y(0)=4$ and $y\prime(0)=0$. Case 2:', r'y=(c_1+c_2t)\,e^{-t/2}'),
          (r'$y(0)$: the $c_2t$ is $0$ at $t=0$.', r'c_1=4'),
          (r'$y\prime(0)$: the root times $c_1$, plus $c_2$.', r'-\tfrac12c_1+c_2=0'),
          (r'Put in $c_1=4$: $-2+c_2=0$.', r'c_2=2'),
          (r'Where it comes from: the product rule, then $t=0$.', r'y\prime=c_2e^{st}+s(c_1+c_2t)e^{st}\quad\Rightarrow\quad y\prime(0)=c_2+sc_1')])
    CARD(D, r'Case 3: $\;y(0)=c_1,\quad y\prime(0)=\sigma c_1+\omega c_2$',
         [(r'Roots $-3\pm j4$, so $\sigma=-3$ and $\omega=4$, with $y(0)=0$ and $y\prime(0)=8$. Case 3:', r'y=e^{-3t}(c_1\cos4t+c_2\sin4t)'),
          (r'$y(0)$: $\cos0=1$ and $\sin0=0$.', r'c_1=0'),
          (r'$y\prime(0)$: $\sigma$ times $c_1$, plus $\omega$ times $c_2$.', r'-3c_1+4c_2=8'),
          (r'Put in $c_1=0$: $4c_2=8$.', r'c_2=2'),
          (r'Where it comes from: the product rule, then $t=0$. The $\sin0=0$ wipes out two of the terms.', r'y\prime(0)=\sigma c_1+\omega c_2')])
    D.GRAPH(r'''
    title "Slide $k$ through 1: the same start, all three cases"
    x 0 8 label="$t$"
    y -0.6 1.2 label="$y$"
    slider k 0 5 0.5 step=0.05 label="$k$" animate
    let d "sqrt(abs(1-k))"
    let s1 "-1+d"
    let s2 "-1-d"
    curve "if(k<0.999, (s2*exp(s1*x)-s1*exp(s2*x))/(s2-s1), if(k>1.001, exp(-x)*(cos(d*x)+sin(d*x)/d), (1+x)*exp(-x)))" label="$y(t)$" color=1
    hline "0"
    readout "$b^2-4ac=4-4k$" "4-4*k"
    caption "$y\prime\prime+2y\prime+ky=0$, starting at $y(0)=1$, $y\prime(0)=0$. $k<1$: Case 1, it settles with no wiggle. $k=1$: Case 2, the border. $k>1$: Case 3, it wiggles while $e^{-t}$ shrinks it. Same three cases as an RLC circuit in D2."
    ''', intro=r'**What do the three cases look like?**')

    D.H('Practice: B5', level=3)
    P(D, 'W5 · Two different real roots',
      r'Solve $y\prime\prime+5y\prime+6y=0$, $\;y(0)=2$, $y\prime(0)=-5$.',
      [S(r'**Type:** second order, numbers in front, right side $0$ → B5.'),
       S(r'**Write** the quadratic.', r's^2+5s+6=0'),
       S(r'**Solve:** two numbers that multiply to $6$ and add to $5$: $2$ and $3$.', r'(s+2)(s+3)=0\quad\Rightarrow\quad s=-2,\,-3'),
       S(r'**Pick:** two different real roots → Case 1.', r'y=c_1e^{-2t}+c_2e^{-3t}'),
       S(r'**Differentiate.**', r'y\prime=-2c_1e^{-2t}-3c_2e^{-3t}'),
       S(r'**Plug in** $t=0$.', r'c_1+c_2=2,\qquad -2c_1-3c_2=-5'),
       S(r'Multiply the first equation by $2$ and add the second: $-c_2=-1$.', r'c_2=1,\qquad c_1=1')],
      r'$y=e^{-2t}+e^{-3t}$.')
    P(D, 'W5 · A repeated root',
      r'Solve $4y\prime\prime+4y\prime+y=0$, $\;y(0)=4$, $y\prime(0)=0$.',
      [S(r'**Type:** second order, numbers in front, right side $0$ → B5.'),
       S(r'**Write** the quadratic.', r'4s^2+4s+1=0'),
       S(r'**Solve:** $b^2-4ac=16-16=0$, so one root. The formula gives $s=\frac{-4}{8}$.', r's=-\tfrac12\ \text{(twice)}'),
       S(r'**Pick:** repeated root → Case 2.', r'y=(c_1+c_2t)\,e^{-t/2}'),
       S(r'**Differentiate** with the product rule.', r'y\prime=c_2e^{-t/2}-\tfrac12(c_1+c_2t)\,e^{-t/2}'),
       S(r'**Plug in** $t=0$.', r'c_1=4,\qquad c_2-\tfrac12c_1=0'),
       S(r'Put $c_1=4$ into the second equation.', r'c_2=2')],
      r'$y=(4+2t)\,e^{-t/2}$.')
    P(D, 'W5 · No damping term',
      r'Solve $y\prime\prime+9y=0$, $\;y(0)=2$, $y\prime(0)=3$.',
      [S(r'**Type:** second order, numbers in front, right side $0$ → B5.'),
       S(r'**Write** the quadratic. No $y\prime$, so no $s$ term.', r's^2+9=0'),
       S(r'**Solve:** $s^2=-9$, and $\sqrt{-9}=j3$.', r's=\pm j3'),
       S(r'**Pick:** Case 3 with $\sigma=0$, $\omega=3$. $e^{0t}=1$, so no exponential.', r'y=c_1\cos3t+c_2\sin3t'),
       S(r'**Differentiate.**', r'y\prime=-3c_1\sin3t+3c_2\cos3t'),
       S(r'**Plug in** $t=0$: $\cos0=1$, $\sin0=0$.', r'c_1=2,\qquad 3c_2=3\ \Rightarrow\ c_2=1')],
      r'$y=2\cos3t+\sin3t$. Nothing shrinks it, so it swings forever: that’s the ideal LC circuit in ' + link('D2', 'd2') + '.',
      diff='intermediate')
    P(D, 'W5 · Work backwards from the roots',
      r'A constant-coefficient equation $y\prime\prime+by\prime+cy=0$ has roots $-3\pm j4$. ' '\n\n'
      r'(a) Find $b$ and $c$. (b) Write the general solution. (c) Find the solution with $y(0)=0$, $y\prime(0)=8$.',
      [S(r'**Type:** backwards. Roots $s_1$, $s_2$ come from the quadratic $(s-s_1)(s-s_2)=0$.'),
       S(r'(a) Multiply out. The brackets are $(s+3)-j4$ and $(s+3)+j4$: a difference of squares. And $(j4)^2=16j^2=-16$.',
         r'(s+3)^2-(j4)^2=s^2+6s+9+16=s^2+6s+25'),
       S(r'So $b=6$ and $c=25$.', r'y\prime\prime+6y\prime+25y=0'),
       S(r'(b) **Pick:** Case 3 with $\sigma=-3$, $\omega=4$.', r'y=e^{-3t}(c_1\cos4t+c_2\sin4t)'),
       S(r'(c) **Differentiate** with the product rule.', r'y\prime=-3e^{-3t}(c_1\cos4t+c_2\sin4t)+e^{-3t}(-4c_1\sin4t+4c_2\cos4t)'),
       S(r'**Plug in** $t=0$.', r'c_1=0,\qquad -3c_1+4c_2=8\ \Rightarrow\ c_2=2')],
      r'(a) $b=6$, $c=25$. (b) $y=e^{-3t}(c_1\cos4t+c_2\sin4t)$. (c) $y=2e^{-3t}\sin4t$.', diff='advanced')


def verify():
    A, B = sp.symbols('A B')
    E = sp.exp
    # check table: y(0) and y'(0) of each form
    s1, s2, s, sg, w = sp.symbols('s1 s2 s sigma omega')
    for form, y0, dy0 in ((A * E(s1 * t) + B * E(s2 * t), A + B, s1 * A + s2 * B),
                          ((A + B * t) * E(s * t), A, s * A + B),
                          (E(sg * t) * (A * sp.cos(w * t) + B * sp.sin(w * t)), A, sg * A + w * B)):
        zero(form.subs(t, 0) - y0)
        zero(sp.diff(form, t).subs(t, 0) - dy0)
    # derivatives written out in the examples and problems
    zero(sp.diff((A + B * t) * E(-2 * t), t) - (B * E(-2 * t) - 2 * (A + B * t) * E(-2 * t)))
    zero(sp.diff(E(-t) * (A * sp.cos(2 * t) + B * sp.sin(2 * t)), t)
         - (-E(-t) * (A * sp.cos(2 * t) + B * sp.sin(2 * t)) + E(-t) * (-2 * A * sp.sin(2 * t) + 2 * B * sp.cos(2 * t))))
    zero(sp.diff((A + B * t) * E(-t / 2), t) - (B * E(-t / 2) - (A + B * t) * E(-t / 2) / 2))
    zero(sp.diff(E(-3 * t) * (A * sp.cos(4 * t) + B * sp.sin(4 * t)), t)
         - (-3 * E(-3 * t) * (A * sp.cos(4 * t) + B * sp.sin(4 * t)) + E(-3 * t) * (-4 * A * sp.sin(4 * t) + 4 * B * sp.cos(4 * t))))
    second(t * E(-2 * t), 1, 4, 4)  # the Why? box claim
    # graph formulas: y'' + 2y' + k y = 0, y(0)=1, y'(0)=0 in all three cases
    for k in (sp.Rational(1, 2), 0):
        d = sp.sqrt(1 - k)
        r1, r2 = -1 + d, -1 - d
        second((r2 * E(r1 * t) - r1 * E(r2 * t)) / (r2 - r1), 1, 2, k, initial=(0, 1, 0))
    second((1 + t) * E(-t), 1, 2, 1, initial=(0, 1, 0))
    for k in (2, 5):
        d = sp.sqrt(k - 1)
        second(E(-t) * (sp.cos(d * t) + sp.sin(d * t) / d), 1, 2, k, initial=(0, 1, 0))
    # case examples
    second(2 * E(-t) - E(-2 * t), 1, 3, 2, initial=(0, 1, 0))
    second((1 + 3 * t) * E(-2 * t), 1, 4, 4, initial=(0, 1, 1))
    second(E(-t) * (sp.cos(2 * t) + sp.sin(2 * t)), 1, 2, 5, initial=(0, 1, 1))
    # problems
    second(E(-2 * t) + E(-3 * t), 1, 5, 6, initial=(0, 2, -5))
    second((4 + 2 * t) * E(-t / 2), 4, 4, 1, initial=(0, 4, 0))
    second(2 * sp.cos(3 * t) + sp.sin(3 * t), 1, 0, 9, initial=(0, 2, 3))
    zero(sp.expand((s + 3 + 4 * sp.I) * (s + 3 - 4 * sp.I)) - (s ** 2 + 6 * s + 25))
    second(2 * E(-3 * t) * sp.sin(4 * t), 1, 6, 25, initial=(0, 0, 8))
