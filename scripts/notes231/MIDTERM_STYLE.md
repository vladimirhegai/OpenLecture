# ELEC 231 midterm note: layout and rules

One note, "ELEC 231 Midterm: Weeks 1–6 by Problem Type", built by `build_midterm.py` from section modules
`mid_<part>.py` (each has `build(D)` and `verify()`). Parts, in order: head, a, b0–b7, c, d0–d2, e.
Topic E (`mid_e.py`) is the exception to the subtopic layout: a short mixed practice midterm (~10 multi-part problems,
titles `E<n> · W<k> · …`), copied from or modelled on lecture/tutorial examples, each answer ending in a `Review:` link.
Keep it short; the user asked not to be overwhelmed.
Reference sections: `mid_b1.py` and `mid_b2.py`. Copy their shape.

## Who it is for
A student who finds ELEC 231 their hardest course, preparing to **solve midterm problems** (Fri Oct 30, 2 h, 30 marks).
Scope (announced): up to and including the Mon Oct 26 lecture (comments on undetermined coefficients = N6) and the
Oct 26/28 tutorials (Pre-tutorial 5 = T6, the $y''+y=6\cos^2t$ problem). **No Laplace transforms.** They learn visually and from examples. Teach what is needed to solve problems, not theory for its own sake.

## Structure
- Topic = a job: A complex numbers · B find the general solution · C does exactly one solution exist · D circuits.
- Subtopic = a method or a circumstance (`D.H('B2 · …', level=2)`). The heading starts with its code (`B2 · `,
  `Topic C: `). In-note links use that code: `link('B2', 'b2')` → `[B2](#b2)`, `link('Topic C', 'topic-c')`.
- Read linearly, a section only needs earlier sections. When it uses another section, link to it.
- Directly under every topic/subtopic heading: `TAGS(D, (week, topic), ...)`, chips linking to the week notes.

## Inside a subtopic, in this order
1. **Why / when** (1–2 short sentences, bold lead). Example: "**What if you can't separate the variables?** …"
2. **Standard form** as an equation block, then a bullet per part: `$a(t)$ = the coefficient of $y$: …`.
3. **Mini examples** of reading the form (a short bullet list, not a worked example block).
4. **The method**: the formula(s) as equation blocks, then numbered steps (`D.L([...], ordered=True)`, bold lead
   word per step). A `D.STEPS` stepper when watching the equation change helps.
5. **Calculus you need here**: a small table, only the rules this subtopic uses.
6. Callouts, at most a few: `warning` = a trap that costs marks; `tip` = a shortcut; `info` titled
   `**Bonus (skip-safe): why …**` = understanding the student may skip without losing marks.
7. Graphs (`D.GRAPH`) wherever moving something shows the idea (sliders, draggable points).
8. **Worked example**: only when the method has a step the problems don't make obvious. Prefer the lecture's own example.
9. **Problems**, easy → hard, with `P(D, title, prompt, steps, answer, diff, cites)` (numbered through the note).

## Problems
- Title starts with the week tag, then a few words, then the source: `'W3 · Separate and use a starting value · Pre-tutorial 3(a)'`.
  Several weeks: `'W1 + W5 · …'`.
- Source priority: lecture examples and exercises > pre-tutorials (the assignments) and tutorials > Nilsson textbook
  (`D.tb('8.53')`) > your own (only to fill a gap; no source tag). Cite with `cites=D.cite('W3', 4)`, `D.cite('T3', 1)`,
  `D.cite('T6', 1)`, `D.cite('W6', 3)`, `D.tb('7.1')`.
- Difficulty: introductory → intermediate → advanced, in that order within the subtopic.
- Every solution has the same shape: first step `**Type:** …` (what kind, and the clue), then the method's steps with their
  bold lead words (`**Separate:**`, `**Integrate:**`, …), then `**Condition:** …`. Answer box: the final result plus one
  short remark if useful.
- Steps: one short sentence + the math. Never empty explanations (the server rejects them).
- Every answer verified in `verify()` with sympy (`first`, `implicit`, `second`, `zero` from midlib).

## Writing and formatting
- **Voice and explanations: follow `.claude/skills/student-explanations/SKILL.md`** (plain TA speech, never textbook;
  every rule gets what → example → why; one-liner vs short vs full examples).
- Comparing methods (like Topic B's Step 2): a short routing table, then one card per method below it
  (bold lead → form as `D.EQ` → `**Example:**` / `**Method:**` / `**Why…?**` bullets). Table cells hold a few words only.
- One idea per line. Paragraphs ≤ 2 short sentences. Several items → bullets. No walls of text.
- Bold sparingly: the term being defined, the lead word of a step.
- Notation: `j` for √−1, `t` independent, `y(t)`, primes in text as `y\prime` (finish() converts them).
- Raw strings for LaTeX; write files with the Write/Edit tools, never a shell heredoc.
- Display equations must fit ~560 px. **Don't use `\qquad` in a long display**: the library splits such displays into
  stacked lines. Split into two `D.EQ` blocks with a short line between instead.
- Circuits: plain schematics, **no height views** (`#@` lines) and no `#~` flow. Validate with the server
  (`finish()` does it). Two switches with the same `"$t=0$"` label draw a two-position switch.

## Checking
- `python build_midterm.py --preview b3 b4` publishes only those parts to a preview note (own ids file, safe in parallel).
- `node toolshots.cjs <docId> <dir>` (tool errors, overflow); `node ../height_notes/pageshot.cjs <docId> <dir>` with
  `COURSE=206af2a6-c1f1-4700-ac44-5eba708c676b`, then look at the screenshots (open solutions too).
- The full note is >60k px tall and pageshot's single image stops at ~30k. Use
  `node chunkshot.cjs <repoRoot> <docId> <dir>` (one PNG per screen) and `node mathcheck.cjs <repoRoot> <docId>`
  (KaTeX errors, overflowing displays/tables, stray `$`, with all solutions open).
- Delete a preview note when done: `POST /api/v1/courses/<course>/documents/<id>/delete` with body
  `{"expected_revision": <current revision>}` (there is no HTTP DELETE route).
