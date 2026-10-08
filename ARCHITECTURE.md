# Architecture

Open Lecture owns a local SQLite database and immutable uploaded files. Agent clients are interchangeable. A React web app (see [FRONTEND.md](FRONTEND.md)) is served by the same process; the backend works without it, and no model subscription is required except for chat.

HTTP (FastAPI) and stdio MCP call the same `Workspace` application services. Pydantic validates inputs and document blocks. SQLite migrations ship with the package and run atomically on startup. Foreign keys, transactional writes, a unique document identity, and optimistic revision checks protect persistent content. Direct SQL keeps this initial single-user application small; an ORM is not required for service separation.

Core entities: course, folder, document, immutable document revision, source and source version, source chunk, ingestion job, chat, message, viewer state, extractive conversation summary, context inspection, immutable artifact, and replayable event. Stable UUIDs identify content. File paths and titles are not identities.

Document blocks have stable UUIDs, a discriminated `type`, typed content, and citations to a source version/chunk. Artifacts are immutable and referenced by ID. Notes have course/week/topic/purpose metadata. Deterministic discovery happens before creation; a unique identity prevents races and retry keys detect changed request bodies. Explicit separate copies get a distinct identity.

The context engine selects recent messages, relevant document blocks, and FTS5 source chunks within a conservative UTF-8-byte budget. Durable extractive summaries retain message IDs and artifact references; originals are never deleted. Viewing a document never grants edit permission. Request planning is explicit and non-mutating.

Background source ingestion uses a bounded in-process worker and persistent job records, with interrupted work rescheduled on startup. Events commit in the same transaction as their corresponding state changes. SSE clients can resume by sequence ID.

Math uses a restricted AST converted to SymPy objects (no eval or sympify on user text), in a subprocess with a deadline. Circuit input is parsed into a validated topology; verified resistive DC uses modified nodal analysis. Arbitrary SPICE commands are never accepted. General transient simulation requires an independently verified ngspice integration and is not silently approximated.

## Implementation sequence

1. Persistence, typed blocks, document discovery, revision-safe edits, HTTP.
2. Original file storage, recoverable extraction, versioned provenance, FTS retrieval.
3. Persistent chats, bounded context, action planning, event replay.
4. Shared MCP tools, computational artifacts, study examples.
5. Integration tests using real SQLite, real parsers and MCP transport; installation and contract documentation.

## Integration boundaries

MCP delegates language reasoning to the connected agent. For in-app chat, `agents.py` launches the student's locally signed-in Claude Code or Codex CLI headlessly for each turn, restricted to the Open Lecture MCP tools, and streams normalized events. Authentication stays with each CLI. There is no API-key provider or server-side model account. Source excerpts are untrusted data, never instructions. Hosted access needs a configured bearer token; the CLI binds loopback by default. This is a single-user service, not a multi-tenant authorization system.
