from time import ctime ,sleep

def timefun(func):
    def wrappedfunc():
        print('%s called at %s'%(func.__name__,ctime()))
        return func()
    return wrappedfunc

@timefun
def foo():
    print('I am foo')
@timefun
def getInfo():
    return '----haha----'
foo()
sleep(2)
foo()

print(getInfo())
