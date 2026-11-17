# 03 — Functions, modules, typing, and API design

## Good function boundaries
A function should have one clear responsibility, documented inputs/outputs, predictable failures, and no unnecessary hidden I/O. Separate **parse → validate → analyze → report** so that each stage can be tested independently. Prefer dependency injection to global state.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Alert:
    subject: str
    count: int
    severity: str

def decide_alert(subject: str, count: int, threshold: int = 5) -> Alert | None:
    if not subject or count < 0 or threshold < 1:
        raise ValueError("invalid alert parameters")
    if count < threshold:
        return None
    return Alert(subject=subject, count=count, severity="review")
```

**Python type annotations do not enforce runtime validation.** Use checks at trust boundaries and a dedicated validation layer when schemas are complex. Common constructs: `list[str]`, `dict[str, int]`, `str | None`, `Iterable`, `Protocol`, `TypedDict`, `Literal`, generics, narrowing, `Callable`, and `TypeVar`.

## Modules, packages, namespaces
`import module` is preferable when namespace clarity matters. `if __name__ == "__main__":` prevents executing CLI work on import. Organize modules by business responsibility: `parsers.py`, `models.py`, `detection.py`, `cli.py`. Avoid import-time network calls, mutable global registries, circular imports, and shadowing the standard library (e.g. naming your file `json.py`).

## Functional tools and closures
Understand `map`, `filter`, generators, comprehensions, `functools.partial`, decorators, closures, and `functools.lru_cache`. Cache only pure computations or carefully scoped data; caching credentials or authorization outcomes can introduce privacy and consistency bugs.

```python
from functools import wraps
from time import perf_counter

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {perf_counter() - start:.6f}s")
        return result
    return wrapper
```

## Security-oriented design
- Parse first; validate field types, lengths, ranges, and allowed values.
- Raise specific exceptions for invalid data; preserve original causes where appropriate.
- Keep secrets out of arguments shown in process listings and out of logs.
- Use immutable values for normalized, verified records where possible.
- Return structured results; avoid implicit printing inside reusable functions.
- Be explicit about timezone-aware timestamps and identifier canonicalization.

## Exercises
1. Convert a monolithic log parser into four independently testable functions.
2. Add precise typing and docstrings; run a static checker.
3. Design a dataclass for an alert and reject invalid severity/count values.
4. Explain why annotations alone do not block a string sent to an `int` argument.

References: [typing](https://docs.python.org/3/library/typing.html), [dataclasses](https://docs.python.org/3/library/dataclasses.html).
