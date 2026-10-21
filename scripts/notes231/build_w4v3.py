"""Week 4: understand an implicit solution, reconstruct it, then make equations exact."""
import sympy as sp

from lib231 import Doc, S
from learning_notes import finish, implicit, potential, t, y, zero

D = Doc(4, 'Week 4: Exact Equations and Integrating Factors',
        ['exact_equations', 'integrating_factors'])
W = lambda *p: D.cite('W4', *p)

D.H('Calculus refresher: partial and implicit differentiation')
D.P(r'The same letter $y$ plays two different roles this week. When taking a **partial derivative**, hold the other variable fixed; when differentiating an equation along a solution $y(t)$, use the chain rule.')
D.T(['Task', 'Example', 'Reason'], [
    [r'Differentiate $ty^2$ partially in $t$', r'$\dfrac{\partial}{\partial t}(ty^2)=y^2$', r'Hold $y$ fixed: it behaves like a constant multiplier.'],
    [r'Differentiate $ty^2$ partially in $y$', r'$\dfrac{\partial}{\partial y}(ty^2)=2ty$', r'Hold $t$ fixed.'],
    [r'Differentiate $ty(t)^2$ along a curve', r'$\dfrac{d}{dt}(ty^2)=y^2+2tyy\prime$', r'Both $t$ and $y(t)$ change: product rule, then chain rule.'],
])
D.P(r'Integration with respect to one variable follows the same “hold the other fixed” idea: $\int2ty\,dt=t^2y+g(y)$. Any function $g(y)$ disappears when partially differentiated in $t$, so it is more general than adding just a number.')
D.PR('Check which variable is fixed · original',
     r'For $U(t,y)=t^2y+y^3$, find (a) $U_t=\partial U/\partial t$ and (b) $U_y=\partial U/\partial y$. Then find (c) $\int3y^2\,dt$.',
     [S('Hold y fixed for (a).', r'U_t=2ty'),
      S('Hold t fixed for (b).', r'U_y=t^2+3y^2'),
      S('In (c), y² is constant with respect to t.', r'\int3y^2\,dt=3ty^2+g(y)')],
     r'(a) $2ty$. (b) $t^2+3y^2$. (c) $3ty^2+g(y)$.')
D.H('Week 4 overview')
D.P('An exact equation describes a function that stays constant along its solutions. First see what that means, then learn to recover the function. Only after that will we introduce integrating factors for equations that are not already exact.')

D.H('Topic 1: What “exact” means', cites=W(1, 2, 3))
D.H('Begin with a curve you already understand', level=2)
D.P(r'The relation $t^2+y^2=9$ describes a circle. On a differentiable branch $y(t)$, differentiate both sides to get $2t+2yy\prime=0$; in differential form this is $2t\,dt+2y\,dy=0$.')
D.P(r'That equation says the quantity $U(t,y)=t^2+y^2$ does not change as you move along the solution. Solving the differential equation reverses this process: recover $U$, then write $U(t,y)=K$, with $K$ a constant.')
D.GRAPH(r'''
title "Each constant selects a different curve"
x -4 4 label="$t$"
y -4 4 label="$y$"
equal
slider K 1 12 9 step=1 label="$K$"
level "x^2+y^2" value="K" label="$t^2+y^2=K$" color=1
point "0" "sqrt(K)" label="positive branch at t=0"
caption "The whole circle is a level curve. A solution y(t) uses a branch; the top and bottom branches cannot be joined through a vertical tangent as one differentiable y(t)."
''')
D.H('Read M and N from the differential form', level=2)
D.EQ(r'M(t,y)\,dt+N(t,y)\,dy=0')
D.P(r'$M$ is the expression multiplying $dt$, and $N$ multiplies $dy$. Exactness means there is one underlying function $U$ with $U_t=M$ and $U_y=N$, so the left side is its total differential $dU$.')
D.EQ(r'dU=U_t\,dt+U_y\,dy')
D.P(r'To test exactness, compare $M_y=\partial M/\partial y$ with $N_t=\partial N/\partial t$. If they are equal, the equation is exact locally, assuming continuous partial derivatives on a neighbourhood; all the potentials constructed below are checked directly.')
D.EQ(r'\dfrac{\partial M}{\partial y}=\dfrac{\partial N}{\partial t}')
D.P('The cross derivatives agree because they would both differentiate the same U once in each variable. Do this test before trying to reconstruct U.')
D.PR('Identify and test; do not solve yet · lecture equations',
     r"Write $M,N$ and test exactness for:" '\n\n'
     r"1. $y'=\dfrac{t-y}{t+y}$." '\n'
     r"2. $y'=\dfrac{t}{t+y}$." '\n\n'
     'Cross-multiply, then move all terms to the left. Keep track of the minus sign.',
     [S('1. Move the dy term to the left.', r'(t-y)\,dt-(t+y)\,dy=0'),
      S('So M = t − y and N = −t − y; the test passes.', r'M_y=-1=N_t'),
      S('2. Here M = t and N = −t − y; the derivatives differ.', r'M_y=0\ne-1=N_t')],
     '1. Exact. 2. Not exact. The original slope formulas require t + y ≠ 0.', cites=W(3, 4))

