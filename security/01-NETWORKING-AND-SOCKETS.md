# Networking with Python: sockets, DNS and safe diagnostics

## Prerequisites
Understand OSI vs TCP/IP models, Ethernet, ARP, IPv4/IPv6, CIDR, subnets, routing, DNS, DHCP, NAT, TLS, UDP, TCP, ports, connection states, and HTTP. Client and server addresses/ports form endpoints; a firewall may block a connection even when an application is running.

## Socket essentials
A TCP socket connects, exchanges a byte stream, and closes. **TCP preserves byte order but not message boundaries.** A single `recv` can return fewer bytes than requested. Design framed protocols (e.g., length-prefix) and maximum message sizes. UDP transmits datagrams and does not guarantee delivery. DNS lookup can return multiple addresses and may be attacker-influenced.

```python
import socket

def check_loopback(port: int, timeout: float = 0.5) -> bool:
    if not 1 <= port <= 65535:
        raise ValueError("port outside range")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        return sock.connect_ex(("127.0.0.1", port)) == 0

if __name__ == "__main__":
    print(check_loopback(8080))
```

This verifies a loopback TCP connect only; it does **not** identify the application, prove TLS security or demonstrate vulnerability.

## Diagnostics and boundaries
- `socket.getaddrinfo` resolves hostnames; be aware of IPv4/IPv6 differences.
- `ipaddress.ip_address` and `ipaddress.ip_network` correctly parse addresses/CIDRs; string splitting is unreliable.
- `ssl.create_default_context` verifies certificates for normal TLS clients; do not disable verification to "fix" errors.
- `asyncio.open_connection` supports concurrent I/O; always bound concurrency and time.
- `http.client`, `urllib.request`, and third-party clients can send approved HTTP requests with explicit timeouts.

## DNS and TLS
DNS answers can change between validation and use; this matters for SSRF and network allowlists. TLS provides authenticated encryption when certificate/hostname verification succeeds. Trust stores, expiration, revocation policy, SNI, mTLS, and protocol downgrade matter. Encryption does not authorize an API call.

## Network monitoring
Log connection errors separately from unreachable endpoints. Record timestamp (UTC), target, protocol, timeout, context, and confidence; do not report "compromised" because a port is open. Establish benign expected services before investigating anomalies.

## Exercises
1. Parse a list of IP strings with `ipaddress`; reject malformed values.
2. Connect to an HTTP test server bound to 127.0.0.1 using a 1-second timeout.
3. Create a length-prefixed message parser with a maximum frame size.
4. Explain SYN/SYN-ACK/ACK, TCP retransmissions, and why timeout != closed port.
5. Compare TCP and UDP diagnostic assumptions.
References: [socket](https://docs.python.org/3/library/socket.html), [ipaddress](https://docs.python.org/3/library/ipaddress.html), [ssl](https://docs.python.org/3/library/ssl.html).
