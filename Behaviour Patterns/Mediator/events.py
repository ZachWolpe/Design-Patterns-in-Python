
class Event(list):
    """ Events: List[callable functions] """
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:
    """
    Mediator
    
    Game events: list[functions] stores all callable functions.
    """
    def __init__(self):
        self.events = Event()

    def fire(self, args):
        self.events(args)
    

class GoalScoredInfo:
    def __init__(self, scorer, goals_scored) -> None:
        self.goals_scored   = goals_scored
        self.scorer         = scorer
    

class Player:
    def __init__(self, name, game):
        self.name           = name
        self.game           = game
        self.goals_scored   = 0
    
    def score(self):
        self.goals_scored += 1
        args = GoalScoredInfo(self.name, self.goals_scored)
        # game (the mediator) is triggered by player
        self.game.fire(args)
        return self
    

class Manager:
    def __init__(self, game):
        # add function the the Game's events: list[functions]
        game.events.append(self.celebrate_goal)
    
    def celebrate_goal(self, args):
        if isinstance(args, GoalScoredInfo) and args.goals_scored < 3:
            print(f'Coach: Bravo {args.scorer}! Goal {args.goals_scored}!')
    

if __name__ == '__main__':
    game    = Game()
    player  = Player('Messi', game)
    manager = Manager(game)

    player\
        .score()\
        .score()\
        .score()
