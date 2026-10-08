# HTTP API v1

Run `uv run open-lecture serve`; interactive documentation is at `http://127.0.0.1:8000/docs`, and machine-readable schemas at `/openapi.json`. The OpenAPI document is generated from the same Pydantic input types used by MCP. Responses are JSON; UUIDs are strings, timestamps UTC ISO 8601.

All course resources live under `/api/v1/courses/{course_id}`. Passing another course's object ID returns 404. This is data isolation in a single-user workspace, not multi-user authorization.

| Route relative to course | Methods | Behavior |
|---|---|---|
| `/profile` | GET, PUT | Read or revision-check an extensible topic map and study skills |
| `/study-guidance` | GET | Selected skills, note recipe, syllabus citations, available/planned tools |
| `/folders` | GET, POST | Parent-linked folder tree |
| `/documents` | GET, POST | Metadata discovery or create validated blocks |
| `/documents/{id}` | GET, PATCH | Read current/historical content or apply targeted edits |
| `/documents/{id}/revisions` | GET | Immutable history metadata |
| `/documents/{id}/delete`, `/restore` | POST | Revision-checked soft deletion/restoration |
| `/document-actions/plan` | POST | Explicit question/create/edit/separate intent; no content mutation |
| `/sources` | GET, POST | List sources or upload multipart `file`, `kind`, optional existing `source_id` |
| `/sources/{id}` | GET | Paginated chunks with version, page/slide, section and extraction method; `pages` is the highest page/slide with text |
| `/sources/{id}/original` | GET | Download the retained original; optional `version` |
| `/sources/{id}/pages/{page}` | GET | Render one PDF page as PNG; optional `version`, 1-based page |
| `/search` | GET | FTS5 search with `query`, `limit`; latest source versions only |
| `/jobs/{id}` | GET | Durable status: queued, running, completed, failed |
| `/jobs/{id}/retry` | POST | Requeue a failed ingestion job |
| `/chats` | GET, POST | Persistent chats |
| `/chats/{id}/messages` | GET, POST | Original messages and validated document references |
| `/chats/{id}/viewer-state` | PUT | Select a document/revision/block, without editing it |
| `/chats/{id}/context` | POST, GET | Assemble bounded evidence or inspect the last selection |
| `/math-cards/binomial`, `/math-cards/distribution`, `/math-cards/linear-ode` | POST | Compute and persist a typed artifact |
| `/logic-cards` | POST | Save a truth table, equivalent SOP and optional Karnaugh map |
| `/circuits` | POST | Save an immutable circuit definition and validated topology |
| `/circuits/{id}/simulate` | POST | Save a real DC operating-point result |
| `/artifacts`, `/artifacts/{id}` | GET | List metadata or retrieve an immutable artifact |
| `/events` | GET | Replayable SSE, `after`, `Last-Event-ID`, optional `follow=false` |

## Chat with a local agent

| Route | Methods | Behavior |
|---|---|---|
| `/api/v1/agents` | GET | Claude Code and Codex CLI status: installed, signed in, account/plan, models with effort levels. Cached 20 s; `refresh=true` re-checks |
| `/api/v1/agents/{provider}/login` | POST | Opens the CLI's own sign-in in a new terminal window. Returns `{opened, command}`; when `opened` is false, run `command` yourself |
| `/api/v1/agents/{provider}/logout` | POST | Signs the CLI out on this computer and returns fresh status |
| `/courses/{id}/chats/{chat}/runs` | POST | Body `{provider, model, effort?, content, document?, source_id?, source_page?}`. Saves the user message, runs one headless agent turn, and streams SSE `data:` events: `user_message`, `text_start`, `text` (delta), `tool` (name), then `done` (saved assistant message) or `error`. Closing the connection cancels the run. One run per chat at a time (409) |

Each turn runs `claude -p` or `codex exec` with only the Open Lecture MCP server available: Claude gets `--tools ToolSearch` plus `mcp__open_lecture`; Codex runs in a read-only sandbox with shell, browser, computer-use, plugins and web search disabled. Codex keeps its code-mode host (0.160+ routes MCP calls through it; it adds no shell) and a few non-mutating built-ins (image viewing, planning). The newest installed copy of each CLI is used, found on PATH and in the Codex desktop app, Claude desktop and IDE extension folders; older copies lack newer models, and an old Codex CLI overwrites the shared model cache with a shorter list. The prompt includes the backend's bounded context packet, so provider or model changes mid-chat keep continuity. Model and effort names are validated against a strict pattern; prompts go over stdin, never the command line.

## Source reading, textbooks and background tasks

