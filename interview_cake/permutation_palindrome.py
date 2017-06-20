def permutation_palindrome(s):

    """Write an efficient function that checks whether any permutation of an input
    string is a palindrome.

    >>> permutation_palindrome("civic")
    True

    >>> permutation_palindrome("ivicc")
    True

    >>> permutation_palindrome("civil")
    False
    """

    s = list(s)
    s.sort()
    no_match = []
    i = len(s) - 1

    while i >= 0:

        if s[i] == s[i - 1]:
            s = s[2:]
            i -= 2

        else:
            no_match.append(s[i])
            s.pop()
            i -= 1

    if len(no_match) > 1:
        return False

    return True

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()

    if not result.failed:
        print "\nALL TESTS PASSED. GOOD JOB!\n"
