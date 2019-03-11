class people(object):
	country='china'
	@classmethod
	def getcountry(cls):
		return cls.country

	@classmethod
	def setcountry(cls,country):
		cls.country=country

p=people()
print(p.getcountry)
print(people.getcountry)

p.setcountry('japan')
print(p.getcountry())
print(people.getcountry())
