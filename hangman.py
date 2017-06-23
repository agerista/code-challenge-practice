import random


def board():
    """set up initial board for the game"""

    "-" * 10
    "|" * 25  # can you do this vertically?
    "_" * 10


def choose_word():
    """choose a random word for the game"""

    word = set("apple", "banana", "cherry")

    return random(word)


def track_turns(word):
    """keep track of how many turns a player has taken"""

    turns = len(word) - 2
    guesses = 0

    while guesses <= turns:

        guess = raw_input("> enter a letter:  ")
        guesses += 1

        if guess != word:
            continue

        elif guess == word:
            print "Congratulations, you win!"

        else:
            print "Sorry, you lose!"



