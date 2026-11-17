# 09 — Operating-system automation with Python

## Core libraries
`os`, `sys`, `pathlib`, `shutil`, `tempfile`, `subprocess`, `signal`, `platform`, `stat`, `getpass`, `logging`, `time` and `datetime`. Learn filesystem permissions, process ownership, environment variables, UIDs/GIDs, Windows tokens, services, scheduled jobs, and shell quoting.

```python
import subprocess
result = subprocess.run(
    ["python", "--version"],
    check=True, text=True, capture_output=True, timeout=5
)
print(result.stdout or result.stderr)
```

**Never** form shell commands by concatenating user input and `shell=True`. Prefer argument arrays, fixed executable paths where possible, per-command timeouts, and least privilege. Note that even `shell=False` does not make an unsafe command or untrusted executable safe.

## Filesystem safety
A path may refer to a symlink; checking then opening creates a time-of-check/time-of-use race. For sensitive operations, use OS-specific secure file APIs and file-descriptor-relative checks. Do not follow arbitrary user-controlled paths into protected areas. Use `tempfile.TemporaryDirectory` and atomic replace patterns where appropriate.

## Defensive automation examples
- Periodic checksum baseline generation for a configured folder.
- Inventory file ownership and weak permission modes on owned hosts.
- Rotate/normalize logs while preserving retention and audit requirements.
- Check whether a known local service listens on a configured port.
- Gather system configuration for an approved compliance checklist.
- Monitor disk pressure and backup freshness without leaking private filenames.

## Security boundaries
Automation often runs with privileged accounts. Split discovery from remediation, default to read-only, require confirmation for high-impact changes, maintain dry-run mode, write immutable logs where supported, and provide rollback. Limit processes' network/file privileges and never embed passwords in source.

## Exercises
1. Write a read-only directory inventory with path, size, modification time and SHA-256.
2. Build a subprocess wrapper with timeout and explicit error reporting.
3. Test paths with spaces, Unicode, symlinks, and missing permissions.
4. Explain why `subprocess.run(["tool", user_value])` is safer than a shell string but still needs validation.

References: [subprocess](https://docs.python.org/3/library/subprocess.html), [pathlib](https://docs.python.org/3/library/pathlib.html).
