# ELEC 231 week notes: style guide (read all of it before writing)

## Who reads this
A second-year ECE student, learning this material from scratch for the midterm (Fri 30 Oct, 2 h, covers Weeks 1–6).
In their own words: *"I want CLEAR explanations and not some cryptic stuff. I want a lot of examples and practice
problems. I do NOT want a bajillion topics and fractured information. Very organized, very easy to understand."*
They learn from examples and from seeing pictures. The previous notes they got (ELEC 221) felt **too terse and cryptic**:
shorthand, symbols that weren't explained, and skipped steps. Don't repeat that. The opposite failure, long textbook
paragraphs, is also bad. Aim for **a good TA explaining at a whiteboard**: plain words, every step shown and justified
in one sentence, nothing assumed.

## Hard rules
1. **At most 3 topics per week.** Each topic is one `D.H('Topic k: Name')` (level 1). **No level-2/3 sub-headings and no
   "Part A/B" splits.** Inside a topic the blocks simply run in the order below.
2. **Every symbol is explained at first use** in that week's note (e.g. "$\tau$ (tau) is the *time constant*: the time
   it takes to cover 63% of the change").
3. **Every worked-example step** = one full sentence saying *what we do and why*, plus the math. No step may jump over
   algebra a student could get stuck on (show the substitution, the integral, the constant).
4. **Every answer is verified with sympy** inside the build script (`check()` with asserts: substitute the solution
   back into the ODE, check the initial condition, check numbers). The build must fail if a check fails.
5. Use the course's notation: `j` for the imaginary unit ($j^2=-1$), $t$ for the independent variable, $y(t)$,
   Leibniz $\dfrac{dy}{dt}$, $M\,dt+N\,dy=0$ (exact equations use $t$ and $y$, as in the lecture).
6. Content follows the professor's lecture notes for that week (page images in the scratchpad `231/` folder, listed below)
   and the syllabus outcomes. Include the lecture's own examples as worked examples (re-explained clearly), with
   `cites=D.cite('W3', 2)`. The pre-tutorial problem appears as a Try it or Practice problem with `cites=D.cite('T3', 1)`
   and a full solution.
7. Problems copied from a source **must** cite it (that makes them `origin: source`). Original problems have no cites.
   Prompts must be **self-contained** (restate every value; draw any circuit with the schematic language).

