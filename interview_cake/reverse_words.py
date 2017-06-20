"""Your team is scrambling to decipher a recent message, worried it's a plot to
break into a major European National Cake Vault. The message has been mostly
deciphered, but all the words are backwards! Your colleagues have handed off the
last step to you.

Write a function reverse_words() that takes a string message and reverses the
order of the words in-place."""


def reverse_words(message):
    """
    >>> reverse_words('find you will pain only go you recordings security the into if')
    'if into the security recordings you go only pain will you find'
    """

    message = message.strip().split(" ")
    message = message[::-1]

    return " ".join(message)


# Non-optimal warm-up solution:

def reverse_words1(message):

    message = message.strip().split(" ")
    deciphered = []
    total = len(message)
    i = 0

    while i < total:
        temp = message.pop()
        deciphered.append(temp)
        i += 1

    return deciphered


message = 'find you will pain only go you recordings security the into if'
reverse_words1(message)


################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD JOB!\n"
