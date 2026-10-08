import hashlib
import json
import os
import re
import subprocess
import sys
import threading
from pathlib import Path

from .errors import DomainError
from .schemas import new_id

SUPPORTED = {".pdf", ".md", ".txt", ".csv", ".json", ".docx", ".pptx", ".png", ".jpg", ".jpeg", ".webp"}
IMAGES = {".png", ".jpg", ".jpeg", ".webp"}
KINDS = {"lecture", "tutorial", "syllabus", "reference", "student_notes", "textbook", "practice", "lab"}
# Sources up to this many pages are read page by page from images; larger ones are indexed, not read.
READ_MAX_PAGES = 80
SIGNATURES = {
    ".png": (b"\x89PNG",),
    ".jpg": (b"\xff\xd8\xff",),
    ".jpeg": (b"\xff\xd8\xff",),
    ".webp": (b"RIFF",),
}


def infer_week(filename):
    """Week numbers named in a filename, e.g. "Week 3", "W03", "week4"."""
    match = re.search(
        r"(?:week|wk)[\s_-]*0?(\d{1,2})\b|(?:^|[^A-Za-z0-9])W0?(\d{1,2})(?=[_\s.-])", filename, re.IGNORECASE
    )
    if match:
        week = int(match.group(1) or match.group(2))
        return week if 1 <= week <= 60 else None
    return None


