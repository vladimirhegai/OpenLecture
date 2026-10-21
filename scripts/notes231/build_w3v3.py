"""Week 3: progressively learn separation, integrating factors, and local IVP theory."""
import sympy as sp

from lib231 import Doc, S
from learning_notes import K, finish, first, implicit, t, y, zero

D = Doc(3, 'Week 3: Linear and Separable First-Order ODEs; Existence and Uniqueness',
        ['linear_first_order', 'separable_odes', 'existence_uniqueness'])
W = lambda *p: D.cite('W3', *p)
T = D.cite('T3', 1)

D.H('Calculus refresher: integrate, then check by differentiating')
D.P('Week 2 gave you solution families. This week you learn how to find them: rearrange the equation until integrating can undo its derivatives.')
D.P(r'Add an arbitrary constant $K$ to each indefinite integral below.')
D.T(['Integral', 'Detail that is easy to forget'], [
    [r'$\int t^n\,dt=\dfrac{t^{n+1}}{n+1}$', r'Increase the power by one and divide by the new power; this excludes $n=-1$.'],
    [r'$\int\dfrac{1}{t}\,dt=\ln|t|$', r'The logarithm is the special case. Work on an interval that avoids $t=0$.'],
    [r'$\int e^{at}\,dt=\dfrac{1}{a}e^{at}$', r'Divide by the constant $a\ne0$; differentiation would multiply by it.'],
])
D.P(r'**Substitution** reverses the chain rule. For $\int\dfrac{2t}{1+t^2}\,dt$, choose $u=1+t^2$; then $du=2t\,dt$, so the integral becomes $\int du/u=\ln(1+t^2)+K$.')
D.P(r'Keep the differential with its variable: integrate $y\,dy$ with respect to $y$, and $t\,dt$ with respect to $t$. After integrating both sides of an equation, one free constant is enough because two constants can be combined.')
D.PR('Two small integration checks · original',
     r'Find: (a) $\int y^{-2}\,dy$; (b) $\int 6e^{3t}\,dt$. Check each by differentiating.',
     [S('For (a), the new power is −1; divide by −1.', r'\int y^{-2}\,dy=-y^{-1}+K'),
      S('For (b), divide by the exponent coefficient 3.', r'\int6e^{3t}\,dt=2e^{3t}+K')],
     r'(a) $-1/y+K$, for $y\ne0$. (b) $2e^{3t}+K$.')
D.H('Week 3 overview')
D.P('First learn separation, which puts each variable on its own side. Then learn the integrating factor for linear equations. Finally, ask what can be guaranteed about an IVP before solving it; those guarantees are a different task from finding a formula.')

D.H('Topic 1: Separable equations', cites=W(3, 4))
D.H('Separate first; integrate second', level=2)
D.P(r"An equation is **separable** when $y'=g(t)h(y)$: a function of $t$ multiplied by a function of $y$. The aim is to put the $y$-expression beside $dy$ and the $t$-expression beside $dt$.")
D.EQ(r'\dfrac{1}{h(y)}\,dy=g(t)\,dt')
D.P(r'This rearrangement assumes $h(y)\ne0$. Whenever you divide by an expression involving the unknown, check its zero cases in the original equation too.')
D.EX('A first complete separation · original',
     r"Solve $y'=2ty$ with $y(0)=3$.",
     [S(r'For $y\ne0$, separate the variables.', r'\dfrac{dy}{y}=2t\,dt'),
      S('Integrate each side in its own variable.', r'\ln|y|=t^2+K'),
      S(r'Exponentiate. Combine the constant and the possible sign into $A$.', r'y=Ae^{t^2}'),
      S(r'Use $y(0)=3$, so $A=3$.', r'y=3e^{t^2}')],
     r'$y=3e^{t^2}$. The divided-out case $y=0$ also solves the ODE, but fails this initial condition.')
