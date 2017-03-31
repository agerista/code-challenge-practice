def fizzbuzz():
    """Count from 1 to 20 in fizzbuzz fashion.

    >>> fizzbuzz()
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    17
    fizz
    19
    buzz
    """

    i = 1

    while i < 21:

        if i % 3 == 0 and i % 5 == 0:
            print "fizzbuzz"

        elif i % 3 == 0:
            print "fizz"

        elif i % 5 == 0:
            print "buzz"

        else:
            print i
        i += 1

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

