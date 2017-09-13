"""Restaurant rating lister."""
from random import choice

# TODO: Add menu links

rankings = {}


def add_ratings_to_dict(filename):
    """Takes in a file and sorts restuarants alphabetically with a rating"""

    for row in open(filename):
        line = row.strip().split(":")
        if rankings.get(line[0], 0) == 0:
            rankings[line[0]] = line[1]

    return user_options()


def user_options():
    """Gives user menu choices"""

    print "\n\nWould you like to:\n"
    print "1. See all restaurant ratings"
    print "2. Add a new restaurant"
    print "3. Change the rating of a random restaurant"
    print "4. Change the rating of a specific restaurant"
    print "5. Quit\n"
    option = raw_input("Enter your choice here:  ")

    if option == "1":
        return view_restaurant_ratings()

    elif option == "2":
        return add_restaurant_rating()

    elif option == "3":
        return change_random_rating()

    elif option == "4":
        return change_specific_rating()

    elif option == "5":
        print "\nThanks for stopping by!"
        return

    else:
        print "I didn't understand your choice, please try again."
        return user_options()


def view_restaurant_ratings():
    """Prints a sorted list of restaurant rankings"""

    for key, value in sorted(rankings.iteritems()):
        print key, value

    return user_options()


def add_restaurant_rating():
    """Allows a user to add a retaurant and rating to the dictionary"""

    add = False

    while not add:

        add_restauarant = raw_input("Would you like to add a new restaurant? Enter Y or N  ")

        if add_restauarant == "Y" or add_restauarant == "y":
            print "Enter a restaurant and a ranking like this: 'Restaurant Name: Rating(1-5)'"
            new_restaurant = raw_input(">Your entry  ")
            new_restaurant = new_restaurant.strip().split(": ")

            if int(new_restaurant[1]) not in range(1, 6):
                print "Your rating was not between 1 and 5, please try again."
                continue

            elif rankings.get(new_restaurant[0], 0) == 0:
                rankings[new_restaurant[0]] = new_restaurant[1]

                print "Would you like to rate another restaurant?"
                answer = raw_input(">Enter Y or N  ")

                if answer == "Y" or answer == "y":
                    continue

                elif answer == "N" or answer == "n":
                        add = True

                else:
                    print "I didn't understand that answer"

            else:
                print "That restaurant has already been added, please add another"

        else:
            add = True

    return user_options()


def change_random_rating():
    """Picks a restaurant at random and allows the user to change the rating"""

    selection = choice(list(rankings.items()))
    print "Selected restaurant is %s: " % selection[0]
    print "Current ranking is %s: " % selection[1]
    print "Would you like to change this rating?"
    response = raw_input(">Enter Y or N  ")

    if response == "Y" or response == "y":
        new_rating = raw_input("Please enter your new rating(1-5):  ")
        rankings[selection[0]] = new_rating
        print "We have updated the rating."

    elif response == "N" or response == "n":
        print "We will keep a %s rating for %s" % (selection[1], selection[0])

    return user_options()


def change_specific_rating():
    """User specifies a restaurant rating to update"""

    print "What restaurant rating would you like to change?"
    reply = raw_input(">Enter the restaurant name  ")

    if rankings.get(reply, 0) != 0:
        update = raw_input(">Enter the new rating(1-5):  ")

        if int(update) in range(1, 6):
            rankings[reply] = update

        else:
            print "Your ranking was not between 1 and 5, try again."

    else:
        print "That restaurant is not in our system, please add it using option 2."

    return user_options()

add_ratings_to_dict("scores.txt")
