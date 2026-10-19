"""Publish the three-section midterm index and preserve later-study navigation."""

import json
import uuid
from pathlib import Path

import httpx
from export import markdown
from lib import API, COURSE, OUT

api = httpx.Client(base_url=API, timeout=60)
docs = []
for n in range(1, 10):
    raw = json.loads((OUT / f"{n:02}-published.json").read_text(encoding="utf-8"))
    docs.append(raw.get("document", raw))
scope = json.loads((OUT / "midterm-scope.json").read_text(encoding="utf-8"))


def link(d):
    return f"[{d['title']}](http://127.0.0.1:8000/courses/{COURSE}/docs/{d['document_id']})"


blocks = [
    {"type": "heading", "level": 1, "text": "October 29 midterm · study these three sections"},
    {
        "type": "paragraph",
        "text": "**Thursday October 29, during class · 40 minutes · Weeks 1–5 only.** Week 6 after reading week is excluded. The instructor’s announcement controls the scope below.",
        "citations": [scope["exam"]],
    },
    {"type": "list", "ordered": True, "items": [link(d) for d in docs[:3]]},
    {
        "type": "table",
        "columns": ["Main note", "What to study"],
        "rows": [
            ["Section 1", "Binary ↔ decimal ↔ hexadecimal, including fractions and limited precision."],
            [
                "Section 2",
                "Description ↔ truth table ↔ function ↔ gates; complements; Venn and timing diagrams; canonical SOP/POS; NAND–NAND and NOR–NOR conversions.",
            ],
            [
                "Section 3 — Week 5",
                "NMOS/PMOS switches, NMOS and CMOS gates, transistor counts, drawing CMOS from a function, and recovering a function from CMOS.",
            ],
        ],
    },
    {
        "type": "paragraph",
        "text": "**PS2: study Q1 and Q3–Q5. Skip Q2 and Q6–Q8 for this midterm.** These exclusions do not remove general Boolean-algebra or CMOS skills from the announced topic list.",
        "citations": [scope["exclusions"]],
    },
    {
        "type": "paragraph",
        "text": "After the three sections, attempt the supplied previous-year midterm with a 40-minute limit. Use its solutions to check reasoning and notation; use this announcement to decide what is examinable this year.",
    },
    {"type": "heading", "level": 1, "text": "Later study · not part of the current midterm study set"},
    {"type": "list", "ordered": False, "items": [link(d) for d in docs[3:]]},
    {
        "type": "paragraph",
        "text": "Later notes retain VHDL, voltage margins, programmable logic, other number bases, K-maps, arithmetic circuits, building blocks, storage/timing, and FSMs for subsequent assessments. Their presence does not indicate scope for a future exam.",
    },
    {"type": "heading", "level": 1, "text": "Sources"},
    {
        "type": "paragraph",
        "text": "The three main notes use the supplied Sections 1–3 lectures, relevant tutorials/problem sets and solutions, the previous-year midterm, and the instructor announcement supplied in chat. Later sections are marked when based on problem sets without corresponding supplied lectures. The existing 20 unique PDFs were retained; the announcement is also indexed as a text source.",
    },
]
for b in blocks:
    b.setdefault("citations", [])
    b["id"] = str(uuid.uuid4())
map_id = "7145f989-9157-4148-b309-71029d0b5768"
old = api.get(f"/documents/{map_id}").json()
ops = [{"op": "remove", "block_id": b["id"]} for b in old["blocks"]]
previous = None
for b in blocks:
    ops.append({"op": "insert", "block": b, "after_id": previous})
    previous = b["id"]
r = api.patch(
    f"/documents/{map_id}", json={"actor": "agent", "expected_revision": old["revision"], "operations": ops}
)
r.raise_for_status()
Path("notes/ELEC-271-Course-map.md").write_text(
    "# ELEC 271: Course map\n\n" + "\n\n".join(markdown(b) for b in blocks) + "\n", encoding="utf-8"
)
profile = api.get("/profile").json()
body = {k: v for k, v in profile.items() if k not in {"revision", "course_id"}}
body["expected_revision"] = profile["revision"]
body["study_preferences"] = [
    p for p in body["study_preferences"] if not p.startswith("Follow the concise ELEC 231 v2 note style:")
]
preferences = [
    "Use three main midterm notes: 01 Binary Numbers, 02 Introduction to Logic Circuits, 03 Implementation Technology (Week 5). Put material outside this midterm study set in clearly labeled Later notes 04 onward. Within each note, use ordered topical subsections, short explanations, distinct worked examples, figures, and a few hidden solutions; no end summaries.",
    "Midterm announcement: Thursday October 29 during class, 40 minutes; Weeks 1–5 only, no Week 6. Section 1 includes fractional binary/decimal/hex conversion. Section 2 includes descriptions, tables, complements, Venn/timing, canonical SOP/POS, gate analysis/drawing, NAND–NAND and NOR–NOR. Section 3 includes transistor switches and NMOS/CMOS drawing/interpretation. PS2 Q2 and Q6–Q8 are excluded; prioritize Q1 and Q3–Q5. Do not infer future exam scope.",
]
for preference in preferences:
    if preference not in body["study_preferences"]:
        body["study_preferences"].append(preference)
r = api.put("/profile", json=body)
r.raise_for_status()
stats = {
    "notes": len(docs),
    "midterm_notes": 3,
    "later_notes": 6,
    "blocks": sum(len(d["blocks"]) for d in docs),
    "worked_examples": sum(b["type"] == "worked_example" for d in docs for b in d["blocks"]),
    "practice_problems": sum(b["type"] == "practice_problem" for d in docs for b in d["blocks"]),
    "figures": sum(
        "```digital" in b.get("text", "") or b["type"] == "schematic" for d in docs for b in d["blocks"]
    ),
    "documents": [{"id": d["document_id"], "title": d["title"]} for d in docs],
}
(OUT / "index.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
print(json.dumps({k: v for k, v in stats.items() if k != "documents"}))
