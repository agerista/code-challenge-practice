class Calculator(object):
    """Build a calculator using only static and class methods.
    Note that an instance of the calculator is never created.


    One final addition. The subtract method must be implemented
    using the add method. Something like this:

    subtract = add(x, y * -1)
    """

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return Calculator.add(x, -y)

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        return x / float(y)


def test_subtract():
    assert Calculator.subtract(5, 2) == 3


def test_divide():
    assert Calculator.divide(9, 3) == 3.0


def test_multiply():
    assert Calculator.multiply(7, 9) == 63


def test_add():
    assert Calculator.add(5, 2) == 7


def test_divide_decimal():
    assert Calculator.divide(9, 2) == 4.5

print test_subtract()
print test_divide()
print test_multiply()
print test_add()
print test_divide_decimal()

def test_subtract():
    assert Calculator.subtract(5, 2) == 3

def test_divide():
    assert Calculator.divide(9, 3) == 3.0

def test_multiply():
    assert Calculator.multiply(7, 9) == 63

def test_add():
    assert Calculator.add(5, 2) == 7

def test_divide_decimal():
    assert Calculator.divide(9, 2) == 4.5