D.H('Topic 2: Recover the function U', cites=W(1, 2, 3, 4))
D.H('Integrate one part, then use the other to finish', level=2)
D.P(r'Integrating $M$ with respect to $t$ gives part of $U$ and an unknown function $g(y)$. Differentiate that result in $y$ and match it to $N$ to discover what $g(y)$ must be.')
D.EX('A nonconstant “constant of integration” · original',
     r'Solve $2ty\,dt+(t^2+2y)\,dy=0$.',
     [S('Identify the two expressions and test them.', r'M_y=2t=N_t'),
      S('Integrate M in t, keeping y fixed.', r'U=t^2y+g(y)'),
      S('Differentiate in y and set it equal to N.', r't^2+g\prime(y)=t^2+2y'),
      S('The known t² terms cancel, leaving an ordinary integral in y.', r'g\prime(y)=2y\quad\Rightarrow\quad g(y)=y^2'),
      S('Combine the terms and set U equal to a constant.', r't^2y+y^2=K')],
     r'$t^2y+y^2=K$. A separate numeric constant inside $g$ can be absorbed into $K$.')
D.PR('Finish the lecture’s missing steps · Example 4.1',
     r'For $(2ty+3t^2)\,dt+t^2\,dy=0$, the test gives $M_y=N_t=2t$. After integrating $M$ we have $U=t^2y+t^3+g(y)$.' '\n\n'
     r'Find $U_y$, determine $g(y)$, and write the implicit solution.',
     [S('Differentiate in y; t³ is a constant for this partial derivative.', r'U_y=t^2+g\prime(y)'),
      S('Match N = t².', r'g\prime(y)=0'),
      S('A constant g is absorbed into the final arbitrary constant.', r't^2y+t^3=K')],
     r'$U_y=t^2+g\prime(y)$, $g$ is constant, and $t^2y+t^3=K$.', cites=W(1, 2))
D.P(r'You can start from $N$ instead: integrating $t^2$ in $y$ gives $U=t^2y+h(t)$. Matching $U_t=2ty+3t^2$ gives $h\prime(t)=3t^2$, so $h=t^3$ and the same answer results. Choose the easier integral.')
D.PR('A constant chooses a curve · lecture (a), added initial condition',
     r'The lecture equation $3t\,dt+4y\,dy=0$ gives $U=\frac32t^2+2y^2$. Write its solution without fractions, then choose the constant for $y(2)=2$.',
     [S('Set U equal to a constant and multiply by 2; rename the constant.', r'3t^2+4y^2=K'),
      S('Substitute the starting point.', r'K=3(2^2)+4(2^2)=28')],
     r'$3t^2+4y^2=28$. Near $(2,2)$, use the positive y-branch.', cites=W(3))
D.EX('From a slope equation to an IVP · lecture (b), added initial condition',
     r"Solve $y'=(t-y)/(t+y)$, $y(1)=0$.",
     [S('The earlier test showed exactness with M = t − y, N = −t − y.', r'(t-y)\,dt-(t+y)\,dy=0'),
      S('Integrate M in t; y is held fixed.', r'U=\dfrac{t^2}{2}-ty+g(y)'),
      S('Match the y-partial derivative to N.', r'-t+g\prime(y)=-t-y'),
      S('Integrate the remaining y-expression.', r'g(y)=-\dfrac{y^2}{2}'),
      S('Set U constant, multiply by 2, and use the start.', r't^2-2ty-y^2=K,\quad K=1'),
      S('Check using implicit differentiation and solve for the derivative.', r'2t-2y-2ty\prime-2yy\prime=0')],
     r'$t^2-2ty-y^2=1$, on the branch through $(1,0)$ where $t+y\ne0$. Differentiating recovers $y\prime=(t-y)/(t+y)$.', cites=W(3))
