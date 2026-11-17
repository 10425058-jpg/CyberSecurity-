# Security engineering: authorization, ethics and threat modeling

## Scope of the handbook
The goal is to learn how Python helps defenders inspect *their own* systems, handle evidence, secure software, and automate authorized assessments. Real systems contain private data; even a seemingly read-only scan can trigger alerts or impact availability. Obtain written authorization specifying targets, methods, times, evidence handling, emergency contacts and permitted traffic volumes. Default labs to loopback, offline PCAPs, or isolated virtual networks.

## Key concepts
- **Asset:** something of value (customer data, availability, credentials).
- **Threat actor and capability:** who may cause a harmful event, with what access.
- **Trust boundary:** where assumptions change (network request → parser; user → OS shell).
- **Attack surface:** reachable inputs, APIs, dependencies, admin tools, and data pipelines.
- **Vulnerability:** weakness; **threat:** potential cause; **risk:** combination of likelihood and impact within context.
- **Control:** prevention, detection, response or recovery measure.
- **Security invariant:** property that must remain true, e.g. "only owners can retrieve their reports".

## STRIDE-informed walkthrough
For a log processing web service:
1. **Spoofing:** token theft; mitigation: validated sessions, MFA, short-lived scoped tokens.
2. **Tampering:** attacker changes alert evidence; mitigation: append-only audit logs, source hashes.
3. **Repudiation:** cannot attribute action; mitigation: identity-linked auditing and synchronized clocks.
4. **Information disclosure:** raw logs expose secrets; mitigation: redaction and access controls.
5. **Denial of service:** huge logs exhaust memory; mitigation: input size limits, streaming, quotas.
6. **Elevation of privilege:** parser executes code or shell command; mitigation: untrusted input as data, least privilege.

## Data handling
Store minimum necessary data; classify private records; use retention periods, access logging and secure transport. Preserve evidentiary originals and document transformations. Hashes are integrity *indicators*, not automatic proof of authenticity. Use synthetic examples in publicly shared repos.

## Safe evaluation process
Scope → baseline → observe → reproduce in lab → assess impact → document evidence → propose fix → validate with owner → report residual risk. Never claim that a detection rule alone proves compromise.

## Exercises
1. Threat-model a Python CLI that ingests login logs and posts alerts.
2. Define clear rules of engagement for a local loopback service check.
3. Create a data-flow diagram with trust boundaries for a security dashboard.
4. Write a false-positive review plan and a responsible disclosure email template.
Resources: [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling), [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework).
