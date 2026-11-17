# 06 — Object-oriented design and maintainable security tools

## Core concepts
- **Class:** declares a type's data and behavior; **instance:** concrete object.
- **Encapsulation:** expose a small stable interface; underscore is a convention, not access control.
- **Composition:** build behavior from collaborating objects; often preferable to deep inheritance.
- **Inheritance:** subclass when substitution really holds; override behavior carefully.
- **Polymorphism:** multiple implementations behind a common interface or `Protocol`.
- **Dataclass:** concise data models; `frozen=True` discourages accidental updates but nested mutable fields can still change.

```python
from dataclasses import dataclass
from typing import Protocol

@dataclass(frozen=True)
class Event:
    actor: str
    action: str

class Rule(Protocol):
    def matches(self, event: Event) -> bool: ...

class FailedLoginRule:
    def matches(self, event: Event) -> bool:
        return event.action == "login_failure"

def evaluate(rule: Rule, events: list[Event]) -> list[Event]:
    return [event for event in events if rule.matches(event)]
```

## Architecture patterns
- Ports and adapters: keep the analysis core independent of storage vendors.
- Strategy: interchangeable detection rules.
- Repository: abstract persistence behind a narrow interface.
- Dependency injection: pass clock, client, filesystem adapter, config, and logger to test without real systems.
- Observer/event bus: notify consumers without coupling every component.
- Command: package repeatable actions with explicit arguments and outcomes.

## Abuse-resistant engineering
Define resource budgets, timeouts, cancellation and retry policy. Operations that mutate security controls must be explicitly authorized and idempotent when possible. Document rollback and audit trails. Avoid plugin systems that import arbitrary code from untrusted paths.

## Exercises
1. Add a second detection rule implementing `Rule`.
2. Replace a live API client with an in-memory test double.
3. Draw dependencies for a file-ingest → normalize → detect → report application.
4. Refactor a 500-line script into CLI, parser, domain logic and output modules.
