# Identity, access management and session security

## Core distinctions
- Identification: claimed identity.
- Authentication (AuthN): evidence that claim is valid.
- Authorization (AuthZ): permission to perform a specific action on a specific resource.
- Accounting/auditing: record who did what, when, and under which context.
- Session: continuity of authenticated state over multiple requests.

## Models
RBAC grants permissions through roles; ABAC evaluates attributes; ReBAC models relationships. Apply least privilege, separation of duties, explicit deny, and per-resource checks. Role strings alone are not a complete authorization policy.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Document:
    owner_id: str
    classification: str

def may_read(user_id: str, roles: set[str], document: Document) -> bool:
    if "security-auditor" in roles:
        return True  # only if policy explicitly permits this
    return document.owner_id == user_id and document.classification == "personal"
```
The sample policy is illustrative; actual auditor access often needs case- or purpose-bound approvals.

## Sessions, tokens and MFA
Sessions need secure random identifiers, TLS, server-side invalidation and expiration. Cookies should use Secure, HttpOnly and an appropriate SameSite value. JWT validation must verify signature, allowed algorithm, issuer, audience, clock bounds and token type; rejecting `alg=none` is necessary but not sufficient. Never treat parsing a JWT as verifying it.

Strong MFA and phishing-resistant authenticators, constrained service accounts, scoped OAuth/OIDC flows and safe recovery procedures reduce account takeover risks. Distinguish API keys from user sessions; avoid logging either.

## Directory and enterprise security
LDAP, Kerberos, Active Directory, group membership, SSO, managed identities and privilege delegation are important background concepts. Automate identity inventory carefully and always separate reporting from privilege changes.

## Exercises
1. Write unit tests for owner vs non-owner vs auditor access.
2. Design an API token with minimal scopes and short expiration.
3. Explain replay attacks and session fixation.
4. Review a hypothetical approval flow for least privilege and audit completeness.
Resources: [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html), [OWASP Authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html).
