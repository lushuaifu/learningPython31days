'''
for i in [1,2,3]:
	print(i)

print(i)
'''

'''
	全局
	局部

	在代码块中，首先是从当前代码中找是否有这样名字的变量
	如果有，拿来用，
	如果没有，再从全局变量中找是否有。


	global num：
		1、先在全局中找是否有这个变量
		2、如果有，拿来用，如果没有，创建并放到全局中

		如果想在函数中修改全局变量，将变量声明位global

	建议：全局变量命名规则g_num
'''
'''
num = 10
def t1():
	num = 20
	print(num)

def t2():
	print(num)

t1()
t2()
'''
'''
num = 10
def t1():
	global num
	num = 20
	print(num)

def t2():
	print(num)

t1()
t2()
'''
'''
def t1():
	global num
	num = 20
	print(num)

def t2():
	#num=1
	print(num)

t1()
t2()
'''
'''
def t1():
	global num
	num = 20
	print(num)

def t2():
	print(num)

#num=10
t1()
#num=10
#t2()
#num=10
'''

'''
ls = [1,2,3,4]

def t1():
	ls = [1]
	#ls.append('哈哈')
	print(ls)

def t2():
	print(ls)

t1()
t2()
'''

a = 10
b = 20

def t1(a,b):
	a = a+b
	print(a,b)

def t2():
	print(a,b)

t1(a,b)
t2()