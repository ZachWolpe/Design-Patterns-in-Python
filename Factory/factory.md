# Factory Design Pattern
## Design Patterns in Python: Part III
----

The factory method provides an interface for creating objects in a superclass, but allows flexibility in the type of objects created by the subclasses.


---
# Pros & Cons

**Pros**


- The object/product can be decoupled from it’s creator, allowing for seamless extensions.
- Adhere to the *Single Responsibility Principle (SRP)* — making code easier to maintain/support.
- Adhere to the *Open/Close Principle* — new products can be introduced without breaking existing client code.

**Cons**

- Requires upfront work & adds complexity.

---
# Example


Suppose we write a class that creates points in some mathematical domain. An intuitive (naive) solution may introduce a few problems.

Firstly we are certain to violate the open-close principle if we add another CoordinateSystem at a later stage. Secondly, the initialiser is at risk of ballooning in arguments & functionality — becoming a God object.

It may be better to extract static `factory` methods to handle different coordinate systems, which are simple to follow, concise & can be extended as required.

If the number of factor methods required becomes substantial, it may be best to follow the *Separations of Concerns (SOC)* principle & move them into an external class.

If the `Factory` class requires state (or simply for readability) it can be moved into & initialised in the Point class.

