# State
## Design Pattern XX
### Behavioural Design Pattern
----

A design pattern where an objects `behaviour` is determined by it's `State`. A trigger is used to update the `State` of the object.

When the internal state changes it appears (to the client) that the object has changed it's class.

`(Finite) State Machines`: The formalized construct that describes `State` & `Transitions`.

## Finite State Machine

At any given moment a program can only be in $1$ of $n$ finite states. Within any unique state the program behaves differently, and the program can switch from one state to another instantiously. However, the available transition may be dependent on the current state. These transition dynamics are also finite & predetermined.




---
# Application

- Use when different behaviour is required in different states, the number of states is large & the app frequently changes between states.
- Use to avoid massive conditionals.
- Use to avoid duplicating code.



---
# Pros & Cons

**Pros**


- _Single Responsibility Principle (SRP)_
- _Open/Close principle_
- Eliminate bulk state conditional logic.

**Cons**

- Overkill if only a few states are required.


---
# Implementation

- `classic.py`:         Classical implementation of a finite state machine.
- `guru.py`:            Classical implementation of a finite state machine.
- `handmade.py`:        Explicit Trigger implementation of a finite state machine.
- `switch_based.py`:    Switch based implementation of a finite state machine.



