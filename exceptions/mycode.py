#!/usr/bin/env python
import os,time
def getvalues():
	name=raw_input("Please enter your name:")
	try:
		age=int(raw_input("please enter your age:"))
		mylist=[]
		mylist.append(name)
		mylist.append(age)
		return mylist
	except:
		mylist=[]
		return mylist


if __name__=="__main__":
	myvalues=[]
	while len(myvalues) == 0:
		try:
			myvalues=getvalues()
		except:
			print "Input String for Name and Int for age"
			time.sleep(2)
			os.system('clear')
			myvalues=getvalues()
	print myvalues[0]
	print myvalues[1]
