# 10 — CLI engineering, distribution and software supply chain

## CLI design
Use `argparse` for clear options, validation, help text and exit codes. Define stable output formats (JSONL/CSV), stderr for errors, and stdout for machine-readable results. Never echo tokens passed through flags.

```python
from argparse import ArgumentParser
from pathlib import Path

def main() -> int:
    parser = ArgumentParser(description="Read-only local file inventory")
    parser.add_argument("directory", type=Path)
    parser.add_argument("--format", choices=["json", "text"], default="text")
    args = parser.parse_args()
    if not args.directory.is_dir():
        parser.error("directory must exist")
    print(args.directory.resolve())
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

## Project structure
```text
tool/
  pyproject.toml
  README.md
  src/package_name/__init__.py
  src/package_name/cli.py
  src/package_name/core.py
  tests/test_core.py
```

## Dependency management
`venv` isolates Python environments but is **not a security sandbox**. `pip` installs third-party code which may execute during build/install. Review maintainers, pin and hash dependencies in controlled deployments, keep lockfiles, inventory transitive dependencies, generate SBOMs where useful, and update affected packages. Check official sources and advisories rather than trusting download counts.

## CI/CD
- Trigger unit tests and type checks on PR.
- Run SAST (e.g. Bandit) and dependency audit; triage, don't blindly suppress.
- Protect credentials with least-privilege CI identities.
- Require review on workflow changes; do not expose secrets to untrusted PR code.
- Build artifacts reproducibly and document provenance and signing where practical.
- Define responsible disclosure and a private security contact.

## Exercises
1. Package an event parser as a `console_scripts` entry point.
2. Add `--help`, `--json`, `--limit` and correct nonzero error codes.
3. Write a pipeline that checks tests, lint, and minimum supported Python.
4. Explain why dependency pinning, signing, and vulnerability scanning address different risks.
References: [packaging user guide](https://packaging.python.org/), [pip](https://pip.pypa.io/).
