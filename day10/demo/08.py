'''
    创建对象的同时需要给对象赋值属性
    __init__
'''


class Dog:
    def __init__(self):
        print('__init__...')
    def __str__(self):
        print('__str__...')
        return '汪汪'

wangcai = Dog()
#ss = str(wangcai)
print(wangcai)
