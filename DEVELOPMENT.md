# Development

Requirements: Python 3.12+ and uv. Python 3.12 is selected by `.python-version`. `uv.lock` pins dependencies.

```sh
uv sync --locked
uv run pytest -q
uv run ruff check .
uv build
uv run open-lecture serve
```

The web app lives in `frontend/` (see [FRONTEND.md](FRONTEND.md)): `npm install`, `npm run build` writes `src/open_lecture/web/` (git-ignored, included in wheels as a hatch artifact), `npm run dev` hot-reloads against a running server, and `npm run screenshot` captures both themes and mobile for visual review. Build the frontend before `uv build` so distributions include it.

Tests use temporary workspaces. Integration tests exercise real SQLite transactions, migrations, PDF/DOCX/PPTX extraction, source versions, context selection, math subprocesses, SciPy distributions and ODEs, circuit analysis, and MCP stdio. No paid model calls are needed; agent runs are tested with recorded CLI event shapes and a fake process. MCP/process tests are included in the default suite; the current suite is small enough for a single run.

The default data directory is `.openlecture`. Keep source documents and personal academic data out of source control. To back up manually, stop HTTP and MCP processes, then copy the complete data directory (database and originals together). Do not copy just `workspace.sqlite3` while SQLite WAL writes are active. A portable course export/import format is still planned.

## Layout

- `api.py`: HTTP adapter, streaming events, agent runs, built frontend.
- `agents.py`: Claude Code / Codex CLI status, sign-in, and restricted headless runs with normalized events.
- `mcp_server.py`: typed agent tool adapter.
- `workspace.py`: document/catalog, transactional shared services and artifacts.
- `sources.py`, `extract.py`, `render_page.py`: original storage, recoverable jobs, bounded parser/page-render subprocesses.
- `chats.py`: messages, selection, extractive compaction, budgeted context diagnostics.
- `profiles.py`, `course_packs/`: reusable study guidance and syllabus-backed course profiles.
- `math_engine.py`, `study_tools.py`, `circuits.py`: validated computations.
- `schemas.py`: document block registry and request contracts.
- `migrations/`: ordered SQL migrations, applied under a cross-process write lock.

Source ingestion is single-worker per workspace using an OS lock. Other HTTP/MCP processes can enqueue jobs and read committed results. A crash releases the lock; the next owner requeues interrupted jobs. Files are immutable and stored under generated keys. A crash between storing bytes and committing metadata can leave an unreferenced file; automated orphan cleanup is not implemented.

## Limits

The local server defaults to loopback; optional bearer authentication is required by the CLI for other binds. Browser-origin checks reject unrelated sites. There is no multi-user identity or permission model. Source extraction has a 30-second deadline, PDF page rendering 15 seconds, symbolic math 10 seconds including startup. These are not hardened OS sandbox or memory quotas. Stay within the local single-user deployment scope.

Maximum upload is 20 MiB, extracted text 2 million characters, expanded Office archive 50 MiB, PDF 2000 pages, pending jobs 100. FastAPI's multipart parser may spool an HTTP upload before the application size check; network/proxy request-body limits are a deployment follow-up.

Adding a course does not require a new engine. Compose existing course packs and store a new topic map. Add a new computational capability only with strict input validation, declared scope and numerical/behavioral tests.
