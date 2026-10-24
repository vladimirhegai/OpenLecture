r"""Test 2 - Question 2: continuous random variables, PDFs and probability calculations (Lectures 9-11)."""
from math import exp, log, pi, sqrt

from scipy.stats import norm

from lib226 import Doc, S, cite, num

D = Doc('q2', 'Test 2 - Question 2', ['continuous_random_variables', 'pdf', 'cdf', 'uniform', 'exponential', 'gaussian',
                                      'mixed_random_variables'])


def Phi(z):
    """Standard normal CDF as the lecture table prints it: 4 d.p. below z = 2, 5 d.p. from z = 2."""
    z = round(z, 2)
    return round(norm.cdf(z), 4 if abs(z) < 2 else 5)


def f4(v):
    return f'{v:.4f}'


D.P('**Lectures 9–11.** Continuous random variables, probability density functions (PDFs), probability calculations, '
    'and the uniform, exponential, Gaussian and mixed cases.',
    cites=cite('L9', 3) + cite('L10', 2) + cite('L11', 1))

# =====================================================================================================
D.H('Topic 1: PDFs, CDFs and probability as area')
D.P('Some random quantities (time, voltage, temperature, error) can take **any** value in an interval, not just a list.\n\n'
    'Such an $X$ is **continuous**: probability lives on **intervals**, not on single points.', cites=cite('L9', 3))
D.L([r'**Single points have probability 0.** Pick a number uniformly from $[0,1]$: $P(X=0.3)=0$. It is possible, just "infinitely thin".',
     r'So the CDF $F_X(x)=P(X\le x)$ has **no jumps**: it is a continuous curve rising from $0$ to $1$.',
     r'The **PDF** $f_X(x)$ is a **density** (like kg/m along a bar). It is **not** a probability. Integrate it to get one.'],
    cites=cite('L9', 4))
D.EQ(r'P(a<X\le b)=\int_a^b f_X(x)\,dx=\text{area under } f_X \text{ from } a \text{ to } b', cites=cite('L9', 8))
D.P('**The rules of a PDF** (memorise, no formula sheet):')
D.L([r'**Never negative:** $f_X(x)\ge0$ (it *can* be bigger than 1).',
     r'**Total area 1:** $\displaystyle\int_{-\infty}^{\infty}f_X(x)\,dx=1$. Use this to find an unknown constant $c$.',
     r'**PDF → CDF:** $F_X(x)=\displaystyle\int_{-\infty}^{x}f_X(t)\,dt$ (area to the left of $x$).',
     r'**CDF → PDF:** $f_X(x)=\dfrac{d}{dx}F_X(x)$ (slope of the CDF).',
     r'**Endpoints don’t matter:** $P(a<X<b)=P(a\le X\le b)$, because $P(X=a)=0$.',
     r'**Right tail:** $P(X>a)=1-F_X(a)$.'], cites=cite('L9', 8))
D.REMIND(r'''**Calculus you need here**

- **Power rule:** $\displaystyle\int x^n\,dx=\frac{x^{n+1}}{n+1}$, e.g. $\displaystyle\int x^2\,dx=\frac{x^3}{3}$, $\displaystyle\int 1\,dx=x$.
- **Exponential:** $\displaystyle\int e^{-\lambda x}\,dx=-\frac{1}{\lambda}e^{-\lambda x}$, and $e^{-\lambda x}\to0$ as $x\to\infty$.
- **Definite integral:** $\displaystyle\int_a^b f(x)\,dx=G(b)-G(a)$, where $G$ is the antiderivative.
- **Piecewise $f$:** split the integral at every break point. Pieces where $f=0$ add nothing.
- **Derivatives** (CDF → PDF): $\dfrac{d}{dx}x^n=nx^{n-1}$, $\dfrac{d}{dx}e^{-\lambda x}=-\lambda e^{-\lambda x}$, constants → $0$.''')
D.P('**How to solve a "given a PDF" question:**')
D.L(['**Sketch** $f_X$: where is it non-zero? This tells you the limits.',
     '**Constant:** set the total area equal to 1.',
     '**CDF:** integrate from the left end up to $x$, one piece at a time (0 before the start, 1 after the end).',
     '**Probabilities:** area between the limits, or $F_X(b)-F_X(a)$.'], ordered=True)
D.GRAPH(['title "Probability = shaded area under the PDF $f_X(x)=x/2$ on $[0,2]$"',
         'x -0.5 2.5 label="$x$" height=250', 'y 0 1.2 label="$f_X(x)$"',
         'slider A -0.5 2.5 0.5 step=0.05 label="$a$"', 'slider B -0.5 2.5 1.5 step=0.05 label="$b$"',
         'curve "0" from=-0.5 to=0 color=1', 'curve "x/2" from=0 to=2 color=1 label="$f_X(x)$"', 'curve "0" from=2 to=2.5 color=1',
         'segment "2" "0" "2" "1" color=1 dash',
         'region "(x>A)*(x<B)*(y>0)*(y<(x>0)*(x<2)*x/2)" color=2',
         'readout "$P(a<X<b)$" "max(min(max(B,0),2)^2-min(max(A,0),2)^2,0)/4"',
         'readout "$F_X(b)$" "min(max(B,0),2)^2/4"'],
        intro='Drag $a$ and $b$: the shaded area **is** the probability. Here $F_X(x)=x^2/4$ on $[0,2]$.')
