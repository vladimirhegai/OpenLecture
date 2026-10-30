r"""Test 2 - Question 2: continuous random variables, PDFs and probability calculations (Lectures 9-11).

Layout v3 (REWRITE_PLAN.md): topics, not cases. Each topic: explanation + formulas (open) -> open worked examples
of each kind of question -> (Extras: Gaussian, mixed) -> practice. Step words: Spot, Read off, Find c, Accumulate,
Differentiate, Rewrite, Standardise, Table, Jump, Plug in (the same words as Questions 1, 3 and 4).
"""
from math import exp, log, sqrt

from scipy.stats import norm

from lib226 import Doc, S, cite

D = Doc('q2', 'Test 2 - Question 2', ['continuous_random_variables', 'pdf', 'cdf', 'uniform', 'exponential', 'gaussian',
                                      'mixed_random_variables'])


def Phi(z):
    """Standard normal CDF as the lecture table prints it: 4 d.p. below z = 2, 5 d.p. from z = 2."""
    z = round(z, 2)
    return round(norm.cdf(z), 4 if abs(z) < 2 else 5)


def f4(v):
    return f'{v:.4f}'


D.P(r'**Lectures 9–11.** Question 2 gives you a PDF or a CDF (or names one: uniform, exponential, normal) and asks for $c$, the CDF, '
    r'and probabilities. It’s all about how the **PDF**, the **CDF** and **probability** connect.',
    cites=cite('L9', 3) + cite('L10', 2) + cite('L11', 1))

# =====================================================================================================
D.H('Topic 1: PDF ↔ CDF ↔ probability')
D.P(r'$X$ can be any number in a range: a time, a voltage, a length. Its **PDF** $f_X(x)$ is a curve. '
    r'The curve’s height is **not** a probability. The **area under it** is.')
D.P(r'**Compared with Question 1:** a PMF gives a chance at each point, and you **add** them. A PDF gives a height, and you take **area** (integrate).')
D.T(['', 'Discrete (Question 1)', 'Continuous (Question 2)'],
    [['chance of one exact value', r'$p_X(x)$', r'$0$'],
     ['everything adds to 1', r'$\sum p_X(x)=1$', r'$\int f_X(x)\,dx=1$'],
     ['CDF $F_X(x)=P(X\\le x)$', 'running total', 'area so far'],
     ['back from the CDF', 'jump sizes', 'slope']])
D.P(r'**The 5 formulas.** $f_X$ = the PDF (height of the curve), $F_X$ = the CDF (area so far), $a$ and $b$ = the ends of the range you’re asked about.')
D.P(r'**1. Total area = 1.** This is how you find an unknown $c$:')
D.EQ(r'\int_{-\infty}^{\infty}f_X(x)\,dx=1', cites=cite('L9', 8))
D.P(r'**2. CDF = the area from the far left up to $x$.** It starts at $0$ on the left and ends at $1$ on the right. ($t$ is just a placeholder letter, so it doesn’t clash with the $x$ at the top.)')
D.EQ(r'F_X(x)=P(X\le x)=\int_{-\infty}^{x}f_X(t)\,dt', cites=cite('L9', 8))
D.P(r'**3. PDF = the slope of the CDF.** Going back is a derivative:')
D.EQ(r'f_X(x)=F_X^{\prime}(x)')
D.P(r'**4. Probability = area between = a difference of $F$’s.** Every probability turns into $F$’s:')
D.EQ(r'P(a<X<b)=\int_a^b f_X(x)\,dx=F_X(b)-F_X(a)', cites=cite('L9', 8))
D.EQ(r'P(X>a)=1-F_X(a),\qquad P(X\le b)=F_X(b)')
D.P(r'**5. One exact value has chance 0.** So $<$ and $\le$ give the same answer.')
D.EQ(r'P(X=a)=0\qquad\Longrightarrow\qquad P(a<X<b)=P(a\le X\le b)')
D.GRAPH(['title "Drag $x$: the shaded area under the PDF is the CDF $F(x)$"', 'x -0.3 2.4 label="$x$" height=250', 'y 0 1.15 label=""',
         'slider X 0 2 1 step=0.05 label="$x$" animate',
         'region "(x>0)*(x<X)*(y>0)*(y<x/2)"',
         'curve "x/2" from=0 to=2 color=1 label="PDF $f(x)=x/2$"',
         'curve "x^2/4" from=0 to=2 color=2 label="CDF $F(x)=x^2/4$"',
         'segment "X" "0" "X" "X^2/4" color=0 dash', 'point "X" "X^2/4" color=2'],
        intro=r'**See it:** $f(x)=\tfrac x2$ on $[0,2]$. The shaded area left of $x$ is exactly the height of the CDF at $x$.')
D.P(r'**What to do, by what you have and what you want:**')
D.T(['You have', 'You want', 'Do'],
    [[r'$f_X$ with an unknown $c$', r'$c$', 'total area $=1$, solve (triangle: $\\tfrac12$ base × height)'],
     [r'$f_X$', r'$F_X$', 'integrate from the left end up to $x$'],
     [r'$F_X$', r'$f_X$', 'differentiate'],
     [r'$f_X$ or $F_X$', r'$P(a<X<b)$', r'$F_X(b)-F_X(a)$'],
     ['a probability', r'the cut-off $b$', r'set $F_X(b)=$ that probability, solve for $b$']])
D.P(r'**Piecewise PDF** (a triangle, or a formula that changes at some $x$): split at every corner. '
    r'On each piece, $F_X(x)$ = all the area of the earlier pieces + the area of this piece up to $x$. Before the range $F_X=0$; after it $F_X=1$.')
D.REMIND(r'''**Integrals you’ll need**

$$
\int x^n\,dx=\frac{x^{n+1}}{n+1}\qquad\qquad \int e^{-\lambda x}\,dx=-\frac1\lambda\,e^{-\lambda x}
$$

By parts, for $x\,e^{-x}$ (take $u=x$, $dv=e^{-x}dx$):

$$
\int x\,e^{-x}\,dx=-(x+1)\,e^{-x}
$$

Shortcut (not from the lectures, good for checking):

$$
\int_0^{\infty}x^n\,e^{-\lambda x}\,dx=\frac{n!}{\lambda^{n+1}}
$$''')

