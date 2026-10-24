"""Import the ELEC 226 PDFs once and record a citation (first chunk) for every page: out/citations.json."""

import json
import time
from pathlib import Path

import httpx

COURSE = "149e587a-a62f-415a-91de-6337ea2f0006"
SOURCE = Path(r"C:\Users\vladh\Downloads\226 - Probability")
OUT = Path(__file__).parent / "out"
OUT.mkdir(exist_ok=True)
api = httpx.Client(base_url=f"http://127.0.0.1:8000/api/v1/courses/{COURSE}", timeout=120)

for file in sorted(SOURCE.glob("*.pdf")):
    name = file.name.lower()
    kind = "lecture" if name.startswith("elec226") else "tutorial" if "tutorial" in name else "practice"
    r = api.post("/sources", data={"kind": kind}, files={"file": (file.name, file.read_bytes(), "application/pdf")})
    r.raise_for_status()
    print(file.name, r.json()["source_id"], "reused" if r.json().get("duplicate") else "imported", flush=True)

deadline = time.monotonic() + 600
while True:
    sources = api.get("/sources?limit=100").json()
    if all(s["status"] not in ("queued", "running") for s in sources):
        break
    if time.monotonic() > deadline:
        raise SystemExit("Ingestion still running; rerun to collect citations.")
    time.sleep(2)

cites = {}
for s in sources:
    by_page = {}
    for offset in range(0, 1000, 100):
        r = api.get(f"/sources/{s['id']}?limit=100&offset={offset}")
        r.raise_for_status()
        data = r.json()
        for c in data["chunks"]:
            if c.get("page") and str(c["page"]) not in by_page:
                by_page[str(c["page"])] = {"source_id": s["id"], "version": s["current_version"], "chunk_id": c["id"]}
        if len(data["chunks"]) < 100:
            break
    cites[s["filename"]] = by_page
(OUT / "citations.json").write_text(json.dumps(cites, indent=2), encoding="utf-8")
print("Ready:", {s["filename"]: (s["status"], len(cites[s["filename"]])) for s in sources})
