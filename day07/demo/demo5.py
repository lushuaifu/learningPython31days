'''
必选和默认参数
必选在前，默认在后
'''

def f1(a,b=100):
	print(a,b)

f1(1,2)
f1(111)
f1(b=1,a=2)

help(print)
print('哈哈',end='-')
print('呵呵')
