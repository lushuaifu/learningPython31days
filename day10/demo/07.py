'''
    创建对象的同时需要给对象赋值属性
    __init__
'''


class Dog:
    def __init__(self,name,brand):
        print('__init__...')
        self.name = name
        self.brand = brand
    def show(self):
        print('名字:%s，品种:%s'%(self.name,self.brand))


wangcai = Dog('旺财','哈士奇')
wangcai.show()

xiaoqiang = wangcai
xiaoqiang.name = '小强'

wangcai.show()
xiaoqiang.show()
