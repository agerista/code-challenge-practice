"""Generate Markov text from text files."""

import os
import sys
from random import choice
import tweepy


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text = ""

    for file in file_path:
        text_string = open(file)
        text = text + text_string.read()
        text_string.close()

    return text


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
    """Return text from chains"""

    next = True

    # Choose a starting point for the Markov chain
    key = choice(chains.keys())
    words = [key[0], key[1]]
    link = choice(chains[key])

    while next:

        words.append(link)
        key = (key[1], link)
        link = choice(chains[key])
        next_key = (key[1], link)

        # If there is no next key, stop generating text
        if chains.get(next_key, 0) == 0:
            next = False

    # Make the text tweet length
    words.append(link)
    customize = " ".join(words)
    tweet = customize[:140]

    return tweet


def post_to_twitter(tweet):
    """limit chains to 140 characters"""

    # Twitter credentials
    consumer_key = os.environ['TWITTER_CONSUMER_KEY']
    consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
    access_token = os.environ['TWITTER_ACCESS_TOKEN']
    access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

    # OAuth process
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # TWEET!!!
    return api.update_status(tweet)


input_path = sys.argv[1:]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)
print random_text

# Post tweet to twitter
twit = post_to_twitter(random_text)

print twit
