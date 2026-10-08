import sqlite3
from contextlib import contextmanager
from importlib.resources import files
from pathlib import Path


class Database:
    def __init__(self, path: Path):
        self.path = path
        path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as connection:
            connection.execute("PRAGMA journal_mode=WAL")
            connection.execute("CREATE TABLE IF NOT EXISTS schema_migrations (version TEXT PRIMARY KEY)")
        with self.transaction() as connection:
            for migration in sorted(files("open_lecture.migrations").iterdir(), key=lambda p: p.name):
                if migration.name.endswith(".sql"):
                    applied = connection.execute(
                        "SELECT 1 FROM schema_migrations WHERE version=?", (migration.name,)
                    ).fetchone()
                    if not applied:
                        # Keep the migration check and all DDL under the same cross-process write lock.
                        statement = ""
                        for line in migration.read_text(encoding="utf-8").splitlines(keepends=True):
                            statement += line
                            if sqlite3.complete_statement(statement):
                                connection.execute(statement)
                                statement = ""
                        if statement.strip():
                            raise ValueError(f"Incomplete migration: {migration.name}")
                        connection.execute("INSERT INTO schema_migrations VALUES (?)", (migration.name,))

    @contextmanager
    def connect(self):
        connection = sqlite3.connect(self.path, timeout=15)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys=ON")
        try:
            yield connection
        finally:
            connection.close()

    @contextmanager
    def transaction(self):
        with self.connect() as connection:
            connection.execute("BEGIN IMMEDIATE")
            try:
                yield connection
                connection.commit()
            except BaseException:
                connection.rollback()
                raise
