


class Monostate:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj
    
class Person(Monostate):
    def __init__(self) -> None:
        self.name   = 'Zach'
        self.age    = 27
    
    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old.'


if __name__=='__main__':
    print()
    p1 = Person()
    print(p1)
    p2 = Person()
    p1.name = 'Chase'
    print(p1,p2)
    print()