D.P(r'**Examples: one for each kind of question.**')
p1q = 79 / 128
D.EX(r'Find $c$, then the CDF and a probability · Practice 02 Q1',
     r'$f_X(x)=c(1-x^4)$ for $-1\le x\le1$, and $0$ elsewhere. Find $c$, the CDF, and $P(|X|<\tfrac12)$.',
     [S(r'**Spot:** an unknown $c$ → total area $=1$.'),
      S(r'**Find $c$:** integrate over the range, set it to $1$.', r'c\Big[x-\frac{x^5}{5}\Big]_{-1}^{1}=c\Big(\frac45+\frac45\Big)=\frac{8c}{5}=1\quad\Longrightarrow\quad c=\frac58'),
      S(r'**Accumulate:** the area from $-1$ up to $x$. It’s $0$ before $-1$ and $1$ after $1$.',
        r'F_X(x)=\frac58\int_{-1}^{x}(1-t^4)\,dt=\frac58\Big(x-\frac{x^5}{5}+\frac45\Big),\qquad -1\le x\le1'),
      S(r'**Rewrite:** $|X|<\tfrac12$ means $-\tfrac12<X<\tfrac12$. The PDF is symmetric, so double the area on $[0,\tfrac12]$.',
        r'P\big(|X|<\tfrac12\big)=2\cdot\frac58\Big[x-\frac{x^5}{5}\Big]_0^{1/2}=\frac{79}{128}\approx ' + f4(p1q))],
     r'$c=\tfrac58$, $\;F_X(x)=\tfrac58\big(x-\tfrac{x^5}{5}+\tfrac45\big)$ on $[-1,1]$, $\;P(|X|<\tfrac12)=\tfrac{79}{128}\approx ' + f4(p1q) + '$',
     cites=cite('P2', 1))
D.EX(r'Find $c$ fast: the triangle shortcut · Tutorial 4 Q2',
     r'$X$ has a triangle PDF: $0$ at $x=1$, peak height $c$ at $x=3$, back to $0$ at $x=5$. Find $c$ and write $f_X$.',
     [S(r'**Spot:** the PDF is a triangle, so skip the integral. Area of a triangle $=\tfrac12\cdot$ base $\cdot$ height.'),
      S(r'**Read off:** the base runs from $1$ to $5$.', r'\text{base}=4,\qquad\text{height}=c'),
      S(r'**Find $c$:** area $=1$.', r'\frac12\cdot4\cdot c=1\quad\Longrightarrow\quad c=\frac12'),
      S(r'Each side is a straight line: it climbs $\tfrac12$ over $2$ units, so the slope is $\tfrac14$.',
        r'f_X(x)=\begin{cases}\frac{x-1}{4},&1\le x\le3\\ \frac{5-x}{4},&3\le x\le5\\ 0,&\text{elsewhere}\end{cases}')],
     r'$c=\tfrac12$', cites=cite('T4', 1))
D.EX(r'PDF → CDF, piece by piece · Tutorial 4 Q2',
     r'Same triangle: $f_X(x)=\tfrac{x-1}{4}$ on $[1,3]$ and $\tfrac{5-x}{4}$ on $[3,5]$. Find the CDF and $P(2<X<3.5)$.',
     [S(r'**Spot:** have $f$, want $F$ → integrate. The PDF changes at $x=3$, so do two pieces.'),
      S(r'**Accumulate**, left piece: the area from $1$ up to $x$.', r'F_X(x)=\int_1^x\frac{t-1}{4}\,dt=\frac{(x-1)^2}{8},\qquad 1\le x\le3'),
      S(r'**Accumulate**, right piece: everything ($1$) minus the small triangle still to come on the right.', r'F_X(x)=1-\frac{(5-x)^2}{8},\qquad 3\le x\le5'),
      S(r'**Check:** both pieces give $\tfrac12$ at $x=3$ (the peak splits the area in half).', r'\frac{(3-1)^2}{8}=\frac12=1-\frac{(5-3)^2}{8}'),
      S(r'**Rewrite** $P(2<X<3.5)=F(3.5)-F(2)$, then **plug in**: $3.5$ is on the right piece, $2$ on the left.', r'F(3.5)-F(2)=\Big(1-\frac{1.5^2}{8}\Big)-\frac18=\frac{19}{32}\approx0.5938')],
     r'$F_X(x)=\begin{cases}0,&x<1\\ \frac{(x-1)^2}{8},&1\le x\le3\\ 1-\frac{(5-x)^2}{8},&3\le x\le5\\ 1,&x>5\end{cases}$, $\;P(2<X<3.5)=\tfrac{19}{32}$',
     cites=cite('T4', 1))
D.EX(r'CDF → probabilities and the PDF · Lecture 9',
     r'$F_X(x)=\tfrac x4$ for $0\le x\le4$ ($0$ before, $1$ after). Find (a) $P(X\le-1)$, (b) $P(X\le1)$, (c) $P(2<X\le3)$, (d) $P(X>1)$, (e) $P(X=1)$, (f) the PDF.',
     [S(r'**Spot:** have $F$. Probabilities → **rewrite** with $F$’s; the PDF → **differentiate**.'),
      S(r'(a) $-1$ is left of the range.', r'P(X\le-1)=F_X(-1)=0'),
      S(r'(b) Up to $1$.', r'P(X\le1)=F_X(1)=\frac14'),
      S(r'(c) Between: a difference.', r'P(2<X\le3)=F_X(3)-F_X(2)=\frac34-\frac24=\frac14'),
      S(r'(d) Above: one minus.', r'P(X>1)=1-F_X(1)=\frac34'),
      S(r'(e) One exact value.', r'P(X=1)=0'),
      S(r'(f) **Differentiate:** the slope of $\tfrac x4$.', r'f_X(x)=\frac14,\qquad 0\le x\le4\quad(0\text{ elsewhere})')],
     r'(a) $0$ (b) $\tfrac14$ (c) $\tfrac14$ (d) $\tfrac34$ (e) $0$ (f) $f_X=\tfrac14$ on $[0,4]$', cites=cite('L9', 5))
bh, bt = sqrt(2), sqrt(3.6)
D.EX(r'Working backwards: find the cut-off $b$',
     r'$f_X(x)=\tfrac x2$ on $[0,2]$ (the PDF in the graph above). (a) Find $b$ with $P(X\le b)=\tfrac12$. (b) Find the value that only the top $10\%$ are above.',
     [S(r'**Spot:** given a probability, want the cut-off → get $F$, set it equal, solve.'),
      S(r'**Accumulate** first.', r'F_X(x)=\int_0^x\frac t2\,dt=\frac{x^2}{4},\qquad 0\le x\le2'),
      S(r'(a) Set $F_X(b)=\tfrac12$.', r'\frac{b^2}{4}=\frac12\quad\Longrightarrow\quad b=\sqrt2\approx ' + f'{bh:.3f}'),
      S(r'(b) Top $10\%$ above $b$ means $90\%$ below it: set $F_X(b)=0.9$.', r'\frac{b^2}{4}=0.9\quad\Longrightarrow\quad b=\sqrt{3.6}\approx ' + f'{bt:.3f}')],
     f'(a) $b=\\sqrt2\\approx {bh:.3f}$ (b) $b=\\sqrt{{3.6}}\\approx {bt:.3f}$')

