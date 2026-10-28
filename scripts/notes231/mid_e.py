"""E: a short mixed practice set in midterm style (Weeks 1-6), copied from or modelled on the lectures and tutorials."""
import sympy as sp

from midlib import S, first, implicit, link, second, t, y, zero


def sch(src):
    return '```schematic\n' + src.strip() + '\n```'


def PE(D, title, prompt, steps, answer, diff='introductory', cites=()):
    """A Topic E problem, labelled 'E1', 'E2', ... instead of the note-wide 'Problem n'."""
    D.enum = getattr(D, 'enum', 0) + 1
    D.PR(title, prompt, steps, answer, diff=diff, cites=cites, label=f'E{D.enum}')


RC_STEP = r'''
I1 0,0 -> 0,3 "$3\,\mathrm{mA}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$2\,\mathrm{k\Omega}$"
S1 3,3 -> 6,3 "$t=0$" action=close
C1 6,3 -> 6,0 "$5\,\mu\mathrm{F}$" v="$v$" i="$i_C$"
wire 6,0 -> 0,0
ground 0,0
'''

RLC_STEP = r'''
I1 0,0 -> 0,3 "$24\,\mathrm{mA}$"
S1 0,3 -> 3,3 "$t=0$" action=close
C1 3,3 -> 3,0 "$25\,\mathrm{nF}$" i="$i_C$"
wire 3,3 -> 6,3
L1 6,3 -> 6,0 "$25\,\mathrm{mH}$" i="$i_L$"
wire 6,3 -> 9,3
R1 9,3 -> 9,0 "$400\,\Omega$" i="$i_R$" v="$v$"
wire 9,0 -> 0,0
ground 0,0
'''


