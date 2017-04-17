def longest_word(str):
    """Return the length of the longest word in the a sentence

    >>> longest_word("The quick brown fox jumped over the lazy dog")
    6

    >>> longest_word("May the force be with you")
    5

    >>> longest_word("What if we try a super-long word such as otorhinolaryngology")
    19

    """

    count = 0
    phrase = str.split()

    for word in phrase:

        if len(word) > count:

            count = len(word)

    return count


def longest_word2(phrase):
    """
    Return a list of all words in the phrase, along with the length of the 
    longest word in the phrase.

    >>> longest_word2("The quick brown fox jumped over the lazy dog")
    (6, ['The', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog'])


    >>> longest_word2("May the force be with you")
    (5, ['May', 'the', 'force', 'be', 'with', 'you'])

    >>> longest_word2("What if we try a super-long word such as otorhinolaryngology")
    (19, ['What', 'if', 'we', 'try', 'a', 'super-long', 'word', 'such', 'as', 'otorhinolaryngology'])

    """

    length = 0
    count = 0
    len_list = []

    for char in phrase:

        if char != " ":

            length += 1

        elif char == " ":
            len_list.append(phrase[:length])
            phrase = phrase[length + 1:]
            length = 0

        if count < length:
            count = length

    len_list.append(phrase[:length])
    return count, len_list


def longest_word_fancy(phrase):
    """Return the length of the longest word in the a sentence

    >>> longest_word("The quick brown fox jumped over the lazy dog")
    6

    >>> longest_word("May the force be with you")
    5

    >>> longest_word("What if we try a super-long word such as otorhinolaryngology")
    19

    """

    phrase = sorted(phrase.split(), key=len)

    return phrase[-1]

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD WORK!\n"
