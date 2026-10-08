# Agent connection

The stdio server is a real MCP server using the official Python SDK. It reads the same SQLite database and immutable originals as HTTP. Always set the **same absolute** `OPENLECTURE_DATA_DIR` in both processes. The server does not call a model, reuse CLI authentication, or own a separate transcript database.

## Codex

Add to a trusted project's `.codex/config.toml` or your chosen Codex configuration, adjusting paths:

```toml
[mcp_servers.open_lecture]
command = "uv"
args = ["--directory", "C:/dev/Coding/OpenLecture", "run", "open-lecture-mcp"]
startup_timeout_sec = 30
tool_timeout_sec = 45

[mcp_servers.open_lecture.env]
OPENLECTURE_DATA_DIR = "C:/dev/Coding/OpenLecture/.openlecture"
```

Codex supports local stdio servers with command/args/env and project-scoped configuration. See the [official Codex MCP documentation](https://developers.openai.com/codex/mcp). No configuration has been installed globally by this project.

## Claude Code

Use a project `.mcp.json` (merge with existing servers rather than overwriting them):

```json
{
  "mcpServers": {
    "open_lecture": {
      "type": "stdio",
      "command": "uv",
      "args": ["--directory", "C:/dev/Coding/OpenLecture", "run", "open-lecture-mcp"],
      "env": {"OPENLECTURE_DATA_DIR": "C:/dev/Coding/OpenLecture/.openlecture"}
    }
  }
}
```

Claude Code supports local stdio MCP commands and project-scoped configuration; see [its official MCP documentation](https://code.claude.com/docs/en/mcp). Client approval/trust settings remain under your control. If `uv` is not on a client's PATH, use its absolute executable path.

## Agent workflow

1. `course_list`, `course_get`, `course_study_guidance`; `study_skill_list` and `study_skill_read` for the `weekly-notes`, `textbook-problems`, `schematic` and `source-reading` skills.
2. `document_plan` and `document_find` before generating notes.
3. `source_notes` to read a course PDF (AI notes of every page, including handwriting and circuits); `source_search` for relevant passages; `source_page` only to look at a figure. For practice, `textbook_outline` and `textbook_problems`, then `source_page` on the problem's page.
4. Draw circuits in the schematic language (`study_skill_read schematic`) and confirm each drawing with `schematic_check`, which lists the nodes every element connects.
5. Use `math_evaluate`, `math_binomial`, `probability_distribution`, `math_linear_ode`, `logic_truth_table`, or circuit tools where supported.
6. Save reusable computations using the save-card tools; embed returned artifact IDs in validated blocks.
7. `document_create` or revision-safe `document_update`, then a short `chat_add_message` with its committed reference.
8. `context_select` and `context_retrieve` for follow-ups; ordinary questions do not edit notes.

`study_skill_list` lists skills without full guidance. Discovery/list tools omit large content where possible. PDF rendering returns actual image content. All user inputs are typed; invalid blocks/tool arguments are rejected. Source uploads over MCP accept bounded UTF-8 text as student notes; original binary uploads use HTTP multipart. No tool accepts an arbitrary filesystem path or shell command.

## Verification status

Automated tests launch a separate server process, initialize an actual MCP session, enumerate schemas, and call tools over stdio. They verify that MCP-created documents are visible over HTTP and HTTP edits are visible over MCP, including conflicts, provenance, isolation and computations. Subagent-authored acceptance tests repeat the study workflow independently.

The configurations above are documented from official sources. The in-app chat (see [API.md](API.md#chat-with-a-local-agent)) launches both CLIs headlessly with an equivalent per-run MCP configuration. Real end-to-end turns were run on 2026-10-07 with Claude Code 2.1.207 and Codex CLI 0.146.0: both called Open Lecture tools and answered with syllabus page citations, and a Codex follow-up in the same chat used context from an earlier Claude turn. Interactive use of the `.mcp.json`/`config.toml` setups above inside those applications' own UIs is still unverified.