D.EX('Reading a continuous CDF',
     r'''$X$ has CDF

$$
F_X(x)=\begin{cases}0,&x<0\\ x/4,&0\le x\le4\\ 1,&x>4\end{cases}
$$

Find (a) $P(X\le-1)$, (b) $P(X\le1)$, (c) $P(2<X\le3)$, (d) $P(X>1)$, (e) $P(X=1)$, and the PDF.''',
     [S('(a) Left of 0 the CDF is 0.', r'P(X\le-1)=F_X(-1)=0'),
      S('(b) Read the CDF directly.', r'P(X\le1)=F_X(1)=\tfrac14'),
      S('(c) **Difference** of the CDF.', r'P(2<X\le3)=F_X(3)-F_X(2)=\tfrac34-\tfrac24=\tfrac14'),
      S('(d) **Right tail.**', r'P(X>1)=1-F_X(1)=1-\tfrac14=\tfrac34'),
      S(r'(e) **A single point** of a continuous $X$: squeeze it into $(1-\varepsilon,1]$, whose probability $\varepsilon/4\to0$.',
        r'P(X=1)\le F_X(1)-F_X(1-\varepsilon)=\tfrac{\varepsilon}{4}\to0\;\Rightarrow\;P(X=1)=0'),
      S('**PDF** = slope of the CDF: $\\tfrac14$ on $[0,4]$, $0$ elsewhere (a uniform $X$).',
        r'f_X(x)=\frac{d}{dx}\frac{x}{4}=\tfrac14,\quad 0\le x\le4')],
     r'(a) $0$ (b) $\tfrac14$ (c) $\tfrac14$ (d) $\tfrac34$ (e) $0$; $f_X=\tfrac14$ on $[0,4]$.', cites=cite('L9', 5))
p1q = 79 / 128
D.TRY('Find $c$, the CDF, and a probability',
      r'''$X$ has PDF $f_X(x)=c(1-x^4)$ for $-1\le x\le1$, and $0$ otherwise.
(a) Find $c$. (b) Find the CDF. (c) Find $P(|X|<\tfrac12)$.''',
      [S('(a) **Total area 1.** Power rule.', r'c\int_{-1}^{1}(1-x^4)\,dx=c\left[x-\frac{x^5}{5}\right]_{-1}^{1}=c\left(\frac45+\frac45\right)=\frac{8c}{5}=1'),
       S('So:', r'c=\tfrac58'),
       S(r'(b) **CDF** for $-1\le x\le1$: integrate from the left end $-1$ to $x$.',
         r'F_X(x)=\frac58\left[t-\frac{t^5}{5}\right]_{-1}^{x}=\frac58\left(x-\frac{x^5}{5}+\frac45\right)'),
       S('With the outside pieces:', r'F_X(x)=\begin{cases}0,&x<-1\\ \frac58\left(x-\frac{x^5}{5}+\frac45\right),&-1\le x\le1\\ 1,&x>1\end{cases}'),
       S('(c) $|X|<\\tfrac12$ means $-\\tfrac12<X<\\tfrac12$. The PDF is symmetric, so take twice the area on $[0,\\tfrac12]$.',
         r'P(|X|<\tfrac12)=2\cdot\frac58\left[x-\frac{x^5}{5}\right]_0^{1/2}=\frac54\left(\frac12-\frac1{160}\right)=\frac{79}{128}'),
       S('As a decimal:', r'\frac{79}{128}\approx ' + f4(p1q))],
      r'$c=\tfrac58$; $F_X(x)=\tfrac58\left(x-\tfrac{x^5}{5}+\tfrac45\right)$ on $[-1,1]$; $P(|X|<\tfrac12)=\tfrac{79}{128}\approx' + f4(p1q) + '$',
      cites=cite('P2', 1))
D.TRY('A triangle PDF',
      r'''Sketch $f(x)=\tfrac12-\tfrac14|x-3|$ for $1\le x\le5$ ($0$ otherwise). (a) Show it is a PDF. (b) Find its CDF $F$ and show $F$ is continuous. (c) Find $P(2<X<4)$.''',
      [S('(a) **Sketch:** a triangle with peak $\\tfrac12$ at $x=3$, falling to $0$ at $x=1$ and $x=5$. It is $\\ge0$ there.',
         r'f(1)=0,\quad f(3)=\tfrac12,\quad f(5)=0'),
       S('**Area** of the triangle = $\\tfrac12\\cdot$base$\\cdot$height.', r'\tfrac12\cdot4\cdot\tfrac12=1\;\checkmark'),
       S('(b) **Left piece** $1\\le x\\le3$: here $|x-3|=3-x$, so $f(t)=\\tfrac{t-1}{4}$.',
         r'F(x)=\int_1^x\frac{t-1}{4}\,dt=\frac{(x-1)^2}{8}'),
       S('**Right piece** $3\\le x\\le5$: the area still missing is a small triangle on $[x,5]$, by symmetry.',
         r'F(x)=1-\frac{(5-x)^2}{8}'),
       S('**Continuous:** both pieces give $\\tfrac12$ at $x=3$; $F(1)=0$ and $F(5)=1$ match the outside pieces.',
         r'\frac{(3-1)^2}{8}=\frac12=1-\frac{(5-3)^2}{8}'),
       S('(c) Use $F(4)-F(2)$.', r'P(2<X<4)=\left(1-\frac18\right)-\frac18=\frac34')],
      r'Area $=1$; $F=\tfrac{(x-1)^2}{8}$ on $[1,3]$, $1-\tfrac{(5-x)^2}{8}$ on $[3,5]$ ($0$ before, $1$ after); $P(2<X<4)=\tfrac34$.',
      cites=cite('T4', 1))

# =====================================================================================================
D.H('Topic 2: Uniform and exponential')
D.P('Two named continuous families. **Memorise** both PDFs and CDFs.')
D.P('**Uniform$(a,b)$:** every value in $[a,b]$ is equally likely, so the PDF is flat.', cites=cite('L10', 2))
D.EQ(r'f_X(x)=\begin{cases}\dfrac{1}{b-a},&a\le x\le b\\ 0,&\text{otherwise}\end{cases}\qquad F_X(x)=\begin{cases}0,&x<a\\ \dfrac{x-a}{b-a},&a\le x\le b\\ 1,&x>b\end{cases}',
     cites=cite('L10', 3))
D.L([r'The height $\frac1{b-a}$ is forced: the rectangle must have area 1.',
     r'**Shortcut:** probability = (length of the part inside $[a,b]$) ÷ (total length $b-a$).'])
