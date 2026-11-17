# 07 — Iterators, generators, context managers and decorators

## Iteration protocol
An iterable returns an iterator via `iter()`; an iterator provides successive values via `next()` and raises `StopIteration` at exhaustion. Generator functions use `yield`, suspending between items rather than allocating a complete collection.

```python
from collections.abc import Iterator
from pathlib import Path

def nonblank_lines(path: Path) -> Iterator[str]:
    with path.open("r", encoding="utf-8") as source:
        for line in source:
            value = line.strip()
            if value:
                yield value
```
A generator keeps the file open while iterating and closes it when execution finishes or is finalized; consume promptly or use an explicit resource boundary when ownership matters.

## Context managers
`with` invokes enter/exit protocols; it is crucial for closing sockets, files, locks and temporary artifacts even on exceptions.

```python
from contextlib import contextmanager
from time import monotonic

@contextmanager
def stopwatch():
    start = monotonic()
    try:
        yield
    finally:
        print(f"elapsed: {monotonic() - start:.3f}s")
```

## Decorators
A decorator wraps a function or class. Keep signatures, metadata (`functools.wraps`), exceptions and authorization decisions intact. Do not rely on a decorator as the **only** access-control layer unless its coverage is tested.

## Async iteration
`async for` processes asynchronous iterables; `async with` manages asynchronous resources. They are useful for long-lived network streams but need clear shutdown/cancellation paths.

## Exercises
1. Stream the first 100 malformed lines out of a massive JSONL file.
2. Create a context manager that records duration even if its body fails.
3. Explain lazy vs eager evaluation with memory measurements.
4. Verify an early-terminated generator closes its resources under explicit cleanup.
