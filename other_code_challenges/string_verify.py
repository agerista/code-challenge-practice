def string_verify(s):
    """Given a string S find out if the string contains: alphanumeric characters,
    alphabetical characters, digits, lowercase and uppercase characters.

    >>> string_verify("qA2")
    True
    True
    True
    True
    True

    >>> string_verify('123')
    True
    False
    True
    False
    False

    >>> string_verify('Abc')
    True
    True
    False
    True
    True

    """

    print any(c.isalnum() for c in s)
    print any(c.isalpha() for c in s)
    print any(c.isdigit() for c in s)
    print any(c.islower() for c in s)
    print any(c.isupper() for c in s)


################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print
        print "ALL TESTS PASSED. GOOD WORK!"
        print
