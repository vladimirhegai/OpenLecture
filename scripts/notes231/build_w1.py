"""ELEC 231 Week 1: complex numbers and the first differential equation (RL natural response).
Run: .venv/Scripts/python.exe scripts/notes231/build_w1.py [--publish]"""
import cmath
import math
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib231 import Doc, S  # noqa: E402
from figs_w1 import make  # noqa: E402

FIGS = make()

D = Doc(1, 'Week 1: Complex Numbers and Your First Differential Equation',
        ['complex_numbers', 'complex_arithmetic', 'rl_natural_response'])
W = lambda *p: D.cite('W1', *p)  # noqa: E731


# ---------------------------------------------------------------- checks (the build stops if any fails)
def polar(z):
    return abs(z), math.degrees(cmath.phase(z))


def close(a, b, tol=1e-3):
    return abs(a - b) < tol


def check():
    # Topic 1 conversions
    assert close(polar(3 + 4j)[0], 5) and close(polar(3 + 4j)[1], 53.13)
    assert close(polar(-3 + 4j)[1], 126.87)
    assert close(polar(-1 - 1j)[1], -135)
    z = 10 * cmath.exp(1j * math.radians(150))
    assert close(z.real, -8.660) and close(z.imag, 5)
    z = 2 * cmath.exp(-1j * math.pi / 3)
    assert close(z.real, 1) and close(z.imag, -1.732)
    assert close(polar(1 + 1j * math.sqrt(3))[1], 60)
    assert close(polar(-5 - 12j)[0], 13) and close(polar(-5 - 12j)[1], -112.62)
    assert close(polar(4 - 4j)[0], 5.657) and close(polar(4 - 4j)[1], -45)
    z = 6 * cmath.exp(1j * math.radians(240))
    assert close(z.real, -3) and close(z.imag, -5.196)
    # Euler identities
    A, B, th = sp.symbols('A B theta', real=True)
    e = sp.expand(sp.expand_complex((sp.cos(A) + sp.I * sp.sin(A)) * (sp.cos(B) - sp.I * sp.sin(B))))
    assert sp.simplify(sp.re(e) - sp.cos(A - B)) == 0 and sp.simplify(sp.im(e) - sp.sin(A - B)) == 0
    e = sp.expand((sp.cos(th) + sp.I * sp.sin(th)) ** 2)
    assert sp.simplify(sp.re(e) - sp.cos(2 * th)) == 0 and sp.simplify(sp.im(e) - sp.sin(2 * th)) == 0
    # Topic 2 arithmetic
    assert (3 + 4j) + (1 - 6j) == 4 - 2j and (3 + 4j) - (1 - 6j) == 2 + 10j
    assert (2 + 3j) * (4 - 1j) == 11 + 10j
    assert close((80 + 18j) / (8 + 10j), 5 - 4j)
    p = polar(6 * cmath.exp(1j * math.radians(40)) * 2 * cmath.exp(-1j * math.radians(70)))
    assert close(p[0], 12) and close(p[1], -30)
    p = polar(6 * cmath.exp(1j * math.radians(40)) / (2 * cmath.exp(-1j * math.radians(70))))
    assert close(p[0], 3) and close(p[1], 110)
    assert close((1 + 1j) ** 8, 16)
    for ang in (15, 105, 195, 285):
        assert close((3 * cmath.exp(1j * math.radians(ang))) ** 4, 81 * cmath.exp(1j * math.radians(60)))
    s = sp.symbols('s')
    assert set(sp.solve(s**2 + 2 * s + 5, s)) == {-1 - 2 * sp.I, -1 + 2 * sp.I}
    assert (5 - 2j) - (-3 + 7j) == 8 - 9j and (5 - 2j) * (-3 + 7j) == -1 + 41j
    assert close((10 + 5j) / (3 - 4j), 0.4 + 2.2j)
    assert 1 / 1j == -1j and 1j ** 3 == -1j and close(1j ** 10, -1)
    assert close((1 - 1j * math.sqrt(3)) ** 6, 64)
    for r in (math.sqrt(3) + 1j, -math.sqrt(3) + 1j, -2j):
        assert close(r ** 3, 8j)
    z = 3 - 4j
    assert z * z.conjugate() == 25 and z + z.conjugate() == 6 and z - z.conjugate() == -8j
    assert set(sp.solve(s**2 + 4 * s + 13, s)) == {-2 - 3 * sp.I, -2 + 3 * sp.I}
    # Topic 3 ODEs
    t = sp.symbols('t', nonnegative=True)
    y0, R, L = sp.symbols('y_0 R L', positive=True)
    y = y0 * sp.exp(-t)
    assert sp.simplify(sp.diff(y, t) + y) == 0 and y.subs(t, 0) == y0
    i = y0 * sp.exp(-R / L * t)
    assert sp.simplify(R * i + L * sp.diff(i, t)) == 0
    i = 4 * sp.exp(-500 * t)  # pre-tutorial 1: L = 8 mH, R = 4 ohm
    assert sp.simplify(sp.Rational(8, 1000) * sp.diff(i, t) + 4 * i) == 0
    i = 10 * sp.exp(-200 * t)  # 0.5 H, 100 ohm
    assert sp.simplify(sp.Rational(1, 2) * sp.diff(i, t) + 100 * i) == 0
    assert close(0.005 * math.log(10), 0.011513)
    assert close(5 * math.exp(-3 * 0), 5)
    assert close(3 * math.exp(-5 * 0.2), 1.1036)
    assert close(0.004 * 50, 0.2)
    assert close(math.log(100), 4.605)
    i = 2 * sp.exp(-500 * t)  # 40 mH, 20 ohm
    assert sp.simplify(sp.Rational(40, 1000) * sp.diff(i, t) + 20 * i) == 0
    i = 2 * sp.exp(-50 * t)  # 0.1 H, 5 ohm
    assert sp.simplify(sp.Rational(1, 10) * sp.diff(i, t) + 5 * i) == 0
    # Mixed practice
    z1, z2 = 2 + 2j, 1 - 1j * math.sqrt(3)
    assert close(polar(z1 * z2)[0], 5.657) and close(polar(z1 * z2)[1], -15)
    assert close(z1 * z2, 5.464 - 1.464j) and close(z1 / z2, -0.366 + 1.366j) and close(polar(z1 / z2)[1], 105)
    for r in (1.5 + 2.598j, -3, 1.5 - 2.598j):
        assert close(r ** 3, -27, 1e-2)
    assert close(0.0025 * math.log(5), 0.004024) and close(5 * math.exp(-2), 0.6767)
    assert close(cmath.exp(1j * math.pi) + 1, 0) and close((4 * cmath.exp(1j * math.pi / 6)).real, 3.464)
    assert close((3 + 4j) ** 2 / (1 - 1j), -15.5 + 8.5j)
    assert set(sp.solve(s**2 + 6 * s + 25, s)) == {-3 - 4 * sp.I, -3 + 4 * sp.I} and close(polar(-3 + 4j)[1], 126.87)
    assert close(2 * math.exp(-1), 0.7358)
    print('all Week 1 checks passed')


check()

# ================================================================ intro
D.CO('info', "**Week 1 in one sentence:** complex numbers are points on a flat plane that you can write two ways "
             "($a+jb$ or $c\\,e^{j\\theta}$), and a circuit with an inductor gives you your first differential equation, "
             "whose answer is a decaying exponential.\n\n"
             "**By the end you can:**\n\n"
             "- switch any complex number between rectangular form $a+jb$ and polar form $c\\,e^{j\\theta}$ (with the right angle in every quadrant);\n"
             "- add, subtract, multiply, divide, and take powers and roots of complex numbers;\n"
             "- use Euler's identity $e^{j\\theta}=\\cos\\theta+j\\sin\\theta$ (including to prove trig identities);\n"
             "- write the differential equation of an RL circuit after a switch opens, solve it, and use the time constant $\\tau=L/R$.")
D.CO('tip', "**Why complex numbers in a differential-equations course?** In Week 5 you will solve equations like "
            "$y''+2y'+5y=0$ by solving $s^2+2s+5=0$, and the roots are $s=-1\\pm j2$, complex numbers. "
            "Those roots turn into decaying oscillations (the ringing of an RLC circuit). Everything in Topics 1–2 is the toolkit for that.")

