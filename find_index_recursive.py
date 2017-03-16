def find_index(lst, item, index=0):
    """find index of an item in a list using recursion

    >>> find_index([1,2,3,4,5], 2)
    1

    """

    if len(lst) > 0:

        if lst[index] == item:

            return index

        return find_index(lst, item, index + 1)

################################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print