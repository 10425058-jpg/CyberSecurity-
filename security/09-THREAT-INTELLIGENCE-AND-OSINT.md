# Threat intelligence, OSINT and privacy-respecting enrichment

## Intelligence concepts
Data → information → analyzed intelligence → decision. IOC (IP/domain/hash), behavior, TTP, actor/campaign hypothesis and vulnerability are different artifacts. Attributes include source, collection time, confidence, expiration, classification, license and permitted sharing.

## Python ingestion pipeline
Fetch authorized feeds with API keys kept outside source, validate JSON schemas, normalize domains/IPs/hashes, deduplicate, assign TTL/confidence, enrich against internal approved data, and produce traceable reports. Treat external feeds as adversarial inputs: supply-chain poisoning and stale indicators cause false positives.

```python
import ipaddress
from datetime import datetime, timezone

def normalize_indicator(value: str) -> str:
    return str(ipaddress.ip_address(value.strip()))

record = {
    "indicator": normalize_indicator("192.0.2.4"),
    "type": "ip",
    "source": "synthetic-example",
    "observed_utc": datetime.now(timezone.utc).isoformat(),
    "confidence": "unverified",
}
```

## OSINT ethics
Public availability does not automatically mean unrestricted collection or republication. Respect privacy law, rate limits, robots/policy constraints, copyright, and research purpose. Avoid doxxing or harvesting private personal information.

## Standards and contexts
STIX 2.x defines structured threat intelligence; TAXII is an exchange API ecosystem; MITRE ATT&CK models observed adversary tactics/techniques, not every possible action. CVE identifies publicly disclosed vulnerabilities; CVSS severity is not identical to contextual business risk.

## Exercises
1. Normalize synthetic IPv4 and IPv6 indicators with strong validation.
2. Build a deduplication pipeline that preserves source/provenance.
3. Assign expiry dates to ephemeral indicators; explain stale-data risk.
4. Map a hypothetical defensive detection to a technique and evidence source.
Resources: [OASIS CTI](https://oasis-open.github.io/cti-documentation/), [MITRE ATT&CK](https://attack.mitre.org/), [CVE](https://www.cve.org/).
