#!/usr/bin/env python
def myname():
	name="ravi"
	age=33
	print "%s age is %d " %(name,age)
	def profession():
		print locals()
		print globals()
		if name=="ravi":
			print "%s is into trading" %(name)
		elif name=="naveen":
			print "%s is into IT" %(name)
		else:
			print "he is a sports person"
	return profession

if __name__=="__main__":
	name=raw_input("Please enter your name:")
	prof=myname()
	prof()
