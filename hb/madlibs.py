"""A madlib game that compliments its users."""

from random import choice
from flask import Flask, render_template, request
from madlibs_scripts import (get_input_fields, madlibs_scripts)

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask("madlibs")

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]



@app.route('/')
def start_here():
    """Display homepage."""

    print "hello!"

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    print "hello!"

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game', methods=['GET', 'POST'])
def play_madlibs():
    """Madlibs Game"""

    text = madlibs_scripts()
    title = text[0]
    script = text[1].strip().split()
    # print script
    game = get_input_fields(text)
    print game
    fields = {}
    i = 0

    if request.method == 'GET':
        return render_template("game.html", game=game)

    elif request.method == 'POST':
        for key, value in game.iteritems():
            fields[key] = key
            fields[key] = []
            for item in range(0, value):
                num = str(item + 1)
                field = request.form.get(key + "-" + num)
                fields[key].append(field)

        for word in script:
            if fields.get(word, 0) != 0:
                script[i] = fields[word][0]
                try:
                    fields[word] = fields[word][1:]
                except KeyError:
                    "No key found"
            i += 1



        print script

        return render_template("game.html", game=game, script=script)

# @app.route('/game')
# def madlibs_results():
#     """Funny results ensue"""

    
    # TODO: get fields from form and plug them into the script 

    # results = request.form.get("h3")

    # for result in results:
    #     print result

    

    
if __name__ == "__main__":

    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = False
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    app.run(port=5000, host='0.0.0.0')
