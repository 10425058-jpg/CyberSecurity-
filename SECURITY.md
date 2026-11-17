# Security policy for this educational repository

This repository is teaching material, not a deployed security platform. Examples are local-first and cannot be relied upon as production-grade detectors, cryptography services or forensic acquisition systems.

## Responsible reporting
If you identify a vulnerability in an example, please contact the maintainer privately rather than publishing secrets or exploit details. Do not send private logs, unauthorized packet captures or live malware binaries in a GitHub issue.

## Testing and data
Run only on owned or expressly authorized environments. Example fixtures must be synthetic and should use documentation-reserved addresses (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24 and 2001:db8::/32).

## Dependency and CI handling
- Keep examples standard-library-only when reasonable.
- Review third-party dependencies and sources before installation.
- Never commit keys, environment secrets, captured credentials or proprietary logs.
- Keep CI permissions limited and do not expose secrets to untrusted PRs.
- Security scanner output requires review, confirmation and remediation.

## Limitations
Safe paths and file hashes do not ensure forensic chain of custody; a reachable service is not necessarily secure or insecure; statistical findings are not proof of an intrusion. Treat all examples as starting points for disciplined engineering.
