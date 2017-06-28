def prime_checker(num):
    """determines if a number is prime or not

    >>> prime_checker(2)
    True

    >>> prime_checker(3)
    True

    >>> prime_checker(4)
    False

    >>> prime_checker(25)
    False
    """

    assert num > 0

    if num < 2:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    n = 3

    while n * n <= num:

        if num % n == 0:
            return False

        else:
            num += 2

    return True


def primes(count):
    """Return count number of prime numbers, starting at 2.

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]
    """

    prime_list = []
    num = 2

    while count > 0:

        if prime_checker(num):
            prime_list.append(num)
            count -= 1
            num += 1

    return prime_list

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
