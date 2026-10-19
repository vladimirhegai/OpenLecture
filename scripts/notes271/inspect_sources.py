"""Extract page text and contact sheets for visual review of the supplied course PDFs."""

import hashlib
import json
from pathlib import Path

import fitz

SOURCE = Path(r"C:\Users\vladh\Downloads\271 - Digital Systems")
OUT = Path("tmp/notes271")
OUT.mkdir(parents=True, exist_ok=True)
seen = {}
manifest = []
for file in sorted(SOURCE.glob("*.pdf")):
    digest = hashlib.sha256(file.read_bytes()).hexdigest()
    if digest in seen:
        manifest.append({"filename": file.name, "duplicate_of": seen[digest], "sha256": digest})
        continue
    seen[digest] = file.name
    tag = f"s{len(seen):02}"
    doc = fitz.open(file)
    manifest.append({"tag": tag, "filename": file.name, "pages": len(doc), "sha256": digest})
    text = "\n\n".join(f"=== PAGE {i + 1} ===\n{p.get_text()}" for i, p in enumerate(doc))
    (OUT / f"{tag}.txt").write_text(text, encoding="utf-8")
    # Six pages per sheet; original page numbers are printed above each thumbnail.
    for start in range(0, len(doc), 6):
        sheet = fitz.open()
        canvas = sheet.new_page(width=1200, height=1500)
        for offset in range(min(6, len(doc) - start)):
            i = start + offset
            x, y = (offset % 2) * 600, (offset // 2) * 500
            canvas.insert_text((x + 10, y + 18), f"{tag} | page {i + 1}", fontsize=15)
            canvas.show_pdf_page(fitz.Rect(x + 5, y + 25, x + 595, y + 495), doc, i)
        canvas.get_pixmap(matrix=fitz.Matrix(1.3, 1.3)).save(OUT / f"{tag}-{start + 1:03}.png")
    print(tag, len(doc), file.name)
(OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
