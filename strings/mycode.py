#!/usr/bin/env python
a=raw_input("Please enter a string:")
b=""
for i in a:
	if i.isupper():
		b=b+i.lower()
	else:
		b=b+i.upper()
print "The string you entered is %s" %(b)
