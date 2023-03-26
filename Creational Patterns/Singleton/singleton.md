# Singleton
## Design Patterns in Python: Part VI
----

Singleton ensures that a class only has a single instance while providing a global access point to this instance.

Ensuring only a single instance exists is usually done to control access to some shared resources (like a database or file).

Further, providing a global access point to some object/data can, in general, be dangerous as the code may overwrite this data causing cascading bugs. For this reason, a singleton instance is safer than simply relying on global variables/objects.

When implementing a singleton class the constructor is usually kept private or fitted with additional logic to enforce a single instantiation.


---
# Pros & Cons

**Pros**


- Provides certainty that only a single instance exists.
- You have a global access point to that instance.
- The pattern can mitigate unnecessary expensive initializer calls.

**Cons**

- It regularly violates the *Single Responsibility Principle (SRP)*. The pattern solves two problems simultaneously.
- The Singleton pattern can mask bad design, for instance, when the components of the program know too much about each other.
- Additional complications can arise in a multithreading environment so that multiple instances are not created.
- Difficulties may arise in unit testing the client code because many test frameworks rely on inheritance when producing mock objects. A private constructor can necessitate a unique testing solution.

---
# Implementation

In Python, a singleton is a component which is only instantiated once. A common mistake is to define the Singleton logic in the `__new__` dunder. By design, python call `__init__` after `__new__` regardless of the logic in `__new__`.


Singleton is often implemented as:

- Decorator
- Metaclass
- Monostate

---
# Infinite Recursion

When I first discovered this `__call__()` block of code that calls itself, I was left wondering why it does not create an infinite recursion. A simple explanation is provided here.

This doesn’t cause an infinite recursion because you aren’t calling the `__new__` method of the `Singleton()` class. You are calling the `__new__()` method of it's super class which is still untouched and behaves as default.

Identify to explicitly calling `super(Singleton, cls).__new__(cls)`.


---
## Testing Singleton

It’s worth noting that it is bad practice for test cases to rely on a singleton instance directly, as this elevates risk in a production setting. Singleton objections should be replaceable by dummy objects in order to run tests.