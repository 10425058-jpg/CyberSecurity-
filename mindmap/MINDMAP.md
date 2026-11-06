# Complete Cybersecurity Mind Map

## 1. IT and CS foundations
- Hardware: CPU, RAM, storage, motherboard, firmware, BIOS/UEFI.
- OS concepts: kernel, processes, threads, memory, filesystems, permissions, services, boot.
- Virtualization: hypervisors, guest/host OS, snapshots, virtual networking, VMware, VirtualBox, Proxmox, ESXi.
- Data: binary/hex, encoding, databases, SQL, algorithms basics.

## 2. Operating systems
- Linux: filesystem, users/groups, permissions, sudo, packages, processes, systemd, SSH, logs, firewall, Bash, hardening.
- Windows: NTFS, registry, services, Event Viewer, PowerShell, Defender, Sysinternals, Group Policy.
- macOS: permissions, Gatekeeper, FileVault, logs.
- Enterprise identity: Active Directory, LDAP, Kerberos, domains, Entra ID.

## 3. Networking
- OSI, TCP/IP, encapsulation, Ethernet.
- IPv4/IPv6, public/private IP, subnetting, CIDR, gateways, loopback.
- TCP, UDP, ICMP, ARP, DNS, DHCP, HTTP/S, SSH, FTP/SFTP, SMTP, NTP, SNMP, SMB, LDAP, TLS, IPsec.
- Routers, switches, VLAN, WLAN, WAN, VPN, NAT, proxies, load balancers, firewalls, DMZ, segmentation.
- DHCP, DNS, NTP, IPAM, AAA, RADIUS, TACACS+.
- Tools: ping, traceroute, ipconfig, ip, dig, nslookup, ss/netstat, tcpdump, Wireshark, Nmap, Netcat.

## 4. Programming and automation
- Python: syntax, data structures, functions, OOP, files, JSON, regex, requests, sockets, subprocess, logging, testing.
- Bash, PowerShell; further languages as needed: JavaScript, Go, C/C++.
- Git/GitHub, APIs, SQL, debugging, automation, secure coding.

## 5. Security fundamentals
- CIA triad, threats, vulnerabilities, exploits, risk, attack surface.
- Authentication/authorization, MFA, SSO, RBAC, ABAC, ACL, least privilege.
- Hashing, salting, encryption, signatures, key exchange, PKI, certificates, TLS.
- Defense in depth, Zero Trust, isolation, segmentation, hardening.
- Firewall, IDS/IPS, EDR/XDR, antivirus, DLP, NAC, sandboxing.
- Backups, disaster recovery, business continuity, incident response.
- Frameworks: NIST CSF/800-series, CIS Controls, ISO 27001, MITRE ATT&CK, Cyber Kill Chain, Diamond Model.

## 6. Red Team / penetration testing
- Ethics, authorization, scope, rules of engagement, evidence, reporting.
- Reconnaissance: OSINT, DNS, WHOIS, metadata, asset discovery.
- Enumeration: hosts, ports, services, users, shares, web content.
- Vulnerability assessment, validation, prioritization, remediation retest.
- Web: HTTP, sessions, access control, authentication, SQLi, XSS, CSRF, SSRF, file upload, path traversal, command injection, API security, OWASP Top 10/ASVS.
- Network, wireless, Linux/Windows host testing; Active Directory security.
- Tools: Nmap, Burp, ZAP, Metasploit, Netcat, BloodHound, Impacket (authorized labs).
- Reporting: scope, findings, severity, evidence, impact, remediation, retest.

## 7. Blue Team / SOC / detection
- SOC tiers, alert triage, escalation, case management.
- Telemetry: Windows Event Logs, Sysmon, Linux logs, firewall, DNS, proxy, endpoint, cloud audit, NetFlow.
- SIEM ingestion, parsing, normalization, correlation, dashboards, tuning.
- Sigma, YARA, IOC, ATT&CK mapping, behavioral detection, false positives/negatives.
- Threat intelligence, hunting hypotheses, TTPs.
- Incident response: preparation, identification, containment, eradication, recovery, lessons learned.
- Tools: Wazuh, Splunk, Elastic, Sentinel, Sysmon, Wireshark, CyberChef.

## 8. DFIR, malware and reverse engineering
- Evidence handling, chain of custody, timelines.
- Disk, memory, network and endpoint forensics.
- Volatility, Autopsy, forensic images.
- Malware behavior, static/dynamic analysis, sandboxing, YARA.
- Assembly concepts, Ghidra, reverse engineering.
- Isolated lab safety.

## 9. Cloud and infrastructure security
- IaaS/PaaS/SaaS; public/private/hybrid.
- AWS, Azure, Google Cloud.
- IAM, roles, policies, MFA, key management, secrets, audit logs.
- VPC/VNet, segmentation, private endpoints, storage permissions, encryption, backups.
- Containers: Docker images, registries, secrets, runtime.
- Kubernetes RBAC, network policies, pod security, secrets, audit.
- IaC, Terraform, configuration scanning, cloud incident response.

## 10. AppSec and DevSecOps
- Secure SDLC, threat modeling, code review.
- SAST, DAST, SCA, secrets scanning, dependency management.
- CI/CD security, build provenance, artifact integrity.
- API security, OAuth/OIDC, JWT, rate limiting.
- Secure coding, input validation, output encoding, parameterized queries.
- OWASP SAMM and ASVS.

## 11. Wireless, mobile, IoT and OT/ICS
- Wi-Fi WPA2/WPA3, enterprise auth, rogue AP, segmentation.
- Bluetooth, NFC, RFID, infrared.
- Android/iOS permissions, app storage, mobile threat models.
- IoT firmware, device identity, updates, exposed services.
- OT/ICS: PLC, SCADA, industrial protocols, safety, zoning, passive monitoring.

## 12. GRC, risk, compliance and privacy
- Risk registers, controls, policies, standards, procedures, audit evidence.
- ISO 27001/27002, NIST CSF/RMF, CIS Controls.
- Privacy principles, classification, retention, access governance.
- GDPR concepts, third-party risk, business continuity, awareness.

## 13. Emerging security
- AI/ML and LLM security, prompt injection, data leakage, model supply chain.
- AI threat modeling, secure deployment and monitoring.
- Quantum-safe cryptography concepts, resilience engineering.

## 14. Career specializations
SOC Analyst, Pentester, AppSec Engineer, Security Engineer/Architect, Cloud Security, DFIR, Threat Hunter, Malware Analyst, DevSecOps, GRC/Audit, IAM, OT/ICS Security.

## Learning dependency
IT/OS → Networking → Programming → Security fundamentals → hands-on labs → try Blue and Red → choose a specialization → role-specific portfolio. This is a dependency map, not a requirement to master every branch.