#!/usr/bin/env python
dict_a={}
option=''
while option!="exit":
	country=raw_input("Please enter the country name:")
	capital=raw_input("Please enter the capital:")
	if dict_a.has_key(country):
		print "duplicate key"
	else:
		dict_a.setdefault(country,capital)
		option=raw_input("please enter the option C to continue exit to exit:")
print dict_a
