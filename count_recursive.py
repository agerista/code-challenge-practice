def count_recursively(lst):
    """count items in a list recursively

    practice problem at Earnest

    >>> count_recursively([1,2,3])
    3
    """

    if lst == []:
        return 0

    return 1 + count_recursively(lst[1:])

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
