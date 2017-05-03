def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses.

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> max([binary_search(i) for i in range(1, 101)])
    7

    """

    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0
    guess = None
    high = 101
    low = 0

    while guess != val:

        num_guesses += 1
        guess = (high - low) / 2 + low

        if val > guess:

            low = guess

        elif val < guess:

            high = guess

    return num_guesses

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD WORK!\n"
