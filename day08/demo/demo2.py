'''
	递归：
		1、函数本身调用本身
		2、有反复执行的过程，
		3、有退出的条件。


	求5的阶乘
	5! = 5*4*3*2*1
	5! = 5*4!
	4！=4*3！
	求20的阶乘
'''


'''
办法1：使用循环
num = int(input('输入数字:'))
#存储结果
ret = 1

i=num
while i>0:
	ret*=i
	i-=1

print(ret)
'''


def funRecursion(num):
	'''输入一个数字num,返回num的阶乘'''
	if(num==1):
		return 1
	else:
		return num*funRecursion(num-1)

ret = funRecursion(5)
print(ret)


'''
1 1 2 3 5 8 13 21 34 第200个数字

第3个 = 第2 + 第1个
第n个 = 第n-1 + 第n-2
'''

'''
a,b = 1,1
num = int(input('输入第几个数字:'))
while a<num:
	xx
'''

def funRecursion(num):
	'求第几个数字的值'
	if num==1 or num==2:
		return 1
	return funRecursion(num-1)+funRecursion(num-2)

num = int(input('输入第几个数字:'))
ret = funRecursion(num)
print(ret)


'''
def f():
	print(1)
	return 2000
	print(2)

print(f())
'''
'''
def f():
	print(1)
	return
	print(2)

print(f())
'''