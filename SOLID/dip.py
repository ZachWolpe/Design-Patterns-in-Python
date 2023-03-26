
# Dependency Inversion Principle ======================================================================
from abc import abstractmethod
from enum import Enum

class Relationship(Enum):
    PARENT  = 0
    CHILD   = 1
    SIBLING = 2

class Person:
    def __init__(self, name) -> None:
        self.name = name

class RelationshipBrowser:
    @abstractmethod
    def find_all_child_of(self, name):
        pass

# Low-level module (storage)
class Relationships(RelationshipBrowser):
    def __init__(self) -> None:
        self.relations = []
    
    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child,  Relationship.CHILD,  parent))

    def find_all_child_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


# High-level module
class Research:
    # poor solution: relies on relationships data structure.
    # def __init__(self, relationships) -> None:
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}')

    # No longer has a dependence on the internal mechanics of how a relationship is stored!
    def __init__(self, browser) -> None:
        for p in browser.find_all_child_of('John'):
            print(f'John has a child called {p}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')


relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)
Research(relationships)
# Dependency Inversion Principle ======================================================================