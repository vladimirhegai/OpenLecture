"""Small, reproducible builder for cited ELEC 271 notes."""

import json
import sys
import uuid
from pathlib import Path

import httpx

from open_lecture import digital
from open_lecture.schemas import DocumentCreate

ROOT = Path(__file__).parent
OUT = ROOT / "out"
OUT.mkdir(exist_ok=True)
COURSE = "d0b18428-9c03-4bbf-87af-7a1169d667ab"
API = f"http://127.0.0.1:8000/api/v1/courses/{COURSE}"
CITES = json.loads((OUT / "citations.json").read_text(encoding="utf-8"))
SOURCES = {
    "N": "Lecture 1 Introduction, positional number representation and binary numbers.pdf",
    "L": "Section2_Logic_Circuits.pdf",
    "C": "Chapter3_Implementation_technology Lecture 1.pdf",
    "P1": "ELEC271-PS1_TA.pdf",
    "P1B": "Problem_1b_updated.pdf",
    "P1S": "Problem_set_1_solutions2.pdf",
    "P2": "Problem_set_2.pdf",
    "P2S": "Problem_set_2_solutions.pdf",
    "PQ": "Practice questions chapter 2.pdf",
    "P3": "Problem_set_3_.pdf",
    "P4": "Problem_set_4_.pdf",
    "P5": "Problem_set_5_.pdf",
    "P6": "Problem_set_6_.pdf",
    "P7": "Problem_set_7_.pdf",
    "T": "Tutorial Week 2.pdf",
    "MID": "ELEC_271_Fall2025_Midterm.pdf",
    "FORM": "ELEC 271 Midterm Formula Sheet.pdf",
    "FIG": "ELEC_271_book_figures.pdf",
}


def cite(tag, *pages):
    return [CITES[SOURCES[tag]][str(p)] for p in pages]


def S(text, latex=""):
    return {"explanation": text, "latex": latex}


def node(id, gate, x, y, **kw):
    return dict(id=id, gate=gate, x=x, y=y, **kw)


def wire(start, end, via=None):
    return dict(start=start, end=end, **({"via": via} if via else {}))


def circuit(title, nodes, wires):
    return dict(kind="circuit", title=title, nodes=nodes, wires=wires)


