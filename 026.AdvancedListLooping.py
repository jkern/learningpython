#!/usr/bin/python
"""Using the built-in methods to manipulate types.

Joseph Kern
"""
# The importstatement is probably the most import[ant] staement that you can use
# importing allows us to resue our code. Or, even better, use other peoples code.
import string

# import statements should be one to a line, and only import the things that you need. 
# In the above example I have imported the string "module" (some langauges call these libraries)
# By importing the module called string, I have imported a large amount of very cool methods for strings
# The mehtod that we will be using is split() [see line 20]
# Remeber modules are nothing fancy, they are mostly just other bits of python code
# Put into the right directory, and made avalible to users. Import just loads the code into 
# The current program.

# Here is an advanced example to help spark your imagination

# Let's create a new function
def LooperPrinter(input):
	SplitInput = [] # We need to create an empty List to store all of our output into.
	for i in input.split(): # Here we are calling a new string method. We can do this thanks
				# to the import string on line 8
		SplitInput.append(i) # Now let's append the newly split(ed) strings to the List
	return SplitInput	# And finally return the list


# This is the main loop;

UserPrompt = raw_input("Input a string you want me to split apart: ")

SplitOutput = LooperPrinter(UserPrompt)

print SplitOutput

# For more info google "python string methods"
