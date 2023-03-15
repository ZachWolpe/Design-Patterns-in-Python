import copy

class SpyBalloon:
    def __init__(self, launch_date, altitude, sensors) -> None:
        self.launch_date        = launch_date
        self.altitude           = altitude
        self.sensors            = sensors
    
    def __str__(self) -> str:
        n=30
        return f'\n     Launch date:{self.launch_date:>{n-4}}\n     Altitude:{self.altitude:>{n-1}}\n     Sensors:{self.sensors:>{n}}\n'
    

class Nation:
    def __init__(self, name, military_budget, SpyBalloon) -> None:
        self.name               = name
        self.military_budget    = military_budget
        self.spyballoon         = SpyBalloon

    def __str__(self) -> str:
        return f'{self.name} has a military budget of ${self.military_budget}. It special ops team includes a spy balloon:\n {self.spyballoon}'


class NationFactory:
    default_nation = Nation('China', '229.6 Billion', SpyBalloon('2017','65\'000ft', 'infrared camera'))
    default_allie  = Nation('', '0', SpyBalloon('2022', "60'000ft", 'infrared camera & radar'))

    @staticmethod
    def __new_nation(proto, name, military_budget, **kwargs):
        nat                 = copy.deepcopy(proto)
        nat.name            = name
        nat.military_budget = military_budget
        for k,v in kwargs.items():
            print(nat.spyballoon.__dict__)
            nat.spyballoon.__dict__[k] = v
        return nat

    @staticmethod
    def new_nation(name, military_budget, **kwargs):
        return NationFactory.__new_nation(NationFactory.default_nation, name, military_budget, **kwargs)
        
    @staticmethod
    def new_allie(name, military_budget, **kwargs):
        return NationFactory.__new_nation(NationFactory.default_allie, name, military_budget, **kwargs)
        
    
china = NationFactory.new_nation('China', '229.6 Billion')
russia = NationFactory.new_allie('Russia', '84 Billion', launch_date='2021', altitude="78'000ft")
print(china)
print(russia)