#!/usr/bin/python
"""Creating your own functions is easy, and fun.

Joseph Kern
"""

    # Think of a function as a self-contained set of code.
    # First we need to create a function, we'll call it MathFunction

def MathFunction(numberX,numberY):
    """Functions can use docstrings too! Use these for documentation"""
    NewNumber = numberX + numberY
    return NewNumber

    # Okay so we created a new function with 'def'
    # Added a """docstring"""
    # At the end of the line there is a set of '( )';
    # The two variables between the '( )' are called arguments
    # And finally we 'return' the value of NewNumber

    # Now we need to call the function and pass it an argument
value = MathFunction(3,2)
    # 3 now equals numberX and 2 now equals numberY
    # The function does its work and returns the value
print value


