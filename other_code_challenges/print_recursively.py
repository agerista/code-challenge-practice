def print_recursively(lst):
    """Print items in the list, using recursion.

    >>> print_recursively([1, 2, 3])
    1
    2
    3
    """

    if lst == []:
        return

    print lst[0]
    return print_recursively(lst[1:])


###################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD WORK!\n"