D.P('**Exponential$(\\lambda)$:** waiting times and lifetimes. $\\lambda>0$ is the rate.', cites=cite('L10', 4))
D.EQ(r'f_X(x)=\lambda e^{-\lambda x}\ (x\ge0),\qquad F_X(x)=1-e^{-\lambda x}\ (x\ge0)')
D.EQ(r'P(X>x)=e^{-\lambda x}')
D.L([r'Both are $0$ for $x<0$ (a lifetime can’t be negative).',
     r'**Tail formula** $P(X>x)=e^{-\lambda x}$ is the one you’ll use most.',
     r'**Interval:** $P(s<X<t)=e^{-\lambda s}-e^{-\lambda t}$.'])
D.REMIND(r'''**Conditional probability (Test 1):** $P(A\mid B)=\dfrac{P(A\cap B)}{P(B)}$.

If $A$ is inside $B$ (e.g. $\{X>20\}\subset\{X>10\}$), then $A\cap B=A$, so $P(A\mid B)=\dfrac{P(A)}{P(B)}$.''', cites=cite('L4', 1))
D.P('**Memoryless property** (exponential only): having already waited $s$ doesn’t change the future.')
D.EQ(r'P(X>s+t\mid X>s)=\frac{e^{-\lambda(s+t)}}{e^{-\lambda s}}=e^{-\lambda t}=P(X>t)')
D.GRAPH(['title "Exponential PDF: the shaded tail is $P(X>t)=e^{-\\lambda t}$"',
         'x 0 6 label="$x$" height=250', 'y 0 2.2 label="$f_X(x)$"',
         'slider L 0.2 2 1 step=0.05 label="$\\lambda$"', 'slider T 0 5 1 step=0.05 label="$t$"',
         'curve "L*exp(-L*x)" from=0 to=6 color=1 label="$\\lambda e^{-\\lambda x}$"',
         'region "(x>T)*(y>0)*(y<L*exp(-L*x))" color=2',
         'readout "$P(X>t)$" "exp(-L*T)"', 'readout "$F_X(t)$" "1-exp(-L*T)"'],
        intro='Bigger $\\lambda$ = a taller start and a faster drop = shorter waits.')
pl = exp(-1)
D.EX('Component lifetime',
     r'The lifetime $X$ (hours) of a component is exponential with $\lambda=0.002$. Find the probability it works for **at least 500 hours**.',
     [S('**Family:** exponential → use the tail formula.', r'P(X\ge500)=P(X>500)=e^{-\lambda\cdot500}'),
      S('Or from the PDF, to see where it comes from:', r'\int_{500}^{\infty}0.002e^{-0.002x}\,dx=\Big[-e^{-0.002x}\Big]_{500}^{\infty}=0+e^{-1}'),
      S('Evaluate.', r'e^{-0.002\cdot500}=e^{-1}\approx ' + f4(pl))],
     r'$e^{-1}\approx ' + f4(pl) + '$', cites=cite('L10', 4))
D.TRY('Waiting for the bus',
      'A bus arrives at a random time, uniform between 1:00 and 1:30 P.M. You arrive at 1:00. Find the probability you wait **at least 10 minutes**.',
      [S('**Family:** $X$ = minutes after 1:00, Uniform$(0,30)$.', r'f_X(x)=\tfrac1{30},\quad 0\le x\le30'),
       S('Waiting $\\ge10$ minutes means the bus comes at $X\\ge10$. **Length ratio.**', r'P(X\ge10)=\frac{30-10}{30}=\frac23')],
      r'$\tfrac23$', diff='introductory', cites=cite('T2', 1))
D.TRY('Sine beats cosine',
      r'A number $X$ is chosen uniformly from $[0,\tfrac{\pi}{2}]$. Find $P(\sin X>\cos X)$.',
      [S('**Turn the event into an interval.** On $[0,\\tfrac{\\pi}{2}]$, $\\sin x>\\cos x$ exactly when $x>\\tfrac{\\pi}{4}$ (they cross at $45^\\circ$).',
         r'\{\sin X>\cos X\}=\{X>\tfrac{\pi}{4}\}'),
       S('**Length ratio.**', r'P=\frac{\pi/2-\pi/4}{\pi/2}=\frac12')],
      r'$\tfrac12$', cites=cite('T3', 1))
D.TRY('Old TV still working',
      r'A TV tube’s lifetime (years) is exponential with $\lambda=0.1$. The TV is already 10 years old. Find the probability the tube lasts **another 10 years**.',
      [S('**Conditional:** we want $P(X>20\\mid X>10)$. $\\{X>20\\}$ is inside $\\{X>10\\}$.',
         r'P(X>20\mid X>10)=\frac{P(X>20)}{P(X>10)}=\frac{e^{-2}}{e^{-1}}=e^{-1}'),
       S('**Memoryless:** same as a brand-new tube lasting 10 years.', r'P(X>10)=e^{-0.1\cdot10}=e^{-1}\approx ' + f4(pl))],
      r'$e^{-1}\approx ' + f4(pl) + '$ (the 10 years already used don’t matter)', cites=cite('T4', 1))
D.TRY('Catching a flight',
      'Flights leave every half hour starting at 5:00 A.M. (so 9:00, 9:30, 10:00, …). A passenger arrives at a uniform random time between 8:45 and 9:45 A.M. '
      'Find the probability she waits (a) **at most 10 minutes**, (b) **at least 15 minutes**.',
      [S('**Family:** $T$ = minutes after 8:45, Uniform$(0,60)$. Flights leave at $T=15,\\ 45,\\ 75$.', r'f_T(t)=\tfrac1{60},\quad 0\le t\le60'),
       S('(a) Wait $\\le10$: arrive in the 10 minutes before a flight.', r'T\in[5,15]\cup[35,45]\;\Rightarrow\;P=\frac{10+10}{60}=\frac13'),
       S('(b) Wait $\\ge15$: the next flight is at least 15 minutes away.', r'T\in[15,30]\cup[45,60]\;\Rightarrow\;P=\frac{15+15}{60}=\frac12')],
      r'(a) $\tfrac13$ (b) $\tfrac12$', cites=cite('T4', 1))

