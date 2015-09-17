#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
bfe8a224a603df022b875553616e610b generated for bjvi13 at 2015-09-12 07:28:24
"""

from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print("Ready to begin.")


"""
==========================================================================
Lab 3 - python


"""

"""
--------------------------------------------------------------------------
Section 1. List basics


"""

"""
Exercise 1.1

Concatenate the two lists [Berenger, fly] and [desk, bass]. Answer with
your list.

Write your code below and put the answer into the variable ANSWER.
"""

listOne = ['Berenger', 'fly']
listTwo = ['desk', 'bass']

listOneTwo = listOne + listTwo
#print(listOneTwo)




ANSWER = listOneTwo

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2

Use the list [flute, guitar, drums, piano, bass]. Add the words: 'icecream'
and 'money' as the second and third element. Answer with the modified list.

Write your code below and put the answer into the variable ANSWER.
"""

listThree = ['flute', 'guitar', 'drums', 'piano', 'bass']
listThree.insert(1, 'icecream')
listThree.insert(2, 'money')



ANSWER = listThree

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3

Use the list [flute, guitar, drums, piano, bass]. Replace the third word
with: 'potato'. Answer with the modified list.

Write your code below and put the answer into the variable ANSWER.
"""


listThree = ['flute', 'guitar', 'drums', 'piano', 'bass']
listThree[2] = 'potato'


ANSWER = listThree

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4

Sort the list [lion, tiger, ozelot, bobcat, cougar] in ascending
alphabetical order. Answer with the sorted list.

Write your code below and put the answer into the variable ANSWER.
"""



input1 = 'lion, tiger, ozelot, bobcat, cougar'
listThree = input1.split(', ')
listThree.sort()
#print(listThree)

ANSWER = listThree

#ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5

Use the list from the last excercise ([lion, tiger, ozelot, bobcat,
cougar]) and sort it in decending alphabetical order. Answer with the
sorted list.

Write your code below and put the answer into the variable ANSWER.
"""


input1 = 'lion, tiger, ozelot, bobcat, cougar'
listThree = input1.split(', ')
listThree.sort(reverse=True)
#print(listThree)

ANSWER = listThree

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6

Use pop() to get the second and the last element in the list: [flute,
guitar, drums, piano, bass]. Answer with the popped elements in a new list.

Write your code below and put the answer into the variable ANSWER.
"""

input1 = 'flute, guitar, drums, piano, bass'
listThree = input1.split(', ')

newList = [listThree.pop(1)]
newList = newList + [listThree.pop(-1)]



ANSWER = newList

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7

Use remove() to delete the word: 'tiger' from the list: [lion, tiger,
ozelot, bobcat, cougar]. Answer with the modified list.

Write your code below and put the answer into the variable ANSWER.
"""


input1 = 'lion, tiger, ozelot, bobcat, cougar'
listThree = input1.split(', ')
listThree.remove("tiger")



ANSWER = listThree

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Built-in list functions

Some basic built-in functions
"""

"""
Exercise 2.1

Use a built-in function to sum all numbers in the list: [567, 23, 12, 36,
7]. Answer with the result as an integer.

Write your code below and put the answer into the variable ANSWER.
"""

input1 = (567, 23, 12, 36, 7)
sum1 = sum(input1)



ANSWER = sum1

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2

Use built-in functions, such as 'sum' and 'len' to get the average value of
the list: [123, 4, 125, 69, 155]. Answer with the result as a float with at
most one decimal.

Write your code below and put the answer into the variable ANSWER.
"""
import statistics
input1 = [123, 4, 125, 69, 155]
mean1 = statistics.mean(input1)


ANSWER = mean1

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3

Use a built-in function to get the lowest number in the list: [567, 23, 12,
36, 7]. Answer with the result as a integer.

Write your code below and put the answer into the variable ANSWER.
"""


input1 = [567, 23, 12, 36, 7]
min1 = min(input1)


ANSWER = min1




# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4

Use the built-in functions split() and join() to fix this string:
'The?snow?is?falling' into a real sentence, (without '?'). Answer with the
fixed string.

Write your code below and put the answer into the variable ANSWER.
"""

str1 = 'The?snow?is?falling'
input1 = str1.split('?')
s = " "
input1 = s.join(input1)
#input1 = input1 + ' outside.'


ANSWER = input1

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5

Use the string: 'Whenever I feel the need to exercise, I lie down until it
goes away.' and split it with the delimiter ' ' (space). Answer with the
element at index 12.

Write your code below and put the answer into the variable ANSWER.
"""


str1 = 'Whenever I feel the need to exercise, I lie down until it goes away.'
input1 = str1.split(' ')

ANSWER = input1[12]

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6

Use slice on the list [reggae, rock, blues, jazz, opera] and replace the
second and third element with 'book, candle'. Answer with the modified
list.

