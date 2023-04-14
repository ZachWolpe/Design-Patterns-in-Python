from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    Component Interface declares an `accept` method that should take the base visitor interface as an argument.
    """

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

class ConcreteComponentA(Component):
    """
    Each concerete class must implement the `accept` method such that
    it calls the corresponding visitors method.
    """

    def accept(self, visitor: Visitor) -> None:
        """
        Note that we're calling `visitConcreteComponentA` 
        (matching the current class name) - informing the visitor of the class component being used.
        """
        visitor.visit_concrete_component_a(self)
    
    def exclusive_method_of_concrete_component_a(self) -> str:
        # special methods that don't exist in the base class.
        return "A"
    

class ConcreteComponentB(Component):
    """
    Same here: visitConcreteComponentB => ConcreteComponentB
    """

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_component_b(self)

    def special_method_of_concrete_component_b(self) -> str:
        return "B"

class Visitor(ABC):
    """
    Interface declares a set of visitng methods that correspond to component classes.
    The signature of a visiting method allows the visitor to
    identify the exact class of the component that it's dealing with.
    """

    @abstractmethod
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        pass


"""
Concrete Visitors implement several versions of the same algorithm,
which can work with all concrete component classes.

Complex object structures (such as Composite trees) may benefit from the Visitor pattern.
It may be helpful to store interim state of the algorithm while executing the visitor's 
methods over various objects.
"""

class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1")
    
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor1")
    

class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor2")


def client(components: List[Component], visitor: Visitor) -> None:
    """
    Can run visitor ops over any set of elements without figuring out thier concrete classes.
    """
    for component in components:
        component.accept(visitor)


if __name__ == "__main__":
    components = [ConcreteComponentA(), ConcreteComponentB()]

    print("The client code works with all visitors via the base Visitor interface:")
    visitor1 = ConcreteVisitor1()
    client(components, visitor1)
    
    print("It allows the same client code to work with different types of visitors:")
    visitor2 = ConcreteVisitor2()
    client(components, visitor2)
    