"""Week 6: find a second solution from a known one, then find particular solutions by guessing their form.

Sources: the professor's handwritten notes (Spiegel, Applied Differential Equations pp. 153, 158, 164),
uploaded as course sources; tags W6 (4 pages) and N6 (1 page) in cites.json. No typed lecture or pre-tutorial.
"""
import sympy as sp

from lib231 import Doc, S, steps_fence
from learning_notes import finish, second, t, zero

D = Doc(6, 'Week 6: Reduction of Order and Undetermined Coefficients',
        ['reduction_of_order', 'undetermined_coefficients'])
W = lambda *p: D.cite('W6', *p)

D.H('Calculus refresher: the product rule twice, and squared trig')
D.P(r'This week you substitute $y=y_1v$, where $y_1$ is a known function and $v$ an unknown one. Differentiating a product twice gives a middle term with a 2 in front:')
D.T(['Expression', 'Result', 'Rule'], [
    [r'$(y_1v)\prime$', r'$y_1\prime v+y_1v\prime$', 'Product rule.'],
    [r'$(y_1v)\prime\prime$', r'$y_1\prime\prime v+2y_1\prime v\prime+y_1v\prime\prime$', 'Product rule again; the two middle terms combine.'],
    [r'$\int\frac1z\,dz$', r'$\ln|z|$', 'Used when separating a first-order equation.'],
    [r'$\cos^2t$', r'$\frac12+\frac12\cos2t$', 'Double-angle identity: removes the square.'],
    [r'$\sin^2t$', r'$\frac12-\frac12\cos2t$', 'Same identity, opposite sign.'],
])
D.P(r'Some integrals, such as $\int e^{t^2/2}/t^2\,dt$, have no formula in ordinary functions. Leave them as an integral: that is a complete answer.')
D.PR('Differentiate a product twice; remove a square · original',
     r'(a) Find $(tv)\prime\prime$, where $v(t)$ is unknown. (b) Write $8\sin^2t$ as a constant plus a cosine.',
     [S('First derivative: product rule.', r"(tv)'=v+tv'"),
      S('Differentiate again; v′ appears twice.', r"(tv)''=v'+v'+tv''=2v'+tv''"),
      S('Multiply the sin² identity by 8.', r'8\sin^2t=4-4\cos2t')],
     r"(a) $tv''+2v'$. (b) $4-4\cos2t$.")

D.H('Week 6 overview')
D.P('Week 6 has two methods for second-order linear ODEs:')
D.L([r'**Reduction of order:** you know one solution $y_1$ of a homogeneous equation; find the second one.',
     r'**Undetermined coefficients:** the equation has a forcing term $g(t)$; guess the form of a particular solution from $g$.'])
D.P(r'Both come from the professor’s handwritten notes (Spiegel, *Applied Differential Equations*). The Week 6 tutorial problem is Example 4. The notes write $\dot y,\ \ddot y$ for $y\prime,\ y\prime\prime$.')

D.H('Topic 1: Reduction of order', cites=W(1, 2))
D.H('Multiply the known solution by an unknown function', level=2)
D.P(r'Suppose $y_1$ solves a second-order linear homogeneous ODE. Look for the second solution as $y=y_1v$, where $v(t)$ is unknown.')
D.P('The recipe:')
D.L([r'**Substitute** $y=y_1v$, using the product rule for $y\prime$ and $y\prime\prime$.',
     r'**Collect terms:** every term with plain $v$ cancels, because $y_1$ is a solution.',
     r'**Set $z=v\prime$:** what remains is a first-order equation in $z$ (the order went down by one).',
     r'**Solve for $z$**, then integrate once more: $v=\int z\,dt$.',
     r'**Multiply back:** $y=y_1v$.'])
