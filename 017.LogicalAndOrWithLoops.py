#!/usr/bin/python
"""More if statements, this is where it gets fun!

Joseph Kern
"""

# Try different values for y
y = 3

if y == 3:	# this does NOT make y = 3 it checks to see if y is equivalent to 3
	print "Y is equal to 3!"
else:
	print "Y is NOT equal to 3!"

if (y > 0) and (y < 10):
	print "Y is greater than 0 and less than 10!"
elif y >= 10:
	print "Y is 10 or more!"
else:
	print "Y is less than 0!"

