def bubble_sort(num, array):
    """sorts a given list from smallest to largest

    >>> bubble_sort(3, [1, 2, 3])
    Array is sorted in 0 swaps.
    First Element: 1
    Last Element: 3
    """

    count = 0
    i = 0

    while i in range(len(array) - 1):

        sorts = 0

        if array[i] > array[i + 1]:
            array[i + 1], array[i] = array[i], array[i + 1]
            count += 1
            sorts += 1
            i += 1

        if sorts == 0:
            break

    print "Array is sorted in %s swaps." % count
    print "First Element: %s" % array[0]
    print "Last Element: %s" % array[-1]

################################################################################
if __name__ == '__main__':
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
