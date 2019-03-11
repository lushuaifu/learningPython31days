import types

class Person(object):
    num=0
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age

    def eat(self):
        print('eat food')

def run(self,speed):
    print('%s在移动，速度是%d km/h'%(self.name,speed))
@classmethod
def testclass(cls):
    cls.num=100
@staticmethod
def teststatic():
    print('--static method--')

p=Person('旺财','5')

a=types.MethodType(run,p)
a(100)

Person.testclass=testclass
print(Person.num)
Person.testclass()
print(Person.num)

Person.teststatic=teststatic
Person.teststatic()
