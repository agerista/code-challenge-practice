def calculate_median_rating(businesses):

    new_list = []

    for business in businesses:

        new_list.append(business[1])

    if len(new_list) < 1:

        return None

    elif len(new_list) % 2:

        return len(new_list - 1) / 2.0

    else:

        return len(new_list - 1) + len(new_list) / 2.0

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
