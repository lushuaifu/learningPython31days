from time import ctime ,sleep

def timefun(func):
    def wrappedfunc(*args,**kwargs):
        print('%s called at %s'%(func.__name__,ctime()))
        print(*args,**kwargs)
        func(*args,**kwargs)
    return wrappedfunc

@timefun
def foo1(a,b):
    print(a+b)
@timefun
def foo2(a,b,c):
    print(a+b+c)
foo1(3,5)
sleep(2)
foo2(2,4,6)
