#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
1a780006135d8b7a0c1e5a60d7d9f34d generated for bjvi13 at 2015-09-07 10:42:29
"""

from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print("Ready to begin.")


"""
==========================================================================
Lab 2 - python

Strings and files
"""

"""
--------------------------------------------------------------------------
Section 1. Strings

The basics of strings
"""

"""
Exercise 1.1

Assign the word: 'milk' to a variable and put your variable as the answer.

Write your code below and put the answer into the variable ANSWER.
"""

ex1String = 'milk'



ANSWER = ex1String

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2

Assign the word 'milk' to a variable. Create another variable where you put
the first and the last letter in the word. Answer with the second variable.

Write your code below and put the answer into the variable ANSWER.
"""

ex1String = 'milk'
milk2 = ex1String[0] + ex1String[-1]


ANSWER = milk2

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3

Assign the word: banana to a variable. Answer with the length of the word
as an integer.

Write your code below and put the answer into the variable ANSWER.
"""
fruit = "banana"
lenght = int(len(fruit))



ANSWER = lenght

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4

Use the 'in-operator' to see if the word: 'banana' contains the letter 'a'.
Answer with a boolean result.

Write your code below and put the answer into the variable ANSWER.
"""

fruit = "banana"
if 'a' in fruit:
    xx = True



ANSWER = xx

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5

Make all the letters in the word 'banana' capitalized. Answer with the
capitalized word.

Write your code below and put the answer into the variable ANSWER.
"""

fruit = "banana"
oldfruit = fruit.upper()



ANSWER = oldfruit

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6

Use the built-in function 'startswith()' to see if the word 'potato' starts
with the letter 'p'. Answer with the boolean value.

Write your code below and put the answer into the variable ANSWER.
"""
fruit = "potato"
xx = fruit.startswith('p')


ANSWER = xx

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7

Assign the words: 'helicopter' and 'melon' to two different variables.
Create a function and pass the two words as arguments to it. Your function
should return them as a single word. Answer with the result.

Write your code below and put the answer into the variable ANSWER.
"""



def fly(aa, bb):
    """ drink """
    return aa + bb

h = 'helicopter'
m = 'melon'
xx = fly(h, m)




ANSWER = xx

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8

Create a function and pass the word: 'milk' to it. Your function should
return the sentence: 'This word was: milk'. Answer with the result.

Write your code below and put the answer into the variable ANSWER.
"""
def drink(aaa):
    """ drink """
    if aaa == "milk":
        return "This word was: milk"
wtd = "milk"
xx = drink(wtd)


ANSWER = xx

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9

Create a function and pass the word: 'melon' to it. Your function should
return the string 'yes' if the word is longer than 5 characters. Else
return 'no'. Answer with the result.

Write your code below and put the answer into the variable ANSWER.
"""
def howlong(aaaa):
    """ drink """
    if len(aaaa) > 5:
        return 'yes'
    else:
        return 'no'


aaaaa = howlong('melon')

ANSWER = aaaaa

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10

Create a function and pass the word: 'banana' to it. Your function should
return a string with the word backwards. Answer with the result.

Write your code below and put the answer into the variable ANSWER.
"""

def around(a):
    """ around """
    return a[::-1]

ab = around('banana')

ANSWER = ab

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
Exercise 1.11

Create a function and pass the word: 'helicopter' to it. Your function
should exclude the first and the last letter of the word and return it.
Answer with the result.

Write your code below and put the answer into the variable ANSWER.
"""

def itm(a):
    """ around """
    return a[1:-1]
b = itm('helicopter')


ANSWER = b

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.11", ANSWER, False))

"""
Exercise 1.12

Use str.format() to print out: 'My 'string' has 'integer' 'string''. Use
the values: 'brother', '2' and 'dogs'. Answer with the result.

Write your code below and put the answer into the variable ANSWER.
"""
b = 'brother'
dc = 2
dgs = 'dogs'

x = '{0} {1} {2} {3} {4}'.format('My', b, 'has', dc, 'dogs')



ANSWER = x

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.12", ANSWER, True))

"""
Exercise 1.13

Use 'find' and 'slice' on the string: '196.98.2.54 : (tree), window' to get
the word inside the parenthesis. Answer with the word as a string.

Write your code below and put the answer into the variable ANSWER.
"""

str1 = '196.98.2.54 : (tree), window'
str2 = "("
str3 = ')'
start = str1.find(str2) + 1
stop = str1.find(str3)
xx = str1[start:stop]




ANSWER = xx
# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.13", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Files

This section uses the text file: 'httpd-access.txt'
"""

"""
Exercise 2.1

Open the file and count the number of times a line starts with '81'. Answer
with the result as an integer.

Write your code below and put the answer into the variable ANSWER.
"""

inputFile = open('httpd-access.txt', 'r+')
count = 0
for cheese in inputFile:
    if cheese.startswith('81'):
        count += 1
#    print(cheese)

#print("Count: ", count)

ANSWER = count

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2

Find out the last 4 digits on line 821 in the file. Answer with the result
as an integer.

Write your code below and put the answer into the variable ANSWER.
"""

inputFile = open('httpd-access.txt', 'r+')

lines = inputFile.readlines()
xx = lines[820]
yy = int(xx[-5:-1])
inputFile.close()


ANSWER = yy

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3

Find out which of the ip adresses 81.226.253.26 and 95.19.133.73 that has
the highest amount of entries. Answer with the result as an integer.

Write your code below and put the answer into the variable ANSWER.
"""

inputFile = open('httpd-access.txt', 'r+')
count = 0
count2 = 0
for cheese in inputFile:
    xx = cheese.split(' ')
    strdd = xx[0:1]
#    print(strdd)
    strdd = ''.join(xx[0:1])
    if strdd == '81.226.253.26':
        count += 1
    if strdd == '95.19.133.73':
        count2 += 1
top = max(count, count2)



ANSWER = top

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4

Count the number of periods (.) there are in the file. Use the built-in
function count() on the file after you have converted it to a string.
Answer with the result as an integer.

Write your code below and put the answer into the variable ANSWER.
"""

inputFile = open('httpd-access.txt', 'r+')
inp = inputFile.read()
yy = inp.count('.')



ANSWER = yy

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5

Find the characters on line 637 from index 65 to index 75. Make sure that
the character at index 75 also gets included. Answer with the piece of
string you found.

Write your code below and put the answer into the variable ANSWER.
"""


inputFile = open('httpd-access.txt', 'r+')

lines = inputFile.readlines()

xx = lines[636]
yy = xx[65:76]





ANSWER = yy

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6

Find the last element on each line and sum all that are even numbers.
Answer with the result as an integer.

Write your code below and put the answer into the variable ANSWER.
"""


""" test """
inputFile = open('httpd-access.txt', 'r+')
count = 0
for cheese in inputFile:
    xx = cheese.split()
    zz = len(xx)
    strdd = ''.join(xx[zz-1:])
    if strdd != '-':
        pp = int(strdd)
        pp_string = str(pp)
      #  print(pp_string[:2])
       # print(pp_string[-1:])
        strss = int(pp_string[-1:])
    if strss % 2 == 0:
        count = count + strss


ANSWER = count


# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, True))


dbwebb.exitWithSummary()
