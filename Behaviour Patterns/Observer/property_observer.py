from typing import Any

class Event(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for item in self:
            item(*args, **kwds)


class PropertyObserver:
    def __init__(self) -> None:
        self.property_changed = Event()


class Person(PropertyObserver):
    def __init__(self, age=None):
        super().__init__()
        self._age = age
        self._job = 'Data Scientist'

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if self._age == value:
            return
        self._age = value
        self.property_changed('age', value)

    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, value):
        self._job = value

    def __str__(self) -> str:
        return f'Person ({self._age}) is a {self.job}'


class TrafficAuthority:
    def __init__(self, person) -> None:
        self.person = person
        person.property_changed.append(self.person_changed)
    
    def person_changed(self, name, value):
        if name == 'age':
            if value < 16:
                print('WARNING: too young to drive.')
            else:
                print('Drivable age :)')
                self.person.property_changed.remove(
                    self.person_changed
                    )
    
    def __str__(self) -> str:
        return f'Traffic Authority property_changed:{self.person.property_changed}'
                

if __name__ == '__main__':
    p = Person()
    print(p)
    p.age = 12
    print(p.property_changed)
    p.job = 'Software Eng'
    print(p)
    print(p.property_changed)

    t = TrafficAuthority(p)
    print(t)
    for age in range(14,20):
        print(f'Setting age to {age}')
        p.age = age
        print(t)