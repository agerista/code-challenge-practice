def urlify(s):
    """Write a method to replace all spaces in a string with '%20'.

    >>> urlify("Mr John Smith")
    'Mr%20John%20Smith'

    >>> urlify("Hello this is a test")
    'Hello%20this%20is%20a%20test'
    """

    url = ""

    for char in s:

        if char == " ":
            url += '%20'

        else:
            url += char

    return url

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()

    if not result.failed:
        print "\nALL TESTS PASSED. GOOD WORK!\n"
