import sys


def word_count(filename):

    word_dict = {}

    for row in open(filename):

        line = row.strip().replace(",", "").replace('"', "").replace(".", "").lower().split()

        for word in line:

            if word_dict.get(word, 0) == 0:
                word_dict[word] = 1

            else:
                word_dict[word] += 1

    for key, value in word_dict.iteritems():

        print key, value


filename = sys.argv[1]
word_count(filename)
