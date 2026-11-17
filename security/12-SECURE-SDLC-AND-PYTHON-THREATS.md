# Secure Python software development lifecycle

## Python-specific attack surfaces
- **Command injection:** `os.system` and `subprocess` with concatenated shell input.
- **Untrusted deserialization:** `pickle`, unsafe YAML tags, unsafe object hooks.
- **Template injection:** evaluating untrusted template expressions.
- **Path traversal:** user-supplied paths escaping intended storage.
- **Weak secrets:** `random` and hardcoded API keys.
- **SQL injection:** composing SQL text with untrusted values.
- **SSRF:** fetching a URL without enforcing network-boundary policy.
- **Prototype or object misuse analogs:** unsafe dynamic attribute setting, mass assignment to data models.
- **Dependency compromise:** typosquatting, malicious build backends, vulnerable packages.
- **Sensitive logging:** tokens and private data in exception/diagnostic output.
- **TLS mistakes:** `verify=False`, overly permissive cert trust.
- **Race conditions:** permission changes between check and use.

## Review method
1. Identify entry points, sinks and trust boundaries.
2. Follow user-controlled data through transformations.
3. Verify authentication and per-resource authorization.
4. Inspect output contexts, parser resource limits, file paths and network egress.
5. Examine dependency list and CI credentials.
6. Trace error paths, logging, retries and cleanup.
7. Verify fixes with tests and document any residual risk.

## Safe patterns
Input schemas and length limits, positive allowlists where appropriate, parameterized queries, context-aware output encoding, safe serialization, `secrets`, authenticated cryptography from maintained libraries, and least-privilege service identities. Configuration must be treated as untrusted if it comes from an unverified source.

```python
# Avoid unsafe dynamic object construction from untrusted records.
ALLOWED = {"username", "department"}

def sanitize_profile(payload: dict) -> dict[str, str]:
    if not isinstance(payload, dict):
        raise ValueError("object required")
    if set(payload) - ALLOWED:
        raise ValueError("unexpected fields")
    if not all(isinstance(v, str) and len(v) <= 100 for v in payload.values()):
        raise ValueError("invalid profile field")
    return dict(payload)
```

## Tool-assisted assurance
Static scanners help find suspicious patterns, dependency auditors identify known advisory matches, tests exercise behavior, and reviews assess design. No individual tool guarantees correctness. Maintain a threat model, security test suite, incident escalation policy and dependency update process.

## Exercises
1. Review an intentionally vulnerable toy script and suggest a safer rewrite.
2. Design security test cases for every input boundary of a Python service.
3. Write a dependency and secrets handling policy for this repository.
4. Describe how authorization tests differ from authentication tests.
References: [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/), [Python security warnings](https://docs.python.org/3/library/security_warnings.html).