# ================================================================ Topic 1
D.H('Topic 1: Complex numbers: one point, two ways to write it', cites=W(1))
D.P("Engineers write $j$ for $\\sqrt{-1}$ (so $j^2=-1$; $i$ is already taken by current). A complex number "
    "$z=a+jb$ is really just a **point on a plane**: go $a$ to the right along the horizontal *real axis* (Re) and "
    "$b$ up along the vertical *imaginary axis* (Im). $a=\\mathrm{Re}\\{z\\}$ is the *real part* and "
    "$b=\\mathrm{Im}\\{z\\}$ is the *imaginary part*; both are ordinary real numbers.\n\n"
    "You can describe the same point a second way: **how far** it is from the origin ($c=|z|$, the *magnitude*, never negative) "
    "and **which direction** it points ($\\theta=\\angle z$, the *angle*, measured counter-clockwise from the positive real axis). "
    "That is *polar form*, written $z=c\\,e^{j\\theta}$ or, in angle notation, $z=c\\angle\\theta$. "
    "Rectangular form is best for adding; polar form is best for multiplying. Converting between them is the core skill of this week.",
    cites=W(1))
D.CO('tip', "**The method: converting**\n\n"
            "**Rectangular → polar** ($a+jb\\;\\to\\;c\\angle\\theta$):\n\n"
            "1. **Sketch the point** $(a,b)$ so you know its quadrant.\n"
            "2. Magnitude: $c=\\sqrt{a^2+b^2}$.\n"
            "3. Reference angle: $\\theta_{\\text{ref}}=\\arctan\\left|\\dfrac{b}{a}\\right|$ (an angle between $0^\\circ$ and $90^\\circ$).\n"
            "4. Put it in the right quadrant with the table below.\n\n"
            "**Polar → rectangular** ($c\\angle\\theta\\;\\to\\;a+jb$): $a=c\\cos\\theta$, $b=c\\sin\\theta$. "
            "No quadrant thinking needed: the signs of $\\cos$ and $\\sin$ take care of it.\n\n"
            "**Casio 991 check:** `Pol(a, b)` returns $c$ and $\\theta$ (between $-180^\\circ$ and $180^\\circ$) with the quadrant already handled; "
            "`Rec(c, θ)` goes back. Make sure the calculator is in degree mode when you use degrees.", cites=W(1, 2, 3))
D.EQ(r'z=a+jb=c\,e^{j\theta}=c\angle\theta,\qquad c=\sqrt{a^2+b^2},\quad \tan\theta=\frac{b}{a},\qquad a=c\cos\theta,\quad b=c\sin\theta',
     cites=W(1, 2, 3))
D.T(['Where the point is', 'Signs', 'Angle $\\theta$ (from the reference angle)', 'Example'], [
    ['1st quadrant (up-right)', '$a>0,\\ b>0$', '$\\theta=\\theta_{\\text{ref}}$', '$3+j4$: $53.13^\\circ$'],
    ['2nd quadrant (up-left)', '$a<0,\\ b>0$', '$\\theta=180^\\circ-\\theta_{\\text{ref}}$', '$-3+j4$: $126.87^\\circ$'],
    ['3rd quadrant (down-left)', '$a<0,\\ b<0$', '$\\theta=180^\\circ+\\theta_{\\text{ref}}$ (same as $-(180^\\circ-\\theta_{\\text{ref}})$)', '$-3-j4$: $233.13^\\circ=-126.87^\\circ$'],
    ['4th quadrant (down-right)', '$a>0,\\ b<0$', '$\\theta=-\\theta_{\\text{ref}}$ (same as $360^\\circ-\\theta_{\\text{ref}}$)', '$3-j4$: $-53.13^\\circ$'],
    ['On an axis', '', '$1=1\\angle0^\\circ$, $j=1\\angle90^\\circ$, $-1=1\\angle180^\\circ$, $-j=1\\angle-90^\\circ$', ''],
], cites=W(3))
D.FIG(FIGS['plane'], 'Four points, four quadrants. Every arrow has length $c=5$; only the angle changes. The angle is always measured counter-clockwise from the positive real axis (orange arc for $-3+j4$).')
D.P("**Euler's identity** is the bridge between the two forms. It says that $e^{j\\theta}$ is the point at angle $\\theta$ "
    "on the circle of radius 1:")
D.EQ(r'e^{j\theta}=\cos\theta+j\sin\theta\qquad\Longrightarrow\qquad c\,e^{j\theta}=c\cos\theta+j\,c\sin\theta=a+jb', cites=W(1))
D.P("Multiplying by $c$ just stretches that unit point out to distance $c$, which is why $a=c\\cos\\theta$ and $b=c\\sin\\theta$. "
    "Two consequences you will use a lot: $|e^{j\\theta}|=\\sqrt{\\cos^2\\theta+\\sin^2\\theta}=1$ (it always has length 1), and "
    "$e^{j\\theta}$ only moves *around* a circle, so it can never grow or shrink.", cites=W(4))

D.EX('A first-quadrant point', r'Write $z=3+j4$ in polar form.',
     [S("Sketch it: 3 to the right, 4 up. Both parts are positive, so the point is in the 1st quadrant."),
      S("The magnitude is the distance from the origin, by Pythagoras.", r'c=\sqrt{3^2+4^2}=\sqrt{25}=5'),
      S("In the 1st quadrant the angle is just the arctangent of (up ÷ right).", r'\theta=\arctan\frac{4}{3}=53.13^\circ'),
      S("Write the answer both ways.", r'z=5\angle53.13^\circ=5\,e^{j53.13^\circ}')],
     r'$z=5\angle 53.13^\circ$')
D.EX('The quadrant trap', r'Write $z=-3+j4$ in polar form.',
     [S("Sketch it: 3 to the **left**, 4 up. That is the 2nd quadrant."),
      S("The magnitude doesn't care about signs.", r'c=\sqrt{(-3)^2+4^2}=5'),
      S("A calculator's $\\arctan(4/(-3))$ gives $-53.13^\\circ$, which points down-right: wrong quadrant! "
        "Instead take the reference angle (the angle to the nearest horizontal axis) using sizes only.", r'\theta_{\text{ref}}=\arctan\frac{4}{3}=53.13^\circ'),
      S("In the 2nd quadrant the angle is measured from the positive real axis, so it is $180^\\circ$ minus the reference angle.",
        r'\theta=180^\circ-53.13^\circ=126.87^\circ'),
      S("Check with `Pol(-3, 4)` on the calculator: it gives $5$ and $126.87^\\circ$. ✓", r'z=5\angle126.87^\circ')],
     r'$z=5\angle126.87^\circ$ (not $-53.13^\circ$)')
D.EX('Third quadrant', r'Write $z=-1-j$ in polar form.',
     [S("Sketch: 1 left and 1 down, the 3rd quadrant."),
      S("The magnitude is the distance from the origin, by Pythagoras (the minus signs disappear when squared).", r'c=\sqrt{(-1)^2+(-1)^2}=\sqrt2\approx1.414'),
      S("The reference angle uses the sizes only (ignore the signs): the angle between the arrow and the horizontal axis.", r'\theta_{\text{ref}}=\arctan\frac11=45^\circ'),
      S("3rd quadrant: go past $180^\\circ$ by the reference angle. Going clockwise instead gives the equivalent negative angle; both are correct.",
        r'\theta=180^\circ+45^\circ=225^\circ\quad(\text{same as }-135^\circ)')],
     r'$z=\sqrt2\angle225^\circ=\sqrt2\angle-135^\circ$')
D.EX('Polar back to rectangular', r'Write (a) $z=10\,e^{j150^\circ}$ and (b) $w=2\,e^{-j\pi/3}$ in rectangular form.',
     [S("Use $a=c\\cos\\theta$ and $b=c\\sin\\theta$. For (a), $c=10$ and $\\theta=150^\\circ$.", r'a=10\cos150^\circ=10(-0.866)=-8.66,\qquad b=10\sin150^\circ=10(0.5)=5'),
      S("So (a) is in the 2nd quadrant, as $150^\\circ$ should be.", r'z=-8.66+j5'),
      S("For (b) the angle is in **radians**: $\\pi/3=60^\\circ$, and the minus sign means clockwise. Set the calculator to radians, or convert to degrees first.",
        r'a=2\cos(-60^\circ)=2(0.5)=1,\qquad b=2\sin(-60^\circ)=2(-0.866)=-1.732'),
      S("So (b) is in the 4th quadrant.", r'w=1-j1.732')],
     r'(a) $-8.66+j5$  (b) $1-j1.732$')
