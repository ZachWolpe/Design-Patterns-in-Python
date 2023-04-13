# Memento Design Pattern
## Design Pattern XVIII
### Behavioural Design Pattern
----

Make a snapshot of an object's state & restore it later - without revealing the details of its implementation.

Similar to the Command design pattern, but simplier in that we save a snapshot at every state change.

---
# Application

- When you wish to restore previous state at a later stage.
- Use the pattern when direct access to the object's fields/getters/setters violates its encapsulation.

---
# Pros & Cons

**Pros**

- Simplyfies the originators code by letting the caretaker maintain the history of the originator's state.
- provide a snapshot of state without violating encapsulation.

**Cons**

- RAM intensive.
- Many dynmaic programming languages (PHP, Python, JS) cannot guarantee that the object's state will not be changed by other objects.

---
# Example

Describe.

---
# Implementation

Reference file `file.py`.
