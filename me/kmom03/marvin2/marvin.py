#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.

"""


def meImagex():
    """
    Store my ascii image in a separat variabel as a raw string
    """
    return r"""
          ,     ,
         (\____/)
          (_oo_)
            (O)
          __||__    \)
       []/______\[] /
       / \______/ \/
      /    /__\
     (\   /____\
    """
def meImageBIG():
    """
    store
    """
    return r"""
              ____               ____
             /,,,,\_____________/,,,,\
            |,(  )/,,,,,,,,,,,,,\(  ),|
             \__,,,,___,,,,,___,,,,__/
               /,,,/(')\,,,/(')\,,,\
              |,,,,___ _____ ___,,,,|
              |,,,/   \\o_o//   \,,,|
              |,,|       |       |,,|
              |,,|   \__/|\__/   |,,|
               \,,\     \_/     /,,/
                \__\___________/__/
  ________________/,,,,,,,,,,,,,\________________
 / \,,,,,,,,,,,,,,,,___________,,,,,,,,,,,,,,,,/ \
(   ),,,,,,,,,,,,,,/           \,,,,,,,,,,,,,,(   )
 \_/____________,,/             \,,____________\_/
               /,/    *SWEET*    \,\
              |,|                 |,|
              |,|     *DREAMS*    |,|
              |,|                 |'|
              |,|        O        |,|
               \,\               /,/
               /,,\_____________/,,\
              /,,,,,,,,,,,,,,,,,,,,,\
             /,,,,,,,,_______,,,,,,,,\
            /,,,,,,,,/       \,,,,,,,,\
           /,,,,,,, /         \,,,,,,,,\
          /_____,,,/           \,,,_____\
         //     \,/             \,/     \\
         \\_____//               \\_____//                              """
def meImage():
    """
    store
    """
    return r"""
              ____               ____
             /,,,,\_____________/,,,,\
            |,(  )/,,,,,,,,,,,,,\(  ),|
             \__,,,,___,,,,,___,,,,__/
               /,,,/(')\,,,/(')\,,,\
              |,,,,___ _____ ___,,,,|
              |,,,/   \\o_o//   \,,,|
              |,,|       |       |,,|
              |,,|   \__/|\__/   |,,|
               \,,\     \_/     /,,/
                \__\___________/__/
                             """
def menu():
    """
    Display the menu with the options that Marvin can do.
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(meImage())
    print("Hi, I'm Bjorn. Been there done that. \nWhat can U do you for mee?")
    print("1) Present yourself to Björn.")
    print("2) Inform Bjorn of your age.")
    print("3) Your wheight on the moon.")
    print("4) Minutes to hours.")
    print("5) Convert from C to F.")
    print("6) Repeat something a number of times")
    print("7) Ten random numbers in a range .. . .")
    print("8) Sum and avargae when you quit")
    print("9) Points to grades 'learning curve'")
    print("10) Circle area from radius  ")
    print("11) a triangle long leg  hypotenuse")
    print("12) compare two numbers in a logrow ")
    print("13) Guess the number ")
    print("14) Talk2Marvin ")
    print("15) Randomize ")
    print("q) Quit.")


def myNameIs():
    """
    Read the users name and say hello to Marvin.
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")

#from datetime import datetime
def myAgeIs():
    """
    Read user bd
    """

    age = input("Pls enter your age: ")
    try:
        age = int(age)
    except ValueError:
        print("Try to enter a number please")
    #    main()
      #  quit()
    print("Your age is more than: " +  str(age * 365 * 24 * 3600) +  " secs")


def myMoonWeight():
    '''moon weight
    '''
    moonWeight = int(input("Pls enter weight: "))
    print("Yout weight on the moon are: " + str(moonWeight * 0.166) + " kg or moonKg")

def myMinutes2Hours():
    '''
    time conversion
    '''

    mins2Hours = int(input("Pls enter minutes: "))
    print("Is is: " + str(int(mins2Hours / 60)) + " hours and " + str(int(mins2Hours % 60)) + " minutes")


def myDegC2F():
    """
    Convert Deg C to deg F
    """
    degC = int(input("Pls enter your agedeg C convert to deg F: "))
    print(str(degC) + "C...Converts to: " + str(degC * 9 / 5 + 32) + " deg F")

def myWordBoost():
    """
    repeat as wanted
    """
    nums = int(input("repete this many times: "))
    st = input("what to repete? ")
    i = 0
    while i < nums:
        i += 1
        print(st)



def myRandGen():
    """
    Generate 10 random in range
    """
    import random
    minn = float(input("Random from "))
    maxx = float(input("random too  "))
    randy = ''
    i = 0
    while i < 10:
        y = float(random.uniform(minn, maxx))
        randy = ', \n' + str(y) + randy
        i += 1
        #print("check01")

   # print(randy)
    randy2 = randy[1:]
    print(randy2)
#    print("check02")
#    print("check03")
#
def mySumAvg():
    """
    -----
    """

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




def myP2G():
    """
    convert points to a grade
    """


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

def myCircleArea():
    """ circle area """
    import math
    radius = float(input("set radius "))
    area = radius**2 * math.pi
    print("The area of a cirkle with radius: " + str(radius) + " is " + str(area))
def myPyt():
    """ hptnusa """
    import math
    leg1 = float(input("Leg1: "))
    leg2 = float(input("Leg2: "))
    hy = math.sqrt(leg1**2 + leg2**2)
    print("Hyppe: " + str(hy))

def mySameSame():
    """ ss """
    first = input("First: ")

    while first != "done":
        after = input("Next: ")
        if after < first:
            print("Is less ")
            x = after
            after = first
            first = x
           # print(after, '  ' , first)
        elif after > first:
            print("Is more ")
            x = after
            after = first
            first = x
            #print(after, '  ' , first)
        else:
            print(" same--same ")

def guessNumber():
    """ guess a number in a range """
    # This is a guess the number game.
    import random

    guessesTaken = 0

    print('Hello! What is your name?')
    myName = input()

    number = random.randint(1, 100)
    print('Well, ' + myName + ', I am thinking of a number between 1 and 100.')

    while guessesTaken < 6:
        print('Take a guess.') # There are four spaces in front of print.
        guess = input()
        guess = int(guess)

        guessesTaken = guessesTaken + 1

        if guess < number:
            print('Your guess is too low.') # There are eight spaces in front of print.

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            break

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

    if guess != number:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number)