D.EX("Trig identities for free from Euler (Lecture 1)",
     r'Use $e^{jA}e^{jB}=e^{j(A+B)}$ to find formulas for $\cos(A+B)$ and $\sin(A+B)$.',
     [S("Exponents add when you multiply, so the left and right sides are equal. Write each exponential with Euler's identity.",
        r'(\cos A+j\sin A)(\cos B+j\sin B)=\cos(A+B)+j\sin(A+B)'),
      S("Multiply out the left side like ordinary brackets, remembering $j\\cdot j=j^2=-1$.",
        r'\cos A\cos B+j\cos A\sin B+j\sin A\cos B+j^2\sin A\sin B'),
      S("Group the real terms (no $j$) and the imaginary terms (with $j$).",
        r'=(\cos A\cos B-\sin A\sin B)+j(\sin A\cos B+\cos A\sin B)'),
      S("Two complex numbers are equal only if their real parts match **and** their imaginary parts match. Match them.",
        r'\cos(A+B)=\cos A\cos B-\sin A\sin B,\qquad \sin(A+B)=\sin A\cos B+\cos A\sin B')],
     r'$\cos(A+B)=\cos A\cos B-\sin A\sin B$, $\sin(A+B)=\sin A\cos B+\cos A\sin B$', cites=W(2))

D.CO('warning', "**Common mistakes**\n\n"
                "- Trusting $\\arctan(b/a)$ blindly. It only gives the right angle in the 1st and 4th quadrants. Always sketch the point first.\n"
                "- Calculator in the wrong mode: $\\cos(150)$ in radian mode is not $\\cos150^\\circ$.\n"
                "- A negative magnitude. $c$ is a distance, so it is always $\\ge0$; a minus sign belongs in the angle ($-5=5\\angle180^\\circ$).\n"
                "- Forgetting that $\\theta$ and $\\theta\\pm360^\\circ$ are the same direction ($225^\\circ=-135^\\circ$). Either is a correct answer.")

D.PR('Quick conversion', r'Write $z=1+j\sqrt3$ in polar form.',
     [S("1 right and $\\sqrt3\\approx1.73$ up: 1st quadrant."),
      S("The magnitude is the distance from the origin, by Pythagoras.", r'c=\sqrt{1^2+(\sqrt3)^2}=\sqrt{4}=2'),
      S("In the 1st quadrant the angle is just $\\arctan(\\text{up}\\div\\text{right})$; $\\arctan\\sqrt3=60^\\circ$ is a standard angle.", r'\theta=\arctan\frac{\sqrt3}{1}=60^\circ')],
     r'$z=2\angle60^\circ=2e^{j\pi/3}$')
D.PR('Down and to the left', r'Write $z=-5-j12$ in polar form.',
     [S("5 left and 12 down: 3rd quadrant."),
      S("The magnitude, by Pythagoras (the signs disappear when squared).", r'c=\sqrt{(-5)^2+(-12)^2}=\sqrt{169}=13'),
      S("The reference angle uses the sizes only: up/down size 12, left/right size 5.", r'\theta_{\text{ref}}=\arctan\frac{12}{5}=67.38^\circ'),
      S("In the 3rd quadrant go past $180^\\circ$ by the reference angle. Subtracting $360^\\circ$ gives the same direction measured clockwise.", r'\theta=180^\circ+67.38^\circ=247.38^\circ\;(=-112.62^\circ)')],
     r'$z=13\angle247.38^\circ=13\angle-112.62^\circ$')
D.PR('Fourth quadrant', r'Write $z=4-j4$ in polar form.',
     [S("4 right and 4 down: 4th quadrant."),
      S("The magnitude, by Pythagoras.", r'c=\sqrt{4^2+(-4)^2}=\sqrt{32}=4\sqrt2\approx5.657'),
      S("Reference angle $45^\\circ$; in the 4th quadrant measure it clockwise.", r'\theta=-45^\circ')],
     r'$z=5.657\angle-45^\circ$')
D.PR('Polar to rectangular', r'Write $z=6\,e^{j240^\circ}$ in rectangular form.',
     [S("Use $a=c\\cos\\theta$, $b=c\\sin\\theta$.", r'a=6\cos240^\circ=6(-0.5)=-3,\qquad b=6\sin240^\circ=6(-0.866)=-5.196'),
      S("$240^\\circ$ is in the 3rd quadrant, and both parts are negative. ✓", r'z=-3-j5.196')],
     r'$z=-3-j5.196$')
D.PR('Points on the axes', r'Write in polar form: (a) $-7$ (b) $j2$ (c) $-j7$.',
     [S("(a) 7 to the left on the real axis: distance 7, pointing at $180^\\circ$.", r'-7=7\angle180^\circ'),
      S("(b) 2 straight up: $90^\\circ$.", r'j2=2\angle90^\circ'),
      S("(c) 7 straight down: $-90^\\circ$ (or $270^\\circ$).", r'-j7=7\angle-90^\circ')],
     r'(a) $7\angle180^\circ$ (b) $2\angle90^\circ$ (c) $7\angle-90^\circ$')
D.PR("Another identity from Euler", r'Use $e^{jA}e^{-jB}=e^{j(A-B)}$ to find $\cos(A-B)$ and $\sin(A-B)$.',
     [S("$e^{-jB}=\\cos(-B)+j\\sin(-B)=\\cos B-j\\sin B$ (cosine is even, sine is odd).",
        r'(\cos A+j\sin A)(\cos B-j\sin B)=\cos(A-B)+j\sin(A-B)'),
      S("Multiply out, using $j\\cdot(-j)=-j^2=+1$.", r'=(\cos A\cos B+\sin A\sin B)+j(\sin A\cos B-\cos A\sin B)'),
      S("Match real and imaginary parts.", r'\cos(A-B)=\cos A\cos B+\sin A\sin B,\qquad \sin(A-B)=\sin A\cos B-\cos A\sin B')],
     r'$\cos(A-B)=\cos A\cos B+\sin A\sin B$, $\sin(A-B)=\sin A\cos B-\cos A\sin B$', diff='intermediate')

# ================================================================ Topic 2
D.H('Topic 2: Complex arithmetic: add, multiply, divide, powers and roots', cites=W(3, 4))
D.P("Each operation is easy in one form and messy in the other, so the whole trick is **pick the right form first**:\n\n"
    "- **Adding and subtracting** works like adding arrows tip-to-tail: add the real parts and add the imaginary parts. Use **rectangular** form.\n"
    "- **Multiplying** multiplies the lengths and **adds the angles** (it stretches and rotates). Dividing divides the lengths and subtracts the angles. Use **polar** form.\n"
    "- **Powers** repeat a multiplication: raise the length to the power and multiply the angle (*de Moivre's theorem*).\n"
    "- **Roots**: a $k$-th root has **$k$ different answers**, all the same length, spread evenly around a circle, $360^\\circ/k$ apart.\n\n"
    "The **complex conjugate** $z^*$ flips the sign of the imaginary part (a mirror image across the real axis). "
    "Its superpower: $z\\,z^*=a^2+b^2$ is a plain real number, which is how you divide in rectangular form.", cites=W(3, 4))
D.CO('tip', "**The method: which form for which job**\n\n"
            "1. $+$ or $-$: rectangular. $(a_1+jb_1)\\pm(a_2+jb_2)=(a_1\\pm a_2)+j(b_1\\pm b_2)$.\n"
            "2. $\\times$ or $\\div$: polar (multiply/divide the lengths, add/subtract the angles). In rectangular form you can also multiply out the brackets with $j^2=-1$, and divide by multiplying top and bottom by the conjugate of the bottom.\n"
            "3. Power $z^k$: polar, $c^k\\angle k\\theta$.\n"
            "4. Roots $z^{1/k}$: polar. Length $c^{1/k}$; first angle $\\theta/k$; add $360^\\circ/k$ to get each of the other $k-1$ roots.", cites=W(3, 4))