# =====================================================================================================
D.H('Topic 2: Uniform and exponential')
D.P(r'When the question **names** the PDF, it’s ready-made: no $c$ to find. Just learn these two and use Topic 1’s rules on them.')
D.P(r'**Uniform$(a,b)$:** “uniformly at random between $a$ and $b$”. $a$ = the left end, $b$ = the right end. The PDF is flat:')
D.EQ(r'f_X(x)=\frac{1}{b-a},\qquad F_X(x)=\frac{x-a}{b-a},\qquad a\le x\le b', cites=cite('L10', 3))
D.P(r'Flat means every probability is just a **length ratio**:')
D.EQ(r'P(X\text{ lands in a piece})=\frac{\text{length of the piece}}{b-a}')
D.P(r'**Exponential$(\lambda)$:** a lifetime or a waiting time. $\lambda$ = the rate (per hour, per minute), $x\ge0$ = the time. '
    r'Given the **mean** instead? Then $\lambda=\dfrac1{\text{mean}}$.')
D.EQ(r'f_X(x)=\lambda e^{-\lambda x},\qquad F_X(x)=1-e^{-\lambda x},\qquad x\ge0', cites=cite('L10', 4))
D.P(r'You’ll use the **tail** (chance it lasts longer than $x$) more than the CDF. A “between” is a difference of two tails:')
D.EQ(r'P(X>x)=e^{-\lambda x},\qquad P(a<X<b)=e^{-\lambda a}-e^{-\lambda b}')
D.P(r'**Memoryless:** “it has already lasted $s$; chance it lasts $t$ more?” The time already waited doesn’t matter: an old part is as good as new. '
    r'$s$ = time already lasted, $t$ = the extra time.')
D.EQ(r'P(X>s+t\mid X>s)=P(X>t)=e^{-\lambda t}', cites=cite('L4', 1))

D.P(r'**Examples.**')
D.EX(r'Uniform: length ÷ length · Tutorial 2 Q5',
     r'A bus comes at a uniform random time between 1:00 and 1:30. What’s the chance you wait at least 10 minutes (arriving at 1:00)?',
     [S(r'**Spot:** “uniformly between” → uniform. $X$ = minutes after 1:00.'),
      S(r'**Read off:**', r'a=0,\qquad b=30'),
      S(r'**Rewrite:** waiting at least 10 means the bus comes in $[10,30]$, a piece of length $20$.'),
      S(r'**Plug in:** length ÷ total length.', r'P(X\ge10)=\frac{30-10}{30}=\frac23')],
     r'$\tfrac23$', cites=cite('T2', 1))
D.EX(r'Uniform, with an event to rewrite · Tutorial 3 Q1',
     r'Pick $X$ uniformly in $(0,\tfrac\pi2)$. What’s the chance $\sin X>\cos X$?',
     [S(r'**Spot:** uniform.', r'a=0,\qquad b=\frac\pi2'),
      S(r'**Rewrite** the event as a range of $X$: $\sin x$ passes $\cos x$ at $x=\tfrac\pi4$.', r'\sin X>\cos X\iff X>\frac\pi4'),
      S(r'**Plug in:** length ÷ total length.', r'P=\frac{\frac\pi2-\frac\pi4}{\frac\pi2}=\frac12')],
     r'$\tfrac12$', cites=cite('T3', 1))
pl, pb = exp(-1), exp(-0.4) - exp(-2)
D.EX(r'Exponential: tail and between',
     r'A part’s lifetime is exponential with a mean of 500 hours. Find (a) $P(X>500)$, (b) $P(200<X<1000)$.',
     [S(r'**Spot:** lifetime, exponential. **Read off** $\lambda$ from the mean.', r'\lambda=\frac1{500}=0.002\text{ per hour}'),
      S(r'(a) **Plug in** the tail.', r'P(X>500)=e^{-0.002\cdot500}=e^{-1}\approx ' + f4(pl)),
      S(r'(b) **Rewrite** as a difference of tails, then **plug in**.', r'P(200<X<1000)=e^{-0.4}-e^{-2}\approx ' + f4(pb))],
     f'(a) $e^{{-1}}\\approx {f4(pl)}$ (b) $\\approx {f4(pb)}$')
D.EX(r'Exponential, memoryless · Tutorial 4 Q3',
     r'A TV tube’s lifetime (years) is exponential with $\lambda=0.1$. The tube is already 10 years old. What’s the chance it lasts another 10?',
     [S(r'**Spot:** “already lasted” → memoryless.', r'P(X>20\mid X>10)'),
      S(r'**Read off:**', r'\lambda=0.1,\qquad s=10,\qquad t=10'),
      S(r'**Plug in:** the old tube is as good as new, so it’s just a new tube lasting 10 years.', r'P(X>10)=e^{-0.1\cdot10}=e^{-1}\approx ' + f4(pl)),
      S(r'Same thing the long way, as a ratio of tails:', r'\frac{P(X>20)}{P(X>10)}=\frac{e^{-2}}{e^{-1}}=e^{-1}')],
     r'$e^{-1}\approx ' + f4(pl) + '$', cites=cite('T4', 1))

# =====================================================================================================
D.H('Extras: Gaussian and mixed')
D.H('Gaussian (normal)', level=2)
D.P(r'“Normal with mean $\mu$ and standard deviation $\sigma$”, written $X\sim N(\mu,\sigma^2)$. $\mu$ = the centre of the bell, '
    r'$\sigma$ = how wide it is, $\sigma^2$ = the variance.')
D.P(r'You can’t integrate the bell curve by hand. So **standardise**: $z$ = how many $\sigma$’s you are from the centre. Then read $\Phi(z)=P(Z\le z)$ from the table.')
D.EQ(r'z=\frac{x-\mu}{\sigma},\qquad F_X(x)=\Phi(z),\qquad \Phi(-z)=1-\Phi(z)', cites=cite('L11', 1))
D.P(r'Topic 1’s rules, with $\Phi$ in place of $F$:')
D.EQ(r'P(X>x)=1-\Phi(z),\qquad P(a<X<b)=\Phi(z_b)-\Phi(z_a)')
D.P(r'For a range centred on $\mu$ (within $k$ standard deviations), both tails are the same size:')
D.EQ(r'P(|X-\mu|<k\sigma)=2\Phi(k)-1')
D.P(r'**Backwards** (given a probability, find $x$): find the $z$ whose $\Phi(z)$ is the chance **below** $x$, then undo the standardising:')
D.EQ(r'x=\mu+z\,\sigma')
D.T(['$z$', '0.5', '1.0', '1.28', '1.5', '1.645', '1.96', '2.0', '2.5'],
    [['$\\Phi(z)$', f4(Phi(.5)), f4(Phi(1)), f4(Phi(1.28)), f4(Phi(1.5)), '0.95', f4(Phi(1.96)), f'{Phi(2):.5f}', f'{Phi(2.5):.5f}']],
    cites=cite('L10', 6))
