def deduped(items):
    """Return new list from items with duplicates removed.

    >>> deduped([1, 1, 1])
    [1]

    >>> deduped([1, 2, 1, 1, 3])
    [1, 2, 3]

    >>> deduped([1, 2, 3])
    [1, 2, 3]
    """

    result = []
    temp = set()

    if items == []:
        return result

    for item in items:

        if item not in temp:
            result.append(item)
            temp.add(item)

    return result

##################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD WORK!\n"
