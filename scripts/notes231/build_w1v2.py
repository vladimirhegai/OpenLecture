"""ELEC 231 Week 1 v2: complex numbers and the RL natural response (short, example-led, interactive)."""
import math

import sympy as sp

from lib231 import Doc, S, steps_fence

D = Doc(week=1, title='Week 1: Complex Numbers and Your First Differential Equation',
        topic_keys=['complex_numbers', 'euler_identity', 'rl_natural_response'])
W = lambda *p: D.cite('W1', *p)  # noqa: E731
T1 = D.cite('T1', 1)

# ---------------------------------------------------------------- checks
j = sp.I
z = -3 + 4 * j
assert sp.Abs(z) == 5 and abs(math.degrees(math.atan2(4, -3)) - 126.87) < 0.01
assert abs(10 * math.cos(math.radians(-150)) + 8.660) < 1e-3 and abs(10 * math.sin(math.radians(-150)) + 5) < 1e-9
assert sp.simplify((80 + 18 * j) / (8 + 10 * j) - (5 - 4 * j)) == 0
assert sp.expand((1 + j) ** 8) == 16
for ang in (15, 105, 195, 285):
    r = 3 * sp.exp(j * sp.rad(ang))
    assert sp.simplify(sp.expand(r ** 4) - 81 * sp.exp(j * sp.pi / 3)) == 0
s_ = sp.symbols('s')
assert set(sp.solve(s_ ** 2 + 2 * s_ + 5, s_)) == {-1 + 2 * j, -1 - 2 * j}
assert [sp.nsimplify(sp.expand(x ** 3)) for x in (1 + sp.sqrt(3) * j, -2, 1 - sp.sqrt(3) * j)] == [-8, -8, -8]
assert j ** 27 == -j
assert sp.exp(j * sp.pi) == -1 and sp.exp(j * sp.pi / 2) == j and sp.exp(-j * sp.pi / 2) == -j
t, L, R, Is = sp.symbols('t L R I_s', positive=True)
i = Is * sp.exp(-R * t / L)
assert sp.simplify(L * sp.diff(i, t) + R * i) == 0
tau1 = sp.Rational(8, 1000) / 4
assert tau1 == sp.Rational(2, 1000) and abs(4 * math.exp(-1) - 1.47) < 0.01
assert abs(0.005 * math.log(10) - 0.0115) < 1e-4
tau5 = 0.003 / math.log(2)
assert abs(20 * tau5 - 0.0866) < 1e-4

# ================================================================ Topic 1
D.H('Topic 1: Complex numbers: one point, two ways to write it', cites=W(1, 3))
D.P(r"$j=\sqrt{-1}$, so $j^2=-1$. (Engineers write $j$ because $i$ means current.)"
    "\n\n"
    r"A complex number $z$ is a **point on a plane**. You can describe that point two ways."
    "\n\n"
    r"**Rectangular form** $z=a+jb$: how far across, how far up."
    "\n"
    r"- $a=\mathrm{Re}\{z\}$: the **real part** (across)"
    "\n"
    r"- $b=\mathrm{Im}\{z\}$: the **imaginary part** (up)"
    "\n\n"
    r"**Polar form** $z=c\angle\theta$: how long, which direction."
    "\n"
    r"- $c=|z|$: the **magnitude** (length of the arrow, never negative)"
    "\n"
    r"- $\theta=\angle z$: the **angle** (counter-clockwise from the positive real axis)",
    cites=W(1))
D.EQ(r'z=a+jb=c\,e^{j\theta}=c\angle\theta', cites=W(1))
D.T(['Convert', 'How'], [
    [r'$a+jb\ \to\ c\angle\theta$', r'$c=\sqrt{a^2+b^2}$, $\ \theta=\arctan\dfrac{b}{a}$, **then add $180^\circ$ if $a<0$**'],
    [r'$c\angle\theta\ \to\ a+jb$', r'$a=c\cos\theta$, $\ b=c\sin\theta$'],
], cites=W(2, 3))
D.GRAPH(r'''
title "Drag $z$: both forms update"
x -5 5 label="Re"
y -4 4 label="Im"
equal
drag Z 3 4 label="$z$" snap=0.5
arrow "Z_x" "Z_y" color=1
segment "Z_x" "0" "Z_x" "Z_y" dash color=0
segment "0" "Z_y" "Z_x" "Z_y" dash color=0
circle "0" "0" "1" dash color=0
readout "$a=$" "Z_x"
readout "$b=$" "Z_y"
readout "$c=$" "hypot(Z_x,Z_y)"
readout "$\theta=$" "deg(atan2(Z_y,Z_x))" unit="°"
readout "$\arctan(b/a)=$" "deg(atan(Z_y/Z_x))" unit="°"
caption "Drag $z$ into the left half: $\arctan(b/a)$ is now off by $180^\circ$ from the true angle $\theta$."
''')
D.P(r"**Euler's identity** connects the two forms:", cites=W(1, 4))
D.EQ(r'e^{j\theta}=\cos\theta+j\sin\theta\quad\Rightarrow\quad c\,e^{j\theta}=\underbrace{c\cos\theta}_{a}+j\,\underbrace{c\sin\theta}_{b}',
     cites=W(1))
