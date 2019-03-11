class Dog:
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand

#实例方法
def eat(self):
    print('%s  在吃。。。。。。'%self.name)
#类方法
@classmethod
def eat1(cls):
    print('类方法。。。。。。')

#静态方法
@staticmethod
def eat2():
    print('静态方法。。。。。。')


Dog.eat = eat

wangcai = Dog('旺财','哈巴狗')
wangcai.eat()

Dog.eat1 = eat1
Dog.eat1()

Dog.eat2 = eat2
Dog.eat2()

