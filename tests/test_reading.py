import pymupdf
import pytest
from conftest import wait_job

from open_lecture import agents
from open_lecture.reading import parse_pages
from open_lecture.sources import infer_week


def test_parse_pages_splits_page_sections():
    text = "## Page 3\nKCL at node 1.\n\n## Page 4\n$$v=iR$$\n\n## Page 9\n"
    assert parse_pages(text) == {3: "KCL at node 1.", 4: "$$v=iR$$"}


def test_week_inferred_from_filenames():
    assert infer_week("ELEC 221 Week 1 Fall 2026 copy.pdf") == 1
    assert infer_week("ELEC221-F2026-Week5-Sec001.pdf") == 5
    assert infer_week("ELEC231_F2026_W02_Lecture_Notes.pdf") == 2
    assert infer_week("Chapter 4 Problems.pdf") is None


def test_codex_reading_command_attaches_images_and_keeps_tool_host(monkeypatch, tmp_path):
    monkeypatch.setattr(agents, "executable", lambda provider: f"/bin/{provider}")
    pages = [tmp_path / "p1.png", tmp_path / "p2.png"]
    args = agents.command("codex", "gpt-6-luna", "high", tmp_path, pages)
    assert args[args.index("-i") + 1] == str(pages[0]) and args.count("-i") == 2
    disabled = {args[i + 1] for i, arg in enumerate(args) if arg == "--disable"}
    # Codex 0.160+ routes MCP tool calls through the code-mode host; disabling it breaks note writing.
    assert "code_mode_host" not in disabled and "shell_tool" in disabled
    assert args[-1] == "-"


def test_settings_and_background_routes(client, course):
    assert client.get("/api/v1/settings").json()["reading_model"]["model"] == "gpt-6-luna"
    choice = {"provider": "claude", "model": "claude-sonnet-5-5", "effort": "high"}
    assert client.put("/api/v1/settings", json={"reading_model": choice}).json()["reading_model"] == choice
    assert {s["name"] for s in client.get("/api/v1/skills").json()} >= {"weekly-notes", "source-reading"}
    response = client.post(
        f"/api/v1/courses/{course}/weeks/1/generate", json={"provider": "codex", "model": "gpt-6.1-sol"}
    )
    assert response.status_code == 503  # Background agents are disabled in tests.
    assert client.get(f"/api/v1/courses/{course}/tasks").json() == []


def test_page_notes_replace_raw_text_in_search(client, course, settings):
    from open_lecture.workspace import Workspace

    base = f"/api/v1/courses/{course}"
    with pymupdf.open() as pdf:
        pdf.new_page().insert_text((72, 72), "Thevenin garbled extraction")
        upload = client.post(base + "/sources", files={"file": ("Week 5.pdf", pdf.tobytes())}).json()
    wait_job(client, course, upload["job_id"])
    source = next(s for s in client.get(base + "/sources").json() if s["id"] == upload["source_id"])
    assert source["week"] == 5 and source["reading_status"] == "pending"

    workspace = Workspace(settings)
    try:
        workspace.store_page_notes(
            course, upload["source_id"], 1, {1: "Thevenin equivalent: $V_{Th}=v_{oc}$"}
        )
        workspace.update_reading(upload["source_id"], 1, status="ready", pages_done=1)
    finally:
        workspace.close()
    hits = client.get(base + "/search", params={"query": "Thevenin"}).json()
    assert [hit["method"] for hit in hits] == ["ai_digest"]
    notes = client.get(base + f"/sources/{upload['source_id']}/notes").json()
    assert notes["pages"][0]["note"].startswith("Thevenin equivalent")


def test_page_zoom_region_and_thumbnail_sheet(tmp_path):
    import pymupdf

    from open_lecture.render_page import grid_png, page_png

    document = pymupdf.open()
    for number in range(1, 6):
        document.new_page(width=600, height=800).insert_text((50, 100), f"Page {number}", fontsize=40)
    full = pymupdf.Pixmap(page_png(document, 2, 800))
    zoom = pymupdf.Pixmap(page_png(document, 2, 800, [0, 0, 0.5, 0.25]))
    assert max(full.width, full.height) == max(zoom.width, zoom.height) == 800
    assert zoom.width > zoom.height  # a wide crop of the top-left of the page
    sheet = pymupdf.Pixmap(grid_png(document, 2, 12))
    assert sheet.width > sheet.height  # pages 2-5 laid out side by side
    with pytest.raises(ValueError):
        page_png(document, 2, 800, [0.5, 0, 0.2, 1])


def test_image_upload_can_be_rendered_and_read(client, course, settings):
    from open_lecture.workspace import Workspace

    base = f"/api/v1/courses/{course}"
    with pymupdf.open() as pdf:
        page = pdf.new_page(width=200, height=200)
        page.insert_text((20, 40), "Handwritten circuit placeholder")
        png = page.get_pixmap().tobytes("png")
    uploaded = client.post(base + "/sources", files={"file": ("Week 6.png", png)}).json()
    assert wait_job(client, course, uploaded["job_id"])["status"] == "completed"
    ws = Workspace(settings)
    try:
        image = ws.render_source_page(course, uploaded["source_id"], 1)
        assert pymupdf.Pixmap(image).width > 0
        ws.store_page_notes(course, uploaded["source_id"], 1, {1: "Circuit: $v=L\\,di/dt$."})
        assert ws.source_notes(course, uploaded["source_id"])["pages"][0]["note"].startswith("Circuit")
    finally:
        ws.close()


