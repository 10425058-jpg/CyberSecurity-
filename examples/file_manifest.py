"""Generate a SHA-256 inventory of ordinary files in a local directory.

Designed for educational snapshots, not race-free forensic acquisition.
Does not follow detected symlinks; ownership and path identity can race.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


def sha256_path(path: Path, chunk_size: int = 1024 * 1024) -> str:
    if chunk_size < 1:
        raise ValueError("chunk_size must be positive")
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def manifest(root: Path, *, limit_files: int = 10_000, max_bytes: int = 100_000_000):
    """Yield relative path, size and SHA-256. Skip symlinks and oversized files."""
    if limit_files < 1 or max_bytes < 0:
        raise ValueError("invalid resource limits")
    if not root.is_dir():
        raise NotADirectoryError(root)
    root = root.resolve()
    count = 0
    for path in sorted(root.rglob("*")):
        if path.is_symlink() or not path.is_file():
            continue
        count += 1
        if count > limit_files:
            raise ValueError("file limit exceeded")
        size = path.stat().st_size
        if size > max_bytes:
            continue
        yield {"path": path.relative_to(root).as_posix(),
               "size": size, "sha256": sha256_path(path)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="owned local directory")
    parser.add_argument("--limit-files", type=int, default=10_000)
    parser.add_argument("--max-bytes", type=int, default=100_000_000)
    args = parser.parse_args(argv)
    try:
        for record in manifest(args.directory, limit_files=args.limit_files,
                               max_bytes=args.max_bytes):
            print(json.dumps(record))
    except (OSError, ValueError) as exc:
        print(f"inventory failed: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
