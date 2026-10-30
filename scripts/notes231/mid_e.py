"""E: the final run. Every lecture example and tutorial problem (the ★ problems) in one list, by week, with the short
answers in a closed box per week. The prof reuses these on the midterm; the full solutions live in the sections."""
import sympy as sp

from midlib import first, implicit, link, second, t, y, zero

WEEKS = [
    ('Week 1', [link('Topic A', 'topic-a'), link('D1', 'd1')], [
        (r'**Ex 1.1** Compute $\dfrac{80+j18}{8+j10}$.', r'$5-j4$'),
        (r'**Ex 1.2** The four fourth roots of $81e^{j60^\circ}$.', r'$3e^{j15^\circ},\ 3e^{j105^\circ},\ 3e^{j195^\circ},\ 3e^{j285^\circ}$'),
        (r'**§2** Get $\cos(A+B)$ and $\sin(A+B)$ from $e^{jA}e^{jB}=e^{j(A+B)}$.', r'Expand both sides with Euler, match real parts and $j$ parts.'),
        (r'**Pre-tut 1** RL natural response: $L=8\,\mathrm{mH}$, $R=4\,\Omega$, $I_s=4\,\mathrm{A}$. Find $i(t)$ and sketch.', r'$\tau=2\,\mathrm{ms}$, $i=4e^{-500t}\,\mathrm{A}$'),
    ]),
    ('Week 2', [link('Topic B', 'topic-b'), link('D1', 'd1')], [
        (r'**Ex 2.1** Is $t^3y\prime\prime+e^ty\prime+y=0$ linear? Order? Homogeneous? Constant coefficients?', r'Linear, 2nd order, homogeneous, **not** constant-coefficient.'),
        (r'**§4** RC natural response: $v(0)=V_s$, then $C$ alone with $R$. Find $v(t)$.', r'$v=V_se^{-t/RC}$'),
        (r'**§5** RC step response: $I_s$, $R$, $C$ in parallel, $v(0)=V_0$. Find $v(t)$.', r'$v=RI_s+(V_0-RI_s)e^{-t/RC}$'),
        (r'**Pre-tut 2** Same circuit, $V_0=0$, $I_s=2\,\mathrm{A}$, $R=1\,\mathrm{k\Omega}$: $i_C(0^-)$ and $i_C(0^+)$?', r'$0$ and $2\,\mathrm{A}$: the current jumps, the voltage doesn’t.'),
    ]),
    ('Week 3', [link('B1', 'b1'), link('B2', 'b2'), link('Topic C', 'topic-c')], [
        (r'**Ex 3.1** $y\prime+\dfrac{10y}{2t+5}=10$, $y(0)=0$.', r'$\mu=(2t+5)^5$, $\;y=\tfrac56(2t+5)-\dfrac{5^7}{6(2t+5)^5}$'),
        (r'**§1.1** RL circuit: $2\frac{di}{dt}+10i=100$, $i(0)=0$. Integrating factor, then again by separating.', r'$i=10(1-e^{-5t})\,\mathrm{A}$'),
        (r'**Ex 3.2** $\dfrac{dy}{dt}=\dfrac{y^2}{t^3}$.', r'$\dfrac1y=\dfrac{1}{2t^2}-C$ (and $y=0$)'),
        (r'**Ex 3.3** $\dfrac{dy}{dt}=\dfrac{3t+ty^2}{y+t^2y}$, $y(1)=3$.', r'$y^2+3=6(t^2+1)$'),
        (r'**Ex 3.4** $y\,dt+(t^3y^2+t^3)\,dy=0$.', r'$y^2+2\ln|y|-t^{-2}=C$'),
        (r'**Pre-tut 3(a)** $\dfrac{dy}{dt}=-\dfrac ty$, $y(1)=2$.', r'$t^2+y^2=5$, $\;y=\sqrt{5-t^2}$'),
        (r'**Pre-tut 3(b)** $3t(y^2+1)\,dt+y(t^2+2)\,dy=0$.', r'$(t^2+2)^3(y^2+1)=C$'),
        (r'**Pre-tut 3(c)** $\dfrac{dy}{dt}=8ty+3y$.', r'$y=Ce^{4t^2+3t}$'),
        (r'**Theorem 3.2** When is there exactly one solution of $y\prime=F(t,y)$ through a point?', r'$F$ and $\partial F/\partial y$ continuous (finite) near the point. Sufficient, not necessary.'),
    ]),
    ('Week 4', [link('B3', 'b3'), link('B4', 'b4')], [
        (r'**Ex 4.1** $(2ty+3t^2)\,dt+t^2\,dy=0$.', r'$t^2y+t^3=C$'),
        (r'**(a)** $3t\,dt+4y\,dy=0$.', r'$3t^2+4y^2=C$'),
        (r'**(b)** $y\prime=\dfrac{t-y}{t+y}$.', r'$t^2-2ty-y^2=C$'),
        (r'**(c)** $2ty\,y\prime=t^2-y^2$.', r'$t^3-3ty^2=C$'),
        (r'**(d)** $y\prime=\dfrac{t}{t+y}$: exact?', r'No: $M_y=0\neq-1=N_t$.'),
        (r'**(e) + Pre-tut 4** $y\,dt+(3+3t-y)\,dy=0$: find $\mu$, then solve.', r'$\mu=y^2$, $\;ty^3+y^3-\tfrac14y^4=C$'),
    ]),
    ('Week 5', [link('B5', 'b5'), link('D2', 'd2'), link('Topic C', 'topic-c')], [
        (r'**§1** Parallel RLC: the characteristic equation and its three cases.', r'$s^2+\frac{1}{RC}s+\frac{1}{LC}=0$; $\alpha=\frac1{2RC}$ vs $\omega_0=\frac1{\sqrt{LC}}$: over / critical / under.'),
        (r'**Ex 5.2** Zero initial energy, $24\,\mathrm{mA}$ switched on, $400\,\Omega$, $25\,\mathrm{nF}$, $25\,\mathrm{mH}$. Find $i_L(t)$.', r'$i_L=24-32e^{-20\,000t}+8e^{-80\,000t}\ \mathrm{mA}$'),
        (r'**Theorem 5.1** When does a linear $n$-th order ODE have exactly one solution?', r'Coefficients and right side continuous on the interval, and the top coefficient $a_0(t)\neq0$ there.'),
    ]),
    ('Week 6', [link('B6', 'b6'), link('B7', 'b7')], [
        (r'**Lecture** $y\prime\prime-ty\prime+y=0$, $y_1=t$. Find the general solution.', r'$y=c_2t+c_1t\displaystyle\int\frac{e^{t^2/2}}{t^2}\,dt$'),
        (r'**Pre-tut 5 = tutorial** $\ddot y+y=6\cos^2t$, $y(0)=0$, $y(\pi/2)=0$.', r'$y=3-\cos2t-4\sin t-2\cos t$'),
    ]),
]


