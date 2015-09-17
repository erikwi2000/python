#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.

"""




from marvin import menu
#from marvin2 import myInventory
from marvin import myInventory
#from marvin2 import myGuestCheckin
from marvin import myGuestCheckin
#from marvin import myDia
from marvin import myQuotas
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
        elif choice == "16":
            myQuotas()
        elif choice == "17":
            output = myGuestCheckin()
            myInventory(output)
      #  elif choice == "17":
      #      myDia()


        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")


#print("wwfffffffffffffffffwwwwwww")
if __name__ == "__main__":
#    print("wwwwwwwwwwwwwwwwwwwww")
    main()
#======================================0


#from datetime import datetime
