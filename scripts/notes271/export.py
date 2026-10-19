"""Markdown counterpart of the structured note blocks used in these notes."""


def steps(items):
    return "\n\n".join(
        f"{i}. {s['explanation']}" + (f"\n\n   $${s['latex']}$$" if s.get("latex") else "")
        for i, s in enumerate(items, 1)
    )


def markdown(b):
    t = b["type"]
    if t == "heading":
        return "## " + b["text"]
    if t == "paragraph":
        return b["text"]
    if t == "list":
        return "\n".join((f"{i}. " if b["ordered"] else "- ") + item for i, item in enumerate(b["items"], 1))
    if t == "equation":
        return "$$" + b["latex"] + "$$"
    if t == "code":
        return f"```{b['language']}\n{b['text']}\n```"
    if t == "schematic":
        return f"```schematic\n{b['source']}\n```\n\n*{b.get('caption', '')}*"
    if t == "table":
        return (
            "| "
            + " | ".join(b["columns"])
            + " |\n|"
            + "---|" * len(b["columns"])
            + "\n"
            + "\n".join("| " + " | ".join(r) + " |" for r in b["rows"])
        )
    body = f"**{b['title']}**\n\n{b['prompt']}\n\n"
    solution = steps(b["steps"]) + "\n\n**Answer:** " + b["answer"]
    if t == "practice_problem":
        return body + "<details><summary>Solution</summary>\n\n" + solution + "\n\n</details>"
    return body + solution