D.PR('A sign decides the test · lecture (c)',
     r'A student rewrites $2tyy\prime=t^2-y^2$ as $(t^2-y^2)\,dt+2ty\,dy=0$ and finds that it is not exact.' '\n\n'
     'Correct the rearrangement and solve the corrected equation.',
     [S('Moving the dy term left requires a minus sign.', r'(t^2-y^2)\,dt-2ty\,dy=0'),
      S('The corrected cross derivatives agree.', r'M_y=-2y=N_t'),
      S('Integrate M and match N; the remaining g is constant.', r'U=\dfrac{t^3}{3}-ty^2+g(y),\quad g\prime(y)=0'),
      S('Set U constant and multiply by 3.', r't^3-3ty^2=K')],
     r'The dy coefficient must be $-2ty$; the solution relation is $t^3-3ty^2=K$.', cites=W(4))
D.P(r'To check an answer $U=K$, either compare $U_t$ and $U_y$ with $M,N$, or differentiate along $y(t)$ and recover the original equation. An implicit relation describes possible curves; use a differentiable branch satisfying any original denominators and initial conditions.')

D.H('Topic 3: Make a non-exact equation exact', cites=W(4, 5))
D.P(r'An **integrating factor** $\mu$ multiplies both terms: $\mu M\,dt+\mu N\,dy=0$. We look for a multiplier that makes the new cross derivatives equal; where $\mu$ is finite and nonzero, this preserves the original equation.')
D.P('First test exactness. If it fails, try the following two tests separately; they find certain integrating factors, not every possible one.')
D.H('First try a factor depending only on t', level=2)
D.EQ(r'\dfrac{M_y-N_t}{N}=f(t)\quad\Rightarrow\quad\mu(t)=e^{\int f(t)\,dt}')
D.P(r'The ratio must simplify to a function of $t$ only. This follows by expanding $(\mu M)_y=(\mu N)_t$ with $\mu=\mu(t)$: the remaining equation is $\mu\prime/\mu=(M_y-N_t)/N$.')
D.EX('Find a t-only factor · original',
     r'Solve $(t^2+y^2+t)\,dt+ty\,dy=0$ with $y(1)=1$, taking $t>0$.',
     [S('The cross derivatives are 2y and y, so the equation is not exact.', r'\dfrac{M_y-N_t}{N}=\dfrac{2y-y}{ty}=\dfrac1t'),
      S('Integrate the ratio; on t > 0 the factor is t.', r'\mu=e^{\ln t}=t'),
      S('Multiply both terms and re-test.', r'(t^3+ty^2+t^2)\,dt+t^2y\,dy=0'),
      S('The new cross derivatives are both 2ty. Integrate in t and match N.', r'U=\dfrac{t^4}{4}+\dfrac{t^2y^2}{2}+\dfrac{t^3}{3}'),
      S('Multiply U = constant by 12 and apply the start.', r'3t^4+6t^2y^2+4t^3=13')],
     r'$3t^4+6t^2y^2+4t^3=13$, using the positive y-branch near $(1,1)$. The multiplier t is nonzero on the chosen domain.')
D.PR('Practise finding the factor only · original',
     r'For $2y\,dt+t\,dy=0$ on $t>0$, find the t-only integrating factor. Multiply both terms and check exactness; stop there.',
     [S('Here M = 2y, N = t.', r'\dfrac{M_y-N_t}{N}=\dfrac{2-1}{t}=\dfrac1t'),
      S('The factor is t.', r'2ty\,dt+t^2\,dy=0'),
      S('Differentiate the new coefficients across variables.', r'\dfrac{\partial(2ty)}{\partial y}=2t=\dfrac{\partial(t^2)}{\partial t}')],
     r'$\mu=t$. The multiplied equation is exact.')
