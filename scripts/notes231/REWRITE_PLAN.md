# ELEC 231 midterm note: rewrite plan

**Goal:** turn every method section into "here's how to do it": steps, cases, formulas, one example, a few practice
problems. Theory goes into closed "Why?" boxes you can skip. Nothing the midterm needs gets dropped. It just gets
moved into a step, a case or an example.

Midterm: **Fri Oct 30**. Order of work: **B (B5 first) → D → C → A → E (practice midterm)**.

---

## 1. One template for every method section

Every section (B1–B7, C1–C2, D1–D2) follows the same layout, top to bottom.

| # | Part | What it looks like | Rule |
|---|---|---|---|
| 1 | **Title + one sentence** | "Use this when the equation looks like `y'' + 3y' + 2y = 0`." | A real equation with numbers, not a, b, c. |
| 2 | **The move** | One line that turns the problem into something you can already do. | Equation block, then one plain line. |
| 3 | **Why? box (optional)** | Closed box titled `Why are we allowed to do this? (optional)` | Theory, proofs, "where the formula comes from". Not needed for marks. |
| 4 | **Steps** | Numbered list, bold first word: **Write**, **Solve**, **Pick**, **Plug in**… | ≤ 6 steps. These exact words are reused in every solution. |
| 5 | **Cases** (if any) | `Case 1: …` heading for each. Inside: how to spot it → formula → example. | Each case has its own full example, **with** `y(0)`, `y'(0)` (or whatever conditions the exam gives). |
| 6 | **Traps** | 1–2 red warning boxes max. | Only mistakes that cost marks. |
| 7 | **Practice** | 3–5 problems, easy → hard. Solutions closed. | Solution steps use the **same bold step words** as part 4. |

**What gets cut or moved:**
- "Calculus you need here" tables → removed. The one derivative you need goes right inside the step that uses it.
- "Bonus (skip-safe)" callouts → become the closed **Why?** boxes.
- Standard-form bullet lists (`a(t)` = …, `f(t)` = …) → one line under the equation, or into the example.
- Graphs → keep at most one per section, only if it shows the cases (e.g. the B5 slider). Placed after the cases.
- Long paragraphs → split into steps or deleted.
- **Give it space.** One idea per line. Every equation is its own centred display, never inline in a bullet
  ("$s=-1,-2$ → $y=\dots$" becomes a centred line). Each case: formula → **Short example** (one centred line) →
  **Full example** in a closed card (`CARD` in midlib: "Step k · **Word** …", math centred under each step, one
  equation per line).
- **Summary/shortcut tables** (one row per case or formula) → one closed card per row instead (`D.BOX`), titled with
  the row's formula, holding a short 3–4 line example with numbers and one "where it comes from" line. A bare table of
  formulas is too condensed.

**How solutions are written (sections and practice midterm):**
- First line: **Type:** what kind of problem, and the clue. ("Second order, plain numbers in front, right side 0 → B5.")
- Then the section's own steps, **same names, same order**. No new tricks that weren't taught in the section.
- Every bit of arithmetic shown: plugging in, solving the 2×2 for the constants, the derivative before plugging in `t=0`.
- Last line: the answer in a box.
- Every answer is checked with sympy in the module's `verify()` (already how the scripts work).

---

## 2. B5 written in the new shape (the pilot)

This is how B5 will read. Every other section copies this shape.

