# Interpreter
## Design Pattern XVI
### Behavioural Design Pattern
----

Everything we do as developers involves _interpreters_ & _compilers_ - all programs need to _interpret_ text files, and all programming languages need to _compile_ source code into machine code.

An _Interpreter_ is a component that processes structured text data by turning into separate lexical tokens _(lexing)_ & then interpreting sequences of said tokens _(parsing)_.


---
# Sequence

The Interpreter generally follows two stages:

1. **Lexing** - the process of breaking a sequence of characters into meaningful chunks _(lexemes)_.
2. **Parsing** - the process of turning a sequence of lexemes into a structure (oop, tree, etc).
