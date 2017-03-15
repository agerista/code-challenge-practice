def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise.

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True

    >>> is_pangram("I like cats, but not mice")
    False
    """

    alpha = set()
    is_alpha = False

    for character in sentence:
        alpha.add(character)

        if len(alpha) == 26:
            is_alpha = True

    return is_alpha

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
