
# Liskov Substitution Principle =======================================================================
# Rule: objects of a superclass should be replaceable with objects of its subclasses without breaking the application. In other words, what we want is to have the objects of our subclasses behaving the same way as the objects of our superclass.

class Rectangle:
    def __init__(self, width, height) -> None:
        self._width  = width
        self._height = height
    
    @property
    def area(self):
        return self._width * self._height
    
    def __str__(self) -> str:
        return f'width:{self._width}, height:{self._height}'

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size) -> None:
        super().__init__(size, size)
    
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value
    
    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value

def fetch_area(rec, h=10):
    w = rec.width
    rec.height  = h
    expc = int(w*h)
    print(f'\nExpected area: {expc:>{3}}, Received area: {rec.area}')

print()
rc = Rectangle(12,43)
fetch_area(rc)

sq = Square(5)
fetch_area(sq)
print()
# Liskov Substitution Principle =======================================================================