> ### B5 · Second order, numbers in front, right side 0
>
> **Use this when** the equation looks like
> $$y''+3y'+2y=0$$
> and you want $y(t)$.
>
> **The move:** turn the ODE into a quadratic. Swap $y''\to s^2$, $y'\to s$, $y\to 1$:
> $$y''+3y'+2y=0\quad\longrightarrow\quad s^2+3s+2=0$$
>
> ▸ *Why are we allowed to do this? (optional)* — closed box: guess $y=e^{st}$, every derivative pulls out an $s$,
> $e^{st}$ factors out and is never 0, so the bracket must be 0.
>
> **Steps**
> 1. **Write** the quadratic: $as^2+bs+c=0$.
> 2. **Solve** it: factor, or $s=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$.
> 3. **Pick** the case from what the roots look like (below).
> 4. **Plug in** the conditions $y(0)$, $y'(0)$ to find $A$ and $B$.
>
> **Case 1: two different real roots** ($b^2-4ac>0$)
> - Find $s_1$ and $s_2$.
> - $y=Ae^{s_1t}+Be^{s_2t}$
> - Example: $y''+3y'+2y=0$, $y(0)=1$, $y'(0)=0$. Roots $-1,-2$ → $y=Ae^{-t}+Be^{-2t}$ →
>   differentiate: $y'=-Ae^{-t}-2Be^{-2t}$ → at $t=0$: $A+B=1$, $-A-2B=0$ → $A=2$, $B=-1$.
>
> **Case 2: one repeated root** ($b^2-4ac=0$)
> - $s$ twice → $y=(A+Bt)e^{st}$ (the extra $t$ is the whole trick).
> - Example with $y(0)$, $y'(0)$, product rule shown.
>
> **Case 3: complex roots** ($b^2-4ac<0$)
> - Calm walkthrough: the number under the root is negative, e.g. $\sqrt{-16}=\sqrt{16}\cdot\sqrt{-1}=4j$.
>   So the roots come out as $s=\sigma\pm j\omega$: a **real part** $\sigma$ and a **$j$ part** $\omega$.
> - $y=e^{\sigma t}(A\cos\omega t+B\sin\omega t)$. Real part → in the exponential. $j$ part → inside cos and sin.
>   No $j$ in the final answer.
> - Example: $y''+2y'+5y=0$ → $s=-1\pm 2j$ → $\sigma=-1$, $\omega=2$ → full conditions worked.
> - Special case: no $y'$ term ($y''+9y=0$) → $\sigma=0$ → just $A\cos3t+B\sin3t$.
>
> ▸ *Why cos and sin? (optional)* — closed box: Euler's formula.
>
> **Trap:** use the conditions on $y$ **after** differentiating. Don't plug $t=0$ into the guess before taking $y'$.
>
> **Shortcut table** (small, after the cases): $y(0)$ and $y'(0)$ of each form, for checking.
>
> **Practice** (closed solutions, same step words): two real roots · repeated root · no damping · work backwards from the roots.

---

## 3. Section-by-section plan

### Topic B (most important)

**B0 · Which method?** Keep the "name it" questions, but cut the five method cards (they repeat B1–B7).
Replace with one **decision list**: 1st order → separable? → linear? → exact? → make exact. 2nd order → numbers in
front? right side 0? Each line: a one-line example + link. Keep the two "name it / check a solution" problems.

**B1 · Separable.** The move: get all $y$ on one side, all $t$ on the other.
Steps: **Separate** → **Integrate** both sides (+C on one side) → **Solve** for $y$ → **Plug in** the condition.
Traps: $\ln|y|$ then $e^{C}$ becomes a new constant; dividing by $h(y)$ can lose $y=0$. Practice: 4 (existing ones).

**B2 · Linear (integrating factor).** The move: $y'+a(t)y=f(t)$ → multiply by $\mu=e^{\int a\,dt}$ → the left side becomes $(\mu y)'$.
Steps: **Divide** so $y'$ stands alone → **Find μ** → **Multiply** → **Integrate** $\mu y=\int\mu f\,dt+C$ → **Divide** by μ → **Plug in**.
Why? box: why $(\mu y)'$ appears. Trap: forgetting to divide first, and $e^{\ln t}=t$. Practice: 4.

**B3 · Exact.** The move: find one function $U(t,y)$ with $U_t=M$, $U_y=N$. Answer is $U=C$.
Steps: **Write** $M$, $N$ → **Test** $M_y=N_t$ → **Integrate** $M$ in $t$ (+ $h(y)$) → **Match** $U_y=N$ to get $h$ → **Answer** $U=C$.
Trap: sign of $N$ when it starts as "$-(\dots)dy$". Practice: 3–4.

**B4 · Not exact → make it exact.** Cases:
- **Case 1:** $\frac{M_y-N_t}{N}$ has only $t$ → $\mu=e^{\int\dots dt}$.
- **Case 2:** $\frac{N_t-M_y}{M}$ has only $y$ → $\mu=e^{\int\dots dy}$.
Steps: **Test** (fails) → **Try case 1, then case 2** → **Multiply** by μ → **Re-test** → finish as **B3**. Each case: one example. Practice: 3.

**B5 · Characteristic equation.** As in section 2 above.

**B6 · Undetermined coefficients.** The move: $y=y_c+y_p$. $y_c$ = B5 with right side 0. $y_p$ = a guess that copies $f(t)$.
Steps: **Solve** $y_c$ (B5) → **Guess** $y_p$ from the table → **Plug in** and **Match** → **Add** $y=y_c+y_p$ → **Conditions** on the whole $y$.
Cases (one per kind of $f(t)$, each with a short example): constant · polynomial (all lower powers) · $e^{at}$ · $\sin/\cos$ (always both) · **guess already in $y_c$ → multiply by $t$**.
Full worked example: the tutorial problem $\ddot y+y=6\cos^2t$, $y(0)=0$, $y(\pi/2)=0$ (marked "know this cold").
Why? boxes: why $y_c+y_p$; why the ×t fix. Keep the resonance graph only if it fits. Practice: 4–5.

