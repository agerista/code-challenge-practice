def string_compression(s):
    """Implement a method to perform basic string compression using the counts
    of repeated characters. If the compressed string would not become smaller than
    the original string, your method should return the original string. You can
    assume the string has only uppercase and lowercase letters(a-z).

    >>> string_compression('aabcccccaaa')
    'a2b1c5a3'

    >>> string_compression('ffaa')
    'ffaa'
    """
    curr = ""
    count = 0
    final = ""

    for char in s:

        if char == curr:
            count += 1

        elif char != curr and count != 0:
            final = final + curr + str(count)
            curr = char
            count = 1

        else:
            curr = char
            count += 1

    final = final + curr + str(count)

    if len(final) >= len(s):
        return s

    else:
        return final

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD JOB!"
