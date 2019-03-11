from time import ctime, sleep

def timefun(func):
    def wrappedfunc():
        print("%s called at %s"%(func.__name__, ctime()))
        return func()
    return wrappedfunc

@timefun
def foo():
    print("I am foo")

@timefun            #getInfo = timefun(getInfo)
def getInfo():
    return '----hahah---'

foo()
sleep(2)


ret = getInfo()
print(ret)
