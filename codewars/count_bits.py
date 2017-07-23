def countBits(n):
    """Write a function that takes an (unsigned) integer as input, and returns
    the number of bits that are equal to one in the binary representation of that
    number.

    >>> countBits(0)
    0
    >>> countBits(4)
    1
    >>> countBits(7)
    3
    >>> countBits(9)
    2
    >>> countBits(10)
    2
    """

    bits = bin(n).count('1')
    return bits

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD WORK!\n"
