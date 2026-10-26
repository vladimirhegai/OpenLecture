# ELEC 231 week notes: style guide v2 (read all of it before writing)

## Who reads this, and what they said
A second-year ECE student learning this from zero for the midterm (Fri 30 Oct, 2 h, Weeks 1–6). They learn from **clear
explanations and examples**, visually. Their feedback on v1 of these notes (2026-10-17):

- "I do not like a lot of yap." "Too much words and text. Not organized." "Each week is way too long."
- "I don't like 'Week 1 in 1 sentence'. Same for 'why complex numbers'. Useless info."
- "Short, concise bullet points, ONLY when necessary, don't overuse."
- "Examples: don't repeat the same example. Each should be a completely new thing."
- "We are LEARNING, not practicing. Problems should be purely new things, and fewer of them."
- "Remove the summary. I'll make my own so I remember what I learned."

So the note teaches each idea once, clearly, then shows it working on a few **different** examples. That's all.

## Hard rules
1. **No intro or outro furniture.** No "Week N in one sentence", no "By the end you can", no "Why X matters", no
   "What you need from earlier weeks", no summary, no cheat sheet, no "Mixed practice" section, no "Common mistakes"
   callout (fold a real trap into the example where it bites, in one sentence).
2. **1–3 topics per week**, each `D.H('Topic k: Name')`. No sub-headings, no "Part A/B".
3. **Inside a topic:** the idea → the formula(s) → examples → 1–2 Try its. Explanations are short: 1–4 plain sentences,
   or a compact table, or bullets (see "Layout" below). Every symbol is named at first use (in a
   few words). Nothing the reader didn't ask for: no history, no "this will be useful later".
4. **Examples are all different.** Each example teaches something the earlier ones didn't (a new case, a new trap, a
   new kind of question). Never two examples of the same move with different numbers. 2–4 examples per topic.
5. **Try its are new things too**, not drills of the examples: a twist, a reverse question, a case the examples didn't
   show. 1–2 per topic, full hidden solution. About 4–6 in the whole week.
6. **Use the interactive tools** (grammar: `src/open_lecture/skills/math-tools.md`):
   - `D.STEPS(title, [(latex, note), ...])`: an equation stepper. Use it for the main **derivation** of each topic and
     for the algebra of examples where watching the equation transform is the point (separating, integrating,
     solving for a constant). Each note is one short sentence; mark what changed with `\hl{...}`.
     Inside an example or Try it, put a stepper in the steps instead: one step `S('', '')` is not allowed, so use
     `S(steps_fence(title, [...]))` (import `steps_fence` from lib231) as a step's explanation.
   - `D.GRAPH(src)`: 2-D plots with sliders/draggable points: solution families, slope fields with a draggable initial
     point, how a parameter changes a curve, the complex plane. `D.GRAPH3D(src)` for surfaces.
   - One tool per idea where it truly helps (2–4 per week). A tool replaces text, it doesn't add to it.
7. **Every answer verified with sympy** in the build script (asserts; the build fails on a wrong answer).
8. Notation: `j` ($j^2=-1$), $t$ independent, $y(t)$, $\dfrac{dy}{dt}$, $M\,dt+N\,dy=0$ for exact equations.
9. Content = the professor's lecture for that week + the pre-tutorial (page images below). Include the lecture's own
   examples (cite them `cites=D.cite('W3', 2)`), the pre-tutorial as an example or Try it (`cites=D.cite('T3', 1)`).
   Keep everything the lecture teaches; cut everything it doesn't.
10. The reader forgot calculus. When a step uses a derivative/integral rule, name it in the note in a few words
    ("$\int \frac{1}{y}dy=\ln|y|$"). Don't lecture on calculus.

## Size
About **1/3 of the v1 note**: roughly 20–35 blocks and 1,500–2,500 words for the week. If a block doesn't teach,
delete it.

## Layout: one idea per line (MOST IMPORTANT)
Second feedback, same day, on v2 Week 1's opening paragraph: *"what is this note structure, it's all in a jumbled
paragraph and it's confusing. Have you EVER heard of new lines? Or bullet points? The content ain't bad but I can
barely read it."* "Bullets only when necessary" never means dense paragraphs. **2+ parallel items is when it's necessary.**

- **No paragraph longer than 2 short sentences.** One idea per paragraph; separate with a blank line (`"\n\n"`).
- **Several terms defined → a bullet list**, one term per bullet: `- $c=|z|$: the **magnitude** (length of the arrow)`.
- **Cases / situations / a sequence** (before/at/after, case 1/2/3, what changes) → bullets with a bold lead:
  `- **At $t=0$:** the switch opens…`.
- A short lead-in line ("You can describe that point two ways."), then the list.
- In a `D.P`, list items are joined with `"\n"`, separate paragraphs with `"\n\n"`.
- Reference layout: the Topic 1 opening of `build_w1v2.py` (bold label line, then its bullets).

## Writing
- Voice and explanations: follow `.claude/skills/student-explanations/SKILL.md` (plain speech, what → example → why).
- Worked-example steps: one short sentence (what and why) + the math. Skip nothing a student could get stuck on, but
  don't narrate the obvious.
  Good: `S('Divide by $L$ so $\\dfrac{di}{dt}$ stands alone.', r'\dfrac{di}{dt}+5i=50')`
  Bad: `S('Standard form.', ...)` (cryptic) and three sentences of theory (yap).
- Bold sparingly: the one term being defined.
- Markdown in text fields; inline `$...$`; display math in `EQ` / `S(..., latex)` without `$`.
- Python raw strings for LaTeX. Write files with the Write tool, never through a shell heredoc (it eats `\\`).
- Display equations must fit a ~560 px column; split instead of cramming.
- Callouts only when they earn it (a key rule box, at most one per topic): tones `info` | `tip` | `warning`.
- Circuits: `D.SCH(source, caption)` (schematic language: `src/open_lecture/skills/schematic.md`). Validate with
  `POST http://127.0.0.1:8000/api/v1/schematics/check`.

## Files and tools
- Builder: `scripts/notes231/lib231.py`. Python: `C:/Users/vladh/Downloads/OpenLecture-main/OpenLecture-main/.venv/Scripts/python.exe`
  (has sympy). Week builder: `scripts/notes231/build_w<N>v2.py` → writes `out/w<N>.json`. Publish with `--publish`
  (replaces the live note in place).
- Check rendering: `node scripts/notes231/toolshots.cjs <docId> <outDir>` (screenshots every tool card, reports tool and
  KaTeX errors and overflowing equations); `node scripts/height_notes/pageshot.cjs <docId> <outDir>` with
  `COURSE=206af2a6-c1f1-4700-ac44-5eba708c676b` for the whole page. Look at the screenshots.
- Lecture page images: `C:/Users/vladh/AppData/Local/Temp/claude/c--Users-vladh-Downloads-OpenLecture-main-OpenLecture-main/56f77eee-3680-42b7-b015-debdf9f1ec5a/scratchpad/231/`
  `W1_p1..7`, `W2_p1..5`, `W3_p1..5`, `W4_p1..5`, `T1_p1..T4_p1`. (No Week 5 lecture: Week 5 follows the syllabus and
  Nilsson & Riedel Ch. 8.)
- The v1 builders (`build_w<N>.py`) and their output (`out/v1_backup/w<N>.json`) hold verified content and citations:
  reuse their facts, cut their words.
- Textbook (Nilsson & Riedel) is indexed: `D.tb('8.5')`; problems: `GET http://127.0.0.1:8000/api/v1/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/textbook/problems?chapter=8&limit=100`.
