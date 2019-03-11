'''
class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color

class Dog(Animal):
    def __init__(self,brand):
        self.brand = brand


wangcai = Dog('旺财')
print(wangcai.brand)
print(wangcai.name)
'''

class Animal:
    def __init__(self,name,color):
        print('init...Animal')
        self.name = name
        self.color = color

class Dog(Animal):
    def __init__(self,brand,name,color):
        print('init...Dog')
        self.brand = brand
        #super().__init__(name,color)
        Animal.__init__(self,name,color)


wangcai = Dog('哈士奇','旺财','黑白')
print(wangcai.brand)
print(wangcai.name)
