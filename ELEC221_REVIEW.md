# ELEC 221 Weeks 1–6 review

Reviewed and corrected on October 8, 2026, against the originals in `C:\Users\vladh\Downloads\Elec 221`. The saved course notes and source page notes have already been updated in the local workspace. This report records the scope, fixes, evidence, and remaining source ambiguities.

Open Lecture stores courses, uploaded originals, searchable source chunks, page transcriptions, and revisioned study notes in a local SQLite workspace. FastAPI exposes the same workspace operations to the React interface and MCP agents. The interface renders Markdown, KaTeX equations, and circuit schematics. Headless Codex/Claude sessions read sources or generate notes using the application's tools and writing instructions.

Uploads preserve the original file, validate the file type, detect duplicate content, assign a source version, and ingest its pages. The background reading worker renders PDF/image pages and sends four pages per call to the configured reading model. The existing ELEC 221 readings identify that model as `codex:gpt-6-luna:high`. Each page gets an `ai_digest` note with a citation ID; search prefers these notes over raw PDF extraction. Weekly note generation receives the page notes, original-page tools, syllabus topics, textbook problem index, and instructions to verify calculations and drawings.

The six lecture uploads match the downloaded originals byte for byte. Every lecture page has a completed, nonempty AI page note:

| Week | Lecture pages / page notes | Study-note blocks | Examples and problems | Current note revision |
| --- | ---: | ---: | ---: | ---: |
| 1 | 47 / 47 | 68 | 12 | 6 |
| 2 | 32 / 32 | 76 | 16 | 7 |
| 3 | 22 / 22 | 67 | 16 | 8 |
| 4 | 20 / 20 | 59 | 11 | 4 |
| 5 | 38 / 38 | 61 | 13 | 4 |
| 6 | 69 / 69 | 76 | 11 | 6 |
| Total | 228 / 228 | 407 | 79 | |

The review covered the six saved notes, lecture page transcriptions and original lecture images, supporting tutorial/assessment transcriptions, and the original pages and figures cited by the examples and practice problems. The textbook check covered 22 cited PDF pages, rather than its entire 816 pages. Labs were outside the requested lecture review; their uploaded readings are complete, but the three lab originals were absent from the supplied folder.

Factual corrections or necessary qualifications affected 39 saved blocks: 11 in Week 4, 12 in Week 5, and 16 in Week 6. Another 20 source page notes were corrected or annotated. Main findings:

- A Week 1 transcription merged intermediate nodes, turning series elements into parallel branches. The circuit's connections and polarities are now described correctly.
- Handwritten Tutorial 1 work was misread: a central resistor was 4 Ω, and the handwritten term was `4i₂`. The transcription no longer invents a different resistor value or an arithmetic error.
- Thévenin/Norton ratios now state their required conditions. Zero open-circuit voltage and short-circuit current require a test source; dependent sources can produce a valid negative equivalent resistance. Maximum-power matching requires a finite positive equivalent resistance and an adjustable passive load.
- Source constraints no longer automatically subtract an unknown for every dependent source. The controlling relation must actually permit a substitution.
- Week 5 superposition notes now preserve the nonzero controlling current and dependent voltage source in the voltage-source-only subproblem. A slide's swapped voltage/current output formulas are flagged and corrected.
- Week 6 now distinguishes resistor discharge current from capacitor current under the passive sign convention, preserves given initial states, qualifies DC steady-state shortcuts and continuity, and checks energy maxima at endpoints as well as stationary points.
- Textbook P6.15 now preserves the explicitly given zero initial voltage. Zero capacitor current alone would not establish that initial voltage.
- The open-switch RL drawing no longer claims it already carries an arbitrary nonzero initial current. Its general response formula explicitly allows an earlier circuit configuration to establish that current.

