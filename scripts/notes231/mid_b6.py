"""B6: undetermined coefficients for a(y'') + b y' + c y = g(t) (Week 6)."""
import sympy as sp

from midlib import P, S, TAGS, link, second, t, zero


def build(D):
    W6 = lambda *p: D.cite('W6', *p)
    D.H('B6 · Undetermined coefficients', level=2, cites=W6(3, 4) + D.cite('N6', 1))
    TAGS(D, (6, 2))
    D.P(r'**What if the right side isn’t zero?** The forcing $g(t)$ (a source, in a circuit) pushes the solution. '
        r'The ' + link('B5', 'b5') + r' solutions only ever produce $0$ on the right, so they need a partner that produces $g(t)$.')
    D.P('Second-order linear equations with constant coefficients and a forcing term look like:')
    D.EQ(r'a\,y\prime\prime+b\,y\prime+c\,y=g(t)')
    D.L([r'left side = the same as in B5 (numbers $a,b,c$)',
         r'$g(t)$ = the **forcing**: everything with no $y$ in it, moved to the right'])
    D.P('The solution is always built from two pieces:')
    D.EQ(r'y=y_c+y_p')
    D.L([r'$y_c$ = the **complementary solution**: the general solution with $g$ replaced by $0$ (that is ' + link('B5', 'b5') + r'). It holds the two constants $c_1,c_2$.',
         r'$y_p$ = a **particular solution**: any one function that produces $g(t)$. No constants.'])
    D.P(r'Mini example: $y\prime\prime+y=3$. Then $y_c=c_1\sin t+c_2\cos t$, and $y_p=3$ works ($0+3=3$). So $y=3+c_1\sin t+c_2\cos t$.')

    D.P(r'**Finding $y_p$: guess its form from $g(t)$.** Write a guess with unknown coefficients ($A,B,\dots$), substitute it, and match coefficients. '
        r'The guess copies the shape of $g$:')
    D.T([r'Term in $g(t)$', r'Guess for $y_p$'], [
        [r'constant, or polynomial of degree $n$', r'$A_nt^n+\dots+A_1t+A_0$ (**all** lower powers)'],
        [r'$e^{at}$', r'$Ae^{at}$'],
        [r'$\sin rt$ or $\cos rt$', r'$A\cos rt+B\sin rt$ (**always both**)'],
        [r'$e^{at}\cos rt$ or $e^{at}\sin rt$', r'$e^{at}(A\cos rt+B\sin rt)$'],
        ['a sum of these', 'the sum of their guesses'],
    ], cites=D.cite('N6', 1))
    D.CO('warning', r'**The $\times t$ rule.** If any term of your guess already appears in $y_c$, substituting it gives $0$, so it can never produce $g$. '
         r'**Multiply that guess by $t$.** If it is still in $y_c$ (a repeated root), multiply by $t^2$.')
    D.P('**Method:**')
    D.L([r'**Complementary:** solve the equation with $g=0$ (' + link('B5', 'b5') + r') to get $y_c$.',
         r'**Guess:** take $y_p$’s form from the table. Compare it with $y_c$; apply the $\times t$ rule if needed.',
         r'**Substitute** $y_p$ into the ODE and **match coefficients** (constants, each $\cos$, each $\sin$, each power of $t$). Solve for $A,B,\dots$',
         r'**Add:** $y=y_c+y_p$.',
         r'**Conditions** on the **whole** $y$, never on $y_c$ or $y_p$ alone.'],
        ordered=True)
    D.P('**Calculus you need here:**')
    D.T(['Expression', 'Result', 'Note'], [
        [r'$\cos^2t$', r'$\tfrac12+\tfrac12\cos2t$', 'remove squares before guessing'],
        [r'$\sin^2t$', r'$\tfrac12-\tfrac12\cos2t$', ''],
        [r'$(A\cos rt+B\sin rt)\prime\prime$', r'$-r^2(A\cos rt+B\sin rt)$', 'each derivative brings out an $r$'],
        [r'$(te^{at})\prime$', r'$(1+at)\,e^{at}$', 'product rule'],
        [r'$(t\,f)\prime\prime$', r'$t\,f\prime\prime+2f\prime$', r'product rule twice, for a $\times t$ guess'],
    ])
    D.CO('info', r'**Bonus (skip-safe): why $y=y_c+y_p$ works.** The left side is linear: put in $y_c+y_p$ and you get (what $y_c$ gives) + (what $y_p$ gives) $=0+g=g$. '
         r'And $y_c$ still carries two free constants, enough to meet any two conditions. '
         r'The $\times t$ rule has the same root: a term of $y_c$ gives $0$ on the left, so it is useless as a guess.')

    D.EX('W6 · The tutorial problem, with two boundary values · Week 6 tutorial, lecture notes p. 3–4',
         r"Solve $\ddot y+y=6\cos^2t$ with $y(0)=0$ and $y(\pi/2)=0$. The tutorial gives the forms $y_c=c_1\sin t+c_2\cos t$ and $y_p=A+B\cos2t+D\sin2t$. "
         r'($\ddot y$ is the professor’s notation for $y\prime\prime$.)',
         [S(r'**Type:** constant coefficients with forcing $6\cos^2t$. **Complementary:** $s^2+1=0$ gives $s=\pm j$.', r'y_c=c_1\sin t+c_2\cos t'),
          S(r'Remove the square with the identity, so the guess table applies.', r'6\cos^2t=3+3\cos2t'),
          S(r'**Guess:** constant → $A$; $\cos2t$ → both $\cos2t$ and $\sin2t$. None of them is in $y_c$.', r'y_p=A+B\cos2t+D\sin2t'),
          S(r'Differentiate twice: each derivative brings out a 2.', r"y_p''=-4B\cos2t-4D\sin2t"),
          S(r'**Substitute** $y_p\prime\prime+y_p$ and collect.', r'A-3B\cos2t-3D\sin2t=3+3\cos2t'),
          S('**Match** constants, cosines and sines.', r'A=3,\qquad B=-1,\qquad D=0'),
          S(r'**Add** $y_c$ **before** using the conditions: they apply to the whole $y$.', r'y=3-\cos2t+c_1\sin t+c_2\cos t'),
          S(r'**Condition** $y(0)=0$: $\sin0=0$, $\cos0=1$.', r'3-1+c_2=0\quad\Rightarrow\quad c_2=-2'),
          S(r'**Condition** $y(\pi/2)=0$: $\cos\pi=-1$, $\sin\frac\pi2=1$, $\cos\frac\pi2=0$.', r'3+1+c_1=0\quad\Rightarrow\quad c_1=-4')],
         r'$y=3-\cos2t-4\sin t-2\cos t$.', cites=D.cite('T6', 1) + W6(3, 4))
    D.GRAPH(r'''
    title "Tutorial problem: pick the constants"
    x 0 6.3 label="$t$"
    y -8 8 label="$y$"
    slider c1 -6 6 0 step=0.5 label="$c_1$"
    slider c2 -6 6 0 step=0.5 label="$c_2$"
    curve "3-cos(2*x)" label="$y_p=3-\cos2t$" color=0 dash
    curve "3-cos(2*x)+c1*sin(x)+c2*cos(x)" label="$y=y_p+c_1\sin t+c_2\cos t$" color=1
    point "0" "0" label="must pass $(0,0)$" color=3
    point "pi/2" "0" label="must pass $(\pi/2,0)$" color=3
    readout "$y(0)$" "2+c2"
    readout "$y(\pi/2)$" "4+c1"
    caption "Every $c_1,c_2$ gives a solution of the ODE. Only $c_1=-4$, $c_2=-2$ passes through both points."
    ''')
    D.P(r'**Why the $\times t$ rule matters.** When the forcing matches a term of $y_c$, the response does not settle to the shape of $g$: it keeps growing, like $t\cos2t$. Slide $\omega$ to 2:')
    D.GRAPH(r'''
    title "Forcing at the natural frequency"
    x 0 12 label="$t$"
    y -25 25 label="$y$"
    slider w 1 3 1.5 step=0.05 label="$\omega$" animate
    curve "if(abs(w-2)<0.001, sin(2*x)-2*x*cos(2*x), 8/(4-w^2)*(sin(w*x)-w/2*sin(2*x)))" label="$y(t)$, starting at rest" color=1
    curve "2*x" label="$\pm2t$" color=0 dash
    curve "-2*x" color=0 dash
    caption "Solutions of $y''+4y=8\sin\omega t$ with $y(0)=y'(0)=0$. Here $y_c$ contains $\sin2t$ and $\cos2t$. For $\omega$ far from 2 the swing stays small. At $\omega=2$ the forcing is in $y_c$, the particular solution needs the extra $t$, and the swing grows along $\pm2t$."
    ''')

    P(D, 'W6 · A constant forcing, from rest',
      r"Solve $y''+4y=8$, $\;y(0)=0$, $y'(0)=0$.",
      [S(r'**Type:** constant coefficients, constant forcing. **Complementary:** $s^2+4=0$, $s=\pm j2$.', r'y_c=c_1\cos2t+c_2\sin2t'),
       S(r'**Guess:** a constant, $y_p=A$ (not in $y_c$). **Substitute:** $0+4A=8$.', r'y_p=2'),
       S(r'**Add.**', r'y=2+c_1\cos2t+c_2\sin2t'),
       S(r'**Conditions:** $y(0)=2+c_1=0$; $y\prime(0)=2c_2=0$.', r'c_1=-2,\qquad c_2=0')],
      r'$y=2-2\cos2t$. A constant source gives a constant $y_p$: the same idea as an RLC circuit switched onto a DC source (' + link('Topic D', 'topic-d') + ').')
    P(D, 'W6 · A polynomial guess needs every lower power',
      r"Find the general solution of $y''+y'-2y=2t$.",
      [S(r'**Type:** forcing $2t$. **Complementary:** $s^2+s-2=(s+2)(s-1)$.', r'y_c=c_1e^{t}+c_2e^{-2t}'),
       S(r'**Guess:** degree 1, so $At+B$. The $B$ is needed even though $g$ has no constant.', r"y_p=At+B,\quad y_p'=A,\quad y_p''=0"),
       S('**Substitute.**', r'A-2(At+B)=2t'),
       S(r'**Match** the $t$ terms, then the constants.', r'-2A=2,\qquad A-2B=0'),
       S('Solve.', r'A=-1,\qquad B=-\tfrac12')],
      r'$y=c_1e^{t}+c_2e^{-2t}-t-\tfrac12$. Guessing only $At$ fails: the leftover constant $A$ has nothing to match.')
    P(D, 'W6 · The guess is already in the complementary solution',
      r"Find the general solution of $y''-y'-2y=3e^{2t}$.",
      [S(r'**Type:** exponential forcing. **Complementary:** $s^2-s-2=(s-2)(s+1)$.', r'y_c=c_1e^{2t}+c_2e^{-t}'),
       S(r'**Guess:** the table says $Ae^{2t}$, but that is in $y_c$ (it would give $0=3e^{2t}$). Multiply by $t$.', r'y_p=Ate^{2t}'),
       S('Product rule, twice.', r"y_p'=A(1+2t)e^{2t},\qquad y_p''=A(4+4t)e^{2t}"),
       S(r'**Substitute** and divide by $e^{2t}$. The $t$ terms cancel.', r'A\big[(4+4t)-(1+2t)-2t\big]=3A=3'),
       S('Solve.', r'A=1')],
      r'$y_p=te^{2t}$, so $y=c_1e^{2t}+c_2e^{-t}+te^{2t}$.', diff='intermediate')
    P(D, 'W6 · Choose the form; do not solve',
      r"For $y''-2y'+y=g(t)$, write the guess for $y_p$ when $g$ is (a) $t^2$, (b) $e^{-t}$, (c) $e^t$, (d) $\cos t$.",
      [S(r'**Type:** guessing only. **Complementary** first: $s^2-2s+1=(s-1)^2$, a repeated root.', r'y_c=(c_1+c_2t)e^t'),
       S('(a) Degree 2: all lower powers.', r'At^2+Bt+C'),
       S(r'(b) $e^{-t}$ is not in $y_c$.', r'Ae^{-t}'),
       S(r'(c) $Ae^t$ and $Ate^t$ are **both** in $y_c$, so multiply by $t^2$.', r'At^2e^t'),
       S('(d) Cosine needs both cosine and sine.', r'A\cos t+B\sin t')],
      r'(a) $At^2+Bt+C$. (b) $Ae^{-t}$. (c) $At^2e^t$. (d) $A\cos t+B\sin t$.', diff='intermediate')
    P(D, 'W6 · A trig guess that is already in the complementary solution',
      r"Find a particular solution of $y''+9y=12\cos3t$. Use $(tf)\prime\prime=tf\prime\prime+2f\prime$ from the calculus table.",
      [S(r'**Type:** trig forcing. **Complementary:** $y_c=c_1\cos3t+c_2\sin3t$ already contains $\cos3t$, so multiply the guess by $t$.', r'y_p=t\,f,\qquad f=A\cos3t+B\sin3t'),
       S(r'**Substitute:** since $f\prime\prime=-9f$, the $t$ terms cancel in $y_p\prime\prime+9y_p$.', r"y_p''+9y_p=t(f''+9f)+2f'=2f'"),
       S(r'Differentiate $f$.', r"2f'=-6A\sin3t+6B\cos3t"),
       S(r'**Match** with $12\cos3t$.', r'6B=12,\qquad -6A=0')],
      r'$A=0$, $B=2$: $y_p=2t\sin3t$. The swing grows like $2t$, as in the graph above.', diff='advanced')


