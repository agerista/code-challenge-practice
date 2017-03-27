def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list.

    >>> show_evens([1, 2, 3, 4, 6, 8])
    [1, 3, 4, 5]
    """

    even = []
    i = -1

    for num in nums:
        i += 1
        if num % 2 == 0:
            even.append(i)

    return even

################################################################################
if __name__ == '__main__':
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
