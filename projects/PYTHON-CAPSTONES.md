# Python for Cybersecurity — project ladder and capstones

Each project must be confined to owned test data, published with synthetic fixtures, and include tests, safe defaults, requirements, README, limitations and an operational threat model.

## Level 1 — beginner (1–3 weeks each)
**P1. File integrity inventory:** walk an approved directory, hash files incrementally, emit JSONL, compare snapshots without altering originals. Edge cases: symlinks, unreadable files, file changes during hashing and huge files.

**P2. Offline login log reviewer:** parse sorted JSONL, validate fields and timestamps, apply five-minute threshold with bounded memory, emit review alerts. Edge cases: malformed records, clock skew, unknown action, duplicate events, huge actor cardinality.

**P3. IP indicator normalizer:** verify IPv4/IPv6, dedup by source and preserve confidence. Edge cases: text encoding, untrusted provenance, IPv6 normalization and expired records.

## Level 2 — intermediate (3–6 weeks each)
**P4. Secure local asset inventory dashboard:** SQLite-backed local data and API; object-level authorization tests; optional HTML frontend; safe error handling. No live fleet agents.

**P5. PCAP summarizer (offline):** enumerate protocols/flows from pre-approved synthetic capture and compare with Wireshark; bounded packet count, encryption-aware reporting, performance benchmark.

**P6. Security audit CLI framework:** pluggable *read-only* local checks, typed config, dry-run and JSON output; prevent dangerous plugins by explicit trusted-code policy.

**P7. Incident timeline generator:** ingest two different synthetic log formats, normalize clocks, preserve provenance and emit chronology with uncertainty notes.

## Level 3 — advanced (6–12+ weeks each)
**P8. Mini SOC platform (recommended):**
- Components: ingest from offline JSONL → schema validation → immutable raw reference → normalization → deduplication → bounded queues → correlation → review alerts → analyst notes → reports.
- Threat model: attacker-controlled event fields, path traversal, high-cardinality actors, misleading timestamps, sensitive payloads and compromised dependencies.
- Required detections: failed-login bursts, newly observed source/actor pair, improbable repeated events in a narrow window (synthetic-only assumptions).
- Evaluation: labeled synthetic baseline, precision, recall, false-positive examples, memory and latency bounds.
- Delivery: diagrams, documented data contract, test suite, CI, demo, runbook and postmortem exercise.

**P9. Safe dependency inventory and advisory correlator:** import synthetic SBOM, normalize package versions, compare with downloaded/curated *offline* advisory sample, prioritize by exposure and availability of remediation. No opportunistic Internet scanning.

**P10. Offline forensics workbench:** hash manifest, file-type hints, bounded entropy, timestamp timeline, evidence notes and exportable report. Ensure you are clear about the distinction between educational artifact analysis and forensic-grade acquisition.

**P11. Cloud posture audit using mocks:** create a mock AWS/Azure/GCP inventory and policy rules; return explanatory findings with zero cloud credentials; later design (do not default to) real read-only SDK integrations.

## Recommended repository layout for student capstone
```text
mini-soc/
  README.md
  pyproject.toml
  src/minisoc/{models,parsers,ingest,rules,report,cli}.py
  tests/{test_parsers,test_rules,test_ingest}.py
  fixtures/synthetic-events.jsonl
  docs/{architecture,threat-model,runbook,results}.md
```

## Acceptance criteria
1. Reproducible setup, explicit Python version and documented dependencies.
2. Every parser rejects malformed inputs predictably and enforces limits.
3. Strong test coverage of critical logic; no network required for test suite.
4. Least privilege, no secrets or real personal data, clear authorization.
5. Error paths and cancellation are documented and tested.
6. Honest precision/recall or a justified reason metrics do not apply.
7. One-page executive summary understandable by a non-developer.
8. An explicit list of what is **not** secure/production ready.

## Portfolio write-up
Problem → scope and threat model → architecture → Python design choices → tests → measurements → false positives and limitations → hardening backlog → responsible demo.
