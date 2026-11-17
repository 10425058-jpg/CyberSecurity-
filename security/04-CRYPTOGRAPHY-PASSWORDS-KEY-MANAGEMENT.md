# Cryptography with Python: correct primitives and use cases

## What cryptography solves
- **Hash function:** maps bytes to a fixed-size digest; integrity comparison, not encryption.
- **MAC/HMAC:** keyed message authentication; prevents undetected modification if the key remains secret.
- **Symmetric encryption:** shared secret key, efficient confidentiality.
- **AEAD:** authenticated encryption with associated data; confidentiality **and** integrity.
- **Asymmetric cryptography:** public/private keys for signing, key exchange and encryption use cases.
- **Digital signature:** proof that a holder of a signing key signed data (subject to key identity and trust).
- **KDF/password hashing:** deliberately expensive derivation from low-entropy passwords.

## Correct random and comparison APIs
```python
import secrets, hmac, hashlib
token = secrets.token_urlsafe(32)
digest = hashlib.sha256(b"authorized-lab-evidence").hexdigest()
signature = hmac.new(b"example-key-not-for-production", b"payload", hashlib.sha256).digest()
assert hmac.compare_digest(signature, signature)
```
Use `secrets`, not `random`, for tokens. Do not compare secret MACs with naive equality when the use case requires timing-resistant comparison.

## Password storage
Modern password-hashing/KDF choices include Argon2id (typically preferred where supported), scrypt and carefully configured PBKDF2 when required. Unique random salt per password; track algorithm and parameters; use a verified library; consider rate limiting, MFA and breach-password checks. Plain SHA-256 is **not** a password hashing scheme.

```python
import hashlib, secrets, hmac
password = b"synthetic-demo-only"
salt = secrets.token_bytes(16)
stored = hashlib.scrypt(password, salt=salt, n=2**14, r=8, p=1)
candidate = hashlib.scrypt(password, salt=salt, n=2**14, r=8, p=1)
assert hmac.compare_digest(stored, candidate)
```
Production password hashing needs a maintained system/library, calibrated parameters, migration/versioning, and appropriate memory/work-factor limits.

## Authenticated encryption
With the `cryptography` package, AES-GCM uses a secret key and a unique nonce for each encryption under that key. **Never reuse a nonce with the same key.** Associated data is authenticated but not encrypted.

```python
# Optional: python -m pip install cryptography
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
key = AESGCM.generate_key(bit_length=256)
nonce = os.urandom(12)  # 96-bit nonce; ensure uniqueness per key
aead = AESGCM(key)
ciphertext = aead.encrypt(nonce, b"lab note", b"context-v1")
assert aead.decrypt(nonce, ciphertext, b"context-v1") == b"lab note"
```

## Key management
Separate key storage from ciphertext and code; manage access/rotation, revocation, audit, backup, service identity and lifecycle. Prefer platform KMS/HSM for operational keys. A successful decrypt does not grant authorization to use the plaintext. Do not implement custom cryptographic algorithms for production.

## Common mistakes
ECB mode; unauthenticated AES-CBC; static IV/nonce; weak random; reversible password storage; hardcoded secrets; homegrown token formats; disabled TLS verification; using a checksum as authentication; revealing whether a username exists in password reset flows.

## Exercises
1. Explain hash vs HMAC vs signature vs encryption.
2. Build a CLI that hashes local evidence files; document tamper-detection limitations.
3. Encrypt/decrypt synthetic data with AEAD and prove wrong AAD fails.
4. Write tests confirming token uniqueness (statistical illustration, not a proof).
5. Sketch a key rotation plan without exposing key material.
References: [Python secrets](https://docs.python.org/3/library/secrets.html), [cryptography AEAD](https://cryptography.io/en/stable/hazmat/primitives/aead/), [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html).
