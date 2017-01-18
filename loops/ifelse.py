#!/usr/bin/env python
mob=raw_input("Pleas enter your month of birth:")
year=raw_input("please enter your year of birth:")
if mob == 'january' and  year in ['2012','2013']:
	print "you are the best"
	print "january is the best"
elif mob in['february','feb']:
	print "you are the second best"
	print "feb is the 2nd best"
elif mob in['march','mar']:
	print "you are the third best"
	print "march is summer"
else:
	print "you are virus"
print "not good"
