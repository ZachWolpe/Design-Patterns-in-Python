# Template Method
## Design Pattern XXII
### Behavioural Design Pattern
----

Template allows the user to define a skeleton of an algorithm in a superclass & then lets subclasses override specific steps of the algorithm without changing its structure.

Note:

The `Strategy` & `Template` pattterns achieve the same behaviour but:

- `Strategy` uses _*composition*_ to change the behaviour of an object.
- `Template` uses _*inheritance*_ to change the behaviour of an object.

---
# Application

- Let the client extend only a particular step of an algorithm, but not the entire algorithm, or its structure.
- Useful if several subclasses contain almost identical algorithms with some minor differences.


---
# Pros & Cons

**Pros**

- Remove duplicate code by adding superclasses.
- Allows the client to override only certain parts of a large algorithm.

**Cons**

- May impose unessarary limitations.
- May violate the _Liskov Substitution Principle_ by suppressing a defaul step implementation via a subclass.
- Harder to maintain as the number of steps in the template grows.