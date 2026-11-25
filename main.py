"""Micro-confession entry: copy the two-part confession in entry.txt
(a To: line plus the unsent line) byte-for-byte to the grader output
directory, with no transformation, temp file, or rename."""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
try:
    out_dir.mkdir(parents=True, exist_ok=True)
except OSError:
    if not out_dir.is_dir():
        raise
data = (HERE / "entry.txt").read_bytes()
out = out_dir / "entry.txt"
out.write_bytes(data)
os.chmod(out, 0o644)
