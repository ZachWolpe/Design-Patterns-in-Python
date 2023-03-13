 # SOLID Design Principles
## Design Patterns in Python: Part I
----

**SOLID Design Principles for Object-Oriented Programming.**


The structural design of OOP software can take any form. The SOLID design principles are a set of (best-practice) OOP class structure heuristics to improve your code.

The goal of SOLID design is simple:

_“To create understandable, readable, and testable code that many developers can collaboratively work on.”_

The principles, compiled to form the SOLID acronym, are:

  - *S* — Single Responsibility Principle
  - *O* — Open-Closed Principle
  - *L* — Liskov Substitution Principle
  - *I* — Interface Segregation Principle
  - *D* — Dependency Inversion Principle


---

## Single Responsibility Principle

*A class should only do one thing (separation of concerns) and therefore only has a single reason to change.*

#### Example

Implementation: `srp.py`.

**Explanation**

Suppose we implement a `Journal` class that is used to store journal entries. The class allows one to add or remove journal entries.

Adding functionality to load or save a given journal may be desirable. Although implementing a `save_to_file()` or `load_from_file()` method in the Journalis straightforward, it may cause unwanted side effects that violate the SRP (single responsibility principle).

In a real application, persistence management of a journal (saving and loading) may be applied to other object types. A centralised design avoids code duplication. It is also undesirable to create `“God objects”`: bloated classes that perform all tasks.

It is more elegant to create another class to abstract the persistence methods.



## Open-Closed Principle

*Classes should be open for extension and closed for modification.*

*Modification* refers to changing the code of an existing class, *Extension* refers to adding new functionality.

Modifying existing (tested) code can cause bugs. Avoid touching tested, reliable, (mostly) production code. Interfaces (or abstract classes) can be used to circumvent this issue.

Interfaces allow us to change the explicit logic after implementing a solution, without modifying the initial solution.

#### Example

Implementation: `ocp.py`.

**Explanation**

Suppose we have a number of products, each with 3 attributes (name, colour & size) and we want to implement a product filter to sort through products. A naive solution would be to write a class `ProductFilter` that possesses a method for each filter type.

Although this solution works, it violates the open-closed principle if we want to add a new filter at a later stage. It may be advised to instead implement base classes.

The filter can be switched out as desired.

**Aside**: This has the additional benefit of preventing a state-space explosion in this particular example: growing the code disproportionally in the number of filters.


## Liskov Substitution Principle

*The Liskov Substitution Principle sates that subclasses should be substitutable for their base classes.*

More specifically, if `class B` is a subclass of `class A`, the expected behaviour should not change when using methods from B instead of methods from A. The child class should only extend the behaviour of the base class.

To improve predictability and avoid unexpected obscured bugs, we should be able to pass any object of `class B` to any method that expects an object of `class A` and the method should not return any unexpected output.


#### Example

Implementation: `lsp.py`.

**Explanation**

Suppose we have a `rectangle` class with a method to return the area. We use private `properties` and `setters` to ensure control of the rectangle’s attributes.

We declare an external function to compute the area and expected area, given certain parameters.

We then derive a subclass to handle squares.

Finally, we instantiate both classes and use the `fetch_area()` method.

The function `FetchArea()` now only works on the base class rectangle and not the subclass square— violating the Liskov Substitution Principle.

## Interface Segregation Principle

*Many client-specific interfaces are better than one general-purpose interface. Clients should not be forced to implement a function they do not need.*

This ensures class models are flexible, extendable, & the clients do not need to implement any irrelevant logic.

#### Example

Implementation: `isp.py`.

**Explanation**

Consider an interface for a modern printer. It hosts a number of features. The interface can be used to implement a modern multi-function printer.

If, however, we wish to implement an older (simpler) printer using the same interface some of the functionality becomes superfluous.

Creating an instance of `OldFashionPrinter` may be confusing and lead to unexpected behaviour. The class contains a fax method — despite not doing anything. It is verbose and misleading. One may implement warnings or exceptions to alert the client, however, raising these elements may cause downstream issues in larger applications (crashing the application in an obscured way).

It is instead preferable to decouple the interfaces. That way downstream classes inherit exactly what they need.

If a multi-facet interface is still required, it can be created by inheriting from the base classes.

## Dependency Inversion Principle

*Classes should depend on interfaces or abstract classes, and not concrete classes or functions.*

#### Example

Implementation: `dip.py`.

**Explanation**

Suppose we define a `person` class and a class that stores the relationships between people. We then define a class `Research` to search for all parents named “John”.


This yields the expected behaviour but violates the Dependency Inversion Principle.

Violation: The Research class (high-level module) depends on the data structure of the relationships class (low-level module (storage)). The code is now vulnerable to the implementation of the relations data structure.

It is better to depend on abstract classes &/or interfaces to improve the robustness of the code.

This can be achieved by introducing an interface module RelationshipBrowser that ensures certain functionality is implemented by its sub-classes. That way the research class can depend on the structure of the interface.

---
# Summary

## Single Responsibility Principle

- A class should only have one reason to change.
- *Separation of Concerns (SOC)*: independent tasks should be handled by different classes.

## Open-Closed Principle

- Classes should be open for extension but closed for modification.

## Liskov Substitution Principle

- Base types should be substitutable by subtypes.
- This ensures that we maintain the expected behaviour.

## Interface Segmentation Principle

- Decouple interfaces. Don’t add too much complexity to a single interface.
- YAGNI — You Ain’t Going to Need it!

## Dependency Inversion Principle

- Classes/modules should depend on abstract classes/interfaces and not instances.
Use abstractions.

