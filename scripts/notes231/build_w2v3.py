"""Week 2 learning sequence: small explanations with interleaved original practice.

Run without arguments to validate and export only this week's Markdown.
Add --publish to replace the existing Week 2 document, preserving revision history.
"""
import json
import sys
import urllib.request
from pathlib import Path

import sympy as sp

from lib231 import Doc, S

D = Doc(2, 'Week 2: Classifying ODEs, Initial Value Problems and RC/RL Circuits',
        ['ode_classification', 'initial_value_problems', 'first_order_circuits'])
W = lambda *pages: D.cite('W2', *pages)
SCHEMATICS = []


def drawing(source):
    source = source.strip()
    SCHEMATICS.append(source)
    return '```schematic\n' + source + '\n```'


# Calculus first; no unrelated integration techniques this week.
D.H('Calculus refresher: the derivatives used this week')
D.P(r'This week you mostly differentiate and substitute. You will be given the solution families you need; learning a general method for finding them comes in Week 3.')
D.T(['Reminder', 'What to remember'], [
    [r"$y'=\dfrac{dy}{dt}$; $y''=\dfrac{d^2y}{dt^2}$", 'First derivative = rate of change; second derivative = rate of change of that rate.'],
    [r'$\dfrac{d}{dt}(K)=0$', r'$K$ is a constant, even when you do not know its value.'],
    [r'$\dfrac{d}{dt}(Ae^{kt})=Ak e^{kt}$', r'Chain rule: multiply by the derivative of the exponent. $A$ and $k$ are constants.'],
    [r'$e^0=1$; $e^{-kt}\to0$ for $k>0$', r'Use the first at $t=0$, and the second when finding the long-term value.'],
])
D.P(r'For instance, if $y=3-2e^{-4t}$, the constant $3$ differentiates to zero. The exponential contributes a factor of $-4$, so the two negative signs cancel:')
D.EQ(r'\dfrac{dy}{dt}=(-2)(-4)e^{-4t}=8e^{-4t}')
D.PR('Quick calculus check · original',
     r'1. Differentiate $y=5+3e^{-2t}$.' '\n'
     r'2. For $v(t)=8-6e^{-100t}$, find $v(0)$ and the value approached as $t\to\infty$.',
     [S('Multiply by the derivative of the exponent.', r"y'=-6e^{-2t}"),
      S(r'At zero, use $e^0=1$. At large positive time, the exponential tends to zero.', r'v(0)=8-6=2,\qquad v(t)\to8')],
     r"1. $y'=-6e^{-2t}$. 2. $v(0)=2$ and $v\to8$.")

D.H('Week 2 overview')
D.P('There are three separate jobs this week: describe the kind of differential equation you have, understand what its solution means, and connect a simple circuit to that equation. Learn them in that order; the circuit section will reuse the same ideas about functions and starting values.')

D.H('Topic 1: Classifying a differential equation', cites=W(2, 3))
D.P(r'A differential equation relates an unknown function to its derivatives. In $\dfrac{dy}{dt}+2y=6$, we want a function $y(t)$ whose rate of change plus twice its value always equals $6$.')
D.P(r'An **ordinary differential equation (ODE)** uses derivatives with respect to one independent variable. Here $t$ is the independent variable, and $y$ is the dependent variable: its value depends on $t$.')
D.H('Five labels, five different questions', level=2)
D.P(r"Read $y'$ as $\dfrac{dy}{dt}$ below. For the linear-equation labels, first move all terms containing $y$ or its derivatives to the left.")
D.T(['Label', 'Question to ask', 'Useful distinction'], [
    ['Order', 'What is the highest derivative present?', r"$y''$ means second order; $(y')^3$ is still first order."],
    ['Linear', r'Are $y$ and its derivatives only to the first power, without multiplying each other or appearing inside functions?', r"$t^2y'+y$ is linear. $yy'$, $y^2$, and $\sin y$ are nonlinear."],
    ['Homogeneous (linear)', 'After collecting the unknown-function terms on the left, is the right side identically zero?', r"$y'-3y=0$ is homogeneous; $y'-3y=2$ is nonhomogeneous."],
    ['Constant coefficients (linear)', r'Are the multipliers of $y$ and its derivatives constants?', r"$y'+2y=\sin t$ has constant coefficients: the forcing on the right does not count as a coefficient."],
    ['Autonomous', r'Does the equation avoid explicit dependence on $t$?', r"$y'=3y+2$ is autonomous; $y'=ty$ is not. Writing $y(t)$ does not itself count as explicit $t$."],
])
D.P(r"For a linear equation, a **coefficient** multiplies $y$ or one of its derivatives. The leftover right side is called the **forcing**, often written $f(t)$; it can be zero, constant, or time-varying.")
D.P('Use “homogeneous” here in the linear-ODE sense. For a nonlinear equation, mark homogeneous and constant coefficients as “not applicable” in these exercises.')
D.EX('Classify one equation · lecture Example 2.1',
     r"Classify $t^3y''+e^ty'+y=0$ using all five labels.",
     [S(r"The highest derivative is $y''$: second order."),
      S(r"Each occurrence of $y$, $y'$, and $y''$ is linear. The multipliers $t^3$ and $e^t$ depend only on $t$, which is allowed."),
      S('The right side is zero, so it is homogeneous.'),
      S(r'The coefficients change with $t$, so they are variable coefficients.'),
      S(r'The explicit $t^3$ and $e^t$ make it non-autonomous.')],
     'Second order; linear; homogeneous; variable coefficients; not autonomous.', cites=W(3))
