#!/usr/bin/env python
def add(a,b):
	print a+b
	def multipli(a,b):
		print a*b
	return multipli
a=int(raw_input("please enter integer1:"))
b=int(raw_input("please enter integer2:"))
multipli(a,b)
