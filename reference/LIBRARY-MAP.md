# Python library and technology map for cybersecurity

This is a map of what to investigate, **not** a requirement to install every package. Review current official docs, compatibility, maintenance and licenses before adoption. Avoid unvetted dependencies and never run tool functionality against unapproved targets.

## Standard library (master these first)
| Module | Security application | Important caution |
|---|---|---|
| `pathlib`, `os`, `shutil` | filesystem inventories | traversal, symlinks, races |
| `sys`, `platform`, `subprocess` | diagnostics and automation | shell injection, privileges |
| `hashlib`, `hmac`, `secrets` | hashes, MACs, CSPRNG | choose correct primitive |
| `ssl`, `socket`, `ipaddress` | TLS, networking, CIDR | certificate/hostname validation |
| `http.client`, `urllib` | HTTP clients | SSRF, redirects, timeouts |
| `json`, `csv`, `tomllib`, `configparser` | data exchange | schema/size validation |
| `re`, `string`, `unicodedata` | parsing | ReDoS, normalization |
| `struct`, `base64`, `binascii` | binary formats | bounds and format confusion |
| `sqlite3` | local event store | parameterize SQL |
| `datetime`, `zoneinfo`, `time` | incident timelines | timezone and clock skew |
| `collections`, `heapq`, `bisect` | counters, priority, streams | capacity bounds |
| `asyncio`, `concurrent.futures`, `threading`, `multiprocessing` | parallel analysis | races/overload |
| `argparse`, `logging` | CLI and diagnostics | never log secrets |
| `unittest`, `doctest`, `unittest.mock` | reproducible tests | mocked ≠ integrated |
| `tempfile`, `contextlib` | safe resource lifecycles | cleanup and permissions |
| `dataclasses`, `typing`, `enum` | robust domain models | annotations not validation |
| `zipfile`, `tarfile` | archive inspection | bombs, traversal, links |
| `ast`, `tokenize` | code analysis | do not use `eval` on untrusted code |
| `statistics`, `math`, `decimal` | analytics | mathematical assumptions |

## Third-party libraries
| Package / ecosystem | Core use | Caveat |
|---|---|---|
| `requests` / `httpx` / `aiohttp` | HTTP API integrations | SSRF, redirects, TLS and resource limits |
| `scapy` / `dpkt` / `pyshark` | packet parsing | untrusted captures; offline first |
| `cryptography` / `argon2-cffi` | vetted crypto and passwords | key/nonce/work-factor policy |
| `pandas` / `numpy` / `pyarrow` / `polars` | large telemetry analysis | memory/privacy |
| `pydantic` / `jsonschema` | input schemas | size/depth constraints |
| `SQLAlchemy` / `psycopg` | database access | authorized queries, least privilege |
| `FastAPI` / `Django` / `Flask` | secure service development | auth/authz not automatic |
| `paramiko` | authorized SSH automation | host key verification |
| `psutil` | local process/resource telemetry | privileges/PID reuse |
| `yara-python` / `pefile` / `lief` | static file analysis | hostile parsers need isolation |
| `volatility3` | memory forensics | lawful acquisitions, integrity |
| `bandit` / `semgrep` / `ruff` | code analysis | false positives and blind spots |
| `pip-audit` / `safety` | dependency advisories | coverage depends on data |
| `pytest` / `hypothesis` / `coverage` | quality & property tests | purposeful test design |
| `boto3` / Azure SDK / Google Cloud SDK | cloud read-only audits | scoped credentials |
| `docker` / Kubernetes Python client | container inventory | socket and cluster privileges |
| `stix2` / `taxii2-client` | intel formatting/exchange | licensing/confidence |
| `elastic-transport` / SIEM SDKs | approved telemetry queries | query cost, privacy |
| `python-evtx` | offline Windows event logs | source consistency |
| `capstone` | disassembly for benign samples | static inference limits |
| `networkx` / `matplotlib` | graph and statistical visualization | avoid misleading charts |

## Ecosystem and platforms to understand
Linux, Windows, TCP/IP, Wireshark, Git/GitHub, Docker, Kubernetes, SQLite, PostgreSQL, OpenTelemetry, SIEM, EDR, SOAR, ATT&CK, Sigma, YARA, STIX/TAXII, CVE, CVSS, SBOM, SLSA, OIDC, OAuth2, WebAuthn, TLS, DNS, Active Directory, Zero Trust, SOC, DFIR and incident response.

## Selection process
1. State the real input/output and threat model.
2. Prefer standard library for small tasks when adequate.
3. Evaluate functionality, maintenance, documented security boundaries, and license.
4. Pin/test dependency versions and track advisories.
5. Keep a small dependency set and restrict installation to a virtual environment.
6. Document operational constraints, access privileges and data protection.