D.P(r"- $e^{j\theta}$ is the point at angle $\theta$ on the **unit circle** (the dashed circle above): its length is "
    r"$\sqrt{\cos^2\theta+\sin^2\theta}=1$."
    "\n"
    r"- Multiplying by $c$ stretches it out to length $c$. That's where $a=c\cos\theta$ and $b=c\sin\theta$ come from.",
    cites=W(4))

D.EX('Left half of the plane: the arctan trap', r'Write $z=-3+j4$ in polar form.', [
    S('The length uses Pythagoras; signs don\'t matter.', r'c=\sqrt{(-3)^2+4^2}=5'),
    S(r'The calculator gives $\arctan\frac{4}{-3}=-53.13^\circ$, which points down-right. But $z$ is up-left ($a<0$).',
      r'\arctan\frac{4}{-3}=-53.13^\circ\quad\text{(wrong side)}'),
    S(r'$a<0$, so add $180^\circ$. (`Pol(-3,4)` on a Casio does this for you.)', r'\theta=-53.13^\circ+180^\circ=126.87^\circ'),
], r'$z=5\angle126.87^\circ=5e^{j126.87^\circ}$', cites=W(3))

D.EX('Polar back to rectangular', r'Write $z=10\angle{-150^\circ}$ as $a+jb$.', [
    S(r'No quadrant thinking needed: the signs of $\cos$ and $\sin$ handle it.', r'a=10\cos(-150^\circ)=-8.66'),
    S('Same for the imaginary part.', r'b=10\sin(-150^\circ)=-5'),
], r'$z=-8.66-j5$ (down-left, as $-150^\circ$ says)', cites=W(2))

D.EX("Trig identities for free (lecture)", r'Use $e^{jA}e^{jB}=e^{j(A+B)}$ to get the formulas for $\cos(A+B)$ and $\sin(A+B)$.', [
    S(steps_fence('', [
        (r'e^{jA}\,e^{jB}=e^{j(A+B)}', 'Exponents add when you multiply.'),
        (r'\hl{(\cos A+j\sin A)(\cos B+j\sin B)}=\hl{\cos(A+B)+j\sin(A+B)}', "Write every exponential with Euler's identity."),
        (r'\cos A\cos B+j\cos A\sin B+j\sin A\cos B+\hl{j^2}\sin A\sin B', 'Expand the left side like ordinary brackets.'),
        (r'\hl{(\cos A\cos B-\sin A\sin B)}+j\hl{(\sin A\cos B+\cos A\sin B)}', r'$j^2=-1$; group the terms without $j$ and with $j$.'),
        (r'\cos(A+B)=\cos A\cos B-\sin A\sin B', 'Two complex numbers are equal only if their real parts match…'),
        (r'\sin(A+B)=\sin A\cos B+\cos A\sin B', '…and their imaginary parts match.'),
    ])),
], r'$\cos(A+B)=\cos A\cos B-\sin A\sin B$, $\ \sin(A+B)=\sin A\cos B+\cos A\sin B$', cites=W(2))

D.PR('Euler on the axes', r'Without a calculator, find $e^{j\pi}$, $e^{j\pi/2}$ and $e^{-j\pi/2}$. (Angles in radians: $\pi=180^\circ$.)', [
    S(r'$e^{j\theta}$ is the point at angle $\theta$ on the unit circle. $\pi$ is $180^\circ$: straight left.', r'e^{j\pi}=\cos\pi+j\sin\pi=-1'),
    S(r'$\pi/2$ is $90^\circ$: straight up.', r'e^{j\pi/2}=\cos\tfrac{\pi}{2}+j\sin\tfrac{\pi}{2}=j'),
    S(r'$-\pi/2$ is $90^\circ$ clockwise: straight down.', r'e^{-j\pi/2}=-j'),
], r'$e^{j\pi}=-1$, $\ e^{j\pi/2}=j$, $\ e^{-j\pi/2}=-j$')

