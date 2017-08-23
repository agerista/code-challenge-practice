def is_pangram(phrase):
    """A pangram is a sentence that contains all the letters of the English
    alphabet at least once, like 'The quick brown fox jumps over the lazy
    dog.'

    >>> is_pangram("The quick brown fox jumps over the lazy dog")
    True

    >>> is_pangram("I like cats, but not mice")
    False
    """

    alpha = {}
    phrase = phrase.lower()

    for letter in phrase:

        if letter.isalpha():
            if alpha.get(letter, 0) != 0:
                alpha[letter] += 1

            else:
                alpha[letter] = 0

    if len(alpha) != 26:
        return False

    return True

###########################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD WORK!\n"
