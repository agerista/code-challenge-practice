def array_left_rotation(n, k, a):
    """Given an array of n integers and a number, d, perform d left rotations on
    the array. Then print the updated array as a single line of space-separated
    integers.

    >>> array_left_rotation(5, 4, [1, 2, 3, 4, 5])
    5 1 2 3 4
    """

    while k > 0:

        rotation = a.pop(0)
        a.append(rotation)
        k -= 1

    print a

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
