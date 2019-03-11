def fib(times):
    n=0
    a,b=0,1
    while n<times:
        yield(b)
        a,b=b,a+b
        n+=1
    return '结束'
f=fib(5)
while 1:
    try:
        x=next(f)
        print('value:%d'%x)
    except StopIteration as e:
        print('生成器返回值：%s'%e.value)
        break