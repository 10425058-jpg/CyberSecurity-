# 08 — Threads, processes, asyncio and resilient I/O

## Choose the right model
- **Threading:** convenient for blocking I/O; shared mutable state requires synchronization.
- **Multiprocessing / ProcessPoolExecutor:** useful for CPU-heavy tasks; inter-process transfer has cost, and worker startup differs across OSs.
- **Asyncio:** cooperative scheduling for many I/O tasks, when using non-blocking APIs.
- **Serial streaming:** often simplest and sufficiently fast for log pipelines.

The CPython GIL and free-threaded builds are version/build dependent; never assume threads automatically speed CPU-bound Python. Measure your workload and interpreter configuration.

```python
import asyncio

async def check_local_service(port: int) -> bool:
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection("127.0.0.1", port), timeout=0.5
        )
    except (OSError, TimeoutError):
        return False
    writer.close()
    await writer.wait_closed()
    return True

async def main():
    for port in (80, 443, 8080):
        print(port, await check_local_service(port))

if __name__ == "__main__":
    asyncio.run(main())
```
This example connects **only** to loopback. For any real network diagnostic, obtain authorization, define specific target bounds, and rate-limit requests.

## Failure and backpressure
Set explicit timeouts; use bounded queues and semaphores, exponential backoff with jitter for allowed APIs, cancellation cleanup, idempotency keys where relevant and graceful shutdown. Concurrency amplifies mistakes (bad retries can cause outages). Never fire unlimited requests or silently swallow task failures.

## Race conditions
Two operations reading/updating shared data can race. Use queues, locks, immutable messages or database transactions. A dictionary operation being individually atomic in one implementation is not a general concurrency contract.

## Exercises
1. Benchmark sequential vs bounded concurrent processing using 100 local delay simulations.
2. Add a semaphore limiting in-flight tasks to three.
3. Simulate cancellation during a local connection attempt and prove cleanup.
4. Explain the difference among timeout, retry, circuit breaker, and backpressure.

References: [asyncio](https://docs.python.org/3/library/asyncio.html), [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html).
