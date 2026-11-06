# 12-Month Cybersecurity Roadmap — 10 Hours per Week

Starting point: basic IT knowledge, beginner in cybersecurity. Total: approximately 520 hours. Strategy: foundations → sample Red and Blue → choose specialization. This plan samples the complete mind map; it does not cover every advanced branch.

## Month 1 — Linux
- W1: OS, kernel, filesystem; install Ubuntu VM.
- W2: directories, files, users, groups, permissions.
- W3: processes, services, packages, SSH.
- W4: Bash, pipes, redirection, logs; write backup/log-filter script.
- Course/docs: https://linuxjourney.com/ ; https://documentation.ubuntu.com/ ; https://www.gnu.org/software/bash/manual/
- Lab: https://overthewire.org/wargames/bandit/
- Output: Linux administration lab.
- Gate: install VM, explain permissions, use shell, write basic script.

## Month 2 — Windows and virtualization
- W5: Windows architecture, NTFS, registry, accounts.
- W6: CMD, PowerShell, services, processes.
- W7: Event Viewer, logs, permissions, Sysinternals.
- W8: VM networking and snapshots; connect Windows and Ubuntu in isolated lab.
- Resources: https://learn.microsoft.com/training/ ; https://learn.microsoft.com/powershell/ ; https://www.virtualbox.org/manual/
- Output: Windows/Linux administration lab, network diagram, sample logs.
- Gate: manage accounts/services, inspect events, explain VM networking.

## Month 3 — Networking foundations
- W9: OSI, TCP/IP, encapsulation.
- W10: IPv4/IPv6, MAC, public/private addresses.
- W11: subnet masks, CIDR, gateways; solve 20 subnetting problems.
- W12: TCP/UDP, ports, handshake.
- Course: https://www.netacad.com/ ; https://www.cloudflare.com/learning/
- Lab: https://www.netacad.com/courses/packet-tracer
- Output: small-office LAN topology and subnet table.
- Gate: explain OSI/TCP-IP, calculate basic subnets, compare TCP/UDP.

## Month 4 — Network services and analysis
- W13: DNS, DHCP, ARP, NAT.
- W14: HTTP/HTTPS, SSH, FTP/SFTP, TLS.
- W15: routers, switches, VLANs, VPN, firewall.
- W16: Wireshark, Nmap, Netcat; inspect authorized lab traffic.
- Docs: https://www.wireshark.org/docs/ ; https://wiki.wireshark.org/SampleCaptures ; https://nmap.org/book/
- Output: packet analysis report showing DNS, TCP handshake and protocol metadata.
- Gate: analyze a PCAP and explain common services.

## Month 5 — Python and automation
- W17: variables, types, conditions, loops.
- W18: functions, collections, modules, basic OOP.
- W19: files, CSV/JSON, regex, exceptions.
- W20: sockets, requests, logging, Git.
- Resources: https://www.netacad.com/ ; https://docs.python.org/3/tutorial/ ; https://exercism.org/tracks/python ; https://git-scm.com/book/en/v2
- Output: log analyzer, SHA-256 integrity checker, localhost/lab-only port checker.
- Gate: write/explain scripts, use Git, handle errors.

## Month 6 — Security fundamentals
- W21: CIA triad, threats, vulnerabilities, risk.
- W22: authentication, authorization, MFA, RBAC, ACL.
- W23: hashing, salting, encryption, keys, certificates, TLS.
- W24: firewalls, IDS/IPS, hardening, Zero Trust.
- Resources: https://csrc.nist.gov/ ; https://www.netacad.com/ ; https://www.professormesser.com/
- Output: basic security assessment of your own lab.
- Gate: distinguish threat/vulnerability/risk, hashing/encryption, authentication/authorization.

## Month 7 — Red Team foundations
- W25: authorization, scope, rules of engagement, methodology.
- W26: reconnaissance and Nmap.
- W27: enumeration and service identification.
- W28: Kali, Burp Suite, vulnerability assessment concepts.
- Resources: https://tryhackme.com/ ; https://www.hackthebox.com/ ; https://nmap.org/book/ ; https://www.kali.org/docs/
- Output: scoped reconnaissance report for isolated lab.
- Gate: explain methodology and interpret scan results.

## Month 8 — Web security and CTF
- W29: HTTP, cookies, sessions, request/response.
- W30: SQL injection and XSS in training labs.
- W31: access control, authentication flaws, CSRF.
- W32: OWASP Top 10, evidence and reporting.
- Resources: https://portswigger.net/web-security ; https://owasp.org/ ; https://owasp.org/www-project-juice-shop/ ; https://picoctf.org/
- Output: local web assessment with three documented findings and fixes.
- Gate: complete beginner labs and explain root cause, impact, remediation.

## Month 9 — Blue Team and SOC
- W33: SOC workflow, alert triage, escalation.
- W34: Windows Event Logs, Sysmon, Linux logs.
- W35: SIEM, ingestion, normalization, correlation.
- W36: deploy Wazuh and connect a lab endpoint.
- Resources: https://documentation.wazuh.com/ ; https://learn.microsoft.com/sysinternals/downloads/sysmon ; https://attack.mitre.org/
- Output: Mini SOC lab with sample telemetry and basic alert.
- Gate: explain log sources, inspect events, demonstrate alert workflow.

## Month 10 — Incident response and hunting
- W37: incident response lifecycle.
- W38: ATT&CK tactics, techniques and mapping.
- W39: IOC, threat intelligence, hunting hypotheses.
- W40: PCAP/log/forensic artefact analysis using safe training datasets.
- Resources: https://csrc.nist.gov/pubs/sp/800/61/r2/final ; https://cyberdefenders.org/ ; https://gchq.github.io/CyberChef/
- Output: investigation report with timeline, evidence and response recommendations.
- Gate: investigate a training scenario and justify conclusions.

## Month 11 — Cloud and containers
- W41: IaaS/PaaS/SaaS, public/private/hybrid.
- W42: IAM, shared responsibility, logging.
- W43: storage, network controls, misconfiguration risks.
- W44: Docker fundamentals and container security.
- Resources: https://skillbuilder.aws/ ; https://docs.aws.amazon.com/security/ ; https://learn.microsoft.com/azure/security/ ; https://docs.docker.com/get-started/
- Output: cloud/container security design or safe local Docker lab.
- Gate: explain IAM, shared responsibility and basic container risks.

## Month 12 — Portfolio and career
- W45: review Linux, Windows, networking and Python.
- W46: polish Red Team assessment and report.
- W47: polish Blue Team investigation and report.
- W48: polish integrated lab architecture and deployment guide.
- W49: review Security+ objectives if relevant: https://www.comptia.org/certifications/security
- W50: GitHub README, CV and project documentation.
- W51: technical interview practice.
- W52: skills assessment and choose a primary specialization.
- Output: 4–6 polished projects/reports.
- Gate: reproduce projects, explain decisions, discuss limitations and remediation.

## Weekly allocation
2h course, 1h documentation, 4h labs, 2h project, 1h review. Adjust around university workload. Do not skip foundational gates to keep up with the calendar.

## Specialization decision
- Blue Team: monitoring, logs, investigation, detection, response.
- Red Team: scoped testing, enumeration, web/application security, reporting.
Keep the other track at foundation level while specializing in one.