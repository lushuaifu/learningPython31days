#函数的嵌套
def f1(a):
    print('f1...begin...')
    f2(a,a+10)
    print('f1...end...')

def f2(a,b):
    print('f2...begin...')
    print(a,b)
    print('f2...end...')
   

f1(110)

def f3(a):
    a=a+1
    print('a',a)
b=123
f3(b)
print('b',b)


def f4(a):
    a.append('123')
    print('a',a)
b=['456','789']
f4(b)
print('b',b)

'''
必选和默认参数
必选在前，默认在后
'''
def f5(a,b=10):
    print(a,b)
f5(1,2)
f5(111)
f5(b=1,a=2)
help(print)
print('哈哈',end='_')
print('呵呵')

'''
	可变参数
	参数必须加*，传递过去之后，会组合成元组
'''
def f6(*num1):
    print(num1,type(num1))
    ret=0
    for i in num1:
        ret+=i
    return ret
print(f6(1,2,3,4))

ls=[2,3,4,5,6]
t=[2,3,4,5,6,7]
print(f6(*ls))
print(f6(*t))

'''
可变参数的一种，*组成成元组，**组成字典
'''
def f7(a,b,**kw):
    print(a,b,kw)
f7(1,2,name='zs')

def f8(a,*b,**kw):
    print(a,b,kw)
f8(1,2,3,4,5,name='zs',id=123)

def f9(a,*b,**kw):
    print(a,b,kw)
f9(1,2,3,4,5,)



