"""Exercise a small study session using only the running HTTP API."""

import os
import time

import httpx

token = os.getenv("OPENLECTURE_API_TOKEN")
with httpx.Client(
    base_url=os.getenv("OPENLECTURE_API_URL", "http://127.0.0.1:8000/api/v1"),
    timeout=30,
    headers={"Authorization": f"Bearer {token}"} if token else {},
) as client:

    def request(method, url, **kwargs):
        response = client.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()

    courses = request("GET", "/courses")
    course = next((item for item in courses if item["code"] == "DEMO 101"), None)
    course = course or request("POST", "/courses", json={"code": "DEMO 101", "title": "Circuit study demo"})
    base = f"/courses/{course['id']}"
    upload = request(
        "POST",
        base + "/sources",
        data={"kind": "reference"},
        files={
            "file": (
                "original-sample.md",
                b"# Original demonstration material\n\nFor a resistor, V = IR. This is not an uploaded university tutorial.",
            )
        },
    )
    for _ in range(150):
        job = request("GET", base + f"/jobs/{upload['job_id']}")
        if job["status"] in {"completed", "failed"}:
            break
        time.sleep(0.1)
    if job["status"] != "completed":
        raise RuntimeError(job)
    passage = request("GET", base + "/search", params={"query": "resistor"})[0]
    citation = {"source_id": passage["source_id"], "version": passage["version"], "chunk_id": passage["id"]}
    existing = request("GET", base + "/documents", params={"academic_week": 1})
    if existing:
        doc = request("GET", base + f"/documents/{existing[0]['document_id']}")
    else:
        doc = request(
            "POST",
            base + "/documents",
            json={
                "title": "Week 1: Ohm's law",
                "academic_week": 1,
                "blocks": [
                    {"type": "equation", "latex": "V=IR", "citations": [citation]},
                    {
                        "type": "practice_problem",
                        "prompt": "Find voltage for 2 mA through 3 kOhm.",
                        "solution": "V = 0.002 * 3000 = 6 V.",
                        "origin": "original",
                    },
                ],
            },
        )["document"]
    if doc["revision"] == 1:
        doc = request(
            "PATCH",
            base + f"/documents/{doc['document_id']}",
            json={
                "expected_revision": 1,
                "operations": [
                    {
                        "op": "insert",
                        "after_id": doc["blocks"][0]["id"],
                        "block": {
                            "type": "paragraph",
                            "text": "Convert milliamps to amps before multiplying.",
                        },
                    }
                ],
            },
        )
    print(f"Saved {doc['title']} at revision {doc['revision']}")
    print(doc["reference"])
