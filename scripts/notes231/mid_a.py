"""Topic A: complex numbers (Week 1)."""
import sympy as sp

from midlib import P, S, TAGS, link, zero


def build(D):
    W1 = lambda *p: D.cite('W1', *p)
    D.H('Topic A: Complex numbers', cites=W1(1, 3, 4, 5))
    TAGS(D, (1, 1), (1, 2))
    D.P('Complex numbers show up in two places on the midterm:')
    D.L(['**On their own:** convert, divide, raise to a power, take roots.',
         r'**Inside ' + link('B5', 'b5') + r':** when a characteristic equation has no real roots, you need things like $\sqrt{-36}=j6$.'])

    D.P('**One number, two ways to write it.** Think of a complex number as an arrow from the origin. '
        'You can say where its tip is (how far right, how far up), or how long it is and which way it points:')
    D.EQ(r'z=a+jb=c\,e^{j\theta}=c\angle\theta')
    D.L([r'$a=\mathrm{Re}\{z\}$ = the **real part**: how far right',
         r'$b=\mathrm{Im}\{z\}$ = the **imaginary part**: how far up',
         r'$c=|z|$ = the **magnitude**: how long the arrow is',
         r'$\theta=\angle z$ = the **angle**: measured from the positive real axis, counter-clockwise',
         r'$j=\sqrt{-1}$, so $j^2=-1$ (this course writes $j$, not $i$)'])
    D.P(r'Example: $3+j4$ is 3 right and 4 up. Its length is $c=\sqrt{9+16}=5$ and its angle is $\theta=\tan^{-1}(4/3)=53.13^\circ$, '
        r'so $3+j4=5\angle53.13^\circ$.')
    D.P('Why two forms? Adding is easy in $a+jb$. Multiplying, dividing and powers are easy in $c\\angle\\theta$.')

    D.P('**Polar → rectangular.** The arrow is the long side of a right triangle, so use cos and sin:')
    D.EQ(r'a=c\cos\theta,\quad b=c\sin\theta')
    D.P(r'Example: $2\angle30^\circ=2\cos30^\circ+j\,2\sin30^\circ=\sqrt3+j$.')
    D.P('**Rectangular → polar.** Pythagoras gives the length, $\\tan^{-1}$ gives the angle:')
    D.EQ(r'c=\sqrt{a^2+b^2},\quad \theta=\tan^{-1}\!\left(\dfrac{b}{a}\right)')
    D.P(r'Example: the $3+j4=5\angle53.13^\circ$ above. But watch the quadrant:')
    D.CO('warning', r'**The quadrant trap.** The calculator’s $\tan^{-1}$ only gives angles between $-90^\circ$ and $90^\circ$, i.e. arrows pointing right. '
         r'If $a<0$, your arrow points left, so **add $180^\circ$** to what the calculator says. '
         r'Example: $-1+j$ points up-left. The calculator gives $\tan^{-1}(1/{-1})=-45^\circ$, but the real angle is $-45^\circ+180^\circ=135^\circ$.')

    D.P('**Arithmetic: pick the form that makes the job easy.**')
    D.L([r'**Add or subtract → rectangular.** Add the real parts, add the imaginary parts: $(1+j2)+(3-j5)=4-j3$.',
         r'**Multiply → polar.** Multiply the lengths, add the angles: $2\angle30^\circ\times3\angle40^\circ=6\angle70^\circ$.',
         r'**Divide → polar.** Divide the lengths, subtract the angles: $\dfrac{6\angle70^\circ}{3\angle40^\circ}=2\angle30^\circ$.',
         r'**Power → polar** (de Moivre). Length to the power, angle times the power: $(2\angle30^\circ)^3=8\angle90^\circ$.',
         r'**Divide → rectangular** (if both are given that way). Multiply top and bottom by the **conjugate** of the bottom, $(a+jb)^*=a-jb$: '
         r'$\dfrac{1}{1+j}=\dfrac{1-j}{(1+j)(1-j)}=\dfrac{1-j}{2}$.'])
    D.P(r'Why the conjugate works: $(a+jb)(a-jb)=a^2+b^2$ is a plain real number, so the bottom stops being complex.')
    D.P(r'Powers of $j$ repeat every four: $j^2=-1$, $j^3=j^2\cdot j=-j$, $j^4=(j^2)^2=1$. '
        r'And $\dfrac1j=\dfrac{j}{j\cdot j}=-j$.')

    D.P(r'**Roots: a $k$-th root question always has $k$ answers.** Write $z$ in polar form, then use:')
    D.EQ(r'z^{1/k}=c^{1/k}\angle\dfrac{\theta+360^\circ\ell}{k},\quad \ell=0,1,\dots,k-1')
    D.L([r'All $k$ roots have the **same length**, $c^{1/k}$.',
         r'The first one is at angle $\theta/k$.',
         r'Each next one is $360^\circ/k$ further round the circle.'])
    D.P(r'Example: the square roots of $4\angle60^\circ$ have length $\sqrt4=2$ and angles $30^\circ$ and $30^\circ+180^\circ=210^\circ$. '
        r'So they are $2\angle30^\circ$ and $2\angle210^\circ$.')
    D.P(r'Why $k$ answers: $\theta$ and $\theta+360^\circ$ are the same arrow, but after you divide by $k$ they point different ways.')
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
    ''')
    D.CO('info', r'**Bonus (skip-safe): why multiplying adds angles.** Write both numbers as exponentials and use $e^Ae^B=e^{A+B}$: '
         r'$z_1z_2=c_1e^{j\theta_1}\,c_2e^{j\theta_2}=c_1c_2\,e^{j(\theta_1+\theta_2)}$. '
         r'The two forms are linked by Euler’s identity, $e^{j\theta}=\cos\theta+j\sin\theta$. '
         r'The lecture uses it to get trig identities for free: expand $e^{jA}e^{jB}=e^{j(A+B)}$, and the real parts give $\cos(A+B)=\cos A\cos B-\sin A\sin B$.')
    D.CO('tip', r'**Casio 991 check:** complex mode does $+,-,\times,\div$ and can show the answer as $r\angle\theta$. '
         r'Use it to check your answer, but write the steps: the marks are for the working.')

    D.EX('W1 · All four fourth roots · lecture Example 1.2',
         r'Find the fourth roots of $z=81e^{j60^\circ}$.',
         [S(r'**Type:** roots ($k=4$). The number is already polar: $c=81$, $\theta=60^\circ$.'),
          S(r'**Length and first angle:** $81^{1/4}=3$, and $60^\circ/4=15^\circ$.'),
          S(r'**Spacing:** $360^\circ/4=90^\circ$, so keep adding $90^\circ$.',
            r'z^{1/4}=3\angle(15^\circ+90^\circ\ell),\quad \ell=0,1,2,3')],
         r'$3\angle15^\circ,\ 3\angle105^\circ,\ 3\angle195^\circ,\ 3\angle285^\circ$.', cites=W1(5))

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