# ================================================================ Topic 2
D.H('Topic 2: Complex arithmetic', cites=W(3, 4))
D.P('Each operation is easy in one form and messy in the other:')
D.T(['Operation', 'Use', 'Rule'], [
    ['Add, subtract', 'rectangular', 'add the real parts and the imaginary parts separately'],
    ['Multiply', 'polar', r'lengths multiply, angles add: $c_1e^{j\theta_1}\cdot c_2e^{j\theta_2}=c_1c_2\,e^{j(\theta_1+\theta_2)}$'],
    ['Divide', 'polar', r'lengths divide, angles subtract: $\dfrac{c_1e^{j\theta_1}}{c_2e^{j\theta_2}}=\dfrac{c_1}{c_2}e^{j(\theta_1-\theta_2)}$'],
    ['Divide', 'rectangular', 'multiply top and bottom by the conjugate of the bottom'],
    [r'Power $z^k$', 'polar', r"$c^k\,e^{jk\theta}$ (de Moivre's theorem)"],
    [r'$k$-th roots', 'polar', r'$c^{1/k}\,e^{j(\theta+360^\circ\ell)/k}$ for $\ell=0,1,\dots,k-1$: $k$ answers'],
], cites=W(3, 4))
D.P(r'**Conjugate** $z^*$: flip the sign of the imaginary part.'
    '\n'
    r'- $z^*=a-jb=c\,e^{-j\theta}$ (mirror image across the real axis)'
    '\n'
    r'- $z\,z^*=a^2+b^2=c^2$, always a **real** number. That is what makes rectangular division work.', cites=W(4))
D.GRAPH(r'''
title "Multiplying: lengths multiply, angles add"
x -4 4 label="Re"
y -3 3 label="Im"
equal
drag Z 1.5 0.5 label="$z$" color=1 snap=0.25
drag W 0.5 1.5 label="$w$" color=3 snap=0.25
arrow "Z_x" "Z_y" color=1
arrow "W_x" "W_y" color=3
arrow "Z_x*W_x-Z_y*W_y" "Z_x*W_y+Z_y*W_x" color=2 label="$zw$"
circle "0" "0" "1" dash color=0
readout "$|z|\,|w|=$" "hypot(Z_x,Z_y)*hypot(W_x,W_y)"
readout "$|zw|=$" "hypot(Z_x*W_x-Z_y*W_y,Z_x*W_y+Z_y*W_x)"
readout "$\angle z+\angle w=$" "deg(atan2(Z_y,Z_x))+deg(atan2(W_y,W_x))" unit="°"
readout "$\angle zw=$" "deg(atan2(Z_x*W_y+Z_y*W_x,Z_x*W_x-Z_y*W_y))" unit="°"
caption "Put $w$ on the dashed unit circle: then $zw$ is just $z$ rotated."
''')

D.EX('Dividing in rectangular form (lecture Example 1.1)', r'Find $\dfrac{80+j18}{8+j10}$.', [
    S(steps_fence('', [
        (r'\dfrac{80+j18}{8+j10}', 'The $j$ in the bottom is the problem.'),
        (r'\dfrac{80+j18}{8+j10}\cdot\hl{\dfrac{8-j10}{8-j10}}', 'Multiply top and bottom by the conjugate of the bottom (that is multiplying by 1).'),
        (r'=\dfrac{(80+j18)(8-j10)}{\hl{64+100}}', r'Bottom: $zz^*=a^2+b^2$, a real number.'),
        (r'=\dfrac{\hl{640+180}+j(\hl{144-800})}{164}', r'Top: expand, with $j\cdot j=-1$ turning $-j^2180$ into $+180$.'),
        (r'=\dfrac{820-j656}{164}=\hl{5-j4}', 'Divide each part by 164.'),
    ])),
], r'$5-j4$', cites=W(4))

D.EX("A big power: de Moivre", r'Find $(1+j)^8$.', [
    S(r"Multiplying out 8 brackets is painful; in polar form it's one step. $1+j$ is 1 right and 1 up.", r'1+j=\sqrt2\angle45^\circ'),
    S('Raise the length to the 8th power and multiply the angle by 8.', r'(\sqrt2)^8\angle(8\times45^\circ)=16\angle360^\circ'),
    S(r'$360^\circ$ is a full turn: pointing along the positive real axis.', r'16\angle360^\circ=16'),
], r'$(1+j)^8=16$', cites=W(4))