# =====================================================================================================
D.H('Topic 3: Gaussian (normal) random variables')
D.P('The bell curve: noise, measurement error, sums of many small effects. $X\\sim N(\\mu,\\sigma^2)$.', cites=cite('L10', 5))
D.EQ(r'f_X(x)=\frac{1}{\sqrt{2\pi\sigma^2}}\,e^{-(x-\mu)^2/(2\sigma^2)}', cites=cite('L10', 5))
D.L([r'$\mu$ = the **centre** of the bell (any real number).',
     r'$\sigma>0$ = the **width**: small $\sigma$ → narrow and tall, large $\sigma$ → wide and flat.',
     r'Symmetric about $\mu$, so $P(X\le\mu)=\tfrac12$.',
     r'This PDF has **no antiderivative** you can write down. That is why we use a table.'])
D.P('**Standard normal** $Z\\sim N(0,1)$: its CDF has a name, $\\Phi(z)=P(Z\\le z)$, and is printed in a table (Lecture 10/11).',
    cites=cite('L11', 1))
D.EQ(r'F_X(x)=\Phi\!\left(\frac{x-\mu}{\sigma}\right)\qquad\text{and}\qquad \Phi(-z)=1-\Phi(z)', cites=cite('L11', 1))
D.P('**Recipe** (the skill tested is standardising; $\\Phi$ values come from the table):')
D.L([r'**Standardise:** $z=\dfrac{x-\mu}{\sigma}$ ("how many $\sigma$’s from the centre").',
     r'**Rewrite with $\le$:** $P(X>x)=1-\Phi(z)$, $\;P(a<X<b)=\Phi(z_b)-\Phi(z_a)$.',
     r'**Negative $z$:** the table has only $z\ge0$, so use $\Phi(-z)=1-\Phi(z)$.',
     r'**Symmetric interval:** $P(|X-\mu|<k\sigma)=2\Phi(k)-1$.',
     r'**Backwards** (given a probability, find $x$): find $z$ in the table, then $x=\mu+z\sigma$.'], ordered=True)
D.T(['$z$', '0.5', '1.0', '1.28', '1.5', '1.645', '1.96', '2.0', '2.5'],
    [['$\\Phi(z)$', f4(Phi(.5)), f4(Phi(1)), f4(Phi(1.28)), f4(Phi(1.5)), '0.95', f4(Phi(1.96)), f'{Phi(2):.5f}', f'{Phi(2.5):.5f}']],
    cites=cite('L10', 6))
D.CO('tip', r'**Handy landmarks:** $\Phi(1.28)\approx0.90$ (top 10%), $\Phi(1.645)\approx0.95$ (between the table’s 1.64 and 1.65), '
            r'$\Phi(1.96)=0.975$ (middle 95%). About 68% of values lie within $1\sigma$ of $\mu$, 95% within $2\sigma$.')
# Abramowitz-Stegun 7.1.26 erf, written in the graph's expression language
ERF = '1-((((1.061405429*{t}-1.453152027)*{t}+1.421413741)*{t}-0.284496736)*{t}+0.254829592)*{t}*exp(-{z}^2)'
D.GRAPH(['title "Normal PDF: slide $\\mu$, $\\sigma$ and the interval $[a,b]$"',
         'x -6 6 label="$x$" height=260', 'y 0 1.02 label="$f_X(x)$"',
         'slider M -3 3 0 step=0.1 label="$\\mu$"', 'slider S 0.4 3 1 step=0.05 label="$\\sigma$"',
         'slider A -6 6 -1 step=0.05 label="$a$"', 'slider B -6 6 1 step=0.05 label="$b$"',
         'let za "(A-M)/(S*sqrt(2))"', 'let zb "(B-M)/(S*sqrt(2))"',
         'let ta "1/(1+0.3275911*abs(za))"', 'let tb "1/(1+0.3275911*abs(zb))"',
         'let ea "sign(za)*(' + ERF.format(t='ta', z='za') + ')"', 'let eb "sign(zb)*(' + ERF.format(t='tb', z='zb') + ')"',
         'curve "exp(-(x-M)^2/(2*S^2))/(S*sqrt(2*pi))" from=-6 to=6 color=1 label="$f_X(x)$"',
         'vline "M" color=1',
         'region "(x>A)*(x<B)*(y>0)*(y<exp(-(x-M)^2/(2*S^2))/(S*sqrt(2*pi)))" color=2',
         'readout "$z_a=(a-\\mu)/\\sigma$" "(A-M)/S"', 'readout "$z_b$" "(B-M)/S"',
         'readout "$P(a<X<b)=\\Phi(z_b)-\\Phi(z_a)$" "max(0.5*(eb-ea),0)"'],
        intro='Only the $z$-values matter: shift $\\mu$ and the interval together, or scale $\\sigma$ and the interval together, and the area stays the same.')
pz = 2 * Phi(1.6) - 1
D.EX('Sensor measurement error',
     r'A temperature sensor’s error $X$ (°C) is Gaussian with $\mu=0$, $\sigma=0.5$. The sensor is accurate enough if $|X|<0.8$. Find the probability of that.',
     [S('**Rewrite** the event as an interval.', r'P(|X|<0.8)=P(-0.8<X<0.8)=F_X(0.8)-F_X(-0.8)'),
      S('**Standardise** both ends.', r'z=\frac{\pm0.8-0}{0.5}=\pm1.6\;\Rightarrow\;\Phi(1.6)-\Phi(-1.6)'),
      S('**Negative $z$:** $\\Phi(-1.6)=1-\\Phi(1.6)$.', r'\Phi(1.6)-\big(1-\Phi(1.6)\big)=2\Phi(1.6)-1'),
      S('**Table:** $\\Phi(1.6)=' + f4(Phi(1.6)) + '$.', r'2(' + f4(Phi(1.6)) + r')-1=' + f4(pz))],
     r'$2\Phi(1.6)-1=' + f4(pz) + '$', cites=cite('L11', 3))
D.TRY('Top 10% of a test',
      r'Scores are normal with $\mu=500$, $\sigma=100$. What score puts a student in the **top 10%**?',
      [S('**Backwards question:** find $x$ with $P(X\\le x)=0.90$.', r'\Phi\!\left(\frac{x-500}{100}\right)=0.90'),
       S('**Table:** $\\Phi(1.28)=' + f4(Phi(1.28)) + '$ and $\\Phi(1.29)=' + f4(Phi(1.29)) + '$, so $z\\approx1.28$.', r'z\approx1.28'),
       S('**Un-standardise:** $x=\\mu+z\\sigma$.', r'x=500+1.28(100)=628')],
      r'About $628$ or more.', cites=cite('T4', 1))
