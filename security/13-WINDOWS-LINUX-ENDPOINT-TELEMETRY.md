# Linux, Windows and endpoint telemetry for Python defenders

## Linux
Key concepts: users/groups, permissions, sudo/polkit, systemd services, journald, syslog, cron, sockets, processes, namespaces, auditd, firewall/nftables, SELinux/AppArmor and SSH. Sources may include journald JSON exports, auth logs, audit logs and EDR agent events. Access requires privilege and privacy controls.

## Windows
Key concepts: processes/services, registry hives, Windows Event Logs, Sysmon events, PowerShell transcription, Windows Defender, WMI, Active Directory context, Kerberos and NTFS. Event IDs are meaningful only in their provider/channel/version context; never claim a number always means one thing across systems.

## Cross-platform Python
Use `platform` and `pathlib`; prefer platform APIs to parsing localized shell output. For read-only monitoring: collect process metadata, configured service status, local file hashes and time-based event statistics. Some privileged data is unavailable without permission—do not bypass operating-system controls.

### Event mapping
Normalize to: `event_time_utc`, `ingest_time_utc`, `host`, `source/provider`, `event_id`, `user`, `process`, `action`, `outcome`, `raw_reference`. Document what was lost or transformed.

## Security pitfalls
- Event logs are incomplete and can be tampered with.
- High cardinality and event storms demand bounded memory.
- Process paths, command lines and environment variables may contain secrets.
- PID reuse makes process identity ambiguous; incorporate start time.
- Remote management requires authenticated channels, privileges and approval.

## Exercises
1. Parse a sanitized Linux auth log to count failures by username.
2. Normalize Windows and Linux synthetic events into one schema.
3. Design a test for PID reuse and timestamp skew.
4. Write an operational checklist before enabling new endpoint logging.
Resources: [Microsoft event logging docs](https://learn.microsoft.com/en-us/windows/win32/eventlog/event-logging), [systemd journal](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html).
