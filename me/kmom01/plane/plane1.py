#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Some various ways of saying Hello World in Python.
"""

def alt(hojd):
    """
    Altitude
    """
    print("Altitude:     " + str(int(hojd * 3.28084)) + " feet")


def speed(hastighet):
    """
    Speed
    """
    print("Speed:         " + str(int(hastighet * 0.62137)) + " mph") 
def temp(temperatur):
    """
    Temp
    """
    print("Temperature:   " + str(int(temperatur * 9 / 5 + 32)) + " [F]")


#h = int(input("Ange höjd: "))
#ha = int(input("Ange hastighet: "))
#t = int(input("Ange temp [C]: "))

h = 1100
ha = 1000
t = -50
alt(h)
speed(ha)
temp(t)
