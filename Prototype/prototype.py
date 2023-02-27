import copy

class SpyBalloon:
    def __init__(self, launch_date, altitude, sensors) -> None:
        self.launch_date        = launch_date
        self.altitude           = altitude
        self.sensors            = sensors
        # ['infrared camera','radar','lidar','rasberryPi']
    
    def __str__(self) -> str:
        n=30
        return f'\n     Launch date:{self.launch_date:>{n-4}}\n     Altitude:{self.altitude:>{n-1}}\n     Sensors:{self.sensors:>{n}}\n'
    
class Nation:
    def __init__(self, name, military_budget, SpyBalloon) -> None:
        self.name               = name
        self.military_budget    = military_budget
        self.spyballon          = SpyBalloon

    def __str__(self) -> str:
        return f'{self.name} has a military budget of ${self.military_budget}. It special ops team includes a spy balloon:\n {self.spyballon}'
    


china = Nation('China', '229.6 Billion', SpyBalloon('2017','65\'000ft', 'infrared camera'))

# copy ------------++
def create_deepcopy(nation_prototype, name, military_budget, launch_date, altitude):
    nat                         = copy.deepcopy(nation_prototype)
    nat.name                    = name
    nat.military_budget         = military_budget
    nat.spyballon.launch_date   = launch_date
    nat.spyballon.altitude      = altitude
    return nat
# copy ------------++


usa = create_deepcopy(china,'USA', '800.67 Billion', '2021','73\'000ft')
print(china)
print(usa)