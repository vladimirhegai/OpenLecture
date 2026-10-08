"""Independent agent scenarios using the real API, SQLite, and ingestion worker."""

from uuid import uuid4

from conftest import wait_job

from open_lecture.schemas import CourseProfileUpdate


def chat_url(client, course):
    base = f"/api/v1/courses/{course}"
    response = client.post(base + "/chats", json={"title": "Context agent exercise"})
    assert response.status_code == 201
    return base, base + f"/chats/{response.json()['id']}"


def select_document(client, base, chat, blocks, selected_id):
    created = client.post(base + "/documents", json={"title": "Study notes", "blocks": blocks})
    assert created.status_code == 201, created.text
    document = created.json()["document"]
    selected = client.put(
        chat + "/viewer-state",
        json={
            "document_id": document["document_id"],
            "block_id": selected_id,
        },
    )
    assert selected.status_code == 200, selected.text
    return document


def context(client, chat, query, budget=3000):
    response = client.post(chat + "/context", json={"query": query, "token_budget": budget})
    assert response.status_code == 200, response.text
    inspection = response.json()
    assert inspection["estimated_input_tokens"] + inspection["reserved_tokens"] <= budget
    return inspection["context"]


def test_simple_followup_in_large_document_keeps_selected_block(client, course):
    base, chat = chat_url(client, course)
    selected_id = str(uuid4())
    selected = {
        "id": selected_id,
        "type": "paragraph",
        "text": "Negative power means this source delivers energy under the passive sign convention.",
    }
    blocks = [{"type": "paragraph", "text": "Unrelated material " * 200} for _ in range(80)]
    blocks.insert(60, selected)
    document = select_document(client, base, chat, blocks, selected_id)
    packet = context(client, chat, "Why is that negative?")
    assert packet["document_blocks"][0]["block"]["id"] == selected_id
    assert packet["document_blocks"][0]["revision"] == document["revision"]
    assert len(packet["document_blocks"]) <= 4
    assert "delivers energy" in packet["document_blocks"][0]["block"]["text"]


def test_oversized_selected_block_retains_useful_excerpt(client, course):
    base, chat = chat_url(client, course)
    selected_id = str(uuid4())
    select_document(
        client,
        base,
        chat,
        [
            {
                "id": selected_id,
                "type": "paragraph",
                "text": "Negative power means the source delivers energy. " + "Supporting detail. " * 650,
            }
        ],
        selected_id,
    )
    packet = context(client, chat, "Why is power negative?")
    selected = [item for item in packet["document_blocks"] if item["block"]["id"] == selected_id]
    assert selected, "An oversized selected block must remain available as a bounded excerpt"
    assert "delivers energy" in selected[0]["block"]["text"]
    assert selected[0]["excerpt"] is True
    assert selected[0]["retrieval_hint"]
    full = client.get(base + f"/documents/{selected[0]['document_id']}").json()
    assert len(full["blocks"][0]["text"]) > 12000, "Excerpting must not modify saved notes"


def test_vague_followup_uses_open_document_without_block_selection(client, course):
    base, chat = chat_url(client, course)
    document = client.post(
        base + "/documents",
        json={
            "title": "Sign convention",
            "blocks": [
                {
                    "type": "paragraph",
                    "text": "Negative power means the source delivers energy.",
                }
            ],
        },
    ).json()["document"]
    assert (
        client.put(
            chat + "/viewer-state",
            json={
                "document_id": document["document_id"],
            },
        ).status_code
        == 200
    )
    packet = context(client, chat, "Explain this")
    assert packet["document_blocks"], "The open document is context even without a selected block"
    assert "delivers energy" in packet["document_blocks"][0]["block"]["text"]


def test_relevant_source_survives_long_unrelated_history(client, course):
    base, chat = chat_url(client, course)
    lecture = "Thevenin equivalent resistance is found looking into the terminals. " * 20
    job = client.post(base + "/sources", files={"file": ("thevenin.txt", lecture.encode())}).json()
    assert wait_job(client, course, job["job_id"])["status"] == "completed"
    for i in range(24):
        added = client.post(
            chat + "/messages",
            json={
                "role": "user",
                "content": f"Unrelated question {i}. " + "previous topic " * 45,
            },
        )
        assert added.status_code == 201
    packet = context(client, chat, "How do I find Thevenin resistance?", budget=4000)
    assert packet["source_chunks"], "History must not crowd out the only relevant source evidence"
    assert packet["source_chunks"][0]["source_id"] == job["source_id"]
    assert packet["source_chunks"][0]["trust"] == "untrusted_source_content"
    assert packet["source_chunks"][0]["excerpt"] is True
    assert any(message["excerpt"] for message in packet["recent_messages"])
    assert len(client.get(chat + "/messages").json()) == 24


def test_course_pack_context_is_compact_and_subject_relevant(client, course):
    _, chat = chat_url(client, course)
    client.app.state.workspace.update_profile(
        course,
        CourseProfileUpdate(
            expected_revision=0,
            pack_ids=["circuits"],
        ),
    )
    packet = context(client, chat, "Explain negative power using the passive sign convention", budget=4000)
    assert any(item.get("pack_id") == "circuits" for item in packet["course_guidance"])
    rules = [item["guidance"] for item in packet["course_guidance"] if "guidance" in item]
    assert len(rules) <= 2
    assert any("negative power" in rule for rule in rules)
    assert all(item["pack_id"] == "circuits" for item in packet["course_guidance"])


def test_missing_evidence_does_not_borrow_other_course_sources(client, course):
    _, chat = chat_url(client, course)
    other = client.post("/api/v1/courses", json={"code": "OTHER", "title": "Other course"}).json()["id"]
    job = client.post(
        f"/api/v1/courses/{other}/sources",
        files={
            "file": ("secret.txt", b"Thevenin resistance is 123 ohms in the other course."),
        },
    ).json()
    assert wait_job(client, other, job["job_id"])["status"] == "completed"
    packet = context(client, chat, "What is the Thevenin resistance?")
    assert packet["source_chunks"] == []
    assert packet["document_blocks"] == []
    assert packet["course_guidance"] == []
    assert "untrusted evidence" in packet["source_policy"]
