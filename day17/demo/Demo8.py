from time import ctime, sleep

def timefun(func):
    def wrappedfunc(*args, **kwargs):
        print("%s called at %s"%(func.__name__, ctime()))
        print(args, kwargs)
        func(*args, **kwargs)
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
def foo3(**v_dict):
    print('字典参数。。。')

foo1(3,5)
foo(1,2,3)
foo2()
foo3(id=1,name='zs')




