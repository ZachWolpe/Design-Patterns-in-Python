from abc import ABC, abstractmethod

class Server(ABC):
    """
    Common interface for both:
        - RealServer
        - Proxy
    """
    @abstractmethod
    def request(self) -> None:
        pass


class RealServer(Server):
    def request(self) -> None:
        print("RealServer: Handling request.")


class Proxy(Server):
    def __init__(self, real_server: RealServer) -> None:
        self._real_server = real_server

    def request(self) -> None:
        if self.check_access():
            self._real_server.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True
    
    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")


def client_code(server: Server) -> None:
    server.request()

if __name__ == "__main__":
    print('...'*20, 'Launch real server', '...'*20)
    print("Client: Executing the client code with a real server:")
    real_server = RealServer()
    client_code(real_server)
    
    print("")
    print('...'*20, 'Launch proxy', '...'*20)
    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_server)
    client_code(proxy)