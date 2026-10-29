# ELEC 226 Test 2 notes: rewrite plan

**Test 2:** Fri Oct 30 · 40 min · closed book · **no formula sheet** · Lectures 7–15.
Four notes, one per test question (keep that split, it matches the test):
Q1 discrete RVs · Q2 continuous RVs · Q3 mean and variance · Q4 functions of a RV.

**Goal:** the same treatment as the ELEC 231 midterm note. Each kind of question becomes: what you'll see → the move
→ steps → cases (short example + full example in a closed card) → practice. Theory goes in closed "Why?" boxes.
Nothing on the test gets dropped. It moves into a step, a case, a card or a box.

---

## 1. What's wrong with the current notes (live versions, rev 11–16)

- **Formula tables you're told to "memorise"**: 6 discrete families, 2 continuous, 8 means/variances. Each row is a
  formula with no example. Too condensed.
- **Steps that do 2–3 things at once**: "Label and group", "(a), (b) Read the CDF", inline math mid-sentence.
- **Examples are always open.** You see the answer before you try.
- **Q1 opens with a Test 1 counting review** (a table + 5 try-its) before any Test 2 content.
- **"In plain words" repeats the steps**, then the section repeats them again (Q4 has Step 1/2/3 twice).
- **Reminder callouts** (calculus, Test 1) sit in the middle of the method.

## 2. What you have to learn (from Lectures 7–15, Tutorials 3–6, Practice 02–03)

Every item below gets a case or a card. ✓ = already in the notes and will be kept (rewritten). + = gap to add.

