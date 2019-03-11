'''
	函数1：无参，无返
'''
def fun1():
	print('哈哈')

fun1()

'''
	函数2：有参，无返
	fun2有两个参数，名字分别是a,b--->形参
	fun2(1,2),调用函数，并给形参赋值 a=1,b=2 --->实参


'''
def fun2(a,b):
	'''
		输入两个值，打印二者的和
		a:变量1
		b:变量2
	'''
	print(a+b)

fun2(1,2)
fun2(1,10)
#fun2(10)
help(fun2)

'''
	函数3：无参，有返
	关键字 return 值，只能放在函数的最后一行
'''

def fun3():
	print('fun3()...1')
	return '酱油'
	#print('fun3()...2')

var = fun3()
print(var)


'''
	函数4：有参，有返
	关键字 return 值，只能放在函数的最后一行
	python代码是从上往下一行一行运行，解释性语言
'''

def fun4(a,b):
	print('fun4......')
	ret = a+b
	return ret

var = fun4(1,2)
print(var)

#输入两个数值，得到最大值
num1 = int(input('第一个值：'))
num2 = int(input('第一个值：'))


def fun5(a,b):
	'''求两个值的最大值'''
	if a>b:
		return a
	else:
		return b

ret = fun5(num1,num2)

print(ret)


