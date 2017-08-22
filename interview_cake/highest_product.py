def highest_product(lst):
    """Given a list of integers, find the highest product you can get from three of the integers.

    The input list_of_ints will always have at least three integers.

    >>> highest_product([1, 2, 3, 4, 5])
    60

    >>> highest_product([1, 2, 3])
    6

    >>> highest_product([-10, -10, 3, 1, 2])
    """

    for i in range(len(lst) - 2):

        if abs(lst[i]) >= abs(lst[i + 1]):
            lst[i], lst[i + 1] = lst[i + 1], lst[i]

    return lst[-3] * lst[-2] * lst[-1]

#############################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD WORK!\n"
