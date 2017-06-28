def is_beautiful(w):
    """consider a word, w, to be beautiful if the following two conditions are
    satisfied:

    No two consecutive characters are the same.
    No two consecutive characters are in the following vowel set: a, e, i, o, u, y
    Note that we consider y to be a vowel in this challenge.

    >>> is_beautiful("apple")
    No

    >>> is_beautiful("batman")
    Yes

    >>> is_beautiful("beauty")
    No
    """
    i = 1
    beauty = True

    while i < len(w):

        if w[i] == w[i - 1]:
            beauty = False
            break

        elif w[i] in "aeiouy" and w[i - 1] in "aeiouy":
            beauty = False
            break

        i += 1

    if beauty is True:

        print "Yes"

    else:

        print "No"

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