D.EQ(r'z_1z_2=c_1c_2\,e^{j(\theta_1+\theta_2)},\qquad \frac{z_1}{z_2}=\frac{c_1}{c_2}\,e^{j(\theta_1-\theta_2)},\qquad z^k=c^k\,e^{jk\theta}', cites=W(3, 4))
D.EQ(r'z^{1/k}=c^{1/k}\,e^{j\theta/k}\,x_\ell,\quad x_\ell=e^{j\,360^\circ\ell/k}\;(\ell=0,1,\dots,k-1),\qquad (a+jb)^*=a-jb,\quad z\,z^*=a^2+b^2', cites=W(4))
D.P("The $x_\\ell$ are the *$k$-th roots of 1*: the $k$ points on the unit circle that land on 1 when raised to the $k$-th power "
    "(for $k=4$: $1,\\ j,\\ -1,\\ -j$). Multiplying by them is what spaces the roots $360^\\circ/k$ apart. "
    "Also handy from the conjugate: $z+z^*=2\\,\\mathrm{Re}\\{z\\}$ and $z-z^*=j\\,2\\,\\mathrm{Im}\\{z\\}$.", cites=W(4, 5))

D.EX('Adding and subtracting', r'$z_1=3+j4$, $z_2=1-j6$. Find $z_1+z_2$ and $z_1-z_2$.',
     [S("Add real parts with real parts and imaginary with imaginary.", r'z_1+z_2=(3+1)+j(4-6)=4-j2'),
      S("Subtracting: be careful to subtract **both** parts of $z_2$.", r'z_1-z_2=(3-1)+j(4-(-6))=2+j10')],
     r'$z_1+z_2=4-j2$, $z_1-z_2=2+j10$', cites=W(3))
D.EX('Multiplying in rectangular form', r'Find $(2+j3)(4-j)$.',
     [S("Expand the brackets term by term (FOIL), exactly like $(x+y)(u+v)$.", r'2\cdot4+2(-j)+j3\cdot4+j3(-j)=8-j2+j12-j^2\,3'),
      S("Replace $j^2$ with $-1$, so $-j^2\\,3=+3$.", r'=8+3+j(12-2)'),
      S("Collect the real numbers ($8+3$) and the $j$ terms ($12-2$).", r'=11+j10')],
     r'$11+j10$', cites=W(4))
D.EX('Dividing in rectangular form (Lecture Example 1.1)', r'Find $\dfrac{80+j18}{8+j10}$.',
     [S("To get rid of $j$ in the bottom, multiply top and bottom by the conjugate of the bottom, $8-j10$. "
        "This doesn't change the value (it's multiplying by 1).", r'\frac{80+j18}{8+j10}\cdot\frac{8-j10}{8-j10}'),
      S("The bottom becomes a real number: $z\\,z^*=a^2+b^2$.", r'(8+j10)(8-j10)=64+100=164'),
      S("Multiply out the top with $j^2=-1$.", r'(80+j18)(8-j10)=640-j800+j144-j^2\,180=820-j656'),
      S("Divide each part by 164.", r'\frac{820-j656}{164}=5-j4')],
     r'$5-j4$', cites=W(4))
D.EX('Multiplying and dividing in polar form', r'Find $(6\angle40^\circ)(2\angle-70^\circ)$ and $\dfrac{6\angle40^\circ}{2\angle-70^\circ}$.',
     [S("Multiplying: multiply the lengths, **add** the angles.", r'(6)(2)\angle(40^\circ+(-70^\circ))=12\angle-30^\circ'),
      S("Dividing: divide the lengths, **subtract** the angles (top minus bottom).", r'\frac{6}{2}\angle(40^\circ-(-70^\circ))=3\angle110^\circ')],
     r'$12\angle-30^\circ$ and $3\angle110^\circ$', cites=W(3))
D.EX("A big power: de Moivre's theorem", r'Find $(1+j)^8$.',
     [S("Multiplying $1+j$ by itself 8 times is painful. In polar form it's one step. First convert: 1 right, 1 up.",
        r'1+j=\sqrt2\angle45^\circ'),
      S("Raise the length to the 8th power and multiply the angle by 8.", r'(\sqrt2)^8\angle(8\times45^\circ)=16\angle360^\circ'),
      S("$360^\\circ$ is a full turn, the same direction as $0^\\circ$: pointing along the positive real axis.", r'16\angle360^\circ=16')],
     r'$(1+j)^8=16$', cites=W(4))
D.EX('All four fourth roots (Lecture Example 1.2)', r'Find all fourth roots of $z=81\,e^{j60^\circ}$.',
     [S("Here $c=81$, $\\theta=60^\\circ$ and $k=4$. The length of every root is the 4th root of 81.", r'81^{1/4}=3'),
      S("The first root's angle is the angle divided by 4.", r'\frac{60^\circ}{4}=15^\circ\quad\Rightarrow\quad 3\,e^{j15^\circ}'),
      S("The other three are spaced $360^\\circ/4=90^\\circ$ apart (that's multiplying by the fourth roots of 1: $1, j, -1, -j$).",
        r'3e^{j15^\circ},\quad 3e^{j105^\circ},\quad 3e^{j195^\circ},\quad 3e^{j285^\circ}'),
      S("Check one: $(3e^{j105^\\circ})^4=81\\,e^{j420^\\circ}=81\\,e^{j60^\\circ}$ because $420^\\circ-360^\\circ=60^\\circ$. ✓")],
     r'$3e^{j15^\circ},\ 3e^{j105^\circ},\ 3e^{j195^\circ},\ 3e^{j285^\circ}$', cites=W(4, 5))
D.FIG(FIGS['roots'], r'The four fourth roots of $81e^{j60^\circ}$ sit on a circle of radius 3, starting at $15^\circ$ and spaced $90^\circ$ apart. Every $k$-th root problem looks like this: $k$ equally spaced points on one circle.')
D.CO('info', "**Algebra reminder: the quadratic formula** $as^2+bs+c=0\\;\\Rightarrow\\;s=\\dfrac{-b\\pm\\sqrt{b^2-4ac}}{2a}$. "
             "When $b^2-4ac$ is negative, take the square root of the positive number and attach a $j$: $\\sqrt{-16}=\\sqrt{16}\\,\\sqrt{-1}=j4$.")
D.EX('Why we need all this: complex roots of a quadratic', r"Solve $s^2+2s+5=0$. (In Week 5 this equation comes from the ODE $y''+2y'+5y=0$.)",
     [S("Use the quadratic formula with $a=1$, $b=2$, $c=5$.", r's=\frac{-2\pm\sqrt{4-20}}{2}=\frac{-2\pm\sqrt{-16}}{2}'),
      S("The number under the root is negative, so the roots are complex: $\\sqrt{-16}=\\sqrt{16}\\,\\sqrt{-1}=j4$.", r's=\frac{-2\pm j4}{2}=-1\pm j2'),
      S("The roots always come as a **conjugate pair** ($-1+j2$ and $-1-j2$) when the equation has real coefficients.")],
     r'$s=-1\pm j2$')

D.CO('warning', "**Common mistakes**\n\n"
                "- Adding in polar form: $5\\angle0^\\circ+5\\angle90^\\circ$ is **not** $10\\angle90^\\circ$. Convert to rectangular first ($5+j5$).\n"
                "- Forgetting $j^2=-1$ when expanding brackets (a sign error on the real part).\n"
                "- Roots: giving only one answer. A $k$-th root has $k$ answers, $360^\\circ/k$ apart, and the first angle is $\\theta/k$ (divide the angle too!).\n"
                "- The conjugate in polar form flips the **angle**: $(c\\,e^{j\\theta})^*=c\\,e^{-j\\theta}$.")

