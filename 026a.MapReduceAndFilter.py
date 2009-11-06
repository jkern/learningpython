#!/usr/bin/python
""" Map, Reduce, and Filter, are functions that allow fast iteration over lists. And they're fun."""

# To begin with, let's start with a list.

newList = range(10)

# Now I have newList = [0,1,2,3,4,5,6,7,8,9]
# Using map, we can add 1 to each.

print map(lambda x: x + 1, newList)

# Now newList = [1,2,3,4,5,6,7,8,9,10]
# Next let's use filter to only show the odd numbers in newList

print filter(lambda x: x % 2, newList)

# Using reduce we can add list elements together

print reduce(lambda x,y: x + y , newList)

# Finally, let's roll these into an uber-function!
# Let's add one to each of the numbers, remove the even numbers, then add the remaining together

print reduce(lambda x,y: x+y, map(lambda x: x + 1, filter(lambda x: x % 2, newList)))
