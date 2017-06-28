class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        pass

    def comparator(a, b):
        """Given an array of n Player objects, write a comparator that sorts them
        in order of decreasing score; if  or more players have the same score,
        sort those players alphabetically by name.

        aleksa 150
        amy 100
        david 100
        aakansha 75
        heraldo 50
        """


        val = b.score - a.score
        if val == 0:
            return -1 if a.name < b.name else 1
        return val


# n = int(raw_input())
# data = []
# for i in range(n):
#     name, score = raw_input().split()
#     score = int(score)
#     player = Player(name, score)
#     data.append(player)

# data = sorted(data, cmp=Player.comparator)
# for i in data:
#     print i.name, i.score
################################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
