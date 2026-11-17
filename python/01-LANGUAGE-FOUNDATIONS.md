# 01 — Python language foundations

**Goal:** read and write small programs confidently without depending on an assistant.

## 1. Python's execution model
Python programs are modules of statements; CPython commonly compiles source to bytecode interpreted by its virtual machine. Variables are **names bound to objects**, not fixed-size boxes. Objects have identity, type, and value. Python is dynamically typed, but type annotations can document expected values and aid static checking. Indentation defines blocks.

```python
name = "Ada"                 # str (immutable)
count = 3                    # int, arbitrary precision
ratio = 0.75                 # float, approximate binary number
enabled = True               # bool
missing = None               # sentinel: no value
print(f"{name}: {count * ratio:.2f}")
```

`is` compares identity; `==` compares values. Avoid `is` for integers/strings; `is None` is correct. Mutable objects may share references; rebinding is not mutation. Beware aliasing when passing lists or dicts.

## 2. Expressions and operators
Arithmetic: `+ - * / // % **`. Comparisons: `== != < <= > >=`. Boolean: `and or not` uses short-circuit evaluation; `in` tests membership. Bitwise operations: `& | ^ ~ << >>` for flags, masks and protocol fields. Parenthesize mixed boolean expressions to make security checks auditable. Remember `bool([])`, `bool("")`, and `bool(0)` are false, but a missing value is not always equivalent to an invalid one.

## 3. Strings, bytes and encoding
A `str` is Unicode text; `bytes` is an 8-bit sequence. Network packets and file digests use bytes. Encoding text to UTF-8 and decoding bytes must be explicit; wrong decoding corrupts evidence.
```python
message = "login failed"
wire = message.encode("utf-8")
assert wire.decode("utf-8") == message
assert b"\x00\xff".hex() == "00ff"
```
Know slicing (`s[start:stop:step]`), zero-based indexing, negative indices, string methods, and raw strings for regular expressions. Prefer `repr()` when debugging invisible characters.

## 4. Control flow
```python
severity = 7
if severity >= 8:
    verdict = "critical"
elif severity >= 5:
    verdict = "review"
else:
    verdict = "informational"

for event in ["ok", "fail", "fail"]:
    if event == "fail":
        print("review event")
```
Use `while` when termination depends on a condition, `for` when traversing an iterable. `break` exits a loop; `continue` skips one iteration; `pass` is a placeholder. Python `match` is useful for structural pattern matching, not a substitute for verifying untrusted input.

## 5. Functions and input contracts
```python
def categorize_failed_attempts(count: int) -> str:
    if count < 0:
        raise ValueError("count must be nonnegative")
    return "review" if count >= 5 else "normal"
```
Arguments can be positional, keyword, keyword-only (`*`), or positional-only (`/`). Default parameters are evaluated once at definition time: never use mutable defaults such as `items=[]`; use `None` and initialize inside.

## 6. Common security-relevant mistakes
- Concatenating untrusted input into a shell command, SQL statement, path, or HTML fragment.
- Using `eval()`, `exec()`, or unsafe deserialization on user data.
- Assuming `input()` returns a number; it always returns text and needs validation.
- Using `random` for credentials; use `secrets`.
- Forgetting exceptions and encoding errors when parsing external text.
- Using bare `except:`, which can hide interrupts and programming defects.

## Exercises
1. Write a function that accepts a nonnegative count and returns a severity label; test -1, 0, 4, 5, 100.
2. Convert a Unicode event message to UTF-8 bytes and print its hexadecimal form.
3. Parse a text severity input safely: reject decimals, negatives and extremely long inputs.
4. Explain identity vs equality using two lists with the same contents.
**Checkpoint:** predict output and types of ten short snippets without running them, then confirm experimentally.

References: [official tutorial](https://docs.python.org/3/tutorial/), [language reference](https://docs.python.org/3/reference/).