D.PR('Only do the separation · warm-up and lecture equation',
     'Rearrange each equation so it is ready to integrate. **Stop before integrating.**\n\n'
     r"1. $y'=t(1+y^2)$" '\n'
     r"2. $y'=\dfrac{3t+ty^2}{y+t^2y}$",
     [S('1. Divide by the positive expression 1 + y².', r'\dfrac{dy}{1+y^2}=t\,dt'),
      S('2. Factor numerator and denominator before rearranging.', r"y'=\dfrac{t(3+y^2)}{y(1+t^2)}"),
      S('Keep every y-term on the left.', r'\dfrac{y}{3+y^2}\,dy=\dfrac{t}{1+t^2}\,dt')],
     r'1. $dy/(1+y^2)=t\,dt$. 2. $\dfrac{y}{3+y^2}\,dy=\dfrac{t}{1+t^2}\,dt$; the original equation requires $y\ne0$.', cites=W(4))
D.EX('Finish the factored equation · lecture Example 3.3',
     r'Use the separated form from question 2, now with $y(1)=3$.',
     [S('On both sides, the numerator is half the derivative of the denominator.', r'\dfrac12\ln(3+y^2)=\dfrac12\ln(1+t^2)+K'),
      S('Multiply by 2 and exponentiate; call the positive constant A.', r'3+y^2=A(1+t^2)'),
      S('Use the initial condition before choosing a square-root branch.', r'3+3^2=A(1+1^2)\quad\Rightarrow\quad A=6'),
      S('The positive branch matches y(1) = 3.', r'y=\sqrt{6t^2+3}')],
     r'$y=\sqrt{6t^2+3}$ for all real $t$. It stays positive, so the original denominator never vanishes.', cites=W(4))
D.PR('Use an initial value and choose the interval · Pre-tutorial 3(a)',
     r"Solve $y'=-t/y$ with $y(1)=2$. After finding the formula, identify the largest open interval containing $t=1$ where it satisfies the original ODE.",
     [S('Multiply by y and separate.', r'y\,dy=-t\,dt'),
      S('Integrate, then absorb the factor 2 into the constant.', r'y^2+t^2=K'),
      S('Use the starting point and choose its positive branch.', r'K=2^2+1^2=5,\qquad y=\sqrt{5-t^2}'),
      S('The original equation divides by y, so exclude the endpoints where y = 0.', r'-\sqrt5<t<\sqrt5')],
     r'$y=\sqrt{5-t^2}$ on $(-\sqrt5,\sqrt5)$.', cites=T)
D.H('Two things integration can hide', level=2)
D.P(r'**A lost solution:** for $y\prime=y^2/t^3$, separating divides by $y^2$. Integration gives $-1/y=-1/(2t^2)+K$, or $y=2t^2/(1-2Kt^2)$, but $y=0$ also solves the original equation and must be included separately.')
D.P(r'Here $t\ne0$, and the displayed denominator must also stay nonzero. Keep the solution on a connected interval avoiding those restrictions.', cites=W(4))
D.P(r'**An implicit answer:** sometimes integration gives a relation between $t$ and $y$ that you cannot conveniently rearrange into $y=\cdots$. That relation can still describe a solution; check it by implicit differentiation.')
D.PR('Solve in differential form · Pre-tutorial 3(b)',
     r'Solve $3t(y^2+1)\,dt+y(t^2+2)\,dy=0$. An implicit answer is enough.',
     [S('Move the dt-term and divide by the positive factors.', r'\dfrac{y}{y^2+1}\,dy=-\dfrac{3t}{t^2+2}\,dt'),
      S('Use substitution on both sides.', r'\dfrac12\ln(y^2+1)=-\dfrac32\ln(t^2+2)+K'),
      S('Multiply by 2, combine logs, and exponentiate.', r'(y^2+1)(t^2+2)^3=A')],
     r'$(y^2+1)(t^2+2)^3=A$, with $A>0$ for real solution points. A differentiable branch must still satisfy the original equation.', cites=T)
D.P(r'The lecture’s other implicit example is $y\,dt+t^3(y^2+1)\,dy=0$. For $t\ne0$ and $y\ne0$, separation gives $(y+1/y)\,dy=-t^{-3}\,dt$, hence $y^2+2\ln|y|-t^{-2}=K$. Check $y=0$ separately: it also solves the original differential form.', cites=W(4))

