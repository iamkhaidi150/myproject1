#!/usr/bin/env python
name=raw_input("Please enter your name:")
for item in name:
	print name
	occurrences=name.count(item)
	print "character %s occurrs %d no of times:" %(item,occurrences)
print "end of for loop"
