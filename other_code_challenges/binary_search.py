def binary_search(lst, item):
    """binary search

    >>> binary_search([1,2,3], 2)
    1

    >>> binary_search([], 1)
    None

    >>> binary_search([1], 1)
    0

    """

    high = len(lst)
    low = 0
    mid = (low + high) / 2

    if lst == []:
        print "None"

    while low < high:

        if lst[mid] == item:
            return mid

        elif lst[mid] > item:
            high = mid

        else:
            low = mid + 1

        mid = (low + high) / 2

    return None

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
