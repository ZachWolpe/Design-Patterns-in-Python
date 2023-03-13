# Builder Design Pattern
## Design Patterns in Python: Part II
----

Complex objects can’t always be created with a single initializer call. We can use a builder to construct (or build) objects in a stepwise fashion. A builder decouples the object and it’s constructor, allowing for different types of representations of an object using the same construction code.


---
# Pros & Cons

**Pros**


- Allows for step-by-step (piecewise) construction.
- The constructor can be reused.
- *Single Responsibility Principle (SRC)*: complex construction code can be isolated from business logic in the product.

**Cons**

- Code complexity increases as the pattern requires multiple new classes.


**Note**: Builder Inheritance: One may notice that the builder regularly violates the Open-Close principles (SOLID design). If you wish to circumvent this one can decouple the builder further by leveraging inheritance: incrementally adding functionality when needed by inheriting from the current builder. Using the most derived builder at runtime.

---
Implementation:

`builder_facets.py` demonstrates the builder method. `builder_inheritance.py` demonstrates the builder with inheritance.