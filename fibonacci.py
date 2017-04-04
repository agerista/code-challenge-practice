def fibonacci(n):
    """add numbers in a fibonacci sequence

    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(2) = (0+1) = 1
    fibonacci(3) = (1+1) = 2
    fibonacci(4) = (1+2) = 3
    fibonacci(5) = (2+3) = 5
    fibonacci(6) = (3+5) = 8
    """

    x = 0
    y = 1
    fib = 0

    while fib <= n:

        fib = x + y
        x = y
        y = fib

    return fib

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