Every PDF or image source up to 80 pages is read by an AI model from page images, four pages per call, three sources in parallel, following the `source-reading` skill. Each page's note is stored as an `ai_digest` chunk on that page. Search, chat context and citations then use these notes instead of the raw PDF text (raw chunks stay for provenance). Image-only PDFs are accepted. Textbooks (`kind=textbook`) are not read: their PDF outline and numbered end-of-chapter problems are indexed.

| Route | Methods | Behavior |
|---|---|---|
| `/api/v1/settings` | GET, PUT | `{reading_model: {provider, model, effort}}`; default Codex `gpt-6-luna`, `high` |
| `/api/v1/skills`, `/api/v1/skills/{name}` | GET | Workflow skills (`source-reading`, `weekly-notes`, `textbook-problems`) |
| `/courses/{id}/sources` | POST | Also accepts `week`, kinds `textbook`, `practice`, `lab`, and PNG/JPG/WEBP. The week is inferred from the filename when omitted |
| `/courses/{id}/sources/{sid}/notes` | GET | The AI page notes, `first_page`/`last_page` |
| `/courses/{id}/sources/{sid}/read` | POST | Re-read all pages, or `{pages: [...]}` |
| `/courses/{id}/textbook/outline` | GET | Chapters, or a chapter's sections with `chapter` |
| `/courses/{id}/textbook/problems` | GET | `chapter`, `section` (e.g. `4.2`), `query`; number, page, preview, citation |
| `/courses/{id}/weeks/{week}/generate` | POST | `{provider, model, effort, regenerate}`; writes that week's notes in the background (409 while one runs) |
| `/courses/{id}/tasks` | GET | Background tasks (`read_source`, `week_notes`), `active=true` for running ones; each has a step log |
| `/courses/{id}/tasks/{task}/cancel` | POST | Stops the task and its CLI process tree |

Source lists include `week`, `page_count`, `reading_status` (`pending`, `running`, `ready`, `failed`, `skipped`) and page progress. New events: `task.updated`, `source.reading_updated`. The server runs background agents only when `OPENLECTURE_AGENT_RUNNER` is true (the default); MCP processes never do. Upload limit: 100 MiB; extracted text limit: 8 million characters.

Global routes: GET/POST `/api/v1/courses`, GET `/api/v1/courses/{id}`, GET `/api/v1/health`, GET `/api/v1/course-packs`. Computation routes without persistence: POST `/api/v1/math/evaluate`, `/math/binomial`, `/math/distribution`, `/math/linear-ode`, `/logic/truth-table`, `/circuits/validate`. POST `/api/v1/schematics/render` with `{"source": ...}` returns a schematic-language drawing as SVG (`image/svg+xml`); `/schematics/check` returns the nodes and element connections it implies.

## Pagination and discovery

Lists accept `limit` (1-100) and `offset` (nonnegative), defaulting to 50/0. Messages use `after` (sequence ID). Source chunks use `limit` and `offset`. Document discovery accepts `query` (title/topic text), `academic_week`, `document_type`, `topic` (exact key), and `include_deleted`. Results omit blocks. Source search is lexical, not semantic/vector search.

## Writes, errors, and references

Document creation returns `{created, document}`. The document includes a `reference` with `document_id`, `course_id`, `revision`, `title`, and a relative `route`. The web app uses the same routes (`/courses/{id}/docs/{document}`), so references open directly in the viewer. Idempotent retries return the already saved document. Changed bodies under the same key return 409. Equivalent notes return 409 with the existing reference in error details.

Edits and delete/restore operations require `expected_revision`. On conflict, read the current revision and deliberately reapply a targeted edit; never automatically overwrite human changes. Profile updates similarly use `expected_revision`, starting at 0.

Domain errors use `{error: {code, message, details}}`. Common statuses: 400 invalid action/citation, 404 missing or wrong-course entity, 409 revision/identity conflict, 413 upload size, 415 unsupported format, 422 schema/computation failure, 429 full ingestion queue. Validation responses omit raw request content. FastAPI's framework-level routing errors may use its native `detail` shape.

Document references must point to a committed revision, and optional block IDs must exist in that revision. Saving a chat message never invokes a model or modifies its referenced document. A viewer selection pins a revision until explicitly changed.

## Events

Events commit with content and have globally monotonic sequence IDs filtered by course. Event types include `course.created`, `course.profile_updated`, `document.created`, `document.updated`, `document.deleted`, `document.restored`, `source.ingestion_queued`, `source.ingestion_started`, `source.ingestion_completed`, `job.failed`, `chat.message_added`, `context.compacted`, and `artifact.created`.

Reconnect with the last ID to avoid reprocessing old events. `follow=false` drains available events and closes, useful for tests and polling. This release streams workspace events, not generated model text.
