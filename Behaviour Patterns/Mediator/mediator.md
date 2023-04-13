# Mediator
## Design Pattern XVII
### Behavioural Design Pattern
----

A mediator reduces chaotic dependencies between objects by restricting direct communications between the objects and enforcing indirect collaboration through a mediator object.

Much like air traffic control. The planes don't talk to each other directly but they talk to the air traffic controller.

A mediator is thus _a component that facilitates communication between other components without them necessarily being aware of each other or having direct (reference) acess to each other._

---
# Application

- Complexity arising from tightly coupled classes can eleviated with a mediator.
- Use a mediator when reusability is impeded by a tight coupling between classes.
- Use a mediator when a set of objects communicate in well-defined but complex ways.

---
# Build

1. Each object in the system refers to the mediator.
    1.a. Likely by storing a reference to the mediator in an instance variable/property.
2. The mediator provides an interface for the objects to communicate with each other.
3. Event processing (e.g. Rx) libraries can be used to implement the mediator.