def reverse_words(message):
    """Write a function reverse_words() that takes a string message and reverses
    the order of the words

    >>> reverse_words('find you will pain only go you recordings security the into if')
    'if into the security recordings you go only pain will you find'

    """

    decipher = message.split()

    return ' '.join(decipher[::-1])

def reverse_words2(message):
    """Write a function reverse_words() that takes a string message and reverses
    the order of the words

    >>> reverse_words2('find you will pain only go you recordings security the into if')
    'if into the security recordings you go only pain will you find'

    >>> reverse_words2('hello help me')
    'me help hello'
    """

    result = []
    start = 0
    stop = 0

    for character in message:

        stop += 1

        if character == ' ':

            result.append(message[start:stop - 1])
            start = stop

    result.append(message[start:])
    result = result[::-1]
    return ' '.join(result)

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
