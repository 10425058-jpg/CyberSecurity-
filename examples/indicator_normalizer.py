"""Normalize offline example IP indicators. No network requests are made."""
from __future__ import annotations

import argparse
import ipaddress
import json
import sys
from pathlib import Path
from collections.abc import Iterable, Iterator


def normalize_ip(value: str) -> str:
    if not isinstance(value, str) or len(value) > 64:
        raise ValueError("indicator must be a short IP string")
    try:
        return str(ipaddress.ip_address(value.strip()))
    except ValueError as exc:
        raise ValueError("indicator is not an IP address") from exc


def records(lines: Iterable[str]) -> Iterator[dict]:
    seen: set[tuple[str, str]] = set()
    for number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        if len(line) > 16_384:
            raise ValueError(f"line {number}: too long")
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"line {number}: invalid JSON") from exc
        if not isinstance(obj, dict):
            raise ValueError(f"line {number}: object required")
        source = obj.get("source")
        if not isinstance(source, str) or not 1 <= len(source) <= 128:
            raise ValueError(f"line {number}: invalid source")
        ip = normalize_ip(obj.get("indicator"))
        key = (ip, source)
        if key not in seen:
            seen.add(key)
            yield {"indicator": ip, "type": "ip", "source": source,
                   "confidence": "unverified"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("jsonl", type=Path)
    args = parser.parse_args(argv)
    try:
        with args.jsonl.open("r", encoding="utf-8") as stream:
            for item in records(stream):
                print(json.dumps(item))
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"normalization failed: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
