# ELEC 221 Midterm Questions (doc 4463001f-6e90-4e75-9c5e-d1e0ef74faa5)

A practice midterm paper: one module per question, in exam order (`MODULES` in `build_midterm.py`).
`--publish` replaces the course document. Questions keep their exam number even while others are missing or failing.
Check the result with `node ../practice221/stepshots.cjs <docId> <outDir> [--dark] [--only=<title text>]`.

## Module interface

Same as `scripts/practice221/README.md` (PROMPT, GIVEN, STEPS, `checks(check)`, solving conventions and style),
minus `SECTION`, plus:

```python
TOPIC = 'Δ–Y'                                   # shown in italics above the question, with "inspired by SOURCE"
MARKS = 10                                      # the paper totals 120
SOURCE = 'Textbook P3.58 and Assessment Problem 3.7'   # what the question is modelled on (not a copy)
FORMULAS = ['delta_wye']                        # optional: parts of the exam's formula sheet to show under the question
```

`FORMULA_SHEET` in the builder holds the exam's formula sheet ('delta_wye', 'max_power'), redrawn in its own names.
Questions that use it solve in those names ($R_a, R_b, R_c$ for the Δ, $R_1, R_2, R_3$ for the Y, $(p_L)_{max}$),
so practising with the sheet feels like the exam.

Template: `q01_delta_wye.py`. Prompts read like the Fall 2025 paper: lettered parts **(a)**, **(b)**, …, and
"write (but do not solve)" parts where the method itself is being tested.
