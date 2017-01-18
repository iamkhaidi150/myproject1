#!/usr/bin/env python
import os,time
if __name__=="__main__":
	try:
		name=raw_input("Please enter your name:")
		age=raw_input("please enter your age:")
	except:
		print "Input String for Name and Int for age"
		age=raw_input("please enter your age:")
		time.sleep(2)
		os.system('clear')
	print name 
	print age
