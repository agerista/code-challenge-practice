def largest_of_four(arr):
    """Return an array consisting of the largest number from each provided
    sub-array. For simplicity, the provided array will contain exactly 4
    sub-arrays.

    >>> largest_of_four([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]])
    [5, 27, 39, 1001]

    >>> largest_of_four([[4, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1]])
    [9, 35, 97, 1000000]
    """

    largest = []

    for a in arr:

        maximum = sorted(a)
        largest.append(maximum[-1])

    return largest

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD JOB!\n"
