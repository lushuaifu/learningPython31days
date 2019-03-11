#ls = []
def fib(times):
    n = 0
    a, b = 0, 1
    while n < times:
        print(b)
        #ls.append(b)
        a, b = b, a + b
        n += 1
    return 'done'


ret = fib(5)
print(type(ret))
print('*'*100)

'''
虽然上面的写法可以获取对应的值
但是有问题：
    1、打印不是我们开发中无法存储值
    2、如果使用集合存储值，数量小的时候，可以。但是一旦是大数据，不行了，可能造成内存溢出

下面使用生成器的方式，并没有完全保存值，而是通过算法每次计算出需要的值
这样一旦是大数据，也不会造成内存溢出
'''

def fib(times):
    print('1......')
    n = 0
    a, b = 0, 1
    while n < times:
        print('2.1......')
        yield b
        print('2.2......')
        a, b = b, a + b
        n += 1
        print('3......')
    print('4......')
    return 'over...'


ret = fib(5)
print(type(ret))

print('ret:%s'%next(ret))
print('ret:%s'%next(ret))
print('ret:%s'%next(ret))
print('ret:%s'%next(ret))
#print('ret:%s'%next(ret))
print('ret:%s'%ret.__next__())

print('ret:%s'%next(ret))


