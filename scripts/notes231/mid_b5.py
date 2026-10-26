"""B5: second-order linear homogeneous equations with constant coefficients (Weeks 4-5)."""
import sympy as sp

from midlib import P, S, TAGS, link, second, t, zero


def build(D):
    D.H('B5 · Second order, constant coefficients: the characteristic equation', level=2)
    TAGS(D, (5, 1))
    D.P(r'**What if the equation has a $y\prime\prime$ in it?** Like $y\prime\prime+3y\prime+2y=0$. '
        r'If every coefficient is a plain number, there’s a shortcut: guess $y=e^{st}$.')
    D.P(r'Why that guess works: each derivative of $e^{st}$ is $e^{st}$ again, times one more $s$. '
        r'So the whole ODE turns into a quadratic in $s$, and you already know how to solve those.')
    D.P('The equations this works on look like:')
    D.EQ(r'a\,y\prime\prime+b\,y\prime+c\,y=0')
    D.L([r'$a,b,c$ = plain numbers, no $t$ in them ($a\neq0$). Example: $y\prime\prime+3y\prime+2y=0$ has $a=1$, $b=3$, $c=2$.',
         r'right side $=0$ (called **homogeneous**). If it isn’t $0$, like $y\prime\prime+y=3$, you also need ' + link('B6', 'b6') + '.',
         r'If a coefficient has $t$ in it, like $y\prime\prime-ty\prime+y=0$, this shortcut fails: see ' + link('B7', 'b7') + '.'])

    D.P(r'**Step 1: the characteristic equation.** Swap each derivative for a power of $s$: $y\prime\prime\to s^2$, $y\prime\to s$, $y\to1$.')
    D.EQ(r'a\,s^2+b\,s+c=0')
    D.L([r'$y\prime\prime+3y\prime+2y=0$ → $s^2+3s+2=0$',
         r'$4y\prime\prime+4y\prime+y=0$ → $4s^2+4s+1=0$',
         r'$y\prime\prime+9y=0$ → $s^2+9=0$ (no $y\prime$ term, so no $s$ term)'])
    D.P(r'**Step 2: the roots.** Factor if you can. If not, use the quadratic formula:')
    D.EQ(r's=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}')
    D.P(r'A negative number under the root gives complex roots. Example: $s^2+2s+5=0$ has $\sqrt{4-20}=\sqrt{-16}=j4$, so $s=-1\pm j2$. '
        r'Complex numbers are in ' + link('Topic A', 'topic-a') + '.')
    D.P(r'**Step 3: the roots pick the form.** Find your row:')
    D.T(['Roots', r'General solution $y(t)$', r'$y(0)$', r'$y\prime(0)$'], [
        [r'two different real: $s_1\neq s_2$', r'$Ae^{s_1t}+Be^{s_2t}$', r'$A+B$', r'$s_1A+s_2B$'],
        [r'one repeated real: $s$', r'$(A+Bt)\,e^{st}$', r'$A$', r'$sA+B$'],
        [r'complex pair: $\sigma\pm j\omega$', r'$e^{\sigma t}(A\cos\omega t+B\sin\omega t)$', r'$A$', r'$\sigma A+\omega B$'],
    ])
    D.L([r'**Two different roots:** $s=-1,\,-2$ → $y=Ae^{-t}+Be^{-2t}$. One exponential per root.',
         r'**Repeated root:** $s=-\frac12$ twice → $y=(A+Bt)\,e^{-t/2}$. $Ae^{st}+Be^{st}$ is really one term, so you need a different second solution: $te^{st}$.',
         r'**Complex pair:** $s=-1\pm j2$ → $y=e^{-t}(A\cos2t+B\sin2t)$. $\sigma$ = the real part (how fast it shrinks), $\omega$ = the $j$ part (how fast it wiggles).'])
    D.P(r'**Time saver:** the last two columns already give $y(0)$ and $y\prime(0)$. With conditions at $t=0$, write the two equations for $A$ and $B$ straight from the table.')
    D.P(r'Example: roots $-2$ and $-3$ → $y(0)=A+B$ and $y\prime(0)=-2A-3B$. '
        r'For conditions at another time, like $y(1)$, differentiate $y(t)$ yourself (table below).')
    D.P('**Method:**')
    D.L([r'**Characteristic equation:** swap $y\prime\prime\to s^2$, $y\prime\to s$, $y\to1$.',
         r'**Roots:** factor, or use the quadratic formula.',
         r'**Form:** pick the row of the table that matches your roots.',
         r'**Conditions:** $y(0)$ and $y\prime(0)$ give two equations. Solve them for $A$ and $B$.'],
        ordered=True)
    D.P('**Calculus you need here** (to differentiate the forms yourself):')
    D.T(['Function', 'Derivative', 'Rule'], [
        [r'$e^{st}$', r'$s\,e^{st}$', 'chain rule'],
        [r'$t\,e^{st}$', r'$(1+st)\,e^{st}$', 'product rule'],
        [r'$e^{\sigma t}\cos\omega t$', r'$e^{\sigma t}(\sigma\cos\omega t-\omega\sin\omega t)$', 'product rule'],
        [r'$e^{\sigma t}\sin\omega t$', r'$e^{\sigma t}(\sigma\sin\omega t+\omega\cos\omega t)$', 'product rule'],
    ])
    D.GRAPH(r'''
    title "Slide $k$ through 1: the same start, three kinds of response"
    x 0 8 label="$t$"
    y -0.6 1.2 label="$y$"
    slider k 0 5 0.5 step=0.05 label="$k$" animate
    let d "sqrt(abs(1-k))"
    let s1 "-1+d"
    let s2 "-1-d"
    curve "if(k<0.999, (s2*exp(s1*x)-s1*exp(s2*x))/(s2-s1), if(k>1.001, exp(-x)*(cos(d*x)+sin(d*x)/d), (1+x)*exp(-x)))" label="$y(t)$" color=1
    hline "0"
    readout "$b^2-4ac=4-4k$" "4-4*k"
    caption "$y\prime\prime+2y\prime+ky=0$, starting at $y(0)=1$, $y\prime(0)=0$. $k<1$: two real roots, the curve settles with no wiggle. $k=1$: one repeated root, the border case. $k>1$: complex roots, it wiggles inside the shrinking envelope $e^{-t}$."
    ''')
    D.CO('info', r'**Bonus (skip-safe): why $e^{st}$ turns the ODE into a quadratic.** Plug in $y=e^{st}$, $y\prime=se^{st}$, $y\prime\prime=s^2e^{st}$. Every term has $e^{st}$, so pull it out:'
         '\n\n$$\n' r'(as^2+bs+c)\,e^{st}=0' '\n$$\n\n'
         r'$e^{st}$ is never zero, so the bracket must be zero. That bracket is the characteristic equation.'
         '\n\n'
         r'For complex roots, Euler’s formula $e^{(\sigma\pm j\omega)t}=e^{\sigma t}(\cos\omega t\pm j\sin\omega t)$ turns the two exponentials into $\cos$ and $\sin$. That’s why the third row has no $j$ in it. '
         r'The extra $t$ for a repeated root comes from reduction of order (' + link('B7', 'b7') + ').')

    D.EX('W5 · Complex roots, real answer',
         r"Solve $y''+2y'+5y=0$, $\;y(0)=1$, $y'(0)=1$.",
         [S(r'**Type:** second order, plain-number coefficients, right side 0.'),
          S(r'**Characteristic equation** and roots. $\sqrt{4-20}=\sqrt{-16}=j4$.', r's^2+2s+5=0\quad\Rightarrow\quad s=\dfrac{-2\pm j4}{2}=-1\pm j2'),
          S(r'**Form:** complex row, with $\sigma=-1$ and $\omega=2$.', r'y=e^{-t}(A\cos2t+B\sin2t)'),
          S(r'**Conditions** straight from the table: $y(0)=A$ and $y\prime(0)=\sigma A+\omega B$.', r'A=1,\qquad -A+2B=1\ \Rightarrow\ B=1')],
         r'$y=e^{-t}(\cos2t+\sin2t)$. It wiggles at 2 rad/s, and the $e^{-t}$ shrinks the wiggle towards 0.')

    P(D, 'W5 · Two different real roots',
      r"Solve $y''+5y'+6y=0$, $\;y(0)=2$, $y'(0)=-5$.",
      [S(r'**Type:** plain-number coefficients, right side 0.'),
       S(r'**Characteristic equation:** it factors.', r's^2+5s+6=(s+2)(s+3)=0\quad\Rightarrow\quad s=-2,\,-3'),
       S(r'**Form:** two different real roots.', r'y=Ae^{-2t}+Be^{-3t}'),
       S(r'**Conditions** from the table: $y(0)=A+B$, $y\prime(0)=-2A-3B$.', r'A+B=2,\qquad -2A-3B=-5'),
       S(r'Multiply the first equation by 2 and add the second: $-B=-1$.', r'B=1,\qquad A=1')],
      r'$y=e^{-2t}+e^{-3t}$.')
    P(D, 'W5 · A repeated root',
      r"Solve $4y''+4y'+y=0$, $\;y(0)=4$, $y'(0)=0$.",
      [S(r'**Type:** plain-number coefficients, right side 0.'),
       S(r'**Characteristic equation:** it’s a perfect square.', r'4s^2+4s+1=(2s+1)^2=0\quad\Rightarrow\quad s=-\tfrac12\ \text{(twice)}'),
       S(r'**Form:** repeated root, so add the extra $t$.', r'y=(A+Bt)\,e^{-t/2}'),
       S(r'**Conditions:** $y(0)=A$, $y\prime(0)=sA+B$ with $s=-\frac12$.', r'A=4,\qquad -2+B=0\ \Rightarrow\ B=2')],
      r'$y=(4+2t)\,e^{-t/2}$.')
    P(D, 'W5 · No damping term',
      r"Solve $y''+9y=0$, $\;y(0)=2$, $y'(0)=3$.",
      [S(r'**Type:** plain-number coefficients, right side 0. There’s no $y\prime$ term, so $b=0$.'),
       S(r'**Characteristic equation:** $s^2+9=0$, so $s^2=-9$.', r's=\pm j3\qquad(\sigma=0,\ \omega=3)'),
       S(r'**Form:** complex row. $e^{0t}=1$, so the exponential drops out.', r'y=A\cos3t+B\sin3t'),
       S(r'**Conditions:** $y(0)=A$, $y\prime(0)=\omega B=3B$.', r'A=2,\qquad B=1')],
      r'$y=2\cos3t+\sin3t$. With $\sigma=0$ nothing shrinks it, so it swings forever. That’s the ideal LC circuit in ' + link('Topic D', 'topic-d') + '.', diff='intermediate')
    P(D, 'W5 · Work backwards from the roots',
      r'A constant-coefficient equation $y\prime\prime+by\prime+cy=0$ has characteristic roots $-3\pm j4$. ' '\n\n'
      r'(a) Find $b$ and $c$. (b) Write the general solution. (c) Find the solution with $y(0)=0$, $y\prime(0)=8$.',
      [S(r'**Type:** backwards. You have the roots, so build the quadratic as $(s-s_1)(s-s_2)=0$.'),
       S(r'(a) Multiply out $(s+3-j4)(s+3+j4)=(s+3)^2-(j4)^2=(s+3)^2+16$.', r's^2+6s+25=0\quad\Rightarrow\quad b=6,\ c=25'),
       S(r'(b) **Form:** complex row with $\sigma=-3$, $\omega=4$.', r'y=e^{-3t}(A\cos4t+B\sin4t)'),
       S(r'(c) **Conditions:** $y(0)=A=0$, and $y\prime(0)=\sigma A+\omega B=4B=8$.', r'A=0,\qquad B=2')],
      r'(a) $y\prime\prime+6y\prime+25y=0$. (b) $y=e^{-3t}(A\cos4t+B\sin4t)$. (c) $y=2e^{-3t}\sin4t$.', diff='advanced')


