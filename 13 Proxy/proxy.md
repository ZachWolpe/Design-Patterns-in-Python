# Proxy Design
## Design Pattern XIII
### Structural Design Pattern
----

Proxy allows you to provide a substitute for another object, controlling access to the original object.


---
# Application

- Virtual Proxy (Lazy initialization): Providing efficient access to a heavyweight service object.

- *Protection proxy* (access control). Allow only specific clients to access the service object.

- *Remote proxy*: access to a remote server.

- *Logging proxy*: log history of requests to the service object.

- *Caching proxy*: caching results of client requests.

- *Smart reference*: perform additional actions when an object is accessed.



---
# Pros & Cons

**Pros**

- Control the service object without the clients knowing about it.
- Provides a failsafe - keeps the service live even if the server is down.
- *Open/Close principle*: you can introduce new proxies without changing the service or clients.


**Cons**

- complexity.
- performance overhead.

---
# Provy vs Decorator

- Proxy: provides an identical interface to the service object.
- Decorator: provides an enhanced (additional funtionality) interface.

Additionaly a proxy is a wrapper around a purely _lazy_ object, that is not initialised until it is needed.

