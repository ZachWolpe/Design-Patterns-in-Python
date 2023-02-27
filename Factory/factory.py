from enum import Enum
from math import *

class Point:
    def __init__(self, x, y):
            self.x = x
            self.y = y
            
    def __str__(self) -> str:
        return f'x:{self.x}, y:{self.y}'

    class Factory:
        def new_cartesian_point(self,x,y):
            return Point(x,y)

        def new_polar_point(self,rho,theta):
            rho=rho
            return Point(rho * sin(theta), rho * cos(theta))

    factory = Factory()

if __name__ == '__main__':
    for i in [1,2,3]:
        p1 = Point.factory.new_cartesian_point(1, 2)
        p2 = Point.factory.new_polar_point(1, 2)
        print(p1)
        print(p2)
        print('....')