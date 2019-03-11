class people(object):
	country='china'
	@staticmethod
	def getcountry():
		return people.country

print(people.getcountry())
