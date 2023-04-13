from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Context():
    """
    The Context defines the interface of interest to the client.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Context (usually) accepts a strategy through the constructor,
        but also provides a setter to change it at runtime.
        """
        self._strategy = strategy
    
    @property
    def strategy(self) -> Strategy:
        """
        Context does not need to know the concrete class of a strategy - 
        but only contain a reference to it.
        """
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Update Strategy object at runtime.
        """
        self._strategy = strategy
    
    def business_logic(self) -> None:
        """
        Context --> delegates work to the strategy object.
        (instead of implementing multiple versions of the algorithm)
        """
        print('Context: delegate work to the strategy object...')
        result = self._strategy.execute(['a', 'b', 'c', 'd', 'e'])
        print(','.join(result))

class Strategy(ABC):
    """
    Interface declares operations common to all supported versions of some algorithm.

    Context uses this interface to call the algorithm defined by Concrete Strategies.
    """
    @abstractmethod
    def execute(self, data: List) -> List:
        pass


"""
Concrete Strategies implement the algorithm while following the base Strategy interface.
The interface makes them interchangeable in the Context.
"""


class ConcreteStrategyA(Strategy):
    def execute(self, data: List) -> List:
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def execute(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == '__main__':
    # Client code picks the concrete strategy and passes it to the context.
    # Client should be aware of different strategies.

    context = Context(ConcreteStrategyA())
    print('Client: Strategy is set to normal sorting.')
    context.business_logic()
    print()
    context.strategy = ConcreteStrategyB()
    print('Client: Strategy is set to reverse sorting.')
    context.business_logic()