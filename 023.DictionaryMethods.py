#!/usr/bin/python
"""Using the built-in methods to manipulate types.

Joseph Kern
"""
# Dictionaries have their own bulit-in mehtods as well.
# Because Dictionaries, just like lists, are Objects as well

# Let's take and easy alphabetical example.

Alpha = {'A': 1, 'B': 2, 'D': 4}

# First we can find the value of any key by simply asking for it.
print Alpha['A']

# Second we can add new keys by giving them to the Dictionary
Alpha['C'] = 3
print Alpha

# We can just ask to see the keys (in a list)
print Alpha.keys()

# A dictionary is literally a List of Key/Values stored as Tuples. 
#	dict = ([(Key, Value),(Key,Value),(Key,Value)])