D.EX('All four fourth roots (lecture Example 1.2)', r'Find all fourth roots of $z=81e^{j60^\circ}$.', [
    S(r'Every root has length $81^{1/4}$.', r'81^{1/4}=3'),
    S(r'The first root has a quarter of the angle.', r'\tfrac{60^\circ}{4}=15^\circ\ \Rightarrow\ 3e^{j15^\circ}'),
    S(r'The other three are spaced $\tfrac{360^\circ}{4}=90^\circ$ apart round the same circle.', r'3e^{j15^\circ},\ 3e^{j105^\circ},\ 3e^{j195^\circ},\ 3e^{j285^\circ}'),
    S(r'Check one: $(3e^{j105^\circ})^4=81e^{j420^\circ}$, and $420^\circ-360^\circ=60^\circ$ ✓', ''),
], r'$3e^{j15^\circ},\ 3e^{j105^\circ},\ 3e^{j195^\circ},\ 3e^{j285^\circ}$', cites=W(4, 5))
# one point per root l = 0..5; roots with l >= k evaluate to NaN (sqrt(-1)) and are not drawn
roots = '\n'.join(
    f'point "if(k>{l},c^(1/k)*cos(rad((th+360*{l})/k)),sqrt(-1))" '
    f'"if(k>{l},c^(1/k)*sin(rad((th+360*{l})/k)),sqrt(-1))" color={1 if l else 2}'
    for l in range(6))
D.GRAPH(r'''
title "The $k$ roots of $z=c\angle\theta$ sit evenly on one circle"
x -4.6 4.6 label="Re"
y -4.6 4.6 label="Im"
equal
slider k 3 6 4 step=1 label="$k$"
slider c 1 81 81 step=1 label="$c$"
slider th 0 360 60 step=5 label="$\theta$ (°)"
''' + roots + r'''
circle "0" "0" "c^(1/k)" dash color=0
readout "radius $c^{1/k}=$" "c^(1/k)"
readout "first angle $\theta/k=$" "th/k" unit="°"
readout "spacing $360^\circ/k=$" "360/k" unit="°"
caption "Orange is the first root ($\ell=0$). Set $k=4$, $c=81$, $\theta=60^\circ$ for the lecture example."
''')

D.EX('Square root of a negative: complex roots of a quadratic', r'Solve $s^2+2s+5=0$.', [
    S('Quadratic formula with $a=1$, $b=2$, $c=5$.', r's=\frac{-2\pm\sqrt{4-20}}{2}=\frac{-2\pm\sqrt{-16}}{2}'),
    S(r'$\sqrt{-16}=\sqrt{16}\,\sqrt{-1}=j4$.', r's=\frac{-2\pm j4}{2}=-1\pm j2'),
], r'$s=-1\pm j2$ (a conjugate pair)')

D.PR('Cube roots of a negative number', r'Find all three cube roots of $-8$. Give each in polar and rectangular form.', [
    S(r'$-8$ points straight left: length 8, angle $180^\circ$.', r'-8=8\angle180^\circ'),
    S(r'Root length $8^{1/3}=2$; first angle $\tfrac{180^\circ}{3}=60^\circ$; spacing $\tfrac{360^\circ}{3}=120^\circ$.', r'2\angle60^\circ,\quad 2\angle180^\circ,\quad 2\angle300^\circ'),
    S(r'Convert with $a=c\cos\theta$, $b=c\sin\theta$.', r'1+j1.732,\quad -2,\quad 1-j1.732'),
], r'$2\angle60^\circ=1+j\sqrt3$, $\ 2\angle180^\circ=-2$, $\ 2\angle300^\circ=1-j\sqrt3$', diff='intermediate')

D.PR('A high power of j', r'Simplify $j^{27}$.', [
    S(r'$j$ is length 1 at $90^\circ$, so $j^{27}$ is length 1 at $27\times90^\circ$.', r'j^{27}=1\angle2430^\circ'),
    S(r'Remove whole turns: $2430^\circ-6\times360^\circ=270^\circ$, which points straight down.', r'1\angle270^\circ=-j'),
], r'$j^{27}=-j$')

