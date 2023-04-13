from __future__ import annotations
from abc        import ABC

class Mediator(ABC):
    def notify(self, sender:object, event: str) -> None:
        pass


class MediatorConcrete(Mediator):
    def __init__(self, components:list[BaseComponent]) -> None:
        self.components = components
        for c in self.components:
            c.mediator = self
    
    def notify(self, sender:object, event:str) -> None:
        for c in self.components:
            if event == c.event_name:
                print(f'Mediator triggering {c.event_name}!')
                self.components[0].trigger()


class BaseComponent(ABC):
    """Basic functionality of storing a mediator's instance inside a component object"""

    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator  = mediator
        self.event_name = None

    @property
    def mediator(self) -> Mediator:
        return self._mediator
    
    @mediator.setter
    def mediator(self, mediator:Mediator) -> None:
        self._mediator = mediator

    
    
class ComponentInterface(BaseComponent):
    def __init__(self, mediator: Mediator = None) -> None:
        super().__init__(mediator)
        self.event_name = None

    "Required functionality."
    def execute(self):
        self.mediator.notify(None, self.event_name)
    
    def trigger(self):
        print(f'{self.event_name} trigger successfully.')


"""
Concrete Compnents: actual instantiations implement unique functionality.
"""

class cmpt_a(ComponentInterface):
    def __init__(self, mediator: Mediator = None) -> None:
        self.event_name = 'Component A'
    
    
class cmpt_b(ComponentInterface):
    def __init__(self, mediator: Mediator = None) -> None:
        self.event_name = 'Component B'



if __name__ == '__main__':
    c1 = cmpt_a()
    c2 = cmpt_b()
    
    mediator = MediatorConcrete([c1,c2])

    print('Trigger 1...')
    c1.execute()
    print('Trigger 2...')
    c2.execute()
    print('Fini.')
