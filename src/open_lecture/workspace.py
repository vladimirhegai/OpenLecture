import hashlib
import json
import sqlite3
from datetime import datetime, timezone

from .chats import ChatService
from .config import Settings
from .db import Database
from .errors import DomainError
from .profiles import ProfileService
from .reading import ReadingStore
from .schemas import ActionRequest, DocumentCreate, DocumentEdit, new_id
from .sources import SourceService


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def encode(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


class Workspace(SourceService, ChatService, ProfileService, ReadingStore):
    def __init__(self, settings: Settings):
        self.settings = settings
        self.db = Database(settings.database)
        self.start_ingestion()

    def close(self):
        self.stop_ingestion()

    @staticmethod
    def require(connection, table: str, entity_id: str, course_id: str | None = None):
        allowed = {"courses", "folders", "documents", "sources", "chats", "artifacts", "jobs"}
        if table not in allowed:
            raise ValueError("Unknown table")
        row = connection.execute(f"SELECT * FROM {table} WHERE id=?", (str(entity_id),)).fetchone()
        if row is None or (course_id is not None and row["course_id"] != str(course_id)):
            raise DomainError("not_found", f"{table.rstrip('s')} not found", 404)
        return dict(row)

    @staticmethod
    def event(connection, course_id: str, event_type: str, payload: dict):
        connection.execute(
            "INSERT INTO events(course_id,type,payload,created_at) VALUES (?,?,?,?)",
            (course_id, event_type, encode(payload), now()),
        )

    def create_course(self, data):
        result = {"id": new_id(), **data.model_dump(), "created_at": now()}
        with self.db.transaction() as c:
            c.execute("INSERT INTO courses VALUES (:id,:code,:title,:created_at)", result)
            self.event(c, result["id"], "course.created", result)
        return result

    def list_courses(self, limit=50, offset=0):
        with self.db.connect() as c:
            return [
                dict(row)
                for row in c.execute(
                    "SELECT * FROM courses ORDER BY created_at,id LIMIT ? OFFSET ?", (limit, offset)
                )
            ]

    def get_course(self, course_id):
        with self.db.connect() as c:
            return self.require(c, "courses", course_id)

    def create_folder(self, course_id, data):
        result = {"id": new_id(), "course_id": course_id, **data.model_dump(mode="json")}
        with self.db.transaction() as c:
            self.require(c, "courses", course_id)
            if data.parent_id:
                self.require(c, "folders", str(data.parent_id), course_id)
            c.execute("INSERT INTO folders VALUES (:id,:course_id,:parent_id,:title)", result)
        return result

    def list_folders(self, course_id, limit=100, offset=0):
        with self.db.connect() as c:
            self.require(c, "courses", course_id)
            return [
                dict(row)
                for row in c.execute(
                    "SELECT * FROM folders WHERE course_id=? ORDER BY title,id LIMIT ? OFFSET ?",
                    (course_id, limit, offset),
                )
            ]

    @staticmethod
    def document_link(payload):
        return {key: payload[key] for key in ("document_id", "course_id", "revision", "title")} | {
            "route": f"/courses/{payload['course_id']}/docs/{payload['document_id']}"
        }

    def validate_references(self, c, course_id, blocks):
        for block in blocks:
            for citation in block.get("citations", []):
                row = c.execute(
                    "SELECT 1 FROM chunks WHERE id=? AND source_id=? AND version=? AND course_id=?",
                    (citation["chunk_id"], citation["source_id"], citation["version"], course_id),
                ).fetchone()
                if not row:
                    raise DomainError(
                        "invalid_citation", "Citation must reference a real course source chunk"
                    )
            if block["type"] == "artifact_reference":
                self.require(c, "artifacts", block["artifact_id"], course_id)

    @staticmethod
    def identity(data):
        # A week identifies a complete set of notes; topic subsets are discovery metadata.
        subject = (
            f"week:{data.academic_week}"
            if data.academic_week
            else (
                "topics:" + ",".join(data.topic_keys) if data.topic_keys else "title:" + data.title.casefold()
            )
        )
        return f"{data.document_type}:{subject}"

    def create_document(self, course_id: str, data: DocumentCreate):
        raw = data.model_dump(mode="json")
        # Generated default IDs must not invalidate retries of the same user request.
        fingerprint = data.model_dump(mode="json", exclude_unset=True)
        request_hash = hashlib.sha256(encode(fingerprint).encode()).hexdigest()
        with self.db.transaction() as c:
            self.require(c, "courses", course_id)
            if data.idempotency_key:
                prior = c.execute(
                    "SELECT * FROM idempotency WHERE course_id=? AND key=?", (course_id, data.idempotency_key)
                ).fetchone()
                if prior:
                    if prior["request_hash"] != request_hash:
                        raise DomainError(
                            "idempotency_conflict", "This retry key was used for a different request", 409
                        )
                    saved = self.require(c, "documents", prior["document_id"], course_id)
                    return {"created": False, "document": self.decorate_document(c, saved)}
            if data.folder_id:
                self.require(c, "folders", str(data.folder_id), course_id)
            identity = self.identity(data)
            if data.separate_copy:
                identity += ":copy:" + new_id()
            existing = c.execute(
                "SELECT * FROM documents WHERE course_id=? AND identity_key=? AND deleted=0",
                (course_id, identity),
            ).fetchone()
            if existing:
                raise DomainError(
                    "document_exists",
                    "Equivalent notes already exist; read or edit them",
                    409,
                    self.document_link(json.loads(existing["payload"])),
                )
            self.validate_references(c, course_id, raw["blocks"])
            timestamp = now()
            payload = {k: v for k, v in raw.items() if k not in ("separate_copy", "idempotency_key", "actor")}
            payload |= {
                "document_id": new_id(),
                "course_id": course_id,
                "revision": 1,
                "created_at": timestamp,
                "updated_at": timestamp,
                "deleted": False,
            }
            c.execute(
                "INSERT INTO documents VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    payload["document_id"],
                    course_id,
                    raw["folder_id"],
                    data.title,
                    data.document_type,
                    data.academic_week,
                    encode(data.topic_keys),
                    identity,
                    1,
                    0,
                    encode(payload),
                    timestamp,
                    timestamp,
                ),
            )
            self.save_revision(c, payload, data.actor)
            if data.idempotency_key:
                c.execute(
                    "INSERT INTO idempotency VALUES (?,?,?,?)",
                    (course_id, data.idempotency_key, request_hash, payload["document_id"]),
                )
            self.event(c, course_id, "document.created", self.document_link(payload))
            return {
                "created": True,
                "document": payload
                | {"reference": self.document_link(payload), "potentially_outdated": False},
            }

    @staticmethod
    def save_revision(c, payload, actor):
        c.execute(
            "INSERT INTO document_revisions VALUES (?,?,?,?,?)",
            (payload["document_id"], payload["revision"], encode(payload), actor, now()),
        )

    def decorate_document(self, c, row):
        payload = json.loads(row["payload"])
        stale = []
        for block in payload["blocks"]:
            for citation in block.get("citations", []):
                source = self.require(c, "sources", citation["source_id"], payload["course_id"])
                if source["current_version"] > citation["version"]:
                    stale.append(citation["source_id"])
        return payload | {
            "reference": self.document_link(payload),
            "potentially_outdated": bool(stale),
            "outdated_source_ids": sorted(set(stale)),
        }

    def read_document(self, course_id, document_id, revision=None):
        with self.db.connect() as c:
            row = self.require(c, "documents", document_id, course_id)
            if revision is not None:
                record = c.execute(
                    "SELECT payload FROM document_revisions WHERE document_id=? AND revision=?",
                    (document_id, revision),
                ).fetchone()
                if not record:
                    raise DomainError("not_found", "Revision not found", 404)
                row["payload"] = record["payload"]
            return self.decorate_document(c, row)

    def find_documents(
        self,
        course_id,
        query="",
        academic_week=None,
        document_type=None,
        topic=None,
        include_deleted=False,
        limit=50,
        offset=0,
    ):
        with self.db.connect() as c:
            self.require(c, "courses", course_id)
            clauses, args = ["course_id=?"], [course_id]
            if not include_deleted:
                clauses.append("deleted=0")
            if academic_week is not None:
                clauses.append("academic_week=?")
                args.append(academic_week)
            if document_type:
                clauses.append("document_type=?")
                args.append(document_type)
            if topic:
                clauses.append("EXISTS(SELECT 1 FROM json_each(documents.topic_keys) WHERE value=?)")
                args.append(topic)
            if query:
                clauses.append("(instr(lower(title),lower(?))>0 OR instr(lower(topic_keys),lower(?))>0)")
                args.extend([query, query])
            rows = c.execute(
                "SELECT * FROM documents WHERE "
                + " AND ".join(clauses)
                + " ORDER BY updated_at DESC,id LIMIT ? OFFSET ?",
                [*args, limit, offset],
            )
            return [
                {k: v for k, v in self.decorate_document(c, row).items() if k != "blocks"} for row in rows
            ]

    @staticmethod
    def check_revision(row, expected):
        if row["revision"] != expected:
            raise DomainError(
                "revision_conflict",
                "The document has changed; read it before retrying",
                409,
                {"expected_revision": expected, "current_revision": row["revision"]},
            )

    def edit_document(self, course_id, document_id, data: DocumentEdit):
        with self.db.transaction() as c:
            row = self.require(c, "documents", document_id, course_id)
            self.check_revision(row, data.expected_revision)
            if row["deleted"]:
                raise DomainError("document_deleted", "Restore the document before editing", 409)
            payload = json.loads(row["payload"])
            if data.title is not None:
                payload["title"] = data.title
            if "folder_id" in data.model_fields_set:
                if data.folder_id:
                    self.require(c, "folders", str(data.folder_id), course_id)
                payload["folder_id"] = str(data.folder_id) if data.folder_id else None
            blocks = payload["blocks"]
            for op in data.operations:
                positions = {b["id"]: i for i, b in enumerate(blocks)}
                block_id = str(op.block_id) if op.block_id else None
                after_id = str(op.after_id) if op.after_id else None
                if op.op != "insert" and block_id not in positions:
                    raise DomainError("block_not_found", "Target block does not exist", 404)
                if after_id is not None and after_id not in positions:
                    raise DomainError("block_not_found", "Insertion anchor does not exist", 404)
                if op.op == "replace":
                    blocks[positions[block_id]] = op.block.model_dump(mode="json")
                elif op.op == "remove":
                    blocks.pop(positions[block_id])
                else:
                    if op.op == "move":
                        if block_id == after_id:
                            raise DomainError("invalid_move", "A block cannot be moved after itself")
                        block = blocks.pop(positions[block_id])
                    else:
                        block = op.block.model_dump(mode="json")
                        if block["id"] in positions:
                            raise DomainError("duplicate_block", "Block ID already exists", 409)
                    insertion = next((i + 1 for i, b in enumerate(blocks) if b["id"] == after_id), 0)
                    blocks.insert(insertion, block)
            if len(blocks) > 500:
                raise DomainError("document_too_large", "Documents support at most 500 blocks")
            self.validate_references(c, course_id, blocks)
            payload["revision"] += 1
            payload["updated_at"] = now()
            c.execute(
                "UPDATE documents SET title=?,folder_id=?,revision=?,payload=?,updated_at=? WHERE id=?",
                (
                    payload["title"],
                    payload["folder_id"],
                    payload["revision"],
                    encode(payload),
                    now(),
                    document_id,
                ),
            )
            self.save_revision(c, payload, data.actor)
            self.event(c, course_id, "document.updated", self.document_link(payload))
            return self.decorate_document(c, {"payload": encode(payload)})

    def set_document_deleted(self, course_id, document_id, request, deleted):
        with self.db.transaction() as c:
            row = self.require(c, "documents", document_id, course_id)
            self.check_revision(row, request.expected_revision)
            payload = json.loads(row["payload"])
            if bool(row["deleted"]) == deleted:
                return self.decorate_document(c, row)
            payload |= {"deleted": deleted, "revision": payload["revision"] + 1, "updated_at": now()}
            try:
                c.execute(
                    "UPDATE documents SET deleted=?,revision=?,payload=?,updated_at=? WHERE id=?",
                    (int(deleted), payload["revision"], encode(payload), now(), document_id),
                )
            except sqlite3.IntegrityError as error:
                raise DomainError(
                    "document_exists", "An equivalent active document prevents restore", 409
                ) from error
            self.save_revision(c, payload, request.actor)
            self.event(
                c,
                course_id,
                "document.deleted" if deleted else "document.restored",
                self.document_link(payload),
            )
            return self.decorate_document(c, {"payload": encode(payload)})

    def list_revisions(self, course_id, document_id, limit=50, offset=0):
        with self.db.connect() as c:
            self.require(c, "documents", document_id, course_id)
            return [
                dict(row)
                for row in c.execute(
                    "SELECT revision,actor,created_at FROM document_revisions WHERE document_id=? "
                    "ORDER BY revision DESC LIMIT ? OFFSET ?",
                    (document_id, limit, offset),
                )
            ]

    def plan_document_action(self, course_id, data: ActionRequest):
        self.get_course(course_id)
        if data.intent == "question":
            return {
                "action": "answer_in_chat",
                "targets": [],
                "reason": "A question does not authorize note edits",
            }
        if data.intent == "edit":
            if not data.target_document_id:
                return {
                    "action": "ask_for_clarification",
                    "targets": [],
                    "reason": "Select the document to edit",
                }
            doc = self.read_document(course_id, str(data.target_document_id))
            if doc["deleted"]:
                raise DomainError("document_deleted", "Restore the document before editing", 409)
            return {
                "action": "update_document",
                "targets": [doc["reference"]],
                "reason": "Explicit edit intent",
            }
        matches = self.find_documents(
            course_id, academic_week=data.academic_week, document_type=data.document_type
        )
        if data.academic_week is None:
            matches = [d for d in matches if set(data.topic_keys) & set(d["topic_keys"])]
        if data.intent == "separate":
            action, reason = "create_related_document", "An independent document was explicitly requested"
        elif matches:
            action, reason = "reuse_document", "Existing notes match the requested week or topics"
        else:
            action, reason = "create_document", "No catalog match; content creation is authorized"
        return {"action": action, "targets": [d["reference"] for d in matches], "reason": reason}

    def save_artifact(self, course_id, kind, title, payload):
        artifact = {
            "id": new_id(),
            "course_id": course_id,
            "kind": kind,
            "title": title,
            "payload": payload,
            "created_at": now(),
        }
        with self.db.transaction() as c:
            self.require(c, "courses", course_id)
            c.execute(
                "INSERT INTO artifacts VALUES (?,?,?,?,?,?)",
                (artifact["id"], course_id, kind, title, encode(payload), artifact["created_at"]),
            )
            self.event(c, course_id, "artifact.created", {"artifact_id": artifact["id"], "kind": kind})
        return artifact

    def get_artifact(self, course_id, artifact_id):
        with self.db.connect() as c:
            row = self.require(c, "artifacts", artifact_id, course_id)
            return row | {"payload": json.loads(row["payload"])}

    def list_artifacts(self, course_id, limit=50, offset=0):
        with self.db.connect() as c:
            self.require(c, "courses", course_id)
            return [
                dict(row)
                for row in c.execute(
                    "SELECT id,course_id,kind,title,created_at FROM artifacts WHERE course_id=? "
                    "ORDER BY created_at DESC,id LIMIT ? OFFSET ?",
                    (course_id, limit, offset),
                )
            ]

    def events(self, course_id, after=0, limit=100):
        with self.db.connect() as c:
            self.require(c, "courses", course_id)
            return [
                dict(row) | {"payload": json.loads(row["payload"])}
                for row in c.execute(
                    "SELECT * FROM events WHERE course_id=? AND sequence>? ORDER BY sequence LIMIT ?",
                    (course_id, after, limit),
                )
            ]
