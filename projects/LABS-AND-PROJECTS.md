# Labs and Project Catalogue

Use isolated VMs, local intentionally vulnerable applications, supplied PCAP/log datasets, or platforms that explicitly authorize the exercise.

## Project 1 — Linux Administration Lab
Skills: filesystem, users/groups, permissions, services, Bash. Create users/groups, apply least privilege, manage packages/services, write a backup script. Evidence: setup guide, permissions matrix, script, tests, troubleshooting notes.

## Project 2 — Windows/Linux Administration Lab
Skills: virtualization, Windows/Linux administration, VM networking, logging. Build one Windows VM and one Ubuntu VM on an isolated network; configure accounts; verify connectivity; collect sample logs. Evidence: network diagram, VM config, screenshots, log explanation.

## Project 3 — Network Design and Traffic Analyzer
Skills: IP addressing, subnetting, Packet Tracer, Wireshark, TCP/IP. Design a small LAN; document subnets/gateways; capture authorized traffic; identify DNS, TCP handshake and HTTP metadata. Evidence: topology, subnet table, sanitized PCAP and report.

## Project 4 — Python Security Toolkit
Build three documented tools:
1. Log Analyzer: parse sample logs, count event types, flag repeated failed logins in sample data.
2. File Integrity Checker: calculate SHA-256 hashes and compare against baseline.
3. Port Checker: check selected ports on localhost or lab host only; include timeouts and clear scope controls.
Evidence: source, tests, sample data, README, usage examples, limitations.

## Project 5 — Basic Security Assessment
Scope: your own Windows and Ubuntu lab. Inventory assets, review users/permissions, examine exposed services, inspect host firewall, identify insecure configurations, classify risk and propose remediation. Evidence: scope, asset list, findings, remediation, retest.

## Project 6A — Web Application Security Assessment (Red Team)
Target: local OWASP Juice Shop or PortSwigger Academy lab. Review request/response; test selected beginner vulnerability classes; preserve evidence; explain root cause and remediation. Evidence: scope, methodology, sanitized requests/responses, impact, remediation, retest. Never test public applications without explicit authorization.

## Project 6B — Mini SOC Investigation (Blue Team)
Environment: Wazuh, Windows endpoint with Sysmon, and/or supplied training logs. Ingest logs, identify test event, triage alert, build timeline, map behaviour to ATT&CK, recommend containment. Evidence: dashboard, sanitized logs, timeline, investigation report, detection improvement.

## Project 7 — Integrated Security Lab
Components: Windows VM, Ubuntu VM, local training web app, Wazuh manager, endpoint telemetry, Docker if appropriate. Workflow: build → document baseline → conduct authorized benign test activity → collect telemetry → detect → investigate → remediate → retest. Evidence: architecture, deployment guide, test plan, detections, incident report, remediation.

## Project report template
1. Title and summary.
2. Learning objectives.
3. Scope and authorization.
4. Architecture and environment.
5. Tools and versions.
6. Method and commands (remove secrets and personal data).
7. Findings and evidence.
8. Risk/impact.
9. Remediation and retest.
10. Limitations and lessons learned.

## Portfolio quality
A reviewer can reproduce the environment; scope and authorization are explicit; no secrets or personal data are published; screenshots are sanitized; findings include fixes; author can explain tools and code.