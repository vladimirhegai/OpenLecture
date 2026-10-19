# ELEC 271 notes

Nine course notes are stored in OpenLecture and exported to `notes/ELEC-271-01.md` through `09.md`.
Notes 01–03 are the main midterm sections: Binary Numbers, Introduction to Logic Circuits, and Implementation Technology (Week 5).
Notes 04–09 are explicitly marked Later. The live course map separates these two study sets.

The instructor announcement is indexed from `midterm_scope.md`: October 29 during class, 40 minutes, Weeks 1–5 only.
PS2 Q2 and Q6–Q8 are excluded from the midterm notes; Q1 and Q3–Q5 are covered.
The notes retain concise explanations, worked examples, figures, and hidden solutions in the ELEC 231 style.

The supplied lectures cover Sections 1–3. Later notes teach the methods requested in Problem Sets 3–7,
explicitly distinguishing that coverage from supplied lectures. Referenced textbook figures were reviewed visually.
The 2025 midterm is a practice source, not evidence of the 2026 exam scope.

From the repository root:

```powershell
.venv/Scripts/python.exe scripts/notes271/inspect_sources.py
.venv/Scripts/python.exe scripts/notes271/import_sources.py
.venv/Scripts/python.exe scripts/notes271/record_visual_reading.py
.venv/Scripts/python.exe scripts/notes271/import_midterm_scope.py
.venv/Scripts/python.exe scripts/notes271/build.py --publish
.venv/Scripts/python.exe scripts/notes271/course_index.py
.venv/Scripts/python.exe scripts/notes271/verify_midterm.py
node scripts/notes271/audit.cjs
```

`build.py` runs mathematical and state-transition checks, validates note schemas and figures, writes Markdown/JSON,
and revises the existing notes in place when publishing. `midterm.py` reorganizes the original verified content builders;
use `build.py` rather than publishing an individual `0N_*.py` builder. Sources/citations and document IDs are local to this workspace.
`out/duplicates.json` records the exact filenames and SHA-256 hashes of the three removed byte-identical aliases.
Distinct question sheets, solutions, and TA annotations were retained.

The app's reusable figure grammar is in `src/open_lecture/skills/digital-figures.md`.
No HDL simulation or synthesis was performed.