Write your code below and put the answer into the variable ANSWER.
"""

input1 = 'reggae, rock, blues, jazz, opera'
input2 = input1.split(', ')
print(input2)
input2[1] = 'book'
input2[2] = 'candle'

ANSWER = input2

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))

"""
Exercise 2.7

Use slice on the list [reggae, rock, blues, jazz, opera] and replace the
last two elements with 'book, candle'. Answer with the modified list.

Write your code below and put the answer into the variable ANSWER.
"""


input1 = 'reggae, rock, blues, jazz, opera'
input2 = input1.split(', ')
#print(input2)
input2[-2] = 'book'
input2[-1] = 'candle'

ANSWER = input2

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.7", ANSWER, False))

"""
Exercise 2.8

Use slice on the list [reggae, rock, blues, jazz, opera] and insert the
words 'book, candle' after the third element. Answer with the modified
list.

Write your code below and put the answer into the variable ANSWER.
"""

input1 = 'reggae, rock, blues, jazz, opera'
input2 = input1.split(', ')
#print(input2)
input2.insert(3, 'candle')
input2.insert(3, 'book')

ANSWER = input2





# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.8", ANSWER, False))

"""
Exercise 2.9

Use 'del' on the list [dvd, mp3, blu-ray, vhs, cd] and delete the first
element. Answer with the modified list.

Write your code below and put the answer into the variable ANSWER.
"""
input1 = 'dvd, mp3, blu-ray, vhs, cd'
input2 = input1.split(', ')
#print(input2)
del input2[0]


ANSWER = input2

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.9", ANSWER, False))

"""
Exercise 2.10

Use 'del' on the list [dvd, mp3, blu-ray, vhs, cd] and delete the second
and third element. Answer with the modified list.

Write your code below and put the answer into the variable ANSWER.
"""


input1 = 'dvd, mp3, blu-ray, vhs, cd'
input2 = input1.split(', ')
#print(input2)
del input2[1]
del input2[1]
#print(input2)

ANSWER = input2



# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.10", ANSWER, False))

"""
Exercise 2.11

Assign the list [b, a, e, d, c] to a variable called 'list1'. Assign the
list again, but to another variable called 'list2'. Answer with the result
of 'list1 is list2'.

Write your code below and put the answer into the variable ANSWER.
"""
list11 = 'b, a, e, d, c'
list1 = list11.split(', ')

list22 = 'b, a, e, d, c'
list2 = list22.split(', ')


ANSWER = list1 is list2



# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.11", ANSWER, True))

"""
Exercise 2.12

Use your lists from the last exercise. Assign 'list1' to another variable
called 'list3' like this: list3 = list1. Answer with the result of 'list1
is list3'.

Write your code below and put the answer into the variable ANSWER.
"""

list11 = 'b, a, e, d, c'
list1 = list11.split(', ')
list3 = list1
#list22 = 'b, a, e, d, c'
#list2 = list22.split(', ')




ANSWER = list1 is list3

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.12", ANSWER, False))

"""
Exercise 2.13

Use your lists from the last exercise. Change the first element in 'list1'
to 'y'. Answer with 'list3'.

Write your code below and put the answer into the variable ANSWER.
"""

list11 = 'b, a, e, d, c'
list1 = list11.split(', ')
list3 = list1
list1[0] = 'y'




ANSWER = list3

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.13", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 3. Lists as arguments

Some excercises with passing lists as arguments to a function.
"""

"""
Exercise 3.1

Create a function that returns the list passed as argument sorted in
numerical and ascending order. Also multiply all values with 10. Use the
list: [567, 23, 12, 36, 7], and the built-in method 'sort()'. Answer with
the sorted list.

Write your code below and put the answer into the variable ANSWER.
"""

list1 = '567, 23, 12, 36, 7'
list1 = list1.split(', ')
list1 = [int(x) * 10 for x in list1]
list1.sort()


ANSWER = list1

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.1", ANSWER, True))

"""
Exercise 3.2

Create a function that takes the list: [123, 4, 125, 69, 155] as argument.
The function should multiply all even numbers by 3 and add 8 to all odd
numbers. Answer with the modified list sorted in numerical order,
descending.

Write your code below and put the answer into the variable ANSWER.
"""

inandoutput = '123, 4, 125, 69, 155'
inandoutput = inandoutput.split(', ')



def listor(insidefunclistor):
    """ Funktion """
    i = 0
    while i < len(insidefunclistor):
        #x = int(insidefunclistor[i]) % 2
        if int(insidefunclistor[i]) % 2 == 0:
            insidefunclistor[i] = int(insidefunclistor[i]) * 3
        else:
            insidefunclistor[i] = int(insidefunclistor[i]) + 8
        i += 1
    return insidefunclistor

listor(inandoutput)
inandoutput.sort(reverse=True)





ANSWER = inandoutput

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.2", ANSWER, False))


dbwebb.exitWithSummary()
