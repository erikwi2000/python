#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""                                               
7b8169ba57c7463f4c482a06dfb23df0 generated for bjvi13 at 2015-09-02 18:33:20 
"""

from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print("Ready to begin.")


"""
==========================================================================
Lab 1 - python 
 
If you need to peek at examples or just want to know more, take a look at
the page: https://docs.python.org/3/library/index.html. Here you will find
everything this lab will go through and much more. 
"""

"""
--------------------------------------------------------------------------
Section 1. Integers, strings, floats and basic arithmetics 
 
The foundation of numbers and basic arithmetic. 
"""

"""
Exercise 1.1 
 
Create a variable called 'numOne' and give it the value 59. Create another
variable called 'numTwo' and give it the value 78. Create a third variable
called 'result' and assign to it the sum of the first two variables. Answer
with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
numOne = 59
numTwo = 78
result = numOne + numTwo
#print("Result Exercise 1.1:  ", result)

ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2 
 
Create a variable called 'numThree' and give it the value 48. Create
another variable called 'numFour' and give it the value 55. Subtract
'numThree' from 'numFour' and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
numThree = 48
numFour = 55
result = numFour - numThree 
#print("Result Exercise 1.2:  ", result)


ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3 
 
Find out the product of 'numOne' and 'numThree' and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
numOne = 59
numThree = 48
result = numOne * numThree 
#print("Result Exercise 1.3:  ", result)

ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4 
 
Divide 30 with 5 and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""


result = 30 / 5 
#print("Result Exercise 1.4:  ", result)


ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5 
 
Create a variable called 'floatOne' and give it the value 14.5. Create
another variable called 'floatTwo' and give it the value 17.59. Sum the two
values and answer with the result, rounded to 2 decimals. 

Write your code below and put the answer into the variable ANSWER.
"""

floatOne = 14.5
floatTwo = 17.59
result = round(floatOne + floatTwo, 2)


ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6 
 
Subtract 'floatTwo' from 'floatOne' and answer with the result. Round to 2
decimals. 

Write your code below and put the answer into the variable ANSWER.
"""

floatOne = 14.5
floatTwo = 17.59
result = round(floatOne-floatTwo, 2)


ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7 
 
Answer with the product of 'floatOne' and 'floatTwo', rounded to 4
decimals. 

Write your code below and put the answer into the variable ANSWER.
"""

floatOne = 14.5
floatTwo = 17.59
result = round(floatOne*floatTwo, 4)


ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8 
 
Create three variables: 'n1' = 284, 'n2' = 404 and 'n3' = 31. Sum up 'n1'
and 'n2'. Subtract 'n3' and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""

n1 = 284
n2 = 404
n3 = 31
result = n1 + n2 - n3
#print("Result Exercise 1.8:  ", result)

ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9 
 
Answer with the result of 544 modulo (%) 27. 

Write your code below and put the answer into the variable ANSWER.
"""

result = 544 % 27
#print("Result Exercise 1.9:  ", result)

ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10 
 
Add the word: 'program' to the word: 'restaurant' and answer with the
result. 

Write your code below and put the answer into the variable ANSWER.
"""

result = 'restaurant' + 'program'


ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Conditions, exceptions, booleans, if, else and elif 
 
 
"""

"""
Exercise 2.1 
 
Answer with the boolean value of: 189 is less than 360. 

Write your code below and put the answer into the variable ANSWER.
"""

#print("Result Exercise 2.1:  ", 189 < 360)

result = 189 < 360
#result = bool([466 < 373])

ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2 
 
Answer with the boolean value of: 373 is larger than 466. 

Write your code below and put the answer into the variable ANSWER.
"""


result = 373 > 466
 
ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3 
 
Answer with the boolean value of: 189 == 373. 

Write your code below and put the answer into the variable ANSWER.
"""

result = 189 == 373

ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4 
 
Create three variables representing dice values: 'd1' = 4, 'd2' = 3 and
'd3' = 5. Sum them up and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""

d1 = 4
d2 = 3
d3 = 5
result = d1 + d2 + d3



ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5 
 
Create an if statement to see if the total value of your dices is 11 or
higher. If that is the case, answer with the string: 'big', else answer
with the string: 'nothing'.  

Write your code below and put the answer into the variable ANSWER.
"""

if (d1+d2+d3) >= 11:
    result = 'big'
else:
    result = 'nothing'



ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6 
 
Create an elif statement that checks your total dice value. The checks and
results should be: three of the same value = 'triple', total of 11 or
higher = 'big', total of 10 or lower = 'small'. If you get a triple you
should not make more checks. 

Write your code below and put the answer into the variable ANSWER.
"""
if d1 == d2 == d3:
    result = 'triple'
elif (d1+d2+d3) >= 11:
    result = 'big'
