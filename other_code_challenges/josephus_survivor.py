def find_survivor(num_people, kill_every):
    """Given num_people in circle, kill [kill_every]th person, return survivor.

    1  2  3  4  5  6  7  8  9  10
       !  X        X  !     X
    1  2  3  4  5  6  7  8  9  10
    !  X  X        X  X  !  X

    1  2  3  4  5  6  7  8  9  10
    X  X  X     !  X  X  X  X

    1  2  3  4  5  6  7  8  9  10
    X  X  X     X  X  X  X  X  !

    >>> find_survivor(10, 3)
    4

    """

    i = 0
    kill_list = [] 

    while len(num_people) > 1:

        if i % kill_every == 0:

            num_people.pop(i)

    return i

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "/n ALL TESTS PASSED. GOOD WORK! /n"