D.H('Topic 2: Linear equations and integrating factors', cites=W(1, 2, 3))
D.H('Make the derivative stand alone first', level=2)
D.P(r"A first-order linear equation has standard form $y'+a(t)y=f(t)$. The coefficient $a(t)$ and forcing $f(t)$ may depend on $t$, but not on the unknown $y$.")
D.PR('Identify the coefficient before doing calculus · original',
     r"Put each equation into standard form and identify $a(t)$ and $f(t)$." '\n\n'
     r"1. $y'=3y+6$" '\n'
     r"2. $ty'+2y=4t^2$, with $t>0$.",
     [S('1. Move 3y left and keep its negative sign.', r"y'-3y=6,\quad a=-3,\quad f=6"),
      S('2. Divide every term by t.', r"y'+\dfrac2t y=4t,\quad a=\dfrac2t,\quad f=4t")],
     r'1. $a=-3$, $f=6$. 2. $a=2/t$, $f=4t$.')
D.H('Why multiplying helps', level=2)
D.P(r"The product rule says $(\mu y)'=\mu y'+\mu'y$, where $\mu$ is a function of $t$. If we choose $\mu$ so that $\mu'=a\mu$, multiplying the linear ODE by it makes the entire left side one derivative.")
D.STEPS('Build the integrating-factor method', [
    (r"y'+a(t)y=f(t)", 'Start in standard form.'),
    (r'\mu=e^{\int a(t)\,dt}', 'This choice has derivative μ′ = aμ.'),
    (r"\mu y'+\hl{\mu a}y=\mu f", 'Multiply every term by μ.'),
    (r"\hl{(\mu y)'}=\mu f", 'Recognise the product rule backwards.'),
    (r'\mu y=\hl{\int\mu f\,dt+K}', 'Integrate once.'),
    (r'y=\hl{\dfrac{1}{\mu}}\left(\int\mu f\,dt+K\right)', 'Divide by μ, then use the initial condition.'),
])
D.P(r'Use one convenient antiderivative inside $\mu$; you do not need an extra integration constant there. Multiplying $\mu$ by a nonzero constant would give an equivalent method.')
D.EX('Use the method with simple numbers · original',
     r"Solve $y'+2y=6$, $y(0)=1$. This recovers Week 2’s solution without being given its family.",
     [S('The coefficient is 2, so compute the factor.', r'\mu=e^{\int2\,dt}=e^{2t}'),
      S('Multiply and recognise the product derivative.', r'\dfrac{d}{dt}(e^{2t}y)=6e^{2t}'),
      S('Integrate; divide by 2 when integrating the exponential.', r'e^{2t}y=3e^{2t}+K'),
      S('Divide by the factor and use the starting value.', r'y=3+Ke^{-2t},\quad 1=3+K'),
      S('The initial condition sets K = −2.', r'y=3-2e^{-2t}')],
     r'$y=3-2e^{-2t}$.')
D.PR('A coefficient that varies with time · original',
     r"Finish $ty'+2y=4t^2$, $y(1)=2$, on $t>0$. You already found its standard form above. Find the integrating factor, integrate, and apply the condition.",
     [S('Integrate 2/t and simplify the exponential.', r'\mu=e^{2\ln t}=t^2'),
      S('Multiply the standard form by t².', r'\dfrac{d}{dt}(t^2y)=4t^3'),
      S('Integrate and divide by t².', r't^2y=t^4+K,\qquad y=t^2+\dfrac{K}{t^2}'),
      S('At t = 1, the given value is 2.', r'2=1+K\quad\Rightarrow\quad K=1')],
     r'$y=t^2+1/t^2$ on $t>0$.')
D.H('Choose a method, then handle a harder integral', level=2)
D.PR('Separable, linear, both, or neither? · original',
     'Identify the method; do not solve.\n\n'
     r"1. $y'=t^2+y$" '\n'
     r"2. $y'=e^{t+y}$" '\n'
     r"3. $y'=2y-6$" '\n'
     r"4. $y'=t+y^2$",
     [S('1. Linear; its sum does not separate into a t-factor times a y-factor.'),
      S(r'2. Write $e^{t+y}=e^te^y$: separable, nonlinear.'),
      S('3. Linear and separable; the right side is a function of y alone.'),
      S('4. Neither linear nor separable.')],
     '1. Linear only. 2. Separable only. 3. Both. 4. Neither.')
