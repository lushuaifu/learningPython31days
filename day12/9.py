class people(object):
	country='china'
	@classmethod
	def getcountry(cls):
		return cls.country

p=people()
p.country=1
print(p.getcountry())
print(people.getcountry())
