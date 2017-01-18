class mycar(object):
	def __init__(self,car):
		self.car=car
	def cartype(self,owner):
		if self.car=="swift":
			print "it is %s's maruti suzuki" %(owner)
		elif self.car=="city":
			print "it is naveen's honda city"
		elif self.car=="corolla":
			print "it ia toyota"
		elif self.car=="i20":
			print "it is a Hyundai"
		else:
			print "check google"
	def carweight(self):
		if self.car=="swift":
			print "car weight is 1190 kg"
		elif self.car=="i20":
			print "car weight is 1290 kg"
		elif self.car=="city":
			print "car weight is 1500 kg"
		elif self.car=="corolla":
			print "car weight is 1600 kg"
		else:
			print "check with the showroom"
