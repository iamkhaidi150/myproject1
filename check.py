#!/usr/bin/env python
import sys
a=sys.stdin.readlines()
print a
if len(a)==1:
	a=a[0].strip()
	a=a.split()
	print "input entered is "
	print a
else:
	hostlist=[]
	for vfiler in a:
		vfiler=vfiler.strip()
		hostlist.append(vfiler)
	print "input entered is"
	print hostlist
