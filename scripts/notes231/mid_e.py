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
    D.P('So this set is built from those examples, some copied, some with new numbers or a twist. '
        '**Every solution uses exactly the steps of its section**, word for word, so you practise the way you learned it.')
    D.P('**How to use it:**')
    D.L([r'Close the rest of the note. Do a whole problem on paper before you open its solution.',
         r'Start every answer with the **type** (which section) and the clue that told you.',
         r'Stuck or wrong? Each answer ends with the section to review.'], ordered=True)
    D.P('**The midterm question is always one of these.** Spot the clue, run the steps:')
    D.T(['You see…', 'Go to', 'First move'], [
        [r'a complex number to divide, convert, power, root', link('A', 'topic-a'), 'go polar'],
        [r'$y\prime=$ ($t$-part)($y$-part)', link('B1', 'b1'), 'separate'],
        [r'$y\prime+p(t)\,y=f(t)$', link('B2', 'b2'), r'$\mu=e^{\int p\,dt}$'],
        [r'$M\,dt+N\,dy=0$', link('B3', 'b3') + ' / ' + link('B4', 'b4'), r'test $M_y=N_t$'],
        [r'$ay\prime\prime+by\prime+cy=0$', link('B5', 'b5'), 'the quadratic'],
        [r'$ay\prime\prime+by\prime+cy=f(t)$', link('B6', 'b6'), r'$y_c$, then guess $y_p$'],
        [r'$t$ in front, $y_1$ given', link('B7', 'b7'), r'$y=y_1v$'],
        [r'“exactly one solution?”, “interval?”', link('C', 'topic-c'), 'find where it breaks'],
        [r'a circuit with a switch', link('D', 'topic-d'), 'Before → Carry across → After'],
    ])
    D.P(r'**Redo the full-example cards too, solutions closed:** B1 (lecture 3.3), B2 (lecture 3.1), B3 (lecture 4.1), B4 (Pre-tutorial 4), '
        r'B6 (the tutorial problem), B7 (the lecture example), D1 (the lecture RL circuit), D2 (P8.53).')

    PE(D, 'W1 · Divide, convert, take roots · like lecture Examples 1.1 and 1.2',
      r'(a) Write $z=\dfrac{10+j5}{2-j}$ in rectangular form. (b) Write $z$ in polar form. '
      r'(c) Find all three cube roots of $8j$, in polar and in rectangular form.',
      [S(r'(a) **Type:** dividing in rectangular → Topic A, Case 2. Multiply top and bottom by the conjugate of the bottom, $2+j$.',
         r'z=\dfrac{(10+j5)(2+j)}{(2-j)(2+j)}'),
       S(r'Multiply out. $j^2=-1$, so $5j^2=-5$. The bottom is $2^2+1^2$.', (r'(10+j5)(2+j)=20+j10+j10+5j^2=15+j20', r'(2-j)(2+j)=5')),
       S(r'Divide each part by $5$.', r'z=3+j4'),
       S(r'(b) **Type:** Case 1, rectangular → polar. $a=3>0$, so no $180^\circ$ fix.', (r'c=\sqrt{3^2+4^2}=5', r'\theta=\tan^{-1}\tfrac43=53.13^\circ')),
       S(r'(c) **Type:** Case 3, roots with $k=3$. Go polar first: $8j$ points straight up.', r'8j=8\angle90^\circ'),
       S(r'**Length:** the cube root of $8$.', r'8^{1/3}=2'),
       S(r'**First angle**, then **spacing** $360^\circ/3$.', (r'\dfrac{90^\circ}{3}=30^\circ', r'30^\circ,\quad 150^\circ,\quad 270^\circ')),
       S(r'Convert each to rectangular (Case 1): $a=2\cos\theta$, $b=2\sin\theta$.',
         (r'2\angle30^\circ=\sqrt3+j', r'2\angle150^\circ=-\sqrt3+j', r'2\angle270^\circ=-j2'))],
      r'(a) $3+j4$. (b) $5\angle53.13^\circ$. (c) $2\angle30^\circ=\sqrt3+j$, $\;2\angle150^\circ=-\sqrt3+j$, $\;2\angle270^\circ=-j2$. '
      r'Review: ' + link('Topic A', 'topic-a') + '.')

    PE(D, 'W2 · Classify, then use linearity',
      r'For each equation, give the order and say whether it is linear, homogeneous, constant-coefficient and autonomous.' '\n\n'
      r'(a) $\dfrac{d^2i}{dt^2}+\dfrac{R}{L}\dfrac{di}{dt}+\dfrac{1}{LC}\,i=0$ (the series RLC circuit of the Week 2 notes)' '\n\n'
      r'(b) $y\prime=y^2+t$' '\n\n'
      r'(c) $y\prime\prime+y=6\cos^2t$' '\n\n'
      r'(d) $y=e^{-t}$ solves $y\prime+2y=e^{-t}$. Without solving, give a solution of $y\prime+2y=5e^{-t}$.',
      [S(r'**Type:** classification → the five questions at the start of Topic B.'),
       S(r'(a) **Order:** $i\prime\prime$, so 2nd. **Linear:** $i$ only to the power 1. **Homogeneous:** right side $0$. '
         r'**Constant coefficients:** $\frac RL$, $\frac1{LC}$ are numbers. **Autonomous:** no $t$ anywhere.'),
       S(r'(b) **Order** 1. $y^2$ is not power 1, so **nonlinear**. The $t$ means **not** autonomous.'),
       S(r'(c) **Order** 2, linear, numbers in front. Right side $\neq0$: **not** homogeneous. $\cos^2t$ has $t$: not autonomous.'),
       S(r'(d) **Linearity:** multiply $y$ by $5$ and the whole left side is multiplied by $5$. Check:',
         r'(5e^{-t})\prime+2(5e^{-t})=-5e^{-t}+10e^{-t}=5e^{-t}\ \checkmark')],
      r'(a) 2nd order, linear, homogeneous, constant-coefficient, autonomous. (b) 1st order, nonlinear, not autonomous. '
      r'(c) 2nd order, linear, not homogeneous, constant-coefficient, not autonomous. (d) $y=5e^{-t}$. '
      r'Review: ' + link('Topic B', 'topic-b') + '.')

    PE(D, 'W3–W4 · Name the type, then solve · like lecture Examples 3.3, 3.1 and 4.1',
      r'Name the type of each equation, then solve it.' '\n\n'
      r'(a) $\dfrac{dy}{dt}=\dfrac{2t+2ty^2}{y+t^2y}$, $\;y(0)=1$' '\n\n'
      r'(b) $\dfrac{dy}{dt}+\dfrac{6y}{3t+2}=4$, $\;y(0)=0$' '\n\n'
      r'(c) $(2t+y\cos t)\,dt+(\sin t+2y)\,dy=0$, $\;y(0)=1$',
      [S(r'(a) **Type:** factor top and bottom → a $t$-part times a $y$-part → B1. **Write:**', r'\dfrac{dy}{dt}=\dfrac{2t}{1+t^2}\cdot\dfrac{1+y^2}{y}'),
       S(r'**Separate.**', r'\dfrac{y}{1+y^2}\,dy=\dfrac{2t}{1+t^2}\,dt'),
       S(r'**Integrate:** both are “top = derivative of bottom” (the left one is half).', r'\tfrac12\ln(1+y^2)=\ln(1+t^2)+C'),
       S(r'**Solve for $y$:** multiply by $2$, raise $e$ to both sides ($e^{2C}$ is a new $C$).', r'1+y^2=C\,(1+t^2)^2'),
       S(r'**Plug in** $y(0)=1$, then take the $+$ root ($y(0)>0$).', (r'1+1=C\cdot1\quad\Rightarrow\quad C=2', r'y=\sqrt{2(1+t^2)^2-1}')),
       S(r'(b) **Type:** linear → B2. **Write:** $y\prime$ is alone.', r'p=\dfrac{6}{3t+2},\qquad f=4'),
       S(r'**Find $\mu$:** $\int\frac{6}{3t+2}dt=2\ln(3t+2)$, and $e$, $\ln$ cancel.', r'\mu=(3t+2)^2'),
       S(r'**Multiply.**', r'\big[(3t+2)^2y\big]\prime=4(3t+2)^2'),
       S(r'**Integrate** with $u=3t+2$, $du=3\,dt$.', r'(3t+2)^2y=\tfrac49(3t+2)^3+C'),
       S(r'**Divide** by $(3t+2)^2$.', r'y=\tfrac49(3t+2)+\dfrac{C}{(3t+2)^2}'),
       S(r'**Plug in** $y(0)=0$.', r'0=\tfrac89+\dfrac C4\quad\Rightarrow\quad C=-\tfrac{32}{9}'),
       S(r'(c) **Type:** $dt$, $dy$ form → B3. **Write.**', r'M=2t+y\cos t,\qquad N=\sin t+2y'),
       S(r'**Test.**', r'M_y=\cos t,\qquad N_t=\cos t\quad\checkmark'),
       S(r'**Integrate $M$ in $t$** ($y$ is a number).', r'U=t^2+y\sin t+h(y)'),
       S(r'**Match $N$.**', r'U_y=\sin t+h\prime=\sin t+2y\quad\Rightarrow\quad h=y^2'),
       S(r'**Answer**, then **plug in** $t=0$, $y=1$: $0+0+1=C$.', r't^2+y\sin t+y^2=1')],
      r'(a) B1: $y=\sqrt{2(1+t^2)^2-1}$. (b) B2: $y=\frac49(3t+2)-\dfrac{32}{9(3t+2)^2}$. (c) B3: $t^2+y\sin t+y^2=1$. '
      r'Review: ' + link('B1', 'b1') + ', ' + link('B2', 'b2') + ', ' + link('B3', 'b3') + '.',
      diff='intermediate')

    PE(D, 'W4 · Not exact: find the factor, then solve · like Pre-tutorial 4',
      r'Consider $(3ty+y^2)\,dt+(t^2+ty)\,dy=0$ with $y(1)=1$. (a) Show it is not exact. (b) Find an integrating factor. (c) Solve.',
      [S(r'**Type:** $dt$, $dy$ form → test (B3). **Write.**', r'M=3ty+y^2,\qquad N=t^2+ty'),
       S(r'(a) **Test:** they don’t match → B4.', r'M_y=3t+2y,\qquad N_t=2t+y'),
       S(r'(b) **Find $\mu$:** try Case 1. Factor the bottom, $N=t(t+y)$: the $(t+y)$ cancels, only $t$ is left.',
         (r'\dfrac{M_y-N_t}{N}=\dfrac{t+y}{t(t+y)}=\dfrac1t', r'\mu=e^{\int\frac1t\,dt}=t')),
       S(r'**Multiply** by $t$.', r'(3t^2y+ty^2)\,dt+(t^3+t^2y)\,dy=0'),
       S(r'**Re-test.**', r'M_y=3t^2+2ty,\qquad N_t=3t^2+2ty\quad\checkmark'),
       S(r'(c) **Integrate $M$ in $t$.**', r'U=t^3y+\tfrac12t^2y^2+h(y)'),
       S(r'**Match $N$:** $U_y=t^3+t^2y+h\prime$ must equal $t^3+t^2y$.', r'h\prime=0'),
       S(r'**Answer**, then **plug in** $t=1$, $y=1$: $1+\tfrac12=C$. Multiply by $2$.', r'2t^3y+t^2y^2=3')],
      r'(a) $M_y=3t+2y\neq2t+y=N_t$. (b) $\mu=t$. (c) $2t^3y+t^2y^2=3$. '
      r'If a ratio seems to have both letters, factor before giving up. Review: ' + link('B4', 'b4') + '.',
      diff='intermediate')

    PE(D, 'W3 + W5 · Is the solution guaranteed?',
      r'(a) For $\dfrac{dy}{dt}=3y^{2/3}$, does the theorem guarantee exactly one solution through (i) $(1,8)$, (ii) $(0,0)$? '
      r'Then check that $y=0$ and $y=t^3$ both solve it. What does that say about $(0,0)$?' '\n\n'
      r'(b) Without solving, find the largest interval on which $(t^2-9)\,y\prime\prime+t\,y\prime+y=\dfrac1t$, $\;y(1)=0$, $y\prime(1)=2$, has exactly one solution.',
      [S(r'(a) **Type:** exactly one solution, first order → C1. **Write.**', r'F=3y^{2/3}'),
       S(r'**Differentiate** in $y$.', r'F_y=2y^{-1/3}=\dfrac{2}{y^{1/3}}'),
       S(r'**Find where it breaks:** $F$ is fine everywhere. $F_y$ divides by $y^{1/3}$.', r'y=0'),
       S(r'**Check the points:** (i) $y_0=8$ is off the line → exactly one. (ii) $y_0=0$ is on it → no guarantee.'),
       S(r'Both pass through $(0,0)$ and solve it, so there really are two solutions there.', r'y=0:\ 0=0\ \checkmark\qquad y=t^3:\ 3t^2=3(t^3)^{2/3}\ \checkmark'),
       S(r'(b) **Type:** interval, second-order linear → C2, Case 1. **Write:** divide by $t^2-9$.', r'p=\dfrac{t}{t^2-9},\quad q=\dfrac{1}{t^2-9},\quad f=\dfrac{1}{t(t^2-9)}'),
       S(r'**Find where they break:** the bottoms are $0$ at $t=-3,\,0,\,3$.'),
       S(r'**Pick the piece** containing $t_0=1$.', r'(0,\,3)')],
      r'(a) (i) Yes. (ii) No guarantee, and in fact two solutions ($y=0$, $y=t^3$) pass through $(0,0)$. (b) $(0,3)$. '
      r'Review: ' + link('C1', 'c1') + ', ' + link('C2', 'c2') + '.',
      diff='intermediate')

    PE(D, 'W2 · RC step response, and a current that jumps · like Pre-tutorial 2',
      r'Before $t=0$ the switch is open and the capacitor holds $v=2\,\mathrm{V}$. The switch closes at $t=0$. '
      r'(a) Write the ODE for $v$ for $t\ge0$. (b) Find $v(t)$. (c) Find $i_C$ just before and just after the switch closes.' '\n\n' + sch(RC_STEP),
      [S(r'**Type:** one capacitor and a DC source after the switch → D1, step response. Solve for $v$ (it can’t jump).'),
       S(r'(a) **After:** KCL at the top node: the source current splits into $R$ and $C$. Divide by $C=5\times10^{-6}$.',
         (r'C\dfrac{dv}{dt}+\dfrac{v}{R}=I_s', r'\dfrac{dv}{dt}+100\,v=600')),
       S(r'(b) **Before:** given.', r'v(0^-)=2\,\mathrm{V}'),
       S(r'**Carry across:** a capacitor voltage can’t jump.', r'x_0=v(0^+)=2\,\mathrm{V}'),
       S(r'**After** (final value): long after, $C$ is a gap, so all of $I_s$ goes through $R$.', r'x_f=RI_s=2000\times0.003=6\,\mathrm{V}'),
       S(r'**After** (time constant): the current source is off (a gap), so $C$ sees just $R$.', r'\tau=RC=2000\times5\times10^{-6}=0.01\,\mathrm{s}'),
       S(r'**Plug in.**', r'v=6+(2-6)e^{-t/0.01}=6-4e^{-100t}\ \mathrm{V}'),
       S(r'(c) **Before:** the switch is open, so no current reaches $C$.', r'i_C(0^-)=0'),
       S(r'**Carry across:** $v=2\,\mathrm{V}$ still, so $R$ takes $\frac{2}{2000}=1\,\mathrm{mA}$. KCL: $C$ gets the rest.', r'i_C(0^+)=3-1=2\,\mathrm{mA}'),
       S(r'**Check** with $i_C=C\,v\prime$ from (b): $v\prime(0)=400$.', r'i_C(0^+)=5\times10^{-6}\times400=2\,\mathrm{mA}\ \checkmark')],
      r'(a) $v\prime+100v=600$. (b) $v=6-4e^{-100t}\,\mathrm{V}$. (c) $0$ before, $2\,\mathrm{mA}$ after: the capacitor **current** jumps, its voltage doesn’t. '
      r'Review: ' + link('D1', 'd1') + '.')

    PE(D, 'W5 · Complex roots, then a repeated root',
      r'Solve (a) $y\prime\prime+4y\prime+13y=0$, and (b) $y\prime\prime+4y\prime+4y=0$, each with $y(0)=1$, $y\prime(0)=0$.',
      [S(r'(a) **Type:** numbers in front, right side $0$ → B5. **Write** the quadratic.', r's^2+4s+13=0'),
       S(r'**Solve** with the formula. Under the root: $16-52=-36<0$, so Case 3.', r's=\dfrac{-4\pm\sqrt{-36}}{2}=\dfrac{-4\pm j6}{2}=-2\pm j3'),
       S(r'**Pick:** Case 3, $\sigma=-2$, $\omega=3$.', r'y=e^{-2t}(c_1\cos3t+c_2\sin3t)'),
       S(r'**Differentiate** (product rule).', r'y\prime=-2e^{-2t}(c_1\cos3t+c_2\sin3t)+e^{-2t}(-3c_1\sin3t+3c_2\cos3t)'),
       S(r'**Plug in** $t=0$.', (r'y(0)=c_1=1', r'y\prime(0)=-2c_1+3c_2=0\quad\Rightarrow\quad c_2=\tfrac23')),
       S(r'(b) **Type:** B5. **Write** and **solve:** a perfect square.', r's^2+4s+4=(s+2)^2=0\quad\Rightarrow\quad s=-2\ \text{(twice)}'),
       S(r'**Pick:** Case 2.', r'y=(c_1+c_2t)\,e^{-2t}'),
       S(r'**Differentiate** (product rule).', r'y\prime=c_2e^{-2t}-2(c_1+c_2t)\,e^{-2t}'),
       S(r'**Plug in** $t=0$.', (r'y(0)=c_1=1', r'y\prime(0)=c_2-2c_1=0\quad\Rightarrow\quad c_2=2'))],
      r'(a) $y=e^{-2t}\big(\cos3t+\tfrac23\sin3t\big)$. (b) $y=(1+2t)e^{-2t}$. Review: ' + link('B5', 'b5') + '.')

    PE(D, 'W5 · Parallel RLC step response · lecture Example 5.2, plus a twist',
      r'The initial energy stored in the circuit is zero. At $t=0$ a DC current source of $24\,\mathrm{mA}$ is applied. '
      r'(a) Find $i_L(t)$ for $t\ge0$. (b) Twist: which $R$ would make the circuit critically damped? Find $i_L(t)$ for that $R$.' '\n\n' + sch(RLC_STEP),
      [S(r'**Type:** an $L$ and a $C$, all in parallel, with a DC source → D2, parallel step response. Solve for $i_L$ (it can’t jump).'),
       S(r'(a) **Before:** zero energy, so nothing is charged and no current flows.', r'i_L(0^-)=0,\qquad v_C(0^-)=0'),
       S(r'**Carry across:** both carry over. Slope: $L$ sits across $C$, so $v_L=v_C(0^+)=0$, and $i_L\prime=\frac{v_L}{L}$.', r'i_L(0^+)=0,\qquad i_L\prime(0^+)=\dfrac{0}{L}=0'),
       S(r'**After:** parallel, so $\alpha=\frac{1}{2RC}$. Use H and F.', r'\alpha=\dfrac{1}{2(400)(25\times10^{-9})}=50000,\qquad \omega_0=\dfrac{1}{\sqrt{(0.025)(25\times10^{-9})}}=40000'),
       S(r'**After** (final value): long after, $L$ is a wire and takes all of the source.', r'I_f=24\,\mathrm{mA}'),
       S(r'**Pick:** $\alpha>\omega_0$, overdamped (B5 Case 1). Roots:', (r's=-50000\pm\sqrt{50000^2-40000^2}=-50000\pm30000', r'i_L=24+c_1e^{-20000t}+c_2e^{-80000t}\ \mathrm{mA}')),
       S(r'**Plug in** $t=0$: the value, then the slope (each root times its constant).', (r'24+c_1+c_2=0', r'-20000c_1-80000c_2=0')),
       S(r'The second gives $c_1=-4c_2$. Put it in the first: $-3c_2=-24$.', r'c_2=8,\qquad c_1=-32'),
       S(r'(b) **Critical damping** means $\alpha=\omega_0=40000$. Solve $\frac{1}{2RC}=40000$.', r'R=\dfrac{1}{2(40000)(25\times10^{-9})}=500\,\Omega'),
       S(r'**Pick:** Case 2, root $-40000$ twice. Same final value.', r'i_L=24+(c_1+c_2t)\,e^{-40000t}\ \mathrm{mA}'),
       S(r'**Plug in** $t=0$: value, then slope ($c_2-40000c_1$ from the product rule).', (r'24+c_1=0\quad\Rightarrow\quad c_1=-24', r'c_2-40000c_1=0\quad\Rightarrow\quad c_2=-960000')),
       S(r'**Check:** $t\to\infty$ gives $24\,\mathrm{mA}$ in both ✓.')],
      r'(a) $i_L=24-32e^{-20000t}+8e^{-80000t}\ \mathrm{mA}$ (the lecture’s answer). (b) $R=500\,\Omega$: $i_L=24-24(1+40000t)e^{-40000t}\ \mathrm{mA}$. '
      r'Review: ' + link('D2', 'd2') + '.',
      diff='intermediate', cites=D.cite('W5', 5, 6))

    PE(D, 'W6 · The tutorial problem without the hints · Pre-tutorial 5',
      r'(a) Solve $y\prime\prime+y=6\cos^2t$, $\;y(0)=0$, $\;y(\pi/2)=0$. This time the forms of $y_c$ and $y_p$ are **not** given.' '\n\n'
      r'(b) For $y\prime\prime-4y=e^{2t}+t$, write the form of $y_p$ and find it.',
      [S(r'(a) **Type:** numbers in front, right side not $0$ → B6. **Solve $y_c$:** $s^2+1=0$, $s=\pm j$ (B5 Case 3, $\sigma=0$, $\omega=1$).', r'y_c=c_1\sin t+c_2\cos t'),
       S(r'No case fits $\cos^2t$, so use the identity first.', r'6\cos^2t=3+3\cos2t'),
       S(r'**Guess $y_p$:** constant → $A$ (Case 1); $\cos2t$ → both (Case 3). None is in $y_c$.', r'y_p=A+B\cos2t+D\sin2t'),
       S(r'Differentiate twice: each $\cos2t$, $\sin2t$ is multiplied by $-4$.', r'y_p\prime\prime=-4B\cos2t-4D\sin2t'),
       S(r'**Plug in** to $y_p\prime\prime+y_p$ and collect.', r'A-3B\cos2t-3D\sin2t=3+3\cos2t'),
       S(r'**Match** constants, $\cos2t$, $\sin2t$.', r'A=3,\qquad B=-1,\qquad D=0'),
       S(r'**Add.**', r'y=3-\cos2t+c_1\sin t+c_2\cos t'),
       S(r'**Plug in** $y(0)=0$: $\sin0=0$, $\cos0=1$.', r'3-1+c_2=0\quad\Rightarrow\quad c_2=-2'),
       S(r'**Plug in** $y(\pi/2)=0$: $\cos\pi=-1$, $\sin\frac\pi2=1$, $\cos\frac\pi2=0$.', r'3+1+c_1=0\quad\Rightarrow\quad c_1=-4'),
       S(r'(b) **Solve $y_c$:** $s^2-4=0$, $s=\pm2$ (B5 Case 1).', r'y_c=c_1e^{2t}+c_2e^{-2t}'),
       S(r'**Guess $y_p$:** $e^{2t}$ is in $y_c$ → Case 4, times $t$. The $t$ → Case 1, $Bt+D$.', r'y_p=Ate^{2t}+Bt+D'),
       S(r'Differentiate twice (product rule on $te^{2t}$).', r'y_p\prime\prime=A(4+4t)e^{2t}'),
       S(r'**Plug in** to $y_p\prime\prime-4y_p$. The $te^{2t}$ terms cancel.', r'4Ae^{2t}-4Bt-4D=e^{2t}+t'),
       S(r'**Match** $e^{2t}$, $t$, constants.', r'A=\tfrac14,\qquad B=-\tfrac14,\qquad D=0')],
      r'(a) $y=3-\cos2t-4\sin t-2\cos t$. (b) $y_p=\frac14te^{2t}-\frac14t$. Review: ' + link('B6', 'b6') + '.',
      diff='intermediate', cites=D.cite('T5', 1))

    PE(D, 'W6 · Reduction of order · like lecture Example 6.1',
      r'Given that $y_1=t$ solves $t^2y\prime\prime+t\,y\prime-y=0$ for $t>0$, find the general solution.',
      [S(r'**Type:** $t$ in front, one solution given → B7. **Write** (check $y_1$): $0+t-t=0$ ✓.'),
       S(r'**Substitute** $y=tv$ (product rule).', (r'y\prime=v+tv\prime', r'y\prime\prime=2v\prime+tv\prime\prime')),
       S(r'**Plug in and collect.** The plain-$v$ terms cancel ($tv-tv$).', (r't^2(2v\prime+tv\prime\prime)+t(v+tv\prime)-tv=0', r't^3v\prime\prime+3t^2v\prime=0')),
       S(r'**Solve for $z$:** set $z=v\prime$, divide by $t^3$, separate (B1).', (r'\dfrac{dz}{z}=-\dfrac3t\,dt', r'z=\dfrac{c_1}{t^3}')),
       S(r'**Integrate** (power rule).', r'v=-\dfrac{c_1}{2t^2}+c_2'),
       S(r'**Multiply back** by $t$. $-\frac{c_1}{2}$ is just another constant: call it $c_1$.', r'y=c_2\,t+\dfrac{c_1}{t}')],
      r'$y=c_1\dfrac1t+c_2t$. Check $y=\frac1t$: $t^2\cdot\frac{2}{t^3}+t\cdot\left(-\frac{1}{t^2}\right)-\frac1t=0$ ✓. Review: ' + link('B7', 'b7') + '.',
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
