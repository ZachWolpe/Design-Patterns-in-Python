# Observer
## Design Pattern XIX
### Behavioural Design Pattern
----

Define a subscription mechanism to notify objects about events.

An _observer_ is an object that listens to events & the _observable_ is the object that emits events.



---
# Application

- Manage state dependencies between objects.
- Allows some object to `observe` another to monitor changes.

---
# Pros & Cons

**Pros**


- Allows for loosely coupled communication between objects - by `subscription` & `unsubscription`.
- Allows for `one-to-many` communication between objects.
- `Open/Closed principle`.
- Can establish the relationship between objects at runtime.

**Cons**

- Property notifications can become difficult to manage.
- Potential spaghetti code.
- Difficult to debug.
- Unordered subscription execution.

---
# Implementation Warning

1. As demonstrating in `property-dependencies.py` it is easy for complex dependencies to arise between properties. This can be mitigated by using a mediator.