def verify():
    A, B = sp.symbols('A B')
    E = sp.exp
    # table: y(0) and y'(0) of each form
    s1, s2, s, sg, w = sp.symbols('s1 s2 s sigma omega')
    for form, y0, dy0 in ((A * E(s1 * t) + B * E(s2 * t), A + B, s1 * A + s2 * B),
                          ((A + B * t) * E(s * t), A, s * A + B),
                          (E(sg * t) * (A * sp.cos(w * t) + B * sp.sin(w * t)), A, sg * A + w * B)):
        zero(form.subs(t, 0) - y0)
        zero(sp.diff(form, t).subs(t, 0) - dy0)
    zero(sp.diff(t * E(s * t), t) - (1 + s * t) * E(s * t))
    zero(sp.diff(E(sg * t) * sp.cos(w * t), t) - E(sg * t) * (sg * sp.cos(w * t) - w * sp.sin(w * t)))
    zero(sp.diff(E(sg * t) * sp.sin(w * t), t) - E(sg * t) * (sg * sp.sin(w * t) + w * sp.cos(w * t)))
    # graph formulas: y'' + 2y' + k y = 0, y(0)=1, y'(0)=0 in all three cases
    for k in (sp.Rational(1, 2), 0):
        d = sp.sqrt(1 - k)
        r1, r2 = -1 + d, -1 - d
        second((r2 * E(r1 * t) - r1 * E(r2 * t)) / (r2 - r1), 1, 2, k, initial=(0, 1, 0))
    second((1 + t) * E(-t), 1, 2, 1, initial=(0, 1, 0))
    for k in (2, 5):
        d = sp.sqrt(k - 1)
        second(E(-t) * (sp.cos(d * t) + sp.sin(d * t) / d), 1, 2, k, initial=(0, 1, 0))
    # worked example and problems
    second(E(-t) * (sp.cos(2 * t) + sp.sin(2 * t)), 1, 2, 5, initial=(0, 1, 1))
    second(E(-2 * t) + E(-3 * t), 1, 5, 6, initial=(0, 2, -5))
    second((4 + 2 * t) * E(-t / 2), 4, 4, 1, initial=(0, 4, 0))
    second(2 * sp.cos(3 * t) + sp.sin(3 * t), 1, 0, 9, initial=(0, 2, 3))
    zero(sp.expand((s + 3 + 4 * sp.I) * (s + 3 - 4 * sp.I)) - (s ** 2 + 6 * s + 25))
    second(2 * E(-3 * t) * sp.sin(4 * t), 1, 6, 25, initial=(0, 0, 8))
