#!/usr/bin/env python3
"""
Example of how to read the content of a file into a list
"""

# the name of the file
filename = "test.txt"

# with - as for reading a file automatically closes it after reading is done
with open(filename) as filehandle:
    line = filehandle.readline()  #1
# print the line read from the file
print("items in invertory: ", line)
line = line.rstrip('\n') #1B

# split the line into a list on the comma ","
items_as_list = line.split(",") #2
# print what the list looks like
print("splitted (list) ", items_as_list)
numOfItemsInList = len(items_as_list)
#***print("lenght ", xx)
if numOfItemsInList == 4:
    print("Hi there you are already on maximun pls do not att items")
elif numOfItemsInList > 4:
    print("UR naughty pls remove something")


#crap = input(
#print(items_as_list.index('cup'))


# add item to the list
items_as_list.append("cup")
# print what the list looks like after change
print("added thing ", items_as_list)


# join the list into a string with a comma ","" between every item
list_as_str = ",".join(items_as_list) #3
# show what the string looks like after join
print("string again ", list_as_str)


# write the line to the file
with open(filename, "w") as filehandle:
    filehandle.write(list_as_str)