r1 = Phi(round(1 / 1.5, 2))
r5 = 1 - norm.cdf(5 / 1.5)
D.TRY('Rover distance estimate',
      r'A rover’s distance travelled is $X\sim N(\mu,\sigma^2)$ with $\mu=500$ m and $\sigma^2=2.25$ m². Find (a) $P(X<500)$, (b) $P(X=501)$, (c) $P(X>501)$ and $P(X>505)$.',
      [S('**Careful:** the variance is given, so $\\sigma=\\sqrt{2.25}=1.5$.', r'\sigma=1.5'),
       S('(a) $500=\\mu$: half the bell is below the centre.', r'P(X<500)=\Phi(0)=0.5'),
       S('(b) A single point of a continuous $X$.', r'P(X=501)=0'),
       S('(c) Standardise: $z=\\tfrac{1}{1.5}\\approx0.67$.', r'P(X>501)=1-\Phi(0.67)=1-' + f4(r1) + '=' + f4(1 - r1)),
       S('$z=\\tfrac{5}{1.5}\\approx3.33$ is past the end of the table ($\\Phi\\approx1$).', r'P(X>505)=1-\Phi(3.33)\approx ' + f4(r5))],
      r'(a) $0.5$ (b) $0$ (c) $\approx' + f4(1 - r1) + r'$ and $\approx' + f4(r5) + '$', cites=cite('T6', 1))
b95, b89 = Phi(round(15 / 7, 2)), Phi(round(9 / 7, 2))
D.TRY('Blood pressure',
      r'Diastolic blood pressure is normal with $\mu=80$, $\sigma=7$ (mm Hg). $\ge95$ is hypertensive; strictly between $89$ and $95$ is mild hypertension. '
      'What percent of people are in each group?',
      [S('**Standardise** both cut-offs (round to the table’s 2 decimals).', r'z_{95}=\frac{95-80}{7}\approx2.14,\qquad z_{89}=\frac{89-80}{7}\approx1.29'),
       S('**Hypertensive:** right tail.', r'P(X\ge95)=1-\Phi(2.14)=1-' + f'{b95:.5f}' + '=' + f'{1 - b95:.5f}'),
       S('**Mild:** between the two.', r'\begin{gathered}P(89<X<95)=\Phi(2.14)-\Phi(1.29)\\ =' + f'{b95:.5f}' + '-' + f4(b89) + '=' + f'{b95 - b89:.4f}' + r'\end{gathered}')],
      f'Mild ≈ {100 * (b95 - b89):.2f}%, hypertensive ≈ {100 * (1 - b95):.2f}%', cites=cite('P3', 3))

# =====================================================================================================
D.H('Topic 4: Mixed random variables')
D.P('A **mixed** $X$ has a **point with positive probability** (a jump in the CDF) **plus** a continuous part (a sloped CDF).',
    cites=cite('L10', 8))
D.L([r'**Spot it:** the story has "with probability $q$ it is exactly $x_0$, otherwise it is spread over an interval".',
     r'**The jump:** $P(X=x_0)$ = size of the jump in $F_X$ at $x_0$.',
     r'**The continuous part:** its density is scaled by the leftover probability, so its area is $1-q$, not 1.',
     r'**Probability of an interval** = (point masses inside it) + (area of the continuous part over it).'])
D.EX('Received signal level',
     r'A receiver loses the signal completely with probability $0.2$, so $P(X=0)=0.2$. Otherwise (probability $0.8$) the level $X$ is uniform on $(0,10)$. '
     r'(a) Find $P(2<X<5)$. (b) Find and sketch the CDF.',
     [S('**Continuous part:** uniform on $(0,10)$, scaled by $0.8$.', r'f(x)=0.8\cdot\tfrac1{10}=0.08,\quad 0<x<10'),
      S('(a) The point $X=0$ is **not** in $(2,5)$, so only area counts.', r'P(2<X<5)=\int_2^5 0.08\,dx=0.08\cdot3=0.24'),
      S('(b) **CDF:** $0$ before $0$; **jump of $0.2$** at $0$; then rises with slope $0.08$; reaches $1$ at $10$.',
        r'F_X(x)=\begin{cases}0,&x<0\\ 0.2+0.08x,&0\le x<10\\ 1,&x\ge10\end{cases}'),
      S('Check: at $x=10$, $0.2+0.8=1$. ✓', r'F_X(10)=1')],
     r'(a) $0.24$ (b) jump $0.2$ at $0$, then a straight ramp up to $1$ at $x=10$.', cites=cite('L11', 4) + cite('L11', 5))
D.GRAPH(['title "CDF of the received signal: a jump, then a ramp"', 'x -2 12 label="$x$" height=230', 'y 0 1.1 label="$F_X(x)$"',
         'segment "-2" "0" "0" "0" color=2', 'segment "0" "0.2" "10" "1" color=2', 'segment "10" "1" "12" "1" color=2',
         'point "0" "0.2" color=2', 'segment "0" "0" "0" "0.2" color=0 dash', 'text "1.6" "0.12" "jump $=0.2$"',
         'text "6.8" "0.6" "slope $0.08$"'],
        intro='A discrete $X$ is all jumps, a continuous $X$ is all slope, a mixed $X$ has both.')

# =====================================================================================================
D.H('Practice Questions')
D.P('Test-style questions for Question 2, roughly easy → hard. Solve on paper first, then open the solution.')

