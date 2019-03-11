''' 
类属性 
    1、每个对象都有这个属性
    2、如果通过 类修改的，所有的都会被修改
    3、如果通过 对象修改的，只会修改当前这一个对象的，其它并不受影响
    4、可以通过 类.类属性  访问


实例属性
    1、每个对象的实例属性可能不同，只要通过self.属性，就拥有
    2、实例化是属于当前对象的，与另一对象的无关
    3、一个实例属性被修改，不影响其它对象的
    4、通过 self.实例属性 访问
'''

class Student:
   def __init__(self,name):
       self.name = name
   def f1(self,age):
       self.age = age

s1 = Student('旺财')
s1.f1(100)
print(dir(s1))

print(s1.name)

s2 = Student('小强')

print(s2.name)

s2.name = 'xx'

print(s1.name)
print(s2.name)

print(Student.name)


