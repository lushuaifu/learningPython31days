import time

class DecoratorClass(object):
    def __init__(self, func):
        #print("---初始化---")
        #print("func name is %s"%func.__name__)
        self.__func = func
    def __call__(self,*args,**kwargs):
        print("---装饰器中的功能,验证权限，记录日志。。。---")
        print(args)
        print(kwargs)
        return self.__func(*args,**kwargs)

@DecoratorClass
def foo1():
    print("----foo1---")

@DecoratorClass
def foo2(a,b):
    print("----foo2---")
    return a+b

foo1()
print(foo2(1,2))

