def add(num1, num2):
    """Return the sum of the two input integers."""

    return num1 + num2


def subtract(num1, num2):
    """Return the second number subtracted from the first."""

    return num2 - num1


def multiply(num1, num2):
    """Multiply the two inputs together."""

    return num1 * num2


def divide(num1, num2):
    """Divide the first input by the second, returning a floating point."""

    return float(num2) / num1


def square(num1):
    """Return the square of the input."""

    return num1 ** 2


def cube(num1):
    """Return the cube of the input."""

    return num1 ** 3


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""

    return num1 ** num2


def mod(num1, num2):
    """Return the remainder of num1 / num2."""

    return num1 % num2


def addMult(num1, num2, num3):
    """takes three numbers, adds the first two, then multiplies the sum with the third."""

    return (num1 + num2) * num3


def cubeSum(num1, num2):
    """takes two numbers, and adds together the cubes of those numbers"""

    return (num1 ** 3) + (num2 ** 3)
