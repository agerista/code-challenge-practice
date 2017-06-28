def bubble_sort(n, lst):
    """sorts a given list from smallest to largest

    >>> bubble_sort(3, [1, 2, 3])
    Array is sorted in 0 swaps.
    First Element: 1
    Last Element: 3

    >>> bubble_sort(3, [3, 2, 1])
    Array is sorted in 3 swaps.
    First Element: 1
    Last Element: 3
    """

    sorts = 0

    if len(lst) < 2:
        return sorts

    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):

            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
                sorts += 1

    print "Array is sorted in %s swaps." % sorts
    print "First Element: %s" % lst[0]
    print "Last Element: %s" % lst[-1]

################################################################################
if __name__ == '__main__':
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