D.STEPS('Lecture: reduce y″ − t y′ + y = 0, given y = t', [
    (r"y''-ty'+y=0,\qquad y_1=t", 'Check: $y_1=t$ gives $0-t+t=0$.'),
    (r'y=\hl{tv}', 'Multiply the known solution by an unknown $v$.'),
    (r"y'=\hl{v+tv'},\qquad y''=\hl{2v'+tv''}", 'Product rule (refresher table).'),
    (r"(2v'+tv'')-t(v+tv')+tv=0", 'Substitute all three into the ODE.'),
    (r"\hl{tv''+(2-t^2)v'}=0", 'Collect terms. The $-tv$ and $+tv$ cancel, as promised.'),
    (r"t\hl{z'}+(2-t^2)\hl{z}=0,\qquad z=v'", r'Only $v\prime$ and $v\prime\prime$ remain: first order in $z$.'),
], intro='The professor’s example, step by step:')
D.EX('Finish the lecture example · handwritten notes p. 1–2',
     r"Solve $tz'+(2-t^2)z=0$ (from the stepper above), then find the general solution of $y''-ty'+y=0$ for $t\ne0$.",
     [S('The equation is separable. Divide by $tz$ and move the $t$ terms right.', r'\dfrac{dz}{z}=\dfrac{t^2-2}{t}\,dt=\left(t-\dfrac2t\right)dt'),
      S(r'Integrate both sides: $\int\frac1z\,dz=\ln|z|$.', r'\ln|z|=\dfrac{t^2}2-2\ln|t|+C'),
      S(r'Exponentiate; $e^{-2\ln|t|}=1/t^2$.', r'z=C_1\,\dfrac{e^{t^2/2}}{t^2}'),
      S(r'$z=v\prime$, so integrate again. The integral has no closed form, so it stays.', r'v=C_1\int\dfrac{e^{t^2/2}}{t^2}\,dt+C_2'),
      S(r'Multiply back by $y_1=t$.', r'y=tv')],
     r'$y=C_2\,t+C_1\,t\displaystyle\int\frac{e^{t^2/2}}{t^2}\,dt$. The known solution $t$ reappears as the $C_2$ term.',
     cites=W(1, 2))
D.H(r'Where the repeated-root $te^{st}$ comes from', level=2)
D.EX('Reduce a constant-coefficient equation · original',
     r"$y''+4y'+4y=0$ has the repeated root $s=-2$, so $y_1=e^{-2t}$. Use reduction of order to find the second solution.",
     [S(r'Set $y=e^{-2t}v$ and differentiate with the product rule.', r"y'=e^{-2t}(v'-2v)"),
      S('Differentiate again.', r"y''=e^{-2t}(v''-4v'+4v)"),
      S(r'Substitute and divide by $e^{-2t}$. The $v\prime$ terms cancel too.', r"(v''-4v'+4v)+4(v'-2v)+4v=v''=0"),
      S('Integrate twice.', r'v=C_1+C_2t')],
     r'$y=(C_1+C_2t)e^{-2t}$: exactly the Week 5 repeated-root form. The extra $t$ is $v$.')
D.CO('tip', r'**Check with the formula.** Write the ODE as $y\prime\prime+p(t)y\prime+q(t)y=0$. Reduction of order always ends at'
     '\n\n'
     '$$\n' r'y_2=y_1\int\frac{e^{-\int p\,dt}}{y_1^2}\,dt' '\n$$'
     '\n\n'
     r'Lecture example: $p=-t$, so $e^{-\int p\,dt}=e^{t^2/2}$ and $y_1^2=t^2$, matching Example 1.')
D.PR('A second solution with a logarithm · original',
     r"For $t>0$, $y_1=t^2$ solves $t^2y''-3ty'+4y=0$. Find the general solution.",
     [S(r'Set $y=t^2v$ and use the product rule twice.', r"y'=2tv+t^2v',\qquad y''=2v+4tv'+t^2v''"),
      S(r'Substitute; the plain $v$ terms cancel ($2-6+4=0$).', r"t^4v''+t^3v'=0"),
      S(r'Divide by $t^4$ and set $z=v\prime$.', r"z'+\dfrac zt=0"),
      S(r'Separate: $\int\frac{dz}{z}=-\int\frac{dt}{t}$, so $\ln|z|=-\ln t+C$.', r'z=\dfrac{C_2}t'),
      S(r'Integrate: $\int\frac1t\,dt=\ln t$ for $t>0$.', r'v=C_1+C_2\ln t')],
     r'$y=C_1t^2+C_2t^2\ln t$.')

