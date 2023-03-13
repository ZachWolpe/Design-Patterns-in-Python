# Prototype
## Design Patterns in Python: Part V
----

The prototype design pattern allows you to copy existing objects without making your code dependent on their classes.

Copying an object entirely can introduce a few problems. Some private fields may not be visible outside of the object itself; the copy is often dependent on the class or interface used to generate the original object — creating an additional dependency; concrete classes may be obscured, hiding arguments/methods used in particular instantiations.

The prototype pattern includes the cloning process in the actual objects being cloned, declaring an interface that supports cloning, & decoupling the instantiation code and the object class. All fields and attributes are internal to the interface, and they’re accessible (in most programming languages).


---
# Pros & Cons

**Pros**

- Objects can be cloned without coupling to their concrete classes.
- Reduces repeated initialization code.
- It’s easy to reproduce complex objects.
- Offers an alternative to inheritance.


**Cons**

- Circular referencing can arise when cloning complex objects, which is convoluted, counterintuitive and confusing.


---
# Implementation

`Deep Copy`

We rely on pythons' built-in copy module to implement this pattern. Extract from the documentation:

_“The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):_

- _A `shallow copy` constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original._
- _A `deep copy` constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.”_


If we simply use a `x = y` operator (or a shallow copy `copy.copy()`) to create `x` as a copy of `y` we only instantiate a pointer, thus updating `x`’s attributes will erroneously update `y`‘s. The function `copy.deepcopy()` instead recursively duplicates the data associated with y into x.


In a production system, it is often better to combine the `prototype` & `factory` design patterns. That way a collection of pattern interfaces (& their associated relationships) are bundled. This also allows the internal state (in my example, default values) to be dependent on the interface and not another concrete object.
