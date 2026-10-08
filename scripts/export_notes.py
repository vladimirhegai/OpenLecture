"""Write every note as Markdown under notes/ (readable on GitHub, no app needed).

    uv run python scripts/export_notes.py
"""

import re
from pathlib import Path

from open_lecture.config import Settings
from open_lecture.workspace import Workspace


def steps(items):
    return "\n".join(f"{i}. {s['explanation']}" + (f"\n\n   $${s['latex']}$$" if s.get("latex") else "") for i, s in enumerate(items, 1))


def block(b):
    t = b["type"]
    if t == "heading":
        return "#" * (b["level"] + 1) + " " + b["text"]
    if t in ("paragraph",):
        return b["text"]
    if t == "callout":
        return "> **" + b["tone"].title() + ":** " + b["text"].replace("\n", "\n> ")
    if t == "equation":
        return f"$${b['latex']}$$"
    if t == "list":
        return "\n".join((f"{i}. " if b["ordered"] else "- ") + x for i, x in enumerate(b["items"], 1))
    if t == "table":
        head = "| " + " | ".join(b["columns"]) + " |\n|" + "---|" * len(b["columns"])
        return head + "\n" + "\n".join("| " + " | ".join(c.replace("\n", " ") for c in r) + " |" for r in b["rows"])
    if t == "derivation":
        return f"**{b['title']}**\n\n{steps(b['steps'])}"
    if t == "worked_example":
        return f"**Example: {b['title']}**\n\n{b['prompt']}\n\n{steps(b['steps'])}\n\n**Answer:** {b['answer']}"
    if t == "practice_problem":
        body = steps(b["steps"]) if b.get("steps") else b.get("solution", "")
        return f"**Problem: {b.get('title', '')}** ({b['difficulty']})\n\n{b['prompt']}\n\n<details><summary>Solution</summary>\n\n{body}\n\n**Answer:** {b.get('answer', '')}\n\n</details>"
    if t == "schematic":
        return f"```schematic\n{b['source']}\n```"
    if t == "code":
        return f"```{b['language']}\n{b['text']}\n```"
    return ""


def main():
    ws = Workspace(Settings(agent_runner=False))
    out = Path("notes")
    out.mkdir(exist_ok=True)
    for course in ws.list_courses():
        for summary in ws.find_documents(course["id"], "", None, None, None, False, 200, 0):
            doc = ws.read_document(course["id"], summary["document_id"])
            name = re.sub(r"[^\w\- ]+", "", doc["title"]).strip().replace(" ", "-")
            text = f"# {doc['title']}\n\n" + "\n\n".join(filter(None, (block(b) for b in doc["blocks"]))) + "\n"
            (out / f"{name}.md").write_text(text, encoding="utf-8", newline="\n")
            print("wrote", out / f"{name}.md")


main()
