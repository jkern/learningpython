#!/usr/bin/pyhton

# -- An if statement checks to see IF a condition is true or false
x = 5

# Pay special attention to how the if statements are separated and tabbed
# This is VERY important to a python program! Without the proper whitespace
# a python program will NOT RUN!

if x > 5:
	print "X is greater than 5!"
elif x >= 5:		# elif is short for else if
	print "X is greater than or equal to 5!"
elif x <= 5:		# elif statements could go on forever
	print "X is less than or equal to 5!"
else:			# This is the final condition, if all else fails at least do this 
	print "X is less than 5!"


