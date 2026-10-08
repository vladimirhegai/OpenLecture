from io import BytesIO

import pymupdf
import pytest
from conftest import wait_job
from docx import Document
from fastapi.testclient import TestClient
from pptx import Presentation

from open_lecture.api import create_app


@pytest.mark.parametrize("format", ["pdf", "docx", "pptx", "txt", "csv", "json"])
def test_real_file_parsers(client, course, format):
    text = "Kirchhoff current law conserves charge."
    if format == "pdf":
        with pymupdf.open() as document:
            document.new_page().insert_text((72, 72), text)
            content = document.tobytes()
    elif format == "docx":
        document = Document()
        document.add_heading("Week two", 1)
        document.add_paragraph(text)
        buffer = BytesIO()
        document.save(buffer)
        content = buffer.getvalue()
    elif format == "pptx":
        presentation = Presentation()
        slide = presentation.slides.add_slide(presentation.slide_layouts[1])
        slide.shapes.title.text = text
        buffer = BytesIO()
        presentation.save(buffer)
        content = buffer.getvalue()
    else:
        content = ('{"content":"' + text + '"}' if format == "json" else text).encode()
    base = f"/api/v1/courses/{course}"
    job = client.post(base + "/sources", files={"file": (f"lecture.{format}", content)}).json()
    assert wait_job(client, course, job["job_id"])["status"] == "completed"
    found = client.get(base + "/search", params={"query": "Kirchhoff"}).json()
    assert found and found[0]["source_id"] == job["source_id"]
    if format in {"pdf", "pptx"}:
        assert found[0]["page"] == 1
    duplicate = client.post(base + "/sources", files={"file": (f"lecture.{format}", content)}).json()
    assert duplicate["duplicate"] and duplicate["version"] == 1


def test_bad_files_and_failed_jobs(client, course):
    base = f"/api/v1/courses/{course}"
    for filename, data, status in [
        ("../../evil.txt", b"text", 400),
        ("run.exe", b"MZ", 415),
        ("empty.txt", b"", 413),
        ("fake.pdf", b"text", 400),
        ("binary.txt", b"\x00", 400),
        ("bad.json", b"{bad}", 400),
    ]:
        assert client.post(base + "/sources", files={"file": (filename, data)}).status_code == status
    job = client.post(base + "/sources", files={"file": ("corrupt.pdf", b"%PDF-invalid")}).json()
    failed = wait_job(client, course, job["job_id"])
    assert failed["status"] == "failed" and failed["error"]
    assert client.post(base + f"/jobs/{job['job_id']}/retry").status_code == 200
    assert wait_job(client, course, job["job_id"])["status"] == "failed"
    assert client.get(base + "/search", params={"query": '" OR NOT * ( --'}).status_code == 200
    with pymupdf.open() as pdf:
        pdf.new_page()
        empty = client.post(base + "/sources", files={"file": ("scan.pdf", pdf.tobytes())}).json()
    # Image-only PDFs are accepted and queued for AI reading from page images instead of failing.
    assert wait_job(client, course, empty["job_id"])["status"] == "completed"
    scan = client.get(base + f"/sources/{empty['source_id']}").json()
    assert scan["pages"] == 1 and scan["chunks"] == []
    listed = next(s for s in client.get(base + "/sources").json() if s["id"] == empty["source_id"])
    assert listed["reading_status"] == "pending" and listed["reading_pages_total"] == 1


def test_context_compaction_preserves_history_and_bounds(client, course):
    base = f"/api/v1/courses/{course}"
    chat_id = client.post(base + "/chats", json={"title": "Long session"}).json()["id"]
    chat = base + f"/chats/{chat_id}"
    for i in range(40):
        assert (
            client.post(
                chat + "/messages", json={"role": "user", "content": f"Question {i}: " + "resistor " * 100}
            ).status_code
            == 201
        )
    response = client.post(chat + "/context", json={"query": "Explain resistor power", "token_budget": 2000})
    assert response.status_code == 200
    context = response.json()
    assert context["estimated_input_tokens"] <= 1500
    assert len(client.get(chat + "/messages").json()) == 40
    assert client.get(chat + "/context").json()["id"] == context["id"]
    events = client.get(base + "/events", params={"follow": False}).text
    assert "context.compacted" in events
    assert client.post(chat + "/context", json={"query": "x" * 4000, "token_budget": 1000}).status_code == 400
    second = client.post(base + "/chats", json={"title": "Other chat"}).json()["id"]
    assert client.get(base + f"/chats/{second}/context").json() is None


def test_event_replay_and_origin_access(client, course, settings):
    base = f"/api/v1/courses/{course}"
    client.post(base + "/documents", json={"title": "First"})
    initial = client.get(base + "/events", params={"follow": False}).text
    event_ids = [int(line[4:]) for line in initial.splitlines() if line.startswith("id: ")]
    assert len(event_ids) == 2
    assert not client.get(
        base + "/events", params={"follow": False}, headers={"Last-Event-ID": str(event_ids[-1])}
    ).text
    client.post(base + "/documents", json={"title": "Second"})
    replay = client.get(
        base + "/events", params={"follow": False}, headers={"Last-Event-ID": str(event_ids[-1])}
    ).text
    assert replay.count("event: document.created") == 1
    assert (
        client.post(
            base + "/documents", json={"title": "Bad"}, headers={"Origin": "https://unrelated.example"}
        ).status_code
        == 403
    )
    assert client.get("/api/v1/courses", headers={"Host": "unrelated.example"}).status_code == 403
    secured = settings.model_copy(update={"api_token": "test-token"})
    with TestClient(create_app(secured)) as secure:
        assert secure.get("/api/v1/courses").status_code == 401
        assert (
            secure.get("/api/v1/courses", headers={"Authorization": "Bearer test-token"}).status_code == 200
        )
