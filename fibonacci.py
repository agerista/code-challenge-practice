def fibonacci(n):
    """add numbers in a fibonacci sequence

    >>> fibonacci(0)
    'The fibonacci of 0 is 0'

    >>> fibonacci(1)
    'The fibonacci of 1 is 0'

    >>> fibonacci(2)
    'The fibonacci of 2 is 1'

    >>> fibonacci(3)
    'The fibonacci of 3 is 2'

    fibonacci(4) = (1+2) = 3
    fibonacci(5) = (2+3) = 5
    fibonacci(6) = (3+5) = 8
    """

    x = 0
    y = 1
    fib = 0
    i = 2

    while i <= n:

        if n == 0:
            fib = 0

        elif n == 1:
            fib = 1

        else:

            fib = x + y
            x = y
            y = fib

        i += 1

    return "The fibonacci of {} is {}".format(n, fib)


def fibonacci_recursive(n1=0, n2=1):
    """add numbers in a fibonacci sequence recursively

    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(2) = (0+1) = 1
    fibonacci(3) = (1+1) = 2

    >>> fibonacci(4)
    3

    >>> fibonacci(5)
    5

    >>> fibonacci(6)
    8
    """

    if n == 0:
        return 0

    else:
        
        return 3


################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
