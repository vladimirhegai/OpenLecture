"""Topic A: complex numbers (Week 1)."""
import sympy as sp

from midlib import P, S, TAGS, link, zero


def build(D):
    W1 = lambda *p: D.cite('W1', *p)
    D.H('Topic A: Complex numbers', cites=W1(1, 3, 4, 5))
    TAGS(D, (1, 1), (1, 2))
    D.P('Complex numbers show up twice on the midterm:')
    D.L(['as their own question (convert, divide, raise to a power, take roots);',
         r'inside ' + link('B5', 'b5') + r', when a characteristic equation has no real roots and you need $\sqrt{-36}=j6$.'])

    D.P('**One number, two ways to write it.** A complex number is a point (an arrow) in the plane. You can give its '
        'coordinates, or its length and angle:')
    D.EQ(r'z=a+jb=c\,e^{j\theta}=c\angle\theta')
    D.L([r'$a=\mathrm{Re}\{z\}$: the **real part**, how far right',
         r'$b=\mathrm{Im}\{z\}$: the **imaginary part**, how far up',
         r'$c=|z|$: the **magnitude**, the length of the arrow',
         r'$\theta=\angle z$: the **angle**, measured from the positive real axis',
         r'$j=\sqrt{-1}$, so $j^2=-1$ (this course writes $j$, not $i$)'])
    D.P(r'Example: $3+j4$ has $a=3$, $b=4$, $c=\sqrt{9+16}=5$ and $\theta=\tan^{-1}(4/3)=53.13^\circ$, so $3+j4=5\angle53.13^\circ$.')

    D.P('**Converting between the two forms:**')
    D.T(['Direction', 'Formula'], [
        [r'polar → rectangular', r'$a=c\cos\theta,\quad b=c\sin\theta$'],
        [r'rectangular → polar', r'$c=\sqrt{a^2+b^2},\quad \theta=\tan^{-1}\!\left(\dfrac{b}{a}\right)$, then fix the quadrant'],
    ])
    D.CO('warning', r'**The quadrant trap.** The calculator’s $\tan^{-1}$ only returns angles between $-90^\circ$ and $90^\circ$. '
         r'Look at the signs of $a$ and $b$ first. If $a<0$ (left half of the plane), **add $180^\circ$** to what the calculator gives.')

    D.P('**Arithmetic: pick the form that makes the operation easy.**')
    D.T(['Operation', 'Use', 'Rule'], [
        [r'$z_1\pm z_2$', 'rectangular', 'add (subtract) real parts and imaginary parts separately'],
        [r'$z_1z_2$', 'polar', r'multiply magnitudes, **add** angles: $c_1c_2\angle(\theta_1+\theta_2)$'],
        [r'$z_1/z_2$', 'polar', r'divide magnitudes, **subtract** angles: $\frac{c_1}{c_2}\angle(\theta_1-\theta_2)$'],
        [r'$z_1/z_2$', 'rectangular', r'multiply top and bottom by the **conjugate** of the bottom: $(a+jb)^*=a-jb$'],
        [r'$z^k$', 'polar', r'$c^k\angle k\theta$ (de Moivre)'],
    ])
    D.P(r'The conjugate works because $(a+jb)(a-jb)=a^2+b^2$, a real number. Powers of $j$ repeat every four: '
        r'$j^2=-1$, $j^3=-j$, $j^4=1$, and $\dfrac1j=-j$.')

    D.P(r'**Roots: a $k$-th root question always has $k$ answers.** Write $z$ in polar form, then:')
    D.EQ(r'z^{1/k}=c^{1/k}\angle\dfrac{\theta+360^\circ\ell}{k},\qquad \ell=0,1,\dots,k-1')
    D.L([r'all $k$ roots have the **same magnitude** $c^{1/k}$;',
         r'the first is at angle $\theta/k$;',
         r'the rest follow, each $360^\circ/k$ further round the circle.'])
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
    caption "Start: $z=2.5\angle90^\circ$, $k=3$. The roots have magnitude $2.5^{1/3}$; the first is at $90^\circ/3=30^\circ$, the others $120^\circ$ apart."
    ''')
    D.CO('info', r'**Bonus (skip-safe): why multiplying adds angles.** In polar form $z_1z_2=c_1e^{j\theta_1}\,c_2e^{j\theta_2}=c_1c_2\,e^{j(\theta_1+\theta_2)}$: '
         r'the exponent rule $e^Ae^B=e^{A+B}$ adds the angles. Euler’s identity $e^{j\theta}=\cos\theta+j\sin\theta$ connects the two forms. '
         r'The lecture uses it to get trig identities for free: expand $e^{jA}e^{jB}=e^{j(A+B)}$ and compare real parts to get $\cos(A+B)=\cos A\cos B-\sin A\sin B$.')
    D.CO('tip', r'**Casio 991 check:** complex mode does $+,-,\times,\div$ and can show the answer as $r\angle\theta$. Use it to check, but write the steps: the marks are for the working.')

    D.EX('W1 · All four fourth roots · lecture Example 1.2',
         r'Find the fourth roots of $z=81e^{j60^\circ}$.',
         [S(r'**Type:** roots ($k=4$). The number is already polar: $c=81$, $\theta=60^\circ$.'),
          S(r'**Method:** magnitude $81^{1/4}=3$; first angle $60^\circ/4=15^\circ$; spacing $360^\circ/4=90^\circ$.',
            r'z^{1/4}=3\angle(15^\circ+90^\circ\ell),\qquad \ell=0,1,2,3')],
         r'$3\angle15^\circ,\ 3\angle105^\circ,\ 3\angle195^\circ,\ 3\angle285^\circ$.', cites=W1(5))

    P(D, 'W1 · Convert, watching the quadrant',
      r'Write (a) $-3+j4$ and (b) $-3-j4$ in polar form.',
      [S(r'**Type:** rectangular → polar. Both have $a<0$: left half, so the $180^\circ$ fix applies.'),
       S(r'Magnitude (same for both).', r'c=\sqrt{(-3)^2+4^2}=5'),
       S(r'(a) The calculator gives $\tan^{-1}(4/-3)=-53.13^\circ$. The point is in quadrant II, so add $180^\circ$.', r'\theta=126.87^\circ'),
       S(r'(b) The calculator gives $\tan^{-1}(-4/-3)=53.13^\circ$. The point is in quadrant III, so add $180^\circ$.', r'\theta=233.13^\circ\ \ (=-126.87^\circ)')],
      r'(a) $5\angle126.87^\circ$. (b) $5\angle233.13^\circ$, the same as $5\angle-126.87^\circ$.')
    P(D, 'W1 · Divide in rectangular form · lecture Example 1.1',
      r'Compute $\dfrac{80+j18}{8+j10}$. Give the answer in rectangular and polar form.',
      [S(r'**Type:** division of two rectangular numbers: multiply top and bottom by the conjugate $8-j10$.',
         r'\dfrac{(80+j18)(8-j10)}{(8+j10)(8-j10)}'),
       S(r'Bottom: $8^2+10^2=164$. Top: expand, using $j^2=-1$.', r'(640+180)+j(144-800)=820-j656'),
       S('Divide both parts by 164.', r'5-j4'),
       S(r'Polar: $a>0$, $b<0$, quadrant IV, so the calculator angle is already right.', r'\sqrt{41}\angle-38.66^\circ')],
      r'$5-j4=\sqrt{41}\angle-38.66^\circ\approx6.40\angle-38.66^\circ$.', cites=W1(4))
    P(D, 'W1 · A high power',
      r'Compute $(1+j)^8$.',
      [S(r'**Type:** power. Go polar first: $c=\sqrt2$, $\theta=45^\circ$.', r'1+j=\sqrt2\angle45^\circ'),
       S(r'de Moivre: raise the magnitude to the 8th, multiply the angle by 8.', r'(\sqrt2)^8\angle360^\circ=16\angle0^\circ')],
      r'$(1+j)^8=16$.', diff='intermediate')
    P(D, 'W1 · Cube roots of a negative number',
      r'Find all three cube roots of $-8$, in polar and rectangular form.',
      [S(r'**Type:** roots ($k=3$). Polar first: $-8$ sits on the negative real axis.', r'-8=8\angle180^\circ'),
       S(r'Magnitude $8^{1/3}=2$; first angle $180^\circ/3=60^\circ$; spacing $120^\circ$.', r'2\angle60^\circ,\quad 2\angle180^\circ,\quad 2\angle300^\circ'),
       S(r'Rectangular: $a=2\cos\theta$, $b=2\sin\theta$.', r'1+j\sqrt3,\quad -2,\quad 1-j\sqrt3')],
      r'$2\angle60^\circ=1+j\sqrt3$, $2\angle180^\circ=-2$, $2\angle300^\circ=1-j\sqrt3$. The real root $-2$ is only one of three.',
      diff='intermediate')
    P(D, 'W1 + W5 · The complex roots of a quadratic',
      r'Solve $s^2+4s+13=0$. (This is exactly the step you meet in ' + link('B5', 'b5') + '.)',
      [S(r'**Type:** quadratic with $b^2-4ac<0$: the roots are complex.', r's=\dfrac{-4\pm\sqrt{16-52}}{2}=\dfrac{-4\pm\sqrt{-36}}{2}'),
       S(r'$\sqrt{-36}=\sqrt{36}\,\sqrt{-1}=j6$.', r's=\dfrac{-4\pm j6}{2}')],
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
