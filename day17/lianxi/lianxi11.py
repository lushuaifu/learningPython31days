from time import ctime,sleep

def timefun_arg(pre='hello'):
    def timefun(func):
        def wrappedfunc():
            print('%s called at %s %s'%(func.__name__,ctime(),pre))
            return print(func())

        return wrappedfunc
    return timefun

@timefun_arg('wangcai')
def foo():
    print('I am foo')
    return '--我出来啦。。。--'

foo()



