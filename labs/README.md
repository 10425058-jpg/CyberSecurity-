# Practical labs — isolated, authorized, reproducible

**Preflight for every lab:** scope is your own device/VM, 127.0.0.1, or the provided synthetic fixture; no external probing. Record Python/OS versions, input hashes, exact commands, observed behavior, test results and limitations. Use a new `.venv` for optional packages.

## Lab 01 — Local environment, 45–90 minutes
**Concepts:** interpreter, venv, imports, shell, Git.
1. Run `python --version` and `python -m venv .venv`.
2. Activate the venv and run `python -m unittest discover -s tests -v`.
3. Print current UTC time with a timezone-aware `datetime`.
4. Document Python and OS versions.
**Deliverable:** environment report and test output.
**Success:** zero failed tests and a reproducible setup.

## Lab 02 — Files and hashes, 1–2 hours
**Concepts:** `pathlib`, chunks, SHA-256, evidence integrity.
1. Execute `python -m examples.file_manifest fixtures`.
2. Save its JSONL stdout; compare each file's digest via another trusted command.
3. Copy a fixture to a temporary directory, change one byte and recompute.
4. Document what the hash can and cannot establish.
**Success:** changed content produces a different digest; you explain collisions/authenticity nuances.

## Lab 03 — Structured log detection, 2–3 hours
**Concepts:** JSONL, timezone-aware datetime, deque, streaming.
1. Inspect `fixtures/synthetic-auth.jsonl`.
2. Run `python -m examples.log_detector fixtures/synthetic-auth.jsonl --threshold 3`.
3. Change threshold to 5 and compare outputs.
4. Create a malformed copy and verify a clear nonzero exit with line number.
5. Study how out-of-order events, huge actor counts and clock skew change validity.
**Success:** correct bounded alerts and documented limitations.

## Lab 04 — Local network-only checks, 1–2 hours
**Concepts:** TCP connect, timeouts, service identity.
1. In an isolated local shell start `python -m http.server 8765 --bind 127.0.0.1`.
2. In a second shell run `python -m examples.local_port_check 8765 8766`.
3. Stop the server and rerun.
4. Explain why reachability != secure service or vulnerability.
**Success:** results change with the local service and errors do not hang.

## Lab 05 — Binary introspection, 1–2 hours
**Concepts:** signatures, entropy, sampling.
1. Run `python -m examples.binary_triage fixtures/synthetic-auth.jsonl`.
2. Create two harmless local files (repeated ASCII bytes vs compressed data).
3. Compare entropy and file-magic classification.
4. Explain why entropy is not a malware verdict.
**Success:** write a read-only triage report with caveats.

## Lab 06 — Safer SQLite, 1–2 hours
**Concepts:** parameterized SQL, schema, transactions.
1. Run `python -m examples.sqlite_safety_demo`.
2. Read `tests/test_examples.py`'s parameterization check.
3. Add tests for empty strings and long names.
4. Write a per-document ownership SQL query for an invented local schema.
**Success:** code treats injection-looking strings as ordinary data.

## Lab 07 — Offline threat indicator enrichment, 1–2 hours
**Concepts:** IP normalization, dedup, provenance.
1. Run `python -m examples.indicator_normalizer fixtures/synthetic-indicators.jsonl`.
2. Add malformed IPs and verify validation failures.
3. Extend normalization with an "observed_utc" field.
4. Add expiry and freshness checks; do not call remote reputation APIs.
**Success:** provenance preserved and no false certainty of compromise.

## Lab 08 — Archive metadata safety, 1–2 hours
**Concepts:** path traversal, expansion bombs, resource caps.
1. Create your own small ZIP with a normal file using `zipfile`.
2. Run `python -m examples.archive_inspector your-test.zip`.
3. Add a harmless entry named `../outside.txt` **without extracting**.
4. Verify the inspector flags it, then delete your toy archive.
**Success:** can explain why detecting suspicious names is not a complete safe extractor.

## Lab 09 — Offline PCAP analysis, 2–3 hours
**Concepts:** packet layers, TCP, Scapy.
1. In an isolated lab, generate traffic to your own 127.0.0.1 server.
2. Capture it with a separately authorized capture tool, export a PCAP.
3. Optionally install Scapy and run `python -m examples.offline_pcap your-lab.pcap`.
4. Compare counts with Wireshark; explain capture gaps.
**Success:** report frame/transport statistics without claiming to read TLS plaintext.

## Lab 10 — Defensive software assurance, 2–4 hours
**Concepts:** source review, tests, supply-chain hygiene.
1. Run `python -m unittest discover -s tests -v` and `python -m compileall examples`.
2. Optionally install `bandit`, `ruff`, `pip-audit` in a venv; review their documentation before use.
3. Run appropriate static analysis and triage findings.
4. Write a concise change proposal and regression test for one genuine improvement.
**Success:** distinguish scanner signal from proof and maintain a testable patch.

## Further labs (design your own)
11. Local event normalization from synthetic Windows/Linux records.
12. Clock skew and late-arrival simulation.
13. Bounded asynchronous local HTTP health checker.
14. Detection precision/recall evaluation with labeled examples.
15. Approved read-only mock cloud inventory and finding report.
16. Digital forensics evidence manifest and chain-of-custody template.
17. Local API with per-resource access controls.
18. AEAD encrypt/decrypt with harmless notes and negative tests.
19. Synthetic SIEM data ingestion to SQLite with deduplication.
20. Final mini SOC capstone with tests, metrics and a written response playbook.

**Lab report template:** title; objective; authorization scope; environment; input description/hash; procedure; observed evidence; test results; false positives/limitations; cleanup; next improvements.