D.EX('Use substitution inside the method · lecture Example 3.1',
     r"Solve $y'+\dfrac{10}{2t+5}y=10$, $y(0)=0$.",
     [S(r'Use $u=2t+5$, $du=2\,dt$ to integrate the coefficient.', r'\int\dfrac{10}{2t+5}\,dt=5\ln|2t+5|'),
      S(r'The interval containing 0 has $t>-5/2$, so $2t+5>0$.', r'\mu=(2t+5)^5'),
      S('Multiply; the left side becomes a product derivative.', r'\dfrac{d}{dt}\big[(2t+5)^5y\big]=10(2t+5)^5'),
      S('Use the same substitution on the right.', r'(2t+5)^5y=\dfrac56(2t+5)^6+K'),
      S('Apply y(0) = 0 before dividing.', r'0=\dfrac56\,5^6+K\quad\Rightarrow\quad K=-\dfrac{5^7}{6}'),
      S('Divide by the integrating factor.', r'y=\dfrac56(2t+5)-\dfrac{5^7}{6(2t+5)^5}')],
     r'The displayed solution holds on $t>-5/2$, the interval containing the starting time.', cites=W(1, 2))
D.P(r'**A brief integration-by-parts refresher:** if multiplying by $\mu$ leaves an integral such as $\int4te^{2t}\,dt$, use $\int u\,dv=uv-\int v\,du$. Choose $u=4t$, $dv=e^{2t}dt$; then $du=4dt$ and $v=e^{2t}/2$.')
D.EQ(r'\int4te^{2t}\,dt=2te^{2t}-e^{2t}+K')
D.PR('When the integral needs parts · original',
     r"Solve $y'+2y=4t$, $y(0)=1$. Use the integral just shown rather than learning a new ODE method.",
     [S('The factor is still e²ᵗ; only the right-hand integral changes.', r'\dfrac{d}{dt}(e^{2t}y)=4te^{2t}'),
      S('Use the integration-by-parts result.', r'e^{2t}y=2te^{2t}-e^{2t}+K'),
      S('Divide and apply the initial condition.', r'y=2t-1+Ke^{-2t},\quad K=2')],
     r'$y=2t-1+2e^{-2t}$.')
D.PR('One equation, two methods · Pre-tutorial 3(c)',
     r"For $y'=8ty+3y$, find the general solution using separation. Then identify the integrating factor and explain how it gives the same family, including the zero solution.",
     [S('Factor y, divide by it for nonzero solutions, and integrate.', r'\ln|y|=4t^2+3t+K'),
      S('Exponentiate; restore the divided-out solution by allowing A = 0.', r'y=Ae^{4t^2+3t}'),
      S('In linear form, a(t) = −(8t + 3).', r'\mu=e^{-(4t^2+3t)}'),
      S('The product derivative is zero, so its value is an arbitrary constant.', r'\dfrac{d}{dt}(\mu y)=0\quad\Rightarrow\quad\mu y=A')],
     r'$y=Ae^{4t^2+3t}$ for any real $A$. The integrating-factor route never divides by $y$, so $A=0$ is included directly.', cites=T)
