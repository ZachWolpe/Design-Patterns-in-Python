# Chain of Responsibility
## Design Pattern XIV
### Behavioural Design Pattern
----

This design pattern passes requests along a chain of `handlers`. Each handler either processes the request or passes it to the next handler.

**Command Query Separation**

_CQS_ is a principle of imperative programming that states that every method should either be a *command* or a *Query* but not both.

- A *command* is a method that performs an action.
- A *query* is a method that returns data to the caller.

---
# Application

- Use `CoR` f the order of requests is conditional on the type of request.
- Use when an ordered sequence is required.
- Use `CoR` when the set of handlers & their order aren't known until runtime.

---
# Pros & Cons

**Pros**

- Control the order of request handling.
- _Single Responsibility Principle (SRP)_: decouple classess that invoke operations from classes that perform operations.
- _Open/Closed Principle (OCP)_: easy to extend the chain of responsibility by adding new handlers.

**Cons**

- Danger of creating `spaghetti code`.
- Performance issues.

---
# Implementation

- `guru.py` demonstrates the implementation's core structure.
- `method.py` offers an example of a method-based chain implementation.
- `broker.py`