def verify():
    E = sp.exp
    A, B, c1, c2 = sp.symbols('A B c1 c2')
    zero(sp.cos(t) ** 2 - (sp.Rational(1, 2) + sp.cos(2 * t) / 2))
    zero(sp.sin(t) ** 2 - (sp.Rational(1, 2) - sp.cos(2 * t) / 2))
    second(3 + c1 * sp.sin(t) + c2 * sp.cos(t), 1, 0, 1, 3)
    sol = 3 - sp.cos(2 * t) - 4 * sp.sin(t) - 2 * sp.cos(t)
    second(sol, 1, 0, 1, 6 * sp.cos(t) ** 2)
    zero(sol.subs(t, 0))
    zero(sol.subs(t, sp.pi / 2))
    w = sp.Rational(3, 2)
    second(8 / (4 - w ** 2) * (sp.sin(w * t) - w / 2 * sp.sin(2 * t)), 1, 0, 4, 8 * sp.sin(w * t), initial=(0, 0, 0))
    second(sp.sin(2 * t) - 2 * t * sp.cos(2 * t), 1, 0, 4, 8 * sp.sin(2 * t), initial=(0, 0, 0))
    second(2 - 2 * sp.cos(2 * t), 1, 0, 4, 8, initial=(0, 0, 0))
    second(c1 * E(t) + c2 * E(-2 * t) - t - sp.Rational(1, 2), 1, 1, -2, 2 * t)
    second(c1 * E(2 * t) + c2 * E(-t) + t * E(2 * t), 1, -1, -2, 3 * E(2 * t))
    second(E(2 * t), 1, -1, -2, 0)
    for guess_solution, g in ((t ** 2 + 4 * t + 6, t ** 2), (E(-t) / 4, E(-t)),
                              (t ** 2 * E(t) / 2, E(t)), (-sp.sin(t) / 2, sp.cos(t))):
        second(guess_solution, 1, -2, 1, g)
    second(t * E(t), 1, -2, 1, 0)
    second(2 * t * sp.sin(3 * t), 1, 0, 9, 12 * sp.cos(3 * t))
    f = A * sp.cos(3 * t) + B * sp.sin(3 * t)
    zero(sp.diff(t * f, t, 2) + 9 * t * f - 2 * sp.diff(f, t))
    zero(sp.diff(t * E(2 * t), t) - (1 + 2 * t) * E(2 * t))
