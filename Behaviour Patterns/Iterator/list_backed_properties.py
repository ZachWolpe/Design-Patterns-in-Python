class Pokemon:
    """Niave implementation of a Pokemon class"""
    def __init__(self):
        self.strength       = 10
        self.agility        = 10
        self.intelligence   = 10

    @property
    def sum_of_stats(self):
        return self.strength + self.agility + self.intelligence
    
    @property
    def max_stat(self):
        return max(self.strength, self.agility, self.intelligence)
    
    @property
    def mean_stat(self):
        return self.sum_of_stats / 3
    

class PokemonBetter:
    """
    Known as: LISTED BACKED PROPERTIES (LBP) or ARRAY BACKED PROPERTIES (ABP)
    Increased stability & flexibility.
    Minimize the likelihood of a bug by using properties, as well as removing magic numbers
    """
    _strength       = 0
    _agility        = 1
    _intelligence   = 2
    def __init__(self):
        self.stats = [10,10,10]

    @property
    def strength(self):
        return self.stats[PokemonBetter._strength]
    
    @strength.setter
    def strength(self, value):
        self.stats[PokemonBetter._strength] = value
    
    @property
    def agility(self):
        return self.stats[PokemonBetter._agility]
    
    @agility.setter
    def agility(self, value):
        self.stats[PokemonBetter._agility] = value

    @property
    def intelligence(self):
        return self.stats[PokemonBetter._intelligence]
    
    @intelligence.setter
    def intelligence(self, value):
        self.stats[PokemonBetter._intelligence] = value

    @property
    def sum_of_stats(self):
        return sum(self.stats)
    
    @property
    def max_stat(self):
        return max(self.stats)
    
    @property
    def mean_stat(self):
        return self.sum_of_stats / len(self.stats)