D.PR('Order and linearity · original',
     'For now, identify **only order and linearity**. Do not solve.\n\n'
     r"1. $y''+4y=0$" '\n'
     r"2. $(y')^3+y=0$" '\n'
     r"3. $y'+y^2=t$",
     [S(r"1. The second derivative is highest, and the unknown appears linearly: second order, linear."),
      S(r"2. Cubing $y'$ does not turn it into a third derivative: first order, nonlinear."),
      S(r'3. Only a first derivative appears, but $y^2$ breaks linearity: first order, nonlinear.')],
     '1. Second order, linear. 2. First order, nonlinear. 3. First order, nonlinear.')
D.PR('Separate the three remaining labels · original',
     'All three equations below are first order and linear. Identify **homogeneous/nonhomogeneous**, **constant/variable coefficients**, and **autonomous/not autonomous**.\n\n'
     r"1. $y'=3y$" '\n'
     r"2. $y'=3y+2$" '\n'
     r"3. $y'+2y=\sin t$",
     [S(r'Move the unknown-function terms left in 1 and 2.', r"y'-3y=0,\qquad y'-3y=2"),
      S(r'1. Zero forcing; coefficients $1,-3$; no explicit time: homogeneous, constant coefficients, autonomous.'),
      S(r'2. Forcing $2$ is nonzero but does not depend on time: nonhomogeneous, constant coefficients, autonomous.'),
      S(r'3. The forcing $\sin t$ changes with time, but coefficients $1,2$ are constant: nonhomogeneous, constant coefficients, not autonomous.')],
     '1. Homogeneous, constant, autonomous. 2. Nonhomogeneous, constant, autonomous. 3. Nonhomogeneous, constant, not autonomous.')
D.PR('Put the labels together · original',
     'Classify fully; use “not applicable” where needed.\n\n'
     r"1. $y''+ty'+y=0$" '\n'
     r"2. $y'=\sin y$",
     [S(r"1. Highest derivative $y''$; unknown appears linearly; zero forcing; coefficient $t$ varies and introduces explicit time."),
      S(r'2. The unknown is inside sine, so it is nonlinear. There is no explicit time.')],
     '1. Second order, linear, homogeneous, variable coefficients, not autonomous. '
     '2. First order, nonlinear, autonomous; the other two labels do not apply.')
D.P(r'One consequence of linearity: if $y$ solves a linear equation with forcing $f(t)$, then $Ay$ solves the equation with forcing $Af(t)$, for constant $A$. For a homogeneous equation the forcing stays zero, so scaling a solution gives another solution of the same equation.', cites=W(2))

D.H('Topic 2: What a solution is, and what an initial condition does')
D.H('First: check a function you are given', level=2)
D.P(r"In algebra, solving $x+2=5$ gives a number. Solving $y'+2y=6$ gives a function: a rule assigning a value to $y$ at each time.")
D.P('A proposed function is a solution when it makes the differential equation true throughout the interval being considered. Matching at just one time is not enough.')
D.EX('Check a proposed solution · original',
     r"Does $y=3-2e^{-2t}$ solve $y'+2y=6$?",
     [S('Differentiate the proposed function using the chain rule.', r"y'=4e^{-2t}"),
      S(r"Replace both $y'$ and $y$ on the left with their expressions.", r"y'+2y=4e^{-2t}+2(3-2e^{-2t})"),
      S('Expand and cancel. The result equals the required right side for every time.', r'4e^{-2t}+6-4e^{-2t}=6')],
     r'Yes. Its rate of change and its value combine to give $6$ for every $t$.')
D.PR('Your turn: check, without solving · original',
     r"Which of these solve $y'+2y=6$?" '\n\n'
     r'1. $y=3+e^{-2t}$' '\n'
     r'2. $y=3+t$' '\n\n'
     'Differentiate each, substitute, and simplify. Candidate 2 matches the equation at one time; explain why that is insufficient.',
     [S(r'For 1, the derivative is $-2e^{-2t}$.', r'-2e^{-2t}+2(3+e^{-2t})=6'),
      S(r'For 2, the derivative is $1$.', r'1+2(3+t)=7+2t'),
      S(r'This equals $6$ only at $t=-1/2$. A solution must satisfy the equation on an interval.')],
     '1 is a solution; 2 is not.')