D.PR('Subtract and multiply', r'$z_1=5-j2$, $z_2=-3+j7$. Find $z_1-z_2$ and $z_1z_2$.',
     [S("Subtract real from real and imaginary from imaginary; subtracting $-3$ adds 3, and subtracting $j7$ takes 7 off the imaginary part.", r'z_1-z_2=(5+3)+j(-2-7)=8-j9'),
      S("Expand the brackets term by term: $5(-3)$, $5(j7)$, $(-j2)(-3)$ and $(-j2)(j7)$.", r'(5-j2)(-3+j7)=-15+j35+j6-j^2\,14'),
      S("Replace $j^2$ by $-1$, so $-j^2\\,14=+14$, then collect real and imaginary parts.", r'=-15+14+j41=-1+j41')],
     r'$z_1-z_2=8-j9$, $z_1z_2=-1+j41$')
D.PR('Divide with the conjugate', r'Find $\dfrac{10+j5}{3-j4}$ in rectangular form.',
     [S("Multiply top and bottom by $3+j4$, the conjugate of the bottom.", r'\frac{(10+j5)(3+j4)}{(3-j4)(3+j4)}'),
      S("Bottom: $3^2+4^2=25$. Top: expand with $j^2=-1$.", r'(10+j5)(3+j4)=30+j40+j15+j^2\,20=10+j55'),
      S("Divide both the real and the imaginary part by 25.", r'\frac{10+j55}{25}=0.4+j2.2')],
     r'$0.4+j2.2$')
D.PR('Powers of j', r'Simplify (a) $\dfrac1j$ (b) $j^3$ (c) $j^{10}$.',
     [S("(a) Multiply top and bottom by $-j$: the bottom becomes $j(-j)=-j^2=1$.", r'\frac1j=\frac{-j}{1}=-j'),
      S("(b) $j^3=j^2\\cdot j$.", r'j^3=(-1)j=-j'),
      S("(c) The powers of $j$ repeat every 4 ($j, -1, -j, 1$). $10=8+2$, so $j^{10}=j^2$.", r'j^{10}=(j^4)^2j^2=1\cdot(-1)=-1')],
     r'(a) $-j$ (b) $-j$ (c) $-1$')
D.PR('A sixth power', r'Find $(1-j\sqrt3)^6$.',
     [S("Convert: 1 right, $\\sqrt3$ down (4th quadrant).", r'1-j\sqrt3=2\angle-60^\circ'),
      S("de Moivre: length to the 6th, angle times 6.", r'2^6\angle(6\times-60^\circ)=64\angle-360^\circ'),
      S("$-360^\\circ$ is a full turn, pointing along the positive real axis.", r'=64')],
     r'$64$', diff='intermediate')
D.PR('Cube roots', r'Find all three cube roots of $j8$, in polar and rectangular form.',
     [S("Write $j8$ in polar form: 8 straight up.", r'j8=8\angle90^\circ'),
      S("Length $8^{1/3}=2$; first angle $90^\\circ/3=30^\\circ$; spacing $360^\\circ/3=120^\\circ$.", r'2\angle30^\circ,\quad 2\angle150^\circ,\quad 2\angle270^\circ'),
      S("Convert each with $a=c\\cos\\theta$, $b=c\\sin\\theta$.", r'\sqrt3+j,\quad -\sqrt3+j,\quad -j2')],
     r'$2\angle30^\circ=\sqrt3+j$, $2\angle150^\circ=-\sqrt3+j$, $2\angle270^\circ=-j2$', diff='intermediate')
D.PR('Conjugate facts', r'For $z=3-j4$ find $z^*$, $zz^*$, $z+z^*$ and $z-z^*$.',
     [S("The conjugate flips the sign of the imaginary part (mirror image across the real axis).", r'z^*=3+j4'),
      S("A number times its conjugate is $a^2+b^2$ (the $j$ terms cancel), with $a=3$, $b=-4$.", r'zz^*=3^2+(-4)^2=25'),
      S("$z+z^*=2\\,\\mathrm{Re}\\{z\\}$ and $z-z^*=j\\,2\\,\\mathrm{Im}\\{z\\}$ with $\\mathrm{Im}\\{z\\}=-4$.", r'z+z^*=6,\qquad z-z^*=-j8')],
     r'$z^*=3+j4$, $zz^*=25$, $z+z^*=6$, $z-z^*=-j8$')
D.PR('Complex roots of a quadratic', r'Solve $s^2+4s+13=0$.',
     [S("Quadratic formula with $a=1$, $b=4$, $c=13$.", r's=\frac{-4\pm\sqrt{16-52}}{2}=\frac{-4\pm\sqrt{-36}}{2}'),
      S("The number under the root is negative: $\\sqrt{-36}=\\sqrt{36}\\,\\sqrt{-1}=j6$. Then divide both parts by 2.", r's=\frac{-4\pm j6}{2}=-2\pm j3')],
     r'$s=-2\pm j3$')

# ================================================================ Topic 3
D.H('Topic 3: Your first differential equation: the RL natural response', cites=W(5, 6))
D.P("A **differential equation** is an equation that involves an unknown *function* and its *derivatives*. "
    "Solving it means finding the whole function, e.g. the current $i(t)$ at every time $t$.\n\n"
    "Inductors create them because an inductor's voltage depends on how fast its current changes: $v_L=L\\dfrac{di}{dt}$ "
    "($L$ is the *inductance* in henries). Two facts from the lecture that you will use all term:\n\n"
    "- **An inductor's current cannot jump:** $i(0^-)=i(0^+)$ (just before and just after a switch moves).\n"
    "- **In DC steady state an inductor acts like a short circuit** (a plain wire): nothing changes, so $\\dfrac{di}{dt}=0$ and $v_L=0$.\n\n"
    "In the circuit below the switch has been closed for a long time, so the inductor is a short and carries all of $I_s$. "
    "At $t=0$ the switch opens. The inductor's current can't stop instantly, so it keeps flowing round the loop through $R$, "
    "and $R$ slowly burns the energy off. Kirchhoff's voltage law (KVL) around that loop says the voltages add to zero:", cites=W(5, 6))
D.SCH('''I1 0,3 -> 0,0 "$I_s$"
wire 0,3 -> 3,3
R0 3,3 -> 3,0 "$R_0$"
S1 3,3 -> 6,3 "$t=0$" state=closed action=open
L1 6,0 -> 6,3 "$L$" i="$i$"
wire 6,3 -> 9,3
R1 9,3 -> 9,0 "$R$" v="$v$"
wire 0,0 -> 9,0
ground 0,0''', 'Lecture 1, Fig. 1: the switch has been closed for a long time and opens at $t=0$. Afterwards only the loop $L$–$R$ is left, with $i(0)=I_s$.', cites=W(5))
D.EQ(r'L\frac{di}{dt}+Ri=0\quad\Longleftrightarrow\quad \frac{di}{dt}=-\frac{R}{L}\,i', cites=W(5))
D.P("Read it in words: *the current shrinks at a rate proportional to how big it is.* Big current → fast drop; small current → slow drop. "
    "The only function that behaves like that is a **decaying exponential**:", cites=W(6))
D.EQ(r'i(t)=i(0)\,e^{-t/\tau},\qquad \tau=\frac{L}{R}\quad(\text{the time constant, in seconds})', cites=W(6))
D.P("$\\tau$ (tau) is the *time constant*. After one $\\tau$ the current is $e^{-1}\\approx0.37$ of its start (it has lost 63%); "
    "after $5\\tau$ it is under 1%, which engineers call \"done\". A bigger $L$ (more stored energy) or a smaller $R$ (less "
    "resistance to burn it) makes $\\tau$ longer.", cites=W(6))
D.FIG(FIGS['tau'], r'Every RL (and RC) natural response has this one shape. Measure time in time constants: after $1\tau$ 37% is left, after $5\tau$ less than 1%.')
D.CO('tip', "**The method: RL natural response**\n\n"
            "1. **Before the switch** ($t<0$, settled): replace $L$ by a wire and find the inductor current $i(0^-)$.\n"
            "2. **The jump rule:** $i(0^+)=i(0^-)$. Call it $I_0$.\n"
            "3. **After the switch:** find the resistance $R$ the inductor sees (only what is still connected to it).\n"
            "4. Write KVL: $L\\dfrac{di}{dt}+Ri=0$. The solution is $i(t)=I_0e^{-t/\\tau}$ with $\\tau=L/R$.\n"
            "5. Get anything else from $i$: e.g. the resistor voltage $v=Ri$ (sign from the drawn $+/-$ and current arrow).", cites=W(5, 6))
