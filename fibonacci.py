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
    i = 2

    while i <= n:

        if n == 0:
            return 0

        elif n == 1:
            return 1

        else:

            fib = x + y
            x = y
            y = fib

        i += 1


    return fib

# def fibonacci_recursive(n1=0, n2=1):
#     """add numbers in a fibonacci sequence recursively

#     fibonacci(0) = 0
#     fibonacci(1) = 1
#     fibonacci(2) = (0+1) = 1
#     fibonacci(3) = (1+1) = 2
#     fibonacci(4) = (1+2) = 3
#     fibonacci(5) = (2+3) = 5
#     fibonacci(6) = (3+5) = 8
#     """

#     if n == 0:
#         return 0

#     return fib = fibonacci_recursive(n1, n2)

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
