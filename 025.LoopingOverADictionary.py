#!/usr/bin/python
"""Using the built-in methods to manipulate types.

Joseph Kern
"""
# for loops are also great for looping over dictionaries. 

Alpha = {'A': 1, 'B': 2, 'D': 4}

# Now let's call a new mehtod for the Dictionary Object
# 'iteritems()'

for l,n in Alpha.iteritems():
	print "%s = %s" % (l,n)
