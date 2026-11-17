"""Demonstrate parameterized SQLite queries with synthetic data."""
from __future__ import annotations

import sqlite3
from contextlib import closing


def find_roles(name: str) -> list[str]:
    if not isinstance(name, str) or len(name) > 128:
        raise ValueError("invalid name")
    with closing(sqlite3.connect(":memory:")) as conn:
        with conn:
            conn.execute("CREATE TABLE users (username TEXT, role TEXT)")
            conn.executemany("INSERT INTO users VALUES (?, ?)", [
                ("alice", "reader"),
                ("bob", "analyst"),
            ])
        return [role for (role,) in conn.execute(
            "SELECT role FROM users WHERE username = ?", (name,)
        )]


if __name__ == "__main__":
    print(find_roles("alice"))
    print(find_roles("alice' OR '1'='1"))  # test data only; returns []
