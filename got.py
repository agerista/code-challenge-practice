def possible_palindromes(astr):
    """ game of thrones 1 -- any possible palindrome --
    Write the code to find the required palindrome and then assign the variable
    'found' a value of True or False

    test 1
    aaabbbb
    Yes
    bbaaabb

    test 2
    cdefghmnopqrstuvw
    No

    test 3
    cdcdcdcdeeeef
    cdcdeefeedcdc2

    """

    pal = {}
    final = []

    for letter in astr:

        if letter not in pal:

            pal[letter] = 1

        else:
            pal[letter] += 1

    for key, value in pal.iteritems():
        check how many values are odd
            if more than one odd
                not palindrome
            else:
                palindrome





    found = False

    if not found:
        print("NO")
    else:
        print("YES")


################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