D.CO('warning', r'**Variance or standard deviation?** “$\sigma^2=2.25$” means $\sigma=1.5$. Dividing by $2.25$ is the most common lost mark.')
pz = 2 * Phi(1.6) - 1
D.EX(r'Gaussian, forwards · Lecture 11',
     r'A sensor’s error $X$ is normal with $\mu=0$ and $\sigma=0.5$. What’s the chance $|X|<0.8$?',
     [S(r'**Read off:**', r'\mu=0,\qquad\sigma=0.5'),
      S(r'**Rewrite:** $|X|<0.8$ means $-0.8<X<0.8$.'),
      S(r'**Standardise** both ends.', r'z=\frac{\pm0.8-0}{0.5}=\pm1.6'),
      S(r'A symmetric interval, so use $2\Phi(k)-1$.', r'\Phi(1.6)-\Phi(-1.6)=\Phi(1.6)-\big(1-\Phi(1.6)\big)=2\Phi(1.6)-1'),
      S(r'**Table:** $\Phi(1.6)=' + f4(Phi(1.6)) + '$.', r'2(' + f4(Phi(1.6)) + r')-1=' + f4(pz))],
     f'${f4(pz)}$', cites=cite('L11', 3))
D.EX(r'Gaussian, backwards · Tutorial 4 Q4',
     r'Test scores are $N(500,100^2)$. Which score marks the top $10\%$?',
     [S(r'**Read off:**', r'\mu=500,\qquad\sigma=100'),
      S(r'**Rewrite:** top $10\%$ above means $90\%$ below.', r'\Phi(z)=0.90'),
      S(r'**Table, backwards:** $\Phi(1.28)=' + f4(Phi(1.28)) + '$ is closest to $0.90$.', r'z\approx1.28'),
      S(r'Undo the standardising.', r'x=\mu+z\sigma=500+1.28\cdot100=628')],
     r'about $628$', cites=cite('T4', 1))
b95, b89 = Phi(round(15 / 7, 2)), Phi(round(9 / 7, 2))
D.EX(r'Gaussian, two cut-offs · Practice 03 Q8',
     r'Diastolic blood pressure is normal with $\mu=80$, $\sigma=7$ (mm Hg). $\ge95$ is hypertensive; strictly between $89$ and $95$ is mild hypertension. '
     'What percent of people are in each group?',
     [S(r'**Read off:**', r'\mu=80,\qquad\sigma=7'),
      S(r'**Standardise** both cut-offs (2 decimals, like the table).', (r'z_{95}=\frac{95-80}{7}\approx2.14', r'z_{89}=\frac{89-80}{7}\approx1.29')),
      S(r'Hypertensive: the right tail. **Table.**', r'P(X\ge95)=1-\Phi(2.14)=1-' + f'{b95:.5f}' + '=' + f'{1 - b95:.5f}'),
      S(r'Mild: between the two. **Table.**', (r'P(89<X<95)=\Phi(2.14)-\Phi(1.29)', r'=' + f'{b95:.5f}' + '-' + f4(b89) + '=' + f'{b95 - b89:.4f}'))],
     f'Mild ≈ {100 * (b95 - b89):.2f}%, hypertensive ≈ {100 * (1 - b95):.2f}%', cites=cite('P3', 3))

D.H('Mixed: a jump and a ramp', level=2)
D.P(r'“With probability $q$ it is **exactly** $x_0$, otherwise it’s spread over a range.” That’s a mixed $X$: part discrete, part continuous.')
D.L([r'**Jump:** an exact value with real chance. On the CDF it’s a jump, and the jump size is the chance: $P(X=x_0)=q$.',
     r'**Spread:** the rest of the time, $X$ has its usual PDF, but it only gets the **leftover** chance $1-q$. So multiply that PDF by $1-q$.',
     r'**Any probability** = the jumps inside the range + the area over the range.'])
D.EQ(r'P(X=x_0)=q,\qquad f_{\text{spread}}(x)=(1-q)\times(\text{its usual PDF})', cites=cite('L10', 8))
D.GRAPH(['title "CDF of the received signal: a jump, then a ramp"', 'x -2 12 label="$x$" height=230', 'y 0 1.1 label="$F_X(x)$"',
         'segment "-2" "0" "0" "0" color=2', 'segment "0" "0.2" "10" "1" color=2', 'segment "10" "1" "12" "1" color=2',
         'point "0" "0.2" color=2', 'segment "0" "0" "0" "0.2" color=0 dash', 'text "1.6" "0.12" "jump $=0.2$"',
         'text "6.8" "0.6" "slope $0.08$"'],
        intro='**Discrete = all jumps, continuous = all slope, mixed = both.**')
D.EX(r'Mixed: build the CDF · Lectures 10–11',
     r'A received signal is lost ($X=0$) with probability $0.2$. Otherwise its level is uniform on $(0,10)$. Find the CDF and $P(2<X<5)$.',
     [S(r'**Jump** at $0$: the lost signal.', r'P(X=0)=0.2'),
      S(r'**Spread:** the uniform PDF times the leftover $0.8$.', r'f(x)=0.8\cdot\frac1{10}=0.08,\qquad 0<x<10'),
      S(r'**Accumulate:** the jump first, then the ramp.', r'F_X(x)=\begin{cases}0,&x<0\\ 0.2+0.08x,&0\le x<10\\ 1,&x\ge10\end{cases}'),
      S(r'**Rewrite** $P(2<X<5)$: the jump at $0$ isn’t inside, so only area counts.', r'F_X(5)-F_X(2)=0.6-0.36=0.24')],
     r'jump $0.2$ at $0$, then the ramp $0.2+0.08x$ up to $1$ at $x=10$; $\;P(2<X<5)=0.24$', cites=cite('L11', 4) + cite('L11', 5))
rn, r1m = 0.4 * exp(-1), 0.6 + 0.4 * (1 - exp(-0.5))
D.EX(r'Mixed: daily rainfall',
     r'On a given day it doesn’t rain with probability $0.6$ ($X=0$). If it rains, the amount $X$ (mm) is exponential with $\lambda=0.5$. '
     r'(a) Find the CDF of $X$. (b) Find $P(X>2)$. (c) Find $P(X\le1)$.',
     [S(r'**Spot:** an exact value ($0$) with chance $0.6$, plus a spread → mixed.', r'q=0.6,\qquad 1-q=0.4,\qquad\lambda=0.5'),
      S(r'(a) **Jump** of $0.6$ at $0$, then the exponential CDF scaled by $0.4$.', r'F_X(x)=\begin{cases}0,&x<0\\ 0.6+0.4\left(1-e^{-0.5x}\right),&x\ge0\end{cases}'),
      S(r'(b) **Rewrite:** only rainy days can go above 2. The exponential tail times $0.4$.', r'P(X>2)=0.4\,e^{-0.5\cdot2}=0.4e^{-1}\approx ' + f4(rn)),
      S(r'(c) **Rewrite:** $F_X(1)$, which includes the jump at $0$.', r'P(X\le1)=0.6+0.4(1-e^{-0.5})\approx ' + f4(r1m))],
     f'(a) jump $0.6$ at $0$, then $0.6+0.4(1-e^{{-0.5x}})$ (b) $\\approx {f4(rn)}$ (c) $\\approx {f4(r1m)}$')