def test_rereading_preserves_citations_and_replaces_search_text(client, course, settings):
    from open_lecture.errors import DomainError
    from open_lecture.workspace import Workspace

    base = f"/api/v1/courses/{course}"
    with pymupdf.open() as pdf:
        pdf.new_page().insert_text((72, 72), "Raw extraction")
        uploaded = client.post(base + "/sources", files={"file": ("Week 6.pdf", pdf.tobytes())}).json()
    wait_job(client, course, uploaded["job_id"])
    source_id = uploaded["source_id"]
    ws = Workspace(settings)
    try:
        ws.store_page_notes(course, source_id, 1, {1: "Oldword voltage"})
        ws.update_reading(source_id, 1, status="ready", pages_done=1)
        page = ws.source_notes(course, source_id)["pages"][0]
        citation = {"source_id": source_id, "version": 1, "chunk_id": page["chunk_id"]}
        saved = client.post(
            base + "/documents",
            json={
                "title": "Cited notes",
                "blocks": [{"type": "paragraph", "text": "Voltage", "citations": [citation]}],
            },
        ).json()["document"]
        with pytest.raises(DomainError, match="between 1 and 1"):
            ws.request_reading(course, source_id, [2])
        ws.request_reading(course, source_id, [1])
        assert ws.pages_read(source_id, 1) == set()
        assert ws.source_notes(course, source_id)["pages"][0] == page
        assert ws.page_text(source_id, 1, 1) == "Raw extraction"
        assert ws.search_sources(course, "Oldword")[0]["id"] == citation["chunk_id"]
        assert ws.search_sources(course, "Raw extraction") == []
        ws.store_page_notes(course, source_id, 1, {1: "Newword current"})
        ws.update_reading(source_id, 1, status="ready", pages_done=1)
        assert ws.source_notes(course, source_id)["pages"][0]["chunk_id"] == citation["chunk_id"]
        assert ws.search_sources(course, "Oldword") == []
        assert ws.search_sources(course, "Newword")[0]["id"] == citation["chunk_id"]
        # A subsequent edit still validates the previously saved citation.
        assert (
            client.patch(
                base + f"/documents/{saved['document_id']}",
                json={"expected_revision": saved["revision"], "title": "Updated cited notes"},
            ).status_code
            == 200
        )
        with pytest.raises(DomainError, match="1–20000"):
            ws.store_page_notes(course, source_id, 1, {1: "x" * 20001})
        assert ws.source_notes(course, source_id)["pages"][0]["note"] == "Newword current"
    finally:
        ws.close()


def test_week_prompt_requires_completed_readings(client, course, settings):
    from open_lecture.runner import AgentError, week_prompt
    from open_lecture.workspace import Workspace

    with pymupdf.open() as pdf:
        pdf.new_page().insert_text((72, 72), "Inductor notes")
        uploaded = client.post(
            f"/api/v1/courses/{course}/sources", files={"file": ("Week 6.pdf", pdf.tobytes())}
        ).json()
    wait_job(client, course, uploaded["job_id"])
    ws = Workspace(settings)
    try:
        with pytest.raises(AgentError, match="Finish source ingestion"):
            week_prompt(ws, course, 6, False)
        ws.store_page_notes(course, uploaded["source_id"], 1, {1: "Inductor voltage"})
        ws.update_reading(uploaded["source_id"], 1, status="ready", pages_done=1)
        assert "AI page notes: ready" in week_prompt(ws, course, 6, False)
    finally:
        ws.close()


def test_invalid_model_notes_stop_after_two_attempts(client, course, settings, monkeypatch):
    from open_lecture.runner import Runner
    from open_lecture.workspace import Workspace

    with pymupdf.open() as pdf:
        pdf.new_page().insert_text((72, 72), "Inductor")
        uploaded = client.post(
            f"/api/v1/courses/{course}/sources", files={"file": ("Week 6.pdf", pdf.tobytes())}
        ).json()
    wait_job(client, course, uploaded["job_id"])
    ws = Workspace(settings)
    runner = Runner(ws, settings)
    calls = []

    def invalid_answer(*args, **kwargs):
        calls.append(args)
        return "## Page 1\n" + "x" * 20001

    monkeypatch.setattr(runner, "run_agent", invalid_answer)
    try:
        runner.read_source(ws.claim_pending_reading("test-model"))
        assert len(calls) == 2
        status = ws.reading_status(course, uploaded["source_id"])
        assert status["status"] == "failed"
        assert "1–20000" in status["error"]
        assert ws.pages_read(uploaded["source_id"], 1) == set()
    finally:
        runner.stop()
        ws.close()
