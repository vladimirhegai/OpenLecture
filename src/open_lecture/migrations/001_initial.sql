CREATE TABLE courses (id TEXT PRIMARY KEY, code TEXT NOT NULL, title TEXT NOT NULL, created_at TEXT NOT NULL);
CREATE TABLE folders (
    id TEXT PRIMARY KEY, course_id TEXT NOT NULL REFERENCES courses(id),
    parent_id TEXT REFERENCES folders(id), title TEXT NOT NULL
);
CREATE TABLE documents (
    id TEXT PRIMARY KEY, course_id TEXT NOT NULL REFERENCES courses(id),
    folder_id TEXT REFERENCES folders(id), title TEXT NOT NULL, document_type TEXT NOT NULL,
    academic_week INTEGER, topic_keys TEXT NOT NULL, identity_key TEXT NOT NULL,
    revision INTEGER NOT NULL, deleted INTEGER NOT NULL DEFAULT 0, payload TEXT NOT NULL,
    created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE INDEX document_catalog ON documents(course_id, document_type, academic_week, deleted);
CREATE UNIQUE INDEX document_identity ON documents(course_id, identity_key) WHERE deleted=0;
CREATE TABLE document_revisions (
    document_id TEXT NOT NULL REFERENCES documents(id), revision INTEGER NOT NULL,
    payload TEXT NOT NULL, actor TEXT NOT NULL, created_at TEXT NOT NULL,
    PRIMARY KEY(document_id, revision)
);
CREATE TABLE idempotency (
    course_id TEXT NOT NULL REFERENCES courses(id), key TEXT NOT NULL,
    request_hash TEXT NOT NULL, document_id TEXT NOT NULL REFERENCES documents(id),
    PRIMARY KEY(course_id, key)
);
CREATE TABLE sources (
    id TEXT PRIMARY KEY, course_id TEXT NOT NULL REFERENCES courses(id),
    filename TEXT NOT NULL, kind TEXT NOT NULL, current_version INTEGER NOT NULL, created_at TEXT NOT NULL
);
CREATE TABLE source_versions (
    source_id TEXT NOT NULL REFERENCES sources(id), version INTEGER NOT NULL,
    hash TEXT NOT NULL, storage_key TEXT NOT NULL, status TEXT NOT NULL,
    error TEXT, created_at TEXT NOT NULL, PRIMARY KEY(source_id, version)
);
CREATE TABLE chunks (
    id TEXT PRIMARY KEY, course_id TEXT NOT NULL REFERENCES courses(id), source_id TEXT NOT NULL,
    version INTEGER NOT NULL, page INTEGER, section TEXT, text TEXT NOT NULL, method TEXT NOT NULL,
    FOREIGN KEY(source_id, version) REFERENCES source_versions(source_id, version)
);
CREATE INDEX chunk_source ON chunks(source_id, version);
CREATE VIRTUAL TABLE source_fts USING fts5(chunk_id UNINDEXED, text, tokenize='unicode61');
CREATE TABLE jobs (
    id TEXT PRIMARY KEY, course_id TEXT NOT NULL REFERENCES courses(id), kind TEXT NOT NULL,
    source_id TEXT NOT NULL, version INTEGER NOT NULL, status TEXT NOT NULL,
    error TEXT, created_at TEXT NOT NULL, updated_at TEXT NOT NULL,
    FOREIGN KEY(source_id, version) REFERENCES source_versions(source_id, version)
);
CREATE TABLE chats (
    id TEXT PRIMARY KEY, course_id TEXT NOT NULL REFERENCES courses(id), title TEXT NOT NULL,
    viewer_state TEXT NOT NULL DEFAULT '{}', created_at TEXT NOT NULL
);
CREATE TABLE messages (
    sequence INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT UNIQUE NOT NULL,
    chat_id TEXT NOT NULL REFERENCES chats(id), role TEXT NOT NULL,
    content TEXT NOT NULL, references_json TEXT NOT NULL, created_at TEXT NOT NULL
);
CREATE TABLE summaries (
    id TEXT PRIMARY KEY, chat_id TEXT NOT NULL REFERENCES chats(id), through_sequence INTEGER NOT NULL,
    payload TEXT NOT NULL, created_at TEXT NOT NULL
);
CREATE TABLE context_inspections (
    id TEXT PRIMARY KEY, chat_id TEXT NOT NULL REFERENCES chats(id), payload TEXT NOT NULL, created_at TEXT NOT NULL
);
CREATE TABLE artifacts (
    id TEXT PRIMARY KEY, course_id TEXT NOT NULL REFERENCES courses(id), kind TEXT NOT NULL,
    title TEXT NOT NULL, payload TEXT NOT NULL, created_at TEXT NOT NULL
);
CREATE TABLE events (
    sequence INTEGER PRIMARY KEY AUTOINCREMENT, course_id TEXT NOT NULL REFERENCES courses(id),
    type TEXT NOT NULL, payload TEXT NOT NULL, created_at TEXT NOT NULL
);
CREATE INDEX event_course ON events(course_id, sequence);
