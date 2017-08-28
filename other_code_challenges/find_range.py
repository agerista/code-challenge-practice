def find_range(nums):
    """Given list of numbers, return smallest & largest number as a tuple.

    >>> find_range([3, 4, 2, 5, 10])
    (2, 10)

    >>> find_range([43, 3, 44, 20, 2, 1, 100])
    (1, 100)

    >>> find_range([])
    (None, None)

    >>> find_range([7])
    (7, 7)
    """

    if nums == []:
        return None, None

    else:

        return min(nums), max(nums)


def find_range2(nums):
    """Given list of numbers, return smallest & largest number as a tuple.

    >>> find_range2([3, 4, 2, 5, 10])
    (2, 10)

    >>> find_range2([43, 3, 44, 20, 2, 1, 100])
    (1, 100)

    >>> find_range2([])
    (None, None)

    >>> find_range2([7])
    (7, 7)
    """
    if nums == []:
        return None, None

    smallest = nums[0]
    largest = nums[0]

    for num in nums:

        if num < smallest:
            smallest = num

        if num > largest:
            largest = num

    return smallest, largest

#############################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD WORK!\n"


