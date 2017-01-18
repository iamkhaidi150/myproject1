#!/usr/bin/env python
class myhost(object):
	def __init__(self,name):
		self.name=name
		print "class myhost is initialized now and my name is %s" %(self.name)
	def checkstatus(self,name):
		if name=="naveen":
			print "naveen is in blr "
		elif name=="sarath":
			print "sarath is from hyd"
		elif name=="saradhi":
			print "saradhi is from amaravathi"
		else:
			print "No data present"
