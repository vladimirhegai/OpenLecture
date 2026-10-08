"""Hidden AI source notes, the textbook problem index, app settings, and background agent task records.

Every paged source (PDF or image) up to READ_MAX_PAGES is read page by page from page images by an
AI model. Each page's note is stored as an ``ai_digest`` chunk on that page, so search, citations and
chat context use the note instead of raw PDF text. Textbooks are not read; their table of contents and
numbered problems are indexed so agents can fetch only the problem pages they need.
"""

import json
import re
from importlib.resources import files

from .errors import DomainError
from .schemas import new_id

DEFAULT_READING_MODEL = {"provider": "codex", "model": "gpt-6-luna", "effort": "high"}
DIGEST_METHOD = "ai_digest"
PENDING_DIGEST_METHOD = "ai_digest_pending"


def skill(name: str) -> str:
    return (files("open_lecture.skills") / f"{name}.md").read_text(encoding="utf-8")


def list_skills() -> list[dict]:
    result = []
    for path in sorted(files("open_lecture.skills").iterdir(), key=lambda p: p.name):
        if path.name.endswith(".md"):
            text = path.read_text(encoding="utf-8")
            summary = next((line.strip() for line in text.splitlines()[1:] if line.strip()), "")
            result.append({"name": path.name[:-3], "summary": summary})
    return result


def parse_pages(text: str) -> dict[int, str]:
    """Split a reading response into ``## Page N`` sections."""
    pages = {}
    parts = re.split(r"(?m)^#{1,3}\s*Page\s+(\d+)\s*$", text)
    for index in range(1, len(parts) - 1, 2):
        body = parts[index + 1].strip()
        if body:
            pages[int(parts[index])] = body
    return pages


