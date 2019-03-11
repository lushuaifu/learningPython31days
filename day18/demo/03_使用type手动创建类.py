class Dog:
    pass

Person = type('Person',(),{})

print(Dog)
print(Person)

print('*'*100)


Person = type('Person',(),{'name':'zhangsan','age':10})
print(Person.name)
print(Person.age)

print('*'*100)

Person = type('Person',(object,),{'name':'zhangsan','age':10})
print(Person.__mro__)
'''
t = ('a',)
print(type(t))
'''

print('*'*100)

def yi(self):
    print('衣......')
'''
    从这里可以看出：类里存储的都是属性，
    访问属性的时候，通过指针找到对象的内存块里的内容
'''
Person = type('Person',(object,),{'name':'zhangsan','age':10,'yi':yi})
p = Person()
p.yi()
print(hasattr(Person,'name'))
print(hasattr(Person,'name1111'))
print(hasattr(Person,'yi'))
Person.yi(1)

'''
class Dog:
    def __init__(self):
        self.name = 'xx'
    def eat(self):
        print('eat.......')
        #print(self.name)

d = Dog()
d.eat()

Dog.eat(1111)
'''