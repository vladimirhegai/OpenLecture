from concurrent.futures import ThreadPoolExecutor
from uuid import uuid4

from conftest import wait_job
from fastapi.testclient import TestClient

from open_lecture.api import create_app


def test_source_notes_followup_targeted_edit_and_restart(client, course, settings):
    base = f"/api/v1/courses/{course}"
    upload = client.post(
        base + "/sources",
        files={
            "file": (
                "week1.md",
                b"# Power\n\nPassive sign convention: p = vi. Negative power means delivery.",
            )
        },
    )
    assert upload.status_code == 202
    source = upload.json()
    assert wait_job(client, course, source["job_id"])["status"] == "completed"
    passage = client.get(base + "/search", params={"query": "power"}).json()[0]
    citation = {"source_id": passage["source_id"], "version": passage["version"], "chunk_id": passage["id"]}
    folder = client.post(base + "/folders", json={"title": "Week 1"}).json()
    first, second = str(uuid4()), str(uuid4())
    body = {
        "title": "Week 1: Circuit fundamentals",
        "academic_week": 1,
        "topic_keys": ["power"],
        "folder_id": folder["id"],
        "idempotency_key": "week1",
        "blocks": [
            {"id": first, "type": "heading", "text": "Power"},
            {
                "id": second,
                "type": "paragraph",
                "text": "Negative power indicates delivery.",
                "citations": [citation],
            },
            {"type": "equation", "latex": "p=vi"},
            {
                "type": "practice_problem",
                "prompt": "Find power for 2 V and 3 A.",
                "solution": "6 W",
                "origin": "original",
            },
        ],
    }
    response = client.post(base + "/documents", json=body)
    assert response.status_code == 201, response.text
    doc = response.json()["document"]
    document_id = doc["document_id"]
    assert doc["reference"]["route"] == f"/courses/{course}/docs/{document_id}"
    retry = client.post(base + "/documents", json=body).json()
    assert not retry["created"] and retry["document"]["document_id"] == document_id
    assert client.post(base + "/documents", json=body | {"title": "Changed"}).status_code == 409
    duplicate = client.post(base + "/documents", json=body | {"idempotency_key": "other"})
    assert duplicate.status_code == 409 and duplicate.json()["error"]["code"] == "document_exists"
    chat = client.post(base + "/chats", json={"title": "Midterm preparation"}).json()["id"]
    chat_url = base + f"/chats/{chat}"
    assert (
        client.put(
            chat_url + "/viewer-state", json={"document_id": document_id, "block_id": second}
        ).status_code
        == 200
    )
    question = "Why is power negative in that example?"
    client.post(chat_url + "/messages", json={"role": "user", "content": question})
    context = client.post(chat_url + "/context", json={"query": question}).json()
    assert context["context"]["document_blocks"][0]["block"]["id"] == second
    assert context["estimated_input_tokens"] + context["reserved_tokens"] <= context["budget"]
    assert client.get(base + f"/documents/{document_id}").json()["revision"] == 1
    assert (
        client.post(base + "/document-actions/plan", json={"intent": "question"}).json()["action"]
        == "answer_in_chat"
    )
    assert (
        client.post(base + "/document-actions/plan", json={"intent": "create", "academic_week": 1}).json()[
            "action"
        ]
        == "reuse_document"
    )
    new_block = {
        "id": str(uuid4()),
        "type": "paragraph",
        "text": "The chosen current reference determines the sign.",
    }
    edited = client.patch(
        base + f"/documents/{document_id}",
        json={
            "expected_revision": 1,
            "operations": [{"op": "insert", "after_id": second, "block": new_block}],
        },
    ).json()
    assert edited["revision"] == 2
    assert edited["blocks"][2]["id"] == new_block["id"]
    assert edited["blocks"][0] == doc["blocks"][0]
    assert (
        client.patch(
            base + f"/documents/{document_id}", json={"expected_revision": 1, "title": "Stale write"}
        ).status_code
        == 409
    )
    historical = client.get(base + f"/documents/{document_id}", params={"revision": 1}).json()
    assert historical["blocks"] == doc["blocks"]
    # A separate process/client sees the same committed state, even while the first server remains open.
    with TestClient(create_app(settings)) as restarted:
        assert restarted.get(base + f"/documents/{document_id}").json()["revision"] == 2
        assert restarted.get(base + "/search", params={"query": "power"}).json()
    update = client.post(
        base + "/sources",
        data={"source_id": source["source_id"]},
        files={"file": ("week1.md", b"# Power\n\nRevised power notes explain energy delivery.")},
    ).json()
    assert wait_job(client, course, update["job_id"])["status"] == "completed"
    stale = client.get(base + f"/documents/{document_id}").json()
    assert stale["potentially_outdated"] and stale["revision"] == 2
    old_source = client.get(base + f"/sources/{source['source_id']}", params={"version": 1}).json()
    assert any("Passive sign" in chunk["text"] for chunk in old_source["chunks"])
    original = client.get(base + f"/sources/{source['source_id']}/original", params={"version": 1})
    assert b"Passive sign" in original.content


