def sums(n):
    """Thinking of space complexity in big O terms. Each call will add on to the
    stack, taking up space in memory, so this will be O(n) space.

    >>> sums(5)
    15

    >>> sums(0)
    0

    >>> sums(-1)
    0

    """
    if n <= 0:
        return 0

    return n + sums(n - 1)

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
