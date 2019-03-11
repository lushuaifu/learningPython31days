point1=[10,20]
point2=[20,30]
ls=[point1,point2]
print(ls)
print(ls[0][1])

for i in ls:
    for j in i:
        print(j)
print('begin......')
#定义一个函数
def de1():
    i=0
    while i<10:
        print('好好学习，天天向上。%s'%i)
        i+=1
#调用
de1()
print('over....')
print()

'''
    函数1：无参，无返
'''
def fun1():
    print('哈哈哈。。。')
fun1()

'''
函数2：有参，无返
'''
def fun2(a,b):
    '''
                    输入两个值，打印二者的和
                    a:变量1
                    b:变量2
    '''
    print(a+b)
fun2(1,2)
fun2(10,20)
help(fun2)

def fun3(a,b,c):
    print(a+b+c)
fun3(1,2,3)

'''
函数3：无参，有返
'''
def fun4():
    print('哈哈哈。。。')
    return '结束啦。。。'
fun4()
    
'''
函数4：有参，有返
关键字return值，只能放在函数最后一行
Python代码是从上往下运行的，解释性语言
'''
def fun5(a,b):
    print('fun5...')
    ret=a+b
    return ret
var=fun5(4,5)
print(var)


#输入两个数值，得到最大值
num1=int(input('第一个值'))
num2=int(input('第二个值'))

def fun6(a,b):
    if a>b:
        return a
    else:
        return b
ret=fun6(num1,num2)
print(ret)
