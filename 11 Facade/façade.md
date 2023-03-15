# Façade
## Design Pattern XI
### Structural Design Pattern
----

Occludes the complexity of a system by providing a simpler interface to the client. The façade defines a higher-level interface that makes the subsystem easier to use.


Although a Façade provides a simplified API over a set of classe, you may wish to allow users to 'escalate' were required, having access to lower level functionality.

---
# Application

- You desire an interface over a complex subsystem.
- You wish to structure a subsystem into layers.

---
# Pros & Cons

**Pros**

- You can provide a simpler client interface. 

**Cons**

- The façade may become a god object.
