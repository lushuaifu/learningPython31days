'''
如果装饰运行完毕之后，如果后面还有装饰器，交给下一个装饰器
直到没有装饰器了，执行功能代码
'''

def decorator1(fn):
    def inner1():
        print('decorator1_inner1  begin...')
        #if False:
        fn()
        print('decorator1_inner1  end...')
    return inner1


def decorator2(fn):
    def inner2():
        print('decorator2_inner2  begin...')
        fn()
        print('decorator2_inner2  end...')
    return inner2

@decorator1
@decorator2
def myFunc():
    print('myFunc......')


myFunc()