D.H('Then: a family of solutions', level=2)
D.P(r"The same equation can have many solutions. For $y'+2y=6$, they can be written together as:")
D.EQ(r'y=3+Ke^{-2t}')
D.P(r'The free constant $K$ labels the different functions. Choosing $K=-2$ gives the worked example; choosing $K=1$ gives the first practice candidate; choosing $K=0$ gives the constant solution $y=3$.')
D.P(r"This is the **general solution** on the real time line. You can check the whole family at once: $y'=-2Ke^{-2t}$, which cancels the exponential term in $2y$, leaving $6$.")
D.H('Finally: choose the member that starts in the right place', level=2)
D.P(r'An **initial condition** specifies one starting value. The statement $y(0)=1$ means “when $t=0$, the function must equal $1$”; it says nothing about the derivative being $1$.')
D.P('An **initial value problem (IVP)** gives the differential equation and the initial condition together. The differential equation describes the allowed behaviour, and the starting value selects the appropriate solution here.')
D.EX('Use a starting value · original',
     r"Solve the IVP $y'+2y=6$, $y(0)=1$, using the given family $y=3+Ke^{-2t}$.",
     [S(r'Put $t=0$ into the family; the exponential becomes $1$.', r'y(0)=3+K'),
      S('Set this equal to the required starting value and solve for the constant.', r'3+K=1\quad\Rightarrow\quad K=-2'),
      S('Put that constant back into the family.', r'y(t)=3-2e^{-2t}')],
     r'$y(t)=3-2e^{-2t}$. At $t=0$, this gives $1$, as required.')
D.GRAPH(r'''
title "A starting point chooses one member of the family"
x 0 3 label="$t$"
y -1 7 label="$y$"
family K -4 4 1 "3+K*exp(-2*t)" color=0
hline "3" label="$y=3$"
drag P 0 1 label="starting point" snap=0.25
solution "-2*y+6" x0="P_x" y0="P_y" label="selected solution"
readout "$K=$" "(P_y-3)*exp(2*P_x)"
caption "Start at (0,1): K=-2. Move the point vertically to select a different curve; move it along that curve and K stays the same."
''')
D.PR('The starting time is not always zero · original',
     r'Use $y=3+Ke^{-2t}$ with $y(1)=5$. Find $K$ and write the selected solution. Start by substituting $t=1$ and $y=5$.',
     [S(r'At $t=1$, the exponential is $e^{-2}$, not $1$.', r'5=3+Ke^{-2}'),
      S(r'Subtract $3$, then divide by $e^{-2}$.', r'K=2e^2'),
      S('Substitute and combine exponentials if desired.', r'y=3+2e^2e^{-2t}=3+2e^{-2(t-1)}')],
     r'$K=2e^2$, $y=3+2e^{-2(t-1)}$. At $t=1$ this gives $5$.')
D.PR('A solution of the equation can fail the IVP · original',
     r"For $y'+2y=6$ with $y(0)=1$, a student proposes $y=3+e^{-2t}$." '\n\n'
     'It already passed the differential-equation check. Does it solve this IVP? What must you check separately?',
     [S('Check the initial condition separately.', r'y(0)=3+1=4\ne1')],
     'No. It solves the differential equation but has the wrong starting value.')
D.P(r"A second-order IVP typically specifies both a value $y(t_0)$ and a slope $y'(t_0)$. We will work with those in Week 5; this week, keep the distinction between the equation and the starting value clear.")

