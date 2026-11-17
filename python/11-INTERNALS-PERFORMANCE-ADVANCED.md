# 11 — Python internals, performance and advanced topics

## Language mechanics
Understand scopes (LEGB), closures, descriptors, properties, dunder methods, metaclasses (only when justified), decorators, generators, coroutine state, exception groups, pattern matching, typing protocols, and the import system. Learn how mutable references and garbage collection affect long-running agents.

## Python runtime and memory
Use `sys.getsizeof` only as a shallow indicator. Profile allocations with `tracemalloc`, time with `time.perf_counter` and `cProfile`, and test production-like data volumes. Use streaming parsers, bounded caches, memoryviews and chunked I/O before introducing native extensions. Offload specialized calculations to trustworthy libraries when appropriate.

```python
import tracemalloc
tracemalloc.start()
data = [str(i) for i in range(10_000)]
current, peak = tracemalloc.get_traced_memory()
print({"current_bytes": current, "peak_bytes": peak})
tracemalloc.stop()
```

## Native interfaces and isolation
Learn C extensions, CFFI/ctypes risk, integer bounds across languages, shared libraries, subprocess isolation, FFI calling conventions and serialization boundaries. **Never use ctypes or a native library on untrusted inputs without understanding bounds and memory safety.**

## Robust long-running tools
- Resource caps: memory, CPU, file descriptors, concurrent requests.
- Checkpointing and idempotent replay for telemetry ingestion.
- Structured logging, error budgets, metrics, tracing and health checks.
- Data retention, secure deletion caveats, access control and audit trail design.
- Threat model the tool itself: it may parse malicious packets and adversarial logs.
- Guard plugin loading and supply-chain trust; do not deserialize Python objects from third parties.
- Review cross-platform differences in paths, timestamps, networking and process models.

## Advanced exercises
1. Profile a generator-based log parser vs `readlines()` on a synthetic dataset.
2. Bound memory use in a burst-detection pipeline.
3. Explain why faster code is not always safer and what resource budgets must be tested.
4. Make an import-safe package and verify that importing it does not touch network/filesystem.
