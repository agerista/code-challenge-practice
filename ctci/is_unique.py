def is_unique(s):
    """Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?

    >>> is_unique('cat')
    True

    >>> is_unique('hello')
    False

    """
    seen = ""

    for char in s:
        
        if char in seen:
            return False
        
        seen = seen + char
    
    return True

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()

    if not result.failed:
        print "\nALL TESTS PASSED. GOOD JOB!\n"
