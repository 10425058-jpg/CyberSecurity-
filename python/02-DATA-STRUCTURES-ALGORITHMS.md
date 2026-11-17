# 02 — Data structures, algorithms and complexity

## Collections
| Type | Ordering | Mutable? | Typical cybersecurity use |
|---|---|---|---|
| `list` | insertion | yes | event sequences |
| `tuple` | insertion | no | immutable event keys |
| `dict` | insertion | yes | parsed JSON, counters, indexes |
| `set` / `frozenset` | iteration not ordered contract | yes / no | deduplication, indicators |
| `collections.deque` | sequence | yes | bounded queues, rolling windows |
| `collections.Counter` | mapping | yes | frequency analysis |
| `heapq` | heap ordering | yes | top-priority alerts |
| `bisect` | sorted-list operations | n/a | thresholds and intervals |

### Counting events
```python
from collections import Counter, defaultdict
events = [
    {"ip": "192.0.2.1", "status": 401},
    {"ip": "192.0.2.1", "status": 401},
    {"ip": "198.51.100.2", "status": 200},
]
failures = Counter(e["ip"] for e in events if e["status"] == 401)
print(failures.most_common(5))
by_ip = defaultdict(list)
for event in events:
    by_ip[event["ip"]].append(event)
```

### Complexity
- List append: amortized O(1); membership: O(n).
- Dict/set lookup: expected average O(1), not a universal worst-case guarantee.
- Sorting: O(n log n); sorting millions of logs in memory is expensive.
- Streaming through a file: O(n) time and bounded memory when avoiding `read()` of the whole file.
- Nested comparison of all hosts against all hosts: O(n²), which often does not scale.

Understand the distinction between **average performance**, **worst-case performance**, and **adversarial inputs**. Set limits on input sizes, recursion depth, and decompression output to prevent resource exhaustion.

### Comprehensions and safe parsing
```python
valid_ports = {p for p in [22, 80, 443, -1, 70000] if 1 <= p <= 65535}
assert valid_ports == {22, 80, 443}
```
Comprehensions are concise but can obscure multiple validation steps. Prefer explicit loops when incident logic needs an audit trail.

### Core patterns to master
- Deduplication with a set while preserving first-seen order with dict keys.
- Sliding windows for burst detection (deque of timestamps).
- Aggregation by normalized principal/IP/event ID.
- Sorting with `key=`, stable sorting, and `heapq.nlargest`.
- Searching sorted timestamps via `bisect`.
- Hashing and indexing normalized indicators; normalize case and Unicode thoughtfully.

## Exercises
1. Stream 100,000 synthetic login events and count by user using a `Counter`.
2. Find the ten noisiest client addresses without storing full event payloads.
3. Implement a bounded sliding-window failed-login count and explain O(n) time.
4. Compare list vs set membership with `timeit` and document measurement errors.
5. Create adversarial tests with missing keys, null values, duplicates, and huge fields.
