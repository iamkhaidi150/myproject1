#!/usr/bin/env python
number=int(raw_input("Please enter your digit:"))
#number+=1
for i in range(1,number):
	if i%2==0:
		print i
	else:
		continue