D.Q('Uniform voltage',
    r'A voltage $X$ is uniform on $[-2,3]$ V. Find (a) the PDF and CDF, (b) $P(|X|<1)$, (c) $P(X>2\mid X>0)$.',
    [S('(a) **Uniform$(-2,3)$:** height $\\tfrac1{5}$.', r'f_X(x)=\tfrac15\ (-2\le x\le3),\qquad F_X(x)=\frac{x+2}{5}\ (-2\le x\le3)'),
     S('(b) $|X|<1$ is $(-1,1)$, length 2, inside $[-2,3]$.', r'P(|X|<1)=\frac{2}{5}'),
     S('(c) **Conditional**, and $\\{X>2\\}\\subset\\{X>0\\}$.', r'P(X>2\mid X>0)=\frac{P(X>2)}{P(X>0)}=\frac{1/5}{3/5}=\frac13')],
    r'$f=\tfrac15$, $F=\tfrac{x+2}{5}$ on $[-2,3]$; (b) $\tfrac25$ (c) $\tfrac13$', diff='introductory')

lam = 0.05
e30, med, e1030 = exp(-1.5), log(2) / lam, exp(-0.5) - exp(-1.5)
D.Q('Battery lifetime',
    r'A battery’s lifetime $X$ (hours) is exponential with $\lambda=0.05$. Find (a) $P(X>30)$, (b) $P(10<X<30)$, (c) the **median** $m$ (the time with $P(X\le m)=\tfrac12$).',
    [S('(a) **Tail formula.**', r'P(X>30)=e^{-0.05\cdot30}=e^{-1.5}\approx ' + f4(e30)),
     S('(b) **Difference of tails.**', r'P(10<X<30)=e^{-0.5}-e^{-1.5}\approx ' + f4(e1030)),
     S('(c) Set the CDF to $\\tfrac12$ and take $\\ln$ of both sides.', r'1-e^{-0.05m}=\tfrac12\;\Rightarrow\;e^{-0.05m}=\tfrac12\;\Rightarrow\;-0.05m=\ln\tfrac12'),
     S('Solve ($\\ln\\tfrac12=-\\ln2$).', r'm=\frac{\ln2}{0.05}\approx ' + f'{med:.2f}' + r'\text{ h}')],
    f'(a) $\\approx {f4(e30)}$ (b) $\\approx {f4(e1030)}$ (c) $m=\\ln 2/0.05\\approx {med:.2f}$ h')

D.Q('Power-law PDF',
    r'$X$ has PDF $f_X(x)=kx^2$ for $0\le x\le3$, $0$ otherwise. Find (a) $k$, (b) the CDF, (c) $P(1<X<2)$, (d) the value $a$ with $P(X\le a)=\tfrac18$.',
    [S('(a) **Total area 1.**', r'k\int_0^3x^2\,dx=k\cdot\frac{27}{3}=9k=1\;\Rightarrow\;k=\tfrac19'),
     S('(b) **CDF** on $[0,3]$.', r'F_X(x)=\int_0^x\frac{t^2}{9}\,dt=\frac{x^3}{27}\quad(0\le x\le3),\quad 0\text{ before},\ 1\text{ after}'),
     S('(c) $F(2)-F(1)$.', r'P(1<X<2)=\frac{8-1}{27}=\frac{7}{27}'),
     S('(d) Solve $F(a)=\\tfrac18$.', r'\frac{a^3}{27}=\frac18\;\Rightarrow\;a^3=\frac{27}{8}\;\Rightarrow\;a=\frac32')],
    r'(a) $\tfrac19$ (b) $\tfrac{x^3}{27}$ on $[0,3]$ (c) $\tfrac7{27}$ (d) $a=1.5$')

lp1, lp2 = exp(-2) / 2, 1 - exp(-1)
D.Q('Two-sided exponential',
    r'$X$ has PDF $f_X(x)=c\,e^{-2|x|}$ for all real $x$. Find (a) $c$, (b) $P(X>1)$, (c) $P(|X|<0.5)$.',
    [S('(a) **Symmetric:** total area = twice the area on $[0,\\infty)$.', r'2c\int_0^{\infty}e^{-2x}\,dx=2c\cdot\frac12=c=1'),
     S('(b) Only the right side.', r'P(X>1)=\int_1^{\infty}e^{-2x}\,dx=\frac{e^{-2}}{2}\approx ' + f4(lp1)),
     S('(c) Twice the area on $[0,0.5]$.', r'P(|X|<0.5)=2\int_0^{0.5}e^{-2x}\,dx=1-e^{-1}\approx ' + f4(lp2))],
    f'(a) $c=1$ (b) $\\approx {f4(lp1)}$ (c) $\\approx {f4(lp2)}$')

ra, rb = exp(-0.5) - exp(-2), exp(-4.5)
D.Q('Rayleigh · Practice 02 Q4',
    r'''$R$ has CDF

$$
F_R(r)=\begin{cases}0,&r<0\\ 1-e^{-r^2/(2\sigma^2)},&r\ge0\end{cases}
$$

Find $P(\sigma\le R\le2\sigma)$ and $P(R>3\sigma)$.''',
    [S('**Difference of the CDF** (continuous, so endpoints don’t matter).', r'P(\sigma\le R\le2\sigma)=F_R(2\sigma)-F_R(\sigma)=e^{-1/2}-e^{-2}\approx ' + f4(ra)),
     S('**Right tail.** $\\sigma$ cancels: $\\tfrac{(3\\sigma)^2}{2\\sigma^2}=\\tfrac92$.', r'P(R>3\sigma)=1-F_R(3\sigma)=e^{-9/2}\approx ' + f4(rb)),
     S('**PDF** (if asked): differentiate, chain rule.', r'f_R(r)=\frac{r}{\sigma^2}e^{-r^2/(2\sigma^2)},\quad r\ge0')],
    f'$e^{{-1/2}}-e^{{-2}}\\approx {f4(ra)}$; $e^{{-9/2}}\\approx {f4(rb)}$', cites=cite('P2', 1))