def build(D):
    D.H('Topic E: Practice midterm')
    D.P('**The professor’s advice:** “Study all the examples in the lectures and posted materials, and those in the tutorials, and you will be fine. '
        'The examples will be a good guide to the problems on the Midterm.”')
    D.P('So this set is built from those examples. Some are copied straight from a lecture or tutorial. '
        'The rest change the numbers or add a twist, so you practise the exact move the example teaches.')
    D.P('**How to use it:**')
    D.L([r'Close the rest of the note. Do a whole problem on paper before you open its solution.',
         r'Start every answer by naming the **type** and the clue. On the exam, that’s the step that picks the method.',
         r'Stuck or wrong? Each answer box links to the section to review.'],
        ordered=True)
    D.P('**Redo the worked examples too, solutions closed.** They’re the lecture and tutorial examples themselves:')
    D.L([r'Example 1 (fourth roots) · Example 2 (separable) · Example 3 (integrating factor) · Example 4 (exact)',
         r'Example 5 (Pre-tutorial 4) · Example 7 (Pre-tutorial 5) · Example 8 (reduction of order) · Example 9 (RL circuit)'])

    PE(D, 'W1 · Divide, convert, take roots · like lecture Examples 1.1 and 1.2',
      r'(a) Write $z=\dfrac{10+j5}{2-j}$ in rectangular form. (b) Write $z$ in polar form. '
      r'(c) Find all three cube roots of $8j$, in polar and in rectangular form.',
      [S(r'**Type:** (a) division in rectangular form, so multiply top and bottom by the conjugate of the bottom, $2+j$.',
         r'z=\dfrac{(10+j5)(2+j)}{(2-j)(2+j)}=\dfrac{20+10j+10j+5j^2}{4+1}'),
       S(r'**Multiply out:** $j^2=-1$, so $5j^2=-5$.', r'z=\dfrac{15+j20}{5}=3+j4'),
       S(r'(b) **Length:** $\sqrt{3^2+4^2}$. **Angle:** $3+j4$ is in the 1st quadrant, so $\tan^{-1}\frac43$ is already right.',
         r'z=5\,e^{j53.13^\circ}'),
       S(r'(c) **Polar first:** $8j$ sits on the positive imaginary axis.', r'8j=8\,e^{j90^\circ}'),
       S(r'**Length and first angle:** take the cube root of the length, and divide the angle by 3.', r'8^{1/3}=2,\qquad \dfrac{90^\circ}{3}=30^\circ'),
       S(r'**Spacing:** three roots, so $360^\circ/3=120^\circ$ apart.', r'2e^{j30^\circ},\quad 2e^{j150^\circ},\quad 2e^{j270^\circ}'),
       S(r'**Rectangular:** $2\cos30^\circ=\sqrt3$, $2\sin30^\circ=1$, and so on.', r'\sqrt3+j,\quad -\sqrt3+j,\quad -j2')],
      r'(a) $3+j4$. (b) $5e^{j53.13^\circ}$. (c) $2e^{j30^\circ}=\sqrt3+j$, $\;2e^{j150^\circ}=-\sqrt3+j$, $\;2e^{j270^\circ}=-j2$. '
      r'Review: ' + link('Topic A', 'topic-a') + '.',
      diff='introductory')

    PE(D, 'W2 · Classify, then use linearity',
      r'For each equation, give the order and say whether it is linear, homogeneous, constant-coefficient and autonomous.' '\n\n'
      r'(a) $\dfrac{d^2i}{dt^2}+\dfrac{R}{L}\dfrac{di}{dt}+\dfrac{1}{LC}\,i=0$ (the series RLC circuit of the Week 2 notes)' '\n\n'
      r'(b) $y\prime=y^2+t$' '\n\n'
      r'(c) $y\prime\prime+y=6\cos^2t$' '\n\n'
      r'(d) $y=e^{-t}$ solves $y\prime+2y=e^{-t}$. Without solving, give a solution of $y\prime+2y=5e^{-t}$.',
      [S(r'**Type:** classification. (a) Highest derivative $i\prime\prime$: 2nd order. $i$ appears to the power 1: linear. Right side $0$: homogeneous. '
         r'$R,L,C$ are numbers: constant coefficients. No $t$ anywhere: autonomous.'),
       S(r'(b) 1st order. $y^2$ is not power 1, so **nonlinear**. The $t$ on the right means it is not autonomous.'),
       S(r'(c) 2nd order, linear, numbers in front. Right side is not $0$, so **not** homogeneous. $\cos^2t$ has a $t$, so not autonomous.'),
       S(r'(d) **Linearity:** multiply $y$ by 5 and the whole left side gets multiplied by 5. So $5e^{-t}$ gives $5e^{-t}$ on the right.',
         r'(5e^{-t})\prime+2(5e^{-t})=-5e^{-t}+10e^{-t}=5e^{-t}\ \checkmark')],
      r'(a) 2nd order, linear, homogeneous, constant-coefficient, autonomous. (b) 1st order, nonlinear, not autonomous. '
      r'(c) 2nd order, linear, not homogeneous, constant-coefficient, not autonomous. (d) $y=5e^{-t}$. '
      r'Review: ' + link('Topic B', 'topic-b') + '.',
      diff='introductory')

    PE(D, 'W3–W4 · Name the type, then solve · like lecture Examples 3.3, 3.1 and 4.1',
      r'Name the type of each equation, then solve it.' '\n\n'
      r'(a) $\dfrac{dy}{dt}=\dfrac{2t+2ty^2}{y+t^2y}$, $\;y(0)=1$' '\n\n'
      r'(b) $\dfrac{dy}{dt}+\dfrac{6y}{3t+2}=4$, $\;y(0)=0$' '\n\n'
      r'(c) $(2t+y\cos t)\,dt+(\sin t+2y)\,dy=0$, $\;y(0)=1$',
      [S(r'(a) **Type:** factor the top and the bottom. It becomes a $t$-part times a $y$-part, so separable.', r'\dfrac{dy}{dt}=\dfrac{2t(1+y^2)}{y(1+t^2)}'),
       S(r'**Separate:** every $y$ left, every $t$ right.', r'\dfrac{y}{1+y^2}\,dy=\dfrac{2t}{1+t^2}\,dt'),
       S(r'**Integrate:** each side is (derivative of the bottom) over (the bottom), up to a constant factor.', r'\tfrac12\ln(1+y^2)=\ln(1+t^2)+c\ \Rightarrow\ 1+y^2=C(1+t^2)^2'),
       S(r'**Condition** $y(0)=1$: $1+1=C$, so $C=2$. Take the $+$ root, since $y(0)=1>0$.', r'y=\sqrt{2(1+t^2)^2-1}'),
       S(r'(b) **Type:** $y\prime+a(t)\,y=f(t)$ with $a=\dfrac{6}{3t+2}$: linear. **Integrating factor:** $\int\frac{6}{3t+2}dt=2\ln(3t+2)$.', r'\mu=e^{2\ln(3t+2)}=(3t+2)^2'),
       S(r'**Rewrite and integrate:** the left side becomes $\big[(3t+2)^2y\big]\prime$. On the right, $\int4(3t+2)^2dt=\frac49(3t+2)^3$.', r'(3t+2)^2\,y=\tfrac49(3t+2)^3+C'),
       S(r'**Condition** $y(0)=0$: $0=\frac49\cdot8+C$, so $C=-\frac{32}{9}$. Divide by $(3t+2)^2$.', r'y=\tfrac49(3t+2)-\dfrac{32}{9(3t+2)^2}'),
       S(r'(c) **Type:** $M\,dt+N\,dy=0$. **Test:** $M_y=\cos t$ and $N_t=\cos t$ match, so exact.'),
       S(r'**Integrate** $M$ in $t$: $U=t^2+y\sin t+h(y)$. **Match:** $U_y=\sin t+h\prime(y)$ must equal $N=\sin t+2y$, so $h=y^2$.', r'U=t^2+y\sin t+y^2'),
       S(r'**Condition** $y(0)=1$: $U(0,1)=0+0+1=1$.', r't^2+y\sin t+y^2=1')],
      r'(a) Separable: $y=\sqrt{2(1+t^2)^2-1}$. (b) Linear: $y=\frac49(3t+2)-\dfrac{32}{9(3t+2)^2}$. (c) Exact: $t^2+y\sin t+y^2=1$. '
      r'Review: ' + link('B1', 'b1') + ', ' + link('B2', 'b2') + ', ' + link('B3', 'b3') + '.',
      diff='intermediate')

    PE(D, 'W4 · Not exact: find the factor, then solve · like Pre-tutorial 4',
      r'Consider $(3ty+y^2)\,dt+(t^2+ty)\,dy=0$ with $y(1)=1$. (a) Show it is not exact. (b) Find an integrating factor. (c) Solve.',
      [S(r'**Type:** $M\,dt+N\,dy=0$ with $M=3ty+y^2$, $N=t^2+ty$. (a) **Test:** the cross derivatives don’t match.', r'M_y=3t+2y\neq2t+y=N_t'),
       S(r'(b) **Ratios:** try Case 1. Factor the bottom: $N=t(t+y)$. The $(t+y)$ cancels and only $t$ is left.', r'\dfrac{M_y-N_t}{N}=\dfrac{t+y}{t(t+y)}=\dfrac1t\ \Rightarrow\ \mu=e^{\int\frac1t\,dt}=t'),
       S(r'**Multiply** by $t$, then test again: now they match.', r'(3t^2y+ty^2)\,dt+(t^3+t^2y)\,dy=0,\qquad M_y=3t^2+2ty=N_t'),
       S(r'(c) **Integrate** the new $M$ in $t$: $U=t^3y+\tfrac12t^2y^2+h(y)$. **Match:** $U_y=t^3+t^2y$ is already the new $N$, so $h=0$.', r'U=t^3y+\tfrac12t^2y^2'),
       S(r'**Condition** $y(1)=1$: $U(1,1)=1+\tfrac12=\tfrac32$. Multiply by 2.', r'2t^3y+t^2y^2=3')],
      r'(a) $M_y=3t+2y$, $N_t=2t+y$. (b) $\mu=t$. (c) $2t^3y+t^2y^2=3$. '
      r'If the ratio looked like it had both letters, factor before giving up: here $t+y$ cancels. Review: ' + link('B4', 'b4') + '.',
      diff='intermediate')

    PE(D, 'W3 + W5 · Is the solution guaranteed?',
      r'(a) For $\dfrac{dy}{dt}=3y^{2/3}$, does the theorem guarantee exactly one solution through (i) $(1,8)$, (ii) $(0,0)$? '
      r'Then check that $y=0$ and $y=t^3$ both solve it. What does that say about $(0,0)$?' '\n\n'
      r'(b) Without solving, find the largest interval on which $(t^2-9)\,y\prime\prime+t\,y\prime+y=\dfrac1t$, $\;y(1)=0$, $y\prime(1)=2$, has exactly one solution.',
      [S(r'(a) **Type:** first order, $y\prime=F(t,y)$, with $F=3y^{2/3}$. Check $F$ and $\partial F/\partial y$.', r'\dfrac{\partial F}{\partial y}=2y^{-1/3}=\dfrac{2}{y^{1/3}}'),
       S(r'**Find the bad set:** $F$ is fine everywhere, but $\partial F/\partial y$ breaks at $y=0$ (division by zero).'),
       S(r'**Check the point:** (i) $y=8$ is away from $y=0$, so the theorem guarantees one solution. (ii) $y=0$ is in the bad set, so no guarantee.'),
       S(r'**Two solutions:** both pass through $(0,0)$, so at $(0,0)$ there really is more than one solution.', r'y=0:\ 0=0\ \checkmark\qquad y=t^3:\ 3t^2=3(t^3)^{2/3}=3t^2\ \checkmark'),
       S(r'(b) **Type:** second-order linear, so use the interval theorem. **Divide** by $t^2-9$.', r'p=\dfrac{t}{t^2-9},\quad q=\dfrac{1}{t^2-9},\quad g=\dfrac{1}{t(t^2-9)}'),
       S(r'**Trouble points:** zeros of the bottoms, $t=-3,\,0,\,3$. **Pick the piece** that contains $t_0=1$.', r'0<t<3')],
      r'(a) (i) Yes. (ii) No guarantee, and in fact two solutions ($y=0$, $y=t^3$) pass through $(0,0)$. (b) $0<t<3$. '
      r'Review: ' + link('C1', 'c1') + ', ' + link('C2', 'c2') + '.',
      diff='intermediate')

    PE(D, 'W2 · RC step response, and a current that jumps · like Pre-tutorial 2',
      r'Before $t=0$ the switch is open and the capacitor holds $v=2\,\mathrm{V}$. The switch closes at $t=0$. '
      r'(a) Write the ODE for $v$ for $t\ge0$. (b) Find $v(t)$. (c) Find $i_C$ just before and just after the switch closes.' '\n\n' + sch(RC_STEP),
      [S(r'**Type:** after the switch, one capacitor with a resistor and a DC source: first-order RC step response.'),
       S(r'(a) **KCL** at the top node for $t\ge0$: the source current splits into $R$ and $C$.', r'C\dfrac{dv}{dt}+\dfrac{v}{R}=I_s\ \Rightarrow\ \dfrac{dv}{dt}+100\,v=600'),
       S(r'(b) **Time constant:** $\tau=RC=2000\times5\times10^{-6}$. **Final value:** $C$ is open, so all of $I_s$ goes through $R$.', r'\tau=0.01\,\mathrm{s},\qquad v_f=RI_s=6\,\mathrm{V}'),
       S(r'**Plug in:** $v=v_f+(v_0-v_f)e^{-t/\tau}$ with $v_0=2\,\mathrm{V}$ (the capacitor voltage can’t jump).', r'v=6-4e^{-100t}\ \mathrm{V},\quad t\ge0'),
       S(r'(c) **Before:** the switch is open, so no current reaches $C$: $i_C(0^-)=0$. '
         r'**Just after:** $v=2\,\mathrm{V}$ still, so $R$ takes $2/2000=1\,\mathrm{mA}$ and $C$ gets the rest.', r'i_C(0^+)=3-1=2\,\mathrm{mA}'),
       S(r'**Check** with $i_C=C\,v\prime$ from (b).', r'i_C(0^+)=5\times10^{-6}\times400=2\times10^{-3}\,\mathrm{A}\ \checkmark')],
      r'(a) $v\prime+100v=600$. (b) $v=6-4e^{-100t}\,\mathrm{V}$. (c) $0$ before, $2\,\mathrm{mA}$ after: the capacitor **current** jumps, its voltage doesn’t. '
      r'Review: ' + link('D1', 'd1') + '.',
      diff='introductory')

    PE(D, 'W5 · Complex roots, then a repeated root',
      r"Solve (a) $y''+4y'+13y=0$, and (b) $y''+4y'+4y=0$, each with $y(0)=1$, $y'(0)=0$.",
      [S(r'(a) **Type:** numbers in front, right side $0$. **Characteristic equation:** $s^2+4s+13=0$.', r's=\dfrac{-4\pm\sqrt{16-52}}{2}=-2\pm j3'),
       S(r'**Form:** a complex pair $-2\pm j3$ gives decay $e^{-2t}$ times a cosine and sine of $3t$.', r'y=e^{-2t}(A\cos3t+B\sin3t)'),
       S(r'**Conditions:** $y(0)=A=1$. The slope at $0$ is $-2A+3B=0$, so $B=\frac23$.', r'y=e^{-2t}\big(\cos3t+\tfrac23\sin3t\big)'),
       S(r'(b) **Characteristic equation:** $s^2+4s+4=(s+2)^2$, a repeated root $s=-2$. **Form:** add a $t$ to the second term.', r'y=(c_1+c_2t)e^{-2t}'),
       S(r'**Conditions:** $y(0)=c_1=1$. The slope at $0$ is $c_2-2c_1=0$, so $c_2=2$.', r'y=(1+2t)e^{-2t}')],
      r'(a) $y=e^{-2t}\big(\cos3t+\tfrac23\sin3t\big)$. (b) $y=(1+2t)e^{-2t}$. Review: ' + link('B5', 'b5') + '.',
      diff='introductory')

    PE(D, 'W5 · Parallel RLC step response · lecture Example 5.2, plus a twist',
      r'The initial energy stored in the circuit is zero. At $t=0$ a DC current source of $24\,\mathrm{mA}$ is applied. '
      r'(a) Find $i_L(t)$ for $t\ge0$. (b) Twist: which $R$ would make the circuit critically damped? Find $i_L(t)$ for that $R$.' '\n\n' + sch(RLC_STEP),
      [S(r'**Type:** $C$, $L$, $R$ in parallel with a DC source: parallel RLC step response. KCL gives the lecture’s equation.', r"i_L''+\dfrac{1}{RC}\,i_L'+\dfrac{1}{LC}\,i_L=\dfrac{I}{LC}"),
       S(r'(a) **Equation:** compare $\alpha=\frac{1}{2RC}$ with $\omega_0=\frac{1}{\sqrt{LC}}$. $\alpha>\omega_0$, so overdamped.', r'\alpha=\dfrac{1}{2(400)(25\times10^{-9})}=50000,\qquad \omega_0=\dfrac{1}{\sqrt{25\times10^{-3}\cdot25\times10^{-9}}}=40000'),
       S(r'**Roots:** $s=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}=-50000\pm30000$. **Final value:** in DC steady state $L$ is a short and takes all $24\,\mathrm{mA}$.', r'i_L=24+A_1e^{-20000t}+A_2e^{-80000t}\ \mathrm{mA}'),
       S(r'**Starting values:** zero energy means $i_L(0)=0$ and $v(0)=0$. Since $v=L\,i_L\prime$, the starting slope is $0$ too.', r'A_1+A_2=-24,\qquad -20000A_1-80000A_2=0'),
       S(r'**Constants:** the second equation gives $A_1=-4A_2$. Then $-3A_2=-24$.', r'A_2=8,\qquad A_1=-32'),
       S(r'(b) **Critical damping** means $\alpha=\omega_0=40000$. Solve $\frac{1}{2RC}=40000$ for $R$.', r'R=\dfrac{1}{2(40000)(25\times10^{-9})}=500\,\Omega'),
       S(r'**Form:** one repeated root $s=-40000$. Same final value.', r'i_L=24+(D_1+D_2t)e^{-40000t}\ \mathrm{mA}'),
       S(r'**Constants:** $i_L(0)=0$ gives $D_1=-24$. The slope at $0$ is $D_2-40000D_1=0$.', r'D_2=-960000\ \mathrm{mA/s}')],
      r'(a) $i_L=24-32e^{-20000t}+8e^{-80000t}\ \mathrm{mA}$ (the lecture’s answer). (b) $R=500\,\Omega$: $i_L=24-24(1+40000t)e^{-40000t}\ \mathrm{mA}$. '
      r'Review: ' + link('D2', 'd2') + '.',
      diff='intermediate', cites=D.cite('W5', 5, 6))

    PE(D, 'W6 · The tutorial problem without the hints · Pre-tutorial 5',
      r"(a) Solve $y''+y=6\cos^2t$, $\;y(0)=0$, $\;y(\pi/2)=0$. This time the forms of $y_c$ and $y_p$ are **not** given." '\n\n'
      r"(b) For $y''-4y=e^{2t}+t$, write the form of $y_p$ and find it.",
      [S(r'(a) **Type:** numbers in front, right side not $0$: undetermined coefficients. **Complementary:** $s^2+1=0$, $s=\pm j$.', r'y_c=c_1\sin t+c_2\cos t'),
       S(r'No table row fits $\cos^2t$, so rewrite it first.', r'6\cos^2t=3+3\cos2t'),
       S(r'**Guess:** a constant for the $3$, both $\cos2t$ and $\sin2t$ for the $3\cos2t$. None of them is in $y_c$.', r'y_p=A+B\cos2t+D\sin2t'),
       S(r'**Substitute:** $y_p\prime\prime=-4B\cos2t-4D\sin2t$. **Match:** constants, cosines, sines.', r'A=3,\qquad -3B=3,\qquad -3D=0'),
       S(r'**Add**, then use both **conditions** on the whole $y$: $y(0)=3-1+c_2=0$, $y(\pi/2)=3+1+c_1=0$.', r'y=3-\cos2t-4\sin t-2\cos t'),
       S(r'(b) **Complementary:** $s^2-4=0$, $s=\pm2$, so $y_c=c_1e^{2t}+c_2e^{-2t}$. **Guess:** $Ae^{2t}$ is in $y_c$, so multiply it by $t$. Add $Bt+C$ for the $t$.', r'y_p=Ate^{2t}+Bt+C'),
       S(r'**Substitute:** $(te^{2t})\prime\prime=(4+4t)e^{2t}$, so the $te^{2t}$ terms cancel against $-4Ate^{2t}$.', r'4Ae^{2t}-4Bt-4C=e^{2t}+t'),
       S(r'**Match:** $4A=1$, $-4B=1$, $-4C=0$.', r'y_p=\tfrac14te^{2t}-\tfrac14t')],
      r'(a) $y=3-\cos2t-4\sin t-2\cos t$. (b) $y_p=\frac14te^{2t}-\frac14t$. Review: ' + link('B6', 'b6') + '.',
      diff='intermediate', cites=D.cite('T5', 1))

    PE(D, 'W6 · Reduction of order · like lecture Example 6.1',
      r"Given that $y_1=t$ solves $t^2y''+t\,y'-y=0$ for $t>0$, find the general solution.",
      [S(r'**Type:** second order with $t$ in front, and one solution given: reduction of order. **Substitute** $y=tv$.', r"y'=v+tv',\qquad y''=2v'+tv''"),
       S(r'**Plug in** and **collect:** the $v$ terms cancel (they always do, because $t$ is a solution).', r"t^2(2v'+tv'')+t(v+tv')-tv=t^3v''+3t^2v'=0"),
       S(r'Set $z=v\prime$ and divide by $t^3$: a first-order equation in $z$. **Separate.**', r"\dfrac{dz}{z}=-\dfrac{3}{t}\,dt\ \Rightarrow\ z=\dfrac{C}{t^3}"),
       S(r'**Integrate** $z$ to get $v$.', r'v=-\dfrac{C}{2t^2}+C_2'),
       S(r'**Multiply back** by $t$, and rename the constant.', r'y=tv=C_2\,t-\dfrac{C}{2t}=c_1t+\dfrac{c_2}{t}')],
      r'$y=c_1t+\dfrac{c_2}{t}$. Check $y=\frac1t$: $t^2\cdot\frac{2}{t^3}+t\cdot\left(-\frac{1}{t^2}\right)-\frac1t=0$ ✓. Review: ' + link('B7', 'b7') + '.',
      diff='intermediate')


