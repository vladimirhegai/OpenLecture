# Structured documents v1

Documents contain stable `document_id`, `course_id`, `schema_version: 1`, `revision`, title, folder, purpose (`study_notes`, `revision_sheet`, `practice_set`, `reference`), optional academic week, canonical topic keys, ordered blocks, timestamps, and soft-delete state. LaTeX and Markdown-like text are stored as data; this backend never executes content or renders arbitrary HTML.

Every block has a UUID `id`, a discriminated `type`, and optional `citations`. Unknown types or extra properties are rejected. The discriminated union in `schemas.py` is the block registry; add a typed model and union member for a new kind, without changing storage tables.

| Type | Content |
|---|---|
| `paragraph` | `text` |
| `heading` | `text`, `level` 1-6 |
| `equation` | `latex`, `display` |
| `list` | `items`, `ordered` |
| `callout` | `text`, `tone` info/warning/tip |
| `table` | `columns`, rectangular `rows` |
| `code` | inert `language`, `text` |
| `derivation` | `title`, ordered steps containing `explanation` and `latex` |
| `practice_problem` | `title`, `prompt`, solution `steps` (`explanation`, optional `latex`) and/or Markdown `solution`, `answer`, `difficulty`, `origin` original/source |
| `worked_example` | `title`, `prompt`, `steps`, `answer` (shown solved) |
| `schematic` | `source` in the schematic language (`skills/schematic.md`), `caption` |
| `solution` | `title`, `text`, `collapsed` |
| `artifact_reference` | immutable `artifact_id`, `caption` |

Markdown text in any block may embed ` ```schematic ` fences; documents reject drawings that do not parse or that touch the middle of an element. Solutions are marked collapsible for a future renderer. Artifacts currently include circuit definitions, simulation results, probability/ODE math cards, and logic tables/maps. Card definitions include validated parameter schemas and chart data. Recompute explorations through non-persisting endpoints; save only when requested.

## Citations

```json
{"source_id":"<uuid>","version":1,"chunk_id":"<uuid>"}
```

All three values must resolve to an actual chunk in the same course. Source-derived practice requires at least one citation. This validates provenance existence, not semantic entailment: agents must still ensure a source actually supports a statement. Page/slide and extraction method are stored on the chunk. Previous source versions remain readable. New source versions flag dependent notes as potentially outdated without rewriting them.

## Targeted edits

```json
{
  "expected_revision": 2,
  "actor": "agent",
  "operations": [
    {"op":"insert","after_id":"<existing-block-uuid>","block":{"type":"paragraph","text":"Additional explanation."}}
  ]
}
```

`insert` adds a new block; `replace` requires `block_id` and a replacement with the same ID; `remove` requires `block_id`; `move` requires `block_id` and optional `after_id`. A missing/null `after_id` inserts or moves to the beginning. IDs and anchors must exist as appropriate. A failing operation rolls back the whole edit. Renaming uses `title`; moving uses `folder_id`, with explicit null meaning the course root. An omitted folder leaves it unchanged.

All edits create a new immutable revision. Document creation avoids duplicate purpose/week combinations, or purpose/topic sets when no week is specified, falling back to a normalized title. Separate copies require `separate_copy: true`. An `idempotency_key` makes creation retries safe; it does not make arbitrary edits replayable.
