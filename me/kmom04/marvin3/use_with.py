"""
Use with - as for reading and writing
With closes file automatically after the code in the statement has finished
"""

# read all lines into list
with open("test.txt") as fhand:
    all_lines = fhand.readlines()

# write line into file
with open("test.txt", "w") as fhand:
    fhand.write("This is a test.")
