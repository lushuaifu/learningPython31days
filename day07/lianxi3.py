def f1(a,b,c):
    print(a,b,c)
f1(1,2,3)
f1(b=1,a=2,c=3)


def f2(a,b,*,c,d):
    print(a,b,c,d)
f2(1,2,d=3,c=5)

def f3(a,b=123,*s,c,d):
    print(a,b,s,c,d)
f3(1,2,77,88,c=3,d=4)

def f4(a,b='默认',*c,**kw):
    print(a,b,c,kw)
f4(1,name='123')

num=10
def f5():
    num=20
    print(num)
def f6():
    print(num)
f5()
f6()


num=10
def f7():
    global num
    num=20
    print(num)
def f8():
    print(num)
f7()
f8()

def f9():
    global num
    num=30
    print()



