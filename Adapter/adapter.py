# ========================================================================##
# file: adapter.py
#
# Implement the adapter design pattern.
#
# ------------------------------------------------------------------------++
# author:       zach wolpe
# email:        zach.wolpe@medibio.com.au
# date:         13 Mar 2023
# ========================================================================##


class Point:
    def __init__(self,x,y) -> None:
        self.x  = x
        self.y  = y


class Line:
    def __init__(self, start, end) -> None:
        self.end    = end
        self.start  = start

class Rectangle(list):
    """Represented as a list of lines."""

    def __init__(self,x,y,width,height):
        super().__init__()
        self.append(Line(Point(x,       y),         Point(x+width,  y)))
        self.append(Line(Point(x+width, y),         Point(x+width,  y+height)))
        self.append(Line(Point(x,       y),         Point(x,        y+height)))
        self.append(Line(Point(x,       y+height),  Point(x+width,  y+height)))


class RectangleToPointsAdapter(list):
    """Receive a rectangle -> change it into a string of points."""


    def __init__(self, rec):
        
        # get dimensions
        x = 999999999
        x0=x; x1=-x; y0=x; y1=-x
        for r in rec:
            a,b,c,d = r.start.x, r.end.x, r.start.y, r.end.y
            x0 = min(a,b,x0)
            x1 = max(a,b,x1)
            y0 = min(c,d,y0)
            y1 = max(c,d,y1)



        # draw
        points  = ''
        for _ in range(round((y1-y0)/2)):
            points += '\n'
        for _ in range(round(y1-y0)):
            points += self.draw_points(x0, null=True) + self.draw_points(x1) + '\n'
        for _ in range(round((y1-y0)/2)):
            points += '\n'
        print(points)


    def draw_points(self,n,null=False):
        if null:
            return ' '*n
        return '.'*n
    


if __name__ == '__main__':
    a,b,c,d=12,3,71,4
    assert a>0; assert b>0; assert c>a; assert d>b
    rec = Rectangle(a,b,c,d)
    ra = RectangleToPointsAdapter(rec=rec)


