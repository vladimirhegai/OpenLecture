"""Persist page notes for raster-only pages actually reviewed visually, then refresh citations."""

import json
from pathlib import Path

from open_lecture.config import Settings
from open_lecture.workspace import Workspace

course = "d0b18428-9c03-4bbf-87af-7a1169d667ab"
ws = Workspace(Settings(agent_runner=False))
try:
    sources = ws.list_sources(course, 100)
    source = next(s for s in sources if s["filename"] == "ELEC_271_Fall2025_Midterm.pdf")
    ws.store_page_notes(
        course,
        source["id"],
        1,
        {
            2: "Visually reviewed raster page. Q1: f(x1,x2,x3)=sum m(2,3,4,6,7). Find canonical SOP, minimum SOP, and NAND-only circuit. The solution derives f=x2+x1 NOT(x3). Its NAND circuit uses NAND(x2,x2), NAND(x3,x3), NAND(x1,NOT(x3)), and a final NAND of the two complemented product terms. K-maps are permitted in this past-paper question.",
            3: "Visually reviewed raster page. Q2(a): convert decimal 14.3125 to binary; answer 1110.0101. Q2(b): binary equivalent of 2/3 to four fractional places, convert back to decimal and find closeness. Repeated doubling gives .1010, which is 0.625; absolute truncation error 2/3-5/8=1/24, about 0.04167.",
        },
    )
    result = {}
    for s in sources:
        pages = {}
        for offset in range(0, 500, 100):
            chunks = ws.read_source(course, s["id"], None, 100, offset)["chunks"]
            for c in chunks:
                if c["page"] and str(c["page"]) not in pages:
                    pages[str(c["page"])] = {
                        "source_id": s["id"],
                        "version": s["current_version"],
                        "chunk_id": c["id"],
                    }
            if len(chunks) < 100:
                break
        result[s["filename"]] = pages
    Path("scripts/notes271/out/citations.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
finally:
    ws.close()
