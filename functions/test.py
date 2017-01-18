#!/usr/bin/env python
def validate(message):
	upper=0
	lower=0
	whitespace=0
	sspecial=0
	for element in message:
		if element.isupper():
			upper+=1
		elif element.islower():
			lower+=1
		elif element.isspace():
			whitespace+=1
		else:
			sspecial+=1
	print "your input has the below number of upper,lower,space and special symbols"
	print "upper  lower  whitespace  special"
	print "%d      %d      %d         %d" %(upper,lower,whitespace,sspecial)
message=raw_input("Please enter a message:")
validate(message)

