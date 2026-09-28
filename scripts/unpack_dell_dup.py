#!/usr/bin/env python3
import gzip, io, tarfile, sys
from pathlib import Path

src = Path(sys.argv[1])
out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("extracted")
data = src.read_bytes()
off = data.find(b"\x1f\x8b")
if off < 0:
    raise SystemExit("gzip member not found")
tar_bytes = gzip.decompress(data[off:])
with tarfile.open(fileobj=io.BytesIO(tar_bytes), mode="r:") as tf:
    for m in tf.getmembers():
        if m.isfile():
            dest = out / m.name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(tf.extractfile(m).read())
print("Extracted:", out)
