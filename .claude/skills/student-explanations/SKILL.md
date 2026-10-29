---
name: student-explanations
description: How to write explanations in study notes so a struggling student understands them on the first read — plain talk, organised layout, examples that show the why, short vs long examples, logical flow. Use whenever writing or rewriting any study-note text (ELEC 221/226/231/271 notes, midterm notes, problem solutions, callouts, table cells).
---

# Writing explanations students actually understand

The reader is a student who finds this course hard, studying for an exam. They learn from **examples and pictures**,
not definitions. If they have to read a sentence twice, the sentence failed.

## 1. Talk like a TA at a whiteboard, not a textbook

Write what you would *say* out loud to a classmate. Short words, active voice, "you" and "we".

| Bad (textbook) | Good (TA) |
|---|---|
| Autonomous equations admit separation owing to the absence of explicit independent-variable dependence. | An autonomous equation has no $t$ in it. For example, $y'=3y$. Since the right side only depends on $y$, you can separate the variables and integrate. |
| The integrating factor renders the left-hand side an exact derivative. | Multiplying by $\mu$ turns the left side into one derivative, $(\mu y)'$. Now you can just integrate both sides. |
| A solution is valid provided the identity holds for all $t$ in the interval. | Plug $y$ into the equation. If both sides match for every $t$, it's a solution. |

Banned words and patterns (rewrite the sentence): *admit, owing to, thereby, hence, whereby, renders, yields
(say "gives"), provided that, it follows that, explicit dependence, one obtains, the aforementioned, in general
form, is said to be, respectively, note that, it is evident, clearly, trivially, simply*.

Other rules:
- **Name things, then use them.** Don't say "the independent variable", say $t$. Don't say "the forcing function", say "the right side, $g(t)$" (you may add "(called the forcing)" once).
- **One idea per line.** At most 2 short sentences per paragraph.
- **No undefined jargon.** If a word is new, define it in the same line, with an example.
- **Don't stack conditions in one sentence.** "If it is also homogeneous or autonomous (both constants), it separates too" → split into bullets, one case each, each with its example.

## 2. Organise it so the eye can find things

Pick the shape that matches the content:
- **A formula or a form** to remember → its own equation block, never buried mid-sentence.
- **Parts of a formula** → bullets, one part each: "$a(t)$ = what multiplies $y$".
- **Steps** → a numbered list with a bold lead word (**Separate:**, **Integrate:**).
- **Cases** ("if X do A, if Y do B") → bold-lead bullets or a small table, one case per row.
- **Comparison of several methods** → a table to *route*, then a short card per item to *explain*. A table cell is
  for a few words, not an explanation. If a cell needs a sentence, the explanation belongs below the table.

Bold only the term being defined or the lead word of a step. Never bold half a sentence.

**Figures need a question first.** Put the line that says what the figure is for ("**PS1 Q3:** what does this
circuit compute?") *before* the figure, and the explanation right after it. A figure with no prompt, or one placed
under an unrelated example, reads as random. Never let a figure's title or caption give away a try-it answer.

## 3. Always: what → example → why

Every rule or method gets, in this order:
1. **What it looks like** (the form, as an equation block).
2. **A real example** of that form, with numbers.
3. **Why** the method fits (one plain sentence connecting the look to the move).

> **Separable:** the right side is a $t$-part times a $y$-part.
> $$\frac{dy}{dt}=t^2\,y$$
> Why it works: you can put every $y$ on one side and every $t$ on the other, $\frac{dy}{y}=t^2\,dt$, then integrate each side.

Never write only the rule. Never write only the example. The "why" is one sentence, not a proof; a proof goes in a
skip-safe Bonus box.

## 4. Short examples vs long examples

Not everything deserves a full worked example. Choose the size by what the reader needs:

| Size | When | Shape |
|---|---|---|
| **One-liner** | showing what a definition looks like, or reading a form | `$y'=3y$ → autonomous (no $t$).` |
| **Short (2–4 lines)** | showing a method's key move, inside a routing guide or callout | the equation, the one move, the result |
| **Full worked example** | a method with a step that isn't obvious, or a classic exam pattern | Type → steps with bold leads → answer |

Most examples in a routing/overview section are one-liners or short. Save full worked examples for the method's own
section. A study note is still a study note: if a section scrolls on for pages, cut the weakest example.

## 5. Flow: each line leads to the next

- Start from a **question the student would ask** ("What if you can't separate the variables?"), then answer it.
- Order: simplest case first, then what breaks it, then the fix. Each new method answers "what if the last one fails?"
- Never use something before it's introduced. If you must, link to where it's explained.
- Transitions are short and plain: "So…", "But…", "That's where … comes in."
- End a section when the job is done: no summary paragraph, no "in conclusion".

## 6. Self-check before you hand it over

Read every paragraph and ask:
- Would a tired student get this on the **first** read? If not, split it or add an example.
- Is there a sentence that sounds like a textbook or a lawyer? Rewrite it as speech.
- Does every rule have an example right next to it?
- Is every example the right size (one-liner / short / full)?
- Is any table cell carrying a full sentence of explanation? Move it below.
- Is every claim **true**? Check edge cases (e.g. "linear + constant coefficients separates" is false for $y'+2y=t$).
