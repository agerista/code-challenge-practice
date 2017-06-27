def smallest_substring(arr, s):
    """
    >>> smallest_substring(['x','y','z'], 'xyyzyzyx')
    'zyx'

    >>> smallest_substring(['a','c','e'], 'cceccaeceeacc')
    'cae'

    >>> smallest_substring(['a','x','e'], 'cceccaeceeacc')
    ''
    """

    head = 0
    tail = len(arr)
    shortest = ''

    while head <= len(s):

        temp = set(s[head:tail])

        if tail == len(s) and head < (len(s) - len(arr)):
            head += 1

        if sorted(temp) != sorted(arr) and tail < len(s):
            tail += 1

        elif sorted(temp) == sorted(arr):
            if shortest == '':
                shortest = s[head:tail]

            elif len(s[head:tail]) < len(shortest):
                shortest = s[head:tail]
            head += 1

        else:
            break

    return shortest

################################################################################
if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD JOB!\n"
