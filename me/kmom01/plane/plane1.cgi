#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Me-page redovisning, texts from each course moment.
As cgi.

"""


# To write pagecontent to sys.stdout as bytes instead of string
import sys
import codecs


#Enable debugging of cgi-.scripts
import cgi, cgitb
cgitb.enable()


# Send the HTTP header
print("Content-Type: text/plain;charset=utf-8")
print("Content-Type: text/html;charset=utf-8")
print("")

print("<TITLE>CGI script output</TITLE>")
print("<H3>This is my first CGI script</H3>")
#print("Hello, world!")


import sys
import math
sys.stderr = sys.stdout

#x = 200
#print(x  * x)




###############################################################################

def alt(hojd):
    """
    Altitude
    """
    print("Altitude:     " + str(int(hojd * 3.28084)) + " feet <br>")


def speed(hastighet):
    """
    Speed
    """
    print("Speed:         " + str(int(hastighet * 0.62137)) + " mph <br>")
def temp(temperatur):
    """
    Temp
    """
    print("Temperature:   " + str(int(temperatur * 9 / 5 + 32)) + " [F] <br>")


#h = int(input("Ange höjd: "))
#ha = int(input(" "))
#t = int(input("Ange temp [C]: "))

h = 100
ha = 1000
t = -50
alt(h)
speed(ha)
temp(t)
#######################################################################################




#<h1>Min Redovisnings-sida, <i>bjvi13 alt. erikwi2000</i></h1>
# Here comes the content of the webpage
content = """




"""


# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content)
