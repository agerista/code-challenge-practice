"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_string = open(file_path, "r")

    return text_string.read()


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    i = 0

    corpus = text_string.strip().split()

    while i < len(corpus) - 2:

        n_gram = (corpus[i], corpus[i + 1])

        if chains.get(n_gram, 0) == 0:
            chains[n_gram] = [corpus[i + 2]]

        else:
            chains[n_gram].append(corpus[i + 2])

        i += 1

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    i = 1

    start = choice(chains.keys())
    words.append(start[0])
    words.append(start[1])
    link = choice(chains[start])
    words.append(link)

    while words[-3:] != ['Sam', 'I', 'am']:

        key = (words[i], words[i + 1])
        link = choice(chains[key])
        words.append(link)
        next_key = (key[1], link)
        if chains.get(next_key, 0) == 0:
            break
        else:
            i += 1

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
