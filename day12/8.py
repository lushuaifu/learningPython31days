class people(object):
	country='china'

print(people.country)
p=people()
print(p.country)

p.country='japan'
print(p.country)
print(people.country)
del p.country
print(p.country)
