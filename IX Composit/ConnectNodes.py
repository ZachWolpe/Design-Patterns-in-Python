from abc import ABC
from collections.abc import Iterable


class LinkNodes(Iterable, ABC):
    def connect_to(self, other):
        if self == other:
            return

        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Nodes(LinkNodes):
    def __init__(self, name):
        self.name    = name
        self.inputs  = []
        self.outputs = []

    def __iter__(self):
        yield self

    def __str__(self):
        return f'{self.name}, {len(self.inputs)} inputs, {len(self.outputs)} outputs'
    

class NodeLayer(list, LinkNodes):
    def __init__(self, name, n_nodes):
        super().__init__()
        self.name = name
        for i in range(0, n_nodes):
            self.append(Nodes(f'{name}-{i}'))
    
    def __str__(self):
        ln =  '\n---------------------------------------'
        ln += '\n---------------------------------------'
        ln += f'\n{self.name} with {len(self)} nodes'
        for node in self:
            ln += '\n' + node.__str__()
        ln += '\n---------------------------------------'
        ln += '\n---------------------------------------'
        return ln
    


if __name__ == '__main__':
    layer1  = NodeLayer('Layer1', 1)
    layer2  = NodeLayer('Layer2', 2)
    for l in layer1:
        for l2 in layer2:
            l.connect_to(l2)

    print(layer1)
    print(layer2)