## Order of blocks in every week
1. `D.CO('info', ...)`: **"Week N in one sentence"**, then a blank line and "**By the end you can:**" with 3–5 `-` bullets.
2. Optional `D.CO('tip', ...)`: "What you need from earlier weeks" (only if needed, e.g. W5 uses Euler's formula from W1).
3. For each topic (1–3 of them):
   - `D.H('Topic k: <plain name>')`
   - `D.P(...)`: **the big idea** in plain words, 2–5 sentences. Analogies and intuition welcome. Say *when* you use it.
   - `D.CO('tip', '**The method**\n\n1. ...\n2. ...')`: a numbered recipe (3–6 steps) the student can follow on the exam.
   - `D.EQ(...)`: the 1–3 key formulas (each explained in a sentence before or after).
   - 3–5 **worked examples** `D.EX(title, prompt, steps, answer, cites)`, easy → hard. The first one should be dead simple.
   - Charts: `D.CHART(...)` where a picture helps (e.g. a decaying exponential, a step response, the three damping cases).
     Put it right after the example it illustrates, with a caption saying what to notice.
   - `D.CO('warning', '**Common mistakes**\n\n- ...')`: 2–4 bullets, concrete ("forgetting the $+C$ before using
     $y(0)$", not "be careful").
   - 4–6 **Try its** `D.PR(title, prompt, steps, answer, diff)`, easy → hard, each with a complete step-by-step solution
     (same standard as the worked examples). `diff` is 'introductory' | 'intermediate' | 'advanced'.
4. `D.H('Mixed practice (exam style)')` + one `D.P` line ("Mixed topics, like the midterm. Try each one before opening
   the solution."), then 5–8 problems `D.PR(..., label=f'Practice {k}')` that mix the week's topics (and earlier weeks
   where natural), including at least one multi-part problem.
5. `D.H('Summary')`, then a `D.T(['Problem type', 'How to recognise it', 'What to do'], [...])` and, if useful,
   a second table of key formulas.

Size target: 40–60 blocks; at least 10 worked examples + 15 practice problems in total for the week.

## Text formatting
- Markdown in every text field; inline math `$...$`; display math in `EQ` or `S(..., latex)` fields **without** `$`.
- Use Python raw strings `r'...'` for anything with backslashes. **Never** write `\'` (the save() check rejects it).
  Inside raw strings write single backslashes: `r'\dfrac{dy}{dt}'`.
- Multi-line answers: separate parts with `\n` inside a normal string or use `(a) ... (b) ...` on one line.
- Prompt with parts: use a Markdown numbered list ("1. Find ...\n2. Sketch ...").
- Keep display equations short enough to fit a phone-width column; split long chains over several steps.
- Callout tones: only `info`, `warning`, `tip`.
- Circuits: fenced ```` ```schematic ```` blocks inside a prompt, or `D.SCH(source, caption)`. Language reference:
  `src/open_lecture/skills/schematic.md`. Example (from the course):
  ```
  V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
  S1 0,3 -> 3,3 "$t=0$" action=close
  R1 3,3 -> 6,3 "$10\,\Omega$"
  L1 6,3 -> 6,0 "$2\,\mathrm{H}$" i="$i$"
  wire 6,0 -> 0,0
  ground 0,0
  ```
  Validate drawings with `POST http://127.0.0.1:8000/api/v1/schematics/check` body `{"source": "..."}` (the build
  only saves JSON; a bad drawing is rejected when the note is published).

## Tone sample (worked-example step)
Good: `S("Divide both sides by $L=2$ so the $\\dfrac{di}{dt}$ term stands alone; this is the standard form "
"$\\dfrac{di}{dt}+a(t)\\,i=f(t)$ we need for the integrating factor.", r'\dfrac{di}{dt}+5i=50')`
Bad: `S("Standard form.", r'i\'+5i=50')`   (cryptic, skips the why)
Bad: three-sentence lectures about history or theory nobody asked for.

## Files and tools
- Builder library: `scripts/notes231/lib231.py` (read its docstring). Run scripts with
  `C:/Users/vladh/Downloads/OpenLecture-main/OpenLecture-main/.venv/Scripts/python.exe` (has sympy). Write the script as
  `scripts/notes231/build_w<N>.py`; running it writes `scripts/notes231/out/w<N>.json`. **Do not pass --publish.**
- Lecture page images (read them with the Read tool):
  `C:/Users/vladh/AppData/Local/Temp/claude/c--Users-vladh-Downloads-OpenLecture-main-OpenLecture-main/0c3e4ef4-2fb9-4def-8130-f2dbbc4b2e15/scratchpad/231/`
  `W1_p1..7.png, W2_p1..5, W3_p1..5, W4_p1..5` (lectures), `T1_p1..T4_p1` (pre-tutorials).
- Syllabus weekly outcomes: W1 modelling with ODEs, complex numbers (rectangular/polar/exponential forms);
  W2 classify ODEs, solutions and IVPs, special first-order ODEs; W3 separable and linear first-order ODEs,
  existence and uniqueness; W4 exact ODEs and integrating factors, (intro) homogeneous 2nd-order constant-coefficient
  ODEs; W5 homogeneous 2nd-order constant-coefficient ODEs, RLC circuit with constant impressed voltage, existence and
  uniqueness for linear 2nd-order ODEs.
- Textbook (Nilsson & Riedel, Electric Circuits) is indexed in this course: `D.tb('8.5')` gives the citation; problem
  list: `GET http://127.0.0.1:8000/api/v1/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/textbook/problems?chapter=8&limit=100`;
  page images: `GET .../sources/c00436ce-ecb3-4417-ad98-c305d442e7e2/pages/<pdfPage>?size=1600` (save the PNG to the
  scratchpad and Read it). The `page` field of a problem is the printed page; find the PDF page by trying nearby numbers.
