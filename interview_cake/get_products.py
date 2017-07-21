def get_products_of_all_ints_except_at_index(l):
    """Write a function that takes a list of integers and returns a list of the
    products. Do not use division in your solution.

    >>> get_products_of_all_ints_except_at_index([1, 7, 3, 4])
    [84, 12, 28, 21]

    >>> get_products_of_all_ints_except_at_index([3, 5, 7, 9])
    [315, 189, 135, 105]

    >>> get_products_of_all_ints_except_at_index([0, 5, 7, 9])
    [315, 0, 0, 0]
    """

    i = 0
    prod = 1
    result = []

    while i < len(l):

        temp = l[:i] + l[i+1:]

        for num in temp:

            prod *= num

        result.append(prod)
        prod = 1
        i += 1

    return result


def get_products_of_all_ints_except_at_index2(l):
    """
    >>> get_products_of_all_ints_except_at_index2([1, 7, 3, 4])
    [84, 12, 28, 21]

    >>> get_products_of_all_ints_except_at_index2([3, 5, 7, 9])
    [315, 189, 135, 105]

    >>> get_products_of_all_ints_except_at_index2([0, 5, 7, 9])
    [315, 0, 0, 0]
    """

    i = 0
    prod = 1

    for num in l:

        if num != l[i]:
            prod *= num

        l[i] = prod
        prod = 1

    return l
################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD WORK!\n"
