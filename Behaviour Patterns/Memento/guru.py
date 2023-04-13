from __future__     import annotations
from datetime       import datetime
from random         import sample
from string         import ascii_letters, digits
from abc            import ABC, abstractmethod


class Originator():
    """
    The Originator:
        - holds sates.
        - defines a method for saving the state inside a momento.
        - defines a method for retoring the state from it.
    """

    _state = None

    def __str__(self) -> str:
        return f'Originator state: {self._state}'

    def __init__(self, state:str) -> None:
        self._state = state
    
    def do_something(self):
        print('Updating state...')
        self._state = self._generate_state(44)
        print(self)
    
    def _generate_state(self, ln=77):
        return "".join(sample(ascii_letters, ln))
    
    def save(self) -> Momento:
        # save current state
        return ConcreteMomento(self._state)

    def restore(self, momento:Momento):
        print('Restoring state...')
        self._state = momento.get_state()
        print(self)


class Momento(ABC):
    """
    Interface provides a way to:
        - Retrieve the momento's metadata
        - Without exposing the Originator's state
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_data(self) -> str:
        pass 
    

class ConcreteMomento(Momento):
    def __init__(self, state:str) -> None:
        self._state = state
        self._date  = str(datetime.now())[:19]

    def get_state(self):
        return self._state
    
    def get_name(self):
        return f'[{self._date}]  state:{self._state[0:9]}...'
    
    def get_data(self) -> str:
        return self._date
    


class Caretaker():
    """
        - Independent of the Concrete Momento class.
        - Does not have access to the originator's state, stored inside the momento.
        - Works with all momento's via the base Mememnto interface.
    """

    def __init__(self, originator:Originator) -> None:
        self._mementos       = []
        self._originator    = originator

    def backup(self):
        print(f'Caretaker: Saving Originator\'s state...')
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f'Caretaker: storing state to {memento.get_name()}')
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    
    def show_history(self) -> None:
        for momento in self._mementos:
            print(momento.get_name())


if __name__ == '__main__':
    originator  = Originator('super-duper-super-puper-super')
    caretaker   = Caretaker(originator)
    
    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()
    print('\nClient: rollback:\n')
    caretaker.undo()
    caretaker.undo()    

