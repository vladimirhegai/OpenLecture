# ELEC 226 Test 2 notes

Four Open Lecture notes, one per question of In-Class Test 2 (Fri Oct 30 2026, 40 min, closed book, no formula sheet, Lectures 7–15):

| Note | Builder | Covers |
|---|---|---|
| Test 2 - Question 1 | `q1.py` | random experiments, sample spaces, discrete RVs, PMFs, CDFs (L7–9) |
| Test 2 - Question 2 | `q2.py` | continuous RVs, PDFs, probability calculations (L9–11) |
| Test 2 - Question 3 | `q3.py` | expected value, variance, their properties (L11–13) |
| Test 2 - Question 4 | `q4.py` | functions of continuous RVs and their distributions (L12–15) |

Each note (rewritten 2026-10-29, see `REWRITE_PLAN.md`): "Question N in plain words" (you'll see → the move → which-case
table), then one level-1 heading per **Case**: you'll see → the move (centred formula) → numbered steps → **Short example**
(one centred line) → **Full example** in a closed card (`D.CARD`) → shortcut/reference cards (`numbered=False`) → at most
two warnings. Test-only content: no theory/Why? boxes, no concept-only graphs, no Test 1 counting (only nCk inside formulas). A final **Practice Questions** section opens with "Question N is always
one of these" and holds ~10 test-style problems; every solution starts with **Type:**/**Spot:** (the case) and uses that
case's step words (Spot, Find c, Accumulate, Differentiate, Rewrite, …; Q3: Mean → Square → Subtract → Root).
Write primes as `^{\prime}` (the 226 builder doesn't convert `\prime`).

From the repository root:

```powershell
.venv/Scripts/python.exe scripts/notes226/import_sources.py      # once: imports the PDFs, writes out/citations.json
cd scripts/notes226
python lintstr.py q1.py                                           # LaTeX must be in r'' strings
../../.venv/Scripts/python.exe -W error::SyntaxWarning q1.py --publish   # verify() + build + create/replace the note
node shots.cjs <docId> <outDir> [--dark] [--closed]               # KaTeX/overflow/tool errors + page slices
```

Doc ids are in `out/doc_<key>.txt` (one file per note so notes can be published in parallel).
Every number in a note is computed in its builder, and `verify()` re-checks the answers with sympy.
Write builders with the Write/Edit tools, never through a shell heredoc (heredocs eat LaTeX backslashes).
