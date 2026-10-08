# Weekly notes
Write one complete, consistently structured study note per course week, built for learning: explanation first, then worked examples, then practice.

## Before writing

1. `course_study_guidance` for the course's learning outcomes, packs and preferences.
2. `document_find` with `academic_week` to see whether this week already has notes. If the task says to regenerate, `document_delete` the old note first. Otherwise update the existing note instead of creating a duplicate.
3. `source_list`, then read every source for this week with `source_notes`. These are the AI page notes of the lecture, tutorial and problem PDFs. They are a fast summary, not ground truth: look at the PDF yourself whenever it matters.
   - `source_thumbnails` shows up to 12 pages at once; use it to skim a lecture and spot the pages with circuits, worked examples and handwriting.
   - `source_page` shows one page. Pass `region` = [left, top, right, bottom] (fractions of the page) with a larger `size` to zoom into a circuit, a crowded equation or handwriting.
   - Always look at the original page of every circuit you draw and every example you reuse, so values, polarities and arrow directions match the figure exactly.
4. Find practice problems as described in the `textbook-problems` skill, plus any assessment or tutorial problems among the week's sources.
5. Verify every numeric answer you write: re-derive it, and for resistive DC circuits check it with `circuit_validate` and `circuit_simulate`. Use `math_evaluate` for algebra and calculus.
   - Preserve all given initial conditions. Zero capacitor current does not imply zero capacitor voltage; zero inductor voltage does not imply zero inductor current.
   - A transcription is not proof of correctness. Check units and source polarities against the original image. If a source omits units or contains an apparent error, distinguish the literal source result from the physically consistent result and state any assumption explicitly.
   - State which element and reference direction every current belongs to. For switched circuits, check initial/final values and substitute the response into the circuit's differential equation.
6. Draw every circuit you use in the `schematic` language and check each drawing with `schematic_check`.

## Document

`document_create` with:
- `title`: `Week N: <short theme>`, e.g. `Week 3: Node-Voltage and Mesh-Current Methods`
- `document_type`: `study_notes`, `academic_week`: N, `topic_keys`: the course topic keys this week covers
- `actor`: `agent`, and an `idempotency_key` of `week-N-notes`

## Headings

Heading levels carry the structure, and each level has its own color in the app, so use them consistently:
- **Level 1**: the top-level sections of the note: `Overview`, `Topic 1: <name>`, `Topic 2: <name>`, …, `Practice problems`, `Summary`.
- **Level 2**: sub-topics inside a topic section, e.g. `Series resistors`, `Parallel resistors`, and `Formula sheet` under Summary.
- **Level 3**: rarely, for a further split inside a long sub-topic.

Never skip a level, and do not put examples or problems under their own headings: those blocks carry their own titles.

## Block structure (same order every week)

1. **Overview** (level 1): a `callout` (tone `info`) with two or three sentences on what this week is about and how it builds on earlier weeks, then a `list` of this week's learning outcomes from the syllabus.
2. **One `Topic k: …` section per topic** (level 1), in lecture order, containing as needed:
   - `paragraph`: intuition first (what problem this solves, when to use it), then the precise idea. Keep paragraphs short: 2–4 sentences.
   - Definitions as a `table` (Term | Meaning) or `list`.
   - Key results as `equation` blocks, each followed by a short `paragraph` that says what every symbol means and when the result applies.
   - A `derivation` block wherever the lecture derives a result, with one explanation per step.
   - A `schematic` block for a circuit that illustrates the idea (e.g. a divider, a supernode).
   - At least one `worked_example` (format below). Prefer the lecture's own examples.
   - `callout` tone `warning` for common mistakes (sign conventions, reference directions, units, special cases).
   - `callout` tone `tip` for a method choice rule or exam shortcut, when there is one.
3. **Practice problems** (level 1): one short `paragraph` on how to use them, then 5–8 `practice_problem` blocks that together cover every topic of the week, ordered from introductory to advanced. Include at least 3 textbook problems and, when the week has them, tutorial or assessment problems. Rules are in `textbook-problems`.
4. **Summary** (level 1): a `list` of 5–8 key takeaways, then a level 2 `Formula sheet` heading and a `table` with the columns Result | Formula | Use when.

## Worked examples and problems

Both use a statement, numbered solution steps and a final answer, so they always read the same way:

```json
{"type": "worked_example",
 "title": "Power in a source and two resistors",
 "prompt": "The circuit below is from Lecture 2.\n\n```schematic\n...\n```\n\nFind:\n\n1. the current $i_a$;\n2. the power absorbed by the source.",
 "steps": [
   {"explanation": "Apply KVL clockwise around the loop, writing each resistor drop with Ohm's law.",
    "latex": "-50 + 5i_a + 20i_a = 0"},
   {"explanation": "Solve for the current.", "latex": "i_a = \\frac{50}{25} = 2\\,\\mathrm{A}"}
 ],
 "answer": "$i_a = 2\\,\\mathrm{A}$; the source absorbs $p = -100\\,\\mathrm{W}$ (it delivers 100 W).",
 "citations": [<the page the example comes from>]}
```

- `prompt` (Markdown) contains, in this order, each part separated by a blank line: one or two sentences of setup; the circuit as a ` ```schematic ` fence; the given values as a short list if there are more than three; and what to find, as a numbered list when there are several parts. Never describe a circuit as a sentence-long element list: draw it.
- `steps`: 3–8 steps. Each `explanation` is one or two plain sentences saying what is done and why. `latex` holds that step's equation, displayed on its own line. Use `\begin{aligned}...\end{aligned}` for two or three related lines, and leave `latex` empty for a reasoning-only step.
- `answer`: the final results with units, one per part. For several parts, start each with **(a)**, **(b)**, ….
- `practice_problem` blocks add `title` (e.g. `Textbook P1.16 · Battery energy`), `difficulty` and `origin` (see `textbook-problems`). Their steps stay hidden until the student opens the solution.

## Citations

Cite sparingly. Readers see one source line per section, not a source on every block.
- Each `Topic k` level 1 heading cites the lecture pages the section is built on: 1–4 citations from `source_notes` (`source_id`, `version`, `chunk_id`).
- Every `worked_example` taken from a source cites that page.
- **Every `practice_problem` cites the page it comes from.** There are no unsourced problems: only use problems that exist in the textbook, a tutorial, an assessment or a lecture.
- Do not cite paragraphs, equations, lists, tables or callouts.
- Never cite a page that does not support the block.

## Writing rules

- Write in plain, direct language for a second-year engineering student. Define every symbol on first use.
- All math in LaTeX: `$...$` inline in text, `equation` blocks for displayed results.
- Use readable stacked fractions for mathematical ratios in inline math: `$\dfrac{di}{dt}$`, `$\dfrac{v}{R}$`, `$\dfrac{V_{Th}}{R_{Th}}$`. Use `\frac` for fractions inside exponents so those remain compact. Keep unit ratios compact with a slash, e.g. `$\mathrm{V}=\mathrm{J/C}$` and `$\mathrm{W}=\mathrm{J/s}$`. Preserve a slash when it is part of a name or a literal source quotation rather than a mathematical ratio.
- Explanations beyond the sources are welcome, but never invent course facts (deadlines, what the instructor said, data).
- Aim for about 40–80 blocks. Depth over breadth: every topic must be understandable from the note alone.
- Finish by replying with the document title and a one-line summary of what it covers.
