def is_palindrome(word):
    """If a given string is the spelled the same forwards and backwards, it is a
    palindrome. You must remove all non-alphanumeric characters.

    >>> is_palindrome("RaceCar")
    True

    >>> is_palindrome("2a3*3a2")
    True

    >>> is_palindrome("Tattoo")
    False
    """
    word = validator(word)

    if word == "":
        return True

    elif word[0] == word[-1]:
            return is_palindrome(word[1:-1])

    return False


def validator(word):
    """string validator for is_palindrome"""

    word = word.lower()

    if not word.isalnum():
        word = ''.join(c for c in word if c.isalnum())

    return word

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD WORK!\n"
