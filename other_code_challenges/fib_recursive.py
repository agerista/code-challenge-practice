def fibonacci_recursive(n):
    """add numbers in a fibonacci sequence recursively.

    0 + 1 + 1 + 2 + 3 + 5 + 8 + 13

    fibonacci_recursive(0) = 0
    fibonacci_recursive(1) = 1
    fibonacci_recursive(2) = (0+1) = 1
    fibonacci_recursive(3) = (1+1) = 2

    >>> fibonacci_recursive(4)
    3

    >>> fibonacci_recursive(5)
    5

    >>> fibonacci_recursive(6)
    8
    """

    if n == 0 or n == 1:
        return n

    else:
        # print 1 + fibonacci_recursive(n - 1)
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
