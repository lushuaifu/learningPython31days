'''
    创建对象的同时需要给对象赋值属性
        def__init_(self,参数):
            self.x=参数_
  
    在对象转成字符串的时候调用__str__这个方法，将此方法的返回值返回
        def __str__(self):
            xxxxx
            xxxx
            return 字符串
'''


class Dog:
    def __init__(self,name,brand):
        print('__init__...')
        self.name = name
        self.brand = brand
    def __str__(self):
        print('__str__...')
        return '名字:%s，品种:%s'%(self.name,self.brand)


wangcai = Dog('旺财','哈士奇')
print(wangcai)
