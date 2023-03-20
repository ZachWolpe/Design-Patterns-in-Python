from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional, Dict, List

# Interface ----------------------------------------------------++
class Handler(ABC):
    """
    Interface for:
        - Building a chain of handlers.
        - Executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass
# Interface ----------------------------------------------------++


# Base class ---------------------------------------------------++
class AbstractHandler(Handler):
    """
    Base hanlder class implements the default chaining behaviour.
    """
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler # allow chaining
    
    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None
# Base class ---------------------------------------------------++
    

# Concrete handlers --------------------------------------------++
class AccessHandler_01(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "password_01":
            return f"AccessHandler_01: I'll grant access to {request}"
        else:
            return super().handle(request)

class AccessHandler_02(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "password_02":
            return f"AccessHandler_02: I''ll grant access to {request}"
        else:
            return super().handle(request)

class AccessHandler_03(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "password_03":
            return f"AccessHandler_03: I''ll grant access to {request}"
        else:
            return super().handle(request)
# Concrete handlers --------------------------------------------++


# Client -------------------------------------------------------++
def client_code(handler: Handler) -> None:
    """
    The client code is usually not aware of the handler chain, & designed to work with a single handler.
    """

    for password in ["password_01", "password_02", "password_03"]:
        print(f"\nClient: {password}")
        result = handler.handle(password)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {password} was left untouched.", end="")
# Client -------------------------------------------------------++



if __name__ == '__main__':
    access_01 = AccessHandler_01()
    access_02 = AccessHandler_02()
    access_03 = AccessHandler_03()

    access_01.set_next(access_02).set_next(access_03)
    
    # The client should be able to send a request to ANY handler, not only the first one in the chain.
    print('Chain:   AccessHandler_01 > AccessHandler_02 > AccessHandler_03')
    client_code(access_01)
    print('\n')
    print('Subchain: AccessHandler_02 > AccessHandler_03')
    client_code(access_02)
