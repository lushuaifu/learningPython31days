class Test(object):
    def __init__(self,func):
        print('---初始化---')
        print('func name is %s'%func.__name__)
        self.__func=func
    def __call__(self):
        print('---装饰器中的功能---')
        self.__func()

@Test
def test():
    print('---test---')
test()
