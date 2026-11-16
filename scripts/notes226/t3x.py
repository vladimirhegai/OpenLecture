r"""Test 3 - Extra: covariance and Gaussian pairs (Lectures 19-20, Tutorial 8).

Moved out of Test 3 - Question 1 on 2026-11-15: the Test 3 announcement does not list them, so they are kept here
for later review. Content is the old Part D, unchanged apart from the intro.
"""
from lib226 import Doc, S, cite

D = Doc('t3x', 'Test 3 - Extra (Covariance & Gaussian)', ['covariance', 'gaussian_pair'])

D.CO('info', r'**Probably not on Test 3.** The test announcement lists marginals, independence and conditional distributions only. These were taught in Lectures 19–20, so they are kept here to review when you have time.')

D.H('Covariance')
D.P(r'**Covariance** answers one question: do $X$ and $Y$ move together?', cites=cite('L19', 7))
D.L([r'$\operatorname{Cov}>0$: big $X$ tends to come with big $Y$.',
     r'$\operatorname{Cov}<0$: big $X$ tends to come with small $Y$.',
     r'$\operatorname{Cov}=0$: no straight-line pattern.'])
D.EQ(r'\operatorname{Cov}[X,Y]=E[XY]-E[X]\,E[Y]', cites=cite('L20', 2))
D.P(r'To get $E[XY]$, multiply each pair $xy$ by its probability, then add (or integrate):')
D.EQ(r'E[XY]=\sum_x\sum_y xy\,p_{X,Y}(x,y)\qquad\qquad E[XY]=\iint xy\,f_{X,Y}(x,y)\,dx\,dy')
D.L([r'If $X$ and $Y$ are independent, then $E[XY]=E[X]E[Y]$, so $\operatorname{Cov}=0$.',
     r'The reverse is **not** true in general. $\operatorname{Cov}=0$ does not prove independent. (Gaussian pairs are the exception.)',
     r'The correlation $\rho=\dfrac{\operatorname{Cov}[X,Y]}{\sigma_X\sigma_Y}$ is the covariance rescaled to sit between $-1$ and $1$.'])
D.EX('Covariance from a table',
     r'''Find $\operatorname{Cov}[X,Y]$.

| | $Y=0$ | $Y=1$ | $Y=2$ |
|---|---|---|---|
| $X=0$ | $0.10$ | $0.15$ | $0.05$ |
| $X=1$ | $0.20$ | $0.30$ | $0.20$ |''',
     [S(r'**$E[XY]$:** only cells with $x\ne0$ and $y\ne0$ matter: $(1,1)$ and $(1,2)$.', r'E[XY]=1\cdot1\cdot0.30+1\cdot2\cdot0.20=0.70'),
      S(r'**Marginals:** $p_X=0.30,\ 0.70$ and $p_Y=0.30,\ 0.45,\ 0.25$.', (r'E[X]=0.70', r'E[Y]=0\cdot0.30+1\cdot0.45+2\cdot0.25=0.95')),
      S(r'**Plug in.**', r'\operatorname{Cov}[X,Y]=0.70-0.70\cdot0.95=0.035')],
     r'$\operatorname{Cov}[X,Y]=0.035$', cites=cite('L19', 6))
D.TRY('Covariance from a density ★ · Lecture 19',
      r'$f_{X,Y}(x,y)=4xy$ on the unit square. Find $E[XY]$ and $\operatorname{Cov}[X,Y]$.',
      [S(r'**$E[XY]$.**', r'E[XY]=\int_0^1\!\!\int_0^1xy\cdot4xy\,dx\,dy=4\cdot\frac13\cdot\frac13=\frac49'),
       S(r'**Means** from the marginals $2x$ and $2y$.', r'E[X]=\int_0^1x\cdot2x\,dx=\frac23=E[Y]'),
       S(r'**Plug in.**', r'\operatorname{Cov}=\frac49-\frac49=0')],
      r'$E[XY]=\tfrac49$, $\operatorname{Cov}=0$ (this pair is independent)', cites=cite('L19', 6))

