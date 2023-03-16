# Flyweight (Cache)
## Design Pattern XII
### Structural Design Pattern
----

Flyweight (or Cache) is a way of optimising memory usage by sharing data between objects.

To implement the flyweight pattern, you store some shared (_*intrinsic state*_) extrernally to each object. Each object then stores only the unique (_*extrinsic state*_) data. This way, you can share the same data between multiple objects, saving memory.

---
# Application

- Use this design pattern when a large number of objects have redundant or overlapping characteristics - to optimise memory.

---
# Pros & Cons

**Pros**

- Save RAM.

**Cons**

- Often trading RAM for CPU cycles.
- Increased complexity.