# ================================================================ Topic 3
D.H('Topic 3: Your first differential equation: the RL natural response', cites=W(5, 6))
D.SCH(r'''I1 0,3 -> 0,0 "$I_s$"
wire 0,3 -> 3,3
R0 3,3 -> 3,0 "$R_0$"
S1 3,3 -> 6,3 "$t=0$" state=closed action=open
L1 6,0 -> 6,3 "$L$" i="$i$"
wire 6,3 -> 9,3
R1 9,3 -> 9,0 "$R$" v="$v$"
wire 0,0 -> 9,0
ground 0,0
#~ flow
#~ value I1 4
#~ value R0 10
#~ value L1 8m
#~ value R1 4
#~ slow 1000
#~ probe L1 "inductor $L$:"
#~ probe R1 "resistor $R$:"
#~ probe R0 "resistor $R_0$:"
#~ note "Dots show the current: faster dots, more current. Values: $I_s=4$ A, $R_0=10\,\Omega$, $L=8$ mH, $R=4\,\Omega$."''',
      'Lecture Fig. 1. **Click the switch** (or the button) to open it, and watch where the current goes.', cites=W(5))
D.P(r"- **Before $t=0$:** the inductor has been in DC a long time, so it acts like a wire and carries all of $I_s$."
    "\n"
    r"- **At $t=0$:** the switch opens. An inductor's current **can't jump**, so $i(0)=I_s$."
    "\n"
    r"- **After:** only the $L$–$R$ loop is left. KVL around it gives the equation below."
    "\n\n"
    r"That equation is a **differential equation**: the unknown is a *function* $i(t)$, and the equation involves its "
    r"rate of change $\frac{di}{dt}$.", cites=W(5, 6))
D.STEPS('Solving the RL loop (lecture)', [
    (r'L\dfrac{di}{dt}+Ri=0', r'KVL around the loop: the inductor voltage is $L\frac{di}{dt}$, the resistor voltage $Ri$.'),
    (r'\dfrac{di}{\hl{i}}=\hl{-\dfrac{R}{L}\,dt}', r'Divide by $L$ and by $i$, multiply by $dt$: all $i$ on the left, all $t$ on the right.'),
    (r'\hl{\int_{i(0)}^{i(t)}}\dfrac{dx}{x}=-\dfrac{R}{L}\hl{\int_0^t}ds', r'Integrate from the start ($0$, $i(0)$) to any time $t$. $x$ and $s$ are placeholder names.'),
    (r'\hl{\ln i(t)-\ln i(0)}=-\dfrac{R}{L}\,t', r'$\int\frac{dx}{x}=\ln x$, and $\int ds=s$.'),
    (r'\hl{\ln\dfrac{i(t)}{i(0)}}=-\dfrac{R}{L}\,t', r'$\ln A-\ln B=\ln\frac{A}{B}$.'),
    (r'\dfrac{i(t)}{i(0)}=\hl{e^{-(R/L)t}}', r'Undo $\ln$ by raising $e$ to both sides.'),
    (r'i(t)=\hl{I_s}\,e^{-t/\tau},\qquad \hl{\tau=\dfrac{L}{R}}', r'Multiply by $i(0)=I_s$. $\tau$ (tau) is the **time constant**, in seconds.'),
], intro='')
D.GRAPH(r'''
title "$i(t)=I_se^{-t/\tau}$: change $\tau$ and $I_s$"
x 0 6 label="$t$ (s)"
y 0 5 label="$i$ (A)"
slider tau 0.2 3 1 step=0.05 label="$\tau$" animate
slider I 0.5 4.5 4 step=0.1 label="$I_s$"
curve "I*exp(-t/tau)" label="$I_se^{-t/\tau}$"
vline "tau" label="$t=\tau$"
point "tau" "I*exp(-1)" color=2
vline "5*tau" color=0
readout "$i(\tau)=$" "I*exp(-1)"
readout "$i(\tau)/I_s=$" "exp(-1)"
caption "After one $\tau$, $37\%$ is left; after $5\tau$ (grey line), under $1\%$."
''')
D.STEPS("Where the $e$ comes from (lecture's outline)", [
    (r'\dfrac{dy}{dt}+y=0,\qquad y(0)=y_0', 'The simplest version of the RL equation.'),
    (r'\hl{\dfrac{y(t)-y(t-\Delta)}{\Delta}}+y(t)\approx0', r'Replace the derivative by a slope over a tiny time step $\Delta$.'),
    (r'y(t)\,\hl{(1+\Delta)}=y(t-\Delta)', r'Multiply by $\Delta$ and rearrange: every step divides $y$ by $(1+\Delta)$.'),
    (r'y(t)=y(0)\,(1+\Delta)^{\hl{-t/\Delta}}', r'Going from $0$ to $t$ takes $t/\Delta$ steps.'),
    (r'y(t)=y(0)\,\Big[\hl{(1+\Delta)^{1/\Delta}}\Big]^{-t}', 'Regroup the exponent.'),
    (r'y(t)=y(0)\,\hl{e}^{-t}', r'As $\Delta\to0$, $(1+\Delta)^{1/\Delta}\to e\approx2.718$. That is one definition of $e$.'),
])

