class Dog(object):
    def __init__(self):
        print('__init__......')
    def __new__(cls):
        print('__new__......')
        obj = object.__new__(cls)
        print('obj:%s,cls:%s'%(obj,cls))
        return obj

'''
    1、调用__new__方法，这个__new__方法在object中返回一个对象
    2、调用__init__方法，将1中的返回对象传递给__init__中的self
    3、返回这个对象
'''
wangcai = Dog()


print(wangcai)