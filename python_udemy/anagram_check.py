def anagram_check(str1, str2):
    """checks if 2 strings are anagrams of one another

    >>> anagram_check("go go go", "gggooo")
    True

    >>> anagram_check("abc", "cba")
    True

    >>> anagram_check("hi man", "hi     man")
    True

    >>> anagram_check("123", "1 2")
    False

    >>> anagram_check("aabbcc", "aabbc")
    False
    """

    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    d1 = {}
    d2 = {}

    if len(str1) != len(str2):
        return False

    for letter in str1:
        if d1.get(letter, 0) == 0:
            d1[letter] = 1

        else:
            d1[letter] += 1

    for letter in str2:
        if d2.get(letter, 0) == 0:
            d2[letter] = 1

        else:
            d2[letter] += 1

    if d1 == d2:
        return True

    else:
        return False

#############################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD JOB!\n"
