"""Bounded TCP connectivity check for 127.0.0.1 ONLY.

Connectivity is not a vulnerability test. No remote targets are accepted.
"""
from __future__ import annotations

import argparse
import socket
import sys


def check_port(port: int, timeout: float = 0.5) -> bool:
    if not isinstance(port, int) or isinstance(port, bool) or not 1 <= port <= 65535:
        raise ValueError("invalid port")
    if not 0 < timeout <= 5:
        raise ValueError("timeout must be in (0, 5]")
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=timeout):
            return True
    except OSError:
        return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ports", nargs="+", type=int, help="TCP port (1-65535)")
    args = parser.parse_args(argv)
    if len(args.ports) > 16:
        parser.error("at most 16 ports per invocation")
    try:
        for port in args.ports:
            print(f"127.0.0.1:{port} {'reachable' if check_port(port) else 'unreachable'}")
    except ValueError as exc:
        print(f"invalid request: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