D.H('Circuit connection: the lecture’s RL equation', level=2, cites=W(2, 3))
D.P(r'The lecture uses $2i\prime+10i=100$, $i(0)=0$. The drawing below follows that KVL equation, with the source positive at the top; the printed circuit figure has its source polarity reversed.')
D.SCH(r'''
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$10\,\Omega$"
L1 6,3 -> 6,0 "$2\,\mathrm{H}$" i="$i$" v="$v_L$"
wire 6,0 -> 0,0
ground 0,0
#~ flow
#~ init L1 0
#@ view "Just after closing"
#@ node a 100 "source: $100\,\mathrm{V}$"
#@ node b 100 "after switch: $100\,\mathrm{V}$"
#@ node c 100 "inductor: $100\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$100\,\mathrm{V}$" col=0 id=src
#@ el W a b "closed" col=1
#@ el R b c "$10\,\Omega$" col=2 id=res
#@ el L c g "$2\,\mathrm{H}$" col=3 plus=c v="$v_L$" id=ind
#@ step "Ground the bottom wire." show=g
#@ step "The source fixes the top at 100 V; the closed switch has no step." show=a,b,src
#@ step "Current starts at zero, so R has no fall; L takes all 100 V." show=c,res,ind
#@ view "At one time constant"
#@ node a 100 "source: $100\,\mathrm{V}$"
#@ node b 100 "after switch: $100\,\mathrm{V}$"
#@ node c 36.787944 "inductor: $36.79\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$100\,\mathrm{V}$" col=0 i="$6.32\,\mathrm{A}$" to=a
#@ el W a b "closed" col=1 i="$6.32\,\mathrm{A}$" to=b
#@ el R b c "$10\,\Omega$" col=2 i="$6.32\,\mathrm{A}$" to=c
#@ el L c g "$2\,\mathrm{H}$" col=3 plus=c v="$v_L$" i="$6.32\,\mathrm{A}$" to=g
#@ note "Ground the bottom wire. At t = 0.2 s, i = 10(1 - 1/e) A. The 100 V source equals the resistor fall plus the inductor voltage."
#@ view "DC final value"
#@ node a 100 "source: $100\,\mathrm{V}$"
#@ node b 100 "after switch: $100\,\mathrm{V}$"
#@ node c 0 "inductor: $0\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$100\,\mathrm{V}$" col=0 i="$10\,\mathrm{A}$" to=a
#@ el W a b "closed" col=1 i="$10\,\mathrm{A}$" to=b
#@ el R b c "$10\,\Omega$" col=2 i="$10\,\mathrm{A}$" to=c
#@ el L c g "$2\,\mathrm{H}$" col=3 plus=c v="$v_L$" i="$10\,\mathrm{A}$" to=g
#@ note "Ground the bottom wire. The inductor is a DC short; i = 100/10 = 10 A."
'''.strip(), 'RL circuit, redrawn to match the lecture equation', cites=W(2, 3))
D.P(r"Divide by $2$: $i'+5i=50$, so $\mu=e^{5t}$. Integrating $(e^{5t}i)'=50e^{5t}$ gives $i=10+Ke^{-5t}$; $i(0)=0$ sets $K=-10$, hence $i=10(1-e^{-5t})\,\mathrm{A}$.")
D.P(r'Separation gives the same result: $di/(50-5i)=dt$, then $-\frac15\ln|50-5i|=t+K$. Its final current $10\,\mathrm{A}$ and time constant $2/10=0.2\,\mathrm{s}$ match Week 2’s circuit reasoning.')

D.H('Topic 3: Existence and uniqueness', cites=W(5))
D.H('Calculus reminder: a partial derivative holds t fixed', level=2)
D.P(r'For a function of two variables, $F(t,y)$, the symbol $\partial F/\partial y$ means differentiate with respect to $y$ while treating $t$ as a constant. For example, if $F=t^2+3ty$, then $\partial F/\partial y=3t$.')
D.P(r"Write the ODE as $y'=F(t,y)$. If $F$ and $\partial F/\partial y$ are real-valued and continuous on an open region around the initial point, the IVP has exactly one solution on some interval near its starting time.")
D.L(['**Existence:** there is a solution through the starting point.',
     '**Uniqueness:** there is only one such solution locally.',
     '**If the conditions fail:** this theorem gives no conclusion; inspect the equation separately.',
     '**Local guarantee:** even smooth formulas do not guarantee that a solution survives for all time.'])
D.EX('Check the point, without solving the ODE · original',
     r"For $y'=(t+y)/(t-y)$, check whether the theorem guarantees a unique local solution through $(0,1)$ and through $(2,2)$.",
     [S('The denominator vanishes on the line t = y.', r'F=\dfrac{t+y}{t-y}'),
      S('Use the quotient rule in y, holding t fixed.', r'\dfrac{\partial F}{\partial y}=\dfrac{2t}{(t-y)^2}'),
      S('Both expressions are continuous near (0,1), which is off that line.'),
      S('At (2,2), the original right side is undefined; it cannot define a classical solution through that point.')],
     '(0,1): a unique local solution is guaranteed. (2,2): the theorem does not apply, and the ODE itself is undefined there.')
