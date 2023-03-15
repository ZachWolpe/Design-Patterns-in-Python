
# Interfact Segregation Principle =====================================================================
class Machine:
    def print(self, document):
        raise NotImplementedError
    def fax(self, document):
        raise NotImplementedError
    def scan(self, document):
        raise NotImplementedError

class MultiFunctionPrinter(Machine):
    def print(self, docment):
        pass
    def fax(self, document):
        pass
    def scan(self, document):
        return super().scan(document)

class OldFashionPrinter(Machine):
    def print(self, docment):
        pass
    def fax(self, document):
        raise NotImplementedError('fax not available.')
    def scan(self, document):
        return super().scan(document)

# Correct solution ---------------------------------++
# Many smaller base classes used as building blocks.
from abc import abstractmethod

class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class MyPrinter(Printer):
    def print(self, document):
        print(document)

class Photocopier(Printer, Scanner):
    def print(self, document):
        pass
    def scan(self, document):
        pass 

# If more extensive interface required -----------------++
class MultiFunctionDevice(Printer, Scanner):
    
    @abstractmethod
    def print(self, document):
        return super().print(document)
    
    @abstractmethod
    def scan(self, document):
        return super().scan(document)

class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner) -> None:
        super().__init__()
        self.scanner = scanner
        self.printer = printer

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)
# Interfact Segregation Principle =====================================================================