"""Check scope, figure validity, and live preservation of the reorganized notes."""

import json
import re

import httpx
from lib import API, OUT, string_values

from open_lecture import digital, schematic
from open_lecture.schemas import DocumentCreate

docs = [json.loads((OUT / f"{i:02}.json").read_text(encoding="utf-8")) for i in range(1, 10)]
for n, d in enumerate(docs, 1):
    DocumentCreate.model_validate(d)
    assert d["title"].startswith(f"{n:02} · ")
    if n <= 3:
        assert "Midterm" in d["title"]
        text = "\n".join(string_values(d["blocks"]))
        assert not any(term in text for term in ["VHDL", "LUT", "PLA", "Karnaugh", "Noise margin"])
        assert not any(b["type"] == "code" for b in d["blocks"])
    else:
        assert "Later" in d["title"]
    for b in d["blocks"]:
        for text in string_values(b):
            for source in re.findall(r"```digital[^\n]*\n(.*?)```", text, re.S):
                digital.render_svg(source)
        if b["type"] == "schematic":
            schematic.check(b["source"])
assert "octal" not in "\n".join(string_values(docs[0])).lower()
titles = [b.get("title", "") for b in docs[2]["blocks"]]
assert all(any(f"PS2 Q{q}:" in t for t in titles) for q in (1, 3, 4, 5))
assert not any(re.search(r"PS2 Q(?:2|6|7|8)\b", t) for t in titles)
logic = "\n".join(string_values(docs[1]))
assert all(
    term in logic for term in ["description", "timing", "Venn", "Complement", "SOP", "POS", "NAND", "NOR"]
)
with httpx.Client(base_url=API, timeout=60) as api:
    live = api.get("/documents?limit=100").json()
    notes = [d for d in live if d["document_type"] == "study_notes"]
    assert len(notes) == 9, "Reorganization must not create duplicate active notes"
    assert {d["title"] for d in notes} == {d["title"] for d in docs}
print(
    "Verified: 3 midterm notes, 6 retained later notes, PS2 scope, schemas, figures, and no duplicate notes"
)
