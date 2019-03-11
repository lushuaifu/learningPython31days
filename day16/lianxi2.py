def fib(times):
    n=0
    a,b=0,1
    while n<times:
        print(b)
        a,b=b,a+b
        n+=1
    return '结束'
f=fib(5)

print('*'*100)

def fib(times):
    n=0
    a,b=0,1
    while n<times:
        yield(b)
        a,b=b,a+b
        n+=1
    return '结束'
f=fib(5)
for i in f:
    print(i)