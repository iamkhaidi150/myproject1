#!/usr/bin/env python
import time,os
if __name__=="__main__":
	try:
		a=int(raw_input("Please enter a integer:"))
		b=int(raw_input("Please enter a integer:"))
		if a==0 or b==0:
			raise ZeroDivisionError("Not a Valid Input")
		name="naveen"
		print a/b
		print a/name
	except ZeroDivisionError as e:
		print "you cannot divide a integer by 0"
		print type(e)
		print dir(e)
		print e
	except TypeError:
		print "you are trying to divide a integer by string"
	except ValueError:
		print "you have not given a valid integer as input"
	else:
		print "Not sure why program exited.. Please talk to the Author of this code"