D.H('Topic 3: First-order RC and RL circuits', cites=W(1, 2, 3, 4, 5))
D.P('A capacitor stores energy through its voltage; an inductor stores energy through its current. Their component laws contain a first derivative, which is where the differential equation enters.')
D.T(['Component', 'Law with current entering the + terminal', 'At DC steady state'], [
    ['Capacitor', r'$i_C=C\dfrac{dv_C}{dt}$', r'Constant voltage means $i_C=0$: an open circuit.'],
    ['Inductor', r'$v_L=L\dfrac{di_L}{dt}$', r'Constant current means $v_L=0$: a short circuit.'],
])
D.P(r'$C$ is capacitance in farads (F), and $L$ is inductance in henries (H). **Steady state** means the values have stopped changing; a zero derivative means constant, not necessarily zero.')
D.H('Start with a capacitor discharging through one resistor', level=2)
D.P(r'The diagram shows the circuit **after** switching, with a capacitor already holding $8\,\mathrm{V}$. There is no source attached; the stored energy is released through the resistor. This is a **natural response**.')
natural = drawing(r'''
C1 0,3 -> 0,0 "$5\,\mu\mathrm{F}$" v="$v$" i="$i_C$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$2\,\mathrm{k\Omega}$" i="$i_R$"
wire 3,0 -> 0,0
ground 0,0
#~ flow
#~ init C1 8
#@ view "Just after switching"
#@ node a 8 "top: $8\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el C a g "$5\,\mu\mathrm{F}$" col=0 plus=a v="$v$" i="$4\,\mathrm{mA}$" to=a
#@ el R a g "$2\,\mathrm{k\Omega}$" col=1 i="$4\,\mathrm{mA}$" to=g
#@ note "Ground the bottom wire. The capacitor holds 8 V; resistor current is 8/2000 = 4 mA downward. Capacitor current is upward."
#@ view "One time constant"
#@ node a 2.9430355 "top: $2.94\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el C a g "$5\,\mu\mathrm{F}$" col=0 plus=a v="$v$" i="$1.47\,\mathrm{mA}$" to=a
#@ el R a g "$2\,\mathrm{k\Omega}$" col=1 i="$1.47\,\mathrm{mA}$" to=g
#@ note "Ground the bottom wire. At 10 ms the voltage is 8/e V, and both current magnitudes are v/R."
#@ view "Long after switching"
#@ node a 0 "top: $0\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el C a g "$5\,\mu\mathrm{F}$" col=0 plus=a v="$v$"
#@ el R a g "$2\,\mathrm{k\Omega}$" col=1
#@ note "Ground the bottom wire. With no source, the voltage and both currents tend to zero."
''')
D.P(natural)
D.P(r'Both current arrows point down, so Kirchhoff’s current law (KCL) at the top node gives $i_C+i_R=0$. A negative value for one reference current simply means its actual direction is upward.')
D.STEPS('From the circuit to its equation', [
    (r'i_C+i_R=0', 'No source injects current into the top node.'),
    (r'C\dfrac{dv}{dt}+\dfrac{v}{R}=0', 'Replace capacitor current with its law and resistor current with Ohm’s law.'),
    (r'\dfrac{dv}{dt}+\dfrac{v}{RC}=0', 'Divide both terms by C.'),
    (r'v(t)=Ke^{-t/(RC)}', 'This solution family has the required exponential decay; check it by differentiating and substituting.'),
    (r'v(0)=K=V_0', 'The initial voltage V₀ fixes K, exactly as in Topic 2.'),
    (r'v(t)=V_0e^{-t/\tau},\quad\tau=RC', 'The time constant τ is the decay time scale, measured in seconds.'),
])
D.EX('Use the equation for the circuit above · original values',
     r'Find $v(t)$ for the $2\,\mathrm{k\Omega}$, $5\,\mu\mathrm{F}$ circuit with $v(0)=8\,\mathrm{V}$.',
     [S('Convert to ohms and farads before multiplying.', r'\tau=2000(5\times10^{-6})=0.010\,\mathrm{s}'),
      S(r'Use $V_0=8$ and $1/\tau=100$.', r'v(t)=8e^{-100t}\,\mathrm{V},\qquad t\ge0'),
      S('Check the starting and final values.', r'v(0)=8\,\mathrm{V},\qquad v(t)\to0')],
     r'$v(t)=8e^{-100t}\,\mathrm{V}$, with $t$ in seconds. At $t=\tau=10\,\mathrm{ms}$, $v=8/e\approx2.94\,\mathrm{V}$: about 37% remains.')
D.PR('Read the circuit equation · original',
     'For that same discharge, answer without solving again:\n\n'
     r"1. Classify $v'+100v=0$ using all five labels." '\n'
     r"2. Is $i_C=Cv'$ positive or negative during discharge? Explain using the downward reference arrow.",
     [S('1. It is first order, linear, homogeneous, constant-coefficient, and autonomous.'),
      S(r'2. Voltage decreases, so its derivative is negative.', r'i_C=(5\times10^{-6})(-800e^{-100t})=-4e^{-100t}\,\mathrm{mA}')],
     '1. First order, linear, homogeneous, constant coefficients, autonomous. 2. Negative: actual capacitor current flows upward.')
