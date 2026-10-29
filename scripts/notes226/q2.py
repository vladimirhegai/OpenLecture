r"""Test 2 - Question 2: continuous random variables, PDFs and probability calculations (Lectures 9-11).

Layout (REWRITE_PLAN.md): you'll see -> the move -> Case 1-6 (formula, short example, full example in a
closed card, shortcut card) -> practice. Step words: Spot, Find c, Accumulate, Differentiate, Rewrite, Standardise,
Table, Jump, Plug in (the same words as Questions 1, 3 and 4).
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


D.P(r'**Lectures 9–11.** $X$ can be any number in an interval (a time, a voltage). Find $c$, the CDF, and probabilities.',
    cites=cite('L9', 3) + cite('L10', 2) + cite('L11', 1))

# =====================================================================================================
D.H('Question 2 in plain words')
D.P(r'**You’ll see:** a PDF or CDF formula, or a story with “uniform”, “exponential” or “normal”. Then parts (a), (b), (c).')
D.P(r'**The move: probability is area under the PDF.** The CDF is the area so far:')
D.EQ(r'P(a<X\le b)=\int_a^b f_X(x)\,dx=F_X(b)-F_X(a)', cites=cite('L9', 8))
D.L([r'**Accumulate:** $F_X(x)=P(X\le x)$ = the area left of $x$. Same word as the running total in Question 1.',
     r'**Differentiate:** the PDF is the slope of the CDF, $f_X=F_X^{\prime}$.',
     r'**One exact value has chance $0$:** $P(X=2)=0$. So $<$ and $\le$ give the same answer.'])
D.P(r'**Short example:** $X$ uniform on $[0,4]$ is flat at $\tfrac14$:')
D.EQ(r'P(1<X<3)=\underbrace{2}_{\text{width}}\cdot\underbrace{\frac14}_{\text{height}}=\frac12')
D.P(r'**Which case?** Look for the clue:')
D.T(['The question says…', 'Go to'],
    [[r'“$f_X(x)=c\cdot(\dots)$, find $c$”', 'Case 1'],
     [r'“find the CDF / PDF / $P(a<X<b)$”', 'Case 2'],
     ['“uniformly at random between…”', 'Case 3'],
     ['“exponential”, a lifetime, a waiting time', 'Case 4'],
     ['“normal” / “Gaussian” with $\\mu$, $\\sigma$', 'Case 5'],
     ['“with probability $q$ it is exactly…”, a CDF with a jump', 'Case 6']])

# =====================================================================================================
D.H('Case 1: find c (total area = 1)')
D.P(r'**You’ll see:** “$f_X(x)=c\cdot(\dots)$. Find $c$”, or “show this is a PDF”.')
D.P(r'**The move:** the whole area under a PDF is $1$. Write it, set it to $1$, solve:')
D.EQ(r'\int_{-\infty}^{\infty}f_X(x)\,dx=1', cites=cite('L9', 8))
D.L([r'**Spot:** the unknown is $c$.',
     r'**Find $c$:** integrate $f_X$ over the range where it isn’t $0$ (split at every break), set it to $1$.',
     r'**Check:** $f_X\ge0$ everywhere. It may be bigger than $1$, that’s fine.'], ordered=True)
D.P(r'**Short example:** $f_X(x)=c(1-x^4)$ on $[-1,1]$:')
D.EQ(r'c\Big[x-\frac{x^5}{5}\Big]_{-1}^{1}=\frac{8c}{5}=1\quad\Longrightarrow\quad c=\frac58')
p1q = 79 / 128
D.CARD(r'Full example (Practice 02 Q1): $\;f_X(x)=c(1-x^4)$ on $[-1,1]$: find $c$, the CDF, $P(|X|<\tfrac12)$',
       [(r'**Find $c$:** total area $=1$.', r'c\Big[x-\frac{x^5}{5}\Big]_{-1}^{1}=\frac{8c}{5}=1\quad\Longrightarrow\quad c=\frac58'),
        (r'**Accumulate:** the area from $-1$ up to $x$. It’s $0$ before $-1$ and $1$ after $1$.',
         r'F_X(x)=\frac58\int_{-1}^{x}(1-t^4)\,dt=\frac58\Big(x-\frac{x^5}{5}+\frac45\Big),\qquad -1\le x\le1'),
        (r'**Rewrite:** $|X|<\tfrac12$ means $-\tfrac12<X<\tfrac12$. The PDF is symmetric, so double the area on $[0,\tfrac12]$.',
         r'P\big(|X|<\tfrac12\big)=2\cdot\frac58\Big[x-\frac{x^5}{5}\Big]_0^{1/2}=\frac{79}{128}\approx ' + f4(p1q))],
       r'c=\frac58,\qquad P\big(|X|<\tfrac12\big)=\frac{79}{128}\approx ' + f4(p1q), cites=cite('P2', 1))
D.CARD(r'Shortcut: a triangle or rectangle PDF → use its area formula',
       [(r'Tutorial 4 Q2: $f(x)=\tfrac12-\tfrac14|x-3|$ on $[1,5]$ is a triangle: base $4$, peak height $f(3)=\tfrac12$.', r'\text{area}=\frac12\cdot4\cdot\frac12=1\quad\checkmark'),
        (r'Unknown height $c$, base $2a$ (Practice 02 Q2):', r'\frac12\cdot2a\cdot c=1\quad\Longrightarrow\quad c=\frac1a')],
       numbered=False, cites=cite('T4', 1))
D.CARD(r'Integrals you’ll need',
       [(r'Power rule:', r'\int x^n\,dx=\frac{x^{n+1}}{n+1}'),
        (r'Exponential (and $e^{-\lambda x}\to0$ as $x\to\infty$):', r'\int e^{-\lambda x}\,dx=-\frac1\lambda\,e^{-\lambda x}'),
        (r'By parts, for $x\,e^{-x}$ (take $u=x$):', r'\int x\,e^{-x}\,dx=-(x+1)\,e^{-x}'),
        (r'Shortcut (not from the lectures):', r'\int_0^{\infty}x^n\,e^{-\lambda x}\,dx=\frac{n!}{\lambda^{n+1}}')], numbered=False)

# =====================================================================================================
D.H('Case 2: PDF → CDF → probabilities')
D.P(r'**You’ll see:** “find the CDF”, “find the PDF from this CDF”, “find $P(a<X<b)$”.')
D.P(r'**The move:** go back and forth between the two, then turn every probability into $F$’s:')
D.EQ(r'F_X(x)=\int_{-\infty}^{x}f_X(t)\,dt\qquad\Longleftrightarrow\qquad f_X(x)=F_X^{\prime}(x)', cites=cite('L9', 8))
D.L([r'**Accumulate** (PDF → CDF): the area from the left end up to $x$. Do it piece by piece. $0$ before the range, $1$ after.',
     r'**Differentiate** (CDF → PDF): the slope of each piece.',
     r'**Rewrite** the probability with $F$’s (card below), then **plug in**.'], ordered=True)
D.CARD(r'Rewrite: turn any probability into $F$’s',
       [(r'Example: $F_X(x)=\tfrac x4$ on $[0,4]$.', ''),
        (r'Up to $b$:', r'P(X\le b)=F_X(b)\qquad\qquad P(X\le1)=\frac14'),
        (r'Above $a$:', r'P(X>a)=1-F_X(a)\qquad\qquad P(X>1)=\frac34'),
        (r'Between:', r'P(a<X<b)=F_X(b)-F_X(a)\qquad\qquad P(2<X<3)=\frac34-\frac24=\frac14'),
        (r'One point:', r'P(X=a)=0')], numbered=False, cites=cite('L9', 8))
D.P(r'**Short example:** $f_X(x)=\tfrac x2$ on $[0,2]$:')
D.EQ(r'F_X(x)=\int_0^x\frac t2\,dt=\frac{x^2}{4}\quad\Longrightarrow\quad P(X>1)=1-\frac14=\frac34')
D.CARD(r'Full example (Lecture 9): read a CDF, $\;F_X(x)=\tfrac x4$ on $[0,4]$',
       [(r'(a) $P(X\le-1)$: left of the range.', r'F_X(-1)=0'),
        (r'(b) $P(X\le1)$.', r'F_X(1)=\frac14'),
        (r'(c) $P(2<X\le3)$: **Rewrite** as a difference.', r'F_X(3)-F_X(2)=\frac34-\frac24=\frac14'),
        (r'(d) $P(X>1)$: one minus.', r'1-F_X(1)=\frac34'),
        (r'(e) $P(X=1)$: one point.', r'0'),
        (r'**Differentiate** for the PDF.', r'f_X(x)=\frac14,\qquad 0\le x\le4\quad(0\text{ elsewhere})')],
       r'0,\ \ \frac14,\ \ \frac14,\ \ \frac34,\ \ 0;\qquad f_X=\frac14\ \text{on }[0,4]', cites=cite('L9', 5))
D.CARD(r'Full example (Tutorial 4 Q2): a triangle PDF, piece by piece',
       [(r'$f(x)=\tfrac12-\tfrac14|x-3|$ on $[1,5]$. Split at the peak: left $\tfrac{x-1}{4}$, right $\tfrac{5-x}{4}$.', ''),
        (r'**Accumulate**, left half: the area of a small triangle.', r'F(x)=\int_1^x\frac{t-1}{4}\,dt=\frac{(x-1)^2}{8},\qquad 1\le x\le3'),
        (r'**Accumulate**, right half: $1$ minus the small triangle still to come.', r'F(x)=1-\frac{(5-x)^2}{8},\qquad 3\le x\le5'),
        (r'**Rewrite** $P(2<X<3.5)$.', r'F(3.5)-F(2)=\Big(1-\frac{1.5^2}{8}\Big)-\frac18=\frac{19}{32}\approx0.5938')],
       r'F(x)=\begin{cases}0,&x<1\\ \frac{(x-1)^2}{8},&1\le x\le3\\ 1-\frac{(5-x)^2}{8},&3\le x\le5\\ 1,&x>5\end{cases}', cites=cite('T4', 1))

# =====================================================================================================
D.H('Case 3: uniform')
D.P(r'**You’ll see:** “uniformly at random between $a$ and $b$”.')
D.P(r'**The move:** a flat PDF, so every probability is **length ÷ total length**:')
D.EQ(r'f_X(x)=\frac{1}{b-a},\qquad F_X(x)=\frac{x-a}{b-a},\qquad a\le x\le b', cites=cite('L10', 3))
D.EQ(r'P(\text{X lands in a piece})=\frac{\text{length of the piece}}{b-a}')
D.P(r'**Short example** (Tutorial 2 Q5): a bus comes uniformly between 1:00 and 1:30. Wait at least 10 minutes:')
D.EQ(r'P(X\ge10)=\frac{30-10}{30}=\frac23')
D.CARD(r'Full example (Tutorial 3 Q1): pick $X$ uniformly in $(0,\tfrac\pi2)$. Chance $\sin X>\cos X$?',
       [(r'**Spot:** uniform on $(0,\tfrac\pi2)$, total length $\tfrac\pi2$.', ''),
        (r'**Rewrite** the event: $\sin x$ passes $\cos x$ at $x=\tfrac\pi4$.', r'\sin X>\cos X\iff X>\frac\pi4'),
        (r'Length ÷ total length.', r'P=\frac{\frac\pi2-\frac\pi4}{\frac\pi2}=\frac12')],
       r'\frac12', cites=cite('T3', 1))

# =====================================================================================================
D.H('Case 4: exponential')
D.P(r'**You’ll see:** a lifetime or a waiting time, “exponential with $\lambda=\dots$” ($\lambda$ = the rate, per hour/minute).')
D.P(r'**The move:** use the **tail**. You’ll need it more than the CDF:')
D.EQ(r'f_X(x)=\lambda e^{-\lambda x},\qquad F_X(x)=1-e^{-\lambda x},\qquad P(X>x)=e^{-\lambda x}\qquad(x\ge0)', cites=cite('L10', 4))
D.L([r'**Spot:** exponential, and read $\lambda$. Given the **mean** instead? Then $\lambda=\dfrac{1}{\text{mean}}$.',
     r'**Rewrite** with tails: $P(a<X<b)=e^{-\lambda a}-e^{-\lambda b}$.',
     r'**Plug in.**'], ordered=True)
pl = exp(-1)
D.P(r'**Short example:** lifetime with $\lambda=0.002$ per hour. Lasts at least 500 hours:')
D.EQ(r'P(X>500)=e^{-0.002\cdot500}=e^{-1}\approx ' + f4(pl))
D.CARD(r'Memoryless: $\;P(X>s+t\mid X>s)=P(X>t)$',
       [(r'Time already waited doesn’t matter: an old part is as good as new.', ''),
        (r'To use it: “already lasted $s$, chance of $t$ more” is a ratio of tails.',
         r'\frac{P(X>s+t)}{P(X>s)}=\frac{e^{-\lambda(s+t)}}{e^{-\lambda s}}=e^{-\lambda t}')], numbered=False, cites=cite('L4', 1))
D.CARD(r'Full example (Tutorial 4 Q3): a TV tube is 10 years old, $\lambda=0.1$. Chance it lasts another 10?',
       [(r'**Spot:** exponential, $\lambda=0.1$, and “already lasted” → memoryless.', r'P(X>20\mid X>10)'),
        (r'**Rewrite** as a ratio of tails.', r'\frac{P(X>20)}{P(X>10)}=\frac{e^{-2}}{e^{-1}}=e^{-1}'),
        (r'Same as a new tube lasting 10 years.', r'P(X>10)=e^{-0.1\cdot10}=e^{-1}\approx ' + f4(pl))],
       r'e^{-1}\approx ' + f4(pl), cites=cite('T4', 1))

# =====================================================================================================
D.H('Case 5: Gaussian (normal)')
D.P(r'**You’ll see:** “normal with mean $\mu$ and standard deviation $\sigma$” (or variance $\sigma^2$): $X\sim N(\mu,\sigma^2)$.')
D.P(r'**The move:** you can’t integrate the bell curve. **Standardise** to $z$ and read $\Phi(z)=P(Z\le z)$ from the table:')
D.EQ(r'F_X(x)=\Phi\Big(\frac{x-\mu}{\sigma}\Big),\qquad \Phi(-z)=1-\Phi(z)', cites=cite('L11', 1))
D.L([r'**Spot:** read $\mu$ and $\sigma$. Given the **variance**? Take its square root first.',
     r'**Standardise** every number: $z=\dfrac{x-\mu}{\sigma}$.',
     r'**Rewrite** with $\Phi$: $P(X>x)=1-\Phi(z)$, $\;P(a<X<b)=\Phi(z_b)-\Phi(z_a)$. Negative $z$? $\Phi(-z)=1-\Phi(z)$.',
     r'**Table.**'], ordered=True)
D.T(['$z$', '0.5', '1.0', '1.28', '1.5', '1.645', '1.96', '2.0', '2.5'],
    [['$\\Phi(z)$', f4(Phi(.5)), f4(Phi(1)), f4(Phi(1.28)), f4(Phi(1.5)), '0.95', f4(Phi(1.96)), f'{Phi(2):.5f}', f'{Phi(2.5):.5f}']],
    cites=cite('L10', 6))
pz = 2 * Phi(1.6) - 1
D.P(r'**Short example:** $\mu=0$, $\sigma=0.5$, find $P(X<1)$:')
D.EQ(r'z=\frac{1-0}{0.5}=2\quad\Longrightarrow\quad P(X<1)=\Phi(2)=' + f'{Phi(2):.5f}')
D.CARD(r'Shortcut: a symmetric interval, $\;P(|X-\mu|<k\sigma)=2\Phi(k)-1$',
       [(r'Both tails are the same size, so take $\Phi(k)$ and remove one tail twice.', r'\Phi(k)-\Phi(-k)=\Phi(k)-\big(1-\Phi(k)\big)=2\Phi(k)-1'),
        (r'Example: within $1.5\sigma$ of the mean.', r'2(' + f4(Phi(1.5)) + r')-1=' + f4(2 * Phi(1.5) - 1))], numbered=False)
D.CARD(r'Backwards: given a probability, find $x$ $\;\Longrightarrow\;x=\mu+z\sigma$',
       [(r'Find the $z$ in the table whose $\Phi(z)$ is the probability **below** $x$, then undo the standardising.', r'x=\mu+z\,\sigma'),
        (r'Top $5\%$ → $95\%$ below → $z=1.645$. Middle $95\%$ → $\Phi(z)=0.975$ → $z=1.96$.', '')], numbered=False)
D.CARD(r'Full example (Lecture 11): sensor error, $\;\mu=0$, $\;\sigma=0.5$. Chance $|X|<0.8$?',
       [(r'**Rewrite:** $|X|<0.8$ means $-0.8<X<0.8$.', ''),
        (r'**Standardise** both ends.', r'z=\frac{\pm0.8-0}{0.5}=\pm1.6'),
        (r'Negative $z$: flip it.', r'\Phi(1.6)-\Phi(-1.6)=\Phi(1.6)-\big(1-\Phi(1.6)\big)=2\Phi(1.6)-1'),
        (r'**Table:** $\Phi(1.6)=' + f4(Phi(1.6)) + '$.', r'2(' + f4(Phi(1.6)) + r')-1=' + f4(pz))],
       f4(pz), cites=cite('L11', 3))
D.CARD(r'Full example (Tutorial 4 Q4): scores $N(500,100^2)$. Which score is the top $10\%$?',
       [(r'**Rewrite:** top $10\%$ means $90\%$ below.', r'\Phi\Big(\frac{x-500}{100}\Big)=0.90'),
        (r'**Table, backwards:** $\Phi(1.28)=' + f4(Phi(1.28)) + '$ is closest to $0.90$.', r'z\approx1.28'),
        (r'Undo the standardising.', r'x=500+1.28\cdot100=628')],
       r'\text{about }628', cites=cite('T4', 1))
# Abramowitz-Stegun 7.1.26 erf, written in the graph's expression language
D.CO('warning', r'**Variance or standard deviation?** “$\sigma^2=2.25$” means $\sigma=1.5$. Dividing by $2.25$ is the most common lost mark.')
b95, b89 = Phi(round(15 / 7, 2)), Phi(round(9 / 7, 2))
D.TRY('Case 5 · Blood pressure · Practice 03 Q8',
      r'Diastolic blood pressure is normal with $\mu=80$, $\sigma=7$ (mm Hg). $\ge95$ is hypertensive; strictly between $89$ and $95$ is mild hypertension. '
      'What percent of people are in each group?',
      [S(r'**Spot:** Gaussian, $\mu=80$, $\sigma=7$.'),
       S(r'**Standardise** both cut-offs (2 decimals, like the table).', (r'z_{95}=\frac{95-80}{7}\approx2.14', r'z_{89}=\frac{89-80}{7}\approx1.29')),
       S(r'**Rewrite**, hypertensive: the right tail. **Table.**', r'P(X\ge95)=1-\Phi(2.14)=1-' + f'{b95:.5f}' + '=' + f'{1 - b95:.5f}'),
       S(r'**Rewrite**, mild: between the two. **Table.**', (r'P(89<X<95)=\Phi(2.14)-\Phi(1.29)', r'=' + f'{b95:.5f}' + '-' + f4(b89) + '=' + f'{b95 - b89:.4f}'))],
      f'Mild ≈ {100 * (b95 - b89):.2f}%, hypertensive ≈ {100 * (1 - b95):.2f}%', cites=cite('P3', 3))

# =====================================================================================================
D.H('Case 6: mixed (a jump and a ramp)')
D.P(r'**You’ll see:** “with probability $q$ it is exactly $x_0$, otherwise it is spread over…”, or a CDF that jumps **and** ramps.')
D.P(r'**The move:** the jump is an exact chance. The spread part only has the **leftover** area $1-q$:')
D.EQ(r'P(X=x_0)=\text{jump size},\qquad f_{\text{spread}}=(1-q)\times(\text{its usual PDF})', cites=cite('L10', 8))
D.L([r'**Jump:** $P(X=x_0)=q$ (or read the jump size off the CDF).',
     r'**Spread:** the usual PDF times $1-q$.',
     r'**Rewrite:** any probability = the jumps inside the range + the area over the range.'], ordered=True)
D.P(r'**Short example:** signal lost ($X=0$) with chance $0.2$, otherwise uniform on $(0,10)$:')
D.EQ(r'f_{\text{spread}}=0.8\cdot\frac1{10}=0.08\quad\Longrightarrow\quad P(2<X<5)=0.08\cdot3=0.24')
D.CARD(r'Full example (Lectures 10–11): received signal level, the CDF',
       [(r'**Jump** at $0$: the lost signal.', r'P(X=0)=0.2'),
        (r'**Spread:** uniform on $(0,10)$ scaled by $0.8$.', r'f(x)=0.8\cdot\frac1{10}=0.08,\qquad 0<x<10'),
        (r'**Accumulate:** jump first, then the ramp.', r'F_X(x)=\begin{cases}0,&x<0\\ 0.2+0.08x,&0\le x<10\\ 1,&x\ge10\end{cases}'),
        (r'**Rewrite** $P(2<X<5)$: the jump at $0$ isn’t inside, so only area.', r'F_X(5)-F_X(2)=0.6-0.36=0.24')],
       r'\text{jump }0.2\text{ at }0,\ \text{then a ramp up to }1\text{ at }x=10', cites=cite('L11', 4) + cite('L11', 5))
D.GRAPH(['title "CDF of the received signal: a jump, then a ramp"', 'x -2 12 label="$x$" height=230', 'y 0 1.1 label="$F_X(x)$"',
         'segment "-2" "0" "0" "0" color=2', 'segment "0" "0.2" "10" "1" color=2', 'segment "10" "1" "12" "1" color=2',
         'point "0" "0.2" color=2', 'segment "0" "0" "0" "0.2" color=0 dash', 'text "1.6" "0.12" "jump $=0.2$"',
         'text "6.8" "0.6" "slope $0.08$"'],
        intro='**Discrete = all jumps, continuous = all slope, mixed = both.**')
rn, r1m = 0.4 * exp(-1), 0.6 + 0.4 * (1 - exp(-0.5))
D.TRY('Case 6 · Daily rainfall',
      r'On a given day it doesn’t rain with probability $0.6$ ($X=0$). If it rains, the amount $X$ (mm) is exponential with $\lambda=0.5$. '
      r'(a) Find the CDF of $X$. (b) Find $P(X>2)$. (c) Find $P(X\le1)$.',
      [S(r'**Spot:** an exact value with chance $0.6$, plus a spread → Case 6.'),
       S(r'(a) **Jump** of $0.6$ at $0$, then **spread:** the exponential CDF scaled by $0.4$.', r'F_X(x)=\begin{cases}0,&x<0\\ 0.6+0.4\left(1-e^{-0.5x}\right),&x\ge0\end{cases}'),
       S(r'(b) **Rewrite:** only rainy days can go above 2. Exponential tail times $0.4$.', r'P(X>2)=0.4\,e^{-0.5\cdot2}=0.4e^{-1}\approx ' + f4(rn)),
       S(r'(c) **Rewrite:** $F_X(1)$, which includes the jump at $0$.', r'P(X\le1)=0.6+0.4(1-e^{-0.5})\approx ' + f4(r1m))],
      f'(a) jump $0.6$ at $0$, then $0.6+0.4(1-e^{{-0.5x}})$ (b) $\\approx {f4(rn)}$ (c) $\\approx {f4(r1m)}$')

# =====================================================================================================
D.H('Practice Questions')
D.CO('tip', r'''**Question 2 is always these cases, in parts (a), (b), (c).** Spot the clue, run its steps:

1. **Find $c$:** total area $=1$ (triangle/rectangle: area formula).
2. **PDF ↔ CDF:** Accumulate (area so far), Differentiate (slope), Rewrite with $F$'s.
3. **Uniform:** length ÷ total length.
4. **Exponential:** $P(X>x)=e^{-\lambda x}$; “already lasted” → memoryless.
5. **Gaussian:** $z=\frac{x-\mu}{\sigma}$ → $\Phi$ table; $\Phi(-z)=1-\Phi(z)$; backwards $x=\mu+z\sigma$.
6. **Mixed:** jump = exact chance; spread × $(1-q)$; add jumps + area.''')
D.P('Test-style, easy → hard. Solve on paper first, then open the solution.')

D.Q('Case 3 · Uniform · Tutorial 4 Q5',
    'Flights leave every half hour (9:00, 9:30, 10:00, …). A passenger arrives at a uniform random time between 8:45 and 9:45 A.M. '
    'Find the probability the passenger waits (a) **at most 10 minutes**, (b) **at least 15 minutes**.',
    [S(r'**Type:** uniform → Case 3. $T$ = minutes after 8:45, total length $60$. Flights leave at $T=15,\ 45,\ 75$.', r'f_T(t)=\frac1{60},\quad 0\le t\le60'),
     S(r'(a) **Rewrite:** wait $\le10$ means arriving in the 10 minutes before a flight.', r'T\in[5,15]\cup[35,45]'),
     S(r'Length ÷ total length.', r'P=\frac{10+10}{60}=\frac13'),
     S(r'(b) **Rewrite:** wait $\ge15$ means the next flight is 15+ minutes away.', r'T\in[15,30]\cup[45,60]'),
     S(r'Length ÷ total length.', r'P=\frac{15+15}{60}=\frac12')],
    r'(a) $\tfrac13$ (b) $\tfrac12$', diff='introductory', cites=cite('T4', 1))

ea, eb, med = exp(-1), exp(-0.5) - exp(-1.5), 4 * log(2)
D.Q('Case 4 · Exponential, memoryless · like Lecture 10',
    r'The length $X$ (minutes) of a phone call is exponential with $\lambda=0.25$. Find (a) $P(X>4)$, (b) $P(2<X<6)$, '
    r'(c) the chance a call that has already lasted 3 minutes lasts **more than 7** in total, (d) the time $t$ with $P(X>t)=\tfrac12$.',
    [S(r'**Type:** exponential, $\lambda=0.25$ → Case 4.'),
     S(r'(a) **Rewrite** as a tail. **Plug in.**', r'P(X>4)=e^{-0.25\cdot4}=e^{-1}\approx ' + f4(ea)),
     S(r'(b) **Rewrite:** difference of two tails.', r'P(2<X<6)=e^{-0.5}-e^{-1.5}\approx ' + f4(eb)),
     S(r'(c) **Memoryless:** 4 more minutes, as if new.', r'P(X>7\mid X>3)=P(X>4)=e^{-1}\approx ' + f4(ea)),
     S(r'(d) **Backwards:** set the tail to $\tfrac12$, take $\ln$.', r'e^{-0.25t}=\frac12\quad\Longrightarrow\quad t=4\ln2\approx ' + f'{med:.2f}' + r'\text{ min}')],
    f'(a) $\\approx {f4(ea)}$ (b) $\\approx {f4(eb)}$ (c) $\\approx {f4(ea)}$ (d) $4\\ln2\\approx {med:.2f}$ min', diff='introductory',
    cites=cite('L10', 4))

ra, rb = exp(-0.5) - exp(-2), exp(-4.5)
D.Q('Case 2 · CDF → probabilities and PDF · Practice 02 Q4',
    r'''The Rayleigh random variable $R$ has CDF

$$
F_R(r)=\begin{cases}0,&r<0\\ 1-e^{-r^2/(2\sigma^2)},&r\ge0\end{cases}
$$

(a) Find $P(\sigma\le R\le2\sigma)$ and $P(R>3\sigma)$. (b) Find the PDF of $R$.''',
    [S(r'**Type:** a CDF is given → Case 2.'),
     S(r'(a) **Rewrite** as a difference. $\sigma$ cancels in each power.', r'P(\sigma\le R\le2\sigma)=F_R(2\sigma)-F_R(\sigma)=e^{-1/2}-e^{-2}\approx ' + f4(ra)),
     S(r'**Rewrite** as one minus: $\tfrac{(3\sigma)^2}{2\sigma^2}=\tfrac92$.', r'P(R>3\sigma)=1-F_R(3\sigma)=e^{-9/2}\approx ' + f4(rb)),
     S(r'(b) **Differentiate** (chain rule: the inside $-\tfrac{r^2}{2\sigma^2}$ has slope $-\tfrac{r}{\sigma^2}$).', r'f_R(r)=\frac{r}{\sigma^2}\,e^{-r^2/(2\sigma^2)},\qquad r\ge0')],
    f'(a) $e^{{-1/2}}-e^{{-2}}\\approx {f4(ra)}$; $e^{{-9/2}}\\approx {f4(rb)}$ (b) $\\dfrac{{r}}{{\\sigma^2}}e^{{-r^2/(2\\sigma^2)}}$ for $r\\ge0$',
    cites=cite('P2', 1))

D.Q('Case 1 + 2 · Find $c$, then the CDF · Tutorial 5 Q5',
    r'$X$ has PDF $f_X(x)=Cx^2$ for $|x|\le1$, and $0$ otherwise. (a) Find $C$. (b) Find the CDF. (c) Find $P(X>\tfrac12)$ and $P(|X|<\tfrac12)$.',
    [S(r'(a) **Type:** unknown constant → Case 1. **Find $c$:** total area $=1$.', r'C\int_{-1}^{1}x^2\,dx=\frac{2C}{3}=1\quad\Longrightarrow\quad C=\frac32'),
     S(r'(b) **Accumulate** from $-1$ up to $x$ (Case 2).', r'F_X(x)=\int_{-1}^{x}\frac32t^2\,dt=\frac{x^3+1}{2},\qquad -1\le x\le1'),
     S(r'(c) **Rewrite** as one minus.', r'P(X>\tfrac12)=1-\frac{\frac18+1}{2}=\frac{7}{16}'),
     S(r'**Rewrite** as a difference. Small, because the PDF is near $0$ around $x=0$.', r'F(\tfrac12)-F(-\tfrac12)=\frac{\frac98-\frac78}{2}=\frac18')],
    r'(a) $C=\tfrac32$ (b) $\tfrac{x^3+1}{2}$ on $[-1,1]$ (c) $\tfrac7{16}$ and $\tfrac18$', cites=cite('T5', 1))

t25, t7 = 3 * exp(-2) - 6 * exp(-5), 8 * exp(-7)
D.Q('Case 1 + 2 · Find $c$ by parts · Tutorial 4 Q1',
    r'The time $X$ (minutes) between seeing two runners has PDF $f(x)=\lambda x e^{-x}$ for $x>0$. (a) Find $\lambda$. (b) Find the CDF. '
    r'(c) Find the probability the next runner is seen in 2 to 5 minutes, and in at least 7 minutes.',
    [S(r'**Type:** unknown constant → Case 1. First the integral, **by parts** ($u=x$, $dv=e^{-x}dx$):', r'\int xe^{-x}\,dx=-xe^{-x}+\int e^{-x}\,dx=-(x+1)e^{-x}'),
     S(r'(a) **Find $c$:** total area $=1$. (Shortcut: $\int_0^\infty xe^{-x}dx=\tfrac{1!}{1^2}=1$.)', r'\lambda\Big[-(x+1)e^{-x}\Big]_0^{\infty}=\lambda(0+1)=1\quad\Longrightarrow\quad\lambda=1'),
     S(r'(b) **Accumulate** from $0$ to $x$ ($0$ for $x<0$).', r'F(x)=\Big[-(t+1)e^{-t}\Big]_0^{x}=1-(1+x)e^{-x}'),
     S(r'(c) **Rewrite** as a difference.', r'P(2<X<5)=F(5)-F(2)=3e^{-2}-6e^{-5}\approx ' + f4(t25)),
     S(r'**Rewrite** as one minus.', r'P(X\ge7)=1-F(7)=8e^{-7}\approx ' + f4(t7))],
    f'$\\lambda=1$; $F(x)=1-(1+x)e^{{-x}}$; $\\approx {f4(t25)}$ and $\\approx {f4(t7)}$', cites=cite('T4', 1))

tb = 1 - 1 / sqrt(2)
D.Q('Case 1 + 2 · a triangle, then work backwards · Practice 02 Q2',
    r'$X$ has a triangle PDF: $0$ at $x=-a$, peak height $c$ at $x=0$, back to $0$ at $x=a$. '
    r'(a) Find $c$ and $f_X(x)$. (b) Find the CDF. (c) Find $b$ with $P(|X|<b)=\tfrac12$.',
    [S(r'(a) **Type:** unknown height → Case 1. **Find $c$** with the triangle shortcut: base $2a$, height $c$.', r'\frac12(2a)c=1\quad\Longrightarrow\quad c=\frac1a'),
     S(r'The two sides are straight lines down from the peak.', r'f_X(x)=\frac1a\Big(1-\frac{|x|}{a}\Big),\qquad |x|\le a'),
     S(r'(b) **Accumulate:** left half = a small triangle; right half = $1$ minus the small triangle still to come.',
       r'F_X(x)=\begin{cases}0,&x<-a\\ \frac{(a+x)^2}{2a^2},&-a\le x\le0\\ 1-\frac{(a-x)^2}{2a^2},&0\le x\le a\\ 1,&x>a\end{cases}'),
     S(r'(c) **Rewrite:** $F(b)-F(-b)$. Each tail outside $[-b,b]$ is $\tfrac{(a-b)^2}{2a^2}$.', r'1-\frac{(a-b)^2}{a^2}=\frac12\quad\Longrightarrow\quad\frac{a-b}{a}=\frac1{\sqrt2}'),
     S(r'Solve for $b$.', r'b=a\Big(1-\frac1{\sqrt2}\Big)\approx ' + f'{tb:.3f}' + r'\,a')],
    r'(a) $c=\tfrac1a$ (b) as above (c) $b=a(1-\tfrac1{\sqrt2})\approx' + f'{tb:.3f}' + 'a$', cites=cite('P2', 1))

r1 = Phi(round(1 / 1.5, 2))
r5 = 1 - norm.cdf(5 / 1.5)
D.Q('Case 5 · Gaussian · Tutorial 6 Q5',
    r'A rover’s distance travelled is $X\sim N(\mu,\sigma^2)$ with $\mu=500$ m and $\sigma^2=2.25$ m². Find (a) $P(X<500)$, (b) $P(X=501)$, (c) $P(X>501)$ and $P(X>505)$.',
    [S(r'**Type:** normal → Case 5. **Spot:** that’s the variance, so take the root.', r'\sigma=\sqrt{2.25}=1.5'),
     S(r'(a) $500$ is the centre: half the bell is below it.', r'P(X<500)=0.5'),
     S(r'(b) One point of a continuous $X$.', r'P(X=501)=0'),
     S(r'(c) **Standardise**, then **Rewrite** as one minus. **Table.**', (r'z=\frac{501-500}{1.5}\approx0.67', r'P(X>501)=1-\Phi(0.67)=1-' + f4(r1) + '=' + f4(1 - r1))),
     S(r'$z=\tfrac{5}{1.5}\approx3.33$ is off the table ($\Phi\approx1$).', r'P(X>505)=1-\Phi(3.33)\approx ' + f4(r5))],
    r'(a) $0.5$ (b) $0$ (c) $\approx' + f4(1 - r1) + r'$ and $\approx' + f4(r5) + '$', cites=cite('T6', 1))

rw = 2 * Phi(1.5) - 1
D.Q('Case 5 · Gaussian, backwards · like Tutorial 4 Q4',
    r'Resistances are normal with $\mu=100\ \Omega$ and variance $4\ \Omega^2$. '
    r'(a) What fraction are within $100\pm3\ \Omega$? (b) Find $t$ so that $95\%$ are within $100\pm t$. (c) Which value is exceeded by only $5\%$?',
    [S(r'**Type:** normal → Case 5. **Spot:** variance $4$, so $\sigma=2$.', r'\sigma=2'),
     S(r'(a) **Standardise:** $z=\tfrac32=1.5$. Symmetric interval shortcut.', r'2\Phi(1.5)-1=2(' + f4(Phi(1.5)) + ')-1=' + f4(rw)),
     S(r'(b) **Backwards:** $2\Phi(z)-1=0.95$, so $\Phi(z)=0.975$. Then $t=z\sigma$.', r'z=1.96\quad\Longrightarrow\quad t=1.96\cdot2=3.92\ \Omega'),
     S(r'(c) **Backwards**, one tail: $\Phi(z)=0.95$, so $z=1.645$. Then $x=\mu+z\sigma$.', r'x=100+1.645\cdot2=103.29\ \Omega')],
    f'(a) ${f4(rw)}$ (b) $t=3.92\\ \\Omega$ (c) $103.29\\ \\Omega$')

D.Q('Case 6 · a CDF with two jumps',
    r'''A clipped sensor reading $X$ has CDF

$$
F_X(x)=\begin{cases}0,&x<0\\ 0.25+\tfrac x2,&0\le x<1\\ 1,&x\ge1\end{cases}
$$

(a) Why is $X$ mixed? (b) Find $P(X=0)$ and $P(X=1)$. (c) Find $P(0<X<1)$ and $P(X\le0.5)$. (d) Find the PDF of the spread part.''',
    [S(r'(a) **Type:** $F$ jumps (exact values with real chance) **and** ramps → Case 6.', r'\text{jumps at }0\text{ and }1,\ \text{ramp in between}'),
     S(r'(b) **Jump** sizes. At $1$, $F$ goes from $0.25+0.5=0.75$ up to $1$.', r'P(X=0)=0.25,\qquad P(X=1)=1-0.75=0.25'),
     S(r'(c) **Rewrite:** only the ramp is strictly inside $(0,1)$.', r'P(0<X<1)=0.75-0.25=0.5'),
     S(r'$P(X\le0.5)$ is just $F(0.5)$, jump at $0$ included.', r'P(X\le0.5)=F(0.5)=0.25+0.25=0.5'),
     S(r'(d) **Differentiate** the ramp. Check: $0.25+0.25+0.5=1$.', r'f(x)=\frac12,\qquad 0<x<1')],
    r'(b) $0.25$, $0.25$ (c) $0.5$, $0.5$ (d) $\tfrac12$ on $(0,1)$')

D.Q('Case 6 · Practice 02 Q3',
    r'''$X$ has CDF

$$
F_X(x)=\begin{cases}0,&x<-1\\ \tfrac13+\tfrac23(x+1)^2,&-1\le x\le0\\ 1,&x>0\end{cases}
$$

Find the probabilities of $A=\{X>\tfrac13\}$, $B=\{|X|\ge1\}$, $C=\{|X-\tfrac13|<1\}$, $D=\{X<0\}$.''',
    [S(r'**Type:** $F$ jumps from $0$ to $\tfrac13$ at $x=-1$, then rises smoothly → Case 6.', r'P(X=-1)=\frac13'),
     S(r'$A$: **Rewrite** as one minus. $X$ is never above $0$.', r'P(A)=1-F_X(\tfrac13)=0'),
     S(r'$B$: $X\ge1$ can’t happen, and $X\le-1$ means $X=-1$ (the jump).', r'P(B)=F_X(-1)=\frac13'),
     S(r'$C$ is $-\tfrac23<X<\tfrac43$. **Rewrite**; no jump at $-\tfrac23$.', r'P(C)=1-F_X(-\tfrac23)=1-\Big(\frac13+\frac23\cdot\frac19\Big)=\frac{16}{27}'),
     S(r'$D$: no jump at $0$ ($\tfrac13+\tfrac23=1$), so $P(X<0)=F_X(0)$.', r'P(D)=F_X(0)=1')],
    r'$P(A)=0$, $P(B)=\tfrac13$, $P(C)=\tfrac{16}{27}$, $P(D)=1$', diff='advanced', cites=cite('P2', 1))


def erf_as(x):
    """Abramowitz-Stegun 7.1.26, exactly as the graph's let lines compute it."""
    t = 1 / (1 + 0.3275911 * abs(x))
    y = 1 - ((((1.061405429 * t - 1.453152027) * t + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * exp(-x * x)
    return y if x >= 0 else -y


def verify():
    import numpy as np
    import sympy as sp
    x, t, c, s, a = sp.symbols('x t c sigma a', positive=True)
    X = sp.Symbol('X', real=True)
    # Type 1
    assert sp.integrate(x / 2, (x, 0, 2)) == 1
    assert sp.solve(c * sp.integrate(1 - X ** 4, (X, -1, 1)) - 1, c) == [sp.Rational(5, 8)]
    F = sp.Rational(5, 8) * sp.integrate(1 - t ** 4, (t, -1, X))
    assert sp.simplify(F - sp.Rational(5, 8) * (X - X ** 5 / 5 + sp.Rational(4, 5))) == 0
    assert F.subs(X, sp.Rational(1, 2)) - F.subs(X, -sp.Rational(1, 2)) == sp.Rational(79, 128)
    tri = sp.Piecewise((sp.Rational(1, 2) - sp.Abs(t - 3) / 4, (t >= 1) & (t <= 5)), (0, True))
    assert sp.integrate(tri, (t, 1, 5)) == 1
    Ft = lambda v: sp.integrate(tri, (t, 1, v))
    assert sp.simplify(Ft(2) - sp.Rational(1, 8)) == 0 and sp.simplify(Ft(sp.Rational(7, 2)) - Ft(2) - sp.Rational(19, 32)) == 0
    # Type 3
    assert sp.integrate(sp.Rational(1, 500) * sp.exp(-x / 500), (x, 500, sp.oo)) == sp.exp(-1)
    assert sp.Rational(30 - 10, 30) == sp.Rational(2, 3)
    # Type 4
    assert abs(Phi(1.6) - 0.9452) < 1e-9 and abs(Phi(1.28) - 0.8997) < 1e-9
    assert abs(Phi(2.14) - 0.98382) < 1e-9 and abs(Phi(0.67) - 0.7486) < 1e-9 and abs(Phi(1.29) - 0.9015) < 1e-9
    assert abs(Phi(1.96) - 0.975) < 1e-9 and abs(Phi(2) - 0.97725) < 1e-9 and abs(Phi(1.5) - 0.9332) < 1e-9
    for lo, hi in [(-1, 1), (-0.8, 0.8), (0.3, 2.7), (-3, -0.5)]:
        approx = 0.5 * (erf_as(hi / sqrt(2)) - erf_as(lo / sqrt(2)))
        assert abs(approx - (norm.cdf(hi) - norm.cdf(lo))) < 1e-6, (lo, hi)
    assert abs(norm.ppf(0.9) - 1.28) < 0.01 and abs(norm.ppf(0.975) - 1.96) < 0.001 and abs(norm.ppf(0.95) - 1.645) < 0.001
    # Type 5
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
    print('q2 verify ok')


if __name__ == '__main__':
    verify()
    D.save()
