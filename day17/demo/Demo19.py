import types

class Dog:
    pass


def eat(self):
    print('吃。。。。。。')

wangcai = Dog()
xiaoqiang = Dog()
#给某一个对象绑定一个方法
wangcai.eat = types.MethodType(eat,wangcai)
wangcai.eat()

#xiaoqiang.eat()


