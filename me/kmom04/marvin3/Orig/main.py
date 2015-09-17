#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.

"""




from marvin import menu
from marvin import myHoppsan
from marvin import myDate
#from marvin import meImage
#from marvin import meImagex
#from marvin import meImageBIG
from marvin import guessNumber
from marvin import myNameIs
from marvin import myAgeIs
from marvin import myMoonWeight
from marvin import myMinutes2Hours
from marvin import myDegC2F
from marvin import myWordBoost

from marvin import myRandGen
from marvin import mySumAvg
from marvin import myP2G
from marvin import myPyt
from marvin import myCircleArea
from marvin import mySameSame








# MAIN  MAIN MAIN  MAIN  MAIN IN  MAIN  MAIN  MAIN  MAIN
def main():
    """
    This is the main method, I call it main by convention.
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    while True:
        #print("MMMMMMMMMMMMMMMMMMMMMMMMMM")
        menu()
        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            return
        elif choice == "1":
            myNameIs()
        elif choice == "2":
            myAgeIs()
        elif choice == "3":
            myMoonWeight()
        elif choice == "4":
            myMinutes2Hours()

        elif choice == "5":
            myDegC2F()

        elif choice == "6":
            myWordBoost()

        elif choice == "7":
            myRandGen()
        elif choice == "8":
            mySumAvg()

        elif choice == "9":
            myP2G()

        elif choice == "10":
            myCircleArea()

        elif choice == "11":
            myPyt()
        elif choice == "12":
            mySameSame()
        elif choice == "13":
            guessNumber()
        elif choice == "14":
            myDate()
        elif choice == "15":
            myHoppsan()

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")


#print("wwfffffffffffffffffwwwwwww")
if __name__ == "__main__":
#    print("wwwwwwwwwwwwwwwwwwwww")
    main()
#======================================0


#from datetime import datetime


"""
def myNameIs():

    Read the users name and say hello to Marvin.

    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")
"""
"""
def myAgeIs():

    Read user bd


    age = input("Pls enter your age: ")
    try:
        age = int(age)
    except ValueError:
        print("Try to enter a number please")
        main()
      #  quit()
    print("Your age is more than: " +  str(age * 365 * 24 * 3600) +  " secs")
  """

'''
def myMoonWeight():

    moon weight


    moonWeight = int(input("Pls enter weight: "))
    print("Yout weight on the moon are: " + str(moonWeight * 0.166) + " kg or moonKg")

'''

'''
def myMinutes2Hours():

    time conversion


    mins2Hours = int(input("Pls enter minutes: "))
    print("Is is: " + str(int(mins2Hours / 60)) + " hours and " + str(int(mins2Hours % 60)) + " minutes")



'''

"""
def myDegC2F():

    Convert Deg C to deg F

    degC = int(input("Pls enter your agedeg C convert to deg F: "))
    print(str(degC) + "C...Converts to: " + str(degC * 9 / 5 + 32) + " deg F")

"""

"""
def myWordBoost():

    repeat as wanted

    nums = int(input("repete this many times: "))
    st = input("what to repete? ")
    for st in range(nums):
        print(st)

 """



"""---------------------------------
def myRandGen():

    Generate 10 random in range

    import random
    minn = float(input("Random from "))
    maxx = float(input("random too"))
    randy = ''
    i = 0
    while i < 10:
        y = float(random.uniform(minn, maxx))
        randy = ', ' + str(y) + randy
        i += 1
    randy2 = randy[1:]
    print(randy2)

-------------------------------------"""



"""---------------------------------
def mySumAvg():

    -----


    summa = 0
    count = 0
    x = 0
    while x != 'done':
        x = float(x)
        summa = summa + x
        count += 1
        x = input("feed me:!! with a number. END is 'done': ")
    count -= 1

    print("The sum of " + str(count) + ' numbers is: ' + str(summa) + ' and the avg is ' + str(summa / count))



-------------------------------------"""

"""---------------------------------
def myP2G():

    convert points to a grade



    try:
        points = input('Enter points: ')
        points = float(points)
        if points > 1.0:
            print('To many points')
        elif points >= 0.9:
            print('Grade: A')
        elif points >= 0.8:
            print('Grade: B')
        elif points >= 0.7:
            print('Grade: C')
        elif points >= 0.6:
            print('Grade: D')
        elif points < 0.6:
            print('Grade: F')
    except ValueError:
        print('Bad score')

-------------------------------------"""


"""---------------------------------
def myCircleArea():
     circle area
    import math
    radius = float(input("set radius "))
    area = radius**2 * math.pi
    print("The area of a cirkle with radius: " + str(radius) + " is " + str(area))
-------------------------------------"""
"""---------------------------------
def myPyt():
    hptnusa
    import math
    leg1 = float(input("Leg1: "))
    leg2 = float(input("Leg2: "))
    hy = math.sqrt(leg1**2 + leg2**2)
    print("Hyppe: " + str(hy))
-------------------------------------"""



"""---------------------------------
def mySameSame():
    """  """
    first = input("First: ")

    while first != "done":
        after = input("Next: ")
        if after < first:
            print("Is less ")
            x = after
            after = first
            first = x
        elif after > first:
            print("Is more ")
            x = after
            after = first
            first = x
        else:
            print(" same--same ")

-------------------------------------"""
