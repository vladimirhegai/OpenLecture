"""B6: undetermined coefficients for a(y'') + b y' + c y = g(t) (Week 6)."""
import sympy as sp

from midlib import P, S, TAGS, link, second, t, zero


def build(D):
    W6 = lambda *p: D.cite('W6', *p)
    D.H('B6 · Undetermined coefficients', level=2, cites=W6(3, 4) + D.cite('N6', 1))
    TAGS(D, (6, 2))
    D.P(r'**What if the right side isn’t zero?** Like $y\prime\prime+y=3$. The right side, $g(t)$, is called the **forcing** (in a circuit, it’s the source).')
    D.P(r'The ' + link('B5', 'b5') + r' solutions all give $0$ when you plug them in, never $g(t)$. So you need one extra piece that gives $g(t)$.')
    D.P('The equations look like:')
    D.EQ(r'a\,y\prime\prime+b\,y\prime+c\,y=g(t)')
    D.L([r'left side = the same as in ' + link('B5', 'b5') + r': plain numbers $a,b,c$',
         r'$g(t)$ = everything with no $y$ in it, moved to the right. Example: $y\prime\prime+4y-8=0$ → $g=8$.'])
    D.P('The answer always has two pieces:')
    D.EQ(r'y=y_c+y_p')
    D.L([r'$y_c$ = the **complementary solution**: set the right side to $0$ and solve with ' + link('B5', 'b5') + r'. It carries the two constants $c_1,c_2$.',
         r'$y_p$ = a **particular solution**: any one function that gives exactly $g(t)$ when you plug it in. No constants.'])
    D.P(r'Why adding works: plug in $y_c+y_p$. The $y_c$ part gives $0$ and the $y_p$ part gives $g$, so the total is $0+g=g$.')
    D.P(r'Example: $y\prime\prime+y=3$.')
    D.L([r'$y_c$: $s^2+1=0$, $s=\pm j$, so $y_c=c_1\sin t+c_2\cos t$.',
         r'$y_p$: try a constant. $y_p=3$ gives $0+3=3$ ✓.',
         r'Add: $y=3+c_1\sin t+c_2\cos t$.'])

    D.P(r'**How do you find $y_p$? Copy the shape of $g(t)$.** Derivatives of $t^2$, $e^{2t}$ or $\cos3t$ stay the same kind of function.')
    D.P(r'So guess a $y_p$ that looks like $g$, with unknown numbers $A,B,\dots$ in front. Plug it in to find the numbers.')
    D.T([r'Term in $g(t)$', r'Guess for $y_p$', 'Example'], [
        [r'constant, or polynomial of degree $n$', r'$A_nt^n+\dots+A_1t+A_0$ (**all** lower powers)', r'$2t$ → $At+B$'],
        [r'$e^{at}$', r'$Ae^{at}$', r'$3e^{2t}$ → $Ae^{2t}$'],
        [r'$\sin rt$ or $\cos rt$', r'$A\cos rt+B\sin rt$ (**always both**)', r'$5\sin2t$ → $A\cos2t+B\sin2t$'],
        [r'$e^{at}\cos rt$ or $e^{at}\sin rt$', r'$e^{at}(A\cos rt+B\sin rt)$', r'$e^{-t}\cos t$ → $e^{-t}(A\cos t+B\sin t)$'],
        ['a sum of these', 'the sum of their guesses', r'$t+e^{t}$ → $At+B+Ce^{t}$'],
    ], cites=D.cite('N6', 1))
    D.L([r'**Why all lower powers:** derivatives of $At$ make a constant. The $B$ in $At+B$ is there to balance it.',
         r'**Why always both:** each derivative swaps $\cos$ and $\sin$, so both show up even if $g$ has only one.'])
    D.CO('warning', r'**Trap: your guess is already in $y_c$.** Then plugging it in gives $0$, so it can never give $g$. '
         r'**Fix: multiply the guess by $t$.** If that is still in $y_c$ (a repeated root), multiply by $t^2$ instead.'
         '\n\n'
         r'Example: $y\prime\prime-y\prime-2y=3e^{2t}$ has $y_c=c_1e^{2t}+c_2e^{-t}$. The table says $Ae^{2t}$, but that’s in $y_c$. So guess $Ate^{2t}$.')
    D.P('**Method:**')
    D.L([r'**Complementary:** set the right side to $0$ and solve (' + link('B5', 'b5') + r'). That gives $y_c$.',
         r'**Guess:** pick $y_p$’s shape from the table. If any term of it is already in $y_c$, multiply by $t$.',
         r'**Substitute:** plug $y_p$ into the left side.',
         r'**Match:** the constants must match, then each $\cos$, each $\sin$, each power of $t$. Solve for $A,B,\dots$',
         r'**Add:** $y=y_c+y_p$.',
         r'**Conditions:** use them on the **whole** $y$, never on $y_c$ or $y_p$ alone.'],
        ordered=True)
    D.P('**Calculus you need here:**')
    D.T(['Expression', 'Result', 'Note'], [
        [r'$\cos^2t$', r'$\tfrac12+\tfrac12\cos2t$', 'get rid of squares before guessing'],
        [r'$\sin^2t$', r'$\tfrac12-\tfrac12\cos2t$', ''],
        [r'$(A\cos rt+B\sin rt)\prime\prime$', r'$-r^2(A\cos rt+B\sin rt)$', r'two derivatives = times $-r^2$'],
        [r'$(te^{at})\prime$', r'$(1+at)\,e^{at}$', 'product rule'],
        [r'$(t\,f)\prime\prime$', r'$t\,f\prime\prime+2f\prime$', r'product rule twice, for a $\times t$ guess'],
    ])
    D.CO('info', r'**Bonus (skip-safe): why you can’t skip $y_c$.** $y_p$ has no constants, so on its own it can’t meet two conditions like $y(0)=0$ and $y\prime(0)=0$. '
         r'$y_c$ brings the two free constants that the conditions pin down. '
         r'And the trap above has the same cause: anything already in $y_c$ gives $0$ on the left, so it’s useless as a guess.')

    D.EX('W6 · The tutorial problem, with two boundary values · Week 6 tutorial, lecture notes p. 3–4',
         r"Solve $\ddot y+y=6\cos^2t$ with $y(0)=0$ and $y(\pi/2)=0$. The tutorial gives the forms $y_c=c_1\sin t+c_2\cos t$ and $y_p=A+B\cos2t+D\sin2t$. "
         r'($\ddot y$ is the professor’s notation for $y\prime\prime$.)',
         [S(r'**Type:** plain-number coefficients, forcing $6\cos^2t$. **Complementary:** $s^2+1=0$ gives $s=\pm j$.', r'y_c=c_1\sin t+c_2\cos t'),
          S(r'The table has no row for $\cos^2t$. Use the identity to turn it into a constant plus $\cos2t$.', r'6\cos^2t=3+3\cos2t'),
          S(r'**Guess:** the constant → $A$; the $\cos2t$ → both $\cos2t$ and $\sin2t$. None of them is in $y_c$.', r'y_p=A+B\cos2t+D\sin2t'),
          S(r'Differentiate twice: each $\cos2t$ and $\sin2t$ gets multiplied by $-4$.', r"y_p''=-4B\cos2t-4D\sin2t"),
          S(r'**Substitute** into $y_p\prime\prime+y_p$ and collect.', r'A-3B\cos2t-3D\sin2t=3+3\cos2t'),
          S('**Match** the constants, the cosines and the sines.', r'A=3,\qquad B=-1,\qquad D=0'),
          S(r'**Add** $y_c$ **before** using the conditions: they belong to the whole $y$.', r'y=3-\cos2t+c_1\sin t+c_2\cos t'),
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
    caption "Every $c_1,c_2$ gives a solution of the ODE. Only $c_1=-4$, $c_2=-2$ goes through both points."
    ''')
    D.P(r'**What does the extra $t$ look like?** When $g$ matches a term of $y_c$, the answer doesn’t just copy the shape of $g$. '
        r'It keeps growing, like $t\cos2t$ (this is **resonance**). Slide $\omega$ to 2 and watch:')
    D.GRAPH(r'''
    title "Forcing at the natural frequency"
    x 0 12 label="$t$"
    y -25 25 label="$y$"
    slider w 1 3 1.5 step=0.05 label="$\omega$" animate
    curve "if(abs(w-2)<0.001, sin(2*x)-2*x*cos(2*x), 8/(4-w^2)*(sin(w*x)-w/2*sin(2*x)))" label="$y(t)$, starting at rest" color=1
    curve "2*x" label="$\pm2t$" color=0 dash
    curve "-2*x" color=0 dash
    caption "$y''+4y=8\sin\omega t$, starting at rest. Here $y_c$ has $\sin2t$ and $\cos2t$. With $\omega$ far from 2, the swing stays small. At $\omega=2$ the forcing is in $y_c$, $y_p$ needs the extra $t$, and the swing grows along $\pm2t$."
    ''')

    P(D, 'W6 · A constant forcing, from rest',
      r"Solve $y''+4y=8$, $\;y(0)=0$, $y'(0)=0$.",
      [S(r'**Type:** plain-number coefficients, constant forcing. **Complementary:** $s^2+4=0$, $s=\pm j2$.', r'y_c=c_1\cos2t+c_2\sin2t'),
       S(r'**Guess:** a constant, $y_p=A$ (not in $y_c$). **Substitute:** $0+4A=8$.', r'y_p=2'),
       S(r'**Add.**', r'y=2+c_1\cos2t+c_2\sin2t'),
       S(r'**Conditions:** $y(0)=2+c_1=0$, and $y\prime(0)=2c_2=0$.', r'c_1=-2,\qquad c_2=0')],
      r'$y=2-2\cos2t$. A constant source gives a constant $y_p$, just like an RLC circuit switched onto a DC source (' + link('Topic D', 'topic-d') + ').')
    P(D, 'W6 · A polynomial guess needs every lower power',
      r"Find the general solution of $y''+y'-2y=2t$.",
      [S(r'**Type:** forcing $2t$. **Complementary:** $s^2+s-2=(s+2)(s-1)$.', r'y_c=c_1e^{t}+c_2e^{-2t}'),
       S(r'**Guess:** degree 1, so $At+B$. You need the $B$ even though $g$ has no constant.', r"y_p=At+B,\quad y_p'=A,\quad y_p''=0"),
       S('**Substitute.**', r'A-2(At+B)=2t'),
       S(r'**Match** the $t$ terms, then the constants.', r'-2A=2,\qquad A-2B=0'),
       S('Solve.', r'A=-1,\qquad B=-\tfrac12')],
      r'$y=c_1e^{t}+c_2e^{-2t}-t-\tfrac12$. With only $At$, you’d need $A=-1$ (from the $t$ terms) and $A=0$ (from the constants) at once, which is impossible.')
    P(D, 'W6 · The guess is already in the complementary solution',
      r"Find the general solution of $y''-y'-2y=3e^{2t}$.",
      [S(r'**Type:** exponential forcing. **Complementary:** $s^2-s-2=(s-2)(s+1)$.', r'y_c=c_1e^{2t}+c_2e^{-t}'),
       S(r'**Guess:** the table says $Ae^{2t}$, but that’s in $y_c$ (it would give $0=3e^{2t}$). Multiply by $t$.', r'y_p=Ate^{2t}'),
       S('Product rule, twice.', r"y_p'=A(1+2t)e^{2t},\qquad y_p''=A(4+4t)e^{2t}"),
       S(r'**Substitute** and divide by $e^{2t}$. The $t$ terms cancel.', r'A\big[(4+4t)-(1+2t)-2t\big]=3A=3'),
       S('Solve.', r'A=1')],
      r'$y_p=te^{2t}$, so $y=c_1e^{2t}+c_2e^{-t}+te^{2t}$.', diff='intermediate')
    P(D, 'W6 · Choose the form; do not solve',
      r"For $y''-2y'+y=g(t)$, write the guess for $y_p$ when $g$ is (a) $t^2$, (b) $e^{-t}$, (c) $e^t$, (d) $\cos t$.",
      [S(r'**Type:** guessing only. Find the **complementary** first: $s^2-2s+1=(s-1)^2$, a repeated root.', r'y_c=(c_1+c_2t)e^t'),
       S('(a) Degree 2, so all lower powers too.', r'At^2+Bt+C'),
       S(r'(b) $e^{-t}$ is not in $y_c$.', r'Ae^{-t}'),
       S(r'(c) $Ae^t$ is in $y_c$, and so is $Ate^t$. Multiply by $t^2$.', r'At^2e^t'),
       S('(d) Cosine needs both cosine and sine.', r'A\cos t+B\sin t')],
      r'(a) $At^2+Bt+C$. (b) $Ae^{-t}$. (c) $At^2e^t$. (d) $A\cos t+B\sin t$.', diff='intermediate')
    P(D, 'W6 · A trig guess that is already in the complementary solution',
      r"Find a particular solution of $y''+9y=12\cos3t$. Use $(tf)\prime\prime=tf\prime\prime+2f\prime$ from the calculus table.",
      [S(r'**Type:** trig forcing. **Complementary:** $y_c=c_1\cos3t+c_2\sin3t$ already has $\cos3t$, so multiply the guess by $t$.', r'y_p=t\,f,\qquad f=A\cos3t+B\sin3t'),
       S(r'**Substitute:** $f\prime\prime=-9f$, so the $t$ terms cancel in $y_p\prime\prime+9y_p$.', r"y_p''+9y_p=t(f''+9f)+2f'=2f'"),
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
