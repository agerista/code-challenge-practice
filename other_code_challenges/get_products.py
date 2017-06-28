def get_products_of_all_ints_except_at_index(lst):
    """takes a list of integers and returns a list of the products.

    >>> get_products_of_all_ints_except_at_index([1, 7, 3, 4])
    [84, 12, 28, 21]

    by calculating:
    [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]
    """

    i = 0

    while i <= len(lst):

        



################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()

    if not result.failed:
        print "\nALL TESTS PASSED. GOOD WORK!\n"
