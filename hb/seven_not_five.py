def seven_not_five():
    """Find all numbers divisible by 7 that are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line."""

    for num in range(2000, 3201):

        if num % 7 == 0 and num % 5 != 0:
            print num,

seven_not_five()
