def highest_product(lst):
    """Given a list of integers, find the highest product you can get from three of the integers.

    The input list_of_ints will always have at least three integers.
    """

    abValueList = []

    for num in lst:

        abValueList.append(abs(num))

    abValueList.sort()
    max_prod = abValueList[-3] * abValueList[-2] * abValueList[-1]

    return max_prod


def highest_product2(lst):

    high = max(lst[0], lst[1])
    low = min(lst[0], lst[1])

    high_prod2 = lst[0] * lst[1]
    high_prod3 = lst[0] * lst[1] * lst[2]
    low_prod = lst[0] * lst[1]

    for num in lst[2:]:

        high_prod3 = max(high_prod3, num * high_prod2, num * low_prod)
        high_prod2 = max(high_prod2, num * high, num * low)
        low_prod = min(low_prod, num * high, num * low)

        high = max(high, num)
        low = min(low, num)

    return high_prod3


def highest_product3(lst):

    if lst[0] >= lst[1]:
        high = lst[0]
        low = lst[1]
    else:
        low = lst[0]
        high = lst[1]

    high_prod2 = lst[0] * lst[1]
    high_prod3 = lst[0] * lst[1] * lst[2]
    low_prod = lst[0] * lst[1]

    for num in lst[2:]:

        if num * high_prod2 > high_prod3:
            high_prod3 = num * high_prod2

        if num * low_prod > high_prod3:
            high_prod3 = num * low_prod

        if num * high > high_prod2:
            high_prod2 = num * high

        if num * low > high_prod2:
            high_prod2 = num * low

        if num * low < low_prod:
            low_prod = num * low_prod

        if num * high < low_prod:
            low_prod = num * high

        if num > high:
            high = num

        if num < low:
            low = num

    return high_prod3

#############################################################################
assert highest_product([1, 2, 3, 4, 5]) == 60
assert highest_product([1, 10, -5, 1, -100]) == 5000
assert highest_product([-10, -10, 3, 1, 2]) == 300

assert highest_product2([1, 2, 3, 4, 5]) == 60
assert highest_product2([1, 10, -5, 1, -100]) == 5000
assert highest_product2([-10, -10, 3, 1, 2]) == 300

assert highest_product3([1, 2, 3, 4, 5]) == 60
assert highest_product3([1, 10, -5, 1, -100]) == 5000
assert highest_product3([-10, -10, 3, 1, 2]) == 300
