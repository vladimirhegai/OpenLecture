# Context without loading the whole course

`context_retrieve` / POST `/courses/{course}/chats/{chat}/context` accepts a query and a budget (default 6000, 1000-32000). No LLM call is used for retrieval, intent planning, or compaction.

The budget is a cap, not a target. The engine reserves 25% and counts the serialized input packet conservatively as one UTF-8 byte per token. This typically overestimates real token usage. It counts framing and metadata too. The returned diagnostics describe **only this workspace packet**; a connected agent must independently budget its own system instructions, tool definitions, history, images, and outputs. This backend cannot enforce Codex/Claude's full session budgets.

## Selection

1. Keep the current question and selected document/revision/block identities.
2. Prioritize a selected or query-relevant document block and the highest-ranked source passage.
3. Add compact course-skill identities, up to two matching guidance rules, and up to two study preferences.
4. Add up to four bounded recent/relevant messages and a small extractive summary, if they fit.
5. Add remaining relevant blocks/passages while respecting the cap (at most three each).

Large blocks/passages receive query-bearing excerpts with `excerpt: true`, stable IDs, revision/version metadata, and retrieval hints. Full content stays retrievable. Unrelated blocks are not included just because the document is open; a vague query with no selected block falls back to at most two introductory blocks. Source search considers current source versions; historical citations remain independently accessible. Full course-skill guidance is fetched deliberately through `course_study_guidance`, not appended to every question. PDF image pages are explicitly requested one at a time and are outside the text context budget.

No selected document is automatically edited. Viewing pins the chosen revision. Document planning uses explicit question/create/edit/separate intent; it is not a natural-language intent classifier.

## Compaction and limits

Long histories trigger a durable **lossy extractive** summary of older turns while preserving every original message. Recent turns remain available; summaries retain message IDs, document references, and a link to their predecessor. They do not make model-generated claims about user knowledge or decisions.

This is deliberately a small implementation, not a full semantic memory system. Unresolved tasks are not guaranteed to survive extractive compression, older summaries are not automatically merged, and the engine may omit candidates under pressure. `omitted_candidates`, per-category estimates, and the saved context inspection expose that behavior. A caller should retrieve missing evidence rather than guess.

## Independent regression scenarios

Subagent-written tests exercise an 80-block note, an oversized selected paragraph, long unrelated history with a relevant lecture, concise course guidance, vague follow-ups, and cross-course isolation. They found dropped large blocks, history displacing evidence, and a vague-query fallback regression. These were fixed by bounded excerpts, evidence-first selection, and a small open-document fallback. The fixtures use real SQLite, HTTP and ingestion, not mocked search results.

Measured fixture packet sizes: 764 UTF-8 bytes for a simple follow-up in an approximately 280 KB note; 1397 bytes for an oversized selected paragraph; 2649 bytes for relevant evidence alongside a 24-message history. These are reproducible fixture results, not provider billing or production performance claims.

Optional future improvements: exact provider token counters, section-level read tools for external clients, semantic summaries with explicit unresolved-task state, retrieval caching, and embeddings. None is required for a basic source-grounded question.
