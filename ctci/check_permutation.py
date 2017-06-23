def check_permutation(s1, s2):
    """Given two strings, write a method to decide if one is a permutation of
    the other

    >>> check_permutation('cat', 'taco')
    False

    >>> check_permutation('hello', 'elloh')
    True

    """

    d1 = {}
    d2 = {}

    for char in s1:

        if d1.get(char, 0) >= 1:
            d1[char] += 1
        else:
            d1[char] = 1

    for char in s2:

        if d2.get(char, 0) >= 1:
            d2[char] += 1
        else:
            d2[char] = 1

    if d1 == d2:
        return True

    return False

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()

    if not result.failed:
        print "\nALL TESTS PASSED. GOOD WORK!\n"
