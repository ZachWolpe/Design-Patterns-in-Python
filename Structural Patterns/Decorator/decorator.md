# Decorator
## Design Pattern X
### Structural Design Pattern
----

Sometimes we want to augment a class with additional functionality. Rewriting code is one solution, but this is not always practical & violates the _open-close principle_. Additionally, you may want to share the new functionality accross many classes & ideally you want to keep the new functionality separate _(separation of concerns)_.

Two possible implementation procedures can handle this requirement:

 - **Inheritance**: Use inheritance to pass new functionality to existing modules.
 - **Decorator**: Wraps existing modules to facilitate additional behaviour without inheritance.


---
# Application

- Useful to assign additional beaviour at runtime.
- Useful to add functionality when it's awkward or difficult to extend an object's behaviour.
- Useful to attached new behaviour to multiple (independent) objects.


---
# Pros & Cons

**Pros**

- Possible to extend an objects behaviour without inheritance or subclasses.
- Extend functionality at runtime.
- Can add multiple decorators.
- _Single Responsibility Principle (SRP)_.

**Cons**

- Can be difficult to remove wrappers.
- Expected behaviour can be obfuscated.
- Order (usually) matters.
- Can make code messy.

---
# Implementation

- Functional decorator: `functional_decorator.py`
- Dynamic decorator: `dynamic_decorator.py`
- OOP decorator: `oop_decorator.py`
