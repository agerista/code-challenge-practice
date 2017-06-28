def array_left_rotation(n, k, a):
    """Given an array of n integers and a number, d, perform d left rotations on
    the array. Then print the updated array as a single line of space-separated
    integers.

    >>> array_left_rotation(5, 4, [1, 2, 3, 4, 5])
    5 1 2 3 4

    un-optomized solution, terrible answer: run-time = O(n*k)
    """

    while k > 0:

        rotation = a.pop(0)
        a.append(rotation)
        k -= 1

    print ' '.join(str(x) for x in a)


def arr_left_rot(n, k, a):
    """Given an array of n integers and a number, d, perform d left rotations on
    the array. Then print the updated array as a single line of space-separated
    integers.

    >>> array_left_rotation(5, 4, [1, 2, 3, 4, 5])
    5 1 2 3 4

    more optomized solution, run-time = O(1)

    """

    answer = a[k:] + a[:k]
    print ' '.join(str(x) for x in answer)

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
