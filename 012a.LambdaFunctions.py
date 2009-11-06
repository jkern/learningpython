#!/usr/bin/python
""" Functions can be named (as in the previous example) or unnamed. An unnamed function is called a lambda. At first it may seem odd that we need to name an un-named function. Think of lambdas as a noun, rather than a proper noun. A generic function. """

# Getting started let's create a simple squaring function

square = lambda x: x * x

# So we've created a squaring function, that will take the input x and return the square of x.
# the function lambda, creates a function without a def statement. This is the beginning of functional programming.

# Functions can be created in this manner, and like all functions can be used as the input for other functions.

print "This is the square of 12 : %d" % square(12)
print "This is the square of the square of 12 : %d" % square(square(12))

# lambdas are limited by design in python, but there will be certain times they are useful. You will know when the time comes.


