class Events(list):
    def __call__(self, *args, **kwargs):
        for items in self:
            items(*args, **kwargs)


class Person:
    def __init__(self, name, address):
        self.name       = name
        self.address    = address
        self.falls_ill  = Events()
    
    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)


def call_doctor(name, address):
    print(f'A doctor has been called to {address}')


if __name__ == '__main__':
    p = Person('Nemo', 'P. Sherman 42 Wallaby Way')
    p.falls_ill.append(lambda name, addr: print(f'{name} is ill'))
    p.falls_ill.append(call_doctor)
    p.catch_a_cold()

    # remote subscription
    p.falls_ill.remove(call_doctor)
    p.catch_a_cold()
