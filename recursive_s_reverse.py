def rev_string(astring):
    """Return reverse of string using recursion.

    You may NOT use the reversed() function!

    >>> rev_string("porcupine")
    'enipucrop'
    """

    if len(astring) < 2:
        return astring

    return astring[-1] + rev_string(astring[:-1])

rev_string("porcupine")

################################################################################
if __name__ == '__main__':
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
