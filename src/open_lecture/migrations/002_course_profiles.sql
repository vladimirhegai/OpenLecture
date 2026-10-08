CREATE TABLE course_profiles (
    course_id TEXT PRIMARY KEY REFERENCES courses(id), revision INTEGER NOT NULL,
    payload TEXT NOT NULL, updated_at TEXT NOT NULL
);