def myDate():
    """ Date feeling ??? """
#    import time
    import datetime
    import random

    moods = ["happy", "sad", "depressed",
             "angry", "annoyed", "bored",
             "confused", "excited", "lonely", "undefined"]
    """
    smilies = [":)", ":(", ":D",
                ":/", ":|", ":'(",
                ":O", ":@", ":P", ":3"]
    """
    #smiley = random.choice(smilies)

    yy = datetime.datetime.now()
    stre = str(yy)
    temp01 = stre.split('.')
    temp01 = str(temp01[0])
    timeDate = temp01.split(' ')


    lines = [line.rstrip('\n') for line in open('filen.txt')]

    mood = random.choice(moods)
    xxx = moods.index(mood)
    yyy = len(mood)

    flyt = round((3.1416 * xxx / yyy), 3)

    print(lines[0] +  ' '  + timeDate[0] +  lines[1]\
          + ' '  +  timeDate[1] + lines[2]\
         + ' ' + mood  + lines[3] + ' ' + \
        str(xxx + 1) + ' '  + lines[4] +\
        ' ' + str(flyt))


def myHoppsan():
    """ kaos """
    import random

    snurr = input("Give me a word to randomize!  ")
#    lengt = len(snurr)
    print("Starting with:   ", snurr)
    snurr = ''.join(random.sample(snurr, len(snurr)))
    print("Retards to       ", str(snurr))

def myQuotas():
    """ Some Quotas """

    print("Hello Quota")
