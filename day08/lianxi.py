def f1(a,b,c='默认值',*d,**e):
    print(a,b,c,d,e)
f1(1,2,3,44,55,name='haha',ls=123)

def f2(a,b=110,c='默认值'):
    print(a,b,c)
f2(1,2,3)
f2(1,c=2)
print('xx',end='_')
print()
print('xx','_')

num=int(input('请输入一个数字'))
ret=1
while num>0:
    ret*=num
    num-=1
print(ret)

num=int(input('请输入一个数字'))
def f3(num):
    if num==1:
        return 1
    return num*f3(num-1)
print(f3(num))


'''
1 1 2 3 5 8 13 21 34 第200个数字

第3个 = 第2 + 第1个
第n个 = 第n-1 + 第n-2
'''
def f4(num):
    if num==1 or num==2:
        return 1
    return f4(num-1)+f4(num-2)
num=int(input('输入第几个数字'))
print(f4(num))


def f5():
    print(1)
    return 2000
    print(25)
print(f5())


def f6():
    print(1)
    return
    print(2)
print(f6())
       
