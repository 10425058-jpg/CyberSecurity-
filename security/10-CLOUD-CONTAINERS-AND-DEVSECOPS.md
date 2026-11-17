# Cloud, containers and DevSecOps with Python

## Concepts before SDKs
Shared responsibility, IAM principals/roles, temporary credentials, network policies, encryption at rest/in transit, audit logs, object storage ACLs, secrets management, container image provenance and workload identity. A cloud service being reachable does not make querying it authorized.

## Python cloud automation patterns
Use vendor SDKs only with explicitly scoped credentials (e.g. read-only inventory role). Implement pagination, retries within rate limits, timeouts, multi-account/region scope, tagged resource normalization, and dry-run. Never store cloud API secrets in examples or code.

Example audit objective: detect storage resources without desired encryption or audit policy. **Do not automatically change production settings**; emit findings with source, timestamp, policy ID and confidence for operator review.

## Container basics
Image vs running container, registries, layered filesystems, namespaces, cgroups, capabilities, mounts, seccomp, rootless execution, Kubernetes pods/services/RBAC, admission policy and network policy. A container is not a universal secure sandbox. Mounting the host Docker socket often grants substantial host control.

## DevSecOps pipeline
Threat model → review dependency provenance → SAST → secret scanning → dependency/SBOM audit → tests → build/sign → deploy with minimal privileges → monitor → patch/rollback. Handle untrusted pull requests safely; CI workflows can be an attack surface.

```yaml
# Illustrative workflow checks, not a full production security policy
steps:
  - name: Check syntax
    run: python -m compileall python examples
  - name: Unit tests
    run: python -m unittest discover -s tests -v
```

## Exercises
1. Draft a least-privilege cloud read-only inventory role.
2. Parse a synthetic cloud audit log and classify permission changes.
3. Threat-model a GitHub Actions workflow that runs on untrusted PRs.
4. Review a container spec for root user, writable host mounts and excessive capabilities.
Resources: [OWASP CI/CD](https://owasp.org/www-project-top-10-ci-cd-security-risks/), [Kubernetes security](https://kubernetes.io/docs/concepts/security/), [Python security model](https://docs.python.org/3/library/security_warnings.html).
