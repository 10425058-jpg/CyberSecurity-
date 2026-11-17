"""Read-only file-format hint and entropy report for benign training files.

Format magic is a hint, NOT an antivirus verdict. Reads only a bounded prefix.
"""
from __future__ import annotations

import argparse
from collections import Counter
from math import log2
from pathlib import Path
import json

SIGNATURES = (
    (b"\x89PNG\r\n\x1a\n", "PNG"),
    (b"%PDF-", "PDF"),
    (b"PK\x03\x04", "ZIP"),
    (b"\x7fELF", "ELF"),
    (b"MZ", "MZ / possible PE"),
)


def entropy(data: bytes) -> float:
    if not data:
        return 0.0
    total = len(data)
    return -sum((n / total) * log2(n / total)
                for n in Counter(data).values())


def classify_magic(data: bytes) -> str:
    return next((label for magic, label in SIGNATURES
                 if data.startswith(magic)), "unknown")


def analyze(path: Path, sample_bytes: int = 1_048_576) -> dict:
    if not 1 <= sample_bytes <= 16_777_216:
        raise ValueError("sample_bytes outside allowed range")
    with path.open("rb") as source:
        sample = source.read(sample_bytes)
    return {"file": path.name, "sample_size": len(sample),
            "format_hint": classify_magic(sample),
            "sample_entropy_bits_per_byte": round(entropy(sample), 4),
            "interpretation": "descriptive metadata, not a malware verdict"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    args = parser.parse_args(argv)
    try:
        print(json.dumps(analyze(args.file), indent=2))
        return 0
    except (OSError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    raise SystemExit(main())
