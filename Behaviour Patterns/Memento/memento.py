
class Memento:
    def __init__(self, ops:int):
        self.ops = ops
    
    def __str__(self) -> str:
        return f'ops: {self.ops}'


class FlightLog:
    def __init__(self, op:int=0):
        self.ops        = op
        self.changes    = [Memento(self.ops)]
        self.current    = 0
    
    def new_mission(self, ops:int):
        self.ops += ops
        m = Memento(self.ops)
        self.changes.append(m)
        self.current += 1
        return m
    
    def restore(self, momento):
        if momento:
            self.ops     = momento.ops
            self.current = len(self.changes)-1
            self.changes.append(momento)
        
    def undo(self):
        if self.current > 0:
            # do not edit self.changes to allow for a full historical log.
            self.current -= 1
            m = self.changes[self.current]
            self.ops = m.ops
            return m
        return None

    def redo(self):
        if self.current+1 < len(self.changes):
            self.current += 1
            m = self.changes[self.current]
            self.ops = m.ops
            return m
        return None

    def __str__(self) -> str:
        return f'Operations: Ops={self.ops}'


if __name__ == '__main__':
    fl = FlightLog(774)
    fl.new_mission(32)
    fl.new_mission(91)
    print(fl)
    fl.undo()
    print(f'undo 1: {fl}')
    fl.undo()
    print(f'undo 2: {fl}')
    fl.redo()
    print(f'redo 1: {fl}')
    print('..')
    [print(m) for m in fl.changes]


    

