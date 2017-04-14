def absolute_sort(arr):
    """Consider an unsorted array, arr = a0, a1, a2, an-1, of distinct integers
    from 0 to n-1. We can swap two adjacent elements in arr any number of times
    as long as the absolute difference between these elements is 1.

    >>> absolute_sort([1, 0, 3, 2])
    Yes

    >>> absolute_sort([2, 1, 0])
    No
    """

    i = 1
    a_sort = True

    while i < len(arr):

        result = abs(arr[i]) - abs(arr[i - 1])

        if arr[i - 1] > arr[i]:

            arr[i - 1], arr[i] = arr[i], arr[i - 1]
        i += 1

    for num in arr:

        if abs(result) != 1:
            a_sort = False

    if a_sort == True:
        print "Yes"
    else:
        print "No"

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
