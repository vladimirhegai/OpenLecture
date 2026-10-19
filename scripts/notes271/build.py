"""Rebuild (and optionally --publish) all nine verified notes in reading order."""

import runpy
from pathlib import Path

from lib import Doc
from midterm import reorganize

# Reuse the verified content builders without publishing their former organization.
originals = {}
save = Doc.save
try:
    Doc.save = lambda self: originals.__setitem__(self.number, self)
    for file in sorted(Path(__file__).parent.glob("0[1-9]_*.py")):
        runpy.run_path(str(file), run_name="__main__")
finally:
    Doc.save = save
for document in reorganize(originals):
    document.save()
