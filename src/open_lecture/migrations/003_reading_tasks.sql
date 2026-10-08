ALTER TABLE sources ADD COLUMN week INTEGER;
ALTER TABLE source_versions ADD COLUMN page_count INTEGER;
CREATE TABLE source_digests (
    source_id TEXT NOT NULL, version INTEGER NOT NULL, course_id TEXT NOT NULL REFERENCES courses(id),
    status TEXT NOT NULL, pages_total INTEGER NOT NULL DEFAULT 0, pages_done INTEGER NOT NULL DEFAULT 0,
    model TEXT, error TEXT, updated_at TEXT NOT NULL,
    PRIMARY KEY(source_id, version),
    FOREIGN KEY(source_id, version) REFERENCES source_versions(source_id, version)
);
CREATE TABLE textbook_sections (
    id TEXT PRIMARY KEY, course_id TEXT NOT NULL REFERENCES courses(id), source_id TEXT NOT NULL,
    version INTEGER NOT NULL, level INTEGER NOT NULL, chapter INTEGER, title TEXT NOT NULL,
    start_page INTEGER NOT NULL, end_page INTEGER NOT NULL,
    FOREIGN KEY(source_id, version) REFERENCES source_versions(source_id, version)
);
CREATE INDEX textbook_section_source ON textbook_sections(source_id, version, chapter);
CREATE TABLE textbook_problems (
    id TEXT PRIMARY KEY, course_id TEXT NOT NULL REFERENCES courses(id), source_id TEXT NOT NULL,
    version INTEGER NOT NULL, chapter INTEGER NOT NULL, number TEXT NOT NULL, kind TEXT NOT NULL,
    section TEXT, page INTEGER NOT NULL, text TEXT NOT NULL,
    FOREIGN KEY(source_id, version) REFERENCES source_versions(source_id, version)
);
CREATE INDEX textbook_problem_source ON textbook_problems(source_id, version, chapter);
CREATE VIRTUAL TABLE textbook_problem_fts USING fts5(problem_id UNINDEXED, text, tokenize='unicode61');
CREATE TABLE app_settings (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE agent_tasks (
    id TEXT PRIMARY KEY, course_id TEXT NOT NULL REFERENCES courses(id), kind TEXT NOT NULL,
    title TEXT NOT NULL, status TEXT NOT NULL, params TEXT NOT NULL, log TEXT NOT NULL,
    result TEXT, error TEXT, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE INDEX agent_task_course ON agent_tasks(course_id, created_at);