def test_course_isolation_and_citation_validation(client, course):
    base = f"/api/v1/courses/{course}"
    other = client.post("/api/v1/courses", json={"code": "MATH", "title": "Calculus"}).json()["id"]
    other_base = f"/api/v1/courses/{other}"
    folder = client.post(base + "/folders", json={"title": "Private"}).json()["id"]
    assert (
        client.post(other_base + "/folders", json={"title": "Child", "parent_id": folder}).status_code == 404
    )
    assert (
        client.post(other_base + "/documents", json={"title": "Bad", "folder_id": folder}).status_code == 404
    )
    doc = client.post(base + "/documents", json={"title": "My notes"}).json()["document"]
    assert client.get(other_base + f"/documents/{doc['document_id']}").status_code == 404
    assert client.get(other_base + "/documents").json() == []
    chat = client.post(other_base + "/chats", json={"title": "Chat"}).json()["id"]
    ref = {"document_id": doc["document_id"], "revision": 1}
    assert (
        client.post(
            other_base + f"/chats/{chat}/messages",
            json={"role": "assistant", "content": "Link", "references": [ref]},
        ).status_code
        == 404
    )
    bad = {
        "type": "paragraph",
        "text": "Fake evidence",
        "citations": [{"source_id": str(uuid4()), "version": 1, "chunk_id": str(uuid4())}],
    }
    assert (
        client.post(base + "/documents", json={"title": "Bad citation", "blocks": [bad]}).status_code == 400
    )
    problem = {
        "type": "practice_problem",
        "prompt": "Tutorial problem",
        "solution": "Answer",
        "origin": "source",
    }
    assert (
        client.post(base + "/documents", json={"title": "Bad problem", "blocks": [problem]}).status_code
        == 422
    )


def test_atomic_edits_concurrency_and_restore(client, course):
    base = f"/api/v1/courses/{course}/documents"
    first, second = str(uuid4()), str(uuid4())
    doc = client.post(
        base,
        json={
            "title": "Notes",
            "blocks": [
                {"type": "paragraph", "id": first, "text": "First"},
                {"type": "paragraph", "id": second, "text": "Second"},
            ],
        },
    ).json()["document"]
    url = base + "/" + doc["document_id"]
    invalid = client.patch(
        url,
        json={
            "expected_revision": 1,
            "title": "Must roll back",
            "operations": [{"op": "remove", "block_id": first}, {"op": "remove", "block_id": str(uuid4())}],
        },
    )
    assert invalid.status_code == 404
    assert client.get(url).json()["title"] == "Notes"
    with ThreadPoolExecutor(2) as pool:
        statuses = list(
            pool.map(
                lambda title: client.patch(url, json={"expected_revision": 1, "title": title}).status_code,
                ["A", "B"],
            )
        )
    assert sorted(statuses) == [200, 409]
    moved = client.patch(
        url, json={"expected_revision": 2, "operations": [{"op": "move", "block_id": second}]}
    ).json()
    assert moved["blocks"][0]["id"] == second
    assert client.post(url + "/delete", json={"expected_revision": 3}).json()["deleted"]
    assert client.get(base).json() == []
    assert len(client.get(base, params={"include_deleted": True}).json()) == 1
    restored = client.post(url + "/restore", json={"expected_revision": 4}).json()
    assert not restored["deleted"] and restored["revision"] == 5
    assert len(client.get(url + "/revisions").json()) == 5


def test_duplicate_creation_race(client, course):
    url = f"/api/v1/courses/{course}/documents"
    with ThreadPoolExecutor(2) as pool:
        statuses = list(
            pool.map(
                lambda _: client.post(url, json={"title": "Week one", "academic_week": 1}).status_code,
                range(2),
            )
        )
    assert sorted(statuses) == [201, 409]
    assert len(client.get(url).json()) == 1
    assert (
        client.post(
            url, json={"title": "Separate version", "academic_week": 1, "separate_copy": True}
        ).status_code
        == 201
    )