D.H('Gaussian pairs')
D.P(r'A **jointly Gaussian** pair has a density like a constant times $e^{-(\text{stuff in }x\text{ and }y)}$.', cites=cite('L20', 4))
D.L([r'**No $xy$ term** in the exponent means $\rho=0$, which for a Gaussian pair means **independent**.',
     r'**Read the variances.** Match the $x^2$ term with $\dfrac{x^2}{2\sigma_X^2}$ and the $y^2$ term with $\dfrac{y^2}{2\sigma_Y^2}$. A shifted square $(x-\mu_X)^2$ gives the mean.',
     r'**The constant** is $c=\dfrac{1}{2\pi\,\sigma_X\sigma_Y}$ when $\rho=0$.',
     r'**$Z=aX+bY$** is Gaussian with mean $a\mu_X+b\mu_Y$; for independent $X,Y$ its variance is $a^2\sigma_X^2+b^2\sigma_Y^2$.'])
D.EX('A Gaussian pair ★ (Tutorial 8 Q9)',
     r'$f_{X,Y}(x,y)=c\exp\Big(-2x^2-\dfrac{y^2}{2}\Big)$. (a) Find $c$. (b) Independent? (c) Means and variances. (d) Distribution of $Z=aX+bY$.',
     [S(r'**Match the squares.**', (r'2x^2=\dfrac{x^2}{2\sigma_X^2}\ \Rightarrow\ \sigma_X^2=\dfrac14', r'\dfrac{y^2}2=\dfrac{y^2}{2\sigma_Y^2}\ \Rightarrow\ \sigma_Y^2=1')),
      S(r'(a) **The constant.**', r'c=\frac{1}{2\pi\cdot\frac12\cdot1}=\frac1\pi'),
      S(r'(b) **No $xy$ term** → independent.'),
      S(r'(c) No shifts, so both means are $0$.', r'E[X]=E[Y]=0,\qquad \operatorname{Var}(X)=\frac14,\qquad \operatorname{Var}(Y)=1'),
      S(r'(d) **Combination.**', r'Z\sim N\Big(0,\ \frac{a^2}{4}+b^2\Big)')],
     r'(a) $\tfrac1\pi$ (b) independent (c) $0,\ 0,\ \tfrac14,\ 1$ (d) $N\big(0,\ \tfrac{a^2}4+b^2\big)$', cites=cite('T8', 2) + cite('L20', 4, 6))
D.TRY('Shifted means',
      r'$f_{X,Y}(x,y)=c\exp\Big(-\dfrac{(x-1)^2}{2}-\dfrac{(y+2)^2}{18}\Big)$. Find $c$, the means, the variances, and the distribution of $Z=X+Y$.',
      [S(r'**Match the squares.**', (r'\mu_X=1,\ \sigma_X^2=1', r'\mu_Y=-2,\ \sigma_Y^2=9')),
       S(r'**Constant.**', r'c=\frac{1}{2\pi\cdot1\cdot3}=\frac1{6\pi}'),
       S(r'**$Z=X+Y$:** means add, variances add (independent).', r'Z\sim N(-1,\ 10)')],
      r'$c=\tfrac1{6\pi}$; $1,\,-2$; $1,\,9$; $Z\sim N(-1,10)$')


def verify():
    import sympy as sp
    x, y = sp.symbols('x y', real=True)
    I = sp.integrate
    R = sp.Rational
    assert R(70, 100) - R(70, 100) * R(95, 100) == R(35, 1000)
    assert I(4 * x ** 2 * y ** 2, (x, 0, 1), (y, 0, 1)) == R(4, 9)
    cG = 1 / sp.pi
    assert sp.simplify(I(cG * sp.exp(-2 * x ** 2 - y ** 2 / 2), (x, -sp.oo, sp.oo), (y, -sp.oo, sp.oo)) - 1) == 0
    cS = 1 / (6 * sp.pi)
    assert abs(float(I(cS * sp.exp(-(x - 1) ** 2 / 2 - (y + 2) ** 2 / 18), (x, -sp.oo, sp.oo), (y, -sp.oo, sp.oo))) - 1) < 1e-9
    print('t3x verify ok')


if __name__ == '__main__':
    verify()
    D.save()
