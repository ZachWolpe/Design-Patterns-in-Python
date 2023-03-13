# Bridge
## Design Pattern VIII
----

This pattern is about connecting components through abstractions.

A bridge prevents a *Cartesian product complexity explosion*. More simple, the number of combinations required grows exponentially in the feature space. This is achieved through decoupling the abstraction & implementation layer.

*Abstraction* (also called _interface_) is a high-level control layer for some entity. This layer isn’t supposed to do any real work on its own. It should delegate the work to the *implementation* layer (also called *platform*).


---
# Application

- Splitting up a monolithic class that has several variants of some functionality.
- Bridge can be used to extend a class on several dimensions.
- Bridge design is useful when one needs to switch implementations at runtime.


---
# Pros & Cons

**Pros**


- High-level abstractions.
- *Open/Closed Principle*. You can introduce new abstractions and implementations independently from each other.
- *Single Responsibility Principle (SRP)*. You can focus on high-level logic in the abstraction and on platform details in the implementation.

**Cons**

- Increase complexity in setup.

---
# Example

Suppose we write the code to flight navigation software for the Lockhead Martin. For a given plan, need a class that implements a number of flight & defence functions. As the number of planes & variants grows, the number of combinations grows exponentially, the bridge allows us to decouple the pairing between variants.

The `Attack` class is abstracted & passed to the `FighterJet` class.

---
# Implementation

The `bridge.py` script demonstrates how to implement an bridge.

