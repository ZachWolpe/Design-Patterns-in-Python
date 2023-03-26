from __future__ import annotations
from abc import ABC, abstractmethod

class Command(ABC):
    """
    Abstract Command class: declares an interface for executing an operation.
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class FirstCommand(Command):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f'    - first command: {self._payload}')


class ComplexCommand(Command):
    """
    Receivers: more complex operations.
    """
    def __init__(self, receiver:Receiver, a:str, b:str) -> None:
        """Accepts: multiple recievers & context data via the constructor"""
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        print(f'    - complex command starting...')
        self._receiver.operation_1(self._a)
        self._receiver.operation_2(self._b)


class Receiver:
    """
    Contains business logic, carry out requests by performing  operations.
    Any class may serve as a receiver.
    """
    def operation_1(self, a:str) -> None:
        print(f'        - operation 1: {a}')

    def operation_2(self, b:str) -> None:
        print(f'        - operation 2: {b}')


class Invoker:
    """
    Associated with a (or several) commands, the invoker sends a request to the command.
    """
    _launch_command: Command = None
    _land_command:   Command = None

    def set_launch_command(self, command: Command) -> None:
        self._launch_command = command
    
    def set_land_command(self, command: Command) -> None:
        self._land_command = command
    
    def launcher(self) -> None:
        """Invoker: request --> execute command --> receiver"""
        print(f'    - Invoker: launching...')
        if isinstance(self._launch_command, Command):
            self._launch_command.execute()
        print(f'    - Invoker: launched.')
        if isinstance(self._land_command, Command):
            self._land_command.execute()


if __name__ == '__main__':
    invoker  = Invoker()
    receiver = Receiver()
    invoker.set_launch_command(FirstCommand('launching...'))
    invoker.set_land_command(ComplexCommand(receiver, 'landing...', 'landed.'))
    invoker.launcher()
    print('....')
    print('equally')
    invoker  = Invoker()
    receiver = Receiver()
    FirstCommand('launching...').execute()
    ComplexCommand(receiver, 'landing...', 'landed.').execute()