D.EX('Pre-tutorial 1: numbers in the RL loop', r'In the circuit above, $L=8\,\mathrm{mH}$, $R=4\,\Omega$ and $I_s=4\,\mathrm{A}$. '
     r'Find $i(t)$ and $v(t)$ for $t\ge0$, and sketch $i(t)$.', [
    S(r"The current can't jump, so it starts at $I_s$.", r'i(0)=4\,\mathrm{A}'),
    S(r'Time constant (convert mH to H).', r'\tau=\frac{L}{R}=\frac{8\times10^{-3}}{4}=2\,\mathrm{ms},\quad \frac1\tau=500\,\mathrm{s^{-1}}'),
    S(r'Put both into $i(t)=I_se^{-t/\tau}$.', r'i(t)=4e^{-500t}\,\mathrm{A}'),
    S(r'The current comes down through $R$ from $+$ to $-$, so $v=Ri$.', r'v(t)=4\cdot4e^{-500t}=16e^{-500t}\,\mathrm{V}'),
], r'$\tau=2\,\mathrm{ms}$, $i(t)=4e^{-500t}\,\mathrm{A}$, $v(t)=16e^{-500t}\,\mathrm{V}$', cites=T1 + W(6))
D.GRAPH(r'''
title "Sketch: $i(t)=4e^{-500t}$ A"
x 0 10 label="$t$ (ms)"
y 0 4.5 label="$i$ (A)"
curve "4*exp(-t/2)" label="$i(t)$"
vline "2" label="$t=\tau=2$ ms"
point "2" "4*exp(-1)" color=2
text "2.3" "1.95" "$1.47$ A"
caption "Starts at 4 A, is at $37\%$ (1.47 A) after one $\tau$, gone by $5\tau=10$ ms."
''')

D.EX('How long until it is small?', r'An RL loop has $L=0.5\,\mathrm{H}$, $R=100\,\Omega$ and $i(0)=10\,\mathrm{A}$. When is $i=1\,\mathrm{A}$?', [
    S('Time constant and response.', r'\tau=\frac{0.5}{100}=5\,\mathrm{ms},\qquad i(t)=10e^{-t/\tau}'),
    S(r'Set $i=1$ and isolate the exponential.', r'e^{-t/\tau}=0.1'),
    S(r'Take $\ln$ of both sides ($\ln e^x=x$).', r'-\frac{t}{\tau}=\ln0.1=-2.303'),
    S(r'Multiply by $-\tau$.', r't=2.303\,\tau=11.5\,\mathrm{ms}'),
], r'$t=\tau\ln10=11.5\,\mathrm{ms}$')

D.PR('Check a solution by substituting it', r'Show that $i(t)=I_se^{-t/\tau}$ with $\tau=\dfrac{L}{R}$ really satisfies $L\dfrac{di}{dt}+Ri=0$.', [
    S(r'Differentiate: $\frac{d}{dt}e^{-t/\tau}=-\frac1\tau e^{-t/\tau}$ (chain rule).', r'\frac{di}{dt}=-\frac{I_s}{\tau}e^{-t/\tau}=-\frac{R}{L}I_se^{-t/\tau}'),
    S('Substitute both pieces into the left side.', r'L\Big(-\frac{R}{L}I_se^{-t/\tau}\Big)+R\,I_se^{-t/\tau}=-RI_se^{-t/\tau}+RI_se^{-t/\tau}=0\ \checkmark'),
], 'It gives $0$ for every $t$, so it is a solution.')

D.PR('Work backwards from a measurement', r'In an RL loop with $R=20\,\Omega$, the current halves every $3\,\mathrm{ms}$. Find $L$.', [
    S(r'Halving in $3\,\mathrm{ms}$ means $e^{-0.003/\tau}=\tfrac12$.', r'\frac{0.003}{\tau}=\ln2\ \Rightarrow\ \tau=\frac{0.003}{0.693}=4.33\,\mathrm{ms}'),
    S(r'$\tau=L/R$, so $L=R\tau$.', r'L=20\times0.00433=0.0866\,\mathrm{H}'),
], r'$L\approx86.6\,\mathrm{mH}$', diff='intermediate')

D.save()