# =====================================================================================================
D.H('Practice Questions')
D.CO('tip', r'''**Question 2 is always one of these three, in parts (a), (b), (c):**

1. **PDF ↔ CDF ↔ PMF:** integrate $f$ for $F$; differentiate $F$ for $f$; a **staircase** $F$ → the jumps are a PMF; probabilities $=F(b)-F(a)$.
2. **Find $c$:** total area $=1$, solve (triangle: $\tfrac12$ base × height).
3. **Uniform:** length ÷ total length. **Exponential:** $\lambda=\tfrac1{\text{mean}}$, $P(X>x)=e^{-\lambda x}$, between = difference of tails, “already lasted” → memoryless.''')
D.P('Test-style, easy → medium, same level as the practice sets. Solve on paper first, then open the solution.')

# ---- PDF <-> CDF <-> PMF
D.Q('PDF ↔ CDF · CDF → probabilities and the PDF',
    r'$X$ has CDF $F_X(x)=\dfrac{x^2}{9}$ for $0\le x\le3$ ($0$ before, $1$ after). Find (a) $P(X\le1)$, (b) $P(1<X\le2)$, (c) $P(X>2)$, (d) the PDF.',
    [S(r'**Spot:** have $F$. Probabilities → **rewrite** with $F$’s; the PDF → **differentiate**.'),
     S(r'(a) Up to $1$.', r'P(X\le1)=F_X(1)=\frac19'),
     S(r'(b) Between: a difference.', r'P(1<X\le2)=F_X(2)-F_X(1)=\frac49-\frac19=\frac13'),
     S(r'(c) Above: one minus.', r'P(X>2)=1-F_X(2)=1-\frac49=\frac59'),
     S(r'(d) **Differentiate** $\tfrac{x^2}{9}$.', r'f_X(x)=\frac{2x}{9},\qquad 0\le x\le3\quad(0\text{ elsewhere})')],
    r'(a) $\tfrac19$ (b) $\tfrac13$ (c) $\tfrac59$ (d) $\tfrac{2x}{9}$ on $[0,3]$', diff='introductory', cites=cite('L9', 5))

e2 = 1 - exp(-2)
D.Q('PDF ↔ CDF ↔ PMF · staircase or smooth?',
    r'''Two CDFs:

$$
F_X(x)=\begin{cases}0,&x<0\\ 0.3,&0\le x<1\\ 0.8,&1\le x<2\\ 1,&x\ge2\end{cases}\qquad\qquad F_Y(y)=\begin{cases}0,&y<0\\ 1-e^{-2y},&y\ge0\end{cases}
$$

(a) Which one is discrete? Find its PMF. (b) Find the PDF of the other one. (c) Find $P(X\le1)$, $P(X<1)$, $P(Y\le1)$ and $P(Y<1)$.''',
    [S(r'(a) **Spot:** $F_X$ is a **staircase** → $X$ is discrete. The **jump sizes** are the PMF.', r'p_X(0)=0.3,\quad p_X(1)=0.8-0.3=0.5,\quad p_X(2)=1-0.8=0.2'),
     S(r'(b) $F_Y$ is **smooth** → $Y$ is continuous. **Differentiate.**', r'f_Y(y)=\frac{d}{dy}\big(1-e^{-2y}\big)=2e^{-2y},\qquad y\ge0'),
     S(r'(c) Discrete: $\le1$ includes the jump at $1$, $<1$ doesn’t.', r'P(X\le1)=F_X(1)=0.8,\qquad P(X<1)=0.3'),
     S(r'Continuous: one point has chance $0$, so $<$ and $\le$ agree.', r'P(Y\le1)=P(Y<1)=1-e^{-2}\approx' + f4(e2))],
    r'(a) $X$: $0.3,0.5,0.2$ at $0,1,2$ (b) $f_Y=2e^{-2y}$, $y\ge0$ (c) $0.8$, $0.3$, $\approx' + f4(e2) + r'$, $\approx' + f4(e2) + '$',
    diff='introductory')

D.Q('PDF ↔ CDF · a triangle, piece by piece',
    r'$f_X(x)=x$ for $0\le x\le1$, $f_X(x)=2-x$ for $1\le x\le2$, and $0$ elsewhere. (a) Find the CDF. (b) Find $P(0.5<X<1.5)$.',
    [S(r'**Spot:** have $f$, want $F$ → integrate. The PDF changes at $x=1$, so do two pieces.'),
     S(r'(a) **Accumulate**, left piece: area from $0$ up to $x$.', r'F_X(x)=\int_0^x t\,dt=\frac{x^2}{2},\qquad 0\le x\le1'),
     S(r'**Accumulate**, right piece: everything ($1$) minus the small triangle still to come on the right.', r'F_X(x)=1-\frac{(2-x)^2}{2},\qquad 1\le x\le2'),
     S(r'**Check:** both pieces give $\tfrac12$ at $x=1$.', r'\frac{1^2}{2}=\frac12=1-\frac{(2-1)^2}{2}'),
     S(r'(b) **Rewrite** as $F(1.5)-F(0.5)$: $1.5$ is on the right piece, $0.5$ on the left.', r'\Big(1-\frac{0.5^2}{2}\Big)-\frac{0.5^2}{2}=0.875-0.125=0.75')],
    r'(a) $0$, $\tfrac{x^2}{2}$ on $[0,1]$, $1-\tfrac{(2-x)^2}{2}$ on $[1,2]$, $1$ after (b) $0.75$')

