def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place.

    >>> print_digits(1)
    1
    >>> print_digits(314)
    4
    1
    3
    >>> print_digits(12)
    2
    1
    """

    while num:

        if num > 9:
            print num % 10
            num = num / 10

        else:
            print num
