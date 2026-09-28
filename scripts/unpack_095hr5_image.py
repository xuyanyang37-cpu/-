#!/usr/bin/env python3
from pathlib import Path
import sys

src = Path(sys.argv[1])
dst = Path(sys.argv[2])
b = src.read_bytes()

# Identified for the 00.3D.67 payload.
start = 0x104
end = min(0x10004, len(b))
records = b[start:end]

if len(records) % 4:
    raise SystemExit("record region is not 4-byte aligned")

out = bytearray()
for i in range(0, len(records), 4):
    r = records[i:i+4]
    if r[0] != 0:
        raise SystemExit(f"unexpected record prefix at 0x{start+i:x}: {r.hex()}")
    out += r[1:4]

dst.write_bytes(out)
print(f"{len(out)} packed bytes written to {dst}")
