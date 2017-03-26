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


def is_matched2(expression):
    """Given a string of brackets, determine whether the brackets are balanced.

    >>> is_matched("{[}")
    False

    >>> is_matched("{[(])}")
    False

    >>> is_matched("{{[[(())]]}}")
    True
    """

    balanced = {"{": "}",
                "[": "]",
                "(": ")"
                }
    stack = []

    if len(expression) < 2 or len(expression) % 2 != 0:
        return False


    for i in expression:

        if i in balanced.keys():
            stack.append(balanced[i])

        elif len(stack) > 0 and i == stack[-1]:
            stack.pop()

        else:
            return False

    return True

################################################################################
if __name__ == '__main__':
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