D.H('Add a source: the final voltage can be nonzero', level=2)
D.P(r'Now a constant source remains connected after switching. The capacitor moves from its initial voltage $V_0$ toward a final voltage $V_f$, rather than necessarily toward zero.')
step = drawing(r'''
I1 0,0 -> 0,3 "$3\,\mathrm{mA}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$2\,\mathrm{k\Omega}$" i="$i_R$"
S1 3,3 -> 6,3 "$t=0$" action=close
C1 6,3 -> 6,0 "$1\,\mu\mathrm{F}$" v="$v$" i="$i_C$"
wire 6,0 -> 0,0
ground 0,0
#~ flow
#~ init C1 2
#@ view "Before switching"
#@ node a 6 "source top: $6\,\mathrm{V}$"
#@ node b 2 "capacitor: $2\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el I g a "$3\,\mathrm{mA}$" col=0 i="$3\,\mathrm{mA}$" to=a rail
#@ el R a g "$2\,\mathrm{k\Omega}$" col=1 i="$3\,\mathrm{mA}$" to=g
#@ el S a b "open" col=2
#@ el C b g "$1\,\mu\mathrm{F}$" col=3 plus=b v="$v$"
#@ note "Ground the bottom wire. The source drives only the resistor: 3 mA times 2 kΩ = 6 V. The isolated capacitor holds the given 2 V."
#@ view "Just after switching"
#@ node a 2 "top: $2\,\mathrm{V}$"
#@ node b 2 "capacitor: $2\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el I g a "$3\,\mathrm{mA}$" col=0 i="$3\,\mathrm{mA}$" to=a rail
#@ el R a g "$2\,\mathrm{k\Omega}$" col=1 i="$1\,\mathrm{mA}$" to=g
#@ el W a b "closed" col=2
#@ el C b g "$1\,\mu\mathrm{F}$" col=3 plus=b v="$v$" i="$2\,\mathrm{mA}$" to=g
#@ note "Ground the bottom wire. Capacitor voltage stays 2 V. The resistor takes 1 mA, leaving 2 mA into C."
#@ view "One time constant"
#@ node a 4.528482 "top: $4.53\,\mathrm{V}$"
#@ node b 4.528482 "capacitor: $4.53\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el I g a "$3\,\mathrm{mA}$" col=0 i="$3\,\mathrm{mA}$" to=a rail
#@ el R a g "$2\,\mathrm{k\Omega}$" col=1 i="$2.26\,\mathrm{mA}$" to=g
#@ el W a b "closed" col=2
#@ el C b g "$1\,\mu\mathrm{F}$" col=3 plus=b v="$v$" i="$0.736\,\mathrm{mA}$" to=g
#@ note "Ground the bottom wire. At 2 ms, v = 6 - 4/e V. KCL: resistor and capacitor currents add to 3 mA."
#@ view "Long after switching"
#@ node a 6 "top: $6\,\mathrm{V}$"
#@ node b 6 "capacitor: $6\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el I g a "$3\,\mathrm{mA}$" col=0 i="$3\,\mathrm{mA}$" to=a rail
#@ el R a g "$2\,\mathrm{k\Omega}$" col=1 i="$3\,\mathrm{mA}$" to=g
#@ el W a b "closed" col=2
#@ el C b g "$1\,\mu\mathrm{F}$" col=3 plus=b v="$v$"
#@ note "Ground the bottom wire. Capacitor current tends to zero, so all 3 mA flows in R and sets v = 6 V."
''')
D.P(step)
D.P(r'The capacitor initially holds $2\,\mathrm{V}$. In these ordinary switching circuits, capacitor voltage cannot jump, so it still holds $2\,\mathrm{V}$ just after the switch closes.')
D.P(r'Write $0^-$ for just before switching and $0^+$ for just after. Thus $v_C(0^+)=v_C(0^-)=V_0$; for an inductor the corresponding continuous quantity is its current, $i_L(0^+)=i_L(0^-)$.')
D.L([r'**Initial value:** use the stored voltage before switching, or find it from the pre-switch steady-state circuit.',
     r'**Final value:** analyse the post-switch DC steady state: capacitor open, so all source current $I_s$ flows through $R$ and $V_f=RI_s$.',
     r'**Time constant:** for this one-resistor RC circuit, $\tau=RC$.'])
D.P(r'KCL now says “source current = capacitor current + resistor current”:')
D.EQ(r'C\dfrac{dv}{dt}+\dfrac{v}{R}=I_s')
D.P(r'The solution has the same decaying exponential as before, with the final voltage added:')
D.EQ(r'v(t)=V_f+(V_0-V_f)e^{-t/\tau}')
D.P(r"The quantity $v-V_f$ is the remaining difference from the final voltage. Call it $u=v-V_f$; because $V_f$ is constant, $u'=v'$. Substituting $v=V_f+u$ into KCL cancels $V_f/R=I_s$, leaving $Cu'+u/R=0$: the natural-response equation again.")
D.P(r'At $t=0$, the formula gives $V_f+(V_0-V_f)=V_0$. As time passes, the exponential dies away and leaves $V_f$; at one time constant, 37% of the initial difference remains, so 63% of the change is complete.')
D.EX('Build the response from three quantities · original values',
     r'For the source-driven circuit above, $I_s=3\,\mathrm{mA}$, $R=2\,\mathrm{k\Omega}$, $C=1\,\mu\mathrm{F}$ and $V_0=2\,\mathrm{V}$. Find $v(t)$.',
     [S('The initial capacitor voltage is given.', r'V_0=2\,\mathrm{V}'),
      S('At steady state, the source current flows entirely through the resistor.', r'V_f=(2000)(0.003)=6\,\mathrm{V}'),
      S('Convert to SI units and multiply.', r'\tau=(2000)(10^{-6})=0.002\,\mathrm{s}'),
      S('Substitute all three quantities into the response.', r'v(t)=6+(2-6)e^{-t/0.002}=6-4e^{-500t}\,\mathrm{V}')],
     r'$v(t)=6-4e^{-500t}\,\mathrm{V}$, $t\ge0$, with $t$ in seconds. It starts at $2\,\mathrm{V}$ and approaches $6\,\mathrm{V}$.')
