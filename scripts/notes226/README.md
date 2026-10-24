# ELEC 226 Test 2 notes

Four Open Lecture notes, one per question of In-Class Test 2 (Fri Oct 30 2026, 40 min, closed book, no formula sheet, Lectures 7–15):

| Note | Builder | Covers |
|---|---|---|
| Test 2 - Question 1 | `q1.py` | random experiments, sample spaces, discrete RVs, PMFs, CDFs (L7–9) |
| Test 2 - Question 2 | `q2.py` | continuous RVs, PDFs, probability calculations (L9–11) |
| Test 2 - Question 3 | `q3.py` | expected value, variance, their properties (L11–13) |
| Test 2 - Question 4 | `q4.py` | functions of continuous RVs and their distributions (L12–15) |

Each note: topics only (no subtopics), each one explained with bullets, equation blocks, graphs and worked examples, with a few
"Try it" problems. Purple `reminder` callouts recap Test 1 or calculus material only where the topic uses it.
A final **Practice Questions** section holds about 10 test-style problems (easy → hard, source in the title).

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
