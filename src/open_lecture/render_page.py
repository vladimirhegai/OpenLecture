"""Render original PDF pages in a process with a parent-enforced deadline.

python -m open_lecture.render_page FILE PAGE [SIZE [LEFT TOP RIGHT BOTTOM]]
    One page as PNG. SIZE is the long side in pixels; the optional region (fractions 0-1 of the
    page) crops to that part first, so a small region at a large size is a zoom.
python -m open_lecture.render_page FILE --grid FIRST COUNT
    A labelled thumbnail sheet of COUNT pages starting at FIRST.
"""

import sys

import pymupdf

MAX_BYTES = 6 * 1024 * 1024


def page_png(document, number: int, size: int, region=None) -> bytes:
    if number < 1 or number > len(document):
        raise ValueError(f"Page must be between 1 and {len(document)}")
    page = document[number - 1]
    rect = page.rect
    if region:
        left, top, right, bottom = region
        if not (0 <= left < right <= 1 and 0 <= top < bottom <= 1):
            raise ValueError("Region must be fractions 0-1 with left < right and top < bottom")
        rect = pymupdf.Rect(
            rect.x0 + left * rect.width,
            rect.y0 + top * rect.height,
            rect.x0 + right * rect.width,
            rect.y0 + bottom * rect.height,
        )
    scale = size / max(rect.width, rect.height)
    return page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), clip=rect, alpha=False).tobytes("png")


def grid_png(document, first: int, count: int) -> bytes:
    last = min(len(document), first + count - 1)
    if first < 1 or first > len(document):
        raise ValueError(f"First page must be between 1 and {len(document)}")
    numbers = list(range(first, last + 1))
    columns = 4 if len(numbers) > 6 else 3 if len(numbers) > 2 else len(numbers)
    rows = -(-len(numbers) // columns)
    cell_w, cell_h, label = 420, 420, 26
    sheet = pymupdf.open()
    canvas = sheet.new_page(width=columns * cell_w, height=rows * (cell_h + label))
    for index, number in enumerate(numbers):
        x, y = (index % columns) * cell_w, (index // columns) * (cell_h + label)
        page = document[number - 1]
        canvas.insert_text((x + 8, y + 18), f"Page {number}", fontsize=14)
        target = pymupdf.Rect(x + 6, y + label, x + cell_w - 6, y + label + cell_h - 6)
        canvas.draw_rect(target, color=(0.8, 0.8, 0.8), width=0.5)
        canvas.show_pdf_page(target, document, page.number, keep_proportion=True)
    scale = min(1.0, 1800 / canvas.rect.width)
    return canvas.get_pixmap(matrix=pymupdf.Matrix(scale, scale), alpha=False).tobytes("png")


if __name__ == "__main__":
    try:
        with pymupdf.open(sys.argv[1]) as document:
            if sys.argv[2] == "--grid":
                png = grid_png(document, int(sys.argv[3]), int(sys.argv[4]))
            else:
                size = int(sys.argv[3]) if len(sys.argv) > 3 else 1400
                region = [float(v) for v in sys.argv[4:8]] if len(sys.argv) > 7 else None
                png = page_png(document, int(sys.argv[2]), size, region)
            if len(png) > MAX_BYTES:
                raise ValueError("Rendered image exceeds 6 MiB; use a smaller size or region")
            sys.stdout.buffer.write(png)
    except Exception as error:
        sys.stderr.buffer.write(str(error).encode("utf-8"))
        raise SystemExit(1)
