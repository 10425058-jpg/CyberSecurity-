# Python for Cybersecurity — A Complete Learning Handbook (English)

**From Python zero to defensive security engineering.** This open learning repository teaches the language, software engineering, and Python's applications to cybersecurity through chapters, offline exercises, readable code, local labs, tests, and progressive capstones.

> **Safety:** Operate only on systems, traffic and data you own or have explicit written permission to assess. The repository uses synthetic data and loopback-first examples. Tools are educational, not production-hardened scanners or forensic acquisition systems.

## Choose your entry point
| Your background | Begin here | Then |
|---|---|---|
| New to Python | [Start Here](python/00-START-HERE.md) → [Foundations](python/01-LANGUAGE-FOUNDATIONS.md) | Complete all `python/` chapters |
| Know some Python | [Python index](reference/CHAPTER-INDEX.md) | [Security modules](security/00-SAFETY-THREAT-MODELING.md) |
| Know Linux and networking | [Networking with Python](security/01-NETWORKING-AND-SOCKETS.md) | [SOC detection](security/06-LOG-ANALYTICS-SOC-DETECTION.md) |
| Prefer building | [Runnable examples](examples/README.md) | [Labs](labs/README.md) and [capstones](projects/PYTHON-CAPSTONES.md) |
| Need a schedule | [Study plan](reference/LEARNING-PLAN.md) | [Skills checklist](reference/SKILLS-CHECKLIST.md) |

## The handbook
**Python fundamentals:** [01](python/01-LANGUAGE-FOUNDATIONS.md) language, [02](python/02-DATA-STRUCTURES-ALGORITHMS.md) collections/complexity, [03](python/03-FUNCTIONS-MODULES-TYPING.md) functions/typing, [04](python/04-FILES-ENCODING-PARSING.md) files/bytes, [05](python/05-EXCEPTIONS-TESTING-DEBUGGING.md) testing, [06](python/06-OOP-AND-ARCHITECTURE.md) OOP, [07](python/07-ITERATORS-ASYNC-FOUNDATIONS.md) iterators, [08](python/08-CONCURRENCY-AND-ASYNCIO.md) concurrency, [09](python/09-OS-AND-AUTOMATION.md) OS automation, [10](python/10-CLI-PACKAGING-DEPENDENCIES.md) packaging/CLI, [11](python/11-INTERNALS-PERFORMANCE-ADVANCED.md) advanced.

**Cybersecurity:** [00](security/00-SAFETY-THREAT-MODELING.md) threat modeling, [01](security/01-NETWORKING-AND-SOCKETS.md) networks, [02](security/02-PACKET-ANALYSIS-AND-PCAP.md) packets, [03](security/03-WEB-APPLICATION-AND-API-SECURITY.md) web/API, [04](security/04-CRYPTOGRAPHY-PASSWORDS-KEY-MANAGEMENT.md) crypto, [05](security/05-IDENTITY-ACCESS-AND-AUTHORIZATION.md) IAM, [06](security/06-LOG-ANALYTICS-SOC-DETECTION.md) SOC, [07](security/07-DIGITAL-FORENSICS-AND-INCIDENT-RESPONSE.md) DFIR, [08](security/08-MALWARE-TRIAGE-AND-STATIC-ANALYSIS.md) malware triage, [09](security/09-THREAT-INTELLIGENCE-AND-OSINT.md) intelligence, [10](security/10-CLOUD-CONTAINERS-AND-DEVSECOPS.md) cloud, [11](security/11-VULNERABILITY-MANAGEMENT-AND-FUZZING.md) vulnerabilities, [12](security/12-SECURE-SDLC-AND-PYTHON-THREATS.md) secure SDLC, [13](security/13-WINDOWS-LINUX-ENDPOINT-TELEMETRY.md) endpoints, [14](security/14-DATABASES-DATA-PIPELINES-AND-SIEM.md) pipelines, [15](security/15-ADVANCED-DEFENSE-RESEARCH.md) research.

**Reference:** [Full index](reference/CHAPTER-INDEX.md), [Python/security library map](reference/LIBRARY-MAP.md), [glossary](reference/GLOSSARY.md), [100 exercises](reference/100-EXERCISES.md), [learning plan](reference/LEARNING-PLAN.md), [skills checklist](reference/SKILLS-CHECKLIST.md), [verified starting references](reference/REFERENCES.md).

**Practice:** [Step-by-step labs](labs/README.md), [code examples](examples/README.md), [synthetic fixtures](fixtures/), [tests](tests/), [capstone specifications](projects/PYTHON-CAPSTONES.md).

## Run the examples
```bash
git clone https://github.com/10425058-jpg/CyberSecurity-.git
cd CyberSecurity-
python -m venv .venv
# Activate your venv using instructions in python/00-START-HERE.md
python -m unittest discover -s tests -v
python -m examples.log_detector fixtures/synthetic-auth.jsonl
python -m examples.file_manifest fixtures
python -m examples.indicator_normalizer fixtures/synthetic-indicators.jsonl
python -m examples.local_port_check 8080
```

## What this resource does and does not claim
The content is a **broad, structured first edition**, not a claim to cover every evolving Python library, protocol, operating system, threat technique or framework exhaustively. Chapters provide conceptual coverage and initial examples; specialist production skills require current vendor docs, deeper courses, supervised experience and ongoing updates. Learn defensive fundamentals first; document uncertainty and limitations.

## Pre-existing general cybersecurity material (preserved)
- [General mind map](mindmap/MINDMAP.md)
- [General resources](RESOURCES.md)
- [12-month cybersecurity roadmap](roadmap/12-MONTH-ROADMAP.md)
- [General labs](projects/LABS-AND-PROJECTS.md)
- [Careers & certifications](career/CAREERS-AND-CERTIFICATIONS.md)
- [Study guide](STUDY-GUIDE.md)

## Contributions
Improve explanations with tested examples, version-aware citations, meaningful exercises, and small PRs. Never commit credentials, proprietary logs, malware samples, stolen data, or live unauthorized targets. Report software vulnerabilities privately to the repository maintainer.
