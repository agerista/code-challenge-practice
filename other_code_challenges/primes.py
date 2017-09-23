def primes(n):
    """Return a list of n prime numbers, prime numbers begin with 2.

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]
    """

    result = [2]
    num = 3

    if n < 1:
        return []

    if n == 1:
        return result

    while len(result) < n:

        if is_prime(num):
            result.append(num)

        num += 2

    return result


def is_prime(num):
    """checks if a number is prime, because this is a helper function for primes,
    it is assumed that the number is 2 or greater.

    >>> is_prime(2)
    True

    >>> is_prime(4)
    False
    """

    n = 3

    if num % 2 == 0 and num != 2:
        return False

    while n * n <= num:
        if num % n == 0:
            return False

        n += 2

    return True

##################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()

    if not result.failed:
        print "\nALL TESTS PASSED. GOOD WORK!\n"
