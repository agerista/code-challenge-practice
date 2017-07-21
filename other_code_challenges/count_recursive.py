def count_recursively(lst):
    """count items in a list recursively

    practice problem at Earnest

    >>> count_recursively([1,2,3])
    3
    """

    if lst == []:
        return 0

    return 1 + count_recursively(lst[1:])


def count_recursively2(lst, count=0):
    """Return number of items in a list, using recursion.

    >>> count_recursively2([])
    0

    >>> count_recursively2([1, 2, 3])
    3
    """

    if lst == []:
        return count

    return count_recursively2(lst[1:], count + 1)

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
