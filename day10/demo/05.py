'''
    创建对象的同时需要给对象赋值属性
    __init__
'''


class Dog:
    def __init__(self,new_name,new_brand):
        print('__init__...')
        self.name = new_name
        self.brand = new_brand
    def show(self):
        print('名字:%s，品种:%s'%(self.name,self.brand))


wangcai = Dog('旺财','哈士奇')
wangcai.show()

xiaoqiang = Dog('小强','泰迪')
xiaoqiang.show()
