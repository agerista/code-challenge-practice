def second_largest(arr):
    """Find the second largest number in an array.

    >>> second_largest([2, 3, 6, 6, 5])
    5

    >>> second_largest([1, 2, 3])
    2

    >>> second_largest([6, 5, 4])
    5
    """

    largest = second = -100

    for num in arr:
        if num > largest:
            tmp = largest
            largest = num
            second = tmp
        elif num > second and num != largest:
            second = num

    return second

####################################################
if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD WORK!\n"
