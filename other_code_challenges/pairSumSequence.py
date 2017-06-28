def pairSumSequence(n):
    """reviewing big O time, thinking about space complexity. There will be roughly
    O(n) calls to pairSum. Those calls happen one at a time, not simultaneously,
    so you only need O(1) space for this function.

    >>> pairSumSequence(5)
    25

    >>> pairSumSequence(3)
    9

    """

    sum = 0
    i = 0
    while i < n:
        sum += pairSum(i, i + 1)
        i += 1

    return sum


def pairSum(a, b):

    return a + b

pairSumSequence(5)

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