D.H('Topic 2: Undetermined coefficients', cites=W(3, 4) + D.cite('N6', 1))
D.H('Total solution = complementary + particular', level=2)
D.P(r'Now the right side is a forcing term: $ay\prime\prime+by\prime+cy=g(t)$.')
D.L([r'$y_c$: the **complementary solution**, the general solution with $g=0$ (Week 5). It holds the two constants.',
     r'$y_p$: one **particular solution**, any single function that produces $g(t)$. No constants.',
     r'$y=y_c+y_p$: the general solution.'])
D.P(r'To find $y_p$, guess a form that looks like $g(t)$ with unknown coefficients, substitute, and match coefficients on both sides.')
D.T([r'Term in $g(t)$', r'Guess for $y_p$'], [
    [r'constant or polynomial of degree $n$', r'$A_nt^n+\dots+A_1t+A_0$ (all lower powers)'],
    [r'$e^{at}$', r'$Ae^{at}$'],
    [r'$\sin rt$ or $\cos rt$', r'$A\cos rt+B\sin rt$ (always both)'],
    [r'$e^{at}\cos rt$ or $e^{at}\sin rt$', r'$e^{at}(A\cos rt+B\sin rt)$'],
    [r'a sum of these', 'the sum of their guesses'],
], cites=D.cite('N6', 1))
D.EX('A polynomial guess needs every lower power · original',
     r"Find the general solution of $y''+y'-2y=2t$.",
     [S(r'Complementary: $s^2+s-2=(s+2)(s-1)$.', r'y_c=C_1e^t+C_2e^{-2t}'),
      S(r'$2t$ has degree 1, so guess $At+B$. The $B$ is needed even though $g$ has no constant.', r"y_p=At+B,\quad y_p'=A,\quad y_p''=0"),
      S('Substitute.', r'A-2(At+B)=2t'),
      S(r'Match the $t$ terms, then the constants.', r'-2A=2,\qquad A-2B=0'),
      S('Solve.', r'A=-1,\qquad B=-\tfrac12')],
     r'$y=C_1e^t+C_2e^{-2t}-t-\tfrac12$. Guessing only $At$ fails: the constant $A$ left over has nothing to match.')
D.EX('The Week 6 tutorial problem (also the lecture example) · tutorial 6, notes p. 3–4',
     r"Solve $\ddot y+y=6\cos^2t$ with $y(0)=0$ and $y(\pi/2)=0$. The tutorial gives the forms $y_c=c_1\sin t+c_2\cos t$ and $y_p=A+B\cos2t+D\sin2t$.",
     [S(r'Complementary: $s^2+1=0$ gives $s=\pm j$.', r'y_c=c_1\sin t+c_2\cos t'),
      S('Remove the square with the identity, so the guess table applies.', r'6\cos^2t=3+3\cos2t'),
      S('Constant → $A$; cos 2t → both cos 2t and sin 2t.', r'y_p=A+B\cos2t+D\sin2t'),
      S(r'Differentiate twice: each derivative brings out a 2.', r"y_p''=-4B\cos2t-4D\sin2t"),
      S(r'Substitute $y_p\prime\prime+y_p$ and collect.', r'A-3B\cos2t-3D\sin2t=3+3\cos2t'),
      S('Match constants, cosines and sines.', r'A=3,\qquad B=-1,\qquad D=0'),
      S(r'Add $y_c$ **before** using the conditions: they apply to the whole $y$.', r'y=3-\cos2t+c_1\sin t+c_2\cos t'),
      S(r'$y(0)=0$: $\sin0=0$, $\cos0=1$.', r'3-1+c_2=0\quad\Rightarrow\quad c_2=-2'),
      S(r'$y(\pi/2)=0$: $\cos\pi=-1$, $\sin\frac\pi2=1$, $\cos\frac\pi2=0$.', r'3+1+c_1=0\quad\Rightarrow\quad c_1=-4')],
     r'$y=3-\cos2t-4\sin t-2\cos t$.', cites=D.cite('T6', 1) + W(3, 4))
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
D.H(r'When the guess is already in $y_c$: multiply by $t$', level=2)
D.P(r'If a term of your guess already solves the homogeneous equation, substituting it gives $0$, so it can never produce $g$.')
D.P(r'**Fix:** multiply that guess by $t$. If the result is still in $y_c$ (a repeated root), multiply by $t^2$.')
D.EX('The guess is already in the complementary solution · original',
     r"Find a particular solution of $y''-y'-2y=3e^{2t}$.",
     [S(r'Complementary: $s^2-s-2=(s-2)(s+1)$.', r'y_c=C_1e^{2t}+C_2e^{-t}'),
      S(r'The table says $Ae^{2t}$, but that is in $y_c$: it gives $0=3e^{2t}$. Multiply by $t$.', r'y_p=Ate^{2t}'),
      S('Product rule, twice.', r"y_p'=A(1+2t)e^{2t},\qquad y_p''=A(4+4t)e^{2t}"),
      S(r'Substitute and divide by $e^{2t}$. The $t$ terms cancel.', r'A\big[(4+4t)-(1+2t)-2t\big]=3A=3'),
      S('Solve.', r'A=1')],
     r'$y_p=te^{2t}$, so $y=C_1e^{2t}+C_2e^{-t}+te^{2t}$.')