t25, t7 = 3 * exp(-2) - 6 * exp(-5), 8 * exp(-7)
D.Q('Seeing runners · Tutorial 4 Q1',
    r'The time $X$ (minutes) between seeing two runners has PDF $f(x)=\lambda x e^{-x}$ for $x>0$. (a) Find $\lambda$. (b) Find the CDF. '
    r'(c) Find the probability the next runner is seen in 2 to 5 minutes, and in at least 7 minutes.',
    [S('**Integration by parts** (you’ll need it): $\\int u\\,dv=uv-\\int v\\,du$. With $u=x$, $dv=e^{-x}dx$:',
       r'\int xe^{-x}\,dx=-xe^{-x}+\int e^{-x}\,dx=-(x+1)e^{-x}'),
     S('(a) **Total area 1.** At $\\infty$ the term is $0$; at $0$ it is $-1$.', r'\lambda\Big[-(x+1)e^{-x}\Big]_0^{\infty}=\lambda(0+1)=1\;\Rightarrow\;\lambda=1'),
     S('(b) **CDF** for $x\\ge0$ ($0$ for $x<0$).', r'F(x)=\Big[-(t+1)e^{-t}\Big]_0^{x}=1-(1+x)e^{-x}'),
     S('(c) **2 to 5 minutes:** $F(5)-F(2)$.', r'P(2<X<5)=3e^{-2}-6e^{-5}\approx ' + f4(t25)),
     S('**At least 7:** right tail.', r'P(X\ge7)=1-F(7)=8e^{-7}\approx ' + f4(t7))],
    f'$\\lambda=1$; $F(x)=1-(1+x)e^{{-x}}$; $\\approx {f4(t25)}$ and $\\approx {f4(t7)}$', cites=cite('T4', 1))

g15, g2 = 2 * Phi(1.5) - 1, 1 - Phi(2)
D.Q('Resistor tolerance',
    r'Resistances are $R\sim N(100,\,4)$ Ω (so $\sigma=2$). (a) A resistor passes if $97\le R\le103$. What fraction passes? '
    r'(b) What fraction is above $104$ Ω? (c) Find $t$ so that $95\%$ lie in $100\pm t$.',
    [S('(a) **Symmetric** interval, $k=\\tfrac{3}{2}=1.5$ standard deviations.', r'P(|R-100|\le3)=2\Phi(1.5)-1=2(' + f4(Phi(1.5)) + ')-1=' + f4(g15)),
     S('(b) $z=\\tfrac{104-100}{2}=2$.', r'P(R>104)=1-\Phi(2)=1-' + f'{Phi(2):.5f}' + '=' + f'{g2:.5f}'),
     S('(c) **Backwards:** $2\\Phi(k)-1=0.95$ means $\\Phi(k)=0.975$, so $k=1.96$.', r't=1.96\,\sigma=1.96\cdot2=3.92\ \Omega')],
    f'(a) ${f4(g15)}$ (b) ${g2:.5f}$ (c) $t=3.92$ Ω')

sg = 1 / 1.96
D.Q('Noise level',
    r'Noise $X\sim N(0,\sigma^2)$ (volts). Find $\sigma$ so that $|X|$ exceeds $1$ V only $5\%$ of the time.',
    [S('**Rewrite:** $P(|X|>1)=0.05$ means $P(|X|\\le1)=0.95$.', r'2\Phi\!\left(\frac{1}{\sigma}\right)-1=0.95\;\Rightarrow\;\Phi\!\left(\frac1\sigma\right)=0.975'),
     S('**Table:** $\\Phi(1.96)=0.975$.', r'\frac1\sigma=1.96\;\Rightarrow\;\sigma=\frac{1}{1.96}\approx ' + f'{sg:.3f}' + r'\text{ V}')],
    f'$\\sigma\\approx {sg:.3f}$ V')

rn = 0.4 * exp(-1)
D.Q('Daily rainfall (mixed)',
    r'On a given day it doesn’t rain with probability $0.6$ ($X=0$). If it rains, the amount $X$ (mm) is exponential with $\lambda=0.5$. '
    r'(a) Find the CDF of $X$. (b) Find $P(X>2)$. (c) Find $P(X\le1)$.',
    [S('**Mixed:** a jump of $0.6$ at $0$, then the exponential CDF scaled by $0.4$.', r'F_X(x)=\begin{cases}0,&x<0\\ 0.6+0.4\left(1-e^{-0.5x}\right),&x\ge0\end{cases}'),
     S('(b) **Right tail:** only the rainy part can exceed 2.', r'P(X>2)=0.4\,e^{-0.5\cdot2}=0.4e^{-1}\approx ' + f4(rn)),
     S('(c) Includes the jump at $0$.', r'P(X\le1)=0.6+0.4(1-e^{-0.5})\approx ' + f4(0.6 + 0.4 * (1 - exp(-0.5))))],
    f'(a) jump $0.6$ at $0$, then $0.6+0.4(1-e^{{-0.5x}})$ (b) $\\approx {f4(rn)}$ (c) $\\approx {f4(0.6 + 0.4 * (1 - exp(-0.5)))}$')

D.Q('A CDF with a jump · Practice 02 Q3',
    r'''$X$ has CDF

$$
F_X(x)=\begin{cases}0,&x<-1\\ \tfrac13+\tfrac23(x+1)^2,&-1\le x\le0\\ 1,&x>0\end{cases}
$$

Find the probabilities of $A=\{X>\tfrac13\}$, $B=\{|X|\ge1\}$, $C=\{|X-\tfrac13|<1\}$, $D=\{X<0\}$.''',
    [S('**Spot the type:** $F$ jumps from $0$ to $\\tfrac13$ at $x=-1$, then rises smoothly. **Mixed**, with $P(X=-1)=\\tfrac13$.', r'P(X=-1)=F_X(-1)-F_X(-1^-)=\tfrac13'),
     S('$A$: $X$ never exceeds $0$.', r'P(A)=1-F_X(\tfrac13)=1-1=0'),
     S('$B$: $X\\ge1$ is impossible, and $X\\le-1$ means $X=-1$ exactly (the jump).', r'P(B)=P(X\le-1)=F_X(-1)=\tfrac13'),
     S('$C$: $-\\tfrac23<X<\\tfrac43$. $F$ has no jump at $-\\tfrac23$.', r'P(C)=1-F_X(-\tfrac23)=1-\left(\tfrac13+\tfrac23\cdot\tfrac19\right)=1-\tfrac{11}{27}=\tfrac{16}{27}'),
     S('$D$: $F$ is continuous at $0$ ($\\tfrac13+\\tfrac23=1$), so $P(X=0)=0$.', r'P(D)=F_X(0^-)=1')],
    r'$P(A)=0$, $P(B)=\tfrac13$, $P(C)=\tfrac{16}{27}$, $P(D)=1$', diff='advanced', cites=cite('P2', 1))


