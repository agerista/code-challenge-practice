def pair_sum(arr, n):
    """Return number of pairs in an array that add up to a given number

    >>> pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1], 10)
    6

    >>> pair_sum([1,2,3,1], 3)
    1

    >>> pair_sum([1,2,3,2,2], 4)
    2
    """

    seen = set()
    pairs = set()

    for num in arr:

        target = n - num

        if target not in seen:
            seen.add(num)

        else:
            pairs.add(((min(num, target), max(num, target))))

    return len(pairs)
    # print "\n".join(map(str, list(pairs)))

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD JOB!\n"