def build(D):
    D.H('Topic E: Final run — every ★ problem')
    D.P(r'**The last hour.** These are all the prof’s own problems. For each one: cover the answer, do it on paper, then open the box and check. '
        r'Wrong or slow? Click the section link and redo it there (the full solutions are there, same steps).')
    for week, links, items in WEEKS:
        D.P(f'**{week}** · ' + ' · '.join(links))
        D.L([q for q, _ in items], ordered=True)
        D.BOX(f'Answers: {week}', '\n'.join(f'{i}. {a}' for i, (_, a) in enumerate(items, 1)))


def verify():
    zero((80 + 18 * sp.I) / (8 + 10 * sp.I) - (5 - 4 * sp.I))
    C = sp.symbols('C')
    ys = sp.Rational(5, 6) * (2 * t + 5) - 5 ** 7 / (6 * (2 * t + 5) ** 5)
    first(ys, 10 - 10 * y / (2 * t + 5), (0, 0))
    first(10 - 10 * sp.exp(-5 * t), 50 - 5 * y, (0, 0))
    first(1 / (1 / (2 * t ** 2) - C), y ** 2 / t ** 3)
    assert implicit((y ** 2 + 3) / (t ** 2 + 1), t * (3 + y ** 2) / (y * (1 + t ** 2)), (1, 3)) == 6
    implicit(y ** 2 + 2 * sp.log(y) - t ** -2, -y / (t ** 3 * y ** 2 + t ** 3))
    first(sp.sqrt(5 - t ** 2), -t / y, (1, 2))
    implicit((t ** 2 + 2) ** 3 * (y ** 2 + 1), -3 * t * (y ** 2 + 1) / (y * (t ** 2 + 2)))
    first(C * sp.exp(4 * t ** 2 + 3 * t), 8 * t * y + 3 * y)
    implicit(t ** 2 * y + t ** 3, -(2 * t * y + 3 * t ** 2) / t ** 2)
    implicit(3 * t ** 2 + 4 * y ** 2, -3 * t / (4 * y))
    implicit(t ** 2 - 2 * t * y - y ** 2, (t - y) / (t + y))
    implicit(t ** 3 - 3 * t * y ** 2, (t ** 2 - y ** 2) / (2 * t * y))
    implicit(t * y ** 3 + y ** 3 - y ** 4 / 4, -y / (3 + 3 * t - y))
    L, Cc = sp.Rational(25, 1000), sp.Rational(25, 10 ** 9)
    second(24 - 32 * sp.exp(-20000 * t) + 8 * sp.exp(-80000 * t), 1, 1 / (400 * Cc), 1 / (L * Cc), 24 / (L * Cc), initial=(0, 0, 0))
    sol = 3 - sp.cos(2 * t) - 4 * sp.sin(t) - 2 * sp.cos(t)
    second(sol, 1, 0, 1, 6 * sp.cos(t) ** 2)
    zero(sol.subs(t, 0))
    zero(sol.subs(t, sp.pi / 2))
