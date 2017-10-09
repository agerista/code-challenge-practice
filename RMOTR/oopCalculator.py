class Calculator(object):
    """Provides basic calculator functions"""

    def add(self, x, y):
        """Adds two numbers together"""

        return x + y

    def subtract(self, x, y):
        """Subtracts two numbers"""

        return x - y

    def multiply(self, x, y):
        """Multiplies two numbers"""

        return x * y

    def divide(self, x, y):
        """Divides two numbers"""

        return x / float(y)

calculator = Calculator()

calculator.add(2, 4)  # 6
calculator.subtract(8, 1)  # 7
calculator.multiply(3, 5)  # 15
calculator.divide(5, 2)  # 2.5


def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 2) == 3


def test_divide():
    calc = Calculator()
    assert calc.divide(9, 3) == 3.0


def test_multiply():
    calc = Calculator()
    assert calc.multiply(7, 9) == 63


def test_add():
    calc = Calculator()
    assert calc.add(5, 2) == 7


def test_divide_decimal():
    calc = Calculator()
    assert calc.divide(9, 2) == 4.5


print test_subtract()
print test_divide()
print test_multiply()
print test_add()
print test_divide_decimal()
