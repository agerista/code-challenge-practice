import random


def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive).

    >>> lucky_numbers(2)
    [3, 7]

    >>> lucky_numbers(0)
    []

    >>> sorted(lucky_numbers(10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """

    numbers = range(1, 11)
    nums = set()

    while len(nums) < n:

        nums.add(random.choice(numbers))

    return list(nums)

#############################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD WORK!\n"
