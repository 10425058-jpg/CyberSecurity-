# Start here: Python for Cybersecurity

> Track A: programming fundamentals → Track B: systems and networking → Track C: defensive engineering → Track D: advanced specialization.

## Outcomes and boundaries
After the foundational track, you should be able to write maintainable Python, transform security telemetry, build local diagnostic tools, and explain why a tool is safe. After the security tracks, you should be able to design, test, and document useful blue-team automation. No single handbook makes someone an expert: practical experience, operating-system fundamentals, networking, and incident judgment are essential.

**Authorization first.** Run network experiments against loopback, owned VMs, or systems for which you have written permission. Treat collected traffic and logs as sensitive. Never upload production credentials or third-party packet captures. All active exercises default to isolated lab environments.

## Environment and prerequisites
- A supported Python 3 release (prefer a maintained stable version), Git, VS Code or another editor.
- A shell (Bash, PowerShell), a Git repository, and the ability to make a virtual environment.
- Recommended: Linux VM with snapshots, Windows VM for event-log study, and an isolated virtual network.
- A personal notebook: record commands, hypotheses, screenshots, expected results, observed results, and limitations.

### Start a virtual environment
```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python --version
python -m unittest discover -s tests -v
```

Do not execute fetched scripts blindly; verify sources and pin dependency versions for reproducible builds. Nothing in the standard-library examples needs paid services.

## Recommended sequence
1. `01–11`: master Python syntax, data handling, typing, file processing, tests, OOP, async and packaging.
2. `security/01–12`: understand boundaries, logs, networks, web apps, crypto, IR, detection, cloud, malware triage, and threat intelligence.
3. `labs/`: complete reproducible, local exercises; write a report for each.
4. `projects/`: extend and test the reference programs.
5. `reference/`: review the library map, exercises, glossary, and study schedule.

## Definition of done for a topic
- Explain **what it does**, **why it is used**, **how it can fail**, and **how to test it**.
- Implement at least one script without copying code.
- Add tests for normal, edge, and error cases.
- Document input assumptions, output format, required privileges, and privacy impact.
- Demonstrate that your code fails closed or safely when data is malformed.

## Learning method: 10 hours/week
- 2 h reading, 4 h building, 2 h debugging/testing, 1 h documenting, 1 h reviewing.
- Keep a small evidence-based portfolio. Compare observations with reference baselines, not intuition.
- Prefer official references: [Python documentation](https://docs.python.org/3/), [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/), [NIST CSRC](https://csrc.nist.gov/).
