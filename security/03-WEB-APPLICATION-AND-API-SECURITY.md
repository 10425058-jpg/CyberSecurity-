# Web applications, APIs and secure Python backend patterns

## HTTP fundamentals
Methods (GET/POST/PUT/PATCH/DELETE), status codes, URL components, headers, cookies, JSON, content types, caching, redirects, CORS, TLS, proxies and reverse proxies. CORS is a **browser enforcement mechanism**, not API authentication. Distinguish authentication from authorization and resource ownership checks.

## High-impact web risks
- Injection: SQL, shell, template and expression injection; never interpret untrusted data as code.
- Broken access control/IDOR: enforce authorization per object on the server.
- SSRF: server is tricked into reaching unintended internal destinations. Host allowlists, DNS/rebinding checks, route restrictions and network egress policy are needed; regex alone is not enough.
- XSS: output encode for actual HTML/JS/attribute context and use framework auto-escaping.
- CSRF: cookie-authenticated state-changing requests need appropriate protections (tokens, SameSite, origin checks).
- Unsafe file upload: check extension, media and content, set limits, isolate storage, randomize filenames, scan when appropriate.
- Deserialization: never unpickle untrusted objects; use safe data formats and schema validation.
- Security misconfiguration: verbose errors, debug mode, secrets in source, permissive CORS, missing TLS.
- Resource exhaustion: request size/timeout limits, pagination and rate limiting.

## Parameterized SQL
```python
import sqlite3
connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE users (name TEXT, role TEXT)")
connection.execute("INSERT INTO users VALUES (?, ?)", ("alice", "reader"))
untrusted_name = "alice' OR '1'='1"
rows = connection.execute(
    "SELECT role FROM users WHERE name = ?", (untrusted_name,)
).fetchall()
assert rows == []
connection.close()
```
Parameterization applies to *values*, not arbitrary SQL identifiers. Allowlist table/column names if dynamically selecting them.

## Framework security
For Flask, Django or FastAPI: review request validation, auth dependencies, middleware ordering, CSRF/session handling, secure cookies, trusted proxy settings, file uploads, ORM usage and secrets. Read each framework's own security guidance and OWASP cheat sheets. Do not assume a framework's defaults cover every deployment.

## API client safety
Set timeouts, validate response schemas, avoid sharing tokens across hosts on redirects, constrain allowed endpoints, handle 429s with controlled backoff, and avoid logging authorization headers. Return error categories rather than leaking remote error details.

## Exercises
1. Build a local read-only API and enforce per-record access checks.
2. Write parameterized SQLite queries and tests using injection-shaped strings **as harmless test data**.
3. Implement positive input schema validation and safe error responses.
4. Explain why blocking the string `../` alone does not prevent filesystem traversal.
5. Draw all trust boundaries for client → reverse proxy → app → database.
Resources: [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/), [PortSwigger Web Security Academy](https://portswigger.net/web-security).
