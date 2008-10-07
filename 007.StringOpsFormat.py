#!/usr/bin/python

# 007.StringOpsFormat.py -- An introduction to built in string operations, format 

phrase = "Ni!" 		# Monty Python and the Holy Grail reference
phrase  = phrase * 4	# Oh hai, what are we doing here? This is kind of cool, we are storing a new vaule of the variable INSIDE the variable.
			# This is a very common practice and quite handy

print "We are the knights who say %s" % phrase
			# When I first started learning python the previouse line used to confuse me.
			# Basically the '%s' means a string, there are other types of these too.
			# They are called string foramting codes, and they have many uses.

