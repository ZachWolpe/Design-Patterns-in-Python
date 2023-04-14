from abc import ABC

class Expression(ABC):
    pass

class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value

class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.right  = right
        self.left   = left

class ExpressionPrinter:

    @staticmethod
    def print(e, buffer):
        if isinstance(e, DoubleExpression):
            buffer.append(str(e.value))
        elif isinstance(e, AdditionExpression):
            buffer.append('(')
            ExpressionPrinter.print(e.left, buffer)
            buffer.append('+')
            ExpressionPrinter.print(e.right, buffer)
            buffer.append(')')
    
    # backpropergate the method to the base class
    Expression.print = lambda self, b: ExpressionPrinter.print(self, b)
    

# VIOLATES OCP: new types require MxN modifications.

if __name__ == '__main__':
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    buffer = []

    e.print(buffer)
    print(''.join(buffer))
