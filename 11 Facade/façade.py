from __future__ import annotations

class Facade:
    def __init__(self, subsystem1:system2, subsystem2:system2):
        self._subsystem1 = subsystem1 or system1()
        self._subsystem2 = subsystem2 or system2()

    def ops(self) -> str:
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.ops1())
        results.append(self._subsystem2.ops1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.ops_n())
        results.append(self._subsystem2.ops_z())
        return "\n".join(results)


class system1:
    def ops1(self) -> str:
        return "system1: ready!"

    def ops_n(self) -> str:
        return "system1: go!"
    
class system2:
    def ops1(self) -> str:
        return "system2: get ready!"

    def ops_z(self) -> str:
        return "system2: fire!"


def client_interface(facade:Facade) -> None:
    print(facade.ops(), end="")



if __name__ == "__main__":
    subsystem1  = system1()
    subsystem2  = system2()
    facade      = Facade(subsystem1, subsystem2)
    client_interface(facade)