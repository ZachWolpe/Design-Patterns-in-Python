# Command Design Pattern
## Design Pattern XV
### Behavioural Design Pattern
----

A command is an object that represents an instruction to perform a particular action (request). Containing all the information necessary to take the action.

Ordinary statements are perishable - cannot be undone. Assignmnents cannot be undone, & we cannot serialize a sequence of actions (calls).

Representing an operation as an object allows us to keep a record fo state, parameters & operations: allowing rollback & serialization.


---
# Application

- GUI commands (undo, redo, copy, paste, etc).
- Macri recording.

---
# Pros & Cons

**Pros**


- _Single Responsibility Priniciple (SPR)_: decoupling classes that invoke operations from classes that perform operations.
- _Open/Closed Principle (OCP)_: code is extendable without requiring modification.
- Defer execution of operations until required.
- Breakdown complex commands into smaller subsets.


**Cons**

- Sender & receiver code can be hard to read.


---
# Notes

The command pattern is used to:

- Encapsulate a request (operation & it's parameters) as an object.
- Define instructions & conditions for applying a command.
- (Optionally) define instructions for undoing a command.
- Create a command queue (composite) command (also known as macros).