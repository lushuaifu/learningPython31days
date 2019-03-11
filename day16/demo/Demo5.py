import  random

def fun():
    for i in range(10):
        temp = yield random.randint(1,100)
        if temp%2==0:
            print('xx算法')
        else:
            print('yy算法')

gen = fun()
#next(gen)
gen.send(None)
print(gen.send(1))
print(gen.send(2))
