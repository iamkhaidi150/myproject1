#!/usr/bin/env python
def myname():
	print "begining of function myname"
	name="ravi"
	print hex(id(name))
	print "Hi there, How are you ?"
	print name
	print "end of function myname"
	return name

if __name__=="__main__":
	name=raw_input("Please enter your name:")
	print hex(id(name))
	name=myname()
	print name
	print hex(id(name))