D.PR('Find a region containing the start · original',
     r"For $(t-3)y'+(\ln t)y=2t$ with $y(1)=2$, find the region containing the starting point where the theorem applies. Do not solve.",
     [S('First isolate the derivative.', r'F=\dfrac{2t-(\ln t)y}{t-3}'),
      S('Differentiate only with respect to y.', r'\dfrac{\partial F}{\partial y}=-\dfrac{\ln t}{t-3}'),
      S('The log requires t > 0, and division excludes t = 3. The start has t = 1.', r'0<t<3,\qquad\text{any real }y')],
     r'The strip $0<t<3$ contains the initial point and gives the local uniqueness guarantee.')
D.P(r"**A local solution can end:** $y'=y^2$, $y(0)=1$ has solution $y=1/(1-t)$ on $t<1$. It blows up at $t=1$ despite smooth $F$ and $F_y$.")
D.P(r"**A failed test can allow multiple solutions:** for $y'=y^{1/3}$ at $y=0$, $F$ is continuous but $F_y$ is not. Both $y=0$ and a function that stays zero for $t\le0$ then follows $(2t/3)^{3/2}$ for $t>0$ solve the IVP with $y(0)=0$.")
D.GRAPH(r'''
title "A failed uniqueness test can allow several curves"
x -1 4 label="$t$"
y -0.2 3 label="$y$"
family c 0 2 0.5 "if(t>c,(2*max(0,t-c)/3)^1.5,0)" color=2
hline "0" label="zero solution" color=1
caption "Each purple solution stays at zero until its own departure time. They all pass through (0,0); the y-partial derivative of F fails there."
''')


def verify():
    E = sp.exp
    zero(sp.diff(-1/y, y)-y**-2)
    zero(sp.diff(2*E(3*t), t)-6*E(3*t))
    first(3*E(t**2), 2*t*y, (0,3))
    first(sp.sqrt(6*t**2+3), t*(3+y**2)/(y*(1+t**2)), (1,3))
    first(sp.sqrt(5-t**2), -t/y, (1,2))
    first(2*t**2/(1-2*K*t**2), y**2/t**3)
    first(sp.S(0), y**2/t**3)
    implicit(3*t*(y**2+1), y*(t**2+2), (y**2+1)*(t**2+2)**3)
    yp = sp.symbols('yp', positive=True)
    U = yp**2+2*sp.log(yp)-t**-2
    zero(yp*sp.diff(U,yp)-t**3*(yp**2+1)*sp.diff(U,t))
    first(3-2*E(-2*t), 6-2*y, (0,1))
    first(t**2+t**-2, 4*t-2*y/t, (1,2))
    first(sp.Rational(5,6)*(2*t+5)-5**7/(6*(2*t+5)**5), 10-10*y/(2*t+5), (0,0))
    zero(sp.diff(2*t*E(2*t)-E(2*t),t)-4*t*E(2*t))
    first(2*t-1+2*E(-2*t), 4*t-2*y, (0,1))
    first(K*E(4*t**2+3*t), (8*t+3)*y)
    first(10*(1-E(-5*t)), 50-5*y, (0,0))
    zero(sp.diff((t+y)/(t-y),y)-2*t/(t-y)**2)
    zero(sp.diff((2*t-sp.log(t)*y)/(t-3),y)+sp.log(t)/(t-3))
    first(1/(1-t), y**2, (0,1))
    tp = sp.symbols('tp', positive=True)
    zero(sp.diff((2*tp/3)**sp.Rational(3,2),tp)-(2*tp/3)**sp.Rational(1,2))
    # Recognition tasks: factorability and linearity are checked separately.
    for F, expected in [(t**2+y,(False,True)), (E(t+y),(True,False)),
                        (2*y-6,(True,True)), (t+y**2,(False,False))]:
        actual = (sp.separatevars(F,symbols=[t,y],dict=True) is not None, sp.diff(F,y,2)==0)
        assert actual == expected, (F,actual)


if __name__ == '__main__':
    verify()
    finish(D, 'Week-3-Linear-and-Separable-First-Order-ODEs-Existence-and-Uniqueness.md')