D.GRAPH(r'''
title "Why the extra t: forcing at the natural frequency"
x 0 12 label="$t$"
y -25 25 label="$y$"
slider w 1 3 1.5 step=0.05 label="$\omega$" animate
curve "if(abs(w-2)<0.001, sin(2*x)-2*x*cos(2*x), 8/(4-w^2)*(sin(w*x)-w/2*sin(2*x)))" label="$y(t)$, starting at rest" color=1
curve "2*x" label="$\pm2t$" color=0 dash
curve "-2*x" color=0 dash
caption "Solutions of $y''+4y=8\sin\omega t$ with $y(0)=y'(0)=0$. Here $y_c$ contains $\sin2t$ and $\cos2t$. For $\omega$ far from 2 the swing stays small. At $\omega=2$ the forcing is in $y_c$, the particular solution has the extra $t$, and the swing grows along $\pm2t$."
''')
D.PR('Choose the form; do not solve · original',
     r"For $y''-2y'+y=g(t)$, write the guess for $y_p$ when $g$ is (a) $t^2$, (b) $e^{-t}$, (c) $e^t$, (d) $\cos t$.",
     [S(r'Complementary first: $s^2-2s+1=(s-1)^2$, a repeated root.', r'y_c=(C_1+C_2t)e^t'),
      S('(a) Degree 2: all lower powers.', r'At^2+Bt+C'),
      S(r'(b) $e^{-t}$ is not in $y_c$.', r'Ae^{-t}'),
      S(r'(c) $Ae^t$ and $Ate^t$ are both in $y_c$, so multiply by $t^2$.', r'At^2e^t'),
      S('(d) Cosine needs both cosine and sine.', r'A\cos t+B\sin t')],
     r'(a) $At^2+Bt+C$. (b) $Ae^{-t}$. (c) $At^2e^t$. (d) $A\cos t+B\sin t$.')
D.PR('A trig guess that is already in the complementary solution · original',
     r"Find a particular solution of $y''+9y=12\cos3t$. Use $(tf)\prime\prime=tf\prime\prime+2f\prime$ from Try it 1.",
     [S(r'$y_c=c_1\cos3t+c_2\sin3t$ already contains $\cos3t$, so multiply the guess by $t$.', r'y_p=t\,f,\qquad f=A\cos3t+B\sin3t'),
      S(r'Since $f\prime\prime=-9f$, the $t$ terms cancel in $y_p\prime\prime+9y_p$.', r"y_p''+9y_p=t(f''+9f)+2f'=2f'"),
      S(r'Differentiate $f$.', r"2f'=-6A\sin3t+6B\cos3t"),
      S('Match with 12 cos 3t.', r'6B=12,\qquad -6A=0')],
     r'$A=0$, $B=2$: $y_p=2t\sin3t$. The swing grows like $2t$, as in the graph above.')


