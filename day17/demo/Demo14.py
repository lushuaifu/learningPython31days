import time

class Dog(object):
    def __init__(self, func):
        print("---初始化---")
        print("func name is %s"%func.__name__)
        self.__func = func
    def __call__(self):
        print("---装饰器中的功能,验证权限，记录日志。。。---")
        self.__func()

#@Dog  #foo = Dog(foo)
def foo():
    print("----foo---")


#foo()


foo = Dog(foo)
foo()

