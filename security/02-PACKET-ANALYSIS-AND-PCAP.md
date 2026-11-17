# Packet analysis with Python and offline PCAPs

## Packet anatomy
Ethernet → IP → TCP/UDP → application. Headers carry metadata: source/destination MAC/IP/ports, protocol, sequence numbers, flags and lengths. Parsing raw bytes requires correct link-layer type, fragmentation handling, endianness and bounds. A TCP payload may contain only part of an application message.

## Scapy and offline inspection
[Scapy](https://scapy.readthedocs.io/) can dissect packets, craft packets, and perform active operations. For this course, begin with **offline captures you generated in an isolated lab**.

```python
# Optional dependency: python -m pip install scapy
from scapy.all import IP, TCP, rdpcap

packets = rdpcap("lab-capture.pcap")
for packet in packets:
    if IP in packet and TCP in packet:
        print(
            packet[IP].src, packet[IP].dst,
            packet[TCP].sport, packet[TCP].dport,
            packet[TCP].flags,
        )
```
`rdpcap` loads a capture in memory; for larger files, use Scapy's streaming `PcapReader` with context/resource cleanup. Packet content may include secrets; anonymize cautiously, since naive IP replacement can break correlation.

## Analytic concepts
- Baselines: normal peers, protocols, hours and traffic volumes.
- TCP: 3-way handshake, retransmissions, resets, sequence/acknowledgment reasoning.
- DNS: query/response correlation, NXDOMAIN bursts, unusual query lengths (not proof of maliciousness).
- HTTP/TLS: methods/status codes, SNI/certificate metadata where observable; HTTPS payloads are normally encrypted.
- ICMP: reachability, errors, fragmentation.
- Traffic features: flows, byte counts, inter-arrival intervals, beacon-like periodicity, fan-out.

## Reliability and privacy
Capture permission and relevant jurisdictions matter. Treat packet timestamps and capture loss as uncertain. False positives are frequent: software updaters, monitoring and CDNs create repetitive traffic.

## Exercises
1. Create a local HTTP exchange, capture it with an approved tool, and export a PCAP.
2. Count TCP ports and talkers offline; verify with Wireshark.
3. Compare `PcapReader` memory to `rdpcap` on a large synthetic capture.
4. Identify limitations from truncation, encrypted TLS and asymmetric routing.
Resources: [Scapy docs](https://scapy.readthedocs.io/), [Wireshark guide](https://www.wireshark.org/docs/).
