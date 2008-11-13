#!/usr/bin/python
"""Slicing through variables and data structures

Joseph Kern
"""

# Many Types have bult-in methods. In this case let's look at slicing. 

MyString = "Hello World!"
MyList = ["Hello","World","!"]
MyTuple = "Hello","World","!"
MyDict = {1 : "Hello", 2 : "World", 3 : "!"}

# A slice allows us to slice through certain types of variables.
# For example let's imagine that we just need the first letter of the string, MyString

print "MyString 0 	", MyString[0]

# In this case 0 is the FIRST position of the string. 
# What if we need to get the LAST letter from the string?

print "MyString -1 	", MyString[-1]

# Since 0 == to the FIRST position -1 == to the LAST position
# IMHO -0 might be more descriptive to the LAST position than -1

# We can have slices of Lists also. 

print "MyList 		", MyList[0]

# Although in this case every Item in the List has its own position.

# Tuples work the same way as Lists.

print "MyTuple 	", MyTuple[0]

# Dictionaries cannot be sliced. 
