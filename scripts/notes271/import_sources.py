"""Import each unique 271 PDF once and retain a hash-based duplicate-removal record."""

import hashlib
import json
import time
from pathlib import Path

import httpx

COURSE = "d0b18428-9c03-4bbf-87af-7a1169d667ab"
SOURCE = Path(r"C:\Users\vladh\Downloads\271 - Digital Systems")
OUT = Path(__file__).parent / "out"
OUT.mkdir(exist_ok=True)
api = httpx.Client(base_url=f"http://127.0.0.1:8000/api/v1/courses/{COURSE}", timeout=60)
# Prefer the unnumbered originals. Only remove verified byte-identical aliases.
groups = {}
for file in SOURCE.glob("*.pdf"):
    digest = hashlib.sha256(file.read_bytes()).hexdigest()
    groups.setdefault(digest, []).append(file)
removed = []
for digest, files in groups.items():
    files.sort(key=lambda p: (len(p.name), p.name))
    keep = files[0]
    for duplicate in files[1:]:
        assert duplicate.parent.resolve() == SOURCE.resolve()
        assert duplicate.read_bytes() == keep.read_bytes()
        duplicate.unlink()
        removed.append({"removed": duplicate.name, "kept": keep.name, "sha256": digest})
    name = keep.name.lower()
    kind = (
        "syllabus"
        if "syllabus" in name
        else "lecture"
        if ("lecture" in name or "section2" in name)
        else "reference"
        if ("formula" in name or "figures" in name)
        else "tutorial"
        if "tutorial" in name
        else "practice"
    )
    r = api.post(
        "/sources", data={"kind": kind}, files={"file": (keep.name, keep.read_bytes(), "application/pdf")}
    )
    r.raise_for_status()
    print(keep.name, r.json()["source_id"], "reused" if r.json().get("duplicate") else "imported", flush=True)
if removed:
    (OUT / "duplicates.json").write_text(json.dumps(removed, indent=2), encoding="utf-8")
deadline = time.monotonic() + 180
while True:
    sources = api.get("/sources?limit=100").json()
    if all(s["status"] not in ("queued", "running") for s in sources):
        break
    if time.monotonic() > deadline:
        raise SystemExit("Ingestion still running; rerun to collect citations.")
    time.sleep(1)
cites = {}
for s in sources:
    by_page = {}
    for offset in range(0, 1000, 100):
        r = api.get(f"/sources/{s['id']}?limit=100&offset={offset}")
        r.raise_for_status()
        data = r.json()
        for c in data["chunks"]:
            if c.get("page") and str(c["page"]) not in by_page:
                by_page[str(c["page"])] = {
                    "source_id": s["id"],
                    "version": s["current_version"],
                    "chunk_id": c["id"],
                }
        if len(data["chunks"]) < 100:
            break
    cites[s["filename"]] = by_page
(OUT / "sources.json").write_text(json.dumps(sources, indent=2), encoding="utf-8")
(OUT / "citations.json").write_text(json.dumps(cites, indent=2), encoding="utf-8")
print("Ready:", len(sources), "sources;", len(removed), "duplicate files removed")