def verify():
    E = sp.exp
    c1, c2 = sp.symbols('c1 c2')
    j = sp.I
    # E1
    z = (10 + 5 * j) / (2 - j)
    zero(sp.expand(z) - (3 + 4 * j))
    assert sp.Abs(3 + 4 * j) == 5
    for k in range(3):
        root = 2 * sp.exp(j * sp.pi * (sp.Rational(1, 6) + sp.Rational(2, 3) * k))
        zero(sp.expand(root ** 3) - 8 * j)
    zero(sp.expand((sp.sqrt(3) + j) ** 3) - 8 * j)
    zero(sp.expand((-sp.sqrt(3) + j) ** 3) - 8 * j)
    zero(sp.expand((-2 * j) ** 3) - 8 * j)
    # E2 (d)
    second(5 * E(-t), 0, 1, 2, 5 * E(-t))
    second(E(-t), 0, 1, 2, E(-t))
    # E3
    rhs_a = 2 * t * (1 + y ** 2) / (y * (1 + t ** 2))
    first(sp.sqrt(2 * (1 + t ** 2) ** 2 - 1), rhs_a, (0, 1))
    first(sp.Rational(4, 9) * (3 * t + 2) - sp.Rational(32, 9) / (3 * t + 2) ** 2, 4 - 6 * y / (3 * t + 2), (0, 0))
    M, N = 2 * t + y * sp.cos(t), sp.sin(t) + 2 * y
    zero(sp.diff(M, y) - sp.diff(N, t))
    assert implicit(t ** 2 + y * sp.sin(t) + y ** 2, -M / N, (0, 1)) == 1
    # E4
    M, N = 3 * t * y + y ** 2, t ** 2 + t * y
    zero((sp.diff(M, y) - sp.diff(N, t)) / N - 1 / t)
    zero(sp.diff(t * M, y) - sp.diff(t * N, t))
    assert implicit(2 * t ** 3 * y + t ** 2 * y ** 2, -M / N, (1, 1)) == 3
    # E5
    zero(sp.diff(3 * y ** sp.Rational(2, 3), y) - 2 * y ** sp.Rational(-1, 3))
    tp = sp.symbols('tp', positive=True)
    zero(sp.diff(tp ** 3, tp) - 3 * (tp ** 3) ** sp.Rational(2, 3))
    # E6
    v = 6 - 4 * E(-100 * t)
    zero(sp.diff(v, t) + 100 * v - 600)
    zero(v.subs(t, 0) - 2)
    zero(sp.Rational(5, 10 ** 6) * sp.diff(v, t).subs(t, 0) - sp.Rational(2, 1000))
    # E7
    second(E(-2 * t) * (sp.cos(3 * t) + sp.Rational(2, 3) * sp.sin(3 * t)), 1, 4, 13, initial=(0, 1, 0))
    second((1 + 2 * t) * E(-2 * t), 1, 4, 4, initial=(0, 1, 0))
    # E8 (mA, with R, L, C in ohms, henries, farads)
    L, C = sp.Rational(25, 1000), sp.Rational(25, 10 ** 9)
    for R, iL in ((400, 24 - 32 * E(-20000 * t) + 8 * E(-80000 * t)),
                  (500, 24 - 24 * (1 + 40000 * t) * E(-40000 * t))):
        second(iL, 1, 1 / (R * C), 1 / (L * C), 24 / (L * C), initial=(0, 0, 0))
    # E9
    sol = 3 - sp.cos(2 * t) - 4 * sp.sin(t) - 2 * sp.cos(t)
    second(sol, 1, 0, 1, 6 * sp.cos(t) ** 2)
    zero(sol.subs(t, 0))
    zero(sol.subs(t, sp.pi / 2))
    second(t * E(2 * t) / 4 - t / 4, 1, 0, -4, E(2 * t) + t)
    # E10
    second(c1 * t + c2 / t, t ** 2, t, -1)
