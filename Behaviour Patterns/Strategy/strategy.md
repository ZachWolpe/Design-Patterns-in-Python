# Stategy Pattern
## Design Pattern XXI
### Behavioural Design Pattern
----

The `Strategy pattern` uses a `Context` object that possesses a `Strategy` property - allowing interchange between concrete strategies when executing an algorithm.

It is useful for decoupling an algorithm into `higher level` & `lower level` parts.

1. Define an algorithm at a high level.
2. Define an interface that you expect each strategy to follow.
3. Provide a dynamic composition of strategies to the context object.

---
# Application

- Use when different variants of an algorithm within an object is required.
- Allows the client to specify the strategy at runtime.
- Useful when the many similar classes only differ in executing some behaviour.
- Useful to isolate business logic from implementation details.
- Useful to isolate code, internal data & dependencies of various algorithms from the rest of the code.
- Useful to avoid massive conditionals. 

---
# Pros & Cons

**Pros**

- Swap algorithms used inside an object at runtime.
- Isolate the implementation details of an algorithm from the code that relies on it.
- Replace inheritance with composition.
- _Open/Closed principle_: add strategies without having to modify the context.


**Cons**

- Overkill of only a few strategies are required.
- Client must be aware of different strategies.
- Many modern programming languages have `functional type support` that allows the implementation of different versions of an algorithm inside a set of anonymous functions - making the overkill of the strategy pattern redundant. 