D.CO('info', "**Calculus reminder** (you need these four facts to solve the equation yourself):\n\n"
             "- $\\dfrac{d}{dt}e^{at}=a\\,e^{at}$: the derivative of an exponential is the same exponential times the number in front of $t$.\n"
             "- $\\displaystyle\\int\\frac{dx}{x}=\\ln|x|+C$.\n"
             "- $\\ln A-\\ln B=\\ln\\dfrac AB$.\n"
             "- $\\ln A=B$ means $A=e^B$ (take $e$ to the power of both sides).")

D.EX('Solve the simplest ODE: dy/dt + y = 0', r'Solve $\dfrac{dy}{dt}+y=0$ with $y(0)=y_0$, then check the answer.',
     [S("Move $y$ to the other side so the derivative is alone.", r'\frac{dy}{dt}=-y'),
      S("**Separate the variables**: get everything with $y$ on the left and everything with $t$ on the right (divide by $y$, multiply by $dt$).",
        r'\frac{dy}{y}=-dt'),
      S("Integrate both sides. On the left use $\\int dx/x=\\ln|x|$; only one $+C$ is needed.", r'\ln|y|=-t+C'),
      S("Undo the logarithm by raising $e$ to both sides: $|y|=e^{-t+C}=e^C e^{-t}$. Dropping the absolute value allows either sign, "
        "so $y=\\pm e^{C}e^{-t}$; call the constant $A=\\pm e^{C}$ (it can be positive or negative).", r'y=A\,e^{-t}'),
      S("Use the initial condition: at $t=0$, $e^0=1$, so $A=y_0$.", r'y(t)=y_0\,e^{-t}'),
      S("**Check** by putting it back into the equation: $\\dfrac{dy}{dt}=-y_0e^{-t}$, and adding $y=y_0e^{-t}$ gives 0. ✓",
        r'\frac{dy}{dt}+y=-y_0e^{-t}+y_0e^{-t}=0')],
     r'$y(t)=y_0\,e^{-t}$', cites=W(2, 7))
D.EX('Where the e comes from (lecture outline)', r'Without calculus: why does $\dfrac{dy}{dt}+y=0$ give $y=y_0e^{-t}$? Use a tiny time step $\Delta$.',
     [S("Replace the derivative by a slope over a tiny step $\\Delta$: (value now − value a moment ago) ÷ $\\Delta$.",
        r'\frac{y(t)-y(t-\Delta)}{\Delta}+y(t)\approx0'),
      S("Multiply by $\\Delta$ and rearrange. Each step the value gets divided by $(1+\\Delta)$.", r'y(t)\,(1+\Delta)=y(t-\Delta)'),
      S("Repeat from $t=0$: after $k=t/\\Delta$ steps you have divided by $(1+\\Delta)$ $k$ times.",
        r'y(t)=y(0)\,(1+\Delta)^{-t/\Delta}'),
      S("As the steps get tiny, $(1+\\Delta)^{1/\\Delta}$ approaches the number $e\\approx2.718$ (that is one definition of $e$).",
        r'y(t)=y(0)\Big[(1+\Delta)^{1/\Delta}\Big]^{-t}\;\to\;y(0)\,e^{-t}')],
     r'Shrinking by the same small fraction every instant is exactly what $e^{-t}$ does.', cites=W(2, 7))
D.EX('The general RL loop (Lecture 1)', r'Solve $L\dfrac{di}{dt}+Ri=0$ with $i(0)=I_s$.',
     [S("Divide by $L$ and separate: currents on the left, time on the right.", r'\frac{di}{i}=-\frac{R}{L}\,dt'),
      S("Integrate from the start (time $0$, current $i(0)$) to a general time $t$ (current $i(t)$). Definite integrals mean no $+C$. "
        "($x$ and $s$ are just placeholder names for current and time inside the integrals, so they don't clash with the limits.)",
        r'\int_{i(0)}^{i(t)}\frac{dx}{x}=-\frac{R}{L}\int_0^t ds'),
      S("Evaluate both sides and combine the logs.", r'\ln i(t)-\ln i(0)=\ln\frac{i(t)}{i(0)}=-\frac{R}{L}\,t'),
      S("Exponentiate both sides and multiply by $i(0)=I_s$.", r'i(t)=I_s\,e^{-(R/L)t}=I_s\,e^{-t/\tau},\qquad \tau=\frac{L}{R}')],
     r'$i(t)=I_s\,e^{-t/\tau}$ with $\tau=L/R$', cites=W(5, 6))
D.EX('Pre-tutorial 1: numbers in the RL loop', r'In the circuit above, $L=8\,\mathrm{mH}$, $R=4\,\Omega$ and $I_s=4\,\mathrm{A}$. Find $i(t)$ for $t\ge0$, sketch it, and find $v(t)$.',
     [S("Before the switch opens, the inductor is a short, so it carries the whole source current. The current can't jump.", r'i(0^+)=i(0^-)=I_s=4\,\mathrm{A}'),
      S("After the switch opens, the inductor only sees $R=4\\,\\Omega$ ($R_0$ and the source are cut off). Convert mH to H.",
        r'\tau=\frac{L}{R}=\frac{8\times10^{-3}}{4}=2\times10^{-3}\,\mathrm{s}=2\,\mathrm{ms}'),
      S("$1/\\tau=500\\,\\mathrm{s^{-1}}$, so $e^{-t/\\tau}=e^{-500t}$.", r'i(t)=4\,e^{-500t}\,\mathrm{A},\quad t\ge0'),
      S("The current goes up through $L$ and comes down through $R$ from $+$ to $-$, so $v=Ri$.", r'v(t)=4\cdot4e^{-500t}=16\,e^{-500t}\,\mathrm{V}'),
      S("Sketch points: starts at 4 A, is $4(0.37)=1.47\\,\\mathrm{A}$ at $t=2\\,\\mathrm{ms}$, and is essentially 0 after $5\\tau=10\\,\\mathrm{ms}$ (see the plot).")],
     r'$\tau=2\,\mathrm{ms}$, $i(t)=4e^{-500t}\,\mathrm{A}$, $v(t)=16e^{-500t}\,\mathrm{V}$', cites=D.cite('T1', 1) + W(6))
D.CHART('Pre-tutorial 1: $i(t)=4e^{-500t}$ A for 10 ms. Notice the value $1.47$ A at $t=\\tau=2$ ms (37% of the start) and that by $5\\tau=10$ ms the current is gone. Time is in seconds.',
        order=1, a=-500, y0=4, duration=0.01)
D.EX('How long until it is small?', r'An RL loop has $L=0.5\,\mathrm{H}$, $R=100\,\Omega$ and $i(0)=10\,\mathrm{A}$. When is $i=1\,\mathrm{A}$?',
     [S("Compute $\\tau=L/R$, then write the natural response $i=i(0)e^{-t/\\tau}$; note $1/\\tau=1/0.005=200\\,\\mathrm{s^{-1}}$.", r'\tau=\frac{0.5}{100}=0.005\,\mathrm{s}=5\,\mathrm{ms},\qquad i(t)=10e^{-t/0.005}=10e^{-200t}\,\mathrm{A}'),
      S("Set $i=1$ and isolate the exponential.", r'10e^{-200t}=1\;\Rightarrow\;e^{-200t}=0.1'),
      S("Take $\\ln$ of both sides ($\\ln e^{x}=x$).", r'-200t=\ln0.1=-2.303'),
      S("Solve. A neat shortcut: the time to fall to a fraction $f$ is $\\tau\\ln(1/f)$.", r't=\frac{2.303}{200}=11.5\,\mathrm{ms}=\tau\ln10')],
     r'$t=\tau\ln10\approx11.5\,\mathrm{ms}$')

D.CO('warning', "**Common mistakes**\n\n"
                "- $\\tau=L/R$, not $R/L$. Check units: henries ÷ ohms = seconds.\n"
                "- Using a resistor that is no longer connected after the switch moves (here $R_0$). $R$ is what the inductor sees **after** switching.\n"
                "- Mixing ms and s: convert $L$ in mH to H first, then $\\tau$ comes out in seconds.\n"
                "- Forgetting to check the answer: put $i(t)$ back into $L\\,di/dt+Ri$ and you must get 0, and $i(0)$ must match.")