else:
    result = 'nothing'




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 3. Built-in functions 
 
Some useful built-in functions 
"""

"""
Exercise 3.1 
 
Use max() to find the largest number in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""
result = max(6, 8, 95, 2, 12, 152, 4, 78, 621, 45)




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.1", ANSWER, False))

"""
Exercise 3.2 
 
Use min() to find the smallest number in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""


result = min(6, 8, 95, 2, 12, 152, 4, 78, 621, 45)


ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.2", ANSWER, False))

"""
Exercise 3.3 
 
Use len() to find the number of letters in the word: screen. Answer with
the result. 

Write your code below and put the answer into the variable ANSWER.
"""


result = len('screen')



ANSWER = result
# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.3", ANSWER, False))

"""
Exercise 3.4 
 
Convert the number 784 to a string and add it to the word 'screen'. Answer
with the result. 

Write your code below and put the answer into the variable ANSWER.
"""

result = 'screen' + str(784) 



ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.4", ANSWER, False))

"""
Exercise 3.5 
 
Convert the number 567.16 to an integer and then to a string. Add it to the
beginning of the word: 'screen'. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""
result = str(int(567.16)) + 'screen'




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.5", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 4. Functions 
 
Basic functions 
"""

"""
Exercise 4.1 
 
Create a function called 'prodNr' that takes two arguments, 99 and 14. The
function should return the product of the numbers. Answer with a call to
the function.  

Write your code below and put the answer into the variable ANSWER.
"""
x = 99
y = 14


result = x * y


ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("4.1", ANSWER, False))

"""
Exercise 4.2 
 
Create a function called 'funnyWord' that takes one argument and adds it to
the string ' is a funny word'. If the argument is 'water', the function
should return: 'water is a funny word'. Use the argument 'beach' and answer
with a call to the function. 

Write your code below and put the answer into the variable ANSWER.
"""
def funnyWorld(xxx):
    """ blaj """
    yy = xxx + " is a funny word"
    return yy
   
result = funnyWorld('beach')


ANSWER = result
#print(result)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("4.2", ANSWER, True))

"""
Exercise 4.3 
 
Create a function called 'inRange' that takes one argument. The function
should return 'true' if the argument is higher than 50 and lower than 100.
If the number is out of range, the function should return 'false'. The
return type should be boolean. Use the argument 57 and answer with a call
to the function. 

Write your code below and put the answer into the variable ANSWER.
"""
def inRange(xx):
    """ bkllii """
    if xx > 50 and xx < 100:
        return True
    else:
        return False


result = inRange(57)

ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("4.3", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 5. Iteration and loops 
 
For-loops and while-loops.  
"""

"""
Exercise 5.1 
 
Create a while-loop that adds 8 to the number 56, 37 times. Answer with the
result.  

Write your code below and put the answer into the variable ANSWER.
"""

x = 0
y = 56
while x < 37:
    x += 1
    y += 8
result = y



ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.1", ANSWER, False))

"""
Exercise 5.2 
 
Create a while-loop that subtracts 4 from 21, 50 times. Answer with the
result.  

Write your code below and put the answer into the variable ANSWER.
"""

x = 0
y = 21
while x < 50:
    x += 1
    y -= 4
result = y



ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.2", ANSWER, False))

"""
Exercise 5.3 
 
Create a for-loop that counts the number of elements in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""
dd = (6, 8, 95, 2, 12, 152, 4, 78, 621, 45)
count = 0
for i in  dd:
    count += 1
result = count




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.3", ANSWER, False))

"""
Exercise 5.4 
 
Create a for-loop that sums up the numbers in the serie:
67,2,12,28,128,15,90,4,579,450. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""

dd = (67, 2, 12, 28, 128, 15, 90, 4, 579, 450)
summ = 0
for i in  dd:
    summ += i
result = summ



ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.4", ANSWER, False))

"""
Exercise 5.5 
 
Create a for-loop that finds the largest number in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""
dd = (6, 8, 95, 2, 12, 152, 4, 78, 621, 45)
check = dd[0]


for i in  dd:
    if i > check:
        check = i
result = check



ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.5", ANSWER, False))

"""
Exercise 5.6 
 
Create a for-loop that goes through the numbers:
67,2,12,28,128,15,90,4,579,450. If the current number is even, you should
add it to a variable and if the current number is odd, you should subtract
it from the variable. Answer with the final result.  

Write your code below and put the answer into the variable ANSWER.
"""

dd = (67, 2, 12, 28, 128, 15, 90, 4, 579, 450)
summ = 0
for i in  dd:
    if i % 2 == 0:
        summ += i
    else:
        summ -= i
result = summ



ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.6", ANSWER, False))


dbwebb.exitWithSummary()
