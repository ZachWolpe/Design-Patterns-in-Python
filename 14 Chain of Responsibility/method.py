class Pokemon:
    def __init__(self, name, attack, defense):
        self.defense = defense
        self.attack  = attack
        self.name    = name
    
    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'

class PokemonModifier:
    def __init__(self, pokemon):
        self.pokemon        = pokemon
        self.next_modifier  = None
    
    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier
    
    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class NoBonusesModifier(PokemonModifier):
    def handle(self):
        print('No bonuses for you!')
    

class DoubleAttackModifier(PokemonModifier):
    def handle(self):
        print(f'Doubling {self.pokemon.name}''s attack')
        self.pokemon.attack *= 2
        super().handle()

class IncreaseDefenceModifier(PokemonModifier):
    def handle(self):
        if self.pokemon.attack <= 2:
            print(f'Increasing {self.pokemon.name}''s defence')
            self.pokemon.defense += 1
        super().handle()

if __name__ == '__main__':
    pikachu = Pokemon('Pikachu', 1, 1)
    print(pikachu)
    root = PokemonModifier(pikachu)
    # root.add_modifier(NoBonusesModifier(pikachu))
    root.add_modifier(DoubleAttackModifier(pikachu))
    root.add_modifier(IncreaseDefenceModifier(pikachu))
    root.handle()
    print(pikachu)