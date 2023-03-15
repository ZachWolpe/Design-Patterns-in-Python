from abc import ABC

class Shape(ABC):
    def __str__(self):
        return ''
    

class Circle(Shape):
    def __init__(self, radius=0.0):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor
    
    def __str__(self):
        return f'A circle of radius {self.radius}'
    

class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side

    def __str__(self):
        return f'A square with side {self.side}'
    

class ColouredShape(Shape):
    def __init__(self, shape, colour):
        if isinstance(shape, ColouredShape):
            raise Exception('Cannot apply ColouredDecorator twice')
        self.shape  = shape
        self.colour = colour

    def __str__(self):
        return f'{self.shape} has the colour {self.colour}'
    

class TransparentShape(Shape):
    def __init__(self, shape, transparency):
        self.shape          = shape
        self.transparency   = transparency

    def __str__(self):
        return f'{self.shape} has {self.transparency * 100.0}% transparency'
    


if __name__ == '__main__':
    circle = Circle(2)
    print(circle)

    red_circle = ColouredShape(circle, 'red')
    print(red_circle)

    # ColouredShape doesn't have resize()
    # red_circle.resize(3)

    red_half_transparent_square = TransparentShape(red_circle, 0.5)
    print(red_half_transparent_square)

    # nothing prevents double application
    # mixed = ColouredShape(ColouredShape(Circle(3), 'red'), 'blue')
    # print(mixed)
