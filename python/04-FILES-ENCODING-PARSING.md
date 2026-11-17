# 04 — Files, binary data, parsing and evidence hygiene

## File handling
Use `pathlib.Path` and context managers. Text and bytes are different: `read_text(encoding="utf-8")`, `read_bytes()`, streaming with `open(..., encoding="utf-8")`. Ensure you have permission and avoid modifying originals when processing forensic artifacts.

```python
from pathlib import Path
import hashlib

def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(chunk_size), b""):
            digest.update(block)
    return digest.hexdigest()
```
A digest supports integrity checks but **does not by itself prove who created the file**, nor whether it is malicious.

## Structured formats
- JSON / JSON Lines: `json.loads`, `json.dumps`. Validate expected keys and types; avoid loading unbounded files into memory.
- CSV: `csv.DictReader` with explicit encoding and newline handling. CSV formula injection is a concern when exporting data for spreadsheets; escape cells that start with formula-like prefixes according to consumer requirements.
- INI: `configparser`; TOML: `tomllib` (read-only); XML: use hardened parsers when handling untrusted XML and heed entity/expansion risks.
- YAML: if using PyYAML, `yaml.safe_load` instead of loading arbitrary Python objects. Even safe parsers require size/depth limits.
- Archives: beware zip-slip path traversal, symlinks, decompression bombs, and file-name ambiguity. Do not blindly extract third-party archives.

## Reading timestamps
Log timestamps may have missing offsets, daylight-saving ambiguity, or inconsistent clocks. Convert aware times to UTC, retain source timezone/precision, and record collection time separately.

```python
from datetime import datetime, timezone
when = datetime.fromisoformat("2026-01-05T12:00:00+07:00")
utc = when.astimezone(timezone.utc)
assert utc.utcoffset().total_seconds() == 0
```

## Bytes and binary analysis
`bytes`, `bytearray`, `memoryview`, `struct.pack/unpack`, `int.from_bytes`, Base64, hex, endianness and offsets are foundational for packets, executables and artifacts. Base64 is **encoding, not encryption**.

```python
import struct
header = struct.pack("!HI", 443, 1024)  # network-endian unsigned short + int
port, length = struct.unpack("!HI", header)
assert (port, length) == (443, 1024)
```

## Reliable parser checklist
1. Restrict maximum file size and record length.
2. Parse without executing data.
3. Check types and bounds.
4. Normalize only when doing so preserves intended semantics.
5. Record malformed rows separately, without silently discarding evidence.
6. Emit structured reports with hashes and tool versions.
7. Test empty, corrupt, truncated, duplicated and hostile inputs.

## Exercises
- Hash a 1 GB synthetic file using constant memory.
- Stream JSONL records, count parse errors, retain line numbers.
- Parse a simple 6-byte binary header and reject truncated headers.
- Explain why file hash, timestamp, custody record, and source metadata play different roles.
