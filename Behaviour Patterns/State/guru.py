from __future__ import annotations
from abc import ABC, abstractmethod

class Context:
    """
    Context defines the interface of interest to the client.
    Maintains a reference to an instance of a `State` subclass, which represents the current state of the Context.
    """

    _state = None

    """
    REFERENCE: reference to the current state of the Context.
    """

    def __init__(self, state:State) -> None:
        self.transition_to(state)
    
    def transition_to(self, state:State):
        """
        The Context allows changing the State object at runtime.
        """
        print(f'Context: Transition to {type(state).__name__}')
        self._state         = state
        self._state.context = self
    
    """
    The Context delegates part of its behaviour to the current State object.
    """

    def request1(self):
        self._state.handle1()
    
    def request2(self):
        self._state.handle2()


class State(ABC):
    """
    Base State class declares methods that 
        - all Concrete State's should implement.
        - provides a backreference to the Context object, associated with the State.
          The backreference can be used by States to transition the Context to another state.  
    """

    @property
    def context(self) -> Context:
        return self._context
    
    @context.setter
    def context(self, context:Context) -> None:
        self._context = context
    
    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


    """
    Concrete States implement various behaviours, associated with a state of the Context.
    """


class ConcreteStateA(State):
    def handle1(self) -> None:
        print('Concrete State A --> handles(request1)')
        print('Concrete State A wants to change the state of the context.')
        self.context.transition_to(ConcreteStateB())
    
    def handle2(self) -> None:
        print('Concrete State A --> handles(request2)')

class ConcreteStateB(State):
    def handle1(self) -> None:
        print('Concrete State B --> handles(request1)')

    def handle2(self) -> None:
        print('Concrete State B --> handles(request2)')
        print('Concrete State B wants to change the state of the context.')
        self.context.transition_to(ConcreteStateA())

if __name__ == '__main__':
    context = Context(ConcreteStateA())
    context.request1()
    context.request2()