class ReadingStore:
    # ---------------- Textbook index ----------------

    def _store_textbook_index(self, c, job, index):
        course, source, version = job["course_id"], job["source_id"], job["version"]
        c.execute("DELETE FROM textbook_sections WHERE source_id=? AND version=?", (source, version))
        for section in index["sections"]:
            c.execute(
                "INSERT INTO textbook_sections VALUES (?,?,?,?,?,?,?,?,?)",
                (
                    new_id(),
                    course,
                    source,
                    version,
                    section["level"],
                    section["chapter"],
                    section["title"],
                    section["start_page"],
                    section["end_page"],
                ),
            )
        for problem in index["problems"]:
            problem_id = new_id()
            c.execute(
                "INSERT INTO textbook_problems VALUES (?,?,?,?,?,?,?,?,?,?)",
                (
                    problem_id,
                    course,
                    source,
                    version,
                    problem["chapter"],
                    problem["number"],
                    problem["kind"],
                    problem["section"],
                    problem["page"],
                    problem["text"],
                ),
            )
            c.execute(
                "INSERT INTO textbook_problem_fts VALUES (?,?)",
                (problem_id, f"{problem['number']} {problem['section'] or ''} {problem['text']}"),
            )

    def _textbooks(self, c, course_id):
        return list(
            c.execute(
                "SELECT s.id,s.filename,s.current_version AS version FROM sources s "
                "JOIN source_versions v ON v.source_id=s.id AND v.version=s.current_version "
                "WHERE s.course_id=? AND s.kind='textbook' AND v.status='ready' ORDER BY s.created_at",
                (course_id,),
            )
        )

    def textbook_outline(self, course_id, chapter=None):
        with self.db.connect() as c:
            self.require(c, "courses", course_id)
            books = []
            for book in self._textbooks(c, course_id):
                query = (
                    "SELECT level,chapter,title,start_page,end_page FROM textbook_sections "
                    "WHERE source_id=? AND version=? AND level<=2"
                )
                args = [book["id"], book["version"]]
                if chapter is not None:
                    query += " AND chapter=?"
                    args.append(chapter)
                sections = [dict(row) for row in c.execute(query + " ORDER BY start_page,level", args)]
                if chapter is None:
                    sections = [s for s in sections if s["level"] == 1]
                books.append({"source_id": book["id"], "filename": book["filename"], "sections": sections})
            return books

    def textbook_problems(self, course_id, chapter=None, section=None, query=None, limit=20):
        with self.db.connect() as c:
            self.require(c, "courses", course_id)
            books = self._textbooks(c, course_id)
            if not books:
                return []
            clauses, args = ["p.course_id=?"], [course_id]
            clauses.append("(" + " OR ".join("(p.source_id=? AND p.version=?)" for _ in books) + ")")
            for book in books:
                args += [book["id"], book["version"]]
            if chapter is not None:
                clauses.append("p.chapter=?")
                args.append(chapter)
            if section:
                clauses.append("p.section LIKE ?")
                args.append(f"%{section}%")
            tokens = re.findall(r"\w+", query or "", re.UNICODE)[:16]
            if tokens:
                sql = (
                    "SELECT p.* FROM textbook_problem_fts f JOIN textbook_problems p ON p.id=f.problem_id "
                    f"WHERE textbook_problem_fts MATCH ? AND {' AND '.join(clauses)} "
                    "ORDER BY bm25(textbook_problem_fts) LIMIT ?"
                )
                rows = c.execute(sql, [" OR ".join(f'"{t}"' for t in tokens), *args, limit])
            else:
                sql = (
                    f"SELECT p.* FROM textbook_problems p WHERE {' AND '.join(clauses)} "
                    "ORDER BY p.chapter, CAST(substr(p.number, instr(p.number,'.')+1) AS INTEGER) LIMIT ?"
                )
                rows = c.execute(sql, [*args, limit])
            result = []
            for row in rows:
                chunk = c.execute(
                    "SELECT id FROM chunks WHERE source_id=? AND version=? AND page=? ORDER BY rowid LIMIT 1",
                    (row["source_id"], row["version"], row["page"]),
                ).fetchone()
                result.append(
                    {
                        "number": row["number"],
                        "chapter": row["chapter"],
                        "section": row["section"],
                        "page": row["page"],
                        "text_preview": row["text"][:420],
                        "citation": {
                            "source_id": row["source_id"],
                            "version": row["version"],
                            "chunk_id": chunk["id"] if chunk else None,
                        },
                        "trust": "untrusted_source_content",
                    }
                )
            return result

    # ---------------- Source reading (hidden page notes) ----------------

    def reading_status(self, course_id, source_id):
        with self.db.connect() as c:
            source = self.require(c, "sources", source_id, course_id)
            row = c.execute(
                "SELECT * FROM source_digests WHERE source_id=? AND version=?",
                (source_id, source["current_version"]),
            ).fetchone()
            return dict(row) if row else None

    def claim_pending_reading(self, model):
        """Atomically take the oldest pending reading so parallel readers never share a source."""
        from .workspace import now

        with self.db.transaction() as c:
            row = c.execute(
                "SELECT d.*,s.filename,s.kind,s.week FROM source_digests d JOIN sources s ON s.id=d.source_id "
                "WHERE d.status='pending' AND d.version=s.current_version ORDER BY d.updated_at LIMIT 1"
            ).fetchone()
            if row is None:
                return None
            c.execute(
                "UPDATE source_digests SET status='running',model=?,updated_at=? WHERE source_id=? AND version=?",
                (model, now(), row["source_id"], row["version"]),
            )
            self.event(
                c,
                row["course_id"],
                "source.reading_updated",
                {"source_id": row["source_id"], "status": "running"},
            )
            return dict(row)

    def update_reading(self, source_id, version, **fields):
        from .workspace import now

        assignments = ",".join(f"{key}=?" for key in fields)
        with self.db.transaction() as c:
            c.execute(
                f"UPDATE source_digests SET {assignments},updated_at=? WHERE source_id=? AND version=?",
                (*fields.values(), now(), source_id, version),
            )
            row = c.execute(
                "SELECT course_id,status,pages_done,pages_total FROM source_digests WHERE source_id=? AND version=?",
                (source_id, version),
            ).fetchone()
            if row:
                self.event(
                    c,
                    row["course_id"],
                    "source.reading_updated",
                    {"source_id": source_id, "version": version, **dict(row)},
                )

    def request_reading(self, course_id, source_id, pages=None):
        """Queue (re)reading of a source; ``pages`` limits it to those pages."""
        from .workspace import now

        with self.db.transaction() as c:
            source = self.require(c, "sources", source_id, course_id)
            version = source["current_version"]
            row = c.execute(
                "SELECT * FROM source_digests WHERE source_id=? AND version=?", (source_id, version)
            ).fetchone()
            if row is None:
                raise DomainError("not_readable", "Only PDF and image sources are read from page images", 409)
            if row["status"] == "running":
                raise DomainError("reading_running", "Wait for the current reading to finish", 409)
            targets = pages or list(range(1, row["pages_total"] + 1))
            if any(page < 1 or page > row["pages_total"] for page in targets):
                raise DomainError("invalid_page", f"Pages must be between 1 and {row['pages_total']}")
            for page in targets:
                # Keep the note and its citation ID readable until the replacement is saved.
                c.execute(
                    "UPDATE chunks SET method=? WHERE source_id=? AND version=? AND page=? AND method=?",
                    (PENDING_DIGEST_METHOD, source_id, version, page, DIGEST_METHOD),
                )
            done = self._pages_done(c, source_id, version)
            c.execute(
                "UPDATE source_digests SET status='pending',error=NULL,pages_done=?,updated_at=? "
                "WHERE source_id=? AND version=?",
                (done, now(), source_id, version),
            )
            self.event(c, course_id, "source.reading_updated", {"source_id": source_id, "status": "pending"})
        return self.reading_status(course_id, source_id)

    @staticmethod
    def _pages_done(c, source_id, version):
        return c.execute(
            "SELECT count(DISTINCT page) FROM chunks WHERE source_id=? AND version=? AND method=?",
            (source_id, version, DIGEST_METHOD),
        ).fetchone()[0]

    def pages_read(self, source_id, version):
        with self.db.connect() as c:
            return {
                row[0]
                for row in c.execute(
                    "SELECT DISTINCT page FROM chunks WHERE source_id=? AND version=? AND method=?",
                    (source_id, version, DIGEST_METHOD),
                )
            }

    def page_text(self, source_id, version, page):
        with self.db.connect() as c:
            return "\n".join(
                row[0]
                for row in c.execute(
                    "SELECT text FROM chunks WHERE source_id=? AND version=? AND page=? AND method NOT IN (?,?) "
                    "ORDER BY rowid",
                    (source_id, version, page, DIGEST_METHOD, PENDING_DIGEST_METHOD),
                )
            )

    def store_page_notes(self, course_id, source_id, version, notes: dict[int, str]):
        with self.db.transaction() as c:
            self.require(c, "sources", source_id, course_id)
            source_version = c.execute(
                "SELECT page_count FROM source_versions WHERE source_id=? AND version=?",
                (source_id, version),
            ).fetchone()
            if source_version is None:
                raise DomainError("not_found", "Source version not found", 404)
            for page, text in notes.items():
                if not 1 <= page <= (source_version["page_count"] or 0):
                    raise DomainError("invalid_page", "Page is outside the source")
                if not text.strip() or len(text) > 20000:
                    raise DomainError("invalid_page_note", "Page notes must contain 1–20000 characters")
                previous = c.execute(
                    "SELECT id FROM chunks WHERE source_id=? AND version=? AND page=? AND method IN (?,?)",
                    (source_id, version, page, DIGEST_METHOD, PENDING_DIGEST_METHOD),
                ).fetchone()
                chunk_id = previous["id"] if previous else new_id()
                if previous:
                    c.execute("DELETE FROM source_fts WHERE chunk_id=?", (chunk_id,))
                    c.execute("UPDATE chunks SET text=?,method=? WHERE id=?", (text, DIGEST_METHOD, chunk_id))
                else:
                    c.execute(
                        "INSERT INTO chunks VALUES (?,?,?,?,?,?,?,?)",
                        (
                            chunk_id,
                            course_id,
                            source_id,
                            version,
                            page,
                            f"Page {page}",
                            text,
                            DIGEST_METHOD,
                        ),
                    )
                c.execute("INSERT INTO source_fts VALUES (?,?)", (chunk_id, text))
            return self._pages_done(c, source_id, version)

    def source_notes(self, course_id, source_id, first_page=1, last_page=None, version=None):
        """The AI page notes for a source: the preferred way to read lecture and tutorial material."""
        with self.db.connect() as c:
            source = self.require(c, "sources", source_id, course_id)
            version = version or source["current_version"]
            rows = c.execute(
                "SELECT id,page,text FROM chunks WHERE source_id=? AND version=? AND method IN (?,?) "
                "AND page>=? AND page<=? ORDER BY page",
                (source_id, version, DIGEST_METHOD, PENDING_DIGEST_METHOD, first_page, last_page or 100000),
            ).fetchall()
            status = c.execute(
                "SELECT status,pages_total,pages_done FROM source_digests WHERE source_id=? AND version=?",
                (source_id, version),
            ).fetchone()
            return {
                "source_id": source_id,
                "filename": source["filename"],
                "version": version,
                "reading": dict(status) if status else None,
                "pages": [{"page": row["page"], "chunk_id": row["id"], "note": row["text"]} for row in rows],
                "citation_hint": "Cite {source_id, version, chunk_id} of the page you use.",
                "trust": "untrusted_source_content",
            }

    # ---------------- Settings ----------------

    def get_setting(self, key, default=None):
        with self.db.connect() as c:
            row = c.execute("SELECT value FROM app_settings WHERE key=?", (key,)).fetchone()
            return json.loads(row["value"]) if row else default

    def set_setting(self, key, value):
        with self.db.transaction() as c:
            c.execute(
                "INSERT INTO app_settings VALUES (?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value",
                (key, json.dumps(value)),
            )
        return value

    def reading_model(self):
        return self.get_setting("reading_model", DEFAULT_READING_MODEL)

    # ---------------- Background agent tasks ----------------

    def create_task(self, course_id, kind, title, params):
        from .workspace import encode, now

        task_id, timestamp = new_id(), now()
        with self.db.transaction() as c:
            self.require(c, "courses", course_id)
            c.execute(
                "INSERT INTO agent_tasks VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                (
                    task_id,
                    course_id,
                    kind,
                    title,
                    "queued",
                    encode(params),
                    "[]",
                    None,
                    None,
                    timestamp,
                    timestamp,
                ),
            )
            self.event(c, course_id, "task.updated", {"task_id": task_id, "status": "queued", "kind": kind})
        return self.get_task(course_id, task_id)

    def update_task(self, task_id, **fields):
        from .workspace import encode, now

        values = {k: encode(v) if k in {"log", "result", "params"} else v for k, v in fields.items()}
        assignments = ",".join(f"{key}=?" for key in values)
        with self.db.transaction() as c:
            c.execute(
                f"UPDATE agent_tasks SET {assignments},updated_at=? WHERE id=?",
                (*values.values(), now(), task_id),
            )
            row = c.execute("SELECT course_id,status,kind FROM agent_tasks WHERE id=?", (task_id,)).fetchone()
            if row and "status" in fields:
                self.event(
                    c,
                    row["course_id"],
                    "task.updated",
                    {"task_id": task_id, "status": row["status"], "kind": row["kind"]},
                )

    @staticmethod
    def _task(row):
        task = dict(row)
        task["params"] = json.loads(task["params"])
        task["log"] = json.loads(task["log"])
        task["result"] = json.loads(task["result"]) if task["result"] else None
        return task

    def get_task(self, course_id, task_id):
        with self.db.connect() as c:
            row = c.execute(
                "SELECT * FROM agent_tasks WHERE id=? AND course_id=?", (task_id, course_id)
            ).fetchone()
            if row is None:
                raise DomainError("not_found", "Task not found", 404)
            return self._task(row)

    def list_tasks(self, course_id, active=False, limit=30):
        with self.db.connect() as c:
            self.require(c, "courses", course_id)
            query = "SELECT * FROM agent_tasks WHERE course_id=?"
            if active:
                query += " AND status IN ('queued','running')"
            rows = c.execute(query + " ORDER BY created_at DESC LIMIT ?", (course_id, limit))
            return [self._task(row) for row in rows]

    def backfill_readings(self):
        """Queue reading for paged sources ingested before page reading existed."""
        from .sources import IMAGES, READ_MAX_PAGES
        from .workspace import now

        with self.db.transaction() as c:
            rows = c.execute(
                "SELECT s.id,s.course_id,s.filename,s.kind,v.version,v.page_count FROM sources s "
                "JOIN source_versions v ON v.source_id=s.id AND v.version=s.current_version "
                "LEFT JOIN source_digests d ON d.source_id=s.id AND d.version=v.version "
                "WHERE v.status='ready' AND d.source_id IS NULL AND s.kind!='textbook'"
            ).fetchall()
            for row in rows:
                suffix = "." + row["filename"].rsplit(".", 1)[-1].lower()
                if suffix != ".pdf" and suffix not in IMAGES:
                    continue
                pages = (
                    row["page_count"]
                    or c.execute(
                        "SELECT MAX(page) FROM chunks WHERE source_id=? AND version=?",
                        (row["id"], row["version"]),
                    ).fetchone()[0]
                )
                if not pages:
                    continue
                c.execute(
                    "UPDATE source_versions SET page_count=? WHERE source_id=? AND version=?",
                    (pages, row["id"], row["version"]),
                )
                within = pages <= READ_MAX_PAGES
                c.execute(
                    "INSERT INTO source_digests VALUES (?,?,?,?,?,?,?,?,?)",
                    (
                        row["id"],
                        row["version"],
                        row["course_id"],
                        "pending" if within else "skipped",
                        pages,
                        0,
                        None,
                        None if within else f"Over {READ_MAX_PAGES} pages; indexed as text only",
                        now(),
                    ),
                )

    def interrupt_stale_tasks(self):
        """Tasks and readings left running by a previous server process cannot resume mid-run."""
        from .workspace import now

        with self.db.transaction() as c:
            c.execute(
                "UPDATE agent_tasks SET status='failed',error='Interrupted by a server restart',updated_at=? "
                "WHERE status IN ('queued','running')",
                (now(),),
            )
            c.execute("UPDATE source_digests SET status='pending' WHERE status='running'")
