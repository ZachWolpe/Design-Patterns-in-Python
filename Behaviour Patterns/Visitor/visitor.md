# Interpreter
## Visitor Pattern XXIV
### Behavioural Design Pattern
----

Visitors allow the separation of algorithms from the objects on which they operate.

If an exisiting object requires additional functionality, a visitor can be implemented to perform the new behavior.


A (niave) intrusive approach to adding functionality to an existing data structure would be to simple modify all existing objects to perform the required additonal behaviour. Visitors can be used to, more elequently, add functionality by creating the visitor.

---
# Application

- Useful to perform an operation on all elements of a complex object structure (for example, an object tree).
- Useful to clean up business logic of auxiliary behaviours.
- Useful when a behaviour is only applicable to some classes of a class hierarchy.


---
# Pros & Cons

**Pros**


- _Single Responsibility Principle_.
- _Open/Closed Principle_.
- Visitors may accumulate useful state during a data strucuture traversal.

**Cons**

- Difficult to maintain: all visitors require updating each time a class gets added to or removed from the element hierarchy.
- Visitors may lack the (required) access to private fields & methods of the elements that they're suppsed to handle.

