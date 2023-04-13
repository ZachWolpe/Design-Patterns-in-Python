from abc import ABC

class Switch:
    def __init__(self):
        self.state = OffState()

    def on(self):
        self.state.on(self)
        return self
    
    def off(self):
        self.state.off(self)
        return self


class State(ABC):
    def on(self, switch):
        print('light is already on.')
    
    def off(self, switch):
        print('light is already off.')
    

class OnState(State):
    def __init__(self):
        print('light turned on.')
    
    def off(self, switch):
        print('turning light off...')
        switch.state = OffState()

class OffState(State):
    def __init__(self):
        print('light turned off.')
    
    def on(self, switch):
        print('turning light on...')
        switch.state = OnState()

    
if __name__ == '__main__':
    sw = Switch()
    sw \
        .on() \
        .off() \
        .off()
     