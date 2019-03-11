'''
带参数的装饰器：为了传递一些参数，再通过这些参数完成一些业务逻辑
'''
def decorator(num):
    def timefun(func):
        def wrappedfunc(*args, **kwargs):
            #业务逻辑代码，比如权限，日志等等
            if num%2==0:
                print('验证权限...')
            else:
                print('记录日志...')
            #调用最终客户想调用的功能方法
            return func(*args, **kwargs)
        return wrappedfunc
    return timefun

@decorator(1)
def foo1():
    print('foo1......')

foo1()

@decorator(2)
def foo2():
    print('foo2......')

foo2()