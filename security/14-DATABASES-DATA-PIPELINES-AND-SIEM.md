# Secure data pipelines, SQL, telemetry storage and SIEM integrations

## Storage choices
- SQLite: local analysis and lightweight state; transactional, embedded.
- PostgreSQL: multi-user relational workloads and indexes.
- Search systems: indexed text/event retrieval, operational complexity.
- Columnar files (Parquet): efficient historical analytics.
- Object storage: durable raw records, access controls and retention.
- Message queues: asynchronous ingestion and backpressure.

## Pipeline invariants
Raw input is immutable where practical. Every transformation is reproducible, versioned and traceable. Event IDs support deduplication; timestamps have clear semantics; parser errors are observable. Define schema evolution, retention, encryption and deletion policies.

### SQLite example
```python
import sqlite3
from contextlib import closing
with closing(sqlite3.connect(":memory:")) as conn:
    with conn:
        conn.execute("""CREATE TABLE events (
            event_id TEXT PRIMARY KEY,
            actor TEXT NOT NULL,
            action TEXT NOT NULL
        )""")
        conn.execute(
            "INSERT INTO events VALUES (?, ?, ?)",
            ("lab-001", "alice", "login_failure")
        )
    count = conn.execute(
        "SELECT COUNT(*) FROM events WHERE action = ?", ("login_failure",)
    ).fetchone()[0]
    assert count == 1
```

## SIEM integration
Use least-privilege credentials, pagination, explicit query scopes, retry/backoff, read-only defaults and rate caps. Treat SIEM searches as potentially expensive. Avoid unrestricted export of raw personally identifiable logs. Audit who ran a search and why.

## Exercises
1. Build a schema for normalized events and find all events for a user in a time range.
2. Add a unique event ID and simulate duplicate ingestion.
3. Measure index advantages and costs on synthetic data.
4. Draw a resilient ingest topology with dead-letter queue and replay.
Resources: [SQLite docs](https://www.sqlite.org/docs.html), [Python sqlite3](https://docs.python.org/3/library/sqlite3.html).
