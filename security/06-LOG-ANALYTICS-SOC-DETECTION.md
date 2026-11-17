# Log analytics, SOC automation and detection engineering

## Telemetry sources
Application, authentication, operating system, endpoint, DNS, HTTP, proxy, firewall, cloud audit and container audit logs. Each has coverage gaps and different trust, delay and retention properties. Syslog, Windows Event Logs, JSONL, CSV, OpenTelemetry formats and vendor APIs require normalization.

## An event schema
```json
{
  "timestamp": "2026-01-01T00:00:00Z",
  "source": "synthetic-auth",
  "actor": "alice",
  "src_ip": "192.0.2.15",
  "action": "login_failure",
  "outcome": "failure",
  "event_id": "example-001"
}
```
Prefer aware UTC timestamps, stable field names, provenance, original-event references and explicit uncertainty. Normalize without deleting evidence. Real log data may have duplicates, clock skew, missing fields and attacker-influenced text.

## Detection approaches
- Signature: known pattern.
- Threshold: repeated failures in a time window.
- Behavioral: deviation from actor/device baseline.
- Correlation: several weak signals joined over time.
- Threat intelligence: contextualize indicators by freshness and confidence.
- Anomaly detection: deviations need investigation, not automatic guilty verdicts.

## A simple frequency rule
```python
from collections import Counter

def identify_bursts(events: list[dict], threshold: int = 5) -> dict[str, int]:
    failures = Counter(
        e.get("actor")
        for e in events
        if e.get("action") == "login_failure" and isinstance(e.get("actor"), str)
    )
    return {actor: count for actor, count in failures.items() if count >= threshold}
```
This is **not** time-window aware. A reliable rule must include time ranges, source integrity, false-positive review and entity normalization.

## Operational practice
Define hypothesis, required data, detection logic, expected benign matches, tests, tuning notes, owner, response playbook and measurable effectiveness. Record coverage, precision, triage latency, data volume, and missed-event paths. Use MITRE ATT&CK as a common technique vocabulary, not a guarantee that rule coverage equals security.

## Python ecosystem
`pandas` for offline analysis, `pyarrow`/Parquet for efficient columns, `re` and `ipaddress` for parsing, `collections` for streaming, `sqlite3` for local state, `elasticsearch` and SIEM SDKs when authorized. All connectors should use scoped, audited API credentials.

## Exercises
1. Detect login bursts from a synthetic JSONL file with a 5-minute window.
2. Add deduplication and clear timezone conversion.
3. Evaluate a rule on 100 benign and 10 intentionally suspicious synthetic events; report precision/recall.
4. Write a SOC runbook: verify → enrich → escalate → contain with human approval.
Resources: [MITRE ATT&CK](https://attack.mitre.org/), [Sigma](https://sigmahq.io/), [OWASP Logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html).