D.H('If needed, try a factor depending only on y', level=2)
D.EQ(r'\dfrac{N_t-M_y}{M}=g(y)\quad\Rightarrow\quad\mu(y)=e^{\int g(y)\,dy}')
D.P('Notice both changes: the subtraction order reverses, and the denominator becomes M. This time the ratio must contain only y. A constant qualifies as a function of either variable.')
D.STEPS('Repair the lecture equation', [
    (r'y\,dt+(3+3t-y)\,dy=0', 'Identify M = y and N = 3 + 3t − y.'),
    (r'M_y=1,\quad N_t=3', 'The original equation is not exact.'),
    (r'\dfrac{M_y-N_t}{N}=\dfrac{-2}{3+3t-y}', 'The t-only test fails: this still contains y.'),
    (r'\dfrac{N_t-M_y}{M}=\hl{\dfrac2y}', 'The y-only test works away from y = 0.'),
    (r'\mu=e^{2\ln|y|}=\hl{y^2}', 'Integrate 2/y, then exponentiate.'),
    (r'\hl{y^3}\,dt+\hl{y^2}(3+3t-y)\,dy=0', 'Multiply both terms by the factor.'),
    (r'\dfrac{\partial(y^3)}{\partial y}=\hl{3y^2}=\dfrac{\partial[y^2(3+3t-y)]}{\partial t}', 'Re-test: the new equation is exact.'),
])
D.PR('Finish the repaired equation · Pre-tutorial 4',
     r'Solve $y^3\,dt+y^2(3+3t-y)\,dy=0$. Start by integrating $M=y^3$ with respect to $t$, then determine the missing function of $y$.',
     [S('Treat y³ as constant while integrating in t.', r'U=ty^3+h(y)'),
      S('Match the y-partial derivative to N.', r'3ty^2+h\prime(y)=3y^2+3ty^2-y^3'),
      S('Cancel the shared term, then integrate in y.', r'h\prime(y)=3y^2-y^3,\quad h=y^3-\dfrac{y^4}{4}'),
      S('Set U constant and multiply by 4.', r'4(t+1)y^3-y^4=K')],
     r'$4(t+1)y^3-y^4=K$.', cites=D.cite('T4', 1))
D.P(r'We multiplied the original equation by $y^2$, which vanishes on $y=0$. Check that line in the original equation separately: $y=0$ does solve it. Other branches must also be checked where the multiplier is zero or undefined; equivalence was guaranteed only where it was nonzero.')
D.PR('Choose the test instead of memorising its answer · original',
     r'For $t\,dt-(t+y)\,dy=0$, compute both ratios. Does either simple test supply a factor?',
     [S('For the t-only test, the ratio still contains y.', r'\dfrac{M_y-N_t}{N}=-\dfrac{1}{t+y}'),
      S('For the y-only test, the ratio contains t.', r'\dfrac{N_t-M_y}{M}=-\dfrac1t')],
     'Neither test works. This does not prove that no integrating factor exists; these two tests are limited.')
D.H('Connect this to Week 3', level=2)
D.P(r"Write a linear equation as $(a(t)y-f(t))\,dt+dy=0$. Here $M=a(t)y-f(t)$ and $N=1$, so $(M_y-N_t)/N=a(t)$. The t-only test therefore gives exactly Week 3’s factor $\mu=e^{\int a(t)dt}$.")


def verify():
    U=t**2*y+y**3
    zero(sp.diff(U,t)-2*t*y)
    zero(sp.diff(U,y)-(t**2+3*y**2))
    zero(sp.diff(3*t*y**2,t)-3*y**2)
    potential(2*t,2*y,t**2+y**2)
    potential(2*t*y,t**2+2*y,t**2*y+y**2)
    potential(2*t*y+3*t**2,t**2,t**2*y+t**3)
    potential(3*t,4*y,sp.Rational(3,2)*t**2+2*y**2)
    assert (3*t**2+4*y**2).subs({t:2,y:2})==28
    potential(t-y,-t-y,t**2/2-t*y-y**2/2)
    assert (t**2-2*t*y-y**2).subs({t:1,y:0})==1
    potential(t**2-y**2,-2*t*y,t**3/3-t*y**2)
    M,N=t**2+y**2+t,t*y
    zero((sp.diff(M,y)-sp.diff(N,t))/N-1/t)
    potential(t*M,t*N,t**4/4+t**2*y**2/2+t**3/3)
    assert (3*t**4+6*t**2*y**2+4*t**3).subs({t:1,y:1})==13
    potential(2*t*y,t**2,t**2*y)
    M,N=y,3+3*t-y
    zero((sp.diff(N,t)-sp.diff(M,y))/M-2/y)
    U=t*y**3+y**3-y**4/4
    potential(y**2*M,y**2*N,U)
    implicit(M,N,U)
    assert M.subs(y,0)==0
    M,N=t,-t-y
    zero((sp.diff(M,y)-sp.diff(N,t))/N+1/(t+y))
    zero((sp.diff(N,t)-sp.diff(M,y))/M+1/t)


if __name__ == '__main__':
    verify()
    finish(D, 'Week-4-Exact-Equations-and-Integrating-Factors.md')