class SourceService:
    def start_ingestion(self):
        self._stop = threading.Event()
        self._worker = threading.Thread(target=self._worker_loop, daemon=True, name="lecture-ingestion")
        self._worker.start()

    def stop_ingestion(self):
        self._stop.set()
        self._worker.join(timeout=40)

    def _worker_loop(self):
        # Only one process ingests a workspace at a time. OS releases the lock on crash.
        with (self.settings.data_dir / "ingestion.lock").open("a+b") as lock:
            lock.seek(0)
            lock.write(b"0")
            lock.flush()
            while not self._stop.is_set():
                try:
                    lock.seek(0)
                    if os.name == "nt":
                        import msvcrt

                        msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
                    else:
                        import fcntl

                        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    break
                except OSError:
                    self._stop.wait(0.5)
            else:
                return
            with self.db.transaction() as c:
                c.execute("UPDATE jobs SET status='queued' WHERE status='running'")
            while not self._stop.is_set():
                with self.db.connect() as c:
                    job = c.execute(
                        "SELECT * FROM jobs WHERE status='queued' ORDER BY created_at LIMIT 1"
                    ).fetchone()
                if job:
                    self._ingest(dict(job))
                else:
                    self._stop.wait(0.2)

    def upload_source(self, course_id, filename, content: bytes, kind="lecture", source_id=None, week=None):
        from .workspace import now

        if (
            not filename
            or len(filename) > 200
            or any(ord(ch) < 32 for ch in filename)
            or any(ch in filename for ch in "/\\:")
            or filename in {".", ".."}
        ):
            raise DomainError("invalid_filename", "Use a plain filename without path separators")
        suffix = Path(filename).suffix.lower()
        if suffix not in SUPPORTED:
            raise DomainError("unsupported_format", f"Supported formats: {', '.join(sorted(SUPPORTED))}", 415)
        if kind not in KINDS:
            raise DomainError("invalid_source_kind", "Unsupported source kind")
        if not content or len(content) > self.settings.max_upload_bytes:
            raise DomainError("upload_size", "Source is empty or exceeds the upload limit", 413)
        if suffix == ".pdf" and not content.startswith(b"%PDF-"):
            raise DomainError("invalid_file", "PDF signature is missing")
        if suffix in IMAGES and not content.startswith(SIGNATURES[suffix]):
            raise DomainError("invalid_file", "Image signature does not match its extension")
        if suffix in {".docx", ".pptx"} and not content.startswith(b"PK"):
            raise DomainError("invalid_file", "Office files must be valid ZIP containers")
        if suffix in {".txt", ".md", ".csv", ".json"}:
            try:
                decoded = content.decode("utf-8-sig")
                if "\x00" in decoded:
                    raise ValueError("NUL byte")
                if suffix == ".json":
                    json.loads(decoded)
            except (ValueError, RecursionError) as error:
                raise DomainError(
                    "invalid_file", "Text sources require valid UTF-8; JSON must parse"
                ) from error
        digest = hashlib.sha256(content).hexdigest()
        with self.db.transaction() as c:
            self.require(c, "courses", course_id)
            pending = c.execute("SELECT count(*) FROM jobs WHERE status IN ('queued','running')").fetchone()[
                0
            ]
            if pending >= 100:
                raise DomainError("queue_full", "Wait for pending source jobs to finish", 429)
            if source_id:
                source = self.require(c, "sources", source_id, course_id)
                if Path(source["filename"]).suffix.lower() != suffix:
                    raise DomainError("format_changed", "A source update must preserve its file format")
                same = c.execute(
                    "SELECT * FROM source_versions WHERE source_id=? AND version=? AND hash=?",
                    (source_id, source["current_version"], digest),
                ).fetchone()
                version = source["current_version"] + 1
            else:
                same = c.execute(
                    "SELECT v.* FROM source_versions v JOIN sources s ON s.id=v.source_id "
                    "WHERE s.course_id=? AND s.current_version=v.version AND v.hash=? LIMIT 1",
                    (course_id, digest),
                ).fetchone()
                version = 1
            if same:
                job = c.execute(
                    "SELECT id FROM jobs WHERE source_id=? AND version=?",
                    (same["source_id"], same["version"]),
                ).fetchone()
                return {
                    "source_id": same["source_id"],
                    "version": same["version"],
                    "job_id": job["id"],
                    "status": same["status"],
                    "duplicate": True,
                }
            timestamp, job_id = now(), new_id()
            source_id = source_id or new_id()
            storage_key = new_id() + suffix
            directory = self.settings.data_dir / "sources"
            directory.mkdir(exist_ok=True)
            (directory / storage_key).write_bytes(content)
            if version == 1:
                c.execute(
                    "INSERT INTO sources (id,course_id,filename,kind,current_version,created_at,week) "
                    "VALUES (?,?,?,?,?,?,?)",
                    (source_id, course_id, filename, kind, version, timestamp, week or infer_week(filename)),
                )
            else:
                c.execute(
                    "UPDATE sources SET current_version=?,filename=? WHERE id=?",
                    (version, filename, source_id),
                )
            c.execute(
                "INSERT INTO source_versions (source_id,version,hash,storage_key,status,error,created_at) "
                "VALUES (?,?,?,?,?,?,?)",
                (source_id, version, digest, storage_key, "queued", None, timestamp),
            )
            c.execute(
                "INSERT INTO jobs VALUES (?,?,?,?,?,?,?,?,?)",
                (
                    job_id,
                    course_id,
                    "source.ingestion",
                    source_id,
                    version,
                    "queued",
                    None,
                    timestamp,
                    timestamp,
                ),
            )
            self.event(
                c,
                course_id,
                "source.ingestion_queued",
                {"source_id": source_id, "version": version, "job_id": job_id},
            )
        return {
            "source_id": source_id,
            "version": version,
            "job_id": job_id,
            "status": "queued",
            "duplicate": False,
        }

    def _ingest(self, job):
        from .workspace import now

        try:
            with self.db.transaction() as c:
                record = c.execute(
                    "SELECT * FROM source_versions WHERE source_id=? AND version=?",
                    (job["source_id"], job["version"]),
                ).fetchone()
                c.execute("UPDATE jobs SET status='running',updated_at=? WHERE id=?", (now(), job["id"]))
                c.execute(
                    "UPDATE source_versions SET status='running' WHERE source_id=? AND version=?",
                    (job["source_id"], job["version"]),
                )
                self.event(c, job["course_id"], "source.ingestion_started", {"job_id": job["id"]})
                kind = c.execute("SELECT kind FROM sources WHERE id=?", (job["source_id"],)).fetchone()[0]
            path = self.settings.data_dir / "sources" / record["storage_key"]
            textbook = kind == "textbook"
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "open_lecture.extract",
                    str(path.resolve()),
                    str(self.settings.max_extracted_chars),
                    *(["--textbook"] if textbook else []),
                ],
                stdin=subprocess.DEVNULL,
                capture_output=True,
                timeout=300 if textbook else 90,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0,
            )
            if result.returncode:
                raise ValueError(result.stderr.decode("utf-8", errors="replace")[-1000:])
            extracted = json.loads(result.stdout)
            passages, page_count = extracted["chunks"], extracted["page_count"]
            paged = path.suffix.lower() == ".pdf" or path.suffix.lower() in IMAGES
            if not passages and not paged:
                raise ValueError("No extractable text in this file")
            with self.db.transaction() as c:
                for passage in passages:
                    chunk_id = new_id()
                    c.execute(
                        "INSERT INTO chunks VALUES (?,?,?,?,?,?,?,?)",
                        (
                            chunk_id,
                            job["course_id"],
                            job["source_id"],
                            job["version"],
                            passage["page"],
                            passage["section"],
                            passage["text"],
                            passage["method"],
                        ),
                    )
                    c.execute("INSERT INTO source_fts VALUES (?,?)", (chunk_id, passage["text"]))
                c.execute(
                    "UPDATE source_versions SET status='ready',error=NULL,page_count=? "
                    "WHERE source_id=? AND version=?",
                    (page_count, job["source_id"], job["version"]),
                )
                if extracted.get("textbook"):
                    self._store_textbook_index(c, job, extracted["textbook"])
                if paged and not textbook:
                    # Page images are read by an AI into hidden per-page notes (see reading.py).
                    within = page_count and page_count <= READ_MAX_PAGES
                    c.execute(
                        "INSERT INTO source_digests VALUES (?,?,?,?,?,?,?,?,?) ON CONFLICT DO NOTHING",
                        (
                            job["source_id"],
                            job["version"],
                            job["course_id"],
                            "pending" if within else "skipped",
                            page_count or 0,
                            0,
                            None,
                            None if within else f"Over {READ_MAX_PAGES} pages; indexed as text only",
                            now(),
                        ),
                    )
                c.execute(
                    "UPDATE jobs SET status='completed',error=NULL,updated_at=? WHERE id=?",
                    (now(), job["id"]),
                )
                self.event(
                    c,
                    job["course_id"],
                    "source.ingestion_completed",
                    {
                        "job_id": job["id"],
                        "source_id": job["source_id"],
                        "version": job["version"],
                        "chunks": len(passages),
                    },
                )
        except Exception as error:
            message = str(error)[:1000]
            with self.db.transaction() as c:
                c.execute(
                    "UPDATE source_versions SET status='failed',error=? WHERE source_id=? AND version=?",
                    (message, job["source_id"], job["version"]),
                )
                c.execute(
                    "UPDATE jobs SET status='failed',error=?,updated_at=? WHERE id=?",
                    (message, now(), job["id"]),
                )
                self.event(c, job["course_id"], "job.failed", {"job_id": job["id"], "error": message})

    def list_sources(self, course_id, limit=50, offset=0):
        with self.db.connect() as c:
            self.require(c, "courses", course_id)
            return [
                dict(row)
                for row in c.execute(
                    "SELECT s.*,v.status,v.error,v.hash,v.page_count,d.status AS reading_status,"
                    "d.pages_done AS reading_pages_done,d.pages_total AS reading_pages_total "
                    "FROM sources s JOIN source_versions v "
                    "ON v.source_id=s.id AND v.version=s.current_version "
                    "LEFT JOIN source_digests d ON d.source_id=s.id AND d.version=s.current_version "
                    "WHERE s.course_id=? ORDER BY coalesce(s.week, 99),s.created_at,s.id LIMIT ? OFFSET ?",
                    (course_id, limit, offset),
                )
            ]

    def source_file(self, course_id, source_id, version=None):
        with self.db.connect() as c:
            source = self.require(c, "sources", source_id, course_id)
            row = c.execute(
                "SELECT * FROM source_versions WHERE source_id=? AND version=?",
                (source_id, version or source["current_version"]),
            ).fetchone()
            if row is None:
                raise DomainError("not_found", "Source version not found", 404)
            return self.settings.data_dir / "sources" / row["storage_key"], source["filename"]

    def read_source(self, course_id, source_id, version=None, limit=50, offset=0):
        with self.db.connect() as c:
            source = self.require(c, "sources", source_id, course_id)
            version = version or source["current_version"]
            status = c.execute(
                "SELECT version,status,error,hash,page_count FROM source_versions WHERE source_id=? AND version=?",
                (source_id, version),
            ).fetchone()
            if status is None:
                raise DomainError("not_found", "Source version not found", 404)
            chunks = [
                dict(row)
                for row in c.execute(
                    "SELECT * FROM chunks WHERE source_id=? AND version=? ORDER BY rowid LIMIT ? OFFSET ?",
                    (source_id, version, limit, offset),
                )
            ]
            pages = (
                status["page_count"]
                or c.execute(
                    "SELECT MAX(page) FROM chunks WHERE source_id=? AND version=?", (source_id, version)
                ).fetchone()[0]
            )
            reading = c.execute(
                "SELECT status,error,pages_done,pages_total FROM source_digests WHERE source_id=? AND version=?",
                (source_id, version),
            ).fetchone()
            return (
                source
                | dict(status)
                | {
                    "chunks": chunks,
                    "pages": pages,
                    "reading_status": reading["status"] if reading else None,
                    "reading_error": reading["error"] if reading else None,
                    "reading_pages_done": reading["pages_done"] if reading else None,
                    "reading_pages_total": reading["pages_total"] if reading else None,
                    "trust": "untrusted_source_content",
                }
            )

    def render_source_page(self, course_id, source_id, page, version=None, size=1400, region=None):
        """PNG of one PDF page; `region` = [left, top, right, bottom] fractions crops (zooms) first."""
        args = [str(page), str(int(size))] + ([str(float(v)) for v in region] if region else [])
        return self._render(course_id, source_id, version, args)

    def render_source_thumbnails(self, course_id, source_id, first, count=12, version=None):
        """A labelled thumbnail sheet of up to 12 pages, for scanning a PDF for figures."""
        return self._render(
            course_id, source_id, version, ["--grid", str(first), str(min(max(count, 1), 12))]
        )

    def _render(self, course_id, source_id, version, args):
        path, filename = self.source_file(course_id, source_id, version)
        if path.suffix.lower() != ".pdf" and path.suffix.lower() not in IMAGES:
            raise DomainError("unsupported_preview", "Page previews are available for PDFs and images", 415)
        try:
            result = subprocess.run(
                [sys.executable, "-m", "open_lecture.render_page", str(path.resolve()), *args],
                stdin=subprocess.DEVNULL,
                capture_output=True,
                timeout=15,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0,
            )
        except subprocess.TimeoutExpired as error:
            raise DomainError("preview_timeout", "PDF page rendering exceeded 15 seconds", 422) from error
        if result.returncode:
            raise DomainError("preview_failed", result.stderr.decode("utf-8", errors="replace")[:500], 422)
        return result.stdout

    def search_sources(self, course_id, query, limit=10, include_textbook=False):
        tokens = re.findall(r"\w+", query, re.UNICODE)[:24]
        with self.db.connect() as c:
            self.require(c, "courses", course_id)
            if not tokens:
                return []
            expression = " OR ".join('"' + token + '"' for token in tokens)
            return [
                dict(row) | {"trust": "untrusted_source_content"}
                for row in c.execute(
                    "SELECT ch.*,s.filename,s.kind,bm25(source_fts) AS rank FROM source_fts "
                    "JOIN chunks ch ON ch.id=source_fts.chunk_id JOIN sources s ON s.id=ch.source_id "
                    "WHERE source_fts MATCH ? AND ch.course_id=? AND ch.version=s.current_version "
                    # Read sources answer from their AI page notes; textbooks only when asked.
                    "AND (s.kind!='textbook' OR ?) AND (ch.method IN ('ai_digest','ai_digest_pending') OR (NOT EXISTS ("
                    "SELECT 1 FROM chunks note WHERE note.source_id=ch.source_id AND note.version=ch.version "
                    "AND note.page=ch.page AND note.method IN ('ai_digest','ai_digest_pending')) AND NOT EXISTS ("
                    "SELECT 1 FROM source_digests d WHERE d.source_id=ch.source_id AND d.version=ch.version "
                    "AND d.status='ready'))) ORDER BY rank,ch.id LIMIT ?",
                    (expression, course_id, int(include_textbook), limit),
                )
            ]

    def get_job(self, course_id, job_id):
        with self.db.connect() as c:
            return self.require(c, "jobs", job_id, course_id)

    def retry_job(self, course_id, job_id):
        from .workspace import now

        with self.db.transaction() as c:
            job = self.require(c, "jobs", job_id, course_id)
            if job["status"] != "failed":
                raise DomainError("job_not_failed", "Only failed jobs can be retried", 409)
            c.execute("UPDATE jobs SET status='queued',error=NULL,updated_at=? WHERE id=?", (now(), job_id))
            c.execute(
                "UPDATE source_versions SET status='queued',error=NULL WHERE source_id=? AND version=?",
                (job["source_id"], job["version"]),
            )
            self.event(c, course_id, "source.ingestion_queued", {"job_id": job_id})
        return self.get_job(course_id, job_id)
