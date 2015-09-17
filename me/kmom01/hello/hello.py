#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Some various ways of saying Hello World in Python.
"""

def hello():
    """
    Print out Hello World in a function.
    """
    print("Hello World in a function.")

for x in range(0, 7):
    if x == 1:
        x = 4
    print("We're on time %d" % (x))


# Call a function that prints out Hello World
hello()

# Print out Hello World
print("Just saying Hello World")

# Assign the string Hello World to a variable and print it out
#str = "Hello World in a variable"
#print(str)
str1 = "Hello World in a variable"
print(str1)
