
# Open-Close ==========================================================================================
# OPEN  --> for Extension
# CLOSE --> for Modification
        
from enum import Enum

class colour(Enum):
    red     = 1
    green   = 2
    blue    = 3

class Size(Enum):
    small   = 1
    medium  = 2
    large   = 3

class Product:
    def __init__(self, name, colour, size) -> None:
        self.name   = name
        self.colour = colour
        self.size   = size

class ProductFilter:
    def filter_by_colour(self, products, colour):
        for p in products:
            if p.colour == colour:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p


# Approach 2 -----------------------------++
class Specification:
    # INTERFACE (base class)
    def is_satisfied(self, item):
        pass

class Filter:
    # INTERFACE (base class)
    def filter(self, items, spec):
        pass

class ColourSpecification(Specification):
    def __init__(self, colour) -> None:
        super().__init__()
        self.colour = colour
    
    def is_satisfied(self, item):
        return item.colour == self.colour

class SizeSpecification(Specification):
    def __init__(self, size) -> None:
        super().__init__()
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, *args) -> None:
        super().__init__()
        self.args = args
    
    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item
# Approach 2 -----------------------------++

# Instantiate ----------------------------++
def sp():
    print('.....'*10)

if __name__ == '__main__':
    apple   = Product('Apple', colour.green, Size.small)
    tree    = Product('Tree', colour.green, Size.large)
    house   = Product('house', colour.blue, Size.large)
    prods   = [apple, tree, house]
    pf      = ProductFilter()
    sp()
    print('Green products (old):')
    for p in pf.filter_by_colour(prods, colour.green):
        print('Product: {:<5} is green'.format(p.name))
    sp()
    print('Green products (new):')
    bf = BetterFilter()
    cs = ColourSpecification(colour.green)
    for p in bf.filter(items=prods, spec=cs):
        print('Product: {:<5} is green'.format(p.name))    
    sp()
    print('Large products (new):')
    bf = BetterFilter()
    ss = SizeSpecification(Size.large)
    for p in bf.filter(items=prods, spec=ss):
        print('Product: {:<5} is large'.format(p.name))    
    sp()
    print('Large blue items:')
    cs = ColourSpecification(colour.blue)
    ss = SizeSpecification(Size.large)
    ns = AndSpecification(cs,ss)
    for p in bf.filter(items=prods, spec=ns):
        print('Product {:<5} is large'.format(p.name))
# Open-Close ==========================================================================================
