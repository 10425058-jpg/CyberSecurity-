"""Summarize a user-provided local PCAP without live capture.

Optional dependency: pip install scapy. Handle only approved synthetic PCAPs.
"""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path


def summarize(path: Path, limit: int = 100_000) -> dict:
    if not 1 <= limit <= 1_000_000:
        raise ValueError("invalid packet limit")
    try:
        from scapy.all import IP, IPv6, TCP, UDP, PcapReader
    except ImportError as exc:
        raise RuntimeError("Install optional package: python -m pip install scapy") from exc
    counts: Counter[str] = Counter()
    total = 0
    with PcapReader(str(path)) as capture:
        for packet in capture:
            total += 1
            if total > limit:
                break
            if IP in packet:
                counts["IPv4"] += 1
            if IPv6 in packet:
                counts["IPv6"] += 1
            if TCP in packet:
                counts["TCP"] += 1
            if UDP in packet:
                counts["UDP"] += 1
    return {"packets_examined": min(total, limit),
            "truncated_at_limit": total > limit,
            "protocol_counts": dict(counts)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pcap", type=Path)
    args = parser.parse_args(argv)
    try:
        print(summarize(args.pcap))
        return 0
    except (OSError, RuntimeError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    raise SystemExit(main())
