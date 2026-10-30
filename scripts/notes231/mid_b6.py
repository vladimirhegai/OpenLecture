"""B6: undetermined coefficients for a y'' + b y' + c y = f(t) (Week 6).

Layout (REWRITE_PLAN.md). Shared letters: f(t) = the right side (as in B2/B7/C2), c1, c2 = the constants of y_c
(as in B5), A, B, D = the unknown numbers in the guess (the tutorial's letters). Step words: Write, Solve y_c,
Guess, Plug in and match, Add, Plug in the conditions. Only the right sides the lecture taught: constants, sin/cos.
"""
import sympy as sp

from midlib import CARD, P, S, TAGS, link, second, t, zero


def build(D):
    W6 = lambda *p: D.cite('W6', *p)
    D.H('B6 · Second order, numbers in front, right side f(t)', level=2, cites=W6(3, 4) + D.cite('N6', 1))
    TAGS(D, (6, 2))
    D.P(r'**Use this when** it looks like ' + link('B5', 'b5') + r', but the right side is **not** $0$:')
    D.EQ(r'y\prime\prime+y=3')
    D.P('Every one of these looks like:')
    D.EQ(r'a\,y\prime\prime+b\,y\prime+c\,y=f(t)')
    D.L([r'$a,b,c$ = plain numbers, same as ' + link('B5', 'b5'),
         r'$f(t)$ = the right side, everything with no $y$ in it (in a circuit: the source)'])

    D.P(r'**The move: the answer comes in two pieces.**')
    D.EQ(r'y=y_c+y_p')
    D.L([r'$y_c$ = the ' + link('B5', 'b5') + r' answer, with the right side set to $0$. It carries $c_1$ and $c_2$.',
         r'$y_p$ = one guess that gives exactly $f(t)$. Copy the **shape** of $f(t)$, with unknown numbers $A,B,D$ in front.'])
    D.P(r'**Short example:** $y\prime\prime+y=3$:')
    D.EQ(r'y_c=c_1\sin t+c_2\cos t,\qquad y_p=3')
    D.EQ(r'y=3+c_1\sin t+c_2\cos t')

    D.P('**Steps**')
    D.L([r'**Write** it with every $y$ term on the left and $f(t)$ on the right.',
         r'**Solve $y_c$:** set the right side to $0$ and do ' + link('B5', 'b5') + r' (quadratic → case → form with $c_1,c_2$).',
         r'**Guess $y_p$** from the two cases below.',
         r'**Plug $y_p$ into the ODE and match:** constants with constants, each $\cos$, each $\sin$. Solve for $A,B,D$.',
         r'**Add:** $y=y_c+y_p$.',
         r'**Plug in** the conditions on the **whole** $y$, never on $y_c$ alone.'], ordered=True)

    D.H('Case 1: f is a constant', level=3)
    D.P(r'Guess a constant $A$. Two derivatives of a constant are $0$, so only the $y$ term is left:')
    D.EQ(r'y\prime\prime+4y=8\quad\Longrightarrow\quad y_p=A,\quad 4A=8,\quad A=2')

    D.H('Case 2: f is a sin or a cos', level=3)
    D.P(r'Guess **both** $\cos$ and $\sin$, even if $f$ has only one:')
    D.EQ(r'5\sin2t\ \to\ A\cos2t+B\sin2t')
    D.P(r'Why both: each derivative swaps $\cos$ and $\sin$, so both show up anyway. Handy fact: two derivatives multiply by $-r^2$:')
    D.EQ(r'(A\cos rt+B\sin rt)\prime\prime=-r^2(A\cos rt+B\sin rt)')
    CARD(D, r'Full example: $\;y\prime\prime+3y\prime+2y=10\sin t$ (general solution)',
         [(r'**Solve $y_c$:** $s^2+3s+2=(s+1)(s+2)=0$.', r'y_c=c_1e^{-t}+c_2e^{-2t}'),
          (r'**Guess $y_p$:** both $\cos t$ and $\sin t$.', (r'y_p=A\cos t+B\sin t', r'y_p\prime=-A\sin t+B\cos t', r'y_p\prime\prime=-A\cos t-B\sin t')),
          (r'**Plug in** to $y\prime\prime+3y\prime+2y$ and collect the $\cos t$ and $\sin t$ terms.', r'(A+3B)\cos t+(B-3A)\sin t=10\sin t'),
          (r'**Match:** the right side has no $\cos t$, so its coefficient is $0$.', (r'A+3B=0', r'B-3A=10')),
          (r'Solve: $A=-3B$, so $B+9B=10$.', r'B=1,\qquad A=-3'),
          (r'**Add.**', r'y=c_1e^{-t}+c_2e^{-2t}-3\cos t+\sin t')],
         r'y=c_1e^{-t}+c_2e^{-2t}-3\cos t+\sin t')
    D.P(r'**A constant plus a cos?** Guess the sum of the two guesses: $A+B\cos2t+D\sin2t$.')
    D.P(r'**A $\cos^2t$ or $\sin^2t$?** Turn it into a constant plus $\cos2t$ first:')
    D.EQ(r'\cos^2t=\tfrac12+\tfrac12\cos2t,\qquad \sin^2t=\tfrac12-\tfrac12\cos2t')

    D.H('★ The tutorial problem (know this cold)', level=3)
    D.P(r'Pre-tutorial 5 = the Week 6 tutorial = the lecture’s own example. The single most likely midterm question. '
        r'Be able to do every step, the two conditions included. ($\ddot y$ is the prof’s way of writing $y\prime\prime$.)')
    D.EQ(r'\ddot y+y=6\cos^2t,\qquad y(0)=0,\quad y(\pi/2)=0')
    CARD(D, r'★ Full solution (try it, then open): $\;\ddot y+y=6\cos^2t$, $\;y(0)=0$, $\;y(\pi/2)=0$',
         [(r'**Solve $y_c$:** $s^2+1=0$ gives $s=\pm j$ (B5 Case 3, $\sigma=0$, $\omega=1$).', r'y_c=c_1\sin t+c_2\cos t'),
          (r'Use the identity: a constant plus $\cos2t$.', r'6\cos^2t=3+3\cos2t'),
          (r'**Guess $y_p$:** the constant → $A$ (Case 1). The $\cos2t$ → both $\cos2t$ and $\sin2t$ (Case 2).',
           r'y_p=A+B\cos2t+D\sin2t'),
          (r'Differentiate twice: each $\cos2t$, $\sin2t$ gets multiplied by $-4$.', r'y_p\prime\prime=-4B\cos2t-4D\sin2t'),
          (r'**Plug in** to $y_p\prime\prime+y_p$ and collect.', r'A-3B\cos2t-3D\sin2t=3+3\cos2t'),
          (r'**Match** the constants, the $\cos2t$’s and the $\sin2t$’s.', r'A=3,\qquad B=-1,\qquad D=0'),
          (r'**Add** $y_c$ **before** the conditions: they belong to the whole $y$.', r'y=3-\cos2t+c_1\sin t+c_2\cos t'),
          (r'**Plug in** $y(0)=0$: $\sin0=0$, $\cos0=1$.', r'3-1+c_2=0\quad\Rightarrow\quad c_2=-2'),
          (r'**Plug in** $y(\pi/2)=0$: $\cos\pi=-1$, $\sin\frac\pi2=1$, $\cos\frac\pi2=0$.', r'3+1+c_1=0\quad\Rightarrow\quad c_1=-4')],
         r'y=3-\cos2t-4\sin t-2\cos t')
    D.P(r'The tutorial hands you $y_c$ and the $y_p$ guess. The exam might not: get $y_c$ from ' + link('B5', 'b5') + r' and $y_p$ from the two cases above.',
        cites=D.cite('T5', 1) + D.cite('T6', 1) + W6(3, 4))

    D.H('Practice: B6', level=3)
    P(D, 'W6 · A constant right side, from rest',
      r'Solve $y\prime\prime+4y=8$, $\;y(0)=0$, $y\prime(0)=0$.',
      [S(r'**Type:** numbers in front, right side $8$ → B6.'),
       S(r'**Solve $y_c$:** $s^2+4=0$, $s=\pm j2$ (B5 Case 3).', r'y_c=c_1\cos2t+c_2\sin2t'),
       S(r'**Guess $y_p$:** a constant (Case 1).', r'y_p=A'),
       S(r'**Plug in and match:** $y_p\prime\prime=0$.', r'0+4A=8\quad\Rightarrow\quad A=2'),
       S(r'**Add.**', r'y=2+c_1\cos2t+c_2\sin2t'),
       S(r'**Differentiate** for $y\prime(0)$.', r'y\prime=-2c_1\sin2t+2c_2\cos2t'),
       S(r'**Plug in** $t=0$.', (r'y(0)=2+c_1=0\quad\Rightarrow\quad c_1=-2', r'y\prime(0)=2c_2=0\quad\Rightarrow\quad c_2=0'))],
      r'$y=2-2\cos2t$. A constant source gives a constant $y_p$, like an RLC circuit switched onto DC (' + link('D2', 'd2') + ').')
    P(D, 'W6 · The tutorial problem with sin², no hints · like Pre-tutorial 5',
      r'Solve $y\prime\prime+y=4\sin^2t$, $\;y(0)=0$, $y\prime(0)=0$.',
      [S(r'**Type:** numbers in front, right side not $0$ → B6. Same left side as the tutorial.'),
       S(r'**Solve $y_c$:** $s^2+1=0$, $s=\pm j$ (B5 Case 3).', r'y_c=c_1\sin t+c_2\cos t'),
       S(r'**Write** the right side with the identity.', r'4\sin^2t=2-2\cos2t'),
       S(r'**Guess $y_p$:** constant + both $\cos2t$ and $\sin2t$.', (r'y_p=A+B\cos2t+D\sin2t', r'y_p\prime\prime=-4B\cos2t-4D\sin2t')),
       S(r'**Plug in and match.**', (r'A-3B\cos2t-3D\sin2t=2-2\cos2t', r'A=2,\qquad B=\tfrac23,\qquad D=0')),
       S(r'**Add.**', r'y=2+\tfrac23\cos2t+c_1\sin t+c_2\cos t'),
       S(r'**Differentiate** for $y\prime(0)$.', r'y\prime=-\tfrac43\sin2t+c_1\cos t-c_2\sin t'),
       S(r'**Plug in** $t=0$.', (r'y(0)=2+\tfrac23+c_2=0\quad\Rightarrow\quad c_2=-\tfrac83', r'y\prime(0)=c_1=0'))],
      r'$y=2+\tfrac23\cos2t-\tfrac83\cos t$.', diff='intermediate')


