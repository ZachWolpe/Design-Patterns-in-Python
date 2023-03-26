# Required Elements:
#   1. event broker
#   2. command-query separation (cqs)
#   3. observer
from enum import Enum
from abc  import ABC


class Event(list):
    """List of callable functions."""
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

class WhatToQuery(Enum):
    ATTACK  = 1
    DEFENSE = 2


class Query:
    def __init__(self, pokemon_name, what_to_query, default_value):
        self.value          = default_value  # value after modification.
        self.what_to_query  = what_to_query
        self.pokemon_name   = pokemon_name


class Game:
    # event broker
    def __init__(self):
        self.queries = Event()
    
    def perform_query(self, sender, query):
        self.queries(sender, query)
    

class Pokemon:
    def __init__(self, game, name, attack, defense):
        self.initial_defense = defense
        self.initial_attack  = attack
        self.name            = name
        self.game            = game
    
    @property
    def attack(self):
        q = Query(
            pokemon_name    = self.name,
            what_to_query   = WhatToQuery.ATTACK,
            default_value   = self.initial_attack)
        self.game.perform_query(self, q)
        return q.value
    
    @property
    def defense(self):
        q = Query(
            pokemon_name    = self.name,
            what_to_query   = WhatToQuery.DEFENSE,
            default_value   = self.initial_attack)
        self.game.perform_query(self, q)
        return q.value
    
    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'


class PokemonModifier(ABC):
    def __init__(self, game, pokemon):
        self.pokemon    = pokemon
        self.game       = game
        self.game.queries.append(self.handle)

    def handle(self, sender, query):
        pass

    # allow `with()` implementation. --->
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.queries.remove(self.handle)
    # allow `with()` implementation. --->
    

class DoubleAttackModifier(PokemonModifier):
    def handle(self, sender, query):
        if (sender.name == self.pokemon.name and
            query.what_to_query == WhatToQuery.ATTACK):
            query.value *= 2
        

class IncreaseDefenseModifier(PokemonModifier):
    def handle(self, sender, query):
        if (sender.name == self.pokemon.name and
            query.what_to_query == WhatToQuery.DEFENSE):
            query.value += 3
        

if __name__ == '__main__':
    game    = Game()
    pikachu = Pokemon(game, 'Pikachu', 5, 5)
    print(pikachu)

    with DoubleAttackModifier(game, pikachu):
        print(pikachu)
        with IncreaseDefenseModifier(game, pikachu):
            print(pikachu)
    
    print(pikachu)