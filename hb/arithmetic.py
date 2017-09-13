"""Utility file for calculator.py"""
# TODO write tests!!!

from calculator import *


def play():
    print "hello"

    exit = False

    while not exit:

        calculate = raw_input("> input command  ").strip().split()

        if calculate[0] == "+":
            result = add(float(calculate[1]), float(calculate[2]))

        elif calculate[0] == "-":
            result = subtract(float(calculate[1]), float(calculate[2]))

        elif calculate[0] == "*":
            result = multiply(float(calculate[1]), float(calculate[2]))

        elif calculate[0] == "/":
            result = divide(float(calculate[1]), float(calculate[2]))

        elif calculate[0] == "square":
            result = square(float(calculate[1]))

        elif calculate[0] == "cube":
            result = cube(float(calculate[1]))

        elif calculate[0] == "pow":
            result = power(float(calculate[1]), float(calculate[2]))

        elif calculate[0] == "mod":
            result = mod(float(calculate[1]), float(calculate[2]))

        elif calculate[0] == "x+":
            result = addMult(float(calculate[1]), float(calculate[2]), float(calculate[3]))

        elif calculate[0] == "3+":
            result = cubeSum(float(calculate[1]), float(calculate[2]))

        elif calculate[0] == "q":
            break

        else:
            print "incorrect input, try again"

        print result

play()
