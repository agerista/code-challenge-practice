def find_biggest(lst, target):
    """Returns the index of the biggest number which is smaller than the target

    >>> find_biggest([1,2,3,4,5], 4)
    2

    >>> find_biggest([3,4,5], 2)
    None

    """

    i = 0

    while i < len(lst):

        if lst[i] < target:
            i += 1

        elif lst[i] >= target:
            return i - 1

    return None

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