D.PR('Solve and check', r'Solve $\dfrac{dy}{dt}=-3y$ with $y(0)=5$, and check your answer.',
     [S("Separate the variables: divide both sides by $y$ and multiply by $dt$, so $y$ is on the left and $t$ on the right.", r'\frac{dy}{y}=-3\,dt'),
      S("Integrate both sides ($\\int dy/y=\\ln|y|$, $\\int -3\\,dt=-3t$), add one constant, then raise $e$ to both sides; the constant $A=\\pm e^{C}$ can have either sign.", r'\ln|y|=-3t+C\;\Rightarrow\;|y|=e^{C}e^{-3t}\;\Rightarrow\;y=Ae^{-3t}'),
      S("Use the initial condition: at $t=0$, $e^0=1$, so $y(0)=A=5$.", r'y(t)=5e^{-3t}'),
      S("Check: $\\dfrac{dy}{dt}=-15e^{-3t}=-3(5e^{-3t})=-3y$ ✓ and $y(0)=5$ ✓.")],
     r'$y(t)=5e^{-3t}$')
D.PR('An RL loop with numbers', r'An RL loop has $L=2\,\mathrm{H}$, $R=10\,\Omega$ and $i(0)=3\,\mathrm{A}$. Find $\tau$, $i(t)$ and $i(0.2\,\mathrm{s})$.',
     [S("The time constant of an RL loop is $\\tau=L/R$.", r'\tau=\frac{2}{10}=0.2\,\mathrm{s}'),
      S("The natural response starts at $i(0)=3\\,\\mathrm{A}$ and decays with that $\\tau$; $1/0.2=5$.", r'i(t)=3e^{-t/0.2}=3e^{-5t}\,\mathrm{A}'),
      S("At $t=0.2\\,\\mathrm{s}=\\tau$: 37% of the start.", r'i(0.2)=3e^{-1}=1.10\,\mathrm{A}')],
     r'$\tau=0.2\,\mathrm{s}$, $i(t)=3e^{-5t}\,\mathrm{A}$, $i(0.2)=1.10\,\mathrm{A}$')
D.PR('Work backwards', r'A measured inductor current is $i(t)=6e^{-250t}\,\mathrm{A}$ and the resistor is $R=50\,\Omega$. Find $i(0)$, $\tau$ and $L$.',
     [S("At $t=0$ the exponential is 1.", r'i(0)=6\,\mathrm{A}'),
      S("The exponent is $-t/\\tau$, so $1/\\tau=250$.", r'\tau=\frac{1}{250}=4\,\mathrm{ms}'),
      S("Rearrange $\\tau=L/R$ to get $L=\\tau R$ (time in seconds: $4\\,\\mathrm{ms}=0.004\\,\\mathrm{s}$).", r'L=(0.004)(50)=0.2\,\mathrm{H}')],
     r'$i(0)=6\,\mathrm{A}$, $\tau=4\,\mathrm{ms}$, $L=0.2\,\mathrm{H}$')
D.PR('How many time constants?', r'How many time constants does it take an RL current to fall to 1% of its starting value?',
     [S("1% of the start means the factor $e^{-t/\\tau}$ has dropped to $0.01$ (the starting value cancels).", r'I_0e^{-t/\tau}=0.01\,I_0\;\Rightarrow\;e^{-t/\tau}=0.01'),
      S("Take $\\ln$ of both sides; $\\ln(e^x)=x$ brings the exponent down.", r'-\frac{t}{\tau}=\ln0.01=-4.605'),
      S("So about $4.6\\tau$, which is why \"$5\\tau$\" is used as the rule of thumb for \"finished\".", r't=4.6\,\tau')],
     r'$t=\tau\ln100\approx4.6\,\tau$')
D.PR('The full switching problem', r'In the lecture circuit (switch closed for a long time, opens at $t=0$): $I_s=2\,\mathrm{A}$, $R_0=10\,\Omega$, $L=40\,\mathrm{mH}$, $R=20\,\Omega$. Find $i(t)$ and $v(t)$ for $t\ge0$.',
     [S("Before: the inductor is a short, which also shorts out $R_0$ and $R$, so it carries all of $I_s$.", r'i(0^-)=2\,\mathrm{A}=i(0^+)'),
      S("After: only $R=20\\,\\Omega$ is connected to $L$; $R_0$ plays no part.", r'\tau=\frac{0.04}{20}=2\,\mathrm{ms}'),
      S("The natural response starts at $2\\,\\mathrm{A}$; $1/\\tau=1/0.002=500\\,\\mathrm{s^{-1}}$.", r'i(t)=2e^{-500t}\,\mathrm{A}'),
      S("The current flows down through $R$ from $+$ to $-$, so Ohm's law gives $v=Ri$.", r'v(t)=20\,i=40e^{-500t}\,\mathrm{V}')],
     r'$i(t)=2e^{-500t}\,\mathrm{A}$, $v(t)=40e^{-500t}\,\mathrm{V}$', diff='intermediate')
D.PR('Write the ODE yourself', r'A $0.1\,\mathrm{H}$ inductor carrying $2\,\mathrm{A}$ is suddenly connected across a $5\,\Omega$ resistor at $t=0$. Write the differential equation for $i(t)$ and solve it by separating variables.',
     [S("KVL around the loop: the inductor voltage $L\\,di/dt$ plus the resistor voltage $Ri$ add to zero. Divide by $0.1$.", r'0.1\frac{di}{dt}+5i=0\;\Rightarrow\;\frac{di}{dt}=-50i'),
      S("Separate ($i$ left, $t$ right), integrate both sides, and raise $e$ to both sides; $A=\\pm e^{C}$ is a constant of either sign.", r'\frac{di}{i}=-50\,dt\;\Rightarrow\;\ln|i|=-50t+C\;\Rightarrow\;i=Ae^{-50t}'),
      S("Initial condition $i(0)=2$ gives $A=2$. (Check: $\\tau=L/R=0.02\\,\\mathrm{s}=1/50$ ✓)", r'i(t)=2e^{-50t}\,\mathrm{A}')],
     r'$0.1\,\dfrac{di}{dt}+5i=0$, $i(t)=2e^{-50t}\,\mathrm{A}$', diff='intermediate')

# ================================================================ Mixed practice
D.H('Mixed practice (exam style)')
D.P("Mixed topics, like the midterm. Try each one before opening the solution.")
D.PR('Multiply and divide two ways', r'$z_1=2+j2$ and $z_2=1-j\sqrt3$.' '\n\n'
     r'1. Write both in polar form.' '\n' r'2. Find $z_1z_2$ and $z_1/z_2$ in polar and rectangular form.',
     [S("Convert. $z_1$: 1st quadrant. $z_2$: 1 right, $\\sqrt3$ down, 4th quadrant.", r'z_1=2\sqrt2\angle45^\circ,\qquad z_2=2\angle-60^\circ'),
      S("Product: multiply lengths, add angles.", r'z_1z_2=4\sqrt2\angle-15^\circ=5.657(\cos15^\circ-j\sin15^\circ)=5.464-j1.464'),
      S("Quotient: divide lengths, subtract angles.", r'\frac{z_1}{z_2}=\sqrt2\angle105^\circ=1.414(\cos105^\circ+j\sin105^\circ)=-0.366+j1.366')],
     r'$z_1z_2=5.657\angle-15^\circ=5.464-j1.464$; $z_1/z_2=1.414\angle105^\circ=-0.366+j1.366$', diff='intermediate', label='Practice 1')
D.PR('Solve a cubic', r'Find all solutions of $z^3=-27$.',
     [S("Write $-27$ in polar form: 27 to the left.", r'-27=27\angle180^\circ'),
      S("Length $27^{1/3}=3$; first angle $180^\\circ/3=60^\\circ$; spacing $120^\\circ$.", r'3\angle60^\circ,\quad3\angle180^\circ,\quad3\angle300^\circ'),
      S("Convert each with $a=3\\cos\\theta$, $b=3\\sin\\theta$ ($\\cos60^\\circ=0.5$, $\\sin60^\\circ=0.866$).", r'1.5+j2.598,\qquad -3,\qquad 1.5-j2.598')],
     r'$z=3\angle60^\circ,\ 3\angle180^\circ=-3,\ 3\angle300^\circ$, i.e. $1.5\pm j2.598$ and $-3$', diff='intermediate', label='Practice 2')
