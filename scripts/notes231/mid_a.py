"""Topic A: complex numbers (Week 1)."""
import sympy as sp

from midlib import CARD, P, S, TAGS, link, zero


def build(D):
    W1 = lambda *p: D.cite('W1', *p)
    D.H('Topic A: Complex numbers', cites=W1(1, 3, 4, 5))
    TAGS(D, (1, 1), (1, 2))
    D.P(r'**Use this when** you have to convert, multiply, divide, raise to a power, or take roots of a complex number. '
        r'(They also show up inside ' + link('B5', 'b5') + r' Case 3: $\sqrt{-36}=j6$.)')
    D.P(r'**The move: every complex number has two forms.** Pick the one that makes the job easy.')
    D.EQ(r'z=a+jb\quad=\quad c\angle\theta\quad(=c\,e^{j\theta})')
    D.L([r'$a+jb$ (**rectangular**): $a$ = how far right, $b$ = how far up. Easy for **adding**.',
         r'$c\angle\theta$ (**polar**): $c$ = the length, $\theta$ = the angle from the positive real axis. Easy for **multiplying, dividing, powers, roots**.',
         r'$j=\sqrt{-1}$, so $j^2=-1$. (This course writes $j$, not $i$.)'])
    D.P('**Short example:**')
    D.EQ(r'3+j4=5\angle53.13^\circ')
    D.WHY('Why does multiplying add the angles?',
          r'Write both as exponentials and use $e^Ae^B=e^{A+B}$:'
          '\n\n$$\n' r'c_1e^{j\theta_1}\cdot c_2e^{j\theta_2}=c_1c_2\,e^{j(\theta_1+\theta_2)}' '\n$$\n\n'
          r'The two forms are linked by Euler’s identity, $e^{j\theta}=\cos\theta+j\sin\theta$. '
          r'The lecture uses it for trig identities: expand $e^{jA}e^{jB}=e^{j(A+B)}$, and the real parts give $\cos(A+B)=\cos A\cos B-\sin A\sin B$.')

    D.H('Case 1: convert between the forms', level=3)
    D.P(r'**Polar → rectangular** (the arrow is the long side of a right triangle):')
    D.EQ(r'a=c\cos\theta,\qquad b=c\sin\theta')
    D.EQ(r'2\angle30^\circ=2\cos30^\circ+j\,2\sin30^\circ=\sqrt3+j')
    D.P(r'**Rectangular → polar** (Pythagoras, then $\tan^{-1}$):')
    D.EQ(r'c=\sqrt{a^2+b^2},\qquad \theta=\tan^{-1}\!\left(\dfrac{b}{a}\right)')
    D.EQ(r'3+j4:\quad c=\sqrt{9+16}=5,\quad \theta=\tan^{-1}\tfrac43=53.13^\circ')
    D.CO('warning', r'**The quadrant trap.** The calculator’s $\tan^{-1}$ only gives arrows pointing right. If $a<0$ (pointing left), **add $180^\circ$**. '
         r'Example: $-1+j$. The calculator says $-45^\circ$, but the real angle is $-45^\circ+180^\circ=135^\circ$.')

    D.H('Case 2: multiply, divide, powers', level=3)
    D.P(r'Go **polar**. Lengths multiply/divide, angles add/subtract:')
    D.EQ(r'2\angle30^\circ\times3\angle40^\circ=6\angle70^\circ')
    D.EQ(r'\dfrac{6\angle70^\circ}{3\angle40^\circ}=2\angle30^\circ')
    D.P(r'**Power** (de Moivre): length to the power, angle times the power:')
    D.EQ(r'(2\angle30^\circ)^3=8\angle90^\circ')
    D.P(r'**Dividing in rectangular?** Multiply top and bottom by the **conjugate** of the bottom ($a+jb\to a-jb$). The bottom becomes $a^2+b^2$, a plain number:')
    D.EQ(r'\dfrac{1}{1+j}=\dfrac{1-j}{(1+j)(1-j)}=\dfrac{1-j}{2}')
    D.P(r'Adding or subtracting? Stay rectangular: $(1+j2)+(3-j5)=4-j3$.')
    CARD(D, r'Powers of $j$: $\;j^2=-1,\ \ j^3=-j,\ \ j^4=1,\ \ \dfrac1j=-j$',
         [(r'They repeat every four.', r'j^3=j^2\cdot j=-j,\qquad j^4=(j^2)^2=1'),
          (r'Dividing by $j$: multiply top and bottom by $j$.', r'\dfrac1j=\dfrac{j}{j\cdot j}=\dfrac{j}{-1}=-j')])

    D.H('Case 3: roots (k answers)', level=3)
    D.P(r'A $k$-th root has **$k$ answers**, all the same length, evenly spaced round a circle. Go polar, then:')
    D.EQ(r'z^{1/k}=c^{1/k}\angle\dfrac{\theta+360^\circ\ell}{k},\qquad \ell=0,1,\dots,k-1')
    D.L([r'**Length:** $c^{1/k}$ for all of them.',
         r'**First angle:** $\theta/k$.',
         r'**Spacing:** add $360^\circ/k$ each time.'])
    D.P('**Short example:** the square roots of $4\\angle60^\\circ$:')
    D.EQ(r'\sqrt4=2,\quad \dfrac{60^\circ}{2}=30^\circ,\quad +\dfrac{360^\circ}{2}=180^\circ\quad\Longrightarrow\quad 2\angle30^\circ,\ \ 2\angle210^\circ')
    CARD(D, r'Full example (lecture 1.2): the fourth roots of $\;z=81e^{j60^\circ}$',
         [(r'Already polar: $c=81$, $\theta=60^\circ$, $k=4$.', r'z=81\angle60^\circ'),
          (r'**Length:** $81^{1/4}$.', r'81^{1/4}=3'),
          (r'**First angle.**', r'\dfrac{60^\circ}{4}=15^\circ'),
          (r'**Spacing:** keep adding $360^\circ/4$.', r'\dfrac{360^\circ}{4}=90^\circ'),
          (r'List all four.', r'3\angle15^\circ,\quad 3\angle105^\circ,\quad 3\angle195^\circ,\quad 3\angle285^\circ')],
         None)
    D.WHY('Why $k$ answers?',
          r'$\theta$ and $\theta+360^\circ$ are the same arrow. But after you divide by $k$, they point different ways. Each extra $360^\circ$ gives a new root, until you come back round after $k$ of them.')
    D.GRAPH(r'''
    title "Drag $z$, change $k$: the $k$ roots sit evenly on one circle"
    x -3 3 label="Re"
    y -3 3 label="Im"
    equal
    drag Z 0 2.5 label="$z$" color=1
    slider k 2 6 3 step=1 label="$k$"
    let c "hypot(Z_x,Z_y)"
    let th "atan2(Z_y,Z_x)"
    let r "c^(1/k)"
    arrow "Z_x" "Z_y" color=1
    circle "0" "0" "r" color=0 dash
    point "r*cos(th/k)" "r*sin(th/k)" label="the $k$ roots of $z$" color=2
    point "r*cos((th+2*pi)/k)" "r*sin((th+2*pi)/k)" color=2
    point "if(k>2, r*cos((th+4*pi)/k), 99)" "if(k>2, r*sin((th+4*pi)/k), 99)" color=2
    point "if(k>3, r*cos((th+6*pi)/k), 99)" "if(k>3, r*sin((th+6*pi)/k), 99)" color=2
    point "if(k>4, r*cos((th+8*pi)/k), 99)" "if(k>4, r*sin((th+8*pi)/k), 99)" color=2
    point "if(k>5, r*cos((th+10*pi)/k), 99)" "if(k>5, r*sin((th+10*pi)/k), 99)" color=2
    readout "$|z|$" "c"
    readout "$\angle z$" "deg(th)" unit="°"
    readout "root magnitude" "r"
    caption "Start: $z=2.5\angle90^\circ$, $k=3$. The roots have length $2.5^{1/3}$. The first is at $90^\circ/3=30^\circ$, the others $120^\circ$ apart."
    ''', intro='**What do the roots look like?**')
    D.CO('tip', r'**Casio 991 check:** complex mode does $+,-,\times,\div$ and can show $r\angle\theta$. Use it to check, but write the steps: the marks are for the working.')

    D.H('Practice: A', level=3)
    P(D, 'W1 · Convert, watching the quadrant',
      r'Write (a) $-3+j4$ and (b) $-3-j4$ in polar form.',
      [S(r'**Type:** rectangular → polar. Both have $a<0$ (they point left), so the $180^\circ$ fix applies.'),
       S(r'**Length:** the same for both.', r'c=\sqrt{(-3)^2+4^2}=5'),
       S(r'**Angle (a):** the calculator gives $\tan^{-1}(4/{-3})=-53.13^\circ$. The arrow points up-left (quadrant II), so add $180^\circ$.', r'\theta=126.87^\circ'),
       S(r'**Angle (b):** the calculator gives $\tan^{-1}(-4/{-3})=53.13^\circ$. The arrow points down-left (quadrant III), so add $180^\circ$.', r'\theta=233.13^\circ\ \ (=-126.87^\circ)')],
      r'(a) $5\angle126.87^\circ$. (b) $5\angle233.13^\circ$, the same as $5\angle-126.87^\circ$.')
    P(D, 'W1 · Divide in rectangular form · lecture Example 1.1',
      r'Compute $\dfrac{80+j18}{8+j10}$. Give the answer in rectangular and polar form.',
      [S(r'**Type:** dividing two rectangular numbers. Multiply top and bottom by the conjugate of the bottom, $8-j10$.',
         r'\dfrac{(80+j18)(8-j10)}{(8+j10)(8-j10)}'),
       S(r'**Multiply out:** the bottom is $8^2+10^2=164$. On top, expand and use $j^2=-1$.', r'(640+180)+j(144-800)=820-j656'),
       S(r'**Divide** both parts by 164.', r'5-j4'),
       S(r'**Polar:** $a>0$, $b<0$ points down-right (quadrant IV), so the calculator angle is already right.', r'\sqrt{41}\angle-38.66^\circ')],
      r'$5-j4=\sqrt{41}\angle-38.66^\circ\approx6.40\angle-38.66^\circ$.', cites=W1(4))
    P(D, 'W1 · A high power',
      r'Compute $(1+j)^8$.',
      [S(r'**Type:** a power, so go polar first: $c=\sqrt2$, $\theta=45^\circ$.', r'1+j=\sqrt2\angle45^\circ'),
       S(r'**de Moivre:** length to the 8th, angle times 8.', r'(\sqrt2)^8\angle360^\circ=16\angle0^\circ')],
      r'$(1+j)^8=16$.', diff='intermediate')
    P(D, 'W1 · Cube roots of a negative number',
      r'Find all three cube roots of $-8$, in polar and rectangular form.',
      [S(r'**Type:** roots ($k=3$). Go polar first: $-8$ points straight left.', r'-8=8\angle180^\circ'),
       S(r'**Roots:** length $8^{1/3}=2$, first angle $180^\circ/3=60^\circ$, spacing $360^\circ/3=120^\circ$.', r'2\angle60^\circ,\quad 2\angle180^\circ,\quad 2\angle300^\circ'),
       S(r'**Rectangular:** $a=2\cos\theta$, $b=2\sin\theta$.', r'1+j\sqrt3,\quad -2,\quad 1-j\sqrt3')],
      r'$2\angle60^\circ=1+j\sqrt3$, $2\angle180^\circ=-2$, $2\angle300^\circ=1-j\sqrt3$. The real root $-2$ is only one of three.',
      diff='intermediate')
    P(D, 'W1 + W5 · The complex roots of a quadratic',
      r'Solve $s^2+4s+13=0$. (This is exactly the step you meet in ' + link('B5', 'b5') + '.)',
      [S(r'**Type:** a quadratic with $b^2-4ac<0$, so the roots are complex.', r's=\dfrac{-4\pm\sqrt{16-52}}{2}=\dfrac{-4\pm\sqrt{-36}}{2}'),
       S(r'**Root of a negative:** $\sqrt{-36}=\sqrt{36}\,\sqrt{-1}=j6$.', r's=\dfrac{-4\pm j6}{2}')],
      r'$s=-2\pm j3$: a conjugate pair (same real part, opposite imaginary parts).', diff='intermediate')


def verify():
    j = sp.I
    z = -3 + 4 * j
    assert abs(float(sp.deg(sp.arg(z))) - 126.8699) < 1e-3 and sp.Abs(z) == 5
    assert abs(float(sp.deg(sp.arg(-3 - 4 * j))) + 126.8699) < 1e-3
    zero((80 + 18 * j) / (8 + 10 * j) - (5 - 4 * j))
    assert abs(float(sp.deg(sp.arg(5 - 4 * j))) + 38.6598) < 1e-3
    zero(sp.expand((1 + j) ** 8) - 16)
    for r in (1 + sp.sqrt(3) * j, -2, 1 - sp.sqrt(3) * j):
        zero(sp.expand(r ** 3) + 8)
    for r in (-2 + 3 * j, -2 - 3 * j):
        zero(sp.expand(r ** 2 + 4 * r + 13))
    for ang in (15, 105, 195, 285):
        w = 3 * sp.exp(j * sp.pi * ang / 180)
        zero(sp.simplify(sp.expand(w ** 4) - 81 * sp.exp(j * sp.pi / 3)))
