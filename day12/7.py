class people(object):
	address='山东'
	def __init__(self):
		self.name='xiaowang'
		self.age=20

p=people()
p.age=12
print(p.address)
print(p.name)
print(p.age)

print(people.address)
