def missing_number(lst, max_num):
    """Given a list of numbers 1-max inclusive, find the missing number

    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8

    non-optomized version
    """
    count = 0

    while count <= max_num:

        count += 1
        if count not in lst:

            return count


def missing_number_2(lst, max_num):
    """Given a list of numbers 1-max inclusive, find the missing number

    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8

    optomized version
    """

    seen = [False] * max_num

    for num in lst:
        seen[num - 1] = True

    # False value is the number we have not seen
    return seen.index(False) + 1


def missing_number_3(lst, max_num):

    """Given a list of numbers 1-max inclusive, find the missing number

    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8

    one more way
    """

    lst.append(max_num + 1)
    lst.sort()
    last = 0

    for i in lst:

        if i != last:
            return last + 1

        last += 1

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