ra, rb = exp(-0.5) - exp(-2), exp(-4.5)
D.Q('PDF ↔ CDF · CDF → probabilities and PDF · Practice 02 Q4',
    r'''The Rayleigh random variable $R$ has CDF

$$
F_R(r)=\begin{cases}0,&r<0\\ 1-e^{-r^2/(2\sigma^2)},&r\ge0\end{cases}
$$

(a) Find $P(\sigma\le R\le2\sigma)$ and $P(R>3\sigma)$. (b) Find the PDF of $R$.''',
    [S(r'**Spot:** a CDF is given → have $F$.'),
     S(r'(a) **Rewrite** as a difference. $\sigma$ cancels in each power.', r'P(\sigma\le R\le2\sigma)=F_R(2\sigma)-F_R(\sigma)=e^{-1/2}-e^{-2}\approx ' + f4(ra)),
     S(r'**Rewrite** as one minus: $\tfrac{(3\sigma)^2}{2\sigma^2}=\tfrac92$.', r'P(R>3\sigma)=1-F_R(3\sigma)=e^{-9/2}\approx ' + f4(rb)),
     S(r'(b) **Differentiate** (chain rule: the inside $-\tfrac{r^2}{2\sigma^2}$ has slope $-\tfrac{r}{\sigma^2}$).', r'f_R(r)=\frac{r}{\sigma^2}\,e^{-r^2/(2\sigma^2)},\qquad r\ge0')],
    f'(a) $e^{{-1/2}}-e^{{-2}}\\approx {f4(ra)}$; $e^{{-9/2}}\\approx {f4(rb)}$ (b) $\\dfrac{{r}}{{\\sigma^2}}e^{{-r^2/(2\\sigma^2)}}$ for $r\\ge0$',
    cites=cite('P2', 1))

# ---- Find c
e3 = exp(-3)
D.Q('Find $c$ · area = 1',
    r'(a) $f_X(x)=c(2-x)$ for $0\le x\le2$, $0$ elsewhere. Find $c$, the CDF, and $P(X<1)$. '
    r'(b) $f_Y(y)=c\,e^{-3y}$ for $y\ge0$. Find $c$ and $P(Y>1)$. Which family is $Y$?',
    [S(r'(a) **Find $c$:** total area $=1$. (Or the triangle shortcut: base $2$, height $2c$.)', r'c\int_0^2(2-x)\,dx=c\Big[2x-\frac{x^2}{2}\Big]_0^2=2c=1\quad\Longrightarrow\quad c=\frac12'),
     S(r'**Accumulate** from $0$ up to $x$.', r'F_X(x)=\frac12\Big(2x-\frac{x^2}{2}\Big)=x-\frac{x^2}{4},\qquad 0\le x\le2'),
     S(r'**Plug in** $x=1$.', r'P(X<1)=F_X(1)=1-\frac14=\frac34'),
     S(r'(b) **Find $c$:**', r'c\int_0^{\infty}e^{-3y}\,dy=\frac c3=1\quad\Longrightarrow\quad c=3'),
     S(r'That’s the exponential PDF with $\lambda=3$, so use the tail.', r'P(Y>1)=e^{-3}\approx' + f4(e3))],
    r'(a) $c=\tfrac12$, $F_X=x-\tfrac{x^2}{4}$ on $[0,2]$, $P(X<1)=\tfrac34$ (b) $c=3$, $P(Y>1)=e^{-3}\approx' + f4(e3) + '$, exponential$(3)$',
    diff='introductory')

D.Q('Find $c$ · then the CDF · Tutorial 5 Q5',
    r'$X$ has PDF $f_X(x)=Cx^2$ for $|x|\le1$, and $0$ otherwise. (a) Find $C$. (b) Find the CDF. (c) Find $P(X>\tfrac12)$ and $P(|X|<\tfrac12)$.',
    [S(r'(a) **Spot:** unknown constant → total area $=1$. **Find $c$.**', r'C\int_{-1}^{1}x^2\,dx=\frac{2C}{3}=1\quad\Longrightarrow\quad C=\frac32'),
     S(r'(b) **Accumulate** from $-1$ up to $x$.', r'F_X(x)=\int_{-1}^{x}\frac32t^2\,dt=\frac{x^3+1}{2},\qquad -1\le x\le1'),
     S(r'(c) **Rewrite** as one minus.', r'P(X>\tfrac12)=1-\frac{\frac18+1}{2}=\frac{7}{16}'),
     S(r'**Rewrite** as a difference. Small, because the PDF is near $0$ around $x=0$.', r'F(\tfrac12)-F(-\tfrac12)=\frac{\frac98-\frac78}{2}=\frac18')],
    r'(a) $C=\tfrac32$ (b) $\tfrac{x^3+1}{2}$ on $[-1,1]$ (c) $\tfrac7{16}$ and $\tfrac18$', cites=cite('T5', 1))

t25, t7 = 3 * exp(-2) - 6 * exp(-5), 8 * exp(-7)
D.Q('Find $c$ · by parts · Tutorial 4 Q1',
    r'The time $X$ (minutes) between seeing two runners has PDF $f(x)=\lambda x e^{-x}$ for $x>0$. (a) Find $\lambda$. (b) Find the CDF. '
    r'(c) Find the probability the next runner is seen in 2 to 5 minutes, and in at least 7 minutes.',
    [S(r'**Spot:** unknown constant → total area $=1$. First the integral, **by parts** ($u=x$, $dv=e^{-x}dx$):', r'\int xe^{-x}\,dx=-xe^{-x}+\int e^{-x}\,dx=-(x+1)e^{-x}'),
     S(r'(a) **Find $c$:** total area $=1$. (Shortcut: $\int_0^\infty xe^{-x}dx=\tfrac{1!}{1^2}=1$.)', r'\lambda\Big[-(x+1)e^{-x}\Big]_0^{\infty}=\lambda(0+1)=1\quad\Longrightarrow\quad\lambda=1'),
     S(r'(b) **Accumulate** from $0$ to $x$ ($0$ for $x<0$).', r'F(x)=\Big[-(t+1)e^{-t}\Big]_0^{x}=1-(1+x)e^{-x}'),
     S(r'(c) **Rewrite** as a difference.', r'P(2<X<5)=F(5)-F(2)=3e^{-2}-6e^{-5}\approx ' + f4(t25)),
     S(r'**Rewrite** as one minus.', r'P(X\ge7)=1-F(7)=8e^{-7}\approx ' + f4(t7))],
    f'$\\lambda=1$; $F(x)=1-(1+x)e^{{-x}}$; $\\approx {f4(t25)}$ and $\\approx {f4(t7)}$', cites=cite('T4', 1))

# ---- Uniform and exponential
D.Q('Uniform · the basics',
    r'$X$ is uniform on $[2,8]$. Find (a) the PDF and the CDF, (b) $P(X<5)$, (c) $P(3<X<4)$, (d) $P(X>7)$, (e) the $b$ with $P(X\le b)=0.25$.',
    [S(r'(a) **Read off:** $a=2$, $b=8$, total length $6$.', r'f_X(x)=\frac16,\qquad F_X(x)=\frac{x-2}{6},\qquad 2\le x\le8'),
     S(r'(b) Length ÷ total length: $[2,5]$ has length $3$.', r'P(X<5)=\frac36=\frac12'),
     S(r'(c) $[3,4]$ has length $1$.', r'P(3<X<4)=\frac16'),
     S(r'(d) $[7,8]$ has length $1$.', r'P(X>7)=\frac16'),
     S(r'(e) **Backwards:** set $F_X(b)=0.25$.', r'\frac{b-2}{6}=0.25\quad\Longrightarrow\quad b=3.5')],
    r'(a) $\tfrac16$ and $\tfrac{x-2}{6}$ on $[2,8]$ (b) $\tfrac12$ (c) $\tfrac16$ (d) $\tfrac16$ (e) $3.5$', diff='introductory')

