
# Abstract Factory Design Pattern
## Design Patterns in Python: Part IV
----

Abstract Factory allows one to families/collectives of related objects without specifying their concrete classes.

It is useful if we are dealing with a hierarchy of types, requiring a hierarchy of factories.



---
# Pros & Cons

**Pros**

- Enforce certain object/product standards by using the family interface.
- *Single Responsibility Principle (SRP)*: one can extract the creational code, making code easier to maintain/support.
- *Open-Closed Principle (OCP)*: code is amenable to extensions.

**Cons**

- Increased complexity due to the introduction of many interfaces/classes.


---
# Example

Suppose an abstract factory class is used to generate different hot drinks (subclasses) belonging to the same family.