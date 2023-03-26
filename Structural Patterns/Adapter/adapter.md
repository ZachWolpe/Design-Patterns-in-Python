# Adapter
## Design Patterns VII
----


Aptly named, the Adapter design patterns adapts an interface to work with another interface.

Adapter is a `structural design pattern` that allows objects with incompatible interfaces to collaborate.

----
# Application

1. An adapter can be used as a middle layer allows for compatibility between new code, legacy code & 3rd party software.
2. An adapter can be used when existing subclasses lack some common functionality, providing the functionality without adding to the superclass. One could wrap objects with missing features inside an adapter, similar to a `Decorator`.



----
# Pros & Cons

**Pros**

- _Single Responsibility Principle (SRP)_: The interface, conversion (adapter) & business logic can be isolated.
- _Open/Closed Principle_: Adapters can be introduced (open for extention) without changing existing code (closed for modification).
    
**Cons**

- The added complexity may not be worth the effort. Updating the original issue (cause for the adapter) may be simpler.



----
# Implementation

The `adapter.py` script demonstrates how to implement an adapter.

**Protip**: `caching` is often used to reduce redundency when implementing the adapter pattern. In python this can be acheived by storing a `cache = {}` dictionary with keys generating by the built in `hash()` function (providing a unique ID for each immutable object), prevent extraneous opporations & excess memory usage.