D.GRAPH(r'''
title "Initial value, final value, and speed are separate choices"
x 0 12 label="$t$ (ms)"
y -1 13 label="$v$ (V)"
slider V0 0 12 2 step=1 label="$V_0$ (V)"
slider Vf 0 12 6 step=1 label="$V_f$ (V)"
slider tau 0.5 3 2 step=0.5 label="$\tau$ (ms)"
curve "Vf+(V0-Vf)*exp(-t/tau)" label="$v(t)$"
hline "Vf" label="final voltage"
vline "tau" label="one time constant"
caption "Move one slider at a time. V₀ sets the starting height, V_f sets the destination, and τ sets the speed. Set V_f=0 to recover discharge."
''')
tutorial = drawing(r'''
I1 0,0 -> 0,3 "$2\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$1\,\mathrm{k\Omega}$" i="$i_R$"
S1 3,3 -> 6,3 "$t=0$" action=close
C1 6,3 -> 6,0 "$C$" v="$v$" i="$i_C$"
wire 6,0 -> 0,0
ground 0,0
#@ spoiler
#@ view "Before switching"
#@ node a 2000 "source top: $2000\,\mathrm{V}$"
#@ node b 0 "capacitor: $0\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el I g a "$2\,\mathrm{A}$" col=0 i="$2\,\mathrm{A}$" to=a rail
#@ el R a g "$1\,\mathrm{k\Omega}$" col=1 i="$2\,\mathrm{A}$" to=g
#@ el S a b "open" col=2
#@ el C b g "$C$" col=3 plus=b v="$v$"
#@ note "Ground the bottom wire. All 2 A flows in R, so its top is 2000 V; the disconnected capacitor holds the given 0 V."
#@ view "Just after switching"
#@ node a 0 "top: $0\,\mathrm{V}$"
#@ node b 0 "capacitor: $0\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el I g a "$2\,\mathrm{A}$" col=0 i="$2\,\mathrm{A}$" to=a rail
#@ el R a g "$1\,\mathrm{k\Omega}$" col=1
#@ el W a b "closed" col=2 i="$2\,\mathrm{A}$" to=b
#@ el C b g "$C$" col=3 plus=b v="$v$" i="$2\,\mathrm{A}$" to=g
#@ note "Ground the bottom wire. Capacitor voltage stays zero. R carries zero current, so all 2 A enters C."
''')
D.PR('Can current jump? · Pre-tutorial 2',
     r'The capacitor is initially uncharged: $V_0=0$. The capacitance is unspecified and is not needed.' '\n\n' + tutorial + '\n\n'
     r'Find capacitor current $i_C(0^-)$ and $i_C(0^+)$, using the downward reference into the capacitor. Is current discontinuous even though voltage is continuous?',
     [S('Before switching the capacitor branch is disconnected, so its current is zero.', r'i_C(0^-)=0'),
      S('Immediately after switching, its voltage is still zero.', r'v(0^+)=0'),
      S('The resistor therefore carries no current at that instant.', r'i_R(0^+)=\dfrac{0}{1000}=0'),
      S('KCL sends all the source current into the capacitor.', r'i_C(0^+)=I_s-i_R(0^+)=2\,\mathrm{A}')],
     r'$i_C(0^-)=0$, $i_C(0^+)=2\,\mathrm{A}$. Yes, capacitor current jumps; capacitor voltage stays at $0\,\mathrm{V}$ through the switch.',
     cites=D.cite('T2', 1))