**B7 · Reduction of order.** The move: you're given one solution $y_1$. Guess $y=y_1v$; the plain $v$ terms always cancel, leaving a 1st-order equation.
Steps: **Check** $y_1$ → **Write** $y=y_1v$, $y'$, $y''$ (product rule shown inline) → **Plug in**, plain $v$ cancels → **Set** $z=v'$, solve (B1/B2) → **Integrate** $v=\int z$ → **Multiply** back by $y_1$.
Shortcut: $y_2=y_1\int\frac{e^{-\int p\,dt}}{y_1^2}dt$ as a "check your answer" box. Example: the lecture's $y''-ty'+y=0$, $y_1=t$ (keep the stepper). Practice: 3.

### Topic D (second most important): circuits

**D0 · The circuit recipe.** One 5-step recipe at the top, everything else hangs off it:
**Before** ($t<0$: C = gap, L = wire) → **Carry across** ($v_C$, $i_L$ don't jump) → **After** (write KVL/KCL) → **Solve** (D1 or D2) → **Check** $t\to\infty$.
The element table stays (it's the rules). The "why can't it jump" goes in a Why? box. The two sign/two-circuit warnings stay.

**D1 · One C or one L (first order).** The move: you don't need the ODE. Find 3 numbers and plug into
$x(t)=x_f+(x_0-x_f)e^{-t/\tau}$.
Steps: **x₀** (old circuit) → **x_f** (new circuit, long time) → **τ** ($R_{th}C$ or $L/R_{th}$, sources off) → **Plug in** → **Anything else** from $x(t)$.
Cases: natural response ($x_f=0$) · step response. Each with a circuit example. Why? box: where the formula comes from (it's B2).
Practice: keep the 6 circuit problems, rewrite solutions in the 5 step words.

**D2 · RLC (second order).** The move: it's **B5 with circuit names**. Same 3 cases.
Steps: **Initial values** $v(0)$, $v'(0)=i_C(0^+)/C$ → **Final value** $V_f$ → **α and ω₀** (series: $\alpha=\frac{R}{2L}$; parallel: $\alpha=\frac{1}{2RC}$; both $\omega_0=\frac1{\sqrt{LC}}$) → **Pick the case** → **Constants** from $v(0)$, $v'(0)$.
Cases: overdamped $\alpha>\omega_0$ (= B5 case 1) · critically damped $\alpha=\omega_0$ (= case 2) · underdamped $\alpha<\omega_0$ (= case 3, with $\omega_d$). Each with an example.
Practice: keep the 6 RLC problems, rewritten in the step words.

### Topic C (third): does exactly one solution exist?

**C1 · First order.** Steps: **Write** $F$ → **Differentiate** $F_y$ → **Find where it breaks** (÷0, ln of ≤0, √ of <0) → **Check the point**.
Answer wording to copy on the exam: "guaranteed" / "theorem says nothing". Full theorem statement → Why? box. Keep the √y graph in the box.

**C2 · Second-order linear.** Three cases = three kinds of question:
- **Case 1: what interval?** Divide by the $y''$ coefficient → trouble points → the piece containing $t_0$.
- **Case 2: both starting values 0, right side 0** → $y\equiv0$, no solving.
- **Case 3: do $y_1$, $y_2$ give the general solution?** Wronskian $W=y_1y_2'-y_1'y_2\neq0$.
Each with a one-line example. Theorem + why the Wronskian works → Why? boxes. Practice: keep the 6.

### Topic A: complex numbers (light touch)
Already mostly steps. Make each job (convert, multiply/divide, power, roots) a case with its formula + one example.
Move theory into a Why? box. Calculator steps for the Casio 991 kept.

### Topic E: practice midterm
Keep the ~10 multi-part problems. **Re-write every solution** so it:
- starts with **Type:** and names the section (B5 case 3, D1, …),
- uses that section's step words in order, no shortcuts we didn't teach,
- shows every line of arithmetic, including finding constants,
- ends with the answer box + a `Review:` link to the section.
Open with a short "the midterm is always one of these" checklist (one line per question kind + the move).

---

## 4. How I'll build and check it

- Edit the `mid_*.py` modules in place (same build system). Add a small `D.WHY(title, text)` helper that makes a
  closed box (the existing collapsible `solution` block).
- Each section: `verify()` passes (sympy checks every answer) → `python build_midterm.py --preview b5` →
  `mathcheck.cjs` (no broken math, nothing overflowing) → `chunkshot.cjs` screenshots, read by me, solutions open.
- **B5 first**, then I show you the screenshot before doing the rest the same way (one quick check that the shape is what you want).
- Then publish the full note once, re-run the math check on the whole thing.
- Update `MIDTERM_STYLE.md` to this template so later edits keep the shape.