def verify():
    c1, c2, A, B = sp.symbols('c1 c2 A B')
    zero(sp.cos(t) ** 2 - (sp.Rational(1, 2) + sp.cos(2 * t) / 2))
    zero(sp.sin(t) ** 2 - (sp.Rational(1, 2) - sp.cos(2 * t) / 2))
    second(3 + c1 * sp.sin(t) + c2 * sp.cos(t), 1, 0, 1, 3)
    sol = 3 - sp.cos(2 * t) - 4 * sp.sin(t) - 2 * sp.cos(t)
    second(sol, 1, 0, 1, 6 * sp.cos(t) ** 2)
    zero(sol.subs(t, 0))
    zero(sol.subs(t, sp.pi / 2))
    second(2 - 2 * sp.cos(2 * t), 1, 0, 4, 8, initial=(0, 0, 0))
    second(c1 * sp.exp(-t) + c2 * sp.exp(-2 * t) - 3 * sp.cos(t) + sp.sin(t), 1, 3, 2, 10 * sp.sin(t))
    yp = A * sp.cos(t) + B * sp.sin(t)
    zero(sp.diff(yp, t, 2) + 3 * sp.diff(yp, t) + 2 * yp - ((A + 3 * B) * sp.cos(t) + (B - 3 * A) * sp.sin(t)))
    second(2 + sp.Rational(2, 3) * sp.cos(2 * t) - sp.Rational(8, 3) * sp.cos(t), 1, 0, 1, 4 * sp.sin(t) ** 2, initial=(0, 0, 0))
