# Composite
## Design Pattern IX
### Structural Design Pattern
----


Composite design composes objects into tree structures & uses these structures as if they were individual objects.


When implementing the composite pattern, individual (scalar) objects & composition (aggregate) objects are treated uniformly.


Higher level objects (leaf nodes) reference common interfaces from lower level objects (stems).

---
# Application

- Used to implement tree-like object structure.
- Sharing an interface across many leaf objects is required.
- The client code should treat both simple & complex objects uniformly.

---
# Pros & Cons

**Pros**


- Offers an intuitive way to work with complex tree structures, using `polumorphism` & `recursion` to one's advantage.
- _Open/Closed Principle (OPC)_ you can extend without modifying existing code. 

**Cons**

- A common interface may not fit multiple subclasses well, resulting in overgeneralisation & verbose code.

---
# Example

Describe.

---
# Implementation

Reference file `file.py`.
