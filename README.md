# Open Lecture

A local-first, open-source study workspace. Organize courses, ingest lecture files, search cited passages, and maintain structured study notes with revision history. Read notes and PDFs side by side with a chat that runs on your own Claude Code or Codex sign-in, or connect an agent through MCP. Your data stays in one local workspace.

**Status:** early release with a web interface. See [PROGRESS.md](PROGRESS.md) for tested capabilities and remaining work, and [FRONTEND.md](FRONTEND.md) for every screen and control.

## Run

Install Python 3.12+, [uv](https://docs.astral.sh/uv/) and Node.js 20+, then run from this directory:

```sh
uv sync
cd frontend && npm install && npm run build && cd ..
uv run open-lecture serve
```

Open http://127.0.0.1:8000 for the app and http://127.0.0.1:8000/docs for the interactive API. To chat, install the [Claude Code](https://code.claude.com/docs/en/setup) and/or [Codex](https://developers.openai.com/codex/cli) CLI and sign in from **Settings**. Chats use your own subscription; Open Lecture never handles your credentials. Data defaults to `.openlecture/`; set `OPENLECTURE_DATA_DIR` to an absolute directory to share it between server and MCP clients.

```sh
uv run python examples/study_session.py
uv run pytest
uv run ruff check .
uv run open-lecture-mcp
```

Your four Fall 2026 syllabi can be loaded with:

```powershell
uv run python examples/setup_semester.py --syllabus-dir 'C:\Users\vladh\Downloads'
```

The local workspace has been initialized with these four courses, syllabus originals, cited course maps, and reusable subject/PDF study skills. See [COURSE_PACKS.md](COURSE_PACKS.md) for the course-specific tools and their limits. This setup does not bundle the PDFs into the open-source project.

The example creates a small demonstration course using original sample material, retrieves a cited passage, creates notes, and makes a targeted revision. It needs the HTTP server running. Re-running it reuses its course and document.

Read [FRONTEND.md](FRONTEND.md), [API.md](API.md), [MCP.md](MCP.md), [DOCUMENT_FORMAT.md](DOCUMENT_FORMAT.md), [CONTEXT_ENGINE.md](CONTEXT_ENGINE.md), [CIRCUIT_LANGUAGE.md](CIRCUIT_LANGUAGE.md), [HEIGHT_METHOD.md](HEIGHT_METHOD.md) (the height/river method used by the circuit notes), and [DEVELOPMENT.md](DEVELOPMENT.md) for contracts and setup. Design decisions are in [ARCHITECTURE.md](ARCHITECTURE.md).

## Local configuration

Environment variables (or a local `.env` file):

- `OPENLECTURE_DATA_DIR`: database and source-file directory.
- `OPENLECTURE_API_TOKEN`: optional bearer token; required by the CLI when binding beyond loopback.
- `OPENLECTURE_MAX_UPLOAD_BYTES`: default 20 MiB.
- `OPENLECTURE_MAX_EXTRACTED_CHARS`: default 2 million characters per source.

The API is single-user. Keep it on loopback unless you provide authentication and a trusted deployment environment. No cloud service or API key is needed for persistence, retrieval, math, or supported DC circuit analysis. Chat needs a signed-in Claude Code or Codex CLI on the same computer.

## Quick start on Windows

Install Python 3.12+ and Node.js once ([uv](https://docs.astral.sh/uv/) is optional), then double-click `Open-Lecture.bat`. It reuses the server if one is already running; otherwise it sets up `.venv` when it is missing or broken, rebuilds the interface when its sources changed, starts the server in the background (on the next free port if 8000 is taken by another program) and opens the browser. `Stop-Open-Lecture.bat` stops only Open Lecture. Both call `scripts\launcher.ps1` (`start`, `stop`, `status`). The server log is `.openlecture\server.log`, and a failed start prints its last lines.

## Install on macOS

Use the Apple Silicon (`arm64`) or Intel (`x86_64`) disk image for your Mac. Open the `.dmg`, drag **Open Lecture** to **Applications**, then open it from Applications. The app starts its local server and opens your default browser. Quit from the Open Lecture menu or Dock to stop the server.

The download includes Python and the web interface and creates a fresh workspace in `~/Library/Application Support/Open Lecture/`. AI chat still needs Claude Code or Codex installed and signed in. The build targets macOS 14 and later. The test builds use an ad hoc signature, so macOS may ask you to approve the first launch in **System Settings → Privacy & Security**.

To build the disk image, run `bash scripts/macos/build.sh` on a Mac with Xcode command-line tools, Node.js 24, and uv. Intel builds also need Rust and Homebrew's `openssl@3`. The script writes the `.dmg` to `dist/macos/`. The **Build macOS download** GitHub Actions workflow builds both architectures.

## Your data

Notes, chats and settings live in `.openlecture/workspace.sqlite3`, and the uploaded PDFs in `.openlecture/sources/`. This repository currently tracks those files, so cloning it copies that workspace. Commit the database only while the server is stopped (`Stop-Open-Lecture.bat`). `uv run python scripts/export_notes.py` writes every note as Markdown to `notes/`, readable without the app.
