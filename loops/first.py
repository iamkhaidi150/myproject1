#!/usr/bin/env python
country="United states of america"
for item in country:
	print "item is %s" %(item)
	if item.isupper():
		print "item %s is upper" %(item)
	elif item.isspace():
		print "item %s is space character" %(item)
	else:
		print "item %s is lower" %(item)