D.H('The RL version: track current instead of voltage', level=2)
D.P(r'For a series resistor–inductor circuit, Kirchhoff’s voltage law (KVL) gives $V_s=Ri+L\dfrac{di}{dt}$, where $V_s$ is a constant source voltage. The starting current carries over through switching; at DC steady state the inductor is a short, so $I_f=V_s/R$.')
D.EQ(r'i(t)=I_f+(I_0-I_f)e^{-t/\tau},\qquad\tau=\dfrac{L}{R}')
D.P(r'$I_0$ is the initial inductor current and $I_f$ is its final current. The response has the same shape as the RC result; the changing quantity and time constant differ.')
rl = drawing(r'''
V1 0,3 -> 0,0 "$24\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$6\,\Omega$" i="$i$"
L1 6,3 -> 6,0 "$0.3\,\mathrm{H}$" v="$v_L$"
wire 6,0 -> 0,0
ground 0,0
#~ flow
#~ init L1 0
#@ spoiler
#@ view "Before switching"
#@ node a 24 "source: $24\,\mathrm{V}$"
#@ node b 0 "after switch: $0\,\mathrm{V}$"
#@ node c 0 "inductor: $0\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$24\,\mathrm{V}$" col=0
#@ el S a b "open" col=1
#@ el R b c "$6\,\Omega$" col=2
#@ el L c g "$0.3\,\mathrm{H}$" col=3 plus=c v="$v_L$"
#@ note "Ground the bottom wire. The source steps 24 V, all taken by the open switch. No current flows."
#@ view "Just after switching"
#@ node a 24 "source: $24\,\mathrm{V}$"
#@ node b 24 "after switch: $24\,\mathrm{V}$"
#@ node c 24 "inductor: $24\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$24\,\mathrm{V}$" col=0
#@ el W a b "closed" col=1
#@ el R b c "$6\,\Omega$" col=2
#@ el L c g "$0.3\,\mathrm{H}$" col=3 plus=c v="$v_L$"
#@ note "Ground the bottom wire. Current is still zero, so the resistor has no fall; the inductor takes all 24 V."
#@ view "One time constant"
#@ node a 24 "source: $24\,\mathrm{V}$"
#@ node b 24 "after switch: $24\,\mathrm{V}$"
#@ node c 8.829107 "inductor: $8.83\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$24\,\mathrm{V}$" col=0 i="$2.53\,\mathrm{A}$" to=a
#@ el W a b "closed" col=1 i="$2.53\,\mathrm{A}$" to=b
#@ el R b c "$6\,\Omega$" col=2 i="$2.53\,\mathrm{A}$" to=c
#@ el L c g "$0.3\,\mathrm{H}$" col=3 plus=c v="$v_L$" i="$2.53\,\mathrm{A}$" to=g
#@ note "Ground the bottom wire. At 50 ms, i = 4(1 - 1/e) A; the resistor falls 15.17 V and the inductor takes 8.83 V."
#@ view "Long after switching"
#@ node a 24 "source: $24\,\mathrm{V}$"
#@ node b 24 "after switch: $24\,\mathrm{V}$"
#@ node c 0 "inductor: $0\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ el V a g "$24\,\mathrm{V}$" col=0 i="$4\,\mathrm{A}$" to=a
#@ el W a b "closed" col=1 i="$4\,\mathrm{A}$" to=b
#@ el R b c "$6\,\Omega$" col=2 i="$4\,\mathrm{A}$" to=c
#@ el L c g "$0.3\,\mathrm{H}$" col=3 plus=c v="$v_L$" i="$4\,\mathrm{A}$" to=g
#@ note "Ground the bottom wire. At steady state the inductor has no step, so i = 24/6 = 4 A."
''')
D.PR('Build an RL response with less help · original',
     r'The inductor initially carries no current. The switch closes at $t=0$.' '\n\n' + rl + '\n\n'
     r'1. Find $I_0$, $I_f$, and $\tau$.' '\n'
     r'2. Write $i(t)$.' '\n'
     r'3. Use $v_L=L\dfrac{di}{dt}$ to find $v_L(0^+)$. Does inductor voltage have to stay continuous?',
     [S('The current cannot jump, so its starting value remains zero.', r'I_0=0'),
      S('At DC steady state the inductor is a short.', r'I_f=\dfrac{24}{6}=4\,\mathrm{A}'),
      S('Use the RL time constant.', r'\tau=\dfrac{0.3}{6}=0.050\,\mathrm{s}'),
      S('Put the three quantities into the current response.', r'i(t)=4-4e^{-20t}\,\mathrm{A}'),
      S('Differentiate and multiply by inductance.', r'v_L(t)=0.3(80e^{-20t})=24e^{-20t}\,\mathrm{V}')],
     r'$I_0=0$, $I_f=4\,\mathrm{A}$, $\tau=50\,\mathrm{ms}$. '
     r'$i(t)=4-4e^{-20t}\,\mathrm{A}$ and $v_L(0^+)=24\,\mathrm{V}$. Inductor voltage can jump; its current is continuous.')
D.P(r'These exponential response formulas apply to the simple first-order circuits here, with constant sources after the switch. In a more complicated RC/RL circuit, use the resistance seen by the storage element after switching for $R$; do not automatically choose one labelled resistor.')