def erf_as(x):
    """Abramowitz-Stegun 7.1.26, exactly as the graph's let lines compute it."""
    t = 1 / (1 + 0.3275911 * abs(x))
    y = 1 - ((((1.061405429 * t - 1.453152027) * t + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * exp(-x * x)
    return y if x >= 0 else -y


def verify():
    import sympy as sp
    x, t, c, k, lm, s = sp.symbols('x t c k lambda sigma', positive=True)
    X = sp.Symbol('X', real=True)
    # Topic 1
    assert sp.integrate(x / 2, (x, 0, 2)) == 1
    assert sp.solve(c * sp.integrate(1 - X ** 4, (X, -1, 1)) - 1, c) == [sp.Rational(5, 8)]
    F = sp.Rational(5, 8) * sp.integrate(1 - t ** 4, (t, -1, X))
    assert sp.simplify(F - sp.Rational(5, 8) * (X - X ** 5 / 5 + sp.Rational(4, 5))) == 0
    assert F.subs(X, sp.Rational(1, 2)) - F.subs(X, -sp.Rational(1, 2)) == sp.Rational(79, 128)
    tri = sp.Piecewise((sp.Rational(1, 2) - (3 - X) / 4, X <= 3), (sp.Rational(1, 2) - (X - 3) / 4, True))
    assert sp.integrate(tri, (X, 1, 5)) == 1 and sp.integrate(tri, (X, 2, 4)) == sp.Rational(3, 4)
    assert sp.simplify(sp.integrate((t - 1) / 4, (t, 1, X)) - (X - 1) ** 2 / 8) == 0
    assert sp.simplify(sp.integrate(sp.Rational(1, 2) - (t - 3) / 4, (t, 3, X)) + sp.Rational(1, 2) - (1 - (5 - X) ** 2 / 8)) == 0
    # Topic 2
    assert sp.integrate(sp.Rational(1, 500) * sp.exp(-x / 500), (x, 500, sp.oo)) == sp.exp(-1)
    assert sp.Rational(30 - 10, 30) == sp.Rational(2, 3)
    import numpy as np
    u = np.linspace(0, pi / 2, 200001)[1:-1]
    assert np.array_equal(np.sin(u) > np.cos(u), u > pi / 4)  # sin > cos exactly on (pi/4, pi/2]
    grid = np.linspace(0, 60, 600001)[:-1] + 0.00005
    w = np.where(grid < 15, 15 - grid, np.where(grid < 45, 45 - grid, 75 - grid))
    assert abs((w <= 10).mean() - 1 / 3) < 1e-4 and abs((w >= 15).mean() - 1 / 2) < 1e-4
    # Topic 3
    assert abs(Phi(1.6) - 0.9452) < 1e-9 and abs(Phi(1.28) - 0.8997) < 1e-9 and abs(Phi(1.29) - 0.9015) < 1e-9
    assert abs(Phi(2.14) - 0.98382) < 1e-9 and abs(Phi(0.67) - 0.7486) < 1e-9 and abs(Phi(1.5) - 0.9332) < 1e-9
    assert abs(Phi(1.96) - 0.975) < 1e-9 and abs(Phi(2) - 0.97725) < 1e-9
    for a, b in [(-1, 1), (-0.8, 0.8), (0.3, 2.7), (-3, -0.5)]:
        approx = 0.5 * (erf_as(b / sqrt(2)) - erf_as(a / sqrt(2)))
        assert abs(approx - (norm.cdf(b) - norm.cdf(a))) < 1e-6, (a, b)
    assert abs(norm.ppf(0.9) - 1.28) < 0.01
    # Topic 4
    assert sp.integrate(sp.Rational(8, 100), (x, 2, 5)) == sp.Rational(24, 100)
    # Practice
    assert sp.integrate(k * x ** 2, (x, 0, 3)) == 9 * k
    assert sp.Rational(8 - 1, 27) == sp.Rational(7, 27) and sp.Rational(3, 2) ** 3 / 27 == sp.Rational(1, 8)
    assert sp.integrate(sp.exp(-2 * sp.Abs(X)), (X, -sp.oo, sp.oo)) == 1
    assert sp.simplify(sp.integrate(sp.exp(-2 * x), (x, 1, sp.oo)) - sp.exp(-2) / 2) == 0
    assert sp.simplify(2 * sp.integrate(sp.exp(-2 * x), (x, 0, sp.Rational(1, 2))) - (1 - sp.exp(-1))) == 0
    Fr = 1 - sp.exp(-x ** 2 / (2 * s ** 2))
    assert sp.simplify(Fr.subs(x, 2 * s) - Fr.subs(x, s) - (sp.exp(-sp.Rational(1, 2)) - sp.exp(-2))) == 0
    assert sp.simplify(sp.diff(Fr, x) - x / s ** 2 * sp.exp(-x ** 2 / (2 * s ** 2))) == 0
    assert sp.integrate(x * sp.exp(-x), (x, 0, sp.oo)) == 1
    Fx = sp.integrate(t * sp.exp(-t), (t, 0, x))
    assert sp.simplify(Fx - (1 - (1 + x) * sp.exp(-x))) == 0
    assert sp.simplify(Fx.subs(x, 5) - Fx.subs(x, 2) - (3 * sp.exp(-2) - 6 * sp.exp(-5))) == 0
    assert sp.simplify(1 - Fx.subs(x, 7) - 8 * sp.exp(-7)) == 0
    Fm = sp.Rational(1, 3) + sp.Rational(2, 3) * (X + 1) ** 2
    assert 1 - Fm.subs(X, -sp.Rational(2, 3)) == sp.Rational(16, 27) and Fm.subs(X, 0) == 1
    assert abs(med - 13.86) < 0.01
    print('q2 verify ok')


if __name__ == '__main__':
    verify()
    D.save()
