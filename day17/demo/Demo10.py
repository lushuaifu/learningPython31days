from time import ctime, sleep

def timefun(func):
    def wrappedfunc(*args, **kwargs):
        #业务逻辑代码，比如权限，日志等等
        print("%s called at %s"%(func.__name__, ctime()))
        print(args, kwargs)
        #调用最终客户想调用的功能方法
        return func(*args, **kwargs)
    return wrappedfunc

@timefun
def foo(a, b,c):
    print(a+b)

@timefun
def foo1(a, b):
    print(a+b)

@timefun
def foo2():
    print('没有参数。。。')
@timefun
def foo3(**kwargs):
    print('字典参数。。。')

@timefun
def foo4(a,b):
    return '----hahah---'

foo1(3,5)
foo(1,2,3)
foo2()
foo3(id=1,name='zs')

#print(foo4(1,2))



