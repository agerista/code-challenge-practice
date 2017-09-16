from bs4 import BeautifulSoup
import urllib2
import os

misspelled = {}

def get_misspelled_words(source):
    """Scrapes wikipedia for the most common misspelled words"""

    content = urllib2.urlopen(source).read()
    soup = BeautifulSoup(content)

    for div in soup.find_all("div", class_="div-col columns column-count column-count-2"):
        for litag in soup.find_all("li", attrs={"class": None, "id": None}):
            words = litag.text.encode("utf-8")
            word = words.strip().split()
            right = word[0]
            temp = word[2:]
            if temp != []:
                wrong = temp[0]
            add_to_dict(right, wrong)


def add_to_dict(right, wrong, misspelled):
    """Adds misspelled words to dictionary"""

    errors = ('"100', '"Canadian,', '"Merriam-Webster', '"200', 'Linguistic',
                 'Nonstandard', 'Orthography', 'All', 'Articles', "Often", "With")

    if right not in errors and wrong not in errors and wrong != []:
        if misspelled.get(right, 0) == 0:
            wrong.replace('[1]', '').replace('[2]', '').replace('[3]', '').replace('[4]', '').replace('[5]', '')
            misspelled[right] = wrong

    print misspelled
    return misspelled

source = get_misspelled_words("https://en.wikipedia.org/wiki/Commonly_misspelled_English_words#Typing_errors")