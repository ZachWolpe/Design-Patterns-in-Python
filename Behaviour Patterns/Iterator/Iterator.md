# Iterator
## Design Pattern XVII
### Behavioural Design Pattern
----

An *_iterator_* allows you to traverse elements of a collection without exposing its underlying representation (stack, list, queue, tree, etc.)

_*Iteration*_ or _traversal_ is a core functionality of many data structures. An iterator is therefore defined as:

_"An object that facilitates the traversal of a data structure."_


---
# Implementation

In `python` the iterator protocol requires:

- `__iter__()` to expose the iterator object, which uses the
- `__next__()` to return each of the iterated elements.


The `__next__()` method should raise a `StopIteration` exception when there are no more elements to return: `raise StopIteration()`.


---
# Application

- Use when you wish to hide the complexity of the data structure from the client.
- Use to reduce duplication of the traversal code (RL dynamic programming).
- Use to provide a standard interface for traversing different data structures.

---
# Notes

Stateful iterators _*cannot*_ be recursive, using the `yield` keyword is much cleaner.