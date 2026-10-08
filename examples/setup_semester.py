"""Import the user's four syllabi into their local workspace. Originals are never checked into Git."""

import argparse
import json
import time
from pathlib import Path

from open_lecture.config import Settings
from open_lecture.errors import DomainError
from open_lecture.schemas import CourseCreate, CourseProfileUpdate, DocumentCreate, FolderCreate
from open_lecture.workspace import Workspace


def setup(workspace: Workspace, syllabus_dir: Path, manifest: dict):
    # Validate all paths before creating anything.
    for item in manifest["courses"]:
        if not (syllabus_dir / item["filename"]).is_file():
            raise FileNotFoundError(item["filename"])
    results = []
    for item in manifest["courses"]:
        matches = [
            course
            for course in workspace.list_courses(limit=1000)
            if course["code"] == item["code"]
            and workspace.get_profile(course["id"])["term"] in {"", manifest["term"]}
        ]
        if len(matches) > 1:
            raise ValueError(f"Multiple courses match {item['code']}; resolve them before importing")
        course = (
            matches[0]
            if matches
            else workspace.create_course(CourseCreate(code=item["code"], title=item["title"]))
        )
        course_id = course["id"]
        folders = {folder["title"]: folder for folder in workspace.list_folders(course_id)}
        for title in ("Course information", "Study notes", "Practice"):
            if title not in folders:
                folders[title] = workspace.create_folder(course_id, FolderCreate(title=title))
        path = syllabus_dir / item["filename"]
        source = workspace.upload_source(course_id, path.name, path.read_bytes(), kind="syllabus")
        deadline = time.monotonic() + 40
        while time.monotonic() < deadline:
            job = workspace.get_job(course_id, source["job_id"])
            if job["status"] in {"completed", "failed"}:
                break
            time.sleep(0.1)
        if job["status"] != "completed":
            raise RuntimeError(f"{item['code']} syllabus ingestion: {job['status']}: {job['error']}")
        passages = workspace.read_source(course_id, source["source_id"], limit=200)["chunks"]
        citations = []
        for page in item["scope_pages"]:
            chunk = next(chunk for chunk in passages if chunk["page"] == page)
            citations.append(
                {"source_id": chunk["source_id"], "version": chunk["version"], "chunk_id": chunk["id"]}
            )
        current = workspace.get_profile(course_id)
        if current["revision"] == 0:
            workspace.update_profile(
                course_id,
                CourseProfileUpdate(
                    expected_revision=0,
                    term=manifest["term"],
                    pack_ids=item["pack_ids"],
                    topics=item["topics"],
                    syllabus_citations=citations,
                    study_preferences=[
                        "Explain the reasoning before substituting numbers.",
                        "Use meaningful diagrams, verified examples, and clearly labeled original practice.",
                    ],
                ),
            )
        try:
            doc = workspace.create_document(
                course_id,
                DocumentCreate.model_validate(
                    {
                        "title": f"{item['code']}: Course map",
                        "document_type": "reference",
                        "topic_keys": ["course_map"],
                        "folder_id": folders["Course information"]["id"],
                        "actor": "agent",
                        "blocks": [
                            {"type": "heading", "text": item["title"], "level": 1},
                            {
                                "type": "callout",
                                "text": "This map summarizes syllabus scope. Upload lectures and tutorials for detailed source-grounded notes and actual tutorial problems.",
                            },
                            {
                                "type": "list",
                                "items": [
                                    (f"Week {topic['week']}: " if topic.get("week") else "") + topic["title"]
                                    for topic in item["topics"]
                                ],
                                "citations": citations,
                            },
                            {
                                "type": "paragraph",
                                "text": "Study notes should include explanations, justified equations, useful diagrams, checked worked examples, original practice, and common mistakes. Course tools and limitations are listed in the study guidance.",
                            },
                        ],
                    }
                ),
            )["document"]
            document_id = doc["document_id"]
        except DomainError as error:
            if error.code != "document_exists":
                raise
            document_id = error.details["document_id"]
        results.append(
            {
                "course_id": course_id,
                "code": item["code"],
                "source_id": source["source_id"],
                "course_map_document_id": document_id,
                "course_packs": item["pack_ids"],
            }
        )
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--syllabus-dir", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, default=Path(__file__).with_name("queens_fall_2026.json"))
    args = parser.parse_args()
    workspace = Workspace(Settings())
    try:
        result = setup(workspace, args.syllabus_dir, json.loads(args.manifest.read_text(encoding="utf-8")))
        print(json.dumps(result, indent=2))
    finally:
        workspace.close()
