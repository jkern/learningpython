#!/usr/bin/python
"""
A simple program that demonstrates basic file operations
"""

string = "Let's write this to a file!"
# Files are a built in type in python. Which is awesome IMO

f = open('tmp.txt', 'w')
# f will hold the method open 
# 'tmp.txt' is the file we will be writing to.
# and the 'w' is the mode in which we open the file
# 'w' = "write'
# 'r' = read 
# 'a' = append
# The difference between 'w' and 'a' is very important:
# 'w' will overwrite ALL data in the file with the new
# 'a' will add the data to the end of the file

f.write(string)
# Now let's write to the file. Sweet two lines to file IO . . .
