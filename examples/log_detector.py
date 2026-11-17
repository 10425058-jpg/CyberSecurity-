"""Detect threshold crossings in *sorted synthetic* JSONL authentication events.

Outputs review candidates, not proof of an attack. Requires timestamp order.
Input event fields: timestamp (ISO8601 with UTC offset), actor, action.
"""
from __future__ import annotations

import argparse
from collections import deque
from datetime import datetime, timezone, timedelta
import json
import sys
from pathlib import Path
from collections.abc import Iterable, Iterator


def parse_event(line: str) -> tuple[datetime, str, str]:
    if len(line) > 65_536:
        raise ValueError("line exceeds maximum length")
    try:
        obj = json.loads(line)
    except json.JSONDecodeError as exc:
        raise ValueError("invalid JSON") from exc
    if not isinstance(obj, dict):
        raise ValueError("event must be a JSON object")
    ts = obj.get("timestamp")
    actor = obj.get("actor")
    action = obj.get("action")
    if not isinstance(ts, str) or "T" not in ts:
        raise ValueError("timestamp must be ISO8601 datetime")
    try:
        when = datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("invalid timestamp") from exc
    if when.tzinfo is None or when.utcoffset() is None:
        raise ValueError("timestamp must include a timezone")
    if not isinstance(actor, str) or not (1 <= len(actor) <= 128):
        raise ValueError("invalid actor")
    if not isinstance(action, str) or len(action) > 128:
        raise ValueError("invalid action")
    return when.astimezone(timezone.utc), actor, action


def detect(
    lines: Iterable[str], *,
    threshold: int = 3,
    window_seconds: int = 300,
    max_actors: int = 10_000,
) -> Iterator[dict]:
    if threshold < 1 or window_seconds < 1 or max_actors < 1:
        raise ValueError("invalid rule parameters")
    windows: dict[str, deque[datetime]] = {}
    signaled: set[str] = set()
    previous: datetime | None = None
    window = timedelta(seconds=window_seconds)
    for number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            when, actor, action = parse_event(line)
        except ValueError as exc:
            raise ValueError(f"line {number}: {exc}") from exc
        if previous is not None and when < previous:
            raise ValueError(f"line {number}: out-of-order timestamp")
        previous = when
        if action != "login_failure":
            continue
        if actor not in windows and len(windows) >= max_actors:
            raise ValueError("actor cardinality cap exceeded")
        attempts = windows.setdefault(actor, deque())
        while attempts and when - attempts[0] > window:
            attempts.popleft()
        if len(attempts) < threshold - 1:
            signaled.discard(actor)
        attempts.append(when)
        if len(attempts) >= threshold and actor not in signaled:
            signaled.add(actor)
            yield {
                "actor": actor, "failure_count": len(attempts),
                "window_seconds": window_seconds,
                "timestamp_utc": when.isoformat(),
                "classification": "review", "confidence": "rule-only",
            }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("jsonl", type=Path)
    parser.add_argument("--threshold", type=int, default=3)
    parser.add_argument("--window-seconds", type=int, default=300)
    args = parser.parse_args(argv)
    try:
        with args.jsonl.open("r", encoding="utf-8") as stream:
            # Fail before emitting incomplete output when possible in pipelines.
            for alert in detect(stream, threshold=args.threshold,
                                window_seconds=args.window_seconds):
                print(json.dumps(alert))
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"detection failed: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
