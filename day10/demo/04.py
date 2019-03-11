'''
    创建对象的同时需要给对象赋值属性
    __init__
'''

print('1'*20)

class Dog:
    print('2'*20)
    def __init__(self):
        print('__init__...')
        self.name = '旺财'
        self.brand = '哈士奇'
    def show(self):
        print('show...')
        print('名字:%s，品种:%s'%(self.name,self.brand))


print('3'*20)
wangcai = Dog()
wangcai.show()

xiaoqiang = Dog()
xiaoqiang.show()
print('4'*20)
