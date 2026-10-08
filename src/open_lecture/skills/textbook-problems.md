# Textbook problems
Choose good practice problems from the course textbook and put them in notes without loading the whole book.

The textbook is indexed, not read: there is a chapter and section outline and a list of numbered end-of-chapter problems with their page numbers. Text extraction garbles symbols and loses every figure, so always look at the page image before using a problem.

## Finding problems

1. `textbook_outline` to see the chapters. Then `textbook_outline` with a `chapter` to see its sections and the page range of its "Problems" section.
2. `textbook_problems` with that `chapter`, optionally a `section` (problems are grouped like "Section 4.2–4.3", matching the chapter sections they practice) and a `query` (e.g. "supernode", "dependent source"). Each result has a number, page, short text preview, and a ready-made `citation`.
3. Shortlist problems that match the week's topics, use only material taught so far, and together cover every topic. Prefer a spread: one direct application, one with a twist (dependent source, special case), one multi-step problem.
4. Call `source_page` on the textbook for each shortlisted problem's page. Read the full statement and the figure (figures may sit on the previous or next page; check `page±1` if the figure is missing). Zoom into the figure with `region` (fractions of the page, e.g. `[0.5, 0, 1, 0.5]` for the top-right quarter) and `size` up to 2400 when labels are small.

## Writing a practice_problem block

Every practice problem comes from a source and cites it. Never invent an unsourced problem.

- `title`: where it is from plus a short name, e.g. `Textbook P4.12 · Mesh currents with a supernode`, `Tutorial 2 Q3 · Bridge circuit`, `Assessment AP 1.5 · Reference directions`.
- `origin`: `source`, and `citations`: the citation returned by `textbook_problems` for that problem, or the page of the course PDF it comes from.
- `difficulty`: `introductory`, `intermediate` or `advanced`.
- `prompt` (Markdown), separated by blank lines:
  1. The statement in one to three short sentences, with every value the problem needs.
  2. The circuit drawn with a ` ```schematic ` fence (see the `schematic` skill), with the figure's node labels, voltage polarities and current arrows. Check it with `schematic_check`. Never write the circuit out as an element list in prose.
  3. What to find, as a numbered list when there are several parts.
- `steps`: your full solution as 3–10 steps (`explanation` plus an optional displayed `latex` equation each), as in `weekly-notes`. Show the method choice, the equations, and the algebra. The textbook has no solutions, so work each one out yourself and verify resistive DC answers with `circuit_simulate`.
- `answer`: the final results with units, one per part, each starting with **(a)**, **(b)** … when there are parts.
- For a problem from a course PDF (tutorial, assessment problems), cite that source's page note, and follow its official solution if the PDF has one.
