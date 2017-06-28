def merge_lists(lst1, lst2):
    """Merge two sorted lists

    merge_lists([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    """

    final = []

    while len(lst1) > 0 or len(lst2) > 0:

        if lst1 == []:
            final.append(lst2.pop(0))

        elif lst2 == []:
            final.append(lst1.pop(0))

        elif lst1[0] < lst2[0]:
            final.append(lst1.pop(0))

        else:
            final.append(lst2.pop(0))

    return final


def sort_list(lst):
    """sort lists, yay!

    >>> sort_list([3, 1, 5])
    [1, 3, 5]
    """

    if len(lst) == 1:
        return lst

    else:
        mid = int(len(lst) / 2)
        lst_a = sort_list(lst[:mid])
        lst_b = sort_list(lst[mid:])

        return merge_lists(lst_a, lst_b)

################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
