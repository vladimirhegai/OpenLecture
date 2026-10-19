"""Index the user-provided announcement so the scope can be cited inside the notes."""

import json
import time
from pathlib import Path

import httpx
from lib import API, OUT

file = Path(__file__).with_name("midterm_scope.md")
api = httpx.Client(base_url=API, timeout=60)
r = api.post(
    "/sources", data={"kind": "reference"}, files={"file": (file.name, file.read_bytes(), "text/markdown")}
)
r.raise_for_status()
source_id = r.json()["source_id"]
for _ in range(50):
    r = api.get(f"/sources/{source_id}?limit=100")
    r.raise_for_status()
    source = r.json()
    if source["status"] == "ready" and source["chunks"]:
        break
    time.sleep(0.2)
else:
    raise RuntimeError("Announcement ingestion did not finish")
citations = {}
for key, fragment in [("exam", "40 minutes"), ("exclusions", "Problem Set 2 Q2")]:
    chunk = next(c for c in source["chunks"] if fragment in c["text"])
    citations[key] = {"source_id": source_id, "version": source["current_version"], "chunk_id": chunk["id"]}
(OUT / "midterm-scope.json").write_text(json.dumps(citations, indent=2), encoding="utf-8")
print("Midterm scope indexed:", source_id)
