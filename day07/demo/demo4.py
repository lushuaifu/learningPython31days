#定义函数
def f1(a):
	a.append('王二')
	print('f1()......')
	print('a',a)

b = ['张三','李四']
f1(b)
print('b',b)

'''
def f1(b):
	b+=1
	print('f1()......')
	print('b',b)

a = 123
f1(a)
print('a',a)
'''