def verify():
    E = sp.exp
    C1, C2, A, B = sp.symbols('C1 C2 A B')
    v = sp.Function('v')(t)
    # refresher
    zero(sp.diff(t*v, t, 2) - (2*sp.diff(v, t) + t*sp.diff(v, t, 2)))
    zero(8*sp.sin(t)**2 - (4 - 4*sp.cos(2*t)))
    zero(sp.cos(t)**2 - (sp.Rational(1, 2) + sp.cos(2*t)/2))
    # lecture reduction: y=t v reduces y''-ty'+y to t v''+(2-t^2)v'
    y = t*v
    zero(sp.diff(y, t, 2) - t*sp.diff(y, t) + y - (t*sp.diff(v, t, 2) + (2 - t**2)*sp.diff(v, t)))
    zero(sp.diff(t, t, 2) - t*sp.diff(t, t) + t)
    z = E(t**2/2)/t**2
    zero(t*sp.diff(z, t) + (2 - t**2)*z)
    # Abel-formula check: e^{-int p} / y1^2 with p=-t
    zero(E(-sp.integrate(-t, t))/t**2 - z)
    # repeated root by reduction
    y = E(-2*t)*v
    zero((sp.diff(y, t, 2) + 4*sp.diff(y, t) + 4*y)/E(-2*t) - sp.diff(v, t, 2))
    zero(sp.diff(y, t) - E(-2*t)*(sp.diff(v, t) - 2*v))
    zero(sp.diff(y, t, 2) - E(-2*t)*(sp.diff(v, t, 2) - 4*sp.diff(v, t) + 4*v))
    second((C1 + C2*t)*E(-2*t), 1, 4, 4)
    # t^2 y'' - 3t y' + 4y = 0
    tp = sp.symbols('tp', positive=True)
    y = tp**2*v.subs(t, tp)
    vv = v.subs(t, tp)
    zero(tp**2*sp.diff(y, tp, 2) - 3*tp*sp.diff(y, tp) + 4*y - (tp**4*sp.diff(vv, tp, 2) + tp**3*sp.diff(vv, tp)))
    for sol in (tp**2, tp**2*sp.log(tp)):
        zero(tp**2*sp.diff(sol, tp, 2) - 3*tp*sp.diff(sol, tp) + 4*sol)
    # polynomial guess
    second(C1*E(t) + C2*E(-2*t) - t - sp.Rational(1, 2), 1, 1, -2, 2*t)
    # lecture undetermined coefficients
    sol = 3 - sp.cos(2*t) - 4*sp.sin(t) - 2*sp.cos(t)
    second(sol, 1, 0, 1, 6*sp.cos(t)**2)
    zero(sol.subs(t, 0))
    zero(sol.subs(t, sp.pi/2))
    second(3 - sp.cos(2*t), 1, 0, 1, 3 + 3*sp.cos(2*t))
    # correction rule (exponential)
    second(t*E(2*t), 1, -1, -2, 3*E(2*t))
    second(E(2*t), 1, -1, -2, 0)
    yp = A*t*E(2*t)
    zero(sp.simplify((sp.diff(yp, t, 2) - sp.diff(yp, t) - 2*yp)/E(2*t)) - 3*A)
    # resonance graph: y''+4y=8 sin(w t), y(0)=y'(0)=0, and its w=2 limit
    w = sp.Rational(3, 2)
    second(8/(4 - w**2)*(sp.sin(w*t) - w/2*sp.sin(2*t)), 1, 0, 4, 8*sp.sin(w*t), initial=(0, 0, 0))
    second(sp.sin(2*t) - 2*t*sp.cos(2*t), 1, 0, 4, 8*sp.sin(2*t), initial=(0, 0, 0))
    # choose-the-form answers really work (with numbers)
    second(sp.Rational(1, 2)*t**2*E(t), 1, -2, 1, E(t))
    second(t**2 + 4*t + 6, 1, -2, 1, t**2)
    second(E(-t)/4, 1, -2, 1, E(-t))
    second(-sp.sin(t)/2, 1, -2, 1, sp.cos(t))
    # trig correction
    second(2*t*sp.sin(3*t), 1, 0, 9, 12*sp.cos(3*t))
    f = A*sp.cos(3*t) + B*sp.sin(3*t)
    zero(sp.diff(t*f, t, 2) + 9*t*f - 2*sp.diff(f, t))


if __name__ == '__main__':
    verify()
    finish(D, 'Week-6-Reduction-of-Order-and-Undetermined-Coefficients.md')
