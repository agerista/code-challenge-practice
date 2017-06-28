def recursive_index(needle, haystack):
    """Return the list index recursively for a given search term. If the search
    term is not found, return None.

    >>>  recursive_index("hey", ["hey", "there", "you"])
    0

    >>> recursive_index("folks", ["hey", "there", "you"])
    None

    >>> recursive_index("you", ["hey", "there", "you"])
    2
    """

    if haystack == []:
        return None

    if haystack[0] == needle:
        return 0

    result = recursive_index(needle, haystack)
    if result is not None:
        return 1 + result


def recursive_index2(needle, haystack, result=0):
    """
    >>> recursive_index2("hey", ["hey", "there", "you"])
    0

    >>> recursive_index2("folks", ["hey", "there", "you"])
    None

    >>> recursive_index2("you", ["hey", "there", "you"])
    2
    """

    if haystack == []:
        return None

    if haystack[0] == needle:
        return 0

    if result is not None:
        return 1 + recursive_index(needle, haystack, result+1)

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD WORK!\n"