Some errors or ambiguities belong to the original material. Those remain identifiable in the source notes rather than being silently rewritten. In particular, Week 4 PDF page 5 labels a dependent source with an undefined controlling voltage, while the drawing names a different voltage. Week 6 PDF pages 33–34 omit waveform units; the numerical solutions now state their SI assumptions. On page 34, assuming volts gives `iₛ(t) = 3000 sin(t) + 0.008 A`; the slide's unitless `3 sin(t) + 8` is not an SI answer. Other annotations flag a power-reference sign, a nodal/mesh planarity mix-up, incorrect current-source deactivation wording, a missing capacitance factor in stored energy, and an RC initial-current sign/reference mismatch. These annotations distinguish the printed source from the checked result.

The dollar signs in Week 6 Topic 1 came from schematic captions being rendered as plain text. Schematic and artifact captions, plus expandable solution titles, now use the shared Markdown/math renderer. Mathematical ratios in all six saved notes now use readable stacked fractions, including inline derivatives. Unit ratios such as `V = J/C`, `W = J/s`, and `A/V` retain slash notation. Fractions inside exponents remain compact. Both AI writing instructions now specify this convention.

Source-reading fixes were also applied:

- Uploaded image files can now be rendered for the reading model, using the same page-rendering path as PDFs.
- Rereading preserves the page's citation ID and keeps its previous note available until the replacement succeeds. Previously, deleting the old chunk invalidated saved citations.
- Updated page notes refresh the search index, and raw extraction does not compete with an existing transcription of the same page.
- Invalid or oversized page notes fail explicitly rather than being silently truncated. Invalid model responses are limited to two attempts per page, preventing an endless retry loop.
- Weekly generation reports incomplete ingestion or reading of week-tagged sources before starting.

Verification completed:

- `uv run pytest -q`: **62 passed**. Added checks cover image upload/render/read, citation preservation during rereading, search replacement, readiness gating, and bounded retries for invalid model output.
- `uv run ruff check src tests`: **passed**.
- `npm run build` in `frontend`: **passed**, including TypeScript checking. The served frontend assets were rebuilt.
- All six notes were opened in a real browser with practice solutions expanded: **zero KaTeX errors and zero browser errors**. The corrected caption renders math, the inline derivative uses a stacked fraction, and the `J/C` unit ratio remains on one line.
- All **88 schematics** parsed and rendered. **34 numerical independent-source DC circuits** were solved, with KCL residuals no larger than approximately `7e-15` and power-balance residuals no larger than approximately `6e-13`.
- Dependent-source and transient calculations were checked against their equations and original reference directions. Additional symbolic checks confirmed the RL/RC initial values, final values and differential equations; P6.25's branch-current sum and energy balance; and P6.2's power/energy extrema.
- All **212 citation references** resolve to nonempty chunks in the correct course/source/version. The corrected source notes match their search entries, and SQLite integrity checking returns `ok`.

The existing Luna transcriptions were reviewed; this task did not launch a new live Luna generation. The regression tests exercise the upload and storage paths with controlled model responses. These checks support the corrected material and pipeline behavior, but do not establish that every future AI-generated answer will be correct. In particular, the built-in circuit simulator supports independent-source resistive DC circuits; dependent-source and transient results still require algebra/calculus verification.

Automatic page reading currently applies to non-textbook PDFs/images up to 80 pages. Textbooks are indexed and their needed problem pages are inspected separately; other document types use their extracted content. Thus a complete Luna transcription is available for each of these six lectures, but it is not the current policy for every possible uploaded source.

The pre-review SQLite backup, original note snapshots, correction logs, verified snapshots, figures, browser results, and calculation evidence are in `.openlecture/review-elec221/`. The main records are `corrections.json`, `refinements.json`, `last-unit-correction.json`, `fraction-size.json`, `integrity-and-math.json`, `diagram_checks.txt`, and `ui-results.json`. Document edits use revision history and retain citation identities. Original PDFs were not changed.

**Optional follow-ups**

- Support automatic or explicitly requested page reading for larger non-textbook PDFs beyond the current 80-page limit.
- Extend automated circuit validation to dependent sources and transient responses.
- Align README upload/extraction defaults with `Settings`: the README currently says 20 MiB / 2 million characters; the code defaults are 100 MiB / 8 million characters.
- Address the existing Starlette/httpx test-client deprecation warning when updating dependencies.