D.Q('Uniform · Tutorial 4 Q5',
    'Flights leave every half hour (9:00, 9:30, 10:00, …). A passenger arrives at a uniform random time between 8:45 and 9:45 A.M. '
    'Find the probability the passenger waits (a) **at most 10 minutes**, (b) **at least 15 minutes**.',
    [S(r'**Spot:** uniform. $T$ = minutes after 8:45, total length $60$. Flights leave at $T=15,\ 45,\ 75$.', r'f_T(t)=\frac1{60},\quad 0\le t\le60'),
     S(r'(a) **Rewrite:** wait $\le10$ means arriving in the 10 minutes before a flight.', r'T\in[5,15]\cup[35,45]'),
     S(r'Length ÷ total length.', r'P=\frac{10+10}{60}=\frac13'),
     S(r'(b) **Rewrite:** wait $\ge15$ means the next flight is 15+ minutes away.', r'T\in[15,30]\cup[45,60]'),
     S(r'Length ÷ total length.', r'P=\frac{15+15}{60}=\frac12')],
    r'(a) $\tfrac13$ (b) $\tfrac12$', cites=cite('T4', 1))

ea, eb, med = exp(-1), exp(-0.5) - exp(-1.5), 4 * log(2)
D.Q('Exponential, memoryless · like Lecture 10',
    r'The length $X$ (minutes) of a phone call is exponential with a **mean of 4 minutes**. Find (a) $P(X>4)$, (b) $P(2<X<6)$, '
    r'(c) the chance a call that has already lasted 3 minutes lasts **more than 7** in total, (d) the time $t$ with $P(X>t)=\tfrac12$.',
    [S(r'**Read off** $\lambda$ from the mean.', r'\lambda=\frac14=0.25\text{ per minute}'),
     S(r'(a) **Rewrite** as a tail. **Plug in.**', r'P(X>4)=e^{-0.25\cdot4}=e^{-1}\approx ' + f4(ea)),
     S(r'(b) **Rewrite:** difference of two tails.', r'P(2<X<6)=e^{-0.5}-e^{-1.5}\approx ' + f4(eb)),
     S(r'(c) **Memoryless:** 4 more minutes, as if new.', r'P(X>7\mid X>3)=P(X>4)=e^{-1}\approx ' + f4(ea)),
     S(r'(d) **Backwards:** set the tail to $\tfrac12$, take $\ln$.', r'e^{-0.25t}=\frac12\quad\Longrightarrow\quad t=4\ln2\approx ' + f'{med:.2f}' + r'\text{ min}')],
    f'(a) $\\approx {f4(ea)}$ (b) $\\approx {f4(eb)}$ (c) $\\approx {f4(ea)}$ (d) $4\\ln2\\approx {med:.2f}$ min', cites=cite('L10', 4))


