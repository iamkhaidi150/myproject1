#!/usr/bin/env python
def fib(limit):
	a=[0,1]
	for i in range(1,limit):
		b=a[-1]+a[-2]
		a.append(b)
	limit-=1
	print a
if __name__=="__main__":
	limit=int(raw_input("Please a fibonacci seq number:"))
	fib(limit)
