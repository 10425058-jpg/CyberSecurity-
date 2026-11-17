# Digital forensics and incident response (DFIR)

## Lifecycle and standards
Use [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) (April 2025) together with organizational policies. Preparation, governance and protection support effective detection, response and recovery. The older Rev. 2 lifecycle remains common in legacy material but has been superseded.

## Evidence handling
- Obtain authority to access evidence.
- Record system identity, collector, UTC time, acquisition method, tool version, and hash.
- Preserve originals; analyze verified copies; maintain access and chain-of-custody records.
- Know the difference between live response (volatile state) and offline imaging.
- Recognize that time sources, filesystem metadata and logs can be forged or inaccurate.
- Keep private data out of public issue trackers and coursework repos.

## Python DFIR tasks
Filesystem timeline construction, evidence hashing, CSV/JSON event normalization, authorized process inventory, browser artifact parsing from sanitized copies, packet analysis and timeline correlation. Binary file formats require exact schema parsing, bounds checks and version awareness.

```python
from pathlib import Path
from datetime import datetime, timezone
import hashlib

def manifest_entry(path: Path) -> dict:
    stat = path.stat()
    with path.open("rb") as stream:
        digest = hashlib.file_digest(stream, "sha256").hexdigest()
    return {
        "path": str(path), "size": stat.st_size,
        "modified_utc": datetime.fromtimestamp(
            stat.st_mtime, timezone.utc
        ).isoformat(),
        "sha256": digest,
    }
```
The example relies on `hashlib.file_digest`, available on supported modern Python versions; streaming with `hashlib.sha256().update` is a portable alternative.

## Timeline pitfalls
File `mtime`, `ctime` and birth time have platform-dependent semantics; distinguish event time, ingest time and modification time. Always preserve original timestamp and timezone, and document uncertainty.

## Reporting
Executive summary → scope/authority → observed facts → evidence table → timeline → assessment (confidence and alternatives) → actions taken → impact → remediation → lessons learned. Avoid presenting correlation as proof of cause.

## Exercises
1. Produce a hash manifest for synthetic incident files and verify unchanged copies.
2. Merge two event streams with distinct time zones into one UTC timeline.
3. Record chain of custody for a lab VM snapshot.
4. Explain why acquiring RAM and shutting down a device can conflict.
Resources: [NIST incident response](https://csrc.nist.gov/pubs/sp/800/61/r3/final), [SANS DFIR](https://www.sans.org/digital-forensics-incident-response/).
