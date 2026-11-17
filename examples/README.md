# Runnable examples (local-first)

All examples use synthetic/local data. Most require only the Python standard library. `offline_pcap.py` optionally needs Scapy and works on **offline** user-supplied PCAP files. A reachable TCP port does not imply a vulnerability; entropy does not imply malware; log alerts require human review.

## Commands
```bash
python -m examples.file_manifest fixtures
python -m examples.log_detector fixtures/synthetic-auth.jsonl --threshold 3
python -m examples.local_port_check 80 443 8080
python -m examples.binary_triage fixtures/synthetic-auth.jsonl
python -m examples.indicator_normalizer fixtures/synthetic-indicators.jsonl
python -m examples.sqlite_safety_demo
python -m examples.archive_inspector some-owned-test.zip
python -m unittest discover -s tests -v
```

## Engineering lessons
- Make operations read-only by default.
- Check file/record size, type and valid values before processing.
- Clearly distinguish observations from proof of a security incident.
- Do not scan external systems or upload real evidence.
- Avoid treating these teaching examples as hardened forensic tools or production detectors.
- Keep input fixtures synthetic and documented.
