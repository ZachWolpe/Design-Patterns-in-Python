from abc import ABC, abstractmethod

class AbstractClass(ABC):
    """
    Defines a template method that contains a skeleton of 
    some algorithm, composed of calls to (usually) abstract primitve operations.
    
    Concrete subclasses should implement these operations, but leave the
    template method intact.
    """

    def template_method(self) -> None:
        """
        Template method defines the skeleton of an algorithm.
        """
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    # These operations already have implementations.

    def base_operation1(self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")

    def base_operation2(self) -> None:
        print("AbstractClass says: But I let subclasses override some operations")

    def base_operation3(self) -> None:
        print("AbstractClass says: But I am doing the bulk of the work anyway")

    # These operations have to be implemented in subclasses.
    @abstractmethod
    def required_operations1(self) -> None:
        pass

    def required_operations2(self) -> None:
        pass

    # "hooks": subclasses may override them, but it's not mandatory

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class ConcreteClass1(AbstractClass):
    """
    1. Implement all abstract operations of the base class.
    2. (Optionally) override some operations with a default implementation.
    """

    def required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")
    
    def required_operations2(self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")




class ConcreteClass2(AbstractClass):
    """
    Usually, concrete classes only override a small subset of base class' ops.
    """

    def required_operations1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")

    def hook1(self) -> None:
        print("ConcreteClass2 says: Overridden Hook1")



def client_code(abstract_class:AbstractClass) -> None:
    """
    Calls template method to execute the algorithm.
    Client code does not have to know the concrete class of an object it works with.
    """

    abstract_class.template_method()


if __name__ == '__main__':
    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass1())
    print("")

    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass2())