### Q1 · Discrete random variables (Lec 7–9, Tutorial 3, Practice 02 Q5–6, Practice 03 Q5, Q7)
- ✓ Build a PMF from an experiment (coins, dice, chips without replacement)
- ✓ Find the constant $c$ in a PMF (geometric series, $e^\lambda$ series)
- ✓ CDF: PMF → staircase, staircase → PMF, $P(a<X\le b)$ from $F$, $<$ vs $\le$
- ✓ Families: Bernoulli, Binomial, Geometric, Negative Binomial, Hypergeometric, Poisson (Lec 8's list)
- ✓ Poisson: scale $\lambda$ to the time asked ("7 per week, one day")
- ✓ Two families in one question (Poisson inside, Binomial/Geometric outside: Tutorial 3 Q6)
- ✓ Geometric tail $P(N>k)=(1-p)^k$, $P(N\text{ even})$, $P(N=k\mid N\le m)$ (Practice 03 Q7)
- Counting (Test 1) → shrink to 3 closed cards ($n^k$, ${}_nP_k$, $\binom nk$, each with one example)

### Q2 · Continuous random variables (Lec 9–11, Tutorial 4, Practice 02 Q1–4)
- ✓ Find $c$ in a PDF (area = 1), including triangle/piecewise PDFs
- ✓ PDF → CDF (area so far, piece by piece) and CDF → PDF (slope)
- ✓ Probabilities from $F$; $P(X=a)=0$; find $b$ with $P(|X|<b)=\tfrac12$ (Practice 02 Q2)
- ✓ Uniform (length ÷ total length), exponential (tail $e^{-\lambda x}$, memoryless: Tutorial 4 Q3)
- ✓ Gaussian: standardise, $\Phi$ table, $\Phi(-z)=1-\Phi(z)$, backwards (top 10%), $2\Phi(k)-1$
- ✓ Mixed: CDF with a jump (Lec 10–11 received signal, Practice 02 Q3)
- ✓ Rayleigh from its CDF (Practice 02 Q4): stays a practice question, not a family to memorise

### Q3 · Mean and variance (Lec 11–13, Tutorial 5, Practice 03 Q1–6, Q9, Q11)
- ✓ $E[X]$ and $E[g(X)]$ (sum or integral); symmetric PDF shortcut; mixed $X$
- ✓ $\operatorname{Var}=E[X^2]-(E[X])^2$, $\sigma$
- ✓ Family means/variances (cards, not a table)
- ✓ Mean from a CDF: staircase → PMF; smooth → PDF; tail formula $\int_0^\infty(1-F)\,dt$ (Tutorial 5 Q3, Practice 03 Q1)
- ✓ Rules: $E[aX+b]$, $\operatorname{Var}(aX+b)=a^2\operatorname{Var}$, $E[X^2]=\operatorname{Var}+\mu^2$, expand $(2-X)^2$
- ✓ Moments: raw $E[X^n]$, central $E[(X-\mu)^n]$ (story-so-far page): one line + example
- ✓ Mars canisters $E[x]$ vs $E[y]$ (Practice 03 Q6)
- Markov / Chebyshev: Practice 03 only, **not in the lectures** → closed optional box with one example

### Q4 · Functions of a random variable (Lec 13–15, Tutorial 6, Tutorial 5 Q5c)
- ✓ What type is $Y$: discrete → discrete, staircase → discrete, smooth → continuous, flat piece → mixed (Lec 13)
- ✓ Discrete $Y$: add the probabilities that land on the same value
- ✓ Monotonic: the CDF method, $F_Y=F_X(g^{-1}(y))$; decreasing flips it to $1-F_X(\dots)$ (Lec 14–15)
- ✓ $Y=aX+b$ for $a>0$, $a<0$, $a=0$ (Lec 15)
- ✓ Non-monotonic: DAD (Distribution → Accumulation → Differentiation), $X^2$, $|X|$, $\cos X$ (Lec 15)
- ✓ Flat piece → a jump (clipping, timeout)
- ✓ Tutorial 6: $1/X$ in general, $\ln X$, $e^X$, $|X|$

The course teaches the CDF method and DAD. You said shortcuts are welcome even if untaught, so each case also gets a
**Shortcut** card (marked "not from the lectures: use it to go faster or to check"):
- Q4 monotonic: $f_Y(y)=f_X\big(g^{-1}(y)\big)\,\Big|\dfrac{d}{dy}g^{-1}(y)\Big|$
- Q4 $Y=X^2$: $f_Y(y)=\dfrac{f_X(\sqrt y)+f_X(-\sqrt y)}{2\sqrt y}$; $Y=|X|$: $f_Y(y)=f_X(y)+f_X(-y)$
- Q4 $aX+b$ of a Gaussian is Gaussian $N(a\mu+b,a^2\sigma^2)$; of a uniform is uniform
- Q3 $\int_0^\infty x^ne^{-\lambda x}dx=\dfrac{n!}{\lambda^{n+1}}$; symmetric PDF → mean = centre; $E[X^2]=\operatorname{Var}+\mu^2$
- Q2 uniform = length ÷ length; exponential tail $e^{-\lambda x}$; triangle/rectangle PDF → area formula for $c$
- Q1 "at least one" = $1-P(0)$; geometric tail $P(X>k)=(1-p)^k$; Binomial "at least $m$" = $1-$ (the few below)
Markov/Chebyshev stay a box (they're a topic, not a shortcut), but not marked optional: Practice 03 asks them.

---

## 3. One layout for every section (same as the 231 note)

| # | Part | Rule |
|---|---|---|
| 1 | **You'll see** + one real question with numbers | Not $a,b,c$: a real line from a tutorial. |
| 2 | **The move** | One line, with its equation centred. |
| 3 | **Why? box** (closed, optional) | Proofs, "where this comes from". |
| 4 | **Steps** | Numbered, bold first word, ≤ 5 steps, the same words everywhere (below). |
| 5 | **Cases** (level-3 headings) | Formula → **Short example** (one centred line) → **Full example** in a closed card. |
| 6 | **Traps** | 1–2 warning boxes. |
| 7 | **Practice** | Solutions open with **Type:** (which case), then that case's step words, every line of arithmetic. |

- Formula tables → a tiny **"spot it" table** (clue word → family, a few words per cell), then **one closed card per
  family**: title = name + formula; inside = clue, short example, mean and variance.
- Each equation on its own centred line. One step per line inside cards.
- Calculus/Test 1 reminders → closed cards right where they're used, not callouts in the middle.
- Remove the duplicated "in plain words" steps: keep a short top ("You'll see", "The kinds of Question N").
- Keep what you asked for this morning: few kinds per question, and Practice opens with "Question N is always one of
  these" (one line per case + its first move).

### Same words in all four notes (less to remember)
| Step word | Means | Used in |
|---|---|---|
| **Spot** | name the case or family from the clue | all |
| **Find $c$** | total = 1 (sum in Q1, area in Q2), solve | Q1, Q2 |
| **Accumulate** | the CDF: running total (Q1) = area so far (Q2) = $P(g(X)\le y)$ (Q4) | Q1, Q2, Q4 |
| **Differentiate** | the PDF = slope of the CDF | Q2, Q4 |
| **Rewrite** | turn the question into $F$'s: $P(X>a)=1-F(a)$, $P(a<X\le b)=F(b)-F(a)$ | Q1, Q2 |
| **Plug in** | put the numbers in | all |
| **Mean → Square → Subtract → Root** | $E[X]$, $E[X^2]$, Var, $\sigma$ | Q3 |

Q4's DAD is literally "range, **Accumulate**, **Differentiate**": the same two words you already used in Q2.

### Same letters in all four notes
$X$ = the random variable, $Y=g(X)$ = the new one · $p_X$ PMF, $f_X$ PDF, $F_X$ CDF · $c$ = the unknown constant ·
$p$ = success chance · $n$ = number of tries, $k$ = the value · $\lambda$ = rate per unit time (Poisson **and**
exponential) · $\mu$, $\sigma$ = mean and standard deviation (Gaussian **and** Q3).
One clash the lectures force on us: Uniform$(a,b)$ and $Y=aX+b$. Never in the same example.

---

## 4. Note by note

**Q1 · Discrete.** Top: you'll see / the 2 kinds.
- **Case 1: build the PMF** — Spot → List → Label → Add → Check (sum = 1). Full card: 3 coins; 2 chips (Practice 02 Q5).
- **Case 2: find $c$** — Find $c$ with the two series as cards. Full card: Tutorial 3 Q2.
- **Case 3: the CDF** — Accumulate (running total) / jumps back to the PMF / Rewrite table → cards. Full card: Practice 03 Q9.
- **Case 4: named family** — spot-it table + 6 family cards (Bernoulli, Binomial, Geometric, Neg. Binomial,
  Hypergeometric, Poisson). Steps: Spot → Write → Plug in (complement for "at least").
- **Case 5: two families in one question** — Inside $q$ → Outside Binomial/Geometric. Full card: Tutorial 3 Q6.
- Counting → 3 closed cards (Test 1). Practice: keep the 10, re-label the steps.

**Q2 · Continuous.** Top: probability = area; the 2 kinds.
- **Case 1: find $c$** (area = 1). Full card: Practice 02 Q1.
- **Case 2: PDF → CDF → probabilities** — Accumulate piece by piece, Differentiate back, Rewrite. Full card: triangle (Practice 02 Q2).
- **Case 3: uniform** · **Case 4: exponential** (tail, memoryless) · **Case 5: Gaussian** (standardise → $\Phi$; backwards).
  Each: formula → short example → full card (Tutorial 4 Q5, Q3, Q4).
- **Case 6: mixed** (jump + ramp). Full card: received signal level (Lec 10–11).
- Practice: keep the 10.

**Q3 · Mean and variance.**
- **Case 1: from a PMF** · **Case 2: from a PDF** · **Case 3: from a CDF** (jumps / slope / tail formula) ·
  **Case 4: named family** (cards) · **Case 5: only $E[X]$ and Var given** (the rules).
- Steps everywhere: Mean → Square → Subtract → Root. Chebyshev/Markov → optional box.
- Practice: keep the 10.

**Q4 · Functions of a RV.**
- **Step 0 everywhere: Spot the type of $Y$** (discrete / continuous / mixed), 4 one-line cards instead of the table.
- **Case 1: discrete $Y$** (add the probabilities on the same value).
- **Case 2: $g$ only goes up** — Range → Invert → Accumulate ($F_X(g^{-1}(y))$) → Differentiate. Cards: $X^3$ (Lec 14), $e^X$, $\ln X$.
- **Case 3: $g$ only goes down** — same, but $1-F_X(\dots)$. Card: $aX+b$ with $a<0$ (Lec 15), $1/X$ (Tutorial 6 Q1).
- **Case 4: $g$ turns around (DAD)** — Distribution → Accumulation → Differentiation, with the drag-$y$ graph. Cards: $X^2$, $|X|$, $\cos X$.
- **Case 5: $g$ goes flat (mixed $Y$)** — the jump. Card: $\max\{X,0\}$.
- Practice: keep the 10.

---

## 5. How I'll build and check it

- Edit `q1.py`…`q4.py` in place. Add the same `BOX` / `WHY` / `CARD` helpers to `lib226.py` that the 231 notes use.
- `verify()` (sympy) re-checks every number, as now. Publish each note → KaTeX/overflow check → screenshots I read myself.
- **Pilot: Q4 first** (the hardest), show you, then Q2 → Q3 → Q1 without stopping.
- The 500-block cap won't bite (each note is ~70 blocks).
