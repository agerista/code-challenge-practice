def one_away(w1, w2):
    """Given two strings, are they, at most, one edit away?

    >>> one_away("make", "fake")
    True

    >>> one_away("task", "take")
    False

    >>> one_away("ask", "asks")
    True

    >>> one_away("sand", "and")
    True
    """

    longer = max(w1, w2)
    shorter = min(w1, w2)
    different = 0
    i = j = 0

    if (len(longer) - len(shorter)) >= 2:
        return False

    while j < len(shorter):

        if longer[i] != shorter[j]:
            different += 1

            if different > 1:
                return False

            if len(longer[i:]) == len(shorter[j:]):
                i += 1
                j += 1

            else:
                i += 1

        else:
            i += 1
            j += 1

    return True

#################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD WORK!\n"
