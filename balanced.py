def is_matched(expression):
    """
    Given a string of brackets, determine whether the brackets are balanced. 
    
    >>> is_matched("{[()]}")
    True

    >>> is_matched("{[(])}")
    False

    >>> is_matched("{{[[(())]]}}")
    True
    """

    balance = []

    for char in expression:
        if char == "{" or char == "[" or char == "(":
            balance.append(char)

        elif char == "}":
            if balance[-1] == "{":
                balance.pop()
            else:
                return False

        elif char == "]":
            if balance[-1] == "[":
                balance.pop()
            else:
                return False

        elif char == ")":
            if balance[-1] == "(":
                balance.pop()
            else:
                return False

    if len(balance) == 0:
        return True

################################################################################
if __name__ == '__main__':
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
