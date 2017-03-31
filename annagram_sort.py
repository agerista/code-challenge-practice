def letter_counts(s):
    """counts letters in a string

    >>> letter_counts("apple")
    {'a': 1, 'e': 1, 'l': 1, 'p': 2}

    >>> letter_counts("bob")
    {'b': 2, 'o': 1}
    """

    counts = {}

    for letter in s:

        if letter not in counts:
            counts[letter] = 1

        else:
            counts[letter] += 1

    return counts


def matches(s1, s2):
    """checks to see if strings are annagrams of each other

    >>> matches("apple", "paple")
    True

    >>> matches("apple", "bob")
    False
    """

    return letter_counts(s1) == letter_counts(s2)


def annagram_sort(lst):
    """list of words sorted by annagrams next to each other

    >>> annagram_sort(["bob", "apple", "obb", "paple"])
    ["bob, "obb", "apple", "paple"]

    >>> annagram_sort(["apple", "berry", "cherry"])
    ["apple", "berry", "cherry"]

    """

    result = []
    while lst:

        word = lst.pop()
        group = [word]

        for s in lst:

            if matches(word, s):
                group.append(s)

        for s in group:
            lst.remove(s)

        result.extend(group)

    return result

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
