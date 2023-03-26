from typing import Dict
import json

class Flyweight():
    """store shared (intrinsic) state"""
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state
    
    def method(self, unique_state: str) -> None:
        s = self._shared_state
        u = unique_state
        print(f'Flyweight: Displaying shared ({s}) and unique ({u}) state.', end='')



class FlyweightFactory():
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweight: Dict) -> None:
        for state in initial_flyweight:
            self._flyweights[self._get_keys(state)] = Flyweight(state)
    
    def _get_keys(self, state: Dict) -> str:
        return '_'.join(sorted(state))
    
    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        key = self._get_keys(shared_state)
        if not self._flyweights.get(key):
            print('FlyweightFactory: Can\'t find a flyweight, creating new one.')
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print('FlyweightFactory: Reusing existing flyweight.')
        return self._flyweights[key]
    

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f'flyweightFactory: I have {count} flyweights:\n')
        print('\n'.join(map(str, self._flyweights.keys())))


def add_car_to_police_database(
        factory:   FlyweightFactory,
        plates:    str,
        owner:     str,
        brand:     str,
        model:     str,
        color:     str) -> None:
    print('\nClient: Adding a car to database.')
    flyweight = factory.get_flyweight([brand, model, color])
    print(flyweight)
    flyweight.method([plates, owner])



if __name__ == "__main__":


    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["Mercedes Benz", "C500", "red"], # intentional redundancy
        ["Mercedes Benz", "C500", "red"], # intentional redundancy
        ["Mercedes Benz", "C500", "red"], # intentional redundancy
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweights()

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "red")

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    print("\n")

    factory.list_flyweights()