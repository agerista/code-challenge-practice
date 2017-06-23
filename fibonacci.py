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

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
