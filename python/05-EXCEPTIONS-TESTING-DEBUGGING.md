# 05 — Error handling, tests, debugging and observability

## Exception design
Use `try` only around the statement that can fail; catch specific exceptions. Preserve stack traces with `raise` and chain causes with `raise NewError(...) from exc` when translating failures. Never return a successful-looking empty result after an unexpected exception.

```python
import json

def parse_record(line: str) -> dict:
    try:
        obj = json.loads(line)
    except json.JSONDecodeError as exc:
        raise ValueError("invalid JSON record") from exc
    if not isinstance(obj, dict):
        raise ValueError("expected a JSON object")
    return obj
```

## Testing strategy
1. **Unit tests:** pure functions and validation; no network or filesystem side effects.
2. **Integration tests:** parser + database + local test fixture.
3. **Property/fuzz tests:** many generated valid/invalid inputs; establish invariants.
4. **Regression tests:** add one after every resolved bug.
5. **Security tests:** malformed paths, Unicode, timeouts, authorization edge cases, injection-like strings treated as data.
6. **Performance tests:** memory and response limits for large or adversarial input.

```python
import unittest
class ParseTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(parse_record('{"ok": true}'), {"ok": True})
    def test_non_object(self):
        with self.assertRaises(ValueError):
            parse_record("[]")
```

## Tooling and quality
- `python -m unittest discover -s tests -v` (stdlib), or pytest for fixture-rich workflows.
- `python -m compileall .` for syntax validation.
- `ruff check .` for lint and `ruff format .` for consistent style.
- `mypy` or pyright for static typing.
- `bandit -r src` for a security-oriented static analysis pass; findings still require human review.
- `pip-audit` for known vulnerable dependencies; absence of findings is not proof of safety.
- CI should fail for test regressions and block publication of secrets.

## Logging and tracing
Use `logging` with structured, contextual metadata; avoid raw credentials, access tokens, session cookies, complete personal identifiers, or entire untrusted payloads. Preserve request correlation IDs where authorized. Rate-limit repetitive errors and monitor false positives. Use `pdb`, IDE breakpoints, and `traceback` locally; sanitize tracebacks exposed to users.

## Exercises
1. Write table-driven tests for a severity classifier.
2. Make a parser robust against a blank line, object/list confusion, and 10 MB fields.
3. Add a log handler and prove no secret token is emitted.
4. Explain expected error vs unexpected programmer error and why broad catches obscure bugs.

References: [unittest](https://docs.python.org/3/library/unittest.html), [logging](https://docs.python.org/3/library/logging.html), [Bandit](https://bandit.readthedocs.io/).
