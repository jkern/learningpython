#!/usr/bin/python

def PriceListDict(filename):
	"""PriceListDict(File Path to Prices file)

	Price file should be formatted like this
		
		Item:value:
		Item:value:
	"""
	values = {}
	print "Loading from ", filename, "...",
	for line in open(filename):
	#split up to 2 times (i.e., in correspondence to two occurrences of colon)
		head, rewrite = line.split(':',2)[:2]
	#Convert the strings into floats
		rewrite = float(rewrite)
	# is keyed by a string equal to "head", creating an empty list entry if it
	# doesn't already exist. The "append" part then operates on the string
	# referred to by the "rewrite" variable, adding it to the (possibly empty)
	# list keyed by "head".
		values.setdefault(head, []).append(rewrite)
	# Print a period for each dict record in filename
	print "Done!"
	return values

if __name__ == '__main__':
	
	prices = PriceListDict('prices.txt')
	print prices