def erf_as(x):
    """Abramowitz-Stegun 7.1.26 (kept for the erf check in verify())."""
    t = 1 / (1 + 0.3275911 * abs(x))
    y = 1 - ((((1.061405429 * t - 1.453152027) * t + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * exp(-x * x)
    return y if x >= 0 else -y


def verify():
    import numpy as np
    import sympy as sp
    x, t, c, s, a = sp.symbols('x t c sigma a', positive=True)
    X = sp.Symbol('X', real=True)
    # Topic 1
    assert sp.integrate(x / 2, (x, 0, 2)) == 1
    assert sp.solve(c * sp.integrate(1 - X ** 4, (X, -1, 1)) - 1, c) == [sp.Rational(5, 8)]
    F = sp.Rational(5, 8) * sp.integrate(1 - t ** 4, (t, -1, X))
    assert sp.simplify(F - sp.Rational(5, 8) * (X - X ** 5 / 5 + sp.Rational(4, 5))) == 0
    assert F.subs(X, sp.Rational(1, 2)) - F.subs(X, -sp.Rational(1, 2)) == sp.Rational(79, 128)
    tri = sp.Piecewise(((t - 1) / 4, (t >= 1) & (t <= 3)), ((5 - t) / 4, (t > 3) & (t <= 5)), (0, True))
    assert sp.integrate(tri, (t, 1, 5)) == 1 and sp.Rational(1, 2) * 4 * sp.Rational(1, 2) == 1
    assert sp.simplify(tri.subs(t, 2) - (sp.Rational(1, 2) - sp.Abs(2 - 3) / 4)) == 0  # same triangle as Tutorial 4 Q2
    Ft = lambda v: sp.integrate(tri, (t, 1, v))
    assert sp.simplify(Ft(2) - sp.Rational(1, 8)) == 0 and sp.simplify(Ft(sp.Rational(7, 2)) - Ft(2) - sp.Rational(19, 32)) == 0
    assert sp.simplify(Ft(3) - sp.Rational(1, 2)) == 0
    Fh = sp.integrate(t / 2, (t, 0, x))
    assert sp.simplify(Fh - x ** 2 / 4) == 0
    assert sp.solve(Fh - sp.Rational(1, 2), x) == [sp.sqrt(2)] and abs(float(sp.solve(Fh - sp.Rational(9, 10), x)[0]) - bt) < 1e-12
    # Topic 2
    assert sp.integrate(sp.Rational(1, 500) * sp.exp(-x / 500), (x, 500, sp.oo)) == sp.exp(-1)
    assert sp.simplify(sp.integrate(sp.Rational(1, 500) * sp.exp(-x / 500), (x, 200, 1000)) - (sp.exp(-sp.Rational(2, 5)) - sp.exp(-2))) == 0
    assert abs(pb - (exp(-0.4) - exp(-2))) < 1e-15
    assert sp.Rational(30 - 10, 30) == sp.Rational(2, 3)
    # Gaussian
    assert abs(Phi(1.6) - 0.9452) < 1e-9 and abs(Phi(1.28) - 0.8997) < 1e-9
    assert abs(Phi(2.14) - 0.98382) < 1e-9 and abs(Phi(0.67) - 0.7486) < 1e-9 and abs(Phi(1.29) - 0.9015) < 1e-9
    assert abs(Phi(1.96) - 0.975) < 1e-9 and abs(Phi(2) - 0.97725) < 1e-9 and abs(Phi(1.5) - 0.9332) < 1e-9
    for lo, hi in [(-1, 1), (-0.8, 0.8), (0.3, 2.7), (-3, -0.5)]:
        approx = 0.5 * (erf_as(hi / sqrt(2)) - erf_as(lo / sqrt(2)))
        assert abs(approx - (norm.cdf(hi) - norm.cdf(lo))) < 1e-6, (lo, hi)
    assert abs(norm.ppf(0.9) - 1.28) < 0.01 and abs(norm.ppf(0.975) - 1.96) < 0.001 and abs(norm.ppf(0.95) - 1.645) < 0.001
    # Mixed
    assert sp.integrate(sp.Rational(8, 100), (x, 2, 5)) == sp.Rational(24, 100)
    rain = sp.Rational(2, 5) * sp.integrate(sp.exp(-x / 2) / 2, (x, 2, sp.oo))
    assert sp.simplify(rain - sp.Rational(2, 5) * sp.exp(-1)) == 0
    # Practice
    grid = np.linspace(0, 60, 600001)[:-1] + 0.00005
    w = np.where(grid < 15, 15 - grid, np.where(grid < 45, 45 - grid, 75 - grid))
    assert abs((w <= 10).mean() - 1 / 3) < 1e-4 and abs((w >= 15).mean() - 1 / 2) < 1e-4
    lam = sp.Rational(1, 4)
    tail = lambda v: sp.integrate(lam * sp.exp(-lam * x), (x, v, sp.oo))
    assert sp.simplify(tail(4) - sp.exp(-1)) == 0 and sp.simplify(tail(2) - tail(6) - (sp.exp(-sp.Rational(1, 2)) - sp.exp(-sp.Rational(3, 2)))) == 0
    assert sp.simplify(tail(7) / tail(3) - tail(4)) == 0 and sp.simplify(tail(4 * sp.log(2)) - sp.Rational(1, 2)) == 0
    Fr = 1 - sp.exp(-x ** 2 / (2 * s ** 2))
    assert sp.simplify(Fr.subs(x, 2 * s) - Fr.subs(x, s) - (sp.exp(-sp.Rational(1, 2)) - sp.exp(-2))) == 0
    assert sp.simplify(1 - Fr.subs(x, 3 * s) - sp.exp(-sp.Rational(9, 2))) == 0
    assert sp.simplify(sp.diff(Fr, x) - x / s ** 2 * sp.exp(-x ** 2 / (2 * s ** 2))) == 0
    C = sp.solve(c * sp.integrate(X ** 2, (X, -1, 1)) - 1, c)[0]
    assert C == sp.Rational(3, 2)
    Fc = sp.integrate(C * t ** 2, (t, -1, X))
    assert sp.simplify(Fc - (X ** 3 + 1) / 2) == 0
    assert 1 - Fc.subs(X, sp.Rational(1, 2)) == sp.Rational(7, 16)
    assert Fc.subs(X, sp.Rational(1, 2)) - Fc.subs(X, -sp.Rational(1, 2)) == sp.Rational(1, 8)
    assert sp.integrate(x * sp.exp(-x), (x, 0, sp.oo)) == 1
    Fx = sp.integrate(t * sp.exp(-t), (t, 0, x))
    assert sp.simplify(Fx - (1 - (1 + x) * sp.exp(-x))) == 0
    assert sp.simplify(Fx.subs(x, 5) - Fx.subs(x, 2) - (3 * sp.exp(-2) - 6 * sp.exp(-5))) == 0
    assert sp.simplify(1 - Fx.subs(x, 7) - 8 * sp.exp(-7)) == 0
    b = sp.Symbol('b', positive=True)
    ft = (1 - t / a) / a  # right half of the triangle; the left half is its mirror image
    assert sp.simplify(2 * sp.integrate(ft, (t, 0, a)) - 1) == 0
    assert sp.simplify(sp.integrate(ft, (t, x, a)) - (a - x) ** 2 / (2 * a ** 2)) == 0
    sol = sp.solve(2 * sp.integrate(ft, (t, 0, b)) - sp.Rational(1, 2), b)
    assert any(sp.simplify(r - a * (1 - 1 / sp.sqrt(2))) == 0 for r in sol)
    Fm2 = sp.Rational(1, 4) + X / 2
    assert Fm2.subs(X, 0) == sp.Rational(1, 4) and 1 - Fm2.subs(X, 1) == sp.Rational(1, 4) and Fm2.subs(X, sp.Rational(1, 2)) == sp.Rational(1, 2)
    Fm = sp.Rational(1, 3) + sp.Rational(2, 3) * (X + 1) ** 2
    assert 1 - Fm.subs(X, -sp.Rational(2, 3)) == sp.Rational(16, 27) and Fm.subs(X, 0) == 1
    assert sp.Rational(1, 2) == (sp.pi / 2 - sp.pi / 4) / (sp.pi / 2)  # sin beats cos
    assert abs(2 * Phi(1.5) - 1 - 0.8664) < 1e-9
    # new practice: x^2/9, staircase vs 1-e^{-2y}, triangle on [0,2], c(2-x), c e^{-3y}, Uniform(2,8)
    F9 = x ** 2 / 9
    assert [F9.subs(x, 1), F9.subs(x, 2) - F9.subs(x, 1), 1 - F9.subs(x, 2)] == [sp.Rational(1, 9), sp.Rational(1, 3), sp.Rational(5, 9)]
    assert sp.diff(F9, x) == 2 * x / 9 and sp.diff(1 - sp.exp(-2 * x), x) == 2 * sp.exp(-2 * x)
    tri2 = sp.Piecewise((t, t <= 1), (2 - t, True))
    Ftri = lambda v: sp.integrate(tri2, (t, 0, v))
    assert Ftri(2) == 1 and Ftri(sp.Rational(3, 2)) - Ftri(sp.Rational(1, 2)) == sp.Rational(3, 4)
    assert sp.simplify(Ftri(sp.Rational(3, 2)) - (1 - sp.Rational(1, 2) ** 2 / 2)) == 0
    assert sp.solve(c * sp.integrate(2 - x, (x, 0, 2)) - 1, c) == [sp.Rational(1, 2)]
    Fl = sp.integrate((2 - t) / 2, (t, 0, x))
    assert sp.simplify(Fl - (x - x ** 2 / 4)) == 0 and Fl.subs(x, 1) == sp.Rational(3, 4)
    assert sp.solve(c * sp.integrate(sp.exp(-3 * x), (x, 0, sp.oo)) - 1, c) == [3]
    assert sp.integrate(3 * sp.exp(-3 * x), (x, 1, sp.oo)) == sp.exp(-3)
    assert [sp.Rational(3, 6), sp.Rational(1, 6), sp.Rational(1, 6)] == [sp.Rational(5 - 2, 6), sp.Rational(4 - 3, 6), sp.Rational(8 - 7, 6)]
    assert sp.solve((x - 2) / 6 - sp.Rational(1, 4), x) == [sp.Rational(7, 2)]
    print('q2 verify ok')


if __name__ == '__main__':
    verify()
    D.save()
