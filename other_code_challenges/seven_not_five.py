def seven_not_five():
    """Find all numbers divisible by 7 that are not a multiple of 5,
    between 2000 and 3200 (both included). The numbers obtained should
    be printed in a comma-separated sequence on a single line.

    * Note: the following is not a complete documentation of the output,
    and the doctest is therefore expected to fail.

    seven_not_five()
    2002,  2009,  2016,  2023,  2037,  2044,  2051, ...
    """

    for num in range(2000, 3201):

        if num % 7 == 0 and num % 5 != 0:
            print str(num) + ", ",

########################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD JOB!\n"
