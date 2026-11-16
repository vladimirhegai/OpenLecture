# ELEC 221 Midterm 2 notes (Ch 6, 7, 8)

Three Open Lecture notes in the ELEC 221 course, one per chapter, written 2026-11-13 for Midterm 2 (Nov 20). No phasors (Ch 9) yet.

Scope (prof's announcement, 2026-11-13): textbook 6.1-6.3, 7.1-7.5, 8.1-8.3 = parallel RLC only (series RLC removed
2026-11-14). Formula sheet: posted on OnQ "early next week" (add it under the practice questions once we have it).

| Note | Builder | Doc id file | Covers |
|---|---|---|---|
| Midterm 2 · 1. Inductors and Capacitors | `ch6.py` | `out/doc_ch6.txt` | v-i, power/energy/max energy, DC rules, series/parallel with starting values, trapped energy |
| Midterm 2 · 2. RL and RC Circuits | `ch7.py` | `out/doc_ch7.txt` | start value, tau, natural response + energy %, step response (six steps), Thevenin/dependent sources, sequential switching |
| Midterm 2 · 3. Parallel RLC Circuits | `ch8.py` | `out/doc_ch8.txt` | which damping, parallel natural, parallel step |
| Midterm 2 Practice Questions | `practice.py` | `out/doc_practice.txt` | 12 questions, 4 per note (Q1-4 / 5-8 / 9-12), each answer ends with "Review: note X, section" |

Each topic note: what it is -> formula -> worked example -> Try it; ends with a "Formula summary" section.

Style: gradual Parts (memory `notes-gradual-parts`): plain-words intro → overview table → Parts → each topic is
question → rule (display equation) → short example → one "why" line → Try it; ~4 practice questions at the end.
★ = lecture (Eren W7–W9, Bakhshai W7), tutorial (Tutorial 6, Week 8 Tutorial) or Assessment Problem.
Step words: Ch 7 **Before, Jump, After, τ, Plug in, Other**; Ch 8 **Shape, Start, Constants, Plug in**.

`lib221.py` = the lib226 helpers plus `sch()` (schematic fence, parsed with `open_lecture.schematic.topology` at save
time) and `near()` (every number in a builder is computed and asserted). `ch8.py` also checks each response against
its ODE (`ode_ok`). Citations: `out/citations.json` (page → chunk) for the week 6–9 sources.

```powershell
cd scripts/notes221
../../.venv/Scripts/python.exe -W error::SyntaxWarning ch7.py --publish   # checks + build + replace the note
node shots.cjs (Get-Content out/doc_ch7.txt) out/shots_ch7                # KaTeX/overflow/tool errors + slices
```

Source notes: the Ch 7/8 Assessment Problem sheets are solutions only (another edition's numbering). Problems whose
circuit can't be rebuilt from the sheet (AP 7.1, 7.2, 7.4, 7.7) are left out; AP 8.7–8.9 are stated with their given
final values. The AP 8.3(c) line on the sheet has both signs flipped (gives i_L(0) = −8 mA); the note says so.
Write builders with the Write/Edit tools: the Bash tool collapses `\\`.
