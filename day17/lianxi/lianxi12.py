class Person(object):
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age

p=Person('小明','24')
print(p.name,p.age)
p.sex='male'
print(p.sex)