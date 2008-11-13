#!/usr/bin/python
"""Using the built-in methods to manipulate types.

Joseph Kern
"""

# The only way to call a method, is to understand object oriented programming concepts.
# Previously we covered functions. Objects can be considered groups of functions. 
# An Object contains a series of functions. In programming terms, an Object is called a Class.
# Certain Classes, contain certain functions.
# If a function is a reusable, and independent grouping of code. A Class is a group of goupings.

# We will use the List data structure as an example. A List is not an ordinary variable.
# Its actually an object in disguse.

MyList = ["Hello","World","!"]

# Here we have created a new Object called MyList. Python knows that this is a builtin object
# called a list (Don't worry about how, it just does). This object contains three variables. 
# In this case it's three strings.

# Our first method 'count' will call into the Object MyList and find the fuction count
# Specifically count will count the number of times an 'argument' is found in the Object MyList

print MyList.count("Hello"), MyList.count("World")

# Since Lists are mutable (changable), we can insert data into the list anywhere we want

MyList.insert(1, ",")
print MyList

# The insert method takes two arguments:
# 	The position
#	The value to insert

# Next let's call the 'append' method and add some data onto the end of the Object MyList

MyList.append("!")

# append takes one argument:
#	The value to insert

print MyList

# There are other mehtods that can be used with lists specifically:
#	reverse
#	sort
#	remove
#	Plus many more, be sure to check the python dovumentation for the rest.

