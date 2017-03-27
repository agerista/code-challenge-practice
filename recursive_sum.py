def recursive_sum(lst):
    """Sum the numbers in a list recursively

    >>> recursive_sum([5, 5])
    10

    >>> recursive_sum([-5, 10, 4])
    9

    >>> recursive_sum([20])
    20

    >>> recursive_sum([])
    0
    """

    if lst == []:
        return 0

    else:

        return lst[0] + recursive_sum(lst[1:])

################################################################################
if __name__ == '__main__':
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print