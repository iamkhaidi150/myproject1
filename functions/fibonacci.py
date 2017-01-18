#!/usr/bin/env python
import os
def fib(n):
	a=[0,1]
	for iter in range(1,n-1):
		b=a[-1]+a[-2]
		a.append(b)
	return a[n-1]
if __name__=="__main__":
	n=0
	try:
		n=int(raw_input("Please enter the fibonacci seq element:"))
		value=fib(n)
		print "%d position element in fib series is %d" %(n,value)
	except ValueError:	
		print "You have not given a valid integer, please give a valid integer"
	else:
		print "please recheck your input"