def verify():
    """Check the actual equations, candidate solutions, initial values and units."""
    t = sp.symbols('t', real=True)
    k = sp.symbols('K', real=True)
    exp = sp.exp
    assert sp.diff(3 - 2 * exp(-4*t), t) == 8 * exp(-4*t)
    assert sp.diff(5 + 3 * exp(-2*t), t) == -6 * exp(-2*t)
    assert (8 - 6 * exp(-100*t)).subs(t, 0) == 2
    assert sp.limit(8 - 6 * exp(-100*t), t, sp.oo) == 8
    family = 3 + k * exp(-2*t)
    assert sp.simplify(sp.diff(family, t) + 2*family - 6) == 0
    assert sp.solve(family.subs(t, 0) - 1, k) == [-2]
    assert sp.solve(family.subs(t, 1) - 5, k) == [2*exp(2)]
    assert sp.expand(sp.diff(3+t, t) + 2*(3+t)) == 7+2*t
    v_natural = 8 * exp(-100*t)
    c_natural = sp.Rational(5, 10**6)
    assert 2000 * c_natural == sp.Rational(1, 100)
    assert sp.simplify(c_natural*sp.diff(v_natural, t) + v_natural/2000) == 0
    assert v_natural.subs(t, 0) == 8
    assert sp.limit(v_natural, t, sp.oo) == 0
    assert c_natural*sp.diff(v_natural, t) == -sp.Rational(4, 1000)*exp(-100*t)
    v_step = 6 - 4*exp(-500*t)
    c_step = sp.Rational(1, 10**6)
    assert 2000*c_step == sp.Rational(2, 1000)
    assert sp.simplify(c_step*sp.diff(v_step, t) + v_step/2000 - sp.Rational(3, 1000)) == 0
    assert v_step.subs(t, 0) == 2
    assert sp.limit(v_step, t, sp.oo) == 6
    assert (c_step*sp.diff(v_step, t)).subs(t, 0) == sp.Rational(2, 1000)
    i_rl = 4 - 4*exp(-20*t)
    assert sp.Rational(3, 10)/6 == sp.Rational(1, 20)
    assert sp.simplify(sp.Rational(3, 10)*sp.diff(i_rl, t) + 6*i_rl - 24) == 0
    assert i_rl.subs(t, 0) == 0
    assert sp.limit(i_rl, t, sp.oo) == 4
    assert sp.Rational(3, 10)*sp.diff(i_rl, t) == 24*exp(-20*t)
    # Tutorial: cap voltage 0 => resistor current 0 => all 2 A enters C.
    assert 2 - sp.Rational(0, 1000) == 2
    # Independently classify the nine equations (one worked example and eight exercises).
    y = sp.Function('y')(t)
    def classification(expr):
        order = sp.ode_order(expr, y)
        ds = sp.symbols(f'd0:{order+1}')
        reduced = expr
        for n in range(order, 0, -1):
            reduced = reduced.subs(sp.diff(y, t, n), ds[n])
        reduced = sp.expand(reduced.subs(y, ds[0]))
        linear = all(sp.diff(reduced, a, b) == 0 for a in ds for b in ds)
        homogeneous = sp.simplify(reduced.subs(dict.fromkeys(ds, 0))) == 0 if linear else None
        constant = all(not sp.diff(reduced, d).has(t) for d in ds) if linear else None
        return order, linear, homogeneous, constant, not reduced.has(t)
    cases = [
        (t**3*sp.diff(y,t,2)+exp(t)*sp.diff(y,t)+y, (2,True,True,False,False)),
        (sp.diff(y,t,2)+4*y, (2,True,True,True,True)),
        (sp.diff(y,t)**3+y, (1,False,None,None,True)),
        (sp.diff(y,t)+y**2-t, (1,False,None,None,False)),
        (sp.diff(y,t)-3*y, (1,True,True,True,True)),
        (sp.diff(y,t)-3*y-2, (1,True,False,True,True)),
        (sp.diff(y,t)+2*y-sp.sin(t), (1,True,False,True,False)),
        (sp.diff(y,t,2)+t*sp.diff(y,t)+y, (2,True,True,False,False)),
        (sp.diff(y,t)-sp.sin(y), (1,False,None,None,True)),
        (sp.diff(y,t)+100*y, (1,True,True,True,True)),
    ]
    for expr, expected in cases:
        assert classification(expr) == expected, (expr, classification(expr), expected)
    for source in SCHEMATICS:
        req = urllib.request.Request('http://127.0.0.1:8000/api/v1/schematics/check',
                                     json.dumps({'source': source}).encode(),
                                     {'Content-Type': 'application/json'})
        result = json.load(urllib.request.urlopen(req))
        assert not result['errors'], result['errors']
        print('Schematic:', [(e['name'], e['from'], e['to']) for e in result['elements']])
    print('Verified classifications, calculus, ODE residuals, initial/final values, and schematics.')


if __name__ == '__main__':
    verify()
    D.save()
    # Export only this document; preserve other notes and in-progress user edits.
    sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src'))
    # export_notes.py invokes main() on import: load just its reusable rendering functions.
    export_source = (Path(__file__).resolve().parents[1] / 'export_notes.py').read_text(encoding='utf-8')
    namespace = {}
    exec(export_source.rsplit('\nmain()', 1)[0], namespace)
    body = '# ' + D.title + '\n\n' + '\n\n'.join(filter(None, (namespace['block'](b) for b in D.B))) + '\n'
    target = Path(__file__).resolve().parents[2] / 'notes/Week-2-Classifying-ODEs-Initial-Value-Problems-and-RCRL-Circuits.md'
    target.write_text(body, encoding='utf-8', newline='\n')
    print('Exported', target, 'words:', len(body.split()))