D.PR('Double-angle formulas', r'Use $e^{j2\theta}=(e^{j\theta})^2$ to show $\cos2\theta=\cos^2\theta-\sin^2\theta$ and $\sin2\theta=2\sin\theta\cos\theta$.',
     [S("Write both sides with Euler.", r'\cos2\theta+j\sin2\theta=(\cos\theta+j\sin\theta)^2'),
      S("Square the right side with $j^2=-1$.", r'=\cos^2\theta+j2\sin\theta\cos\theta-\sin^2\theta'),
      S("Match real and imaginary parts.", r'\cos2\theta=\cos^2\theta-\sin^2\theta,\qquad \sin2\theta=2\sin\theta\cos\theta')],
     r'Shown by matching real and imaginary parts.', diff='intermediate', label='Practice 3')
D.PR('RL with every question asked', r'In the lecture RL circuit, $I_s=5\,\mathrm{A}$, $L=20\,\mathrm{mH}$ and $R=8\,\Omega$ (the switch opens at $t=0$).' '\n\n'
     r'1. Find $\tau$, $i(t)$ and $v(t)=Ri$.' '\n' r'2. Find $i$ at $t=5\,\mathrm{ms}$.' '\n' r'3. When is $i=1\,\mathrm{A}$?',
     [S("$i(0^+)=i(0^-)=I_s=5\\,\\mathrm{A}$ (inductor was a short).", r'\tau=\frac{0.02}{8}=2.5\,\mathrm{ms}'),
      S("Write the natural response with $1/\\tau=1/0.0025=400\\,\\mathrm{s^{-1}}$; the resistor voltage is $v=Ri$.", r'i(t)=5e^{-400t}\,\mathrm{A},\qquad v(t)=8i=40e^{-400t}\,\mathrm{V}'),
      S("Put $t=0.005\\,\\mathrm{s}$ in (that is $2\\tau$, so the exponent is $-2$).", r'i(0.005)=5e^{-400(0.005)}=5e^{-2}=0.677\,\mathrm{A}'),
      S("Set $5e^{-400t}=1$: divide by 5 to isolate the exponential, take $\\ln$ of both sides ($\\ln\\tfrac15=-\\ln5$), then divide by $-400$.", r'e^{-400t}=\tfrac15\;\Rightarrow\;-400t=-\ln5\;\Rightarrow\;t=\frac{\ln5}{400}=4.02\,\mathrm{ms}')],
     r'$\tau=2.5\,\mathrm{ms}$, $i=5e^{-400t}\,\mathrm{A}$, $v=40e^{-400t}\,\mathrm{V}$; $i(5\,\mathrm{ms})=0.677\,\mathrm{A}$; $t=4.02\,\mathrm{ms}$', diff='intermediate', label='Practice 4')
D.PR("Euler warm-up", r'Evaluate (a) $e^{j\pi}+1$ (b) $|e^{j3}|$ (c) $\mathrm{Re}\{4e^{j\pi/6}\}$.',
     [S("(a) $e^{j\\pi}=\\cos\\pi+j\\sin\\pi=-1$.", r'e^{j\pi}+1=0'),
      S("(b) Every $e^{j\\theta}$ has length 1, whatever $\\theta$ is.", r'|e^{j3}|=1'),
      S("(c) The real part is $c\\cos\\theta$ with $\\theta=\\pi/6=30^\\circ$.", r'4\cos30^\circ=3.464')],
     r'(a) $0$ (b) $1$ (c) $3.464$', label='Practice 5')
D.PR('A messy expression', r'Find $\dfrac{(3+j4)^2}{1-j}$ in rectangular form.',
     [S("Square the top first.", r'(3+j4)^2=9+j24+j^2\,16=-7+j24'),
      S("Divide by $1-j$: multiply top and bottom by $1+j$; the bottom becomes $1+1=2$.", r'\frac{(-7+j24)(1+j)}{2}=\frac{-7-j7+j24+j^2\,24}{2}'),
      S("Simplify with $j^2=-1$.", r'=\frac{-31+j17}{2}=-15.5+j8.5')],
     r'$-15.5+j8.5$', diff='intermediate', label='Practice 6')
D.PR('Roots in polar form', r'Solve $s^2+6s+25=0$ and write both roots in polar form.',
     [S("Quadratic formula with $a=1$, $b=6$, $c=25$; the number under the root is negative.", r's=\frac{-6\pm\sqrt{36-100}}{2}=\frac{-6\pm\sqrt{-64}}{2}'),
      S("$\\sqrt{-64}=\\sqrt{64}\\,\\sqrt{-1}=j8$; divide both parts by 2.", r's=\frac{-6\pm j8}{2}=-3\pm j4'),
      S("$-3+j4$ is in the 2nd quadrant: length 5, reference angle $53.13^\\circ$.", r'-3+j4=5\angle126.87^\circ'),
      S("The other root is the conjugate: same length, angle with the opposite sign (mirror image across the real axis).", r'-3-j4=5\angle-126.87^\circ')],
     r'$s=-3\pm j4=5\angle\pm126.87^\circ$', label='Practice 7')
D.PR('Read the time constant from data', r'In an RL loop with $R=10\,\Omega$, the current is $2\,\mathrm{A}$ at $t=0$ and $0.736\,\mathrm{A}$ at $t=1\,\mathrm{ms}$. Find $\tau$ and $L$.',
     [S("$0.736/2=0.368=e^{-1}$, so 1 ms is exactly one time constant.", r'e^{-0.001/\tau}=0.368\;\Rightarrow\;\tau=1\,\mathrm{ms}'),
      S("Rearrange $\\tau=L/R$ to $L=\\tau R$.", r'L=(0.001)(10)=10\,\mathrm{H}\times10^{-3}=10\,\mathrm{mH}')],
     r'$\tau=1\,\mathrm{ms}$, $L=10\,\mathrm{mH}$', diff='intermediate', label='Practice 8')

# ================================================================ Summary
D.H('Summary')
D.T(['Problem type', 'How to recognise it', 'What to do'], [
    ['Rectangular → polar', 'given $a+jb$, asked for $c\\angle\\theta$ or $ce^{j\\theta}$', 'sketch; $c=\\sqrt{a^2+b^2}$; reference angle; fix the quadrant'],
    ['Polar → rectangular', 'given $c\\angle\\theta$ or $ce^{j\\theta}$', '$a=c\\cos\\theta$, $b=c\\sin\\theta$'],
    ['Add / subtract', '$z_1\\pm z_2$', 'rectangular: add the parts'],
    ['Multiply / divide', '$z_1z_2$, $z_1/z_2$', 'polar: multiply/divide lengths, add/subtract angles (or expand with $j^2=-1$; divide using the conjugate)'],
    ['Power', '$z^k$', 'polar: $c^k\\angle k\\theta$'],
    ['Roots', '$z^{1/k}$ or "solve $z^k=w$"', '$k$ answers: length $c^{1/k}$, angles $\\theta/k+360^\\circ\\ell/k$'],
    ['Trig identity', '"use Euler to show…"', 'write both sides with $e^{j\\theta}=\\cos\\theta+j\\sin\\theta$, expand, match real and imaginary parts'],
    ['RL natural response', 'switch disconnects the source; an inductor is left with a resistor', '$i(0^+)=i(0^-)$ (L = short before); $\\tau=L/R$; $i=I_0e^{-t/\\tau}$'],
])
D.T(['Formula', 'Meaning'], [
    ['$e^{j\\theta}=\\cos\\theta+j\\sin\\theta$', "Euler's identity: the unit-circle point at angle $\\theta$"],
    ['$z\\,z^*=a^2+b^2=c^2$', 'a number times its conjugate is real'],
    ['$L\\dfrac{di}{dt}+Ri=0$', 'KVL for the source-free RL loop'],
    ['$i(t)=I_0e^{-t/\\tau},\\ \\tau=L/R$', '37% left after $\\tau$, under 1% after $5\\tau$'],
    ['time to fall to fraction $f$', '$t=\\tau\\ln(1/f)$'],
])

D.save()
