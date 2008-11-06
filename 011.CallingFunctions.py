#!/usr/bin/python
"""How to call a function.

Joseph Kern
"""

# The most basic function is 'print'
print "\nHello\n"
# print is the function, and "Hello" is the argument

# There are many other functions too.
# one of the simplest to use is called raw_input

UserInput = raw_input("What is your name? ")
print "\nHello %s\n" % UserInput
