def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.
    If the word begins with a consonant (not a, e, i, o, u),
    move the first letter to the end and add ‘ay’

    If the word begins with a vowel, add ‘yay’ to the end


        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """

    vowel = "aeiou"
    latin = phrase.split()
    new_phrase = []

    for word in latin:
        if word[0] in vowel:
            new_phrase.append(word + 'yay')

        else:
            new_phrase.append(word[1:] + word[0] + 'ay')

    return " ".join(new_phrase)

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
