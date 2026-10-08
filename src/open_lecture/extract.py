"""Bounded parser subprocess. Its stdout is a UTF-8 JSON result, never logging."""

import json
import re
import sys
import zipfile
from pathlib import Path

IMAGES = {".png", ".jpg", ".jpeg", ".webp"}
UNIT = re.compile(r"^(?:[kmMuµnpG]?(?:V|A|W|Ω|Ohm|F|H|S|s|Hz)|ohm|percent|%)(?:\s|$)")


def textbook_index(document, toc):
    """Chapter/section page ranges from the PDF outline, plus numbered end-of-chapter problems."""
    pages = len(document)
    entries = [(level, title.strip(), page) for level, title, page in toc if page >= 1]
    sections, chapter_starts = [], []
    for index, (level, title, start) in enumerate(entries):
        end = pages
        for later_level, _, later_start in entries[index + 1 :]:
            if later_level <= level:
                end = max(start, later_start - 1)
                break
        match = re.match(r"Chapter\s+(\d+)", title)
        if level == 1 and match:
            chapter_starts.append((int(match.group(1)), start, end))
        sections.append({"level": level, "title": title, "start_page": start, "end_page": end})

    def chapter_of(page):
        return next((number for number, start, end in chapter_starts if start <= page <= end), None)

    for section in sections:
        section["chapter"] = chapter_of(section["start_page"])

    problems = []
    for section in sections:
        chapter = section["chapter"]
        if section["level"] != 2 or chapter is None or section["title"] != "Problems":
            continue
        current, last_minor, group = None, 0, None
        for page_number in range(section["start_page"], section["end_page"] + 1):
            for line in document[page_number - 1].get_text().splitlines():
                stripped = line.strip()
                header = re.match(r"^Sections?\s+(\d+\.\d+.*)$", stripped)
                if header:
                    group = "Section " + header.group(1)
                    continue
                match = re.match(r"^(\d{1,2})\.(\d{1,3})\s+(.*)$", stripped)
                if (
                    match
                    and int(match.group(1)) == chapter
                    and last_minor < int(match.group(2)) <= last_minor + 4
                    and not UNIT.match(match.group(3))
                    and match.group(3)[:1].isalpha()
                ):
                    current = {
                        "chapter": chapter,
                        "number": f"{chapter}.{int(match.group(2))}",
                        "kind": "end_of_chapter",
                        "section": group,
                        "page": page_number,
                        "text": match.group(3),
                    }
                    problems.append(current)
                    last_minor = int(match.group(2))
                elif current and current["page"] >= page_number - 1 and len(current["text"]) < 900:
                    if (
                        stripped
                        and stripped not in {"PSPICE", "MULTISIM"}
                        and not stripped.startswith("Figure")
                    ):
                        current["text"] += " " + stripped
    return {"sections": sections, "problems": problems}


def extract(path: Path, max_chars: int, textbook: bool = False):
    suffix = path.suffix.lower()
    sections = []
    page_count = None
    index = None
    if suffix == ".pdf" or suffix in IMAGES:
        import pymupdf

        with pymupdf.open(path) as document:
            if document.needs_pass or len(document) > 2000:
                raise ValueError("Encrypted PDFs and PDFs over 2000 pages are not supported")
            page_count = len(document)
            total = 0
            for number, page in enumerate(document, 1):
                text = page.get_text() if suffix == ".pdf" else ""
                total += len(text)
                if total > max_chars:
                    raise ValueError("Extracted text exceeds configured limit")
                sections.append((number, None, text, "pymupdf"))
            if textbook and suffix == ".pdf":
                index = textbook_index(document, document.get_toc())
    elif suffix in {".docx", ".pptx"}:
        with zipfile.ZipFile(path) as archive:
            if sum(info.file_size for info in archive.infolist()) > 50 * 1024 * 1024:
                raise ValueError("Office archive expands beyond 50 MiB")
        if suffix == ".docx":
            from docx import Document

            document = Document(path)
            heading = None
            for paragraph in document.paragraphs:
                if paragraph.style and paragraph.style.name.startswith("Heading"):
                    heading = paragraph.text
                sections.append((None, heading, paragraph.text, "python-docx"))
            for table in document.tables:
                sections.append(
                    (
                        None,
                        "Table",
                        "\n".join(" | ".join(cell.text for cell in row.cells) for row in table.rows),
                        "python-docx",
                    )
                )
        else:
            from pptx import Presentation

            for number, slide in enumerate(Presentation(path).slides, 1):
                sections.append(
                    (
                        number,
                        None,
                        "\n".join(shape.text for shape in slide.shapes if shape.has_text_frame),
                        "python-pptx",
                    )
                )
    else:
        text = path.read_text(encoding="utf-8-sig")
        heading = None
        for paragraph in re.split(r"\n\s*\n", text):
            match = re.match(r"^#{1,6}\s+(.+)", paragraph)
            if match:
                heading = match.group(1)
            sections.append((None, heading, paragraph, "utf8"))
    if page_count is None and suffix == ".pptx":
        page_count = len(sections)
    if sum(len(part[2]) for part in sections) > max_chars:
        raise ValueError("Extracted text exceeds configured limit")
    chunks = []
    for page, section, text, method in sections:
        text = text.strip()
        start = 0
        while start < len(text):
            end = min(start + 1800, len(text))
            if end < len(text):
                boundary = text.rfind(" ", start + 1200, end)
                if boundary != -1:
                    end = boundary
            chunk = text[start:end].strip()
            if chunk:
                chunks.append({"page": page, "section": section, "text": chunk, "method": method})
            start = end
    return {"page_count": page_count, "chunks": chunks, "textbook": index}


if __name__ == "__main__":
    try:
        result = extract(Path(sys.argv[1]), int(sys.argv[2]), "--textbook" in sys.argv[3:])
        sys.stdout.buffer.write(json.dumps(result, ensure_ascii=False).encode("utf-8"))
    except Exception as error:
        sys.stderr.buffer.write(str(error).encode("utf-8"))
        raise SystemExit(1)
