# Progress

Updated 2026-10-07. Working backend plus a first web interface. Not the complete v2 specification or a production-ready study application.

Latest validation: **42 automated tests passed**, Ruff passed, the frontend typechecks and builds, and wheel/source distributions built successfully. A separate real HTTP example ran twice with no duplicate course/document. Both subagents' regression suites are included in the test count. The single test warning is an upstream Starlette TestClient deprecation.

## Web interface (2026-10-07)

Implemented and checked in a real browser (Edge via `npm run screenshot`, light and dark, 1440 px and 390 px):

- Three-pane layout: course navigation, note/source viewer, chat. Drawer and full-screen chat on mobile.
- Light, dark and system themes with no flash on load; Instrument Sans UI, Newsreader reading text, KaTeX math.
- Note reader: every block type, citation pills that open the cited PDF page, revision history with old-revision banner, delete with undo, ask-about-block.
- Source viewer: lazily rendered PDF pages, page jump, zoom, dark pages, download; DOCX/PPTX/Markdown text view with slide labels.
- Computed-result cards: probability/ODE charts with hover tooltips, truth tables, DC results in engineering units.
- Search palette (notes and full-text passages), course creation, uploads with kind selection, live refresh from workspace events.
- Chat with Claude Code or Codex through the student's own CLI sign-in: provider/model/effort picker, streaming tool activity, stop, chat history, context from the current note, page or block.
- Settings: theme, account status with sign-in/sign-out, chat model, about.

Verified with real CLIs: Claude (Haiku) and Codex (GPT-5.6-Luna) turns answered with cited syllabus pages. Stop killed the CLI process tree, including its MCP server, and the next message in the same chat worked. Built-in tool restriction was confirmed by asking each agent to list its tools.

Not verified: the sign-in and sign-out buttons against real accounts. They were exercised with mocked status so this machine's CLI sessions stayed signed in. The terminal-opening path is implemented for Windows, macOS and common Linux terminals but was only reasoned about, not run. The token prompt for `OPENLECTURE_API_TOKEN` deployments is untested, and live events are disabled in that mode.

## Implemented and tested

- Local SQLite persistence, atomic migrations and referential integrity.
- Courses, parent-linked folders, extensible course profiles and five reusable study/PDF skills.
- Structured notes, stable block IDs, LaTeX/derivations/solutions, citations and immutable artifacts.
- Revision-safe targeted edits, audit history, soft delete/restore, duplicate prevention and creation retry keys.
- PDF/Markdown/text/CSV/JSON/DOCX/PPTX ingestion, originals, versions, durable jobs, FTS5 retrieval and stale-note flags.
- One-page PDF image rendering for visual inspection of diagrams/equations.
- Persistent chats and references, viewer selection, explicit non-mutating action planning.
- Bounded context packets, query-bearing excerpts, course-aware guidance, extractive compaction and diagnostics.
- Persistent reconnectable SSE workspace events.
- Real stdio MCP transport and shared HTTP/MCP data, including independent subagent acceptance testing.
- Exact arithmetic, differentiation, bounded polynomial roots through SymPy; binomial and five further probability distributions.
- First/second-order constant-coefficient ODE trajectories via matrix exponentials.
- Combinational truth tables, verified SOP simplification, 2-4-variable Karnaugh maps.
- Validated DC circuit language, restricted SPICE compilation, real NumPy nodal analysis and saved results.

## Implemented but not fully tested

- OS-lock worker recovery behavior is implemented; exhaustive crash-injection and long-running load testing remain.
- Codex/Claude `.mcp.json`/`config.toml` examples are based on official documentation; headless sessions launched by the in-app chat are verified (see above), interactive use inside those applications is not.
- User's four real syllabi are imported locally and indexed; educational note quality over complete lecture/tutorial collections is not yet evaluated because those files were not supplied.

## Partial

- Context compaction is lossy and extractive, not semantic long-term learning memory.
- Course skills guide note quality and tool selection; they do not create missing computations or guarantee model reasoning.
- Circuit engine supports resistive DC; an ODE exploration tool can illustrate explicitly derived RC/RLC equations but is not a general transient circuit simulator.
- Notes are rendered but not editable by hand in the UI; edits happen through the agent (MCP/HTTP targeted edits).
- In-app chat stores only the final answer; intermediate agent commentary and tool steps are shown live but not persisted. Each turn is a fresh CLI process, so there is a few seconds of startup per message.
- PDF page count comes from the highest page with extracted text; trailing image-only pages are not shown.
- Local safety controls and bounded workloads exist; OS-level memory isolation and remote multi-user operation are not implemented.

## Planned

- Structured-output validation for agent-written notes beyond the existing block schema; per-message provider/model metadata.
- General ngspice transient/AC simulation, dependent sources, interactive schematic rendering.
- More symbolic ODE/Laplace tools, joint-distribution and stochastic-process tools, sequential logic/HDL tools.
- OCR, more sophisticated equation/table extraction, semantic/vector retrieval and retrieval caches.
- Durable learning progress/memory, semantic compaction with unresolved-task tracking.
- Portable course export/import, automated backups, folder/source editing and full entity lifecycle APIs.
- Hand editing of notes in the reader; drag-and-drop uploads; interactive schematic rendering.

## Blocked

- No ngspice executable was available during this build; no ngspice execution is claimed.
- Detailed source-grounded course notes need actual lecture/tutorial materials beyond the four supplied syllabi.

## Optional follow-ups

- Address the upstream Starlette TestClient deprecation notice when updating test dependencies.
- Add strict deployment upload limits, hardened subprocess memory quotas and orphan-file cleanup before exposing the service beyond a trusted local environment.

## Subagent findings resolved

Independent tests found that an oversized selected paragraph could disappear from context and that unrelated history could displace the only relevant source. Context now keeps marked excerpts and prioritizes evidence. Independent study-session tests cover citations, revisions, artifact embedding, shared storage and course isolation.

A second agent pass found a vague-query fallback regression and a nested PDF-render subprocess timeout over MCP on Windows. The fallback now retains a small introduction; parser/render subprocesses explicitly detach stdin from the MCP transport. Both regression cases pass.
