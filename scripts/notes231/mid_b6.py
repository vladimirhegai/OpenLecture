"""B6: undetermined coefficients for a y'' + b y' + c y = f(t) (Week 6).

Layout (REWRITE_PLAN.md). Shared letters: f(t) = the right side (as in B2/B7/C2), c1, c2 = the constants of y_c
(as in B5), A, B, D = the unknown numbers in the guess (the tutorial's letters). Step words: Write, Solve y_c,
Guess, Plug in and match, Add, Plug in the conditions. One case per kind of f(t).
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
    D.WHY('Why add two pieces?',
          r'Plug $y_c+y_p$ into the left side. The $y_c$ part gives $0$ (that’s how B5 built it). The $y_p$ part gives $f$. Total: $0+f=f$.'
          '\n\n'
          r'And $y_p$ has no free constants, so on its own it can’t meet two conditions like $y(0)$ and $y\prime(0)$. $y_c$ brings the $c_1,c_2$ that the conditions pin down.')

    D.P('**Steps**')
    D.L([r'**Write** it with every $y$ term on the left and $f(t)$ on the right.',
         r'**Solve $y_c$:** set the right side to $0$ and do ' + link('B5', 'b5') + r' (quadratic → case → form with $c_1,c_2$).',
         r'**Guess $y_p$** from the cases below. If any term of it is already in $y_c$, multiply it by $t$.',
         r'**Plug $y_p$ into the ODE and match:** constants with constants, each $\cos$, each $\sin$, each power of $t$. Solve for $A,B,\dots$',
         r'**Add:** $y=y_c+y_p$.',
         r'**Plug in** the conditions on the **whole** $y$, never on $y_c$ alone.'], ordered=True)
    D.CO('tip', r'**What the lecture worked (Mon Oct 26):** Cases 1 and 3 below (a constant, and $\sin$/$\cos$). '
         r'That’s exactly what the tutorial problem needs. Nail those first.', cites=D.cite('N6', 1))

    D.H('Case 1: f is a constant or a polynomial', level=3)
    D.P(r'Guess a polynomial of the **same degree**, with **every lower power** too:')
    D.EQ(r'8\ \to\ A,\qquad 2t\ \to\ At+B,\qquad t^2\ \to\ At^2+Bt+D')
    CARD(D, r'Full example: $\;y\prime\prime+y\prime-2y=2t$ (general solution)',
         [(r'**Solve $y_c$:** set the right side to $0$. The quadratic factors.', (r's^2+s-2=(s+2)(s-1)=0', r'y_c=c_1e^{t}+c_2e^{-2t}')),
          (r'**Guess $y_p$:** degree 1, so $At+B$. You need the $B$ even though $f$ has no constant.', (r'y_p=At+B', r'y_p\prime=A,\qquad y_p\prime\prime=0')),
          (r'**Plug in** to $y\prime\prime+y\prime-2y$.', r'0+A-2(At+B)=2t'),
          (r'**Match** the $t$ terms, then the constants.', (r'-2A=2', r'A-2B=0')),
          (r'Solve.', r'A=-1,\qquad B=-\tfrac12'),
          (r'**Add.**', r'y=c_1e^{t}+c_2e^{-2t}-t-\tfrac12')],
         r'y=c_1e^{t}+c_2e^{-2t}-t-\tfrac12')

    D.H('Case 2: f is an exponential', level=3)
    D.P(r'Guess the same exponential:')
    D.EQ(r'3e^{2t}\ \to\ Ae^{2t}')
    CARD(D, r'Full example: $\;y\prime\prime+3y\prime+2y=6e^{t}$ (general solution)',
         [(r'**Solve $y_c$:** $s^2+3s+2=(s+1)(s+2)$.', r'y_c=c_1e^{-t}+c_2e^{-2t}'),
          (r'**Guess $y_p$:** $e^{t}$ is not in $y_c$. Every derivative of $Ae^{t}$ is $Ae^{t}$.', r'y_p=Ae^{t},\qquad y_p\prime=y_p\prime\prime=Ae^{t}'),
          (r'**Plug in and match:** divide by $e^{t}$.', r'A+3A+2A=6\quad\Rightarrow\quad A=1'),
          (r'**Add.**', r'y=c_1e^{-t}+c_2e^{-2t}+e^{t}')],
         r'y=c_1e^{-t}+c_2e^{-2t}+e^{t}')

    D.H('Case 3: f is a sin or a cos', level=3)
    D.P(r'Guess **both** $\cos$ and $\sin$, even if $f$ has only one:')
    D.EQ(r'5\sin2t\ \to\ A\cos2t+B\sin2t')
    D.P(r'Why both: each derivative swaps $\cos$ and $\sin$, so both show up anyway. Handy fact: two derivatives multiply by $-r^2$:')
    D.EQ(r'(A\cos rt+B\sin rt)\prime\prime=-r^2(A\cos rt+B\sin rt)')
    CARD(D, r'Full example: $\;y\prime\prime+3y\prime+2y=10\sin t$ (general solution)',
         [(r'**Solve $y_c$:** same quadratic as Case 2.', r'y_c=c_1e^{-t}+c_2e^{-2t}'),
          (r'**Guess $y_p$:** both $\cos t$ and $\sin t$.', (r'y_p=A\cos t+B\sin t', r'y_p\prime=-A\sin t+B\cos t', r'y_p\prime\prime=-A\cos t-B\sin t')),
          (r'**Plug in** to $y\prime\prime+3y\prime+2y$ and collect the $\cos t$ and $\sin t$ terms.', r'(A+3B)\cos t+(B-3A)\sin t=10\sin t'),
          (r'**Match:** the right side has no $\cos t$, so its coefficient is $0$.', (r'A+3B=0', r'B-3A=10')),
          (r'Solve: $A=-3B$, so $B+9B=10$.', r'B=1,\qquad A=-3'),
          (r'**Add.**', r'y=c_1e^{-t}+c_2e^{-2t}-3\cos t+\sin t')],
         r'y=c_1e^{-t}+c_2e^{-2t}-3\cos t+\sin t')
    D.P(r'**A sum of these?** Guess the sum of their guesses:')
    D.EQ(r't+e^{t}\ \to\ At+B+De^{t}')
    D.P(r'**A $\cos^2t$ or $\sin^2t$?** Turn it into a constant plus $\cos2t$ first:')
    D.EQ(r'\cos^2t=\tfrac12+\tfrac12\cos2t,\qquad \sin^2t=\tfrac12-\tfrac12\cos2t')

    D.H('Case 4: the guess is already in y_c', level=3)
    D.P(r'Then plugging it in gives $0$, never $f$. **Multiply the guess by $t$.** Still in $y_c$ (a repeated root)? Multiply by $t^2$.')
    D.EQ(r'y_c=c_1e^{2t}+c_2e^{-t},\quad f=3e^{2t}\quad\Longrightarrow\quad y_p=Ate^{2t}')
    CARD(D, r'Full example: $\;y\prime\prime-y\prime-2y=3e^{2t}$ (general solution)',
         [(r'**Solve $y_c$:** $s^2-s-2=(s-2)(s+1)$.', r'y_c=c_1e^{2t}+c_2e^{-t}'),
          (r'**Guess $y_p$:** Case 2 says $Ae^{2t}$, but that’s in $y_c$. Multiply by $t$.', r'y_p=Ate^{2t}'),
          (r'Differentiate with the product rule, twice.', (r'y_p\prime=A(1+2t)e^{2t}', r'y_p\prime\prime=A(4+4t)e^{2t}')),
          (r'**Plug in** and divide by $e^{2t}$. The $t$ terms cancel.', r'A\big[(4+4t)-(1+2t)-2t\big]=3A=3'),
          (r'**Match.**', r'A=1'),
          (r'**Add.**', r'y=c_1e^{2t}+c_2e^{-t}+te^{2t}')],
         r'y=c_1e^{2t}+c_2e^{-t}+te^{2t}')
    D.CO('warning', r'**Always find $y_c$ before you guess.** That’s the only way to spot Case 4.')

    D.H('The tutorial problem (know this cold)', level=3)
    D.P(r'Pre-tutorial 5, the Week 7 tutorial (Oct 26, 28), and the lecture’s own example. Be able to do every step, the two conditions included. '
        r'($\ddot y$ is the professor’s way of writing $y\prime\prime$.)')
    D.EQ(r'\ddot y+y=6\cos^2t,\qquad y(0)=0,\quad y(\pi/2)=0')
    CARD(D, r'Full solution: $\;\ddot y+y=6\cos^2t$, $\;y(0)=0$, $\;y(\pi/2)=0$',
         [(r'**Solve $y_c$:** $s^2+1=0$ gives $s=\pm j$ (B5 Case 3, $\sigma=0$, $\omega=1$).', r'y_c=c_1\sin t+c_2\cos t'),
          (r'No case for $\cos^2t$, so use the identity: a constant plus $\cos2t$.', r'6\cos^2t=3+3\cos2t'),
          (r'**Guess $y_p$:** the constant → $A$ (Case 1). The $\cos2t$ → both $\cos2t$ and $\sin2t$ (Case 3). None is in $y_c$.',
           r'y_p=A+B\cos2t+D\sin2t'),
          (r'Differentiate twice: each $\cos2t$, $\sin2t$ gets multiplied by $-4$.', r'y_p\prime\prime=-4B\cos2t-4D\sin2t'),
          (r'**Plug in** to $y_p\prime\prime+y_p$ and collect.', r'A-3B\cos2t-3D\sin2t=3+3\cos2t'),
          (r'**Match** the constants, the $\cos2t$’s and the $\sin2t$’s.', r'A=3,\qquad B=-1,\qquad D=0'),
          (r'**Add** $y_c$ **before** the conditions: they belong to the whole $y$.', r'y=3-\cos2t+c_1\sin t+c_2\cos t'),
          (r'**Plug in** $y(0)=0$: $\sin0=0$, $\cos0=1$.', r'3-1+c_2=0\quad\Rightarrow\quad c_2=-2'),
          (r'**Plug in** $y(\pi/2)=0$: $\cos\pi=-1$, $\sin\frac\pi2=1$, $\cos\frac\pi2=0$.', r'3+1+c_1=0\quad\Rightarrow\quad c_1=-4')],
         r'y=3-\cos2t-4\sin t-2\cos t')
    D.P(r'The tutorial hands you the forms of $y_c$ and $y_p$. On the exam they might not: the ' + link('Topic E', 'topic-e') + ' version has no hints.',
        cites=D.cite('T5', 1) + D.cite('T6', 1) + W6(3, 4))

    D.H('Practice: B6', level=3)
    P(D, 'W6 · A constant right side, from rest',
      r'Solve $y\prime\prime+4y=8$, $\;y(0)=0$, $y\prime(0)=0$.',
      [S(r'**Type:** numbers in front, right side $8$ → B6.'),
       S(r'**Solve $y_c$:** $s^2+4=0$, $s=\pm j2$ (B5 Case 3).', r'y_c=c_1\cos2t+c_2\sin2t'),
       S(r'**Guess $y_p$:** a constant (Case 1). Not in $y_c$.', r'y_p=A'),
       S(r'**Plug in and match:** $y_p\prime\prime=0$.', r'0+4A=8\quad\Rightarrow\quad A=2'),
       S(r'**Add.**', r'y=2+c_1\cos2t+c_2\sin2t'),
       S(r'**Differentiate** for $y\prime(0)$.', r'y\prime=-2c_1\sin2t+2c_2\cos2t'),
       S(r'**Plug in** $t=0$.', (r'y(0)=2+c_1=0\quad\Rightarrow\quad c_1=-2', r'y\prime(0)=2c_2=0\quad\Rightarrow\quad c_2=0'))],
      r'$y=2-2\cos2t$. A constant source gives a constant $y_p$, like an RLC circuit switched onto DC (' + link('D2', 'd2') + ').')
    P(D, 'W6 · Choose the form; do not solve',
      r'For $y\prime\prime-2y\prime+y=f(t)$, write the guess for $y_p$ when $f$ is (a) $t^2$, (b) $e^{-t}$, (c) $e^t$, (d) $\cos t$.',
      [S(r'**Solve $y_c$ first** (you need it for Case 4): $s^2-2s+1=(s-1)^2$, a repeated root.', r'y_c=(c_1+c_2t)\,e^{t}'),
       S(r'(a) Case 1, degree 2: every lower power too.', r'At^2+Bt+D'),
       S(r'(b) Case 2. $e^{-t}$ is not in $y_c$.', r'Ae^{-t}'),
       S(r'(c) Case 4. $Ae^t$ is in $y_c$, and so is $Ate^t$. Multiply by $t^2$.', r'At^2e^{t}'),
       S(r'(d) Case 3: both $\cos$ and $\sin$.', r'A\cos t+B\sin t')],
      r'(a) $At^2+Bt+D$. (b) $Ae^{-t}$. (c) $At^2e^{t}$. (d) $A\cos t+B\sin t$.', diff='intermediate')
    P(D, 'W6 · A trig guess that is already in y_c',
      r'Find a particular solution of $y\prime\prime+9y=12\cos3t$. Use $(t\,u)\prime\prime=t\,u\prime\prime+2u\prime$ (product rule twice).',
      [S(r'**Solve $y_c$:** $s=\pm j3$.', r'y_c=c_1\cos3t+c_2\sin3t'),
       S(r'**Guess $y_p$:** Case 3 says $A\cos3t+B\sin3t$, but that’s in $y_c$. Case 4: multiply by $t$.', (r'y_p=t\,u', r'u=A\cos3t+B\sin3t')),
       S(r'**Plug in:** $u\prime\prime=-9u$, so the $t$ terms cancel.', r'y_p\prime\prime+9y_p=t(u\prime\prime+9u)+2u\prime=2u\prime'),
       S(r'Differentiate $u$.', r'2u\prime=-6A\sin3t+6B\cos3t'),
       S(r'**Match** with $12\cos3t$.', r'6B=12,\qquad -6A=0')],
      r'$A=0$, $B=2$: $\;y_p=2t\sin3t$. It keeps growing like $2t$: that’s **resonance**.', diff='advanced')


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
    second(2 - 2 * sp.cos(2 * t), 1, 0, 4, 8, initial=(0, 0, 0))
    second(c1 * E(t) + c2 * E(-2 * t) - t - sp.Rational(1, 2), 1, 1, -2, 2 * t)
    second(c1 * E(-t) + c2 * E(-2 * t) + E(t), 1, 3, 2, 6 * E(t))
    second(c1 * E(-t) + c2 * E(-2 * t) - 3 * sp.cos(t) + sp.sin(t), 1, 3, 2, 10 * sp.sin(t))
    yp = A * sp.cos(t) + B * sp.sin(t)
    zero(sp.diff(yp, t, 2) + 3 * sp.diff(yp, t) + 2 * yp - ((A + 3 * B) * sp.cos(t) + (B - 3 * A) * sp.sin(t)))
    second(c1 * E(2 * t) + c2 * E(-t) + t * E(2 * t), 1, -1, -2, 3 * E(2 * t))
    second(E(2 * t), 1, -1, -2, 0)
    zero(sp.diff(t * E(2 * t), t) - (1 + 2 * t) * E(2 * t))
    zero(sp.diff(t * E(2 * t), t, 2) - (4 + 4 * t) * E(2 * t))
    for guess_solution, f in ((t ** 2 + 4 * t + 6, t ** 2), (E(-t) / 4, E(-t)),
                              (t ** 2 * E(t) / 2, E(t)), (-sp.sin(t) / 2, sp.cos(t))):
        second(guess_solution, 1, -2, 1, f)
    second(t * E(t), 1, -2, 1, 0)
    second(2 * t * sp.sin(3 * t), 1, 0, 9, 12 * sp.cos(3 * t))
    u = A * sp.cos(3 * t) + B * sp.sin(3 * t)
    zero(sp.diff(t * u, t, 2) + 9 * t * u - 2 * sp.diff(u, t))