class Doc:
    def __init__(self, number, title, topics):
        self.number = number
        self.title = f"ELEC 271 · {number:02} · {title}"
        self.topics = topics
        self.blocks = []
        self.slug = f"{number:02}"  # file names: out/<slug>.json, notes/ELEC-271-<slug>.md
        self.document_type = "study_notes"

    def add(self, kind, cites=(), **kw):
        self.blocks.append(
            dict(
                type=kind,
                id=str(uuid.uuid5(uuid.NAMESPACE_URL, f"elec271/{self.number}/{len(self.blocks)}")),
                citations=list(cites),
                **kw,
            )
        )

    def H(self, text, cites=()):
        self.add("heading", cites, level=1, text=text)

    def P(self, text, cites=()):
        self.add("paragraph", cites, text=text)

    def E(self, latex, cites=()):
        self.add("equation", cites, latex=latex)

    def T(self, columns, rows, cites=()):
        self.add("table", cites, columns=columns, rows=[[str(c) for c in r] for r in rows])

    def F(self, spec, caption, cites=()):
        self.P(figure(spec, caption), cites)

    def X(self, title, prompt, steps, answer, cites=()):
        self.add("worked_example", cites, title=title, prompt=prompt, steps=steps, answer=answer)

    def Q(self, title, prompt, steps, answer, cites=()):
        self.add(
            "practice_problem",
            cites,
            title=title,
            prompt=prompt,
            steps=steps,
            answer=answer,
            difficulty="intermediate",
            origin="source" if cites else "original",
        )

    def CODE(self, source, cites=()):
        self.add("code", cites, language="vhdl", text=source.strip())

    def LOGICSTEPS(self, title, steps, cites=()):
        self.P(logicsteps(title, steps), cites)

    def STEPS(self, title, steps, cites=()):
        lines = ["```steps", f'title "{title}"']
        for latex, text in steps:
            lines.extend([f"$$ {latex} $$", text])
        self.P("\n".join(lines + ["```"]), cites)

    def save(self):
        slug = self.slug
        payload = dict(
            title=self.title,
            document_type=self.document_type,
            topic_keys=self.topics,
            folder_id="a0ce20ce-b87b-408f-8488-44130e5ce4ea",
            blocks=self.blocks,
            actor="agent",
            idempotency_key=f"elec271-{slug}-v1",
        )
        DocumentCreate.model_validate(payload)
        for b in self.blocks:
            for text in string_values(b):
                assert not any(ord(c) < 32 and c != "\n" for c in text), "control character in note"
                assert text.count("$") % 2 == 0, "unbalanced math delimiters"
        (OUT / f"{slug}.json").write_text(
            json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        # Human-readable copy includes source filenames and pages, as well as clickable app citations.
        chunks = [f"# {self.title}"]
        from export import markdown

        for b in self.blocks:
            chunks.append(markdown(b))
            refs = []
            for c in b["citations"]:
                scope_file = OUT / "midterm-scope.json"
                if scope_file.exists():
                    scope = json.loads(scope_file.read_text(encoding="utf-8"))
                    if "exam" in scope and c["source_id"] == scope["exam"]["source_id"]:
                        refs.append("midterm_scope.md (instructor announcement supplied in chat)")
                for filename, pages in CITES.items():
                    page = next((p for p, ref in pages.items() if ref == c), None)
                    if page:
                        refs.append(f"{filename}, p. {page}")
            if refs:
                chunks.append("*Sources: " + "; ".join(refs) + "*")
        Path(f"notes/ELEC-271-{slug}.md").write_text("\n\n".join(chunks) + "\n", encoding="utf-8")
        print(self.title, len(self.blocks), "blocks")
        if "--publish" in sys.argv:
            self.publish(payload)

    def publish(self, payload):
        api = httpx.Client(base_url=API, timeout=90)
        existing = api.get("/documents?limit=100").json()
        target = getattr(self, "target_document_id", None)
        matches = (
            [d for d in existing if d["document_id"] == target]
            if target
            else [d for d in existing if d["title"] == self.title]
        )
        if target and not matches:
            raise RuntimeError(f"The existing note {target} is missing; refusing to create a duplicate")
        if matches:
            doc = api.get(f"/documents/{matches[0]['document_id']}").json()
            canonical = DocumentCreate.model_validate(payload)
            new_blocks = [b.model_dump(mode="json") for b in canonical.blocks]

            def content(blocks):
                return [{k: v for k, v in b.items() if k != "id"} for b in blocks]

            if content(doc["blocks"]) == content(new_blocks) and doc["title"] == self.title:
                result = doc
            else:
                ops = [{"op": "remove", "block_id": b["id"]} for b in doc["blocks"]]
                prev = None
                for block in self.blocks:
                    block = dict(block, id=str(uuid.uuid4()))
                    ops.append({"op": "insert", "after_id": prev, "block": block})
                    prev = block["id"]
                revision = doc["revision"]
                for offset in range(0, len(ops), 100):
                    r = api.patch(
                        f"/documents/{doc['document_id']}",
                        json={
                            "expected_revision": revision,
                            "actor": "agent",
                            "operations": ops[offset : offset + 100],
                            **({"title": self.title} if offset == 0 else {}),
                        },
                    )
                    r.raise_for_status()
                    result = r.json()
                    revision = result["revision"]
        else:
            r = api.post("/documents", json=payload)
            r.raise_for_status()
            result = r.json()
        (OUT / f"{self.slug}-published.json").write_text(json.dumps(result, indent=2), encoding="utf-8")


def figure(spec, caption):
    """A ```digital fence with its caption; the spec is validated by rendering it."""
    source = json.dumps(spec, ensure_ascii=False, separators=(",", ":"))
    digital.render_svg(source)  # validate and exercise the renderer for every authored figure
    return f"```digital\n{source}\n```\n\n*{caption}*"


def logicsteps(title, steps):
    """A ```logicsteps card: steps are (title, drawing, found_values, notes[, highlight]); changes highlight
    themselves, and `highlight` (node ids, or "pdn"/"pun" for a transistor drawing) adds to them."""
    lines = ["```logicsteps", f'title "{title}"']
    for step_title, spec, values, notes, *focus in steps:
        source = json.dumps(spec, ensure_ascii=False, separators=(",", ":"))
        digital.render_svg(source)
        hl = [f"hl {' '.join(focus[0])}"] if focus else []
        lines += [f"== {step_title}", source, *hl, *(f"#+ {v}" for v in values), "--", notes]
    return "\n".join(lines + ["```"])


def string_values(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from string_values(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from string_values(item)
