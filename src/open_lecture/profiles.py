import json
from importlib.resources import files

from .errors import DomainError

NOTE_RECIPE = [
    "Learning objectives and prerequisites",
    "Definitions, notation, and assumptions",
    "Concept explanations with cited course evidence",
    "Equations and justified derivations",
    "Useful diagrams or verified computational artifacts",
    "Worked examples with intermediate steps",
    "Source-derived practice only when actual question sources exist",
    "Clearly labeled original practice and collapsible solutions",
    "Common mistakes, limiting cases, and a retrieval-practice summary",
]


def list_packs():
    return [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(files("open_lecture.course_packs").iterdir(), key=lambda p: p.name)
        if path.name.endswith(".json")
    ]


class ProfileService:
    def get_profile(self, course_id):
        with self.db.connect() as c:
            self.require(c, "courses", course_id)
            row = c.execute("SELECT * FROM course_profiles WHERE course_id=?", (course_id,)).fetchone()
        return (
            (json.loads(row["payload"]) | {"revision": row["revision"], "course_id": course_id})
            if row
            else {
                "course_id": course_id,
                "revision": 0,
                "term": "",
                "pack_ids": [],
                "topics": [],
                "syllabus_citations": [],
                "study_preferences": [],
            }
        )

    def update_profile(self, course_id, data):
        from .workspace import encode, now

        available = {pack["id"] for pack in list_packs()}
        if set(data.pack_ids) - available:
            raise DomainError("unknown_course_pack", "Choose registered pack IDs from /api/v1/course-packs")
        payload = data.model_dump(mode="json", exclude={"expected_revision"})
        with self.db.transaction() as c:
            self.require(c, "courses", course_id)
            row = c.execute("SELECT * FROM course_profiles WHERE course_id=?", (course_id,)).fetchone()
            revision = row["revision"] if row else 0
            if revision != data.expected_revision:
                raise DomainError(
                    "revision_conflict",
                    "Course profile changed; read it before retrying",
                    409,
                    {"current_revision": revision},
                )
            self.validate_references(
                c, course_id, [{"type": "paragraph", "citations": payload["syllabus_citations"]}]
            )
            c.execute(
                "INSERT INTO course_profiles VALUES (?,?,?,?) ON CONFLICT(course_id) DO UPDATE SET "
                "revision=excluded.revision,payload=excluded.payload,updated_at=excluded.updated_at",
                (course_id, revision + 1, encode(payload), now()),
            )
            self.event(c, course_id, "course.profile_updated", {"revision": revision + 1})
        return payload | {"course_id": course_id, "revision": revision + 1}

    def study_guidance(self, course_id):
        profile = self.get_profile(course_id)
        return {
            "profile": profile,
            "note_recipe": NOTE_RECIPE,
            "course_packs": [pack for pack in list_packs() if pack["id"] in profile["pack_ids"]],
            "provenance_rule": "A syllabus establishes course scope, not detailed lecture coverage or tutorial questions.",
        }
