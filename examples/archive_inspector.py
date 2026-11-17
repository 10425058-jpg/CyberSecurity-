"""Check ZIP metadata for path traversal and resource warning signs.

Read-only. Does not extract files. This is NOT a comprehensive archive scanner.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
import zipfile


def suspicious_name(name: str) -> bool:
    normalized = name.replace("\\", "/")
    path = PurePosixPath(normalized)
    return (path.is_absolute()
            or ".." in path.parts
            or "\x00" in normalized
            or (len(normalized) >= 2 and normalized[1] == ":"))


def inspect_zip(path: Path, max_entries: int = 1_000) -> list[dict]:
    if max_entries < 1:
        raise ValueError("max_entries must be positive")
    warnings: list[dict] = []
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        if len(infos) > max_entries:
            raise ValueError("entry count exceeds limit")
        for info in infos:
            reasons = []
            if suspicious_name(info.filename):
                reasons.append("unsafe-path")
            if info.file_size > 100_000_000:
                reasons.append("large-uncompressed-size")
            if info.compress_size and info.file_size > 1000 * info.compress_size:
                reasons.append("extreme-compression-ratio")
            if reasons:
                warnings.append({"entry": info.filename, "reasons": reasons})
    return warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("zipfile", type=Path)
    args = parser.parse_args(argv)
    try:
        print(json.dumps(inspect_zip(args.zipfile), indent=2))
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
